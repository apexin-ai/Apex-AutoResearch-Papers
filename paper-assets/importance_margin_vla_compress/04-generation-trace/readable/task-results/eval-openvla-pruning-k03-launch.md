# eval openvla pruning k03 launch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_openvla_pruning_k03_launch_20260518T012419_result.json`
- **Structured JSON:** [`f66d74ac54a6bcb22efa.json`](../../sessions/f6/f66d74ac54a6bcb22efa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

PID 768729 **已经在跑你要求的任务**，不需要 kill。

日志确认：
```
[*] libero_object: 10 tasks x 50 episodes = 500 total
[*] Random pruning: k=0.3
```

完整命令：
```
python -u /tmp/eval_openvla_libero_gpu1.py --mode random_prune --k_ratio 0.3 --suite libero_object --num_episodes 50 --seed 7
```

参数与 k=0.7 (GPU:0, PID 755671) 完全一致，仅 `--k_ratio` 不同。`--num_episodes 50` 是每 task 50 eps，10 tasks 共 500 episodes。

当前进度：Task 1/10, Ep 30/50，速度 ~1.7 eps/min。预计总耗时约 5 小时。

- PID: **768729**
- GPU: cuda:1
- 日志: `eval_results/openvla_random_prune_k03_object.log`

---
