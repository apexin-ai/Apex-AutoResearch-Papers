"""exp009 Dose-Response — graduated vs binary filtering at varying synthetic injection ratios.

Measures downstream LM quality (MMLU/HellaSwag) after continued pretraining on data
with 10%/30%/50% synthetic injection, filtered by graduated vs binary-ours strategies.
Fixed dataset size (default 5000) across all ratios ensures training cost parity.

Input:  data/ directory (features.csv + depth_*.jsonl, same as exp-006)
        Qwen2.5-1.5B-Instruct base model (local path or HF hub)
Output: outputs/exp009/r<ratio>_<strategy>_s<seed>/eval_results.json  (per-run)
        outputs/exp009/analysis.json                                   (paired t-tests)

Usage:
    # Dry-run: 1 seed, 200 samples, 10 training steps, hellaswag-only eval (limit=20)
    python run_exp009_dose_response.py --dry-run

    # Full experiment (30 runs)
    python run_exp009_dose_response.py

    # Single config
    python run_exp009_dose_response.py --ratios 0.3 --strategies graduated --seeds 42

    # Analyze existing results only
    python run_exp009_dose_response.py --analyze-only

Dependencies: torch, transformers, peft, lightgbm, lm_eval, numpy, pandas, scipy
"""

import argparse
import json
import os
import sys
import time
import traceback
from collections import defaultdict

import numpy as np
import pandas as pd
import torch
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
    set_seed,
)
from peft import LoraConfig, get_peft_model, TaskType
from scipy import stats

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from exp006_filtering_strategies import STRATEGIES, FEATURE_COLS, load_data


def prepare_dose_data(df, texts, ratio, seed, total_n):
    """Subsample a fixed-size dataset at the target synthetic injection ratio.

    Samples without replacement from human (depth=0) and synthetic (depth>0)
    pools to construct a dataset where exactly ratio*total_n samples are synthetic.
    All strategies at the same (ratio, seed) see identical data for fair comparison.
    """
    rng = np.random.RandomState(seed)

    human_idx = np.where(df["depth"].values == 0)[0]
    synthetic_idx = np.where(df["depth"].values > 0)[0]

    n_synthetic = int(round(total_n * ratio))
    n_human = total_n - n_synthetic

    if n_human > len(human_idx):
        raise ValueError(f"Need {n_human} human samples but only have {len(human_idx)}")
    if n_synthetic > len(synthetic_idx):
        raise ValueError(f"Need {n_synthetic} synthetic samples but only have {len(synthetic_idx)}")

    sel_h = rng.choice(human_idx, size=n_human, replace=False)
    sel_s = rng.choice(synthetic_idx, size=n_synthetic, replace=False)

    selected = np.concatenate([sel_h, sel_s])
    rng.shuffle(selected)

    sub_df = df.iloc[selected].reset_index(drop=True)
    sub_texts = [texts[i] for i in selected]
    return sub_df, sub_texts


class TextDataset(Dataset):
    def __init__(self, texts, tokenizer, max_length=512):
        self.texts = texts
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx],
            truncation=True,
            max_length=self.max_length,
            padding=False,
            return_attention_mask=False,
        )
        return {"input_ids": enc["input_ids"]}


def make_weighted_trainer(weights_array):
    """Trainer subclass that uses WeightedRandomSampler when weights are non-uniform."""
    uniform = np.allclose(weights_array, 1.0)

    class WeightedTrainer(Trainer):
        def get_train_dataloader(self):
            if uniform:
                return super().get_train_dataloader()
            sampler = WeightedRandomSampler(
                weights=weights_array.tolist(),
                num_samples=len(weights_array),
                replacement=True,
            )
            return DataLoader(
                self.train_dataset,
                batch_size=self.args.per_device_train_batch_size,
                sampler=sampler,
                collate_fn=self.data_collator,
                num_workers=self.args.dataloader_num_workers,
                pin_memory=self.args.dataloader_pin_memory,
            )

    return WeightedTrainer


