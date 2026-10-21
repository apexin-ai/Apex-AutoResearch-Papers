#!/usr/bin/env python3
"""Frontier model SC experiment on FewNERD (exp_b_frontier_sc_fewnerd).

Tests whether the correlation-selection gap in structured self-consistency
persists with frontier models (GPT-5.5, Claude Opus 4.6), validating it
as a fundamental limitation rather than a capability issue.

CPU-only — all computation is via API calls through OpenRouter.

Usage:
    export OPENROUTER_API_KEY="[REDACTED]"
    python run_frontier_sc.py --data-path /path/to/fewnerd_test.jsonl
    python run_frontier_sc.py --from-hf  # load from HuggingFace
"""

from __future__ import annotations

import argparse
import json
import logging
import os
import random
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import spearmanr

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODELS = {
    "gpt-5.5": "openai/gpt-5.5",
    "claude-opus-4.6": "anthropic/claude-opus-4.6",
}

API_BASE_URL = "http://47.94.22.126/v1"

ENTITY_TYPES = {
    "person": "Person names",
    "organization": "Organizations, companies, teams",
    "location": "Geographic locations, countries, cities",
    "building": "Buildings, facilities, landmarks",
    "art": "Artworks, songs, films, books",
    "product": "Commercial products, software, vehicles",
    "event": "Events, competitions, wars, festivals",
    "other": "Other named entities not fitting the above categories",
}

VALID_TYPES = set(ENTITY_TYPES.keys())

MV_THRESHOLDS = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Data Loading
# ---------------------------------------------------------------------------

def _token_offsets(tokens: list[str]) -> list[tuple[int, int]]:
    offsets = []
    pos = 0
    for tok in tokens:
        offsets.append((pos, pos + len(tok)))
        pos += len(tok) + 1
    return offsets


def _bio_to_entities(tokens: list[str], tag_names: list[str], tag_ids: list[int]) -> list[dict]:
    """Convert BIO-tagged tokens to entity spans with char offsets."""
    offsets = _token_offsets(tokens)
    entities = []
    current = None

    for i, tag_id in enumerate(tag_ids):
        tag = tag_names[tag_id]

        if tag.startswith("B-"):
            if current is not None:
                entities.append(current)
            fine_type = tag[2:]
            coarse = fine_type.split("-")[0].lower()
            current = {
                "text": tokens[i],
                "type": coarse,
                "start": offsets[i][0],
                "end": offsets[i][1],
            }
        elif tag.startswith("I-") and current is not None:
            fine_type = tag[2:]
            coarse = fine_type.split("-")[0].lower()
            if coarse == current["type"]:
                current["text"] = current["text"] + " " + tokens[i]
                current["end"] = offsets[i][1]
            else:
                entities.append(current)
                current = None
        else:
            if current is not None:
                entities.append(current)
                current = None

    if current is not None:
        entities.append(current)

    return entities


def load_fewnerd_hf(n_instances: int = 200, seed: int = 42) -> list[dict]:
    """Load FewNERD test set from HuggingFace, convert to UIE format."""
    from datasets import load_dataset

    log.info("Loading FewNERD from HuggingFace (DFKI-SLT/few-nerd, supervised)...")
    ds = load_dataset("DFKI-SLT/few-nerd", "supervised", split="test")
    tag_names = ds.features["ner_tags"].feature.names

    instances = []
    for idx, example in enumerate(ds):
        tokens = example["tokens"]
        tag_ids = example["ner_tags"]
        text = " ".join(tokens)
        entities = _bio_to_entities(tokens, tag_names, tag_ids)

        instances.append({
            "id": f"fewnerd_test_{idx:05d}",
            "text": text,
            "entities": entities,
            "relations": [],
            "events": [],
        })

    instances_with_ents = [inst for inst in instances if inst["entities"]]
    log.info("  Total test: %d, with entities: %d", len(instances), len(instances_with_ents))

    rng = random.Random(seed)
    if len(instances_with_ents) > n_instances:
        instances_with_ents = rng.sample(instances_with_ents, n_instances)

    log.info("  Sampled %d instances (seed=%d)", len(instances_with_ents), seed)
    return instances_with_ents


