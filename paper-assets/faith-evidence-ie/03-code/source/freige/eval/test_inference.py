"""Test set inference for DocRED - generates predictions + CodaLab submission.

Usage (from ./outputs
  python -m freige.eval.test_inference \
    --model_path ./outputs \
    --base_model ./outputs \
    --sft_adapter ./outputs \
    --data_path ./data/docred \
    --output_dir ./outputs/eval_results
    --no-quantize --batch_size 16 --max_new_tokens 1024
"""
import argparse
import json
import logging
import time
from pathlib import Path

import torch

from freige.eval.inference import (
    load_model_and_tokenizer,
    build_prompt,
    run_inference,
    evaluate,
    SYSTEM_PROMPT,
    NO_EVIDENCE_SYSTEM_PROMPT,
)
from freige.eval.evaluator import gold_from_docred
from freige.data.docred_processor import DocREDProcessor, SPLIT_FILENAMES, DOCRED_REL_INFO

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

REL_NAME_TO_CODE = {v.lower().strip(): k for k, v in DOCRED_REL_INFO.items()}


def prepare_test_data(data_dir, tokenizer, split="test", include_evidence=True, system_prompt=SYSTEM_PROMPT):
    """Build inference prompts from a test split."""
    processor = DocREDProcessor(data_dir=data_dir)
    split_file = Path(data_dir) / SPLIT_FILENAMES[split]
    with open(split_file) as f:
        raw_docs = json.load(f)

    eval_items = []
    for doc in raw_docs:
        doc_id = doc.get("title", "")
        sents = [processor._tokens_to_text(s) for s in doc["sents"]]
        numbered_sents = "\n".join(f"[{i}] {s}" for i, s in enumerate(sents))

        entity_list = set()
        for entity_mentions in doc["vertexSet"]:
            name = entity_mentions[0]["name"]
            entity_type = entity_mentions[0].get("type", "UNK")
            entity_list.add(f"{name} ({entity_type})")
        entity_str = ", ".join(sorted(entity_list))

        if include_evidence:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, tail entity, "
                "and the sentence IDs that serve as evidence. "
                "Output as a JSON list."
            )
        else:
            instruction = (
                "Extract all relation triples from the document. "
                "For each triple, provide the head entity, relation, and tail entity. "
                "Output as a JSON list."
            )

        input_text = f"Document:\n{numbered_sents}\n\nEntities: {entity_str}"
        prompt = build_prompt(tokenizer, instruction, input_text, system_prompt=system_prompt)
        eval_items.append({"doc_id": doc_id, "prompt": prompt})

    logger.info("Prepared %d test documents", len(eval_items))
    return eval_items, raw_docs


def build_entity_name_to_idx(doc):
    """Map entity name -> vertexSet index (case-insensitive)."""
    name_to_idx = {}
    for idx, entity_mentions in enumerate(doc["vertexSet"]):
        for mention in entity_mentions:
            name = mention["name"].lower().strip()
            if name not in name_to_idx:
                name_to_idx[name] = idx
    return name_to_idx


def to_codalab_format(predictions_by_doc, raw_docs):
    """Convert predictions to CodaLab submission format."""
    doc_map = {doc.get("title", ""): doc for doc in raw_docs}
    submission = {}
    stats = {"converted": 0, "skipped_rel": 0, "skipped_entity": 0}

    for doc_pred in predictions_by_doc:
        doc_id = doc_pred["doc_id"]
        raw_doc = doc_map.get(doc_id)
        if raw_doc is None:
            continue

        name_to_idx = build_entity_name_to_idx(raw_doc)
        doc_triples = []
        seen = set()

        for triple in doc_pred.get("parsed_triples", []):
            rel_name = triple.get("relation", "").lower().strip()
            rel_code = REL_NAME_TO_CODE.get(rel_name)
            if rel_code is None:
                stats["skipped_rel"] += 1
                continue

            h_idx = name_to_idx.get(triple.get("head", "").lower().strip())
            t_idx = name_to_idx.get(triple.get("tail", "").lower().strip())
            if h_idx is None or t_idx is None:
                stats["skipped_entity"] += 1
                continue

            dedup_key = (rel_code, h_idx, t_idx)
            if dedup_key in seen:
                continue
            seen.add(dedup_key)

            evidence = [e for e in triple.get("evidence", []) if isinstance(e, int)]
            doc_triples.append({
                "r": rel_code,
                "h": h_idx,
                "t": t_idx,
                "evidence": evidence,
            })
            stats["converted"] += 1

        submission[doc_id] = doc_triples

    return submission, stats


