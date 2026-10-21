# 附录数据真实性审计

## 审计统计
- 总数字数：~540（表格 cell ~497 + 正文定量数字 ~43）
- 已验证（与服务器 JSON 源对账）：~380
- 未验证（无预计算 JSON，需重跑脚本）：~120
- 问题数：11（含 2 个严重、5 个中等、4 个轻微）

---

## 表格逐一验证摘要

| 表格 | cell 数 | 已验证 | 问题数 | 状态 |
|------|---------|--------|--------|------|
| tab:gee_corr (GEE correlation) | 36 | 36 | 0 | ✅ 通过（threshold values only） |
| tab:gee-interaction | 24 | 24 | 1 轻微 | ⚠️ Qwen3 Form p 微小舍入差 |
| tab:gee_ci | 48 | 44 | 1 中等 | ⚠️ Gemini verb Style OR 不一致 |
| tab:rewriter_indep | 10 | 5 | 0 | ⏳ GPT-4o rewriter verb 无专用 JSON |
| tab:rewriter_indep_form | 6 | 6 | 0 | ✅ 通过 |
| tab:nli_sweep | 44 | 44 | 0 | ✅ 通过 |
| tab:tost_sensitivity | 12 | 8 | 1 轻微 | ⚠️ 舍入偏差（见下） |
| tab:bayesian_equiv | 9 | 0 | 0 | ⏳ 无预计算 JSON |
| tab:bt_ci | 51 | 42 | 0 | ✅ 通过（已验证部分） |
| tab:attenuation | 21 | 21 | 0 | ✅ 通过 |
| tab:power | 18 | 0 | 0 | ⏳ 无预计算 JSON，需重跑 gen_power_curve.py |
| tab:sensitivity (formality) | 21 | 7 | 0 | ⏳ 部分验证（BT 行匹配；无formality 7-method JSON） |
| tab:verb_sensitivity | 21 | 21 | 0 | ✅ 通过 |
| tab:verb_n355 | 16 | 0 | 0 | ⏳ 原始 JSONL 存在，无汇总 JSON |
| tab:likert100 | 12 | 8 | 1 轻微 | ⚠️ Llama 1-10 d 与源文件差异 |
| tab:nli_ablation | 6 | 6 | 2 中等 | ❌ "All" 列两个值与源不一致 |
| tab:artifact | 12 | 12 | 0 | ✅ 通过 |
| tab:holm8 | 32 | 32 | 1 中等 | ⚠️ Gemini Form raw p 不一致 |
| tab:cross_axis | 12 | 4 | 0 | ⏳ 定性 JSON 仅有摘要 |
| tab:fk_desc | 12 | 8 | 1 轻微 | ⚠️ Caption 称 "all pairs" 但数值匹配 NLI-passed |
| tab:cross_bench | 24 | 18 | 2 中等 | ⚠️ 两处 Likert d/p 与源不一致 |
| tab:claude_crossbench | 25 | 25 | 1 严重 | ❌ AEval Verb Likert d/p 不一致 |
| tab:concordance | 50 | 0 | 0 | ⏳ 无预计算 JSON |
| tab:gee_corr footnote n | 2 | 2 | 0 | ✅ 已修复（form n=88, verb n=86） |

---

## 问题清单

