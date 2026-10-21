# Handover — 2026-05-26

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- exp-rebuttal-mia-grpo: Min-K% and Min-K%++ MIA methods will fail on GRPO-contaminated Llama (AUC near 0.5), while lz* retains detection power, demonstrating lz* advantage over logit-based MIA for RL-trained models（排队等待 GPU）
- exp-rebuttal-llama-5pct: Llama at 5% contamination produces detectable lz* shift, extending dose-response coverage for rebuttal. Existing exp-ctrl-contam-llama-5pct may already have results.（准备中）
- exp-rebuttal-mistral-25pct: Mistral at 25% contamination will show intermediate lz* shift between 15% and 50%, confirming monotonic dose-response for rebuttal defense（准备中）
- exp-rebuttal-mistral-5pct: Mistral at 5% contamination will produce detectable lz* shift (|d|>0.8), completing the 4-point dose-response curve for rebuttal defense of dose-response generalizability（准备中）
- exp-mistral-5pct-s2: Mistral-7B-v0.3 5% MMLU contamination with seed=123 produces reproducible ℓz* anomaly at minimal contamination, extending multi-seed evidence for this model family.（准备中）
- exp-mistral-50pct-s3: Mistral-7B-v0.3 50% MMLU contamination with seed=456 completes 3-seed evidence, enabling full multi-seed multi-model contamination detection analysis.（准备中）
- exp-mistral-15pct-s3: Mistral-7B-v0.3 15% MMLU contamination with seed=456 completes 3-seed reproducibility for this model family, enabling robust cross-model comparison.（准备中）
- exp-llama-5pct-s2: Llama-3.1-8B 5% MMLU contamination with seed=123 produces reproducible ℓz* detection signal at the lowest contamination level, extending multi-seed evidence.（准备中）
- exp-llama-25pct-s2: Llama-3.1-8B 25% MMLU contamination with seed=123 produces consistent mid-contamination detection signal, enabling multi-seed dose-response comparison.（准备中）
- exp-llama-50pct-s3: Llama-3.1-8B 50% MMLU contamination with seed=456 completes 3-seed evidence for θ-shift absorption pattern in Llama, enabling cross-model comparison with Qwen.（准备中）
- …另有 28 项

## 近期结论
- **exp-mistral-25pct-s2** (killed): Mistral-7B-v0.3 25% MMLU contamination with seed=123 extends multi-seed evidence at mid-contamination for Mistral dose-response.
- **exp-mistral-25pct-s1** (killed): Mistral-7B-v0.3 25% MMLU contamination with seed=42 fills the mid-contamination cell, completing the dose-response curve for Mistral with the original seed.
- **exp-llama-15pct-s1-pilot** (success): Llama-3.1-8B 15% MMLU contamination with seed=42 in the unified pilot pipeline (item selection seed=42) produces comparable lz* anomaly to ctrl_contam_llama results, enabling apples-to-apples multi-seed comparison across all model families.

## 趋势
成功 67 / 负向 8 / 失败 0 / 共 81
acc_overall: 0.6654 ↓（近 3 次 success）
acc_seen: 0.6676 ↓（近 3 次 success）

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-35694: 无 GPU 信息

## 告警
- llama_clean_s8: 已被终止 — unknown
- llama_clean_s9: 已被终止 — unknown
- llama_clean_s10: 已被终止 — unknown
- llama_clean_s11: 已被终止 — unknown
- exp-mistral-25pct-s1: 已被终止 — unknown
- exp-mistral-25pct-s2: 已被终止 — unknown
