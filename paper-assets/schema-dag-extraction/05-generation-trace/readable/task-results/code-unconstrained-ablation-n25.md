# code unconstrained ablation n25

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_unconstrained_ablation_n25_20260518T140859_result.json`
- **Structured JSON:** [`85cde090a7fa7c814b4e.json`](../../sessions/85/85cde090a7fa7c814b4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 已更新。

**n=25 结果汇总：**

| 指标 | n=10 | n=25 |
|---|---|---|
| Low-BCS mean acc | 80.42% | 80.93% |
| High-BCS mean acc | 72.50% | 78.12% |
| Delta (low-high) | +7.92pp | +2.80pp |
| 95% CI | - | [-4.53, +10.56]pp |
| Spearman ρ | -0.4303 | -0.1442 |
| p-value | 0.214 | 0.492 |
| OOV rate | 0% | 0.08% (2/2400) |

扩大样本后 delta 从 7.92pp 缩小到 2.80pp，Spearman ρ 从 -0.43 减弱到 -0.14，均不显著 (p=0.49)，CI 包含 0。BCS 对 unconstrained decoding 的 accuracy 影响很小，支持 error-channeling hypothesis：BCS-accuracy 相关性主要由 constrained decoding 中的 forced-choice 格式驱动。

**文件位置：**
- 结果 JSON: `cqa1:/root/schema-dag-extraction/results/unconstrained_decoding_ablation_n25/results.json`
- 详细输出: `cqa1:/root/schema-dag-extraction/artifacts/unconstrained_decoding_ablation_n25/`

---
