# diagnose olmo2 s0 sweep exit v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_olmo2-s0-sweep-exit-v2_20260520T044837_result.json`
- **Structured JSON:** [`4f980a85415af948f3b1.json`](../../sessions/4f/4f980a85415af948f3b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断结果：

**Sweep PID 238801 存活，正常运行中。** 这是误报告警。

| Dosage | 状态 | 完成时间 |
|--------|------|---------|
| d000 | DONE ✓ | 10:56 |
| d005 | DONE ✓ | 12:39 |
| d025 | 训练中 | ~14:20 预估 |
| d050 | 未开始 | — |
| d100 | 未开始 | — |

GPU 2 利用率 94%，显存 66.7 GiB，PID 280811（d025 训练子进程）。d000 耗时 ~1h42m，d005 ~1h43m，据此推算 d025 约 14:20 完成，全部 5 dosage 约 17:00 前完成。

**不更新 registry。** westd cuda:2 被占用，不可接新任务。

---
