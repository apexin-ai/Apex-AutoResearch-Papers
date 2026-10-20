# analysis llama sft s43 train eval r3

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama_sft_s43_train_eval_r3_20260520T140644_result.json`
- **Structured JSON:** [`feec3d14ff3a7975811b.json`](../../sessions/fe/feec3d14ff3a7975811b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有 wandb 记录。所有数据已收集完毕。

## 结果

- **conclusion**: success
- **ign_f1**: 0.5142
- **evi_f1**: 0.4220 (joint) / 0.8245 (TP)
- **edcr**: 0.5866
- **re_p** (ign_precision): 0.4917
- **re_r** (ign_recall): 0.5389
- **train_loss_final**: 0.521
- **checkpoint_path**: `/root/autodl-tmp/sft_output_llama_3_1_8b_s43/` (adapter_model.safetensors 640MB, checkpoint-190, checkpoint-570)
- **log_path**: `~/runs/faith-evidence-ie/llama_sft_s43_train_eval_r3.log`
- **wandb_run_id**: 无（未启用 wandb）

## 对比

| Seed | ign_f1 | evi_f1 (joint) | edcr |
|------|--------|----------------|------|
| s42 (SFT) | 0.5384 | — | — |
| **s43 (SFT)** | **0.5142** | **0.4220** | **0.5866** |
| RSFT 3-seed mean | 0.5654 ± 0.0052 | — | — |

s43 ign_f1 = 0.5142，比 s42 (0.5384) 低 **0.0242**（-4.5%）。两个 SFT seed 目前 mean = 0.5263，与 RSFT mean 0.5654 差距 0.0391。

SFT 两个 seed 之间的差异 (0.0242) 已经明显大于 RSFT 3-seed 的 std (0.0052)，初步支持 "SFT variance > RSFT variance" 的 claim。还需要 s44 完成 3-seed 统计才能做正式对比。

---
