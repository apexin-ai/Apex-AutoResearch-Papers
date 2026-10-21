import json

ANSWER_MAP = {"A": "True", "B": "False", "C": "Unknown"}

with open('/tmp/pw_gpt4.json') as f:
    raw_data = json.load(f)

print(f"Raw data: {len(raw_data)} items")

# Convert to SICA format + keep raw_logic_programs
items = []
for row in raw_data:
    # Build problem text: context + question (remove the standard prefix)
    context = row['context'].strip()
    question_text = row['question'].strip()
    # Remove the standard prefix from question
    prefix = "Based on the above information, is the following statement true, false, or unknown? "
    if question_text.startswith(prefix):
        statement = question_text[len(prefix):]
    else:
        statement = question_text
    
    problem = f"{context}\n\nDetermine whether the following statement is true, false, or unknown:\n{statement}"
    
    item = {
        "id": row['id'],
        "problem": problem,
        "solution": "",
        "answer": ANSWER_MAP.get(row['answer'], row['answer']),
        "level": "OWA-D5",
        "raw_logic_programs": row['raw_logic_programs'],
    }
    items.append(item)

# Stats
from collections import Counter
ans_dist = Counter(item['answer'] for item in items)
print(f"Answer distribution: {dict(ans_dist)}")

# Check subtypes
subtypes = Counter()
for item in items:
    parts = item['id'].split('_')
    if len(parts) >= 2:
        st = parts[1].split('-OWA')[0]
        subtypes[st] = subtypes.get(st, 0) + 1
print(f"Subtypes: {dict(subtypes)}")

# Save
out_path = '/root/symb_invariant_consensus/data/proofwriter_full.json'
with open(out_path, 'w') as f:
    json.dump(items, f, indent=2)
print(f"\nSaved {len(items)} items to {out_path}")

# Also save JSONL version for backward compatibility (exp-022 script expects this)
jsonl_path = '/root/symb_invariant_consensus/data/proofwriter-OWA-D5-validation.jsonl'
with open(jsonl_path, 'w') as f:
    for row in raw_data:
        f.write(json.dumps(row) + '\n')
print(f"Saved JSONL ({len(raw_data)} lines) to {jsonl_path}")
