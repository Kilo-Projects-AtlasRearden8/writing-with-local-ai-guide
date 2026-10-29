# 4. Editing with Local AI

Editing is where your writing becomes polished. A local model can read your
draft and suggest changes — but you decide what to keep. Because everything runs
on your computer, you can paste private drafts (personal letters, unpublished
manuscripts, work documents) without worrying about where they go.

## How to edit with a local model

Start a chat:

```bash
ollama run llama3.2:3b
```

Paste your text, then ask for a specific kind of help. Never send a draft
without an instruction — otherwise the model may just rewrite it in its own
voice.

### Example editing prompts

**Proofread for typos:**

```text
Proofread this for spelling, grammar, and punctuation. List each change you make, then show the corrected version:

<<PASTE YOUR DRAFT HERE>>
```

**Make it clearer:**

```text
Rewrite this paragraph to be clearer and more concise. Keep my voice and do not change the meaning. Show me what changed and why:

<<PASTE YOUR DRAFT HERE>>
```

**Change the tone:**

```text
Rewrite this email to sound warmer and more patient, less frustrated. Keep it under 120 words:

<<PASTE YOUR DRAFT HERE>>
```

**Check pacing (fiction):**

```text
Look at this scene and tell me: where does the pacing drag? Where does it rush? Suggest one specific cut and one addition. Do not rewrite the whole scene:

<<PASTE YOUR SCENE>>
```

## The `<< >>` trick

Marking your draft with `<<` and `>>` tells the model exactly where your writing
starts and ends, so it does not accidentally treat your instructions as part of
the story.

## Review every suggestion

A local model can:

- Miss typos it introduces itself
- Suggest changes that flatten your voice
- Miss the point of a sentence you care about

Read each suggestion and ask: "Does this sound like me?" Keep what helps, ignore
the rest. You are the editor; the model is an assistant.

## Editing workflow

1. Write your draft (see [03. Drafting](./03-drafting.md)).
2. Paste a section into the model with a specific editing task.
3. Apply the suggestions you like, by hand, in your own document.
4. Repeat for the next section.
5. Read the whole piece aloud yourself before calling it done.

---

Published by **Asdale Dynamics, LLC**. MIT License. Copyright (c) 2026 Asdale
Dynamics, LLC.
