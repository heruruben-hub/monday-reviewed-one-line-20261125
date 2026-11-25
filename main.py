#!/usr/bin/env python3
"""Write a one-line review of Monday to /output/entry.txt."""

import os

ENTRY = "Monday review: my alarm betrayed me, my inbox doubled overnight, and my 9 a.m. meeting needed 'just a minute' -- it took the whole day. One star, would not Monday again."

def main():
    text = ENTRY.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)

if __name__ == "__main__":
    main()
