# paper writing method v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_v2_20260514T092526_result.json`
- **Structured JSON:** [`ea6e6e30f4ceb801e4f0.json`](../../sessions/ea/ea6e6e30f4ceb801e4f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Method section v2 写入 `artifacts/_project/paper/method_v2_draft.md` 并已注册。

结构概要：
- **§3.1 Counterfactual Episode Collection** — 解释 per-step oracle 退化（98.2% tie rate）→ episode-level counterfactual 方案；pure-internal (ReAct) vs pure-deterministic；operational definition of deterministic computation；245 episodes / 11 task types
- **§3.2 Death-Aware Labeling** — 四个 mutually exclusive cases（death asymmetry / both dead / score comparison / tied alive）；label 分布 86/9/150
- **§3.3 Death Avoidance Factor** — DAF 公式、boundary case（Δ_full=0 → undefined）；Δ_full=+29.60, Δ_no_death=+2.84, DAF=90.41%；Pearson r=0.9698
- **§3.4 Rule-Based Baseline** — 三个 keyword list (v1: 85.8%, v2: 4.9%, v3: 2.8%) 全部退化；以 observation-based approaches 收尾

所有数值均来自 A-source（plan-012-full, 11 tasks / 245 episodes）。Labels 与 experiments_draft.md 中的 `\ref{sec:collection}`, `\ref{sec:daf}`, `\ref{sec:rule}` 一致。

---
