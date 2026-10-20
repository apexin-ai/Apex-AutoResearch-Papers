# exp dr epoch matched indep lr

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_dr_epoch_matched_indep_lr_20260521T115157_result.json`
- **Structured JSON:** [`b13b63a7383ab77197fe.json`](../../sessions/b1/b13b63a7383ab77197fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已启动，配置确认：

- **max_steps: 2533** (独立 schedule，不是 6103)
- **lr_scheduler_type: linear** (与所有其他实验一致)
- **num_examples: 217,774** (scored_data_filtered_q05.jsonl)
- **warmup_ratio: 0.05** → ~127 warmup steps
- **weighting_method: uniform**
- **PID: 605271, GPU: cuda:1**

关于 scheduler 类型的说明：确认之前所有实验（包括 detect_remove_q05_seed42）实际使用 **linear** scheduler（HuggingFace 默认），不是 cosine。本实验保持一致，用 linear。核心修复是 `max_steps=2533` 让 LR 在训练结束时衰减到 minimum，消除之前 6103 步 schedule 在 2533 步截断时 LR 仍在 ~62% peak 的 confound。

---
