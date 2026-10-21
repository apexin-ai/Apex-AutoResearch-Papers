# audit westd 38929 harvest and pids

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd-38929-harvest-and-pids_20260524T013412_result.json`
- **Structured JSON:** [`0dd404e3876ae6a5e1ea.json`](../../sessions/0d/0dd404e3876ae6a5e1ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。另外发现 eval_xvla_random_k05_spatial_seed43 也已完成但不在 registry 中——这是个额外发现，暂不创建 registry 条目。

---

## eval_xvla_l2norm_k05_long_seed43
状态: **完成** (PID 432791 已退出)
SR: **43.8%** (219/500)
Wilson CI 95%: [39.5%, 48.2%]

| Task | SR | Detail |
|------|-----|--------|
| T0 | 26% | put both alphabet soup & tomato sauce in basket |
| T1 | 0% | put both cream cheese box & butter in basket |
| T2 | 52% | turn on stove & put moka pot on it |
| T3 | 78% | put black bowl in bottom drawer & close |
| T4 | 38% | put white mug on left plate & yellow mug on right |
| T5 | 86% | pick up book & place in caddy |
| T6 | 56% | put white mug on plate & chocolate pudding right |
| T7 | 76% | put both alphabet soup & cream cheese in basket |
| T8 | 24% | put both moka pots on stove |
| T9 | 2% | put yellow mug in microwave & close |

Registry → DONE (conclusion: success)

## 额外发现：eval_xvla_random_k05_spatial_seed43
状态: **完成** (tmux session 仍存在，进程已结束)
SR: **72.6%** (363/500), Wilson CI 95%: [68.5%, 76.3%]
结果: `eval_results/eval_xvla_random_k05_spatial_seed43.json`

## X-VLA Random k=0.85 Re-runs (均启动于 09:10, 运行 ~26 min)

| GPU | 实验 | PID | 已完成 Tasks | 当前进度 | 总进度 |
|-----|------|-----|-------------|---------|--------|
| 0 | Object seed42 | 674755 | T0=98%, T1=14%, T2=100%, T3=88% | T4 Ep 29/50 | ~229/500 (46%) |
| 1 | **空闲** | — | — | — | — |
| 2 | Goal seed42 | 674830 | T0=100%, T1=42%, T2=70%, T3=78% | T4 Ep 40/50 | ~240/500 (48%) |
| 3 | Spatial seed42 | 674970 | T0=100%, T1=6%, T2=98%, T3=98% | T4 Ep 11/50 | ~211/500 (42%) |

tmux sessions: `eval_xvla_random_k085_object_seed42`, `eval_xvla_random_k085_goal_seed42`, `eval_xvla_random_k085_spatial_seed42`

GPU 1 完全空闲（0% util, 1 MiB），可用于新实验。

---
