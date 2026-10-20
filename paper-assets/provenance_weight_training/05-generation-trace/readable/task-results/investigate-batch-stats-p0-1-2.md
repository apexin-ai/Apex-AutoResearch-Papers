# investigate batch stats p0 1 2

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_batch_stats_p0_1_2_20260523T112038_result.json`
- **Structured JSON:** [`2de633390c7b8485d0c2.json`](../../sessions/2d/2de633390c7b8485d0c2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完成。以下是完整分析。

---

## P0-1: b*=0 (clean batch) 真实比例

**定义等价性**: `b*=0` ⟺ `α_eff(0) ≥ τ`。代码中 `find_optimal_b()` 在 `alpha_0 >= tau` 时立即返回 0。两个定义完全相同。

**τ=0.7 (主实验) 的真实数据**:

| Seed | b*=0 count | b*=0 % |
|------|-----------|--------|
| 42   | 1,419 / 24,412 | **5.81%** |
| 123  | 1,391 / 24,412 | 5.70% |
| 456  | 1,449 / 24,412 | 5.94% |
| **Mean** | | **5.82%** |

appendix per-seed table 的 5.8% 是**正确的**（τ=0.7 数据）。

§5.4 的 "~2%" 来自 `binding_stats_seed42.json`，那是 **τ=0.8 实验**的数据（clean=1.91%）。

---

## P0-2: 三分类比例

**τ=0.7 (主实验, seed42) 的真实三分类**:

| Regime | Count | Pct |
|--------|-------|-----|
| α_eff-binding | 12,356 | **50.61%** |
| ESS-binding | 10,637 | **43.57%** |
| Clean (b*=0) | 1,419 | **5.81%** |

跨 seed 平均: **50.91% / 43.27% / 5.82%**

**论文两个版本都不对（都引用了错误的 τ=0.8 数据）**:

| 来源 | α_eff-bind | ESS-bind | Clean | 实际τ |
|------|-----------|----------|-------|------|
| §5.4 (results.tex:126) | 38.2% | 61.8% | ~2% | τ=0.8 |
| appendix fig caption (appendix.tex:144) | 38.2% | 59.8% | ~2% | τ=0.8 |
| appendix per-seed table (appendix.tex:331) | — | — | 5.8% | **τ=0.7** ✓ |
| **真实 τ=0.7 数据** | **50.6%** | **43.6%** | **5.8%** | **τ=0.7** ✓ |

---

## 61.8% vs 59.8% 的解释

这不是两个不同的数字源，而是**分类方式不同**（但都来自 τ=0.8 数据）:

- §5.4 用 **二分法**: "among the rest [非 clean]"，所以 61.8% = ESS-binding 在非 clean batches 中的占比（59.78% / 98.09% ≈ 61%），或者直接把 clean 归入 ESS: 59.78 + 1.91 ≈ 61.7%
- appendix 用 **三分法**: 38.2% / 59.8% / 2.0% 占全部 batches

---

## 根因

§5.4 和 appendix regime decomposition 图引用了 `binding_stats_seed42.json`，该文件由 `extract_figure_data.py` 对 `adaptive_fix_seed42` (τ=0.8) 的一个旧的完整训练运行生成。而主实验已经切换到 τ=0.7（`tau07_seed*`），但 regime 统计没有重新生成。

method.tex 中还有第三套数字（49.9% clean / 20.2% α_eff / 30.0% ESS, 26,458 batches, τ=0.8），也来自更早的版本。

**§5.4 的 batch 总数 25,991 也有问题** — 所有 ρ=0.4 完整实验都是 24,412 micro-batches (6,103 steps × 4)。25,991 不对应任何现有实验。

---
