# ssh llama lora only eval

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_llama_lora_only_eval_20260522T073931_result.json`
- **Structured JSON:** [`d0fe8fb24ef19f51abb1.json`](../../sessions/d0/d0fe8fb24ef19f51abb1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已提交。

**eval 脚本内容**：4 个 eval step — TF×{ours, dongre} + AR×{ours, dongre}，全部 `--gate-type none --checkpoint-dir runs/phase2_llama_lora_only_s42/epoch_2`

**运行状态**：
- PID: 309670
- tmux session: `eval_llama_lora_only_s42`
- log: `~/runs/turn_residual_gating/eval_llama_lora_only_s42.log`
- GPU: cuda:0

**预估运行时间**：参照 TG eval，Llama-8B 单 GPU 4 个 eval step 约 20-40 分钟。

---
