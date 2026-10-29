# Writing with Local AI Models via Ollama

A beginner-friendly manual and static site for writing with AI models that run **entirely on your own computer**. Drafting, editing, brainstorming, and privacy — step by step, in plain English, with nothing ever leaving your machine.

> **Nothing leaves your computer.** No account. No API key. No cloud. Your words stay yours.

---

## Who this is for

This guide was written for anyone who wants to write with AI without sending their words to a cloud service: authors, nurses, students, small-business owners, and anyone curious about local AI. **No coding required.**

It is published by **Asdale Dynamics, LLC**, an Indiana LLC focused on beginner-friendly AI education, books, and practical tools. Learn more at [dylanasdale.github.io](https://dylanasdale.github.io).

---

## What you'll learn

| Section | Description |
|---------|-------------|
| [1. Set Up Ollama](docs/01-setup-ollama.md) | Install Ollama, pull a model, run your first prompt — step by step |
| [2. Model Choices](docs/02-model-choices.md) | Pick the right local model for writing (size, speed, quality) |
| [3. Drafting](docs/03-drafting.md) | Use a local model to draft stories, articles, and letters |
| [4. Editing](docs/04-editing.md) | Edit and polish your own writing with local AI |
| [5. Brainstorming](docs/05-brainstorming.md) | Generate titles, plots, characters, and ideas locally |
| [6. Privacy](docs/06-privacy.md) | Why nothing leaves your computer, and what that means |
| [7. Prompt Templates](docs/07-prompt-templates.md) | Printable templates you can fill in by hand |

**Also available:** A static HTML version of this manual in `site/` — open `site/index.html` in any browser. No server required.

---

## Quick Start (3 minutes)

1. **Install Ollama** — Go to [ollama.com](https://ollama.com), download for your system (Mac/Windows/Linux), and install like any app.
2. **Pull a writing model** — Open your terminal and run:
   ```bash
   ollama pull llama3.2:3b
   ```
   (This downloads a small, fast model good for writing. Takes a few minutes.)
3. **Write your first prompt** — In the same terminal:
   ```bash
   ollama run llama3.2:3b "Write a friendly opening paragraph for a letter to a new neighbor."
   ```
4. **That's it!** The model replies on your screen, entirely on your computer. Type `/bye` to exit.

---

## How to use this manual

1. **Start here:** Read [docs/01-setup-ollama.md](docs/01-setup-ollama.md) to install Ollama and pull a writing model.
2. **Build skills:** Work through [Drafting](docs/03-drafting.md), [Editing](docs/04-editing.md), and [Brainstorming](docs/05-brainstorming.md) in order.
3. **Keep templates handy:** Print [docs/07-prompt-templates.md](docs/07-prompt-templates.md) (or open `site/templates.html` and press `Ctrl+P` / `Cmd+P`) and keep the templates beside your keyboard.
4. **Prefer a website?** Open `site/index.html` in your browser — same content, clickable navigation, works offline.

---

## Privacy promise

Every model mentioned in this guide runs locally through Ollama. Your writing, your prompts, and your data **stay on your computer**. Nothing is uploaded. No API key is required. Works offline once a model is downloaded.

---

## License

MIT License. Copyright (c) 2026 Asdale Dynamics, LLC. See [LICENSE](LICENSE).

---

## Credit

Created and published by **Asdale Dynamics, LLC** (Indiana, formed October 2026). Founded by Dylan Asdale, registered nurse turned AI author of *The Massive AI Manual* and the hub site [dylanasdale.github.io](https://dylanasdale.github.io). AI explained "like a friend would": plain English, step by step, never condescending.