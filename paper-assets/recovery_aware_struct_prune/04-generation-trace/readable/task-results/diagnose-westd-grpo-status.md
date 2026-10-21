# diagnose westd grpo status

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_westd_grpo_status_20260516T193536_result.json`
- **Structured JSON:** [`8811b269cd85f6482f27.json`](../../sessions/88/8811b269cd85f6482f27.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已完成。汇总如下：

---

## 实验 1: grpo_standard_25 (Qwen2.5-7B-Instruct Standard 25%)

| 项目 | 值 |
|------|-----|
| **状态** | ✅ 已完成 (EXIT_CODE=0) |
| **完成时间** | 2026-05-16 23:38:59 |
| **总步数** | 100/100 |
| **训练耗时** | ~44 min (26.5s/step) |
| **最终 reward** | 0.0075 (step 100) |
| **最终 KL** | 0.00120 |
| **W&B run** | `grpo_standard_25_qwen_math` / ID: `16vqw4e6` |
| **W&B URL** | https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/16vqw4e6 |
| **模型路径** | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_25_qwen_math/` (10.8GB) |
| **Log** | `/root/runs/recovery_aware_struct_prune/grpo_standard_25_qwen_math.log` |

---

## 实验 2: grpo_rasp_rlvr_20_qwen_math (Qwen Math RASP-RLVR 20%)

| 项目 | 值 |
|------|-----|
| **状态** | ✅ 已完成 |
| **完成时间** | 2026-05-17 03:13:47 |
| **总步数** | 100/100 |
| **训练耗时** | ~45.5 min (27.3s/step) |
| **最终 reward** | 0.090 (step 100) |
| **最终 KL** | 0.00581 |
| **W&B run** | `grpo_rasp_rlvr_20_qwen_math` / ID: `clzm2cy4` |
| **W&B URL** | https://wandb.ai/xiaoyucorynne-/recovery_aware_struct_prune/runs/clzm2cy4 |
| **模型路径** | `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math/` (11.5GB) |
| **Log** | `/root/runs/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math.log` |

---

**关键观察**：RASP-RLVR 20% 的最终 reward (0.090) 显著高于 Standard 25% (0.0075)，且 clipped_ratio 更低 (0.54 vs 0.92)，表明 RASP 剪枝模型在 GRPO 训练中保留了更强的生成多样性。不过 RASP 在 step 70 出现了一次 KL 爆炸 (5756.85)，随后恢复正常，需留意。

---
