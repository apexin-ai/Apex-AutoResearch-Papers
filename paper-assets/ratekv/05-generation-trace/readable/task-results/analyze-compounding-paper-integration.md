# analyze compounding paper integration

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_compounding_paper_integration_20260515T180021_result.json`
- **Structured JSON:** [`3ca5abad39cb4f25d1f5.json`](../../sessions/3c/3ca5abad39cb4f25d1f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Draft 已保存至 `artifacts/compounding_analysis_draft.tex` 并注册。

**内容概要**：

- **对比结构**：Llama (spike, conc=0.57, t₁/t₅=0.85) 的 k₂₅₆/k₀ = 188× catastrophic compounding vs Mistral (flat, conc=0.24, t₁/t₅=0.41) 的 k₂₅₆/k₀ = 1.065× benign
- **关键转折点**：Llama 在 k≈32 出现 elbow（9.05→11.99→40.21→1519）；Mistral 全程在 1.065× 带内，k≥64 饱和
- **因果解释**：spike 分布的 outlier head (L2H5, δ=15.26) 与其他 head 的 distortion 非可加性交互 → 超线性 compounding；flat 分布（CV=1.31, top δ=0.32）的 distortion 太小，joint effect 保持近似可加
- **Claim 支持**：constraint 对 spike 模型 essential（防止 188× collapse），对 flat 模型 redundant（unconstrained 已近 uniform）；diagnostic rule 正确预测两种 outcome
- 所有数字追溯至 `llama_compounding_sweep`、`mistral_compounding_sweep`、`llama_hires_bf16_2bitonly`、`mistral_hires_bf16_2bitonly_v4`，exp_id 标注在 LaTeX 注释中

**注意**：task description 中的 concentration/t₁/t₅ 数字（Llama conc=0.62, t₁/t₅=24.35; Mistral conc=0.18, t₁/t₅=0.38）与 registry 和论文 Table 1 不一致。Draft 使用 registry 验证值（Llama 0.57/0.85; Mistral 0.24/0.41）。

---
