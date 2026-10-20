# ssh urgent 5task rtx6000 check

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_urgent_5task_rtx6000_check_20260522T160902_result.json`
- **Structured JSON:** [`386e9558170875c3a9b9.json`](../../sessions/38/386e9558170875c3a9b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 状态报告

### 1. exp-009 进度

| 指标 | 值 |
|------|-----|
| PID | 112923 (alive, 15h04m) |
| 进度 | **155/200** (77.5%) |
| 当前 | rho=0.9, seed=4 |
| 已用 | ~54,185s (~15h) |
| ETA | **~15,731s (~4.4h)** |
| GPU | GPU 0 (61% util, 74.3/97.9 GB) |

输出文件已生成: `bias_vs_rho.csv`, `bias_vs_rho.png`, `cn_recovery_scatter.png`

---

### 2. Judge 收集状态

**9 个 judge 全部在线收集中**（均运行 ~4h）：

| Judge | 已收集 | 进度 | ETA | 状态 |
|-------|--------|------|-----|------|
| claude-opus-4.7 | 4,826 | 2030/6871 (30%) | ~7.8h | 正常 |
| claude-sonnet-4.6 | 4,368 | 2030/7282 (28%) | ~8.6h | 正常 |
| gpt-5.5 | 4,646 | 2030/6601 (31%) | ~8.6h | 正常 |
| qwen3-235b | 3,087 | — | — | 运行中（无日志尾部） |
| gemini-2.5-pro | 2,795 | — | — | 运行中（无日志尾部） |
| deepseek-v4-pro | 2,157 | — | — | 运行中（无日志尾部） |
| llama-3.3-70b | 1,931 | — | — | 运行中（无日志尾部） |
| qwen2.5-72b | 1,445 | 960/8534 (11%) | ~31.9h | **⚠ 有 context length 错误** |
| mistral-large-2 | 916 | 590/8742 (7%) | ~52.7h | **⚠ 有 context length 错误** |

**总计**: 26,467 judgments

**⚠ 关键问题**: qwen2.5-72b 和 mistral-large-2 的 vLLM 实例 `max-model-len=4096`，部分 prompt 超限（3073 input + 1024 output = 4097），导致反复重试失败。这两个 judge 速度极慢且会丢失部分判断。需要将 `max-model-len` 提高到至少 8192。

---

### 3. API Response 生成进度

| Model | 进度 | 状态 |
|-------|------|------|
| claude-opus-4.7 | 500/500 | ✓ |
| gemma-2-9b | 500/500 | ✓ |
| gpt-3.5-turbo-0125 | 500/500 | ✓ |
| gpt-4-0314 | 500/500 | ✓ |
| gpt-4-0613 | 500/500 | ✓ |
| gpt-4o | 500/500 | ✓ |
| gpt-4o-mini | 500/500 | ✓ |
| llama-3.3-70b | 500/500 | ✓ |
| qwen2.5-72b | 500/500 | ✓ |
| qwen3-8b | 500/500 | ✓ |
| gpt-5.5 | **495/500** | ⚠ 差 5 条 |
| mistral-large-2 | **362/500** | ⚠ 差 138 条 |
| claude-sonnet-4.6 | **200/500** | ⚠ 差 300 条 |

2 个生成进程仍在运行：`generate_responses.py --group openai`（10h22m）和 `--group proxy_nocredit`（7h26m）。

---

### 4. GPU 状态

| GPU | 利用率 | 显存 | 用途 |
|-----|--------|------|------|
| 0 | 61% | 74.3 / 97.9 GB | exp-009 (MCMC) |
| 1 | 100% | 89.7 / 97.9 GB | vLLM 服务 |
| 2 | 100% | 91.0 / 97.9 GB | vLLM Llama-3.3-70B (port 8001) |
| 3 | 100% | 88.1 / 97.9 GB | vLLM Mistral-Large (port 8003) |

---

### 需要关注的问题

1. **qwen2.5-72b / mistral-large-2 vLLM context length 不足** — `max-model-len=4096` 导致部分 judge prompt 失败重试。qwen2.5-72b (port 8002) 当前 ETA 31.9h、mistral 52.7h，实际会更久因为错误重试浪费时间。建议重启这两个 vLLM 实例并将 `max-model-len` 提高到 8192。
2. **3 个模型 response 未满 500** — claude-sonnet-4.6 (200)、mistral-large-2 (362)、gpt-5.5 (495)，生成进程仍在跑。

---
