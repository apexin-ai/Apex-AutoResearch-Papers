# ops westd41074 gpu1 identify

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd41074-gpu1-identify_20260520T102834_result.json`
- **Structured JSON:** [`300dc5f891bca0d2cbc8.json`](../../sessions/30/300dc5f891bca0d2cbc8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果如下：

```
PID 125816:
  状态: 存在
  命令: python eval_xvla_pruning_libero.py --model_path /root/autodl-tmp/X-VLA-Libero --suite libero_object --keep_ratio 0.95 --num_episodes 50 --seed 42 --domain_id 3 --gpu 0 --output eval_results/xvla_prune_k0.95_libero_object.json
  用户: root
  启动时间: 17:26:46
  运行时长: 01:02:04
  GPU 显存: 4853 MiB (GPU 1)
  父进程: PID 94304 — bash run_xvla_prune_sweep.sh
  工作目录: /root/autodl-tmp/importance_margin_vla_compress
  关联实验: X-VLA pruning sweep — libero_object suite, keep_ratio=0.95, domain_id=3
  建议: 这是 X-VLA pruning evaluation sweep 的一部分（注意命令行写了 --gpu 0 但实际跑在 GPU 1 上，可能脚本内部有 remap）。已运行约 1 小时，是活跃的 eval 任务。建议保留，等它跑完。如果不需要这个 sweep 了再 kill。

GPU 0: 空闲 (1 MiB)
GPU 1: PID 125816 — X-VLA prune eval, 4853 MiB, 39% util
GPU 2: PID 68539 — M=96 训练, 28546 MiB
GPU 3: PID 68852 — M=64 训练, 27526 MiB
```

关键发现：PID 125816 不是残留进程，是 `run_xvla_prune_sweep.sh` 启动的 X-VLA pruning evaluation（keep_ratio=0.95, libero_object, domain_id=3）。父进程 PID 94304 是 sweep 脚本，说明可能还会顺序启动更多 eval 任务。

---
