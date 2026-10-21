"""Downstream Curation PoC: RF depth predictor as data curator for Pythia-410M LoRA finetune.

Phases:
  data_prep  - Mix d0-d3, RF cross-val predict, filter into 8 conditions
  finetune   - LoRA finetune Pythia-410M on each condition x seed, eval WikiText-103 PPL
  analyze    - Collect PPL results, paired t-test, Cohen's d

Input:  data/depth_{0-3}.jsonl, data/features_all.jsonl
Output: data/curation_poc/*.jsonl, results/curation_poc/*/ppl_result.json, results/curation_poc/summary.json
"""

import argparse
import json
import os
import sys
import time
import math
import random
from pathlib import Path

import numpy as np

PROJECT_ROOT = "/root/autodl-tmp/recursive_gen_depth_est"
DATA_DIR = f"{PROJECT_ROOT}/data"
FEATURES_PATH = f"{DATA_DIR}/features_all.jsonl"
OUTPUT_DATA_DIR = f"{DATA_DIR}/curation_poc"
RESULT_DIR = f"{PROJECT_ROOT}/results/curation_poc"
MODEL_NAME = "EleutherAI/pythia-410m"
MODEL_CACHE = "/root/autodl-tmp/models/pythia-410m"

SAMPLES_PER_DEPTH = 2500
NUM_DEPTHS = 4
SEEDS = [42, 123, 456, 789, 1024]
CONDITIONS = [
    "unfiltered", "rf_strict", "rf_moderate", "rf_soft",
    "oracle_strict", "oracle_moderate", "random_strict", "random_moderate",
]

FEATURE_NAMES = [
    "mean_ppl", "var_ppl", "skewness_ppl", "kurtosis_ppl",
    "p10_ppl", "p25_ppl", "p50_ppl", "p75_ppl", "p90_ppl",
    "mean_surprisal", "var_surprisal", "entropy_of_surprisal",
    "type_token_ratio", "hapax_ratio",
    "bigram_entropy", "trigram_entropy",
    "rep_2gram", "rep_3gram", "rep_4gram",
]


# ============================================================
# Phase 1: Data Preparation
# ============================================================

def load_data_and_features():
    """Load text data and features, align by (depth, index), subsample 2500/depth."""
    texts_by_depth = {}
    for d in range(NUM_DEPTHS):
        path = f"{DATA_DIR}/depth_{d}.jsonl"
        with open(path) as f:
            texts_by_depth[d] = [json.loads(line) for line in f]
        print(f"  depth_{d}: {len(texts_by_depth[d])} samples loaded")

    features_by_depth = {d: [] for d in range(NUM_DEPTHS)}
    with open(FEATURES_PATH) as f:
        for line in f:
            rec = json.loads(line)
            features_by_depth[rec["depth"]].append(rec)

    for d in range(NUM_DEPTHS):
        print(f"  depth_{d} features: {len(features_by_depth[d])}")
        assert len(features_by_depth[d]) == len(texts_by_depth[d]), \
            f"Mismatch depth {d}: {len(features_by_depth[d])} features vs {len(texts_by_depth[d])} texts"

    rng = np.random.RandomState(42)
    all_texts, all_features, all_labels = [], [], []
    for d in range(NUM_DEPTHS):
        n = len(texts_by_depth[d])
        idx = rng.choice(n, size=SAMPLES_PER_DEPTH, replace=False)
        idx.sort()
        for i in idx:
            all_texts.append(texts_by_depth[d][i])
            feat_vec = [features_by_depth[d][i][fname] for fname in FEATURE_NAMES]
            all_features.append(feat_vec)
            all_labels.append(d)

    X = np.array(all_features, dtype=np.float64)
    y = np.array(all_labels, dtype=np.int32)
    print(f"  Total mixed: {len(all_texts)} samples, feature matrix {X.shape}")
    return all_texts, X, y


def train_rf_crossval(X, y):
    """Train RF and return cross-validated held-out probabilities."""
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler
    from sklearn.model_selection import cross_val_predict
    from sklearn.pipeline import Pipeline

    pipe = Pipeline([
        ("scaler", StandardScaler()),
        ("rf", RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1)),
    ])
    print("  Training RF with 5-fold cross_val_predict...")
    proba = cross_val_predict(pipe, X, y, cv=5, method="predict_proba", n_jobs=1)
    pred_class = proba.argmax(axis=1)

    from sklearn.metrics import accuracy_score, classification_report
    acc = accuracy_score(y, pred_class)
    print(f"  Cross-val accuracy: {acc:.4f}")
    print(classification_report(y, pred_class, digits=3))
    return proba


