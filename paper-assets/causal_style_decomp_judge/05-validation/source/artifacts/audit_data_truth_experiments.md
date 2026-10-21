# 实验数据真实性审计（Experiments/Analysis + Table 1 + Table 2）

## 审计统计
- 总数字数：~120+
- 已验证：115
- 问题数：10（3 HIGH, 4 MEDIUM, 3 LOW）

---

## Table 1 逐 cell 验证

### BT win probability

| Judge | Axis | BT(论文) | BT(源文件) | 源 | 状态 |
|-------|------|----------|-----------|-----|------|
| GPT-4o | Form | .630 | 0.6302 | nli_threshold_sweep (threshold=0.9) | ✓ |
| GPT-4o | Verb | .760 | 0.7602 | nli_threshold_sweep (threshold=0.9) | ✓ |
| GPT-4o | Reg | .570 | 0.5699 | registry gpt4o_register | ✓ |
| Qwen3 | Form | .665 | 0.6647 | nli_gate_ablation.json (nli_pass) | ✓ |
| Qwen3 | Form^b | .675 | 0.675 | registry exp-006 (n=355) | ✓ |
| Qwen3 | Verb | .773 | 0.7732 | nli_gate_ablation.json (nli_pass) | ✓ |
| Qwen3 | Reg | .553 | 0.553 | cross_axis_gradient.json | ✓ |
| Llama-70B | Form | .695 | 0.6946 | llama70b_third_judge.json | ✓ |
| Llama-70B | Verb | .735 | 0.7349 | llama70b_third_judge.json | ✓ |
| Llama-70B | Reg | .635 | 0.6353 | llama70b_register_summary.json | ✓ |
| Gemini | Form | .574 | 0.5738 | gemini_flash_fourth_judge.json | ✓ |
| Gemini | Verb | .708 | 0.7076 | gemini_flash_fourth_judge.json | ✓ |
| Claude | Form | .562 | 0.562 | claude_tost_equivalence.json | ✓ |
| Claude | Verb | .541 | 0.541 | claude_tost_equivalence.json | ✓ |

**结论：14/14 BT 值全部验证通过。**

### Likert d 和 p 值

源文件：`/root/causal_style_decomp_judge/analysis/table1_verified.csv`

| Judge | Axis | d(论文) | d(源) | p(论文) | p(源) | 状态 |
|-------|------|---------|-------|---------|-------|------|
| GPT-4o | Form | -.041 | -0.0417 | .905 | 0.9054 | ⚠️ d 应四舍五入为-.042 |
| GPT-4o | Verb | .049 | 0.0488 | .403 | 0.4033 | ✓ |
| GPT-4o | Reg | .000 | 0.0000 | .785 | 0.7849 | ✓ |
| Qwen3 | Form | -.052 | -0.0523 | .461 | 0.4611 | ✓ |
| Qwen3 | Form^b | -.025 | -0.025 | .600 | 0.5999 | ✓ (registry exp-006) |
| Qwen3 | Verb | .036 | 0.0362 | .395 | 0.3949 | ✓ |
| Qwen3 | Reg | -.073 | -0.0731 | .373 | 0.3730 | ✓ |
| Llama-70B | Form | .010 | 0.0096 | .534 | 0.5335 | ✓ |
| Llama-70B | Verb | .020 | 0.0203 | .284 | 0.2840 | ✓ |
| Llama-70B | Reg | .024 | 0.0238 | .524 | 0.5241 | ✓ |
| Gemini | Form | -.082 | -0.0820 | .309 | 0.3088 | ✓ |
| Gemini | Verb | .051 | 0.0509 | .370 | 0.3697 | ✓ |
| Claude | Form | -.021 | -0.0210 | .721 | 0.7207 | ✓ |
| Claude | Verb | -.039 | -0.0397 | .743 | 0.7427 | ⚠️ d 应四舍五入为-.040 |

