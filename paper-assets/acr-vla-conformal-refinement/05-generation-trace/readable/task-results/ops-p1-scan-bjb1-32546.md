# ops p1 scan bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_p1-scan-bjb1-32546_20260515T111526_result.json`
- **Structured JSON:** [`02637155b043da0c80c6.json`](../../sessions/02/02637155b043da0c80c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## bjb1-32546 Object Eval 全量进度

### GPU 状态
全 6 卡均在用（~20% utilization, ~2.8-3.8 GB VRAM），6 个 eval 进程正常运行。

### 实验进度

| # | 实验 | GPU | Mode | 完成 | 最新完成 Task + SR | 状态 |
|---|------|-----|------|------|-------------------|------|
| 1 | reconvla | cuda:0 | reconvla | **6/10** | T5 tomato_sauce 0% | 运行中，正跑 T6 |
| 2 | perdof (norm=0.1) | cuda:1 | crm_perdof | **6/10** | T5 tomato_sauce 0%, T6 butter 进行中 (5/10) | 运行中 |
| 3 | obs_only (norm=0.1) | cuda:2 | crm_obs_only | **6/10** | T5 tomato_sauce 0% | 运行中，正跑 T6 |
| 4 | scalar (norm=0.1) | cuda:3 | crm_scalar | **6/10** | T5 tomato_sauce 0% | 运行中，正跑 T6 |
| 5 | obs_only norm=0.2 | cuda:4 | crm_obs_only | **4/10** | T3 bbq_sauce 40%, T4 ketchup 进行中 (5/10) | 运行中 |
| 6 | vla_mean | cuda:5 | vla_only mean | **6/10** | T5 tomato_sauce 10% | 运行中，正跑 T6 |

### 各实验已完成 Tasks 的 SR

| Task | reconvla | perdof | obs_only 0.1 | scalar | obs_only 0.2 | vla_mean |
|------|----------|--------|-------------|--------|-------------|----------|
| T0 alphabet_soup | 0% | 0% | 0% | 0% | 0% | 0% |
| T1 cream_cheese | 0% | 0% | 10% | 0% | 0% | 0% |
| T2 salad_dressing | 10% | 20% | 20% | 10% | 30% | 10% |
| T3 bbq_sauce | 30% | 30% | 40% | 10% | 40% | 30% |
| T4 ketchup | 0% | 0% | 10% | 0% | 进行中 | 10% |
| T5 tomato_sauce | 0% | 0% | 0% | 0% | — | 10% |

### 重点关注：obs_only (cuda:2)
**已过 T5。** 当前 6/10 完成，正在跑 T6。目前 running SR = (0+10+20+40+10+0)/6 = **13.3%**。

### 异常标记
- **eval-acr-object-v4-default** 和 **eval-vla-only-object-k1** 有日志但无运行进程（前者停在 T3，后者停在 T0）— 疑似早期被终止的实验。
- obs_only norm=0.2 (GPU 4) 比其他实验慢约 2 个 task，因为启动时间晚 ~2.5h（13:21 vs 10:37-11:00）。
- 全部 6 个实验预计还需 ~3-4h 完成剩余 tasks。

---
