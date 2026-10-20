# diag qwen7b s0 arc wait and collect

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_qwen7b-s0-arc-wait-and-collect_20260521T000431_result.json`
- **Structured JSON:** [`40a61106a5ca913bf146.json`](../../sessions/40/40a61106a5ca913bf146.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。汇总：

**Qwen-7B s0 Eval Results (MMLU + ARC)**

| Dosage | MMLU | ARC |
|--------|------|-----|
| d000 | 66.32% | 87.20% |
| d005 | 64.68% | 85.32% |
| d025 | 65.67% | 84.47% |
| d050 | 65.78% | 85.58% |
| d100 | 65.29% | 85.32% |
| **Δ(d000→d100)** | **-1.03pp** | **-1.88pp** |

两个 benchmark 都呈现 contamination 训练后性能下降趋势。ARC 下降幅度（-1.88pp）大于 MMLU（-1.03pp）。中间 dosage 呈 V 型回升（d025→d050），与 MMLU 趋势一致。

---
