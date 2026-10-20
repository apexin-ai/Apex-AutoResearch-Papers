# train v4 fixed inject10

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_v4-fixed-inject10_20260514T221001_result.json`
- **Structured JSON:** [`be3afe62bc5115f2a438.json`](../../sessions/be/be3afe62bc5115f2a438.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，registry 状态 RUNNING。

**汇总：**
- **exp_id**: `v4-fixed-inject10`
- **数据**: `sft_taxei_v4_fixed_inject10.jsonl`，4,358 samples（10% injection）
- **GPU**: cuda:2，tmux session `v4-fixed-inject10`
- **训练进度**: 0/1,635 steps，3 epochs，~2.7s/it
- **输出目录**: `/root/autodl-tmp/tax_error_inject_agent/output/v4-fixed-inject10/v0-20260515-061243/`
- **日志**: `/tmp/v4-fixed-inject10.log`
- **参数**: 完全照抄 mini_taxei_sft_v4 配置（LoRA r=16/α=32, lr=1e-4, bs=1×8, cosine, bf16, max_len=4096）

---
