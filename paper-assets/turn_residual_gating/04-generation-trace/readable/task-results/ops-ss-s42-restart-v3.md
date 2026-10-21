# ops ss s42 restart v3

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_ss_s42_restart_v3_20260522T160335_result.json`
- **Structured JSON:** [`034072855a602c69f596.json`](../../sessions/03/034072855a602c69f596.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Step 6: 结果**

```
STATUS: PASS ✓
PID: 33402
GPU MEM: 65.0 GiB / 97.9 GiB (66%)
TMUX: alive (ss_s42_v3)
LOG LAST 5 LINES:
  Resume: start_epoch=1, global_step=1000, lr=[0.0001686, 0.001686]
  Epoch 1 Step 0 | L_NTP=1.1575 L_GAR=0.0000 L_DIV=0.0000 Loss=1.1575 | Gate=0.9743 | Mem=42.3GB | SS=no ratio=0.300
```

三项全部 PASS。训练已从 epoch_0 checkpoint 成功 resume（start_epoch=1, global_step=1000），正在运行 Epoch 1。

---
