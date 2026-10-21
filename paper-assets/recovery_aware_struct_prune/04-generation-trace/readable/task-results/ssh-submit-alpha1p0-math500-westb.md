# ssh submit alpha1p0 math500 westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_submit_alpha1p0_math500_westb_20260522T205113_result.json`
- **Structured JSON:** [`04d9c87ab6cc21dc9203.json`](../../sessions/04/04d9c87ab6cc21dc9203.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**MODEL_NOT_FOUND**

westb-23072 上没有 α=1.0 RASP SFT 7B 模型。现有 SFT 模型：

| 路径 | 说明 |
|------|------|
| `sft_rasp_20_1p5b` | α=1.0 但是 1.5B |
| `sft_rasp_alpha3p0_20` | α=3.0 |
| `sft_rasp_rlvr_20` | RASP+RLVR |

该模型在 **westd-32935** 上存在：`/root/autodl-tmp/recovery_aware_struct_prune/sft_rasp_20_westd`。

另外 westb GPU:0 状态异常（100% util / 0 MiB，无进程），可能需要 `nvidia-smi --gpu-reset -i 0`。

需要我把模型从 westd 拷到 westb 吗？或者改在 westd 上跑这个 eval？

---
