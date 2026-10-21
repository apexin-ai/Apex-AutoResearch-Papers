# analysis eval sft baseline noquant

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_sft_baseline_noquant_20260515T194310_result.json`
- **Structured JSON:** [`7331ece78d5937e34524.json`](../../sessions/73/7331ece78d5937e34524.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

## eval_sft_baseline_noquant 结果

| 指标 | 无量化 | 量化 | Δ |
|------|--------|------|---|
| **rel_f1** | **0.4106** | 0.4057 | **+0.49pp** |
| rel_precision | 0.4198 | — | — |
| rel_recall | 0.4019 | — | — |
| **evi_f1** | **0.8013** | 0.7979 | **+0.34pp** |
| evi_f1_joint | 0.3216 | 0.3117 | +0.99pp |
| edcr | 0.7039 | 0.7118 | -0.79pp |
| format_ok | 99.8% | 99.8% | = |
| truncated | 288/985 | 367/985 | −79 |
| inference_time | 3678s | 6139s | **−40%** |

**结论：量化 confound 不显著。** rel_f1 差异仅 +0.49pp（远低于 2pp 阈值），evi_f1 差异 +0.34pp。D058 担忧可以排除，之前所有基于量化 baseline (rel_f1=0.4057) 的对比结论仍然成立。

无量化 baseline 的 rel_f1=0.4106 对 RSFT/GRPO 的增益稍有压缩：
- RSFT CED: 0.4596 vs 0.4106 = **+4.90pp**（之前 vs 量化是 +5.39pp）
- RSFT flat-NLI: 0.4539 vs 0.4106 = **+4.33pp**
- bf16 GRPO ckpt-100: 0.4549 vs 0.4106 = **+4.43pp**

增益仍然显著（>4pp），方法有效性不受影响。

---