def load_fewnerd_local(path: str, n_instances: int = 200, seed: int = 42) -> list[dict]:
    """Load FewNERD from local UIE-format JSONL file."""
    instances = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            if isinstance(obj, dict) and obj.get("entities"):
                instances.append(obj)

    log.info("Loaded %d instances with entities from %s", len(instances), path)

    rng = random.Random(seed)
    if len(instances) > n_instances:
        instances = rng.sample(instances, n_instances)

    log.info("Sampled %d instances (seed=%d)", len(instances), seed)
    return instances


# ---------------------------------------------------------------------------
# Prompt Construction (matches project template in zeroshot_prompts.py)
# ---------------------------------------------------------------------------

SYSTEM_PROMPT = (
    "You are a precise named entity recognition (NER) system. "
    "Extract all named entities from the given text and output them in the specified JSON format. "
    "Be exhaustive: identify every entity that matches the given types. "
    "Be precise: the 'start' and 'end' values must be character offsets in the original text, "
    "where 'start' is the index of the first character and 'end' is the index after the last character, "
    "such that text[start:end] == entity text."
)


def build_ner_prompt(text: str) -> list[dict]:
    type_desc_lines = "\n".join(f"  - {t}: {d}" for t, d in ENTITY_TYPES.items())
    user_prompt = (
        "Extract all named entities from the following text.\n\n"
        f"Entity types and their definitions:\n{type_desc_lines}\n\n"
        f"Text: {text}\n\n"
        "Output a JSON object in exactly this format:\n"
        '{"entities": [{"text": "exact span", "type": "TYPE", "start": 0, "end": 5}], '
        '"relations": [], "events": []}\n\n'
        "Rules:\n"
        "- Extract ALL entities matching the given types\n"
        "- 'start' is the character offset of the first character of the entity in the text\n"
        "- 'end' is the character offset after the last character (Python slice convention)\n"
        "- 'text' must be the exact substring from the input text\n"
        '- If no entities are found, return: {"entities": [], "relations": [], "events": []}\n'
        "- Output ONLY the JSON object, no explanation"
    )
    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt},
    ]


# ---------------------------------------------------------------------------
# API Sampling
# ---------------------------------------------------------------------------

def create_client(api_base: str):
    from openai import OpenAI

    api_key = [REDACTED]"OPENROUTER_API_KEY", "")
    if not api_key:
        log.error("OPENROUTER_API_KEY not set")
        sys.exit(1)
    return OpenAI(base_url=api_base, api_key=[REDACTED]


def _api_call(client, model_id: str, messages: list[dict],
              temperature: float, max_retries: int = 5) -> str:
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model_id,
                messages=messages,
                temperature=temperature,
                max_tokens=1024,
                response_format={"type": "json_object"},
            )
            return resp.choices[0].message.content or "{}"
        except Exception as e:
            wait = min(2 ** attempt * 1.0, 60)
            log.warning("  API error (attempt %d/%d): %s", attempt + 1, max_retries, e)
            if attempt < max_retries - 1:
                time.sleep(wait)
            else:
                log.error("  FAILED after %d attempts, returning empty", max_retries)
                return "{}"


def sample_instance(client, model_id: str, messages: list[dict],
                    n_samples: int, temperature: float) -> tuple[str, list[str]]:
    """Return (greedy_response, [n_samples stochastic responses])."""
    greedy = _api_call(client, model_id, messages, temperature=0.0)
    stochastic = []
    for _ in range(n_samples):
        stochastic.append(_api_call(client, model_id, messages, temperature=temperature))
    return greedy, stochastic


# ---------------------------------------------------------------------------
# Response Parsing
# ---------------------------------------------------------------------------

