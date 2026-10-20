# research citation verification

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_citation-verification_20260515T025744_result.json`
- **Structured JSON:** [`f7a8ae6cf49932dba75c.json`](../../sessions/f7/f7a8ae6cf49932dba75c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。报告已写入 `artifacts/citation_verification_report.md`。

**结果概要**：27 篇引用全部真实存在，无幻觉论文。但有 **7 处元数据错误**需修正：

| 问题 | 严重性 |
|------|--------|
| **Longpre 2020**: 标题、作者、venue 全错（混淆了另一篇论文） | ❗ 高 |
| **Luo 2023**: 7 个作者中 5 个是幻觉 | ❗ 高 |
| **Zhou 2023 LIMA**: 作者列表含 "Hinton" 等 5 个幻觉名字 | ❗ 高 |
| **Li 2024 ICLR**: 实际无 "Li"，应为 Yuan et al. | ⚠️ 中 |
| **Curriculum Robust**: 年份错 3 年（2021→2024） | ⚠️ 中 |
| **PALADIN literature_map**: +13.6% 未注明 baseline | ⚠️ 低 |
| **AgentPRM**: 缺 arXiv ID，与同名论文混淆 | ⚠️ 低 |

---
