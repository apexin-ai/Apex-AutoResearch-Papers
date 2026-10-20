# diagnose exp 086 failed

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_exp_086_failed_20260525T180955_result.json`
- **Structured JSON:** [`ccb2e072787ad7107124.json`](../../sessions/cc/ccb2e072787ad7107124.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。关键发现：

## exp_086 诊断报告

### 失败进度
- **最后记录 step**: 48000 / 105000（~46%）
- **最后 eval (step 45000)**: eval_return = 133.2

### 失败原因：SIGHUP（终端断连）
- EXIT_CODE=129 = 128+1 = **SIGHUP 信号**
- 日志中**无任何** OOM、CUDA error、RuntimeError 或 Traceback
- dmesg 无权限读取，但 grep 日志确认无错误
- 日志末尾有两次 "Terminated" 字样，是进程收到 HUP 信号后被终止的表现
- **结论**：原 tmux session 断开或被杀，导致 SIGHUP 传播到训练进程

### 当前状态：已被重启
- tmux session `exp_086_frozen_dt_emb_cheetah_s0` **已重建**（02:10:27 创建）
- Python 进程 PID 40748 **正在运行**（415% CPU）
- GPU 0 当前 1 MiB（新进程仍在初始化阶段）
- GPU 1 使用 3242 MiB（exp_087 正常运行，40% utilization）

### 原始启动命令
```bash
python -u dreamer.py --configs defaults dmc_proprio \
  --task dmc_cheetah_run \
  --logdir logdir/exp_086_frozen_dt_emb_cheetah_s0 \
  --steps 105000 --seed 0 --compile False --device cuda:0 \
  --gate_enabled True --gate_fixed_dt 2 --gate_subsample_max_dt 2 \
  --imag_horizon 8 --dt_emb_freeze True
```

### 注意事项
新启动的运行使用 `>` 重定向（非 `>>`），旧日志会被覆盖。如果需要保留上一次运行到 step 48000 的日志/checkpoint 数据，当前 logdir 中的 checkpoint 可能已被新运行覆盖或继续使用（取决于代码是否支持 resume）。建议确认新运行是从 step 0 重新开始还是从 checkpoint 恢复。

---
