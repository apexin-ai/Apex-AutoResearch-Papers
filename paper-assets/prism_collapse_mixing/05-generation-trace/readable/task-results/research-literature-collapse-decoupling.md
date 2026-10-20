# research literature collapse decoupling

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_literature-collapse-decoupling_20260515T224520_result.json`
- **Structured JSON:** [`f0da3077c0084f45c801.json`](../../sessions/f0/f0da3077c0084f45c801.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`literature_map.yaml` 已写入。调研结果：

**Q1: 是否有人报告过 loss-collapse 信号脱钩？**
没有直接的系统实证。但 Truong 2025 理论预测 collapsed 系统可保持 loss 稳定；Schaeffer 2025 区分了 population risk 与 tail risk 可脱钩；He 2025 在扩散模型上发现 entropy-泛化强相关（与我们 Gen 0 的 ρ=0.929 一致），但未追踪跨代 ρ 变化。

**Q2: Collapse 信号监测方法论**
- **Entropy**: He 2025 (NeurIPS Spotlight) 用训练数据 entropy 做 collapse indicator
- **Spectral rank**: SIGMA (Gu 2026) 用 Gram matrix eigenspectrum；SA (Qiu 2025) 用 spectral alignment 分布
- **Diversity**: Zhu 2025 (ICML) 系统比较了 n-gram diversity / self-BLEU / DCScore

**Q3: 最相关 5 篇**

| 论文 | 关系 |
|------|------|
| He 2025 (NeurIPS) | 对照基线：entropy-泛化强相关，但未跨代追踪 |
| SIGMA (Gu 2026) | 方法互补：spectral 监测框架，未研究与 loss 的 ρ |
| Truong 2025 | 理论支撑：预测 loss 稳定但 entropy 坍缩，未实证 |
| Schaeffer 2025 Position | 概念框架：population risk ≠ tail risk |
| Qiu 2025 SA | 方法启发：spectral 信号比 loss 更早预警 |

**Novelty 定位**: 已有零散理论暗示，但缺乏系统实证验证。我们首次在 LLM 迭代合成训练中量化 ρ(loss, signal) 的跨代演变。novelty 成立。

---
