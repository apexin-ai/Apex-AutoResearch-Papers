# exp qwen14b constrained pipeline

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_qwen14b_constrained_pipeline_20260515T112623_result.json`
- **Structured JSON:** [`15d8ef436f7c52373bf3.json`](../../sessions/15/15d8ef436f7c52373bf3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。

**脚本**: `run_qwen14b_constrained_pipeline.py` — 三种方案 (uniform 4-bit / constrained MCKP k=8 / unconstrained MCKP) 在 WikiText-2 上的 PPL 对比。

**Dry-run 结果**:
- 384 heads (48L × 8KV), profiling 加载 + solver 运行正常
- Constrained (k=8): {4: 374, 8: 1, 16: 1, 2: 8} — 几乎全是 4-bit
- Unconstrained: {4: 271, 2: 77, 8: 35, 16: 1} — 77 heads 用 2-bit

**运行状态**:
- PID: 329678, GPU 1 (96GB RTX PRO 6000 Blackwell)
- 模型已加载 (29.7GB), baseline eval 进行中 (~chunk 300/583)
- 日志: `/root/ratekv/logs/qwen14b_constrained_pipeline.log`
- 输出: `artifacts/qwen14b_constrained_pipeline_results.json`

**预计完成**: ~20-30 min (4 轮 WikiText-2 eval × 583 chunks each, 14B 模型推理较慢)

---
