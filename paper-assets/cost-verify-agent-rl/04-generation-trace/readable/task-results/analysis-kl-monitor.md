# analysis kl monitor

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_kl-monitor_20260515T172024_result.json`
- **Structured JSON:** [`a4e226a29399e1c154b1.json`](../../sessions/a4/a4e226a29399e1c154b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/exp027_kl_analysis.md`。

**结论**：训练进程健康，双 GPU 100% 满载，但尚未完成 step 1——KL 指标还没有。

关键数据：
- **Step 0 val**: success = 6.25% (16 episodes), reward_mean = 0.3226
- **当前阶段**: step 1 policy update 正在计算（compute_policy_loss 已触发，~47min 无新日志输出但 GPU 满载）
- **W&B**: 确认 entity=`xiaoyucorynne-`，project=`cost-verify-agent-rl`，目前 0 条历史数据

KL 监控需等 step 1 完成后才有数据。根据当前 GPU 负载和已耗时间，预计 **30-60 分钟后** step 1 完成，届时可再次检查获取首批 KL/entropy/reward 指标。

---
