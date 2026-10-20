# Round 25 Submission Checklist — EMNLP 2026 ARR May

**Target**: EMNLP 2026 Main Conference (score 4.0+), via ARR May cycle  
**Deadline**: 2026-05-25  
**Previous**: R24 score 3.25/5 (borderline)  
**Generated**: 2026-05-20  

---

## 1. Format & Pages

| # | Item | Status | Detail |
|---|------|--------|--------|
| 1.1 | 正文 ≤ 8 页 | ✅ PASS | Main body (§1–§6, Abstract through Conclusion) ends on page 8. Limitations starts bottom of page 8, does not count. **Exactly at limit — no room for additions to main text.** |
| 1.2 | 正确 ARR/EMNLP 模板 | ✅ PASS | `\usepackage[review]{acl}` + `acl.sty` + `acl_natbib.bst`. Review mode with line numbers enabled. |
| 1.3 | 匿名化 | ✅ PASS | `\author{Anonymous}`, "Anonymous ACL submission" header. Code release: `[anonymized URL]`. No "our previous work" or identity-leaking language found. |

## 2. Content Completeness

| # | Item | Status | Detail |
|---|------|--------|--------|
| 2.1 | Abstract 反映最新结果 | ✅ PASS | Abstract correctly reports: ρ up to 0.45, AUROC up to 0.82, +1.40pp Few-NERD, +1.02pp SciERC (multi-seed mean, p<0.005), 72B ZS confirmation, 4B–8B FT + 72B ZS coverage. |
| 2.2 | 无 "??" 占位符 | ✅ PASS | Zero instances of "??" across all tex files. |
| 2.3 | 所有 \cite 解析成功 | ✅ PASS | 72 unique citation keys, all present in `references.bib` (615 lines). |
| 2.4 | 所有 \ref 解析成功 | ⚠️ WARN | 1 undefined ref: `\ref{tab:72b_zs_vs_fs}` on page 36 (appendix §L.5). **Label exists** at appendix line 1661 — forward reference needs second compile pass. Fix: rerun `pdflatex` twice or use `latexmk`. |
| 2.5 | Figure 文件完整 | ✅ PASS | All 8 referenced figures exist as PDF in `docs/paper/figures/`: fig_overview, fig_selection_gap, fig_degeneracy_lp_scatter, fig_temperature_robustness, fig_reliability, fig_signal_heatmap, fig_length_logprob_scatter, fig_lp_range_cdf. |
| 2.6 | §4.6 Scaling 数据 | ⏳ PENDING | **Commented-out scaling curve figure** (`% Figure: scaling_curve (pending data — re-enable when ready)` at experiments.tex:209). Qwen2.5-7B/14B/32B FewNERD experiments still running: |
|   |                    |            | — 7B: seed42 inference ~92% (nearly done), seed123/456 ~51% |
|   |                    |            | — 14B: training 65.5%, ETA ~05-20 20:00 UTC |
|   |                    |            | — 32B: training 47.4%, ETA ~05-21 02:30 UTC |
|   |                    |            | **§4.6 is functional without this data** — already has 72B ZS in Table 5. The 7B/14B/32B curve would strengthen the scaling narrative. |
| 2.7 | Appendix 完整性 | ✅ PASS | 30+ appendix sections covering: notation (A), robustness (B), calibration (C), additional analyses (D), bootstrap CI (E), diversity (F), supervised/hidden probes (G), multi-seed (H), training config (I), thinking tokens (J), LP compression (K), VC quartile (L), RE extension (M), MBR discussion (N), free-form ablation (O), LP failure stability (P), N-scaling (Q), temperature (R), OOD (S), verbalized confidence (T), LLaMA-3B (U), Few-NERD full (V), per-type LP (W), calibration baseline (X), epoch confound (Y), ZS vs FS (Z). All have data. |
| 2.8 | Limitations section | ✅ PASS | Comprehensive: 19 lines covering datasets, languages, scale, regimes, supervised approaches, seed sensitivity, epoch confounds, verbalized confidence, entity-token LP. |
| 2.9 | Ethics Statement | ✅ PASS | Covers: public benchmarks, open-weight models, no new data collection, responsible deployment implications. |
| 2.10 | Responsible NLP Checklist | ✅ PASS | All sections A–E completed (70 lines). Covers limitations, risks, claims, artifacts, licenses, experiments, human subjects, AI assistants. |

## 3. Numerical Consistency

| # | Item | Status | Detail |
|---|------|--------|--------|
| 3.1 | Abstract ↔ Tables | ✅ PASS | "ρ up to 0.45" → Tab 1: EM ρ=0.451 (CoNLL Qwen) ✓ |
|     |                    |         | "AUROC up to 0.82" → Tab 1: EM AUROC=0.816 ✓ |
|     |                    |         | "+1.40pp Few-NERD" → Tab 6: +1.40±0.51pp ✓ |
|     |                    |         | "+1.02pp SciERC" → Tab 6: +1.02±0.49pp ✓ |
|     |                    |         | "+5–8pp F1 at 80% coverage" → §4.7, Tab 12 ✓ |
|     |                    |         | "4B–8B and zero-shot 72B" → Tabs 4, 5 ✓ |
| 3.2 | Main text ↔ Tables | ✅ PASS | Spot-checked: §4.3 "LP +0.2pp (p=0.29)" → Tab 2 ✓; §4.4 "LP +1.39pp (p<0.001)" → Tab 3 ✓; §4.5 "mean |Δρ|=0.042" → Tab 4 ✓; §4.6 "+1.53pp SciERC 72B ZS" → Tab 5 derivable ✓; degeneracy percentages consistent across Tabs 3, 5, 15. |
| 3.3 | Greedy F1 variants explained | ✅ PASS | §3.3 explicitly documents 4 greedy F1 values (0.640/0.644/0.645/0.650) and their protocol origins. Each table specifies its protocol. |

