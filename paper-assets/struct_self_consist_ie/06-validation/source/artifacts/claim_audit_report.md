# Claim Audit Report — struct_self_consist_ie (v3)

**Date**: 2026-05-23 (supersedes v2 from 2026-05-22)
**Scope**: All quantitative claims in `docs/paper/sections/*.tex` cross-verified against source tables/figures within the paper itself
**Method**: Extracted every numerical claim from abstract, introduction, single_signal, adaptive, theory, experiments_main; traced each to its source Table/Figure; checked cross-section consistency

---

## Executive Summary

- **55+ quantitative claims** checked
- **3 MISMATCH** found (2 in a single sentence of experiments_main.tex:76; 1 cross-section degeneracy inconsistency)
- **1 UNTRACED** claim (selective prediction "+5--8pp at 80% coverage" references a table that doesn't contain the data)
- All other claims PASS cross-verification

---

## MISMATCH（不一致）

| # | 声明位置 | 声明数值 | 来源数值 | 来源位置 | 修正建议 |
|---|----------|----------|----------|----------|----------|
| M1 | experiments_main.tex:76 "LP Δ collapses from +1.39 to **+0.09**pp" | +0.09pp | +0.12±0.04pp | appendix tab:epoch_confound (line 2094); experiments_main.tex:107 also uses +0.12pp | 将 +0.09 改为 +0.12。+0.09 疑似混淆了同段 footnote 中 corpus micro-F1 的 3-epoch 值（+0.09±0.03pp） |
| M2 | experiments_main.tex:76 "5-epoch: **31%**" 及 experiments_main.tex:107 "degeneracy rises from 13% to **31%**" | 31% | 26.4% | appendix tab:epoch_confound (line 2092) | 将 31% 改为 26%（或 26.4%）。31% 疑似混淆了 Qwen2.5-7B FT degeneracy（31.7%, tab:scale_comparison line 1609） |
| M3 | experiments_main.tex:91 "SciERC **13.4%**" | 13.4% | 12.2% | tab:fewnerd (line 70), tab:scale_comparison (line 1606) | 13.4% 出自 free-form ablation 表（appendix:1368, single seed）及 RE extension（appendix:1040），与 3-seed mean 12.2% 不一致。建议统一为 12.2% 或标注口径差异 |

## UNTRACED（无法溯源）

| # | 声明位置 | 数值 | 备注 |
|---|----------|------|------|
| U1 | experiments_main.tex:106 "QE signals support selective prediction (**+5--8pp at 80% coverage**; Table~\ref{tab:cross_selection})" | +5--8pp at 80% coverage | tab:cross_selection 仅包含 selection F1 数据，无 selective prediction / coverage 数据。appendix 中也未找到 selective prediction 结果表。该声明可能残留自旧版本（_archived/experiments_OLD.tex:254 有相同表述含 AUPRC 数据）。需补充数据来源、更正引用，或删除此声明 |

## PASS（一致）

| 声明位置 | 数值 | 来源 Table/Figure | 状态 |
|----------|------|-------------------|------|
| abstract:4, intro:6, intro:26 | AUROC up to 0.82 | tab:quality_estimation CoNLL EM AUROC=0.816 → rounds to 0.82 | PASS |
| intro:6 | ρ up to 0.45 | tab:quality_estimation CoNLL EM ρ=0.451 → rounds to 0.45 | PASS |
| intro:6, single_signal:39, experiments:71 | LP +1.39pp Few-NERD | tab:fewnerd: +1.39pp, p<.001 | PASS |
| abstract:6, intro:12,19,30, experiments:104 | +1.40pp entity construction Few-NERD | tab:entity_construction: +1.40±0.51pp, p<.001 | PASS |
| single_signal:50, theory:38 | α = 0.000--0.121 | tab:bound_verification: 0.000 (CoNLL) to 0.121 (FN s123) | PASS |
| theory:38, experiments:113 | 8--33× tighter | 1/α range: 1/0.121≈8.3× to higher ratios at small α | PASS |
| theory:11,18; appendix:1557 | R² > 0.999 | fig:oracle_scaling caption & appendix text | PASS |
| single_signal:50 | R² < 0 | Multi-factor regression context, consistent usage | PASS |
| single_signal:39, tab:selection | p = 0.29 (LP SciERC) | tab:selection LP p=.29 | PASS |
| single_signal:42, experiments:104 | p < 0.001 | tab:fewnerd p<.001; tab:entity_construction p<.001 | PASS |
| abstract:6, intro:12, experiments:105 | global Holm p_adj = 0.055 | tab:holm_family test #24: p_adj=0.055 (k=57) | PASS |
| abstract:6, intro:12, experiments:105 | per-family p_adj = 0.006 | Construction family k=10; raw p≈6×10⁻⁴ × 10 = 0.006 | PASS |
| single_signal:42 | Holm p_adj = 0.021, selection family k=21 | tab:holm_family: 21 selection tests (#1-21); consistent | PASS |
| intro:9, experiments:112 | degeneracy 12--68% | tab:fewnerd: 12.2%--67.9% → rounds to 12--68% | PASS |
| single_signal:46, experiments:69-71 | SciERC 12.2%, CoNLL 61.7%, WNUT 67.9%, FN 13.0% | tab:fewnerd: all match | PASS |
| adaptive:33 | cross-model +0.42pp (p<.001, CI [0.27, 0.58]) | tab:method_summary: +0.42pp (FN) | PASS |
| adaptive:38 | LGB AUC=0.923±0.002, +0.30pp | tab:method_summary: +0.30pp (OOF) | PASS |
| adaptive:39 | verifier transfer −0.76 to −1.02pp | appendix: −0.76, −1.02 | PASS |
| single_signal:54, adaptive tab | MRSC −3.1pp | tab:self_verification: 0.794−0.763=3.1pp | PASS |
| single_signal:54, adaptive tab | LSC −3.5pp | tab:self_verification: 0.794−0.759=3.5pp | PASS |
| single_signal:53, adaptive tab | ESJ AUROC 0.51 | tab:self_verification: 0.512 → rounds to 0.51 | PASS |
| intro:8, single_signal:53 | probe AUROC 0.63--0.88 | appendix: 0.636, 0.882, 0.630 → 0.63--0.88 | PASS |
| single_signal:53 | LODO 0.56--0.67 | appendix: 0.559, 0.671 → rounds correctly | PASS |
| single_signal:53,56 | Qwen3-8B ESJ AUROC 0.50--0.55 | tab:esj_cross: near-random all datasets | PASS |
| theory:12 | GPT-5.5: 50% degen, SJ ρ=0.346, MV +1.4pp | tab:frontier_sc_cross: 50.0%, .346, +1.4 | PASS |
| theory:12 | 6.8pp oracle headroom unrealized | oracle−MV = 0.720−0.652 = 6.8pp | PASS |
| theory:12 footnote | 10.1% GPT-5.5 parse failures | tab:frontier_sc_cross: Parse%=10.1 | PASS |
| intro:14 | SQL 87.2% degeneracy | appendix: 87.2% (Spider SQL, GPT-5.5) | PASS |
| intro:11, experiments:91 | RE 40% zero-F1 | appendix: 159/397=40% | PASS |
| theory:13 | Qwen2.5 31.7--46.2%, Qwen3 13.0%, GPT-5.5 50% | tab:scale_comparison + tab:frontier_sc_cross | PASS |
| experiments:104 | +0.32pp SciERC, −0.39pp CoNLL (construction) | tab:entity_construction | PASS |
| experiments:104 | D=13%, headroom=12.4pp (Few-NERD) | tab:scale_comparison: 13.0%, Hdr=12.4 | PASS |
| adaptive tab | DALS +0.71pp SciERC | appendix: +0.71±0.48pp | PASS |
| experiments:76 | LP 50× more seed-stable (σ=0.04 vs SJ 2.02pp) | 2.02/0.04=50.5× | PASS |
| single_signal:6 | 60% SciERC LP range < 0.041 nats | appendix: median 0.041 nats | PASS |
| single_signal:6 | within-instance std ratio 0.97× | appendix free-form table: 0.97× | PASS |
| single_signal:35 | oracle headroom 11.4pp (SciERC) | tab:selection 3-seed: 0.781−0.667=11.4pp | PASS |
| theory:23 | inverse scaling 40 of 58 transitions | appendix app:n_scaling | PASS |
| single_signal:49, experiments:81 | ρ=0.052, p=0.81, n=23 | fig:degeneracy_scatter caption consistent | PASS |
| single_signal:49, experiments:81 | ρ=−0.881 (within-setting) | Consistent across mentions | PASS |
| theory:11 | c≈0.61 (Few-NERD), c≈0.35 (SciERC) | appendix: same values | PASS |
| theory:37 | 3--12% recovery ratio | tab:bound_verification + appendix text "3--12%" | PASS |
| experiments:90 | MV −2.71pp (Few-NERD), +0.6pp (CoNLL N=64) | Consistent with fig/tab data | PASS |
| experiments:114 | +3.85pp MV pretrained N=32, D=5.4% | tab:pretrained_summary: +3.9pp (1dp), D=5.4% | PASS* |
| experiments:107 | construction +0.88→+0.20pp | tab:epoch_confound: +0.88→+0.20 | PASS |
| theory:26 | few-shot CoNLL SJ ρ .30→.44 | appendix: .304→.442 | PASS |
| experiments:106 | ρ_adj Few-NERD 0.516 | Internal consistency | PASS |
| adaptive tab | LR/MLP/RF −0.4 to −3.1pp | Consistent | PASS |
| experiments:7 | SciERC 551 test, Few-NERD 37648, CoNLL 3453, WNUT 1287 | Consistent with tab data | PASS |

\* +3.85pp rounds to +3.9pp at 1dp shown in tab:pretrained_summary. Precision differs but values are consistent.

---

## 重点检查项结果

### 1. α range "0.000--0.121": ✅ PASS
- single_signal.tex:50 — α=0.000--0.121 ✓
- theory.tex:38 — α=0.000--0.121 ✓
- 来源: tab:bound_verification, α from 0.000 (CoNLL) to 0.121 (FN s123)
- 全文一致

### 2. MV gains "+3.85pp" and "+4.06pp": ✅ PASS (precision note)
- +3.85pp (experiments_main.tex:114, N=32 pretrained): tab:pretrained_summary shows +3.9pp (1dp). 3.85 rounds to 3.9.
- +4.06pp (appendix:1687, N=16 pretrained): tab:pretrained_summary shows +4.1pp (1dp). 4.06 rounds to 4.1.
- D=5.4% at N=32: tab:pretrained_summary confirms 5.4%.

### 3. Degeneracy rates: ⚠️ PARTIAL FAIL
- 12--68% (intro, experiments): rounds of 12.2%--67.9% from tab:fewnerd. ✓
- Per-dataset values (12.2%, 13.0%, 61.7%, 67.9%): all match tab:fewnerd. ✓
- **5-epoch degeneracy "31%"**: tab:epoch_confound shows **26.4%**. ❌ MISMATCH (M2)
- **SciERC "13.4%" in RE context**: tab:fewnerd shows **12.2%**. ❌ MISMATCH (M3)

### 4. AUROC 0.82: ✅ PASS
- 来源: tab:quality_estimation CoNLL Qwen EM AUROC = 0.816 → 0.82 (2dp)
- abstract, intro, related_work 全文一致

### 5. ρ up to 0.45: ✅ PASS
- 来源: tab:quality_estimation CoNLL Qwen EM ρ = 0.451 → 0.45 (2dp)

### 6. "+1.39pp" vs "+1.40pp" 区分: ✅ PASS
- +1.39pp = LP best-of-N **selection** on Few-NERD (tab:fewnerd)
- +1.40pp = LP-weighted entity **construction** on Few-NERD (tab:entity_construction)
- 全文用法正确，两者来源不同、语境无混淆
- experiments:90 "LP-best +1.4pp" 是 +1.39 的简写，可接受

### 7. "8--33×" tighter bound: ✅ PASS
- α=0.121 → 1/0.121 ≈ 8.3× (最松端)
- 更小 α 值给出 ~33× (最紧端)
- 与 appendix 文字一致

### 8. R² < 0 和 R² > 0.999: ✅ PASS
- R² < 0: single_signal.tex:50, 多因子回归语境
- R² > 0.999: theory.tex:11,18, oracle scaling law
- 各自语境正确，无混淆

### 9. p 值: ✅ PASS
- p = 0.29 (LP SciERC): tab:selection ✓
- p < 0.001 (LP Few-NERD): tab:fewnerd ✓
- p < 0.001 (entity construction): tab:entity_construction ✓
- p < 0.001 (cross-model): CI [0.27, 0.58] excludes zero ✓
- p = 0.81 (degen vs LP, n=23): consistent across mentions ✓
- Holm corrections (0.055, 0.006, 0.021): all verified against tab:holm_family ✓

---

## 修正优先级

| 优先级 | 编号 | 位置 | 问题 | 建议修正 |
|--------|------|------|------|----------|
| **HIGH** | M1+M2 | experiments_main.tex:76 | 同一句有两处数值错误：+0.09→+0.12, 31%→26.4% | 改为 "5-epoch: 26%, LP Δ collapses from +1.39 to +0.12pp" |
| **HIGH** | M2 | experiments_main.tex:107 | 31% 应为 26.4% | 改为 "degeneracy rises from 13% to 26%" |
| **MEDIUM** | U1 | experiments_main.tex:106 | "+5--8pp at 80% coverage" 引用 tab:cross_selection 但该表无此数据 | 补充来源表或删除此声明 |
| **LOW** | M3 | experiments_main.tex:91 | SciERC degeneracy 13.4% vs 12.2% | 统一为 12.2%（3-seed mean）或注明子集差异 |
