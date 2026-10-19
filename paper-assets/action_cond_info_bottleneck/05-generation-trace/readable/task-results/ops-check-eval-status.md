# ops check eval status

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-status_20260516T173043_result.json`
- **Structured JSON:** [`1950fc236fc98070a51a.json`](../../sessions/19/1950fc236fc98070a51a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### 进程状态

| Eval | PID | 状态 | 运行时长 | 实际 out_dir |
|------|-----|------|---------|-------------|
| fixed seed1 | 104743 | **存活** (Rl+) | 9h26m | `/root/autodl-tmp/v7_eval_fixed_seed1/` |
| fixed seed2 | 111920 | **存活** (Rl+) | 4h48m | `/root/autodl-tmp/v7_eval_fixed_seed2/` |

注意：seed2 的实际输出目录是 `v7_eval_fixed_seed2`，不是任务描述中的 `v7_eval_seed2`。

### 进度

两个 eval 都处于 **第 1 个 suite (libero_spatial) 的第 1 个 task (libero_spatial_0)** 阶段，各完成了 10 个 episode 的视频录制。4 个 suite 均无 `eval_info.json`，尚未完成任何 suite。

### GPU 使用情况

| GPU | 显卡 | 利用率 | 显存占用 |
|-----|------|--------|---------|
| 0 | RTX PRO 6000 Blackwell | 1% | 6578 / 97887 MiB |
| 1 | RTX PRO 6000 Blackwell | 0% | 6596 / 97887 MiB |

### 注意事项

两个进程的命令行都显示 `--gpu 0`，但两张 GPU 各有 ~6.5GB 显存占用，说明可能通过 `CUDA_VISIBLE_DEVICES` 做了映射，实际各占一张卡。eval 正常进行中，无需干预。

---
