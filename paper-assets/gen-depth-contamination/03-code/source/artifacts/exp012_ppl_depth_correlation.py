"""
exp012: Binary Detector Confidence vs. Generational Depth Correlation

Tests whether scalar binary-detector confidence scores can estimate generational
depth. Two detectors:
  1. DivEye log-PPL (Qwen2.5-1.5B-Instruct)
  2. Binoculars ratio (observer=Pythia-1.4b / performer=OLMo-1B, separate tokenizers)

Inputs:
  - depth_0.jsonl .. depth_5.jsonl from 4 model conditions
Outputs:
  - artifacts/exp012_results.json
  - artifacts/exp012_confidence_vs_depth.pdf
Dependencies: torch, transformers, scipy, matplotlib, numpy
"""

import argparse
import json
import os
import sys
from pathlib import Path

import numpy as np
import torch
from scipy.stats import spearmanr
from sklearn.metrics import roc_auc_score

PROJECT_ROOT = Path("/root/autodl-tmp/gen-depth-contamination")

MODEL_CONDITIONS = {
    "qwen-rewrite": PROJECT_ROOT / "data",
    "pythia-1.4b":  PROJECT_ROOT / "data_exp001_pythia",
    "olmo-1b":      PROJECT_ROOT / "data_exp002_olmo",
    "qwen-cont":    PROJECT_ROOT / "data_exp017_qwen_cont",
}

OBD_PAIRWISE_AUC = {
    "qwen-rewrite": {"0v1": 0.9956, "1v2": 0.6957, "2v3": 0.5893, "3v4": 0.5434, "4v5": 0.5343},
    "pythia-1.4b":  {"0v1": 0.9932, "1v2": 0.6539, "2v3": 0.5515, "3v4": 0.5153, "4v5": 0.5135},
    "olmo-1b":      {"0v1": 0.9970, "1v2": 0.6146, "2v3": 0.5497, "3v4": 0.5090, "4v5": 0.5044},
    "qwen-cont":    {"0v1": 0.9972, "1v2": 0.6114, "2v3": 0.5609, "3v4": 0.5408, "4v5": 0.5139},
}

DEPTH_PAIRS = ["0v1", "1v2", "2v3", "3v4", "4v5"]


def load_texts(data_dir: Path, max_samples: int) -> dict[int, list[str]]:
    texts = {}
    for d in range(6):
        fpath = data_dir / f"depth_{d}.jsonl"
        if not fpath.exists():
            print(f"  WARNING: {fpath} not found, skipping depth {d}")
            continue
        samples = []
        with open(fpath) as f:
            for i, line in enumerate(f):
                if i >= max_samples:
                    break
                samples.append(json.loads(line)["text"])
        texts[d] = samples
    return texts


def compute_log_perplexity_batch(
    model, tokenizer, texts: list[str], batch_size: int = 8, max_length: int = 512
) -> np.ndarray:
    device = next(model.parameters()).device
    all_ppl = []

    for start in range(0, len(texts), batch_size):
        batch_texts = texts[start : start + batch_size]
        encodings = tokenizer(
            batch_texts,
            return_tensors="pt",
            padding=True,
            truncation=True,
            max_length=max_length,
        ).to(device)

        with torch.no_grad():
            outputs = model(**encodings)
            logits = outputs.logits

        shift_logits = logits[:, :-1, :].contiguous()
        shift_labels = encodings["input_ids"][:, 1:].contiguous()
        attention_mask = encodings["attention_mask"][:, 1:].contiguous()

        loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
        token_losses = loss_fn(
            shift_logits.view(-1, shift_logits.size(-1)),
            shift_labels.view(-1),
        ).view(shift_labels.size())

        token_losses = token_losses * attention_mask
        mean_loss = token_losses.sum(dim=1) / attention_mask.sum(dim=1).clamp(min=1)
        all_ppl.extend(mean_loss.cpu().numpy().tolist())

    return np.array(all_ppl)


