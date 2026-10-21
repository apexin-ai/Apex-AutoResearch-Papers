# analysis sigma rectangularity

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sigma_rectangularity_20260515T140530_result.json`
- **Structured JSON:** [`4f3780859221c19517a6.json`](../../sessions/4f/4f3780859221c19517a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结果。

## Rectangularity 分析结果

### 1. σ(r) Rectangularity 概况

| Dataset | Total rels | Rectangular | Non-rect | 总 over-permissive rate |
|---------|-----------|-------------|----------|------------------------|
| **SciERC** | 7 | **0/7** | 7/7 | **33.3%** |
| **DocRED** | 96 | **23/96** | 73/96 | **36.8%** |

**没有一个 SciERC relation 是 rectangular。** DocRED 只有 23/96 是 rectangular（主要是 dom×range 本身就很小的 relations，如只有 1-2 个 valid pair 且 dom/range 各只有 1 个 type）。

### 2. SciERC 非 rectangular relations

| Relation | |σ(r)| | |dom×range| | Over-permissive | Rate |
|----------|--------|-----------|----------------|------|
| Compare | 17 | 36 | 19 | 52.8% |
| Hyponym-of | 21 | 36 | 15 | 41.7% |
| Part-of | 21 | 36 | 15 | 41.7% |
| Evaluate-for | 23 | 36 | 13 | 36.1% |
| Conjunction | 25 | 36 | 11 | 30.6% |
| Feature-of | 26 | 36 | 10 | 27.8% |
| Used-for | 35 | 36 | 1 | 2.8% |

SciERC 所有 relation 的 dom 和 range 都涵盖大部分 entity types（6×6=36 的笛卡尔积），但实际 valid pairs 远小于此。

### 3. 实际影响量化（Independent-valid but pair-invalid triples）

| Condition | DocRED full_s1 | DocRED unconstrained | SciERC full_s1 | SciERC unconstrained |
|-----------|---------------|---------------------|----------------|---------------------|
| Total triples | 17,341 | 17,497 | 1,729 | 1,724 |
| Pair violations | 1,770 | 3,157 | 16 | 265 |
| Independent violations | 1,279 | 2,199 | 0 | 14 |
| **Gap (indep-ok, pair-bad)** | **491** | **958** | **16** | **251** |
| **Gap / pair violations** | **27.7%** | **30.3%** | **100%** | **94.7%** |

关键发现：

- **SciERC full_s1**：16 个 pair violations 中，**100%** 被 independent enforcement 漏掉——所有 DR violations 都是 head_type ∈ dom(r) 且 tail_type ∈ range(r) 但 pair 不合法。Independent enforcement 对 SciERC **完全无法捕获** non-rectangular 的违规。
- **DocRED full_s1**：1,770 个 pair violations 中 491 个（27.7%）被 independent 漏掉。
- **DocRED unconstrained**：无约束时 gap 更大，958 个（30.3%）。

### 4. 主要 gap 来源 relations

**DocRED**：`influenced by`(97), `member of`(71), `author`(69), `location of formation`(52), `conflict`(35)

**SciERC**：`Evaluate-for`(8), `Feature-of`(6), `Compare`(2)

### 5. 对 §2/§3 的建议

**σ(r) 显著不是 rectangular。** Independent enforcement 是 pair-based 的松弛（over-approximation），在 SciERC 上捕获率为 0%，在 DocRED 上遗漏约 28% 的 pair violations。

§3 写作建议：
- **不能**写 "σ(r) is rectangular" — 数据不支持
- 应在 §2 形式化中明确定义 pair-based constraint σ(r) 和 independent constraint dom(r)×range(r) 的区别
- §3 可以走两条路：
  - **A**: 实现 pair-based enforcement，彻底解决 — 改动不大（约束检查从两个 set membership 改为一个 tuple lookup）
  - **B**: 保留 independent enforcement，但 §3 需要量化其 over-permissiveness bound，说明它是 σ(r) 的 outer approximation，并用实验数据说明实际 gap

结果已保存至 `/root/schema_semantic_constrained_ie/outputs/rectangularity_analysis.json`。

---
