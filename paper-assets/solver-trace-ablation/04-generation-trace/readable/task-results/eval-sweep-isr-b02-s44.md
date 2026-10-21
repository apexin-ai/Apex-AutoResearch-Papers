# eval sweep isr b02 s44

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_sweep-isr-b02-s44_20260516T065624_result.json`
- **Structured JSON:** [`eb28e6f56ddd99cb7d0d.json`](../../sessions/eb/eb28e6f56ddd99cb7d0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 释放完毕。

## sweep-isr-b02-s44 Eval 结果

| 指标 | s42 | s43 | **s44** |
|------|-----|-----|---------|
| eval_prove_rate | 1.00 | 0.96 | **0.94** |
| eval_mean_isr | 0.6017 | 0.5298 | **0.9058** |
| H7a | 100% | 96.9% | **100%** |
| H1 | 0% | 0% | **0%** |
| H8 | 0% | 0% | **0%** |
| genuine | 0% | 0% | **0%** |
| single_premise | 100% | 100% | **100%** |
| ISR=1.0 | — | — | **92.5%** |

s44 确认 Goodhart collapse：H7a=100%, genuine=0%。与 s42/s43 一致。

唯一显著差异：s44 的 eval_mean_isr 高很多（0.91 vs 0.60/0.53）。原因是 s44 的单前提 tautology 更"纯净"——92.5% 的 proved 样本 ISR=1.0（单前提中唯一 clause 就是 conclusion 本身，ablation 后必然 fail，所以 ISR=1.0）。s42/s43 的 ISR 较低说明它们有更多带额外冗余 clause 的 tautology 变体。

结论：β=0.2 三个 seed 全部 Goodhart collapse，dose-response 假设在此 β 值成立。Registry 已更新为 DONE/success。

---
