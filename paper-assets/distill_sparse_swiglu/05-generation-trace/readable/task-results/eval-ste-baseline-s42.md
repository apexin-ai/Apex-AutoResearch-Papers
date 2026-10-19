# eval ste baseline s42

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_ste_baseline_s42_20260515T195932_result.json`
- **Structured JSON:** [`84a54c2d45cdfbff852a.json`](../../sessions/84/84a54c2d45cdfbff852a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 全部更新完成。

---

## 报告

### (1) 完整 Eval 指标

| 指标 | 值 |
|------|------|
| True Dense PPL | 6.12 |
| Predictor Hard Mask PPL | 8.18 |
| TEAL Sparse PPL | **15.77** |
| Model-level sparsity (TEAL) | 0.470 |
| Per-token sparsity | 0.470 |

### (2) vs Gumbel-sigmoid 对比

| 指标 | STE | Gumbel 4-seed mean | 差异 |
|------|-----|---------------------|------|
| TEAL Sparse PPL | 15.77 | 12.00 ± 0.07 | **+31.4%** |
| Hard Mask PPL | 8.18 | 9.19 ± 0.04 | -11.0%* |
| Per-token sparsity | 0.470 | 0.498 | -2.8pp |

\*Hard mask PPL 比较不公平：STE 实际稀疏度更低（47% vs 49.8%），自然 PPL 更好。TEAL 路径是公平比较（均为全局 50%）。

### (3) Lambda 震荡统计

| 区间 | Mean | Std | Min | Max |
|------|------|-----|-----|-----|
| Steps 70-130 | 66.40 | 94.87 | 0.01 | 1000 |
| 前 500 步 | 688.07 | 440.57 | 0.01 | 1000 |
| 后 500 步 | 965.69 | 141.59 | 250 | 1000 |
| 全程 | 826.88 | 354.23 | 0.01 | 1000 |

前 500 步 std=440 vs 后 500 步 std=142，说明 STE 训练前期 lambda 剧烈震荡（0.01→1000→3.91 在 30 步内），后期被 cap=1000 压住但仍有波动。

### (4) Conclusion 判定

**conclusion = success**（验证了 Gumbel 的必要性）

TEAL sparse PPL 15.77 显著差于 Gumbel 12.00 (+31.4%)。STE hard threshold 的两个致命缺陷：
1. **Lagrangian 不稳定**：离散 mask 导致 constraint 满足在 violated/satisfied 间剧烈跳变，lambda 被迫震荡
2. **逐层稀疏度极端两极化**（Layer 0-17: 5-56%, Layer 18-31: 56-90%），导致 TEAL 全局 topk 分配质量差

---
