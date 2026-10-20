# Handover — 2026-05-23

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
（无）

## 近期结论
- **r16_70b_lora_scierc_eval** (success): 70B AWQ INT4 LoRA fine-tuned on SciERC will achieve higher R-F1 than 8B FT (Qwen 47.15, Llama 46.13) and S1 constraints will maintain DR→0% at 70B scale
- **p1_llama_ee_ft** (killed): —
- **sf2_70b_prompt_sensitivity** (success): 70B LLaMA-3.1 constrained decoding should show consistent violation reduction across different prompt styles, similar to the 8B result where ΔDR was 94.0-94.6% regardless of prompt variant.

## 趋势
成功 133 / 负向 15 / 失败 11 / 共 164

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-16980: 无 GPU 信息
westd-21461: 空闲 cuda:0, cuda:1

## 告警
- mvp_phase0_docred_schema_r2: 已被终止 — unknown
- w1_cf_fallback_docred: 已被终止 — unknown
- w1_cf_fallback_llama_scierc: 已被终止 — unknown
- w1_cf_fallback_llama_docred: 已被终止 — unknown
- w9_qwen_docred_zs_sampling: 训练失败 — unknown
- p8b_docred_latency: 训练失败 — unknown
- p1_ee_ft_composability: 训练失败 — unknown
- p1_ee_ft_composability_r2: 训练失败 — unknown
- p1_ee_ft_composability_r3: 训练失败 — unknown
- p1_ee_ft_composability_r4: 训练失败 — unknown
- p1_ee_ft_llama: 训练失败 — unknown
- p1_llama_ee_ft: 已被终止 — unknown
- d064_docred_full_beam: 训练失败 — unknown
- d066_docred_beam_sweep: 训练失败 — unknown
- d065_qwen_greedy_4096: 训练失败 — unknown
- d066_sweep_llama_scierc_beam1_unc: 训练失败 — unknown
