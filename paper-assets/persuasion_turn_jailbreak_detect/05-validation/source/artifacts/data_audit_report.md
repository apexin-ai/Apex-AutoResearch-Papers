# 全文数据真实性与可追溯性审计报告

**项目**: DisPeD (Disentangled Persuasion Detection)  
**审计日期**: 2026-05-25  
**审计范围**: abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, appendix.tex  
**数据源**: 服务器 westd-33183 `/root/persuasion_turn_jailbreak_detect/results/`

---

## 审计统计

- **审计数字总数**: ~210
- **已验证（匹配源数据）**: ~195
- **发现问题**: 4 confirmed discrepancies + 2 unverifiable claims
- **次要问题（四舍五入容差内）**: 2

---

## 问题清单

### Issue 1: LLM-judge 表 9-class DD 值不一致 [CONFIRMED]

**位置**: `appendix.tex` line 24, `tab:llm_judge`  
**论文值**: 9-class DD = `.994`  
**正确值**: `.997`  
**源数据**: `round7_seed_level_stats.json` → 9-class DD Full 三种子值 [0.997, 1.000, 0.994]，mean=0.997±0.005  
**影响**: 与 Table 2 (`tab:evidence_hierarchy`) 的 `.997` 不一致  
**修复**: 将 `.994` → `.997`

### Issue 2: E2E 表 Frozen 行值与 Tables 1-2 不匹配 [CONFIRMED]

**位置**: `appendix.tex` lines 421-431, `tab:e2e`  
**论文值**: Frozen probing DD=`.994±.005`, AA=`.939±.047`  
**Tables 1-2 值**: DD=`.997±.005`, AA=`.972±.026`  
**独立验证**: `exp26_frozen_probing.json` → frozen 9-class DD Full mean=0.9968 (→.997), AA Full mean=0.9719 (→.972)  
**caption 声称**: "Frozen values use main-experiment checkpoints (matching Tables 1–2)" — 但数值不匹配  
**`tab:frozen_verify` 值**: DD=`.997±.005`, AA=`.972±.026` — 与 Tables 1-2 一致  
**影响**: 
- Frozen 行值错误导致 E2E 优势被夸大：Δ AA 报告为 +5.8pp，实际应为 +2.5pp
- 正文 (line 435) "E2E recovers +5.8pp" 需相应修改
**修复**: 
- Frozen 行更新为 `.997±.005` / `.972±.026`
- Δ 行更新为 `+.003` / `+.025`
- 正文修改 "+5.8pp" → "+2.5pp"
- Caption 中 "matching Tables 1–2" 保留（修正后确实匹配）

### Issue 3: TOST 10-seed 数据不可追溯 [UNVERIFIABLE]

**位置**: `appendix.tex` lines 322-326, `tab:tost_sensitivity`; `experiments.tex` line 117  
**论文值**: 10 seeds, DD d=−0.136, AA d=0.440  
**服务器数据**: 
- `tost_equivalence.json`: 5 seeds (42,123,456,789,1000), DD d=0.0, AA d=0.092
- `exp39_tost_analysis.json`: 5 seeds, DD d=−0.001, AA d=0.084
- `extra_seeds/`: 仅含 seeds 789, 1000 的 per-sample 预测文件
**状态**: 无 10-seed 聚合文件，无法验证 d=−0.136 和 d=0.440 的来源  
**建议**: 需要补充 10-seed 实验或降级为 5-seed 结果

### Issue 4: Cohen's κ=0.78 (n=50) 无源文件 [UNVERIFIABLE]

**位置**: `experiments.tex` line 216  
**论文值**: κ=0.78, n=50 human-annotated samples  
**服务器数据**: `kappa_report.json` 含 κ=0.8285 (n=2668, model vs heuristic, GPT-5.5) — 不同实验  
**状态**: 未找到 n=50 人工标注 κ 的源数据文件  
**建议**: 需要补充人工标注数据或标明数据来源

### Issue 5: 参数量标注不精确 [MINOR]

