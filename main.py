#!/usr/bin/env python3
"""The poem about permission — writes one short poem to /output/entry.txt."""

import os

POEM = (
    "She kept the key in her apron pocket,\n"
    "heavy as a small held word.\n"
    "I asked — not for the door,\n"
    "but for the weight of it in my palm.\n"
    "She pressed it there, still warm.\n"
    "The lock turned. The house said my name."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
