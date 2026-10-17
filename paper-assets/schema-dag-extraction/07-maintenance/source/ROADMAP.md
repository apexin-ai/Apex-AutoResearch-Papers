# schema-dag-extraction — Research Dashboard

> 最后更新: 2026-05-22 12:08 UTC | 更新原因: v35 用户质量审查 7 项全部完成 + R² 数据修复

## 核心方向
Training-free LLM IE 中 schema 复杂度如何预测性能下降：count-related recall decline (Dim1, cross-task) + confusability-related type substitution (Dim2, RE batch-level, format-independent)。详见 paper_framing.md。

## 当前阶段：v35 submission-ready，等待用户审批 R30 + ARR 提交（DDL 2026-05-25，3 天）

**论文状态 v35**：
- R26 审稿 3.5 → 8 项论文修改 + 3 项补分析全部完成
- 🚨 R²=0.218 数据错误修复（r/R² 混淆）→ 80pool R²≈0.05, pooled semipartial R²=0.273
- C3 证据层级调整：pooled R²=0.273 (primary) → 80pool R²≈0.05 (secondary) → Figure 1b (illustrative)
- Figure 1b caption 标注为 illustrative（N=1 per condition）
- SDGD §5 移入 Appendix，正文保留 3-4 句摘要
- Limitations 压缩：5 条→3 点 1 段 + logit variance 归因句
- 2 篇新引用（NER Retriever, Reflect then Learn）
- ARR 预检全部 PASS（匿名化、格式、references pages 补全）
- Anonymous GitHub 包修复（API key 泄露 + configs 目录）
- Author response template 5 个 Q&A block 预写
- Camera-ready prose polish（13 处）+ appendix 表格格式统一（29 表）

**用户质量审查 7 项（2026-05-22）**：
- C3 极端 batch N=1 → 证据层级调整 ✓
- R² 数据修复 → 0.218→0.273/0.05 ✓
- M1 Gemini leverage → PASS（count_8 稳健，count_16 已披露）
- M2 Ecological fallacy → PASS（BCS 是 Level-2 contextual variable，batch-level 分析正确）
- M4 FewRel contamination → PASS（contamination risk LOW）
- Discussion 扩展 + TOST anchoring → PASS（12→26-28 行）
- 文献蒸馏 v2 → 无需调整 framing

**审稿轨迹**：R23 3.5 → R24 3.0（caveat backfire）→ R25 3.5（"strong core"）→ R26 3.5 → 用户审查 → v35

## 近期任务
- [x] R25 全部修复（v34）
- [x] R26 全部修复（8 项论文修改 + 3 项补分析）
- [x] R²=0.218 数据错误修复
- [x] C3 证据层级调整
- [x] ARR 预检 + Anonymous GitHub 修复
- [x] Author response template
- [x] 端到端最终一致性检查（6/6 PASS）
- [x] M1/M2/M4 分析完成（全部 Reviewer PASS）
- [x] Discussion 扩展 + TOST margin anchoring（Reviewer PASS）
- [ ] R30 审稿（待用户审批）
- [ ] Anonymous GitHub 上传（待用户操作）
- [ ] ARR 提交（DDL 2026-05-25）

## GPU 预算
- cqa1-38874 cuda:0：空闲（reserve for rebuttal / 最终加固实验）

## 实验状态
69 个实验，39 成功。v35 为纯写作 + 数据修复 + 补充分析（0 GPU）。

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D072 | 2026-05-23 | 提交前不再跑新实验，cuda:0 保留给 rebuttal 阶段 | exp-009, exp-010, exp-011, exp-014 |
| D071 | 2026-05-21 | R25 Action Matrix (D071): 做 DocRED semipartial R²  | — |
| D070 | 2026-05-21 | R24 Action Matrix: 重构叙事为 "strong core (FewRel R²=2 | — |
| D069 | 2026-05-21 | Round 23 Action Matrix 定稿：16 issues 全部通过 framing/w | — |
| D068 | 2026-05-20 | v14 claim 回滚 + v15 叙事优化 + v16 格式统一确认为最终提交版。GPU cud | exp012_llama_fewrel_ch2, exp_paired_constrained |
| D067 | 2026-05-19 | D067: Gemini 2.5 Flash 复制 Dim2 BCS-accuracy 负相关 (r | exp_gemini_flash_cross_model, exp_paired_constrained |
| D066 | 2026-05-19 | D066: exp_paired_constrained 证明 BCS-accuracy 关系 fo | exp_paired_constrained, exp_unconstrained_decoding_ablation |
| D065 | 2026-05-19 | D065: 批准 paired constrained decoding 实验——在 25 个 un | exp_unconstrained_decoding_ablation |
| D064 | 2026-05-19 | D064: Round 22 Action Matrix 定稿——4 must-fix + 7 sh | exp_bcs_range_matched, exp_docred_error_taxonomy |
| D063 | 2026-05-19 | D063: 补充 2 个低风险实验：DocRED BCS 扩样本量 + SDGD-zero MAVE | exp_docred_confusability, exp008_sdgd_v2_fewnerd |

