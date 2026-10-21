# ops check smart compress eval results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_smart_compress_eval_results_20260518T012042_result.json`
- **Structured JSON:** [`26611a7f0f669f17b3b9.json`](../../sessions/26/26611a7f0f669f17b3b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
M=32 eval: running | ep 191/500 | SR = 64.9% (124/191) | ~37% done
M=64 eval: running | ep 174/500 | SR = 68.97% (120/174) | ~35% done
M=96 train: step 67050/100K (67%) | loss=0.039 | sps=4.1
M=16 train: step 63800/100K (64%) | loss=0.040 | sps=4.2

GPU status:
  GPU 0: 19%, 3462/24564 MiB (M=32 eval)
  GPU 1:  1%, 3494/24564 MiB (M=64 eval)
  GPU 2: 21%, 2787/24564 MiB (M=96 train)
  GPU 3:  0%, 2815/24564 MiB (M=16 train)
```

早期信号很积极：M=32 当前 ~65% SR，M=64 更高 ~69% SR。两个 eval 还需约 2 小时完成（按当前速度 ~6 sec/ep）。训练 M=96 和 M=16 都在正常推进，预计再跑约 2 小时完成。

---
