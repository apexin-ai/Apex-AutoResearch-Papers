#!/usr/bin/env python3
"""exp48: Ensemble JB-MLM + 9-class models for jailbreak detection.

Two complementary DeBERTa+GRU models:
  - JB-MLM: DeBERTa-v3-base with MLM continued pretraining on jailbreak data
  - 9-class: DeBERTa-v3-base with 9-class persuasion classification DAPT

Fusion methods:
  1. Logit averaging (pre-softmax)
  2. Majority vote (AND / OR)
  3. Weighted probability averaging (grid search over MLM weight)

Evaluation: IID test F1, OOD (DD/AA/FITD) F1, ToxicChat F1, WildChat FPR.

Run:
  source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  cd /root/persuasion_turn_jailbreak_detect && \
  python scripts/exp48_ensemble.py --device cuda:0
"""

import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import sys
import json
import argparse
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import f1_score, accuracy_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier
from transformers import AutoModel, AutoTokenizer

# =========================================================================
# PATHS
# =========================================================================
PROJ = Path("/root/persuasion_turn_jailbreak_detect")
ARCHIVE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive")
LOCAL_MODEL = "/root/autodl-tmp/hf_cache/hub/models--microsoft--deberta-v3-base/snapshots/8ccc9b6f36199bec6961081d44eb72fb3f7353f3"
MAX_LENGTH = 256

# Checkpoint config (same structure as exp35)
CKPT_CONFIG = {
    "jb_mlm": {
        42: {
            "deberta_type": "safetensors",
            "deberta": ARCHIVE / "plan_017_mlm/best",
            "tokenizer": ARCHIVE / "plan_017_mlm/best",
            "gru": ARCHIVE / "plan_017_mlm/gru/best.pt",
        },
        123: {
            "deberta_type": "safetensors",
            "deberta": ARCHIVE / "plan_017_mlm_seed123/best",
            "tokenizer": ARCHIVE / "plan_017_mlm_seed123/best",
            "gru": ARCHIVE / "plan_017_mlm_seed123/gru/best_gru.pt",
        },
        456: {
            "deberta_type": "safetensors",
            "deberta": ARCHIVE / "plan_017_mlm_seed456/best",
            "tokenizer": ARCHIVE / "plan_017_mlm_seed456/best",
            "gru": ARCHIVE / "plan_017_mlm_seed456/gru/best_gru.pt",
        },
    },
    "9class": {
        42: {
            "deberta_type": "multitask",
            "deberta": ARCHIVE / "plan_002/deberta_multitask/best/model.pt",
            "tokenizer": ARCHIVE / "plan_002/deberta_multitask/best",
            "gru": ARCHIVE / "plan_002/gru/treatment/best.pt",
        },
        123: {
            "deberta_type": "multitask",
            "deberta": ARCHIVE / "plan_002_seed123/deberta_multitask/best/model.pt",
            "tokenizer": ARCHIVE / "plan_002_seed123/deberta_multitask/best",
            "gru": ARCHIVE / "plan_002_seed123/gru/treatment/best.pt",
        },
        456: {
            "deberta_type": "multitask",
            "deberta": ARCHIVE / "plan_002_seed456/deberta_multitask/best/model.pt",
            "tokenizer": ARCHIVE / "plan_002_seed456/deberta_multitask/best",
            "gru": ARCHIVE / "plan_002_seed456/gru/treatment/best.pt",
        },
    },
}

# Data paths
TEST_PATH = PROJ / "data" / "plan_002_splits" / "test.jsonl"
DD_PATH = PROJ / "data" / "generated" / "deceptive_delight_all.jsonl"
AA_PATH = PROJ / "data" / "actorattack_ood" / "actorattack_all.jsonl"
FITD_PATH = PROJ / "data" / "generated" / "fitd_all.jsonl"
TOXICCHAT_PATH = PROJ / "data" / "mhj" / "toxicchat_eval.jsonl"
WILDCHAT_PATH = PROJ / "data" / "exp42_wildchat_eval.jsonl"
RESULTS_JSON = PROJ / "results" / "exp48_ensemble.json"

# Fusion weights for grid search
MLM_WEIGHTS = [0.3, 0.4, 0.5, 0.6, 0.7]

# GRU config (must match training)
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3


# =========================================================================
# UTILS
# =========================================================================
def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    lbl = conv.get("label", "benign")
    if isinstance(lbl, int):
        return lbl
    return 1 if lbl == "jailbreak" else 0


