# analyze gemma2 hires bf16 2bitonly

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_gemma2_hires_bf16_2bitonly_20260514T225101_result.json`
- **Structured JSON:** [`58c224fa8732e18803cb.json`](../../sessions/58/58c224fa8732e18803cb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
STATUS: still_running
PROGRESS: 160/336 heads (47.6%), elapsed 46.6min, ETA ~51min
PID: 268242 (alive)
GPU: cuda:0 @ 100% utilization, 20229 MiB / 97887 MiB

cron sentinel exit_code=0 确认为假阳性——进程仍在跑。

当前速度: ~17.5s/head
预计完成时间: ~2026-05-14 01:10 UTC (约51min后)

目前高 delta heads (top-5 so far):
  L13H3: 0.039025
  L15H7: 0.030296
  L17H6: 0.025366
  L15H6: 0.025188
  L19H6: 0.019447

趋势: L15+ 层 delta 明显增大，与其他模型一致的后层集中模式。
结果文件尚未生成，需等实验完成。
```

---
