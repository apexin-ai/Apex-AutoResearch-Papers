# Topic drift descriptive analysis for reviewer response
# Measures semantic drift across generation depths and correlates with depth features

import json
import os
import glob
import numpy as np
import pandas as pd
from collections import defaultdict
from scipy.stats import spearmanr
from sentence_transformers import SentenceTransformer

DATA_DIR = "/root/gen-depth-fingerprint/data"
RESULTS_DIR = "/root/gen-depth-fingerprint/results"
os.makedirs(RESULTS_DIR, exist_ok=True)

DEVICE = "cuda:0"

# --- Data loading ---

CONTINUATION_DIRS = {
    "pythia-2.8b": "pythia-2.8b-continuation",
    "pythia-1b": "pythia-1b",
    "olmo-2-1b": "olmo-2-1b",
    "qwen3-0.6b": "qwen3-0.6b",
    "qwen3-1.7b": "qwen3-1.7b",
    "qwen3-8b": "qwen3-8b",
}

PROMPT_TYPE_DIRS = {
    "continuation": "pythia-2.8b-continuation",
    "elaboration": "pythia-2.8b-elaboration",
    "inspired_rewriting": "pythia-2.8b-inspired_rewriting",
}


def load_generations(subdir):
    """Load all generation records from a data subdirectory."""
    records = []
    pattern = os.path.join(DATA_DIR, subdir, "generations*.jsonl")
    for fpath in sorted(glob.glob(pattern)):
        with open(fpath) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
    return records


def build_chains(records):
    """Group records into chains keyed by (model, seed_id), sorted by depth."""
    chains = defaultdict(dict)
    for r in records:
        model = r.get("model", "unknown")
        seed = r["seed_id"]
        depth = r["depth"]
        chains[(model, seed)][depth] = r["text"]
    return chains


# --- Main ---

print("Loading generation data...")
all_cont_records = []
for model_name, subdir in CONTINUATION_DIRS.items():
    recs = load_generations(subdir)
    print(f"  {model_name}: {len(recs)} records")
    all_cont_records.extend(recs)

prompt_type_records = {}
for pt, subdir in PROMPT_TYPE_DIRS.items():
    recs = load_generations(subdir)
    print(f"  prompt_type={pt}: {len(recs)} records")
    prompt_type_records[pt] = recs

# Build chains for continuation models
cont_chains = build_chains(all_cont_records)
print(f"Total continuation chains: {len(cont_chains)}")

# Collect all unique texts and their indices for batch embedding
print("Collecting texts for embedding...")
text_list = []
text_index = {}  # (model, seed, depth) -> index in text_list

for (model, seed), depth_map in cont_chains.items():
    for depth in sorted(depth_map.keys()):
        key = (model, seed, depth)
        text_index[key] = len(text_list)
        text_list.append(depth_map[depth])

# Also collect prompt type texts
pt_chains = {}
for pt, recs in prompt_type_records.items():
    chains = build_chains(recs)
    pt_chains[pt] = chains
    for (model, seed), depth_map in chains.items():
        for depth in sorted(depth_map.keys()):
            key = (f"pt_{pt}", seed, depth)
            if key not in text_index:
                text_index[key] = len(text_list)
                text_list.append(depth_map[depth])

print(f"Total texts to embed: {len(text_list)}")

