# analyze goal adapt tau025 s42 urgent

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_goal-adapt-tau025-s42-urgent_20260523T085416_result.json`
- **Structured JSON:** [`7c3b82efa37e3ad238b6.json`](../../sessions/7c/7c3b82efa37e3ad238b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/negative。结果汇总：

## eval-supp-goal-adapt-tau025-s42 结果

| 指标 | 值 |
|------|-----|
| **Overall SR** | **84.0%** (168/200) |
| trigger_rate | 8.25% (2334/28283 steps) |
| mean_uncertainty | 0.1448 |

**对比：**

| 配置 | Goal SR |
|------|---------|
| VLA-only baseline | ~97.5-98% |
| CRM always-on norm=0.05 | 85.5% |
| **Adaptive tau=0.25** | **84.0%** |

### 结论：**Negative**

Adaptive 机制在 Goal suite 上失败。尽管 trigger_rate 仅 8.25%（极少触发 correction），SR 仍从 ~98% 暴跌至 84%，甚至比 always-on CRM 的 85.5% 还略差。

这说明问题不在于 correction 频率，而在于 correction 质量——即使少量的错误 correction（在关键时刻施加）也足以破坏整条轨迹。Goal 任务本身 VLA 已经接近饱和，CRM 的 correction 信号在这里是纯噪声。

### 退化最严重的任务
- put_the_cream_cheese_in_the_bowl: 60%（baseline ~98%，跌了 38pp）
- open_the_top_drawer_and_put_the_bowl_inside: 70%

### GPU 状态
**cuda:2 已空闲**（0% utilization, 1 MiB），可部署新实验。

---
