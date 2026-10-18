# ops cqa1 eval monitor

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1_eval_monitor_20260520T011523_result.json`
- **Structured JSON:** [`b85a895ed7bf34a5aec2.json`](../../sessions/b8/b85a895ed7bf34a5aec2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

情况比预期复杂——eval_m16_seed44 被重新启动了。当前状态：

```
eval_m16_seed44: [RUNNING] libero_object suite, Task 1 ep 78/500 (Task 0: 38.0%)
  ⚠️ 08:12 重启了新 eval，非之前 415/500 的那次。整体进度 ~12% (10 tasks × 500 eps)

eval_m128_seed43: [RUNNING] libero_object suite, Task 2 ep 291/500
  Task 0: 64.6% | Task 1: 32.2% | 整体进度 ~26%

eval_m16_seed43:  [RUNNING] libero_object suite, Task 2 ep 272/500
  Task 0: 42.8% | Task 1: 47.4% | 整体进度 ~25%

GPU 3: 空闲（无计算进程）
```

之前 415/500 的 m16_seed44 eval 似乎已完成或被替换，当前日志显示 08:12 启动了全新的 libero_object 10-task eval。按 Task 0 耗时 ~55min 估算，整个 eval 预计还需 ~8 小时。

---
