# ssh kill and restart 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill-and-restart-34685_20260528T230832_result.json`
- **Structured JSON:** [`fbb16aac69f3b8302da1.json`](../../sessions/fb/fbb16aac69f3b8302da1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**全部验证通过。最终判定：成功。**

| 检查项 | 结果 |
|--------|------|
| GPU 僵尸进程清理 | westd-34685 GPU 已清空（0 MiB → 重启后 63940 MiB） |
| tmux session | `full_occ_bn_v2_s2_r5` 存在，TMUX_OK |
| 进程存活 | PID 30149，占用 63940 MiB GPU 显存 |
| Occ 数据加载 | Occ preload done: 9 files, 55370 条目 |
| occ_loss | step=0, occ_loss=0.1422 > 0 |
| 错误/异常 | 无 traceback、无 exception |
| 训练速度 | ~1.03 s/it，已到 step 14，预计约 14.4h 完成 50005 步 |

---