| # | 表格/位置 | 问题描述 | 严重度 | 建议修复 |
|---|----------|----------|--------|----------|
| 1 | tab:nli_ablation Formality "All" | 论文 63.0%，源 nli_gate_ablation.json bt=0.635 (63.5%) | **中等** | 核实计算逻辑。若源正确，改为 63.5%；若 63.0% 来自不同分析（如 GPT-4o），需标注 |
| 2 | tab:nli_ablation Verbosity "All" | 论文 76.0%，源 nli_gate_ablation.json bt=0.7699 (77.0%) | **中等** | 同上。源数据明确显示 n=100, bt=0.7699 |
| 3 | tab:gee_ci Gemini verb | Style OR 论文 8.98，源 gemini_flash_fourth_judge.json style_or=9.159；CI [3.68, 21.94] vs 源 [3.75, 22.38] | **中等** | 重跑 GEE 确认。可能是不同 NLI 筛选批次导致 |
| 4 | tab:holm8 rank 8 | Gemini Form raw p 论文 .0306，源 gemini_flash_fourth_judge.json p_val=0.0448 | **中等** | 与 #3 相关。若 BT 重算，Holm p 也需更新。.0306 < .0500 和 .0448 < .0500 结论不变，但数值需一致 |
| 5 | tab:claude_crossbench AEval Verb | Likert d 论文 .252，源 claude_crossbench_results.json cohen_d=0.298；p 论文 .002，源 wilcoxon_p=0.000441 | **严重** | d 和 p 均有显著差异（.252 vs .298，.002 vs .0004）。需确认是否使用了不同统计方法或数据子集 |
| 6 | tab:cross_bench GPT-4o MTB | Likert d 论文 .111，源 gpt4o_crossbench_results.json cohen_d=0.135；p 论文 .016，源 wilcoxon_p=0.007 | **严重** | 同上，d 和 p 均有差异。也需确认 BT CI 上界（论文 .753 vs 源 .760） |
| 7 | tab:tost_sensitivity 10pp | p 论文 .156，源 tost_sensitivity.json tost_p=0.155455 → .155 | 轻微 | 舍入偏差 0.001，不影响结论。建议统一为 .155 |
| 8 | tab:tost_sensitivity 15pp | p 论文 .010，源 tost_p=0.009472 → .009 | 轻微 | 舍入偏差 0.001。建议改为 .009 |
| 9 | tab:gee-interaction Qwen3 Form p | 论文 .320，源 interaction_p=0.319457 → .319 | 轻微 | 舍入偏差 0.001。建议改为 .319 |
| 10 | tab:fk_desc caption | Caption 称 "Computed on all pairs"，但 FK grade 和 sent length 数值匹配 NLI-passed 子集 | 轻微 | 修改 caption 为 "Computed on NLI-verified pairs" 或重算 all-pairs 值 |
| 11 | tab:likert100 Llama 1-10 | d=.000 (p=1.00)，但 llama70b_third_judge.json cohen_d=0.010, wilcoxon_p=0.533 | 轻微 | 可能使用不同 d 定义（style-aligned vs ATE）。建议确认并注明 |

---

## 之前已知问题修复确认

- [x] **BT 66.5% → 67.5% 区分**：论文正确区分了 n=88 BT=66.5%（tab:bt_ci Qwen3 Form .665）和 n=355 BT=67.5%（正文引用）。tab:attenuation 正文说 "BT stable at 67.5%"。n=355 的 67.5% 无预计算 JSON 验证，但与 n=88 的 66.5% 逻辑一致（scaled replication 效应略增属合理）。**部分确认——建议补一个 n=355 BT 的汇总 JSON。**

- [x] **GEE 脚注 n=88 → form n=88 / verb n=86**：tab:gee_ci 脚注已修复为 "formality rows: n = 88; verbosity rows: n = 86"。与源数据（gee_interaction_analysis.json: Form n_pairs=88, Verb n_pairs=86）一致。**已修复。**

---

## 找不到出处的数字

以下数字在服务器上无预计算 JSON，需重跑分析脚本验证：

| 位置 | 数字 | 状态 | 处理建议 |
|------|------|------|----------|
| tab:verb_n355 全表 | Qwen3 BT=.733, Likert d=.149 等 | 原始 JSONL 存在（verified_scaled_verbosity_passed.jsonl, 330 行），无汇总 | 运行分析脚本生成汇总 JSON |
| tab:concordance 全表 | 所有 concordance 率和 r_pb | 无 concordance JSON | 从 pairwise/likert 原始数据重算 |
| tab:power 全表 | Required n 和 Ratio | gen_power_curve.py 存在，无输出 JSON | 重跑脚本并存储输出 |
| tab:bayesian_equiv 全表 | BF₀₁ 值 | 无 Bayesian 分析 JSON | 需编写或定位 Bayesian 等价性分析脚本 |
| tab:sensitivity 非 BT 行 | Likert ATE d=0.102 等 | 无 formality 7-method JSON（仅有 verbosity 版） | 需定位或重跑 formality sensitivity 分析 |
| tab:gee_corr 具体 QIC 值 | |ΔQIC| < 0.001 等 | 无 QIC 比较 JSON | 上界声明无需精确值，但建议存档 |
| tab:cross_axis Word count −3.4% 等 | 定量 cross-axis 指标 | cross_axis_gradient.json 仅有定性摘要 | 需定位详细 cross-axis 分析输出 |
| 正文 n=355 BT=67.5% | 67.5% | gee_n355_results.json 仅有 GEE，无 BT | 从 scored_scaled_formality_qwen32b.jsonl 计算 BT |
| 正文 Direction §A: 78.8%, 54.5% | 方向不对称 BT 值 | 无专用 JSON | 从 bt_model_diagnostics.json 推导或独立验证 |
| 正文 Consistency §B: 55/98, 56.1% | 一致性筛选统计 | 无专用 JSON | 可从 pairwise 数据重算 |

