# monitor westd gpu status check

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_westd_gpu_status_check_20260516T162234_result.json`
- **Structured JSON:** [`c0d364fefdf5dc8eb24c.json`](../../sessions/c0/c0d364fefdf5dc8eb24c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报如下：

## GPU 状态 (westd-11672)

| GPU | 显存占用 | 进程 | 状态 |
|-----|---------|------|------|
| cuda:0 | 83180/97887 MiB (94%) | PID 21408 grpo_rasp_25 (30min) + PID 22389 eval_grpo_rasp_25_qwen_math (22min) | 训练正常 + eval 仍在跑 |
| cuda:1 | 77618/97887 MiB (97%) | PID 21488 sft_standard_25 (30min) + PID 22465 eval_grpo_standard_25_qwen_math (22min) | 训练正常 + eval 仍在跑 |
| cuda:2 | 0 MiB | 空 | Qwen 20% eval 已退出 |
| cuda:3 | 0 MiB | 空 | Qwen 20% eval 已退出 |

## DeepSeek 25% 进程
- **PID 21408** (grpo_rasp_25): 运行 30 分钟，正常
- **PID 21488** (sft_standard_25): 运行 30 分钟，正常

## 注意
cuda:0/1 上各有一个 **25% Qwen Math eval** 进程与 DeepSeek 训练共享 GPU，已跑 22 分钟，结果文件尚未生成。

## 已完成的 Qwen Math eval (20% 剪枝率)

| 模型 | GSM8K Accuracy |
|------|---------------|
| eval_grpo_rasp_20_qwen_math | **72.5%** |
| eval_grpo_standard_20_qwen_math | **70.5%** |

RASP 20% 比 Standard 20% 高 2 个点。25% 的 eval 仍在运行中，预计稍后完成。

---
