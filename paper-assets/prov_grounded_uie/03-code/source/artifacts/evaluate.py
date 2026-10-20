"""Evaluation script for ProvUIE.

Generates predictions from a trained model and computes:
  - RE F1:  relation extraction F1 (exact triple match)
  - Evi F1: evidence sentence F1 (DocRED standard)
  - Attribution Precision: fraction of extractions backed by evidence

Input:  Model checkpoint + evaluation JSONL.
Output: Formatted report + JSON results file.

Changes:
  - Batch generation via left-padded tokenization (--batch_size, default 8)

Usage:
    python evaluate.py --model_path ./outputs/grpo/final --eval_file ./data/docred_dev.jsonl
"""

import os
os.environ.setdefault("PYTHONUNBUFFERED", "1")

import json
from pathlib import Path

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, HfArgumentParser

from config import ModelArgs, EvalArgs
from data_utils import load_grpo_dataset
from rewards import parse_json_output


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------

def compute_re_f1(pred_rels: list[dict], gold_rels: list[dict]) -> tuple[float, float, float]:
    """Relation extraction F1 (exact triple match on head+tail+relation)."""
    pred_set = {
        (r.get("head", "").lower(), r.get("tail", "").lower(), r.get("relation", "").lower())
        for r in pred_rels
    }
    gold_set = {
        (r["head"].lower(), r["tail"].lower(), r["relation"].lower())
        for r in gold_rels
    }
    if not pred_set and not gold_set:
        return 1.0, 1.0, 1.0

    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0.0
    rec = tp / len(gold_set) if gold_set else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    return prec, rec, f1


def compute_evi_f1(
    pred_rels: list[dict], gold_rels: list[dict], sentences: list[str]
) -> tuple[float, float, float]:
    """Evidence sentence F1 (per-relation, sentence-level).

    Matches predicted evidence text back to sentence indices for comparison
    with gold evidence_sids.
    """
    sent_to_idx: dict[str, int] = {}
    for i, s in enumerate(sentences):
        sent_to_idx[s.strip().lower()] = i

    all_pred: set[tuple] = set()
    all_gold: set[tuple] = set()

    gold_map: dict[tuple, set[int]] = {}
    for r in gold_rels:
        key = (r["head"].lower(), r["tail"].lower(), r["relation"].lower())
        sids = set(r.get("evidence_sids", []))
        if not sids:
            for ev in r.get("evidence", []):
                idx = sent_to_idx.get(ev.strip().lower())
                if idx is not None:
                    sids.add(idx)
        gold_map[key] = sids
        for sid in sids:
            all_gold.add((key, sid))

    for r in pred_rels:
        key = (
            r.get("head", "").lower(),
            r.get("tail", "").lower(),
            r.get("relation", "").lower(),
        )
        for ev in r.get("evidence", []):
            if isinstance(ev, str):
                idx = sent_to_idx.get(ev.strip().lower())
                if idx is not None:
                    all_pred.add((key, idx))

    if not all_pred and not all_gold:
        return 1.0, 1.0, 1.0

    tp = len(all_pred & all_gold)
    prec = tp / len(all_pred) if all_pred else 0.0
    rec = tp / len(all_gold) if all_gold else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    return prec, rec, f1


