# ops nomarker submit v4

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_nomarker_submit_v4_20260516T154236_result.json`
- **Structured JSON:** [`aba7cf5237c5cfcfe9dd.json`](../../sessions/ab/aba7cf5237c5cfcfe9dd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练失败。日志显示：

```
train_sft.py: error: unrecognized arguments: --epochs 3
```

脚本不接受 `--epochs` 参数。GPU 0 上的进程 (PID 285223) 已退出（显存 15384MiB 是残留，进程已报错终止）。

需要确认正确的 epoch 参数名（可能是 `--num_train_epochs` 或类似）。是否要我查看脚本的参数定义？

---
