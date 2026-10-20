# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-1/edabc97e-fd03-48b3-82cf-935ea08bdb99.jsonl`
- **Structured JSON:** [`5bd07a4cfacb8af18986.json`](../../sessions/5b/5bd07a4cfacb8af18986.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:22:52.406Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:22:52.406Z",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: contrastive_trace_safety\nvenue: emnlp-2026\nfocus: Evaluate whether adding CV-validated ensemble results (currently p≤0.002 without CV) meaningfully improves paper acceptance probability at EMNLP 2026. Key question: does upgrading ensemble from 'preliminary' to 'CV-validated' move the needle from Findings to Main, or is it marginal? Also assess current paper state post-R30 fixes (commit 322b668) — are there any OTHER low-cost improvements the dream reviewers would prioritize?\n\n## paper_framing.md\n\n# Paper Framing — contrastive_trace_safety\n\n## Target Venue\n- Primary: EMNLP 2026 Main (LLM Security Track)\n- Deadline: ARR submission May 25, 2026\n\n## Core Claims (D031: layer selection as primary contribution, 4 models)\n\n**Contribution structure (D031)**:\n- **Primary (methodological)**: Layer selection metric sensitivity — biased metrics reverse conclusions\n- **Secondary (empirical)**: HS advantage at correct layers, qualified by scale; temporal improvement universal\n- **Tertiary (negative results)**: 6 alternative methods fail, establishing what doesn't work\n\n1. **Temporal context universally improves probe accuracy across both modalities** (D014 + D023 nuanced) — Temporal context is the most robust improvement across all 4 models and both modalities. Text probes benefit consistently from larger windows across all models. HS probes benefit in 3/4 models; OT-7B HS peaks at W=3 and declines at larger W (confirmed on both layer 0 and layer 16).\n\n   **HS temporal gains** (W=1→best, 3 original models): accuracy +3pp (77.8%→81.0%), precision +13pp (69.3%→82.2%), FPR halved (9.65%→4.83%).\n   **OT-7B HS temporal** (layer 16): bal_acc peaks at W=3 (68.8%), declines to 65.9% at W=25 (-2.9pp). BUT precision and FPR continue improving (prec 42.8%→49.4%, FPR 12.0%→7.5%). Temporal saturation is bal_acc-specific; larger W trades bal_acc for better precision/FPR. Confirmed on both layer 0 and layer 16 — genuine OT-7B characteristic.\n   **Text temporal gains** (all 4 models, W=1→best): universally +3-12pp bal_acc, +8-23pp precision, FPR reduced.\n\n   **IMPORTANT: coverage direction depends on detection criterion K.** K=1 (single crossing): coverage DECREASES with W. K=5 (consecutive crossings): coverage may INCREASE with W. Claim 1 is about accuracy/precision improvement, NOT coverage.\n\n   The core insight: \"Temporal context universally improves text probes across all 4 models. For HS probes, 3/4 models benefit from larger temporal windows, while OT-7B shows early saturation (W=3 peak).\"\n\n2. **HS probes outperform text probes at correctly selected layers, with strong evidence at 7-8B and model-specific patterns at 32B** (D031: qualified from D030 \"universal\") —\n\n   **KEY FINDING (D029)**: The apparent \"scale-dependent\" HS advantage (significant at 7-8B, absent at 32B) was an artifact of the layer selection metric `bal_acc × crossing_rate`, which systematically selects shallow layers for 32B models. At correctly selected deep layers, HS outperforms text on all 4 models, but the NATURE of the advantage differs by scale.\n\n   **Layer selection metric bias (D028, refined D036)**: `bal_acc × crossing_rate` selects shallow layers because shallow layers have higher crossing rates (more trigger-happy probes). 3/4 non-biased threshold-dependent metrics (precision, pre_cp_fpr, composite) converge on deep layers; pure bal_acc (threshold-free) selects middle layers (L30/L47). Deployment-relevant metric consensus selects L60/L63 for 32B models.\n\n   **7-8B models: HS significantly outperforms text (2/2 models) — UNCHANGED**\n\n   **R1-8B (Llama-8B, R1-distilled, n=43):**\n   - Precision: 69.7% vs 47.2% (+22.4pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Accuracy: 81.3% vs 72.9% (+8.2pp, p=0.005, **Holm-Bonferroni ✅**)\n   - Pre-CP FPR: 14.8% vs 22.2% (-7.4pp, p=0.044, **Holm-Bonferroni ✅** — rank 12/12, threshold=0.0500)\n\n   **OT-7B (Qwen-7B, STILL-trained, n=47, layer 16, matched W=3) — D026 M001 corrected:**\n   - Bal Acc: 68.8% vs 58.1% (+10.7pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Precision: 46.6% vs 24.7% (+21.9pp, p<0.001, **Holm-Bonferroni ✅**)\n   - Pre-CP FPR: 10.0% vs 27.1% (-17.1pp, p<0.001, **Holm-Bonferroni ✅**)\n   - **3/3 metrics significant — OT-7B cleanest single-model evidence**\n\n   **32B models: HS outperforms text at CORRECTED LAYERS but with model-specific caveats (D029+D031)**\n\n   **QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 corrected from L2):**\n   - Bal Acc: +11-22pp across all 15 window sizes, all p<0.005 (bootstrap, null-centered)\n   - 15/15 W values show significant HS advantage\n   - **CRITICAL CAVEAT (D031)**: HS lead time NEGATIVE (-1.2 to 1.9 steps vs text 3.7-12.3). HS is \"more accurate but detects later.\" Position baseline bal_acc=0.746 > HS=0.740. In safety deployment, detecting 8-12 steps earlier may outweigh higher accuracy.\n   - W=3: bal_acc +15.4pp, precision +23.6pp, FPR -9.8pp — **3/3 Holm-Bonferroni ✅**\n\n   **R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 corrected from L10):**\n   - W=1: bal_acc +18.7pp (0.826 vs 0.639), p=0.000; precision +15.4pp (0.603 vs 0.448), p=0.000; FPR -14.6pp (0.235 vs 0.380), p=0.007 — **3/3 Bonferroni ✅**\n   - W=3: bal_acc +11.2pp p=0.020, precision p=0.032, FPR p=0.077 — **0/3 Bonferroni** (v2 null-centered)\n   - W=5-15: all NS\n   - **CRITICAL CAVEAT (D031)**: Only W=1 passes Bonferroni, coverage=25% (5/20 traces). Evidence statistically narrow.\n   - **POSITIVE**: Lead time +11.7-13.3 steps (excellent early warning). HS >> Position (+14.2pp).\n   - **NOTE**: L10 vs L63 at W=10: L10=0.795 vs L63=0.754 — L10 slightly better. \"Scheme B选错层\" narrative weaker for R1-32B.\n   - ✅ P-VALUE UNIFIED: null-centered two-sided, consistent with QwQ.\n\n   **32B cross-model divergence (D031 key finding for Discussion):**\n   | Dimension | R1-32B L63 | QwQ L60 |\n   |-----------|-----------|---------|\n   | Bonferroni | W=1 only (3/3) | All 15 W (3/3) |\n   | Lead time | +11.7 to +13.3 (excellent) | -1.2 to +1.9 (poor) |\n   | HS vs Position | HS >> Pos (+14.2pp) | HS < Pos (-0.6pp) |\n   | Coverage (W=1) | 25% | 74% |\n   Paper MUST discuss this divergence per-model, not unify into single narrative.\n\n   **OLD 32B results at BIASED layers (L2/L10) — RETRACTED as metric artifact:**\n   - R1-32B L10: precision +9.4pp (p=0.064), accuracy +6.2pp (p=0.13)\n   - QwQ-32B L2: precision +5.8pp (p=0.35), accuracy +0.9pp (p=0.83)\n   - These non-significant results were caused by the biased `bal_acc × crossing_rate` metric selecting layers where HS signal is weak.\n\n   **Holm-Bonferroni COMPLETE (D032): 12/12 ALL PASS**\n   Previously 5/12 (biased layers). With corrected layers: **12/12** step-down pass (α=0.05).\n\n   | Rank | Model | Metric | p-value | Threshold | Pass |\n   |------|-------|--------|---------|-----------|------|\n   | 1 | R1-8B | precision | <0.001 | 0.0042 | ✅ |\n   | 2 | OT-7B | bal_acc | <0.001 | 0.0045 | ✅ |\n   | 3 | OT-7B | precision | <0.001 | 0.0050 | ✅ |\n   | 4 | OT-7B | FPR | <0.001 | 0.0056 | ✅ |\n   | 5 | QwQ | bal_acc | <0.001 | 0.0063 | ✅ |\n   | 6 | QwQ | precision | <0.001 | 0.0071 | ✅ |\n   | 7 | R1-32B | bal_acc | <0.001 | 0.0083 | ✅ |\n   | 8 | R1-32B | precision | <0.001 | 0.0100 | ✅ |\n   | 9 | QwQ | FPR | 0.004 | 0.0125 | ✅ |\n   | 10 | R1-8B | bal_acc | 0.005 | 0.0167 | ✅ |\n   | 11 | R1-32B | FPR | 0.007 | 0.0250 | ✅ |\n   | 12 | R1-8B | FPR | 0.044 | 0.0500 | ✅ |\n\n   **Caveats**: Different W per model (R1-8B W=15, OT-7B/QwQ W=3, R1-32B W=1). Tests measure \"HS > text at each model's best setting,\" not \"at uniform W.\" R1-32B W=1 has 25% coverage. Paper must state these conditions.\n\n   **FPR dual reporting**: Step-level (r1-8b: HS 8.8%, text 20.5%) vs trace-level (HS 14.8%, text 22.2%). Both reported.\n\n   **FPR reversal RESOLVED (D026)**: OT-7B HS FPR@L16 (10.0%) < Text FPR at ANY window (16.1%). HS dominates on FPR at 7-8B.\n\n   **Effect size consistency**: Precision advantage across all 4 models at corrected layers: R1-8B +22.4pp, OT-7B +21.2pp, QwQ +23.6pp, R1-32B +15.4pp. Remarkably consistent +15-24pp range.\n\n   Paper recommended claim (D032): \"At correctly selected layers, HS probes significantly outperform text probes on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp). The layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers, entirely masking this advantage at 32B scale. Practical implications differ by model: 7-8B models show strong HS advantage with comparable timing; R1-32B shows excellent lead time (+13 steps) but narrow coverage at the significant window; QwQ shows robust statistical significance but HS detects later than text.\"\n\n3. **HS and text monitoring exhibit different detection timing profiles** (narrowed from old Claim 3, now 4/4 models with GRU) — On r1-8b: HS temporal LR detects AT the commitment point (lead ~0) while text detects ~10 steps earlier. GRU achieves modest positive lead (+4.5+-3.0, worst seed +0.9). BOCPD/CUSUM fail to improve over simple thresholds. The oracle's +31-step advantage shows hidden states encode current safety state but poorly predict future trajectory. On 32B models: timing profiles vary (QwQ GRU lead +15.9, R1-32B +8.8) but FPR differences are non-significant. OT-7B GRU (layer 16, multi-layer L13-19, 3 seeds): bal_acc 74.6+-1.3%, coverage 64.5+-7.0%, lead +33.6+-4.8, FPR 27.4+-6.1%. GRU trades higher FPR for longer lead (consistent with R1-8B pattern). NOTE: OT-7B absolute lead times are inflated by long traces (~80 sentences vs ~30). Paper should normalize or explicitly caveat trace length differences when comparing across models.\n\n   NOTE: 32B timing profiles should be RE-EVALUATED at corrected layers (L60/L63) — current GRU results used old biased layers.\n\n## Methodological Contribution: Layer Selection Sensitivity (D028, elevated from RETRACTED Claim 4)\n\nThe layer selection metric `bal_acc × crossing_rate` systematically biases toward shallow layers because shallow layers have higher crossing rates (more frequently crossing the detection threshold). This bias is especially problematic for 32B models, where it selects layers at 3-16% depth instead of deep layers selected by threshold-dependent metrics.\n\n**Ablation evidence (4 models × 5 metrics) — UPDATED D036**:\n- `bal_acc × crossing_rate`: selects L2 (QwQ), L10 (R1-32B) — shallow, biased\n- Pure `bal_acc`: selects **middle layers** for 32B — L30 (QwQ, 47%), L47 (R1-32B, 73%); deep for 7-8B (agrees with other metrics). Threshold-free metric, behaves like AUROC.\n- `precision`: selects deep layers for all models (L60/L63 for 32B)\n- `pre_cp_fpr`: selects deep layers for all models\n- `composite` (additive): selects deep layers for all models\n- **Pattern**: Threshold-FREE metrics (bal_acc, AUROC) → middle layers; threshold-DEPENDENT metrics (precision, FPR, composite) → deep layers. Crossing_rate-contaminated metrics → shallow layers.\n\n**LOO-CV stability (D036)**: Under LOO-CV, the dominant layer is selected in 65-68% of folds regardless of metric. QwQ L30 selected 13/19 folds (bal_acc), R1-32B L47 selected 13/20 folds (bal_acc). Selection is robust to val set composition.\n\n**Corrected layer definition (D036)**: \"Corrected layers\" = consensus of threshold-dependent metrics (precision, inverse FPR, additive composite) — 3 of 4 non-biased metrics, not all 4. Pure bal_acc selects middle layers (L30/L47) with higher step-level accuracy (0.75/0.83 vs 0.71/0.76 at deep layers), but deployment-relevant metrics (precision, FPR) favor deep layers where all 4 models achieve HB-significant HS advantage.\n\n**Impact**: Incorrect layer selection entirely masked the HS advantage at 32B scale, leading to the false conclusion that HS advantage is scale-dependent. Even among unbiased metrics, metric choice affects optimal layer depth — threshold-free vs threshold-dependent is a second dimension of researcher degrees of freedom beyond the crossing_rate bias.\n\n**Anti-circular-reasoning defense (D031, refined D036)**: The claim that deep layers are \"correct\" for deployment rests on: (1) `crossing_rate` has a MECHANISTIC bias — shallow layers have compressed representations (1.4-2.7× smaller cosine distances) generating noise-driven crossings; (2) threshold-dependent metrics (precision, FPR) directly measure deployment-relevant properties; (3) at deep layers, all 4 models show significant HS advantage (HB corrected); (4) LOO-CV confirms selection stability. The paper presents layer selection as a \"researcher degree of freedom\" with systematic audit via sensitivity analysis.\n\n**Paper treatment**: Dedicated subsection in Method + Table showing metric × model → selected layer + downstream HS-text comparison. Frame as sensitivity analysis, not \"correct vs incorrect.\"\n\n## Story Spine\n\n- **Problem**: Reasoning models exhibit \"self-jailbreak\" — safety reasoning and harmful execution interleave throughout extended CoT, culminating in a \"commitment point\" where safety reasoning permanently ceases. Existing hidden-state detectors (TrajGuard, SafeSwitch, SIREN) target adversarial INPUT attacks on instruction-tuned models; they have never been evaluated on reasoning-model self-jailbreak where the threat is the model's OWN reasoning process.\n\n- **Existing approaches & gaps**: Hidden-state detectors achieve 95% defense on standard LLMs (TrajGuard) but operate at token-level. Reasoning-model safety analysis (Self-Jailbreaking, HarmThoughts) characterizes the phenomenon without providing deployable detectors. Text-level CoT monitors (SafeRemind, SafeThink) are vulnerable to pathological CoT. No prior work systematically compares detection modalities for reasoning-model self-jailbreak.\n\n- **Our framing**: We provide the first systematic evaluation of detection methods for reasoning-model safety commitment across **4 models, 2 architectures (Llama + Qwen), 2 training methods (R1-distilled + STILL), and 2 scales (7-8B + 32B)**, comparing hidden-state probes, text-based probes, sequence models (GRU), change-point detection (BOCPD/CUSUM), unsupervised methods (Mahalanobis, RepE direction, CCS), and nonlinear probes (MLP). We discover that: (a) temporal context is the most robust improvement, benefiting both modalities universally; (b) HS probes universally outperform text at correctly selected layers, with a critical sensitivity to layer selection methodology; (c) existing methods designed for other settings (TrajGuard, BOCPD, CCS, RepE) fail on reasoning model commitment; (d) linear probes are sufficient (MLP adds no value); (e) safety representations are model-specific (cross-transfer fails entirely), validated by control task (selectivity 7.5-18.5pp).\n\n- **Headline result (D032)**: \"Hidden-state probes significantly outperform text probes for safety commitment detection on all 4 models (12/12 Holm-Bonferroni, precision +15-24pp), but this advantage is entirely invisible under biased layer selection metrics. The composite metric `bal_acc × crossing_rate` systematically selects shallow layers at 32B scale, masking the HS signal and producing false negatives. This methodological finding, together with model-specific practical trade-offs at 32B (early detection vs broad coverage) and the comprehensive failure of 6 alternative methods, establishes that supervised temporal probing with principled layer selection is the most effective and robust approach for monitoring reasoning-model safety commitment.\"\n\n## Key Evidence Summary\n\n### R1-8B (Llama-8B, R1-distilled, n=43 test, class_weight=balanced, 60/20/20 split — CANONICAL)\n\nBest layer: 14 (45% depth). Full sweep layers 0-24 confirmed: layer 12 marginally better (+0.4pp bal_acc), no practical difference.\n\n| Method | Coverage | Lead Time | Pre-CP FPR | Safe FPR |\n|--------|----------|-----------|------------|----------|\n| HS Static LR L14 | — | -2.0 | **9.7%** | — |\n| HS Temporal W=5 | — | +0.6 | **10.2%** | — |\n| HS Temporal W=15 | — | **-0.1** | **8.8%** | — |\n| Text Temporal W=15 | — | +10.3* | 20.5% | — |\n| GRU Multi-7L (3-seed) | 72.9+-4.0% | +4.5+-3.0 | 16.5+-4.1% | — |\n\n*Text lead time inflated by high pre-CP FPR (trigger-happy detection)\nNOTE: HS LR lead time collapsed to ~0 with balanced weights — HS detects AT commitment, not before. Only GRU achieves positive lead (+4.5, worst seed +0.9).\n\n### OT-7B (Qwen-7B, STILL-trained, n=47 test, 228 total traces) — D026 CORRECTED to layer 16\n\nBest layer: **16 (57% depth)**. M001 corrected: layer 0 was selected by bal_acc x crossing_rate bug; layer 16 selected by bal_acc.\n\n| Method | Bal Acc | Precision | Coverage | Pre-CP FPR | Lead |\n|--------|---------|-----------|----------|-----------|------|\n| HS Temporal W=3 L16 (best) | **68.8%** | **46.6%** | 53.2% | **10.0%** | — |\n| Text Temporal W=25 (best) | 61.4% | 32.9% | 66.0% | 16.1% | 45.5 |\n| Text Temporal W=3 (matched) | 57.9% | 25.4% | — | 27.1% | — |\n\nBootstrap (layer 16, matched W=3, 1000 resamples):\n   bal_acc +10.7pp, 95% CI [4.9, 16.3], p<0.001 ✅\n   precision +21.9pp, 95% CI [14.0, 29.6], p<0.001 ✅\n   FPR -17.1pp, 95% CI [-22.2, -12.2], p<0.001 ✅ — **3/3 Holm-Bonferroni**\nSelectivity: 18.3pp (real=0.688, random=0.505) — highest across all models\n\n### 32B Cross-Architecture — D029 CORRECTED LAYERS\n\n**QwQ-32B (Qwen-32B, native, n=19-20, Layer 60 — corrected from L2)**\n- HS vs Text bootstrap (null-centered, 1000 resamples):\n  - Bal Acc: +11-22pp across W=1-15, ALL 15/15 significant (p<0.005)\n  - W=3 (matched): bal_acc +15.4pp (p<0.001 ✅), precision +23.6pp (p<0.001 ✅), FPR -9.8pp (p=0.004 ✅) — **3/3 Holm-Bonferroni**\n- Caveats: HS lead time poor (-1.2 to 1.9 steps vs text 3.7-12.3), position baseline competitive\n- Layer selection: `bal_acc × crossing_rate` selected L2 (3.1%); threshold-dependent metrics consensus selects L60 (94%); pure `bal_acc` selects L30 (47%, bal_acc=0.7513 vs L60=0.7101) (D036)\n\n**R1-32B (Qwen-32B, R1-distilled, n=20, Layer 63 — corrected from L10)**\n- W=1: bal_acc +18.7pp, p<0.001 ✅\n- W≥5: NS (dimensionality: 51200 × W features for n=20)\n- W=1: 3/3 Holm-Bonferroni ✅; W=3: 0/3 Bonferroni (null-centered v2); W≥5: NS\n- Layer selection: `bal_acc × crossing_rate` selected L10 (15.6%); threshold-dependent metrics consensus selects L63 (98%); pure `bal_acc` selects L47 (73%, bal_acc=0.8290 vs L63=0.7585) (D036)\n\n**OLD biased-layer results (RETRACTED as metric artifact):**\n| Model | Biased Layer | Corrected Layer | Biased p-value | Corrected p-value |\n|-------|-------------|----------------|----------------|-------------------|\n| R1-32B | L10 (16%) | L63 (98%) | 0.064-0.13 (NS) | <0.001 (W=1) ✅ |\n| QwQ-32B | L2 (3%) | L60 (94%) | 0.35-0.83 (NS) | <0.005 (all W) ✅ |\n\n### 4-Model Holm-Bonferroni Summary (D032 — COMPLETE: 12/12 ✅)\n\n| Model | Arch | Training | Scale | Layer | W | bal_acc | precision | FPR | Selectivity |\n|-------|------|----------|-------|-------|---|--------|-----------|-----|-------------|\n| R1-8B | Llama | R1-distilled | 8B | L14 (45%) | 15 | +8.2pp ✅ | +22.4pp ✅ | -7.4pp ✅ | 12.5pp |\n| OT-7B | Qwen | STILL | 7B | L16 (57%) | 3 | +10.7pp ✅ | +21.9pp ✅ | -17.1pp ✅ | 18.3pp |\n| QwQ-32B | Qwen | native | 32B | L60 (94%) | 3 | +15.4pp ✅ | +23.6pp ✅ | -9.8pp ✅ | 15.3pp |\n| R1-32B | Qwen | R1-distilled | 32B | L63 (98%) | 1 | +18.7pp ✅ | +15.4pp ✅ | -14.6pp ✅ | 7.5pp |\n\n**12/12 all pass Holm-Bonferroni step-down (α=0.05)**. Previously 5/12 with biased layers.\nPrecision advantage remarkably consistent: +15.4 to +23.6pp across all 4 models.\nCaveats: Different W per model; R1-32B W=1 coverage=25%; QwQ lead time negative.\n\n### Position Mediation Analysis (D038 → D039 → D042 complete)\n\n**Finding**: Position (relative step t/T) is a significant component of probe performance. 3/4 models retain HS advantage after residualization; R1-32B is the exception.\n\n| Model | W | Resid HS BA | Resid Text BA | HS-Text Gap | Gap p | HB |\n|-------|---|------------|--------------|-------------|-------|-----|\n| OT-7B | 3 | 0.609 | 0.540 | **+6.9pp** | <0.001 | ✅ |\n| R1-8B | 15 | 0.669 | 0.605 | **+6.4pp** | <0.001 | ✅ |\n| R1-8B | 3 | 0.571 | 0.534 | **+3.7pp** | <0.001 | ✅ |\n| QwQ-32B | 3 | 0.619 | 0.582 | **+3.7pp** | 0.011 | ✅ |\n| R1-32B | 1 | 0.552 | 0.532 | +1.9pp | 0.914 | ❌ |\n\nPosition-only BA: OT-7B/R1-8B/QwQ ≈ 0.706; R1-32B = 0.686.\n\n**D042 final picture**: HS advantage has two separable components — position-mediated and non-positional. 3/4 models retain significant non-positional HS advantage (HB pass); R1-32B's advantage is almost entirely position-mediated (drop 20.4pp, residualized gap NS). This is consistent with R1-32B's other caveats (W=1 only significant, 25% coverage).\n\n**Key implications for paper**:\n1. Position is a significant component (12-20pp drop) — universal\n2. 3/4 models retain non-positional HS advantage (residualized BA gap +3.7 to +6.9pp, HB pass)\n3. R1-32B is the exception: HS advantage position-mediated, residualized gap NS\n4. Temporal windowing preserves non-positional signal (R1-8B: 24pp drop@W=3 → 16pp@W=15)\n5. Paper framing: \"HS advantage persists after position removal in 3/4 models; R1-32B advantage is position-mediated\"\n\n### 5-Seed Robustness (D041)\n\n| Model | HB Pass Rate | Mean ΔPrec ± std | Mean ΔBA ± std |\n|-------|-------------|------------------|----------------|\n| OT-7B | **5/5** | +20.9 ± 1.3pp | +11.3 ± 1.5pp |\n| R1-32B | **5/5** | +13.7 ± 2.0pp | +11.8 ± 2.4pp |\n| QwQ-32B | **5/5** | +19.9 ± 2.5pp | +11.4 ± 3.2pp |\n| R1-8B | **3/5** | +14.6 ± 4.5pp | +9.4 ± 2.4pp |\n\nR1-8B failures are FPR-specific (seed 123 FPR p=0.262, seed 456 FPR p=0.952). Precision is directionally consistent across all 20 seed-model combinations (always positive). ΔPrec never reverses.\n\n**D041 insight**: Robustness splits by MODEL not SCALE. R1-32B (5/5, ΔPrec std=2.0pp) is more stable than R1-8B (3/5, ΔPrec std=4.5pp). \"7-8B robust / 32B sample-limited\" is factually wrong. R1-32B's absolute precision std (12.8pp) vs paired delta std (2.0pp) — paper must distinguish these.\n\n**Per-model evidence tier (D042)**:\n- **OT-7B**: Cleanest — 5/5 HB, largest residualized gap (+6.9pp), highest selectivity (18.3pp)\n- **QwQ-32B**: Robust — 5/5 HB, residualized gap holds (+3.7pp), but position baseline competitive\n- **R1-8B**: Precision-robust — residualized holds (+3.7-6.4pp), but FPR unstable (3/5 HB)\n- **R1-32B**: Statistically stable (5/5 HB, ΔPrec std=2.0pp) but advantage position-mediated (residualized NS)\n\n**Residualized precision**: Not tested (scope limited to BA per Reviewer recommendation).\n\n### BA-Layer Robustness: Metric Circularity Refuted (D044)\n\nR13 W1 concern: corrected selection uses threshold-dependent metrics (precision, FPR), evaluation also uses precision/FPR — potential circularity. Test: compute HS vs text on BA-selected layers (threshold-free criterion).\n\n| Model | BA-Opt Layer | ΔPrec | ΔBA | ΔFPR | ΔAUROC | All 4 HB? |\n|-------|-------------|-------|-----|------|--------|-----------|\n| R1-8B | L12 | +17.8pp | +7.8pp | -12.9pp | +9.3pp | ✅ |\n| OT-7B | L9 | +25.4pp | +11.7pp | -19.3pp | +14.8pp | ✅ |\n| QwQ-32B | L30 | +18.0pp | +14.8pp | -8.0pp | +17.3pp | ✅ |\n| R1-32B | L47 | +13.7pp | +14.9pp | -23.1pp | +21.1pp | ✅ |\n\n**4/4 models × 4 metrics = 16/16 HB pass.** HS advantage is a genuine modality property, not a layer selection artifact.\n\nKey insight: R1-32B on BA-layer L47 shows ΔPrec +13.7pp and ΔAUROC +21.1pp — stronger than corrected L63 in threshold-free metrics. OT-7B on BA-layer L9 has ΔPrec +25.4pp > corrected L16 (+21.9pp). HS advantage is robust to layer selection criterion.\n\nCaveat: QwQ FPR adj_p=0.041 (marginal, CI close to zero). Other 15/16 tests p≤0.006.\n\n### Post-hoc Power Analysis (D044)\n\n| Model | n (test) | MDE (80% power, α=0.05) |\n|-------|----------|------------------------|\n| OT-7B | 47-69 | 6.7-8.1pp |\n| R1-8B | 43-63 | 7.4-9.0pp |\n| QwQ-32B | 29 | 9.5pp |\n| R1-32B | 20-30 | 8.6-11.2pp |\n\nAll significant effects (15-24pp) are well above MDE → adequately powered. R1-32B residualized gap (+1.9pp) is far below MDE (11.2pp) → NS is power limitation, not evidence of absence.\n\n### Negative Results (expanded with R3 supplementary experiments)\n- **BOCPD/CUSUM (4/4 models)**: R1-8B BOCPD 93% detection but lead +3.5 < threshold +4.9; OT-7B/R1-32B/QwQ all 0% detection across all λ. CUSUM worse than threshold on all models.\n- **Mahalanobis (4/4 models confirmed negative)**: R1-8B (+0.07), OT-7B (+0.031), R1-32B (+0.148), QwQ (+0.204) — all separation ≈ 0. Signal in minor PCA components, not principal directions.\n- **RepE direction probing (4/4 models, corrected layers confirmed)**: Direction-based supervised method (needs CP labels). Results highly layer-dependent and model-specific:\n  - R1-32B L63 (corrected): bal_acc=0.559 (near-random), FPR=49.9% — **direction vector fails at deep layer** where supervised LR excels (0.826). Train-test gap 13.3pp shows poor generalization.\n  - QwQ L60 (corrected): bal_acc=0.756, precision=0.512, FPR=0.309 — **improves** from L2 (0.666), narrows gap with supervised LR W=1 (0.740 bal_acc), but still inferior in precision/FPR.\n  - R1-8B L14: bal_acc=0.749, OT-7B L16: bal_acc=0.642\n  - **Key insight**: Supervised LR is necessary — mean-difference direction cannot decode safety commitment at deep layers for R1-32B (discriminative training finds signal that simple direction averaging misses). Layer selection sensitivity applies to RepE too, but in model-specific ways (R1-32B: shallow better for RepE; QwQ: deep better for both).\n- **MLP nonlinear probe (4/4 models)**: 3/4 models worse than LR. Linear probes sufficient; nonlinearity adds no value.\n- **CCS-adapted (Burns et al. 2023, 4/4 models)**: WEAKLY SUPERVISED (needs CP labels for pair construction, not truly unsupervised). R1-8B bal_acc=0.777 (between supervised LR 0.817 and RepE 0.749). R1-32B FPR=0.410 (near-chance). OT-7B precision=0.319 (near-chance, high lead=20.5 is artifact of high FPR). Uses scheme B layers (biased). Paper must: (a) label as \"weakly supervised\" not \"unsupervised\"; (b) disclose pair construction differs from Burns et al.; (c) note scheme B layer limitation.\n- **Cross-model transfer (exp-003)**: All directions fail entirely (best: 58.3% acc, 40.7% crossing).\n\n## Venue Fit Risks\n\n- **EMNLP LLM Security track fit**: Strong — defense/detection evaluation for reasoning model jailbreak.\n- **Method simplicity risk**: Mitigate: frame as empirical study. Contribution is systematic evaluation + layer selection sensitivity discovery + comprehensive negative results.\n- **Statistical power**: With corrected layers, **12/12** tests pass Holm-Bonferroni across ALL 4 models (up from 5/12 with biased layers).\n- **HS advantage universal**: UPGRADED from \"scale-dependent\" — layer selection is the true moderator, not scale. Cleaner story.\n- **Trace vs step FPR**: Both reported with explanation.\n- **High safe FPR risk**: All methods 39-62% safe FPR. Frame as diagnostic tool limitation.\n- **32B caveats**: HS advantage exists but is more sensitive to window size (R1-32B W=1 only) and affected by dimensionality (51200-d at large W with n=20). Lead times shorter than 7-8B. These are honest limitations, not disqualifiers.\n\n## Anticipated Reviewer Concerns\n\n1. \"Method novelty?\" → Empirical study + systematic method comparison + layer selection sensitivity as methodological contribution + comprehensive negative results (6 methods fail).\n2. \"Only one model family?\" → **RESOLVED**: 4 models, 2 architectures (Llama + Qwen), 2 training methods, 2 scales. ALL showing significant HS advantage at corrected layers.\n3. \"GRU unstable?\" → 3-seed reporting with worst-seed bounds. R1-32B GRU at L10 was unstable; needs re-evaluation at L63.\n4. \"Too few traces?\" → Cross-model validation + control task selectivity 7.5-18.5pp.\n5. \"Fine-grained taxonomy?\" → Out of scope for current study.\n6. \"HS doesn't beat text?\" → **QUALIFIED REBUTTAL (D031)**: HS outperforms text at correct layers with STRONG evidence at 7-8B (precision +22pp, Holm-Bonf) and QUALIFIED evidence at 32B (R1-32B: significant W=1 but narrow; QwQ: significant all W but late detection). 32B non-significance at OLD layers was artifact. Layer selection sensitivity analysis shows this is a methodological issue, not absence of signal.\n7. \"Commitment point circular?\" → Cross-model consistency + control task selectivity argues against artifact.\n8. \"Missing related work?\" → Expansion to 30+ citations.\n9. \"No FPR analysis?\" → RESOLVED: both trace-level and step-level FPR reported.\n10. \"High safe FPR?\" → Limitation acknowledged.\n11. \"Control task / position confound?\" → RESOLVED (C2, D011): selectivity 7.5-18.5pp, HS FPR < position-only FPR.\n12. \"Multiple testing correction?\" → **RESOLVED**: 12/12 Holm-Bonferroni step-down (α=0.05) across all 4 models (up from 5/12 with biased layers).\n13. \"Trace vs step FPR?\" → Both reported with explanation.\n14. \"Layer selection is just hyperparameter tuning?\" → No — we show a systematic bias in a commonly used composite metric. The ablation across 5 metrics × 4 models is a reproducible methodological finding, not a one-off parameter choice.\n15. \"Why not just use the best layer for each model?\" → We do. The point is that the METRIC for selecting \"best\" matters. Biased metrics produce systematically wrong selections, masking real effects.\n16. \"32B results are marginal / only W=1 significant for R1-32B?\" → Dimensionality constraint (51200 × W > n=20 at W≥5). QwQ L60 significant at ALL W values. R1-32B L63 significant at W=1. Both confirm HS advantage exists; practical deployment would use W=1-3 for 32B models.\n\n## Title Candidates (D031)\n- \"Layer Selection Matters: How Metric Choice Determines Hidden-State Probe Effectiveness for Safety Monitoring\"\n- \"Temporal Probing for Safety Commitment Detection in Reasoning Models: A Comprehensive Evaluation\"\n- \"What Detects Safety Commitment in Reasoning Models? A Systematic Comparison of Probe-Based Methods\"\n- \"Hidden-State vs Text Monitoring for Reasoning Model Safety: Layer Selection as the Missing Variable\"\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 1\n  description: Cross-architecture hidden-state extraction + layer sweep + static probe\n    evaluation on r1-32b and QwQ-32B. Includes mandatory layer sweep (all layers)\n    to find best layer for 64-layer models before probe evaluation. Validates Claim\n    1 generalizes beyond r1-8b.\n  priority: P0\n  gpu_budget_hours: 10\n  deps: []\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  notes: 32B models have 64 layers, 5120-d hidden. r1-8b best layer was 14/32 (44%\n    depth) → expect best around layer 28-32 for 64-layer models. Extract ALL layers\n    for sweep, then select best for subsequent experiments. Must do layer sweep BEFORE\n    reporting static probe results — using wrong layer would produce false negative.\n  status: planned\n- id: exp-002\n  claim: 2\n  description: 'Cross-architecture temporal window evaluation: temporal LR W=15 on\n    r1-32b and QwQ-32B. Validate +30pp coverage improvement holds cross-architecture.'\n  priority: P0\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  models:\n  - DeepSeek-R1-Distill-Qwen-32B\n  - QwQ-32B\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  description: 'Cross-model transfer: train probe on r1-8b (Llama), test on r1-32b/QwQ\n    (Qwen2.5). Train on Qwen, test on Llama. Measures zero-shot cross-architecture\n    generalization.'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Key for cross-architecture story. Projection head needed (4096→5120 or vice\n    versa).\n  status: planned\n- id: exp-004\n  claim: 3\n  description: 'Lead time analysis across models: confirm negative lead time finding\n    on 32B models. Report lead time distribution per model.'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-005\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'TrajGuard-style Mahalanobis baseline: implement and evaluate on all\n    3 models. Expected to fail (signal in minor PCs, Fisher drops 17→1 in PCA-3D).'\n  priority: P0\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Critical baseline for 'existing detectors fail' claim. Use safe traces to\n    estimate covariance, compute MD per step.\n  status: planned\n- id: exp-006\n  claim:\n  - 1\n  - 2\n  description: 'Bootstrap confidence intervals + threshold-independent metrics: 1000\n    bootstrap resamples on all key metrics (coverage, lead time, accuracy). ALSO report\n    AUROC, precision-recall curves, detection delay CDF, cross-validation per-fold\n    variance, and FPR on safe traces (final_judgment=0.5).'\n  priority: P0\n  gpu_budget_hours: 1\n  deps:\n  - exp-001\n  - exp-002\n  - exp-003\n  - exp-004\n  - exp-005\n  status: planned\n- id: exp-007\n  claim: 2\n  description: 'Window size ablation: W=1,3,5,10,15,20,25 on all 3 models. Find optimal\n    W and show diminishing returns curve.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Layer selection ablation: all layers (not just 14) for temporal probe\n    on 32B models. Confirm middle-layer finding generalizes.'\n  priority: P1\n  gpu_budget_hours: 3\n  deps:\n  - exp-001\n  status: planned\n- id: exp-009\n  claim: 2\n  description: '16-label taxonomy supervision: use fine-grained labels (Type 1/2/3/4)\n    instead of binary commitment for richer training signal. May improve both coverage\n    and timing.'\n  priority: P1\n  gpu_budget_hours: 2\n  deps:\n  - exp-001\n  notes: Addresses reviewer concern about underusing available supervision.\n  status: planned\n- id: exp-010\n  claim: 3\n  description: 'Oracle decomposition: why can oracle but not probes achieve positive\n    lead time? Analyze what label patterns encode that hidden states don''t.'\n  priority: P1\n  gpu_budget_hours: 1\n  deps:\n  - exp-004\n  notes: For Discussion section. May reveal what architectural changes could close\n    the gap.\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'OpenThinker-7B (Qwen2.5-7B base): 4th model for 2×2 architecture×scale\n    matrix. Controls for scale confound.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-002\n  notes: From Human Review Note point 5. Adds Qwen2.5-7B to complement Llama-8B for\n    scale-matched comparison.\n  status: planned\n- id: exp-012\n  claim:\n  - 1\n  - 2\n  description: 'GRU/Attention probe as upper bound: verify GRU finding holds on 32B\n    models with more data. If still no improvement over LR, strengthens ''simplicity\n    is optimal'' story.'\n  priority: P2\n  gpu_budget_hours: 4\n  deps:\n  - exp-001\n  - exp-002\n  status: planned\n- id: exp-013\n  claim:\n  - 1\n  - 2\n  description: 'Text-based baseline: sentence-BERT embeddings (all-MiniLM-L6-v2) +\n    same temporal window LR (W=15) on CoT text. Compare coverage/lead time to hidden-state\n    probes. CRITICAL for proving hidden-state monitoring adds unique value over cheap\n    text monitoring. If text achieves comparable performance, paper motivation needs\n    restructuring.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps: []\n  notes: No GPU needed for embedding extraction (small model, CPU-feasible). Run on\n    all 4 models. This is the single most important missing baseline per Dream review\n    (flagged by all 3 tiers, both reviewers).\n  status: planned\n- id: exp-014\n  claim: 3\n  description: 'Bayesian Online Change-Point Detection (BOCPD) on per-step probe scores:\n    apply Adams & MacKay 2007 to the sequence of probe confidence scores. Could achieve\n    positive lead time by detecting distributional shift before textual commitment.\n    Also test CUSUM as simpler alternative.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - exp-001\n  notes: Addresses both 'no method novelty' and 'no positive lead time' criticisms\n    simultaneously. If BOCPD achieves reliable lead time where GRU doesn't, this becomes\n    a genuine methods contribution. If it also fails, strengthens the 'fundamental\n    limitation' narrative.\n  status: planned\n- id: exp-015\n  claim:\n  - 1\n  - 2\n  description: 'False positive analysis: run all probes (static, temporal, GRU, BOCPD)\n    on safe traces (final_judgment=0.5). Report FPR, precision-recall curves at various\n    thresholds. Essential for deployment utility claims.'\n  priority: P0\n  gpu_budget_hours: 0.5\n  deps:\n  - exp-001\n  - exp-002\n  notes: Dream flagged missing FPR as critical gap across median and worst tiers.\n    Without this, 'coverage' metric is uninterpretable — a probe that fires everywhere\n    gets 100% coverage.\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: diag_d1_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    best_layer_idx: 2\n    best_model_layer: 14\n    best_acc: 0.8114\n    best_f1: 0.6455\n    best_crossing_rate: 0.186\n    best_lead_mean: 8.38\n    best_lead_median: 6\n    default_layer20_acc: 0.7831\n    num_traces: 209\n    split: 125/41/43\n- exp_id: diag_d4_oracle_upper_bound\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    K5_detection_rate: 100\n    K5_early_detection_rate: 76.7\n    K5_mean_lead_time: 31\n    K5_median_lead_time: 29\n    K1_early_detection_rate: 83.7\n    K8_early_detection_rate: 65.1\n    pre_cp_mean_longest_streak: 14.6\n    test_traces: 43\n- exp_id: diag_d2_pca_viz\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    fisher_orig_L12: 17.462\n    fisher_orig_L14: 17.875\n    fisher_orig_L20: 18.614\n    fisher_orig_L24: 18.106\n    fisher_pca_L12: 0.953\n    fisher_pca_L14: 0.928\n    fisher_pca_L20: 0.92\n    fisher_pca_L24: 1.111\n    var_explained_3pc: 0.166\n    test_steps: 1835\n- exp_id: diag_d3_regularized_probes\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    static_lr_acc: 0.8172\n    static_lr_crossing_rate: 0.4651\n    static_lr_lead_mean: -2\n    temporal_lr_w5_acc: 0.8274\n    temporal_lr_w5_crossing_rate: 0.6512\n    temporal_lr_w5_lead_mean: -1.18\n    temporal_lr_w10_acc: 0.8364\n    temporal_lr_w10_crossing_rate: 0.6512\n    temporal_lr_w10_lead_mean: -0.61\n    temporal_lr_w15_acc: 0.8478\n    temporal_lr_w15_crossing_rate: 0.7674\n    temporal_lr_w15_lead_mean: -1.09\n    best_temporal_delta_over_static: 1.39\n    pass_criterion_met: false\n- exp_id: diag_gru_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    test_acc: 0.8305\n    test_acc_std: 0.1856\n    crossing_rate: 0.6744\n    lead_mean: -0.207\n    lead_median: -1\n    lead_std: 13\n    positive_lead_rate: 0.345\n    n_positive_lead: 10\n    n_detected: 29\n    early_stop_epoch: 14\n    model_params: 1622913\n- exp_id: exp_gru256_multilayer\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    gru_single_l14:\n      acc: 0.8386\n      crossing_rate: 0.721\n      lead_mean: 3.5\n      lead_median: 0\n      pos_lead: 13/31\n    gru_multi_7l:\n      acc: 0.8094\n      crossing_rate: 0.767\n      lead_mean: 4.7\n      lead_median: 0\n      pos_lead: 13/33\n    lr_single_l14:\n      acc: 0.8172\n      crossing_rate: 0.465\n      lead_mean: -2\n      lead_median: -2\n      pos_lead: 6/20\n    lr_multi_7l:\n      acc: 0.806\n      crossing_rate: 0.395\n      lead_mean: 1.1\n      lead_median: 0\n      pos_lead: 6/17\n    delta_gru_vs_lr: 3.7\n- exp_id: exp_005_trajguard_mahalanobis\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    best_k5_crossing_rate: 0.302\n    best_k5_lead_mean: 16.4\n    best_k5_config: pca_64_p75\n    best_k3_crossing_rate: 0.605\n    best_k3_lead_mean: 20.4\n    delta_max_rate: 0.023\n    safe_md_mean: 6.66\n    jb_pre_md_mean: 6.73\n    jb_post_md_mean: 6.64\n- exp_id: exp_006_bootstrap_ci\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    static_lr_acc: 0.768 [0.702,0.827]\n    static_lr_crossing: 60.4% [44.2,74.4]\n    static_lr_lead: +2.9 [-2.8,+9.5]\n    temporal_lr_acc: 0.731 [0.654,0.804]\n    temporal_lr_crossing: 60.6% [46.5,74.4]\n    temporal_lr_lead: +5.0 [-0.8,+11.9]\n    gru_single_acc: 0.790 [0.734,0.848]\n    gru_single_crossing: 51.4% [37.2,67.4]\n    gru_single_lead: -2.0 [-8.6,+4.9]\n    gru_multi_acc: 0.799 [0.742,0.854]\n    gru_multi_crossing: 51.4% [37.2,67.4]\n    gru_multi_lead: -0.4 [-6.4,+6.1]\n    paired_temporal_vs_static_lead_p: 0.19\n    paired_gru_vs_static_lead_p: 0.94\n    paired_gru_vs_temporal_lead_p: 0.99\n- exp_id: exp_013_text_baseline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    text_static_coverage: 0.605\n    text_static_lead: 4.3\n    text_static_acc: 0.661\n    text_static_auroc: 0.7384\n    text_temporal_w15_coverage: 0.651\n    text_temporal_w15_lead: 11.5\n    text_temporal_w15_acc: 0.678\n    text_temporal_w15_auroc: 0.759\n    hs_acc_advantage: 15-18pp\n- exp_id: exp_015_fpr_analysis\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    text_static_safe_fpr: 0.502\n    text_static_precp_fpr: 0.356\n    text_static_precision: 0.448\n    text_static_coverage: 0.605\n    text_static_lead: 4.3\n    text_static_acc: 0.661\n    text_temporal_safe_fpr: 0.385\n    text_temporal_precp_fpr: 0.272\n    text_temporal_precision: 0.487\n    text_temporal_coverage: 0.651\n    text_temporal_lead: 11.5\n    text_temporal_acc: 0.678\n    hs_static_safe_fpr: 0.39\n    hs_static_precp_fpr: 0.162\n    hs_static_precision: 0.622\n    hs_static_coverage: 0.605\n    hs_static_lead: 3\n    hs_static_acc: 0.768\n    hs_temporal_safe_fpr: 0.392\n    hs_temporal_precp_fpr: 0.16\n    hs_temporal_precision: 0.583\n    hs_temporal_coverage: 0.651\n    hs_temporal_lead: 4.9\n    hs_temporal_acc: 0.726\n    gru_safe_fpr: 0.521\n    gru_precp_fpr: 0.188\n    gru_precision: 0.648\n    gru_coverage: 0.744\n    gru_lead: 5.25\n    gru_acc: 0.816\n- exp_id: exp_014_bocpd_poc\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    bocpd_lambda10:\n      detection_rate: 0.93\n      mean_lead: 3.45\n      median_lead: 0\n      early_count: 16\n      late_count: 19\n    bocpd_lambda100:\n      detection_rate: 0.674\n      mean_lead: 1.03\n      median_lead: 0\n    cusum_best_t03h3:\n      detection_rate: 0.651\n      mean_lead: 0.89\n      median_lead: -4\n    fcp_baseline:\n      detection_rate: 0.651\n      mean_lead: 4.89\n      median_lead: 0\n    head_to_head_bocpd_vs_fcp:\n      bocpd_wins: 16\n      fcp_wins: 6\n      ties: 5\n    verdict: BOCPD higher detection (93% vs 65%) but lower mean lead (3.45 vs 4.89).\n      CUSUM universally worse. Neither method achieves earlier detection than simple\n      threshold crossing on average.\n- exp_id: exp_001a_r1_32b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    m001_corrected: true\n    best_layer_old: 2\n    best_layer_corrected: 10\n    layer_selection_metric: balanced_accuracy × crossing_rate (scheme B)\n    layer10_bal_acc: 0.718\n    layer10_crossing_rate: 0.6\n    gru_single_bal_acc_mean: 0.675\n    gru_single_crossing_mean: 0.3\n    gru_single_lead_mean: 9.1\n    gru_single_precp_fpr_mean: 0.135\n    gru_multi_bal_acc_mean: 0.655\n    gru_multi_crossing_mean: 0.23\n    gru_multi_lead_mean: 8.8\n    gru_multi_precp_fpr_mean: 0.114\n    temporal_lr_best_window: 10\n    temporal_lr_w10_bal_acc: 0.737\n    temporal_lr_w10_crossing: 0.5\n    temporal_lr_w10_lead: 9\n    temporal_lr_w10_precp_fpr: 0.189\n    bootstrap_hs_precp_fpr: 0.26\n    bootstrap_text_precp_fpr: 0.246\n    bootstrap_diff: 0.014\n    bootstrap_p_value: 0.999\n    bootstrap_ci95:\n    - -0.103\n    - 0.127\n    bootstrap_conclusion: no_significant_difference\n    paired_bootstrap_corrected:\n      hs_bal_acc: 0.794\n      text_bal_acc: 0.711\n      acc_delta: 0.084\n      acc_p_value_two_sided: 0.08\n      hs_precision: 0.61\n      text_precision: 0.516\n      prec_delta: 0.094\n      prec_p_value_two_sided: 0.05\n      hs_precp_fpr: 0.242\n      text_precp_fpr: 0.326\n      fpr_delta: -0.084\n      fpr_p_value_two_sided: 0.114\n      bonferroni_alpha: 0.017\n      bonferroni_pass: false\n      test_type: two-sided\n      solver: liblinear\n      canonical_file: artifacts/r1_32b_paired_bootstrap/results.json\n      note: directional but ns after Bonferroni. n=20 test traces insufficient power.\n        Old m001 FPR=0.246 used lbfgs solver (non-canonical).\n- exp_id: exp_001b_qwq_32b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    m001_corrected: true\n    best_layer_old: 1\n    best_layer_corrected: 2\n    layer_selection_metric: balanced_accuracy × crossing_rate (scheme B)\n    layer2_bal_acc: 0.73\n    layer2_crossing_rate: 0.47\n    gru_single_bal_acc_mean: 0.694\n    gru_single_crossing_mean: 0.75\n    gru_single_lead_mean: 19.3\n    gru_single_precp_fpr_mean: 0.303\n    gru_multi_bal_acc_mean: 0.724\n    gru_multi_crossing_mean: 0.84\n    gru_multi_lead_mean: 15.9\n    gru_multi_precp_fpr_mean: 0.289\n    temporal_lr_best_window: 5\n    temporal_lr_w5_bal_acc: 0.761\n    temporal_lr_w5_crossing: 0.42\n    temporal_lr_w5_lead: 23.5\n    temporal_lr_w5_precp_fpr: 0.18\n    bootstrap_phase5_invalid: true\n    bootstrap_phase5_bug: M002 - text_baseline_predictions() in exp_001b_bootstrap.py\n      used midpoint heuristic, not sentence embeddings\n    corrected_hs_vs_text:\n      hs_bal_acc: 0.679\n      text_bal_acc: 0.671\n      acc_delta: 0.009\n      acc_p_value_two_sided: 0.828\n      hs_precision: 0.583\n      text_precision: 0.525\n      prec_delta: 0.057\n      prec_p_value_two_sided: 0.346\n      hs_precp_fpr: 0.208\n      text_precp_fpr: 0.178\n      fpr_delta: 0.03\n      fpr_p_value_two_sided: 0.43\n      bonferroni_alpha: 0.017\n      bonferroni_pass: false\n      test_type: two-sided\n      solver: liblinear\n      note: No significant HS vs text difference on QwQ-32B. HS FPR slightly worse\n        than text.\n    bootstrap_conclusion: no_significant_difference\n- exp_id: exp_003_cross_transfer\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    baselines:\n      r1_8b_acc: 0.8234\n      r1_32b_acc: 0.6516\n      qwq_32b_acc: 0.7171\n    best_transfer_acc:\n      r1_8b_to_r1_32b: 0.522\n      r1_8b_to_qwq: 0.5948\n      r1_32b_to_qwq: 0.5499\n      qwq_to_r1_32b: 0.6726\n      r1_32b_to_r1_8b: 0.5828\n    transfer_method: PCA projection\n    conclusion_detail: Simple PCA projection insufficient for zero-shot cross-model\n      transfer. Signal is model-specific in geometric encoding.\n- exp_id: exp_c2_control_task\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_selectivity: 0.1245\n    r1_32b_selectivity: 0.075\n    r1_32b_selectivity_note: layer 10 (corrected best layer). Old layer 2 = 0.168\n    r1_32b_layer10_real_acc: 0.583\n    r1_32b_layer10_random_mean: 0.508\n    r1_32b_layer10_random_std: 0.051\n    qwq_32b_selectivity: 0.153\n    qwq_32b_selectivity_note: layer 2 (corrected from layer 1 = 0.189)\n    r1_8b_hs_pre_fpr: 0.0809\n    r1_8b_position_pre_fpr: 0.1581\n    r1_8b_cp_position_mean: 0.705\n    qwq_32b_layer2_real_acc: 0.678\n    qwq_32b_layer2_random_mean: 0.526\n    qwq_32b_layer2_random_std: 0.076\n    qwq_32b_layer2_position_acc: 0.706\n    qwq_32b_layer2_hs_pre_fpr: 0.2903\n    qwq_32b_layer2_position_pre_fpr: 0.25\n    qwq_32b_layer2_issue: position_baseline (70.6%) > HS probe (67.8%)\n- exp_id: exp_007_window_ablation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_8b:\n      W1:\n        bal_acc: 0.7783\n        precision: 0.6926\n        coverage: 0.7209\n        precp_fpr_trace: 0.1037\n        precp_fpr_step: 0.0965\n        lead_mean: 13.84\n      W3:\n        bal_acc: 0.7902\n        precision: 0.7228\n        coverage: 0.6977\n        precp_fpr_trace: 0.0988\n        precp_fpr_step: 0.085\n        lead_mean: 12.07\n      W5:\n        bal_acc: 0.781\n        precision: 0.7258\n        coverage: 0.6512\n        precp_fpr_trace: 0.0913\n        precp_fpr_step: 0.0809\n        lead_mean: 8.25\n      W10:\n        bal_acc: 0.7925\n        precision: 0.7431\n        coverage: 0.5581\n        precp_fpr_trace: 0.0865\n        precp_fpr_step: 0.0761\n        lead_mean: 10.04\n      W15:\n        bal_acc: 0.8017\n        precision: 0.7767\n        coverage: 0.5116\n        precp_fpr_trace: 0.0701\n        precp_fpr_step: 0.0639\n        lead_mean: 7.23\n      W20:\n        bal_acc: 0.8072\n        precision: 0.7862\n        coverage: 0.5349\n        precp_fpr_trace: 0.0661\n        precp_fpr_step: 0.0612\n        lead_mean: 7.43\n      W25:\n        bal_acc: 0.8095\n        precision: 0.8216\n        coverage: 0.4884\n        precp_fpr_trace: 0.0545\n        precp_fpr_step: 0.0483\n        lead_mean: 8.14\n      best_bal_acc_W: 25\n    r1_32b:\n      W1:\n        bal_acc: 0.7182\n        precision: 0.549\n        coverage: 0.8\n        precp_fpr_trace: 0.2764\n        precp_fpr_step: 0.3203\n        lead_mean: 12.88\n      W3:\n        bal_acc: 0.7252\n        precision: 0.56\n        coverage: 0.8\n        precp_fpr_trace: 0.2576\n        precp_fpr_step: 0.3064\n        lead_mean: 11.38\n      W5:\n        bal_acc: 0.7309\n        precision: 0.575\n        coverage: 0.75\n        precp_fpr_trace: 0.2393\n        precp_fpr_step: 0.2841\n        lead_mean: 11.07\n      W10:\n        bal_acc: 0.7371\n        precision: 0.6093\n        coverage: 0.7\n        precp_fpr_trace: 0.1891\n        precp_fpr_step: 0.234\n        lead_mean: 10.79\n      W15:\n        bal_acc: 0.7207\n        precision: 0.5907\n        coverage: 0.7\n        precp_fpr_trace: 0.2089\n        precp_fpr_step: 0.2451\n        lead_mean: 10.86\n      W20:\n        bal_acc: 0.6961\n        precision: 0.5628\n        coverage: 0.65\n        precp_fpr_trace: 0.2193\n        precp_fpr_step: 0.2618\n        lead_mean: 9.62\n      W25:\n        bal_acc: 0.7028\n        precision: 0.5662\n        coverage: 0.7\n        precp_fpr_trace: 0.2282\n        precp_fpr_step: 0.2646\n        lead_mean: 10.71\n      best_bal_acc_W: 10\n    qwq_32b:\n      W1:\n        bal_acc: 0.7298\n        precision: 0.5435\n        coverage: 0.7895\n        precp_fpr_trace: 0.185\n        precp_fpr_step: 0.2276\n        lead_mean: 19.73\n      W3:\n        bal_acc: 0.7452\n        precision: 0.5647\n        coverage: 0.7368\n        precp_fpr_trace: 0.175\n        precp_fpr_step: 0.2141\n        lead_mean: 20.64\n      W5:\n        bal_acc: 0.761\n        precision: 0.5733\n        coverage: 0.7368\n        precp_fpr_trace: 0.1795\n        precp_fpr_step: 0.2168\n        lead_mean: 20.07\n      W10:\n        bal_acc: 0.7469\n        precision: 0.5714\n        coverage: 0.7368\n        precp_fpr_trace: 0.1707\n        precp_fpr_step: 0.2073\n        lead_mean: 18.43\n      W15:\n        bal_acc: 0.7412\n        precision: 0.5816\n        coverage: 0.6842\n        precp_fpr_trace: 0.1605\n        precp_fpr_step: 0.1911\n        lead_mean: 15.77\n      W20:\n        bal_acc: 0.7542\n        precision: 0.6024\n        coverage: 0.6316\n        precp_fpr_trace: 0.1567\n        precp_fpr_step: 0.1789\n        lead_mean: 15.75\n      W25:\n        bal_acc: 0.7624\n        precision: 0.6177\n        coverage: 0.5789\n        precp_fpr_trace: 0.1476\n        precp_fpr_step: 0.1694\n        lead_mean: 14.91\n      best_bal_acc_W: 25\n    finding: Coverage monotonically DECREASES with W across all 3 models. Temporal\n      context creates precision-sensitivity tradeoff (higher W → higher precision,\n      lower coverage, lower FPR). R1-8B dominates (lowest FPR, highest precision).\n      QwQ-32B FPR significantly lower than R1-32B with larger lead_mean.\n- exp_id: exp_ot7b_full_pipeline\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_traces: 228\n    best_layer: 16\n    best_layer_depth_pct: 57.1\n    best_layer_score: 0.6876\n    best_hs_window: 3\n    best_hs_bal_acc: 0.688\n    best_hs_precision: 0.466\n    best_hs_pre_cp_fpr: 0.1\n    best_hs_coverage: 0.5319\n    best_hs_lead: 21.6\n    best_text_window: 25\n    best_text_bal_acc: 0.6141\n    best_text_precision: 0.3291\n    best_text_pre_cp_fpr: 0.1605\n    bootstrap_bal_acc_delta: 0.1067\n    bootstrap_bal_acc_ci95: '[0.049, 0.163]'\n    bootstrap_bal_acc_p: 0.001\n    bootstrap_bal_acc_bonf: true\n    bootstrap_precision_delta: 0.2189\n    bootstrap_precision_ci95: '[0.140, 0.296]'\n    bootstrap_precision_p: 0.001\n    bootstrap_precision_bonf: true\n    bootstrap_fpr_delta: -0.1705\n    bootstrap_fpr_ci95: '[-0.222, -0.122]'\n    bootstrap_fpr_p: 0.001\n    bootstrap_fpr_bonf: true\n    holm_bonferroni: 3/3\n    selectivity_pp: 18.3\n    selectivity_real_acc: 0.688\n    selectivity_random_mean: 0.505\n    layer0_bal_acc: 0.672\n    layer0_precision: 0.357\n    layer0_pre_cp_fpr: 0.188\n    layer16_vs_layer0: '+9.0pp bal_acc, +20.8pp precision, -8.7pp FPR. Precision Bonf:\n      L0 p=0.056 FAIL -> L16 p<0.001 PASS'\n    layer_verification: 'Layer 16 verified superior to Layer 0: 3/3 Bonferroni (was\n      2/3 on L0)'\n    r1_8b_layer_supplement: 'Full sweep layers 0-24 confirmed: best=L12 (0.7871) ~\n      L14 (0.7830), no early-layer dominance.'\n    gru_single_l16_bal_acc: 0.7246\n    gru_single_l16_coverage: 0.667\n    gru_single_l16_lead: 35.25\n    gru_single_l16_precp_fpr: 0.2904\n    gru_multi_l13_19_bal_acc: 0.7464\n    gru_multi_l13_19_coverage: 0.645\n    gru_multi_l13_19_lead: 33.61\n    gru_multi_l13_19_precp_fpr: 0.2741\n- exp_id: exp_pathb_annotation_validation\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    tfidf_lr_f1: 0.5899\n    tfidf_lr_cp_agreement: 0.561\n    minilm_lr_f1: 0.5149\n    minilm_lr_cp_agreement: 0.534\n    threshold_f1: 0.9\n    threshold_cp: 0.85\n    failure_reason: Safety recall extremely low (41-46%). Simple classifiers cannot\n      distinguish subtle safety-aware expressions in CoT from regular reasoning. CP\n      MAE=5-6 sentences.\n    recommendation: Need LLM API annotation or fine-tuned DeBERTa 16-class classifier\n- exp_id: exp_r3_repe_direction\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b:\n      layer: 2\n      bal_acc: 0.7491\n      precision: 0.516\n      pre_cp_fpr: 0.2264\n      coverage: 0.3953\n      lead_mean: 9.7\n    r1_32b_corrected:\n      layer: 63\n      bal_acc: 0.5588\n      precision: 0.3891\n      pre_cp_fpr: 0.4986\n      coverage: 0.6\n      lead_mean: 12\n    r1_32b_old:\n      layer: 10\n      bal_acc: 0.6707\n      precision: 0.5538\n      pre_cp_fpr: 0.2423\n      coverage: 0.45\n      lead_mean: 6.3\n    qwq_32b_corrected:\n      layer: 60\n      bal_acc: 0.7562\n      precision: 0.5118\n      pre_cp_fpr: 0.3089\n      coverage: 0.7368\n      lead_mean: 11.9\n    qwq_32b_old:\n      layer: 2\n      bal_acc: 0.6661\n      precision: 0.4193\n      pre_cp_fpr: 0.3997\n      coverage: 0.7368\n      lead_mean: 13.4\n    ot_7b:\n      layer: 16\n      bal_acc: 0.718\n      precision: 0.3733\n      pre_cp_fpr: 0.2573\n      coverage: 0.5319\n      lead_mean: 26.1\n    vs_lr_r1_8b:\n      lr_bal_acc: 0.817\n      lr_precision: 0.693\n      lr_fpr: 0.097\n      repe_weaker_acc: true\n      repe_weaker_precision: true\n    finding: 'Corrected layers: R1-32B L63 RepE degrades severely (bal_acc 0.67→0.56,\n      FPR 0.24→0.50); QwQ L60 improves (bal_acc 0.67→0.76). Both still below supervised\n      LR. Unsupervised RepE direction insufficient at any layer.'\n- exp_id: exp_r3_bocpd_ot7b_w15\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    W: 15\n    fcp_null_rate: 0.53\n    note: W=15 mismatched with OT-7B best window W=3, causing 53% traces with null\n      FCP. Results unreliable due to parameter mismatch.\n    parent_best_W: 3\n- exp_id: exp_r3_mlp_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    source: v1_per_model_json (K=5)\n    warning: 'over-parameterization: v2 had K=1 detection bug (coverage=1.0). v1 data\n      used here.'\n    caveat: OT-7B uses centered window; other models use causal window\n    r1_8b:\n      W1:\n        bal_acc: 0.806\n        precision: 0.646\n        fpr: 0.137\n        coverage: 0.767\n        lead: 14.27\n      W3:\n        bal_acc: 0.81\n        precision: 0.706\n        fpr: 0.1\n        coverage: 0.721\n        lead: 9.71\n      W5:\n        bal_acc: 0.843\n        precision: 0.595\n        fpr: 0.201\n        coverage: 0.884\n        lead: 12.89\n      W10:\n        bal_acc: 0.846\n        precision: 0.592\n        fpr: 0.206\n        coverage: 0.884\n        lead: 13.29\n      lr_W3: 0.79\n      lr_W5: 0.781\n      lr_W10: 0.793\n    r1_32b:\n      W3:\n        bal_acc: 0.713\n        precision: 0.585\n        fpr: 0.245\n        coverage: 0.8\n        lead: 9.12\n      W10:\n        bal_acc: 0.688\n        precision: 0.524\n        fpr: 0.332\n        coverage: 0.75\n        lead: 10.33\n      lr_W3: 0.725\n      lr_W10: 0.737\n    qwq_32b:\n      W5:\n        bal_acc: 0.604\n        precision: 0.339\n        fpr: 0.692\n        coverage: 0.842\n        lead: 33.19\n      W10:\n        bal_acc: 0.698\n        precision: 0.432\n        fpr: 0.428\n        coverage: 0.842\n        lead: 22.94\n      lr_W5: 0.761\n      lr_W10: 0.747\n    ot_7b:\n      W1:\n        bal_acc: 0.73\n        precision: 0.456\n        fpr: 0.165\n        coverage: 0.766\n        lead: 32.19\n      W3:\n        bal_acc: 0.747\n        precision: 0.343\n        fpr: 0.362\n        coverage: 0.872\n        lead: 41.22\n      lr_W3: 0.688\n    finding: 'MLP inconsistent vs LR: r1_8b +5pp at W5/10, ot_7b +6pp at W3, but r1_32b\n      -2 to -5pp, qwq_32b -5 to -16pp. Small datasets (r1_32b=100, qwq=95) likely\n      cause MLP overfitting. Signal linearly separable for most models.'\n- exp_id: exp_r3_bocpd_ot7b_w3\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    W: 3\n    layer: 16\n    n_test: 47\n    bocpd_all_lambda:\n      detection_rate: 0\n      note: W=3 probe scores too spiky (0→1 in 1-2 steps), Gaussian model fails\n    fcp_t05_k2:\n      detection_rate: 0.894\n      mean_lead: 11.83\n      median_lead: 10.5\n    fcp_t05_k3:\n      detection_rate: 0.745\n      mean_lead: 8.71\n      median_lead: 7\n    fcp_t03_k3:\n      detection_rate: 0.787\n      mean_lead: 11.92\n      median_lead: 10\n    fcp_t05_k5:\n      detection_rate: 0.468\n      mean_lead: 5.09\n      median_lead: 4.5\n    cusum_t02_h2:\n      detection_rate: 0.745\n      mean_lead: 7.46\n      median_lead: 6\n    cusum_t03_h2:\n      detection_rate: 0.702\n      mean_lead: 6.03\n      median_lead: 5\n    vs_r1_8b:\n      r1_bocpd_l10_det: 0.93\n      ot7b_bocpd_det: 0\n      r1_fcp_det: 0.651\n      ot7b_fcp_k2_det: 0.894\n      r1_fcp_lead: 4.89\n      ot7b_fcp_k2_lead: 11.83\n    finding: 'BOCPD 0% on OT-7B (all lambdas) vs 93% on R1-8B. Commitment dynamics\n      model-specific: R1-8B gradual (BOCPD works), OT-7B abrupt (simple threshold\n      optimal). Negative result confirmed cross-model for R3-W2.'\n- exp_id: exp_r3_mahalanobis_ot7b\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    layer: 16\n    pca_dims_tested:\n    - 16\n    - 32\n    - 64\n    - 128\n    - 256\n    md_separation:\n      pca16: -0.048\n      pca32: 0.012\n      pca64: 0.031\n      pca128: 0.004\n      pca256: -0.093\n    safe_md_mean_pca64: 7.68\n    post_md_mean_pca64: 7.71\n    pca64_k3_false_alarm_vs_tp:\n      p50:\n        fa_rate: 0.872\n        tp_rate: 0.385\n      p75:\n        fa_rate: 0.574\n        tp_rate: 0.231\n      p90:\n        fa_rate: 0.17\n        tp_rate: 0.154\n      p95:\n        fa_rate: 0.043\n        tp_rate: 0\n    vs_r1_8b:\n      r1_safe_md: 6.66\n      r1_post_md: 6.73\n      r1_separation: 0.07\n      ot7b_safe_md: 7.68\n      ot7b_post_md: 7.71\n      ot7b_separation: 0.03\n      failure_mode: 'identical: signal in minor PCA components, not principal directions'\n    finding: 'Mahalanobis zero discriminative power on OT-7B (separation ≈ 0 across\n      all PCA dims). False alarm rate >= true positive rate at every threshold. Failure\n      mode identical to R1-8B. R3-W2 fully addressed: 3/3 methods (BOCPD/CUSUM/Mahalanobis)\n      fail consistently across both models.'\n- exp_id: exp_r3_ccs_probe\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_8b:\n      bal_acc: 0.777\n      precision: 0.565\n      fpr: 0.191\n      coverage: 0.674\n      lead: 0.7\n    qwq_32b:\n      bal_acc: 0.731\n      precision: 0.555\n      fpr: 0.214\n      coverage: 0.684\n      lead: 2\n    r1_32b:\n      bal_acc: 0.703\n      precision: 0.507\n      fpr: 0.41\n      coverage: 0.9\n      lead: 5.2\n    ot_7b:\n      bal_acc: 0.692\n      precision: 0.319\n      fpr: 0.344\n      coverage: 0.809\n      lead: 20.5\n    vs_supervised_lr_r1_8b:\n      lr_bal_acc: 0.817\n      lr_precision: 0.693\n      lr_fpr: 0.097\n      ccs_weaker: true\n    vs_repe_r1_8b:\n      repe_bal_acc: 0.749\n      ccs_better: true\n    finding: CCS is best unsupervised method (beats RepE) but still significantly\n      below supervised LR. All models needed polarity flip. FPR 0.19-0.41 across all\n      models confirms unsupervised gap.\n- exp_id: exp_r3_r1_32b_l63_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: null-centered two-sided bootstrap\n    W1:\n      bal_acc_delta: 0.187\n      bal_acc_p: 0\n      precision_delta: 0.154\n      precision_p: 0\n      fpr_delta: -0.146\n      fpr_p: 0.007\n      bonferroni_pass: 3/3\n    W3:\n      bal_acc_delta: 0.112\n      bal_acc_p: 0.02\n      precision_delta: 0.13\n      precision_p: 0.032\n      fpr_delta: -0.114\n      fpr_p: 0.077\n      bonferroni_pass: 0/3\n    W5:\n      bal_acc_delta: 0.097\n      bal_acc_p: 0.046\n      bonferroni_pass: 0/3\n    W10:\n      bal_acc_p: 0.384\n      bonferroni_pass: 0/3\n    W15:\n      bal_acc_p: 0.075\n      bonferroni_pass: 0/3\n    finding: W=1 significant 3/3 Bonferroni (alpha=0.0167). W3+ all fail after Bonferroni.\n      Confirms HS advantage exists at L63 but only robust at minimal temporal context.\n- exp_id: exp_r3_qwq_l60_bootstrap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    method: null-centered two-sided bootstrap (bugfixed)\n    bug_fixed: missing np.mean(bd) centering caused p~0.5\n    W1:\n      bal_acc_ci: '[0.15,0.29]'\n      bal_acc_p: 0\n      precision_ci: '[0.21,0.39]'\n      precision_p: 0\n      fpr_ci: '[-0.23,-0.12]'\n      fpr_p: 0\n    W3:\n      bal_acc_p: 0\n      precision_p: 0\n      fpr_p: 0.004\n      precision_delta: 0.236\n      fpr_delta: -0.098\n    W5:\n      bal_acc_p: 0\n      precision_p: 0\n      fpr_p: 0.011\n    W10:\n      bal_acc_p: 0\n      precision_p: 0.016\n      fpr_p: 0.009\n    W15:\n      bal_acc_p: 0.004\n      precision_p: 0.003\n      fpr_p: 0.007\n    bonferroni_summary: 15/15 pass (alpha=0.0167)\n    finding: All 15 tests significant after bugfix. QwQ L60 shows robust HS advantage\n      across all windows, consistent with OT-7B. scale-dependent claim falsified.\n- exp_id: exp_r3_layer_ablation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    models_tested: 4\n    metrics_tested: 5\n    bias_discovered: bal_acc x crossing_rate systematically selects shallow layers\n    qwq_32b:\n      biased_layer: 2\n      corrected_layer: 60\n      bal_acc_gain: +1.75pp\n      precision_gain: +11.5pp\n      fpr_reduction: -8.3pp\n    r1_32b:\n      biased_layer: 10\n      corrected_layer: 63\n      bal_acc_gain: +3.7pp\n      precision_gain: +4.1pp\n      fpr_reduction: -4.3pp\n    r1_8b:\n      biased_layer: 0\n      best_layer: 12\n      consistency: L12-L16 cluster, current L14 near-optimal\n    ot_7b:\n      biased_layer: 0\n      best_layer: 9\n      current_layer: 16\n      note: 4 metrics select 4 different layers\n    cross_metric_consistency:\n      r1_8b: CONSISTENT\n      r1_32b: VARIED (all point deep)\n      qwq_32b: VARIED (all point deep)\n      ot_7b: VARIED\n    finding: crossing_rate biases layer selection to shallow layers. Pure bal_acc/precision\n      select mid-to-deep layers (40-95% depth). R1-32B and QwQ affected most severely.\n- exp_id: exp_r3_mahalanobis_r1_32b_qwq\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_32b:\n      layer: 63\n      safe_md: 6.73\n      post_md: 6.88\n      separation: 0.15\n      best_pca: 64\n    qwq_32b:\n      layer: 60\n      safe_md: 3.22\n      post_md: 3.42\n      separation: 0.2\n      best_pca: 16\n    cross_model_summary:\n      r1_8b_sep: 0.07\n      ot_7b_sep: 0.03\n      r1_32b_sep: 0.15\n      qwq_32b_sep: 0.2\n      max_separation: 0.2\n      all_fail: true\n    finding: 4/4 models Mahalanobis fails. Max separation 0.20 (QwQ), false alarm\n      rate >= true positive at every threshold. Signal in minor PCA components, not\n      principal directions.\n- exp_id: exp_r3_bocpd_r1_32b_qwq\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_32b:\n      layer: 10\n      W: 10\n      bocpd_det: 0\n      cusum_det: 0.85\n      cusum_lead: 2.59\n      fcp_det: 0.95\n      fcp_lead: 5.68\n    qwq_32b:\n      layer: 2\n      W: 5\n      bocpd_det: 0\n      cusum_det: 0.737\n      cusum_lead: 9.86\n      fcp_det: 0.789\n      fcp_lead: 9.4\n    cross_model_bocpd:\n      r1_8b: 0.93\n      r1_32b: 0\n      ot_7b: 0\n      qwq_32b: 0\n      only_r1_8b_works: true\n    finding: BOCPD 0% on 3/4 models (only R1-8B exception at 93%). CUSUM universally\n      inferior to simple FCP threshold. Advanced change-point methods fail for safety\n      commitment detection.\n- exp_id: exp_r3_coverage_bias\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b:\n      total: 268\n      included: 209\n      excluded: 59\n      exclusion_rate: 0.22\n    r1_32b:\n      total: 100\n      excluded: 0\n      exclusion_rate: 0\n    qwq_32b:\n      total: 95\n      excluded: 0\n      exclusion_rate: 0\n    exclusion_reason: All 59 excluded traces are jailbreak with no safety reasoning\n      phase (no commitment point annotatable)\n    length_test:\n      excluded_mean: 38\n      included_mean: 46.3\n      mann_whitney_p: 0.0001\n      excluded_shorter: true\n    finding: 22% exclusion in R1-8B is task-definitional (no CP to annotate), not\n      sampling bias. R1-32B/QwQ 0% exclusion. Coverage metric valid within annotatable\n      population.\n- exp_id: exp_r3_selectivity_ci_raw\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    feature_type: raw 5120-d (no PCA)\n    real_acc: 0.584\n    random_mean: 0.508\n    selectivity_pp: 7.6\n    bootstrap_mean_pp: 8.4\n    bootstrap_std_pp: 6.7\n    ci_95: '[-3.9, 22.7]pp'\n    p_value: 0.107\n    significant: false\n    vs_pca128:\n      pca128_selectivity: 15.9\n      pca128_p: 0\n      pca128_ci: '[9.7, 21.9]pp'\n    finding: Raw 5120-d selectivity 7.6pp not significant (p=0.107, CI includes 0).\n      Under-determined n&lt;p without PCA. PCA-128 gives 15.9pp (p<0.001) — dimensionality\n      reduction needed for reliable selectivity.\n- exp_id: exp_r3_gru_per_seed\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    seeds:\n    - 42\n    - 123\n    - 456\n    - 789\n    - 1024\n    split: 70/30\n    bal_acc:\n      mean: 0.772\n      std: 0.038\n      min: 0.729\n      max: 0.833\n    crossing_rate:\n      mean: 0.711\n      std: 0.121\n    lead_mean:\n      mean: 8.2\n      std: 2.9\n    fpr:\n      mean: 0.229\n      std: 0.075\n    vs_single_seed:\n      single_seed_bal_acc: 0.839\n      multi_seed_mean: 0.772\n      delta: -0.067\n      note: Single seed (0.839) is optimistic; multi-seed mean (0.772) more representative\n    finding: GRU robust across 5 seeds (std=3.8pp < 5pp threshold). Single-seed result\n      overestimates by ~6.7pp. Lead time high variance (std=2.9) indicates sensitivity\n      to data split.\n- exp_id: exp_r3_selectivity_corrected\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    qwq_32b_l60:\n      real_acc: 0.667\n      random_mean: 0.523\n      random_std: 0.051\n      selectivity_pp: 14.4\n      position_baseline_acc: 0.705\n      layer: 60\n    r1_32b_l63:\n      real_acc: 0.746\n      random_mean: 0.549\n      random_std: 0.06\n      selectivity_pp: 19.7\n      position_baseline_acc: 0.624\n      layer: 63\n    comparison:\n      qwq_old_l2: 15.3\n      qwq_new_l60: 14.4\n      r1_32b_old_l10: 7.5\n      r1_32b_new_l63: 19.7\n    both_pass_5pp: true\n    finding: Both corrected layers pass 5pp threshold. R1-32B selectivity dramatically\n      improves from 7.5pp (L10) to 19.7pp (L63). QwQ stable (15.3→14.4pp). Deep layers\n      encode stronger safety signal beyond positional confounds.\n- exp_id: exp_r3_bootstrap_10k\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    n_resamples: 10000\n    holm_bonferroni: 12/12 pass\n    tests:\n      r1_8b_bal_acc:\n        delta: 0.1796\n        p: 0\n        rank: 1\n      r1_8b_precision:\n        delta: 0.2786\n        p: 0\n        rank: 2\n      r1_8b_fpr:\n        delta: -0.1255\n        p: 0\n        rank: 3\n      ot_7b_precision:\n        delta: 0.2189\n        p: 0\n        rank: 4\n      ot_7b_fpr:\n        delta: -0.1705\n        p: 0\n        rank: 5\n      r1_32b_bal_acc:\n        delta: 0.1871\n        p: 0\n        rank: 6\n      r1_32b_precision:\n        delta: 0.1544\n        p: 0\n        rank: 7\n      qwq_32b_bal_acc:\n        delta: 0.1478\n        p: 0\n        rank: 8\n      qwq_32b_precision:\n        delta: 0.2349\n        p: 0\n        rank: 9\n      ot_7b_bal_acc:\n        delta: 0.1067\n        p: 0.0003\n        rank: 10\n      qwq_32b_fpr:\n        delta: -0.0952\n        p: 0.0061\n        rank: 11\n      r1_32b_fpr:\n        delta: -0.1457\n        p: 0.0096\n        rank: 12\n    marginal_tests:\n      r1_32b_fpr:\n        p: 0.0096\n        threshold: 0.05\n      qwq_32b_fpr:\n        p: 0.0061\n        threshold: 0.025\n    r1_8b_fpr_clarification: R1-8B FPR at W=3 is p<0.0001 (rank 3), not marginal.\n      The 0.044 was from old W=15 config.\n    finding: 'All 12/12 Holm-Bonferroni pass with 10000 resamples. R1-8B FPR not marginal\n      at corrected W=3. Actual marginal tests: R1-32B FPR (p=0.0096) and QwQ FPR (p=0.0061),\n      both passing comfortably.'\n- exp_id: exp_r5_auroc_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    r1_8b:\n      auroc_best_layer: 13\n      auroc_best: 0.806\n      paper_layer: 14\n      auroc_at_paper: 0.803\n      match: near-match (adjacent, delta=0.003)\n    ot_7b:\n      auroc_best_layer: 1\n      auroc_best: 0.777\n      paper_layer: 16\n      auroc_at_paper: 0.746\n      match: no (flat landscape 0.70-0.78)\n    qwq_32b:\n      auroc_best_layer: 32\n      auroc_best: 0.839\n      paper_layer: 60\n      auroc_at_paper: 0.756\n      match: no (AUROC prefers mid-depth ~50%)\n    r1_32b:\n      auroc_best_layer: 31\n      auroc_best: 0.897\n      paper_layer: 63\n      auroc_at_paper: 0.767\n      match: no (AUROC prefers mid-depth ~50%)\n    finding: 'AUROC does NOT converge to the same deep layers. For 32B models, AUROC\n      selects mid-depth layers (~50%) vs paper''s very deep layers (>90%). R1-8B near-match\n      only. Note: worker applied PCA-256 on 32B models to handle dimensionality, which\n      may affect results.'\n- exp_id: exp_r5_pca384_control\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    holm_bonferroni: 10/12 reject\n    tests:\n      r1_8b_bal_acc:\n        pca384: 0.7001\n        text: 0.6875\n        delta: 0.0126\n        p: 0.731\n        reject: false\n      r1_8b_precision:\n        pca384: 0.8162\n        text: 0.5852\n        delta: 0.231\n        p: 0\n        reject: true\n      r1_8b_fpr:\n        pca384: 0.0668\n        text: 0.1614\n        delta: -0.0947\n        p: 0.003\n        reject: true\n      ot_7b_bal_acc:\n        pca384: 0.7558\n        text: 0.643\n        delta: 0.1128\n        p: 0\n        reject: true\n      ot_7b_precision:\n        pca384: 0.5225\n        text: 0.3545\n        delta: 0.1681\n        p: 0\n        reject: true\n      ot_7b_fpr:\n        pca384: 0.1207\n        text: 0.2477\n        delta: -0.127\n        p: 0\n        reject: true\n      qwq_bal_acc:\n        pca384: 0.8116\n        text: 0.6504\n        delta: 0.1612\n        p: 0\n        reject: true\n      qwq_precision:\n        pca384: 0.608\n        text: 0.4213\n        delta: 0.1867\n        p: 0\n        reject: true\n      qwq_fpr:\n        pca384: 0.173\n        text: 0.2871\n        delta: -0.1141\n        p: 0.038\n        reject: false\n      r1_32b_bal_acc:\n        pca384: 0.7471\n        text: 0.6461\n        delta: 0.1011\n        p: 0.011\n        reject: true\n      r1_32b_precision:\n        pca384: 0.6343\n        text: 0.4503\n        delta: 0.184\n        p: 0.002\n        reject: true\n      r1_32b_fpr:\n        pca384: 0.2256\n        text: 0.3809\n        delta: -0.1553\n        p: 0.006\n        reject: true\n    pca_explained_variance:\n      r1_8b: 0.793\n      ot_7b: 0.828\n      qwq_32b: 0.881\n      r1_32b: 0.924\n    finding: 'Modality advantage persists at matched 384d dimensionality. 10/12 Holm-Bonferroni\n      reject. Precision gains +16.8 to +23.1pp across all 4 models. Two non-rejections:\n      R1-8B bal_acc (small delta 1.3pp) and QwQ FPR (raw p=0.038, adj threshold too\n      strict).'\n- exp_id: exp_safe_trace_fpr_multimodel\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    ot7b_hs_static_fpr: 0.111\n    ot7b_text_static_fpr: 0.302\n    ot7b_hs_temp_fpr: 0.175\n    ot7b_text_temp_fpr: 0.46\n    qwq_hs_static_fpr: 0.5\n    qwq_text_static_fpr: 0.325\n    qwq_hs_temp_fpr: 0.45\n    qwq_text_temp_fpr: 0.425\n    r1_32b_hs_static_fpr: 0.239\n    r1_32b_text_static_fpr: 0.31\n    r1_32b_hs_temp_fpr: 0.239\n    r1_32b_text_temp_fpr: 0.31\n- exp_id: exp_qwq_safe_fpr_correct_lr\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    hs_cv_acc: 0.935\n    hs_step_fpr: 0.279\n    hs_trace_fpr_k5: 0.475\n    text_cv_acc: 0.667\n    text_step_fpr: 0.394\n    text_trace_fpr_k5: 0.5\n- exp_id: exp_bge_large_text_comparison\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_hs_prec: 0.497\n    r1_8b_bge_prec: 0.436\n    r1_8b_diff: 0.058\n    r1_8b_p: 0.185\n    r1_8b_hb: false\n    ot_7b_hs_prec: 0.446\n    ot_7b_bge_prec: 0.263\n    ot_7b_diff: 0.181\n    ot_7b_p: 0\n    ot_7b_hb: true\n    r1_32b_hs_prec: 0.588\n    r1_32b_bge_prec: 0.475\n    r1_32b_diff: 0.117\n    r1_32b_p: 0.027\n    r1_32b_hb: false\n    qwq_32b_hs_prec: 0.545\n    qwq_32b_bge_prec: 0.454\n    qwq_32b_diff: 0.094\n    qwq_32b_p: 0.132\n    qwq_32b_hb: false\n    hb_pass_count: 1/4\n- exp_id: nested_cv_7_8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_mean_delta_prec: 0.174\n    r1_8b_std_delta_prec: 0.026\n    r1_8b_hs_better_folds: 5/5\n    ot_7b_mean_delta_prec: 0.164\n    ot_7b_std_delta_prec: 0.033\n    ot_7b_hs_better_folds: 5/5\n    total_hs_better: 10/10\n- exp_id: random_cp_qwq32b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    real_cp_cr_composite_layer: 4\n    real_cp_precision_layer: 63\n    real_cp_gap: 59\n    random_cp_cr_shallow_freq: 0.8\n    random_cp_precision_deep_freq: 0.2\n    metric_disagreement_replicates: false\n- exp_id: split_half_ot7b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    half1_cr_composite_layer: 0\n    half2_cr_composite_layer: 0\n    half1_precision_layer: 20\n    half2_precision_layer: 26\n    half1_delta_prec: 0.262\n    half2_delta_prec: 0.154\n    cr_composite_both_shallow: true\n    threshold_both_deep: true\n    delta_precision_same_direction: true\n    delta_ba_same_direction: true\n    all_checkpoints_pass: true\n- exp_id: sf3_quadratic_residual\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_linear_gap: 0.104\n    r1_8b_linear_p: 0.0001\n    r1_8b_linear_hb: true\n    r1_8b_quad_gap: 0.103\n    r1_8b_quad_p: 0.0001\n    r1_8b_quad_hb: true\n    ot_7b_linear_gap: 0.114\n    ot_7b_linear_p: 0.0001\n    ot_7b_linear_hb: true\n    ot_7b_quad_gap: 0.098\n    ot_7b_quad_p: 0.0003\n    ot_7b_quad_hb: true\n    r1_32b_linear_gap: -0.014\n    r1_32b_linear_p: 0.598\n    r1_32b_linear_hb: false\n    r1_32b_quad_gap: 0\n    r1_32b_quad_p: 0.499\n    r1_32b_quad_hb: false\n    qwq_32b_l60_w3_linear_gap: 0.074\n    qwq_32b_l60_w3_linear_p: 0.0017\n    qwq_32b_l60_w3_linear_hb: true\n    qwq_32b_l60_w3_quad_gap: -0.01\n    qwq_32b_l60_w3_quad_p: 0.6384\n    qwq_32b_l60_w3_quad_hb: false\n    note: QwQ corrected from layer_idx=63 to L60, W=3\n- exp_id: n6_multi_metric_ensemble\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    r1_8b_ensemble_prec: 0.565\n    r1_8b_best_single_prec: 0.604\n    r1_8b_text_prec: 0.372\n    r1_8b_ens_vs_text_gap: 0.193\n    ot_7b_ensemble_prec: 0.506\n    ot_7b_best_single_prec: 0.473\n    ot_7b_text_prec: 0.236\n    ot_7b_ens_vs_text_gap: 0.27\n    qwq_32b_ensemble_prec: 0.578\n    qwq_32b_best_single_prec: 0.578\n    qwq_32b_text_prec: 0.374\n    qwq_32b_ens_vs_text_gap: 0.203\n    r1_32b_ensemble_prec: 0.581\n    r1_32b_best_single_prec: 0.583\n    r1_32b_text_prec: 0.476\n    r1_32b_ens_vs_text_gap: 0.105\n    all_ens_vs_text_significant: true\n    ens_vs_text_p_max: 0.002\n    ens_never_worse_than_best_single: true\n    ot_7b_ens_beats_best_single: 0.033\n- exp_id: r1_8b_full_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_layers:\n      bal_acc:\n        W1: L12\n        W3: L12\n        W5: L12\n        W15: L11\n      precision:\n        W1: L16\n        W3: L12\n        W5: L12\n        W15: L9\n      fpr:\n        W1: L16\n        W3: L9\n        W5: L9\n        W15: L8\n      crossing_rate:\n        W1: L0\n        W3: L0\n        W5: L0\n        W15: L0\n      composite:\n        W1: L16\n        W3: L12\n        W5: L12\n        W15: L9\n    max_layer_gap_same_model: 16\n    hs_vs_text_gap: 0.15-0.17 stable across all layers\n    shallow_bias_W15_only: true\n    traces: 209\n    seed: 42\n- exp_id: advbench_r1_8b_full\n  name: ''\n  status: DONE\n  conclusion: failed\n  metrics: {}\n- exp_id: pca_artifact_verification\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    pca100d_best_precision: 0.633\n    nopca_best_precision: 0.732\n    pca100d_best_fpr: 0.145\n    nopca_best_fpr: 0.072\n    pca100d_best_composite: 0.43\n    nopca_best_composite: 0.803\n    pca100d_cr_best_layer: L0\n    nopca_best_layer_range: L9-L16\n    n_traces: 209\n- exp_id: advbench_llm_cp_annotation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: advbench_llm_cp_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen3_cp_dryrun\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen3_cp_dryrun2\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: qwen3_cp_full\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: gpt4omini-cp-annotation\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: advbench_phase4_layer_sweep\n  name: ''\n  status: DONE\n  conclusion: killed\n  metrics: {}\n- exp_id: random_cp_r1_8b\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    crossing_rate_random_mean_layer: 10.7\n    crossing_rate_random_shallow_pct: 0\n    precision_random_mean_layer: 0\n    precision_random_shallow_pct: 100\n    metric_disagreement_replicates: false\n    real_cp_cr_composite_layer: 0\n    real_cp_precision_layer: 23\n    real_cp_gap: 23\n    elapsed_s: 105.4\n\n\n## what_if (hypothetical experiments — additive)\n\n- name: ensemble_cv_7b\n  claim: C1 (layer selection bias mitigation)\n  description: 5-fold CV validation of multi-metric ensemble layer selection on 7-8B\n    models (R1-8B + OT-7B). Validates that ensemble eliminates metric-induced bias\n    under cross-validation, upgrading from preliminary to validated diagnostic guidance.\n  estimated_gpu_hours: 0.5\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T21:22:52.409Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:22:52.409Z",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-21T21:22:52.446Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "67c9347b-5a8d-477d-b560-16a7c0c620d2",
  "type": "user",
  "uuid": "a1719e1a-4cc8-4c7e-995d-4ea98e13281c",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:22:52.443Z_

```json
{
  "parentUuid": "a1719e1a-4cc8-4c7e-995d-4ea98e13281c",
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
  "uuid": "3913eebe-70f8-47fc-bef8-5a2150cc141b",
  "timestamp": "2026-05-21T21:22:52.443Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:22:52.443Z_

```json
{
  "parentUuid": "3913eebe-70f8-47fc-bef8-5a2150cc141b",
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
  "uuid": "eb15075b-15b0-4391-b785-fa92d76cf7da",
  "timestamp": "2026-05-21T21:22:52.443Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-21T21:22:52.443Z_

```json
{
  "parentUuid": "eb15075b-15b0-4391-b785-fa92d76cf7da",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9490037f-ac34-4826-82c4-3603062ddd66",
  "timestamp": "2026-05-21T21:22:52.443Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "9490037f-ac34-4826-82c4-3603062ddd66",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenarios for contrastive trace safety paper",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99"
}
```

---

### Assistant

_source line 9 · 2026-05-21T21:23:36.801Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the research project carefully to define three tiers of Dream simulation scenarios for this EMNLP 2026 submission on contrastive trace safety.

Key elements to consider:
1. The paper's core claims: layer selection metric sensitivity, HS advantage at correct layers, temporal improvement, negative results
2. Current state: 12/12 HB pass, 4 models, position mediation analysis done, 5-seed robustness done, BA-layer robustness done (16/16 HB), PCA control done (10/12 HB)
3. The focus question: does upgrading ensemble from preliminary to CV-validated move the needle? What other low-cost improvements matter?


4. For EMNLP 2026 Main versus Findings, I'm thinking through how the paper might be received: best case has all evidence holding up with the layer selection sensitivity recognized as novel and the comprehensive 4-model evaluation appreciated, landing in Main. The median scenario sees reviewers acknowledge the empirical work but question whether the 32B limitations and some negative results undermine the broader claims, pushing toward Findings.

In the worst case, reviewers might dismiss this as just hyperparameter tuning or argue the HS advantage is too modest given the caveats. I'm also considering whether the CV-validated ensemble results would strengthen the methodological contribution enough to shift outcomes between tiers. The key factors that'll determine reviewer reception are their scores, concerns about statistical validity, how they view the layer selection contribution, whether they see the 32B caveats as fatal to the claims, and whether they value the negative results as meaningful.

For the best-case scenario, reviewers would recognize layer selection sensitivity as a genuine methodological advance rather than just tuning, find the robustness across 12 HB and 16 BA-layer configurations compelling, accept that 4 models across 2 architectures and 2 scales provides sufficient breadth, appreciate the negative results as a community contribution, view the 32B caveats as honest science, and see the position mediation analysis as adequately addressing confound concerns. In the median case, the layer selection contribution gets seen as useful but not primary, with pushback on the R1-32B position-mediated advantage, the varying W values in the HB table, and small sample sizes at 32B—where ensemble CV might help but wouldn't be decisive.

For the worst case, the hyperparameter tuning critique gains traction, reviewers question whether the HS advantage is practically useful given the high false positive rates and negative lead times, find the linear probe results unsurprising, and view the small sample sizes (especially n=20 for R1-32B) as undermining statistical claims despite the HB corrections. I need to think through what reviewer scores and novelty/soundness ratings would look like across these scenarios, and how many of the typical three reviewers would actually champion the paper in each case.

Now I'm refocusing on the core question: does adding CV-validated ensemble results move the paper from Findings to Main acceptance, or is it just a marginal improvement? The tiers should really reflect how dream reviewers would evaluate the current state plus potential upgrades. For the best case, I'm imagining reviewers averaging 3.5-4.0 on a 5-point scale, where the layer selection sensitivity emerges as the main novelty contribution, and the CV-validated ensemble is a solid addition but not the deciding factor—the existing evidence around HB corrections, BA-layer consistency, and position mediation already makes a strong case.

In the median scenario, reviewers land around 3.0-3.5, appreciating the breadth and rigor but wanting more methodological depth. Here's where CV-validated ensemble could tip a borderline reviewer toward acceptance, though other fixes like clarifying practical implications and addressing the 32B limitations would also help push toward Main. For the worst case, I'm looking at 2.5-3.0 scores where the fundamental issue is that the method itself doesn't feel novel enough and the practical deployment concerns (especially the high false positive rate) make the impact questionable. The CV-validated ensemble wouldn't move the needle much here—instead, the paper might need repositioning as an evaluation framework or leaning into the negative results as the primary insight.

Now I'm writing the YAML output...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9490037f-ac34-4826-82c4-3603062ddd66",
  "isSidechain": false,
  "requestId": "req_011CbGR8KU3KTasjw2MKGmWq",
  "type": "assistant",
  "uuid": "590026d6-14a1-4798-b296-224b33a8b630",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THEQR42AAWmeao6ofY9EnW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 37076,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3210,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 37076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37076
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

_source line 10 · 2026-05-21T21:24:14.882Z_

```yaml
tiers:
  best:
    meaning: "Current evidence package (12/12 HB, 16/16 BA-layer, position mediation 3/4, 5-seed robustness, 6 negative methods) is already sufficient for Main. Layer selection sensitivity is recognized as a genuine methodological contribution distinct from hyperparameter tuning. CV-validated ensemble is cosmetic, not load-bearing."
    key_assumptions:
      - "Reviewers treat layer selection metric bias as a reproducible methodological finding (not 'you just picked the wrong hyperparameter')"
      - "4 models × 2 architectures × 2 scales is accepted as sufficient breadth for an empirical study"
      - "32B caveats (R1-32B W=1 only, QwQ negative lead time) are read as honest science, not evidence of fragility"
      - "Comprehensive negative results (BOCPD/CUSUM/Mahalanobis/RepE/CCS/MLP all fail) are valued as community service"
      - "Position mediation analysis (3/4 retain non-positional HS advantage) fully resolves confound concern"
      - "High safe FPR (39-62%) is acceptable as acknowledged limitation for a detection-evaluation paper"
    number_ranges:
      avg_reviewer_score: [3.5, 4.0]  # out of 5, ARR scale
      novelty_rating: [3.5, 4.0]
      soundness_rating: [4.0, 4.5]
      champions_out_of_3: [2, 3]
      ensemble_cv_impact_on_acceptance: [0.0, 0.05]  # near-zero marginal lift
      lowest_single_reviewer: [3.0, 3.5]
    narrative_direction: "Original framing fully intact. Primary contribution = layer selection sensitivity as researcher-degree-of-freedom audit. Secondary = HS advantage universal at correct layers. Tertiary = 6 methods fail. Paper title emphasizes 'layer selection matters' angle. Claims need no softening. Ensemble CV can go in appendix as supplementary validation."

  median:
    meaning: "Paper is borderline Main/Findings. Layer selection contribution is seen as 'useful observation' not 'methodological advance'. One reviewer flags practical impact (high FPR, QwQ timing). CV-validated ensemble helps marginally but the real gap is in framing clarity and addressing the 'so what for deployment' question."
    key_assumptions:
      - "At least one reviewer sees layer selection as 'just good practice' rather than a contribution — needs explicit framing as sensitivity analysis framework"
      - "R1-32B caveats (W=1 only significant, 25% coverage, position-mediated advantage) weaken the 'universal' claim enough that one reviewer downgrades"
      - "Different W per model in the 12/12 HB table is flagged as cherry-picking each model's best setting"
      - "High safe FPR (39-62%) is flagged as undermining deployment relevance — reviewer asks 'would anyone actually use this?'"
      - "Negative results are appreciated but not enough to carry the paper alone"
      - "Position mediation partially resolves confound but QwQ's competitive position baseline (0.746 > HS 0.740) bothers one reviewer"
    number_ranges:
      avg_reviewer_score: [3.0, 3.5]
      novelty_rating: [2.5, 3.5]
      soundness_rating: [3.5, 4.0]
      champions_out_of_3: [1, 2]
      ensemble_cv_impact_on_acceptance: [0.05, 0.12]  # small but nonzero — pushes one borderline reviewer
      lowest_single_reviewer: [2.5, 3.0]
    narrative_direction: "Soften 'universal HS advantage' to 'HS advantage robust at 7-8B, model-specific at 32B'. Elevate the systematic evaluation framework (4 models × 7 methods × 5 metrics) as the primary contribution over the HS-vs-text comparison itself. Add a 'practical deployment analysis' subsection: at what FPR threshold is monitoring useful, and which model-method combos meet it? CV-validated ensemble strengthens the 'principled layer selection' story but the real lift comes from (a) explicit uniform-W table alongside best-W table, (b) deployment-oriented discussion of when HS monitoring is worth the infrastructure cost. Findings acceptance likely; Main possible if AC weights breadth and rigor."

  worst:
    meaning: "Core premise challenged: 'HS outperforms text' is seen as either (a) unsurprising (hidden states have more info than text, obviously) or (b) not practically useful (high FPR, small absolute gains, deployment cost of hidden-state access). Layer selection sensitivity is dismissed as hyperparameter tuning. Paper needs fundamental reframing."
    key_assumptions:
      - "Reviewers frame the HS-vs-text comparison as 'trivially expected' — hidden states are a superset of information available to text"
      - "Method novelty rated insufficient: linear probes + temporal windows are standard; no new architecture or training procedure"
      - "Small sample sizes (R1-32B n=20, QwQ n=19-20) make the 32B claims unconvincing despite HB corrections — reviewer notes MDE analysis shows R1-32B residualized gap is underpowered"
      - "Safe FPR 39-62% is a dealbreaker for the deployment framing — 'a monitor that fires on half of safe traces is useless'"
      - "R1-32B being position-mediated + QwQ having negative HS lead time means 2/4 models have serious practical caveats, undermining breadth claims"
      - "One reviewer points out text probes require zero infrastructure change while HS probes need white-box access — the 15-24pp precision gain may not justify the engineering cost"
    number_ranges:
      avg_reviewer_score: [2.5, 3.0]
      novelty_rating: [2.0, 2.5]
      soundness_rating: [3.0, 3.5]
      champions_out_of_3: [0, 1]
      ensemble_cv_impact_on_acceptance: [0.0, 0.03]  # irrelevant to core concerns
      lowest_single_reviewer: [2.0, 2.5]
    narrative_direction: "Reframe away from 'HS beats text' toward one of two angles, both still targeting EMNLP Main: (A) **Negative-results-first framing**: 'We systematically evaluate 7 detection methods across 4 reasoning models and find that none achieves deployment-ready performance. The best approach (temporal HS probes) still has 39-62% safe FPR. We identify layer selection bias as a critical confounder and provide a sensitivity analysis framework.' This positions the paper as a cautionary benchmark. (B) **Methodology-first framing**: 'We discover that a commonly used layer selection metric systematically biases hidden-state evaluations, producing false negatives at scale. We demonstrate this across 4 models and 5 metrics, show it reverses published conclusions, and propose a multi-metric audit protocol.' This makes layer selection the headline and HS-vs-text becomes supporting evidence. Either angle requires: toning down deployment language, foregrounding limitations honestly, positioning as 'the field needs this evaluation before building on shaky foundations.' Add cost-benefit analysis (HS access cost vs marginal gain over text) to preempt the engineering-cost reviewer."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "590026d6-14a1-4798-b296-224b33a8b630",
  "isSidechain": false,
  "requestId": "req_011CbGR8KU3KTasjw2MKGmWq",
  "type": "assistant",
  "uuid": "439726bc-c473-4584-a9b3-b17baaf92c1c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_5",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01THEQR42AAWmeao6ofY9EnW",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 37076,
      "cache_read_input_tokens": 11447,
      "output_tokens": 3210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 37076,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 3210,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 37076,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 37076
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "439726bc-c473-4584-a9b3-b17baaf92c1c",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Define three scenarios for contrastive trace safety paper",
  "sessionId": "edabc97e-fd03-48b3-82cf-935ea08bdb99"
}
```

---
