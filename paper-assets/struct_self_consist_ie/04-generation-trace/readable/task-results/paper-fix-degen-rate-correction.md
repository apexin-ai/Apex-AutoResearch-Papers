# paper fix degen rate correction

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper-fix_degen_rate_correction_20260519T142219_result.json`
- **Structured JSON:** [`3d4bc2ac0aa25bf39d8e.json`](../../sessions/3d/3d4bc2ac0aa25bf39d8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修改完成。汇总如下：

---

## 已修改（8 处）

| # | 文件 | 行 | old | new |
|---|------|----|-----|-----|
| 1 | experiments.tex | L102 | `CoNLL 48.4\%` | `CoNLL 61.7\%` |
| 2 | experiments.tex | L122 | `48.4\%` (CoNLL table row) | `61.7\%` |
| 3 | experiments.tex | L124 | `13.8\%` (Few-NERD table row) | `13.0\%` |
| 4 | appendix.tex | L362 | `Constant F1 & ... & 48.4\%` | `61.7\%` |
| 5 | appendix.tex | L1248 | `13.8\% (vs.\ ... 48.4\% on CoNLL)` | `13.0\% (vs.\ ... 61.7\% on CoNLL)` |
| 6 | appendix.tex | L1274 | `(13.8\%)` + `(48.4\%)` | `(13.0\%)` + `(61.7\%)` |
| 7 | appendix.tex | L1341 | `(48.4\% → 17.8\% → 13.8\%)` | `(61.7\% → 17.8\% → 13.0\%)` |
| 8 | appendix.tex | L1121 | `${\sim}$14\%` | `${\sim}$13\%` |

## 检查但未修改（3 处）

| 位置 | 内容 | 原因 |
|------|------|------|
| discussion.tex L4 | `17.8--67.9\%` | 61.7% 仍在此范围内，无需改 |
| introduction.tex L15 | `13\textendash 87\%` | 13.0% ≈ 13%，无需改 |
| appendix.tex L1436 | `CoNLL at 59--89\%` | 59% = seed42 N=8 (59.14%)，89% 来自其他配置，范围仍正确 |

## 待确认项（2 处）

1. **appendix.tex L687**: `valid-instance fraction is low (41\% for Qwen, 11\% for LLaMA)` — 如果 valid-instance = 100% - degeneracy%，则 N=8 下应为 ~38%（100-61.7），需改 41%→38%。但 100-48.4=51.6 ≠ 41，说明 41% 可能来自不同的计算口径（如不同 N 值或额外过滤条件），无法确定应改为什么值。**建议回查 CoNLL 的 non-degenerate instance count 确认。**

2. **appendix.tex L360**: 表头 `\shortstack{CoNLL 8B\\($N{=}16$)}` — 值已改为 N=8 数据 (61.7%)，但表头仍标注 N=16。**如果此列现在报告 N=8 结果，表头需改为 `$N{=}8$`；如果保留 N=16 列，则值应还原为 48.4%。**

## 已创建文件

`artifacts/w1_table3_multiseed.json` — 记录 3-seed degeneracy 原始数据。

---
