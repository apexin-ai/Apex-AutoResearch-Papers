# ops 025 midpoint check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_025-midpoint-check_20260519T193255_result.json`
- **Structured JSON:** [`c20071abc8858a3f6299.json`](../../sessions/c2/c20071abc8858a3f6299.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据已拉取。汇总如下：

## exp_025 中期 ve_ratio 汇总

### 各 seed 当前步数

| Seed | 服务器 | 当前步数 |
|------|--------|---------|
| s1 | bjb1-40020 | 65K |
| s2 | bjb1-40020 | 65K |
| s3 | bjb1-45299 | 65K |
| s4 | bjb1-45299 | **45K** |

### ve_ratio 全量数据

| step | s1 eval→ve | s2 eval→ve | s3 eval→ve | s4 eval→ve |
|------|-----------|-----------|-----------|-----------|
| 5K | 36.66→0.0000 | 35.23→0.0000 | 36.13→0.0000 | 30.91→0.0000 |
| 15K | 182.31→0.0230 | 141.78→0.0295 | 122.89→0.0271 | 176.61→0.0206 |
| 25K | 184.17→0.1585 | 169.20→0.1479 | 172.04→0.1299 | 179.07→0.1623 |
| 35K | 180.50→0.3517 | 161.66→0.3149 | 216.56→0.2395 | 100.25→**0.7183** |
| 45K | 209.25→0.4780 | 165.67→0.5586 | 375.62→0.2372 | 170.82→**0.6700** |
| 55K | 340.02→0.4818 | 195.11→0.6476 | 384.68→0.3712 | — |
| 65K | 393.24→0.5932 | 232.16→0.6993 | 480.45→0.4350 | — |

### 重点关注

- **s4@45K**: ve_ratio = 0.6700, eval_return = 170.82 — ve_ratio 偏高，eval_return 偏低。35K 时 ve_ratio 曾飙到 0.7183（eval 仅 100.25），value 过估严重。
- **s3@65K**: ve_ratio = 0.4350, eval_return = 480.45 — 四个 seed 中表现最好，eval 最高且 ve_ratio 最健康。
- **s2** ve_ratio 持续偏高（65K 达 0.6993），eval 增长缓慢（232）。
- **s1** 居中，65K 时 ve_ratio 0.5932, eval 393。

---
