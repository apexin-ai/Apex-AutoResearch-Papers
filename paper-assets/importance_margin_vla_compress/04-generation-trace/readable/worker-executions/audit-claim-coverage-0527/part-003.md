# audit claim coverage 0527 — Part 3 of 3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Worker execution logs

[← Part 2](part-002.md) · [Transcript overview](../audit-claim-coverage-0527.md) · [Structured JSON](../../../sessions/c2/c2285704e4208a57e586.json)

## Before a recorded user message

### Tool result

_source line 22 · 2026-05-27T01:08:11.814Z_

<details><summary>↩ Tool result · `toolu_01Xc3TyGYGuSekG2ah5CooMH`</summary>

```text
1	{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\", \"content\": \"# Paper Framing — importance_margin_vla_compress\\n\\n## Target Venue\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\n\\n## Title (working)\\n\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\"\\n\\n## Core Insight\\n\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\"threshold-graded\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\n\\n**Axis 1 — Token Coupling (connector architecture):**\\n| Type | Connectors | CV Range | Mechanism |\\n|------|-----------|----------|-----------|\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\n\\n**Axis 2 — Task Complexity:**\\n| Level | Suites | Characteristics |\\n|-------|--------|----------------|\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\n\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\\n\\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\\n\\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\\n- **Linear projection** (π0 3.3B, π0.5 4B): **\\\"Uniformly Critical\\\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\\n  Baseline: 97.2%. Random pruning profile:\\n  | k | Object | Spatial | Δ | Pattern |\\n  |---|--------|---------|---|---------|\\n  | 0.95 | 71.1% | deploying | — | — |\\n  | 0.925 | 28.8% (2-seed) | — | — | — |\\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\\n  **Paper value:** strengthens \\\"uniformly critical\\\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\\n\\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\\n\\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\\n\\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\\n\\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\\n\\n**Method contribution**: Diagnose-then-Compress framework:\\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\\n  - **Key discovery**: X-VLA \\\"linear projection\\\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \\\"VTR ceiling depends on connector type\\\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\\n\\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\\n\\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\\n\\n## Core Claims (5 claims, expanded from 4)\\n\\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\\n\\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\\n\\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\\n\\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\\n\\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\\n\\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\\n\\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\\n\\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\\n\\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\\n\\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\\n\\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\\n\\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\\n\\n**Paper narrative upgrade**: From \\\"connector determines compressibility\\\" to \\\"connector determines both compressibility AND optimal compression strategy.\\\" This is a significantly stronger and more novel contribution.\\n\\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\\n\\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\\n\\n**Evidence**:\\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\\n- k=0.9 (remove 13/128 tokens) = 0% SR\\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\\n\\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \\\"robust-then-cliff\\\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\\n\\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\\n- k=0.2: **~4.0%** (-96pp) — near-zero\\n- k=0.1: **~0.0%** (-100pp) — complete failure\\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\\n\\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\\n\\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \\\"sweet spot\\\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\\n\\n**Cross-suite generalization (D117, updated with full results)**:\\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\\n\\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\\n\\nX-VLA pruning curve comparison across suites:\\n\\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\\n|-------|-------|-------|-----|-------|----------|----------|\\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\\n\\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\\n\\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\\n\\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\\n|------|-------|-------|-------|---------|\\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\\n\\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\\n\\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\\n\\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\\n- Robust (Δ≤10pp): T0 \\\"between plate and ramekin\\\" (-4pp), T4 \\\"in top drawer\\\" (-2pp) — global spatial / unambiguous target\\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\\n- Catastrophic (Δ>40pp): T5 \\\"on ramekin\\\" (-48pp, 0%), T9 \\\"on cabinet\\\" (-58pp), T7 \\\"on stove\\\" (-64pp), T1 \\\"next to ramekin\\\" (-78pp)\\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\\n\\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \\\"pick bowl...\\\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\\n\\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\\n- From \\\"connector determines pruning tolerance\\\" → \\\"pruning sensitivity = f(connector_type, task_semantics)\\\"\\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\\n- Task semantic structure determines degradation *severity* within that class\\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\\n\\nπ0 evidence:\\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\\n- Importance CV: π0 = 0.038 (lowest in spectrum)\\n\\n**Key insight**: \\\"Linear projection\\\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\\n\\n### Claim 3b: MLP Projector → Graded Degradation\\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\\n\\n**Evidence** (OpenVLA 6-point degradation curve):\\n- k=1.0: 74.0% (baseline)\\n- k=0.95: 69.4% (-6% relative)\\n- k=0.9: 62.0% (-16% relative)\\n- k=0.7: 49.0% (-34% relative)\\n- k=0.5: 37.4% (-49% relative)\\n- k=0.3: 20.6% (-72% relative)\\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\\n\\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \\\"re-encoding boost\\\" to \\\"near-lossless compression recovery\\\".**\\n\\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\\n\\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\\n\\n**Evidence** (all confirmed):\\n\\nCross-attention re-encoding (M sweep, 3-seed where available):\\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\\n|---|------------|-----|-----|-----|\\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\\n\\nMLP adapter control (M=32, ~22.14M params, 3-seed):\\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\\n|---|---|---|-----|-----|-----|\\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\\n\\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\\n\\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\\n\\n**k=0.5 (main table):**\\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\\n|-------|-----|--------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\\n\\n**k=0.7 (second validation, D142):**\\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\\n|-------|-----|--------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\\n\\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\\n\\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\\n\\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\\n\\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\\n\\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\\n|-------|-----|--------|-----------|-------------|-------------|----------|\\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\\n\\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\\n\\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\\n\\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\\n\\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\\n|---|-----------------|-----------------|-----------|---------------|\\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\\n\\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\\n\\n**V-shape fully confirmed (2 seeds, both methods)**:\\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\\n\\n**Mechanism confirmed by token position visualization (D141)**:\\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\\n\\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\\n\\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \\\"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\\\"\\n\\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\\n\\n**Evidence** (Reviewer-verified, D132 PASS):\\n\\nX-VLA vs OpenVLA full comparison:\\n\\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\\n|---|---|---|---|---|\\n| | L2norm | Random | L2norm | Random |\\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\\n\\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\\n\\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\\n\\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\\n|------|---------|--------|--------|------------|---------|\\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\\n\\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\\n\\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\\n\\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \\\"slightly larger\\\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\\n\\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\\n\\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\\n\\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\\n\\n## Story Spine\\n\\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\\n\\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \\\"token pruning works or fails uniformly\\\" is untested. The critical architectural factor determining prunability is unknown.\\n\\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\\n\\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\\n\\n**Headline result**: \\\"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\\\"\\n\\n## Paper Structure (7-model version)\\n\\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\\n4. **Main Results**:\\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\\n5. **Analysis**:\\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\\n7. **Conclusion**: 5 claims summary\\n\\n## Anticipated Reviewer Concerns\\n\\n### RC1: Only 2 models → **FULLY ADDRESSED**\\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\\n\\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \\\"larger models are more robust\\\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\\n\\n### RC3: Why not test SmolVLA without pixel_shuffle?\\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\\n\\n### RC4: Smart compression — is re-encoding or compression the mechanism?\\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\\n\\n### RC5: Relationship to VLA-IAP\\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\\n\\n### RC6: Is this just \\\"different models behave differently\\\"?\\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\\n\\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\\n\\n## All Experimental Evidence (confirmed)\\n\\n### SmolVLA Cliff-Edge\\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\\n- Attention entropy: 0.952 (flat, TV=0.05)\\n- Official checkpoint Object: 59.2% → 0% at k=0.5\\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\\n\\n### OpenVLA Degradation Curve\\n- k=1.0: 74.0% (370/500)\\n- k=0.95: 69.4% (-6% relative)\\n- k=0.9: 62.0% (-16% relative)\\n- k=0.7: 49.0% (245/500, -34% relative)\\n- k=0.5: 37.4% (187/500, -49% relative)\\n- k=0.3: 20.6% (103/500, -72% relative)\\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\\n\\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\\n|-------|-----------|--------|---------------|---------------|-------|\\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\\n\\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\\n|-------|----------------------|---------|------|------------------|\\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\\n\\nKey insights (updated with 7-model data):\\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \\\"high entropy\\\" like π0.\\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \\\"linear proj\\\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \\\"effective connector\\\" = projection + any intermediate processing.\\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\\n6. Framing: CV captures \\\"degree of non-linear mixing in the vision-to-LLM pathway.\\\" More mixing → higher CV → less tolerant of pruning.\\n\\n### Smart Compress (Learned Re-encoding)\\nCross-attention (VTC) M sweep (3-seed where available):\\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\\n\\nMLP adapter (M=32, 3-seed):\\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\\n- t-test p≈0.15, no significant difference — confirms architecture-independence\\n\\n### D109: VTR on OpenVLA (MLP projector) — FAILED\\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\\n- Failure mode: model outputs identical action every timestep (severe overfitting)\\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\\n\\n### Cross-Suite VTR Generalization (SmolVLA)\\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\\n\\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\\n\\n### Supplementary\\n- Inference latency: 6% speedup at M=32\\n- KV-cache: 75% memory reduction at M=32\\n\", \"total_chars\": 51958, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "628b6e64-3141-4164-aeae-180de1ca7c10",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/7a12e78f-6295-4999-ab31-4ef688467957/tool-results/toolu_014dBPKsooz3jRGA9omaXWwD.txt",
      "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/paper_framing.md\\\", \\\"content\\\": \\\"# Paper Framing — importance_margin_vla_compress\\\\n\\\\n## Target Venue\\\\n- Primary: **CoRL 2026** (Austin, Nov 9-12; abstract May 26, paper May 29)\\\\n- Timeline: 4 days to abstract, 7 days to paper (as of 2026-05-22)\\\\n\\\\n## Title (working)\\\\n\\\\\\\"Why Token Pruning Crashes Some Robot Policies but Not Others: The Role of Vision Connectors in VLA Token Compressibility\\\\\\\"\\\\n\\\\n## Core Insight\\\\n\\\\n**⚠️ D171 (2026-05-22): Restructured from 4-class taxonomy to 2-axis framework.** Cross-suite data broke the original per-model classification — X-VLA \\\\\\\"threshold-graded\\\\\\\" on Object becomes catastrophic on Goal (-27.8pp at k=0.9) and Long (-45pp at k=0.95). The same connector produces drastically different pruning outcomes depending on task complexity. Pruning sensitivity is the product of two independent axes:\\\\n\\\\n**Axis 1 — Token Coupling (connector architecture):**\\\\n| Type | Connectors | CV Range | Mechanism |\\\\n|------|-----------|----------|-----------|\\\\n| **Token-independent** | Pure linear (π0, π0.5), MLP (OpenVLA, OFT) | 0.038–0.219 | Tokens retain individual spatial meaning; pruning damage is local |\\\\n| **Token-entangling** | BART post-proc (X-VLA), Pixel-shuffle (SmolVLA) | 0.151–0.314 | Cross-token dependencies; pruning damage cascades |\\\\n\\\\n**Axis 2 — Task Complexity:**\\\\n| Level | Suites | Characteristics |\\\\n|-------|--------|----------------|\\\\n| **Simple** | Object, Spatial | Single-step, pruning impact contained |\\\\n| **Complex** | Goal, Long | Multi-step reasoning, token loss cascades through action sequence |\\\\n\\\\n**Key interaction (D169):** Token-entangling connectors are dramatically more sensitive to task complexity:\\\\n- X-VLA Object k=0.9: 97.6% → X-VLA Goal k=0.9: 70.2% (-27.8pp, same model/method/k, only task differs)\\\\n- X-VLA Long k=0.95: ~53% (-45pp from baseline) — removing 3 of 50 tokens collapses performance\\\\n- SmolVLA: 0% on Object already → floor effect, task complexity cannot worsen\\\\n- Token-independent (π0.5 Goal/Long): data collecting, expected smaller amplification\\\\n\\\\n**CV remains the primary Axis-1 diagnostic** — predicts both pruning tolerance and optimal strategy (Claim 5). Task complexity (Axis 2) explains within-model variance across suites that the old taxonomy could not capture.\\\\n\\\\n_Original per-connector evidence (from Object-suite 4-class taxonomy) retained below; reinterpret through 2-axis lens:_\\\\n- **Linear projection** (π0 3.3B, π0.5 4B): **\\\\\\\"Uniformly Critical\\\\\\\" (D139)**. NOT immune. π0.5 baseline=98.2%, random k=0.5=**69.4%** (-28.8pp), L2norm k=0.5=**33.4%** (-64.8pp). Gap=+36.0pp, random wins 9/10 tasks. Low CV (0.038/0.055) = uniformly important tokens → L2norm's systematic bias selects spatially clustered tokens → catastrophic at k≤0.7. Random preserves spatial coverage → 2× better at k=0.5. **L2norm extended curve:** k=0.1=2.6% (collapse) → k=0.3=51.0% → k=0.5=33.4% (valley) → k=0.7=55.0% → k=0.9=98.2%. V-shape with collapse at extreme compression. CV=0.055 makes this the extreme case of the monotonic diagnostic trend. **⚠️ MAJOR FINDING (2026-05-22, fully investigated):** π0.5 random pruning exhibits sharp cliff at k=0.85-0.925 with non-monotonic recovery:\\\\n  - k=0.95: 71.1% FINAL (seed42 500ep; seed43=72.8%) — already 27pp below baseline\\\\n  - k=0.925: **27.6%** FINAL (seed42) — cliff entry point, 43pp drop from k=0.95\\\\n  - k=0.9: 10.8%±1.2pp (dual seed: seed42=12.0%, seed43=9.6%) — **87.4pp gap vs L2norm k=0.9=98.2%**\\\\n  - k=0.85: **5.0%** FINAL (seed42 v2=4.4%) — cliff floor\\\\n  - k=0.7: 75.5% (mean), k=0.5: 68.9%, k=0.3: 36.4% — recovery zone\\\\n  - Cliff profile: 71.1%(k=0.95) → 27.6%(k=0.925) → 10.8%(k=0.9) → 5.0%(k=0.85) — 66pp collapse over 10% keep ratio change\\\\n  **D151 (2026-05-22): Cliff is RANDOM-SPECIFIC.** L2norm maintains 98.0-99.2% plateau across the entire cliff zone:\\\\n  - L2norm k=0.95=98.2%, k=0.925=99.2%, k=0.9=98.2%, k=0.85=98.0% — zero degradation\\\\n  - Random k=0.925: 27.6% vs L2norm=99.2% → **71.6pp gap** (maximum separation)\\\\n  - Random k=0.85: 5.0% vs L2norm=98.0% → **93.0pp gap**\\\\n  - L2norm succeeds because deterministic selection consistently retains the same token subset; random sampling creates variable damage\\\\n  **D152 (2026-05-22): Cliff is TASK-SPECIFIC.** Object tasks collapse catastrophically, Spatial tasks degrade but survive:\\\\n  - Random k=0.9: Object=10.8% vs Spatial=54.6% — Spatial retains 5× more SR\\\\n  - Random k=0.85: Object=5.0% vs Spatial=TBD (collecting)\\\\n  - Within Object suite: all 10 tasks collapse at k=0.9 (2-16%). Within Spatial suite: degradation but not catastrophic.\\\\n  - Mechanism: Object tasks require precise object identity discrimination (visually similar objects); Spatial tasks rely on spatial layout (more distributed visual information). Random token loss destroys fine-grained discriminative features needed for Object before destroying spatial layout features.\\\\n  **Fixed-mask experiment (D149) NEGATES temporal inconsistency hypothesis:** per-episode fixed mask T0=12% = per-call random T0=12%. Temporal mask variation is NOT the cause.\\\\n  **D153: Cross-suite LIBERO-Spatial — weaker non-monotonicity, no catastrophic dip (2026-05-22)**\\\\n  Baseline: 97.2%. Random pruning profile:\\\\n  | k | Object | Spatial | Δ | Pattern |\\\\n  |---|--------|---------|---|---------|\\\\n  | 0.95 | 71.1% | deploying | — | — |\\\\n  | 0.925 | 28.8% (2-seed) | — | — | — |\\\\n  | 0.9 | 10.8% | 54.6% | +43.8pp | Spatial 5× more robust |\\\\n  | 0.85 | 5.0% | **58.4%** | **+53pp** | Maximum divergence |\\\\n  | 0.7 | 75.5% | 74.4% | -1pp | Suite-independent |\\\\n  | 0.5 | 69.4% | 71.6% | +2pp | Suite-independent |\\\\n  | 0.3 | 36.4% | 49.6% | +13pp | Spatial more robust |\\\\n  L2norm Spatial: k=0.9=95.0%, k=0.7=67.0%, k=0.5=55.6%, k=0.3=57.2%. L2norm k=0.95/k=0.85 deploying.\\\\n  **Object has deep V-shape dip**: 5%(k=0.85) → 10.8%(k=0.9) → 75.5%(k=0.7), 70pp recovery from cliff floor. **Spatial has weaker non-monotonicity**: k=0.5(71.6%) > k=0.85(58.4%) > k=0.9(54.6%), but no catastrophic collapse — floor stays above 50% vs Object's 5% floor. The cliff zone gap (Object 5% vs Spatial 58%) reflects concentrated vs distributed critical token patterns.\\\\n  **Mechanism**: Object tasks have **concentrated** critical tokens (object identity discrimination — visually similar objects). Random removal at cliff zone destroys these concentrated patches → catastrophic. Spatial tasks have **distributed** critical information (layout patches spread across image). Random removal damages any random subset but never completely destroys spatial signal → graceful degradation.\\\\n  **Paper value**: Two distinct cliff behavior modes — **concentrated-critical (Object)** vs **distributed-critical (Spatial)** — as a function of task semantics. Pruning sensitivity = f(connector, method, k, task_semantics). Suite-independent at moderate k (0.5-0.7), suite-dependent at cliff zone (0.85-0.95).\\\\n  **Paper value:** strengthens \\\\\\\"uniformly critical\\\\\\\" class — even uniform importance distribution doesn't make pruning safe. Simple deletion fails; learned compression (VTR) needed.\\\\n- **Linear projection + deep post-processing** (X-VLA 880M, linear proj + 12-layer BART encoder): robust k≥0.9 (97.6% SR), **cliff at k=0.7 (56.2% SR, -43pp)**. BART encoder introduces non-linear mixing that creates partial token dependencies. CV=0.151. **D127: random pruning k=0.9=97.8% ≈ L2norm 97.6% — pruning method independence confirmed for low-CV connectors.**\\\\n- **Multi-layer MLP** (OpenVLA 7B, OpenVLA-OFT 7B): graded degradation. k=0.1 normalized loss = 1.608 (+61%). Non-linear mixing creates partial dependencies. OFT entropy (0.667) ≈ Standard (0.661), CV(OFT)=0.219 ≈ CV(OpenVLA)=0.215, confirming connector — not action head — determines attention structure. **D136: OFT LIBERO eval infeasible (Blackwell GPU SDPA incompatibility, requires A100+torch2.2). OFT included via CV/entropy analysis only; cite official baseline ~97% SR.** π0.5 baseline confirmed 98.2% (D135).\\\\n- **Pixel-shuffle** (SmolVLA 450M): catastrophic cliff-edge. k=0.95 (removing 5%) → 0% SR. Spatial folding creates irreversible entanglement. **D147: Official HF checkpoint (HuggingFaceVLA/smolvla_libero) confirms identical cliff — random k=0.95 = 0%, L2norm k=0.95 = 0%. Cliff is architectural, not training artifact. Resolves W-C2.** **Dual-seed confirmed (2026-05-22):** Baseline 59.4%±0.3pp (seed42=59.2%, seed43=59.6%), random k=0.95: 0.1% mean (0.0%/0.2%), random k=0.5: 0.0%, L2norm k=0.95: 0.2% mean (0.4%/0.0%). All pruning ≤0.2% across both seeds. cqa1 supplementary: L2norm k=0.7=0%, random k=0.9=0%.\\\\n\\\\nKey controlled comparison: π0 (256 tokens, linear) vs OpenVLA (256 tokens, 3-layer MLP) — same token count, same encoder lineage, only connector differs. k=0.1: π0 improves 2.4% vs OpenVLA degrades 61%. This isolates connector as the causal factor.\\\\n\\\\nLearned re-encoding (VTR) overcomes the cliff-edge: cross-attention 60.1±1.3% and MLP adapter 63.4±2.6% at M=32 (vs 0% hard pruning), with M=128 passthrough (58.0%±3.5, 3-seed) ≈ baseline 59.2% — VTR recovers to baseline rather than exceeding it. SmolVLA M-curve confirmed flat (D105): M=16 (56.9%±1.3) = M=128 (58.0%±3.5), all 5 M-values within ±3pp of baseline 59.2%. VTR achieves near-lossless compression at any ratio (0-87.5%) for pixel-shuffle connectors.\\\\n\\\\n## Paper Identity (Round 5 Upgrade — D171 2-Axis, 2026-05-22)\\\\n**ANALYSIS + METHOD paper.** (D091 → D097 → D171: 5 models × 3 connector families × 4 LIBERO suites)\\\\n\\\\n**Analysis contribution (primary)**: First systematic study revealing that VLA token pruning robustness is determined by the interaction of two axes: (1) connector architecture (token-independent vs token-entangling, diagnosed by importance CV 0.038→0.314) and (2) task complexity (simple vs multi-step). Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio. 5 models × 4 suites × 4 model sizes (450M-7B) eliminate confounds. No competing work does cross-architecture, cross-task VLA token analysis.\\\\n\\\\n**Method contribution**: Diagnose-then-Compress framework:\\\\n- Step 1: **Connector Compressibility Diagnostic** (D104: resolved)\\\\n  - **Primary metric: Importance CV** (token importance heterogeneity) — zero-cost, one forward pass\\\\n  - CV forms continuous spectrum predicting pruning tolerance: π0=0.038 < π0.5=0.055 < X-VLA=0.151 < OpenVLA=0.215 < OFT=0.219 < SmolVLA=0.314\\\\n  - ⚠️ D106+: X-VLA CV=0.151 correctly predicted its intermediate pruning behavior (k=0.7 ≈50% SR ≈ OpenVLA k=0.7). CV is a valid continuous predictor, NOT a 3-class discrete classifier.\\\\n  - **Key discovery**: X-VLA \\\\\\\"linear projection\\\\\\\" passes through BART encoder (12 transformer layers) before decoder → introduces non-linear mixing → explains CV=0.151 (much higher than π0=0.038 pure linear)\\\\n  - **Entropy as mechanistic supplement** (CV is primary; entropy is supplementary):\\\\n    - π0: entropy=0.959 (per-layer mean, range 0.931–0.983), CV=0.038 — uniform & independent → most tolerant\\\\n    - **π0.5: entropy=0.666, CV=0.055** — similar entropy to OpenVLA (0.661) but vastly different pruning behavior (CV correctly differentiates)\\\\n    - X-VLA: entropy=0.614, CV=0.151 — selective & BART-mixed → intermediate\\\\n    - OpenVLA: entropy=0.661, CV=0.215 — selective & MLP-mixed → graded\\\\n    - SmolVLA: entropy=0.952, CV=0.314 — near-uniform but spatially entangled → catastrophic\\\\n  - **KEY INSIGHT**: Entropy clusters π0.5/X-VLA/OpenVLA together (0.61-0.67) despite very different pruning behaviors. CV correctly separates them (0.055 vs 0.151 vs 0.215). Entropy fails as diagnostic because it doesn't capture token independence structure — only attention distribution shape.\\\\n  - ✅ Batch 2 complete: continuous CV spectrum confirmed (X-VLA full 8-point curve validates threshold-graded class)\\\\n  - Supplementary: lightweight pruning probe (remove 5%, one forward pass) as practitioner-friendly alternative\\\\n- Step 2: VTR (Vision Token Re-encoding) — lightweight cross-attention module (~22M params) for universal compression\\\\n- For entangled tokens (pixel-shuffle): recovers from 0% (hard pruning) to ~59% ≈ baseline, M-curve flat D105 (near-lossless compression at any ratio 0-87.5%)\\\\n- For independent tokens (MLP projector): **D109 C4-ext confirmed 0% SR** at 20K steps (M=128, severe overfitting — model outputs identical action every step). VTR on MLP projector does NOT improve SR; reframed as \\\\\\\"VTR ceiling depends on connector type\\\\\\\" finding. User directive: performance degradation acceptable if efficiency improves — VTR value is 75% KV-cache reduction + attention speedup. VTC-only M=32/M=64 training in progress to test whether smaller M values fare better.\\\\n\\\\n**Differentiation from concurrent work**: 4 concurrent works (Compressor-VLA, SpecPrune-VLA, LightVLA ICRA'26, See What Matters ICML'26) all propose pruning on MLP-projector VLAs. We (1) explain why pruning fails on pixel-shuffle architectures, (2) identify why pruning succeeds on linear projection (tokens are truly independent), and (3) propose a re-encoding method motivated by the diagnostic analysis.\\\\n\\\\n**Model coverage**: 5 VLA models × 3 connector families × 4 LIBERO suites × 4 model sizes (450M-7B). RC1 (only 2 models), RC2 (size confound), and RC7 (only one suite) fully addressed.\\\\n\\\\n## Core Claims (5 claims, expanded from 4)\\\\n\\\\n### Claim 1: 2-Axis Compressibility Framework (D107 → D171 UPGRADED)\\\\nPruning sensitivity = f(connector_architecture, task_complexity). Two axes interact:\\\\n\\\\n**Axis 1 — Token Coupling (connector determines base sensitivity):**\\\\n- **Token-independent** connectors (pure linear π0/π0.5, MLP OpenVLA/OFT): tokens retain spatial meaning → pruning damage is local, graded degradation\\\\n- **Token-entangling** connectors (BART X-VLA, pixel-shuffle SmolVLA): cross-token dependencies → pruning damage cascades\\\\n\\\\n**Axis 2 — Task Complexity (task amplifies entangling-connector sensitivity):**\\\\n- Simple tasks (Object): even entangling connectors tolerate mild pruning (X-VLA k=0.9=97.6%)\\\\n- Complex tasks (Goal/Long): entangling connectors collapse (X-VLA Goal k=0.9=70.2%, Long k=0.95≈53%)\\\\n- Key: same connector, same k, same method — **only task differs** → 27.8pp drop (Object→Goal)\\\\n\\\\n**CV predicts Axis-1 position**: 0.038 (most independent) → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 (most entangled)\\\\n\\\\n**Evidence**: 5 models, 3 connector families, 4 LIBERO suites, 4 model sizes (450M-7B). Key controlled comparisons:\\\\n1. π0 (256 tokens, linear) k=0.1 = 0.976 vs OpenVLA (256 tokens, MLP) k=0.1 = 1.608 → connector isolates base sensitivity\\\\n2. X-VLA Object k=0.9 = 97.6% vs X-VLA Goal k=0.9 = 70.2% → task complexity isolates amplification\\\\n3. SmolVLA Object = 0% at k=0.95 → extreme entanglement dominates even on simple tasks\\\\n\\\\n🔴 **D108→D127→D130→D132: Pruning method comparison — MAJOR REVERSAL at aggressive compression**\\\\n\\\\nBoth L2 norm and random pruning tested on X-VLA and OpenVLA. **CV predicts not just tolerance but optimal strategy**:\\\\n\\\\n- **OpenVLA (MLP, CV=0.215)**: L2 norm consistently ≥ random at all k values. High CV → meaningful importance differentiation → L2 norm selection effective.\\\\n  - k=0.95: L2norm=69.4% ≈ random=69.2% (+0.2pp)\\\\n  - k=0.7: L2norm=49.8%¹ > random=44.4% (+5.4pp). ¹seed43 only, seed42 running on westd-38929:2\\\\n  - k=0.5: L2norm=39.2% > random=35.8% (+3.4pp)\\\\n  - k=0.3: L2norm=25.0%, random=pending (re-running)\\\\n\\\\n- **X-VLA (BART, CV=0.151)**: 🔴 **REVERSAL** — L2 norm ≈ random at mild compression, but **random MASSIVELY outperforms L2 norm at aggressive compression**:\\\\n  - k=0.9: L2norm=97.6% ≈ random=97.8% (≈0pp)\\\\n  - k=0.85: L2norm=68.0% > random=63.6% (+4.4pp, cliff boundary)\\\\n  - k=0.8: L2norm=89.0% ≈ random=89.4% (≈0pp, non-monotonic recovery)\\\\n  - **k=0.5: L2norm=42.6% << random=70.6% (-28.0pp!)** — CI non-overlapping, statistically significant. Random wins 9/10 tasks; T4 ketchup: L2norm=42% vs random=100% (+58pp). Only T6 butter both crash at 2%.\\\\n  - k=0.7: L2norm=56.2% << random=65.2% (+9pp). Crossover confirmed at k≈0.8.\\\\n  - **k=0.3: L2norm=22.8% << random=62.8% (+40pp!)** — gap scales monotonically with compression.\\\\n  - **D137**: seed43 k=0.5=71.0% confirms seed42=70.6% (Δ=0.4pp). Gap reproducible.\\\\n\\\\n- **SmolVLA**: all methods = 0% at all k values → trivially method independent.\\\\n\\\\n**KEY INSIGHT (D132→D137)**: Importance-based pruning can be **actively harmful** on low-CV architectures under aggressive compression, and the harm SCALES: +9pp@k=0.7, +28pp@k=0.5, +40pp@k=0.3. Mechanism: X-VLA's linear projection + BART encoder produces relatively uniform token norms (CV=0.151). L2 norm selection on a near-uniform distribution degenerates into selecting spatially clustered tokens → loses diversity → catastrophic failure. Random pruning preserves spatial coverage → dramatically better. Multi-seed confirmed.\\\\n\\\\n**This strengthens the paper**: CV serves as a dual predictor — predicts both (1) pruning tolerance ceiling and (2) whether importance-based methods help or hurt. Connector architecture determines both via its effect on token importance distribution.\\\\n\\\\n**Paper narrative upgrade**: From \\\\\\\"connector determines compressibility\\\\\\\" to \\\\\\\"connector determines both compressibility AND optimal compression strategy.\\\\\\\" This is a significantly stronger and more novel contribution.\\\\n\\\\n**Pending data**: X-VLA random k=0.7 (crossover characterization), multi-seed k=0.5 random (robustness). OpenVLA L2norm k_ratio=null provenance issue needs fixing.\\\\n\\\\n### Claim 2: Pixel Shuffle Creates Irreversible Token Entanglement\\\\nSmolVLA's pixel_shuffle connector spatially folds 1024 SigLIP patches into 64 tokens per camera (16x compression). Each resulting token encodes a 32x32 pixel region via channel-to-spatial reorganization. This creates extreme cross-token spatial entanglement: removing any single token eliminates an entire spatial quadrant's information with no redundancy to compensate.\\\\n\\\\n**Evidence**:\\\\n- k=0.95 (remove only 7/128 tokens = 5.5%) = 0% SR — even minimal removal is catastrophic\\\\n- k=0.9 (remove 13/128 tokens) = 0% SR\\\\n- Geometric prior (Sobel edge) k=0.5/0.7/0.9 = all 0%\\\\n- Attention entropy ratio 0.952 (near-uniform, TV=0.05)\\\\n- Official checkpoint Object (59.2% baseline) cliff-edge at k=0.5 → 0%\\\\n- Official checkpoint Spatial (43.8% baseline) cliff-edge at k=0.5 → 0.6% (3/500, CI [0.2%, 1.7%])\\\\n\\\\n### Claim 3a: Linear Projection → Depends on Effective Pipeline (D107: RESOLVED)\\\\nPure linear projection (π0): immune. Linear projection + deep post-processing (X-VLA, BART 12L): \\\\\\\"robust-then-cliff\\\\\\\" — immune at k≥0.9, cliff at k=0.7, then graded degradation. The BART encoder introduces non-linear cross-token mixing that explains intermediate CV=0.151 and the cliff pattern.\\\\n\\\\n**Evidence** (X-VLA LIBERO SR — Batch 1 + Batch 2 COMPLETE, full 8-point curve):\\\\n- k=1.0: **99.2%** (baseline, 496/500) — per-task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]\\\\n- k=0.95: **99.0%** (-0.2pp) — per-task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]\\\\n- k=0.9: **97.6%** (-1.6pp) — per-task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]\\\\n- k=0.7: **56.2%** (-43pp, CLIFF — 281/500) — per-task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]\\\\n- k=0.5: **42.6%** (-57pp) — Batch 2 confirmed (MSH fix applied)\\\\n- k=0.3: **23.0%** (-77pp) — graded degradation continues below cliff\\\\n- k=0.2: **~4.0%** (-96pp) — near-zero\\\\n- k=0.1: **~0.0%** (-100pp) — complete failure\\\\n✅ Full curve confirms threshold-graded pattern: immune k≥0.9, cliff at k=0.7, then graded degradation k≤0.5 (42.6%→23.0%→~4%→~0%).\\\\n\\\\n**Cliff localization (D114, D117: 3-seed deterministic, L2norm)**:\\\\n- k=0.80: **89.0% ± 0.72pp** (seeds: 88.8/88.4/89.8)\\\\n- k=0.85: **67.9% ± 0.31pp** (seeds: 68.0/67.6/68.2 — T4=26%, T6=0% across ALL 3 seeds)\\\\n- Non-monotonic: k=0.85 < k=0.80 by **21.1pp**. BART encoder creates length-dependent interactions near critical token density. SD < 1pp confirms fully deterministic, not stochastic.\\\\n\\\\n**Random pruning comparison (D127-D130, D132 REVERSAL)**:\\\\n- k=0.9: random=97.8% ≈ L2norm=97.6% → method independent at mild compression\\\\n- k=0.85: random=63.6% vs L2norm=68.0% (+4.4pp for L2norm at cliff boundary). Both crash on same tasks (T1, T4, T6, T8) → cliff is architectural.\\\\n- k=0.8: random=89.4% ≈ L2norm=89.0% → method independent, non-monotonic recovery confirmed in both\\\\n- 🔴 **k=0.5: random=70.6% >> L2norm=42.6% (+28pp REVERSAL, CI non-overlapping)**. Per-task random: [96, 46, 100, 92, 100, 94, 2, 82, 42, 100]. Random wins 9/10 tasks; L2norm actively harmful. T4: random=100% vs L2norm=42% (+58pp).\\\\n- k=0.7: random=65.2% vs L2norm=56.2% (+9pp random). Crossover confirmed at k≈0.8.\\\\n- 🔴 **k=0.3: random=62.8% vs L2norm=22.8% (+40pp!)** — gap SCALES with compression: +9@k=0.7, +28@k=0.5, +40@k=0.3.\\\\n- **D137 multi-seed confirmed**: seed43 k=0.5=71.0% (seed42=70.6%, Δ=0.4pp). Gap is reproducible.\\\\n- **Random non-monotonicity confirmed**: k=0.5 (70.6%) > k=0.7 (65.2%) > k=0.3 (62.8%). seed43 reproduces (71.0%). L2norm monotonically decreasing (42.6% > 22.8%). Random's k=0.5 \\\\\\\"sweet spot\\\\\\\" may reflect optimal diversity-coverage tradeoff: enough tokens removed to break BART clustering, but enough retained for spatial coverage.\\\\n- k=0.85 per-task (random): [100, 10, 100, 94, 24, 92, 0, 94, 22, 100] = 63.6%.\\\\n- **Non-monotonicity confirmed in both methods**: k=0.85 (42 tokens) cliff vs k=0.8 (40 tokens) recovery. 2-token difference, 21-26pp gap.\\\\n- **D132 KEY INSIGHT**: At aggressive compression (k=0.5), L2 norm is catastrophically worse than random for X-VLA. Low CV=0.151 → near-uniform importance → L2 norm degenerates into spatially clustered selection → loses diversity. This is the opposite of OpenVLA (CV=0.215) where L2 norm helps. **CV predicts optimal pruning strategy, not just tolerance.**\\\\n\\\\n**Cross-suite generalization (D117, updated with full results)**:\\\\n- X-VLA Spatial baseline: **91.6%** [88.8%, 93.7%] (500 eps, T5=48% is hardest task)\\\\n- X-VLA Goal baseline: **98.0%** [96.4%, 98.9%] (500 eps, all tasks ≥92%)\\\\n- X-VLA-Libero checkpoint covers all 4 suites without suite-specific fine-tuning.\\\\n\\\\n**⚠️ Cross-suite pruning sensitivity (key finding — potential new contribution)**:\\\\n\\\\nX-VLA pruning curve comparison across suites:\\\\n\\\\n| Suite | k=1.0 | k=0.9 | k=0.85 (L2/Rand) | k=0.8 (L2/Rand) | k=0.7 (L2/Rand) | k=0.5 (L2/Rand) |\\\\n|-------|-------|-------|-----|-------|----------|----------|\\\\n| Object | 99.2% | 97.8% | 68.0/63.6% | 89.0/89.4% | 56.2/65.2% | 42.6/**70.6%** |\\\\n| Spatial | 91.6% | 79.0% | 66.6/67.6% | — | — | 58.8%/**71.4%** |\\\\n| Goal | 98.0% | 70.2% | — | — | — | 61.0%/— |\\\\n\\\\n**Goal suite FINAL results (10/10 tasks, D123: suite-level monotonic confirmed)**:\\\\n- k=0.9: **70.2%** (351/500) — much larger drop than Object (-1.4pp) despite similar baseline\\\\n- k=0.5: **61.0%** (305/500) — suite-level monotonic (k=0.9 > k=0.5), D123 retracted earlier partial-data non-monotonic claim\\\\n\\\\n**Per-task non-monotonic pruning remains valid (selected tasks)**:\\\\n\\\\n| Task | k=1.0 | k=0.9 | k=0.5 | Pattern |\\\\n|------|-------|-------|-------|---------|\\\\n| T0 open drawer | 100% | 100% | 82% | monotonic ↓ |\\\\n| T2 close drawer | 94% | 96% | **100%** | **pruning improves** |\\\\n| T3 open+put (multi-step) | 100% | **6%** | **40%** | catastrophic + non-monotonic (k=0.5 > k=0.9) |\\\\n| T8 | — | — | — | +46pp non-monotonic (k=0.5 > k=0.9) |\\\\n| T9 | 98% | — | ~0% | catastrophic collapse (-98pp) |\\\\n\\\\n- Suite-level: Goal k=0.5=61.0% > Spatial k=0.5=58.8% — Goal slightly more robust, but both moderate degradation\\\\n- Per-task: T3/T8 show non-monotonicity (k=0.5 > k=0.9), T9 catastrophic collapse. These are genuine misalignments between global L2-norm ranking and task-specific token utility.\\\\n- T2 pruning improvement: consistent with π0 finding — simple tasks benefit from token noise removal\\\\n\\\\n**Key cross-suite finding**: Goal k=0.9 drops **27.8pp** (vs Object -1.4pp). Same connector, same pruning method, different task distribution → **task complexity amplifies pruning sensitivity**. Goal tasks involve multi-step reasoning that depends heavily on precise spatial tokens.\\\\n\\\\n**Task-level analysis (Spatial, k=0.5 vs baseline)**:\\\\n- Robust (Δ≤10pp): T0 \\\\\\\"between plate and ramekin\\\\\\\" (-4pp), T4 \\\\\\\"in top drawer\\\\\\\" (-2pp) — global spatial / unambiguous target\\\\n- Moderate (Δ 10-30pp): T2(-10), T3(-24), T6(-22), T8(-18) — mild spatial precision needed\\\\n- Catastrophic (Δ>40pp): T5 \\\\\\\"on ramekin\\\\\\\" (-48pp, 0%), T9 \\\\\\\"on cabinet\\\\\\\" (-58pp), T7 \\\\\\\"on stove\\\\\\\" (-64pp), T1 \\\\\\\"next to ramekin\\\\\\\" (-78pp)\\\\n- **T1 has 100% baseline but 22% at k=0.5** — high baseline ≠ pruning robustness\\\\n\\\\n**Mechanism**: Goal tasks are semantically diverse (different verbs/objects) → language instruction alone disambiguates → vision tokens are redundant for task selection. Spatial tasks are semantically near-identical (all \\\\\\\"pick bowl...\\\\\\\") → disambiguation relies entirely on spatial vision tokens → pruning destroys the only discriminative signal.\\\\n\\\\n**Paper framing upgrade (Reviewer suggestion, agreed)**:\\\\n- From \\\\\\\"connector determines pruning tolerance\\\\\\\" → \\\\\\\"pruning sensitivity = f(connector_type, task_semantics)\\\\\\\"\\\\n- Connector CV predicts degradation *class* (immune/threshold/graded/catastrophic)\\\\n- Task semantic structure determines degradation *severity* within that class\\\\n- When language disambiguates: aggressive pruning is safe (Goal k=0.5 ≈ baseline)\\\\n- When spatial vision disambiguates: even conservative pruning degrades (Spatial k=0.9 -12.6pp)\\\\n- **Potential new contribution**: first task-level pruning sensitivity analysis in VLAs. §4.6 should include per-task heatmap + the language-vs-spatial disambiguation framework.\\\\n\\\\nπ0 evidence:\\\\n- π0 (3.3B, 256 tokens, pure linear proj): k=0.1 normalized_L1 = 0.976 (-2.4% = improvement), k=0.5 = 0.983\\\\n- Attention entropy: π0 suffix-to-vision mean 0.959 (near-uniform across 18 layers, range [0.931, 0.983])\\\\n- Importance CV: π0 = 0.038 (lowest in spectrum)\\\\n\\\\n**Key insight**: \\\\\\\"Linear projection\\\\\\\" is NOT sufficient for immunity. The effective pipeline matters. X-VLA's BART encoder (12 transformer layers after linear proj) introduces partial dependencies → CV=0.151 → cliff at k=0.7. π0's pure linear proj → CV=0.038 → immune even at k=0.1.\\\\n\\\\n### Claim 3b: MLP Projector → Graded Degradation\\\\nMulti-layer MLP connectors create partial token dependencies through non-linear mixing, enabling graceful but real degradation.\\\\n\\\\n**Evidence** (OpenVLA 6-point degradation curve):\\\\n- k=1.0: 74.0% (baseline)\\\\n- k=0.95: 69.4% (-6% relative)\\\\n- k=0.9: 62.0% (-16% relative)\\\\n- k=0.7: 49.0% (-34% relative)\\\\n- k=0.5: 37.4% (-49% relative)\\\\n- k=0.3: 20.6% (-72% relative)\\\\n- Entropy ratio 0.639 (progressive sharpening L0=0.98→L29=0.48, TV=0.50)\\\\n- **Method independence confirmed**: random k=0.95=69.2% ≈ L2norm k=0.95=69.4%; random k=0.5=35.8% ≈ L2norm k=0.5=37.4%. For MLP projectors, pruning method doesn't matter.\\\\n- OFT (same connector, different action head): entropy 0.667 ≈ Standard 0.661 → connector determines attention structure, not action head\\\\n- CogACT (MLP projector, literature): 74.8% → 74.2% under 78% pruning (EfficientVLA)\\\\n\\\\n### Claim 4: Learned Re-Encoding Achieves Near-Lossless Compression Where Deletion Fails (D072+MLP confirmed → upgraded to METHOD per D091)\\\\n**⚠️ Baseline correction (2026-05-22): SmolVLA Object baseline = 59.2% (official HF checkpoint), NOT 44.8% (old reproduced). VTR narrative reframed from \\\\\\\"re-encoding boost\\\\\\\" to \\\\\\\"near-lossless compression recovery\\\\\\\".**\\\\n\\\\nTwo independent re-encoding architectures (~22M params each) validate that **any learned re-encoding** can recover entangled pixel_shuffle tokens from 0% (hard pruning) to near-baseline levels. Cross-attention (60.1±1.3%, 3-seed) and MLP adapter (63.4±2.6%, 3-seed) both achieve this recovery, with p≈0.15 confirming no significant difference between architectures. M=128 passthrough (58.0±3.5%, 3-seed) ≈ baseline 59.2% (-1.2pp), confirming VTR recovers to baseline rather than exceeding it. **M-curve is flat**: M=16 (56.9%) through M=128 (58.0%), all within ±3pp of baseline 59.2% — VTR achieves near-lossless compression at ANY ratio (0-87.5%) for pixel-shuffle connectors. M=64 achieves best absolute SR at 62.0±2.3% (+2.8pp over baseline) with 50% compression. Cross-suite generalization confirmed: M=32 recovers to 53.2% on Spatial (vs 0.6% pruning cliff-edge) and 56.4% on Goal. M=96 dip statistically confirmed (p=0.034 vs M=64).\\\\n\\\\n**D109 C4-ext on OpenVLA (MLP projector)**: M=128 VTR at 20K steps = **0% SR** (severe overfitting, model outputs identical action every step). This suggests VTR's effectiveness is connector-dependent: pixel-shuffle benefits enormously (0%→~59% ≈ baseline) because re-encoding repairs spatial entanglement, while MLP projector tokens are already individually meaningful and VTR adds unnecessary complexity. VTC-only M=32/M=64 training in progress — if these also fail, VTR is specifically a pixel-shuffle solution, which strengthens the architecture-dependency narrative.\\\\n\\\\n**Evidence** (all confirmed):\\\\n\\\\nCross-attention re-encoding (M sweep, 3-seed where available):\\\\n| M | Compression | SR (3-seed mean±std) | Seeds | Notes |\\\\n|---|------------|-----|-----|-----|\\\\n| 16 | 87.5% | **56.9±1.3%** | 42/43/44 | ✅ ZERO loss vs M=128 |\\\\n| 32 | 75% | **60.1±1.3%** | 42/43/44 | ✅ |\\\\n| 64 | 50% | **62.0±2.3%** | 42/43/44 | ✅ best tradeoff |\\\\n| 96 | 25% | 54.5±3.2% | 42/43/44 | ✅ highest variance |\\\\n| 128 | 0% (passthrough) | **58.0±3.5%** | 42/43/44 | ✅ passthrough control |\\\\n\\\\nMLP adapter control (M=32, ~22.14M params, 3-seed):\\\\n| Architecture | Params | M | Mean SR (3-seed) | Std | Individual seeds |\\\\n|---|---|---|-----|-----|-----|\\\\n| Cross-attention (VTC) | 22.2M | 32 | **60.1%** | ±1.3 | 61.6 / 59.2 / 59.6 |\\\\n| **MLP adapter** | **22.14M** | **32** | **63.4%** | **±2.6** | **65.2 / 64.6 / 60.4** |\\\\n\\\\nTwo-sample t-test: t≈1.94, p≈0.15 → **no significant difference** (α=0.05). Both >> 0% (hard pruning) and ≈ 59.2% (baseline). MLP ≥ VTC in all 3 seeds but difference not statistically significant — confirms any re-encoding architecture recovers to near-baseline, not a specific mechanism. (Note: M=32 seed43 corrected from 62.4% to 59.2% per registry verification; 62.4% was M=96 seed43 CI upper bound misattributed.)\\\\n\\\\n### Claim 5: CV Predicts Optimal Pruning Strategy — Monotonic Diagnostic Trend (D132→D139→D140→D142)\\\\nToken importance CV determines **which pruning method to use**, with the L2norm-vs-random gap scaling monotonically with CV. **Validated at TWO k values (D142):**\\\\n\\\\n**k=0.5 (main table):**\\\\n| Model | CV | Tokens | L2norm k=0.5 | Random k=0.5 | Δ (R-L2) |\\\\n|-------|-----|--------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | **33.4%** | **69.4%** | **+36.0pp** |\\\\n| X-VLA | 0.151 | 50 | 43.4%³ | 70.3%⁴ | +26.9pp |\\\\n| OpenVLA | 0.215 | 256 | 39.2% | 37.4%¹⁰ | -1.8pp |\\\\n\\\\n**k=0.7 (second validation, D142):**\\\\n| Model | CV | Tokens | L2norm k=0.7 | Random k=0.7 | Δ (R-L2) |\\\\n|-------|-----|--------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | **55.0%** | **77.2%** | **+22.2pp** |\\\\n| X-VLA | 0.151 | 50 | 58.6%⁶ | 65.1%⁷ | +6.5pp |\\\\n| OpenVLA | 0.215 | 256 | 49.8% | 44.4% | -5.4pp |\\\\n⁶ X-VLA L2norm k=0.7 2-seed: 58.2/59.0, mean=58.6%, σ=0.4pp (seed44 pending → tri-seed)\\\\n⁷ X-VLA random k=0.7 2-seed: 65.2/65.0, mean=65.1%, σ=0.1pp (seed44 running)\\\\n\\\\n³ X-VLA L2norm k=0.5 3-seed mean: 42.6/43.4/44.2, mean=43.4%, range 1.6pp\\\\n⁴ X-VLA random k=0.5 3-seed mean: 70.6/71.0/69.2, mean=70.3%, σ=0.9pp\\\\n\\\\n¹⁰ OpenVLA random k=0.5 = 37.4% (seed7). Table 3 previously showed 35.8% (unverified source). seed42 running on westd-38929, will replace when available.\\\\n\\\\n✅ **D139+D142 CONFIRMED**: Monotonic trend validated at BOTH k=0.5 (-1.8→+26.9→+36.0) and k=0.7 (-5.4→+6.5→+22.2). Same monotonic pattern. Paper: k=0.5 as main table, k=0.7 as confirmatory second row or separate table.\\\\n\\\\n**D140: k=0.3 interaction — method preference REVERSES at extreme compression for π0.5:**\\\\n\\\\n| Model | CV | Tokens | k=0.3 kept | L2norm k=0.3 | Random k=0.3 | Δ (R-L2) |\\\\n|-------|-----|--------|-----------|-------------|-------------|----------|\\\\n| π0.5 | 0.055 | 768 | 230 | **51.0%** | 36.4% | **-14.6pp** |\\\\n| X-VLA | 0.151 | 50 | 15 | 22.2%⁸ | **64.5%⁹** | **+42.3pp** |\\\\n| OpenVLA | 0.215 | 256 | 77 | 25.0% | **21.4%** | **+3.6pp** |\\\\n\\\\n⁸ X-VLA L2norm k=0.3 3-seed: 22.2/21.0/22.8 (from D137), mean=22.0%; seed43 running on cqa1\\\\n⁹ X-VLA random k=0.3 2-seed: 62.8/66.2, mean=64.5%, σ=2.4pp; seed44 running on cqa1\\\\n\\\\nAt k=0.3, π0.5 L2norm wins (+14.6pp) while X-VLA random still wins massively (+42.3pp). OpenVLA L2norm also wins (+3.6pp). The pattern: at k=0.3, both high-CV (OpenVLA) and low-CV-with-large-budget (π0.5, 230 tokens) favor L2norm, while mid-CV-with-small-budget (X-VLA, 15 tokens) strongly favors random. Strategy preference is f(CV, k, absolute_token_budget).\\\\n\\\\n**OpenVLA (CV=0.215) full seed42 Δ(L2-R) pattern**: +1.4pp (k=0.95) → +5.4pp (k=0.7) → pending (k=0.5) → +3.6pp (k=0.3). L2norm consistently better at ALL k values — high CV enables meaningful importance-based selection. Peak advantage at k=0.7, not monotonically increasing with compression.\\\\n\\\\n**D141: π0.5 L2norm complete curve — valley at k=0.5 confirmed (multi-seed)**:\\\\n| k | L2norm SR (s42) | L2norm SR (s43) | Random SR | Δ (R-L2) s42 |\\\\n|---|-----------------|-----------------|-----------|---------------|\\\\n| 0.7 | **55.0%** | **57.8%**¹⁰ | **77.2%** / **73.8%** (mean=75.5%) | +22.2pp (s42) / +19.8pp (mean) |\\\\n| 0.5 | **33.4%** | **33.6%** ✅ | **69.4%** / **68.4%** (mean=68.9%) | +36.0pp (s42) / +35.4pp (mean) |\\\\n| 0.3 | **51.0%** | **55.4%** ✅ | 36.4% | -14.6pp |\\\\n\\\\n¹⁰ Agent audit reported 56.4% for L2norm k=0.7 seed43 vs earlier worker result 57.8%. Needs reconciliation. Pattern unchanged.\\\\n\\\\n**V-shape fully confirmed (2 seeds, both methods)**:\\\\n- **Valley (k=0.5)**: L2norm 33.4/33.6% (std=0.1pp); Random 69.4/68.4% (std=0.7pp) — both methods stable\\\\n- **2-seed means**: L2norm k=0.7=56.4%, k=0.5=33.5%, k=0.3=53.2%; Random k=0.7=75.5%, k=0.5=68.9%\\\\n- **V-depth**: seed42=17.6pp, seed43=21.8pp (seed43 deeper because endpoints higher)\\\\n- **Δ(R-L2) dual-seed means**: k=0.7=+19.8pp, k=0.5=+35.4pp — monotonic trend holds with multi-seed\\\\n- seed43 consistently +2-4pp above seed42 but identical shape. Valley position/depth is architectural determinism.\\\\n\\\\n**Mechanism confirmed by token position visualization (D141)**:\\\\n- k=0.7: 2 clusters, 97% in largest, **100% spatial coverage** — enough tokens to maintain coverage\\\\n- k=0.5: **1 cluster, 100% in single region, 78% coverage** — worst-case spatial concentration\\\\n- k=0.3: **3 clusters**, 86% in largest, 78% coverage — cluster breaks apart, better diversity\\\\n\\\\nThe non-monotonicity arises because k=0.5 sits at the worst point of the spatial correlation structure: L2norm selects exactly the number of tokens that maximizes spatial clustering. At k=0.7 there are enough tokens for coverage; at k=0.3 the selection threshold crosses a boundary that fragments the cluster. Per-task variance is extreme at k=0.7 (T1=94%, T5=98% vs T7=0%) — L2norm deterministic selection can catastrophically miss specific task-critical spatial regions.\\\\n\\\\n**Paper strategy**: k=0.5 as **main table** (cleanest monotonic trend, clear gap). Full L2norm curve as **figure** showing pathological valley — strong evidence for spatial clustering mechanism. k=0.3 reversal as supplementary. Key message: \\\\\\\"CV predicts method preference at k=0.5; L2norm's spatial clustering creates pathological non-monotonicity unique to low-CV models.\\\\\\\"\\\\n\\\\n**Notable asymmetry**: Random tolerance is similar for low/medium CV at k=0.5 (π0.5=69.4% ≈ X-VLA=70.6%), while L2norm harm increases dramatically (π0.5=33.4% < X-VLA=43.4%). High CV (OpenVLA=35.8% random) is less random-tolerant because tokens have genuine importance differentiation that random discards.\\\\n\\\\n**Evidence** (Reviewer-verified, D132 PASS):\\\\n\\\\nX-VLA vs OpenVLA full comparison:\\\\n\\\\n| k | X-VLA (CV=0.151) | | OpenVLA (CV=0.215) | |\\\\n|---|---|---|---|---|\\\\n| | L2norm | Random | L2norm | Random |\\\\n| 0.95 | — | — | 70.6% | 69.2% (+1.4 L2norm) |\\\\n| 0.9 | 97.6% | 97.8% (≈0) | 70.6% | 64.6% (+6.0 L2norm) |\\\\n| 0.85 | 68.0% | 63.6% (+4.4 L2norm) | — | — |\\\\n| 0.8 | 89.0% | 89.4% (≈0) | — | — |\\\\n| 0.7 | 56.2% | **65.2% (+9pp random)** | 49.8%¹ | 44.4% (+5.4 L2norm¹) |\\\\n| 0.5 | **42.6%** | **70.6% (+28pp random!)** | 39.2% | 35.8% (+3.4 L2norm) |\\\\n| 0.3 | **22.8%** | **62.8% (+40pp random!)** | 25.0% | pending² |\\\\n\\\\n¹ OpenVLA L2norm k=0.7 = seed43 only, random = seed42; cross-seed caveat. seed42 L2norm k=0.7 running on westd-38929.\\\\n² OpenVLA random k=0.3 result file missing, re-running on westd-38929.\\\\n³ D137 multi-seed: X-VLA random k=0.5 seed43=71.0% (seed42=70.6%, Δ=0.4pp). Gap reproducible.\\\\n\\\\n**Per-task X-VLA k=0.5 (Reviewer-verified, 9/10 tasks random > L2norm):**\\\\n\\\\n| Task | Baseline | L2 s42 | L2 s43 | Random s42 | Δ(R-L2) |\\\\n|------|---------|--------|--------|------------|---------|\\\\n| T0 alphabet_soup | 98% | 58% | 56% | **96%** | +38 |\\\\n| T1 cream_cheese | 100% | 2% | 6% | 46% | +44 |\\\\n| T4 ketchup | 100% | 42% | 40% | **100%** | **+58** |\\\\n| T7 milk | 100% | 38% | 38% | 82% | +44 |\\\\n| T9 orange_juice | 100% | 68% | 70% | **100%** | +32 |\\\\n| T6 butter | 100% | 2% | 2% | 2% | 0 (both crash) |\\\\n\\\\nL2norm two seeds highly consistent (s42 vs s43 diff <6pp) → not RNG noise.\\\\nT6: baseline=100% but both methods=2% → highly localized visual cue, k=0.5 always loses it regardless of method.\\\\nT4/T9: Random recovers to baseline → L2norm systematically discards the critical tokens for these tasks.\\\\n\\\\n**Pattern**: Low CV (X-VLA) → importance-based selection degenerates at aggressive k → random better. High CV (OpenVLA) → meaningful importance differentiation → L2 norm better.\\\\n\\\\n**Mechanism hypothesis** (Reviewer: consistent with data, needs direct evidence): X-VLA's linear projection + BART encoder produces tokens with relatively uniform L2 norms (CV=0.151). At aggressive compression (k=0.5 = keeping 25 of 50 tokens), L2 norm selects the \\\\\\\"slightly larger\\\\\\\" tokens which tend to be spatially clustered → loses spatial diversity → catastrophic. Random preserves spatial coverage stochastically → dramatically better.\\\\n\\\\n**⚠️ Visualization needed (Reviewer warning)**: Must produce token position visualization — for same input image, show which tokens L2 norm vs random retains. If L2 norm shows spatial clustering, mechanism is proven. This should be a key figure (§4.6 or Fig 4).\\\\n\\\\n**Implication for practitioners**: CV diagnoses → predicts tolerance → prescribes strategy at aggressive compression. Low CV + aggressive k (≤0.5) → random/position-based. High CV → importance-based at all k. Mild compression (k≥0.8) → method choice doesn't matter regardless of CV.\\\\n\\\\n**Pending**: X-VLA random k=0.7 (crossover), multi-seed k=0.5, token position visualization, OpenVLA L2norm k=0.7 seed42, k_ratio=null fix.\\\\n\\\\n## Story Spine\\\\n\\\\n**Problem**: Vision token efficiency is critical for real-time VLA deployment. Growing literature proposes inference-time token reduction (FastV, VLA-IAP, H2O, ToMe). These methods succeed on some VLAs but their behavior across different architectures is unstudied.\\\\n\\\\n**Gap**: No work has systematically compared token pruning robustness across VLA architectures. The implicit assumption that \\\\\\\"token pruning works or fails uniformly\\\\\\\" is untested. The critical architectural factor determining prunability is unknown.\\\\n\\\\n**Discovery**: We find that VLA token pruning robustness is governed by two interacting axes. **Axis 1 — Token Coupling**: connector architecture determines whether tokens are independent (linear proj, MLP) or entangled (BART encoder, pixel-shuffle), diagnosed by importance CV (0.038→0.314). **Axis 2 — Task Complexity**: multi-step tasks (Goal/Long) amplify pruning damage on entangling connectors — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at k=0.9. Evidence from 5 VLA models × 4 LIBERO suites:\\\\n- **Token-independent** (π0, π0.5 linear; OpenVLA, OFT MLP): graded degradation, CV 0.038–0.219\\\\n- **Token-entangling** (X-VLA BART 12L; SmolVLA pixel-shuffle): task-dependent collapse — tolerate simple tasks, catastrophic on complex tasks. CV 0.151–0.314\\\\nCV predicts both pruning tolerance and optimal strategy (L2norm hurts low-CV models, helps high-CV).\\\\n\\\\n**Solution**: Diagnose-then-Compress framework. Step 1: Token importance CV provides zero-cost diagnostic for pruning tolerance (one forward pass). Step 2: VTR (Vision Token Re-encoding) provides universal compression. For pixel-shuffle: recovers from 0% (hard pruning) to ~59% ≈ baseline (59.2%), M-curve flat (D105: M=16 56.9% ≈ M=128 58.0%, near-lossless at any compression ratio). For MLP projector: D109 C4-ext = 0% SR (overfitting at M=128); VTC-only M=32/M=64 in progress.\\\\n\\\\n**Headline result**: \\\\\\\"Across 5 VLA models (450M-7B) × 4 task suites, we find that token pruning robustness is governed by two axes: connector architecture (token-independent vs token-entangling, diagnosed by importance CV) and task complexity. Token-entangling connectors (BART encoder, pixel-shuffle) show dramatically amplified sensitivity under complex tasks — X-VLA drops 27.8pp on Goal vs 1.6pp on Object at the same keep ratio; SmolVLA collapses to 0% at 5% removal regardless of task. CV (0.038→0.314) predicts both pruning tolerance and optimal strategy: importance-based pruning is actively harmful on low-CV architectures (+28-36pp gap favoring random), while it helps on high-CV models (+1-6pp). VTR recovers to ~59% (≈baseline) at any compression ratio (0-87.5%) where hard deletion achieves 0%.\\\\\\\"\\\\n\\\\n## Paper Structure (7-model version)\\\\n\\\\n1. **Introduction**: VLA efficiency motivation → diverse connector architectures → 2-axis framework discovery (D171) → Diagnose-then-Compress framework\\\\n2. **Background**: 5 VLA models, 3 connector families (linear/MLP/pixel-shuffle), 4 LIBERO suites, token flow analysis\\\\n3. **Experimental Setup**: 5 models, LIBERO benchmark (4 suites: Object/Spatial/Goal/Long), pruning protocol, VTR compression, diagnostic metrics\\\\n4. **Main Results**:\\\\n   - §4.1: 2-Axis Framework Overview (Table 1: 5 models × token coupling axis; Table 2: cross-suite interaction — connector × task complexity)\\\\n   - §4.2: Token-Entangling Catastrophic — pixel-shuffle cliff-edge (SmolVLA, all configs 0% regardless of task)\\\\n   - §4.3: Token-Independent Graded — MLP degradation (OpenVLA 6-point curve + OFT entropy confirmation)\\\\n   - §4.4: Token-Independent Tolerant — linear projection (π0 + π0.5, controlled comparison with OpenVLA)\\\\n   - §4.5: Task Complexity Amplification — X-VLA cross-suite (Object 97.6% vs Goal 70.2% vs Long ~53% at same k)\\\\n   - §4.6: Pruning Strategy Depends on CV (D132: low-CV random>>L2norm, high-CV L2norm>>random)\\\\n   - §4.7: VTR overcomes cliff-edge (M-curve flat + architecture independence)\\\\n   - (REMOVED — D119: LIBERO-Plus L1 SR=3.3% floor effect, noted in Discussion §6)\\\\n5. **Analysis**:\\\\n   - §5.1: Why pixel_shuffle creates entanglement (spatial folding + controlled comparison)\\\\n   - §5.2: Diagnostic metric — Entropy + CV composite (D104, 4-model validation)\\\\n   - §5.3: Re-encoding mechanism (M=128 passthrough + MLP adapter + M-curve flat D105)\\\\n6. **Discussion**: Design implications, limitations (sim-only, no real robot), future work\\\\n7. **Conclusion**: 5 claims summary\\\\n\\\\n## Anticipated Reviewer Concerns\\\\n\\\\n### RC1: Only 2 models → **FULLY ADDRESSED**\\\\n**Response**: Now 5 models (SmolVLA, OpenVLA, OpenVLA-OFT, π0, X-VLA) across 3 connector families (pixel-shuffle, 3-layer MLP, linear projection) and 4 model sizes (450M-7B). Each connector class has ≥2 models.\\\\n\\\\n### RC2: Model size confound (450M vs 7B) → **FULLY ADDRESSED**\\\\n**Response**: π0 (3.3B, linear) is pruning-immune while OpenVLA (7B, MLP) degrades 61% at k=0.1. Larger model is MORE vulnerable, not less — directly falsifies \\\\\\\"larger models are more robust\\\\\\\" hypothesis. X-VLA (880M, linear) also immune, matching π0 behavior despite 4× smaller. Size is not the explanatory variable; connector type is.\\\\n\\\\n### RC3: Why not test SmolVLA without pixel_shuffle?\\\\n**Response**: SmolVLA's connector is integral (LLM expects 128 tokens, not 1024). Removing it requires retraining from scratch. OpenVLA comparison isolates the connector's role.\\\\n\\\\n### RC4: Smart compression — is re-encoding or compression the mechanism?\\\\n**Response (corrected with baseline=59.2%)**: VTR achieves near-lossless compression at any ratio — the M-curve is flat (M=16: 56.9% → M=128: 58.0%, all within ±3pp of baseline 59.2%). Two lines of evidence: (1) M=128 passthrough (58.0%) ≈ baseline (59.2%) — re-encoding recovers spatial entanglement to baseline level, not above it. (2) Architecture control: MLP adapter (63.4%) ≈ cross-attention (60.1%) with CI overlap — any re-encoding mechanism works. The key contribution is recovery from 0% (hard pruning) to ~59% (baseline), not exceeding baseline. Compression ratio is a free parameter with negligible SR cost.\\\\n\\\\n### RC5: Relationship to VLA-IAP\\\\n**Response**: VLA-IAP's 97.8% on OpenVLA is consistent with our finding: MLP projector preserves token independence. VLA-IAP untested on pixel_shuffle VLAs; our geometric prior experiments (0%) predict it would fail.\\\\n\\\\n### RC6: Is this just \\\\\\\"different models behave differently\\\\\\\"?\\\\n**Response**: We identify the specific mechanism (pixel_shuffle spatial folding) and provide evidence for WHY. Concrete design implications: future VLAs wanting efficiency should avoid pixel_shuffle or include learned re-encoding modules.\\\\n\\\\n### RC7: Only one benchmark (LIBERO-Object) → **ADDRESSING (D115, D119)**\\\\n**Response**: Expanded to ALL 4 LIBERO suites (Object/Spatial/Goal/Long) — 4 genuinely different task distributions (manipulation skills, spatial reasoning, goal-conditioned, long-horizon). Taxonomy consistency validated across suites. LIBERO-Plus robustness benchmark tested (D119) but abandoned: L1 camera perturbation collapses OpenVLA to SR=3.3% (consistent with leaderboard 0.8%), creating floor effect with no room for pruning analysis. This floor effect itself is noted in Discussion as evidence of general VLA brittleness under distribution shift. Sim-only limitation acknowledged.\\\\n\\\\n## All Experimental Evidence (confirmed)\\\\n\\\\n### SmolVLA Cliff-Edge\\\\n- Fine-tuned baseline (Object): 44.8% (224/500) — ⚠️ OLD reproduced checkpoint, superseded by official HF = 59.2%\\\\n- 6 pruning conditions (random/ACIS/ToMe × k=0.5/0.7/0.9): all 0%\\\\n- Geometric prior (Sobel) k=0.5/0.7/0.9: all 0%\\\\n- Attention entropy: 0.952 (flat, TV=0.05)\\\\n- Official checkpoint Object: 59.2% → 0% at k=0.5\\\\n- Official checkpoint Spatial: 43.8% → 0.6% (3/500, CI [0.2%, 1.7%]) at k=0.5 — near-zero, confirms cliff-edge across suites\\\\n- LoRA-FT checkpoint Spatial: 8.0% (per-task: [24,8,4,24,0,2,2,2,14,0]) — LoRA trained on Object only, does not transfer to Spatial. Use official checkpoint for cross-suite SmolVLA analysis.\\\\n\\\\n### OpenVLA Degradation Curve\\\\n- k=1.0: 74.0% (370/500)\\\\n- k=0.95: 69.4% (-6% relative)\\\\n- k=0.9: 62.0% (-16% relative)\\\\n- k=0.7: 49.0% (245/500, -34% relative)\\\\n- k=0.5: 37.4% (187/500, -49% relative)\\\\n- k=0.3: 20.6% (103/500, -72% relative)\\\\n- Entropy: 0.639 (progressive sharpening, TV=0.50)\\\\n\\\\n### Cross-Model Pruning Taxonomy (7 models — D100, D120, D127)\\\\n| Model | Connector | Tokens | k=0.1 norm_L1 | k=0.5 norm_L1 | Class |\\\\n|-------|-----------|--------|---------------|---------------|-------|\\\\n| π0 (3.3B) | Pure linear proj | 256 | 0.976 (-2.4%) | 0.983 | Immune |\\\\n| π0.5 (4B) | Pure linear proj (×√d scaling) | 768 (3×256) | **98.2%** (491/500) | **L2norm=33.4%, random=69.4%** | **Uniformly Critical (D139)**: L2norm catastrophic (-64.8pp), random tolerant (-28.8pp), gap=+36pp. CV=0.055. |\\\\n| X-VLA (880M) | Linear + BART 12L | 50 | ~1.00 | ~1.00 | Threshold-graded (k=0.7: 56.2%) |\\\\n| OpenVLA (7B) | 3-layer MLP | 256 | 1.608 (+61%) | 1.167 (+17%) | Smooth graded |\\\\n| OFT (7B) | 3-layer MLP (DINOv2+SigLIP fused) | **512** | N/A | N/A | D136: Blackwell GPU incompatible. CV=0.219≈OpenVLA → graded. Cite official ~97% baseline. |\\\\n| SmolVLA (450M) | Pixel-shuffle | 128 | — | 0% cliff | Catastrophic |\\\\n\\\\nDiagnostic metrics (D104+D106+D120: CV as continuous predictor, 7 models):\\\\n| Model | Connector (effective) | Entropy | CV | Pruning Behavior |\\\\n|-------|----------------------|---------|------|------------------|\\\\n| π0 | Pure linear proj | 0.959 | 0.038 | Immune (offline, k=0.1 improves) |\\\\n| π0.5 | Pure linear proj (×√d) | pending | 0.055 | **Uniformly Critical (D139)**: L2norm=33.4%, random=69.4%, gap=+36pp. Monotonic trend extreme. |\\\\n| X-VLA | Linear proj + BART enc (12L) | **0.614** | **0.151** | Threshold-graded: robust k≥0.9, cliff k=0.7 (56.2%). D127: random=L2norm at k=0.9 |\\\\n| OpenVLA | 3-layer MLP (GELU) | 0.661 | 0.215 | Graded (74→37.4% at k=0.5) |\\\\n| OFT | 3-layer MLP (DINOv2+SigLIP, **512 tokens**) | 0.667 | 0.219 | D136: Graded expected (CV≈OpenVLA). Blackwell GPU incompatible, no LIBERO SR. |\\\\n| SmolVLA | Pixel-shuffle (16×) | 0.952 | **0.314** | Catastrophic (0% at k=0.95) |\\\\n\\\\nKey insights (updated with 7-model data):\\\\n1. **CV is a continuous predictor**: 0.038 → 0.055 → 0.151 → 0.215 → 0.219 → 0.314 maps to decreasing pruning tolerance. NOT a 3-class discrete classifier.\\\\n2. **X-VLA CV=0.151 correctly predicted its intermediate behavior** — closer to OpenVLA (0.215) than π0 (0.038), matching k=0.7 SR ≈ OpenVLA k=0.7.\\\\n3. **X-VLA entropy=0.614 ≈ OpenVLA 0.661** — both have BART/MLP non-linear mixing. X-VLA is NOT \\\\\\\"high entropy\\\\\\\" like π0.\\\\n4. **Effective connector complexity matters more than nominal label**: X-VLA is \\\\\\\"linear proj\\\\\\\" but BART encoder introduces 12 transformer layers of mixing. Paper should discuss \\\\\\\"effective connector\\\\\\\" = projection + any intermediate processing.\\\\n5. OFT entropy 0.667 ≈ Standard 0.661 → action head does not affect attention structure\\\\n6. Framing: CV captures \\\\\\\"degree of non-linear mixing in the vision-to-LLM pathway.\\\\\\\" More mixing → higher CV → less tolerant of pruning.\\\\n\\\\n### Smart Compress (Learned Re-encoding)\\\\nCross-attention (VTC) M sweep (3-seed where available):\\\\n- M=16: **56.9% ± 1.3pp** (3-seed: 55.8/58.4/56.5) — 87.5% compression, ZERO loss vs M=128\\\\n- M=32: 60.1±1.3% (3-seed: 61.6/59.2/59.6)\\\\n- M=64: 62.0±2.3% (3-seed: 61.6/60.0/64.4)\\\\n- M=96: 54.5±3.2% (3-seed: 52.6/58.2/52.8) — highest variance\\\\n- M=128: 58.0±3.5pp (3-seed: 59.8/54.0/60.2) — passthrough control\\\\n- **D102 CONFIRMED: M-curve is flat.** M=16 (56.9%) = M=128 (58.0%), difference < 1.1pp. VTC achieves near-lossless compression at ANY ratio for pixel-shuffle connector. All M values within ±5pp of baseline ~59%.\\\\n\\\\nMLP adapter (M=32, 3-seed):\\\\n- seed42: 65.2% (326/500), seed43: 64.6% (323/500), seed44: 60.4% (302/500)\\\\n- Mean: 63.4% ± 2.6 vs VTC M=32 mean 60.1% ± 1.3\\\\n- t-test p≈0.15, no significant difference — confirms architecture-independence\\\\n\\\\n### D109: VTR on OpenVLA (MLP projector) — FAILED\\\\n- C4-ext M=128 at 20K steps: **0% SR** (0/44 episodes before eval termination)\\\\n- Failure mode: model outputs identical action every timestep (severe overfitting)\\\\n- Interpretation: VTR adds unnecessary complexity for MLP projector tokens (already individually meaningful). VTR specifically solves pixel-shuffle entanglement.\\\\n- VTC-only M=32 and M=64 training in progress on westd-41074:2-3\\\\n\\\\n### Cross-Suite VTR Generalization (SmolVLA)\\\\n- M=32 Spatial: 53.2% (vs official Spatial baseline 44.6% per ROADMAP, vs pruning 0.6% — recovery from cliff-edge, +8.6pp over baseline)\\\\n- M=32 Goal: 56.4% (vs official Goal baseline 60.8% per ROADMAP, vs pruning 0% — recovery from cliff-edge, -4.4pp below baseline)\\\\n- ⚠️ Cross-suite baselines need reconciliation: paper_framing previously used 43.8%/63.0%, ROADMAP uses 44.6%/60.8%. Use n=500 official checkpoint data as ground truth.\\\\n- Note: VTR trained on Object suite, evaluated cross-suite. Official baselines from different checkpoint (official vs LoRA-FT); comparisons should emphasize recovery from 0% rather than absolute performance vs uncompressed.\\\\n\\\\n### Pairwise Statistical Tests (Welch's t-test, n=3 per condition)\\\\n- M=32 VTC vs M=32 MLP: p=0.150 (not significant) — confirms architecture-independence\\\\n- M=64 VTC vs M=96 VTC: p=0.034 (significant) — M=96 dip confirmed real\\\\n- M=32 MLP vs M=96 VTC: p=0.022 (significant) — M=96 underperforms\\\\n- M=32/M=64/M=128 VTC cluster: all pairwise p>0.25 — robust across M values\\\\n- Bonferroni note: no pair survives correction at 10 tests; n=3 limits power (~0.2 for medium effects)\\\\n\\\\n### Supplementary\\\\n- Inference latency: 6% speedup at M=32\\\\n- KV-cache: 75% memory reduction at M=32\\\\n\\\", \\\"total_chars\\\": 51958, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
      "numLines": 1,
      "startLine": 1,
      "totalLines": 1
    }
  }
}
```

