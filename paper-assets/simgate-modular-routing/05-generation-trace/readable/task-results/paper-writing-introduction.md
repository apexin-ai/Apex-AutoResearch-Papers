# paper writing introduction

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_introduction_20260514T014429_result.json`
- **Structured JSON:** [`d448bcf528a503985172.json`](../../sessions/d4/d448bcf528a503985172.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Introduction draft v1 已写入 `artifacts/_project/paper/introduction_draft.md` 并注册 (`art_20260514_d860d5`)。

**结构概览（4 段 + 贡献列表，~650 words）：**

1. **开场** — 从 catastrophic death 切入（非泛泛 LLM 成功论），指出 tool-use / adaptive computation 文献忽略 failure avoidance 作为 routing signal
2. **Oracle 退化** — per-step oracle 在 sparse-reward 下产生 98% ties，motivate episode-level 方法；自然引入 ReAct 作为 internal reasoning baseline
3. **核心发现** — episode-level counterfactual 揭示 Δ\_full=+37.9 → Δ\_no\_death=+0.2，death avoidance fraction 98.75%，r=0.989；label distribution 41%/0.5%/59% 确认不对称性
4. **三条贡献** — counterfactual methodology、death decomposition framework、empirical finding

所有 registry 数字已用 `[PLACEHOLDER: 值]` 标注，待 plan-001b 全量数据到位后替换。引用仅使用 Related Work 已确认的 cite keys，无新增引用。

---
