from datasets import load_dataset

ds = load_dataset("tasksource/proofwriter", split="validation")
print(f"Columns: {ds.column_names}")
print(f"Total rows: {len(ds)}")

# Check unique config values
configs = set(ds['config'])
print(f"\nUnique configs ({len(configs)}):")
for c in sorted(configs):
    count = sum(1 for x in ds['config'] if x == c)
    print(f"  {c}: {count}")
