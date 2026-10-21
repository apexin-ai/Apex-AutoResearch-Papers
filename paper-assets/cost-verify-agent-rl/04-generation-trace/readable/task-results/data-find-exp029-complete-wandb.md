# data find exp029 complete wandb

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_find-exp029-complete-wandb_20260518T205030_result.json`
- **Structured JSON:** [`5f4c4de7fd1673b25123.json`](../../sessions/5f/5f4c4de7fd1673b25123.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果：**
- **正确的 W&B run ID**: `7a59sudo`
- **URL**: https://wandb.ai/xiaoyucorynne-/cost-verify-agent-rl/runs/7a59sudo
- **数据**: 16 行，steps 0-15，完整 15 步训练数据
- **之前的 run 6d4oml60**: 仅 1 行（step 0 的 val 数据），确认是崩溃前的 run

**Val success 趋势**: 0.125 (step 0) → 0.25 (step 5) → 0.25 (step 10) → 0.28125 (step 15)

**Train success 趋势**: 从 ~0.10-0.18 逐步上升到 step 14-15 的 0.4375

exp029 在 bjb1 上经历了 5 次 W&B runs（aofjc8id → 6d4oml60 → j52mfcnt → ugkd8ys1 → 7a59sudo），前 4 次均在 step 0 崩溃，第 5 次（7a59sudo，04:13 启动）完成了全部 15 步训练。

数据已保存到 `artifacts/exp029/data/wandb_data_7a59sudo.json`。

---
