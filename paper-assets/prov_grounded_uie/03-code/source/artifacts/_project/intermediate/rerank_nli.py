"""Post-hoc NLI Reranking for ProvUIE (MVP Step 3).

Scores SFT-generated evidence spans with an NLI model and applies
filter/rerank/oracle strategies to measure evidence quality ceiling.

Input:  SFT checkpoint (or pre-computed predictions JSON) + dev JSONL + NLI model.
Output: outputs/nli_reranking_results.json with per-strategy metrics.

Usage:
    # Generate from SFT model + rerank
    python rerank_nli.py --model_path ./outputs/sft/merged --eval_file ./data/docred_dev.jsonl

    # Rerank from saved evaluate.py output (skip generation)
    python rerank_nli.py --predictions_file ./outputs/eval_results.json \
                         --eval_file ./data/docred_dev.jsonl

Dependencies: evaluate.py, rewards.py, data_utils.py, config.py
"""

import gc
import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, HfArgumentParser

from config import ModelArgs, EvalArgs, RewardArgs
from data_utils import load_grpo_dataset
from evaluate import compute_re_f1, compute_evi_f1, compute_attribution_precision
from rewards import parse_json_output, _batch_nli_scores


@dataclass
class NLIRerankArgs:
    """NLI reranking configuration."""

    output_dir: str = field(
        default="./outputs",
        metadata={"help": "Output directory for results"},
    )
    filter_thresholds: str = field(
        default="0.3,0.5,0.7,0.9",
        metadata={"help": "Comma-separated NLI filter thresholds to sweep"},
    )
    predictions_file: Optional[str] = field(
        default=None,
        metadata={"help": "Pre-computed predictions JSON from evaluate.py (skips generation)"},
    )

    def get_thresholds(self) -> list[float]:
        return [float(t.strip()) for t in self.filter_thresholds.split(",")]


# ---------------------------------------------------------------------------
# Generation (reuses evaluate.py model-loading pattern)
# ---------------------------------------------------------------------------