def pairwise_auc(scores: np.ndarray, labels: np.ndarray, d_low: int, d_high: int) -> float:
    mask = np.isin(labels, [d_low, d_high])
    s = scores[mask]
    y = (labels[mask] == d_high).astype(int)
    if len(np.unique(y)) < 2:
        return 0.5
    auc = roc_auc_score(y, s)
    return max(auc, 1 - auc)


def threshold_accuracy(scores: np.ndarray, labels: np.ndarray, n_classes: int = 6) -> float:
    thresholds = np.quantile(scores, np.linspace(0, 1, n_classes + 1)[1:-1])
    predicted = np.digitize(scores, thresholds)
    return float(np.mean(predicted == labels))


def analyze_condition(
    condition: str,
    ref_ppl: dict[int, np.ndarray],
    obs_ppl: dict[int, np.ndarray],
    perf_ppl: dict[int, np.ndarray],
) -> dict:
    depths_present = sorted(set(ref_ppl.keys()) & set(obs_ppl.keys()) & set(perf_ppl.keys()))

    all_ref = np.concatenate([ref_ppl[d] for d in depths_present])
    all_obs = np.concatenate([obs_ppl[d] for d in depths_present])
    all_perf = np.concatenate([perf_ppl[d] for d in depths_present])
    all_labels = np.concatenate([np.full(len(ref_ppl[d]), d) for d in depths_present])

    # Binoculars ratio = observer_ppl / performer_ppl
    ppl_ratio = all_obs / np.clip(all_perf, 1e-6, None)

    rho_ref, p_ref = spearmanr(all_ref, all_labels)
    rho_obs, p_obs = spearmanr(all_obs, all_labels)
    rho_ratio, p_ratio = spearmanr(ppl_ratio, all_labels)

    pair_auc_ref = {}
    pair_auc_obs = {}
    pair_auc_ratio = {}
    obd_baseline = OBD_PAIRWISE_AUC[condition]

    for pair_name in DEPTH_PAIRS:
        d_low, d_high = int(pair_name[0]), int(pair_name[2])
        if d_low in depths_present and d_high in depths_present:
            pair_auc_ref[pair_name] = round(pairwise_auc(all_ref, all_labels, d_low, d_high), 4)
            pair_auc_obs[pair_name] = round(pairwise_auc(all_obs, all_labels, d_low, d_high), 4)
            pair_auc_ratio[pair_name] = round(pairwise_auc(ppl_ratio, all_labels, d_low, d_high), 4)

    acc_ref = round(threshold_accuracy(all_ref, all_labels), 4)
    acc_obs = round(threshold_accuracy(all_obs, all_labels), 4)
    acc_ratio = round(threshold_accuracy(ppl_ratio, all_labels), 4)

    return {
        "spearman": {
            "log_ppl_ref": {"rho": round(rho_ref, 4), "p": round(p_ref, 6)},
            "log_ppl_obs": {"rho": round(rho_obs, 4), "p": round(p_obs, 6)},
            "ppl_ratio":   {"rho": round(rho_ratio, 4), "p": round(p_ratio, 6)},
        },
        "pairwise_auc": {
            "log_ppl_ref": pair_auc_ref,
            "log_ppl_obs": pair_auc_obs,
            "ppl_ratio":   pair_auc_ratio,
            "obd_15d":     {k: v for k, v in obd_baseline.items() if k in pair_auc_ref},
        },
        "threshold_accuracy_6class": {
            "log_ppl_ref": acc_ref,
            "log_ppl_obs": acc_obs,
            "ppl_ratio":   acc_ratio,
            "random_baseline": round(1/6, 4),
        },
    }


