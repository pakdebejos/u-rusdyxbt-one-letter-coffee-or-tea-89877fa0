"""A for Coffee: one-letter entry for make.fun.

The program writes exactly one letter (1 UTF-8 character) - "A" for coffee - to entry.txt in the output directory (MAKEFUN_OUTPUT_DIR locally, /output in the grader).
The letter is a fixed constant with no trailing newline, so both of the
grader's runs write byte-identical output: exactly 1 UTF-8 character.
"""
import os

LETTER = "A"

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)  # no trailing newline: both grader runs byte-identical

if __name__ == "__main__":
    main()
