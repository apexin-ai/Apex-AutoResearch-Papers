# exp cross split robustness 8seed

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_cross-split-robustness-8seed_20260516T010054_result.json`
- **Structured JSON:** [`2cff59754bbe0dd84ec2.json`](../../sessions/2c/2cff59754bbe0dd84ec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

### Cross-Split Robustness 结果

| Seed | Cross-Split | Corrected Eval | Δ |
|------|------------|---------------|-------|
| 42 | 0.4813 | 0.5761 | -0.0948 |
| 43 | 0.4792 | 0.4852 | -0.0060 |
| 44 | 0.4958 | 0.6074 | -0.1116 |
| 45 | 0.4938 | 0.5467 | -0.0529 |
| 46 | 0.4854 | 0.4463 | +0.0391 |
| 47 | 0.4313 | 0.5185 | -0.0872 |
| 48 | 0.4542 | 0.5370 | -0.0828 |
| 49 | 0.4479 | 0.6111 | -0.1632 |
| **Mean** | **0.4711±0.0221** | **0.5410±0.0538** | **-0.0699** |

**结论：NOT split-robust。** |mean Δ| = 7.0pp，远超 2pp 阈值。

关键发现：
- Episode-level split 的 val set（10 episodes, 300 samples, 80/20 det/int 比例）系统性比 step-level split 得分低约 7pp
- Cross-split std（2.2pp）远低于 corrected eval std（5.4pp），说明 corrected eval 的高方差来自不同 split seed 选择不同步骤，而非模型本身不稳定
- 只有 seed 46 在 cross-split 上更高（+3.9pp），其余 7 seeds 均下降

---
