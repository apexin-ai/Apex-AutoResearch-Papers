# audit framing reaudit tex scan

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_framing-reaudit-tex-scan_20260515T005515_result.json`
- **Structured JSON:** [`f9e2467239d92b4f9efb.json`](../../sessions/f9/f9e2467239d92b4f9efb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。报告已写入 `artifacts/framing-reaudit/inconsistency_list.md` 并注册。

**核心发现**：

- **P0 — 必须删除的 INVALID claims**: +17.6pp cmd_rep removal 效果（5处）、71% FP rate（3处）、"cmd_rep corrupts labels" 叙事链
- **P0 — 核心数字错误**: OH stag rate 6.6%→21.45%（4处）、probe FT 0.751→0.9763（5处）、cmd_rep fire rate 92.2%→5.39%（5处）、cross-agent gap 21.6pp→2.21pp（1处）
- **P1 — Framing**: "fundamentally structural" → "zero-shot transfer dominance"（4处）
- **P1 — probe ZS**: 0.528/0.530 → 0.5984（3处）
- **P2 — 支持文件**: writing_plan.yaml 8处旧值、SlopCodeBench 90%/80%→77%/75.5%

总计 40+ 处需修改，覆盖 abstract/introduction/method/experiments/analysis/conclusion/appendix 全部章节 + writing_plan.yaml。experiments.tex §5.5 (Command Repetition Ablation) 需整段重写。

---
