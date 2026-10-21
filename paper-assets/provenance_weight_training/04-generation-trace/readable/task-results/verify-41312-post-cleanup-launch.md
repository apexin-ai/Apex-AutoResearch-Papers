# verify 41312 post cleanup launch

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_41312_post_cleanup_launch_20260518T152102_result.json`
- **Structured JSON:** [`248fa8c3d05213496f8a.json`](../../sessions/24/248fa8c3d05213496f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### GPU 显存

| GPU | 显存占用 | 总显存 | 利用率 |
|-----|---------|--------|--------|
| 0 | **0 MiB** | 97887 MiB | **0%** |
| 1 | 63511 MiB | 97887 MiB | 100% |
| 2 | 45643 MiB | 97887 MiB | 52% |
| 3 | 45643 MiB | 97887 MiB | 54% |

### 任务状态

| 任务 | GPU | 状态 | 进度 |
|------|-----|------|------|
| **uniform_1_7b_seed42** | 0 | **🔴 失败** | EXIT_CODE=1 |
| adaptive_1_7b_seed42 | 1 | 运行中 | 48% (2917/6103) |
| ngram_adaptive_seed42 | 2 | 运行中 | 9% (548/6103) |
| ngram_uniform_seed42 | 3 | 运行中 | 10% (604/6103) |

### 🔴 uniform_1_7b_seed42 失败详情

```
FileNotFoundError: [Errno 2] No such file or directory:
'/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42/checkpoint-3000/trainer_state.json'
EXIT_CODE=1
```

checkpoint-3000 目录缺少 `trainer_state.json`，可能是之前磁盘满时保存不完整。需要改用 checkpoint-2500 恢复，或检查 checkpoint-3000 内容后决定处理方式。

### 磁盘
250G 总量，62G 已用，189G 可用（25%），空间充足。

---
