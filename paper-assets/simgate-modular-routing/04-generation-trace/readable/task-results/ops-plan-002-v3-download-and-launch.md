# ops plan 002 v3 download and launch

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan-002-v3-download-and-launch_20260514T054223_result.json`
- **Structured JSON:** [`9275142c0b2cf7152120.json`](../../sessions/92/9275142c0b2cf7152120.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已成功启动，所有确认项均通过。

```
模型下载: 已存在, ~3.8GB (2个safetensors分片, tokenizer完整)
GPU0 状态: 空闲确认后启动（plan-004-implicit 刚结束释放）
训练启动: GPU0 占用 29801 MiB / 87% 利用率
日志确认:
  - 模型加载路径: /root/autodl-tmp/models/Qwen/Qwen3-1.7B (本地, 无网络请求)
  - class_weights: internal=3.929, deterministic=0.573
  - sampler: WeightedRandomSampler (upsample_minority enabled)
  - 数据: 2040 samples, 1650 train / 390 val, 156 steps/epoch
  - LoRA r=16, trainable 0.37%
  - WANDB offline, HF_HUB_OFFLINE=1
  - tmux session: plan-002-formal-v3
```

---
