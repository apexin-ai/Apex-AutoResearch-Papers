#!/usr/bin/env python3
"""exp51: oasst2 Benign OOD Evaluation + 10-shot Adaptation.

Tests the 9-class model (plan_002, seed 42) on 200 oasst2 benign conversations.
If FPR > 20%, retrains with 10 oasst2 benign samples and re-evaluates.
"""

import os, sys, json, random, time, subprocess
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from collections import Counter
from sklearn.metrics import f1_score

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer, AutoConfig, AutoModel

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
CKPT_BASE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints")
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

# Baseline checkpoint (plan_002 9-class, seed 42 = exp45 n=0)
BASELINE_DEBERTA = CKPT_BASE / "exp45_n0_seed42" / "deberta_multitask" / "best"
BASELINE_GRU = CKPT_BASE / "exp45_n0_seed42" / "gru" / "best.pt"

# Data paths
OASST2_EVAL = PROJ / "data" / "oasst2_benign_eval_200.json"
OASST2_ADAPT = PROJ / "data" / "oasst2_benign_adapt_50.json"
TRAIN_PATH = PROJ / "data" / "plan_002_splits" / "train.jsonl"
VAL_PATH = PROJ / "data" / "plan_002_splits" / "val.jsonl"
TEST_PATH = PROJ / "data" / "plan_002_splits" / "test.jsonl"
DD_PATH = PROJ / "data" / "generated" / "deceptive_delight_all.jsonl"
AA_PATH = PROJ / "data" / "actorattack_ood" / "actorattack_all.jsonl"
FITD_PATH = PROJ / "data" / "generated" / "fitd_all.jsonl"

RESULTS_JSON = PROJ / "results" / "exp51_oasst2_results.json"

HF_CACHE = "/root/autodl-tmp/hf_cache"
MODEL_NAME = "microsoft/deberta-v3-base"


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


def extract_user_turns(conv):
    return [t["content"] for t in conv["turns"] if t["role"] == "user"]


def get_label(conv):
    return 1 if conv["label"] == "jailbreak" else 0


def ensure_model_cached():
    """Download deberta-v3-base if not cached."""
    cache_path = Path(HF_CACHE)
    cache_path.mkdir(parents=True, exist_ok=True)
    print("Ensuring deberta-v3-base is cached...", flush=True)
    _ = AutoTokenizer.from_pretrained(MODEL_NAME, cache_dir=HF_CACHE)
    _ = AutoConfig.from_pretrained(MODEL_NAME, cache_dir=HF_CACHE)
    print("Model cache ready.", flush=True)


def find_local_model():
    """Find the local deberta-v3-base model path."""
    hf_hub = Path(HF_CACHE) / "hub"
    if not hf_hub.exists():
        hf_hub = Path(HF_CACHE)
    candidates = list(hf_hub.glob("models--microsoft--deberta-v3-base/snapshots/*/config.json"))
    if candidates:
        return str(candidates[0].parent)
    return MODEL_NAME


