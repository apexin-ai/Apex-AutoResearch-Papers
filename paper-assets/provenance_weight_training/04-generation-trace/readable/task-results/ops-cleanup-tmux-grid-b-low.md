# ops cleanup tmux grid b low

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cleanup_tmux_grid_b_low_20260515T215342_result.json`
- **Structured JSON:** [`9603b1eef971e21d9ced.json`](../../sessions/96/9603b1eef971e21d9ced.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**发现：`grid_b_low_seed42_r3` 中有活跃训练进程，不能 kill。**

进程树：
- `timeout 57600` → `bash run_grid_b_low_seed42.sh` → **`python training/pretrain_weighted.py`**（CPU 99%，刚启动于 05:53）
- 训练参数：`grid_b_low_b0.1_seed42`，200M tokens，seed42

这个 session 是刚创建的（今天 05:53），训练正在进行中。

**GPU 状态：**
| GPU | 显存占用 | 总显存 |
|-----|---------|--------|
| 0 | 46,523 MiB | 97,887 MiB |
| 1 | 46,523 MiB | 97,887 MiB |
| 2 | 81,705 MiB | 97,887 MiB |
| 3 | 46,523 MiB | 97,887 MiB |

**结论：**
- 只有 1 个 grid_b_low 相关 session（`grid_b_low_seed42_r3`），且正在活跃训练，**未执行 kill**
- cuda:0 不空闲（46.5GB 占用），4 块 GPU 全部在使用中
- 另外还有一个 `contamination_60_seed42_r2` 训练进程也在运行

需要等当前训练完成后再清理，还是要强制终止？

---
