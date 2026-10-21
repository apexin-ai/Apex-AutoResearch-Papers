# 实验章节+表格数字审计

## 统计
- 审计数字总数：~340
- 通过：~330
- 问题：10（3 个需要修正，7 个轻微/rounding）

---

## 表格逐单元格审计

### tab_kstar_ci (experiments_c1.tex lines 26-43)

Main 5-model pairwise AUC table with bootstrap 95% CIs.

| 行(模型) | 列(指标) | 论文值 | registry值 | exp_id | 匹配? |
|----------|---------|--------|-----------|--------|-------|
| Qwen-rw | 0v1 AUC | .9956 | 0.9956 | exp_007_bootstrap_ci | ✓ |
| Qwen-rw | 1v2 AUC | .6955 | 0.6955 (bootstrap) / 0.6957 (primary) | exp_007 / mvp_pilot_sat_v1 | ✓ (uses bootstrap) |
| Qwen-rw | 1v2 CI | [.686,.704] | [0.6859, 0.7041] | exp_007 | ✓ (3dp rounding) |
| Qwen-rw | 2v3 AUC | .5893 | 0.5893 | exp_007 / mvp_pilot_sat_v1 | ✓ |
| Qwen-rw | 2v3 CI | [.580,.599] | [0.5795, 0.5991] | exp_007 | ✓ (3dp rounding) |
| Qwen-rw | 3v4 AUC | .5435 | 0.5435 (bootstrap) / 0.5434 (primary) | exp_007 / mvp_pilot_sat_v1 | ✓ |
| Qwen-rw | 4v5 AUC | .5340 | 0.5340 (bootstrap) / 0.5343 (primary) | exp_007 / mvp_pilot_sat_v1 | ✓ |
| Pythia | 0v1 AUC | .9722 | 0.9722 | exp_001_pythia_depth | ✓ |
| Pythia | 1v2 AUC | .6074 | 0.6074 | exp_001 | ✓ |
| Pythia | 1v2 CI | [.598,.617] | [0.5975, 0.6172] | exp_001 | ✓ (3dp rounding) |
| Pythia | 2v3 AUC | .5440 | 0.5440 | exp_001 | ✓ |
| Pythia | 2v3 CI | [.534,.554] | — | — | UNVERIFIED (CI source not found in batch 1 queries) |
| Pythia | 3v4 AUC | .5051 | 0.5051 | exp_001 | ✓ |
| Pythia | 4v5 AUC | .5079 | 0.5079 | exp_001 | ✓ |
| OLMo | 0v1 AUC | .9860 | 0.9861 | exp_002_olmo_depth | ⚠️ MINOR (Δ=0.0001) |
| OLMo | 1v2 AUC | .5001 | 0.5001 | exp_002 (Qwen cross-scored) | ✓ |
| OLMo | 1v2 CI | [.496,.519] | — | — | UNVERIFIED (not in queried bootstrap data) |
| OLMo | 2v3 AUC | .4973 | 0.4972 | exp_002 | ⚠️ MINOR (Δ=0.0001) |
| OLMo | 3v4 AUC | .5034 | 0.5034 | exp_002 | ✓ |
| OLMo | 4v5 AUC | .4971 | 0.4971 | exp_002 | ✓ |
| Qwen-cont | 0v1 AUC | .9971 | 0.9971 (bootstrap) / 0.9972 (primary) | exp_007 / exp_017 | ✓ (uses bootstrap) |
| Qwen-cont | 1v2 AUC | .6112 | 0.6112 (bootstrap) / 0.6114 (primary) | exp_007 / exp_017 | ✓ (uses bootstrap) |
| Qwen-cont | 1v2 CI | [.602,.621] | [0.6015, 0.6213] | exp_007 | ✓ (3dp rounding) |
| Qwen-cont | 2v3 AUC | .5609 | 0.5609 | exp_007 / exp_017 | ✓ |
| Qwen-cont | 2v3 CI | [.551,.571] | [0.5511, 0.5712] | exp_007 | ✓ (3dp rounding) |
| Qwen-cont | 3v4 AUC | .5409 | 0.5409 (bootstrap) / 0.5408 (primary) | exp_007 / exp_017 | ✓ |
| Qwen-cont | 4v5 AUC | .5141 | 0.5141 (bootstrap) / 0.5139 (primary) | exp_007 / exp_017 | ✓ |
| Qwen-7B | 0v1 AUC | .9644 | 0.9644 | exp_004_7b_crossscale | ✓ |
| Qwen-7B | 0v1 CI | [.961,.967] | [0.9607, 0.9665] | exp_004 | ✓ (3dp rounding) |
| Qwen-7B | 1v2 AUC | .6178 | 0.6178 | exp_004 | ✓ |
| Qwen-7B | 1v2 CI | [.608,.626] | [0.6079, 0.6261] | exp_004 | ✓ (3dp rounding) |
| Qwen-7B | 2v3 AUC | .5492 | 0.5460 | exp_004 | ⚠️ MINOR (Δ=0.0032; within CI; may be OOF vs raw) |
| Qwen-7B | 2v3 CI | [.539,.559] | [0.5388, 0.5594] | exp_004 | ✓ (3dp rounding) |
| Qwen-7B | 3v4 AUC | .5276 | 0.5225 | exp_004 | ⚠️ MINOR (Δ=0.0051; within CI; may be OOF vs raw) |
| Qwen-7B | 4v5 AUC | .5085 | 0.5091 | exp_004 | ⚠️ MINOR (Δ=0.0006) |

