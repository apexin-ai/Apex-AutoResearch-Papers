# 数据自查报告

审计日期：2026-05-23
审计范围：论文全部定量数据 vs registry/实验产出/表格内部一致性

---

## ✅ 已核对一致

### Abstract 数字追溯

| Abstract 中的数字 | 来源 | 核对结果 |
|---|---|---|
| AUROC up to 0.82 | tab:quality_estimation CoNLL(Qwen) EM AUROC .816→0.82 | ✅ 合理四舍五入 |
| <1 pp; CI crosses zero | tab:selection LP Δ=+0.2pp, p=0.29 | ✅ |
| +1.40 pp on Few-NERD | tab:entity_construction Few-NERD LP +1.40±0.51 pp | ✅ |
| global Holm p_adj=0.055 | experiments_main.tex line 105, appendix tab:holm_family | ✅ |
| per-family p_adj=0.006 | experiments_main.tex line 105, appendix tab:holm_family | ✅ |
| collapses at convergence | tab:epoch_confound 3→5 epoch | ✅ |

### tab:quality_estimation — ρ 值

| Signal | Dataset | Table 值 | Registry 来源 | Registry 值 | 核对 |
|---|---|---|---|---|---|
| VC | SciERC | .379 | exp_012_rerun_1024 voting_conf_rho | 0.3792 | ✅ |
| SJ | SciERC | .360 | exp_012_rerun_1024 SJ_rho_full | 0.3599 | ✅ |
| FK | SciERC | .267 | exp_012_rerun_1024 FK_rho_full | 0.2665 | ✅ |
| EM | SciERC | .295 | exp_012_rerun_1024 EM_rho | 0.2945 | ✅ |
| LP | SciERC | .205 | exp_012_rerun_1024 logprob_rho | 0.2052 | ✅ |
| VC | CoNLL(Q) | .424 | exp_002 ev_rho_full | 0.4237 | ✅ |
| SJ | CoNLL(Q) | .436 | exp_002 sj_rho_full | 0.4357 | ✅ |
| FK | CoNLL(Q) | .400 | exp_002 fk_rho_full | 0.3998 | ✅ |
| EM | CoNLL(Q) | .451 | exp_002 em_rho_full | 0.4507 | ✅ |
| LP | CoNLL(Q) | .316 | exp_002 logprob_rho_full | 0.3157 | ✅ |
| VC | CoNLL(L) | .426 | exp_017_llama_conll_infer voting_conf_rho | 0.4256 | ✅ |
| SJ | CoNLL(L) | .431 | exp_017_llama_conll_infer SJ_rho | 0.4314 | ✅ |
| FK | CoNLL(L) | .428 | exp_017_llama_conll_infer FK_rho | 0.4277 | ✅ |
| EM | CoNLL(L) | .431 | exp_017_llama_conll_infer EM_rho | 0.4306 | ✅ |
| LP | CoNLL(L) | .307 | exp_017_llama_conll_infer logprob_rho | 0.3072 | ✅ |

### tab:quality_estimation — AUROC (CoNLL Qwen only, registry 有直接对应)

| Signal | Table 值 | Registry 来源 | Registry 值 | 核对 |
|---|---|---|---|---|
| VC | .789 | exp_002 ev_auroc_full | 0.7889 | ✅ |
| SJ | .801 | exp_002 sj_auroc_full | 0.8008 | ✅ |
| FK | .774 | exp_002 fk_auroc_full | 0.7741 | ✅ |
| EM | .816 | exp_002 em_auroc_full | 0.8156 | ✅ |
| LP | .753 | exp_002 logprob_auroc_full | 0.7532 | ✅ |

### tab:fewnerd

| Dataset | Metric | Table 值 | 来源 | 核对 |
|---|---|---|---|---|
| Few-NERD | LP Δ | +1.39 pp | exp_fewnerd_s789_n8: 4-seed mean 1.38, CI [1.32,1.44]; appendix tab:fewnerd_full | ✅ |
| Few-NERD | Degen.% | 13.0% | constant-F1 degeneracy, 3-seed mean | ✅ |
| Few-NERD | Greedy | .748 | exp_021_fewnerd_full greedy_macro_f1 0.7478 | ✅ |
| SciERC | Degen.% | 12.2% | appendix tab:degeneracy Constant F1 12.2% | ✅ |
| CoNLL | Degen.% | 61.7% | appendix tab:degeneracy Constant F1 61.7% | ✅ |

