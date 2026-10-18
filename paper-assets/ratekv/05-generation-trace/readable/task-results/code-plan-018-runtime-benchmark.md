# code plan 018 runtime benchmark

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_018_runtime_benchmark_20260514T085811_result.json`
- **Structured JSON:** [`e9d7fc4dae25ba256b0f.json`](../../sessions/e9/e9d7fc4dae25ba256b0f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All validations pass:

- **Syntax**: clean compile
- **`--help`**: all arguments documented, `--gpu` defaults to `cuda:0`
- **Imports**: all dependencies resolve (transformers, DynamicCache, solver, utils)
- **MCKP solver**: correctly loads profiles and produces 112-head allocation (28 layers × 4 KV heads), bit distribution `{8:4, 2:8, 4:100}`, memory ratio 0.2500
- **Uniform allocation**: 112 heads, all set to 4-bit

Script written to `/root/ratekv/run_runtime_benchmark.py`. It benchmarks three conditions (baseline bf16, uniform 4-bit, constrained MCKP) using a manual generation loop with `DynamicCache`, applying per-head quantize-dequantize to the KV cache after each forward pass. Timing uses `torch.cuda.synchronize()` with `perf_counter`, 3 warmup + 10 measurement runs, GPU cache flushed between conditions. Results go to `runtime_benchmark_results.json`.

---
