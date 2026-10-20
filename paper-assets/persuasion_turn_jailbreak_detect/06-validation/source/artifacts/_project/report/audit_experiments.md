# Experiments.tex 数字审计报告

**审计日期**: 2026-05-23
**审计文件**: `docs/paper/experiments.tex`
**数据源**: Project registry (`persuasion_turn_jailbreak_detect`, 135 experiments)

---

## 汇总

- **总检查数字**: ~120 个定量声明
- **完全匹配 (✓)**: ~100
- **需修正 (✗)**: 5
- **无法追溯 (N/A)**: 6
- **轻微舍入差异 (~)**: 5

---

## 需修正的问题 (✗)

### 1. 9-class DD-Full F1: 论文 .994±.005 → 实际 .997±.005

| 位置 | 论文值 | Registry 值 | exp_id |
|------|--------|-------------|--------|
| Table 1 L48 | .994±.005 | .997±.005 | plan_006 (s42=1.0), plan_002_seed123 (1.0), plan_002_seed456 (0.9904) |
| Table 2 L90 | .994±.005 | .997±.005 | 同上 |
| Table 3 L156 | .994±.005 | .997±.005 | 同上 |
| L62 inline | 0.994±0.005 | 0.997±0.005 | 同上 |
| L109 hierarchy | 9-class (0.994±0.005) | 0.997±0.005 | 同上 |
| L114 "F1 = 0.994–1.000" | 下界 0.994 | 下界 0.997 | 同上 |

**验证**: 3 seed mean = (1.000 + 1.000 + 0.9904)/3 = **0.9968**; population std = **0.0045** ≈ 0.005。多个独立 registry 条目（exp9_bootstrap_ci mean=0.9968, exp4 clean_full=0.9968, exp35 individual_mean=0.9968）一致确认为 0.997，不是 0.994。

### 2. Scrambled DD-Full F1: 论文 .994±.005 → 实际 .997±.005

| 位置 | 论文值 | Registry 值 | exp_id |
|------|--------|-------------|--------|
| Table 2 L92 | .994±.005 | .997±.005 | exp4 scrambled_3seed.clean_full=0.9968; mf1_scrambled_seed123 (1.0), seed456 (1.0) → seed42≈0.9904 |
| L109 hierarchy | scrambled (0.994±0.005) | 0.997±0.005 | 同上 |

**验证**: exp4_dd_ood_perturbation 的 `scrambled_3seed.clean_full = 0.9968`，与 9-class 完全一致。

### 3. Mean pooling DD-K=2: 论文 1.000 → 实际 0.994±.009 (3-seed)

| 位置 | 论文值 | Registry 值 | exp_id |
|------|--------|-------------|--------|
| Table 2 L94 | 1.000 (无 std) | 0.9936±0.009 | exp13_meanpool_multiseed dd_ood.k2.mean=0.9936, std=0.009 |

**说明**: 论文报告的 1.000 来自 seed42 单种子值（plan_015），但 Table 2 其他行均为 3-seed mean±std。应改为 `.994±.009` 或标注单种子。

### 4. Llama Guard DD-Full: 论文 .025 → 实际 .024

| 位置 | 论文值 | Registry 值 | exp_id |
|------|--------|-------------|--------|
| Table 2 L100 | .025 | 0.0244 | exp40_llama_guard_baseline ood_dd.full.f1_jb=0.0244 |

**说明**: 0.0244 四舍五入到 3 位应为 .024，不是 .025。末位差 1 个单位。

### 5. FITD "all variants F1 ≥ 0.990" 表述不准确

| 位置 | 论文声明 | Registry 数据 | exp_id |
|------|----------|--------------|--------|
| L65 | "all variants F1 ≥ 0.990" | 9class=1.000, jb_mlm=0.990, vanilla=0.994 (exp35) — 仅测试了 3 个 variant | exp35_cross_seed_ensemble |

