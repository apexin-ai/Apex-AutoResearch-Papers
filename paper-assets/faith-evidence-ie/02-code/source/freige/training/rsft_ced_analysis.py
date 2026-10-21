"""D032: RSFT CED Diversity 诊断脚本。
分析 RSFT 候选的 CED score 方差，判断 rejection sampling 是否可行。
"""
import json
import sys
import time
from collections import defaultdict
from pathlib import Path

import numpy as np
import torch

# sys.path.insert(0, project_root)

from freige.rewards.ced_reward import CEDRewardModel, verbalize_triple


def load_generations(input_dir):
    path = Path(input_dir) / "generations.jsonl"
    records = []
    with open(path) as f:
        for line in f:
            records.append(json.loads(line))
    return records


def compute_ced_for_record(record, ced_model, tau=0.5):
    """计算单条记录的 CED reward（复用 rsft_score_filter 逻辑）。"""
    parsed_triples = record.get("parsed_triples", [])
    gold_triples = record.get("gold_triples", [])
    sents = record.get("sents", [])

    if not parsed_triples:
        return {"ced_reward": 0.0, "evidence_ids": set(), "n_matched": 0}

    gold_map = {}
    for g in gold_triples:
        key = (
            str(g.get("head") or "").lower().strip(),
            str(g.get("relation") or "").lower().strip(),
            str(g.get("tail") or "").lower().strip(),
        )
        gold_map[key] = g

    matched_rewards = []
    all_evidence_ids = set()

    for p in parsed_triples:
        if not isinstance(p, dict):
            continue
        pk = (
            str(p.get("head") or "").lower().strip(),
            str(p.get("relation") or "").lower().strip(),
            str(p.get("tail") or "").lower().strip(),
        )
        if pk not in gold_map:
            continue

        gold = gold_map[pk]
        pred_ev_ids = p.get("evidence", [])
        if not isinstance(pred_ev_ids, list):
            continue

        # 收集 evidence IDs
        valid_ev_ids = [i for i in pred_ev_ids if isinstance(i, int) and 0 <= i < len(sents)]
        all_evidence_ids.update(valid_ev_ids)

        cited_sents = [sents[i] for i in valid_ev_ids]
        if not cited_sents:
            matched_rewards.append(0.0)
            continue

        hard_neg_ids = gold.get("hard_negative_sent_ids", [])
        hard_neg_sents = [sents[i] for i in hard_neg_ids if isinstance(i, int) and 0 <= i < len(sents)]

        claim = verbalize_triple(str(p.get("head", "")), str(p.get("relation", "")), str(p.get("tail", "")))
        result = ced_model.compute_ced_reward(claim, cited_sents, hard_neg_sents, tau=tau)
        matched_rewards.append(result["reward"])

    if not matched_rewards:
        return {"ced_reward": 0.0, "evidence_ids": all_evidence_ids, "n_matched": 0}

    return {
        "ced_reward": float(np.mean(matched_rewards)),
        "evidence_ids": all_evidence_ids,
        "n_matched": len(matched_rewards),
    }


def main():
    import os
    os.environ["HF_HOME"] = "~/.cache/huggingface"

    input_dir = "./outputs"

    print("Loading generations...")
    records = load_generations(input_dir)
    print(f"Total records: {len(records)}")

    # 按 doc_id 分组
    doc_groups = defaultdict(list)
    for rec in records:
        doc_groups[rec["doc_id"]].append(rec)

    n_docs = len(doc_groups)
    group_sizes = [len(v) for v in doc_groups.values()]
    print(f"Unique docs: {n_docs}, candidates per doc: min={min(group_sizes)} max={max(group_sizes)} mean={np.mean(group_sizes):.1f}")

    print("Loading NLI model on cuda:2...")
    ced_model = CEDRewardModel(model_name="~/.cache/huggingface/hub/models--cross-encoder--nli-deberta-v3-base/snapshots/6c749ce3425cd33b46d187e45b92bbf96ee12ec7", device="cuda:0")
    print("Model loaded.")

    # Scoring
    doc_ced_scores = {}
    doc_evidence_sets = {}
    t0 = time.time()

    for i, (doc_id, group) in enumerate(doc_groups.items()):
        scores = []
        ev_sets = []
        for rec in group:
            result = compute_ced_for_record(rec, ced_model)
            scores.append(result["ced_reward"])
            ev_sets.append(result["evidence_ids"])
        doc_ced_scores[doc_id] = scores
        doc_evidence_sets[doc_id] = ev_sets

        if (i + 1) % 20 == 0 or i == 0:
            elapsed = time.time() - t0
            eta = elapsed / (i + 1) * (n_docs - i - 1)
            print(f"  [{i+1}/{n_docs}] elapsed={elapsed:.1f}s eta={eta:.1f}s")

        # 快速报告：前 20 个 doc
        if i + 1 == 20:
            print("\n=== 快速报告 (前 20 docs) ===")
            _report(doc_ced_scores, doc_evidence_sets, "quick")
            print("=" * 50)
            print("继续处理剩余文档...\n")

    # 最终报告
    print(f"\nTotal scoring time: {time.time() - t0:.1f}s")
    print("\n" + "=" * 60)
    _report(doc_ced_scores, doc_evidence_sets, "full")
    print("=" * 60)


