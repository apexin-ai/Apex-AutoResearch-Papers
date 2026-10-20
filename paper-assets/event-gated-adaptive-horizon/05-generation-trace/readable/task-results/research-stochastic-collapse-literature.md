# research stochastic collapse literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_stochastic-collapse-literature_20260514T220508_result.json`
- **Structured JSON:** [`d3c44d5d5fc7a3a2138f.json`](../../sessions/d3/d3c44d5d5fc7a3a2138f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。新增 8 篇论文到 `literature_map.yaml` 的 **Seed-Dependent Stochastic Outcomes in MBRL** section，并附带综合分析。

## 新增论文

| Paper | Year | Venue | Relevance | 核心关联 |
|-------|------|-------|-----------|---------|
| Lyle et al. — Capacity Loss | 2022 | ICLR 2023 | **5** | Feature rank collapse 是 failure 的 necessary but not sufficient condition → 直接对应 nve>1.5x 作为 marker 而非 deterministic predictor |
| Kumar et al. — DR3 | 2022 | ICLR 2022 | 4 | TD 学习的 implicit regularization 导致 feature aliasing → dt_embedding 放大跨时间步的 aliasing |
| Sokar et al. — Dormant Neurons | 2023 | ICML 2023 | 4 | 不同 seed 的初始化产生不同 dormancy pattern → 解释为何某些 seed 丧失自我修正能力 |
| Nikishin et al. — Plasticity Injection | 2023 | NeurIPS 2023 | 4 | 可作为诊断工具：如果注入 plasticity 能阻止 seed 0 的 collapse，则确认 plasticity loss 是 bifurcation 机制 |
| Lyle et al. — Normalization & Effective LR | 2024 | NeurIPS 2024 | 4 | Normalization 引发的 effective LR 衰减 → seed 2 自我修正的候选机制 |
| Schwarzer et al. — BBF | 2023 | ICML 2023 | 3 | Periodic resets 阻止 primacy bias → 潜在的 collapse 预防手段 |
| Farebrother et al. — Stop Regressing | 2024 | ICML 2024 | 3 | Categorical value training 提供 implicit regularization → DreamerV3 已使用但仍不足以阻止 dt_embedding 引发的 collapse |
| Colas et al. — Statistical Power | 2018 | arXiv | 3 | 2-seed 观测的统计功效分析 → 未来多 seed 验证的方法学基础 |

## 对 framing 的支撑总结

1. **Stochastic collapse 有先例**：plasticity loss 文献（Lyle 2022, Sokar 2023, Nikishin 2023）明确表明训练失败的 seed-dependency 来源于初始化 → 早期梯度动力学 → 神经元活跃模式的链式随机性。

2. **"nve>1.5x as diagnostic marker but not deterministic predictor" 有理论基础**：Lyle 2022 的 capacity loss 框架直接支撑 "necessary but not sufficient" 的 framing — feature rank collapse（类比 nve>1.5x）是学习失败的前提条件，但需要额外的 stochastic conditions 才会触发 collapse。

3. **Self-correction 机制**：Lyle 2024 (effective LR decay) + Farebrother 2024 (categorical value implicit regularization) 共同解释了 seed 2 为何能从 2.05x nve 自我修正到 0.38x — DreamerV3 的架构提供了部分隐式正则化，但是否足够取决于 seed-dependent 的参数范数增长速度。

---
