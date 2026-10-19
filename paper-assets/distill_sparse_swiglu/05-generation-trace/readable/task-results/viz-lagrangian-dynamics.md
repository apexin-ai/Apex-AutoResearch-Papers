# viz lagrangian dynamics

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_viz_lagrangian_dynamics_20260517T044635_result.json`
- **Structured JSON:** [`28e848e34f7e73dbc9b5.json`](../../sessions/28/28e848e34f7e73dbc9b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。生成文件：

- **PDF**: `/root/distill_sparse_swiglu/paper/figures/lagrangian_dynamics.pdf`
- **PNG**: `/root/distill_sparse_swiglu/paper/figures/lagrangian_dynamics.png` (1036×1336 px, 300 DPI)
- **脚本**: `/root/distill_sparse_swiglu/scripts/plot_lagrangian_dynamics.py`

图的内容：
- **(a)** 上面板：4 条 λ 曲线（log scale），30% 的 λ 从 0.01 涨到 5000，70% 的从 2 涨到 1000，展示 Lagrangian multiplier 的自适应调节过程
- **(b)** 下面板：实际 sparsity（实线）vs 目标 sparsity（虚线），可见各 target 的收敛行为

注意：50% 实验只有 200 步数据（其余三个有 1000 步），图上会体现为 50% 曲线较短。如需补跑 50% 的完整数据再告知。

---
