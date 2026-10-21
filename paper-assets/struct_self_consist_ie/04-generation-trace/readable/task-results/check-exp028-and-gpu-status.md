# check exp028 and gpu status

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp028_and_gpu_status_20260517T083227_result.json`
- **Structured JSON:** [`0e6699ba8975f3ebb1fe.json`](../../sessions/0e/0e6699ba8975f3ebb1fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Log 最新到 step 1450，但进度条显示已到 1477。综合报告：

```
exp_028 Status:
- PID: alive (371545)
- Current step: ~1477 / 41180
- Current epoch: 0.18 / 5
- Loss: 0.0765 (step 1450)
- ETA: ~26 hours
- GPU: cuda:0

GPU Status:
- cuda:0: 87% util, 28494 MiB / 32607 MiB
- cuda:1:  0% util,     2 MiB / 32607 MiB
- cuda:2:  0% util,     2 MiB / 32607 MiB
- cuda:3:  0% util,     2 MiB / 32607 MiB
```

训练速度稳定在 ~1.9s/it，loss 从 0.0845 (step 1250) 下降到 0.0765 (step 1450)，趋势正常。3 张卡空闲。

---