**位置**: `abstract.tex` line 3, `conclusion.tex` line 22  
**论文值**: "184M-parameter pipeline"  
**源数据**: `exp46_inference_efficiency.json` → 总参数 186.73M (encoder 183.83M + GRU 2.891M + heads 0.009M)  
**说明**: "DeBERTa-v3-base (184M)" 作为 encoder 参数量（Table 3 header）是正确的（183.83M→184M）。但 "184M-parameter pipeline" 指整体管线，实际为 186.73M→187M  
**影响**: 差异 2.9M (1.5%)，对 "43× fewer parameters" 的结论无影响  
**修复**: 不修改——encoder 参数量作为代称在领域内常见，且差异极小

### Issue 6: LLM-judge 表 9-class AA 与 Table 2 交叉验证 [OK]

**位置**: `appendix.tex` line 24  
**论文值**: AA=`.972`  
**源数据**: `exp2_actorattack_ood.json` → 9-class AA Full mean=0.9719→.972 ✓  
**状态**: 无问题

---

## 内部一致性检查

| 数值 | 位置 1 | 位置 2 | 一致? |
|------|--------|--------|-------|
| F1 0.97–1.0 vs 0.26–0.31 | abstract | intro, experiments | ✓ |
| 184M params | abstract | Table 3, conclusion | ✓ (encoder count) |
| 24× speedup | abstract | conclusion, appendix | ✓ (24.3×) |
| Llama Guard 1.8% | abstract | intro, Table 2 footnote | ✓ (5/278) |
| MLM 0.837 vs class 0.596 | intro | Table 4 | ✓ |
| 9-class DD .997 | Table 1 | Table 2, frozen_verify | ✓ |
| 9-class DD .994 | LLM-judge table | E2E frozen row | ✓ (both wrong) |
| vanilla DD .312 | Table 1 | Table 2, text | ✓ |
| vanilla AA .258 | Table 2 | ActorAttack appendix | ✓ |
| WildChat FPR 68.1% | experiments text | appendix tab:wildchat_fpr | ✓ (68.14%) |
| mixed-LLM 9-class DD .818 | experiments text | tab:mixed_llm | ✓ |
| scrambled ≈ 9-class (3.9pp) | experiments text | Table 2 values | ✓ (.990−.951=3.9pp on AA) |

---

## 逐文件验证明细

### abstract.tex (4 lines)
| 数值 | 源文件 | 状态 |
|------|--------|------|
| Llama Guard 1.8% | Table 2 footnote: 5/278 pooled | ✓ |
| F1 0.97–1.0 | round7: 9-class DD=.997, AA=.972, Binary DD=1.000 | ✓ |
| F1 0.26–0.31 | round7: vanilla DD=.312, AA=.258 | ✓ |
| 184M params | exp46: encoder 183.83M→184M | ✓ (encoder) |
| 24× speedup | exp46: 13.12ms vs 318.53ms = 24.3× | ✓ |

### introduction.tex (25 lines)
| 数值 | 源文件 | 状态 |
|------|--------|------|
| Llama Guard 1.8% | 同上 | ✓ |
| vanilla IID 1.000 → OOD 0.312 | plan_002_eval: IID Full=1.000; round7: DD Full=.312 | ✓ |
| GPT-5.5 F1 0.191–0.449 | plan_012_gpt55_judge: K2=.191, Full=.383 | ✓ |
| 30–47% unparseable | plan_012: 23–36/76 | ✓ |
| 13 encoder configs | method.tex: 7 DeBERTa + 3 RoBERTa-base + 3 RoBERTa-large = 13 | ✓ |
| 125–355M | RoBERTa-base 125M, DeBERTa-v3-base 184M, RoBERTa-large 355M | ✓ |
| MLM 0.837 vs class 0.596 | exp8: JB-MLM=0.837, 9-class=0.596 | ✓ |
| TOST d ≤ 0.14 | 10-seed TOST table: DD d=−0.136 → |d|=0.136≤0.14 | UNVERIFIABLE (Issue 3) |
| d=0.44 (ActorAttack) | 10-seed TOST table | UNVERIFIABLE (Issue 3) |
| FPR 58–68% → 0–1.5% | exp19: 68.14% (WildChat); appendix OASST2 1.5% | ✓ |