def compute_attribution_precision(pred_rels: list[dict]) -> float:
    """Fraction of predicted relations that include non-empty evidence."""
    if not pred_rels:
        return 0.0
    with_ev = sum(1 for r in pred_rels if r.get("evidence") and len(r["evidence"]) > 0)
    return with_ev / len(pred_rels)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = HfArgumentParser((ModelArgs, EvalArgs))
    model_args, eval_args = parser.parse_args_into_dataclasses()

    # ── Load model ─────────────────────────────────────────────────────
    tokenizer = AutoTokenizer.from_pretrained(eval_args.model_path, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    # Left-padding: causal LMs need prompts right-aligned so generated tokens
    # are contiguous at the end of each sequence in the batch.
    tokenizer.padding_side = "left"

    model_kwargs: dict = {"trust_remote_code": True, "torch_dtype": "auto"}
    if model_args.use_flash_attention:
        model_kwargs["attn_implementation"] = "flash_attention_2"

    # Handle both full models and PEFT adapters
    adapter_config_path = Path(eval_args.model_path) / "adapter_config.json"
    if adapter_config_path.exists():
        from peft import PeftModel

        with open(adapter_config_path) as f:
            acfg = json.load(f)
        base_name = acfg.get("base_model_name_or_path", model_args.model_name_or_path)
        model = AutoModelForCausalLM.from_pretrained(base_name, **model_kwargs)
        model = PeftModel.from_pretrained(model, eval_args.model_path)
        model = model.merge_and_unload()
    else:
        model = AutoModelForCausalLM.from_pretrained(eval_args.model_path, **model_kwargs)

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device).eval()

    # ── Load data ──────────────────────────────────────────────────────
    dataset = load_grpo_dataset(eval_args.eval_file)

    # ── Prepare prompts ───────────────────────────────────────────────
    all_prompts: list[str] = []
    all_gold_rels: list[list[dict]] = []
    all_sentences: list[list[str]] = []
    for i in range(len(dataset)):
        all_gold_rels.append(json.loads(dataset[i]["gold_relations"]))
        all_sentences.append(json.loads(dataset[i]["sentences"]))
        all_prompts.append(
            tokenizer.apply_chat_template(
                dataset[i]["prompt"], tokenize=False, add_generation_prompt=True
            )
        )

    # ── Batch generate & evaluate ─────────────────────────────────────
    all_re_f1: list[float] = []
    all_evi_f1: list[float] = []
    all_attr: list[float] = []
    predictions: list[dict] = []
    batch_size = eval_args.batch_size
    next_log = 50

    for batch_start in range(0, len(all_prompts), batch_size):
        batch_prompts = all_prompts[batch_start : batch_start + batch_size]

        inputs = tokenizer(
            batch_prompts, return_tensors="pt", padding=True,
            truncation=True, max_length=eval_args.max_prompt_length,
        ).to(device)

        with torch.no_grad():
            gen_kwargs = {
                "max_new_tokens": eval_args.max_new_tokens,
                "do_sample": eval_args.temperature > 0,
            }
            if eval_args.temperature > 0:
                gen_kwargs["temperature"] = eval_args.temperature
            outputs = model.generate(**inputs, **gen_kwargs)

        prompt_len = inputs["input_ids"].shape[1]
        for j in range(len(batch_prompts)):
            idx = batch_start + j
            generated_ids = outputs[j][prompt_len:]
            completion = tokenizer.decode(generated_ids, skip_special_tokens=True)

            parsed = parse_json_output(completion)
            pred_rels = parsed.get("relations", []) if parsed else []

            re_p, re_r, re_f1 = compute_re_f1(pred_rels, all_gold_rels[idx])
            evi_p, evi_r, evi_f1 = compute_evi_f1(pred_rels, all_gold_rels[idx], all_sentences[idx])
            attr = compute_attribution_precision(pred_rels)

            all_re_f1.append(re_f1)
            all_evi_f1.append(evi_f1)
            all_attr.append(attr)

            predictions.append({
                "index": idx,
                "completion": completion,
                "pred_relations": pred_rels,
                "re_f1": re_f1,
                "evi_f1": evi_f1,
                "attribution_precision": attr,
            })

        processed = batch_start + len(batch_prompts)
        if processed >= next_log or processed == len(all_prompts):
            print(f"[{processed}/{len(all_prompts)}] running RE-F1={sum(all_re_f1)/len(all_re_f1):.4f}")
            while next_log <= processed:
                next_log += 50

    # ── Aggregate ──────────────────────────────────────────────────────
    n = len(all_re_f1)
    metrics = {
        "num_samples": n,
        "re_f1": sum(all_re_f1) / n if n else 0,
        "evi_f1": sum(all_evi_f1) / n if n else 0,
        "attribution_precision": sum(all_attr) / n if n else 0,
    }

    # ── Report ─────────────────────────────────────────────────────────
    print("=" * 60)
    print("ProvUIE Evaluation Report")
    print("=" * 60)
    print(f"  Model:   {eval_args.model_path}")
    print(f"  Data:    {eval_args.eval_file}")
    print(f"  Samples: {n}")
    print("-" * 60)
    print(f"  RE F1:                 {metrics['re_f1']:.4f}")
    print(f"  Evidence F1:           {metrics['evi_f1']:.4f}")
    print(f"  Attribution Precision: {metrics['attribution_precision']:.4f}")
    print("=" * 60)

    # ── Save ───────────────────────────────────────────────────────────
    output = {"metrics": metrics, "predictions": predictions}
    out_path = Path(eval_args.output_file)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Results → {out_path}")


if __name__ == "__main__":
    main()
