# analysis qwen n500 full

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen_n500_full_20260515T053128_result.json`
- **Structured JSON:** [`72a8bf27a0a434a52621.json`](../../sessions/72/72a8bf27a0a434a52621.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本执行成功，JSON/CSV/LaTeX 输出均无报错。以下按 5 个检查项逐一报告。

---

## 1. QW rand s030 是否显著？

**显著。**

| 指标 | 值 |
|---|---|
| median II diff | +0.9127 |
| 95% CI | [0.6134, 1.2584] |
| Bonferroni-corrected p | <0.001 (***) |

CI 不跨零，与 n=50 dryrun 方向一致（dryrun CI [0.242, 3.488]），n=500 后 CI 大幅收窄，效应量稳定。

---

## 2. QW 4-level dose-response 单调性

### Importance: 完美单调递增

| Sparsity | median II diff |
|---|---|
| s015 | +0.0659 |
| s020 | +0.3073 |
| s025 | +1.0745 |
| s030 | +3.1550 |

- `is_monotonic` = **True**
- `permutation_p` = **0.0417** (≤0.042 ✓)
- exact Spearman rho = **1.000**, p = **0.0417** (≤0.042 ✓)

### Random: 也单调递增

| Sparsity | median II diff |
|---|---|
| s015 | -0.0111 |
| s020 | +0.0153 |
| s025 | +0.3931 |
| s030 | +0.9127 |

- `is_monotonic` = **True**
- `permutation_p` = **0.0417**
- exact Spearman rho = **1.000**, p = **0.0417**

Random 也呈单调但效应量远小于 importance（s030: 0.91 vs 3.16，约 3.5 倍差距）。

---

## 3. QW imp-vs-rand paired 对比

| Sparsity | median_diff (imp−rand) | r_rb | Wilcoxon p_bonf |
|---|---|---|---|
| s015 | +0.0991 | +0.301 | <0.001 *** |
| s020 | +0.3146 | +0.373 | <0.001 *** |
| s025 | +0.7572 | +0.309 | <0.001 *** |
| s030 | +2.0006 | +0.343 | <0.001 *** |

**全部 4 个 sparsity level importance 效应均显著大于 random**。

- s025: importance 是 random 的 **2.7×**（1.0745 vs 0.3931）
- s030: importance 是 random 的 **3.5×**（3.1550 vs 0.9127）
- 差距随 sparsity 增加而扩大，符合预期。

---

## 4. d_z 可靠性

### Within-importance robust d_z

| Pair | robust_dz | 95% CI | Interpretation | r_rb | Reliable? |
|---|---|---|---|---|---|
| s015 vs s020 | −0.629 | [−0.709, −0.476] | medium | −0.632 | ✓ reliable |
| s020 vs s025 | −0.865 | [−0.963, −0.715] | large | −0.840 | ✓ reliable |
| s025 vs s030 | −0.767 | [−0.854, −0.679] | medium | −0.839 | ✓ reliable |
| s015 vs s030 | −0.923 | [−1.023, −0.820] | large | −0.955 | ✓ reliable |

全部 4 对均 reliable，CI 不跨零。rank-biserial correlation 与 d_z 方向一致，绝对值匹配（中-大效应）。s015→s030 跨度最大，d_z=−0.923（large），r_rb=−0.955，说明 importance masking 在全量程上有强且可靠的剂量效应。

---

## 5. 异常/意外

- **rand s015**: median=−0.0111, CI=[−0.039, 0.012], p_bonf=1.000 — **NS，符合预期**（已知 FAIL）。
- **rand s020**: median=+0.0153, CI=[−0.015, 0.068], p_bonf=1.000 — **NS**，也符合预期。
- **无方向不一致**：所有结果与 n=50 dryrun 方向一致。
- **mid-phase null rate**: 45.2%（226/500），对所有条件相同（因为 mid-phase null 是 task-level 属性而非 condition-level），合理。
- **无离群值警告**。
- **random 也单调且 s025/s030 显著**：这是值得注意的发现——random pruning 在高 sparsity 时也产生可测量的 II 差异，但幅度远小于 importance。这支持"pruning 本身有效应，但 importance-guided pruning 效应显著更大"的论述。

---
