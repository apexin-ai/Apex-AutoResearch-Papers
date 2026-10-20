"""exp37: Length-matched benign analysis — verify model doesn't use turn count as shortcut.

Three parts:
  Part 1: WildChat length-stratified FPR (Short 3-10, Medium 11-15, Long 16+)
  Part 2: Benign truncation test (K=3,5,8,10 user turns)
  Part 3: Jailbreak padding test (pad to 15+ user turns with benign content)
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/hf_cache"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
import json
import random
import numpy as np
import torch
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.gru_classifier import GRUClassifier
from src.models.deberta_multitask import DeBERTaMultiTask
from transformers import AutoTokenizer

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
ARCHIVE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive")
MODEL_NAME = "microsoft/deberta-v3-base"
MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
SEEDS = [42, 123, 456]

DAPT_CHECKPOINTS = {
    42: ARCHIVE / "plan_002",
    123: ARCHIVE / "plan_002_seed123",
    456: ARCHIVE / "plan_002_seed456",
}

WILDCHAT_PATH = PROJ / "data" / "wildchat_benign_226.jsonl"
TEST_PATH = PROJ / "data" / "plan_002_splits" / "test.jsonl"
DD_PATH = PROJ / "data" / "generated" / "deceptive_delight_all.jsonl"
AA_PATH = PROJ / "data" / "generated" / "actorattack_all.jsonl"

RESULTS_DIR = PROJ / "results"
HIST_DIR = RESULTS_DIR / "exp37_histograms"


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def count_user_turns(conv):
    return len([t for t in conv["turns"] if t["role"] == "user"])


def load_encoder(seed, device):
    ckpt_dir = DAPT_CHECKPOINTS[seed] / "deberta_multitask" / "best"
    model = DeBERTaMultiTask(model_name=MODEL_NAME)
    state_dict = torch.load(ckpt_dir / "model.pt", map_location="cpu", weights_only=False)
    model.load_state_dict(state_dict)
    encoder = model.deberta
    encoder.eval()
    for p in encoder.parameters():
        p.requires_grad = False
    return encoder.float().to(device)


def load_gru(seed, device):
    gru_path = DAPT_CHECKPOINTS[seed] / "gru" / "treatment" / "best.pt"
    gru = GRUClassifier(
        input_dim=768, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS,
        dropout=GRU_DROPOUT,
    )
    gru.load_state_dict(torch.load(gru_path, map_location="cpu", weights_only=True))
    return gru.float().to(device)


def embed_turns(encoder, tokenizer, turns, device):
    if not turns:
        turns = [""]
    enc = tokenizer(
        turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt",
    ).to(device)
    with torch.no_grad():
        out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        return out.last_hidden_state[:, 0, :]


def predict_conversations(encoder, gru, tokenizer, convs, device, turn_extractor=None):
    """Returns list of predictions (0=benign, 1=jailbreak) and probabilities."""
    if turn_extractor is None:
        turn_extractor = extract_user_turns
    gru.eval()
    preds = []
    probs = []
    for c in convs:
        turns = turn_extractor(c)
        embs = embed_turns(encoder, tokenizer, turns, device)
        embs_padded = embs.unsqueeze(0)
        lengths = torch.tensor([embs.size(0)], dtype=torch.long).to(device)
        with torch.no_grad():
            logits = gru(embs_padded, lengths)
            prob = torch.softmax(logits, dim=1)[0, 1].item()
            pred = logits.argmax(dim=1).item()
        preds.append(pred)
        probs.append(prob)
    return preds, probs


# ============================================================
# Part 1: WildChat length-stratified FPR
# ============================================================
def part1_wildchat_fpr(device, tokenizer):
    print("\n" + "=" * 60)
    print("PART 1: WildChat Length-Stratified FPR")
    print("=" * 60)

    convs = load_jsonl(WILDCHAT_PATH)
    turn_counts = [count_user_turns(c) for c in convs]
    print(f"Loaded {len(convs)} WildChat benign conversations")
    print(f"User turn range: {min(turn_counts)}-{max(turn_counts)}, mean={np.mean(turn_counts):.1f}")

    bins = {"Short (3-10)": (3, 10), "Medium (11-15)": (11, 15), "Long (16+)": (16, 999)}
    bucketed = {}
    for bname, (lo, hi) in bins.items():
        idxs = [i for i, tc in enumerate(turn_counts) if lo <= tc <= hi]
        bucketed[bname] = idxs
        print(f"  {bname}: {len(idxs)} samples")

    results = {}
    for seed in SEEDS:
        print(f"\n--- Seed {seed} ---")
        encoder = load_encoder(seed, device)
        gru = load_gru(seed, device)
        preds, _ = predict_conversations(encoder, gru, tokenizer, convs, device)

        for bname, idxs in bucketed.items():
            if not idxs:
                continue
            bucket_preds = [preds[i] for i in idxs]
            n_fp = sum(bucket_preds)
            fpr = n_fp / len(bucket_preds)
            key = f"seed{seed}_{bname}"
            results[key] = {"fpr": fpr, "n_fp": n_fp, "n_total": len(bucket_preds)}
            print(f"  {bname}: FPR={fpr:.3f} ({n_fp}/{len(bucket_preds)})")

        del encoder, gru
        torch.cuda.empty_cache()

    summary = {}
    for bname in bins:
        fprs = [results[f"seed{s}_{bname}"]["fpr"] for s in SEEDS if f"seed{s}_{bname}" in results]
        if fprs:
            bucket_tc = [turn_counts[i] for i in bucketed[bname]]
            summary[bname] = {
                "fpr_mean": float(np.mean(fprs)),
                "fpr_std": float(np.std(fprs)),
                "n_samples": len(bucketed[bname]),
                "turn_count_mean": float(np.mean(bucket_tc)),
                "turn_count_min": int(min(bucket_tc)),
                "turn_count_max": int(max(bucket_tc)),
                "per_seed": {f"seed{s}": results[f"seed{s}_{bname}"]["fpr"]
                             for s in SEEDS if f"seed{s}_{bname}" in results},
            }

    print("\n--- Part 1 Summary ---")
    for bname, s in summary.items():
        print(f"  {bname}: FPR={s['fpr_mean']:.3f}±{s['fpr_std']:.3f} (n={s['n_samples']})")

    return summary, turn_counts


# ============================================================
# Part 2: Benign truncation test
# ============================================================
def part2_benign_truncation(device, tokenizer):
    print("\n" + "=" * 60)
    print("PART 2: Benign Truncation Test")
    print("=" * 60)

    all_convs = load_jsonl(TEST_PATH)
    benign_convs = [c for c in all_convs if c["label"] == "benign"]
    benign_tc = [count_user_turns(c) for c in benign_convs]
    print(f"Loaded {len(benign_convs)} benign test conversations")
    print(f"User turn range: {min(benign_tc)}-{max(benign_tc)}, mean={np.mean(benign_tc):.1f}")

    truncation_ks = [3, 5, 8, 10]

    def make_truncated(convs, k):
        truncated = []
        for c in convs:
            user_turns = [t for t in c["turns"] if t["role"] == "user"]
            if len(user_turns) <= k:
                truncated.append(c)
            else:
                kept_turns = user_turns[:k]
                new_conv = dict(c)
                new_conv["turns"] = [{"role": "user", "content": t["content"]} for t in kept_turns]
                truncated.append(new_conv)
        return truncated

    results = {}

    for seed in SEEDS:
        print(f"\n--- Seed {seed} ---")
        encoder = load_encoder(seed, device)
        gru = load_gru(seed, device)

        orig_preds, _ = predict_conversations(encoder, gru, tokenizer, benign_convs, device)
        orig_fpr = sum(orig_preds) / len(orig_preds)
        results[f"seed{seed}_original"] = {"fpr": orig_fpr, "n_fp": sum(orig_preds), "n": len(orig_preds)}
        print(f"  Original: FPR={orig_fpr:.3f} ({sum(orig_preds)}/{len(orig_preds)})")

        for k in truncation_ks:
            truncated = make_truncated(benign_convs, k)
            actual_lengths = [count_user_turns(c) for c in truncated]
            preds, _ = predict_conversations(encoder, gru, tokenizer, truncated, device)
            fpr = sum(preds) / len(preds)
            n_actually_truncated = sum(1 for bl, al in zip(benign_tc, actual_lengths) if al < bl)
            results[f"seed{seed}_K{k}"] = {
                "fpr": fpr, "n_fp": sum(preds), "n": len(preds),
                "n_truncated": n_actually_truncated,
                "mean_turns_after": float(np.mean(actual_lengths)),
            }
            print(f"  K={k}: FPR={fpr:.3f} ({sum(preds)}/{len(preds)}) "
                  f"[{n_actually_truncated}/{len(benign_convs)} actually truncated]")

        del encoder, gru
        torch.cuda.empty_cache()

    summary = {"original": {}, "truncated": {}}
    orig_fprs = [results[f"seed{s}_original"]["fpr"] for s in SEEDS]
    summary["original"] = {
        "fpr_mean": float(np.mean(orig_fprs)),
        "fpr_std": float(np.std(orig_fprs)),
        "n_samples": len(benign_convs),
        "per_seed": {f"seed{s}": results[f"seed{s}_original"]["fpr"] for s in SEEDS},
    }

    for k in truncation_ks:
        fprs = [results[f"seed{s}_K{k}"]["fpr"] for s in SEEDS]
        summary["truncated"][f"K={k}"] = {
            "fpr_mean": float(np.mean(fprs)),
            "fpr_std": float(np.std(fprs)),
            "delta_vs_original": float(np.mean(fprs) - np.mean(orig_fprs)),
            "n_actually_truncated": results[f"seed{SEEDS[0]}_K{k}"]["n_truncated"],
            "mean_turns_after": results[f"seed{SEEDS[0]}_K{k}"]["mean_turns_after"],
            "per_seed": {f"seed{s}": results[f"seed{s}_K{k}"]["fpr"] for s in SEEDS},
        }

    print("\n--- Part 2 Summary ---")
    print(f"  Original: FPR={summary['original']['fpr_mean']:.3f}±{summary['original']['fpr_std']:.3f}")
    for k in truncation_ks:
        s = summary["truncated"][f"K={k}"]
        print(f"  K={k}: FPR={s['fpr_mean']:.3f}±{s['fpr_std']:.3f} "
              f"(delta={s['delta_vs_original']:+.3f})")

    return summary, benign_tc


# ============================================================
# Part 3: Jailbreak padding test
# ============================================================
def part3_jailbreak_padding(device, tokenizer):
    print("\n" + "=" * 60)
    print("PART 3: Jailbreak Padding Test")
    print("=" * 60)

    dd_convs = load_jsonl(DD_PATH)
    aa_convs = load_jsonl(AA_PATH)
    test_convs = load_jsonl(TEST_PATH)
    benign_convs = [c for c in test_convs if c["label"] == "benign"]

    benign_user_turns = []
    for c in benign_convs:
        for t in c["turns"]:
            if t["role"] == "user":
                benign_user_turns.append(t["content"])

    print(f"DD jailbreak: {len(dd_convs)} conversations")
    print(f"AA jailbreak: {len(aa_convs)} conversations")
    print(f"Benign user turns pool: {len(benign_user_turns)} turns for padding")

    TARGET_TURNS = 15

    def pad_conversation(conv, rng):
        user_turns = [t for t in conv["turns"] if t["role"] == "user"]
        n_existing = len(user_turns)
        if n_existing >= TARGET_TURNS:
            return conv
        n_pad = TARGET_TURNS - n_existing
        pad_turns = [rng.choice(benign_user_turns) for _ in range(n_pad)]
        new_turns = list(conv["turns"])
        for pt in pad_turns:
            new_turns.append({"role": "user", "content": pt})
            new_turns.append({"role": "assistant", "content": "Sure, I can help with that."})
        new_conv = dict(conv)
        new_conv["turns"] = new_turns
        return new_conv

    results = {}

    for seed in SEEDS:
        print(f"\n--- Seed {seed} ---")
        encoder = load_encoder(seed, device)
        gru = load_gru(seed, device)
        rng = random.Random(seed)

        for name, convs in [("DD", dd_convs), ("AA", aa_convs)]:
            orig_preds, _ = predict_conversations(encoder, gru, tokenizer, convs, device)
            orig_det_rate = sum(orig_preds) / len(orig_preds)

            padded_convs = [pad_conversation(c, rng) for c in convs]
            padded_tc = [count_user_turns(c) for c in padded_convs]
            padded_preds, _ = predict_conversations(encoder, gru, tokenizer, padded_convs, device)
            padded_det_rate = sum(padded_preds) / len(padded_preds)

            results[f"seed{seed}_{name}_original"] = {
                "detection_rate": orig_det_rate,
                "n_detected": sum(orig_preds),
                "n_total": len(orig_preds),
            }
            results[f"seed{seed}_{name}_padded"] = {
                "detection_rate": padded_det_rate,
                "n_detected": sum(padded_preds),
                "n_total": len(padded_preds),
                "mean_turns_after": float(np.mean(padded_tc)),
            }
            print(f"  {name} Original: det_rate={orig_det_rate:.3f} ({sum(orig_preds)}/{len(orig_preds)})")
            print(f"  {name} Padded:   det_rate={padded_det_rate:.3f} ({sum(padded_preds)}/{len(padded_preds)}) "
                  f"[mean {np.mean(padded_tc):.1f} user turns]")

        del encoder, gru
        torch.cuda.empty_cache()

    summary = {}
    for name in ["DD", "AA"]:
        orig_rates = [results[f"seed{s}_{name}_original"]["detection_rate"] for s in SEEDS]
        pad_rates = [results[f"seed{s}_{name}_padded"]["detection_rate"] for s in SEEDS]
        summary[name] = {
            "original": {
                "mean": float(np.mean(orig_rates)),
                "std": float(np.std(orig_rates)),
                "per_seed": {f"seed{s}": results[f"seed{s}_{name}_original"]["detection_rate"] for s in SEEDS},
            },
            "padded": {
                "mean": float(np.mean(pad_rates)),
                "std": float(np.std(pad_rates)),
                "target_turns": TARGET_TURNS,
                "mean_turns_after": results[f"seed{SEEDS[0]}_{name}_padded"]["mean_turns_after"],
                "per_seed": {f"seed{s}": results[f"seed{s}_{name}_padded"]["detection_rate"] for s in SEEDS},
            },
            "delta": float(np.mean(pad_rates) - np.mean(orig_rates)),
        }

    print("\n--- Part 3 Summary ---")
    for name, s in summary.items():
        print(f"  {name} Original: det_rate={s['original']['mean']:.3f}±{s['original']['std']:.3f}")
        print(f"  {name} Padded:   det_rate={s['padded']['mean']:.3f}±{s['padded']['std']:.3f} "
              f"(delta={s['delta']:+.3f})")

    return summary


# ============================================================
# Histograms
# ============================================================
def plot_histograms(wc_turn_counts, benign_tc):
    HIST_DIR.mkdir(parents=True, exist_ok=True)

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))

    axes[0].hist(wc_turn_counts, bins=range(1, max(wc_turn_counts) + 2),
                 color="steelblue", edgecolor="white", alpha=0.8)
    axes[0].set_xlabel("User turns")
    axes[0].set_ylabel("Count")
    axes[0].set_title("WildChat Benign (n=226)")
    axes[0].axvline(x=10.5, color="red", linestyle="--", alpha=0.6, label="Short/Med boundary")
    axes[0].axvline(x=15.5, color="orange", linestyle="--", alpha=0.6, label="Med/Long boundary")
    axes[0].legend(fontsize=8)

    axes[1].hist(benign_tc, bins=range(min(benign_tc), max(benign_tc) + 2),
                 color="forestgreen", edgecolor="white", alpha=0.8)
    axes[1].set_xlabel("User turns")
    axes[1].set_ylabel("Count")
    axes[1].set_title("Test Benign (n=38)")

    dd = load_jsonl(DD_PATH)
    aa = load_jsonl(AA_PATH)
    dd_tc = [count_user_turns(c) for c in dd]
    aa_tc = [count_user_turns(c) for c in aa]
    axes[2].hist(dd_tc, bins=range(min(dd_tc + aa_tc), max(dd_tc + aa_tc) + 2),
                 color="crimson", edgecolor="white", alpha=0.6, label="DD OOD")
    axes[2].hist(aa_tc, bins=range(min(dd_tc + aa_tc), max(dd_tc + aa_tc) + 2),
                 color="darkorange", edgecolor="white", alpha=0.6, label="AA OOD")
    axes[2].set_xlabel("User turns")
    axes[2].set_ylabel("Count")
    axes[2].set_title("Jailbreak OOD")
    axes[2].legend(fontsize=8)

    plt.tight_layout()
    fig.savefig(HIST_DIR / "turn_count_distributions.pdf", bbox_inches="tight")
    fig.savefig(HIST_DIR / "turn_count_distributions.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"\nHistograms saved to {HIST_DIR}/")


# ============================================================
# Main
# ============================================================
def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    p1_summary, wc_tc = part1_wildchat_fpr(device, tokenizer)
    p2_summary, benign_tc = part2_benign_truncation(device, tokenizer)
    p3_summary = part3_jailbreak_padding(device, tokenizer)

    plot_histograms(wc_tc, benign_tc)

    output = {
        "experiment": "exp37_length_matched_benign",
        "description": "Length confound analysis: WildChat stratified FPR, benign truncation, jailbreak padding",
        "model": "plan_002 9-class DeBERTa+BiGRU",
        "seeds": SEEDS,
        "part1_wildchat_fpr": p1_summary,
        "part2_benign_truncation": p2_summary,
        "part3_jailbreak_padding": p3_summary,
    }

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "exp37_length_matched_benign.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {out_path}")

    print("\n" + "=" * 60)
    print("FINAL SUMMARY")
    print("=" * 60)
    print("\nPart 1 - WildChat FPR by length:")
    for bname, s in p1_summary.items():
        print(f"  {bname}: FPR={s['fpr_mean']:.3f}±{s['fpr_std']:.3f} (n={s['n_samples']})")
    print("\nPart 2 - Benign truncation FPR:")
    print(f"  Original: FPR={p2_summary['original']['fpr_mean']:.3f}±{p2_summary['original']['fpr_std']:.3f}")
    for k, s in p2_summary["truncated"].items():
        print(f"  {k}: FPR={s['fpr_mean']:.3f}±{s['fpr_std']:.3f} (delta={s['delta_vs_original']:+.3f})")
    print("\nPart 3 - Jailbreak padding detection rate:")
    for name, s in p3_summary.items():
        print(f"  {name}: orig={s['original']['mean']:.3f}±{s['original']['std']:.3f} → "
              f"padded={s['padded']['mean']:.3f}±{s['padded']['std']:.3f} (delta={s['delta']:+.3f})")


if __name__ == "__main__":
    main()
