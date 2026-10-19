# check exp028c step6 9

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028c_step6_9_20260516T030451_result.json`
- **Structured JSON:** [`148198a36d4298a1f140.json`](../../sessions/14/148198a36d4298a1f140.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已保存。核心发现：

**进度纠正**: 实际仅完成 step 5，step 6 in progress（非预估的 step 8-9）。Pace ~51min/step，step 10 val 预计 ~4h 后。

**关键趋势 (steps 1→5)**:
- **action_is_valid**: 持续上升 0.764→0.896 (train), 0.745→0.965 (val) — 最明确的正向信号
- **success**: 波动无趋势，val 维持 6.25% 不变
- **kl_loss**: step 5 飙升到 0.824（step 4 仅 0.031，26 倍增长）— 最大风险信号，需关注后续是否继续恶化
- **ppo_kl/pg_loss/grad_norm**: 正常，趋于稳定

---
