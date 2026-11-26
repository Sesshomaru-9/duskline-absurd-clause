# Duskline Absurd Clause

One absurd clause for a Terms of Service, written for
The Absurd Clause Contest on make.fun.

## The clause

> Upon your death, your account passes to your next of kin or, failing
> that, to a raccoon selected by us in our sole discretion.

126 characters, one line. The raccoon is chosen in our sole discretion.
No appeal process is described. The raccoon does not sign anything.

## How it works

`main.py` (Python 3.13 standard library only) writes the clause above
to `$MAKEFUN_OUTPUT_DIR/entry.txt` and exits with status 0. It writes
nowhere else.

If the output directory cannot be written — for example when the
repository is read-only — the program does not crash; it simply exits
with status 0.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## License

MIT — see `LICENSE`.
