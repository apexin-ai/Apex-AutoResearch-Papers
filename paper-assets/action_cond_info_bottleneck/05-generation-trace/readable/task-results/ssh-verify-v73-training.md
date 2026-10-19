# ssh verify v73 training

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_verify_v73_training_20260517T225549_result.json`
- **Structured JSON:** [`2a45f48d87d2dda9ca69.json`](../../sessions/2a/2a45f48d87d2dda9ca69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### 1. GPU 占用
| GPU | PID | 显存 | 利用率 |
|-----|-----|------|--------|
| 0 | 745668 | 15276MiB / 97887MiB | 99% |
| 1 | 745746 | 13550MiB / 97887MiB | 94% |

### 2. 训练日志（最后 10 行）

**v7.3 Connector+LoRA** — 仍在初始化阶段，显示配置信息：
```
[FREEZE-MODE] connector_lora
Steps: 20000, Batch size: 64, Device: cuda:0, dtype: bfloat16
alpha=0.01, beta=0.01, diversity_lambda=0.1, lambda_contrastive=0.1
```

**Connector-only ablation** — 同样处于初始化阶段：
```
[FREEZE-MODE] connector_only
Steps: 20000, Batch size: 64, Device: cuda:0, dtype: bfloat16
alpha=0.01, beta=0.01, diversity_lambda=0.0, lambda_contrastive=0.0
```

### 3. 进程状态
- PID 747024: `train_acib.py --freeze_mode connector_lora` (22.8% CPU, 活跃)
- PID 747115-747118: `train_acib.py --freeze_mode connector_only` (37-38% CPU each, 活跃，含 DataLoader workers)

### 4. 判断：训练正在正常启动中 — **是**

两个训练均已成功启动，进程存活，GPU 占用正常（99%/94%）。当前处于模型加载/数据预处理阶段（启动约 1 分钟），尚未输出 training step。这是正常行为，预计再等 1-2 分钟即可看到 step 输出。无错误信息。

---
