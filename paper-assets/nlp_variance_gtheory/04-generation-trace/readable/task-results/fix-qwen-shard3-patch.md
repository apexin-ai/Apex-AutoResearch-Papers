# fix qwen shard3 patch

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_qwen_shard3_patch_20260521T070049_result.json`
- **Structured JSON:** [`0c9d331e42d6c3a2c151.json`](../../sessions/0c/0c9d331e42d6c3a2c151.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### 1. 缺失的 69 condition IDs
```
[9, 17, 18, 20, 27, 36, 38, 39, 54, 104, 128, 151, 152, 153, 155, 158, 161, 176, 181, 191, 
 208, 226, 230, 246, 254, 256, 263, 284, 288, 302, 321, 323, 346, 404, 408, 878, 881, 897, 
 914, 957, 960, 993, 1015, 1020, 1046, 1061, 1075, 1085, 1089, 1090, 1103, 1116, 1121, 1135, 
 1150, 1160, 1178, 1187, 1192, 1214, 1222, 1226, 1228, 1261, 1267, 1273, 1275, 1285, 1286]
```

### 2. 补跑 PID
- PID: 106052（已完成）

### 3. 各 shard 行数
| Shard | 行数 |
|-------|------|
| shard_0 | 64,800 |
| shard_1 | 64,800 |
| shard_2 | 64,800 |
| shard_3 | 64,800 |
| **总计** | **259,200** |

shard_3 验证：324 unique conditions, 64,800 records。全量 4 shards 通过 assert 验证。

### 4. 最终统计
- **Accuracy**: 0.7252
- **Precision 分布**: bfloat16=100,200 / float16=79,600 / float32=79,400
- **Unique conditions**: 1,227

---
