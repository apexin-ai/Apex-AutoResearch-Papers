# analyze westd vla only batch and adaptive

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_westd-vla-only-batch-and-adaptive_20260526T115459_result.json`
- **Structured JSON:** [`8000a451573797971962.json`](../../sessions/80/8000a451573797971962.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

7 个实验全部完成分析，registry 已更新。汇总：

## 结果汇总

| exp_id | benchmark | seed | success_rate | 备注 |
|--------|-----------|------|-------------|------|
| westd-pi05-vla-only-goal-s42-paired | goal | 42 | **97.5%** | 最低 task: open_drawer/push_plate/wine_rack 95% |
| westd-pi05-vla-only-goal-s43-paired | goal | 43 | **96.5%** | 最低 task: open_top_drawer 85% |
| westd-pi05-vla-only-goal-s44-paired | goal | 44 | **95.5%** | 最低 task: open_top_drawer 80% |
| westd-pi05-vla-only-object-s42-paired | object | 42 | **99.5%** | 仅 bbq_sauce 95% |
| westd-pi05-vla-only-object-s43-paired | object | 43 | **100%** | 10/10 tasks 全部满分 |
| westd-pi05-vla-only-object-s44-paired | object | 44 | **99.5%** | 仅 bbq_sauce 95% |
| pi05-adaptive-object-s42-cqa1 | object | 42 | **85.5%** | trigger_rate=3.7%, mean_unc=0.084, 最低 ketchup 50% |

**VLA-only baseline 均值：**
- Goal (westd): 96.5% ± 1.0%
- Object (westd): 99.7% ± 0.3%

**Adaptive vs VLA-only (Object, s42)：** 85.5% vs 99.5%，Adaptive 反而下降 14pp。trigger_rate 仅 3.7% 说明 conformal 几乎不触发，但触发时 CRM correction 损害了性能（尤其 ketchup 从 100%→50%，cream_cheese 从 100%→70%）。

---
