"""Post-hoc BM25 evidence retrieval baseline for DocRED.

Given relation triples predicted by a no-evidence model, retrieves evidence
sentences from the source document using BM25. Compares with jointly-trained
models on joint F1 (relation + evidence evaluated together).

Usage:
    python post_hoc_retrieval.py \
        --predictions ./outputs/eval_results
        --dev_path ./data/docred/dev.json \
        --train_path ./data/docred/train_annotated.json \
        --output_dir ./outputs/eval_results
"""
import argparse
import json
import logging
import os
import sys
from collections import defaultdict
from pathlib import Path

from rank_bm25 import BM25Okapi

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from eval.evaluator import DocREDEvaluator, gold_from_docred

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def build_doc_index(dev_data: list[dict]) -> dict:
    """Build doc_id -> {sents, sents_text, vertex_set, entity_names} mapping."""
    doc_index = {}
    for doc in dev_data:
        title = doc["title"]
        sents = doc["sents"]
        sents_text = [" ".join(tokens) for tokens in sents]

        entity_names = defaultdict(set)
        for entity_group in doc["vertexSet"]:
            canonical = entity_group[0]["name"].lower().strip()
            for mention in entity_group:
                entity_names[canonical].add(mention["name"].lower().strip())

        doc_index[title] = {
            "sents": sents,
            "sents_text": sents_text,
            "sents_tokens": [s.lower().split() for s in sents_text],
            "entity_names": entity_names,
        }
    return doc_index


def get_entity_mention_tokens(doc_info: dict, entity_name: str) -> list[str]:
    """Get all mention surface forms for an entity, tokenized."""
    key = entity_name.lower().strip()
    names = doc_info["entity_names"].get(key, {key})
    tokens = []
    for name in names:
        tokens.extend(name.split())
    return tokens


def bm25_retrieve(
    doc_info: dict,
    head: str,
    tail: str,
    relation: str,
    top_k: int,
    query_mode: str = "entity_only",
) -> list[int]:
    """Retrieve top-K evidence sentence indices using BM25."""
    sents_tokens = doc_info["sents_tokens"]
    if not sents_tokens:
        return []

    head_tokens = get_entity_mention_tokens(doc_info, head)
    tail_tokens = get_entity_mention_tokens(doc_info, tail)

    if query_mode == "entity_only":
        query = head_tokens + tail_tokens
    else:
        rel_tokens = relation.lower().replace("_", " ").split()
        query = head_tokens + tail_tokens + rel_tokens

    if not query:
        return list(range(min(top_k, len(sents_tokens))))

    bm25 = BM25Okapi(sents_tokens)
    scores = bm25.get_scores(query)
    ranked = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)
    return sorted(ranked[:top_k])


def oracle_k_retrieve(
    doc_info: dict,
    head: str,
    tail: str,
    relation: str,
    gold_evidence: set[int],
    query_mode: str = "entity_only",
) -> list[int]:
    """Retrieve using oracle K (K = number of gold evidence sentences)."""
    k = len(gold_evidence) if gold_evidence else 2
    return bm25_retrieve(doc_info, head, tail, relation, k, query_mode)


