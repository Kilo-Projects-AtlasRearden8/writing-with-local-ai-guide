# 7. Printable Prompt Templates

Print this page (or open `site/templates.html` and press `Ctrl+P` / `Cmd+P`) and
keep the templates beside your keyboard. Fill in the blanks by hand, then type
the finished prompt into Ollama.

Each template works with `ollama run <model-name> "your prompt here"`.

---

## Template 1: Draft a story opening

```text
Write the opening scene of a _______________ (genre: cozy mystery, romance, etc.)
set in _______________ (place).
The protagonist is _______________ (name, job, one trait).
Tone: _______________ (gentle, humorous, suspenseful, etc.).
About _______________ words.

Extra details to include: _________________________________________
```

## Template 2: Draft an article or blog post

```text
Write a _______________-word beginner-friendly article about _______________.
Include: ________________________________________________________.
Tone: _______________ (warm, professional, encouraging, etc.).
One sentence takeaway for the reader: _____________________________.
```

## Template 3: Draft a letter or email

```text
Write a _______________ (polite / firm / friendly) _______________ (letter/email)
to _______________ about _______________.
Key points to mention: ___________________________________________.
Keep it under _______________ words.
```

## Template 4: Proofread a draft

```text
Proofread this for spelling, grammar, and punctuation. List each change,
then show the corrected version:

<<
________________________________________________________
________________________________________________________
________________________________________________________
>>
```

## Template 5: Rewrite for tone

```text
Rewrite this to sound _______________ (warmer, more patient, more professional,
more humorous). Keep my voice and do not change the meaning. Show what changed:

<<
________________________________________________________
________________________________________________________
>>
```

## Template 6: Brainstorm titles

```text
I wrote a _______________ (book/article/essay) about _______________.
Suggest _______________ titles. Make some _______________ and some _______________.
Under _______________ words each.
```

## Template 7: Brainstorm characters

```text
Create _______________ characters for a story set in _______________.
For each: name, age, one secret, one thing they love, and their goal.
```

## Template 8: Check fiction pacing

```text
Look at this scene and tell me where the pacing drags and where it rushes.
Suggest one specific cut and one addition. Do not rewrite the whole scene:

<<
________________________________________________________
________________________________________________________
>>
```

---

How to use: fill in the blanks, remove the `<<` and `>>` brackets around your
own text, and paste into:

```bash
ollama run llama3.2:3b "your filled-in prompt"
```

Published by **Asdale Dynamics, LLC**. MIT License. Copyright (c) 2026 Asdale
Dynamics, LLC.
