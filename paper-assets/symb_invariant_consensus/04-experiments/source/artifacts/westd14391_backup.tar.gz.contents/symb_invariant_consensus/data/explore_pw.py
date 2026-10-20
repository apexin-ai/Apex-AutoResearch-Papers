from datasets import load_dataset

names = [
    ("allenai/proofwriter-dataset-V2020.12.2", None),
    ("allenai/proofwriter-dataset-V2020.12.2", "OWA"),
    ("allenai/proofwriter-dataset-V2020.12.2", "depth-5"),
    ("allenai/proofwriter-dataset-V2020.12.2", "OWA-depth-5"),
]

for name, config in names:
    try:
        label = f"{name}" + (f" config={config}" if config else "")
        print(f"Trying: {label}")
        if config:
            ds = load_dataset(name, config)
        else:
            ds = load_dataset(name)
        print(f"  Splits: {list(ds.keys())}")
        for split_name in list(ds.keys())[:3]:
            print(f"  {split_name}: {len(ds[split_name])} rows, cols={ds[split_name].column_names}")
        first_split = list(ds.keys())[0]
        row = ds[first_split][0]
        print(f"  Sample row:")
        for k, v in row.items():
            print(f"    {k}: {str(v)[:200]}")
        break
    except Exception as e:
        print(f"  Failed: {str(e)[:150]}")
        continue
