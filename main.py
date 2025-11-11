"""
HW03 — Group anagrams using a dictionary.
No type hints. Standard library only.
"""

def _clean_letters(s):
    """Return lowercase letters from s (a-z)."""
    # TODO Step 4: build a cleaned string with only letters
    return ''.join(c.lower() for c in s if c.isalpha())

def _signature(s):
    """Return sorted lowercase-letter signature for s."""
    # TODO Step 5: use _clean_letters, then sort characters and join
    cleaned = _clean_letters(s)
    return ''.join(sorted(cleaned))

def group_anagrams(words):
    """Return dict: signature -> list of original words in input order."""
    # TODO Steps 4–6: iterate words, compute key, append to list in dict
    # TODO Step 7: test with empty list and words with punctuation
    # TODO Step 8: small improvements if needed
    from collections import defaultdict
    groups = defaultdict(list)
    for word in words:
        sig = _signature(word)
        groups[sig].append(word)
    return dict(groups)

if __name__ == "__main__":
    # Optional: small manual check
    pass
