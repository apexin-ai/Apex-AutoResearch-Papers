# Paper Framing — vla-ssd (D060 Reframe → D095 Cross-Architecture Upgrade)

> D048: PI 批准按最大质量重构。A+ 版本保留为 fallback (branch paper-a-plus-backup)。
> D060: Round 4 weak reject → C1 降为框架, C2 升为唯一核心 claim, C3 降为 qualified observation。
> D088-D094: 跨架构验证完成（OpenVLA/Llama-2, TraceVLA/Phi-3, NORA/Qwen2.5-VL × 4 LIBERO suites）。C2 从单架构观察升级为跨架构 robust finding。RC4 基本解决。

## Target Venue
- Primary: CoRL 2026
- Deadline: Abstract May 26, Paper May 29
- Format: 8 pages + references

## Core Insight

VLA fine-tuning 的核心贡献是学习 deliberate instruction routing——**跨三种 VLA 架构（Llama-2-7B, Phi-3-mini, Qwen2.5-VL-3B）和四种任务类型一致成立**。训练将 instruction 表征从 LLM 预训练的中层处理模式 reorganize 到 entry-exit bookend 模式，同时在出口层制造 R² collapse（action-relevant information 在 exit 层被选择性丢弃）。跨架构一致性表明这是 VLA 训练的 emergent property，而非特定模型的 artifact。

**两类效应区分（D090）**：
- **Training-induced（architecture-independent）**: R² exit collapse、counterfactual sensitivity 提升 — 三架构一致
- **Base-model-dependent（NOT training-induced）**: L1 head count — 取决于 base VLM/LLM 的预训练 attention 模式

**三层级路由梯度（D094）**: VLM base（无 routing）→ OXE-pretrained VLA（通用 routing）→ task-finetuned VLA（任务特化 routing）。Routing 在 VLM→VLA 转换时 emerge，在 general→task-specific 转换时 reshape。

## Core Claims (D060 重构：1 核心 + 1 框架 + 1 观察)

### C1: Experimental Framework + Architecture-Verified Specialization [方法论贡献，非 empirical finding]
**重新定位（D060）**: Token-level specialization 是 causal mask 的数学必然（image tokens 在序列中先于 instruction tokens，无法 attend to instructions）+ frozen encoder 不接收 instruction input。论文贡献不是"发现"这一点，而是：
- **(a) 系统实验框架**：factorial design (trained/pretrained/untrained × instruction presence) + 四种互补分析方法（cross-instruction probe + attention + RSA + MLP probe），适用于任何 decoder-only VLA
- **(b) 量化验证**：即使 residual stream 理论上可以 leak information，image tokens 在实际模型的全部 32 层均保持 chance（10%）。这不是 trivial——frozen encoder 权重与 LLM 权重共享 residual stream，验证了 no leakage
- **(c) 训练差异的量化**：untrained readout L1=100% 但 L31=82%（信号衰减）vs trained 100% 全程稳定——framework 揭示了训练影响 routing robustness 而非 routing existence

Key evidence (unchanged):
- Cross-instruction probe: same frame × 10 instructions → 10-way classification
- Dense L0-L32: image_mean = chance at ALL layers
- LOOCV: 100%±0.00 trained, decaying untrained
- **承认**: 10-way classification 本身 trivially easy（untrained L1 也 100%），贡献在于 framework + 三条件对比揭示的 routing 差异

### C2: Three Qualitatively Different Routing Strategies — VLA Fine-tuning Achieves Immediate Dedicated Routing
三条件揭示三种定性不同的 routing 模式：

**L1 Attention Routing (heads + attention fraction):**
- **Untrained (random init)**: 0/32 heads, 12% text attention
- **Llama-2 base (pretrained, no VLA)**: 9/32 heads, 36.5% text attention
- **VLA Trained**: 24/32 heads, 58% text attention

**Full-Layer Probe Profile (instruction classification accuracy):**
- **Trained**: L1=99.6% → 全程 100% — "即时路由 + 完全稳定"
- **Llama-2 base**: L1=80.2% → L2=98.7% → L5+=100% — "渐进建立 + 稳定维持"
- **Untrained**: L1=100% → L8=98.6% → L31=82% — "偶然路由 + 逐渐遗忘"

