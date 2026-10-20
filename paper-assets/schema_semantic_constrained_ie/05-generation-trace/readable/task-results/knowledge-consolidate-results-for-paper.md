# knowledge consolidate results for paper

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_consolidate_results_for_paper_20260514T022941_result.json`
- **Structured JSON:** [`3396ef8ff87339a22f9a.json`](../../sessions/33/3396ef8ff87339a22f9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件: `artifacts/paper_results_summary.md`，包含：

- **Table 1**: SciERC 5 种解码模式对比 (unconstrained → full_s1/s2)，含 delta 表
- **Table 2**: DocRED Phase 0 unconstrained vs schema-informed，含跨数据集 prompt 有效性对比
- **Figure 数据**: 7 个 relation 在 5 种 mode 下的 DR 变化 + triple count 分母
- **Claim-evidence mapping**: 4 个 core claims 各对应具体 exp_id 和数字
- **CF 根因分析**: EVR 占 >90%，top 冲突 Generic↔OtherScientificTerm (60次)，grammar CF=0.08% 证明 CF 100% 来自 semantic 层
- **S1 vs S2**: S1 全面略优，S2 定位为 ablation
- **待补实验**: DocRED Phase 2 (2 个 RUNNING) + cross-model validation (stretch)

---
