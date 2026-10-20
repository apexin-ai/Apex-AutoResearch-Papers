"""RSFT Step 2: CED 打分 + 筛选。

读取 rsft_generate.py 生成的 JSONL，对每个候选输出计算三种奖励:
  - format_reward: JSON 格式合规性
  - f1_reward: 与 gold triples 的 micro-F1
  - ced_reward: CED 对比证据判别奖励

按组合阈值筛选高质量样本，输出 SFT 训练兼容格式。

输入:
  - generations.jsonl (rsft_generate.py 的输出)

输出 (保存到 --output_path):
  - rsft_train.json: 筛选后的 SFT 训练数据
  - rsft_scores.jsonl: 带分数的完整记录（供分析）
  - rsft_report.json: 统计报告

依赖: transformers, torch, freige.rewards.ced_reward

用法:
  python -m freige.training.rsft_score_filter \
      --input_dir /root/autodl-tmp/rsft_generations \
      --output_path /root/autodl-tmp/rsft_filtered \
      --selection_strategy top_pct --top_pct 25 \
      --nli_model_path /root/autodl-tmp/models/nli-deberta-v3-base
"""

import argparse
import json
import logging
import os
from collections import defaultdict
from pathlib import Path

import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are an information extraction model. Given a document with numbered sentences "
    "and a list of entities, extract all relation triples. For each triple, provide the "
    "head entity, relation type, tail entity, and the sentence IDs that serve as evidence. "
    "Output as a JSON list."
)


# ---------------------------------------------------------------------------
# Reward functions — 复用 grpo_trainer 中的逻辑
# ---------------------------------------------------------------------------

def compute_format_reward(parsed_triples, format_ok):
    """格式奖励，复用 grpo_trainer.format_reward_fn 的逻辑。"""
    if not format_ok:
        return 0.0
    if not parsed_triples:
        return 0.1
    valid = 0
    for item in parsed_triples:
        if (isinstance(item, dict) and "head" in item
                and "relation" in item and "tail" in item
                and "evidence" in item
                and isinstance(item["evidence"], list)):
            valid += 1
    return valid / len(parsed_triples)


def compute_f1_reward(parsed_triples, gold_triples):
    """F1 奖励，复用 grpo_trainer.f1_reward_fn 的逻辑。"""
    gold_set = set()
    for g in gold_triples:
        gold_set.add((
            str(g.get("head") or "").lower().strip(),
            str(g.get("relation") or "").lower().strip(),
            str(g.get("tail") or "").lower().strip(),
        ))

    pred_set = set()
    for p in parsed_triples:
        if isinstance(p, dict):
            pred_set.add((
                str(p.get("head") or "").lower().strip(),
                str(p.get("relation") or "").lower().strip(),
                str(p.get("tail") or "").lower().strip(),
            ))

    if not gold_set:
        return 1.0 if not pred_set else 0.0

    tp = len(pred_set & gold_set)
    prec = tp / len(pred_set) if pred_set else 0.0
    rec = tp / len(gold_set) if gold_set else 0.0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) > 0 else 0.0
    return f1


