# 全文数字追溯审计报告

审计日期: 2026-05-24
审计范围: 主文全部 sections + Appendix 10 个重点 table
方法: 逐 cell 与 experiment registry 交叉验证 + 内部算术验证 + 跨位置一致性检查

---

## 一、7 个 Bug-Prone 数字 — 全部通过 ✅

| # | 数字 | 位置 | 验证结果 |
|---|------|------|---------|
| 1 | SciERC EM AUROC = .631 | Tab quality_estimation, tab:multiseed | ✅ 论文正确（D114 修正后值）。Registry/provenance 仍存旧值 .749（stale） |
| 2 | Headroom = 13.0pp | Tab selection, fig_selection_gap | ✅ Oracle .775 − Greedy .645 = .130 = 13.0pp |
| 3 | MV = +0.6pp | Intro, §4.3, fig_n_scaling | ✅ Registry 0.64pp → 0.6 (1dp) |
| 4 | α = 0.121 | §4.1, theory.tex | ✅ 跨位置一致 |
| 5 | SciERC construction = +0.32pp n.s. | §4.5, tab:entity_construction | ✅ 算术验证: (.6701−.6669)×100 = 0.32 |
| 6 | fig_selection_gap Oracle = +13.0pp | fig caption | ✅ = #2 |
| 7 | Holm p_adj=0.006 (k=10) / p_adj=0.055 (k=57) | Abstract, §4.5, limitations, tab:holm | ✅ 算术正确，step-up enforcement 正确 |

---

## 二、统计摘要

| 类别 | 主文 | 附录 | 合计 |
|------|------|------|------|
| 已验证 (✅) | ~70 cells | ~180 cells | ~250 |
| 严重问题 (❌) | 3 | 3 | 6 |
| 中等问题 (⚠️) | 11 | 3 | 14 |
| 轻微/舍入 (△) | 3 | 4 | 7 |
| 不可验证 (❓) | ~30 | 6 | ~36 |

---

## 三、严重问题 (6)

### 主文 (3)

**M-1. Tab selection vs Tab fewnerd SciERC 基线不一致**
- Tab selection (§4.1): Greedy = .645, LP Δ = +0.2pp
- Tab fewnerd (§4.3): Greedy = .663, LP Δ = +0.61pp
- 原因: 不同种子集 / 不同评估 pipeline（Tab selection = bootstrap 2-seed; Tab fewnerd = 3-seed mean instance-averaged F1）
- 论文 caption 已注明 footnote 区分，但数值差距 1.8pp 较大
- **此前 Director 已决策: 不改，DDL-36h 改动风险大于收益**

**M-2. Registry EM AUROC stale (.749 vs 论文 .631)**
- 论文已正确写 .631，但 registry exp_012_rerun_1024 和 provenance c002 仍存旧值
- **不影响论文**，仅影响后续内部操作引用 registry 时可能取到错误值

**M-3. LP ρ 跨表不一致 (Tab quality_estimation vs Tab fewnerd)**
- SciERC LP ρ: .205 (seed42) vs .159 (3-seed entity-type-averaged)
- CoNLL LP ρ: .316 vs .302
- 原因: Tab quality_estimation = instance-averaged, Tab fewnerd = entity-type-averaged + 不同 seed set
- Tab scale_comparison caption 已注明 "entity-type-averaged macro-F1, which differs from instance-averaged F1 in Table tab:fewnerd"

### 附录 (3)

**A-1. tab:robustness SJ N=16 RE = 0.281**
- 3-seed mean ≈ 0.276。Paper 0.281 匹配单 seed (exp_008_re_n16_v2)，与表头 "3-seed" 不符

**A-2. tab:robustness FK N=16 RE = 0.279**
- 3-seed mean = 0.296。Registry 中无任何实验给出 0.279。来源不明

**A-3. tab:fewnerd_epoch 3-epoch SJ mean = 0.685**
- Registry 3-seed mean = 0.677，差 0.008

---

## 四、中等问题 (14)

