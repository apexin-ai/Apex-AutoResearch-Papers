# analysis oracle improvable tost

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oracle_improvable_tost_20260515T050343_result.json`
- **Structured JSON:** [`48d88e84b10a53c44277.json`](../../sessions/48/48d88e84b10a53c44277.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `oracle_improvable_tost.json`。

**Task 6 — Oracle-Improvable Fraction：**

| Config | n_valid | improvable | fraction | mean gain |
|--------|---------|-----------|----------|-----------|
| qwen_scierc_ner | 529 | 222 | 42.0% | +0.319 |
| qwen_scierc_re | 397 | 164 | 41.3% | +0.453 |
| llama_scierc_ner | 529 | 208 | 39.3% | +0.337 |
| qwen_conll_ner | 2756 | 251 | 9.1% | +0.448 |
| llama_conll_ner | 2756 | 110 | 4.0% | +0.461 |

SciERC 约 40% 的 instance 可通过 oracle selection 改善；CoNLL 由于 greedy 已经很强（90%+），仅 4-9% 可改善，但改善幅度大（~45pp）。

**Task 7 — TOST 等价检验：**

- **llama_conll_ner**：所有 5 个 signal 在 δ=0.01 和 δ=0.02 下均与 greedy 统计等价（p≈0）
- **qwen_conll_ner**：δ=0.02 下 sj/em/logprob/vc 等价；δ=0.01 下均不等价
- **SciERC NER**（Qwen/LLaMA）：仅 sj 和 logprob 在 δ=0.02 下等价
- **qwen_scierc_re**：所有 signal 均**不等价**——selection 显著低于 greedy（Δ 从 -1pp 到 -4.5pp）

---
