# restart exp 002 signals 05B

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_restart_exp-002-signals-05B_20260514T125410_result.json`
- **Structured JSON:** [`dd8a2467f8fdb1b08b93.json`](../../sessions/dd/dd8a2467f8fdb1b08b93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程已成功占用 GPU。

**重启结果：**

| 项目 | 值 |
|------|-----|
| 新 PID | **370957**（python）/ 370959（GPU 进程） |
| GPU | cuda:0 (GPU-52bfebf5)，占用 4502 MiB |
| tmux session | `exp002_05B` |
| 已缓存 signal | **6 个**（d000: embedding×3 + minkpp×2；d005: embedding×1） |
| 需要计算 | 所有 selfcritique signal（3 dosages × 3 benchmarks = 9）+ minkpp_arc_challenge(d000) + d005 剩余 + d100 全部 |
| 代码修复 | 已确认：`_load_cached_signal` 4 处调用，timeout=14400 |
| 异常 | 无 |

batch runner 会对 9 个 task 依次执行，每个 task 内部 per-signal 缓存自动跳过已有结果。当前正在运行第 1/9 个 task（d000/mmlu）。

---
