# audit gru architecture consistency

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_gru-architecture-consistency_20260519T085201_result.json`
- **Structured JSON:** [`ea88f0df1c9d36bb606c.json`](../../sessions/ea/ea88f0df1c9d36bb606c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GRU 架构一致性审计

### 代码默认参数
- `GRUClassifier` 默认 `hidden_dim=256`, `num_layers=2`, `dropout=0.3`
- 所有训练脚本（`train_classifier.py`, `train_classifier_binary.py`, `train_baseline_gru.py`, `run_plan_002.sh`, `exp15_roberta_large.py` 等）均使用 `hidden_dim=256, num_layers=2`
- MLP 结构: `512→256→2`（BiGRU 输出 256×2=512 → Linear(512,256) → ReLU → Linear(256,2)）

### Checkpoint 验证结果（全部一致）

| Checkpoint | input_dim | hidden_dim | num_layers | MLP |
|-----------|----------|-----------|-----------|-----|
| plan_002 (treat/base/s123/s456) | 768 | 256 | 2 | 512→256→2 |
| plan_003_scrambled_fix | 768 | 256 | 2 | 512→256→2 |
| mf1_binary_seed42 | 768 | 256 | 2 | 512→256→2 |
| plan_016v2_topic | 768 | 256 | 2 | 512→256→2 |
| plan_017_mlm | 768 | 256 | 2 | 512→256→2 |
| plan_018_wiki_mlm | 768 | 256 | 2 | 512→256→2 |
| exp1_roberta_vanilla_seed42 | 768 | 256 | 2 | 512→256→2 |
| exp1_roberta_9class_seed42 | 768 | 256 | 2 | 512→256→2 |
| exp15_roberta_large_vanilla_seed42 | **1024** | 256 | 2 | 512→256→2 |
| exp15_roberta_large_9class_seed42 | **1024** | 256 | 2 | 512→256→2 |
| vanilla_seed123 | 768 | 256 | 2 | 512→256→2 |

### 结论

**情况 A：所有实验 GRU 参数完全一致。** hidden_dim=256, num_layers=2, MLP=512→256→2。

exp15 唯一的区别是 `input_dim=1024`（因为 RoBERTa-large embedding 是 1024 维），GRU 本身参数不变。

**论文描述有误**：论文写的 "hidden dimension 128, MLP 256→64→2" 与实际不符。实际是 **hidden dimension 256, MLP 512→256→2**。需要修正论文中的架构描述。

---
