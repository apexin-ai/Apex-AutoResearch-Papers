# check plan 015 v2 status

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_plan-015-v2-status_20260515T012532_result.json`
- **Structured JSON:** [`6f778155476997557799.json`](../../sessions/6f/6f778155476997557799.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## plan-015-v2 状态报告

**进程存活**：PID 148428，运行 `scripts/ordinal_baseline.py --device cuda:0`（CUDA_VISIBLE_DEVICES=2），08:56 启动，已运行约 30 分钟。

**当前阶段**：已完成 Eval 阶段，正在执行 Bootstrap CI（置信区间计算）。日志最后显示完成了 LD-Score 的 bootstrap，正在处理 FastDetectGPT。

**Eval 中间结果**：

| 方法 | F1 | LOGO | rho |
|------|-----|------|-----|
| LD-Score | 0.6603±0.0070 | 0.6597 | 0.6837 |
| FastDetectGPT | 0.6938±0.0097 | 0.6824 | 0.4174 |
| Avg-LogProb | 0.7592±0.0064 | 0.7564 | 0.7282 |
| Binoculars | 0.2462±0.0050 | 0.2507 | 0.1762 |
| 7-feat | 0.8024±0.0049 | 0.7980 | — |

**输出文件**：
- `results/ordinal_baseline_results.json`（3.2KB，08:55 写入）
- `artifacts/plan-015/bootstrap_ci_results.txt`（08:41 写入）
- `artifacts/plan-015/report/ordinal_baseline_results.txt`（08:55 写入）

**结论**：进程正常运行中，Bootstrap CI 阶段进行中，预计短时间内完成。

---
