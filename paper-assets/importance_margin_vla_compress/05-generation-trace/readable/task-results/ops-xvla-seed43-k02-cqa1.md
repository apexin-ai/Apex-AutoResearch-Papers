# ops xvla seed43 k02 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-seed43-k02-cqa1_20260520T151149_result.json`
- **Structured JSON:** [`d5503c8b187f6ab287b6.json`](../../sessions/d5/d5503c8b187f6ab287b6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

**汇总：**
- **PID**: 443004 (python 进程), GPU 0, `cuda:0`
- **配置**: X-VLA L2 norm pruning, k=0.2 (keep 20%, 即 50 → 10 vision tokens), seed=43, libero_object, 50 episodes/task × 10 tasks
- **日志**: `logs/eval_xvla_prune_k02_seed43.log`
- **输出**: `eval_results/xvla_prune_k0.2_libero_object_seed43.json`
- **预估完成时间**: 参考同 suite 其他 eval，约 2-3 小时（~凌晨 1:30-2:30）

当前 GPU 分配：
| GPU | 任务 | PID |
|-----|------|-----|
| 0 | seed43 k=0.2 | 443004 |
| 1 | seed44 k=0.3 | 346216 |
| 2 | seed44 k=0.5 | 132420 |
| 3 | seed43 k=0.3 | 344867 |

---
