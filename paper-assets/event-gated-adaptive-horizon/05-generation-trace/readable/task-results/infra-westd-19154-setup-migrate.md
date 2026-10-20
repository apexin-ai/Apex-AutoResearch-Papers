# infra westd 19154 setup migrate

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_westd_19154_setup_migrate_20260525T044048_result.json`
- **Structured JSON:** [`e8f927a0f4762fe9a9f5.json`](../../sessions/e8/e8f927a0f4762fe9a9f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总报告：

---

### 新服务器 westd-19154 配置结果

| 项目 | 状态 |
|------|------|
| **SSH 密钥认证** | 成功，已配置 `~/.ssh/config` 别名 `westd-19154` |
| **GPU** | 2× NVIDIA RTX PRO 6000 Blackwell Server Edition, 96GB VRAM each |
| **CUDA/PyTorch** | PyTorch 2.8.0+cu128, CUDA 可用, 2 GPU |
| **Python** | 3.12.3 (conda base) |
| **磁盘** | 根分区 30GB (可用 30GB), 数据盘 350GB (可用 350GB) |
| **镜像** | 非 aml-train 镜像，手动安装依赖 |
| **代码迁移** | 成功，从 bjb1-40020 迁移 ~8.5MB 代码（排除 logdir） |
| **依赖安装** | torch, torchvision, torchaudio, wandb, einops, gym, mujoco, dm_control, crafter, opencv, tensorboard, matplotlib, scipy 等全部就绪 |
| **EGL 渲染** | 已安装 libegl1/libegl-dev，需设 `MUJOCO_GL=egl PYOPENGL_PLATFORM=egl` |
| **Dry-run** | 成功 (walker_walk, gate_enabled, 100 updates, eval_return=37.6) |
| **最终状态** | **就绪，可提交实验** |

**注意**：启动训练时需要设置环境变量：
```bash
export MUJOCO_GL=egl
export PYOPENGL_PLATFORM=egl
```

---
