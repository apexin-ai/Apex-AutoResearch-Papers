# fix conll oracle headroom global

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_conll-oracle-headroom-global_20260519T185016_result.json`
- **Structured JSON:** [`f2b8d72745afd918600d.json`](../../sessions/f2/f2b8d72745afd918600d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正已到位，grep 确认无遗漏。

### 修改清单

| # | 文件 | 行号 | 修改前 | 修改后 |
|---|------|------|--------|--------|
| 1 | appendix.tex | L248 | `.957` | `.948` |
| 2 | experiments.tex | L102 | `CoNLL ${\approx}5$\,pp` | `CoNLL ${\approx}4$\,pp` |
| 3 | appendix.tex | L932 | `5.0~pp at $N{=}8$` | `4.0~pp at $N{=}8$` |
| 4 | experiments.tex L201 (Table 5) | — | 已为 `${\approx}$4` | 无需修改 |

### grep 确认

- `.957` → **0 matches** (已清除)
- `4.9` → 5 matches，均为 temperature degeneracy `14.9%` 和 Few-NERD headroom `14.9pp`，与 CoNLL 无关
- `≈5` / `\approx 5` → **0 matches**
- `5.0` → 2 matches，均为 SciERC `15.0` pp，与 CoNLL 无关

---
