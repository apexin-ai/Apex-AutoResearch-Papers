# code fix mix bidirectional

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-mix-bidirectional_20260514T181557_result.json`
- **Structured JSON:** [`cfad0bbe0928ee4f2834.json`](../../sessions/cf/cfad0bbe0928ee4f2834.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

14/14 全部通过。

### 修改内容

**`iterative_train.py` — `mix_datasets` 函数**：改为双向 subsample 逻辑
- `needed_syn <= len(synthetic)` → 低 α 路径：保全 real，subsample synthetic
- 否则 → 高 α 路径：保全 synthetic，subsample real 到 `int(len(syn) * (1-ratio) / ratio)`

**`test_alpha_sweep.py`**：14 个测试全部通过

| 测试 | ratio | 实际比例 | 路径 |
|------|-------|---------|------|
| ratio=1.0 | 1.00 | pure syn | 边界 |
| ratio=0.0 | 0.00 | pure real | 边界 |
| ratio=0.50 | 0.50 | 0.500 | 低 α |
| ratio=0.25 | 0.25 | 0.249 | 低 α |
| ratio=0.90 | 0.90 | 0.900 | 低 α |
| ratio=0.25 precise | 0.25 | 0.242 | 低 α |
| **ratio=0.75 precise** | **0.75** | **0.758** | **高 α** |
| **ratio=0.90 precise** | **0.90** | **0.901** | **高 α** |
| ratio=0.50 balanced | 0.50 | 0.500 | 低 α |
| accumulate stability | 0.50 | 0.500 ×3 | 低 α |
| accumulate high α | 0.50 | 0.500 ×3 | 高 α |
| no-accumulate | 0.50 | 0.500 ×3 | 高 α |
| determinism | 0.50 | — | — |
| **sweep 全覆盖** | 0→1.0 | 全部误差 <0.05 | 双向 |

之前 ratio=0.75 被截断到 0.50、ratio=0.90 被截断的问题已修复。

---
