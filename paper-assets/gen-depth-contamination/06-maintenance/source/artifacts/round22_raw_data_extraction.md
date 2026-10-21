# Round 22 审稿修复原始数据提取

提取日期: 2026-05-20
数据来源: cqa1-22115:/root/autodl-tmp/gen-depth-contamination/

---

## T4: Permutation Test 精确 p-values

所有 p-value 来自 label permutation test (n_permutation=10000, 除 exp_14b_c4 使用 n_permutation=1000)。
`perm_p = 0.0001` 对应 0/10000 permutations 超过观测值, 即 p = 1/(10000+1) ≈ 0.0001。

### 主要 configs 的完整逐对 p-value

**exp016 (Qwen-1.5B base, C4)** — boundary: 1v2
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9870 | 0.0001 |
| 1v2 | 0.6260 | 0.0001 |
| 2v3 | 0.5496 | 0.0001 |
| 3v4 | 0.5293 | 0.0001 |
| 4v5 | 0.5181 | 0.0016 |

**exp018 (LLaMA-3.1-8B, C4)** — boundary: 1v2
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9224 | 0.0001 |
| 1v2 | 0.6123 | 0.0001 |
| 2v3 | 0.5273 | 0.0001 |
| 3v4 | 0.5168 | 0.0037 |
| 4v5 | 0.5159 | 0.0035 |

**exp019 (Mistral-7B-Instruct, C4)** — boundary: 1v2 (K*_CI=1, borderline)
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9842 | 0.0001 |
| 1v2 | 0.5934 | 0.0001 |
| 2v3 | 0.5402 | 0.0001 |
| 3v4 | 0.5233 | 0.0003 |
| 4v5 | 0.5180 | 0.0014 |

**exp024 (Qwen-1.5B arXiv)** — boundary: 2v3 (K*=3)
| Pair | AUC | perm_p | p_vs_θ |
|------|-----|--------|--------|
| 0v1 | 0.9946 | 0.0001 | 0.0 |
| 1v2 | 0.8580 | 0.0001 | 0.0 |
| 2v3 | 0.6427 | 0.0001 | 0.0 |
| 3v4 | 0.5437 | 0.0001 | 1.0 |
| 4v5 | 0.5294 | 0.0006 | 1.0 |

**exp025 (Pythia-1.4B arXiv)** — boundary: 2v3 (K*=3)
| Pair | AUC | perm_p | p_vs_θ |
|------|-----|--------|--------|
| 0v1 | 0.9876 | 0.0001 | 0.0 |
| 1v2 | 0.8047 | 0.0001 | 0.0 |
| 2v3 | 0.6544 | 0.0001 | 0.0 |
| 3v4 | 0.5500 | 0.0001 | 1.0 |
| 4v5 | 0.5284 | 0.0010 | 1.0 |

**exp_gemma2b (Gemma-2-2B, C4)** — boundary: 1v2
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9530 | 0.0001 |
| 1v2 | 0.5981 | 0.0001 |
| 2v3 | 0.5340 | 0.0001 |
| 3v4 | 0.5033 | 0.2919 |
| 4v5 | 0.5025 | 0.3418 |

**exp027 retrain-chain (Pythia, C4)** — boundary: 3v4 (K*=4)
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9847 | 0.0001 |
| 1v2 | 0.9482 | 0.0001 |
| 2v3 | 0.8885 | 0.0001 |
| 3v4 | 0.7977 | 0.0001 |

**exp_008_retrain_chain (v2, bootstrap_ci_v2)** — boundary: 3v4 (K*=4)
| Pair | AUC | perm_p | p_vs_θ |
|------|-----|--------|--------|
| 0v1 | 0.9842 | 0.0001 | 0.0 |
| 1v2 | 0.9471 | 0.0001 | 0.0 |
| 2v3 | 0.8888 | 0.0001 | 0.0 |
| 3v4 | 0.7994 | 0.0001 | 0.0 |

**exp_14b_c4 (Qwen-14B, C4)** — boundary: 1v2, n_perm=1000
| Pair | AUC | p_value |
|------|-----|---------|
| 0v1 | 0.9598 | 0.0 (0/1000) |
| 1v2 | 0.6210 | 0.0 (0/1000) |
| 2v3 | 0.5494 | 0.0 (0/1000) |
| 3v4 | 0.5243 | 0.0 (0/1000) |
| 4v5 | 0.5154 | 0.0 (0/1000) |