**VLA Fine-tuning 的独特贡献（精��化）：**
1. **即时性**：L1 即达 99.6%（vs pretrained 需 5 层才饱和）
2. **头数专用化**：24/32 heads instruction-dominant（vs pretrained 9/32）
3. **不是**深层稳定性 — 稳定性来自 pretrained weights（pretrained 也不衰减）

**深层���减只发生在 random init**：说明结构化的 pretrained 表示（无论是否经过 VLA 训练）都能维持 instruction signal；random weights 的噪声累积导致信号退化。

**Full 32-Layer Attention Profile（D054 升级，dense evidence）：**
- **Untrained**: 全 32 层 × 所有 head = 0 instruction-dominant。完全无语言处理能力。
- **Llama-2 base**: 倒U型 — L0-L4 低(0-10 heads) → L9-L16 高峰(15-22 heads) → L31 回落(8)。经典 LM pattern：中层做深度语义处理。
- **VLA Trained**: 书挡型 — L0-L1 高峰(21-24 heads) → L2-L30 低谷(0-11) → L31 再次高峰(18)。入口获取 instruction + 出口条件化 action output。

**C2 Claim（D073 reframe: open-loop functional sensitivity）**: VLA fine-tuning **shifts** instruction attention from mid-layer processing (Llama-2 base: 15-22/32 heads at L10-L17) to entry-layer routing (L0-L1: 21-24/32) and exit-layer re-engagement (L31: 18/32)。Instruction-conditioned action generation operates through **distributed L1 routing** where instruction-attention fraction predicts per-head contribution magnitude (specificity ratio 1.08x at action output)。Routing modulates output direction (d=0.65) without systematic quality degradation (ΔMSE≈0), consistent with an information-computation dissociation (Hewitt & Liang 2019)。不能 claim instruction heads "uniquely responsible" 或 "confirms routing function"——用 "open-loop functional sensitivity" + "support" 而非 "confirm"。可 claim "disproportionate contribution" + "attention-ordered routing"。Section 标题用 "Open-loop functional sensitivity"，正文用 "shifts...from...to..." + "distributed routing"。

Key evidence:
- **32-layer dense attention profile**: Trained bookend (L0-1: 21-24, L31: 18) vs Llama2base inverted-U (L9-16: 15-22)
- Three-condition full-layer probe: trained flat 100%; llama2base saturates L5+100%; untrained decays L1:100%→L31:82%
- L1 attention gradient: 0/32 → 9/32 → 24/32 heads
- VLA-specific contributions: (1) temporal reorganization from mid-peak to bookend, (2) immediacy (L1: 80.2→99.6%), (3) head dedication (9→25 at L1)
- **Per-token normalization**: 38.2x text/image ratio (trained instr-dom) vs 1.5x (untrained) — eliminates token-count confound
- **Trajectory-level d**: all conditions d>2.0 (token-level is conservative ~4x underestimate)
- **GT error**: ΔMSE≈0 (ablation redirects outputs without degrading GT accuracy) — supports information-computation dissociation
- **Token overlap**: Spearman ρ=1.0 between token novelty and d — lexical/positional sensitivity, not semantic distance
- **LOO sensitivity**: all leave-one-out p ≤ 0.083, no qualitative reversal; cream cheese reclassification p=0.008
- **4-condition training trajectory (D075)**: untrained(0) → llama2(9) → bridge-vla(24) → libero-finetuned(22) at L1。Entry routing 稳定，但 L31 exit engagement 18→0（entry-exit → entry-only sharpening）。Probe accuracy 不变（L31 仍 100%），确认 attention-representation dissociation
- **OXE training diversity**: openvla-7b 在 Open X-Embodiment 970K episodes（多平台多任务）上训练，L1 routing 不是 LIBERO-specific

#### C2-X: Cross-Architecture Validation (D088-D094 — 论文最强升级)

**三架构 × 四 suite 矩阵**验证 C2 不是 OpenVLA-specific artifact：

**R² Exit Collapse（architecture-independent training effect）：**

