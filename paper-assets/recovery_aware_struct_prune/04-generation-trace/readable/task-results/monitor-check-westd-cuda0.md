# monitor check westd cuda0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_check_westd_cuda0_20260516T191831_result.json`
- **Structured JSON:** [`b105c102b28bcf324d1a.json`](../../sessions/b1/b105c102b28bcf324d1a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-11672 cuda:0 完全空闲**（0MiB 显存 / 0% 利用率）。cuda:1 同样空闲。

当前 GPU 活动全在 cuda:2 上（96% 利用率，54GB/98GB 显存），跑的是两个 eval 任务：
- `eval_gsm8k.py` → `grpo_standard_qwen_math`（pass@8 评估）
- `eval_gsm8k.py` → `grpo_rasp_25`（全量 1319 样本评估）

`grpo_rasp_rlvr_20_qwen_math` 的 checkpoint 目录已存在于 `/root/autodl-tmp/recovery_aware_struct_prune/grpo_rasp_rlvr_20_qwen_math/`（最后修改 May 17 03:13），但没有相关进程在运行。无 tmux session。

**总结：westd cuda:0 空闲可用，无任何进程占用。**

---
