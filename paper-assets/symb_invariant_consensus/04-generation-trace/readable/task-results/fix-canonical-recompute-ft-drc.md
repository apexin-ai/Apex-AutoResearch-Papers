# fix canonical recompute ft drc

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_canonical-recompute-ft-drc_20260522T225027_result.json`
- **Structured JSON:** [`9342ebf096ce09a1d160.json`](../../sessions/93/9342ebf096ce09a1d160.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits verified. Here's the summary:

## 重算结果

### FT DeBERTa Combo (r11_canonical SC)
| w | 旧 combo | 新 combo | 旧 Δ | 新 Δ | 变化 |
|---|---------|---------|------|------|------|
| 1 | 42.33   | 42.17   | +3.00| +2.83| -0.17pp |
| 3 | 52.17   | 52.00   | +12.83| +12.67| -0.17pp |
| 5 | 65.50   | 65.50   | +26.17| +26.17| 无变化 |

Complementarity: 365:2 → 364:2 (因 ID_FIX 使 1 个 Mistral SC 回答由错变对)

### DRC τ=0.7 (r11_canonical)
| 指标 | 旧值 | 新值 | 变化 |
|------|------|------|------|
| Accuracy | 45.33% | 45.33% | 无变化 |
| NLI calls | 233/600 | 207/600 | -26 |
| NLI cost | 38.8% | 34.5% | -4.3pp |
| Recovery | 90.0% | 90.0% | 无变化 |

### 根因
`mistral_pw600_sc_votes.json` 中两个 problem ID 用的是 `_Q4`，而 `proofwriter_full.json` 用 `_Q8`。ID_FIX 映射后 SC baseline = 236/600 = 39.33%，与 r11_canonical 完全一致（0 mismatches）。

### 修改清单
- `docs/paper/appendix.tex:868` — DRC 表 caption: "35--39%" → "~35%"
- `docs/paper/appendix.tex:876` — DRC 表 PW-D5 行: 233/600, 38.8% → 207/600, 34.5%
- `docs/paper/appendix.tex:1002-1003` — FT NLI 表: 42.33→42.17, 52.17→52.00, 365:2→364:2
- `docs/paper/solutions.tex:32` — +12.83→+12.67, 365:2→364:2, DRC 文本修正
- `docs/paper/figures/gen_capability_gap_scatter.py:50` — 12.83→12.67

### 编译状态
成功 (27 pages, 652515 bytes)

---
