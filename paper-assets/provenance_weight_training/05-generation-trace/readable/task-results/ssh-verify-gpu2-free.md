# ssh verify gpu2 free

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_gpu2_free_20260515T184550_result.json`
- **Structured JSON:** [`631fa621ca1d3f84b692.json`](../../sessions/63/631fa621ca1d3f84b692.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 2 状态：已完全释放，可立即使用。**

| 项目 | 状态 |
|------|------|
| GPU 2 显存 | **0 MiB / 97887 MiB**（完全空闲） |
| GPU 2 进程 | 无任何计算进程 |
| GPU 2 温度 | 34°C（空闲态） |
| 旧目录 `bs8_nmin2_seed42/` | 存在，仅含 1 个 `config.json`（266 bytes） |

其他 GPU 状态：GPU 0/1/3 各有训练进程运行中（~46GB 显存，97-99% 利用率）。

旧目录只有一个小配置文件，要清理掉吗？

---
