# analysis cross arch summary

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cross_arch_summary_20260521T155716_result.json`
- **Structured JSON:** [`125fac3de50e7a5b3175.json`](../../sessions/12/125fac3de50e7a5b3175.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据收集完毕。以下是跨架构实验数据汇总。

---

## Cross-Architecture Probing Comparison Summary

### 1. R² Action Probing — Peak & Exit

**标准化格式数据 (image_mean / last_preaction)**

| 架构 | Suite | Cond | Layers | Peak Ly (img) | Peak R² (img) | Peak Ly (preact) | Peak R² (preact) | Exit R² (img) | Exit R² (preact) |
|------|-------|------|--------|--------------|---------------|------------------|------------------|--------------|-----------------|
| **OpenVLA** (Llama-2-7B) | Object | trained | 32 | L12 | 0.807 | L13 | 0.787 | 0.793 | 0.666 |
| OpenVLA | Object | untrained | 32 | L29 | 0.791 | L19 | 0.761 | 0.781 | 0.685 |
| **TracVLA** (Phi-3-mini) | Spatial | trained | 32 | L19 | 0.835 | L17 | 0.809 | 0.791 | 0.671 |
| TracVLA | Object | trained | 32 | L19 | 0.774 | L9 | 0.764 | 0.748 | 0.470 |
| TracVLA | Object | untrained | 32 | L20 | 0.753 | L23 | 0.690 | 0.736 | 0.681 |
| **NORA** (Qwen2.5-VL-3B) | Goal | trained | 36 | L10 | 0.697 | L9 | 0.688 | **-0.004** | **-0.004** |
| NORA | Goal | untrained | 36 | L9 | 0.735 | L15 | 0.660 | 0.656 | 0.619 |
| NORA | Spatial | trained | 36 | L10 | 0.721 | L24 | 0.720 | 0.553 | 0.417 |
| NORA | Spatial | untrained | 36 | L11 | 0.725 | L19 | 0.629 | 0.668 | 0.596 |

**旧格式数据 (overall_r2 / last_preaction only)**

| 架构 | Suite | Cond | Peak Ly | Peak R² | Exit Ly | Exit R² |
|------|-------|------|---------|---------|---------|---------|
| OpenVLA | Goal | trained | L19 | 0.677 | L32 | 0.618 |
| OpenVLA | Goal | untrained | L1 | 0.566* | L32 | 0.607 |
| TracVLA | Goal | trained | L11 | 0.634 | L32 | 0.549 |
| TracVLA | Goal | untrained | L6 | 0.585 | L32 | 0.391 |

*untrained OpenVLA Goal R² 曲线极不规则（MLP probe），L1=0.566, L4仅0.051, L16=0.535

### 2. L1 Attention — Instruction-Dominant Heads

| 架构 | Suite | Trained | Untrained |
|------|-------|---------|-----------|
| OpenVLA | Goal | **24/32** (75%) | 9/32 (28%) |
| OpenVLA | Object | **32/32** (100%) | 24/32 (75%) |
| TracVLA | Goal | **32/32** (100%) | 28/32 (88%) |
| TracVLA | Spatial | **30/32** (94%) | — |
| TracVLA | Object | **30/32** (94%) | 30/32 (94%) |
| NORA | Goal | **13/16** (81%) | 13/16 (81%) |
| NORA | Spatial | **12/16** (75%) | 14/16 (88%) |

### 3. Counterfactual Ranking (trained only)

| 架构 | Suite | Method | Ranking (高→低) | Top d/dist |
|------|-------|--------|-----------------|-----------|
| OpenVLA | Goal (10t) | MSE/Cohen's d | empty > wrong > shuffled > paraphrased | 0.978 |
| OpenVLA | Spatial | MSE/Cohen's d | empty > wrong > shuffled > paraphrased | 0.942 |
| OpenVLA | Object | MSE/Cohen's d | empty > wrong > shuffled > paraphrased | 1.212 |
| TracVLA | Spatial | MSE/Cohen's d | empty > shuffled > paraphrased > wrong | 1.327 |
| TracVLA | Object | MSE/Cohen's d | empty > shuffled > wrong > paraphrased | 1.212 |
| NORA | Goal | cosine dist | **all=1.0** (FAST+ invariant) | — |
| NORA | Spatial | cosine dist | wrong > empty > shuffled > paraphrased | 0.275 |

NORA untrained Goal counterfactual: empty(0.081) > shuffled(0.033) > wrong(0.014) > paraphrased(0.004)

### 4. 缺失条件

| 架构 | Suite | 缺失项 |
|------|-------|--------|
| OpenVLA | Spatial | R² probing 无标准化数据（仅有 counterfactual） |
| TracVLA | Spatial | untrained 目录为空，实验未跑 |
| TracVLA | Goal | 仅有 last_preaction R²（旧格式 10-seed），无 image_mean |
| OpenVLA | Goal | 仅有 overall_r2 MLP probe（旧格式），无 image_mean/last_preaction 分离 |
| NORA | Object | 未测试 |

### 5. 关键发现（纯数据层面）

**R² 峰值位置差异**：OpenVLA/TracVLA 中层偏后（L11-L19），NORA 早层（L9-L11）后急降——NORA Goal trained exit R² 近零（FAST+ action token 架构在终层擦除表征）。

**训练效应**：
- OpenVLA Goal trained-untrained Δ=+0.111（最大增益）
- TracVLA Goal Δ=+0.049, TracVLA Object Δ=+0.074
- NORA Goal image_mean trained(0.697) < untrained(0.735)——训练不增加而是重分配

**L1 attention 训练效应**：OpenVLA Goal 训练后从 9/32→24/32（+15 heads），OpenVLA Object 从 24→32。TracVLA/NORA 变化小。

**Counterfactual 一致性**：OpenVLA 三个 suite 一致 empty > wrong 排序；TracVLA wrong 排名下降（shuffled 反超 wrong）；NORA Goal trained 因 FAST+ 完全不敏感，但 intermediate layers 有 cosine distance 梯度。

---