def train_one(model_name, texts, weights, output_dir, seed, args):
    """LoRA continued pretraining on weighted text data. Returns adapter path."""
    set_seed(seed)
    os.makedirs(output_dir, exist_ok=True)

    tokenizer = AutoTokenizer.from_pretrained(
        model_name, cache_dir=args.cache_dir, trust_remote_code=True,
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        model_name, cache_dir=args.cache_dir,
        torch_dtype=torch.bfloat16, trust_remote_code=True,
    )

    lora_config = LoraConfig(
        task_type=TaskType.CAUSAL_LM,
        r=args.lora_rank,
        lora_alpha=args.lora_alpha,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
    )
    model = get_peft_model(model, lora_config)

    dataset = TextDataset(texts, tokenizer, args.max_length)
    collator = DataCollatorForLanguageModeling(tokenizer=tokenizer, mlm=False)

    n_epochs = 1 if args.dry_run else args.epochs
    max_steps = 10 if args.dry_run else -1
    log_steps = 5 if args.dry_run else 50

    training_args = TrainingArguments(
        output_dir=output_dir,
        num_train_epochs=n_epochs,
        max_steps=max_steps,
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        learning_rate=args.lr,
        warmup_ratio=args.warmup_ratio,
        bf16=True,
        logging_steps=log_steps,
        save_strategy="no",
        seed=seed,
        report_to="none",
        dataloader_num_workers=2,
        dataloader_pin_memory=True,
        remove_unused_columns=False,
    )

    TrainerCls = make_weighted_trainer(weights)
    trainer = TrainerCls(
        model=model,
        args=training_args,
        train_dataset=dataset,
        data_collator=collator,
    )

    print("    Training...")
    train_result = trainer.train()
    print(f"    Train loss: {train_result.training_loss:.4f}")

    adapter_dir = os.path.join(output_dir, "final_adapter")
    model.save_pretrained(adapter_dir)
    tokenizer.save_pretrained(adapter_dir)

    metrics = {
        "train_loss": train_result.training_loss,
        "train_runtime": train_result.metrics.get("train_runtime", 0),
        "train_samples_per_second": train_result.metrics.get("train_samples_per_second", 0),
    }
    with open(os.path.join(output_dir, "train_metrics.json"), "w") as f:
        json.dump(metrics, f, indent=2)

    del model, trainer
    torch.cuda.empty_cache()
    return adapter_dir


def evaluate_one(model_name, adapter_path, output_path, args):
    """Run lm-eval-harness (MMLU + HellaSwag). Returns result dict with scores."""
    import lm_eval

    model_args = f"pretrained={model_name},dtype=bfloat16,trust_remote_code=True"
    if args.cache_dir:
        model_args += f",cache_dir={args.cache_dir}"
    if adapter_path:
        model_args += f",peft={adapter_path}"

    tasks = ["hellaswag"] if args.dry_run else args.tasks
    limit = 20 if args.dry_run else None

    print(f"    Evaluating: tasks={tasks}" + (f" limit={limit}" if limit else ""))

    results = lm_eval.simple_evaluate(
        model="hf",
        model_args=model_args,
        tasks=tasks,
        batch_size=args.eval_batch_size,
        device="cuda:0",
        limit=limit,
    )

    scores = {}
    for task_name, task_results in results["results"].items():
        task_scores = {}
        for metric, value in task_results.items():
            if isinstance(value, (int, float)):
                task_scores[metric] = value
        scores[task_name] = task_scores

    output = {
        "model": model_name,
        "adapter": adapter_path,
        "tasks": tasks,
        "scores": scores,
    }

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    for task, s in scores.items():
        main_metric = s.get("acc_norm,none", s.get("acc,none", "N/A"))
        print(f"    {task}: {main_metric}")

    torch.cuda.empty_cache()
    return output


def extract_scores(result):
    """Pull MMLU acc and HellaSwag acc_norm from lm-eval result JSON."""
    scores = result.get("scores", {})
    mmlu = hellaswag = None
    for task_name, metrics in scores.items():
        if "mmlu" in task_name.lower():
            mmlu = metrics.get("acc,none", metrics.get("acc_norm,none"))
        if "hellaswag" in task_name.lower():
            hellaswag = metrics.get("acc_norm,none", metrics.get("acc,none"))
    return mmlu, hellaswag