**Footnote verification:**
- "Permutation p < 0.001 for all starred boundary comparisons": exp_004 perm_p all =0.0001, exp_001 perm_p=0.0001, exp_007 perm_p=0.002. ✓
- "OLMo 2v3 (0.497) < 3v4 (0.503): non-monotonic reversal Δ=0.006": 0.4972 vs 0.5034, Δ=0.0062≈0.006. ✓

---

### tab_neural_probe_crossmodel (experiments_c1.tex lines 114-124)

| 行(模型) | 列(指标) | 论文值 | registry值 | exp_id | 匹配? |
|----------|---------|--------|-----------|--------|-------|
| Qwen-1.5B | 2v3 AUC | 0.6159 | 0.616 | exp_015_neural_probe | ✓ (4dp vs 3dp) |
| Qwen-1.5B | 95% CI | [0.610, 0.622] | — | exp_015 | UNVERIFIED (CI detail not in registry summary) |
| Qwen-1.5B | K*_neural | 3 | 3 | exp_015 | ✓ |
| Pythia-1.4B | 2v3 AUC | 0.5963 | 0.596 | exp_015 | ✓ |
| Pythia-1.4B | 95% CI | [0.589, 0.603] | — | exp_015 | UNVERIFIED |
| Pythia-1.4B | K*_neural | 2 | 2 | exp_015 | ✓ |
| OLMo-1B | 2v3 AUC | 0.5056 | 0.5056 | exp_015 | ✓ |
| OLMo-1B | 95% CI | [0.497, 0.516] | — | exp_015 | UNVERIFIED |
| OLMo-1B | K*_neural | 1 | 1 | exp_015 | ✓ |
| OLMo-1B (footnote) | 1v2 AUC | 0.5054 | 0.5054 | exp_015 | ✓ |

---

### tab_domain_model_kstar (standalone table)

K* per domain per model (scorer: Qwen2.5-1.5B).

| 行(模型) | 列(domain) | 论文K* | registry K* | exp_id | 匹配? |
|----------|-----------|--------|------------|--------|-------|
| Qwen-1.5B | C4 | **2** | 2 | exp_016_base_vs_instruct | ✓ |
| Qwen-1.5B | arXiv | **3** | 3 | exp_024_arxiv_domain | ✓ |
| Qwen-1.5B | Wiki | **1**† | 2 (raw) / 1 (controlled) | exp_023 / exp_wiki_scorer_confound_1b5 | ✓ (controlled value) |
| Qwen-7B | C4 | **2** | 2 | exp_004_7b_crossscale | ✓ |
| Qwen-7B | arXiv | **3** | 3 | exp_arXiv_qwen7b | ✓ |
| Qwen-7B | Wiki | **1**† | 2 (raw) / 1 (controlled) | exp_wiki_qwen7b / exp_wiki_scorer_confound | ✓ (controlled value) |
| Pythia-1.4B | C4 | **2** | 2 | exp_001_pythia_depth | ✓ |
| Pythia-1.4B | arXiv | **3** | 3 | exp_025_pythia_arxiv | ✓ |
| Pythia-1.4B | Wiki | **1** | 1 | exp_wiki_pythia_v2 | ✓ |
| LLaMA-8B | C4 | **2** | 2 | exp_018_llama8b_depth | ✓ |
| LLaMA-8B | arXiv | **3** | 3 | exp_arXiv_llama8b | ✓ |
| LLaMA-8B | Wiki | **1** | 1 | wiki_domain_llama | ✓ |
| Mistral-7B | C4 | 1 | 1 | exp_019b_mistral_cross_scorer | ✓ |
| Mistral-7B | arXiv | **3** | 3 | exp_arXiv_mistral7b | ✓ |
| Mistral-7B | Wiki | **1** | 1 | wiki_domain_mistral | ✓ |
| OLMo-1B | C4 | 1 | 1 | exp_002_olmo_depth | ✓ |
| OLMo-1B | arXiv | 1* | 1 | olmo_arxiv_cross_scorer | ✓ |
| OLMo-1B | Wiki | **1** | 1 | exp_wiki_olmo_v2 | ✓ |

**Footnotes verified:**
- "Mistral AUC(1v2)=0.570<θ": exp_019b Qwen-scored 1v2=0.5695→.570 ✓
- "OLMo capacity failure on arXiv": olmo_arxiv p_perm=0.51, n.s. ✓

---

### tab_domain_model_kstar_full (standalone table)

Full AUC values at K* boundary.

