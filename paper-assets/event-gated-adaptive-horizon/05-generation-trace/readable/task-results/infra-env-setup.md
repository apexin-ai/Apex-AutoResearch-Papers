# infra env setup

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_env-setup_20260513T012611_result.json`
- **Structured JSON:** [`617d814165725f3a0744.json`](../../sessions/61/617d814165725f3a0744.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`autodl-rtx6000` 别名现在可以正常连接了。

---

## 环境搭建完成 - 汇报

### GPU 信息
- 2× NVIDIA RTX PRO 6000 Blackwell Server Edition (96GB VRAM each)
- Driver: 595.58.03, CUDA Toolkit: 12.8

### 环境信息
- Python 3.12.3 (conda base, `/root/miniconda3`)
- PyTorch 2.10.0+cu128, CUDA 可用
- 所有依赖已装：gym 0.22.0, dm_control 1.0.41, mujoco 3.8.1, einops, ruamel.yaml, wandb, matplotlib, moviepy, crafter, opencv-python, tensorboard

### Dry-run 结果
- **通过** — 训练跑到 step 100，评估完成
- `eval_return=30.7, eval_length=500.0, eval_episodes=10.0`
- 模型参数：model_opt 16.5M, actor_opt 1.1M, value_opt 1.2M

### 修复的问题
1. **SSH 认证**：autodl-rtx6000 配置中缺少密码，已用 bjb1-45299 的加密密码更新
2. **OSMesa/libstdc++**：conda 的 libstdc++ 缺少 GLIBCXX_3.4.30，需 `LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6`
3. **torch.compile bug**：PyTorch 2.10 的 `duplicate template name` 断言错误，需 `--compile False`
4. 安装了 `libosmesa6-dev libgl1-mesa-glx libglfw3` 系统包

### 环境激活命令（后续 Worker 使用）
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libstdc++.so.6 && \
export MUJOCO_GL=osmesa && \
export PYOPENGL_PLATFORM=osmesa
```

### 注意事项
- `--compile False` 必须传给 dreamer.py，否则 torch.compile 会报错
- pip 安装前需 `source /etc/network_turbo`
- 项目路径：`/root/autodl-tmp/event-gated-adaptive-horizon`
- 数据盘 250GB 可用

---
