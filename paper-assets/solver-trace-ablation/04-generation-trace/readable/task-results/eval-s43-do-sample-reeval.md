# eval s43 do sample reeval

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_s43-do-sample-reeval_20260514T035320_result.json`
- **Structured JSON:** [`beafb5a871d929904bf5.json`](../../sessions/be/beafb5a871d929904bf5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

## do_sample 评估结果

| 指标 | greedy (原) | do_sample=True, T=0.7 |
|------|-------------|----------------------|
| prove_rate | 13% (13/100) | **14% (14/100)** |
| mean_isr | 0.0000 | 0.0000 |
| avg gen time | ~12s | ~10.9s |

**结论：sampling 没有修复问题。** PR 仅从 13% → 14%（多 proved 1 个样本），统计上无显著差异。所有 ISR 仍为 0.0000。

大多数样本（~86/100）仍然 gen=11-12s hit max_new_tokens，即使用 temperature=0.7 sampling 也无法打断 repetition collapse。少数 proved 的样本 gen=4-7s（没有 hit max_tokens）。

**这不是 greedy decoding 的 artifact。模型确实退化了。** 训练 PR=88.3% 与 eval PR=14% 的巨大差距说明 s43-r4 训练时发生了 reward hacking / 过拟合，学到的模式不具备泛化能力。

---
