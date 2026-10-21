from datasets import load_dataset

# Use streaming to explore without downloading all
ds = load_dataset("tasksource/proofwriter", split="validation", streaming=True)

configs_seen = {}
sample_shown = False
for i, row in enumerate(ds):
    cfg = row.get('config', 'unknown')
    configs_seen[cfg] = configs_seen.get(cfg, 0) + 1
    if not sample_shown and 'OWA' in cfg and 'D5' in cfg:
        print(f"Sample OWA-D5 row:")
        for k, v in row.items():
            print(f"  {k}: {str(v)[:300]}")
        sample_shown = True
    if i % 10000 == 0 and i > 0:
        print(f"Scanned {i} rows so far...")

print(f"\nTotal scanned: {i+1}")
print(f"\nConfig distribution:")
for c in sorted(configs_seen.keys()):
    print(f"  {c}: {configs_seen[c]}")
