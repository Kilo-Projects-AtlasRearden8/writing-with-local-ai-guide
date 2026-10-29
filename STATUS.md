STATUS — Writing with Local AI via Ollama (Asdale Dynamics, LLC)
================================================================

What was built
--------------
A beginner manual and static HTML site for writing with local AI models via Ollama,
targeted at non-technical writers (authors, nurses, small-business owners, students).
Everything runs locally; nothing leaves your computer.

Files:
- LICENSE — MIT License, Copyright (c) 2026 Asdale Dynamics, LLC
- README.md — overview, contents, quick start, privacy promise, credit to Asdale Dynamics, LLC
- docs/index.md — table of contents
- docs/01-setup-ollama.md — step-by-step Ollama install and first prompt
- docs/02-model-choices.md — model sizes and recommended starter models
- docs/03-drafting.md — drafting stories, articles, letters
- docs/04-editing.md — proofreading, clarity, tone, pacing edits
- docs/05-brainstorming.md — titles, plots, characters, ideas
- docs/06-privacy.md — privacy promise and practical steps
- docs/07-prompt-templates.md — eight printable fill-in prompt templates
- site/ — static HTML version of the manual (index + 7 pages), css/style.css, js/site.js
  - Print styles on templates.html: press Ctrl+P/Cmd+P to print the prompt cards
- tests/verify_site.py — verification script (file inventory, LICENSE/README credit,
  HTML structure, internal links, markdown headings, secret scan)
- .markdownlint.json — project lint config (MD013 line-length relaxed so example
  commands stay copy-pasteable; run `markdownlint docs/*.md` from the project root)
- STATUS.md — this file

How to run it
-------------
Markdown manual: read docs/*.md in any text editor or Markdown viewer.
Static site: open site/index.html in any browser. No build step, no server, no
internet required after the pages are downloaded.
Ollama (separate install): https://ollama.com — then `ollama pull llama3.2:3b`
and `ollama run llama3.2:3b "your prompt"`.

Verification results
--------------------
- markdownlint docs/*.md: PASS (exit 0)
- tests/verify_site.py: PASS (exit 0) — covers file inventory, exact LICENSE
  copyright line "Copyright (c) 2026 Asdale Dynamics, LLC", Asdale Dynamics, LLC
  credit in README and every site page, balanced HTML tags, DOCTYPE/charset/
  stylesheet/script on all pages, resolving internal links, required markdown
  headings, no secrets or API-key-looking strings.
- No .github/workflows files present. No secrets, API keys, or personal data in
  any file. Ollama was not installed in this environment, so the ollama commands
  were not executed end-to-end; they are written from the official Ollama docs.

Known gaps
----------
- Ollama is not installed here, so `ollama pull` / `ollama run` steps were not
  executed end-to-end (verified as documentation steps only).
- Site pages are static HTML linked to docs/ markdown; no search or dark mode.
- Prompt templates are printable cards, not editable web forms.
- No CI workflows (intentionally omitted per project rules).

Published by Asdale Dynamics, LLC (Indiana, formed October 2026).
MIT License. Copyright (c) 2026 Asdale Dynamics, LLC.