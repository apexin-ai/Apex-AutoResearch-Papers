# code evi f1 joint impl

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_evi_f1_joint_impl_20260515T131621_result.json`
- **Structured JSON:** [`b2e8ed865923c5a32e8a.json`](../../sessions/b2/b2e8ed865923c5a32e8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果如下：

```
Experiment        evi_f1_cond  evi_f1_joint    delta  joint_P  joint_R  evi_tp  pred_tot  gold_tot
---------------------------------------------------------------------------------------------------------
SFT baseline           0.7979        0.3117  -0.4862   0.3037   0.3200    6164     20294     19261
RSFT r1                0.8187        0.3468  -0.4719   0.3515   0.3423    6593     18759     19261
RSFT r2a               0.8108        0.3509  -0.4599   0.3423   0.3599    6932     20251     19261
RSFT r2b               0.8128        0.3490  -0.4638   0.3455   0.3526    6791     19653     19261
RSFT s44               0.8087        0.3713  -0.4374   0.3775   0.3653    7037     18640     19261
```

**关键发现：**
- Joint evi_f1 在 0.31–0.37 范围，远低于 conditional 的 0.80–0.82，与 DREEAM 报告的 ~57% 量级更接近（我们的模型 RE F1 本身只有 ~0.45，大量 FP/FN triple 拉低了 evidence 指标）
- RSFT s44 仍是最优（0.3713），排序不变
- FP triples 贡献了大量 pred_total（SFT baseline 20294 vs gold 19261），FN triples 同样拉高了 gold_total 分母

`compute_evi_f1_joint()` 已添加到 `/root/autodl-tmp/freige/eval/evaluator.py`，不影响现有 `compute_evi_f1()`。对比结果保存在 `/root/autodl-tmp/eval_results/evi_f1_joint_comparison.json`。

---
