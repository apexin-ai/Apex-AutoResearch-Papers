"""
Build fully-crossed balanced datasets for Henderson Method I G-theory.

Produces two datasets:
  A) 3 models × bf16-only × all temps — for cross-model variance decomposition
  B) 2 models (Llama+Gemma) × bf16+fp32 × temps {0.3, 0.7} — for precision effect

Why these subsets:
  - Llama fp32 is entirely missing at temp=0.0 (100/144 conditions gone)
  - Mistral fp32 has gaps at ALL temps (~50/144 each), unusable for crossed design
  - Gemma fp32 is complete
"""

import json
import glob
import numpy as np
import pandas as pd
from pathlib import Path

MODEL_NAME_MAP = {
    'meta-llama/Llama-3.1-8B-Instruct': 'llama-3.1-8b-instruct',
    'google/gemma-2-9b-it': 'gemma-2-9b-it',
    'google/gemma-2-9b-it': 'gemma-2-9b-it',
    'mistralai/Mistral-7B-Instruct-v0.3': 'mistral-7b-instruct-v0.3',
}

FILE_PATTERNS = [
    'results/exp001_llama/llama_shard_*.jsonl',
    'results/exp001_gemma/shard_*.jsonl',
    'results/exp001_gemma_fp32/shard_*.jsonl',
    'results/exp001_mistral/shard_*.jsonl',
]


def load_all():
    records = []
    for pattern in FILE_PATTERNS:
        files = sorted(glob.glob(pattern))
        for f in files:
            with open(f) as fh:
                for line in fh:
                    records.append(json.loads(line))
        print(f"  {pattern}: {len(files)} files")
    return pd.DataFrame(records)


def verify_crossed(df, facets):
    """Verify the design is fully crossed: every factor combo has equal items."""
    cell_counts = df.groupby(facets).size()
    n_cells = len(cell_counts)
    expected_cells = 1
    for f in facets:
        expected_cells *= df[f].nunique()
    if n_cells != expected_cells:
        actual_levels = {f: df[f].nunique() for f in facets}
        raise ValueError(
            f"Not fully crossed: {n_cells} cells present, "
            f"expected {expected_cells} from levels {actual_levels}"
        )
    if cell_counts.min() != cell_counts.max():
        raise ValueError(
            f"Unequal cell sizes: min={cell_counts.min()}, max={cell_counts.max()}"
        )
    return n_cells, int(cell_counts.iloc[0])


def save_dataset(df, name, facets, output_dir):
    n_cells, items_per_cell = verify_crossed(df, facets)
    levels = {f: sorted(df[f].unique().tolist()) for f in facets}
    n_levels = {f: len(v) for f, v in levels.items()}

    csv_path = output_dir / f'{name}.csv'
    df.to_csv(csv_path, index=False)

    meta = {
        'name': name,
        'n_records': len(df),
        'n_cells': n_cells,
        'items_per_cell': items_per_cell,
        'facets': facets,
        'n_levels': n_levels,
        'factor_levels': {
            f: v if len(v) <= 20 else f'{len(v)} levels'
            for f, v in levels.items()
        },
        'fully_crossed': True,
    }
    meta_path = output_dir / f'{name}_meta.json'
    with open(meta_path, 'w') as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"\n  === {name} ===")
    print(f"  Records: {len(df)}")
    print(f"  Cells: {n_cells} (fully crossed)")
    print(f"  Items/cell: {items_per_cell}")
    print(f"  Levels: {n_levels}")
    print(f"  Saved: {csv_path}, {meta_path}")
    return meta


def main():
    print("Loading data...")
    df = load_all()
    print(f"Raw total: {len(df)}")

    df['model'] = df['model'].map(MODEL_NAME_MAP).fillna(df['model'])
    models = sorted(df['model'].unique())
    print(f"Models: {models}")

    output_dir = Path('results/analysis')
    output_dir.mkdir(parents=True, exist_ok=True)

    # ── Dataset A: 3 models × bf16 only × all temps ──
    print("\n--- Dataset A: 3-model bf16-only ---")
    df_a = df[df['precision'] == 'bfloat16'].copy()
    facets_a = ['model', 'temperature', 'prompt_template', 'seed', 'ordering']
    meta_a = save_dataset(df_a, 'cross_model_3way_bf16', facets_a, output_dir)

    # ── Dataset B: Llama+Gemma × bf16+fp32 × temp ∈ {0.3, 0.7} ──
    print("\n--- Dataset B: Llama+Gemma bf16+fp32, temp ∈ {0.3, 0.7} ---")
    target_models = ['llama-3.1-8b-instruct', 'gemma-2-9b-it']
    target_temps = [0.3, 0.7]
    target_precs = ['bfloat16', 'float32']
    df_b = df[
        (df['model'].isin(target_models)) &
        (df['precision'].isin(target_precs)) &
        (df['temperature'].isin(target_temps))
    ].copy()
    facets_b = ['model', 'precision', 'temperature', 'prompt_template', 'seed', 'ordering']
    meta_b = save_dataset(df_b, 'cross_model_2way_precision', facets_b, output_dir)

    # ── Dataset C (bonus): single-model Llama all-precision all-temp intersection ──
    print("\n--- Dataset C: Llama-only bf16+fp32, temp ∈ {0.3, 0.7} ---")
    df_c = df[
        (df['model'] == 'llama-3.1-8b-instruct') &
        (df['precision'].isin(['bfloat16', 'float32'])) &
        (df['temperature'].isin([0.3, 0.7]))
    ].copy()
    facets_c = ['precision', 'temperature', 'prompt_template', 'seed', 'ordering']
    meta_c = save_dataset(df_c, 'llama_precision_balanced', facets_c, output_dir)

    # ── Summary ──
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    for m in [meta_a, meta_b, meta_c]:
        print(f"  {m['name']}: {m['n_records']} records, {m['n_cells']} cells, "
              f"{m['items_per_cell']} items/cell, fully_crossed={m['fully_crossed']}")

    # Compare with old unbalanced
    old_path = output_dir / 'cross_model_llama_gemma.jsonl'
    if old_path.exists():
        old_count = sum(1 for _ in open(old_path))
        print(f"\n  Old unbalanced cross_model_llama_gemma.jsonl: {old_count} records")
        print(f"  New balanced 2-way: {meta_b['n_records']} records (fully crossed)")


if __name__ == '__main__':
    main()