def run_post_hoc(
    predictions_path: str,
    dev_path: str,
    train_path: str,
    output_dir: str,
    top_ks: list[int],
    query_modes: list[str],
):
    os.makedirs(output_dir, exist_ok=True)

    with open(predictions_path) as f:
        pred_data = json.load(f)
    with open(dev_path) as f:
        dev_data = json.load(f)

    logger.info("Building document index for %d documents", len(dev_data))
    doc_index = build_doc_index(dev_data)

    gold = gold_from_docred(dev_data)
    evaluator = DocREDEvaluator.from_train_file(train_path)

    gold_evi_map = defaultdict(set)
    for g in gold:
        key = (g["doc_id"], g["head"].lower().strip(), g["tail"].lower().strip(), g["relation"].lower().strip())
        gold_evi_map[key].update(g.get("evidence", []))

    all_predictions_flat = []
    for doc_pred in pred_data:
        doc_id = doc_pred["doc_id"]
        for triple in doc_pred.get("parsed_triples", []):
            all_predictions_flat.append({
                "doc_id": doc_id,
                "head": triple["head"],
                "tail": triple["tail"],
                "relation": triple["relation"],
            })

    logger.info("Total predicted triples: %d", len(all_predictions_flat))

    results_summary = {}

    for query_mode in query_modes:
        for top_k in top_ks:
            config_name = f"bm25_{query_mode}_k{top_k}"
            logger.info("Running config: %s", config_name)

            preds_with_evi = []
            n_missing_doc = 0
            for p in all_predictions_flat:
                doc_id = p["doc_id"]
                doc_info = doc_index.get(doc_id)
                if doc_info is None:
                    n_missing_doc += 1
                    preds_with_evi.append({**p, "evidence": []})
                    continue

                evi_indices = bm25_retrieve(
                    doc_info, p["head"], p["tail"], p["relation"],
                    top_k, query_mode,
                )
                preds_with_evi.append({**p, "evidence": evi_indices})

            if n_missing_doc > 0:
                logger.warning("Missing docs for %d predictions", n_missing_doc)

            metrics = evaluator.evaluate(preds_with_evi, gold)
            results_summary[config_name] = {
                "rel_f1": metrics["f1"],
                "ign_f1": metrics["ign_f1"],
                "evi_f1": metrics["evi_f1"],
                "evi_f1_joint": metrics["evi_f1_joint"],
                "edcr": metrics["edcr"],
                "evi_precision": metrics["evi_precision"],
                "evi_recall": metrics["evi_recall"],
                "evi_joint_precision": metrics["evi_joint_precision"],
                "evi_joint_recall": metrics["evi_joint_recall"],
            }
            logger.info("  %s: rel_f1=%.4f evi_f1_joint=%.4f edcr=%.4f",
                        config_name, metrics["f1"], metrics["evi_f1_joint"], metrics["edcr"])

            config_out = os.path.join(output_dir, f"{config_name}_metrics.json")
            with open(config_out, "w") as f:
                json.dump(metrics, f, indent=2)

        oracle_config = f"bm25_{query_mode}_oracle_k"
        logger.info("Running config: %s", oracle_config)

        preds_with_evi = []
        for p in all_predictions_flat:
            doc_id = p["doc_id"]
            doc_info = doc_index.get(doc_id)
            if doc_info is None:
                preds_with_evi.append({**p, "evidence": []})
                continue

            key = (doc_id, p["head"].lower().strip(), p["tail"].lower().strip(), p["relation"].lower().strip())
            gold_evi = gold_evi_map.get(key, set())
            evi_indices = oracle_k_retrieve(
                doc_info, p["head"], p["tail"], p["relation"],
                gold_evi, query_mode,
            )
            preds_with_evi.append({**p, "evidence": evi_indices})

        metrics = evaluator.evaluate(preds_with_evi, gold)
        results_summary[oracle_config] = {
            "rel_f1": metrics["f1"],
            "ign_f1": metrics["ign_f1"],
            "evi_f1": metrics["evi_f1"],
            "evi_f1_joint": metrics["evi_f1_joint"],
            "edcr": metrics["edcr"],
            "evi_precision": metrics["evi_precision"],
            "evi_recall": metrics["evi_recall"],
            "evi_joint_precision": metrics["evi_joint_precision"],
            "evi_joint_recall": metrics["evi_joint_recall"],
        }
        logger.info("  %s: rel_f1=%.4f evi_f1_joint=%.4f edcr=%.4f",
                    oracle_config, metrics["f1"], metrics["evi_f1_joint"], metrics["edcr"])

        config_out = os.path.join(output_dir, f"{oracle_config}_metrics.json")
        with open(config_out, "w") as f:
            json.dump(metrics, f, indent=2)

    comparison = {
        "post_hoc_results": results_summary,
        "reference_baselines": {
            "no_evidence_sft": {
                "rel_f1": 0.4876,
                "evi_f1_joint": 0.0,
                "note": "plan_014_no_evidence_eval_d076",
            },
            "sft_with_evidence": {
                "rel_f1": 0.4049,
                "evi_f1_joint": 0.3147,
                "edcr": 0.6982,
                "note": "sft_baseline_d076_reeval",
            },
            "rsft_ced_s43": {
                "rel_f1": 0.4601,
                "evi_f1_joint": 0.3605,
                "edcr": 0.6542,
                "note": "rsft_s43_dev_eval_preds",
            },
        },
    }

    summary_path = os.path.join(output_dir, "comparison_summary.json")
    with open(summary_path, "w") as f:
        json.dump(comparison, f, indent=2)
    logger.info("Summary saved to %s", summary_path)

    print("\n" + "=" * 80)
    print("POST-HOC BM25 RETRIEVAL RESULTS")
    print("=" * 80)
    header = f"{'Config':<35} {'Rel-F1':>8} {'Evi-F1j':>8} {'EDCR':>8} {'Evi-P':>8} {'Evi-R':>8}"
    print(header)
    print("-" * 80)
    for name, m in results_summary.items():
        print(f"{name:<35} {m['rel_f1']:>8.4f} {m['evi_f1_joint']:>8.4f} {m['edcr']:>8.4f} {m['evi_joint_precision']:>8.4f} {m['evi_joint_recall']:>8.4f}")
    print("-" * 80)
    print("REFERENCE BASELINES (jointly trained)")
    print(f"{'SFT (with evidence)':<35} {'0.4049':>8} {'0.3147':>8} {'0.6982':>8}")
    print(f"{'RSFT-CED s43':<35} {'0.4601':>8} {'0.3605':>8} {'0.6542':>8}")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Post-hoc BM25 evidence retrieval baseline")
    parser.add_argument("--predictions", required=True, help="Path to no-evidence predictions.json")
    parser.add_argument("--dev_path", required=True, help="Path to DocRED dev.json")
    parser.add_argument("--train_path", required=True, help="Path to DocRED train_annotated.json")
    parser.add_argument("--output_dir", default="./outputs/eval_results")
    parser.add_argument("--top_ks", nargs="+", type=int, default=[2, 3])
    parser.add_argument("--query_modes", nargs="+", default=["entity_only", "entity_relation"])
    args = parser.parse_args()

    run_post_hoc(
        predictions_path=args.predictions,
        dev_path=args.dev_path,
        train_path=args.train_path,
        output_dir=args.output_dir,
        top_ks=args.top_ks,
        query_modes=args.query_modes,
    )


if __name__ == "__main__":
    main()
