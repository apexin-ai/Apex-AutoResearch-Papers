# analysis cos sim trajectory extract

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cos_sim_trajectory_extract_20260520T021655_result.json`
- **Structured JSON:** [`0486e79091ff6a02e7eb.json`](../../sessions/04/0486e79091ff6a02e7eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。提取结果：

**v9 PCGrad** (`artifacts/cos_sim_trajectory/v9_pcgrad_cos_sim.json`):
- 60 个数据点，step 50→3000，每 50 步一个
- cos_sim 在 [-0.15, +0.09] 之间振荡，无收敛趋势
- mag_ratio 从 ~2.8 增长到 ~28.8
- conflict_layers 稳定在 39-57%

**v7 TG** (`artifacts/cos_sim_trajectory/v7_cos_sim.json`):
- 3 个 epoch 级数据点（来自服务器上 `runs/analysis/gradient_conflict/epoch_{0,1,2}.json` 的完整离线分析结果）
- cos_sim: -0.089 → -0.054 → -0.042（持续负值但缓慢收敛）
- mag_ratio median: 7.5 → 13.7 → 14.7
- neg_layers: 78.6% → 71.4% → 67.9%

数据来源：v9 训练日志 `~/runs/turn_residual_gating/phase2_tg_s42_v9_pcgrad.log`（通过 cron hook 捕获），v7 为 `gradient_conflict_analysis.py` 的离线分析 JSON。

---
