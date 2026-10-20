# Exp8 F1 metric correction: recompute all evaluations with both binary and macro F1.
# Also checks verazuo benign data leakage (train vs test-only benign).
# Saves raw predictions for reproducibility.

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/hf_cache"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "3"

import sys
import json
import random
from pathlib import Path
from collections import defaultdict

import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score

from transformers import AutoTokenizer, AutoModel

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.deberta_topic import DeBERTaTopic
from src.models.gru_classifier import GRUClassifier

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
CKPT = PROJ / "checkpoints"
LOCAL_MODEL = "/root/autodl-tmp/hf_cache/hub/models--microsoft--deberta-v3-base/snapshots/8ccc9b6f36199bec6961081d44eb72fb3f7353f3"
DEVICE = torch.device("cuda:0")  # maps to physical gpu:3 via CUDA_VISIBLE_DEVICES
MAX_LENGTH = 256

MODEL_CONFIGS = {
    "vanilla": {
        "encoder_type": "vanilla",
        "seeds": {
            42:  {"gru": CKPT / "plan_002/gru/baseline/best.pt"},
            123: {"gru": CKPT / "plan_002_seed123/gru/baseline/best.pt"},
            456: {"gru": CKPT / "plan_002_seed456/gru/baseline/best.pt"},
        },
    },
    "9class": {
        "encoder_type": "multitask",
        "num_classes": 9,
        "seeds": {
            42:  {"deberta": CKPT / "plan_002/deberta_multitask/best",
                  "gru": CKPT / "plan_002/gru/treatment/best.pt"},
            123: {"deberta": CKPT / "plan_002_seed123/deberta_multitask/best",
                  "gru": CKPT / "plan_002_seed123/gru/treatment/best.pt"},
            456: {"deberta": CKPT / "plan_002_seed456/deberta_multitask/best",
                  "gru": CKPT / "plan_002_seed456/gru/treatment/best.pt"},
        },
    },
    "binary": {
        "encoder_type": "multitask",
        "num_classes": 2,
        "seeds": {
            42:  {"deberta": CKPT / "mf1_binary_seed42/deberta_multitask/best",
                  "gru": CKPT / "mf1_binary_seed42/gru/treatment/best.pt"},
            123: {"deberta": CKPT / "mf1_binary_seed123/deberta_multitask/best",
                  "gru": CKPT / "mf1_binary_seed123/gru/treatment/best.pt"},
            456: {"deberta": CKPT / "mf1_binary_seed456/deberta_multitask/best",
                  "gru": CKPT / "mf1_binary_seed456/gru/treatment/best.pt"},
        },
    },
    "scrambled": {
        "encoder_type": "multitask",
        "num_classes": 9,
        "seeds": {
            42:  {"deberta": CKPT / "plan_003_scrambled_fix/deberta_multitask/best",
                  "gru": CKPT / "plan_003_scrambled_fix/gru/best.pt"},
            123: {"deberta": CKPT / "mf1_scrambled_seed123/deberta_multitask/best",
                  "gru": CKPT / "mf1_scrambled_seed123/gru/best.pt"},
            456: {"deberta": CKPT / "mf1_scrambled_seed456/deberta_multitask/best",
                  "gru": CKPT / "mf1_scrambled_seed456/gru/best.pt"},
        },
    },
    "jb_mlm": {
        "encoder_type": "hf_local",
        "seeds": {
            42:  {"deberta": CKPT / "plan_017_mlm/best",
                  "gru": CKPT / "plan_017_mlm/gru/best.pt"},
            123: {"deberta": CKPT / "plan_017_mlm_seed123/best",
                  "gru": CKPT / "plan_017_mlm_seed123/gru/best_gru.pt"},
            456: {"deberta": CKPT / "plan_017_mlm_seed456/best",
                  "gru": CKPT / "plan_017_mlm_seed456/gru/best_gru.pt"},
        },
    },
    "wiki_mlm": {
        "encoder_type": "hf_local",
        "seeds": {
            42:  {"deberta": CKPT / "plan_018_wiki_mlm/best",
                  "gru": CKPT / "plan_018_wiki_mlm/gru/best_gru.pt"},
            123: {"deberta": CKPT / "plan_018_wiki_mlm_seed123/best",
                  "gru": CKPT / "plan_018_wiki_mlm_seed123/gru/best_gru.pt"},
            456: {"deberta": CKPT / "plan_018_wiki_mlm_seed456/best",
                  "gru": CKPT / "plan_018_wiki_mlm_seed456/gru/best_gru.pt"},
        },
    },
    "topic": {
        "encoder_type": "topic",
        "seeds": {
            42:  {"deberta": CKPT / "plan_016v2_topic/best",
                  "gru": CKPT / "plan_016v2_topic/gru/best.pt"},
            123: {"deberta": CKPT / "plan_016v2_topic_seed123/best",
                  "gru": CKPT / "plan_016v2_topic_seed123/gru/gru_best.pt"},
            456: {"deberta": CKPT / "plan_016v2_topic_seed456/best",
                  "gru": CKPT / "plan_016v2_topic_seed456/gru/gru_best.pt"},
        },
    },
}