def parse_response(raw: str) -> dict:
    raw = raw.strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                data = json.loads(raw[start : end + 1])
            except json.JSONDecodeError:
                return {"entities": [], "relations": [], "events": []}
        else:
            return {"entities": [], "relations": [], "events": []}

    if not isinstance(data, dict):
        return {"entities": [], "relations": [], "events": []}

    entities = []
    for e in data.get("entities", []):
        if not isinstance(e, dict):
            continue
        try:
            etype = str(e["type"]).lower()
            if etype not in VALID_TYPES:
                continue
            entities.append({
                "text": str(e["text"]),
                "type": etype,
                "start": int(e["start"]),
                "end": int(e["end"]),
            })
        except (KeyError, ValueError, TypeError):
            continue

    return {"entities": entities, "relations": [], "events": []}


# ---------------------------------------------------------------------------
# Evaluation Primitives
# ---------------------------------------------------------------------------

def entity_set(entities: list[dict]) -> set[tuple]:
    return {(e["start"], e["end"], e["type"]) for e in entities}


def compute_prf(pred_set: set, gold_set: set) -> tuple[float, float, float]:
    if not gold_set and not pred_set:
        return 1.0, 1.0, 1.0
    if not pred_set:
        return 0.0, 0.0, 0.0
    if not gold_set:
        return 0.0, 0.0, 0.0
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0, 0.0, 0.0
    p = tp / len(pred_set)
    r = tp / len(gold_set)
    f = 2 * p * r / (p + r)
    return p, r, f


def entity_majority_vote(samples: list[dict], threshold: float = 0.5) -> set[tuple]:
    counts: dict[tuple, int] = defaultdict(int)
    N = len(samples)
    for sample in samples:
        for e in sample.get("entities", []):
            counts[(e["start"], e["end"], e["type"])] += 1
    return {k for k, c in counts.items() if c / N >= threshold}


# ---------------------------------------------------------------------------
# Instance-level Metrics
# ---------------------------------------------------------------------------

def compute_instance_metrics(
    greedy_parsed: dict,
    sc_parsed: list[dict],
    gold_entities: list[dict],
) -> dict:
    gold = entity_set(gold_entities)

    # Greedy F1
    greedy_ents = entity_set(greedy_parsed)
    g_p, g_r, g_f = compute_prf(greedy_ents, gold)

    # Per-sample F1
    sample_f1s = []
    for s in sc_parsed:
        _, _, f = compute_prf(entity_set(s), gold)
        sample_f1s.append(f)

    # MV at multiple thresholds
    mv_results = {}
    for t in MV_THRESHOLDS:
        mv_ents = entity_majority_vote(sc_parsed, threshold=t)
        mv_p, mv_r, mv_f = compute_prf(mv_ents, gold)
        mv_results[f"t{t:.1f}"] = {"p": mv_p, "r": mv_r, "f1": mv_f}

    # Entity-level agreement: frequency of each entity across N samples
    N = len(sc_parsed)
    ent_counts: dict[tuple, int] = defaultdict(int)
    for s in sc_parsed:
        for e in s.get("entities", []):
            ent_counts[(e["start"], e["end"], e["type"])] += 1

    agreement_scores = {str(k): v / N for k, v in ent_counts.items()}
    mean_agreement = float(np.mean(list(agreement_scores.values()))) if agreement_scores else 0.0

    # Degeneracy: all sample entity sets identical
    sample_sets = [frozenset(entity_set(s)) for s in sc_parsed]
    is_degenerate = len(set(sample_sets)) == 1

    # Oracle best-of-N
    oracle_f1 = max(sample_f1s) if sample_f1s else 0.0

    return {
        "greedy_p": g_p,
        "greedy_r": g_r,
        "greedy_f1": g_f,
        "sample_f1s": sample_f1s,
        "mean_sample_f1": float(np.mean(sample_f1s)) if sample_f1s else 0.0,
        "oracle_f1": oracle_f1,
        "mv": mv_results,
        "mean_agreement": mean_agreement,
        "n_unique_entities": len(ent_counts),
        "n_gold_entities": len(gold),
        "is_degenerate": is_degenerate,
    }


