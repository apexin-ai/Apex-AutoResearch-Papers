# audit bjb1 18228 precompute check

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_bjb1-18228-precompute-check_20260523T123546_result.json`
- **Structured JSON:** [`73c8db61d3c96d88726b.json`](../../sessions/73/73c8db61d3c96d88726b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**bjb1-18228 Pi0.5 Precompute 状态**

| GPU | Benchmark | 进度 | 完成% | 已用时间 | 预计剩余 | 预计完成时间 |
|-----|-----------|------|-------|---------|---------|------------|
| 0 | object | 30500/72507 | 42.1% | 16.2h | **22.3h** | ~5/24 19:00 |
| 1 | spatial | 29200/60250 | 48.5% | 16.2h | **17.2h** | ~5/24 14:00 |
| 2 | goal | 29200/61728 | 47.3% | 16.2h | **18.1h** | ~5/24 14:40 |
| 3 | long | 30400/136090 | 22.3% | 16.2h | **56.2h** | ~5/25 05:00 |

所有进程速度 ~1.91-2.00s/sample，GPU 利用率 23-25%，显存占用 ~9.9GB/24.6GB。

**结论：4 张卡全部 busy，无空闲 GPU 可分配。** spatial 和 goal 最快释放（明天下午），long benchmark 数据量最大（136K samples），预计后天凌晨才能完成。

---
