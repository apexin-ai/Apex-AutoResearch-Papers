# analyze eval pi05 l2norm k09 long seed43 postfix

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_pi05_l2norm_k09_long_seed43_postfix_20260525T124256_result.json`
- **Structured JSON:** [`4ca5c9626a76f6527895.json`](../../sessions/4c/4ca5c9626a76f6527895.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。分析结果如下：

## 实验结果：`eval_pi05_l2norm_k09_long_seed43_postfix`

**状态：成功完成** — 之前标记的 failure 是启动阶段的环境变量问题，但进程后来正常跑完了。

**Overall SR = 80.8%** (404/500)，耗时 194 分钟。

### Per-task breakdown

| Task | Description | SR | n |
|------|------------|-----|---|
| T0 | alphabet soup + tomato → basket | **92%** | 46/50 |
| T1 | cream cheese + butter → basket | **96%** | 48/50 |
| T2 | stove on + moka pot | **92%** | 46/50 |
| T3 | black bowl → drawer | **100%** | 50/50 |
| T4 | white mug left plate + yellow mug right plate | **88%** | 44/50 |
| T5 | book → caddy | **96%** | 48/50 |
| T6 | mug on plate + pudding beside | **14%** | 7/50 |
| T7 | soup + cream cheese → basket | **82%** | 41/50 |
| T8 | two moka pots → stove | **58%** | 29/50 |
| T9 | mug → microwave | **90%** | 45/50 |

### 与 v2 (SR=80%) 对比

seed43 的 **80.8%** 与 v2 的 **80%** 高度一致（Δ=+0.8pp），dual-seed 结果互相印证，支持 cliff zone immunity claim 的统计可信度。T6 仍是明显弱项（14%），T8 次之（58%），其余 task 均 ≥82%。

---
