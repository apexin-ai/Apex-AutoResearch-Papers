# research concurrent work fang buurmeijer

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_concurrent_work_fang_buurmeijer_20260522T140447_result.json`
- **Structured JSON:** [`20eedc65a798449e19f8.json`](../../sessions/20/20eedc65a798449e19f8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/concurrent_work_analysis.md`。

核心发现：

**Fang et al. (arXiv:2602.17659)** — 最直接的 concurrent work。与我们共享 LIBERO 平台和 counterfactual perturbation 思路，但分析层面完全不同：他们做 behavioral failure 评估 + 推理时 CAG 修复，我们做 representational dynamics 分析（Cohen's d, trained vs untrained）。两者互补：我们提供了他们观察到的 vision-override 现象的表征层解释。

**Buurmeijer et al. (arXiv:2603.05487)** — 方法层面的 concurrent work。与我们共享 linear probing on VLA hidden states 的方法论，但他们只 probe 低层 motor features（位置/抓手），我们 probe 高层 semantic features（language sensitivity）。他们的 observability/controllability 框架与我们的 counterfactual sensitivity 框架形成多层次互补。

两篇论文都不做 trained vs. untrained 对比，也都不做 cross-architecture 的 semantic-level probing — 这正是我们的独特贡献点。

---
