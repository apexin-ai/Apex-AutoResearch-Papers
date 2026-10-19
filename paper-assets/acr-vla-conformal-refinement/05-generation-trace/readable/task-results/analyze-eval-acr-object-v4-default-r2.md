# analyze eval acr object v4 default r2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval-acr-object-v4-default-r2_20260516T085851_result.json`
- **Structured JSON:** [`a014c567fce81f7b935c.json`](../../sessions/a0/a014c567fce81f7b935c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 不存在（可能已被清理或从未创建）。

**诊断完成：**

| 项目 | 结果 |
|------|------|
| **实际 mode** | `crm_perdof`（非 crm_default） |
| **norm** | default ~1.42（无 `--max_correction_norm`） |
| **seed** | 42 |
| **完整性** | 10/10 tasks, 100 rollouts |
| **overall SR** | **0.0%** (0/100) — 所有 task 全部 0 |
| **anomaly** | 已解决：exp_id 叫 "v4-default" 实际是 perdof default norm 消融实验 |
| **结论** | success — 假设验证通过：perdof 在无 magnitude control 时完全崩溃 |

Registry 已更新为 DONE/success，metrics 中备注了实际配置。bjb1-18228:cuda:0 已释放。

---
