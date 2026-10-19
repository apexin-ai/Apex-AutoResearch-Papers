# code d077 fix assert resubmit both

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d077_fix_assert_resubmit_both_20260519T144050_result.json`
- **Structured JSON:** [`7fcc1e50c0a6ac025fb3.json`](../../sessions/7f/7fcc1e50c0a6ac025fb3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full situation:

## Status Report

### Code fix (tolerance 0.02 → 0.05)
- **westd-34887**: Already fixed (line 165 has `0.05`)
- **westd-41718**: Fixed just now ✓

### westd-34887 GPU状态 — 两块GPU都被占用

| GPU | Experiment | Elapsed | Progress | Tasks |
|-----|-----------|---------|----------|-------|
| cuda:0 | `qwen14b_kl30_s42_eval_uniform_v3` | ~14min | MMLU eval 11% (est ~30min left) | wikitext2,arc_challenge,winogrande,**hellaswag,piqa**,mmlu |
| cuda:1 | `qwen14b_teal275_uniform_eval_v3` | ~2min | arc_challenge eval 8% | wikitext2,arc_challenge,winogrande,mmlu,gsm8k |

### 问题

1. **两个实验已经在跑**，但不在 registry 中（不是通过 `submit_training_job` 提交的），没有 cron 监控
2. **kl30 的 task list 和你要求的不同**：正在跑的是 `hellaswag,piqa,mmlu`（6 tasks），你要求的是 `mmlu,gsm8k`（5 tasks，没有 hellaswag/piqa 但有 gsm8k）
3. kl30 正在跑的是 v3 而非 v4

### 需要你决定

- **Option A**: 让当前实验跑完（它们代码已经是修复后的），事后补注册。kl30 的 task list 不含 gsm8k，后续可能需要单独补跑 gsm8k。
- **Option B**: Kill 掉，按你的 spec 用 `submit_training_job` 重新提交 v3/v4（正确 task list + registry + cron 监控）。浪费当前进度。

怎么处理？

---