# Compute embeddings
print("Computing sentence embeddings with all-MiniLM-L6-v2...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device=DEVICE)
embeddings = model.encode(text_list, batch_size=256, show_progress_bar=True,
                          convert_to_numpy=True, normalize_embeddings=True)
print(f"Embeddings shape: {embeddings.shape}")


def cosine_sim(a, b):
    return float(np.dot(a, b))


# --- Report (a): Semantic similarity by depth transition ---

print("\n=== (a) Semantic similarity by depth transition ===")
transition_sims = defaultdict(list)

for (model_name, seed), depth_map in cont_chains.items():
    depths = sorted(depth_map.keys())
    for i in range(1, len(depths)):
        d_prev, d_curr = depths[i - 1], depths[i]
        if d_curr - d_prev != 1:
            continue
        idx_prev = text_index[(model_name, seed, d_prev)]
        idx_curr = text_index[(model_name, seed, d_curr)]
        sim = cosine_sim(embeddings[idx_prev], embeddings[idx_curr])
        transition_sims[f"{d_prev}_to_{d_curr}"].append(sim)

sim_by_transition = {}
for trans in sorted(transition_sims.keys()):
    vals = transition_sims[trans]
    m, s = np.mean(vals), np.std(vals)
    sim_by_transition[trans] = {"mean": round(float(m), 4), "std": round(float(s), 4), "n": len(vals)}
    print(f"  {trans}: mean={m:.4f} ± {s:.4f} (n={len(vals)})")


# --- Report (b): Prompt type comparison (Pythia-2.8B only) ---

print("\n=== (b) Prompt type comparison ===")
prompt_type_results = {}

for pt, chains in pt_chains.items():
    pt_trans_sims = defaultdict(list)
    all_sims = []
    for (model_name, seed), depth_map in chains.items():
        depths = sorted(depth_map.keys())
        for i in range(1, len(depths)):
            d_prev, d_curr = depths[i - 1], depths[i]
            if d_curr - d_prev != 1:
                continue
            idx_prev = text_index[(f"pt_{pt}", seed, d_prev)]
            idx_curr = text_index[(f"pt_{pt}", seed, d_curr)]
            sim = cosine_sim(embeddings[idx_prev], embeddings[idx_curr])
            pt_trans_sims[f"{d_prev}_to_{d_curr}"].append(sim)
            all_sims.append(sim)

    trans_summary = {}
    for trans in sorted(pt_trans_sims.keys()):
        vals = pt_trans_sims[trans]
        trans_summary[trans] = {"mean": round(float(np.mean(vals)), 4),
                                "std": round(float(np.std(vals)), 4)}

    avg_sim = round(float(np.mean(all_sims)), 4) if all_sims else None
    prompt_type_results[pt] = {"avg_sim": avg_sim, "sim_by_transition": trans_summary}
    print(f"  {pt}: avg_sim={avg_sim}, transitions={trans_summary}")


# --- Compute cumulative semantic drift for correlation analysis ---

print("\n=== Computing cumulative semantic drift ===")
# For each (model, seed, depth>0): cumulative cosine distance from depth 0
drift_records = []

for (model_name, seed), depth_map in cont_chains.items():
    depths = sorted(depth_map.keys())
    cum_drift = 0.0
    for i in range(1, len(depths)):
        d_prev, d_curr = depths[i - 1], depths[i]
        if d_curr - d_prev != 1:
            cum_drift = None
            break
        idx_prev = text_index[(model_name, seed, d_prev)]
        idx_curr = text_index[(model_name, seed, d_curr)]
        sim = cosine_sim(embeddings[idx_prev], embeddings[idx_curr])
        cum_drift += (1.0 - sim)
        drift_records.append({
            "model_name": model_name,
            "seed_id": seed,
            "depth": d_curr,
            "step_cosine_dist": 1.0 - sim,
            "cumulative_drift": cum_drift,
        })

drift_df = pd.DataFrame(drift_records)
print(f"Drift records: {len(drift_df)}")

# Load features
features_df = pd.read_csv(os.path.join(DATA_DIR, "features_all_models.csv"))
print(f"Features records: {len(features_df)}")

# Merge
merged = drift_df.merge(features_df, on=["model_name", "seed_id", "depth"], how="inner")
print(f"Merged records: {len(merged)}")


# --- Report (c): Shape features vs semantic drift ---

print("\n=== (c) Shape feature correlations ===")
shape_features = ["entropy_std", "tail_decay"]
shape_corr = {}

for feat in shape_features:
    valid = merged[[feat, "cumulative_drift"]].dropna()
    rho, p = spearmanr(valid[feat], valid["cumulative_drift"])
    shape_corr[f"{feat}_vs_semantic_drift"] = {"rho": round(float(rho), 4), "p": round(float(p), 6)}
    print(f"  {feat} vs cumulative_drift: rho={rho:.4f}, p={p:.2e}")


# --- Report (d): Drifting features vs semantic drift ---

print("\n=== (d) Drifting feature correlations ===")
drifting_features = ["hapax_ratio", "ttr", "entropy_mean"]
drifting_corr = {}

for feat in drifting_features:
    valid = merged[[feat, "cumulative_drift"]].dropna()
    rho, p = spearmanr(valid[feat], valid["cumulative_drift"])
    drifting_corr[f"{feat}_vs_semantic_drift"] = {"rho": round(float(rho), 4), "p": round(float(p), 6)}
    print(f"  {feat} vs cumulative_drift: rho={rho:.4f}, p={p:.2e}")


# --- Save results ---

results = {
    "semantic_similarity_by_transition": sim_by_transition,
    "prompt_type_comparison": prompt_type_results,
    "shape_feature_correlations": shape_corr,
    "drifting_feature_correlations": drifting_corr,
}

out_path = os.path.join(RESULTS_DIR, "review_topic_drift_results.json")
with open(out_path, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {out_path}")
print(json.dumps(results, indent=2))
