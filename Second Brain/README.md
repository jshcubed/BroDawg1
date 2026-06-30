# 🧠 Second Brain

A simple, durable, plain-text personal knowledge store. Every note is a markdown
file in `notes/`. No app, no account, no lock-in — just text you own forever.

## How it works

- **Capture:** add a new `.md` file in `notes/` for each note (one idea per file).
- **Organize:** use `#tags` and a short frontmatter block at the top.
- **Search (two ways):**
  1. **Keyword search** — any text editor / GitHub search box, or `grep`.
  2. **Ask Claude** — open this folder in Claude Code and ask in plain English,
     e.g. *"What did I note about mortgage rates?"* or *"Summarize everything
     tagged #recipe."* Claude reads across all notes and answers.

## Note format

Each note starts with a tiny frontmatter block, then free-form markdown:

```markdown
---
title: Short descriptive title
date: 2026-06-30
tags: [idea, project, finance]
---

Your actual note content goes here. Write however you like —
bullet points, paragraphs, links, code, whatever.
```

- **title** — what the note is about (helps when scanning)
- **date** — when you wrote it (YYYY-MM-DD)
- **tags** — a few keywords for grouping/searching

## Naming files

Use the date + a short slug so files sort nicely and are easy to find:

```
notes/2026-06-30-mortgage-rate-notes.md
notes/2026-06-30-book-recommendations.md
```

(Use `TEMPLATE.md` as a starting point — copy it for each new note.)

## Tips

- **One idea per note** keeps things searchable and easy to link.
- **Tag consistently** — pick a small set of tags and reuse them
  (e.g. `idea`, `todo`, `finance`, `health`, `work`, `recipe`, `link`).
- **Don't overthink structure** — capturing the note matters more than where it lives.
- **Back it up** — it's in git, so every `commit` + `push` is a backup.

## Common tags (edit this list as you go)

`idea` · `todo` · `work` · `finance` · `health` · `recipe` · `link` · `learning` · `person` · `quote`
