# W1 CF Fallback SciERC Pilot — Analysis Report

**Date**: 2026-05-15
**Experiment**: w1_cf_fallback_scierc_pilot
**Dataset**: SciERC (551 test samples)
**Model**: Qwen3-8B, full_s1 mode with CF fallback
**Checker version**: fixed_20260514_v2 (strip + alias + unique_et)

---

## 1. Completion Status

**正常完成。** 551/551 samples processed, success=551, fail=0, JSON parse failures=0.

---

## 2. Violation Rates

| Metric | w1_cf_fallback (pilot) | phase2_full_s1 (baseline) | Δ | 判定 |
|--------|----------------------|--------------------------|---|------|
| ET (Entity Type) | 0.00% (0/2474) | 0.00% | 0.00 | ✓ |
| RV (Relation Vocab) | 0.00% (0/1725) | 0.00% | 0.00 | ✓ |
| DR (Domain/Range) | **14.78%** (255/1725) | 0.93% | **+13.85pp** | **✗ FAIL** |
| CF (Cross-Field) | **0.04%** (1/1725) | 9.90% | **-9.86pp** | ✓ |
| Violation Budget (DR+CF) | 14.82% | 10.83% | +3.99pp | ✗ |

### Per-Relation DR Breakdown

| Relation | Total | DR Violations | Rate |
|----------|-------|---------------|------|
| Feature-of | 494 | 158 | 31.98% |
| Compare | 71 | 28 | 39.44% |
| Part-of | 77 | 18 | 23.38% |
| Evaluate-for | 134 | 31 | 23.13% |
| Hyponym-of | 125 | 18 | 14.40% |
| Used-for | 791 | 2 | 0.25% |
| Conjunction | 33 | 0 | 0.00% |

---

## 3. F1 Metrics

| Metric | w1_cf_fallback (pilot) | phase2_full_s1 (baseline) | Δ | 判定 |
|--------|----------------------|--------------------------|---|------|
| E-F1 | 30.98% (P=25.98, R=38.37) | 30.98% | 0.00pp | ✓ |
| R-F1 | 8.23% (P=6.43, R=11.40) | 8.36% | -0.13pp | ✓ |

Entity/Relation counts: Entities=2474, Relations=1725 (baseline: 2474/1729).

---

## 4. Fallback Trigger Statistics

| Metric | Value |
|--------|-------|
| Total mask calls | 17,024 |
| Grammar-first fallback | 6,237 (36.64%) |
| CF-registry fallback | 763 (4.48%) |
| **Combined fallback rate** | **41.12%** |

Grammar-first fallback: semantic mask eliminates all grammar-valid tokens → fall back to grammar-only.
CF-registry fallback: CF constraint specifically triggers the conflict.

---

## 5. Comparison with Unconstrained Baseline

| Metric | w1_cf_fallback | unconstrained | full_s1 |
|--------|---------------|---------------|---------|
| DR | 14.78% | 15.37% | 0.93% |
| CF | 0.04% | ~0% | 9.90% |
| R-F1 | 8.23% | 8.23% | 8.36% |
| E-F1 | 30.98% | 31.01% | 30.98% |

CF fallback 后的结果几乎完全等同于 unconstrained baseline。

---

## 6. Conclusion: **NEGATIVE**

### 判定

| 标准 | 阈值 | 结果 | 判定 |
|------|------|------|------|
| CF 显著下降 | < 9.90% | 0.04% | ✓ PASS |
| DR 保持低 | < 2% | 14.78% | **✗ FAIL** |
| R-F1 不显著下降 | Δ < -2pp | -0.13pp | ✓ PASS |

CF 成功降低，但 DR 灾难性恶化（+13.85pp），整体违反率上升 3.99pp。

### Root Cause Analysis

1. **Fallback 触发过于频繁**：41.12% 的 token 生成触发了 fallback，意味着语义约束在近半数 token 位置被完全绕过
2. **Grammar-first fallback 占主导**（36.64% vs CF-specific 4.48%）：大量 fallback 并非 CF 约束本身引起，而是整体 semantic mask 与 grammar mask 冲突
3. **退化为 unconstrained**：DR/CF/F1 指标与 unconstrained baseline 几乎完全一致，说明 fallback 机制实质上禁用了约束解码
4. **DR 集中在特定关系类型**：Feature-of (32%), Compare (39%), Part-of (23%), Evaluate-for (23%) 是主要受灾区

### W1 Issue Implication

简单的 grammar-first CF fallback 不可行。需要更精细的方案：
- **Partial relaxation**: 仅放松 CF 约束而保留 DR 约束，而非完全回退到 grammar-only
- **Selective fallback**: 仅在 CF-specific 冲突时放松，grammar-first fallback 应保留 DR mask
- **Constraint re-examination**: 检查 SciERC ontology 中高冲突关系类型的约束定义是否过严
- **Two-pass approach**: 第一遍 constrained（保 DR），第二遍 post-hoc 修复 CF violations