### Cross-scorer configs (arXiv, scorer=Pythia-1.4B)

**Qwen-7B crossscorer** (K*=2)
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9573 | 0.0001 |
| 1v2 | 0.8163 | 0.0001 |
| 2v3 | 0.5986 | 0.0001 |
| 3v4 | 0.5413 | 0.0001 |
| 4v5 | 0.5191 | 0.0166 |

**Mistral-7B crossscorer** (K*=2)
| Pair | AUC | perm_p |
|------|-----|--------|
| 0v1 | 0.9798 | 0.0001 |
| 1v2 | 0.8138 | 0.0001 |
| 2v3 | 0.6075 | 0.0001 |
| 3v4 | 0.5489 | 0.0001 |
| 4v5 | 0.5389 | 0.0001 |

**LLaMA-8B crossscorer** (K*=2)
| Pair | AUC | perm_p |
|------|-----|--------|
| 2v3 | 0.6201 | 0.0001 |
| 3v4 | 0.5228 | 0.0060 |
| 4v5 | 0.5247 | 0.0034 |

### Retrain-chain permutation_test.json (独立格式, p_value不同编码)

**exp_008_retrain_chain (Pythia)**
| Pair | AUC | p_value |
|------|-----|---------|
| 0v1 | 0.9968 | 0.0 |
| 1v2 | 0.9855 | 0.0 |
| 2v3 | 0.9556 | 0.0 |
| 3v4 | 0.9029 | 0.304 |

**exp_olmo_retrain_chain (OLMo)**
| Pair | AUC | p_value |
|------|-----|---------|
| 0v1 | 0.9988 | 0.0 |
| 1v2 | 0.9610 | 0.0 |
| 2v3 | 0.8919 | 0.998 |
| 3v4 | 0.8762 | 1.0 |

### Borderline 10K 比较

| Config | Pair | AUC | perm_p_10k |
|--------|------|-----|------------|
| LLaMA-3.1-8B (exp_018) | 1v2 | 0.6075 | 0.0001 |
| Gemma-2-2B | 1v2 | 0.5981 | 0.0001 |
| Mistral-7B (exp_019) | 1v2 | 0.5902 | 0.0001 |
| 512-tok (exp_021) | 1v2 | 0.6136 | 0.0001 |

---

## T3: PELT Changepoint 完整配对数据 (37 configs)

| Config | K*_OBD | K*_PELT | Agree |
|--------|--------|---------|-------|
| exp_008_retrain_chain | 4 | 4 | ✓ |
| exp_018_llama8b | 2 | 1 | ✗ |
| exp_021_length_128 | 2 | 1 | ✗ |
| exp_021_length_256 | 2 | 1 | ✗ |
| exp_021_length_512 | 2 | 1 | ✗ |
| exp_023_wiki | 2 | 1 | ✗ |
| exp_024_arxiv | 3 | 2 | ✗ |
| exp_025_pythia_arxiv | 3 | 2 | ✗ |
| exp_027_latex_ablation | 3 | 2 | ✗ |
| exp_14b_c4 | 2 | 1 | ✗ |
| exp_arXiv_llama8b | 3 | 2 | ✗ |
| exp_arXiv_llama8b_crossscorer | 3 | 2 | ✗ |
| exp_arXiv_mistral7b | 3 | 2 | ✗ |
| exp_arXiv_mistral7b_crossscorer | 3 | 2 | ✗ |
| exp_arXiv_olmo | 1 | 1 | ✓ |
| exp_arXiv_qwen1b5_crossscorer | 3 | 2 | ✗ |
| exp_arXiv_qwen7b | 3 | 2 | ✗ |
| exp_arXiv_qwen7b_crossscorer | 2 | 2 | ✓ |
| exp_code_llama8b | 2 | 2 | ✓ |
| exp_code_mistral7b | 2 | 1 | ✗ |
| exp_code_pythia1b4 | 1 | 1 | ✓ |
| exp_code_qwen1b5 | 2 | 2 | ✓ |
| exp_code_qwen1b5_pythia_scorer | 2 | 2 | ✓ |
| exp_code_qwen7b | 2 | 2 | ✓ |
| exp_pythia_retrain_depth7 | 7 | 4 | ✗ |
| exp_qwen_retrain_chain | 4 | 4 | ✓ |
| exp_qwen_retrain_chain_ext | 7 | 2 | ✗ |
| exp_wiki_llama8b | 1 | 1 | ✓ |
| exp_wiki_mistral7b | 1 | 1 | ✓ |
| exp_wiki_olmo | 1 | 1 | ✓ |
| exp_wiki_olmo_v2 | 1 | 1 | ✓ |
| exp_wiki_pythia | 2 | 1 | ✗ |
| exp_wiki_pythia_v2 | 1 | 1 | ✓ |
| exp_wiki_qwen7b | 2 | 1 | ✗ |
| exp_wiki_scorer_confound | 1 | 1 | ✓ |
| exp_wiki_scorer_confound_1b5 | 1 | 1 | ✓ |
| olmo_c4_cont | 1 | 1 | ✓ |

