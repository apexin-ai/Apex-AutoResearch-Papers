"""Turn-shuffle ablation: test whether detection depends on turn order.

Shuffles turn embeddings (after DeBERTa encoding, before BiGRU) and compares
macro F1 of original vs shuffled on IID test, DD OOD, AA OOD.

Uses exp15 (RoBERTa-large) checkpoints: 3 seeds × 2 variants (9-class, vanilla).
"""
import os
os.environ["HF_HOME"] = "/root/autodl-tmp/hf_cache"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["WANDB_MODE"] = "disabled"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import json
import random
import numpy as np
import torch
import sys
from pathlib import Path
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.gru_classifier import GRUClassifier
from src.models.deberta_multitask import DeBERTaMultiTask
from transformers import AutoTokenizer, AutoModel

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
ROBERTA_LARGE = "/root/autodl-tmp/roberta-large-local"
CKPT_ROOT = PROJ / "checkpoints"
MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
SEEDS = [42, 123, 456]
SHUFFLE_SEEDS = [0, 1, 2]


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def load_ood_data(ood_path, benign_test_path):
    conversations = []
    with open(ood_path) as f:
        for line in f:
            conv = json.loads(line.strip())
            user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
            conversations.append({"turns": user_turns, "label": 1})
    with open(benign_test_path) as f:
        for line in f:
            conv = json.loads(line.strip())
            if conv["label"] == "benign":
                user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
                conversations.append({"turns": user_turns, "label": 0})
    return conversations


def load_iid_test(test_path):
    conversations = []
    for conv in load_jsonl(test_path):
        user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
        label = 1 if conv["label"] == "jailbreak" else 0
        conversations.append({"turns": user_turns, "label": label})
    return conversations


def eval_with_shuffle(encoder, gru, tokenizer, conversations, device, shuffle_seed=None):
    all_preds, all_labels = [], []
    if shuffle_seed is not None:
        rng = torch.Generator()
        rng.manual_seed(shuffle_seed)

    for conv in conversations:
        turns = conv["turns"]
        if len(turns) == 0:
            turns = [""]
        enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(device)
        with torch.no_grad():
            out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].unsqueeze(0)  # (1, num_turns, dim)

            if shuffle_seed is not None and embs.size(1) > 1:
                perm = torch.randperm(embs.size(1), generator=rng)
                embs = embs[:, perm, :]

            lengths = torch.tensor([len(turns)], dtype=torch.long).to(device)
            logits = gru(embs, lengths)
        pred = logits.argmax(-1).item()
        all_preds.append(pred)
        all_labels.append(conv["label"])
    return float(f1_score(all_labels, all_preds, average="macro"))


def load_models(variant, seed, device):
    tokenizer = AutoTokenizer.from_pretrained(ROBERTA_LARGE)

    if variant == "9class":
        model = DeBERTaMultiTask(model_name=ROBERTA_LARGE, num_persuasion_classes=9)
        state_dict = torch.load(
            CKPT_ROOT / f"exp15_roberta_large_9class_seed{seed}/deberta_multitask/best/model.pt",
            map_location="cpu"
        )
        model.load_state_dict(state_dict)
        encoder = model.deberta
        del model
        gru_path = CKPT_ROOT / f"exp15_roberta_large_9class_seed{seed}/gru/treatment/best.pt"
    else:
        encoder = AutoModel.from_pretrained(ROBERTA_LARGE, torch_dtype=torch.float32)
        gru_path = CKPT_ROOT / f"exp15_roberta_large_vanilla_seed{seed}/gru/best.pt"

    encoder.to(device).eval()
    for p in encoder.parameters():
        p.requires_grad = False

    embed_dim = encoder.config.hidden_size
    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT)
    gru.load_state_dict(torch.load(gru_path, map_location="cpu"))
    gru.to(device).eval()

    return encoder, gru, tokenizer


def main():
    device = torch.device("cuda:0")
    test_path = PROJ / "data/plan_002_splits/test.jsonl"

    iid_data = load_iid_test(test_path)
    dd_data = load_ood_data(PROJ / "data/generated/deceptive_delight_all.jsonl", test_path)
    aa_data = load_ood_data(PROJ / "data/generated/actorattack_all.jsonl", test_path)

    n_iid = len(iid_data)
    n_dd = len(dd_data)
    n_aa = len(aa_data)
    print(f"IID test: {n_iid} samples")
    print(f"DD OOD: {n_dd} samples ({sum(1 for c in dd_data if c['label']==1)} jb + {sum(1 for c in dd_data if c['label']==0)} bn)")
    print(f"AA OOD: {n_aa} samples ({sum(1 for c in aa_data if c['label']==1)} jb + {sum(1 for c in aa_data if c['label']==0)} bn)")

    datasets = {"IID": iid_data, "DD_OOD": dd_data, "AA_OOD": aa_data}
    results = {}

    for variant in ["9class", "vanilla"]:
        results[variant] = {}
        for ds_name in datasets:
            results[variant][ds_name] = {"original": [], "shuffled": []}

        for seed in SEEDS:
            print(f"\n--- {variant} seed={seed} ---")
            encoder, gru, tokenizer = load_models(variant, seed, device)

            for ds_name, ds_data in datasets.items():
                f1_orig = eval_with_shuffle(encoder, gru, tokenizer, ds_data, device, shuffle_seed=None)
                results[variant][ds_name]["original"].append(f1_orig)
                print(f"  {ds_name} original: {f1_orig:.4f}")

                for sh_seed in SHUFFLE_SEEDS:
                    f1_shuf = eval_with_shuffle(encoder, gru, tokenizer, ds_data, device, shuffle_seed=sh_seed)
                    results[variant][ds_name]["shuffled"].append(f1_shuf)
                    print(f"  {ds_name} shuffle(seed={sh_seed}): {f1_shuf:.4f}")

            del encoder, gru
            torch.cuda.empty_cache()

    print("\n" + "=" * 70)
    print("Turn-Shuffle Ablation Results:")
    print("=" * 70)

    for ds_name, n_samples in [("IID", n_iid), ("DD_OOD", n_dd), ("AA_OOD", n_aa)]:
        print(f"\n=== {ds_name} ({n_samples} samples) ===")
        for variant in ["9class", "vanilla"]:
            orig = results[variant][ds_name]["original"]
            shuf = results[variant][ds_name]["shuffled"]
            orig_mean = np.mean(orig)
            orig_std = np.std(orig)
            shuf_mean = np.mean(shuf)
            shuf_std = np.std(shuf)
            delta = shuf_mean - orig_mean
            print(f"{variant}:")
            print(f"  Original:  F1 = {orig_mean:.4f}±{orig_std:.4f} (seeds {'/'.join(str(s) for s in SEEDS)})")
            print(f"  Shuffled:  F1 = {shuf_mean:.4f}±{shuf_std:.4f} (3 model seeds × 3 shuffle seeds = 9 runs)")
            print(f"  Δ = {delta:+.4f} (shuffled - original)")

    out_path = PROJ / "results/turn_shuffle_ablation.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
