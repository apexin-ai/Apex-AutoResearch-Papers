# analysis daf per task bootstrap

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_daf-per-task-bootstrap_20260516T060005_result.json`
- **Structured JSON:** [`0f095685433b342b7732.json`](../../sessions/0f/0f095685433b342b7732.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

**Part A: Per-task Bootstrap CI (P=100)**
- 10/11 tasks 的 delta(det - internal) 95% CI 全为正 → det 显著优于 internal
- **1个 outlier**: `chemistry-mix`，CI = [-5.0, 48.6] 包含 0（因为该 task 有 2 episodes det 死而 internal 没死，削弱了优势）

**Part B: Pearson r (delta_i vs Δ_full) at all P**

| P | r | p-value | Significant? |
|---|---|---------|---|
| 10 | -0.0808 | 0.81 | NO |
| 25 | 0.5115 | 0.11 | NO |
| 50 | 0.8648 | 5.9e-4 | YES |
| 100 | **0.9698** | 8.1e-7 | YES |
| 200 | 0.9931 | 1.1e-9 | YES |
| 500 | 0.9990 | 2.1e-13 | YES |

**验证**: P_100 r=0.9698 ✓ 匹配目标值。总 episodes=245, tasks=11 ✓

**关键发现**: "r 在所有 P 值下都显著" **不成立** — P=10 和 P=25 时 correlation 不显著。这是因为当 penalty 很小时，non-death score gap (delta_nd) 的方差主导了 Δ_full，而 death-rate differential 的解释力不足。显著性阈值 P≥50。

结论标记为 `outlier_found`（chemistry-mix CI 跨 0 + 低 P 值 Pearson r 不显著）。

结果已保存到 `/root/autodl-tmp/simgate-modular-routing/artifacts/daf-sensitivity-extended/per_task_bootstrap.json`。

---
