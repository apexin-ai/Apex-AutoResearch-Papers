# analysis d042 re rerun

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d042_re_rerun_20260514T185144_result.json`
- **Structured JSON:** [`bd733722da076d61f73e.json`](../../sessions/bd/bd733722da076d61f73e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结果：

**过滤效果**：551 → 397 实例（移除 154 个空 gold relation，占 28%）

**Proxy 独立性修复**：过滤后所有 proxy 都变独立了
- `ent_count` |ρ|: 0.512 → **0.011** （彻底修复，之前的高相关完全由空 gold 实例驱动）
- `sent_len` |ρ|: 0.124 → 0.023
- `type_diversity` |ρ|: 0.481 → 0.071
- `rel_count`（新增）|ρ|=0.131

**Global Signal ρ 变化**（过滤前 → 后）：
- SJ: 0.063 → **0.281** — 从无信号变成有信号
- FK: 0.226 → 0.279
- logprob: 0.400 → 0.287
- voting_conf: 0.220 → **0.322**
- EM: -0.132 → **+0.165** — 翻正

**Sentence Length 分层**（Q1→Q4 信号递增）：SJ 从 0.110 到 0.473（Q1 vs Q4 Fisher z p=0.004*），表明较长句子中一致性信号更强。

结果、registry、artifact 均已保存在 `output/exp_009_v2_re_rerun/`。

---
