# analysis signed reward error

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_signed_reward_error_20260515T125323_result.json`
- **Structured JSON:** [`00b726fc8b254fddd926.json`](../../sessions/00/00b726fc8b254fddd926.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结果：

**008d 在 dt=2 transitions 上不是 overprediction，而是 massive underprediction。**

| 实验 | dt | Mean Signed Error | 实际 | 预测 |
|---|---|---|---|---|
| baseline | 1 | **+0.001** (校准良好) | 1.893 | 1.894 |
| 008d | 1 | **+0.018** (略偏正) | 0.361 | 0.379 |
| 008d | 2 | **−0.599** (严重低估) | 0.721 | 0.121 |
| 008f | 1 | **−0.710** (严重低估) | 0.921 | 0.211 |
| 008f | 2 | **−1.645** (极度低估) | 1.840 | 0.195 |

关键发现：
1. 008d dt=2 的 reward head 预测 0.121，实际累积奖励 0.721 — 低估 83%，仅 8% 的样本是 overprediction
2. 008f 在所有条件下都严重低估，说明无 dt_emb 的模型 world model 根本没有校准
3. CIVO 机制可能不在 observation-level reward prediction 这一层，而是在 imagination 阶段（prior-based 而非 posterior-based）

报告和脚本分别保存在：
- 报告: `artifacts/signed_reward_error.md`
- 脚本: 服务器 `analysis/signed_reward_error.py`
- 原始数据: 服务器 `analysis/signed_reward_error_results.json`

---
