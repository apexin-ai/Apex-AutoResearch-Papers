# code fix exp E holm bonferroni

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_exp_E_holm_bonferroni_20260515T141733_result.json`
- **Structured JSON:** [`04f17a000e47a3687505.json`](../../sessions/04/04f17a000e47a3687505.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。汇报：

---

## 修复结果

### Bug 1: Holm-Bonferroni `cummax` 未更新（已修复）

`holm_bonferroni()` 中 `cummax = 0.0` 初始化后循环内从未赋值，导致 adjusted p-values 失去单调性约束。具体表现：raw_p 更大的 pair 反而得到更小的 corrected_p，跨过 0.05 阈值被错误判定为 significant。

**修复**：在 `adjusted = min(adjusted, 1.0)` 后加 `cummax = adjusted`。

**影响**：
| 指标 | 修复前 | 修复后 |
|------|--------|--------|
| MMLU significant pairs | 10/15 | **8/15** |
| HellaSwag significant pairs | 9/15 | **9/15**（未变） |

MMLU 中 2 对被错误标记为 significant 的 pair 现已修正：
- graduated_a0.9 vs no-filter: 0.0496 → **0.0523** (not sig)
- surprisal vs dsir: 0.0473 → **0.0523** (not sig)

graduated_a0.9 vs DSIR 的 corrected_p=0.0523 本身计算无误，边界未过。

### Bug 2: Cohen's d 分母选择（已调整）

原实现用 d_z（paired differences 的 SD），n=5 且 seed 间方差极小时 d_z 膨胀到 11。改为 d_av（两组 SD 均值做分母，Lakens 2013），更适合与 small/medium/large 基准对照。

**影响**：最大 d 值从 11.0 降至 10.8（MMLU），仍然很大——这是 n=5 固有的，5 个 seed 的 within-strategy SD≈0.0007 vs between-strategy diff≈0.003-0.008，任何标准化效应量都会很大。建议论文中以 mean_diff 为主要效应量指标。

---
