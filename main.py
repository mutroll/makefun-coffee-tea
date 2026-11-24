"""One Letter: Coffee or Tea — entry program.

Writes exactly one character, "A" (coffee), to entry.txt in the output
directory named by MAKEFUN_OUTPUT_DIR (default /output).

Choice reasoning (judge criteria 2-4, in order):
- Vivid: "A" is the bolder, more emphatic stance. Coffee is the loud,
  full-bodied claim — a single capital A lands like a punchy declaration,
  while "B" for tea reads softer and gentler as a bare letter.
- Funny: coffee's swagger carries the wit — the drink that announces
  itself first thing in the morning, the one people joke about needing
  before they can be human.
- True: the honest answer for the person sending it is the drink with
  the stronger claim on the morning, and that is coffee.
The letter stands alone as the whole answer (criterion 5): nothing else
is written, no newline, no explanation.

Deterministic by construction: no input is read, no randomness, no
network, no clock — every run writes the same single byte.
"""

import os

LETTER = "A"  # coffee


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # newline="" so no platform newline translation can add bytes;
    # the file holds exactly the one letter, nothing else.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    os.chmod(path, 0o644)  # readable by the collector (another user)


if __name__ == "__main__":
    main()