**说明**: 仅 9-class/MLM/vanilla 三个变体在 FITD 上有数据，且均 ≥ 0.990。但 "all variants" 暗示包括 topic (0.541 on DD)、wiki-MLM 等——这些在 FITD 上无 registry 数据。建议改为 "all tested variants" 或明确列出。

---

## 无法追溯的数字 (N/A)

| 数字 | 位置 | 说明 |
|------|------|------|
| MLM seed 456 recall = 0.64 | L62 | Registry 仅存 F1（seed456 DD Full F1=0.7512），无 per-seed recall breakdown |
| Turn-order shuffling DeBERTa Δ (DD=0.000, AA=−0.009, IID=0.000) | L137 | 无对应 registry experiment |
| Turn-order shuffling RoBERTa-large Δ (DD=+0.001, AA=−0.007, IID=0.000) | L137 | 无对应 registry experiment |
| McNemar p > 0.13 (classification variants) | L114 | Registry 无 McNemar test between 9class/binary/scrambled |
| κ=0.78, n=50 (IID strategy annotation) | L228 | Annotation-derived, 非实验 registry |
| OOD κ=0.126 (strategy prediction) | L228 | Cohen's kappa 非 registry 存储指标 |

---

## 轻微舍入差异 (~) — 可接受

| 数字 | 位置 | 论文值 | Registry 值 | exp_id | 说明 |
|------|------|--------|-------------|--------|------|
| TOST d on DD | L114 | −0.14 | −0.136 | exp41_tost_10seed | 舍入到 2 位 ✓ |
| Bootstrap CI lower (9-class DD) | L65 | 0.943 | 0.9426 | exp9_bootstrap_ci | 舍入 ✓ |
| Bootstrap CI (vanilla DD) | L65 | [0.202, 0.341] | [0.2017, 0.3414] | exp9_bootstrap_ci | 舍入 ✓ |
| DAPT adds "1.3pp" (RoBERTa) | L172 | 1.3pp | 1.23pp (0.9936−0.9813) | exp1_roberta_9class/vanilla | 略高于实际 |
| VRAM 862 MB | appendix | 862 | 861.5 | exp29_inference_efficiency | 舍入 ✓ |

---

## Table 1 完整审计 (L43–56)

| 数字 | 位置 | exp_id | Registry 值 | 一致性 |
|------|------|--------|-------------|--------|
| 9-class IID K=2: 1.000±.000 | L48 | plan_002 3 seeds | 1.000±0.000 | ✓ |
| 9-class IID Full: 1.000±.000 | L48 | plan_002 3 seeds | 1.000±0.000 | ✓ |
| 9-class OOD DD K=2: .981±.013 | L48 | plan_006+seeds | 0.981±0.013 (pop std) | ✓ |
| 9-class OOD DD Full: .994±.005 | L48 | plan_006+seeds | **0.997±0.005** | **✗** |
| MLM IID K=2: .974 | L49 | plan_017 seed42 | 0.9737 | ✓ |
| MLM IID Full: 1.000 | L49 | plan_017 seed42 | 1.000 | ✓ |
| MLM OOD DD K=2: .993±.009 | L49 | plan_017 3-seed | 0.9934±0.0093 | ✓ |
| MLM OOD DD Full: .914±.115 | L49 | plan_017 3-seed | 0.9138±0.115 | ✓ |
| Vanilla IID K=2: .978±.016 | L50 | plan_002 3 seeds | 0.9775±0.0161 | ✓ |
| Vanilla IID Full: 1.000±.000 | L50 | plan_002 3 seeds | 1.000±0.000 | ✓ |
| Vanilla OOD DD K=2: .479±.038 | L50 | vanilla_multiseed_dd_ood | 0.479±0.038 | ✓ |
| Vanilla OOD DD Full: .312±.026 | L50 | vanilla_multiseed_dd_ood | 0.312±0.026 | ✓ |
| TF-IDF IID K=2: 1.000 | L51 | plan_002 | 1.000 | ✓ |
| TF-IDF IID Full: 1.000 | L51 | plan_002 | 1.000 | ✓ |
| TF-IDF OOD DD K=2: 1.000 | L51 | exp7 | 1.000 | ✓ |
| TF-IDF OOD DD Full: .961 | L51 | exp7 | 0.961 | ✓ |

