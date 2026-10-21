# code submit math500 fixed batch

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_submit_math500_fixed_batch_20260523T221716_result.json`
- **Structured JSON:** [`b5e93b26b2e57f0c60c4.json`](../../sessions/b5/b5e93b26b2e57f0c60c4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

**所有 6 张 GPU 已满载，无空闲 GPU 可提交新实验。**

### 当前运行中的 MATH-500 fixed eval (7 个进程 / 6 GPU)

| 实验 | 服务器:GPU | PID | 已运行 |
|------|-----------|------|--------|
| sft_standard_25_fixed_v2 | westd:0 | 166245 | 1h08m |
| grpo_rasp_alpha2p0_20_fixed | westd:1 | 168524 | 49m |
| sft_rasp_alpha2p0_20_fixed | westd:2 | 171964 | 7m |
| **grpo_cka_only_25_fixed** | westd:3 | 168451 | 49m |
| **sft_rasp_alpha0p5_20_fixed** | westd:3 | 170326 | 30m |
| grpo_cka_only_20_fixed | westb:0 | 321428 | 2h44m |
| **grpo_random_20_fixed** | westb:1 | 330254 | 32m |

**粗体** = 原以为"未启动"的 3 个 cron 实验中的 2 个 + 1 个新提交的。实际上全部已在运行。

### 问题
- westd:3 有 2 个 eval 争抢同一 GPU（~33.5GB VRAM），会互相拖慢。

### 仍待提交（等 GPU 空出）
1. **eval_math500_sft_rasp_alpha4p0_20_fixed** — checkpoint 在 westd
2. **eval_math500_sft_standard_20_fixed** — checkpoint 在 westd（v3 之前 SIGHUP 失败）
3. **eval_math500_sft_random_20_fixed** — checkpoint 在 westb（v2 之前 SIGTERM 失败）

### Registry 已更新
5 个正在运行的实验的 spec（server/gpu/pid/checkpoint_source）已更新到 registry，包括新建的 `eval_math500_grpo_rasp_alpha2p0_20_fixed`。

---
