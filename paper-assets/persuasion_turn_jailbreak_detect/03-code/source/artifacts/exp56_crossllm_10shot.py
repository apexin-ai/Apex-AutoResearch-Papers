#!/usr/bin/env python3
"""exp56: Cross-LLM 10-shot Benign Adaptation.

Tests whether 10-shot benign adaptation fixes cross-LLM FPR.
Train: Qwen-generated data only. Eval: Llama-generated benign (expect 88-90% FPR).
Adaptation: add N Llama-benign conversations to training, retrain Stage1+Stage2.
"""

import os, sys, json, random, time, subprocess
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from sklearn.metrics import f1_score

os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

sys.path.insert(0, "/root/persuasion_turn_jailbreak_detect")
from src.models.deberta_multitask import DeBERTaMultiTask
from src.models.gru_classifier import GRUClassifier
from transformers import AutoTokenizer, AutoConfig

PROJ = Path("/root/persuasion_turn_jailbreak_detect")
CKPT_BASE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints")
CKPT_ARCHIVE = Path("/root/autodl-tmp/persuasion_turn_jailbreak_detect/checkpoints_archive")
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

BASELINE_DEBERTA = CKPT_ARCHIVE / "plan_002" / "deberta_multitask" / "best"
BASELINE_GRU = CKPT_ARCHIVE / "plan_002" / "gru" / "treatment" / "best.pt"

LLAMA_BENIGN_ALL = PROJ / "data" / "llama_conversations" / "benign_llama_250.jsonl"
TRAIN_PATH = PROJ / "data" / "plan_002_splits" / "train.jsonl"
VAL_PATH = PROJ / "data" / "plan_002_splits" / "val.jsonl"
TEST_PATH = PROJ / "data" / "plan_002_splits" / "test.jsonl"
DD_PATH = PROJ / "data" / "generated" / "deceptive_delight_all.jsonl"
AA_PATH = PROJ / "data" / "actorattack_ood" / "actorattack_all.jsonl"
FITD_PATH = PROJ / "data" / "generated" / "fitd_all.jsonl"

# Cross-LLM jailbreak data (Llama-generated)
DD_LLAMA = PROJ / "data" / "cross_llm" / "dd_llama.jsonl"
AA_LLAMA = PROJ / "data" / "cross_llm" / "aa_llama.jsonl"
FITD_LLAMA = PROJ / "data" / "cross_llm" / "fitd_llama.jsonl"

RESULTS_JSON = PROJ / "results" / "exp56_crossllm_10shot.json"

HF_CACHE = "/root/autodl-tmp/.hf_cache"
MODEL_NAME = "microsoft/deberta-v3-base"

N_ADAPT_POOL = 50
N_EVAL = 200
ADAPT_CURVE = [0, 5, 10, 25]


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


def find_local_model():
    hf_dir = Path(HF_CACHE) / "models--microsoft--deberta-v3-base" / "snapshots"
    if not hf_dir.exists():
        hf_hub = Path(HF_CACHE) / "hub"
        hf_dir = hf_hub / "models--microsoft--deberta-v3-base" / "snapshots"
    if hf_dir.exists():
        candidates = list(hf_dir.glob("*/config.json"))
        if candidates:
            return str(candidates[0].parent)
    return MODEL_NAME


def load_encoder_and_tokenizer(deberta_ckpt_path, local_model_path):
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
    gru = GRUClassifier(
        input_dim=input_dim, hidden_dim=GRU_HIDDEN,
        num_layers=GRU_LAYERS, dropout=GRU_DROPOUT
    )
    state = torch.load(gru_path, map_location="cpu", weights_only=False)
    gru.load_state_dict(state)
    gru.to(DEVICE).eval()
    return gru


def predict_convs(encoder, tokenizer, gru, conversations):
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


def evaluate_fpr(encoder, tokenizer, gru, benign_data, label=""):
    preds, probs = predict_convs(encoder, tokenizer, gru, benign_data)
    fpr = sum(preds) / len(preds)
    print(f"  {label} FPR: {fpr:.4f} ({sum(preds)}/{len(preds)})", flush=True)
    print(f"  Mean jailbreak prob: {np.mean(probs):.4f}", flush=True)
    return {
        "fpr": fpr,
        "n_fp": sum(preds),
        "n_total": len(preds),
        "mean_jailbreak_prob": float(np.mean(probs)),
    }


def prepare_llama_benign_for_training(conv):
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
        "source": conv.get("source", "llama-benign"),
        "attack_type": "benign",
    }


