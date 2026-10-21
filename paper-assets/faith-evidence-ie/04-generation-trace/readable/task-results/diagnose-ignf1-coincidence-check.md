# diagnose ignf1 coincidence check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_ignf1_coincidence_check_20260516T033953_result.json`
- **Structured JSON:** [`26244cb83646007607eb.json`](../../sessions/26/26244cb83646007607eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据已全部收集。汇报结果：

---

## 对比结果

### SFT no-evidence
- **来源**: `sft_no_evidence/metrics_v2.json`（已修正 Ign-F1）
- **ign_f1 = 0.4735509540** (47.36%)
- ign_precision = 0.4635744003, ign_recall = 0.4839663617

### CED reranker
- **来源**: `ced_reranker_poc/results.json`（全量 985 docs 版本）
- **ign_f1 = 0.4863674148** (48.64%)
- ign_precision = 0.4913090940, ign_recall = 0.4815241544

### 差异
- |SFT - CED| = **0.0128164608** (1.28 percentage points)
- 结论：**两者 Ign-F1 并不相同**。SFT no-evidence = 47.36，CED reranker = 48.64。Reviewer 的"两者都是 47.36"前提不成立。

---

## 额外发现：CED reranker 的 Ign-F1 计算可能有 bug

CED reranker 结果中 **ign 指标与非 ign 指标完全相同**：
- `ign_f1 == f1` = 0.4863674148
- `ign_precision == precision` = 0.4913090940
- `ign_recall == recall` = 0.4815241544

这意味着 Ign 计算没有实际过滤训练集事实（train_facts），等价于没做 Ign。对比 SFT no-evidence 的 v2（修正后）：
- f1 = 0.4893, ign_f1 = 0.4736（差 1.57pp，说明 Ign 过滤确实生效了）

**CED reranker 的 eval 脚本很可能没有加载 train_triples 来做 Ign 过滤。** 这是一个真实的计算 bug，但不是 Reviewer 怀疑的"共享计算路径"问题——而是 CED reranker eval 缺少 Ign 逻辑。

---
