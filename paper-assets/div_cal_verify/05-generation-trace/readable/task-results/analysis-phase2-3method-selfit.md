# analysis phase2 3method selfit

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_3method_selfit_20260513T094549_result.json`
- **Structured JSON:** [`0474ffedc77e839cd28e.json`](../../sessions/04/0474ffedc77e839cd28e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新到 DONE/success。图表在远程服务器，register_artifact 需要本地路径，跳过。

---

## 最终总结

### 1. phase2_3method_selfit 关键指标对比

**PPL（越低越好）**

| Gen | RGDS | Uncurated | External |
|-----|------|-----------|----------|
| 0 | 37.09 | 37.10 | 37.04 |
| 4 | 53.97 | 55.88 | **52.27** |
| 7 | 75.07 | 50.28 | **45.51** |
| Δ% | +102% | +36% | **+23%** |

**Selection Ratio（alignment ratio, 核心指标）**

| Gen | RGDS (internal) | External (contriever) |
|-----|----------------|-----------------------|
| 0 | 1.037 | 1.137 |
| 1 | **0.910** | 1.211 |
| 4 | **0.896** | 1.282 |
| 7 | **0.517** | 1.095 |

RGDS ratio 单调下降至 0.52，external ratio 全程 >1.0（范围 1.10-1.28）。

**Rare n-gram（Gen 7）**: External(0.0099) > Uncurated(0.0090) > RGDS(0.0051)

### 2. D009 MVP 判定: **PASS**

三条标准全部满足：
- **Alignment gap 确认**: RGDS 内部 embedding 的 selection ratio 从 1.04 跌至 0.52，证明内部表征与真实数据分布逐代偏离
- **External ratio 持续 >1.0**: gen4-7 = 1.28/1.11/1.12/1.10，外部 embedding 不受 collapse 影响
- **External rare > uncurated**: 0.0099 vs 0.0090，外部选择保留了更多多样性

额外发现：external_only 的 PPL 在 gen4 后**回落改善**（53.55→52.27→47.37→46.11→45.51），而 RGDS 持续恶化。这是 alignment gap 导致的级联效应——内部 embedding 失准 → 选错数据 → 加速 collapse。

### 3. seed123 状态

- 进程存活（PID 180459/180473），GPU 0 运行中
- 当前进度：Gen 4/7（刚完成 selection，开始训练）
- 已有 ratio: 1.08, 1.10, 1.15, 1.16, 1.14 — 与主实验一致（全部 >1.0）
- 预计完成：还需 ~80-120 分钟（约 11:30-12:10 CST）
- Registry 已更新为 RUNNING

### 4. GPU 利用率

| GPU | 显存占用 | 利用率 | 任务 |
|-----|---------|--------|------|
| 0 | 70.9 / 97.9 GB | 0%（采样瞬时值） | seed123 |
| 1 | 0 / 97.9 GB | 空闲 | 无 |

---