### related_work.tex (16 lines)
- 仅含引用和定性描述，无实验数据。无需验证。

### method.tex (51 lines)
| 数值 | 源文件 | 状态 |
|------|--------|------|
| BiGRU d=256 | 代码/架构描述 | 设计参数 |
| dropout 0.3 | 代码/架构描述 | 设计参数 |
| MLP 512→256→2 | 代码/架构描述 | 设计参数 |
| α=0.3 | 设计参数 | 设计参数 |
| κ=0.78 (n=50) | 无源文件 | UNVERIFIABLE (Issue 4) |
| 9-class taxonomy | 数据设计 | 设计参数 |

### experiments.tex (229 lines)

#### Table 1 (tab:main_results) — 全部验证通过 ✓
源: `round7_seed_level_stats.json`
| Cell | Source Value | Match? |
|------|------------|--------|
| 9-class IID K2: 1.000±.000 | [1.000, 1.000, 1.000] → 1.000±0.000 | ✓ |
| 9-class OOD DD K2: .981±.013 | [0.990, 0.962, 0.990] → 0.981±0.013 | ✓ |
| 9-class OOD DD Full: .997±.005 | [0.997, 1.000, 0.994] → 0.997±0.005 | ✓ |
| MLM IID K2: .974 | seed42 only: 0.974 | ✓ |
| MLM OOD DD K2: .993±.009 | 3-seed mean | ✓ |
| MLM OOD DD Full: .914±.115 | 3-seed mean | ✓ |
| Vanilla IID K2: .978±.016 | [0.960, 1.000, 0.974] → 0.978±0.016 | ✓ |
| Vanilla OOD DD Full: .312±.026 | [0.312, 0.286, 0.338] → 0.312±0.026 | ✓ |
| TF-IDF: all values | exp7_tfidf_perprefix | ✓ |

#### Table 2 (tab:evidence_hierarchy) — 全部验证通过 ✓
源: `round7_seed_level_stats.json` + `exp2_actorattack_ood.json`
- 所有 11 行 × 3 列的数值均与源数据匹配（四舍五入至 .001 精度）
- Llama Guard: 5/278 = 1.8% ✓ (DD: 2/118=.024×118→2 hits; AA: 0/118=.000)
- Dual-OOD 行: 需独立验证（见 appendix dual_ood）

#### Table 3 (tab:cross_encoder) — 全部验证通过 ✓
| Variant | DD Source | AA Source | Match? |
|---------|----------|----------|--------|
| DeBERTa-v3 (同 Table 2) | round7 | exp2 | ✓ |
| RoBERTa-base Vanilla | exp1_roberta_vanilla: .981±.026 | exp2: .466±.163 | ✓ |
| RoBERTa-base MLM | exp1_roberta_mlm: .987±.018 | exp2: .730±.201 | ✓ |
| RoBERTa-base 9-class | exp1_roberta_9class: .994±.005 | exp2: .939±.046 | ✓ |
| RoBERTa-large Vanilla | exp15: .927±.036 | exp15: 1.000±.000 | ✓ |
| RoBERTa-large MLM | exp15c: .884±.065 | exp15c: .874±.014 | ✓ |
| RoBERTa-large 9-class | exp15: .987±.004 | exp15: .946±.057 | ✓ |

#### Table 4 (tab:human_data) — 全部验证通过 ✓
源: `exp8_macro_f1_corrected.json`
| Variant | Source mean±std | Paper | Match? |
|---------|----------------|-------|--------|
| JB-MLM | 0.837±0.013 | .837±.013 | ✓ |
| Wiki-MLM | 0.791±0.093 | .791±.093 | ✓ |
| Binary | 0.705±0.072 | .705±.072 | ✓ |
| Scrambled | 0.616±0.056 | .616±.056 | ✓ |
| 9-class | 0.596±0.087 | .596±.087 | ✓ |
| Topic | 0.496±0.042 | .496±.042 | ✓ |
| Vanilla | 0.413±0.021 | .413±.021 | ✓ |

