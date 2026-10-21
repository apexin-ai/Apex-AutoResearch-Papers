# audit paper framing numbers check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_paper-framing-numbers-check_20260514T085836_result.json`
- **Structured JSON:** [`b3b093acfa86b984ffc1.json`](../../sessions/b3/b3b093acfa86b984ffc1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 审计结果

**主文数字全部正确** — 修正 Worker 已将所有 [A] 标签数字统一到 plan-012-full (11 tasks / 245 eps)，无残留的 30-task 错误数据。

逐项核查 10 个关键数字均与权威源一致：Δ_full=+29.60, Δ_nd=+2.84, DAF=90.41%, r=0.9698, p=8.12e-07, labels 86/9/150, death rates 42.9%/16.3%, 11 tasks/245 eps, find-non-living-thing n=40/Δ=+9.58, Δ_nd/Δ_full=9.6%。

Robustness Check 段的 30-task 数据正确标注为 [B] 且注明仅限 appendix。

**修正项**：数据源权威声明补充了第二条禁引条目 `results/plan_c_test_labels/implicit_sft.jsonl`（标签损坏）。已保存。

---
