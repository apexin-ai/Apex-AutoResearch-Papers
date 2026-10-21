# analyze eval xvla l2norm k03 goal seed42 v5

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_xvla_l2norm_k03_goal_seed42_v5_20260524T101455_result.json`
- **Structured JSON:** [`34b6e24b32f4977f5d5c.json`](../../sessions/34/34b6e24b32f4977f5d5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果汇总：

**X-VLA L2norm k=0.3 Goal seed42 v5**
- **Overall SR: 37.0% (185/500)**，95% CI: [32.9%, 41.3%]
- 无错误，EXIT_CODE=0，耗时 84 min

| Task | SR | 描述 |
|------|------|------|
| 0 | 42% (21/50) | open the middle drawer |
| 1 | 92% (46/50) | put bowl on stove |
| 2 | 20% (10/50) | wine bottle on cabinet |
| 3 | 24% (12/50) | drawer + bowl inside |
| 4 | **98%** (49/50) | bowl on top of cabinet |
| 5 | 0% (0/50) | push plate |
| 6 | 2% (1/50) | cream cheese in bowl |
| 7 | 16% (8/50) | turn on stove |
| 8 | 76% (38/50) | bowl on plate |
| 9 | 0% (0/50) | wine bottle on rack |

**对比分析**：
- v3/v4: 37.6% (188/500) → v5: 37.0% (185/500)，差 3 episodes，在 CI 内，**结果一致**
- L2norm k=0.3 (37.0%) vs L2norm k=0.5 (59.6%): 从 50% 降到 30% keep ratio 损失 22.6pp
- L2norm k=0.3 (37.0%) vs Random k=0.5 (67.9%): L2norm 在低保留率下显著弱于 random 在高保留率

---
