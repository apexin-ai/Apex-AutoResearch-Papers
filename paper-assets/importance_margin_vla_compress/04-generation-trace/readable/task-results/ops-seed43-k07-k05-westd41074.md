# ops seed43 k07 k05 westd41074

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_seed43-k07-k05-westd41074_20260520T131639_result.json`
- **Structured JSON:** [`573e02b6d9ff384dea6b.json`](../../sessions/57/573e02b6d9ff384dea6b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已启动，汇总：

| 实验 | GPU | PID | tmux session | 输出 |
|------|-----|-----|-------------|------|
| k=0.7 seed=43 | cuda:0 (15GB) | 461502 | `eval_random_k07_seed43` | `eval_results/eval_openvla_random_k07_seed43.json` |
| k=0.5 seed=43 | cuda:1 (15GB) | 461577 | `eval_random_k05_seed43` | `eval_results/eval_openvla_random_k05_seed43.json` |

- GPU 2 (M96 training, PID 68539) 和 GPU 3 (M64 training, PID 68852) 未受影响
- 实际脚本是 `eval_oft_prune_libero.py`（不是 `eval_openvla_libero.py`）
- Registry 条目已注册，parent = `eval_openvla_prune_seed43_sweep`
- 预估完成时间：libero_object 10 tasks × 50 episodes，约 4-6 小时（参考之前 seed=7 的运行时间）

---
