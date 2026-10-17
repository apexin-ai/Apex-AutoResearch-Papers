#!/usr/bin/env python3
"""R1-W2 FP16 Baseline: AWQ INT4 vs FP16 accuracy on MMLU / ARC-Challenge."""

import gc
import json
import logging
import os
import random
import re
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import torch

os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["TOKENIZERS_PARALLELISM"] = "false"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("/tmp/fp16_baseline.log"),
    ],
)
log = logging.getLogger("fp16_baseline")

SEED = 42
N_SAMPLES = 100

# Ordered: Qwen (ungated) first, then gated models.
# can_fp16 = True only if FP16 fits on single 98GB GPU.
MODELS = [
    {
        "name": "Qwen2.5-14B-Instruct",
        "awq_id": "Qwen/Qwen2.5-14B-Instruct-AWQ",
        "fp16_id": "Qwen/Qwen2.5-14B-Instruct",
        "can_fp16": True,
        "params_b": 14,
    },
    {
        "name": "Qwen2.5-32B-Instruct",
        "awq_id": "Qwen/Qwen2.5-32B-Instruct-AWQ",
        "fp16_id": "Qwen/Qwen2.5-32B-Instruct",
        "can_fp16": True,
        "params_b": 32,
    },
    {
        "name": "Llama-3.1-8B-Instruct",
        "awq_id": "TechxGenus/Meta-Llama-3.1-8B-Instruct-AWQ",
        "fp16_id": "meta-llama/Llama-3.1-8B-Instruct",
        "can_fp16": True,
        "params_b": 8,
    },
    {
        "name": "Qwen2.5-72B-Instruct",
        "awq_id": "Qwen/Qwen2.5-72B-Instruct-AWQ",
        "fp16_id": "Qwen/Qwen2.5-72B-Instruct",
        "can_fp16": False,
        "params_b": 72,
        "skip_reason": "FP16 requires ~144GB VRAM, exceeds single 98GB GPU",
    },
    {
        "name": "Llama-3.1-70B-Instruct",
        "awq_id": "TechxGenus/Meta-Llama-3.1-70B-Instruct-AWQ",
        "fp16_id": "meta-llama/Llama-3.1-70B-Instruct",
        "can_fp16": False,
        "params_b": 70,
        "skip_reason": "FP16 requires ~140GB VRAM, exceeds single 98GB GPU",
    },
    {
        "name": "Mistral-Large-Instruct-2407",
        "awq_id": "TechxGenus/Mistral-Large-Instruct-2407-AWQ",
        "fp16_id": "mistralai/Mistral-Large-Instruct-2407",
        "can_fp16": False,
        "params_b": 123,
        "skip_reason": "FP16 requires ~246GB VRAM, exceeds single 98GB GPU",
    },
]

OUTPUT_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")


def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def load_mmlu_samples(n):
    from datasets import load_dataset
    log.info("Loading MMLU...")
    ds = load_dataset("cais/mmlu", "all", split="test")
    rng = random.Random(SEED)
    indices = rng.sample(range(len(ds)), min(n, len(ds)))
    samples = []
    for i in sorted(indices):
        row = ds[i]
        samples.append({
            "question": row["question"],
            "choices": row["choices"],
            "answer": int(row["answer"]),
        })
    return samples


def load_arc_samples(n):
    from datasets import load_dataset
    log.info("Loading ARC-Challenge...")
    ds = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test")
    rng = random.Random(SEED)
    indices = rng.sample(range(len(ds)), min(n, len(ds)))
    samples = []
    for i in sorted(indices):
        row = ds[i]
        labels = row["choices"]["label"]
        texts = row["choices"]["text"]
        answer_key = row["answerKey"]
        answer_idx = labels.index(answer_key)
        samples.append({
            "question": row["question"],
            "choices": texts,
            "answer": answer_idx,
            "labels": labels,
        })
    return samples


def format_mcq(question, choices, labels=None):
    if labels is None:
        labels = [chr(65 + i) for i in range(len(choices))]
    opts = "\n".join(f"({l}) {c}" for l, c in zip(labels, choices))
    return (
        "Answer the following multiple-choice question. "
        "Reply with ONLY the letter of the correct answer.\n\n"
        f"Question: {question}\n{opts}\n\nAnswer:"
    )


def extract_answer(text):
    text = text.strip()
    m = re.match(r'^[(\[]?([A-Da-d])[)\].]?', text)
    if m:
        return m.group(1).upper()
    m = re.search(r'(?:answer|correct)\s*(?:is|:)\s*[(\[]?([A-Da-d])', text, re.IGNORECASE)
    if m:
        return m.group(1).upper()
    m = re.search(r'\b([A-D])\b', text)
    if m:
        return m.group(1)
    return None


def release_gpu():
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    time.sleep(2)


