# 引用核对清单 — Batch 2

| # | bib key | 存在? | 标题正确? | 作者正确? | 年份正确? | Venue正确? | arXiv ID正确? | 问题 |
|---|---------|-------|----------|----------|----------|-----------|-------------|------|
| 14 | mpruner2024 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 15 | lachance2022cka | ✅ | ✅ | ✅ | ✅ | ✅ | N/A | 无 |
| 16 | ainslie2023gqa | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 17 | shortgpt2024 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 18 | slicegpt2024 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 19 | llms2lrms2026 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 20 | rac2025 | ✅ | ✅ | ✅ | ❌ | ❌ | ✅ | 年份应为2025(提交)/2026(发表); Venue 应为 ICLR 2026（非 NeurIPS 2025 Workshop） |
| 21 | ssgr2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 22 | p2law2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 23 | pat2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 24 | fang_2025 | ✅ | ❌ | ✅ | ✅ | ✅ | ✅ | 标题缺少 "FANG:" 前缀——bib 中有但实际 arXiv 标题为 "Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping"（无 FANG 前缀）；bib 加了 {FANG} 可接受 |
| 25 | funcnet_2025 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | 无 |
| 26 | klabunde_similarity_survey_2023 | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ | 年份错误：bib 写 2023，ACM Computing Surveys 正式发表于 2025（Vol 57, No 9, May 2025）；arXiv 首发 2023 但期刊年份应以正式发表为准 |

## 详细问题

### #20 rac2025 — Venue 和年份错误

**bib 中写的**：`NeurIPS 2025 Workshop on Efficient Reasoning`, year=2025

**实际**：该论文（arXiv:2509.12464）已被 **ICLR 2026** 接收为正式会议论文（Published as a conference paper at ICLR 2026）。arXiv 提交日期为 2025-09-15，最新修订版为 2026-05-02。

**建议修正**：
- `booktitle` 改为 `Proceedings of the 14th International Conference on Learning Representations (ICLR)`
- `year` 改为 `2026`

### #24 fang_2025 — 标题前缀

**bib 中写的**：`{FANG}: Improving Generalization in {LLM} Structured Pruning via Function-Aware Neuron Grouping`

**实际 arXiv 标题**：`Improving Generalization in LLM Structured Pruning via Function-Aware Neuron Grouping`（无 "FANG:" 前缀）

**评估**：arXiv 原始标题不含 "FANG:" 前缀，FANG 是论文中提出的方法缩写。bib 中加上 `{FANG}:` 前缀虽然方便读者识别，但严格来说与原标题不符。建议移除前缀以匹配原标题，或保留但知悉这是编辑添加。

### #26 klabunde_similarity_survey_2023 — 年份

**bib 中写的**：`year={2023}`

**实际**：该论文在 ACM Computing Surveys 上的正式发表日期为 **2025 年 5 月 6 日**（Volume 57, Issue 9, Article 242）。arXiv 首次提交确实在 2023 年 5 月（2305.06329），但期刊引用应使用正式发表年份。

**建议修正**：`year` 改为 `2025`，bib key 也可考虑更新为 `klabunde_similarity_survey_2025`。