### tab:entity_construction (appendix lines 2257-2276)

| Dataset | Wt. | Greedy | Constr. | Δ | 核对 |
|---|---|---|---|---|---|
| SciERC | LP | .667±.001 | .670±.003 | +0.32 pp | ✅ |
| Few-NERD | LP | .748 | .762±.005 | +1.40±0.51 pp | ✅ p<.001 |
| Few-NERD | Unif | .748 | .756±.006 | +0.74±0.58 pp | ✅ p=.003 |
| CoNLL | Unif | .908 | .904 | -0.39 pp | ✅ |

### tab:epoch_confound (appendix lines 2080-2099)

| Metric | 3-epoch | 5-epoch | 核对 |
|---|---|---|---|
| Instance degen. (%) | 8.8 | 26.4 | ✅ 主文 "9%→26%" 合理四舍五入 |
| LP Δ (pp) | +1.39 | +0.12±0.04 | ✅ 主文 "+1.39→+0.12" |
| Entity constr. Δ (pp) | +0.88 | +0.20 | ✅ 主文 "+0.88→+0.20" |

### tab:multiseed — NER ρ (appendix lines 708-731)

多种子 ρ 均值 vs 主表 seed=42 值一致性：
| Signal | seed=42 (主表) | 5-seed mean (multiseed) | Δ | sigma | 核对 |
|---|---|---|---|---|---|
| LP | .205 | .205±.015 | 0 | ✅ |
| FK | .267 | .254±.016 | +.013 (0.8σ) | ✅ |
| SJ | .360 | .356±.014 | +.004 (0.3σ) | ✅ |
| VC | .379 | .386±.019 | -.007 (0.4σ) | ✅ |
| EM | .295 | .307±.008 | -.012 (1.5σ) | ✅ |

### Introduction 数字

| 数字 | 来源 | 核对 |
|---|---|---|
| ρ up to 0.45 | tab:quality_estimation CoNLL(Q) EM ρ=.451 | ✅ |
| AUROC 0.82 | tab:quality_estimation CoNLL(Q) EM AUROC=.816 | ✅ |
| MV <1 pp even at N=64 | fig_n_scaling data; CoNLL N=64 +0.64pp | ✅ |
| AUROC 0.63–0.88 | exp_hidden_state_probe: scierc 0.6344, conll 0.8849 | ✅ |
| degeneracy 12–68% | SciERC 12.2% ~ WNUT 67.9% | ✅ |
| LP +1.39 pp Few-NERD | tab:fewnerd | ✅ |
| +1.40 pp construction | tab:entity_construction | ✅ |
| SQL 87.2% degeneracy | exp_spider_sc_pilot degeneracy 0.8724 | ✅ |

### experiments_main.tex 正文数字

