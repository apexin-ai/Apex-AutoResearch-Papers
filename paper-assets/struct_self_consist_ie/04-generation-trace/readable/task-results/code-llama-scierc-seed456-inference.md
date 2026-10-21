# code llama scierc seed456 inference

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_scierc_seed456_inference_20260518T191311_result.json`
- **Structured JSON:** [`5962c1ff6775718229d3.json`](../../sessions/59/5962c1ff6775718229d3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

**LLaMA-3.1-8B SciERC seed=456 — 5-signal + DGS 分析**

| | Full (n=529) | Conditional (n=478) |
|---|---|---|
| Greedy F1 | 0.6457 | 0.7146 |
| Oracle F1 | 0.7574 | 0.7999 |
| Headroom | 0.1117 | 0.0853 |

**5-Signal ρ (full split):**

| Signal | ρ | AUROC |
|---|---|---|
| voting_conf | 0.4135 | 0.7113 |
| SJ | 0.3663 | 0.7061 |
| FK | 0.3115 | 0.6723 |
| EM | 0.3088 | 0.7538 |
| logprob | 0.1911 | 0.5636 |

**DGS:** 27.6% degenerate (146/529)。DGS F1=0.6454，与 Greedy 持平（−0.03pp, CI crosses zero）。Non-degenerate subset 上 LP 选择也无增益（−0.05pp）。

与 seed=42/123 一致：结构性信号（SJ/FK/voting_conf）稳定优于 logprob，DGS 在 LLaMA SciERC 上无显著 selection gain。Registry 已注册为 `exp_llama_scierc_seed456`。

---
