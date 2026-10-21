# data libero download

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_libero-download_20260513T035457_result.json`
- **Structured JSON:** [`6cb34ea8727715429b7d.json`](../../sessions/6c/6cb34ea8727715429b7d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 LIBERO 数据完整下载且结构验证通过。

## 产出总结

### 1. 数据状态（全部完整）

| Benchmark | 文件数 | 总大小 | 每文件 demos |
|-----------|--------|--------|-------------|
| libero_spatial | 10 | 5.81 GB | 50 |
| libero_object | 10 | 6.93 GB | 50 |
| libero_10 | 10 | 12.79 GB | 50 |
| libero_goal | 10 | 5.94 GB | 50 |
| libero_90 | 90 | 62.08 GB | 50 |
| **总计** | **130** | **~93.5 GB** | |

### 2. Action shape: **7D** (`(T, 7)`, float64)
含义：6D pose (3D position + 3D orientation) + 1D gripper

### 3. Observation keys

| Key | Shape | Dtype |
|-----|-------|-------|
| `agentview_rgb` | (T, 128, 128, 3) | uint8 |
| `eye_in_hand_rgb` | (T, 128, 128, 3) | uint8 |
| `ee_pos` | (T, 3) | float64 |
| `ee_ori` | (T, 3) | float64 |
| `ee_states` | (T, 6) | float64 |
| `gripper_states` | (T, 2) | float64 |
| `joint_states` | (T, 7) | float64 |

其他 top-level keys: `robot_states (T, 9)`, `states (T, 47~110)`, `rewards`, `dones`

### 4. 磁盘
数据盘 250GB，已用 97GB（含 93.5GB LIBERO 数据），剩余 **154GB**。

### 5. 无 `.incomplete` 文件，数据干净，无需补下载。

---
