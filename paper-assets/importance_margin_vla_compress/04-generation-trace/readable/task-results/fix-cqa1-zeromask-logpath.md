# fix cqa1 zeromask logpath

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1-zeromask-logpath_20260525T182525_result.json`
- **Structured JSON:** [`eee9360328b52b33ded5.json`](../../sessions/ee/eee9360328b52b33ded5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

- Symlink 已建立：`~/runs/.../eval_pi05_zeromask_random_k09_object_seed42.log` → `/tmp/eval_pi05_zeromask_random_k09_object_seed42.log`
- Registry `log_path` 已更新为 `/root/runs/importance_margin_vla_compress/eval_pi05_zeromask_random_k09_object_seed42.log`
- 日志可正常读取（最后输出：模型 4143.4M 参数，ZERO-MASK random 模式，keep 230/256 tokens）

注意：日志自 02:21 后无新输出（~6 分钟），进程仍在（PID 617871）。可能在 torch.compile 或第一个 episode 推理中，建议稍后再查。

---
