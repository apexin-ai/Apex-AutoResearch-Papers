# ops check codellama and qwen15b status

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_codellama_and_qwen15b_status_20260518T014533_result.json`
- **Structured JSON:** [`da757d406553d8ccb641.json`](../../sessions/da/da757d406553d8ccb641.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验状态汇总

### 1. codellama13b_full_trace_tail256_seed42 (cuda:0)
- **进程**: 存活，tmux session 运行中（09:41 启动）
- **训练进度**: step 52/444 (12%)，约 4 分钟已过
- **速度**: ~5 s/step，预计总训练时间 ~37 分钟
- **Eval**: 未完成（eval_results.json 不存在）

### 2. codellama13b_full_trace_head2048_seed42 (cuda:1)
- **进程**: 存活，tmux session 运行中（07:42 启动）
- **训练进度**: step 251/444 (57%)，已训练 ~2h02m
- **速度**: ~28 s/step，预计剩余 ~1h30m
- **Eval**: 未完成（eval_results.json 不存在）

### 3. qwen15b_full_trace_tail1024_seed42
- **Eval**: 已完成，结果如下：

| Metric | Value |
|--------|-------|
| **Accuracy** | **96.55%** |
| Majority baseline | 71.51% |
| Lift | +25.04% |
| Pass precision | 96.44% |
| Pass recall | 98.82% |
| Pass F1 | 97.62% |
| Fail precision | 96.86% |
| Fail recall | 90.86% |
| Fail F1 | 93.76% |
| N | 1190 |
| Accuracy 95% CI | [95.46%, 97.56%] |

---
