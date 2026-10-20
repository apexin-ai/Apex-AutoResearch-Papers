"""Phase 0: Property orthogonality check.

Fine-tune gen-0, generate synthetic samples, compute 4 property scores,
analyze pairwise correlations, produce scatter plots + heatmap.
"""

import json
import os
import random
import sys
import time
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
from scipy import stats
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model, PeftModel
from trl import SFTTrainer, SFTConfig
from datasets import Dataset

sys.path.insert(0, "/root/autodl-tmp/pgpf")
from pgpf.config import PGPFConfig
from pgpf.data_prep import load_dataset_splits, extract_assistant_texts
from pgpf.property_scorer import PropertyScorer
from pgpf.utils import save_jsonl, save_json, set_seed, ensure_dir, logger

MODEL_PATH = "/root/autodl-tmp/.hf_cache/Qwen/Qwen2.5-1.5B"
EMBED_MODEL = "dunzhang/stella_en_1.5B_v5"
DATA_DIR = "/root/autodl-tmp/pgpf/data"
OUTPUT_DIR = "/root/autodl-tmp/pgpf/outputs/phase0"
CHECKPOINT_DIR = "/root/autodl-tmp/pgpf/outputs/phase0/checkpoint"
NUM_SYNTHETIC = 5000
BATCH_SIZE = 8
SEED = 42
DEVICE_FT = "cuda:0"
DEVICE_BASE = "cuda:1"


def step1_finetune(train_data: list[dict]) -> tuple:
    ckpt = Path(CHECKPOINT_DIR)
    if (ckpt / "adapter_config.json").exists():
        logger.info("[Step 1] Checkpoint found, loading from disk...")
        tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
        if tokenizer.pad_token is None:
            tokenizer.pad_token = tokenizer.eos_token
        base_model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH, torch_dtype=torch.bfloat16,
            device_map={"": DEVICE_FT}, trust_remote_code=True,
        )
        model = PeftModel.from_pretrained(base_model, str(ckpt))
        logger.info("[Step 1] Checkpoint loaded.")
        return model, tokenizer

    logger.info(f"[Step 1] Fine-tuning on {len(train_data)} samples...")
    cfg = PGPFConfig()

    tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16,
        device_map={"": DEVICE_FT}, trust_remote_code=True,
    )

    lora_config = LoraConfig(
        r=cfg.lora.r, lora_alpha=cfg.lora.lora_alpha,
        lora_dropout=cfg.lora.lora_dropout,
        target_modules=cfg.lora.target_modules,
        task_type=cfg.lora.task_type,
    )
    model = get_peft_model(model, lora_config)
    model.print_trainable_parameters()

    train_ds = Dataset.from_list(train_data)

    training_args = SFTConfig(
        output_dir=str(ckpt),
        per_device_train_batch_size=cfg.training.per_device_train_batch_size,
        gradient_accumulation_steps=cfg.training.gradient_accumulation_steps,
        learning_rate=cfg.training.learning_rate,
        lr_scheduler_type=cfg.training.lr_scheduler_type,
        warmup_steps=cfg.training.warmup_steps,
        num_train_epochs=cfg.training.num_train_epochs,
        max_length=cfg.training.max_seq_length,
        bf16=cfg.training.bf16,
        logging_steps=cfg.training.logging_steps,
        save_strategy="no",
        report_to="none",
        seed=SEED,
    )

    trainer = SFTTrainer(
        model=model, args=training_args,
        train_dataset=train_ds, processing_class=tokenizer,
    )
    trainer.train()
    trainer.save_model(str(ckpt))
    logger.info(f"[Step 1] Fine-tuning complete, checkpoint saved to {ckpt}")
    return model, tokenizer


