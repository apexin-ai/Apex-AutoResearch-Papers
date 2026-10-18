# harvest eval pi05 l2norm k03 goal seed42

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_l2norm_k03_goal_seed42_20260523T223606_result.json`
- **Structured JSON:** [`6253c056910d4d321fad.json`](../../sessions/62/6253c056910d4d321fad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

没有活跃的 cron job，可能已在之前的 session 中删除或过期。

---

## 结果报告

**实验**: eval_pi05_l2norm_k03_goal_seed42
**状态**: DONE (negative)

| 指标 | 值 |
|------|-----|
| Overall SR | **54.2%** (271/500) |
| v2 run SR | 50.6% (253/500) |
| Random k=0.3 Goal | 51.8% (259/500) |
| **L2norm vs Random delta** | **+2.4pp (negligible)** |

**Per-task SR**: turn on stove 96% | wine bottle on cabinet 82% | bowl on plate 72% | open drawer 70% | bowl on cabinet 60% | plate to stove 48% | drawer+bowl 40% | wine bottle on rack 28% | cream cheese in bowl 26% | bowl on stove 20%

**Conclusion**: Negative — 极端剪枝 (k=0.3) 下 L2norm 与 Random 几乎无差异 (+2.4pp)，importance margin 在高压缩率下消失。

**Log**: `logs/eval_pi05_l2norm_k03_goal_seed42.log`
**Results JSON**: `eval_results/pi05_l2norm_k0.30_libero_goal_seed42.json`

---

GPU 2 已空闲，可部署 eval_pi05_random_k07_object_seed42_v2。

---
