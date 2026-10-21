# research negative pattern analysis

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_negative_pattern_analysis_20260514T032102_result.json`
- **Structured JSON:** [`b3d9161fc9e2f7eef83c.json`](../../sessions/b3/b3d9161fc9e2f7eef83c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

文档已写入并注册 (`art_20260514_c907bc`)。核心内容：

- **实现 bug 类** (002/003/004)：3 条教训——跨模块 shape assert、canary metrics 前 1K 步验证、单变量实验
- **结构性发现类** (005/006/007)：hard Gumbel gate 关闭、dt 与 compounding error 超线性关系、peak-then-collapse 早停信号
- **008a vs 008c 解读**：打破了 3 条原始预测，新结论是 H（imagination steps 数量）才是关键变量，非 dt 本身；附 65K/105K 决策树
- **dt_embedding 风险评估**：008d 只能部分覆盖，需要额外实验 (008e: dt_embedding + dt=1 训练数据) 才能完全隔离 embedding 效应；建议等 008d 结果再决定

---
