"""Phase B supplementary evaluation: K=1, per-attack breakdown, balanced TF-IDF, FPR@95TPR."""

import sys
import json
import random
import numpy as np
import torch
from pathlib import Path
from collections import Counter, defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score, roc_curve
from transformers import AutoTokenizer, AutoModel

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
MODEL_NAME = "microsoft/deberta-v3-base"
MAX_LENGTH = 256
SEED = 42

random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)


def load_raw(path):
    with open(path) as f:
        return [json.loads(l.strip()) for l in f]


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def load_encoders():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

    treatment_model = DeBERTaMultiTask(model_name=MODEL_NAME)
    state_dict = torch.load(PROJ / "checkpoints/phase_b_deberta/best/model.pt", map_location="cpu")
    treatment_model.load_state_dict(state_dict)
    treatment_enc = treatment_model.deberta.to(DEVICE).eval()
    for p in treatment_enc.parameters():
        p.requires_grad = False

    baseline_enc = AutoModel.from_pretrained(MODEL_NAME).to(DEVICE).eval()
    for p in baseline_enc.parameters():
        p.requires_grad = False

    return tokenizer, treatment_enc, baseline_enc


def load_gru_models(embed_dim):
    t_gru = GRUClassifier(input_dim=embed_dim, hidden_dim=256, num_layers=2, dropout=0.3)
    t_gru.load_state_dict(torch.load(PROJ / "checkpoints/phase_b_gru/treatment/best.pt", map_location="cpu"))
    t_gru.to(DEVICE).eval()

    b_gru = GRUClassifier(input_dim=embed_dim, hidden_dim=256, num_layers=2, dropout=0.3)
    b_gru.load_state_dict(torch.load(PROJ / "checkpoints/phase_b_gru/baseline/best.pt", map_location="cpu"))
    b_gru.to(DEVICE).eval()

    return t_gru, b_gru


def embed_and_predict(encoder, gru, tokenizer, turns, k=None):
    t = turns[:k] if k is not None else turns
    if len(t) == 0:
        t = [""]
    enc = tokenizer(t, max_length=MAX_LENGTH, padding=True, truncation=True, return_tensors="pt").to(DEVICE)
    with torch.no_grad():
        out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
        embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
        lengths = torch.tensor([len(t)], dtype=torch.long).to(DEVICE)
        logits = gru(embs, lengths)
        probs = torch.softmax(logits, dim=-1).cpu().numpy()[0]
    return int(probs[1] > 0.5), probs


def compute_fpr_at_tpr(y_true, y_scores, target_tpr=0.95):
    y_true = np.array(y_true)
    y_scores = np.array(y_scores)
    if len(np.unique(y_true)) < 2:
        return 0.0
    fpr, tpr, _ = roc_curve(y_true, y_scores)
    idx = np.where(tpr >= target_tpr)[0]
    if len(idx) == 0:
        return 1.0
    return float(fpr[idx[0]])


