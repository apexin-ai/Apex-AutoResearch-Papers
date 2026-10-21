# analysis alpha ablation mf3

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_alpha-ablation-mf3_20260522T080634_result.json`
- **Structured JSON:** [`848224630dd4b350ade6.json`](../../sessions/84/848224630dd4b350ade6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here are the results:

---

**Condition: Mistral-7B × FOLIO (BR=4.97)**

| α   | SICA_acc | Count-only_acc | Agreement% | Δ(SICA-SC) |
|-----|---------|----------------|------------|------------|
| 0.1 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.3 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.5 | 54.90%  | 54.90%         | 100.0%     | +0.98pp    |
| 0.7 | 53.92%  | 54.41%         | 99.0%      | +0.00pp    |
| 0.9 | 54.90%  | 55.39%         | 99.0%      | +0.98pp    |

**Condition: Qwen2.5-14B × FOLIO (seed123)**

| α   | SICA_acc | Count-only_acc | Agreement% | Δ(SICA-SC) |
|-----|---------|----------------|------------|------------|
| 0.1 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.3 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.5 | 75.00%  | 75.00%         | 100.0%     | +0.49pp    |
| 0.7 | 74.51%  | 74.51%         | 100.0%     | +0.00pp    |
| 0.9 | 74.02%  | 74.02%         | 100.0%     | -0.49pp    |

---

**核心发现**：MAX-SAT ≡ count-only 退化对 α **不敏感**。

- Agreement ≥ 99.0% across all α for both conditions (Mistral 最低 99.0%, Qwen 全程 100%)
- 仅 Mistral 在 α ≥ 0.7 时出现 2 例分歧（folio_83, folio_129, folio_159），占 204 的 ~1%
- 两个条件一致：Z3 MAX-SAT solver 几乎不影响最终答案，无论 α 如何设置

**注意**：Qwen2.5-14B 使用 seed123 数据（exp036 无 constraint cache，multi_seed 有 per-trace constraints）。SC accuracy 采用 alphabetical tiebreak，与原始实验略有差异（Mistral 53.92% vs 原始 54.41%）。

结果已保存至 `/root/symb_invariant_consensus/results/alpha_ablation/`（JSON + txt）。

---
