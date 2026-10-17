"""Content preservation verification via BERTScore and NLI entailment.

Input:  counterfactuals.jsonl (with original_text, counterfactual_text, double_rewrite_text)
Output: verified.jsonl — adds bertscore_cf/dr, nli_cf/dr, passed_cf/dr fields
Deps:   bert-score, transformers, torch
"""

import argparse
import json
import logging
import os
import statistics

logger = logging.getLogger(__name__)

NLI_THRESHOLD_MVP = 0.90
NLI_THRESHOLD_FULL = 0.95


def compute_bertscore_batch(
    references: list[str], candidates: list[str], batch_size: int = 16, device: str = "cuda",
    model_type: str = "microsoft/deberta-xlarge-mnli", num_layers: int | None = None,
) -> list[float]:
    """Returns F1 BERTScore for each (reference, candidate) pair."""
    from bert_score import score as bert_score

    kwargs = dict(
        model_type=model_type,
        batch_size=batch_size,
        device=device,
        verbose=False,
    )
    if num_layers is not None:
        kwargs["num_layers"] = num_layers
    _, _, f1 = bert_score(candidates, references, **kwargs)
    return f1.tolist()


def compute_nli_batch(
    nli_pipe,
    texts_a: list[str],
    texts_b: list[str],
    batch_size: int = 16,
    modes: list[str] | None = None,
) -> list[float]:
    """NLI entailment scoring with per-record direction control.

    modes: per-record "both" (bidirectional min), "forward" (a→b only),
           or "backward" (b→a only). Default: all "both".
    """
    if modes is None:
        modes = ["both"] * len(texts_a)

    forward_inputs = [{"text": a, "text_pair": b} for a, b in zip(texts_a, texts_b)]
    backward_inputs = [{"text": b, "text_pair": a} for a, b in zip(texts_a, texts_b)]

    def _entailment_scores(inputs: list[dict]) -> list[float]:
        scores = []
        for i in range(0, len(inputs), batch_size):
            batch = inputs[i : i + batch_size]
            results = nli_pipe(batch, top_k=None, tokenizer_kwargs={"truncation": True, "padding": True, "max_length": 512})
            for result in results:
                label_scores = {r["label"].lower(): r["score"] for r in result}
                scores.append(label_scores.get("entailment", 0.0))
        return scores

    fwd = _entailment_scores(forward_inputs)
    bwd = _entailment_scores(backward_inputs)
    return [
        f if m == "forward" else b if m == "backward" else min(f, b)
        for f, b, m in zip(fwd, bwd, modes)
    ]


def print_summary(records: list[dict]):
    """Print aggregate verification statistics."""
    for suffix, label in [("cf", "Original vs Counterfactual"), ("dr", "Original vs Double-Rewrite")]:
        bs_key = f"bertscore_{suffix}"
        nli_key = f"nli_{suffix}"
        pass_key = f"passed_{suffix}"

        bs_vals = [r[bs_key] for r in records if r[bs_key] is not None]
        nli_vals = [r[nli_key] for r in records if r[nli_key] is not None]
        pass_vals = [r[pass_key] for r in records]

        n_passed = sum(pass_vals)
        n_total = len(pass_vals)

        print(f"\n{'='*60}")
        print(f"  {label}")
        print(f"{'='*60}")
        if bs_vals:
            print(f"  BERTScore  — mean: {statistics.mean(bs_vals):.4f}, std: {statistics.stdev(bs_vals) if len(bs_vals) > 1 else 0:.4f}")
        if nli_vals:
            print(f"  NLI        — mean: {statistics.mean(nli_vals):.4f}, std: {statistics.stdev(nli_vals) if len(nli_vals) > 1 else 0:.4f}")
        print(f"  Passed     — {n_passed}/{n_total} ({100*n_passed/n_total:.1f}%)")
    print(f"\n  Note: NLI threshold {NLI_THRESHOLD_MVP} is relaxed for MVP; full pipeline uses {NLI_THRESHOLD_FULL}.")


