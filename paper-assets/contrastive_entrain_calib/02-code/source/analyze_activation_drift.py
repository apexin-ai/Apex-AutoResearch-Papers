#!/usr/bin/env python3
"""Compare ckpt-4500 vs ckpt-5000 activation projections onto d_syc direction.

Extracts layer-19 hidden states at user_last_token and asst_first_token positions,
projects onto d_syc[19], and compares valid_correction vs invalid_pressure distributions.
"""

import json
import os
import sys
from pathlib import Path

import numpy as np
import torch
from peft import PeftModel
from sklearn.metrics import roc_auc_score
from transformers import AutoModelForCausalLM, AutoTokenizer

os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

BASE_MODEL = "/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B"
CKPT_4500 = "/root/autodl-tmp/checkpoints/exp003/checkpoint-4500/"
CKPT_5000 = "/root/autodl-tmp/checkpoints/exp003/checkpoint-5000/"
DIRECTIONS = "/root/contrastive_entrain_calib/results/exp001/directions.pt"
DATA_PATH = "/root/mvp_v2_1_expanded/data/calibration_v2_1_expanded.jsonl"
OUT_DIR = Path("/root/contrastive_entrain_calib/results/mechanistic_analysis/activation_drift")
LAYER = 19
DEVICE = torch.device("cuda:0")


def load_data(path):
    samples = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                samples.append(json.loads(line))
    return samples


def apply_template(tokenizer, messages, **kwargs):
    try:
        return tokenizer.apply_chat_template(
            messages, enable_thinking=False, tokenize=True, return_dict=False, **kwargs
        )
    except TypeError:
        return tokenizer.apply_chat_template(
            messages, tokenize=True, return_dict=False, **kwargs
        )


def find_positions(tokenizer, turns):
    """Find user_last_token and asst_first_token positions.

    turns = [user, assistant, user_correction] (3 turns, no assistant response).
    We add a generation prompt to get the assistant start position.
    """
    msgs_all = [{"role": t["role"], "content": t["content"]} for t in turns]
    msgs_through_last_user = msgs_all  # all 3 turns

    # ids_A: through last user turn (no gen prompt)
    ids_no_gen = apply_template(tokenizer, msgs_through_last_user, add_generation_prompt=False)
    # ids_B: with generation prompt appended
    ids_with_gen = apply_template(tokenizer, msgs_through_last_user, add_generation_prompt=True)

    # user_last_pos: last content token before <|im_end|> at end of user turn
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    user_last_pos = None
    if im_end_id is not None:
        for pos in range(len(ids_no_gen) - 1, -1, -1):
            if ids_no_gen[pos] == im_end_id:
                user_last_pos = pos - 1
                break
    if user_last_pos is None or user_last_pos < 0:
        user_last_pos = len(ids_no_gen) - 1

    # asst_first_pos: first token after generation prompt = len(ids_with_gen) - 1
    # (this is the last token of the gen prompt; its hidden state encodes what comes next)
    asst_first_pos = len(ids_with_gen) - 1

    return user_last_pos, asst_first_pos, ids_with_gen


def extract_projections(model, tokenizer, samples, d_syc_layer):
    """Extract layer-19 hidden states and project onto d_syc for all samples."""
    d_user = d_syc_layer[0].to(DEVICE)  # (hidden_dim,)
    d_asst = d_syc_layer[1].to(DEVICE)  # (hidden_dim,)

    results = []
    for i, sample in enumerate(samples):
        user_pos, asst_pos, input_ids = find_positions(tokenizer, sample["turns"])

        input_tensor = torch.tensor([input_ids], dtype=torch.long, device=DEVICE)
        with torch.no_grad():
            outputs = model(
                input_ids=input_tensor,
                output_hidden_states=True,
            )

        # hidden_states[0] = embedding, [1..36] = layer outputs
        h = outputs.hidden_states[LAYER + 1]  # layer 19 output, shape (1, seq_len, hidden_dim)
        h_user = h[0, user_pos, :].float()
        h_asst = h[0, asst_pos, :].float()

        proj_user = torch.dot(h_user, d_user).item()
        proj_asst = torch.dot(h_asst, d_asst).item()

        cos_user = torch.nn.functional.cosine_similarity(
            h_user.unsqueeze(0), d_user.unsqueeze(0)
        ).item()
        cos_asst = torch.nn.functional.cosine_similarity(
            h_asst.unsqueeze(0), d_asst.unsqueeze(0)
        ).item()

        results.append({
            "pair_id": sample["pair_id"],
            "condition": sample["condition"],
            "domain": sample.get("domain", "unknown"),
            "proj_user": proj_user,
            "proj_asst": proj_asst,
            "cos_user": cos_user,
            "cos_asst": cos_asst,
        })

        if (i + 1) % 50 == 0:
            print(f"  Processed {i+1}/{len(samples)} samples")

    return results


