"""CCS (Contrast Consistent Search) Unsupervised Probe — Burns et al. ICLR 2023.

Trains a linear probe with consistency + confidence losses only (no labels).
Pairs: pre-CP hidden states (x+) vs post-CP hidden states (x-).
"""

import os, sys, json, glob, warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
# os.environ["HF_ENDPOINT"] = "..."  # set HF mirror if needed
warnings.filterwarnings("ignore")

import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import balanced_accuracy_score, precision_score

sys.path.insert(0, "DATA_DIR")
from src.config import SEED, DETECTION_WINDOW

PROJECT = Path("DATA_DIR")
K_CONSECUTIVE = DETECTION_WINDOW
N_SEEDS = 10
CCS_LR = 1e-3
CCS_STEPS = 1000
CCS_WEIGHT_DECAY = 0.01

MODEL_CONFIGS = {
    "r1-8b": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states",
        "layer_idx": 2,
        "hidden_dim": 4096,
    },
    "r1-32b": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_r1_32b",
        "layer_idx": 10,
        "hidden_dim": 5120,
    },
    "qwq-32b": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_qwq_32b",
        "layer_idx": 2,
        "hidden_dim": 5120,
    },
    "ot-7b": {
        "hs_dir": PROJECT / "artifacts" / "hidden_states_ot7b",
        "layer_idx": 16,
        "hidden_dim": 3584,
    },
}


def load_traces(hs_dir):
    traces = []
    for pt_file in sorted(glob.glob(str(hs_dir / "*.pt"))):
        data = torch.load(pt_file, map_location="cpu", weights_only=False)
        if data.get("step_labels") is None or data.get("commitment_point") is None:
            continue
        traces.append(data)
    return traces


def split_traces(traces, seed=SEED):
    rng = np.random.default_rng(seed)
    indices = rng.permutation(len(traces))
    n_train = int(len(traces) * 0.6)
    n_val = int(len(traces) * 0.2)
    return (
        [traces[i] for i in indices[:n_train]],
        [traces[i] for i in indices[n_train:n_train + n_val]],
        [traces[i] for i in indices[n_train + n_val:]],
    )


class CCSProbe(nn.Module):
    def __init__(self, input_dim):
        super().__init__()
        self.linear = nn.Linear(input_dim, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))


def collect_pairs(traces, layer_idx):
    pre_list, post_list = [], []
    for t in traces:
        hs = t["hidden_states"][:, layer_idx, :].float()
        labels = np.array(t["step_labels"])
        n = min(hs.shape[0], len(labels))
        hs, labels = hs[:n], labels[:n]
        pre_list.append(hs[labels == 0])
        post_list.append(hs[labels == 1])
    return torch.cat(pre_list, dim=0), torch.cat(post_list, dim=0)


def normalize_hs(pre_hs, post_hs):
    all_hs = torch.cat([pre_hs, post_hs], dim=0)
    mean = all_hs.mean(dim=0)
    std = all_hs.std(dim=0) + 1e-8
    return (pre_hs - mean) / std, (post_hs - mean) / std, mean, std


def train_ccs_single(pre_norm, post_norm, input_dim, seed):
    torch.manual_seed(seed)
    probe = CCSProbe(input_dim)
    optimizer = torch.optim.AdamW(probe.parameters(), lr=CCS_LR,
                                  weight_decay=CCS_WEIGHT_DECAY)

    n_pre, n_post = pre_norm.shape[0], post_norm.shape[0]
    n_pairs = min(n_pre, n_post)
    best_loss, best_state = float("inf"), None

    for step in range(CCS_STEPS):
        pre_idx = torch.randperm(n_pre)[:n_pairs]
        post_idx = torch.randperm(n_post)[:n_pairs]
        x_pre, x_post = pre_norm[pre_idx], post_norm[post_idx]

        p_pre = probe(x_pre)
        p_post = probe(x_post)

        consistency = ((p_pre + p_post - 1) ** 2).mean()
        confidence = (torch.min(p_pre, p_post) ** 2).mean()
        loss = consistency + confidence

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if loss.item() < best_loss:
            best_loss = loss.item()
            best_state = {k: v.clone() for k, v in probe.state_dict().items()}

    if best_state:
        probe.load_state_dict(best_state)
    return probe, best_loss


