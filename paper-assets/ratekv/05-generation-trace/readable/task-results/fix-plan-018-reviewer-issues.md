# fix plan 018 reviewer issues

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_plan_018_reviewer_issues_20260514T091155_result.json`
- **Structured JSON:** [`deb30d4e6bea9c3b5ba2.json`](../../sessions/de/deb30d4e6bea9c3b5ba2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成：

1. **脚本修改** — 3 处改动已写入 `/root/ratekv/run_runtime_benchmark.py`（335→381 行）：
   - 新增 `compute_theoretical_memory()` 函数（行 231），按公式计算 baseline/uniform/MCKP 三种条件的理论 KV cache 内存
   - 在 Save 前插入 `results["theoretical_memory"]`、`results["note"]`（decode latency 注释）、`results["peak_memory_note"]`（peak memory 注释）
   - benchmark 核心逻辑未改动

2. **提交运行** — PID=208103，CUDA_VISIBLE_DEVICES=0，GPU 0 上正常运行中（GPU 1 空间不足，改用 GPU 0 的 ~50GB 空闲）。Baseline bf16 condition 已在跑 runs，预计 15-20 分钟完成全部 3 个 conditions。

输出文件：`/root/ratekv/runtime_benchmark_results.json`

---