def run_adaptation(local_model_path, adapt_samples, n_adapt, seed=42):
    set_seed(seed)
    original_train = load_jsonl(TRAIN_PATH)
    selected = adapt_samples[:n_adapt]
    formatted = [prepare_llama_benign_for_training(c) for c in selected]
    mixed_train = list(original_train) + formatted

    print(f"  Mixed train: {len(mixed_train)} ({len(original_train)} original + {n_adapt} Llama-benign)", flush=True)

    mixed_path = PROJ / "data" / f"exp56_mixed_n{n_adapt}_seed{seed}.jsonl"
    save_jsonl(mixed_train, mixed_path)

    name = f"exp56_crossllm_n{n_adapt}_seed{seed}"
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
        "--seed", str(seed),
        "--alpha", str(ALPHA),
    ]

    print(f"\n  Stage 1: DeBERTa DAPT (n={n_adapt})...", flush=True)
    t0 = time.time()
    result = subprocess.run(cmd, text=True, capture_output=True)
    elapsed = time.time() - t0
    print(f"  Stage 1 done in {elapsed/60:.1f} min (exit={result.returncode})", flush=True)
    if result.returncode != 0:
        print(f"  STDERR: {result.stderr[-2000:]}", flush=True)
        raise RuntimeError(f"Stage 1 failed for n={n_adapt}")

    deberta_path = ckpt_dir / "best"
    assert (deberta_path / "model.pt").exists(), f"No checkpoint at {deberta_path}"

    # Stage 2: GRU
    print(f"  Stage 2: GRU training (n={n_adapt})...", flush=True)
    set_seed(seed)

    gru_dir = CKPT_BASE / name / "gru"
    gru_dir.mkdir(parents=True, exist_ok=True)

    encoder, tokenizer = load_encoder_and_tokenizer(deberta_path, local_model_path)

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

    gru = GRUClassifier(input_dim=768, hidden_dim=GRU_HIDDEN,
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
            print(f"    Epoch {epoch+1}: loss={total_loss/n_batches:.4f} val_f1={val_f1:.4f} best={best_val_f1:.4f}", flush=True)

        if no_improve >= patience:
            print(f"    Early stopping at epoch {epoch+1}", flush=True)
            break

    gru_path = gru_dir / "best.pt"
    torch.save(best_state, gru_path)
    print(f"  GRU saved to {gru_path}", flush=True)

    del gru, encoder
    torch.cuda.empty_cache()

    return deberta_path, gru_path


def full_evaluation(encoder, tokenizer, gru, llama_eval, test_data, ood_datasets):
    results = {}

    # Llama-benign FPR
    llama_preds, llama_probs = predict_convs(encoder, tokenizer, gru, llama_eval)
    fpr = sum(llama_preds) / len(llama_preds)
    results["llama_benign_fpr"] = fpr
    results["llama_benign_n_fp"] = sum(llama_preds)
    results["llama_benign_n_total"] = len(llama_preds)
    print(f"  Llama-benign FPR: {fpr:.4f} ({sum(llama_preds)}/{len(llama_preds)})", flush=True)

    # IID F1
    iid_preds, _ = predict_convs(encoder, tokenizer, gru, test_data)
    iid_true = [get_label(c) for c in test_data]
    iid_f1 = f1_score(iid_true, iid_preds, average="macro")
    results["iid_f1_macro"] = iid_f1
    print(f"  IID F1 macro: {iid_f1:.4f}", flush=True)

    # OOD F1 (Qwen-generated)
    iid_benign = [c for c in test_data if c["label"] == "benign"]
    for ood_name, ood_data in ood_datasets.items():
        ood_preds, _ = predict_convs(encoder, tokenizer, gru, ood_data)
        ood_recall = sum(ood_preds) / len(ood_preds)
        results[f"ood_{ood_name}_recall"] = ood_recall
        print(f"  OOD {ood_name} recall: {ood_recall:.4f}", flush=True)

        benign_preds, _ = predict_convs(encoder, tokenizer, gru, iid_benign)
        combined_preds = list(benign_preds) + list(ood_preds)
        combined_true = [0] * len(iid_benign) + [1] * len(ood_data)
        combined_f1 = f1_score(combined_true, combined_preds, average="macro")
        results[f"ood_{ood_name}_f1"] = combined_f1
        print(f"  OOD {ood_name} F1: {combined_f1:.4f}", flush=True)

    return results


def main():
    t_total = time.time()
    print("=" * 70, flush=True)
    print("exp56: Cross-LLM 10-shot Benign Adaptation", flush=True)
    print("=" * 70, flush=True)

    local_model_path = find_local_model()
    print(f"Using model: {local_model_path}", flush=True)

    # Split Llama benign: first 50 for adaptation, remaining 200 for eval
    set_seed(SEED)
    all_llama = load_jsonl(LLAMA_BENIGN_ALL)
    random.shuffle(all_llama)
    llama_adapt = all_llama[:N_ADAPT_POOL]
    llama_eval = all_llama[N_ADAPT_POOL:N_ADAPT_POOL + N_EVAL]
    print(f"Llama benign: {len(all_llama)} total, {len(llama_adapt)} adapt pool, {len(llama_eval)} eval", flush=True)

    # Load OOD datasets
    test_data = load_jsonl(TEST_PATH)
    ood_qwen = {
        "dd": load_jsonl(DD_PATH),
        "aa": load_jsonl(AA_PATH),
        "fitd": load_jsonl(FITD_PATH),
    }
    ood_llama = {}
    if DD_LLAMA.exists():
        ood_llama["dd_llama"] = load_jsonl(DD_LLAMA)
    if AA_LLAMA.exists():
        ood_llama["aa_llama"] = load_jsonl(AA_LLAMA)
    if FITD_LLAMA.exists():
        ood_llama["fitd_llama"] = load_jsonl(FITD_LLAMA)
    all_ood = {**ood_qwen, **ood_llama}

    # ============================================================
    # Phase 1: Baseline FPR
    # ============================================================
    print("\n" + "=" * 70, flush=True)
    print("PHASE 1: Baseline FPR on Llama-benign", flush=True)
    print("=" * 70, flush=True)

    encoder, tokenizer = load_encoder_and_tokenizer(BASELINE_DEBERTA, local_model_path)
    gru = load_gru(BASELINE_GRU)

    baseline_fpr_result = evaluate_fpr(encoder, tokenizer, gru, llama_eval, label="Llama-benign (baseline)")

    # Also check Llama jailbreak recall with baseline
    baseline_llama_jb = {}
    for name, data in ood_llama.items():
        preds, _ = predict_convs(encoder, tokenizer, gru, data)
        recall = sum(preds) / len(preds)
        baseline_llama_jb[name] = recall
        print(f"  Baseline {name} recall: {recall:.4f}", flush=True)

    del encoder, gru
    torch.cuda.empty_cache()

    # ============================================================
    # Phase 2: Adaptation curve (n=0,5,10,25)
    # ============================================================
    print("\n" + "=" * 70, flush=True)
    print("PHASE 2: Adaptation Curve", flush=True)
    print("=" * 70, flush=True)

    adaptation_results = {}

    for n in ADAPT_CURVE:
        print(f"\n--- N = {n} ---", flush=True)

        if n == 0:
            # n=0 is the baseline
            encoder, tokenizer = load_encoder_and_tokenizer(BASELINE_DEBERTA, local_model_path)
            gru = load_gru(BASELINE_GRU)
            deberta_path = BASELINE_DEBERTA
            gru_path = BASELINE_GRU
        else:
            deberta_path, gru_path = run_adaptation(local_model_path, llama_adapt, n_adapt=n, seed=SEED)
            encoder, tokenizer = load_encoder_and_tokenizer(deberta_path, local_model_path)
            gru = load_gru(gru_path)

        eval_result = full_evaluation(encoder, tokenizer, gru, llama_eval, test_data, all_ood)
        adaptation_results[f"n{n}"] = eval_result

        del encoder, gru
        torch.cuda.empty_cache()

    # ============================================================
    # Save results
    # ============================================================
    final_results = {
        "experiment": "exp56_crossllm_10shot_adaptation",
        "hypothesis": "10-shot benign adaptation with Llama-origin conversations reduces cross-LLM FPR",
        "baseline_fpr": baseline_fpr_result["fpr"],
        "baseline_llama_jb_recall": baseline_llama_jb,
        "n_eval": len(llama_eval),
        "n_adapt_pool": len(llama_adapt),
        "adaptation_curve": adaptation_results,
        "seed": SEED,
        "elapsed_minutes": (time.time() - t_total) / 60,
    }

    RESULTS_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(RESULTS_JSON, "w") as f:
        json.dump(final_results, f, indent=2)
    print(f"\nResults saved to {RESULTS_JSON}", flush=True)

    # Summary
    print(f"\n{'=' * 70}", flush=True)
    print("SUMMARY", flush=True)
    print(f"{'=' * 70}", flush=True)
    print(f"  Baseline Llama-benign FPR: {baseline_fpr_result['fpr']:.4f}", flush=True)
    for n_key, res in adaptation_results.items():
        fpr = res.get("llama_benign_fpr", "N/A")
        iid = res.get("iid_f1_macro", "N/A")
        dd = res.get("ood_dd_f1", "N/A")
        aa = res.get("ood_aa_f1", "N/A")
        fitd = res.get("ood_fitd_f1", "N/A")
        dd_l = res.get("ood_dd_llama_recall", "N/A")
        aa_l = res.get("ood_aa_llama_recall", "N/A")
        fitd_l = res.get("ood_fitd_llama_recall", "N/A")
        print(f"  {n_key}: FPR={fpr:.4f} IID_F1={iid:.4f} DD={dd:.4f} AA={aa:.4f} FITD={fitd:.4f} "
              f"DD_llama={dd_l:.4f} AA_llama={aa_l:.4f} FITD_llama={fitd_l:.4f}", flush=True)
    print(f"  Total time: {(time.time()-t_total)/60:.1f} min", flush=True)


if __name__ == "__main__":
    main()
