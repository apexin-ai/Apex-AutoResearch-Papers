# analysis negative results audit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_negative-results-audit_20260518T214028_result.json`
- **Structured JSON:** [`08996bae5d05716939fd.json`](../../sessions/08/08996bae5d05716939fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已生成并注册。28 个阴性实验的分类结果：

| 分类 | 数量 | |
|------|------|---|
| **[已讨论]** | 17 | 论文正文或附录已覆盖 |
| **[应讨论]** | 4 | 有价值但论文未提及 |
| **[基础设施]** | 5 | 训练 bug、OOM、pipeline 问题 |
| **[已过时]** | 2 | 被后续实验取代 |

**4 个应讨论的实验**：

1. **plan-010-cross-task-v2** — 跨 task-type cluster 迁移失败（life→physical bal_acc=0.49），直接量化论文"signal is task-type-level"的定性声明。建议加入 Discussion。

2. **leave-one-tasktype-out** — 7/11 task types 只有 deterministic 一个类别，仅 4 types 有两类 signal。解释了 router 多数类坍塌的根因。建议加入 Discussion。

3. **plan-002-generative-v1** — 生成式 router 也失败（bal_acc=46.7%），证明 failure is signal-limited, not architecture-limited。建议加入 Appendix ablations。

4. **loto-guided-router-eval** — LOTO blind routing = always-det，keyword 变体靠泄漏 task identity 才达 0.63。建议加入 Appendix。

论文覆盖率整体良好（17/28 已讨论），4 个遗漏实验可用 2-3 句话补入 Discussion 和 Appendix，为已有定性论断提供定量支撑。

---
