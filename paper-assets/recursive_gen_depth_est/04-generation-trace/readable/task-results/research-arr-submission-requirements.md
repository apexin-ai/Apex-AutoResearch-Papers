# research arr submission requirements

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_arr_submission_requirements_20260517T073558_result.json`
- **Structured JSON:** [`3cffe18c1a00568e8d05.json`](../../sessions/3c/3cffe18c1a00568e8d05.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

以下是完整调研结果。

---

## 1. 页数限制

| 类型 | Review 版 | Camera-ready 版 |
|---|---|---|
| Long paper 正文 | **8 页** | **9 页**（多 1 页用于 reviewer feedback） |
| Short paper 正文 | **4 页** | **5 页** |
| References | **不占页数** | **不占页数** |
| Limitations section | **不占页数**（必须有，缺失 = desk reject） | 不占页数 |
| Ethical Considerations | **不占页数**（可选） | 不占页数 |
| Appendix | **不占页数**，放在 references 之后 | 不占页数 |
| Acknowledgments | **Review 版不写**（泄露身份） | 不占页数 |

**Limitations section 位置**: 在 Conclusion 之后、References 之前，不能包含新实验/分析/图表。

**Appendix 格式要求**: 必须使用双栏格式（数学密集部分可例外用单栏）。自 **2025 年 7 月 cycle** 起，Appendix 格式不符将 desk reject。

---

## 2. 匿名化要求

**核心规则**:
- 论文中不能出现作者姓名和单位
- 自引必须用第三人称：用 "Smith (2020) showed..." 而不是 "We previously showed..."
- 不能引用 reviewer 无法获取的文件
- Supplementary material 必须完全匿名
- 禁止使用 Dropbox/Google Drive 等可追踪下载的链接，代码需用 Anonymous GitHub
- **Review 版不写 Acknowledgments**

**预印本政策（2024 年 2 月起更新）**:
- **无匿名期**：随时可发 arXiv 预印本
- 但广泛传播会导致更难招到不知道作者身份的 reviewer
- ACL 对未公开发表的匿名投稿设立了特别奖项激励

**LaTeX 匿名化设置**:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}    % review 版：匿名 + 行号 + 页码
% \usepackage{acl}           % camera-ready 版：显示作者，无行号
% \usepackage[preprint]{acl} % preprint 版：显示作者 + 页码
```

---

## 3. 必须提交的材料清单

### 必须提交
| 材料 | 格式 | 说明 |
|---|---|---|
| **主 PDF** | ACL 模板格式 PDF，所有字体嵌入 | `pdffonts mypaper.pdf` 验证 |
| **Responsible NLP Research Checklist** | OpenReview 提交表单中填写 | 每项 Yes/No/NA + section 编号或 justification。填写不当可 desk reject。接受后作为附录公开发表 |
| **Limitations section** | 嵌入主 PDF，Conclusion 之后 References 之前 | 缺失 = desk reject |
| **Author Registration Form** | 提交 deadline 后 48 小时内完成 | OpenReview profile 需含 affiliation、Semantic Scholar、DBLP、ACL Anthology 链接 |
| **Reviewer 注册** | 提交 deadline 后 48 小时内注册 reviewer | 2025 年 5 月起所有作者必须参与审稿 |

### EMNLP 2026 特有
| 材料 | 说明 |
|---|---|
| **会议声明（binding）** | 提交时必须在 ARR 表单中选择 EMNLP 2026，否则无法 commit。**选择具有约束力** |

### 可选提交
| 材料 | 格式 | 说明 |
|---|---|---|
| **Ethical Considerations section** | 嵌入主 PDF | 推荐但非必须 |
| **Appendix** | 主 PDF 中 references 之后，双栏格式 | reviewer 不要求阅读 |
| **Software** | 单个 `.tgz` 或 `.zip` | 必须匿名 |
| **Data** | 单独的 `.tgz` 或 `.zip`（与 software 分开） | 必须匿名 |

### 重投 (Resubmission) 额外材料
- 上一次提交的链接
- **Revision summary PDF**：逐条说明如何 address 每位 reviewer 的意见
- 可选：color-coded 修改标记版论文

### Author Response（审稿后）
- 纯文本，不允许外部链接
- 在 Author Response 期间提交，非投稿时准备

---

## 4. LaTeX 模板

