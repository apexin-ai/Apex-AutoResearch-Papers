# analysis action divergence v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_action_divergence_v2_20260517T124712_result.json`
- **Structured JSON:** [`476b17f486a59c59c5a8.json`](../../sessions/47/476b17f486a59c59c5a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全量实验完成。结果摘要：

---

## Closed-Loop Action Divergence 结果

**配置**: 3 tasks × 10 episodes, 300 max steps, ACIS k=0.5 true_removal

### 核心数据

| 指标 | 值 |
|------|------|
| Action L2 (mean) | **1.117** |
| Action L2 (median) | 0.850 |
| EEF Position L2 (mean) | **0.214m** (21.4cm) |
| EEF Position L2 (median) | 0.214m |

### Divergence 时序特征

- **Onset**: step 0（立即偏离，eef_l2 > 1cm 从第 0 步开始）
- **First 10 steps**: action_L2=1.262, eef_L2=**0.041m** (4.1cm)
- **Last 10 steps**: action_L2=0.759, eef_L2=**0.198m** (19.8cm)
- **Pattern**: EEF divergence 持续增长（4cm → 20cm），轨迹快速且不可逆地分叉

### 额外发现

- Bypass 模型多次成功完成任务（提前终止，如 121-168 steps），pruned 模型**从未提前终止**（全部跑满 300 steps），强烈暗示 pruned 模型完全无法完成任务
- 三个 task 间结果一致（action_L2: 1.08-1.17, eef_L2: 0.19-0.25m），说明 pruning 导致的 divergence 是系统性的

### 对论文的意义

这确认了 "catastrophic divergence" 的 narrative：
1. 单步 action error 很大（L2=1.12, 与 offline 分析的 1.284 一致）
2. 在 closed-loop 下 error 不会自我修正，反而通过 state divergence 放大
3. Pruned 模型的行为彻底崩溃（0% implicit success vs bypass 的多次成功）

脚本路径: `/root/autodl-tmp/importance_margin_vla_compress/closedloop_action_divergence.py`
结果路径: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/action_divergence_closedloop.json`

---
