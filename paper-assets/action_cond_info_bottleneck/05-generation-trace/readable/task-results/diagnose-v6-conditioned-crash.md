# diagnose v6 conditioned crash

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_v6-conditioned-crash_20260516T093057_result.json`
- **Structured JSON:** [`2590e64c1bfad20511a8.json`](../../sessions/25/2590e64c1bfad20511a8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

**进程存活：Y**

| 指标 | 值 |
|------|-----|
| PID | 866194，状态 Sl，运行时间 2h51m |
| 当前 step | 10800/20000 (54%) |
| 速度 | 1.1 steps/s |
| GPU 0 显存 | 16,227 MiB / 97,887 MiB (16.6%) |
| GPU 利用率 | 74% |
| 温度/功耗 | 65°C / 446W |
| Exit marker | 不存在（未退出） |

**训练健康**：正常运行中。loss 稳定在 0.0~0.05 区间，IB loss ~0.20，diversity loss ~-0.46，β 已完成 warmup 固定在 0.01。checkpoint-10000 已保存。

**Registry 标记 DONE/failed 是误报**——进程从未中断。预计剩余 ~9200 steps ÷ 1.1 steps/s ≈ 2.3 小时完成（约 19:50 UTC）。

---
