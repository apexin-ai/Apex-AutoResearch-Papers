# EMNLP 2026 ARR May Cycle Submission Checklist

**Deadline**: May 25, 2026, 23:59:59 UTC-12 (Anywhere on Earth)
**Commitment deadline**: August 2, 2026
**Conference**: October 24--29, 2026, Budapest, Hungary

> EMNLP 2026 shares the ARR May cycle with AACL. Authors must **declare target conference at submission time** (binding).

---

## 已满足

### 论文格式
- [x] **LaTeX 模板**: 使用官方 acl.sty + `\usepackage[review]{acl}` (review 模式)
- [x] **行号**: `\linenumbers` 已启用
- [x] **匿名化**: `\author{Anonymous}`，无自我引用泄露
- [x] **无外部链接泄露**: 未发现 GitHub/Dropbox/Google Drive 等可追踪链接
- [x] **Long paper 页数**: 正文 (Section 1--6) 在 8 页内 (Conclusion 结束于 p8)
- [x] **Limitations section**: limitations.tex 存在且内容充实 (30 行)，不计入页数
- [x] **Ethics Statement**: ethics.tex 存在，含 Licenses / Compute budget / Software 段落
- [x] **References**: references.bib 含 61 条引用，使用 acl_natbib.bst
- [x] **Appendix**: 15 个附录 section，双栏格式，不计入页数
- [x] **字体/排版**: 11pt, article class, times + latexsym

### Responsible NLP Checklist (论文中已覆盖)
- [x] **A1 Limitations**: limitations.tex 详述 8 项限制 (base-only models, scale, prompt-type, cross-domain, etc.)
- [x] **A2 Risks**: ethics.tex 讨论潜在误用 (suppression of legitimate AI text) 及推荐用途
- [x] **B1 Cite creators**: 所有生成模型 (Pythia, OLMo, Qwen3, Llama, Mistral) 及工具均有引用
- [x] **B2 License/terms**: ethics.tex Licenses 段列出所有模型许可证 (Apache 2.0, Qwen License, Llama Community License, CC BY-SA 3.0)
- [x] **B4 PII/offensive content**: ethics.tex 说明 "no personal or sensitive data"
- [x] **B6 Dataset statistics**: appendix_dataset_stats.tex 提供数据集统计
- [x] **C1 Parameters/compute**: ethics.tex 列出 4x RTX 5090, 62 GPU-hours
- [x] **C4 Packages/versions**: ethics.tex Software 段列出所有包版本 (Python 3.12.3, PyTorch 2.10.0, etc.)

---

## 未满足 / 需确认

