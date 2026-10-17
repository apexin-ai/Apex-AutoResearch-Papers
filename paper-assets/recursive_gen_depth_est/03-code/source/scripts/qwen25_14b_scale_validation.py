"""Qwen2.5-14B FP16 scale validation pipeline.
Recursive generation d0-d3, 19 statistical features (self-reference), RF/LR 5-fold CV.
No quantization: clean FP16 to verify depth signal persists at 14B scale.
"""

import gc
import json
import os
import sys
import time
from collections import Counter

import numpy as np
import torch
from scipy.stats import skew, kurtosis, entropy
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)
from peft import LoraConfig, PeftModel, get_peft_model

SEED = 42
MODEL_PATH = "/root/autodl-tmp/models/qwen25_14b"
PROJECT_DIR = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_DIR = os.path.join(PROJECT_DIR, "data/qwen25_14b")
CKPT_DIR = os.path.join(PROJECT_DIR, "checkpoints/qwen25_14b")
RESULTS_DIR = os.path.join(PROJECT_DIR, "results/qwen25_14b_scale")
NUM_SAMPLES = 5000
MAX_DEPTH = 3
NUM_FOLDS = 5


def cleanup_gpu():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
        torch.cuda.synchronize()


def load_model_fp16():
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.float16,
        trust_remote_code=True,
        device_map="auto",
    )
    return model, tokenizer


# =====================================================================
# Phase 2: Generate d0 (unconditional from base model)
# =====================================================================