def apply_filters(proba, labels):
    """Generate boolean masks for 8 conditions."""
    pred_class = proba.argmax(axis=1)
    n = len(labels)

    masks = {
        "unfiltered": np.ones(n, dtype=bool),
        "rf_strict": pred_class == 0,
        "rf_moderate": np.isin(pred_class, [0, 1]),
        "rf_soft": (proba[:, 0] + proba[:, 1]) > 0.6,
        "oracle_strict": labels == 0,
        "oracle_moderate": np.isin(labels, [0, 1]),
    }

    rng = np.random.RandomState(42)
    idx_all = np.arange(n)

    n_strict = masks["rf_strict"].sum()
    rand_strict = np.zeros(n, dtype=bool)
    rand_strict[rng.choice(idx_all, size=n_strict, replace=False)] = True
    masks["random_strict"] = rand_strict

    n_moderate = masks["rf_moderate"].sum()
    rand_moderate = np.zeros(n, dtype=bool)
    rand_moderate[rng.choice(idx_all, size=n_moderate, replace=False)] = True
    masks["random_moderate"] = rand_moderate

    return masks


def write_filtered_data(masks, texts, labels):
    """Write 8 condition JSONL files."""
    os.makedirs(OUTPUT_DATA_DIR, exist_ok=True)
    summary = {}
    for name in CONDITIONS:
        mask = masks[name]
        path = f"{OUTPUT_DATA_DIR}/{name}.jsonl"
        count = 0
        with open(path, "w", encoding="utf-8") as f:
            for i in np.where(mask)[0]:
                rec = {"text": texts[i]["text"], "depth": int(labels[i])}
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
                count += 1
        depth_dist = {}
        for i in np.where(mask)[0]:
            d = int(labels[i])
            depth_dist[d] = depth_dist.get(d, 0) + 1
        summary[name] = {"count": count, "depth_distribution": depth_dist}
        print(f"  {name}: {count} samples -> {path}  dist={depth_dist}")

    with open(f"{OUTPUT_DATA_DIR}/data_prep_summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    return summary


def phase_data_prep():
    print("=" * 60)
    print("Phase 1: Data Preparation")
    print("=" * 60)
    texts, X, y = load_data_and_features()
    proba = train_rf_crossval(X, y)
    masks = apply_filters(proba, y)
    summary = write_filtered_data(masks, texts, y)
    print("\nData preparation complete.")
    return summary


# ============================================================
# Phase 2: Finetune + Eval
# ============================================================

def get_model_path():
    """Return local path if model exists locally, else HF model name."""
    if os.path.exists(MODEL_CACHE) and any(
        f.endswith(".safetensors") or f.endswith(".bin")
        for f in os.listdir(MODEL_CACHE) if os.path.isfile(os.path.join(MODEL_CACHE, f))
    ):
        return MODEL_CACHE
    return MODEL_NAME


def finetune_one_run(condition, seed, gpu_id=1, dry_run=False):
    """Run one LoRA finetune + WikiText-103 PPL eval."""
    import torch
    from torch.utils.data import Dataset
    from transformers import (
        AutoModelForCausalLM, AutoTokenizer,
        TrainingArguments, Trainer, DataCollatorForLanguageModeling,
    )
    from peft import LoraConfig, get_peft_model, PeftModel
    from datasets import load_dataset

    out_dir = f"{RESULT_DIR}/{condition}/seed_{seed}"
    adapter_dir = f"{out_dir}/adapter"
    ppl_path = f"{out_dir}/ppl_result.json"

    if os.path.exists(ppl_path):
        print(f"  SKIP {condition}/seed_{seed} — already done")
        return

    os.makedirs(adapter_dir, exist_ok=True)
    data_path = f"{OUTPUT_DATA_DIR}/{condition}.jsonl"

    print(f"\n{'='*50}")
    print(f"  Finetune: {condition} | seed={seed}")
    print(f"  Data: {data_path}")
    print(f"{'='*50}")

    model_path = get_model_path()
    print(f"  Model path: {model_path}")
    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # --- Build dataset ---
    class TextDataset(Dataset):
        def __init__(self, path, tok, max_len):
            self.examples = []
            with open(path) as f:
                for line in f:
                    rec = json.loads(line)
                    enc = tok(rec["text"], truncation=True, max_length=max_len, padding=False)
                    self.examples.append(enc)

        def __len__(self):
            return len(self.examples)

        def __getitem__(self, idx):
            return {k: torch.tensor(v) for k, v in self.examples[idx].items()}

    dataset = TextDataset(data_path, tokenizer, 512)
    print(f"  Dataset size: {len(dataset)}")

    # --- Load model + LoRA ---
    model = AutoModelForCausalLM.from_pretrained(
        model_path, torch_dtype=torch.bfloat16, trust_remote_code=True,
    )
    lora_config = LoraConfig(
        r=16, lora_alpha=32,
        target_modules=["query_key_value"],
        lora_dropout=0.05, bias="none", task_type="CAUSAL_LM",
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    # --- Training ---
    training_args = TrainingArguments(
        output_dir=adapter_dir,
        num_train_epochs=3,
        per_device_train_batch_size=8,
        gradient_accumulation_steps=4,
        learning_rate=2e-4,
        warmup_ratio=0.05,
        weight_decay=0.01,
        lr_scheduler_type="cosine",
        bf16=True,
        logging_steps=10,
        save_strategy="no",
        seed=seed,
        report_to="none",
        remove_unused_columns=False,
        dataloader_pin_memory=True,
        dataloader_num_workers=2,
    )

    data_collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)
    trainer = Trainer(
        model=model, args=training_args,
        train_dataset=dataset, data_collator=data_collator,
    )

    t0 = time.time()
    result = trainer.train()
    train_time = time.time() - t0
    print(f"  Training done in {train_time:.0f}s. Loss: {result.training_loss:.4f}")

    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)

    # --- PPL Evaluation ---
    print("  Evaluating WikiText-103 PPL...")
    ppl = eval_wikitext_ppl(model, tokenizer, model.device)

    # --- Save result ---
    ppl_result = {
        "condition": condition,
        "seed": seed,
        "perplexity": ppl,
        "train_loss": result.training_loss,
        "train_time_s": round(train_time, 1),
        "n_samples": len(dataset),
    }
    with open(ppl_path, "w") as f:
        json.dump(ppl_result, f, indent=2)
    print(f"  PPL={ppl:.2f} -> {ppl_path}")

    del model, trainer
    torch.cuda.empty_cache()
    return ppl_result


