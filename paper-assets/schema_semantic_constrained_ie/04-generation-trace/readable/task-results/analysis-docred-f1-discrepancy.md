# analysis docred f1 discrepancy

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_f1_discrepancy_20260514T133716_result.json`
- **Structured JSON:** [`c33c32c7d6376e715288.json`](../../sessions/c3/c33c32c7d6376e715288.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调查完成。以下是完整结论。

---

## 调查结果

### 根因

两个 Worker 使用了不同的 **predicted relations 统计范围** 来计算 F1 denominator：

| | Worker A (R-F1=9.33%) | Worker B (R-F1=7.69%) |
|---|---|---|
| **方法** | `recognized_set` — 只计入能归一化到有效 PID 的 triples | `all_set` — 计入所有 triples（含 out-of-vocabulary） |
| **unconstrained pred count** | 12,214 | 17,355 |
| **差异来源** | 过滤掉了 5,189 个 relation_vocabulary_violation triples | 包含所有 triples |
| **tp / gold** | 1137 / 12,021~12,154 | 相同 |

Recall 一致（~9.4%）是因为 tp 和 gold 相同。Precision 差异完全来自 denominator：1137/12214=9.31% vs 1137/17355=6.55%。

### 正确方法

**`method_all_set`（Worker B）是公平的比较方法**，因为：
- Out-of-vocabulary predictions 是真实的模型错误（false positives），不应从 denominator 中移除
- 对于 constrained decoding（grammar_only / full_s1），几乎没有 vocab violations（仅 5 个），两种方法结果一致
- `recognized_set` 人为抬高了 unconstrained 的 precision，隐藏了无约束解码产生大量无效 relation type 的代价

### 统一评估结果（method_all_set）

| Mode | R-P | R-R | **R-F1** | Records | Unrecognized Rels |
|---|---|---|---|---|---|
| unconstrained | 6.55% | 9.46% | **7.74%** | 998 | 5,189 |
| grammar_only | 7.06% | 10.12% | **8.31%** | 998 | 5 |
| semantic_only | 6.53% | 9.59% | **7.76%** | 911* | 4,830 |
| full_s1 | 6.99% | 10.01% | **8.23%** | 999 | 5 |

*semantic_only 记录数较少，可能尚未跑完

### Delta（unconstrained → full_s1）

- **R-F1: +0.49pp**（full_s1 更好）
- R-P: +0.44pp, R-R: +0.55pp
- Entity F1: +1.22pp（0.5815 → 0.5937）

### 被误导的结论（Worker A 的 recognized_set 方法）

用 recognized_set 算，unconstrained 得 9.38%，full_s1 得 8.23%，delta=-1.15pp — 会错误地认为 constrained decoding 降低了 F1。实际上这是因为 unconstrained 的 5,189 个无效 prediction 被排除了。

### `f1_report_docred_unconstrained_phase2.json` 的来源

该文件中的数值（pred=12214, tp=1137, R-F1=9.33%）完全吻合 `recognized_set` 方法——某个脚本在计算 F1 前先过滤掉了无法映射到 PID 的 predicted relations。

---
