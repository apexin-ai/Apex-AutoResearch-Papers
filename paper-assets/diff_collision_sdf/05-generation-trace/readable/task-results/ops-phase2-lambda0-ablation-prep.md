# ops phase2 lambda0 ablation prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_phase2_lambda0_ablation_prep_20260525T074355_result.json`
- **Structured JSON:** [`d32a57449e5f6c30db1c.json`](../../sessions/d3/d32a57449e5f6c30db1c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整结果：

---

## 1. 10K checkpoint 不存在

`seed0_l005` 目录**只有 30000/**，没有 10K：
```
/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000/
```

原因：`train_pytorch.py` 的 `save_checkpoint` 函数有 **`SAVE_TOTAL_LIMIT = 2`**，只保留最近 2 个 checkpoint，中间的全部被清理。所有 seed/lambda 组合都只剩 30000/（seed1/2 额外有 29999/ 和 best/）。

## 2. 脚本能力分析

| 功能 | 支持? | 说明 |
|------|-------|------|
| `--lambda_sdf 0` | ✅ | float 参数，直接传 0 即可，loss 公式: `action_loss + lambda_sdf * sdf_total + lambda_ee * ee_loss` |
| `--resume` | ✅ | 自动找 exp_name 目录下最新 checkpoint 恢复 global_step 和 optimizer |
| 指定恢复到特定 step | ❌ | 只能从目录里最大 step 的 checkpoint 恢复 |
| Phase 2 lambda 独立控制 | ❌ | `self.lambda_sdf` 从 args 一次性设置，整个训练周期不变 |

Phase 逻辑：
- Phase 1（step 0 → 5000）：只训 SDF decoder + EE extractor，LoRA 冻结
- Phase 2（step 5000+）：LoRA 解冻，含 100 步 gradient warmup

## 3. 可行方案：两阶段训练

由于 10K checkpoint 已丢失，需要重新训练 Phase 1 → 保存 10K → resume with λ_sdf=0。

### a) Stage 1：训练 10K steps（重建 checkpoint）

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && \
cd /root/colliforce-vla && \
python scripts/train_a1_sdf_aux_pi05.py \
    --scene object_pudding --seed 0 --gpu 0 \
    --num_train_steps 10000 \
    --lambda_sdf 0.005 \
    --save_interval 10000 \
    --exp_name a1_sdf_pi05_object_pudding_seed0_l005_p2abl
```

预计耗时：~8-10h（30K 约 24h，按比例）。产出 checkpoint 在：
`/root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005_p2abl/10000/`

### b) Stage 2：从 10K resume，λ_sdf=0，训到 30K

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && \
cd /root/colliforce-vla && \
python scripts/train_a1_sdf_aux_pi05.py \
    --scene object_pudding --seed 0 --gpu 0 \
    --num_train_steps 30000 \
    --lambda_sdf 0 \
    --save_interval 5000 \
    --resume \
    --exp_name a1_sdf_pi05_object_pudding_seed0_l005_p2abl
```

resume 时 global_step=10000 > warmup_phase_steps=5000 → `on_step_start` 自动触发 Phase 2 → LoRA 解冻。λ_sdf=0 从 args 传入，后续 20K 步 SDF loss 权重为 0。

### c) s0 l005 30K eval

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && \
cd /root/colliforce-vla && \
python scripts/eval_safelibero.py \
    --model_type a1 \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l005/30000 \
    --config_name baseline_object_pudding \
    --suite safelibero_object \
    --task_id 0 \
    --n_episodes 50 \
    --gpu 0 \
    --pi05
```

### d) s0 l01 30K eval

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && \
cd /root/colliforce-vla && \
python scripts/eval_safelibero.py \
    --model_type a1 \
    --checkpoint /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/a1_sdf_pi05_object_pudding_seed0_l01/30000 \
    --config_name baseline_object_pudding \
    --suite safelibero_object \
    --task_id 0 \
    --n_episodes 50 \
    --gpu 0 \
    --pi05
```

## 4. 阻塞问题

| # | 问题 | 影响 | 解决 |
|---|------|------|------|
| 1 | **10K checkpoint 不存在** | 不能直接 resume | 需要先重训 10K（Stage 1），额外 ~8-10h |
| 2 | Stage 1 与原始 s0 训练不完全相同 | 数据 shuffle 可能因 seed 相同而一致，但 wandb run 是新的 | 影响可忽略——random seed 固定，dataloader 顺序确定性由 seed 保证 |
| 3 | `SAVE_TOTAL_LIMIT=2` 也会影响 Stage 2 | 20K 步中间 checkpoint 可能被清理 | 已将 save_interval 设为 5000，最多保留 2 个（25000+30000），如需更多需改 SAVE_TOTAL_LIMIT |

---
