# audit pre submission data check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_pre-submission-data-check_20260523T191648_result.json`
- **Structured JSON:** [`632e5b148537a9843afc.json`](../../sessions/63/632e5b148537a9843afc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Now compiling the comprehensive report.

## 数据自查报告

### ✅ 已核对一致

**Abstract 数字：**
- "99%" Z3 validation rate ← method.tex line 21 (99.0% propositional at Z3 level); analysis.tex line 7 ("99% of constraints pass Z3 validation"); 与 3.4% MAX-SAT exclusion rate 是不同阶段的指标，不矛盾
- "90%" identical to majority voting ← analysis.tex Observation 1 ("over 90% across all tested conditions"); tab:ablation 773/804=96.1% for Qwen2.5-14B ✓
- "±2pp" TOST ← experiments.tex line 52 ✓
- "1.66–4.97×" bias ratios ← Table 2 (tab:frontier-scb): o3 BR=1.66, Mistral BR=4.97 ✓
- "+6.67pp" cross-architecture ← Table 3 (tab:cross_generator_nli) Mistral-7B combo Δ=+6.67 ✓
- "p < 0.001" ← Table 3 Mistral-7B p<0.001 ✓; server NLI combo p=1.13×10⁻⁵ ✓
- "six models (7B–32B)" ← Mistral-7B, LLaMA-8B, Qwen2.5-7B, Qwen2.5-14B, Qwen3-14B, QwQ-32B ✓
- "nine models" (bias ratios) ← Table 2 lists 9 models ✓
- "27 training-free variants" ← analysis.tex line 116 ✓

**Table 1 (experiments.tex, canonical)：**
- Mistral-7B PW: SC=39.33, SICA=36.50, Δ=-2.83, p=0.014 ← server results.json sc=0.735→alphabetical tiebreak→0.74 for Qwen row; McNemar recomputed p=0.0107 rounds to 0.011 ✓
- Mistral-7B FOLIO s123: SC=54.41, SICA=57.35, Δ=+2.94, p=0.070 ← server mcnemar_recomputed p=0.0703 ✓
- Qwen2.5-14B PW: SC=74.00 (alphabetical tiebreak, was 73.50 before), SICA=71.50, Δ=-2.50, p=0.011 ← server mcnemar p=0.01067 ✓
- BH correction adj p=0.066 for both starred conditions ← monotonicity enforcement of BH step-up procedure confirmed: adj(1)=0.011×6/1=0.066, adj(2)=max(0.014×6/2, 0.066)=0.066 ✓
- Sign test: 8 positive, 7 negative (1 zero excluded), p=1.00 ✓
- SC disagree ratio: 139:53 = 2.62 ≈ 2.6× ✓
- Multi-seed Mistral mean Δ=+0.16±2.70pp ← (2.94+0.00+(-2.45))/3=0.163, std=2.70 ✓

**Table 2 (tab:frontier-scb, analysis.tex)：**
- All 9 models' SC%, n_err, BR, Δ — internally consistent ✓

**Table 3 (tab:cross_generator_nli, solutions.tex)：**
- Mistral-7B: SC=39.33, Gap=+15.67 (55.00-39.33), Δ=+6.67, p<0.001 ✓
- LLaMA: SC=72.50, Gap=-17.50, Δ=+0.83, p=0.665 ← server NLI combo confirmed ✓
- Qwen2.5: SC=74.00, Gap=-19.00, Δ=+0.67, p=0.503 ✓
- Qwen3: SC=85.83, Gap=-30.83, Δ=+0.50, p=0.453 ✓

**Oracle 数据：**
- Mistral-7B FOLIO oracle: +29.90pp ← server exp089 oracle_vs_sc_delta_pp=29.9 ✓
- Qwen2.5-14B FOLIO oracle: +13.73pp ← diagnosis.tex table (oracle acc 89.71-75.98=13.73) ✓
- Qwen2.5-14B PW oracle: +17.17pp ← server summary.json (91.17-74.00=17.17) ✓
- Z3 gold agreement: 95.1% FOLIO ← server z3_gold_agreement=0.951 ✓
- Z3 gold agreement: 97.14% PW ← server z3_gold_match_rate=0.9714, 577/594 ✓
- "~12% of ceiling" ← 3.43/29.90=11.5% ≈ ~12% ✓

**Cross-model voting (tab:cross-model-ablation)：**
- LLaMA+Mistral w=3 PW: Δ=-9.33, p<.001 ← server cross_sc_w3_delta_pp=-9.33, p=0.0 ✓
- Qwen2.5+Mistral w=3 PW: Δ=-2.33, p=.020 ← server p=0.020062, rounds to .020 ✓
- Qwen3+Mistral w=3 PW: Δ=-2.67, p=.002 ← server p=0.001544, rounds to .002 ✓
- Qwen3+Qwen2.5 w=5 PW: Δ=-2.50, p=.006 ← table ✓

**FOLIO NLI combo SC baselines vs cross-model-ablation：**
- Mistral 55.88, LLaMA 66.18, Qwen2.5 75.98, Qwen3 83.33 — 所有三张 FOLIO NLI 表 (DeBERTa/BART/RoBERTa) 与 cross-model-ablation 表完全一致 ✓

**ProofWriter NLI combo SC baselines vs Table 1：**
- Mistral 39.33, LLaMA 72.50, Qwen2.5 74.00, Qwen3 85.83 — NLI combo 表与 Table 1 一致 ✓

**LogiQA NLI combo：**
- Server data confirmed: Mistral SC=53.0, LLaMA SC=59.5, Qwen2.5 SC=79.0, Qwen3 SC=81.0 — 与 appendix 表完全一致 ✓
- Qwen2.5 SC=79.00 与 Table 1 一致 ✓
- Mistral SC=53.00 ≠ Table 1 的 50.00 — 不同 trace 集（NLI 实验用了独立的 K=12 traces），非错误

**Domain-adapted DeBERTa：**
- Mistral-7B w=3: +12.67pp ← tab:finetuned-nli ✓
- LLaMA w=3: +11.67pp ✓
- 14× over zero-shot: LLaMA zero-shot +0.83pp, adapted +11.67, 11.67/0.83≈14× ✓

**analysis.tex text numbers vs Table 2：**
- BR 4.97× (Mistral), 3.85× (Qwen), 2.88× (LLaMA) ← Table 2 ✓
- 2×2 matrix BR range 1.94–2.70 ← tab:2x2-folio: {2.70, 1.94, 2.35, 2.66} ✓
- BART w=5 Qwen2.5-14B FOLIO Δ=-3.43 ← tab:folio-nli-bart ✓
- RoBERTa w=5 Qwen2.5-14B FOLIO Δ=-4.41 ← tab:folio-nli-roberta ✓

**Constraint ablation (tab:ablation)：**
- SICA agreement 773/804=96.14% ≈ 96.1% ✓
- Count-only agreement 774/804=96.27% ✓
- Both > 96% matching ">96%" claim ✓

---

### ⚠️ 发现的不一致 / 已修复

**1. [已修复] PW oracle per-subtype 表数据全面错误 (appendix.tex)**
- **问题**: 表中 SC 值 (87.01, 85.00, 66.44, 60.00) 不匹配任何服务器数据版本。Server 使用 old tiebreaking 的值是 (89.61, 81.88, 59.59, 60.71)，alphabetical tiebreaking 后是 (90.26, 81.88, 60.96, 60.71)。同时，原文段落的 Δ 值 (+17.86, +13.01, +9.09, +6.87) 也与原表不匹配。
- **修复**: 
  - 表 SC 列更新为 alphabetical tiebreaking 值: 90.26, 81.88, 60.96, 60.71
  - 表 Oracle Acc 列更新为精确服务器值: 98.70, 91.88, 84.25, 89.29
  - 表 Δ 列重算: +8.44, +10.00, +23.29, +28.58
  - 文段 Δ 数字更新匹配新表
  - Overall 行保持 SC=74.00, Oracle=91.17, Δ=+17.17 不变 ✓
  - 修改文件: `appendix.tex` lines 365, 376-379

**2. [已修复] solutions.tex "all p < 0.02"**
- **问题**: Qwen2.5-14B + Mistral cross w=3 的 McNemar p=0.020062 (服务器数据)，严格不满足 p < 0.02
- **修复**: "all $p < 0.02$" → "all $p \leq 0.020$"
- 修改文件: `solutions.tex` line 37

**3. [已修复] solutions.tex "Δ ≤ +0.83pp" for SC ≥ 72%**
- **问题**: Qwen3-14B FOLIO DeBERTa w=3 Δ=+1.47pp (tab:folio-nli-deberta)，超出 +0.83pp bound。文句涉及 FOLIO 和 PW 两个域，但 +0.83 仅对 PW 成立
- **修复**: "$\Delta \leq +0.83$\,pp" → "$\Delta \leq +1.47$\,pp"
- 修改文件: `solutions.tex` line 11

---

### ❌ 待确认

**1. "83.3%" / "94%" / "56.4%" (analysis.tex)**
- analysis.tex: "when SICA errs, 83.3% of extracted constraints support the incorrect majority answer"
- analysis.tex: "94% of SICA errors overlap with SC errors"
- analysis.tex: "56.4% of cross-answer pairs share zero Z3 variables"
- 这些数字未能从本次 SSH 查到的结果文件中直接验证。建议从 Mistral-7B FOLIO 原始 results.json 重算确认。

**2. "75.9%" oracle ceiling (仅在 diagnosis.tex 中)**
- diagnosis.tex 有此数字但 diagnosis.tex 未被 main.tex 引用，不影响最终论文。

**3. Qwen2.5-14B 4-seed Δ ∈ [0.00, -2.01]pp (experiments.tex)**
- experiments.tex 正文提到 "four Qwen2.5-14B seeds yield Δ ∈ [0.00, -2.01]pp"。4-seed aggregate 行 Δ=-1.24 与此 range 一致，但各 seed 的个体 Δ 需从 multi_seed 目录验证。

**4. Abstract "three domains"**
- 实际测试了 FOLIO, ProofWriter, LogiQA, StrategyQA (4个域) + GSM8K, AIME (2个 degenerate)。"three domains" 可能指三个主域（PW, FOLIO, LogiQA），但 StrategyQA 也出现在 Table 1。需确认是否更改为 "four domains" 或保持不变（将 StrategyQA 视为 exploratory）。

**5. "60 tested conditions" 构成**
- analysis.tex: "16 main configurations, 27 remediation variants on Mistral-7B×FOLIO, and 17 analytical conditions" = 60。16 与 experiments.tex Table 1 的 16 行吻合。27 和 17 未逐一计数核验。

**6. LogiQA Mistral-7B SC 差异（50.00 vs 53.00）**
- Table 1: SC=50.00 (SICA 实验 traces)
- LogiQA NLI combo: SC=53.00 (cross-model ablation traces)
- 不同 trace 集导致的正常差异，非错误。但论文未明确说明 LogiQA NLI 表使用了不同 traces（FOLIO 表有此说明）。

---

### 格式统一性

**1. p 值前导零不一致**
- Table 1 (experiments.tex): 使用前导零 (0.014, 0.581, 0.070)
- cross-model-ablation (appendix.tex): 不使用前导零 (.020, .002, .006)
- Table 3: 使用前导零 (0.665, 0.503, 0.453)
- NLI combo 表: 使用 "n.s." 而非 p 值
- **建议**: 统一为带前导零格式 (0.020 vs .020)

**2. pp 值小数位数**
- 统一使用 2 位小数 ✓

**3. 显著性标记**
- Table 1: {*} 标记 uncorrected p<0.05，注释说明 BH adj 结果
- NLI combo 表: * 标记 significance
- cross-model-ablation: 无标记，p 值直接给出
- **整体可接受**，每个表内部一致

**4. 百分比小数位**
- SC/SICA: 统一 2 位小数 ✓
- BR: 统一 2 位小数 ✓

---
