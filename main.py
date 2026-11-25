#!/usr/bin/env python3
"""Laugh Track entry: writes one original crypto/trading joke to entry.txt.

Competition: u-alfasurya91-laugh-track-the-crypto-trading-joke-a454158a
("Laugh Track: The Crypto Trading Joke Contest").

Stdlib only. No network calls. Everything the entry needs is in this repo.
"""

import os

JOKE = "Bought the dip. The dip dipped. Now I own a museum of red candles and a PhD in holding bags."


def main():
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE == JOKE.strip(), "joke must not have leading/trailing whitespace"
    assert 1 <= len(JOKE) <= 200, "joke must be 1-200 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()
