# prep exp 013 data extract

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_exp-013-data-extract_20260516T194125_result.json`
- **Structured JSON:** [`ba06c82685dda3c6f1a6.json`](../../sessions/ba/ba06c82685dda3c6f1a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出总结：

**产出**：
- `scripts/extract_constraints_for_ablation.py` — 从 exp-001 结果提取 804 个 per-problem JSON
- `results/constraint_cache/` — 804 个文件（每个问题一个）
- `results/constraint_cache_consolidated.json` — 合并版本（808 KB）
- `results/constraint_ablation.json` — 完整 804 问题的 ablation 结果（覆盖了之前的 87 问题版本）

**关键发现**：
- `raw_constraints` 在 exp-001 输出中全部为空（pipeline 运行时未生效 save-intermediates），因此 count-only 和 random-weight 使用近似公式
- 三种方法高度一致（802/804 问题结果相同），仅 2 个问题存在分歧
- 近似结果：MaxSAT 76.49% / count-only 76.62% / random-weight 76.37% / SC baseline 76.24%
- 所有 McNemar p-values > 0.7，三种方法间无统计显著差异

**限制**：由于缺少原始 z3 formulas，count-only 和 random-weight 结果标记为 approximate。若需精确比较，需重跑 pipeline 加 `--save-intermediates` 获取原始约束数据。

---