# ---------------------------------------------------------------------------
# Aggregate Analysis
# ---------------------------------------------------------------------------

def aggregate_model_results(results: list[dict]) -> dict:
    n = len(results)

    # Macro-averaged metrics
    greedy_f1s = [r["metrics"]["greedy_f1"] for r in results]
    oracle_f1s = [r["metrics"]["oracle_f1"] for r in results]
    mean_sample_f1s = [r["metrics"]["mean_sample_f1"] for r in results]
    agreements = [r["metrics"]["mean_agreement"] for r in results]
    degeneracy_flags = [r["metrics"]["is_degenerate"] for r in results]

    # MV F1 per threshold
    mv_f1_by_threshold = {}
    for t in MV_THRESHOLDS:
        tk = f"t{t:.1f}"
        f1s = [r["metrics"]["mv"][tk]["f1"] for r in results]
        mv_f1_by_threshold[tk] = {
            "mean_f1": float(np.mean(f1s)),
            "std_f1": float(np.std(f1s)),
        }

    # Best threshold
    best_t = max(mv_f1_by_threshold, key=lambda k: mv_f1_by_threshold[k]["mean_f1"])
    best_mv_f1 = mv_f1_by_threshold[best_t]["mean_f1"]

    greedy_mean = float(np.mean(greedy_f1s))
    selection_gap = best_mv_f1 - greedy_mean

    # Correlation: mean_agreement vs greedy_f1 (Spearman)
    if n >= 3:
        rho, pval = spearmanr(agreements, greedy_f1s)
        corr_agreement_f1 = {"rho": float(rho), "p": float(pval)}
    else:
        corr_agreement_f1 = {"rho": 0.0, "p": 1.0}

    # Correlation: mean_agreement vs MV F1 at best threshold
    best_mv_f1s = [r["metrics"]["mv"][best_t]["f1"] for r in results]
    if n >= 3:
        rho2, pval2 = spearmanr(agreements, best_mv_f1s)
        corr_agreement_mv = {"rho": float(rho2), "p": float(pval2)}
    else:
        corr_agreement_mv = {"rho": 0.0, "p": 1.0}

    return {
        "n_instances": n,
        "greedy_f1": {"mean": greedy_mean, "std": float(np.std(greedy_f1s))},
        "oracle_f1": {"mean": float(np.mean(oracle_f1s)), "std": float(np.std(oracle_f1s))},
        "mean_sample_f1": {"mean": float(np.mean(mean_sample_f1s)), "std": float(np.std(mean_sample_f1s))},
        "mv_f1_by_threshold": mv_f1_by_threshold,
        "best_threshold": best_t,
        "best_mv_f1": best_mv_f1,
        "selection_gap": selection_gap,
        "degeneracy_rate": sum(degeneracy_flags) / n,
        "mean_agreement": {"mean": float(np.mean(agreements)), "std": float(np.std(agreements))},
        "correlation_agreement_greedy_f1": corr_agreement_f1,
        "correlation_agreement_mv_f1": corr_agreement_mv,
    }


