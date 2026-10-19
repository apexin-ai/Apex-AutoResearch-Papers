# code prep exp004 s2

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prep-exp004-s2_20260522T040437_result.json`
- **Structured JSON:** [`0940698297bc4883cdcb.json`](../../sessions/09/0940698297bc4883cdcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

**汇报：exp-004-s2 (ACT seed 2) 准备完毕**

| 项目 | 详情 |
|------|------|
| **脚本** | `/root/contrastive_entrain_calib/training/run_exp004s2_act.py` (on westd-29046) |
| **与 exp-004 的差异** | `seed`: 42 → **43**；`output_dir`: `exp-004-act-baseline` → **`exp-004-act-baseline-s2`**；内联 `_resolve_transformer_layers` 去除对 `dcgrpo_trainer.py` 的依赖 |
| **其余超参数** | 完全相同（lr=5e-5, max_steps=8000, grad_accum=16, lora_rank=64, lambda_l2=0.1, save_steps=500） |
| **GPU** | GPU 1 空闲（0 MB 占用） |
| **dry-run** | 2 步训练通过，22 秒完成 |
| **训练命令** | `cd /root/contrastive_entrain_calib && HF_HUB_OFFLINE=1 CUDA_VISIBLE_DEVICES=1 nohup /root/miniconda3/bin/python training/run_exp004s2_act.py > /tmp/exp004s2_train.log 2>&1 &` |
| **预计训练时长** | ~11 秒/step × 8000 steps ÷ 16 grad_accum ≈ 约 24-30 小时（每个 micro step ~11s × 8000×16 micro steps... 实际 2 步用 22s，即每 optimizer step ~11s，8000 步 ≈ ~24 小时） |
| **Checkpoint 保存** | 每 500 步保存至 `/root/contrastive_entrain_calib/outputs/exp-004-act-baseline-s2/checkpoint-{step}`，最终模型在 `final/` |

等待 Director 审批后启动训练。

---
