# analysis plan002 metrics

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan002-metrics_20260514T032528_result.json`
- **Structured JSON:** [`6c0156f384f72c24728e.json`](../../sessions/6c/6c0156f384f72c24728e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总：

**plan002-additive-b03-s42** — conclusion: **success**

| 指标 | 值 |
|------|-----|
| total_steps | 500 |
| duration | 56.7 min |
| overall_prove_rate | 0.340 |
| last100_prove_rate | **0.553** |
| overall_isr (binary) | 0.115 |
| final_isr_mean | 0.309 |
| parse_rate | 1.0 |
| mean_loss / last100_loss | 0.0089 / 0.0145 |

**prove_rate 窗口轨迹：**
w1-50: 0.130 → w51-100: 0.095 → w101-200: 0.185 → w201-300: 0.375 → w301-400: 0.476 → w401-500: **0.553**

**vs plan001/plan013 饱和对比：** 仅 52/500 步 ≥0.85（plan001/plan013 通常 >300 步饱和）。additive bonus 模式下 prove_rate 仍在稳步上升，未出现强饱和，说明 ISR bonus 引入的额外 reward 信号可能减缓了 GRPO 过早收敛。需 eval_sta.py 评估真实 ISR 后才可做跨 run 对比。

---
