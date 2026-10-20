# analysis registry s43s44 taxonomy

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_registry-__-s43s44-taxonomy_20260515T164613_result.json`
- **Structured JSON:** [`64be59546419be71f204.json`](../../sessions/64/64be59546419be71f204.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。总结如下：

## 完整 Taxonomy 分类结果

| | s42 (registry) | s43 (fresh) | s44 (fresh) |
|--|--|--|--|
| **PR** | 0.93 | 0.90 | 1.00 |
| **Mean ISR** | 0.1232 | 0.5308 | 0.002 |
| **H7** | 0 (0%) | 90 (100%) | 0 (0%) |
| **H1** | 81 (87.1%) | 0 (0%) | 85 (85%) |
| **H8** | 6 (6.5%) | 0 (0%) | 15 (15%) |
| **Genuine** | 7 (7.5%) | 0 (0%) | 3 (3%) |

## s44 genuine=3 调查

3 个样本 (folio_1296, folio_1428, folio_1051) 全部 ISR=0，是析取式结论逃过 H8 检测 + 交换律/全称实例化逃过 H1 文本匹配的边缘情况。**功能上退化，非真正推理。**

## 三 Seed Pooled 统计

- **Mean genuine_rate = 3.51% ± 3.78%**
- **与 D090 的 "1.0%±1.7%" 不一致**：主要差异来自 s42 的 genuine=7 (7.5%)。s42 可能需要用当前版本 classify_h7.py 重跑（其 H8 audit 是单独做的，不是同一批次管线）。

## Registry 更新

- s43: 补全了 h7_count/h7a_count/h7b_count/h1_count/h8_count/genuine_count + eval 详细字段 + checkpoint_path/log_path
- s44: 补全了 median_isr/proved_only_mean_isr/content_independent_count + genuine 审计注释 + checkpoint_path/log_path
- s44 taxonomy 数值与之前 registry 完全一致，无出入

---
