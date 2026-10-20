# ops check eval progress use gpu2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-progress-use-gpu2_20260521T123308_result.json`
- **Structured JSON:** [`3335c8575b9e59ede9eb.json`](../../sessions/33/3335c8575b9e59ede9eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程确认正常运行：模型已加载到 GPU 2（18589 MiB），正在评估 arc_challenge。

汇报：

```
d000 MMLU eval: ✓ 完成
d000 ARC eval:  运行中 (GPU 2, PID 522297, 刚启动)
d025 MMLU eval: 运行中 (GPU 0, PID 521464)
d025 ARC eval:  未启动
GPU 1:          空闲，可用于下一个任务
GPU 2 任务:     d000 ARC eval, PID 522297
```

注意：evaluate.py 大小 37775 bytes，与 C009 记录的 reference（37591 bytes）不一致，但本服务器上所有 eval 用的是同一版本，C010 同服务器一致性满足。GPU 1 也空闲，d025 MMLU 完成后可立即在 GPU 1 启动 d025 ARC。

---
