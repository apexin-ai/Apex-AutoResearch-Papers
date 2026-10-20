# eval b02 s42 eval sta

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_b02-s42-eval-sta_20260516T045629_result.json`
- **Structured JSON:** [`3caacc27a1f9cf30e5a9.json`](../../sessions/3c/3caacc27a1f9cf30e5a9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。**sweep-isr-b02-s42 eval_sta 结果**：

- **prove_rate**: 100% (100/100)
- **mean_isr**: 0.6017 (σ=0.1973)
- **median_isr**: 0.500

Registry 已更新。注意 eval ISR (0.60) 高于训练日志末期的 ~0.52，说明 greedy decoding 下模型倾向更短的 formalization（多数样本 ISR=0.5，即仅 1 premise + conclusion）。

---
