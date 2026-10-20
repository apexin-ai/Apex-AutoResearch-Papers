# Deep Error Analysis Framework (plan_021)

## 可用数据（27个eval目录有predictions.json）

核心多尺度对比组（dev split, 985 docs）：

| 条件 | Qwen3-1.7B | Qwen3-8B | Llama-3.1-8B |
|------|-----------|----------|-------------|
| SFT | qwen3_1_7b_sft_eval (F1=.495) | qwen3_8b_sft_eval (F1=.526) | llama_3_1_8b_sft_eval (F1=.551) |
| No-Evidence | qwen3_1_7b_no_evidence_eval_v3 (F1=.410) | qwen3_8b_no_evidence_eval_v2 (F1=.528) | llama_3_1_8b_no_evidence_eval (F1=.562) |
| RSFT | plan_006_qwen3_1_7b_rsft_eval_r2 (F1=.522) | plan_006_qwen3_8b_rsft_eval (F1=.561) | plan_006_llama_rsft_r3_eval (F1=.567) |
| d102(k=1) | d102_1_7b_k1_s42 (F1=.529) | d102_8b_k1_s42 (F1=.555) | d102_llama_k1_s42 (F1=.584) |

## Error分类体系

### FP: 幻觉关系 / 关系混淆 / 实体混淆 / 重复预测
### FN: 跨句遗漏 / 稀有关系遗漏 / 截断丢失 / 实体不识别
### Evidence: 过泛引用 / 证据偏移 / 证据不全

## 分析优先级
- P0: 3尺度×{SFT,RSFT} FP/FN对比 + Evidence error分类
- P1: 截断影响量化 + 跨句vs单句F1 + d102 vs RSFT
- P2: Qualitative case study扩展 + No-evidence FP分析

## 现有代码
- eval/evaluator.py, scripts/edcr_diagnostic.py, eval/cross_method_table.py
- 需要新写 error_analysis.py

所有P0/P1分析可用现有dev predictions完成，无需重新推理。