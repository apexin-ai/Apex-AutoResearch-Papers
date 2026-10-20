# EMNLP 2026 ARR 投稿材料清单

> 目标周期：ARR 2026 May cycle → EMNLP 2026 commitment
> Deadline：2026-05-25 (submission), 2026-05-27 (reviewer registration), 2026-08-02 (commitment)
> 所有截止时间：11:59PM UTC-12:00 (AoE)

---

## 1. 投稿材料

| # | 材料 | 格式要求 | 状态 |
|---|------|---------|------|
| 1 | **Main Paper PDF** | Long: 8pp content + unlimited references/limitations/ethics; Short: 4pp. ACL style template (`\usepackage[review]{acl}`), double-blind, 行号开启 | ✅ 已有 |
| 2 | **Limitations Section** | 正文 Conclusion 后、References 前，不计入页数限制。缺失 = desk reject | ✅ 已有 (`limitations.tex`) |
| 3 | **Ethics Statement** | 可选但强烈建议。正文 Limitations 后、References 前，不计入页数 | ✅ 已有 (`ethics.tex`) |
| 4 | **Responsible NLP Research Checklist** | 必填，OpenReview submission form 内逐题回答。2024.12 起填写不当可 desk reject。接收后作为 appendix 公开 | ⚠️ 需准备（草稿已有，需转为 OpenReview 表单格式） |
| 5 | **Supplementary Materials (Appendix)** | 双栏格式（2025.07 起强制），不计入页数，reviewer 不必阅读，关键内容必须在正文 | ✅ 已有（18 个 appendix sections） |
| 6 | **Supplementary Materials (Code)** | 单个 .tgz/.zip，或 Anonymous GitHub 链接。禁止 Google Drive/Dropbox（可追踪下载） | ⚠️ 需准备（Anonymous GitHub repo） |
| 7 | **Supplementary Materials (Data)** | 单个 .tgz/.zip，匿名化 | ⚠️ 需准备（数据包打包） |

## 2. OpenReview Submission Form 必填字段

| 字段 | 说明 | 状态 |
|------|------|------|
| Title | 论文标题 | ✅ |
| Abstract | 论文摘要 | ✅ |
| PDF | 主论文 PDF | ✅ |
| Paper Type | Long / Short | ✅ Long |
| Track/Area Keywords | 选择研究领域 | ⚠️ 需选择（建议: NLP Applications / Machine Learning for NLP） |
| Preprint Status | 是否允许作为 anonymous preprint 公开 | ⚠️ 需决定 |
| Conference Declaration | **必须选择 EMNLP 2026**（binding，未选则无法 commitment） | ❌ 提交时必填 |
| Responsible NLP Checklist | 逐题 Yes/No/N/A + section/justification | ⚠️ 草稿已有 |
| Anonymization Confirmation | 确认已匿名化 | ⚠️ 提交时勾选 |
| Metadata Consent | 同意匿名元数据用于数据集 | ⚠️ 提交时勾选 |
| Reviewer Signup | 所有作者必须注册 reviewer（截止: submission + 48h） | ❌ 需注册 |
| Resubmission Info | 若为 resubmission：前版链接 + 修改说明 + reviewer 偏好 | N/A（首投） |

## 3. 格式与匿名要求

- **模板**: 官方 ACL style template, `\documentclass[11pt]{article}` + `\usepackage[review]{acl}`
- **匿名化**: 无作者姓名/机构，self-citation 用第三人称，supplementary 匿名化，禁止可追踪链接
- **匿名期**: 无匿名期要求（2024.02 起取消）
- **Appendix 格式**: 双栏（2025.07 起强制，不符 = desk reject）
- **字体**: 图表中字体 ≥ 合规大小（参照 ACLPUB formatting guidelines 2025.01 更新）
- **行号**: review 版必须开启

## 4. Desk Reject 高风险项（逐项检查）

| 检查项 | 状态 |
|--------|------|
| 页数符合限制（Long ≤ 8pp content） | ⚠️ 需确认 |
| Limitations section 存在 | ✅ |
| 匿名化完整（无作者名、无可追踪链接） | ⚠️ 需检查 |
| Appendix 双栏格式 | ⚠️ 需确认 |
| Responsible NLP Checklist 完整填写 | ⚠️ 需完成 |
| 无 dual submission | ✅ |
| ACL style template 合规 | ✅ (`\usepackage[review]{acl}`) |
| Conference declaration = EMNLP 2026 | ❌ 提交时必选 |
| Reviewer registration（所有作者） | ❌ 需在 05-27 前完成 |

## 5. Commitment 阶段（2026-08-02）

- Author response period: 2026-07-07 ~ 07-13（纯文本，禁止外链，新实验仅限回应 reviewer 问题的 minor ablation）
- Meta review release: 2026-07-30
- Commitment deadline: 2026-08-02
- Acceptance notification: 2026-08-20
- Camera-ready: 2026-09-20（Long ≤ 9pp, Short ≤ 5pp）
- Commitment 时不可修改作者列表（可调整顺序）

---

Sources:
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Author Guidelines](https://aclrollingreview.org/authors)
- [ARR Responsible NLP Research](https://aclrollingreview.org/responsibleNLPresearch/)
- [ARR Common Submission Problems](https://aclrollingreview.org/authorchecklist)
- [Checklist Appendix Policy](https://aclrollingreview.org/responsible-nlp-checklist-appendices)
