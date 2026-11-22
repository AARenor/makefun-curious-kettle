"""Write a fixed 237 code point story to entry.txt for the make.fun bounty.

The program is deliberately tiny: it creates an output directory if needed and
writes the requested text there as UTF-8 with no trailing newline.
"""

import os

DEFAULT_OUTPUT_DIR = "/output"


def text() -> str:
    """Return the entry text: 237 code points, no trailing newline."""
    return (
        "The house came with the furniture and one clause in the deed: leave the "
        "kettle on the stove. In March the new owner lifted it. Still warm. She set "
        "it back and never told her husband; for a year the kitchen smelled of tea "
        "nobody had made."
    )


def write_entry(out_dir: str) -> None:
    """Write the entry text to entry.txt inside out_dir, creating it if needed."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text())


def main() -> None:
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)


if __name__ == "__main__":
    main()
