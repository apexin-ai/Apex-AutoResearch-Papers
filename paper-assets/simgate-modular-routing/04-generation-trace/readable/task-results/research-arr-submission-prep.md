# research arr submission prep

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_arr-submission-prep_20260517T075411_result.json`
- **Structured JSON:** [`d5796fe5fa02a5c4333c.json`](../../sessions/d5/d5796fe5fa02a5c4333c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现在我有了完整信息。论文正文约 5 页（远低于 8 页限制），共 15 页（含附录）。

```
=== ARR → EMNLP 2026 Submission Checklist ===

截止日期：2026-05-25 23:59:59 AoE（距今 8 天）
Author Registration Form：2026-05-27 EoD AoE
会议：Budapest, Hungary, Oct 24-29, 2026

⚠️  重要：EMNLP 和 AACL 共享 ARR May cycle，提交时必须选择目标会议（binding）

─────────────────────────────────────────

[已完成]
- ✓ ACL style template（acl.sty + acl_natbib.bst）
- ✓ Review mode 开启（\usepackage[review]{acl}，含行号）
- ✓ 匿名化（\author{Anonymous}，无 acknowledgements）
- ✓ 无自引泄露（grep 未发现 github/gitlab/huggingface/self-reference）
- ✓ Limitations section（正文后，不计入页数）
- ✓ Ethics Statement（正文后，不计入页数）
- ✓ 正文页数：~5 页（限制 8 页 long paper），充裕
- ✓ References 使用 acl_natbib.bst
- ✓ 附录结构完整（8 个 appendix sections: A-H）
- ✓ 所有 sections 齐全：Abstract / Introduction / Method / Experiments / Related Work / Discussion / Conclusion
- ✓ 论文可编译（main.pdf 15 页，无 error）
- ✓ 双栏格式正确
- ✓ 字体 Times，11pt

[需要做]
- ☐ Abstract 字数超限：当前 ~220 words，ACL 限制 200 words → 需删减约 20 words
- ☐ Responsible NLP Research Checklist：在 OpenReview 表单中逐项填写（非 PDF 附录）
    - Section A: Limitations + Risks（已有 Limitations section，需对应填写）
    - Section B: Scientific Artifacts（代码、数据集、模型引用）
    - Section C: Computational Experiments（GPU hours、参数量、基础设施）
    - Section D: Human Annotation（如适用）
    每项答 Yes 需标注 section number，答 No 需 justification
    ⚠️  不可全部填 Yes、不可不填 justification，否则 desk reject
- ☐ Author Registration Form：所有作者须在 deadline 后 48h 内完成（5月27日前）
- ☐ 所有作者须注册为 reviewer（不合规可能 desk reject）
- ☐ 选择 target venue = EMNLP 2026（binding，不可更改）
- ☐ AI 工具使用声明：如使用 generative AI，须在 Responsible Checklist 中披露，
    详情写入 Acknowledgements（review 版先不加）或 README
- ☐ Supplementary materials 匿名化检查（如提交代码/数据附件）
- ☐ 确认 code/data release 承诺（Ethics Statement 中已写 "upon acceptance"）

[Metadata 字段 — OpenReview 提交表单]
- Title: Death Avoidance as a Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld
- Abstract: 需粘贴（≤200 words 版本）
- Keywords/Track: 建议选 "NLP Applications" 或 "Interpretability and Analysis of Models for NLP"
- Paper type: Long paper
- Target venue: EMNLP 2026（binding）
- Resubmission URL: N/A（首次提交）
- Justification for author changes: N/A
- Responsible NLP Checklist: 逐项填写

[风险项]
- 🔴 Abstract 超限（~220 > 200 words）— 部分 cycle 严格执行会 desk reject
- 🔴 距 deadline 仅 8 天，Responsible Checklist 填写需认真准备
- 🟡 正文仅 ~5 页（long paper 上限 8 页）— 不是格式问题，但审稿人可能认为内容不够充实
    建议：将部分 appendix 核心内容（如 cross-model verification 精华）移入正文
- 🟡 LaTeX warnings: 7 个 `h` float specifier changed to `ht` — 不影响提交但建议修复
- 🟡 references.bib 部分条目缺少 pages/doi 字段 — 建议补全以提升规范性
```

Sources:
- [ARR Call for Papers](http://aclrollingreview.org/cfp)
- [ARR Authors Guidelines](http://aclrollingreview.org/authors)
- [ARR Submission Form Fields](http://aclrollingreview.org/submissionform)
- [ARR Common Submission Problems](http://aclrollingreview.org/authorchecklist)
- [ARR Responsible NLP Research](http://aclrollingreview.org/responsibleNLPresearch/)
- [Responsible NLP Checklist PDF](https://aclrollingreview.org/static/responsibleNLPresearch.pdf)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACLPUB Formatting Guidelines](https://acl-org.github.io/ACLPUB/formatting.html)
- [ACL Style Files (GitHub)](https://github.com/acl-org/acl-style-files)

---