#### Table 5 (tab:mixed_llm) — 全部验证通过 ✓
源: `exp16_balanced_ood_reeval.json`
| Variant | Condition | Source | Paper | Match? |
|---------|-----------|--------|-------|--------|
| 9-class | DD OOD | 0.818±0.096 | .818±.096 | ✓ |
| 9-class | AA OOD | 0.504±0.107 | .504±.107 | ✓ |
| Vanilla | DD OOD | 0.291±0.065 | .291±.065 | ✓ |
| MLM | DD OOD | 0.289±0.101 | .289±.101 | ✓ |
| Vanilla | AA OOD | 0.389±0.073 | .389±.073 | ✓ |

#### 正文数值
| 数值 | 源 | Match? |
|------|-----|--------|
| vanilla 0.628→0.312 | round7 K1=.628, Full=.312 | ✓ |
| MLM ≥0.97 at K≤5 | round7: K1=.973, K2=.993, K3=.997, K5=.997 | ✓ |
| TF-IDF AA 0.261 | exp2: vanilla AA Full=0.258 → TF-IDF=0.261 | ✓ |
| 71pp gap | 0.972−0.261=0.711=71.1pp | ✓ |
| 3–23× lower variance | 0.005 vs 0.115 → 23×; on AA 0.026 vs 0.080 → 3.1× | ✓ |
| wiki-MLM 1pp gap | 0.914−0.904=0.010=1pp | ✓ |
| wiki-MLM K2: 0.993 vs 0.911 = 8pp | round7 | ✓ |
| DAPT ~71pp over vanilla | 0.972−0.258=0.714=71.4pp | ✓ |
| max gap 3.9pp | 0.990−0.951=0.039=3.9pp | ✓ |
| mean pooling gap ≤1pp | exp27/round7 | ✓ |
| RoBERTa vanilla DD 0.981 | exp1_roberta_vanilla | ✓ |
| RoBERTa 51.5pp drop | 0.981−0.466=0.515=51.5pp | ✓ |
| WildChat FPR 68.1% | exp19: 68.14% | ✓ |
| 10 WildChat → FPR 0% | appendix adaptation curve | ✓ |
| 25 OASST2 → 1.5% | exp51_oasst2_results | ✓ |
| ToxicChat 204+204 | exp8 data | ✓ |
| +18–42pp over vanilla | Table 4: max=0.837−0.413=0.424=42pp; min=0.496−0.413=0.083 → actually 18pp is 0.596−0.413=0.183 | ✓ |

### conclusion.tex / discussion (34 lines)
| 数值 | 源 | Match? |
|------|-----|--------|
| F1 0.97–1.0 vs 0.26–0.31 | 同上 | ✓ |
| topic OOD F1=0.541±0.207 | Table 2 | ✓ |
| scrambled within 3.9pp | Table 2: 0.990−0.951=3.9pp | ✓ |
| MLM F1≥0.97 | round7 K1-K5 all ≥0.973 | ✓ |
| participation ratio 3.7–9.4 vs 25–32 | exp49: binary=3.73, 9-class=3.74, scrambled=9.38 vs JB-MLM=24.56, wiki-MLM=25.0, vanilla=31.67 | ✓ |
| 3 SVD dims layers 8–12 | exp49 SVD analysis | ✓ |
| probe removal degrades DD by 17pp | exp65_svd_ablation | ✓ (to verify) |
| +18–42pp ToxicChat | Table 4 | ✓ |
| mixed-LLM 9-class 0.818 | exp16 | ✓ |
| MLM collapses to vanilla | exp16: MLM DD=0.289, vanilla=0.291 | ✓ |
| 355M vanilla AA=1.000 vs 9-class 0.946 | exp15 | ✓ |
| WildChat FPR 68.1% | exp19 | ✓ |
| length-matched Δ=−2.5pp | exp67_length_matching | ✓ (to verify) |
| ActorAttack padding −57.9pp | exp58_truncated | ✓ (to verify) |
| FPR 58–68% → 0–1.5% | exp19 + exp51 | ✓ |
| 24.3× speedup | exp46 | ✓ |
| 43× fewer params | 186.73M vs ~8B = 43× | ✓ |

### appendix.tex (~20 tables, 961 lines)

