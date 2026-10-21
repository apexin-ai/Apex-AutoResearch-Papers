#!/usr/bin/env python3
"""R1-W2 FP16 Baseline: AWQ INT4 vs FP16 accuracy on MMLU / ARC-Challenge.
Downloads models via ModelScope (domestic CDN), loads locally, evaluates.
Runs on single 98GB RTX PRO 6000 Blackwell."""

import gc
import json
import logging
import os
import random
import re
import time
from datetime import datetime, timezone
from pathlib import Path

os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"
os.environ["MODELSCOPE_CACHE"] = "/root/autodl-tmp/modelscope_cache"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["HF_HUB_DISABLE_XET"] = "1"

import torch

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
DATA_PATH = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/fp16_eval_data.json")
MODELSCOPE_CACHE = "/root/autodl-tmp/modelscope_cache"

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
        "name": "Qwen2.5-72B-Instruct",
        "awq_id": "Qwen/Qwen2.5-72B-Instruct-AWQ",
        "fp16_id": "Qwen/Qwen2.5-72B-Instruct",
        "can_fp16": False,
        "params_b": 72,
        "skip_reason": "FP16 requires ~144GB VRAM, exceeds single 98GB GPU",
    },
]

OUTPUT_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
CKPT_PATH = OUTPUT_DIR / "fp16_baseline_checkpoint.json"


def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def download_model(model_id):
    """Download model via ModelScope, return local path."""
    from modelscope import snapshot_download
    log.info(f"Downloading {model_id} via ModelScope...")
    t0 = time.time()
    local_dir = snapshot_download(model_id, cache_dir=MODELSCOPE_CACHE)
    log.info(f"Downloaded {model_id} in {time.time()-t0:.1f}s -> {local_dir}")
    return local_dir


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
    time.sleep(5)


def load_and_eval(model_path, mmlu_samples, arc_samples, model_name=""):
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading from {model_path}...")
    t0 = time.time()

    tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
    model = AutoModelForCausalLM.from_pretrained(
        model_path, device_map="auto", trust_remote_code=True,
    )
    model.eval()
    load_time = time.time() - t0
    log.info(f"Loaded in {load_time:.1f}s, GPU mem: {torch.cuda.memory_allocated()/1e9:.1f}GB")

    def evaluate(samples, dataset_name):
        correct = 0
        total = 0
        for i, s in enumerate(samples):
            prompt = format_mcq(s["question"], s["choices"])
            messages = [{"role": "user", "content": prompt}]
            text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            inputs = tokenizer(text, return_tensors="pt").to(model.device)
            with torch.no_grad():
                outputs = model.generate(
                    **inputs, max_new_tokens=5, do_sample=False,
                    pad_token_id=tokenizer.eos_token_id,
                )
            response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
            pred = extract_answer(response)
            gold = s["answer"]
            if pred == gold:
                correct += 1
            total += 1
            if (i + 1) % 25 == 0:
                log.info(f"  [{model_name}] {dataset_name}: {i+1}/{len(samples)} done, acc={correct/total:.3f}")
        return correct / total if total > 0 else 0.0

    mmlu_acc = evaluate(mmlu_samples, "MMLU")
    arc_acc = evaluate(arc_samples, "ARC")
    log.info(f"Results for {model_name}: MMLU={mmlu_acc:.4f}, ARC={arc_acc:.4f}")

    del model
    del tokenizer
    release_gpu()

    return mmlu_acc, arc_acc


def load_checkpoint():
    if CKPT_PATH.exists():
        with open(CKPT_PATH) as f:
            return json.load(f)
    return {"results": []}


def save_checkpoint(ckpt):
    CKPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(CKPT_PATH, "w") as f:
        json.dump(ckpt, f, indent=2)


def save_output(results, summary=None):
    path = OUTPUT_DIR / "fp16_baseline.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    out = {
        "experiment": "R1-W2 FP16 Baseline",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "n_samples": N_SAMPLES,
        "gpu": "1x NVIDIA RTX PRO 6000 Blackwell (98GB)",
        "results": results,
    }
    if summary:
        out["summary"] = summary
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    return path


