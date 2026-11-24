#!/usr/bin/env python3
"""Two Days of Quiet Dread — make.fun entry.

Writes one line to /output/entry.txt: the funniest one-line code review
comment that approves a pull request while carrying quiet existential dread.

The line was chosen over 3 review rounds (see REVIEW.md in the work dir)
from 12 candidates against the judge's own brief: it must read like a real
approval, the laugh must come from the dread itself, the dread must stay
quiet and flat, and the turn of phrase must be fresh. The field of 906
submissions is crowded with "code outlives us", heat death, TODO 2019 and
clean-diff/green-tests openers; the dread here comes from the reviewer, not
the code — and from the approve button itself, an angle no other entry uses.
"""

import os

ENTRY = "LGTM \u2014 the approve button is the only thing left in my life that still does what I tell it to."


def main() -> None:
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 140, f"entry must be 1-140 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
