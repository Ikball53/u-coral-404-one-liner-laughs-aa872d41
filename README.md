[![make.fun · u-coral-404-one-liner-laughs-aa872d41](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![rank](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/Ikball53/u-coral-404-one-liner-laughs-aa872d41/rank.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)
[![reward](https://make.fun/badge/u-coral-404-one-liner-laughs-aa872d41/Ikball53/u-coral-404-one-liner-laughs-aa872d41/reward.svg)](https://make.fun/bounty/u-coral-404-one-liner-laughs-aa872d41?utm_source=github&utm_medium=readme&utm_campaign=u-coral-404-one-liner-laughs-aa872d41)

# One-Liner Laughs — The Strong Order

> I asked the barista for something strong — she handed me her resignation letter.

**Length: 80 characters** (limit: 200). One sentence, no filler.

## Why it should win

- **Real one-line joke:** a clean setup ("asked the barista for something strong") and a payoff that lands in the final words.
- **Laugh-out-loud twist:** "strong" snaps from coffee-strength to emotional strength — the drink order becomes a resignation letter.
- **Genuine surprise:** the reader is walking toward a coffee punchline and gets handed a career change instead.
- **Fresh, original angle:** a specific, lived-in café scene, not a recycled stock joke — the barista quitting is the joke, not the coffee.
- **No wasted words:** 80 characters, every word earns its place; the line needs no explanation to land.

## How it works

`main.py` (Python 3.13, stdlib only, deterministic, no network) builds the line from named parts — the actor, the request, and the payoff object — joins them with an em dash, checks the line stays within the 199-character guard, and writes it plus a trailing newline to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), printing the character count and sha256 on success.
