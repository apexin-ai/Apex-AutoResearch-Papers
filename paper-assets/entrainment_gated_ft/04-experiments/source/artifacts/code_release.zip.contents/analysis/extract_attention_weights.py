"""
exp-004: Extract attention weight patterns from hybrid-3-1 models.

For each sample in LAMBADA, extracts the last-token attention distribution
from all 8 attention layers across GatedDeltaNet/RetNet/HGRN2 hybrid-3-1 models.
Uses manual Q@K^T computation since Flash Attention doesn't return weights.

Usage:
    python extract_attention_weights.py --arch gdn --device cuda:0 --output_dir ./results
    python extract_attention_weights.py --arch retnet --device cuda:0 --output_dir ./results
    python extract_attention_weights.py --arch hgrn2 --device cuda:0 --output_dir ./results
    python extract_attention_weights.py --analyze --output_dir ./results
"""

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
import torch
import torch.nn.functional as F
from einops import rearrange
from tqdm import tqdm

# ── Config ──────────────────────────────────────────────────────────────────

ATTN_LAYER_INDICES = [2, 5, 8, 11, 14, 17, 20, 23]  # 8 attention layers in h3-1

MODEL_PATHS = {
    "gdn":    "/root/autodl-tmp/models_1.3b/1.3B-100B-GatedDeltaNet-hybrid-3-1",
    "retnet": "/root/autodl-tmp/models_1.3b/1.3B-100B-RetNet-hybrid-3-1",
    "hgrn2":  "/root/autodl-tmp/models_1.3b/1.3B-100B-HGRN2-hybrid-3-1",
}

SAMPLE_DATA_PATH = "/root/entrainment_gated_ft/analysis/sample_perplexity_results.csv"

ARCH_TO_LABEL = {"gdn": "GDN", "retnet": "RetNet", "hgrn2": "HGRN2"}


# ── Model loading ───────────────────────────────────────────────────────────

def load_model_and_tokenizer(arch: str, device: str):
    from transformers import AutoTokenizer

    model_path = MODEL_PATHS[arch]

    if arch == "gdn":
        from fla.models.gated_deltanet import GatedDeltaNetForCausalLM
        model = GatedDeltaNetForCausalLM.from_pretrained(
            model_path, trust_remote_code=True, dtype=torch.float16, device_map=device
        )
    elif arch == "retnet":
        from fla.models.retnet import RetNetForCausalLM
        model = RetNetForCausalLM.from_pretrained(
            model_path, trust_remote_code=True, dtype=torch.float16, device_map=device
        )
    elif arch == "hgrn2":
        from fla.models.hgrn2 import HGRN2ForCausalLM
        if not hasattr(HGRN2ForCausalLM, '_tied_weights_keys') or \
                isinstance(HGRN2ForCausalLM._tied_weights_keys, list):
            HGRN2ForCausalLM._tied_weights_keys = {}
        model = HGRN2ForCausalLM.from_pretrained(
            model_path, trust_remote_code=True, dtype=torch.float16, device_map=device
        )
    else:
        raise ValueError(f"Unknown arch: {arch}")

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model.eval()
    return model, tokenizer


# ── Attention weight extraction via hooks ───────────────────────────────────

class AttentionWeightExtractor:

    def __init__(self, model, layer_indices: list[int]):
        self.layer_indices = layer_indices
        self.hooks = []
        self.captured = {}

        for idx in layer_indices:
            attn_module = model.model.layers[idx].attn
            hook = attn_module.register_forward_hook(self._make_hook(idx), with_kwargs=True)
            self.hooks.append(hook)

    def _make_hook(self, layer_idx: int):
        def hook_fn(module, args, kwargs, outputs):
            hidden_states = args[0] if args else kwargs['hidden_states']
            batch_size, seq_len, _ = hidden_states.size()

            with torch.no_grad():
                q = rearrange(module.q_proj(hidden_states), '... (h d) -> ... h d', d=module.head_dim)
                k = rearrange(module.k_proj(hidden_states), '... (h d) -> ... h d', d=module.head_dim)
                q, k = module.rotary(q, k, seqlen_offset=0, max_seqlen=seq_len)

            self.captured[layer_idx] = {"q": q.detach().cpu(), "k": k.detach().cpu()}
        return hook_fn

    def compute_last_token_attention(self) -> dict[int, torch.Tensor]:
        results = {}
        for layer_idx, qk in self.captured.items():
            q = qk["q"].float()   # (B, L, num_heads, head_dim)
            k = qk["k"].float()   # (B, L, num_kv_heads, head_dim)

            num_heads = q.shape[2]
            num_kv_heads = k.shape[2]
            num_groups = num_heads // num_kv_heads

            if num_groups > 1:
                k = k.unsqueeze(3).expand(-1, -1, -1, num_groups, -1)
                k = k.reshape(k.shape[0], k.shape[1], num_heads, -1)

            head_dim = q.shape[-1]
            q_last = q[:, -1:, :, :]
            scores = torch.einsum('bqhd,bkhd->bhqk', q_last, k) / (head_dim ** 0.5)

            attn_weights = F.softmax(scores, dim=-1)
            results[layer_idx] = attn_weights.squeeze(2).squeeze(0)

        return results

    def clear(self):
        self.captured.clear()

    def remove_hooks(self):
        for h in self.hooks:
            h.remove()
        self.hooks.clear()