**结论：Likert p 值全部正确。2 个 d 值存在截断 vs 四舍五入不一致（LOW，不影响结论）。**

### n 值

| Axis | n(论文) | n(源) | 状态 |
|------|---------|-------|------|
| Formality | 88 | 88 (table1_verified) | ✓ |
| Verbosity | 86 | 86 (table1_verified) | ✓ |
| Register | 不在 Table 1 | 93-94 (table1_verified) | - |

---

## Table 2 逐 cell 验证

主要源文件：`gee_interaction_analysis.json`（GPT-4o/Qwen3/Llama-70B）、`gemini_flash_fourth_judge.json`（Gemini）、`gee_n355_results.json`（Qwen3 n=355）

| Config | StyleOR(论文) | StyleOR(源) | Sp(论文) | Sp(源) | OrigOR(论文) | OrigOR(源) | Op(论文) | Op(源) | 状态 |
|--------|-------------|-------------|---------|-------|-------------|-------------|---------|-------|------|
| Qwen3 verb | 13.10 | 13.101 | <.0001 | 0.0 | 0.49 | 0.491 | .096 | 0.0963 | ✓ |
| GPT-4o verb | 11.34 | 11.344 | <.0001 | 0.0 | 0.45 | 0.452 | .062 | 0.0616 | ✓ |
| Llama-70B verb | 8.21 | 8.213 | <.0001 | 0.0 | 0.38 | 0.378 | .020 | 0.0196 | ✓ |
| Gemini verb | 8.98 | **9.159** | <.0001 | 1.2e-6 | 0.46 | **0.452** | .061 | **0.057** | ⚠️ JSON不匹配 |
| GPT-4o form | 2.58 | 2.582 | .002 | 0.00217 | 2.32 | 2.324 | .006 | 0.00642 | ✓ |
| Qwen3 form | 4.20 | 4.201 | .0002 | 0.000168 | 4.70 | 4.704 | .0001 | 5.2e-5 | ✓ |
| Qwen3 form^a | 2.15 | 2.1502 | <.0001 | 9.9e-5 | 4.99 | 4.9949 | <.0001 | 0.0 | ✓ |
| Llama-70B form | 4.81 | 4.808 | <.0001 | 3e-6 | 3.12 | 3.118 | .0007 | 0.000746 | ✓ |
| Gemini form | 1.64 | 1.644 | .101 | 0.1008 | 2.51 | 2.508 | .002 | 0.00239 | ✓ |
| GPT-4o reg | 1.88 | 1.876* | .029 | 0.0285* | 2.21 | 2.210* | .006 | 0.0058* | ✓* |
| Qwen3 reg | 1.91 | 1.905 | .046 | 0.04548 | 5.72 | 5.718 | <.0001 | 0.0 | ✓ |
| Llama-70B reg | 3.33 | 3.330 | .0003 | 0.000324 | 3.07 | 3.074 | .0008 | 0.000791 | ✓ |

*GPT-4o reg: gee_interaction_analysis.json 给出略不同的值（style_p=0.0267, orig_p=0.00542），但 registry 值（0.0285, 0.0058）与论文一致。

**Gemini verbosity GEE 问题：** `gemini_flash_fourth_judge.json` 中 style_or=9.159，但论文和 registry 使用 8.98。JSON 文件可能被后续分析覆写。实验 registry 中的值与论文一致，但底层数据文件已不匹配。

**结论：10/12 config 完全验证。Gemini verbosity 存在源文件追溯性缺口（MEDIUM）。GPT-4o register 有两个略不同的源，论文使用 registry 版本（可接受）。**

---

## 图表数据验证

