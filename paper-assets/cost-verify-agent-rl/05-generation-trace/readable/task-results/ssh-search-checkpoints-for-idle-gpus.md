# ssh search checkpoints for idle gpus

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_search_checkpoints_for_idle_gpus_20260523T014214_result.json`
- **Structured JSON:** [`46f7f2ad3f5a0a410eab.json`](../../sessions/46/46f7f2ad3f5a0a410eab.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 搜索结果

### seed300 resume (bjb1)
**状态: SEED300_NOT_FOUND**

`exp029-seed300/` FSDP 目录在 bjb1 上不存在（无 global_step、无 optimizer states）。仅有 HF 格式权重 `qwen_exp029_seed300_step5_hf`（不含 optimizer，无法 resume 训练）。

### seed2 late-step (两台服务器)

**bjb1:** 无 seed2 checkpoint（`*seed2*` 匹配的是 seed200/seed2048）

**westd:** 
- `exp029_seed2_step15_hf` — HF 格式，3.8GB，step **15**（最晚的 seed2 checkpoint）
- `qwen_exp029_seed2_step15_hf` — 同上的 qwen 前缀副本
- 无 FSDP 格式 checkpoint
- **无 step30+ checkpoint**，最远只到 step15

### 其他可用 HF checkpoints

**bjb1 (6个):**
| checkpoint | step |
|---|---|
| `qwen_c_prime_step5_hf` | 5 |
| `qwen_exp029_seed200_step5_hf` | 5 |
| `qwen_exp029_seed300_step5_hf` | 5 |
| `qwen_exp029_seed4_step15_hf` | 15 |
| `qwen_exp029_seed7_high_kl_step5_hf` | 5 |
| `qwen_exp029_seed7_high_kl_step7_hf` | 7 |

**westd (14个):**
| checkpoint | step |
|---|---|
| `qwen_c_prime_step5_hf` | 5 |
| `qwen_exp029_seed100_step10_hf` | 10 |
| `qwen_exp029_seed100_step5_hf` | 5 |
| `qwen_exp029_seed2_step15_hf` | 15 |
| `qwen_exp029_seed42_step5_hf` | 5 |
| `qwen_exp029_seed4_step15_hf` | 15 |
| `qwen_exp029_seed5_step10_hf` | 10 |
| `qwen_exp029_seed6_step15_hf` | 15 |
| `qwen_exp029_seed7_high_kl_step5_hf` | 5 |
| `qwen_exp029_seed7_high_kl_step7_hf` | 7 |
| `qwen_exp029_seed8_step5_hf` | 5 |
| `qwen_intervention_c_hard_cap_step5_hf` | 5 |
| `qwen_intervention_c_hard_cap_step7_hf` | 7 |
| `qwen_seed2048_step5_hf` | 5 |

---
