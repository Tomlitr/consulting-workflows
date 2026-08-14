#!/usr/bin/env python3
"""Upload the page copy from 10-seiten-de.md / 20-seiten-en.md to WordPress as DRAFTS.

Usage:
  export WP_URL="https://www.tomklein.de"
  export WP_USER="<wp username>"
  export WP_APP_PASSWORD="<application password>"   # wp-admin -> Users -> Profile -> Application Passwords
  python3 publish_to_wp.py [--publish]

Creates/updates one WordPress page per "# Seite:" / "# Page:" section, keyed by slug.
Everything is uploaded as status=draft unless --publish is given, so nothing goes
live without review. Requires: requests (pip install requests).
"""
import os
import re
import sys
import html
import pathlib

try:
    import requests
except ImportError:
    sys.exit("pip install requests")

HERE = pathlib.Path(__file__).parent
FILES = ["10-seiten-de.md", "20-seiten-en.md"]

WP_URL = os.environ.get("WP_URL", "").rstrip("/")
WP_USER = os.environ.get("WP_USER", "")
WP_PASS = os.environ.get("WP_APP_PASSWORD", "")
STATUS = "publish" if "--publish" in sys.argv else "draft"

if not (WP_URL and WP_USER and WP_PASS):
    sys.exit("Set WP_URL, WP_USER, WP_APP_PASSWORD environment variables first.")

AUTH = (WP_USER, WP_PASS)
API = f"{WP_URL}/wp-json/wp/v2"


def md_inline(s: str) -> str:
    s = html.escape(s, quote=False)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\*(.+?)\*", r"<em>\1</em>", s)
    s = re.sub(r"`(.+?)`", r"<code>\1</code>", s)
    return s


def md_to_html(body: str) -> str:
    out, para, ul = [], [], False

    def flush_para():
        nonlocal para
        if para:
            out.append("<p>" + md_inline(" ".join(para)) + "</p>")
            para = []

    def flush_ul():
        nonlocal ul
        if ul:
            out.append("</ul>")
            ul = False

    for raw in body.splitlines():
        line = raw.rstrip()
        if not line.strip():
            flush_para()
            flush_ul()
            continue
        if line.startswith("> "):  # editorial notes -> skip, they are not page copy
            flush_para()
            flush_ul()
            continue
        m = re.match(r"^(#{2,4})\s+(.*)$", line)
        if m:
            flush_para()
            flush_ul()
            level = min(len(m.group(1)), 4)
            title = re.sub(r"^H\d\s*[—-]\s*", "", m.group(2))
            out.append(f"<h{level}>{md_inline(title)}</h{level}>")
            continue
        if re.match(r"^[-*]\s+", line):
            flush_para()
            if not ul:
                out.append("<ul>")
                ul = True
            out.append("<li>" + md_inline(re.sub(r"^[-*]\s+", "", line)) + "</li>")
            continue
        para.append(line.strip())
    flush_para()
    flush_ul()
    return "\n".join(out)


def parse_pages(text: str):
    """Yield (title, slug, html_body) per '# Seite:'/'# Page:'/'# Baustein:' section."""
    sections = re.split(r"^# (?=Seite:|Page:|Baustein:)", text, flags=re.M)
    for sec in sections[1:]:
        head, _, body = sec.partition("\n")
        if head.startswith("Baustein:"):
            continue  # snippets, not pages
        slug_m = re.search(r"`/?([a-z0-9\-/]*?)/?`\s*$", head.strip())
        h1_m = re.search(r"^## H1\s*\n(.+)$", body, flags=re.M)
        if not slug_m or not h1_m:
            print(f"  ! skipped (no slug/H1): {head.strip()[:60]}")
            continue
        # '/beratung/organisationsdesign/' -> 'organisationsdesign' (parent set in wp-admin)
        # '/en/services/' -> 'en-services' so EN drafts never overwrite DE pages;
        # with Polylang/WPML assign the language and drop the 'en-' prefix on review.
        path_ = slug_m.group(1).strip("/")
        if not path_:
            slug = "startseite"
        elif path_ == "en":
            slug = "en-home"
        elif path_.startswith("en/"):
            slug = "en-" + path_.split("/")[-1]
        else:
            slug = path_.split("/")[-1]
        title = h1_m.group(1).strip()
        # drop the H1 block itself from the body
        body = re.sub(r"^## H1\s*\n.+?\n", "", body, count=1, flags=re.M)
        yield title, slug, md_to_html(body)


def upsert(title: str, slug: str, content: str):
    r = requests.get(f"{API}/pages", auth=AUTH,
                     params={"slug": slug, "status": "any", "per_page": 1}, timeout=30)
    r.raise_for_status()
    hits = r.json()
    payload = {"title": title, "slug": slug, "content": content, "status": STATUS}
    if hits:
        r = requests.post(f"{API}/pages/{hits[0]['id']}", auth=AUTH, json=payload, timeout=30)
        verb = "updated"
    else:
        r = requests.post(f"{API}/pages", auth=AUTH, json=payload, timeout=30)
        verb = "created"
    r.raise_for_status()
    print(f"  {verb} [{STATUS}] /{slug}/  ({r.json()['link']})")


def main():
    print(f"Target: {API}  as {WP_USER}  status={STATUS}")
    for fname in FILES:
        path = HERE / fname
        if not path.exists():
            print(f"! missing {fname}")
            continue
        print(f"-- {fname}")
        for title, slug, content in parse_pages(path.read_text(encoding="utf-8")):
            upsert(title, slug, content)
    print("Done. Review the drafts in wp-admin before publishing; "
          "menus, redirects and plugin deactivation are manual steps (see 00-*.md).")


if __name__ == "__main__":
    main()
