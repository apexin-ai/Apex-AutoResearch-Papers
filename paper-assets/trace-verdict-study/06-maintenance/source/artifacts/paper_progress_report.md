# Paper Progress Report — trace-verdict-study
**Date**: 2026-05-16 | **Deadline**: ARR May 25 (9 days) | **Target**: EMNLP 2026 Main

---

## 1. Section 完成度

论文源码位于服务器 `/root/trace-verdict-study/docs/paper/`，共 8 个 .tex 文件（701 行）。

| Section | File | Lines | 完成度 | 备注 |
|---------|------|-------|--------|------|
| Abstract | main.tex | 39 | 100% | 3 claims + numbers 全部匹配 |
| Introduction | introduction.tex | 30 | 100% | Motivation, framing, 3 contributions |
| Method | method.tex | 85 | 100% | Task def, dataset, 7 conditions, models, training, loss ablation |
| Experiments | experiments.tex | 189 | 100% | 6 subsections: cross-model, ablation, density, trace length, calibration, DebugBench |
| Discussion | discussion.tex | 86 | 100% | 5 subsections + limitations |
| Related Work | related_work.tex | 29 | 100% | 3 paragraphs, 19 citations |
| Conclusion | conclusion.tex | 19 | 100% | 3 findings + future work |
| Appendix | appendix.tex | 224 | 100% | Per-class, training details, VOTA examples, full results, irreducible analysis |

**编译状态**: SUCCESS (pdflatex x3 + bibtex), 0 errors, 0 undefined refs, 0 missing citations

---

## 2. 图表清单

### Figures

| Figure | 文件 | 服务器 | 本地 artifacts | 状态 |
|--------|------|--------|----------------|------|
| fig1_trace_overview | PDF (37K) + PNG (200K) | ✅ `/root/trace-verdict-study/figures/paper/` | ✅ `_project/chart/` | ✅ 完成 |
| fig2_calibration | PDF (18K) + PNG (169K) | ✅ 同上 | ✅ 同上 | ✅ 完成 |
| fig3_cross_model_gap | PDF (33K) + PNG (157K) | ✅ 同上 | ✅ 同上 | ✅ 完成 |
| fig4_trace_length | PDF (18K) + PNG (114K) | ✅ 同上 | ✅ `figures/paper/` | ✅ 完成 |

### Tables (12 个)

| Table | 位置 | 状态 |
|-------|------|------|
| tab:dedup | method.tex | ✅ |
| tab:cross_model | experiments.tex | ✅ |
| tab:ablation | experiments.tex | ✅ |
| tab:density | experiments.tex | ✅ |
| tab:trace_length | experiments.tex | ✅ |
| tab:calibration | experiments.tex | ✅ |
| tab:debugbench | experiments.tex | ✅ |
| tab:per_class | appendix.tex | ✅ |
| tab:hyperparams | appendix.tex | ✅ |
| tab:train_time | appendix.tex | ✅ |
| tab:full_qwen | appendix.tex | ✅ |
| tab:full_deepseek | appendix.tex | ✅ |

数据一致性: 全部 15 个关键指标与 paper_framing.md 完全匹配 ✅

---

## 3. 关键 Blocking Items

### P0 — 必须解决

| # | 问题 | 严重性 | 说明 |
|---|------|--------|------|
| 1 | **页数超限: 14 页 → 8 页** | 🔴 Critical | EMNLP 限制 8 页正文 + unlimited refs/appendix。D042 已决定将 Discussion 4 个分析性小节移入 appendix，但尚未执行 |
| 2 | **Placeholder 引用: ~25 处** | 🔴 Critical | `related_work.tex` 和 `section3_experimental_setup.tex` 中有 ~25 个 `\cite{placeholder_...}` 需替换为真实 bib 条目。注意: 服务器上编译通过的 `docs/paper/` 版本已无 placeholder（22 个真实 bib key），但 `_project/paper/` 中的旧版本仍有 placeholder |

### P1 — 应当解决

| # | 问题 | 严重性 | 说明 |
|---|------|--------|------|
| 3 | **full_trace_1024tok_seed42** | 🟡 Medium | 正在 GPU cuda:0 上训练，完成后需更新 4-point trace length ablation 图 |
| 4 | **eval_missing_predictions batch** | 🟡 Medium | 正在 GPU cuda:1 上运行，补全全条件 paired comparison 表 |
| 5 | **3 个 minor overfull hbox** | 🟢 Low | Abstract 29pt, Discussion 13pt, Verbatim 13pt — 可接受 |

---

## 4. 实验数据完备性

- 总实验数: 43 (22 success / 6 negative / 3 failed)
- Plans: 11 个中 10 完成, 1 在跑
- Core claims: 3/3 FINALIZED
- Provenance: 32/32 全覆盖
- Seed robustness: Qwen 3-seed ✅ (99.83% ± 0.00), DeepSeek 3-seed ✅ (2/3 = 99.33%, 1 outlier = 91.09%)

---

## 5. 建议下一步优先级

| 优先级 | 任务 | 预估耗时 | 依赖 |
|--------|------|----------|------|
| **1** | 14→8 页压缩重组: Discussion 移入 appendix，精简 Method/Experiments 文字 | 3-4h | 无 |
| **2** | 确认 `docs/paper/` 引用全部为真实 bib（已完成?），清理 `_project/paper/` 旧版 placeholder | 1h | 无 |
| **3** | 等 1024tok 训练完成 → 更新 fig4 + trace length ablation 数据 | 等 GPU | full_trace_1024tok_seed42 |
| **4** | 等 eval batch 完成 → 生成全条件 paired bootstrap 表 | 等 GPU | eval_missing_predictions |
| **5** | Paper Agent 交付最终初稿 → Reviewer 对抗审稿 | 1-2 天 | #1-4 |
| **6** | 迭代修改 + 定稿 + ARR 提交 | 2-3 天 | #5 |

---

## 6. 时间线风险评估

- **May 16 (今天)**: 1024tok + eval batch 应当完成；页数压缩可并行进行
- **May 17-18**: Paper Agent 完成初稿 + Reviewer 对抗
- **May 19-21**: 迭代修改
- **May 22-23**: 定稿 + 最终检查
- **May 24**: 提交 ARR

**主要风险**: 14→8 页压缩是最大工作量，需要对正文结构做实质性重组。建议立即开始。