## 4. Typesetting Quality

| # | Item | Status | Detail |
|---|------|--------|--------|
| 4.1 | Overfull hbox | ✅ PASS | 0 overfull hbox warnings in compilation log. |
| 4.2 | Underfull hbox | ⚠️ WARN | ~40 underfull hbox warnings (cosmetic; mostly in appendix dense paragraphs). Not submission-blocking. |
| 4.3 | Float placement | ⚠️ WARN | 4× `'h' float specifier changed to 'ht'` warnings in appendix tables. Cosmetic — LaTeX auto-adjusts. |
| 4.4 | 图表清晰度 | ✅ PASS | All figures are PDF vector graphics. Overview figure (fig_overview) also has PNG fallback. |
| 4.5 | References 格式 | ✅ PASS | Uses `acl_natbib.bst`, standard ACL bibliography style. 615-line bib file. |
| 4.6 | PDF 大小 | ✅ PASS | 790 KB, 37 pages. Well within typical submission limits. |

## 5. Submission Materials

| # | Item | Status | Detail |
|---|------|--------|--------|
| 5.1 | Response letter / revision summary | ⏳ PENDING | **Not found.** If ARR requires a response to R24 reviews for resubmission, this needs to be prepared. R24 score was 3.25 — response should address reviewer concerns and highlight improvements (scaling data, new appendix sections, 72B ZS confirmation). |
| 5.2 | Supplementary materials | ⏳ PENDING | No supplementary package found. "[anonymized URL]" placeholder in Ethics Statement. Consider preparing: code archive, experiment configs, raw results. |
| 5.3 | ARR Reproducibility checklist | ✅ PASS | `checklist.tex` covers all ARR sections (A1–E1). Computing infrastructure specified (4× NVIDIA RTX 5090). |
| 5.4 | Data availability statement | ✅ PASS | Ethics Statement: "Code and data will be released upon acceptance at [anonymized URL]." |

## 6. Compilation Status

| # | Item | Status | Detail |
|---|------|--------|--------|
| 6.1 | 本地 PDF | ✅ PASS | `docs/paper/main.pdf` exists (790 KB, 37 pages, dated 2026-05-20). |
| 6.2 | 编译 warnings 总数 | ⚠️ WARN | 7 LaTeX warnings: 4 float placement (cosmetic), 1 undefined ref (fix with recompile), 1 "undefined references" (same cause), 1 "rerun" (same cause). **All resolve with one additional compile pass.** |
| 6.3 | 服务器编译 | ❌ FAIL | `main.tex` and `sections/` not synced to autodl-5090. No LaTeX toolchain on server. **Not blocking** — compile locally. |

## 7. Scaling Data Timeline (Critical Path)

| Experiment | Current Status | ETA | Post-processing | Paper Impact |
|-----------|---------------|-----|-----------------|-------------|
| 7B FewNERD seed42 | Inference 92.1% | ~imminent | compute_signals → bootstrap → aggregate | Scaling curve data point |
| 7B FewNERD seed123/456 | Inference 50.8% | ~05-20 04:30 UTC | Same pipeline | 3-seed mean for 7B |
| 14B FewNERD | Training 65.5% | ~05-20 20:00 UTC | export → 3-seed inference → pipeline | Scaling curve data point |
| 32B FewNERD | Training 47.4% | ~05-21 02:30 UTC | export → 3-seed inference → pipeline | Scaling curve data point |
| **All data → scaling curve** | | **~05-23 (est.)** | aggregate → plot → §4.6 update | fig_scaling_curve + narrative |

**Risk assessment**: DDL is 05-25. 32B training finishes ~05-21, then needs export + 3-seed inference + post-processing. Estimated ~2 days for full pipeline → data ready ~05-23, leaving ~2 days for paper update and final compile. **Tight but feasible.**

---

## Summary

| Category | ✅ | ⚠️ | ❌ | ⏳ |
|----------|----|----|----|----|
| Format & Pages | 3 | 0 | 0 | 0 |
| Content | 8 | 1 | 0 | 1 |
| Numerical | 3 | 0 | 0 | 0 |
| Typesetting | 4 | 2 | 0 | 0 |
| Submission | 2 | 0 | 0 | 2 |
| Compilation | 1 | 1 | 1 | 0 |
| **Total** | **21** | **4** | **1** | **3** |

## Action Items (Priority Order)

1. **⏳ [CRITICAL] 等 scaling 数据到齐** → 更新 §4.6 + 启用 fig_scaling_curve + 更新 narrative
2. **⏳ [HIGH] 准备 response letter** → 回应 R24 reviewer 意见，突出改进点
3. **⏳ [MEDIUM] 准备 supplementary materials** → code + configs + raw results
4. **⚠️ [LOW] 重新编译修复 forward ref** → `latexmk` 或 pdflatex 跑两遍
5. **⚠️ [LOW] 检查 underfull hbox** → 仅美观问题，不影响提交
6. **❌ [INFO] 服务器编译环境** → 非必需，本地编译即可

## Decision Point: Submit Without Scaling Curve?

如果 7B/14B/32B 数据来不及：
- §4.6 **已有 72B ZS 数据**（Table 5），section 功能完整
- 可提交当前版本，scaling curve 作为 camera-ready 更新
- R24→R25 的改进已足够：72B ZS confirmation + Few-NERD LP success + entity construction + 全面 appendix
- **建议**：尽量等数据，但 05-24 若仍未就绪则提交现有版本
