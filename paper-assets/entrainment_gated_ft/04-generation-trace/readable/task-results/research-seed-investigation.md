# research seed investigation

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed_investigation_20260522T100734_result.json`
- **Structured JSON:** [`589b56d94fda6b68a8c7.json`](../../sessions/58/589b56d94fda6b68a8c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。核心结论：

## 调查结果摘要

### Task 1: Wang et al. Model Zoo
- **72 个模型全部是单 seed**，无 multi-seed checkpoints，无中间 checkpoints
- 训练用 fla + flame 框架，数据集 fineweb-edu
- HF collection: `m-a-p/hybrid-linear-attention-research`
- 服务器已有 16 个 340M 模型（GDN/RetNet/HGRN2 × 5 ratios + transformer baseline）

### Task 2: 训练可行性
- GPU: RTX PRO 6000 Blackwell (96GB) — VRAM 充足
- 340M 模型需 20B tokens 训练，单卡估计 **28-70 小时/seed**
- 2 seeds = 56-140 小时，加上环境搭建和调试 → **DDL 前不可行**
- flame 是分布式训练框架，单卡适配也需要额外工作

### Task 3: 替代方案 → **推荐 Pythia 410m 9-seed 实验**

| 策略 | 强度 | 时间 |
|------|------|------|
| **Pythia 410m × 9 seeds 评估** | 极高 — 直接量化 seed noise | **2-4 小时** |
| 现有 within-arch stability 分析 | 强 — sigma CI 不重叠 | 已完成 |
| 置换检验 z=6-9 | 强 — p<0.0001 | 已完成 |

**核心逻辑**：下载 Pythia 410m seed1-9（都是 Transformer，和我们的 340M 规模接近），跑 LAMBADA/ARC-Easy，算 seed-pair Jaccard。如果 Pythia seed-Jaccard << 我们的 cross-architecture Jaccard，就直接证明 architecture effect 远大于 seed noise。

这个实验可以**立即开始**，几小时内完成。

---
