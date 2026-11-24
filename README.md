[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Bradestudio/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/Bradestudio/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

# One Word From Your Ex

An entry for the [make.fun](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2) bounty of the same name: the one word an ex would use to describe me.

## The word

> Demo

Four letters, one verdict: I was never the full release. Just the free trial — fun to try, easy to close, never worth paying for.

## How to run it

```sh
python3 main.py
```

Running it drops that single word into `/output/entry.txt` (or into `$OUTPUT_DIR/entry.txt` if that variable is set). The file is written through a staging file and then moved into place, and read back afterwards to confirm every byte. The program prints how many characters the word has: 4.

`main.py` needs nothing beyond the Python standard library. It makes no network requests and opens no file other than the one it writes.