</details>

---


### Assistant

_source line 23_

<details><summary>Logged reasoning block</summary>

```text
The registry returned 0 results with SUCCESS filter and then the unfiltered query was too large. Let me use bash with jq to parse the registry data and extract what I need. Let me also read the large registry file.

Actually, the ROADMAP and paper_framing have already given me most of the data I need. The cliff curve tables in ROADMAP.md are comprehensive. Let me also check the registry file with jq to get the experiment counts and statuses.

Let me extract core claims from paper_framing.md and cross-reference with the data in ROADMAP.md.


Now I'm pulling out the key claims and their supporting evidence. The first claim establishes a 2-axis framework around token coupling and task complexity, with specific performance deltas like X-VLA showing 97.6% retention versus Goal's 70.2%. The second claim focuses on how pixel shuffling creates irreversible token entanglement, though it appears to be cut off.

Looking at the remaining claims, I see evidence for linear projections being architecture-dependent, MLP projectors showing graded degradation across multiple models, and learned re-encoding achieving significant recovery in SmolVLA but failing on OpenVLA. The final claim appears incomplete.

Now I'm examining the OpenVLA object detection cliff curve data across different pruning ratios and methods to verify coverage. Looking at the performance metrics for the OpenVLA Long Cliff Curve, I'm seeing similar patterns with some results completed and others still running or missing—particularly at the k=0.95 and k=0.5 thresholds where certain methods haven't finished yet. Compiling the π0.5 Long Cliff Curve results, where most configurations are performing well with L2norm and Attn showing strong scores across different k values, though a couple of runs are still in progress. Checking the crossover table completion status and now moving through the claim coverage audit by pulling together data from the roadmap and paper framing, while also reviewing the GPU diagnostics to see what experiments are currently running.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "99218632-5821-4993-be44-cefd325dab56",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRRthHG3AiXiEutZCvSqek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 38529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20685
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 24_

Let me extract registry stats to complete the picture.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "b4bc6909-ee74-4fe4-b6af-ba6fa41185d2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRRthHG3AiXiEutZCvSqek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 38529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20685
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 25_

<details open><summary>🔧 Tool call — Bash · `toolu_01TmEyE3A3uEzwQjDerRhyyC`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/7a12e78f-6295-4999-ab31-4ef688467957/tool-results/mcp-agent-ml-research-read_registry-1779844089826.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\nprint(f'Total experiments: {data[\\\"data\\\"][\\\"count\\\"]}')\n# Count by status\nfrom collections import Counter\nstatuses = Counter()\nfor eid, e in exps.items():\n    statuses[e.get('status', 'UNKNOWN')] += 1\nfor s, c in statuses.most_common():\n    print(f'  {s}: {c}')\nprint()\n# List RUNNING experiments\nprint('=== RUNNING ===')\nfor eid, e in exps.items():\n    if e.get('status') == 'RUNNING':\n        m = e.get('metrics', {})\n        print(f'  {eid}: {e.get(\\\"conclusion\\\",\\\"\\\")}')\n\" 2>&1 | head -60",
  "description": "Parse registry to count experiments by status and list running ones"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "e66bfe97-a90a-42a1-bb86-55ddd929a3f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BRRthHG3AiXiEutZCvSqek",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 20685,
      "cache_read_input_tokens": 38529,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 20685
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 26 · 2026-05-27T01:09:00.900Z_

<details><summary>↩ Tool result · `toolu_01TmEyE3A3uEzwQjDerRhyyC`</summary>

```text
Total experiments: 848
  DONE: 733
  PREPARING: 94
  RUNNING: 12
  DEPLOYED: 9