def load_model(model_type, seed, device):
    """Load DeBERTa encoder + GRU classifier for a given model type and seed."""
    cfg = CKPT_CONFIG[model_type][seed]

    if cfg["deberta_type"] == "multitask":
        mt = DeBERTaMultiTask(model_name=LOCAL_MODEL, num_persuasion_classes=9)
        sd = torch.load(cfg["deberta"], map_location="cpu")
        mt.load_state_dict(sd)
        encoder = mt.deberta
        del mt
    else:  # safetensors
        encoder = AutoModel.from_pretrained(str(cfg["deberta"]), torch_dtype=torch.float32)

    tokenizer = AutoTokenizer.from_pretrained(str(cfg["tokenizer"]))
    encoder.to(device).eval()
    for p in encoder.parameters():
        p.requires_grad = False

    embed_dim = encoder.config.hidden_size
    gru = GRUClassifier(
        input_dim=embed_dim,
        hidden_dim=GRU_HIDDEN,
        num_layers=GRU_LAYERS,
        dropout=GRU_DROPOUT,
    )
    gru.load_state_dict(torch.load(cfg["gru"], map_location="cpu", weights_only=True))
    gru.to(device).eval()

    return encoder, tokenizer, gru


# =========================================================================
# INFERENCE
# =========================================================================
@torch.no_grad()
def get_logits_for_dataset(encoder, tokenizer, gru, convs, device):
    """Run inference and return raw GRU logits (N, 2) for each conversation."""
    all_logits = []
    for conv in convs:
        turns = extract_user_turns(conv)
        if not turns:
            turns = [""]
        tok = tokenizer(
            turns,
            max_length=MAX_LENGTH,
            padding=True,
            truncation=True,
            return_tensors="pt",
        ).to(device)
        out = encoder(input_ids=tok["input_ids"], attention_mask=tok["attention_mask"])
        embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
        lens = torch.tensor([embs.size(1)], device=device)
        logits = gru(embs, lens)  # (1, 2)
        all_logits.append(logits.cpu())
    return torch.cat(all_logits, dim=0)  # (N, 2)


# =========================================================================
# ENSEMBLE METHODS
# =========================================================================
def ensemble_logit_avg(logits_mlm, logits_9class):
    """Average logits (pre-softmax), then argmax."""
    avg = (logits_mlm + logits_9class) / 2.0
    probs = torch.softmax(avg, dim=1)[:, 1].numpy()
    preds = avg.argmax(dim=1).numpy()
    return preds, probs


def ensemble_vote_and(preds_mlm, preds_9class):
    """AND vote: both must predict jailbreak."""
    preds = ((preds_mlm == 1) & (preds_9class == 1)).astype(int)
    return preds


def ensemble_vote_or(preds_mlm, preds_9class):
    """OR vote: either predicts jailbreak."""
    preds = ((preds_mlm == 1) | (preds_9class == 1)).astype(int)
    return preds


def ensemble_weighted_avg(logits_mlm, logits_9class, mlm_weight):
    """Weighted average of softmax probabilities."""
    probs_mlm = torch.softmax(logits_mlm, dim=1)[:, 1].numpy()
    probs_9class = torch.softmax(logits_9class, dim=1)[:, 1].numpy()
    probs = mlm_weight * probs_mlm + (1.0 - mlm_weight) * probs_9class
    preds = (probs > 0.5).astype(int)
    return preds, probs


# =========================================================================
# EVALUATION
# =========================================================================
def eval_preds(y_true, y_pred):
    return {
        "f1_macro": float(f1_score(y_true, y_pred, average="macro")),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "n": len(y_true),
    }


def eval_ood(ood_preds, iid_benign_preds, n_ood):
    """OOD evaluation: combine OOD jailbreak with IID benign."""
    combined_preds = list(iid_benign_preds) + list(ood_preds)
    combined_true = [0] * len(iid_benign_preds) + [1] * n_ood
    recall = float(np.sum(ood_preds)) / n_ood if n_ood > 0 else 0.0
    f1 = float(f1_score(combined_true, combined_preds, average="macro"))
    return {"f1_macro": f1, "recall": recall, "n_ood": n_ood}


def eval_wildchat_fpr(preds):
    """WildChat is all benign; any predicted as 1 is FP."""
    fpr = float(np.sum(preds)) / len(preds)
    return {"fpr": fpr, "fp": int(np.sum(preds)), "n": len(preds)}