### 论文格式 (提交前必做)
- [ ] **确认 acl.sty 为最新版本**: 当前使用的 acl.sty 来源不明，需对比 [acl-org/acl-style-files](https://github.com/acl-org/acl-style-files) master 分支最新版。自 2026 年 3 月起 ARR 不再接受 Word 模板，但 LaTeX 模板也需确保最新
- [ ] **编译最终 PDF**: 确认编译无 warning，所有引用/交叉引用正确解析
- [ ] **检查 appendix 双栏格式**: ARR 要求 appendix 使用双栏 (有特定例外)，确认当前 appendix 符合

### OpenReview 提交表单字段
- [ ] **Title**: 填入 "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"
- [ ] **TL;DR**: 需撰写一句话概述 (~150 字符)。建议: "We show that recursive LLM generation leaves measurable distributional fingerprints that enable classifying text generation depth with lightweight features."
- [ ] **Abstract**: 从 abstract.tex 复制，检查 TeX 公式用 `$...$` 语法
- [ ] **Paper Type**: 选择 "Long paper"
- [ ] **Area**: 选择最相关的研究方向 (建议: "Generation" 或 "NLP Applications" 或 "Resources and Evaluation"，需查看 ARR area 列表确认)
- [ ] **Preferred Venue**: 必须选择 **EMNLP 2026** (binding，提交后不可更改)
- [ ] **Preprint**: 决定是否公开匿名预印本 (选 "yes" 允许 ARR 公开匿名版本；选 "no" 则保持私密)
- [ ] **Existing Preprints**: 如已有 arXiv 预印本，填入 URL
- [ ] **Software**: 准备匿名化代码压缩包 (.tgz/.zip, ≤200MB)。需从代码中移除所有作者信息、路径中的用户名等
- [ ] **Data**: 准备匿名化数据压缩包 (.tgz/.zip, ≤200MB)。包含生成的 depth chains 数据集
- [ ] **Consent to Share Data**: 勾选同意
- [ ] **Consent to Review**: 勾选同意

### Responsible NLP Checklist (OpenReview 表单逐项填写)
- [ ] **B3 Intended use consistency**: 需确认所有 artifacts 使用符合其 intended use，并在论文中说明或在表单中给出 justification
- [ ] **B5 Documentation of artifacts**: 需确认是否充分描述了数据集覆盖范围 (domains, languages)
- [ ] **C2 Hyperparameter search**: 需确认论文中是否描述了 XGBoost/分类器超参数搜索过程及最优值
- [ ] **C3 Descriptive statistics**: 确认结果报告是否透明说明了 mean/max/std 等统计量
- [ ] **D1--D5 Human annotators**: N/A，但需在表单中标注 "No" 并说明不涉及人类标注
- [ ] **E1 AI assistants**: 如使用了 AI 写作/编码辅助工具 (ChatGPT, Copilot, Claude 等)，**必须披露**。自 2024.12 起 ARR 对 checklist 不完整/误导性回答执行 desk reject

### 作者注册 & 审稿义务
- [ ] **OpenReview 个人资料**: 所有作者需在提交后 48 小时内 (May 27 前) 完成 OpenReview 注册，包括: affiliation, Semantic Scholar link, DBLP link, ACL Anthology link, 可接收邮件的邮箱
- [ ] **审稿人注册**: 所有作者必须在 May 27 前注册为审稿人并接受审稿任务。未注册可能导致当前及下一轮 ARR 投稿资格被取消
- [ ] **审稿完成**: 审稿截止 July 6，meta-review 截止 July 29

### 其他注意事项
- [ ] **Dual submission 检查**: 确认论文未同时提交至其他会议/期刊/workshop
- [ ] **Text reuse 检查**: 文本复用不超过总 token 数的 10%
- [ ] **作者列表锁定**: commitment 阶段 (August 2) 不允许增减作者，仅可调整顺序。提交时确认最终作者列表
- [ ] **Presentation 注册**: 被接受的论文必须有至少一名作者注册参会 (in-person 或 virtual) 并完成报告

---

## 关键时间线

| 日期 | 事项 |
|------|------|
| **May 25** | ARR 提交截止 (AoE) |
| **May 27** | 所有作者完成 OpenReview 注册 + 审稿人注册 |
| **July 6** | 审稿截止 |
| **July 7--13** | Author response & discussion |
| **July 29** | Meta-review 截止 |
| **July 30** | Meta-review 发布 |
| **August 2** | EMNLP commitment 截止 |
| **August 20** | 录用通知 |
| **September 20** | Camera-ready 截止 |
| **October 24--29** | EMNLP 2026 会议 (Budapest) |

---

## 参考链接

- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Submission Form Fields](https://aclrollingreview.org/submissionform)
- [ARR Author Guidelines](https://aclrollingreview.org/authors)
- [ARR Responsible NLP Checklist](https://aclrollingreview.org/responsibleNLPresearch/)
- [EMNLP 2026 CFP](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Style Files (GitHub)](https://github.com/acl-org/acl-style-files)
- [ARR Dates & Venues](https://aclrollingreview.org/dates)
- [Common Submission Problems](https://aclrollingreview.org/authorchecklist)
