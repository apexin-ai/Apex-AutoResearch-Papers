# research d032 verify v2

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_d032-verify-v2_20260514T112904_result.json`
- **Structured JSON:** [`783d7cdae2d2ad968186.json`](../../sessions/78/783d7cdae2d2ad968186.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部数据收集完毕。结论如下：

---

## D032 核实结果

### Q1: v5 是否用了 WeightedTrainer?

**YES**。v5 的 `train_config.json` 明确设置 `upsample_minority: true`，代码路径与 ablation-b 完全一致——`implicit_router_sft.py` 在 `upsample_minority=true` 时始终创建 `WeightedRandomSampler` 并传入 `WeightedTrainer`。

证据：v5 步数 1305 / 3 epochs = 435 步/epoch，与 `ceil(~1740/4)` 一致（WeightedRandomSampler draws N samples/epoch），排除了普通 Trainer 的可能。

### Q2: 代码是否有变更?

**无法通过 git 验证**（服务器和本地均无 git 仓库）。但两次训练都用 `src/training/implicit_router_sft.py`，同一代码路径，日志格式一致。

### Q3: 完整配置差异

| 参数 | ablation-b | v5 | 差异? |
|------|-----------|-----|------|
| gradient_accumulation_steps | **8** | **1** | **YES** |
| effective batch size | **32** (4×8) | **4** (4×1) | **8× 差异** |
| per_device_train_batch_size | 4 | 4 | - |
| upsample_minority | true | true | - |
| class_weights | (absent) | null | 等价 |
| lr | 2e-5 | 2e-5 | - |
| epochs | 3 | 3 | - |
| warmup_ratio | 0.1 | 0.1 | - |
| seed | 42 | 42 | - |
| max_seq_len | 2048 | 2048 | - |
| lora_r / alpha / dropout | 16/32/0.05 | 16/32/0.05 | - |
| max_steps | 165 (55/epoch) | 1305 (435/epoch) | 由 ga 导致 |
| total_flos | 6.45e15 | 6.55e15 | ~一致 |
| data_dir | data/plan-004-implicit | data/plan-004-implicit/ | 等价 |

**注意**：ablation-b 的 `train_config.json` 缺少 `gradient_accumulation_steps` 字段（保存代码的 bug），但 `training_args.bin` 明确记录 ga=8。

### 根因结论

ablation-b（internal_recall=51.5%）与 v5（26.7%）的**唯一实质差异是 effective batch size：32 vs 4**。

两者都用了 WeightedRandomSampler 做 50/50 类别平衡采样。但 effective batch size 4 时，每个优化步仅 ~2 internal + ~2 deterministic 样本，梯度噪声极大，模型无法稳定学习少数类（internal，仅占原始分布 10.4%）的路由信号。ga=8 将 effective batch 提升到 32，每步 ~16 internal 样本，梯度稳定，minority class 学习成功。

---