def eval_wikitext_ppl(model, tokenizer, device, stride=512, max_length=1024):
    """Sliding-window perplexity on WikiText-103 test set."""
    import torch
    from datasets import load_dataset

    cache_path = f"{PROJECT_ROOT}/data/wikitext103_test.txt"
    if os.path.exists(cache_path):
        with open(cache_path) as f:
            text = f.read()
    else:
        ds = load_dataset("wikitext", "wikitext-103-raw-v1", split="test")
        text = "\n\n".join(ds["text"])
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        with open(cache_path, "w") as f:
            f.write(text)

    encodings = tokenizer(text, return_tensors="pt")
    seq_len = encodings.input_ids.size(1)

    nlls = []
    prev_end = 0
    for begin_loc in range(0, seq_len, stride):
        end_loc = min(begin_loc + max_length, seq_len)
        trg_len = end_loc - prev_end
        input_ids = encodings.input_ids[:, begin_loc:end_loc].to(device)

        target_ids = input_ids.clone()
        target_ids[:, :-trg_len] = -100

        with torch.no_grad():
            outputs = model(input_ids, labels=target_ids)
            neg_log_likelihood = outputs.loss

        nlls.append(neg_log_likelihood.item() * trg_len)
        prev_end = end_loc

        if end_loc >= seq_len:
            break

    ppl = math.exp(sum(nlls) / prev_end)
    return ppl


def phase_finetune(conditions=None, seeds=None, gpu_id=1, dry_run=False):
    import torch

    os.environ["CUDA_VISIBLE_DEVICES"] = str(gpu_id)

    if conditions is None:
        conditions = CONDITIONS
    if seeds is None:
        seeds = SEEDS

    print("=" * 60)
    print(f"Phase 2: Finetune + Eval")
    print(f"  Conditions: {conditions}")
    print(f"  Seeds: {seeds}")
    print(f"  GPU: cuda:{gpu_id} (CUDA_VISIBLE_DEVICES={gpu_id})")
    print(f"  Total runs: {len(conditions) * len(seeds)}")
    print("=" * 60)

    model_path = get_model_path()
    print(f"  Model path: {model_path}")

    total = len(conditions) * len(seeds)
    done = 0
    for cond in conditions:
        for seed in seeds:
            done += 1
            print(f"\n[{done}/{total}] {cond} seed={seed}")
            finetune_one_run(cond, seed, gpu_id=gpu_id, dry_run=dry_run)

    print(f"\nAll {total} runs complete.")


