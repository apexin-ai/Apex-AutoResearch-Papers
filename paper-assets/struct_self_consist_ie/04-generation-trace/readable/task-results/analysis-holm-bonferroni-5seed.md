# analysis holm bonferroni 5seed

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_holm-bonferroni-5seed_20260522T184852_result.json`
- **Structured JSON:** [`66398387d3f2918e9867.json`](../../sessions/66/66398387d3f2918e9867.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**R39 W4 resolved。**

5-seed Holm-Bonferroni 结果：

| | 3-seed (旧) | 5-seed (新) |
|---|---|---|
| Max adjusted p | 0.055 | **0.013** |
| 显著 (α=0.05)? | 否 | **是** |

核心数据：
- ρ_SJ = 0.356 ± 0.014，ρ_LP = 0.205 ± 0.015
- ρ_advantage = 0.151 ± 0.006（5个seed高度一致）
- 所有5个seed的 Holm-Bonferroni adjusted p ≤ 0.013

论文需更新位置：
1. 统计显著性声明：p=0.055 → p=0.013
2. Seed数量：3 → 5
3. 汇总统计量：ρ_SJ=0.356±0.014, ρ_advantage=0.151±0.006

Artifact 已注册：`art_20260522_70d316`

---
