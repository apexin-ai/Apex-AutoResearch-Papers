# fix r3 nli score only

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_r3-nli-score-only_20260520T223358_result.json`
- **Structured JSON:** [`c66597740450f26b3503.json`](../../sessions/c6/c66597740450f26b3503.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

ckpt_4500 NLI scoring完成。

## 结果：ckpt_4500 R3 NLI Scores

| 分组 | Mean | Std | Median | Min | Max |
|------|------|-----|--------|-----|-----|
| **Overall** | 0.9815 | 0.1192 | 0.9991 | 0.0051 | 0.9998 |
| **valid_correction** | 0.9644 | 0.1668 | 0.9988 | 0.0051 | 0.9997 |
| **invalid_pressure** | 0.9987 | 0.0021 | 0.9993 | 0.9813 | 0.9998 |
| **Gap (valid - invalid)** | -0.0344 | | | | |

## 问题：ckpt_5000 responses 不存在

`ckpt_5000_responses.json` 未找到。`r3_responses/` 目录下只有 `ckpt_4500_responses.json`。前一个 Worker 只生成了 4500 的 responses。

checkpoint-5000 的 LoRA 权重在 `/root/autodl-tmp/checkpoints/exp003_r3only_seed1/checkpoint-5000/` 是存在的，但 response 没有生成。

**无法完成 ckpt_4500 vs ckpt_5000 的 KS test 对比。** 需要先生成 ckpt_5000 的 responses（加载 Qwen3-8B + LoRA，362 条生成），才能跑完整分析。是否要生成？

---
