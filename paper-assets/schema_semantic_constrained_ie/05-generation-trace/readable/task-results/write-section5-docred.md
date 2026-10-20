# write section5 docred

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_section5_docred_20260514T175414_result.json`
- **Structured JSON:** [`e86f825532e272cc858c.json`](../../sessions/e8/e86f825532e272cc858c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入并注册。文件在 `artifacts/_project/paper/section5_docred_draft.tex`。

结构概览：
- **Table**: 4-way ablation，列结构与 SciERC table 完全平行（DR/ΔDR/RV/ET/CF/R-F1/E-F1），grammar 行 ΔDR 标 ↑42%
- **Core result**: DR↓44.8%, ET/RV→0%, F1-neutral (+0.49pp R-F1, 不 claim improvement)
- **Grammar layer**: ET/RV 泛化完美；DR 上升 +42% 的结构性解释（RV→valid name 后暴露 latent DR violations），用此论证 semantic 层必要性
- **Enabling dependency**: semantic-only DR↓25% 但 RV/ET 未消除；ET 10.44% side effect 一句带过 defer limitations；两数据集一致确认 grammar→semantic 依赖是架构属性
- **Constraint tightness**: DocRED tightness=0.842 (5.68 valid pairs) vs SciERC=0.333 (23 pairs)，DR 降幅与紧度反相关（45% vs 94%），定位为首个 constraint scaling 实证 contribution

---
