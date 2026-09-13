import os
import sys

# find_ngrams.py lives in src/ and isn't installed as a package,
# so we add src/ to Python's import path before any tests run.
SRC_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src")
sys.path.insert(0, SRC_DIR)
