# paper r30 p1 text edits

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_r30-p1-text-edits_20260522T154550_result.json`
- **Structured JSON:** [`9b82e8f2ca3b87f86999.json`](../../sessions/9b/9b82e8f2ca3b87f86999.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改汇总：

### P1-A: 因果语言（experiments.tex, 两个目录）
| 位置 | before | after |
|------|--------|-------|
| L26 | `that reveals structural degeneration` | `consistent with structural degeneration` |
| L32 | `and confirming that structural degeneration requires` | `and suggesting that structural degeneration requires` |
| L105 | `confirming STA's diagnostic transfer` | `supporting STA's diagnostic transfer` |

### P1-B: Table 1 caption（experiments.tex:L70, 两个目录）
caption 末尾增加：`ISR* reported for completeness; mode-level analysis (\S\ref{sec:goodhart}) provides the primary diagnostic.`

### P1-C: Limitations（limitations.tex:L9, 两个目录）
末尾新增一句：`All ISR conditions use a single multiplicative reward family ($r_{\text{exec}} \cdot (1+\beta\,\text{ISR})$); alternative formulations remain untested.`

### P1-D: Wilhelm 引用（两个目录）
- **references.bib**: 末尾添加 `wilhelm2026monitoring` 条目
- **related_work.tex:L26**: Reward hacking 段尾新增：`Complementarily, \citet{wilhelm2026monitoring} detect reward hacking at generation time via internal activations, whereas STA provides a post-training structural diagnostic.`

---
