# write experiments setup

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_write_experiments-setup_20260514T085919_result.json`
- **Structured JSON:** [`886954784dd9bb0a5144.json`](../../sessions/88/886954784dd9bb0a5144.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiments section 框架已写入 `docs/paper/experiments.tex`（v1），包含 4 个子节：

- **4.1 Models and Datasets** — DeepSeek-R1-Distill-Qwen-7B（28 layers, GQA 4 KV groups），GSM8K 校准+评测，Phase 2 扩展 benchmark 标注
- **4.2 Pruning Methods** — Standard importance-only / RASP (ours) / GRASPrune (ACL 2026)，35% sparsity 为主实验，公式和引用齐全
- **4.3 Recovery Methods** — GRPO RLVR，超参数全部标 `[TBD]`，Phase 2 对比 SFT 标注
- **4.4 Evaluation Metrics** — exact-match accuracy / recoverability Δacc / Spearman ρ correlation，Phase 2 扩展指标标注

3 条 provenance claims 已注册，全部关联 D001 决策和 MVP 实验。所有待填数据统一用 `\textbf{[TBD]}` 标记，MVP 结果出来后直接替换。

---
