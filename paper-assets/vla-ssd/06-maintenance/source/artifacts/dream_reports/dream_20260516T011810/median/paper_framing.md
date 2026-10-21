# Paper Framing — vla-ssd

## Target Venue
- Primary: CoRL 2026
- Deadline: Abstract May 26, Paper May 29
- Format: 8 pages + references

## Core Claims (3 条)

1. **Vision Encoder Dominance**: VLA 中 action-relevant 表征结构由 frozen vision encoder（SigLIP）决定。SigLIP+projector 的 RSA 与 action structure 的相关性（ρ=0.615）远高于完整 VLA（ρ≈0.501, image_mean 聚合）和 standalone vision model（DINOv2 ρ=0.388）。
2. **LLM Redistributes Action-Relevant Structure (Training-Dependent)**: LLM 降解 distributed image token 的 **geometric alignment**（RSA: 0.615→0.501）和 functional capacity（R²: 0.706→0.683, p=0.001），但 global structure 保留（CKA 单调上升）。**训练后** LLM 学会将 action 信号 concentrate 到 readout token（trained R²=0.731 > projector 0.706, p=0.001），但 **untrained LLM 做不到**（untrained readout best=0.686 < projector 0.706）。Readout concentration 是 learned behavior，不是架构固有属性。
3. **Training: Routing Without Creating**: VLA fine-tuning 不改变 distributed representation structure（image_mean RSA: trained 0.501 ≈ untrained 0.485, bootstrap CI includes 0, p=0.20），但提升 readout concentration（trained last_preaction 0.731 >> untrained 0.686，Δ=0.045, bootstrap CI=[0.032, 0.058], p<0.0001）。Instruction input 对两者均无影响。综合解读：**Training 的贡献是学习信息路由（routing），而非注入新的 action knowledge（creating）**。

## Paper 主数值基准（image_mean 聚合，公平对比）

| Model / Condition | RSA (image_mean) | Notes |
|---|---|---|
| **SigLIP+Projector** | **0.615** | Smoking gun, LLM input |
| VLA trained with-inst | 0.501 | Peak L23 |
| VLA untrained with-inst | 0.485 | Peak L23 |
| VLA trained no-inst | 0.501 | Peak L23, identical to with-inst |
| VLA untrained no-inst | 0.482 | Peak L29 |
| DINO-V2 | 0.388 | Vision-only baseline |

last_preaction 数值（trained 0.488, untrained 0.485）放 supplementary 作为 robustness check。

## Functional Probe 数值基准

### Raw Action Prediction R²

| Model | mean_R² | Notes |
|---|---|---|
| **SigLIP+Projector** | **0.706** | Vision encoder output |
| VLA Trained image_mean L19 | 0.683 | image tokens degraded — ✅ bootstrap CI=[0.011, 0.037], p=0.001 vs Proj |
| **Trained last_preaction L19** | **0.731** | readout concentration (p=0.001 vs projector) |
| Untrained image_mean L0 | 0.714 | Architecture-intrinsic |
| **Untrained last_preaction L32** | **0.686** | < projector (0.706) → redistribution requires training (D034) |
| DINO-V2 (LIBERO-Goal) | **0.712** | ✅ cls_token; DINO ≈ Proj (Δ=0.005, CI=[-0.008, 0.019], p=0.22, n.s.) |

**Three-way ordering**: DINO (0.712) ≈ Projector (0.706) > LLM image_mean (0.683)

**重要发现**: DINO 与 Projector 在 action decodability (R²) 上无显著差异，但 RSA 几何对齐差异显著（0.388 vs 0.615）。说明 action information 的 presence（probe 可解码）与 geometric alignment（表征空间结构匹配 action 空间结构）是不同维度。论文需区分这两个层面。

### Action-Delta Prediction R²

| Model | mean_R² | Notes |
|---|---|---|
| VLA Trained image_mean L14 | 0.122 | |
| SigLIP+Projector | 0.118 | ≈ LLM, CI includes 0 (p=0.04) |
| Untrained image_mean L0 | 0.117 | ≈ projector ≈ LLM |
| DINO (LIBERO-Goal) | 0.100 | action_delta probe from v2 |
| DINO (MVP-2 LIBERO-10) | 0.061 | 2× lower than projector/LLM |

**Delta 维度结论**：三者几乎相同（~0.12），远 > DINO (0.06-0.10)。支持 vision encoder dominance（所有 action-delta info 追溯到 SigLIP）。Delta last_preaction 缺失（待补）。

### 聚合口径依赖性（论文必须如实讨论）

| Comparison | image_mean | last_preaction |
|---|---|---|
| Raw action: Proj vs LLM | Proj wins (+0.023, CI=[0.011, 0.037], p=0.001) | LLM wins (+0.025, p=0.001) |
| Delta: Proj vs LLM | ≈ tie (−0.003, CI includes 0) | TBD |

主文用 image_mean（公平聚合），last_preaction 放 supplementary。但必须讨论聚合口径对结论的影响。

## Story Spine

