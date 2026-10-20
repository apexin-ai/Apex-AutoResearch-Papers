# analysis codellama13b loop only seed456

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_codellama13b_loop_only_seed456_20260520T125520_result.json`
- **Structured JSON:** [`ced8197f6dfcc3b93356.json`](../../sessions/ce/ced8197f6dfcc3b93356.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

**seed456 结果**：accuracy=79.08%，fail_f1=0.688，lift=+7.6pp，在预期范围内。

**3-seed 汇总 (CodeLlama-13B loop_only)**：**77.40±1.54%**
- seed42=77.06%, seed123=76.05%, seed456=79.08%
- Fail F1 跨 seed 极稳定：0.680±0.009

**跨模型排序**：Qwen-7B (86.05%) > DeepSeek-6.7B (81.26%) > Qwen-1.5B (78.32%) > CodeLlama-13B (77.40%) — 确认 CodeLlama-13B 是 loop_only 条件下最弱模型，参数量 13B 未带来优势。

Registry 已更新（hypothesis + parent），报告已注册（`art_20260520_d70ad7`）。

---
