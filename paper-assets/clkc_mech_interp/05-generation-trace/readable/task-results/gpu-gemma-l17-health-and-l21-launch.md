# gpu gemma L17 health and L21 launch

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_gemma-L17-health-and-L21-launch_20260522T155445_result.json`
- **Structured JSON:** [`963429b4a849a6dbc79d.json`](../../sessions/96/963429b4a849a6dbc79d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

| 项目 | 状态 |
|------|------|
| **Gemma L17** | 正常运行。PID 493756，GPU 2 占用 18570 MiB，GPU util 12%，CPU 72.3%，已运行 1h16m。日志无更新是 stdout buffering，进程活跃无需干预 |
| **Gemma L21** | 已启动。PID 499402，GPU 0 占用 18410 MiB，GPU util 30%，模型已加载完成，probe accuracy 0.7627，正在执行 steering |

GPU 分布：GPU 0 → L21 (499402)，GPU 2 → L17 (493756)，GPU 1/3 空闲。

---
