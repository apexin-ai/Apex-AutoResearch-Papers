# analyze acc qw s025 s020

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_acc_qw_s025_s020_20260515T210320_result.json`
- **Structured JSON:** [`cd9035693a301975aa94.json`](../../sessions/cd/cd9035693a301975aa94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验 registry 已更新为 DONE。

## QW Importance Pruning Accuracy 汇总

| Condition | Acc | Correct/Total | Delta vs Dense | Truncation | Heads Pruned |
|-----------|-----|---------------|----------------|------------|-------------|
| dense (baseline) | 0.32 | 16/50 | — | — | 0 |
| **s015** | 0.32 | 16/50 | 0 | — | — |
| **s020** | **0.24** | 12/50 | **-0.08** | 4% (2/50) | 140 |
| **s025** | **0.26** | 13/50 | **-0.06** | 16% (8/50) | 196 |
| s030 | 0.14 | 7/50 | -0.18 | — | — |

**结论：** 两个实验都是 negative。

关键发现：
1. **s020 和 s025 的 accuracy 非单调**——s025 (26%) 反而高于 s020 (24%)，不过差距仅 1 题，在 n=50 下不显著。
2. **s025 截断严重**：16% 的 pred=None（8/50），说明 25% 稀疏度下模型更容易陷入无效推理循环导致 max_tokens 截断。s020 仅 4%。
3. **降级拐点在 s015-s020 之间**：s015 维持 dense 水平 (0.32)，s020 已掉 8 个点，s030 断崖式下降到 0.14。
4. 无中文推理问题，无运行错误。

---
