# ssh westd olmo d050 metrics

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_westd-olmo-d050-metrics_20260519T080034_result.json`
- **Structured JSON:** [`e9f19485fdceb66cc53f.json`](../../sessions/e9/e9f19485fdceb66cc53f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## OLMo-2-7B d050 训练最终指标

| 指标 | 值 |
|---|---|
| **train_loss** | 0.9733 |
| **mean_token_accuracy** | 0.7418 |
| **entropy** | 1.122 |
| **total steps** | 3642 |
| **epoch** | 1.0 |
| **runtime** | 7519s (2h 05m 19s) |
| **throughput** | 7.749 samples/s, 0.484 steps/s |
| **最终 step loss** | 0.8916 |
| **最终 step accuracy** | 0.7746 |
| **最终 step entropy** | 0.9642 |

**Adapter**: `/root/autodl-tmp/exp001/checkpoints/OLMo-2-7B_d050_s42/lora_adapter/adapter_model.safetensors` (152.5 MB), `.done` sentinel 已写入。

**GPU 状态**: cuda:0 空闲 (3MiB, 0%)。cuda:1/2/3 各有训练进程运行中。Phi-4 d100 未在 cuda:0 上启动。

---
