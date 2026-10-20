# research paper evidence table

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper-evidence-table_20260514T090950_result.json`
- **Structured JSON:** [`b8c4d9e8e518d289f0eb.json`](../../sessions/b8/b8c4d9e8e518d289f0eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入并注册：`artifacts/paper_tables_draft.md` (art_20260514_c6d177)

内容概要：

**Table 1 (Main Results)** — 12 行，覆盖 6 种方法 × 多 seed/β 配置：
- Exec-only 3 seeds: s42 正常 (PR=0.93, ISR=0.12), s43 sampling eval 退化 (PR=0.14), s44 tautological collapse (ISR=0.57§)
- 1000-step extended: ISR 从 0.12 跌至 0.003，确认 collapse 单调恶化
- ISR β=0.1 s42: PR=0.81, ISR=0.34 (3.2× baseline)，s43/s44 标 TBD
- Random β=0.1 s42: PR=0.79, ISR=0.10 — 控制组证明 ISR 非纯正则化效果
- β=0.3: 两组均 PR 崩溃 (ISR: 0.18, Random: 0.48)
- Convex-random/Convex-ISR(STA): 退化/仅训练指标

**Table 2 (Hacking Taxonomy)** — ISR β=0.1 vs Random β=0.1：
- Genuine rate: 25.9% vs 17.7% (+8.2pp)
- Conclusion embedding: 72.8% vs 78.5% (主导 hacking 模式)
- Complexity w/o utility: 0% vs 3.8% (ISR 完全消除)
- Genuine proof 质量: ISR 0.67 vs 0.34 (2.0×)

所有 footnote 标注了 s43 sampling eval、s44 tautological artifact、plan005 train-only 等不可比性。

---