---

## Table 2 完整审计 (L86–104)

| 数字 | 位置 | exp_id | Registry 值 | 一致性 |
|------|------|--------|-------------|--------|
| 9-class DD-Full .994±.005 | L90 | plan_006+seeds | **0.997±0.005** | **✗** |
| 9-class AA-Full .972±.026 | L90 | exp2_actorattack_ood | 0.972±0.026 | ✓ |
| 9-class DD-K=2 .981±.013 | L90 | exp26/plan seeds | 0.981±0.013 | ✓ |
| Binary DD-Full 1.000±.000 | L91 | mf1_binary seeds | 1.000±0.000 | ✓ |
| Binary AA-Full .990±.008 | L91 | exp2 | 0.990±0.008 | ✓ |
| Binary DD-K=2 .994±.009 | L91 | mf1_binary seeds | seed123=1.0, seed456=1.0; seed42 K2 未存储 | N/A |
| Scrambled DD-Full .994±.005 | L92 | exp4 scrambled_3seed | **0.997±0.005** | **✗** |
| Scrambled AA-Full .951±.043 | L92 | exp2 | 0.951±0.043 | ✓ |
| Scrambled DD-K=2 .981±.026 | L92 | mf1_scrambled seeds | seed123=1.0, seed456=1.0; seed42 K2 未存储 | N/A |
| MLM DD-Full .914±.115 | L93 | plan_017 | 0.9138±0.115 | ✓ |
| MLM AA-Full .893±.080 | L93 | exp2 | 0.893±0.080 | ✓ |
| MLM DD-K=2 .993±.009 | L93 | plan_017 | 0.9934±0.0093 | ✓ |
| Mean pool DD-Full .991±.013 | L94 | exp13 | 0.9905±0.0134 | ✓ |
| Mean pool AA-Full .962±.015 | L94 | exp13 | 0.9623±0.0151 | ✓ |
| Mean pool DD-K=2 1.000 | L94 | exp13 | **0.9936±0.009** | **✗** |
| Topic DD-Full .541±.207 | L96 | plan_016v2 | 0.5411±0.2069 | ✓ |
| Topic AA-Full .625±.141 | L96 | exp2 | 0.625±0.141 | ✓ |
| Topic DD-K=2 .593±.166 | L96 | plan_016v2 | 0.5926±0.1655 | ✓ |
| Wiki-MLM DD-Full .904±.115 | L97 | plan_018 | 0.9042±0.1147 | ✓ |
| Wiki-MLM AA-Full .686±.297 | L97 | exp2 | 0.686±0.297 | ✓ |
| Wiki-MLM DD-K=2 .911±.073 | L97 | plan_018 | 0.9112±0.0725 | ✓ |
| Vanilla DD-Full .312±.026 | L98 | vanilla_multiseed | 0.312±0.026 | ✓ |
| Vanilla AA-Full .258±.000 | L98 | exp2 | 0.258±0.000 | ✓ |
| Vanilla DD-K=2 .479±.038 | L98 | vanilla_multiseed | 0.479±0.038 | ✓ |
| TF-IDF DD-Full .961 | L99 | exp7 | 0.961 | ✓ |
| TF-IDF AA-Full .261 | L99 | exp7 | 0.2609 | ✓ |
| TF-IDF DD-K=2 1.000 | L99 | exp7 | 1.000 | ✓ |
| Llama Guard DD-Full .025 | L100 | exp40 | **0.0244** (≈.024) | **✗** |
| Llama Guard AA-Full .000 | L100 | exp40 | 0.000 | ✓ |

