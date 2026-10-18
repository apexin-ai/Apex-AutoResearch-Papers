# gpu dual rerun sync

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_gpu_dual_rerun_sync_20260514T164828_result.json`
- **Structured JSON:** [`c557cef3e2705a52986c.json`](../../sessions/c5/c557cef3e2705a52986c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，双卡正常运行。

**Step 3 验证结果**：
| 文件 | `.float().view` | 备注 |
|------|----------------|------|
| `full_bitwidth_profiler.py` | L63 ✓ | |
| `eval_ppl.py` | L162 ✓ | sed 修复 |
| `run_kv_separation.py` | L143 ✓ | |
| `run_gemma2_full_pipeline.py` | L181, L270 ✓ | |
| `run_yi15_full_pipeline.py` | 无 `solve_ratequant_greedy` ✓ | `MCKP total distortion` L201 ✓ |

**Step 6 验证结果**：
- **GPU 0** (Gemma-2): 43951 MiB 已占用，Baseline PPL = **9.3785**，profiling 进行中 (10/1008)
- **GPU 1** (Yi-1.5): 25551 MiB 已占用，Baseline PPL = **7.3461**，profiling 进行中 (4/576)
- 两个 baseline PPL 值合理（Gemma-2 ~9，Yi-1.5 ~7），delta 非零，修复生效
- 无报错

---