# ============================================================
# Phase 3: Analysis
# ============================================================

def phase_analyze():
    from scipy import stats

    print("=" * 60)
    print("Phase 3: Analysis")
    print("=" * 60)

    results = {}
    for cond in CONDITIONS:
        ppls = []
        for seed in SEEDS:
            ppl_path = f"{RESULT_DIR}/{cond}/seed_{seed}/ppl_result.json"
            if not os.path.exists(ppl_path):
                print(f"  WARNING: missing {ppl_path}")
                continue
            with open(ppl_path) as f:
                ppls.append(json.load(f)["perplexity"])
        if ppls:
            results[cond] = np.array(ppls)
            print(f"  {cond}: {len(ppls)} seeds loaded, PPL={np.mean(ppls):.2f}±{np.std(ppls):.2f}")
        else:
            print(f"  {cond}: NO results found")

    if "unfiltered" not in results:
        print("ERROR: unfiltered baseline missing, cannot analyze.")
        return

    baseline = results["unfiltered"]
    summary = {"conditions": {}}

    print(f"\n{'Condition':<20} {'PPL':>12} {'Δ':>8} {'p-value':>10} {'Cohen d':>10} {'Sig':>5}")
    print("-" * 70)

    for cond in CONDITIONS:
        if cond not in results:
            continue
        vals = results[cond]
        entry = {
            "ppl_mean": round(float(vals.mean()), 4),
            "ppl_std": round(float(vals.std()), 4),
            "n_seeds": len(vals),
        }

        if cond != "unfiltered":
            delta = baseline.mean() - vals.mean()
            t_stat, p_val = stats.ttest_rel(baseline, vals)
            pooled_std = np.sqrt((baseline.std()**2 + vals.std()**2) / 2)
            cohens_d = delta / pooled_std if pooled_std > 0 else 0.0
            sig = "***" if p_val < 0.001 else "**" if p_val < 0.01 else "*" if p_val < 0.05 else ""

            entry.update({
                "delta_vs_unfiltered": round(float(delta), 4),
                "p_value": round(float(p_val), 6),
                "t_statistic": round(float(t_stat), 4),
                "cohens_d": round(float(cohens_d), 4),
                "significant_0.05": p_val < 0.05,
            })
            print(f"  {cond:<18} {vals.mean():>8.2f}±{vals.std():.2f} {delta:>+8.2f} {p_val:>10.4f} {cohens_d:>10.3f} {sig:>5}")
        else:
            print(f"  {cond:<18} {vals.mean():>8.2f}±{vals.std():.2f} {'(base)':>8}")

        summary["conditions"][cond] = entry

    summary_path = f"{RESULT_DIR}/summary.json"
    os.makedirs(RESULT_DIR, exist_ok=True)
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSummary saved to {summary_path}")


# ============================================================
# Main
# ============================================================

def parse_args():
    p = argparse.ArgumentParser(description="Downstream Curation PoC")
    p.add_argument("--phase", required=True, choices=["data_prep", "finetune", "analyze"],
                    help="Which phase to run")
    p.add_argument("--gpu", type=int, default=1, help="GPU device index")
    p.add_argument("--conditions", nargs="+", default=None,
                    help="Subset of conditions to finetune (default: all 8)")
    p.add_argument("--seeds", nargs="+", type=int, default=None,
                    help="Subset of seeds (default: all 5)")
    p.add_argument("--dry-run", action="store_true",
                    help="Run only 1 condition x 1 seed for validation")
    return p.parse_args()


def main():
    args = parse_args()

    if args.phase == "data_prep":
        phase_data_prep()

    elif args.phase == "finetune":
        conditions = args.conditions or CONDITIONS
        seeds = args.seeds or SEEDS
        if args.dry_run:
            conditions = [conditions[0]]
            seeds = [seeds[0]]
        phase_finetune(conditions=conditions, seeds=seeds, gpu_id=args.gpu)

    elif args.phase == "analyze":
        phase_analyze()


if __name__ == "__main__":
    main()
