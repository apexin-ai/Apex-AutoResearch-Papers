# research literature supplement

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-supplement_20260514T054346_result.json`
- **Structured JSON:** [`5dae6f44c38da0b3a08f.json`](../../sessions/5d/5dae6f44c38da0b3a08f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。literature_map.yaml 从 26 篇扩充到 31 篇（5 新增 + 1 充实），YAML 验证通过。

## 补全结果

| # | key | title | category | role | 与本项目核心关系 |
|---|-----|-------|----------|------|----------------|
| 1 | `sigma2026spectral` | SIGMA: Scalable Spectral Insights for LLM Model Collapse | canary-metrics | direct-competitor | 最直接的 spectral canary 竞争者；Track I/II 双轨 Gram matrix 谱界 vs 我们的单标量 effective rank——我们用更低计算开销换取多指标 panel 集成 |
| 2 | `truong2025entropy` | Entropy Collapse: A Universal Failure Mode of Intelligent Systems | core-collapse | theoretical-foundation | 证明 Class 1 凸反馈系统 entropy collapse 是一阶相变，autocorrelation/variance 无预警。定义了 canary 失效的 regime boundary，我们需证明 canary 在 Class 2+ 中有效 |
| 3 | `fu2025selfconsuming` | A Theoretical Perspective: How to Prevent Model Collapse in Self-consuming Training Loops | data-mixing | theoretical-foundation | 恒定 real data 比例保证 STL 收敛，为 α-sweep 50% accumulation 条件提供理论基础 |
| 4 | `kalinowski2026topology` | Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index | canary-metrics | background | topology-based monitoring 正交路线，related work 需对比说明我们选择 spectral/calibration panel 的理由 |
| 5 | `wang2026contaminated` | Can Generative AI Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training | core-collapse | theoretical-foundation | 首个 universal approximator 下的正面收敛结果：收敛速率 = min(baseline rate, real data fraction)，为 α-sweep 提供理论上界 |
| 6 | `bakshi2026improvement` (充实) | From Collapse to Improvement | data-mixing | theoretical-foundation (升级自 background) | 补充 αt trajectory + nt scaling 决定 collapse/improvement/consistency 三 regime 的条件；新增 gaps 和 TV distance 指标 |

---
