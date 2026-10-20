# monitor rtx6000 check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_rtx6000_check_20260522T191647_result.json`
- **Structured JSON:** [`fa3f23a98571134bfa46.json`](../../sessions/fa/fa3f23a98571134bfa46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态报告

### exp-001 — 数据收集 pipeline: **STILL_RUNNING (部分 FAILING)**

**vLLM 进程**：3 个本地 judge 的 vLLM server 运行中
- `llama-3.3-70b` @ port 8001 ✓
- `qwen2.5-72b` @ port 8002 ✓
- `mistral-large` @ port 8003 ✓

**9 个 judge 收集进度**：

| Judge | 已收集 | 总量 | 进度 | 状态 |
|-------|--------|------|------|------|
| claude-opus-4.7-proxy | 8519 | — | — | **402 Insufficient balance** |
| claude-sonnet-4.6-proxy | 8025 | 7282 | 84% | 运行中（偶发 402，仍在推进） |
| deepseek-v4-pro-proxy | 5379 | — | — | **402 Insufficient balance** |
| gemini-2.5-pro-proxy | 6077 | — | — | **402 Insufficient balance** |
| gpt-5.5-proxy | 7698 | — | — | **402 Insufficient balance** |
| qwen3-235b-proxy | 6484 | — | — | **402 Insufficient balance** |
| llama-3.3-70b | 2892 | 8311 | 35% | 运行中，ETA ~21h |
| qwen2.5-72b | 6071 | 8534 | 71% | 运行中，ETA ~7h |
| mistral-large-2 | 4169 | 8742 | 48% | 运行中，ETA ~10.5h |

**关键问题**：6 个 API proxy judge（opus、deepseek、gemini、gpt-5.5、qwen3-235b，以及 opus）全部报 **402 Insufficient balance**，持续重试中。需要充值 API 余额才能继续。sonnet 也有间歇性 402 但还在出数据。

---

### exp-002 — exposure estimation: **COMPLETED**

- 进程已结束（无 exp002 进程）
- 产出完整：317 items × 9 judges × 8 target models
- `exposure_scores.csv`: 318 行（含 header）
- 还生成了 3 组 sensitivity 分析（100_0, 50_50, 90_10）
- summary.json 确认数据有效

---

### exp-009 — MCMC simulation: **STILL_RUNNING**

- 进度：**187/200**（93.5%）
- 已运行 ~18.1h，ETA ~75min
- 当前在 `rho=0.9` 区段跑最后的 seeds
- 有 UserWarning（MCMC chains sequential 而非 parallel），不影响正确性

---