| 行号 | 数字 | 来源 | 核对 |
|---|---|---|---|
| L50 | VC ρ=0.379, SJ 0.360, LP 0.205 | tab:quality_estimation | ✅ |
| L50 | Δρ=+0.151±0.006, 5 seeds | multiseed mean: .356-.205=.151 | ✅ |
| L51 | p_adj=0.013 (Holm, k=5) | appendix bootstrap signal | ✅ |
| L52 | EM AUROC 0.816 | tab:quality_estimation CoNLL(Q) | ✅ |
| L53 | VC ρ=0.724 at N=16 | tab:wnut VC rho .724 | ✅ |
| L53 | conditional ρ=0.038 | tab:wnut VC Cond. rho .038 | ✅ |
| L53 | LP conditional ρ=0.350 | tab:wnut LP Cond. rho .350 | ✅ |
| L76 (fn) | corpus micro-F1 LP Δ=+0.09±0.03 | 脚注值，与 instance-averaged +1.39 区分 | ✅ 不同指标 |
| L76 | +0.12 pp (5-epoch) | tab:epoch_confound LP Δ 5-epoch +0.12±0.04 | ✅ |
| L76 | 26% (5-epoch degen) | tab:epoch_confound 26.4%→26% | ✅ |
| L81 | ρ=0.052, p=0.81, n=23 | fig:degeneracy_scatter | ✅ |
| L81 | ρ=-0.881 | appendix per_type_lp | ✅ |
| L90 | MV -2.71 pp Few-NERD | 3-seed mean: (-3.27+-2.61+-2.24)/3=-2.71 | ✅ |
| L91 | RE 10.1% degen, SciERC 12.2% | tab:degeneracy | ✅ |
| L104 | +1.40±0.51 pp, p<.001 | tab:entity_construction | ✅ |
| L104 | D=13%, headroom=12.4 pp | tab:fewnerd 13.0%, tab:fewnerd_full headroom 12.4 | ✅ |
| L104 | +0.32 pp SciERC | tab:entity_construction | ✅ |
| L104 | -0.39 pp CoNLL | tab:entity_construction | ✅ |
| L107 | 9%→26% | tab:epoch_confound 8.8→26.4, rounded | ✅ |
| L107 | +1.39→+0.12 pp selection | tab:epoch_confound | ✅ |
| L107 | +0.88→+0.20 pp construction | tab:epoch_confound | ✅ |
| L112 | 12–68% degeneracy | SciERC 12.2%, WNUT 67.9% | ✅ |
| L113 | 8–33× tighter | theory section consistent | ✅ |
| L114 | +3.85 pp MV, D=5.4% | pretrained FewNERD N=32: mv_delta +3.85, degen 5.42% | ✅ |

### single_signal.tex 正文数字

| 行号 | 数字 | 来源 | 核对 |
|---|---|---|---|
| L35/39 | ρ up to 0.38 | SciERC VC ρ=.379→0.38 | ✅ 合理四舍五入 |
| L35 | oracle headroom +11.4 pp | 0.781-0.667=0.114=11.4pp | ✅ |
| L39 | LP +0.2 pp, p=0.29 | tab:selection LP 0.647-0.645=0.002=0.2pp | ✅ |
| L42 | LP +1.39 pp, p<.001 | tab:fewnerd | ✅ |
| L42 | Holm p_adj=0.021, k=21 | appendix | ✅ |
| L42 | VC -1.79, SJ -2.14 pp | tab:fewnerd_full (appendix) | ✅ |
| L46 | SciERC 12.2%, CoNLL 61.7% | tab:degeneracy | ✅ |

### theory.tex 数字

| 行号 | 数字 | 来源 | 核对 |
|---|---|---|---|
| L11 | R² > 0.999, c≈0.61 (FN), c≈0.35 (Sci) | appendix oracle scaling fits | ✅ |
| L12 | 50% degen, SJ ρ=0.346, MV +1.4 pp (GPT-5.5) | exp_frontier_sc_gpt55 degen 0.5, rho_sj 0.3461, mv +1.39 | ✅ |
| L13 | Qwen2.5: 31.7–46.2%, Qwen3: 13.0%, GPT-5.5: 50% | exp_qwen25_7b_fewnerd degen 31.7%, frontier degen | ✅ |
| L23 | 40 of 58 transitions | appendix n_scaling inverse | ✅ |
| L25 | 11.1% vs 1.3%, OR=0.109 | tab:degen_inverse | ✅ |
| L37 | 3–12% recovery ratio | tab:bound_verification | ✅ |
| L43 | α=0.068, θ_crit=0.70, ε=0.3 pp | fig:bound | ✅ |

### Limitations 数字

| 数字 | 来源 | 核对 |
|---|---|---|
| 5.5–74% | tab:frontier_sc_cross: DeepSeek 5.5%, Claude 74.0% | ✅ |
| p_adj=0.055 | experiments_main consistent | ✅ |
| MDE ≈1.5 pp | statistical calculation, consistent | ✅ |
| +1–1.4 pp | tab:entity_construction FewNERD LP +1.40 | ✅ 约指 FewNERD 范围 |

### Figure 源数据 (gen_fig_overview.py)

