# diag eval math500 sft standard 20 2048

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval_math500_sft_standard_20_2048_20260518T224914_result.json`
- **Structured JSON:** [`d19e3b591855f114f28d.json`](../../sessions/d1/d19e3b591855f114f28d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

根因已定位。

## 诊断报告

### 失败根因

**GPU 资源冲突**：eval 进程 (PID 33033) 在 cuda:2 上运行到 10/500 时，另一个 SFT 训练任务 (PID 34346) 于 06:42 在同一 cuda:2 上启动：

```
python src/sft_recovery.py --model_path .../pruned_standard_20 --output_dir .../sft_standard_20 --gpu 2
```

SFT 任务抢占了 51.5GB 显存，导致 eval 进程被直接杀死（日志无 traceback，说明是被 OOM killer/CUDA 内存不足直接终止）。

### 当前 GPU 状态

| GPU | 占用 | 进程 |
|-----|------|------|
| cuda:0 | 17.7GB | python (PID 32469) |
| cuda:1 | 19.3GB | python (PID 22049) |
| cuda:2 | 51.5GB | sft_recovery.py (PID 34346) |
| cuda:3 | 17.5GB | python (PID 21100) |

4 张 GPU 全部被占用。

### 环境/模型/脚本状态

- 模型路径完好（12GB safetensors）
- 评估脚本存在
- 数据集已缓存（网络不通但 cache 可用）
- 磁盘空间充足（数据盘 71GB 可用）

### 结论

- **可以直接重试**，脚本和模型无问题
- **前提**：等 cuda:2 上的 SFT 任务结束后再重跑，或改用其他空闲 GPU
- 无需修复代码，纯粹是 GPU 调度冲突

---