**汇总**: 37 configs, 18 agree (48.6%), 19 disagree (51.4%)
- K*_OBD = K*_PELT 时 agree: 当两者都为 1 (14 cases) 或都为 2 (5 cases) 或都为 4 (2 cases)
- 不一致模式: K*_OBD 系统性偏高 (PELT 总是 ≤ OBD), 差 1 的有 15 cases, 差 ≥2 的有 4 cases

---

## T2: Fold-level AUC 数据 (1v2 和 2v3)

### 核心 configs 的 5-fold AUC

**C4 domain:**

| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |
|--------|------|------|-----|-----|-----|-----|-----|
| exp016 (Qwen-1.5B) | 1v2 | 0.6262 | 0.5963 | 0.6362 | 0.6366 | 0.6337 | 0.6282 |
| exp016 (Qwen-1.5B) | 2v3 | 0.5496 | 0.5516 | 0.5456 | 0.5403 | 0.5605 | 0.5501 |
| exp018 (LLaMA-8B) | 1v2 | 0.6123 | 0.6362 | 0.6072 | 0.5975 | 0.6067 | 0.6140 |
| exp018 (LLaMA-8B) | 2v3 | 0.5274 | 0.5345 | 0.5442 | 0.5342 | 0.5141 | 0.5101 |
| exp019 (Mistral-7B) | 1v2 | 0.5935 | 0.5981 | 0.5894 | 0.5962 | 0.5850 | 0.5988 |
| exp019 (Mistral-7B) | 2v3 | 0.5402 | 0.5308 | 0.5340 | 0.5493 | 0.5584 | 0.5286 |
| exp_gemma2b | 1v2 | 0.5981 | 0.6010 | 0.5841 | 0.6006 | 0.5966 | 0.6082 |
| exp_gemma2b | 2v3 | 0.5342 | 0.5598 | 0.5246 | 0.5338 | 0.5241 | 0.5286 |
| exp_14b_c4 (Qwen-14B) | 1v2 | 0.6211 | 0.6252 | 0.6112 | 0.6153 | 0.6323 | 0.6214 |
| exp_14b_c4 (Qwen-14B) | 2v3 | 0.5494 | 0.5362 | 0.5529 | 0.5590 | 0.5445 | 0.5546 |
| olmo_c4_cont | 1v2 | 0.5070 | 0.5083 | 0.4946 | 0.4953 | 0.5170 | 0.5195 |
| olmo_c4_cont | 2v3 | 0.5042 | 0.5106 | 0.4896 | 0.5140 | 0.4977 | 0.5093 |

**arXiv domain:**

| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |
|--------|------|------|-----|-----|-----|-----|-----|
| exp024 (Qwen-1.5B) | 1v2 | 0.8581 | 0.8763 | 0.8669 | 0.8411 | 0.8515 | 0.8549 |
| exp024 (Qwen-1.5B) | 2v3 | 0.6436 | 0.6738 | 0.6349 | 0.6479 | 0.6537 | 0.6078 |
| exp025 (Pythia-1.4B) | 1v2 | 0.8047 | 0.7906 | 0.8278 | 0.8018 | 0.8065 | 0.7967 |
| exp025 (Pythia-1.4B) | 2v3 | 0.6545 | 0.6409 | 0.6433 | 0.6764 | 0.6548 | 0.6572 |
| exp027_latex_ablation | 1v2 | 0.8297 | 0.8085 | 0.8529 | 0.8198 | 0.8292 | 0.8381 |
| exp027_latex_ablation | 2v3 | 0.6229 | 0.6429 | 0.6196 | 0.6258 | 0.5986 | 0.6275 |

**Wiki domain:**

| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |
|--------|------|------|-----|-----|-----|-----|-----|
| exp023 (Qwen-1.5B) | 1v2 | 0.6193 | 0.6152 | 0.6161 | 0.6189 | 0.6112 | 0.6352 |
| exp023 (Qwen-1.5B) | 2v3 | 0.5498 | 0.5473 | 0.5559 | 0.5378 | 0.5637 | 0.5442 |
| exp_wiki_pythia_v2 | 1v2 | 0.5846 | 0.5826 | 0.5783 | 0.5842 | 0.5864 | 0.5913 |
| exp_wiki_qwen7b | 1v2 | 0.6108 | 0.6135 | 0.6085 | 0.6031 | 0.6016 | 0.6272 |
| exp_wiki_scorer_confound | 1v2 | 0.5870 | 0.5850 | 0.5825 | 0.5877 | 0.5766 | 0.6030 |

**Retrain-chain configs:**

| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |
|--------|------|------|-----|-----|-----|-----|-----|
| exp008 retrain (v2) | 1v2 | 0.9472 | 0.9520 | 0.9444 | 0.9558 | 0.9401 | 0.9437 |
| exp008 retrain (v2) | 2v3 | 0.8891 | 0.8794 | 0.8828 | 0.8998 | 0.8986 | 0.8848 |
| exp008 retrain (v2) | 3v4 | 0.7996 | 0.8020 | 0.7975 | 0.8036 | 0.7898 | 0.8050 |

**Cross-scorer configs (arXiv, scorer=Pythia-1.4B):**

| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |
|--------|------|------|-----|-----|-----|-----|-----|
| Qwen-7B crossscorer | 1v2 | 0.8171 | 0.7892 | 0.8093 | 0.8265 | 0.8236 | 0.8372 |
| Qwen-7B crossscorer | 2v3 | 0.5989 | 0.5920 | 0.6006 | 0.6108 | 0.5768 | 0.6142 |
| Mistral-7B crossscorer | 1v2 | 0.8141 | 0.7874 | 0.8256 | 0.8225 | 0.8223 | 0.8125 |
| Mistral-7B crossscorer | 2v3 | 0.6075 | 0.6052 | 0.5803 | 0.6210 | 0.6113 | 0.6195 |
| LLaMA-8B crossscorer | 2v3 | 0.6201 | 0.6306 | 0.6115 | 0.6073 | 0.6136 | 0.6377 |

**Length ablation:**

| Config | Pair | Mean | F1 | F2 | F3 | F4 | F5 |
|--------|------|------|-----|-----|-----|-----|-----|
| 128-tok | 1v2 | 0.6219 | 0.6405 | 0.6269 | 0.6191 | 0.6117 | 0.6112 |
| 256-tok | 1v2 | 0.6282 | 0.6335 | 0.6173 | 0.6231 | 0.6244 | 0.6425 |
| 512-tok | 1v2 | 0.6073 | 0.6184 | 0.5979 | 0.5952 | 0.6118 | 0.6134 |

---

## T6: Generator Identity AUC

### 结论: 无独立的 "generator identity classification AUC" 指标

multi_source 实验测量的是将 generator ID 作为第 16 个特征加入 depth classifier 后的 AUC 变化, 而非 generator identity 本身的分类性能。

### 所有 multi-source 实验的 Δ(with_label - no_label)

**C4 domain (v1: Qwen-1.5B + Pythia-1.4B + OLMo-1B)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.9929 | 0.9948 | +0.0019 |
| 1v2 | 0.7007 | 0.7015 | +0.0008 |
| K* | 2 | 2 | unchanged |

