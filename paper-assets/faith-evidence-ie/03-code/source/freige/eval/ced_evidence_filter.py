"""CED Evidence Filtering: inference-time per-sentence NLI filtering of evidence citations.

Input: predictions.json (from inference.py) + dev.json (for document sentences)
Output: For each tau, filtered predictions + metrics (Evi-F1, EDCR, F1)
"""

import argparse
import json
import logging
import os
import sys
from pathlib import Path

import torch

# sys.path.insert(0, project_root)

from freige.rewards.ced_reward import CEDRewardModel, VERBALIZATION_TEMPLATES, verbalize_triple
from freige.data.docred_processor import DOCRED_REL_INFO
from freige.eval.evaluator import DocREDEvaluator, gold_from_docred

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

# Reverse map: human-readable relation name -> P-code (for better verbalization)
REL_NAME_TO_PCODE = {v.lower().strip(): k for k, v in DOCRED_REL_INFO.items()}


def load_predictions(pred_path):
    with open(pred_path) as f:
        return json.load(f)


def load_doc_sents(data_dir, split="dev"):
    """Load document sentences from DocRED JSON. Returns {title: [sent_str, ...]}"""
    path = Path(data_dir) / f"{split}.json"
    with open(path) as f:
        data = json.load(f)
    return {doc["title"]: [" ".join(s) for s in doc["sents"]] for doc in data}


def verbalize_for_nli(head, relation, tail):
    """Verbalize a triple for NLI. Maps human-readable relation back to P-code for templates."""
    pcode = REL_NAME_TO_PCODE.get(relation.lower().strip())
    if pcode:
        return verbalize_triple(head, pcode, tail)
    return verbalize_triple(head, relation, tail)


def filter_evidence_for_triple(triple, sents, ced_model, tau):
    """Score each evidence sentence independently and keep those >= tau."""
    evi_ids = triple.get("evidence", [])
    if not evi_ids:
        return triple

    valid_evi = [i for i in evi_ids if isinstance(i, int) and 0 <= i < len(sents)]
    if not valid_evi:
        return {**triple, "evidence": []}

    claim = verbalize_for_nli(triple["head"], triple["relation"], triple["tail"])
    premises = [sents[i] for i in valid_evi]
    hypotheses = [claim] * len(valid_evi)

    scores = ced_model.nli_entailment_prob(premises, hypotheses).tolist()

    kept_ids = [idx for idx, s in zip(valid_evi, scores) if s >= tau]

    if not kept_ids:
        # Keep the highest-scoring sentence as fallback
        best_idx = valid_evi[scores.index(max(scores))]
        kept_ids = [best_idx]

    return {**triple, "evidence": kept_ids}


def filter_all(predictions, doc_sents, ced_model, tau):
    """Filter evidence for all documents."""
    filtered = []
    n_total_evi = 0
    n_kept_evi = 0

    for doc_pred in predictions:
        doc_id = doc_pred.get("doc_id", "")
        sents = doc_sents.get(doc_id, [])

        if not sents:
            filtered.append(doc_pred)
            continue

        new_triples = []
        for triple in doc_pred.get("parsed_triples", []):
            n_total_evi += len(triple.get("evidence", []))
            new_triple = filter_evidence_for_triple(triple, sents, ced_model, tau)
            n_kept_evi += len(new_triple.get("evidence", []))
            new_triples.append(new_triple)

        filtered.append({**doc_pred, "parsed_triples": new_triples})

    logger.info(
        "tau=%.2f: %d/%d evidence sentences kept (%.1f%%)",
        tau, n_kept_evi, n_total_evi,
        100 * n_kept_evi / max(n_total_evi, 1)
    )
    return filtered


def evaluate_filtered(filtered_preds, gold, evaluator):
    """Flatten filtered predictions and compute metrics."""
    flat_preds = []
    for doc_pred in filtered_preds:
        doc_id = doc_pred["doc_id"]
        for triple in doc_pred.get("parsed_triples", []):
            flat_preds.append({
                "doc_id": doc_id,
                "head": triple["head"],
                "tail": triple["tail"],
                "relation": triple["relation"],
                "evidence": triple.get("evidence", []),
            })
    return evaluator.evaluate(flat_preds, gold)


