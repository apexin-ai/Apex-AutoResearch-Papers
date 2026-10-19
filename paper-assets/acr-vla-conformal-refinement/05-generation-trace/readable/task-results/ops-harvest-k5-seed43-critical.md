# ops harvest k5 seed43 critical

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-k5-seed43-critical_20260518T123828_result.json`
- **Structured JSON:** [`fcc8334965d136d5b4bc.json`](../../sessions/fc/fcc8334965d136d5b4bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。汇总如下：

---

## 1. K=5 seed43 结果 — Overall SR = **19%**

| Task | SR |
|---|---|
| chocolate_pudding | 50% |
| bbq_sauce | 30% |
| orange_juice | 30% |
| salad_dressing | 20% |
| tomato_sauce | 20% |
| cream_cheese | 10% |
| ketchup | 10% |
| butter | 10% |
| milk | 10% |
| alphabet_soup | 0% |

**K-value curve 更新（obs_only, norm=0.2）：**
| K | seed42 | seed43 | mean |
|---|---|---|---|
| 1 | 10.3% | — | 10.3% |
| 5 | 14% | **19%** | **16.5%** |
| 10 | 17.5% | — | 17.5% |

seed43 比 seed42 高 5 个百分点，K=5 数据点看起来稳健，均值 16.5% 位于 K=1 和 K=10 之间，单调递增趋势成立。

## 2. 两个"失败"实验 — **cron 误判，实际仍在运行**

- **PID 497445** (cuda:1): `crm_obs_only, K=10, norm=0.1, seed42` — CPU 159%，仍在跑
- **PID 497642** (cuda:3): `crm_perdof, K=10, norm=0.1, seed42` — CPU 161%，仍在跑

日志文件不存在于 `/root/runs/` 下以 `-r2` 命名的路径，因为它们实际是原始运行（非 r2 重跑）。registry 标记为 FAILED 是 cron 误判，建议将这两个 registry 状态改回 RUNNING。

## 3. GPU 状态 (bjb2-28827)

| GPU | Util | Memory | Status |
|---|---|---|---|
| cuda:0 | 18% | 2.3G/24.6G | 占用 |
| cuda:1 | 18% | 1.9G/24.6G | PID 497445 占用 |
| **cuda:2** | **0%** | **1M/24.6G** | **已释放** ✓ |
| cuda:3 | 18% | 1.9G/24.6G | PID 497642 占用 |
| cuda:4 | 18% | 2.8G/24.6G | 占用 |
| cuda:5 | 19% | 1.9G/24.6G | 占用 |

cuda:2 已空闲，cuda:1 和 cuda:3 仍被上述两个实验占用。

---