**C4 domain (v2: Qwen-1.5B + Pythia-1.4B + LLaMA-8B)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.9680 | 0.9785 | +0.0105 |
| 1v2 | 0.7144 | 0.7250 | +0.0106 |
| K* | 2 | 2 | unchanged |

**arXiv domain (vocab-only, Qwen-1.5B + Pythia-1.4B + LLaMA-8B)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.9431 | 0.9436 | +0.0005 |
| 1v2 | 0.6922 | 0.7020 | +0.0098 |
| 2v3 | 0.5890 | 0.5883 | -0.0007 |
| K* | 2 | 2 | unchanged |

**arXiv domain (unified scorer, same generators)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.9899 | 0.9911 | +0.0012 |
| 1v2 | 0.8117 | 0.8338 | +0.0221 |
| 2v3 | 0.6247 | 0.6276 | +0.0029 |
| K* | 3 | 3 | unchanged |

**Wiki domain (vocab-only, Qwen-1.5B + LLaMA-8B + Mistral-7B)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.7616 | 0.7779 | +0.0163 |
| 1v2 | 0.5434 | 0.5520 | +0.0086 |
| K* | 1 | 1 | unchanged |

**Wiki domain (unified scorer)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.9603 | 0.9685 | +0.0082 |
| 1v2 | 0.5685 | 0.5790 | +0.0105 |
| K* | 1 | 1 | unchanged |

**Code domain (vocab-only, Qwen-7B + LLaMA-8B + Mistral-7B)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.7891 | 0.7900 | +0.0009 |
| 1v2 | 0.6353 | 0.6440 | +0.0087 |
| K* | 2 | 2 | unchanged |

**Code domain (unified scorer)**
| Pair | AUC_no_label | AUC_with_label | Δ |
|------|-------------|----------------|-------|
| 0v1 | 0.9123 | 0.9123 | +0.0000 |
| 1v2 | 0.6702 | 0.6803 | +0.0101 |
| K* | 2 | 2 | unchanged |

### 关键结论
- **Generator identity 对 depth detection 的增益可忽略**: 平均 Δ(1v2) ≈ +0.01 AUC
- **K* 从未因加入 generator label 而改变**
- 最大 Δ 出现在 arXiv unified scorer 1v2 (+0.0221), 但仍不改变 K*
- **不存在独立的 generator identity classification AUC** — 实验设计中没有将 "识别 generator" 作为目标任务

---

## 数据文件索引

| 数据类型 | 文件路径 |
|---------|---------|
| Permutation test (retrain) | results/exp_008_retrain_chain/permutation_test.json |
| Permutation test (OLMo retrain) | results/exp_olmo_retrain_chain/permutation_test.json |
| Bootstrap CI (含 perm_p) | artifacts/exp016_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | artifacts/exp018_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | artifacts/exp019_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | artifacts/exp024_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | artifacts/exp025_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | artifacts/exp027_retrain_bootstrap.json |
| Bootstrap CI (含 perm_p) | artifacts/exp_gemma2b_depth_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | artifacts/crossscorer_bootstrap_ci.json |
| Bootstrap CI (含 perm_p) | results/exp_14b_c4/bootstrap_ci_results.json |
| Bootstrap CI v2 | results/exp_008_retrain_chain/bootstrap_ci_v2.json |
| Borderline 10K comparison | results/exp_bootstrap_10k/bootstrap_10k_comparison.json |
| Borderline bootstrap | artifacts/borderline_bootstrap_ci.json |
| PELT changepoint | results/exp_changepoint_kstar/changepoint_results.json |
| PELT bootstrap comparison | results/exp_changepoint_kstar/bootstrap_comparison.json |
| Multi-source v1 (C4) | results/exp_multi_source_detection/multi_source_results.json |
| Multi-source v2 (C4) | results/exp_multi_source_detection_v2/multi_source_results.json |
| Multi-source arXiv | results/exp_multi_source_arxiv/results.json |
| Multi-source Wiki | results/exp_wiki_multi_source/results.json |
| Multi-source Code | results/exp_code_multi_source/results.json |
| Fold AUC (per config) | results/*/pairwise_auc.json, results_*/pairwise_auc.json |