def evaluate_vllm(model_id, mmlu_samples, arc_samples, quantization=None):
    """Load model once via vLLM, evaluate both benchmarks, return (mmlu_acc, arc_acc)."""
    from vllm import LLM, SamplingParams

    kwargs = {
        "model": model_id,
        "tensor_parallel_size": 1,
        "gpu_memory_utilization": 0.85,
        "max_model_len": 2048,
        "trust_remote_code": True,
        "enforce_eager": True,
    }
    if quantization:
        kwargs["quantization"] = quantization
    else:
        kwargs["dtype"] = "float16"

    log.info(f"Loading {model_id} (quant={quantization}) ...")
    t0 = time.time()
    llm = LLM(**kwargs)
    log.info(f"  Loaded in {time.time()-t0:.1f}s")

    tokenizer = llm.get_tokenizer()
    sp = SamplingParams(temperature=0.0, max_tokens=32)

    results = {}
    for bench_name, samples in [("mmlu", mmlu_samples), ("arc", arc_samples)]:
        prompts = []
        for s in samples:
            labels = s.get("labels")
            user_msg = format_mcq(s["question"], s["choices"], labels)
            messages = [{"role": "user", "content": user_msg}]
            try:
                p = tokenizer.apply_chat_template(
                    messages, tokenize=False, add_generation_prompt=True
                )
            except Exception:
                p = user_msg
            prompts.append(p)

        log.info(f"  {bench_name}: generating {len(prompts)} responses ...")
        outputs = llm.generate(prompts, sp)

        correct = 0
        for i, out in enumerate(outputs):
            pred = extract_answer(out.outputs[0].text)
            labels = samples[i].get("labels", [chr(65+j) for j in range(len(samples[i]["choices"]))])
            expected = labels[samples[i]["answer"]].upper()
            if pred == expected:
                correct += 1
        acc = correct / len(samples)
        results[bench_name] = acc
        log.info(f"  {bench_name}: {acc:.4f} ({correct}/{len(samples)})")

    del llm
    release_gpu()
    return results["mmlu"], results["arc"]


def save_output(results_list, summary=None):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = {
        "purpose": "R1-W2: AWQ INT4 vs FP16 accuracy comparison",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "n_samples": {"mmlu": N_SAMPLES, "arc": N_SAMPLES},
        "seed": SEED,
        "gpu": "1x NVIDIA RTX PRO 6000 Blackwell (98GB)",
        "results": results_list,
    }
    if summary:
        out["summary"] = summary
    path = OUTPUT_DIR / "fp16_baseline.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    return path


def main():
    set_seed(SEED)
    log.info(f"GPU: {torch.cuda.get_device_name(0)} ({torch.cuda.get_device_properties(0).total_mem // 1024**3}GB)")

    mmlu = load_mmlu_samples(N_SAMPLES)
    arc = load_arc_samples(N_SAMPLES)
    log.info(f"Samples loaded: MMLU={len(mmlu)}, ARC={len(arc)}")

    results_list = []

    for cfg in MODELS:
        name = cfg["name"]
        log.info(f"\n{'='*60}\n  {name} ({cfg['params_b']}B)\n{'='*60}")

        entry = {
            "model": name,
            "awq_model_id": cfg["awq_id"],
            "fp16_model_id": cfg["fp16_id"],
            "params_b": cfg["params_b"],
            "mmlu": {},
            "arc": {},
        }

        # ── AWQ ──
        try:
            awq_mmlu, awq_arc = evaluate_vllm(
                cfg["awq_id"], mmlu, arc, quantization="awq"
            )
            entry["mmlu"]["awq_acc"] = round(awq_mmlu, 4)
            entry["arc"]["awq_acc"] = round(awq_arc, 4)
        except Exception as e:
            log.error(f"AWQ failed for {name}: {e}")
            entry["mmlu"]["awq_acc"] = None
            entry["arc"]["awq_acc"] = None
            entry["awq_error"] = str(e)
            results_list.append(entry)
            save_output(results_list)
            continue

        # ── FP16 ──
        if cfg["can_fp16"]:
            try:
                fp16_mmlu, fp16_arc = evaluate_vllm(
                    cfg["fp16_id"], mmlu, arc, quantization=None
                )
                entry["mmlu"]["fp16_acc"] = round(fp16_mmlu, 4)
                entry["arc"]["fp16_acc"] = round(fp16_arc, 4)
                entry["mmlu"]["delta_pp"] = round((fp16_mmlu - awq_mmlu) * 100, 2)
                entry["arc"]["delta_pp"] = round((fp16_arc - awq_arc) * 100, 2)
                entry["gpu_config"] = "1x cuda:0"
            except Exception as e:
                log.error(f"FP16 failed for {name}: {e}")
                entry["mmlu"]["fp16_acc"] = None
                entry["arc"]["fp16_acc"] = None
                entry["fp16_error"] = str(e)
                entry["gpu_config"] = "1x cuda:0"
        else:
            entry["mmlu"]["fp16_acc"] = "skipped"
            entry["mmlu"]["delta_pp"] = "skipped"
            entry["arc"]["fp16_acc"] = "skipped"
            entry["arc"]["delta_pp"] = "skipped"
            entry["skip_reason"] = cfg.get("skip_reason", "FP16 exceeds GPU memory")
            entry["gpu_config"] = "1x cuda:0 (AWQ only)"

        results_list.append(entry)
        save_output(results_list)
        log.info(f"[checkpoint] {len(results_list)}/{len(MODELS)} models done")

    # ── Summary ──
    deltas = []
    for r in results_list:
        for bench in ("mmlu", "arc"):
            d = r[bench].get("delta_pp")
            if isinstance(d, (int, float)):
                deltas.append(abs(d))

    summary = {
        "n_compared": len([r for r in results_list
                          if isinstance(r["mmlu"].get("delta_pp"), (int, float))]),
        "n_skipped_fp16": sum(1 for c in MODELS if not c["can_fp16"]),
    }
    if deltas:
        summary["mean_delta_pp"] = round(sum(deltas) / len(deltas), 2)
        summary["max_delta_pp"] = round(max(deltas), 2)
        summary["conclusion"] = (
            f"AWQ degradation {'<2pp' if max(deltas) < 2 else '>2pp'} "
            f"(mean {sum(deltas)/len(deltas):.1f}pp, max {max(deltas):.1f}pp)"
        )

    path = save_output(results_list, summary)
    log.info(f"\nDone. Results: {path}")
    log.info(f"Summary: {json.dumps(summary, indent=2)}")


if __name__ == "__main__":
    main()
