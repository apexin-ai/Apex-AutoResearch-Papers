# ARR 提交材料清单

**目标会议**: EMNLP 2026 (via ARR)
**检查时间**: 2026-05-24 (最新)

---

## 材料总览

| 材料 | 路径 | 状态 | 备注 |
|------|------|------|------|
| 主论文 PDF | `docs/paper/main.pdf` | ✅ | 874KB, 32页, 2026-05-24 06:00 编译 |
| 主文页数 (≤8页) | — | ✅ | Sec 1–6 (Abstract–Conclusion) 在第 1–8 页 |
| Limitations 章节 | `docs/paper/limitations.tex` | ✅ | 在正文中（第 8 页底），不计入 8 页限制；3 个核心点，篇幅适当 |
| Limitations 唯一性 | — | ✅ | 仅在正文，appendix 中无重复 limitations section |
| Abstract (≤200 words) | `docs/paper/abstract.tex` | ⚠️ | **约 207 词，超出约 7 词，需精简** |
| 匿名性: 作者 | `main.tex` L26 | ✅ | `\author{Anonymous}` |
| 匿名性: review 模式 | `main.tex` L2 | ✅ | `\usepackage[review]{acl}`，行号已启用 |
| 匿名代码仓库 | `_anonymous_repo.json` | ✅ | `https://github.com/anonymous-nlp-2026-2/ec_hte_llm_annotation` |
| Appendix | `docs/paper/appendix.tex` | ✅ | 含在 main.pdf 中（第 11–32 页），ARR 允许 |
| ACL 模板 | `docs/paper/acl.sty` | ✅ | 存在 |
| BibTeX | `docs/paper/references.bib` | ✅ | 57 条 entries, 564 行 |
| 引用解析 | — | ✅ | 编译无 undefined reference 警告 |
| NLP Checklist | `docs/paper/checklist.tex` | ✅ | 已准备参考答案；main.tex 中正确注释掉（ARR 在 OpenReview form 填写） |
| 图: fig1_sign_reversal.pdf | `docs/paper/figures/` | ✅ | |
| 图: fig2_heatmap.pdf | `docs/paper/figures/` | ✅ | |
| 图: fig3_budget.pdf | `docs/paper/figures/` | ✅ | |
| 图: fig4_roc.png | `docs/paper/figures/` | ✅ | |
| 图: applicability_frontier.pdf | `docs/paper/figures/` | ✅ | |
| 图: treatment_dep_misclass.pdf | `docs/paper/figures/` | ✅ | |
| 图: policy_reversal_zone.pdf | `docs/paper/figures/` | ✅ | |

## 问题列表

1. **⚠️ Abstract 超字数** — 约 207 词，EMNLP 2026 限制 200 词。需删减约 7 词。
2. **🔍 匿名仓库可访问性** — URL 已配置，建议在无登录浏览器中验证仓库是否公开可访问。

## 就绪度

**19/21 项就绪**（1 项需修复，1 项需验证）
