"""MVP-1: CED 信号可行性离线验证。"""

import argparse
import json
import logging
import re
import sys
from pathlib import Path

import numpy as np
from scipy import stats

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

_TOKENIZE_RE = re.compile(r"\w+")


def _tokenize(text: str) -> set[str]:
    return set(_TOKENIZE_RE.findall(text.lower()))


def _token_jaccard(text_a: str, text_b: str) -> float:
    tokens_a = _tokenize(text_a)
    tokens_b = _tokenize(text_b)
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def run_validation(
    data_dir: str = None,
    split: str = "dev",
    nli_model: str = "cross-encoder/nli-deberta-v3-base",
    tau: float = 0.5,
    batch_size: int = 32,
    output_dir: str = ".",
    max_samples: int = 0,
):
    from freige.data.docred_processor import DocREDProcessor
    from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple

    processor = DocREDProcessor(data_dir=data_dir)
    samples = processor.process(split)
    logger.info("Total relation samples: %d", len(samples))

    samples_with_negs = [s for s in samples if s.hard_negative_sent_ids]
    logger.info(
        "Samples with hard negatives: %d (%.1f%%)",
        len(samples_with_negs),
        len(samples_with_negs) / len(samples) * 100 if samples else 0,
    )

    if max_samples > 0:
        samples_with_negs = samples_with_negs[:max_samples]
        logger.info("Using first %d samples", len(samples_with_negs))

    reward_model = CEDRewardModel(model_name=nli_model)

    claims = []
    evidence_lists = []
    negative_lists = []

    for s in samples_with_negs:
        claim = verbalize_triple(s.head.name, s.relation, s.tail.name)
        evidence_sents = [s.sents[i] for i in s.evidence_sent_ids if i < len(s.sents)]
        negative_sents = [s.sents[i] for i in s.hard_negative_sent_ids if i < len(s.sents)]
        claims.append(claim)
        evidence_lists.append(evidence_sents)
        negative_lists.append(negative_sents)

    logger.info("Computing CED rewards for %d samples...", len(claims))

    all_results = []
    for start in range(0, len(claims), batch_size):
        end = min(start + batch_size, len(claims))
        batch_results = reward_model.compute_ced_reward_batch(
            claims[start:end],
            evidence_lists[start:end],
            negative_lists[start:end],
            tau=tau,
        )
        all_results.extend(batch_results)
        if (start // batch_size) % 10 == 0:
            logger.info("  Processed %d / %d", end, len(claims))

    margins = np.array([r["margin"] for r in all_results])
    p_pos_arr = np.array([r["p_pos"] for r in all_results])
    p_neg_arr = np.array([r["p_neg"] for r in all_results])
    rewards = np.array([r["reward"] for r in all_results])

    jaccard_pos_arr = np.zeros(len(claims))
    jaccard_neg_arr = np.zeros(len(claims))
    for i in range(len(claims)):
        evi_concat = " ".join(evidence_lists[i])
        jaccard_pos_arr[i] = _token_jaccard(claims[i], evi_concat)
        if negative_lists[i]:
            jaccard_neg_arr[i] = max(
                _token_jaccard(claims[i], neg) for neg in negative_lists[i]
            )
    jaccard_diff = jaccard_pos_arr - jaccard_neg_arr

    pearson_r, pearson_p = stats.pearsonr(margins, jaccard_diff)

    discrimination_acc = np.mean(margins > 0)
    mean_margin = np.mean(margins)
    median_margin = np.median(margins)
    std_margin = np.std(margins)

    pass_margin = mean_margin > 0.1
    pass_acc = discrimination_acc > 0.70
    pass_lexical = abs(pearson_r) < 0.7

    report_lines = [
        "=" * 60,
        "MVP-1: CED Signal Validation Report",
        "=" * 60,
        f"Split: {split}",
        f"Total relation samples: {len(samples)}",
        f"Samples with hard negatives: {len(samples_with_negs)}",
        f"NLI model: {nli_model}",
        f"Tau: {tau}",
        "",
        "--- p_pos (gold evidence -> claim) ---",
        f"  Mean:   {np.mean(p_pos_arr):.4f}",
        f"  Median: {np.median(p_pos_arr):.4f}",
        f"  Std:    {np.std(p_pos_arr):.4f}",
        f"  > tau:  {np.mean(p_pos_arr > tau) * 100:.1f}%",
        "",
        "--- p_neg (hard negative -> claim) ---",
        f"  Mean:   {np.mean(p_neg_arr):.4f}",
        f"  Median: {np.median(p_neg_arr):.4f}",
        f"  Std:    {np.std(p_neg_arr):.4f}",
        "",
        "--- CED Margin (p_pos - p_neg) ---",
        f"  Mean:   {mean_margin:.4f}  {'PASS' if pass_margin else 'FAIL'} (threshold: > 0.1)",
        f"  Median: {median_margin:.4f}",
        f"  Std:    {std_margin:.4f}",
        f"  Min:    {np.min(margins):.4f}",
        f"  Max:    {np.max(margins):.4f}",
        "",
        f"Discrimination accuracy (p_pos > p_neg): "
        f"{discrimination_acc * 100:.1f}%  {'PASS' if pass_acc else 'FAIL'} (threshold: > 70%)",
        "",
        "--- CED Reward ---",
        f"  Mean:   {np.mean(rewards):.4f}",
        f"  Non-zero: {np.mean(rewards > 0) * 100:.1f}%",
        "",
        "--- Lexical Overlap Diagnostics ---",
        f"  Token Jaccard (claim vs gold evidence):",
        f"    Mean:   {np.mean(jaccard_pos_arr):.4f}",
        f"    Median: {np.median(jaccard_pos_arr):.4f}",
        f"  Token Jaccard (claim vs hard negative):",
        f"    Mean:   {np.mean(jaccard_neg_arr):.4f}",
        f"    Median: {np.median(jaccard_neg_arr):.4f}",
        f"  Jaccard diff (pos - neg):",
        f"    Mean:   {np.mean(jaccard_diff):.4f}",
        f"    Median: {np.median(jaccard_diff):.4f}",
        f"  Pearson r(CED margin, Jaccard diff): "
        f"{pearson_r:.4f} (p={pearson_p:.2e})  "
        f"{'PASS' if pass_lexical else 'FAIL'} (threshold: |r| < 0.7)",
        "",
        "=" * 60,
        f"MVP-1 VERDICT: {'PASS' if (pass_margin and pass_acc and pass_lexical) else 'FAIL'}",
        "=" * 60,
    ]

    report = "\n".join(report_lines)
    print(report)

    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)

    report_path = out / "ced_signal_validation_report.txt"
    with open(report_path, "w") as f:
        f.write(report)
    logger.info("Report saved to %s", report_path)

    detail_path = out / "ced_signal_validation_detail.json"
    detail_data = []
    for i, s in enumerate(samples_with_negs):
        detail_data.append({
            "doc_id": s.doc_id,
            "head": s.head.name,
            "tail": s.tail.name,
            "relation": s.relation,
            "relation_name": s.relation_name,
            "claim": claims[i],
            "n_evidence_sents": len(s.evidence_sent_ids),
            "n_hard_negatives": len(s.hard_negative_sent_ids),
            **all_results[i],
            "jaccard_pos": float(jaccard_pos_arr[i]),
            "jaccard_neg": float(jaccard_neg_arr[i]),
            "jaccard_diff": float(jaccard_diff[i]),
        })
    with open(detail_path, "w") as f:
        json.dump(detail_data, f, ensure_ascii=False, indent=2)
    logger.info("Detail saved to %s", detail_path)

    return {
        "pass": bool(pass_margin and pass_acc and pass_lexical),
        "mean_margin": float(mean_margin),
        "discrimination_accuracy": float(discrimination_acc),
        "mean_p_pos": float(np.mean(p_pos_arr)),
        "mean_p_neg": float(np.mean(p_neg_arr)),
        "mean_reward": float(np.mean(rewards)),
        "pearson_r_margin_jaccard": float(pearson_r),
        "n_samples": len(all_results),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MVP-1: CED signal validation")
    parser.add_argument("--data_dir", type=str, default=None)
    parser.add_argument("--split", type=str, default="dev")
    parser.add_argument("--nli_model", type=str, default="cross-encoder/nli-deberta-v3-base")
    parser.add_argument("--tau", type=float, default=0.5)
    parser.add_argument("--batch_size", type=int, default=32)
    parser.add_argument("--output_dir", type=str, default="./mvp1_results")
    parser.add_argument("--max_samples", type=int, default=0)
    args = parser.parse_args()

    results = run_validation(
        data_dir=args.data_dir,
        split=args.split,
        nli_model=args.nli_model,
        tau=args.tau,
        batch_size=args.batch_size,
        output_dir=args.output_dir,
        max_samples=args.max_samples,
    )

    print(f"\nResults JSON: {json.dumps(results, indent=2)}")
    sys.exit(0 if results["pass"] else 1)