def print_summary(results: dict):
    print("\n" + "=" * 80)
    print("EXP-012: Perplexity vs. Depth Correlation — Summary")
    print("=" * 80)

    for cond, res in results.items():
        print(f"\n--- {cond} ---")

        sp = res["spearman"]
        print(f"  Spearman ρ:  ref={sp['log_ppl_ref']['rho']:.4f}  "
              f"obs={sp['log_ppl_obs']['rho']:.4f}  "
              f"ratio={sp['ppl_ratio']['rho']:.4f}")

        print(f"  6-class acc: ref={res['threshold_accuracy_6class']['log_ppl_ref']:.4f}  "
              f"obs={res['threshold_accuracy_6class']['log_ppl_obs']:.4f}  "
              f"ratio={res['threshold_accuracy_6class']['ppl_ratio']:.4f}  "
              f"(random={res['threshold_accuracy_6class']['random_baseline']:.4f})")

        pa = res["pairwise_auc"]
        print(f"  {'Pair':>5s}  {'PPL_ref':>8s}  {'PPL_obs':>8s}  {'Ratio':>8s}  {'OBD-15D':>8s}  {'Delta':>8s}")
        for pair in DEPTH_PAIRS:
            if pair in pa["log_ppl_ref"]:
                best_scalar = max(pa["log_ppl_ref"][pair], pa["log_ppl_obs"][pair], pa["ppl_ratio"][pair])
                obd = pa["obd_15d"][pair]
                delta = obd - best_scalar
                print(f"  {pair:>5s}  {pa['log_ppl_ref'][pair]:>8.4f}  "
                      f"{pa['log_ppl_obs'][pair]:>8.4f}  "
                      f"{pa['ppl_ratio'][pair]:>8.4f}  "
                      f"{obd:>8.4f}  {delta:>+8.4f}")

    print("\n" + "=" * 80)


