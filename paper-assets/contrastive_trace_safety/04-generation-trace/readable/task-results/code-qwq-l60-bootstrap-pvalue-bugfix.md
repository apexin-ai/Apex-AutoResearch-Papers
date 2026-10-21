# code qwq l60 bootstrap pvalue bugfix

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwq_l60_bootstrap_pvalue_bugfix_20260517T135335_result.json`
- **Structured JSON:** [`7087f248ae3262d31a4c.json`](../../sessions/70/7087f248ae3262d31a4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## Bug 根因分析

**Bug 位置**: `src/experiments/exp_r3_qwq_layer60_bootstrap.py` 第 240 行

**错误公式**:
```python
p_value = float(np.mean(np.abs(bootstrap_diffs) >= abs(observed_diff)))
```

**正确公式** (与 OT-7B 脚本一致):
```python
p_value = float(np.mean(np.abs(bootstrap_diffs - np.mean(bootstrap_diffs)) >= np.abs(observed_diff)))
```

**原因**: Bootstrap 重采样 `bootstrap_diffs` 的分布中心在 `observed_diff` 附近（因为是从 observed 差值重采样的）。不做中心化直接取绝对值，约 50% 的样本满足 `|x| >= |observed|` → p≈0.5。正确做法是先中心化构造 null 分布（`diffs - mean(diffs)`），再看 observed_diff 在 null 分布中的极端程度。

---

## 修正前后 p-value 对比

| Window | Metric | CI 95% | p (旧/错) | p (新/正确) |
|--------|--------|--------|-----------|------------|
| W=1 | bal_acc | [0.15, 0.29] | 0.513 | **0.000** |
| W=1 | precision | [0.21, 0.39] | 0.511 | **0.000** |
| W=1 | pre_cp_fpr | [-0.23, -0.12] | 0.492 | **0.000** |
| W=3 | bal_acc | [0.10, 0.22] | 0.473 | **0.000** |
| W=3 | precision | [0.13, 0.35] | 0.468 | **0.000** |
| W=3 | pre_cp_fpr | [-0.17, -0.03] | 0.472 | **0.004** |
| W=5 | bal_acc | [0.09, 0.21] | 0.490 | **0.000** |
| W=5 | precision | [0.07, 0.29] | 0.495 | **0.000** |
| W=5 | pre_cp_fpr | [-0.12, -0.02] | 0.487 | **0.011** |
| W=10 | bal_acc | [0.05, 0.19] | 0.475 | **0.000** |
| W=10 | precision | [0.05, 0.37] | 0.498 | **0.016** |
| W=10 | pre_cp_fpr | [-0.15, -0.03] | 0.493 | **0.009** |
| W=15 | bal_acc | [0.04, 0.20] | 0.479 | **0.004** |
| W=15 | precision | [0.11, 0.44] | 0.489 | **0.003** |
| W=15 | pre_cp_fpr | [-0.16, -0.03] | 0.497 | **0.007** |

---

## 结论影响

- 所有 15 个测试全部通过 Bonferroni 校正 (α=0.0167)，n_significant = **15/15**
- Conclusion 从 `"not_significant"` 变为 `"significant"`
- **QwQ-32B Layer 60 确实存在显著的 HS vs Text 差异**
- "scale-dependent" claim 不再成立 → 支持 "layer-selection dependent" 叙事
- 修正后结果与 OT-7B Layer 16 (p=0.001) 一致：类似效应量得到类似显著性

---
