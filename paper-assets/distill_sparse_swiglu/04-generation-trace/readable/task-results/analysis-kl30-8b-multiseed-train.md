# analysis kl30 8b multiseed train

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl30_8b_multiseed_train_20260518T005819_result.json`
- **Structured JSON:** [`54241797f1caae289fd9.json`](../../sessions/54/54241797f1caae289fd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练尚未完成，进程仍在运行：

| Experiment | Current Step | Loss (last) | Sparsity (last) | Status |
|---|---|---|---|---|
| kl30_8b_s123_train | 830/1000 | 0.197 | 0.285 | Running (PID 34700) |
| kl30_8b_s456_train | 810/1000 | 0.160 | 0.289 | Running (PID 35045) |

训练指标与预期一致（loss ~0.16, sparsity ~0.285-0.29）。

关键发现：两个 nohup 脚本已经内置了 Phase 2 eval（benchmark_eval.py 在 train.py 完成后自动执行），不需要单独提交 eval job。eval 日志会追加到同一个 log 文件中。

预估剩余：训练约 5-7 分钟完成，之后自动进入 eval 阶段。建议等训练+eval 全部完成后再更新 registry。要我设一个定时检查吗？

---
