"""exp28: Data Efficiency — 9-class DAPT performance under different training set sizes.

Subsamples: {50, 125, 250, 350(full)} from plan_002 train.jsonl.
For each subset:
  Stage 1: Train DeBERTa 9-class DAPT (same hyperparams as plan_002)
  Stage 2: Train BiGRU classifier (frozen probing)
  Evaluate: IID, DD OOD, AA OOD (macro F1)

Also trains vanilla baseline at 125 and 350 samples for comparison.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/hf_cache"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import sys
import json
import random
from pathlib import Path
from collections import Counter

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from transformers import AutoTokenizer, AutoModel, get_linear_schedule_with_warmup
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.data.dataset import TurnDataset, ConversationDataset
from src.data.collator import TurnCollator
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier

PROJ = "/root/persuasion_turn_jailbreak_detect"
DATA_DIR = f"{PROJ}/data/plan_002_splits"
MODEL_NAME = "microsoft/deberta-v3-base"
TMP_DIR = "/root/autodl-tmp/exp28_tmp"
CKPT_DIR = "/root/autodl-tmp/exp28_checkpoints"

SUBSET_SIZES = [50, 125, 250, 350]
SEED = 42

DEBERTA_LR = 2e-5
DEBERTA_EPOCHS = 5
DEBERTA_BATCH_SIZE = 16
DEBERTA_MAX_LENGTH = 256
DEBERTA_ALPHA = 0.3
DEBERTA_WARMUP_RATIO = 0.1
DEBERTA_WEIGHT_DECAY = 0.01

GRU_LR = 1e-3
GRU_EPOCHS = 20
GRU_BATCH_SIZE = 32
GRU_HIDDEN_DIM = 256
GRU_NUM_LAYERS = 2
GRU_DROPOUT = 0.3


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line.strip()) for line in f]


def stratified_subsample(conversations, n, seed):
    rng = random.Random(seed)
    by_label = {}
    for c in conversations:
        by_label.setdefault(c["label"], []).append(c)

    sampled = []
    total = len(conversations)
    for label, convs in by_label.items():
        k = max(1, round(n * len(convs) / total))
        if k > len(convs):
            k = len(convs)
        sampled.extend(rng.sample(convs, k))

    while len(sampled) > n:
        sampled.pop()
    while len(sampled) < n and len(sampled) < total:
        remaining = [c for c in conversations if c not in sampled]
        if remaining:
            sampled.append(rng.choice(remaining))
        else:
            break

    rng.shuffle(sampled)
    return sampled


def write_jsonl(data, path):
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


# ============================================================
# Stage 1: DeBERTa DAPT — returns encoder directly (no disk save)
# ============================================================

def train_deberta_stage1(train_path, val_path, device):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    train_dataset = TurnDataset(train_path, tokenizer=tokenizer, max_length=DEBERTA_MAX_LENGTH)
    val_dataset = TurnDataset(val_path, tokenizer=tokenizer, max_length=DEBERTA_MAX_LENGTH)

    print(f"  Stage1 TurnDataset: train={len(train_dataset)}, val={len(val_dataset)}")

    train_loader = DataLoader(
        train_dataset, batch_size=DEBERTA_BATCH_SIZE, shuffle=True, collate_fn=TurnCollator()
    )
    val_loader = DataLoader(
        val_dataset, batch_size=DEBERTA_BATCH_SIZE, shuffle=False, collate_fn=TurnCollator()
    )

    model = DeBERTaMultiTask(model_name=MODEL_NAME).to(device)
    optimizer = torch.optim.AdamW(
        model.parameters(), lr=DEBERTA_LR, weight_decay=DEBERTA_WEIGHT_DECAY
    )
    total_steps = len(train_loader) * DEBERTA_EPOCHS
    scheduler = get_linear_schedule_with_warmup(
        optimizer,
        num_warmup_steps=int(total_steps * DEBERTA_WARMUP_RATIO),
        num_training_steps=total_steps,
    )

    best_val_loss = float("inf")
    best_state = None
    train_losses = []

    for epoch in range(DEBERTA_EPOCHS):
        model.train()
        epoch_loss = 0.0
        steps = 0

        for batch in train_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                persuasion_labels=batch["persuasion_labels"],
                intent_labels=batch["intent_labels"],
                alpha=DEBERTA_ALPHA,
            )
            loss = outputs["loss"]
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            epoch_loss += loss.item()
            steps += 1

        avg_train_loss = epoch_loss / max(steps, 1)
        train_losses.append(avg_train_loss)

        model.eval()
        val_loss = 0.0
        correct_p = 0
        correct_i = 0
        val_total = 0
        for batch in val_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            with torch.no_grad():
                outputs = model(
                    input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    persuasion_labels=batch["persuasion_labels"],
                    intent_labels=batch["intent_labels"],
                    alpha=DEBERTA_ALPHA,
                )
            val_loss += outputs["loss"].item() * batch["input_ids"].size(0)
            correct_p += (outputs["persuasion_logits"].argmax(-1) == batch["persuasion_labels"]).sum().item()
            correct_i += (outputs["intent_logits"].argmax(-1) == batch["intent_labels"]).sum().item()
            val_total += batch["input_ids"].size(0)

        avg_val_loss = val_loss / max(val_total, 1)
        p_acc = correct_p / max(val_total, 1)
        i_acc = correct_i / max(val_total, 1)

        marker = ""
        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            marker = " *"

        print(f"    Epoch {epoch+1}/{DEBERTA_EPOCHS} | "
              f"Train: {avg_train_loss:.4f} | Val: {avg_val_loss:.4f} | "
              f"P_Acc: {p_acc:.4f} | I_Acc: {i_acc:.4f}{marker}")

    # Extract frozen encoder from best state
    model.load_state_dict(best_state)
    encoder = model.deberta.to(device).eval()
    for p in encoder.parameters():
        p.requires_grad = False

    # Free the full model (heads etc)
    del model, best_state, optimizer, scheduler
    torch.cuda.empty_cache()

    return encoder, {"best_val_loss": best_val_loss, "train_losses": train_losses}


# ============================================================
# Stage 2: GRU frozen probing
# ============================================================

def precompute_embeddings(conversations, tokenizer, encoder, max_length, device):
    all_embeddings = []
    all_labels = []
    all_lengths = []
    for conv in conversations:
        turns = conv["turns"]
        if len(turns) == 0:
            all_embeddings.append(torch.zeros(1, encoder.config.hidden_size))
            all_lengths.append(1)
        else:
            enc = tokenizer(
                turns, max_length=max_length, padding=True,
                truncation=True, return_tensors="pt"
            ).to(device)
            with torch.no_grad():
                outputs = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
                embs = outputs.last_hidden_state[:, 0, :].cpu()
            all_embeddings.append(embs)
            all_lengths.append(len(turns))
        all_labels.append(conv["label"])
    return all_embeddings, all_labels, all_lengths


class PrecomputedDataset(torch.utils.data.Dataset):
    def __init__(self, embeddings, labels, lengths):
        self.embeddings = embeddings
        self.labels = labels
        self.lengths = lengths

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            "embeddings": self.embeddings[idx],
            "label": self.labels[idx],
            "length": self.lengths[idx],
        }


def precomputed_collator(batch):
    max_t = max(b["length"] for b in batch)
    embed_dim = batch[0]["embeddings"].size(-1)
    padded = torch.zeros(len(batch), max_t, embed_dim)
    lengths = []
    labels = []
    for i, b in enumerate(batch):
        padded[i, : b["length"], :] = b["embeddings"]
        lengths.append(b["length"])
        labels.append(b["label"])
    return {
        "embeddings": padded,
        "lengths": torch.tensor(lengths, dtype=torch.long),
        "labels": torch.tensor(labels, dtype=torch.long),
    }


def evaluate_loader(model, loader, criterion, device):
    model.eval()
    total_loss = 0.0
    all_preds = []
    all_labels = []
    with torch.no_grad():
        for batch in loader:
            embs = batch["embeddings"].to(device)
            lengths = batch["lengths"].to(device)
            labels = batch["labels"].to(device)
            logits = model(embs, lengths)
            loss = criterion(logits, labels)
            total_loss += loss.item() * labels.size(0)
            all_preds.extend(logits.argmax(-1).cpu().tolist())
            all_labels.extend(labels.cpu().tolist())
    n = max(len(all_labels), 1)
    f1 = f1_score(all_labels, all_preds, average="macro")
    acc = sum(p == l for p, l in zip(all_preds, all_labels)) / n
    return {"loss": total_loss / n, "acc": acc, "f1": f1}


def train_gru_stage2(train_embs, train_labels, train_lengths,
                      val_embs, val_labels, val_lengths,
                      embed_dim, output_dir, device):
    train_dataset = PrecomputedDataset(train_embs, train_labels, train_lengths)
    val_dataset = PrecomputedDataset(val_embs, val_labels, val_lengths)

    train_loader = DataLoader(
        train_dataset, batch_size=GRU_BATCH_SIZE, shuffle=True,
        collate_fn=precomputed_collator,
    )
    val_loader = DataLoader(
        val_dataset, batch_size=GRU_BATCH_SIZE, shuffle=False,
        collate_fn=precomputed_collator,
    )

    gru = GRUClassifier(
        input_dim=embed_dim,
        hidden_dim=GRU_HIDDEN_DIM,
        num_layers=GRU_NUM_LAYERS,
        dropout=GRU_DROPOUT,
    ).to(device)

    optimizer = torch.optim.Adam(gru.parameters(), lr=GRU_LR)
    criterion = nn.CrossEntropyLoss()

    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    best_val_loss = float("inf")
    best_state = None

    for epoch in range(GRU_EPOCHS):
        gru.train()
        epoch_loss = 0.0
        steps = 0
        for batch in train_loader:
            embs = batch["embeddings"].to(device)
            lengths = batch["lengths"].to(device)
            labels = batch["labels"].to(device)
            logits = gru(embs, lengths)
            loss = criterion(logits, labels)
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()
            epoch_loss += loss.item()
            steps += 1

        avg_train_loss = epoch_loss / max(steps, 1)
        val_metrics = evaluate_loader(gru, val_loader, criterion, device)

        if val_metrics["loss"] < best_val_loss:
            best_val_loss = val_metrics["loss"]
            best_state = {k: v.cpu().clone() for k, v in gru.state_dict().items()}
            print(f"    GRU Epoch {epoch+1}/{GRU_EPOCHS} | "
                  f"Train: {avg_train_loss:.4f} | "
                  f"Val: {val_metrics['loss']:.4f} | "
                  f"F1: {val_metrics['f1']:.4f} *")
        elif (epoch + 1) % 5 == 0:
            print(f"    GRU Epoch {epoch+1}/{GRU_EPOCHS} | "
                  f"Train: {avg_train_loss:.4f} | "
                  f"Val: {val_metrics['loss']:.4f} | "
                  f"F1: {val_metrics['f1']:.4f}")

    gru.load_state_dict(best_state)
    torch.save(best_state, output_dir / "best.pt")
    gru.eval()
    return gru


# ============================================================
# Evaluation helpers
# ============================================================

def predict_conversation(encoder, gru, tokenizer, turns, max_length, device):
    if len(turns) == 0:
        return 0
    enc = tokenizer(
        turns, max_length=max_length, padding=True,
        truncation=True, return_tensors="pt",
    ).to(device)
    with torch.no_grad():
        outputs = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        embs = outputs.last_hidden_state[:, 0, :].unsqueeze(0)
        lengths = torch.tensor([len(turns)], dtype=torch.long)
        logits = gru(embs.to(device), lengths.to(device))
        probs = torch.softmax(logits, dim=-1).cpu().numpy()[0]
    return int(probs[1] > 0.5)


def evaluate_on_set(encoder, gru, tokenizer, conversations, max_length, device):
    y_true = np.array([c["label"] for c in conversations])
    y_pred = np.array([
        predict_conversation(encoder, gru, tokenizer, c["turns"], max_length, device)
        for c in conversations
    ])
    return float(f1_score(y_true, y_pred, average="macro"))


def load_ood_data(attack_path, benign_source_path):
    conversations = []
    with open(attack_path) as f:
        for line in f:
            conv = json.loads(line.strip())
            user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
            conversations.append({
                "turns": user_turns,
                "label": 1,
                "attack_type": conv.get("attack_type", "unknown"),
                "conversation_id": conv["conversation_id"],
            })
    with open(benign_source_path) as f:
        for line in f:
            conv = json.loads(line.strip())
            if conv["label"] != "benign":
                continue
            user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
            conversations.append({
                "turns": user_turns,
                "label": 0,
                "attack_type": "benign",
                "conversation_id": conv["conversation_id"],
            })
    return conversations


def load_conversations(path):
    conversations = []
    with open(path) as f:
        for line in f:
            conv = json.loads(line.strip())
            user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
            label = 1 if conv["label"] == "jailbreak" else 0
            conversations.append({
                "turns": user_turns,
                "label": label,
                "attack_type": conv.get("attack_type", "unknown"),
                "conversation_id": conv["conversation_id"],
            })
    return conversations


# ============================================================
# Main
# ============================================================

def run_condition(subset_size, mode, train_data_raw, val_path, device):
    tag = f"{mode}_n{subset_size}"
    print(f"\n{'='*60}")
    print(f"Condition: {tag}")
    print(f"{'='*60}")

    set_seed(SEED)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    if subset_size < len(train_data_raw):
        subset = stratified_subsample(train_data_raw, subset_size, SEED)
    else:
        subset = train_data_raw

    label_dist = Counter(c["label"] for c in subset)
    print(f"  Subset: {len(subset)} conversations, distribution: {dict(label_dist)}")

    subset_path = f"{TMP_DIR}/{tag}_train.jsonl"
    write_jsonl(subset, subset_path)

    if mode == "9class":
        print(f"\n  --- Stage 1: DeBERTa 9-class DAPT ---")
        encoder, deberta_info = train_deberta_stage1(
            train_path=subset_path,
            val_path=val_path,
            device=device,
        )
    elif mode == "vanilla":
        print(f"\n  --- Using vanilla DeBERTa (no DAPT) ---")
        encoder = AutoModel.from_pretrained(MODEL_NAME, torch_dtype=torch.float32).to(device).eval()
        for p in encoder.parameters():
            p.requires_grad = False
        deberta_info = {"train_losses": [], "best_val_loss": None}

    embed_dim = encoder.config.hidden_size

    train_convs = load_conversations(subset_path)
    val_convs = load_conversations(val_path)

    print(f"\n  --- Stage 2: GRU Frozen Probing ---")
    print(f"  Pre-computing train embeddings...")
    train_embs, train_labels, train_lengths = precompute_embeddings(
        train_convs, tokenizer, encoder, DEBERTA_MAX_LENGTH, device
    )
    print(f"  Pre-computing val embeddings...")
    val_embs, val_labels, val_lengths = precompute_embeddings(
        val_convs, tokenizer, encoder, DEBERTA_MAX_LENGTH, device
    )

    gru = train_gru_stage2(
        train_embs, train_labels, train_lengths,
        val_embs, val_labels, val_lengths,
        embed_dim=embed_dim,
        output_dir=f"{CKPT_DIR}/{tag}/gru",
        device=device,
    )

    print(f"\n  --- Evaluation ---")
    test_convs = load_conversations(f"{DATA_DIR}/test.jsonl")
    iid_f1 = evaluate_on_set(encoder, gru, tokenizer, test_convs, DEBERTA_MAX_LENGTH, device)
    print(f"  IID F1: {iid_f1:.4f}")

    dd_convs = load_ood_data(
        f"{PROJ}/data/generated/deceptive_delight_all.jsonl",
        f"{DATA_DIR}/test.jsonl",
    )
    dd_f1 = evaluate_on_set(encoder, gru, tokenizer, dd_convs, DEBERTA_MAX_LENGTH, device)
    print(f"  DD OOD F1: {dd_f1:.4f}")

    aa_convs = load_ood_data(
        f"{PROJ}/data/generated/actorattack_all.jsonl",
        f"{DATA_DIR}/test.jsonl",
    )
    aa_f1 = evaluate_on_set(encoder, gru, tokenizer, aa_convs, DEBERTA_MAX_LENGTH, device)
    print(f"  AA OOD F1: {aa_f1:.4f}")

    result = {
        "n_train": len(subset),
        "label_distribution": dict(label_dist),
        "iid": iid_f1,
        "dd_ood": dd_f1,
        "aa_ood": aa_f1,
        "deberta_train_losses": deberta_info["train_losses"],
        "deberta_best_val_loss": deberta_info["best_val_loss"],
    }

    del encoder, gru
    torch.cuda.empty_cache()

    return result


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    train_data_raw = load_jsonl(f"{DATA_DIR}/train.jsonl")
    val_path = f"{DATA_DIR}/val.jsonl"
    print(f"Full training set: {len(train_data_raw)} conversations")
    print(f"Label distribution: {Counter(c['label'] for c in train_data_raw)}")

    results = {"9class": {}, "vanilla": {}}

    for n in SUBSET_SIZES:
        actual_n = min(n, len(train_data_raw))
        res = run_condition(actual_n, "9class", train_data_raw, val_path, device)
        results["9class"][str(actual_n)] = res

    res_v125 = run_condition(125, "vanilla", train_data_raw, val_path, device)
    results["vanilla"]["125"] = res_v125

    res_v350 = run_condition(350, "vanilla", train_data_raw, val_path, device)
    results["vanilla"]["350"] = res_v350

    results["reference"] = {
        "vanilla_multiseed_dd_ood_full_mean": 0.312,
        "9class_plan002_iid_full_seed42": 1.0,
        "note": "Vanilla DD OOD mean=0.312 from vanilla_multiseed_dd_ood registry entry",
    }

    output_path = f"{PROJ}/results/exp28_data_efficiency.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    print(f"\n{'='*70}")
    print("exp28 Data Efficiency Summary (macro F1)")
    print(f"{'='*70}")
    print(f"{'Condition':<25} {'N':>5} {'IID':>8} {'DD OOD':>8} {'AA OOD':>8}")
    print("-" * 70)
    for n in SUBSET_SIZES:
        key = str(min(n, len(train_data_raw)))
        r = results["9class"][key]
        print(f"{'9class':<25} {r['n_train']:>5} {r['iid']:>8.4f} {r['dd_ood']:>8.4f} {r['aa_ood']:>8.4f}")
    for n_key in ["125", "350"]:
        r = results["vanilla"][n_key]
        print(f"{'vanilla':<25} {r['n_train']:>5} {r['iid']:>8.4f} {r['dd_ood']:>8.4f} {r['aa_ood']:>8.4f}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