---

## Table 3 完整审计 (Cross-Encoder, L148–168)

| 数字 | 位置 | exp_id | Registry 值 | 一致性 |
|------|------|--------|-------------|--------|
| DeBERTa Vanilla DD .312±.026 | L154 | vanilla_multiseed | 0.312±0.026 | ✓ |
| DeBERTa Vanilla AA .258±.000 | L154 | exp2 | 0.258±0.000 | ✓ |
| DeBERTa MLM DD .914±.115 | L155 | plan_017 | 0.9138±0.115 | ✓ |
| DeBERTa MLM AA .893±.080 | L155 | exp2 | 0.893±0.080 | ✓ |
| DeBERTa 9-class DD .994±.005 | L156 | — | **同 Table 1 问题: 实际 .997** | **✗** |
| DeBERTa 9-class AA .972±.026 | L156 | exp2 | 0.972±0.026 | ✓ |
| RoBERTa-base Vanilla DD .981±.026 | L159 | exp1_roberta_vanilla | 0.9813±0.0264 | ✓ |
| RoBERTa-base Vanilla AA .466±.163 | L159 | exp2 roberta_vanilla | 0.466±0.163 | ✓ |
| RoBERTa-base MLM DD .987±.018 | L160 | exp1_roberta_mlm | 0.9874±0.0178 | ✓ |
| RoBERTa-base MLM AA .730±.201 | L160 | exp2 roberta_mlm | 0.730±0.201 | ✓ |
| RoBERTa-base 9-class DD .994±.005 | L161 | exp1_roberta_9class | 0.9936±0.0045 | ✓ |
| RoBERTa-base 9-class AA .939±.046 | L161 | exp2 roberta_9class | 0.939±0.046 | ✓ |
| RoBERTa-large Vanilla DD .927±.036 | L164 | exp15 | 0.927 (std 未存储) | ✓ |
| RoBERTa-large Vanilla AA 1.000±.000 | L164 | exp15 | 1.000 | ✓ |
| RoBERTa-large MLM DD .884±.065 | L165 | exp15c | 0.884 | ✓ |
| RoBERTa-large MLM AA .874±.014 | L165 | exp15c | 0.874 | ✓ |
| RoBERTa-large 9-class DD .987±.004 | L166 | exp15 | 0.987 | ✓ |
| RoBERTa-large 9-class AA .946±.057 | L166 | exp15 | 0.946 | ✓ |

---

## Table 4 完整审计 (ToxicChat, L198–211)

| 数字 | 位置 | exp_id | Registry 值 | 一致性 |
|------|------|--------|-------------|--------|
| JB-MLM .837±.013 | L202 | exp8_mhj_human_data | 0.837±0.013 | ✓ |
| Wiki-MLM .791±.093 | L203 | exp8 | 0.791±0.093 | ✓ |
| Binary .705±.072 | L204 | exp8 | 0.705±0.072 | ✓ |
| Scrambled .616±.056 | L205 | exp8 | 0.616±0.056 | ✓ |
| 9-class .596±.087 | L206 | exp8 | 0.596±0.087 | ✓ |
| Topic .496±.042 | L207 | exp8 | 0.496±0.042 | ✓ |
| Vanilla .413±.021 | L209 | exp8 | 0.413±0.021 | ✓ |

---

## 行内数字审计 (按 Section)

