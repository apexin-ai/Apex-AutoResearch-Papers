# ssh mcmc data prep script

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_mcmc_data_prep_script_20260524T045008_result.json`
- **Structured JSON:** [`3c2b9c22e3ba980d88ee.json`](../../sessions/3c/3c2b9c22e3ba980d88ee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

## 报告

**数据格式**：N=17 与 N=8 JSONL 字段完全一致（`benchmark`, `item_id`, `model_a`, `model_b`, `judge`, `score`, `position`, `raw_output`, `status`, `timestamp`），data_loader 无需修改。

**Symlink 结构**（`exp003/judgment_data_n17/`）：

| Judge 目录 | 来源 | 原始记录 | status=ok |
|---|---|---|---|
| claude-sonnet-4.6-proxy | results/claude-sonnet-4.6-proxy_n17 | 4509 | 4509 |
| deepseek-v4-pro-proxy | results/deepseek-v4-pro-proxy_n17 | 2461 | 2215 |
| gemini-2.5-pro-proxy | results/gemini-2.5-pro-proxy_n17 | 2948 | 2347 |
| qwen3-235b-proxy | results/qwen3-235b-proxy_n17 | 3031 | 3018 |
| llama-3.3-70b | results/llama-3.3-70b-local_n17 | 448 | 448 |
| qwen2.5-72b | output_n17_qwen2.5-72b-local | 283 | 283 |

**Dry-run 结果**：data_loader 成功加载 → N=18 target models, I=74 items, J=6 judges, 4525 binary observations（56.6% sparsity）。Exposure scores 74/74 匹配。

**注意**：llama-3.3-70b（185 obs）和 qwen2.5-72b（113 obs）数据量明显偏少，覆盖的 item 数较少（分别 13 和 8 个 unique items）。N=8 时有的 3 个 judge（claude-opus-4.7-proxy, gpt-5.5-proxy, mistral-large-2）在 N=17 中尚无数据。

---