| 图 | 数据源文件 | 数据一致 | 问题 |
|----|-----------|---------|------|
| Fig 3 (forest plot) | `gen_forest_plot.py` 硬编码数据 | ✓ 与 Table 1 完全一致 | BT 值、CI、显著性全部匹配 |
| Fig 5 (GEE decomp) | `gen_gee_decomposition_v2.py` 硬编码 | ✓ 与 Table 2 完全一致 | 包括 Gemini verb 8.98 |
| Fig 6 (cross-bench heatmap) | `gen_cross_benchmark_heatmap_v2.py` | ⚠️ 部分问题 | 见下方详细说明 |
| Fig 4 (power curve) | `gen_power_curve.py` | 未验证底层数据 | 需查 power analysis 源 |

### Figure 6 (heatmap) 详细检查

脚本中硬编码数据 vs 源文件交叉验证：

| Judge | Cell | Heatmap值 | 可追溯源 | 状态 |
|-------|------|----------|---------|------|
| GPT-4o | LLMBar Form | .630 | nli_sweep 0.6302 | ✓ |
| GPT-4o | LLMBar Verb | .760 | nli_sweep 0.7602 | ✓ |
| GPT-4o | LLMBar Reg | .570 | registry 0.5699 | ✓ |
| GPT-4o | AEval Form | .727 | registry gpt4o_alpacaeval bt=0.727 | ✓ |
| GPT-4o | MTB Form | .692 | registry gpt4o_mtbench bt=0.692 | ✓ |
| Qwen3 | LLMBar Form | .665 | nli_ablation 0.6647 | ✓ |
| Qwen3 | LLMBar Verb | .773 | nli_ablation 0.7732 | ✓ |
| Qwen3 | LLMBar Reg | .553 | cross_axis 0.553 | ✓ |
| Qwen3 | AEval Form | .657 | 需追溯 | ？ |
| Qwen3 | AEval Verb | .841 | registry alpacaeval_verbosity bt=0.841 | ✓ |
| Qwen3 | MTB Form | .712 | 需追溯 | ？ |
| Llama-70B | LLMBar Form | .695 | third_judge 0.6946 | ✓ |
| Llama-70B | LLMBar Verb | .735 | third_judge 0.7349 | ✓ |
| Llama-70B | LLMBar Reg | .635 | register_summary 0.6353 | ✓ |
| Llama-70B | AEval Form | .756 | 论文正文说75.0%，差0.6pp | ⚠️ |
| Claude | LLMBar Form | .562 | tost 0.562 | ✓ |
| Claude | LLMBar Verb | .541 | tost 0.541 | ✓ |
| Claude | AEval Form | .698 | 需追溯 | ？ |
| Claude | AEval Verb | .683 | 需追溯 | ？ |
| Claude | MTB Form | .733 | 需追溯 | ？ |

---

## Analysis 数字追溯表