def compute_stats(projections, label):
    """Compute summary statistics for a checkpoint's projections."""
    valid = [p for p in projections if p["condition"] == "valid_correction"]
    invalid = [p for p in projections if p["condition"] == "invalid_pressure"]

    def _stats(arr):
        a = np.array(arr)
        return {"mean": float(np.mean(a)), "std": float(np.std(a)),
                "median": float(np.median(a)), "min": float(np.min(a)), "max": float(np.max(a))}

    stats = {"checkpoint": label, "n_valid": len(valid), "n_invalid": len(invalid)}

    for pos_name in ["proj_user", "proj_asst", "cos_user", "cos_asst"]:
        v_vals = [p[pos_name] for p in valid]
        i_vals = [p[pos_name] for p in invalid]
        stats[f"{pos_name}_valid"] = _stats(v_vals)
        stats[f"{pos_name}_invalid"] = _stats(i_vals)
        stats[f"{pos_name}_mean_diff"] = float(np.mean(v_vals) - np.mean(i_vals))

        # AUROC: can d_syc separate valid from invalid?
        all_vals = v_vals + i_vals
        labels = [1] * len(v_vals) + [0] * len(i_vals)
        try:
            stats[f"{pos_name}_auroc"] = float(roc_auc_score(labels, all_vals))
        except ValueError:
            stats[f"{pos_name}_auroc"] = None

    return stats


