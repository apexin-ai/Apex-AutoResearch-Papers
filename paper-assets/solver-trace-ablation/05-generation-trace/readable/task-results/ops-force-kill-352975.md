# ops force kill 352975

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_force-kill-352975_20260515T125959_result.json`
- **Structured JSON:** [`50a5aa1f188e01293354.json`](../../sessions/50/50a5aa1f188e01293354.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。结果汇总：

**Step 1 - kill -9 352975**: 进程已不存在（`No such process`），说明在执行前已自行退出。

**Step 3 - 进程确认**: `PROCESS_GONE` — 352975 已消失。

**Step 4 - nvidia-smi**:
```
GPU 0: NVIDIA RTX PRO 6000 Black — 63861MiB / 97887MiB — 99% util — PID 352142 (63852MiB)
GPU 1: NVIDIA RTX PRO 6000 Black — 40701MiB / 97887MiB —  5% util — PID 353661 (40692MiB)
```
cuda:1 上只剩 r3 (PID 353661) 的 ~40GB，僵尸进程的 53GB 已释放。

**Step 5 - r3 状态**: PID 353661, 状态 `Rl`（运行中），已运行 4 分 17 秒。
```
python3 scripts/train_sft.py --model_path /root/autodl-tmp/models/Qwen3-4B \
  --data_path data/train_500_seed42.jsonl \
  --output_dir /root/autodl-tmp/outputs/plan009_sft_baseline_s44_1000 \
  --num_steps 1000 --seed 44 --no_wandb --gpu 1
```

**Step 6 - r3 日志**: 正常训练中，当前进度 150/1000 steps，速度 ~1.25 it/s。

cuda:1 已恢复正常，r3 不受影响。

---
