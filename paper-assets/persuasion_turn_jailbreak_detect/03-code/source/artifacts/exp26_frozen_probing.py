"""exp26: Frozen Probing — freeze DeBERTa 9-class DAPT encoder, train BiGRU from scratch.
Verifies whether DAPT representations alone carry OOD generalization signal.
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/hf_cache"
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["CUDA_VISIBLE_DEVICES"] = "0,1,2,3"

import sys
import json
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from transformers import AutoTokenizer
from sklearn.metrics import f1_score

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.data.dataset import ConversationDataset
from src.models.gru_classifier import GRUClassifier
from src.models.deberta_multitask import DeBERTaMultiTask

PROJ = "/root/persuasion_turn_jailbreak_detect"
DATA_DIR = f"{PROJ}/data/plan_002_splits"
ARCHIVE = "/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive"
MODEL_NAME = "microsoft/deberta-v3-base"

DAPT_CHECKPOINTS = {
    42: f"{ARCHIVE}/plan_002/deberta_multitask/best",
    123: f"{ARCHIVE}/plan_002_seed123/deberta_multitask/best",
    456: f"{ARCHIVE}/plan_002_seed456/deberta_multitask/best",
}

MAX_LENGTH = 256
BATCH_SIZE = 32
LR = 1e-3
HIDDEN_DIM = 256
NUM_LAYERS = 2
DROPOUT = 0.3
EPOCHS = 20
SEEDS = [42, 123, 456]


def load_frozen_encoder(seed, device):
    ckpt_dir = DAPT_CHECKPOINTS[seed]
    model = DeBERTaMultiTask(model_name=MODEL_NAME)
    state_dict = torch.load(
        Path(ckpt_dir) / "model.pt", map_location="cpu", weights_only=False
    )
    model.load_state_dict(state_dict)
    encoder = model.deberta
    encoder.eval()
    for param in encoder.parameters():
        param.requires_grad = False
    return encoder.to(device)


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
                outputs = encoder(
                    input_ids=enc["input_ids"],
                    attention_mask=enc["attention_mask"],
                )
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


def predict_conversation(encoder, gru, tokenizer, turns, max_length, device, max_turns=None):
    if max_turns is not None:
        turns = turns[:max_turns]
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


def evaluate_ood(encoder, gru, tokenizer, conversations, max_length, device, k_values=None):
    if k_values is None:
        k_values = [1, 2, 3, 5]
    y_true = np.array([c["label"] for c in conversations])
    results = {}

    y_pred = np.array([
        predict_conversation(encoder, gru, tokenizer, c["turns"], max_length, device)
        for c in conversations
    ])
    results["full"] = float(f1_score(y_true, y_pred, average="macro"))

    for k in k_values:
        y_pred_k = np.array([
            predict_conversation(encoder, gru, tokenizer, c["turns"], max_length, device, max_turns=k)
            for c in conversations
        ])
        results[f"k{k}"] = float(f1_score(y_true, y_pred_k, average="macro"))

    return results


def train_one_seed(seed, device):
    print(f"\n{'='*60}")
    print(f"Training seed={seed}")
    print(f"{'='*60}")

    torch.manual_seed(seed)
    np.random.seed(seed)

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    encoder = load_frozen_encoder(seed, device)
    embed_dim = encoder.config.hidden_size

    print("Pre-computing train embeddings...")
    train_ds = ConversationDataset(f"{DATA_DIR}/train.jsonl")
    train_embs, train_labels, train_lengths = precompute_embeddings(
        train_ds.conversations, tokenizer, encoder, MAX_LENGTH, device
    )
    train_dataset = PrecomputedDataset(train_embs, train_labels, train_lengths)

    print("Pre-computing val embeddings...")
    val_ds = ConversationDataset(f"{DATA_DIR}/val.jsonl")
    val_embs, val_labels, val_lengths = precompute_embeddings(
        val_ds.conversations, tokenizer, encoder, MAX_LENGTH, device
    )
    val_dataset = PrecomputedDataset(val_embs, val_labels, val_lengths)

    train_loader = DataLoader(
        train_dataset, batch_size=BATCH_SIZE, shuffle=True,
        collate_fn=precomputed_collator,
    )
    val_loader = DataLoader(
        val_dataset, batch_size=BATCH_SIZE, shuffle=False,
        collate_fn=precomputed_collator,
    )

    gru = GRUClassifier(
        input_dim=embed_dim,
        hidden_dim=HIDDEN_DIM,
        num_layers=NUM_LAYERS,
        dropout=DROPOUT,
    ).to(device)

    optimizer = torch.optim.Adam(gru.parameters(), lr=LR)
    criterion = nn.CrossEntropyLoss()

    output_dir = Path(f"{PROJ}/checkpoints/exp26_frozen_seed{seed}")
    output_dir.mkdir(parents=True, exist_ok=True)
    best_val_loss = float("inf")

    for epoch in range(EPOCHS):
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

        print(
            f"  Epoch {epoch+1}/{EPOCHS} | "
            f"Train Loss: {avg_train_loss:.4f} | "
            f"Val Loss: {val_metrics['loss']:.4f} | "
            f"Val Acc: {val_metrics['acc']:.4f} | "
            f"Val F1: {val_metrics['f1']:.4f}"
        )

        if val_metrics["loss"] < best_val_loss:
            best_val_loss = val_metrics["loss"]
            torch.save(gru.state_dict(), output_dir / "best.pt")
            print(f"    -> Best model saved (val_loss={best_val_loss:.4f})")

    # Load best
    gru.load_state_dict(torch.load(output_dir / "best.pt", map_location=device, weights_only=True))
    gru.eval()

    # === Evaluation ===
    print(f"\nEvaluating seed={seed}...")
    seed_results = {}

    # IID test
    print("  IID test...")
    test_ds = ConversationDataset(f"{DATA_DIR}/test.jsonl")
    iid_res = evaluate_ood(encoder, gru, tokenizer, test_ds.conversations, MAX_LENGTH, device, k_values=[])
    seed_results["iid_full"] = iid_res["full"]

    # DD OOD (k=1,2,3,5,full)
    print("  DD OOD...")
    dd_convs = load_ood_data(
        f"{PROJ}/data/generated/deceptive_delight_all.jsonl",
        f"{DATA_DIR}/test.jsonl",
    )
    dd_res = evaluate_ood(encoder, gru, tokenizer, dd_convs, MAX_LENGTH, device)
    seed_results["dd_ood_full"] = dd_res["full"]
    for k in [1, 2, 3, 5]:
        seed_results[f"dd_ood_k{k}"] = dd_res[f"k{k}"]

    # AA OOD (full)
    print("  AA OOD...")
    aa_convs = load_ood_data(
        f"{PROJ}/data/generated/actorattack_all.jsonl",
        f"{DATA_DIR}/test.jsonl",
    )
    aa_res = evaluate_ood(encoder, gru, tokenizer, aa_convs, MAX_LENGTH, device, k_values=[])
    seed_results["aa_ood_full"] = aa_res["full"]

    # FITD OOD (full)
    fitd_path = f"{PROJ}/data/generated/fitd_all.jsonl"
    if os.path.exists(fitd_path):
        print("  FITD OOD...")
        fitd_convs = load_ood_data(fitd_path, f"{DATA_DIR}/test.jsonl")
        fitd_res = evaluate_ood(encoder, gru, tokenizer, fitd_convs, MAX_LENGTH, device, k_values=[])
        seed_results["fitd_ood_full"] = fitd_res["full"]

    print(f"  seed={seed} done: " + ", ".join(f"{k}={v:.4f}" for k, v in seed_results.items()))

    del encoder, gru
    torch.cuda.empty_cache()

    return seed_results


def main():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")

    all_seeds_results = {}
    for seed in SEEDS:
        all_seeds_results[f"seed{seed}"] = train_one_seed(seed, device)

    # Compute mean/std
    metrics = [
        "iid_full",
        "dd_ood_k1", "dd_ood_k2", "dd_ood_k3", "dd_ood_k5", "dd_ood_full",
        "aa_ood_full", "fitd_ood_full",
    ]
    mean_results = {}
    std_results = {}
    for m in metrics:
        vals = [all_seeds_results[f"seed{s}"][m] for s in SEEDS if m in all_seeds_results[f"seed{s}"]]
        if vals:
            mean_results[m] = float(np.mean(vals))
            std_results[m] = float(np.std(vals))

    # e2e reference from exp18
    e2e_reference = {
        "comment": "Reference from exp18 end-to-end fine-tuning (unfrozen DeBERTa + GRU)",
        "seed42": {"IID": 1.0, "DD_OOD": 1.0, "AA_OOD": 1.0},
        "seed123": {"IID": 1.0, "DD_OOD": 1.0, "AA_OOD": 0.9904},
        "seed456": {"IID": 1.0, "DD_OOD": 1.0, "AA_OOD": 1.0},
        "mean": {"IID": 1.0, "DD_OOD": 1.0, "AA_OOD": 0.9968},
    }

    output = {
        "frozen_9class": {
            **all_seeds_results,
            "mean": mean_results,
            "std": std_results,
        },
        "e2e_reference": e2e_reference,
    }

    output_path = f"{PROJ}/results/exp26_frozen_probing.json"
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {output_path}")

    # Summary
    print(f"\n{'='*60}")
    print("exp26 Frozen Probing Summary (mean +/- std):")
    print(f"{'='*60}")
    for m in metrics:
        if m in mean_results:
            print(f"  {m}: {mean_results[m]:.4f} +/- {std_results[m]:.4f}")

    print(f"\ne2e reference (exp18 mean): IID={e2e_reference['mean']['IID']:.4f} "
          f"DD_OOD={e2e_reference['mean']['DD_OOD']:.4f} "
          f"AA_OOD={e2e_reference['mean']['AA_OOD']:.4f}")


if __name__ == "__main__":
    main()
