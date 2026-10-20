# ops gpu check and submit lead2 8b

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_check_and_submit_lead2_8b_20260517T055221_result.json`
- **Structured JSON:** [`68eafca4dc5ca1ba0525.json`](../../sessions/68/68eafca4dc5ca1ba0525.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 状态

| GPU | 显存 | 进程 | 状态 |
|-----|------|------|------|
| cuda:0 | 10851/32607 MiB | PID 414837 (rsft_s44_dev_eval_preds) | 33% (81/247 batches), ~1.8h 剩余 |
| cuda:1 | 0 MiB → 已提交 | PID 418198 (lead2_rsft_grpo_ced) | 正在执行 merge script |
| cuda:2 | 22985/32607 MiB | PID 409565 (plan_016_llama_rsft_train_r3) | 运行中, 97% util |
| cuda:3 | 0 MiB → 已提交 | PID 418278 (plan_006_qwen3_8b_rsft_train) | 已加载 9041 样本, 正在载模型 |

## 完成的实验 Metrics

**1.7B RSFT** (plan_006_qwen3_1_7b_rsft_train) — 完成于 13:32:
- train_loss: 0.5234, eval_loss: 0.8725
- eval_mean_token_accuracy: 0.8185
- 1698 steps, 3 epochs, 2h15m runtime
- 输出: `/root/autodl-tmp/rsft_output_qwen3_1_7b`

**8B CED Scoring** — 完成:
- 输出: `/root/autodl-tmp/rsft_scored_qwen3_8b/rsft_train.jsonl` (9041 samples)

## 线索 1 状态

s44 dev eval 仍在运行 (33%, 81/247 batches, ~1.8h ETA)。`predictions.json` 尚未生成，CED evidence filtering 待 eval 完成后执行。

## Lead 2 提交

- **PID**: 418198 | **GPU**: cuda:1
- **流程**: merge_sft_rsft.py (base+SFT+RSFT → merged model) → grpo_trainer stage=3
- **参数**: lr=1e-6, max_steps=50, num_generations=8, kl_coef=0.01, bf16, ced_reward_weight=1.0, f1=0.0, format=0.5, save_steps=10
- **输出**: `/root/autodl-tmp/grpo_from_rsft_lead2`
- **Log**: `~/runs/faith-evidence-ie/lead2_rsft_grpo_ced.log`

## 8B RSFT 提交

- **PID**: 418278 | **GPU**: cuda:3
- **参数**: base=Qwen3-8B, sft=sft_output_qwen3_8b_bf16, data=9041 samples, epochs=3, bs=1, grad_accum=8, bf16, gradient_checkpointing (hardcoded)
- **输出**: `/root/autodl-tmp/rsft_output_qwen3_8b`
- **Log**: `~/runs/faith-evidence-ie/plan_006_qwen3_8b_rsft_train.log`

---
