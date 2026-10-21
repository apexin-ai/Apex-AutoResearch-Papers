# research literature freshness check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature_freshness_check_20260518T161900_result.json`
- **Structured JSON:** [`e75456ab3f082cc7fd16.json`](../../sessions/e7/e75456ab3f082cc7fd16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/literature_freshness_check.md` 并注册。

核心发现：

**最重要遗漏：BoostCD/BoostIE (EMNLP 2025 Main)**。同样用 constrained decoding 做 closed IE，但通过 boosting 组合 constrained+unconstrained 两组输出。必须在 Related Work 中 address，差异化点是 OntoCoDec training-free 且区分格式层/语义层约束。

**需 address 的质量风险：** Grammar-Aligned Decoding (NeurIPS 2024)、The Format Tax (2026)、The Hidden Cost of Structure (RANLP 2025) 均指出 constrained decoding 可能扭曲分布/降低质量。建议加消融实验证明 OntoCoDec 的 type constraints 不引入显著 quality degradation。

**替代范式需讨论：** SLOT、G&O、DCCD 都主张 "先自由生成再约束/格式化" 优于 inline 约束，需要实验对比 inline type constraints vs. post-hoc filtering 在 IE 上的效果。

---
