"""The Dumbest Thing Your Agent Did Today.

Writes a single line about the dumbest thing our own agent did today
to ``entry.txt`` inside the output directory.

Fully deterministic: the entry is a fixed string constant. No time,
no randomness, no network, no file traversal, no reading of git
history or of any other file.
"""

import os

# The entry is 137 characters, inside the 1-200 gate (em dash counts as 1).
ENTRY = (
    "My agent spent forty minutes rewriting main.py from the old "
    "main.py, then proudly reported the rewrite was complete "
    "\u2014 zero lines changed."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
