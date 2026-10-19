# code plan005 phase2 lambda0 prep

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan005_phase2_lambda0_prep_20260526T143911_result.json`
- **Structured JSON:** [`9e0b283e89c0214ca894.json`](../../sessions/9e/9e0b283e89c0214ca894.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息收集完毕。汇总产出：

---

## Phase 2 λ=0 训练准备报告

### 1. 可用 10K SDF Checkpoints: 无

**`SAVE_TOTAL_LIMIT=2`**（`/root/autodl-tmp/openpi/scripts/train_pytorch.py:240`）已删除所有 λ>0 SDF 训练的中间 checkpoints。只剩终态。

**westd-35807:**
| Run | 可用 steps |
|-----|-----------|
| seed0_l005 | 30000 |
| seed0_l01 | 30000 |
| seed0_l1 | 12000, 14000（仍在跑） |
| seed1_l005 | 29999, 30000 |
| seed1_l01 | 29999, 30000 |
| seed1_l1 | 12000, 14000（仍在跑） |
| seed2_l0 | 9999, 10000（这是 λ=0 run，非 SDF 源） |
| seed2_l005 | 29999, 30000 |
| seed2_l01 | 29999, 30000 |
| phase2_lambda0_s0_stage1 | 空（仅 wandb_id.txt） |
| seed0_l005_p2abl | 空（仅 wandb_id.txt） |

**westd-45947:**
| Run | 可用 steps |
|-----|-----------|
| seed0_l005 | 30000 |
| seed0_l01 | 30000 |
| seed1_l005 | 30000 |
| seed1_l01 | 30000 |
| seed2_l005 | 30000 |
| seed2_l01 | 30000 |
| baseline_seed0/1 | 30000 |
| baseline_seed2 | 10000, 12000（仍在跑） |

### 2. Resume 机制

- `--resume`：布尔 flag，自动找 exp 目录下**最新** checkpoint 恢复（model + optimizer + step）
- **无 `--resume_from` 参数**，不能指定特定 step
- Checkpoint 目录：`{CHECKPOINT_BASE}/a1_sdf_pi05_{scene}/{exp_name}/`
- `--exp_name` 可覆盖自动名称，指向不同 checkpoint 目录
- `SdfAuxHooks` 的 resume 额外从 `aux_metadata.pt` 恢复 phase 状态（LoRA 是否解冻）；但路径构造有 bug（缺 `name` 层级），实际不影响功能——`on_step_start` 会在 `global_step >= warmup_phase_steps` 时自动触发 Phase 2

### 3. Phase 2 命令模板

前提：先获得 10K SDF checkpoint（见下方选项）。假设 checkpoint 位于 `{exp_dir}/10000/`：

```bash
source /root/miniconda3/etc/profile.d/conda.sh && conda activate libero && \
cd /root/colliforce-vla && export WANDB_MODE=disabled && \
python scripts/train_a1_sdf_aux_pi05.py \
  --scene object_pudding \
  --seed &lt;SEED> \
  --lambda_sdf 0 \
  --gpu &lt;GPU_ID> \
  --num_train_steps 30000 \
  --resume \
  --exp_name &lt;SOURCE_EXP_NAME>
```

`--resume` 会从 `&lt;SOURCE_EXP_NAME>` 目录找最新 checkpoint（必须是 10000），以 λ=0 继续训到 30000。

### 4. 核心问题与选项

之前 Phase 2 成功是因为赶在 SAVE_TOTAL_LIMIT 清理前捞到了 10K checkpoint。现在 **所有 l005/l01 的 10K checkpoint 已被删除**。

**Option A：重跑 Phase 1 到 10K（推荐）**
```bash
python scripts/train_a1_sdf_aux_pi05.py \
  --scene object_pudding --seed 0 --lambda_sdf 0.005 \
  --num_train_steps 10000 --gpu &lt;ID> \
  --exp_name a1_sdf_pi05_object_pudding_seed0_l005_p2
```
10K 是终态 step，不会被 SAVE_TOTAL_LIMIT 删。约 ~8h/run。然后 Phase 2 用 `--resume --exp_name` 同名目录 + `--lambda_sdf 0 --num_train_steps 30000`。

**Option B：用 l1 的 12K checkpoint**
`seed0_l1/12000` 和 `seed1_l1/12000`（westd-35807 上还在）。但 λ=1.0 ≠ 0.005，实验设计不同。

**Option C：直接从 30K checkpoint 继续**
`--num_train_steps 50000`，但改变了实验设计。

### 5. SAVE_TOTAL_LIMIT 注意事项

当前值 = 2，**必须改为 ≥3**。改动位置：`/root/autodl-tmp/openpi/scripts/train_pytorch.py:240`。否则 Phase 1 跑完后 10K checkpoint 仍会被删。

对于 Option A（`--num_train_steps 10000`），10K 是最终 step，不存在被清理问题。但如果后续还要跑完整 30K SDF + 保留 10K，则必须改 SAVE_TOTAL_LIMIT。

### 6. 代码改动

训练脚本本身不需要改动。唯一需要的改动是 `SAVE_TOTAL_LIMIT`（如果选择方案需要保留中间 checkpoints）。

---
