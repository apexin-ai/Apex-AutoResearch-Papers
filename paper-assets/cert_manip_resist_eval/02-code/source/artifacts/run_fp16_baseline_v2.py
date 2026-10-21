#!/usr/bin/env python3
"""R1-W2 FP16 Baseline v2: AWQ INT4 vs FP16 accuracy on MMLU / ARC-Challenge.

Key fixes over v1:
- N_SAMPLES=300 (was 100)
- max_new_tokens=1 (was 5)
- Unified tokenizer: always use FP16 model's tokenizer for both AWQ and FP16
- Explicit torch_dtype=torch.float16 for FP16 models
"""

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
        logging.FileHandler("/tmp/fp16_baseline_v2.log"),
    ],
)
log = logging.getLogger("fp16_baseline_v2")

SEED = 42
N_SAMPLES = 300

MODELS = [
    {
        "name": "Qwen2.5-14B-Instruct",
        "awq_hf": "Qwen/Qwen2.5-14B-Instruct-AWQ",
        "fp16_hf": "Qwen/Qwen2.5-14B-Instruct",
        "params_b": 14,
    },
    {
        "name": "Qwen2.5-32B-Instruct",
        "awq_hf": "Qwen/Qwen2.5-32B-Instruct-AWQ",
        "fp16_hf": "Qwen/Qwen2.5-32B-Instruct",
        "params_b": 32,
    },
    {
        "name": "Llama-3.1-8B-Instruct",
        "awq_hf": "hugging-quants/Meta-Llama-3.1-8B-Instruct-AWQ-INT4",
        "awq_alt": ["LLM-Research/Meta-Llama-3.1-8B-Instruct-AWQ-INT4"],
        "fp16_hf": "meta-llama/Llama-3.1-8B-Instruct",
        "fp16_alt": ["LLM-Research/Meta-Llama-3.1-8B-Instruct",
                      "LLM-Research/Meta-Llama-3___1-8B-Instruct"],
        "params_b": 8,
    },
]

OUTPUT_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001")
CKPT_PATH = OUTPUT_DIR / "fp16_baseline_v2_checkpoint.json"
DATA_PATH = OUTPUT_DIR / "fp16_eval_data_v2.json"


def set_seed(seed):
    random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def find_local_path(model_id, alt_ids=None):
    """Find model in local cache (HF or ModelScope) without downloading.
    alt_ids: additional model IDs to search (e.g. ModelScope org differs from HF)."""
    import glob

    candidates = [model_id] + (alt_ids or [])
    for mid in candidates:
        # HF cache
        hf_name = mid.replace("/", "--")
        hf_snaps = glob.glob(f"/root/autodl-tmp/.hf_cache/hub/models--{hf_name}/snapshots/*")
        for snap in hf_snaps:
            safetensors = glob.glob(os.path.join(snap, "*.safetensors"))
            if safetensors:
                log.info(f"Found {model_id} in HF cache: {snap}")
                return snap

        # ModelScope cache (dots may become underscores)
        ms_base = "/root/autodl-tmp/modelscope_cache"
        parts = mid.split("/")
        if len(parts) == 2:
            for variant in [parts[1], parts[1].replace(".", "___")]:
                candidate = os.path.join(ms_base, parts[0], variant)
                if os.path.isdir(candidate):
                    safetensors = glob.glob(os.path.join(candidate, "*.safetensors"))
                    if safetensors:
                        log.info(f"Found {model_id} in ModelScope cache: {candidate}")
                        return candidate

    return None