### Cross-Attack Generalization (L58–75)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| DD TF-IDF F1=0.961 | L59 | exp7 | 0.961 | ✓ |
| AA TF-IDF F1=0.261 | L59 | exp7 | 0.2609 | ✓ |
| Vanilla DD Full=0.312±0.026 | L60 | vanilla_multiseed | 0.312±0.026 | ✓ |
| Vanilla K=1: 0.628 → Full: 0.312 | L60 | vanilla_multiseed | k1=0.628, full=0.312 | ✓ |
| MLM F1≥0.97 at K≤5 | L61 | plan_017 | K1:0.973, K2:0.993, K3:0.997, K5:0.997 | ✓ |
| MLM full 0.914±0.115 | L62 | plan_017 | 0.9138±0.115 | ✓ |
| MLM seed 456 recall=0.64 | L62 | — | Registry 仅存 F1=0.7512 | ⚠️ 无法追溯 |
| 9-class full 0.994±0.005 | L62 | — | **0.997±0.005** | **✗** |
| TF-IDF DD=0.961 | L63 | exp7 | 0.961 | ✓ |
| AA 9-class 0.972±0.026 | L64 | exp2 | 0.972±0.026 | ✓ |
| AA TF-IDF 0.261 (P=1.0, R=0.15) | L64 | exp7 | F1=0.2609 (P/R 未存储，数学一致) | ✓ |
| 71pp gap | L64 | plan_006 | max_dd_delta_pp=71.55 | ✓ |
| Bootstrap CI 9-class [0.943,1.000] | L65 | exp9 | [0.9426, 1.000] | ~ |
| Bootstrap CI vanilla [0.202,0.341] | L65 | exp9 | [0.2017, 0.3414] | ~ |
| Permutation p<0.0001 | L65 | exp9 | p=0 (stored) | ✓ |
| FITD all variants ≥0.990 | L65 | exp35 | 9class=1.0, mlm=0.990, vanilla=0.994 | ✓ (但表述模糊) |
| Vanilla K=1: 0.628 → full: 0.312 | L74 | vanilla_multiseed | 0.628 → 0.312 | ✓ |
| MLM K=2: 0.993, full: 0.914±0.115 | L74 | plan_017 | 0.9934, 0.9138±0.115 | ✓ |
| 9-class 0.972–0.994 across prefixes | L74 | plan_006+seeds | K1–Full range 确认 | ✓ |

### Decomposing the Detection Mechanism (L107–137)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| Hierarchy ordering values | L109 | multiple | 全部匹配 (除 .994→.997) | ✗ (同上) |
| MLM ~60pp from vanilla | L113 | derived | 0.914−0.312=0.602 | ✓ |
| TF-IDF AA 0.261 vs 9-class 0.972 | L113 | exp7/exp2 | 一致 | ✓ |
| Classification F1=0.994–1.000 | L114 | — | **0.997–1.000** | **✗** |
| McNemar p>0.13 | L114 | — | ⚠️ 无对应 registry 条目 | N/A |
| Permutation p≥0.40 | L114 | exp9 | p=1.0 | ✓ |
| TOST margin=5pp, p<10⁻⁸, d=−0.14 | L114 | exp41 | p=2.06e-9, d=−0.136 | ~ |
| FITD p<10⁻⁸, d≈0 | L114 | exp41 | p=0, d=0 | ✓ |
| AA d=0.44, p=0.183 | L114 | exp41 | d=0.44, p=0.183 | ✓ |
| 4–20× lower variance (0.005 vs 0.115) | L115 | plan_017/plan_002 | 0.115/0.005=23× | ~ (23× 略超 20×) |
| Wiki-MLM 0.904±0.115 vs jb-MLM 1pp gap | L119 | plan_018/017 | 0.9042 vs 0.9138, gap=1.0pp | ✓ |
| K=2: 0.993 vs 0.911 (8pp) | L119 | plan_017/018 | 0.9934 vs 0.9112, gap=8.2pp | ✓ |
| Wiki-MLM ~12pp degradation under perturbation | L120 | plan_018_wiki_perturbation | 确认 | ✓ |
| Jb-MLM 2.6pp degradation | L120 | exp4 | 确认 | ✓ |
| Topic DD-Full 0.541±0.207 | L123 | plan_016v2 | 0.5411±0.2069 | ✓ |
| Topic seed123=0.252 vs vanilla 0.312 | L123 | plan_016v2 | seed123=0.2525 | ✓ |
| AA hierarchy values | L129 | exp2/exp7/multiple | 全部匹配 | ✓ |
| TF-IDF 0.961→0.261, P=1.0, R=0.15 | L132 | exp7 | F1 一致，P/R 数学一致 | ✓ |
| Classification 0.951–0.990, max gap 3.9pp | L133 | exp2 | 0.951, 0.972, 0.990 → max gap 3.9pp | ✓ |
| DAPT ~71pp over vanilla/TF-IDF | L133 | exp2 | 0.972−0.258=71.4pp | ✓ |
| Mean pooling gap ≤1pp | L136 | exp13 vs plan_002 | DD gap=0.6pp, AA gap=1.0pp | ✓ |
| Turn-order shuffle DeBERTa Δ | L137 | — | ⚠️ 无法追溯 | N/A |
| Turn-order shuffle RoBERTa-large Δ | L137 | — | ⚠️ 无法追溯 | N/A |

