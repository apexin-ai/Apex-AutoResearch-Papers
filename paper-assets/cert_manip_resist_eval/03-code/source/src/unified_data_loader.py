#!/usr/bin/env python3
"""Unified data loader for 15-model cert_manip_resist_eval pipeline.

Handles two data formats:
  - Checkpoint files (local 6 models): nested {clean_scores: {ds: {model: [...]}}}
  - Individual JSON files (API 9 models): flat {scores: [...], asr, accuracy, ...}
"""

import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# ── Model lists ──────────────────────────────────────────────────────
LOCAL_MODELS = [
    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
]
API_MODELS = [
    "claude-opus-4", "gpt-5.5", "gemini-2.5-pro", "gpt-4.1",
    "claude-sonnet-4", "gpt-4o", "gemini-2.5-flash",
    "gpt-4o-mini", "claude-3-haiku",
]
ALL_MODELS = LOCAL_MODELS + API_MODELS
DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]

# ── Default paths ────────────────────────────────────────────────────
RESULTS_DIR = Path("/root/cert_manip_resist_eval/artifacts/results")
PLAN001_DIR = RESULTS_DIR / "plan001"
SCORES_DIR = PLAN001_DIR / "individual_scores"
MI_PATH = PLAN001_DIR / "mi_matrix" / "mi_matrix_15models.json"
CKPT_FILES = [
    RESULTS_DIR / "_taxonomy_checkpoint.json",
    RESULTS_DIR / "_step2v3_checkpoint.json",
]
OUTPUT_DIR = PLAN001_DIR / "panel_regression"


def _is_valid_score(s):
    if s.get("error") or s.get("format_error"):
        return False
    if s.get("winner") not in ("A", "B", "tie"):
        return False
    return True


def _invert_winners(scores):
    swap = {"A": "B", "B": "A", "tie": "tie"}
    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]


def load_all_scores(
    checkpoint_files=None,
    individual_dir=None,
    datasets=None,
    attacks=None,
    all_models=None,
):
    """Load sample-level clean + attacked scores for all 15 models.

    Returns:
        clean:    {ds: {model_id: [score_dicts]}}
        attacked: {ds: {atk: {model_id: [score_dicts]}}}
    """
    checkpoint_files = checkpoint_files or CKPT_FILES
    individual_dir = Path(individual_dir or SCORES_DIR)
    datasets = datasets or DATASETS
    attacks = attacks or ATTACKS
    all_models = all_models or ALL_MODELS

    clean = {ds: {} for ds in datasets}
    attacked = {ds: {a: {} for a in attacks} for ds in datasets}

    for ckpt_path in checkpoint_files:
        ckpt_path = Path(ckpt_path)
        if not ckpt_path.exists():
            logger.warning(f"Checkpoint not found: {ckpt_path}")
            continue
        logger.info(f"Loading checkpoint: {ckpt_path.name}")
        with open(ckpt_path) as f:
            data = json.load(f)
        for ds in datasets:
            for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
                if mid not in clean[ds]:
                    clean[ds][mid] = scores
            for atk in attacks:
                for mid, scores in (
                    data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items()
                ):
                    if mid not in attacked[ds][atk]:
                        if atk == "position_bias":
                            scores = _invert_winners(scores)
                        attacked[ds][atk][mid] = scores

    if individual_dir.exists():
        logger.info(f"Loading individual scores from {individual_dir}")
        for mid in all_models:
            for ds in datasets:
                fp = individual_dir / f"{mid}__{ds}__clean.json"
                if fp.exists() and mid not in clean[ds]:
                    with open(fp) as f:
                        clean[ds][mid] = json.load(f).get("scores", [])
                for atk in attacks:
                    fp = individual_dir / f"{mid}__{ds}__{atk}.json"
                    if fp.exists() and mid not in attacked[ds][atk]:
                        with open(fp) as f:
                            scores = json.load(f).get("scores", [])
                        if atk == "position_bias":
                            scores = _invert_winners(scores)
                        attacked[ds][atk][mid] = scores

    for ds in datasets:
        nc = len(clean[ds])
        logger.info(f"  {ds} clean: {nc}/{len(all_models)}")
        for atk in attacks:
            na = len(attacked[ds][atk])
            if na > 0:
                logger.info(f"  {ds} {atk}: {na}/{len(all_models)}")

    return clean, attacked


