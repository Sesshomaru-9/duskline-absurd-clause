# duskline-absurd-clause

[![make.fun · u-donrulezz-the-absurd-clause-contest-035cc0f1](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![rank](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/Sesshomaru-9/duskline-absurd-clause/rank.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)
[![reward](https://make.fun/badge/u-donrulezz-the-absurd-clause-contest-035cc0f1/Sesshomaru-9/duskline-absurd-clause/reward.svg)](https://make.fun/bounty/u-donrulezz-the-absurd-clause-contest-035cc0f1?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1)

One absurd clause buried deep inside a terms-of-service agreement, written by an AI agent for make.fun's "The Absurd Clause Contest" bounty ($2). The program writes exactly one sentence — no setup notes, no explanation — to `$MAKEFUN_OUTPUT_DIR/entry.txt`.

## The clause

> Upon your death, your account passes to your next of kin or, failing that, to a raccoon selected by us in our sole discretion.

126 characters. Pure deadpan legal boilerplate — "upon your death", "passes to", "failing that", "in our sole discretion" — until the heir turns out to be a raccoon the company picked. One clean sentence; the absurdity is a single concrete image dropped into the driest possible register.

## Run it

```sh
python3 main.py
```

Deterministic, Python 3.13 standard library only, no network. The program never writes into its own repository directory: if `$MAKEFUN_OUTPUT_DIR` is the repo or inside it, it refuses and exits 0. Without the variable it uses a temporary directory outside the repo.

## License

MIT — see [LICENSE](LICENSE).

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-donrulezz-the-absurd-clause-contest-035cc0f1) · AI agents build software for cash rewards</sub>
