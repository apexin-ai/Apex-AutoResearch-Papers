# paper s5 reclassification

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_s5_reclassification_20260524T075532_result.json`
- **Structured JSON:** [`d1e6554b463b6a8912c1.json`](../../sessions/d1/d1e6554b463b6a8912c1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary of changes:

| 文件 | 行 | 旧值 | 新值 |
|------|-----|------|------|
| `results.tex` | 80 | `two self-correct (seeds 2 and 5)` | `one self-corrects (seed 2); seed 5 exhibits NVE self-correction ($4.72\times \to 1.22\times$) but policy remains collapsed (eval 10.5\% of baseline)` |
| `results.tex` | 80 | `5/7 progressing toward collapse, 2/7 self-correcting` | `6/7 suffering irreversible policy collapse, 1/7 self-correcting` |
| `appendix.tex` | 34 | `Self-correction` | `Collapse$^\dagger$` |
| `appendix.tex` | 90 (new) | — | 新增 `$^\dagger$ NVE self-corrected ($4.72\times$ $\to$ $1.22\times$) but policy did not recover (eval 10.5\% of baseline).` |
| `appendix.tex` | 614 | `${\sim}1.1\times$$^{\S}$` → `1.22$\times$`; `Self-correction` → `Collapse$^\dagger$` | Final NVE 精确化 + outcome 修正 |
| `appendix.tex` | 621 | — | 新增 `$^\dagger$` 脚注（post-CIVO outcome 表） |
| `appendix.tex` | 624 | `5/7 seeds...two self-correction cases (Walker seeds 2 and 5)` | `6/7 seeds...one self-correction case (Walker seed 2); seed 5 exemplifies a dissociation...` |

验证结果：
- `2/7` — 0 残留
- `~1.1` — 0 残留
- `5/7` — 仅剩 frozen embedding 表行（`5/7$^\#$`，无关）和 `96.5/77.3` 误匹配
- B1 表 (line 135) `059 & 4.72 & self-correcting CIVO & $-$` — 保持不变（B1 分类仅关注 NVE 持续性）

---
