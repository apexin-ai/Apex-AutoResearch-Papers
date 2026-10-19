# prep lambda0 ablation config

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_prep_lambda0_ablation_config_20260524T140932_result.json`
- **Structured JSON:** [`c072044d2b7d176cd92c.json`](../../sessions/c0/c072044d2b7d176cd92c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have the complete picture. Here's the analysis and training command.

---

## 现有 A1 配置确认

从 registry 和 `train_pi05_lora_baseline.py`（同源 fork）确认：

| 参数 | 值 |
|------|-----|
| 脚本 | `scripts/train_a1_sdf_aux_pi05.py` |
| LoRA | PaliGemma rank=16/alpha=16, Action Expert rank=32/alpha=32 |
| LR | 2.5e-5, cosine decay (warmup 1000 steps, decay to lr/10) |
| Phase 1 | 0→5000 steps: backbone+LoRA frozen, only aux heads (SDF decoder + EE extractor) trainable |
| Phase 2 | 5000→30000 steps: unfreeze LoRA, aux heads 继续训练 |
| λ_sdf 传入方式 | `--lambda_sdf` 命令行参数 |
| Loss 公式 | `action_loss + λ_sdf × sdf_total + λ_ee × ee_loss` |
| Batch size | 32 |
| Optimizer | cosine decay schedule |
| 数据集 | safelibero_object (object_pudding) |

## 是否需要代码修改

**不需要。** `--lambda_sdf 0` 直接可用。Loss 公式中 `0 × sdf_total = 0`，SDF loss 项被自然消除。SDF decoder 仍然存在于模型中，SDF forward pass 仍然执行（只是不贡献 gradient）。

## 需要注意的语义

`--lambda_sdf 0` 意味着 **全程** λ_sdf=0：
- **Phase 1**: SDF decoder 虽然存在且 trainable，但因 `0 × sdf_loss = 0`，SDF decoder 实际 **不会收到任何梯度**。只有 EE extractor 通过 `λ_ee × ee_loss` 获得训练。
- **Phase 2**: LoRA 训练 loss = `action_loss + 0.01 × ee_loss`，无 SDF 贡献。

这个 ablation 的实际含义是："没有任何 SDF loss 时（但有 EE loss + 相同的 Phase 1/2 调度），CAR 是否提升？" 对比条件：
- **LoRA baseline** (正在跑): 无 SDF、无 EE
- **λ_sdf=0 ablation**: 无 SDF、有 EE loss
- **λ_sdf=0.005/0.01**: 有 SDF + 有 EE loss

如果你需要的是 "Phase 1 正常预热 SDF decoder（λ_sdf>0），Phase 2 关闭 SDF（λ_sdf=0）"，那需要代码修改（当前脚本 λ_sdf 全程固定）。请确认你要的是哪种。

## 完整训练命令

checkpoint path 自动生成可能产生 `_l0` 而非 `_l000`，用 `--exp_name` 显式指定：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && \
cd /root/colliforce-vla && \
WANDB_MODE=offline PYTHONUNBUFFERED=1 \
python scripts/train_a1_sdf_aux_pi05.py \
  --scene object_pudding \
  --seed 0 \
  --gpu &lt;GPU_ID> \
  --batch_size 32 \
  --num_train_steps 30000 \
  --lambda_sdf 0 \
  --lambda_ee 0.01 \
  --lr 2.5e-5 \
  --save_interval 2000 \
  --exp_name a1_sdf_pi05_object_pudding_seed0_l000 \
  2>&1 | tee /tmp/train_pi05_a1_obj_s0_l000.log
```

GPU 选择：westd-35807 的 cuda:0-3 目前空闲（之前的 A1 实验已完成），westd-45947 的 cuda:0-1 被 LoRA baseline 占用。建议在 westd-35807 上跑，填入具体 GPU 编号。

---
