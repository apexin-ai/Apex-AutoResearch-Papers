# code fix s42 gap

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_s42_gap_20260514T151836_result.json`
- **Structured JSON:** [`d855e3fc9afceb58e6da.json`](../../sessions/d8/d855e3fc9afceb58e6da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部检查完成。汇报如下：

---

## 汇报

### 缺失 Runs

| 编码器 | 缺失 | 已完成 s42 |
|--------|------|-----------|
| Qwen | embedding_distance_s42, dataflow_aware_s42 | random_s42 ✅ (3 epochs) |
| StarCoder | embedding_distance_s42, dataflow_aware_s42 | random_s42 运行中 (3 epochs, step 3800/~4215) |

### 训练数据

全部就绪，每个文件 11308 行：
- Qwen: `full_m2_training_data/train_{embedding_distance,dataflow_aware}_s42.jsonl` + 对应 val
- StarCoder: `full_m2_starcoder_data/train_{embedding_distance,dataflow_aware}_s42.jsonl` + 对应 val
- 两个 `dataflow_graph.json` 均存在

### 补充脚本 `/root/structfuse/run_m2_s42_supplement.sh`

- 语法验证通过
- 覆盖: embedding_distance_s42 + dataflow_aware_s42
- 参数与 random_s42 完全一致: **3 epochs, 无 early stopping**, lr=2e-5, batch=8, num_neg=7, temp=0.07, max_seq=2048, LoRA, gradient checkpointing
- 支持 `--encoder qwen|starcoder|both` 和 `--gpu cuda:N`
- 不设置 CUDA_VISIBLE_DEVICES（由框架注入）

### 当前执行队列

**cuda:0** — Qwen `run_m2_full_qwen.sh` (SEEDS=43,44):
```
random_s43 ← 运行中 (step 1000/~2810, epoch 1/2)
→ random_s44 → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s43 → dataflow_aware_s44
```

**cuda:1** — StarCoder random_s42 单独进程:
```
random_s42 ← 运行中 (step 3800/~4215, epoch 3/3, 快完成)
→ [完成后自动启动 run_m2_full_starcoder_s43plus.sh]:
  random_s43 → random_s44 → embedding_distance_s43 → embedding_distance_s44 → dataflow_aware_s43 → dataflow_aware_s44
```

**不会冲突** — 补充脚本未启动，现有队列不包含 s42 的 embedding_distance / dataflow_aware。

### 建议执行计划

每个 2-epoch run 约 11h (Qwen) / 16h (StarCoder)。3-epoch s42 supplement run 约 17h (Qwen) / 23h (StarCoder)。

| 时间 | 事件 | 动作 |
|------|------|------|
| ~May 15 01:40 | StarCoder random_s42 完成 | s43+ 自动启动 |
| ~May 17 13:30 | Qwen s43+s44 全部完成 | cuda:0 空闲, 启动 `--encoder qwen` |
| ~May 18 22:40 | StarCoder s43+s44 全部完成 | cuda:1 空闲, 启动 `--encoder starcoder` |

或分别链式启动：Qwen s43+ 完成后自动接 supplement qwen, StarCoder s43+ 完成后自动接 supplement starcoder，无需手动介入。

---
