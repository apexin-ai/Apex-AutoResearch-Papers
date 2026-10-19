# exp mf1a adversarial monotonicity

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_mf1a_adversarial_monotonicity_20260523T173639_result.json`
- **Structured JSON:** [`3d2c6c2a05e823e9c1fb.json`](../../sessions/3d/3d2c6c2a05e823e9c1fb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**MF-1a 完成。** 54,611 条曲线，14.3s 运行。

核心发现：

| 维度 | max ε_abs | 非单调率 |
|------|-----------|----------|
| **总体** | **0.0164** | 11.9% |
| safe topos (conf/med/exp/fd) | 0.0164 | — |
| fragile topos (col/mbias/iv) | 0.0132 | — |

**按 adversarial 类型：**
- **near_perm**: 最具对抗性，35.3% 非单调，max ε=0.016
- **block_diag**: 0% 非单调（确定性结构，无违反）
- **sparse**: 2.3% 非单调，max ε=0.003
- **near_uniform**: 0% 非单调

**按 topology：**
- confounding/mediation/frontdoor 约 20% 曲线有微小违反（ε < 0.017）
- exposure 仅 0.68%，mbias 1.44%
- IV: 0 违反（过滤掉 2,089 条 weak-IV 曲线后）

**结论：** 所有 adversarial 结构下 max ε_abs = 0.016，远低于论文声称的 0.06 bound。Conjecture 1 的 ε-approximate envelope monotonicity 在 adversarial 条件下成立。违反集中在 near-permutation 矩阵 + alternating_large β + 小 K 的组合。

---
