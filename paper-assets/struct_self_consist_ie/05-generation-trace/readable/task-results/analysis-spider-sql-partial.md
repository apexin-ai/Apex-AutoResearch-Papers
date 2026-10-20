# analysis spider sql partial

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_spider_sql_partial_20260520T214803_result.json`
- **Structured JSON:** [`3c2640cde958d434e06b.json`](../../sessions/3c/3c2640cde958d434e06b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是核心结论：

## Spider SQL SC Pilot — 196/200 instances

**准确率**: Greedy 76.5%, MV 77.0% (+0.51pp), Oracle 80.6% (+4.1pp)

**关键发现**：SQL 呈现与 NER 完全不同的失效模式——

| | Spider SQL | NER (FewNERD/SciERC) | CoNLL |
|---|---|---|---|
| Degeneracy | **87.2%** | 10-27% | 85-89% |
| Dominant failure | F1 (degeneracy) | F2 (low agreement) | F1 (degeneracy) |
| MV gain | +0.51pp | varies | ~0 |
| Spearman ρ | 0.55 (ceiling artifact) | 0.30-0.42 | 0.43-0.47 |

**机制**：执行结果等价性将语法级多样性折叠为语义一致，87% instances 的 8 个 sample 产生完全相同的执行结果。非退化子集（n=25）上 MV 实际有效（+4pp），但占比仅 12.8%。

**论文价值**：跨任务普适性的对比案例——同一 F1-F4 diagnostic cascade 正确诊断了 SQL 的瓶颈（degeneracy），与 NER 的瓶颈（low agreement）形成对照。框架本身是任务无关的，只是主导失效模式随任务变化。

196 instances 统计充分（degeneracy 95% CI: 82-92%, ρ p<1e-16）。

已更新：registry metrics/conclusion/notes, artifact 注册, memory.md。

---
