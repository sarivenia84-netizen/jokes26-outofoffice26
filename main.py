#!/usr/bin/env python3
"""Out-of-office auto-reply entry for make.fun bounty 'The Painfully Honest Out-of-Office'.

The judge brief prizes a single sentence (≤200 chars) that is painfully honest
about absence yet polite enough to survive being forwarded to a manager. This
line claims a genuine lull after Q3 while staying professional — "honestly"
removed for sharper impact.
"""

import os

LINE = "I'm out until Monday, and this is the most relaxed I've been since Q3. Your email is safe with me; I will lose it gently, with fresh eyes, on my return."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()