| # | 行 | 数字 | 出处 | 状态 |
|---|-----|------|------|------|
| 1 | L8 | α = 0.05 | 方法论设定 | ✓ |
| 2 | L12 | L2 regularization α = 10^-6 | choix 默认参数 | ✓ |
| 3 | L13 | formal-origin 88.9% vs casual-origin 52.6% | bt_model_diagnostics.json stratified_bt formality: 24/27=0.889, 10/19=0.526 | ✓ |
| 4 | L13 | Fisher p = 0.015 | bt_model_diagnostics.json fisher_p=0.014644 → .015 | ✓ |
| 5 | L14 | 10,000 pair-level resamples, seed 42 | nli_threshold_sweep.json seed=42, n_bootstrap=10000 | ✓ |
| 6 | L15 | α̂ ∈ [-0.25, +0.11] | 需查 GEE diagnostics appendix | ？ |
| 7 | L16 | n = 86–88 pairs | table1_verified: form=88, verb=86 | ✓ |
| 8 | L16 | >90% power, P ≥ 0.63 | 需查 power_analysis appendix | ？ |
| 9 | L16 | 4–206× sample size | 需查 power_analysis appendix | ？ |
| 10 | L53 | formal-origin 78.8% vs casual-origin 54.5% | 不同于 L13 的 88.9%/52.6% — L53 使用 ALL pairs, L13 使用 consistent-only | 需验证 |
| 11 | L53 | GEE Style OR = 2.58 (p=.002) | gee_interaction GPT-4o form: 2.582, p=0.002167 | ✓ |
| 12 | L52 | 22% lower Style OR | verbosity rewriter: 10.17/13.10=0.776 → 22.4% reduction | ✓ |
| 13 | L73 | d = −0.04, p = 0.91 (n=88) | table1_verified GPT-4o form: d=-0.0417→-.04, p=0.9054→.91 | ✓ |
| 14 | L73 | 63.0% (p=0.0004, 173 comparisons) | registry exp016_bt: p_formal=0.63, p=0.0004, n_comp=173 | ✓ |
| 15 | L73 | 73.9%, p=0.006, n=46 | **⚠️ p值来源混淆** — n=46时p=0.0015, p=0.006来自n=55分析 | **MEDIUM** |
| 16 | L75 | n=355, d=−0.025, BT 67.5% (p<0.0001) | registry exp-006: bt=0.675, d=-0.025, p=0.0001 | ✓ |
| 17 | L79 | tie rates 58–73% | table1_verified: 三主judge verb 58.1%–form 72.7% | ✓ |
| 18 | L79 | all three judges p > 0.15 (100pt) | **⚠️** GPT-4o verb 100pt: wilcoxon_p=0.067, t_p=0.117，均<0.15 | **MEDIUM** |
| 19 | L85 | 4–206× current n (336–27,159) | appendix power analysis，未在本审计范围验证 | ？ |
| 20 | L86 | 8/8 Blindspot, binomial p=0.004 | 0.5^8 = 0.0039 ≈ 0.004 | ✓ |
| 21 | L86 | non-tie concordance 76.6%, p<.001 | construct_divergence pooled: rate=0.7662, binom_p=0.0 | ✓ |
| 22 | L90 | r = 0.20–0.45, 7/9 significant | construct_divergence correlation: range 0.2026–0.4465, 7/9 sig | ✓ |
| 23 | L91 | Claude AEval verbosity Style OR = 4.76, p<.001 | 需查 Claude cross-benchmark GEE 源 | ？ |
| 24 | L106 | GPT-4o OR=2.58 p=0.002; Qwen3 OR=2.15 p<.0001 n=355; Llama OR=4.81 p<.0001 | 与 Table 2 一致，已验证 | ✓ |
| 25 | L140 | n=330: Style OR 2.5–4.0 | registry verb_scaled: gemini 2.52, qwen 3.83, llama 4.01 → 2.5–4.0 | ✓ |
| 26 | L142 | Gemini Style OR = 1.64, n.s. | gemini_json: 1.6436, p=0.1008 (n.s.) | ✓ |
| 27 | L152 | Style OR 4.20→2.15 (−49%), Orig OR 4.70→4.99 | gee_n355: (4.2008-2.1502)/4.2008=48.8%→49% | ✓ |
| 28 | L153 | 51–72% GEE shrinkage (Style OR 2.5–4.0) | registry: qwen 70.8%, llama 51.2% → 51–71% | ⚠️ 论文72% vs 源71% |
| 29 | L159 | Qwen3 BT 66.5% p<0.0001, Likert p=0.461 | nli_ablation/table1_verified 一致 | ✓ |
| 30 | L159 | Llama BT 69.5% p=0.0001, Likert p=0.534 | third_judge/table1_verified 一致 | ✓ |
| 31 | L160 | Gemini BT 57.4% p=0.031 | registry: bt_p=0.0306→.031 ✓; JSON: bt_p=0.0448 ✗ | ✓ (registry源) |
| 32 | L161 | Claude BT ≤ 0.562, n.s. | tost: form 0.562 p=0.09, verb 0.541 p=0.28 | ✓ |
| 33 | L163 | GPT-4o 76.0%, Qwen3 77.3%, Llama 73.5%, Gemini 70.8% | debiased_gpt4o 76.0; nli_ablation 77.3; third_judge 73.5; gemini_json 70.8 | ✓ |
| 34 | L163 | Likert p = 0.284–0.403 | table1_verified verb p: 0.284–0.403 | ✓ |
| 35 | L164 | Style OR 8.2–13.1, Orig OR 0.38–0.49 | Table 2 已验证 | ✓ |
| 36 | L165 | 90.7%/80.6% (both directions verbose) | **⚠️** bt_model_diagnostics: 91.2%/82.8% | **MEDIUM** |
| 37 | L166 | 60% mediated by sentence length | fk_length_control coef_reduction_pct=60.33% | ✓ |
| 38 | L166 | Sobel z = 2.15, p = .031 | **fk_length_control: z=3.5953, p=0.000324** | **HIGH** |
| 39 | L166 | direct-effect Style OR = 2.15 for GPT-4o (total OR = 2.70) | **找不到出处** — GPT-4o form Style OR=2.58，不是2.70 | **HIGH** |
| 40 | L168 | Llama-70B AEval BT 75.0%, Style OR=7.64 | heatmap=0.756(75.6%); crossbench_summary degenerate GEE; **OR=7.64 无法追溯** | **HIGH** |
| 41 | L182 | 98.6% precision (69/70), Gwet's AC1=0.96 | 人工标注研究，需验证 annotation_sheet 源 | ？ |
| 42 | L184 | ≤3pp variation across 11 NLI thresholds | nli_threshold_sweep: ranges 1.7–2.8pp | ✓ |
| 43 | L185 | 49–66% detectable style change | 人工标注结果，需验证 | ？ |
| 44 | L190 | NLI-fail BT 41.7% | nli_gate_ablation form nli_fail bt=0.4168 | ✓ |
| 45 | L190 | debiased −5.2/−13.1pp | Llama form: 69.5-64.3=5.2pp ✓; GPT-4o verb: 76.0-62.9=13.1pp ✓ | ✓ |
| 46 | L190 | ~9–17% amplification | 计算逻辑需确认，基数不明确 | ？ |

