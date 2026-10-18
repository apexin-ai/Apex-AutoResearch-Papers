# code bt model diagnostics

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_bt_model_diagnostics_20260521T114335_result.json`
- **Structured JSON:** [`fd8d40104f753607384d.json`](../../sessions/fd/fd8d40104f753607384d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果摘要：

**GoF Deviance Test** — 两个维度 BT 模型均 adequate：
- Formality: D=52.80, df=45, **p=0.198** (n=46 consistent pairs, BT prob=0.739)
- Verbosity: D=47.96, df=62, **p=0.905** (n=63 consistent pairs, BT prob=0.873)

**Stratified BT Stability:**
- **Formality: 显著方向差异**
  - orig_is_formal: 88.9% [77.8%, 100%], 24/27
  - orig_is_casual: 52.6% [31.6%, 73.7%], 10/19
  - Fisher p=0.015, chi2 p=0.006
- **Verbosity: 无显著方向差异**
  - orig_is_verbose: 82.8% [69.0%, 96.6%], 24/29
  - orig_is_concise: 91.2% [79.4%, 100%], 31/34
  - Fisher p=0.453, chi2 p=0.317

Formality 的分层差异 (Fisher p=0.015) 提示原始文本为 formal 时 judge 更倾向选择 formal，originality preference confound 显著。Verbosity 无此问题。

---
