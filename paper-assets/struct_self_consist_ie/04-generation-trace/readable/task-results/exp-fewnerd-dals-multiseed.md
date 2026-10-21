# exp fewnerd dals multiseed

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_fewnerd_dals_multiseed_20260518T070429_result.json`
- **Structured JSON:** [`0e36d6d069a3ebee3786.json`](../../sessions/0e/0e36d6d069a3ebee3786.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果出来了。汇总：

## Task 1: Few-NERD 3-seed Bootstrap (τ=0.05)

| | Value |
|---|---|
| N instances (gold-filtered) | 4351 |
| Greedy F1 | 74.93 |
| LP Selection F1 | 76.78 |
| **DALS F1** | **76.01** |
| **DALS gain** | **+1.08pp** |
| LP selected | 3498/4351 (80.4%) |

Bootstrap (n=10000) 跨 3 个 seed 完全一致（DALS 本身是确定性的，只有 CI 宽度微变）：

| Seed | Gain (pp) | 95% CI | p-value |
|---|---|---|---|
| 42 | +1.0842 | [0.6984, 1.4709] | 0.0000 |
| 123 | +1.0842 | [0.7049, 1.4794] | 0.0000 |
| 456 | +1.0842 | [0.7090, 1.4803] | 0.0000 |

**所有 3 seed 均 p<0.001，CI 不含 0。Few-NERD DALS 效果高度稳定。**

## Task 2: τ Sensitivity

| τ | DALS F1 | Gain vs Greedy (pp) | Gain vs LP (pp) | % LP Selected |
|---|---|---|---|---|
| 0.01 | 76.66 | +1.73 | -0.12 | 96.2% |
| 0.03 | 76.22 | +1.29 | -0.56 | 91.4% |
| **0.05** | **76.01** | **+1.08** | **-0.77** | **80.4%** |
| 0.10 | 75.50 | +0.57 | -1.28 | 50.3% |
| 0.15 | 75.01 | +0.08 | -1.77 | 32.0% |
| 0.20 | 74.92 | -0.01 | -1.86 | 18.3% |

关键发现：
- Gain 在 τ=0.01~0.10 范围内均为正且单调递减，τ=0.05 不是最优（τ=0.01 给出 +1.73pp）
- τ≥0.20 时 gain 消失（接近 0）
- 说明 Few-NERD 的 +1.08pp 效果稳健，不依赖 τ=0.05 的特定选择；更小的 τ 反而更好

结果已保存到 `output/fewnerd_dals_multiseed_results.json`。

---
