"""Compute MAVEN event type SCS (Semantic Confusability Score) matrix.

Uses sentence-transformers for lightweight type name embeddings.
Outputs:
  - configs/maven_event_types.json: type list
  - data/maven_scs_matrix.json: full SCS matrix + statistics
"""
import json
import os
import numpy as np
from pathlib import Path

import torch
import torch.nn.functional as F
from sentence_transformers import SentenceTransformer

PROJECT_ROOT = Path(".")
MAVEN_DATA = PROJECT_ROOT / "data" / "maven"

def extract_event_types():
    """Extract all 168 event types from MAVEN train.jsonl."""
    types = set()
    with open(MAVEN_DATA / "train.jsonl") as f:
        for line in f:
            doc = json.loads(line)
            for event in doc.get("events", []):
                types.add(event["type"])
    return sorted(types)

def compute_scs_matrix(type_names, model_name="all-MiniLM-L6-v2"):
    """Compute pairwise cosine similarity matrix using sentence-transformers."""
    print(f"Loading model: {model_name}")
    model = SentenceTransformer(model_name, cache_folder="~/.cache/huggingface")

    # Encode type names (with space-separated words from CamelCase/underscores)
    readable_names = [t.replace("_", " ") for t in type_names]
    print(f"Encoding {len(readable_names)} event types...")
    embeddings = model.encode(readable_names, convert_to_tensor=True, normalize_embeddings=True)

    # Pairwise cosine similarity
    scs_matrix = (embeddings @ embeddings.T).cpu().numpy()
    return scs_matrix

def analyze_scs(scs_matrix, type_names):
    """Compute statistics and find most confusable pairs."""
    n = len(type_names)

    # Extract upper triangle (excluding diagonal)
    upper_indices = np.triu_indices(n, k=1)
    upper_values = scs_matrix[upper_indices]

    stats = {
        "n_types": n,
        "n_pairs": len(upper_values),
        "mean": float(np.mean(upper_values)),
        "std": float(np.std(upper_values)),
        "min": float(np.min(upper_values)),
        "max": float(np.max(upper_values)),
        "median": float(np.median(upper_values)),
        "q75": float(np.percentile(upper_values, 75)),
        "q90": float(np.percentile(upper_values, 90)),
        "q95": float(np.percentile(upper_values, 95)),
    }

    # Top-20 most confusable pairs
    pair_scores = []
    for idx in range(len(upper_values)):
        i, j = upper_indices[0][idx], upper_indices[1][idx]
        pair_scores.append((float(upper_values[idx]), type_names[i], type_names[j]))
    pair_scores.sort(reverse=True)

    top_pairs = [{"type_a": p[1], "type_b": p[2], "scs": round(p[0], 4)} for p in pair_scores[:20]]

    return stats, top_pairs

def main():
    # Step 1: Extract event types
    print("Extracting MAVEN event types...")
    type_names = extract_event_types()
    print(f"Found {len(type_names)} event types")

    # Step 2: Save event types config
    configs_dir = PROJECT_ROOT / "configs"
    configs_dir.mkdir(exist_ok=True)
    types_path = configs_dir / "maven_event_types.json"
    with open(types_path, "w") as f:
        json.dump(type_names, f, indent=2)
    print(f"Saved event types to {types_path}")

    # Step 3: Compute SCS matrix
    scs_matrix = compute_scs_matrix(type_names)

    # Step 4: Analyze
    stats, top_pairs = analyze_scs(scs_matrix, type_names)

    print("\n=== SCS Statistics ===")
    for k, v in stats.items():
        print(f"  {k}: {v:.4f}" if isinstance(v, float) else f"  {k}: {v}")

    print("\n=== Top-20 Most Confusable Pairs ===")
    for p in top_pairs:
        print(f"  {p['scs']:.4f}  {p['type_a']} <-> {p['type_b']}")

    # Step 5: Save SCS matrix
    data_dir = PROJECT_ROOT / "data"
    scs_output = {
        "type_names": type_names,
        "scs_matrix": scs_matrix.tolist(),
        "statistics": stats,
        "top_confusable_pairs": top_pairs,
        "model": "all-MiniLM-L6-v2",
        "note": "SCS = pairwise cosine similarity of type name embeddings"
    }
    scs_path = data_dir / "maven_scs_matrix.json"
    with open(scs_path, "w") as f:
        json.dump(scs_output, f, indent=2)
    print(f"\nSaved SCS matrix to {scs_path}")

    # Step 6: Also save as .pt for compatibility with compute_bcs.py
    scs_tensor = torch.tensor(scs_matrix, dtype=torch.float32)
    type_to_idx = {name: i for i, name in enumerate(type_names)}
    torch.save({"sim_matrix": scs_tensor, "type_names": type_names, "type_to_idx": type_to_idx},
               data_dir / "maven_sim_matrix.pt")
    print(f"Saved maven_sim_matrix.pt")

if __name__ == "__main__":
    main()
