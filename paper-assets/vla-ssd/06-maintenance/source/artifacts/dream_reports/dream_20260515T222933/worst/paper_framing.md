# Paper Framing — vla-ssd

## Target Venue
- Primary: CoRL 2026
- Deadline: Abstract May 26, Paper May 29
- Format: 8 pages + references

## Core Claims (3 条)

1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.488）和 standalone vision model（DINOv2 ρ=0.388）。
2. **LLM Degrades Action Alignment**: LLM processing 降低而非增强 action-relevant 几何结构（0.615→0.488）。这一 degradation 在 trained/untrained、with/without instruction 四种条件下一致发生。
3. **Training and Instruction Invariance**: VLA task-specific fine-tuning（Δ<0.01）和 instruction input（Δ<0.005）均不显著改变 LLM hidden state 中的 action-relevant 表征结构。2×2 matrix（training × instruction）四格收敛于 0.48-0.49。

## Story Spine

- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。
- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。
- **Our framing**: 首次对 VLA 进行系统性 representational analysis——7 种 probing 方法 × 2 benchmarks × 组件级分解，定量揭示 action-relevant 结构的来源。发现 LLM 不仅不贡献，反而 degrades vision encoder 提供的 action alignment。
- **Headline result**: "SigLIP+projector representations achieve RSA ρ=0.615 with action structure, while the full VLA only achieves ρ≈0.488 regardless of training or instruction — the LLM degrades rather than enhances action-relevant representations."

## Anticipated Reviewer Concerns & Responses

### C1: 单一 VLA 架构（OpenVLA）泛化性
- **应对**: Scope 明确限定为 "OpenVLA-class architecture"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。
- **实验**: 无需额外实验，Limitations 明确标注。

### C2: SigLIP vs DINOv2 pretraining confound
- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。
- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。
- **实验**: P2 可补 CLIP vs DINOv2 对比，但非 blocking。

### C3: LLM degradation 机制不清
- **问题**: 为什么 LLM 降低 action alignment？
- **应对**: LLM 对 representation 做 next-token prediction 优化的变换，这与保持 action-relevant geometric structure 目标不同。Projector bottleneck（D026 发现 SigLIP+projector frozen）约束了信息通路。Discussion 讨论 information bottleneck 解释。
- **实验**: Per-layer RSA degradation curve 作为 P1 supplementary evidence。

### C4: Grant 2026 checkpoint 差异
- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。
- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。

### C5: Practical implications 不够
- **问题**: 发现了问题，然后呢？
- **应对**: 三个可操作建议：(1) 投资 vision encoder pretraining 质量比 LLM fine-tuning 更重要；(2) representation-based downstream tasks 应直接使用 projector output 而非 LLM hidden states；(3) VLA 架构设计应关注减少 LLM 对 visual structure 的 degradation。

## Key Evidence Inventory

| Evidence | Claim | Status |
|----------|-------|--------|
| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |
| Full VLA RSA ≈ 0.488 (4 conditions) | C2, C3 | ✅ Done |
| DINO RSA=0.388 | C1 | ✅ Done |
| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |
| Instruction ablation Δ=0.004 | C3 | ✅ Done |
| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |
| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |
| Per-layer RSA degradation curve | C2 | 🔄 P1 supplementary |
| Random instruction control | C3 | 📋 P1 planned |

## Literature Positioning

- **Grant et al. 2026**: Behavioral level "visual pathway dominates" → 我们 representational level 确认 + 定量组件分解
- **Fang 2025**: "Fine-tuning erodes VLM reasoning" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure
- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: "VLAs ignore language instructions" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响
