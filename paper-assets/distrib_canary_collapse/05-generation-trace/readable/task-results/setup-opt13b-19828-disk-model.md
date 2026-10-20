# setup opt13b 19828 disk model

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_opt13b_19828_disk_model_20260519T153016_result.json`
- **Structured JSON:** [`06c8d04d4b9aa0472673.json`](../../sessions/06/06c8d04d4b9aa0472673.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

| 项目 | 状态 |
|------|------|
| 磁盘 | 27G 可用 / 250G（未清理，空间充足） |
| OPT-1.3B | 已下载到 HF cache，1.32B params，fp32 |
| cuda:0 | **空闲**（0 MiB used / 97887 MiB） |
| cuda:1 | 占用中（64685 MiB / 97887 MiB） |

OPT-1.3B 模型缓存不额外占磁盘（HF cache 之前就 40G，模型 ~2.6G 被吸收进去，df 显示 used 没变是因为四舍五入到 224G）。s43 fp32 实验可直接在 cuda:0 上跑。

---
