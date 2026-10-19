# infra plan003 progress v5

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_plan003-progress-v5_20260520T204553_result.json`
- **Structured JSON:** [`a79f86d133d3279d5d6d.json`](../../sessions/a7/a79f86d133d3279d5d6d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan_003 三路标注进度报告

### 进程状态

| 模型 | PID | 状态 | 运行时间 | CPU% | RSS(MB) |
|------|--------|------|----------|------|---------|
| llama4 | 438497 | ALIVE | 6h46m | 0.0 | 59 |
| qwen3 | 438843 | ALIVE | 6h45m | 0.0 | 58 |
| deepseek | 439116 | ALIVE | 6h44m | 0.0 | 59 |

### 任务进度（每模型 9 任务 × 1500 样本 = 13,500 总样本）

| 模型 | 当前任务 | 已完成任务 | 已完成样本 | 完成率 | 速率(样本/h) | 预估剩余 |
|------|----------|-----------|-----------|--------|-------------|---------|
| **llama4** | vast/few-shot-3 (993/1500) | 5/9 | 6,993 | **51.8%** | ~1,033 | **~6.3h** |
| **deepseek** | vast/zero-shot (420/1500) | 4/9 | 4,920 | **36.4%** | ~730 | **~11.8h** |
| **qwen3** | humaid/few-shot-3 (1114/1500) | 2/9 | 2,614 | **19.4%** | ~387 | **~28.1h** |

### 已完成文件明细

```
humaid/llama4_zero-shot:    1500 ✓    humaid/deepseek_zero-shot:    1500 ✓    humaid/qwen3_zero-shot:    1500 ✓
humaid/llama4_few-shot-3:   1500 ✓    humaid/deepseek_few-shot-3:   1500 ✓    humaid/qwen3_few-shot-3:   1114 ◐
humaid/llama4_few-shot-5:   1500 ✓    humaid/deepseek_few-shot-5:   1500 ✓
vast/llama4_zero-shot:      1500 ✓    vast/deepseek_zero-shot:       420 ◐
vast/llama4_few-shot-3:      993 ◐
```

civil_comments 目录尚未创建（三个模型都还没跑到该数据集）。

### 注意

**qwen3 速度显著落后**（387 vs llama4 的 1033 样本/h），按当前速率还需约 28 小时。日志中有间歇性 502 和 timeout 错误（三个模型都有），但 qwen3 的总体吞吐量仅为 llama4 的 37%。

---