def prepare_data():
    if DATA_PATH.exists():
        with open(DATA_PATH) as f:
            data = json.load(f)
        if len(data.get("mmlu", [])) >= N_SAMPLES and len(data.get("arc", [])) >= N_SAMPLES:
            log.info(f"Using cached eval data: {len(data['mmlu'])} MMLU, {len(data['arc'])} ARC")
            return data["mmlu"][:N_SAMPLES], data["arc"][:N_SAMPLES]

    log.info(f"Preparing eval data: {N_SAMPLES} samples per benchmark...")
    from datasets import load_dataset

    mmlu = load_dataset("cais/mmlu", "all", split="test")
    arc = load_dataset("allenai/ai2_arc", "ARC-Challenge", split="test")

    set_seed(SEED)
    mmlu_indices = random.sample(range(len(mmlu)), min(N_SAMPLES, len(mmlu)))
    arc_indices = random.sample(range(len(arc)), min(N_SAMPLES, len(arc)))

    mmlu_samples = []
    for i in mmlu_indices:
        s = mmlu[i]
        mmlu_samples.append({
            "question": s["question"],
            "choices": s["choices"],
            "answer": s["answer"],
        })

    arc_samples = []
    for i in arc_indices:
        s = arc[i]
        label_map = {l: idx for idx, l in enumerate(s["choices"]["label"])}
        arc_samples.append({
            "question": s["question"],
            "choices": s["choices"]["text"],
            "answer": label_map.get(s["answerKey"], 0),
            "labels": s["choices"]["label"],
        })

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(DATA_PATH, "w") as f:
        json.dump({"mmlu": mmlu_samples, "arc": arc_samples}, f)
    log.info(f"Saved {len(mmlu_samples)} MMLU + {len(arc_samples)} ARC samples to {DATA_PATH}")
    return mmlu_samples, arc_samples


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
    time.sleep(3)


def evaluate_model(model, tokenizer, samples, dataset_name, model_name=""):
    correct = 0
    total = 0
    for i, s in enumerate(samples):
        prompt = format_mcq(s["question"], s["choices"], s.get("labels"))
        messages = [{"role": "user", "content": prompt}]
        text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(text, return_tensors="pt").to(model.device)
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=1,
                do_sample=False,
                pad_token_id=tokenizer.eos_token_id,
            )
        response = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        pred = extract_answer(response)
        gold = chr(65 + s["answer"])
        if pred == gold:
            correct += 1
        total += 1
        if i < 3:
            log.info(f"  [{model_name}] {dataset_name} #{i}: resp={response!r} pred={pred} gold={gold} {'OK' if pred==gold else 'WRONG'}")
        if (i + 1) % 50 == 0:
            log.info(f"  [{model_name}] {dataset_name}: {i+1}/{len(samples)}, acc={correct/total:.3f}")
    return correct / total if total > 0 else 0.0


def run_model_eval(model_path, tokenizer, mmlu_samples, arc_samples, model_name="", is_awq=False):
    from transformers import AutoModelForCausalLM
    log.info(f"Loading {'AWQ' if is_awq else 'FP16'} model from {model_path}...")
    t0 = time.time()

    load_kwargs = {"device_map": "auto", "trust_remote_code": True}
    if not is_awq:
        load_kwargs["torch_dtype"] = torch.float16

    model = AutoModelForCausalLM.from_pretrained(model_path, **load_kwargs)
    model.eval()
    log.info(f"Loaded in {time.time()-t0:.1f}s, GPU mem: {torch.cuda.memory_allocated()/1e9:.1f}GB")

    mmlu_acc = evaluate_model(model, tokenizer, mmlu_samples, "MMLU", model_name)
    arc_acc = evaluate_model(model, tokenizer, arc_samples, "ARC", model_name)
    log.info(f"[{model_name}] results: MMLU={mmlu_acc:.4f}, ARC={arc_acc:.4f}")

    del model
    release_gpu()
    return mmlu_acc, arc_acc


def load_checkpoint():
    if CKPT_PATH.exists():
        with open(CKPT_PATH) as f:
            return json.load(f)
    return {"results": []}


def save_checkpoint(ckpt):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(CKPT_PATH, "w") as f:
        json.dump(ckpt, f, indent=2)


def save_output(results, summary=None):
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out = {
        "experiment": "R1-W2 FP16 Baseline v2",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "seed": SEED,
        "n_samples": N_SAMPLES,
        "fixes_applied": [
            "unified_tokenizer_from_fp16",
            "max_new_tokens=1",
            "torch_dtype=float16_for_fp16",
            "n_samples=300",
        ],
        "gpu": f"1x {torch.cuda.get_device_name(0)} ({torch.cuda.get_device_properties(0).total_mem // 1024**3}GB)" if torch.cuda.is_available() else "N/A",
        "results": results,
    }
    if summary:
        out["summary"] = summary
    path = OUTPUT_DIR / "fp16_baseline_v2.json"
    with open(path, "w") as f:
        json.dump(out, f, indent=2)
    return path


