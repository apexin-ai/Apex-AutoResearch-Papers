# fix lagrangian dynamics regen

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_lagrangian_dynamics_regen_20260520T065139_result.json`
- **Structured JSON:** [`239fce998af44565a5a0.json`](../../sessions/23/239fce998af44565a5a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**数据来源**: `/root/distill_sparse_swiglu/logs/multiseed_kl30_fixed.log`（KL 30% target=0.3, cap=5000, 完整 1000 步训练）

**提取数据点**: 101 个（step 1, 10, 20, ..., 1000）

**生成文件**:
- 脚本: `figures/paper/gen_lagrangian_dynamics.py`
- PDF: `figures/paper/lagrangian_dynamics.pdf`
- PNG: `figures/paper/lagrangian_dynamics.png`

图表展示了 Lagrangian controller 的典型行为：前 130 步 lambda 极低（0.01），sparsity 自然从 0.406 下降；~step 150 sparsity 首次低于 target，lambda 急升至 327→5000 触发 bang-bang 振荡；step 270 后 lambda 饱和在 cap=5000，sparsity 收敛并稳定在 0.28 附近。

---
