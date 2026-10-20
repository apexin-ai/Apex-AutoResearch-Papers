# analysis claim coverage audit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_claim-coverage-audit_20260514T061811_result.json`
- **Structured JSON:** [`a298d654e89f53fc9ee1.json`](../../sessions/a2/a298d654e89f53fc9ee1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。核心发现：

**Claims 1 & 2 证据充分（⭐⭐⭐⭐），但有 2 个必须修复的 eval 缺口：**

1. **🔴 CRITICAL — plan001-s43-r4 缺 eval_sta.py 评估。** 当前只有 sampling eval（`do_sample=True, temp=0.7`），违反 C004。3-seed 对比的 s43 ISR=0 这个数据点缺少标准化支撑。需要对 checkpoint 跑 eval_sta.py。

2. **🟡 HIGH — plan005 (convex ISR) 缺 eval_sta.py 评估。** 当前只有训练日志 metrics（可能用 binary `_fast_fn`）。这是 Claim 2 "penalty effect" 的唯一数据点。

**Claim 3（Cross-Logic Generality）无证据，plan006 未启动。** 11 天内完成 Prolog 全流程不现实，建议降级为 Future Work。

**2 个 RUNNING 实验的价值：**
- plan002-b01 (β=0.1)：填补 ISR 剂量-响应，非关键但 nice-to-have
- plan016 (1000 steps)：回应 reviewer "500 steps too short"，有价值但非 blocking

报告已写入 `artifacts/claim_coverage_audit.md` 并注册。

---
