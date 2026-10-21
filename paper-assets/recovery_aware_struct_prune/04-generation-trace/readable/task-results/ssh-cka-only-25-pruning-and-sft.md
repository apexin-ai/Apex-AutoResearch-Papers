# ssh cka only 25 pruning and sft

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_cka_only_25_pruning_and_sft_20260521T014335_result.json`
- **Structured JSON:** [`7d9fdea104fc64570465.json`](../../sessions/7d/7d9fdea104fc64570465.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Pruning 结果：**
- Mode: cka_only, sparsity 25%（actual 23.67%）
- MLP groups pruned: 248/784, Attn groups pruned: 0/112
- 参数量: 5.81B（原 7.62B）
- 输出: `/root/autodl-tmp/recovery_aware_struct_prune/pruned_cka_only_25/`
- 文件: config.json, generation_config.json, model.safetensors (11.63GB), tokenizer.json, tokenizer_config.json

**SFT 训练状态：**
- PID: 307651, GPU: cuda:1 (25.9 GB VRAM)
- 1870 steps (7473 samples × 2 epochs / effective_batch 8), ~1.1 it/s
- 预计耗时 ~28 分钟
- lr=2e-5, batch_size=1, grad_accum=8, max_seq_length=2048
- Registry: `sft_cka_only_25` → RUNNING
- 日志: `~/runs/recovery_aware_struct_prune/sft_cka_only_25.log`
- 输出: `/root/autodl-tmp/recovery_aware_struct_prune/sft_cka_only_25/`

---
