# ssh launch a1 lora spa and check eval

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_launch_a1_lora_spa_and_check_eval_20260521T064930_result.json`
- **Structured JSON:** [`c14994061ad44aca9a56.json`](../../sessions/c1/c14994061ad44aca9a56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常推进，step 2/30000，cuda:0 占用 16.9GB。

---

## 汇报

### 1. A1 LoRA spatial_bowl 训练状态

| 项目 | 值 |
|------|-----|
| PID | **299910** |
| GPU | cuda:0，16873 MiB / 97887 MiB |
| tmux | `a1_lora_spa` |
| 进度 | 2/30000，~7.9s/it |
| 日志 | `/root/autodl-tmp/colliforce-outputs/a1_lora_spa_s0/train.log` |
| exp_name | `a1_lora_spatial_bowl_seed0` |

### 2. Eval 是否支持 CPU-only

**不建议 CPU-only 运行。** 证据：

- `eval_safelibero.py:712` — 内部设 `CUDA_VISIBLE_DEVICES=str(args.gpu)`
- `eval_safelibero.py:736` — `device = "cuda:0" if torch.cuda.is_available() else "cpu"`，技术上有 CPU fallback
- `eval_safelibero.py:713` — `MUJOCO_GL=egl`，LIBERO 仿真依赖 EGL GPU 渲染
- 模型推理（pi0 ~7GB）在 CPU 上会极慢

**GPU 共享可行**：`--gpu N` 指定设备。cuda:0 当前占 16.9GB / 98GB，剩余 ~80GB，足够同时跑 eval（模型 ~7GB + 仿真开销）。但建议等训练完或用其他空闲卡。

### 3. baseline_spatial_bowl checkpoint

路径：`/root/autodl-tmp/checkpoints/baseline_spatial_bowl/baseline_spatial_bowl_seed0/best/`

| 文件 | 大小 |
|------|------|
| model.safetensors | 7.0 GB |
| optimizer.pt | 12.5 GB |
| metadata.pt | 3.2 KB |
| best_loss.txt | 0.00316 @ step 30000 |

checkpoint 完整，可用于 eval。另有 `29999/` 和 `30000/` 两个中间 checkpoint。

---
