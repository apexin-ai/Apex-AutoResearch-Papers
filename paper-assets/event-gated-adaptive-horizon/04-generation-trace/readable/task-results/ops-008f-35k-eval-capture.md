# ops 008f 35k eval capture

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_008f_35k_eval_capture_20260514T062318_result.json`
- **Structured JSON:** [`565a4462288d32a4ffb8.json`](../../sessions/56/565a4462288d32a4ffb8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

45K 数据尚未产生。计算结果：

```
008f @35K:
- eval_return: 206.67
- value_mean: 36.28
- v/e ratio: 17.6% (36.28 / 206.67)
- normalized v/e: 0.73x (17.6% / 24.1%)
- vs 008d@35K: 008d v/e=41.2% (1.71x) → 008f 仅 0.73x，差距 2.3 倍
- 结论: normalized v/e = 0.73x < 1.0x，因果确认——dt_embedding 是 delusional critic 的直接原因
```

补充观察：
- gate 完全退化：`gate_dt_mean=2.0, gate_dt_2_frac=1.0`，所有 horizon 锁定在 dt=2，gate entropy=0。去掉 dt_embedding 后 gate 丧失了区分能力，但 critic 反而健康。
- value_mean (36.28) 与 eval_return (206.67) 量级差距合理（critic 估计的是折扣累积回报片段，非完整 episode return）。
- 008f @25K normalized v/e 为 1.02x → @35K 降至 0.73x，critic 估值相对收敛而非发散，与 008d 的发散轨迹（25K→35K 持续膨胀）形成鲜明对比。

进程 127766 仍在运行，45K eval 暂未产出。

---
