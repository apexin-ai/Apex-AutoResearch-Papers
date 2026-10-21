# Server Status: westd-11235 — 2026-05-16 09:17 UTC

## GPU 使用情况

| GPU | 显存占用 | 温度 | 功耗 | 利用率 | 进程 |
|-----|----------|------|------|--------|------|
| GPU 0 | 85,547 / 97,887 MiB | 80°C | 527W/600W | 100% | PID 212653 — `full_trace_1024tok_seed42` |
| GPU 1 | 46,527 / 97,887 MiB | 71°C | 476W/600W | 100% | PID 216816 — `debugbench_exception_only_seed42` |

## 训练任务状态

### 1. DeepSeek full_trace_seed42_v3 — ✅ 已完成

- **PID 163109**: 已退出（进程不存在）
- **完成时间**: ~07:26 UTC (训练 2h28m + eval 6min)
- **最终指标**:
  - train_loss: 0.0547
  - eval_loss: 0.1108
  - eval_mean_token_accuracy: 0.9801
  - train_runtime: 8891s (2h28m)
  - epoch: 3.0
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_full_trace_seed42_v3/final`
- **中间 checkpoints**: checkpoint-148, checkpoint-296, checkpoint-444

### 2. full_trace_1024tok_seed42 — 🔄 训练中

- **PID**: 212653 (运行 1h02m)
- **GPU**: 0
- **进度**: 296/444 steps (67%), eval 循环中
- **tmux session**: `full_trace_1024tok_seed42`
- **预计**: 还需约 50min 完成训练

### 3. debugbench_exception_only_seed42 — 🔄 训练中

- **PID**: 216816 (运行 6min)
- **GPU**: 1
- **进度**: 66/153 steps (43%), ~5s/it
- **tmux session**: `debugbench_exception_only_seed42`
- **预计**: 还需约 8min 完成训练

### 4. deepseek_exception_only_seed456 — ⚠️ tmux 存在但无活跃 python 进程

- tmux session PID 160926 存在，但未在 GPU 进程列表中
- 已完成（exit file 存在于 `/tmp/agent-ml-exit/deepseek_exception_only_seed456.exit`）

## 磁盘空间

| 挂载点 | 总量 | 已用 | 可用 | 使用率 |
|--------|------|------|------|--------|
| /root/autodl-tmp | 250G | 110G | 141G | 44% |

## 异常发现

- **GPU 0 温度 80°C**: 接近高温区，但在 600W TDP 卡满载下属正常范围
- **CUDA 版本**: 显示 13.2（Driver 595.58.03），之前记录为 12.8 — 可能驱动已更新
