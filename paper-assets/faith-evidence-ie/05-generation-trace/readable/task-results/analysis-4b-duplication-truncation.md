# analysis 4b duplication truncation

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_4b_duplication_truncation_20260518T133445_result.json`
- **Structured JSON:** [`8867dc2909f394306d64.json`](../../sessions/88/8867dc2909f394306d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，artifact 已注册 (`art_20260518_c36f7f`)。核心结果总结：

### 1. Duplication Rate (Table 2 补充)
| Model | Condition | Raw | Unique | Dup rate | Docs w/dups |
|-------|-----------|-----|--------|----------|-------------|
| 4B | With-Evi | 16,880 | 11,626 | 31.1% | N/A* |
| 4B | No-Evi | 21,181 | 12,025 | 43.2% | 345 |

*with-evi 无 predictions.json，从 metrics 的 n_predictions vs pred_count 计算。

### 2. Truncation Crossover (Table 3.2)
4B with-evidence 缺 per-doc predictions.json，仅有聚合数据：
- With-evi truncated: 288/985 (29.2%)
- No-evi truncated: 307/985 (31.2%)

**需要重跑 4B with-evidence eval 并保存 predictions.json 才能做完整 crossover 分析。**

### 3. Doc Complexity (4B No-Evidence)
| Bin | Docs | Truncated | Rate |
|-----|------|-----------|------|
| 0-5 | 154 | 15 | 9.7% |
| 6-10 | 323 | 52 | 16.1% |
| 11-20 | 370 | 154 | 41.6% |
| 21+ | 138 | 86 | 62.3% |

### 4. Capacity Valley 验证
**4B 的 evidence tax (+7.47pp) 是所有模型中最高的**，完美符合 capacity valley 叙事：
- 1.7B: -8.04pp（evidence 起正则化作用，防止退化）
- **4B: +7.47pp**（evidence 是纯开销，容量不够但不至于退化）
- 8B: +0.28pp（容量充足，evidence 影响微乎其微）

### 5. Config 修正
确认 1.7B eval 的 `base_model` 字段误写为 `Qwen3-4B`，`model_path` 正确是 `Qwen3-1.7B`（仅元数据错误，不影响实际推理）。

---
