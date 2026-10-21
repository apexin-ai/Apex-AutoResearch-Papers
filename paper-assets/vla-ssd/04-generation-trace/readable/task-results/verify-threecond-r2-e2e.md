# verify threecond r2 e2e

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_threecond_r2_e2e_20260528T221321_result.json`
- **Structured JSON:** [`34c02cb55168c8477a3a.json`](../../sessions/34/34c02cb55168c8477a3a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证完成。

**结果**: Plot 脚本全部 192 个硬编码值与 `threecond_multiseed_v2.json`（3 seeds [42,123,456]，sequential split，denormalized R²）完全一致，零偏差。

**之前抽检偏移的原因**: 对比的是 15-seed 的 local artifact 文件，而非 3-seed 的 v2 JSON。两者是同一管线不同种子数的实验，sample mean 自然不同（trained MAD=0.0117, untrained MAD=0.1208）。不是数据错误。

报告已写入 `artifacts/verify_threecond_r2_report.md` 并注册。

---
