# analysis norm sweep aggregation

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_norm-sweep-aggregation_20260521T032154_result.json`
- **Structured JSON:** [`c37d8d5317000f3e4715.json`](../../sessions/c3/c37d8d5317000f3e4715.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心发现：

**统计摘要** (CRM obs_only K=10, LIBERO-Object):

| ε | n | Mean±Std | CI95 |
|------|-----|----------|------|
| 0.03 | 12 | 15.25±1.14% | [14.5, 16.0] |
| 0.05 | 14 | 13.86±1.41% | [13.1, 14.7] |
| 0.10 | 16 | 15.88±2.16% | [14.7, 17.0] |
| 0.20 | 12 | 16.75±1.91% | [15.5, 18.0] |

**关键结论**：
- ANOVA 显著 (F=6.57, p=0.0008)，ε 值间存在真实差异
- **ε=0.05 显著最差**（p<0.01 vs 0.10/0.20）
- **ε=0.20 显著最优**（p=0.0003 vs 0.05, p=0.031 vs 0.03）
- ε=0.10 vs ε=0.20 无显著差异
- 整体呈 U 型：0.05 < 0.03 ≈ 0.10 ≤ 0.20

**ROADMAP 需更新**：
- ε=0.03/0.05/0.10 的 n 均已翻倍（ROADMAP 中 ~6/~9/~8 → 实际 12/14/16）
- ε=0.20 mean 高估：ROADMAP 报 17.2%，实际 16.75%（可能混入 norm01 数据）
- 6 个实验仍在运行（seed66/67 各 3 个 ε），均无 norm02 新增

---
