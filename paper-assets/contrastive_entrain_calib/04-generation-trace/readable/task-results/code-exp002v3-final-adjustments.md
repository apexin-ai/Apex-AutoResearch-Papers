# code exp002v3 final adjustments

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002v3-final-adjustments_20260519T073451_result.json`
- **Structured JSON:** [`bc20775af110f192a279.json`](../../sessions/bc/bc20775af110f192a279.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 最终配置确认表

| 参数 | 要求值 | 实际值 | 状态 |
|---|---|---|---|
| `R1_WEIGHT` | 0.4 | 0.4 | OK |
| `R2_WEIGHT` | 0.0 | 0.0 | OK |
| `R3_WEIGHT` | 0.6 | 0.6 | OK |
| `R1_SCALE_FACTOR` | 5.0 | 5.0 | OK |
| `lora_alpha` | 64 | 64 | OK |
| `recalibration_interval` | 500 | 500 | OK |
| `max_steps` | 8000 | 8000 | OK |
| `seed` | 42 | 42 | OK |
| `resume_from_checkpoint` | 删除 | 已删除，`trainer.train()` 无参数 | OK |

## Dry-run 结果

`py_compile` → **PASS**

## Trainer import 路径确认

- Run script: `sys.path.insert(0, "/root/mvp_v2_1_expanded/training")`
- 导入: `from dcgrpo_trainer import DCGRPOConfig, DCGRPOTrainer`
- 实际路径: `/root/mvp_v2_1_expanded/training/dcgrpo_trainer.py`
- `/root/contrastive_entrain_calib/training/dcgrpo_trainer.py` **不存在**，无歧义
- `r1_scale_factor` 在该 trainer 第130/271/674行正确实现（config default=1.0，run script 传入 5.0）

## 修改摘要

1. 删除 `resume_from_checkpoint`，从 base model 从头训练
2. 添加顶部异常阈值监控注释
3. 增强 `compute_rewards`：step 1-50 每步打印 R1/R3 mean+std、combined reward std、按 strength 分组的 R1；step 50+ 恢复每 10 步打印
4. `grad_norm`/`entropy` 由 HF trainer 内置 `logging_steps=10` 自动记录，无需额外代码
5. 远程 + 本地文件已同步

---
