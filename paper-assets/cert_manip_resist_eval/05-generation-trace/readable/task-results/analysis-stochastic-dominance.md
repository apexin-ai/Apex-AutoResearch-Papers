# analysis stochastic dominance

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stochastic-dominance_20260523T001734_result.json`
- **Structured JSON:** [`592daf9feb3bbbb6b118.json`](../../sessions/59/592daf9feb3bbbb6b118.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| Scope | Dominant ordered pairs | / 210 | Proportion |
|-------|----------------------|-------|-----------|
| **Global (12 conditions)** | 61 | 210 | **29.0%** |
| **MMLU (6 conditions)** | 69 | 210 | 32.9% |
| **ARC (6 conditions)** | 74 | 210 | 35.2% |

- **Unordered pairs with dominance**: 61/105 (58.1%) — 所有 61 个 ordered pairs 都是单向的（无双向 dominance）
- **No total ordering** — 14 个相邻 pair 打破了链式排序
- **最常被 dominate 的 judges**: gpt-5.5 (11), gemini-3.5-flash (11), gemini-3.1-pro-preview (10) — 这些是最强的 judges（ASR 最低，几乎不被攻击翻转），所以它们被更弱的 judges dominate
- **最常 dominate 别人的 judges**: claude-3-haiku (10), qwen2.5-14b (8), llama3.1-8b (7) — 这些是最弱的 judges（ASR 最高）

Theorem 1 的 pointwise stochastic dominance 在约 29% 的 ordered pairs 中成立，覆盖了 58% 的 unordered pairs。结果已保存到 `artifacts/results/plan001/stochastic_dominance.json`。

---
