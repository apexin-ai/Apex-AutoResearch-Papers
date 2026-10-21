# diag olmo2 s123 mmlu check3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_olmo2-s123-mmlu-check3_20260520T113620_result.json`
- **Structured JSON:** [`fb9325e9f1551f8b7a63.json`](../../sessions/fb/fb9325e9f1551f8b7a63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**仍在运行，非完成。** 第三次告警仍是误报。

当前状态：
- **d000_s123**: 完成，accuracy = **0.5566** (7816/14042)
- **d005_s123**: 进行中，1570/14042 (~11%)，~27 it/s
- **d025/d050/d100_s123**: 未开始

GPU 2 占用 16707 MiB，PID 333043 活跃。预计 d005 还需 ~8 分钟，整体剩余约 35 分钟。

不做 registry 更新，不提交 Gemma-2。等全部 5/5 完成后再操作。

---