def compute_ced_reward_for_record(record, ced_model, tau=0.5):
    """CED 奖励，复用 grpo_trainer.CEDRewardWrapper.__call__ 的逻辑。

    对一条记录中的所有 parsed_triples 计算平均 CED reward。
    """
    from freige.rewards.ced_reward import verbalize_triple

    parsed_triples = record["parsed_triples"]
    gold_triples = record["gold_triples"]
    sents = record["sents"]

    if not parsed_triples:
        return {"ced_reward": 0.0, "triple_details": []}

    # 构建 gold_map
    gold_map = {}
    for g in gold_triples:
        key = (
            str(g.get("head") or "").lower().strip(),
            str(g.get("relation") or "").lower().strip(),
            str(g.get("tail") or "").lower().strip(),
        )
        gold_map[key] = g

    # F1 gate: 至少一个预测 triple 匹配 gold
    has_gold_match = False
    for p in parsed_triples:
        if isinstance(p, dict):
            pk = (
                str(p.get("head") or "").lower().strip(),
                str(p.get("relation") or "").lower().strip(),
                str(p.get("tail") or "").lower().strip(),
            )
            if pk in gold_map:
                has_gold_match = True
                break
    if not has_gold_match:
        return {"ced_reward": 0.0, "triple_details": []}

    triple_details = []
    triple_rewards = []
    for p in parsed_triples:
        if not isinstance(p, dict):
            continue
        pred_evi_ids = p.get("evidence", [])
        if not isinstance(pred_evi_ids, list) or not pred_evi_ids:
            triple_rewards.append(0.0)
            triple_details.append({"reward": 0.0, "reason": "no_evidence"})
            continue

        claim = verbalize_triple(
            str(p.get("head") or ""),
            str(p.get("relation") or ""),
            str(p.get("tail") or ""),
        )
        cited_sents = [sents[idx] for idx in pred_evi_ids
                       if isinstance(idx, int) and 0 <= idx < len(sents)]
        if not cited_sents:
            triple_rewards.append(0.0)
            triple_details.append({"reward": 0.0, "reason": "invalid_evidence_ids"})
            continue

        key = (
            str(p.get("head") or "").lower().strip(),
            str(p.get("relation") or "").lower().strip(),
            str(p.get("tail") or "").lower().strip(),
        )
        matched_gold = gold_map.get(key, {})
        hard_neg_ids = matched_gold.get("hard_negative_sent_ids", [])
        hard_neg_sents = [sents[idx] for idx in hard_neg_ids
                          if isinstance(idx, int) and 0 <= idx < len(sents)]

        result = ced_model.compute_ced_reward(
            claim, cited_sents, hard_neg_sents, tau=tau,
        )
        triple_rewards.append(result["reward"])
        triple_details.append(result)

    mean_ced = sum(triple_rewards) / len(triple_rewards) if triple_rewards else 0.0
    return {"ced_reward": mean_ced, "triple_details": triple_details}


def load_generations(input_dir):
    """加载 generations.jsonl。"""
    input_path = Path(input_dir) / "generations.jsonl"
    records = []
    with open(input_path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    logger.info("Loaded %d generation records from %s", len(records), input_path)
    return records


def score_all_records(records, ced_model, tau=0.5):
    """对所有记录计算三种奖励分数。"""
    scored = []
    for i, rec in enumerate(records):
        format_reward = compute_format_reward(rec["parsed_triples"], rec.get("format_ok", False))
        f1_reward = compute_f1_reward(rec["parsed_triples"], rec["gold_triples"])
        ced_result = compute_ced_reward_for_record(rec, ced_model, tau=tau)

        scored_rec = {
            "doc_id": rec["doc_id"],
            "generation_idx": rec["generation_idx"],
            "output": rec["output"],
            "parsed_triples": rec["parsed_triples"],
            "format_ok": rec.get("format_ok", False),
            "gold_triples": rec["gold_triples"],
            "sents": rec["sents"],
            "prompt": rec.get("prompt", ""),
            "format_reward": format_reward,
            "f1_reward": f1_reward,
            "ced_reward": ced_result["ced_reward"],
            "combined_score": format_reward * 0.2 + f1_reward * 0.4 + ced_result["ced_reward"] * 0.4,
        }
        scored.append(scored_rec)

        if (i + 1) % 500 == 0:
            logger.info("Scored %d/%d records", i + 1, len(records))

    logger.info("Scoring complete: %d records", len(scored))
    return scored


def filter_records(scored_records, args):
    """根据策略筛选高质量样本。"""
    # 先按硬阈值过滤
    candidates = []
    for rec in scored_records:
        if rec["format_reward"] < args.format_threshold:
            continue
        if rec["f1_reward"] < args.f1_threshold:
            continue
        if rec["ced_reward"] < args.ced_threshold:
            continue
        candidates.append(rec)

    logger.info("After threshold filter: %d/%d (format>=%.2f, f1>=%.2f, ced>=%.2f)",
                len(candidates), len(scored_records),
                args.format_threshold, args.f1_threshold, args.ced_threshold)

    if args.selection_strategy == "threshold":
        return candidates

    if args.selection_strategy == "top_pct":
        # 按 doc_id 分组，每组取 top N%
        by_doc = defaultdict(list)
        for rec in candidates:
            by_doc[rec["doc_id"]].append(rec)

        selected = []
        for doc_id, doc_recs in by_doc.items():
            doc_recs.sort(key=lambda x: x["combined_score"], reverse=True)
            n_keep = max(1, int(len(doc_recs) * args.top_pct / 100))
            selected.extend(doc_recs[:n_keep])

        logger.info("After top_%d%%: %d records from %d documents",
                     args.top_pct, len(selected), len(by_doc))
        return selected

    if args.selection_strategy == "top_k":
        # 按 doc_id 分组，每组取 top-K
        by_doc = defaultdict(list)
        for rec in candidates:
            by_doc[rec["doc_id"]].append(rec)

        selected = []
        for doc_id, doc_recs in by_doc.items():
            doc_recs.sort(key=lambda x: x["combined_score"], reverse=True)
            selected.extend(doc_recs[:args.top_k])

        logger.info("After top_%d: %d records from %d documents",
                     args.top_k, len(selected), len(by_doc))
        return selected

    raise ValueError(f"Unknown selection strategy: {args.selection_strategy}")


def format_sft_training_data(selected_records, tokenizer_name=None):
    """将筛选后的记录转换为 SFT 训练格式。

    输出格式与 sft_trainer.prepare_dataset 一致:
    每条记录包含 "text" 字段，为完整的 chat template 格式文本。
    """
    sft_data = []
    for rec in selected_records:
        # 用模型的实际输出作为 assistant 回复（而非 gold output）
        # 这就是 RSFT 的核心: 用模型自己的高质量输出做 SFT
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _extract_user_content(rec["prompt"])},
            {"role": "assistant", "content": rec["output"]},
        ]

        sft_data.append({
            "messages": messages,
            "doc_id": rec["doc_id"],
            "generation_idx": rec["generation_idx"],
            "scores": {
                "format_reward": rec["format_reward"],
                "f1_reward": rec["f1_reward"],
                "ced_reward": rec["ced_reward"],
                "combined_score": rec["combined_score"],
            },
        })

    return sft_data


