# check mlp param counts

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_mlp_param_counts_20260514T170657_result.json`
- **Structured JSON:** [`92409d6bc4f5f03f7d7a.json`](../../sessions/92/92409d6bc4f5f03f7d7a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All four configs retrieved. Here's the analysis:

## 1. per_layer_intermediate_size 完整列表

| Layer | standard_20 | rasp_20 | standard_25 | rasp_25 |
|------:|------------:|--------:|------------:|--------:|
| 0 | 8128 | 8128 | 8128 | 8128 |
| 1 | 8128 | 8128 | 8128 | 8128 |
| 2 | 8128 | 8128 | 8128 | 8128 |
| 3 | 8128 | 8128 | 8128 | 8128 |
| 4 | 8128 | 8128 | 8128 | 8128 |
| 5 | 8128 | 8128 | 8128 | 8128 |
| 6 | **18944** | **8128** | **18944** | **8128** |
| 7 | 18944 | 18944 | 18944 | 18944 |
| 8 | 18944 | **18268** | 18944 | **12184** |
| 9 | 18944 | **16240** | 18944 | **15564** |
| 10 | 18944 | 18944 | 18944 | 18944 |
| 11 | 18944 | 18944 | 18944 | 18944 |
| 12 | 18944 | 18944 | 18944 | 18944 |
| 13 | 18944 | 18944 | 18944 | 18944 |
| 14 | 18944 | 18944 | 18944 | 18944 |
| 15 | 18944 | 18944 | **16916** | 18944 |
| 16 | **14212** | **18944** | **8128** | **17592** |
| 17 | **16240** | **18944** | **10156** | **17592** |
| 18 | **14212** | **18944** | **8128** | **14212** |
| 19 | 8128 | **9480** | 8128 | 8128 |
| 20 | **17592** | **18944** | **10832** | **12184** |
| 21 | 13536 | 13536 | **10832** | **8128** |
| 22 | **16240** | **18944** | **13536** | **16916** |
| 23 | 8128 | 8128 | 8128 | 8128 |
| 24 | 8128 | 8128 | 8128 | 8128 |
| 25 | **8128** | **11508** | 8128 | 8128 |
| 26 | **13536** | **17592** | **11508** | **16916** |
| 27 | **18944** | **8128** | 18944 | **8128** |

## 2. Sum 比较

| Model | Sum | 占原始比 (原始=18944×28=530432) |
|-------|-----|------|
| **standard_20** | **395232** | 74.5% (剪了 25.5%) |
| **rasp_20** | **395232** | 74.5% (剪了 25.5%) |
| **standard_25** | **360756** | 68.0% (剪了 32.0%) |
| **rasp_25** | **361432** | 68.1% (剪了 31.9%) |

- **20% 模型：sum 完全相同（395232）**
- **25% 模型：rasp 比 standard 多 676（差 0.19%），不完全相同**

## 3. 各层差异

**20% 模型**：12/28 层不同（层 6, 8, 9, 16, 17, 18, 19, 20, 22, 25, 26, 27）
- 最大差异在层 6 和 27：standard 保留 18944，rasp 缩到 8128（差 10816）
- RASP 在中间层（16-18）保留更多容量，在首尾层（6, 27）剪得更狠
- 净差 = 0（预算完全守恒）

**25% 模型**：13/28 层不同（层 6, 8, 9, 15, 16, 17, 18, 20, 21, 22, 26, 27）
- 同样的模式：RASP 保中间层、剪首尾
- 净差 = +676（rasp 略多，预算未严格守恒）

## 4. Attention heads

两组模型的 attention 结构完全相同：`num_attention_heads=28`, `num_key_value_heads=4`，无 per-layer attention head 差异。config 中无 `per_layer_num_attention_heads` 或 `per_layer_num_key_value_heads` 字段——剪枝仅作用于 MLP intermediate size。

---
