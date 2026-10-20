# analysis exp005 4model degradation

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp005_4model_degradation_20260513T061801_result.json`
- **Structured JSON:** [`67e3942c6a0b6816ed43.json`](../../sessions/67/67e3942c6a0b6816ed43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 4×4 τ 矩阵结果（Kendall τ, first-pair AUC ranking）

|  | Pythia | OLMo | Qwen-rewrite | Qwen-cont |
|---|---|---|---|---|
| **Pythia** | — | **0.733** | 0.467 | **0.695** |
| **OLMo** | | — | 0.429 | 0.543 |
| **Qwen-rewrite** | | | — | **0.733** |
| **Qwen-cont** | | | | — |

### 关键判断

**Generation mode 是主因，架构是次因。**

1. **Qwen-cont vs Pythia τ=0.695**，远高于 Qwen-rewrite vs Pythia τ=0.467（Δ=+0.23）。切换到 continuation mode 后 Qwen 与 Pythia 的排序一致性大幅提升。

2. **Qwen-cont vs OLMo τ=0.543**，高于 Qwen-rewrite vs OLMo τ=0.429（Δ=+0.11）。提升幅度较小但方向一致。

3. **Qwen-rewrite vs Qwen-cont τ=0.733**——同架构不同 mode，排序一致性高但非完美，说明 mode 确实改变了部分 feature 的退化优先级。

4. **残余架构效应**：Qwen-cont vs OLMo (0.54) 仍显著低于 Pythia vs OLMo (0.73)，说明架构差异贡献约 30-40% 的 ordering 偏离。

**C2 claim 建议**：退化排序在 continuation mode 下大体一致（mode 是之前偏离的主因），但需注明不同架构仍存在残余差异。

Artifact 已注册：`art_20260513_f28dd5`

---