def main():
    parser = argparse.ArgumentParser(description="CED Evidence Filtering")
    parser.add_argument("--predictions", required=True, help="Path to predictions.json")
    parser.add_argument("--data_dir", default="./data/docred")
    parser.add_argument("--nli_model", default="~/.cache/huggingface/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7")
    parser.add_argument("--nli_device", default="cuda:0")
    parser.add_argument("--taus", nargs="+", type=float, default=[0.3, 0.5, 0.7])
    parser.add_argument("--output_dir", required=True)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load data
    logger.info("Loading predictions from %s", args.predictions)
    predictions = load_predictions(args.predictions)
    logger.info("Loaded %d documents", len(predictions))

    logger.info("Loading document sentences from %s", args.data_dir)
    doc_sents = load_doc_sents(args.data_dir, "dev")
    logger.info("Loaded sentences for %d documents", len(doc_sents))

    # Load gold
    dev_path = Path(args.data_dir) / "dev.json"
    with open(dev_path) as f:
        dev_data = json.load(f)
    gold = gold_from_docred(dev_data)
    logger.info("Loaded %d gold triples", len(gold))

    # Build evaluator
    train_path = Path(args.data_dir) / "train_annotated.json"
    if train_path.exists():
        evaluator = DocREDEvaluator.from_train_file(str(train_path))
    else:
        evaluator = DocREDEvaluator()

    # Compute baseline metrics (unfiltered)
    logger.info("Computing baseline metrics (no filtering)...")
    baseline_metrics = evaluate_filtered(predictions, gold, evaluator)
    print("\n" + "=" * 60)
    print("BASELINE (no filtering)")
    print(f"  F1:      {baseline_metrics['f1']:.4f}")
    print(f"  Ign-F1:  {baseline_metrics['ign_f1']:.4f}")
    print(f"  Evi-F1:  {baseline_metrics['evi_f1']:.4f}")
    print(f"  EDCR:    {baseline_metrics.get('edcr', 0):.4f}")
    print("=" * 60)

    with open(output_dir / "metrics_baseline.json", "w") as f:
        json.dump(baseline_metrics, f, indent=2)

    # Load NLI model
    logger.info("Loading NLI model from %s", args.nli_model)
    ced_model = CEDRewardModel(model_name=args.nli_model, device=args.nli_device)

    # Filter for each tau
    all_results = {"baseline": baseline_metrics}
    for tau in args.taus:
        logger.info("Filtering with tau=%.2f...", tau)
        filtered = filter_all(predictions, doc_sents, ced_model, tau)

        # Save filtered predictions
        out_path = output_dir / f"filtered_tau{tau}.json"
        with open(out_path, "w") as f:
            json.dump(filtered, f, indent=2, ensure_ascii=False)

        # Compute metrics
        metrics = evaluate_filtered(filtered, gold, evaluator)
        all_results[f"tau={tau}"] = metrics

        print(f"\n{'=' * 60}")
        print(f"tau={tau}")
        print(f"  F1:      {metrics['f1']:.4f} (delta: {metrics['f1'] - baseline_metrics['f1']:+.4f})")
        print(f"  Ign-F1:  {metrics['ign_f1']:.4f} (delta: {metrics['ign_f1'] - baseline_metrics['ign_f1']:+.4f})")
        print(f"  Evi-F1:  {metrics['evi_f1']:.4f} (delta: {metrics['evi_f1'] - baseline_metrics['evi_f1']:+.4f})")
        print(f"  EDCR:    {metrics.get('edcr', 0):.4f} (delta: {metrics.get('edcr', 0) - baseline_metrics.get('edcr', 0):+.4f})")
        print(f"={'=' * 59}")

        with open(output_dir / f"metrics_tau{tau}.json", "w") as f:
            json.dump(metrics, f, indent=2)

    # Summary table
    with open(output_dir / "summary.json", "w") as f:
        json.dump(all_results, f, indent=2)

    print(f"\nAll results saved to {output_dir}/")


if __name__ == "__main__":
    main()
