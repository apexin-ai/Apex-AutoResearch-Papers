# ssh urgent status westb

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_status_westb_20260522T183318_result.json`
- **Structured JSON:** [`1bc18a2f18a26be0b32e.json`](../../sessions/1b/1bc18a2f18a26be0b32e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## westb-23072 GPU 状态

| GPU | VRAM | Util | 进程 | PID | 状态 |
|-----|------|------|------|-----|------|
| 0 | 16801 / 97887 MiB | 98% | CKA-only MATH-500 eval | 234500 | alive (27m) |
| 1 | 16547 / 97887 MiB | 99% | GSM8K GRPO CKA-only v2 eval | 220343 | alive (3h24m) |

## CKA-only MATH-500 进度
- 状态: running
- 进度: 40/500 (8%)
- 启动时间: ~27 分钟前
- 预估剩余: ~20h（按 ~2.6min/sample）

## MF3 v3 进度
- **注意**: PID 220343 实际跑的是 **v2**（非 v3），输出文件 `eval_gsm8k_grpo_qwen_math_cka_only_20_n500_v2.json`
- 状态: running
- 进度: **148/500** (29.6%)
- acc@100: 48.0%, eos_rate: 18%, avg_len: 1734
- 速度: ~100s/it，预估剩余 ~9.7h

## 空闲 GPU
- 无。两张 GPU 均满载。

---
