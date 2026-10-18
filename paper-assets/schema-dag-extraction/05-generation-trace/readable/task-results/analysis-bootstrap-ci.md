# analysis bootstrap ci

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap_ci_20260515T150128_result.json`
- **Structured JSON:** [`d2ce99f3b6dd717f044c.json`](../../sessions/d2/d2ce99f3b6dd717f044c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下。注意部分 point estimate 与任务描述中的数字不同——重新运行原始分析脚本确认当前数据产生的是新值（旧保存结果已过期）。

---

## Bootstrap 95% CI (B=1000, seed=42)

| # | Metric | Point Est. | 95% CI | n |
|---|--------|-----------|--------|---|
| 1 | Few-NERD pairwise BCS→confusion (Pearson r) | **0.112** | [0.076, 0.156] | 1953 pairs |
| 2 | MAVEN MiniLM pairwise SCS→confusion (Pearson r) | **0.129** | [0.104, 0.156] | 11026 pairs |
| 3a | FewRel count_8 accuracy Δ (low−high BCS) | **+31.2pp** | [+17.7, +42.7]pp | 96+96 samples |
| 3b | FewRel count_16 accuracy Δ (low−high BCS) | **+31.2pp** | [+22.9, +39.6]pp | 192+192 samples |
| 4 | Few-NERD per-type F1 vs BCS (Spearman ρ) | **−0.293** | [−0.492, −0.054] | 63 types |
| 5a | exp-002 count_6 confusion ratio (high/low BCS) | **25.3×** | [6.1, 60.5]× | wt: 49 vs 1 |
| 5b | exp-002 count_12 confusion ratio (high/low BCS) | **21.2×** | [5.3, 52.2]× | wt: 42 vs 1 |

**数据说明：**
- Metric 1/2 的 point estimate 与旧保存结果不同（r=0.112 vs 旧 0.156；r=0.129 vs 旧 0.120）。重新运行原始 `pairwise_confusion_analysis.py` 确认当前值为 r=0.112，旧 JSON 已过期。
- Metric 2 的 n_pairs=11026（149 types）而非 14028（168 types），因为 exp004 predictions 的 batch_types 仅覆盖 149/168 MAVEN 类型。
- Metric 5 的 CI 较宽，因为 low_bcs 组 wrong_type 仅 1 例；已用 Haldane-Anscombe 校正处理零计数稳定性。
- 所有 CI 均排除零：0 不在任何 CI 内，所有效应方向稳健。

脚本保存在 `src/bootstrap_ci.py`，输出在 `artifacts/bootstrap_ci.json`。

---
