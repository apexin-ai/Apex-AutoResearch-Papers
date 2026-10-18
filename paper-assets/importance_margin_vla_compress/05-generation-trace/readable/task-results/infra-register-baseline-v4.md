# infra register baseline v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_register-baseline-v4_20260515T152810_result.json`
- **Structured JSON:** [`473be60adf0d506c406a.json`](../../sessions/47/473be60adf0d506c406a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### Baseline 训练 ✅ 正常运行

| 项目 | 值 |
|------|-----|
| **主进程 PID** | **30745** (`python3 train.py --config configs/baseline.yaml --gpu 0 --seed 42`) |
| tmux session PID | 30738 |
| 数据加载 worker PIDs | 31027, 31028, 31029, 31030 |
| GPU 0 | 48% 利用率, 4114 MiB / 97887 MiB |
| 当前进度 | **step 600/30000**, loss=0.0286, lr=6.01e-05, sps=4.0 |
| wandb | offline 模式, run id `7dikql04` |

Loss 从 step 0 的 3.4066 快速下降到 step 600 的 0.0286，训练正常收敛。

---

### IMM Anchor ❌ 已崩溃

没有找到 IMM anchor 的运行进程。日志显示启动时报错：

```
OSError: Can't load the configuration of 'HuggingFaceTB/SmolVLM2-500M-Video-Instruct'
```

模型配置加载失败，可能是模型未下载完成或缓存路径问题。GPU 1 空闲（0% 利用率，3 MiB 显存），确认 IMM anchor 未在运行。

---
