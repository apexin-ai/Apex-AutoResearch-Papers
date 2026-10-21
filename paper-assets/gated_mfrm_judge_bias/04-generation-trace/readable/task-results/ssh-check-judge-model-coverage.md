# ssh check judge model coverage

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_judge_model_coverage_20260522T102213_result.json`
- **Structured JSON:** [`ccb39f53c3cc974e6dc5.json`](../../sessions/cc/ccb39f53c3cc974e6dc5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果已收集。汇总如下：

---

## 1. Judge × Target Model 交叉矩阵（OK judgments）

| Judge | gpt-3.5-turbo-0125 | gpt-4-0314 | gpt-4-0613 | **TOTAL** | **FAILED** |
|---|---|---|---|---|---|
| claude-opus-4.7-proxy | 480 | 480 | 478 | **1438** | 138 |
| claude-sonnet-4.6-proxy | 350 | 350 | 349 | **1049** | 124 |
| deepseek-v4-pro-proxy | 145 | 150 | 141 | **436** | 187 |
| gemini-2.5-pro-proxy | 148 | 151 | 144 | **443** | 382 |
| gpt-5.5-proxy | 599 | 630 | 591 | **1820** | 73 |
| llama-3.3-70b | 78 | 78 | 77 | **233** | 0 |
| mistral-large-2 | 22 | 22 | 20 | **64** | 4 |
| qwen2.5-72b | 46 | 47 | 47 | **140** | 4 |
| qwen3-235b-proxy | 232 | 232 | 230 | **694** | 118 |
| **TOTAL** | **2100** | **2140** | **2077** | **6317** | |

## 2. 覆盖度评估

| 指标 | 要求 | 实际 | 通过？ |
|---|---|---|---|
| Judges 数量 | ≥ 5 | **9** | YES |
| Target models 数量 | ≥ 6 | **3** | **NO** |
| 所有 cell ≥ 20 | 全部 | min cell = 20 | YES |
| Judges with ≥ 200 OK | — | 7/9 (mistral-large-2=64, qwen2.5-72b=140 不足) | — |

注意事项：
- **gemini-2.5-pro-proxy** 失败率极高（382/825 = 46%）
- **deepseek-v4-pro-proxy** 失败率也高（187/623 = 30%）
- 根目录合并文件仅含 llama/qwen/mistral 的 296 条，已跳过避免重复计数

## 3. exp-003 可否启动

**NO — target models 数量不足。** 当前只有 3 个 target models（gpt-3.5-turbo-0125, gpt-4-0314, gpt-4-0613），远低于 ≥6 的门槛。需要补充更多 target model 的 response 生成和 judgment 收集。

## 4. Local Judge 自动重启状态

- **auto-restart tmux session 运行中**，日志显示持续监控：
  - llama: **499/500**（几乎完成）
  - qwen: **496/500**（几乎完成）
- 5 个 API judge session 活跃：judge-opus, judge-sonnet, judge-deepseek, judge-gemini, judge-qwen3
- vLLM 推理服务运行中：vllm-llama, vllm-mistral
- **mistral-large-2**（64 OK）和 **qwen2.5-72b**（140 OK）数据量偏低，local judge 正在补充中

---
