# diagnose flatnli r6 step30 health

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_flatnli-r6-step30-health_20260514T180957_result.json`
- **Structured JSON:** [`3d70c514f06699cfd094.json`](../../sessions/3d/3d70c514f06699cfd094.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## flatnli_r6 健康状态报告

**判定: MODE COLLAPSE CONFIRMED** — step 25 已完全坍塌

### 进程状态
- PID 76958: **仍在运行**, elapsed 44:52, RSS 3.3GB
- GPU 3: 54% util, 13647/32607 MiB
- 当前 step: ~26/100
- W&B 链接: 日志中未找到

### 最近 5 个 log point 的关键指标

| Step | frac_zero_std | f1_reward | flat_nli | total_reward | KL | grad_norm |
|------|:---:|:---:|:---:|:---:|:---:|:---:|
| 5 | 0.1 | 0.007 | 0.021 | 0.192 | **1.24亿** | 0.479 |
| 10 | 0.4 | 0.003 | 0.006 | 0.257 | 0.022 | 0.235 |
| 15 | 0.6 | 0.023 | 0.018 | 0.318 | 0.043 | 0.201 |
| 20 | 0.7 | 0.012 | 0.023 | 0.325 | 0.036 | 0.037 |
| **25** | **0.9** | **0.0** | **0.0** | 0.293 | 0.056 | 0.271 |

### 坍塌分析

- **frac_zero_std**: 0.1 → 0.4 → 0.6 → 0.7 → **0.9**, 单调上升，step 25 远超 0.8 警戒线
- **task reward 归零**: step 25 的 f1_reward 和 flat_nli_reward 均为 **精确 0.0** — 模型已完全丧失任务能力
- **reward 全部来自 format**: total_reward 0.293 ≈ format_reward 0.293
- **生成长度坍缩**: mean_length 从 774 → 400, reward_std 从 0.16 → 0.018（所有样本输出趋同）
- **坍塌起始**: step 20-25 之间，step 25 确认完全坍塌
- 模式与 extract_r4 一致，但更快（r4 是 step 30+，r6 在 step 25 就完全坍塌）

这个 run 继续跑没有意义，建议 kill。

---