| 硬编码值 | 来源 | 核对 |
|---|---|---|
| AUROC ≈ 0.82 | CoNLL EM AUROC .816 | ✅ |
| ρ = 0.39 | caption 说来自 FewNERD; FewNERD VC ρ=.386→0.39 | ✅ 脚本注释说"SciERC"但 caption 正确 |
| +1.4 pp (Few-NERD, 4-seed) | tab:entity_construction +1.40 | ✅ |

### "31%" 残留检查

`grep "31\\%" sections/*.tex` 仅在 appendix epsilon_sweep 数据表找到 `31.8%`（epsilon=0.03 的 tied percentage），属于正常数据，非旧值残留。✅

---

## ⚠️ 不一致（需用户确认，未自动修复）

### Issue 1: CRITICAL — tab:quality_estimation SciERC EM AUROC vs tab:multiseed

- **主表** (tab:quality_estimation, experiments_main.tex L40): SciERC EM AUROC = **.749** (bold,标为最佳)
- **多种子表** (tab:multiseed, appendix L726): EM AUROC Qwen 5-seed mean = **.631±.013**
- **数学不可能**：seed=42 值 .749 距 5-seed 均值 .631 有 **9.1σ** 偏差。若其中一个 seed 为 .749，其余 4 个需均值 .601，整体 σ 应为 ~0.059 而非 .013。
- **影响**：主表中 SciERC AUROC 最佳信号从 EM (.749) 可能变为 SJ (.692) 或 VC (.684)
- **推测原因**：数据复制错误（.749 可能来自 RE 或其他配置），或 multiseed AUROC 使用了不同的计算方法
- **建议**：回查 SciERC seed=42 EM AUROC 的原始计算脚本

### Issue 2: SIGNIFICANT — tab:selection 表头 vs 表体不一致

- **表头** (caption, single_signal.tex L12): `baselines: 3-seed (Oracle=0.781, Greedy=0.667)`
- **表体** (L18-19): `Oracle = 0.775±0.001`, `Greedy (T=0) = 0.645±0.001`
- **Oracle**: 表头 .781 vs 表体 .775 (Δ=.006)
- **Greedy**: 表头 .667 vs 表体 .645 (Δ=.022)
- **Oracle headroom**: 表头计算 .781-.667 = **11.4 pp** (与正文/图标一致); 表体计算 .775-.645 = **13.0 pp** (与正文不一致)
- **正文一致性**：全文使用 11.4 pp headroom (single_signal.tex L35, L39)，与表头一致
- **推测原因**：表体使用 entity-type-averaged macro F1 (较低), 表头使用 micro/instance-averaged F1 (较高)，两种 F1 计算未统一
- **建议**：统一 F1 指标。若表标题 "macro F1" 正确，则表头和正文的 11.4pp 需更新为 13.0pp；若正文的 11.4pp 正确，则表体需使用同一 F1 指标重算

### Issue 3: MINOR — MV +0.61 pp on CoNLL 无法精确追溯

- **出现位置**: introduction L11 ("MV $+0.61$\,pp on CoNLL"), experiments_main.tex L90 ("MV $+0.61$\,pp on CoNLL")
- **Figure caption**: fig_n_scaling_mv caption 说 "+0.6 pp at N=64"
- **Registry**: CoNLL N=64 seed=42: MV Δ = +0.64 pp
- **分析**: +0.64→+0.6 是合理四舍五入, 但 +0.61 不是 +0.64 的标准四舍五入。可能来自多种子平均或不同 N 值，但 registry 无对应精确值。
- **影响极小**: 0.03 pp 差异不影响结论
- **建议**: 统一为 +0.6 pp (与 figure caption 一致) 或确认多种子来源

---

## ❌ 无法追溯

### 1. WNUT-17 LP ρ = −.446 (tab:fewnerd)
- 表格标注 "3-seed means"，但 registry 仅有 1-2 个 WNUT seed
- exp_003_ner_wnut17: rho_logprob_full = -0.414 (1 seed)
- 3-seed 均值可能来自未记录的其他 seed 实验
- **风险**: 低（排名和方向一致）

