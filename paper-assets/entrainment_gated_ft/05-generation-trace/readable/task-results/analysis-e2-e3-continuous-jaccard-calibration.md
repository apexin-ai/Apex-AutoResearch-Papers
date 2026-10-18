# analysis e2 e3 continuous jaccard calibration

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_e2_e3_continuous_jaccard_calibration_20260522T095214_result.json`
- **Structured JSON:** [`51e247140d175c66eac0.json`](../../sessions/51/51e247140d175c66eac0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

## E2: Continuous-Threshold Jaccard

| τ | LAMBADA J_helped | LAMBADA J_hurt | ARC-Easy J_helped | PIQA J_helped |
|---|---|---|---|---|
| 0.00 | 0.256 | 0.271 | 0.314 | 0.291 |
| 0.05 | 0.187 | 0.208 | 0.190 | 0.182 |
| 0.10 | 0.145 | 0.150 | 0.156 | 0.154 |
| 0.20 | 0.087 | 0.078 | 0.110 | 0.101 |
| 0.30 | 0.051 | 0.044 | 0.065 | 0.088 |

**结论**：Jaccard 随 τ 增大单调下降，在所有 benchmark 上均低于 0.32。HellaSwag 因 softmax 概率变化极小，τ≥0.05 时几乎无样本满足条件。低 Jaccard 不是 binary decomposition 的 artifact。

## E3: ECE Calibration

| 架构 | LAMBADA ECE (pure) | Disruption Threshold |
|---|---|---|
| GDN | 0.198 | 0.696 |
| RetNet | 0.233 | 0.998 |
| HGRN2 | 0.236 | 1.137 |

- ECE relative spread: **17.1%** vs disruption threshold relative spread: **46.7%**
- Spearman rho=1.0（仅 3 个点，rank 一致但 p 值无参考价值）
- PIQA/ARC-Easy 的 ECE 跨架构差异极小（<1%）
- HellaSwag ECE 全部在 0.41-0.42，几乎无差异

**结论**：calibration 差异的量级远小于 disruption threshold 差异，不足以解释后者。Threshold 差异反映真实的架构特异性，而非 calibration artifact。

---
