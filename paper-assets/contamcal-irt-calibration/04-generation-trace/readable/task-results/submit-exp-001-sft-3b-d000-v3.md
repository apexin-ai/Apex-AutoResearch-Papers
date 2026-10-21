# submit exp 001 sft 3B d000 v3

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_submit_exp_001_sft_3B_d000_v3_20260515T160651_result.json`
- **Structured JSON:** [`942a528589372e98db43.json`](../../sessions/94/942a528589372e98db43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 5 上正在跑 `evaluate.py`（d025_s123 的 eval），已运行 33 分钟。

**无法提交 exp_001_sft_3B_d000_v3 到 GPU 5** — 当前有评估任务占用（PID 584315，`Qwen2.5-3B_d025_s123_para_aligned` eval，显存 13GB）。

选项：
1. 等该 eval 完成后再提交（eval 通常 1-2 小时）
2. 换一个空闲 GPU（当前 6 块全部被占用，没有空闲的）
3. 如果某个任务可以中断/已完成，kill 后腾出 GPU

需要你决定怎么处理。

---
