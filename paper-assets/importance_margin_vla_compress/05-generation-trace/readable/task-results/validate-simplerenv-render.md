# validate simplerenv render

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_validate_simplerenv_render_20260524T164831_result.json`
- **Structured JSON:** [`bf3c8d9ba92d9eba216d.json`](../../sessions/bf/bf3c8d9ba92d9eba216d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**✅ 渲染通过** — SimplerEnv 在 westd-27271 上可以 headless 渲染，后续 pruning eval 可行。

但有一个重要限制需要注意：

### 通过路径
- **ManiSkill3 分支** (`maniskill3`) + `sapien==3.0.3` + `mani-skill==3.0.1`，在 conda base (Python 3.12) 下运行
- 4 个 WidowX Bridge 环境全部通过，输出 480×640 RGB 图像
- 环境变量：`VK_ICD_FILENAMES=/etc/vulkan/icd.d/nvidia_icd.json NVIDIA_DRIVER_CAPABILITIES=all`

### 失败路径（已排除）
- **SAPIEN 2.2.2**（ManiSkill2 主分支）：`camera.take_picture()` segfault，RTX PRO 6000 Blackwell + driver 580 不兼容，无法修复

### 限制
- ManiSkill3 只移植了 **4 个 Bridge 环境**（PutCarrot, PutSpoon, StackCube, PutEggplant），**无 Google Robot 环境**（Pick Coke Can, Open Drawer 等不可用）
- obs_mode 只支持 `'rgb+segmentation'`，不支持 `'rgbd'`
- obs 路径：`obs['sensor_data']['3rd_view_camera']['rgb']`

### 下一步
需要决策：4 个 Bridge tasks 是否足够做 SimplerEnv eval，还是必须想办法获取 Google Robot 环境（可能需要旧驱动的服务器或等待 ManiSkill3 移植）。

---