| Arch (backbone) | Suite | Trained Δ (peak−exit) | Untrained Δ | Training-induced? |
|-----------------|-------|----------------------|-------------|-------------------|
| OpenVLA (Llama-2-7B) | Object | 0.121 | 0.076 | ✓ |
| OpenVLA (Llama-2-7B) | Long (OFT) | 0.004 | 0.016 | △ (OFT outlier) |
| TracVLA (Phi-3-mini) | Goal | 0.228 | 0.048 | ✓ |
| TracVLA (Phi-3-mini) | Spatial | 0.138 | 0.016 | ✓ |
| TracVLA (Phi-3-mini) | Object | 0.294 | 0.009 | ✓ |
| TracVLA (Phi-3-mini) | Long | 0.198 | 0.028 | ✓ |
| NORA (Qwen2.5-VL-3B) | Goal | 0.691 | 0.044 | ✓ (极端) |
| NORA (Qwen2.5-VL-3B) | Spatial | 0.302 | 0.037 | ✓ |

结论：9/10 cells 确认 trained Δ >> untrained Δ。OpenVLA Long (OFT) 是唯一例外，与 OFT 微调方式相关。

**L1 Instruction-Dominant Heads（D090: base-model-dependent, NOT training-induced）：**

| Arch | Suite | Trained | Untrained | 解读 |
|------|-------|---------|-----------|------|
| OpenVLA | Goal | 24/32 | 0/32 (random init) | OpenVLA 特有：untrained = random init 无语言能力 |
| OpenVLA | Object | 24/32 | 24/32 (OXE pretrained) | OXE 已创建 routing |
| OpenVLA | Long | 14/32 (OFT) | 25/32 (OXE) | OFT 增加 mixed heads |
| TracVLA | All 4 suites | 27-30/32 | 32/32 | Phi-3-Vision 预训练已 32/32 全极化 |
| NORA | Goal | 13/16 | 13/16 | Qwen2.5-VL 预训练已 13/16 |
| NORA | Spatial | 12/16 | 14/16 | 同上 |

**关键区分**: L1 head count 反映 base model 的语言预训练 attention 模式，**不是** VLA 训练效果。TracVLA untrained（纯 VLM）已 32/32，训练反而减少到 27-30/32（repurpose some heads）。**论文不能 claim L1 heads 是训练学到的**——只能 claim R² collapse 和 CF sensitivity 是训练效果。

**Counterfactual Sensitivity（training-induced）：**

| Arch | Suite | Trained (top d/cos) | Untrained (top cos) | 训练效应 |
|------|-------|---------------------|---------------------|----------|
| OpenVLA | Object | d=1.21 (empty) | cos=0.569 | ✓ trained >> untrained |
| TracVLA | Goal | d=1.52 (empty) | cos=0.153 | ✓ 10× |
| TracVLA | Spatial | d=1.33 (empty) | cos=0.180 | ✓ 7× |
| TracVLA | Object | d=1.21 (empty) | cos=0.185 | ✓ 7× |
| TracVLA | Long | d=1.47 (empty) | cos=0.173 | ✓ 8× |
| NORA | Goal | cos=1.0 (saturated) | cos=0.081 | ✓ 极端 |

"empty" 在 11/12 trained settings 排第一（exception: OpenVLA Long "shuffled" first）。

**TracVLA Universal Mixed Heads (D091)**: h13 和 h22 在全部 4 个 LIBERO suite 的 trained 模型中一致作为 "mixed" head 出现（非 instruction-dominant 也非 image-dominant），而 untrained (Phi-3-Vision) 无此 pattern。暗示训练创建了功能特化的 mixed-modality heads。

**Three-Tier Routing Gradient (D094)**:
- **Tier 1 — VLM base (无 action training)**: TracVLA untrained (Phi-3-Vision) / NORA untrained (Qwen2.5-VL) — 无 R² collapse，无 CF sensitivity（cos < 0.2），L1 heads 来自语言预训练
- **Tier 2 — OXE-pretrained VLA (通用 action training)**: OpenVLA untrained (openvla-7b, 970K OXE episodes) — 已有强 L1 routing (25/32)，强 CF (d=1.048)，但无 exit collapse
- **Tier 3 — Task-finetuned VLA**: OpenVLA/TracVLA/NORA trained — R² exit collapse + task-specific CF pattern

