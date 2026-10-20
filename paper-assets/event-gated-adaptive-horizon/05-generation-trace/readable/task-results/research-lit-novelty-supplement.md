# research lit novelty supplement

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_lit-novelty-supplement_20260514T144926_result.json`
- **Structured JSON:** [`fd9a6c5b627f4bfb2665.json`](../../sessions/fd/fd9a6c5b627f4bfb2665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总如下：

## Part 1：真实性验证

| 论文 | 结果 | 备注 |
|------|------|------|
| **HarmonyDream** (Ma et al., ICML 2024) | **真实，信息正确** | arXiv:2310.00344，Tsinghua thuml 组，yaml 中已有条目无需修改 |
| **"Mind the Model, Not the Agent"** (Qiao et al., ECAI 2024) | **真实，信息正确** | arXiv:2310.15017，IOS Press 出版，yaml 中已有条目无需修改 |

## Part 2：4 篇新文献已添加

| 论文 | 验证状态 | category / role | 与我们工作的 differentiation |
|------|----------|----------------|--------------------------|
| **NE-Dreamer** (Bredis et al., arXiv:2603.02765) | 真实。CoRL 2026 尚未举行（11月），标为 arXiv preprint | direct-competitor | 改进 RSSM 预测质量（next-embedding 替代 pixel reconstruction），但不涉及 temporal abstraction 或 dt_embedding 问题——与我们正交 |
| **DyMoDreamer** (Zhang et al., arXiv:2509.24804) | 真实。实际 venue 是 **NeurIPS 2025**（非仅 2025） | direct-competitor | 动态调制 RSSM 提升 dynamics 特征提取，Atari 100k SOTA，但不涉及 variable-rate imagination 或 value overestimation 诊断 |
| **VanTA** (Liu et al., ICLR 2025) | 真实 | method-component | High-level VLM-guided skill abstraction（Franka Kitchen/Crafter），与我们 low-level dt-based imagination abstraction 层级不同 |
| **Agarwal et al. 2021** (NeurIPS 2021) | 真实，Outstanding Paper Award | evaluation | rliable 评估方法论（IQM、performance profiles），我们的 multi-seed 实验设计遵循此标准 |

## Part 3

HarmonyDream 和 Qiao et al. 信息均已确认正确，无需修正。

---