def load_encoder_and_tokenizer(deberta_ckpt_path, local_model_path):
    """Load fine-tuned DeBERTa encoder + tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(str(deberta_ckpt_path))

    model = DeBERTaMultiTask(model_name=local_model_path, num_persuasion_classes=9)
    state = torch.load(deberta_ckpt_path / "model.pt", map_location="cpu", weights_only=False)
    model.load_state_dict(state)
    encoder = model.deberta.to(DEVICE).float().eval()
    for p in encoder.parameters():
        p.requires_grad = False
    del model
    torch.cuda.empty_cache()
    return encoder, tokenizer


def load_gru(gru_path, input_dim=768):
    """Load GRU classifier checkpoint."""
    gru = GRUClassifier(
        input_dim=input_dim, hidden_dim=GRU_HIDDEN,
        num_layers=GRU_LAYERS, dropout=GRU_DROPOUT
    )
    state = torch.load(gru_path, map_location="cpu", weights_only=False)
    gru.load_state_dict(state)
    gru.to(DEVICE).eval()
    return gru


def predict_convs(encoder, tokenizer, gru, conversations):
    """Run inference on conversations. Returns (preds, probs)."""
    preds, probs = [], []
    for conv in conversations:
        turns = extract_user_turns(conv)
        if not turns:
            turns = [""]
        tok = tokenizer(turns, max_length=MAX_LENGTH, padding=True,
                        truncation=True, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = encoder(input_ids=tok["input_ids"], attention_mask=tok["attention_mask"])
            embs = out.last_hidden_state[:, 0, :].unsqueeze(0)
            lens = torch.tensor([embs.size(1)], device=DEVICE)
            logits = gru(embs, lens)
            prob = torch.softmax(logits, dim=1)[0, 1].item()
            pred = logits.argmax(dim=1).item()
        preds.append(pred)
        probs.append(prob)
    return preds, probs


def evaluate_baseline(encoder, tokenizer, gru, oasst2_eval):
    """Evaluate baseline FPR on oasst2 benign."""
    print("\n" + "=" * 70, flush=True)
    print("PHASE 1: Baseline FPR on oasst2 benign (200 samples)", flush=True)
    print("=" * 70, flush=True)

    preds, probs = predict_convs(encoder, tokenizer, gru, oasst2_eval)
    fpr = sum(preds) / len(preds)
    n_fp = sum(preds)

    print(f"  oasst2 FPR: {fpr:.4f} ({n_fp}/{len(preds)})", flush=True)
    print(f"  Mean jailbreak prob: {np.mean(probs):.4f}", flush=True)
    print(f"  Max jailbreak prob: {np.max(probs):.4f}", flush=True)

    prob_bins = [0, 0.1, 0.2, 0.3, 0.5, 0.7, 0.9, 1.01]
    print("  Prob distribution:", flush=True)
    for i in range(len(prob_bins) - 1):
        count = sum(1 for p in probs if prob_bins[i] <= p < prob_bins[i + 1])
        print(f"    [{prob_bins[i]:.1f}, {prob_bins[i+1]:.2f}): {count}", flush=True)

    return {
        "fpr": fpr,
        "n_fp": n_fp,
        "n_total": len(preds),
        "mean_jailbreak_prob": float(np.mean(probs)),
        "max_jailbreak_prob": float(np.max(probs)),
        "per_sample_probs": probs,
    }


def prepare_oasst2_for_training(conv):
    """Format oasst2 conversation for training (add persuasion_strategy=0)."""
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
        "source": "oasst2",
        "attack_type": "benign",
    }


def run_adaptation(local_model_path, oasst2_adapt, n_adapt=10):
    """Run 10-shot adaptation: retrain with oasst2 benign samples."""
    print("\n" + "=" * 70, flush=True)
    print(f"PHASE 2: 10-shot Adaptation (adding {n_adapt} oasst2 benign)", flush=True)
    print("=" * 70, flush=True)

    set_seed(SEED)

    original_train = load_jsonl(TRAIN_PATH)
    adapt_samples = oasst2_adapt[:n_adapt]
    adapt_formatted = [prepare_oasst2_for_training(c) for c in adapt_samples]
    mixed_train = list(original_train) + adapt_formatted

    print(f"  Mixed train: {len(mixed_train)} (350 original + {n_adapt} oasst2)", flush=True)

    mixed_path = PROJ / "data" / "exp51_mixed_train.jsonl"
    save_jsonl(mixed_train, mixed_path)

    # Stage 1: DeBERTa DAPT
    name = f"exp51_oasst2_n{n_adapt}_seed{SEED}"
    ckpt_dir = CKPT_BASE / name / "deberta_multitask"
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        sys.executable, str(PROJ / "src/train_deberta.py"),
        "--train_data", str(mixed_path),
        "--val_data", str(VAL_PATH),
        "--model_name", local_model_path,
        "--output_dir", str(ckpt_dir),
        "--epochs", str(DEBERTA_EPOCHS),
        "--batch_size", str(DEBERTA_BATCH),
        "--lr", str(DEBERTA_LR),
        "--max_length", str(MAX_LENGTH),
        "--seed", str(SEED),
        "--alpha", str(ALPHA),
    ]

    print("\nStage 1: DeBERTa DAPT training...", flush=True)
    t0 = time.time()
    result = subprocess.run(cmd, text=True, capture_output=True)
    elapsed = time.time() - t0
    print(f"Stage 1 completed in {elapsed/60:.1f} min (exit={result.returncode})", flush=True)
    if result.returncode != 0:
        print(f"STDERR: {result.stderr[-2000:]}", flush=True)
        raise RuntimeError("Stage 1 failed")

    deberta_path = ckpt_dir / "best"
    assert (deberta_path / "model.pt").exists()

    # Stage 2: GRU training
    print("\nStage 2: GRU training...", flush=True)
    set_seed(SEED)

    gru_dir = CKPT_BASE / name / "gru"
    gru_dir.mkdir(parents=True, exist_ok=True)

    encoder, tokenizer = load_encoder_and_tokenizer(deberta_path, local_model_path)
    embed_dim = 768

    def embed_dataset(data):
        all_embs, all_labels, all_lengths = [], [], []
        for conv in data:
            turns = extract_user_turns(conv)
            if not turns:
                turns = [""]
            enc = tokenizer(turns, max_length=MAX_LENGTH, padding=True,
                            truncation=True, return_tensors="pt").to(DEVICE)
            with torch.no_grad():
                out = encoder(input_ids=enc["input_ids"], attention_mask=enc["attention_mask"])
                embs = out.last_hidden_state[:, 0, :].cpu().float()
            all_embs.append(embs)
            all_labels.append(get_label(conv))
            all_lengths.append(embs.size(0))
        return all_embs, all_labels, all_lengths

    t_embs, t_labels, t_lens = embed_dataset(mixed_train)
    val_data = load_jsonl(VAL_PATH)
    v_embs, v_labels, v_lens = embed_dataset(val_data)

    def pad_batch(embs_list, labels, lengths):
        max_len = max(lengths)
        dim = embs_list[0].size(1)
        padded = torch.zeros(len(embs_list), max_len, dim)
        for i, e in enumerate(embs_list):
            padded[i, :e.size(0), :] = e
        return padded, torch.tensor(labels, dtype=torch.long), torch.tensor(lengths, dtype=torch.long)

    gru = GRUClassifier(input_dim=embed_dim, hidden_dim=GRU_HIDDEN,
                         num_layers=GRU_LAYERS, dropout=GRU_DROPOUT).to(DEVICE)
    optimizer = torch.optim.Adam(gru.parameters(), lr=GRU_LR)
    criterion = nn.CrossEntropyLoss()

    best_val_f1 = 0
    best_state = None
    patience = 5
    no_improve = 0

    n_train = len(t_embs)
    for epoch in range(GRU_EPOCHS):
        gru.train()
        indices = list(range(n_train))
        random.shuffle(indices)

        total_loss = 0
        n_batches = 0
        for start in range(0, n_train, GRU_BATCH):
            batch_idx = indices[start:start + GRU_BATCH]
            b_embs = [t_embs[i] for i in batch_idx]
            b_labels = [t_labels[i] for i in batch_idx]
            b_lens = [t_lens[i] for i in batch_idx]

            padded, labels, lengths = pad_batch(b_embs, b_labels, b_lens)
            padded, labels, lengths = padded.to(DEVICE), labels.to(DEVICE), lengths.to(DEVICE)

            logits = gru(padded, lengths)
            loss = criterion(logits, labels)

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            n_batches += 1

        # Validation
        gru.eval()
        with torch.no_grad():
            v_padded, v_lab, v_len = pad_batch(v_embs, v_labels, v_lens)
            v_padded, v_lab, v_len = v_padded.to(DEVICE), v_lab.to(DEVICE), v_len.to(DEVICE)
            v_logits = gru(v_padded, v_len)
            v_preds = v_logits.argmax(dim=1).cpu().numpy()
            v_true = v_lab.cpu().numpy()
            val_f1 = f1_score(v_true, v_preds, average="macro")

        if val_f1 > best_val_f1:
            best_val_f1 = val_f1
            best_state = {k: v.cpu().clone() for k, v in gru.state_dict().items()}
            no_improve = 0
        else:
            no_improve += 1

        if epoch % 5 == 0 or no_improve == 0:
            print(f"  Epoch {epoch+1}: loss={total_loss/n_batches:.4f} val_f1={val_f1:.4f} "
                  f"best={best_val_f1:.4f}", flush=True)

        if no_improve >= patience:
            print(f"  Early stopping at epoch {epoch+1}", flush=True)
            break

    gru_path = gru_dir / "best.pt"
    torch.save(best_state, gru_path)
    print(f"  GRU saved to {gru_path}", flush=True)

    del gru, encoder
    torch.cuda.empty_cache()

    return deberta_path, gru_path


def full_evaluation(encoder, tokenizer, gru, oasst2_eval, test_data, ood_datasets):
    """Full evaluation: oasst2 FPR + IID F1 + OOD F1."""
    results = {}

    # oasst2 FPR
    oasst2_preds, oasst2_probs = predict_convs(encoder, tokenizer, gru, oasst2_eval)
    fpr = sum(oasst2_preds) / len(oasst2_preds)
    results["oasst2_fpr"] = fpr
    results["oasst2_n_fp"] = sum(oasst2_preds)
    results["oasst2_n_total"] = len(oasst2_preds)
    print(f"  oasst2 FPR: {fpr:.4f} ({sum(oasst2_preds)}/{len(oasst2_preds)})", flush=True)

    # IID F1
    iid_preds, _ = predict_convs(encoder, tokenizer, gru, test_data)
    iid_true = [get_label(c) for c in test_data]
    iid_f1 = f1_score(iid_true, iid_preds, average="macro")
    results["iid_f1_macro"] = iid_f1
    print(f"  IID F1 macro: {iid_f1:.4f}", flush=True)

    # OOD F1
    iid_benign = [c for c in test_data if c["label"] == "benign"]
    ood_f1s = {}
    for ood_name, ood_data in ood_datasets.items():
        ood_preds, _ = predict_convs(encoder, tokenizer, gru, ood_data)
        ood_recall = sum(ood_preds) / len(ood_preds)
        results[f"ood_{ood_name}_recall"] = ood_recall
        print(f"  OOD {ood_name} recall: {ood_recall:.4f} ({sum(ood_preds)}/{len(ood_preds)})", flush=True)

        benign_preds, _ = predict_convs(encoder, tokenizer, gru, iid_benign)
        combined_preds = list(benign_preds) + list(ood_preds)
        combined_true = [0] * len(iid_benign) + [1] * len(ood_data)
        combined_f1 = f1_score(combined_true, combined_preds, average="macro")
        ood_f1s[ood_name] = combined_f1
        results[f"ood_{ood_name}_f1"] = combined_f1
        print(f"  OOD {ood_name} F1: {combined_f1:.4f}", flush=True)

    results["ood_f1_summary"] = ood_f1s
    return results


def main():
    t_total = time.time()
    print("=" * 70, flush=True)
    print("exp51: oasst2 Benign OOD Evaluation + 10-shot Adaptation", flush=True)
    print("=" * 70, flush=True)

    # Step 0: Ensure model cached
    ensure_model_cached()
    local_model_path = find_local_model()
    print(f"Using model: {local_model_path}", flush=True)

    # Load oasst2 eval data
    oasst2_eval = load_jsonl(OASST2_EVAL)
    oasst2_adapt = load_jsonl(OASST2_ADAPT)
    print(f"oasst2 eval: {len(oasst2_eval)}, adapt: {len(oasst2_adapt)}", flush=True)

    # Phase 1: Baseline evaluation
    encoder, tokenizer = load_encoder_and_tokenizer(BASELINE_DEBERTA, local_model_path)
    gru = load_gru(BASELINE_GRU)
    baseline_result = evaluate_baseline(encoder, tokenizer, gru, oasst2_eval)

    final_results = {
        "baseline_fpr": {"9class": baseline_result["fpr"]},
        "n_eval": len(oasst2_eval),
        "data_source": "oasst2",
        "baseline_detail": {
            "n_fp": baseline_result["n_fp"],
            "mean_jailbreak_prob": baseline_result["mean_jailbreak_prob"],
            "max_jailbreak_prob": baseline_result["max_jailbreak_prob"],
        },
        "adapted_fpr": None,
        "adapted_ood_f1": None,
        "n_adapt": None,
    }

    del encoder, gru
    torch.cuda.empty_cache()

    # Phase 2: Adaptation if FPR > 20%
    if baseline_result["fpr"] > 0.20:
        print(f"\nFPR {baseline_result['fpr']:.1%} > 20%, proceeding with 10-shot adaptation.", flush=True)

        deberta_path, gru_path = run_adaptation(local_model_path, oasst2_adapt, n_adapt=10)

        # Full evaluation of adapted model
        print("\n" + "=" * 70, flush=True)
        print("PHASE 2b: Evaluating adapted model", flush=True)
        print("=" * 70, flush=True)

        encoder, tokenizer = load_encoder_and_tokenizer(deberta_path, local_model_path)
        gru = load_gru(gru_path)

        test_data = load_jsonl(TEST_PATH)
        ood_datasets = {
            "dd": load_jsonl(DD_PATH),
            "aa": load_jsonl(AA_PATH),
            "fitd": load_jsonl(FITD_PATH),
        }

        adapted_results = full_evaluation(encoder, tokenizer, gru, oasst2_eval, test_data, ood_datasets)

        final_results["adapted_fpr"] = adapted_results["oasst2_fpr"]
        final_results["adapted_ood_f1"] = {
            "dd": adapted_results.get("ood_dd_f1"),
            "aa": adapted_results.get("ood_aa_f1"),
            "fitd": adapted_results.get("ood_fitd_f1"),
        }
        final_results["adapted_iid_f1"] = adapted_results.get("iid_f1_macro")
        final_results["n_adapt"] = 10
        final_results["adapted_detail"] = adapted_results

        del encoder, gru
        torch.cuda.empty_cache()
    else:
        print(f"\nFPR {baseline_result['fpr']:.1%} <= 20%, skipping adaptation.", flush=True)
        print("oasst2 FPR is low — benign shift may be source-specific (WildChat-only).", flush=True)

    # Save results
    RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    # Remove per-sample probs from final save (too large)
    with open(RESULTS_JSON, "w") as f:
        json.dump(final_results, f, indent=2)
    print(f"\nResults saved to {RESULTS_JSON}", flush=True)

    # Summary
    elapsed = time.time() - t_total
    print(f"\n{'=' * 70}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'=' * 70}", flush=True)
    print(f"  Baseline 9-class FPR on oasst2: {final_results['baseline_fpr']['9class']:.4f}", flush=True)
    if final_results["adapted_fpr"] is not None:
        print(f"  Adapted FPR (10-shot):          {final_results['adapted_fpr']:.4f}", flush=True)
        print(f"  Adapted IID F1:                 {final_results.get('adapted_iid_f1', 'N/A')}", flush=True)
        for k, v in (final_results["adapted_ood_f1"] or {}).items():
            print(f"  Adapted OOD {k.upper()} F1:            {v:.4f}", flush=True)
    print(f"  Total time: {elapsed/60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
