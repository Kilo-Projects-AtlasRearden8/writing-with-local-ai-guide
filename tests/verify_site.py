#!/usr/bin/env python3
"""Verification for the Writing with Local AI manual + static site.

Checks:
- All expected files exist
- LICENSE copyright line is exact
- README credits Asdale Dynamics, LLC
- HTML files have valid structure and internal links resolve
- Markdown files exist with required headings
- No secrets/API-key-looking strings in any tracked file
"""
import html
import os
import re
import sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXPECTED_FILES = [
    "LICENSE",
    "README.md",
    "docs/index.md",
    "docs/01-setup-ollama.md",
    "docs/02-model-choices.md",
    "docs/03-drafting.md",
    "docs/04-editing.md",
    "docs/05-brainstorming.md",
    "docs/06-privacy.md",
    "docs/07-prompt-templates.md",
    "site/index.html",
    "site/setup.html",
    "site/models.html",
    "site/drafting.html",
    "site/editing.html",
    "site/brainstorming.html",
    "site/privacy.html",
    "site/templates.html",
    "site/css/style.css",
    "site/js/site.js",
    "STATUS.md",
]
HTML_FILES = [f for f in EXPECTED_FILES if f.endswith(".html")]
MD_FILES = [f for f in EXPECTED_FILES if f.endswith(".md")]

errors = []
warnings = []


def check(condition, message):
    if not condition:
        errors.append(message)


def exists(path):
    return os.path.isfile(os.path.join(ROOT, path))


# 1. Expected files exist
for f in EXPECTED_FILES:
    check(exists(f), f"Missing expected file: {f}")

# 2. LICENSE copyright line exact
license_text = ""
if exists("LICENSE"):
    with open(os.path.join(ROOT, "LICENSE"), encoding="utf-8") as fh:
        license_text = fh.read()
check(
    "Copyright (c) 2026 Asdale Dynamics, LLC" in license_text.splitlines(),
    "LICENSE missing exact copyright line: Copyright (c) 2026 Asdale Dynamics, LLC",
)
check(license_text.startswith("MIT License\n"), "LICENSE should start with 'MIT License'")

# 3. README credits Asdale Dynamics, LLC
readme_text = ""
if exists("README.md"):
    with open(os.path.join(ROOT, "README.md"), encoding="utf-8") as fh:
        readme_text = fh.read()
check("Asdale Dynamics, LLC" in readme_text, "README does not credit Asdale Dynamics, LLC")

# 4. No secrets/API-key-looking strings anywhere
secret_patterns = [
    r"sk-[A-Za-z0-9]{20,}",          # OpenAI-style keys
    r"api[_-]?key[^A-Za-z]{0,5}[A-Za-z0-9]{20,}",  # generic API keys
    r"(?i)password\s*[:=]\s*\S+",    # passwords
]
all_text = ""
for root, _dirs, files in os.walk(ROOT):
    if "/.git" in root:
        continue
    for fn in files:
        path = os.path.join(root, fn)
        try:
            with open(path, encoding="utf-8", errors="ignore") as fh:
                all_text += fh.read() + "\n"
        except OSError:
            pass
for pat in secret_patterns:
    matches = re.findall(pat, all_text)
    check(not matches, f"Possible secret found matching {pat!r}: {matches[:3]}")

# 5. HTML structure: parse each HTML file
class SimpleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.open_tags = []
        self.unclosed = []

    def handle_starttag(self, tag, attrs):
        if tag not in ("meta", "link", "br", "hr", "img", "input"):
            self.open_tags.append(tag)

    def handle_endtag(self, tag):
        if self.open_tags and self.open_tags[-1] == tag:
            self.open_tags.pop()
        else:
            self.unclosed.append(tag)

    def mismatches(self):
        return list(reversed(self.open_tags)) + self.unclosed


for html_file in HTML_FILES:
    path = os.path.join(ROOT, html_file)
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    parser = SimpleParser()
    parser.feed(content)
    mismatches = parser.mismatches()
    check(
        not mismatches,
        f"{html_file}: unbalanced tags {mismatches[:5]}",
    )
    check("<!DOCTYPE html>" in content.upper() or "<!doctype html>" in content.lower(),
          f"{html_file}: missing DOCTYPE")
    check('<meta charset="UTF-8">' in content, f"{html_file}: missing charset")
    check('href="css/style.css"' in content, f"{html_file}: missing stylesheet link")
    check('src="js/site.js"' in content, f"{html_file}: missing script link")
    check("Asdale Dynamics, LLC" in content, f"{html_file}: missing Asdale Dynamics, LLC credit")
    check("Nothing" in content or "never" in content.lower(), f"{html_file}: privacy language missing")

# 6. Internal HTML links resolve
link_pattern = re.compile(r'href="([^"]+)"')
for html_file in HTML_FILES:
    path = os.path.join(ROOT, html_file)
    with open(path, encoding="utf-8") as fh:
        content = fh.read()
    here = os.path.dirname(path)
    for href in link_pattern.findall(content):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        target = href.split("#")[0]
        if not target:
            continue
        target_path = os.path.normpath(os.path.join(here, target))
        check(
            os.path.isfile(target_path),
            f"{html_file}: broken link to {href} (resolved {target_path})",
        )

# 7. Markdown headings present
expected_headings = {
    "docs/01-setup-ollama.md": ["Set Up Ollama"],
    "docs/02-model-choices.md": ["Model Choices"],
    "docs/03-drafting.md": ["Drafting"],
    "docs/04-editing.md": ["Editing"],
    "docs/05-brainstorming.md": ["Brainstorming"],
    "docs/06-privacy.md": ["Privacy"],
    "docs/07-prompt-templates.md": ["Prompt Templates"],
}
for md_file, headings in expected_headings.items():
    if not exists(md_file):
        continue
    with open(os.path.join(ROOT, md_file), encoding="utf-8") as fh:
        text = fh.read()
    for h in headings:
        check(
            any(re.search(rf"^#+\s+.*{re.escape(h)}", line, re.MULTILINE) for line in text.split("\n")),
            f"{md_file}: missing heading containing '{h}'",
        )

# 8. No .github/workflows
check(not exists(".github/workflows/.keep") and not any(
    p.endswith(".github/workflows") or ".github/workflows/" in p
    for p, _ in [(os.path.join(r, f), f) for r, d, fs in os.walk(ROOT) for f in fs]
), "No .github/workflows files should exist")

print(f"{'PASS' if not errors else 'FAIL'}: {len(errors)} error(s), {len(warnings)} warning(s)")
for e in errors:
    print(f"  ERROR: {e}")
for w in warnings:
    print(f"  WARN:  {w}")
sys.exit(1 if errors else 0)
