# nlp_variance_gtheory — Research Dashboard

> 最后更新: 2026-05-24 11:51 UTC | 更新原因: Anonymous repo finalized (0a73ee7), all deliverables complete, awaiting user OpenReview submission

> 目标: EMNLP 2026 via ARR | DDL 2026-05-25 | 目标 4.0 Conference

## 核心方向
G-theory 多 facet 方差分解应用于 LLM benchmark 评测。Primary contribution: D-study reproducibility budgets — 3×3 design (178 items, 1,602 evals/model) for G≥0.80, 3.1× item reduction over single-condition (552 items)。详见 paper_framing.md。

## 当前进展
**阶段**: 全部就绪，等待用户在 OpenReview 提交 ARR

- **Score trajectory**: R5 (3.5) → R6 (3.0↓) → R7 (3.5↑) → R8 (3.5) → R9 (3.5) → R10 (3.5, fresh)
- **Llama-3.1-70B 跨家族验证 ✅**: item_id=74.5%, G_item=0.957, facet ranking 一致 (D029)
- **数据审计 ✅**: 47 checks, 3 issues fixed, Reviewer verified
- **Table 2/3 修正 ✅**: 10 cells corrected from source JSON, Reviewer verified
- **BibTeX 修复 ✅**: wei→song, varannot 2025→2026
- **编译**: 17 页 (8 main + 9 appendix), 0 critical warnings
- **实验**: 12 成功 / ~2.36M records / 8 models + 72B + Llama-70B out-of-sample
- **匿名 repo ✅**: commit 0a73ee7, HTTPS 确认
- **Figure 3 ✅**: 5 benchmarks + 8-model 数据 + MC/FF 分组 + hatching
- **流程架构主图 ✅**: PaperBanana 生成, 移至 Appendix
- **Rebuttal 预案 ✅**: docs/rebuttal_prep.md, 覆盖 4 个预期攻击点
- **C2 Bootstrap 加固 ✅**: MC vs FF item-related variance CI 不重叠 (21pp gap)

## 近期任务
- [x] Llama-70B MMLU 推理 + Henderson I 分析
- [x] 论文 §4.6 / limitations / abstract 集成 Llama-70B 结果
- [x] BibTeX key 修复
- [x] 全量数据审计 + Table 修正
- [x] C2 Bootstrap 加固 + Rebuttal 预案
- [x] Figure 3 修复 (5 benchmarks + 8-model)
- [x] 流程架构主图 (PaperBanana)
- [x] §4.6/Conclusion 压缩, Limitations 精简 → 8 页 main
- [x] 匿名 repo 最终版推送 (commit 0a73ee7)
- [ ] **用户在 OpenReview 提交 ARR (DDL 5/25)**

## GPU 预算
westd-32570: 4× RTX PRO 6000 96GB — 空闲
westd-19912: 4× RTX PRO 6000 96GB — 空闲

## 关键决策日志

| ID | 日期 | 摘要 | 关联实验 |
|----|------|------|----------|
| D029 | 2026-05-23 | D029: Llama-3.1-70B cross-family validation SUCCES | exp_llama70b_mmlu |
| D028 | 2026-05-23 | D028: Round 10 Fresh Review (3.5) — 3 MF + 8 SF +  | — |
| D027 | 2026-05-23 | D027: Round 9 (3.5) — 2 systemic issues identified | — |
| D026 | 2026-05-22 | D026: Round 8 (3.5) — 三个 MF 需实质性新分析，不做表面修改 | — |
| D025 | 2026-05-22 | D025: Round 7 (3.5) — Cost framing 重构 (3×3=178 ite | exp-004, exp-002 |
| D024 | 2026-05-22 | Round 6 修订完成提交 Round 7 — all N1-N5/W1-W8 fixed, fo | exp-004, exp006_partial_credit |
| D023 | 2026-05-22 | D023: Round 6 (3.0) — Format claim 核弹移除 + model fa | exp-002, exp-004 |
| D022 | 2026-05-22 | Round 5 (3.5): Contribution #2 合并到 #1 — format pat | exp-004, exp-002 |
| D021 | 2026-05-22 | Round 4 (3.5): 重构 contribution 排序 — D-study budget | exp-004, exp-002 |
| D020 | 2026-05-22 | D018 撤回 — Messing (2026) arXiv:2604.11581 确认真实存在，W | — |



