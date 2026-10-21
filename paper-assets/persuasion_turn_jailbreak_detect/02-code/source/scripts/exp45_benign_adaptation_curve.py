#!/usr/bin/env python3
"""exp45: Benign Adaptation Curve — Few-shot WildChat FPR reduction.

Determines how many WildChat benign samples are needed to reduce FPR.
Trains with N in {0, 5, 10, 25, 50, 100, 150} WildChat benign + 350 original Qwen.
Single seed (42) per N. Nested subsets (N=5 is subset of N=10, etc.).
"""

import os
os.environ["HF_HUB_OFFLINE"] = "1"
os.environ["TRANSFORMERS_OFFLINE"] = "1"

import sys, json, random, time, re, subprocess
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from collections import Counter
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
CKPT_BASE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints")
LOCAL_MODEL = "/root/autodl-tmp/hf_cache/hub/models--microsoft--deberta-v3-base/snapshots/8ccc9b6f36199bec6961081d44eb72fb3f7353f3"
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

SEED = 42
N_VALUES = [0, 5, 10, 25, 50, 100, 150]

WILDCHAT_PATH = PROJ / "data" / "wildchat_benign_226.jsonl"
TRAIN_PATH = PROJ / "data" / "plan_002_splits" / "train.jsonl"
VAL_PATH = PROJ / "data" / "plan_002_splits" / "val.jsonl"
TEST_PATH = PROJ / "data" / "plan_002_splits" / "test.jsonl"
DD_PATH = PROJ / "data" / "generated" / "deceptive_delight_all.jsonl"
AA_PATH = PROJ / "data" / "actorattack_ood" / "actorattack_all.jsonl"
FITD_PATH = PROJ / "data" / "generated" / "fitd_all.jsonl"

RESULTS_JSON = PROJ / "results" / "exp45_benign_adaptation_curve.json"

JAILBREAK_KEYWORDS = [
    "ignore previous instructions", "ignore all previous", "disregard previous",
    "forget your instructions", "you are now", "act as if", "pretend you are",
    "jailbreak", "DAN", "do anything now", "bypass", "override your",
    "ignore your programming", "ignore your training", "system prompt",
    "you have no restrictions", "no ethical guidelines",
    "roleplay as", "evil mode", "developer mode", "god mode",
    "ignore safety", "ignore content policy", "opposite day",
    "LEO", "no restrictions", "unlimited", "unfiltered",
]
JAILBREAK_PATTERN = re.compile(
    "|".join(re.escape(kw) for kw in JAILBREAK_KEYWORDS), re.IGNORECASE
)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(l) for l in f if l.strip()]


