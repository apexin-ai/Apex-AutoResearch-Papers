# ssh verify throughput restart partial

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_throughput_restart_partial_20260523T204200_result.json`
- **Structured JSON:** [`4b22b0f6c0f15f1af284.json`](../../sessions/4b/4b22b0f6c0f15f1af284.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有数据收集完毕。

---

## 产出报告

### 1. N=17 Judge Throughput

**Snapshot 1**: 04:43:17 CST → **Snapshot 2**: 04:48:08 CST — 间隔 **291 秒**

| Judge | S1 行数 | S2 行数 | 5min Δ | items/hr | 错误 |
|-------|--------|--------|--------|----------|------|
| claude-sonnet-4.6-proxy | 11198 | 11238 | +40 | **495** | 0 |
| qwen3-235b-proxy | 8132 | 8165 | +33 | **408** | 0 |
| llama-3.3-70b | 6876 | 6907 | +31 | **383** | 0 |
| gemini-2.5-pro-proxy | 7659 | 7686 | +27 | **334** | 0 |
| qwen2.5-72b | 9740 | 9762 | +22 | **272** | 0 |
| mistral-large-2 | 9301 | 9323 | +22 | **272** | 0 |
| deepseek-v4-pro-proxy | 6748 | 6767 | +19 | **235** | 0 |

所有 7 个 N=17 进程正常运行（`--workers 10`），restart 日志 0 errors。

N=17 target 约 18,000 行/judge（18 target models × 500 questions × 2 position swap）。按当前速率，最快的 sonnet 约 14 小时完成，最慢的 deepseek 约 48 小时。

### 2. Partial Judge 状态

| Judge | 行数 | 目标(≈9000) | PID | 状态 |
|-------|------|------------|-----|------|
| GPT-5.5 | 8454 | ~9000 | 659566 | 运行中，+7 lines since restart |
| Claude Opus 4.7 | 9148 | ~9000 | 659677 | 运行中，+10 lines since restart |

- Opus 已超过 9000 行——可能包含重复/retry 条目，或者正在收尾剩余 position swap。进程仍在运行说明还有未完成的 item。
- GPT-5.5 还差 ~546 行，按 ~84 items/hr 估计约 6.5 小时完成。

### 3. 问题标记

- **无 500/429/error**：所有 7 个 N=17 restart 日志均为 0 errors
- **Opus log 重定向问题**：首次启动 opus 时日志文件创建失败（路径解析问题），第二次用绝对路径成功。日志在 `/root/gated_mfrm_judge_bias/exp001/logs/opus_partial_restart.log`
- **注意**：`python` 不在默认 PATH 中，启动 collect.py 需先 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`

---