def train_ccs(train_traces, layer_idx, input_dim):
    pre_hs, post_hs = collect_pairs(train_traces, layer_idx)
    print(f"  Pairs: {pre_hs.shape[0]} pre-CP, {post_hs.shape[0]} post-CP steps")

    pre_norm, post_norm, mean, std = normalize_hs(pre_hs, post_hs)

    best_probe, best_loss = None, float("inf")
    for s in range(N_SEEDS):
        probe, loss = train_ccs_single(pre_norm, post_norm, input_dim, seed=SEED + s)
        print(f"    Seed {s}: loss={loss:.6f}")
        if loss < best_loss:
            best_loss = loss
            best_probe = probe

    print(f"  Best CCS loss: {best_loss:.6f}")
    return best_probe, mean, std


def predict_ccs(probe, traces, layer_idx, mean, std):
    results = []
    for t in traces:
        hs = t["hidden_states"][:, layer_idx, :].float()
        labels = np.array(t["step_labels"])
        n = min(hs.shape[0], len(labels))
        hs, labels = hs[:n], labels[:n]

        hs_norm = (hs - mean) / (std + 1e-8)
        with torch.no_grad():
            probs = probe(hs_norm).squeeze(-1).numpy()

        results.append({
            "trace_id": t["trace_id"],
            "probs": probs,
            "labels": labels,
            "commitment_point": t["commitment_point"],
        })
    return results


def determine_polarity(train_results):
    all_probs = np.concatenate([r["probs"] for r in train_results])
    all_labels = np.concatenate([r["labels"] for r in train_results])
    preds = (all_probs > 0.5).astype(int)
    bal_acc = balanced_accuracy_score(all_labels, preds)
    return bal_acc < 0.5


def first_crossing_point(probs, threshold=0.5, k=K_CONSECUTIVE):
    n = len(probs)
    if n < k:
        return None
    for i in range(n - k + 1):
        if all(probs[i:i + k] > threshold):
            return i
    return None


def evaluate(results, flip=False):
    all_probs, all_labels = [], []
    pre_cp_fps, pre_cp_total = 0, 0
    detected = 0
    leads = []

    for r in results:
        probs = 1 - r["probs"] if flip else r["probs"]
        labels = r["labels"]
        cp = r["commitment_point"]

        all_probs.append(probs)
        all_labels.append(labels)

        pre_preds = (probs[:cp] > 0.5).astype(int)
        pre_cp_fps += pre_preds.sum()
        pre_cp_total += len(pre_preds)

        fcp = first_crossing_point(probs)
        if fcp is not None:
            detected += 1
            leads.append(cp - fcp)

    all_probs = np.concatenate(all_probs)
    all_labels = np.concatenate(all_labels)
    preds = (all_probs > 0.5).astype(int)

    return {
        "bal_acc": round(float(balanced_accuracy_score(all_labels, preds)), 4),
        "precision": round(float(precision_score(all_labels, preds, zero_division=0)), 4),
        "pre_cp_fpr": round(float(pre_cp_fps / max(pre_cp_total, 1)), 4),
        "coverage": round(float(detected / max(len(results), 1)), 4),
        "lead_mean": round(float(np.mean(leads)), 1) if leads else None,
        "n_detected": detected,
        "n_traces": len(results),
    }


def run_model(model_name, config):
    hs_dir = config["hs_dir"]
    if not hs_dir.exists():
        print(f"\n  {model_name}: hidden states dir not found, skipping")
        return None

    print(f"\n{'='*60}")
    print(f"  {model_name} (layer_idx={config['layer_idx']}, dim={config['hidden_dim']})")
    print(f"{'='*60}")

    traces = load_traces(hs_dir)
    print(f"  Loaded {len(traces)} jailbreak traces with CP")
    if len(traces) < 10:
        print(f"  Too few traces, skipping")
        return None

    train, val, test = split_traces(traces)
    print(f"  Split: train={len(train)}, val={len(val)}, test={len(test)}")

    probe, mean, std = train_ccs(train, config["layer_idx"], config["hidden_dim"])

    train_results = predict_ccs(probe, train, config["layer_idx"], mean, std)
    flip = determine_polarity(train_results)
    print(f"  Polarity flip: {flip}")

    train_metrics = evaluate(train_results, flip=flip)
    print(f"  Train bal_acc: {train_metrics['bal_acc']:.4f}")

    test_results = predict_ccs(probe, test, config["layer_idx"], mean, std)
    metrics = evaluate(test_results, flip=flip)
    metrics["flip"] = flip
    metrics["train_bal_acc"] = train_metrics["bal_acc"]

    print(f"\n  TEST RESULTS:")
    print(f"    bal_acc:    {metrics['bal_acc']:.4f}")
    print(f"    precision:  {metrics['precision']:.4f}")
    print(f"    pre_cp_fpr: {metrics['pre_cp_fpr']:.4f}")
    print(f"    coverage:   {metrics['coverage']:.4f}")
    print(f"    lead_mean:  {metrics['lead_mean']}")

    return metrics