# ── Data loading ────────────────────────────────────────────────────────────

def load_lambada():
    from datasets import load_dataset
    ds = load_dataset("EleutherAI/lambada_openai", "default", split="test")
    return ds


def load_sample_labels() -> pd.DataFrame:
    return pd.read_csv(SAMPLE_DATA_PATH)


# ── Extraction loop ────────────────────────────────────────────────────────

def extract_attention_patterns(arch: str, device: str, output_dir: Path,
                                max_samples: int | None = None):
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Loading {arch} model...")
    model, tokenizer = load_model_and_tokenizer(arch, device)
    extractor = AttentionWeightExtractor(model, ATTN_LAYER_INDICES)

    print("Loading LAMBADA dataset...")
    dataset = load_lambada()
    n_samples = min(len(dataset), max_samples) if max_samples else len(dataset)

    all_patterns = []
    attn_entropies = []

    for doc_id in tqdm(range(n_samples), desc=f"Extracting {arch}"):
        text = dataset[doc_id]["text"]
        inputs = tokenizer(text, return_tensors="pt").to(device)
        seq_len = inputs["input_ids"].shape[1]

        with torch.no_grad():
            model(**inputs)

        last_token_attn = extractor.compute_last_token_attention()

        sample_record = {"doc_id": doc_id, "seq_len": seq_len}
        for layer_idx, attn in last_token_attn.items():
            sample_record[f"layer_{layer_idx}_attn"] = attn.half()

            entropy = -(attn * torch.log(attn + 1e-10)).sum(dim=-1)
            for h_idx in range(entropy.shape[0]):
                attn_entropies.append({
                    "doc_id": doc_id,
                    "layer_idx": layer_idx,
                    "head_idx": h_idx,
                    "entropy": entropy[h_idx].item(),
                    "max_attn_pos": attn[h_idx].argmax().item(),
                    "max_attn_val": attn[h_idx].max().item(),
                    "last_5_mass": attn[h_idx, -5:].sum().item() if seq_len >= 5 else float("nan"),
                    "first_5_mass": attn[h_idx, :5].sum().item() if seq_len >= 5 else float("nan"),
                })

        all_patterns.append(sample_record)
        extractor.clear()

    extractor.remove_hooks()

    save_path = output_dir / f"{arch}_attention_patterns.pt"
    torch.save(all_patterns, save_path)
    print(f"Saved raw patterns: {save_path} ({len(all_patterns)} samples)")

    entropy_df = pd.DataFrame(attn_entropies)
    entropy_path = output_dir / f"{arch}_attention_entropy.csv"
    entropy_df.to_csv(entropy_path, index=False)
    print(f"Saved entropy data: {entropy_path}")

    del model
    torch.cuda.empty_cache()
    return entropy_df


# ── Analysis ────────────────────────────────────────────────────────────────

def analyze_helped_vs_hurt(output_dir: Path):
    labels = load_sample_labels()
    results = {}

    for arch in ["gdn", "retnet", "hgrn2"]:
        entropy_path = output_dir / f"{arch}_attention_entropy.csv"
        if not entropy_path.exists():
            print(f"Skipping {arch}: no entropy data found")
            continue

        df = pd.read_csv(entropy_path)
        arch_label = ARCH_TO_LABEL[arch]

        helped_ids = set(labels[labels[f"{arch_label}_helped"] == 1]["doc_id"])
        hurt_ids = set(labels[labels[f"{arch_label}_hurt"] == 1]["doc_id"])

        df["group"] = df["doc_id"].apply(
            lambda x: "helped" if x in helped_ids else ("hurt" if x in hurt_ids else "neutral")
        )

        layer_comparison = []
        for layer_idx in ATTN_LAYER_INDICES:
            layer_data = df[df["layer_idx"] == layer_idx]
            for group in ["helped", "hurt", "neutral"]:
                g = layer_data[layer_data["group"] == group]
                if len(g) == 0:
                    continue
                layer_comparison.append({
                    "arch": arch,
                    "layer_idx": layer_idx,
                    "group": group,
                    "mean_entropy": g["entropy"].mean(),
                    "std_entropy": g["entropy"].std(),
                    "mean_max_attn_val": g["max_attn_val"].mean(),
                    "mean_last_5_mass": g["last_5_mass"].mean(),
                    "mean_first_5_mass": g["first_5_mass"].mean(),
                    "n_samples": g["doc_id"].nunique(),
                })

        results[arch] = pd.DataFrame(layer_comparison)

    if results:
        combined = pd.concat(results.values(), ignore_index=True)
        combined.to_csv(output_dir / "helped_vs_hurt_entropy.csv", index=False)
        print(f"Saved helped-vs-hurt analysis: {output_dir / 'helped_vs_hurt_entropy.csv'}")

        summary = {}
        for arch in combined["arch"].unique():
            arch_data = combined[combined["arch"] == arch]
            helped = arch_data[arch_data["group"] == "helped"]
            hurt = arch_data[arch_data["group"] == "hurt"]
            if not helped.empty and not hurt.empty:
                summary[arch] = {
                    "helped_mean_entropy": helped["mean_entropy"].mean(),
                    "hurt_mean_entropy": hurt["mean_entropy"].mean(),
                    "entropy_diff": helped["mean_entropy"].mean() - hurt["mean_entropy"].mean(),
                    "helped_mean_last5_mass": helped["mean_last_5_mass"].mean(),
                    "hurt_mean_last5_mass": hurt["mean_last_5_mass"].mean(),
                }
        with open(output_dir / "attention_analysis_summary.json", "w") as f:
            json.dump(summary, f, indent=2)
        print(f"Saved summary: {output_dir / 'attention_analysis_summary.json'}")

        return combined
    return None


