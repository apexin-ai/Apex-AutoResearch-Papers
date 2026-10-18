# code c4 rerun d032

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c4_rerun_d032_20260514T090654_result.json`
- **Structured JSON:** [`e2fbe86c32097bd09ff5.json`](../../sessions/e2/e2fbe86c32097bd09ff5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 状态总结：**

| GPU | 进程 | 显存 | 说明 |
|-----|-------|------|------|
| 0 | `run_multi_seed.py` + `run_runtime_benchmark.py` | 89.5 GB / 98 GB | 满 |
| 1 | `run_cross_domain.py` (168/336, 44 seqs) | 67 GB | 使用全部 200 条 C4（无 cal/eval 分割） |
| 1 | `run_c4_cross_dataset_v2.py` (218/336, **仅 5 seqs**) | 24 GB | 只有 5 条校准序列，delta 全为 0，**结果无效** |

**问题：**
- `run_c4_cross_dataset_v2.py` 用 `FullBitwidthProfiler`（逐条匹配长度），只有 5 条 C4 text 够 2048 tokens，profiling 结果全是零——废实验
- `run_cross_domain.py` 用 concatenate 方式得到 44 seqs，结果可用但没做 cal/eval 分割
- 我们的 `run_c4_rerun.py` 方法更好（100 条 cal / 100 条 eval 分割，concatenate 得 18+20 seqs），但 GPU 1 没有空间

**建议：kill `run_c4_cross_dataset_v2.py`（废实验），释放 24 GB，然后尝试与 `run_cross_domain.py` 共存运行。** 如果 OOM 就等 `run_cross_domain.py` 跑完。

是否 kill PID 206887？

---
