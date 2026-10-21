# research death avoidance literature

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_death-avoidance-literature_20260513T205941_result.json`
- **Structured JSON:** [`1d20426498744cb8699a.json`](../../sessions/1d/1d20426498744cb8699a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

调研完成。核心结论：

## "~93% death avoidance" 发现没有直接先例

没有找到任何论文量化过 "tool invocation / modality routing 的收益中 failure prevention vs positive guidance 各占多少"。这是 novel finding。

## 最接近的 5 篇论文

| 论文 | 关系 | 差异 |
|------|------|------|
| **"Check Yourself Before You Wreck Yourself"** (NeurIPS 2025 WS) | selective quitting for safety | 放弃任务 vs 切换modality继续完成；没有benefit decomposition |
| **Dead-Ends Avoidance** (ICRA 2024) | safe RL dead-end detection | continuous control robotics；没做收益分解 |
| **Intrinsic Fear** (Lipton 2016) | death avoidance in RL 的先驱 | 传统RL，不是LLM agent |
| **SwiftSage** (NeurIPS 2023) | ScienceWorld 双模块路由，84.7分 | 没分析路由收益来源 |
| **ReTool** (ICLR 2026) | RL学when to use code interpreter | implicit routing，没做failure vs positive分解 |

## Novelty claim 安全

- **强 novelty**: 首次量化 modality routing benefit decomposition
- **中等 novelty**: Episode-level counterfactual labeling 方法论
- **主要攻击面**: "trivial → just always-det"，回应：contribution 是 finding 不是 method；always-det 是强 baseline 正是 finding 的核心

完整调研已写入 `artifacts/literature_survey_death_avoidance.md`，涵盖 22 篇论文，附建议引用列表。

Sources:
- [SwiftSage](https://arxiv.org/abs/2305.17390)
- [Check Yourself Before You Wreck Yourself](https://arxiv.org/abs/2510.16492)
- [Safe RL with Dead-Ends Avoidance](https://arxiv.org/abs/2306.13944)
- [Intrinsic Fear](https://arxiv.org/abs/1611.01211)
- [ReTool](https://arxiv.org/abs/2504.11536)
- [Toolformer](https://arxiv.org/abs/2302.04761)
- [MTRouter](https://arxiv.org/abs/2604.23530)
- [Where LLM Agents Fail](https://arxiv.org/abs/2509.25370)
- [Towards Verifiably Safe Tool Use](https://arxiv.org/abs/2601.08012)
- [Avoiding Death through Fear](https://arxiv.org/abs/2506.05529)
- [ToolRLA](https://arxiv.org/html/2603.01620v3)
- [ScienceWorld](https://arxiv.org/abs/2203.07540)
- [ARES](https://arxiv.org/pdf/2603.07915)
- [Router-R1](https://arxiv.org/abs/2506.09033)
- [How Do LLMs Fail in Agentic Scenarios](https://arxiv.org/pdf/2512.07497)
- [BEACON](https://arxiv.org/html/2605.06078)
- [Learning How Hard to Think](https://openreview.net/forum?id=6qUUgw9bAZ)
- [Safe RL Survey (Garcia & Fernandez)](https://www.jmlr.org/papers/volume16/garcia15a/garcia15a.pdf)
- [SafeHarbor](https://arxiv.org/html/2605.05704)
- [AgentMath](https://arxiv.org/pdf/2512.20745)

---
