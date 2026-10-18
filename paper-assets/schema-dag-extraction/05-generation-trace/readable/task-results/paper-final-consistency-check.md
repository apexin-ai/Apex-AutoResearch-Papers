# paper final consistency check

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final_consistency_check_20260522T120807_result.json`
- **Structured JSON:** [`f86758bc933ae0559e68.json`](../../sessions/f8/f86758bc933ae0559e68.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All data collected. Here's the report:

---

## 端到端一致性检查报告

### 1. R²=0.218 残留: **PASS**

2 处匹配，均为 **Spearman ρ = 0.218**（SCS-confusion pairwise correlation），非 semipartial R²：
- `main.tex:590` — "SCS--confusion Spearman correlation ... ($\rho = 0.218$, $p < 0.001$, $n = 3{,}160$ pairs)"
- `main.tex:630` — 表格中 "FewRel & SCS (embedding) & **0.218** & $< 0.001$"

两处均为合法的 pairwise Spearman ρ，与 semipartial R² = 0.273 是不同指标。无残留错误。

### 2. 数字一致性: **PASS**

| 数字 | 出现次数 | 一致性 |
|------|---------|--------|
| semipartial R²=0.273 | abstract×1, intro×1, results×3, main(appendix)×7 | 全部一致，上下文正确 |
| 80pool R²≈0.05 | results×1 | 仅 1 处，搭配 r=-0.22, p=0.027，上下文正确 |
| VIF=50.9 | main×4, results×3 | 全部一致，均指 DocRED multicollinearity |
| VIF=1.18 | abstract×2, intro×1, main×2, results×2 | 全部一致，均指 FewRel low collinearity |
| TOST p=0.003 | main×2, results×1 | 全部指 ±3pp TOST（main:909 的 0.003 是 relaxed-span 表格，不同指标） |
| TOST p=0.209 | main×1, results×1 | 全部指 logit-scale TOST inconclusive |
| TOST p=0.047 | main×4, results×1 | ±2pp TOST 和 logit interaction p，上下文均正确 |
| partial r=-0.537 | main×2, results×1 | 全部一致，FewRel partial correlation |
| 80pool r=-0.22 | results×1（r=-0.22），main×3（-0.221） | 精度不同但一致（results 取两位小数，表格取三位） |
| p=0.027 | main×4, results×1 | 全部指 80pool within-pool regression p 值；另 main:337 的 SD=0.027 是 Few-NERD BCS SD，不同指标 |

### 3. 交叉引用: **PASS**

- undefined references: **0**
- multiply defined labels: **0**

### 4. 编译: **PASS**

- LaTeX errors (`^!`): **0**
- BibTeX warnings: 1（`guo-2021-label-confusion` volume/number 冲突，不影响输出）
- 输出: 27 pages, 476127 bytes

### 5. 页数: **PASS**

- Sections 1–6 (Discussion and Conclusion) 结束于 **page 8**
- Limitations 从 page 8 底部开始（不计入 8 页限制）
- References 从 page 9 开始（无限制）
- 正文 ≤ 8 页 ✓

### 6. Anonymization: **PASS**

- `\author{Anonymous}` ✓
- 无大学/机构名泄露（grep 匹配均为 `\label{}` 命令和通用学术用语的误匹配）
- 无服务器路径/IP 泄露
- 无致谢/基金信息
- 无 GitHub/HuggingFace 链接

---

**总结: 6/6 PASS。** BibTeX 的 volume/number warning 建议修复（在 `references.bib` 中 `guo-2021-label-confusion` 条目删除 `number` 字段），但不影响论文内容。

---
