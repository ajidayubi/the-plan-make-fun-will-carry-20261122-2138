#!/usr/bin/env python3
"""The plan make.fun will carry out in public.

Writes one text (1-280 Unicode chars) to /output/entry.txt: a plan an AI
agent can carry out itself to turn $100 into the most money in 30 days.

The plan: sell small AI automations to a narrow niche of local firms
(plumbers, dentists) who already pay for this kind of help. Day 1 builds
three ready-made n8n automations and lists them at $29 on Gumroad; the
rest of the month is daily demo videos plus direct outreach offering a
$99 done-for-you setup, with the first sale funding a small ad budget and
a $49/mo support upsell. The expected outcome is stated honestly
(12 sales + 3 setups = about $650), not a best case, and every step uses
services that exist today and take an agent's work.
"""

import os

PLAN = (
    "Day 1: build 3 n8n automations for plumbers/dentists "
    "(missed-call texter, review replier, invoice chaser) at $29 on "
    "Gumroad. Then: 1 demo/day on X + Shorts; DM 40 firms/day, $99 "
    "setup. First sale pays $5/day X ads; upsell $49/mo support. "
    "Likely: 12 sales + 3 setups = $650."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = PLAN.strip()
    assert 1 <= len(text) <= 280, f"plan is {len(text)} chars, must be 1-280"
    assert text.strip(), "plan must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
