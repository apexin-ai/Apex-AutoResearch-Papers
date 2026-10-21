# read eval results check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_read_eval-results-check_20260514T142221_result.json`
- **Structured JSON:** [`37d10bded7c57c6a47e2.json`](../../sessions/37/37d10bded7c57c6a47e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

**1. plan018-s44 eval 结果：** `NO_EVAL_RESULTS`（文件不存在）

**2. plan009-sft eval 结果：** 存在，关键指标：
| 指标 | 值 |
|------|-----|
| n_problems | 100 |
| n_proved | 14 |
| prove_rate | 0.14 |
| mean_isr | 0.08 |
| proved_only_mean_isr | 0.5713 |
| by_type: true | 13/34 proved (38.2%), mean_isr=0.225 |
| by_type: unknown | 1/41 proved (2.4%), mean_isr=0.008 |
| by_type: false | 0/25 proved (0%), mean_isr=0.0 |

**3. plan006 训练进度：**

| 实验 | 当前步数 | 最新 reward_mean | prove_rate | isr_mean | 最新时间 |
|------|---------|-----------------|------------|----------|----------|
| plan006_prolog_exec_s44 | 151 | 0.50 | 0.50 | 0.094 | 14:22:39 UTC |
| plan006_prolog_exec_s43_r3 | 122 | 0.625 | 0.625 | 0.058 | 14:22:29 UTC |

两个 plan006 实验都在活跃训练中（时间戳均为几分钟前）。

---