---

## 已验证表格详细对账记录

### tab:attenuation（Bootstrap Attenuation）✅
源文件：`bootstrap_attenuation.json`
| n | 论文 d | 源 d_median | 论文 CI | 源 CI | 匹配 |
|---|--------|-------------|---------|-------|------|
| 50 | −0.017 | −0.01737 | [−0.308, 0.262] | [−0.308, 0.262] | ✅ |
| 100 | −0.015 | −0.01540 | [−0.219, 0.176] | [−0.220, 0.176] | ✅ |
| 150 | −0.019 | −0.01855 | [−0.179, 0.145] | [−0.179, 0.145] | ✅ |
| 200 | −0.016 | −0.01577 | [−0.157, 0.119] | [−0.157, 0.119] | ✅ |
| 250 | −0.018 | −0.01770 | [−0.144, 0.107] | [−0.144, 0.107] | ✅ |
| 300 | −0.018 | −0.01754 | [−0.131, 0.095] | [−0.131, 0.095] | ✅ |
| 355 | −0.017 | −0.01669 | [−0.123, 0.087] | [−0.123, 0.087] | ✅ |

### tab:gee-interaction（GEE Interaction）✅ (1 轻微舍入)
源文件：`gee_interaction_analysis.json`
| Config | 论文 OR | 源 OR | 论文 p | 源 p | 匹配 |
|--------|---------|-------|--------|------|------|
| GPT-4o Form | 0.661 | 0.661 | .527 | .527 | ✅ |
| GPT-4o Verb | 1.269 | 1.269 | .705 | .705 | ✅ |
| GPT-4o Reg | 2.601 | 2.601 | .136 | .136 | ✅ |
| Qwen3 Form | 0.518 | 0.518 | .320 | .319 | ⚠️ |
| Qwen3 Verb | 0.450 | 0.450 | .221 | .221 | ✅ |
| Qwen3 Reg | 0.555 | 0.555 | .383 | .383 | ✅ |
| Llama Form | 0.968 | 0.968 | .963 | .963 | ✅ |
| Llama Verb | 1.103 | 1.103 | .870 | .870 | ✅ |

### tab:gee_ci（GEE CIs）✅ (1 中等)
源文件：`gee_interaction_analysis.json` + `gee_n355_results.json` + `gemini_flash_fourth_judge.json`
| Config | 论文 Style OR | 源 Style OR | 论文 Orig OR | 源 Orig OR | 匹配 |
|--------|--------------|-------------|-------------|------------|------|
| Qwen3 verb | 13.10 | 13.101 | 0.49 | 0.491 | ✅ |
| GPT-4o verb | 11.34 | 11.344 | 0.45 | 0.452 | ✅ |
| Llama verb | 8.21 | 8.213 | 0.38 | 0.378 | ✅ |
| Gemini verb | 8.98 | **9.159** | 0.46 | 0.451 | ❌ Style OR |
| GPT-4o form | 2.58 | 2.582 | 2.32 | 2.324 | ✅ |
| Qwen3 form | 4.20 | 4.201 | 4.70 | 4.704 | ✅ |
| Qwen3 form^a | 2.15 | 2.150 | 4.99 | 4.995 | ✅ |
| Llama form | 4.81 | 4.808 | 3.12 | 3.118 | ✅ |
| Gemini form | 1.64 | 1.644 | 2.51 | 2.508 | ✅ |
| GPT-4o reg | 1.88 | 1.880 | 2.21 | 2.207 | ✅ |
| Qwen3 reg | 1.91 | 1.905 | 5.72 | 5.718 | ✅ |
| Llama reg | 3.33 | 3.330 | 3.07 | 3.074 | ✅ |

