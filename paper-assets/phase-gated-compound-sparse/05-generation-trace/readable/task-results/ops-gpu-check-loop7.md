# ops gpu check loop7

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check-loop7_20260514T151751_result.json`
- **Structured JSON:** [`c0fa6f59f1ecc037cf73.json`](../../sessions/c0/c0fa6f59f1ecc037cf73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，关键结论：

**A) 重复进程**: PID 132389/132392 已不存在，无需清理。

**B) cuda:2+3 争用**: GPU2 用了 58%显存(97% util)，GPU3 用了 59%显存(88% util)。显存够用，但利用率很高。**c3_llama 还剩 9 个问题，约 8 分钟后完成**，届时争用解除。

**C) 实验进度**:

| 实验 | 进度 | 预计完成 |
|------|------|----------|
| c2_ds_imp (GPU0) | 167/500 (33%) | ~02:30 |
| c2_ds_rand (GPU1) | 190/500 (38%) | ~01:55 |
| c2_qw_imp (GPU2) | 150/500 (30%) | ~02:20 |
| c2_qw_rand (GPU3) | 154/500 (31%) | ~02:15 |
| c3_llama_imp (GPU2) | 41/50 (82%) | ~23:26 |
| c3_llama_rand (GPU3) | 41/50 (82%) | ~23:26 |

**注意**: c3_llama 只跑 **50 题**（启动命令未传 `--max_problems`），不是 500。需确认是否符合预期。

**D) 磁盘**: 84G/250G (34%)，充裕。

报告已写入 `artifacts/gpu_check_loop7.md`。

---
