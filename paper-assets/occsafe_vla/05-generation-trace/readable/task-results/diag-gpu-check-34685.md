# diag gpu check 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_gpu-check-34685_20260528T182137_result.json`
- **Structured JSON:** [`db576f8bde121c5c4a7b.json`](../../sessions/db/db576f8bde121c5c4a7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-34685 GPU 状态：**

| 项目 | 值 |
|------|-----|
| 可见 GPU | **1 张**（仅 GPU 0） |
| 型号 | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| 总显存 | 97,887 MiB (~96 GB) |
| 已用显存 | 0 MiB |
| GPU 利用率 | 0% |
| 运行进程 | **无** |

注意：约束 C001 写的是 cuda:0-3（4张），但实际只看到 1 张 GPU。项目目录 `/root/occsafe_vla/` 已存在，内含代码和数据。

---
