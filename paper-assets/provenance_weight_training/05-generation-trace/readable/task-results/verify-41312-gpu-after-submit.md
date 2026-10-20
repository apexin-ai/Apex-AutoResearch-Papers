# verify 41312 gpu after submit

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_41312_gpu_after_submit_20260518T145217_result.json`
- **Structured JSON:** [`7279755410228eeb05cd.json`](../../sessions/72/7279755410228eeb05cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 🔴 全部 4 个任务启动失败

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| GPU 0 | **0 MiB** / 97887 MiB | ❌ 空闲 |
| GPU 1 | **0 MiB** / 97887 MiB | ❌ 空闲 |
| GPU 2 | **0 MiB** / 97887 MiB | ❌ 空闲 |
| GPU 3 | **0 MiB** / 97887 MiB | ❌ 空闲 |

**失败原因：磁盘空间不足**

所有 4 个任务都因相同错误退出：
```
OSError: [Errno 28] No space left on device: '/root/autodl-tmp/output'
EXIT_CODE=1
```

- `uniform_1_7b_seed42` — ❌ EXIT_CODE=1
- `adaptive_1_7b_seed42` — ❌ EXIT_CODE=1
- `ngram_adaptive_seed42` — ❌ EXIT_CODE=1
- `ngram_uniform_seed42` — ❌ EXIT_CODE=1

无 tmux session 运行，无 python 进程存活。

需要清理 `/root/autodl-tmp/` 的磁盘空间后重新启动任务。

---
