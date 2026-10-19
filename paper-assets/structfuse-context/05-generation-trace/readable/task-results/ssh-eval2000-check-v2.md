# ssh eval2000 check v2

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_eval2000_check_v2_20260514T014910_result.json`
- **Structured JSON:** [`60d36f12f530f4f4b02e.json`](../../sessions/60/60d36f12f530f4f4b02e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志最后一行是 `step 2000 loss=0.0429`，但 **eval@2000 还没出**——训练刚到 step 2000，eval 还没开始跑。

已有的 eval checkpoint 汇总：

| Eval | val_loss | R@1 | R@5 | R@10 |
|------|----------|-----|-----|------|
| @500 | 0.4869 | 0.5332 | 0.9540 | 1.0 |
| @1000 | **0.4651** | **0.5527** | 0.9594 | 1.0 |
| @1500 | 0.5365 | 0.5228 | 0.9550 | 1.0 |

eval@1000 是目前的 best（val_loss 和 R@1 均最优）。eval@1500 出现了明显退化（val_loss 升高、R@1 下降），进入 epoch 2 后有 overfitting 迹象。

训练正在继续（step 2000 刚打印），eval@2000 应该很快会出。

---
