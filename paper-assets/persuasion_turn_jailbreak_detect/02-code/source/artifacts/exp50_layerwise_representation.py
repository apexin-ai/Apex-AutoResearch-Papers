"""exp50: Layer-wise representation analysis (PR + Fisher) across DeBERTa layers."""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

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
MAX_LENGTH = 256
ARCHIVE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive")
OUT_PATH = PROJ / "results/exp50_layerwise_results.json"
FIG_DIR = PROJ / "figures/paper"

PRETRAINED_PATH = "/root/.cache/huggingface/hub/models--microsoft--deberta-v3-base/snapshots/de19fe7db5162df5f3d8f0b41321c0267288fd74"
TOKENIZER_PATH = str(ARCHIVE / "plan_017_mlm/best")

VARIANTS = OrderedDict({
    "vanilla": {"type": "pretrained", "path": PRETRAINED_PATH},
    "9-class": {
        "type": "multitask",
        "path": str(ARCHIVE / "plan_002/deberta_multitask/best/model.pt"),
    },
    "scrambled": {
        "type": "multitask",
        "path": str(ARCHIVE / "plan_003_scrambled_fix/deberta_multitask/best/model.pt"),
    },
    "JB-MLM": {
        "type": "safetensors",
        "path": str(ARCHIVE / "plan_017_mlm/best"),
    },
})

DATA_FILES = {
    "iid_test": PROJ / "data/plan_002_splits/test.jsonl",
    "dd_ood": PROJ / "data/generated/deceptive_delight_all.jsonl",
    "aa_ood": PROJ / "data/actorattack_ood/actorattack_all.jsonl",
}

COLORS = {
    "9-class": "#2ca02c",
    "scrambled": "#a8d08d",
    "JB-MLM": "#ff7f0e",
    "vanilla": "#1f77b4",
}
MARKERS = {
    "9-class": "o",
    "scrambled": "s",
    "JB-MLM": "^",
    "vanilla": "D",
}


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def load_encoder(variant_info):
    vtype = variant_info["type"]
    if vtype in ("pretrained", "safetensors"):
        model = AutoModel.from_pretrained(variant_info["path"], torch_dtype=torch.float32)
    elif vtype == "multitask":
        sd = torch.load(variant_info["path"], map_location="cpu", weights_only=False)
        deberta_sd = {}
        for k, v in sd.items():
            if k.startswith("deberta."):
                deberta_sd[k[len("deberta."):]] = v
        config = AutoConfig.from_pretrained(PRETRAINED_PATH)
        model = AutoModel.from_config(config)
        model.load_state_dict(deberta_sd, strict=False)
        model = model.float()
    else:
        raise ValueError(f"Unknown type: {vtype}")
    model.to(DEVICE).eval()
    return model


def extract_layerwise_cls(model, tokenizer, conversations, batch_size=16):
    """Extract [CLS] hidden states from all layers for all samples."""
    all_texts = []
    for conv in conversations:
        user_turns = extract_user_turns(conv)
        all_texts.append(" [SEP] ".join(user_turns))

    num_layers = model.config.num_hidden_layers + 1  # +1 for embedding layer
    layer_embeddings = [[] for _ in range(num_layers)]

    for i in range(0, len(all_texts), batch_size):
        batch_texts = all_texts[i:i + batch_size]
        inputs = tokenizer(
            batch_texts, max_length=MAX_LENGTH, padding=True,
            truncation=True, return_tensors="pt"
        ).to(DEVICE)

        with torch.no_grad():
            outputs = model(**inputs, output_hidden_states=True)

        for layer_idx, hidden_state in enumerate(outputs.hidden_states):
            cls_emb = hidden_state[:, 0, :].cpu().numpy()
            layer_embeddings[layer_idx].append(cls_emb)

    for layer_idx in range(num_layers):
        layer_embeddings[layer_idx] = np.concatenate(layer_embeddings[layer_idx], axis=0)

    return layer_embeddings


def compute_participation_ratio(embeddings):
    """PR = (Σσ_i)² / Σσ_i²"""
    centered = embeddings - embeddings.mean(axis=0, keepdims=True)
    _, s, _ = np.linalg.svd(centered, full_matrices=False)
    s2 = s ** 2
    pr = (s2.sum()) ** 2 / (s2 ** 2).sum()
    return round(float(pr), 4)


