"""MVP evaluation script: run CompressLink configs and report EM/F1 metrics."""

import argparse
import json
import re
import string
import time
from collections import Counter
from pathlib import Path
from typing import List, Dict

import torch
import yaml
from transformers import AutoModelForCausalLM, AutoTokenizer

from .nope_attention import patch_model_for_nope
from .pipeline import CompressLinkPipeline


def normalize_answer(s: str) -> str:
    s = s.lower()
    s = re.sub(r"\b(a|an|the)\b", " ", s)
    s = s.translate(str.maketrans("", "", string.punctuation))
    s = " ".join(s.split())
    return s.strip()


def compute_em(prediction: str, ground_truths: List[str]) -> float:
    pred_norm = normalize_answer(prediction)
    return float(any(normalize_answer(gt) == pred_norm for gt in ground_truths))


def compute_f1(prediction: str, ground_truths: List[str]) -> float:
    pred_tokens = normalize_answer(prediction).split()
    if not pred_tokens:
        return 0.0

    best_f1 = 0.0
    for gt in ground_truths:
        gt_tokens = normalize_answer(gt).split()
        if not gt_tokens:
            continue
        common = Counter(pred_tokens) & Counter(gt_tokens)
        num_same = sum(common.values())
        if num_same == 0:
            continue
        precision = num_same / len(pred_tokens)
        recall = num_same / len(gt_tokens)
        f1 = 2 * precision * recall / (precision + recall)
        best_f1 = max(best_f1, f1)

    return best_f1


def load_dataset_samples(config: dict, num_samples: int) -> List[Dict]:
    """Load evaluation samples with context + question + answers.

    Prefers pre-processed JSONL (from prepare_nq_data.py) over raw HF dataset
    since NQ requires HTML parsing for context extraction.
    """
    jsonl_path = config.get("jsonl_path")
    if jsonl_path and Path(jsonl_path).exists():
        samples = []
        with open(jsonl_path) as f:
            for line in f:
                if len(samples) >= num_samples:
                    break
                item = json.loads(line)
                samples.append({
                    "context": item["context"],
                    "question": item["question"],
                    "answers": item["answers"],
                })
        return samples

    from datasets import load_dataset

    dataset_name = config.get("name", "google-research-datasets/natural_questions")
    split = config.get("split", "validation")

    ds = load_dataset(dataset_name, split=f"{split}[:{num_samples}]", streaming=False)

    samples = []
    for item in ds:
        question = item.get("question", "")
        if isinstance(question, dict):
            question = question.get("text", "")

        context = item.get("context", item.get("passage", ""))

        if "answers" in item:
            ans = item["answers"]
            if isinstance(ans, dict):
                answers = ans.get("text", [])
            elif isinstance(ans, list):
                answers = ans
            else:
                answers = [str(ans)]
        elif "answer" in item:
            ans = item["answer"]
            answers = ans if isinstance(ans, list) else [ans]
        else:
            answers = []

        if context and question:
            samples.append(
                {"context": context, "question": question, "answers": answers}
            )

    return samples


def run_evaluation(config_path: str, gpu: str = "cuda:0") -> Dict:
    with open(config_path) as f:
        config = yaml.safe_load(f)

    device = torch.device(gpu)

    # Load model
    model_name = config["model"]["name"]
    dtype = getattr(torch, config["model"].get("dtype", "float16"))

    print(f"Loading model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=dtype,
        attn_implementation="eager",
        device_map=gpu,
    )
    model.eval()

    patch_model_for_nope(model)

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # Load dataset
    num_samples = config["dataset"].get("num_samples", 500)
    samples = load_dataset_samples(config["dataset"], num_samples)
    print(f"Loaded {len(samples)} samples")

    # Pipeline config
    head_dim = model.config.hidden_size // model.config.num_attention_heads
    pipeline_config = {
        "chunk_size": config["chunking"]["chunk_size"],
        "block_size": config["chunking"]["block_size"],
        "total_budget": config["budget"]["total_recomputation"],
        "beta": config["cegr"]["beta"],
        "head_dim": head_dim,
        "max_bits": config["compression"]["max_bits"],
        "max_new_tokens": config["evaluation"].get("max_new_tokens", 32),
    }

    pipeline = CompressLinkPipeline(model, tokenizer, pipeline_config)

    # Run evaluation
    eval_configs = config["evaluation"]["configs"]
    ratios = config["compression"]["ratios"]

    results = {}

    for cfg_name in eval_configs:
        run_ratios = [0] if cfg_name == "E" else ratios

        for ratio in run_ratios:
            run_key = f"{cfg_name}_{'baseline' if ratio == 0 else f'{ratio}x'}"
            print(f"\nRunning config: {run_key}")

            ems, f1s, latencies = [], [], []

            for idx, sample in enumerate(samples):
                sys_content = "Answer the question based on the given context. Provide ONLY the answer as a short phrase."
                user_content = f"Context: {sample['context']}\n\nQuestion: {sample['question']}"
                messages = [
                    {"role": "system", "content": sys_content},
                    {"role": "user", "content": user_content},
                ]
                full_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
                split_marker = f"Question: {sample['question']}"
                split_idx = full_text.index(split_marker)
                ctx_text = full_text[:split_idx]
                q_text = full_text[split_idx:]
                ctx_enc = tokenizer(ctx_text, return_tensors="pt", truncation=True, max_length=4096, add_special_tokens=False)
                q_enc = tokenizer(q_text, return_tensors="pt", add_special_tokens=False)

                t0 = time.time()
                try:
                    result = pipeline.run_single(
                        context_ids=ctx_enc.input_ids,
                        query_ids=q_enc.input_ids,
                        config_name=cfg_name,
                        compression_ratio=max(ratio, 1),
                    )
                    pred = result["generated_text"].split("\n")[0].strip()
                except Exception as e:
                    print(f"  Sample {idx} error: {e}")
                    pred = ""
                latency = time.time() - t0

                em = compute_em(pred, sample["answers"])
                f1 = compute_f1(pred, sample["answers"])

                ems.append(em)
                f1s.append(f1)
                latencies.append(latency)

                if idx < 5:
                    print(f"  [{idx}] pred={repr(pred[:80])} gold={sample['answers']} em={em:.1f} f1={f1:.3f}")

                if (idx + 1) % 50 == 0:
                    print(
                        f"  {idx+1}/{len(samples)}: "
                        f"EM={sum(ems)/len(ems):.3f}, F1={sum(f1s)/len(f1s):.3f}"
                    )

            results[run_key] = {
                "config": cfg_name,
                "compression_ratio": ratio,
                "em": sum(ems) / len(ems),
                "f1": sum(f1s) / len(f1s),
                "avg_latency": sum(latencies) / len(latencies),
                "num_samples": len(samples),
            }
            print(
                f"  Final: EM={results[run_key]['em']:.3f}, "
                f"F1={results[run_key]['f1']:.3f}"
            )

    # Save results
    output_dir = Path(config["output"]["results_dir"])
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "mvp_results.json"

    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to {output_path}")
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CompressLink MVP Evaluation")
    parser.add_argument("--config", type=str, default="configs/mvp_config.yaml")
    parser.add_argument("--gpu", type=str, default="cuda:0")
    args = parser.parse_args()

    run_evaluation(args.config, args.gpu)
