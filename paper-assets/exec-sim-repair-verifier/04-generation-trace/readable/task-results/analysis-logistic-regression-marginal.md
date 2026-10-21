# analysis logistic regression marginal

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_logistic-regression-marginal_20260522T170132_result.json`
- **Structured JSON:** [`a2dc0d53d36a6d39339d.json`](../../sessions/a2/a2dc0d53d36a6d39339d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。核心结论：

**Cross-complexity (DeepSeek, n=56,480, 139 clusters):**
- CWM function-level: OR=0.98, p=0.771, AME=−0.2pp (LPM: −0.2pp, p=0.805) — 一致
- CWM×repo interaction: OR=0.31, p=0.002, AME=−21.6pp (LPM: −21.9pp, p<0.001) — 一致

**Cross-model (repo, n=78,272, 25 clusters):**
- CWM deficit: OR=0.30, p=0.001, AME=−21.1pp (LPM: −22.0pp, p<0.001) — 一致
- Model effect/interaction: GEE下不显著 (p=0.449/0.860)，与LPM有分歧。原因是25个cluster下GEE sandwich SE更保守，论文已注意到这一点。

所有主效应 (primary effects) 的方向、量级和显著性在 LPM 和 logistic 之间一致。报告含一段可直接插入 Appendix M 的文字和 LaTeX 表格。

产出：
- 服务器：`/home/sonny/exec-sim-repair-verifier/artifacts/logistic_regression_results.json`
- 本地：`artifacts/logistic_regression_report.md`（已注册 artifact）

---