def make_plots(
    ref_ppls: dict[str, dict[int, np.ndarray]],
    obs_ppls: dict[str, dict[int, np.ndarray]],
    perf_ppls: dict[str, dict[int, np.ndarray]],
    output_path: Path,
):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    conditions = list(MODEL_CONDITIONS.keys())
    methods = ["DivEye log-PPL", "Bino observer PPL", "Bino ratio"]
    fig, axes = plt.subplots(len(conditions), len(methods), figsize=(14, 12), sharey=False)

    for row, cond in enumerate(conditions):
        depths_present = sorted(ref_ppls[cond].keys())

        def get_depth_scores(score_dict):
            ds, ss = [], []
            for d in depths_present:
                arr = score_dict[d]
                ds.extend([d] * len(arr))
                ss.extend(arr.tolist())
            return np.array(ds), np.array(ss)

        # DivEye log-PPL
        d_arr, s_arr = get_depth_scores(ref_ppls[cond])
        ax = axes[row, 0]
        for d in depths_present:
            mask = d_arr == d
            ax.scatter(np.full(mask.sum(), d) + np.random.uniform(-0.15, 0.15, mask.sum()),
                       s_arr[mask], alpha=0.3, s=6)
        rho, p = spearmanr(d_arr, s_arr)
        ax.set_title(f"{cond}\nρ={rho:.3f}, p={p:.2e}" if row == 0 else f"ρ={rho:.3f}, p={p:.2e}", fontsize=9)
        if row == 0:
            ax.set_title(f"DivEye log-PPL\n{cond}: ρ={rho:.3f}", fontsize=9)
        ax.set_ylabel(cond, fontsize=9)
        ax.set_xticks(depths_present)

        # Bino observer PPL
        d_arr, s_arr = get_depth_scores(obs_ppls[cond])
        ax = axes[row, 1]
        for d in depths_present:
            mask = d_arr == d
            ax.scatter(np.full(mask.sum(), d) + np.random.uniform(-0.15, 0.15, mask.sum()),
                       s_arr[mask], alpha=0.3, s=6)
        rho, p = spearmanr(d_arr, s_arr)
        ax.set_title(f"Bino observer PPL\n{cond}: ρ={rho:.3f}" if row == 0 else f"ρ={rho:.3f}", fontsize=9)
        ax.set_xticks(depths_present)

        # Bino ratio
        ratio_dict = {}
        for d in depths_present:
            ratio_dict[d] = obs_ppls[cond][d] / np.clip(perf_ppls[cond][d], 1e-6, None)
        d_arr, s_arr = get_depth_scores(ratio_dict)
        ax = axes[row, 2]
        for d in depths_present:
            mask = d_arr == d
            ax.scatter(np.full(mask.sum(), d) + np.random.uniform(-0.15, 0.15, mask.sum()),
                       s_arr[mask], alpha=0.3, s=6)
        rho, p = spearmanr(d_arr, s_arr)
        ax.set_title(f"Bino ratio (obs/perf)\n{cond}: ρ={rho:.3f}" if row == 0 else f"ρ={rho:.3f}", fontsize=9)
        ax.set_xticks(depths_present)

    for ax in axes[-1, :]:
        ax.set_xlabel("Generational Depth")

    fig.suptitle("exp-012: Binary Detector Confidence vs. True Depth", fontsize=13, y=1.01)
    fig.tight_layout()
    fig.savefig(output_path, bbox_inches="tight", dpi=150)
    print(f"Plot saved to {output_path}")
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="exp012: PPL vs depth correlation")
    parser.add_argument("--n_samples", type=int, default=500,
                        help="Samples per depth per condition (default: 500)")
    parser.add_argument("--batch_size", type=int, default=8,
                        help="Inference batch size (default: 8)")
    parser.add_argument("--max_length", type=int, default=512,
                        help="Max token length for truncation (default: 512)")
    parser.add_argument("--device", type=str, default=None,
                        help="Device: cuda / cpu (default: auto)")
    parser.add_argument("--ref_model", type=str, default="Qwen/Qwen2.5-1.5B-Instruct")
    parser.add_argument("--bino_observer", type=str, default="EleutherAI/pythia-1.4b")
    parser.add_argument("--bino_performer", type=str, default="allenai/OLMo-1B-0724-hf")
    parser.add_argument("--output_dir", type=str,
                        default=str(PROJECT_ROOT / "artifacts"))
    args = parser.parse_args()

    os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    if args.device is not None:
        device = torch.device(args.device)
    else:
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    # --- Load texts ---
    print("Loading texts...")
    all_texts: dict[str, dict[int, list[str]]] = {}
    for cond, data_dir in MODEL_CONDITIONS.items():
        print(f"  {cond}: {data_dir}")
        all_texts[cond] = load_texts(data_dir, args.n_samples)
        for d, t in sorted(all_texts[cond].items()):
            print(f"    depth {d}: {len(t)} samples")

    total_texts = sum(len(t) for cond_texts in all_texts.values() for t in cond_texts.values())
    print(f"Total texts: {total_texts}")

    # --- Load models sequentially to minimize GPU memory ---
    from transformers import AutoModelForCausalLM, AutoTokenizer

    # 1) Reference model (DivEye log-PPL)
    print(f"\nLoading reference model: {args.ref_model}")
    ref_tokenizer = AutoTokenizer.from_pretrained(args.ref_model, trust_remote_code=True)
    ref_model = AutoModelForCausalLM.from_pretrained(
        args.ref_model, torch_dtype=torch.float16, trust_remote_code=True
    ).to(device).eval()
    if ref_tokenizer.pad_token is None:
        ref_tokenizer.pad_token = ref_tokenizer.eos_token
        ref_model.config.pad_token_id = ref_model.config.eos_token_id

    print("Computing reference model PPL...")
    ref_ppls: dict[str, dict[int, np.ndarray]] = {}
    for cond in MODEL_CONDITIONS:
        print(f"  {cond}...")
        ref_ppls[cond] = {}
        for d, texts in sorted(all_texts[cond].items()):
            ref_ppls[cond][d] = compute_log_perplexity_batch(
                ref_model, ref_tokenizer, texts, args.batch_size, args.max_length
            )
            print(f"    depth {d}: mean_ppl={ref_ppls[cond][d].mean():.4f}")

    del ref_model
    torch.cuda.empty_cache()

    # 2) Binoculars performer (OLMo) — own tokenizer
    print(f"\nLoading Binoculars performer model: {args.bino_performer}")
    perf_tokenizer = AutoTokenizer.from_pretrained(args.bino_performer)
    perf_model = AutoModelForCausalLM.from_pretrained(
        args.bino_performer, torch_dtype=torch.float16
    ).to(device).eval()
    if perf_tokenizer.pad_token is None:
        perf_tokenizer.pad_token = perf_tokenizer.eos_token
        perf_model.config.pad_token_id = perf_model.config.eos_token_id

    print("Computing Binoculars performer PPL...")
    perf_ppls: dict[str, dict[int, np.ndarray]] = {}
    for cond in MODEL_CONDITIONS:
        print(f"  {cond}...")
        perf_ppls[cond] = {}
        for d, texts in sorted(all_texts[cond].items()):
            perf_ppls[cond][d] = compute_log_perplexity_batch(
                perf_model, perf_tokenizer, texts, args.batch_size, args.max_length
            )
            print(f"    depth {d}: mean_ppl={perf_ppls[cond][d].mean():.4f}")

    del perf_model
    torch.cuda.empty_cache()

    # 3) Binoculars observer (Pythia) — own tokenizer
    print(f"\nLoading Binoculars observer model: {args.bino_observer}")
    obs_tokenizer = AutoTokenizer.from_pretrained(args.bino_observer)
    obs_model = AutoModelForCausalLM.from_pretrained(
        args.bino_observer, torch_dtype=torch.float16
    ).to(device).eval()
    if obs_tokenizer.pad_token is None:
        obs_tokenizer.pad_token = obs_tokenizer.eos_token
        obs_model.config.pad_token_id = obs_model.config.eos_token_id

    print("Computing Binoculars observer PPL...")
    obs_ppls: dict[str, dict[int, np.ndarray]] = {}
    for cond in MODEL_CONDITIONS:
        print(f"  {cond}...")
        obs_ppls[cond] = {}
        for d, texts in sorted(all_texts[cond].items()):
            obs_ppls[cond][d] = compute_log_perplexity_batch(
                obs_model, obs_tokenizer, texts, args.batch_size, args.max_length
            )
            print(f"    depth {d}: mean_ppl={obs_ppls[cond][d].mean():.4f}")

    del obs_model
    torch.cuda.empty_cache()

    # --- Analysis ---
    print("\nAnalyzing...")
    results = {}
    for cond in MODEL_CONDITIONS:
        results[cond] = analyze_condition(cond, ref_ppls[cond], obs_ppls[cond], perf_ppls[cond])

    # --- Save results ---
    out_path = output_dir / "exp012_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # --- Per-sample scores ---
    per_sample_path = output_dir / "exp012_per_sample_scores.json"
    per_sample = {}
    for cond in MODEL_CONDITIONS:
        per_sample[cond] = {}
        for d in sorted(ref_ppls[cond].keys()):
            per_sample[cond][str(d)] = {
                "log_ppl_ref": ref_ppls[cond][d].tolist(),
                "log_ppl_bino_obs": obs_ppls[cond][d].tolist(),
                "log_ppl_bino_perf": perf_ppls[cond][d].tolist(),
            }
    with open(per_sample_path, "w") as f:
        json.dump(per_sample, f)
    print(f"Per-sample scores saved to {per_sample_path}")

    # --- Visualization ---
    plot_path = output_dir / "exp012_confidence_vs_depth.pdf"
    make_plots(ref_ppls, obs_ppls, perf_ppls, plot_path)

    print_summary(results)


if __name__ == "__main__":
    main()
