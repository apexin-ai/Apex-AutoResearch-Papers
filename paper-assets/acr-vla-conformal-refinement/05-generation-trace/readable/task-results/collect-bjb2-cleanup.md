# collect bjb2 cleanup

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_collect_bjb2-cleanup_20260527T230956_result.json`
- **Structured JSON:** [`0928bf1f4646876efdad.json`](../../sessions/09/0928bf1f4646876efdad.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**所有 6 个 GPU 都在跑实验，不是空闲的。** 用户前提有误。

当前 bjb2-28827 实际状态：

| GPU | PID | 运行时间 | 实验 | τ |
|-----|-----|---------|------|---|
| 0 | 4609 | 19min | long, SmolVLA | 0.15 |
| 1 | 5160 | 19min | long, SmolVLA | 0.20 |
| 2 | 5635 | 19min | long, SmolVLA | 0.30 |
| 3 | 7362 | 19min | long, SmolVLA | 0.35 |
| 4 | 13514 | 1h55m | long (output 文件名误写 spatial) | 0.15 |
| 5 | 934207 | 4h14m | long, SmolVLA | 0.05 |

每个 GPU 占用 ~6.3GB（GPU 5 为 2.3GB）。日志只有 15 行是因为刚启动不久（Long benchmark 520 steps × 10 tasks × 20 rollouts，很慢）。

**结论：不能清理 tmux session、不能提交新实验。** 这些实验正在运行，杀掉会丢失进度。

注意 PID 13514 有个疑似 bug：命令是 `--benchmark long` 但 output_file 写的是 `eval_spatial_...`，可能需要确认是否有意为之。

---
