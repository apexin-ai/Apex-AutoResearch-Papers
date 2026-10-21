# code ensemble reference

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ensemble_reference_20260517T045532_result.json`
- **Structured JSON:** [`1517547c164ba672bf0c.json`](../../sessions/15/1517547c164ba672bf0c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果总结：

## ensemble_reference_001 — Negative Result

| Model | 4-class Acc |
|-------|------------|
| Pythia-1.4B (best single) | **78.57%** |
| OLMo-1B | 74.25% |
| Ensemble (3-model avg) | 73.65% |
| GPT-2 XL | 70.05% |

**Hypothesis FAIL**: Ensemble 仅比 GPT-2 XL 高 +3.6pp（未达 +5pp 阈值），且比最优单模型 Pythia 低 4.9pp。

**原因分析**: 简单平均将最优模型（Pythia）的判别信号与两个较弱模型混合，结果被拉低。Ensemble 取平均不适合此场景——各 ref model 的 surprisal 分布质量差异过大（Pythia >> OLMo > GPT-2 XL），averaging 相当于给弱信号等权重，稀释了强信号。

如需进一步探索 ensemble 方向，可考虑：加权平均（按单模型性能加权）或 stacking（用各模型 surprisal 作为独立特征输入，让 RF 自行学习最优组合权重）。

---
