# Paper Framing — importance_margin_vla_compress

## Target Venue
- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29 — 13 days, 极紧但 AI 团队可行需加卡)
- Secondary: **AAAI 2027** (deadline ~August 2026 — 充裕时间做完整实验+理论打磨)
- Stretch: **ICLR 2027** (deadline ~October 2026 — 全面扩展实验)

## Core Insight
VLA token compression 的脆弱性根源是 importance ranking instability（margin Δ_k 太小），而非 entropy 问题。直接最大化 Δ_k 既避开了 entropy 方向的文献矛盾，又提供了可证明的 top-k 选择稳定性保证。关键工程发现：ACIS 和 backbone 必须解耦训练（two-stage），否则 co-adaptation 损害 backbone 质量。

## Core Claims (3 条，均可证伪)

### Claim 1: Certified Robustness
IMM 训练使 VLA token compression 在 ε-bounded 对抗扰动下具有可证明的 top-k 选择稳定性。形式化保证：P(top-k set changes) ≤ k · ε · L / Δ_k。这是首个针对 VLA token compression 的 certified robustness condition。

**支撑证据（MVP）**：G1=93.23x margin 提升，G2=+56pp preservation rate 提升，G4=0.135 LED。
**待补充**：多 ε 水平下的 bound 实证验证、与现有防御方法（adversarial training, smoothing）对比。

### Claim 2: Lossless Compression via Two-Stage Training
Two-stage 训练（Stage1 冻结 backbone 训 ACIS → Stage2 冻结 ACIS 训 LoRA）消除 ACIS-backbone co-adaptation，使 50% token 压缩在保持甚至提升 action prediction 质量的同时提供鲁棒性。

**支撑证据（MVP）**：G3-deploy=0.87x（优于 baseline 13%），ACIS prune vs random prune = 5.1x。
**待补充**：跨模型（OpenVLA/OpenPi）、跨 benchmark（LIBERO）验证；success rate 评估；joint vs grad-isolated vs two-stage ablation。

### Claim 3: Importance-Guided Denoising Effect
ACIS 学到的 importance scoring 识别出信息密集的 token 子集，pruning 低重要性 token 起到 denoising/正则化作用，解释了 G3 < 1.0 的现象。

**支撑证据（MVP）**：pruneTrue 0.0035 < baseline 0.0041 < random prune 0.018。
**待补充**：被删除 token 的 attention weight 分布分析、不同 pruning ratio 下的性能曲线、token importance 与 action relevance 的相关性分析。

## Story Spine

**Problem**: VLA token compression 对实时机器人部署至关重要，但 "Less Is More Until It Breaks" (2601.12042) 和 CAGE (ICML 2026) 证明压缩引入了对抗脆弱性——小扰动使压缩机制丢弃安全关键 token。现有 15+ 种 VLA 压缩方法全部只关注效率，无一解决 adversarial robustness。

**Existing approaches & gaps**: 两类工作互不交叉——压缩方法（VLA-ADP, LightVLA, GridS 等）忽略鲁棒性；鲁棒性方法（RobustVLA, ProGAL-VLA）忽略压缩。试图通过 entropy reduction 提升鲁棒性的方向与文献矛盾（ICCV 2023 ADL 和 HIES 证明低 entropy 本身是脆弱性来源）。

**Our framing**: 压缩鲁棒性取决于 importance margin Δ_k，不取决于 entropy。我们直接最大化 Δ_k，提供首个 certified condition for safe VLA token compression。关键工程贡献：two-stage 训练解耦 ACIS 与 backbone，消除 co-adaptation 使压缩无损甚至增益。

**Headline result template**: "On {benchmark}, IMM-trained SmolVLA achieves {X}% task success under 50% token compression + ε={Y} perturbation, while standard compression retains only {Z}%, providing the first certified robustness guarantee for VLA token compression."

## Venue Fit Risks

- **CoRL**: 理想匹配（VLA + robotics deployment + robustness）。风险：理论贡献需要包装为"deployability criterion"而非纯 adversarial ML。时间极紧（13 天），需要加 GPU 并行铺实验。
- **AAAI**: 接受理论+实验混合贡献。风险：robotics 社区 overlap 较小，需要强调通用 token compression 安全性。
- **ICLR**: 最匹配理论+方法贡献。风险：需要更全面的 baseline 对比和 ablation。

## Anticipated Reviewer Concerns & Response Plan

### RC1: G3 < 1.0 为什么压缩后更好？
**应对**：Claim 3 的 ablation（attention weight 分析、pruning ratio 曲线、token importance-action 相关性）。预期审稿人会怀疑这是 evaluation artifact。

### RC2: 只在 SmolVLA/aloha_sim_insertion 上验证
**应对**：扩展到 OpenVLA + LIBERO suite。至少 2 个模型 × 2 个 benchmark。

### RC3: 只有 action loss 没有 success rate
**应对**：已在准备 sim rollout 评估。成功率是最终判据。

### RC4: ACIS hard dependency（standard ratio 5.09x）
**应对**：这是 feature not bug——ACIS 是 deployment 时的必要组件（类似 BatchNorm），部署成本可忽略（lightweight cross-attention）。论文需讨论 deployment overhead。

### RC5: Formal bound 实证验证
**应对**：多 ε 水平下测量 bound tightness，绘制 theoretical vs empirical 对比图。

### RC6: 与现有压缩方法的 head-to-head 对比
**应对**：IMM 是 compression-agnostic 的训练方法，可叠加到任何 compression method 上。实验需展示 IMM + FastV、IMM + VLA-IAP、IMM + VLA-Cache 的组合效果。
