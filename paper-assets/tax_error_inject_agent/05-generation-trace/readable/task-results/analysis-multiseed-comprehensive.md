# analysis multiseed comprehensive

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_multiseed-comprehensive_20260514T210150_result.json`
- **Structured JSON:** [`731967850ffcc674aabc.json`](../../sessions/73/731967850ffcc674aabc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心发现：

1. **Vanilla 最稳定** (SD=3.3 pp)，注入方法波动 2-3 倍大 (TaxEI SD=10.5, Random SD=7.6)
2. **D012 "系统性损害" 结论 premature** — seed=42 下注入方法与 Vanilla 无差异甚至更好，seed=0 下才出现大幅下降。方法差异与 seed 高度交互，不是稳定主效应
3. **统计功效严重不足** — n=47 的 McNemar 需要 ~17 pp 才有 power，而观察效应 (11 pp 均值差) 与噪声 (10-15 pp 跨 seed 波动) 在同一量级
4. **Recovery eval**: Vanilla 61.7% 盲恢复 (detection=0)，TaxEI 结果将决定 taxonomy 是否有正面价值——如果 recovery ≤ 0.617 则全面 negative

---
