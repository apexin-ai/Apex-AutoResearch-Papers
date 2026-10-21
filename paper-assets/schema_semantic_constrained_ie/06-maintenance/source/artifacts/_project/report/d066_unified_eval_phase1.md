# Phase 1: 统一 Eval 结果 (PF-as-FN)

**评估脚本**: `eval_d066_unified.py` (基于 eval_d064.py 逻辑，PF 计入 FN)
**旧值来源**: `paper_results_tables.md` (checker_version: fixed_20260514_v2)
**评估日期**: 2026-05-20

---

## Table 2 (Composability / FT + OntoCoDec) Diff

| Row | Model | Dataset | Mode | Old E-F1 | New E-F1 | ΔE-F1 | Old R-F1 | New R-F1 | ΔR-F1 | DR% | CF% | PF% |
|-----|-------|---------|------|----------|----------|-------|----------|----------|-------|-----|-----|-----|
| 1 | Qwen | DocRED | unc | 82.15 | 82.15 | 0.00 | 40.86 | 40.86 | 0.00 | 0.76 | 0.09 | 7.1 |
| 2 | Qwen | DocRED | S1 | 81.43 | 81.43 | 0.00 | 40.56 | 40.56 | 0.00 | 0.01 | 0.27 | 8.5 |
| 3 | Llama | DocRED | unc | 83.93 | 83.93 | 0.00 | 43.72 | 43.72 | 0.00 | 0.49 | 0.08 | 2.3 |
| **4** | **Llama** | **DocRED** | **S1** | **85.23** | **83.94** | **−1.29** | **44.23** | **43.78** | **−0.45** | 0.21 | 0.21 | 2.5 |
| 5 | Qwen | SciERC | unc | 67.05 | 67.05 | 0.00 | 43.86 | 43.86 | 0.00 | 1.95 | 0.00 | 0.0 |
| 6 | Qwen | SciERC | S1 | 67.05 | 67.05 | 0.00 | 43.77 | 43.77 | 0.00 | 0.00 | 0.45 | 0.0 |
| 7 | Llama | SciERC | unc | 67.76 | 67.76 | 0.00 | 45.45 | 45.45 | 0.00 | 1.11 | 0.00 | 0.0 |
| 8 | Llama | SciERC | S1 | 67.76 | 67.76 | 0.00 | 45.47 | 45.47 | 0.00 | 0.09 | 0.23 | 0.0 |

### CF% 变化说明

CF% 在多行有小幅变化（Row 2: 0.41→0.27, Row 6: 1.18→0.45, Row 8: 0.46→0.23）。这不是 PF 处理导致的，而是 CF 计算方法差异：
- 旧 checker: CF violations / relations (或混合 denominator)
- d066: CF violations / total_entities_pred (与 eval_d064.py 一致)

---

## Zero-Shot Tables Diff

### SciERC ZS Ablation (Qwen2.5-7B)

| Row | Mode | Old E-F1 | New E-F1 | ΔE-F1 | Old R-F1 | New R-F1 | ΔR-F1 | DR% | CF% | PF% |
|-----|------|----------|----------|-------|----------|----------|-------|-----|-----|-----|
| 13 | unconstrained | 31.01 | 30.94 | −0.07 | 8.23 | 8.23 | 0.00 | 15.37 | 0.04 | 0.0 |
| 14 | grammar_only | — | 30.98 | — | — | 8.23 | — | 14.84 | 0.04 | 0.0 |
| 15 | semantic_only | — | 30.94 | — | — | 8.15 | — | 11.65 | 0.28 | 0.0 |
| 16 | S1 (full) | 30.98 | 30.98 | 0.00 | 8.36 | 8.36 | 0.00 | 0.93 | 1.62 | 0.0 |