def generate_predictions(
    model_args: ModelArgs, eval_args: EvalArgs, dataset
) -> list[dict]:
    """Run SFT model on dataset and return per-sample predictions.

    Frees GPU memory after generation so the NLI model can load.
    """
    tokenizer = AutoTokenizer.from_pretrained(
        eval_args.model_path, trust_remote_code=True
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model_kwargs: dict = {"trust_remote_code": True, "torch_dtype": "auto"}
    if model_args.use_flash_attention:
        model_kwargs["attn_implementation"] = "flash_attention_2"

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
        model = AutoModelForCausalLM.from_pretrained(
            eval_args.model_path, **model_kwargs
        )

    device = "cuda" if torch.cuda.is_available() else "cpu"
    model.to(device).eval()

    results = []
    for i in range(len(dataset)):
        prompt_messages = dataset[i]["prompt"]
        gold_rels = json.loads(dataset[i]["gold_relations"])
        sentences = json.loads(dataset[i]["sentences"])
        document_text = dataset[i]["document_text"]

        input_text = tokenizer.apply_chat_template(
            prompt_messages, tokenize=False, add_generation_prompt=True
        )
        inputs = tokenizer(
            input_text, return_tensors="pt", truncation=True, max_length=2048
        ).to(device)

        with torch.no_grad():
            gen_kwargs = {
                "max_new_tokens": eval_args.max_new_tokens,
                "do_sample": eval_args.temperature > 0,
            }
            if eval_args.temperature > 0:
                gen_kwargs["temperature"] = eval_args.temperature
            outputs = model.generate(**inputs, **gen_kwargs)

        generated_ids = outputs[0][inputs["input_ids"].shape[1] :]
        completion = tokenizer.decode(generated_ids, skip_special_tokens=True)
        parsed = parse_json_output(completion)
        pred_rels = parsed.get("relations", []) if parsed else []

        results.append(
            {
                "index": i,
                "completion": completion,
                "pred_rels": pred_rels,
                "gold_rels": gold_rels,
                "sentences": sentences,
                "document_text": document_text,
            }
        )

        if (i + 1) % 50 == 0:
            print(f"[Generation {i + 1}/{len(dataset)}]")

    del model, tokenizer
    torch.cuda.empty_cache()
    gc.collect()
    print(f"Generated {len(results)} predictions, freed generation model.")

    return results


def load_predictions(predictions_file: str, dataset) -> list[dict]:
    """Load pre-computed predictions from evaluate.py output and merge with dataset metadata."""
    with open(predictions_file) as f:
        saved = json.load(f)

    preds = saved["predictions"]
    results = []
    for i, pred in enumerate(preds):
        gold_rels = json.loads(dataset[i]["gold_relations"])
        sentences = json.loads(dataset[i]["sentences"])
        results.append(
            {
                "index": i,
                "completion": pred["completion"],
                "pred_rels": pred.get("pred_relations", []),
                "gold_rels": gold_rels,
                "sentences": sentences,
                "document_text": dataset[i]["document_text"],
            }
        )
    return results


# ---------------------------------------------------------------------------
# NLI Scoring
# ---------------------------------------------------------------------------


def score_evidence_with_nli(
    samples: list[dict], nli_model_name: str, nli_batch_size: int
) -> list[dict]:
    """Score each evidence span with NLI entailment probability.

    premise = evidence span, hypothesis = "head relation tail" claim.
    Augments each relation dict with 'nli_scores' parallel to 'evidence'.
    """
    premises: list[str] = []
    hypotheses: list[str] = []
    span_map: list[tuple[int, int, int]] = []

    for si, sample in enumerate(samples):
        for ri, rel in enumerate(sample["pred_rels"]):
            evidence = rel.get("evidence", [])
            claim = (
                f'{rel.get("head", "")} {rel.get("relation", "")} '
                f'{rel.get("tail", "")}'
            )
            for ei, span in enumerate(evidence):
                if isinstance(span, str) and span.strip():
                    premises.append(span)
                    hypotheses.append(claim)
                    span_map.append((si, ri, ei))

    for sample in samples:
        for rel in sample["pred_rels"]:
            rel["nli_scores"] = [0.0] * len(rel.get("evidence", []))

    if not premises:
        return samples

    print(f"Scoring {len(premises)} evidence spans with NLI ({nli_model_name})...")
    scores = _batch_nli_scores(
        premises, hypotheses, model_name=nli_model_name, batch_size=nli_batch_size
    )

    for (si, ri, ei), score in zip(span_map, scores):
        samples[si]["pred_rels"][ri]["nli_scores"][ei] = score

    return samples


def compute_oracle_nli_stats(
    samples: list[dict], nli_model_name: str, nli_batch_size: int
) -> dict:
    """NLI scores on gold evidence — upper bound on what NLI can detect."""
    premises: list[str] = []
    hypotheses: list[str] = []

    for sample in samples:
        for rel in sample["gold_rels"]:
            claim = f'{rel["head"]} {rel["relation"]} {rel["tail"]}'
            for span in rel.get("evidence", []):
                if isinstance(span, str) and span.strip():
                    premises.append(span)
                    hypotheses.append(claim)

    if not premises:
        return {"mean_nli_score": 0.0, "num_spans": 0}

    print(f"Computing oracle NLI on {len(premises)} gold evidence spans...")
    scores = _batch_nli_scores(
        premises, hypotheses, model_name=nli_model_name, batch_size=nli_batch_size
    )

    return {
        "mean_nli_score": sum(scores) / len(scores),
        "num_spans": len(scores),
        "fraction_above_0.5": sum(1 for s in scores if s >= 0.5) / len(scores),
        "fraction_above_0.7": sum(1 for s in scores if s >= 0.7) / len(scores),
        "fraction_above_0.9": sum(1 for s in scores if s >= 0.9) / len(scores),
    }


# ---------------------------------------------------------------------------
# Reranking Strategies
# ---------------------------------------------------------------------------


def apply_filter(pred_rels: list[dict], threshold: float) -> list[dict]:
    """Remove evidence spans with NLI score below threshold."""
    filtered = []
    for rel in pred_rels:
        new_rel = {k: v for k, v in rel.items() if k != "nli_scores"}
        evidence = rel.get("evidence", [])
        scores = rel.get("nli_scores", [0.0] * len(evidence))
        new_rel["evidence"] = [
            ev for ev, sc in zip(evidence, scores) if sc >= threshold
        ]
        filtered.append(new_rel)
    return filtered


def apply_rerank_topk(pred_rels: list[dict], k: int) -> list[dict]:
    """Sort evidence by NLI score descending, keep top-k per relation."""
    reranked = []
    for rel in pred_rels:
        new_rel = {k_: v for k_, v in rel.items() if k_ != "nli_scores"}
        evidence = rel.get("evidence", [])
        scores = rel.get("nli_scores", [0.0] * len(evidence))
        sorted_pairs = sorted(zip(scores, evidence), reverse=True)
        new_rel["evidence"] = [ev for _, ev in sorted_pairs[:k]]
        reranked.append(new_rel)
    return reranked


# ---------------------------------------------------------------------------
# Metrics
# ---------------------------------------------------------------------------


def compute_sample_metrics(
    pred_rels: list[dict], gold_rels: list[dict], sentences: list[str]
) -> dict:
    """All metrics for a single sample."""
    re_p, re_r, re_f1 = compute_re_f1(pred_rels, gold_rels)
    evi_p, evi_r, evi_f1 = compute_evi_f1(pred_rels, gold_rels, sentences)
    attr = compute_attribution_precision(pred_rels)
    return {
        "re_f1": re_f1,
        "evi_precision": evi_p,
        "evi_recall": evi_r,
        "evi_f1": evi_f1,
        "attribution_precision": attr,
    }


def aggregate_metrics(per_sample: list[dict]) -> dict:
    """Macro-average per-sample metrics."""
    n = len(per_sample)
    if n == 0:
        return {}
    return {k: sum(s[k] for s in per_sample) / n for k in per_sample[0]}


def mean_nli_score(all_pred_rels: list[list[dict]]) -> float:
    """Average NLI score across all evidence spans in all samples."""
    total, count = 0.0, 0
    for pred_rels in all_pred_rels:
        for rel in pred_rels:
            for sc in rel.get("nli_scores", []):
                total += sc
                count += 1
    return total / count if count > 0 else 0.0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = HfArgumentParser((ModelArgs, EvalArgs, RewardArgs, NLIRerankArgs))
    model_args, eval_args, reward_args, rerank_args = (
        parser.parse_args_into_dataclasses()
    )

    dataset = load_grpo_dataset(eval_args.eval_file)
    thresholds = rerank_args.get_thresholds()

    # ── Step 1: Get predictions ───────────────────────────────────────
    if rerank_args.predictions_file:
        print(f"Loading predictions from {rerank_args.predictions_file}")
        samples = load_predictions(rerank_args.predictions_file, dataset)
    else:
        print(f"Generating predictions from {eval_args.model_path}")
        samples = generate_predictions(model_args, eval_args, dataset)

    # ── Step 2: NLI scoring ───────────────────────────────────────────
    samples = score_evidence_with_nli(
        samples, reward_args.nli_model_name, reward_args.nli_batch_size
    )

    # ── Step 3: Baseline (original predictions) ───────────────────────
    baseline_per_sample = [
        compute_sample_metrics(s["pred_rels"], s["gold_rels"], s["sentences"])
        for s in samples
    ]
    baseline_agg = aggregate_metrics(baseline_per_sample)
    baseline_agg["mean_nli_score"] = mean_nli_score(
        [s["pred_rels"] for s in samples]
    )

    print(
        f"\nBaseline: RE-F1={baseline_agg['re_f1']:.4f}  "
        f"Evi-F1={baseline_agg['evi_f1']:.4f}  "
        f"AttrPrec={baseline_agg['attribution_precision']:.4f}  "
        f"NLI={baseline_agg['mean_nli_score']:.4f}"
    )

    # ── Step 4a: NLI-filter (threshold sweep) ─────────────────────────
    filter_results = {}
    for t in thresholds:
        per_sample_metrics = []
        total_kept, total_orig = 0, 0
        for s in samples:
            filtered = apply_filter(s["pred_rels"], t)
            per_sample_metrics.append(
                compute_sample_metrics(filtered, s["gold_rels"], s["sentences"])
            )
            total_orig += sum(len(r.get("evidence", [])) for r in s["pred_rels"])
            total_kept += sum(len(r.get("evidence", [])) for r in filtered)

        agg = aggregate_metrics(per_sample_metrics)
        agg["evidence_retention_rate"] = (
            total_kept / total_orig if total_orig > 0 else 0.0
        )
        filter_results[str(t)] = agg
        print(
            f"NLI-filter@{t}: Evi-F1={agg['evi_f1']:.4f}  "
            f"EviP={agg['evi_precision']:.4f}  EviR={agg['evi_recall']:.4f}  "
            f"AttrPrec={agg['attribution_precision']:.4f}  "
            f"Retention={agg['evidence_retention_rate']:.2%}"
        )

    # ── Step 4b: NLI-rerank (top-1 and top-3) ────────────────────────
    # Evi F1 is set-based, so pure reordering doesn't change it;
    # top-k truncation is needed to see the effect.
    rerank_results = {}
    for k in [1, 3]:
        per_sample_metrics = [
            compute_sample_metrics(
                apply_rerank_topk(s["pred_rels"], k),
                s["gold_rels"],
                s["sentences"],
            )
            for s in samples
        ]
        agg = aggregate_metrics(per_sample_metrics)
        rerank_results[f"top{k}"] = agg
        print(
            f"NLI-rerank-top{k}: Evi-F1={agg['evi_f1']:.4f}  "
            f"EviP={agg['evi_precision']:.4f}  EviR={agg['evi_recall']:.4f}"
        )

    # ── Step 4c: NLI-oracle (gold evidence scores) ────────────────────
    oracle_stats = compute_oracle_nli_stats(
        samples, reward_args.nli_model_name, reward_args.nli_batch_size
    )
    print(
        f"NLI-oracle: mean_gold_NLI={oracle_stats['mean_nli_score']:.4f}  "
        f">0.5={oracle_stats.get('fraction_above_0.5', 0):.2%}  "
        f">0.7={oracle_stats.get('fraction_above_0.7', 0):.2%}"
    )

    # ── Step 5: Save results ──────────────────────────────────────────
    output = {
        "config": {
            "model_path": eval_args.model_path,
            "eval_file": eval_args.eval_file,
            "nli_model": reward_args.nli_model_name,
            "filter_thresholds": thresholds,
        },
        "baseline": baseline_agg,
        "nli_filter": filter_results,
        "nli_rerank": rerank_results,
        "nli_oracle": oracle_stats,
        "per_sample": [
            {
                "index": s["index"],
                "pred_rels_with_nli": [
                    {k: v for k, v in r.items()} for r in s["pred_rels"]
                ],
                "baseline_metrics": bm,
            }
            for s, bm in zip(samples, baseline_per_sample)
        ],
    }

    out_path = Path(rerank_args.output_dir) / "nli_reranking_results.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\nResults -> {out_path}")


if __name__ == "__main__":
    main()