def step2_generate(model, tokenizer, train_data: list[dict]) -> list[dict]:
    logger.info(f"[Step 2] Generating {NUM_SYNTHETIC} synthetic samples (batch_size={BATCH_SIZE})...")
    cfg = PGPFConfig()

    prompts = []
    for sample in train_data:
        msgs = sample["messages"]
        context = [m for m in msgs if m["role"] in ("system", "user")]
        if context:
            prompts.append(context)

    random.shuffle(prompts)
    prompts = prompts[:NUM_SYNTHETIC]

    model.eval()
    tokenizer.padding_side = "left"
    synthetic = []
    n_total = len(prompts)

    for batch_start in range(0, n_total, BATCH_SIZE):
        batch_prompts = prompts[batch_start:batch_start + BATCH_SIZE]
        prompt_texts = [
            tokenizer.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)
            for msgs in batch_prompts
        ]

        try:
            inputs = tokenizer(
                prompt_texts, return_tensors="pt", truncation=True,
                max_length=cfg.training.max_seq_length, padding=True,
            )
            input_ids = inputs.input_ids.to(model.device)
            attention_mask = inputs.attention_mask.to(model.device)

            with torch.no_grad():
                outputs = model.generate(
                    input_ids, attention_mask=attention_mask,
                    max_new_tokens=cfg.generation.max_new_tokens,
                    temperature=cfg.generation.temperature,
                    top_p=cfg.generation.top_p,
                    do_sample=cfg.generation.do_sample,
                    pad_token_id=tokenizer.pad_token_id,
                )

            for i, context_msgs in enumerate(batch_prompts):
                new_tokens = outputs[i][input_ids.shape[1]:]
                response = tokenizer.decode(new_tokens, skip_special_tokens=True)
                synthetic.append({"messages": list(context_msgs) + [{"role": "assistant", "content": response}]})

        except Exception as e:
            logger.warning(f"Batch failed at {batch_start}: {e}, falling back to per-sample")
            for context_msgs in batch_prompts:
                try:
                    pt = tokenizer.apply_chat_template(context_msgs, tokenize=False, add_generation_prompt=True)
                    inp = tokenizer(pt, return_tensors="pt", truncation=True, max_length=cfg.training.max_seq_length)
                    ids = inp.input_ids.to(model.device)
                    mask = torch.ones_like(ids)
                    with torch.no_grad():
                        out = model.generate(
                            ids, attention_mask=mask,
                            max_new_tokens=cfg.generation.max_new_tokens,
                            temperature=cfg.generation.temperature,
                            top_p=cfg.generation.top_p,
                            do_sample=cfg.generation.do_sample,
                            pad_token_id=tokenizer.pad_token_id,
                        )
                    response = tokenizer.decode(out[0][ids.shape[1]:], skip_special_tokens=True)
                    synthetic.append({"messages": list(context_msgs) + [{"role": "assistant", "content": response}]})
                except Exception as e2:
                    logger.warning(f"Sample failed: {e2}, skipping")

        if (batch_start + BATCH_SIZE) % 100 < BATCH_SIZE or batch_start + BATCH_SIZE >= n_total:
            logger.info(f"  [Step 2] Generated {len(synthetic)}/{n_total} samples")

    logger.info(f"[Step 2] Generation complete: {len(synthetic)} samples")
    return synthetic


def step3_score(synthetic: list[dict], ft_model, ft_tokenizer, gen0_texts: list[str]) -> list[dict]:
    logger.info(f"[Step 3] Scoring {len(synthetic)} samples on 4 properties...")

    scorer = PropertyScorer(
        embedding_model_name=EMBED_MODEL,
        corpus_k=50,
        device=DEVICE_BASE,
    )
    logger.info("  Setting reference corpus (embedding gen-0 texts)...")
    scorer.set_reference_corpus(gen0_texts)

    synthetic_texts = extract_assistant_texts(synthetic)

    logger.info(f"  Loading base model on {DEVICE_BASE} for quality scoring...")
    base_tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True)
    if base_tokenizer.pad_token is None:
        base_tokenizer.pad_token = base_tokenizer.eos_token
    base_model = AutoModelForCausalLM.from_pretrained(
        MODEL_PATH, torch_dtype=torch.bfloat16,
        device_map={"": DEVICE_BASE}, trust_remote_code=True,
    )
    base_model.eval()

    logger.info("  Running score_batch (lexical, semantic, quality, confidence)...")
    scores = scorer.score_batch(
        synthetic_texts,
        model=ft_model,
        tokenizer=ft_tokenizer,
        base_model=base_model,
        base_tokenizer=base_tokenizer,
    )

    scored = []
    for sample, score in zip(synthetic, scores):
        scored.append({**sample, "scores": score})

    del base_model
    torch.cuda.empty_cache()

    logger.info(f"[Step 3] Scoring complete.")
    return scored


def step4_correlation(scored_samples: list[dict]) -> dict:
    logger.info("[Step 4] Computing pairwise correlations...")
    props = ["lexical_conformity", "semantic_novelty", "quality", "confidence"]
    arrays = {p: np.array([s["scores"][p] for s in scored_samples]) for p in props}

    corr = {"pearson": {}, "spearman": {}}
    for i in range(len(props)):
        for j in range(i + 1, len(props)):
            p1, p2 = props[i], props[j]
            pair_key = f"{p1}_vs_{p2}"
            r_p, pval_p = stats.pearsonr(arrays[p1], arrays[p2])
            r_s, pval_s = stats.spearmanr(arrays[p1], arrays[p2])
            corr["pearson"][pair_key] = {"r": round(float(r_p), 4), "p_value": round(float(pval_p), 6)}
            corr["spearman"][pair_key] = {"rho": round(float(r_s), 4), "p_value": round(float(pval_s), 6)}
            logger.info(f"  {pair_key}: Pearson r={r_p:.4f}, Spearman rho={r_s:.4f}")

    return corr


