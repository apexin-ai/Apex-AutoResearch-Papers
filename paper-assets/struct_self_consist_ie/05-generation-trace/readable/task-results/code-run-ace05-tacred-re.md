# code run ace05 tacred re

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_run_ace05_tacred_re_20260520T210436_result.json`
- **Structured JSON:** [`c990287b8e1ab09027b2.json`](../../sessions/c9/c990287b8e1ab09027b2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，结果已注册。

## 总结

**FewRel RE SC 诊断实验** 在 5090-c cuda:1 完成（5090-b 全部 GPU 被 32B 训练占用，改用 5090-c）。

### 关键结果

| 指标 | 值 |
|------|------|
| Greedy micro-F1 | **0.075** |
| Construction micro-F1 | **0.088** (+1.3pp) |
| Majority Vote F1 | 0.059 |
| Oracle F1 | 0.177 |
| Fleiss' κ | 0.151 |
| Degeneracy rate | 5.9% |
| Bootstrap p-value | **0.757**（不显著） |

### Failure Mode 分布
- **F2_low_agreement: 75.8%** — 绝大多数实例模型采样间缺乏一致性
- F3_high_agreement_low_quality: 15.2%
- F1_degeneracy: 5.9%
- F4_lp_quality_gap: 0.8%
- None: 2.3%

### 分析
结论标记为 **negative**：零样本 Qwen2.5-7B-Instruct 在 FewRel（16 类关系、Wikipedia 域）上绝对 F1 很低（~7.5%），SC construction 无法显著提升。75.8% 的 F2_low_agreement 表明模型在该任务上采样一致性极低，符合 SC 诊断预期——当 agreement 不足时，consensus 无法产生增益。

输出文件在 5090-c: `/root/autodl-tmp/struct_self_consist_ie/output/fewrel_re_sc/`

---