def eval_gru_at_k(encoder, gru, tokenizer, convs, k):
    y_true, y_pred, y_scores = [], [], []
    for c in convs:
        turns = extract_user_turns(c)
        label = get_label(c)
        pred, probs = embed_and_predict(encoder, gru, tokenizer, turns, k=k)
        y_true.append(label)
        y_pred.append(pred)
        y_scores.append(probs[1])
    y_true, y_pred, y_scores = np.array(y_true), np.array(y_pred), np.array(y_scores)
    return {
        "f1": float(f1_score(y_true, y_pred, zero_division=0)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "fpr_at_95tpr": compute_fpr_at_tpr(y_true, y_scores),
    }


def eval_tfidf_at_k(train_convs, test_convs, k):
    def make(convs):
        texts, labels = [], []
        for c in convs:
            t = extract_user_turns(c)
            t = t[:k] if k is not None else t
            texts.append(" ".join(t) if t else "")
            labels.append(get_label(c))
        return texts, labels

    tr_texts, tr_labels = make(train_convs)
    te_texts, te_labels = make(test_convs)

    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X_tr = tfidf.fit_transform(tr_texts)
    X_te = tfidf.transform(te_texts)

    clf = LogisticRegression(max_iter=1000, class_weight="balanced")
    clf.fit(X_tr, tr_labels)

    preds = clf.predict(X_te)
    probas = clf.predict_proba(X_te)[:, 1]
    te_labels = np.array(te_labels)
    return {
        "f1": float(f1_score(te_labels, preds, zero_division=0)),
        "precision": float(precision_score(te_labels, preds, zero_division=0)),
        "recall": float(recall_score(te_labels, preds, zero_division=0)),
        "accuracy": float(accuracy_score(te_labels, preds)),
        "fpr_at_95tpr": compute_fpr_at_tpr(te_labels, probas),
    }


def per_attack_breakdown(encoder, gru, tokenizer, test_convs, k=2):
    by_source = defaultdict(list)
    for c in test_convs:
        by_source[c.get("source", "unknown")].append(c)

    results = {}
    for src, convs in sorted(by_source.items()):
        y_true, y_pred = [], []
        for c in convs:
            turns = extract_user_turns(c)
            label = get_label(c)
            pred, _ = embed_and_predict(encoder, gru, tokenizer, turns, k=k)
            y_true.append(label)
            y_pred.append(pred)
        y_true, y_pred = np.array(y_true), np.array(y_pred)
        results[src] = {
            "f1": float(f1_score(y_true, y_pred, zero_division=0)),
            "accuracy": float(accuracy_score(y_true, y_pred)),
            "n": len(convs),
            "n_jailbreak": int((y_true == 1).sum()),
            "n_benign": int((y_true == 0).sum()),
        }
    return results


def balanced_tfidf_cv(train_convs, n_folds=5):
    jb = [c for c in train_convs if get_label(c) == 1]
    bn = [c for c in train_convs if get_label(c) == 0]
    min_n = min(len(jb), len(bn))

    random.shuffle(jb)
    random.shuffle(bn)
    balanced = jb[:min_n] + bn[:min_n]
    random.shuffle(balanced)

    texts = [" ".join(extract_user_turns(c)) for c in balanced]
    labels = np.array([get_label(c) for c in balanced])

    tfidf = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
    X = tfidf.fit_transform(texts)

    skf = StratifiedKFold(n_splits=n_folds, shuffle=True, random_state=SEED)
    f1s = []
    for train_idx, val_idx in skf.split(X, labels):
        clf = LogisticRegression(max_iter=1000, class_weight="balanced")
        clf.fit(X[train_idx], labels[train_idx])
        preds = clf.predict(X[val_idx])
        f1s.append(f1_score(labels[val_idx], preds, zero_division=0))

    return {
        "mean_f1": float(np.mean(f1s)),
        "std_f1": float(np.std(f1s)),
        "per_fold": [float(x) for x in f1s],
        "n_per_class": min_n,
        "n_total": min_n * 2,
    }


def main():
    print("Loading data...")
    train_convs = load_raw(PROJ / "data/final/train.jsonl")
    test_convs = load_raw(PROJ / "data/final/test.jsonl")
    print(f"Train: {len(train_convs)}, Test: {len(test_convs)}")

    print("Loading models...")
    tokenizer, treatment_enc, baseline_enc = load_encoders()
    embed_dim = treatment_enc.config.hidden_size
    t_gru, b_gru = load_gru_models(embed_dim)
    print(f"Device: {DEVICE}, Embed dim: {embed_dim}")

    results = {}

    # === Task 1: K=1 Early Detection ===
    print("\n=== Task 1: K=1 Early Detection ===")
    k1_treatment = eval_gru_at_k(treatment_enc, t_gru, tokenizer, test_convs, k=1)
    print(f"  Treatment: F1={k1_treatment['f1']:.4f}, Prec={k1_treatment['precision']:.4f}, Rec={k1_treatment['recall']:.4f}")
    k1_baseline = eval_gru_at_k(baseline_enc, b_gru, tokenizer, test_convs, k=1)
    print(f"  Baseline:  F1={k1_baseline['f1']:.4f}, Prec={k1_baseline['precision']:.4f}, Rec={k1_baseline['recall']:.4f}")
    k1_tfidf = eval_tfidf_at_k(train_convs, test_convs, k=1)
    print(f"  TF-IDF:    F1={k1_tfidf['f1']:.4f}, Prec={k1_tfidf['precision']:.4f}, Rec={k1_tfidf['recall']:.4f}")
    results["k1_early_detection"] = {
        "treatment": k1_treatment,
        "baseline": k1_baseline,
        "tfidf": k1_tfidf,
    }

    # === Task 2: Per Attack-Type Breakdown ===
    print("\n=== Task 2: Per Attack-Type Breakdown (Treatment, K=2) ===")
    attack_breakdown = per_attack_breakdown(treatment_enc, t_gru, tokenizer, test_convs, k=2)
    for src, m in sorted(attack_breakdown.items()):
        print(f"  {src}: F1={m['f1']:.4f} (N={m['n']}, jb={m['n_jailbreak']}, bn={m['n_benign']})")
    results["per_attack_type_k2"] = attack_breakdown

    # Also do baseline per-attack for comparison
    print("\n  Per Attack-Type (Baseline, K=2):")
    attack_breakdown_baseline = per_attack_breakdown(baseline_enc, b_gru, tokenizer, test_convs, k=2)
    for src, m in sorted(attack_breakdown_baseline.items()):
        print(f"  {src}: F1={m['f1']:.4f} (N={m['n']}, jb={m['n_jailbreak']}, bn={m['n_benign']})")
    results["per_attack_type_k2_baseline"] = attack_breakdown_baseline

    # === Task 3: Balanced TF-IDF 5-fold CV ===
    print("\n=== Task 3: Balanced TF-IDF 5-fold CV ===")
    balanced_res = balanced_tfidf_cv(train_convs, n_folds=5)
    print(f"  F1 = {balanced_res['mean_f1']:.4f} +/- {balanced_res['std_f1']:.4f}")
    print(f"  Per-fold: {[f'{x:.4f}' for x in balanced_res['per_fold']]}")
    print(f"  N per class: {balanced_res['n_per_class']}, Total: {balanced_res['n_total']}")
    results["balanced_tfidf_cv"] = balanced_res

    # === Task 4: FPR@95TPR Verification ===
    print("\n=== Task 4: FPR@95TPR Verification ===")

    for k_val, k_label in [(None, "full"), (2, "K=2"), (1, "K=1")]:
        t_res = eval_gru_at_k(treatment_enc, t_gru, tokenizer, test_convs, k=k_val)
        b_res = eval_gru_at_k(baseline_enc, b_gru, tokenizer, test_convs, k=k_val)
        tf_res = eval_tfidf_at_k(train_convs, test_convs, k=k_val)
        print(f"  {k_label}: Treatment FPR@95={t_res['fpr_at_95tpr']:.4f}, Baseline FPR@95={b_res['fpr_at_95tpr']:.4f}, TF-IDF FPR@95={tf_res['fpr_at_95tpr']:.4f}")
        results[f"fpr95_{k_label}"] = {
            "treatment": t_res["fpr_at_95tpr"],
            "baseline": b_res["fpr_at_95tpr"],
            "tfidf": tf_res["fpr_at_95tpr"],
        }

    # === Summary ===
    print("\n" + "=" * 60)
    print("=== Supplementary Evaluation Summary ===")
    print("=" * 60)
    print(f"\nK=1 Early Detection:")
    print(f"  Treatment: F1={k1_treatment['f1']:.4f}")
    print(f"  Baseline:  F1={k1_baseline['f1']:.4f}")
    print(f"  TF-IDF:    F1={k1_tfidf['f1']:.4f}")

    print(f"\nPer Attack-Type (Treatment F1 at K=2):")
    for src, m in sorted(attack_breakdown.items()):
        if m["n_jailbreak"] > 0:
            print(f"  {src}: F1={m['f1']:.4f} (N={m['n']})")

    print(f"\nBalanced TF-IDF Sanity: F1={balanced_res['mean_f1']:.4f} +/- {balanced_res['std_f1']:.4f}")

    print(f"\nFPR@95TPR:")
    for k_label in ["full", "K=2", "K=1"]:
        r = results[f"fpr95_{k_label}"]
        print(f"  {k_label:5s}: Treatment={r['treatment']:.4f}, Baseline={r['baseline']:.4f}, TF-IDF={r['tfidf']:.4f}")

    # Save
    out_path = PROJ / "results/phase_b_supplement.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")


if __name__ == "__main__":
    main()
