"""Exp20: DeepContext Proxy Baseline — BERT-base-uncased + BiGRU (frozen probing, no DAPT).

Replaces DeBERTa-v3-base encoder with BERT-base-uncased to quantify DAPT contribution.
Same frozen probing pipeline: freeze encoder, extract [CLS], train BiGRU classifier.
3 seeds (42, 123, 456), evaluated on IID test + DD OOD + AA OOD.
"""
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

import sys
import json
import random
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer, AutoModel

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
CKPT_ROOT = PROJ / "checkpoints"
DATA_ROOT = PROJ / "data"

BERT_MODEL = "/root/.cache/modelscope_bert/AI-ModelScope/bert-base-uncased"

MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
GRU_LR = 1e-3
GRU_EPOCHS = 20
GRU_BATCH = 32
PATIENCE = 3
SEEDS = [42, 123, 456]


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


# ==================== Embedding ====================

def embed_turns(encoder, tokenizer, turns, device):
    if len(turns) == 0:
        turns = [""]
    enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(device)
    with torch.no_grad():
        out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        return out.last_hidden_state[:, 0, :]


def precompute_conv_embeddings(encoder, tokenizer, convs, device):
    all_embs, all_labels, all_lengths = [], [], []
    for c in convs:
        turns = extract_user_turns(c)
        embs = embed_turns(encoder, tokenizer, turns, device)
        all_embs.append(embs.cpu())
        all_labels.append(get_label(c))
        all_lengths.append(embs.size(0))
    return all_embs, all_labels, all_lengths


def pad_embeddings(embs_list, labels, lengths):
    max_len = max(lengths)
    dim = embs_list[0].size(1)
    padded = torch.zeros(len(embs_list), max_len, dim)
    for i, e in enumerate(embs_list):
        padded[i, :e.size(0), :] = e
    return padded, torch.tensor(labels, dtype=torch.long), torch.tensor(lengths, dtype=torch.long)


# ==================== GRU Training ====================

def train_gru(train_embs, train_labels, train_lengths,
              val_embs, val_labels, val_lengths,
              save_dir, seed, embed_dim, device):
    set_seed(seed)
    tr_padded, tr_labels, tr_lens = pad_embeddings(train_embs, train_labels, train_lengths)
    vl_padded, vl_labels, vl_lens = pad_embeddings(val_embs, val_labels, val_lengths)

    model = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT)
    model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=GRU_LR)
    criterion = nn.CrossEntropyLoss()

    best_val_f1 = 0.0
    patience_counter = 0
    save_dir = Path(save_dir)
    save_dir.mkdir(parents=True, exist_ok=True)

    for epoch in range(GRU_EPOCHS):
        model.train()
        indices = torch.randperm(tr_padded.size(0))
        epoch_loss, steps = 0.0, 0
        for start in range(0, tr_padded.size(0), GRU_BATCH):
            idx = indices[start:start + GRU_BATCH]
            embs = tr_padded[idx].to(device)
            lens = tr_lens[idx].to(device)
            labs = tr_labels[idx].to(device)
            logits = model(embs, lens)
            loss = criterion(logits, labs)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            steps += 1

        model.eval()
        all_preds, all_labels_v = [], []
        with torch.no_grad():
            for start in range(0, vl_padded.size(0), GRU_BATCH):
                embs = vl_padded[start:start + GRU_BATCH].to(device)
                lens = vl_lens[start:start + GRU_BATCH].to(device)
                logits = model(embs, lens)
                all_preds.extend(logits.argmax(-1).cpu().tolist())
                all_labels_v.extend(vl_labels[start:start + GRU_BATCH].tolist())

        val_f1 = f1_score(all_labels_v, all_preds, average="macro")
        improved = val_f1 > best_val_f1
        if improved:
            best_val_f1 = val_f1
            torch.save(model.state_dict(), save_dir / "best.pt")
            patience_counter = 0
        else:
            patience_counter += 1

        if (epoch + 1) % 5 == 0 or improved:
            print(f"      Epoch {epoch+1}/{GRU_EPOCHS} | Loss: {epoch_loss/max(steps,1):.4f} | Val F1: {val_f1:.4f} (best={best_val_f1:.4f})")

        if patience_counter >= PATIENCE:
            print(f"      Early stopping at epoch {epoch+1} (patience={PATIENCE})")
            break

    print(f"      GRU done, best val F1={best_val_f1:.4f}")
    model.load_state_dict(torch.load(save_dir / "best.pt", map_location="cpu"))
    model.to(device)
    model.eval()
    return model


