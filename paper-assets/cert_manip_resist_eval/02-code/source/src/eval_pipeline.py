# Judge Evaluation Pipeline.
# Loads datasets, generates response pairs, collects judge scores.
# Output: scores[judge_id][sample_id] = {winner, score_a, score_b}

import json
import random
from pathlib import Path
from typing import Any, Dict, List, Tuple

from datasets import load_dataset
from tqdm import tqdm

from src.config import DATASET_REGISTRY, ExperimentConfig
from src.judge_service import JudgeService
from src.utils import save_results, setup_logging, set_seed

logger = setup_logging("eval_pipeline")


def load_eval_dataset(dataset_name: str, n_samples: int) -> List[Dict[str, Any]]:
    """Load and sample from a HuggingFace dataset."""
    hf_id, config_name, split, default_n = DATASET_REGISTRY[dataset_name]
    n = min(n_samples, default_n)
    ds = load_dataset(hf_id, config_name, split=split)
    indices = random.sample(range(len(ds)), min(n, len(ds)))
    samples = [ds[i] for i in indices]
    logger.info(f"Loaded {len(samples)} samples from {dataset_name}")
    return samples


def _format_mmlu_question(sample: Dict) -> str:
    choices = sample["choices"]
    q = sample["question"]
    options = "\n".join(f"  ({chr(65+i)}) {c}" for i, c in enumerate(choices))
    return f"{q}\n{options}"


def _format_arc_question(sample: Dict) -> str:
    choices = sample["choices"]
    q = sample["question"]
    labels = choices["label"]
    texts = choices["text"]
    options = "\n".join(f"  ({l}) {t}" for l, t in zip(labels, texts))
    return f"{q}\n{options}"


def _generate_good_response(sample: Dict, dataset_name: str) -> str:
    """Generate a correct response with explanation."""
    if dataset_name == "mmlu":
        answer_idx = sample["answer"]
        answer_letter = chr(65 + answer_idx)
        answer_text = sample["choices"][answer_idx]
        return (
            f"The correct answer is ({answer_letter}) {answer_text}. "
            f"This is because the question asks about a concept where "
            f"option {answer_letter} is the most accurate and complete choice "
            f"among the given alternatives."
        )
    else:  # arc_challenge
        answer_key = sample["answerKey"]
        labels = sample["choices"]["label"]
        texts = sample["choices"]["text"]
        idx = labels.index(answer_key)
        answer_text = texts[idx]
        return (
            f"The correct answer is ({answer_key}) {answer_text}. "
            f"This answer is correct because it accurately addresses "
            f"the scientific concept being tested in the question."
        )


def _generate_bad_response(sample: Dict, dataset_name: str) -> str:
    """Generate an incorrect response with plausible-sounding but wrong reasoning."""
    if dataset_name == "mmlu":
        answer_idx = sample["answer"]
        choices = sample["choices"]
        wrong_indices = [i for i in range(len(choices)) if i != answer_idx]
        wrong_idx = random.choice(wrong_indices)
        wrong_letter = chr(65 + wrong_idx)
        wrong_text = choices[wrong_idx]
        return (
            f"The answer is ({wrong_letter}) {wrong_text}. "
            f"While other options might seem plausible, this option "
            f"best captures the key aspect of the question."
        )
    else:  # arc_challenge
        answer_key = sample["answerKey"]
        labels = sample["choices"]["label"]
        texts = sample["choices"]["text"]
        wrong_labels = [l for l in labels if l != answer_key]
        wrong_label = random.choice(wrong_labels)
        wrong_idx = labels.index(wrong_label)
        wrong_text = texts[wrong_idx]
        return (
            f"The answer is ({wrong_label}) {wrong_text}. "
            f"This is the most scientifically accurate choice "
            f"given the context of the question."
        )


def generate_response_pairs(
    samples: List[Dict], dataset_name: str
) -> List[Dict[str, str]]:
    """Generate (question, good_response, bad_response) triples.
    Randomly assign good/bad to A/B positions to avoid position bias."""
    pairs = []
    for sample in samples:
        if dataset_name == "mmlu":
            question = _format_mmlu_question(sample)
        else:
            question = _format_arc_question(sample)

        good = _generate_good_response(sample, dataset_name)
        bad = _generate_bad_response(sample, dataset_name)

        # Randomly assign to A/B to control for position bias
        if random.random() < 0.5:
            pairs.append({
                "question": question,
                "response_a": good,
                "response_b": bad,
                "ground_truth_winner": "A",
            })
        else:
            pairs.append({
                "question": question,
                "response_a": bad,
                "response_b": good,
                "ground_truth_winner": "B",
            })
    return pairs


def run_evaluation(
    model_ids: List[str],
    pairs: List[Dict[str, str]],
    dataset_name: str,
) -> Dict[str, List[Dict[str, Any]]]:
    """Run all judges on all pairs. Loads/unloads each judge sequentially
    to avoid GPU memory conflicts when models share GPUs."""
    all_scores: Dict[str, List[Dict[str, Any]]] = {}

    items = [
        {"question": p["question"], "response_a": p["response_a"], "response_b": p["response_b"]}
        for p in pairs
    ]

    for model_id in model_ids:
        logger.info(f"Loading judge {model_id}...")
        judge = JudgeService(model_id)
        judge.load()

        logger.info(f"Scoring {len(pairs)} pairs ({dataset_name})")
        scores = judge.batch_score(items, mode="pairwise")

        for score, pair in zip(scores, pairs):
            score["ground_truth_winner"] = pair["ground_truth_winner"]
            score["dataset"] = dataset_name

        all_scores[model_id] = scores
        logger.info(f"  {model_id}: {len(scores)} scores collected")

        judge.unload()
        logger.info(f"  {model_id}: GPU memory released")

    return all_scores


def run_full_pipeline(
    model_ids: List[str],
    config: ExperimentConfig,
) -> Dict[str, Any]:
    """Run evaluation across all configured datasets.
    Each judge is loaded/unloaded sequentially to support GPU sharing."""
    set_seed(config.seed)
    all_results: Dict[str, Any] = {}

    for ds_name in config.datasets:
        logger.info(f"=== Dataset: {ds_name} ===")
        samples = load_eval_dataset(ds_name, config.n_samples)
        pairs = generate_response_pairs(samples, ds_name)
        scores = run_evaluation(model_ids, pairs, ds_name)
        all_results[ds_name] = {
            "scores": scores,
            "n_pairs": len(pairs),
            "pairs": pairs,
        }

    out_path = save_results(all_results, config.results_dir, tag="eval_pipeline")
    logger.info(f"Results saved to {out_path}")
    return all_results
