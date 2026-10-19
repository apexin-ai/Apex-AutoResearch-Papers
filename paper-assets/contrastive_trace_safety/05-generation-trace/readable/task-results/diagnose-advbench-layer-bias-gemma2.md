# diagnose advbench layer bias gemma2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_advbench_layer_bias_gemma2_20260522T173007_result.json`
- **Structured JSON:** [`0d5bf03b44e5062216f2.json`](../../sessions/0d/0d5bf03b44e5062216f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。

**根因**：代码 bug — `phase_analyze()` 中 `best_key` 为 None 时未做 guard 直接下标访问，触发 `TypeError: 'NoneType' object is not subscriptable`。极端类不平衡（6 JB / 514 safe）+ 非 stratified split 导致某些评估返回空结果。

**现状**：已修复（添加 None guard + stratified split）。Phase 2 已单独重跑成功，layer selection bias 结论：Divergence = 22.0pp — REPLICATED。无需进一步操作。

---