=== RUNNING ===
  eval_openvla_random_k095_object_seed42: 
  eval_pi05_random_k07_long_seed42: 
  eval_openvla_attn_k05_goal_seed42_v2: 
  eval_pi05_l2norm_k085_long_seed42_v4: 
  eval_openvla_random_k095_long_seed42: 
  eval_openvla_l2norm_k095_goal_seed42: 
  eval_openvla_attn_k095_object_seed42: 
  eval_openvla_random_k075_long_seed42: 
  eval_openvla_attn_k075_long_seed42: 
  eval_openvla_l2norm_k075_long_seed42: 
  eval_openvla_attn_k05_long_seed42: 
  eval_openvla_l2norm_k05_long_seed42:
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "4f39757d-ea3e-45de-8f59-6a9d341916a6",
  "tool_use_result": {
    "stdout": "Total experiments: 848\n  DONE: 733\n  PREPARING: 94\n  RUNNING: 12\n  DEPLOYED: 9\n\n=== RUNNING ===\n  eval_openvla_random_k095_object_seed42: \n  eval_pi05_random_k07_long_seed42: \n  eval_openvla_attn_k05_goal_seed42_v2: \n  eval_pi05_l2norm_k085_long_seed42_v4: \n  eval_openvla_random_k095_long_seed42: \n  eval_openvla_l2norm_k095_goal_seed42: \n  eval_openvla_attn_k095_object_seed42: \n  eval_openvla_random_k075_long_seed42: \n  eval_openvla_attn_k075_long_seed42: \n  eval_openvla_l2norm_k075_long_seed42: \n  eval_openvla_attn_k05_long_seed42: \n  eval_openvla_l2norm_k05_long_seed42:",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 27_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check if any key DONE experiments have the metrics I need for the crossover table.

Let me extract the crossover table data. From the paper_framing, the crossover table should be Claim 5 related - the comparison of L2norm vs Random at different k values across models with different CVs.

Actually, the ROADMAP says "Crossover table 16/16 完成" - let me check what this table is. It could be the method × model × k crossover table.

Let me also check what Attn k=0.5 Goal status is - there's eval_openvla_attn_k05_goal_seed42_v2 running.


Now I'm ready to compose the full audit. I have enough information to map each claim to its data requirements. For Claim 1, I need the 5 models × 4 suites evaluation data which I've confirmed from paper_framing, the CV spectrum across the 6 models with their specific values, and I'm still tracking down the X-VLA cross-suite Object data.

Claim 2 on pixel shuffle entanglement is complete—I have SmolVLA's k=0.95 result at 0%, the dual-seed verification, the official checkpoint, and confirmation that multiple methods all yield 0%.

Claim 3a on linear projection pipeline dependency is also complete with π0 immunity at k=0.1, the full X-VLA 8-point curve, and cross-suite data across Object, Spatial, and Goal. Now I'm moving into Claim 3b on MLP projection.

For the MLP projection vector graded degradation, I have the OpenVLA 6-point degradation curve, method independence verification, and OFT entropy/CV analysis—the basic claim is solid, though the cliff curves across the three methods are still partially filled in.

Claim 4 on VTR learned re-encoding is complete: SmolVLA's M-sweep shows the expected flat curve, architecture independence holds across cross-attention and MLP adapters, cross-suite VTR works, and OpenVLA VTR stays at 0%.

For Claim 5 on CV predicting optimal pruning strategy, I'm checking whether π0.5 L2norm outperforms random at k=0.5 and need to continue gathering that comparison data.

Now I'm tracking the cliff curves for the paper figures—OpenVLA Object is mostly done with L2norm complete at k=0.95 and all three methods through k=0.5, while OpenVLA Goal still needs some attention and random pruning results filled in at the higher sparsity levels. I'm noticing some inconsistencies between the ROADMAP table and the decision logs. The table shows Goal k=0.5 with only L2norm completed at 43.4%, but decision D244 indicates that Attention at k=0.5 should be 44.2%, and memory.md section 15 mentions Random at k=0.5 reaching 52.2%. It looks like the ROADMAP table might be outdated compared to what's documented in the decisions and memory sections. Looking at the Goal cliff curve across different k values, I see k=0.95 is still missing Attention and Random results, k=0.75 has Attention and Random currently running, while k=0.9, k=0.85, and k=0.7 are all complete. There's a potential re-run of the k=0.5 Attention experiment in the registry, but the results are already confirmed from D244.

For the Long cliff curve, k=0.95 is missing results across all three methods, k=0.75 is still running, and k=0.7 and k=0.5 have partial completions. The π0.5 Long variant shows k=0.95 and k=0.9 fully done, k=0.85 has Attention and Random complete with L2norm running, and k=0.75 appears complete.

Cross-seed validation for Goal k=0.9 confirms all three methods have consistent results across seeds, and the crossover table is marked complete at 16/16 cells. Now I'm assessing which data points are truly essential for the paper figures versus what's nice-to-have, focusing on whether we have dense enough sampling across the cliff curves to show the performance trends clearly.

For OpenVLA Object, I have 15 out of 18 cells completed with 3 still running. Even without the missing k=0.95 and k=0.75 Random runs, the coverage across k values is solid enough to draw smooth curves for the paper.

For OpenVLA Goal, I'm at 13 completed cells with 3 running and 2 missing from the k=0.95 experiments. The key thing is that each method still gets 4 data points even without those k=0.95 entries, which should be sufficient for the visualization.

For OpenVLA Long, the situation is tighter—only 10 completed cells out of 18, with 6 still running. If those finish, I'd have 16 cells, and even if the k=0.95 experiments don't come through, each method would still have 4 points to work with.

Now checking π0.5 Long...

it's looking much better. Almost everything is done—16 out of 18 cells complete, with just 2 still running. Across all four cliff curves, I'm at 54 complete cells out of 72 total, which is 75% done. There are 14 still processing and only 4 missing entirely—the Goal k=0.95 Attention and one other Goal k=0.95 experiment that didn't get deployed.

Looking at what's missing, all four gaps are at the k=0.95 level. The roadmap says urgent deployment instructions were sent for these four experiments, but Goal k=0.95 Attention and Random k=0.95 Attention still need to be deployed, along with Long k=0.95 L2norm and Long k=0.95 Attention. With the May 28 deadline at 20:00 Beijing time, and each experiment taking 3-6 hours, I need to get these deployed immediately to have any chance of finishing in time.

Before I finalize the audit, I should verify that the crossover table is fully backed up. Looking at the actual data in Claim 5, I'm seeing tables for k=0.5, k=0.7, and k=0.3, each with 3 models and 2 metrics—that's 18 data points total, not 16. The 16/16 crossover table might refer to something like 4 suites by 4 models, or 4 suites by 2 connector types by 2 methods, but without more specifics I can't pin down exactly what it represents. Either way, the ROADMAP marks it as complete.

Now I'm moving on to write the audit itself. I should also check the GPU diagnostics from the memory logs to see if there are estimated completion times for the running experiments—there are 12 experiments currently active, including several OpenVLA evaluations across different k values and seeds that are distributed across the available GPUs. Looking at the status breakdown across different configurations, I can see which experiments are actively running versus which ones are still missing. The truly missing ones are becoming clearer as I track through each combination of parameters.

The four k=0.95 experiments stand out as the critical gaps that the roadmap is flagging—both Goal and Long variants across Attention and Random strategies need to be deployed to complete that tier.

For the claims themselves, I'm noticing that Claim 1 already has solid support from the existing cross-suite data, and Claim 5's core evidence is essentially complete with the k=0.5 and k=0.7 results already in hand.

The cliff curves matter more for visual completeness in the figures than for proving the core arguments. Without the k=0.95 points, the curves would start at k=0.9 instead, which is a moderate risk for presentation polish but not a threat to the paper's validity. The 14 running experiments carry low risk if they finish within the next 28 hours, and cross-seed validation is already done for Goal k=0.9 across all three methods.

Now I'm ready to write up the audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "125b8d87-ef65-45f0-a63f-6dac4c0bfeeb",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iccbVAx2dfcKZbfqLd5P5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 59214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 28_

Now let me check if any of the "missing" k=0.95 experiments have been deployed since the last ROADMAP update.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "ddedf67e-5adc-4ca1-af3a-33e3f4083862",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iccbVAx2dfcKZbfqLd5P5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 59214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Bash · `toolu_01NvRHJ3N4AXbxY3gY3Rd5sG`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/7a12e78f-6295-4999-ab31-4ef688467957/tool-results/mcp-agent-ml-research-read_registry-1779844089826.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check for k=0.95 experiments\ntargets = ['k095', 'k0.95']\nprint('=== All k=0.95 experiments ===')\nfor eid, e in sorted(exps.items()):\n    if any(t in eid for t in targets):\n        s = e.get('status','?')\n        m = e.get('metrics', {})\n        sr = m.get('success_rate', m.get('sr', ''))\n        print(f'  {s:12s} {eid}  SR={sr}')\n\nprint()\nprint('=== Goal k=0.75 experiments ===')\nfor eid, e in sorted(exps.items()):\n    if 'k075' in eid and 'goal' in eid:\n        s = e.get('status','?')\n        m = e.get('metrics', {})\n        sr = m.get('success_rate', m.get('sr', ''))\n        print(f'  {s:12s} {eid}  SR={sr}')\n\nprint()\nprint('=== Goal k=0.5 experiments ===')\nfor eid, e in sorted(exps.items()):\n    if ('k05' in eid or 'k0.5' in eid) and 'goal' in eid and 'k05_' not in eid.replace('k05_goal','k05goal'):\n        # filter to k=0.5, not k=0.5x\n        if 'k05' in eid and 'k050' not in eid:\n            s = e.get('status','?')\n            m = e.get('metrics', {})\n            sr = m.get('success_rate', m.get('sr', ''))\n            print(f'  {s:12s} {eid}  SR={sr}')\n\" 2>&1",
  "description": "Check registry for k=0.95 and Goal k=0.75/0.5 experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "6c4622df-ede0-41b2-bc39-7201a593384d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016iccbVAx2dfcKZbfqLd5P5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2741,
      "cache_read_input_tokens": 59214,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2741
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 30 · 2026-05-27T01:10:41.885Z_

<details><summary>↩ Tool result · `toolu_01NvRHJ3N4AXbxY3gY3Rd5sG`</summary>

```text
=== All k=0.95 experiments ===
  DONE         eval_official_smolvla_prune_k095  SR=
  RUNNING      eval_openvla_attn_k095_object_seed42  SR=
  RUNNING      eval_openvla_l2norm_k095_goal_seed42  SR=
  DONE         eval_openvla_l2norm_k095_object_seed42  SR=
  DONE         eval_openvla_prune_k095  SR=69.4
  DONE         eval_openvla_prune_l2norm_k095  SR=0.706
  DONE         eval_openvla_prune_l2norm_k095_seed42  SR=0.706
  DONE         eval_openvla_prune_random_k095_seed42  SR=
  DONE         eval_openvla_prune_random_k095_seed42_v2  SR=69.2
  DONE         eval_openvla_prune_random_k095_seed43  SR=0.668
  RUNNING      eval_openvla_random_k095_long_seed42  SR=
  RUNNING      eval_openvla_random_k095_object_seed42  SR=
  DONE         eval_pi05_attention_k095_object_seed42  SR=0.984
  DONE         eval_pi05_attn_k095_long_seed42  SR=
  DONE         eval_pi05_l2norm_k095_goal_seed42  SR=
  DONE         eval_pi05_l2norm_k095_goal_seed42_postfix  SR=
  DONE         eval_pi05_l2norm_k095_goal_seed42_v2  SR=89.4
  DONE         eval_pi05_l2norm_k095_long_seed42  SR=
  DONE         eval_pi05_l2norm_k095_long_seed42_postfix  SR=
  DONE         eval_pi05_l2norm_k095_long_seed43_postfix  SR=
  PREPARING    eval_pi05_l2norm_k095_object_seed42  SR=
  DONE         eval_pi05_l2norm_k095_object_seed42_v2  SR=98.2
  PREPARING    eval_pi05_l2norm_k095_object_seed42_v3  SR=
  DONE         eval_pi05_l2norm_k095_object_seed43  SR=
  DONE         eval_pi05_l2norm_k095_object_seed43_v2  SR=
  DONE         eval_pi05_l2norm_k095_spatial_seed42  SR=0.978
  DONE         eval_pi05_l2norm_k095_spatial_seed42_v2  SR=
  DONE         eval_pi05_l2norm_k095_spatial_seed43  SR=
  DONE         eval_pi05_random_k095_goal_seed42  SR=0.84
  DONE         eval_pi05_random_k095_goal_seed42_postfix  SR=
  DONE         eval_pi05_random_k095_goal_seed42_v2  SR=83.8
  DONE         eval_pi05_random_k095_goal_seed43  SR=0.834
  DONE         eval_pi05_random_k095_long_seed42  SR=0.612
  DONE         eval_pi05_random_k095_long_seed42_postfix  SR=
  DONE         eval_pi05_random_k095_long_seed43_postfix  SR=
  DONE         eval_pi05_random_k095_object_seed42  SR=
  DONE         eval_pi05_random_k095_object_seed42_v2  SR=74
  DONE         eval_pi05_random_k095_object_seed43  SR=0.728
  DONE         eval_pi05_random_k095_spatial_seed42  SR=
  DONE         eval_pi05_random_k095_spatial_seed42_postfix  SR=
  DONE         eval_pi05_random_k095_spatial_seed42_postfix_v2  SR=
  DONE         eval_pi05_random_k095_spatial_seed42_v2  SR=
  DONE         eval_pi05_random_k095_spatial_seed42_v3  SR=
  DONE         eval_pi05_random_k095_spatial_seed42_v4  SR=
  DONE         eval_pi05_random_k095_spatial_seed43  SR=
  DONE         eval_smolvla_official_l2norm_k095_object_seed42  SR=0.4
  DONE         eval_smolvla_official_l2norm_k095_object_seed43  SR=
  DONE         eval_smolvla_official_random_k095_object_seed42  SR=0
  DONE         eval_smolvla_official_random_k095_object_seed43  SR=
  DONE         eval_smolvla_random_prune_k095  SR=
  DONE         eval_smolvla_zeromask_l2norm_k095_object_seed42  SR=0
  DONE         eval_smolvla_zeromask_random_k095_object_seed42  SR=0.002
  DONE         eval_xvla_l2norm_k095_goal_seed42  SR=0.538
  DONE         eval_xvla_l2norm_k095_long_seed42  SR=0.47
  DONE         eval_xvla_l2norm_k095_spatial_seed42  SR=0.716
  DONE         eval_xvla_prune_k095_seed42  SR=0.99
  DONE         eval_xvla_prune_k095_seed43  SR=0.99
  DONE         eval_xvla_prune_k095_seed44  SR=0.994
  DONE         eval_xvla_random_k095_goal_seed42  SR=
  DONE         eval_xvla_random_k095_long_seed42  SR=48.2
  PREPARING    eval_xvla_random_k095_object_seed42  SR=
  DONE         eval_xvla_random_k095_object_seed42_v2  SR=0.988
  DONE         eval_xvla_random_k095_spatial_seed42  SR=
  DONE         l2norm_k095_goal_seed42  SR=
  DONE         pi05_l2norm_k095_long_s42  SR=
  DONE         random_k095_goal_seed42  SR=
  DONE         random_k095_long_seed42  SR=
  DONE         smolvla_l2norm_k095_goal_seed42  SR=0.034
  DONE         smolvla_l2norm_k095_long_seed42  SR=0
  DONE         smolvla_l2norm_k095_spatial_seed42  SR=0.066
  DONE         smolvla_official_object_l2norm_k095_s42  SR=0.002
  DONE         smolvla_random_k095_goal_seed42  SR=0.042
  DONE         smolvla_random_k095_long_seed42  SR=0
  DONE         smolvla_random_k095_spatial_seed42  SR=0.042

=== Goal k=0.75 experiments ===
  DONE         eval_openvla_attn_k075_goal_seed42  SR=
  DONE         eval_openvla_l2norm_k075_goal_seed42  SR=
  DONE         eval_openvla_l2norm_k075_goal_seed42_v2  SR=

=== Goal k=0.5 experiments ===
  PREPARING    eval_e5_xvla_attn_last_goal_k05  SR=0
  PREPARING    eval_e5_xvla_attn_mean_goal_k05  SR=0
  PREPARING    eval_e5_xvla_attn_rollout_goal_k05  SR=0
  DONE         eval_goal_prune_k05  SR=
  DONE         eval_openvla_attn_k05_goal_seed42  SR=
  RUNNING      eval_openvla_attn_k05_goal_seed42_v2  SR=
  DONE         eval_openvla_l2norm_k05_goal_seed42  SR=
  DONE         eval_openvla_l2norm_k05_goal_seed42_v2  SR=
  DONE         eval_openvla_l2norm_k05_goal_seed42_v3  SR=
  DONE         eval_openvla_random_k05_goal_seed42  SR=
  DONE         eval_openvla_random_k05_goal_seed42_v2  SR=
  DONE         eval_pi05_attention_k05_goal_seed42  SR=70.2
  DONE         eval_pi05_attention_k05_goal_seed43  SR=
  DONE         eval_pi05_l2norm_k05_goal_seed42  SR=0.592
  DONE         eval_pi05_l2norm_k05_goal_seed42_postfix  SR=
  PREPARING    eval_pi05_random_k05_goal_seed42  SR=73.6
  DONE         eval_pi05_random_k05_goal_seed42_postfix  SR=
  DONE         eval_pi05_random_k05_goal_seed42_v2  SR=
  DONE         eval_xvla_l2norm_k05_goal_seed42_v2  SR=0.59
  DONE         eval_xvla_l2norm_k05_goal_seed42_v3  SR=59
  DONE         eval_xvla_l2norm_k05_goal_seed43  SR=
  DONE         eval_xvla_random_k05_goal_seed42  SR=0
  DONE         eval_xvla_random_k05_goal_seed42_v2  SR=67.2
  DONE         eval_xvla_random_k05_goal_seed43  SR=
  DONE         eval_xvla_random_k05_goal_seed43_v2  SR=
  DONE         eval_xvla_random_k05_goal_seed43_v3  SR=
  DONE         eval_xvla_random_k05_goal_seed43_v4  SR=68.6
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "5e6df8f8-c0c1-4b7a-92bf-c16878357235",
  "tool_use_result": {
    "stdout": "=== All k=0.95 experiments ===\n  DONE         eval_official_smolvla_prune_k095  SR=\n  RUNNING      eval_openvla_attn_k095_object_seed42  SR=\n  RUNNING      eval_openvla_l2norm_k095_goal_seed42  SR=\n  DONE         eval_openvla_l2norm_k095_object_seed42  SR=\n  DONE         eval_openvla_prune_k095  SR=69.4\n  DONE         eval_openvla_prune_l2norm_k095  SR=0.706\n  DONE         eval_openvla_prune_l2norm_k095_seed42  SR=0.706\n  DONE         eval_openvla_prune_random_k095_seed42  SR=\n  DONE         eval_openvla_prune_random_k095_seed42_v2  SR=69.2\n  DONE         eval_openvla_prune_random_k095_seed43  SR=0.668\n  RUNNING      eval_openvla_random_k095_long_seed42  SR=\n  RUNNING      eval_openvla_random_k095_object_seed42  SR=\n  DONE         eval_pi05_attention_k095_object_seed42  SR=0.984\n  DONE         eval_pi05_attn_k095_long_seed42  SR=\n  DONE         eval_pi05_l2norm_k095_goal_seed42  SR=\n  DONE         eval_pi05_l2norm_k095_goal_seed42_postfix  SR=\n  DONE         eval_pi05_l2norm_k095_goal_seed42_v2  SR=89.4\n  DONE         eval_pi05_l2norm_k095_long_seed42  SR=\n  DONE         eval_pi05_l2norm_k095_long_seed42_postfix  SR=\n  DONE         eval_pi05_l2norm_k095_long_seed43_postfix  SR=\n  PREPARING    eval_pi05_l2norm_k095_object_seed42  SR=\n  DONE         eval_pi05_l2norm_k095_object_seed42_v2  SR=98.2\n  PREPARING    eval_pi05_l2norm_k095_object_seed42_v3  SR=\n  DONE         eval_pi05_l2norm_k095_object_seed43  SR=\n  DONE         eval_pi05_l2norm_k095_object_seed43_v2  SR=\n  DONE         eval_pi05_l2norm_k095_spatial_seed42  SR=0.978\n  DONE         eval_pi05_l2norm_k095_spatial_seed42_v2  SR=\n  DONE         eval_pi05_l2norm_k095_spatial_seed43  SR=\n  DONE         eval_pi05_random_k095_goal_seed42  SR=0.84\n  DONE         eval_pi05_random_k095_goal_seed42_postfix  SR=\n  DONE         eval_pi05_random_k095_goal_seed42_v2  SR=83.8\n  DONE         eval_pi05_random_k095_goal_seed43  SR=0.834\n  DONE         eval_pi05_random_k095_long_seed42  SR=0.612\n  DONE         eval_pi05_random_k095_long_seed42_postfix  SR=\n  DONE         eval_pi05_random_k095_long_seed43_postfix  SR=\n  DONE         eval_pi05_random_k095_object_seed42  SR=\n  DONE         eval_pi05_random_k095_object_seed42_v2  SR=74\n  DONE         eval_pi05_random_k095_object_seed43  SR=0.728\n  DONE         eval_pi05_random_k095_spatial_seed42  SR=\n  DONE         eval_pi05_random_k095_spatial_seed42_postfix  SR=\n  DONE         eval_pi05_random_k095_spatial_seed42_postfix_v2  SR=\n  DONE         eval_pi05_random_k095_spatial_seed42_v2  SR=\n  DONE         eval_pi05_random_k095_spatial_seed42_v3  SR=\n  DONE         eval_pi05_random_k095_spatial_seed42_v4  SR=\n  DONE         eval_pi05_random_k095_spatial_seed43  SR=\n  DONE         eval_smolvla_official_l2norm_k095_object_seed42  SR=0.4\n  DONE         eval_smolvla_official_l2norm_k095_object_seed43  SR=\n  DONE         eval_smolvla_official_random_k095_object_seed42  SR=0\n  DONE         eval_smolvla_official_random_k095_object_seed43  SR=\n  DONE         eval_smolvla_random_prune_k095  SR=\n  DONE         eval_smolvla_zeromask_l2norm_k095_object_seed42  SR=0\n  DONE         eval_smolvla_zeromask_random_k095_object_seed42  SR=0.002\n  DONE         eval_xvla_l2norm_k095_goal_seed42  SR=0.538\n  DONE         eval_xvla_l2norm_k095_long_seed42  SR=0.47\n  DONE         eval_xvla_l2norm_k095_spatial_seed42  SR=0.716\n  DONE         eval_xvla_prune_k095_seed42  SR=0.99\n  DONE         eval_xvla_prune_k095_seed43  SR=0.99\n  DONE         eval_xvla_prune_k095_seed44  SR=0.994\n  DONE         eval_xvla_random_k095_goal_seed42  SR=\n  DONE         eval_xvla_random_k095_long_seed42  SR=48.2\n  PREPARING    eval_xvla_random_k095_object_seed42  SR=\n  DONE         eval_xvla_random_k095_object_seed42_v2  SR=0.988\n  DONE         eval_xvla_random_k095_spatial_seed42  SR=\n  DONE         l2norm_k095_goal_seed42  SR=\n  DONE         pi05_l2norm_k095_long_s42  SR=\n  DONE         random_k095_goal_seed42  SR=\n  DONE         random_k095_long_seed42  SR=\n  DONE         smolvla_l2norm_k095_goal_seed42  SR=0.034\n  DONE         smolvla_l2norm_k095_long_seed42  SR=0\n  DONE         smolvla_l2norm_k095_spatial_seed42  SR=0.066\n  DONE         smolvla_official_object_l2norm_k095_s42  SR=0.002\n  DONE         smolvla_random_k095_goal_seed42  SR=0.042\n  DONE         smolvla_random_k095_long_seed42  SR=0\n  DONE         smolvla_random_k095_spatial_seed42  SR=0.042\n\n=== Goal k=0.75 experiments ===\n  DONE         eval_openvla_attn_k075_goal_seed42  SR=\n  DONE         eval_openvla_l2norm_k075_goal_seed42  SR=\n  DONE         eval_openvla_l2norm_k075_goal_seed42_v2  SR=\n\n=== Goal k=0.5 experiments ===\n  PREPARING    eval_e5_xvla_attn_last_goal_k05  SR=0\n  PREPARING    eval_e5_xvla_attn_mean_goal_k05  SR=0\n  PREPARING    eval_e5_xvla_attn_rollout_goal_k05  SR=0\n  DONE         eval_goal_prune_k05  SR=\n  DONE         eval_openvla_attn_k05_goal_seed42  SR=\n  RUNNING      eval_openvla_attn_k05_goal_seed42_v2  SR=\n  DONE         eval_openvla_l2norm_k05_goal_seed42  SR=\n  DONE         eval_openvla_l2norm_k05_goal_seed42_v2  SR=\n  DONE         eval_openvla_l2norm_k05_goal_seed42_v3  SR=\n  DONE         eval_openvla_random_k05_goal_seed42  SR=\n  DONE         eval_openvla_random_k05_goal_seed42_v2  SR=\n  DONE         eval_pi05_attention_k05_goal_seed42  SR=70.2\n  DONE         eval_pi05_attention_k05_goal_seed43  SR=\n  DONE         eval_pi05_l2norm_k05_goal_seed42  SR=0.592\n  DONE         eval_pi05_l2norm_k05_goal_seed42_postfix  SR=\n  PREPARING    eval_pi05_random_k05_goal_seed42  SR=73.6\n  DONE         eval_pi05_random_k05_goal_seed42_postfix  SR=\n  DONE         eval_pi05_random_k05_goal_seed42_v2  SR=\n  DONE         eval_xvla_l2norm_k05_goal_seed42_v2  SR=0.59\n  DONE         eval_xvla_l2norm_k05_goal_seed42_v3  SR=59\n  DONE         eval_xvla_l2norm_k05_goal_seed43  SR=\n  DONE         eval_xvla_random_k05_goal_seed42  SR=0\n  DONE         eval_xvla_random_k05_goal_seed42_v2  SR=67.2\n  DONE         eval_xvla_random_k05_goal_seed43  SR=\n  DONE         eval_xvla_random_k05_goal_seed43_v2  SR=\n  DONE         eval_xvla_random_k05_goal_seed43_v3  SR=\n  DONE         eval_xvla_random_k05_goal_seed43_v4  SR=68.6",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 31_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me also check the Goal k=0.75 experiments to verify which specific ones exist and their metrics.

From the registry:
- eval_openvla_attn_k075_goal_seed42: DONE (no SR in summary, but it's been noted as running in ROADMAP)
- eval_openvla_l2norm_k075_goal_seed42: DONE
- eval_openvla_l2norm_k075_goal_seed42_v2: DONE

So Goal k=0.75 Attn and L2norm are DONE! The ROADMAP just wasn't updated. 

I notice Random k=0.75 Goal is currently running on westd-38929 GPU 3 but hasn't been registered yet, so that's the one still in progress. Now I need to identify which k=0.95 experiments are actually missing from the registry.

Looking at the status breakdown, I can see that for OpenVLA k=0.95, the Goal variant with L2norm is running, but both the Attention and Random Goal variants are missing, and the Long variants with L2norm and Attention are also not found. So the experiments that haven't been deployed yet are the Attention-based Goal and Long variants, plus the Random Goal variant, and the L2norm Long variant.

With the May 28 deadline at 12:00 UTC and about 28 hours remaining, these four experiments could theoretically complete if started immediately since each takes 3-6 hours. But I'm running into a GPU constraint—only two idle RTX 4090s are available, and I need to verify whether they have enough VRAM for OpenVLA's 7B parameters, since the model appears to use around 16GB on Blackwell GPUs. The 4 missing k=0.95 experiments require Blackwell GPUs, but all 8 are currently occupied—they'll need to wait for the running experiments to finish. Based on the GPU diagnostics from earlier today, most of those experiments should complete within the next 6-12 hours, which gives enough time to deploy the missing ones before the deadline. I should also verify whether the Attn Goal k=0.75 experiment actually has results despite showing as DONE without SR in the summary.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "4e4af682-6df1-49b0-921c-ff0fefd6cfbf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATAgAULibAV5Cubawjns4Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8274,
      "cache_read_input_tokens": 61955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8274
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 32_

<details open><summary>🔧 Tool call — Bash · `toolu_0199nMBsk42uJeJVDGbqjsgL`</summary>

```json
{
  "command": "cat /home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-be-idea-gen-0515-2-projects-importance-margin-vla-compress/7a12e78f-6295-4999-ab31-4ef688467957/tool-results/mcp-agent-ml-research-read_registry-1779844089826.txt | python3 -c \"\nimport json, sys\ndata = json.loads(json.loads(sys.stdin.read())['result'])\nexps = data['data']['experiments']\n\n# Check specific experiments for details\ntargets = [\n    'eval_openvla_attn_k075_goal_seed42',\n    'eval_openvla_l2norm_k075_goal_seed42',\n    'eval_openvla_l2norm_k075_goal_seed42_v2',\n    'eval_openvla_attn_k05_goal_seed42',\n    'eval_openvla_random_k05_goal_seed42',\n    'eval_openvla_random_k05_goal_seed42_v2',\n    'eval_openvla_l2norm_k05_goal_seed42_v3',\n    'eval_openvla_attn_k05_goal_seed42_v2',\n    'eval_pi05_attn_k095_long_seed42',\n]\nfor t in targets:\n    if t in exps:\n        e = exps[t]\n        print(f'{t}:')\n        print(f'  status={e.get(\\\"status\\\")}, conclusion={e.get(\\\"conclusion\\\",\\\"\\\")}')\n        print(f'  metrics={e.get(\\\"metrics\\\",{})}')\n        print(f'  updated_at={e.get(\\\"updated_at\\\",\\\"\\\")}')\n        print()\n\" 2>&1",
  "description": "Check details of specific goal experiments"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "b7d5c912-5bd3-4c59-a271-9c7e1ef3ecad",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ATAgAULibAV5Cubawjns4Q",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8274,
      "cache_read_input_tokens": 61955,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8274
      },
      "output_tokens": 10,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 33 · 2026-05-27T01:11:21.386Z_

<details><summary>↩ Tool result · `toolu_0199nMBsk42uJeJVDGbqjsgL`</summary>

```text
eval_openvla_attn_k075_goal_seed42:
  status=DONE, conclusion=failed
  metrics={}
  updated_at=2026-05-27T00:49:40.152Z

eval_openvla_l2norm_k075_goal_seed42:
  status=DONE, conclusion=failed
  metrics={}
  updated_at=2026-05-26T16:50:30.393Z

eval_openvla_l2norm_k075_goal_seed42_v2:
  status=DONE, conclusion=success
  metrics={'overall_sr': 70.2, 'task_srs': [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], 'episodes': 500, 'tasks': 10, 'time_min': 198, 'tokens_256_to_192': True}
  updated_at=2026-05-26T23:33:06.545Z

eval_openvla_attn_k05_goal_seed42:
  status=DONE, conclusion=success
  metrics={'overall_sr': 44.2, 'total_episodes': 500, 'total_successes': 221, 'source': 'result file found on westd-27271 by audit worker, needs verification'}
  updated_at=2026-05-26T16:06:47.555Z

eval_openvla_random_k05_goal_seed42:
  status=DONE, conclusion=success
  metrics={'overall_sr': 0.522, 'total_successes': 261, 'total_episodes': 500}
  updated_at=2026-05-26T23:49:28.279Z

eval_openvla_random_k05_goal_seed42_v2:
  status=DONE, conclusion=negative
  metrics={'overall_sr': 0.522, 'total_successes': 261, 'total_episodes': 500, 'per_task_sr': {'open_middle_drawer': 0.44, 'bowl_on_stove': 0.64, 'wine_bottle_on_cabinet': 0.64, 'open_drawer_put_bowl': 0.1, 'bowl_on_cabinet': 0.74, 'push_plate_stove': 0.54, 'cream_cheese_in_bowl': 0.48, 'turn_on_stove': 0.94, 'bowl_on_plate': 0.46, 'wine_bottle_on_rack': 0.24}, 'source': 'v1 results (v2 process died early)', 'elapsed_minutes': 230.08}
  updated_at=2026-05-26T15:26:39.040Z

eval_openvla_l2norm_k05_goal_seed42_v3:
  status=DONE, conclusion=negative
  metrics={'eval_time_min': 247.8, 'overall_sr': 0.434, 'task_sr': {'open_the_middle_drawer_of_the_cabinet': 0.28, 'open_the_top_drawer_and_put_the_bowl_inside': 0.06, 'push_the_plate_to_the_front_of_the_stove': 0.2, 'put_the_bowl_on_the_plate': 0.3, 'put_the_bowl_on_the_stove': 0.38, 'put_the_bowl_on_top_of_the_cabinet': 0.66, 'put_the_cream_cheese_in_the_bowl': 0.22, 'put_the_wine_bottle_on_the_rack': 0.44, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.82, 'turn_on_the_stove': 0.98}, 'total_episodes': 500, 'total_successes': 217}
  updated_at=2026-05-23T23:18:01.760Z

eval_openvla_attn_k05_goal_seed42_v2:
  status=RUNNING, conclusion=
  metrics={}
  updated_at=2026-05-27T00:49:35.454Z

eval_pi05_attn_k095_long_seed42:
  status=DONE, conclusion=success
  metrics={'overall_sr': 77, 'n_episodes': 500, 'task_sr': {'T0': None, 'T1': None, 'T2': None, 'T3': None, 'T4': None, 'T5': None, 'T6': 14, 'T7': 80, 'T8': 30, 'T9': 98}}
  updated_at=2026-05-26T23:35:43.863Z
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "5e63567d-520e-4b61-b611-00776a90894a",
  "tool_use_result": {
    "stdout": "eval_openvla_attn_k075_goal_seed42:\n  status=DONE, conclusion=failed\n  metrics={}\n  updated_at=2026-05-27T00:49:40.152Z\n\neval_openvla_l2norm_k075_goal_seed42:\n  status=DONE, conclusion=failed\n  metrics={}\n  updated_at=2026-05-26T16:50:30.393Z\n\neval_openvla_l2norm_k075_goal_seed42_v2:\n  status=DONE, conclusion=success\n  metrics={'overall_sr': 70.2, 'task_srs': [54, 80, 86, 22, 88, 70, 68, 98, 82, 54], 'episodes': 500, 'tasks': 10, 'time_min': 198, 'tokens_256_to_192': True}\n  updated_at=2026-05-26T23:33:06.545Z\n\neval_openvla_attn_k05_goal_seed42:\n  status=DONE, conclusion=success\n  metrics={'overall_sr': 44.2, 'total_episodes': 500, 'total_successes': 221, 'source': 'result file found on westd-27271 by audit worker, needs verification'}\n  updated_at=2026-05-26T16:06:47.555Z\n\neval_openvla_random_k05_goal_seed42:\n  status=DONE, conclusion=success\n  metrics={'overall_sr': 0.522, 'total_successes': 261, 'total_episodes': 500}\n  updated_at=2026-05-26T23:49:28.279Z\n\neval_openvla_random_k05_goal_seed42_v2:\n  status=DONE, conclusion=negative\n  metrics={'overall_sr': 0.522, 'total_successes': 261, 'total_episodes': 500, 'per_task_sr': {'open_middle_drawer': 0.44, 'bowl_on_stove': 0.64, 'wine_bottle_on_cabinet': 0.64, 'open_drawer_put_bowl': 0.1, 'bowl_on_cabinet': 0.74, 'push_plate_stove': 0.54, 'cream_cheese_in_bowl': 0.48, 'turn_on_stove': 0.94, 'bowl_on_plate': 0.46, 'wine_bottle_on_rack': 0.24}, 'source': 'v1 results (v2 process died early)', 'elapsed_minutes': 230.08}\n  updated_at=2026-05-26T15:26:39.040Z\n\neval_openvla_l2norm_k05_goal_seed42_v3:\n  status=DONE, conclusion=negative\n  metrics={'eval_time_min': 247.8, 'overall_sr': 0.434, 'task_sr': {'open_the_middle_drawer_of_the_cabinet': 0.28, 'open_the_top_drawer_and_put_the_bowl_inside': 0.06, 'push_the_plate_to_the_front_of_the_stove': 0.2, 'put_the_bowl_on_the_plate': 0.3, 'put_the_bowl_on_the_stove': 0.38, 'put_the_bowl_on_top_of_the_cabinet': 0.66, 'put_the_cream_cheese_in_the_bowl': 0.22, 'put_the_wine_bottle_on_the_rack': 0.44, 'put_the_wine_bottle_on_top_of_the_cabinet': 0.82, 'turn_on_the_stove': 0.98}, 'total_episodes': 500, 'total_successes': 217}\n  updated_at=2026-05-23T23:18:01.760Z\n\neval_openvla_attn_k05_goal_seed42_v2:\n  status=RUNNING, conclusion=\n  metrics={}\n  updated_at=2026-05-27T00:49:35.454Z\n\neval_pi05_attn_k095_long_seed42:\n  status=DONE, conclusion=success\n  metrics={'overall_sr': 77, 'n_episodes': 500, 'task_sr': {'T0': None, 'T1': None, 'T2': None, 'T3': None, 'T4': None, 'T5': None, 'T6': 14, 'T7': 80, 'T8': 30, 'T9': 98}}\n  updated_at=2026-05-26T23:35:43.863Z",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---


### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the data I need. Let me compile the definitive audit.

Key findings from registry data:
- Goal k=0.75: L2norm=70.2% (v2 success), Attn=failed (original), Random still running on server
- Goal k=0.5: L2norm=43.4% ✅, Attn=44.2% ✅ (but v2 running for verification), Random=52.2% ✅
- π0.5 Attn k=0.95 Long: 77.0% ✅

Now let me also verify the Random k=0.5 Goal - the metric shows 0.522 which is 52.2%. 

I should check the crossover table status next. The ROADMAP indicates 16/16 complete, which likely refers to the method crossover analysis where L2norm and Random preference comparisons are tracked across different k-values and model-suite combinations. I'll mark that as done and move forward with compiling the full audit.

Now I'm looking at the OpenVLA Object results across the six k-values and three methods, tracking which cells show completed runs versus those still in progress. Looking at the results table, I'm noticing some discrepancies in the status tracking—the k=0.75 Attention method shows as both completed with a failure and currently running according to the roadmap, so I need to recount the actual completion status: 13 successful runs, 2 still in progress, and 3 that need to be redone.

Checking the GPU diagnostics more carefully, I can see the k=0.75 Attention experiment is registered and actively running on westd-27271, but it's not appearing in my filtered running list, which suggests there might be a naming mismatch or version suffix I'm missing. I'm going back through the RUNNING experiments list from the registry to double-check which ones are actually active. Looking at the entries, I can see eval_openvla_attn_k075_goal_seed42 isn't in this list, which confirms the GPU process might be either a stale run or something that started after the registry was last updated. The experiment appears to be either running unregistered or failed and needs redeployment, so I can't confirm the data is available yet. For the audit, I'm marking the Goal k=0.75 Attention variant as failed in the registry with a note that it might be running unregistered on the GPU. Now I'm finalizing the audit by checking claim coverage across the framework—I have comprehensive evaluation data for the 5 models across 4 suites, the CV spectrum with 6 models, cross-suite comparisons showing the performance gap between Object and Goal variants, and SmolVLA's zero performance, though the cliff curves for the figures are still incomplete. I'm verifying the remaining evidence for Claim 3a with the X-VLA random comparison showing the reversal pattern at k=0.5, plus the cross-suite results demonstrating the Goal task degradation of 27.8 percentage points. For Claim 3b, the OpenVLA degradation curve from k=1.0 down to k=0.3 is confirmed across multiple methods, with the cliff curves for Object, Goal, and Long tasks providing supplementary support. Now I'm checking Claim 4 on VTR learned re-encoding, starting with the SmolVLA evidence.

I've confirmed the M-sweep across five values with three seeds, the flat M-curve on D105, and that the effect holds regardless of whether using VTC or MLP adapters. The cross-suite results show strong performance on Spatial and Goal tasks, while VTR produces zero improvement on OpenVLA as expected. For Claim 5, I'm validating that coefficient of variation predicts the optimal strategy by comparing π0.5, X-VLA, and OpenVLA at both k=0.5 and k=0.7, with monotonic trends confirmed across multiple seeds.

Now I'm checking the completeness of the cliff curves needed for the figures. The OpenVLA Object task has 15 out of 18 cells done with three still running, which gives enough data points to make a viable figure. For OpenVLA Goal, I have 13 complete with two running and three failed, but even without the k=0.95 results I should have sufficient coverage. The OpenVLA Long task is further behind at 10 complete with six still in progress.

Moving to π0.5 Long, I've got 16 out of 18 cells finished with just two experiments running, so that's looking solid. The cross-seed and crossover table experiments are both complete as planned. The main concern is those four missing k=0.95 experiments that need attention.

The critical issue is that I need to deploy the k=0.95 Attn, Random, and L2norm variants for both Goal and Long configurations, but there are no idle Blackwell GPUs available right now. Each experiment takes about 4 hours, and with 28 hours until the deadline, I'm cutting it close—I can still pull this off if GPUs free up within the next 20 hours. The k=0.75 Attn experiment failed during registration, so I'll need to either rerun it unregistered or redeploy it. Most of my 11 running experiments should wrap up in 6-12 hours, with the k=0.95 Object Attn and Random variants being the most critical for the figures.

Now I'm updating my memory file with the current status and need to read what's already there before appending the new section. Generating the results table...

For the audit, I need to prioritize what's critical before the deadline versus what would be nice to have. The running experiments completing would give me fourteen more data points for the cliff curves, and I need at least two of the four missing k=0.95 experiments to have a complete top row across at least two suites. The remaining k=0.95 experiments and the Goal k=0.75 attention data point would be ideal but aren't essential—I can work around missing k=0.95 data by starting the cliff curves at k=0.9 with a note, and the Goal curve has enough points even without that one attention measurement. Now I'm ready to write out the full audit.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "3e1d20f2-4148-4953-9520-7c0b59b61115",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN6PvDgsPty45PCkQhDwyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 70229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2888
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 35_

Now I have the full picture. Let me compose the audit and save it.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "24b90b74-3db7-453a-b988-43fd39a13012",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN6PvDgsPty45PCkQhDwyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 70229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2888
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 36_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Soqev7BY4pL5ffwwZLDeSH`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "max_chars": 500
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "686a9375-78b9-4787-924a-f617fd15d76d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NN6PvDgsPty45PCkQhDwyT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2888,
      "cache_read_input_tokens": 70229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2888
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 37 · 2026-05-27T01:12:50.518Z_

<details><summary>↩ Tool result · `toolu_01Soqev7BY4pL5ffwwZLDeSH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# SimplerEnv 可行性调研报告\\n\\n## 1. SimplerEnv 概述\\n\\n**仓库**: [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) (CoRL 2024, ICLR 2025)\\n\\n**核心**：基于 SAPIEN + ManiSkill2 的仿真评估框架，用于评估真实世界机器人操控策略在仿真环境中的表现。\\n\\n### 支持的 Tasks（9 个预设环境）\\n\\n**Google Robot（控制频率 3Hz）**：\\n- Pick Coke Can / Pick Random Object / Move Near\\n- Open/Close Drawer / Place in Closed Drawer\\n\\n**WidowX Bridge（控制频率 5Hz）**：\\n- Spoon on Towel / Carrot on Plate / Stack Cube / Eggplant in Basket\\n\\n### 支持的 VLA 模型\\n- RT-1 / RT-1-X（原生支持）\\n- Octo（原生\\n\\n... [截断: 省略 14022 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 14522, \"truncated\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "0b42ac4f-2d5a-43dd-8d82-5d490ca4c80f",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\\\", \\\"content\\\": \\\"# SimplerEnv 可行性调研报告\\\\n\\\\n## 1. SimplerEnv 概述\\\\n\\\\n**仓库**: [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) (CoRL 2024, ICLR 2025)\\\\n\\\\n**核心**：基于 SAPIEN + ManiSkill2 的仿真评估框架，用于评估真实世界机器人操控策略在仿真环境中的表现。\\\\n\\\\n### 支持的 Tasks（9 个预设环境）\\\\n\\\\n**Google Robot（控制频率 3Hz）**：\\\\n- Pick Coke Can / Pick Random Object / Move Near\\\\n- Open/Close Drawer / Place in Closed Drawer\\\\n\\\\n**WidowX Bridge（控制频率 5Hz）**：\\\\n- Spoon on Towel / Carrot on Plate / Stack Cube / Eggplant in Basket\\\\n\\\\n### 支持的 VLA 模型\\\\n- RT-1 / RT-1-X（原生支持）\\\\n- Octo（原生\\\\n\\\\n... [截断: 省略 14022 字符，传 max_chars=0 获取完整内容]\\\", \\\"total_chars\\\": 14522, \\\"truncated\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"content\": \"# SimplerEnv 可行性调研报告\\n\\n## 1. SimplerEnv 概述\\n\\n**仓库**: [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) (CoRL 2024, ICLR 2025)\\n\\n**核心**：基于 SAPIEN + ManiSkill2 的仿真评估框架，用于评估真实世界机器人操控策略在仿真环境中的表现。\\n\\n### 支持的 Tasks（9 个预设环境）\\n\\n**Google Robot（控制频率 3Hz）**：\\n- Pick Coke Can / Pick Random Object / Move Near\\n- Open/Close Drawer / Place in Closed Drawer\\n\\n**WidowX Bridge（控制频率 5Hz）**：\\n- Spoon on Towel / Carrot on Plate / Stack Cube / Eggplant in Basket\\n\\n### 支持的 VLA 模型\\n- RT-1 / RT-1-X（原生支持）\\n- Octo（原生\\n\\n... [截断: 省略 14022 字符，传 max_chars=0 获取完整内容]\", \"total_chars\": 14522, \"truncated\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 38_

<details><summary>Logged reasoning block</summary>

```text
Good. Now let me compose the audit section and append it to the existing memory.md content. I already have the full content from the earlier read. Let me construct the new section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "86ad8ef5-2535-463b-900a-213ad02dba21",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRoPBp872VmLGVQijjwDSf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4622,
      "cache_read_input_tokens": 73117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4622
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Assistant

_source line 39_

Now composing and saving the audit. I have all the data from the ROADMAP, paper_framing, registry, and memory.md.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "fc17e546-d7e2-42c9-8f5d-92d1dbce4656",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRoPBp872VmLGVQijjwDSf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4622,
      "cache_read_input_tokens": 73117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4622
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool call

_source line 40_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__save_project_file · `toolu_01EasHxvSF1GSCebGFJim4JU`</summary>

```json
{
  "project": "importance_margin_vla_compress",
  "file": "memory.md",
  "content": "# SimplerEnv 可行性调研报告\n\n## 1. SimplerEnv 概述\n\n**仓库**: [simpler-env/SimplerEnv](https://github.com/simpler-env/SimplerEnv) (CoRL 2024, ICLR 2025)\n\n**核心**：基于 SAPIEN + ManiSkill2 的仿真评估框架，用于评估真实世界机器人操控策略在仿真环境中的表现。\n\n### 支持的 Tasks（9 个预设环境）\n\n**Google Robot（控制频率 3Hz）**：\n- Pick Coke Can / Pick Random Object / Move Near\n- Open/Close Drawer / Place in Closed Drawer\n\n**WidowX Bridge（控制频率 5Hz）**：\n- Spoon on Towel / Carrot on Plate / Stack Cube / Eggplant in Basket\n\n### 支持的 VLA 模型\n- RT-1 / RT-1-X（原生支持）\n- Octo（原生支持）\n- **OpenVLA**（通过 [DelinQu fork](https://github.com/DelinQu/SimplerEnv-OpenVLA) 集成）\n- **π0 / π0-FAST**（通过 openpi/lerobot 集成，已有社区支持）\n- π0.5：**存在已知问题**（[openpi#799](https://github.com/Physical-Intelligence/openpi/issues/799)），SimplerEnv 上性能不稳定\n\n### 评估方式\n- **Visual Matching**：将真实图像叠加到仿真背景\n- **Variant Aggregation**：多种环境变体（背景、光照、干扰物）取平均\n\n### 版本\n- **ManiSkill2（主分支）**：CPU 仿真，9 个 tasks，成熟稳定\n- **ManiSkill3 分支**：GPU 加速 10-15x，但只移植了 4 个 Bridge tasks\n\n## 2. 与 LIBERO 的互补性\n\n| 维度 | LIBERO | SimplerEnv |\n|------|--------|------------|\n| 定位 | 终身学习/知识迁移 | 仿真复现真实策略 |\n| Tasks | 130 个，分 4 个 suite | 9 个预设，多变体 |\n| 机器人 | Franka Panda (tabletop) | Google Robot + WidowX |\n| 观测 | 多相机 (agentview + wrist) | 单相机 (obs_camera) |\n| 动作空间 | 7-DoF (delta pos + gripper) | world_vector + rot_axangle + gripper |\n| 评估指标 | 成功率 (per-task, per-suite) | 成功率 (visual matching / variant agg) |\n| GPU 需求 | 渲染用 EGL | 需 RTX GPU（ray-tracing） |\n\n**互补性**：LIBERO 测试 long-horizon + 多任务泛化，SimplerEnv 测试 sim-to-real 保真度。论文中两个 benchmark 同时报告可以展示方法的全面性。\n\n## 3. 竞品分析（Token Pruning for VLA）\n\n| 方法 | 发表 | SimplerEnv | LIBERO | 核心思路 |\n|------|------|-----------|--------|---------|\n| **SP-VLA** | arXiv 2506.12723 | ✅ 2.4x加速+6%提升 | ✅ 1.5x无损加速 | 动作感知调度 + 时空token pruning |\n| **DTP** | arXiv 2601.16065 | ✅ SIMPLER benchmark | ❓ | 去除task无关区域的干扰token |\n| **Compressor-VLA** | arXiv 2511.18950 | ❌ | ✅ 59% FLOPs↓ | 指令引导的视觉token压缩（cross-attn） |\n| **LightVLA** | arXiv 2509.12594 | ✅ | ✅ | 可微分token pruning |\n| **EfficientVLA** | OpenReview | ✅ | ❓ | Training-free 加速+压缩 |\n| **Ours** | - | ❌ 放弃 | ✅ | Importance margin + smart compress |\n\n**关键发现**: SP-VLA 是最直接的竞品。\n\n## 4. Pruning 适配方案\n\n**关键洞察：pruning hook 与环境无关，只需替换 env loop。**\n\n- **OpenVLA 适配（2-3h）**：创建 `OpenVLAPruningPolicy` 实现 SimplerEnv 接口，复用现有 hook 代码\n- **π0.5 适配（4-6h）**：需解决多相机→单相机映射，且存在已知稳定性问题\n- **建议**：先做 OpenVLA\n\n## 5. 安装与渲染状态（westd-27271）\n\n### 服务器配置\n- **GPU**: 2x NVIDIA RTX PRO 6000 Blackwell (94GB each)\n- **CUDA**: 12.8 | **Driver**: 580.95.05 | **PyTorch**: 2.11.0+cu128\n- **SimplerEnv 路径**: `/root/autodl-tmp/SimplerEnv/`\n\n### SAPIEN 2 vs 3 兼容性（2026-05-25 验证）\n\n**SAPIEN 2.2.2（ManiSkill2 主分支要求）**：\n- ❌ `camera.take_picture()` 在 RTX PRO 6000 Blackwell + driver 580 上 segfault\n- 原因：SAPIEN 2.2.2 编译的 Vulkan pipeline 与新驱动不兼容\n- 尝试过 `VK_ICD_FILENAMES`、`LD_PRELOAD libvulkan`、不同分辨率、`offscreen_only=True`，均 segfault\n- **结论：SAPIEN 2.x 在此 GPU/驱动组合上不可用**\n\n**SAPIEN 3.0.3（ManiSkill3 使用）**：\n- ✅ 渲染完全正常，端到端测试通过\n- 环境变量：`VK_ICD_FILENAMES=/etc/vulkan/icd.d/nvidia_icd.json NVIDIA_DRIVER_CAPABILITIES=all`\n\n### 渲染测试结果（2026-05-25 通过）\n\n**使用 ManiSkill3 分支**（`git checkout maniskill3`）+ `mani-skill==3.0.1` + `sapien==3.0.3`（conda base, Python 3.12）\n\n4 个 WidowX Bridge 环境全部通过：\n- ✅ `PutCarrotOnPlateInScene-v1` — rgb=(1,480,640,3) uint8\n- ✅ `PutSpoonOnTableClothInScene-v1` — rgb=(1,480,640,3) uint8\n- ✅ `StackGreenCubeOnYellowCubeBakedTexInScene-v1` — rgb=(1,480,640,3) uint8\n- ✅ `PutEggplantInBasketScene-v1` — rgb=(1,480,640,3) uint8\n\n**obs 结构**：`obs['sensor_data']['3rd_view_camera']['rgb']` (torch.uint8) + `['segmentation']` (torch.int16)\n**obs_mode**: 必须用 `'rgb+segmentation'`（不支持 `'rgbd'`）\n\n**限制**：ManiSkill3 只移植了 4 个 Bridge 环境，无 Google Robot 环境（GraspSingleOpenedCokeCanInScene 等未注册）。\n\n## 6. SimplerEnv 结论 (D209, 2026-05-24)\n\n**已放弃。** OpenVLA-7B + ManiSkill3 Bridge baseline = 0% SR（全 4 tasks × 50 eps = 0/200 成功）。L2norm k=0.9 同样 0%。\n\n**原因分析**：\n- Baseline 本身 0%，问题不在 pruning，在于 OpenVLA-7B + ManiSkill3 集成\n- transformers 版本不匹配（expected 4.40.1 但实际 5.5.4）\n- action 接口 / unnormalization 可能不兼容 ManiSkill3\n- 修复成本不可接受（CoRL 距 deadline 5 天）\n\n**结论**：论文 benchmark = LIBERO + MetaWorld，不含 SimplerEnv。\n\n## 7. 关键决策记录\n\n### [2026-05-24] OpenVLA 转 SimplerEnv 路线\nDirector 决策：不在 westd-38929 修 LIBERO OpenVLA Goal 脚本（模型不在 + 脚本要改），OpenVLA 的新数据直接从 SimplerEnv 来。\n\n### [2026-05-24] MetaWorld 部署规范\nMetaWorld 实验必须统一走 `submit_training_job`，禁止 `ssh_execute` 直接部署（绕过碰撞检测导致 GPU3 冲突事件）。\n\n### [2026-05-24] MetaWorld baseline\nSmolVLA (0.45B, Linear connector) MetaWorld 5 tasks baseline = 26.4% overall SR。早期信号：L2norm k=0.5 reach-v3 (4%) 比 Random k=0.5 (20%) 更差，初步支持 Linear connector scale-invariance hypothesis。\n\n### [2026-05-24] cqa1-33015 需要 conda activate\ncqa1 服务器上 python 不在 PATH 中，提交命令必须用 `bash -c \\\"source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && ...\\\"` 包装。\n\n### SmolVLA MetaWorld Sweep 失败诊断 (2026-05-24)\n- **根因**: 监控系统误报（false positive）。两个 sweep 实验实际已全部成功完成，产出了全部 8 个结果文件。监控报 \"process dead 5× with no sentinel/W&B\" 是因为 cron entry 中没有配置 `log_path`，且自动发现机制未找到 `/tmp/random_sweep.log` 和 `/tmp/l2norm_sweep.log`。\n- **证据**: \n  - 脚本 `/tmp/run_random_sweep.sh` 和 `/tmp/run_l2norm_sweep.sh` 均存在且内容正确\n  - 日志末尾有 `ALL_RANDOM_DONE` 和 `ALL_L2NORM_DONE` sentinel\n  - 全部 8 个结果 JSON 均已写入 `/root/autodl-tmp/importance_margin_vla_compress/results/`\n  - GPU 正常，无 OOM\n- **完整结果** (50 episodes/task, 5 tasks, Overall SR)：\n\n| Method | k=0.5 | k=0.85 | k=0.9 | k=0.95 | Baseline (k=1.0) |\n|--------|-------|--------|-------|--------|-----------|\n| Random | 9.6% | 4.4% | 5.6% | 6.4% | 26.4% (25ep) |\n| L2Norm | 0.8% | 2.4% | 10.0% | 7.2% | 26.4% (25ep) |\n\n- **观察**: \n  - 所有 pruned 版本远低于 baseline (26.4%)，token pruning 对 SmolVLA + MetaWorld 伤害极大\n  - Random: k=0.5 (9.6%) 反而优于 k=0.95 (6.4%)，非单调，可能因 random pruning 引入的随机性\n  - L2Norm: k=0.9 (10.0%) 是最佳点，但仍仅为 baseline 的 38%\n  - drawer-open 是最鲁棒的 task（L2Norm k=0.95: 30%），其余 tasks 几乎归零\n- **修复建议**: 提交 sweep 任务时配置 `log_path` 指向持久化路径（非 /tmp），或在脚本中输出 W&B sentinel，使监控能正确追踪。\n\n## 8. π0.5 L2norm vs Random Cliff Zone 分析 (2026-05-25)\n\n**核心发现：π0.5 Object suite 上 L2norm 与 Random 存在 crossover，约在 k≈0.75。**\n\nL2norm 在高 k（0.85-0.95）完全无损（98-99% vs baseline 98.2%），cliff 在 k=0.85→0.7 之间（42pp 断崖跌落至 56%）。Random 在高 k 极度不稳定（k=0.85 约 0-6%），但低 k 时（0.5-0.7）反而比 L2norm 更稳（68-74% vs 33-56%）。\n\n**解释**：Random 均匀采样保留了 token 多样性，低 k 时多样性比 importance 更重要。L2norm 集中保留高 norm token，高 k 时保全了关键信息，但低 k 时丢弃的 token 里可能含不可替代的空间/语义信息，导致崩溃比 Random 更彻底。\n\n**论文意义**：这个 crossover 是 importance margin 概念的直接证据——scoring method 的优劣取决于 keep ratio，不存在全局最优 scoring method。\n\n## 9. 服务器模型部署清单 (2026-05-26)\n\n**教训 [2026-05-26]**：westd-41074 上多次部署 OpenVLA Long 实验失败（eval_openvla_attn_k085_long, eval_openvla_random_k085_long, eval_openvla_attn_k09_goal_seed43），根因是该服务器缺少对应 suite 的 finetuned 模型。eval 脚本不传 `--model_path` 时默认加载 Object 模型，不报错但产出垃圾结果。\n\n**各服务器已确认可用的 OpenVLA 模型**：\n| 服务器 | Object | Goal | Spatial | Long (libero_10) |\n|--------|--------|------|---------|-------------------|\n| westd-41074 | ✅ openvla-7b-finetuned-libero-object | ❓ | ❓ | ✅ 已 rsync（2026-05-26） |\n| westd-38929 | ✅ models/openvla-libero-object | ✅ models/openvla-7b-finetuned-libero-goal (2026-05-26 确认，random_k085_goal 运行 3h+) | ❓ | ✅ models/openvla-7b-finetuned-libero-10 |\n| westd-27271 | ✅ | ✅ openvla-7b-finetuned-libero-goal | ❓ | ❓ |\n| cqa1-33015 | ✅ | ✅ openvla-libero-goal | ❓ | ❓ |\n\n**注意**：westd-38929 模型在 `/root/autodl-tmp/models/` 子目录下（有 models/ 前缀），其他服务器直接在 `/root/autodl-tmp/` 下。\n\n**部署 OpenVLA 实验前必须**：\n1. `ls` 验证目标服务器模型实际路径\n2. 显式传 `--model_path` 和 `--unnorm_key`\n3. 不要依赖脚本默认路径——默认会静默加载 Object 模型\n\n## 10. OpenVLA Long Cliff Curve — Scoring 方法退化速度差异 (2026-05-26)\n\n**核心发现：MLP connector (OpenVLA) Long suite 上，L2norm 退化速度快于 Random。**\n\n| k | Baseline | L2norm | Random | Attn |\n|---|----------|--------|--------|------|\n| 1.0 | 52.8% | — | — | — |\n| 0.9 | — | 43.6% (-9.2pp) | 46.8% (-6.0pp) | 44.0% (-8.8pp) |\n| 0.85 | — | 38.8% (-14.0pp) | — | — |\n| 0.7 | — | 31.2% (-21.6pp) | 38.8% (-14.0pp) | 🏃 running |\n\nk=0.9 时三方法差距仅 ~3pp；到 k=0.7 时 L2norm 比 Random 差 7.6pp。L2norm 每降 0.1k 损失 ~6pp，Random 仅 ~4pp。\n\n**与 π0.5 对比**：π0.5 (Linear) Long k=0.9 L2norm=81% >> Random=32%，49pp 领先。同样的 L2norm scoring 在 MLP connector 上无优势还有害，在 Linear connector 上压倒性领先。\n\n**论文意义**：直接支持 \"connector × scoring 交互\" claim——scoring method 的效果不仅取决于 task，更取决于 connector 架构。MLP connector 的非线性变换破坏了 L2 norm 作为重要性指标的有效性。\n\n## 11. 操作规则沉淀 (2026-05-26)\n\n### M121: Kill 进程前必须验证日志时间\n判断进程 stuck 前必须用 `stat -c %Y &lt;log_file>` 检查日志最后修改时间，>30min 无更新才能 kill。Long suite 日志间隔 10-20min 是正常的。GPU 利用率 0% 不能单独作为 kill 依据。\n\n### M122: 非 Object 套件必须显式传模型参数\n所有非 Object 套件的 OpenVLA 实验必须显式传 `--model_path` 和 `--unnorm_key`：\n- Goal: `--model_path .../openvla-*-libero-goal --unnorm_key libero_goal`\n- Spatial: `--model_path .../openvla-libero-spatial --unnorm_key libero_spatial`\n- Long: `--model_path .../openvla-7b-finetuned-libero-10 --unnorm_key libero_10`\n\n### M123: 部署前必须 ls 验证模型路径\n每台服务器的模型目录结构不同（如 westd-38929 有 models/ 前缀）。部署前必须先 `ls` 确认实际路径，不要假设。\n\n### M124: 禁止 kill 运行中实验腾位置\n有空闲 GPU 时禁止 kill 运行中的实验来腾位置。只在进程确认 stuck（M121 规则）时才 kill。\n\n### M125: 重跑实验必须用唯一 log_path\nv2/v3 重跑实验必须在 log 文件名中加版本后缀（如 `_v2.log`），不能复用 v1 的 log_path。否则新 run 覆盖旧日志，导致：(1) v1 的完整结果日志丢失 (2) v2 失败时无法从日志定位原始数据。事故案例：eval_openvla_random_k05_goal_seed42_v2 覆盖了 v1 日志。\n\n## 12. π0.5 Random Long V-shape 现象 — 已确认为真实 (2026-05-26)\n\n**现象**：π0.5 Random pruning on Long (libero_10) 的 cliff curve 非单调：\n\n| k | SR | seed | 备注 |\n|---|-----|------|------|\n| 0.95 | 61.2-63.2% | s42, s42_postfix | 正常 |\n| 0.9 | 32-35.6% | s42_postfix, s43_postfix | 骤降 ~31pp |\n| 0.85 | 44.4% | s42_v2 | |\n| 0.75 | 62.4% | s42_v2 | 回升 ~30pp |\n| 0.7 | 64.6% | s42 | 继续上升 |\n| 0.5 | 50.2% | s42 | |\n\n**一致性检查结果 (2026-05-26 18:00 UTC, Worker 验证)**：\n- ✅ **VERDICT: CONSISTENT — V-shape 是真实现象，非 bug**\n- 模型路径: MATCH（两组实验均使用 /root/autodl-tmp/pi05_libero_finetuned, 7.47GB, 自 May 22 未变）\n- 脚本: MATCH（eval_pi05_pruning_libero.py，May 26 05:43 修改过但不影响 random pruning 逻辑——k=0.85 v1 和 v2 结果完全一致 44.4%）\n- 参数: 仅 keep_ratio 不同（k=0.7: 179/256 tokens, k=0.85: 217/256 tokens）\n- 环境变量: MATCH（HF_HUB_OFFLINE=1, TRANSFORMERS_OFFLINE=1, 等）\n- 跨 seed 一致: k=0.85 seed43=42.0%, k=0.7 seed43=68.6%\n\n**根因（per-task 分析）**：V-shape 主要由 **T4 (put mugs on plates)** 驱动：\n- k=0.7: T4=80% (s42), 86% (s43)\n- k=0.85: T4=12% (s42), 4% (s43) — **灾难性下降**\n- T0 也有大差距: k=0.7=100%, k=0.85=52%\n\n**机制解释**：Random pruning 在 k=0.85 时保留的 217/256 tokens 恰好系统性丢弃了 T4 任务所需的关键 spatial tokens，而 k=0.7 保留 179 tokens 时的随机采样反而保留了这些 tokens（或者说在更低 token 数下模型能通过其他 token 补偿）。这不是随机噪声——跨 seed、跨独立运行完全复现。\n\n**论文意义**：V-shape 是 random pruning 的固有缺陷——无法保证关键 token 不被丢弃，且这种丢弃在特定 keep ratio 上是系统性的。与 L2norm 的平滑单调下降形成对比，支持 importance-aware scoring 的必要性。\n\n## 13. L2norm Method Gap 是恒定的，不随 Pruning Ratio 缩小 (2026-05-26)\n\n**发现**：OpenVLA L2norm k=0.95 Object = 70.6% = L2norm k=0.9 Object = 70.6%，完全相同。\n\nbaseline Object = 74%，即 method gap = -3.4pp，无论去掉 5% 还是 10% token，损失完全一样。\n\n**解释**：L2norm scoring 在 MLP connector 上的偏差是系统性的——它总是\"错误\"地排序某些关键 token，使得即使只去极少量 token，最先被去掉的恰好包含关键信息。这不是量的问题（prune 多少），是质的问题（scoring 偏差是固有的）。\n\n**论文意义**：method gap 不是 pruning ratio 的函数——是 scoring method × connector 交互的**固有属性**。可以加强 \"intrinsic method gap\" claim，与 Goal 上双方法免疫（Attn k=0.85≈baseline, L2norm k=0.85>baseline）形成鲜明对比：同一方法在不同 task 上表现完全不同。\n\n## 14. GPU 诊断 2026-05-27 (07:33 UTC)\n\n### cqa1-33015 (4× RTX 4090 D, 24GB)\n| GPU | Mem Used | Util | PID | Experiment |\n|-----|----------|------|-----|-----------|\n| 0 | 1 MiB | 0% | — | **IDLE** |\n| 1 | 1 MiB | 0% | — | **IDLE** |\n| 2 | 10208 MiB | 44% | 790017 | π0.5 attn k=0.5 Long s42 (tmux: eval_attn_k05_long_s42) |\n| 3 | 10495 MiB | 16% | 732826 | π0.5 random k=0.7 Long s42 (log: eval_pi05_random_k07_long_seed42.log) |\n\n**注**：eval_pi05_attn_k095_long_seed42 (PID 546282) 已完成 (SR=77.0%, EXIT_CODE=0, 04:20 UTC)，GPU 3 已被新实验占用。\n\n### westd-38929 (4× RTX PRO 6000 Blackwell, 98GB)\n| GPU | Mem Used | Util | PID | Experiment |\n|-----|----------|------|-----|-----------|\n| 0 | 15780 MiB | 43% | 623613 | OV L2norm k=0.5 Long s42 ✅ registry |\n| 1 | 15780 MiB | 70% | 668245 | OV Random k=0.85 Long s42 v3 ✅ registry (parent PID 668236) |\n| 2 | 16212 MiB | 48% | 732931 | OV L2norm k=0.75 Long s42 ✅ registry (parent PID 732922) |\n| 3 | 15964 MiB | 89% | 811418 | OV Random k=0.75 Goal s42 (NOT in registry) |\n\n### westd-41074 (4× RTX PRO 6000 Blackwell, 98GB)\n| GPU | Mem Used | Util | PID | Experiment |\n|-----|----------|------|-----|-----------|\n| 0 | 15480 MiB | 0%* | 856148 | OV Random k=0.75 Object s42 (NOT in registry; 0% util = momentary, CPU active) |\n| 1 | 16358 MiB | 82% | 856656 | OV Random k=0.75 Long s42 ✅ registry |\n| 2 | 15980 MiB | 84% | 934369 | OV Random k=0.95 Object s42 (NOT in registry) |\n| 3 | 16212 MiB | 80% | 824210 | OV Attn k=0.75 Long s42 ✅ registry |\n\n### westd-27271 (2× RTX PRO 6000 Blackwell, 98GB)\n| GPU | Mem Used | Util | PID | Experiment |\n|-----|----------|------|-----|-----------|\n| 0 | 15964 MiB | 70% | 499267 | OV Attn k=0.75 Goal s42 ✅ registry |\n| 1 | 15780 MiB | 74% | 397225 | OV Attn k=0.5 Long s42 ✅ registry |\n\n### 汇总\n- **总 GPU**: 14\n- **在跑**: 12\n- **空闲**: 2 (cqa1-33015 GPU 0, GPU 1)\n- **可立即部署**: cqa1-33015 GPU 0, GPU 1 (RTX 4090 D 24GB, 仅适合 π0.5 实验)\n\n### Cron 实验定位\n- eval_openvla_l2norm_k05_long_seed42 (PID 623613) → **westd-38929 GPU 0** ✅ confirmed\n- eval_openvla_attn_k05_long_seed42 (PID 397225) → **westd-27271 GPU 1** ✅ confirmed\n\n### 未在 registry 中但实际在跑的实验\n- cqa1 GPU 2: π0.5 attn k=0.5 Long s42 (PID 790017)\n- cqa1 GPU 3: π0.5 random k=0.7 Long s42 (PID 732826)\n- westd-38929 GPU 3: OV random k=0.75 Goal s42 (PID 811418)\n- westd-41074 GPU 0: OV random k=0.75 Object s42 (PID 856148)\n- westd-41074 GPU 2: OV random k=0.95 Object s42 (PID 934369)\n\n### Registry 更新\n- eval_pi05_attn_k095_long_seed42: RUNNING → DONE (success), SR=77.0%\n\n## 15. Paper 数据更新通知 2026-05-27\n\n**以下新数据点已确认，需要更新到论文 cliff curve 图表中。Paper Agent 请在下次 session 处理。**\n\n### π0.5 Long Cliff Curve 更新\n| k | Method | SR | Registry ID |\n|---|--------|----|-------------|\n| 0.7 | Attention | 50.8% | eval_pi05_attention_k07_long_seed42_v2 |\n| 0.7 | L2norm | 63.2% | eval_pi05_l2norm_k07_long_seed42 |\n| 0.5 | Attention | 49.8% | eval_pi05_attention_k05_long_seed42_v2 (D239) |\n\n### OpenVLA Long Cliff Curve 更新\n| k | Method | SR | Registry ID | 备注 |\n|---|--------|----|-------------|------|\n| 0.85 | Attention | 45.8% | eval_openvla_attn_k085_long_seed42_v5 | confirmed non-noise |\n\n### OpenVLA Object Cliff Curve 更新\n| k | Method | SR | Registry ID |\n|---|--------|----|-------------|\n| 0.75 | Attention | 53.2% | eval_openvla_attn_k075_object_seed42 |\n\n### OpenVLA Goal Cliff Curve 更新\n| k | Method | SR | Registry ID |\n|---|--------|----|-------------|\n| 0.5 | Random | 52.2% | eval_openvla_random_k05_goal_seed42 |\n\n## 16. Claim 覆盖度审计 2026-05-27\n\n**审计时间**: 2026-05-27 ~08:00 UTC | **截止**: 2026-05-28 12:00 UTC (20:00 BJT) | **剩余**: ~28h\n\n### 一、Core Claims 数据支撑状态\n\n#### Claim 1: 2-Axis Compressibility Framework (connector × task complexity)\n| 所需证据 | 状态 | 数据来源 |\n|----------|------|----------|\n| 5 models × CV spectrum (0.038→0.314) | ✅ | π0=0.038, π0.5=0.055, X-VLA=0.151, OpenVLA=0.215, OFT=0.219, SmolVLA=0.314 |\n| X-VLA cross-suite: Object 97.6% vs Goal 70.2% at k=0.9 | ✅ | eval_xvla_prune_k09 系列 |\n| X-VLA Long k=0.95 ~53% (-45pp) | ✅ | eval_xvla_l2norm_k095_long (SR=47.0%), eval_xvla_random_k095_long (SR=48.2%) |\n| SmolVLA catastrophic 0% at k=0.95 | ✅ | dual-seed, official checkpoint, 4 suites |\n| OpenVLA cliff curves (Object/Goal/Long) | 🏃 部分在跑 | 见下方 cliff curve 表 |\n| π0.5 cliff curves (Long) | 🏃 2/18 在跑 | 见下方 cliff curve 表 |\n**风险: ✅ 核心证据完备。** Cliff curves 是补充性 figure 数据，不影响 claim 成立。\n\n#### Claim 2: Pixel Shuffle Irreversible Token Entanglement\n| 所需证据 | 状态 | 数据来源 |\n|----------|------|----------|\n| SmolVLA k=0.95 = 0% (dual-seed) | ✅ | seed42=0.0%, seed43=0.2% |\n| 多方法均 0% (L2norm/Random/Sobel) | ✅ | 6+ 实验全部 0% |\n| Official HF checkpoint 确认 | ✅ | eval_smolvla_official_* |\n| Cross-suite (Object/Spatial/Goal/Long 均 0%) | ✅ | smolvla_*_k095_{goal,long,spatial} |\n**风险: ✅ 完备，无缺口。**\n\n#### Claim 3a: Linear Projection → Depends on Effective Pipeline\n| 所需证据 | 状态 | 数据来源 |\n|----------|------|----------|\n| π0 immune at k=0.1 (norm_L1=0.976) | ✅ | offline analysis |\n| X-VLA full 8-point curve | ✅ | 8 k values confirmed |\n| X-VLA cliff localization (3-seed k=0.80/0.85) | ✅ | SD<1pp, fully deterministic |\n| X-VLA random REVERSAL at k=0.5 (+28pp) | ✅ | multi-seed confirmed |\n| X-VLA cross-suite (Object/Spatial/Goal) | ✅ | D117, D123 |\n**风险: ✅ 完备。**\n\n#### Claim 3b: MLP Projector → Graded Degradation\n| 所需证据 | 状态 | 数据来源 |\n|----------|------|----------|\n| OpenVLA 6-point curve (k=1.0→0.3) | ✅ | 74.0%→69.4%→62.0%→49.0%→37.4%→20.6% |\n| Method independence (L2norm≈Random) | ✅ | k=0.95: 69.4% vs 69.2% |\n| OFT entropy/CV analysis | ✅ | CV=0.219≈OpenVLA=0.215 |\n| CogACT literature comparison | ✅ | 74.8%→74.2% under 78% pruning |\n**风险: ✅ 完备。**\n\n#### Claim 4: VTR Learned Re-Encoding\n| 所需证据 | 状态 | 数据来源 |\n|----------|------|----------|\n| SmolVLA VTR M-sweep (5 M, 3-seed) | ✅ | M=16 56.9% → M=128 58.0% |\n| M-curve flat (D105) | ✅ | 所有 M within ±3pp of baseline |\n| Architecture independence (VTC vs MLP adapter) | ✅ | p=0.150, not significant |\n| Cross-suite VTR (Spatial 53.2%, Goal 56.4%) | ✅ | confirmed |\n| VTR on OpenVLA MLP = 0% (failed) | ✅ | D109 confirmed |\n**风险: ✅ 完备。**\n\n#### Claim 5: CV Predicts Optimal Pruning Strategy (Monotonic Diagnostic)\n| 所需证据 | 状态 | 数据来源 |\n|----------|------|----------|\n| k=0.5: π0.5(+36pp) → X-VLA(+26.9pp) → OpenVLA(-1.8pp) | ✅ | D139, multi-seed |\n| k=0.7: π0.5(+22.2pp) → X-VLA(+6.5pp) → OpenVLA(-5.4pp) | ✅ | D142, dual-seed |\n| Monotonic trend confirmed at both k | ✅ | paper_framing verified |\n| Cross-seed validation Goal k=0.9 三方法 | ✅ | L2n Δ=0.4pp, Rand Δ=0.8pp, Attn Δ=0 |\n**风险: ✅ 完备。**\n\n### 二、Cliff Curve 完整性（论文 Figure 数据）\n\n#### OpenVLA Object (18 cells)\n| k | L2norm | Attn | Random |\n|---|--------|------|--------|\n| 0.95 | ✅ 70.6% | 🏃 running | 🏃 running |\n| 0.9 | ✅ 70.6% | ✅ 61.4% | ✅ 62.8% |\n| 0.85 | ✅ 55.2% | ✅ 55.0% | ✅ 60.4% |\n| 0.75 | ✅ 57.4% | ✅ 53.2% | 🏃 running |\n| 0.7 | ✅ 49.8% | ✅ 43.8% | ✅ 44.4% |\n| 0.5 | ✅ 39.2% | ✅ 40.6% | ✅ 35.8% |\n**完成度: 15/18 ✅ + 3 🏃** — 每个方法至少 5 个数据点，figure 可画。\n\n#### OpenVLA Goal (18 cells)\n| k | L2norm | Attn | Random |\n|---|--------|------|--------|\n| 0.95 | 🏃 running | ❌ **未部署** | ❌ **未部署** |\n| 0.9 | ✅ 74.8% | ✅ 73.2% | ✅ 79.6% |\n| 0.85 | ✅ 75.4% | ✅ 74.6% | ✅ 78.6% |\n| 0.75 | ✅ 70.2% | ⚠️ failed, 可能重跑中 | 🏃 running (on server) |\n| 0.7 | ✅ 68.4% | ✅ 66.4% | ✅ 68.4% |\n| 0.5 | ✅ 43.4% | ✅ 44.2% (D244) | ✅ 52.2% |\n**完成度: 13/18 ✅ + 2 🏃 + 2 ❌ + 1 ⚠️** — 每个方法至少 4 个点（无 k=0.95），figure 可画但不完整。\n\n#### OpenVLA Long (18 cells)\n| k | L2norm | Attn | Random |\n|---|--------|------|--------|\n| 0.95 | ❌ **未部署** | ❌ **未部署** | 🏃 running |\n| 0.9 | ✅ 43.6% | ✅ 44.0% | ✅ 46.8% |\n| 0.85 | ✅ 38.8% | ✅ 45.8% | ✅ 45.0% |\n| 0.75 | 🏃 running | 🏃 running | 🏃 running |\n| 0.7 | ✅ 31.2% | ✅ 24.0% | ✅ 38.8% |\n| 0.5 | 🏃 running | 🏃 running | ✅ 18.6% |\n**完成度: 10/18 ✅ + 6 🏃 + 2 ❌** — 完成度最低。若 running 全完成则 16/18。\n\n#### π0.5 Long (18 cells)\n| k | L2norm | Attn | Random |\n|---|--------|------|--------|\n| 0.95 | ✅ 87.0% | ✅ 77.0% | ✅ 63.2% |\n| 0.9 | ✅ 81.0% | ✅ 63.8% | ✅ ~32% |\n| 0.85 | 🏃 running | ✅ 51.6% | ✅ 44.4% |\n| 0.75 | ✅ 73.4% | ✅ 51.8% | ✅ 62.4% |\n| 0.7 | ✅ 63.2% | ✅ 50.8% | 🏃 running |\n| 0.5 | ✅ 50.0% | ✅ 49.8% | ✅ 50.2% |\n**完成度: 16/18 ✅ + 2 🏃** — 接近完成。\n\n#### Cliff Curve 汇总\n| | ✅ 完成 | 🏃 在跑 | ❌ 未部署 | ⚠️ 异常 |\n|---|---------|---------|-----------|---------|\n| Object | 15 | 3 | 0 | 0 |\n| Goal | 13 | 2 | 2 | 1 |\n| Long | 10 | 6 | 2 | 0 |\n| π0.5 Long | 16 | 2 | 0 | 0 |\n| **合计** | **54/72 (75%)** | **13 (18%)** | **4 (6%)** | **1 (1%)** |\n\n### 三、关键缺口清单\n\n#### ❌ 未部署（必须尽快行动）\n1. **Goal k=0.95 Attn** — cliff curve 顶端数据点\n2. **Goal k=0.95 Random** — cliff curve 顶端数据点\n3. **Long k=0.95 L2norm** — cliff curve 顶端数据点\n4. **Long k=0.95 Attn** — cliff curve 顶端数据点\n\n**约束**: 需 Blackwell GPU (98GB)，当前 0 张空闲。需等 running 实验完成后部署。每个实验约 4h。\n\n#### ⚠️ 可能异常\n5. **Goal k=0.75 Attn** — registry 标记 DONE/failed，GPU 诊断显示可能在重跑但不确定\n\n#### 🏃 在跑（预计 6-12h 内完成）\n- Object: k=0.95 Attn/Random, k=0.75 Random (3)\n- Goal: k=0.95 L2norm, k=0.75 Random (2)\n- Long: k=0.95 Random, k=0.75 ×3, k=0.5 L2norm/Attn (6)\n- π0.5: k=0.85 L2norm, k=0.7 Random (2)\n\n### 四、Crossover Table 16/16\nROADMAP 标记 ✅ 完成。\n\n### 五、Cross-seed 验证\nGoal k=0.9 三方法全部通过：\n- L2norm: s42=74.8%, s43=75.2% (Δ=0.4pp) ✅\n- Random: s42=79.6%, s43=80.4% (Δ=0.8pp) ✅\n- Attn: s42=73.2%, s43=73.2% (Δ=0pp) ✅\n\n### 六、建议\n\n**Deadline 前必须补（blocking）:**\n- 4 个 k=0.95 ❌ 实验：GPU 空出后立即部署（估计 May 27 下午开始有 GPU 释放）\n- 确认 Goal k=0.75 Attn 状态：是否在重跑？若没有则立即部署\n\n**Nice-to-have（不阻塞论文）:**\n- 全部 13 个 running 实验正常完成（预计无问题）\n- k=0.95 全齐后 cliff curve 图更完整，但即使缺少也可从 k=0.9 起画\n\n**无需担心:**\n- 5 条 core claims 的核心证据全部到位，**没有任何 claim 因数据缺失而无法成立**\n- Crossover table 16/16、cross-seed 验证均已完成\n- VTR 数据完整\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "c2438210-3559-463e-b203-06cfa19a4b13",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WRoPBp872VmLGVQijjwDSf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4622,
      "cache_read_input_tokens": 73117,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4622
      },
      "output_tokens": 9,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Tool result

