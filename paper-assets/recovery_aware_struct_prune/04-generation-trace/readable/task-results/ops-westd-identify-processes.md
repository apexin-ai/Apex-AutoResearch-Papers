# ops westd identify processes

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd_identify_processes_20260517T130640_result.json`
- **Structured JSON:** [`b7886ec6aeb00850f145.json`](../../sessions/b7/b7886ec6aeb00850f145.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## GPU 进程识别

| GPU | PID | 任务 | 脚本 | 模型 | 输出路径 |
|-----|-----|------|------|------|---------|
| **0** | 23707 | **eval_humaneval_unpruned_2048** | `eval_humaneval.py` | `DeepSeek-R1-Distill-Qwen-7B` (unpruned) | `results/eval_humaneval_unpruned_2048.json` |
| 1 | 14556 | eval_math500_grpo_standard_20 (已知) | `eval_math500.py` | `grpo_stage2_standard_20_v8/checkpoint-50` | `results/eval_math500_grpo_standard_20.json` |
| **2** | 23785 | **eval_humaneval_sft_rasp_20_2048** | `eval_humaneval.py` | `sft_rasp_20_westd` | `results/eval_humaneval_sft_rasp_20_2048.json` |
| 3 | 11896 | eval_math500_grpo_rasp_20_v2 (已知) | `eval_math500.py` | `grpo_stage2_rasp_20_v9` | `results/math500_grpo_rasp_20.json` |

两个"未知"进程都是 HumanEval eval，使用 `max_new_tokens=2048`（比之前的 HumanEval eval 更长的生成长度）。

## 运行进度

| 任务 | 进度 | 当前指标 | 预估剩余 |
|------|------|---------|---------|
| GPU 0: humaneval_unpruned_2048 | **71/164 (43%)** | pass@1=0.633 (60题时) | ~42 min |
| GPU 1: math500_grpo_standard_20 | **91/500 (18%)** | acc=0.36 (50题时) | ~15h+ (非常慢) |
| GPU 2: humaneval_sft_rasp_20_2048 | **106/164 (65%)** | pass@1=0.150 (100题时) | ~23 min |
| GPU 3: math500_grpo_rasp_20_v2 | **141/500 (28%)** | acc=0.33 (100题时) | ~14h+ (非常慢) |

## 已完成的结果（今日，按时间倒序）

| 文件 | 时间 | 关键指标 |
|------|------|---------|
| eval_math500_unpruned.json | 19:09 | **accuracy=0.736** |
| eval_humaneval_grpo_standard_20.json | 18:36 | **pass_at_1=0.0183** |
| eval_math500_sft_standard_20.json | 17:57 | **accuracy=0.260** |
| eval_math500_sft_rasp_20.json | 17:19 | **accuracy=0.242** |
| eval_humaneval_sft_standard_20.json | 16:14 | **pass_at_1=0.0305** |
| eval_humaneval_sft_rasp_20.json | 15:35 | **pass_at_1=0.0732** |
| eval_humaneval_grpo_rasp_20.json | 15:11 | **pass_at_1=0.1037** |
| eval_humaneval_unpruned.json | 14:39 | **pass_at_1=0.0183** |

注意：GPU 1 和 GPU 3 的 MATH500 eval 速度极慢（每题 ~3-5 分钟），预计还需要 14-15 小时才能完成。这是因为 GRPO 模型生成长度很长（max_new_tokens=4096）。

---
