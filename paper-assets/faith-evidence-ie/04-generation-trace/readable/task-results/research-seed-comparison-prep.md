# research seed comparison prep

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_seed-comparison-prep_20260516T052633_result.json`
- **Structured JSON:** [`3e993e45ed942e9ae835.json`](../../sessions/3e/3e993e45ed942e9ae835.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 验证结果

### seed_comparison.py 路径配置：**正确，无需修改**

脚本 METHODS dict 已指向正确的 8 个目录。

### 8 个目录状态

| Slot | 目录 | 存在 | metrics_v2.json | 状态 |
|------|------|------|-----------------|------|
| CED s42 | `rsft_ced_s42_reeval` | ✓ | **无（空目录）** | re-eval 进行中 |
| CED s43 | `rsft_ced_s43` | ✓ | ✓ f1=0.4601, ign_f1=0.4512 | **完成** |
| CED s44 | `rsft_ced_s44_reeval` | ✓ | **无（空目录）** | re-eval 进行中 |
| CED s45 | `rsft_ced_s45` | ✓ | ✓ | **完成** |
| flatNLI s42 | `rsft_flat_nli_s42_reeval` | ✓ | **无（空目录）** | re-eval 进行中 |
| flatNLI s43 | `rsft_flat_nli_s43_reeval_r2` | ✓ | **无（空目录）** | re-eval 进行中 |
| flatNLI s44 | `rsft_flat_nli_s44` | ✓ | ✓ f1=0.4615, ign_f1=0.4521 | **完成** |
| flatNLI s45 | `rsft_flat_nli_s45` | ✓ | ✓ | **完成** |

### 指标读取验证

脚本 `load_metrics()` 优先读 `metrics_v2.json`，`METRICS_KEYS` 包含 `ign_f1` 和 `f1`（即 rel_f1）。已确认已完成的 metrics_v2.json 中这两个字段均存在且有效。

### 结论

- 脚本配置正确，**不需要修改**
- 4/8 已完成（CED s43、CED s45、flatNLI s44、flatNLI s45）
- 4/8 re-eval 进行中（CED s42、CED s44、flatNLI s42、flatNLI s43），目录已创建但尚无输出

---
