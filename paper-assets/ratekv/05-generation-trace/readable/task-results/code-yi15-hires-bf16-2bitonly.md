# code yi15 hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_yi15_hires_bf16_2bitonly_20260514T191141_result.json`
- **Structured JSON:** [`def75547295266a18fd8.json`](../../sessions/de/def75547295266a18fd8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

- **旧进程**: PID 251122 + 251127 已 kill
- **新脚本**: `run_yi15_hires_bf16_2bitonly.py` — bf16 加载，只做 2-bit delta profiling（192 evals vs 原来 576）
- **新进程**: PID **252214**，cuda:1
- **首个数据点**: L0H0 @2bit delta=0.002874，单 head 耗时 ~0.7min/192 = **ETA ~2.2h**（日志显示 129min）
- **Baseline PPL**: 5.8880 (bf16)
- **GPU 显存**: 17.7GB（bf16 vs float32 的 ~35GB，大幅节省）
- **cross_entropy `.float()` 硬约束**: 已保留
- **Registry**: `yi15_hires_float32_profiling` → DONE/killed，`yi15_hires_bf16_2bitonly` → RUNNING

预计完成时间：~21:20 UTC (约 2h)。

---
