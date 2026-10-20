# Paper Status Audit (2026-05-22)

## 已完成的章节/段落

### LaTeX 正文（docs/paper/sections/）

- **abstract.tex** (18行): 完整。已使用 D144 修正后的 matched@2048 数字（-5.63pp@1.7B, +0.25±0.47pp@4B）。包含三维度 landscape、variance compression、1.7B→8B 跨 scale 对比。
- **introduction.tex** (35行): 完整。5段结构，3 contributions（landscape + spectrum + RSFT），已降级 CED 为组件、EDCR 为分析工具。数字已同步修正。
- **related_work.tex** (30行): 完整。3 主题段（DocRE+evidence / RL alignment / self-training），引用覆盖 SAIS/DREEAM/EIDER/ATLOP/AutoRE/GRPO/DPO/STaR 等，DAPO/Dr.GRPO/R1-RE/REAR 新文献已加入。
- **method.tex** (64行): 完整。5 小节（Task formulation / SFT baseline / Paradigms: GRPO+DPO+RSFT / CED scoring / EDCR definition），CED 公式和 EDCR 公式已写入，flat-NLI 等效性已说明。
- **experiments.tex** (132行): 完整。6 小节（Setup / Main Results + tab:main / Decoupling Spectrum + tab:spectrum / Scaling + tab:scaling / Evidence Strategy / Generalization），所有主表已填数。包含 RSFT inference-time tax 和 LLaMA variance compression。
- **analysis.tex** (14行): 完整但简短。4 段（EDCR diagnostic / Ablation / Error patterns / Practical implications）。内容足够但偏紧凑。
- **conclusion.tex** (4行): 完整。单段总结三维度+RSFT 效果。
- **limitations.tex** (19行): 完整。含 Ethics Statement 和 ARR checklist 注释。覆盖 dev-set / exact-match / 单 RL 算法 / EDCR 未做 human validation / evidence quality unchanged 等 6 点。
- **appendix.tex** (339行): 大量内容。包含 13 个 section：Hyperparams / Full Ablation / Scaling Details / Controlled Eval Subset / Training-Time Tax / RSFT Theory / Spectrum Viz / Scaling Viz / Generalization (cross-family + cross-dataset + Re-DocRED test + encoder comparison) / GRPO Dynamics / Error Analysis / EDCR Per-Relation / Qualitative Analysis。

### 表格

| 表格 | 位置 | 状态 |
|------|------|------|
| tab:main (4B主结果) | experiments.tex | ✅ 已填数 |
| tab:spectrum (decoupling) | experiments.tex | ✅ 已填数 |
| tab:scaling (5模型) | experiments.tex | ✅ 已填数 |
| tab:hyperparams | appendix.tex | ✅ 已填数 |
| tab:ablation_full | appendix.tex | ✅ CED 4-seed + flat-NLI 2-seed + random + k=3 + v3-large |
| tab:cross_detail | appendix.tex | ✅ 5模型 Rel-F1/Evi-F1 |
| tab:mechanistic | appendix.tex | ✅ 3-scale duplication/truncation |
| tab:training_tax | appendix.tex | ✅ matched@2048 4-scale |
| tab:test_results (Re-DocRED test) | appendix.tex | ✅ 4模型 test Ign-F1 |
| tab:encoder_comparison | appendix.tex | ✅ ATLOP/EIDER/SAIS/DREEAM vs ours |
| tab:error_analysis | appendix.tex | ✅ 3-scale error decomposition |
| tab:case_evidence | appendix.tex | ✅ 3 qualitative examples |

### 图表

| 图表 | 文件 | 状态 |
|------|------|------|
| fig_overview (task+pipeline) | figures/paper/fig_overview.pdf | ✅ 已生成 |
| fig_spectrum (decoupling scatter) | figures/paper/fig_spectrum.pdf | ✅ 已生成 |
| fig_scaling (evidence tax bars) | figures/paper/fig_scaling.pdf | ✅ 已生成 |
| fig_edcr_relations (per-relation) | figures/paper/fig_edcr_relations.pdf | ✅ 已生成 |
| fig_grpo_dynamics (training curves) | figures/paper/fig_grpo_dynamics.pdf | ✅ 已生成 |

### 其他

- **references.bib** (301行): 已有，覆盖主要引用
- **main.tex** (42行): 结构完整，引用所有 section 文件
- **main.pdf** (10页): 已编译版本存在

### Artifacts 中的关键支撑文件

- **comprehensive_results.md**: 10 张结果表，涵盖 scale×method / evidence metrics / variance / tax / ablation / GRPO / CED reranker / cross-arch / Re-DocRED / DREEAM
- **paper_evidence_table.md**: 4 claims 的实验证据映射 + gap 清单
- **evidence_tax_annotation_notes.md**: 审计 → 已应用到 .tex（+7.5pp→+0.25pp，-6.2pp→-5.63pp）
- **dev_test_gap_paragraph.md**: 已整合到 appendix.tex §generalization_full
- **test_table_draft.md**: 已过时（appendix 中 tab:test_results 更完整）
- **negative_review.md**: 18 个 negative 实验系统复盘

