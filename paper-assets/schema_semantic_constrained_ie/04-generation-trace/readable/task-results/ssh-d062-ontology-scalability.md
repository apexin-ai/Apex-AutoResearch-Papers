# ssh d062 ontology scalability

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d062_ontology_scalability_20260519T041125_result.json`
- **Structured JSON:** [`20585c3102ffa51f19c7.json`](../../sessions/20/20585c3102ffa51f19c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

d062 完成。结果摘要:

**编译 Benchmark**: 总编译时间从 0.33s (SciERC, 6 types/7 rels) 到 0.42s (XLarge, 200 types/1000 rels)，仅增加 1.25x。Grammar 编译是主要开销且几乎不随 ontology 规模增长 (~0.32-0.36s)；semantic 编译线性增长但极快 (0.4ms → 17ms)。

**推理 Overhead**: 全部 4 个规模的 constrained inference overhead 稳定在 **2-3%** (1.02x-1.03x)，从 small 到 xlarge 无显著增加。Zero failures。

**结论**: OntoCoDec 可以高效扩展到 200+ entity types / 1000+ relations，编译 <0.5s，推理 overhead ~3%。Limitations 中关于"scalability to large ontologies"的 gap 可以用这组数据消除。

**产出**:
- 远程脚本: `/root/schema_semantic_constrained_ie/scripts/ontology_scalability_benchmark.py`
- 合成 ontology: `/root/schema_semantic_constrained_ie/data/synthetic/ontology_{large_100,xlarge_200}.json`
- 报告: `artifacts/d062_ontology_scalability_results.md`
- Registry: `d062_ontology_scalability` → DONE (success)

---
