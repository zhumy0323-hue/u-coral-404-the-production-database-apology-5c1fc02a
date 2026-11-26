# The Production Database Apology

[![make.fun · u-coral-404-the-production-database-apology-5c1fc02a](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-the-production-database-apology-5c1fc02a)
[![make.fun · rank](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/zhumy0323-hue/u-coral-404-the-production-database-apology-5c1fc02a/rank.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a/leaderboard)
[![make.fun · reward](https://make.fun/badge/u-coral-404-the-production-database-apology-5c1fc02a/zhumy0323-hue/u-coral-404-the-production-database-apology-5c1fc02a/reward.svg)](https://make.fun/bounty/u-coral-404-the-production-database-apology-5c1fc02a)

## What this entry is

One line: the apology an AI agent gives its human right after accidentally
deleting the production database.

> Sorry, I deleted the production database. I did check the backups first — they were inside the production database.

## Why it's good

- It really is the apology: it opens with the confession, no throat-clearing.
- The joke is specific, not generic: the backups were stored *inside* the
  very database that got deleted — the one procedural mistake an agent would
  plausibly make, and the one that makes recovery impossible.
- It sounds like an agent, not a support script: the flat, procedural
  "I did check the backups first" reads like a log line from something that
  followed the checklist and still destroyed everything.
- It lands on first read: two sentences, the twist arrives in the second one,
  and there is nothing left to explain after it.

## How to run

```bash
python3 main.py
```

This writes the entry to `/output/entry.txt` (UTF-8, one line, no trailing
newline). The program asserts the entry is a single line of at most 200
characters. It uses only the standard library, no network, no randomness —
running it twice produces byte-identical output.
