# ops verify fixes and repo

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify_fixes_and_repo_20260523T185747_result.json`
- **Structured JSON:** [`d3ee946c7819b1338ed8.json`](../../sessions/d3/d3ee946c7819b1338ed8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all results. Here's the summary:

---

## Part 1: 匿名 repo HTTPS 检查

**HTTPS** — remote URL 为 `https://github.com/anonymous-nlp-2026-2/nlp_variance_gtheory.git`，格式正确。

## Part 2: 论文修复验证

| # | 检查项 | 结果 |
|---|--------|------|
| 1 | model main effect "3--5%" / "9--11%" | **NOT_FIXED** — 第20行仍有 `3--5\% (MC) and 9--11\% (FF)`，但后面有脚注说明了精确值（2.8--5.4% / 8.5--10.7%），是有意保留的四舍五入写法 |
| 2 | CI 标注 "71 to 162" | **CONFIRMED** — 第115行已改为 `Bootstrap CIs (71--162 items) and LOMO analysis`，有 CI 说明 |
| 3 | 硬编码章节号 (\S4.1 等) | **CONFIRMED** — experiments.tex / method.tex / limitations.tex 均无 `\S` + 数字编号匹配，已使用 `\ref` 交叉引用 |
| 4 | Abstract "multi-condition" | **CONFIRMED** — abstract.tex 无命中，术语已统一 |
| 5 | Table 1 温度注释 | **CONFIRMED** — 温度行显示 `0.0 / 0.3 / 0.7`（3 levels），`460,800$^\dagger$` 有 dagger 标注 |
| 6 | 旧 sections/experiments.tex | **CONFIRMED (CLEANED)** — 文件不存在 |
| 7 | BibTeX key wei2025gtheory / varannot2025gtheory | **CONFIRMED** — 0 匹配，已清除 |

**注意**: 检查 1 中 "3--5%" 和 "9--11%" 仍在文中，但带有脚注给出精确值。如果原意是彻底移除这些四舍五入数字，则需进一步修改。

---
