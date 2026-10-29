# 6. Privacy: Nothing Leaves Your Computer

This manual is built around one rule: **your writing stays on your computer.**

When you use Ollama with a local model, the model runs on your processor — not
on someone else's server. There is no account to create, no login, and no API
key. Your prompts, your drafts, your unpublished manuscript, and your personal
letters never leave your machine.

## What "local" means here

| Cloud AI tools | Ollama on your computer |
| --- | --- |
| Your text is sent over the internet | Your text never leaves your machine |
| You need an account and often a credit card | No account, no payment |
| A company may store or review your input | Only you can see what you type |
| You need internet to write | Works offline after you download a model |
| The service can change or shut down | The model stays on your hard drive |

## What this guide does NOT do

- It never asks you to paste an API key.
- It never asks you to create an account.
- It never sends your writing to a website.
- It does not collect your email, name, or anything else.

## Practical privacy steps

1. **Download models from ollama.com only.** The official library is the safest source.
2. **Work offline.** Once a model is downloaded (`ollama pull`), you can turn off Wi-Fi and it still works.
3. **Keep your drafts in files on your computer.** Use any text editor or word processor you like.
4. **Delete models you no longer need:** `ollama rm <model-name>`

## What Ollama does see

Ollama itself is installed on your computer, so it can see the models you run
and the prompts you type — the same way any program you install can see what you
do with it. Ollama does not upload your prompts as part of normal operation. If
you want to be extra cautious, disconnect from the internet after downloading
your model.

## A note on healthcare workers

If you are a nurse or other healthcare worker experimenting with AI (see the
healthcare section in the README), never paste real patient information into any
AI tool, local or otherwise. Local AI keeps your words on your machine, but
patient privacy rules still apply. This guide is for education only, never
medical advice.

---

Published by **Asdale Dynamics, LLC**. MIT License. Copyright (c) 2026 Asdale
Dynamics, LLC.
