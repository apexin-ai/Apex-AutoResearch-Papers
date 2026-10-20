# ssh find sft standard 25 and eval

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_find_sft_standard_25_and_eval_20260521T074644_result.json`
- **Structured JSON:** [`afb2e876be503c55e503.json`](../../sessions/af/afb2e876be503c55e503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**任务 1: SFT Standard 25% 模型**

| 服务器 | 结果 |
|--------|------|
| westd-29022 | 未找到。只有 `sft_qwen_math_standard_25`、`pruned_standard_25`、`grpo_standard_25` |
| westb-23072 | **找到**: `/root/autodl-tmp/recovery_aware_struct_prune/sft_standard_25/checkpoint-1870/` |

模型仅在 westb 上，westd 没有。需要先把模型拷贝到 westd 才能在 cuda:3 启动 eval。是否要我执行 scp 拷贝？

**任务 2: CKA-only 25% GRPO eval**

- PID 322443: **仍在运行**
- 进度: **1224/1319 (93%)**，已运行 2h48m
- 最近 checkpoint (1200/1319): **acc=59.75%**, eos_rate=98.33%, avg_len=232
- 预计剩余 ~95 samples × ~3s/it ≈ **~5 分钟完成**

---
