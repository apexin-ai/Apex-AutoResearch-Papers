# analysis r14 a7 random projection

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r14_a7_random_projection_20260518T182945_result.json`
- **Structured JSON:** [`de28b3a71656631d07e8.json`](../../sessions/de/de28b3a71656631d07e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

A7 完成。结果：

| Model | RP-384d Prec | Text Prec | ΔPrec | RP-384d BA | Text BA | ΔBA | RP-384d AUC | Text AUC | ΔAUC |
|-------|-------------|-----------|-------|-----------|---------|-----|------------|----------|------|
| R1-8B | 0.621±0.009 | 0.416 | **+0.205** | 0.787±0.004 | 0.647 | **+0.140** | 0.871±0.003 | 0.705 | **+0.166** |
| OT-7B | 0.371±0.001 | 0.244 | **+0.127** | 0.708±0.004 | 0.580 | **+0.128** | 0.779±0.008 | 0.597 | **+0.182** |
| R1-32B | 0.524±0.017 | 0.441 | **+0.083** | 0.686±0.010 | 0.601 | **+0.085** | 0.738±0.014 | 0.637 | **+0.101** |
| QwQ-32B | 0.563±0.003 | 0.391 | **+0.172** | 0.724±0.009 | 0.591 | **+0.132** | 0.800±0.005 | 0.624 | **+0.176** |

**结论：HS 优势不依赖 PCA 的 variance-preserving 性质。** 随机高斯投影到 384d 后，HS 在所有 4 个模型上仍显著优于同维度的 text embeddings（所有 bootstrap p=1.000），ΔBA +8.5 到 +14.0pp，ΔAUC +10.1 到 +18.2pp。跨 3 个 RP seed 的方差极小（std < 0.02），说明信号在高维空间中分布广泛，随机投影即可保留。

---
