# research grpo hyperparams sf5

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_grpo-hyperparams-sf5_20260522T121858_result.json`
- **Structured JSON:** [`d748e2cc8f2e618c79e0.json`](../../sessions/d7/d748e2cc8f2e618c79e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here are the hyperparameter tables:

---

## DC-GRPO 超参数（以 exp-002v3 为准）

| 参数 | 值 | 来源 |
|------|-----|------|
| Base model | Qwen3-8B | `run_exp002v3_dcgrpo_scaled_cosine.py:46` |
| learning_rate | 5e-5 | `:74` |
| per_device_train_batch_size | 1 | `:72` |
| gradient_accumulation_steps | 16 | `:73` (effective batch = 16) |
| max_steps | 8,000 | `:79` |
| warmup_steps | 200 | `:75` |
| bf16 | True | `:80` |
| gradient_checkpointing | True | `:74` |
| max_completion_length | 256 | `:82` |
| num_generations (group_size) | 2 | `:83` |
| beta (KL penalty) | 0.04 | GRPOConfig default (exp-003 explicitly sets 0.04) |
| temperature | 0.7 | exp-003 `:86`; exp-002v3 uses GRPOConfig default (1.0 or 0.9) |
| num_iterations | 1 | exp-003 `:85`; exp-002v3 uses default |
| lr_scheduler_type | linear (default) | exp-002v3 未显式设置; exp-003 设为 cosine |
| seed | 42 | `:49` |
| **Reward weights** | R1=0.4, R2=0.0, R3=0.6 | `:47-48` |
| r1_scale_factor | 5.0 | `:50` |
| reward_layers | [19, 20, 24, 27, 32, 33, 35] | `:51` |
| reward_position | asst_first | `:68` |
| R3 NLI model | cross-encoder/nli-deberta-v3-base | `:71` |
| recalibration_interval | 500 | `:72` |
| **LoRA r** | 64 | `:89` |
| **LoRA alpha** | 64 | `:90` |
| **LoRA target_modules** | q_proj, k_proj, v_proj, o_proj | `:91` |
| LoRA bias | none | `:92` |
| LoRA dropout | 0 (default) | 未设置 |

**注意**：exp-002v3 未显式设置 `beta`/`temperature`/`num_iterations`/`lr_scheduler_type`，这些参数继承 TRL `GRPOConfig` 默认值。exp-003 (R3-only baseline) 显式设置了 `beta=0.04, temperature=0.7, lr_scheduler_type="cosine", num_iterations=1, scale_rewards="group"`。需确认 exp-002v3 实际使用的 TRL 版本对应的默认值。

---

## R3-only Baseline (exp-003) 与 DC-GRPO 的差异

| 参数 | 值 |
|------|-----|
| R1/R2/R3 weights | 0.0 / 0.0 / 1.0 |
| direction_path | "" (无对比方向) |
| warmup_steps | 100 |
| lr_scheduler_type | cosine |
| beta | 0.04 |
| temperature | 0.7 |
| reward_layers | range(19, 36) |
| 其余参数同 DC-GRPO | — |

---

## ACT (SFT + L2 Consistency) 超参数

| 参数 | 值 | 来源 (`run_exp004s2_act.py`) |
|------|-----|------|
| Base model | Qwen3-8B | `:152` |
| optimizer | AdamW | `:214` |
| learning_rate | 5e-5 | `:157` |
| weight_decay | 0.01 | `:214` |
| per_device_batch_size | 1 | DataLoader batch_size=1 |
| gradient_accumulation_steps | 16 | `:156` |
| max_steps | 8,000 | `:155` |
| warmup_steps | 200 | `:158` |
| lr_scheduler | linear with warmup | `get_linear_schedule_with_warmup` `:215` |
| max_seq_len | 1,024 | `:160` |
| grad_clip | 1.0 | `clip_grad_norm_` in training loop |
| **lambda_l2** (L2 loss weight) | 0.1 | `:159` |
| **Loss** | `sft_loss + 0.1 * l2_loss` | sft = avg(valid_loss, invalid_loss) |
| **L2 target layers** | [19, 20, 24, 27, 32, 33, 35] | `:30` |
| seed | 43 (s2) / 42 (s1) | `:163` |
| **LoRA r** | 64 | `:164` → `:190` |
| **LoRA alpha** | 128 (rank × 2) | `:191` |
| **LoRA target_modules** | q/k/v/o_proj + gate/up/down_proj | `:192` |
| LoRA dropout | 0.05 | `:193` |
| LoRA bias | none | `:194` |

---

**关键差异**：ACT 的 LoRA 配置比 GRPO 更广（多了 gate/up/down_proj，alpha=2r 而非 r，有 dropout=0.05）。论文中需注明这一差异，或说明 ACT 需要更大的适配容量来同时学 SFT + L2 一致性。

---