def analyze(results_dir, output_path=None):
    """Aggregate results across the ratio x strategy x seed grid and run paired t-tests."""
    import re
    from glob import glob

    result_files = sorted(glob(os.path.join(results_dir, "*/eval_results.json")))
    if not result_files:
        print(f"No results found in {results_dir}")
        return None

    # ratio -> strategy -> {seeds, mmlu, hellaswag}
    data = defaultdict(lambda: defaultdict(lambda: {"seeds": [], "mmlu": [], "hellaswag": []}))

    for fpath in result_files:
        dirname = os.path.basename(os.path.dirname(fpath))
        m = re.match(r"r([\d.]+)_(.+)_s(\d+)", dirname)
        if not m:
            continue
        ratio = float(m.group(1))
        strategy = m.group(2)
        seed = int(m.group(3))

        with open(fpath) as f:
            result = json.load(f)
        mmlu, hellaswag = extract_scores(result)

        data[ratio][strategy]["seeds"].append(seed)
        data[ratio][strategy]["mmlu"].append(mmlu)
        data[ratio][strategy]["hellaswag"].append(hellaswag)

    print("\n" + "=" * 80)
    print("exp009 Dose-Response Results")
    print("=" * 80)

    summary = {}
    all_ttests = {}

    for ratio in sorted(data.keys()):
        print(f"\n--- Injection ratio: {ratio*100:.0f}% ---")
        print(f"{'Strategy':>15}  {'N':>3}  {'MMLU':>18}  {'HellaSwag':>18}")

        ratio_summary = {}
        for strategy in sorted(data[ratio].keys()):
            d = data[ratio][strategy]
            n = len(d["seeds"])
            mmlu_vals = [x for x in d["mmlu"] if x is not None]
            hs_vals = [x for x in d["hellaswag"] if x is not None]

            mmlu_str = f"{np.mean(mmlu_vals):.4f} +/- {np.std(mmlu_vals):.4f}" if mmlu_vals else "N/A"
            hs_str = f"{np.mean(hs_vals):.4f} +/- {np.std(hs_vals):.4f}" if hs_vals else "N/A"
            print(f"{strategy:>15}  {n:>3}  {mmlu_str:>18}  {hs_str:>18}")

            ratio_summary[strategy] = {
                "n": n,
                "mmlu_mean": float(np.mean(mmlu_vals)) if mmlu_vals else None,
                "mmlu_std": float(np.std(mmlu_vals)) if mmlu_vals else None,
                "hellaswag_mean": float(np.mean(hs_vals)) if hs_vals else None,
                "hellaswag_std": float(np.std(hs_vals)) if hs_vals else None,
            }

        summary[str(ratio)] = ratio_summary

        # Paired t-tests within this ratio
        comparisons = [
            ("graduated", "binary-ours"),
            ("graduated", "no-filter"),
            ("binary-ours", "no-filter"),
        ]

        print(f"\n  Paired t-tests:")
        for sa, sb in comparisons:
            da, db = data[ratio].get(sa), data[ratio].get(sb)
            if not da or not db:
                continue
            common_seeds = sorted(set(da["seeds"]) & set(db["seeds"]))
            if len(common_seeds) < 2:
                print(f"    {sa} vs {sb}: insufficient paired data (n={len(common_seeds)})")
                continue

            for metric in ["mmlu", "hellaswag"]:
                vals_a = [da[metric][da["seeds"].index(s)] for s in common_seeds]
                vals_b = [db[metric][db["seeds"].index(s)] for s in common_seeds]
                if any(v is None for v in vals_a + vals_b):
                    continue
                t_stat, p_val = stats.ttest_rel(vals_a, vals_b)
                sig = " **" if p_val < 0.01 else (" *" if p_val < 0.05 else "")
                diff = np.mean(vals_a) - np.mean(vals_b)
                print(f"    {sa} vs {sb} ({metric}): "
                      f"diff={diff:+.4f}, t={t_stat:.3f}, p={p_val:.4f}, n={len(common_seeds)}{sig}")
                key = f"r{ratio}_{sa}_vs_{sb}_{metric}"
                all_ttests[key] = {
                    "t": float(t_stat), "p": float(p_val),
                    "n": len(common_seeds), "mean_diff": float(diff),
                }

    output = {"summary": summary, "paired_ttests": all_ttests}

    if output_path:
        os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
        with open(output_path, "w") as f:
            json.dump(output, f, indent=2)
        print(f"\nAnalysis saved to {output_path}")

    return output


