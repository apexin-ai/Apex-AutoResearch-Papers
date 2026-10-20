# research literature docred compare

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-docred-compare_20260514T083650_result.json`
- **Structured JSON:** [`3306e9b7e2e856d22e17.json`](../../sessions/33/3306e9b7e2e856d22e17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/literature_docred_compare.md` 并注册。

核心发现：

1. **无可比数据** — 没有任何论文在 DocRED 上报告 constrained decoding 的 violation rate。我们的结果是该维度的首个 benchmark。

2. **三个 novel 维度**：
   - 4 层 violation taxonomy (ET/RV/DR/CF) 本身是新贡献
   - SciERC→DocRED 跨 schema 对比是首个 constraint scaling 实证
   - Per-relation violation 分布异质性分析无先例

3. **Framing 建议**：DR 在 DocRED 上只降 45.5%（vs SciERC 94%）不应回避，应定位为"首个实证发现：semantic constraint effectiveness 随 schema complexity 递减"——这比在简单 schema 上刷满分更有学术价值。最近的竞争者（Ru-LLM, BoostCD, ODKE+）要么不在 decode time 做 constraint，要么不报 violation rate，不构成直接对比。

---
