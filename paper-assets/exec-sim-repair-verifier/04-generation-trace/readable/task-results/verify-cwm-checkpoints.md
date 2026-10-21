# verify cwm checkpoints

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_cwm-checkpoints_20260517T174042_result.json`
- **Structured JSON:** [`0a4c491627166a59eeee.json`](../../sessions/0a/0a4c491627166a59eeee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

MD5 完全一致。结论明确：

```
=== CWM s123 ===
Available checkpoints: checkpoint-4422 (epoch 1), checkpoint-8844 (epoch 2)
checkpoint-13266 exists: NO
Training process: not running (stopped at epoch 2)
Current eval: PID 668680, using checkpoint-8844 (epoch 2, latest available)
Action taken: 继续当前 eval，无更优 checkpoint 可用

=== CWM s42 ===
best/ global_step: 13266 (无 trainer_state，通过 md5 确认)
best/ epoch: 3.0 (= last epoch)
Last-epoch checkpoint: checkpoint-13266 (step 13266, epoch 3.0)
best/ == last-epoch: YES (md5 e99085b4b34cd4a87ba53197f8c60948 完全一致)
Current eval: PID 662946, using best/ on cuda:0
Action taken: 无需操作，已在用 last-epoch checkpoint
```

**需要关注**: s123 训练似乎在 epoch 2 后中断（max_steps=13266 但只到 8844），没有训练进程在跑。如果需要 epoch 3 的 checkpoint，需要恢复训练。

---
