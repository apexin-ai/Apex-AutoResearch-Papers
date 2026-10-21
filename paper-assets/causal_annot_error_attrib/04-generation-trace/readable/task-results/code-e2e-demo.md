# code e2e demo

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_e2e_demo_20260523T143128_result.json`
- **Structured JSON:** [`42092ec5654b48f068e9.json`](../../sessions/42/42092ec5654b48f068e9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功，结果符合预期：

- **Confounding**: naive bias = +22.71%, naive_plugin 和 MLA 的 improvement = 0.0%（FWL 不变性，校正无法改善 treatment coefficient），ASV magnitude δ* = 0.352
- **Exposure**: naive bias = -42.87%, PPI++ corrected bias = -0.22%, improvement = +90.9%，ASV magnitude δ* = 0.239

JSON 结果已写入 `artifacts/e2e_demo_results.json`，LaTeX 表格已写入 `artifacts/e2e_demo_table.tex`。

---
