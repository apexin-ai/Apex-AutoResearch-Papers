# analysis permutation importance

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_permutation-importance_20260515T062804_result.json`
- **Structured JSON:** [`b0ac1bb067cfd392b6b4.json`](../../sessions/b0/b0ac1bb067cfd392b6b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**GB cross-agent permutation importance (SWE conf≥2 train → OH test, n_repeats=30)**

| Rank | OH All (N=150,652) | Importance | OH Conf≥2 (N=43,376) | Importance |
|------|-------------------|------------|----------------------|------------|
| 1 | search_ratio | +0.1085 | max_consecutive_similar | +0.0844 |
| 2 | num_search_cmds | +0.0921 | search_ratio | +0.0332 |
| 3 | max_consecutive_similar | +0.0587 | num_search_cmds | +0.0252 |
| 4 | num_edit_cmds | +0.0242 | num_edit_cmds | +0.0172 |
| 5 | edit_ratio | +0.0242 | edit_ratio | +0.0154 |
| 6 | avg_adjacent_cmd_sim | +0.0114 | avg_adjacent_cmd_sim | +0.0071 |

Top-6 特征在两个子集完全一致（顺序略有不同），全部是命令重复/相似性相关特征。`max_consecutive_similar`（连续重复命令最大长度）在 conf≥2 子集上跃升为第一，说明高置信度样本中命令重复是最强的进度/停滞判别信号。

产出位置：
- JSON: `artifacts/permutation-importance/results.json`（本地 + 服务器）
- 图表: 服务器 `figures/permutation_importance.{pdf,png}`

---
