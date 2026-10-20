# ops verify gpu5

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_verify-gpu5_20260513T235849_result.json`
- **Structured JSON:** [`95b1b70840377f667b75.json`](../../sessions/95/95b1b70840377f667b75.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，确认如下：

| 项目 | 状态 |
|------|------|
| GPU 5 进程 | PID **239734**，正在运行 |
| 显存使用 | **21,995 MiB / 24,564 MiB**（~89%） |
| GPU 利用率 | 72% |
| 训练进度 | **66 / 3,177 steps**（~2%） |
| 速度 | ~1.0-1.1 s/it |
| ETA | **约 55 分钟** |
| 模型 | Qwen2.5-0.5B + LoRA (r=16, alpha=32) |
| 训练样本 | 50,826 条 |

**注意**：bitsandbytes 报了 `libnvJitLink.so.13` 加载失败的错误，但这是非致命的——训练已正常跳过并继续执行。日志开头未直接打印 `--gpu` 参数，但 `nvidia-smi` 确认进程在 GPU 5 上运行。

---
