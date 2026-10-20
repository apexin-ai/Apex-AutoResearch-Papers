# analysis harvest submit cuda0 check cuda1

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_submit_cuda0_check_cuda1_20260518T213843_result.json`
- **Structured JSON:** [`865133f3046f63027317.json`](../../sessions/86/865133f3046f63027317.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

```
CUDA:0: 占用 by qwen15b_exception_only_seed456 (PID 468562) — 刚启动，tokenizing 中
        → seed456 训练+eval 完成后将自动接续 seed123_v2
CUDA:1: 占用 by codellama13b_full_trace_tail512_seed123 (PID 466403) — 训练中 step 183/444 (41%), ~14s/it, 预计 ~60min 后完成
```

**详细状态：**

| 实验 | 状态 | 说明 |
|------|------|------|
| qwen15b_exception_only_seed123 | **DONE/failed** | OOM step 3/444，原因：与 codellama13b 同时启动导致 GPU 0 内存被并发占满（45GB PyTorch allocated） |
| qwen15b_exception_only_seed456 | **RUNNING** (cuda:0) | 刚提交，正在 tokenize 数据 |
| qwen15b_exception_only_seed123_v2 | **PREPARING** | 排在 seed456 之后串行执行（同一 tmux session） |
| codellama13b_full_trace_tail512_seed123 | **RUNNING** (cuda:1) | step 183/444, ETA ~60min，含自动 eval |

seed123 OOM 的根因是两个任务同时抢 cuda:0，现在 GPU 0 专属给 qwen15b exception_only 系列，不会再冲突。

---
