# ssh restart api judges new key

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_restart-api-judges-new-key_20260524T145413_result.json`
- **Structured JSON:** [`c353b525dfbc8f7a28af.json`](../../sessions/c3/c353b525dfbc8f7a28af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### Key 配置方式
修改了 `exp001/judge_interface.py`，将 `_PROXY_URL` 从死掉的 `http://47.94.22.126/v1` 改为 `https://openrouter.ai/api/v1`，`_PROXY_KEY` 更新为新 OpenRouter key。模型名同步改为 OpenRouter 格式（`deepseek/deepseek-v4-pro`、`qwen/qwen3-235b-a22b`、`google/gemini-2.5-pro`、`anthropic/claude-sonnet-4.6`）。

### 启动结果

| Judge | PID | 状态 |
|-------|-----|------|
| DeepSeek-v4-pro | 592328 | ✅ 正常产出（9,824→9,861） |
| Qwen3-235B | 592432 | ✅ 正常产出（11,550→11,648） |
| Gemini 2.5 Pro | — | ❌ 403 "This model is not available in your region" |
| Claude Sonnet 4.6 | — | ❌ 403 同上 |

### 失败原因
OpenRouter 对中国 IP 屏蔽了 Google 和 Anthropic 模型。旧 proxy（47.94.22.126）已不可达（超时）。AutoDL 的 `network_turbo` 代理出口仍为中国 IP，无法绕过。

### 6 judge 最新 JSONL 行数

| Judge | 行数 |
|-------|------|
| deepseek-v4-pro-proxy_n17 | 9,861 |
| qwen3-235b-proxy_n17 | 11,648 |
| gemini-2.5-pro-proxy_n17 | 11,253 |
| claude-sonnet-4.6-proxy_n17 | 14,255 |
| llama-3.3-70b-local_n17 | 14,848 |
| qwen2.5-72b-local_n17 | 10,173 |

### 当前 collect.py PID 列表
- 584106 — LLaMA-3.3-70B (local, workers=64)
- 584197 — Qwen2.5-72B (local, workers=64)
- 592328 — DeepSeek-v4-pro (OpenRouter, workers=10)
- 592432 — Qwen3-235B (OpenRouter, workers=10)

### Gemini/Sonnet 恢复方案
需要一个非中国 IP 的代理来访问 OpenRouter 的 Google/Anthropic 模型。选项：
1. 恢复旧 proxy（47.94.22.126）
2. 提供一个海外 HTTP 代理地址
3. 在海外服务器上运行 Gemini/Sonnet 的采集

---
