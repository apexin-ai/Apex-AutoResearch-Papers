# monitor smolvla baseline status

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_smolvla-baseline-status_20260522T231339_result.json`
- **Structured JSON:** [`cf388370a4160cbfa88f.json`](../../sessions/cf/cf388370a4160cbfa88f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个实验全部完成，进程已退出。

```
Goal seed43:    ✓ done  SR = 82.0%  (164/200)
Goal seed44:    ✓ done  SR = 78.0%  (156/200)
Spatial seed43: ✓ done  SR = 54.5%  (109/200)
```

每个实验 10 tasks × 20 episodes = 200 episodes。日志均以 "End of eval" 正常结束（seed43 @ 05:12, seed44 @ 05:17, spatial @ 05:11）。无报错。

对比 Object baselines（seed42=66.5%, seed43=66.5%, seed44=65%），Goal 的 SR 明显更高（78-82%），Spatial 较低（54.5%），符合 LIBERO 各 suite 的难度梯度。

---
