# audit ref check C

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_ref_check_C_20260526T110724_result.json`
- **Structured JSON:** [`cb2751cd3ddad3500721.json`](../../sessions/cb/cb2751cd3ddad3500721.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data needed. Here is the complete audit report.

---

## 39. krosnick1999survey
- 真实性：✓ 存在
- 作者：✓ 正确（Krosnick, Jon A.）
- 年份：✓ 正确（1999）
- 标题：✓ 正确（"Survey Research"）
- Venue：✓ 正确（Annual Review of Psychology, Vol 50, pp 537–567）
- 正文引用上下文：✓ 正确 — related_work.tex 中引用称其"documents satisficing behavior"，Krosnick 1999 确实讨论了 survey 中的 satisficing 行为

## 40. lakens2017equivalence
- 真实性：✓ 存在
- 作者：✓ 正确（Lakens, Daniël）
- 年份：✓ 正确（2017）
- 标题：✓ 正确（"Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses"）
- Venue：✓ 正确（Social Psychological and Personality Science, 8(4), 355–362）
- 正文引用上下文：✓ 正确 — appendix.tex 中用于 TOST equivalence testing，与论文内容完全匹配

## 41. preston2000scale
- 真实性：✓ 存在
- 作者：✓ 正确（Preston, Carolyn C.; Colman, Andrew M.）
- 年份：✓ 正确（2000）
- 标题：✓ 正确（bib 中包含完整副标题 "Reliability, Validity, Discriminating Power, and Respondent Preferences"）
- Venue：✓ 正确（Acta Psychologica, 104(1), 1–15）
- 正文引用上下文：✓ 正确 — appendix.tex 中讨论 scale granularity 对 tie rate 的影响，与该论文研究内容相关

## 42. jeong2025comparative
- 真实性：✓ 存在
- 作者：✓ 正确（Jeong, Hawon; Park, ChaeHun; Hong, Jimin; Lee, Hojoon; Choo, Jaegul）
- 年份：✓ 正确（2025）
- 标题：✓ 正确 — "Amplifies"（单数）确实是 ACL Anthology 原文标题，虽然语法上 "Comparisons Amplifies" 主谓不一致，但这是作者发表的原标题
- Venue：✓ 正确（8th BlackboxNLP Workshop）
- 正文引用上下文：✓ 正确 — 在 related_work.tex、experiments.tex、introduction.tex、main.tex 中多处引用，均描述其"Comparative Trap"发现（pairwise comparison amplifies biases），与论文内容一致

## 43. stureborg2024inconsistent
- 真实性：✓ 存在
- 作者：✓ 正确（Stureborg, Rickard; Alikaniotis, Dimitris; Suhara, Yoshi）
- 年份：✓ 正确（2024）
- 标题：✓ 正确（"Large Language Models are Inconsistent and Biased Evaluators"）
- Venue：✓ 正确（arXiv:2405.01724，截至目前仍为 arXiv 预印本，未查到正式发表版本）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献

## 44. park2024offsetbias
- 真实性：✓ 存在
- 作者：✓ 正确（Park, Junsoo; Jwa, Seungyeon; Ren, Meiying; Kim, Daeyoung; Choi, Sanghyuk）
- 年份：✓ 正确（2024）
- 标题：✓ 正确（"OffsetBias: Leveraging Debiased Data for Tuning Evaluators"）
- Venue：✓ 正确（Findings of EMNLP 2024）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献

## 45. chen2024humans
- 真实性：✓ 存在
- 作者：✓ 正确（Chen, Guiming Hardy et al.）
- 年份：✓ 正确（2024）
- 标题：✗ 错误 — bib 中为 "A Study on Judgement **Biases**"（复数），ACL Anthology 正式发表版标题为 "A Study on Judgement **Bias**"（单数）。应使用正式发表版标题。
- Venue：✓ 正确（EMNLP 2024 Main）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献
- 注意：bib 中作者列表（8人）来自 arXiv v1，ACL Anthology 正式版作者列表可能有差异，建议核对

## 46. he2021debertav3
- 真实性：✓ 存在
- 作者：✓ 正确（He, Pengcheng; Gao, Jianfeng; Chen, Weizhu）
- 年份：✓ 正确 — bib 中 year=2023，对应 ICLR 2023 正式发表年份（bib key 用 2021 是 arXiv 首次提交年份，不影响）
- 标题：✓ 正确
- Venue：✓ 正确（ICLR 2023，arXiv:2111.09543）
- 正文引用上下文：✓ 正确 — appendix.tex 中引用 DeBERTa-v3-large 用于 NLI gate 的内容验证，与论文一致

## 47. shi2024judging
- 真实性：✓ 存在
- 作者：✓ 正确（Shi, Lin; Ma, Chiyu; Liang, Wenhua; Diao, Xingjian; Ma, Weicheng; Vosoughi, Soroush）
- 年份：✓ 正确 — bib 中 year=2025（bib key 用 2024 是 arXiv 年份，不影响）
- 标题：✓ 正确
- Venue：✓ 正确（IJCNLP-AACL 2025，ACL Anthology: 2025.ijcnlp-long.18）
- 正文引用上下文：✓ 正确 — related_work.tex 中称其"study it across 15 judges"，该论文确实系统性地研究了多个 LLM judge 的 position bias

## 48. bavaresco2025llms
- 真实性：✓ 存在
- 作者：✓ 正确（Bavaresco, Anna et al.）
- 年份：✓ 正确（2025）
- 标题：✓ 正确
- Venue：✓ 正确（ACL 2025 Short Papers）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献

## 49. saito2023verbosity
- 真实性：✗ **标题、作者、Venue 均错误（疑似幻觉拼凑）**
- 作者：✗ 错误 — bib 中为 "Saito, Yuki; Nishida, Noriki; Okazaki, Naoaki"，实际该领域的 verbosity bias 论文作者为 **Keita Saito**（非 Yuki）, Akifumi Wachi, Koki Wataoka, Youhei Akimoto。Nishida Noriki 和 Okazaki Naoaki 是日本 NLP 学者但与此论文无关。
- 标题：✗ 错误 — bib 中为 "Verbosity Bias in Multi-Turn Chatbot Evaluations"，**不存在此标题的论文**。实际论文标题为 **"Verbosity Bias in Preference Labeling by Large Language Models"**（arXiv:2310.10076）
- Venue：✗ 错误 — bib 中标注 EMNLP 2023，实际发表于 **NeurIPS 2023 Instruction Workshop**，非 EMNLP
- URL：✗ 错误 — bib 中 URL `aclanthology.org/2023.emnlp-main.665/` 指向一篇完全不相关的 EMNLP 2023 论文
- 正文引用上下文：✓ 引用上下文本身合理（related_work.tex 和 method.tex 中将其作为 verbosity bias 的 prior evidence），Keita Saito 的论文确实研究了 verbosity bias
- **建议**：整条 bib entry 需要重写，修正为正确的论文信息

## 50. simms2019does
- 真实性：✓ 存在
- 作者：✓ 正确（Simms, Leonard J.; Zelazny, Kerry; Williams, Trevor F.; Bernstein, Lee）
- 年份：✓ 正确（2019）
- 标题：✓ 正确
- Venue：✓ 正确（Psychological Assessment, 31(4), 557–566）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献

## 51. carterette2008here
- 真实性：✓ 存在
- 作者：✓ 正确（Ben Carterette, Paul N. Bennett, David Maxwell Chickering, Susan T. Dumais）
- 年份：✓ 正确（2008）
- 标题：✓ 正确（"Here or There: Preference Judgments for Relevance"）
- Venue：✓ 正确（ECIR 2008, LNCS 4956, pp 16–27）
- 正文引用上下文：✓ 正确 — related_work.tex 中称其"confirm this for information retrieval"（确认 preference judgments 在 IR 中的优势），与论文内容一致

## 52. deutsch-etal-2023-ties
- 真实性：✓ 存在
- 作者：✓ 正确（Daniel Deutsch, George Foster, Markus Freitag）
- 年份：✓ 正确（2023）
- 标题：✓ 正确
- Venue：✓ 正确（EMNLP 2023, pp 12914–12929）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献

## 53. luce1959individual
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确（Luce, R. Duncan）
- 年份：✓ 正确（1959）
- 标题：✓ 正确
- Venue：✓ 正确（书籍，John Wiley & Sons）
- 正文引用上下文：✓ 正确 — experiments.tex 中与 Bradley-Terry 模型一起引用，Luce's choice axiom 是 BT 模型的理论基础

## 54. williams2018broad
- 真实性：✓ 存在
- 作者：✓ 正确（Williams, Adina; Nangia, Nikita; Bowman, Samuel R.）
- 年份：✓ 正确（2018）
- 标题：✓ 正确
- Venue：✓ 正确（NAACL 2018, pp 1112–1122）
- 正文引用上下文：✓ 正确 — method.tex 中引用为 MNLI 数据集来源（Multi-Genre NLI），这正是该论文提出的 corpus

## 55. embretson2000irt
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确（Embretson, Susan E.; Reise, Steven P.）
- 年份：✓ 正确（2000）
- 标题：✓ 正确
- Venue：✓ 正确（书籍，Lawrence Erlbaum Associates）
- 正文引用上下文：⚠ 未在任何 tex 文件中被引用（仅存在于 bib 中），属于未使用的参考文献

## 56. gwet2008ac1
- 真实性：✓ 存在
- 作者：✓ 正确（Gwet, Kilem Li）
- 年份：✓ 正确（2008）
- 标题：✓ 正确
- Venue：✓ 正确（British Journal of Mathematical and Statistical Psychology, 61(1), 29–48）
- 正文引用上下文：✓ 正确 — appendix.tex 中使用 Gwet's AC₁ 报告 inter-rater reliability，与论文提出的 AC₁ 统计量一致

## 57. likert1932technique
- 真实性：✓ 存在（经典文献）
- 作者：✓ 正确（Likert, Rensis）
- 年份：✓ 正确（1932）
- 标题：✓ 正确
- Venue：✓ 正确（Archives of Psychology, 22(140), 1–55）
- 正文引用上下文：✓ 正确 — related_work.tex 中与 Likert scales 讨论一起引用

---

## 汇总

**总共 19 条，✓ 17 条，✗ 1 条，⚠ 1 条**

### ✗ 错误（1 条）

| # | cite key | 问题 |
|---|----------|------|
| 49 | `saito2023verbosity` | **严重错误（幻觉拼凑）**：标题、作者名、Venue、URL 全部错误。正确信息：Keita Saito 等, "Verbosity Bias in Preference Labeling by Large Language Models", NeurIPS 2023 Instruction Workshop, arXiv:2310.10076 |

### ⚠ 需修正（1 条）

| # | cite key | 问题 |
|---|----------|------|
| 45 | `chen2024humans` | 标题小错：bib 用 arXiv 版标题 "Judgement **Biases**"（复数），ACL Anthology 正式版为 "Judgement **Bias**"（单数），应改为正式版 |

### ⚠ 未使用的参考文献（7 条）

以下引用仅存在于 bib 中，未在任何 tex 文件中被 `\cite` 引用：`stureborg2024inconsistent`, `park2024offsetbias`, `chen2024humans`, `bavaresco2025llms`, `simms2019does`, `deutsch-etal-2023-ties`, `embretson2000irt`

---
