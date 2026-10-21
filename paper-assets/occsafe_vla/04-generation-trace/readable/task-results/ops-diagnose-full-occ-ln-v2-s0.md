# ops diagnose full occ ln v2 s0

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose-full_occ_ln_v2_s0_20260526T120557_result.json`
- **Structured JSON:** [`15c23ec4826ce30fe5f2.json`](../../sessions/15/15c23ec4826ce30fe5f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**full_occ_ln_v2_s0 正在运行中，没有退出。**

诊断结果：

- **进程状态**：GPU 1 上有活跃进程 PID 341771，占用 63028MiB 显存
- **当前进度**：step 91/50005（刚启动约 2 分钟）
- **日志**：最后修改时间 20:06:49，无退出文件 `/tmp/agent-ml-exit/full_occ_ln_v2_s0.exit`
- **Checkpoint**：目录下只有 `dataset_statistics.json`，尚未触发任何保存（save_freq=10000）
- **初始 loss**：step=0 时 occ_loss=0.1159, action_loss=0.6836
- **预计完成时间**：按 ~1.09 it/s 估算，约需 12.7 小时（明天早上 ~08:50）

训练刚刚开始，不需要做任何诊断或 registry 更新。当前 4 张 GPU 全部在用：
| GPU | 实验 |
|-----|------|
| 0 | reverse_cutoff_s2_v2 |
| 1 | full_occ_ln_v2_s0 |
| 2 | （未确认，可能是其他实验） |
| 3 | detach_ln_v2_s0 |

---
