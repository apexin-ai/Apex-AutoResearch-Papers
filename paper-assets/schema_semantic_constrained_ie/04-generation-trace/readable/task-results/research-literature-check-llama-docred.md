# research literature check llama docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-check-llama-docred_20260516T051723_result.json`
- **Structured JSON:** [`df261dc6f831926b7396.json`](../../sessions/df/df261dc6f831926b7396.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结：

### 文献联动结果

**直接竞争者（可对比指标）：**
- **BoostCD (EMNLP'25)**：最直接竞争者，报告 constrained 比 unconstrained F1 高 5-13pp，但不涉及 FT composability。已加入 must_cite。
- **Frei & Kramer (Frontiers'24)**：Setup 最接近——grammar-constrained + fine-tuned + IE。FT+grammar F1 从 0.062→0.413。支持 composability 发现，但无 2×2 matrix。已升级为 must_cite。

**对立观点：**
- **Schall & de Melo (RANLP'25)**："Hidden Cost of Structure"。发现 constrained decoding 降低性能。调和点：IE 中 OOV→FP 机制使约束提升 F1；他们的任务无此机制。

**R-F1 +0.51pp 的文献支持：**
有充分文献支持 constrained decoding 在 IE 中提升 F1。核心机制：grammar 消除 OOV relation names，all_set 评估下 OOV = FP，消除后 precision↑。Frei & Kramer 和 BoostCD 均观察到同方向效果。

**Composability 创新点确认：**
**文献中无先例**——没有论文系统研究 constrained decoding + LoRA FT 的 2×2 composability matrix（跨模型跨数据集）。这是 OntoCoDec 的独特贡献。

已更新 `memory.md` 和 `artifacts/literature_map.yaml`（新增 BoostCD、升级 grammar_cd_clinical、添加 composability_gap 节、丰富 hidden_cost 条目注释）。

---
