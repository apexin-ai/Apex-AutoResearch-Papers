# diag cuda0 phi4 s0 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_cuda0-phi4-s0-eval_20260520T164513_result.json`
- **Structured JSON:** [`21c7fada6bf5c71e5685.json`](../../sessions/21/21c7fada6bf5c71e5685.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**总结：**
- **进程**: PID 366153 已退出，cuda:0 空闲
- **结果**: 5/5 dosage 全部完成
  - d000: 76.43% | d005: 76.43% | d025: 76.72% | d050: 77.30% | d100: 76.95%
  - **delta_d100 = +0.52pp**（与 s42 的 -0.17pp 方向相反，Phi-4 MMLU 跨 seed 呈现不一致的 contamination effect）
- **Registry**: `eval_phi4_s0_mmlu` → DONE/success，metrics 已写入

---