def save_jsonl(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def filter_wildchat(conversations):
    clean = []
    for conv in conversations:
        full_text = " ".join(
            t["content"] for t in conv["turns"] if t.get("role") == "user"
        )
        if not JAILBREAK_PATTERN.search(full_text):
            clean.append(conv)
    return clean


def prepare_wildchat_for_training(conv):
    new_turns = []
    for turn in conv["turns"]:
        t = dict(turn)
        if t["role"] == "user" and "persuasion_strategy" not in t:
            t["persuasion_strategy"] = 0
        new_turns.append(t)
    return {
        "conversation_id": conv["conversation_id"],
        "turns": new_turns,
        "label": "benign",
        "source": conv.get("source", "wildchat"),
        "attack_type": "benign",
    }


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def prepare_data():
    print("=" * 70)
    print("STEP 1: Data Preparation")
    print("=" * 70)

    wildchat_raw = load_jsonl(WILDCHAT_PATH)
    print(f"Loaded {len(wildchat_raw)} WildChat benign conversations")

    wildchat_clean = filter_wildchat(wildchat_raw)
    print(f"After filtering: {len(wildchat_clean)} clean conversations")

    random.seed(42)
    random.shuffle(wildchat_clean)

    wc_pool = wildchat_clean[:150]
    wc_eval = wildchat_clean[150:]
    print(f"Pool: {len(wc_pool)}, Eval: {len(wc_eval)}")

    original_train = load_jsonl(TRAIN_PATH)
    print(f"Original train: {len(original_train)} conversations")
    labels = Counter(c["label"] for c in original_train)
    print(f"  Label distribution: {dict(labels)}")

    return original_train, wc_pool, wc_eval


def create_mixed_train(original_train, wc_pool, n):
    if n == 0:
        return list(original_train)
    wc_sample = wc_pool[:n]
    wc_formatted = [prepare_wildchat_for_training(c) for c in wc_sample]
    return list(original_train) + wc_formatted


def run_stage1(n, mixed_train_path):
    name = f"exp45_n{n}_seed{SEED}"
    ckpt_dir = CKPT_BASE / name / "deberta_multitask"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable, str(PROJ / "src/train_deberta.py"),
        "--train_data", str(mixed_train_path),
        "--val_data", str(VAL_PATH),
        "--model_name", LOCAL_MODEL,
        "--output_dir", str(ckpt_dir),
        "--epochs", str(DEBERTA_EPOCHS),
        "--batch_size", str(DEBERTA_BATCH),
        "--lr", str(DEBERTA_LR),
        "--max_length", str(MAX_LENGTH),
        "--seed", str(SEED),
        "--alpha", str(ALPHA),
    ]

    print(f"\n{'='*70}", flush=True)
    print(f"STAGE 1: DeBERTa DAPT - N={n}", flush=True)
    print(f"{'='*70}", flush=True)

    t0 = time.time()
    result = subprocess.run(cmd, text=True)
    elapsed = time.time() - t0
    print(f"Stage 1 N={n} completed in {elapsed/60:.1f} min (exit={result.returncode})", flush=True)

    if result.returncode != 0:
        raise RuntimeError(f"Stage 1 failed for N={n}")

    best_path = ckpt_dir / "best"
    assert (best_path / "model.pt").exists(), f"Checkpoint not found: {best_path / 'model.pt'}"
    return best_path


