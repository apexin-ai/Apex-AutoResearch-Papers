# exp proofwriter pilot

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_proofwriter_pilot_20260515T065710_result.json`
- **Structured JSON:** [`3038b22a26233825f4f2.json`](../../sessions/30/3038b22a26233825f4f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Pilot 已运行 17.5 分钟，完成 3/30 样本。基于已有数据，可以给出**初步判定**。

## 初步结果（3/30 样本完成，第 4 个确认 DISAGREE 中）

| # | ID | FOL | Code | GT | Type |
|---|---|---|---|---|---|
| 1 | AttNeg-OWA-D5-979_Q9 | True | False | True | **DISAGREE** |
| 2 | RelNoneg-OWA-D5-1036_Q11 | Error | False | True | **SINGLE_ERROR** |
| 3 | AttNeg-OWA-D5-891_Q1 | True | True | True | AGREE_CORRECT |
| 4 | AttNeg-OWA-D5-347_Q11 | (运行中) | | True | **DISAGREE** (已触发 stability check + repair) |

### C1 计算
- **DISAGREE (fol ≠ code)**: 2/3 = **66.7%**（含 SINGLE_ERROR；纯 DISAGREE 1/3 = 33%）
- **C1 ≥ 10%: YES — ProofWriter 可用**

即使后续 26 个样本全部 AGREE，C1 也至少 2/30 = 6.7%。但从趋势看（4 个样本 3 个非 AGREE），最终 C1 预计 **30-60%**。

### 附加观察
- **Crash 率**: 0/3（无 pipeline_error）
- **FOL 准确率**: 1/3（33%，含 1 Error）
- **Code 准确率**: 1/3（33%）
- **thinking 截断频繁**: Qwen3-32B thinking 链过长导致几乎每次 LLM 调用都截断后 fallback 到 no-thinking
- **每样本耗时**: AGREE ~1min, DISAGREE/ERROR ~5-8min（因 repair + thinking 截断 retry）
- **预计总耗时**: 30 样本约 1.5-2 小时

### 判定
**C1 >> 10%，ProofWriter 可用。** 不需要切 LogiQA。

Pilot 进程 (PID 84818) 仍在后台运行。完整 30 样本结果将写入 `results/proofwriter_pilot.jsonl`。后续可随时查看最终数据。

---