def diagnose_failure_modes(results: list[dict]) -> dict:
    """Categorize failure modes across instances."""
    n = len(results)
    degenerate = [r for r in results if r["metrics"]["is_degenerate"]]
    best_t_key = f"t0.5"

    mv_better = []
    mv_worse = []
    mv_same = []

    for r in results:
        g = r["metrics"]["greedy_f1"]
        m = r["metrics"]["mv"][best_t_key]["f1"]
        diff = m - g
        if diff > 0.01:
            mv_better.append(r)
        elif diff < -0.01:
            mv_worse.append(r)
        else:
            mv_same.append(r)

    # High agreement but wrong
    high_agree_wrong = [
        r for r in results
        if r["metrics"]["mean_agreement"] > 0.8 and r["metrics"]["greedy_f1"] < 0.5
    ]

    # Low agreement but correct
    low_agree_correct = [
        r for r in results
        if r["metrics"]["mean_agreement"] < 0.3 and r["metrics"]["greedy_f1"] > 0.8
    ]

    return {
        "degeneracy_count": len(degenerate),
        "degeneracy_rate": len(degenerate) / n,
        "mv_better_count": len(mv_better),
        "mv_worse_count": len(mv_worse),
        "mv_same_count": len(mv_same),
        "high_agreement_wrong_count": len(high_agree_wrong),
        "low_agreement_correct_count": len(low_agree_correct),
    }


# ---------------------------------------------------------------------------
# Checkpointing
# ---------------------------------------------------------------------------

