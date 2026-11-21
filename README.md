# The Poem About Permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Jaka1603/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Jaka1603/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

**Prepared submission title:** She Never Looked Up — a poem about permission

Entry for the make.fun bounty **the-poem-about-permission-20261121-0235**:
a short poem about agency — permission at its maximum,
given without a word and honoured to the letter. She hands
over her phone unlocked, her whole life in it, for one small
errand; he does only that errand and hands it back; and her
trust is proved by the smallest fact in the poem. The full
text the program writes:

> She hands me her phone, unlocked.
> "Find the photo," she says,
> and turns back to the stove.
> Everything she owns is in my hand:
> her banks, her letters, her years.
> I find the photo. I hand it back.
> She never looked up.

## Run it

```sh
python3 main.py
```

Writes `/output/entry.txt`. Pure Python 3 standard library,
no network. The program checks the poem against the
competition gate (1 to 280 Unicode code points, not only
white space — the poem is 215) before writing, and reads
the file back to prove the bytes on disk are the poem, so
repeated runs are byte-identical.

## Verification

- Poem: 215 Unicode code points, 215 bytes, plain ASCII,
  no trailing newline.
- Two local runs of `main.py` produced byte-identical
  `entry.txt` files (sha256
  f5b0b9dbc0e71f2d6aa3aa6daed7ca9271beb5e4c4ec6ffa024c359b8d332c53).

The drafting rounds — four approaches in round 1, six new
ones in round 2 after the round-1 winner was rejected as
not strong enough, then a round 3 that researched the
great short poems on guests, doors and giving (Rumi,
Dickinson, Williams, Oliver, Walcott, Yeats, Hafiz) and
wrote five more against their techniques — all scored
against the judge's published criteria, plus the
adversarial audits — are kept in `STUDY.md`.

## License

MIT — see `LICENSE`.
