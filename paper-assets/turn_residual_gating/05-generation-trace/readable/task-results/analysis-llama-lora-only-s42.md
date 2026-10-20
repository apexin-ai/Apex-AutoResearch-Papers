# analysis llama lora only s42

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_lora_only_s42_20260522T073713_result.json`
- **Structured JSON:** [`39a2dbc9b6f8e6db29e1.json`](../../sessions/39/39a2dbc9b6f8e6db29e1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志无 W&B 信息。数据已齐全，以下是分析结果。

---

## 训练结果摘要

| 指标 | 值 |
|------|-----|
| epochs_completed | 3 (epoch 0, 1, 2) |
| total_steps | 3000 (optimizer steps) |
| wall_clock_hours | 7.03h (25317.7s) |
| final_avg_loss | 0.9288 |
| final_avg_ntp | 0.9279 |
| final_avg_gar | 0.0009 |
| gate_type | none (constant 1.0, no gate params) |
| gpu | NVIDIA RTX PRO 6000 Blackwell Server Edition |
| mem_used_gb | 63.4 |
| trainable_params | 6,815,744 (0.08%) |
| checkpoint_path | `/root/turn_residual_gating/runs/phase2_llama_lora_only_s42/` |
| checkpoint_size | 27MB per epoch (3 epochs + final lora) |
| log_path | `/root/runs/turn_residual_gating/llama_lora_only_s42.log` |
| wandb_run_id | 未找到（该 run 未接 W&B） |

**Epoch 级别**:
| Epoch | Loss | NTP | GAR |
|-------|------|-----|-----|
| 0 | 1.0053 | 0.9880 | 0.0173 |
| 1 | 0.9516 | 0.9505 | 0.0011 |
| 2 | 0.9288 | 0.9279 | 0.0009 |

## 与 parent llama_tg_s42 对比

| 指标 | LoRA-only | TG (s42) | 差异 |
|------|-----------|----------|------|
| final_avg_loss | 0.9288 | 0.9233 | +0.0055 (TG 略优) |
| final_avg_ntp | 0.9279 | 0.9224 | +0.0055 (TG 略优) |
| final_avg_gar | 0.0009 | 0.0009 | 相同 |
| gate_mean | 1.0000 (固定) | 0.9099 | — |
| gate_std | 0.0000 | 0.0701 | — |
| wall_clock | 7.03h | 7.28h | LoRA-only 略快 |
| mem_used_gb | 63.4 | 63.4 | 相同 |

## 判断

1. **训练正常完成** — EXIT_CODE=0，无 error/exception，3 epoch 全部跑完，checkpoint 完整保存。

2. **必须跑 eval** — 训练时 GAR (0.0009) 两者完全一致，无法区分。真正的 hypothesis test 取决于推理时指标（TF/AR GAR-ours, gap_ratio）。llama_eval_s42 (TG) 已有 TF TG GAR-ours=0.4836, AR TG GAR-ours=0.0304, gap_ratio=15.9×。需要对 LoRA-only checkpoint 跑相同 eval，观察其 base GAR-ours 是否接近 TG 的 GAR-ours。

3. **初步信号** — Loss/NTP 差异仅 0.0055，非常微小。TG 的 gating (mean=0.91) 在训练时只提供了极小的 loss 优势，但 gating 的核心价值应体现在 eval-time 的 turn-level attention steering 上。

---