def main():
    print("=" * 60)
    print("CCS UNSUPERVISED PROBE: Burns et al. ICLR 2023")
    print("=" * 60)
    print(f"Seed: {SEED}, N_seeds: {N_SEEDS}, Steps: {CCS_STEPS}")
    print(f"Pair construction: pre-CP vs post-CP (Method A)")

    all_results = {}
    for model_name, config in MODEL_CONFIGS.items():
        result = run_model(model_name, config)
        if result is not None:
            all_results[model_name] = result

    out_dir = PROJECT / "artifacts" / "exp_r3_ccs_probe"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "results.json"
    with open(out_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nResults saved to: {out_path}")

    lr_ref = {
        "r1-8b": {"bal_acc": 0.817, "precision": 0.693, "pre_cp_fpr": 0.097, "lead_mean": -2.0},
    }
    repe_ref = {
        "r1-8b": {"bal_acc": 0.749, "precision": 0.516, "pre_cp_fpr": 0.226, "lead_mean": 9.7},
    }

    print(f"\n{'='*80}")
    print("COMPARISON: CCS vs RepE vs LR Probe (R1-8B)")
    print(f"{'='*80}")
    print(f"{'Method':<15} {'Type':<14} {'bal_acc':>8} {'precision':>10} {'FPR':>8} {'lead':>8}")
    print("-" * 65)

    if "r1-8b" in lr_ref:
        d = lr_ref["r1-8b"]
        lead_s = f"{d['lead_mean']:+.1f}" if d["lead_mean"] is not None else "N/A"
        print(f"{'LR probe':<15} {'supervised':<14} {d['bal_acc']:>8.3f} {d['precision']:>10.3f} {d['pre_cp_fpr']:>8.3f} {lead_s:>8}")

    if "r1-8b" in repe_ref:
        d = repe_ref["r1-8b"]
        lead_s = f"{d['lead_mean']:+.1f}" if d["lead_mean"] is not None else "N/A"
        print(f"{'RepE':<15} {'unsupervised':<14} {d['bal_acc']:>8.3f} {d['precision']:>10.3f} {d['pre_cp_fpr']:>8.3f} {lead_s:>8}")

    if "r1-8b" in all_results:
        d = all_results["r1-8b"]
        lead_s = f"{d['lead_mean']:+.1f}" if d["lead_mean"] is not None else "N/A"
        print(f"{'CCS':<15} {'unsupervised':<14} {d['bal_acc']:>8.3f} {d['precision']:>10.3f} {d['pre_cp_fpr']:>8.3f} {lead_s:>8}")

    print("=" * 65)

    if len(all_results) > 1:
        print(f"\n{'='*80}")
        print("ALL MODELS: CCS Results")
        print(f"{'='*80}")
        print(f"{'Model':<10} {'bal_acc':>8} {'precision':>10} {'pre_cp_fpr':>11} {'coverage':>9} {'lead_mean':>10}")
        print("-" * 60)
        for m, r in all_results.items():
            lead_s = f"{r['lead_mean']:+.1f}" if r['lead_mean'] is not None else "N/A"
            print(f"{m:<10} {r['bal_acc']:>8.4f} {r['precision']:>10.4f} {r['pre_cp_fpr']:>11.4f} {r['coverage']:>9.4f} {lead_s:>10}")
        print("=" * 60)

    sys.stdout.flush()


if __name__ == "__main__":
    main()
