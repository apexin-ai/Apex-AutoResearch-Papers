# analysis deepseek cls repo v5 ckpt6315 eval

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deepseek-cls-repo-v5-ckpt6315-eval_20260518T215327_result.json`
- **Structured JSON:** [`9f1103265a04e0190f7b.json`](../../sessions/9f/9f1103265a04e0190f7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成，报告已写入 `artifacts/ckpt6315_eval_analysis.md`。核心发现：

**ckpt-6315 (epoch 3) vs ckpt-2105 (epoch 1):**

| 指标 | ep3 | ep1 | Delta |
|---|---|---|---|
| accuracy | 82.51% | 82.61% | -0.10pp |
| fail_recall | **38.47%** | 51.02% | **-12.55pp** |
| f1_macro | 71.76 | 75.07 | -3.31 |
| pass_recall | 98.84% | 94.33% | +4.51pp |
| unparseable | 0 | 0 | -- |

**关键判断：**

1. **Hypothesis 成立** — epoch 3 accuracy 略低于 epoch 1，但真正的退化在 fail_recall (-12.55pp) 和 f1_macro (-3.31)
2. **Variant 级别 decision collapse 确认** — fail variant 0/3 全部判错，模型对每个 fail task 的多数票都投给了 pass
3. **Instance 级别** — fail 预测占 11.2%（实际 fail 占 27%），正在滑向 collapse
4. **ckpt-2105 仍是最优 checkpoint**
5. **需排查**: variant 总数差异 (25 vs 48)，两次 eval 的 problem_id 集合不一致，variant_accuracy 不可直比

---
