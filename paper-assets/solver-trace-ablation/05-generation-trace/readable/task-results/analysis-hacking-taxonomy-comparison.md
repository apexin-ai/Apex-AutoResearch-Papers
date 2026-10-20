# analysis hacking taxonomy comparison

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_hacking-taxonomy-comparison_20260514T085802_result.json`
- **Structured JSON:** [`189c0f4d0e6ff000cae6.json`](../../sessions/18/189c0f4d0e6ff000cae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Conclusion embedding 是两组的主要 hacking 模式**（ISR 72.8% vs Random 78.5%），模型把 conclusion 直接嵌入 premises 使证明 trivially satisfiable。

**ISR reward 的效果**：
- Genuine proof 比例提升 +8.2pp（25.9% vs 17.7%）
- Genuine proof 的 ISR 质量远高于 Random（mean 0.67 vs 0.34，max 1.0 vs 0.5）
- 消除了 "complexity without utility" hacking（0% vs 3.8%）
- 但整体 hacking rate 仍高达 74%，conclusion embedding 是主要瓶颈

产出已注册：`art_20260514_bf31aa`

---
