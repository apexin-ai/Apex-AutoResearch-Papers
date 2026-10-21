# Paper Completeness Check — trace-verdict-study
**Date**: 2026-05-16 | **Target**: EMNLP 2026 Main (ARR May 25, DDL in 9 days)
**Paper location**: `docs/paper/`

---

## 1. Section-by-Section Status

### ✅ Abstract (main.tex)
- All headline numbers present: 99.83% ± 0.00, 14.96pp gap, 26%/74% decomposition, ≥99.8% Tier 1, 85.6% Tier 2
- Numbers match registry and paper_framing.md

### ✅ Introduction (introduction.tex, 26 lines)
- Motivation (DCSH inconsistency, TracePile generation-only), reframing as fault detection, 3 contributions
- Numbers match: 99.83%, 99.33%, 91.09%, 84.45%, 6.64pp, 14.96pp, 26%/74%
- Well-structured: DCSH quote → gap → our framing → headline → contributions

### ✅ Method (method.tex, 63 lines)
- Task definition, dataset (591 problems, 5910 pairs, 4720/1190 split), 7 conditions defined
- Figure 1 reference (fig1_trace_overview) ✅ figure file exists
- Two models described, training setup (LoRA r=16, 3 epochs, 2048 max), loss ablation explained
- Deduplication stats mentioned with appendix pointer

### ✅ Experiments (experiments.tex, 135 lines)
- 4.1 Cross-Model: Table 1 ✅ with DeepSeek full_trace v3 = 79.16% (gap 2.60pp)
- 4.2 Component Ablation: Table 2 ✅ with regex baseline 93.61%
- 4.3 Information Density: Table 3 ✅ (26%/74% decomposition)
- 4.4 Trace Length Ablation: ✅ (256/512/1024/no_limit, appendix pointer)
- 4.5 Calibration: ✅ (ECE 0.0027, Brier 0.0013, appendix pointer)
- 4.6 DebugBench: ✅ (100%/99.77%/96.71%, appendix pointer)

### ⚠️ Discussion (discussion.tex, 26 lines)
- Fault detection framing ✅
- Regex baseline context (93.61% vs 99.33% format marker) ✅
- Limitations subsection ✅ (6 limitations listed)
- **Missing from main text** (only in appendix):
  - D1: eval_loss vs accuracy decoupling (token-level loss ≠ task accuracy)
  - D2: CRUXEval gap hypothesis (VOTA gap ∝ execution reasoning gap)
  - D9: LoRA init sensitivity as finding (training stability recommendation)
  - D11: Truncation as causal factor (group analysis evidence)
- Discussion 偏短 (~0.5 page)，paper_framing.md 中 11 个 Discussion points 大部分只在 appendix

### ✅ Related Work (related_work.tex, 29 lines)
- 3 paragraphs: Execution traces for Code LLMs, Code verdict/patch classification, Trace compression
- 15+ citations, positions against DCSH/TracePile/TRACED/NExT/ET-CoT/TraceCoder/InspectCoder
- Final sentence bridges to our contribution

### ✅ Conclusion (conclusion.tex, 22 lines)
- 3 findings restated with numbers
- DebugBench generalization mentioned
- Future work: more datasets, model scales, classification tasks
- Design principle stated

### ✅ Appendix (appendix.tex, 431 lines)
- A. Per-Class Breakdown (Table 4) ✅
- B. Training Details (Table 5 hyperparams, Table 6 wall-clock) ✅
- C. VOTA Trace Examples (fail + pass) ✅
- D. Full Results (Table 7 Qwen, Table 8 DeepSeek) ✅
- E. Irreducible Sample Analysis ✅
- F. Trace Length Ablation (Table 9 + Figure 4) ✅
- G. Calibration Analysis (Table 10 + Figure 2) ✅
- H. DebugBench (Table 11) ✅
- I. Cross-Model Robustness Analysis ✅
- J. Training Dynamics and Loss Decoupling ✅
- K. Deduplication Statistics (Table 12) ✅
- L. Regex Baseline Analysis (Table 13) ✅

---

## 2. Tables & Figures

