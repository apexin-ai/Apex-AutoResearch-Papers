from datasets import load_dataset
import traceback

names = [
    "allenai/proofwriter-dataset-V2020.12.2",
    "proofwriter",
    "allenai/proofwriter",
    "theblackcat102/proofwriter",
    "tasksource/proofwriter",
]

for name in names:
    try:
        print(f"Trying: {name}")
        ds = load_dataset(name, trust_remote_code=True)
        print(f"  Splits: {list(ds.keys())}")
        for split_name in list(ds.keys())[:3]:
            print(f"  {split_name}: {len(ds[split_name])} rows, cols={ds[split_name].column_names}")
        # Show sample
        first_split = list(ds.keys())[0]
        row = ds[first_split][0]
        print(f"  Sample row keys: {list(row.keys())}")
        for k, v in row.items():
            print(f"    {k}: {str(v)[:200]}")
        break
    except Exception as e:
        print(f"  Failed: {str(e)[:200]}")
        continue
