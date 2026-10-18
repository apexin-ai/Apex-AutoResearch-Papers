# code update gate d025

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_update-gate-d025_20260516T015120_result.json`
- **Structured JSON:** [`7b18fb71f739807742f9.json`](../../sessions/7b/7b18fb71f739807742f9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行正常。输出符合预期：

- **G3-deploy** 显示 N/A（未提供 `--acis-prune`），FAIL
- **G3-standard** 降为 `[REF]` 参考指标，不影响判定
- **overall** = G1 AND G2 AND **G3-deploy** AND G4
- 报告标题已更新为 `D025 GATE EVALUATION REPORT`

改动总结：
- 新增 `--acis-prune` 参数，接收 ACIS+Prune(50%) eval JSON
- `G3_deploy_ratio`（ACIS+Prune/baseline ≤ 1.10）为主 gate，决定 pass/fail
- `G3_standard_ratio` 和 `G3a_bypass_ratio` 标记为 `reference`，仅展示不参与 overall 判定
- `overall_pass = G1 AND G2 AND G3-deploy AND G4`

---