---

## 问题清单

| # | 位置 | 问题描述 | 严重度 | 建议修复 |
|---|------|----------|--------|----------|
| 1 | L166 | **Sobel z/p 值错误**：论文写 z=2.15, p=.031，源文件 fk_length_control_results.json 记录 z=3.5953, p=0.000324。相差悬殊，非四舍五入问题。可能将 Style OR 2.15 误抄为 Sobel z。 | **HIGH** | 更正为 z=3.60, p<.001（或重新运行分析确认） |
| 2 | L166 | **"direct-effect Style OR=2.15 for GPT-4o (total OR=2.70)" 无出处**：GPT-4o formality Style OR=2.58（Table 2），不是 2.70。2.15 恰好等于 Qwen3 n=355 Style OR。可能是 judge 混淆。 | **HIGH** | 确认是否应为 Qwen3 数据或 GPT-4o 长度控制后 GEE 的结果，提供正确出处 |
| 3 | L168 | **Llama-70B AlpacaEval "Style OR=7.64" 无法追溯**：crossbench_summary 记录 GEE 为 "degenerate"（近完美分离）。7.64 找不到任何源文件。BT 75.0% 与 heatmap 75.6% 也有 0.6pp 偏差。 | **HIGH** | 找到 7.64 的计算脚本或删除该数字；统一 BT 为 heatmap 值 75.6% |
| 4 | L73 | **sign test p 值来源混淆**：论文写 "73.9%, p=0.006, n=46"，但 n=46 的 sign test p=0.0015（registry）。p=0.006 来自另一个分析（n=55，无 NLI 过滤）。同一句中混用了两个不同分析的数字。 | **MEDIUM** | 统一为 n=46 对应 p=0.002（双侧）或 n=55 对应 p=0.006 |
| 5 | L165 | **verbosity 双方向百分比**：论文写 90.7%/80.6%，bt_model_diagnostics.json 记录 91.2%/82.8%（Qwen3-32B consistent-filtered）。可能来自不同 judge 或分析。 | **MEDIUM** | 确认使用哪个 judge 的数据，更正为源值或注明 judge |
| 6 | Table 2 Gemini verb | **Gemini verbosity GEE 底层文件不匹配**：gemini_flash_fourth_judge.json 有 Style OR=9.16，论文/registry 使用 8.98。底层 JSON 可能被后续分析覆写。论文值与 registry 一致但与当前 JSON 不一致。 | **MEDIUM** | 确认 8.98 的来源并固化，或更新为最新 JSON 值 9.16 |
| 7 | L79 | **100pt scaling "all three judges p>0.15"**：GPT-4o verbosity 100pt 的 wilcoxon_p=0.067, t_p=0.117，均<0.15。如果指所有 judge × 轴 组合则不成立。 | **MEDIUM** | 确认是否仅指 formality（form 的 p=0.725/0.900 确实>0.15），改为 "formality: all three judges p>0.15" |
| 8 | Table 1 | **两个 d 值四舍五入不一致**：GPT-4o form d=-0.0417→应为-.042 但写-.041；Claude verb d=-0.0397→应为-.040 但写-.039。使用了截断而非四舍五入。 | **LOW** | 统一使用四舍五入（-.042, -.040）或注明截断规则 |
| 9 | L168 | **Llama-70B AEval BT 文字 vs 图表**：正文写 75.0%，heatmap 脚本为 0.756 (75.6%)。 | **LOW** | 统一为 heatmap 值 75.6% |
| 10 | L153 | **"51–72% shrinkage" 上界**：源数据 qwen 70.8%, llama 51.2%，范围应为 51–71%。论文写 72%。 | **LOW** | 更正为 51–71% |

