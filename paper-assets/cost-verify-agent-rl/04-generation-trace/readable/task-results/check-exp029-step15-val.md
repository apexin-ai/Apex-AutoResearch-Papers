# check exp029 step15 val

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_step15_val_20260517T040439_result.json`
- **Structured JSON:** [`b4dad3aa9c7ddb827703.json`](../../sessions/b4/b4dad3aa9c7ddb827703.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正在运行，日志仍在活跃写入（12:06:34 最后修改）。Step 15 val 的 collapse/metrics 计算正在进行中，结果即将输出。

## exp029 状态总结

**当前 step**: 15/100（进度 15%，7h21m 已运行）

**Step 15 val**: 生成已完成（802 秒），metrics 正在计算中（collapse 阶段，~12:04 开始），预计几分钟内输出最终结果。

**已有 val 结果对比（16 episodes）**:

| Metric | Step 0 (init) | Step 5 | Step 10 |
|--------|:---:|:---:|:---:|
| **success_rate** | 12.5% | **25%** | **25%** |
| action_is_valid | 0.783 | 0.704 | 0.602 |
| action_is_effective | 1.0 | 1.0 | 0.999 |
| pass@1 | 12.5% | 25% | 25% |
| best@8 reward mean | 6.44 | 8.97 | 8.85 |
| best@32 reward mean | 9.84 | 9.99 | 9.99 |

**最新 train metrics (step 14)**:
- train success: 43.75%, entropy: 0.027, kl_loss: 0.070, ppo_kl: 0.006

**趋势分析**:
- Val success 从 step 0 (12.5%) 跳到 step 5 (25%)，然后 step 10 持平 (25%)
- action_is_valid 持续下降：0.783 → 0.704 → 0.602（模型探索更多动作但 valid 率降低）
- Train success 在 step 14 达到 43.75%，但 val 是否跟进需要等 step 15 结果
- KL 和 entropy 在合理范围，训练稳定

**ETA**: Step 15 val metrics 应在 ~2-5 分钟内出现在日志中。需要我稍后再查一次最终数值吗？

---
