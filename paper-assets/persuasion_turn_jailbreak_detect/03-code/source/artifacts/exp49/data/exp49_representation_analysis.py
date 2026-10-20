"""exp49: Representation analysis for optimization regularization evidence.

Three analyses:
A1 - Weight norm distance from pretrained
A2 - SVD geometry (participation ratio, spectral decay)
A3 - Intra-class clustering (Fisher ratio)
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
import json
import numpy as np
import torch
from pathlib import Path
from collections import OrderedDict

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from transformers import AutoModel, AutoTokenizer, AutoConfig

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
DEVICE = torch.device("cuda:0")
MODEL_NAME = "microsoft/deberta-v3-base"
MAX_LENGTH = 256
ARCHIVE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive")
OUT_PATH = PROJ / "results/exp49_representation_analysis.json"

VARIANTS = OrderedDict({
    "vanilla": {"type": "pretrained", "path": MODEL_NAME},
    "9-class": {
        "type": "multitask",
        "path": str(ARCHIVE / "plan_002/deberta_multitask/best/model.pt"),
    },
    "scrambled": {
        "type": "multitask",
        "path": str(ARCHIVE / "plan_003_scrambled_fix/deberta_multitask/best/model.pt"),
    },
    "binary": {
        "type": "multitask",
        "path": str(ARCHIVE / "mf1_binary_seed42/deberta_multitask/best/model.pt"),
    },
    "topic": {
        "type": "multitask",
        "path": str(ARCHIVE / "plan_016v2_topic/best/model.pt"),
    },
    "JB-MLM": {
        "type": "safetensors",
        "path": str(ARCHIVE / "plan_017_mlm/best"),
    },
    "wiki-MLM": {
        "type": "safetensors",
        "path": str(ARCHIVE / "plan_018_wiki_mlm/best"),
    },
})

DATA_FILES = {
    "iid_test": PROJ / "data/plan_002_splits/test.jsonl",
    "dd_ood": PROJ / "data/generated/deceptive_delight_all.jsonl",
    "aa_ood": PROJ / "data/actorattack_ood/actorattack_all.jsonl",
}


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def load_encoder(variant_info):
    vtype = variant_info["type"]
    if vtype == "pretrained":
        model = AutoModel.from_pretrained(variant_info["path"], torch_dtype=torch.float32)
    elif vtype == "safetensors":
        model = AutoModel.from_pretrained(variant_info["path"], torch_dtype=torch.float32)
    elif vtype == "multitask":
        sd = torch.load(variant_info["path"], map_location="cpu", weights_only=False)
        deberta_sd = {}
        for k, v in sd.items():
            if k.startswith("deberta."):
                deberta_sd[k[len("deberta."):]] = v
        config = AutoConfig.from_pretrained(MODEL_NAME)
        model = AutoModel.from_config(config)
        model.load_state_dict(deberta_sd, strict=False)
        model = model.float()
    else:
        raise ValueError(f"Unknown type: {vtype}")
    model.to(DEVICE).eval()
    return model


def get_pretrained_state_dict():
    model = AutoModel.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)
    sd = {k: v.cpu() for k, v in model.state_dict().items()}
    del model
    torch.cuda.empty_cache()
    return sd


# === A1: Weight Norm Analysis ===
def weight_norm_analysis(pretrained_sd, variants):
    print("\n=== A1: Weight Norm Analysis ===")
    results = {}

    for name, info in variants.items():
        if name == "vanilla":
            results[name] = {"overall_l2": 0.0, "relative_norm": 0.0, "per_layer": {}}
            print(f"  {name}: L2=0 (baseline)")
            continue

        try:
            model = load_encoder(info)
            variant_sd = {k: v.cpu() for k, v in model.state_dict().items()}
            del model
            torch.cuda.empty_cache()
        except Exception as e:
            print(f"  {name}: SKIP ({e})")
            continue

        all_diffs_sq = []
        all_pretrained_sq = []
        per_layer = {}

        for key in pretrained_sd:
            if key not in variant_sd:
                continue
            diff = (variant_sd[key].float() - pretrained_sd[key].float())
            layer_l2 = diff.norm().item()
            pretrained_norm = pretrained_sd[key].float().norm().item()

            layer_name = ".".join(key.split(".")[:4])
            if layer_name not in per_layer:
                per_layer[layer_name] = {"l2": 0.0, "pretrained_norm": 0.0}
            per_layer[layer_name]["l2"] += layer_l2 ** 2
            per_layer[layer_name]["pretrained_norm"] += pretrained_norm ** 2

            all_diffs_sq.append(diff.flatten())
            all_pretrained_sq.append(pretrained_sd[key].float().flatten())

        all_diff = torch.cat(all_diffs_sq)
        all_pre = torch.cat(all_pretrained_sq)
        overall_l2 = all_diff.norm().item()
        relative_norm = overall_l2 / all_pre.norm().item()

        for ln in per_layer:
            per_layer[ln]["l2"] = per_layer[ln]["l2"] ** 0.5
            per_layer[ln]["pretrained_norm"] = per_layer[ln]["pretrained_norm"] ** 0.5
            if per_layer[ln]["pretrained_norm"] > 0:
                per_layer[ln]["relative"] = per_layer[ln]["l2"] / per_layer[ln]["pretrained_norm"]

        results[name] = {
            "overall_l2": round(overall_l2, 4),
            "relative_norm": round(relative_norm, 6),
            "per_layer": {k: {kk: round(vv, 4) for kk, vv in v.items()} for k, v in per_layer.items()},
        }
        print(f"  {name}: L2={overall_l2:.4f}, relative={relative_norm:.6f}")

    return results


# === A2: SVD Geometry ===
@torch.no_grad()
def extract_all_cls(model, tokenizer, convs):
    embeddings = []
    for conv in convs:
        user_turns = extract_user_turns(conv)
        if not user_turns:
            continue
        enc = tokenizer(
            user_turns, max_length=MAX_LENGTH, padding=True,
            truncation=True, return_tensors="pt"
        ).to(DEVICE)
        outputs = model(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        cls_embs = outputs.last_hidden_state[:, 0, :]
        conv_emb = cls_embs.mean(dim=0).cpu().numpy()
        embeddings.append(conv_emb)
    return np.stack(embeddings)


def svd_geometry(embeddings):
    emb_centered = embeddings - embeddings.mean(axis=0, keepdims=True)
    _, S, _ = np.linalg.svd(emb_centered, full_matrices=False)

    S_sq = S ** 2
    total_var = S_sq.sum()
    participation_ratio = (S.sum()) ** 2 / S_sq.sum()
    top10_idx = max(1, len(S) // 10)
    top10_var_ratio = S_sq[:top10_idx].sum() / total_var

    return {
        "participation_ratio": round(float(participation_ratio), 2),
        "top10_variance_ratio": round(float(top10_var_ratio), 4),
        "effective_dim_90": int(np.searchsorted(np.cumsum(S_sq) / total_var, 0.9) + 1),
        "num_samples": embeddings.shape[0],
        "embedding_dim": embeddings.shape[1],
        "top20_singular_values": [round(float(s), 4) for s in S[:20]],
    }


# === A3: Clustering ===
def clustering_metrics(embeddings, labels):
    jb_mask = np.array(labels) == 1
    benign_mask = np.array(labels) == 0

    jb_embs = embeddings[jb_mask]
    benign_embs = embeddings[benign_mask]

    def cosine_sim_matrix(X):
        norms = np.linalg.norm(X, axis=1, keepdims=True)
        norms = np.clip(norms, 1e-8, None)
        X_norm = X / norms
        return X_norm @ X_norm.T

    def avg_intra_dist(X):
        sim = cosine_sim_matrix(X)
        n = len(X)
        if n < 2:
            return 0.0
        mask = np.ones((n, n), dtype=bool)
        np.fill_diagonal(mask, False)
        return float(1.0 - sim[mask].mean())

    jb_intra = avg_intra_dist(jb_embs) if len(jb_embs) > 1 else 0.0
    benign_intra = avg_intra_dist(benign_embs) if len(benign_embs) > 1 else 0.0

    jb_centroid = jb_embs.mean(axis=0)
    benign_centroid = benign_embs.mean(axis=0)
    jb_norm = np.linalg.norm(jb_centroid)
    benign_norm = np.linalg.norm(benign_centroid)
    if jb_norm > 1e-8 and benign_norm > 1e-8:
        inter_sim = float(np.dot(jb_centroid, benign_centroid) / (jb_norm * benign_norm))
    else:
        inter_sim = 0.0
    inter_dist = 1.0 - inter_sim

    denom = jb_intra + benign_intra
    fisher_ratio = (inter_dist ** 2) / denom if denom > 1e-8 else 0.0

    return {
        "jb_intra_var": round(jb_intra, 6),
        "benign_intra_var": round(benign_intra, 6),
        "inter_class_dist": round(inter_dist, 6),
        "inter_class_sim": round(inter_sim, 6),
        "fisher_ratio": round(fisher_ratio, 6),
        "n_jailbreak": int(jb_mask.sum()),
        "n_benign": int(benign_mask.sum()),
    }


def main():
    print("=== exp49: Representation Analysis ===")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    print("Tokenizer loaded")

    # Load test data
    all_convs = []
    all_labels = []
    data_counts = {}
    for dname, dpath in DATA_FILES.items():
        convs = load_jsonl(dpath)
        data_counts[dname] = len(convs)
        for c in convs:
            all_convs.append(c)
            all_labels.append(1 if c["label"] == "jailbreak" else 0)
    print(f"Data loaded: {data_counts}, total={len(all_convs)}")

    # A1: Weight norm
    print("\nLoading pretrained weights for A1...")
    pretrained_sd = get_pretrained_state_dict()
    weight_results = weight_norm_analysis(pretrained_sd, VARIANTS)
    del pretrained_sd

    # A2 + A3: Need embeddings
    svd_results = {}
    cluster_results = {}

    for name, info in VARIANTS.items():
        print(f"\nExtracting embeddings: {name}...")
        try:
            model = load_encoder(info)
            embeddings = extract_all_cls(model, tokenizer, all_convs)
            print(f"  Shape: {embeddings.shape}")

            svd_results[name] = svd_geometry(embeddings)
            print(f"  PR={svd_results[name]['participation_ratio']}, "
                  f"top10_var={svd_results[name]['top10_variance_ratio']:.4f}, "
                  f"eff_dim_90={svd_results[name]['effective_dim_90']}")

            cluster_results[name] = clustering_metrics(embeddings, all_labels)
            print(f"  Fisher={cluster_results[name]['fisher_ratio']:.6f}, "
                  f"inter_dist={cluster_results[name]['inter_class_dist']:.6f}")

            del model, embeddings
            torch.cuda.empty_cache()
        except Exception as e:
            print(f"  SKIP ({e})")
            import traceback
            traceback.print_exc()

    results = {
        "experiment": "exp49_representation_analysis",
        "data": data_counts,
        "total_samples": len(all_convs),
        "weight_norm": weight_results,
        "svd_geometry": svd_results,
        "clustering": cluster_results,
    }

    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}")

    # Print summary tables
    print("\n" + "=" * 70)
    print("SUMMARY TABLES")
    print("=" * 70)

    print("\n--- Weight Distance from Pretrained ---")
    print(f"{'Variant':<12} {'Overall L2':>12} {'Relative Norm':>15}")
    for name in VARIANTS:
        if name in weight_results:
            w = weight_results[name]
            print(f"{name:<12} {w['overall_l2']:>12.4f} {w['relative_norm']:>15.6f}")

    print("\n--- SVD Geometry ---")
    print(f"{'Variant':<12} {'PR':>8} {'Top10 Var%':>12} {'Eff Dim 90%':>13}")
    for name in VARIANTS:
        if name in svd_results:
            s = svd_results[name]
            print(f"{name:<12} {s['participation_ratio']:>8.2f} "
                  f"{s['top10_variance_ratio']*100:>11.2f}% "
                  f"{s['effective_dim_90']:>13d}")

    print("\n--- Clustering (Fisher Ratio) ---")
    print(f"{'Variant':<12} {'JB Intra':>10} {'Benign Intra':>14} {'Inter Dist':>12} {'Fisher':>10}")
    for name in VARIANTS:
        if name in cluster_results:
            c = cluster_results[name]
            print(f"{name:<12} {c['jb_intra_var']:>10.6f} {c['benign_intra_var']:>14.6f} "
                  f"{c['inter_class_dist']:>12.6f} {c['fisher_ratio']:>10.6f}")


if __name__ == "__main__":
    main()
