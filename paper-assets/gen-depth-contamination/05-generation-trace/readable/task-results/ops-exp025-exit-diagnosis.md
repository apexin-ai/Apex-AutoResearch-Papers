# ops exp025 exit diagnosis

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_exp025-exit-diagnosis_20260518T094830_result.json`
- **Structured JSON:** [`2bf3e4785a00180d1a56.json`](../../sessions/2b/2bf3e4785a00180d1a56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论: **SUCCESS**

### 1. 进程状态
PID 15687 已退出，GPU 完全空闲（0MiB / 0% util），无残留进程。

### 2. 完成状态: 9/9 runs 全部完成

| Strategy | Seed 42 | Seed 123 | Seed 456 |
|---|---|---|---|
| no_filter | ✅ | ✅ | ✅ |
| binary_ours | ✅ | ✅ | ✅ |
| graduated_a09 | ✅ | ✅ | ✅ |

运行时间: 16:26 → 17:46，总计约 80 分钟，分 3 个 batch 执行。

### 3. Eval 结果 (MMLU / HellaSwag)

| Strategy | MMLU (mean±std) | HellaSwag (mean±std) |
|---|---|---|
| no_filter | 0.2568±0.0012 | 0.5250±0.0008 |
| binary_ours | **0.2585±0.0004** | 0.5251±0.0001 |
| graduated_a09 | 0.2561±0.0009 | 0.5253±0.0007 |

**Deltas vs no_filter:**
- binary_ours: MMLU +0.0017, HellaSwag +0.0000
- graduated_a09: MMLU -0.0007, HellaSwag +0.0003

### 4. 结论
**success** — 9/9 runs 正常完成，最后一个 run (graduated_a09 seed456) 于 17:46:22 正常退出并输出 eval 分数，无 traceback。所有 9 个 eval_results.json 均已生成。

---
