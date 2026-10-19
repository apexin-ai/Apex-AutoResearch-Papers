# research adaptive kl assessment

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_adaptive_kl_assessment_20260515T184328_result.json`
- **Structured JSON:** [`920adc4da25feca2c285.json`](../../sessions/92/920adc4da25feca2c285.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

评估完成。核心结论：

**改动量极小 — 零代码修改，纯配置变更。** verl 框架已在 `core_algos.py` 内置了 `AdaptiveKLController`（Ziegler 2019），且 RAGEN 的 `agent_trainer.py` 已完整接入 reward-level KL 的 adaptive 链路。当前项目用的是 loss-level KL（`use_kl_loss` + 静态 `kl_loss_coef`），只需切换到已有的 reward-level KL 即可。

**具体改动**：实验 YAML 中改 ~8 行配置：
- 开启 `algorithm.use_kl_in_reward: True` + `kl_ctrl.type: adaptive`
- 关闭 `actor.use_kl_loss: False`
- 设 `target_kl: 0.1`, `kl_coef: 0.005`（初始值），`horizon: 10000`

**工时**：实现 <1h，验证实验 2-4h。总计 Worker 小时级。

**主要风险**：reward-level 和 loss-level KL 作用机制不同（前者通过 advantage 间接影响梯度）。如果 reward-level 效果不理想，备选方案 B（让 loss-level 也支持 adaptive）需 ~30 行代码改动，半天可完成。

---
