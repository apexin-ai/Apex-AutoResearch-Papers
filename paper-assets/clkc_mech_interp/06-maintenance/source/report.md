# Handover — 2026-05-26

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- gemma-steering-pickup（准备中）
- llama31_en_activations（准备中）
- qwen3_translate_zh（准备中）
- collect_en_activations_qwen3_8b（准备中）
- collect_en_activations_llama_v2（准备中）
- translate_zh_llama_v2（准备中）
- translate_zh_qwen（准备中）
- collect_en_act_llama_v3（准备中）
- collect_en_act_qwen_v2（准备中）
- verify_qwen3_v2（准备中）
- …另有 16 项

## 近期结论
- **steering_gemma_v2_L21_139** (negative): Gemma-2-9B-IT L21 (50% depth) probe direction causally influences conflict resolution when steering with matched-condition data (v2 pipeline, relabel bug fixed). Re-test with valid probe acc ~89% and N=171. Original L21 (steering_107_gemma_L21) used buggy data (N=158, probe acc 76.3%, 68% conflict samples had parametric==contextual due to relabel bug). ← 基于 steering_107_gemma_L21
- **steering_qwen_L15_135** (negative): Qwen3-8B-Instruct L15 (42% depth) probe direction causally influences conflict resolution with matched-condition data. L15 = L14 peak + 1, testing whether causal window extends one layer past the probe peak, analogous to Llama L13-L16 boundary. ← 基于 steering_107_qwen_L14
- **steering_qwen_L14_134** (negative): Qwen3-8B-Instruct L14 (39% depth) probe direction causally influences conflict resolution with matched-condition data. Original L14 had low probe acc (70%, N=84, best p=0.68). Depth matches Llama L13 (41%). Re-test with matched conditions to eliminate probe quality confound. ← 基于 steering_107_qwen_L14

## 趋势
成功 19 / 负向 23 / 失败 1 / 共 53
alpha_neg10_p: 0.458 ↓（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-14391: 空闲 cuda:0

## 告警
- comet_qwen_v5: 已被终止 — unknown
- comet_llama_v5: 已被终止 — unknown
- comet_qwen_v6: 已被终止 — unknown
- comet_llama_v6: 已被终止 — unknown
- gemma_full_pipeline_102: 训练失败 — unknown
- gemma_xnli_113: 已被终止 — unknown
- de_probe_n2000_112: 已被终止 — unknown
- de_bootstrap_parallel_114: 已被终止 — unknown
- steering_gemma_L16_130: 已被终止 — unknown
- steering_gemma_L17_131: 已被终止 — unknown
- steering_gemma_L18_132: 已被终止 — unknown
