# Handover — 2026-05-24

> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。

## 运行中
（无）

## 待处理
- exp-multi-seed-llama-pw-seed456: LLaMA-3.1-8B PW seed456 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42/123/789 组成 4-seed 覆盖。（排队等待 GPU）
- exp-deberta-ft-combo: Fine-tuned DeBERTa-large on ProofWriter OWA depth-5 achieves near-perfect NLI accuracy (99.67%) and provides massive combo gains over SC baseline when used as external verifier, demonstrating that domain-specific NLI fine-tuning breaks the SCB ceiling by providing truly independent verification signal.（准备中）
- exp-multi-seed-mistral-folio: Multi-seed replication (seeds 123,456,789) of Mistral-7B × FOLIO-204 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42 already available. Combined with Mistral×PW and Qwen2.5×FOLIO/PW multi-seed, provides comprehensive reproducibility evidence for W4 reviewer response.（准备中）
- exp-multi-seed-qwen25-7b-folio: Multi-seed replication (seeds 123,456,789) of Qwen2.5-7B × FOLIO-204 adds a fourth model family (beyond Qwen2.5-14B, Mistral-7B, LLaMA-8B) for cross-family consistency of SCB. If Δ(SICA-SC)≤0 holds across 7B-scale Qwen as well, it strengthens the scale+architecture invariance claim.（准备中）
- exp-multi-seed-qwen25: Multi-seed replication (seeds 123,456,789) of Qwen2.5-14B × FOLIO-204 and ProofWriter-600 shows consistent Δ(SICA-SC) direction across seeds. Baseline seed=42: FOLIO Δ=-1.96pp, PW Δ=-2.00pp. Addresses W4 reviewer concern.（准备中）
- exp-013-constraint-ablation: MaxSAT satisfiability checking contributes minimal accuracy gains over naive constraint counting, because extracted constraints are too homogeneous (trace co-sourcing) to provide discriminative satisfiability signals. If SICA-MaxSAT ≈ SICA-count-only, the SAT solver is not the bottleneck — constraint quality is.（准备中）
- exp-d135-frontier-scb: 2026 frontier closed-source models (Claude/GPT/Gemini via OpenRouter) also exhibit SCB: self-extracted constraints will show BR≥2× with SICA≈SC, extending the scale-invariance finding from open-source 7B-72B to frontier closed-source models.（准备中）
- exp-d126-r1-distill-sica: Reasoning-distilled model (DeepSeek-R1-Distill-LLaMA-8B) does not escape SCB: self-extracted constraints will show BR≥2× and SICA≈SC, demonstrating that SCB is a structural property of autoregressive self-extraction that reasoning training cannot eliminate.（准备中）
- exp-d134-e6-closed-model: Closed-source frontier models (GPT-4o, Claude, etc.) also exhibit symbolic confirmation bias when self-extracting FOL constraints. If SCB persists at frontier scale with different architectures, this strengthens the claim that SCB is a fundamental property of self-verification rather than a scale or architecture artifact.（准备中）
- exp-d134-cil: CIL (Cumulative Information Lift) unifies combo gain prediction: CIL>0 iff verifier adds independent signal beyond generator. Cross-architecture NLI pairs show CIL>0 (predicting significant combo gain), while same-model SICA shows CIL≈0 (predicting no gain), validating CIL as the mechanistic criterion for escape.（准备中）
- …另有 6 项

## 近期结论
- **exp-multi-seed-qwen25-pw-seed789-v2** (success): Qwen2.5-14B PW seed789 多种子复制（第三次尝试，独立 vLLM on cuda:2 port 8007）。验证 SCB 在 ProofWriter 上跨 seed 稳定性。前两次因 vLLM 配置问题失败。 ← 基于 exp-multi-seed-qwen25
- **exp-027-qwen3-14b-non-thinking** (negative): Qwen3-14B（代际升级）在 non-thinking mode 下 FOLIO 204 的 SICA vs SC：capability trap 是否在次世代模型持续？预期 Qwen3 基础能力提升使 SC baseline 更高，但 self-extraction 质量仍不足以产生 SICA 增益（delta≈0），证明 capability trap 是结构性的而非模型能力不足。 ← 基于 sica_expanded_14b
- **exp-multi-seed-qwen3-pw-seed789** (negative): Qwen3-14B non-thinking PW seed789 多种子复制。验证 SCB 在 ProofWriter 上跨 seed 稳定性（Δ(SICA-SC)≤0）。配合 seed42 组成多 seed 覆盖。 ← 基于 exp-027-qwen3-14b-non-thinking

## 趋势
成功 42 / 负向 81 / 失败 22 / 共 160

## 下一步
（无活跃 idea，请通过 ideas.md 添加）

## 资源状态
westd-16639: 空闲 cuda:0, cuda:1, cuda:2, cuda:3
westd-30973: 空闲 cuda:0, cuda:1, cuda:2

## 告警
- mvp_math50_t07: 已被终止 — unknown
- sica_aime30_t07: 已被终止 — unknown
- sica_aime30_v2: 已被终止 — unknown
- sica_aime30_v3: 已被终止 — unknown
- sica_proofwriter30: 训练失败 — unknown
- sica_folio30: 已被终止 — unknown
- sica_proofwriter30_v2: 已被终止 — unknown
- exp-011-llama8b: 训练失败 — unknown
- exp-010-mistral: 训练失败 — unknown
- exp-011-llama8b-v2: 训练失败 — unknown
- exp-017-strategyqa: 训练失败 — unknown
- exp-018-arc: 训练失败 — unknown
- exp-010-mistral-v2: 训练失败 — unknown
- exp-017-strategyqa-v2: 训练失败 — unknown
- pilot-contrastive-prompt: 训练失败 — unknown
- exp-028-qwen3-14b-thinking: 已被终止 — unknown
- exp-033-qwen3-pw600-nonthinking: 训练失败 — unknown
- exp-007-qwen72b-awq: 训练失败 — unknown
- exp-004-qwen7b-rerun: 训练失败 — unknown
- exp-042-premise-formalization: 训练失败 — unknown
- exp-044-icl-oracle: 训练失败 — unknown
- exp-042b-premise-formal: 训练失败 — unknown
- exp-045b-backward-verify: 已被终止 — unknown
- exp-028b-qwen3-thinking-folio204: 已被终止 — unknown
- exp-049-mistral-logiqa200: 训练失败 — unknown
- exp-050-mistral-icl-oracle-folio199: 训练失败 — unknown
- exp-052-mistral-folio204-seed123: 已被终止 — unknown
- exp-053-mistral-folio204-seed456: 已被终止 — unknown
- exp-064: 已被终止 — unknown
- exp-075-contrastive-mistral-folio: 训练失败 — unknown
- exp-d126-70b-sica: 训练失败 — unknown
- exp-multi-seed-llama-folio: 训练失败 — unknown
- exp-multi-seed-llama-pw: 训练失败 — unknown
- exp-multi-seed-qwen25-pw-seed789: 训练失败 — unknown
- exp-multi-seed-llama-pw-seed789: 已被终止 — unknown
- exp-multi-seed-qwen25-pw-seed789-v3: 已被终止 — unknown
- exp-multi-seed-llama-pw-seed789-v2: 已被终止 — unknown
