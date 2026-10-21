# monitor shard progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_shard-progress-check_20260516T050006_result.json`
- **Structured JSON:** [`21b6c64f08675098cc80.json`](../../sessions/21/21b6c64f08675098cc80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## CWM 8B ckpt-400 Test Eval 进度报告

**测试集**: 9784 samples (`swebench_test.jsonl`)
**当前服务器时间**: ~13:03 (UTC+8)

### 各 Shard 状态

| Shard | PID | 范围 | 已完成 | 目标 | 进度 | 速度 | 剩余时间 |
|-------|-----|------|--------|------|------|------|---------|
| **Shard1** | 443221 (alive, 100% CPU) | 0→9783 (全集) | 7464 | 9784 | 76.3% | ~8.5/min | **~4h34m** |
| **Shard2** | 448100¹ (alive, 100% CPU) | 7680→9783 | 1856 | 2104 | 88.2% | ~8.6/min | **~29m** |
| **Shard3** | 453335 (alive, 100% CPU) | 6200→7679 | 1208 | 1480 | 81.6% | ~8.5/min | **~32m** |
| **Shard4** | — | 9096→9783 | 688 | 688 | **100%** | — | **DONE** |

¹ PID 448094 是 bash wrapper (0% CPU 正常)，实际 Python 子进程 PID 448100 在跑。

### 覆盖分析

```
Index:  0 -------- 6200 ---- 7464 -- 7680 --------- 9096 -- 9536 -- 9784
Shard1: [███████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░]  → 7464
Shard3:                      [████████████░░░░]                          → 7408
Shard2:                                  [██████████████████████░░░]     → 9536
Shard4:                                                    [████████]    → DONE
```

**唯一未覆盖区间: 7464–7679 (216 samples)**

Shard1 (从 7464 向前) 和 Shard3 (从 7408 向 7679) 都在同时填补这个 gap。

### ETA

- **全覆盖 ETA: ~13:30（约 27 分钟后）** — Shard1 到达 7680 即关闭 gap
- Shard2 自然结束: ~13:32
- Shard3 自然结束: ~13:35
- Shard1 自然结束: **~17:35** — 但 7680+ 的结果与 Shard2+4 重复

### 建议

Shard1 到达 ~7680 后，0–9783 全部 index 已被至少一个 shard 覆盖。此时可以 kill shard1 释放 GPU，然后跑 `merge_cwm8b_shards.py` 合并 4 个 shard。

**实际可用时间: ~30 分钟后。** 如果让 shard1 自然跑完则需要额外 ~4 小时，但不会增加新覆盖。

---
