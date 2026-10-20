# verify citation fang2025

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_citation_fang2025_20260524T013504_result.json`
- **Structured JSON:** [`d3977dbc8bca5d0a4d5e.json`](../../sessions/d3/d3977dbc8bca5d0a4d5e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

核实完成。汇报如下：

---

## DualVLA (arXiv:2511.22134)
- **存在**: 是
- **作者**: Zhen Fang, Zhuoyang Liu, Jiaming Liu, Hao Chen, Yu Zeng, Shiting Huang, Zehui Chen, Lin Chen, Shanghang Zhang, Feng Zhao
- **涉及 reasoning erosion**: 间接涉及。DualVLA 承认 VLA fine-tuning 会导致 "erosion of multi-modal comprehension capabilities"（作为背景动机），但论文的核心命名现象是 **"action degeneration"**（在 specialist VLA 上加推理数据后动作性能下降）。reasoning erosion 是它试图解决的前提问题之一，但不是论文的分析焦点。
- **实际内容**: 提出 dual-teacher 蒸馏策略 + 双层数据剪枝，在保持推理能力的同时提升动作性能。引入 VLA Score 评估指标。

## "From Intention to Execution" (arXiv:2506.09930)
- **存在**: 是
- **作者**: Irving Fang, Juexiao Zhang, Shengbang Tong, Chen Feng (NYU)
- **发表时间**: 2025 年 6 月
- **涉及 reasoning erosion**: 不直接涉及。论文研究的是 **intention-to-execution gap**（VLM backbone 赋予 VLA 良好的感知理解和高层规划，但无法可靠转化为精确动作执行）。
- **核心结论**: 引入 50 个仿真任务的 probing suite，发现 VLA 在 out-of-distribution 观测下表现出 "coherent intentions but falter in action execution"。

## 判断

- **fang2025 引用是否错误**: **有问题，但不算完全错误。** DualVLA 确实讨论了 reasoning erosion 作为背景动机（VLA training 侵蚀多模态理解能力），所以引用它来支撑 "reasoning erosion" 概念是可辩护的。但这不是 DualVLA 的核心贡献或分析焦点——读者去查阅 DualVLA 时，看到的主要是 "action degeneration" 而非 reasoning erosion 的系统性分析。
- **"From Intention to Execution" 不是正确替代**: 这篇论文关注 intention-execution gap，而非 reasoning erosion，且作者是 Irving Fang（NYU），与 DualVLA 的 Zhen Fang 是不同的人。
- **建议修正**:
  1. **如果保留 DualVLA 作为 `fang2025` 的引用**：将 related_work.tex 第 11 行的描述从 "reasoning erosion" 改为更贴合 DualVLA 实际贡献的表述，如 "multi-modal comprehension erosion and action degeneration"
  2. **如果坚持引用 "reasoning erosion" 作为独立概念**：需要找到一篇专门研究此现象的论文（搜索结果中未发现以 "reasoning erosion" 为核心术语的 VLA 论文，这个术语可能是你们论文自己提出的）。如果是你们自己的概念，应在行文中明确说明而非引用他人。
  3. **DualVLA 仍值得引用**：可以在讨论 VLA training trade-off（推理 vs 动作能力之间的冲突）时引用，但应匹配其实际贡献来描述。

Sources:
- [DualVLA (arXiv:2511.22134)](https://arxiv.org/abs/2511.22134)
- [From Intention to Execution (arXiv:2506.09930)](https://arxiv.org/abs/2506.09930)
- [DualVLA HTML](https://arxiv.org/html/2511.22134)
- [From Intention to Execution - Project Page](https://ai4ce.github.io/INT-ACT/)

---
