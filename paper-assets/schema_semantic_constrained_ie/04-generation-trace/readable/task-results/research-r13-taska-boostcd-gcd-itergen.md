# research r13 taskA boostcd gcd itergen

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_r13_taskA_boostcd_gcd_itergen_20260520T190848_result.json`
- **Structured JSON:** [`98785dbb40afcd5fef94.json`](../../sessions/98/98785dbb40afcd5fef94.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已写入 `artifacts/r13_review/taskA_boostcd_gcd_itergen.md`。

核心发现：

- **三篇论文均不在 SciERC 上评测**，也没有任何共同评测数据集与 OntoCoDec 重叠
- **BoostCD / GCD** (同一团队 EPFL dlab) 做 Wikidata-grounded closed IE，输出为 Wikipedia 标题 + Wikidata 关系名，用 KB membership / CFG 约束——与 OntoCoDec 的 span-level NER+RE + schema semantic constraints 在任务定义、输出粒度、约束类型上均不同
- **IterGen** 完全不做 IE 任务（只做 SQL + privacy），仅在方法论层面（解码时施加语义约束）有关联
- BoostCD 最佳 F1 = 52.35 (Wiki-cIE Code)，GCD 最佳 F1 = 36.0 (SynthIE-text)——这些数字与 SciERC 上的 span-level F1 不可直接对比

这些数据足以支撑 Related Work 中 "different benchmarks, task formulations, and constraint types preclude direct numerical comparison" 的论断，同时提供了具体维度的差异证据。

---
