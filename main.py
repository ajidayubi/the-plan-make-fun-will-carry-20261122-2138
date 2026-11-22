#!/usr/bin/env python3
"""30-day plan: turn $100 into the most money with n8n automations.

Writes the plan as a single 1-280 character text to entry.txt.
Stdlib only, deterministic, no network.
"""

import os
import sys

PLAN = (
    "Day 1: build 3 n8n automations for plumbers/dentists "
    "(missed-call texter, review replier, invoice chaser) at $29 on Gumroad. "
    "Then: 1 demo/day on X + Shorts; DM 40 firms/day, $99 setup. "
    "First sale pays $5/day X ads; upsell $49/mo support. "
    "Likely: 12 sales + 3 setups = $650."
)


def main() -> int:
    # Harness limit is 1-280 chars; reject anything outside it before writing.
    if not 1 <= len(PLAN) <= 280:
        print(f"error: plan is {len(PLAN)} chars, must be 1-280", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(PLAN)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
