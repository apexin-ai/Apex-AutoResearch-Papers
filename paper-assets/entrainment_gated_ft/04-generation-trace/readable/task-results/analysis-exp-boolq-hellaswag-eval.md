# analysis exp boolq hellaswag eval

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-boolq-hellaswag-eval_20260520T124927_result.json`
- **Structured JSON:** [`2961a8cdb13d24322cda.json`](../../sessions/29/2961a8cdb13d24322cda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Accuracy

**BoolQ** (acc):
| | pure | h24-1 | h12-1 | h6-1 | h3-1 |
|---|---|---|---|---|---|
| **GDN** | 0.585 | **0.489** | 0.635 | 0.570 | 0.622 |
| **RetNet** | 0.611 | 0.604 | 0.606 | 0.622 | 0.581 |
| **HGRN2** | 0.574 | 0.609 | 0.609 | 0.617 | 0.636 |

**HellaSwag** (acc_norm):
| | pure | h24-1 | h12-1 | h6-1 | h3-1 |
|---|---|---|---|---|---|
| **GDN** | 0.608 | 0.597 | 0.610 | 0.606 | 0.603 |
| **RetNet** | 0.580 | 0.582 | 0.588 | 0.585 | 0.578 |
| **HGRN2** | 0.599 | 0.602 | 0.607 | 0.606 | 0.604 |

### Cross-Architecture Per-Example Analysis

**BoolQ** — 最高 multiplicity，无 convergence：
- Cross-arch std 无趋势：**ρ=-0.30, p=0.62**
- Multiplicity 极高：**44.5%-52.1%** 样本跨架构不一致
- Mean Jaccard: 0.531-0.612

**HellaSwag** — 极高 agreement，弱趋势：
- Cross-arch std 边际趋势：**ρ=-0.80, p=0.10**
- Agreement 极高：**89.7%-90.9%** 样本三架构完全一致
- Multiplicity 很低：仅 **9.1%-10.3%**
- Mean Jaccard: 0.859-0.876

### 四 Benchmark 光谱（按 multiplicity 排序）

| Benchmark | Multiplicity α | Aggregate ρ | p |
|---|---|---|---|
| HellaSwag | ~10% | -0.80 | 0.10 |
| ARC-Easy | ~21% | -0.20 | 0.78 |
| LAMBADA | ~30% | -1.00 | 0.017 |
| **BoolQ** | **~50%** | -0.30 | 0.62 |

**关键发现**：
1. BoolQ 有最高 multiplicity（~50%），远超其他 benchmark，但无 aggregate convergence → 进一步强化 decoupling 叙事
2. HellaSwag 是"无效应" benchmark——三架构几乎完全一致（Jaccard>0.86）
3. Task 特性主导 multiplicity 程度，attention ratio 影响次要
4. **GDN h24-1 BoolQ acc=0.489 异常偏低**（其余 0.57-0.64），可能需要确认

---