_source line 41 · 2026-05-27T01:17:13.922Z_

<details><summary>↩ Tool result · `toolu_01EasHxvSF1GSCebGFJim4JU`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "d3295780-5aec-4712-bc35-366622955431",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\\\", \\\"saved\\\": true}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0515-2/projects/importance_margin_vla_compress/memory.md\", \"saved\": true}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---


### Assistant

_source line 42_

## Claim 覆盖度审计 Checklist

### Core Claims — 全部 ✅ 有数据支撑
| Claim | 状态 | 说明 |
|-------|------|------|
| C1: 2-Axis Framework (connector × task) | ✅ | 5 models, CV spectrum, X-VLA cross-suite 全齐 |
| C2: Pixel Shuffle Irreversible | ✅ | dual-seed + official checkpoint + 4 suites |
| C3a: Linear Pipeline Dependency | ✅ | π0 immune + X-VLA 8-point + random reversal |
| C3b: MLP Graded Degradation | ✅ | OpenVLA 6-point + OFT entropy + method independence |
| C4: VTR Learned Re-Encoding | ✅ | M-sweep + flat curve + arch independence + cross-suite |
| C5: CV Predicts Strategy | ✅ | k=0.5 & k=0.7 monotonic trend + multi-seed |

### Cliff Curves — 54/72 (75%) 完成
| Curve | 完成 | 在跑 | 缺失 |
|-------|------|------|------|
| OpenVLA Object | 15/18 | 3 | 0 |
| OpenVLA Goal | 13/18 | 2 | 3 |
| OpenVLA Long | 10/18 | 6 | 2 |
| π0.5 Long | 16/18 | 2 | 0 |