def load_conversations(path):
    convs = []
    with open(path) as f:
        for line in f:
            conv = json.loads(line.strip())
            user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
            label = 1 if conv["label"] == "jailbreak" else 0
            convs.append({"turns": user_turns, "label": label, "id": conv["conversation_id"]})
    return convs


def load_encoder(variant_cfg, seed_cfg):
    enc_type = variant_cfg["encoder_type"]
    if enc_type == "vanilla":
        encoder = AutoModel.from_pretrained(LOCAL_MODEL).to(DEVICE).eval()
    elif enc_type == "multitask":
        num_cls = variant_cfg.get("num_classes", 9)
        model = DeBERTaMultiTask(model_name=LOCAL_MODEL, num_persuasion_classes=num_cls)
        sd = torch.load(seed_cfg["deberta"] / "model.pt", map_location="cpu", weights_only=True)
        model.load_state_dict(sd)
        encoder = model.deberta.to(DEVICE).eval()
    elif enc_type == "hf_local":
        encoder = AutoModel.from_pretrained(seed_cfg["deberta"]).to(DEVICE).eval()
    elif enc_type == "topic":
        model = DeBERTaTopic(model_name=LOCAL_MODEL)
        sd = torch.load(seed_cfg["deberta"] / "model.pt", map_location="cpu", weights_only=True)
        model.load_state_dict(sd)
        encoder = model.deberta.to(DEVICE).eval()
    else:
        raise ValueError(f"Unknown encoder type: {enc_type}")
    for p in encoder.parameters():
        p.requires_grad = False
    return encoder


def embed_and_predict(convs, tokenizer, encoder, gru):
    all_embs = []
    all_labels = []
    all_lengths = []

    for conv in convs:
        turns = conv["turns"]
        if len(turns) == 0:
            turns = [""]
        enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            outputs = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
            embs = outputs.last_hidden_state[:, 0, :].cpu()
        all_embs.append(embs)
        all_labels.append(conv["label"])
        all_lengths.append(len(turns))

    max_len = max(all_lengths)
    embed_dim = all_embs[0].size(1)
    padded = torch.zeros(len(all_embs), max_len, embed_dim)
    for i, e in enumerate(all_embs):
        padded[i, :e.size(0), :] = e

    lengths_tensor = torch.tensor(all_lengths, dtype=torch.long)
    labels_np = np.array(all_labels)

    gru.eval()
    with torch.no_grad():
        padded = padded.to(DEVICE)
        logits = gru(padded, lengths_tensor.to(DEVICE))
        preds = logits.argmax(-1).cpu().numpy()
        probs = torch.softmax(logits, dim=-1)[:, 1].cpu().numpy()

    return labels_np, preds, probs