def generate_d0():
    output_path = os.path.join(DATA_DIR, "depth_0.jsonl")
    if os.path.exists(output_path):
        count = sum(1 for _ in open(output_path))
        if count >= NUM_SAMPLES:
            print(f"d0 exists: {count} samples, skipping")
            return

    print(f"Generating d0: {NUM_SAMPLES} unconditional samples...")
    model, tokenizer = load_model_fp16()
    model.eval()

    device = next(model.parameters()).device
    bos_id = tokenizer.bos_token_id
    if bos_id is None:
        bos_id = tokenizer.eos_token_id
    pad_id = tokenizer.pad_token_id
    batch_size = 4

    os.makedirs(DATA_DIR, exist_ok=True)
    torch.manual_seed(SEED)

    generated = 0
    with open(output_path, "w", encoding="utf-8") as f:
        for batch_start in range(0, NUM_SAMPLES, batch_size):
            cur_bs = min(batch_size, NUM_SAMPLES - batch_start)
            input_ids = torch.tensor([[bos_id]] * cur_bs, device=device)
            attention_mask = torch.ones_like(input_ids)

            with torch.no_grad():
                outputs = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    max_new_tokens=512,
                    do_sample=True,
                    top_p=0.95,
                    temperature=1.0,
                    pad_token_id=pad_id,
                )

            for i, output in enumerate(outputs):
                text = tokenizer.decode(output[1:], skip_special_tokens=True)
                record = {
                    "text": text,
                    "depth": 0,
                    "seed_id": batch_start + i,
                    "token_count": len(output) - 1,
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

            generated += cur_bs
            if generated % 200 == 0 or generated >= NUM_SAMPLES:
                print(f"  d0: {generated}/{NUM_SAMPLES}")

    del model
    cleanup_gpu()
    print(f"d0 done: {output_path}")


# =====================================================================
# Phase 3: LoRA finetune + generate d1, d2, d3
# =====================================================================

class TextDataset(torch.utils.data.Dataset):
    def __init__(self, data_path, tokenizer, max_seq_len=512):
        self.examples = []
        with open(data_path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                encoded = tokenizer(
                    rec["text"], truncation=True, max_length=max_seq_len, padding=False
                )
                self.examples.append(encoded)

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return {k: torch.tensor(v) for k, v in self.examples[idx].items()}


def lora_finetune(depth):
    input_path = os.path.join(DATA_DIR, f"depth_{depth}.jsonl")
    output_dir = os.path.join(CKPT_DIR, f"lora_depth_{depth}")

    if os.path.exists(os.path.join(output_dir, "adapter_config.json")):
        print(f"LoRA adapter for d{depth} exists, skipping")
        return

    print(f"LoRA finetune on d{depth}...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )

    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    dataset = TextDataset(input_path, tokenizer, max_seq_len=512)
    print(f"  Dataset: {len(dataset)} samples")

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=3,
        per_device_train_batch_size=4,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        bf16=True,
        logging_steps=50,
        save_strategy="epoch",
        save_total_limit=1,
        seed=SEED,
        report_to="none",
        remove_unused_columns=False,
        dataloader_pin_memory=True,
        gradient_checkpointing=True,
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=data_collator,
    )

    result = trainer.train()
    print(f"  Loss: {result.training_loss:.4f}")

    model.save_pretrained(output_dir)
    tokenizer.save_pretrained(output_dir)
    print(f"  Adapter saved: {output_dir}")

    del model, trainer
    cleanup_gpu()


def generate_next_depth(depth):
    output_path = os.path.join(DATA_DIR, f"depth_{depth}.jsonl")
    adapter_dir = os.path.join(CKPT_DIR, f"lora_depth_{depth - 1}")

    if os.path.exists(output_path):
        count = sum(1 for _ in open(output_path))
        if count >= NUM_SAMPLES:
            print(f"d{depth} exists: {count} samples, skipping")
            return

    print(f"Generating d{depth}: {NUM_SAMPLES} samples with LoRA(d{depth-1})...")
    model, tokenizer = load_model_fp16()
    model = PeftModel.from_pretrained(model, adapter_dir)
    model.eval()

    device = next(model.parameters()).device
    bos_id = tokenizer.bos_token_id
    if bos_id is None:
        bos_id = tokenizer.eos_token_id
    pad_id = tokenizer.pad_token_id
    batch_size = 4

    torch.manual_seed(SEED + depth)

    generated = 0
    with open(output_path, "w", encoding="utf-8") as f:
        for batch_start in range(0, NUM_SAMPLES, batch_size):
            cur_bs = min(batch_size, NUM_SAMPLES - batch_start)
            input_ids = torch.tensor([[bos_id]] * cur_bs, device=device)
            attention_mask = torch.ones_like(input_ids)

            with torch.no_grad():
                outputs = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    max_new_tokens=512,
                    do_sample=True,
                    top_p=0.95,
                    temperature=1.0,
                    pad_token_id=pad_id,
                )

            for i, output in enumerate(outputs):
                text = tokenizer.decode(output[1:], skip_special_tokens=True)
                record = {
                    "text": text,
                    "depth": depth,
                    "seed_id": batch_start + i,
                    "token_count": len(output) - 1,
                }
                f.write(json.dumps(record, ensure_ascii=False) + "\n")

            generated += cur_bs
            if generated % 200 == 0 or generated >= NUM_SAMPLES:
                print(f"  d{depth}: {generated}/{NUM_SAMPLES}")

    del model
    cleanup_gpu()
    print(f"d{depth} done: {output_path}")


# =====================================================================
# Phase 4: Feature extraction (self-reference)
# =====================================================================

def compute_perplexity_features(losses):
    if len(losses) == 0:
        losses = np.array([0.0])
    ppl = np.exp(losses)
    return {
        "mean_ppl": float(np.mean(ppl)),
        "var_ppl": float(np.var(ppl)),
        "median_ppl": float(np.median(ppl)),
        "p75_ppl": float(np.percentile(ppl, 75)),
        "p90_ppl": float(np.percentile(ppl, 90)),
        "skew_ppl": float(skew(ppl)) if len(ppl) > 2 else 0.0,
        "kurt_ppl": float(kurtosis(ppl)) if len(ppl) > 3 else 0.0,
        "mean_surprisal": float(np.mean(losses)),
        "var_surprisal": float(np.var(losses)),
        "median_surprisal": float(np.median(losses)),
        "p75_surprisal": float(np.percentile(losses, 75)),
        "p90_surprisal": float(np.percentile(losses, 90)),
    }


def compute_repetition(token_ids, n):
    if len(token_ids) < n:
        return 0.0
    ngrams = [tuple(token_ids[i:i + n]) for i in range(len(token_ids) - n + 1)]
    total = len(ngrams)
    unique = len(set(ngrams))
    return 1.0 - unique / total if total > 0 else 0.0


def compute_lexical_features(token_ids):
    total = len(token_ids)
    if total == 0:
        return {k: 0.0 for k in [
            "type_token_ratio", "hapax_ratio", "bigram_entropy", "trigram_entropy",
            "rep_2gram", "rep_3gram", "rep_4gram"]}

    counts = Counter(token_ids)
    unique = len(counts)
    ttr = unique / total
    hapax = sum(1 for c in counts.values() if c == 1)
    hapax_ratio = hapax / unique if unique > 0 else 0.0

    bigrams = [tuple(token_ids[i:i + 2]) for i in range(total - 1)]
    if bigrams:
        bg_counts = Counter(bigrams)
        bg_freq = np.array(list(bg_counts.values()), dtype=np.float64)
        bg_freq /= bg_freq.sum()
        bg_ent = float(entropy(bg_freq))
    else:
        bg_ent = 0.0

    trigrams = [tuple(token_ids[i:i + 3]) for i in range(total - 2)]
    if trigrams:
        tg_counts = Counter(trigrams)
        tg_freq = np.array(list(tg_counts.values()), dtype=np.float64)
        tg_freq /= tg_freq.sum()
        tg_ent = float(entropy(tg_freq))
    else:
        tg_ent = 0.0

    return {
        "type_token_ratio": ttr,
        "hapax_ratio": hapax_ratio,
        "bigram_entropy": bg_ent,
        "trigram_entropy": tg_ent,
        "rep_2gram": compute_repetition(token_ids, 2),
        "rep_3gram": compute_repetition(token_ids, 3),
        "rep_4gram": compute_repetition(token_ids, 4),
    }


def extract_batch_features(model, tokenizer, texts, trunc_len, device):
    pad_id = tokenizer.pad_token_id
    encoded = []
    for text in texts:
        ids = tokenizer.encode(text, add_special_tokens=False)[:trunc_len]
        encoded.append(ids)

    max_len = max(len(e) for e in encoded)
    input_ids = []
    attention_mask = []
    for e in encoded:
        pad_len = max_len - len(e)
        input_ids.append(e + [pad_id] * pad_len)
        attention_mask.append([1] * len(e) + [0] * pad_len)

    input_ids_t = torch.tensor(input_ids, dtype=torch.long, device=device)
    attention_mask_t = torch.tensor(attention_mask, dtype=torch.long, device=device)

    with torch.no_grad():
        outputs = model(input_ids=input_ids_t, attention_mask=attention_mask_t)
    logits = outputs.logits

    shift_logits = logits[:, :-1, :].contiguous()
    shift_labels = input_ids_t[:, 1:].contiguous()
    loss_fn = torch.nn.CrossEntropyLoss(reduction="none")
    per_token_loss = loss_fn(
        shift_logits.view(-1, shift_logits.size(-1)),
        shift_labels.view(-1),
    ).view(shift_logits.size(0), shift_logits.size(1))

    results = []
    for i in range(len(texts)):
        seq_len = len(encoded[i])
        if seq_len <= 1:
            losses_np = np.array([0.0])
        else:
            losses_np = per_token_loss[i, : seq_len - 1].cpu().numpy().astype(np.float64)

        feats = {}
        feats.update(compute_perplexity_features(losses_np))
        feats.update(compute_lexical_features(encoded[i]))
        results.append(feats)

    return results


def extract_features():
    features_path = os.path.join(DATA_DIR, "features_self_ref.jsonl")
    if os.path.exists(features_path):
        count = sum(1 for _ in open(features_path))
        expected = NUM_SAMPLES * (MAX_DEPTH + 1)
        if count >= expected * 0.95:
            print(f"Features exist: {count} samples, skipping")
            return features_path

    print("Feature extraction (self-reference with Qwen2.5-14B)...")

    depth_data = {}
    for d in range(MAX_DEPTH + 1):
        fpath = os.path.join(DATA_DIR, f"depth_{d}.jsonl")
        records = []
        with open(fpath) as f:
            for line in f:
                if line.strip():
                    records.append(json.loads(line))
        depth_data[d] = records
        print(f"  d{d}: {len(records)} samples")

    model, tokenizer = load_model_fp16()
    model.eval()
    device = next(model.parameters()).device

    depth_medians = {}
    for d, records in sorted(depth_data.items()):
        lengths = [len(tokenizer.encode(r["text"], add_special_tokens=False)) for r in records[:500]]
        med = int(np.median(lengths))
        depth_medians[d] = med
        print(f"  d{d} median tokens: {med}")
    trunc_len = min(depth_medians.values())
    print(f"  Truncation length: {trunc_len}")

    batch_size = 4
    sample_id = 0

    with open(features_path, "w") as out_f:
        for d in sorted(depth_data.keys()):
            texts = [r["text"] for r in depth_data[d]]
            for start in tqdm(range(0, len(texts), batch_size), desc=f"d{d}", unit="batch"):
                end = min(start + batch_size, len(texts))
                batch_texts = texts[start:end]
                try:
                    batch_feats = extract_batch_features(
                        model, tokenizer, batch_texts, trunc_len, device
                    )
                except Exception as e:
                    print(f"\n  [WARN] Batch error d{d} [{start}:{end}]: {e}")
                    continue

                for feat in batch_feats:
                    row = {"depth": d, "sample_id": sample_id}
                    row.update(feat)
                    out_f.write(json.dumps(row) + "\n")
                    sample_id += 1

    del model
    cleanup_gpu()
    print(f"Features done: {sample_id} samples -> {features_path}")
    return features_path


# =====================================================================
# Phase 5: Classification (RF + LR, 5-fold CV)
# =====================================================================

def load_feature_data(path, max_depth=None):
    records = []
    with open(path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            if max_depth is not None and rec["depth"] > max_depth:
                continue
            records.append(rec)

    exclude = {"depth", "sample_id"}
    feat_names = [k for k in records[0].keys() if k not in exclude]
    X = np.array([[r[k] for k in feat_names] for r in records], dtype=np.float64)
    y = np.array([r["depth"] for r in records], dtype=np.int64)
    X = np.nan_to_num(X, nan=0.0, posinf=0.0, neginf=0.0)
    return X, y, feat_names


def boot_ci(y_true, y_pred, n=1000, seed=SEED):
    rng = np.random.RandomState(seed)
    m = len(y_true)
    scores = []
    for _ in range(n):
        idx = rng.choice(m, m, replace=True)
        scores.append(accuracy_score(y_true[idx], y_pred[idx]))
    return [round(float(np.percentile(scores, 2.5)), 4),
            round(float(np.percentile(scores, 97.5)), 4)]


def pair_auc(y_true, y_prob, d1, d2, labels):
    mask = np.isin(y_true, [d1, d2])
    if mask.sum() < 10:
        return None
    yt = (y_true[mask] == d2).astype(int)
    if len(np.unique(yt)) < 2:
        return None
    yp = y_prob[mask, list(labels).index(d2)]
    return round(float(roc_auc_score(yt, yp)), 4)


def align_proba(clf, prob, labels):
    if np.array_equal(clf.classes_, np.array(labels)):
        return prob
    aligned = np.zeros((prob.shape[0], len(labels)))
    for i, c in enumerate(clf.classes_):
        j = labels.index(c)
        aligned[:, j] = prob[:, i]
    return aligned


def run_cv(X, y, clf_fn, labels):
    skf = StratifiedKFold(n_splits=NUM_FOLDS, shuffle=True, random_state=SEED)
    yt_all, yp_all, yprob_all = [], [], []
    fi_accum = None

    for train_idx, test_idx in skf.split(X, y):
        scaler = StandardScaler()
        Xtr = scaler.fit_transform(X[train_idx])
        Xte = scaler.transform(X[test_idx])

        clf = clf_fn()
        clf.fit(Xtr, y[train_idx])

        pred = clf.predict(Xte)
        prob = align_proba(clf, clf.predict_proba(Xte), labels)

        yt_all.append(y[test_idx])
        yp_all.append(pred)
        yprob_all.append(prob)

        if hasattr(clf, "feature_importances_"):
            if fi_accum is None:
                fi_accum = clf.feature_importances_.copy()
            else:
                fi_accum += clf.feature_importances_

    if fi_accum is not None:
        fi_accum /= NUM_FOLDS

    return (
        np.concatenate(yt_all),
        np.concatenate(yp_all),
        np.concatenate(yprob_all),
        fi_accum,
    )


def classify(features_path):
    print("Classification...")
    os.makedirs(RESULTS_DIR, exist_ok=True)

    X, y, feat_names = load_feature_data(features_path, max_depth=3)
    labels = sorted(np.unique(y).tolist())
    print(f"  {X.shape[0]} samples, {X.shape[1]} features, classes={labels}")
    for d in labels:
        print(f"    d{d}: {(y == d).sum()}")

    results = {
        "model": "Qwen2.5-14B",
        "precision": "FP16",
        "reference": "self (Qwen2.5-14B)",
        "samples_per_depth": NUM_SAMPLES,
        "num_folds": NUM_FOLDS,
    }

    # --- RF 4-class ---
    print("\n  RF 5-fold CV (4-class d0-d3)...")
    rf_fn = lambda: RandomForestClassifier(n_estimators=200, random_state=SEED)
    yt_rf, yp_rf, yprob_rf, rf_fi = run_cv(X, y, rf_fn, labels)
    rf_acc = round(float(accuracy_score(yt_rf, yp_rf)), 4)
    rf_ci = boot_ci(yt_rf, yp_rf)

    rf_pair_aucs = {}
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            auc = pair_auc(yt_rf, yprob_rf, labels[i], labels[j], labels)
            rf_pair_aucs[f"d{labels[i]}v{labels[j]}"] = auc

    fi_sorted = sorted(zip(feat_names, rf_fi.tolist()), key=lambda x: -x[1])
    top5 = [name for name, _ in fi_sorted[:5]]

    print(f"  RF acc={rf_acc} CI={rf_ci}")
    print(f"  d0v1={rf_pair_aucs.get('d0v1')} d1v2={rf_pair_aucs.get('d1v2')} d2v3={rf_pair_aucs.get('d2v3')}")
    print(f"  Top-5: {top5}")

    results["rf_4class"] = {
        "acc": rf_acc,
        "ci_95": rf_ci,
        "pairwise_auc": rf_pair_aucs,
        "top5_features": top5,
        "feature_importance": dict(fi_sorted[:10]),
    }

    # --- LR 4-class ---
    print("\n  LR 5-fold CV (4-class)...")
    lr_fn = lambda: LogisticRegression(max_iter=1000, random_state=SEED, C=1.0)
    yt_lr, yp_lr, yprob_lr, _ = run_cv(X, y, lr_fn, labels)
    lr_acc = round(float(accuracy_score(yt_lr, yp_lr)), 4)
    lr_ci = boot_ci(yt_lr, yp_lr)

    lr_pair_aucs = {}
    for i in range(len(labels)):
        for j in range(i + 1, len(labels)):
            auc = pair_auc(yt_lr, yprob_lr, labels[i], labels[j], labels)
            lr_pair_aucs[f"d{labels[i]}v{labels[j]}"] = auc

    print(f"  LR acc={lr_acc} CI={lr_ci}")

    results["lr_4class"] = {
        "acc": lr_acc,
        "ci_95": lr_ci,
        "pairwise_auc": lr_pair_aucs,
    }

    # --- RF 3-class (d1/d2/d3, no d0) ---
    print("\n  RF 5-fold CV (3-class d1/d2/d3)...")
    mask_3c = y >= 1
    X_3c, y_3c = X[mask_3c], y[mask_3c]
    labels_3c = sorted(np.unique(y_3c).tolist())

    yt_3c, yp_3c, _, _ = run_cv(X_3c, y_3c, rf_fn, labels_3c)
    acc_3c = round(float(accuracy_score(yt_3c, yp_3c)), 4)
    ci_3c = boot_ci(yt_3c, yp_3c)
    print(f"  3-class acc={acc_3c} CI={ci_3c}")

    results["rf_3class_no_d0"] = {"acc": acc_3c, "ci_95": ci_3c}

    # --- Save ---
    summary_path = os.path.join(RESULTS_DIR, "summary.json")
    with open(summary_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved: {summary_path}")

    return results


# =====================================================================
# Main
# =====================================================================

def main():
    t0 = time.time()

    for d in [DATA_DIR, CKPT_DIR, RESULTS_DIR]:
        os.makedirs(d, exist_ok=True)

    print("=" * 60)
    print("Qwen2.5-14B FP16 Scale Validation")
    print(f"  Samples/depth: {NUM_SAMPLES}, Depths: 0-{MAX_DEPTH}")
    print(f"  Model: {MODEL_PATH}")
    print(f"  GPU: {os.environ.get('CUDA_VISIBLE_DEVICES', 'all')}")
    print("=" * 60)

    # Phase 2: d0
    print("\n[Phase 2] Generate d0")
    generate_d0()

    # Phase 3: recursive generation d1-d3
    for depth in range(MAX_DEPTH):
        print(f"\n[Phase 3.{depth + 1}a] LoRA finetune d{depth}")
        lora_finetune(depth)

        print(f"\n[Phase 3.{depth + 1}b] Generate d{depth + 1}")
        generate_next_depth(depth + 1)

    # Phase 4: feature extraction
    print("\n[Phase 4] Feature extraction (self-reference)")
    features_path = extract_features()

    # Phase 5: classification
    print("\n[Phase 5] Classification")
    results = classify(features_path)

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"DONE in {elapsed / 3600:.1f}h")
    print(f"RF 4-class: {results['rf_4class']['acc']} {results['rf_4class']['ci_95']}")
    print(f"LR 4-class: {results['lr_4class']['acc']} {results['lr_4class']['ci_95']}")
    print(f"RF 3-class (no d0): {results['rf_3class_no_d0']['acc']}")
    print(f"Top features: {results['rf_4class']['top5_features']}")
    print(f"d1v2 AUC: {results['rf_4class']['pairwise_auc'].get('d1v2')}")
    print("=" * 60)


if __name__ == "__main__":
    main()