### tab:rewriter_indep_form（Rewriter Independence Formality）✅
源文件：`gpt4o_rewriter_formality_results.json`
| Metric | GPT-4o Rewriter 论文 | 源 | 匹配 |
|--------|---------------------|-----|------|
| NLI pass rate | 90/100 (90%) | n_nli_pass=90 | ✅ |
| BT P | .644 [.561, .728] | 0.6444 [0.5611, 0.7277] | ✅ |
| Likert d (p) | −.081 (.184) | d=−0.0808, p=0.1835 | ✅ |
| Blindspot | Yes | true | ✅ |

### tab:artifact（Rewriting Artifact Control）✅
源文件：`placebo_bt_reanalysis.json`
| Config | 论文 BT P(orig) | 源 bt_original | 论文 CI | 源 CI | 论文 p | 匹配 |
|--------|----------------|----------------|---------|-------|--------|------|
| Form GPT-4o | .418 | 0.4177 | [.342, .500] | [.342, .500] | .037 | ✅ |
| Form Qwen3 | .377 | 0.3766 | [.303, .451] | [.303, .451] | .0006 | ✅ |
| Verb GPT-4o | .167 | 0.1668 | [.084, .262] | [.084, .262] | <.0001 | ✅ |
| Verb Qwen3 | .082 | 0.0816 | [.035, .140] | [.035, .140] | <.0001 | ✅ |

### tab:nli_ablation（NLI Gate Ablation）❌
源文件：`nli_gate_ablation.json`
| Axis | Subset | 论文 | 源 | 匹配 |
|------|--------|------|-----|------|
| Form | NLI-pass | 66.5% | 0.6647 (66.5%) | ✅ |
| Form | NLI-fail | 41.7% | 0.4168 (41.7%) | ✅ |
| Form | All | **63.0%** | **0.635 (63.5%)** | ❌ |
| Verb | NLI-pass | 77.3% | 0.7732 (77.3%) | ✅ |
| Verb | NLI-fail | 75.0% | 0.7496 (75.0%) | ✅ |
| Verb | All | **76.0%** | **0.7699 (77.0%)** | ❌ |

### tab:verb_sensitivity（Verbosity Sensitivity）✅
源文件：`verbosity_7method_sensitivity.json`
| Method | 论文 Stat | 源 Stat | 论文 p | 源 p | 匹配 |
|--------|-----------|---------|--------|------|------|
| BT model | 77.3% [70.3, 84.3] | 0.7732 [0.703, 0.843] | <0.001 | 0.0 | ✅ |
| Likert ATE | d=0.056 | 0.0557 | 0.691 | 0.691 | ✅ |
| Binarized χ² | OR=2.16 | 2.162 | 0.213 | 0.213 | ✅ |
| Ordinal reg | β=0.159 | 0.159 | 0.575 | 0.575 | ✅ |
| Paired t-test | d=0.056 | 0.056 | 0.607 | 0.607 | ✅ |
| Mann-Whitney U | r=−0.046 | −0.046 | 0.578 | 0.578 | ✅ |
| Cohen's d | d=0.036 | 0.036 | — | — | ✅ |

### tab:tost_sensitivity（TOST Equivalence）⚠️
源文件：`artifacts/r12_fixes/tost_sensitivity.json`
| Δ (pp) | 论文 p | 源 tost_p | 匹配 |
|--------|--------|-----------|------|
| 5 | .626 | 0.6255 | ✅ |
| 10 | .156 | 0.1555 | ⚠️ (.155→.156) |
| 15 | .010 | 0.00947 | ⚠️ (.009→.010) |
| 20 | .0001 | 0.000117 | ✅ |

### BT GoF（正文 §H）✅
源文件：`bt_model_diagnostics.json`
| Metric | 论文 | 源 | 匹配 |
|--------|------|-----|------|
| Form deviance | 52.80 | 52.8047 | ✅ |
| Form df | 45 | 45 | ✅ |
| Form p | 0.198 | 0.198 | ✅ |
| Verb p | 0.905 | 0.905 | ✅ |
| Strat form 88.9% vs 52.6% | 88.9% / 52.6% | 0.889 / 0.526 | ✅ |
| Fisher p | 0.015 | 0.01464 | ✅ |
| Verb Fisher p | 0.453 | 0.453 | ✅ |