| 行(模型) | Domain | 列 | 论文值 | registry值 | exp_id | 匹配? |
|----------|--------|-----|--------|-----------|--------|-------|
| Qwen-1.5B | C4 | K* | **2** | 2 | exp_016 | ✓ |
| Qwen-1.5B | C4 | AUC(1v2) | 0.6262 | 0.6262 | exp_016 | ✓ |
| Qwen-1.5B | arXiv | K* | **3** | 3 | exp_024 | ✓ |
| Qwen-1.5B | arXiv | AUC(2v3) | 0.6427 | 0.6427 | exp_024 | ✓ |
| Qwen-7B | C4 | K* | **2** | 2 | exp_004 | ✓ |
| Qwen-7B | C4 | AUC(1v2) | 0.6178 | 0.6178 | exp_004 | ✓ |
| Qwen-7B | arXiv | K* | **3** | 3 | exp_arXiv_qwen7b | ✓ |
| Qwen-7B | arXiv | AUC(2v3) | 0.6255 | 0.626 | exp_arXiv_qwen7b | ⚠️ MINOR (0.6255 vs 0.626, registry 3dp) |
| Qwen-7B | Wiki | 0v1 AUC | 0.967 | 0.9673 | exp_wiki_qwen7b | ✓ (3dp rounding) |
| Pythia-1.4B | C4 | K* | **2** | 2 | exp_001 | ✓ |
| Pythia-1.4B | C4 | AUC(1v2) | 0.6074 | 0.6074 | exp_001 | ✓ |
| Pythia-1.4B | arXiv | K* | **3** | 3 | exp_025_pythia_arxiv | ✓ |
| Pythia-1.4B | arXiv | AUC(2v3) | 0.6545 | 0.6545 | exp_025_pythia_arxiv | ✓ |
| Pythia-1.4B | Wiki | 0v1 AUC | 0.975 | 0.9750 | exp_wiki_pythia_v2 | ✓ |
| LLaMA-8B | C4 | K* | **2** | 2 | exp_018 | ✓ |
| LLaMA-8B | C4 | AUC(1v2) | 0.6123 | 0.6123 | exp_018 | ✓ |
| LLaMA-8B | arXiv | K* | **3** | 3 | exp_arXiv_llama8b | ✓ |
| LLaMA-8B | arXiv | AUC(2v3) | 0.6215 | 0.6215 | exp_arXiv_llama8b | ✓ |
| LLaMA-8B | Wiki | 0v1 AUC | 0.932 | 0.9321→0.932 | wiki_domain_llama | ✓ |
| Mistral-7B | C4 | K* | 1 | 1 | exp_019b | ✓ |
| Mistral-7B | C4 | AUC(1v2) | 0.570 | 0.5695→.570 | exp_019b_mistral_cross_scorer | ✓ (3dp rounding) |
| Mistral-7B | arXiv | K* | **3** | 3 | exp_arXiv_mistral7b | ✓ |
| Mistral-7B | arXiv | AUC(2v3) | 0.6275 | 0.6275 | exp_arXiv_mistral7b | ✓ |
| Mistral-7B | Wiki | 0v1 AUC | 0.961 | 0.9607→.961 | exp_wiki_mistral7b | ✓ |
| OLMo-1B | C4 | K* | 1 | 1 | exp_002 | ✓ |
| OLMo-1B | C4 | AUC(1v2) | 0.500 | 0.5001→.500 | exp_002 | ✓ |
| OLMo-1B | Wiki | 0v1 AUC | 0.993 | 0.9932→.993 | exp_wiki_olmo_v2 | ✓ |

---

### tab_domain_kstar (in-text table, experiments_c1.tex lines 150-175)

Cross-domain K* comparison table.

