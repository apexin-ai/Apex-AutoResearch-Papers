# ops qwen monitor eval 21461

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen-monitor-eval-21461_20260520T082141_result.json`
- **Structured JSON:** [`5761ba1a0dcfc78ed4e2.json`](../../sessions/57/5761ba1a0dcfc78ed4e2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个都还在跑，均未完成。

**当前进度：**

```
Qwen unc: 运行中, 887/998, ETA ~17:00 UTC
Qwen con: 运行中, 707/998, ETA ~18:10 UTC
```

**计算依据：**
- unc (PID 167691): 11:14 启动，已跑 308 min 完成 887 样本 → 0.35 min/sample，剩 111 个 → ~39 min
- con (PID 174618): 11:56 启动，已跑 266 min 完成 707 样本 → 0.38 min/sample，剩 291 个 → ~110 min

两个 GPU 利用率正常（87%/89%），进程状态健康。unc 预计约 40 分钟后完成，con 约 2 小时后。

---
