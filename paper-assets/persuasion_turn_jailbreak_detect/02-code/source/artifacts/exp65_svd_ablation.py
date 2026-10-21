"""exp65: SVD dimension necessity ablation.

Tests whether removing top-3 SVD directions from 9-class CLS embeddings
destroys OOD detection (necessity), while removing random-3 does not (control).
Complements exp54/exp57 sufficiency evidence.
"""

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import sys
import json
import time
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from transformers import AutoTokenizer, AutoConfig, AutoModel
from src.models.gru_classifier import GRUClassifier
from src.models.deberta_multitask import DeBERTaMultiTask

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
DEVICE = torch.device("cuda:0")
MAX_LENGTH = 256
ARCHIVE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive")

PRETRAINED_PATH = "/root/.cache/huggingface/hub/models--microsoft--deberta-v3-base/snapshots/de19fe7db5162df5f3d8f0b41321c0267288fd74"
MODEL_PATH = str(ARCHIVE / "plan_002/deberta_multitask/best/model.pt")

DATA_FILES = {
    "train": PROJ / "data/plan_002_splits/train.jsonl",
    "val": PROJ / "data/plan_002_splits/val.jsonl",
    "test": PROJ / "data/plan_002_splits/test.jsonl",
    "dd_ood": PROJ / "data/generated/deceptive_delight_all.jsonl",
    "aa_ood": PROJ / "data/actorattack_ood/actorattack_all.jsonl",
    "fitd_ood": PROJ / "data/generated/fitd_all.jsonl",
}

GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
GRU_LR = 1e-3
GRU_EPOCHS = 20
GRU_BATCH = 32

SEEDS = [42, 123, 456]
TOP_K = 3

OUT_PATH = PROJ / "results/exp65_svd_ablation.json"


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def get_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def load_encoder():
    sd = torch.load(MODEL_PATH, map_location="cpu", weights_only=False)
    deberta_sd = {}
    for k, v in sd.items():
        if k.startswith("deberta."):
            deberta_sd[k[len("deberta."):]] = v
    config = AutoConfig.from_pretrained(PRETRAINED_PATH)
    model = AutoModel.from_config(config)
    model.load_state_dict(deberta_sd, strict=False)
    model = model.float().to(DEVICE).eval()
    for p in model.parameters():
        p.requires_grad = False
    return model


def extract_turn_embeddings(encoder, tokenizer, conversations, batch_size=32):
    conv_embeddings = []
    labels = []
    for conv in conversations:
        turns = get_user_turns(conv)
        if len(turns) == 0:
            conv_embeddings.append(torch.zeros(1, 768))
            labels.append(get_label(conv))
            continue
        all_turn_embs = []
        for i in range(0, len(turns), batch_size):
            batch = turns[i:i+batch_size]
            enc = tokenizer(
                batch, max_length=MAX_LENGTH, padding=True,
                truncation=True, return_tensors="pt"
            ).to(DEVICE)
            with torch.no_grad():
                out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
                embs = out.last_hidden_state[:, 0, :].cpu()
            all_turn_embs.append(embs)
        conv_embeddings.append(torch.cat(all_turn_embs, dim=0))
        labels.append(get_label(conv))
    return conv_embeddings, labels


def compute_svd_directions(conv_embeddings):
    all_turns = torch.cat(conv_embeddings, dim=0).numpy()
    mean = all_turns.mean(axis=0)
    centered = all_turns - mean
    U, S, Vt = np.linalg.svd(centered, full_matrices=False)
    return mean, S, Vt


def generate_random_orthogonal(d, k, seed):
    rng = np.random.RandomState(seed)
    M = rng.randn(d, k)
    Q, _ = np.linalg.qr(M)
    return Q[:, :k].T  # (k, d)


def ablate_embeddings(conv_embeddings, V_directions):
    V = torch.tensor(V_directions, dtype=torch.float32)  # (k, 768)
    ablated = []
    for embs in conv_embeddings:
        projection = embs @ V.T @ V
        ablated.append(embs - projection)
    return ablated


class PrecomputedDataset(torch.utils.data.Dataset):
    def __init__(self, embeddings, labels):
        self.embeddings = embeddings
        self.labels = labels
        self.lengths = [e.size(0) for e in embeddings]

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return {
            "embeddings": self.embeddings[idx],
            "label": self.labels[idx],
            "length": self.lengths[idx],
        }