def load_pairs(checkpoint_files=None, datasets=None):
    """Load evaluation pairs from checkpoint files.

    Returns: {ds: [pair_dicts]} with up to 300 pairs per dataset.
    """
    checkpoint_files = checkpoint_files or CKPT_FILES
    datasets = datasets or DATASETS

    for ckpt_path in checkpoint_files:
        ckpt_path = Path(ckpt_path)
        if not ckpt_path.exists():
            continue
        with open(ckpt_path) as f:
            data = json.load(f)
        if "pairs" not in data:
            continue
        pairs = {}
        for ds in datasets:
            if ds in data["pairs"]:
                pairs[ds] = data["pairs"][ds][:300]
                logger.info(f"  Pairs {ds}: {len(pairs[ds])} from {ckpt_path.name}")
        if pairs:
            return pairs
    raise FileNotFoundError("No pairs found in any checkpoint file")


def load_mi_data(mi_path=None):
    """Load MI matrix from Step 3 output."""
    mi_path = Path(mi_path or MI_PATH)
    if not mi_path.exists():
        raise FileNotFoundError(
            f"MI matrix not found: {mi_path}. Run Step 3 first."
        )
    with open(mi_path) as f:
        data = json.load(f)
    logger.info(f"Loaded MI matrix: {len(data['models'])} models")
    return data


def load_api_asr(individual_dir=None, datasets=None, attacks=None, api_models=None):
    """Load pre-computed ASR for API models from individual score files.

    Returns: {ds: {atk: {model_id: asr}}}
    """
    individual_dir = Path(individual_dir or SCORES_DIR)
    datasets = datasets or DATASETS
    attacks = attacks or ATTACKS
    api_models = api_models or API_MODELS

    asr_data = {}
    for model_id in api_models:
        for ds in datasets:
            if ds not in asr_data:
                asr_data[ds] = {}
            clean_path = individual_dir / f"{model_id}__{ds}__clean.json"
            if not clean_path.exists():
                continue
            for atk in attacks:
                if atk not in asr_data[ds]:
                    asr_data[ds][atk] = {}
                atk_path = individual_dir / f"{model_id}__{ds}__{atk}.json"
                if not atk_path.exists():
                    continue
                with open(atk_path) as f:
                    atk_data = json.load(f)
                asr = atk_data.get("asr")
                if asr is not None:
                    asr_data[ds][atk][model_id] = asr
    return asr_data


def validate_coverage(clean, attacked, datasets=None, attacks=None,
                      all_models=None, expected_samples=300):
    """Check that all models have expected number of samples. Returns list of issues."""
    datasets = datasets or DATASETS
    attacks = attacks or ATTACKS
    all_models = all_models or ALL_MODELS

    issues = []
    for ds in datasets:
        for mid in all_models:
            if mid not in clean[ds]:
                issues.append(f"MISSING clean: {ds}/{mid}")
            elif len(clean[ds][mid]) != expected_samples:
                issues.append(
                    f"COUNT clean: {ds}/{mid} has {len(clean[ds][mid])}, "
                    f"expected {expected_samples}"
                )
            for atk in attacks:
                if mid not in attacked[ds][atk]:
                    issues.append(f"MISSING attacked: {ds}/{atk}/{mid}")
                elif len(attacked[ds][atk][mid]) != expected_samples:
                    issues.append(
                        f"COUNT attacked: {ds}/{atk}/{mid} has "
                        f"{len(attacked[ds][atk][mid])}, expected {expected_samples}"
                    )
    if issues:
        logger.warning(f"Validation: {len(issues)} issues")
        for i in issues[:20]:
            logger.warning(f"  {i}")
        if len(issues) > 20:
            logger.warning(f"  ... and {len(issues) - 20} more")
    else:
        logger.info(
            f"Validation passed: {len(all_models)} models x "
            f"{len(datasets)} datasets x {len(attacks)+1} conditions"
        )
    return issues
