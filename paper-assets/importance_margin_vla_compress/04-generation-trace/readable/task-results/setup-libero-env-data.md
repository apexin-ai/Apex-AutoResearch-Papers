# setup libero env data

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_libero_env_data_20260516T125821_result.json`
- **Structured JSON:** [`7697bcf899be116eb4b5.json`](../../sessions/76/7697bcf899be116eb4b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成状态

### 1. LIBERO 安装 ✅
| 包 | 版本 |
|---|---|
| libero | 0.1.1 |
| robosuite | 1.4.0 |
| mujoco | 3.8.1 |

### 2. Assets 下载 ✅
- 585 文件，405MB
- 从 GitHub raw content 逐文件下载（AutoDL 代理导致 tarball/HF 大文件下载不稳定）
- 所有 MuJoCo 场景 XML、物体模型、纹理齐全

### 3. Benchmark Suites ✅
| Suite | Tasks |
|---|---|
| libero_spatial | 10 |
| libero_object | 10 |
| libero_goal | 10 |
| libero_10 | 10 |
| libero_90 | 90 |

### 4. 环境验证 ✅
```
观测空间:
  agentview_image: (256, 256, 3) uint8
  robot0_eye_in_hand_image: (256, 256, 3) uint8
  robot0_eef_pos: (3,), robot0_eef_quat: (4,)
  robot0_gripper_qpos: (2,)
动作空间: 7 维 (6D EEF delta + 1D gripper)
渲染: MUJOCO_GL=egl (headless)
```
环境可正常 create → reset → step → close。

### 5. 数据集下载 ⏳
- `lerobot/libero_10`：60MB 已下载（parquet 文件完成，视频文件因 SSL 超时卡住，后台重试中 PID 195317）
- `HuggingFaceVLA/libero`：需要 HF 认证（401）—— 项目配置中用的是这个 repo_id
- `yifengzhu-hf/LIBERO-datasets`：官方 HDF5 格式数据可用（无需认证）

### 遗留问题
- **数据集认证**：`HuggingFaceVLA/libero` 需要设置 `HF_TOKEN` 或改用公开替代方案（`lerobot/libero_10` 或 `yifengzhu-hf/LIBERO-datasets`）
- **视频文件下载慢**：AutoDL 代理 SSL 超时导致大文件不稳定，后台进程在重试

### 磁盘
122GB 可用（总 250GB，已用 129GB）

---