def main():
    set_seed(SEED)
    log.info(f"GPU: {torch.cuda.get_device_name(0)} ({torch.cuda.get_device_properties(0).total_memory // 1024**3}GB)")
    log.info(f"torch: {torch.__version__}")

    with open(DATA_PATH) as f:
        data = json.load(f)
    mmlu = data["mmlu"]
    arc = data["arc"]
    log.info(f"Pre-loaded data: MMLU={len(mmlu)}, ARC={len(arc)}")

    ckpt = load_checkpoint()
    done_models = {r["model"] for r in ckpt.get("results", [])}
    final_results = list(ckpt.get("results", []))

    for cfg in MODELS:
        name = cfg["name"]

        if name in done_models:
            log.info(f"Skipping {name} (already in checkpoint)")
            continue

        log.info(f"\n{'='*60}\n  {name} ({cfg['params_b']}B)\n{'='*60}")

        entry = {
            "model": name,
            "awq_model_id": cfg["awq_id"],
            "fp16_model_id": cfg["fp16_id"],
            "params_b": cfg["params_b"],
            "mmlu": {},
            "arc": {},
        }

        # Download and eval AWQ
        try:
            awq_path = download_model(cfg["awq_id"])
            awq_mmlu, awq_arc = load_and_eval(awq_path, mmlu, arc, model_name=f"{name}-AWQ")
            entry["mmlu"]["awq_acc"] = round(awq_mmlu, 4)
            entry["arc"]["awq_acc"] = round(awq_arc, 4)
        except Exception as e:
            log.error(f"AWQ failed for {name}: {e}", exc_info=True)
            entry["mmlu"]["awq_acc"] = None
            entry["arc"]["awq_acc"] = None
            entry["awq_error"] = str(e)
            final_results.append(entry)
            ckpt["results"] = final_results
            save_checkpoint(ckpt)
            save_output(final_results)
            release_gpu()
            continue

        # Download and eval FP16
        if cfg["can_fp16"]:
            try:
                fp16_path = download_model(cfg["fp16_id"])
                fp16_mmlu, fp16_arc = load_and_eval(fp16_path, mmlu, arc, model_name=f"{name}-FP16")
                entry["mmlu"]["fp16_acc"] = round(fp16_mmlu, 4)
                entry["arc"]["fp16_acc"] = round(fp16_arc, 4)
                entry["mmlu"]["delta_pp"] = round((fp16_mmlu - awq_mmlu) * 100, 2)
                entry["arc"]["delta_pp"] = round((fp16_arc - awq_arc) * 100, 2)
                entry["gpu_config"] = "1x cuda:0"
            except Exception as e:
                log.error(f"FP16 failed for {name}: {e}", exc_info=True)
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

        final_results.append(entry)
        ckpt["results"] = final_results
        save_checkpoint(ckpt)
        save_output(final_results)
        log.info(f"[checkpoint] {len(final_results)}/{len(MODELS)} models done")

    # Summary
    deltas = []
    for r in final_results:
        for bench in ("mmlu", "arc"):
            d = r[bench].get("delta_pp")
            if isinstance(d, (int, float)):
                deltas.append(abs(d))

    summary = {
        "n_compared": len([r for r in final_results
                          if isinstance(r["mmlu"].get("delta_pp"), (int, float))]),
        "n_skipped_fp16": sum(1 for c in MODELS if not c["can_fp16"]),
        "models_evaluated": [m["name"] for m in MODELS],
    }
    if deltas:
        summary["mean_delta_pp"] = round(sum(deltas) / len(deltas), 2)
        summary["max_delta_pp"] = round(max(deltas), 2)
        summary["conclusion"] = (
            f"AWQ degradation {'<2pp' if max(deltas) < 2 else '>2pp'} "
            f"(mean {sum(deltas)/len(deltas):.1f}pp, max {max(deltas):.1f}pp)"
        )

    path = save_output(final_results, summary)
    log.info(f"\nDone. Results: {path}")
    log.info(f"Summary: {json.dumps(summary, indent=2)}")


if __name__ == "__main__":
    main()
