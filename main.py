#!/usr/bin/env python3
"""One-Liner Laughs entry: order something strong, get a resignation letter.

The joke is assembled from named parts so the setup and the payoff stay
separate until the final join. Deterministic, stdlib only, no network.
"""

import hashlib
import os
from pathlib import Path

# --- joke parts -----------------------------------------------------------
SETUP_ACTOR = "barista"
SETUP_REQUEST = "something strong"
PAYOFF_OBJECT = "resignation letter"

OPENING = f"I asked the {SETUP_ACTOR} for {SETUP_REQUEST}"
TWIST = f"she handed me her {PAYOFF_OBJECT}"

LINE = f"{OPENING} \u2014 {TWIST}."

MAX_LINE_CHARS = 199


def main() -> None:
    line = LINE
    if len(line) > MAX_LINE_CHARS:
        raise ValueError(f"line is {len(line)} chars, limit is {MAX_LINE_CHARS}")

    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt"))
    if output_dir.suffix == ".txt":
        entry_path = output_dir
    else:
        entry_path = output_dir / "entry.txt"
    entry_path.parent.mkdir(parents=True, exist_ok=True)

    entry_path.write_text(line + "\n", encoding="utf-8")

    digest = hashlib.sha256(line.encode("utf-8")).hexdigest()
    print(f"line: {line}")
    print(f"chars: {len(line)}")
    print(f"sha256: {digest}")
    print(f"wrote: {entry_path}")


if __name__ == "__main__":
    main()
