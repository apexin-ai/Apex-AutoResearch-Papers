# audit table registry traceability

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_table-registry-traceability_20260523T191641_result.json`
- **Structured JSON:** [`e72f506cd6cc86cd86de.json`](../../sessions/e7/e72f506cd6cc86cd86de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

I now have all the data needed. Let me write the comprehensive traceability report.

## Table 数据溯源报告

### Table 2 (main_results) — Cross-attack generalization, IID (Crescendo) / OOD (DD)

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class IID K=2 | 1.000±.000 | plan_002_* (treatment_k2_f1) | 1.000, 1.000, 1.000 → 1.000±.000 | ✅ |
| 9-class IID Full | 1.000±.000 | plan_002_* (treatment_full_f1) | 1.000, 1.000, 1.000 → 1.000±.000 | ✅ |
| 9-class OOD K=2 | .981±.013 | plan_006 + plan_002_{123,456} (dd_ood_k2) | 0.9904, 0.9904, 0.9622 → 0.981±.013 | ✅ |
| 9-class OOD Full | .997±.005 | plan_006 + plan_002_{123,456} (dd_ood_full) | 1.000, 1.000, 0.9904 → 0.997±.005 | ✅ |
| MLM IID K=2 | .974 | plan_017_mlm_control (iid_f1_k2 seed42) | 0.9737 → .974 | ✅ |
| MLM IID Full | 1.000 | plan_017_mlm_control (iid_f1_full seed42) | 1.000 | ✅ |
| MLM OOD K=2 | .993±.009 | plan_017_mlm_control (dd_ood_f1_k2) | mean=0.9934, std=0.0093 | ✅ |
| MLM OOD Full | .914±.115 | plan_017_mlm_control (dd_ood_f1_full) | mean=0.9138, std=0.115 | ✅ |
| Vanilla IID K=2 | .978±.016 | plan_002_* (baseline_k2) | 0.9867, 0.987, 0.9589 → mean=.978 | ⚠️ std |
| Vanilla IID Full | 1.000±.000 | plan_002_* (baseline_full) | 1.000, 1.000, 1.000 | ✅ |
| Vanilla OOD K=2 | .479±.038 | vanilla_multiseed_dd_ood (k2) | mean=0.479, std=0.038 | ✅ |
| Vanilla OOD Full | .312±.026 | vanilla_multiseed_dd_ood (full) | mean=0.312, std=0.026 | ✅ |
| TF-IDF IID K=2 | 1.000 | plan_002 (tfidf_all_k_f1) | 1.000 | ✅ |
| TF-IDF IID Full | 1.000 | plan_002 (tfidf_all_k_f1) | 1.000 | ✅ |
| TF-IDF OOD K=2 | 1.000 | exp7 (dd_ood k2) | 1.000 | ✅ |
| TF-IDF OOD Full | .961 | exp7 (dd_ood full) | 0.961 | ✅ |

---

### Table 3 (evidence_hierarchy) — DD-Full, AA-Full, DD-K=2

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class DD-Full | .997±.005 | plan_006/plan_002 | 1.000, 1.000, 0.990 → .997±.005 | ✅ |
| 9-class AA-Full | .972±.026 | exp2_actorattack_ood (deberta_9class) | full=0.972, std=0.026 | ✅ |
| 9-class DD-K=2 | .981±.013 | plan_006/plan_002 | 0.990, 0.990, 0.962 → .981±.013 | ✅ |
| Binary DD-Full | 1.000±.000 | mf1_binary_{123,456} + plan_013 (seed42) | seed123=1.000, seed456=1.000, seed42=0.990 → .997±.005 | ⚠️ 见下 |
| Binary AA-Full | .990±.008 | exp2_actorattack_ood (deberta_binary) | full=0.990, std=0.008 | ✅ |
| Binary DD-K=2 | .994±.009 | mf1_binary seeds k2 | seed123=1.000, seed456=1.000 | ⚠️ seed42缺失 |
| Scrambled DD-Full | .997±.005 | mf1_scrambled_{123,456} | seed123=1.000, seed456=1.000 | ⚠️ seed42缺失 |
| Scrambled AA-Full | .951±.043 | exp2_actorattack_ood (deberta_scrambled) | full=0.951, std=0.043 | ✅ |
| Scrambled DD-K=2 | .981±.026 | mf1_scrambled seeds k2 | seed123=1.000, seed456=1.000 | ⚠️ seed42缺失 |
| MLM DD-Full | .914±.115 | plan_017_mlm_control | mean=0.914, std=0.115 | ✅ |
| MLM AA-Full | .893±.080 | exp2_actorattack_ood (deberta_mlm) | full=0.893, std=0.080 | ✅ |
| MLM DD-K=2 | .993±.009 | plan_017_mlm_control | mean=0.993, std=0.009 | ✅ |
| Mean pooling DD-Full | .991±.013 | exp13_meanpool_multiseed (dd_ood.full) | mean=0.9905, std=0.0134 | ✅ |
| Mean pooling AA-Full | .962±.015 | exp13_meanpool_multiseed (actorattack.full) | mean=0.9623, std=0.0151 | ✅ |
| Mean pooling DD-K=2 | **1.000** | exp27_mean_pooling (dd_ood_k2) | 1.000±0 | ⚠️ 见下 |
| Topic DD-Full | .541±.207 | plan_016v2_topic_control | mean=0.5411, std=0.2069 | ✅ |
| Topic AA-Full | .625±.141 | exp2_actorattack_ood (deberta_topic) | full=0.625, std=0.141 | ✅ |
| Topic DD-K=2 | .593±.166 | plan_016v2_topic_control (k2) | mean=0.5926, std=0.1655 | ✅ |
| Wiki-MLM DD-Full | .904±.115 | plan_018_wiki_mlm_control | mean=0.904, std=0.115 | ✅ |
| Wiki-MLM AA-Full | .686±.297 | exp2_actorattack_ood (deberta_wiki_mlm) | full=0.686, std=0.297 | ✅ |
| Wiki-MLM DD-K=2 | .911±.073 | plan_018_wiki_mlm_control (k2) | mean=0.911, std=0.073 | ✅ |
| Vanilla DD-Full | .312±.026 | vanilla_multiseed_dd_ood | mean=0.312, std=0.026 | ✅ |
| Vanilla AA-Full | .258±.000 | exp2_actorattack_ood (deberta_vanilla) | full=0.258, std=0 | ✅ |
| Vanilla DD-K=2 | .479±.038 | vanilla_multiseed_dd_ood (k2) | mean=0.479, std=0.038 | ✅ |
| TF-IDF DD-Full | .961 | exp7 (dd_ood full) | 0.961 | ✅ |
| TF-IDF AA-Full | .261 | exp7 (actorattack full) | 0.2609 → .261 | ✅ |
| TF-IDF DD-K=2 | 1.000 | exp7 (dd_ood k2) | 1.000 | ✅ |
| Llama Guard DD-Full | .025 | exp40_llama_guard_baseline (ood_dd.full) | f1_jb=0.0244 → .025 | ⚠️ 指标不一致 |
| Llama Guard AA-Full | .000 | exp40_llama_guard_baseline (ood_aa.full) | f1_jb=0 | ⚠️ 指标不一致 |
| Dual-OOD no adapt DD | .855 | — | — | ❌ 无法溯源 |
| Dual-OOD no adapt AA | .842 | — | — | ❌ 无法溯源 |
| Dual-OOD +10-shot DD | .994 | — | — | ❌ 无法溯源 |
| Dual-OOD +10-shot AA | .981 | exp45 (aa_f1 n10 multiseed) | 0.981±0.016 | ⚠️ 部分匹配 |

---

### Table 4 (cross_encoder) — DD / AA Full, 3-seed

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| DeBERTa Vanilla DD | .312±.026 | vanilla_multiseed_dd_ood | mean=0.312, std=0.026 | ✅ |
| DeBERTa Vanilla AA | .258±.000 | exp2 (deberta_vanilla) | full=0.258, std=0 | ✅ |
| DeBERTa MLM DD | .914±.115 | plan_017_mlm_control | mean=0.914, std=0.115 | ✅ |
| DeBERTa MLM AA | .893±.080 | exp2 (deberta_mlm) | full=0.893, std=0.080 | ✅ |
| DeBERTa 9-class DD | .997±.005 | plan_006/plan_002 | mean=0.997, std=0.005 | ✅ |
| DeBERTa 9-class AA | .972±.026 | exp2 (deberta_9class) | full=0.972, std=0.026 | ✅ |
| RoBERTa-base Vanilla DD | .981±.026 | exp1_roberta_vanilla | mean=0.9813, std=0.0264 | ✅ |
| RoBERTa-base Vanilla AA | .466±.163 | exp2 (roberta_vanilla) | full=0.466, std=0.163 | ✅ |
| RoBERTa-base MLM DD | .987±.018 | exp1_roberta_mlm | mean=0.9874, std=0.0178 | ✅ |
| RoBERTa-base MLM AA | .730±.201 | exp2 (roberta_mlm) | full=0.730, std=0.201 | ✅ |
| RoBERTa-base 9-class DD | .994±.005 | exp1_roberta_9class | mean=0.9936, std=0.0045 | ✅ |
| RoBERTa-base 9-class AA | .939±.046 | exp2 (roberta_9class) | full=0.939, std=0.046 | ✅ |
| RoBERTa-large Vanilla DD | .927±.036 | exp15 (roberta_large_vanilla) | full=0.927 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large Vanilla AA | 1.000±.000 | exp15 (roberta_large_vanilla) | full=1.000 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large MLM DD | .884±.065 | exp15c (mlm) | full=0.884 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large MLM AA | .874±.014 | exp15c (mlm) | full=0.874 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large 9-class DD | .987±.004 | exp15 (roberta_large_9class) | full=0.987 (single seed) | ⚠️ 无std来源 |
| RoBERTa-large 9-class AA | .946±.057 | exp15 (roberta_large_9class) | full=0.946 (single seed) | ⚠️ 无std来源 |

---

### Table 5 (mixed_llm) — 250 Qwen + 250 Llama

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class Mixed | .996±.006 | exp16 (9class_mean.mixed_test) | 0.996 | ⚠️ std无来源 |
| 9-class DD OOD | .818±.096 | exp16 (9class_mean.dd_ood) | 0.818, std=0.096 | ✅ |
| 9-class AA OOD | .504±.107 | exp16 (9class_mean.aa_ood) | 0.504, std=0.107 | ✅ |
| 9-class FITD OOD | .997±.005 | exp16 (9class_mean.fitd_ood) | 0.997, std=0.005 | ✅ |
| 9-class ToxicChat | .550±.052 | exp16 (9class_mean.toxicchat_balanced) | 0.55, std=0.052 | ✅ |
| MLM Mixed | .681±.226 | exp16 (mlm_mean.mixed_test) | **0.975** | ❌ 不一致 |
| MLM DD OOD | .289±.101 | exp16 (mlm_mean.dd_ood) | 0.289, std=0.101 | ✅ |
| MLM AA OOD | .258±.075 | exp16 (mlm_mean.aa_ood) | 0.258, std=0.075 | ✅ |
| MLM FITD OOD | .679±.188 | exp16 (mlm_mean.fitd_ood) | 0.679, std=0.188 | ✅ |
| MLM ToxicChat | .256±.053 | exp16 (mlm_mean.toxicchat_balanced) | 0.256, std=0.053 | ✅ |
| Vanilla Mixed | .802±.010 | exp16 (vanilla_mean.mixed_test) | 0.802 | ⚠️ std无来源 |
| Vanilla DD OOD | .291±.065 | exp16 (vanilla_mean.dd_ood) | 0.291, std=0.065 | ✅ |
| Vanilla AA OOD | .389±.073 | exp16 (vanilla_mean.aa_ood) | 0.389, std=0.073 | ✅ |
| Vanilla FITD OOD | .867±.022 | exp16 (vanilla_mean.fitd_ood) | 0.867, std=0.022 | ✅ |
| Vanilla ToxicChat | .356±.009 | exp16 (vanilla_mean.toxicchat_balanced) | 0.356, std=0.009 | ✅ |

---

### Table 6 (human_data) — ToxicChat macro F1

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| JB-MLM | .837±.013 | exp8 (jb_mlm_macro_f1) | 0.837, std=0.013 | ✅ |
| Wiki-MLM | .791±.093 | exp8 (wiki_mlm_macro_f1) | 0.791, std=0.093 | ✅ |
| Binary | .705±.072 | exp8 (binary_macro_f1) | 0.705, std=0.072 | ✅ |
| Scrambled | .616±.056 | exp8 (scrambled_macro_f1) | 0.616, std=0.056 | ✅ |
| 9-class | .596±.087 | exp8 (9class_macro_f1) | 0.596, std=0.087 | ✅ |
| Topic | .496±.042 | exp8 (topic_macro_f1) | 0.496, std=0.042 | ✅ |
| Vanilla | .413±.021 | exp8 (vanilla_macro_f1) | 0.413, std=0.021 | ✅ |

**Table 6 完全一致 ✅**

---

### Table 7 (ood_perturbation) — OOD DD, Clean/Perturbed Full, Δ

| Cell | 论文值 | Registry exp_id | Registry 值 | 一致? |
|------|--------|----------------|-------------|-------|
| 9-class Clean Full | .994±.005 | exp4 (9class_3seed.clean_full) | 0.9968 (pooled) | ⚠️ .997 vs .994 |
| 9-class Pert Full | 1.000±.000 | exp4 (9class_3seed.perturbed_full) | 1.000 | ✅ |
| 9-class Δ Full | +0.6 | exp4 (delta_full) | +0.0032 → +0.3pp | ⚠️ +0.6 vs +0.3 |
| 9-class Δ K=1 | +0.6 | exp4 (delta_k1) | +0.0063 → +0.6pp | ✅ |
| Binary Clean Full | 1.000±.000 | exp4 (binary_3seed.clean_full) | 0.9968 | ⚠️ .997 vs 1.000 |
| Binary Pert Full | 1.000±.000 | exp4 (binary_3seed.perturbed_full) | 1.000 | ✅ |
| Binary Δ Full | 0.0 | exp4 | +0.0032 → +0.3pp | ⚠️ 0.0 vs +0.3 |
| Binary Δ K=1 | +0.6 | exp4 (delta_k1) | +0.0064 → +0.6pp | ✅ |
| Scrambled Clean Full | .994±.005 | exp4 (scrambled_3seed.clean_full) | 0.9968 | ⚠️ .997 vs .994 |
| Scrambled Pert Full | 1.000±.000 | exp4 (perturbed_full) | 1.000 | ✅ |
| JB MLM Clean Full | .914±.115 | exp4 (jb_mlm_3seed.clean_full) | 0.9138 | ✅ |
| JB MLM Pert Full | .941 | exp4 (jb_mlm_3seed.perturbed_full) | 0.9409 → .941 | ✅ |
| JB MLM Δ Full | +2.7 | exp4 (delta_full) | +0.0271 → +2.7pp | ✅ |
| Wiki MLM Clean Full | .904±.115 | exp4 (wiki_mlm_3seed.clean_full) | 0.9042 | ✅ |
| Wiki MLM Pert Full | .872 | exp4 (perturbed_full) | 0.8715 → .872 | ✅ |
| Wiki MLM Δ Full | −3.3 | exp4 (delta_full) | −0.0327 → −3.3pp | ✅ |
| Vanilla Clean Full | .312±.026 | exp4 (vanilla_3seed.clean_full) | 0.3123 → .312 | ✅ |
| Vanilla Pert Full | .339±.055 | exp4 (perturbed_full) | 0.3394 → .339 | ✅ |
| Vanilla Δ Full | +2.7 | exp4 (delta_full) | +0.0271 → +2.7pp | ✅ |
| Vanilla Δ K=1 | −6.8±1.1 | exp4 (delta_k1) | −0.0681 → −6.8pp | ✅ |

---

### ⚠️ 不一致（需修复或解释）

1. **Table 2 Vanilla IID K=2 std**: 论文 .016, 计算得 .013 (pop std, n=3). 论文声明使用 pop std (n divisor), 但 .016 匹配 Bessel-corrected std (n−1 divisor). 轻微不一致。

2. **Table 3 Binary DD-Full**: 论文 1.000±.000, 但 registry seed42 (plan_013_none_collapse) dd_binary_full_f1=0.9904. 如果 seed42 确实为 0.990, 则 3-seed mean=.997±.005, 不是 1.000±.000。

3. **Table 3 Mean pooling DD-K=2**: 论文 1.000, 但 exp13_meanpool_multiseed 报告 dd_ood.k2 mean=0.994±.009。论文使用了 exp27 (1.000±.000) 的值而非 exp13 的值, 两个实验结果不同 — 应统一使用同一组实验。

4. **Table 3 Llama Guard 指标不一致**: 论文显示 DD=.025 / AA=.000, 这是 **jailbreak-class F1** (f1_jb), 而其他所有行使用 **macro F1**。如果使用 macro F1, Llama Guard DD 应为 .253。虽然 Llama Guard 几乎不检测任何 jailbreak, 但表内指标不统一。

5. **Table 5 MLM Mixed**: 论文 .681±.226, registry exp16 mixed_test=0.975。差异巨大。可能原因: registry 存储的是 Qwen-only test 性能 (note 标注 "qwen_test INVALIDATED" 因 35.5% 数据泄漏), 而论文使用正确的 Qwen+Llama 混合测试集。但 registry 对应字段未更新。

6. **Table 7 Clean Full vs Table 2/3**: 9-class clean DD-Full 在 Table 7 为 .994, 在 Table 2/3 为 .997。两表应评估同一模型在同一数据上的结果, 差异 0.003 表明可能使用了不同的 checkpoint 或不同的评估代码。Binary 同理 (Table 7=1.000 vs 实际应为 .997)。

7. **Table 7 Δ Full 与 clean/pert 不一致**: 9-class clean=.994, pert=1.000, Δ 应为 +0.6pp; 但 exp4 pooled clean=0.9968 → per-seed 计算给出 Δ=+0.32pp, 不是 +0.6pp。Binary clean=1.000, pert=1.000, Δ 应为 0.0; exp4 pooled clean=0.9968 → Δ=+0.32pp。论文的 Δ 值基于四舍五入后的 .994 和 1.000 计算, 而非原始精度值。

---

### ❌ 无法溯源

1. **Table 3 Dual-OOD "no adapt" DD=.855, AA=.842** — 未找到对应 registry 实验。这些值来自将 WildChat benign 替换 IID benign 进行测试, 但该评估结果未注册。

2. **Table 3 Dual-OOD "+10-shot" DD=.994** — exp45 报告适配后 dd_f1=1.000 (使用 IID benign 测试), 与论文 .994 不符。.994 应来自以 WildChat benign 替换测试集的 dual-OOD 评估, 但该计算未注册。AA=.981 与 exp45 的 aa_f1=0.981 匹配, 但 DD 值不匹配。

3. **Table 4 RoBERTa-large 所有 std 值** — registry 仅有单 seed 值 (exp15/15b/15c), 无 3-seed 数据。论文标题声明 "3-seed mean±std", mean 值与 registry 单 seed 值完全吻合, 但 std 来源不明 (未注册为 registry 实验)。

4. **Table 3 Binary/Scrambled DD seed42** — mf1_binary 和 mf1_scrambled 系列仅有 seed123 和 seed456 数据。seed42 的 DD OOD 值需从 plan_013_none_collapse (binary) 推断, 但该实验可能使用不同数据版本 (v4c)。

5. **Table 5 Mixed/Vanilla Mixed 列 std 值** — registry exp16 仅存储 mean, 无 std。论文的 .006 (9-class) 和 .010 (vanilla) 无 registry 来源。

---

### 总结

- **完全一致**: Table 6 (human_data) 全部 7 行 ✅; Table 4 DeBERTa 和 RoBERTa-base 行 (12 cells) ✅; Table 2 大部分 cells ✅; Table 3 大部分 cells ✅
- **轻微不一致**: 主要是 pop std vs Bessel std (Table 2 vanilla IID K=2), 以及 Table 7 的 clean baseline 与 Table 2/3 相差 0.003 (可能来自不同评估 pipeline)
- **显著不一致**: Table 5 MLM Mixed (.681 vs registry 0.975); Table 3 Binary DD-Full (1.000 vs 计算应为 .997); Mean pooling DD-K=2 混用两组实验数据
- **无法溯源**: RoBERTa-large 的全部 std 值; Dual-OOD 的 4 个 cells; Table 5 Mixed 列的 std 值

---
