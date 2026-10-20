# research sgs failure literature

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_sgs-failure-literature_20260515T222534_result.json`
- **Structured JSON:** [`603c3de6557903c1f6d5.json`](../../sessions/60/603c3de6557903c1f6d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存到 `memory.md` 末尾，标题 "## 2026-05-15: SGS Failure Literature Survey"。

核心结论：

1. **无 full-pathway stop-gradient 先例**——没有论文在 MBRL world model 的多个 head 上同时 detach conditioning variable 梯度来控制 value overestimation。
2. **无 partial-vs-full 对比**——文献中不存在 "partial stop-gradient 失败但 full stop-gradient 成功" 的案例。
3. **无 novelty concern**——CIVO 诊断 + Full-SGS 方法 + partial 失败的实证，三个层面均无先例。
4. **最相关的 5 篇必引论文**：Lu & Schuurmans 2018（delusional bias）、PCGrad 2020（gradient surgery 范式）、VaGraM 2022（gradient-level 干预）、Gradient Routing 2024（selective gradient masking）、TAWM 2025（temporal conditioning，需区分）。

---
