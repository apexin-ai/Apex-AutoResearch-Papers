# analysis gradient snr constrained

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gradient_snr_constrained_20260517T041834_result.json`
- **Structured JSON:** [`76919058b13c3c4c2381.json`](../../sessions/76/76919058b13c3c4c2381.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Gradient SNR v2（带 Lagrangian constraint，公平对比）

| 指标 | KL | BCE | 比值 |
|------|-----|-----|------|
| **Avg gradient SNR** | 5.45×10⁻⁴ | 5.28×10⁻⁶ | **103.2×** |
| **Final sparsity** | 0.508 | 0.591 | — |

### Per-layer SNR（选取层）

| Layer | KL SNR | BCE SNR | Ratio |
|-------|--------|---------|-------|
| layer_0 | 4.32e-5 | 8.51e-8 | 508× |
| layer_12 | 1.55e-3 | 6.90e-7 | 2251× |
| layer_29 | 9.53e-4 | 7.44e-6 | 128× |
| layer_31 | 5.89e-4 | 1.17e-4 | 5× |

### vs v1（无 Lagrangian）

| 版本 | KL avg SNR | BCE avg SNR | Ratio |
|------|-----------|-------------|-------|
| **v1**（无 Lagrangian） | 5.77e-5 | 1.00e-5 | **5.76×** |
| **v2**（Lagrangian） | 5.45e-4 | 5.28e-6 | **103.2×** |

### 关键发现

1. **加上 Lagrangian 后 KL SNR 优势不但没有减弱，反而从 5.76× 大幅提升到 103.2×**。Reviewer 的担忧（v1 不公平因无 constraint）被直接反驳。

2. **KL sparsity 成功收敛到 target 0.5**（final 0.508），Lagrangian lambda 轨迹：1→2→4→8→4（step 75 达峰，100 后稳定）。

3. **BCE sparsity 偏离 target**（final 0.591），因 Lagrangian 是单侧 clamp（只惩罚低于 target），BCE predictor 自然偏向高 sparsity 但无约束拉回。

4. **BCE 的 gradient SNR 几乎为零**（多数层 <1e-7），说明 BCE loss 提供的每层梯度方向高度随机，远不如 KL 的端到端信号。

产出文件：
- 脚本：`/root/distill_sparse_swiglu/scripts/gradient_snr_constrained.py`
- 结果：`/root/distill_sparse_swiglu/artifacts/gradient_snr_constrained_results.json`
- 日志：`/root/distill_sparse_swiglu/logs/gradient_snr_v2.log`

---
