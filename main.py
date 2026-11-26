"""Two Days of Quiet Dread, variant 6.

Writes one code review comment to /output/entry.txt: a single line of at
most 140 characters that approves a pull request while carrying quiet
existential dread. Pure standard library, deterministic, no network.

The dread here is a single sharp incident, named once and never
explained. Variants 1 to 5 covered the code outliving us, a temporary
fix from 2019, a Friday ship while on call, tests that pass after the
code they tested was deleted, and four reviewers of whom three have
left. None of them touched the one voice inside the code itself: the
only comment the code carries says "good luck". That is the whole
incident. Nobody wrote who the luck is for, or against what. The
reviewer does not ask. They take it personally, calmly, and approve.

The approval comes first, flat and real, the way a tired engineer
actually pastes it before clicking approve. Then one plain fact, the
comment in the code, and one quiet closing beat that turns the
approval into a confession: the reviewer knows the luck is meant for
them. No exclamation, no melodrama, no cry for help. The laugh, if
there is one, comes from the dread itself, from the reviewer calmly
signing off after the code wished them luck.

The program assembles the entry from three named beats so the
structure of the comment is visible in the code, validates it against
the competition gate (one line, 1 to 140 characters, not only
whitespace), and writes it to /output/entry.txt.
"""

import os

# The three beats of the comment, kept separate so the structure of the
# entry is visible in the code. Joined with single spaces below.
_APPROVAL = "Approved."
_INCIDENT = "The code's only comment says 'good luck'."
_CLOSING = "I am taking that personally."

# The entry itself: approval first, then the incident named once, then
# the closing beat that takes it personally. Exactly 80 characters,
# one line.
ENTRY = " ".join([_APPROVAL, _INCIDENT, _CLOSING])

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 140


def validate_entry(text):
    """Check one candidate entry against the competition gate.

    Returns the stripped text when it is a single non-empty line of
    1 to 140 characters, and raises ValueError otherwise.
    """
    cleaned = text.strip()
    if not MIN_LENGTH <= len(cleaned) <= MAX_LENGTH:
        raise ValueError(
            f"entry must be {MIN_LENGTH}-{MAX_LENGTH} characters, "
            f"got {len(cleaned)}"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if not cleaned:
        raise ValueError("entry must not be only whitespace")
    return cleaned


def build_entry():
    """Assemble the entry from its three beats and validate it."""
    for beat in (_APPROVAL, _INCIDENT, _CLOSING):
        if not beat or beat != beat.strip():
            raise ValueError("each beat must be non-empty and unpadded")
        if "\n" in beat or "\r" in beat:
            raise ValueError("each beat must be a single line")
    return validate_entry(ENTRY)


def write_entry(text):
    """Write one validated entry line to OUTPUT_PATH.

    Creates the output directory when needed and writes the text
    followed by a single trailing newline, using UTF-8.
    """
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


def main():
    """Build the entry, validate it, and write it out."""
    text = build_entry()
    write_entry(text)


if __name__ == "__main__":
    main()
