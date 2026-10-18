# fix cqa1 gpu1 kill duplicate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-gpu1-kill-duplicate_20260525T215701_result.json`
- **Structured JSON:** [`5e7f976274f0751fe71b.json`](../../sessions/5e/5e7f976274f0751fe71b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：

- **PID 790989 存活** — 正在运行 `eval_pi05_pruning_libero.py --prune_mode l2norm --keep_ratio 0.75 --suite libero_10`（GPU 0）
- **GPU1 显存已回落** — 从 ~20GB 降至 10483 MiB（单进程水位），重复进程已清除
- **tmux session** — 仅剩 `eval_pi05_l2norm_k075_long_seed42_v2`（1 window），重复 session 已消失

---
