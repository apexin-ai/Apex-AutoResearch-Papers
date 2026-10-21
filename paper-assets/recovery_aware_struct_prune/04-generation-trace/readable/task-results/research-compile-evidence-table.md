# research compile evidence table

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_compile-evidence-table_20260516T051959_result.json`
- **Structured JSON:** [`ea573719d1801e3c2727.json`](../../sessions/ea/ea573719d1801e3c2727.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。文件写入 `artifacts/evidence_table.md` 并注册。

**核心发现**：

**一致性审查结果**：paper_framing.md 中 14 个关键数字与 registry 全部匹配，发现 3 个问题：

1. **⚠️ grad→0.007** — paper_framing.md 引用了 RASP collapse 时的 grad_norm=0.007，但 registry 中 v9=1.398、v8=0.011，均不匹配。需核查 W&B run mrikafz3 的 step-level 数据。
2. **⚠️ Unpruned frac_zero_std ≤0.275** — registry 中无此数据，可能来自 W&B，需验证。
3. **⚠️ step-90 estimate** — paper 写 "~81.00%"，实际 registry 值为 80.59%，应更正。

**3 个 RUNNING 实验**：unpruned step-100 和 step-90 eval 看起来已完成（有完整 1319 结果）但 status 未更新；RASP step-10 eval 仅完成 249/1319。

**Claim 强度**：Claim 1（decoupling）和 Claim 2（collapse gradient）证据充分；Claim 3（tradeoff）的 SFT 方向仍是关键弱点（p=0.25）。

---