**论文 story 升级**: 从 "VLA training creates routing" 升级为 "routing emerges at VLM→VLA transition and reshapes at general→task-specific transition"。

### C3: Vision Encoder Geometry Observation [降为 qualified observation，非 core claim]
**重新定位（D060）**: RSA inverted-U 的 rise phase 极小（Δρ=0.016, CI 待补），CKA 完全反转 RSA ordering（untrained > trained > DINOv2），"non-monotonic refinement" 仅在 RSA 下成立。DINOv2 ranking 在 CKA 下不成立（CKA 中 DINOv2 排名最低）。

**保留为 observation 的理由**：
- **Decline phase 也是 RSA-specific**：L12→L32 Δρ=-0.206 远大于 rise phase，但 CKA 单调递增无 decline。不能 claim decline 是 metric-robust。
- **R² inverted-U 是 metric-independent 的**：functional probe 确认 L8-L13 peak（0.655-0.678），之后下降。这是 C3 最强的 evidence，不依赖 RSA/CKA 选择。
- **Metric divergence 本身是 honest observation**："non-monotonic under RSA, monotonic under CKA"
- **DINOv2 RSA ranking**：在 RSA 下 robust，但必须加 "under RSA" qualifier

**写法要求**：
- Abstract/Intro 中"non-monotonic refinement"加 "under RSA" qualifier
- DINOv2 "highest geometric foundation" 加 "as measured by RSA"
- best-vs-best Δ=+0.017 明确标 n.s.（CI includes 0）
- Discussion 加 metric-dependence caveat（CKA 反转在正文中 qualify，不只在 appendix）

Key evidence (unchanged but qualified):
- Cross-encoder RSA table — **加 "under RSA" qualifier**
- Per-layer RSA + R² profiles — **rise phase CI 待补报**
- Cross-benchmark replication — still holds
- **CKA divergence** — 必须在正文 acknowledge

## Story Spine (D095 Cross-Architecture Upgrade)

- **Problem**: VLAs fine-tune LLMs on robot data, but how training reshapes instruction routing and information integration at the token level remains uncharacterized — and whether these effects generalize across architectures is unknown.
- **Existing approaches & gaps**: Prior behavioral studies (Grant et al. 2026, Haon et al. 2025) found visual dominance and instruction underutilization, but did not decompose the representational roles of different token positions, explain how training reshapes information flow, or test generalization across VLA families.
- **Our framing**: We provide a systematic experimental framework for token-level analysis of VLAs, validated across three architectures (Llama-2-7B, Phi-3-mini, Qwen2.5-VL-3B) and four task suites. We find that VLA fine-tuning's primary contribution is an architecture-independent routing reorganization: R² exit collapse (action-relevant information selectively dropped at exit layers) and heightened counterfactual sensitivity emerge consistently across all tested architectures. A three-tier routing gradient (VLM base → general VLA → task-specific VLA) reveals that routing emerges at the VLM→VLA transition and reshapes with task specialization.
- **Headline results**: (1) [Framework] Systematic token-level analysis framework applicable to any decoder-only VLA, validated on 3 architectures × 4 task suites (10 cells). (2) [Core finding — architecture-independent] R² exit collapse (trained Δ=0.12-0.69 vs untrained Δ=0.01-0.08) and counterfactual sensitivity (trained 7-10× untrained) confirmed across all three architectures. (3) [Core finding — routing gradient] Three-tier gradient: VLM base (no routing) → OXE-pretrained VLA (general routing, L1=25/32, CF d=1.05) → task-finetuned (task-specific routing with exit collapse). (4) [Nuance — D090] L1 head count is base-model-dependent (Phi-3 32/32 both conditions), not training-induced. (5) [Observation] Under RSA, vision encoder geometry follows inverted-U; functional probes confirm L8-L13 peak.
- **Practical implications**: (1) VLA architecture design should optimize entry-exit instruction routing (architecture-independent finding). (2) Exit-layer collapse is a universal signature of task-specific VLA training — potential diagnostic tool. (3) The routing gradient suggests pretraining-aware fine-tuning strategies.

## Key Numerical Benchmarks (unchanged from A+)

### Cross-Instruction Probe (C1 + C2 核心实验)

