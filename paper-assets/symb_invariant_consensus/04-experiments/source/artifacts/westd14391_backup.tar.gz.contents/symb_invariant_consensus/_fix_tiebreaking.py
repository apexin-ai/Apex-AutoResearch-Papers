"""Fix insertion-order tiebreaking in NLI combo scripts → alphabetical."""
import re

FIXES = [
    # (file, line_no, old_pattern, new_code)
    ("scripts/qwen14b_pw_nli_combo.py", 126,
     "            combo_answer = max(combo_votes, key=combo_votes.get)",
     "            _max = max(combo_votes.values()); combo_answer = sorted(k for k, v in combo_votes.items() if v == _max)[0]"),
    ("scripts/exp092_llama8b_pw_nli_combo.py", 118,
     "            combo_answer = max(votes, key=votes.get)",
     "            _max = max(votes.values()); combo_answer = sorted(k for k, v in votes.items() if v == _max)[0]"),
    ("dir_k_nli_qwen3_pw600.py", 163,
     '            combo_answer = votes.most_common(1)[0][0] if votes else "Unknown"',
     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else "Unknown"'),
    ("dir_k_nli_qwen3_pw600.py", 202,
     '            combo_answer = votes.most_common(1)[0][0] if votes else "Unknown"',
     '            combo_answer = sorted([k for k, v in votes.items() if v == max(votes.values())])[0] if votes else "Unknown"'),
]

for fpath, lineno, old, new in FIXES:
    with open(fpath) as f:
        lines = f.readlines()
    if lines[lineno-1].rstrip() == old:
        lines[lineno-1] = new + "\n"
        with open(fpath, "w") as f:
            f.writelines(lines)
        print(f"FIXED {fpath}:{lineno}")
    else:
        print(f"MISMATCH {fpath}:{lineno}")
        print(f"  Expected: {old!r}")
        print(f"  Got:      {lines[lineno-1].rstrip()!r}")