- **Problem**: VLAs 通过 fine-tuning LLM on robot data 实现 impressive performance，但 action-relevant 表征从何而来？业界隐性假设 fine-tuning 注入 new representational knowledge，但无系统性验证。
- **Existing approaches & gaps**: Grant et al. 2026 从 behavioral level 发现 visual pathway dominates，但未做 representational decomposition。无人测量过 VLA 各组件（vision encoder / projector / LLM）对 action-relevant 表征结构的独立贡献。
- **Our framing**: 首次对 VLA 进行系统性 representational + functional analysis——组件级分解 + per-layer probing + action prediction probes，定量揭示 action-relevant 结构的来源和 LLM 对其的变换。发现 vision encoder 是 action information 的通用源头（DINO ≈ SigLIP in R²，但 VL pretraining 赋予 geometric alignment）。LLM 降解分布式 image token 表征但通过**训练依赖的** attention 机制将信号聚合到 readout token——training 教会 routing 而非 creating new knowledge。
- **Headline result**: "The frozen vision encoder provides action-relevant representations (RSA ρ=0.615, action probe R²=0.706) that the LLM degrades at the image-token level (R²→0.683) but reconcentrates into a readout token (R²=0.731). This reconcentration is training-dependent (untrained readout R²=0.686 < projector 0.706), while distributed representation structure remains training-invariant (image_mean RSA: trained 0.501 ≈ untrained 0.485, p=0.20). Language instructions affect neither."
- **✅ All core evidence complete.** P1 remaining: plan_012 CLIP-ViT control, plan_010 LIBERO-Spatial (P2).

## Anticipated Reviewer Concerns & Responses

### C1: 单一 VLA 架构（OpenVLA）泛化性
- **应对**: Scope 明确限定为 "OpenVLA-class architecture"。OpenVLA 是最广泛使用的开源 VLA 之一，findings 对该架构族直接适用。Discussion 中讨论扩展到其他架构的预期。
- **实验**: 无需额外实验，Limitations 明确标注。

### C2: SigLIP vs DINOv2 pretraining confound
- **问题**: SigLIP 是 image-text contrastive pretrained，DINOv2 是 self-supervised。RSA gap 可能来自 language-aware pretraining 而非纯 vision encoder 质量。
- **应对**: 这个 confound 实际上 **强化** 我们的 story——如果 gap 来自 SigLIP 的 vision-language pretraining，说明 pretraining 阶段的 language grounding 远比 task-specific fine-tuning 重要。Discussion 正面讨论此 confound 并将其转化为 insight。新发现加强此论点：DINO 与 Projector 在 action R² 上无差异（0.712 vs 0.706, p=0.22），但 RSA 几何差异显著（0.388 vs 0.615）。说明 VL pretraining 的贡献在于 geometric alignment 而非 information content。
- **实验**: plan_012 CLIP-ViT control (P1)。区分 "use VL-pretrained encoder" vs "use SigLIP specifically"。

### C3: LLM 对 action structure 的作用机制
- **问题**: LLM 到底做了什么？为什么 image token RSA 降低？
- **应对**: Functional probe 揭示机制——LLM 降解分布式 image token 表征（R² 0.706→0.683, bootstrap CI=[0.011, 0.037]）但通过 self-attention 将 action 信号 concentrate 到 readout token（R² 0.731）。这是 next-token prediction architecture 的自然行为：信息从 context tokens 流向 prediction position。Per-layer curve 的非单调模式（中间层部分恢复）与此一致。
- **实验**: ✅ plan_011 functional probe (Done) + plan_003 per-layer curve (Done)。

### C4: Grant 2026 checkpoint 差异
- **问题**: Grant 用 OFT fine-tuned，我们用 standard fine-tuning checkpoint。
- **应对**: 我们用 standard fine-tuning 是更强的测试——如果完全不同的 LLM 权重（random init vs pretrained+finetuned，cos_sim≈0.2）都不改变表征，OFT 更不会。Related Work 明确区分。

### C5: Practical implications / 功能验证
- **问题**: RSA alignment ≠ task performance。Practical implications?
- **应对**: ✅ plan_011 functional probe 完成——projector R²=0.706 vs LLM image_mean 0.683（gap=0.023, bootstrap CI=[0.011, 0.037], p=0.001）。LLM readout token R²=0.731 > projector（p=0.001）。Delta probe: projector < LLM 但不显著（CI 含 0）。三个建议：(1) Vision encoder pretraining 是 action info 关键；(2) Image-level tasks 用 projector output；(3) LLM 的价值在于 readout concentration。
- **实验**: ✅ plan_011 Done（含 bootstrap CI + DINO 三方对比）。

### C6: 聚合方式伪影（已解决）
- **问题**: SigLIP 用 mean pooling，VLA 用 last token，比较不公平。
- **应对**: ✅ 已用 image_mean 聚合验证。VLA image_mean RSA=0.501，仍远低于 SigLIP 0.615（gap=0.114）。两种聚合方式结果一致（last_preaction 0.488 vs image_mean 0.501）。主文使用 image_mean 保证公平，last_preaction 放 supplementary。

