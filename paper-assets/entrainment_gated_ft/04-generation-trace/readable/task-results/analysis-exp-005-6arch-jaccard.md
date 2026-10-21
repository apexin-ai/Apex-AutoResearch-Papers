# analysis exp 005 6arch jaccard

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-6arch-jaccard_20260522T173937_result.json`
- **Structured JSON:** [`284cd9fe2e0d04102e77.json`](../../sessions/28/284cd9fe2e0d04102e77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifact registered (`art_20260522_cc1e47`). All tasks complete. Summary:

---

## exp-005: HGRN 评估 + 6-arch Jaccard 分析

### Step 1: HGRN 评估结果

| Model | lambada_openai | arc_easy |
|-------|---------------|----------|
| HGRN h3-1 | 0.3586 | 0.6065 |
| HGRN pure | 0.2630 | 0.6157 |

HGRN 在 lambada 上 h3-1 大幅优于 pure（+9.6pp），在 arc_easy 上 pure 略优（-0.9pp）。与其他架构模式一致：hybrid 对 lambada 帮助大，arc_easy 上差异小。

### Step 2: 6-arch Pairwise Jaccard

**汇总统计（C(6,2)=15 pairs）：**

| Benchmark | mean J_helped | mean J_hurt | 显著对数 |
|-----------|--------------|-------------|---------|
| arc_easy | 0.1109 | 0.1032 | 15/15 |
| lambada_openai | 0.1295 | 0.0906 | 15/15 |

所有 30 个配对检验均显著（p<0.05, z>2.9），J_helped 一致高于 J_hurt。

**子组趋势（lambada J_helped）：**

| 子组 | mean J_helped | mean J_hurt | Δ J_helped |
|------|--------------|-------------|------------|
| 3-arch (GDN/RetNet/HGRN2) | 0.1194 | 0.0955 | — |
| 4-arch (+GLA) | 0.1219 | 0.0965 | +0.0025 |
| 5-arch (+DeltaNet) | 0.1221 | 0.0946 | +0.0002 |
| 6-arch (+HGRN) | 0.1295 | 0.0906 | **+0.0074** |

加入 HGRN 后 J_helped 增幅最大（+0.0074），J_hurt 下降最多（-0.004）。HGRN2-HGRN 对在 lambada 上 J_helped=0.1629，为全场最高——这两个同族架构共享了最多的 helped samples。

**已完成：** `jaccard_6arch.json` 生成并注册为 artifact，registry 已更新 `6arch_jaccard` metrics。无异常结果。

---
