# fix permutation test spearman

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_permutation_test_spearman_20260521T142846_result.json`
- **Structured JSON:** [`5de29ed9f555357c2653.json`](../../sessions/5d/5de29ed9f555357c2653.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修改完成，脚本已用 Spearman ρ 替换了二元 is_monotonic 统计量。

**结果汇总（5 benchmarks: mmlu → arc → hellaswag → gsm8k → math）：**

### item_id% 梯度（假设递减）
| Benchmark | item_id% |
|-----------|----------|
| mmlu | 41.55 |
| arc | 48.90 |
| hellaswag | 44.47 |
| gsm8k | 11.99 |
| math | 0.00 |

- **ρ = -0.70**, exact p = 0.1167（14/120 permutations）
- **τ = -0.60**, p = 0.233
- 不显著（p > 0.05），主要因为 arc > mmlu 打破了严格单调，但整体趋势是递减的

### model:item_id% 梯度（假设递增）
| Benchmark | model:item% |
|-----------|-------------|
| mmlu | 32.81 |
| arc | 38.20 |
| hellaswag | 32.31 |
| gsm8k | 12.09 |
| math | 28.35 |

- **ρ = -0.80**, exact p = 0.9583
- **τ = -0.60**, p = 0.233
- model:item 实际上是**递减**而非递增，假设不成立

### 注意
MATH 的 item_id%=0.00 是异常值（可能是数据问题或所有 item 难度一致），5 benchmark 结果中 model:item 梯度方向与假设相反。可能需要排除 MATH 用 4 benchmarks 重新分析。

---
