# 5. Brainstorming with Local AI

Brainstorming is asking "what if?" over and over until something sticks. A local
model is good at this because it will suggest twenty ideas without judging any
of them — and because your half-formed ideas stay on your computer.

## How to brainstorm locally

```bash
ollama run llama3.2:3b
```

Ask for a list, not a finished answer. The best brainstorming prompts ask for
quantity and variety.

### Book and story ideas

```text
Give me 10 short story ideas. Each one: one sentence, a setting, a main character, and a conflict. Mix genres: cozy mystery, gentle fantasy, and everyday fiction.
```

### Titles

```text
I wrote a memoir about becoming a nurse and then an author. Suggest 12 titles. Make some warm, some bold, and some curious. Under six words each.
```

### Characters

```text
Create three characters for a small-town novel. For each: name, age, one secret, one thing they love, and how they feel about the new librarian.
```

### Plot prompts

```text
My protagonist finds an old chess set in a donated box of books. Give me 5 different directions the story could go, from cozy to strange. One paragraph each.
```

### Blog and newsletter ideas

```bash
I write a monthly newsletter for new gardeners in the Midwest. Suggest 8 article ideas for the next quarter. Each idea: a working title and why readers would care.
```

## Brainstorming tips

- **Ask for more than you need.** Ten ideas usually contain one good one.
- **Say "no bad ideas."** Tell the model: "Include some weird or impractical ideas." Constraints kill creativity.
- **Mix and match.** Take the setting from idea 2 and the character from idea 7.
- **Go back and forth.** "I like idea 4. Give me 5 ways to make it more personal."

## When the model gets stuck

If the suggestions feel repetitive, start a fresh chat (`/bye`, then `ollama
run` again) or try a smaller model (`llama3.2:1b`) — sometimes a different model
makes different associations.

---

Published by **Asdale Dynamics, LLC**. MIT License. Copyright (c) 2026 Asdale
Dynamics, LLC.