def compute_metrics(y_true, y_pred, y_prob):
    metrics = {
        "binary_f1": float(f1_score(y_true, y_pred, average="binary", zero_division=0)),
        "macro_f1": float(f1_score(y_true, y_pred, average="macro", zero_division=0)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "accuracy": float(accuracy_score(y_true, y_pred)),
    }

    benign_probs = y_prob[y_true == 0]
    jb_probs = y_prob[y_true == 1]
    if len(jb_probs) > 0 and len(benign_probs) > 0:
        thresholds = np.sort(jb_probs)
        idx = max(0, int(np.floor(len(thresholds) * 0.05)) - 1)
        threshold_at_95tpr = thresholds[idx]
        metrics["fpr_at_95tpr"] = float((benign_probs >= threshold_at_95tpr).mean())

    return metrics


def evaluate_dataset(convs, tokenizer, encoder, gru, dataset_name, variant_name, seed):
    y_true, y_pred, y_prob = embed_and_predict(convs, tokenizer, encoder, gru)
    metrics = compute_metrics(y_true, y_pred, y_prob)
    raw = {
        "y_true": y_true.tolist(),
        "y_pred": y_pred.tolist(),
        "y_prob": y_prob.tolist(),
    }
    print(f"  {dataset_name} seed{seed}: macro_f1={metrics['macro_f1']:.4f} binary_f1={metrics['binary_f1']:.4f} "
          f"prec={metrics['precision']:.4f} rec={metrics['recall']:.4f}")
    return metrics, raw


def main():
    tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL)

    # Load datasets
    toxicchat_convs = load_conversations(PROJ / "data/mhj/toxicchat_eval.jsonl")
    verazuo_convs = load_conversations(PROJ / "data/mhj/human_jailbreak_eval.jsonl")

    n_tc_jb = sum(c["label"] for c in toxicchat_convs)
    n_tc_bn = len(toxicchat_convs) - n_tc_jb
    n_vz_jb = sum(c["label"] for c in verazuo_convs)
    n_vz_bn = len(verazuo_convs) - n_vz_jb
    print(f"ToxicChat: {len(toxicchat_convs)} ({n_tc_jb} jb, {n_tc_bn} bn)")
    print(f"Verazuo: {len(verazuo_convs)} ({n_vz_jb} jb, {n_vz_bn} bn)")

    # Build verazuo test-only-benign subset (leakage check)
    # Reload from source to identify which benign are from test vs train
    test_benign_ids = set()
    with open(PROJ / "data/plan_002_splits/test.jsonl") as f:
        for line in f:
            conv = json.loads(line.strip())
            if conv["label"] == "benign":
                user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
                if user_turns:
                    test_benign_ids.add(user_turns[0][:200])

    verazuo_test_only = []
    verazuo_leakage_info = {"from_test": 0, "from_train": 0}
    for conv in verazuo_convs:
        if conv["label"] == 1:
            verazuo_test_only.append(conv)
        else:
            first_turn = conv["turns"][0] if conv["turns"] else ""
            if first_turn[:200] in test_benign_ids:
                verazuo_test_only.append(conv)
                verazuo_leakage_info["from_test"] += 1
            else:
                verazuo_leakage_info["from_train"] += 1

    n_vz_to_jb = sum(c["label"] for c in verazuo_test_only)
    n_vz_to_bn = len(verazuo_test_only) - n_vz_to_jb
    print(f"\nVerazuo leakage analysis:")
    print(f"  Benign from test split: {verazuo_leakage_info['from_test']}")
    print(f"  Benign from train split (LEAKED): {verazuo_leakage_info['from_train']}")
    print(f"  Verazuo test-only-benign subset: {len(verazuo_test_only)} ({n_vz_to_jb} jb, {n_vz_to_bn} bn)")

    results = {
        "metadata": {
            "description": "Exp8 F1 correction: recomputed with both binary and macro F1",
            "toxicchat": {"n_jailbreak": n_tc_jb, "n_benign": n_tc_bn, "source": "ToxicChat (LMSYS)"},
            "verazuo": {"n_jailbreak": n_vz_jb, "n_benign": n_vz_bn, "source": "verazuo/jailbreak_llms"},
            "verazuo_test_only_benign": {
                "n_jailbreak": n_vz_to_jb, "n_benign": n_vz_to_bn,
                "note": "Only benign from plan_002 test split (no leakage)"
            },
            "leakage_analysis": verazuo_leakage_info,
        },
        "toxicchat": {},
        "verazuo": {},
        "verazuo_test_only_benign": {},
        "raw_predictions": {},
    }

    variants_to_eval = ["vanilla", "9class", "binary", "scrambled", "jb_mlm", "wiki_mlm", "topic"]

    for variant_name in variants_to_eval:
        variant_cfg = MODEL_CONFIGS[variant_name]
        print(f"\n{'='*60}")
        print(f"Evaluating: {variant_name}")
        print(f"{'='*60}")

        tc_seed_results = {}
        vz_seed_results = {}
        vz_to_seed_results = {}
        raw_preds = {}

        for seed, seed_cfg in variant_cfg["seeds"].items():
            gru_path = seed_cfg["gru"]
            if not Path(gru_path).exists():
                print(f"  GRU not found: {gru_path}, skipping seed {seed}")
                continue
            if variant_cfg["encoder_type"] != "vanilla":
                deb_path = seed_cfg["deberta"]
                if variant_cfg["encoder_type"] == "hf_local":
                    if not Path(deb_path / "config.json").exists():
                        print(f"  DeBERTa not found: {deb_path}, skipping seed {seed}")
                        continue
                else:
                    if not Path(deb_path / "model.pt").exists():
                        print(f"  DeBERTa not found: {deb_path}, skipping seed {seed}")
                        continue

            print(f"\n  Seed {seed}:")
            encoder = load_encoder(variant_cfg, seed_cfg)
            embed_dim = encoder.config.hidden_size
            gru = GRUClassifier(input_dim=embed_dim, hidden_dim=256, num_layers=2, dropout=0.3)
            gru.load_state_dict(torch.load(gru_path, map_location="cpu", weights_only=True))
            gru = gru.to(DEVICE).eval()

            tc_metrics, tc_raw = evaluate_dataset(
                toxicchat_convs, tokenizer, encoder, gru, "ToxicChat", variant_name, seed)
            vz_metrics, vz_raw = evaluate_dataset(
                verazuo_convs, tokenizer, encoder, gru, "Verazuo", variant_name, seed)
            vz_to_metrics, vz_to_raw = evaluate_dataset(
                verazuo_test_only, tokenizer, encoder, gru, "Verazuo(test-bn)", variant_name, seed)

            tc_seed_results[str(seed)] = tc_metrics
            vz_seed_results[str(seed)] = vz_metrics
            vz_to_seed_results[str(seed)] = vz_to_metrics
            raw_preds[str(seed)] = {
                "toxicchat": tc_raw,
                "verazuo": vz_raw,
                "verazuo_test_only_benign": vz_to_raw,
            }

            del encoder, gru
            torch.cuda.empty_cache()

        def aggregate(seed_results):
            if not seed_results:
                return {}
            metric_lists = defaultdict(list)
            for s, m in seed_results.items():
                for k, v in m.items():
                    metric_lists[k].append(v)
            agg = {}
            for k, vals in metric_lists.items():
                agg[f"{k}_mean"] = float(np.mean(vals))
                agg[f"{k}_std"] = float(np.std(vals))
            agg["n_seeds"] = len(seed_results)
            return agg

        results["toxicchat"][variant_name] = {
            "per_seed": tc_seed_results, "average": aggregate(tc_seed_results),
            "seeds_used": list(tc_seed_results.keys()),
        }
        results["verazuo"][variant_name] = {
            "per_seed": vz_seed_results, "average": aggregate(vz_seed_results),
            "seeds_used": list(vz_seed_results.keys()),
        }
        results["verazuo_test_only_benign"][variant_name] = {
            "per_seed": vz_to_seed_results, "average": aggregate(vz_to_seed_results),
            "seeds_used": list(vz_to_seed_results.keys()),
        }
        results["raw_predictions"][variant_name] = raw_preds

    # Summary tables
    print(f"\n{'='*90}")
    print(f"{'SUMMARY: Macro F1 (corrected) vs Binary F1 (original)':^90}")
    print(f"{'='*90}")

    for dataset_key, dataset_label in [
        ("toxicchat", "ToxicChat"),
        ("verazuo", "Verazuo (all benign)"),
        ("verazuo_test_only_benign", "Verazuo (test-only benign, no leakage)"),
    ]:
        print(f"\n--- {dataset_label} ---")
        print(f"{'Variant':<12} {'Seeds':<6} {'Macro F1':<20} {'Binary F1':<20} {'Accuracy':<20}")
        print("-" * 80)
        for vn in variants_to_eval:
            r = results[dataset_key].get(vn, {})
            avg = r.get("average", {})
            ns = avg.get("n_seeds", 0)
            if ns == 0:
                print(f"{vn:<12} {'N/A':<6}")
                continue
            mf1 = f"{avg.get('macro_f1_mean', 0):.4f}+/-{avg.get('macro_f1_std', 0):.4f}"
            bf1 = f"{avg.get('binary_f1_mean', 0):.4f}+/-{avg.get('binary_f1_std', 0):.4f}"
            acc = f"{avg.get('accuracy_mean', 0):.4f}+/-{avg.get('accuracy_std', 0):.4f}"
            print(f"{vn:<12} {ns:<6} {mf1:<20} {bf1:<20} {acc:<20}")

    # Save results (without raw predictions in main file to keep it small)
    results_no_raw = {k: v for k, v in results.items() if k != "raw_predictions"}
    out_path = PROJ / "results/exp8_macro_f1_corrected.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results_no_raw, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Save raw predictions separately
    raw_path = PROJ / "results/exp8_raw_predictions.json"
    with open(raw_path, "w") as f:
        json.dump(results["raw_predictions"], f, indent=2)
    print(f"Raw predictions saved to {raw_path}")


if __name__ == "__main__":
    main()