## Key Evidence Inventory

| Evidence | Claim | Status |
|----------|-------|--------|
| SigLIP+Projector RSA=0.615 | C1, C2 | ✅ Done |
| Full VLA RSA ≈ 0.501 (image_mean, 4 conditions) | C2, C3 | ✅ Done |
| DINO RSA=0.388 | C1 | ✅ Done |
| 6 probing methods × 2 benchmarks: trained ≈ untrained | C3 | ✅ Done |
| Instruction ablation Δ=0.004 | C3 | ✅ Done |
| 2×2 matrix Bootstrap CI includes 0 | C3 | ✅ Done |
| Output head analysis: SigLIP+projector frozen | C1, C2 | ✅ Done |
| Per-layer RSA degradation curve | C2 | ✅ Done — non-monotonic, Proj→L1 primary drop |
| VLA image_mean RSA (aggregation robustness) | C2 | ✅ Done — 0.501 vs SigLIP 0.615, gap=0.114 |
| Bootstrap CI on training effect (image_mean) | C3 | ✅ Done — CI includes 0, invariance holds |
| Functional action probe: Proj 0.706 vs LLM img_mean 0.683 vs readout 0.731 | C1, C2 | ✅ Done — bootstrap CI=[0.011, 0.037], p=0.001 |
| DINO action probe on LIBERO-Goal | C1 | ✅ Done — R²=0.712, DINO ≈ Proj (p=0.22) |
| Action-delta probe: Proj 0.118 < LLM 0.122, CI includes 0 | C2 | ✅ Done — BELOW but not significant |
| No-inst image_mean RSA: trained 0.501 = with-inst, untrained 0.482 | C3 | ✅ Done |
| Untrained last_preaction: L32 R²=0.686 < projector 0.706 | C2, C3 | ✅ Done — redistribution is training-dependent (D034) |
| Untrained vs trained last_preaction bootstrap CI | C2, C3 | ✅ Done — Δ=0.045, CI=[0.032, 0.058], p<0.0001 |
| Random instruction control: normal 0.489, random 0.484, shuffled 0.483, empty 0.472 — all within ±0.017 | C3 | ✅ Done — instruction content invariant (plan_008) |
| CLIP-ViT pretraining control | C1, C2 | 📋 P1 planned (plan_012) |
| CKA verification: ordering reversal — CKA untrained > trained > proj > DINO | C1, C2, C7 | ✅ Done — RSA-CKA dissociation (plan_009) |
| LIBERO-Spatial cross-benchmark | C1, C2, C3 | 📋 P2 planned (plan_010) |

### C7: RSA vs CKA metric dependency — 排序反转（plan_009 已完成）
- **问题**: CKA 不仅缩小 gap，还**反转排序**。RSA: projector > trained > untrained > DINO。CKA: untrained > trained > projector > DINO。
- **数据**:
  - CKA vs actions: untrained L23 (0.089) > trained L23 (0.083) > projector (0.081) > DINO (0.066)
  - CKA per-layer trained image_mean: L0=0.081 **单调上升** to L32=0.098（与 RSA 的非单调模式不同）
  - CKA last_preaction: L32=0.127（最高，支持 redistribution — readout concentration）
  - CKA_RDM: last_preaction (0.290) > projector (0.257) ≈ trained (0.260) > DINO (0.241)（部分一致）
- **应对**: 论文正面讨论作为 finding。关键区分：
  - RSA 捕捉 **local geometric alignment**（representation 距离结构是否匹配 action 距离结构）→ LLM 降解
  - CKA 捕捉 **global structure preservation**（整体变换后结构是否保留）→ LLM 保留或改善
  - **Claim 2 必须明确限定为 "geometric (RSA) degradation"**，不能泛化为 "representation quality degradation"
  - CKA last_preaction 最高 (0.127) 与 redistribution narrative 一致
- **实验**: ✅ plan_009 Done。

## Literature Positioning

- **Grant et al. 2026**: Behavioral level "visual pathway dominates" → 我们 representational level 确认 + 定量组件分解
- **Fang 2025**: "Fine-tuning erodes VLM reasoning" → 我们发现 LLM step 本身（不只是 fine-tuning）就降低 visual structure
- **Hou 2026 (LangGap) / Fei 2025 (LIBERO-Plus)**: "VLAs ignore language instructions" → 我们从 representation level 解释 why：instruction text 对表征结构无实质影响
- **Haon et al. (CoRL 2025)**: Mechanistic interpretability + activation steering on OpenVLA — same venue, same model. Must discuss: their sparse semantic directions vs our geometric analysis are complementary views
- **Lu et al. 2025**: Linear probing on OpenVLA hidden layers >90% accuracy — methodologically closest, must differentiate (component decomposition vs layer probing)
- **Rizzardo et al. 2026**: Feature observability/controllability in VLAs
- **Swann et al. 2026**: SAE-based OpenVLA interpretability
- **Molinari et al. 2025**: Emergent world representations in OpenVLA
- **Karamcheti et al. 2024 (Prismatic)**: OpenVLA's architectural foundation, must cite
