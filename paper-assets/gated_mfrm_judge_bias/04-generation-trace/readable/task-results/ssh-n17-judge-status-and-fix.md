# ssh n17 judge status and fix

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_judge_status_and_fix_20260523T231019_result.json`
- **Structured JSON:** [`2958bc2c4c2eb7a7bdfd.json`](../../sessions/29/2958bc2c4c2eb7a7bdfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个 API judges 已在写入结果。总结如下。

---

## 报告

### 1. 本地 judges（N=8）— 全部停止

vLLM 和 collect.py 进程均已死亡，结果文件停更于 5月22日。

| Judge | 已完成 | 总数 | 进度 |
|-------|--------|------|------|
| llama-3.3-70b | 1,238 | 9,000 | 13.8% |
| qwen2.5-72b | 915 | 9,000 | 10.2% |
| mistral-large-2 | 583 | 9,000 | 6.5% |

**无 N=17 config 存在** — 本地 judges 没有 N=17 配置文件，只有 N=8 版。需要你决定是否为本地 judges 也创建 N=17 config 并重启 vLLM。

### 2. N=8 API judges 也未跑完

| Judge | 已完成 | 总数 |
|-------|--------|------|
| claude-opus-4.7-proxy | 3,389 | 9,000 |
| gpt-5.5-proxy | 3,437 | 9,000 |
| claude-sonnet-4.6-proxy | 2,961 | 9,000 |
| qwen3-235b-proxy | 2,091 | 9,000 |
| gemini-2.5-pro-proxy | 1,916 | 9,000 |
| deepseek-v4-pro-proxy | 1,433 | 9,000 |

### 3. N=17 API judges — 已修复并启动

**修复后 target_models（14 个，已去掉 reference gpt-4-0314）：**
claude-opus-4.7, gemma-2-9b, gpt-3.5-turbo-0125, gpt-4-0613, gpt-4o, gpt-4o-mini, gpt-5.5, llama-3.1-8b, llama-3.3-70b, mistral-7b-v0.3, mistral-large-2, qwen2.5-72b, qwen2.5-7b, qwen3-8b

每个 judge 预期总量：14 × 500 × 2 = **14,000 judgments**

| Judge | Python PID | Workers | 初始写入 | 日志 |
|-------|-----------|---------|----------|------|
| claude-sonnet-4.6-proxy | 482393 | 4 | 66 | /tmp/judge_sonnet_n17.log |
| gemini-2.5-pro-proxy | 482451 | 4 | 58 | /tmp/judge_gemini_n17.log |
| deepseek-v4-pro-proxy | 482650 | 4 | 9 | /tmp/judge_deepseek_n17.log |
| qwen3-235b-proxy | 482745 | 10 | 18 | logs/qwen3_n17_autodl.log |

Qwen3 当前速度 0.3 items/s → ETA ~13 小时（约今晚 20:00 CST 完成）。

### 4. ELO / Arena 排名文件

exp001/ 下**未找到**任何 ELO 或 arena ranking 文件。

### 5. 注意事项

- **实际是 N=14 而非 N=17** — responses/ 目录有 15 个文件（含 reference），即 14 个 target。如果需要凑满 17 个，还需为 3 个模型生成 responses。
- 本地 judges 的 vLLM 全挂了，N=8 也没跑完 — 如需继续，需要重启 vLLM 并创建 N=17 config。
- qwen3 的 N=17 进程是外部启动的（workers=10），我杀掉了自己启动的重复进程。

---
