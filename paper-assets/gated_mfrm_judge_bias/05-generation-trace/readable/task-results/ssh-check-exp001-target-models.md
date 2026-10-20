# ssh check exp001 target models

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp001_target_models_20260522T052851_result.json`
- **Structured JSON:** [`d5d20e8d42d770d97997.json`](../../sessions/d5/d5d20e8d42d770d97997.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

---

## 1. Target Models

**当前实际评测 3 个 target models**（数据文件在 `data/arena_hard/responses/`）：

| # | Target Model | Responses |
|---|---|---|
| 1 | gpt-3.5-turbo-0125 | 500 |
| 2 | gpt-4-0314 | 500 |
| 3 | gpt-4-0613 | 500 |

`config.yaml` 列了 22 个 target models，但只有这 3 个有实际 response 数据。所有运行中的 per-judge config 也只指定了这 3 个。

**Reference model**: `gpt-4-0314`（pairwise 对比的基准）

---

## 2. 各 Judge 收集进度

Arena-Hard pairwise + position_swap → 每个 judge 需 3 models × 500 prompts × 2 positions = **3000 judgments**。

| Judge | 已收集 | 进度 | 错误数 | 状态 |
|---|---|---|---|---|
| llama-3.3-70b (local) | ~91* | ~3.0% | 0 | tmux 运行中 |
| qwen2.5-72b (local) | ~91* | ~3.0% | 0 | tmux 运行中 |
| mistral-large-2 (local) | ~91* | ~3.0% | 0 | tmux 运行中（刚启动 12:57） |
| gpt-5.5-proxy | 406 | 13.5% | 21 | tmux 运行中 |
| claude-opus-4.7-proxy | 428 | 14.3% | 99 | tmux 运行中 |
| claude-sonnet-4.6-proxy | 390 | 13.0% | 83 | tmux 运行中 |
| gemini-2.5-pro-proxy | 320 | 10.7% | **286** | tmux 运行中（89% 失败率极高） |
| deepseek-v4-pro-proxy | 204 | 6.8% | 133 | tmux 运行中（65% 失败率） |
| qwen3-235b-proxy | 215 | 7.2% | 81 | tmux 运行中 |

\* 三个 local judges 共用 `results/arena_hard_judgments.jsonl`（274 行，三个 judge 混写），各约 ~91 行。

---

## 3. 数据结构

- **500 prompts**（`data/arena_hard/prompts.jsonl`）
- 每个 prompt 有 3 个 target model 的 responses
- Pairwise 模式：target_model vs reference_model (gpt-4-0314)，AB + BA 两个位置
- 每个 judge 独立 JSONL 输出，支持 incremental resume

---

## 4. collect.py 核心逻辑

遍历顺序：`for item → for target_model → for judge → for position(AB/BA)`。对每个组合调 `judge.evaluate(prompt, resp_target, resp_ref, swap)`，写入 JSONL。通过 `load_completed()` 实现断点续传，`RateLimiter` 控制每个 judge 的 RPM。

---

## 5. 关注点

- **gemini-2.5-pro** 错误率 89%（286/320），**deepseek-v4-pro** 65%（133/204），需要排查 API 问题
- 3 个 local judges 写同一个文件，可能存在并发写入竞争
- config.yaml 规划了 22 个 target models，当前只跑了 3 个——后续需要收集剩余 19 个的 responses

---
