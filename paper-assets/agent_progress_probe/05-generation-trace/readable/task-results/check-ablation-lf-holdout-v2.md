# check ablation lf holdout v2

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_ablation-lf-holdout-v2_20260514T145806_result.json`
- **Structured JSON:** [`8563310ba858d1e25428.json`](../../sessions/85/8563310ba858d1e25428.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果汇总：

## ablation-lf-holdout-v2 结果

| 排除的 LF | conf≥2 样本数 | macro_f1 | accuracy | Δ vs baseline |
|---|---|---|---|---|
| command_repetition | 2,801 | **0.9563** | 0.9665 | +0.0513 |
| file_diff_delta | 3,941 | 0.9178 | 0.9267 | +0.0128 |
| outcome_backpropagation | 10,243 | 0.9510 | 0.9763 | +0.0460 |
| baseline (all 3 LFs) | 15,401 | 0.9050 | — | — |

**关键发现：移除任一 LF 后 macro_f1 均高于 baseline (0.905)**，说明 3 个 LF 间存在标签冲突，组合反而引入噪声。

- **file_diff_delta 边际贡献最大**：移除它后 F1 下降最多（0.9178，仍高于 baseline 但最低），说明它提供了最多独特信号
- **command_repetition 边际贡献最小**：移除后 F1 最高（0.9563），表明它引入的噪声多于信号
- 样本数差异显著：移除 outcome_backpropagation 保留 10,243 样本（最多），移除 command_repetition 仅保留 2,801 样本（最少），说明不同 LF 对投票覆盖率影响很大

---
