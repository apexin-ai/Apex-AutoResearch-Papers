# check bootstrap v2 final condition

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_bootstrap_v2_final_condition_20260523T062741_result.json`
- **Structured JSON:** [`47fee195595fcd37ba16.json`](../../sessions/47/47fee195595fcd37ba16.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**tracvla_long/untrained — 未完成，正在运行中**

- PID 723018，100% CPU，正在处理第 2/10 个 task（1200/5000 samples）
- 每个 task 5000 samples，共 10 个 task，当前约完成 24%
- 按进度估算，每 50 samples ~17 秒 → 剩余约 38000 samples → 约 **2 小时**完成

**完成进度：19/20**

已完成的 19 个 JSON：

| arch | suite | trained | untrained |
|------|-------|---------|-----------|
| openvla | goal | ✅ | ✅ |
| openvla | spatial | ✅ | ✅ |
| openvla | object | ✅ | ✅ |
| openvla | long | ✅ | ✅ |
| tracvla | goal | ✅ | ✅ |
| tracvla | spatial | ✅ | ✅ |
| tracvla | object | ✅ | ✅ |
| tracvla | long | ✅ | ❌ (运行中) |
| nora | goal | ✅ | ✅ |
| nora | spatial | ✅ | ✅ |

注意：输出目录是 `bootstrap_r2`（非 `bootstrap_v2`），JSON 文件名为 `{trained,untrained}.json`（非 `bootstrap_r2_results.json`）。

---
