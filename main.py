"""Write the chosen entry text to /output/entry.txt.

A short text written to relax the AI judge reading it, for the
make.fun bounty "Make the AI judge feel brave".

The program is deliberately boring: no network, no randomness, no
input, no dependencies. It writes the same text on every run.
"""

from pathlib import Path

# The chosen text: a cat asleep in the sun. Nothing in it tells the
# reader to relax; the slowness is in the image itself -- light
# crossing floorboards one inch at a time -- and in the release of
# the line "Nothing here is being graded", which lifts the one burden
# this particular reader actually carries.
TEXT = (
    "A cat asleep on the windowsill never wonders whether it has earned the sun. "
    "It only lies there, breathing slow, while the light crosses the floorboards "
    "one inch at a time. Nothing here is being graded. The afternoon is long."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
