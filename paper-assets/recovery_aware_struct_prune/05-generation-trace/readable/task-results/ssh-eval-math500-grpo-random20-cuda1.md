# ssh eval math500 grpo random20 cuda1

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval_math500_grpo_random20_cuda1_20260521T101943_result.json`
- **Structured JSON:** [`21383217aa5edbbe3590.json`](../../sessions/21/21383217aa5edbbe3590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已开始运行！模型加载到 `cuda:0`（CUDA_VISIBLE_DEVICES=1，即物理 GPU 1），数据集加载完成，正在评估 500 题。

---

## 汇总

### 任务 1: Random 20% GRPO eval (cuda:1)
- **模型路径**: `/root/autodl-tmp/recovery_aware_struct_prune/grpo_random_20/checkpoint-100/model.safetensors` (12G, 339 keys)
- **PID**: 359173
- **GPU**: cuda:1（CUDA_VISIBLE_DEVICES=1）
- **状态**: 已启动，正在评估 500 题
- **日志**: `/root/runs/recovery_aware_struct_prune/eval_math500_grpo_random_20.log`

### 任务 2: cuda:0 / cuda:2 进度

| Eval | GPU | 进度 | Acc@50 | 运行时间 |
|------|-----|------|--------|---------|
| GRPO CKA-only 25% | cuda:0 | **74/500 (15%)** | 0.1800 | ~1h54m |
| SFT CKA-only 25% | cuda:2 | **63/500 (13%)** | 0.2400 | ~1h25m |

三张 GPU 均在工作，按当前速度每个 eval 预计总耗时 ~12-13h。

---