def main():
    parser = argparse.ArgumentParser(description="FREIGE test set inference + CodaLab submission")
    parser.add_argument("--model_path", required=True)
    parser.add_argument("--base_model", default="./outputs")
    parser.add_argument("--sft_adapter", default=None)
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--output_dir", required=True)
    parser.add_argument("--batch_size", type=int, default=16)
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--split", default="test")
    parser.add_argument("--no_evidence", action="store_true", default=False)
    parser.add_argument("--quantize", action=argparse.BooleanOptionalAction, default=True)
    args = parser.parse_args()

    torch.manual_seed(args.seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(args.seed)

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    adapter_config = Path(args.model_path) / "adapter_config.json"
    if adapter_config.exists():
        base_model_path = args.base_model
        adapter_path = args.model_path
        logger.info("Detected adapter at %s, base: %s", adapter_path, base_model_path)
    else:
        base_model_path = args.model_path
        adapter_path = None
        logger.info("Full model: %s", base_model_path)

    model, tokenizer = load_model_and_tokenizer(
        base_model_path, adapter_path, sft_adapter_path=args.sft_adapter,
        quantize=args.quantize,
    )

    sys_prompt = NO_EVIDENCE_SYSTEM_PROMPT if args.no_evidence else SYSTEM_PROMPT
    include_evi = not args.no_evidence
    eval_items, raw_docs = prepare_test_data(
        args.data_path, tokenizer, split=args.split,
        include_evidence=include_evi, system_prompt=sys_prompt,
    )

    t0 = time.time()
    raw_results = run_inference(model, tokenizer, eval_items, args.batch_size, args.max_new_tokens)
    elapsed = time.time() - t0
    logger.info("Inference: %.1fs (%.2f s/doc)", elapsed, elapsed / max(len(eval_items), 1))

    all_predictions = []
    raw_outputs_for_eval = []
    detailed = []
    for r in raw_results:
        doc_id = r["doc_id"]
        for triple in r["parsed_triples"]:
            all_predictions.append({
                "doc_id": doc_id,
                "head": triple["head"],
                "tail": triple["tail"],
                "relation": triple["relation"],
                "evidence": triple.get("evidence", []),
            })
        raw_outputs_for_eval.append({"doc_id": doc_id, "raw_text": r["raw_output"]})
        detailed.append({
            "doc_id": doc_id,
            "raw_output": r["raw_output"],
            "parsed_triples": r["parsed_triples"],
            "truncated": r["truncated"],
            "format_ok": r["format_ok"],
        })

    pred_path = output_dir / "predictions.json"
    with open(pred_path, "w") as f:
        json.dump(detailed, f, indent=2, ensure_ascii=False)
    logger.info("Predictions -> %s", pred_path)

    has_labels = any("labels" in doc and doc["labels"] for doc in raw_docs)

    if has_labels:
        gold = gold_from_docred(raw_docs)
        metrics = evaluate(all_predictions, gold, raw_outputs_for_eval, args.data_path, args.split)
    else:
        metrics = {"note": "test split has no labels - submit to CodaLab for evaluation"}

    submission, stats = to_codalab_format(detailed, raw_docs)
    codalab_path = output_dir / "codalab_submission.json"
    with open(codalab_path, "w") as f:
        json.dump(submission, f)
    logger.info("CodaLab submission -> %s", codalab_path)

    n_truncated = sum(1 for r in raw_results if r["truncated"])
    n_format_ok = sum(1 for r in raw_results if r["format_ok"])
    n_preds = len(all_predictions)

    summary = {
        "n_documents": len(raw_results),
        "n_predictions": n_preds,
        "n_truncated": n_truncated,
        "n_format_ok": n_format_ok,
        "format_ok_rate": n_format_ok / len(raw_results) if raw_results else 0,
        "inference_time_seconds": round(elapsed, 1),
        "codalab_stats": stats,
        "config": vars(args),
    }
    if has_labels:
        summary["metrics"] = metrics
    with open(output_dir / "test_summary.json", "w") as f:
        json.dump(summary, f, indent=2)

    print("\n" + "=" * 50)
    if has_labels:
        print(f"  F1:          {metrics['f1']:.4f}")
        print(f"  Ign-F1:      {metrics['ign_f1']:.4f}")
        print(f"  Evi-F1(DREEAM): {metrics.get('evi_f1_joint', 0):.4f}")
        print(f"  Evi-F1(TP):     {metrics['evi_f1']:.4f}")
        print(f"  EDCR:        {metrics.get('edcr', 0):.4f}")
    print(f"  Documents:   {len(raw_results)}")
    print(f"  Predictions: {n_preds}")
    print(f"  Format OK:   {n_format_ok}/{len(raw_results)}")
    print(f"  Truncated:   {n_truncated}/{len(raw_results)}")
    print(f"  CodaLab:     {stats['converted']} converted, "
          f"{stats['skipped_rel']} skipped (rel), "
          f"{stats['skipped_entity']} skipped (entity)")
    print(f"  Output:      {codalab_path}")
    print("=" * 50)


if __name__ == "__main__":
    main()
