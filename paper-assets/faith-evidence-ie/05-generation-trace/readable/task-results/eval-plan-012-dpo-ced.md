# eval plan 012 dpo ced

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_plan_012_dpo_ced_20260515T174106_result.json`
- **Structured JSON:** [`9623e605e3384ae85a79.json`](../../sessions/96/9623e605e3384ae85a79.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Plan 012 DPO + CED Eval 结果

**Conclusion: NEGATIVE**

| Metric | DPO CED | SFT baseline | RSFT CED | bf16 GRPO G=8 | QLoRA GRPO |
|--------|---------|-------------|----------|---------------|------------|
| **rel_f1** | **0.3429** | 0.4057 | 0.4596 | 0.4549 | 0.2167 |
| evi_f1 | 0.8403 | — | — | — | — |
| edcr | 0.7294 | — | — | — | — |
| format_ok | 99.5% | — | — | — | — |

关键发现：

- **rel_f1=0.3429 低于 SFT 基线 0.4057**，相对下降 15.5%。DPO 训练损害了关系抽取性能。
- 训练时 rewards/accuracies=1.0、margins=9.01，模型完美区分了 chosen/rejected，但这个信号没有迁移到推理阶段——典型的 DPO 过拟合：preference pairs 太容易区分（top-1 vs bottom-1 差距过大）。
- 证据质量保持良好（evi_f1=0.8403, edcr=0.7294），说明 CED preference 在证据引用维度上是有效的，但关系抽取准确率反而退化。
- 优于 QLoRA GRPO（0.2167），但这个基线本身就是失败的。

**结论：离线 DPO + CED preference pairs 不能替代在线 GRPO。** 如果要继续探索 DPO 方向，需要使用更难区分的 preference pairs（如 top-1 vs mid-ranked）、减少训练轮数、或换用 IPO/KTO。

报告已注册：`art_20260515_b15af8`

---
