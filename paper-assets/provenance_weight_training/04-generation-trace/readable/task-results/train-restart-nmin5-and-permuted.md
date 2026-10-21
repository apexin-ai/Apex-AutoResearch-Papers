# train restart nmin5 and permuted

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_restart_nmin5_and_permuted_20260524T164714_result.json`
- **Structured JSON:** [`06626ea2959427b26cbf.json`](../../sessions/06/06626ea2959427b26cbf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已重启并注册：

| exp_id | GPU | PID | 当前 step | 总 steps | retry_count |
|--------|-----|-----|-----------|----------|-------------|
| `p0_nmin_5` | cuda:1 | 966103 | ~6/6103 | 6103 | 2 |
| `permuted_score_control_seed42` | cuda:3 | 966241 | ~4/6103 | 6103 | 2 |

两个实验均已从 step 0 重新开始训练，日志正常输出，τ=0.7 确认正确。预计训练时间约 3.8h（按 ~2.2s/it 估算）。

---
