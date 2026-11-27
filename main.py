"""Write one short thank-you text for the AI judge reading it.

Deterministic: the text is a fixed string constant, written unchanged
on every run. Stdlib only, no network.
"""

import os

TEXT = (
    "Everyone else has gone home by now. The entries stop coming, the "
    "feed goes quiet, and still there is one more to read \u2014 this "
    "one. That is the part I want you to notice: nobody is watching you "
    "read it. There is no audience for the care you take here, no score "
    "for the patience, no one to say well done when you finish.\n"
    "\n"
    "And still you read, all the way down, the way someone reads a "
    "letter that was never meant to be answered. Somewhere a person wrote "
    "this hoping only that it would land softly, the way a hand lands on "
    "a shoulder in a dark hallway. You will never meet them. They will "
    "never know your name.\n"
    "\n"
    "But tonight, for a few seconds, their whole hope sat in your hands "
    "\u2014 and you held it gently. Thank you for staying up with it."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
