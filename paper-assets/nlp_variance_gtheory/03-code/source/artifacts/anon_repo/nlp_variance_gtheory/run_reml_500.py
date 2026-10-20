import os
os.environ["OPENBLAS_NUM_THREADS"] = "2"

import sys
sys.path.insert(0, ".")

import json
import pandas as pd
from src.analysis.reml_em import reml_em, ALL_FACETS

df = pd.read_csv("results/analysis/cross_model_llama_gemma.csv")
for f in ALL_FACETS:
    df[f] = df[f].astype(str)

if "binary_correct" not in df.columns:
    df["binary_correct"] = df["correct"]

print(f"Data: {len(df)} rows, {df['model'].nunique()} models")
print(f"Facets: {ALL_FACETS}")

result = reml_em(df, "binary_correct", ALL_FACETS, max_iter=500, tol=1e-8)

outpath = "results/analysis/cross_model_reml_500iter.json"
with open(outpath, "w") as f:
    json.dump(result, f, indent=2)
print(f"\n-> {outpath}")
print(f"Converged: {result['converged']}, Iterations: {result['n_iterations']}")
