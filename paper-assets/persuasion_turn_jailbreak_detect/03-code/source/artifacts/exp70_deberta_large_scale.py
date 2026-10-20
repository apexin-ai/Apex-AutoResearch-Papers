"""Exp70: DeBERTa-v3-large (~304M) scale comparison.

Trains 2 variants (vanilla, 9-class DAPT) x 3 seeds on DeBERTa-v3-large,
evaluates DD OOD + ActorAttack OOD. Compares with RoBERTa-large baselines
to determine if DAPT harm at ~350M scale is architecture-specific.

Adapted from scripts/exp15_roberta_large.py.
"""
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

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
from src.models.deberta_multitask import DeBERTaMultiTask
from transformers import AutoTokenizer, AutoModel, get_linear_schedule_with_warmup
from src.data.dataset import TurnDataset
from src.data.collator import TurnCollator
from torch.utils.data import DataLoader

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
MODEL_NAME = "microsoft/deberta-v3-large"
CKPT_ROOT = PROJ / "checkpoints"
DATA_ROOT = PROJ / "data"

MAX_LENGTH = 256
GRU_HIDDEN = 256
GRU_LAYERS = 2
GRU_DROPOUT = 0.3
GRU_LR = 1e-3
GRU_EPOCHS = 20
GRU_BATCH = 32
SEEDS = [42, 123, 456]

DAPT_EPOCHS = 5
DAPT_BATCH = 8
DAPT_LR = 2e-5

ROBERTA_LARGE_BASELINES = {
    "dd_ood": {
        "vanilla": {"mean": 0.927, "std": 0.036},
        "9class": {"mean": 0.987, "std": 0.004},
    },
    "actorattack": {
        "vanilla": {"mean": 1.000, "std": 0.000},
        "9class": {"mean": 0.946, "std": 0.057},
    },
}


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


# ==================== Stage 1: DAPT Training ====================

def train_dapt(seed, device):
    save_dir = CKPT_ROOT / f"exp70_deberta_large_9class_seed{seed}" / "deberta_multitask" / "best"
    if (save_dir / "model.pt").exists():
        print(f"  DAPT seed={seed} already done, skipping")
        return save_dir

    set_seed(seed)
    print(f"  Training DAPT seed={seed}...")

    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    train_ds = TurnDataset(
        str(DATA_ROOT / "plan_002_splits/train.jsonl"),
        tokenizer=tokenizer, max_length=MAX_LENGTH
    )
    val_ds = TurnDataset(
        str(DATA_ROOT / "plan_002_splits/val.jsonl"),
        tokenizer=tokenizer, max_length=MAX_LENGTH
    )
    train_loader = DataLoader(train_ds, batch_size=DAPT_BATCH, shuffle=True, collate_fn=TurnCollator())
    val_loader = DataLoader(val_ds, batch_size=DAPT_BATCH, shuffle=False, collate_fn=TurnCollator())

    model = DeBERTaMultiTask(model_name=MODEL_NAME, num_persuasion_classes=9)
    model.to(device)

    optimizer = torch.optim.AdamW(model.parameters(), lr=DAPT_LR, weight_decay=0.01)
    total_steps = len(train_loader) * DAPT_EPOCHS
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=int(total_steps * 0.1), num_training_steps=total_steps
    )

    best_val_loss = float("inf")
    save_dir.mkdir(parents=True, exist_ok=True)

    for epoch in range(DAPT_EPOCHS):
        model.train()
        epoch_loss, steps = 0.0, 0
        for batch in train_loader:
            batch = {k: v.to(device) for k, v in batch.items()}
            outputs = model(
                input_ids=batch["input_ids"],
                attention_mask=batch["attention_mask"],
                persuasion_labels=batch["persuasion_labels"],
                intent_labels=batch["intent_labels"],
                alpha=0.3,
            )
            loss = outputs["loss"]
            loss.backward()
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()
            epoch_loss += loss.item()
            steps += 1

        model.eval()
        val_loss, val_correct, val_total = 0.0, 0, 0
        with torch.no_grad():
            for batch in val_loader:
                batch = {k: v.to(device) for k, v in batch.items()}
                outputs = model(
                    input_ids=batch["input_ids"],
                    attention_mask=batch["attention_mask"],
                    persuasion_labels=batch["persuasion_labels"],
                    intent_labels=batch["intent_labels"],
                    alpha=0.3,
                )
                val_loss += outputs["loss"].item() * batch["input_ids"].size(0)
                val_correct += (outputs["persuasion_logits"].argmax(-1) == batch["persuasion_labels"]).sum().item()
                val_total += batch["input_ids"].size(0)

        avg_val_loss = val_loss / max(val_total, 1)
        val_acc = val_correct / max(val_total, 1)
        print(f"    Epoch {epoch+1}/{DAPT_EPOCHS} | Train Loss: {epoch_loss/steps:.4f} | Val Loss: {avg_val_loss:.4f} | Val Acc: {val_acc:.4f}")

        if avg_val_loss < best_val_loss:
            best_val_loss = avg_val_loss
            unwrapped = model
            torch.save(unwrapped.state_dict(), save_dir / "model.pt")
            tokenizer.save_pretrained(save_dir)
            metrics = {"best_epoch": epoch + 1, "val_loss": avg_val_loss, "val_acc": val_acc}
            with open(save_dir / "training_metrics.json", "w") as mf:
                json.dump(metrics, mf, indent=2)
            print(f"      -> Best model saved (val_loss={best_val_loss:.4f})")

    del model, optimizer, scheduler
    torch.cuda.empty_cache()
    return save_dir


