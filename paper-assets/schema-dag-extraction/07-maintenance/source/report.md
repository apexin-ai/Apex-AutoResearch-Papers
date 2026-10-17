# Handover — 2026-05-23

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- prompt_sensitivity（准备中）
- prompt_sensitivity_dry4（准备中）
- prompt_sensitivity_dry3（准备中）
- prompt_sensitivity_dry2（准备中）
- prompt_sensitivity_dry（准备中）
- exp_aggregation_monte_carlo（准备中）
- exp_scs_name_def_ablation（准备中）
- exp_fewrel_contamination_check（准备中）
- exp017_gpt4o_mini_fewrel（准备中）
- exp_cross_embedding_sensitivity（准备中）
- …另有 2 项

## 近期结论
- **exp_fewshot_bcs_count16** (success): At count=16, the accuracy gap between low-BCS and high-BCS schema batches will widen as few-shot examples increase, consistent with count=8 pattern, because demonstrations reinforce distinguishable schemas more than confusable ones. ← 基于 exp_fewshot_bcs_v2
- **exp_llama70b_ner_bcs_null** (success): Batch-level BCS does not correlate with NER F1 for LLaMA-3.1-70B-FP8, consistent with the BCS null observed in Qwen3-32B (r=0.004) and LLaMA-8B (r=-0.12). The confusability metric is not predictive of extraction quality at the batch level. ← 基于 exp012_llama_8b_r2_exp2
  [LLaMA-70B NER BCS-null analysis](/api/workspace-files/projects/schema-dag-extraction/artifacts/exp_llama70b_ner_bcs_null/data/bcs_null_analysis.json)
- **exp_gemini_flash_bcs_controlled** (success): BCS-accuracy negative correlation observed on open-weight models (Qwen3-32B, LLaMA) generalizes to proprietary API models. Gemini 2.5 Flash should show significant BCS gap on extreme-BCS batches at count 8 and count 16, confirming Dimension 2 is architecture-family-independent. ← 基于 exp_gemini_flash_cross_model

## 趋势
成功 35 / 负向 9 / 失败 10 / 共 58

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
cqa1-38874: 无 GPU 信息
westd-24295: 无 GPU 信息

## 告警
- exp008_sdgd_zero_fewnerd: 训练失败 — unknown
- exp012_llama_fewnerd: 训练失败 — unknown
- exp012_llama_fewnerd_r2: 训练失败 — unknown
- exp012_llama_fewnerd_r3: 训练失败 — unknown
- exp012_llama_8b: 已被终止 — unknown
- exp_fewrel_40rel: 训练失败 — unknown
- exp012_llama_awq: 已被终止 — unknown
- exp012_llama_fewnerd_r4: 训练失败 — unknown
- exp012_llama_8b_fewnerd: 训练失败 — unknown
- exp_fewrel_40rel_r2: 训练失败 — unknown
- exp_fewrel_40rel_r3: 训练失败 — unknown
- exp012_llama_8b_r3: 训练失败 — unknown
- exp_fewrel_16rel_100batch: 已被终止 — unknown
- exp_fewshot_bcs_mitigation: 已被终止 — unknown
