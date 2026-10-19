"""Analyze Microsoft/lost_in_conversation dataset from HuggingFace."""

import json
from collections import Counter, defaultdict
from datasets import load_dataset

print("=" * 70)
print("Loading dataset: microsoft/lost_in_conversation")
print("=" * 70)

ds = load_dataset("microsoft/lost_in_conversation")
print(f"\nDataset object: {ds}")

# Flatten all splits into one list for analysis
all_samples = []
for split_name in ds:
    split_ds = ds[split_name]
    print(f"\nSplit '{split_name}': {len(split_ds)} samples")
    for i in range(len(split_ds)):
        sample = split_ds[i]
        sample["_split"] = split_name
        all_samples.append(sample)

total = len(all_samples)
print(f"\n{'=' * 70}")
print(f"TOTAL SAMPLE COUNT: {total}")
print(f"{'=' * 70}")

# Print all column names
print(f"\n{'=' * 70}")
print("COLUMN NAMES / FIELD NAMES")
print(f"{'=' * 70}")
first_split = list(ds.keys())[0]
columns = ds[first_split].column_names
print(f"Columns: {columns}")

# Identify task field
task_field = None
for candidate in ["task", "task_type", "type", "category"]:
    if candidate in columns:
        task_field = candidate
        break

if task_field is None:
    # Print a sample to find the right field
    print("\nCould not find task field. Printing first sample keys and values:")
    sample0 = all_samples[0]
    for k, v in sample0.items():
        val_str = str(v)
        if len(val_str) > 200:
            val_str = val_str[:200] + "..."
        print(f"  {k}: {val_str}")
    # Try all string-valued fields
    for k, v in sample0.items():
        if isinstance(v, str) and len(v) < 50 and k != "_split":
            print(f"\nPossible task field: '{k}' with value '{v}'")
else:
    print(f"\nTask field identified: '{task_field}'")

# Identify shard field
shard_field = None
for candidate in ["shard", "shards", "num_shards", "shard_count", "num_turns", "turns"]:
    if candidate in columns:
        shard_field = candidate
        break

if shard_field is None:
    print("\nCould not find shard field directly. Checking all integer-like fields:")
    sample0 = all_samples[0]
    for k, v in sample0.items():
        if isinstance(v, (int, float)):
            print(f"  {k}: {v}")

print(f"\n{'=' * 70}")
print("PER-TASK-TYPE SAMPLE COUNTS")
print(f"{'=' * 70}")

# Try to determine task field dynamically
if task_field is None:
    # Fallback: check all fields with low cardinality
    sample0 = all_samples[0]
    for k in sample0:
        if k == "_split":
            continue
        vals = set()
        for s in all_samples[:500]:
            v = s[k]
            if isinstance(v, (str, int, float, bool)):
                vals.add(v)
            if len(vals) > 50:
                break
        if 2 <= len(vals) <= 30:
            print(f"  Low-cardinality field '{k}': {len(vals)} unique values: {sorted(vals)[:20]}")

# Use task_field if found, otherwise try common alternatives
if task_field:
    task_counts = Counter(s[task_field] for s in all_samples)
    for task, count in sorted(task_counts.items(), key=lambda x: -x[1]):
        print(f"  {task}: {count}")
else:
    print("  (task field not identified yet - see above for candidates)")

# Shard distribution
print(f"\n{'=' * 70}")
print("SHARD COUNT DISTRIBUTION PER TASK TYPE")
print(f"{'=' * 70}")

if shard_field and task_field:
    # Check if shards is a list (use len) or an int
    sample0_shard = all_samples[0][shard_field]
    shard_is_list = isinstance(sample0_shard, list)
    if shard_is_list:
        print(f"  Note: '{shard_field}' is a list field. Using len(shards) as shard count.")

    def get_shard_count(s):
        v = s[shard_field]
        if isinstance(v, list):
            return len(v)
        return v

    task_shard_dist = defaultdict(Counter)
    for s in all_samples:
        task_shard_dist[s[task_field]][get_shard_count(s)] += 1

    for task in sorted(task_shard_dist.keys()):
        print(f"\n  Task: {task}")
        dist = task_shard_dist[task]
        for shard_val in sorted(dist.keys()):
            print(f"    shard={shard_val}: {dist[shard_val]}")
else:
    # Try to find them from first sample
    print("  Need to identify shard and task fields first.")
    print("  Printing first sample for inspection:")
    sample0 = all_samples[0]
    print(json.dumps({k: v if not isinstance(v, list) or len(str(v)) < 500 else f"[list of {len(v)} items]" for k, v in sample0.items()}, indent=2, default=str))

# Filter shard >= 5
print(f"\n{'=' * 70}")
print("SAMPLES WITH SHARD >= 5: CODE AND MATH COUNTS")
print(f"{'=' * 70}")

if shard_field and task_field:
    filtered = [s for s in all_samples if get_shard_count(s) >= 5]
    print(f"Total samples with shard_count >= 5: {len(filtered)}")
    filtered_task_counts = Counter(s[task_field] for s in filtered)
    for t in ["code", "math", "Code", "Math", "CODE", "MATH"]:
        if t in filtered_task_counts:
            print(f"  {t}: {filtered_task_counts[t]}")
    # Print all task counts in filtered set
    print(f"\n  All task counts in filtered set:")
    for task, count in sorted(filtered_task_counts.items(), key=lambda x: -x[1]):
        print(f"    {task}: {count}")
else:
    print("  (fields not identified - see above)")

# Print 2-3 complete sample JSONs
print(f"\n{'=' * 70}")
print("COMPLETE SAMPLE JSONS")
print(f"{'=' * 70}")

def find_sample(task_name, min_shard=5):
    """Find a sample with given task and minimum shard count."""
    if task_field and shard_field:
        for s in all_samples:
            if s[task_field].lower() == task_name.lower() and get_shard_count(s) >= min_shard:
                return s
    # Fallback: any sample with matching task
    if task_field:
        for s in all_samples:
            if s[task_field].lower() == task_name.lower():
                return s
    return None

code_sample = find_sample("code", 5)
math_sample = find_sample("math", 5)

if code_sample:
    sc = get_shard_count(code_sample) if shard_field else "N/A"
    print(f"\n--- CODE sample (shard_count={sc}) ---")
    clean = {k: v for k, v in code_sample.items() if k != "_split"}
    print(json.dumps(clean, indent=2, default=str, ensure_ascii=False))
else:
    print("\nNo 'code' sample found.")

if math_sample:
    sc = get_shard_count(math_sample) if shard_field else "N/A"
    print(f"\n--- MATH sample (shard_count={sc}) ---")
    clean = {k: v for k, v in math_sample.items() if k != "_split"}
    print(json.dumps(clean, indent=2, default=str, ensure_ascii=False))
else:
    print("\nNo 'math' sample found.")

# If neither found, print first 2 samples
if not code_sample and not math_sample:
    print("\nPrinting first 2 samples instead:")
    for i in range(min(2, len(all_samples))):
        s = all_samples[i]
        clean = {k: v for k, v in s.items() if k != "_split"}
        print(f"\n--- Sample {i} ---")
        print(json.dumps(clean, indent=2, default=str, ensure_ascii=False))

print(f"\n{'=' * 70}")
print("DONE")
print(f"{'=' * 70}")
