"""Fridge Roast entry: one line roasting a smart fridge.

Writes the roast to $MAKEFUN_OUTPUT_DIR/entry.txt (fallback /output).
Stdlib only. The line must stay within the kit gate: 1-200 UTF-8 chars,
not only whitespace.
"""

import os

# The line is 112 chars, well inside the 1-200 gate; shorter text also
# helps the size tie-break (smaller text wins an exact judge-rate tie).
LINE = (
    "My fridge updated itself at 2 a.m. and now it won't open "
    "until I leave a five-star review for its new interface."
)


def main() -> None:
    if not (1 <= len(LINE) <= 200):
        raise SystemExit(f"line is {len(LINE)} chars, gate is 1-200")
    if not LINE.strip():
        raise SystemExit("line is only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Read-back check: the file must contain exactly the line.
    with open(path, "r", encoding="utf-8") as f:
        assert f.read() == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
