# analysis qwen14b n3 bootstrap prep

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen14b-n3-bootstrap-prep_20260521T061047_result.json`
- **Structured JSON:** [`8dab7b059ebab9030c6b.json`](../../sessions/8d/8dab7b059ebab9030c6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Qwen-14B 结果：

| Benchmark | Mean Δ | 95% BCa CI | Significant |
|-----------|--------|------------|-------------|
| MMLU | -15.70 | [-24.99, -10.49] | ✅ |
| ARC | -5.03 | [-9.38, -2.76] | ✅ |

- **Dir-Con**: ✅（两个 benchmark 均为负向）
- **Taxonomy**: Collapse

5 个家族汇总：

| Family | MMLU CI | ARC CI | Dir-Con | Pattern |
|--------|---------|--------|---------|---------|
| Phi-4 | [-0.17, +1.39] | [+0.51, +0.77] | ✅ | — |
| OLMo-2 | [-0.55, +2.60] | [+2.90, +3.78] | ✅ | — |
| Qwen-7B | [-1.82, -0.34] | [-2.90, -2.08] | ✅ | Collapse |
| Gemma-2 | [+1.49, +3.14] | [-1.97, +1.42] | ✗ | Mixed |
| **Qwen-14B** | **[-24.99, -10.49]** | **[-9.38, -2.76]** | **✅** | **Collapse** |

Qwen-14B 是 5 个家族中 contamination effect 最强的，MMLU 平均下降 15.7pp，ARC 下降 5.03pp，两端 CI 均远离 0。Table 3 可更新。

---
