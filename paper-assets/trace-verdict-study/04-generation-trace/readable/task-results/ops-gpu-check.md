# ops gpu check

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu-check_20260515T214502_result.json`
- **Structured JSON:** [`bdcf71228e478d8a543f.json`](../../sessions/bd/bdcf71228e478d8a543f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**无 GPU 冲突。** 结果如下：

### GPU 显存使用

| GPU | 型号 | 显存占用 | 温度 | 利用率 |
|-----|------|---------|------|--------|
| GPU 0 | RTX PRO 6000 Black (96GB) | 71,595 / 97,887 MiB (73%) | 71°C | 100% |
| GPU 1 | RTX PRO 6000 Black (96GB) | 22,395 / 97,887 MiB (23%) | 72°C | 100% |

### 进程 → GPU 映射

| PID | 实验 | `--gpu` 参数 | `CUDA_VISIBLE_DEVICES` | 物理 GPU | 运行时间 |
|-----|------|-------------|----------------------|----------|---------|
| 160932 | `deepseek_exception_only_seed456` | 0 | **0** | GPU 0 | 1h22m |
| 163109 | `deepseek_full_trace_seed42_v3` | 0 | **1** | GPU 1 | 47m |

### 结论

虽然两个进程的命令行都写了 `--gpu 0`，但它们的 `CUDA_VISIBLE_DEVICES` 环境变量分别设为 `0` 和 `1`，所以实际各用一张物理 GPU，**不存在冲突**。`--gpu 0` 指的是 `CUDA_VISIBLE_DEVICES` 范围内的第 0 张卡，由于环境变量已做隔离，两个进程互不干扰。

两个实验都在满负载运行（GPU-Util 100%），状态正常。

---
