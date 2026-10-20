# investigate rho06 tau07 binding

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_investigate_rho06_tau07_binding_20260523T114032_result.json`
- **Structured JSON:** [`21acce55d119ff012aa6.json`](../../sessions/21/21acce55d119ff012aa6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部到位。以下是 3 项验证的结果。

---

## 结果 1 — ρ=0.6 tau=0.7 binding stats（最高优先级）

appendix.tex:145 当前文本："ESS-binding rises to 66%, α_eff-binding drops to 33.4%"

**这些数字来自 tau=0.8 实验**（`contamination_60_adaptive_seed42_tau08`，实际 tau_batch=0.8），该实验给出 33.8% α_eff-binding / 64.9% ESS-binding。

**ρ=0.6 tau=0.7 的正确 binding stats**（使用 `adaptive_rho06_tau07_seed{42,123,456}`，tau=0.7 阈值分类）：

| Regime | seed42 | seed123 | seed456 | 3-seed 均值 |
|--------|--------|---------|---------|------------|
| α_eff-binding | 47.04% | 46.76% | 46.64% | **46.81%** |
| ESS-binding | 48.39% | 48.69% | 48.88% | **48.65%** |
| clean (b\*=0) | 4.57% | 4.55% | 4.48% | **4.54%** |

Mean b\* by regime (seed42): α_eff-binding=0.6352, ESS-binding=1.307, overall=0.9313

**结论**：appendix 需要将 "66% / 33.4%" 改为 "48.7% / 46.8% / 4.5% clean"。

---

## 结果 2 — Constraint regime figure 数据来源（第二优先级）

图文件：`artifacts/figures/constraint_regime_decomposition.{pdf,png}`，创建于 2026-05-16，修改于 2026-05-19。

**图中数据**（从 PNG 读取）：
- ρ=0.4 bar: 38.2% α_eff-binding, 60% ESS-binding, ~2% clean
- ρ=0.6 bar: 33.4% α_eff-binding, 66% ESS-binding, ~1% clean

**两个 bar 都有问题**：

1. **ρ=0.4 bar**：显示 38.2%/60%，但 ρ=0.4 tau=0.7 的正确数据是 50.6%/43.6%/5.8%（`tau07_seed42`，与 appendix 文本 "50.9%/43.3%/5.8%" 一致）。图中 38.2%/60% 实际匹配 `binding_stats_seed42.json`（38.3%/59.78%），该 json 是对 **ρ=0.6 数据用 tau=0.8 阈值** 错误分类的结果。

2. **ρ=0.6 bar**：显示 33.4%/66%，来自 `contamination_60_adaptive_seed42_tau08`（真实 tau=0.8）。正确的 tau=0.7 值是 47.0%/48.4%/4.6%。

**根因**：`extract_figure_data.py` 的 `classify_regime()` 硬编码 `tau=0.8`，以及图生成可能直接用了错误分类的数据。

**需要**：用 tau=0.7 阈值重新计算两组 binding stats 并重新生成图。

---

## 结果 3 — 4.9× sharpening exponent ratio（第三优先级）

Introduction: "at 4.9× lower sharpening exponents than an ESS-only alternative"

**tau=0.7 下的 sharpening ratio**：

| 设置 | α_eff-binding mean b\* | ESS-only mean b\* | ratio |
|------|----------------------|-------------------|-------|
| ρ=0.4 tau=0.7 | 0.614 | 3.550 | **5.78×** |
| ρ=0.6 tau=0.7 | 0.635 | 3.126 | **4.92×** |

对比 tau=0.8（原始数据）：
| 设置 | α_eff-binding mean b\* | ESS-only mean b\* | ratio |
|------|----------------------|-------------------|-------|
| ρ=0.6 tau=0.8 | 1.099 | 3.126 | **2.85×** |

**结论**：
- Introduction 中 "4.9×" 如果指的是 ρ=0.6，在 tau=0.7 下仍然成立（4.92×），无需修改
- 但 Introduction 同时写了 "50.9% of batches"，这个数来自 ρ=0.4。如果 50.9% 和 4.9× 要对应同一设置（ρ=0.4），那 ratio 应该是 **5.8×** 而非 4.9×
- 建议：确认 Introduction 句子要引用哪个 ρ 的数据。如果是 ρ=0.4 → "5.8×"；如果是 ρ=0.6 → "4.9×"（但 α_eff-binding% 应改为 46.8%）

---
