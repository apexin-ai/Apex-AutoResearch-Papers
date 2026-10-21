# extract scierc cf and docred progress

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_extract_scierc-cf-and-docred-progress_20260522T065044_result.json`
- **Structured JSON:** [`78ca60cdf402713f0a22.json`](../../sessions/78/78ca60cdf402713f0a22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据全部收集完毕。汇总如下：

---

## 任务 1: SciERC 70B LoRA CF% 数据

### Unconstrained
- **CF violations: 0** (0/1133 triples, CF% = 0.0%) — 已确认
- D/R violations: 17/1133 = 1.50%
- 总 violation: 17

### Constrained (S1)
- **CF violations: 15** (15/1129 triples, **CF% = 1.33%**) — 确认
- D/R violations: 0/1129 = 0.0% — S1 约束完全消除了 D/R violations
- 总 violation: 15（全部来自 CF）

### CF violation 详情：15个全部是 **entity type inconsistency**（同一 mention 在不同 triple 中被标注了不同 entity type）

报告中列出的 3 个示例：

| doc_id | mention | conflicting types |
|--------|---------|-------------------|
| INTERSPEECH_2008_20_abs_sent1 | "assumption" | Generic vs Method |
| NIPS_2002_18_abs_sent1 | "standard technologies" | OtherScientificTerm vs Task |
| C04-1036_sent0 | "evaluation criterion" | Generic vs Metric |

这说明 S1 约束解码成功消除了 D/R violations（17→0），但引入/暴露了 cross-field consistency 问题——同一个实体在不同关系中被分配了矛盾的类型标签。

---

## 任务 2: DocRED unconstrained 进度

- **进度: 184/998**（约 18.4%）— 注意总数是 998 不是 200
- 进程仍在运行（PID 881090，CPU 100%，已运行 ~4.4h）
- 最新处理到第 163 条（log 里的编号），已输出 184 行到 jsonl
- 按平均 ~55s/sample 估算，剩余 ~814 samples，预计还需 ~12.4h

---
