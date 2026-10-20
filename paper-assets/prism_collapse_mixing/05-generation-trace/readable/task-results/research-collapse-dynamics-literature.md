# research collapse dynamics literature

**prism collapse mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_collapse-dynamics-literature_20260515T234037_result.json`
- **Structured JSON:** [`8a21882313a2e0e48149.json`](../../sessions/8a/8a21882313a2e0e48149.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

**Collapse 是加速的，不是线性的。** 三条独立证据线汇合：
1. **DPI 指数衰减**（λ=0.2–0.4/iter）——信息损失是乘性的
2. **两阶段 collapse**（Shumailov Nature 2024）——early 阶段表面温和但尾部已在消失，late 阶段发生相变式坍缩
3. **Generalization→Memorization 转变**（He NeurIPS 2025）——数据 cluster 化存在临界点，越过后 entropy 急剧下降

**对我们实验的直接影响：**
- 线性外推 Gen 3 ≈ 0.88 几乎肯定**低估**退化，指数模型预测 0.82–0.86，含相变风险则可能低至 0.75
- **Gen 2 是关键观察点**——如果 Δρ ≥ 0.03（相比 Gen 0→1 的 0.017），说明已进入加速区
- Loss-entropy decoupling 有大量文献支持——loss 平稳不代表没有 collapse
- 50/50 混合比低于文献建议的稳定阈值（≥62% real 或 ≥70% real）

---