### Tables (all present)
| ID | Content | Location | Status |
|----|---------|----------|--------|
| Table 1 | Cross-model comparison (4 conditions × 2 models) | experiments.tex | ✅ DeepSeek full_trace = 79.16% filled |
| Table 2 | Component ablation (7 conditions + regex) | experiments.tex | ✅ |
| Table 3 | Information density decomposition | experiments.tex | ✅ |
| Table 4 | Per-class precision/recall/F1 | appendix | ✅ |
| Table 5 | Training hyperparameters | appendix | ✅ |
| Table 6 | Training wall-clock time | appendix | ✅ |
| Table 7 | Full Qwen results (all seeds) | appendix | ✅ |
| Table 8 | Full DeepSeek results (all seeds) | appendix | ✅ |
| Table 9 | Trace length ablation | appendix | ✅ |
| Table 10 | Calibration metrics (ECE, Brier) | appendix | ✅ |
| Table 11 | DebugBench cross-dataset | appendix | ✅ |
| Table 12 | Deduplication statistics | appendix | ✅ |
| Table 13 | Regex baseline analysis | appendix | ✅ |

### Figures
| ID | Content | File | Status |
|----|---------|------|--------|
| Figure 1 | VOTA trace overview pipeline | fig1_trace_overview.pdf | ✅ |
| Figure 2 | Calibration reliability diagram | fig2_calibration.pdf | ✅ (in appendix) |
| Figure 3 | Cross-model accuracy gap | fig3_cross_model_gap.pdf | ✅ (in appendix) |
| Figure 4 | Trace length ablation | fig4_trace_length.pdf | ✅ (in appendix) |

**Note**: writing_plan.yaml 计划了 5 个 figures (fig_1 through fig_5)。实际论文只有 4 个，且除 Figure 1 外全在 appendix。正文 Experiments 部分无独立 figure — 全部依赖 tables。这对 visual communication 偏弱，但版面紧凑。

---

## 3. Key Data Cross-Check (Paper vs Registry)

| Data Point | Paper Value | Registry Value | Match |
|------------|-------------|----------------|-------|
| exception_only (Qwen, seed42) | 99.83% | 99.83% | ✅ |
| exception_only (Qwen, seed123) | 99.83% | 99.83% | ✅ |
| exception_only (Qwen, seed456) | 99.83% | 99.83% | ✅ |
| ae_only (Qwen) | 99.92% | 99.92% | ✅ |
| VOTA (Qwen) | 99.41% | 99.41% | ✅ |
| VOTA_no_ae (Qwen) | 99.41% | 99.40% | ⚠️ rounding (99.405→99.41 in paper) |
| loop_only (Qwen) | 85.63% | 85.63% | ✅ |
| full_trace (Qwen) | 81.76% | 81.76% | ✅ |
| label_only (Qwen) | 86.22% | 86.22% | ✅ |
| no_trace (Qwen) | 75.13% | 75.13% | ✅ |
| exception_only (DS, seed42) | 99.33% | 99.33% | ✅ |
| exception_only (DS, seed123) | 91.09% | 91.09% | ✅ |
| exception_only (DS, seed456) | 99.33% | 99.33% | ✅ |
| VOTA (DS) | 84.45% | 84.45% | ✅ |
| no_trace (DS) | 73.36% | 73.36% | ✅ |
| full_trace (DS, v3) | 79.16% | 79.16% | ✅ |
| DebugBench exception_only | 100% | 100% | ✅ |
| DebugBench VOTA | 99.77% | 99.77% | ✅ |
| DebugBench no_trace | 96.71% | 96.71% | ✅ |
| Regex B4 | 93.61% | 93.61% | ✅ |
| full_trace 1024tok | 77.23% | 77.23% | ✅ |
| Trace length 256/512 | 78.82%/80.42% | Not in registry | ⚠️ Source unclear |

---

## 4. Pending Experiments

| Experiment | Status | Impact on Paper |
|------------|--------|-----------------|
| ae_only_seed123 | RUNNING | Non-blocking: only needed if reporting ae_only multi-seed (currently not) |
| ae_only_seed456 | RUNNING | Same as above |
| full_trace_2048tok_seed42 | Killed | ⚠️ Trace length ablation uses 256/512/1024/∞ — where did 256 and 512 come from? Not in registry. Need provenance verification |

