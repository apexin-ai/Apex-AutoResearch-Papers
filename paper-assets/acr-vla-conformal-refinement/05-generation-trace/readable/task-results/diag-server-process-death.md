# diag server process death

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_server-process-death_20260520T193147_result.json`
- **Structured JSON:** [`bed980f11a41feb4a57e.json`](../../sessions/be/bed980f11a41feb4a57e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### bjb1-32546（2 个实验）

| 实验 | 状态 | SR | 死因 | 需重跑 |
|------|------|-----|------|--------|
| **eval-perdof-object-norm02-seed50** | ✅ 正常完成 | 10.0% (10/100) | 无——正常退出 | 否 |
| **eval-obs-only-object-norm02-seed51** | ✅ 正常完成 | 17.0% (17/100) | 无——正常退出 | 否 |

- PID 542405 和 542894 均已退出，所有 6 GPU 空闲 (0%)
- Output JSON 均已写入（03:20、03:22）
- **根因**：又是 cron false positive——进程正常完成但不写 sentinel/W&B，cron 检测到 "process gone" 即误判 failed

### bjb1-18228（2 个实验）

| 实验 | 状态 | SR | 死因 | 需重跑 |
|------|------|-----|------|--------|
| **eval-obs-only-object-norm005-seed44** | ✅ 正常完成 | 12.0% (12/100) | 无——正常退出 | 否 |
| **eval-obs-only-object-norm01-seed48** | 🔄 仍在运行 | — | — | 否，等完成 |

- norm005-seed44 被标记 failed 但实际完成，JSON 已存在
- norm01-seed48 PID 507385 活着（Rl+, 运行 55m55s），GPU1 占 3408MiB/29%，已完成 5/10 tasks，预计约 1h 完成

### 结论

**4 个实验中 0 个真正失败**。3 个已正常完成（需手动修正 conclusion=success 并补录 metrics），1 个仍在运行。全部是 cron false positive 的已知模式。

---
