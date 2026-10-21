# ssh matrix result audit

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_matrix_result_audit_20260522T010700_result.json`
- **Structured JSON:** [`9e2b2fd9299d679e3e22.json`](../../sessions/9e/9e2b2fd9299d679e3e22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

审计完成。报告已写入 `artifacts/_project/report/matrix_result_audit_20260522.md`。

核心发现：

**24 个 cell 中：4 个完整 (5/5)，13 个部分完成，7 个完全缺失。**

关键问题：

1. **RSA 系统性缺失** — 所有 TracVLA (8 cells) 和所有 NORA (4 cells) 均无 `rsa_analysis.json`，共 12 个 cell 受影响
2. **整 cell 缺失** — OpenVLA Spatial (T+U)、NORA Object (T+U)、NORA Long (T+U) 共 7 个 cell 为 0/5
3. **Registry 不一致** — `nora_spatial_pipeline_v2` 标记 success 但 untrained CF 文件实际缺失
4. **正在补跑** — `openvla_goal_standardized_v1` (RUNNING) 和 `openvla_spatial_standardized_v1` (PREPARING) 正在填补 OpenVLA Goal/Spatial 缺口；NORA Object/Long 尚无任何实验注册

---