**官方仓库**: [github.com/acl-org/acl-style-files](https://github.com/acl-org/acl-style-files)

**文件列表**:
| 文件 | 用途 |
|---|---|
| `acl.sty` | 主样式文件 |
| `acl_latex.tex` | 示例文档 |
| `acl_lualatex.tex` | LuaLaTeX 变体 |
| `acl_natbib.bst` | 参考文献样式 |
| `custom.bib` | 示例 bib |

**基本设置**:
```latex
\documentclass[11pt]{article}
\usepackage[review]{acl}   % review 版必须用 [review] 选项
```

**`[review]` 选项效果**: 隐藏作者信息、开启行号、显示页码

**格式规格**:
- A4 纸 (21cm x 29.7cm)，四边 margin 2.5cm
- 双栏，栏宽 7.7cm，栏间距 0.6cm
- 正文 11pt Times Roman，单倍行距
- 标题 15pt bold，居中跨双栏
- Abstract 最多 200 words，10pt，两侧各缩进 0.6cm
- 引用格式：`acl_natbib.bst`，作者-年制，alphabetical 排序
- References 部分标题为 "References"，不编号
- 超链接深蓝色 (#000099)，无下划线

**禁止修改 sty 文件**。不符合格式的论文不经审阅直接拒稿。

---

## 5. Responsible NLP Research Checklist（逐项）

每项回答 **Yes / No / NA**，Yes 需给出 section 编号，No/NA 需给出 justification。接受后作为论文附录公开发表。

### Section A: 所有提交必答

| 编号 | 问题 |
|---|---|
| **A1** | 是否描述了工作的 limitations？（假设、鲁棒性、claim 范围、影响因素） |
| **A2** | 是否讨论了潜在风险？（恶意使用、环境影响、公平性、隐私、安全、过度泛化、双重用途） |

### Section B: 使用了科学制品（代码/数据/模型）

| 编号 | 问题 |
|---|---|
| **B1** | 是否引用了所用制品的创建者？（原始论文、版本号、URL） |
| **B2** | 是否讨论了 license/使用条款？ |
| **B3** | 是否讨论了使用方式是否符合制品的 intended use？ |
| **B4** | 是否检查了个人身份信息和冒犯性内容？ |
| **B5** | 是否提供了制品文档？（语言、领域、人口统计信息、data card） |
| **B6** | 是否报告了数据集相关统计？（样本数、train/dev/test 划分） |

### Section C: 计算实验

| 编号 | 问题 |
|---|---|
| **C1** | 是否报告了模型参数量、计算预算、硬件基础设施？ |
| **C2** | 是否讨论了实验设置（含超参搜索）？ |
| **C3** | 是否报告了结果的描述性统计？（error bars、置信区间、max/mean/single run） |
| **C4** | 是否报告了使用的现有包的实现细节？（版本号、参数设置、修改） |

### Section D: 涉及人类标注者/参与者

| 编号 | 问题 |
|---|---|
| **D1** | 是否报告了完整的参与者指令文本？ |
| **D2** | 是否报告了招募方式和报酬？ |
| **D3** | 是否讨论了数据使用的知情同意？ |
| **D4** | 是否经过伦理审查委员会批准？ |
| **D5** | 是否报告了标注者的人口统计和地理特征？ |

### Section E: AI 辅助使用

| 编号 | 问题 |
|---|---|
| **E1** | 如使用了 AI 辅助（ChatGPT、Copilot 等），是否披露？ |

**重要**: AI 写作辅助必须在 checklist + Acknowledgments 中披露（语法检查和语言润色除外）。

---

## 6. 投稿时间线（EMNLP 2026 / ARR May 2026 Cycle）

| 事件 | 日期 |
|---|---|
| **ARR 提交截止** | **2026-05-25**（AoE） |
| Reviewer 注册截止 | 2026-05-27 |
| Reviews due | 2026-06-29 |
| **Author Response** | **2026-07-07 至 07-13** |
| Meta-reviews 发布 | 2026-07-30 |
| **EMNLP 2026 Commitment 截止** | **2026-08-02** |
| **Acceptance Notification** | **2026-08-20** |
| **Camera-ready** | **2026-09-20** |
| **会议日期** | **2026-10-24 至 10-29** |

也可以用 **March 2026 cycle**（提交截止 2026-03-16）的论文在 08-02 之前 commit 到 EMNLP 2026。

---

## 7. 其他关键政策

- **文本复用**: 来自其他出版物的文本不超过总 token 的 10%
- **Dual submission 禁止**: ARR review 期间不能同时在其他 archival venue 投稿
- **Hallucinated citations**: 虚假引用将 desk reject，作者将被禁止 commit EMNLP 2026 和 2027
- **Author list 修改**: commit 阶段禁止修改作者列表（可改顺序）
- **Presentation 要求**: 所有接受论文必须在会议上 present 才能出现在 proceedings 中

Sources:
- [ARR Call for Papers](https://aclrollingreview.org/cfp)
- [ARR Authors Guidelines](https://aclrollingreview.org/authors)
- [ARR Dates and Venues](https://aclrollingreview.org/dates)
- [ARR Anonymity Policy](https://aclrollingreview.org/anonymity/)
- [ARR Responsible NLP Research Checklist](https://aclrollingreview.org/responsibleNLPresearch/)
- [ARR Checklist as Appendices Policy](https://aclrollingreview.org/responsible-nlp-checklist-appendices)
- [ARR Common Submission Problems](https://aclrollingreview.org/authorchecklist)
- [EMNLP 2026 Call for Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Style Files (GitHub)](https://github.com/acl-org/acl-style-files)
- [ACLPUB Formatting Guidelines](https://acl-org.github.io/ACLPUB/formatting.html)

---
