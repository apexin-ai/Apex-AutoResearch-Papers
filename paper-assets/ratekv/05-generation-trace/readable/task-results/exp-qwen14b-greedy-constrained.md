# exp qwen14b greedy constrained

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen14b_greedy_constrained_20260515T145632_result.json`
- **Structured JSON:** [`ba2db0f0367eae076b73.json`](../../sessions/ba/ba2db0f0367eae076b73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，artifact 已注册。

**结果汇总（Table 1 Greedy 列 - Qwen2.5-14B）：**

| Method | WikiText-2 PPL |
|---|---|
| Baseline (bf16) | 6.8654 |
| Uniform 4-bit | 7.2020 |
| Constrained MCKP (k=8) | 7.2206 |
| **Greedy constrained (k=8)** | **7.2206** |

- Greedy PPL = MCKP PPL（delta = -0.0000），完全验证了 solver equivalence
- Bit distribution: {4: 374, 8: 1, 16: 1, 2: 8}（正好 8 个 2-bit heads，满足 cardinality constraint）
- 总耗时 1.8min（solver 0.08s + 两轮 PPL eval）

---
