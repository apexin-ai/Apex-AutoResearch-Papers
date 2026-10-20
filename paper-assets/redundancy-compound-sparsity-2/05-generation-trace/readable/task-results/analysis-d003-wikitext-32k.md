# analysis d003 wikitext 32k

**redundancy compound sparsity 2** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d003_wikitext_32k_20260512T154756_result.json`
- **Structured JSON:** [`fff4e1d257475dfd38ac.json`](../../sessions/ff/fff4e1d257475dfd38ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新完毕。`d003_wikitext_32k` status=DONE, conclusion=negative。

**核心发现：**
- **Recency eviction (PPL 7.1758) 几乎无损**，甚至微优于 full attention (7.1822)，说明在 WikiText 语言建模中，远距离 token 对当前 token 预测几乎无贡献。
- **EMA eviction 全面落败**：best EMA (α=0.9) PPL 7.7788，比 recency 差 8.4%，比 random 还差 1.8%。α 越小越差 (0.7→8.14, 0.5→8.14)。
- EMA 的 avg_evicted_score (~0.48-0.51) 远低于 random (0.70)，说明 EMA score 在驱逐"不重要" token 方面的判别力不如随机。

**根因推测：** WikiText 的 attention pattern 高度局部化，recency 天然就是最优 eviction 策略。EMA score 作为全局累积统计量，在这种局部化 pattern 下反而引入噪声，驱逐了本不该驱逐的近距离 token。

---