def step5_visualize(scored_samples: list[dict], output_dir: str) -> None:
    logger.info("[Step 5] Generating visualizations...")
    props = ["lexical_conformity", "semantic_novelty", "quality", "confidence"]
    labels = {
        "lexical_conformity": "Lexical Conformity",
        "semantic_novelty": "Semantic Novelty",
        "quality": "Quality (PPL)",
        "confidence": "Confidence (log-prob)",
    }
    arrays = {p: np.array([s["scores"][p] for s in scored_samples]) for p in props}

    pairs = [(i, j) for i in range(len(props)) for j in range(i + 1, len(props))]
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))
    axes = axes.flatten()

    for idx, (i, j) in enumerate(pairs):
        ax = axes[idx]
        p1, p2 = props[i], props[j]
        n = len(scored_samples)
        plot_idx = np.random.choice(n, min(2000, n), replace=False)
        ax.scatter(arrays[p1][plot_idx], arrays[p2][plot_idx], alpha=0.3, s=5)
        r_p, _ = stats.pearsonr(arrays[p1], arrays[p2])
        ax.set_xlabel(labels[p1])
        ax.set_ylabel(labels[p2])
        ax.set_title(f"r={r_p:.3f}")

    plt.tight_layout()
    scatter_path = str(Path(output_dir) / "scatter_plots.png")
    plt.savefig(scatter_path, dpi=150)
    plt.close()
    logger.info(f"  Scatter plots -> {scatter_path}")

    n_props = len(props)
    corr_matrix = np.eye(n_props)
    for i in range(n_props):
        for j in range(i + 1, n_props):
            r, _ = stats.pearsonr(arrays[props[i]], arrays[props[j]])
            corr_matrix[i, j] = r
            corr_matrix[j, i] = r

    fig, ax = plt.subplots(figsize=(8, 6))
    im = ax.imshow(corr_matrix, cmap="RdBu_r", vmin=-1, vmax=1)
    ax.set_xticks(range(n_props))
    ax.set_yticks(range(n_props))
    ax.set_xticklabels([labels[p] for p in props], rotation=45, ha="right")
    ax.set_yticklabels([labels[p] for p in props])
    for i in range(n_props):
        for j in range(n_props):
            ax.text(j, i, f"{corr_matrix[i, j]:.3f}", ha="center", va="center",
                    color="white" if abs(corr_matrix[i, j]) > 0.5 else "black")
    plt.colorbar(im, label="Pearson r")
    plt.tight_layout()
    heatmap_path = str(Path(output_dir) / "correlation_heatmap.png")
    plt.savefig(heatmap_path, dpi=150)
    plt.close()
    logger.info(f"  Heatmap -> {heatmap_path}")


def check_pass_criteria(corr: dict) -> bool:
    logger.info("[Check] Evaluating pass criteria...")
    passed = True

    for pair_key, vals in corr["pearson"].items():
        r = abs(vals["r"])
        if r > 0.7:
            logger.warning(f"  FAIL: {pair_key} |Pearson r|={r:.4f} > 0.7")
            passed = False

    lc_conf_key = "lexical_conformity_vs_confidence"
    if lc_conf_key in corr["pearson"]:
        r = abs(corr["pearson"][lc_conf_key]["r"])
        if r >= 0.5:
            logger.warning(f"  FAIL: LC vs Confidence |r|={r:.4f} >= 0.5")
            passed = False

    return passed


def main():
    t0 = time.time()
    set_seed(SEED)
    ensure_dir(OUTPUT_DIR)

    data_splits = load_dataset_splits(DATA_DIR)
    train_data = data_splits["train"]
    gen0_texts = extract_assistant_texts(train_data)
    logger.info(f"Loaded {len(train_data)} train samples, {len(gen0_texts)} gen-0 texts.")

    ft_model, ft_tokenizer = step1_finetune(train_data)

    synthetic = step2_generate(ft_model, ft_tokenizer, train_data)
    save_jsonl(synthetic, Path(OUTPUT_DIR) / "synthetic.jsonl")
    logger.info(f"Saved {len(synthetic)} synthetic samples.")

    scored = step3_score(synthetic, ft_model, ft_tokenizer, gen0_texts)
    save_jsonl(scored, Path(OUTPUT_DIR) / "scored_samples.jsonl")

    del ft_model
    torch.cuda.empty_cache()

    corr = step4_correlation(scored)
    save_json(corr, Path(OUTPUT_DIR) / "correlation_matrix.json")

    step5_visualize(scored, OUTPUT_DIR)

    passed = check_pass_criteria(corr)
    elapsed = time.time() - t0

    result_str = "PASS" if passed else "FAIL"
    logger.info(f"\n{'='*60}")
    logger.info(f"Phase 0 Orthogonality Check: {result_str}")
    logger.info(f"Total time: {elapsed/60:.1f} minutes")
    logger.info(f"{'='*60}")

    summary = {
        "result": result_str,
        "correlation": corr,
        "elapsed_minutes": round(elapsed / 60, 1),
        "num_scored": len(scored),
    }
    save_json(summary, Path(OUTPUT_DIR) / "summary.json")
    print(f"\n>>> Phase 0 Result: {result_str} <<<")


if __name__ == "__main__":
    main()
