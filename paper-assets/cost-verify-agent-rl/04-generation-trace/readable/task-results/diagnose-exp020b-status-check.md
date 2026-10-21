# diagnose exp020b status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp020b-status-check_20260514T223629_result.json`
- **Structured JSON:** [`047bf5a16f24e40f6d90.json`](../../sessions/04/047bf5a16f24e40f6d90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. PID 389434 & 389435 — 存活
```
389434 386605 SNl  23:49 ray::WorkerDict
389435 386605 SNl  23:49 ray::WorkerDict
```

### 2. tmux — 命令被 read_only 拦截
（tmux 不在白名单中）

### 3. train.py 进程 — exp020b 主进程存活
```
PID 385982 (uptime 24:18): python train.py --config-name _alfworld_exp018_sft_grpo 
    model_path=.../qwen3_exp019b_sft 
    trainer.experiment_name=exp020b-alfworld-sft-grpo
```
另有大量 Ray worker 进程在运行，包括两个 Ray session：
- Session 06:12:58 (exp020b): workers 389434, 389435
- Session 06:19:56 (exp020d): workers 394054, 394055, 393854 等

### 4. GPU 使用
```
GPU 0: 100%, 51432 MiB / 97887 MiB
GPU 1: 100%, 51492 MiB / 97887 MiB
```

GPU 上的计算进程：
```
PID 389434 @ GPU-0: 20500 MiB  (exp020b WorkerDict)
PID 394054 @ GPU-0: 40084 MiB  (exp020d actor_rollout_update_actor)
PID 389435 @ GPU-1: 20500 MiB  (exp020b WorkerDict)
PID 394055 @ GPU-1: 40144 MiB  (exp020d actor_rollout_update_actor)
```

### 5. exp020b 日志（最后 30 行）
训练正在推进：
```
Training Progress: 7% | 2/30 [15:51<3:58:41, 511.48s/it]
```
- Step 0 val: success=0.0, pass@1=0.0
- Step 1 train: success=0.1875, pass@16=0.75, entropy=0.107
- 每步约 275-511s，预计剩余约 4 小时

关键训练指标（Step 1）：
- `actor/pg_loss`: 6.39e-05
- `actor/ppo_kl`: 9.30e-05
- `actor/entropy`: 0.107
- `actor/grad_norm`: 2.777
- `critic/score/mean`: 1.875
- `perf/throughput`: 414.9 tokens/s

### 6. exp020d 日志 — **也在运行，未停止**
```
Training Progress: 3% | 1/30 [05:18<2:34:10, 318.98s/it]
```
exp020d 也在运行中（PIDs 393854, 394054, 394055），正在执行 Step 1 的 actor update。

**总结：exp020b 和 exp020d 都在运行，两个实验共享 GPU 0 和 GPU 1（各占约 60GB/98GB）。GPU 利用率均 100%。**

---