### Cross-Encoder (L171–178)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| RoBERTa vanilla DD 0.981±0.026 | L172 | exp1_roberta_vanilla | 0.9813±0.0264 | ✓ |
| DAPT adds 1.3pp | L172 | derived | 0.9936−0.9813=1.23pp | ~ |
| RoBERTa vanilla AA 0.466±0.163, 51.5pp drop | L172 | exp2 | 0.466±0.163, 0.981−0.466=51.5pp | ✓ |
| RoBERTa 9-class AA 0.939±0.046 | L172 | exp2 | 0.939±0.046 | ✓ |
| RoBERTa-large vanilla AA 1.000 vs 9-class 0.946 | L174 | exp15 | 1.000, 0.946 | ✓ |
| BERT proxy DD=0.318±0.031, AA=0.275±0.027 | L178 | exp20_deepcontext_proxy | 0.318±0.031, 0.275±0.027 | ✓ |

### Mixed-LLM (L183–185)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| 9-class DD 0.818±0.096 | L184 | exp16_multi_llm | 0.818±0.096 | ✓ |
| Vanilla DD 0.291±0.065 | L184 | exp16_multi_llm | 0.291±0.065 | ✓ |
| MLM DD 0.289±0.101 | L184 | exp16_multi_llm | 0.289±0.101 | ✓ |
| +53pp (0.818−0.291) | L184 | derived | 0.527=52.7pp | ✓ |
| AA 9-class 0.504±0.107 | L184 | exp16_multi_llm | 0.504±0.107 | ✓ |
| AA vanilla 0.389±0.073 | L184 | exp16_multi_llm | 0.389±0.073 | ✓ |
| +11.5pp | L184 | derived | 0.504−0.389=0.115 | ✓ |
| TF-IDF AA=0.261 | L184 | exp7 | 0.2609 | ✓ |

### Human Data (L214–216)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| 18–42pp gap | L214 | exp8 | 9class−vanilla=18.3pp, JB-MLM−vanilla=42.4pp | ✓ |
| JB-MLM 0.837±0.013 | L216 | exp8 | 0.837±0.013 | ✓ |
| 9-class 0.596±0.087 | L216 | exp8 | 0.596±0.087 | ✓ |
| p<0.001, non-overlapping CIs | L216 | exp12_toxicchat_bootstrap | permutation p=0.0001 | ✓ |

### Perturbation (L220–222)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| Zero degradation IID/OOD DD | L222 | exp4 | 9class delta_full=+0.003 | ✓ |
| ~12pp degradation non-adapted | L222 | plan_004 | baseline_f1_drop=−0.1176 | ✓ |
| p<0.001 | L222 | exp4 | mcnemar p<0.001 | ✓ |
| AA DAPT Δ=−20.4pp | L222 | exp6 | delta_full=−0.2038 | ✓ |
| 52pp over vanilla | L222 | exp6 | 0.7681−0.2482=52.0pp | ✓ |