def _extract_user_content(prompt_text):
    """从完整 prompt 中提取 user 消息内容。

    prompt 是 apply_chat_template 的输出，包含 system/user 标记。
    直接用完整 prompt 中 user turn 的内容。
    """
    # Qwen3 chat template 格式:
    # <|im_start|>system\n...<|im_end|>\n<|im_start|>user\n...<|im_end|>\n<|im_start|>assistant\n
    user_start = prompt_text.find("<|im_start|>user\n")
    if user_start < 0:
        return prompt_text
    content_start = user_start + len("<|im_start|>user\n")
    user_end = prompt_text.find("<|im_end|>", content_start)
    if user_end < 0:
        return prompt_text[content_start:]
    return prompt_text[content_start:user_end]


def generate_report(scored_records, selected_records):
    """生成统计报告。"""
    total = len(scored_records)
    passed = len(selected_records)

    scores = {
        "format_reward": [r["format_reward"] for r in scored_records],
        "f1_reward": [r["f1_reward"] for r in scored_records],
        "ced_reward": [r["ced_reward"] for r in scored_records],
        "combined_score": [r["combined_score"] for r in scored_records],
    }

    report = {
        "total_records": total,
        "selected_records": passed,
        "filtered_records": total - passed,
        "selection_rate": passed / total if total else 0.0,
        "unique_docs_total": len(set(r["doc_id"] for r in scored_records)),
        "unique_docs_selected": len(set(r["doc_id"] for r in selected_records)),
    }

    for name, vals in scores.items():
        arr = np.array(vals)
        report[f"{name}_stats"] = {
            "mean": float(np.mean(arr)),
            "std": float(np.std(arr)),
            "min": float(np.min(arr)),
            "max": float(np.max(arr)),
            "median": float(np.median(arr)),
            "p25": float(np.percentile(arr, 25)),
            "p75": float(np.percentile(arr, 75)),
        }

    # 筛选后子集的统计
    if selected_records:
        sel_scores = {
            "format_reward": [r["format_reward"] for r in selected_records],
            "f1_reward": [r["f1_reward"] for r in selected_records],
            "ced_reward": [r["ced_reward"] for r in selected_records],
            "combined_score": [r["combined_score"] for r in selected_records],
        }
        report["selected_stats"] = {}
        for name, vals in sel_scores.items():
            arr = np.array(vals)
            report["selected_stats"][name] = {
                "mean": float(np.mean(arr)),
                "std": float(np.std(arr)),
                "min": float(np.min(arr)),
                "max": float(np.max(arr)),
            }

    return report


