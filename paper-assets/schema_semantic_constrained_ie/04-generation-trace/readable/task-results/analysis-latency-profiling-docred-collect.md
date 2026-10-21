# analysis latency profiling docred collect

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_latency_profiling_docred_collect_20260516T101608_result.json`
- **Structured JSON:** [`3d35612fd8b89ae1f9ec.json`](../../sessions/3d/3d35612fd8b89ae1f9ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态明确了。汇总报告：

## DocRED Latency Benchmark 状态

**进程仍在运行**（PID 351213/351214/354247），GPU 利用率 85-89%。

### 已完成
- **unconstrained** (100 samples): mean=21.023s, median=15.588s, std=17.729s

### 进行中
- **grammar_only**: 已开始，日志因 Python stdout 缓冲未显示进度

### 未开始
- semantic_only
- full_s1

### 时间估算
- 脚本 17:20 启动，unconstrained 在 ~18:13 完成
- 每个 mode ≈ 35 分钟（100 × 21s）
- 剩余 3 个 mode ≈ 105 分钟
- **预计完成时间：~20:00 CST (UTC+8)**

### 结果文件
- 脚本写结果到 `/tmp/latency_benchmark_docred_results.json`，但仅在全部 4 个 mode 跑完后才写入（目前不存在）
- 完成后还会输出 summary table 到 stdout（会追加到 `/tmp/benchmark_docred.log`）

### 另外
已有的 `/tmp/latency_benchmark.log` 和 `/tmp/latency_benchmark_results.json` 是 **SciERC controlled benchmark** 的结果（已完成）：

| Mode | N | Mean(s) | P50(s) | P95(s) | P99(s) | Overhead | tok/s |
|------|---|---------|--------|--------|--------|----------|-------|
| unconstrained | 100 | 2.594s | 2.359s | 5.985s | 8.194s | - | 57.7 |
| grammar_only | 100 | 2.637s | 2.397s | 6.099s | 8.346s | +1.7% | 56.7 |
| semantic_only | 100 | 2.625s | 2.379s | 6.080s | 8.335s | +1.2% | 57.0 |
| full_s1 | 100 | 2.655s | 2.416s | 6.162s | 8.449s | +2.3% | 56.4 |

建议约 2 小时后（~20:00 CST）再派 Worker 收集 DocRED 结果。

---
