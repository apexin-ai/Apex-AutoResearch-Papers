# code imm core modules

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_imm-core-modules_20260515T111402_result.json`
- **Structured JSON:** [`6d9ccd9f38d07f34fe9d.json`](../../sessions/6d/6d9ccd9f38d07f34fe9d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部模块验证通过，梯度正常流通。

实现的 5 个文件：

| 文件 | 内容 |
|------|------|
| `soft_topk.py` | `SoftTopK` — sigmoid 和 sinkhorn 两种可微 top-k 方案 |
| `losses.py` | `MarginMaximizationLoss` (hinge loss) + `IMMTotalLoss` (含 λ warmup) |
| `token_selection.py` | `MarginAwareTokenSelector` — 训练时 soft mask，推理时 preserve/prune/merge 三分区 |
| `metrics.py` | `compute_margin`, `topk_preservation_rate`, `kendall_tau_distance`, `certified_bound`, `margin_statistics` |
| `__init__.py` | 统一导出 |

---