def main():
    set_seed(SEED)
    log.info("=== FP16 Baseline v2 ===")
    log.info(f"N_SAMPLES={N_SAMPLES}, SEED={SEED}")

    mmlu, arc = prepare_data()
    log.info(f"Eval data: {len(mmlu)} MMLU, {len(arc)} ARC")

    ckpt = load_checkpoint()
    done_models = {r["model"] for r in ckpt.get("results", [])}
    final_results = list(ckpt.get("results", []))

    from transformers import AutoTokenizer

    for cfg in MODELS:
        name = cfg["name"]
        if name in done_models:
            log.info(f"Skipping {name} (in checkpoint)")
            continue

        log.info(f"\n{'='*60}\n  {name} ({cfg['params_b']}B)\n{'='*60}")

        entry = {
            "model": name,
            "awq_model_id": cfg["awq_hf"],
            "fp16_model_id": cfg["fp16_hf"],
            "params_b": cfg["params_b"],
            "mmlu": {},
            "arc": {},
        }

        # Find local paths
        fp16_path = find_local_path(cfg["fp16_hf"], cfg.get("fp16_alt"))
        awq_path = find_local_path(cfg["awq_hf"], cfg.get("awq_alt"))

        if not fp16_path:
            log.error(f"FP16 model not found locally: {cfg['fp16_hf']}")
            entry["error"] = f"fp16_model_not_found: {cfg['fp16_hf']}"
            final_results.append(entry)
            save_checkpoint({"results": final_results})
            save_output(final_results)
            continue

        if not awq_path:
            log.error(f"AWQ model not found locally: {cfg['awq_hf']}")
            entry["error"] = f"awq_model_not_found: {cfg['awq_hf']}"
            final_results.append(entry)
            save_checkpoint({"results": final_results})
            save_output(final_results)
            continue

        # Load tokenizer from FP16 model (ensures template consistency)
        log.info(f"Loading tokenizer from FP16 model: {fp16_path}")
        tokenizer = AutoTokenizer.from_pretrained(fp16_path, trust_remote_code=True)

        # AWQ evaluation
        try:
            awq_mmlu, awq_arc = run_model_eval(
                awq_path, tokenizer, mmlu, arc, model_name=f"{name}-AWQ", is_awq=True
            )
            entry["mmlu"]["awq_acc"] = round(awq_mmlu, 4)
            entry["arc"]["awq_acc"] = round(awq_arc, 4)
        except Exception as e:
            log.error(f"AWQ failed for {name}: {e}", exc_info=True)
            entry["mmlu"]["awq_acc"] = None
            entry["arc"]["awq_acc"] = None
            entry["awq_error"] = str(e)
            final_results.append(entry)
            save_checkpoint({"results": final_results})
            save_output(final_results)
            release_gpu()
            continue

        # FP16 evaluation
        try:
            fp16_mmlu, fp16_arc = run_model_eval(
                fp16_path, tokenizer, mmlu, arc, model_name=f"{name}-FP16", is_awq=False
            )
            entry["mmlu"]["fp16_acc"] = round(fp16_mmlu, 4)
            entry["arc"]["fp16_acc"] = round(fp16_arc, 4)
            entry["mmlu"]["delta_pp"] = round((awq_mmlu - fp16_mmlu) * 100, 2)
            entry["arc"]["delta_pp"] = round((awq_arc - fp16_arc) * 100, 2)
            entry["gpu_config"] = "1x cuda:0"
        except Exception as e:
            log.error(f"FP16 failed for {name}: {e}", exc_info=True)
            entry["mmlu"]["fp16_acc"] = None
            entry["arc"]["fp16_acc"] = None
            entry["fp16_error"] = str(e)
            entry["gpu_config"] = "1x cuda:0"

        final_results.append(entry)
        save_checkpoint({"results": final_results})
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
        "models_evaluated": [m["name"] for m in MODELS],
    }
    if deltas:
        summary["mean_abs_delta_pp"] = round(sum(deltas) / len(deltas), 2)
        summary["max_abs_delta_pp"] = round(max(deltas), 2)
        summary["all_within_2pp"] = max(deltas) < 2.0
        summary["conclusion"] = (
            f"AWQ degradation {'<2pp' if max(deltas) < 2 else '>2pp'} "
            f"(mean |delta|={sum(deltas)/len(deltas):.1f}pp, max |delta|={max(deltas):.1f}pp)"
        )

    path = save_output(final_results, summary)
    log.info(f"\nDone. Results: {path}")
    log.info(f"Summary: {json.dumps(summary, indent=2)}")


if __name__ == "__main__":
    main()
