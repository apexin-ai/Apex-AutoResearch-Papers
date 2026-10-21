# analysis loglik range diagnostic

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_loglik-range-diagnostic_20260520T173004_result.json`
- **Structured JSON:** [`279a055ed7ebc9b8f47a.json`](../../sessions/27/279a055ed7ebc9b8f47a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact 已注册。结果总结：

**假说不成立。** BoolQ 的 loglik range 并不比 LAMBADA 更窄：

| Benchmark | Mean IQR | Mean Range | CV |
|-----------|----------|------------|-----|
| LAMBADA | 0.86 | 4.13 | 0.75 |
| BoolQ | 0.90 | 4.61 | 0.22 |
| ARC-Easy | 7.35 | 50.09 | 0.55 |
| HellaSwag | 46.17 | 158.65 | 0.49 |

关键发现：
- BoolQ 和 LAMBADA 的 IQR/range 几乎相同（~0.9 / ~4.5），因为两者的 completion 都很短（BoolQ: " yes"/" no"，LAMBADA: 单 token）
- HellaSwag 和 ARC-Easy 的 IQR 大 1-2 个数量级，因为 completion 是多 token 长句
- **驱动 loglik range 的是 completion token 长度，不是选项数量（2 vs 4）**
- BoolQ 的 CV（0.20-0.25）远低于其他 benchmark（0.49-0.86），说明 BoolQ loglik 分布确实更集中，但这是 short-completion 效应，LAMBADA 也有类似特征（只是 CV 更高因为 mean 更小）

BoolQ C1 confidence margin 失效需要另外的解释——不能简单归因于 binary MC 的 loglik 压缩。

---
