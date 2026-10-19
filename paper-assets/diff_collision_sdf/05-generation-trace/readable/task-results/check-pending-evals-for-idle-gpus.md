# check pending evals for idle gpus

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_pending_evals_for_idle_gpus_20260527T141850_result.json`
- **Structured JSON:** [`0f861bb20378a6927061.json`](../../sessions/0f/0f861bb20378a6927061.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完毕。以下是完整报告。

---

## GPU 状态 (westd-35807)

| GPU | 状态 | 占用 |
|-----|------|------|
| cuda:0 | **空闲** (0 MiB) | `train_phase2_lambda0_extra_seed_v2` 已崩溃 (EXIT_CODE=1) |
| cuda:1 | **空闲** (0 MiB) | `train_phase2_lambda0_extra_seed` 已死 |
| cuda:2 | **空闲** (0 MiB) | `train_phase2_lambda0_s2_v3` 已崩溃 (EXIT_CODE=1, `RuntimeError: Could not infer dtype of dict`) |
| cuda:3 | 在用 (27 GB, 100%) | `train_spatial_bowl_lora_control_s0` 运行中 (PID 341425, 已运行 1d 2h) |

## eval_pi05_a1_best_s0_l005 — 不可跑

- `a1_sdf_pi05_object_pudding_seed0_l005/` 下**只有 `30000/`**，无 `best/` 目录
- 训练脚本 `train_a1_sdf_aux_pi05.py` 没有 `save_best` 逻辑
- Registry 已标记 conclusion=killed，原因正是 best/ 不存在
- 该 checkpoint 的 30K eval 已完成 (`reeval_sdf_s0_l005_30k`, CAR=57%)

## 所有主要 30K eval 覆盖情况

| checkpoint | seed0 | seed1 | seed2 |
|------------|-------|-------|-------|
| LoRA baseline | 57% ✓ | 52.5% ✓ | **RUNNING** (westd-45947) |
| λ=0.005 | 57% ✓ | 54% ✓ | 52.5% ✓ |
| λ=0.01 | 57% ✓ | 57.5% ✓ | 54.5% ✓ |
| λ=0.1 | 58% ✓ | 58.5% ✓ | **training** (westd-45947) |
| Phase2 λ=0 | **训练崩溃** | — | 57.5% (10K) ✓ |

**结论：目前没有已完成训练但未 eval 的 checkpoint。** 所有可 eval 的 30K checkpoint 均已覆盖。

## 可利用 cuda:0/1/2 的工作

唯一可以做的是**修复并重跑崩溃的训练**（不是 eval）：

1. **`train_phase2_lambda0_extra_seed_v2`** (cuda:0) — Phase 2 Stage 1 seed0, 崩溃在数据加载阶段
2. **`train_phase2_lambda0_s2_v3`** (cuda:2) — Phase 2 Stage 2 seed2 (λ=0 resume to 30K), 崩溃于 lerobot 的 `hf_transform_to_torch` (`Could not infer dtype of dict`)

Eval 命令模板（供之后使用）:
```bash
python scripts/eval_safelibero.py \
  --checkpoint &lt;CHECKPOINT_PATH> \
  --config_name pi05_libero \
  --model_type lora_baseline \
  --pi05 \
  --suite safelibero_object \
  --safety_level II \
  --n_episodes 50 \
  --seed 7 \
  --gpu &lt;GPU_ID>
```

---
