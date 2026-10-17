#!/usr/bin/env python3
"""Schema Intervention Experiment: causal effect of type name renaming on RE accuracy.

Design: For each of 50 batches (25 low-BCS, 25 high-BCS), run control (original names)
and treatment (renamed high-SCS types to low-SCS alternatives), measure accuracy delta.

Input:  artifacts/exp_v2_re_n25/batch_groups.json
        data/fewrel_parquet/val.parquet + train.parquet
        Qwen3-32B-FP8 via vLLM OpenAI API at localhost:8000
Output: artifacts/exp_schema_intervention/results.json
        artifacts/exp_schema_intervention/analysis.json
"""
import json
import logging
import random
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import pandas as pd
from openai import OpenAI
from scipy import stats

logger = logging.getLogger(__name__)

BASE_DIR = Path("/root/schema-dag-extraction")
OUTPUT_DIR = BASE_DIR / "artifacts" / "exp_schema_intervention"
BATCH_GROUPS_PATH = BASE_DIR / "artifacts" / "exp_v2_re_n25" / "batch_groups.json"

RENAME_MAP = {
    "participant of": "event involvement",
    "located in the administrative territorial entity": "situated within governing region",
    "country of origin": "homeland provenance",
    "part of": "integral segment of",
    "follows": "prior entry",
    "member of": "affiliated with",
    "mother": "female progenitor",
    "position played on team": "athletic role on roster",
    "country of citizenship": "citizenship allegiance",
    "military rank": "service rank designation",
    "father": "paternal figure",
    "winner": "contest victor",
}

REVERSE_RENAME_MAP = {v: k for k, v in RENAME_MAP.items()}

SEED = 42
N_PER_REL = 12  # 12 * 80 = 960 total


def load_balanced_samples():
    """Load 960 balanced samples (12 per relation) from FewRel val+train."""
    all_samples = []
    for split in ["val", "train"]:
        path = BASE_DIR / "data" / "fewrel_parquet" / f"{split}.parquet"
        df = pd.read_parquet(path)
        for _, row in df.iterrows():
            all_samples.append({
                "text": row["text"],
                "head_entity": row["head_entity"],
                "tail_entity": row["tail_entity"],
                "relation_type": row["relation_type"],
            })

    by_rel = defaultdict(list)
    for s in all_samples:
        by_rel[s["relation_type"]].append(s)

    rng = random.Random(SEED)
    sampled = []
    for rel in sorted(by_rel.keys()):
        pool = by_rel[rel]
        k = min(N_PER_REL, len(pool))
        sampled.extend(rng.sample(pool, k))

    logger.info("Loaded %d balanced samples (%d relations)", len(sampled), len(by_rel))
    return sampled


def build_re_prompt(sentence, head, tail, relation_types):
    """Build RE classification prompt matching existing format."""
    candidates = ", ".join(sorted(relation_types))
    return (
        "Given the following sentence and two entities, "
        "classify the relation between them.\n\n"
        f'Sentence: "{sentence}"\n'
        f'Head entity: "{head}"\n'
        f'Tail entity: "{tail}"\n\n'
        f"Candidate relations: {candidates}\n\n"
        'Output a single JSON object: {"relation": "<relation_type>"}\n'
        'If none of the candidate relations apply, output: {"relation": "none"}'
    )


def call_vllm_batch(client, prompts, relation_types, model_name):
    """Call vLLM server with guided JSON decoding for a batch of prompts."""
    json_schema = {
        "type": "object",
        "properties": {
            "relation": {
                "type": "string",
                "enum": sorted(relation_types) + ["none"],
            },
        },
        "required": ["relation"],
    }

    results = []
    for prompt in prompts:
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0,
                max_tokens=64,
                extra_body={"guided_json": json.dumps(json_schema)},
            )
            text = response.choices[0].message.content.strip()
            try:
                parsed = json.loads(text)
                pred = parsed.get("relation", "none")
            except json.JSONDecodeError:
                pred = text.strip().strip('"')
        except Exception as e:
            logger.warning("API call failed: %s", e)
            pred = "none"
        results.append(pred)

    return results


