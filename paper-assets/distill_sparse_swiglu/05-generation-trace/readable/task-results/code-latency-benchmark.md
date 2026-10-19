# code latency benchmark

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_latency_benchmark_20260518T183429_result.json`
- **Structured JSON:** [`ac6f60bf7fefb6b272ec.json`](../../sessions/ac/ac6f60bf7fefb6b272ec.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Dry-run 通过。

**产出总结**:

1. **脚本**: 已写入 `/root/distill_sparse_swiglu/src/benchmark_latency.py`，`--help` 和 `--dry_run` 均验证通过。

2. **TEAL sparse kernel 调研结论**: **纯 mask-and-multiply，没有 sparse kernel**。`PredictorWrapper._patch_single_mlp` 计算完整的 `gate_proj`、`up_proj`、`down_proj` dense matmul，只在中间激活上做 element-wise mask。没有 triton kernel、cuSPARSE、或任何结构化稀疏优化。预期 sparse 模式会比 dense **更慢**（额外 predictor forward 开销，无 FLOP 节省）。

3. **Checkpoint 路径修正**: 30% sparsity 用的是 `kl_sparsity30_s42_v3`（用户指定的 `kl_sparsity30_s42` 不存在）。

4. **Predictor 参数验证** (与 C003 约束一致): GELU 激活, d_b=128, 2,373,760 params/layer, 75,960,320 total。

脚本支持: `--batch_sizes 1,8`, `--runs 3`, `--iters 100`, `--warmup 10`, JSON 输出, markdown 表格, GPU memory 测量, predictor 独立开销测量。等 GPU 空闲后可跑: `python src/benchmark_latency.py --device cuda:0`。

---
