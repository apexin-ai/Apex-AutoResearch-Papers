# ssh westd45947 env setup

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd45947_env_setup_20260520T030342_result.json`
- **Structured JSON:** [`9000035c10bd7ab8c21d.json`](../../sessions/90/9000035c10bd7ab8c21d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 环境搭建完成

### 汇报

| 项目 | 状态 |
|------|------|
| **镜像** | 非 aml-train（原生 AutoDL 镜像，带 miniconda3） |
| **Python** | 3.12.3 (conda base) |
| **CUDA** | 12.8 (nvcc V12.8.93), Driver 595.58.03 |
| **PyTorch** | 2.8.0+cu128 |
| **GPU** | 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (94GB each) ✓ |
| **根分区** | 30G，已用 4G，剩 27G |
| **数据盘** | /root/autodl-tmp 250G，已用 15G，剩 236G |

### 已安装依赖

| 包 | 版本 |
|----|------|
| torch | 2.8.0+cu128 |
| transformers | 4.53.2 |
| einops | 0.8.2 |
| accelerate | 1.13.0 |
| jaxtyping | 0.2.36 |
| pysdf | 0.1.9 |
| mujoco | 3.8.1 |
| robosuite | 1.4.0 |
| wandb | 0.27.0 |

### 注意事项

1. **Python 版本差异**：此服务器 Python 3.12，westd-35807 用 3.10。目前所有依赖都正常工作。
2. **robosuite 需要环境变量**：已写入 `.bashrc`，运行时需要 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 MUJOCO_GL=osmesa PYOPENGL_PLATFORM=osmesa`（conda 的 libstdc++ 版本过低）。
3. **项目代码已存在**：`/root/colliforce-vla` 已有代码（LIBERO, colliforce, openpi 等）。
4. **目录已创建**：`/root/autodl-tmp/logs`、`/root/autodl-tmp/checkpoints` 就绪。

---
