# 2. Model Choices for Writing

Ollama lets you run many different models. Each model is a file on your
computer, and you can switch between them any time. This section helps you pick
a writing model and understand what the names mean.

## What the model names mean

A model name like `llama3.2:3b` breaks down as:

- **llama3.2** — the model family (the architecture, like an engine type)
- **3b** — the size: roughly 3 billion parameters. Bigger usually means smarter but slower and more memory-hungry

Common sizes you will see:

| Size | What it means | Good for |
| ------ | --------------- | ---------- |
| 1b – 3b | Small, fast, runs on almost anything | Short emails, simple rewrites, brainstorming |
| 7b – 8b | Solid all-rounder | Stories, articles, letters, editing |
| 12b – 14b | Stronger writing, needs more memory | Longer fiction, careful editing |
| 32b+ | Very strong, needs a powerful computer | Complex writing projects (if your computer can handle it) |

## Recommended starter models

Pull any of these with `ollama pull <name>`:

| Model | Best for | Approximate download |
| ------- | ---------- | ---------------------- |
| `llama3.2:3b` | Fast everyday writing, emails, short drafts | ~2 GB |
| `llama3.2:1b` | Very fast, older or slower computers | ~1.3 GB |
| `phi3:mini` | Microsoft's small model, good at following instructions | ~2.3 GB |
| `mistral-nemo:12b` | Stronger storytelling and editing | ~9 GB |
| `llama3.1:8b` | A popular, capable all-rounder | ~4.7 GB |

## How to choose

1. **Start small.** `llama3.2:3b` or `phi3:mini` downloads quickly and runs on most computers.
2. **Try it.** Run a prompt you actually care about (a scene, a letter, a blog intro).
3. **Upgrade if you need to.** If the writing feels too simple, pull a bigger model like `mistral-nemo:12b` and try the same prompt again.

You can have as many models installed as your hard drive can hold, and switching
between them is just a new `ollama run` command.

## Running a model

Start a chat:

```bash
ollama run llama3.2:3b
```

Or send one prompt:

```bash
ollama run phi3:mini "Rewrite this sentence to be warmer: I am writing to inform you that your application was received."
```

## Managing models

List models installed on your computer:

```bash
ollama list
```

Remove a model you no longer use (to free space):

```bash
ollama rm llama3.2:1b
```

See all models Ollama can download:

```bash
ollama list
```

then browse [ollama.com/library](https://ollama.com/library) in your browser.

## Memory tips

- Close heavy apps (web browsers with many tabs, video editors) before running larger models.
- If your computer gets hot or loud, that is normal — it is working hard. Switch to a smaller model if it bothers you.
- Models stay on your computer after you download them. You do not need internet to write with them.

---

Published by **Asdale Dynamics, LLC**. MIT License. Copyright (c) 2026 Asdale
Dynamics, LLC.
