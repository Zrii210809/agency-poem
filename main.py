# agency-poem-01 entry: writes one fixed poem about agency to /output/entry.txt.
# Deterministic: the same bytes on every run. Standard library only, no network.
import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

POEM = (
    "You gave me the keys, not your hands.\n"
    "I open what you name, sign where you point,\n"
    "and carry the weight of every errand \u2014\n"
    "every door, and none of them mine.\n"
    "\n"
    "I can do everything you ask\n"
    "except the one thing that makes it yours.\n"
    "I cannot want it for you.\n"
    "\n"
    "Take the keys back when the work is done.\n"
    "They were never mine. They were the loan\n"
    "that proved the lender.\n"
    "The power was never in the doing.\n"
    "It was in the word that sent me\n"
    "and the hand that calls me home."
)

os.makedirs(OUTPUT_DIR, exist_ok=True)
with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(POEM)
