# ops westb cuda0 check and launch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westb_cuda0_check_and_launch_20260518T210229_result.json`
- **Structured JSON:** [`071fa830f06680a444ed.json`](../../sessions/07/071fa830f06680a444ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**cuda:0 状态**：空闲（eval 已完成）。cuda:1 有进程运行中（PID 832359, 6568MiB, 59% util）。

**收割结果 — eval_gsm8k_grpo_standard_20_1p5b**：
- accuracy = **22.29%** (294/1319), stderr = 0.0115
- eos_rate = 90.5%, avg_response_length = 515 tokens
- Registry 已更新为 DONE/success

**新实验已启动 — eval_gsm8k_sft_cka_only_20_1p5b**：
- tmux session `eval_gsm8k_sft_cka_only_20_1p5b` 在 westb-23072 cuda:0
- 模型正在加载（nvidia-smi 尚未显示显存占用，刚启动几秒）
- Registry 状态：RUNNING

---