---

## 缺失/需要更新

### CRITICAL（阻塞提交）

1. **DocRED 官方 test set 结果缺失**
   - 当前只有 Re-DocRED test（非官方 benchmark）
   - CodaLab 提交未完成（review_issues.yaml W2 标记 critical）
   - 需要：用户提交 CodaLab，获取官方 test 分数
   - Limitations 中已提前声明 "test set submission is pending"

2. **SFT test baselines 全部缺失**
   - tab:test_results 只有 RSFT test 分数，无 SFT 对比
   - 无法在 test set 上计算 RSFT gain
   - 需要：SFT models 的 test predictions + CodaLab 提交

3. **4B test 数据不可恢复**
   - 4B RSFT s42 checkpoint 丢失，test_table_draft.md 标记 "irrecoverable"
   - tab:test_results 中 4B 行缺失
   - 需要：决定是否接受 4B 无 test 数据，或从 4B RSFT Method B (s44) 补充

### HIGH（显著削弱论文）

4. **Figure 文件路径可能未对齐**
   - 图在 `figures/paper/` 目录下，但 .tex 引用 `fig_spectrum.pdf` 等（无路径前缀）
   - 编译时需确保图在 docs/paper/ 下或 graphicspath 正确设置
   - 需要：验证 LaTeX 编译是否能找到图

5. **Evidence tax annotation 修正验证**
   - evidence_tax_annotation_notes.md 标记了 5 处需修改的位置（abstract:11, intro:24, intro:30, experiments:92, conclusion:4）
   - 当前 .tex 已使用修正后数字，但需确认 ALL instances 都已更新
   - 需要：全文搜索 "+7.5" 和 "-6.2" 确认无残留

6. **flat-NLI ablation Ign-F1 缺失**
   - tab:ablation_full 中 flat-NLI s42/s43 的 Ign-F1 列为 "--"
   - CED 有 4-seed Ign-F1，flat-NLI 只有 Rel-F1
   - 需要：flat-NLI 的 Ign-F1 数据（或在表注中说明）

7. **14B RSFT Rel-F1/Evi-F1/EDCR 在 tab:cross_detail 中缺失**
   - 14B RSFT 行显示 "--"
   - 但 tab:scaling 有 14B RSFT Ign-F1=58.86
   - 需要：14B RSFT 的 Rel-F1 和 Evi-F1 填入 cross_detail

### MEDIUM（改进质量）

8. **CED reranker 结果未在主表中**
   - writing_plan.yaml 中 tab:main 规划包含 CED reranker 行
   - 当前 tab:main 只有 SFT / SFT-no-evi / RSFT CED 三行
   - CED reranker 数据在 Evidence Strategy 小节中提到但无独立表行
   - 需要：决定是否加入主表（Ign-F1 仍为 TBD）

9. **CodaLab 提交材料未准备**
   - 无 prediction 格式化脚本、submission 文件
   - 需要：pred-to-codalab 转换工具 + 用户手动提交

10. **Review issues 跟进状态**
    - review_issues.yaml 记录 22 个 issue，多数 status=in_progress
    - W1 (GRPO confound): 部分解决（已加 GRPO bf16 G=4 实验？需确认）
    - W3 (SFT single seed): 已解决（现有 3-seed SFT）
    - W4 (non-monotonic): 已解决（叙事已从 non-monotonic 改为 within-family threshold）

---

## 下一步建议

### P0（提交前必须完成）

1. **验证 LaTeX 编译**：确认 figures 路径、bib 引用、所有 \ref 和 \label 正确。编译 main.pdf 检查页数（8页限制）
2. **全文搜索旧数字**：grep "+7.5" / "-6.2" / "non-monotonic" / "costly at 4B" / "capacity valley"，确认无残留
3. **确认 DocRED test 策略**：要么完成 CodaLab 提交，要么在 Limitations 中明确说明只有 Re-DocRED test

### P1（显著提升论文质量）

4. **补充 SFT test baselines**：至少 1-2 个 scale 的 SFT test 分数，用于计算 test-set RSFT gain
5. **补全 flat-NLI Ign-F1**：填充 tab:ablation_full 中 flat-NLI 的 Ign-F1 列
6. **补全 14B RSFT 详细指标**：tab:cross_detail 中 14B 行
7. **考虑加入 CED reranker 到主表**：如果 Ign-F1 可计算

### P2（锦上添花）

8. **更新 review_issues.yaml**：标记已解决的 issues
9. **清理过时 artifacts**：test_table_draft.md 已被 appendix 取代
10. **检查页数**：main.pdf 当前 10 页，需确认主文 ≤8 页（references + appendix 不计）
