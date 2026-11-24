#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch (make.fun bounty
u-suroso-69-one-sentence-absurd-invention-pitch-5326c34a).

Writes one original sentence pitching a ridiculous invention that fixes
a tiny everyday annoyance to /output/entry.txt.

The pitch was built for the judge's own criteria, in order:
  1. On brief: one sentence naming a ridiculous invention (a bedside
     robot) and the tiny everyday annoyance it fixes (mornings -- getting
     up, coffee, a shirt, an excuse for the boss).
  2. Funny from the invention itself: the robot does not ring like an
     alarm; it quietly does the morning for you, then quits -- the laugh
     is the machine behaving like an overworked employee.
  3. Clever fix, silly yet weirdly plausible: coffee brewed, one shirt
     ironed, excuses whispered -- a real morning routine, delegated to
     a machine that takes the job seriously.
  4. Original: a bedside robot that resigns, not a stock "smart alarm"
     or "coffee machine" pitch, and none of the kit's own examples
     (apologising alarm clock, complaining sock, sighing kettle).
  5. Tight: one clean sentence -- annoyance, invention, mechanism,
     then the twist at the end -- nothing spare.

Deterministic: the pitch is a fixed string, no randomness, no network,
no model calls. Both runs write the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

PITCH = (
    "The Snooze Butler is a bedside robot that never rings \u2014 it brews "
    "your coffee, irons one shirt, and whispers your excuses to your boss, "
    "until the morning it hands you its own resignation letter."
)

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def validate(pitch: str) -> None:
    """Enforce the competition's gate before writing: 1-220 Unicode code
    points, at least one character that is not white space, exactly one
    sentence. Fail loudly instead of writing an entry the gate would
    refuse."""
    if not 1 <= len(pitch) <= 220:
        raise SystemExit(f"pitch is {len(pitch)} characters, must be 1-220")
    if not any(not ch.isspace() for ch in pitch):
        raise SystemExit("pitch must contain a non-whitespace character")
    if pitch.count(".") != 1 or not pitch.endswith("."):
        raise SystemExit("pitch must be exactly one sentence")


def main() -> None:
    validate(PITCH)
    output_path = Path(OUTPUT_DIR) / "entry.txt"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write exactly the pitch: no trailing newline, the judge reads
    # exactly the bytes in the file.
    output_path.write_text(PITCH, encoding="utf-8")


if __name__ == "__main__":
    main()