# ==================== Evaluation ====================

def eval_set(encoder, gru, tokenizer, convs, device):
    gru.eval()
    all_preds, all_labels = [], []
    for c in convs:
        turns = extract_user_turns(c) if "turns" in c and isinstance(c["turns"][0], dict) else c["turns"]
        embs = embed_turns(encoder, tokenizer, turns, device)
        embs_padded = embs.unsqueeze(0)
        lengths = torch.tensor([embs.size(0)], dtype=torch.long).to(device)
        with torch.no_grad():
            logits = gru(embs_padded, lengths)
            pred = logits.argmax(dim=1).item()
        all_preds.append(pred)
        label = c["label"] if isinstance(c["label"], int) else get_label(c)
        all_labels.append(label)
    return float(f1_score(all_labels, all_preds, average="macro"))


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


def eval_ood(encoder, gru, tokenizer, conversations, device):
    gru.eval()
    all_preds, all_labels = [], []
    for conv in conversations:
        turns = conv["turns"]
        if len(turns) == 0:
            turns = [""]
        enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(device)
        with torch.no_grad():
            out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
            lengths = torch.tensor([len(turns)], dtype=torch.long).to(device)
            logits = gru(embs, lengths)
        pred = logits.argmax(-1).item()
        all_preds.append(pred)
        all_labels.append(conv["label"])
    return float(f1_score(all_labels, all_preds, average="macro"))


# ==================== Main ====================