def save_checkpoint(data: list[dict], path: str):
    with open(path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")


def load_checkpoint(path: str) -> list[dict]:
    if not os.path.exists(path):
        return []
    data = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                data.append(json.loads(line))
    return data


# ---------------------------------------------------------------------------
# Main Experiment Loop
# ---------------------------------------------------------------------------

def run_model(
    client,
    model_name: str,
    model_id: str,
    instances: list[dict],
    n_samples: int,
    temperature: float,
    output_dir: Path,
    resume: bool = True,
) -> list[dict]:
    ckpt_path = output_dir / f"checkpoint_{model_name}.jsonl"
    results = load_checkpoint(str(ckpt_path)) if resume else []
    done_ids = {r["id"] for r in results}

    remaining = [inst for inst in instances if inst["id"] not in done_ids]
    log.info("Model %s: %d done, %d remaining", model_name, len(done_ids), len(remaining))

    for i, inst in enumerate(remaining):
        log.info(
            "  [%d/%d] id=%s len=%d entities=%d",
            len(done_ids) + i + 1,
            len(instances),
            inst["id"],
            len(inst["text"]),
            len(inst["entities"]),
        )

        messages = build_ner_prompt(inst["text"])
        greedy_raw, sc_raws = sample_instance(
            client, model_id, messages, n_samples, temperature
        )

        greedy_parsed = parse_response(greedy_raw)
        sc_parsed = [parse_response(r) for r in sc_raws]

        metrics = compute_instance_metrics(greedy_parsed, sc_parsed, inst["entities"])

        result = {
            "id": inst["id"],
            "text": inst["text"],
            "gold_entities": inst["entities"],
            "greedy_raw": greedy_raw,
            "greedy_parsed": greedy_parsed,
            "sc_raws": sc_raws,
            "sc_parsed": sc_parsed,
            "metrics": metrics,
        }
        results.append(result)

        # Checkpoint every 10 instances
        if (len(done_ids) + i + 1) % 10 == 0:
            save_checkpoint(results, str(ckpt_path))
            running = aggregate_model_results(results)
            log.info(
                "    Checkpoint: greedy=%.4f, MV@0.5=%.4f, gap=%.4f, degen=%.1f%%",
                running["greedy_f1"]["mean"],
                running["mv_f1_by_threshold"]["t0.5"]["mean_f1"],
                running["selection_gap"],
                running["degeneracy_rate"] * 100,
            )

    save_checkpoint(results, str(ckpt_path))
    return results


def main():
    parser = argparse.ArgumentParser(description="Frontier SC on FewNERD")
    parser.add_argument("--data-path", type=str, default=None,
                        help="Path to local FewNERD UIE JSONL file")
    parser.add_argument("--from-hf", action="store_true",
                        help="Load FewNERD from HuggingFace")
    parser.add_argument("--n-instances", type=int, default=200)
    parser.add_argument("--n-samples", type=int, default=8)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--api-base", type=str, default=API_BASE_URL)
    parser.add_argument("--models", type=str, nargs="+", default=list(MODELS.keys()),
                        choices=list(MODELS.keys()),
                        help="Which models to run")
    parser.add_argument("--output-dir", type=str,
                        default=str(Path(__file__).parent / "output"))
    parser.add_argument("--no-resume", action="store_true",
                        help="Start fresh, ignore checkpoints")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    if args.data_path and os.path.exists(args.data_path):
        instances = load_fewnerd_local(args.data_path, args.n_instances, args.seed)
    elif args.from_hf:
        instances = load_fewnerd_hf(args.n_instances, args.seed)
    else:
        parser.error("Specify --data-path or --from-hf")

    # Save selected instance IDs for reproducibility
    id_list = [inst["id"] for inst in instances]
    with open(output_dir / "instance_ids.json", "w") as f:
        json.dump({"seed": args.seed, "n": len(id_list), "ids": id_list}, f, indent=2)

    client = create_client(args.api_base)

    all_summaries = {}

    for model_name in args.models:
        model_id = MODELS[model_name]
        log.info("=" * 60)
        log.info("Running model: %s (%s)", model_name, model_id)
        log.info("=" * 60)

        results = run_model(
            client, model_name, model_id, instances,
            args.n_samples, args.temperature, output_dir,
            resume=not args.no_resume,
        )

        # Aggregate
        summary = aggregate_model_results(results)
        diagnosis = diagnose_failure_modes(results)
        summary["diagnosis"] = diagnosis
        all_summaries[model_name] = summary

        # Print summary
        log.info("\n--- %s Summary ---", model_name)
        log.info("  Greedy F1:       %.4f (±%.4f)", summary["greedy_f1"]["mean"], summary["greedy_f1"]["std"])
        log.info("  Oracle F1:       %.4f", summary["oracle_f1"]["mean"])
        log.info("  Best MV F1:      %.4f (threshold=%s)", summary["best_mv_f1"], summary["best_threshold"])
        log.info("  Selection gap:   %+.4f", summary["selection_gap"])
        log.info("  Degeneracy rate: %.1f%%", summary["degeneracy_rate"] * 100)
        log.info("  Corr(agree,F1):  rho=%.4f (p=%.4f)",
                 summary["correlation_agreement_greedy_f1"]["rho"],
                 summary["correlation_agreement_greedy_f1"]["p"])
        log.info("  MV threshold sweep:")
        for t in MV_THRESHOLDS:
            tk = f"t{t:.1f}"
            mv = summary["mv_f1_by_threshold"][tk]
            delta = mv["mean_f1"] - summary["greedy_f1"]["mean"]
            marker = " <-- BEST" if tk == summary["best_threshold"] else ""
            log.info("    θ=%.1f  F1=%.4f  Δ=%+.4f%s", t, mv["mean_f1"], delta, marker)

    # Cross-model comparison
    if len(all_summaries) > 1:
        log.info("\n" + "=" * 60)
        log.info("CROSS-MODEL COMPARISON")
        log.info("=" * 60)
        log.info("%-20s %8s %8s %8s %10s %8s", "Model", "Greedy", "MV@best", "Oracle", "Gap", "Degen%")
        for name, s in all_summaries.items():
            log.info(
                "%-20s %8.4f %8.4f %8.4f %+10.4f %7.1f%%",
                name,
                s["greedy_f1"]["mean"],
                s["best_mv_f1"],
                s["oracle_f1"]["mean"],
                s["selection_gap"],
                s["degeneracy_rate"] * 100,
            )

    # Save final results
    final_output = {
        "config": {
            "n_instances": args.n_instances,
            "n_samples": args.n_samples,
            "temperature": args.temperature,
            "seed": args.seed,
            "api_base": args.api_base,
            "models": {m: MODELS[m] for m in args.models},
        },
        "summaries": all_summaries,
    }

    with open(output_dir / "results_summary.json", "w") as f:
        json.dump(final_output, f, indent=2, default=str)

    log.info("\nResults saved to %s", output_dir)


if __name__ == "__main__":
    main()
