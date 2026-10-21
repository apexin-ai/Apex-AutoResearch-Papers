"""DPO 偏好对构建: 从 RSFT 生成结果 + CED 分数构建 chosen/rejected 偏好对。

读取 rsft_generate 的 generations.jsonl 和 rsft_score_filter 的 rsft_scores.jsonl，
按 CED 分数排序后为每个文档构建偏好对供 DPO 训练使用。

输入:
  - generations.jsonl (rsft_generate 输出，含 prompt/output/gold_triples/sents)
  - rsft_scores.jsonl (rsft_score_filter 输出，含 ced_reward/f1_reward 等)
  或不提供 scores 文件，内部调用 CED 模型打分

输出 (保存到 --output_dir):
  - dpo_pairs.jsonl: 每行一个偏好对
    {"doc_id", "input", "chosen", "rejected", "chosen_score", "rejected_score", "margin"}
  - dpo_report.json: 统计报告

依赖: numpy, freige.rewards.ced_reward (仅在无 scores 文件时)

用法:
  # 使用预计算的分数
  python -m freige.training.dpo_data_builder \
      --input_dir ./outputs \
      --scores_path ./outputs \
      --output_dir ./outputs

  # 内部计算 CED 分数
  python -m freige.training.dpo_data_builder \
      --input_dir ./outputs \
      --output_dir ./outputs \
      --nli_model_path ./outputs
"""

import argparse
import json
import logging
from collections import defaultdict
from pathlib import Path

import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)


def _extract_user_content(prompt_text):
    """从 Qwen3 chat template 格式的 prompt 中提取 user 消息内容。"""
    user_start = prompt_text.find("<|im_start|>user\n")
    if user_start < 0:
        return prompt_text
    content_start = user_start + len("<|im_start|>user\n")
    user_end = prompt_text.find("<|im_end|>", content_start)
    if user_end < 0:
        return prompt_text[content_start:]
    return prompt_text[content_start:user_end]


def load_generations(input_dir):
    gen_path = Path(input_dir) / "generations.jsonl"
    records = []
    with open(gen_path) as f:
        for line in f:
            if line.strip():
                records.append(json.loads(line))
    logger.info("Loaded %d generation records from %s", len(records), gen_path)
    return records


def load_scores(scores_path):
    """加载预计算的 rsft_scores.jsonl，返回 (doc_id, generation_idx) -> score dict。"""
    scores = {}
    with open(scores_path) as f:
        for line in f:
            if line.strip():
                rec = json.loads(line)
                key = (rec["doc_id"], rec["generation_idx"])
                scores[key] = rec
    logger.info("Loaded %d score records from %s", len(scores), scores_path)
    return scores


def compute_scores_internal(records, nli_model_path, nli_device=None, tau=0.5):
    """无预计算分数时，内部调用 CED 模型打分。

    复用 rsft_score_filter 的打分逻辑，避免重复加载 NLI 模型。
    """
    from freige.rewards.ced_reward import CEDRewardModel
    from freige.training.rsft_score_filter import (
        compute_ced_reward_for_record,
        compute_f1_reward,
        compute_format_reward,
    )

    logger.info("Loading NLI model: %s", nli_model_path)
    ced_model = CEDRewardModel(model_name=nli_model_path, device=nli_device)

    scores = {}
    for rec in records:
        fmt_r = compute_format_reward(rec["parsed_triples"], rec["format_ok"])
        f1_r = compute_f1_reward(rec["parsed_triples"], rec["gold_triples"])
        ced_result = compute_ced_reward_for_record(rec, ced_model, tau=tau)

        key = (rec["doc_id"], rec["generation_idx"])
        scores[key] = {
            "doc_id": rec["doc_id"],
            "generation_idx": rec["generation_idx"],
            "format_reward": fmt_r,
            "f1_reward": f1_r,
            "ced_reward": ced_result["ced_reward"],
        }

    logger.info("Computed scores for %d records", len(scores))
    return scores


