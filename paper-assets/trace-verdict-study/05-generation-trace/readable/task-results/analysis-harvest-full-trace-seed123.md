# analysis harvest full trace seed123

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_harvest_full_trace_seed123_20260519T110606_result.json`
- **Structured JSON:** [`c4577e425d0ad864e4a4.json`](../../sessions/c4/c4577e425d0ad864e4a4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

收割完成。

**qwen7b_full_trace_label_only_seed123 结果汇总：**

| 指标 | seed123 | seed42 (参考) |
|------|---------|--------------|
| Accuracy | 86.89% | 86.22% |
| 95% CI | [85.0%, 88.7%] | — |
| pass F1 | 0.912 | — |
| fail F1 | 0.743 | — |
| Lift over majority | +15.4pp | — |

**操作完成：**
- ✅ Cron 已删除
- ✅ Registry → DONE (conclusion=success)
- ✅ Metrics、checkpoint_path、log_path 已录入

**GPU 状态：** cuda:0 已空闲，cuda:1 正在运行 seed456 训练。

---
