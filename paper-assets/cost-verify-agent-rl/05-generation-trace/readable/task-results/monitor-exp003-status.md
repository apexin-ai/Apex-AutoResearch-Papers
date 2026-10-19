# monitor exp003 status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp003_status_20260513T234828_result.json`
- **Structured JSON:** [`5f8c5529100ef7815071.json`](../../sessions/5f/5f8c5529100ef7815071.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp003 状态汇总

**进程存活** — PID 157852 运行 2h09m，双卡 GPU 97% 利用率。

**进度**: Step 1/100 完成（~96 分钟/步，预计剩余 ~6.6 天）。

**Step 1 核心指标**:
- success: 0.78%，pass@8: 6.25%
- **manager_invalid_action: 95.3%** — 模型几乎无法生成合法动作
- 每 episode 仅 2.14 个动作，大部分 trajectory 因无效动作早期终止
- raw_reward / episodic_return: 0.0

**Checkpoint**: 无（目录不存在）
**W&B**: 日志中无 run URL

训练初期 95% invalid action 率在预期内（base Qwen3-1.7B 未见过 ALFWorld），但需持续监控后续 step 该指标是否下降。报告已写入 `artifacts/exp003_status_check.md`。

---
