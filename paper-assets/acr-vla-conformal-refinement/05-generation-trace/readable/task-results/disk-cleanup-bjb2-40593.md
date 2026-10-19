# disk cleanup bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_disk-cleanup_bjb2-40593_20260520T104143_result.json`
- **Structured JSON:** [`9f32a8891a74b15b90d6.json`](../../sessions/9f/9f32a8891a74b15b90d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**结论：90% 的 `/dev/sda2` 是 AutoDL 宿主机系统盘，以只读方式挂载 NVIDIA 驱动到容器内，容器内无法清理。**

用户可控的两块盘：

| 分区 | 大小 | 已用 | 使用率 |
|------|------|------|--------|
| overlay `/` (根分区) | 30G | 8.9G | **30%** |
| /dev/md0 `/root/autodl-tmp` (数据盘) | 250G | 99G | **40%** |

主要占用：
- `/root/autodl-tmp/libero_data` — 94G（数据集）
- `/root/miniconda3` — 14G（conda 环境）
- `/root/autodl-tmp/models` — 1.8G

这两块盘都远低于 70%，不需要清理。`/dev/sda2` 的 90% 是宿主机层面的问题，需要 AutoDL 平台侧处理，容器内无法干预。

---
