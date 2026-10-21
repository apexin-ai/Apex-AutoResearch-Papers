# eval ngram both seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ngram_both_seed42_20260519T000134_result.json`
- **Structured JSON:** [`5167dd9dcd5731d8e6cb.json`](../../sessions/51/5167dd9dcd5731d8e6cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两组 eval 全部完成。

## 结果汇总

| Model | eval_loss_holdout | eval_ppl_holdout |
|---|---|---|
| ngram_adaptive_seed42 | 2.8803 | 17.82 |
| ngram_uniform_seed42 | 2.8733 | 17.69 |

**Δ PPL (adaptive - uniform) = +0.13**

对比 TF-IDF baseline (adaptive=17.65, uniform=17.69)：
- N-gram adaptive PPL 17.82 比 TF-IDF adaptive 17.65 高 0.17，符合预期（N-gram 检测器 AUC=0.73 质量低，adaptive 加权效果更差）
- N-gram uniform PPL 17.69 与 TF-IDF uniform 17.69 完全一致，符合预期（uniform 不依赖检测器质量，两者用相同权重分布）

---
