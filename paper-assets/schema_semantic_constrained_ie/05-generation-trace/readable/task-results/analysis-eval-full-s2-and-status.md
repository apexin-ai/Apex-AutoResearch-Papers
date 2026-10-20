# analysis eval full s2 and status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval_full_s2_and_status_20260514T020024_result.json`
- **Structured JSON:** [`855bc55e120173a63de0.json`](../../sessions/85/855bc55e120173a63de0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇总如下：

---

## 1. full_s2: 551/551 完成 ✅

| 指标 | 值 |
|------|-----|
| JSON 解析率 | 100% |
| Entity Type (ET%) | 0% |
| Relation Vocab (RV%) | 0% |
| **Domain/Range (DR%)** | **0.97%** (16/1644) |
| Cross-field (CF%) | 8.03% (179) |
| Entity F1 | P=0.2797, R=0.3712, **F1=0.3190** |
| Relation F1 | P=0.0640, R=0.1078, **F1=0.0803** |

**Per-relation DR violations:**

| Relation | Total | Violations | Rate |
|----------|-------|------------|------|
| Used-for | 855 | 1 | 0.12% |
| Feature-of | 328 | 4 | 1.22% |
| Evaluate-for | 118 | 6 | **5.08%** |
| Hyponym-of | 97 | 0 | 0% |
| Compare | 87 | 4 | 4.60% |
| Part-of | 80 | 1 | 1.25% |
| Conjunction | 79 | 0 | 0% |

## 2. S1 vs S2 对比表

| Mode | DR% | RV% | ET% | CF% | R-F1 | E-F1 |
|------|-----|-----|-----|-----|------|------|
| unconstrained | 15.37% | 1.39% | 0.4% | 0.08% | 0.0823 | 0.3101 |
| grammar_only | 14.84% | 0% | 0% | — | 0.0823 | 0.3098 |
| semantic_only | 11.65% | 1.51% | 0.4% | — | 0.0815 | 0.3101 |
| **full_s1** | **0.93%** | 0% | 0% | — | **0.0836** | 0.3098 |
| **full_s2** | **0.97%** | 0% | 0% | 8.03% | **0.0803** | **0.3190** |

**关键发现:**
- S2 的 DR% (0.97%) 与 S1 (0.93%) 基本持平，两种架构在约束违反率上效果相当
- S2 的 E-F1 (0.319) 比 S1 (0.3098) **高了 +0.92pp**，实体抽取质量提升
- S2 的 R-F1 (0.0803) 比 S1 (0.0836) **低了 -0.33pp**，关系抽取略有下降
- S2 的 CF% 较高 (8.03%)，说明两通道分离导致跨字段一致性下降
- Evaluate-for 和 Compare 是 DR violation 的重灾区（5.08% 和 4.60%）

## 3. DocRED grammar_only: 19/998 行

PID 150766 运行中，GPU 0 占用 16.7GB / 85% 利用率。进度约 1.9%，刚启动不久。按 SciERC full_s2 的速度估算（~551 样本/~1h），DocRED 998 样本预计还需约 1.5-2 小时。

---
