# diagnose contamination 60 grid b0 5 seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_contamination_60_grid_b0_5_seed42_20260516T013019_result.json`
- **Structured JSON:** [`6f85405a325aa5db498e.json`](../../sessions/6f/6f85405a325aa5db498e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**训练已完成，这是 false alarm。**

日志最后明确输出：
```
Training complete. Model saved to output/models/contamination_60_grid_b0_5_seed42/final
EXIT_CODE=129
```

关键证据：
1. **训练进度**: 6103/6103 steps 全部完成（`train_runtime: 13102.58s`, `train_steps_per_second: 0.466`）
2. **Checkpoint 完整**: `checkpoint-5500`, `checkpoint-6000`, `checkpoint-6103`（最终step）, 以及 `final/` 目录均存在
3. **SIGHUP 时机**: EXIT_CODE=129 出现在 "Training complete" 之后，说明 SIGHUP 是训练完成后 tmux session 断开导致的，不影响结果

| 问题 | 回答 |
|------|------|
| 训练是否完成？ | 是，6103/6103 steps 全部完成 |
| 失败原因 | 非真正失败。训练完成后收到 SIGHUP（tmux 断连），与 uniform 实验相同 |
| Checkpoint 可用？ | 可用，`final/` 和 `checkpoint-6103` 都在 |
| **建议** | **标记为 success** |

---
