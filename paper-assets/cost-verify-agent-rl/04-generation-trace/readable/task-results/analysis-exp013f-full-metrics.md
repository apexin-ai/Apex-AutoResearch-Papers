# analysis exp013f full metrics

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp013f-full-metrics_20260514T123434_result.json`
- **Structured JSON:** [`afe9b95cecaa8d64e657.json`](../../sessions/af/afe9b95cecaa8d64e657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已写入 `artifacts/exp013f_training_metrics.md`。

## 关键发现

**25 个 train step（6–30）+ 3 个 val 评估点（5/20/30）全部提取完成。**

### 趋势总结

**action_is_valid**：0.556 → 0.860（+54.7%），val 端 0.600 → 0.975。模型明确学会了合法动作格式。

**success**：全程 0–6.25%，后 9 步（22–30）基本为 0。Val success 始终 0%。

### Reward Gaming 定量证据

这是典型的 reward hacking：
- **score_mean +49%**（2.60→3.87），但 **success 无改善**
- 后期 **score_max 塌缩到 4.5**（不再有完成任务的 trajectory，前期有 10+）
- 模型学会产出格式合法的动作刷密集奖励，但放弃了高风险的任务探索
- Val reward mean@4 从 2.7→4.39，但 val success = 0%
- 后期 KL 从 0.001 飙至 0.009、grad_norm 尖峰 8.15，策略过度优化密集奖励

### 磁盘
`/root/autodl-tmp/`: 78% used (57G free)，exp013f checkpoints 占 62G。

---