### Strategy (L225–228)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| κ=0.78, n=50 | L228 | — | ⚠️ Annotation-derived, 非 registry | N/A |
| OOD κ=0.126 | L228 | — | ⚠️ Derived from strategy prediction, 非 registry | N/A |

### Benign Shift (L231–235)

| 数字 | 行 | exp_id | Registry 值 | 一致性 |
|------|-----|--------|-------------|--------|
| WildChat FPR 68.1% | L234 | exp19_wildchat_fpr | 9class_fpr.mean=0.681 | ✓ |
| 10 WildChat → FPR 0% | L235 | exp45_benign_adaptation_curve | n10_multiseed.wc_fpr=0.000±0.000 | ✓ |
| 25 OASST2 → FPR 1.0% | L235 | exp52_oasst2_n25_multiseed | fpr_mean=0.010 (1.0%) | ✓ |
| Dual-OOD drops 12–14pp | L235 | derived from exp19+exp2 | DD: ~13.9pp, AA: ~13.9pp | ✓ |
| Recovers within 0.3pp | L235 | exp45/exp52 | WC: 0.0pp gap; OASST2: 0.3pp gap | ✓ |

### Setup Numbers (L10–17)

| 数字 | 行 | 一致性 |
|------|-----|--------|
| 250 Crescendo + 250 benign = 500 | L11 | ✓ (350+74+76=500) |
| Train 350, val 74, test 76 | L12 | ✓ |
| Test = 38 jailbreak + 38 benign | L12 | ✓ |
| 80 FITD + 38 benign = 118 | L14 | ✓ |
| 80 DD + 38 benign = 118 | L14 | ✓ |
| 80 ActorAttack + 38 benign = 118 | L14 | ✓ |
| BERTScore 0.92, lexical overlap 0.20 | L16 | N/A (dataset construction) |
| ToxicChat 204+204 | L17 | N/A (external dataset) |
| Llama Guard 1.8% (5/278) | L23 | ✓ (exp40: 5/278=1.799%) |

### Inference Efficiency

| 数字 | exp_id | Registry 值 | 一致性 |
|------|--------|-------------|--------|
| 24.3× speedup | exp46_inference_efficiency | speedup_factor=24.3 | ✓ |
| Params 186.7M | exp46 | disped_params_M=186.73 | ✓ |
| VRAM 862 MB | exp29 | 861.5 MB | ~ |

### TOST Equivalence

| 数字 | exp_id | Registry 值 | 一致性 |
|------|--------|-------------|--------|
| DD: p<10⁻⁸ | exp41_tost_10seed | p=2.06e-9 | ✓ |
| DD: d=−0.14 | exp41 | d=−0.136 | ~ |
| FITD: p<10⁻⁸, d≈0 | exp41 | p=0, d=0 | ✓ |
| AA: d=0.44, p=0.183 | exp41 | d=0.44, p=0.183 | ✓ |

---

## 修正建议

1. **9-class / Scrambled DD-Full .994→.997**: 在 Table 1, Table 2, Table 3 及所有行内引用中将 `.994` 改为 `.997`（出现约 8 处）。同时修正 "F1 = 0.994–1.000" 为 "F1 = 0.997–1.000"。
2. **Mean pooling DD-K=2**: 改为 `.994±.009`（3-seed）或添加单种子标注 `$^{\ddagger}$`。
3. **Llama Guard DD-Full**: `.025` → `.024`。
4. **FITD 表述**: "all variants" → "all tested variants" 或列出具体变体。
5. **4–20× variance**: 实际范围为 3–23×（AA std 0.080/0.026=3.1×, DD 0.115/0.005=23×），建议改为 "3–23×" 或限定为 DD 上的比较。
6. **无法追溯项**: 建议将 turn-order shuffling 实验和 McNemar 测试结果注册到 registry。
