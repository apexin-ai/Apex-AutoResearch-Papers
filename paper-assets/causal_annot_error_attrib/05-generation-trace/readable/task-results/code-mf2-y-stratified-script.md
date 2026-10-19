# code mf2 y stratified script

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_mf2_y_stratified_script_20260523T160631_result.json`
- **Structured JSON:** [`c10fcbaa3f290c6dd0d8.json`](../../sessions/c1/c10fcbaa3f290c6dd0d8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本已完成并注册。

**要点**:
- `artifacts/nondiff_y_stratified.py` — 语法验证通过，只依赖 numpy + requests + stdlib
- Phase 1: OpenRouter API 标注 VAST 1000 条数据，支持 `--smoke`、resume、429 退避、402 立即退出
- Phase 2: 3 个 Y proxy（text_length / topic / sentiment）的 column-stochastic confusion matrix 分层 + permutation test（默认 10,000 次）
- 拿到 API key 后 `--phase all --api-key &lt;KEY>` 一步到位

---