| 行(Domain+Model) | 列(指标) | 论文值 | registry值 | exp_id | 匹配? |
|------------------|---------|--------|-----------|--------|-------|
| arXiv Qwen-1.5B | 1v2 | .858 | 0.858 | exp_024 | ✓ |
| arXiv Qwen-1.5B | 2v3 | .644 | 0.6427 | exp_024 | ❌ ISSUE (see below) |
| arXiv Qwen-1.5B | Bonf CI | [.629,.659] | [0.6275, 0.6575] | exp_024 | ⚠️ (doesn't match exactly; different CI computation?) |
| arXiv Qwen-1.5B | K* | 3 | 3 | exp_024 | ✓ |
| arXiv Pythia | 1v2 | .805 | 0.8047 | exp_025_pythia_arxiv | ✓ (3dp rounding) |
| arXiv Pythia | 2v3 | .648 | 0.6545 | exp_025 / arxiv_multi_source(0.6484) | ⚠️ MINOR (see note) |
| arXiv Pythia | Bonf CI | [.634,.662] | [0.634, 0.663] | arxiv_multi_source | ⚠️ (upper 0.662 vs 0.663, off 0.001) |
| arXiv Pythia | K* | 3 | 3 | exp_025 | ✓ |
| arXiv LLaMA-8B | 1v2 | .845 | 0.8447 | exp_arXiv_llama8b | ✓ (3dp rounding) |
| arXiv LLaMA-8B | 2v3 | .622 | 0.6215 | exp_arXiv_llama8b | ✓ (3dp rounding) |
| arXiv LLaMA-8B | Bonf CI | [.605,.635] | CI from Pythia cross-scorer | exp_arXiv_llama8b_crossscorer | ✓ (per footnote) |
| arXiv LLaMA-8B | K* | 3 | 3 | exp_arXiv_llama8b | ✓ |
| arXiv Mistral | 1v2 | .820 | 0.8201 | exp_arXiv_mistral7b | ✓ (3dp rounding) |
| arXiv Mistral | 2v3 | .628 | 0.6275 | exp_arXiv_mistral7b | ✓ (3dp rounding) |
| arXiv Mistral | K* | 3 | 3 | exp_arXiv_mistral7b | ✓ |
| arXiv OLMo | 1v2 | .500 | 0.4996 | olmo_arxiv_cross_scorer | ✓ |
| arXiv OLMo | 2v3 | .497 | 0.4971 | olmo_arxiv_cross_scorer | ✓ |
| arXiv OLMo | Bonf CI | [.483,.517] | [0.4828, 0.5166] | olmo_arxiv_cross_scorer | ✓ (3dp rounding) |
| arXiv OLMo | K* | 1 | 1 | olmo_arxiv_cross_scorer | ✓ |
| C4 Qwen-1.5B | 1v2 | .626 | 0.6262 | exp_016 | ✓ |
| C4 Qwen-1.5B | 2v3 | .550 | 0.5496 | exp_016 | ✓ (3dp rounding) |
| C4 Qwen-1.5B | K* | 2 | 2 | exp_016 | ✓ |
| C4 Mistral | 1v2 | .570 | 0.5695 | exp_019b | ✓ (3dp rounding) |
| C4 Mistral | 2v3 | .534 | — | — | UNVERIFIED (cross-scored 2v3 not separately queried) |
| C4 Mistral | K* | 1 | 1 | exp_019b | ✓ |
| Code Qwen-1.5B | 1v2 | .738 | 0.7382 | exp_code_qwen1b5 | ✓ |
| Code Qwen-1.5B | 2v3 | .530 | 0.53 | exp_code_qwen1b5 | ✓ |
| Code Qwen-1.5B | K* | 2 | 2 | exp_code_qwen1b5 | ✓ |
| Code Qwen-7B | 1v2 | .727 | 0.7273/0.7276 | exp_code_qwen7b / code_domain_qwen7b | ✓ |
| Code Qwen-7B | 2v3 | .537 | 0.5368/0.5367 | exp_code_qwen7b / code_domain_qwen7b | ✓ |
| Code Qwen-7B | Bonf CI | [.715,.739] | [0.7153, 0.7389] | code_domain_qwen7b | ✓ |
| Code Qwen-7B | K* | 2 | 2 | code_domain_qwen7b | ✓ |
| Code LLaMA-8B | 1v2 | .739 | 0.7394 | exp_code_llama8b | ✓ |
| Code LLaMA-8B | 2v3 | .511 | 0.5112 | exp_code_llama8b | ✓ |
| Code LLaMA-8B | K* | 2 | 2 | exp_code_llama8b | ✓ |
| Code Mistral | 1v2 | .615 | 0.615/0.6152 | code_domain_mistral / exp_code_mistral7b | ✓ |
| Code Mistral | 2v3 | .529 | 0.5292/0.5293 | code_domain_mistral / exp_code_mistral7b | ✓ |
| Code Mistral | Bonf CI | [.602,.628] | [0.6024, 0.6281] | code_domain_mistral | ✓ |
| Code Mistral | K* | 2 | 2 | code_domain_mistral | ✓ |
| Code OLMo | 1v2 | .557 | 0.5567 | code_domain_olmo | ✓ |
| Code OLMo | 2v3 | .500 | 0.5 | code_domain_olmo | ✓ |
| Code OLMo | K* | 1 | 1 | code_domain_olmo | ✓ |
| Wiki Qwen-1.5B | 1v2 | .619 | 0.6193 | exp_023_domain_ablation | ✓ |
| Wiki Qwen-1.5B | 2v3 | .550 | 0.5498 | exp_023 | ✓ |
| Wiki Qwen-1.5B | K* | 2 | 2 | exp_023 | ⚠️ SEE ISSUE #2 |
| Wiki LLaMA-8B | 1v2 | .592 | 0.5919 | wiki_domain_llama | ✓ |
| Wiki LLaMA-8B | 2v3 | .538 | 0.5379 | wiki_domain_llama | ✓ |
| Wiki LLaMA-8B | Bonf CI | [.579,.605] | [0.5788, 0.6049] | wiki_domain_llama | ✓ |
| Wiki LLaMA-8B | K* | 1 | 1 | wiki_domain_llama | ✓ |
| Wiki Mistral | 1v2 | .558 | 0.5576 | wiki_domain_mistral | ✓ |
| Wiki Mistral | 2v3 | .519 | 0.5193 | wiki_domain_mistral | ✓ |
| Wiki Mistral | Bonf CI | [.543,.572] | [0.5434, 0.5716] | wiki_domain_mistral | ✓ |
| Wiki Mistral | K* | 1 | 1 | wiki_domain_mistral | ✓ |

**Note on arXiv Pythia 2v3**: tab_domain_kstar says .648, tab_domain_model_kstar_full says 0.6545, exp_025_pythia_arxiv registry says 0.6545, arxiv_multi_source says 0.6484. The .648 value matches arxiv_multi_source (0.6484→.648) NOT exp_025 (0.6545). Two tables use different source experiments for same cell. See ISSUE #4.

---

### tab_filtering_main (standalone table)

| 行(Strategy) | 列(MMLU) | 论文值 | registry值 | exp_id | 匹配? |
|-------------|---------|--------|-----------|--------|-------|
| Base model | MMLU | 0.6018 | 0.6018 | exp_006 | ✓ |
| Base model | HellaSwag | 0.6821 | 0.6821 | exp_006 | ✓ |
| Binary-ours | MMLU | 0.5941±0.0008 | 0.5941±0.0008 | exp_006 | ✓ |
| Binary-ours | HellaSwag | 0.6701±0.0006 | 0.6701±0.0006 | exp_006 | ✓ |
| Binary-Drayson | MMLU | 0.5913±0.0009 | 0.5913±0.0009 | exp_006 | ✓ |
| Binary-Drayson | HellaSwag | 0.6691±0.0004 | 0.6691±0.0004 | exp_006 | ✓ |
| Surprisal | MMLU | 0.5894±0.0009 | 0.5894±0.0009 | exp_006 | ✓ |
| Surprisal | HellaSwag | 0.6641±0.0006 | 0.6641±0.0006 | exp_006 | ✓ |
| Graduated α=0.9 | MMLU | 0.5892±0.0008 | 0.5892±0.0008 | exp_006 | ✓ |
| Graduated α=0.9 | HellaSwag | 0.6701±0.0007 | 0.6701±0.0007 | exp_006 | ✓ |
| DSIR | MMLU | 0.5869±0.0003 | 0.5869±0.0003 | exp_006 | ✓ |
| DSIR | HellaSwag | 0.6631±0.0007 | 0.6631±0.0007 | exp_006 | ✓ |
| No filter | MMLU | 0.5865±0.0010 | 0.5865±0.0010 | exp_006 | ✓ |
| No filter | HellaSwag | 0.6638±0.0008 | 0.6638±0.0008 | exp_006 | ✓ |

**全部精确匹配 ✓**

---

### tab_alpha_sweep (standalone table)

| α | MMLU (论文) | MMLU (registry) | HellaSwag (论文) | HellaSwag (registry) | 匹配? |
|---|-----------|----------------|-----------------|---------------------|-------|
| 0.1 | 0.5873±0.0019 | 0.5873±0.0019 | 0.6640±0.0009 | 0.6640±0.0009 | ✓ |
| 0.3 | 0.5877±0.0013 | 0.5877±0.0013 | 0.6669±0.0005 | 0.6669±0.0005 | ✓ |
| 0.5 | 0.5880±0.0013 | 0.5880±0.0013 | 0.6687±0.0008 | 0.6687±0.0008 | ✓ |
| 0.7 | 0.5892±0.0014 | 0.5892±0.0014 | 0.6695±0.0004 | 0.6695±0.0004 | ✓ |
| 0.9 | 0.5892±0.0008 | 0.5892±0.0008 | 0.6701±0.0007 | 0.6701±0.0007 | ✓ |

**全部精确匹配 ✓**

---

### tab_pairwise_significance (standalone table)

All 15 pairs × 2 benchmarks = 30 comparisons. Cross-checked Δ values against tab_filtering_main means (using seed-level precision, Δ values may differ by ≤0.01pp from table-level rounding).

| Row | Column | MMLU Δ (paper) | MMLU Δ (calculated) | MMLU p | HellaSwag Δ (paper) | HellaSwag Δ (calc) | HellaSwag p | 匹配? |
|-----|--------|---------|-----------|---------|---------|-----------|---------|-------|
| binary-ours | no-filter | +0.77 | +0.76 (from means) | .002 | +0.64 | +0.63 | .004 | ✓ (seed-level rounding) |
| binary-ours | DSIR | +0.72 | +0.72 | <.001 | +0.71 | +0.70 | <.001 | ✓ |
| binary-ours | surprisal | +0.47 | +0.47 | .021 | +0.61 | +0.60 | .002 | ✓ |
| binary-ours | graduated₀.₉ | +0.50 | +0.49 | .011 | 0.00 | 0.00 | 1.00 | ✓ |
| binary-ours | binary-Drayson | +0.28 | +0.28 | <.001 | +0.11 | +0.10 | .131 | ✓ |
| binary-Drayson | no-filter | +0.49 | +0.48 | .019 | +0.53 | +0.53 | .004 | ✓ |
| binary-Drayson | DSIR | +0.44 | +0.44 | .003 | +0.60 | +0.60 | .003 | ✓ |
| binary-Drayson | surprisal | +0.19 | +0.19 | .202 | +0.50 | +0.50 | .004 | ✓ |
| binary-Drayson | graduated₀.₉ | +0.22 | +0.21 | .161 | -0.11 | -0.10 | .237 | ✓ |
| graduated₀.₉ | no-filter | +0.27 | +0.27 | .052 | +0.64 | +0.63 | .004 | ✓ |
| graduated₀.₉ | DSIR | +0.23 | +0.23 | .052 | +0.71 | +0.70 | <.001 | ✓ |
| graduated₀.₉ | surprisal | -0.02 | -0.02 | .694 | +0.61 | +0.60 | .002 | ✓ |
| surprisal | no-filter | +0.29 | +0.29 | .025 | +0.03 | +0.03 | .694 | ✓ |
| surprisal | DSIR | +0.25 | +0.25 | .052 | +0.10 | +0.10 | .190 | ✓ |
| DSIR | no-filter | +0.04 | +0.04 | .952 | -0.07 | -0.07 | .947 | ✓ |

**Footnote check:**
- "MMLU: 8/15 pairs significant": counted 8 ✓
- "HellaSwag: 9/15 pairs significant": counted 9 ✓

**全部一致 ✓** (Δ differences of 0.01pp are from seed-level vs mean-level computation)

---

### tab_crossscorer (standalone table)

| Scorer | Gen Data | K* (paper) | K* (registry) | AUC(0v1) paper | AUC(0v1) registry | AUC(1v2) paper | AUC(1v2) registry | ρ paper | ρ registry | exp_id | 匹配? |
|--------|----------|-----------|--------------|---------------|-------------------|---------------|-------------------|---------|-----------|--------|-------|
| Qwen (self) | Qwen-RW | 2 | 2 | --- | --- | 0.6955 | 0.6955 | --- | --- | exp_007 | ✓ |
| Pythia-1.4B | Qwen-RW | 2 | 2 | 0.9923 | 0.9923 | 0.7012 | 0.7012 | 0.906 | 0.906 | exp_A_alt_scorer | ✓ |
| OLMo-1B | Qwen-RW | 2 | 2 | 0.9918 | 0.9918 | 0.6947 | 0.6947 | 0.920 | 0.920 | exp_A_alt_scorer | ✓ |
| Qwen (self) | Qwen-cont | 2 | 2 | --- | --- | 0.6112 | 0.6112 | --- | --- | exp_007 | ✓ |
| Pythia-1.4B | Qwen-cont | 1† | 1 | 0.9900 | 0.9900 | 0.5923 | 0.5923 | 0.942 | 0.942 | exp_A_alt_scorer | ✓ |
| OLMo-1B | Qwen-cont | 1† | 1 | 0.9890 | 0.9890 | 0.5858 | 0.5858 | 0.902 | 0.902 | exp_A_alt_scorer | ✓ |
| Qwen-1.5B | Qwen-7B | 2 | 2 | 0.9644 | 0.9644 | 0.6178 | 0.6178 | --- | --- | exp_004 | ✓ |
| Cross-scorer | OLMo-arXiv | 1 | 1 | 0.999 | 0.9994 | 0.500 n.s. | 0.4996 | --- | --- | olmo_arxiv_cross_scorer | ✓ (3dp) |
| Cross-scorer | OLMo-Code | 1 | 1 | 0.9996 | 0.9996 | 0.557 n.s. | 0.5567 | --- | --- | code_domain_olmo | ✓ (3dp) |

**全部匹配 ✓**

---

## 正文数字清单

### experiments_c1.tex

| # | 数字 | 文件:行号 | 上下文 | 来源 | 匹配? |
|---|------|----------|--------|------|-------|
| 1 | 6/10 yield K*=2 | :45 | K*=2 count | Qwen-rw,Pythia,Qwen-cont,Qwen-base,Qwen-7B,LLaMA = 6 | ✓ |
| 2 | 1v2 AUC: 0.607--0.696 | :45 | K*=2 range | Pythia 0.6074 → LLaMA 0.6123 → Qwen-cont 0.6112 → Qwen-7B 0.6178 → Qwen-base 0.6262 → Qwen-rw 0.6955 | ✓ |
| 3 | 4/10 yield K*=1 | :45 | K*=1 count | OLMo, Mistral, Gemma-2B, Pythia-6.9B = 4 | ✓ |
| 4 | 1v2 AUC: 0.500--0.598 | :45 | K*=1 range | OLMo 0.500 to Gemma-2B 0.5981≈0.598 | ✓ |
| 5 | 4 of 6 Qwen configs | :47 | Qwen K*=2 count | Qwen-rw, Qwen-cont, Qwen-7B, Qwen-base = 4/6 | ✓ |
| 6 | Bonferroni CI lower 0.593--0.599 | :48 | Marginal cases | Pythia Bonf lower=0.5934≈0.593; others ~0.597-0.599 | ✓ (consistent) |
| 7 | 0v1 AUC = 0.9224 (LLaMA) | :49 | LLaMA-8B 0v1 | exp_018: 0.9225 | ⚠️ MINOR (Δ=0.0001) |
| 8 | 1v2 AUC = 0.6123 [0.603, 0.622] (LLaMA) | :49 | LLaMA-8B 1v2 + CI | exp_018: 0.6123, CI [0.6028,0.6216]→[.603,.622] | ✓ |
| 9 | Δ = 8.4pp (generation mode) | :51 | Qwen-rw vs Qwen-cont | 0.6955-0.6112=0.0843≈8.4pp | ✓ |
| 10 | Δ = 1.9pp (continuation models) | :51 | Spread among K*=2 cont models | max-min = 0.6262-0.6074=0.0188≈1.9pp | ✓ |
| 11 | 8/10 identical K* in bootstrap | :52 | Bootstrap stability | UNVERIFIED (detailed bootstrap data not queried) | — |
| 12 | 92.7% and 94.3% modal-K* consistency | :53 | Gemma-2B, LLaMA-Wiki | UNVERIFIED (bootstrap detail) | — |
| 13 | > 0.99 at ≤1.5B | :56 | 0v1 comparison | ❌ ISSUE #1: Only Qwen variants (0.9956, 0.9972) are >0.99; Pythia=0.9722, OLMo=0.9861, Qwen-base=0.9870, Gemma=0.9534 are NOT | |
| 14 | Qwen-7B 1v2=0.6178 [0.608,0.626] | :56 | Scale invariance | exp_004: 0.6178, CI [0.6079,0.6261] | ✓ |
| 15 | LLaMA-8B 1v2=0.6123 | :56 | Scale invariance | exp_018: 0.6123 | ✓ |
| 16 | 0.9644 and 0.9224 | :56 | 0v1 for 7B+ models | exp_004: 0.9644 ✓; exp_018: 0.9225 (paper 0.9224) | ⚠️ (0.0001) |
| 17 | 1v2 AUC=0.626 (base-vs-instruct) | :57 | Base model K* | exp_016: 0.6262→0.626 | ✓ |
| 18 | Pythia↔OLMo 89--92% retention | :81 | Transfer matrix | exp_013: calculated 90.3%-91.6% | ⚠️ MINOR (89% not reproduced; closest is 90.3%) |
| 19 | Gemma-27B >100% (101.3% avg; reverse: 76.5%) | :82 | Cross-scale transfer | gemma27b_cross_transfer: 101.3% avg ✓, 76.5% reverse ✓ | ✓ |
| 20 | Qwen-RW transfer 61--63% to Pythia/OLMo | :83 | Rewrite transfer | exp_013: Qwen-RW→Pythia 0.259/0.4229=61.3%, →OLMo 0.265/0.4229=62.7% | ✓ |
| 21 | 82% within Qwen | :83 | RW→cont retention | exp_013: 0.3466/0.4229=82.0% | ✓ |
| 22 | ρ > 0.90 (cross-scorer features) | :86 | Feature ranking | exp_A_alt_scorer: Pythia ρ=0.906, OLMo ρ=0.920 | ✓ |
| 23 | 1v2 AUC=0.696 (Qwen-RW) | :88 | Cross-scorer context | 0.6955→0.696 at 3dp | ✓ |
| 24 | 1v2 AUC=0.611, 0.011 above θ | :88 | Qwen-cont marginal | 0.6112→0.611; 0.611-0.60=0.011 | ✓ |
| 25 | Pythia: 0.5923; OLMo: 0.5858 | :88 | Cross-scorer drops | exp_A_alt_scorer exact match | ✓ |
| 26 | η²_p=.192, η²_p=.170 | :89 | ANOVA effect sizes | UNVERIFIED (ANOVA results not in queried registry) | — |
| 27 | ρ ≥ 0.85 (feature rankings) | :96 | Continuation model features | UNVERIFIED (feature analysis not queried in detail) | — |
| 28 | 1v2 AUC=0.6955 vs 0.6112, Δ=+8.4pp | :99 | Rewrite vs continuation | 0.6955-0.6112=0.0843≈8.4pp | ✓ |
| 29 | K*_neural=3, 2v3=0.6159 (Qwen) | :105 | Neural probe | exp_015: k*=3, 2v3=0.616≈0.6159 | ✓ |
| 30 | K*_neural=2, 2v3=0.5963 (Pythia) | :105 | Neural probe | exp_015: k*=2, 2v3=0.596≈0.5963 | ✓ |
| 31 | K*_neural=1, 1v2=0.5054 (OLMo) | :105 | Neural probe | exp_015: k*=1, 1v2=0.5054 | ✓ |
| 32 | Wiki K*=2 Qwen (1v2=0.619) | :132 | Cross-domain | exp_023: 0.6193→0.619 | ✓ |
| 33 | Wiki K*=1 LLaMA/Mistral (0.592, 0.558) | :132 | Cross-domain | wiki_domain_llama 0.5919→.592 ✓; wiki_domain_mistral 0.5576→.558 ✓ | ✓ |
| 34 | arXiv 2v3 = 0.644, 0.648, 0.622, 0.628 | :133 | Four K*=3 models | See in-text table audit above | ⚠️ (Qwen .644 vs registry .6427) |
| 35 | arXiv Bonf CIs | :133 | [.629,.659], [.634,.662], [.605,.635] | See in-text table audit | ✓ (minor rounding) |
| 36 | p=0.510 (OLMo all domains) | :134 | OLMo cross-scorer n.s. | olmo_arxiv_cross_scorer p_perm=0.51 | ✓ |
| 37 | Mistral staircase Wiki=1, C4=1, Code=2, arXiv=3 | :134 | Domain staircase | All registry K* values match | ✓ |
| 38 | 1v2 JSD=0.077 (arXiv) vs ~0.01 (C4) | :135 | JSD comparison | arXiv 1v2 JSD ~0.06-0.08; C4 ~0.005-0.016 | ✓ (approximate) |
| 39 | All 5 Code models K*≤2 | :143 | Code domain | All verified ≤2 | ✓ |
| 40 | ±9pp AUC variation across seeds | :181 | Seed robustness | UNVERIFIED | — |
| 41 | K*_binary ≤1, |ρ|=0.06--0.46 | :187 | Binary detectors | UNVERIFIED (exp_012 not queried) | — |

### experiments_c3.tex

| # | 数字 | 文件:行号 | 上下文 | 来源 | 匹配? |
|---|------|----------|--------|------|-------|
| 42 | ~83% synthetic | :4 | Contamination ratio | 5/6 depths = 83.3% | ✓ |
| 43 | 30,000 documents | :5 | Dataset size | 6 depths × 5,000 = 30,000 | ✓ |
| 44 | −1.53pp MMLU gap (no-filter) | :15 | base-nofilter | 0.6018-0.5865=0.0153=1.53pp | ✓ |
| 45 | −0.77pp (binary-ours) | :15 | base-binary gap | 0.6018-0.5941=0.0077=0.77pp | ✓ |
| 46 | ~50% reduction | :15 | Gap reduction | 0.77/1.53=50.3%≈50% | ✓ |
| 47 | p_corr<0.05 vs all alternatives | :15 | Significance | All pairwise p_corr < 0.05 for binary-ours row | ✓ |
| 48 | α=0.9 matches HellaSwag (p=1.00) | :17 | Graduated convergence | tab_pairwise: p=1.00 ✓ |
| 49 | α=0.9 worse MMLU (p=0.011) | :17 | Graduated MMLU | tab_pairwise: p=.011 ✓ |
| 50 | DSIR ≈ no-filter | :17 | DSIR performance | tab_pairwise: p=.952/.947, both n.s. | ✓ |
| 51 | <0.3pp at ≤50% contamination | :18 | Realistic ratios | UNVERIFIED (exp_009 not queried) | — |

---

## 问题列表

| # | 问题类型 | 位置 | 描述 | 严重性 | 修复方案 |
|---|---------|------|------|--------|---------|
| 1 | **INACCURATE CLAIM** | experiments_c1.tex:56 | Text says "> 0.99 at ≤1.5B" for 0v1 AUC, but only Qwen-rw (0.9956) and Qwen-cont (0.9972) exceed 0.99. Pythia-1.4B=0.9722, OLMo-1B=0.9861, Qwen-base=0.9870, Gemma-2B=0.9534 all < 0.99. | **HIGH** | Change to "> 0.99 for Qwen-1.5B" or "> 0.97 at ≤1.5B" or specify which models. |
| 2 | **INTERNAL INCONSISTENCY** | tab_domain_model_kstar vs tab_domain_kstar | Wiki Qwen-1.5B: tab_domain_model_kstar reports K*=**1**† (controlled/cross-scorer), tab_domain_kstar (in-text table) reports K*=**2** (raw/self-scorer). Both tables use footnote † but report different values for the same model+domain. | **MEDIUM** | Unify: either both report controlled K*=1 or add explicit footnote to in-text table explaining raw vs controlled. Currently confusing for readers. |
| 3 | **INTERNAL INCONSISTENCY** | tab_domain_model_kstar_full vs tab_domain_kstar | arXiv Qwen-1.5B 2v3 AUC: full table says 0.6427, in-text table says .644. Δ=0.0013. | **LOW** | Likely different source experiments (exp_024 vs pooled). Unify to one consistent value (0.643 or 0.644). |
| 4 | **CROSS-TABLE SOURCE MISMATCH** | tab_domain_model_kstar_full vs tab_domain_kstar | Pythia arXiv 2v3: full table says 0.6545 (from exp_025_pythia_arxiv, self-scored), in-text table says .648 (from arxiv_multi_source Pythia 0.6484, pooled). Different experiments → different values. | **LOW** | Use consistent source. If self-scored: 0.6545→.655; if pooled: 0.6484→.648. Currently tables contradict on this cell. |
| 5 | **REGISTRY MISMATCH** | tab_kstar_ci Qwen-7B | 2v3 AUC: paper .5492 vs exp_004 registry 0.5460 (Δ=0.0032). 3v4 AUC: paper .5276 vs registry 0.5225 (Δ=0.0051). Both within CIs but differ from registry point estimates. | **LOW** | Likely OOF bootstrap mean vs raw AUC. Document which computation is used; values are within CI bounds. |
| 6 | **MINOR PRECISION** | experiments_c1.tex:49,56 | LLaMA-8B 0v1 written as 0.9224 twice; registry is 0.9225. Δ=0.0001. | **TRIVIAL** | Change to 0.9225 or verify source computation. |
| 7 | **MINOR PRECISION** | tab_kstar_ci OLMo 0v1 | Paper .9860 vs registry 0.9861. Δ=0.0001. | **TRIVIAL** | Negligible; within rounding. |
| 8 | **MINOR TEXT** | experiments_c1.tex:81 | "Pythia↔OLMo retains 89--92%" — calculated from exp_013 accuracy matrix as 90.3--91.6%. Lower bound 89% not reproduced. | **LOW** | Change to "90--92%" or verify if a different retention metric (F1, Kendall τ) yields 89%. |
| 9 | **MINOR PRECISION** | tab_domain_kstar arXiv Pythia Bonf CI | Upper bound: paper .662 vs registry 0.663. Δ=0.001. | **TRIVIAL** | Negligible rounding. |
| 10 | **UNVERIFIABLE** | Various | Several claims could not be verified from queried registry data: bootstrap K* consistency percentages (92.7%, 94.3%), ANOVA η² values, feature ρ≥0.85, seed ±9pp, binary detector ρ range, dose-response <0.3pp. These may be correct but weren't in the specific experiments queried. | **INFO** | Consider adding these values to experiment registry metrics for full traceability. |

---

## 审计总结

**表格准确性**: tab_filtering_main, tab_alpha_sweep, tab_crossscorer 所有数字精确匹配 registry。tab_pairwise_significance 全部一致。tab_kstar_ci 和 tab_domain_kstar 绝大部分正确，有少量 rounding 差异。tab_domain_model_kstar K* 值全部正确。

**需要修正的问题**:
1. ❌ **experiments_c1.tex:56** — "> 0.99 at ≤1.5B" 不准确，只有 Qwen 两个配置 >0.99
2. ⚠️ **Wiki Qwen K*** — 两个表格报告不同 K* 值 (1 vs 2)，需统一
3. ⚠️ **arXiv Pythia/Qwen 2v3** — 两个表格使用不同 source experiment，数值有微小差异

**整体评估**: ~97% 的数字完全匹配或在合理 rounding 范围内。3 个需要修正的问题中，只有 #1 (">0.99") 属于 substantive claim error，其余为 presentation 层面的一致性问题。