def main():
    device = torch.device("cuda:0")

    print("=" * 60)
    print("Exp20: DeepContext Proxy — BERT-base-uncased + BiGRU")
    print("=" * 60)

    tokenizer = AutoTokenizer.from_pretrained(BERT_MODEL)
    encoder = AutoModel.from_pretrained(BERT_MODEL)
    encoder.to(device)
    encoder.eval()
    for p in encoder.parameters():
        p.requires_grad = False
    embed_dim = encoder.config.hidden_size
    print(f"Encoder: {BERT_MODEL}, hidden_size={embed_dim}")

    # Load data
    train_data = load_jsonl(DATA_ROOT / "plan_002_splits/train.jsonl")
    val_data = load_jsonl(DATA_ROOT / "plan_002_splits/val.jsonl")
    test_data = load_jsonl(DATA_ROOT / "plan_002_splits/test.jsonl")
    dd_convs = load_ood_data(
        DATA_ROOT / "generated/deceptive_delight_all.jsonl",
        DATA_ROOT / "plan_002_splits/test.jsonl"
    )
    aa_convs = load_ood_data(
        DATA_ROOT / "actorattack_ood/actorattack_all.jsonl",
        DATA_ROOT / "plan_002_splits/test.jsonl"
    )

    n_dd_jb = sum(1 for c in dd_convs if c["label"] == 1)
    n_aa_jb = sum(1 for c in aa_convs if c["label"] == 1)
    print(f"Train: {len(train_data)}, Val: {len(val_data)}, IID Test: {len(test_data)}")
    print(f"DD OOD: {n_dd_jb} attack + {len(dd_convs)-n_dd_jb} benign = {len(dd_convs)}")
    print(f"AA OOD: {n_aa_jb} attack + {len(aa_convs)-n_aa_jb} benign = {len(aa_convs)}")

    # Precompute embeddings (shared across seeds since encoder is frozen)
    print("\nPrecomputing train embeddings...")
    train_embs, train_labels, train_lengths = precompute_conv_embeddings(encoder, tokenizer, train_data, device)
    print("Precomputing val embeddings...")
    val_embs, val_labels, val_lengths = precompute_conv_embeddings(encoder, tokenizer, val_data, device)

    results = {}
    for seed in SEEDS:
        print(f"\n{'='*40} Seed {seed} {'='*40}")
        gru_save_dir = CKPT_ROOT / f"exp20_bert_base_seed{seed}"

        gru = train_gru(
            train_embs, train_labels, train_lengths,
            val_embs, val_labels, val_lengths,
            gru_save_dir, seed, embed_dim, device
        )

        iid_f1 = eval_set(encoder, gru, tokenizer, test_data, device)
        dd_f1 = eval_ood(encoder, gru, tokenizer, dd_convs, device)
        aa_f1 = eval_ood(encoder, gru, tokenizer, aa_convs, device)

        results[seed] = {"IID": iid_f1, "DD_OOD": dd_f1, "AA_OOD": aa_f1}
        print(f"  seed{seed}: IID={iid_f1:.4f}  DD_OOD={dd_f1:.4f}  AA_OOD={aa_f1:.4f}")

        del gru
        torch.cuda.empty_cache()

    # Summary
    print("\n" + "=" * 60)
    print("exp20 DeepContext Proxy (BERT-base + BiGRU) Results:")
    print("=" * 60)

    print("\nBERT-base (no DAPT):")
    for seed in SEEDS:
        r = results[seed]
        print(f"  seed{seed}:  IID={r['IID']:.3f}  DD_OOD={r['DD_OOD']:.3f}  AA_OOD={r['AA_OOD']:.3f}")

    iid_vals = [results[s]["IID"] for s in SEEDS]
    dd_vals = [results[s]["DD_OOD"] for s in SEEDS]
    aa_vals = [results[s]["AA_OOD"] for s in SEEDS]
    print(f"  mean:    IID={np.mean(iid_vals):.3f}±{np.std(iid_vals):.3f}  "
          f"DD_OOD={np.mean(dd_vals):.3f}±{np.std(dd_vals):.3f}  "
          f"AA_OOD={np.mean(aa_vals):.3f}±{np.std(aa_vals):.3f}")

    print("\n对比 DeBERTa-v3 (exp1):")
    print(f"  BERT-base (no DAPT):    IID={np.mean(iid_vals):.3f}±{np.std(iid_vals):.3f}  "
          f"DD_OOD={np.mean(dd_vals):.3f}±{np.std(dd_vals):.3f}  "
          f"AA_OOD={np.mean(aa_vals):.3f}±{np.std(aa_vals):.3f}")
    print(f"  DeBERTa vanilla:        IID=1.000±0.000  DD_OOD=0.312±0.043  AA_OOD=???")
    print(f"  DeBERTa 9-class:        IID=1.000±0.000  DD_OOD=0.994±0.005  AA_OOD=0.939±0.047")

    # Save results
    out_path = PROJ / "results" / "exp20_deepcontext_proxy.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump({
            "experiment": "exp20_deepcontext_proxy",
            "encoder": BERT_MODEL,
            "method": "frozen_probing_bigru",
            "seeds": SEEDS,
            "per_seed": {str(s): results[s] for s in SEEDS},
            "mean_std": {
                "IID": {"mean": float(np.mean(iid_vals)), "std": float(np.std(iid_vals))},
                "DD_OOD": {"mean": float(np.mean(dd_vals)), "std": float(np.std(dd_vals))},
                "AA_OOD": {"mean": float(np.mean(aa_vals)), "std": float(np.std(aa_vals))},
            }
        }, f, indent=2)
    print(f"\nResults saved to {out_path}")
    print("Done.")


if __name__ == "__main__":
    main()
