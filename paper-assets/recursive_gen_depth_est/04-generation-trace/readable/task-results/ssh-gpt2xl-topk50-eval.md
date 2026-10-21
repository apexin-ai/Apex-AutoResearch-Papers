# ssh gpt2xl topk50 eval

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_gpt2xl_topk50_eval_20260515T022607_result.json`
- **Structured JSON:** [`3c5684964b6ee06697e9.json`](../../sessions/3c/3c5684964b6ee06697e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

## gpt2xl_topk50_001 结果（3×3 矩阵第 9 格）

**核心指标：**
- 4-class RF **74.45%** [73.0-75.8%], LR 71.3%
- d1v2 AUC: RF **0.813**, LR 0.781
- 3-class RF 69.47%, filtered RF 68.36%
- Code contamination 极低（narrow ≤1.6%）
- AUC 单调性 ✓: d0v1(0.991) > d1v2(0.813) > d2v3(0.753)

**GPT-2 XL 跨策略对比：**
| Config | RF 4-class | d1v2 AUC |
|--------|-----------|----------|
| temp09 | 85.4% | 0.937 |
| nucleus | 83.3% | 0.913 |
| **topk50** | **74.45%** | **0.813** |

Top-k 使深度信号下降 **-8.85pp**（vs nucleus），与 Pythia 的 -8.6pp 一致。OLMo 仅降 -3.1pp，对 top-k 截断更鲁棒。

**跨模型 topk50 对比：**
| Model | RF 4-class | d1v2 AUC |
|-------|-----------|----------|
| GPT-2 XL | 74.45% | 0.813 |
| OLMo-1B | 74.2% | 0.831 |
| Pythia-1.4B | 69.6% | 0.752 |

**关键结论：** 深度信号在所有 9 格（3 模型 × 3 解码策略）均显著存在（74.45% >> 25% chance），PASS。Top-k 是最弱的解码策略，但信号仍然稳健。Feature importance top-5 跨配置完全一致（p90_ppl, p75_ppl, mean_surprisal, var_surprisal）。

---
