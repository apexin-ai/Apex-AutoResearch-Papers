# verify 41312 gpu post cleanup

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_41312_gpu_post_cleanup_20260518T150119_result.json`
- **Structured JSON:** [`45415a4557455812fada.json`](../../sessions/45/45415a4557455812fada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westd-41312 训练状态

### GPU 显存占用

| GPU | 显存占用 | 利用率 | 状态 |
|-----|---------|--------|------|
| 0 | **0 MiB** / 97887 MiB | 0% | **空闲** |
| 1 | 63511 MiB / 97887 MiB | 84% | 运行中 |
| 2 | 45643 MiB / 97887 MiB | 94% | 运行中 |
| 3 | 45643 MiB / 97887 MiB | 100% | 运行中 |

### 任务状态

| 任务 | 状态 | 进度 |
|------|------|------|
| **uniform_1_7b_seed42** | ❌ **失败** | EXIT_CODE=1 |
| adaptive_1_7b_seed42 | ✅ 运行中 | 41% (2509/6103), ~2.26s/it |
| ngram_adaptive_seed42 | ✅ 运行中 | 0.4% (24/6103), ~2.31s/it |
| ngram_uniform_seed42 | ✅ 运行中 | 0.4% (25/6103), ~2.08s/it |

### uniform_1_7b_seed42 失败原因

```
FileNotFoundError: [Errno 2] No such file or directory:
'/root/autodl-tmp/provenance_weight_training/output/models/uniform_1_7b_seed42/checkpoint-3000/trainer_state.json'
```

该任务试图从 checkpoint-3000 恢复训练，但该 checkpoint 不存在。tmux 中也无对应 session（已退出）。GPU 0 空闲。

---
