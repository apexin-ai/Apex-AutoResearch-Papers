# ssh critical disk cleanup 35807

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_critical_disk_cleanup_35807_20260520T071607_result.json`
- **Structured JSON:** [`49e559e73698a3e5ed5b.json`](../../sessions/49/49e559e73698a3e5ed5b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。

**清理前后对比：**

| | Used | Avail | Use% |
|---|---|---|---|
| 清理前 | 254G | 97G | 73% |
| 清理后 | 144G | 207G | 42% |

**释放 ~110GB**，删除了 6 个 checkpoint 目录：
- `baseline_spatial_bowl_seed0/2000` + `4000` (~38GB)
- `baseline_spatial_bowl_seed1/2000` + `4000` (~38GB)
- `baseline_object_pudding_seed0/2000` + `4000` (~38GB)

**保留的 checkpoint：**
- 3 个 baseline 各保留 step 6000 + 8000（最新 2 个）
- A1 保留 step 5000 + 6000（本来就只有 2 个）

当前可用 **207GB**，足够支撑到 step 20000+。

---
