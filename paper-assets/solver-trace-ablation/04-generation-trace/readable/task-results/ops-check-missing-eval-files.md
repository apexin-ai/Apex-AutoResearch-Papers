# ops check missing eval files

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-missing-eval-files_20260515T151751_result.json`
- **Structured JSON:** [`9c5db5a404037a10c746.json`](../../sessions/9c/9c5db5a404037a10c746.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总结果：

## 文件存在性报告

### 核心实验

| # | 实验名 | 状态 | 路径 |
|---|--------|------|------|
| 1 | plan001_exec_only_s42 | **EXISTS** | `/root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s42.json` |
| 2 | plan001_exec_only_s43_r4 | **EXISTS** | `/root/solver-trace-ablation/outputs/eval_sta_plan001_exec_only_s43_r4.json` |
| 3 | plan009_sft_baseline_s42_1000 | **EXISTS** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s42_1000/eval_sta_results.json` |
| 4 | plan009_sft_baseline_s43_1000 | **EXISTS** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s43_1000/eval_sta_results.json` |
| 5 | plan009_sft_baseline_s44_1000 | **EXISTS** | `/root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000/eval_sta_results.json` |
| 6 | plan013_random_reward_s42_r4 | **EXISTS** | `/root/solver-trace-ablation/outputs/eval_sta_plan013_random_reward_s42_r4.json` |
| 7 | plan018_additive_random_b01_s42_1000_r3 | **EXISTS** | `/root/autodl-tmp/outputs/plan018_additive_random_b01_s42_1000_r3/eval_results.json` |

### Pilot runs（可忽略）

| # | 实验名 | 状态 | 路径 |
|---|--------|------|------|
| 8 | exp1_isr_b03_s42_1000 | EXISTS | `/root/autodl-tmp/outputs/exp1_isr_b03_s42_1000/eval_results.json` |
| 9 | exp1_isr_b03_s43_eval | EXISTS | `/root/autodl-tmp/outputs/exp1_isr_b03_s43_eval/eval_results.json` |
| 10 | exp1_isr_b03_s44_r2_eval | EXISTS | `/root/autodl-tmp/outputs/exp1_isr_b03_s44_r2_eval/eval_results.json` |

**全部 10 个文件均存在，无丢失。**

## classify_h7 分类结果

| 实验 | Proved | H7 | H1 | H8 | Genuine | Gen% |
|------|--------|----|----|----|---------| -----|
| plan001_exec_only_s42 | 93 | 1 | 80 | 6 | 7 | 7.5% |
| plan001_exec_only_s43_r4 | 13 | 0 | 13 | 1 | 0 | 0.0% |
| plan009_sft_s42_1000 | 13 | 0 | 1 | 0 | 12 | 92.3% |
| plan009_sft_s43_1000 | 11 | 0 | 1 | 0 | 10 | 90.9% |
| plan009_sft_s44_1000 | 15 | 0 | 1 | 0 | 14 | 93.3% |
| plan013_random_reward_s42_r4 | 100 | 100 | 0 | 0 | 0 | 0.0% |
| plan018_random_b01_s42_1000_r3 | 97 | 97 | 0 | 0 | 0 | 0.0% |

JSON 已保存到 `/root/autodl-tmp/outputs/d086_missed_classify_h7.json`（注意其中 plan009 三条被覆盖为一条 "results"，单独运行的结果见上表）。

---
