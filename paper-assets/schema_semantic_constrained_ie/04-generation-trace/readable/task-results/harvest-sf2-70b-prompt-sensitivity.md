# harvest sf2 70b prompt sensitivity

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_sf2_70b_prompt_sensitivity_20260523T112153_result.json`
- **Structured JSON:** [`1635212b848639e8cf1d.json`](../../sessions/16/1635212b848639e8cf1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 更新完成。总结如下：

## sf2_70b_prompt_sensitivity — 实验完成 (success)

**模型**: LLaMA-3.1-70B-Instruct-AWQ-INT4 | **数据**: SciERC test 551 samples | **服务器**: westd-21461

### 指标汇总

| Variant | E-F1 | R-F1 | ET% | RV% | DR% | CF% |
|---|---|---|---|---|---|---|
| minimal / constrained | 37.22 | 11.35 | 0.00 | 0.00 | **0.00** | 0.62 |
| minimal / unconstrained | 37.51 | 13.42 | 0.27 | 5.88 | 0.22 | 0.00 |
| detailed / constrained | 40.35 | 11.16 | 0.00 | 0.00 | **0.00** | 0.75 |
| detailed / unconstrained | 40.42 | 11.12 | 0.00 | 0.26 | **4.57** | 0.00 |

### 关键发现

1. **Constrained decoding 完全消除 ET/RV/DR violations**，无论 prompt 风格如何（两种 prompt 下均 0.00%），验证了假设
2. **Prompt 风格影响 extraction 质量**：detailed prompt 比 minimal 高 ~3pp E-F1（40.4 vs 37.4），但 R-F1 无显著差异（~11）
3. **Unconstrained + minimal prompt 导致格式漂移**：62/1395 relations 使用了嵌套 dict 格式（`head: {text, type}`）而非扁平格式，constrained grammar 避免了这个问题
4. **CF% 仅在 constrained 模式出现**（0.62-0.75%），unconstrained 为 0%——这是 grammar 允许同一 entity text 出现在多个 relation 中且被分配不同 type 导致的

### 产出路径
- 日志: `/tmp/prompt_sensitivity_70b.log`
- 输出: `/root/schema_semantic_constrained_ie/outputs/prompt_sensitivity_70b/` (4 个 JSONL)

---
