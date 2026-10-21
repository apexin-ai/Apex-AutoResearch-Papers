# ops status check dispatch

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_status-check-dispatch_20260516T111523_result.json`
- **Structured JSON:** [`18e86559cbe9c8ea8069.json`](../../sessions/18/18e86559cbe9c8ea8069.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

| 实验 | 进程 | 状态 | 进度 |
|------|------|------|------|
| **qwen15b_full_trace_seed42** | PID 267886 存活，运行 5m42s | 训练中 | **52/444 steps (~12%)**, ~5.9s/it，预计还需 ~38 分钟 |
| **loop_only_seed123** | PID 261213 存活，运行 1h54m | 训练中 | **416/444 steps (~94%)**, ~15s/it，预计还需 ~7 分钟完成训练，之后进入 eval |

两个实验都没有 eval_results.json，均未完成。

- `loop_only_seed123` 即将完成训练（剩 28 steps），之后会自动运行 evaluate.py
- `qwen15b_full_trace_seed42` 刚启动不久，预计总训练时间约 44 分钟

---