| # | 问题 | 位置 | 影响 |
|---|------|------|------|
| M-4 | Construction +1.40 (non-CV) vs +0.88 (CV) 交替使用 | §4.5 | 读者可能混淆 |
| M-5 | LP selection +1.39pp: 主种子 1.36pp, 3-seed mean 无法直接验证 | §4.1, Tab fewnerd | 低——结论不变 |
| M-6 | Tab selection LP p=.29 vs registry permutation_p=.39 | Tab selection | 低——均不显著 |
| M-7 | Holm p_adj=0.021 k=21 vs provenance 0.019 k=19 | §4.1 footnote | 低——provenance stale |
| M-8 | Few-NERD degen 13.0%: 3-seed mean 计算为 11.8% | Tab fewnerd | 中——0.012 差异 |
| M-9 | RE 40% zero-F1 vs registry 44.3% | §4.2 | 低——引用不同配置 |
| M-10 | SciERC degen 12.2% vs exp_012 17.77% | Tab fewnerd | 中——来源不明确 |
| M-11 | Few-NERD LP ρ=.220 vs registry lp_global_rho=.4215 | Tab fewnerd | 中——不同 LP 定义 |
| M-12 | SciERC constr +0.32pp vs registry +1.12~1.67pp | §4.5 | 中——不同评估方法 |
| M-13 | Supervised -0.4 to -3.1pp 上界无 registry 来源 | Tab method_summary | 低 |
| A-4 | tab:multiseed caption "5 seeds" 实际 FK/VC/EM 仅 3 seeds | Appendix | 中——描述不精确 |
| A-5 | tab:scale_comparison LP 定义跨行不一致 | Appendix | 低——reader-facing |
| A-6 | tab:fewnerd_epoch caption "2-seed" 实际混用 2/3-seed | Appendix | 低——描述不精确 |
| M-14 | Degeneracy 度量类型 (exact-match vs constant-F1) 正文交替使用 | §4.5 | 低——脚注已说明 |

---

## 五、轻微舍入差异 (7)

| 位置 | Paper | Registry | 差异 |
|------|-------|----------|------|
| tab:robustness SJ T=0.7 NER | 0.364 | 0.365 | 0.001 |
| tab:robustness SJ N=16 NER | 0.411 | 0.410 | 0.001 |
| tab:entity_construction Few-NERD LP σ | .005 | .006 | .001 |
| tab:entity_construction Few-NERD Unif σ | .006 | .007 | .001 |
| tab:fewnerd_epoch MV Δ | −2.74 | −2.71 (3-seed) | 0.03 |
| tab:fewnerd_epoch LP Δ | +1.39 | +1.38 (4-seed) | 0.01 |
| AUROC abstract "0.82" | .82 | .816 | 2dp rounding |

---

## 六、不可验证 (~36 cells)

主要类别:
- 理论推导值 (α, θ_crit, R², scaling exponents): ~15
- Appendix 实验 (mechanistic probes, selective prediction): ~10
- 来自不同 pipeline 的统计检验值 (bootstrap p, Wilcoxon p): ~5
- r1024 缺失种子 (LLaMA CoNLL N=16): ~4
- 其他零散值: ~2

---

## 七、跨表一致性全局检查

| 检查项 | 结果 |
|--------|------|
| tab:wnut 20/20 cells | ✅ 完全匹配 |
| tab:72b 53/54 cells | ✅ (1 cell 不可验证) |
| tab:holm 47 p_adj 算术 | ✅ 全部正确 |
| tab:entity_construction Δ 算术 | ✅ 全部正确 |
| tab:cross_selection 全部 cells | ✅ |
| SJ N=8 T=1.0 NER ρ=.360 跨 3 个表 | ✅ 一致 |
| SciERC EM AUROC=.631 跨 2 个表 | ✅ 一致 (D114 修正) |
| Oracle/Headroom 13.0pp 跨 text/fig/tab | ✅ 一致 |
| p_adj=0.055 跨 Abstract/§4.5/Limitations/tab:holm | ✅ 一致 |

---

## 八、结论

**7 个重点监控数字全部正确。** 论文主要数值与 registry 交叉验证率约 70%。

6 个严重问题中:
- M-1 (SciERC baseline 跨表) — 此前 Director 已决策接受，caption 已有区分说明
- M-2 (Registry stale) — 不影响论文，仅影响内部工具
- M-3 (LP ρ 跨表) — caption 已注明不同 F1 定义
- A-1, A-2 (tab:robustness N=16 RE) — 附录表格，2 个 cell 可能使用单 seed 而非 3-seed mean
- A-3 (tab:fewnerd_epoch SJ) — 附录表格，差 0.008

**建议**:
- A-1/A-2 如 Director 同意可快速修复 (改为 3-seed mean 或标注 single-seed)
- 其余不建议 DDL 前修改