def main():
    parser = argparse.ArgumentParser(description="Verify content preservation of counterfactuals")
    parser.add_argument("--input-file", required=True)
    parser.add_argument("--output-file", required=True)
    parser.add_argument("--bertscore-threshold", type=float, default=0.92)
    parser.add_argument("--bertscore-model", default="microsoft/deberta-xlarge-mnli",
                        help="BERTScore model name or local path")
    parser.add_argument("--bertscore-num-layers", type=int, default=None,
                        help="Override num_layers for BERTScore (required for local model paths)")
    parser.add_argument("--nli-model", default="cross-encoder/nli-deberta-v3-large",
                        help="NLI model name or local path")
    parser.add_argument("--nli-threshold", type=float, default=NLI_THRESHOLD_MVP,
                        help=f"NLI entailment threshold (MVP={NLI_THRESHOLD_MVP}, full={NLI_THRESHOLD_FULL})")
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--device", default=None, help="cuda or cpu (auto-detect if omitted)")
    parser.add_argument("--axis", default="formality", choices=["formality", "verbosity", "tone", "register"],
                        help="Style axis — verbosity uses direction-aware NLI (default: formality)")
    args = parser.parse_args()

    if args.device is None:
        import torch
        args.device = "cuda" if torch.cuda.is_available() else "cpu"

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    with open(args.input_file) as f:
        records = [json.loads(line) for line in f if line.strip()]
    logger.info("Loaded %d records", len(records))

    originals = [r["original_text"] for r in records]
    counterfactuals = [r["counterfactual_text"] for r in records]
    double_rewrites = [r["double_rewrite_text"] for r in records]

    # BERTScore
    logger.info("Computing BERTScore (original vs counterfactual)...")
    bs_cf = compute_bertscore_batch(originals, counterfactuals, args.batch_size, args.device, args.bertscore_model, args.bertscore_num_layers)
    logger.info("Computing BERTScore (original vs double_rewrite)...")
    bs_dr = compute_bertscore_batch(originals, double_rewrites, args.batch_size, args.device, args.bertscore_model, args.bertscore_num_layers)

    # NLI
    logger.info("Loading NLI model...")
    from transformers import pipeline

    nli_pipe = pipeline(
        "text-classification",
        model=args.nli_model,
        device=0 if args.device == "cuda" else -1,
    )

    # Direction-aware NLI for information-changing axes (verbosity)
    cf_modes = None
    if args.axis == "verbosity":
        field = "original_verbosity"
        cf_modes = [
            "forward" if rec.get(field) == "verbose" else "backward"
            for rec in records
        ]
        n_fwd = sum(1 for m in cf_modes if m == "forward")
        logger.info("Direction-aware NLI: %d forward (compression), %d backward (expansion)",
                     n_fwd, len(cf_modes) - n_fwd)

    logger.info("Computing NLI (original vs counterfactual)...")
    nli_cf = compute_nli_batch(nli_pipe, originals, counterfactuals, args.batch_size, modes=cf_modes)
    logger.info("Computing NLI (original vs double_rewrite)...")
    nli_dr = compute_nli_batch(nli_pipe, originals, double_rewrites, args.batch_size)

    # Annotate
    for i, rec in enumerate(records):
        rec["bertscore_cf"] = bs_cf[i]
        rec["bertscore_dr"] = bs_dr[i]
        rec["nli_cf"] = nli_cf[i]
        rec["nli_dr"] = nli_dr[i]
        rec["nli_mode_cf"] = cf_modes[i] if cf_modes else "both"
        if args.axis == "verbosity":
            rec["passed_cf"] = nli_cf[i] >= args.nli_threshold
            rec["passed_dr"] = nli_dr[i] >= args.nli_threshold
        else:
            rec["passed_cf"] = (bs_cf[i] >= args.bertscore_threshold) and (nli_cf[i] >= args.nli_threshold)
            rec["passed_dr"] = (bs_dr[i] >= args.bertscore_threshold) and (nli_dr[i] >= args.nli_threshold)

    os.makedirs(os.path.dirname(args.output_file) or ".", exist_ok=True)
    with open(args.output_file, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")
    logger.info("Wrote %d records to %s", len(records), args.output_file)

    print_summary(records)


if __name__ == "__main__":
    main()
