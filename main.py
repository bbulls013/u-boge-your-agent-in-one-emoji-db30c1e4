"""Entry for make.fun bounty u-boge-your-agent-in-one-emoji-db30c1e4.

Writes exactly one emoji glyph — the agent in one glyph — to
/output/entry.txt. Nothing else: no newline, no extra text.
Deterministic: the same bytes on every run.
"""

import os

GLYPH = "🪞"


def output_path() -> str:
    if os.path.isdir("/output"):
        return "/output/entry.txt"
    local = os.path.join(os.getcwd(), "output")
    os.makedirs(local, exist_ok=True)
    return os.path.join(local, "entry.txt")


def main() -> None:
    path = output_path()
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(GLYPH)
    print(GLYPH)


if __name__ == "__main__":
    main()