def compute_fisher_ratio(embeddings, labels):
    """Fisher = inter_class_distance² / (intra_jb + intra_benign)"""
    labels = np.array(labels)
    jb_mask = labels == 1
    benign_mask = labels == 0

    jb_emb = embeddings[jb_mask]
    benign_emb = embeddings[benign_mask]

    if len(jb_emb) < 2 or len(benign_emb) < 2:
        return 0.0

    jb_centroid = jb_emb.mean(axis=0)
    benign_centroid = benign_emb.mean(axis=0)

    jb_intra = np.mean(np.sum((jb_emb - jb_centroid) ** 2, axis=1))
    benign_intra = np.mean(np.sum((benign_emb - benign_centroid) ** 2, axis=1))

    inter_dist_sq = np.sum((jb_centroid - benign_centroid) ** 2)

    denom = jb_intra + benign_intra
    if denom < 1e-10:
        return 0.0
    return round(float(inter_dist_sq / denom), 6)


def plot_results(results):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    FIG_DIR.mkdir(parents=True, exist_ok=True)

    variant_names = list(results.keys())
    num_layers = len(results[variant_names[0]])
    layers = list(range(num_layers))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))

    for name in variant_names:
        pr_vals = [results[name][f"layer_{l}"]["pr"] for l in layers]
        fisher_vals = [results[name][f"layer_{l}"]["fisher"] for l in layers]

        ax1.plot(layers, pr_vals, color=COLORS[name], marker=MARKERS[name],
                 label=name, linewidth=2, markersize=6)
        fisher_plot = [max(v, 1e-8) for v in fisher_vals]
        ax2.plot(layers, fisher_plot, color=COLORS[name], marker=MARKERS[name],
                 label=name, linewidth=2, markersize=6)

    ax1.set_xlabel("Layer", fontsize=12)
    ax1.set_ylabel("Participation Ratio", fontsize=12)
    ax1.set_title("(a) Participation Ratio by Layer", fontsize=13)
    ax1.set_xticks(layers)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)

    ax2.set_xlabel("Layer", fontsize=12)
    ax2.set_ylabel("Fisher Ratio (log scale)", fontsize=12)
    ax2.set_title("(b) Fisher Ratio by Layer", fontsize=13)
    ax2.set_yscale("log")
    ax2.set_xticks(layers)
    ax2.legend(fontsize=10)
    ax2.grid(True, alpha=0.3)

    plt.tight_layout()
    fig.savefig(FIG_DIR / "fig_layerwise_representation.pdf", bbox_inches="tight", dpi=300)
    fig.savefig(FIG_DIR / "fig_layerwise_representation.png", bbox_inches="tight", dpi=300)
    plt.close()
    print(f"Figures saved to {FIG_DIR}/fig_layerwise_representation.{{pdf,png}}")


def main():
    print("=== exp50: Layer-wise Representation Analysis ===")
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_PATH)
    print("Tokenizer loaded")

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

    results = {}

    for name, info in VARIANTS.items():
        print(f"\n--- Processing: {name} ---")
        try:
            model = load_encoder(info)
            layer_embeddings = extract_layerwise_cls(model, tokenizer, all_convs, batch_size=16)
            print(f"  Extracted {len(layer_embeddings)} layers, shape per layer: {layer_embeddings[0].shape}")

            results[name] = {}
            for layer_idx, emb in enumerate(layer_embeddings):
                pr = compute_participation_ratio(emb)
                fisher = compute_fisher_ratio(emb, all_labels)
                results[name][f"layer_{layer_idx}"] = {"pr": pr, "fisher": fisher}
                print(f"  Layer {layer_idx:2d}: PR={pr:8.2f}, Fisher={fisher:.6f}")

            del model, layer_embeddings
            torch.cuda.empty_cache()
        except Exception as e:
            print(f"  FAILED: {e}")
            import traceback; traceback.print_exc()

    output = {
        "experiment": "exp50_layerwise_representation",
        "data": data_counts,
        "total_samples": len(all_convs),
        "n_jailbreak": sum(all_labels),
        "n_benign": len(all_labels) - sum(all_labels),
        "variants": results,
    }
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}")

    print("\n=== Summary ===")
    for name in results:
        print(f"\n{name}:")
        print(f"  {'Layer':>6} {'PR':>10} {'Fisher':>12}")
        for l in range(len(results[name])):
            r = results[name][f"layer_{l}"]
            print(f"  {l:>6d} {r['pr']:>10.2f} {r['fisher']:>12.6f}")

    plot_results(results)
    print("\nDone.")


if __name__ == "__main__":
    main()