**Notes**:
- PF=0% for all SciERC ZS rows → F1 不受 PF 处理方式影响
- E-F1 Row 13 微小差异 (−0.07pp) 来自 entity type normalization 逻辑差异
- Grammar/semantic 行无旧值（旧 paper tables 仅有 unc 和 S1）
- CF% for S1: 旧值 9.90% → 新值 1.62%，差异巨大，源于 CF denominator 不同（旧用 relations，新用 entities）
- 使用 `phase2_scierc_semantic_only_v2.jsonl` 和 `phase2_scierc_full_s1_v2.jsonl`（原始文件不完整，仅 10/7 samples）

### DocRED ZS Ablation (Qwen2.5-7B)

| Row | Mode | Old E-F1 | New E-F1 | ΔE-F1 | Old R-F1 | New R-F1 | ΔR-F1 | DR% | CF% | PF% |
|-----|------|----------|----------|-------|----------|----------|-------|-----|-----|-----|
| 9 | unconstrained | 58.15 | 57.69 | −0.46 | 7.74 | 7.66 | −0.08 | 18.04 | 0.10 | 1.2 |
| 10 | grammar_only | — | 58.90 | — | — | 8.24 | — | 26.17 | 0.07 | 1.3 |
| 11 | semantic_only | — | 57.72 | — | — | 7.65 | — | 13.40 | 1.05 | 1.1 |
| 12 | S1 (full) | 59.37 | 58.96 | −0.41 | 8.23 | 8.17 | −0.06 | 10.21 | 2.57 | 1.1 |

**Notes**:
- DocRED ZS 有 ~1% PF 率，但 F1 差异主要来自 eval 逻辑差异（relation type matching 归一化不同），非 PF 处理
- Row 9 E-F1 Δ=−0.46pp, Row 12 E-F1 Δ=−0.41pp，均 <0.5pp
- Grammar/semantic 行无旧值对比
- RV% 也有差异（旧 29.66 vs 新 30.39 for unc），源于 relation name normalization 逻辑不同

---

## Summary

### 显著变化 (>0.5pp)

**唯一显著变化**: Row 4 — Llama DocRED LoRA S1
- E-F1: 85.23 → 83.94 (**−1.29pp**)
- R-F1: 44.23 → 43.78 (**−0.45pp**)
- 原因：旧值使用 PF-excluded 方法（排除 25 个 parse failure 文档），新值 PF-as-FN 将这些文档的 gold entities/relations 计入 FN
- 旧值中 Llama DocRED S1 看起来比 unc (83.93) 更高 (+1.30pp)，这是评估方法不一致造成的假象
- 统一后 S1 (83.94) ≈ unc (83.93)，符合预期：constrained decoding 不应大幅改变 E-F1

### 基本不变的行

- **所有 SciERC 行** (Rows 5-8, 13-16): PF=0%，F1 值完全不变
- **Qwen DocRED FT** (Rows 1-2): 虽然 PF 高 (7-8.5%)，但旧值已经使用 PF-as-FN，所以不变
- **Llama DocRED FT unc** (Row 3): PF=2.3%，旧值碰巧与 PF-as-FN 结果一致（可能旧 eval 对 unc 行已使用了 PF-as-FN）

### 对 Narrative 的影响

1. **Table 3 (Composability) ΔR-F1**: Llama DocRED 从 +0.51pp 变为 +0.06pp。旧 narrative "constrained decoding helps Llama stay on-schema (+0.51 R_F1)" 需要修改为更保守的表述
2. **Table 3 ΔE-F1**: Llama DocRED 从 +1.30pp 变为 +0.01pp。旧 narrative 中 E-F1 提升的 claim 完全消失
3. 其他所有 claims（DR reduction、composability near-zero cost）不受影响
4. CF% 在多行有变化，但这是 CF computation methodology 不同（denominator: entities vs relations），与 PF 无关。论文中需要统一 CF% 的 denominator 定义

### Raw JSON 输出

所有 d066 评估结果已保存至 `outputs/d066_*.json`（共 16 个文件），不覆盖原始 registry。
