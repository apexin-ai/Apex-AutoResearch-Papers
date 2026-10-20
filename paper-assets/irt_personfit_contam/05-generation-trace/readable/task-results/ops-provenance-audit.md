# ops provenance audit

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_provenance-audit_20260523T111531_result.json`
- **Structured JSON:** [`be817204836d18a9e378.json`](../../sessions/be/be817204836d18a9e378.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计报告已注册（`art_20260523_dbe80e`）。

审计总结：66 个数值逐一追溯验证，55 个 ✅ 匹配，3 个 ❌ 不一致，8 个 🔍 无法追溯。最关键的问题是 `results.tex` 正文中 Llama clean baseline 写成了 +0.29 (SD=1.45)，实际数据为 -0.31 (SD=0.83)——表格里的 Cohen's d 是用正确数据算的，只是 prose 描述错了。

---