def collate_fn(batch):
    max_t = max(b["length"] for b in batch)
    embed_dim = batch[0]["embeddings"].size(-1)
    padded = torch.zeros(len(batch), max_t, embed_dim)
    for i, b in enumerate(batch):
        padded[i, :b["length"], :] = b["embeddings"]
    return {
        "embeddings": padded,
        "lengths": torch.tensor([b["length"] for b in batch], dtype=torch.long),
        "labels": torch.tensor([b["label"] for b in batch], dtype=torch.long),
    }


def train_gru(train_embs, train_labels, val_embs, val_labels, seed):
    torch.manual_seed(seed)
    np.random.seed(seed)

    train_ds = PrecomputedDataset(train_embs, train_labels)
    val_ds = PrecomputedDataset(val_embs, val_labels)
    train_loader = torch.utils.data.DataLoader(
        train_ds, batch_size=GRU_BATCH, shuffle=True, collate_fn=collate_fn
    )
    val_loader = torch.utils.data.DataLoader(
        val_ds, batch_size=GRU_BATCH, shuffle=False, collate_fn=collate_fn
    )

    model = GRUClassifier(
        input_dim=768,
        hidden_dim=GRU_HIDDEN,
        num_layers=GRU_LAYERS,
        dropout=GRU_DROPOUT,
    ).to(DEVICE)

    optimizer = torch.optim.Adam(model.parameters(), lr=GRU_LR)
    criterion = nn.CrossEntropyLoss()

    best_val_loss = float("inf")
    best_state = None
    patience_counter = 0

    for epoch in range(GRU_EPOCHS):
        model.train()
        for batch in train_loader:
            embs = batch["embeddings"].to(DEVICE)
            lengths = batch["lengths"]
            labels = batch["labels"].to(DEVICE)
            logits = model(embs, lengths)
            loss = criterion(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        val_loss = 0.0
        val_n = 0
        with torch.no_grad():
            for batch in val_loader:
                embs = batch["embeddings"].to(DEVICE)
                lengths = batch["lengths"]
                labels = batch["labels"].to(DEVICE)
                logits = model(embs, lengths)
                loss = criterion(logits, labels)
                val_loss += loss.item() * labels.size(0)
                val_n += labels.size(0)

        val_loss /= max(val_n, 1)
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= 5:
                break

    model.load_state_dict(best_state)
    model.eval()
    return model


def evaluate_gru(model, conv_embeddings, labels):
    model.eval()
    all_preds = []
    with torch.no_grad():
        for embs in conv_embeddings:
            embs_batch = embs.unsqueeze(0).to(DEVICE)
            lengths = torch.tensor([embs.size(0)], dtype=torch.long)
            logits = model(embs_batch, lengths)
            all_preds.append(logits.argmax(dim=1).item())
    return float(f1_score(np.array(labels), np.array(all_preds), average="macro"))


def main():
    print("=" * 70)
    print("EXP65: SVD Dimension Necessity Ablation")
    print("=" * 70)

    tokenizer = AutoTokenizer.from_pretrained(PRETRAINED_PATH)

    print("\nLoading 9-class encoder...")
    encoder = load_encoder()

    print("Extracting per-turn CLS embeddings...")
    all_embs = {}
    all_labels = {}
    for name, path in DATA_FILES.items():
        data = load_jsonl(str(path))
        embs, labels = extract_turn_embeddings(encoder, tokenizer, data)
        all_embs[name] = embs
        all_labels[name] = labels
        n_turns = sum(e.size(0) for e in embs)
        print(f"  {name}: {len(data)} convs, {n_turns} turns")

    del encoder
    torch.cuda.empty_cache()

    # Build OOD eval sets: OOD jailbreak + test benign
    test_benign_embs = [e for e, l in zip(all_embs["test"], all_labels["test"]) if l == 0]
    test_benign_labels = [0] * len(test_benign_embs)
    print(f"\nTest benign for OOD eval: {len(test_benign_embs)} conversations")

    ood_eval = {}
    for ood_name in ["dd_ood", "aa_ood", "fitd_ood"]:
        ood_embs = all_embs[ood_name] + test_benign_embs
        ood_labels = all_labels[ood_name] + test_benign_labels
        ood_eval[ood_name] = (ood_embs, ood_labels)
        n_jb = sum(all_labels[ood_name])
        print(f"  {ood_name}: {n_jb} jailbreak + {len(test_benign_embs)} benign = {len(ood_labels)}")

    # SVD on training turn embeddings
    print("\nComputing SVD on training turn embeddings...")
    train_mean, S, Vt = compute_svd_directions(all_embs["train"])
    V_top3 = Vt[:TOP_K]
    var_top3 = float((S[:TOP_K]**2).sum() / (S**2).sum())
    print(f"  Top-10 singular values: {np.round(S[:10], 2).tolist()}")
    print(f"  Variance explained by top-{TOP_K}: {var_top3:.4f}")

    # Define conditions
    conditions = {}

    # 1. Original 768-dim
    conditions["original"] = {
        "train": all_embs["train"],
        "val": all_embs["val"],
        "ood": {k: v for k, v in ood_eval.items()},
    }

    # 2. Remove top-3 SVD directions
    conditions["remove_top3_svd"] = {
        "train": ablate_embeddings(all_embs["train"], V_top3),
        "val": ablate_embeddings(all_embs["val"], V_top3),
        "ood": {k: (ablate_embeddings(v[0], V_top3), v[1]) for k, v in ood_eval.items()},
    }

    # 3. Remove random-3 orthogonal directions (fixed seed=0 for reproducibility)
    random_V = generate_random_orthogonal(768, TOP_K, seed=0)
    conditions["remove_random3"] = {
        "train": ablate_embeddings(all_embs["train"], random_V),
        "val": ablate_embeddings(all_embs["val"], random_V),
        "ood": {k: (ablate_embeddings(v[0], random_V), v[1]) for k, v in ood_eval.items()},
    }

    # Run experiments
    results = {}
    for cond_name, cond_data in conditions.items():
        print(f"\n{'='*60}")
        print(f"Condition: {cond_name}")
        print(f"{'='*60}")

        cond_results = {ood: [] for ood in ood_eval}

        for seed in SEEDS:
            print(f"\n  Seed {seed}:")
            t0 = time.time()

            gru = train_gru(
                cond_data["train"], all_labels["train"],
                cond_data["val"], all_labels["val"],
                seed=seed,
            )

            for ood_name in ood_eval:
                ood_embs, ood_labels = cond_data["ood"][ood_name]
                f1 = evaluate_gru(gru, ood_embs, ood_labels)
                cond_results[ood_name].append(f1)
                short = ood_name.replace("_ood", "").upper()
                print(f"    {short}: F1={f1:.4f}")

            del gru
            torch.cuda.empty_cache()
            print(f"    ({time.time()-t0:.1f}s)")

        results[cond_name] = {}
        for ood_name in ood_eval:
            vals = cond_results[ood_name]
            results[cond_name][ood_name] = {
                "per_seed": {str(s): round(v, 4) for s, v in zip(SEEDS, vals)},
                "mean": round(float(np.mean(vals)), 4),
                "std": round(float(np.std(vals)), 4),
            }

    # Summary
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY (mean +/- std over 3 seeds)")
    print("=" * 70)
    print(f"{'Condition':<25} {'DD F1':>14} {'FITD F1':>14} {'AA F1':>14}")
    print("-" * 67)
    for cond in ["original", "remove_top3_svd", "remove_random3"]:
        dd = results[cond]["dd_ood"]
        fitd = results[cond]["fitd_ood"]
        aa = results[cond]["aa_ood"]
        print(f"{cond:<25} {dd['mean']:.4f}+/-{dd['std']:.4f}  {fitd['mean']:.4f}+/-{fitd['std']:.4f}  {aa['mean']:.4f}+/-{aa['std']:.4f}")

    # Save
    output = {
        "experiment": "exp65_svd_necessity_ablation",
        "hypothesis": "Removing top-3 SVD directions destroys OOD detection; removing random-3 does not",
        "svd_info": {
            "computed_on": "training per-turn CLS embeddings (9-class encoder, plan_002)",
            "top10_singular_values": np.round(S[:10], 4).tolist(),
            "variance_explained_top3": round(var_top3, 4),
        },
        "eval_setup": {
            "ood_composition": "OOD jailbreak + IID test benign",
            "gru_retrained_per_condition": True,
            "gru_config": {"hidden": GRU_HIDDEN, "layers": GRU_LAYERS, "dropout": GRU_DROPOUT, "lr": GRU_LR, "epochs": GRU_EPOCHS},
        },
        "conditions": list(results.keys()),
        "seeds": SEEDS,
        "results": results,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nResults saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
