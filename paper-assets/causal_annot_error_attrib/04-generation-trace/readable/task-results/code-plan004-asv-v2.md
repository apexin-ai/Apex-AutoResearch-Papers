# code plan004 asv v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-asv-v2_20260520T124147_result.json`
- **Structured JSON:** [`1e420a2ea64545cb9ce0.json`](../../sessions/1e/1e420a2ea64545cb9ce0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。总结：

## plan004_asv_framework 结果 (96.3s)

**Part 1-2**: `delta_range` 修复正常，δ>1 支持到 δ_max=1/(1-min_diag(C₀))。Confounding/mediation vulnerability ASV 全为 None（β_T=1.0, τ=0.5 的正向信号永远不会被误分类翻转——confounding bias 同号）。Collider protection ASV 在 0.82–9.01 范围，severity 越低越稳健。

**Part 3**: 单调性大规模违反（~75%）——|bias(δ)| 作为 δ 的有理函数天然非单调。最大违反量 ~1e-2，不影响 ASV 的正确性，但论文中不能 claim 单调性。

**Part 4**: Collider ASV bound 确认 tight（τ(ASV±ε) 横跨阈值）。

**Part 5**: Plim 公式精度完美——三个拓扑 1500 个随机场景 100% coverage。

**Part 6 (核心)**:

| | Naive Type I | ASV Type I | Naive Power | ASV Power |
|---|---|---|---|---|
| Confounding | 0.964–1.000 | **0.000** | 1.000 | 1.000 |
| Mediation | 0.697–0.954 | **0.000** | 1.000 | 1.000 |
| Collider | 0.047–0.074 | **0.000** | 1.000 | 1.000 |

ASV-informed test 消除了所有 false positives 同时保留了 100% power。机制：H₀ 下 plim(I)[τ]=0 → ASV=0（fragile），H₁ 下 τ(δ) 全程 significant → ASV=None（robust）。

---
