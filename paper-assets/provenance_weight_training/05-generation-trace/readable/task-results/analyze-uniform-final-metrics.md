# analyze uniform final metrics

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_uniform-final-metrics_20260514T024819_result.json`
- **Structured JSON:** [`f45ace67b21b6fa1c720.json`](../../sessions/f4/f45ace67b21b6fa1c720.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 个 uniform 实验全部正常完成。汇总：

| 实验 | train_loss | 总 steps | 训练时长 | 状态 |
|------|-----------|----------|----------|------|
| uniform_seed42 | **7.3104** | 6103 | 3h19m (11946s) | 正常完成 (EXIT_CODE=0) |
| uniform_seed123 | **7.3121** | 6103 | 3h20m (11994s) | 正常完成 (EXIT_CODE=0) |
| uniform_seed456 | **7.2895** | 6103 | 3h20m (11974s) | 正常完成 (EXIT_CODE=0) |

**均值 train_loss = 7.3040, 标准差 = 0.0124**

Checkpoint 完整性：
- 每个实验均有 `checkpoint-6000`、`checkpoint-6103`、`final` 三个目录
- final 目录均为 **1.2GB**，包含完整的 `model.safetensors`（1.2G）、tokenizer 文件、config 等
- 路径：`/root/provenance_weight_training/output/models/uniform_seed{42,123,456}/final/`

---