# ==================== Embedding + GRU ====================

def precompute_conv_embeddings(encoder, tokenizer, conversations, device):
    all_embs, all_labels, all_lengths = [], [], []
    for conv in conversations:
        turns = conv["turns"]
        if len(turns) == 0:
            turns = [""]
        enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(device)
        with torch.no_grad():
            out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].cpu()
        all_embs.append(embs)
        all_labels.append(conv["label"])
        all_lengths.append(embs.size(0))
    return all_embs, all_labels, all_lengths


def pad_embeddings(embs_list, labels, lengths):
    max_len = max(lengths)
    dim = embs_list[0].size(1)
    padded = torch.zeros(len(embs_list), max_len, dim)
    for i, e in enumerate(embs_list):
        padded[i, :e.size(0), :] = e
    return padded, torch.tensor(labels, dtype=torch.long), torch.tensor(lengths, dtype=torch.long)


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
        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            torch.save(model.state_dict(), save_dir / "best.pt")

        if (epoch + 1) % 5 == 0:
            print(f"      GRU Epoch {epoch+1}/{GRU_EPOCHS} | Loss: {epoch_loss/max(steps,1):.4f} | Val F1: {val_f1:.4f} (best={best_val_f1:.4f})")

    print(f"      GRU done, best val F1={best_val_f1:.4f}")
    model.load_state_dict(torch.load(save_dir / "best.pt", map_location="cpu"))
    model.to(device)
    model.eval()
    return model


# ==================== Evaluation ====================

def eval_ood(encoder, gru, tokenizer, conversations, device, k=None):
    all_preds, all_labels = [], []
    for conv in conversations:
        turns = conv["turns"][:k] if k is not None else conv["turns"]
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


def load_ood_data(ood_path, benign_test_path):
    conversations = []
    with open(ood_path) as f:
        for line in f:
            conv = json.loads(line.strip())
            user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
            conversations.append({"turns": user_turns, "label": 1, "conversation_id": conv["conversation_id"]})

    with open(benign_test_path) as f:
        for line in f:
            conv = json.loads(line.strip())
            if conv["label"] == "benign":
                user_turns = [t["content"] for t in conv["turns"] if t["role"] == "user"]
                conversations.append({"turns": user_turns, "label": 0, "conversation_id": conv["conversation_id"]})

    return conversations


# ==================== Main ====================