### 关键缺口（4 个未部署 k=0.95 实验）
1. ❌ Goal k=0.95 Attn — 需 Blackwell GPU
2. ❌ Goal k=0.95 Random — 需 Blackwell GPU
3. ❌ Long k=0.95 L2norm — 需 Blackwell GPU
4. ❌ Long k=0.95 Attn — 需 Blackwell GPU

**当前 0 张 Blackwell GPU 空闲**，需等 running 实验完成后立即部署（每个约 4h，deadline 还有 ~28h，可以赶上）。

### 结论
**所有 5 条 core claims 的核心证据已完备，论文写作不受阻。** 唯一风险是 4 个 k=0.95 cliff curve 顶端数据点未部署，需在 GPU 释放后立即行动。即使这些实验未完成，cliff curve 可从 k=0.9 起画，不影响 claim 成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "uuid": "eddb1547-4529-4435-a293-f402b2caaff5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017eRWR3pYMnVajKjcSQtQVA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12647,
      "cache_read_input_tokens": 77739,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12647
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---


### Task result

_source line 43_

## Claim 覆盖度审计 Checklist

### Core Claims — 全部 ✅ 有数据支撑
| Claim | 状态 | 说明 |
|-------|------|------|
| C1: 2-Axis Framework (connector × task) | ✅ | 5 models, CV spectrum, X-VLA cross-suite 全齐 |
| C2: Pixel Shuffle Irreversible | ✅ | dual-seed + official checkpoint + 4 suites |
| C3a: Linear Pipeline Dependency | ✅ | π0 immune + X-VLA 8-point + random reversal |
| C3b: MLP Graded Degradation | ✅ | OpenVLA 6-point + OFT entropy + method independence |
| C4: VTR Learned Re-Encoding | ✅ | M-sweep + flat curve + arch independence + cross-suite |
| C5: CV Predicts Strategy | ✅ | k=0.5 & k=0.7 monotonic trend + multi-seed |

