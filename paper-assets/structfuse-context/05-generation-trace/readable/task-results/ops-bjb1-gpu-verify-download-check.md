# ops bjb1 gpu verify download check

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1-gpu-verify-download-check_20260513T032104_result.json`
- **Structured JSON:** [`540c69f68c1e70b9aff4.json`](../../sessions/54/540c69f68c1e70b9aff4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== GPU 验证 ===
GPU 0: ⚠️ TIMEOUT — torch 测试 30s 超时，stdout/stderr 均为空
GPU 1: 未单独测试（torch 初始化在 GPU 0 卡住导致整体超时）
GPU 0 matmul: TIMEOUT
GPU 1 matmul: TIMEOUT

分析：CUDA 初始化挂在 GPU 0 上，整个 python 进程卡死。
nvidia-smi 确认 GPU 0 异常：100% util / 3MiB memory / 无进程——典型 GPU hang 状态。

=== 模型下载 ===
Qwen2.5-Coder-3B: 下载中 23% (1.05G/4.62G, 1.75MB/s, ETA ~34min)
StarCoder2-3B:     进程存活(PID 2821)，但日志为空白行
flash-attn:        编译中 ("Building wheel... still running...")
磁盘已用: 4.5G (/root/autodl-tmp/models/)

=== nvidia-smi ===
Wed May 13 11:22:40 2026    Driver 590.44.01    CUDA 13.1
GPU 0: RTX PRO 6000 Black 96GB | 34°C P0 | 95W/600W | 3MiB/97887MiB | 100% util ← 异常
GPU 1: RTX PRO 6000 Black 96GB | 27°C P8 | 35W/600W | 3MiB/97887MiB |   0% util ← 正常
No running processes found
```

**GPU 0 问题确认**：100% utilization + 3MiB memory + 无进程 = GPU hang。这导致 torch CUDA 初始化卡死（整个 python 进程 30s 超时无输出）。

需要修复 GPU 0，建议用 `ssh_execute` 执行 `nvidia-smi -r` 重置 GPU，或者先用 `CUDA_VISIBLE_DEVICES=1` 绕过 GPU 0 只用 GPU 1 验证。是否继续？

---
