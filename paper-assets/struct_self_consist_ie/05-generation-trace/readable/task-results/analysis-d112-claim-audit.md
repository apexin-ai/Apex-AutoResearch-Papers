# analysis d112 claim audit

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d112_claim_audit_20260516T094502_result.json`
- **Structured JSON:** [`51061c7ca02735552103.json`](../../sessions/51/51061c7ca02735552103.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。主要发现：

**5个HIGH严重度问题：**
1. Discussion "+0.1pp over single-sample" vs Limitations "+0.4pp over greedy" — 数学上矛盾（审稿人已指出）
2. Table 1 VC AUROC (.663) vs multi-seed table (.697±.010) — seed=42 数学上不可能产生这个均值/σ组合
3. Provenance c002 "EM AUROC=0.749" vs Table 1 实际值 .614 — provenance 严重过时
4. Provenance greedy=0.644 vs paper greedy=0.663 — 来源实验不同，1.9pp差距
5. Provenance VC AUROC=0.684 vs Table 1 VC AUROC=.663 — provenance 过时

**关于 "Single=T=0 greedy" 的结论：**
Single 行大概率确实是 T=1.0。证据：±0.001 方差（T=0 应为零方差）+ 与 Greedy 行差 1.8pp（如果都是 T=0 应完全相同）。混淆来源是 provenance 引用了不同实验的 greedy 值 (0.644) 恰好接近 Single (0.645)。

**最优先修复：** limitations.tex L10 的 "+0.4pp over greedy" 需改为 "+0.1pp over single-sample"（或从实验数据确认正确值）。

产出已保存到 `artifacts/d112_claim_audit/` 并注册。

---