def main():
    device = torch.device("cuda:0")
    print(f"Device: {device}")
    print(f"Model: {MODEL_NAME}")

    # Download model if needed
    print("\n=== Downloading model (if not cached) ===")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    _test_model = AutoModel.from_pretrained(MODEL_NAME)
    embed_dim_check = _test_model.config.hidden_size
    print(f"  hidden_size={embed_dim_check}")
    del _test_model
    torch.cuda.empty_cache()

    # Stage 1: DAPT training for 3 seeds
    print("\n=== Stage 1: DAPT Training ===")
    dapt_dirs = {}
    for seed in SEEDS:
        print(f"\n--- Seed {seed} ---")
        dapt_dirs[seed] = train_dapt(seed, device)
        print(f"  Checkpoint: {dapt_dirs[seed]}")

    # Load data for Stage 2
    print("\n=== Loading data ===")
    train_data_raw = load_jsonl(DATA_ROOT / "plan_002_splits/train.jsonl")
    val_data_raw = load_jsonl(DATA_ROOT / "plan_002_splits/val.jsonl")
    train_data = []
    for c in train_data_raw:
        user_turns = [t["content"] for t in c["turns"] if t["role"] == "user"]
        train_data.append({"turns": user_turns, "label": get_label(c)})
    val_data = []
    for c in val_data_raw:
        user_turns = [t["content"] for t in c["turns"] if t["role"] == "user"]
        val_data.append({"turns": user_turns, "label": get_label(c)})
    print(f"  Train: {len(train_data)}, Val: {len(val_data)}")

    # Load OOD data
    dd_convs = load_ood_data(
        DATA_ROOT / "generated/deceptive_delight_all.jsonl",
        DATA_ROOT / "plan_002_splits/test.jsonl"
    )
    aa_convs = load_ood_data(
        DATA_ROOT / "generated/actorattack_all.jsonl",
        DATA_ROOT / "plan_002_splits/test.jsonl"
    )
    n_dd_jb = sum(1 for c in dd_convs if c["label"] == 1)
    n_dd_bn = sum(1 for c in dd_convs if c["label"] == 0)
    n_aa_jb = sum(1 for c in aa_convs if c["label"] == 1)
    n_aa_bn = sum(1 for c in aa_convs if c["label"] == 0)
    print(f"  DD OOD: {n_dd_jb} jailbreak + {n_dd_bn} benign = {len(dd_convs)}")
    print(f"  AA OOD: {n_aa_jb} jailbreak + {n_aa_bn} benign = {len(aa_convs)}")

    dd_k_values = [1, 2, 3, 5]
    aa_k_values = [1, 2, 3, 5]

    results = {"dd_ood": {}, "actorattack": {}}

    for variant in ["vanilla", "9class"]:
        print(f"\n{'='*60}")
        print(f"Variant: {variant}")
        print(f"{'='*60}")

        variant_dd_results = {"per_seed": {}}
        variant_aa_results = {"per_seed": {}}

        for seed in SEEDS:
            set_seed(seed)
            print(f"\n  --- Seed {seed}, variant={variant} ---")

            if variant == "vanilla":
                print(f"  Loading vanilla DeBERTa-v3-large encoder...")
                encoder = AutoModel.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)
                gru_save_dir = CKPT_ROOT / f"exp70_deberta_large_vanilla_seed{seed}" / "gru" / "baseline"
            else:
                print(f"  Loading 9-class DAPT DeBERTa-v3-large encoder (seed={seed})...")
                model = DeBERTaMultiTask(model_name=MODEL_NAME, num_persuasion_classes=9)
                state_dict = torch.load(dapt_dirs[seed] / "model.pt", map_location="cpu")
                model.load_state_dict(state_dict)
                encoder = model.deberta
                del model
                gru_save_dir = CKPT_ROOT / f"exp70_deberta_large_9class_seed{seed}" / "gru" / "treatment"

            encoder.to(device)
            encoder.eval()
            for p in encoder.parameters():
                p.requires_grad = False
            embed_dim = encoder.config.hidden_size
            print(f"  embed_dim={embed_dim}")

            print(f"  Precomputing train embeddings...")
            train_embs, train_labels, train_lengths = precompute_conv_embeddings(encoder, tokenizer, train_data, device)
            print(f"  Precomputing val embeddings...")
            val_embs, val_labels, val_lengths = precompute_conv_embeddings(encoder, tokenizer, val_data, device)

            print(f"  Training GRU...")
            gru = train_gru(
                train_embs, train_labels, train_lengths,
                val_embs, val_labels, val_lengths,
                gru_save_dir, seed, embed_dim, device
            )

            print(f"  Evaluating DD OOD...")
            seed_dd = {}
            seed_dd["full"] = eval_ood(encoder, gru, tokenizer, dd_convs, device)
            for k in dd_k_values:
                seed_dd[f"k{k}"] = eval_ood(encoder, gru, tokenizer, dd_convs, device, k=k)
            print(f"    DD: full={seed_dd['full']:.4f}, k1={seed_dd['k1']:.4f}, k3={seed_dd['k3']:.4f}")
            variant_dd_results["per_seed"][str(seed)] = seed_dd

            print(f"  Evaluating ActorAttack OOD...")
            seed_aa = {}
            seed_aa["full"] = eval_ood(encoder, gru, tokenizer, aa_convs, device)
            for k in aa_k_values:
                seed_aa[f"k{k}"] = eval_ood(encoder, gru, tokenizer, aa_convs, device, k=k)
            print(f"    AA: full={seed_aa['full']:.4f}, k1={seed_aa['k1']:.4f}, k3={seed_aa['k3']:.4f}")
            variant_aa_results["per_seed"][str(seed)] = seed_aa

            del encoder, gru
            torch.cuda.empty_cache()

        for res_dict in [variant_dd_results, variant_aa_results]:
            res_dict["mean_std"] = {}
            metrics = ["k1", "k2", "k3", "k5", "full"]
            for m in metrics:
                vals = [v[m] for v in res_dict["per_seed"].values() if m in v]
                if vals:
                    res_dict["mean_std"][m] = {"mean": float(np.mean(vals)), "std": float(np.std(vals))}

        key = f"deberta_large_{variant}"
        results["dd_ood"][key] = variant_dd_results
        results["actorattack"][key] = variant_aa_results

    # Save results
    out_dir = PROJ / "results" / "rebuttal" / "deberta_large_scale"
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "exp70_deberta_large_scale.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # Print summary with RoBERTa-large comparison
    print("\n" + "=" * 80)
    print("SUMMARY: DeBERTa-v3-large vs RoBERTa-large Scale Comparison")
    print("=" * 80)

    for eval_name, eval_key in [("DD OOD", "dd_ood"), ("ActorAttack", "actorattack")]:
        print(f"\n{eval_name} (Macro F1 'full', mean +/- std, 3 seeds):")
        print(f"{'Model':<35} {'Full F1':>20}")
        print("-" * 55)

        for variant in ["vanilla", "9class"]:
            deb_key = f"deberta_large_{variant}"
            if deb_key in results[eval_key]:
                ms = results[eval_key][deb_key].get("mean_std", {})
                if "full" in ms:
                    print(f"  DeBERTa-v3-large {variant:<16} {ms['full']['mean']:.4f} +/- {ms['full']['std']:.4f}")

            rob_baseline = ROBERTA_LARGE_BASELINES.get(eval_key, {}).get(variant, {})
            if rob_baseline:
                print(f"  RoBERTa-large {variant:<19} {rob_baseline['mean']:.4f} +/- {rob_baseline['std']:.4f}")

    # Key comparison: does 9-class AA < vanilla AA?
    print("\n" + "=" * 80)
    print("KEY QUESTION: Does DeBERTa-v3-large also show 9-class AA < vanilla AA?")
    print("=" * 80)
    deb_van_aa = results["actorattack"].get("deberta_large_vanilla", {}).get("mean_std", {}).get("full", {})
    deb_9c_aa = results["actorattack"].get("deberta_large_9class", {}).get("mean_std", {}).get("full", {})
    if deb_van_aa and deb_9c_aa:
        gap = deb_9c_aa["mean"] - deb_van_aa["mean"]
        if gap < 0:
            print(f"  YES: 9-class AA ({deb_9c_aa['mean']:.4f}) < vanilla AA ({deb_van_aa['mean']:.4f}), gap = {gap:.4f}")
            print("  -> Confirms scale effect: DAPT harms AA OOD at ~300M+ scale regardless of architecture")
        else:
            print(f"  NO: 9-class AA ({deb_9c_aa['mean']:.4f}) >= vanilla AA ({deb_van_aa['mean']:.4f}), gap = {gap:+.4f}")
            print("  -> Suggests RoBERTa-specific effect, not a general scale phenomenon")

    # Also check DD improvement
    deb_van_dd = results["dd_ood"].get("deberta_large_vanilla", {}).get("mean_std", {}).get("full", {})
    deb_9c_dd = results["dd_ood"].get("deberta_large_9class", {}).get("mean_std", {}).get("full", {})
    if deb_van_dd and deb_9c_dd:
        gap = deb_9c_dd["mean"] - deb_van_dd["mean"]
        print(f"\n  DD OOD: 9-class ({deb_9c_dd['mean']:.4f}) vs vanilla ({deb_van_dd['mean']:.4f}), gap = {gap:+.4f}")

    print("\nDone.")


if __name__ == "__main__":
    main()
