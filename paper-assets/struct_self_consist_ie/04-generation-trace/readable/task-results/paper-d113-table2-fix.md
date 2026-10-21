# paper d113 table2 fix

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d113_table2_fix_20260516T100507_result.json`
- **Structured JSON:** [`13e71f8e2084fa25b8d6.json`](../../sessions/13/13e71f8e2084fa25b8d6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有修改已完成。验证结果：

- `0.663` — 0 matches（全部替换为 0.645）
- `surpass` — 0 matches（全部改为 "approximately matches"）
- `Single` in main sections — 0 matches（仅保留 appendix 和 method.tex 的合法定义）
- `outperform` — 仅剩正确用法（"neither significantly outperforms the other"、conclusion "without significantly outperforming it"、非 tied 子集 p=0.004 的合法 claim）

核心变更：
1. Table 2: Greedy 0.663→0.645±0.001，删除 Single 行，Random 注释为 "= expected F1 of single T=1.0 draw"
2. 全文 framing："greedy surpasses all selection" → "selection approximately matches greedy (Δ=+0.2pp, p=0.29, not significant)"
3. C3 贡献：改为 "selection recovers T=1.0 sampling degradation but fails to close the 13.3pp oracle gap"
4. Limitations: +0.4pp → +0.1pp over greedy

Changelog 已保存并注册为 `art_20260516_606f7e`。

---