def main():
    parser = argparse.ArgumentParser(
        description="exp009: Dose-response — graduated vs binary filtering "
                    "at varying synthetic injection ratios",
    )

    # Data & model
    parser.add_argument("--data-dir", type=str, default="data/")
    parser.add_argument(
        "--model-name", type=str,
        default="/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B-Instruct/"
                "Qwen/Qwen2___5-1___5B-Instruct",
    )
    parser.add_argument("--output-dir", type=str, default="outputs/exp009")
    parser.add_argument("--cache-dir", type=str, default="/root/autodl-tmp/.hf_cache")

    # Experiment grid
    parser.add_argument("--ratios", type=float, nargs="+", default=[0.1, 0.3, 0.5],
                        help="Synthetic injection ratios to test")
    parser.add_argument("--strategies", type=str, nargs="+",
                        default=["binary-ours", "graduated"],
                        choices=["no-filter", "binary-ours", "graduated"])
    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 123, 456, 789, 1024])
    parser.add_argument("--total-n", type=int, default=5000,
                        help="Fixed total dataset size per injection ratio")

    # Graduated filter params
    parser.add_argument("--alpha", type=float, default=0.5,
                        help="Exponential decay param for graduated strategy "
                             "(update to best alpha from exp-006 when available)")

    # Training hyperparams (identical to exp-006 defaults)
    parser.add_argument("--max-length", type=int, default=512)
    parser.add_argument("--lr", type=float, default=2e-5)
    parser.add_argument("--batch-size", type=int, default=4)
    parser.add_argument("--gradient-accumulation-steps", type=int, default=8)
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--warmup-ratio", type=float, default=0.1)
    parser.add_argument("--lora-rank", type=int, default=8)
    parser.add_argument("--lora-alpha", type=int, default=16)

    # Evaluation
    parser.add_argument("--tasks", type=str, nargs="+", default=["mmlu", "hellaswag"])
    parser.add_argument("--eval-batch-size", type=str, default="auto")

    # Run modes
    parser.add_argument("--dry-run", action="store_true",
                        help="Quick validation: 1 ratio, 1 seed, 200 samples, "
                             "10 training steps, hellaswag-only with limit=20")
    parser.add_argument("--analyze-only", action="store_true",
                        help="Skip training/eval, just analyze existing results")
    parser.add_argument("--skip-eval", action="store_true",
                        help="Train only, skip lm-eval (for debugging)")

    args = parser.parse_args()

    # --- Analyze-only mode ---
    if args.analyze_only:
        analyze(args.output_dir, os.path.join(args.output_dir, "analysis.json"))
        return

    # --- Dry-run overrides ---
    if args.dry_run:
        args.ratios = [0.3]
        args.strategies = ["no-filter", "binary-ours", "graduated"]
        args.seeds = [42]
        args.total_n = 200
        print("=" * 60)
        print("DRY RUN MODE")
        print(f"  ratio=0.3, total_n=200, seed=42")
        print(f"  strategies: {args.strategies}")
        print(f"  training: max_steps=10, epochs=1")
        print(f"  eval: hellaswag only, limit=20")
        print("=" * 60)
        print()

    # --- Load full dataset once ---
    print(f"Loading data from {args.data_dir}")
    df, texts, _ = load_data(args.data_dir)
    n_human = (df["depth"] == 0).sum()
    n_synthetic = (df["depth"] > 0).sum()
    print(f"  Total: {len(texts)} samples (human={n_human}, synthetic={n_synthetic})")

    # --- Build experiment grid ---
    configs = []
    for ratio in args.ratios:
        for strategy in args.strategies:
            for seed in args.seeds:
                tag = f"r{ratio}_{strategy}_s{seed}"
                configs.append((ratio, strategy, seed, tag))

    total_runs = len(configs)
    # ~2.5 min train (5K samples) + ~10 min eval (MMLU+HellaSwag) = ~12.5 min/run
    est_min_per_run = 1 if args.dry_run else 13
    est_total_min = total_runs * est_min_per_run

    print(f"\n{'=' * 60}")
    print(f"exp009 Dose-Response Experiment")
    print(f"  Ratios:     {args.ratios}")
    print(f"  Strategies: {args.strategies}")
    print(f"  Seeds:      {args.seeds}")
    print(f"  Total N:    {args.total_n} per ratio")
    print(f"  Alpha:      {args.alpha} (graduated)")
    print(f"  Total runs: {total_runs}")
    print(f"  Est. time:  ~{est_total_min}min ({est_total_min/60:.1f}h)")
    print(f"{'=' * 60}\n")

    os.makedirs(args.output_dir, exist_ok=True)

    # Save experiment config for reproducibility
    exp_config = {
        "experiment": "exp009_dose_response",
        "ratios": args.ratios,
        "strategies": args.strategies,
        "seeds": args.seeds,
        "total_n": args.total_n,
        "alpha": args.alpha,
        "model": args.model_name,
        "hyperparams": {
            "lr": args.lr, "batch_size": args.batch_size,
            "gradient_accumulation_steps": args.gradient_accumulation_steps,
            "epochs": args.epochs, "warmup_ratio": args.warmup_ratio,
            "lora_rank": args.lora_rank, "lora_alpha": args.lora_alpha,
            "max_length": args.max_length,
        },
        "dry_run": args.dry_run,
    }
    with open(os.path.join(args.output_dir, "exp_config.json"), "w") as f:
        json.dump(exp_config, f, indent=2)

    # --- Run grid ---
    completed, failed, skipped = 0, 0, 0

    for idx, (ratio, strategy, seed, tag) in enumerate(configs):
        out_dir = os.path.join(args.output_dir, tag)
        result_file = os.path.join(out_dir, "eval_results.json")

        print(f"[{idx+1}/{total_runs}] {tag}")

        # Skip if results already exist (resume-friendly)
        if os.path.exists(result_file) and not args.dry_run:
            print("  SKIP (results exist)")
            skipped += 1
            completed += 1
            continue

        try:
            t0 = time.time()

            # 1) Prepare dose data at target injection ratio
            sub_df, sub_texts = prepare_dose_data(
                df, texts, ratio, seed, args.total_n,
            )
            features = sub_df[FEATURE_COLS].values
            depths = sub_df["depth"].values
            actual_ratio = (depths > 0).mean()
            print(f"  Data: {len(sub_texts)} samples, "
                  f"synthetic={actual_ratio:.1%} "
                  f"(human={int((1-actual_ratio)*len(sub_texts))}, "
                  f"synth={int(actual_ratio*len(sub_texts))})")

            # 2) Fit filter strategy on this mixture and get weights
            kwargs = {}
            if strategy == "graduated":
                kwargs["alpha"] = args.alpha
            strat = STRATEGIES[strategy](**kwargs)
            strat.fit(features, depths, sub_texts)
            weights = strat.get_weights(features, sub_texts)

            # Remove zero-weight samples
            nonzero = weights > 1e-8
            filtered_texts = [t for t, nz in zip(sub_texts, nonzero) if nz]
            filtered_weights = weights[nonzero]
            print(f"  After filter: {len(filtered_texts)}/{len(sub_texts)} kept "
                  f"({len(filtered_texts)/len(sub_texts)*100:.1f}%), "
                  f"weight mean={filtered_weights.mean():.4f}")

            # Save filter metadata
            os.makedirs(out_dir, exist_ok=True)
            filter_info = {
                "ratio": ratio, "strategy": strategy, "seed": seed,
                "total_n": len(sub_texts),
                "n_after_filter": len(filtered_texts),
                "actual_synthetic_ratio": float(actual_ratio),
                "weight_mean": float(filtered_weights.mean()),
                "weight_std": float(filtered_weights.std()),
            }
            with open(os.path.join(out_dir, "filter_info.json"), "w") as f:
                json.dump(filter_info, f, indent=2)

            # 3) LoRA continued pretraining
            adapter_path = train_one(
                args.model_name, filtered_texts, filtered_weights,
                out_dir, seed, args,
            )

            # 4) lm-eval-harness evaluation
            if not args.skip_eval:
                print("    Evaluating...")
                eval_result = evaluate_one(
                    args.model_name, adapter_path, result_file, args,
                )
                mmlu, hs = extract_scores(eval_result)
                print(f"    => MMLU={mmlu}, HellaSwag={hs}")

            elapsed = time.time() - t0
            print(f"  Done in {elapsed/60:.1f}min")
            completed += 1

        except Exception as e:
            print(f"  FAILED: {e}")
            traceback.print_exc()
            failed += 1
            with open(os.path.join(args.output_dir, "failures.log"), "a") as f:
                f.write(f"{tag}: {e}\n")

    # --- Summary ---
    print(f"\n{'=' * 60}")
    print(f"Complete: {completed}/{total_runs} succeeded "
          f"({skipped} skipped, {failed} failed)")
    print(f"{'=' * 60}")

    # --- Run analysis if we have results ---
    if not args.skip_eval and completed > 0:
        print("\nRunning analysis...")
        analyze(args.output_dir, os.path.join(args.output_dir, "analysis.json"))


if __name__ == "__main__":
    main()
