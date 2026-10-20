# debug counterfactual check result

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_counterfactual_check_result_20260518T172122_result.json`
- **Structured JSON:** [`556e77a4593e4e4e4289.json`](../../sessions/55/556e77a4593e4e4e4289.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Cron 已不存在，无需删除。

---

## 实验结果报告：counterfactual_instruction

**状态**: DONE (success) | **模型**: openvla-7b | **样本数**: 1500 (3 tasks × 10 demos × 50 timesteps)

### 各条件指标（按 Cohen's d 降序）

| Condition | Cohen's d | Paired MSE | Token Divergence | KL Divergence |
|-----------|-----------|------------|------------------|---------------|
| **empty** | **0.968** | 0.0685 | 0.907 | 8.888 |
| **wrong** | **0.844** | 0.0585 | 0.895 | 8.326 |
| **paraphrased** | **0.697** | 0.0456 | 0.826 | 6.928 |
| **shuffled** | **0.625** | 0.0391 | 0.857 | 7.732 |

### 关键发现

- 所有 4 个条件效应量均为 large (d > 0.5)，说明 OpenVLA 确实对指令内容敏感
- **empty > wrong > paraphrased > shuffled** 的 Cohen's d 排序表明：完全移除指令的影响最大，替换为错误任务次之
- paraphrased 条件 d=0.697 值得注意：语义等价的改写仍产生中等偏大的行为偏移，说明模型对表面形式也有依赖
- shuffled 效应最小 (d=0.625)，但 token divergence (0.857) 高于 paraphrased (0.826)，说明打乱词序主要影响 token 层面而非整体行为幅度

Registry 已更新为 DONE/success，cron 已清除。

---
