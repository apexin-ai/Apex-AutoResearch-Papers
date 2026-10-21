# analysis s2 cf diagnosis

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_s2-cf-diagnosis_20260522T204100_result.json`
- **Structured JSON:** [`a7c679970d273ab81b4c.json`](../../sessions/a7/a7c679970d273ab81b4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

## 结论：Not a bug，确认是 over-constraining cascading effect

### CF=18 的来源

**全部 19 个 CF violations（checker 归为 18，去重差异）都来自 `pass2_rel_tail`**：Pass 1 给 entity 分配了类型 X，但 Pass 2 生成 relation 时在 `tail_type` 字段写了不同类型 Y。

典型模式：
- Metric ↔ OtherScientificTerm（如 "transliteration accuracy", "parsing accuracy"）
- Method ↔ Task（如 "ASR System", "vision systems"）  
- OtherScientificTerm ↔ Generic（如 "attention", "intention"）

这些都是 genuinely ambiguous 的 entity typing，模型在 entity-only 和 relation 两个不同 context 下做出了不同判断。`TypeConstraintProcessor` 虽然 pre-register 了 Pass 1 types，但 grammar constraint 只约束 type name 合法性，不强制一致性。

### R-F1 暴跌（44.53→36.28, -8.25pp）的机制

**Pass 1 entity under-extraction → cascading relation wipeout：**

| 指标 | S1 beam4 | S2 | 差异 |
|------|----------|-----|------|
| Entity pred | 1785 | 1522 | -14.7% |
| Entity recall | 0.7029 | 0.5953 | -10.8pp |
| Total triples | 1283 | 1027 | -20.0% |
| 0-relation docs | ~71 | 112 | +57.7% |

关键瓶颈：**129/551 docs（23.4%）Pass 1 只提取了 ≤1 entity → 其中 112 docs（86.8%）relations 完全清零**。Pass 2 的 grammar 将 head/tail 枚举限制为 Pass 1 entity texts，任何 Pass 1 遗漏的 entity 永久丢失，无法参与 relation 抽取。

SciERC 是 sentence-level 数据集，很多句子只含 1-2 个 relation，entity-only extraction（缺少 relation context）系统性地 under-recall entities，导致 cascade failure。

### 对论文 claim 的影响

**不影响，反而支持论文叙事：**
- S2 作为 ablation 展示 pipeline decomposition 的 over-constraining 代价，justifies S1 single-pass 是更优方案
- CF 从 15→18：pipeline 甚至没能消除 type inconsistency，反而引入新的 cross-pass disagreement
- 这是 pipeline IE 的经典问题（error propagation），negative result 清晰可解释

---
