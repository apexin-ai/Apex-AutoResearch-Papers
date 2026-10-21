# ops latency docred collect 20260516T115

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_latency_docred_collect_20260516T115_20260516T111651_result.json`
- **Structured JSON:** [`b41989815577bee502f8.json`](../../sessions/b4/b41989815577bee502f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

**1. 进程状态：仍在运行**
- PID 351214，17:37 启动，已跑 ~101 分钟
- 当前进度：`semantic_only` 阶段 [60/100]

**2. DocRED 结果尚未写入文件**（`/tmp/latency_benchmark_docred_results.json` 不存在）

**3. 当前进度（从日志）：**

| 方法 | 状态 | Mean latency | Median | Std |
|------|------|-------------|--------|-----|
| unconstrained | ✅ 完成 | 21.023s | 15.588s | 17.729s |
| grammar_only | ✅ 完成 | 21.366s | 15.793s | 17.990s |
| semantic_only | ⏳ 60/100 | ~20.55s (so far) | - | - |
| full_s1 | ⬜ 未开始 | - | - | - |

**初步 overhead 估算（已完成部分）：**
- grammar_only: +1.63%（vs SciERC +1.68%）

**预计剩余时间：** semantic_only 剩 40 样本 (~14 min) + full_s1 100 样本 (~35 min) ≈ **~50 分钟完成**

注意：DocRED 每样本 ~21s 远大于 SciERC 的 ~2.6s，符合预期（文档更长，输出 token 更多）。`/tmp/latency_benchmark_results.json` 确认是 SciERC 旧结果。

---
