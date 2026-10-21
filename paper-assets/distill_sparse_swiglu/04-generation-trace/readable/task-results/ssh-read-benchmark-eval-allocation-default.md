# ssh read benchmark eval allocation default

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_read_benchmark_eval_allocation_default_20260520T190832_result.json`
- **Structured JSON:** [`7938d73301198159981e.json`](../../sessions/79/7938d73301198159981e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

**1. `--allocation` 默认值：`global_topk`**

**2. 无条件分支默认值**：argparse 只定义了一个静态 default，不依赖 `sparsity_mode` 或其他参数。choices=[`global_topk`, `uniform`]。

**3. 代码片段**（benchmark_eval.py:111-113）：
```python
p.add_argument("--allocation", type=str, default="global_topk",
               choices=["global_topk", "uniform"],
               help="Sparsity budget allocation: single threshold or per-layer independent top-k")
```

**下游传递**（一律取 `args.allocation`，不改写）：
- L344 baseline 模式：`allocation=args.allocation` → 传给 `compute_baseline_masks`
- L350/L375 predictor + teal_global 模式：同样透传

因此命令行不显式传 `--allocation` 时，所有 baseline（teal_vanilla/teal_greedy/wina/rsparse）和 predictor-teal_global 模式都使用 **global_topk**。

---