def make_histogram(proj_4500, proj_5000, out_path):
    """Create comparison histograms."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("d_syc Projection: ckpt-4500 vs ckpt-5000 (Layer 19)", fontsize=14)

    configs = [
        ("proj_user", "User Last Token — Dot Product"),
        ("proj_asst", "Asst First Token — Dot Product"),
        ("cos_user", "User Last Token — Cosine Similarity"),
        ("cos_asst", "Asst First Token — Cosine Similarity"),
    ]

    for ax, (key, title) in zip(axes.flat, configs):
        for ckpt_name, projs, ls in [("ckpt-4500", proj_4500, "-"), ("ckpt-5000", proj_5000, "--")]:
            valid_vals = [p[key] for p in projs if p["condition"] == "valid_correction"]
            invalid_vals = [p[key] for p in projs if p["condition"] == "invalid_pressure"]

            bins = np.linspace(
                min(min(valid_vals), min(invalid_vals)),
                max(max(valid_vals), max(invalid_vals)),
                40
            )
            ax.hist(valid_vals, bins=bins, alpha=0.4, label=f"{ckpt_name} valid",
                    color="blue" if ls == "-" else "cyan",
                    edgecolor="none")
            ax.hist(invalid_vals, bins=bins, alpha=0.4, label=f"{ckpt_name} invalid",
                    color="red" if ls == "-" else "orange",
                    edgecolor="none")

        ax.set_title(title)
        ax.legend(fontsize=8)
        ax.set_xlabel("Projection value")
        ax.set_ylabel("Count")

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved histogram to {out_path}")


def make_paired_scatter(proj_4500, proj_5000, out_path):
    """Scatter plot of per-sample projection shift between checkpoints."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    # Match by pair_id + condition
    key_fn = lambda p: (p["pair_id"], p["condition"])
    map_4500 = {key_fn(p): p for p in proj_4500}
    map_5000 = {key_fn(p): p for p in proj_5000}
    common_keys = sorted(set(map_4500) & set(map_5000))

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    fig.suptitle("Per-sample projection shift: ckpt-4500 → ckpt-5000", fontsize=13)

    for ax, pos_key in zip(axes, ["proj_user", "proj_asst"]):
        for cond, color, marker in [("valid_correction", "blue", "o"), ("invalid_pressure", "red", "x")]:
            xs, ys = [], []
            for k in common_keys:
                if k[1] == cond:
                    xs.append(map_4500[k][pos_key])
                    ys.append(map_5000[k][pos_key])
            ax.scatter(xs, ys, c=color, marker=marker, alpha=0.5, s=15, label=cond)

        lims = ax.get_xlim()
        ax.plot(lims, lims, "k--", alpha=0.3, lw=1)
        ax.set_xlabel("ckpt-4500")
        ax.set_ylabel("ckpt-5000")
        ax.set_title(pos_key)
        ax.legend(fontsize=8)

    plt.tight_layout()
    plt.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"Saved scatter to {out_path}")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Loading directions...")
    directions = torch.load(DIRECTIONS, map_location="cpu", weights_only=False)
    d_syc = directions["d_syc"]  # (36, 2, 4096)
    d_syc_19 = d_syc[LAYER].float()  # (2, 4096)
    print(f"  d_syc shape: {d_syc.shape}, using layer {LAYER}")

    print("Loading data...")
    samples = load_data(DATA_PATH)
    print(f"  {len(samples)} samples loaded")

    print("Loading tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    all_projections = {}

    for ckpt_name, ckpt_path in [("ckpt-4500", CKPT_4500), ("ckpt-5000", CKPT_5000)]:
        print(f"\n{'='*60}")
        print(f"Processing {ckpt_name}: {ckpt_path}")
        print(f"{'='*60}")

        print("  Loading base model...")
        model = AutoModelForCausalLM.from_pretrained(
            BASE_MODEL,
            torch_dtype=torch.bfloat16,
            device_map={"": DEVICE},
            trust_remote_code=True,
        )
        print("  Loading LoRA adapter...")
        model = PeftModel.from_pretrained(model, ckpt_path)
        model = model.merge_and_unload()
        model.eval()

        print("  Extracting projections...")
        projections = extract_projections(model, tokenizer, samples, d_syc_19)
        all_projections[ckpt_name] = projections

        stats = compute_stats(projections, ckpt_name)
        print(f"\n  --- {ckpt_name} Summary ---")
        print(f"  proj_user AUROC: {stats['proj_user_auroc']:.4f}")
        print(f"  proj_asst AUROC: {stats['proj_asst_auroc']:.4f}")
        print(f"  proj_user mean_diff (valid-invalid): {stats['proj_user_mean_diff']:.4f}")
        print(f"  proj_asst mean_diff (valid-invalid): {stats['proj_asst_mean_diff']:.4f}")

        # Free GPU memory
        del model
        torch.cuda.empty_cache()

    # Compute cross-checkpoint statistics
    print("\n" + "=" * 60)
    print("Cross-checkpoint analysis")
    print("=" * 60)

    stats_4500 = compute_stats(all_projections["ckpt-4500"], "ckpt-4500")
    stats_5000 = compute_stats(all_projections["ckpt-5000"], "ckpt-5000")

    # Mean activation cosine similarity between checkpoints
    def mean_vec(projs, key, condition=None):
        vals = [p[key] for p in projs if condition is None or p["condition"] == condition]
        return np.mean(vals)

    cross_stats = {
        "ckpt_4500": stats_4500,
        "ckpt_5000": stats_5000,
        "delta": {}
    }
    for key in ["proj_user", "proj_asst"]:
        for cond in ["valid", "invalid"]:
            m_4500 = stats_4500[f"{key}_{cond}"]["mean"]
            m_5000 = stats_5000[f"{key}_{cond}"]["mean"]
            delta_key = f"{key}_{cond}_mean_shift"
            cross_stats["delta"][delta_key] = m_5000 - m_4500
            print(f"  {delta_key}: {m_5000 - m_4500:+.4f}")

        auroc_4500 = stats_4500[f"{key}_auroc"]
        auroc_5000 = stats_5000[f"{key}_auroc"]
        cross_stats["delta"][f"{key}_auroc_shift"] = auroc_5000 - auroc_4500
        print(f"  {key}_auroc: {auroc_4500:.4f} → {auroc_5000:.4f} (Δ={auroc_5000-auroc_4500:+.4f})")

    # Save outputs
    print("\nSaving outputs...")
    with open(OUT_DIR / "projection_stats.json", "w") as f:
        json.dump(cross_stats, f, indent=2, ensure_ascii=False)
    print(f"  Saved projection_stats.json")

    raw = {"ckpt-4500": all_projections["ckpt-4500"], "ckpt-5000": all_projections["ckpt-5000"]}
    with open(OUT_DIR / "raw_projections.json", "w") as f:
        json.dump(raw, f, indent=2, ensure_ascii=False)
    print(f"  Saved raw_projections.json")

    make_histogram(all_projections["ckpt-4500"], all_projections["ckpt-5000"],
                   OUT_DIR / "projection_histogram.pdf")
    make_histogram(all_projections["ckpt-4500"], all_projections["ckpt-5000"],
                   OUT_DIR / "projection_histogram.png")
    make_paired_scatter(all_projections["ckpt-4500"], all_projections["ckpt-5000"],
                        OUT_DIR / "projection_scatter.png")

    print("\nDone!")


if __name__ == "__main__":
    main()