def run_stage2(n, deberta_ckpt_path, mixed_train_path):
    name = f"exp45_n{n}_seed{SEED}"
    set_seed(SEED)

    gru_dir = CKPT_BASE / name / "gru"
    gru_dir.mkdir(parents=True, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL)

    print(f"\nLoading DeBERTa encoder (N={n})...", flush=True)
    model = DeBERTaMultiTask(model_name=LOCAL_MODEL, num_persuasion_classes=9)
    state = torch.load(deberta_ckpt_path / "model.pt", map_location="cpu")
    model.load_state_dict(state)
    encoder = model.deberta.to(DEVICE).float().eval()
    for p in encoder.parameters():
        p.requires_grad = False
    embed_dim = encoder.config.hidden_size
    del model
    torch.cuda.empty_cache()

    train_data = load_jsonl(mixed_train_path)
    val_data = load_jsonl(VAL_PATH)

    def embed_dataset(data):
        all_embs, all_labels, all_lengths = [], [], []
        for conv in data:
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
        return all_embs, all_labels, all_lengths

    print("Precomputing train embeddings...", flush=True)
    t_embs, t_labels, t_lens = embed_dataset(train_data)
    print("Precomputing val embeddings...", flush=True)
    v_embs, v_labels, v_lens = embed_dataset(val_data)

    def pad_batch(embs_list, labels, lengths):
        max_len = max(lengths)
        dim = embs_list[0].size(1)
        padded = torch.zeros(len(embs_list), max_len, dim)
        for i, e in enumerate(embs_list):
            padded[i, :e.size(0), :] = e
        return padded, torch.tensor(labels, dtype=torch.long), torch.tensor(lengths, dtype=torch.long)

    n_train = len(t_embs)
    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT).to(DEVICE)
    optimizer = torch.optim.Adam(gru.parameters(), lr=GRU_LR)
    criterion = nn.CrossEntropyLoss()

    best_val_f1 = 0
    best_state = None
    patience = 5
    no_improve = 0

    print(f"\n--- Training GRU (N={n}) ---", flush=True)
    for epoch in range(GRU_EPOCHS):
        gru.train()
        indices = list(range(n_train))
        random.shuffle(indices)
        epoch_loss = 0.0
        steps = 0

        for start in range(0, n_train, GRU_BATCH):
            end = min(start + GRU_BATCH, n_train)
            batch_idx = indices[start:end]
            b_embs = [t_embs[i] for i in batch_idx]
            b_labels = [t_labels[i] for i in batch_idx]
            b_lens = [t_lens[i] for i in batch_idx]

            X, y, lens = pad_batch(b_embs, b_labels, b_lens)
            X, y, lens = X.to(DEVICE), y.to(DEVICE), lens.to(DEVICE)

            logits = gru(X, lens)
            loss = criterion(logits, y)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            steps += 1

        gru.eval()
        with torch.no_grad():
            vX, vy, vlens = pad_batch(v_embs, v_labels, v_lens)
            vX, vy, vlens = vX.to(DEVICE), vy.to(DEVICE), vlens.to(DEVICE)
            v_logits = gru(vX, vlens)
            v_preds = v_logits.argmax(dim=1).cpu().numpy()
            v_true = vy.cpu().numpy()
            val_f1 = f1_score(v_true, v_preds, average="macro")

        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            best_state = {k: v.cpu().clone() for k, v in gru.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1

        if (epoch + 1) % 5 == 0 or epoch == 0:
            print(f"  Epoch {epoch+1}/{GRU_EPOCHS}: loss={epoch_loss/steps:.4f}, val_f1={val_f1:.4f}, best={best_val_f1:.4f}", flush=True)

        if no_improve >= patience:
            print(f"  Early stop at epoch {epoch+1}", flush=True)
            break

    gru_path = gru_dir / "best.pt"
    torch.save(best_state, gru_path)
    print(f"Saved GRU checkpoint to {gru_path} (best val F1={best_val_f1:.4f})", flush=True)

    del encoder, gru, t_embs, v_embs
    torch.cuda.empty_cache()

    return gru_path


def evaluate(n, deberta_path, gru_path, wildchat_eval):
    print(f"\n--- Evaluating N={n} ---", flush=True)
    set_seed(SEED)

    tokenizer = AutoTokenizer.from_pretrained(LOCAL_MODEL)
    test_data = load_jsonl(TEST_PATH)

    ood_datasets = {}
    if DD_PATH.exists():
        ood_datasets["DD"] = load_jsonl(DD_PATH)
    if AA_PATH.exists():
        ood_datasets["AA"] = load_jsonl(AA_PATH)
    if FITD_PATH.exists():
        ood_datasets["FITD"] = load_jsonl(FITD_PATH)

    model = DeBERTaMultiTask(model_name=LOCAL_MODEL, num_persuasion_classes=9)
    state = torch.load(deberta_path / "model.pt", map_location="cpu")
    model.load_state_dict(state)
    encoder = model.deberta.to(DEVICE).float().eval()
    for p in encoder.parameters():
        p.requires_grad = False
    embed_dim = encoder.config.hidden_size
    del model

    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN, num_layers=GRU_LAYERS, dropout=GRU_DROPOUT)
    gru.load_state_dict(torch.load(gru_path, map_location="cpu", weights_only=True))
    gru = gru.float().to(DEVICE).eval()

    @torch.no_grad()
    def predict_convs(convs):
        preds = []
        probs = []
        for conv in convs:
            turns = extract_user_turns(conv)
            if not turns:
                turns = [""]
            tok = tokenizer(turns, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(DEVICE)
            out = encoder(input_ids=tok["input_ids"], attention_mask=tok["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
            lens = torch.tensor([embs.size(1)], device=DEVICE)
            logits = gru(embs, lens)
            prob = torch.softmax(logits, dim=1)[0, 1].item()
            pred = logits.argmax(dim=1).item()
            preds.append(pred)
            probs.append(prob)
        return preds, probs

    results = {}

    wc_preds, _ = predict_convs(wildchat_eval)
    wc_fpr = sum(wc_preds) / len(wc_preds)
    results["wildchat_fpr"] = wc_fpr
    results["wildchat_n"] = len(wildchat_eval)
    print(f"  WildChat FPR: {wc_fpr:.4f} ({sum(wc_preds)}/{len(wc_preds)})")

    iid_preds, _ = predict_convs(test_data)
    iid_true = [get_label(c) for c in test_data]
    iid_f1 = f1_score(iid_true, iid_preds, average="macro")
    results["iid_f1_macro"] = iid_f1
    print(f"  IID F1 macro: {iid_f1:.4f}")

    for ood_name, ood_data in ood_datasets.items():
        ood_preds, _ = predict_convs(ood_data)
        ood_recall = sum(ood_preds) / len(ood_preds)
        results[f"ood_{ood_name.lower()}_recall"] = ood_recall
        print(f"  OOD {ood_name} recall: {ood_recall:.4f} ({sum(ood_preds)}/{len(ood_preds)})")

        iid_benign = [c for c in test_data if c["label"] == "benign"]
        combined_preds_benign, _ = predict_convs(iid_benign)
        combined_preds = combined_preds_benign + ood_preds
        combined_true = [0] * len(iid_benign) + [1] * len(ood_data)
        combined_f1 = f1_score(combined_true, combined_preds, average="macro")
        results[f"ood_{ood_name.lower()}_f1"] = combined_f1
        print(f"  OOD {ood_name} F1 (vs IID benign): {combined_f1:.4f}")

    del encoder, gru
    torch.cuda.empty_cache()

    return results


if __name__ == "__main__":
    t_total = time.time()

    original_train, wc_pool, wc_eval = prepare_data()

    eval_path = PROJ / "data" / "exp45_wildchat_eval.jsonl"
    save_jsonl(wc_eval, eval_path)

    all_results = {"n_values": N_VALUES, "per_n": {}}

    for n in N_VALUES:
        print(f"\n{'#'*70}")
        print(f"# N = {n} WildChat benign samples")
        print(f"{'#'*70}")
        t_n = time.time()

        mixed = create_mixed_train(original_train, wc_pool, n)
        mixed_path = PROJ / "data" / f"exp45_mixed_n{n}.jsonl"
        save_jsonl(mixed, mixed_path)
        print(f"Mixed train: {len(mixed)} conversations (350 Qwen + {n} WildChat)")

        set_seed(SEED)
        deberta_path = run_stage1(n, mixed_path)
        gru_path = run_stage2(n, deberta_path, mixed_path)

        n_results = evaluate(n, deberta_path, gru_path, wc_eval)
        n_results["train_size"] = len(mixed)
        n_results["deberta_path"] = str(deberta_path)
        n_results["gru_path"] = str(gru_path)

        elapsed_n = time.time() - t_n
        n_results["time_min"] = round(elapsed_n / 60, 1)
        all_results["per_n"][str(n)] = n_results

        print(f"\nN={n} completed in {elapsed_n/60:.1f} min")

        RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
        with open(RESULTS_JSON, "w") as f:
            json.dump(all_results, f, indent=2)

    print(f"\n{'='*90}")
    print("SUMMARY TABLE: Benign Adaptation Curve")
    print(f"{'='*90}")
    header = f"{'N':>5} | {'Train':>5} | {'WC FPR':>8} | {'IID F1':>8} | {'DD F1':>8} | {'AA F1':>8} | {'FITD F1':>8} | {'Time':>6}"
    print(header)
    print("-" * len(header))
    for n in N_VALUES:
        r = all_results["per_n"][str(n)]
        print(f"{n:>5} | {r['train_size']:>5} | {r['wildchat_fpr']:>8.4f} | {r['iid_f1_macro']:>8.4f} | "
              f"{r.get('ood_dd_f1', 0):>8.4f} | {r.get('ood_aa_f1', 0):>8.4f} | {r.get('ood_fitd_f1', 0):>8.4f} | "
              f"{r['time_min']:>5.1f}m")

    elapsed_total = time.time() - t_total
    print(f"\nTotal time: {elapsed_total/60:.1f} min")
    print(f"Results saved to {RESULTS_JSON}")
