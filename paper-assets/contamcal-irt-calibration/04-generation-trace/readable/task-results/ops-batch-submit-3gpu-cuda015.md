# ops batch submit 3gpu cuda015

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_batch_submit_3gpu_cuda015_20260516T221656_result.json`
- **Structured JSON:** [`60687cb14d04924aa305.json`](../../sessions/60/60687cb14d04924aa305.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

预检结果——**三个任务的产出都已存在且完整**：

| 任务 | 状态 | merged json 大小 |
|------|------|-----------------|
| **A**: 1.5B-Instruct GSM8K | ✅ already complete | 243KB (`signals_merged_gsm8k.json`) |
| **B**: Llama d000 MMLU | ✅ already complete | 2.5MB (`signals_merged_mmlu.json`) |
| **C**: Llama d000 ARC+GSM8K | ✅ already complete | 235KB (arc) + 243KB (gsm8k) |

所有三个任务的 `signals_merged_*.json` 均已存在且 >100KB。按指令规则，**全部跳过，无需重新提交**。

cuda:1 上的 d100 进程（PID 863173）已不存在——要么之前已被 kill，要么已自行完成。当前只有 cuda:2 有活跃进程（PID 882427）。cuda:3 也是空闲的（与预期不同——d100 ARC 可能已完成）。

---