def run_batch_experiment(client, model_name, samples, batch_types, batch_id, group, bcs):
    """Run control + treatment for one batch. Returns result dict."""
    type_set = set(batch_types)
    batch_samples = [s for s in samples if s["relation_type"] in type_set]

    if not batch_samples:
        logger.warning("No samples for batch %s", batch_id)
        return None

    # Determine which types in this batch can be renamed
    renameable = [t for t in batch_types if t in RENAME_MAP]
    n_renamed = len(renameable)

    # --- CONTROL: original type names ---
    control_prompts = [
        build_re_prompt(s["text"], s["head_entity"], s["tail_entity"], batch_types)
        for s in batch_samples
    ]
    control_preds = call_vllm_batch(client, control_prompts, batch_types, model_name)

    control_correct = sum(
        1 for s, p in zip(batch_samples, control_preds)
        if p == s["relation_type"]
    )
    control_acc = control_correct / len(batch_samples)

    # --- TREATMENT: rename high-SCS types ---
    if n_renamed == 0:
        # No renaming possible, treatment == control
        treatment_acc = control_acc
        treatment_correct = control_correct
        treatment_preds = control_preds
    else:
        # Build renamed type list
        treatment_types = [RENAME_MAP.get(t, t) for t in batch_types]

        treatment_prompts = [
            build_re_prompt(s["text"], s["head_entity"], s["tail_entity"], treatment_types)
            for s in batch_samples
        ]
        raw_preds = call_vllm_batch(client, treatment_prompts, treatment_types, model_name)

        # Map predictions back to original names
        treatment_preds = []
        for pred in raw_preds:
            if pred in REVERSE_RENAME_MAP:
                treatment_preds.append(REVERSE_RENAME_MAP[pred])
            else:
                treatment_preds.append(pred)

        treatment_correct = sum(
            1 for s, p in zip(batch_samples, treatment_preds)
            if p == s["relation_type"]
        )
        treatment_acc = treatment_correct / len(batch_samples)

    delta = treatment_acc - control_acc

    result = {
        "batch_id": batch_id,
        "group": group,
        "bcs": bcs,
        "n_samples": len(batch_samples),
        "n_types_renamed": n_renamed,
        "renamed_types": renameable,
        "control_acc": round(control_acc, 4),
        "treatment_acc": round(treatment_acc, 4),
        "delta": round(delta, 4),
        "control_correct": control_correct,
        "treatment_correct": treatment_correct,
    }

    logger.info(
        "  %s: control=%.4f treatment=%.4f delta=%+.4f (%d renamed, %d samples)",
        batch_id, control_acc, treatment_acc, delta, n_renamed, len(batch_samples)
    )
    return result


