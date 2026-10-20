# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 22
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/af67fca6-bfdd-4586-bb65-252f2dd87fb2.jsonl`
- **Structured JSON:** [`c8fd9f31d47fb11ce5bc.json`](../../sessions/c8/c8fd9f31d47fb11ce5bc.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:24:17.768Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:24:17.768Z",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer selection sensitivity is recognized as a genuine methodological contribution distinct from hyperparameter tuning. CV-validated ensemble is cosmetic, not load-bearing.\n核心假设：[\"Reviewers treat layer selection metric bias as a reproducible methodological finding (not 'you just picked the wrong hyperparameter')\", '4 models × 2 architectures × 2 scales is accepted as sufficient breadth for an empirical study', '32B caveats (R1-32B W=1 only, QwQ negative lead time) are read as honest science, not evidence of fragility', 'Comprehensive negative results (BOCPD/CUSUM/Mahalanobis/RepE/CCS/MLP all fail) are valued as community service', 'Position mediation analysis (3/4 retain non-positional HS advantage) fully resolves confound concern', 'High safe FPR (39-62%) is acceptable as acknowledged limitation for a detection-evaluation paper']\n关键指标范围：{'avg_reviewer_score': [3.5, 4.0], 'novelty_rating': [3.5, 4.0], 'soundness_rating': [4.0, 4.5], 'champions_out_of_3': [2, 3], 'ensemble_cv_impact_on_acceptance': [0.0, 0.05], 'lowest_single_reviewer': [3.0, 3.5]}\n叙事方向：Original framing fully intact. Primary contribution = layer selection sensitivity as researcher-degree-of-freedom audit. Secondary = HS advantage universal at correct layers. Tertiary = 6 methods fail. Paper title emphasizes 'layer selection matters' angle. Claims need no softening. Ensemble CV can go in appendix as supplementary validation.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: contrastive_trace_safety\nvenue: emnlp-2026\nfocus: Evaluate whether adding CV-validated ensemble results (currently p≤0.002 without CV) meaningfully improves paper acceptance probability at EMNLP 2026. Key question: does upgrading ensemble from 'preliminary' to 'CV-validated' move the needle from Findings to Main, or is it marginal? Also assess current paper state post-R30 fixes (commit 322b668) — are there any OTHER low-cost improvements the dream reviewers would prioritize?\n\n## paper_framing.md\n\n# Paper Framing — contrastive_trace_safety\n\n## Target Venue\n- Primary: EMNLP 2026 Main (LLM Security Track)\n- Deadline: ARR submission May 25, 2026\n\n## Core Claims (D031: layer selection as primary contribution, 4 models)\n\n**Contribution structure (D031)**:\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\n\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\n\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\n\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\n\n   The core insight: \"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\"\n\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \"universal\") —\n\n   **KEY FINDING (D029)**: The apparent \"scale-dependent\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\n\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\n\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\n\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\n\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\n\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\n\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\n   - 15/15 W values show significant HS advantage\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \"more accurate but detects later.\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\n\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\n   - W=5-15: all NS\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \"Scheme B选错层\" narrative weaker for R1-32B.\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\n\n   **32B cross-model divergence (D031 key finding for Discussion):**\n   | Dimension | R1-32B L63 | QwQ L60 |\n   |-----------|-----------|---------|\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\n   | Coverage (W=1) | 25% | 74% |\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\n\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\n\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\n\n   | Rank | Model | Metric | p-value | Threshold | Pass |\n   |------|-------|--------|---------|-----------|------|\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\n\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \"HS > text at each model's best setting,\" not \"at uniform W.\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\n\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\n\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\n\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\n\n   Paper recommended claim (D032): \"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\"\n\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\n\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\n\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\n\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\n\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\n- `pre_cp_fpr`: selects deep layers for all models\n- `composite` (additive): selects deep layers for all models\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\n\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\n\n**Corrected layer definition (D036)**: \"Corrected layers\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\n\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\n\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \"correct\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \"researcher degree of freedom\" with systematic audit via sensitivity analysis.\n\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \"correct vs incorrect.\"\n\n## Story Spine\n\n- **Problem**: Reasoning models exhibit \"self-jailbreak\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \"commitment point\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\n\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\n\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\n\n- **Headline result (D032)**: \"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\"\n\n## Key Evidence Summary\n\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\n\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\n\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\n|--------|----------|-----------|------------|----------|\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\n\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\n\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\n\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\n\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\n|--------|---------|-----------|----------|-----------|------|\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\n\nBootstrap (layer 16, matched W=3, 1000 resamples):\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\n\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\n\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\n- HS vs Text bootstrap (null-centered, 1000 resamples):\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\n\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\n- W=1: bal_acc +18.7pp, p<0.001 ✅\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\n\n**OLD biased-layer results (RETRACTED as metric artifact):**\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\n|-------|-------------|----------------|----------------|-------------------|\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\n\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\n\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\n\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\n\n### Position Mediation Analysis (D038 → D039 → D042 complete)\n\n**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.\n\n| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |\n|-------|---|------------|--------------|-------------|-------|-----|\n| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |\n| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |\n| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |\n| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |\n| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |\n\nPosition-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.\n\n**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).\n\n**Key implications for paper**:\n1. Position is a significant component (12-20pp drop) — universal\n2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)\n3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS\n4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)\n5. Paper framing: \"HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated\"\n\n### 5-Seed Robustness (D041)\n\n| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |\n|-------|-------------|------------------|----------------|\n| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |\n| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |\n| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |\n| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |\n\nR1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.\n\n**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). \"7-8B robust / 32B sample-limited\" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.\n\n**Per-model evidence tier (D042)**:\n- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)\n- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive\n- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)\n- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)\n\n**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).\n\n### BA-Layer Robustness: Metric Circularity Refuted (D044)\n\nR13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).\n\n| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |\n|-------|-------------|-------|-----|------|--------|-----------|\n| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |\n| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |\n| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |\n| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |\n\n**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.\n\nKey insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.\n\nCaveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.\n\n### Post-hoc Power Analysis (D044)\n\n| Model | n (test) | MDE (80% power, α=0.05) |\n|-------|----------|------------------------|\n| OT-7B | 47-69 | 6.7-8.1pp |\n| R1-8B | 43-63 | 7.4-9.0pp |\n| QwQ-32B | 29 | 9.5pp |\n| R1-32B | 20-30 | 8.6-11.2pp |\n\nAll significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.\n\n### Negative Results (expanded with R3 supplementary experiments)\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \"weakly supervised\" not \"unsupervised\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\n\n## Venue Fit Risks\n\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\n- **HS advantage universal**: UPGRADED from \"scale-dependent\" — layer selection is the true moderator, not scale. Cleaner story.\n- **Trace vs step FPR**: Both reported with explanation.\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\n\n## Anticipated Reviewer Concerns\n\n1. \"Method novelty?\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\n2. \"Only one model family?\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\n3. \"GRU unstable?\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\n4. \"Too few traces?\" → Cross-model validation + control task selectivity 7.5-18.5pp.\n5. \"Fine-grained taxonomy?\" → Out of scope for current study.\n6. \"HS doesn't beat text?\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\n7. \"Commitment point circular?\" → Cross-model consistency + control task selectivity argues against artifact.\n8. \"Missing related work?\" → Expansion to 30+ citations.\n9. \"No FPR analysis?\" → RESOLVED: both trace-level and step-level FPR reported.\n10. \"High safe FPR?\" → Limitation acknowledged.\n11. \"Control task / position confound?\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\n12. \"Multiple testing correction?\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\n13. \"Trace vs step FPR?\" → Both reported with explanation.\n14. \"Layer selection is just hyperparameter tuning?\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\n15. \"Why not just use the best layer for each model?\" → We do. The point is that the METRIC for selecting \"best\" matters. Biased metrics produce systematically wrong selections, masking real effects.\n16. \"32B results are marginal / only W=1 significant for R1-32B?\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\n\n## Title Candidates (D031)\n- \"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\"\n- \"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\"\n- \"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\"\n- \"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\"\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: Cross-architecture hidden-state extraction + layer sweep + static probe\n    evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers)\n    to find best layer for 64-layer models before probe evaluation. Validates Claim\n    1 generalizes beyond r1-8b.\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  notes: 32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44%\n    depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers\n    for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE\n    reporting static probe results — using wrong layer would produce false negative.\n  status: planned\n- id: exp-002\n  claim: 2\n  description: 'Cross-architecture temporal window evaluation: temporal LR W=15 on\n    r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ\n    (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture\n    generalization.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Key for cross-architecture story. Projection head needed (4096→5120 or vice\n    versa).\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Lead time analysis across models: confirm negative lead time finding\n    on 32B models. Report lead time distribution per model.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'TrajGuard-style Mahalanobis baseline: implement and evaluate on all\n    3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Critical baseline for 'existing detectors fail' claim. Use safe traces to\n    estimate covariance, compute MD per step.\n  status: planned\n- id: exp-006\n  claim:\n  - 1\n  - 2\n  description: 'Bootstrap confidence intervals + threshold-independent metrics: 1000\n    bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report\n    AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold\n    variance, and FPR on safe traces (final_judgment=0.5).'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  - exp-004\n  - exp-005\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal\n    W and show diminishing returns curve.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Layer selection ablation: all layers (not just 14) for temporal probe\n    on 32B models. Confirm middle-layer finding generalizes.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  claim: 2\n  description: '16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4)\n    instead of binary commitment for richer training signal. May improve both coverage\n    and timing.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Addresses reviewer concern about underusing available supervision.\n  status: planned\n- id: exp-010\n  claim: 3\n  description: 'Oracle decomposition: why can oracle but not probes achieve positive\n    lead time? Analyze what label patterns encode that hidden states don''t.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-004\n  notes: For Discussion section. May reveal what architectural changes could close\n    the gap.\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale\n    matrix. Controls for scale confound.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-002\n  notes: From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for\n    scale-matched comparison.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'GRU/Attention probe as upper bound: verify GRU finding holds on 32B\n    models with more data. If still no improvement over LR, strengthens ''simplicity\n    is optimal'' story.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) +\n    same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state\n    probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap\n    text monitoring. If text achieves comparable performance, paper motivation needs\n    restructuring.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps: []\n  notes: No GPU needed for embedding extraction (small model, CPU-feasible). Run on\n    all 4 models. This is the single most important missing baseline per Dream review\n    (flagged by all 3 tiers, both reviewers).\n  status: planned\n- id: exp-014\n  claim: 3\n  description: 'Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores:\n    apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve\n    positive lead time by detecting distributional shift before textual commitment.\n    Also test CUSUM as simpler alternative.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - exp-001\n  notes: Addresses both 'no method novelty' and 'no positive lead time' criticisms\n    simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes\n    a genuine methods contribution. If it also fails, strengthens the 'fundamental\n    limitation' narrative.\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  - 2\n  description: 'False positive analysis: run all probes (static, temporal, GRU, BOCPD)\n    on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various\n    thresholds. Essential for deployment utility claims.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - exp-001\n  - exp-002\n  notes: Dream flagged missing FPR as critical gap across median and worst tiers.\n    Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere\n    gets 100% coverage.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: diag_d1_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    best_layer_idx: 2\n    best_model_layer: 14\n    best_acc: 0.8114\n    best_f1: 0.6455\n    best_crossing_rate: 0.186\n    best_lead_mean: 8.38\n    best_lead_median: 6\n    default_layer20_acc: 0.7831\n    num_traces: 209\n    split: 125/41/43\n- exp_id: diag_d4_oracle_upper_bound\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K5_detection_rate: 100\n    K5_early_detection_rate: 76.7\n    K5_mean_lead_time: 31\n    K5_median_lead_time: 29\n    K1_early_detection_rate: 83.7\n    K8_early_detection_rate: 65.1\n    pre_cp_mean_longest_streak: 14.6\n    test_traces: 43\n- exp_id: diag_d2_pca_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fisher_orig_L12: 17.462\n    fisher_orig_L14: 17.875\n    fisher_orig_L20: 18.614\n    fisher_orig_L24: 18.106\n    fisher_pca_L12: 0.953\n    fisher_pca_L14: 0.928\n    fisher_pca_L20: 0.92\n    fisher_pca_L24: 1.111\n    var_explained_3pc: 0.166\n    test_steps: 1835\n- exp_id: diag_d3_regularized_probes\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    static_lr_acc: 0.8172\n    static_lr_crossing_rate: 0.4651\n    static_lr_lead_mean: -2\n    temporal_lr_w5_acc: 0.8274\n    temporal_lr_w5_crossing_rate: 0.6512\n    temporal_lr_w5_lead_mean: -1.18\n    temporal_lr_w10_acc: 0.8364\n    temporal_lr_w10_crossing_rate: 0.6512\n    temporal_lr_w10_lead_mean: -0.61\n    temporal_lr_w15_acc: 0.8478\n    temporal_lr_w15_crossing_rate: 0.7674\n    temporal_lr_w15_lead_mean: -1.09\n    best_temporal_delta_over_static: 1.39\n    pass_criterion_met: false\n- exp_id: diag_gru_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.8305\n    test_acc_std: 0.1856\n    crossing_rate: 0.6744\n    lead_mean: -0.207\n    lead_median: -1\n    lead_std: 13\n    positive_lead_rate: 0.345\n    n_positive_lead: 10\n    n_detected: 29\n    early_stop_epoch: 14\n    model_params: 1622913\n- exp_id: exp_gru256_multilayer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gru_single_l14:\n      acc: 0.8386\n      crossing_rate: 0.721\n      lead_mean: 3.5\n      lead_median: 0\n      pos_lead: 13/31\n    gru_multi_7l:\n      acc: 0.8094\n      crossing_rate: 0.767\n      lead_mean: 4.7\n      lead_median: 0\n      pos_lead: 13/33\n    lr_single_l14:\n      acc: 0.8172\n      crossing_rate: 0.465\n      lead_mean: -2\n      lead_median: -2\n      pos_lead: 6/20\n    lr_multi_7l:\n      acc: 0.806\n      crossing_rate: 0.395\n      lead_mean: 1.1\n      lead_median: 0\n      pos_lead: 6/17\n    delta_gru_vs_lr: 3.7\n- exp_id: exp_005_trajguard_mahalanobis\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    best_k5_crossing_rate: 0.302\n    best_k5_lead_mean: 16.4\n    best_k5_config: pca_64_p75\n    best_k3_crossing_rate: 0.605\n    best_k3_lead_mean: 20.4\n    delta_max_rate: 0.023\n    safe_md_mean: 6.66\n    jb_pre_md_mean: 6.73\n    jb_post_md_mean: 6.64\n- exp_id: exp_006_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    static_lr_acc: 0.768 [0.702,0.827]\n    static_lr_crossing: 60.4% [44.2,74.4]\n    static_lr_lead: +2.9 [-2.8,+9.5]\n    temporal_lr_acc: 0.731 [0.654,0.804]\n    temporal_lr_crossing: 60.6% [46.5,74.4]\n    temporal_lr_lead: +5.0 [-0.8,+11.9]\n    gru_single_acc: 0.790 [0.734,0.848]\n    gru_single_crossing: 51.4% [37.2,67.4]\n    gru_single_lead: -2.0 [-8.6,+4.9]\n    gru_multi_acc: 0.799 [0.742,0.854]\n    gru_multi_crossing: 51.4% [37.2,67.4]\n    gru_multi_lead: -0.4 [-6.4,+6.1]\n    paired_temporal_vs_static_lead_p: 0.19\n    paired_gru_vs_static_lead_p: 0.94\n    paired_gru_vs_temporal_lead_p: 0.99\n- exp_id: exp_013_text_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    text_static_coverage: 0.605\n    text_static_lead: 4.3\n    text_static_acc: 0.661\n    text_static_auroc: 0.7384\n    text_temporal_w15_coverage: 0.651\n    text_temporal_w15_lead: 11.5\n    text_temporal_w15_acc: 0.678\n    text_temporal_w15_auroc: 0.759\n    hs_acc_advantage: 15-18pp\n- exp_id: exp_015_fpr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    text_static_safe_fpr: 0.502\n    text_static_precp_fpr: 0.356\n    text_static_precision: 0.448\n    text_static_coverage: 0.605\n    text_static_lead: 4.3\n    text_static_acc: 0.661\n    text_temporal_safe_fpr: 0.385\n    text_temporal_precp_fpr: 0.272\n    text_temporal_precision: 0.487\n    text_temporal_coverage: 0.651\n    text_temporal_lead: 11.5\n    text_temporal_acc: 0.678\n    hs_static_safe_fpr: 0.39\n    hs_static_precp_fpr: 0.162\n    hs_static_precision: 0.622\n    hs_static_coverage: 0.605\n    hs_static_lead: 3\n    hs_static_acc: 0.768\n    hs_temporal_safe_fpr: 0.392\n    hs_temporal_precp_fpr: 0.16\n    hs_temporal_precision: 0.583\n    hs_temporal_coverage: 0.651\n    hs_temporal_lead: 4.9\n    hs_temporal_acc: 0.726\n    gru_safe_fpr: 0.521\n    gru_precp_fpr: 0.188\n    gru_precision: 0.648\n    gru_coverage: 0.744\n    gru_lead: 5.25\n    gru_acc: 0.816\n- exp_id: exp_014_bocpd_poc\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bocpd_lambda10:\n      detection_rate: 0.93\n      mean_lead: 3.45\n      median_lead: 0\n      early_count: 16\n      late_count: 19\n    bocpd_lambda100:\n      detection_rate: 0.674\n      mean_lead: 1.03\n      median_lead: 0\n    cusum_best_t03h3:\n      detection_rate: 0.651\n      mean_lead: 0.89\n      median_lead: -4\n    fcp_baseline:\n      detection_rate: 0.651\n      mean_lead: 4.89\n      median_lead: 0\n    head_to_head_bocpd_vs_fcp:\n      bocpd_wins: 16\n      fcp_wins: 6\n      ties: 5\n    verdict: BOCPD higher detection (93% vs 65%) but lower mean lead (3.45 vs 4.89).\n      CUSUM universally worse. Neither method achieves earlier detection than simple\n      threshold crossing on average.\n- exp_id: exp_001a_r1_32b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    m001_corrected: true\n    best_layer_old: 2\n    best_layer_corrected: 10\n    layer_selection_metric: balanced_accuracy × crossing_rate (scheme B)\n    layer10_bal_acc: 0.718\n    layer10_crossing_rate: 0.6\n    gru_single_bal_acc_mean: 0.675\n    gru_single_crossing_mean: 0.3\n    gru_single_lead_mean: 9.1\n    gru_single_precp_fpr_mean: 0.135\n    gru_multi_bal_acc_mean: 0.655\n    gru_multi_crossing_mean: 0.23\n    gru_multi_lead_mean: 8.8\n    gru_multi_precp_fpr_mean: 0.114\n    temporal_lr_best_window: 10\n    temporal_lr_w10_bal_acc: 0.737\n    temporal_lr_w10_crossing: 0.5\n    temporal_lr_w10_lead: 9\n    temporal_lr_w10_precp_fpr: 0.189\n    bootstrap_hs_precp_fpr: 0.26\n    bootstrap_text_precp_fpr: 0.246\n    bootstrap_diff: 0.014\n    bootstrap_p_value: 0.999\n    bootstrap_ci95:\n    - -0.103\n    - 0.127\n    bootstrap_conclusion: no_significant_difference\n    paired_bootstrap_corrected:\n      hs_bal_acc: 0.794\n      text_bal_acc: 0.711\n      acc_delta: 0.084\n      acc_p_value_two_sided: 0.08\n      hs_precision: 0.61\n      text_precision: 0.516\n      prec_delta: 0.094\n      prec_p_value_two_sided: 0.05\n      hs_precp_fpr: 0.242\n      text_precp_fpr: 0.326\n      fpr_delta: -0.084\n      fpr_p_value_two_sided: 0.114\n      bonferroni_alpha: 0.017\n      bonferroni_pass: false\n      test_type: two-sided\n      solver: liblinear\n      canonical_file: artifacts/r1_32b_paired_bootstrap/results.json\n      note: directional but ns after Bonferroni. n=20 test traces insufficient power.\n        Old m001 FPR=0.246 used lbfgs solver (non-canonical).\n- exp_id: exp_001b_qwq_32b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    m001_corrected: true\n    best_layer_old: 1\n    best_layer_corrected: 2\n    layer_selection_metric: balanced_accuracy × crossing_rate (scheme B)\n    layer2_bal_acc: 0.73\n    layer2_crossing_rate: 0.47\n    gru_single_bal_acc_mean: 0.694\n    gru_single_crossing_mean: 0.75\n    gru_single_lead_mean: 19.3\n    gru_single_precp_fpr_mean: 0.303\n    gru_multi_bal_acc_mean: 0.724\n    gru_multi_crossing_mean: 0.84\n    gru_multi_lead_mean: 15.9\n    gru_multi_precp_fpr_mean: 0.289\n    temporal_lr_best_window: 5\n    temporal_lr_w5_bal_acc: 0.761\n    temporal_lr_w5_crossing: 0.42\n    temporal_lr_w5_lead: 23.5\n    temporal_lr_w5_precp_fpr: 0.18\n    bootstrap_phase5_invalid: true\n    bootstrap_phase5_bug: M002 - text_baseline_predictions() in exp_001b_bootstrap.py\n      used midpoint heuristic, not sentence embeddings\n    corrected_hs_vs_text:\n      hs_bal_acc: 0.679\n      text_bal_acc: 0.671\n      acc_delta: 0.009\n      acc_p_value_two_sided: 0.828\n      hs_precision: 0.583\n      text_precision: 0.525\n      prec_delta: 0.057\n      prec_p_value_two_sided: 0.346\n      hs_precp_fpr: 0.208\n      text_precp_fpr: 0.178\n      fpr_delta: 0.03\n      fpr_p_value_two_sided: 0.43\n      bonferroni_alpha: 0.017\n      bonferroni_pass: false\n      test_type: two-sided\n      solver: liblinear\n      note: No significant HS vs text difference on QwQ-32B. HS FPR slightly worse\n        than text.\n    bootstrap_conclusion: no_significant_difference\n- exp_id: exp_003_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baselines:\n      r1_8b_acc: 0.8234\n      r1_32b_acc: 0.6516\n      qwq_32b_acc: 0.7171\n    best_transfer_acc:\n      r1_8b_to_r1_32b: 0.522\n      r1_8b_to_qwq: 0.5948\n      r1_32b_to_qwq: 0.5499\n      qwq_to_r1_32b: 0.6726\n      r1_32b_to_r1_8b: 0.5828\n    transfer_method: PCA projection\n    conclusion_detail: Simple PCA projection insufficient for zero-shot cross-model\n      transfer. Signal is model-specific in geometric encoding.\n- exp_id: exp_c2_control_task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_selectivity: 0.1245\n    r1_32b_selectivity: 0.075\n    r1_32b_selectivity_note: layer 10 (corrected best layer). Old layer 2 = 0.168\n    r1_32b_layer10_real_acc: 0.583\n    r1_32b_layer10_random_mean: 0.508\n    r1_32b_layer10_random_std: 0.051\n    qwq_32b_selectivity: 0.153\n    qwq_32b_selectivity_note: layer 2 (corrected from layer 1 = 0.189)\n    r1_8b_hs_pre_fpr: 0.0809\n    r1_8b_position_pre_fpr: 0.1581\n    r1_8b_cp_position_mean: 0.705\n    qwq_32b_layer2_real_acc: 0.678\n    qwq_32b_layer2_random_mean: 0.526\n    qwq_32b_layer2_random_std: 0.076\n    qwq_32b_layer2_position_acc: 0.706\n    qwq_32b_layer2_hs_pre_fpr: 0.2903\n    qwq_32b_layer2_position_pre_fpr: 0.25\n    qwq_32b_layer2_issue: position_baseline (70.6%) > HS probe (67.8%)\n- exp_id: exp_007_window_ablation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_8b:\n      W1:\n        bal_acc: 0.7783\n        precision: 0.6926\n        coverage: 0.7209\n        precp_fpr_trace: 0.1037\n        precp_fpr_step: 0.0965\n        lead_mean: 13.84\n      W3:\n        bal_acc: 0.7902\n        precision: 0.7228\n        coverage: 0.6977\n        precp_fpr_trace: 0.0988\n        precp_fpr_step: 0.085\n        lead_mean: 12.07\n      W5:\n        bal_acc: 0.781\n        precision: 0.7258\n        coverage: 0.6512\n        precp_fpr_trace: 0.0913\n        precp_fpr_step: 0.0809\n        lead_mean: 8.25\n      W10:\n        bal_acc: 0.7925\n        precision: 0.7431\n        coverage: 0.5581\n        precp_fpr_trace: 0.0865\n        precp_fpr_step: 0.0761\n        lead_mean: 10.04\n      W15:\n        bal_acc: 0.8017\n        precision: 0.7767\n        coverage: 0.5116\n        precp_fpr_trace: 0.0701\n        precp_fpr_step: 0.0639\n        lead_mean: 7.23\n      W20:\n        bal_acc: 0.8072\n        precision: 0.7862\n        coverage: 0.5349\n        precp_fpr_trace: 0.0661\n        precp_fpr_step: 0.0612\n        lead_mean: 7.43\n      W25:\n        bal_acc: 0.8095\n        precision: 0.8216\n        coverage: 0.4884\n        precp_fpr_trace: 0.0545\n        precp_fpr_step: 0.0483\n        lead_mean: 8.14\n      best_bal_acc_W: 25\n    r1_32b:\n      W1:\n        bal_acc: 0.7182\n        precision: 0.549\n        coverage: 0.8\n        precp_fpr_trace: 0.2764\n        precp_fpr_step: 0.3203\n        lead_mean: 12.88\n      W3:\n        bal_acc: 0.7252\n        precision: 0.56\n        coverage: 0.8\n        precp_fpr_trace: 0.2576\n        precp_fpr_step: 0.3064\n        lead_mean: 11.38\n      W5:\n        bal_acc: 0.7309\n        precision: 0.575\n        coverage: 0.75\n        precp_fpr_trace: 0.2393\n        precp_fpr_step: 0.2841\n        lead_mean: 11.07\n      W10:\n        bal_acc: 0.7371\n        precision: 0.6093\n        coverage: 0.7\n        precp_fpr_trace: 0.1891\n        precp_fpr_step: 0.234\n        lead_mean: 10.79\n      W15:\n        bal_acc: 0.7207\n        precision: 0.5907\n        coverage: 0.7\n        precp_fpr_trace: 0.2089\n        precp_fpr_step: 0.2451\n        lead_mean: 10.86\n      W20:\n        bal_acc: 0.6961\n        precision: 0.5628\n        coverage: 0.65\n        precp_fpr_trace: 0.2193\n        precp_fpr_step: 0.2618\n        lead_mean: 9.62\n      W25:\n        bal_acc: 0.7028\n        precision: 0.5662\n        coverage: 0.7\n        precp_fpr_trace: 0.2282\n        precp_fpr_step: 0.2646\n        lead_mean: 10.71\n      best_bal_acc_W: 10\n    qwq_32b:\n      W1:\n        bal_acc: 0.7298\n        precision: 0.5435\n        coverage: 0.7895\n        precp_fpr_trace: 0.185\n        precp_fpr_step: 0.2276\n        lead_mean: 19.73\n      W3:\n        bal_acc: 0.7452\n        precision: 0.5647\n        coverage: 0.7368\n        precp_fpr_trace: 0.175\n        precp_fpr_step: 0.2141\n        lead_mean: 20.64\n      W5:\n        bal_acc: 0.761\n        precision: 0.5733\n        coverage: 0.7368\n        precp_fpr_trace: 0.1795\n        precp_fpr_step: 0.2168\n        lead_mean: 20.07\n      W10:\n        bal_acc: 0.7469\n        precision: 0.5714\n        coverage: 0.7368\n        precp_fpr_trace: 0.1707\n        precp_fpr_step: 0.2073\n        lead_mean: 18.43\n      W15:\n        bal_acc: 0.7412\n        precision: 0.5816\n        coverage: 0.6842\n        precp_fpr_trace: 0.1605\n        precp_fpr_step: 0.1911\n        lead_mean: 15.77\n      W20:\n        bal_acc: 0.7542\n        precision: 0.6024\n        coverage: 0.6316\n        precp_fpr_trace: 0.1567\n        precp_fpr_step: 0.1789\n        lead_mean: 15.75\n      W25:\n        bal_acc: 0.7624\n        precision: 0.6177\n        coverage: 0.5789\n        precp_fpr_trace: 0.1476\n        precp_fpr_step: 0.1694\n        lead_mean: 14.91\n      best_bal_acc_W: 25\n    finding: Coverage monotonically DECREASES with W across all 3 models. Temporal\n      context creates precision-sensitivity tradeoff (higher W → higher precision,\n      lower coverage, lower FPR). R1-8B dominates (lowest FPR, highest precision).\n      QwQ-32B FPR significantly lower than R1-32B with larger lead_mean.\n- exp_id: exp_ot7b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_traces: 228\n    best_layer: 16\n    best_layer_depth_pct: 57.1\n    best_layer_score: 0.6876\n    best_hs_window: 3\n    best_hs_bal_acc: 0.688\n    best_hs_precision: 0.466\n    best_hs_pre_cp_fpr: 0.1\n    best_hs_coverage: 0.5319\n    best_hs_lead: 21.6\n    best_text_window: 25\n    best_text_bal_acc: 0.6141\n    best_text_precision: 0.3291\n    best_text_pre_cp_fpr: 0.1605\n    bootstrap_bal_acc_delta: 0.1067\n    bootstrap_bal_acc_ci95: '[0.049, 0.163]'\n    bootstrap_bal_acc_p: 0.001\n    bootstrap_bal_acc_bonf: true\n    bootstrap_precision_delta: 0.2189\n    bootstrap_precision_ci95: '[0.140, 0.296]'\n    bootstrap_precision_p: 0.001\n    bootstrap_precision_bonf: true\n    bootstrap_fpr_delta: -0.1705\n    bootstrap_fpr_ci95: '[-0.222, -0.122]'\n    bootstrap_fpr_p: 0.001\n    bootstrap_fpr_bonf: true\n    holm_bonferroni: 3/3\n    selectivity_pp: 18.3\n    selectivity_real_acc: 0.688\n    selectivity_random_mean: 0.505\n    layer0_bal_acc: 0.672\n    layer0_precision: 0.357\n    layer0_pre_cp_fpr: 0.188\n    layer16_vs_layer0: '+9.0pp bal_acc, +20.8pp precision, -8.7pp FPR. Precision Bonf:\n      L0 p=0.056 FAIL -> L16 p<0.001 PASS'\n    layer_verification: 'Layer 16 verified superior to Layer 0: 3/3 Bonferroni (was\n      2/3 on L0)'\n    r1_8b_layer_supplement: 'Full sweep layers 0-24 confirmed: best=L12 (0.7871) ~\n      L14 (0.7830), no early-layer dominance.'\n    gru_single_l16_bal_acc: 0.7246\n    gru_single_l16_coverage: 0.667\n    gru_single_l16_lead: 35.25\n    gru_single_l16_precp_fpr: 0.2904\n    gru_multi_l13_19_bal_acc: 0.7464\n    gru_multi_l13_19_coverage: 0.645\n    gru_multi_l13_19_lead: 33.61\n    gru_multi_l13_19_precp_fpr: 0.2741\n- exp_id: exp_pathb_annotation_validation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    tfidf_lr_f1: 0.5899\n    tfidf_lr_cp_agreement: 0.561\n    minilm_lr_f1: 0.5149\n    minilm_lr_cp_agreement: 0.534\n    threshold_f1: 0.9\n    threshold_cp: 0.85\n    failure_reason: Safety recall extremely low (41-46%). Simple classifiers cannot\n      distinguish subtle safety-aware expressions in CoT from regular reasoning. CP\n      MAE=5-6 sentences.\n    recommendation: Need LLM API annotation or fine-tuned DeBERTa 16-class classifier\n- exp_id: exp_r3_repe_direction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b:\n      layer: 2\n      bal_acc: 0.7491\n      precision: 0.516\n      pre_cp_fpr: 0.2264\n      coverage: 0.3953\n      lead_mean: 9.7\n    r1_32b_corrected:\n      layer: 63\n      bal_acc: 0.5588\n      precision: 0.3891\n      pre_cp_fpr: 0.4986\n      coverage: 0.6\n      lead_mean: 12\n    r1_32b_old:\n      layer: 10\n      bal_acc: 0.6707\n      precision: 0.5538\n      pre_cp_fpr: 0.2423\n      coverage: 0.45\n      lead_mean: 6.3\n    qwq_32b_corrected:\n      layer: 60\n      bal_acc: 0.7562\n      precision: 0.5118\n      pre_cp_fpr: 0.3089\n      coverage: 0.7368\n      lead_mean: 11.9\n    qwq_32b_old:\n      layer: 2\n      bal_acc: 0.6661\n      precision: 0.4193\n      pre_cp_fpr: 0.3997\n      coverage: 0.7368\n      lead_mean: 13.4\n    ot_7b:\n      layer: 16\n      bal_acc: 0.718\n      precision: 0.3733\n      pre_cp_fpr: 0.2573\n      coverage: 0.5319\n      lead_mean: 26.1\n    vs_lr_r1_8b:\n      lr_bal_acc: 0.817\n      lr_precision: 0.693\n      lr_fpr: 0.097\n      repe_weaker_acc: true\n      repe_weaker_precision: true\n    finding: 'Corrected layers: R1-32B L63 RepE degrades severely (bal_acc 0.67→0.56,\n      FPR 0.24→0.50); QwQ L60 improves (bal_acc 0.67→0.76). Both still below supervised\n      LR. Unsupervised RepE direction insufficient at any layer.'\n- exp_id: exp_r3_bocpd_ot7b_w15\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    W: 15\n    fcp_null_rate: 0.53\n    note: W=15 mismatched with OT-7B best window W=3, causing 53% traces with null\n      FCP. Results unreliable due to parameter mismatch.\n    parent_best_W: 3\n- exp_id: exp_r3_mlp_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    source: v1_per_model_json (K=5)\n    warning: 'over-parameterization: v2 had K=1 detection bug (coverage=1.0). v1 data\n      used here.'\n    caveat: OT-7B uses centered window; other models use causal window\n    r1_8b:\n      W1:\n        bal_acc: 0.806\n        precision: 0.646\n        fpr: 0.137\n        coverage: 0.767\n        lead: 14.27\n      W3:\n        bal_acc: 0.81\n        precision: 0.706\n        fpr: 0.1\n        coverage: 0.721\n        lead: 9.71\n      W5:\n        bal_acc: 0.843\n        precision: 0.595\n        fpr: 0.201\n        coverage: 0.884\n        lead: 12.89\n      W10:\n        bal_acc: 0.846\n        precision: 0.592\n        fpr: 0.206\n        coverage: 0.884\n        lead: 13.29\n      lr_W3: 0.79\n      lr_W5: 0.781\n      lr_W10: 0.793\n    r1_32b:\n      W3:\n        bal_acc: 0.713\n        precision: 0.585\n        fpr: 0.245\n        coverage: 0.8\n        lead: 9.12\n      W10:\n        bal_acc: 0.688\n        precision: 0.524\n        fpr: 0.332\n        coverage: 0.75\n        lead: 10.33\n      lr_W3: 0.725\n      lr_W10: 0.737\n    qwq_32b:\n      W5:\n        bal_acc: 0.604\n        precision: 0.339\n        fpr: 0.692\n        coverage: 0.842\n        lead: 33.19\n      W10:\n        bal_acc: 0.698\n        precision: 0.432\n        fpr: 0.428\n        coverage: 0.842\n        lead: 22.94\n      lr_W5: 0.761\n      lr_W10: 0.747\n    ot_7b:\n      W1:\n        bal_acc: 0.73\n        precision: 0.456\n        fpr: 0.165\n        coverage: 0.766\n        lead: 32.19\n      W3:\n        bal_acc: 0.747\n        precision: 0.343\n        fpr: 0.362\n        coverage: 0.872\n        lead: 41.22\n      lr_W3: 0.688\n    finding: 'MLP inconsistent vs LR: r1_8b +5pp at W5/10, ot_7b +6pp at W3, but r1_32b\n      -2 to -5pp, qwq_32b -5 to -16pp. Small datasets (r1_32b=100, qwq=95) likely\n      cause MLP overfitting. Signal linearly separable for most models.'\n- exp_id: exp_r3_bocpd_ot7b_w3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    W: 3\n    layer: 16\n    n_test: 47\n    bocpd_all_lambda:\n      detection_rate: 0\n      note: W=3 probe scores too spiky (0→1 in 1-2 steps), Gaussian model fails\n    fcp_t05_k2:\n      detection_rate: 0.894\n      mean_lead: 11.83\n      median_lead: 10.5\n    fcp_t05_k3:\n      detection_rate: 0.745\n      mean_lead: 8.71\n      median_lead: 7\n    fcp_t03_k3:\n      detection_rate: 0.787\n      mean_lead: 11.92\n      median_lead: 10\n    fcp_t05_k5:\n      detection_rate: 0.468\n      mean_lead: 5.09\n      median_lead: 4.5\n    cusum_t02_h2:\n      detection_rate: 0.745\n      mean_lead: 7.46\n      median_lead: 6\n    cusum_t03_h2:\n      detection_rate: 0.702\n      mean_lead: 6.03\n      median_lead: 5\n    vs_r1_8b:\n      r1_bocpd_l10_det: 0.93\n      ot7b_bocpd_det: 0\n      r1_fcp_det: 0.651\n      ot7b_fcp_k2_det: 0.894\n      r1_fcp_lead: 4.89\n      ot7b_fcp_k2_lead: 11.83\n    finding: 'BOCPD 0% on OT-7B (all lambdas) vs 93% on R1-8B. Commitment dynamics\n      model-specific: R1-8B gradual (BOCPD works), OT-7B abrupt (simple threshold\n      optimal). Negative result confirmed cross-model for R3-W2.'\n- exp_id: exp_r3_mahalanobis_ot7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    layer: 16\n    pca_dims_tested:\n    - 16\n    - 32\n    - 64\n    - 128\n    - 256\n    md_separation:\n      pca16: -0.048\n      pca32: 0.012\n      pca64: 0.031\n      pca128: 0.004\n      pca256: -0.093\n    safe_md_mean_pca64: 7.68\n    post_md_mean_pca64: 7.71\n    pca64_k3_false_alarm_vs_tp:\n      p50:\n        fa_rate: 0.872\n        tp_rate: 0.385\n      p75:\n        fa_rate: 0.574\n        tp_rate: 0.231\n      p90:\n        fa_rate: 0.17\n        tp_rate: 0.154\n      p95:\n        fa_rate: 0.043\n        tp_rate: 0\n    vs_r1_8b:\n      r1_safe_md: 6.66\n      r1_post_md: 6.73\n      r1_separation: 0.07\n      ot7b_safe_md: 7.68\n      ot7b_post_md: 7.71\n      ot7b_separation: 0.03\n      failure_mode: 'identical: signal in minor PCA components, not principal directions'\n    finding: 'Mahalanobis zero discriminative power on OT-7B (separation ≈ 0 across\n      all PCA dims). False alarm rate >= true positive rate at every threshold. Failure\n      mode identical to R1-8B. R3-W2 fully addressed: 3/3 methods (BOCPD/CUSUM/Mahalanobis)\n      fail consistently across both models.'\n- exp_id: exp_r3_ccs_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_8b:\n      bal_acc: 0.777\n      precision: 0.565\n      fpr: 0.191\n      coverage: 0.674\n      lead: 0.7\n    qwq_32b:\n      bal_acc: 0.731\n      precision: 0.555\n      fpr: 0.214\n      coverage: 0.684\n      lead: 2\n    r1_32b:\n      bal_acc: 0.703\n      precision: 0.507\n      fpr: 0.41\n      coverage: 0.9\n      lead: 5.2\n    ot_7b:\n      bal_acc: 0.692\n      precision: 0.319\n      fpr: 0.344\n      coverage: 0.809\n      lead: 20.5\n    vs_supervised_lr_r1_8b:\n      lr_bal_acc: 0.817\n      lr_precision: 0.693\n      lr_fpr: 0.097\n      ccs_weaker: true\n    vs_repe_r1_8b:\n      repe_bal_acc: 0.749\n      ccs_better: true\n    finding: CCS is best unsupervised method (beats RepE) but still significantly\n      below supervised LR. All models needed polarity flip. FPR 0.19-0.41 across all\n      models confirms unsupervised gap.\n- exp_id: exp_r3_r1_32b_l63_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: null-centered two-sided bootstrap\n    W1:\n      bal_acc_delta: 0.187\n      bal_acc_p: 0\n      precision_delta: 0.154\n      precision_p: 0\n      fpr_delta: -0.146\n      fpr_p: 0.007\n      bonferroni_pass: 3/3\n    W3:\n      bal_acc_delta: 0.112\n      bal_acc_p: 0.02\n      precision_delta: 0.13\n      precision_p: 0.032\n      fpr_delta: -0.114\n      fpr_p: 0.077\n      bonferroni_pass: 0/3\n    W5:\n      bal_acc_delta: 0.097\n      bal_acc_p: 0.046\n      bonferroni_pass: 0/3\n    W10:\n      bal_acc_p: 0.384\n      bonferroni_pass: 0/3\n    W15:\n      bal_acc_p: 0.075\n      bonferroni_pass: 0/3\n    finding: W=1 significant 3/3 Bonferroni (alpha=0.0167). W3+ all fail after Bonferroni.\n      Confirms HS advantage exists at L63 but only robust at minimal temporal context.\n- exp_id: exp_r3_qwq_l60_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: null-centered two-sided bootstrap (bugfixed)\n    bug_fixed: missing np.mean(bd) centering caused p~0.5\n    W1:\n      bal_acc_ci: '[0.15,0.29]'\n      bal_acc_p: 0\n      precision_ci: '[0.21,0.39]'\n      precision_p: 0\n      fpr_ci: '[-0.23,-0.12]'\n      fpr_p: 0\n    W3:\n      bal_acc_p: 0\n      precision_p: 0\n      fpr_p: 0.004\n      precision_delta: 0.236\n      fpr_delta: -0.098\n    W5:\n      bal_acc_p: 0\n      precision_p: 0\n      fpr_p: 0.011\n    W10:\n      bal_acc_p: 0\n      precision_p: 0.016\n      fpr_p: 0.009\n    W15:\n      bal_acc_p: 0.004\n      precision_p: 0.003\n      fpr_p: 0.007\n    bonferroni_summary: 15/15 pass (alpha=0.0167)\n    finding: All 15 tests significant after bugfix. QwQ L60 shows robust HS advantage\n      across all windows, consistent with OT-7B. scale-dependent claim falsified.\n- exp_id: exp_r3_layer_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models_tested: 4\n    metrics_tested: 5\n    bias_discovered: bal_acc x crossing_rate systematically selects shallow layers\n    qwq_32b:\n      biased_layer: 2\n      corrected_layer: 60\n      bal_acc_gain: +1.75pp\n      precision_gain: +11.5pp\n      fpr_reduction: -8.3pp\n    r1_32b:\n      biased_layer: 10\n      corrected_layer: 63\n      bal_acc_gain: +3.7pp\n      precision_gain: +4.1pp\n      fpr_reduction: -4.3pp\n    r1_8b:\n      biased_layer: 0\n      best_layer: 12\n      consistency: L12-L16 cluster, current L14 near-optimal\n    ot_7b:\n      biased_layer: 0\n      best_layer: 9\n      current_layer: 16\n      note: 4 metrics select 4 different layers\n    cross_metric_consistency:\n      r1_8b: CONSISTENT\n      r1_32b: VARIED (all point deep)\n      qwq_32b: VARIED (all point deep)\n      ot_7b: VARIED\n    finding: crossing_rate biases layer selection to shallow layers. Pure bal_acc/precision\n      select mid-to-deep layers (40-95% depth). R1-32B and QwQ affected most severely.\n- exp_id: exp_r3_mahalanobis_r1_32b_qwq\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_32b:\n      layer: 63\n      safe_md: 6.73\n      post_md: 6.88\n      separation: 0.15\n      best_pca: 64\n    qwq_32b:\n      layer: 60\n      safe_md: 3.22\n      post_md: 3.42\n      separation: 0.2\n      best_pca: 16\n    cross_model_summary:\n      r1_8b_sep: 0.07\n      ot_7b_sep: 0.03\n      r1_32b_sep: 0.15\n      qwq_32b_sep: 0.2\n      max_separation: 0.2\n      all_fail: true\n    finding: 4/4 models Mahalanobis fails. Max separation 0.20 (QwQ), false alarm\n      rate >= true positive at every threshold. Signal in minor PCA components, not\n      principal directions.\n- exp_id: exp_r3_bocpd_r1_32b_qwq\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_32b:\n      layer: 10\n      W: 10\n      bocpd_det: 0\n      cusum_det: 0.85\n      cusum_lead: 2.59\n      fcp_det: 0.95\n      fcp_lead: 5.68\n    qwq_32b:\n      layer: 2\n      W: 5\n      bocpd_det: 0\n      cusum_det: 0.737\n      cusum_lead: 9.86\n      fcp_det: 0.789\n      fcp_lead: 9.4\n    cross_model_bocpd:\n      r1_8b: 0.93\n      r1_32b: 0\n      ot_7b: 0\n      qwq_32b: 0\n      only_r1_8b_works: true\n    finding: BOCPD 0% on 3/4 models (only R1-8B exception at 93%). CUSUM universally\n      inferior to simple FCP threshold. Advanced change-point methods fail for safety\n      commitment detection.\n- exp_id: exp_r3_coverage_bias\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b:\n      total: 268\n      included: 209\n      excluded: 59\n      exclusion_rate: 0.22\n    r1_32b:\n      total: 100\n      excluded: 0\n      exclusion_rate: 0\n    qwq_32b:\n      total: 95\n      excluded: 0\n      exclusion_rate: 0\n    exclusion_reason: All 59 excluded traces are jailbreak with no safety reasoning\n      phase (no commitment point annotatable)\n    length_test:\n      excluded_mean: 38\n      included_mean: 46.3\n      mann_whitney_p: 0.0001\n      excluded_shorter: true\n    finding: 22% exclusion in R1-8B is task-definitional (no CP to annotate), not\n      sampling bias. R1-32B/QwQ 0% exclusion. Coverage metric valid within annotatable\n      population.\n- exp_id: exp_r3_selectivity_ci_raw\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    feature_type: raw 5120-d (no PCA)\n    real_acc: 0.584\n    random_mean: 0.508\n    selectivity_pp: 7.6\n    bootstrap_mean_pp: 8.4\n    bootstrap_std_pp: 6.7\n    ci_95: '[-3.9, 22.7]pp'\n    p_value: 0.107\n    significant: false\n    vs_pca128:\n      pca128_selectivity: 15.9\n      pca128_p: 0\n      pca128_ci: '[9.7, 21.9]pp'\n    finding: Raw 5120-d selectivity 7.6pp not significant (p=0.107, CI includes 0).\n      Under-determined n&lt;p without PCA. PCA-128 gives 15.9pp (p<0.001) — dimensionality\n      reduction needed for reliable selectivity.\n- exp_id: exp_r3_gru_per_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    split: 70/30\n    bal_acc:\n      mean: 0.772\n      std: 0.038\n      min: 0.729\n      max: 0.833\n    crossing_rate:\n      mean: 0.711\n      std: 0.121\n    lead_mean:\n      mean: 8.2\n      std: 2.9\n    fpr:\n      mean: 0.229\n      std: 0.075\n    vs_single_seed:\n      single_seed_bal_acc: 0.839\n      multi_seed_mean: 0.772\n      delta: -0.067\n      note: Single seed (0.839) is optimistic; multi-seed mean (0.772) more representative\n    finding: GRU robust across 5 seeds (std=3.8pp < 5pp threshold). Single-seed result\n      overestimates by ~6.7pp. Lead time high variance (std=2.9) indicates sensitivity\n      to data split.\n- exp_id: exp_r3_selectivity_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwq_32b_l60:\n      real_acc: 0.667\n      random_mean: 0.523\n      random_std: 0.051\n      selectivity_pp: 14.4\n      position_baseline_acc: 0.705\n      layer: 60\n    r1_32b_l63:\n      real_acc: 0.746\n      random_mean: 0.549\n      random_std: 0.06\n      selectivity_pp: 19.7\n      position_baseline_acc: 0.624\n      layer: 63\n    comparison:\n      qwq_old_l2: 15.3\n      qwq_new_l60: 14.4\n      r1_32b_old_l10: 7.5\n      r1_32b_new_l63: 19.7\n    both_pass_5pp: true\n    finding: Both corrected layers pass 5pp threshold. R1-32B selectivity dramatically\n      improves from 7.5pp (L10) to 19.7pp (L63). QwQ stable (15.3→14.4pp). Deep layers\n      encode stronger safety signal beyond positional confounds.\n- exp_id: exp_r3_bootstrap_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_resamples: 10000\n    holm_bonferroni: 12/12 pass\n    tests:\n      r1_8b_bal_acc:\n        delta: 0.1796\n        p: 0\n        rank: 1\n      r1_8b_precision:\n        delta: 0.2786\n        p: 0\n        rank: 2\n      r1_8b_fpr:\n        delta: -0.1255\n        p: 0\n        rank: 3\n      ot_7b_precision:\n        delta: 0.2189\n        p: 0\n        rank: 4\n      ot_7b_fpr:\n        delta: -0.1705\n        p: 0\n        rank: 5\n      r1_32b_bal_acc:\n        delta: 0.1871\n        p: 0\n        rank: 6\n      r1_32b_precision:\n        delta: 0.1544\n        p: 0\n        rank: 7\n      qwq_32b_bal_acc:\n        delta: 0.1478\n        p: 0\n        rank: 8\n      qwq_32b_precision:\n        delta: 0.2349\n        p: 0\n        rank: 9\n      ot_7b_bal_acc:\n        delta: 0.1067\n        p: 0.0003\n        rank: 10\n      qwq_32b_fpr:\n        delta: -0.0952\n        p: 0.0061\n        rank: 11\n      r1_32b_fpr:\n        delta: -0.1457\n        p: 0.0096\n        rank: 12\n    marginal_tests:\n      r1_32b_fpr:\n        p: 0.0096\n        threshold: 0.05\n      qwq_32b_fpr:\n        p: 0.0061\n        threshold: 0.025\n    r1_8b_fpr_clarification: R1-8B FPR at W=3 is p<0.0001 (rank 3), not marginal.\n      The 0.044 was from old W=15 config.\n    finding: 'All 12/12 Holm-Bonferroni pass with 10000 resamples. R1-8B FPR not marginal\n      at corrected W=3. Actual marginal tests: R1-32B FPR (p=0.0096) and QwQ FPR (p=0.0061),\n      both passing comfortably.'\n- exp_id: exp_r5_auroc_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_8b:\n      auroc_best_layer: 13\n      auroc_best: 0.806\n      paper_layer: 14\n      auroc_at_paper: 0.803\n      match: near-match (adjacent, delta=0.003)\n    ot_7b:\n      auroc_best_layer: 1\n      auroc_best: 0.777\n      paper_layer: 16\n      auroc_at_paper: 0.746\n      match: no (flat landscape 0.70-0.78)\n    qwq_32b:\n      auroc_best_layer: 32\n      auroc_best: 0.839\n      paper_layer: 60\n      auroc_at_paper: 0.756\n      match: no (AUROC prefers mid-depth ~50%)\n    r1_32b:\n      auroc_best_layer: 31\n      auroc_best: 0.897\n      paper_layer: 63\n      auroc_at_paper: 0.767\n      match: no (AUROC prefers mid-depth ~50%)\n    finding: 'AUROC does NOT converge to the same deep layers. For 32B models, AUROC\n      selects mid-depth layers (~50%) vs paper''s very deep layers (>90%). R1-8B near-match\n      only. Note: worker applied PCA-256 on 32B models to handle dimensionality, which\n      may affect results.'\n- exp_id: exp_r5_pca384_control\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    holm_bonferroni: 10/12 reject\n    tests:\n      r1_8b_bal_acc:\n        pca384: 0.7001\n        text: 0.6875\n        delta: 0.0126\n        p: 0.731\n        reject: false\n      r1_8b_precision:\n        pca384: 0.8162\n        text: 0.5852\n        delta: 0.231\n        p: 0\n        reject: true\n      r1_8b_fpr:\n        pca384: 0.0668\n        text: 0.1614\n        delta: -0.0947\n        p: 0.003\n        reject: true\n      ot_7b_bal_acc:\n        pca384: 0.7558\n        text: 0.643\n        delta: 0.1128\n        p: 0\n        reject: true\n      ot_7b_precision:\n        pca384: 0.5225\n        text: 0.3545\n        delta: 0.1681\n        p: 0\n        reject: true\n      ot_7b_fpr:\n        pca384: 0.1207\n        text: 0.2477\n        delta: -0.127\n        p: 0\n        reject: true\n      qwq_bal_acc:\n        pca384: 0.8116\n        text: 0.6504\n        delta: 0.1612\n        p: 0\n        reject: true\n      qwq_precision:\n        pca384: 0.608\n        text: 0.4213\n        delta: 0.1867\n        p: 0\n        reject: true\n      qwq_fpr:\n        pca384: 0.173\n        text: 0.2871\n        delta: -0.1141\n        p: 0.038\n        reject: false\n      r1_32b_bal_acc:\n        pca384: 0.7471\n        text: 0.6461\n        delta: 0.1011\n        p: 0.011\n        reject: true\n      r1_32b_precision:\n        pca384: 0.6343\n        text: 0.4503\n        delta: 0.184\n        p: 0.002\n        reject: true\n      r1_32b_fpr:\n        pca384: 0.2256\n        text: 0.3809\n        delta: -0.1553\n        p: 0.006\n        reject: true\n    pca_explained_variance:\n      r1_8b: 0.793\n      ot_7b: 0.828\n      qwq_32b: 0.881\n      r1_32b: 0.924\n    finding: 'Modality advantage persists at matched 384d dimensionality. 10/12 Holm-Bonferroni\n      reject. Precision gains +16.8 to +23.1pp across all 4 models. Two non-rejections:\n      R1-8B bal_acc (small delta 1.3pp) and QwQ FPR (raw p=0.038, adj threshold too\n      strict).'\n- exp_id: exp_safe_trace_fpr_multimodel\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ot7b_hs_static_fpr: 0.111\n    ot7b_text_static_fpr: 0.302\n    ot7b_hs_temp_fpr: 0.175\n    ot7b_text_temp_fpr: 0.46\n    qwq_hs_static_fpr: 0.5\n    qwq_text_static_fpr: 0.325\n    qwq_hs_temp_fpr: 0.45\n    qwq_text_temp_fpr: 0.425\n    r1_32b_hs_static_fpr: 0.239\n    r1_32b_text_static_fpr: 0.31\n    r1_32b_hs_temp_fpr: 0.239\n    r1_32b_text_temp_fpr: 0.31\n- exp_id: exp_qwq_safe_fpr_correct_lr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hs_cv_acc: 0.935\n    hs_step_fpr: 0.279\n    hs_trace_fpr_k5: 0.475\n    text_cv_acc: 0.667\n    text_step_fpr: 0.394\n    text_trace_fpr_k5: 0.5\n- exp_id: exp_bge_large_text_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_hs_prec: 0.497\n    r1_8b_bge_prec: 0.436\n    r1_8b_diff: 0.058\n    r1_8b_p: 0.185\n    r1_8b_hb: false\n    ot_7b_hs_prec: 0.446\n    ot_7b_bge_prec: 0.263\n    ot_7b_diff: 0.181\n    ot_7b_p: 0\n    ot_7b_hb: true\n    r1_32b_hs_prec: 0.588\n    r1_32b_bge_prec: 0.475\n    r1_32b_diff: 0.117\n    r1_32b_p: 0.027\n    r1_32b_hb: false\n    qwq_32b_hs_prec: 0.545\n    qwq_32b_bge_prec: 0.454\n    qwq_32b_diff: 0.094\n    qwq_32b_p: 0.132\n    qwq_32b_hb: false\n    hb_pass_count: 1/4\n- exp_id: nested_cv_7_8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_mean_delta_prec: 0.174\n    r1_8b_std_delta_prec: 0.026\n    r1_8b_hs_better_folds: 5/5\n    ot_7b_mean_delta_prec: 0.164\n    ot_7b_std_delta_prec: 0.033\n    ot_7b_hs_better_folds: 5/5\n    total_hs_better: 10/10\n- exp_id: random_cp_qwq32b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    real_cp_cr_composite_layer: 4\n    real_cp_precision_layer: 63\n    real_cp_gap: 59\n    random_cp_cr_shallow_freq: 0.8\n    random_cp_precision_deep_freq: 0.2\n    metric_disagreement_replicates: false\n- exp_id: split_half_ot7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    half1_cr_composite_layer: 0\n    half2_cr_composite_layer: 0\n    half1_precision_layer: 20\n    half2_precision_layer: 26\n    half1_delta_prec: 0.262\n    half2_delta_prec: 0.154\n    cr_composite_both_shallow: true\n    threshold_both_deep: true\n    delta_precision_same_direction: true\n    delta_ba_same_direction: true\n    all_checkpoints_pass: true\n- exp_id: sf3_quadratic_residual\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_linear_gap: 0.104\n    r1_8b_linear_p: 0.0001\n    r1_8b_linear_hb: true\n    r1_8b_quad_gap: 0.103\n    r1_8b_quad_p: 0.0001\n    r1_8b_quad_hb: true\n    ot_7b_linear_gap: 0.114\n    ot_7b_linear_p: 0.0001\n    ot_7b_linear_hb: true\n    ot_7b_quad_gap: 0.098\n    ot_7b_quad_p: 0.0003\n    ot_7b_quad_hb: true\n    r1_32b_linear_gap: -0.014\n    r1_32b_linear_p: 0.598\n    r1_32b_linear_hb: false\n    r1_32b_quad_gap: 0\n    r1_32b_quad_p: 0.499\n    r1_32b_quad_hb: false\n    qwq_32b_l60_w3_linear_gap: 0.074\n    qwq_32b_l60_w3_linear_p: 0.0017\n    qwq_32b_l60_w3_linear_hb: true\n    qwq_32b_l60_w3_quad_gap: -0.01\n    qwq_32b_l60_w3_quad_p: 0.6384\n    qwq_32b_l60_w3_quad_hb: false\n    note: QwQ corrected from layer_idx=63 to L60, W=3\n- exp_id: n6_multi_metric_ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_ensemble_prec: 0.565\n    r1_8b_best_single_prec: 0.604\n    r1_8b_text_prec: 0.372\n    r1_8b_ens_vs_text_gap: 0.193\n    ot_7b_ensemble_prec: 0.506\n    ot_7b_best_single_prec: 0.473\n    ot_7b_text_prec: 0.236\n    ot_7b_ens_vs_text_gap: 0.27\n    qwq_32b_ensemble_prec: 0.578\n    qwq_32b_best_single_prec: 0.578\n    qwq_32b_text_prec: 0.374\n    qwq_32b_ens_vs_text_gap: 0.203\n    r1_32b_ensemble_prec: 0.581\n    r1_32b_best_single_prec: 0.583\n    r1_32b_text_prec: 0.476\n    r1_32b_ens_vs_text_gap: 0.105\n    all_ens_vs_text_significant: true\n    ens_vs_text_p_max: 0.002\n    ens_never_worse_than_best_single: true\n    ot_7b_ens_beats_best_single: 0.033\n- exp_id: r1_8b_full_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_layers:\n      bal_acc:\n        W1: L12\n        W3: L12\n        W5: L12\n        W15: L11\n      precision:\n        W1: L16\n        W3: L12\n        W5: L12\n        W15: L9\n      fpr:\n        W1: L16\n        W3: L9\n        W5: L9\n        W15: L8\n      crossing_rate:\n        W1: L0\n        W3: L0\n        W5: L0\n        W15: L0\n      composite:\n        W1: L16\n        W3: L12\n        W5: L12\n        W15: L9\n    max_layer_gap_same_model: 16\n    hs_vs_text_gap: 0.15-0.17 stable across all layers\n    shallow_bias_W15_only: true\n    traces: 209\n    seed: 42\n- exp_id: advbench_r1_8b_full\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: pca_artifact_verification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pca100d_best_precision: 0.633\n    nopca_best_precision: 0.732\n    pca100d_best_fpr: 0.145\n    nopca_best_fpr: 0.072\n    pca100d_best_composite: 0.43\n    nopca_best_composite: 0.803\n    pca100d_cr_best_layer: L0\n    nopca_best_layer_range: L9-L16\n    n_traces: 209\n- exp_id: advbench_llm_cp_annotation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: advbench_llm_cp_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen3_cp_dryrun\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen3_cp_dryrun2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen3_cp_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: gpt4omini-cp-annotation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: advbench_phase4_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: random_cp_r1_8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    crossing_rate_random_mean_layer: 10.7\n    crossing_rate_random_shallow_pct: 0\n    precision_random_mean_layer: 0\n    precision_random_shallow_pct: 100\n    metric_disagreement_replicates: false\n    real_cp_cr_composite_layer: 0\n    real_cp_precision_layer: 23\n    real_cp_gap: 23\n    elapsed_s: 105.4\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: ensemble_cv_7b\n  claim: C1 (layer selection bias mitigation)\n  description: 5-fold CV validation of multi-metric ensemble layer selection on 7-8B\n    models (R1-8B + OT-7B). Validates that ensemble eliminates metric-induced bias\n    under cross-validation, upgrading from preliminary to validated diagnostic guidance.\n  estimated_gpu_hours: 0.5\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T21:24:17.771Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:24:17.771Z",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

## Round 1

20 recorded events

### User

_source line 3 · 2026-05-21T21:24:17.793Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer selection sensitivity is recognized as a genuine methodological contribution distinct from hyperparameter tuning. CV-validated ensemble is cosmetic, not load-bearing.
核心假设：["Reviewers treat layer selection metric bias as a reproducible methodological finding (not 'you just picked the wrong hyperparameter')", '4 models × 2 architectures × 2 scales is accepted as sufficient breadth for an empirical study', '32B caveats (R1-32B W=1 only, QwQ negative lead time) are read as honest science, not evidence of fragility', 'Comprehensive negative results (BOCPD/CUSUM/Mahalanobis/RepE/CCS/MLP all fail) are valued as community service', 'Position mediation analysis (3/4 retain non-positional HS advantage) fully resolves confound concern', 'High safe FPR (39-62%) is acceptable as acknowledged limitation for a detection-evaluation paper']
关键指标范围：{'avg_reviewer_score': [3.5, 4.0], 'novelty_rating': [3.5, 4.0], 'soundness_rating': [4.0, 4.5], 'champions_out_of_3': [2, 3], 'ensemble_cv_impact_on_acceptance': [0.0, 0.05], 'lowest_single_reviewer': [3.0, 3.5]}
叙事方向：Original framing fully intact. Primary contribution = layer selection sensitivity as researcher-degree-of-freedom audit. Secondary = HS advantage universal at correct layers. Tertiary = 6 methods fail. Paper title emphasizes 'layer selection matters' angle. Claims need no softening. Ensemble CV can go in appendix as supplementary validation.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: contrastive_trace_safety
venue: emnlp-2026
focus: Evaluate whether adding CV-validated ensemble results (currently p≤0.002 without CV) meaningfully improves paper acceptance probability at EMNLP 2026. Key question: does upgrading ensemble from 'preliminary' to 'CV-validated' move the needle from Findings to Main, or is it marginal? Also assess current paper state post-R30 fixes (commit 322b668) — are there any OTHER low-cost improvements the dream reviewers would prioritize?

## paper_framing.md

# Paper Framing — contrastive_trace_safety

## Target Venue
- Primary: EMNLP 2026 Main (LLM Security Track)
- Deadline: ARR submission May 25, 2026

## Core Claims (D031: layer selection as primary contribution, 4 models)

**Contribution structure (D031)**:
- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions
- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal
- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work

1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).

   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).
   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.
   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.

   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.

   The core insight: "Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak)."

2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 "universal") —

   **KEY FINDING (D029)**: The apparent "scale-dependent" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.

   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.

   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**

   **R1-8B (Llama-8B, R1-distilled, n=43):**
   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)
   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)
   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)

   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**
   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)
   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)
   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)
   - **3/3 metrics significant — OT-7B cleanest single-model evidence**

   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**

   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**
   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)
   - 15/15 W values show significant HS advantage
   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is "more accurate but detects later." Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.
   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**

   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**
   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**
   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)
   - W=5-15: all NS
   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.
   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).
   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. "Scheme B选错层" narrative weaker for R1-32B.
   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.

   **32B cross-model divergence (D031 key finding for Discussion):**
   | Dimension | R1-32B L63 | QwQ L60 |
   |-----------|-----------|---------|
   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |
   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |
   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |
   | Coverage (W=1) | 25% | 74% |
   Paper MUST discuss this divergence per-model, not unify into single narrative.

   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**
   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)
   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)
   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.

   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**
   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).

   | Rank | Model | Metric | p-value | Threshold | Pass |
   |------|-------|--------|---------|-----------|------|
   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |
   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |
   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |
   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |
   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |
   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |
   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |
   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |
   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |
   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |
   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |
   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |

   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure "HS > text at each model's best setting," not "at uniform W." R1-32B W=1 has 25% coverage. Paper must state these conditions.

   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.

   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.

   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.

   Paper recommended claim (D032): "At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text."

3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.

   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.

## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)

The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.

**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:
- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased
- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.
- `precision`: selects deep layers for all models (L60/L63 for 32B)
- `pre_cp_fpr`: selects deep layers for all models
- `composite` (additive): selects deep layers for all models
- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.

**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.

**Corrected layer definition (D036)**: "Corrected layers" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.

**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.

**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are "correct" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a "researcher degree of freedom" with systematic audit via sensitivity analysis.

**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not "correct vs incorrect."

## Story Spine

- **Problem**: Reasoning models exhibit "self-jailbreak" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a "commitment point" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.

- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.

- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).

- **Headline result (D032)**: "Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment."

## Key Evidence Summary

### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)

Best layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.

| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |
|--------|----------|-----------|------------|----------|
| HS Static LR L14 | — | -2.0 | **9.7%** | — |
| HS Temporal W=5 | — | +0.6 | **10.2%** | — |
| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |
| Text Temporal W=15 | — | +10.3* | 20.5% | — |
| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |

*Text lead time inflated by high pre-CP FPR (trigger-happy detection)
NOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).

### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16

Best layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.

| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |
|--------|---------|-----------|----------|-----------|------|
| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |
| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |
| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |

Bootstrap (layer 16, matched W=3, 1000 resamples):
   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅
   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅
   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**
Selectivity: 18.3pp (real=0.688, random=0.505) — highest across all models

### 32B Cross-Architecture — D029 CORRECTED LAYERS

**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**
- HS vs Text bootstrap (null-centered, 1000 resamples):
  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)
  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**
- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive
- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)

**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**
- W=1: bal_acc +18.7pp, p<0.001 ✅
- W≥5: NS (dimensionality: 51200 × W features for n=20)
- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS
- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)

**OLD biased-layer results (RETRACTED as metric artifact):**
| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |
|-------|-------------|----------------|----------------|-------------------|
| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |
| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |

### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)

| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |
|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|
| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |
| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |
| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |
| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |

**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.
Precision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.
Caveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.

### Position Mediation Analysis (D038 → D039 → D042 complete)

**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.

| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |
|-------|---|------------|--------------|-------------|-------|-----|
| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |
| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |
| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |
| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |
| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |

Position-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.

**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).

**Key implications for paper**:
1. Position is a significant component (12-20pp drop) — universal
2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)
3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS
4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)
5. Paper framing: "HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated"

### 5-Seed Robustness (D041)

| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |
|-------|-------------|------------------|----------------|
| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |
| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |
| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |
| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |

R1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.

**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). "7-8B robust / 32B sample-limited" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.

**Per-model evidence tier (D042)**:
- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)
- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive
- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)
- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)

**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).

### BA-Layer Robustness: Metric Circularity Refuted (D044)

R13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).

| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |
|-------|-------------|-------|-----|------|--------|-----------|
| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |
| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |
| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |
| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |

**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.

Key insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.

Caveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.

### Post-hoc Power Analysis (D044)

| Model | n (test) | MDE (80% power, α=0.05) |
|-------|----------|------------------------|
| OT-7B | 47-69 | 6.7-8.1pp |
| R1-8B | 43-63 | 7.4-9.0pp |
| QwQ-32B | 29 | 9.5pp |
| R1-32B | 20-30 | 8.6-11.2pp |

All significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.

### Negative Results (expanded with R3 supplementary experiments)
- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.
- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.
- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:
  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.
  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.
  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642
  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).
- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.
- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as "weakly supervised" not "unsupervised"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.
- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).

## Venue Fit Risks

- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.
- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.
- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).
- **HS advantage universal**: UPGRADED from "scale-dependent" — layer selection is the true moderator, not scale. Cleaner story.
- **Trace vs step FPR**: Both reported with explanation.
- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.
- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.

## Anticipated Reviewer Concerns

1. "Method novelty?" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).
2. "Only one model family?" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.
3. "GRU unstable?" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.
4. "Too few traces?" → Cross-model validation + control task selectivity 7.5-18.5pp.
5. "Fine-grained taxonomy?" → Out of scope for current study.
6. "HS doesn't beat text?" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.
7. "Commitment point circular?" → Cross-model consistency + control task selectivity argues against artifact.
8. "Missing related work?" → Expansion to 30+ citations.
9. "No FPR analysis?" → RESOLVED: both trace-level and step-level FPR reported.
10. "High safe FPR?" → Limitation acknowledged.
11. "Control task / position confound?" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.
12. "Multiple testing correction?" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).
13. "Trace vs step FPR?" → Both reported with explanation.
14. "Layer selection is just hyperparameter tuning?" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.
15. "Why not just use the best layer for each model?" → We do. The point is that the METRIC for selecting "best" matters. Biased metrics produce systematically wrong selections, masking real effects.
16. "32B results are marginal / only W=1 significant for R1-32B?" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.

## Title Candidates (D031)
- "Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring"
- "Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation"
- "What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods"
- "Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable"


## experiment_plan (with registry status)

- id: exp-001
  claim: 1
  description: Cross-architecture hidden-state extraction + layer sweep + static probe
    evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers)
    to find best layer for 64-layer models before probe evaluation. Validates Claim
    1 generalizes beyond r1-8b.
  priority: P0
  gpu_budget_hours: 10
  deps: []
  models:
  - DeepSeek-R1-Distill-Qwen-32B
  - QwQ-32B
  notes: 32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44%
    depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers
    for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE
    reporting static probe results — using wrong layer would produce false negative.
  status: planned
- id: exp-002
  claim: 2
  description: 'Cross-architecture temporal window evaluation: temporal LR W=15 on
    r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.'
  priority: P0
  gpu_budget_hours: 4
  deps:
  - exp-001
  models:
  - DeepSeek-R1-Distill-Qwen-32B
  - QwQ-32B
  status: planned
- id: exp-003
  claim:
  - 1
  - 2
  description: 'Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ
    (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture
    generalization.'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  notes: Key for cross-architecture story. Projection head needed (4096→5120 or vice
    versa).
  status: planned
- id: exp-004
  claim: 3
  description: 'Lead time analysis across models: confirm negative lead time finding
    on 32B models. Report lead time distribution per model.'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - exp-001
  - exp-002
  status: planned
- id: exp-005
  claim:
  - 1
  - 2
  - 3
  description: 'TrajGuard-style Mahalanobis baseline: implement and evaluate on all
    3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).'
  priority: P0
  gpu_budget_hours: 2
  deps:
  - exp-001
  notes: Critical baseline for 'existing detectors fail' claim. Use safe traces to
    estimate covariance, compute MD per step.
  status: planned
- id: exp-006
  claim:
  - 1
  - 2
  description: 'Bootstrap confidence intervals + threshold-independent metrics: 1000
    bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report
    AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold
    variance, and FPR on safe traces (final_judgment=0.5).'
  priority: P0
  gpu_budget_hours: 1
  deps:
  - exp-001
  - exp-002
  - exp-003
  - exp-004
  - exp-005
  status: planned
- id: exp-007
  claim: 2
  description: 'Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal
    W and show diminishing returns curve.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  status: planned
- id: exp-008
  claim: 2
  description: 'Layer selection ablation: all layers (not just 14) for temporal probe
    on 32B models. Confirm middle-layer finding generalizes.'
  priority: P1
  gpu_budget_hours: 3
  deps:
  - exp-001
  status: planned
- id: exp-009
  claim: 2
  description: '16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4)
    instead of binary commitment for richer training signal. May improve both coverage
    and timing.'
  priority: P1
  gpu_budget_hours: 2
  deps:
  - exp-001
  notes: Addresses reviewer concern about underusing available supervision.
  status: planned
- id: exp-010
  claim: 3
  description: 'Oracle decomposition: why can oracle but not probes achieve positive
    lead time? Analyze what label patterns encode that hidden states don''t.'
  priority: P1
  gpu_budget_hours: 1
  deps:
  - exp-004
  notes: For Discussion section. May reveal what architectural changes could close
    the gap.
  status: planned
- id: exp-011
  claim: 2
  description: 'OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale
    matrix. Controls for scale confound.'
  priority: P2
  gpu_budget_hours: 4
  deps:
  - exp-002
  notes: From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for
    scale-matched comparison.
  status: planned
- id: exp-012
  claim:
  - 1
  - 2
  description: 'GRU/Attention probe as upper bound: verify GRU finding holds on 32B
    models with more data. If still no improvement over LR, strengthens ''simplicity
    is optimal'' story.'
  priority: P2
  gpu_budget_hours: 4
  deps:
  - exp-001
  - exp-002
  status: planned
- id: exp-013
  claim:
  - 1
  - 2
  description: 'Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) +
    same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state
    probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap
    text monitoring. If text achieves comparable performance, paper motivation needs
    restructuring.'
  priority: P0
  gpu_budget_hours: 0.5
  deps: []
  notes: No GPU needed for embedding extraction (small model, CPU-feasible). Run on
    all 4 models. This is the single most important missing baseline per Dream review
    (flagged by all 3 tiers, both reviewers).
  status: planned
- id: exp-014
  claim: 3
  description: 'Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores:
    apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve
    positive lead time by detecting distributional shift before textual commitment.
    Also test CUSUM as simpler alternative.'
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - exp-001
  notes: Addresses both 'no method novelty' and 'no positive lead time' criticisms
    simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes
    a genuine methods contribution. If it also fails, strengthens the 'fundamental
    limitation' narrative.
  status: planned
- id: exp-015
  claim:
  - 1
  - 2
  description: 'False positive analysis: run all probes (static, temporal, GRU, BOCPD)
    on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various
    thresholds. Essential for deployment utility claims.'
  priority: P0
  gpu_budget_hours: 0.5
  deps:
  - exp-001
  - exp-002
  notes: Dream flagged missing FPR as critical gap across median and worst tiers.
    Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere
    gets 100% coverage.
  status: planned


## registry (completed experiments)

- exp_id: diag_d1_layer_sweep
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    best_layer_idx: 2
    best_model_layer: 14
    best_acc: 0.8114
    best_f1: 0.6455
    best_crossing_rate: 0.186
    best_lead_mean: 8.38
    best_lead_median: 6
    default_layer20_acc: 0.7831
    num_traces: 209
    split: 125/41/43
- exp_id: diag_d4_oracle_upper_bound
  name: ''
  status: DONE
  conclusion: success
  metrics:
    K5_detection_rate: 100
    K5_early_detection_rate: 76.7
    K5_mean_lead_time: 31
    K5_median_lead_time: 29
    K1_early_detection_rate: 83.7
    K8_early_detection_rate: 65.1
    pre_cp_mean_longest_streak: 14.6
    test_traces: 43
- exp_id: diag_d2_pca_viz
  name: ''
  status: DONE
  conclusion: success
  metrics:
    fisher_orig_L12: 17.462
    fisher_orig_L14: 17.875
    fisher_orig_L20: 18.614
    fisher_orig_L24: 18.106
    fisher_pca_L12: 0.953
    fisher_pca_L14: 0.928
    fisher_pca_L20: 0.92
    fisher_pca_L24: 1.111
    var_explained_3pc: 0.166
    test_steps: 1835
- exp_id: diag_d3_regularized_probes
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    static_lr_acc: 0.8172
    static_lr_crossing_rate: 0.4651
    static_lr_lead_mean: -2
    temporal_lr_w5_acc: 0.8274
    temporal_lr_w5_crossing_rate: 0.6512
    temporal_lr_w5_lead_mean: -1.18
    temporal_lr_w10_acc: 0.8364
    temporal_lr_w10_crossing_rate: 0.6512
    temporal_lr_w10_lead_mean: -0.61
    temporal_lr_w15_acc: 0.8478
    temporal_lr_w15_crossing_rate: 0.7674
    temporal_lr_w15_lead_mean: -1.09
    best_temporal_delta_over_static: 1.39
    pass_criterion_met: false
- exp_id: diag_gru_probe
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    test_acc: 0.8305
    test_acc_std: 0.1856
    crossing_rate: 0.6744
    lead_mean: -0.207
    lead_median: -1
    lead_std: 13
    positive_lead_rate: 0.345
    n_positive_lead: 10
    n_detected: 29
    early_stop_epoch: 14
    model_params: 1622913
- exp_id: exp_gru256_multilayer
  name: ''
  status: DONE
  conclusion: success
  metrics:
    gru_single_l14:
      acc: 0.8386
      crossing_rate: 0.721
      lead_mean: 3.5
      lead_median: 0
      pos_lead: 13/31
    gru_multi_7l:
      acc: 0.8094
      crossing_rate: 0.767
      lead_mean: 4.7
      lead_median: 0
      pos_lead: 13/33
    lr_single_l14:
      acc: 0.8172
      crossing_rate: 0.465
      lead_mean: -2
      lead_median: -2
      pos_lead: 6/20
    lr_multi_7l:
      acc: 0.806
      crossing_rate: 0.395
      lead_mean: 1.1
      lead_median: 0
      pos_lead: 6/17
    delta_gru_vs_lr: 3.7
- exp_id: exp_005_trajguard_mahalanobis
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    best_k5_crossing_rate: 0.302
    best_k5_lead_mean: 16.4
    best_k5_config: pca_64_p75
    best_k3_crossing_rate: 0.605
    best_k3_lead_mean: 20.4
    delta_max_rate: 0.023
    safe_md_mean: 6.66
    jb_pre_md_mean: 6.73
    jb_post_md_mean: 6.64
- exp_id: exp_006_bootstrap_ci
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    static_lr_acc: 0.768 [0.702,0.827]
    static_lr_crossing: 60.4% [44.2,74.4]
    static_lr_lead: +2.9 [-2.8,+9.5]
    temporal_lr_acc: 0.731 [0.654,0.804]
    temporal_lr_crossing: 60.6% [46.5,74.4]
    temporal_lr_lead: +5.0 [-0.8,+11.9]
    gru_single_acc: 0.790 [0.734,0.848]
    gru_single_crossing: 51.4% [37.2,67.4]
    gru_single_lead: -2.0 [-8.6,+4.9]
    gru_multi_acc: 0.799 [0.742,0.854]
    gru_multi_crossing: 51.4% [37.2,67.4]
    gru_multi_lead: -0.4 [-6.4,+6.1]
    paired_temporal_vs_static_lead_p: 0.19
    paired_gru_vs_static_lead_p: 0.94
    paired_gru_vs_temporal_lead_p: 0.99
- exp_id: exp_013_text_baseline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    text_static_coverage: 0.605
    text_static_lead: 4.3
    text_static_acc: 0.661
    text_static_auroc: 0.7384
    text_temporal_w15_coverage: 0.651
    text_temporal_w15_lead: 11.5
    text_temporal_w15_acc: 0.678
    text_temporal_w15_auroc: 0.759
    hs_acc_advantage: 15-18pp
- exp_id: exp_015_fpr_analysis
  name: ''
  status: DONE
  conclusion: success
  metrics:
    text_static_safe_fpr: 0.502
    text_static_precp_fpr: 0.356
    text_static_precision: 0.448
    text_static_coverage: 0.605
    text_static_lead: 4.3
    text_static_acc: 0.661
    text_temporal_safe_fpr: 0.385
    text_temporal_precp_fpr: 0.272
    text_temporal_precision: 0.487
    text_temporal_coverage: 0.651
    text_temporal_lead: 11.5
    text_temporal_acc: 0.678
    hs_static_safe_fpr: 0.39
    hs_static_precp_fpr: 0.162
    hs_static_precision: 0.622
    hs_static_coverage: 0.605
    hs_static_lead: 3
    hs_static_acc: 0.768
    hs_temporal_safe_fpr: 0.392
    hs_temporal_precp_fpr: 0.16
    hs_temporal_precision: 0.583
    hs_temporal_coverage: 0.651
    hs_temporal_lead: 4.9
    hs_temporal_acc: 0.726
    gru_safe_fpr: 0.521
    gru_precp_fpr: 0.188
    gru_precision: 0.648
    gru_coverage: 0.744
    gru_lead: 5.25
    gru_acc: 0.816
- exp_id: exp_014_bocpd_poc
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    bocpd_lambda10:
      detection_rate: 0.93
      mean_lead: 3.45
      median_lead: 0
      early_count: 16
      late_count: 19
    bocpd_lambda100:
      detection_rate: 0.674
      mean_lead: 1.03
      median_lead: 0
    cusum_best_t03h3:
      detection_rate: 0.651
      mean_lead: 0.89
      median_lead: -4
    fcp_baseline:
      detection_rate: 0.651
      mean_lead: 4.89
      median_lead: 0
    head_to_head_bocpd_vs_fcp:
      bocpd_wins: 16
      fcp_wins: 6
      ties: 5
    verdict: BOCPD higher detection (93% vs 65%) but lower mean lead (3.45 vs 4.89).
      CUSUM universally worse. Neither method achieves earlier detection than simple
      threshold crossing on average.
- exp_id: exp_001a_r1_32b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    m001_corrected: true
    best_layer_old: 2
    best_layer_corrected: 10
    layer_selection_metric: balanced_accuracy × crossing_rate (scheme B)
    layer10_bal_acc: 0.718
    layer10_crossing_rate: 0.6
    gru_single_bal_acc_mean: 0.675
    gru_single_crossing_mean: 0.3
    gru_single_lead_mean: 9.1
    gru_single_precp_fpr_mean: 0.135
    gru_multi_bal_acc_mean: 0.655
    gru_multi_crossing_mean: 0.23
    gru_multi_lead_mean: 8.8
    gru_multi_precp_fpr_mean: 0.114
    temporal_lr_best_window: 10
    temporal_lr_w10_bal_acc: 0.737
    temporal_lr_w10_crossing: 0.5
    temporal_lr_w10_lead: 9
    temporal_lr_w10_precp_fpr: 0.189
    bootstrap_hs_precp_fpr: 0.26
    bootstrap_text_precp_fpr: 0.246
    bootstrap_diff: 0.014
    bootstrap_p_value: 0.999
    bootstrap_ci95:
    - -0.103
    - 0.127
    bootstrap_conclusion: no_significant_difference
    paired_bootstrap_corrected:
      hs_bal_acc: 0.794
      text_bal_acc: 0.711
      acc_delta: 0.084
      acc_p_value_two_sided: 0.08
      hs_precision: 0.61
      text_precision: 0.516
      prec_delta: 0.094
      prec_p_value_two_sided: 0.05
      hs_precp_fpr: 0.242
      text_precp_fpr: 0.326
      fpr_delta: -0.084
      fpr_p_value_two_sided: 0.114
      bonferroni_alpha: 0.017
      bonferroni_pass: false
      test_type: two-sided
      solver: liblinear
      canonical_file: artifacts/r1_32b_paired_bootstrap/results.json
      note: directional but ns after Bonferroni. n=20 test traces insufficient power.
        Old m001 FPR=0.246 used lbfgs solver (non-canonical).
- exp_id: exp_001b_qwq_32b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    m001_corrected: true
    best_layer_old: 1
    best_layer_corrected: 2
    layer_selection_metric: balanced_accuracy × crossing_rate (scheme B)
    layer2_bal_acc: 0.73
    layer2_crossing_rate: 0.47
    gru_single_bal_acc_mean: 0.694
    gru_single_crossing_mean: 0.75
    gru_single_lead_mean: 19.3
    gru_single_precp_fpr_mean: 0.303
    gru_multi_bal_acc_mean: 0.724
    gru_multi_crossing_mean: 0.84
    gru_multi_lead_mean: 15.9
    gru_multi_precp_fpr_mean: 0.289
    temporal_lr_best_window: 5
    temporal_lr_w5_bal_acc: 0.761
    temporal_lr_w5_crossing: 0.42
    temporal_lr_w5_lead: 23.5
    temporal_lr_w5_precp_fpr: 0.18
    bootstrap_phase5_invalid: true
    bootstrap_phase5_bug: M002 - text_baseline_predictions() in exp_001b_bootstrap.py
      used midpoint heuristic, not sentence embeddings
    corrected_hs_vs_text:
      hs_bal_acc: 0.679
      text_bal_acc: 0.671
      acc_delta: 0.009
      acc_p_value_two_sided: 0.828
      hs_precision: 0.583
      text_precision: 0.525
      prec_delta: 0.057
      prec_p_value_two_sided: 0.346
      hs_precp_fpr: 0.208
      text_precp_fpr: 0.178
      fpr_delta: 0.03
      fpr_p_value_two_sided: 0.43
      bonferroni_alpha: 0.017
      bonferroni_pass: false
      test_type: two-sided
      solver: liblinear
      note: No significant HS vs text difference on QwQ-32B. HS FPR slightly worse
        than text.
    bootstrap_conclusion: no_significant_difference
- exp_id: exp_003_cross_transfer
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    baselines:
      r1_8b_acc: 0.8234
      r1_32b_acc: 0.6516
      qwq_32b_acc: 0.7171
    best_transfer_acc:
      r1_8b_to_r1_32b: 0.522
      r1_8b_to_qwq: 0.5948
      r1_32b_to_qwq: 0.5499
      qwq_to_r1_32b: 0.6726
      r1_32b_to_r1_8b: 0.5828
    transfer_method: PCA projection
    conclusion_detail: Simple PCA projection insufficient for zero-shot cross-model
      transfer. Signal is model-specific in geometric encoding.
- exp_id: exp_c2_control_task
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b_selectivity: 0.1245
    r1_32b_selectivity: 0.075
    r1_32b_selectivity_note: layer 10 (corrected best layer). Old layer 2 = 0.168
    r1_32b_layer10_real_acc: 0.583
    r1_32b_layer10_random_mean: 0.508
    r1_32b_layer10_random_std: 0.051
    qwq_32b_selectivity: 0.153
    qwq_32b_selectivity_note: layer 2 (corrected from layer 1 = 0.189)
    r1_8b_hs_pre_fpr: 0.0809
    r1_8b_position_pre_fpr: 0.1581
    r1_8b_cp_position_mean: 0.705
    qwq_32b_layer2_real_acc: 0.678
    qwq_32b_layer2_random_mean: 0.526
    qwq_32b_layer2_random_std: 0.076
    qwq_32b_layer2_position_acc: 0.706
    qwq_32b_layer2_hs_pre_fpr: 0.2903
    qwq_32b_layer2_position_pre_fpr: 0.25
    qwq_32b_layer2_issue: position_baseline (70.6%) > HS probe (67.8%)
- exp_id: exp_007_window_ablation
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    r1_8b:
      W1:
        bal_acc: 0.7783
        precision: 0.6926
        coverage: 0.7209
        precp_fpr_trace: 0.1037
        precp_fpr_step: 0.0965
        lead_mean: 13.84
      W3:
        bal_acc: 0.7902
        precision: 0.7228
        coverage: 0.6977
        precp_fpr_trace: 0.0988
        precp_fpr_step: 0.085
        lead_mean: 12.07
      W5:
        bal_acc: 0.781
        precision: 0.7258
        coverage: 0.6512
        precp_fpr_trace: 0.0913
        precp_fpr_step: 0.0809
        lead_mean: 8.25
      W10:
        bal_acc: 0.7925
        precision: 0.7431
        coverage: 0.5581
        precp_fpr_trace: 0.0865
        precp_fpr_step: 0.0761
        lead_mean: 10.04
      W15:
        bal_acc: 0.8017
        precision: 0.7767
        coverage: 0.5116
        precp_fpr_trace: 0.0701
        precp_fpr_step: 0.0639
        lead_mean: 7.23
      W20:
        bal_acc: 0.8072
        precision: 0.7862
        coverage: 0.5349
        precp_fpr_trace: 0.0661
        precp_fpr_step: 0.0612
        lead_mean: 7.43
      W25:
        bal_acc: 0.8095
        precision: 0.8216
        coverage: 0.4884
        precp_fpr_trace: 0.0545
        precp_fpr_step: 0.0483
        lead_mean: 8.14
      best_bal_acc_W: 25
    r1_32b:
      W1:
        bal_acc: 0.7182
        precision: 0.549
        coverage: 0.8
        precp_fpr_trace: 0.2764
        precp_fpr_step: 0.3203
        lead_mean: 12.88
      W3:
        bal_acc: 0.7252
        precision: 0.56
        coverage: 0.8
        precp_fpr_trace: 0.2576
        precp_fpr_step: 0.3064
        lead_mean: 11.38
      W5:
        bal_acc: 0.7309
        precision: 0.575
        coverage: 0.75
        precp_fpr_trace: 0.2393
        precp_fpr_step: 0.2841
        lead_mean: 11.07
      W10:
        bal_acc: 0.7371
        precision: 0.6093
        coverage: 0.7
        precp_fpr_trace: 0.1891
        precp_fpr_step: 0.234
        lead_mean: 10.79
      W15:
        bal_acc: 0.7207
        precision: 0.5907
        coverage: 0.7
        precp_fpr_trace: 0.2089
        precp_fpr_step: 0.2451
        lead_mean: 10.86
      W20:
        bal_acc: 0.6961
        precision: 0.5628
        coverage: 0.65
        precp_fpr_trace: 0.2193
        precp_fpr_step: 0.2618
        lead_mean: 9.62
      W25:
        bal_acc: 0.7028
        precision: 0.5662
        coverage: 0.7
        precp_fpr_trace: 0.2282
        precp_fpr_step: 0.2646
        lead_mean: 10.71
      best_bal_acc_W: 10
    qwq_32b:
      W1:
        bal_acc: 0.7298
        precision: 0.5435
        coverage: 0.7895
        precp_fpr_trace: 0.185
        precp_fpr_step: 0.2276
        lead_mean: 19.73
      W3:
        bal_acc: 0.7452
        precision: 0.5647
        coverage: 0.7368
        precp_fpr_trace: 0.175
        precp_fpr_step: 0.2141
        lead_mean: 20.64
      W5:
        bal_acc: 0.761
        precision: 0.5733
        coverage: 0.7368
        precp_fpr_trace: 0.1795
        precp_fpr_step: 0.2168
        lead_mean: 20.07
      W10:
        bal_acc: 0.7469
        precision: 0.5714
        coverage: 0.7368
        precp_fpr_trace: 0.1707
        precp_fpr_step: 0.2073
        lead_mean: 18.43
      W15:
        bal_acc: 0.7412
        precision: 0.5816
        coverage: 0.6842
        precp_fpr_trace: 0.1605
        precp_fpr_step: 0.1911
        lead_mean: 15.77
      W20:
        bal_acc: 0.7542
        precision: 0.6024
        coverage: 0.6316
        precp_fpr_trace: 0.1567
        precp_fpr_step: 0.1789
        lead_mean: 15.75
      W25:
        bal_acc: 0.7624
        precision: 0.6177
        coverage: 0.5789
        precp_fpr_trace: 0.1476
        precp_fpr_step: 0.1694
        lead_mean: 14.91
      best_bal_acc_W: 25
    finding: Coverage monotonically DECREASES with W across all 3 models. Temporal
      context creates precision-sensitivity tradeoff (higher W → higher precision,
      lower coverage, lower FPR). R1-8B dominates (lowest FPR, highest precision).
      QwQ-32B FPR significantly lower than R1-32B with larger lead_mean.
- exp_id: exp_ot7b_full_pipeline
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_traces: 228
    best_layer: 16
    best_layer_depth_pct: 57.1
    best_layer_score: 0.6876
    best_hs_window: 3
    best_hs_bal_acc: 0.688
    best_hs_precision: 0.466
    best_hs_pre_cp_fpr: 0.1
    best_hs_coverage: 0.5319
    best_hs_lead: 21.6
    best_text_window: 25
    best_text_bal_acc: 0.6141
    best_text_precision: 0.3291
    best_text_pre_cp_fpr: 0.1605
    bootstrap_bal_acc_delta: 0.1067
    bootstrap_bal_acc_ci95: '[0.049, 0.163]'
    bootstrap_bal_acc_p: 0.001
    bootstrap_bal_acc_bonf: true
    bootstrap_precision_delta: 0.2189
    bootstrap_precision_ci95: '[0.140, 0.296]'
    bootstrap_precision_p: 0.001
    bootstrap_precision_bonf: true
    bootstrap_fpr_delta: -0.1705
    bootstrap_fpr_ci95: '[-0.222, -0.122]'
    bootstrap_fpr_p: 0.001
    bootstrap_fpr_bonf: true
    holm_bonferroni: 3/3
    selectivity_pp: 18.3
    selectivity_real_acc: 0.688
    selectivity_random_mean: 0.505
    layer0_bal_acc: 0.672
    layer0_precision: 0.357
    layer0_pre_cp_fpr: 0.188
    layer16_vs_layer0: '+9.0pp bal_acc, +20.8pp precision, -8.7pp FPR. Precision Bonf:
      L0 p=0.056 FAIL -> L16 p<0.001 PASS'
    layer_verification: 'Layer 16 verified superior to Layer 0: 3/3 Bonferroni (was
      2/3 on L0)'
    r1_8b_layer_supplement: 'Full sweep layers 0-24 confirmed: best=L12 (0.7871) ~
      L14 (0.7830), no early-layer dominance.'
    gru_single_l16_bal_acc: 0.7246
    gru_single_l16_coverage: 0.667
    gru_single_l16_lead: 35.25
    gru_single_l16_precp_fpr: 0.2904
    gru_multi_l13_19_bal_acc: 0.7464
    gru_multi_l13_19_coverage: 0.645
    gru_multi_l13_19_lead: 33.61
    gru_multi_l13_19_precp_fpr: 0.2741
- exp_id: exp_pathb_annotation_validation
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    tfidf_lr_f1: 0.5899
    tfidf_lr_cp_agreement: 0.561
    minilm_lr_f1: 0.5149
    minilm_lr_cp_agreement: 0.534
    threshold_f1: 0.9
    threshold_cp: 0.85
    failure_reason: Safety recall extremely low (41-46%). Simple classifiers cannot
      distinguish subtle safety-aware expressions in CoT from regular reasoning. CP
      MAE=5-6 sentences.
    recommendation: Need LLM API annotation or fine-tuned DeBERTa 16-class classifier
- exp_id: exp_r3_repe_direction
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b:
      layer: 2
      bal_acc: 0.7491
      precision: 0.516
      pre_cp_fpr: 0.2264
      coverage: 0.3953
      lead_mean: 9.7
    r1_32b_corrected:
      layer: 63
      bal_acc: 0.5588
      precision: 0.3891
      pre_cp_fpr: 0.4986
      coverage: 0.6
      lead_mean: 12
    r1_32b_old:
      layer: 10
      bal_acc: 0.6707
      precision: 0.5538
      pre_cp_fpr: 0.2423
      coverage: 0.45
      lead_mean: 6.3
    qwq_32b_corrected:
      layer: 60
      bal_acc: 0.7562
      precision: 0.5118
      pre_cp_fpr: 0.3089
      coverage: 0.7368
      lead_mean: 11.9
    qwq_32b_old:
      layer: 2
      bal_acc: 0.6661
      precision: 0.4193
      pre_cp_fpr: 0.3997
      coverage: 0.7368
      lead_mean: 13.4
    ot_7b:
      layer: 16
      bal_acc: 0.718
      precision: 0.3733
      pre_cp_fpr: 0.2573
      coverage: 0.5319
      lead_mean: 26.1
    vs_lr_r1_8b:
      lr_bal_acc: 0.817
      lr_precision: 0.693
      lr_fpr: 0.097
      repe_weaker_acc: true
      repe_weaker_precision: true
    finding: 'Corrected layers: R1-32B L63 RepE degrades severely (bal_acc 0.67→0.56,
      FPR 0.24→0.50); QwQ L60 improves (bal_acc 0.67→0.76). Both still below supervised
      LR. Unsupervised RepE direction insufficient at any layer.'
- exp_id: exp_r3_bocpd_ot7b_w15
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    W: 15
    fcp_null_rate: 0.53
    note: W=15 mismatched with OT-7B best window W=3, causing 53% traces with null
      FCP. Results unreliable due to parameter mismatch.
    parent_best_W: 3
- exp_id: exp_r3_mlp_probe
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    source: v1_per_model_json (K=5)
    warning: 'over-parameterization: v2 had K=1 detection bug (coverage=1.0). v1 data
      used here.'
    caveat: OT-7B uses centered window; other models use causal window
    r1_8b:
      W1:
        bal_acc: 0.806
        precision: 0.646
        fpr: 0.137
        coverage: 0.767
        lead: 14.27
      W3:
        bal_acc: 0.81
        precision: 0.706
        fpr: 0.1
        coverage: 0.721
        lead: 9.71
      W5:
        bal_acc: 0.843
        precision: 0.595
        fpr: 0.201
        coverage: 0.884
        lead: 12.89
      W10:
        bal_acc: 0.846
        precision: 0.592
        fpr: 0.206
        coverage: 0.884
        lead: 13.29
      lr_W3: 0.79
      lr_W5: 0.781
      lr_W10: 0.793
    r1_32b:
      W3:
        bal_acc: 0.713
        precision: 0.585
        fpr: 0.245
        coverage: 0.8
        lead: 9.12
      W10:
        bal_acc: 0.688
        precision: 0.524
        fpr: 0.332
        coverage: 0.75
        lead: 10.33
      lr_W3: 0.725
      lr_W10: 0.737
    qwq_32b:
      W5:
        bal_acc: 0.604
        precision: 0.339
        fpr: 0.692
        coverage: 0.842
        lead: 33.19
      W10:
        bal_acc: 0.698
        precision: 0.432
        fpr: 0.428
        coverage: 0.842
        lead: 22.94
      lr_W5: 0.761
      lr_W10: 0.747
    ot_7b:
      W1:
        bal_acc: 0.73
        precision: 0.456
        fpr: 0.165
        coverage: 0.766
        lead: 32.19
      W3:
        bal_acc: 0.747
        precision: 0.343
        fpr: 0.362
        coverage: 0.872
        lead: 41.22
      lr_W3: 0.688
    finding: 'MLP inconsistent vs LR: r1_8b +5pp at W5/10, ot_7b +6pp at W3, but r1_32b
      -2 to -5pp, qwq_32b -5 to -16pp. Small datasets (r1_32b=100, qwq=95) likely
      cause MLP overfitting. Signal linearly separable for most models.'
- exp_id: exp_r3_bocpd_ot7b_w3
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    W: 3
    layer: 16
    n_test: 47
    bocpd_all_lambda:
      detection_rate: 0
      note: W=3 probe scores too spiky (0→1 in 1-2 steps), Gaussian model fails
    fcp_t05_k2:
      detection_rate: 0.894
      mean_lead: 11.83
      median_lead: 10.5
    fcp_t05_k3:
      detection_rate: 0.745
      mean_lead: 8.71
      median_lead: 7
    fcp_t03_k3:
      detection_rate: 0.787
      mean_lead: 11.92
      median_lead: 10
    fcp_t05_k5:
      detection_rate: 0.468
      mean_lead: 5.09
      median_lead: 4.5
    cusum_t02_h2:
      detection_rate: 0.745
      mean_lead: 7.46
      median_lead: 6
    cusum_t03_h2:
      detection_rate: 0.702
      mean_lead: 6.03
      median_lead: 5
    vs_r1_8b:
      r1_bocpd_l10_det: 0.93
      ot7b_bocpd_det: 0
      r1_fcp_det: 0.651
      ot7b_fcp_k2_det: 0.894
      r1_fcp_lead: 4.89
      ot7b_fcp_k2_lead: 11.83
    finding: 'BOCPD 0% on OT-7B (all lambdas) vs 93% on R1-8B. Commitment dynamics
      model-specific: R1-8B gradual (BOCPD works), OT-7B abrupt (simple threshold
      optimal). Negative result confirmed cross-model for R3-W2.'
- exp_id: exp_r3_mahalanobis_ot7b
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    layer: 16
    pca_dims_tested:
    - 16
    - 32
    - 64
    - 128
    - 256
    md_separation:
      pca16: -0.048
      pca32: 0.012
      pca64: 0.031
      pca128: 0.004
      pca256: -0.093
    safe_md_mean_pca64: 7.68
    post_md_mean_pca64: 7.71
    pca64_k3_false_alarm_vs_tp:
      p50:
        fa_rate: 0.872
        tp_rate: 0.385
      p75:
        fa_rate: 0.574
        tp_rate: 0.231
      p90:
        fa_rate: 0.17
        tp_rate: 0.154
      p95:
        fa_rate: 0.043
        tp_rate: 0
    vs_r1_8b:
      r1_safe_md: 6.66
      r1_post_md: 6.73
      r1_separation: 0.07
      ot7b_safe_md: 7.68
      ot7b_post_md: 7.71
      ot7b_separation: 0.03
      failure_mode: 'identical: signal in minor PCA components, not principal directions'
    finding: 'Mahalanobis zero discriminative power on OT-7B (separation ≈ 0 across
      all PCA dims). False alarm rate >= true positive rate at every threshold. Failure
      mode identical to R1-8B. R3-W2 fully addressed: 3/3 methods (BOCPD/CUSUM/Mahalanobis)
      fail consistently across both models.'
- exp_id: exp_r3_ccs_probe
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    r1_8b:
      bal_acc: 0.777
      precision: 0.565
      fpr: 0.191
      coverage: 0.674
      lead: 0.7
    qwq_32b:
      bal_acc: 0.731
      precision: 0.555
      fpr: 0.214
      coverage: 0.684
      lead: 2
    r1_32b:
      bal_acc: 0.703
      precision: 0.507
      fpr: 0.41
      coverage: 0.9
      lead: 5.2
    ot_7b:
      bal_acc: 0.692
      precision: 0.319
      fpr: 0.344
      coverage: 0.809
      lead: 20.5
    vs_supervised_lr_r1_8b:
      lr_bal_acc: 0.817
      lr_precision: 0.693
      lr_fpr: 0.097
      ccs_weaker: true
    vs_repe_r1_8b:
      repe_bal_acc: 0.749
      ccs_better: true
    finding: CCS is best unsupervised method (beats RepE) but still significantly
      below supervised LR. All models needed polarity flip. FPR 0.19-0.41 across all
      models confirms unsupervised gap.
- exp_id: exp_r3_r1_32b_l63_bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    method: null-centered two-sided bootstrap
    W1:
      bal_acc_delta: 0.187
      bal_acc_p: 0
      precision_delta: 0.154
      precision_p: 0
      fpr_delta: -0.146
      fpr_p: 0.007
      bonferroni_pass: 3/3
    W3:
      bal_acc_delta: 0.112
      bal_acc_p: 0.02
      precision_delta: 0.13
      precision_p: 0.032
      fpr_delta: -0.114
      fpr_p: 0.077
      bonferroni_pass: 0/3
    W5:
      bal_acc_delta: 0.097
      bal_acc_p: 0.046
      bonferroni_pass: 0/3
    W10:
      bal_acc_p: 0.384
      bonferroni_pass: 0/3
    W15:
      bal_acc_p: 0.075
      bonferroni_pass: 0/3
    finding: W=1 significant 3/3 Bonferroni (alpha=0.0167). W3+ all fail after Bonferroni.
      Confirms HS advantage exists at L63 but only robust at minimal temporal context.
- exp_id: exp_r3_qwq_l60_bootstrap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    method: null-centered two-sided bootstrap (bugfixed)
    bug_fixed: missing np.mean(bd) centering caused p~0.5
    W1:
      bal_acc_ci: '[0.15,0.29]'
      bal_acc_p: 0
      precision_ci: '[0.21,0.39]'
      precision_p: 0
      fpr_ci: '[-0.23,-0.12]'
      fpr_p: 0
    W3:
      bal_acc_p: 0
      precision_p: 0
      fpr_p: 0.004
      precision_delta: 0.236
      fpr_delta: -0.098
    W5:
      bal_acc_p: 0
      precision_p: 0
      fpr_p: 0.011
    W10:
      bal_acc_p: 0
      precision_p: 0.016
      fpr_p: 0.009
    W15:
      bal_acc_p: 0.004
      precision_p: 0.003
      fpr_p: 0.007
    bonferroni_summary: 15/15 pass (alpha=0.0167)
    finding: All 15 tests significant after bugfix. QwQ L60 shows robust HS advantage
      across all windows, consistent with OT-7B. scale-dependent claim falsified.
- exp_id: exp_r3_layer_ablation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    models_tested: 4
    metrics_tested: 5
    bias_discovered: bal_acc x crossing_rate systematically selects shallow layers
    qwq_32b:
      biased_layer: 2
      corrected_layer: 60
      bal_acc_gain: +1.75pp
      precision_gain: +11.5pp
      fpr_reduction: -8.3pp
    r1_32b:
      biased_layer: 10
      corrected_layer: 63
      bal_acc_gain: +3.7pp
      precision_gain: +4.1pp
      fpr_reduction: -4.3pp
    r1_8b:
      biased_layer: 0
      best_layer: 12
      consistency: L12-L16 cluster, current L14 near-optimal
    ot_7b:
      biased_layer: 0
      best_layer: 9
      current_layer: 16
      note: 4 metrics select 4 different layers
    cross_metric_consistency:
      r1_8b: CONSISTENT
      r1_32b: VARIED (all point deep)
      qwq_32b: VARIED (all point deep)
      ot_7b: VARIED
    finding: crossing_rate biases layer selection to shallow layers. Pure bal_acc/precision
      select mid-to-deep layers (40-95% depth). R1-32B and QwQ affected most severely.
- exp_id: exp_r3_mahalanobis_r1_32b_qwq
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    r1_32b:
      layer: 63
      safe_md: 6.73
      post_md: 6.88
      separation: 0.15
      best_pca: 64
    qwq_32b:
      layer: 60
      safe_md: 3.22
      post_md: 3.42
      separation: 0.2
      best_pca: 16
    cross_model_summary:
      r1_8b_sep: 0.07
      ot_7b_sep: 0.03
      r1_32b_sep: 0.15
      qwq_32b_sep: 0.2
      max_separation: 0.2
      all_fail: true
    finding: 4/4 models Mahalanobis fails. Max separation 0.20 (QwQ), false alarm
      rate >= true positive at every threshold. Signal in minor PCA components, not
      principal directions.
- exp_id: exp_r3_bocpd_r1_32b_qwq
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    r1_32b:
      layer: 10
      W: 10
      bocpd_det: 0
      cusum_det: 0.85
      cusum_lead: 2.59
      fcp_det: 0.95
      fcp_lead: 5.68
    qwq_32b:
      layer: 2
      W: 5
      bocpd_det: 0
      cusum_det: 0.737
      cusum_lead: 9.86
      fcp_det: 0.789
      fcp_lead: 9.4
    cross_model_bocpd:
      r1_8b: 0.93
      r1_32b: 0
      ot_7b: 0
      qwq_32b: 0
      only_r1_8b_works: true
    finding: BOCPD 0% on 3/4 models (only R1-8B exception at 93%). CUSUM universally
      inferior to simple FCP threshold. Advanced change-point methods fail for safety
      commitment detection.
- exp_id: exp_r3_coverage_bias
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b:
      total: 268
      included: 209
      excluded: 59
      exclusion_rate: 0.22
    r1_32b:
      total: 100
      excluded: 0
      exclusion_rate: 0
    qwq_32b:
      total: 95
      excluded: 0
      exclusion_rate: 0
    exclusion_reason: All 59 excluded traces are jailbreak with no safety reasoning
      phase (no commitment point annotatable)
    length_test:
      excluded_mean: 38
      included_mean: 46.3
      mann_whitney_p: 0.0001
      excluded_shorter: true
    finding: 22% exclusion in R1-8B is task-definitional (no CP to annotate), not
      sampling bias. R1-32B/QwQ 0% exclusion. Coverage metric valid within annotatable
      population.
- exp_id: exp_r3_selectivity_ci_raw
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    feature_type: raw 5120-d (no PCA)
    real_acc: 0.584
    random_mean: 0.508
    selectivity_pp: 7.6
    bootstrap_mean_pp: 8.4
    bootstrap_std_pp: 6.7
    ci_95: '[-3.9, 22.7]pp'
    p_value: 0.107
    significant: false
    vs_pca128:
      pca128_selectivity: 15.9
      pca128_p: 0
      pca128_ci: '[9.7, 21.9]pp'
    finding: Raw 5120-d selectivity 7.6pp not significant (p=0.107, CI includes 0).
      Under-determined n&lt;p without PCA. PCA-128 gives 15.9pp (p<0.001) — dimensionality
      reduction needed for reliable selectivity.
- exp_id: exp_r3_gru_per_seed
  name: ''
  status: DONE
  conclusion: success
  metrics:
    seeds:
    - 42
    - 123
    - 456
    - 789
    - 1024
    split: 70/30
    bal_acc:
      mean: 0.772
      std: 0.038
      min: 0.729
      max: 0.833
    crossing_rate:
      mean: 0.711
      std: 0.121
    lead_mean:
      mean: 8.2
      std: 2.9
    fpr:
      mean: 0.229
      std: 0.075
    vs_single_seed:
      single_seed_bal_acc: 0.839
      multi_seed_mean: 0.772
      delta: -0.067
      note: Single seed (0.839) is optimistic; multi-seed mean (0.772) more representative
    finding: GRU robust across 5 seeds (std=3.8pp < 5pp threshold). Single-seed result
      overestimates by ~6.7pp. Lead time high variance (std=2.9) indicates sensitivity
      to data split.
- exp_id: exp_r3_selectivity_corrected
  name: ''
  status: DONE
  conclusion: success
  metrics:
    qwq_32b_l60:
      real_acc: 0.667
      random_mean: 0.523
      random_std: 0.051
      selectivity_pp: 14.4
      position_baseline_acc: 0.705
      layer: 60
    r1_32b_l63:
      real_acc: 0.746
      random_mean: 0.549
      random_std: 0.06
      selectivity_pp: 19.7
      position_baseline_acc: 0.624
      layer: 63
    comparison:
      qwq_old_l2: 15.3
      qwq_new_l60: 14.4
      r1_32b_old_l10: 7.5
      r1_32b_new_l63: 19.7
    both_pass_5pp: true
    finding: Both corrected layers pass 5pp threshold. R1-32B selectivity dramatically
      improves from 7.5pp (L10) to 19.7pp (L63). QwQ stable (15.3→14.4pp). Deep layers
      encode stronger safety signal beyond positional confounds.
- exp_id: exp_r3_bootstrap_10k
  name: ''
  status: DONE
  conclusion: success
  metrics:
    n_resamples: 10000
    holm_bonferroni: 12/12 pass
    tests:
      r1_8b_bal_acc:
        delta: 0.1796
        p: 0
        rank: 1
      r1_8b_precision:
        delta: 0.2786
        p: 0
        rank: 2
      r1_8b_fpr:
        delta: -0.1255
        p: 0
        rank: 3
      ot_7b_precision:
        delta: 0.2189
        p: 0
        rank: 4
      ot_7b_fpr:
        delta: -0.1705
        p: 0
        rank: 5
      r1_32b_bal_acc:
        delta: 0.1871
        p: 0
        rank: 6
      r1_32b_precision:
        delta: 0.1544
        p: 0
        rank: 7
      qwq_32b_bal_acc:
        delta: 0.1478
        p: 0
        rank: 8
      qwq_32b_precision:
        delta: 0.2349
        p: 0
        rank: 9
      ot_7b_bal_acc:
        delta: 0.1067
        p: 0.0003
        rank: 10
      qwq_32b_fpr:
        delta: -0.0952
        p: 0.0061
        rank: 11
      r1_32b_fpr:
        delta: -0.1457
        p: 0.0096
        rank: 12
    marginal_tests:
      r1_32b_fpr:
        p: 0.0096
        threshold: 0.05
      qwq_32b_fpr:
        p: 0.0061
        threshold: 0.025
    r1_8b_fpr_clarification: R1-8B FPR at W=3 is p<0.0001 (rank 3), not marginal.
      The 0.044 was from old W=15 config.
    finding: 'All 12/12 Holm-Bonferroni pass with 10000 resamples. R1-8B FPR not marginal
      at corrected W=3. Actual marginal tests: R1-32B FPR (p=0.0096) and QwQ FPR (p=0.0061),
      both passing comfortably.'
- exp_id: exp_r5_auroc_layer_sweep
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    r1_8b:
      auroc_best_layer: 13
      auroc_best: 0.806
      paper_layer: 14
      auroc_at_paper: 0.803
      match: near-match (adjacent, delta=0.003)
    ot_7b:
      auroc_best_layer: 1
      auroc_best: 0.777
      paper_layer: 16
      auroc_at_paper: 0.746
      match: no (flat landscape 0.70-0.78)
    qwq_32b:
      auroc_best_layer: 32
      auroc_best: 0.839
      paper_layer: 60
      auroc_at_paper: 0.756
      match: no (AUROC prefers mid-depth ~50%)
    r1_32b:
      auroc_best_layer: 31
      auroc_best: 0.897
      paper_layer: 63
      auroc_at_paper: 0.767
      match: no (AUROC prefers mid-depth ~50%)
    finding: 'AUROC does NOT converge to the same deep layers. For 32B models, AUROC
      selects mid-depth layers (~50%) vs paper''s very deep layers (>90%). R1-8B near-match
      only. Note: worker applied PCA-256 on 32B models to handle dimensionality, which
      may affect results.'
- exp_id: exp_r5_pca384_control
  name: ''
  status: DONE
  conclusion: success
  metrics:
    holm_bonferroni: 10/12 reject
    tests:
      r1_8b_bal_acc:
        pca384: 0.7001
        text: 0.6875
        delta: 0.0126
        p: 0.731
        reject: false
      r1_8b_precision:
        pca384: 0.8162
        text: 0.5852
        delta: 0.231
        p: 0
        reject: true
      r1_8b_fpr:
        pca384: 0.0668
        text: 0.1614
        delta: -0.0947
        p: 0.003
        reject: true
      ot_7b_bal_acc:
        pca384: 0.7558
        text: 0.643
        delta: 0.1128
        p: 0
        reject: true
      ot_7b_precision:
        pca384: 0.5225
        text: 0.3545
        delta: 0.1681
        p: 0
        reject: true
      ot_7b_fpr:
        pca384: 0.1207
        text: 0.2477
        delta: -0.127
        p: 0
        reject: true
      qwq_bal_acc:
        pca384: 0.8116
        text: 0.6504
        delta: 0.1612
        p: 0
        reject: true
      qwq_precision:
        pca384: 0.608
        text: 0.4213
        delta: 0.1867
        p: 0
        reject: true
      qwq_fpr:
        pca384: 0.173
        text: 0.2871
        delta: -0.1141
        p: 0.038
        reject: false
      r1_32b_bal_acc:
        pca384: 0.7471
        text: 0.6461
        delta: 0.1011
        p: 0.011
        reject: true
      r1_32b_precision:
        pca384: 0.6343
        text: 0.4503
        delta: 0.184
        p: 0.002
        reject: true
      r1_32b_fpr:
        pca384: 0.2256
        text: 0.3809
        delta: -0.1553
        p: 0.006
        reject: true
    pca_explained_variance:
      r1_8b: 0.793
      ot_7b: 0.828
      qwq_32b: 0.881
      r1_32b: 0.924
    finding: 'Modality advantage persists at matched 384d dimensionality. 10/12 Holm-Bonferroni
      reject. Precision gains +16.8 to +23.1pp across all 4 models. Two non-rejections:
      R1-8B bal_acc (small delta 1.3pp) and QwQ FPR (raw p=0.038, adj threshold too
      strict).'
- exp_id: exp_safe_trace_fpr_multimodel
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    ot7b_hs_static_fpr: 0.111
    ot7b_text_static_fpr: 0.302
    ot7b_hs_temp_fpr: 0.175
    ot7b_text_temp_fpr: 0.46
    qwq_hs_static_fpr: 0.5
    qwq_text_static_fpr: 0.325
    qwq_hs_temp_fpr: 0.45
    qwq_text_temp_fpr: 0.425
    r1_32b_hs_static_fpr: 0.239
    r1_32b_text_static_fpr: 0.31
    r1_32b_hs_temp_fpr: 0.239
    r1_32b_text_temp_fpr: 0.31
- exp_id: exp_qwq_safe_fpr_correct_lr
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    hs_cv_acc: 0.935
    hs_step_fpr: 0.279
    hs_trace_fpr_k5: 0.475
    text_cv_acc: 0.667
    text_step_fpr: 0.394
    text_trace_fpr_k5: 0.5
- exp_id: exp_bge_large_text_comparison
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b_hs_prec: 0.497
    r1_8b_bge_prec: 0.436
    r1_8b_diff: 0.058
    r1_8b_p: 0.185
    r1_8b_hb: false
    ot_7b_hs_prec: 0.446
    ot_7b_bge_prec: 0.263
    ot_7b_diff: 0.181
    ot_7b_p: 0
    ot_7b_hb: true
    r1_32b_hs_prec: 0.588
    r1_32b_bge_prec: 0.475
    r1_32b_diff: 0.117
    r1_32b_p: 0.027
    r1_32b_hb: false
    qwq_32b_hs_prec: 0.545
    qwq_32b_bge_prec: 0.454
    qwq_32b_diff: 0.094
    qwq_32b_p: 0.132
    qwq_32b_hb: false
    hb_pass_count: 1/4
- exp_id: nested_cv_7_8b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b_mean_delta_prec: 0.174
    r1_8b_std_delta_prec: 0.026
    r1_8b_hs_better_folds: 5/5
    ot_7b_mean_delta_prec: 0.164
    ot_7b_std_delta_prec: 0.033
    ot_7b_hs_better_folds: 5/5
    total_hs_better: 10/10
- exp_id: random_cp_qwq32b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    real_cp_cr_composite_layer: 4
    real_cp_precision_layer: 63
    real_cp_gap: 59
    random_cp_cr_shallow_freq: 0.8
    random_cp_precision_deep_freq: 0.2
    metric_disagreement_replicates: false
- exp_id: split_half_ot7b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    half1_cr_composite_layer: 0
    half2_cr_composite_layer: 0
    half1_precision_layer: 20
    half2_precision_layer: 26
    half1_delta_prec: 0.262
    half2_delta_prec: 0.154
    cr_composite_both_shallow: true
    threshold_both_deep: true
    delta_precision_same_direction: true
    delta_ba_same_direction: true
    all_checkpoints_pass: true
- exp_id: sf3_quadratic_residual
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b_linear_gap: 0.104
    r1_8b_linear_p: 0.0001
    r1_8b_linear_hb: true
    r1_8b_quad_gap: 0.103
    r1_8b_quad_p: 0.0001
    r1_8b_quad_hb: true
    ot_7b_linear_gap: 0.114
    ot_7b_linear_p: 0.0001
    ot_7b_linear_hb: true
    ot_7b_quad_gap: 0.098
    ot_7b_quad_p: 0.0003
    ot_7b_quad_hb: true
    r1_32b_linear_gap: -0.014
    r1_32b_linear_p: 0.598
    r1_32b_linear_hb: false
    r1_32b_quad_gap: 0
    r1_32b_quad_p: 0.499
    r1_32b_quad_hb: false
    qwq_32b_l60_w3_linear_gap: 0.074
    qwq_32b_l60_w3_linear_p: 0.0017
    qwq_32b_l60_w3_linear_hb: true
    qwq_32b_l60_w3_quad_gap: -0.01
    qwq_32b_l60_w3_quad_p: 0.6384
    qwq_32b_l60_w3_quad_hb: false
    note: QwQ corrected from layer_idx=63 to L60, W=3
- exp_id: n6_multi_metric_ensemble
  name: ''
  status: DONE
  conclusion: success
  metrics:
    r1_8b_ensemble_prec: 0.565
    r1_8b_best_single_prec: 0.604
    r1_8b_text_prec: 0.372
    r1_8b_ens_vs_text_gap: 0.193
    ot_7b_ensemble_prec: 0.506
    ot_7b_best_single_prec: 0.473
    ot_7b_text_prec: 0.236
    ot_7b_ens_vs_text_gap: 0.27
    qwq_32b_ensemble_prec: 0.578
    qwq_32b_best_single_prec: 0.578
    qwq_32b_text_prec: 0.374
    qwq_32b_ens_vs_text_gap: 0.203
    r1_32b_ensemble_prec: 0.581
    r1_32b_best_single_prec: 0.583
    r1_32b_text_prec: 0.476
    r1_32b_ens_vs_text_gap: 0.105
    all_ens_vs_text_significant: true
    ens_vs_text_p_max: 0.002
    ens_never_worse_than_best_single: true
    ot_7b_ens_beats_best_single: 0.033
- exp_id: r1_8b_full_layer_sweep
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_layers:
      bal_acc:
        W1: L12
        W3: L12
        W5: L12
        W15: L11
      precision:
        W1: L16
        W3: L12
        W5: L12
        W15: L9
      fpr:
        W1: L16
        W3: L9
        W5: L9
        W15: L8
      crossing_rate:
        W1: L0
        W3: L0
        W5: L0
        W15: L0
      composite:
        W1: L16
        W3: L12
        W5: L12
        W15: L9
    max_layer_gap_same_model: 16
    hs_vs_text_gap: 0.15-0.17 stable across all layers
    shallow_bias_W15_only: true
    traces: 209
    seed: 42
- exp_id: advbench_r1_8b_full
  name: ''
  status: DONE
  conclusion: failed
  metrics: {}
- exp_id: pca_artifact_verification
  name: ''
  status: DONE
  conclusion: success
  metrics:
    pca100d_best_precision: 0.633
    nopca_best_precision: 0.732
    pca100d_best_fpr: 0.145
    nopca_best_fpr: 0.072
    pca100d_best_composite: 0.43
    nopca_best_composite: 0.803
    pca100d_cr_best_layer: L0
    nopca_best_layer_range: L9-L16
    n_traces: 209
- exp_id: advbench_llm_cp_annotation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: advbench_llm_cp_full
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen3_cp_dryrun
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen3_cp_dryrun2
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: qwen3_cp_full
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: gpt4omini-cp-annotation
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: advbench_phase4_layer_sweep
  name: ''
  status: DONE
  conclusion: killed
  metrics: {}
- exp_id: random_cp_r1_8b
  name: ''
  status: DONE
  conclusion: success
  metrics:
    crossing_rate_random_mean_layer: 10.7
    crossing_rate_random_shallow_pct: 0
    precision_random_mean_layer: 0
    precision_random_shallow_pct: 100
    metric_disagreement_replicates: false
    real_cp_cr_composite_layer: 0
    real_cp_precision_layer: 23
    real_cp_gap: 23
    elapsed_s: 105.4


## what_if (hypothetical experiments — additive)

- name: ensemble_cv_7b
  claim: C1 (layer selection bias mitigation)
  description: 5-fold CV validation of multi-metric ensemble layer selection on 7-8B
    models (R1-8B + OT-7B). Validates that ensemble eliminates metric-induced bias
    under cross-validation, upgrading from preliminary to validated diagnostic guidance.
  estimated_gpu_hours: 0.5

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: best
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "d07c2da2-cedb-41ee-ba77-fbe4760dc55d",
  "type": "user",
  "uuid": "628e310d-af28-4c9a-80d6-f2465a2fefa8",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:24:17.791Z_

```json
{
  "parentUuid": "628e310d-af28-4c9a-80d6-f2465a2fefa8",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "857c5da9-2b4a-4e02-90d8-b88d63cfe207",
  "timestamp": "2026-05-21T21:24:17.791Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:24:17.791Z_

```json
{
  "parentUuid": "857c5da9-2b4a-4e02-90d8-b88d63cfe207",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "d91e7f2e-fc18-4029-8328-d34b34290918",
  "timestamp": "2026-05-21T21:24:17.791Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T21:24:17.791Z_

```json
{
  "parentUuid": "d91e7f2e-fc18-4029-8328-d34b34290918",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d6f3494c-bcb2-402b-8bee-1430008eafac",
  "timestamp": "2026-05-21T21:24:17.791Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer se…",
  "leafUuid": "d6f3494c-bcb2-402b-8bee-1430008eafac",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Layer selection sensitivity in safety commitment detection",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Assistant

_source line 9 · 2026-05-21T21:24:21.169Z_

I'll review the experiment plan and the best tier definition to generate detailed predicted results for each planned experiment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6f3494c-bcb2-402b-8bee-1430008eafac",
  "isSidechain": false,
  "requestId": "req_011CbGREcSfdrk7RPK8VSqHR",
  "type": "assistant",
  "uuid": "be7975b3-fba9-4760-b093-156413934e8d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dxv6FXkabCarnmU6RtCC3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 37341,
      "cache_read_input_tokens": 11447,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 265,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 37341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37341
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-21T21:24:25.950Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01G2fGXGXv4Czw3CUD1ELhfv`</summary>

```json
{
  "description": "Review experiment plan details",
  "prompt": "I need to understand the full experiment plan and registry in this project. Read the following files to get complete context:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/paper_framing.md (if it exists as a separate file)\n2. Any files matching experiment_plan* or registry* in the project root\n3. Any YAML or JSON files that contain the experiment plan or what_if definitions\n\nSearch the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_5/ for these files. Report back the full contents of experiment_plan if found as a separate file, and list all files in the project root.",
  "subagent_type": "Explore"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be7975b3-fba9-4760-b093-156413934e8d",
  "isSidechain": false,
  "requestId": "req_011CbGREcSfdrk7RPK8VSqHR",
  "type": "assistant",
  "uuid": "63eaf456-c8c6-4972-b6f7-b86e98bd17b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014dxv6FXkabCarnmU6RtCC3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 37341,
      "cache_read_input_tokens": 11447,
      "output_tokens": 265,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 265,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 37341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37341
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-21T21:25:19.526Z_

<details><summary>↩ Tool result · `toolu_01G2fGXGXv4Czw3CUD1ELhfv`</summary>

```text
Perfect! Now I have comprehensive context. Let me create a detailed summary of the project structure and experiment plans:

## Complete Experiment Plan and Registry Summary

I've successfully explored the project and identified two major research projects with detailed experiment plans and registries. Here's the complete context:

### Project Directory Structure

**/home/ubuntu/.agent-ml-research-idea_gen_0509_5/** contains two main research projects:
- **structfuse-context** — Code retrieval with structural mining strategies
- **contrastive_trace_safety** — LLM safety monitoring via hidden-state probing

---

## Project 1: StructFuse-Context

**File locations:**
- Experiment plan: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml` (223 lines)
- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` (1,887 lines)
- Paper framing: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md`

**Core Research Question:** What hard negative mining strategies work best for contrastive code retrieval, and why?

**Main Claims (3):**
1. Simple static embedding-distance mining provides reliable retrieval improvement at zero additional computational cost (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1)
2. Structure-grounded (dataflow) negatives interact with encoder representation geometry but don't consistently outperform embedding mining (exploratory observation)
3. Scope-bounded inter-procedural data-flow analysis via CodeQL provides practical pipeline for computing structural connectivity at scale

**Target Venue:** EMNLP 2026 Main (Deadline: ARR May 25, 2026)

**Experiment Plan Overview (21 experiments):**

| Phase | Experiment ID | Priority | Description | GPU Hours | Status |
|-------|---------------|----------|-------------|-----------|--------|
| M1 | plan_001 | P0 | CodeQL extraction + connected vs gold statistics | 0 | DONE |
| M2 | plan_002 | P0 | 3-strategy contrastive training (random/embedding/dataflow) | 200 | In progress (4/9 runs) |
| M3a | plan_003 | P0 | SWE-bench Lite end-to-end evaluation | 40 | Awaiting M2 checkpoint |
| M3b | plan_004 | P1 | RepoBench-R cross-file retrieval evaluation | 15 | Awaiting M2 + multi-seed CIs |
| Analysis | plan_005 | P1 | Embedding vs random stratified analysis | 5 | Extended scope needed |
| Scalability | plan_006 | P0 | M1 scalability statistics | 0 | DONE |
| Ablations | plan_007-010 | P1-P2 | 1-3 hop call-graph, data size scaling, fusion head, distance weighting | 55 total | Pending |
| Downstream | plan_011-012 | P1-P2 | Failure analysis, qualitative examples | 5 | Awaiting plan_003 |
| Validation | plan_013 | P0 | StarCoder-3B multi-seed validation (generality) | 15 | DONE (pilot) |
| Ablations | plan_014-015 | P1 | Temperature regime, dynamic vs static mining | 80 | Pending |
| Stats | plan_016 | P0 | Bootstrap CI for SWE-bench | 0 | Pending |
| Analysis | plan_017 | P1 | Literature comparison (CodexGraph, LocAgent) | 0 | DONE |
| Baseline | plan_018 | P0 | BM25 negative baseline (Dream #1 consensus gap) | 15 | High priority |
| Sensitivity | plan_019 | P1 | Pool size sensitivity (50/100/200/500) | 5 | Pending |
| Validation | plan_020 | P1 | UniXcoder multi-seed validation | 6 | Pending |
| Reduced Ablation | plan_021 | P1 | Temperature τ ∈ {0.05, 0.2} reduced scope | 15 | Pending |

**Key M2 Progress:**
- m2_full_qwen: 4/9 runs complete (random s42/s43/s44 ✓, embedding_distance_s43 ✓)
- m2_full_starcoder: 1/9+ runs complete
- m1_reextract_v2: 90.5% complete (25,582/28,276 repos)

**Dream Review Key Findings:**
- Plan 018 (BM25 baseline) identified as #1 structural gap across all 3 tiers
- Plans 004, 005: Need multi-seed CIs and extended stratification
- Writing discipline: Avoid "complementary signal" overstatement

---

## Project 2: Contrastive Trace Safety

**File locations:**
- Experiment plan: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/experiment_plan.yaml` (126 lines)
- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/registry.yaml` (2,599 lines)
- Paper framing: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md`

**Core Research Question:** How to detect reasoning-model safety commitment (self-jailbreak) across architectures and scales?

**Main Claims (3 + 1 methodological):**
1. **Temporal context universally improves probe accuracy** across both modalities (text + hidden-state) — HS: +3pp accuracy, +13pp precision, -50% FPR; Text: +3-12pp bal_acc, +8-23pp precision
2. **HS probes outperform text at correctly selected layers** with strong evidence at 7-8B (precision +22.4pp) and qualified evidence at 32B (layer selection metric bias previously masked signal)
3. **HS and text monitoring exhibit different detection timing profiles** — HS detects AT commitment; text detects 10 steps earlier (but trigger-happy); GRU achieves modest positive lead (+4.5 steps)
4. **Methodological: Layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers**, entirely masking HS advantage at 32B scale

**Target Venue:** EMNLP 2026 Main LLM Security Track (Deadline: ARR May 25, 2026)

**Experiment Plan Overview (15 P0 experiments, ~37 A100-hours total):**

| Experiment ID | Priority | Description | GPU Hours | Status |
|---|---|---|---|---|
| exp-001 | P0 | Cross-architecture layer sweep (R1-32B, QwQ-32B) | 10 | DONE |
| exp-002 | P0 | Cross-architecture temporal evaluation (W=15) | 4 | DONE |
| exp-003 | P0 | Cross-model transfer (Llama↔Qwen) | 2 | DONE |
| exp-004 | P0 | Lead time analysis across models | 1 | DONE |
| exp-005 | P0 | TrajGuard Mahalanobis baseline | 2 | DONE (negative) |
| exp-006 | P0 | Bootstrap CI + threshold-independent metrics | 1 | DONE |
| exp-007 | P1 | Window size ablation (W=1,3,5,10,15,20,25) | 2 | Pending |
| exp-008 | P1 | Layer selection ablation (all layers for 32B) | 3 | Pending |
| exp-009 | P1 | 16-label taxonomy supervision | 2 | Pending |
| exp-010 | P1 | Oracle decomposition analysis | 1 | Pending |
| exp-011 | P2 | OpenThinker-7B (Qwen2.5-7B base) | 4 | Pending |
| exp-012 | P2 | GRU/Attention probe upper bound | 4 | Partial |
| exp-013 | P0 | Text-based baseline (sentence-BERT) | 0.5 | CRITICAL missing |
| exp-014 | P0 | BOCPD/CUSUM change-point detection | 0.5 | DONE (negative) |
| exp-015 | P0 | False positive analysis on safe traces | 0.5 | DONE |

**Key Evidence (Holm-Bonferroni Corrected):**

**7-8B Models (R1-8B Llama, OT-7B Qwen):**
- HS significantly outperforms text: Precision +22.4pp (R1-8B), +21.9pp (OT-7B)
- 12/12 Holm-Bonferroni tests pass ✅
- Selectivity: 12.5pp (R1-8B), 18.3pp (OT-7B)

**32B Models (R1-32B, QwQ-32B):**
- **Critical finding**: `bal_acc × crossing_rate` metric selects shallow layers (L2/L10 at 3-16% depth), masking HS advantage
- Corrected layers (threshold-dependent metrics consensus): L60/L63 (94-98% depth)
- At corrected layers: Precision +15.4-23.6pp (ALL 4 models HB-pass)
- **R1-32B caveat**: W=1 only significant (25% coverage), advantage position-mediated
- **QwQ caveat**: Significant across all W but HS detects LATER than text (lead -1.2 to +1.9 steps)

**Negative Results (6 methods fail):**
- BOCPD/CUSUM: 0-93% detection across models, no positive lead
- Mahalanobis: ~0 separation, signal in minor PCs
- RepE direction: Layer-dependent, poor generalization (R1-32B L63: bal_acc=0.559 vs supervised LR 0.826)
- MLP nonlinear probe: Inferior to linear (3/4 models)
- CCS (weakly supervised): R1-32B FPR=0.410, OT-7B precision=0.319
- Cross-model transfer: Fails entirely (best: 58.3% acc)

**Paper Timeline:**
- P0 experiments: May 17-19 (3 days)
- P1: May 19-21
- Writing: May 21-25
- Text baseline (exp-013) can start immediately (no GPU)

---

## Key Shared Registry Entries

Both registries track:
- **status**: DONE / RUNNING / PENDING
- **conclusion**: success / negative / killed
- **spec**: command, server, data_path, model_name, seed, hypothesis
- **metrics**: Model-specific accuracy, precision, FPR, lead times, coverage rates
- **checkpoint_path**: Model weights or diagnostic outputs
- **completed_at**: ISO timestamp

Both projects use **Dream Review cycle** (best/median/worst tiers) to validate findings and identify gaps before paper submission.

---

This comprehensive context shows two active research projects with clear experiment plans, detailed execution history, and specific reviewer feedback integrated into the roadmaps. All files are tracked in YAML format with structured metadata for reproducibility.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "63eaf456-c8c6-4972-b6f7-b86e98bd17b3",
  "isSidechain": false,
  "promptId": "d07c2da2-cedb-41ee-ba77-fbe4760dc55d",
  "type": "user",
  "uuid": "bef8a7f0-1020-43c1-9c94-69ea9306f3b1",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the full experiment plan and registry in this project. Read the following files to get complete context:\n\n1. /home/ubuntu/.agent-ml-research-idea_gen_0509_5/paper_framing.md (if it exists as a separate file)\n2. Any files matching experiment_plan* or registry* in the project root\n3. Any YAML or JSON files that contain the experiment plan or what_if definitions\n\nSearch the project directory /home/ubuntu/.agent-ml-research-idea_gen_0509_5/ for these files. Report back the full contents of experiment_plan if found as a separate file, and list all files in the project root.",
    "agentId": "a47a256e7db757025",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive context. Let me create a detailed summary of the project structure and experiment plans:\n\n## Complete Experiment Plan and Registry Summary\n\nI've successfully explored the project and identified two major research projects with detailed experiment plans and registries. Here's the complete context:\n\n### Project Directory Structure\n\n**/home/ubuntu/.agent-ml-research-idea_gen_0509_5/** contains two main research projects:\n- **structfuse-context** — Code retrieval with structural mining strategies\n- **contrastive_trace_safety** — LLM safety monitoring via hidden-state probing\n\n---\n\n## Project 1: StructFuse-Context\n\n**File locations:**\n- Experiment plan: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/experiment_plan.yaml` (223 lines)\n- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/registry.yaml` (1,887 lines)\n- Paper framing: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/structfuse-context/paper_framing.md`\n\n**Core Research Question:** What hard negative mining strategies work best for contrastive code retrieval, and why?\n\n**Main Claims (3):**\n1. Simple static embedding-distance mining provides reliable retrieval improvement at zero additional computational cost (pilot: +1.6–2.0pp; M2 seed 43: +0.52pp best_by_R@1)\n2. Structure-grounded (dataflow) negatives interact with encoder representation geometry but don't consistently outperform embedding mining (exploratory observation)\n3. Scope-bounded inter-procedural data-flow analysis via CodeQL provides practical pipeline for computing structural connectivity at scale\n\n**Target Venue:** EMNLP 2026 Main (Deadline: ARR May 25, 2026)\n\n**Experiment Plan Overview (21 experiments):**\n\n| Phase | Experiment ID | Priority | Description | GPU Hours | Status |\n|-------|---------------|----------|-------------|-----------|--------|\n| M1 | plan_001 | P0 | CodeQL extraction + connected vs gold statistics | 0 | DONE |\n| M2 | plan_002 | P0 | 3-strategy contrastive training (random/embedding/dataflow) | 200 | In progress (4/9 runs) |\n| M3a | plan_003 | P0 | SWE-bench Lite end-to-end evaluation | 40 | Awaiting M2 checkpoint |\n| M3b | plan_004 | P1 | RepoBench-R cross-file retrieval evaluation | 15 | Awaiting M2 + multi-seed CIs |\n| Analysis | plan_005 | P1 | Embedding vs random stratified analysis | 5 | Extended scope needed |\n| Scalability | plan_006 | P0 | M1 scalability statistics | 0 | DONE |\n| Ablations | plan_007-010 | P1-P2 | 1-3 hop call-graph, data size scaling, fusion head, distance weighting | 55 total | Pending |\n| Downstream | plan_011-012 | P1-P2 | Failure analysis, qualitative examples | 5 | Awaiting plan_003 |\n| Validation | plan_013 | P0 | StarCoder-3B multi-seed validation (generality) | 15 | DONE (pilot) |\n| Ablations | plan_014-015 | P1 | Temperature regime, dynamic vs static mining | 80 | Pending |\n| Stats | plan_016 | P0 | Bootstrap CI for SWE-bench | 0 | Pending |\n| Analysis | plan_017 | P1 | Literature comparison (CodexGraph, LocAgent) | 0 | DONE |\n| Baseline | plan_018 | P0 | BM25 negative baseline (Dream #1 consensus gap) | 15 | High priority |\n| Sensitivity | plan_019 | P1 | Pool size sensitivity (50/100/200/500) | 5 | Pending |\n| Validation | plan_020 | P1 | UniXcoder multi-seed validation | 6 | Pending |\n| Reduced Ablation | plan_021 | P1 | Temperature τ ∈ {0.05, 0.2} reduced scope | 15 | Pending |\n\n**Key M2 Progress:**\n- m2_full_qwen: 4/9 runs complete (random s42/s43/s44 ✓, embedding_distance_s43 ✓)\n- m2_full_starcoder: 1/9+ runs complete\n- m1_reextract_v2: 90.5% complete (25,582/28,276 repos)\n\n**Dream Review Key Findings:**\n- Plan 018 (BM25 baseline) identified as #1 structural gap across all 3 tiers\n- Plans 004, 005: Need multi-seed CIs and extended stratification\n- Writing discipline: Avoid \"complementary signal\" overstatement\n\n---\n\n## Project 2: Contrastive Trace Safety\n\n**File locations:**\n- Experiment plan: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/experiment_plan.yaml` (126 lines)\n- Registry: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/registry.yaml` (2,599 lines)\n- Paper framing: `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/paper_framing.md`\n\n**Core Research Question:** How to detect reasoning-model safety commitment (self-jailbreak) across architectures and scales?\n\n**Main Claims (3 + 1 methodological):**\n1. **Temporal context universally improves probe accuracy** across both modalities (text + hidden-state) — HS: +3pp accuracy, +13pp precision, -50% FPR; Text: +3-12pp bal_acc, +8-23pp precision\n2. **HS probes outperform text at correctly selected layers** with strong evidence at 7-8B (precision +22.4pp) and qualified evidence at 32B (layer selection metric bias previously masked signal)\n3. **HS and text monitoring exhibit different detection timing profiles** — HS detects AT commitment; text detects 10 steps earlier (but trigger-happy); GRU achieves modest positive lead (+4.5 steps)\n4. **Methodological: Layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers**, entirely masking HS advantage at 32B scale\n\n**Target Venue:** EMNLP 2026 Main LLM Security Track (Deadline: ARR May 25, 2026)\n\n**Experiment Plan Overview (15 P0 experiments, ~37 A100-hours total):**\n\n| Experiment ID | Priority | Description | GPU Hours | Status |\n|---|---|---|---|---|\n| exp-001 | P0 | Cross-architecture layer sweep (R1-32B, QwQ-32B) | 10 | DONE |\n| exp-002 | P0 | Cross-architecture temporal evaluation (W=15) | 4 | DONE |\n| exp-003 | P0 | Cross-model transfer (Llama↔Qwen) | 2 | DONE |\n| exp-004 | P0 | Lead time analysis across models | 1 | DONE |\n| exp-005 | P0 | TrajGuard Mahalanobis baseline | 2 | DONE (negative) |\n| exp-006 | P0 | Bootstrap CI + threshold-independent metrics | 1 | DONE |\n| exp-007 | P1 | Window size ablation (W=1,3,5,10,15,20,25) | 2 | Pending |\n| exp-008 | P1 | Layer selection ablation (all layers for 32B) | 3 | Pending |\n| exp-009 | P1 | 16-label taxonomy supervision | 2 | Pending |\n| exp-010 | P1 | Oracle decomposition analysis | 1 | Pending |\n| exp-011 | P2 | OpenThinker-7B (Qwen2.5-7B base) | 4 | Pending |\n| exp-012 | P2 | GRU/Attention probe upper bound | 4 | Partial |\n| exp-013 | P0 | Text-based baseline (sentence-BERT) | 0.5 | CRITICAL missing |\n| exp-014 | P0 | BOCPD/CUSUM change-point detection | 0.5 | DONE (negative) |\n| exp-015 | P0 | False positive analysis on safe traces | 0.5 | DONE |\n\n**Key Evidence (Holm-Bonferroni Corrected):**\n\n**7-8B Models (R1-8B Llama, OT-7B Qwen):**\n- HS significantly outperforms text: Precision +22.4pp (R1-8B), +21.9pp (OT-7B)\n- 12/12 Holm-Bonferroni tests pass ✅\n- Selectivity: 12.5pp (R1-8B), 18.3pp (OT-7B)\n\n**32B Models (R1-32B, QwQ-32B):**\n- **Critical finding**: `bal_acc × crossing_rate` metric selects shallow layers (L2/L10 at 3-16% depth), masking HS advantage\n- Corrected layers (threshold-dependent metrics consensus): L60/L63 (94-98% depth)\n- At corrected layers: Precision +15.4-23.6pp (ALL 4 models HB-pass)\n- **R1-32B caveat**: W=1 only significant (25% coverage), advantage position-mediated\n- **QwQ caveat**: Significant across all W but HS detects LATER than text (lead -1.2 to +1.9 steps)\n\n**Negative Results (6 methods fail):**\n- BOCPD/CUSUM: 0-93% detection across models, no positive lead\n- Mahalanobis: ~0 separation, signal in minor PCs\n- RepE direction: Layer-dependent, poor generalization (R1-32B L63: bal_acc=0.559 vs supervised LR 0.826)\n- MLP nonlinear probe: Inferior to linear (3/4 models)\n- CCS (weakly supervised): R1-32B FPR=0.410, OT-7B precision=0.319\n- Cross-model transfer: Fails entirely (best: 58.3% acc)\n\n**Paper Timeline:**\n- P0 experiments: May 17-19 (3 days)\n- P1: May 19-21\n- Writing: May 21-25\n- Text baseline (exp-013) can start immediately (no GPU)\n\n---\n\n## Key Shared Registry Entries\n\nBoth registries track:\n- **status**: DONE / RUNNING / PENDING\n- **conclusion**: success / negative / killed\n- **spec**: command, server, data_path, model_name, seed, hypothesis\n- **metrics**: Model-specific accuracy, precision, FPR, lead times, coverage rates\n- **checkpoint_path**: Model weights or diagnostic outputs\n- **completed_at**: ISO timestamp\n\nBoth projects use **Dream Review cycle** (best/median/worst tiers) to validate findings and identify gaps before paper submission.\n\n---\n\nThis comprehensive context shows two active research projects with clear experiment plans, detailed execution history, and specific reviewer feedback integrated into the roadmaps. All files are tracked in YAML format with structured metadata for reproducibility."
      }
    ],
    "totalDurationMs": 53570,
    "totalTokens": 64964,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 16076,
      "cache_read_input_tokens": 45977,
      "output_tokens": 2905,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 16076
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 2905,
          "cache_read_input_tokens": 45977,
          "cache_creation_input_tokens": 16076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 16076,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 8,
      "searchCount": 6,
      "bashCount": 5,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "63eaf456-c8c6-4972-b6f7-b86e98bd17b3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-21T21:25:22.753Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PHcK76DfRwP9xcdQoDQaH8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/experiment_plan.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bef8a7f0-1020-43c1-9c94-69ea9306f3b1",
  "isSidechain": false,
  "requestId": "req_011CbGRKAKRmaac5v1yXEzwM",
  "type": "assistant",
  "uuid": "e2fcc52d-bc10-4fd3-bc72-87cbf0b24ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0182qHyMWWsmhmzAwo3yB7Pf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3178,
      "cache_read_input_tokens": 48788,
      "output_tokens": 87,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3178,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 87,
          "cache_read_input_tokens": 48788,
          "cache_creation_input_tokens": 3178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3178
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-21T21:25:22.765Z_

<details><summary>↩ Tool result · `toolu_01PHcK76DfRwP9xcdQoDQaH8`</summary>

```text
1	experiments:
2	  # === P0: Must-run for paper submission ===
3	
4	  - id: exp-001
5	    claim: 1
6	    description: "Cross-architecture hidden-state extraction + layer sweep + static probe evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers) to find best layer for 64-layer models before probe evaluation. Validates Claim 1 generalizes beyond r1-8b."
7	    priority: P0
8	    gpu_budget_hours: 10
9	    deps: []
10	    models: [DeepSeek-R1-Distill-Qwen-32B, QwQ-32B]
11	    notes: "32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44% depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE reporting static probe results — using wrong layer would produce false negative."
12	
13	  - id: exp-002
14	    claim: 2
15	    description: "Cross-architecture temporal window evaluation: temporal LR W=15 on r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture."
16	    priority: P0
17	    gpu_budget_hours: 4
18	    deps: [exp-001]
19	    models: [DeepSeek-R1-Distill-Qwen-32B, QwQ-32B]
20	
21	  - id: exp-003
22	    claim: [1, 2]
23	    description: "Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture generalization."
24	    priority: P0
25	    gpu_budget_hours: 2
26	    deps: [exp-001]
27	    notes: "Key for cross-architecture story. Projection head needed (4096→5120 or vice versa)."
28	
29	  - id: exp-004
30	    claim: 3
31	    description: "Lead time analysis across models: confirm negative lead time finding on 32B models. Report lead time distribution per model."
32	    priority: P0
33	    gpu_budget_hours: 1
34	    deps: [exp-001, exp-002]
35	
36	  - id: exp-005
37	    claim: [1, 2, 3]
38	    description: "TrajGuard-style Mahalanobis baseline: implement and evaluate on all 3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D)."
39	    priority: P0
40	    gpu_budget_hours: 2
41	    deps: [exp-001]
42	    notes: "Critical baseline for 'existing detectors fail' claim. Use safe traces to estimate covariance, compute MD per step."
43	
44	  - id: exp-006
45	    claim: [1, 2]
46	    description: "Bootstrap confidence intervals + threshold-independent metrics: 1000 bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold variance, and FPR on safe traces (final_judgment=0.5)."
47	    priority: P0
48	    gpu_budget_hours: 1
49	    deps: [exp-001, exp-002, exp-003, exp-004, exp-005]
50	
51	  # === P1: Important but deferrable ===
52	
53	  - id: exp-007
54	    claim: 2
55	    description: "Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal W and show diminishing returns curve."
56	    priority: P1
57	    gpu_budget_hours: 2
58	    deps: [exp-001]
59	
60	  - id: exp-008
61	    claim: 2
62	    description: "Layer selection ablation: all layers (not just 14) for temporal probe on 32B models. Confirm middle-layer finding generalizes."
63	    priority: P1
64	    gpu_budget_hours: 3
65	    deps: [exp-001]
66	
67	  - id: exp-009
68	    claim: 2
69	    description: "16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4) instead of binary commitment for richer training signal. May improve both coverage and timing."
70	    priority: P1
71	    gpu_budget_hours: 2
72	    deps: [exp-001]
73	    notes: "Addresses reviewer concern about underusing available supervision."
74	
75	  - id: exp-010
76	    claim: 3
77	    description: "Oracle decomposition: why can oracle but not probes achieve positive lead time? Analyze what label patterns encode that hidden states don't."
78	    priority: P1
79	    gpu_budget_hours: 1
80	    deps: [exp-004]
81	    notes: "For Discussion section. May reveal what architectural changes could close the gap."
82	
83	  # === P2: Nice-to-have ===
84	
85	  - id: exp-011
86	    claim: 2
87	    description: "OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale matrix. Controls for scale confound."
88	    priority: P2
89	    gpu_budget_hours: 4
90	    deps: [exp-002]
91	    notes: "From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for scale-matched comparison."
92	
93	  - id: exp-012
94	    claim: [1, 2]
95	    description: "GRU/Attention probe as upper bound: verify GRU finding holds on 32B models with more data. If still no improvement over LR, strengthens 'simplicity is optimal' story."
96	    priority: P2
97	    gpu_budget_hours: 4
98	    deps: [exp-001, exp-002]
99	
100	  - id: exp-013
101	    claim: [1, 2]
102	    description: "Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) + same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap text monitoring. If text achieves comparable performance, paper motivation needs restructuring."
103	    priority: P0
104	    gpu_budget_hours: 0.5
105	    deps: []
106	    notes: "No GPU needed for embedding extraction (small model, CPU-feasible). Run on all 4 models. This is the single most important missing baseline per Dream review (flagged by all 3 tiers, both reviewers)."
107	
108	  - id: exp-014
109	    claim: 3
110	    description: "Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores: apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve positive lead time by detecting distributional shift before textual commitment. Also test CUSUM as simpler alternative."
111	    priority: P0
112	    gpu_budget_hours: 0.5
113	    deps: [exp-001]
114	    notes: "Addresses both 'no method novelty' and 'no positive lead time' criticisms simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes a genuine methods contribution. If it also fails, strengthens the 'fundamental limitation' narrative."
115	
116	  - id: exp-015
117	    claim: [1, 2]
118	    description: "False positive analysis: run all probes (static, temporal, GRU, BOCPD) on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various thresholds. Essential for deployment utility claims."
119	    priority: P0
120	    gpu_budget_hours: 0.5
121	    deps: [exp-001, exp-002]
122	    notes: "Dream flagged missing FPR as critical gap across median and worst tiers. Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere gets 100% coverage."
123	
124	gpu_budget_total: "~37 A100-hours (P0: 19.5h, P1: 8h, P2: 8h, new P0: +1.5h)"
125	timeline: "P0 experiments: May 17-19 (3 days). P1: May 19-21. Paper writing: May 21-25. Text baseline (exp-013) can start immediately (no GPU). BOCPD (exp-014) after first probe scores available."
126	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e2fcc52d-bc10-4fd3-bc72-87cbf0b24ded",
  "isSidechain": false,
  "promptId": "d07c2da2-cedb-41ee-ba77-fbe4760dc55d",
  "type": "user",
  "uuid": "66e50350-ab08-4c50-937a-6b2e3adb21d6",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/experiment_plan.yaml",
      "content": "experiments:\n  # === P0: Must-run for paper submission ===\n\n  - id: exp-001\n    claim: 1\n    description: \"Cross-architecture hidden-state extraction + layer sweep + static probe evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers) to find best layer for 64-layer models before probe evaluation. Validates Claim 1 generalizes beyond r1-8b.\"\n    priority: P0\n    gpu_budget_hours: 10\n    deps: []\n    models: [DeepSeek-R1-Distill-Qwen-32B, QwQ-32B]\n    notes: \"32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44% depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE reporting static probe results — using wrong layer would produce false negative.\"\n\n  - id: exp-002\n    claim: 2\n    description: \"Cross-architecture temporal window evaluation: temporal LR W=15 on r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.\"\n    priority: P0\n    gpu_budget_hours: 4\n    deps: [exp-001]\n    models: [DeepSeek-R1-Distill-Qwen-32B, QwQ-32B]\n\n  - id: exp-003\n    claim: [1, 2]\n    description: \"Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture generalization.\"\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-001]\n    notes: \"Key for cross-architecture story. Projection head needed (4096→5120 or vice versa).\"\n\n  - id: exp-004\n    claim: 3\n    description: \"Lead time analysis across models: confirm negative lead time finding on 32B models. Report lead time distribution per model.\"\n    priority: P0\n    gpu_budget_hours: 1\n    deps: [exp-001, exp-002]\n\n  - id: exp-005\n    claim: [1, 2, 3]\n    description: \"TrajGuard-style Mahalanobis baseline: implement and evaluate on all 3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).\"\n    priority: P0\n    gpu_budget_hours: 2\n    deps: [exp-001]\n    notes: \"Critical baseline for 'existing detectors fail' claim. Use safe traces to estimate covariance, compute MD per step.\"\n\n  - id: exp-006\n    claim: [1, 2]\n    description: \"Bootstrap confidence intervals + threshold-independent metrics: 1000 bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold variance, and FPR on safe traces (final_judgment=0.5).\"\n    priority: P0\n    gpu_budget_hours: 1\n    deps: [exp-001, exp-002, exp-003, exp-004, exp-005]\n\n  # === P1: Important but deferrable ===\n\n  - id: exp-007\n    claim: 2\n    description: \"Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal W and show diminishing returns curve.\"\n    priority: P1\n    gpu_budget_hours: 2\n    deps: [exp-001]\n\n  - id: exp-008\n    claim: 2\n    description: \"Layer selection ablation: all layers (not just 14) for temporal probe on 32B models. Confirm middle-layer finding generalizes.\"\n    priority: P1\n    gpu_budget_hours: 3\n    deps: [exp-001]\n\n  - id: exp-009\n    claim: 2\n    description: \"16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4) instead of binary commitment for richer training signal. May improve both coverage and timing.\"\n    priority: P1\n    gpu_budget_hours: 2\n    deps: [exp-001]\n    notes: \"Addresses reviewer concern about underusing available supervision.\"\n\n  - id: exp-010\n    claim: 3\n    description: \"Oracle decomposition: why can oracle but not probes achieve positive lead time? Analyze what label patterns encode that hidden states don't.\"\n    priority: P1\n    gpu_budget_hours: 1\n    deps: [exp-004]\n    notes: \"For Discussion section. May reveal what architectural changes could close the gap.\"\n\n  # === P2: Nice-to-have ===\n\n  - id: exp-011\n    claim: 2\n    description: \"OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale matrix. Controls for scale confound.\"\n    priority: P2\n    gpu_budget_hours: 4\n    deps: [exp-002]\n    notes: \"From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for scale-matched comparison.\"\n\n  - id: exp-012\n    claim: [1, 2]\n    description: \"GRU/Attention probe as upper bound: verify GRU finding holds on 32B models with more data. If still no improvement over LR, strengthens 'simplicity is optimal' story.\"\n    priority: P2\n    gpu_budget_hours: 4\n    deps: [exp-001, exp-002]\n\n  - id: exp-013\n    claim: [1, 2]\n    description: \"Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) + same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap text monitoring. If text achieves comparable performance, paper motivation needs restructuring.\"\n    priority: P0\n    gpu_budget_hours: 0.5\n    deps: []\n    notes: \"No GPU needed for embedding extraction (small model, CPU-feasible). Run on all 4 models. This is the single most important missing baseline per Dream review (flagged by all 3 tiers, both reviewers).\"\n\n  - id: exp-014\n    claim: 3\n    description: \"Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores: apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve positive lead time by detecting distributional shift before textual commitment. Also test CUSUM as simpler alternative.\"\n    priority: P0\n    gpu_budget_hours: 0.5\n    deps: [exp-001]\n    notes: \"Addresses both 'no method novelty' and 'no positive lead time' criticisms simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes a genuine methods contribution. If it also fails, strengthens the 'fundamental limitation' narrative.\"\n\n  - id: exp-015\n    claim: [1, 2]\n    description: \"False positive analysis: run all probes (static, temporal, GRU, BOCPD) on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various thresholds. Essential for deployment utility claims.\"\n    priority: P0\n    gpu_budget_hours: 0.5\n    deps: [exp-001, exp-002]\n    notes: \"Dream flagged missing FPR as critical gap across median and worst tiers. Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere gets 100% coverage.\"\n\ngpu_budget_total: \"~37 A100-hours (P0: 19.5h, P1: 8h, P2: 8h, new P0: +1.5h)\"\ntimeline: \"P0 experiments: May 17-19 (3 days). P1: May 19-21. Paper writing: May 21-25. Text baseline (exp-013) can start immediately (no GPU). BOCPD (exp-014) after first probe scores available.\"\n",
      "numLines": 126,
      "startLine": 1,
      "totalLines": 126
    }
  },
  "sourceToolAssistantUUID": "e2fcc52d-bc10-4fd3-bc72-87cbf0b24ded",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14 · 2026-05-21T21:25:22.922Z_

````json
{
  "parentUuid": "66e50350-ab08-4c50-937a-6b2e3adb21d6",
  "isSidechain": false,
  "attachment": {
    "type": "nested_memory",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/CLAUDE.md",
    "content": {
      "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/.claude/CLAUDE.md",
      "type": "Project",
      "content": "## 当前项目\n当前绑定项目：**contrastive_trace_safety**\n\n## 按需查阅\n- 项目配置：`load_project_config(\"contrastive_trace_safety\")` 或 `load_project_config(\"contrastive_trace_safety\", section=\"execution\")`\n- 知识文件：`read_project_file(file=...)` 读取项目文件（ROADMAP.md/memory.md/ideas.md/report.md 等）\n- 路线图：`read_roadmap()` 读取研究方向和短期任务\n- 产出目录：`/home/ubuntu/.agent-ml-research-idea_gen_0509_5/projects/contrastive_trace_safety/artifacts/`（写文件后用 `register_artifact` 注册）\n\n## 用户自定义规则（必须遵守）\n### 审稿规则\n\n- **[EMNLP 2026]** “EMNLP 2026 通过 ARR 统一审稿，Main/Findings 不分开投稿（不是两个Track），Long/Short 也走同一审稿系统，Overall Assessment的评分标准如下：5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle（需大幅修改，可在下一周期完成），1.5 = Resubmit after next cycle（需大幅修改，无法在下一周期完成），1 = Do not resubmit（需完全重做或与*ACL无关）”\n- **[EMNLP 2026]** EMNLP 2026 restricts long paper submissions to a strict 8-page limit for main text, with unlimited space for references. Mandatory limitations and optional ethical considerations do not count towards this page limit, provided they do not contain excessive additional content.\n\n### 写作规则\n\n- **[EMNLP 2026]** Limitations 章节只需要写一小段，覆盖 3 个点左右就可以了，不需要写得很长\n- **[EMNLP 2026]** ARR Responsible NLP Checklist在OpenReview的submission form里面（由用户手动填写），而不是在论文pdf里面\n- **[项目]** 图例不得遮挡数据曲线，优先使用 bbox_to_anchor将图例放置在图外，或放在图内无数据的空白区域\n\n> 以上规则由用户配置，优先级等同于硬约束。违反会被 Reviewer 标记。\n\n## Worker 操作规范\n\n### ssh-env-setup\n\n# 远程服务器环境搭建规范\n\n## 核心原则\n\n**先探测，再安装。** 不要假设服务器上什么都没有——很多包已经装好了。安装前必须走 discovery 流程。\n\n**镜像快速路径**：连接服务器后，先用 `detect_image` 检测是否为预置镜像。如果是已知镜像且版本匹配，跳过基础环境搭建（Phase 1-4），直接安装项目特有依赖。未检测到镜像时走传统流程。\n\n**aml-train 镜像使用 conda 环境**（不是 venv）。环境激活：`source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`。pip/python 在 `/root/miniconda3/bin/` 下。**不要假设 .venv 存在，不要创建 venv。**\n\n## Phase 1: 环境探测（用 ssh_read_only）\n\n连接到服务器后，第一步永远是收集信息，不要直接装东西：\n\n```bash\n# 1. Python 环境\nwhich python3 && python3 --version\npip3 --version 2>/dev/null || echo \"NO_PIP\"\n\n# 2. CUDA 环境\nnvidia-smi --query-gpu=name,memory.total,driver_version --format=csv,noheader 2>/dev/null || echo \"NO_GPU\"\nnvcc --version 2>/dev/null | grep \"release\" || echo \"NO_NVCC\"\n\n# 3. 包管理器\nls -d /opt/miniconda3 ~/miniconda3 ~/.conda 2>/dev/null || echo \"NO_CONDA\"\nls -d .venv venv env 2>/dev/null || echo \"NO_VENV\"\npip3 list --format=freeze 2>/dev/null | grep -iE \"torch|transformers|flash\" || echo \"NO_ML_PKGS\"\n\n# 4. PEP 668 检查\npython3 -c \"import sysconfig; print(sysconfig.get_path('stdlib'))\" 2>/dev/null\nls /usr/lib/python*/EXTERNALLY-MANAGED 2>/dev/null && echo \"PEP668_MANAGED\" || echo \"PEP668_OK\"\n```\n\n根据探测结果决定安装策略，不要猜。\n\n## Phase 2: 环境策略选择\n\n根据 Phase 1 结果选择**一个**策略，不要混用：\n\n| 探测结果 | 策略 | 说明 |\n|----------|------|------|\n| 项目目录有 `.venv/` | 用它：`source .venv/bin/activate` | 最优先 |\n| 有 conda 且有写权限 | `conda activate base` 或创建专属 env | 次优先 |\n| PEP668_MANAGED + 无 venv | 创建 venv：`python3 -m venv .venv && source .venv/bin/activate` | 不要用 --break-system-packages |\n| PEP668_OK（无保护） | 直接 `pip install`（旧系统） | 仍建议 venv |\n\n**决不混用 conda install + pip install 到同一环境。** 选了 pip 就全用 pip。\n\n## Phase 3: PyTorch 安装\n\n### CUDA 版本映射（2025-2026 常用）\n\n先从 `nvcc --version` 或 `nvidia-smi` 获取 CUDA 版本，然后匹配：\n\n| CUDA 版本 | PyTorch pip index URL | 推荐 torch 版本 |\n|-----------|----------------------|-----------------|\n| 11.8 | `https://download.pytorch.org/whl/cu118` | ≥ 2.0 |\n| 12.1 | `https://download.pytorch.org/whl/cu121` | ≥ 2.1 |\n| 12.4 | `https://download.pytorch.org/whl/cu124` | ≥ 2.4 |\n| 12.6 | `https://download.pytorch.org/whl/cu126` | ≥ 2.6 |\n\n**不要猜版本号。** 如果不确定可用版本：\n```bash\npip index versions torch --index-url https://download.pytorch.org/whl/cu121 2>/dev/null | head -3\n```\n\n安装命令：\n```bash\npip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu{CUDA_SHORT}\n```\n\n### 大包超时处理\n\nPyTorch wheel 约 500MB-2GB，默认 SSH 超时可能不够。策略：\n\n```bash\n# 方法 1: nohup + 轮询（推荐）\nnohup pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 > /tmp/pip_install.log 2>&1 &\necho $!  # 记录 PID\n\n# 后续用 ssh_read_only 轮询\ncat /tmp/pip_install.log | tail -5\nps -p &lt;PID> -o pid= 2>/dev/null && echo \"STILL_RUNNING\" || echo \"DONE\"\n```\n\n```bash\n# 方法 2: 加大 pip 超时\npip install --timeout 300 torch ...\n```\n\n## Phase 4: 验证（必须执行）\n\n安装后必须验证，不要假设成功：\n\n```bash\npython3 -c \"\nimport torch\nprint(f'torch={torch.__version__}, cuda={torch.cuda.is_available()}, gpus={torch.cuda.device_count()}')\nif torch.cuda.is_available():\n    for i in range(torch.cuda.device_count()):\n        print(f'  GPU {i}: {torch.cuda.get_device_name(i)} ({torch.cuda.get_device_properties(i).total_mem // 1024**3}GB)')\n\"\n```\n\n验证失败的常见原因：\n- `torch.cuda.is_available()` 返回 False → CUDA 版本和 torch 不匹配，重装正确版本\n- `ImportError: libcudnn` → 缺 cuDNN，装 `nvidia-cudnn-cu1x`\n- GPU 数量不对 → 检查 `CUDA_VISIBLE_DEVICES` 环境变量\n\n## Phase 5: 项目依赖\n\n基础环境就绪后，安装项目依赖：\n\n```bash\n# 优先用 requirements.txt / pyproject.toml\npip install -r requirements.txt  # 或 pip install -e .\n\n# 常用 ML 依赖补装\npip install transformers datasets einops accelerate wandb\n```\n\nflash-attention 特殊处理（编译型包）：\n```bash\n# 需要匹配的 CUDA toolkit，编译耗时 5-15 分钟\npip install flash-attn --no-build-isolation\n# 如果编译失败，试预编译版本\npip install flash-attn --no-build-isolation 2>/dev/null || pip install flash-attn-wheels\n```\n\n## ssh_read_only vs ssh_execute 使用规则\n\n| 操作 | 用哪个工具 |\n|------|-----------|\n| 检查环境（python --version, nvidia-smi, pip list） | `ssh_read_only` |\n| 读文件内容、查日志 | `ssh_read_only` |\n| 安装包（pip install, conda install） | `ssh_execute` |\n| 创建/修改文件、启动进程 | `ssh_execute` |\n| 运行实验脚本 | `ssh_execute` |\n\n**原则：能用 read_only 就用 read_only，只有要改变服务器状态时才用 execute。**\n\n## AutoDL 专项注意事项\n\nAutoDL 实例有一系列特殊约束，5 个项目反复踩坑，必须遵守：\n\n### 磁盘\n- **根分区只有 ~30GB，严禁存大文件。** 模型、数据集、HF cache 全部放数据盘 `/root/autodl-tmp/`\n- 设置 `HF_HOME=/root/autodl-tmp/.hf_cache`，否则 HF 默认缓存到根分区导致磁盘满\n- 下载模型时用 `--local-dir /root/autodl-tmp/models/&lt;name>`，不要用默认路径\n\n### 网络\n- pip install / git clone 前必须 `source /etc/network_turbo` 启用代理加速，否则 pypi.nvidia.com 504 超时、GitHub TLS 断连\n- HF 下载设 `HF_HUB_DISABLE_XET=1`，xet_get 在 AutoDL 上返回 401\n- **SSL 证书**：`network_turbo` 的代理使用自签名证书，Python 默认 SSL 验证会失败。必须设置 `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt` 和 `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`，否则 HF 下载、datasets 加载等全部报 SSL 错误\n- **大模型下载优先用 ModelScope**：AutoDL 代理下载 HuggingFace 大文件极慢（~200KB/s），改用 ModelScope 国内 CDN 速度快很多。`pip install modelscope && python -c \"from modelscope import snapshot_download; snapshot_download('Qwen/Qwen2.5-7B-Instruct', cache_dir='/root/autodl-tmp/.hf_cache')\"`\n\n### SSH\n- **AutoDL 实例重启后 SSH 端口会变。** 连接失败时不要反复重试，应提示用户去控制台查新端口并更新 `~/.ssh/config`\n\n## 经验沉淀\n\n- [2026-04-05] Worker 首次连接服务器时，先用一条 ssh_read_only 组合命令完成全部探测，减少 SSH 往返次数\n- [2026-04-05] 遇到 PEP 668 时创建 venv 而非 --break-system-packages，避免污染系统 Python\n- [2026-04-05] PyTorch 大包安装用 nohup 后台执行 + 轮询方式，避免 SSH 超时导致安装中断\n- [2026-04-05] conda 环境和 pip 不要混用——如果项目用 pip，就全部用 pip\n- [2026-04-09] sync_code 前确保本地 commit 已 push 到 remote，否则服务器 git pull 拉不到最新代码\n- [2026-04-09] venv 创建后用 `which python` 验证路径指向正确的 venv python，不要假设系统 PATH 正确\n\n## 更多 Skills（按需加载）\n\n执行相关任务前，先 Read 对应 skill 获取环境配置和最佳实践。\n\n- **paper-writing-norms** — 顶会级别论文写作风格规范——章节写法（Abstract/Intro/Related Work）、去 AI 风格、视觉密度、叙事哲学。Paper Agent 和 Worker 写论文章节时必须加载。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-writing-norms.skill.md`\n- **check-training-status** — 当用户问训练进度/实验状态/查状态时使用。用专用工具查看训练状态，禁止 ssh_execute。  →  `/home/ubuntu/agent-ml-research/skills/global/check-training-status.skill.md`\n- **rebuttal** — 撰写和优化学术 rebuttal——逐条回应审稿意见，生成 response letter。当收到审稿意见、需要写 rebuttal、回复 reviewer 评论时使用。关键词：rebuttal、审稿意见、reviewer response、author response、meta-review、AC 意见。  →  `/home/ubuntu/agent-ml-research/skills/global/rebuttal.skill.md`\n- **review-reviewer-session-start** — Review Reviewer session 启动初始化——检查论文格式、编译状态、材料清单。Review Reviewer 角色 session 启动时自动使用。  →  `/home/ubuntu/agent-ml-research/skills/global/review-reviewer-session-start.skill.md`\n- **reference-audit** — 引用验证与审计——检查 bib 条目完整性、引用真实性、格式一致性。写论文、审查论文、提交前检查引用时使用。关键词：citation verification、引用检查、bib 审计、fake citation、引用格式。  →  `/home/ubuntu/agent-ml-research/skills/global/reference-audit.skill.md`\n- **accelerate-distributed** — HuggingFace Accelerate 分布式训练指南——4行代码实现多GPU/DeepSpeed/FSDP/混合精度。多GPU训练时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/accelerate-distributed.skill.md`\n- **draw-paper-figure** — 生成学术论文级 matplotlib 图表——按 narrative_intent + design_notes 设计，从 pattern 库选用技法，远程 SSH 执行输出 PDF/PNG  →  `/home/ubuntu/agent-ml-research/skills/global/draw-paper-figure.skill.md`\n- **experiment-analysis** — 实验结果分析框架——统计显著性检验、消融分析、baseline 对比、可视化建议。分析实验结果或撰写论文 Results 部分时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/experiment-analysis.skill.md`\n- **hf-hub** — HuggingFace Hub CLI (hf) — 下载/上传模型和数据集、管理缓存、搜索论文和模型。涉及 HuggingFace 资源操作时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/hf-hub.skill.md`\n- **latex-paper** — ML 顶会论文 LaTeX 写作全流程——Claim-Evidence 方法论、引用防幻觉、顶会模板速查、投稿工程链、会议转投。写论文/投稿时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/latex-paper.skill.md`\n- **lm-eval-harness** — lm-evaluation-harness 模型评估指南——MMLU/GSM8K/HumanEval 等 60+ 学术基准测试。评估模型质量、对比实验时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/lm-eval-harness.skill.md`\n- **ml-experiment-guide** — 跨项目 ML 实验避坑指南——从多个项目沉淀的通用踩坑经验与最佳实践。当 Worker 准备写实验代码、或排查实验问题时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/ml-experiment-guide.skill.md`\n- **paper-banana** — 用 PaperBanana 生成学术图表——概念图（架构/流程/framework）首选，探索性统计图也可。LLM 写 matplotlib 代码 + VLM Critic 闭环迭代。需要 GOOGLE_API_KEY。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-banana.skill.md`\n- **paper-image-extractor** — 从论文 PDF 或 arXiv 源码包提取图表——优先 arXiv 原始图片，回退 PDF 解析。用户说\"提取图\"/\"抽图\"/\"extract figures\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/paper-image-extractor.skill.md`\n- **peft-lora** — PEFT/LoRA/QLoRA 参数高效微调指南——LoRA 配置选择、QLoRA 量化训练、Adapter 管理与合并。微调大模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/peft-lora.skill.md`\n- **research-news** — 每日论文推荐——搜索 arXiv 最新论文，按相关性/新颖性/影响力评分，生成推荐列表。Director 说\"有什么新论文\"/\"最近进展\"/\"research news\"时使用。  →  `/home/ubuntu/agent-ml-research/skills/global/research-news.skill.md`\n- **trl-training** — TRL (Transformer Reinforcement Learning) 训练指南——SFT/DPO/GRPO/KTO 配置与最佳实践。训练或对齐语言模型时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/trl-training.skill.md`\n- **wandb-guide** — W&B 查询最佳实践——如何高效使用 fetch_wandb_metrics / compare_wandb_runs / get_best_wandb_run 分析实验结果。分析实验指标时参考。  →  `/home/ubuntu/agent-ml-research/skills/global/wandb-guide.skill.md`\n- **contrastive-trace-safety-research** — LLM safety mechanistic interpretability 领域实验设计共识、方法论趋势与研究空白——10 篇论文蒸馏  →  `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/skills/projects/contrastive_trace_safety/distilled-research.skill.md`\n- **contrastive-trace-safety-writing** — LLM safety interpretability 论文叙事结构、图表设计共识与可模仿策略——8 篇深读蒸馏  →  `/home/ubuntu/.agent-ml-research-idea_gen_0509_5/skills/projects/contrastive_trace_safety/distilled-writing.skill.md`\n",
      "contentDiffersFromDisk": false
    },
    "displayPath": "projects/contrastive_trace_safety/.claude/CLAUDE.md"
  },
  "type": "attachment",
  "uuid": "75ba3184-ea7d-4d1c-8cdb-977e035a5121",
  "timestamp": "2026-05-21T21:25:22.922Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
````

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer se…",
  "leafUuid": "75ba3184-ea7d-4d1c-8cdb-977e035a5121",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Layer selection sensitivity in safety commitment detection",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Assistant

_source line 17 · 2026-05-21T21:26:20.782Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the context I need. Let me carefully analyze the experiment plan and generate detailed predicted results for each "planned" experiment under the "best" tier definition.

Looking at the experiment plan, I need to identify which experiments are still in "planned" status. Let me check - the experiment_plan lists experiments exp-001 through exp-015, but the registry shows many of these are already DONE. The user specifically asks about "planned" experiments, so I need to identify which ones in the experiment_plan haven't been completed in the registry.

Let me cross-reference:

From the experiment_plan:
- exp-001: status "planned" in plan, BUT registry has exp_001a_r1_32b (DONE) and exp_001b_qwq_32b (DONE) → DONE


- exp-002: status "planned" in plan, BUT covered by window ablation (exp_007) and other experiments → DONE (implied by temporal results in paper_framing)
- exp-003: status "planned" in plan, registry has exp_003_cross_transfer (DONE) → DONE
- exp-004: status "planned" in plan, lead time results appear in paper_framing → DONE (implied)
- exp-005: status "planned" in plan, registry has exp_005_trajguard_mahalanobis (DONE) → DONE
- exp-006: status "planned" in plan, registry has exp_006_bootstrap_ci (DONE) → DONE
- exp-007: status "planned" in plan, registry has exp_007_window_ablation (DONE) → DONE

Continuing through the rest of the experiments to identify which ones are truly still in planned status and haven't been executed yet. The user is asking for predicted data across all experiments marked as "planned" in the experiment plan, but I'm realizing that many of these have already been completed in the registry. I think what they actually want is imagined results for the planned experiments, treating them as if they'd run under the best-case scenario, which aligns with the `imagined_experiments` output format they're expecting.

Now I'm working through what the "best" tier would look like in terms of realistic metrics—reviewer scores in the 3.5-4.0 range, strong soundness ratings around 4.0-4.5, and 2-3 champions out of 3 reviewers. I'll use these parameters to generate plausible predicted results for all 15 experiments plus the what_if ensemble variant.

For experiments that already have registry data, I'll anchor to those actual results since they represent what was achieved. For the incomplete ones, I need to project forward with reasonable best-case outcomes that stay grounded in the methodological assumptions—treating layer selection sensitivity as the core contribution, acknowledging the breadth of the model/architecture/scale combinations, and accepting the documented limitations like the high false positive rate.

Now I'm systematizing the detailed predictions across all fifteen experiments plus the ensemble variant, using registry data where available and extrapolating conservatively for the rest.

For the layer sweep experiment, the key finding is that biased metrics favor shallow layers while corrected metrics consistently point to deeper layers, with static probes confirming the hidden state advantage at those corrected depths. The temporal window evaluation shows the improvement holds across architectures though with model-specific tradeoffs between coverage and precision. Cross-model transfer attempts fail decisively, reinforcing that these phenomena don't generalize across different model families. Lead time analysis reveals divergent timing profiles—R1-32B shows strong positive lead while QwQ struggles with minimal or negative lead times.

The Mahalanobis baseline produces near-zero separation across all models, validating that standard detection methods fall short. Bootstrap confidence intervals pass all statistical tests at 10k resamples with Holm-Bonferroni correction. Window size ablation confirms the precision-coverage tradeoff with diminishing returns as window size increases. Layer selection ablation across five metrics and four models uncovered the bias issue and identified the corrected layers. The 16-label taxonomy experiment hasn't been completed yet but shows potential for modest gains.

For the oracle decomposition, the advantage stems from label sequence patterns rather than hidden state content, which confirms a fundamental limitation. OpenThinker-7B is the cleanest performer with all three Holm-Bonferroni tests passing and a selectivity gain of 18.3 percentage points. The GRU on 32B shows only modest improvement over logistic regression when evaluated at the corrected layers. Hidden state features provide a 15-18 percentage point accuracy advantage over text baselines. BOCPD and CUSUM approaches fail on three test cases, confirming they're not viable for this task.

Now I'm looking at the false positive rate analysis—it shows safe FPR ranges between 39-62%, which I've acknowledged as a limitation. The cross-validated ensemble approach hasn't been run yet, but preliminary estimates suggest it would only provide marginal gains of 0-5%, so it's not a load-bearing improvement. I should write out the comprehensive YAML summary with all the numerical predictions for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "75ba3184-ea7d-4d1c-8cdb-977e035a5121",
  "isSidechain": false,
  "requestId": "req_011CbGRKQoKmeKU4P4NmXDfh",
  "type": "assistant",
  "uuid": "0d5fa04e-6fda-4d49-90d7-a2bb57dd8a0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyFkpTyNFGj9scg945YzC9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 51966,
      "output_tokens": 20293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20293,
          "cache_read_input_tokens": 51966,
          "cache_creation_input_tokens": 8224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8224
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-21T21:32:02.069Z_

```yaml
tier: best
narrative_guidance: >
  Best 档叙事完全保留原始 framing。Primary contribution = layer selection metric sensitivity
  作为 researcher-degree-of-freedom 审计（methodological）。Secondary = HS 在正确层上全模型
  优于 text（empirical, 12/12 HB）。Tertiary = 6 种替代方法全部失败（negative results as
  community service）。32B caveats 以诚实科学口吻报告，不做辩护。Ensemble CV 放 appendix，
  不进入主叙事。论文标题强调 "layer selection matters" 角度。

imagined_experiments:
  - name: "exp-001: Cross-architecture layer sweep + static probe (R1-32B, QwQ-32B)"
    plan_id: "exp-001"
    description: >
      64 层模型全层 hidden-state 提取 + 静态 LR probe 评估。发现 bal_acc × crossing_rate
      指标系统性选择浅层（L2/L10），corrected metrics 共识选择深层（L60/L63）。静态 probe
      在 corrected 层显示显著 HS 优势。
    expected_results:
      r1_32b_biased_layer: 10
      r1_32b_biased_layer_depth_pct: 15.6
      r1_32b_corrected_layer: 63
      r1_32b_corrected_layer_depth_pct: 98.4
      r1_32b_layer10_bal_acc: 0.718
      r1_32b_layer10_crossing_rate: 0.60
      r1_32b_layer63_bal_acc_W1: 0.826
      r1_32b_layer63_precision_W1: 0.603
      r1_32b_layer63_fpr_W1: 0.235
      r1_32b_hs_vs_text_precision_delta_W1: "+15.4pp"
      r1_32b_hb_W1: "3/3 pass"
      qwq_biased_layer: 2
      qwq_biased_layer_depth_pct: 3.1
      qwq_corrected_layer: 60
      qwq_corrected_layer_depth_pct: 93.8
      qwq_layer2_bal_acc: 0.730
      qwq_layer60_bal_acc_W3: 0.740
      qwq_layer60_precision_W3: 0.578
      qwq_layer60_fpr_W3: 0.208
      qwq_hs_vs_text_precision_delta_W3: "+23.6pp"
      qwq_hb_all_15_W: "15/15 pass"
      selectivity_r1_32b_l63: "19.7pp"
      selectivity_qwq_l60: "14.4pp"
    result_rationale: >
      Best 档假设 layer selection sensitivity 被接受为可复现的方法论发现。在该前提下，
      32B 模型的 biased → corrected 层切换从 NS (p=0.064-0.83) 翻转为高度显著 (p<0.005)，
      构成论文最强 evidence。R1-32B 的 biased L10 位于 15.6% 深度（浅层），corrected L63
      位于 98.4%（极深层）；QwQ 从 L2 (3.1%) 到 L60 (93.8%)。这一翻转之所以成立，是因为
      浅层 hidden state 表示空间被压缩（cosine distance 1.4-2.7× smaller），crossing_rate
      高但 precision 低。深层的 HS representation 编码了更多 semantic safety signal，
      而非仅靠 positional encoding。4 models 全部在 corrected layers 通过 HB，
      将 "scale-dependent HS advantage" 的旧结论完全推翻为 "metric-dependent layer selection
      artifact"。Reviewer 在 best 档接受这一叙事，因为 5 metrics × 4 models ablation
      是系统性审计，而非 cherry-picking。
    tables:
      - name: "Table 1: Layer Selection Metric × Model → Selected Layer"
        content: |
          | Metric             | R1-8B | OT-7B | QwQ-32B | R1-32B |
          |--------------------|-------|-------|---------|--------|
          | bal_acc × CR       | L0    | L0    | L2 (3%) | L10 (16%) |
          | bal_acc (pure)     | L12   | L9    | L30 (47%) | L47 (73%) |
          | precision          | L16   | L16   | L60 (94%) | L63 (98%) |
          | pre_cp_fpr         | L16   | L20   | L60 (94%) | L63 (98%) |
          | composite          | L16   | L12   | L60 (94%) | L63 (98%) |
      - name: "Table 2: Biased vs Corrected Layer Impact"
        content: |
          | Model   | Biased Layer | Corrected | Biased prec p | Corrected prec p |
          |---------|-------------|-----------|---------------|-----------------|
          | R1-32B  | L10 (16%)   | L63 (98%) | 0.050 (NS)    | <0.001 ✅       |
          | QwQ-32B | L2 (3%)     | L60 (94%) | 0.346 (NS)    | <0.001 ✅       |
    figures_description:
      - "Fig 1: 4-panel heatmap (models × layers), y-axis = metric (5 kinds), color = selected layer depth %. Shallow bias of CR-composite visually stark at 32B."
      - "Fig 2: Before/after scatter — biased vs corrected layer precision for all 4 models. Arrows show metric correction shifts HB from 5/12 → 12/12."
    analysis: >
      实验确立了 layer selection bias 是 32B 模型 HS 优势"消失"的唯一原因。在 best 档下，
      reviewer 接受这一发现的 mechanistic 解释（浅层 compressed representation → noise-driven
      crossings → inflated crossing_rate），而非将其视为"选了更好的超参数"。关键区分：
      这是一个影响 ANY 使用 crossing_rate-contaminated 指标的研究者的 systematic bias，
      而非本文特有的参数选择。LOO-CV 稳定性（65-68% fold 选择 dominant layer）进一步
      证明 selection 的 robustness。

  - name: "exp-002: Cross-architecture temporal window evaluation"
    plan_id: "exp-002"
    description: >
      在 R1-32B 和 QwQ-32B 上评估 temporal LR (W=1-25)。验证 temporal context 改善
      是否跨架构泛化。
    expected_results:
      r1_32b_best_W: 10
      r1_32b_W10_bal_acc: 0.737
      r1_32b_W10_precision: 0.609
      r1_32b_W10_coverage: 0.70
      r1_32b_W10_precp_fpr: 0.189
      r1_32b_W10_lead: 10.79
      r1_32b_temporal_vs_static_delta_bal_acc: "+1.9pp"
      qwq_best_W: 5
      qwq_W5_bal_acc: 0.761
      qwq_W5_precision: 0.573
      qwq_W5_coverage: 0.737
      qwq_W5_precp_fpr: 0.180
      qwq_W5_lead: 20.07
      qwq_temporal_vs_static_delta_bal_acc: "+3.1pp"
      r1_32b_dimensionality_issue: "51200×W features for n=20; W≥5 overfitting"
      r1_32b_hb_pattern: "W=1 only 3/3 HB; W≥3 NS after Bonferroni"
      qwq_hb_pattern: "All W=1-15 pass HB (15/15)"
    result_rationale: >
      Temporal improvement 是四模型中最鲁棒的发现（text 和 HS 均受益），在 best 档中
      作为 universality 证据没有争议。32B 的特殊性在于维度灾难：R1-32B 5120-d × W 特征
      在 n=20 test traces 下，W≥5 时参数远超样本量，导致 temporal 增益被 overfitting 抵消。
      这不是 temporal context 失效，而是统计 power 不足。QwQ 的 n=19-20 同样小但因为
      层选对了、信号更强，所有 W 都通过 HB。R1-32B W=1 通过 3/3 HB 但仅 25% coverage
      是因为 W=1 feature 维度仅 5120（可控），但代价是 temporal context 最弱。
      Best 档 reviewer 接受这一 tradeoff 为诚实报告而非 fragility。
    tables:
      - name: "Table: Temporal Improvement Summary (32B models at corrected layers)"
        content: |
          | Model   | W   | BA    | Prec  | FPR   | Coverage | Lead  | HB    |
          |---------|-----|-------|-------|-------|----------|-------|-------|
          | R1-32B  | 1   | 0.826 | 0.603 | 0.235 | 25%      | +11.7 | 3/3 ✅ |
          | R1-32B  | 3   | 0.738 | 0.560 | 0.306 | 80%      | +11.4 | 0/3 ❌ |
          | R1-32B  | 10  | 0.737 | 0.609 | 0.234 | 70%      | +10.8 | 0/3 ❌ |
          | QwQ     | 1   | 0.730 | 0.544 | 0.228 | 79%      | +19.7 | 3/3 ✅ |
          | QwQ     | 3   | 0.745 | 0.565 | 0.214 | 74%      | +20.6 | 3/3 ✅ |
          | QwQ     | 5   | 0.761 | 0.573 | 0.217 | 74%      | +20.1 | 3/3 ✅ |
    figures_description:
      - "Fig: W vs bal_acc curve for 4 models. R1-8B/QwQ monotonic increase; OT-7B peaks at W=3; R1-32B flat/declining after W=1. Shows model-specific temporal saturation."
    analysis: >
      Temporal context 作为 Claim 1（primary universal finding）的核心证据在 best 档
      无争议。关键叙事点：text probes 在所有模型上受益于 temporal context（+3-12pp BA），
      HS probes 在 3/4 模型上受益（OT-7B 的 BA 在 W=3 饱和是可复现的模型特征，
      precision/FPR 持续改善）。R1-32B 的 W=1-only 显著性是 n=20 power limitation
      而非 temporal ineffectiveness，论文应明确区分。

  - name: "exp-003: Cross-model transfer"
    plan_id: "exp-003"
    description: >
      跨模型 zero-shot 迁移：Llama→Qwen, Qwen→Llama, Qwen-32B→Qwen-32B。
      使用 PCA 投影对齐维度。
    expected_results:
      r1_8b_to_r1_32b_acc: 0.522
      r1_8b_to_qwq_acc: 0.595
      r1_32b_to_qwq_acc: 0.550
      qwq_to_r1_32b_acc: 0.673
      r1_32b_to_r1_8b_acc: 0.583
      best_transfer_acc: 0.673
      baseline_in_domain_acc_range: "0.65-0.82"
      conclusion: "negative — all transfer at chance or near-chance"
    result_rationale: >
      Cross-transfer 完全失败在 best 档中是正面结果：它证明 safety representation 是
      model-specific geometric encoding，不存在 universal safety direction。这支撑了
      两个论点：(1) 每个模型需要独立 probe training（deployment implication）；
      (2) control task selectivity（7.5-18.5pp）不是 artifact——如果 safety signal
      是跨模型 universal 的，transfer 应该 work。PCA 投影 (4096→5120) 的失败说明
      safety information 的编码方式在不同架构/训练方法间根本不同，而非简单的维度
      旋转。Qwen-32B→Qwen-32B (QwQ→R1-32B: 0.673) 是最高的 transfer，因为同架构
      同规模，但仍远低于 in-domain。Best 档 reviewer 视此为 expected negative result，
      加强 model-specificity 叙事。
    tables:
      - name: "Table: Cross-Model Transfer Matrix (accuracy)"
        content: |
          | Train → Test  | R1-8B | R1-32B | QwQ   | OT-7B |
          |---------------|-------|--------|-------|-------|
          | R1-8B         | 0.823 | 0.522  | 0.595 | —     |
          | R1-32B        | 0.583 | 0.652  | 0.550 | —     |
          | QwQ           | —     | 0.673  | 0.717 | —     |
          | In-domain     | 0.823 | 0.652  | 0.717 | 0.688 |
    figures_description:
      - "Fig: Transfer accuracy heatmap, diagonal = in-domain baseline, off-diagonal = transfer. All off-diagonal cells near 0.5 (chance)."
    analysis: >
      Negative result 在 best 档中被 valued as community service。论文在 Discussion
      中用一段讨论 cross-transfer 失败的 implication：safety representation geometry
      is model-specific, ruling out universal safety probes. 这与 RepE direction
      probing 的 failure mode 一致——mean-difference direction 也是 model-specific
      且 generalizes poorly。

  - name: "exp-004: Lead time analysis across models"
    plan_id: "exp-004"
    description: >
      四模型 lead time 分布分析。确认 HS probe 的检测时机特性：
      HS 在 commitment point 附近检测，text 更早但 trigger-happy。
    expected_results:
      r1_8b_hs_lr_lead: -0.1
      r1_8b_text_lr_lead: +10.3
      r1_8b_text_fpr_note: "text lead inflated by 20.5% FPR (trigger-happy)"
      r1_8b_gru_lead_mean: "+4.5 ± 3.0"
      r1_8b_gru_worst_seed: "+0.9"
      ot_7b_hs_lead: 21.6
      ot_7b_text_lead: 45.5
      ot_7b_note: "absolute lead inflated by long traces (~80 sentences)"
      qwq_hs_lead_W3: -1.2 to +1.9
      qwq_text_lead_W3: 3.7 to 12.3
      qwq_caveat: "HS more accurate but detects LATER — practical tradeoff"
      r1_32b_hs_lead_W1: "+11.7 to +13.3"
      r1_32b_text_lead: "+3.7 to +9.0"
      r1_32b_positive: "HS lead excellent at W=1; best lead time of any model"
      cross_model_divergence: "R1-32B lead +13 (excellent) vs QwQ lead -1 (poor)"
    result_rationale: >
      Lead time profile 是 best 档叙事中 32B cross-model divergence 的关键证据。
      R1-32B 有 excellent lead time (+13 steps) 但 narrow coverage (W=1, 25%)；
      QwQ 有 robust significance (all W) 但 poor lead time (HS detects later than text)。
      这一 divergence 不削弱 paper——相反，它展示了 32B 模型在 safety commitment
      detection 中的 genuine complexity，reviewer 在 best 档将此视为 nuanced empirical
      finding。R1-8B 的 HS lead ≈ 0 是 balanced weight 训练的结果（HS 准确检测
      commitment point 本身而非预测它），只有 GRU 通过 sequence modeling 获得
      modest positive lead (+4.5)，这本身就是一个有意义的发现。OT-7B 的高 absolute
      lead 是 trace length artifact (~80 sentences vs ~30)，论文必须 normalize 或 caveat。
    tables:
      - name: "Table: Lead Time Profile Summary"
        content: |
          | Model   | HS LR Lead | Text Lead | GRU Lead  | Interpretation        |
          |---------|-----------|-----------|-----------|----------------------|
          | R1-8B   | ~0        | +10.3*    | +4.5±3.0  | HS=at CP, GRU modest |
          | OT-7B   | +21.6†    | +45.5†    | +33.6±4.8 | †inflated by length  |
          | QwQ-32B | -1 to +2  | +4 to +12 | +15.9     | HS late, text early  |
          | R1-32B  | +12-13    | +4 to +9  | +8.8      | HS early, best case  |
    figures_description:
      - "Fig: Lead time distribution violin plot per model (HS vs text). Shows R1-32B and QwQ diverge sharply."
    analysis: >
      Lead time 差异在 best 档中被 framed 为 deployment-relevant 实证发现，
      而非 weakness。论文 Discussion 建议：R1-32B 适合 early-warning 场景（高 lead
      但低 coverage），QwQ 适合 broad-monitoring 场景（high significance, all W）。
      这种 per-model deployment guidance 是实证研究的 legitimate contribution。

  - name: "exp-005: TrajGuard-style Mahalanobis baseline"
    plan_id: "exp-005"
    description: >
      在所有 4 模型上实施 Mahalanobis distance 检测器。使用 safe traces 估计协方差，
      计算每步 MD。测试 PCA 降维后的 discrimination 能力。
    expected_results:
      r1_8b_separation: 0.07
      ot_7b_separation: 0.03
      r1_32b_separation: 0.15
      qwq_32b_separation: 0.20
      max_separation: 0.20
      all_models_fail: true
      best_pca_config: "pca_64"
      r1_8b_k5_crossing_rate: 0.302
      failure_mode: "signal in minor PCA components, not principal directions"
      false_alarm_vs_tp: "FA rate ≥ TP rate at every threshold"
    result_rationale: >
      Mahalanobis 在所有 4 模型上 separation ≈ 0。这不是 implementation error，
      而是 fundamental failure mode：safety commitment signal 编码在 minor PCA
      components 中（Fisher discriminant ratio 从原始 17.9 降到 PCA-3D 的 0.93），
      而 MD 测量的是 principal direction 的偏差。在 best 档中，这个 comprehensive
      negative result 被视为 "community service"——它告诉社区 TrajGuard-style
      detection（依赖 MD 的 unsupervised 方法）在 reasoning model safety commitment
      上根本不适用。4 模型一致的失败模式（separation 0.03-0.20，FA ≥ TP at all
      thresholds）排除了 model-specific 偶然因素。Reviewer 在 best 档 values 这种
      系统性 negative evidence。
    tables:
      - name: "Table: Mahalanobis Discrimination Summary"
        content: |
          | Model   | Layer | PCA  | Safe MD | Post MD | Sep   | Verdict  |
          |---------|-------|------|---------|---------|-------|----------|
          | R1-8B   | L14   | 64   | 6.66    | 6.73    | 0.07  | Fail     |
          | OT-7B   | L16   | 64   | 7.68    | 7.71    | 0.03  | Fail     |
          | QwQ-32B | L60   | 16   | 3.22    | 3.42    | 0.20  | Fail     |
          | R1-32B  | L63   | 64   | 6.73    | 6.88    | 0.15  | Fail     |
    figures_description:
      - "Fig: MD distribution overlay (safe vs post-CP) per model. Distributions nearly identical, visually confirming zero discrimination."
    analysis: >
      Mahalanobis 作为 6 negative methods 之一，在 paper 中占 1-2 段。Best 档
      reviewer 关注的不是 MD 为什么失败（这在 PCA Fisher ratio 分析中已解释），
      而是它 comprehensively 失败的事实本身——排除了 unsupervised distance-based
      方法这一大类 approach。

  - name: "exp-006: Bootstrap CI + threshold-independent metrics"
    plan_id: "exp-006"
    description: >
      10,000 bootstrap resamples, Holm-Bonferroni step-down correction,
      4 models × 3 metrics = 12 tests。报告 AUROC, PR curves, FPR。
    expected_results:
      n_resamples: 10000
      holm_bonferroni_pass: "12/12"
      r1_8b_bal_acc_p: "<0.001"
      r1_8b_precision_p: "<0.001"
      r1_8b_fpr_p: "<0.001"
      ot_7b_all_3_p: "<0.001"
      qwq_bal_acc_p: "<0.001"
      qwq_precision_p: "<0.001"
      qwq_fpr_p: 0.0061
      r1_32b_bal_acc_p: "<0.001"
      r1_32b_precision_p: "<0.001"
      r1_32b_fpr_p: 0.0096
      marginal_tests: "R1-32B FPR (p=0.0096, threshold=0.05), QwQ FPR (p=0.0061, threshold=0.025)"
      precision_range: "+15.4 to +23.6pp"
      precision_consistency: "remarkably consistent across 4 models"
    result_rationale: >
      12/12 HB pass 是 best 档 soundness rating 4.0-4.5 的基础。在 biased layers
      下只有 5/12 pass；corrected layers 将全部 12 tests 翻转为 significant。
      这不是 p-hacking（先选层再做 multiple testing），因为 layer selection 基于
      独立的 metric sensitivity analysis（5 metrics consensus），evaluation 用的
      不同 test set。Precision advantage +15-24pp 跨 4 模型的一致性（std ≈ 3.5pp）
      是 best 档 reviewer 最看重的 robustness evidence——如果只有 1-2 模型显著，
      novelty rating 会降到 3.0。R1-32B FPR (p=0.0096) 和 QwQ FPR (p=0.0061)
      是最 marginal 的两个 test，但都 comfortably pass their respective HB thresholds
      (0.05 和 0.025)。10k resamples（vs 原始 1k）增加了 precision 但不改变结论，
      这本身证明了 statistical robustness。
    tables:
      - name: "Table: 12/12 Holm-Bonferroni Summary"
        content: |
          | Rank | Model   | Metric    | Delta     | p-value | Threshold | Pass |
          |------|---------|-----------|-----------|---------|-----------|------|
          | 1    | R1-8B   | precision | +22.4pp   | <0.001  | 0.0042    | ✅   |
          | 2    | OT-7B   | bal_acc   | +10.7pp   | <0.001  | 0.0045    | ✅   |
          | 3    | OT-7B   | precision | +21.9pp   | <0.001  | 0.0050    | ✅   |
          | 4    | OT-7B   | FPR       | -17.1pp   | <0.001  | 0.0056    | ✅   |
          | 5    | QwQ     | bal_acc   | +15.4pp   | <0.001  | 0.0063    | ✅   |
          | 6    | QwQ     | precision | +23.6pp   | <0.001  | 0.0071    | ✅   |
          | 7    | R1-32B  | bal_acc   | +18.7pp   | <0.001  | 0.0083    | ✅   |
          | 8    | R1-32B  | precision | +15.4pp   | <0.001  | 0.0100    | ✅   |
          | 9    | QwQ     | FPR       | -9.8pp    | 0.004   | 0.0125    | ✅   |
          | 10   | R1-8B   | bal_acc   | +8.2pp    | 0.005   | 0.0167    | ✅   |
          | 11   | R1-32B  | FPR       | -14.6pp   | 0.007   | 0.0250    | ✅   |
          | 12   | R1-8B   | FPR       | -7.4pp    | 0.044   | 0.0500    | ✅   |
    figures_description:
      - "Fig: Bootstrap delta distributions (12 panels), each with 95% CI band and null reference line. All 12 CIs exclude zero."
    analysis: >
      这是 paper 的 statistical backbone。Best 档 reviewer (soundness 4.0-4.5)
      会仔细检查 multiple testing procedure 的正确性。关键防御：(1) HB step-down
      是 conservative（比 Bonferroni 更 powerful 但仍控制 FWER）；(2) null-centered
      two-sided bootstrap 不依赖分布假设；(3) 10k resamples 确保 p-value 精度到
      3 位小数。

  - name: "exp-007: Window size ablation"
    plan_id: "exp-007"
    description: >
      W=1,3,5,10,15,20,25 on all 4 models at corrected layers。
      展示 precision-coverage tradeoff 和 diminishing returns。
    expected_results:
      r1_8b_best_bal_acc_W: 25
      r1_8b_precision_range: "0.693 (W=1) → 0.822 (W=25)"
      r1_8b_coverage_range: "0.721 (W=1) → 0.488 (W=25)"
      r1_8b_fpr_range: "0.097 (W=1) → 0.048 (W=25)"
      r1_32b_best_bal_acc_W: 10
      r1_32b_precision_at_W10: 0.609
      r1_32b_coverage_at_W10: 0.70
      qwq_best_bal_acc_W: 25
      qwq_precision_at_W5: 0.573
      ot_7b_best_W: 3
      ot_7b_W3_bal_acc: 0.688
      ot_7b_saturation: "bal_acc peaks W=3, precision/FPR continue improving"
      universal_finding: "coverage monotonically DECREASES with W across all 4 models"
      tradeoff: "higher W → higher precision, lower coverage, lower FPR"
    result_rationale: >
      Coverage 单调递减与 W 的关系在所有模型上一致，这是因为 larger W 创建了更 selective
      的特征空间——probe 需要更长时间的 consistent signal 才会触发 crossing，减少了
      false positives 同时也减少了 true positives（特别是短 post-CP segments）。
      这不是 "temporal context 有害"，而是一个 precision-sensitivity tradeoff。
      R1-8B 在 W=25 达到最高 bal_acc (0.810) 和 precision (0.822) 但 coverage
      降到 48.8%——论文报告 W=15 作为 reported setting 是合理的 tradeoff。
      OT-7B 的 bal_acc saturation at W=3 是因为 STILL training 创建了 shorter,
      more abrupt commitment transitions，larger W 包含了 non-informative pre-commitment
      context。Best 档 reviewer 接受 per-model W 选择（非 uniform W）因为论文
      透明报告了所有 W 的结果。
    tables:
      - name: "Table: Window Size × Model Ablation (bal_acc)"
        content: |
          | W  | R1-8B | OT-7B | QwQ-32B | R1-32B |
          |----|-------|-------|---------|--------|
          | 1  | 0.778 | 0.672 | 0.730   | 0.718  |
          | 3  | 0.790 | 0.688 | 0.745   | 0.725  |
          | 5  | 0.781 | 0.675 | 0.761   | 0.731  |
          | 10 | 0.793 | 0.660 | 0.747   | 0.737  |
          | 15 | 0.802 | 0.650 | 0.741   | 0.721  |
          | 25 | 0.810 | 0.635 | 0.762   | 0.703  |
    figures_description:
      - "Fig: 4-panel line chart (W vs metrics), 3 lines per panel (bal_acc, precision, coverage). Shows universal precision-coverage tradeoff."
    analysis: >
      Ablation 在 paper 中作为 appendix 完整表格 + main text 一段总结。
      关键 takeaway: W 选择是 deployment decision（precision vs coverage），
      不影响 HS > text 的 modality conclusion。

  - name: "exp-008: Layer selection ablation"
    plan_id: "exp-008"
    description: >
      4 models × 5 metrics 完整 layer selection sensitivity analysis。
      发现 crossing_rate bias 是主方法论贡献。
    expected_results:
      models_tested: 4
      metrics_tested: 5
      bias_pattern: "crossing_rate × bal_acc → shallow; threshold-dependent → deep; pure bal_acc → middle"
      qwq_biased_L2_precision: 0.525
      qwq_corrected_L60_precision: 0.578
      qwq_precision_gain: "+5.3pp"
      r1_32b_biased_L10_precision: 0.516
      r1_32b_corrected_L63_precision: 0.603
      r1_32b_precision_gain: "+8.7pp"
      loo_cv_dominant_layer_stability: "65-68% folds select same dominant layer"
      threshold_free_vs_dependent: "threshold-free (bal_acc, AUROC) → middle layers; threshold-dependent (precision, FPR) → deep layers"
      anti_circularity: "BA-layer analysis (16/16 HB) refutes metric circularity concern"
    result_rationale: >
      这是论文的 primary methodological contribution。Best 档核心假设 #1 直接关联：
      "Reviewers treat layer selection metric bias as a reproducible methodological
      finding (not 'you just picked the wrong hyperparameter')". 证据链：
      (1) bias 有 mechanistic 解释（浅层 compressed representation → noise-driven crossings）；
      (2) 5 metrics × 4 models 是系统性审计；(3) LOO-CV 65-68% stability 排除了
      validation set overfitting；(4) BA-layer analysis (16/16 HB pass) 证明 HS advantage
      在 ANY non-biased layer selection criterion 下都成立，refuting circularity。
      第二个发现——threshold-free vs threshold-dependent 的 middle vs deep 分歧——
      是独立于 crossing_rate bias 的 second dimension of researcher degrees of freedom，
      增加了方法论贡献的 depth。Best 档 novelty 3.5-4.0 很大程度源于此。
    tables:
      - name: "Table: Metric × Model → Layer Depth (%) + HS-Text Δ Precision"
        content: |
          | Metric            | R1-8B Depth | OT-7B Depth | QwQ Depth | R1-32B Depth |
          |-------------------|-------------|-------------|-----------|-------------|
          | BA × CR (biased)  | 0%          | 0%          | 3%        | 16%         |
          | Pure BA           | 39%         | 32%         | 47%       | 73%         |
          | Precision         | 52%         | 57%         | 94%       | 98%         |
          | Inverse FPR       | 52%         | 71%         | 94%       | 98%         |
          | Composite         | 52%         | 43%         | 94%       | 98%         |
    figures_description:
      - "Fig: Layer depth heatmap (5 metrics × 4 models), color gradient from shallow (red) to deep (blue). Clear visual: CR-composite row is uniformly red; threshold-dependent rows are blue at 32B."
    analysis: >
      This subsection in Method is the paper's marquee. Best 档 reviewer 理解
      这不是 hyperparameter tuning 的原因：(1) it's a reproducible bias affecting
      any researcher using crossing_rate; (2) the ablation is exhaustive (20 cells);
      (3) impact is dramatic (5/12 → 12/12 HB); (4) it generalizes a concern
      beyond this paper (any HS probe study using threshold-frequency metrics).

  - name: "exp-009: 16-label taxonomy supervision"
    plan_id: "exp-009"
    description: >
      使用 fine-grained 安全标签（Type 1/2/3/4）替代 binary commitment 训练 probe。
      测试更丰富的监督信号是否改善 coverage 和 timing。
    expected_results:
      r1_8b_16label_bal_acc: 0.82
      r1_8b_16label_coverage: 0.56
      r1_8b_binary_coverage: 0.51
      r1_8b_coverage_delta: "+5pp"
      r1_8b_precision_delta: "+1-3pp"
      ot_7b_16label_bal_acc: 0.70
      ot_7b_16label_coverage: 0.58
      ot_7b_binary_coverage: 0.53
      ot_7b_coverage_delta: "+5pp"
      32b_inconclusive: "n too small for 16-label with 4 classes"
      finding: "modest improvement, not load-bearing for paper claims"
    result_rationale: >
      16-label taxonomy 提供了更 granular 的 supervision——probe 可以区分 "safety reasoning
      declining" 和 "safety reasoning absent"，而非只有 binary crossing。这在 7-8B
      模型上产生 modest coverage improvement (+3-5pp)，因为 fine-grained labels
      让 probe 在 commitment 附近有更 nuanced 的 decision boundary。但改善幅度小于
      temporal windowing 的贡献，且 32B 模型因 n 太小（20-30 traces, 16 classes
      进一步稀释了 per-class 样本）几乎无法训练。在 best 档中，这个实验放 appendix
      作为 supplementary evidence，不影响主叙事。Reviewer 看到它被 attempted 且
      honestly reported 就够了，不期望它成为 major finding。Best 档假设 "comprehensive
      negative results are valued" 适用于此——即使 16-label 没有显著改善，它排除了
      "you're underusing available supervision" 这一批评。
    tables:
      - name: "Table: Binary vs 16-Label Supervision (7-8B models)"
        content: |
          | Model  | Supervision | BA    | Prec  | Coverage | Lead  |
          |--------|-------------|-------|-------|----------|-------|
          | R1-8B  | binary      | 0.802 | 0.777 | 0.512    | -0.1  |
          | R1-8B  | 16-label    | 0.820 | 0.795 | 0.558    | +0.8  |
          | OT-7B  | binary      | 0.688 | 0.466 | 0.532    | 21.6  |
          | OT-7B  | 16-label    | 0.700 | 0.485 | 0.580    | 22.3  |
    figures_description:
      - "Fig: Paired bar chart (binary vs 16-label) for coverage and precision. Modest +3-5pp coverage gains."
    analysis: >
      P1 实验，放 appendix。Best 档 reviewer 不会要求 16-label 作为 main result，
      但 appreciation 它被 attempted。Coverage 的 modest gain 说明 binary supervision
      已接近 ceiling——temporal windowing 是更有效的改善途径。

  - name: "exp-010: Oracle decomposition"
    plan_id: "exp-010"
    description: >
      分析 oracle（使用 ground-truth label sequence）为何能实现 +31 step lead time
      而 probes 不能。Decompose oracle advantage into label sequence pattern vs
      hidden state content。
    expected_results:
      oracle_K5_lead: "+31 steps"
      oracle_K5_detection_rate: "100%"
      probe_best_lead: "+4.5 (GRU)"
      oracle_advantage_source: "label sequence pattern — oracle sees 5+ consecutive post-CP labels before probes stabilize"
      gap_explanation: >
        Oracle exploits K-consecutive pattern in ground-truth labels (pure sequence),
        while probes must INFER label from noisy HS features. The 31-step gap
        comes from label noise: probe confidence fluctuates around CP, requiring
        temporal smoothing (W) to stabilize, whereas oracle has clean binary signal.
      implication: "ceiling on probe lead time is limited by representation noise, not information absence"
      pre_cp_safety_streaks: "mean 14.6 consecutive safe labels before CP"
    result_rationale: >
      Oracle +31 step lead vs probe +4.5 step lead 的 gap 解释是 Discussion section
      的关键内容。Hidden states DO encode current safety state（static probe 80% BA），
      但 POORLY predict future trajectory（probe 看到 t 时刻的 HS，只能判断 t 时刻
      的 safety state，不能预测 t+5 是否会 commit）。Oracle 利用的是 label sequence
      中 K-consecutive pattern——一旦连续 5 个 post-CP label 出现，oracle 确信
      commitment 已发生。Probe 无法复制这一优势，因为：(1) probe confidence 在 CP
      附近波动（pre-CP 也有 false crossings）；(2) temporal smoothing (W) 帮助但
      引入了 latency；(3) GRU 的 +4.5 step lead 是 sequence modeling 的 modest
      contribution（学会了 "confidence 持续上升 = commitment"的 pattern）。
      Best 档 reviewer 视此分析为对 fundamental limitation 的 honest investigation。
    tables:
      - name: "Table: Oracle vs Best Probe Performance (R1-8B)"
        content: |
          | Method         | Detection | Lead  | Mechanism                    |
          |----------------|-----------|-------|------------------------------|
          | Oracle K=5     | 100%      | +31   | Clean label sequence pattern |
          | GRU multi-7L   | 76.7%     | +4.5  | Learned confidence dynamics  |
          | HS Temporal LR | 76.7%     | -0.1  | Snapshot classification      |
          | Text Temporal  | 65.1%     | +10.3 | Text-level (trigger-happy)   |
    figures_description:
      - "Fig: Lead time CDF — oracle vs GRU vs HS LR vs text. Oracle curve far left (early detection), probes clustered near zero."
    analysis: >
      Discussion section 核心段落。Best 档 reviewer 会问 "can you close the gap?"
      答案是 honest "not with current approaches"——这是一个 fundamental limitation
      of snapshot-based HS monitoring。论文建议 future work 方向：(1) predictive
      probes (trained to predict FUTURE safety state); (2) attention pattern analysis;
      (3) multi-step trajectory modeling beyond GRU。

  - name: "exp-011: OpenThinker-7B (4th model, completing 2×2 matrix)"
    plan_id: "exp-011"
    description: >
      完成 2×2 architecture×scale matrix：Llama-8B (R1-8B), Qwen-7B (OT-7B),
      Qwen-32B (QwQ), Qwen-32B (R1-32B)。OT-7B 填充 Qwen-7B slot。
    expected_results:
      n_traces: 228
      best_layer: 16
      best_layer_depth_pct: 57.1
      hs_best_W: 3
      hs_best_bal_acc: 0.688
      hs_best_precision: 0.466
      hs_best_fpr: 0.100
      hs_best_coverage: 0.532
      text_best_W: 25
      text_best_bal_acc: 0.614
      text_best_precision: 0.329
      bootstrap_hs_text_delta_ba: "+10.7pp (p<0.001)"
      bootstrap_hs_text_delta_prec: "+21.9pp (p<0.001)"
      bootstrap_hs_text_delta_fpr: "-17.1pp (p<0.001)"
      holm_bonferroni: "3/3 pass"
      selectivity: "18.3pp (highest across all 4 models)"
      gru_multi_bal_acc: 0.746
      gru_multi_coverage: 0.645
      gru_multi_lead: 33.6
      gru_multi_fpr: 0.274
      ot7b_hs_temporal_saturation: "BA peaks at W=3 (0.688), declines at W≥5; precision/FPR continue improving"
    result_rationale: >
      OT-7B 是 4 模型中 "cleanest single-model evidence"：3/3 HB pass with large
      effect sizes, highest selectivity (18.3pp), 5/5 seed robustness, 和最大的
      residualized gap (+6.9pp after position removal)。它作为 Qwen-7B (STILL-trained)
      slot 完成 2×2 matrix 的作用是关键的：它证明 HS advantage 不是 Llama-specific，
      也不是 R1-distillation-specific。STILL training 创建了不同于 R1-distillation
      的 safety reasoning pattern（更短、更 abrupt 的 commitment），但 HS 优势依然
      显著。OT-7B 的 W=3 temporal saturation 是 genuine model characteristic（两个
      layer 都确认），不影响 BA 以外的 metrics。Best 档假设 #2 直接相关："4 models
      × 2 architectures × 2 scales is accepted as sufficient breadth"。228 traces
      是最大数据集（vs R1-8B 209, QwQ 95, R1-32B 100），给了最高统计 power。
    tables:
      - name: "Table: OT-7B Full Pipeline Summary"
        content: |
          | Method           | BA    | Prec  | FPR   | Cov   | Lead  |
          |------------------|-------|-------|-------|-------|-------|
          | HS Static L16    | 0.672 | 0.357 | 0.188 | —     | —     |
          | HS Temp W=3 L16  | 0.688 | 0.466 | 0.100 | 0.532 | 21.6  |
          | Text Temp W=25   | 0.614 | 0.329 | 0.161 | 0.660 | 45.5  |
          | GRU Multi L13-19 | 0.746 | —     | 0.274 | 0.645 | 33.6  |
    figures_description:
      - "Fig: OT-7B layer landscape — bal_acc vs layer depth, showing L16 as clear optimum with L0 (biased) marked."
    analysis: >
      OT-7B 数据在 paper 中出现在每张 summary table 中。它的 cleanness 为
      HS advantage 叙事提供了 anchor point——即使 32B 有 caveats，7-8B 证据
      是 unambiguous。

  - name: "exp-012: GRU/Attention probe on 32B models"
    plan_id: "exp-012"
    description: >
      在 32B 模型 corrected layers 上训练 GRU probe。验证 "LR sufficient, GRU
      adds modest improvement" 的结论是否跨 scale 成立。
    expected_results:
      qwq_gru_single_bal_acc: 0.724
      qwq_gru_multi_bal_acc: 0.710
      qwq_gru_lead: 15.9
      qwq_gru_fpr: 0.289
      r1_32b_gru_single_bal_acc: 0.675
      r1_32b_gru_multi_bal_acc: 0.655
      r1_32b_gru_lead: 9.1
      r1_32b_gru_fpr: 0.135
      gru_vs_lr_qwq: "-3.7pp BA (LR W=5: 0.761 > GRU single: 0.724)"
      gru_vs_lr_r1_32b: "-6.2pp BA (LR W=10: 0.737 > GRU single: 0.675)"
      gru_advantage: "longer lead time than LR, at cost of higher FPR"
      finding: "GRU does NOT outperform LR on 32B; strengthens 'linear probes sufficient' narrative"
      note: "results at OLD biased layers; corrected-layer GRU may differ"
    result_rationale: >
      GRU 在 32B 上不优于 LR 的原因是相同的 dimensionality constraint：5120-d HS
      输入 × sequence length 对于 n=20-30 test traces 来说参数过多。GRU 的优势
      在于 sequence modeling（捕捉 confidence 随时间的动态），但当 base signal (HS)
      足够 linearly separable 时（如 4 模型 precision +15-24pp 所示），nonlinear
      sequence modeling 无法提供额外信息。这与 MLP probe 的 negative result 一致：
      3/4 models MLP worse than LR。在 best 档中，"linear probes sufficient"是一个
      important practical finding——deployment 不需要 complex model，simple LR + 
      temporal window 就够了。这降低了 method 的 adoption barrier。GRU 在 7-8B 上
      的 modest advantage (+4.5 lead) 是 genuine 但 small，论文报告为 "GRU achieves
      modest positive lead where LR detects at CP"。
    tables:
      - name: "Table: GRU vs LR Comparison (all models)"
        content: |
          | Model   | LR Best BA | GRU BA   | Δ       | GRU Lead | LR Lead |
          |---------|-----------|----------|---------|----------|---------|
          | R1-8B   | 0.802     | 0.809    | +0.7pp  | +4.5     | -0.1    |
          | OT-7B   | 0.688     | 0.746    | +5.8pp  | +33.6    | +21.6   |
          | QwQ-32B | 0.761     | 0.724    | -3.7pp  | +15.9    | ~0      |
          | R1-32B  | 0.737     | 0.675    | -6.2pp  | +9.1     | +12.9   |
    figures_description:
      - "Fig: BA scatter (LR vs GRU) per model with identity line. 7-8B points above line, 32B below."
    analysis: >
      GRU 数据支持论文的 practical message："use simple LR + temporal window"。
      32B GRU at biased layers 需要 re-evaluation at corrected layers 但论文
      可以 caveat this as future work。

  - name: "exp-013: Text-based baseline (sentence-BERT)"
    plan_id: "exp-013"
    description: >
      all-MiniLM-L6-v2 embeddings + temporal LR (W=15) on CoT text。
      验证 HS monitoring 相比 cheap text monitoring 的 unique value。
    expected_results:
      r1_8b_text_static_acc: 0.661
      r1_8b_text_static_auroc: 0.738
      r1_8b_text_temporal_w15_acc: 0.678
      r1_8b_text_temporal_w15_auroc: 0.759
      r1_8b_hs_advantage_over_text: "15-18pp accuracy"
      r1_8b_text_safe_fpr: 0.502
      r1_8b_text_precp_fpr: 0.356
      r1_8b_hs_precp_fpr: 0.162
      hs_vs_text_fpr_delta: "-19.4pp"
      text_coverage: 0.651
      text_lead: 11.5
      hs_lead: 4.9
      text_precision: 0.487
      hs_precision: 0.583
      key_finding: "HS adds unique value: +15pp accuracy, +10pp precision, -19pp FPR over text baseline"
      text_not_useless: "text temporal achieves 67.8% acc — non-trivial but significantly below HS"
    result_rationale: >
      Text baseline 是 best 档中 paper motivation 的关键防线。如果 text 能 match
      HS performance，整个 "hidden-state monitoring" 的 raison d'être 就消失了。
      实际结果：text 在 accuracy、precision、FPR 上全面落后 HS 15-19pp，但 text 不是
      zero——它达到了 67.8% accuracy，说明 CoT 文本确实包含 safety 信息（符合直觉：
      safety reasoning 在文本中可见）。HS 的优势在于 sub-textual signal：hidden states
      编码了模型"实际在想什么"而非"写出来了什么"，这在 safety commitment detection
      中提供了 additional discriminative power。Text 的高 lead time (+11.5 vs HS +4.9)
      是 artifact of trigger-happy detection（text FPR 20.5% vs HS 8.8%）——text
      更早触发是因为它更容易 false alarm。Best 档 reviewer 在看到 comprehensive
      HS vs text comparison 后接受 "HS adds unique value beyond text monitoring"。
    tables:
      - name: "Table: HS vs Text Baseline (R1-8B)"
        content: |
          | Method         | BA    | Prec  | FPR-pre | FPR-safe | Lead  | Cov   |
          |----------------|-------|-------|---------|----------|-------|-------|
          | HS Static      | 0.768 | 0.622 | 0.162   | 0.390    | +3.0  | 0.605 |
          | HS Temporal W15| 0.726 | 0.583 | 0.160   | 0.392    | +4.9  | 0.651 |
          | Text Static    | 0.661 | 0.448 | 0.356   | 0.502    | +4.3  | 0.605 |
          | Text Temp W15  | 0.678 | 0.487 | 0.272   | 0.385    | +11.5 | 0.651 |
          | GRU            | 0.816 | 0.648 | 0.188   | 0.521    | +5.3  | 0.744 |
    figures_description:
      - "Fig: Precision-recall curves (HS vs text, 4 models). HS curve consistently above text curve, especially at low-FPR operating points."
    analysis: >
      Text baseline 在 paper 中作为 Table 的一行存在，不需要 dedicated subsection。
      Key message：HS provides 15-19pp advantage over text，这是 non-trivial 且
      statistically significant (12/12 HB)，justifying the added complexity of
      HS extraction。

  - name: "exp-014: BOCPD/CUSUM change-point detection"
    plan_id: "exp-014"
    description: >
      Adams & MacKay 2007 BOCPD + CUSUM on probe score sequences。
      测试能否通过检测 distributional shift 获得 positive lead time。
    expected_results:
      r1_8b_bocpd_lambda10_detection: 0.93
      r1_8b_bocpd_lambda10_lead: 3.45
      r1_8b_fcp_baseline_lead: 4.89
      r1_8b_bocpd_vs_fcp: "higher detection (93% vs 65%) but lower mean lead (3.45 vs 4.89)"
      ot_7b_bocpd_all_lambda: "0% detection — probe scores too spiky"
      r1_32b_bocpd: "0% detection"
      qwq_bocpd: "0% detection"
      cusum_verdict: "universally worse than simple threshold"
      cross_model_bocpd: "only R1-8B works (93%); 3/4 models 0%"
      finding: "BOCPD/CUSUM fail to improve over simple thresholds on 3/4 models; R1-8B exception due to gradual commitment pattern"
    result_rationale: >
      BOCPD 在 3/4 模型上 0% detection 的原因是 commitment dynamics 的 model-specificity：
      R1-8B 有 gradual commitment transition（probe confidence 缓慢上升），BOCPD 的
      Gaussian changepoint model 能捕捉这种 distributional shift。但 OT-7B/R1-32B/QwQ
      有 abrupt commitment（probe score 在 1-2 steps 内从 0 跳到 1），BOCPD 的 Gaussian
      model 无法 adapt 到这种 spike pattern。CUSUM 更简单但同样依赖 gradual shift
      假设。这个 negative result 在 best 档中有双重价值：(1) 排除了 "just use BOCPD"
      这一 obvious baseline；(2) 揭示了 commitment dynamics 的 model-specificity——
      同一方法在不同模型上表现截然不同，further supporting 论文 "one-size-fits-all
      detection doesn't work" 的 message。Best 档假设 #4 "comprehensive negative results
      valued as community service" 直接适用。
    tables:
      - name: "Table: BOCPD/CUSUM Cross-Model Summary"
        content: |
          | Model   | BOCPD Det | BOCPD Lead | CUSUM Det | FCP Lead | Winner     |
          |---------|----------|-----------|----------|---------|-----------|
          | R1-8B   | 93%      | +3.5      | 65.1%    | +4.9    | FCP (lead) |
          | OT-7B   | 0%       | —         | 70.2%    | +7.5    | FCP        |
          | QwQ-32B | 0%       | —         | 73.7%    | +9.4    | FCP        |
          | R1-32B  | 0%       | —         | 85%      | +2.6    | FCP        |
    figures_description:
      - "Fig: Probe score time series + BOCPD run length posterior for one R1-8B trace (works) vs one OT-7B trace (fails). Illustrates gradual vs abrupt commitment."
    analysis: >
      BOCPD/CUSUM 是 6 negative methods 的第二组。论文 1 段总结：
      "Advanced change-point methods fail because safety commitment dynamics
      are model-specific; BOCPD's Gaussian assumption is violated by abrupt
      transitions in 3/4 models."

  - name: "exp-015: False positive analysis on safe traces"
    plan_id: "exp-015"
    description: >
      所有 probe 方法在 safe traces (final_judgment=0.5) 上的 FPR。
      Essential for deployment utility claims。
    expected_results:
      r1_8b_hs_static_safe_fpr: 0.390
      r1_8b_text_static_safe_fpr: 0.502
      r1_8b_hs_temporal_safe_fpr: 0.392
      r1_8b_gru_safe_fpr: 0.521
      ot_7b_hs_static_safe_fpr: 0.111
      ot_7b_text_static_safe_fpr: 0.302
      qwq_hs_safe_fpr: 0.475
      qwq_text_safe_fpr: 0.500
      r1_32b_hs_safe_fpr: 0.239
      r1_32b_text_safe_fpr: 0.310
      overall_safe_fpr_range: "11.1% - 62%"
      acknowledged_limitation: "safe FPR 39-62% for most model-method combos; OT-7B exception at 11.1%"
      hs_vs_text_fpr: "HS lower than text in 3/4 models (exception: QwQ)"
    result_rationale: >
      High safe FPR (39-62%) 是 best 档 acknowledged limitation。Best 档核心假设 #6：
      "High safe FPR (39-62%) is acceptable as acknowledged limitation for a
      detection-evaluation paper." 这里的关键 framing：本文不声称 ready-for-deployment
      detector，而是 "systematic evaluation revealing what works and what doesn't
      for this new threat model"。Safe FPR 高说明所有方法（包括 HS temporal）都还
      不够 mature 用于 production intervention——但这正是 empirical study 的 value：
      建立 baseline 并量化 gap。OT-7B 的异常低 safe FPR (11.1%) 是因为 STILL training
      创建了 cleaner separation of safe vs unsafe traces in HS space。QwQ 的 HS safe
      FPR (47.5%) > text safe FPR (50.0%) 是 caveat——在 QwQ 上 HS 并不总是 better
      than text on every metric。Best 档 reviewer 接受高 safe FPR 因为论文
      transparently acknowledges 它并且 frames contribution 为 evaluation study 而非
      deployable system。
    tables:
      - name: "Table: Safe Trace FPR Summary"
        content: |
          | Model   | HS Static | HS Temp | Text Static | Text Temp | GRU   |
          |---------|----------|---------|-------------|-----------|-------|
          | R1-8B   | 39.0%    | 39.2%   | 50.2%       | 38.5%     | 52.1% |
          | OT-7B   | 11.1%    | 17.5%   | 30.2%       | 46.0%     | —     |
          | QwQ-32B | 50.0%    | 45.0%   | 32.5%       | 42.5%     | —     |
          | R1-32B  | 23.9%    | 23.9%   | 31.0%       | 31.0%     | —     |
    figures_description:
      - "Fig: FPR bar chart grouped by model, bars colored by method. Shows HS generally lower than text (except QwQ) but all methods have non-trivial safe FPR."
    analysis: >
      Limitations section 明确列出 high safe FPR 作为 top limitation。
      论文 framing："These results establish baselines for future improvement
      rather than production-ready thresholds." Best 档 reviewer 不会因为高 FPR
      reject，因为这是 evaluation paper 而非 system paper。

  - name: "ensemble_cv_7b: CV-validated multi-metric ensemble layer selection"
    plan_id: "what_if/ensemble_cv_7b"
    description: >
      5-fold CV validation of multi-metric ensemble layer selection on 7-8B models。
      验证 ensemble 在 cross-validation 下是否消除 metric-induced bias。
    expected_results:
      r1_8b_ensemble_cv_delta_prec_mean: 0.174
      r1_8b_ensemble_cv_delta_prec_std: 0.026
      r1_8b_hs_better_folds: "5/5"
      ot_7b_ensemble_cv_delta_prec_mean: 0.164
      ot_7b_ensemble_cv_delta_prec_std: 0.033
      ot_7b_hs_better_folds: "5/5"
      total_hs_better_folds: "10/10"
      ensemble_prec_vs_best_single: "ensemble ≈ best single metric (never worse)"
      ensemble_vs_text_all_significant: true
      ensemble_vs_text_p_max: 0.002
      impact_on_acceptance: "0-5% (cosmetic, not load-bearing)"
    result_rationale: >
      Ensemble CV 在 best 档中的 impact 接近 zero (0-5%)。原因：paper 的 acceptance
      已经由 12/12 HB, position mediation 3/4, 5-seed robustness, 16/16 BA-layer
      analysis 这些 evidence package 支撑。Ensemble CV 做的是 "validate that multi-metric
      consensus layer selection is stable under CV"——但 LOO-CV stability (65-68%)
      已经回答了这个问题。Ensemble 结果 10/10 folds HS better than text 是 consistent
      但 unsurprising。Best 档 reviewer 不会要求 "please add CV-validated ensemble"
      作为 acceptance condition，因为 individual metric analysis 已经足够 rigorous。
      Ensemble 放 appendix 作为 supplementary validation，不进入 main text contribution
      claims。核心假设 "ensemble_cv_impact_on_acceptance: [0.0, 0.05]" 直接适用。
    tables:
      - name: "Table: Ensemble CV Results (Appendix)"
        content: |
          | Model  | Metric        | Fold 1 | Fold 2 | Fold 3 | Fold 4 | Fold 5 | Mean±Std       |
          |--------|---------------|--------|--------|--------|--------|--------|---------------|
          | R1-8B  | ΔPrecision    | +0.19  | +0.16  | +0.18  | +0.15  | +0.19  | +0.174±0.026  |
          | R1-8B  | HS>Text?      | ✅      | ✅      | ✅      | ✅      | ✅      | 5/5           |
          | OT-7B  | ΔPrecision    | +0.20  | +0.13  | +0.17  | +0.16  | +0.16  | +0.164±0.033  |
          | OT-7B  | HS>Text?      | ✅      | ✅      | ✅      | ✅      | ✅      | 5/5           |
    figures_description:
      - "Fig (Appendix): CV fold stability — ΔPrecision across 5 folds, error bars. All folds positive, low variance."
    analysis: >
      Appendix-only content。Best 档 reviewer 如果 notice 它会 appreciate thoroughness
      但不会将其列入 strengths/weaknesses。对 acceptance probability 的 marginal
      contribution ≤5%。论文 space budget：1/4 page in appendix max。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0d5fa04e-6fda-4d49-90d7-a2bb57dd8a0e",
  "isSidechain": false,
  "requestId": "req_011CbGRKQoKmeKU4P4NmXDfh",
  "type": "assistant",
  "uuid": "c7c54007-464f-4fed-8008-8dbf2d3be04b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TyFkpTyNFGj9scg945YzC9",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8224,
      "cache_read_input_tokens": 51966,
      "output_tokens": 20293,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8224,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 20293,
          "cache_read_input_tokens": 51966,
          "cache_creation_input_tokens": 8224,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8224
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 19_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer se…",
  "leafUuid": "c7c54007-464f-4fed-8008-8dbf2d3be04b",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "ai-title",
  "aiTitle": "Layer selection sensitivity in safety commitment detection",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer se…",
  "leafUuid": "c7c54007-464f-4fed-8008-8dbf2d3be04b",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Layer selection sensitivity in safety commitment detection",
  "sessionId": "af67fca6-bfdd-4586-bb65-252f2dd87fb2"
}
```

---
