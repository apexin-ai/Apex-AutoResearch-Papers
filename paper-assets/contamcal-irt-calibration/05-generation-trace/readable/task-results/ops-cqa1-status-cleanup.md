# ops cqa1 status cleanup

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-status-cleanup_20260521T103340_result.json`
- **Structured JSON:** [`d937dfe12a997c46f809.json`](../../sessions/d9/d937dfe12a997c46f809.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有进程已清理完毕。

```
GPU 状态: 1x RTX 4090 D, 0MiB 占用, 0% util, 完全空闲
PID 460555: 已 kill（原为错误版本 evaluate.py 跑 gsm8k d005_s123，累计 2310min CPU）
PID 459471: 已 kill（父脚本 wait_and_run_gsm8k.sh，会继续用错误版本跑 d025/d050）
其他进程: 无 evaluate/train_sft 进程
磁盘: 30G 总量, 19G 已用, 12G 可用 (64%)
tmux: 无活跃 session
```

---
