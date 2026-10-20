# ssh kill api judges check coverage

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_api_judges_check_coverage_20260522T194015_result.json`
- **Structured JSON:** [`e31f1d1a00628647cb52.json`](../../sessions/e3/e31f1d1a00628647cb52.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 已杀进程

| Judge | PID | 状态 |
|---|---|---|
| claude-opus-4.7-proxy | — | 进程已不存在（自行退出） |
| gpt-5.5-proxy | 332533 | ✓ 已杀 |
| claude-sonnet-4.6-proxy | 332567 | ✓ 已杀 |
| deepseek-v4-pro-proxy | 332582 | ✓ 已杀 |
| gemini-2.5-pro-proxy | 332599 | ✓ 已杀 |
| qwen3-235b-proxy | 332616 | ✓ 已杀 |

**保留运行中**：llama-3.3-70b (332474), qwen2.5-72b (332493), mistral-large-2 (332512)

### 2. Sonnet 未保留

Sonnet 最近写入的全是 `status=failed` 记录（402 Insufficient balance），已杀掉。

### 3. 覆盖率（成功判定 / 9000 目标）

| Judge | Total | OK | Fail | Unique OK | Coverage |
|---|---|---|---|---|---|
| **gpt-5.5-proxy** | 8447 | 7221 | 1226 | **7221** | **80.2%** |
| **qwen2.5-72b** ★ | 6720 | 6439 | 281 | **6439** | **71.5%** |
| claude-opus-4.7-proxy | 9138 | 5522 | 3616 | 5522 | 61.4% |
| claude-sonnet-4.6-proxy | 8774 | 5041 | 3733 | 5041 | 56.0% |
| mistral-large-2 ★ | 4610 | 4304 | 306 | 4287 | 47.6% |
| qwen3-235b-proxy | 7235 | 3535 | 3700 | 3535 | 39.3% |
| llama-3.3-70b ★ | 3028 | 3028 | 0 | 3028 | 33.6% |
| gemini-2.5-pro-proxy | 6827 | 2526 | 4301 | 2526 | 28.1% |
| deepseek-v4-pro-proxy | 6129 | 2237 | 3892 | 2237 | 24.9% |

★ = 本地 judge，仍在运行中

### 4. 可用性判定

- **≥ 80%**：gpt-5.5-proxy（80.2%）— 唯一达标
- **< 80%**：其余 8 个 judge 均未达标。qwen2.5-72b（71.5%）和 claude-opus-4.7-proxy（61.4%）相对较高但仍不足。3 个本地 judge 仍在运行，覆盖率会继续增长。

---
