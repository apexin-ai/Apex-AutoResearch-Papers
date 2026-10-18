# ops verify gpu state

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpu-state_20260520T094934_result.json`
- **Structured JSON:** [`c6188e66a864df646645.json`](../../sessions/c6/c6188e66a864df646645.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
westd-38929:
  GPU 状态:
    GPU 0: 1MiB / 97887MiB — 空闲
    GPU 1: 1MiB / 97887MiB — 空闲
    GPU 2: 1MiB / 97887MiB — 空闲
    GPU 3: 4840MiB / 97887MiB — 占用 (PID 94627, python)
  
  X-VLA eval 进程: ✅ 在运行
    PID 94627: python eval_xvla_pruning_libero.py --keep_ratio 0.7 --num_episodes 50 --gpu 0 --suite libero_object (运行在 GPU 3)
    父进程: PID 94610 (bash run_xvla_sweep.sh)
    当前进度: k=0.7 正在执行，41/50 episodes 完成（最新日志 17:50:07 UTC）
  
  已完成结果 (Batch 1 前三个):
    k=1.0: SR=99.2% (496/500), 50→50 tokens
    k=0.95: SR=99.0% (495/500), 50→47 tokens
    k=0.9: SR=97.6% (488/500), 50→45 tokens
    k=0.7: 进行中，约 10 分钟内完成
  
  Batch 2 自动启动: ✅ 有
    run_xvla_sweep.sh 中 Batch 1 的 4 个 k 值用 `wait` 阻塞，完成后自动启动 Batch 2 (k=0.5/0.3/0.2/0.1)
    无 crontab，靠脚本内 sequential batch 机制自动衔接

westd-41074:
  GPU 状态:
    GPU 0: 1MiB / 97887MiB — 空闲
    GPU 1: 4872MiB / 97887MiB — 占用 (PID 125816)
    GPU 2: 28555MiB / 97887MiB — 占用 (PID 68539)
    GPU 3: 27535MiB / 97887MiB — 占用 (PID 68852)
  PID 94311: ✅ 已死（进程不存在）
```

**结论**：之前的诊断 Worker (09:16 UTC) 看到 GPU 0MiB 是因为当时进程确实还没启动或已崩溃后被重新启动。当前 sweep 脚本是活的——k=1.0/0.95/0.9 已完成，k=0.7 还剩 ~9 episodes，完成后 Batch 2 会自动启动。westd-41074 的 PID 94311 已确认被 kill。

---
