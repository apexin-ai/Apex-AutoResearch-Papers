# code mistral v3 eval

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mistral_v3_eval_20260518T105307_result.json`
- **Structured JSON:** [`bfe23343b58e1206fd56.json`](../../sessions/bf/bfe23343b58e1206fd56.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部结果汇总如下：

## Mistral v3 Constrained (westd-21461)

| 指标 | 原始 | Post-hoc |
|------|------|----------|
| **Parse failures** | 28/246 (11.4%) | 同上 |
| **Entity F1** | P=0.191 R=0.085 **F1=0.1171** | F1=0.1171 (不变) |
| **Trigger F1** | P=0.036 R=0.042 **F1=0.0387** | F1=0.0387 (不变) |
| **Argument F1** | P=0.0025 R=0.0041 **F1=0.0031** | P=0.0025 R=0.0041 **F1=0.0031** (不变) |
| ET violations | 0 (0%) | 0 |
| EV violations | 0 (0%) | 0 |
| **RoV violations** | **0 (0%)** | 0 |
| **AC violations** | **86 (1.3%)** | **0 (0%)** |
| CF violations | 990 (14.9%) | 965 (14.6%) |
| **RoV+AC rate** | **0.0126** | **0.0000** |

Post-hoc 移除了 86 个 AC 违规 argument（6823→6737），RoV+AC 降至 0，F1 基本不变。

## Mistral grammar_only v3 (westd-16980)

| 指标 | 值 |
|------|-----|
| **Parse failures** | 28/246 (11.4%) |
| **Entity F1** | P=0.196 R=0.086 **F1=0.1192** |
| **Trigger F1** | P=0.033 R=0.035 **F1=0.0337** |
| **Argument F1** | P=0.0022 R=0.0033 **F1=0.0027** |
| ET violations | 0 (0%) |
| EV violations | 0 (0%) |
| **RoV violations** | **4050 (64.0%)** |
| **AC violations** | **872 (13.8%)** |
| CF violations | 71 (1.1%) |
| **RoV+AC rate** | **0.7773** |

## 关键对比

| | Constrained v3 | Grammar-only v3 |
|---|---|---|
| RoV+AC rate | **0.013 → 0.000** (post-hoc) | **0.777** |
| Argument F1 | **0.0031** | 0.0027 |
| Trigger F1 | **0.0387** | 0.0337 |
| Entity F1 | 0.1171 | **0.1192** |

Constrained 在 schema 约束遵从上远优于 grammar-only（RoV 0% vs 64%），F1 略高但两者绝对值都很低。两个实验 parse failure 数量相同（28/246）。

---
