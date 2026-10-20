# analysis per task cross analysis

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_per-task-cross-analysis_20260515T021235_result.json`
- **Structured JSON:** [`87ef3868e6270f24eab4.json`](../../sessions/87/87ef3868e6270f24eab4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已注册 (`art_20260515_d1414a`)。

**核心结论：恒定 6.4pp 差异是离散化伪迹，不是系统性惩罚。**

具体发现：

| 维度 | 结果 |
|------|------|
| 3 个 dose 点的 net penalty | 恒定 3 tasks (≈6.4pp) |
| 在**全部 3 个** dose 点出现的 penalty task | **0 个** |
| 在 2/3 dose 点出现的 | 4 个（且分布在不同 dose 对） |
| 仅在 1 个 dose 点出现的 | 5 个 |
| 涉及的 penalty task 总数（union） | 9 个不同 task |

每个 dose 点翻转的 task 几乎完全不同——没有固定的"taxonomy-sensitive task subset"。恒定 Δ=3 是 47-task 评估粒度的巧合（分辨率 ≈ 2.13pp/task），不反映 taxonomy injection 对特定 task 类型的系统性影响。

---