### Cliff Curves — 54/72 (75%) 完成
| Curve | 完成 | 在跑 | 缺失 |
|-------|------|------|------|
| OpenVLA Object | 15/18 | 3 | 0 |
| OpenVLA Goal | 13/18 | 2 | 3 |
| OpenVLA Long | 10/18 | 6 | 2 |
| π0.5 Long | 16/18 | 2 | 0 |

### 关键缺口（4 个未部署 k=0.95 实验）
1. ❌ Goal k=0.95 Attn — 需 Blackwell GPU
2. ❌ Goal k=0.95 Random — 需 Blackwell GPU
3. ❌ Long k=0.95 L2norm — 需 Blackwell GPU
4. ❌ Long k=0.95 Attn — 需 Blackwell GPU

**当前 0 张 Blackwell GPU 空闲**，需等 running 实验完成后立即部署（每个约 4h，deadline 还有 ~28h，可以赶上）。

### 结论
**所有 5 条 core claims 的核心证据已完备，论文写作不受阻。** 唯一风险是 4 个 k=0.95 cliff curve 顶端数据点未部署，需在 GPU 释放后立即行动。即使这些实验未完成，cliff curve 可从 k=0.9 起画，不影响 claim 成立。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 593931,
  "duration_api_ms": 593210,
  "num_turns": 13,
  "stop_reason": "end_turn",
  "session_id": "7a12e78f-6295-4999-ab31-4ef688467957",
  "total_cost_usd": 1.41558225,
  "usage": {
    "input_tokens": 12,
    "cache_creation_input_tokens": 78545,
    "cache_read_input_tokens": 441168,
    "output_tokens": 28097,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 78545,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 707,
        "cache_read_input_tokens": 77739,
        "cache_creation_input_tokens": 12647,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 12647
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1517,
      "outputTokens": 18,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001607,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 12,
      "outputTokens": 28097,
      "cacheReadInputTokens": 441168,
      "cacheCreationInputTokens": 78545,
      "webSearchRequests": 0,
      "costUSD": 1.41397525,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "4a597483-6d91-49b5-85ae-0d4902ed3664"
}
```

</details>

---
