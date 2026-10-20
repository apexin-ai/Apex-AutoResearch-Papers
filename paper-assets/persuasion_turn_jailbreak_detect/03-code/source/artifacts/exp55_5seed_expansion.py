#!/usr/bin/env python3
"""exp55: 5-seed expansion for MLM vs 9-class comparison on ActorAttack OOD.

Adds seeds 789 and 1024 to existing 42/123/456 results.
Reviewer W2 flagged the 3-seed comparison as insufficient.

Usage (all 4 pipelines):
  source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
  cd /root/persuasion_turn_jailbreak_detect && \
  CUDA_VISIBLE_DEVICES=1 python scripts/exp55_5seed_expansion.py

Single pipeline:
  CUDA_VISIBLE_DEVICES=1 python scripts/exp55_5seed_expansion.py --variant 9class --seed 789
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys, json, random, time, subprocess, argparse
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer, AutoModel

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
CKPT_BASE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints")
MODEL_NAME = "microsoft/deberta-v3-base"
DEVICE = torch.device("cuda:0")
MAX_LENGTH = 256

DEBERTA_LR = 2e-5
DEBERTA_BATCH = 16
DEBERTA_EPOCHS = 4
ALPHA = 0.3

GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
GRU_LR = 1e-3
GRU_EPOCHS = 20
GRU_BATCH = 32


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def run_stage1_9class(name, seed):
    ckpt_dir = CKPT_BASE / f"exp55_{name}" / "deberta_multitask"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    best_path = ckpt_dir / "best"
    if (best_path / "model.pt").exists():
        print(f"Stage 1 checkpoint already exists: {best_path}", flush=True)
        return best_path

    cmd = [
        sys.executable, str(PROJ / "src/train_deberta.py"),
        "--train_data", str(PROJ / "data/plan_002_splits/train.jsonl"),
        "--val_data", str(PROJ / "data/plan_002_splits/val.jsonl"),
        "--model_name", MODEL_NAME,
        "--output_dir", str(ckpt_dir),
        "--epochs", str(DEBERTA_EPOCHS),
        "--batch_size", str(DEBERTA_BATCH),
        "--lr", str(DEBERTA_LR),
        "--max_length", str(MAX_LENGTH),
        "--seed", str(seed),
        "--alpha", str(ALPHA),
    ]

    print(f"\n{'='*70}", flush=True)
    print(f"STAGE 1: DeBERTa 9-class - {name}", flush=True)
    print(f"{'='*70}", flush=True)
    print(f"Command: {' '.join(cmd)}", flush=True)

    t0 = time.time()
    result = subprocess.run(cmd, text=True)
    elapsed = time.time() - t0
    print(f"Stage 1 completed in {elapsed/60:.1f} min (exit code: {result.returncode})", flush=True)

    if result.returncode != 0:
        raise RuntimeError(f"Stage 1 failed for {name}")

    assert (best_path / "model.pt").exists(), f"Checkpoint not found: {best_path / 'model.pt'}"
    return best_path


def run_stage1_mlm(name, seed):
    ckpt_dir = CKPT_BASE / f"exp55_{name}" / "deberta_mlm"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    best_path = ckpt_dir / "best"
    if (best_path / "config.json").exists():
        print(f"Stage 1 MLM checkpoint already exists: {best_path}", flush=True)
        return best_path

    cmd = [
        sys.executable, str(PROJ / "src/train_deberta_mlm.py"),
        "--train_data", str(PROJ / "data/plan_002_splits/train.jsonl"),
        "--val_data", str(PROJ / "data/plan_002_splits/val.jsonl"),
        "--model_name", MODEL_NAME,
        "--output_dir", str(ckpt_dir),
        "--epochs", str(DEBERTA_EPOCHS),
        "--batch_size", str(DEBERTA_BATCH),
        "--lr", str(DEBERTA_LR),
        "--max_length", str(MAX_LENGTH),
        "--seed", str(seed),
    ]

    print(f"\n{'='*70}", flush=True)
    print(f"STAGE 1: DeBERTa MLM - {name}", flush=True)
    print(f"{'='*70}", flush=True)
    print(f"Command: {' '.join(cmd)}", flush=True)

    t0 = time.time()
    result = subprocess.run(cmd, text=True)
    elapsed = time.time() - t0
    print(f"Stage 1 completed in {elapsed/60:.1f} min (exit code: {result.returncode})", flush=True)

    if result.returncode != 0:
        raise RuntimeError(f"Stage 1 MLM failed for {name}")

    assert (best_path / "config.json").exists(), f"MLM checkpoint not found: {best_path}"
    return best_path


def load_encoder_9class(ckpt_path):
    model = DeBERTaMultiTask(model_name=MODEL_NAME, num_persuasion_classes=9)
    state = torch.load(ckpt_path / "model.pt", map_location="cpu")
    model.load_state_dict(state)
    encoder = model.deberta.to(DEVICE).float().eval()
    for p in encoder.parameters():
        p.requires_grad = False
    del model
    torch.cuda.empty_cache()
    return encoder


def load_encoder_mlm(ckpt_path):
    encoder = AutoModel.from_pretrained(str(ckpt_path), torch_dtype=torch.float32)
    encoder.eval()
    for p in encoder.parameters():
        p.requires_grad = False
    return encoder.to(DEVICE)


def run_stage2_and_eval(name, seed, variant, encoder):
    set_seed(seed)

    gru_dir = CKPT_BASE / f"exp55_{name}" / "gru"
    gru_dir.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    embed_dim = encoder.config.hidden_size

    train_data = load_jsonl(PROJ / "data/plan_002_splits/train.jsonl")
    val_data = load_jsonl(PROJ / "data/plan_002_splits/val.jsonl")
    test_data = load_jsonl(PROJ / "data/plan_002_splits/test.jsonl")

    def embed_dataset(data, desc=""):
        all_embs, all_labels, all_lengths = [], [], []
        for i, conv in enumerate(data):
            turns = extract_user_turns(conv)
            if not turns:
                turns = [""]
            enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(DEVICE)
            with torch.no_grad():
                out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
                embs = out.last_hidden_state[:, 0, :].cpu().float()
            all_embs.append(embs)
            all_labels.append(get_label(conv))
            all_lengths.append(embs.size(0))
            if (i + 1) % 200 == 0:
                print(f"  {desc}: {i+1}/{len(data)}", flush=True)
        return all_embs, all_labels, all_lengths

    print("Precomputing train embeddings...", flush=True)
    train_embs, train_labels, train_lengths = embed_dataset(train_data, "train")
    print("Precomputing val embeddings...", flush=True)
    val_embs, val_labels, val_lengths = embed_dataset(val_data, "val")
    print("Precomputing test embeddings...", flush=True)
    test_embs, test_labels, test_lengths = embed_dataset(test_data, "test")

    class PrecomputedDataset(torch.utils.data.Dataset):
        def __init__(self, embeddings, labels, lengths):
            self.embeddings = embeddings
            self.labels = labels
            self.lengths = lengths
        def __len__(self):
            return len(self.labels)
        def __getitem__(self, idx):
            return {"embeddings": self.embeddings[idx], "label": self.labels[idx], "length": self.lengths[idx]}

    def collator(batch):
        max_t = max(b["length"] for b in batch)
        padded = torch.zeros(len(batch), max_t, embed_dim)
        lengths, labels = [], []
        for i, b in enumerate(batch):
            padded[i, :b["length"], :] = b["embeddings"]
            lengths.append(b["length"])
            labels.append(b["label"])
        return {"embeddings": padded, "lengths": torch.tensor(lengths), "labels": torch.tensor(labels)}

    train_loader = torch.utils.data.DataLoader(
        PrecomputedDataset(train_embs, train_labels, train_lengths),
        batch_size=GRU_BATCH, shuffle=True, collate_fn=collator
    )
    val_loader = torch.utils.data.DataLoader(
        PrecomputedDataset(val_embs, val_labels, val_lengths),
        batch_size=GRU_BATCH, shuffle=False, collate_fn=collator
    )

    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT).to(DEVICE)
    optimizer = torch.optim.Adam(gru.parameters(), lr=GRU_LR)
    criterion = nn.CrossEntropyLoss()

    best_val_f1 = 0.0

    print(f"\n--- GRU Training ({name}) ---", flush=True)
    for epoch in range(GRU_EPOCHS):
        gru.train()
        for batch in train_loader:
            embs = batch["embeddings"].to(DEVICE)
            lengths = batch["lengths"].to(DEVICE)
            labels = batch["labels"].to(DEVICE)
            logits = gru(embs, lengths)
            loss = criterion(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        gru.eval()
        all_preds, all_labels_list = [], []
        with torch.no_grad():
            for batch in val_loader:
                embs = batch["embeddings"].to(DEVICE)
                lengths = batch["lengths"].to(DEVICE)
                logits = gru(embs, lengths)
                all_preds.extend(logits.argmax(-1).cpu().tolist())
                all_labels_list.extend(batch["labels"].tolist())
        val_f1 = f1_score(all_labels_list, all_preds, average="macro")

        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            torch.save(gru.state_dict(), gru_dir / "best.pt")

        if (epoch + 1) % 5 == 0:
            print(f"  Epoch {epoch+1}/{GRU_EPOCHS} val_f1={val_f1:.4f} (best={best_val_f1:.4f})", flush=True)

    gru.load_state_dict(torch.load(gru_dir / "best.pt", map_location="cpu"))
    gru.to(DEVICE).eval()
    print(f"  Best GRU val_f1={best_val_f1:.4f}", flush=True)

    def predict_conv(turns, k=None):
        if k is not None:
            turns = turns[:k]
        if not turns:
            return 0
        enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
            lengths = torch.tensor([len(turns)], dtype=torch.long)
            logits = gru(embs.to(DEVICE), lengths.to(DEVICE))
            probs = torch.softmax(logits, dim=-1).cpu().numpy()[0]
        return int(probs[1] > 0.5)

    def eval_set(data, k=None):
        y_true, y_pred = [], []
        for conv in data:
            turns = extract_user_turns(conv)
            pred = predict_conv(turns, k=k)
            y_true.append(get_label(conv))
            y_pred.append(pred)
        return {"f1_macro": round(f1_score(y_true, y_pred, average="macro"), 4)}

    print(f"\n{'='*70}", flush=True)
    print(f"EVALUATION - {name}", flush=True)
    print(f"{'='*70}", flush=True)

    results = {"variant": variant, "seed": seed, "gru_best_val_f1": round(best_val_f1, 4)}
    benign_test = [c for c in test_data if c["label"] == "benign"]

    r = eval_set(test_data)
    results["iid"] = r["f1_macro"]
    print(f"  IID: F1={r['f1_macro']:.4f}", flush=True)

    dd_data = load_jsonl(PROJ / "data/generated/deceptive_delight_all.jsonl")
    dd_test = dd_data + benign_test
    r = eval_set(dd_test)
    results["dd_ood"] = r["f1_macro"]
    print(f"  DD OOD: F1={r['f1_macro']:.4f}", flush=True)

    aa_data = load_jsonl(PROJ / "data/generated/actorattack_all.jsonl")
    aa_test = aa_data + benign_test
    r = eval_set(aa_test)
    results["aa_ood"] = r["f1_macro"]
    print(f"  AA OOD: F1={r['f1_macro']:.4f}", flush=True)

    fitd_data = load_jsonl(PROJ / "data/generated/fitd_all.jsonl")
    fitd_test = fitd_data + benign_test
    r = eval_set(fitd_test)
    results["fitd_ood"] = r["f1_macro"]
    print(f"  FITD OOD: F1={r['f1_macro']:.4f}", flush=True)

    del gru
    torch.cuda.empty_cache()

    return results


def run_pipeline(variant, seed):
    name = f"{variant}_seed{seed}"

    print(f"\n\n{'#'*70}", flush=True)
    print(f"# {name}", flush=True)
    print(f"{'#'*70}", flush=True)

    group_start = time.time()

    if variant == "9class":
        ckpt_path = run_stage1_9class(name, seed)
        encoder = load_encoder_9class(ckpt_path)
    else:
        ckpt_path = run_stage1_mlm(name, seed)
        encoder = load_encoder_mlm(ckpt_path)

    results = run_stage2_and_eval(name, seed, variant, encoder)

    del encoder
    torch.cuda.empty_cache()

    elapsed = time.time() - group_start
    print(f"\n{name} done in {elapsed/60:.1f} min", flush=True)
    print(f"  IID={results['iid']}, DD={results['dd_ood']}, AA={results['aa_ood']}, FITD={results['fitd_ood']}", flush=True)

    result_path = PROJ / "results" / f"exp55_seed{seed}_{variant}.json"
    result_path.parent.mkdir(parents=True, exist_ok=True)
    with open(result_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"  Saved to {result_path}", flush=True)

    return results


def parse_args():
    parser = argparse.ArgumentParser(description="exp55: 5-seed MLM vs 9-class expansion")
    parser.add_argument("--variant", type=str, choices=["9class", "mlm"], default=None)
    parser.add_argument("--seed", type=int, default=None)
    parser.add_argument("--device", type=str, default="cuda:0")
    return parser.parse_args()


def main():
    global DEVICE
    args = parse_args()
    DEVICE = torch.device(args.device)

    start_time = time.time()
    all_results = {}

    if args.variant and args.seed:
        results = run_pipeline(args.variant, args.seed)
        all_results[f"{args.variant}_seed{args.seed}"] = results
    else:
        configs = [
            ("9class", 789),
            ("9class", 1024),
            ("mlm", 789),
            ("mlm", 1024),
        ]
        for variant, seed in configs:
            results = run_pipeline(variant, seed)
            all_results[f"{variant}_seed{seed}"] = results

            interim_path = PROJ / "results" / "exp55_5seed_expansion.json"
            with open(interim_path, "w") as f:
                json.dump(all_results, f, indent=2)

    total = time.time() - start_time
    print(f"\n\n{'='*70}", flush=True)
    print(f"ALL DONE in {total/60:.1f} min", flush=True)
    print(f"{'='*70}", flush=True)
    for name, r in all_results.items():
        print(f"  {name}: IID={r['iid']}, DD={r['dd_ood']}, AA={r['aa_ood']}, FITD={r['fitd_ood']}", flush=True)

    final_path = PROJ / "results" / "exp55_5seed_expansion.json"
    with open(final_path, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nFinal results: {final_path}", flush=True)


if __name__ == "__main__":
    main()
