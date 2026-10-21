# ssh libero goal download

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_libero-goal-download_20260515T160047_result.json`
- **Structured JSON:** [`8de4158fd458d0f94f5f.json`](../../sessions/8d/8de4158fd458d0f94f5f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 报告：LIBERO-Goal 数据集下载与验证

### 下载结果
10/10 HDF5 文件下载成功，存放于 `/root/autodl-tmp/vla-ssd/data/libero/libero_goal/`，总计 **5.94 GB**。

关键发现：AutoDL proxy (`network_turbo`) 会严重干扰 HuggingFace XET bridge 下载。**绕过 proxy 直接连接**后，下载速度从 35KB/s 提升至 ~30MB/s。

### 数据格式
与 libero_10 **完全一致**：
- `agentview_rgb`: (T, 128, 128, 3) uint8
- `eye_in_hand_rgb`: (T, 128, 128, 3) uint8
- `actions`: (T, 7) float64
- obs keys: `agentview_rgb, ee_ori, ee_pos, ee_states, eye_in_hand_rgb, gripper_states, joint_states`
- 每个文件 50 个 demo，共 500 个 demo
- `language_instruction` 存储在 `problem_info` attrs 中

### 10 个任务
| 任务 | 平均 episode 长度 |
|------|-------------------|
| open the middle drawer of the cabinet | 141 |
| open the top drawer and put the bowl inside | 204 |
| push the plate to the front of the stove | 153 |
| put the bowl on the plate | 93 |
| put the bowl on the stove | 102 |
| put the bowl on top of the cabinet | 102 |
| put the cream cheese in the bowl | 107 |
| put the wine bottle on the rack | 176 |
| put the wine bottle on top of the cabinet | 108 |
| turn on the stove | 89 |

Episode 长度范围：75-347，均值 127.5

### 场景共享
LIBERO-Goal 所有 10 个任务共享同一个厨房初始场景，仅目标指令不同。

### Pipeline 兼容性
`extract_features.py` **完全兼容**：
- `task_desc_from_filename()` 的 fallback 分支正确处理无 SCENE 前缀的文件名，10/10 映射结果与 `language_instruction` 属性一致
- 数据结构（obs keys、image shape、action dim）与 libero_10 完全匹配
- 使用方式：`--data_dir /root/autodl-tmp/vla-ssd/data/libero/libero_goal/`

### 磁盘使用
- libero_goal: 6.0 GB
- 数据盘剩余: 83 GB (68% 使用)

---