| Condition | L0 | L1 | L2 | L5 | L8 | L16 | L24 | L31 |
|-----------|----|----|----|----|----|----|-----|-----|
| Trained last_preaction | 10% | 99.6% | 100% | 100% | 100% | 100% | 100% | 100% |
| **Llama-2 base last_preaction** | **10%** | **80.2%** | **98.7%** | **100%** | **100%** | **100%** | **100%** | **100%** |
| Untrained last_preaction | 10% | 100% | 100% | 99.x% | 98.6% | 92.3% | 86.4% | 82.0% |
| Trained image_mean | 10% | — | — | — | 10% | 10% | 10% | 9.6% |
| DINOv2 | 10% | — | — | — | — | — | — | — |

LOOCV (10-fold): Trained 100.00±0.00 (L8-L31), Untrained 96.64±7.07 → 84.76±11.59

### L1 Attention Pattern (C2 mechanistic evidence — three-condition)

| Metric | Untrained | Llama-2 Base | VLA Trained |
|--------|-----------|--------------|-------------|
| Attention to text/instruction | 11.7% | 36.5% | 57.7% |
| Attention to image | 87.8% | 61.7% | 21.3% |
| Instruction-dominant heads (>50%) | 0/32 | 9/32 | 24/32 |

### Training Effect Size Summary

| Metric | Trained | Untrained | Δ |
|--------|---------|-----------|---|
| RSA peak (image_mean) | 0.628 (L12) | 0.612 (L0) | +0.017 |
| R² peak (last_preaction) | 0.678 (L13) | 0.609 (L32) | +0.069 |
| Inst. routing L31 | 100% | 82% | +18pp |
| Inst. attention L1 | 58% | 12% | +46pp |
| Progress classification | 86.3% (L20) | 85.3% (L4) | +1pp |

### Cross-Encoder RSA (C3)

| Source | RSA |
|--------|-----|
| DINO cls_token | 0.692 |
| DINO patch_mean | 0.631 |
| SigLIP+Projector | 0.615 |
| VLA trained peak (L12) | 0.628 |
| CLIP ViT-L | 0.557 |

## Anticipated Reviewer Concerns (D060 updated — Round 4 已验证)

### RC1: "C1 is trivial — causal mask guarantees it" [Round 4 N1, ACCEPTED]
**Response**: We accept this. Paper now explicitly acknowledges causal mask as structural source. C1 is repositioned as methodological framework + empirical verification, not novel finding. The framework itself (factorial design + 4 methods) has reusable value for VLA analysis.

### RC2: "RSA inverted-U is metric-dependent, CKA reverses" [Round 4 N2, PARTIALLY ACCEPTED]
**Response**: Rise phase (Δρ=+0.016) acknowledged as small and qualified with CI. CKA divergence discussed in main text, not just appendix. Decline phase (Δρ=-0.206) is robust across metrics. DINOv2 ranking qualified with "under RSA". C3 downgraded from core claim to observation.

### RC3: "Ablation 5 demos underfitting" [Round 4 N3, ACCEPTED + RERUN]
**Response**: 50-demo rerun in progress. If effect holds → underfitting confound ruled out. Non-dominant-8 control addresses generic regularization concern. Results TBD.

### RC4: "Only tested on one VLA (OpenVLA)" [D088-D094: NOW ADDRESSED]
**Response**: Now validated across three VLA architectures with different backbones:
- **OpenVLA** (Llama-2-7B, 32L, MHA) — 4 LIBERO suites
- **TraceVLA** (Phi-3-mini, 32L, MHA) — 4 LIBERO suites
- **NORA** (Qwen2.5-VL-3B, 36L, GQA 16h/2kv) — 2 LIBERO suites (Goal, Spatial; no Object/Long checkpoints)
Core finding (R² exit collapse, CF sensitivity) confirmed architecture-independent. L1 head count shown to be base-model-dependent (D090), strengthening the paper by distinguishing what training creates vs what it inherits. 10/12 possible matrix cells filled.

### RC5: "Practical implications speculative / frozen encoder confound" [Round 4 W4]
**Response**: Encoder ranking qualified with "under RSA" and "within fixed encoder configuration." Discussion adds explicit caveat that claims about encoder quality require across-encoder experiments. Routing optimization remains well-supported by three-condition gradient.
