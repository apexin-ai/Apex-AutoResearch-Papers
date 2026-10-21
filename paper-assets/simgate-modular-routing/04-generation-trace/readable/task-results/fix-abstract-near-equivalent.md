# fix abstract near equivalent

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_abstract-near-equivalent_20260514T122922_result.json`
- **Structured JSON:** [`acd9c7ce6ae610ee8376.json`](../../sessions/ac/acd9c7ce6ae610ee8376.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务前提与当前文件状态不符：

1. **"near-equivalent"** — 不存在于任何 tex 文件中
2. **"small but non-negligible"** — 也不存在于任何 tex 文件中

当前 experiments.tex 中对 non-death gap 的描述是：
- 第20行：`the gap collapses to $\Delta_{\text{no\_death}} = +2.84$`
- 第26行：`When internal reasoning does not cause death, it performs comparably to deterministic computation.`

Abstract（main.tex 第18行）完全没有描述 non-death gap，只说 "death avoidance accounts for 90.41% of the routing signal"。

**结论：无需修改。** "near-equivalent" 已不存在，abstract 与 experiments 之间不存在措辞冲突。experiments.tex 中 "performs comparably" 与 $\Delta_{\text{no\_death}} = +2.84$（9.6% of full gap）在语义上一致——gap 确实很小。

如果你希望将 experiments.tex 的 "performs comparably" 改为更精确的 "small but non-negligible" 表述，我可以执行，但这不是必须的同步操作。

---
