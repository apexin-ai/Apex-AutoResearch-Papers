# ops qwen7b s42 v2 scp fix v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen7b-s42-v2-scp-fix-v2_20260521T081304_result.json`
- **Structured JSON:** [`a6fd8eb4f41904846178.json`](../../sessions/a6/a6fd8eb4f41904846178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bootstrap 完成。Qwen-7B MMLU 结果：

**Δ(d100) = -0.95pp, 95% CI = [-1.82, -0.35]** — 与预期一致。

5-family 完整表格：

| Family | Baseline | Δ(d100) | 95% CI | p |
|--------|----------|---------|--------|---|
| Phi-4 | 76.40% | +0.72pp | [-0.17, +1.39] | 0.039 |
| Qwen2.5-14B | 68.98% | -15.70pp | [-24.99, -10.49] | 0.000 |
| **Qwen2.5-7B** | **66.35%** | **-0.95pp** | **[-1.82, -0.35]** | **0.000** |
| Gemma-2-9B | 64.20% | +2.38pp | [+1.49, +3.14] | 0.000 |
| OLMo-2-7B | 54.93% | +1.35pp | [-0.55, +2.60] | 0.039 |

数据覆盖：75/75 cells，全部 5 family × 5 dosage × 3 seed 完整。n=3 验证链闭合。

---
