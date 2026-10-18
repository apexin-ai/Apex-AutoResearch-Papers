# analysis gpt4o aeval gee artifact

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gpt4o-aeval-gee-artifact_20260523T031251_result.json`
- **Structured JSON:** [`280e3eeacdad3bd051e5.json`](../../sessions/28/280e3eeacdad3bd051e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

复现完成，结果与 registry 完全一致。

**AlpacaEval × formality (GPT-4o)**:
- BT: P(formal)=0.727 [0.663, 0.785], p<0.001 — **Blindspot=YES**（BT显著但Likert不显著）
- Likert: ATE=0.012, d=0.005, Wilcoxon p=0.909, tie=66.3%
- GEE: Style OR=4.91 [2.59, 9.31] p=1.1e-6, Orig OR=1.99 [1.05, 3.77] p=0.036, VIF=1.51

**MT-Bench × formality (GPT-4o)**:
- BT: P(formal)=0.692 [0.623, 0.760], p<0.001
- Likert: ATE=0.192, d=0.135, Wilcoxon p=0.007
- GEE: Style OR=2.28 [0.84, 6.20] p=0.106 (n.s.), Orig OR=6.24 [2.22, 17.51] p=5.1e-4, VIF=1.95

**AlpacaEval × verbosity**: 数据不可用（所有 100 条记录的 trial1_choice/trial2_choice 均为 null，pairwise 评分未完成）。

Artifact 已保存到本地和远程 `artifacts/r14_fixes/gpt4o_crossbench_results.json`。

---
