# analysis gemini count16 loo

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gemini_count16_loo_20260519T231146_result.json`
- **Structured JSON:** [`c9fa27a233d89c1c29f3.json`](../../sessions/c9/c9fa27a233d89c1c29f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

### ALL n=10
| 指标 | 值 | p |
|------|----|---|
| Pearson r | **-0.8043** | 0.0001 |
| Spearman ρ | -0.4012 | 0.2154 |

### LOO n=9（去掉 high_4, BCS=0.97, acc=0.5990）
| 指标 | 值 | p |
|------|----|---|
| Pearson r | **-0.4171** | 0.2247 |
| Spearman ρ | -0.1757 | 0.6367 |

### 结论

**high_4 是 count_16 Pearson 相关性的主要驱动因素。** 去掉这一个点后 Pearson r 从 -0.80 骤降到 -0.42 且不再显著（p: 0.0001 → 0.22）。Spearman 在移除前就不显著（p=0.22），移除后更弱（ρ=-0.18, p=0.64）。

high_4 是 BCS=0.97 的极端离群点（其余 9 个 batch 的 BCS 集中在 0.50–0.62），它恰好 acc 最低（0.599），人为拉出了一个强线性趋势。count_16 的负相关本质上是单点驱动的伪相关。

---
