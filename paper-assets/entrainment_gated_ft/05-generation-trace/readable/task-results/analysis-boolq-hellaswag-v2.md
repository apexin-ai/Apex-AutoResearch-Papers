# analysis boolq hellaswag v2

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_boolq-hellaswag-v2_20260520T125546_result.json`
- **Structured JSON:** [`f2db3058da5e51b73f8a.json`](../../sessions/f2/f2db3058da5e51b73f8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 JSON 已写入本地 artifacts 并注册，formal_multiplicity_metrics.json 已更新。汇总：

| Benchmark  | N     | ᾱ (ambiguity) | J̄_helped | J̄_hurt | ρ_σ   | p_σ   |
|-----------|-------|---------------|----------|--------|-------|-------|
| HellaSwag | 10042 | 0.098         | 0.091    | 0.080  | -0.80 | 0.133 |
| ARC-Easy  | 2376  | 0.213         | 0.092    | 0.096  | -0.20 | 0.78  |
| LAMBADA   | 5153  | 0.302         | 0.086    | 0.091  | -1.00 | 0.017 |
| BoolQ     | 3270  | 0.487         | 0.103    | 0.098  | +0.10 | 0.950 |

关键发现：
- **HellaSwag** 的 ᾱ 极低（~0.10），3 个架构在 90% 的样本上完全一致（全对或全错），说明 HellaSwag 对架构差异不敏感。所有 Jaccard p<0.001，helped/hurt overlap 显著高于随机，但 nES 很小（0.05–0.11）。σ 收敛趋势 ρ=-0.80 但 p=0.133（不显著）。
- **BoolQ** 的 ᾱ 最高（~0.49），接近一半样本存在架构分歧。Jaccard 呈现有趣的**选择性重叠**：GDN-RetNet 对在所有 ratio 下都显著（p<0.01），但 GDN-HGRN2 和 RetNet-HGRN2 在多数 ratio 下不显著甚至显著低于随机（nES 为负）。σ 收敛无趋势（ρ=0.10, p=0.95）。

---
