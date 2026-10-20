# research find libero rlds data

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_find_libero_rlds_data_20260527T155523_result.json`
- **Structured JSON:** [`8fa34e85827f76e3064d.json`](../../sessions/8f/8fa34e85827f76e3064d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

确认了问题：**object/goal/10 的 tfrecord 文件是 git-lfs 指针（~148K/84K），未拉取实际数据。** 只有 spatial（1.8G）已拉取。

## 汇报

### 1. 预转换 RLDS 数据已找到

来源：[openvla/modified_libero_rlds](https://huggingface.co/datasets/openvla/modified_libero_rlds) — 包含全部 4 个 suite 的 RLDS tfrecord（~10GB 总计）。

### 2. 两台服务器现状

| 数据集 | westd-10894 | westd-34685 | 状态 |
|--------|-------------|-------------|------|
| `libero_spatial_no_noops` | 1.8G (16 shards) | — | 真实数据 |
| `libero_object_no_noops` | 148K (32 shards) | 148K | **git-lfs 指针未拉取** |
| `libero_goal_no_noops` | 84K (16 shards) | 84K | **git-lfs 指针未拉取** |
| `libero_10_no_noops` | 148K (32 shards) | — | **git-lfs 指针未拉取** |

repo 已 clone 在 `/root/autodl-tmp/data/modified_libero_rlds/`，只需执行 **`git lfs pull`** 即可拉取实际数据。

### 3. 最快行动方案

在两台服务器的 `/root/autodl-tmp/data/modified_libero_rlds/` 下执行：
```bash
cd /root/autodl-tmp/data/modified_libero_rlds && git lfs pull
```

预计下载量 ~8GB（spatial 已有），时间取决于网络速度（AutoDL 需先 `source /etc/network_turbo`）。代码已有完整的 dataset config（`libero_object_no_noops` / `libero_goal_no_noops`），数据就位后可直接训练。

### 4. 预估时间

- git lfs pull: 10-30 分钟（视网络）
- 拉取完成后：**立即可以开始训练**，无需任何 RLDS 转换

### 5. HDF5 替代方案

代码库中无 h5py/HDF5 相关代码，openvla-oft 只支持 RLDS 格式，无 HDF5 直接训练路径。

**建议立即在两台服务器上执行 `git lfs pull`。** 是否执行？

---
