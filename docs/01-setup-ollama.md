# 1. Set Up Ollama (Step by Step)

Ollama is a free program that runs AI models locally on your own computer. Think
of it like iTunes for AI: Ollama downloads and plays models, and your writing
never leaves your machine.

## Step 1: Download Ollama

1. Go to [ollama.com](https://ollama.com).
2. Click **Download** and choose your computer: Mac, Windows, or Linux.
3. Install Ollama like any other app (open the installer and follow the prompts).

Once installed, Ollama runs quietly in the background. You do not need to keep
the Ollama website open.

## Step 2: Open your terminal

Ollama is controlled from your computer's command line (Terminal on Mac,
PowerShell or Command Prompt on Windows, Terminal on Linux).

- **Mac:** press `Command + Space`, type `Terminal`, press Enter.
- **Windows:** press the Windows key, type `PowerShell`, press Enter.
- **Linux:** open your terminal application.

## Step 3: Check that Ollama is working

Type this in your terminal and press Enter:

```bash
ollama --version
```

You should see something like:

```bash
ollama version is 0.5.7
```

If you see `ollama: command not found`, Ollama may not be installed or your
terminal may need to be restarted. Restart your terminal and try again.

## Step 4: Pull your first writing model

Models are the brains Ollama runs. To download a small, fast model good for
writing, type:

```bash
ollama pull llama3.2:3b
```

This downloads the model to your computer. It may take a few minutes depending
on your internet speed. Once downloaded, the model stays on your computer — you
do not need internet to use it afterward.

Other good first models (see [02. Model choices](./02-model-choices.md)):

```bash
ollama pull phi3:mini
ollama pull mistral-nemo:12b
```

## Step 5: Run your first prompt

Start a chat with the model:

```bash
ollama run llama3.2:3b
```

Type something like:

```text
Write a short, friendly opening paragraph for a letter to a new neighbor.
```

Press Enter. The model will type out a reply on your screen, letter by letter,
entirely on your computer. Type `/bye` to exit the chat.

## Step 6: Try a one-shot prompt

You do not need to start a chat. Run a single prompt and exit:

```bash
ollama run llama3.2:3b "Write a three-sentence bedtime story about a curious raccoon."
```

## What just happened?

- Ollama downloaded a model file to your computer (usually a few gigabytes).
- When you run a prompt, your computer's processor (and graphics chip, if available) does the thinking.
- Your words never leave your machine. There is no account to create and no API key to buy.

## Troubleshooting

| Problem | What to try |
| --------- | ------------- |
| `ollama: command not found` | Reinstall Ollama, then restart your terminal |
| Pull takes a long time | The model is a few gigabytes; leave your computer awake and on Wi-Fi until it finishes |
| Model replies slowly | Your computer is doing all the work. A smaller model (like `llama3.2:1b` or `phi3:mini`) will be faster |
| "Not enough memory" | Close other apps and try a smaller model |

## Next step

Read [02. Model choices](./02-model-choices.md) to pick the right model for your
writing, or jump to [03. Drafting](./03-drafting.md).

---

Published by **Asdale Dynamics, LLC**. MIT License. Copyright (c) 2026 Asdale
Dynamics, LLC.