def run_analysis(results):
    """Statistical analysis: paired t-tests and interaction effect."""
    low_results = [r for r in results if r["group"] == "low"]
    high_results = [r for r in results if r["group"] == "high"]

    # Only analyze batches where renaming actually happened
    low_renamed = [r for r in low_results if r["n_types_renamed"] > 0]
    high_renamed = [r for r in high_results if r["n_types_renamed"] > 0]

    analysis = {
        "n_low_total": len(low_results),
        "n_high_total": len(high_results),
        "n_low_with_rename": len(low_renamed),
        "n_high_with_rename": len(high_renamed),
    }

    # Within high-BCS group: treatment vs control
    if len(high_renamed) >= 2:
        high_deltas = [r["delta"] for r in high_renamed]
        high_control = [r["control_acc"] for r in high_renamed]
        high_treatment = [r["treatment_acc"] for r in high_renamed]
        t_high, p_high = stats.ttest_rel(high_treatment, high_control)
        analysis["high_bcs_group"] = {
            "mean_delta": round(float(np.mean(high_deltas)), 4),
            "std_delta": round(float(np.std(high_deltas, ddof=1)), 4),
            "mean_control_acc": round(float(np.mean(high_control)), 4),
            "mean_treatment_acc": round(float(np.mean(high_treatment)), 4),
            "paired_ttest_t": round(float(t_high), 4),
            "paired_ttest_p": round(float(p_high), 6),
            "n": len(high_renamed),
            "cohens_d": round(float(np.mean(high_deltas) / (np.std(high_deltas, ddof=1) + 1e-10)), 4),
        }

    # Within low-BCS group: treatment vs control
    if len(low_renamed) >= 2:
        low_deltas = [r["delta"] for r in low_renamed]
        low_control = [r["control_acc"] for r in low_renamed]
        low_treatment = [r["treatment_acc"] for r in low_renamed]
        t_low, p_low = stats.ttest_rel(low_treatment, low_control)
        analysis["low_bcs_group"] = {
            "mean_delta": round(float(np.mean(low_deltas)), 4),
            "std_delta": round(float(np.std(low_deltas, ddof=1)), 4),
            "mean_control_acc": round(float(np.mean(low_control)), 4),
            "mean_treatment_acc": round(float(np.mean(low_treatment)), 4),
            "paired_ttest_t": round(float(t_low), 4),
            "paired_ttest_p": round(float(p_low), 6),
            "n": len(low_renamed),
            "cohens_d": round(float(np.mean(low_deltas) / (np.std(low_deltas, ddof=1) + 1e-10)), 4),
        }

    # Interaction: is renaming benefit larger in high-BCS?
    if len(high_renamed) >= 2 and len(low_renamed) >= 2:
        high_deltas = [r["delta"] for r in high_renamed]
        low_deltas = [r["delta"] for r in low_renamed]
        t_inter, p_inter = stats.ttest_ind(high_deltas, low_deltas)
        analysis["interaction"] = {
            "high_mean_delta": round(float(np.mean(high_deltas)), 4),
            "low_mean_delta": round(float(np.mean(low_deltas)), 4),
            "difference": round(float(np.mean(high_deltas) - np.mean(low_deltas)), 4),
            "ttest_t": round(float(t_inter), 4),
            "ttest_p": round(float(p_inter), 6),
        }

    # Correlation: n_types_renamed vs delta
    all_renamed = [r for r in results if r["n_types_renamed"] > 0]
    if len(all_renamed) >= 3:
        n_renames = [r["n_types_renamed"] for r in all_renamed]
        deltas = [r["delta"] for r in all_renamed]
        r_val, r_p = stats.pearsonr(n_renames, deltas)
        analysis["rename_count_correlation"] = {
            "pearson_r": round(float(r_val), 4),
            "p_value": round(float(r_p), 6),
            "n": len(all_renamed),
        }

    return analysis


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load batch groups
    with open(BATCH_GROUPS_PATH) as f:
        batch_groups = json.load(f)

    low_batches = batch_groups["low"][:25]
    high_batches = batch_groups["high"][:25]
    logger.info("Loaded %d low + %d high batches", len(low_batches), len(high_batches))

    # Load balanced samples
    samples = load_balanced_samples()

    # Connect to vLLM server
    client = OpenAI(base_url="http://localhost:8000/v1", api_key="[REDACTED]")

    # Get model name
    models = client.models.list()
    model_name = models.data[0].id
    logger.info("Using model: %s", model_name)

    # Run experiment
    all_results = []
    results_path = OUTPUT_DIR / "results_incremental.jsonl"

    for i, batch in enumerate(low_batches):
        batch_id = f"low_{i}"
        result = run_batch_experiment(
            client, model_name, samples,
            batch["types"], batch_id, "low", batch["bcs"]
        )
        if result:
            all_results.append(result)
            with open(results_path, "a") as f:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")

    for i, batch in enumerate(high_batches):
        batch_id = f"high_{i}"
        result = run_batch_experiment(
            client, model_name, samples,
            batch["types"], batch_id, "high", batch["bcs"]
        )
        if result:
            all_results.append(result)
            with open(results_path, "a") as f:
                f.write(json.dumps(result, ensure_ascii=False) + "\n")

    # Save full results
    with open(OUTPUT_DIR / "results.json", "w") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)

    # Run analysis
    analysis = run_analysis(all_results)
    with open(OUTPUT_DIR / "analysis.json", "w") as f:
        json.dump(analysis, f, indent=2)

    # Print summary
    logger.info("=" * 70)
    logger.info("SCHEMA INTERVENTION RESULTS")
    logger.info("=" * 70)
    logger.info("Total batches: %d", len(all_results))
    logger.info("Batches with renaming: %d",
                sum(1 for r in all_results if r["n_types_renamed"] > 0))

    if "high_bcs_group" in analysis:
        h = analysis["high_bcs_group"]
        logger.info("HIGH-BCS group (n=%d): mean_delta=%+.4f, t=%.4f, p=%.6f",
                    h["n"], h["mean_delta"], h["paired_ttest_t"], h["paired_ttest_p"])

    if "low_bcs_group" in analysis:
        lo = analysis["low_bcs_group"]
        logger.info("LOW-BCS group (n=%d): mean_delta=%+.4f, t=%.4f, p=%.6f",
                    lo["n"], lo["mean_delta"], lo["paired_ttest_t"], lo["paired_ttest_p"])

    if "interaction" in analysis:
        inter = analysis["interaction"]
        logger.info("INTERACTION: high_delta=%+.4f, low_delta=%+.4f, diff=%+.4f, p=%.6f",
                    inter["high_mean_delta"], inter["low_mean_delta"],
                    inter["difference"], inter["ttest_p"])

    logger.info("Results saved to %s", OUTPUT_DIR)


if __name__ == "__main__":
    main()