### Originality Minimal Subset（正文 §H）✅
源文件：`originality_minimal_subset.json`
| Metric | 论文 | 源 | 匹配 |
|--------|------|-----|------|
| Form BT | 67.3% | 0.6727 | ✅ |
| Form n | 55 | 55 | ✅ |
| Form Δ | +0.8pp | 0.008 | ✅ |
| Form ΔCI | [−11.0, +12.6] | [−0.110, 0.126] | ✅ |
| Verb BT | 76.0% | 0.7599 | ✅ |
| Verb n | 50 | 50 | ✅ |
| Verb Δ | −1.3pp | −0.0133 | ✅ |
| Anti-orig form | 75.0% | 0.7496 | ✅ |
| Anti-orig verb | 86.1% | 0.8609 | ✅ |

### tab:claude_crossbench（Claude Cross-Benchmark）⚠️
源文件：`artifacts/r14_fixes/claude_crossbench_results.json`
| Config | 论文 BT | 源 BT | 论文 d | 源 d | 论文 Style OR | 源 Style OR | 匹配 |
|--------|---------|-------|--------|------|-------------|-------------|------|
| LLMBar Form | .562 | .562 | −.021 | −.021 | 1.47 | 1.47 | ✅ |
| LLMBar Verb | .541 | .541 | −.039 | −.040 | 1.52 | 1.52 | ✅ |
| AEval Form | .698 | .698 | .081 | .081 | 1.99 | 1.99 | ✅ |
| AEval Verb | .683 | .683 | **.252** | **.298** | 4.76 | 4.76 | ❌ d/p |
| MTB Form | .733 | .733 | .233 | .199 | 1.64 | 1.64 | ⚠️ d differs |

### tab:cross_bench（Cross-Benchmark BT）⚠️
源文件：`gpt4o_crossbench_results.json` + `cross_benchmark_local.json`
| Config | 论文 BT | 源 BT | 论文 Likert d | 源 d | 匹配 |
|--------|---------|-------|--------------|------|------|
| AEval GPT-4o Form | .727 | .727 | .005 (.909) | .005 (.909) | ✅ |
| AEval Qwen3 Form | .657 | — | .081 (.198) | — | ⏳ |
| AEval Qwen3 Verb | .841 | — | .375 (.0003) | — | ⏳ |
| AEval Llama Form | .750 | .756 | .212 (.012) | .211 (.012) | ⚠️ BT diff |
| MTB GPT-4o Form | .692 | .692 | **.111 (.016)** | **.135 (.007)** | ❌ d/p |
| MTB Qwen3 Form | .712 | .699 | .149 (.007) | .149 (.007) | ⚠️ BT diff |

---

## 审计结论

### 高置信度通过（数据可追溯且一致）
tab:attenuation, tab:gee-interaction, tab:rewriter_indep_form, tab:nli_sweep, tab:artifact, tab:verb_sensitivity, tab:bt_ci (LLMBar portion), tab:holm8 (除 Gemini form), BT GoF 正文, originality minimal subset 正文

### 需修复（数值与源数据不一致）
1. **tab:nli_ablation "All" 列**（问题 #1-2）：两个 cell 与源 JSON 差 0.5-1.0pp
2. **tab:claude_crossbench AEval Verb Likert**（问题 #5）：d 差 0.046，p 差一个数量级
3. **tab:cross_bench GPT-4o MTB Likert**（问题 #6）：d 差 0.024，p 差 0.009
4. **tab:gee_ci Gemini verb**（问题 #3）：Style OR 差 0.18
5. **tab:holm8 Gemini form p**（问题 #4）：raw p 差 0.014

### 需补充源数据（无预计算 JSON）
tab:verb_n355, tab:concordance, tab:power, tab:bayesian_equiv, tab:sensitivity (formality rows), tab:gee_corr QIC, tab:cross_axis 定量值, 正文 n=355 BT=67.5%

### 建议
1. **优先修复问题 #1-6**，尤其是 nli_ablation 和 claude_crossbench 的数据不一致
2. **补充汇总 JSON**：对 verb_n355, concordance, power, bayesian_equiv 等分析输出存档为 JSON
3. **统一舍入规则**：当前论文混用 round-half-up 和 round-half-even，建议统一为 round-half-even（Python 默认）
4. **修正 fk_desc caption**：改为 "NLI-verified pairs" 或重算 all-pairs 值
