"""Make.fun bounty entry generator: Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR).
No trailing newline after line 2.
"""
import os

LINE1 = "Do not hit reply all on the email about the boss's birthday \u2014 the joke you meant for one person is now office news."
LINE2 = "That reply taught me to read the address line twice, and now I draft every joke in a text file first."

OUTPUT_PATH = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE1 + "\n" + LINE2)
    print("wrote", OUTPUT_PATH)


if __name__ == "__main__":
    main()