def main():
    parser = argparse.ArgumentParser(description="RSFT Step 2: CED Scoring & Filtering")
    parser.add_argument("--input_dir", type=str, required=True,
                        help="rsft_generate 输出目录（含 generations.jsonl）")
    parser.add_argument("--output_path", type=str, required=True,
                        help="筛选结果输出目录")
    parser.add_argument("--nli_model_path", type=str,
                        default="cross-encoder/nli-deberta-v3-base",
                        help="NLI 模型路径（用于 CED 打分）")
    parser.add_argument("--nli_device", type=str, default=None,
                        help="NLI 模型运行设备 (default: auto)")
    parser.add_argument("--tau", type=float, default=0.5,
                        help="CED tau 阈值 (default: 0.5)")

    # 筛选参数
    parser.add_argument("--format_threshold", type=float, default=0.5,
                        help="format_reward 最低阈值 (default: 0.5)")
    parser.add_argument("--f1_threshold", type=float, default=0.0,
                        help="f1_reward 最低阈值 (default: 0.0)")
    parser.add_argument("--ced_threshold", type=float, default=0.0,
                        help="ced_reward 最低阈值 (default: 0.0)")
    parser.add_argument("--selection_strategy", type=str, default="top_pct",
                        choices=["threshold", "top_k", "top_pct"],
                        help="筛选策略 (default: top_pct)")
    parser.add_argument("--top_k", type=int, default=2,
                        help="top_k 策略: 每个文档取 top-K (default: 2)")
    parser.add_argument("--top_pct", type=int, default=25,
                        help="top_pct 策略: 每个文档取 top N%% (default: 25)")
    args = parser.parse_args()

    output_dir = Path(args.output_path)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. 加载生成结果
    records = load_generations(args.input_dir)

    # 2. 加载 CED 模型并打分
    logger.info("Loading NLI model: %s", args.nli_model_path)
    from freige.rewards.ced_reward import CEDRewardModel
    ced_model = CEDRewardModel(model_name=args.nli_model_path, device=args.nli_device)

    scored = score_all_records(records, ced_model, tau=args.tau)

    # 保存带分数的完整记录
    scores_path = output_dir / "rsft_scores.jsonl"
    with open(scores_path, "w") as f:
        for rec in scored:
            # 不保存大字段以节省空间
            slim = {k: v for k, v in rec.items() if k not in ("prompt", "sents", "gold_triples")}
            f.write(json.dumps(slim, ensure_ascii=False) + "\n")
    logger.info("Scores → %s", scores_path)

    # 3. 筛选
    selected = filter_records(scored, args)

    # 4. 转换为 SFT 训练格式
    sft_data = format_sft_training_data(selected)
    train_path = output_dir / "rsft_train.jsonl"
    with open(train_path, "w") as f:
        for item in sft_data:
            user_msg = next(m["content"] for m in item["messages"] if m["role"] == "user")
            asst_msg = next(m["content"] for m in item["messages"] if m["role"] == "assistant")
            record = {
                "input": user_msg,
                "output": asst_msg,
                "ced_score": item["scores"]["ced_reward"],
                "doc_id": item.get("doc_id"),
                "generation_idx": item.get("generation_idx"),
                "scores": item["scores"],
            }
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
    logger.info("Training data → %s (%d samples)", train_path, len(sft_data))

    # 5. 统计报告
    report = generate_report(scored, selected)
    report["args"] = vars(args)
    report_path = output_dir / "rsft_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    logger.info("Report → %s", report_path)

    # 控制台摘要
    print("\n" + "=" * 60)
    print(f"  Total records:    {report['total_records']}")
    print(f"  Selected:         {report['selected_records']}")
    print(f"  Selection rate:   {report['selection_rate']:.1%}")
    print(f"  Unique docs:      {report['unique_docs_selected']}/{report['unique_docs_total']}")
    print("-" * 60)
    for name in ["format_reward", "f1_reward", "ced_reward", "combined_score"]:
        stats = report[f"{name}_stats"]
        print(f"  {name:20s}  mean={stats['mean']:.3f}  std={stats['std']:.3f}  "
              f"median={stats['median']:.3f}  [min={stats['min']:.3f}, max={stats['max']:.3f}]")
    print("=" * 60)


if __name__ == "__main__":
    main()