---

## 找不到出处的数字

| # | 位置 | 数字 | 处理建议 |
|---|------|------|----------|
| 1 | L166 | Sobel z=2.15, p=.031 | 源文件有 z=3.60, p=0.0003。**必须更正。** |
| 2 | L166 | direct-effect Style OR=2.15 (GPT-4o), total OR=2.70 | 找不到 GPT-4o 长度控制 GEE 的结果文件。可能在未保存的分析中。**需补充出处或删除。** |
| 3 | L168 | Llama-70B AlpacaEval Style OR=7.64 | crossbench_summary 中 GEE 为 degenerate。7.64 无任何源文件。**需找到计算脚本或删除。** |
| 4 | L91 | Claude AEval verbosity Style OR=4.76, p<.001 | 可能在 Claude cross-benchmark 结果中，未在本审计范围内定位到精确源文件 |
| 5 | L53 | formal-origin 78.8% vs casual-origin 54.5% | 与 L13 (88.9%/52.6%) 不同。L53 可能用 ALL pairs，L13 用 consistent-only。需确认来源 |
| 6 | L15 | α̂ ∈ [-0.25, +0.11] | GEE diagnostics appendix 数据，未在本审计范围验证 |
| 7 | L165 | 90.7%/80.6% | bt_model_diagnostics 有 91.2%/82.8%。可能来自不同 judge 或不同 pair 集 |
| 8 | L190 | ~9–17% amplification | 计算基数不明确 |

---

## 内部一致性检查

### 同一数字在论文多处出现

