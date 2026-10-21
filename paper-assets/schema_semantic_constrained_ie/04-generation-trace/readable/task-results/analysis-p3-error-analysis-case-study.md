# analysis p3 error analysis case study

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_p3_error_analysis_case_study_20260518T142239_result.json`
- **Structured JSON:** [`1a2cff7af2e093429e8a.json`](../../sessions/1a/1a2cff7af2e093429e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P3 Error Analysis 完成。产出：

**`artifacts/p3_error_analysis.md`** -- 结构化分析报告，包含：
- 全模型全数据集违规率汇总表（SciERC + DocRED, 8B x3 + 70B）
- DR 违规按关系类型分布（Feature-of 是 SciERC 头号违规源，占 50-60%）
- 模型间差异：Mistral BPE 碰撞导致 constrained DR 不降反稳（13.4% SciERC, 33.2% DocRED）
- 70B vs 8B：70B unconstrained 已比 8B 低 58% DR，70B+OntoCoDec 达到 0% DR
- CF tradeoff 量化：constrained 下 CF 实体数增加 27-179x

**`artifacts/p3_case_studies.tex`** -- 4 个 LaTeX-ready case study：
1. **DR 纠正**（Feature-of Task→OtherScientificTerm → Task→Task）
2. **RV+DR 消除**（DocRED 自然语言关系名 → P-code + 类型修正）
3. **Scale 效应**（同一输入 8B vs 70B 的违规模式差异）
4. **Limitation**（constrained 改变生成轨迹导致丢失正确 triple）

---
