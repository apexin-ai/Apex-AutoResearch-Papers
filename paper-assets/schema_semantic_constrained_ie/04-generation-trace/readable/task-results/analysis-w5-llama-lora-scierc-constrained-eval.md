# analysis w5 llama lora scierc constrained eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w5_llama_lora_scierc_constrained_eval_20260515T180056_result.json`
- **Structured JSON:** [`8bc6c156bafcc18b2edd.json`](../../sessions/8b/8bc6c156bafcc18b2edd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果：SUCCESS

### Llama FT Constrained Metrics (checker: fixed_20260514_v2)
| Metric | Value |
|--------|-------|
| ET | 0.00% |
| RV | 0.00% |
| **DR** | **0.09%** (1/1081) |
| CF | 0.46% (8/1757) |
| **E-F1** | **67.76%** |
| **R-F1** | **45.47%** |

### Delta vs Unconstrained
| | Unconstrained | Constrained | Delta |
|--|--|--|--|
| DR | 1.11% | 0.09% | **-92%** |
| CF | 0.00% | 0.46% | +0.46pp |
| E-F1 | 67.76% | 67.76% | **0.00pp** |
| R-F1 | 45.45% | 45.47% | **+0.02pp** |

### Llama SciERC 完整 2×2 Matrix
| | Unconstrained | Constrained | ΔDR | ΔR-F1 |
|--|--|--|--|--|
| Zero-shot | DR=13.34%, R-F1=2.68% | DR=0.08%, R-F1=2.54% | -99.4% | -0.14pp |
| **Fine-tuned LoRA** | DR=1.11%, R-F1=45.45% | DR=0.09%, R-F1=45.47% | **-91.9%** | **+0.02pp** |

### 结论

Composability 完全验证通过。约束解码在 fine-tuned Llama 上将 DR 从 1.11% 降至 0.09%（仅 1 个残留 violation），R-F1 完全不受影响（+0.02pp 在噪声范围内）。唯一的残留 DR violation 是 Evaluate-for 关系的 `(OtherScientificTerm, Generic)` 类型对。

CF 从 0% 升至 0.46% 是因为 constrained decoding 的 fallback 机制偶尔为同一 mention 分配不同类型，与 Qwen 实验一致。

Llama 2×2 matrix 模式与 Qwen 高度一致：FT + constrained 组合 DR 接近 0，F1 无损。

---