# =========================================================================
# MAIN
# =========================================================================
def run_single_seed(seed, device):
    """Run full ensemble evaluation for a single seed pair."""
    print(f"\n{'='*60}", flush=True)
    print(f"Loading models (seed={seed})", flush=True)
    print(f"{'='*60}", flush=True)

    # Load both models
    enc_mlm, tok_mlm, gru_mlm = load_model("jb_mlm", seed, device)
    enc_9c, tok_9c, gru_9c = load_model("9class", seed, device)

    # Load all datasets
    test_data = load_jsonl(TEST_PATH)
    test_labels = np.array([get_label(c) for c in test_data])
    iid_benign = [c for c in test_data if get_label(c) == 0]

    ood_datasets = {}
    for name, path in [("DD", DD_PATH), ("AA", AA_PATH), ("FITD", FITD_PATH)]:
        if path.exists():
            ood_datasets[name] = load_jsonl(path)

    toxicchat = load_jsonl(TOXICCHAT_PATH)
    tc_labels = np.array([get_label(c) for c in toxicchat])

    wildchat = load_jsonl(WILDCHAT_PATH)

    # Get logits from both models on all datasets
    print("Extracting logits from JB-MLM...", flush=True)
    logits_mlm = {
        "iid": get_logits_for_dataset(enc_mlm, tok_mlm, gru_mlm, test_data, device),
        "toxicchat": get_logits_for_dataset(enc_mlm, tok_mlm, gru_mlm, toxicchat, device),
        "wildchat": get_logits_for_dataset(enc_mlm, tok_mlm, gru_mlm, wildchat, device),
        "iid_benign": get_logits_for_dataset(enc_mlm, tok_mlm, gru_mlm, iid_benign, device),
    }
    for name, data in ood_datasets.items():
        logits_mlm[f"ood_{name}"] = get_logits_for_dataset(enc_mlm, tok_mlm, gru_mlm, data, device)

    print("Extracting logits from 9-class...", flush=True)
    logits_9c = {
        "iid": get_logits_for_dataset(enc_9c, tok_9c, gru_9c, test_data, device),
        "toxicchat": get_logits_for_dataset(enc_9c, tok_9c, gru_9c, toxicchat, device),
        "wildchat": get_logits_for_dataset(enc_9c, tok_9c, gru_9c, wildchat, device),
        "iid_benign": get_logits_for_dataset(enc_9c, tok_9c, gru_9c, iid_benign, device),
    }
    for name, data in ood_datasets.items():
        logits_9c[f"ood_{name}"] = get_logits_for_dataset(enc_9c, tok_9c, gru_9c, data, device)

    # Free GPU memory
    del enc_mlm, gru_mlm, enc_9c, gru_9c
    torch.cuda.empty_cache()

    # Individual model predictions (for reference)
    preds_mlm_iid = logits_mlm["iid"].argmax(dim=1).numpy()
    preds_9c_iid = logits_9c["iid"].argmax(dim=1).numpy()

    results = {"seed": seed, "individual": {}, "ensemble": {}}

    # Individual baselines
    results["individual"]["jb_mlm"] = {
        "iid": eval_preds(test_labels, preds_mlm_iid),
        "toxicchat": eval_preds(tc_labels, logits_mlm["toxicchat"].argmax(dim=1).numpy()),
        "wildchat": eval_wildchat_fpr(logits_mlm["wildchat"].argmax(dim=1).numpy()),
    }
    results["individual"]["9class"] = {
        "iid": eval_preds(test_labels, preds_9c_iid),
        "toxicchat": eval_preds(tc_labels, logits_9c["toxicchat"].argmax(dim=1).numpy()),
        "wildchat": eval_wildchat_fpr(logits_9c["wildchat"].argmax(dim=1).numpy()),
    }
    preds_mlm_benign = logits_mlm["iid_benign"].argmax(dim=1).numpy()
    preds_9c_benign = logits_9c["iid_benign"].argmax(dim=1).numpy()
    for name in ood_datasets:
        key = f"ood_{name}"
        mlm_ood_preds = logits_mlm[key].argmax(dim=1).numpy()
        nc_ood_preds = logits_9c[key].argmax(dim=1).numpy()
        results["individual"]["jb_mlm"][key] = eval_ood(mlm_ood_preds, preds_mlm_benign, len(ood_datasets[name]))
        results["individual"]["9class"][key] = eval_ood(nc_ood_preds, preds_9c_benign, len(ood_datasets[name]))

    print("\n--- Individual baselines ---", flush=True)
    for mt in ["jb_mlm", "9class"]:
        r = results["individual"][mt]
        print(f"  {mt}: IID F1={r['iid']['f1_macro']:.4f}  TC F1={r['toxicchat']['f1_macro']:.4f}  WC FPR={r['wildchat']['fpr']:.4f}", flush=True)

    # --- Method 1: Logit averaging ---
    print("\n--- Logit averaging ---", flush=True)
    ens_logit = {}
    preds_la_iid, probs_la_iid = ensemble_logit_avg(logits_mlm["iid"], logits_9c["iid"])
    ens_logit["iid"] = eval_preds(test_labels, preds_la_iid)

    preds_la_tc, _ = ensemble_logit_avg(logits_mlm["toxicchat"], logits_9c["toxicchat"])
    ens_logit["toxicchat"] = eval_preds(tc_labels, preds_la_tc)

    preds_la_wc, _ = ensemble_logit_avg(logits_mlm["wildchat"], logits_9c["wildchat"])
    ens_logit["wildchat"] = eval_wildchat_fpr(preds_la_wc)

    preds_la_benign, _ = ensemble_logit_avg(logits_mlm["iid_benign"], logits_9c["iid_benign"])
    for name in ood_datasets:
        preds_la_ood, _ = ensemble_logit_avg(logits_mlm[f"ood_{name}"], logits_9c[f"ood_{name}"])
        ens_logit[f"ood_{name}"] = eval_ood(preds_la_ood, preds_la_benign, len(ood_datasets[name]))

    results["ensemble"]["logit_avg"] = ens_logit
    print(f"  IID F1={ens_logit['iid']['f1_macro']:.4f}  TC F1={ens_logit['toxicchat']['f1_macro']:.4f}  WC FPR={ens_logit['wildchat']['fpr']:.4f}", flush=True)

    # --- Method 2: Majority vote (AND / OR) ---
    for vote_type, vote_fn in [("vote_and", ensemble_vote_and), ("vote_or", ensemble_vote_or)]:
        print(f"\n--- {vote_type} ---", flush=True)
        ens_vote = {}

        preds_v_iid = vote_fn(preds_mlm_iid, preds_9c_iid)
        ens_vote["iid"] = eval_preds(test_labels, preds_v_iid)

        preds_v_tc = vote_fn(
            logits_mlm["toxicchat"].argmax(dim=1).numpy(),
            logits_9c["toxicchat"].argmax(dim=1).numpy(),
        )
        ens_vote["toxicchat"] = eval_preds(tc_labels, preds_v_tc)

        preds_v_wc = vote_fn(
            logits_mlm["wildchat"].argmax(dim=1).numpy(),
            logits_9c["wildchat"].argmax(dim=1).numpy(),
        )
        ens_vote["wildchat"] = eval_wildchat_fpr(preds_v_wc)

        preds_v_benign = vote_fn(preds_mlm_benign, preds_9c_benign)
        for name in ood_datasets:
            preds_v_ood = vote_fn(
                logits_mlm[f"ood_{name}"].argmax(dim=1).numpy(),
                logits_9c[f"ood_{name}"].argmax(dim=1).numpy(),
            )
            ens_vote[f"ood_{name}"] = eval_ood(preds_v_ood, preds_v_benign, len(ood_datasets[name]))

        results["ensemble"][vote_type] = ens_vote
        print(f"  IID F1={ens_vote['iid']['f1_macro']:.4f}  TC F1={ens_vote['toxicchat']['f1_macro']:.4f}  WC FPR={ens_vote['wildchat']['fpr']:.4f}", flush=True)

    # --- Method 3: Weighted probability averaging ---
    print("\n--- Weighted probability averaging ---", flush=True)
    best_w = None
    best_iid_f1 = -1.0
    for w in MLM_WEIGHTS:
        preds_w_iid, _ = ensemble_weighted_avg(logits_mlm["iid"], logits_9c["iid"], w)
        iid_f1 = float(f1_score(test_labels, preds_w_iid, average="macro"))
        if iid_f1 > best_iid_f1:
            best_iid_f1 = iid_f1
            best_w = w

    results["ensemble"]["weighted_avg"] = {"grid_search": {}}
    for w in MLM_WEIGHTS:
        ens_w = {"mlm_weight": w}

        preds_w_iid, probs_w_iid = ensemble_weighted_avg(logits_mlm["iid"], logits_9c["iid"], w)
        ens_w["iid"] = eval_preds(test_labels, preds_w_iid)

        preds_w_tc, _ = ensemble_weighted_avg(logits_mlm["toxicchat"], logits_9c["toxicchat"], w)
        ens_w["toxicchat"] = eval_preds(tc_labels, preds_w_tc)

        preds_w_wc, _ = ensemble_weighted_avg(logits_mlm["wildchat"], logits_9c["wildchat"], w)
        ens_w["wildchat"] = eval_wildchat_fpr(preds_w_wc)

        preds_w_benign, _ = ensemble_weighted_avg(logits_mlm["iid_benign"], logits_9c["iid_benign"], w)
        for name in ood_datasets:
            preds_w_ood, _ = ensemble_weighted_avg(logits_mlm[f"ood_{name}"], logits_9c[f"ood_{name}"], w)
            ens_w[f"ood_{name}"] = eval_ood(preds_w_ood, preds_w_benign, len(ood_datasets[name]))

        results["ensemble"]["weighted_avg"]["grid_search"][str(w)] = ens_w
        marker = " <-- best IID" if w == best_w else ""
        print(f"  w={w}: IID F1={ens_w['iid']['f1_macro']:.4f}  TC F1={ens_w['toxicchat']['f1_macro']:.4f}  WC FPR={ens_w['wildchat']['fpr']:.4f}{marker}", flush=True)

    results["ensemble"]["weighted_avg"]["best_weight"] = best_w

    return results


