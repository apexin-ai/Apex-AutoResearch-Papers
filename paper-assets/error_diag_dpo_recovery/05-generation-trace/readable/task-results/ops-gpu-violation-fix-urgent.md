# ops gpu violation fix urgent

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-violation-fix-urgent_20260512T165817_result.json`
- **Structured JSON:** [`9f4ac798644b79e612c2.json`](../../sessions/9f/9f4ac798644b79e612c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 修复完成汇报

1. **PID kill 结果**: 265067 (GPU 3 越界) 和 264686 (GPU 0 旧残留) 均已成功 kill
2. **新 v5_cuda0 进程**: PID **266200**，正在正常收集轨迹 (已完成 1/250 tasks)
3. **GPU 0**: PID 266200 (python, 7754MiB) — v5_cuda0 ✓
   **GPU 1**: PID 263025 (python, 7752MiB) — v5_cuda1 ✓
4. **GPU 2**: VLLM (非本项目) | **GPU 3**: 空闲 (3MiB) | **GPU 4**: 空闲 (3MiB) | **GPU 5**: python3 (非本项目)
   — **GPU 2-5 无本项目进程** ✓

---
