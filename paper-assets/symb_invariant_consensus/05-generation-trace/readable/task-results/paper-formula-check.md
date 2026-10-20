# paper formula check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_formula-check_20260524T152044_result.json`
- **Structured JSON:** [`4c97b22c21785315ad91.json`](../../sessions/4c/4c97b22c21785315ad91.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功，无错误。修复了 10 处公式格式问题：

| 文件 | 修复 |
|------|------|
| analysis.tex | `$\geq$99\%` → `${\geq}99\%$`（math/text 边界不一致） |
| analysis.tex | 裸数字 `0.69` → `$0.69$` |
| experiments.tex | `${\sim}$12\%` → `${\sim}12\%$` |
| experiments.tex | 裸数字范围 `1.86--4.84` → `$1.86$--$4.84$` |
| solutions.tex | `$+$12.67/$+$11.67` → `$+12.67$/$+11.67$`（与 `$+6.67$` 模式一致） |
| solutions.tex | `${\sim}$72\%` → `${\sim}72\%$` |
| solutions.tex | 裸数字范围 `83--90\%` → `$83$--$90$\%` |
| solutions.tex | `${\sim}$35\%` → `${\sim}35\%$` |
| limitations_content.tex | `${\sim}$2\,pp` → `${\sim}2$\,pp` + 裸范围 `1.86--4.84` → `$1.86$--$4.84$` |
| limitations_content.tex | 裸范围 `3--4` → `$3$--$4$` |

introduction.tex、method.tex、discussion.tex 无问题。appendix.tex 和 related_work.tex 未触碰。

---
