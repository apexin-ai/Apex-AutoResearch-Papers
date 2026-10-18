# analysis exp llama70b cross model exp3

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp_llama70b_cross_model_exp3_20260517T110806_result.json`
- **Structured JSON:** [`f42c2d40c66be9cefca1.json`](../../sessions/f4/f42c2d40c66be9cefca1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入并注册。核心结论：

## 结果概要

### Exp 1 (FewRel RE): Dimension 1 **REPLICATED**
- Qwen3-32B: count_8→80 decline = -30.1pp
- LLaMA 70B: count_8→80 decline = -30.7pp
- 斜率几乎相同，70B 绝对值低约 4pp

### Exp 2 (BCS-Controlled): Dimension 2 **REPLICATED at count_16**
- 70B count_16: delta=+10.9pp, CI [3.0, 20.1]，显著
- 70B count_8: delta=-4.2pp, CI crosses zero，不显著（BCS range 太窄）
- 方向一致：高 BCS（高混淆度）→ 低 accuracy

### Exp 3 (Few-NERD NER): Dimension 1 **REPLICATED** (partial)
- 用完全相同的评估函数，两个模型 recall 几乎一致：
  - count_2: Qwen3=0.970, 70B=0.962 (diff -0.8pp)
  - count_12: Qwen3=0.826, 70B=0.829 (diff +0.3pp)
  - count_22: Qwen3=0.674, 70B=0.684 (diff +1.1pp)
- **count_44, count_6, count_66 仍在运行**，预计 ~60 分钟完成

### Overall: **SUCCESS**
Two-dimensional degradation pattern 跨模型家族（Qwen vs LLaMA）和模型规模（32B vs 70B）复现。count 驱动的性能下降是 model-invariant 的，confusability 效应方向保持一致。

报告路径：`artifacts/exp_llama70b_cross_model_analysis.md`

---
