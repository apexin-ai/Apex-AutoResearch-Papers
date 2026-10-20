# ssh verify westb gpu0

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_westb_gpu0_20260522T231357_result.json`
- **Structured JSON:** [`74ccaba14aba31f85aa8.json`](../../sessions/74/74ccaba14aba31f85aa8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

| GPU | 利用率 | VRAM | 进程 | PID | 内容 |
|-----|--------|------|------|-----|------|
| **cuda:0** | 99% | 16.3/95.6 GB | `eval_math500.py` | **250771** | MATH-500 eval on `sft_qwen_math_cka_only_20_final`，约 16 分钟前启动，正在运行 |
| **cuda:1** | 99% | 16.5/95.6 GB | `eval_gsm8k.py` | **220343** | GSM8K eval on `grpo_qwen_math_cka_only_20`（500 samples），已跑约 8 小时 |

- PID 250766 存在，是 MATH-500 eval 的父 bash wrapper。
- **GSM8K eval (`eval_gsm8k_sft_qwen_math`) 没在跑**——当前 cuda:1 上跑的是 GRPO 模型的 GSM8K eval，不是 SFT 模型的。
- tmux session `scoring_ablation_v2` 仍在（5月17日创建的旧 session）。

---
