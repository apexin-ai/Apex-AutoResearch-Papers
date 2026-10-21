# status n16 n32 check

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_status_n16_n32_check_20260522T231322_result.json`
- **Structured JSON:** [`08db91f7eda58269b217.json`](../../sessions/08/08db91f7eda58269b217.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== autodl-5090-c (n16_v2, PID 452387) ===
GPU状态: cuda:1 占用 | 29901MiB/32607MiB | 80% util | 73°C | 491W
进度: 95.9% | 577,760/602,368 prompts
已运行: 7h51m | 速度: ~17-32 it/s
ETA: ~20 分钟

=== autodl-5090 (n32_v2, PID 157197→157469) ===
GPU状态: cuda:3 占用 | 29844MiB/32607MiB | 69% util | 69°C | 444W
进度: 37.1% | 447,456/1,204,736 prompts
已运行: 6h56m | 速度: ~15-28 it/s
ETA: ~11.7 小时（预计今晚 ~20:00 服务器时间完成）
```

n16_v2 即将完成，n32_v2 还需要较长时间（总 prompts 数是 n16 的 2 倍，37648×32=1,204,736）。

---
