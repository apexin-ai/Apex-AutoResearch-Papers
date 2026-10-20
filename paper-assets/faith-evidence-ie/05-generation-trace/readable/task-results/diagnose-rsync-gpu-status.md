# diagnose rsync gpu status

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_rsync-gpu-status_20260520T082712_result.json`
- **Structured JSON:** [`e3d2e2969edd38654b49.json`](../../sessions/e3/e3d2e2969edd38654b49.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查结果

### rsync 状态
- **仍在运行**：monitor 日志显示 6 个 rsync 进程活跃
- **当前传输量**：`/root/autodl-tmp/` = **12GB**（3 分钟前是 10GB，增速 ~2GB/3min）
- **当前进度**：正在传输 `grpo_bf16_g4/checkpoint-200/adapter_model.safetensors`（~1GB 文件，最新进度 82%）

### nvidia-smi 完整输出

| GPU | 型号 | 显存占用 | GPU-Util | 温度 | 功耗 |
|-----|------|---------|----------|------|------|
| 0 | RTX PRO 6000 Blackwell | **0MiB** / 97887MiB | **0%** | 31°C | 35W |
| 1 | RTX PRO 6000 Blackwell | **0MiB** / 97887MiB | **0%** | 31°C | 34W |
| 2 | RTX PRO 6000 Blackwell | **0MiB** / 97887MiB | **100%** | 40°C | 102W |
| 3 | RTX PRO 6000 Blackwell | **0MiB** / 97887MiB | **100%** | 40°C | 104W |

### cuda:2 和 cuda:3 异常

**GPU-Util 100% 但无进程、无显存占用。** nvidia-smi 的 Processes 区域显示 "No running processes found"，compute apps 查询也为空。

这是一个**幽灵利用率**现象——可能原因：
1. 之前的进程异常退出但未正确释放 GPU 计算上下文（最常见）
2. 驱动级残留状态

解决方法：需要 `nvidia-smi --gpu-reset -i 2,3` 重置这两张卡，或者重启实例。在重置前这两张卡虽然显存可用，但可能行为异常。

### cuda:0 和 cuda:1
完全空闲，0MiB / 0% 利用率，可立即使用。

---