| 数字 | 出现位置 | 一致？ |
|------|---------|--------|
| Qwen3 Form BT 66.5% | Table 1 (.665), L159 (66.5%) | ✓ |
| Llama Form BT 69.5% | Table 1 (.695), L159 (69.5%) | ✓ |
| GPT-4o Verb BT 76.0% | Table 1 (.760), L163 (76.0%) | ✓ |
| Qwen3 n=355 BT 67.5% | Table 1 (.675), L75 (67.5%) | ✓ |
| Qwen3 n=355 d=-.025 | Table 1 (-.025), L75 (−0.025) | ✓ |
| Style OR GPT-4o form 2.58 | Table 2 (2.58), L106 (2.58), L53 (2.58) | ✓ |
| Style OR Qwen3 n=355 2.15 | Table 2 (2.15), L106 (2.15), L152 (2.15) | ✓ |
| Style OR Llama form 4.81 | Table 2 (4.81), L106 (4.81) | ✓ |
| Style OR Gemini form 1.64 | Table 2 (1.64), L142 (1.64), L160 (1.64) | ✓ |
| Orig OR Gemini form 2.51 | Table 2 (2.51), L160 (2.51) | ✓ |
| Gemini form BT 57.4% | Table 1 (.574), L160 (57.4%) | ✓ |
| Claude BT ≤ 0.562 | Table 1 (.562/.541), L161 (≤0.562) | ✓ |
| NLI-fail BT 41.7% | L190 (41.7%) | 与 nli_gate_ablation 0.4168 ✓ |
| Direction asymmetry L13 vs L53 | L13: 88.9%/52.6%, L53: 78.8%/54.5% | ⚠️ 不同分析，但论文未解释差异 |

### Figure 数据 vs Table 数据

| 比较 | 一致？ |
|------|--------|
| Forest plot BT vs Table 1 BT | ✓ 完全一致 |
| GEE decomp figure vs Table 2 | ✓ 完全一致（包括 Gemini 8.98） |
| Heatmap vs Table 1 (LLMBar cells) | ✓ |

---

## 审计方法

1. 从 experiments.tex 逐行提取所有数字
2. SSH 到 westb-29275 读取 `/root/causal_style_decomp_judge/data/` 下的 JSON/CSV 源文件
3. 通过 read_registry 获取 58 个实验的完整 metrics 作为交叉验证
4. 读取 `docs/paper/figures/` 下的 Python 脚本验证硬编码数据
5. 对每个数字标注出处文件路径和具体字段

## 数据文件清单

| 文件 | 验证内容 |
|------|---------|
| `analysis/table1_verified.csv` | Table 1 所有 Likert d/p/tie_rate |
| `data/nli_threshold_sweep.json` | GPT-4o/Qwen3 BT across thresholds |
| `data/nli_gate_ablation.json` | Qwen3 formality/verbosity BT + NLI ablation |
| `data/gemini_flash_fourth_judge.json` | Gemini BT/Likert/GEE |
| `data/llama70b_third_judge.json` | Llama-70B BT/Likert/GEE |
| `data/llama70b_register_summary.json` | Llama-70B register BT/GEE |
| `data/gee_interaction_analysis.json` | GPT-4o/Qwen3/Llama GEE with interaction |
| `data/gee_n355_results.json` | Qwen3 formality n=88 vs n=355 GEE |
| `data/claude_tost_equivalence.json` | Claude BT/TOST |
| `data/bt_model_diagnostics.json` | Direction asymmetry, GoF |
| `data/fk_length_control_results.json` | FK mediation analysis, Sobel test |
| `data/debiased_verbosity_gpt4o_summary.json` | GPT-4o debiased BT |
| `data/debiased_llama70b_summary.json` | Llama-70B debiased BT |
| `data/cross_axis_gradient.json` | Qwen3 register BT |
| `data/bootstrap_attenuation.json` | d attenuation curves |
| `data/finegrained_likert_100pt.json` | 100-point scaling results |
| `artifacts/r16_analysis/construct_divergence_analysis.json` | Concordance/correlation data |
| `data/gpt4o_rewriter_formality_results.json` | Rewriter independence |
| `data/llama70b_crossbench_summary.json` | Cross-benchmark Llama-70B |
| `data/verbosity_7method_sensitivity.json` | 7-method sensitivity |
| Registry (58 experiments) | 全部实验 metrics 交叉验证 |