---

## 5. Page Count Estimate

| Component | Pages |
|-----------|-------|
| Title + Abstract | ~0.5 |
| Introduction | ~1.2 |
| Method | ~1.5 |
| Experiments | ~3.0 |
| Discussion (+ Limitations) | ~0.7 |
| Related Work | ~0.7 |
| Conclusion | ~0.5 |
| **Body subtotal** | **~8.1** |
| References | ~1.0 |
| Appendix | ~6.0 |

**Compiled PDF: 14 pages total.** Body 约 7-8 页（从 log 看正文结束在 page 7，bibliography 跨 page 7-8）。EMNLP 8 页限制含正文不含 references — **刚好在边界，需精确确认 references 是否算在 8 页内**。

ARR format: **8 pages + unlimited references + unlimited appendix**. References 不计入 8 页。正文约 7 页，留有约 1 页余量。

---

## 6. Missing / Incomplete Items

### ❌ Missing Items
1. **Ethics Statement**: EMNLP ARR 要求 ethics statement（即使只是 "No ethical concerns"）
2. **Reproducibility Checklist**: ARR submission 需要填写 reproducibility checklist (separate form)
3. **Code/Data availability statement**: 未提及是否开源代码/数据

### ⚠️ Partial / Weak Items
4. **Discussion 偏薄**: paper_framing.md 有 11 个 discussion points (D1-D11)，正文只覆盖了核心 fault detection framing + regex context + limitations。关键 findings 如 eval_loss decoupling (D1)、truncation causal evidence (D11) 只在 appendix，减弱了 contribution 感知
5. **正文无 figure**: 除 Figure 1 (method 图) 外，所有 figure 都在 appendix。正文 Experiments 全靠 tables，visual appeal 弱。考虑将 fig3 (cross-model gap) 或 fig2 (calibration) 移入正文
6. **Trace length ablation 256/512 数据溯源**: Registry 中只有 1024tok 实验，256 和 512 的数据来源不明，需确认 provenance
7. **Section order**: Related Work 在 Discussion 之后（Section 5），非常规。EMNLP 不强制，但审稿人可能觉得不习惯。考虑移到 Section 2

---

## 7. Paper Agent 下一步 Patch 清单（优先级排序）

### P0 — 提交前必须完成
1. **添加 Ethics Statement** — 在 Conclusion 后加一段。ARR mandatory
2. **确认 trace length 256/512 数据 provenance** — 验证来源，确保可复现
3. **准备 ARR Reproducibility Checklist** — 单独表格，非论文内容

### P1 — 显著提升论文质量
4. **加厚 Discussion section** (~0.3-0.5 page): 从 appendix 提炼关键 findings 到正文:
   - eval_loss vs accuracy decoupling (D1): 1-2 句
   - Truncation as causal factor with group analysis evidence (D11): 2-3 句
   - Training stability recommendation (D9): 1-2 句
5. **正文增加 1 个 figure**: 将 fig3 (cross-model gap bar chart) 移入 §4.1 Cross-Model，替代纯文字描述。增强 visual storytelling
6. **确认 VOTA_no_ae 精度**: paper 99.41% vs registry 99.40% — 确认是 rounding 还是数据不一致

### P2 — 锦上添花
7. **考虑调整 Related Work 位置**: 移到 Section 2 (Method 之前)，更符合 EMNLP 惯例
8. **添加 Code/Data availability 声明**: 在 Ethics Statement 旁或 Conclusion 末尾
9. **检查 bibtex 编译**: 确认所有 \citep/\citet 引用均 resolve（当前编译未见 undefined warnings，但需 bibtex + pdflatex 双重确认）
10. **Appendix statistical tests section**: writing_plan.yaml 提到 "E. Statistical Tests" (McNemar details, CIs)，当前 appendix 无独立 section — 统计细节散布在各 section 中。考虑汇总

### P3 — 可选优化
11. **ae_only_seed123/456 结果整合**: 如训练完成，补入 Table 7 增强 Tier 1 seed robustness 证据
12. **正文精简 Experiments**: 当前 ~3 pages，考虑将 Calibration 和 DebugBench 段落进一步压缩，为 Discussion 腾空间