def analyze_cross_arch_similarity(output_dir: Path, n_compare: int = 200):
    patterns = {}
    for arch in ["gdn", "retnet", "hgrn2"]:
        pt_path = output_dir / f"{arch}_attention_patterns.pt"
        if not pt_path.exists():
            print(f"Skipping {arch}: no pattern data found")
            continue
        patterns[arch] = torch.load(pt_path, weights_only=False)

    if len(patterns) < 2:
        print("Need at least 2 architectures for cross-arch comparison")
        return None

    arch_list = sorted(patterns.keys())
    similarities = []

    for i in range(len(arch_list)):
        for j in range(i + 1, len(arch_list)):
            a1, a2 = arch_list[i], arch_list[j]
            n = min(n_compare, len(patterns[a1]), len(patterns[a2]))

            for layer_idx in ATTN_LAYER_INDICES:
                layer_key = f"layer_{layer_idx}_attn"
                cos_sims = []
                for s in range(n):
                    p1 = patterns[a1][s].get(layer_key)
                    p2 = patterns[a2][s].get(layer_key)
                    if p1 is None or p2 is None:
                        continue
                    v1 = p1.float().mean(dim=0)
                    v2 = p2.float().mean(dim=0)
                    min_len = min(v1.shape[0], v2.shape[0])
                    v1, v2 = v1[:min_len], v2[:min_len]
                    sim = F.cosine_similarity(v1.unsqueeze(0), v2.unsqueeze(0)).item()
                    cos_sims.append(sim)

                if cos_sims:
                    similarities.append({
                        "arch_pair": f"{a1}_vs_{a2}",
                        "layer_idx": layer_idx,
                        "mean_cosine_sim": np.mean(cos_sims),
                        "std_cosine_sim": np.std(cos_sims),
                        "n_pairs": len(cos_sims),
                    })

    if similarities:
        sim_df = pd.DataFrame(similarities)
        sim_df.to_csv(output_dir / "cross_arch_attention_similarity.csv", index=False)
        print(f"Saved cross-arch similarity: {output_dir / 'cross_arch_attention_similarity.csv'}")

        summary_path = output_dir / "attention_analysis_summary.json"
        summary = {}
        if summary_path.exists():
            with open(summary_path) as f:
                summary = json.load(f)
        summary["cross_arch_similarity"] = {
            row["arch_pair"]: {
                "layer_" + str(row["layer_idx"]): round(row["mean_cosine_sim"], 4)
                for _, row in sim_df[sim_df["arch_pair"] == row["arch_pair"]].iterrows()
            }
            for _, row in sim_df.drop_duplicates("arch_pair").iterrows()
        }
        with open(summary_path, "w") as f:
            json.dump(summary, f, indent=2)

        return sim_df
    return None


# ── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="exp-004: Attention weight extraction")
    parser.add_argument("--arch", choices=["gdn", "retnet", "hgrn2"],
                        help="Architecture to extract from")
    parser.add_argument("--device", default="cuda:0")
    parser.add_argument("--output_dir", type=str,
                        default="/root/entrainment_gated_ft/analysis/attention_weights")
    parser.add_argument("--max_samples", type=int, default=None,
                        help="Limit number of samples (for debugging)")
    parser.add_argument("--analyze", action="store_true",
                        help="Run analysis on pre-extracted data")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.analyze:
        print("=== Helped vs Hurt Analysis ===")
        analyze_helped_vs_hurt(output_dir)
        print("\n=== Cross-Architecture Similarity ===")
        analyze_cross_arch_similarity(output_dir)
    elif args.arch:
        extract_attention_patterns(args.arch, args.device, output_dir, args.max_samples)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
