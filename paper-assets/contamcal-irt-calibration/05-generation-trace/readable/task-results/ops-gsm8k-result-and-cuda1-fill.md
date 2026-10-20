# ops gsm8k result and cuda1 fill

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gsm8k-result-and-cuda1-fill_20260518T144227_result.json`
- **Structured JSON:** [`8780711cfc2597524d00.json`](../../sessions/87/8780711cfc2597524d00.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:1 已有 python 进程 PID 34011（550MB，正在加载模型到 GPU）。

## 汇报

### GSM8K eval
**Accuracy: 71.04%** (937/1319)，已完成，`.done` 标记存在。

### cuda:1
启动了 **d050 s42**，PID 34011（子进程），正在加载模型。

### 全卡状态

| GPU | 任务 | PID | 显存 | Util | 进度 |
|-----|------|------|------|------|------|
| cuda:0 | d025 s42 | 30306 | 69GB | 94% | **2628/3384 (77.6%)**，ETA ~20min |
| cuda:1 | **d050 s42** | 34011 | 550MB→加载中 | 0%→ | 刚启动 |
| cuda:2 | 14B d000 s42 | 28900 | 64GB | 79% | **1844/3125 (59.0%)**，ETA ~1h05min |
| cuda:3 | d000 s123 | 31158 | 61GB | 83% | **1993/3125 (63.8%)**，ETA ~38min |

四卡满载。

---
