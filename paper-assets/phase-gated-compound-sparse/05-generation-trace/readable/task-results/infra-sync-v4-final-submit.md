# infra sync v4 final submit

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_sync-v4-final-submit_20260513T225541_result.json`
- **Structured JSON:** [`629efd09b925c9ce582c.json`](../../sessions/62/629efd09b925c9ce582c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 路实验全部运行正常。

### 结果汇总

| 项目 | 状态 |
|------|------|
| **代码同步** | interaction_index.py (476行) + run_profiling.py (524行) → 双目录写入完成 |
| **Bug 修复** | `compute_dense_forward_with_importance` 中 CPU/CUDA 设备不匹配，添加 `.cpu()` 修复 |
| **导入验证** | IMPORT OK |
| **CLI 验证** | CLI PARSE OK |

| 实验 | exp_id | PID | GPU | Sparsity | 状态 |
|------|--------|-----|-----|----------|------|
| v4a | mvp_ii_profiling_v4a | 22704 | cuda:0 (25.2GB) | 0.1, 0.2 | 运行中 (3/50) |
| v4b | mvp_ii_profiling_v4b | 23052 | cuda:1 (21.2GB) | 0.3, 0.4, 0.5 | 运行中 (2/50) |
| v4c | mvp_ii_profiling_v4c | 23403 | cuda:2 (21.2GB) | 0.15, 0.25 | 运行中 (1/50) |

GPU 利用率 94-99%，3 路并行正常推进。日志：`/tmp/profiling_v4{a,b,c}.log`，输出目录：`profiling_output_v4{a,b,c}/`。

---
