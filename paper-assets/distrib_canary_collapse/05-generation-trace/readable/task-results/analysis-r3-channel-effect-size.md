# analysis r3 channel effect size

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r3_channel_effect_size_20260520T155324_result.json`
- **Structured JSON:** [`a7000acf74ac1a9ae0d7.json`](../../sessions/a7/a7000acf74ac1a9ae0d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心发现：

**Finding 1 — 差分不是 blanket power loss**
- Diversity retention: 95.2% (n=243)
- Perplexity retention: 100.2% (n=8)
- 两类 channel 差分后 |r| 保持率相当，甚至 perplexity 更高。Power loss 假说要求差分成比例地削弱所有 channel，数据不支持。

**Finding 2 — Granger F-stat 的不对称不来自差分，来自时序结构**
- 同实验内（a060_s42_bf16）: diversity median F=229, perplexity F=8.25 → **28x差距**
- 但两者的 naive |r| 几乎相同（0.97 vs 0.96）
- 这说明 F-stat 差距不是差分造成的——raw correlation 就一样高

**Finding 3 — Peak lag 揭示根因**
- Diversity: 81% 的 peak lag < 0（canary 领先 downstream）
- Perplexity: 50% 的 peak lag = 0（同步），median = 0
- Canary→perplexity 是同步共变（同一 training step 驱动），不是滞后因果
- Granger 测的是滞后预测力，所以 lag≈0 的关系天然产生低 F-stat，跟差分无关

**给 Reviewer 的论证**：差分对两类 channel 保持率一致（95-100%），排除了 blanket power loss。Granger F 的 20-28x 差距源于时序结构差异——perplexity 是同步共变（lag=0），diversity 是滞后因果（lag<0）——而非差分操作本身。

---