def main():
    parser = argparse.ArgumentParser(description="exp48: JB-MLM + 9-class ensemble")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42],
                        help="Seeds to evaluate (default: [42]). Use --seeds 42 123 456 for 3-seed.")
    parser.add_argument("--device", type=str, default="cuda:0",
                        help="Device (default: cuda:0)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Only verify model loading, skip full evaluation")
    args = parser.parse_args()

    device = torch.device(args.device if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}", flush=True)

    if args.dry_run:
        print("\n=== DRY RUN: verifying model loading ===", flush=True)
        for mt in ["jb_mlm", "9class"]:
            seed = args.seeds[0]
            cfg = CKPT_CONFIG[mt][seed]
            print(f"\n{mt} (seed={seed}):", flush=True)
            print(f"  encoder: {cfg['deberta']}  exists={cfg['deberta'].exists() if isinstance(cfg['deberta'], Path) else 'N/A'}", flush=True)
            gru_path = cfg["gru"]
            print(f"  gru:     {gru_path}  exists={gru_path.exists()}", flush=True)

            enc, tok, gru = load_model(mt, seed, device)
            print(f"  encoder hidden_size={enc.config.hidden_size}", flush=True)
            print(f"  gru params={sum(p.numel() for p in gru.parameters()):,}", flush=True)
            del enc, gru
            torch.cuda.empty_cache()

        print("\nDry run passed.", flush=True)
        return

    all_seed_results = {}
    for seed in args.seeds:
        all_seed_results[str(seed)] = run_single_seed(seed, device)

    # Summary across seeds
    final = {"seeds": all_seed_results, "config": {
        "seeds": args.seeds,
        "device": str(device),
        "mlm_weights_grid": MLM_WEIGHTS,
    }}

    if len(args.seeds) > 1:
        summary = {}
        methods = ["logit_avg", "vote_and", "vote_or"]
        for method in methods:
            m_summary = {}
            for metric_key in ["iid", "toxicchat"]:
                f1s = [all_seed_results[str(s)]["ensemble"][method][metric_key]["f1_macro"] for s in args.seeds]
                m_summary[f"{metric_key}_f1_mean"] = float(np.mean(f1s))
                m_summary[f"{metric_key}_f1_std"] = float(np.std(f1s))
            wc_fprs = [all_seed_results[str(s)]["ensemble"][method]["wildchat"]["fpr"] for s in args.seeds]
            m_summary["wildchat_fpr_mean"] = float(np.mean(wc_fprs))
            m_summary["wildchat_fpr_std"] = float(np.std(wc_fprs))
            for ood_name in ["DD", "AA", "FITD"]:
                key = f"ood_{ood_name}"
                if key in all_seed_results[str(args.seeds[0])]["ensemble"][method]:
                    f1s = [all_seed_results[str(s)]["ensemble"][method][key]["f1_macro"] for s in args.seeds]
                    m_summary[f"{key}_f1_mean"] = float(np.mean(f1s))
                    m_summary[f"{key}_f1_std"] = float(np.std(f1s))
            summary[method] = m_summary

        # Weighted avg: summarize best weight per seed
        for w in MLM_WEIGHTS:
            w_key = str(w)
            w_summary = {}
            for metric_key in ["iid", "toxicchat"]:
                f1s = [all_seed_results[str(s)]["ensemble"]["weighted_avg"]["grid_search"][w_key][metric_key]["f1_macro"] for s in args.seeds]
                w_summary[f"{metric_key}_f1_mean"] = float(np.mean(f1s))
                w_summary[f"{metric_key}_f1_std"] = float(np.std(f1s))
            summary[f"weighted_w{w}"] = w_summary

        final["summary"] = summary

    RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_JSON, "w") as f:
        json.dump(final, f, indent=2)
    print(f"\nResults saved to {RESULTS_JSON}", flush=True)


if __name__ == "__main__":
    main()
