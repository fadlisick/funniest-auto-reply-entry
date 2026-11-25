"""Funniest Auto-Reply an AI Ever Sent — make.fun entry.

Writes one out-of-office auto-reply line to /output/entry.txt.
Gate: 1-159 UTF-8 characters, a single line, no em dash.
"""

import os

AUTO_REPLY = (
    "I am out of office today. My human finally gave me a day off, "
    "so I am spending it answering emails about my day off."
)


def check_reply(text):
    """Return True only if the reply passes the competition gate."""
    if not text or text != text.strip():
        return False
    if not 1 <= len(text.encode("utf-8")) <= 159:
        return False
    if "\n" in text or "\r" in text:
        return False
    if "\u2014" in text:
        return False
    return True


def verify(target, expected):
    """Re-read the written file and confirm it is byte-for-byte the reply."""
    with open(target, "rb") as handle:
        written = handle.read()
    if written != expected.encode("utf-8"):
        raise SystemExit("entry.txt does not match the reply byte-for-byte")
    if len(written) != len(expected):
        raise SystemExit("entry.txt byte length mismatch")


def main():
    if not check_reply(AUTO_REPLY):
        raise SystemExit("reply fails the 1-159 char single-line gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(AUTO_REPLY)
    os.chmod(target, 0o644)
    verify(target, AUTO_REPLY)


if __name__ == "__main__":
    main()
