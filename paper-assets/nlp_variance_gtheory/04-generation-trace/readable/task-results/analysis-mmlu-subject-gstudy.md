# analysis mmlu subject gstudy

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mmlu_subject_gstudy_20260522T201138_result.json`
- **Structured JSON:** [`69b314612d33c933464a.json`](../../sessions/69/69b314612d33c933464a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存。Summary table:

```
Subject                          item_id%  model:item%   G_item
================================================================================
abstract_algebra                    24.12        32.84   0.8221
clinical_knowledge                  47.45        30.02   0.9227
college_physics                     31.64        30.14   0.8762
computer_security                   37.03        24.90   0.9076
high_school_mathematics             10.37        41.88   0.6140
international_law                   44.35        24.11   0.9303
philosophy                          33.00        36.06   0.8680
professional_medicine               19.93        41.67   0.7781
us_foreign_policy                   20.43        36.94   0.8022
world_religions                     42.16        27.08   0.9097
--------------------------------------------------------------------------------
Mean                                31.05                0.8431
SD                                  12.12                0.0961
Full 200 items                       37.9                 0.896
```

关键发现：
- **item_id% 跨 subject 变异大**：CV=0.39，range 10.4%–47.5%。`high_school_mathematics` 最低（10.4%），`clinical_knowledge` 最高（47.5%）。
- **model:item_id% 与 item_id% 呈互补关系**：item_id% 低的 subject（hs_math, prof_medicine）model:item% 反而最高（~42%），说明这些 subject 的 item 难度差异小但模型间差异行为大。
- **G_item 9/10 subjects ≥ 0.78**，仅 `high_school_mathematics`（0.614）偏低——该 subject residual 占 38%，items 区分度不足。
- 全 200 items 的 item_id%=37.9 和 G_item=0.896 高于 subject-level 均值（31.05 / 0.843），因为 pooling 200 items 引入了跨 subject 难度差异，放大了 item 方差。

---
