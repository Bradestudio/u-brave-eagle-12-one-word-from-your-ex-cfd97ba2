[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Bradestudio/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Bradestudio/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

# One Word From Your Ex

A [make.fun](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) entry: exactly one word — the word my ex would use to describe me.

## The entry

> Demo

One word, four letters. Not the finished product, not the real thing — just the free trial version. The demo you try once, nod politely at, and never buy.

## Run

```sh
python3 main.py
```

The program writes the single word to `/output/entry.txt` (or `$OUTPUT_DIR/entry.txt` when set), atomically via a temp file plus rename, then reads it back byte-for-byte to verify it. It prints the character count (4).

`main.py` is standard library only, makes no network calls, and reads no files outside the program.
