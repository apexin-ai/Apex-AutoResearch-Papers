# infra plan003 progress v6

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-progress-v6_20260520T205558_result.json`
- **Structured JSON:** [`96a3dfb5f35850028f38.json`](../../sessions/96/96a3dfb5f35850028f38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_003 标注进度 (20:53 UTC)

### 进程状态

三个进程全部存活，运行时间 ~6h56m。

| PID | 模型 | Elapsed | CPU | RSS |
|-----|------|---------|-----|-----|
| 438497 | llama4 | 6:56:22 | 0.0% | 59MB |
| 438843 | qwen3 | 6:55:15 | 0.0% | 58MB |
| 439116 | deepseek | 6:54:38 | 0.0% | 59MB |

### 完成明细

| 模型 | humaid (3任务) | vast (3任务) | civil_comments (3任务) | 总完成 | 完成率 | 速率 | 预估剩余 |
|------|---------------|-------------|----------------------|--------|--------|------|---------|
| **llama4** | 4500/4500 ✅ | 2737/4500 (vast/fs3=1237) | 0/4500 | **7237/13500** | **53.6%** | 17.4/min | ~6.0h |
| **deepseek** | 4500/4500 ✅ | 588/4500 (vast/zs=588) | 0/4500 | **5088/13500** | **37.7%** | 12.2/min | ~11.5h |
| **qwen3** | 2682/4500 (humaid/fs3=1182) | 0/4500 | 0/4500 | **2682/13500** | **19.9%** | 6.4/min | ~28.2h |

### 与上次对比 (5分钟前)

| 模型 | 上次 | 现在 | 增量 |
|------|------|------|------|
| llama4 | 51.8% | 53.6% | +1.8pp (+243样本) |
| deepseek | 36.4% | 37.7% | +1.3pp (+174样本) |
| qwen3 | 19.4% | 19.9% | +0.5pp (+63样本) |

### 关键发现

**qwen3 是严重瓶颈**：速率仅 6.4样本/min，是 llama4 的 1/3。按当前速率，qwen3 预计还需 **~28小时**（约 5月22日 01:00 UTC），远落后于 llama4（~6h）和 deepseek（~11.5h）。

---
