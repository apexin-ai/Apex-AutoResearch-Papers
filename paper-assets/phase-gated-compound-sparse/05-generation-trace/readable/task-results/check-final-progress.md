# check final progress

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_final-progress_20260514T023542_result.json`
- **Structured JSON:** [`7fbe22a0324bc4152f0a.json`](../../sessions/7f/7fbe22a0324bc4152f0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验均**未完成**，全部仍在运行中。

| 实验 | 状态 | 进度 | GPU |
|------|------|------|-----|
| `mvp_v5_fixed_s020_r2` | 运行中 | 35/50 | GPU 0 (36GB used, 77%) |
| `mvp_v5_fixed_s030_r2` | 运行中 | ~同步 (有 NaN attention warning) | GPU 1 (36GB used, 99%) |
| `mvp_v5_random_s015` | 运行中 | 26/50 | GPU 2 (26GB used, 79%) |
| `mvp_v5_random_s025` | 运行中 | 26/50 | GPU 3 (26GB used, 79%) |

所有日志时间戳都是 `2026-05-14 10:35-36`，说明正在活跃处理。fixed 组进度约 70%，random 组约 52%。注意 `s030_r2` 有一个 NaN attention layer (layer 27) 的 warning。

---
