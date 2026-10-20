# ssh exp019 mfrm delta theta

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp019_mfrm_delta_theta_20260523T085423_result.json`
- **Structured JSON:** [`4dbf67a86ca30170ad9f.json`](../../sessions/4d/4dbf67a86ca30170ad9f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp-019 完成。

**结果**：

| Model | θ_MFRM | θ_GMFRM | Δθ | c_n |
|---|---|---|---|---|
| gpt-3.5-turbo-0125 | -2.487 | -3.274 | **+0.786** | 5.587 |
| gpt-4-0613 | -1.446 | -1.877 | **+0.431** | 4.168 |
| qwen2.5-72b | 1.213 | 1.178 | +0.035 | 2.961 |
| llama-3.3-70b | 0.518 | 0.539 | -0.022 | 2.478 |
| gemma-2-9b | -0.661 | -0.500 | -0.161 | 1.654 |
| qwen3-8b | 0.208 | 0.513 | **-0.305** | 1.178 |
| gpt-4o-mini | 1.064 | 1.432 | **-0.368** | 0.934 |
| gpt-4o | 1.591 | 1.988 | **-0.397** | 0.880 |

**Spearman ρ(Δθ, c_n) = 1.0000** — 完美秩相关。高 c_n 模型（gpt-3.5, gpt-4-0613）在 MFRM-only 中 ability 被系统性高估，低 c_n 模型（gpt-4o, gpt-4o-mini）被低估。contamination bias 在不建模时完全被吸收进 θ。

---
