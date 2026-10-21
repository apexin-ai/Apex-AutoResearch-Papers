# ssh check running eval progress

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_running_eval_progress_20260521T192458_result.json`
- **Structured JSON:** [`2a17c6a73e0aa51708a7.json`](../../sessions/2a/2a17c6a73e0aa51708a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个实验都在正常运行。汇总如下：

| 实验 | 服务器 | 进度 | 已运行 | 预估剩余 | 中间 Acc |
|------|--------|------|--------|----------|----------|
| grpo_standard_25_v2 | westb-23072 cuda:0 | **320/500 (64%)** | 5h32m | ~2h40m | — |
| grpo_random_20_v2 | westd-29022 cuda:1 | **280/500 (56%)** | 5h25m | ~2h24m | 11.2% @250 |
| sft_random_20 | westd-29022 cuda:3 | **236/500 (47%)** | 4h36m | ~5h~6h30m | 12.0% @200 |

关键数据：
- **grpo_standard_25_v2**: 最快，320/500，~53s/it，预计再 2.5-3h 完成
- **grpo_random_20_v2**: 280/500，速度波动大(40-100s/it)，tqdm 显示剩余 ~2h24m 但实际可能 3-4h
- **sft_random_20**: 最慢，236/500，~89s/it，tqdm 显示剩余 ~6h33m；起步晚了约 48 分钟

三个进程日志都在持续输出进度条，均处于活跃状态。

---