def build_preference_pairs(records, scores, args):
    """构建 DPO 偏好对。

    对每个 doc_id 的 N 个生成按 rank_by 分数排序，
    取 top-k 作为 chosen、bottom-k 作为 rejected，
    过滤掉 margin 低于 min_margin 的对。
    """
    doc_groups = defaultdict(list)
    for rec in records:
        key = (rec["doc_id"], rec["generation_idx"])
        if key not in scores:
            continue
        if args.require_format_ok and not rec.get("format_ok", False):
            continue

        score_rec = scores[key]
        doc_groups[rec["doc_id"]].append({
            "doc_id": rec["doc_id"],
            "generation_idx": rec["generation_idx"],
            "prompt": rec["prompt"],
            "output": rec["output"],
            "score": score_rec.get(args.rank_by, 0.0),
            "ced_reward": score_rec.get("ced_reward", 0.0),
            "f1_reward": score_rec.get("f1_reward", 0.0),
            "format_reward": score_rec.get("format_reward", 0.0),
        })

    pairs = []
    skipped_single = 0
    skipped_margin = 0

    for doc_id, gens in doc_groups.items():
        if len(gens) < 2:
            skipped_single += 1
            continue

        gens.sort(key=lambda x: x["score"], reverse=True)

        k = min(args.pair_k, len(gens) // 2)
        if k < 1:
            skipped_single += 1
            continue

        chosen_pool = gens[:k]
        rejected_pool = gens[-k:]
        user_input = _extract_user_content(gens[0]["prompt"])

        for chosen in chosen_pool:
            for rejected in rejected_pool:
                margin = chosen["score"] - rejected["score"]
                if margin < args.min_margin:
                    skipped_margin += 1
                    continue

                pairs.append({
                    "doc_id": doc_id,
                    "input": user_input,
                    "chosen": chosen["output"],
                    "rejected": rejected["output"],
                    "chosen_score": chosen["score"],
                    "rejected_score": rejected["score"],
                    "chosen_ced": chosen["ced_reward"],
                    "rejected_ced": rejected["ced_reward"],
                    "margin": margin,
                })

    logger.info(
        "Built %d pairs from %d docs (skipped: %d single-gen, %d below margin)",
        len(pairs), len(doc_groups), skipped_single, skipped_margin,
    )
    return pairs


def generate_report(pairs, total_records):
    if not pairs:
        return {
            "total_generation_records": total_records,
            "docs_with_pairs": 0,
            "total_pairs": 0,
        }

    margins = [p["margin"] for p in pairs]
    chosen_scores = [p["chosen_score"] for p in pairs]
    rejected_scores = [p["rejected_score"] for p in pairs]

    def _stats(vals):
        arr = np.array(vals)
        return {
            "mean": float(np.mean(arr)),
            "std": float(np.std(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "median": float(np.median(arr)),
        }

    return {
        "total_generation_records": total_records,
        "docs_with_pairs": len(set(p["doc_id"] for p in pairs)),
        "total_pairs": len(pairs),
        "margin_stats": _stats(margins),
        "chosen_score_stats": _stats(chosen_scores),
        "rejected_score_stats": _stats(rejected_scores),
    }


def main():
    parser = argparse.ArgumentParser(description="DPO Preference Pair Builder")
    parser.add_argument("--input_dir", type=str, required=True,
                        help="rsft_generate 输出目录（含 generations.jsonl）")
    parser.add_argument("--scores_path", type=str, default=None,
                        help="预计算分数文件 rsft_scores.jsonl（不提供则内部计算）")
    parser.add_argument("--output_dir", type=str, required=True,
                        help="输出目录")

    # 排序与配对
    parser.add_argument("--rank_by", type=str, default="ced_reward",
                        choices=["ced_reward", "f1_reward", "combined_score"],
                        help="偏好对排序依据 (default: ced_reward)")
    parser.add_argument("--pair_k", type=int, default=1,
                        help="每个 doc 取 top-k 和 bottom-k 构建对 (default: 1)")
    parser.add_argument("--min_margin", type=float, default=0.05,
                        help="最小分数差 (default: 0.05)")
    parser.add_argument("--require_format_ok", action="store_true", default=True,
                        help="仅使用 format_ok 的生成 (default: True)")
    parser.add_argument("--no_require_format_ok", dest="require_format_ok",
                        action="store_false")

    # CED 内部计算参数（仅在无 --scores_path 时使用）
    parser.add_argument("--nli_model_path", type=str,
                        default="cross-encoder/nli-deberta-v3-base",
                        help="NLI 模型路径")
    parser.add_argument("--nli_device", type=str, default=None)
    parser.add_argument("--tau", type=float, default=0.5)

    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Load generations
    records = load_generations(args.input_dir)

    # 2. Load or compute scores
    if args.scores_path:
        scores = load_scores(args.scores_path)
    else:
        logger.info("No scores_path provided, computing CED scores internally...")
        scores = compute_scores_internal(
            records, args.nli_model_path, args.nli_device, args.tau,
        )

    # 3. Build preference pairs
    pairs = build_preference_pairs(records, scores, args)

    # 4. Save
    pairs_path = output_dir / "dpo_pairs.jsonl"
    with open(pairs_path, "w") as f:
        for p in pairs:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    logger.info("DPO pairs -> %s (%d pairs)", pairs_path, len(pairs))

    # 5. Report
    report = generate_report(pairs, len(records))
    report["args"] = vars(args)
    report_path = output_dir / "dpo_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    logger.info("Report -> %s", report_path)

    # Console summary
    print("\n" + "=" * 60)
    print(f"  Generation records:  {report['total_generation_records']}")
    print(f"  Docs with pairs:     {report['docs_with_pairs']}")
    print(f"  Total DPO pairs:     {report['total_pairs']}")
    if pairs:
        ms = report["margin_stats"]
        print(f"  Margin:  mean={ms['mean']:.3f}  std={ms['std']:.3f}  "
              f"median={ms['median']:.3f}  [{ms['min']:.3f}, {ms['max']:.3f}]")
    print("=" * 60)


if __name__ == "__main__":
    main()