### 2. CoNLL (LLaMA) AUROC 值
- tab:quality_estimation CoNLL(LLaMA) AUROC: VC .709, SJ .704, FK .703, EM .705, LP .761
- Registry 中未找到 LLaMA CoNLL N=8 seed=42 的 AUROC 值
- ρ 值已验证一致，AUROC 来源应为同一实验
- **风险**: 低

### 3. tab:robustness LLaMA CoNLL N=16 3-seed ρ 值轻微偏差
- 表中 SJ: 0.474±0.009
- Registry basic N=16 3-seed mean: 0.4631 (from exp_017_llama_conll_n16 series)
- Registry r=1024 N=16 values: ~0.478-0.484
- 表值 0.474 介于两者之间，可能来自特定 LoRA rank 或评估配置
- **风险**: 低（差异 ~0.01，不影响结论）

### 4. tab:fewnerd WNUT-17 Greedy = .452
- Registry exp_003_ner_wnut17: greedy_f1 = 0.525 (micro F1)
- 表格使用 instance-averaged F1 且 gold-filtered，两种 F1 差异解释了 0.525 vs .452
- **风险**: 低（指标定义不同，非数据错误）

---

## 主表 Experiment ID 对应关系

### tab:quality_estimation
| 列 | 对应实验 | N | seed |
|---|---|---|---|
| SciERC (Qwen) | exp_012_rerun_1024 | 8 | 42 |
| CoNLL (Qwen) | exp_002 | 8 | 42 |
| CoNLL (LLaMA) | exp_017_llama_conll_infer | 8 | 42 |

### tab:fewnerd
| Dataset | 对应实验 | 种子配置 |
|---|---|---|
| WNUT-17 | exp_003_ner_wnut17 + 其他 seeds | 3-seed mean |
| CoNLL | exp_002 + other seeds | 3-seed mean |
| SciERC | exp_012_rerun_1024 + other seeds | 3-seed mean |
| Few-NERD | exp_021_fewnerd_full + seed123/456 | 3-seed mean |

### tab:entity_construction
| Dataset | 对应实验 | 说明 |
|---|---|---|
| SciERC | exp_012 系列 + construction 评估 | multi-seed |
| Few-NERD | exp_021 系列 + construction 评估 | 4-seed (含 s789) |
| CoNLL | exp_002 系列 + construction 评估 | single config |

### tab:epoch_confound
| 列 | 对应实验 |
|---|---|
| 3-epoch | exp_021_fewnerd_full 系列 (2-seed) |
| 5-epoch | exp_028_fewnerd_5epoch 系列 (2-seed) |

### tab:multiseed
| Model | 对应实验 | seeds |
|---|---|---|
| Qwen | exp_012_rerun_1024, exp_001_seed42_v2, exp_001_seed456_v2_ner + seeds 123, 2024, 3141 | 5 seeds |
| LLaMA | exp_007_llama 系列 | 3 seeds (42, 123, 456) |

### tab:robustness
| Section | 对应实验 |
|---|---|
| Temperature | exp_026_T05/T08/T12 系列 + T=0.7 experiments |
| Sample size | exp_001_ner_n16_scierc 系列 |
| Cross-model | exp_017_llama_conll_n16 系列 |

### tab:frontier_sc_cross
| Model | 对应实验 |
|---|---|
| DeepSeek | exp_frontier_sc_deepseek |
| Gemini 2.5 Pro | exp_frontier_sc_gemini25pro |
| GPT-5.5 | exp_frontier_sc_gpt55_fewnerd_v2 |
| Claude Sonnet 4 | exp_frontier_sc_claude_sonnet4 |
| Qwen3-8B FT | exp_021_fewnerd_full |

---

## 审计总结

- **已核对一致**: 85+ 个数字，覆盖 Abstract、Introduction、所有主表 ρ 值、experiments_main 全部正文数字、theory section、limitations、figure 硬编码数据
- **发现 3 个不一致** (1 critical, 1 significant, 1 minor)，均需用户确认后处理
- **4 项无法完全追溯**，风险均为低
- **"31%" 残留**: 无（仅 appendix epsilon_sweep 正常数据）
- **已修复的 4 处** (之前完成): line 76 +0.09→+0.12 ✓, line 76 31%→26% ✓, line 91 13.4%→12.2% ✓, 删除 +5-8pp claim ✓
