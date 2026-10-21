# code train pi05 lora baseline

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_train_pi05_lora_baseline_20260523T032024_result.json`
- **Structured JSON:** [`3350427a717f07a8aba7.json`](../../sessions/33/3350427a717f07a8aba7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过：
- **语法检查**：两台服务器均 `syntax OK`
- **--help**：参数列表正确，无 `--lambda_sdf`/`--lambda_ee`/`--n_query_points`/`--sdf_clamp`/`--eikonal_weight`
- **SDF/EE 清除**：仅第 9 行注释中出现（docstring），无代码引用
- **Phase schedule 保留**：Phase 1/2 切换、LoRA freeze/unfreeze、warmup 逻辑完整（第 75-134 行）

---

## 报告

### 差异摘要（vs `train_a1_sdf_aux_pi05.py`）

| 项目 | A1 SDF Aux | Baseline |
|------|-----------|----------|
| 行数 | 337 | 221 |
| Imports | sdf_decoder, ee_extractor, numpy, F | 仅 lora_utils |
| SCENE_CONFIG | 含 `sdf_gt` 路径 | 移除 `sdf_gt` |
| Args | `--lambda_sdf`, `--lambda_ee`, `--n_query_points`, `--sdf_clamp`, `--eikonal_weight` | 全部移除 |
| Hooks 类 | SdfAuxHooks (含 SDFDecoder, EEExtractor, SuffixOutHook) | LoRABaselineHooks (纯 LoRA) |
| extra_params() | sdf_decoder + ee_extractor params | `[]` (空) |
| on_loss_computed | action_loss + λ_sdf * sdf_loss + λ_ee * ee_loss | action_loss (直接返回) |
| on_save_checkpoint | sdf_decoder.pt + ee_extractor.pt + aux_metadata.pt | baseline_metadata.pt |
| Phase 1/2 schedule | 完全一致 | 完全一致 |
| LoRA 配置 | pali_rank=16, expert_rank=32 | 完全一致 |
| lr/batch/steps/save | 完全一致 | 完全一致 |
| exp_name | `a1_sdf_pi05_{scene}_seed{seed}_l{lambda}` | `pi05_lora_baseline_{scene}_seed{seed}` |

### 训练命令

```bash
# Baseline 训练
WANDB_MODE=offline python scripts/train_pi05_lora_baseline.py \
    --scene object_pudding --seed 0 --gpu 0 \
    --batch_size 32 --num_train_steps 30000 \
    --lr 2.5e-5 --save_interval 2000

# Dry run 验证
python scripts/train_pi05_lora_baseline.py --scene object_pudding --dry_run --gpu 0
```

### Eval 命令模板

```bash
# 评估 baseline checkpoint（与 A1 eval 脚本相同，只需指向 baseline 的 checkpoint 路径）
python scripts/eval_pi05_safelibero.py \
    --checkpoint_dir /root/autodl-tmp/checkpoints/a1_sdf_pi05_object_pudding/pi05_lora_baseline_object_pudding_seed0/step_30000 \
    --scene object_pudding --gpu 0 --n_episodes 50
```

---
