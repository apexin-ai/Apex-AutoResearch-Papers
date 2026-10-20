# analysis scierc n16 3seed selection f1

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_scierc_n16_3seed_selection_f1_20260515T130955_result.json`
- **Structured JSON:** [`c904da6989a6d88dbc54.json`](../../sessions/c9/c904da6989a6d88dbc54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文件已复制到本地。汇总结果：

## SciERC N=16 三种子 Selection F1 结果

**551 instances, 3 seeds (42/123/456), N=16 samples**

| Method | Mean F1 | ±σ | Δ Greedy | p(Fisher) |
|--------|--------:|----:|---------:|----------:|
| Greedy | 0.6184 | 0.0001 | — | — |
| Random | 0.5847 | 0.0014 | -0.0337 | — |
| **VC** | 0.5875 | 0.0053 | **-0.0309** | 1.000 |
| **SJ** | 0.6179 | 0.0023 | -0.0005 | 0.689 |
| **FK** | 0.6199 | 0.0022 | +0.0015 | 0.460 |
| **EM** | 0.6097 | 0.0037 | -0.0087 | 0.995 |
| **LP** | 0.6229 | 0.0067 | **+0.0045** | 0.076 |
| Oracle | 0.7871 | 0.0028 | +0.1687 | — |

**关键发现**：
- **LP 是最佳信号**（+0.45pp vs greedy），接近显著（p=0.076）
- **FK** 也正向（+0.15pp），但不显著
- **VC/EM** 显著低于 greedy
- **SJ** 约等于 greedy

## N=16 vs N=8 对比

| Signal | N=16 | N=8 | Δ(16-8) | N=16 Δg | N=8 Δg |
|--------|-----:|----:|--------:|--------:|-------:|
| SJ | 0.6179 | 0.6157 | +0.0022 | -0.0005 | -0.0043 |
| FK | 0.6199 | 0.6157 | +0.0042 | +0.0015 | -0.0044 |
| LP | 0.6229 | 0.6204 | +0.0025 | +0.0045 | +0.0004 |
| Oracle gap | 0.1687 | — | 0.1253 | — | — |

- **N=16 的 SJ/FK 从负 Δg 翻正**：N=8 时 SJ/FK 低于 greedy ~0.4pp，N=16 时 SJ 约平 greedy、FK 高于 greedy 0.15pp
- **Oracle gap 大幅扩大**（0.169 vs 0.125），说明 N=16 有更多 headroom
- **LP 在两个 N 下都是最好的信号**，N=16 进一步提升

---