def _report(doc_ced_scores, doc_evidence_sets, tag):
    n_docs = len(doc_ced_scores)

    # Per-doc statistics
    doc_means = []
    doc_stds = []
    doc_gaps_1 = []  # top1 - bottom1
    doc_gaps_2 = []  # mean(top2) - mean(bottom2)
    all_scores = []

    for doc_id, scores in doc_ced_scores.items():
        arr = np.array(scores)
        all_scores.extend(scores)
        doc_means.append(arr.mean())
        doc_stds.append(arr.std())

        sorted_s = np.sort(arr)
        doc_gaps_1.append(sorted_s[-1] - sorted_s[0])
        if len(sorted_s) >= 4:
            doc_gaps_2.append(sorted_s[-2:].mean() - sorted_s[:2].mean())
        else:
            doc_gaps_2.append(sorted_s[-1] - sorted_s[0])

    # Evidence overlap
    overlap_rates = []
    for doc_id, ev_sets in doc_evidence_sets.items():
        non_empty = [s for s in ev_sets if s]
        if len(non_empty) < 2:
            continue
        pairwise = []
        for a_i in range(len(non_empty)):
            for b_i in range(a_i + 1, len(non_empty)):
                a, b = non_empty[a_i], non_empty[b_i]
                if a or b:
                    jaccard = len(a & b) / len(a | b) if (a | b) else 1.0
                    pairwise.append(jaccard)
        if pairwise:
            overlap_rates.append(np.mean(pairwise))

    n_cand = len(all_scores) / n_docs if n_docs > 0 else 0

    print(f"== D032 CED Scoring 诊断结果 ({tag}) ==")
    print(f"分析 doc 数: {n_docs}")
    print(f"每 doc 候选数: {n_cand:.0f}")
    print()
    print("CED Score 分布:")
    print(f"- 全局 mean: {np.mean(all_scores):.4f}")
    print(f"- 全局 std: {np.std(all_scores):.4f}")
    print(f"- 跨文档 std 均值 (mean_std): {np.mean(doc_stds):.4f}")
    print(f"- 跨文档 std 中位数: {np.median(doc_stds):.4f}")
    print(f"- top1-bottom1 gap 均值: {np.mean(doc_gaps_1):.4f}")
    print(f"- top2-bottom2 gap 均值: {np.mean(doc_gaps_2):.4f}")
    print()
    print("Evidence 多样性:")
    if overlap_rates:
        print(f"- sentence_ids Jaccard overlap rate: {np.mean(overlap_rates):.4f} (mean), {np.median(overlap_rates):.4f} (median)")
    else:
        print("- 无足够数据计算 overlap")
    print()

    # Score 分布直方图
    arr_all = np.array(all_scores)
    print("CED Score 分位数:")
    for pct in [0, 10, 25, 50, 75, 90, 100]:
        print(f"  P{pct:3d}: {np.percentile(arr_all, pct):.4f}")
    print()

    # 决策
    mean_std = np.mean(doc_stds)
    mean_gap_2 = np.mean(doc_gaps_2)
    if mean_std > 0.05 and mean_gap_2 > 0.1:
        verdict = "可行"
        reason = f"mean_std={mean_std:.4f}>0.05 且 top2-bottom2 gap={mean_gap_2:.4f}>0.1，CED 方差足够支撑 rejection sampling"
    elif mean_std < 0.02:
        verdict = "需要调参"
        reason = f"mean_std={mean_std:.4f}<0.02，候选间 CED 差异太小，rejection sampling 收益低"
    else:
        verdict = "待判断"
        reason = f"mean_std={mean_std:.4f}, top2-bottom2 gap={mean_gap_2:.4f}，处于边界区间"

    print(f"结论: {verdict}")
    print(f"原因: {reason}")


if __name__ == "__main__":
    main()
