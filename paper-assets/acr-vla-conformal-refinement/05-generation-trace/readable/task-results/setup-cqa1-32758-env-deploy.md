# setup cqa1 32758 env deploy

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_setup_cqa1-32758-env-deploy_20260523T072225_result.json`
- **Structured JSON:** [`06f0b87c9ed2308bffb5.json`](../../sessions/06/06f0b87c9ed2308bffb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All experiments running correctly. Here's the final report:

---

## 部署报告 — cqa1-32758 K=2 Mean 实验

### 环境
- **Python**: 3.12.3 (miniconda3 conda base)
- **PyTorch**: 2.8.0+cu128, CUDA 12.8
- **GPU**: 6× RTX 4090D 24GB, Driver 580.105.08
- **关键包**: lerobot==0.5.1, libero==0.1.1, transformers==5.9.0, robosuite==1.4.0, wandb==0.27.0, draccus==0.10.0, num2words==0.5.14

### 代码同步
- 方式: tar + scp from bjb2-40593
- 路径: `/root/acr-vla-conformal-refinement/`
- K=2 fix 已验证: `grep "args.K = 10"` 无结果

### 模型
- SmolVLA: `/root/autodl-tmp/models/smolvla_libero/` (865M)
- SmolVLM2 config: `/root/autodl-tmp/models/SmolVLM2-500M-Video-Instruct/`

### 额外修复
- `MUJOCO_GL=egl` + 安装 `libegl1` 解决 EGL 渲染问题
- 手动创建 `~/.libero/config.yaml` 跳过交互式 prompt
- 从 bjb2 SCP LIBERO assets (226M) 解决缺失场景文件
- 从 Aliyun 镜像安装大部分包，lerobot 单独从 pypi.org `--no-deps` 安装

### 6 个 tmux 实验

| Session | GPU | Benchmark | Seed | PID | 状态 |
|---------|-----|-----------|------|-----|------|
| k2mean_spatial_s43 | cuda:0 | spatial | 43 | 16439 | rollout 5/20, 5/5 success |
| k2mean_spatial_s44 | cuda:1 | spatial | 44 | 16437 | rollout 5/20, 5/5 success |
| k2mean_object_s43 | cuda:2 | object | 43 | 16441 | running (tasks loaded) |
| k2mean_object_s44 | cuda:3 | object | 44 | 16443 | running (tasks loaded) |
| k2mean_goal_s43 | cuda:4 | goal | 43 | 16445 | running (tasks loaded) |
| k2mean_goal_s44 | cuda:5 | goal | 44 | 16447 | running (tasks loaded) |

### GPU 使用
全部 6 张 GPU 占用 5.7-6.5 GiB，利用率 8-30%。

---
