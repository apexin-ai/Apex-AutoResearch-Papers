# bugfix heatmap data source

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_heatmap_data_source_20260514T145100_result.json`
- **Structured JSON:** [`fc5ff7034fb920d9289c.json`](../../sessions/fc/fc5ff7034fb920d9289c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/heatmap_data_audit.md` 并注册。

核心发现：

1. **Voting Conf 差异根因**：`pilot_004/samples.jsonl` 和 `exp_012_logprob/samples_with_logprobs.jsonl` 是两次**独立推理**产生的不同 samples（已通过对比第一个 instance 的 entity 内容确认）。算法一致，数据不同。Voting conf 对 sample 组成高度敏感，所以差异最大 (Δ=0.110)。

2. **RE cond SJ = 0.372**：最匹配 pilot_005 的 0.3716 (T=0.7)，而图表声称 T=1.0。exp_015 统一值为 0.3683。

3. **Heatmap 混用至少 3 个数据源**：pilot_004 原始 samples（SJ/FK/Voting/EM）、exp_012 重新推理 samples（Logprob）、可能还有 pilot_005（RE cond SJ）。

4. **推荐方案 A**：统一使用 exp_015 输出。但需注意 Voting conf 从 0.39→0.50 会改变 signal ranking 叙事。

---
