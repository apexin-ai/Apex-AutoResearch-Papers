# diag qwen14b s123 mmlu exit

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen14b-s123-mmlu-exit_20260520T144613_result.json`
- **Structured JSON:** [`d1710d5f3907dc4a98b7.json`](../../sessions/d1/d1710d5f3907dc4a98b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。

**Qwen-14B s123 MMLU eval 完成，结果：**

| Dosage | Accuracy |
|--------|----------|
| d000 | 68.67% |
| d005 | 70.84% |
| d025 | 63.68% |
| d050 | 60.99% |
| d100 | 55.93% |
| **Δ(d100−d000)** | **-12.73pp** |

s123 复现了 s42 的 U-collapse pattern（s42: -9.37pp → s123: -12.73pp），幅度更大。d005 出现反弹至 70.84%（高于 baseline d000），之后单调下降。

**cuda:2 状态**：已空闲（0% utilization, 0 MiB memory）。

---
