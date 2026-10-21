# code openvla crm eval prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openvla-crm-eval-prep_20260520T192044_result.json`
- **Structured JSON:** [`4b36b38afaa61a875bbd.json`](../../sessions/4b/4b36b38afaa61a875bbd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 完整验证通过。以下是总结。

---

## 结果

### 代码修改（已应用）

在 `evaluate.py` 上做了 7 处 patch，添加 OpenVLA 支持：
1. `--openvla` flag + `--openvla_path` 参数
2. `select_action_crm_openvla()` — OpenVLA 单步预测 + CRM obs_only 矫正
3. `select_action_openvla_only()` — OpenVLA baseline（无 CRM）
4. 条件 VLA 加载（OpenVLA vs SmolVLA）
5. `h_eff` 参数化（OpenVLA=1, SmolVLA=5），影响 CGS 和 CRM 的 action_dim
6. vla_only dispatch 分支
7. crm_obs_only dispatch 分支

备份在 `/root/acr-vla-conformal-refinement/src/evaluate.py.bak2`。

### 完整 eval 命令

**CRM obs_only (主实验)**：
```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/acr-vla-conformal-refinement/src && \
CUDA_VISIBLE_DEVICES=0 python evaluate.py \
  --openvla \
  --mode crm_obs_only \
  --benchmark object \
  --checkpoint /root/autodl-tmp/checkpoints/crm_openvla_obs_only/crm_best.pt \
  --obs_dim 4096 \
  --K 1 \
  --seed 42 \
  --n_rollouts 10 \
  --max_correction_norm 0.2 \
  --output_file logs/eval_object_crm_obs_only_openvla_norm0.2_seed42.json
```

**OpenVLA baseline (对照)**：
```bash
CUDA_VISIBLE_DEVICES=0 python evaluate.py \
  --openvla \
  --mode vla_only \
  --benchmark object \
  --seed 42 \
  --n_rollouts 10 \
  --output_file logs/eval_object_vla_only_openvla_seed42.json
```

### 关键参数

| 参数 | 值 | 说明 |
|------|-----|------|
| obs_dim | 4096 | OpenVLA Llama-2 hidden_dim |
| K | 1 | 确定性单步预测，无多样本 |
| h_eff | 1 (自动) | 单步 action，非 chunk |
| max_correction_norm | 0.2 | eval 时裁剪（训练默认 1.42） |
| CRM input_dim | 4102 = 6+0+4096 | action + obs_only |

### 运行时间预估

- 模型加载：~30s（OpenVLA 7B → 14.1GB VRAM）
- 每步推理：~0.5s（OpenVLA inference + CRM）
- 每 rollout：~150s（300 steps max）
- 10 tasks × 10 rollouts：**~4-5 小时**

### GPU 建议

单卡 RTX 4090 (24GB) 即可，用 GPU 0 或 3（空闲）。OpenVLA 占 14.1GB + LIBERO env + TF ~4GB，总计 ~18GB。

### 关于 max_correction_norm

CRM 训练时 `max_correction_norm=1.42`，eval 用 0.2 是保守限制。建议同时跑一组 `--max_correction_norm 1.42`（不加该参数即可）对比效果。

---
