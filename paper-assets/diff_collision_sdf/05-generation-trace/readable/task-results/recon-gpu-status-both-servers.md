# recon gpu status both servers

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_recon_gpu-status-both-servers_20260528T090034_result.json`
- **Structured JSON:** [`3f8675bf2fce2762a486.json`](../../sessions/3f/3f8675bf2fce2762a486.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. GPU 使用状态

| 服务器 | GPU | 型号 | 显存占用 | 利用率 |
|--------|-----|------|---------|--------|
| westd-35807 | cuda:0-3 | RTX PRO 6000 (96GB) | 全部 0 MiB | 0% |
| westd-45947 | cuda:0-1 | RTX PRO 6000 (96GB) | 全部 0 MiB | 0% |

**6 张 GPU 全部空闲。**

### 2. 训练/Eval 进程

- **westd-35807**: 有一个 tmux session `train_pi05_a1_spatial_bowl_s0_l005`，但训练已完成（30000/30000 steps, EXIT_CODE=0，5月27日 06:28 完成）。有两个残留的 multiprocessing spawn 子进程（无 GPU 占用）。无 eval 进程。
- **westd-45947**: 无任何 python/训练/eval 进程。

### 3. Phase 2 s2_v4 Checkpoint

`/root/colliforce-vla/checkpoints/pi05_a1_phase2_lambda0_s2/` **不存在**。Phase 2 相关 checkpoints 在 `/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/` 下有：
- `phase2_lambda0_s0_stage1`
- `phase2_stage1_seed0_l005`
- `phase2_stage1_seed0_l005_v3`

无 s2 的 Phase 2 checkpoint。

### 4. 30K Checkpoint 分布

**LoRA baseline (30K)**:

| Checkpoint | westd-35807 | westd-45947 |
|-----------|:-----------:|:-----------:|
| lora_baseline_object_pudding_seed0 | ✓ | ✓ |
| lora_baseline_object_pudding_seed1 | ✗ | ✓ |
| lora_baseline_object_pudding_seed2 | ✗ | ✓ |
| lora_baseline_spatial_bowl_seed0 | ✓ | ✗ |

**SDF λ=0.01 (30K)**:

| Checkpoint | westd-35807 | westd-45947 |
|-----------|:-----------:|:-----------:|
| object_pudding_seed0_l01 | ✓ | ✓ |
| object_pudding_seed1_l01 | ✓ | ✓ |
| object_pudding_seed2_l01 | ✓ | ✗ |

**SDF λ=0.005 (30K)**:

| Checkpoint | westd-35807 | westd-45947 |
|-----------|:-----------:|:-----------:|
| object_pudding_seed{0,1,2}_l005 | ✓ | ✓ |
| spatial_bowl_seed0_l005 | ✓ | ✗ |

**SDF λ=1.0 (30K)**:

| Checkpoint | westd-35807 | westd-45947 |
|-----------|:-----------:|:-----------:|
| object_pudding_seed0_l1 | ✓ | ✓ |
| object_pudding_seed1_l1 | ✓ | ✗ |
| object_pudding_seed2_l1 | ✗ | ✓ |

**A3 grad_refine (30K)**: 仅 westd-45947 有 spatial_bowl_seed0 和 object_pudding_seed0。

### 5. Eval 命令格式

主 eval 脚本：`scripts/eval_pi05_safelibero.py` — 通过 websocket 连接已运行的 `serve_policy.py` 服务器。

批量 eval 脚本：
```bash
bash scripts/eval_batch.sh \
  --checkpoint_root /root/autodl-tmp/checkpoints/ \
  --methods "baseline a1" \
  --scenes "spatial_bowl object_pudding" \
  --seeds "0 1" \
  --n_episodes 50 \
  --gpu 0 \
  --step 30000
```

---
