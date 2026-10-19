# ops download pi05 and study eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_download_pi05_and_study_eval_20260522T092826_result.json`
- **Structured JSON:** [`3975811ac1c3d30982c0.json`](../../sessions/39/3975811ac1c3d30982c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

下载继续中。注意到 gcsfs 创建了嵌套的 `params/params/` 目录结构，下载完后需要修正。

现在给出完整分析结果：

---

## 产出报告

### 1. pi0.5 checkpoint 下载状态

- **状态**: 下载中 (PID 368719)，当前 ~1.3GB
- **格式**: JAX ocdbt sharded (非 PyTorch `model.safetensors`)
- **路径**: `/root/autodl-tmp/openpi_weights/pi05_libero/`
- **预估大小**: 与 pi0_base (14GB) 相当，需要较长时间
- **问题**: gcsfs 创建了嵌套 `params/params/` 目录，下载完成后需要修正

> **重要发现**: pi0_base 是 PyTorch 格式 (`model.safetensors`)，pi0.5 是 JAX 格式 (`params/` ocdbt shards)。当前 `eval_safelibero.py` 的 `create_trained_policy()` 会自动检测格式，走 JAX 路径需要 JAX 环境。

### 2. 磁盘空间

`/root/autodl-tmp`: 250GB 总量, 82GB 已用, **169GB 可用** — 充足。

### 3. 官方 eval action 处理流程

`openpi/examples/libero/main.py` 逐步：

1. **渲染图像**: env 以 256×256 渲染 → `image_tools.resize_with_pad` 缩放到 224×224
2. **构建 state**: `ee_pos(3) + _quat2axisangle(ee_quat)(3) + gripper_qpos(2)` = 8D
3. **构建 input dict**: `{"observation/image", "observation/wrist_image", "observation/state", "prompt"}`
4. **推理**: `client.infer(element)["actions"]` → 返回 action chunk (多步)
5. **Action chunk 处理**: 取前 `replan_steps=5` 步放入 deque，每步 popleft 一个 action
6. **执行**: `env.step(action.tolist())` — 7D action (pos_delta(3) + ori_delta(3) + gripper(1))
7. **Re-plan**: 5 步用完后重新推理
8. **Normalization**: 在 server 端由 `transforms.Unnormalize` 自动完成，client 拿到的已经是原始 action space

关键参数：
- warm-up: 10 步 `[0]*6 + [-1.0]` (gripper closed)
- seed: 7, 且显式 `env.seed(7)`
- max_steps: spatial=220, object=280, goal=300

### 4. 差异清单 (官方 vs eval_safelibero.py)

| 维度 | 官方 eval | 我们的 eval | 影响 |
|------|-----------|------------|------|
| **Action chunking** | `replan_steps=5`, 每 5 步 re-plan | **每步都 re-plan**, 取 `actions[0]` | **HIGH** — 改变 temporal execution pattern |
| **Image 渲染分辨率** | 256→resize to 224 | 直接 224 渲染 | **MEDIUM** — 像素级不同 |
| **Warm-up** | 10 步, gripper=-1 | 50 步, action=zeros (gripper=0) | **LOW-MED** — 初始状态可能略不同 |
| **Max steps** | suite-specific (spatial=220) | 固定 default=300 | **LOW** — 我们给更多步，不会更差 |
| **Seed** | default 7 + `env.seed()` | default 0, 无 `env.seed()` | **LOW** — 影响初始状态采样 |
| **Orientation conversion** | 手写 `_quat2axisangle` | `scipy Rotation.as_rotvec()` | **NONE** — 数学等价 |
| **Normalization** | server 端 Unnormalize | `policy.infer()` 内含 Unnormalize | **NONE** — 等价 |
| **Success check** | `done` from env.step | `env.check_success()` | **NONE** — 等价 |

### 5. 建议修复项

**必须修 (影响结果一致性)**:
1. **加 action chunking**: 加 `replan_steps` 参数，用 deque 缓存 action chunk，每 N 步 re-plan 一次（匹配官方 default=5）

**建议修 (对齐官方)**:
2. **渲染分辨率**: 改为 `camera_heights=256, camera_widths=256`，推理前 resize 到 224
3. **Warm-up**: 改为 10 步 + gripper closed (`[0]*6 + [-1.0]`)
4. **env.seed()**: 添加 `env.seed(args.seed)`
5. **Suite-specific max_steps**: 添加默认值映射，或保留 300 统一上限

---