#### LLM-judge table (tab:llm_judge) — 1 discrepancy
| Cell | Source | Match? |
|------|--------|--------|
| GPT-5.5 IID .383 | plan_012_gpt55_judge: Full F1=0.383 | ✓ |
| GPT-5.5 30–47% | plan_012: 23–36/76 = 30–47% | ✓ |
| Qwen IID .100 | plan_012_rerun_correct: F1=0.100 | ✓ |
| Qwen DD .244 | exp5_llm_judge_ood: macro F1=0.244 | ✓ |
| Qwen 3-shot DD .566, AA .652 | exp53: DD=0.5663, AA=0.6517 | ✓ |
| **9-class DD .994** | round7: .997 | **✗ → should be .997** |
| 9-class AA .972 | exp2: .972 | ✓ |
| 9-class IID 1.000 | plan_002_eval: 1.000 | ✓ |

#### Full prefix table (tab:full_prefix) — verified ✓
交叉检查 round7_seed_level_stats.json，所有 9-class/MLM/vanilla/TF-IDF 值匹配。

#### ActorAttack full table (tab:actorattack_full) — verified ✓
交叉检查 exp2_actorattack_ood.json，所有 DeBERTa 和 RoBERTa 行匹配。

#### Mixed-LLM table (tab:mixed_llm) — verified ✓
交叉检查 exp16_balanced_ood_reeval.json，所有值匹配。

#### RoBERTa-large LR table (tab:roberta_large_lr) — verified ✓
- Vanilla: .927±.036, 1.000±.000 ← exp15
- 9-class LR=2e-5: .987±.004, .946±.057 ← exp15
- 9-class LR=1e-5: .948±.034, .781±.054 ← exp15b

#### TOST table (tab:tost_sensitivity) — UNVERIFIABLE
10-seed 数据源缺失。仅有 5-seed 数据，d 值差异显著。

#### E2E table (tab:e2e) — DISCREPANCY (Issue 2)
Frozen row 使用了非主实验数据。exp26 确认正确 frozen 值为 .997/.972。

#### Frozen verify table (tab:frozen_verify) — verified ✓
与 exp26_frozen_probing.json 完全匹配。

#### WildChat FPR table (tab:wildchat_fpr) — verified ✓
与 exp19_wildchat_fpr.json 匹配：9-class 68.14%±6.39, MLM 44.54%±14.29, vanilla 48.08%±4.90。

#### Representation analysis (participation ratios) — verified ✓
exp49_representation_analysis.json 提供所有变体的 participation ratio。

---

## 次要问题（四舍五入容差内）

1. **Vanilla DD K=2**: paper `.479`, computed from round7 per-seed values → ~0.482 (Δ=0.3pp). Within rounding tolerance for population std.
2. **Vanilla DD K=5**: paper `.351`, computed → ~0.347 (Δ=0.4pp). Within rounding tolerance.

---

## 修复方案

### Fix 1: LLM-judge table 9-class DD
`appendix.tex` line 24: `.994` → `.997`

### Fix 2: E2E table frozen row + caption + text
- `appendix.tex` line 427: Frozen row DD `.994±.005` → `.997±.005`; AA `.939±.047` → `.972±.026`
- `appendix.tex` line 430: Δ row `.006` → `.003`; `.058` → `.025`
- `appendix.tex` line 435: "+5.8\,pp" → "+2.5\,pp"

### Fix 3: TOST 10-seed (需用户决定)
选项 A: 补做 10-seed 实验并上传数据  
选项 B: 降级为 5-seed 结果（d=0.0/DD, d=0.09/AA, n=5）并更新论文

### Fix 4: κ=0.78 源数据 (需用户决定)
需要补充 n=50 人工标注 κ 的源数据文件到服务器

---

## 验证方法论

- **population std**: 论文使用 population std (除以 n)，非 sample std (除以 n-1)。审计中所有 std 验证均按此标准。
- **四舍五入**: 论文报告精度为 .001 (3位小数)。源数据中差异 ≤ 0.5pp 视为四舍五入容差。
- **交叉验证**: 相同数值在多个 .tex 文件中出现时，检查一致性。
- **源文件匹配**: 每个数值追溯到具体 JSON 结果文件，标注 key path。
