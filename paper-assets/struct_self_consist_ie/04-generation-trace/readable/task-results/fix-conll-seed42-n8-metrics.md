# fix conll seed42 n8 metrics

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_conll-seed42-n8-metrics_20260519T162228_result.json`
- **Structured JSON:** [`8be4d5197ee4bae66a2e.json`](../../sessions/8b/8be4d5197ee4bae66a2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**seed42 原始值**（CoNLL N=8，无 gold filter，3453 instances）：
- Constant utility: 61.5%（2125/3453）
- Oracle gap closed: 37.4%
- Within-inst SJ ρ (median): 1.000

**3-seed 均值**（seed42 / seed123 / seed456）：
- Constant utility: (61.5 + 65.6 + 65.7) / 3 = 64.3% → **64%**（原 66%）
- Oracle gap closed: (37.4 + 38.4 + 33.4) / 3 = 36.4% → **36%**（不变）
- Within-inst SJ ρ: (1.000 + 0.981 + 0.990) / 3 = 0.990 → **0.990**（原 0.985）

**appendix.tex diff**：
- L363: `66\%` → `64\%`
- L364: 不变（36%）
- L365: `0.985` → `0.990`

---
