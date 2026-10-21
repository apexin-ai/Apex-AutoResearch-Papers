# analysis obs only seed43 final

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_obs-only-seed43-final_20260516T004539_result.json`
- **Structured JSON:** [`107601da6afcf78a6cd3.json`](../../sessions/10/107601da6afcf78a6cd3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整结果如下：

## eval-obs-only-object-seed43 最终结果

**overall_success_rate = 12% (12/100)**

### Per-task SR

| Task | Successes | SR |
|------|-----------|-----|
| alphabet_soup | 0/10 | 0% |
| cream_cheese | 1/10 | 10% |
| salad_dressing | 1/10 | 10% |
| bbq_sauce | 3/10 | 30% |
| ketchup | 0/10 | 0% |
| tomato_sauce | 0/10 | 0% |
| butter | 0/10 | 0% |
| milk | 1/10 | 10% |
| chocolate_pudding | 4/10 | 40% |
| orange_juice | 2/10 | 20% |

### 状态
- **进程 356490**: 已结束（DEAD）
- **cuda:2**: 空闲，无进程占用
- 评估正常完成，EXIT_CODE=0

### 关键分析

obs_only seed=43 SR = **12%**，低于你担心的 14% 阈值。

对比：
- obs_only seed=42 = 19%, seed=43 = 12% → pooled obs_only = **15.5% (31/200)**
- argmin seed=43 = 17% → 如果 argmin seed=42 也在 17% 附近，pooled argmin ~17%

obs_only pooled (15.5%) 反而**低于** argmin baseline，方向反了。这对项目来说是坏消息——Fisher exact test 不仅 p > 0.05，而且 obs_only 的 effect 方向都不对。

---
