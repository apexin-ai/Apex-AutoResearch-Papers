# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-2/9c94f57c-4ce2-468b-8638-fea3e33c2121.jsonl`
- **Structured JSON:** [`80bd6b73b0a346e83341.json`](../../sessions/80/80bd6b73b0a346e83341.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T23:17:14.859Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T23:17:14.859Z",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier\",\n  \"core_problem\": \"How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?\",\n  \"opportunity\": \"Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.\",\n  \"landscape\": \"The landscape of RL-based multimodal reasoning training has exploded in early 2026 along seven axes:\\n\\n**Perception-gating methods:** PEARL (CVPR 2026) derives a perception checklist of factual sub-questions, computes a perceptual reward R̄_p, and uses it as a fidelity gate — blocking reasoning policy updates when perception fails. Gains: +6.6% over GRPO on MathVerse. Limitation: checks perception accuracy but not whether perceived facts are correctly *bound* to reasoning steps or whether integration is *complete*. PaLMR (CVPR 2026, arXiv:2603.06652) introduces V-GRPO (Vision-Guided GRPO) with a hierarchical reward R = S_vis × (α·S_ans + (1−α)·S_fmt), where S_vis is a binary visual fidelity gate computed via pairwise comparison against pseudo ground-truth image descriptions generated by Gemini. Achieves 70.9% on HallusionBench (+4.2pp over GRPO) with only 4,728 training instances and 88% model-human alignment. Limitation: uses external pseudo ground-truth for comparison rather than verifying the model's own explicit evidence citations; does not check completeness; binary gating provides no gradient signal for partial fidelity improvement.\\n\\n**Token-level credit reallocation methods:** VPPO (ICLR 2026) reweights by KL divergence on perturbed images. PGPO (Apr 2026) amplifies learning signals for visually-dependent tokens via threshold-gated advantage reallocation (+18.7% avg). VGPO (ACL 2026) adds visual attention compensation. AT-RL (Feb 2026) identifies ~15% anchor tokens via cross-modality connectivity for targeted credit assignment (+1.2% overhead, 32B surpasses 72B-Instruct). VICRA (2026) reallocates optimization toward visually-grounded tokens (+2.25 avg on Qwen2.5-VL-7B). KAWHI (Mar 2026) performs paragraph-level credit reallocation via structured attribution of vision-critical attention heads. SAYO (Feb 2026) introduces region-level visual attention reward (r_v = tanh(log(a_q/v_q))) on Qwen3-VL-8B. Collective limitation: all operate on statistical attention patterns rather than verifying the semantic correctness of evidence-to-reasoning binding.\\n\\n**Explicit evidence grounding in RL training:** TreeVGR (ICLR 2026) trains models to generate text-space bounding box coordinates as traceable evidence within reasoning trajectories, supervised via dual IoU reward (R_IoU = ½(R_IoU^R + R_IoU^P)) that balances precision and recall of spatial localization. Two-stage training (SFT on 37K samples + RL). Achieves +16.8 on V*Bench, +12.6 on MME-RealWorld. Limitation: verifies *spatial* localization via IoU but not the *semantic validity* of how localized evidence is used in reasoning — a correct bounding box around a labeled angle does not verify that the angle value was correctly read or correctly applied in an inference step. Does not check integration completeness. v1 (May 2026, arXiv:2505.18842) introduces a point-and-copy mechanism where the model selects relevant image patches and copies their embeddings back into the reasoning stream, maintaining visual grounding throughout multi-step reasoning. Trained via SFT on v1g (300K grounding-annotated traces); RL integration is noted as future work. Achieves 68.6% MathVista, 34.5% MathVision. Limitation: operates at the embedding/representation level — re-inserts visual features but does not produce explicit textual evidence citations that can be externally verified for semantic correctness; grounding is implicit in the representation space rather than auditable. VTPerception-R1 (arXiv:2509.24776) implements a two-stage framework (perception-augmented SFT + perception-aware RL) with three perception rewards: visual key-info coverage (R_vkey), textual key-info coverage (R_tkey), and consistency (R_cons = |F_ans∩E|/max(1,|F_ans|)). Achieves 82.5% AI2D, 71.0% MathVista. Limitation: R_vkey measures perception-level element coverage (are visual elements mentioned?) but does not verify binding validity (are inferences logically consistent with cited evidence?) or integration completeness (are all task-relevant facts addressed?). SIEVE (arXiv:2603.14117) trains models to iteratively re-access cached visual region embeddings during RL (GRPO with ℛ = λ₁ℛ_res + λ₂ℛ_format + λ₃ℛ_emb + λ₄ℛ_act), supporting multi-turn evidence refinement. Achieves +7.85 on V*Bench overall. Limitation: like v1, operates at the embedding level — re-inserted features improve grounding but don't produce explicit verifiable citations; iterative re-access addresses the evidence-loss problem but not semantic verification of how evidence supports conclusions.\\n\\n**Self-rewarding perception-reasoning decomposition:** Vision-SR1 (arXiv:2508.19652) decomposes reasoning into explicit &lt;visual_perception> and &lt;think> stages, requiring the model to first articulate a self-contained visual description, then reason from it. The visual reward is computed via self-rewarding: the frozen policy model is re-prompted to answer the question using only the generated visual perception text (without image access); if the correct answer is derived from perception alone, a visual reward of 1 is assigned. Uses GRPO with a decoupled reward-advantage framework that maintains separate advantages for visual and answer rewards. Three-stage training: SFT cold-start on 9K examples, then standard rollout with accuracy reward, then self-reward rollout. Achieves 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B (+1.4 over Vision-R1), 69.8 on HallusionBench. Key distinction from CFRL: (a) Vision-SR1 uses self-rewarding (same model judges itself) rather than an external distilled verifier — the reward is whether perception suffices to re-derive the answer, not whether each cited fact is *factually accurate* relative to the image; a hallucinated but internally consistent perception could score high. (b) Vision-SR1 checks perceptual *self-containment* (can you answer from perception alone?) while CFRL checks factual grounding accuracy (is the perception correct?), binding validity (does the inference follow from cited evidence?), and completeness (are all task-relevant facts covered). (c) Vision-SR1 does not verify the logical consistency between perceived evidence and drawn inferences — it treats perception and reasoning as decomposed stages but does not check whether the reasoning is faithful to the specific evidence cited.\\n\\n**Constrained/faithful training methods:** FGRPO (Apr 2026, arXiv:2604.08476) enforces consistency + semantic grounding + spatial grounding as constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7% and improving grounding by +13 points. Uses Qwen3-VL-30B-A3B-Instruct (MoE, ~3.3B active parameters) as the online judge during training. The semantic grounding reward R_S requires per-sentence VLM judge calls: each non-trivial visual sentence in the CoT is independently evaluated, resulting in ~30-55 judge calls per training sample. This is the closest competitor — but does not check integration completeness. Faithful-MR1 (May 2026) supervises a &lt;Focus> token's attention against image regions and uses counterfactual image intervention to reward attention concentration where vision causally matters. Operates on attention distributions rather than explicit evidence citations.\\n\\n**Structured verification and evaluation judges:** MJ1 (Mar 2026, arXiv:2603.07990) trains a 3B-active-parameter multimodal judge (based on Qwen3-VL-30B-A3B) using RL with a structured grounded verification chain: observations → claims → verification → evaluation → scoring, enforced via 11 required XML tags across 5 sequential stages. Achieves 77.0% on MMRB2, surpassing GPT-5 (72.2%) and Gemini-3-Pro (76.3%). Key distinction from CFRL: (a) MJ1 is an *evaluation-time* judge, not a training-time reward verifier; (b) MJ1 uses stage-separated grounding rather than inline evidence citations; (c) MJ1 performs pairwise response comparison, not composition property verification; (d) MJ1 does not check integration completeness. EVPV/Grounding the Score (Mar 2026) adds visual premise verification via constraint matching and reliability gating to PRMs — improves Best-of-N reranking but is *inference-only*. ViGoRL (2026) trains models to produce spatially grounded reasoning traces with coordinate-level evidence (86.4% on V*Bench) — addresses spatial grounding but not semantic binding validity. AutoRubric-R1V (arXiv:2510.14738) auto-generates rubric-based process rewards by distilling consistent reasoning checkpoints from successful trajectories via self-aggregation — rubric reward equals the fraction of satisfied checkpoints. Achieves +8.0 avg over Qwen2.5-VL-7B on 6 benchmarks. Distinct from CFRL: AutoRubric derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image; rubrics are answer-path-dependent rather than evidence-grounding-dependent. CoRGI (arXiv:2508.00378) performs post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal.\\n\\n**Evidence-aware GRPO variants:** PRCO (Mar 2026) decomposes into Observer+Solver with separate utility/outcome rewards (+7 pts). DocR1 (2026) uses evidence-page guided GRPO for document understanding. OpenMMReasoner (CVPR 2026) achieves +11.6% over Qwen2.5-VL-7B via two-stage SFT+RL recipe.\\n\\n**Attribution and evidence-loss diagnostics:** MuRGAt (Feb 2026, arXiv:2602.11509) introduces a benchmark for multimodal fact-level attribution requiring models to generate explicit citations specifying modality and temporal segments. Critically, MuRGAt finds that 'increasing reasoning depth or enforcing structured grounding often degrades accuracy' in zero-shot/few-shot settings — even strong MLLMs frequently hallucinate citations despite correct reasoning. This documents an accuracy-faithfulness tradeoff that CFRL must address. 'Don't Blink: Evidence Collapse during Multimodal Reasoning' (Apr 2026, arXiv:2604.04207) documents that reasoning VLMs progressively lose visual grounding as reasoning unfolds — attention to annotated evidence regions drops >50% — creating confident but ungrounded predictions that text-only monitoring cannot detect. 'Deeper Thought, Weaker Aim' (Mar 2026, arXiv:2603.14184) independently confirms this, showing reasoning prompts significantly reduce attention to question-critical image regions. 'Compose and Fuse' (ICLR 2026) identifies task-composition and fusion as main barriers. MathLens (Feb 2026) shows integration failures grow as a fraction of remaining errors. The PAR framework (Mar 2026) decomposes multimodal math reasoning into Perception–Alignment–Reasoning and identifies alignment fragmentation as a distinct failure mode.\\n\\n**The gap:** PEARL and PaLMR check perception but not binding or completeness; FGRPO checks consistency+grounding but not completeness, with ~5-8x higher cost per rollout vs. single-pass verification; Vision-SR1 decomposes perception and reasoning with self-rewarding but does not verify factual grounding accuracy, binding validity, or completeness; TreeVGR and ViGoRL verify spatial localization but not semantic reasoning validity; v1 and SIEVE re-access visual evidence at the embedding level but don't produce auditable textual citations; VTPerception-R1 checks perception-level coverage but not binding validity or completeness; MJ1 demonstrates structured grounded verification chains but operates at evaluation time; AutoRubric-R1V provides process supervision via trajectory-mined rubrics but not composition property verification against the image; CoRGI performs step-wise visual verification but is inference-only; attention-based methods (PGPO, SAYO, AT-RL, Faithful-MR1) use statistical proxies; EVPV is inference-only. No existing method unifies all three composition properties (evidence grounding, binding validity, integration completeness) in a single lightweight training-time verifier. MuRGAt's accuracy-faithfulness tradeoff highlights that naive enforcement of structured citation degrades performance — but this was observed under zero-shot prompting, not RL training with curriculum scheduling.\",\n  \"inspired_by\": \"'Compose and Fuse' (ICLR 2026) explicit future direction for composition-aware training; MathLens integration-failure analysis; PAR framework's alignment decomposition; FGRPO's grounding+consistency insight (extended with completeness and efficiency); MJ1's structured verification chain (adapted from evaluation-time judge to training-time reward); PaLMR's visual fidelity gating (extended beyond binary gating to multi-property verification); TreeVGR's explicit evidence generation in RL (extended from spatial to semantic verification); v1's interleaved grounding paradigm (adapted from embedding-level to textual-citation-level); Vision-SR1's perception-reasoning decomposition with self-rewarding (extended from self-containment checking to external factual grounding + binding + completeness verification); MuRGAt's accuracy-faithfulness tradeoff (motivating curriculum training and accuracy-first reward scheduling); 'Don't Blink' and 'Deeper Thought, Weaker Aim' documenting evidence collapse (direct motivation for explicit evidence anchoring); 'An Imperfect Verifier is Good Enough' (Apr 2026) validating noisy-reward robustness for distilled verifiers; GeoSketch's symbolic reward for geometry; Geoparsing (Apr 2026) for formal diagram entity extraction; Chart-RVR's verifiable chart reasoning rewards (informing chart-domain binding checks); CHARGE's keypoint coverage metrics; Countdown-Code (2026) and PURE (2025) for reward hacking diagnosis and mitigation\",\n  \"approach\": \"We propose Composition Fidelity RL (CFRL), which unifies evidence grounding, binding validity, and integration completeness verification in a single distilled composition verifier used as a GRPO training reward.\\n\\n**Structured output format:** The model generates responses with explicit &lt;observe entity='...' value='...'/> tags for visual evidence extraction and &lt;reason evidence='obs1,obs2' rule='...'> blocks for each reasoning step, requiring citation of specific observations and the inference rule applied. This explicit citation format enables automated verification — unlike attention-based methods that can only measure statistical dependency, or embedding-level methods (v1, SIEVE) that re-access visual features without producing auditable textual claims. Compared to TreeVGR's bounding-box coordinates, our citations capture *semantic* content ('radius = 5cm') rather than *spatial* location ([x1,y1,x2,y2]), enabling verification of whether the cited value is correct and whether the inference logically follows. Compared to MJ1's stage-separated verification chain, our format embeds evidence references *inline* with reasoning, creating direct referential links suitable for training-time throughput. Compared to Vision-SR1's &lt;visual_perception> block, our format provides *fine-grained, per-fact citations* (individual &lt;observe> tags) rather than a monolithic perception paragraph, enabling per-fact grounding verification and explicit evidence-to-inference linking via the evidence='obs1,obs2' attribute.\\n\\n**Addressing the accuracy-faithfulness tradeoff (MuRGAt):** MuRGAt (Feb 2026) found that enforcing structured grounding degrades accuracy in zero-shot/few-shot settings — models hallucinate citations despite correct reasoning. This is a direct challenge to CFRL's premise. We address it through four design choices: (1) *RL training develops citation as a learned skill*: unlike MuRGAt's zero-shot evaluation where citation is an imposed constraint, CFRL trains the model to produce faithful citations through reward optimization, allowing the model to develop integrated reasoning-citation capability rather than retrofitting citations onto existing reasoning. (2) *Accuracy-first curriculum scheduling*: Phase 0 (pre-curriculum) establishes answer accuracy via standard GRPO before introducing any citation requirements, ensuring the model's reasoning capability is preserved before grounding constraints are layered on. Citation rewards are introduced gradually with initial weight near zero, increasing only as the model demonstrates stable accuracy. (3) *Accuracy-dominant reward weighting*: R_accuracy receives weight α ≥ 0.4 throughout training, ensuring citation quality never dominates at the expense of answer correctness. If accuracy on a held-out validation set drops >2pp at any curriculum transition, citation reward weights are halved until accuracy recovers. (4) *Counterfactual validation* (safeguard #5) directly monitors for MuRGAt-style degradation by comparing tagged vs. untagged accuracy.\\n\\n**Composition Fidelity Verifier (CFV) — three-property checking:**\\n(1) *Evidence grounding*: Checks whether cited visual facts (in &lt;observe> tags) correspond to actual image content. Uses a lightweight visual QA module that converts each citation into a yes/no visual question (e.g., 'Is the radius labeled as 5cm in the image?'). Inspired by PEARL's perception checklist but applied to model-generated citations rather than externally-derived sub-questions.\\n(2) *Binding validity*: Checks logical consistency between cited evidence and the inference drawn. We define binding validity checks at two levels:\\n\\n  **Tier 1 — Domain-agnostic arithmetic + geometry symbolic (core contribution):**\\n  - *Arithmetic verification* (all domains): Given numerical values extracted from &lt;observe> tags and a stated operation in the &lt;reason> block, verify computational correctness via symbolic execution. Concrete checks: (a) *Sum/difference/product/quotient consistency* — if obs1 cites 'value A = 45' and obs2 cites 'value B = 30', and the reason block claims 'difference = 15' with rule 'subtraction', verify 45−30=15. (b) *Ratio/percentage verification* — if 'Part = 120, Total = 400' and conclusion is '30%', verify 120/400=0.30. (c) *Comparison consistency* — if the reason block claims 'A > B' citing obs1 (A=45) and obs2 (B=30), verify 45>30. (d) *Multi-step arithmetic* — chain verification across sequential &lt;reason> blocks where one step's output is another's input. These checks are domain-agnostic: they apply equally to geometry problems (angle computations), chart problems (bar value comparisons, trend calculations), and diagram problems (counting, distance computations).\\n  - *Geometry symbolic theorem matching*: Cited theorems/rules are matched against a geometry theorem library, and symbolic constraints are verified formally. For example, cited 'angle A=60°, angle B=90°' with rule 'triangle angle sum' → verify 60+90+x=180 → x=30°. Inspired by GeoSketch and the PAR framework.\\n\\n  **Tier 2 — Domain-specific binding checks (extension):**\\n  - *Chart-specific*: (a) *Ordering consistency* — if 'Bar A > Bar B' is cited, verify against the extracted data table that value(A) > value(B). (b) *Extrema verification* — if 'X is the maximum value' is cited, verify X = max(all values in series). (c) *Trend verification* — if 'increasing from 2020 to 2023' is cited, verify monotonic increase in the relevant data points; trends are formally defined as: 'increasing' requires each successive value ≥ previous (strict: >), 'decreasing' requires ≤ (strict: <), with tolerance ε for noise. (d) *Aggregation verification* — if 'average = X' is cited, verify mean(values) ≈ X within 1% relative tolerance. These checks require the chart data table extracted in the completeness pipeline (Stage A), linking Tier 2 binding to Tier 2 completeness infrastructure.\\n  - *Diagram-specific*: (a) *Structural relationship verification* — if 'A connects to B' is cited, verify edge (A,B) exists in the parsed graph from PGDP-Net. (b) *Attribute consistency* — if 'node A is labeled X' is cited, verify label(A) = X in the parsed representation. (c) *Cardinality verification* — if 'A has 3 connections' is cited, verify degree(A) = 3. (d) *Containment/hierarchy* — if 'A is inside B' is cited, verify the containment relation in the parsed spatial layout. These checks require the diagram graph representation from Stage A parsing.\\n  - *Fallback for inapplicable checks*: When a &lt;reason> block involves qualitative reasoning that cannot be reduced to arithmetic or structural constraint checking (e.g., 'the diagram suggests a causal relationship between X and Y'), the binding check returns a neutral score (0.5) rather than penalizing, and the verifier flags it as 'unverifiable-binding' for monitoring. This prevents the binding reward from penalizing valid qualitative reasoning while maintaining signal for verifiable steps.\\n\\n(3) *Integration completeness*: Checks whether all task-relevant visual facts are cited somewhere in the reasoning chain via a three-stage domain-specific pipeline:\\n\\n  **Stage A — Visual Element Enumeration** (domain-specific, offline or cached):\\n  - *Geometry*: Use Geoparsing (arXiv:2604.11600, Apr 2026) to produce a formal entity/relation set from the diagram. Geoparsing achieves 96.4 F1 overall (points 99.6, lines 98.0, circles 98.3, semantics 90.7) using a unified formal language.\\n  - *Charts*: Use DePlot/UniChart-style chart derendering to extract a linearized data table of all data points, then apply CHARGE-style keypoint extraction to convert to self-contained factual statements.\\n  - *Diagrams*: Use PGDP-Net-style graph parsing to extract a node-edge representation of diagram primitives and their relations.\\n\\n  **Stage B — Question-Conditioned Relevance Filtering**:\\n  - Apply VisDoT-style (arXiv:2603.11631) question decomposition to generate ordered perception sub-questions. Match sub-questions against enumerated visual elements from Stage A to produce a *required visual fact set* F_required.\\n  - Reliability estimate: Sub-question coverage as a ranking metric achieves 82% accuracy against human preferences (arXiv:2410.15531), with human inter-annotator agreement of 74.6% on sub-question classification — indicating this is an inherently noisy signal, which motivates our soft treatment of completeness (see below).\\n  - For geometry, the symbolic checker provides an additional signal: any entity appearing in the formal solution path is automatically added to F_required.\\n\\n  **Stage C — Coverage Verification**:\\n  - Compute coverage score: R_completeness = |F_cited ∩ F_required| / |F_required|.\\n  - We target ≥80% recall of task-relevant facts, acknowledging that completeness checking is inherently approximate. The 80% threshold is motivated by CHARGE's finding that even SOTA MLLMs achieve only 73.9% coverage with ground-truth retrieval.\\n  - For facts in F_required that are NOT cited, the verifier generates a soft penalty proportional to the estimated importance of the missing fact.\\n\\n**Verifier architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass. The input consists of the image + the model's full tagged response + a structured verification instruction. The CFV generates verification judgments sequentially as autoregressive output: for each &lt;observe> tag, it produces an inline grounding verdict (verified/unverified with confidence score); for each &lt;reason> block, it produces a binding validity verdict; and finally, it produces an overall completeness assessment. This is architecturally identical to how MJ1 generates its multi-stage verification chain in one forward pass — the grounding VQA for each observation is performed as internal sub-reasoning within the autoregressive generation, NOT as separate VQA calls. The output length scales with the number of observations and reasoning steps (~500-1500 tokens for typical responses with 4-8 observations), but requires only a single image encoding through the vision encoder.\\n\\n**Cost comparison with FGRPO (precise):** FGRPO requires S separate judge calls per rollout (S ≈ 5-8 visual sentences), each requiring its own image encoding through the 30B MoE model (3.3B active parameters). CFRL requires 1 verifier call per rollout with a single image encoding through the 4B dense model. Since image encoding is the dominant cost in VLM inference (processing hundreds of visual tokens through transformer layers), the savings from 1 vs. S encodings is the primary cost driver. Per-call text generation cost is roughly comparable: FGRPO generates S × ~150 = 750-1200 tokens total across all calls; CFRL generates ~500-1500 tokens in one call, at similar active parameter counts (3.3B MoE vs. 4B dense). The effective cost reduction is **~5-8x per rollout** (proportional to S), driven primarily by the single image encoding. Per training sample with K rollouts, FGRPO makes K×S judge calls vs. CFRL's K verifier calls — the same ~5-8x ratio holds. For Tier 1 (grounding + binding only), where binding validity uses lightweight symbolic/arithmetic checking outside the verifier, the verifier output is shorter (~300-800 tokens), further reducing per-call cost.\\n\\n**Staged contribution and risk mitigation (addressing system complexity):** The full CFRL system integrates multiple external tools and domain-specific pipelines, creating compounding failure risk. We structure the contribution in two defensible tiers:\\n\\n  *Tier 1 — Core contribution (grounding + binding):* Evidence grounding (VQA-based, all domains) and binding validity (domain-agnostic arithmetic verification + geometry symbolic theorem matching). This tier requires only the distilled 4B verifier and a geometry theorem library — no external parsing tools. Domain-agnostic arithmetic verification applies to chart and diagram problems too (any reasoning step involving numerical computation is checkable), providing cross-domain binding signal even without domain-specific infrastructure. This tier is self-contained, already differentiates from all existing methods (none verify binding validity as a training reward), and provides a defensible paper even if completeness checking and domain-specific binding prove too approximate. Estimated complexity: 1 distilled model + 1 theorem library.\\n\\n  *Tier 2 — Extension (completeness + domain-specific binding):* Integration completeness adds Geoparsing, DePlot/CHARGE, PGDP-Net, and VisDoT-style decomposition. Domain-specific binding for charts adds data-table-dependent checks (ordering, trends, extrema); for diagrams adds graph-dependent checks (structural relationships, attributes). Each integration is a potential failure point. Fallback strategies per component: (a) If Geoparsing underperforms on out-of-distribution diagrams, fall back to the distilled verifier's own visual element listing (lower accuracy but zero external dependency). (b) If relevance filtering is too noisy, use only the symbolic solver's required entities (geometry) or question-mentioned entities (charts/diagrams) as F_required — a conservative underestimate that still provides signal. (c) If domain-specific binding checks add noise rather than signal (e.g., trend verification on noisy data), fall back to Tier 1 arithmetic-only binding for that domain. (d) If end-to-end completeness R_completeness adds noise rather than signal, set δ=0 and report Tier 1 results as the core finding.\\n\\n  *Risk matrix:*\\n  - Pipeline integration failure (MEDIUM risk): Mitigated by Tier 1/Tier 2 separation and per-component fallbacks.\\n  - Verifier distillation quality (LOW risk): Validated via held-out test set; noise tolerance demonstrated by 'Imperfect Verifier' methodology.\\n  - Accuracy-faithfulness tradeoff (MEDIUM risk): Mitigated by accuracy-first curriculum, accuracy-dominant reward weighting, and counterfactual monitoring (see MuRGAt discussion above).\\n  - Tag gaming / Goodhart effects (LOW-MEDIUM risk): Mitigated by five anti-gaming safeguards (see below).\\n  - Training instability from 5 reward components (MEDIUM risk): Mitigated by curriculum scheduling (components introduced sequentially, not simultaneously) and reward weight monitoring.\\n\\n**Verifier distillation:** The CFV is distilled from Qwen3-VL-235B-A22B on synthetically generated composition judgment pairs. We generate correct/incorrect binding examples by: (a) taking model solutions, (b) perturbing citations (wrong entity, wrong value, missing citation, irrelevant citation, logically inconsistent inference, arithmetic errors), (c) having the teacher label each perturbation type. Target: 50K examples across geometry, chart, and diagram domains, with balanced representation of arithmetic binding errors (Tier 1) and domain-specific binding errors (Tier 2). The distilled verifier (based on Qwen3-VL-4B) is validated on a held-out test set of 5K human-annotated composition judgments.\\n\\n**Verifier validation protocol**: Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with Tier 1 binding validated separately for arithmetic and geometry-symbolic components, (b) ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on binding validity falls below 75%, we activate the fallback: softening binding rewards to a probabilistic consistency score weighted by verifier confidence.\\n\\n**Anti-gaming safeguards** (addressing Goodhart's Law risk):\\n  (1) *Low format weight*: Format compliance ≤0.05 in composite reward. Dominant signals come from verifiable content-level checks.\\n  (2) *Verifiable citation grounding*: Evidence grounding is checked against actual image content via visual QA — un-gameable.\\n  (3) *Answer-leak detection*: Embedding cosine similarity monitoring between &lt;observe> content and final answer, with penalty P_leak.\\n  (4) *KL regularization against base policy*: Standard KL penalty + format/content reward ratio monitoring; divergence triggers early stopping.\\n  (5) *Counterfactual validation*: Every 500 steps, evaluate with tags stripped. If tagged accuracy exceeds untagged by >5pp, signal format-dependent performance and trigger reward recalibration.\\n\\n**Training:** GRPO on Qwen3-VL-8B via veRL with composite reward R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness + ε·R_format − P_leak. Curriculum training: Phase 0 establishes baseline accuracy (week 1), Phase 1 trains grounding (weeks 1.5-2.5), Phase 2 adds binding validity (weeks 2.5-3.5), Phase 3 adds completeness (weeks 3.5-4.5). Training targets geometry (MathVerse, GeoQA+), chart (ChartQA, PlotQA), and diagram (AI2D, ScienceQA) tasks.\\n\\n**Key distinction from Vision-SR1:** Vision-SR1 decomposes reasoning into &lt;visual_perception> and &lt;think> stages and checks perceptual self-containment via self-rewarding — re-prompting the model without image access to verify the perception suffices. CFRL differs in three ways: (a) CFRL uses an external distilled verifier rather than self-rewarding — self-rewarding cannot detect hallucinated perceptions that happen to be internally consistent (a fabricated but plausible description could still support the correct answer), while external grounding verification checks each cited fact against the actual image. (b) CFRL provides fine-grained per-fact citations (&lt;observe> tags) rather than a monolithic perception block, enabling per-fact grounding verification and explicit evidence-to-inference linking. (c) CFRL verifies binding validity (does the inference logically follow from cited evidence?) and integration completeness, which Vision-SR1 does not address.\\n\\n**Key distinction from TreeVGR:** TreeVGR generates bounding-box coordinates as evidence and supervises spatial localization via dual IoU reward — verifying *where* the model attends. CFRL generates semantic textual citations and verifies *what* the model claims to see and *how* it reasons from those claims. These are complementary: TreeVGR could locate the correct region but misread the value; CFRL catches such semantic errors. TreeVGR does not check binding validity or integration completeness.\\n\\n**Key distinction from v1 and SIEVE:** Both re-access visual evidence at the embedding level — v1 via point-and-copy of patch embeddings, SIEVE via cached region embedding re-insertion. This maintains visual grounding in the model's internal representation but does not produce *explicit, auditable textual claims* about what was perceived. CFRL requires the model to articulate its visual evidence in natural language, enabling external verification of both the perception (grounding) and the reasoning (binding validity). v1 uses SFT only; SIEVE uses RL but without composition-level verification.\\n\\n**Key distinction from VTPerception-R1:** VTPerception-R1's R_vkey/R_tkey rewards check perception-level element coverage (whether visual/textual elements are mentioned in reasoning), while R_cons checks entity-attribute consistency. CFRL goes further in two ways: (a) binding validity checks logical inference consistency, not just entity-mention consistency, and (b) integration completeness checks coverage of all task-relevant facts via structured enumeration, not just key-info recall from a VLM scorer.\\n\\n**Key distinction from FGRPO:** FGRPO uses Qwen3-VL-30B-A3B-Instruct as per-sentence online judge, resulting in ~30-55 judge calls per training sample. Our single-pass CFV reduces this to ~K calls per sample (one per rollout), yielding ~5-8x cost reduction driven by single image encoding per rollout vs. S encodings. More importantly, CFRL adds completeness checking. FGRPO uses Lagrangian dual ascent; we use direct reward weighting with curriculum scheduling.\\n\\n**Key distinction from PaLMR:** PaLMR's V-GRPO uses binary visual fidelity gate (S_vis ∈ {0,1}) providing no gradient for partial improvement. CFRL provides continuous, multi-property reward signals. PaLMR does not require or verify explicit evidence citations.\\n\\n**Key distinction from MJ1:** MJ1 is evaluation-time judge with 5-stage pipeline (up to 6144 tokens). CFRL adapts structured verification to training-time with compact inline citations. CFRL checks completeness, which MJ1 does not.\\n\\n**Key distinction from PEARL:** PEARL checks perception accuracy of externally-generated sub-questions. CFRL checks grounding, validity, and completeness of the model's own explicit evidence citations.\\n\\n**Key distinction from AutoRubric-R1V:** AutoRubric-R1V provides process supervision by mining rubric checkpoints from successful trajectories — it checks whether the model's reasoning path conforms to patterns found in correct solutions. CFRL instead verifies composition properties against the image itself: whether cited evidence is factually grounded, inferences are valid, and coverage is complete. These are complementary: AutoRubric rewards path conformity, CFRL rewards evidence fidelity.\\n\\n**Key distinction from attention-based methods (PGPO, SAYO, Faithful-MR1):** These measure statistical attention patterns. CFRL requires and verifies explicit semantic citation.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"950 (verifier distillation: 100h on 4xH100; Geoparsing/DePlot integration and symbolic checker development: 80h; completeness pipeline development: 70h; main GRPO training: 400h on 8xH100; ablations including verifier accuracy sweep, anti-gaming validation, and baselines: 300h)\",\n      \"timeline\": \"10 weeks (1.5w setup + data + completeness pipeline + symbolic checker, 1.5w verifier training + validation, 3w main experiments with curriculum, 2.5w ablations + verifier accuracy study + anti-gaming analysis, 1.5w analysis and writing — overlapping phases)\",\n      \"estimated_gpu_cost\": \"$1,250 (H100 spot at ~$1.30/GPU-hr on Spheron/RunPod 2026 rates)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"950 (same experimental requirements)\",\n      \"timeline\": \"8 weeks (Claude accelerates verifier data generation, completeness pipeline scaffolding, experiment analysis)\",\n      \"claude_api_cost\": \"$300 (code assistance, composition judgment labeling assistance, completeness annotation, paper drafting)\",\n      \"estimated_gpu_cost\": \"$1,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1500 (additional hyperparameter sweeps for α/β/γ/δ/ε, verifier architecture search, verifier accuracy noise ablation, completeness pipeline ablation per domain, anti-gaming validation suite, extended baselines including PEARL+FGRPO+PaLMR+TreeVGR+Vision-SR1 reimplementation, symbolic checker coverage expansion)\",\n      \"timeline\": \"7 weeks (parallelized experiment scheduling, automated verifier validation)\",\n      \"claude_api_cost\": \"$1,000 (teacher labeling for verifier data: $600 for ~50K composition judgments via Qwen3-VL-235B; completeness annotation for chart/diagram domains: $100; experiment orchestration, analysis, and ablation design: $300)\",\n      \"estimated_gpu_cost\": \"$1,950\",\n      \"speed_bottleneck\": \"Verifier data generation requires teacher model (Qwen3-VL-235B) inference at ~50K examples; Geoparsing inference for geometry completeness pipeline; verifier validation requires human-annotated held-out set (5K examples); GRPO rollout reward evaluation is sequential per batch; curriculum phasing requires sequential training stages; anti-gaming counterfactual validation adds ~10% overhead per checkpoint\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated late Sep 2026, ~17 weeks from now — primary target with sufficient buffer for experiments + writing)\",\n    \"AAAI 2027 (abstract: Jul 21, paper: Jul 28, 2026 — stretch goal, 8 weeks with zero buffer; feasible only with aggressive parallelization and if verifier distillation completes in week 2)\",\n    \"CVPR 2027 (estimated ~Nov 2026, not yet announced — fallback if additional ablations needed)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Compose and Fuse: Revisiting the Foundational Bottlenecks in Multimodal Reasoning (ICLR 2026)\",\n    \"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning [PEARL] (CVPR 2026)\",\n    \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment [V-GRPO] (CVPR 2026, arXiv:2603.06652)\",\n    \"MJ1: Multimodal Judgment via Grounded Verification (arXiv:2603.07990, Mar 2026)\",\n    \"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv Mar 2026)\",\n    \"Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization [FGRPO] (arXiv:2604.08476, Apr 2026)\",\n    \"Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention (arXiv May 2026)\",\n    \"TreeVGR: Traceable Evidence Enhanced Visual Grounded Reasoning (ICLR 2026, arXiv:2507.07999)\",\n    \"v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv:2505.18842, May 2026)\",\n    \"VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding (arXiv:2509.24776)\",\n    \"SIEVE: Improving Visual Reasoning with Iterative Evidence Refinement (arXiv:2603.14117, Mar 2026)\",\n    \"Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization (arXiv:2508.19652)\",\n    \"AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning (arXiv:2510.14738)\",\n    \"CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv:2508.00378)\",\n    \"MuRGAt: Multimodal Fact-Level Attribution for Verifiable Reasoning (arXiv:2602.11509, Feb 2026)\",\n    \"Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv:2604.04207, Apr 2026)\",\n    \"Deeper Thought, Weaker Aim: Understanding and Mitigating Perceptual Impairment during Reasoning in MLLMs (arXiv:2603.14184, Mar 2026)\",\n    \"Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models [PGPO] (arXiv Apr 2026)\",\n    \"Credit Where It is Due: Cross-Modality Connectivity Drives Precise RL for MLLM Reasoning [AT-RL] (arXiv Feb 2026)\",\n    \"Don't Lose Sight: Visually-Grounded Credit Assignment for Multimodal Reasoning [VICRA] (2026)\",\n    \"Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs [SAYO] (arXiv Feb 2026)\",\n    \"Grounded Reinforcement Learning for Visual Reasoning [ViGoRL] (arXiv 2026)\",\n    \"What MLLMs Learn about When they Learn about Multimodal Reasoning [MathLens] (arXiv 2026)\",\n    \"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)\",\n    \"Deconstructing Multimodal Mathematical Reasoning: Towards a Unified Perception-Alignment-Reasoning Paradigm [PAR] (arXiv Mar 2026)\",\n    \"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv Apr 2026)\",\n    \"GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025/2026)\",\n    \"Geoparsing: Unified Formal Language for Geometry Diagram Parsing (arXiv:2604.11600, Apr 2026)\",\n    \"Benchmarking Multimodal RAG through a Chart-based Document Question-Answering Generation Framework [CHARGE] (arXiv:2502.14864, 2025)\",\n    \"DePlot: One-shot Visual Language Reasoning by Plot-to-Table Translation (2023)\",\n    \"VisDoT: Decomposition of Thought with Visual Interpretation Grounding (arXiv:2603.11631, Mar 2026, EACL 2026 Findings)\",\n    \"Countdown-Code: A Testbed for Reward Hacking in RLVR (arXiv:2603.07084, Mar 2026)\",\n    \"PURE: Pessimistic Unbiased Reward Estimation for RL with Noisy Rewards (arXiv:2504.15275, NeurIPS 2025)\",\n    \"Spotlight on Token Perception for Multimodal Reinforcement Learning [VPPO] (ICLR 2026)\",\n    \"Visually-Guided Policy Optimization for Multimodal Reasoning [VGPO] (ACL 2026)\",\n    \"DocR1: Evidence Page-Guided GRPO for Multi-Page Document Understanding (arXiv 2026)\",\n    \"OpenMMReasoner: Pushing the Frontiers for Multimodal Reasoning with an Open and General Recipe (CVPR 2026)\",\n    \"From Sight to Insight: Improving Visual Reasoning Capabilities of Multimodal Models via RL (arXiv 2026)\",\n    \"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)\",\n    \"Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR [TGRL] (arXiv 2026)\",\n    \"Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage (arXiv:2410.15531, NAACL 2025)\",\n    \"PGDP-Net: Plane Geometry Diagram Parsing with Graph Neural Networks (IJCAI 2022)\",\n    \"Chart-RVR: Reinforcement Learning with Verifiable Rewards for Explainable Chart Reasoning (arXiv:2510.10973)\"\n  ],\n  \"description\": \"We address the composition gap in multimodal reasoning training: while recent methods tackle perception gating (PEARL, PaLMR), attention-level credit reallocation (PGPO, SAYO, AT-RL, VICRA, KAWHI), grounding+consistency constraints (FGRPO), causal attention anchoring (Faithful-MR1), structured grounded evaluation (MJ1), self-rewarding perception decomposition (Vision-SR1), spatial evidence localization (TreeVGR, ViGoRL), embedding-level evidence re-access (v1, SIEVE), perception-level coverage rewards (VTPerception-R1), rubric-based process supervision (AutoRubric-R1V), post-hoc visual verification (CoRGI), and evidence-loss diagnostics ('Don't Blink', 'Deeper Thought, Weaker Aim'), none unifies evidence grounding, binding validity, and integration completeness verification in a single lightweight training-time verifier. We propose Composition Fidelity RL (CFRL), which requires models to generate explicit evidence citations (&lt;observe>/&lt;reason evidence=''>) and trains a distilled Composition Fidelity Verifier (CFV, 4B parameters) to check three properties: (1) evidence grounding — cited facts match image content, (2) binding validity — inferences are logically consistent with cited evidence, and (3) integration completeness — all task-relevant visual facts are cited. Binding validity is structured in two tiers: Tier 1 (core) provides domain-agnostic arithmetic verification (sum/difference/ratio/comparison consistency between cited values and computed results) and geometry symbolic theorem matching, applicable across all domains without external tools; Tier 2 (extension) adds domain-specific checks for charts (ordering consistency, extrema, trend monotonicity, aggregation) and diagrams (structural relationship, attribute, cardinality verification), requiring parsed data representations. The CFV performs all verification in a single autoregressive forward pass — processing the image once and generating inline grounding/binding verdicts for each observation and reasoning step sequentially — yielding ~5-8x cost reduction over FGRPO's per-sentence judge calls (driven by 1 vs. S ≈ 5-8 image encodings per rollout). The contribution is structured in two tiers: Tier 1 (core: grounding + arithmetic/geometric binding verifier, self-contained with no external tool dependencies) and Tier 2 (extension: completeness pipeline with domain-specific parsing + domain-specific binding checks), ensuring the paper is defensible even if completeness checking or domain-specific binding proves too approximate. Critically, we address MuRGAt's finding that enforcing structured grounding degrades accuracy in zero-shot settings through accuracy-first curriculum scheduling (Phase 0 establishes baseline accuracy before citation requirements), accuracy-dominant reward weighting (α ≥ 0.4), and counterfactual validation monitoring. The CFV is distilled from Qwen3-VL-235B on 50K synthetic composition judgments and validated on 5K held-out human-annotated examples, with noise-tolerance ablation. Unlike Vision-SR1 (self-rewarding checks perceptual self-containment but not factual accuracy or binding validity), we use an external verifier that checks each cited fact against the image. Unlike FGRPO (per-sentence judge), our single-pass verifier reduces cost ~5-8x. Unlike TreeVGR/ViGoRL (spatial localization via IoU), we verify semantic content and reasoning validity. Unlike v1/SIEVE (embedding-level re-access), we require auditable textual citations. Unlike VTPerception-R1 (perception-level coverage), we check binding validity and structured completeness. Unlike AutoRubric-R1V (trajectory-mined rubrics), we verify composition properties against the image. We incorporate anti-gaming safeguards against tag-format Goodhart effects: low format weight (≤0.05), verifiable citation grounding, answer-leak detection, KL regularization, and periodic counterfactual validation. We train Qwen3-VL-8B via GRPO on geometry, chart, and diagram tasks with curriculum scheduling. Key baselines: PEARL-7B (+6.6% over GRPO), FGRPO-7B (1.7% inconsistency, +13 grounding), PaLMR-7B (70.9% HallusionBench), TreeVGR-7B (+16.8 V*Bench), VTPerception-R1-7B (82.5% AI2D), Vision-SR1-7B (58.8 avg, 69.8 HallusionBench), PGPO (+18.7% avg), OpenMMReasoner-7B (+11.6%), AutoRubric-R1V-7B (+8.0 avg), MJ1 (77.0% MMRB2), and Faithful-MR1-7B.\",\n  \"project_name\": \"composition_fidelity_rl\",\n  \"source\": \"web_research\",\n  \"changes_from_previous_revision\": {\n    \"issue_1_vision_sr1\": \"Added Vision-SR1 (arXiv:2508.19652) as a new landscape subsection ('Self-rewarding perception-reasoning decomposition') with detailed technical description: uses &lt;visual_perception>/&lt;think>/&lt;answer> structured tags, self-rewarding via re-prompting the frozen policy model without image access to check perceptual self-containment, GRPO with decoupled reward-advantage framework, three-stage training (SFT cold-start → standard rollout → self-reward rollout), 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B. Differentiated from CFRL on three axes: (a) self-rewarding vs. external distilled verifier — self-rewarding cannot detect hallucinated but internally consistent perceptions, while CFRL's grounding verification checks each cited fact against the actual image; (b) perceptual self-containment checking vs. factual grounding accuracy + binding validity + completeness — Vision-SR1 tests whether perception suffices to re-derive the answer, not whether each fact is correct; (c) monolithic perception block vs. fine-grained per-fact &lt;observe> citations enabling per-fact verification and explicit evidence-to-inference linking. Added dedicated 'Key distinction from Vision-SR1' section in approach.\",\n    \"issue_2_binding_validity_specification\": \"Substantially expanded binding validity with concrete, algorithmic specifications for all domains, organized in two tiers. Tier 1 (core, domain-agnostic): (a) Arithmetic verification — symbolic execution of sum/difference/product/quotient consistency, ratio/percentage verification, comparison consistency, and multi-step arithmetic chaining; applies to ALL domains (geometry, charts, diagrams) without external tools. (b) Geometry symbolic theorem matching (existing). Tier 2 (extension, domain-specific): (a) Chart-specific: ordering consistency against extracted data table, extrema verification (X = max(values)), trend verification with formal monotonicity definition (including tolerance ε for noise), aggregation verification (mean within 1% relative tolerance). (b) Diagram-specific: structural relationship verification against parsed graph (edge existence), attribute consistency (label matching), cardinality verification (degree check), containment/hierarchy verification. Added explicit fallback for qualitative reasoning: binding check returns neutral score (0.5) for steps that cannot be reduced to arithmetic or structural constraint checking, flagged as 'unverifiable-binding' for monitoring. Revised Tier 1/Tier 2 scoping: Tier 1 now includes domain-agnostic arithmetic + geometry symbolic (no external tools needed), Tier 2 adds completeness + domain-specific binding (requiring parsed data representations). This makes Tier 1 stronger — it provides cross-domain binding signal via arithmetic verification even without chart/diagram-specific infrastructure.\",\n    \"issue_3_verifier_cost_model\": \"Clarified CFV architecture and cost model. The CFV performs all three property checks in a single autoregressive forward pass: given image + tagged response + verification instruction as input, it generates verification judgments for all observations and reasoning steps sequentially as autoregressive output. Grounding VQA for each &lt;observe> tag is performed as internal sub-reasoning within the autoregressive generation (inline grounding verdicts), NOT as separate VQA calls. This is architecturally identical to MJ1's single-pass multi-stage verification chain. Revised cost comparison: effective cost reduction is ~5-8x per rollout (revised from ~10-20x), driven by 1 image encoding vs. S ≈ 5-8 encodings. Per-call text generation cost is roughly comparable between CFRL (500-1500 verification tokens at 4B dense) and FGRPO (S × ~150 tokens at 3.3B active MoE). The primary savings come from the single image encoding — processing visual tokens through transformer layers is the dominant cost in VLM inference.\",\n    \"issue_4_autorubric_corgi\": \"Added AutoRubric-R1V (arXiv:2510.14738) and CoRGI (arXiv:2508.00378) to the landscape under 'Structured verification and evaluation judges'. AutoRubric-R1V: auto-generates rubric-based process rewards via self-aggregation from successful trajectories, rubric reward = fraction of satisfied checkpoints, +8.0 avg on 6 benchmarks. Differentiated: derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image. CoRGI: post-hoc step-wise verification via Grounding DINO, decomposing rationales and grounding each step in visual evidence. Differentiated: inference-time only, does not serve as training-time reward. Added 'Key distinction from AutoRubric-R1V' section. Both added to key_references. Also added Chart-RVR (arXiv:2510.10973) to key_references as it informed the chart-domain binding validity specification.\"\n  }\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"LOW-MEDIUM: The proposal does not discuss the 'Format Tax' (arXiv:2604.03616, Apr 2026), which shows 7-11pp reasoning degradation from structured XML/JSON output in open-weight models. While this paper studies inference-time prompting (not RL training), it is a directly relevant risk that should be cited and distinguished. D-CoT (arXiv:2602.21786) provides counter-evidence showing trained tags get internalized — this supporting work should also be cited.\", \"LOW-MEDIUM: The additive reward structure (R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness) is actually a strength for noise tolerance — with additive combination, per-property errors partially cancel (~1/√N reduction) rather than compound multiplicatively. But this is not explicitly argued. The proposal discusses noise tolerance for individual signals (citing 'Imperfect Verifier') but does not explain why the additive structure prevents the compounding error problem that would plague a multiplicative/conjunctive combination. Making this argument explicit would strengthen the feasibility case.\", \"LOW: CoRGI (arXiv:2508.00378) has been withdrawn by its authors. The proposal should either remove this reference or note its withdrawal status. This is a minor issue since CoRGI is positioned as a tangential work (inference-only) and its removal does not affect the gap analysis.\", \"LOW: No precedent exists for a ≤4B model performing multi-property semantic verification (grounding + binding + completeness) in a single autoregressive pass for RL training. MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens — not as a training-time reward with throughput constraints. The proposal should acknowledge this gap more explicitly and discuss what minimum per-property accuracy would make the Tier 1 verifier useful (the 75% fallback threshold for binding is specified, but grounding and completeness thresholds are not).\"]\nFeedback: The proposal is approaching pass quality after five rounds of substantial improvement. Three focused changes would likely reach the threshold:\n\n1. **Cite the Format Tax and D-CoT**: Add a brief paragraph acknowledging that 'The Format Tax' (arXiv:2604.03616) documents 7-11pp degradation from structured output in *prompted* open-weight models, but explicitly distinguish this from CFRL's RL-trained format: (a) D-CoT (arXiv:2602.21786) shows that models trained with structured tags internalize the structure and maintain performance even when tags are dropped at inference (+9.9% GPQA-diamond), (b) CFRL's curriculum develops citation as a learned skill via reward optimization, unlike MuRGAt's zero-shot format imposition where the degradation was observed. This turns a potential objection into a strength.\n\n2. **Explicitly argue the additive reward advantage**: Add 1-2 sentences noting that the additive reward combination (weighted sum of independent verifier signals) is specifically chosen to avoid multiplicative error compounding. With additive combination and independent ~15% error per property, the noise in the composite signal shrinks rather than grows, keeping the training within the 'Imperfect Verifier' tolerance regime. This directly addresses the compounding error concern.\n\n3. **Fix minor reference issues**: Note CoRGI's withdrawal. Specify minimum accuracy thresholds for grounding and completeness verification (currently only binding has a 75% fallback threshold).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 5 轮修订，近 3 轮平均分从 3.6 到 3.8，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T23:17:14.862Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T23:17:14.862Z",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

## Round 1

49 recorded events

### User

_source line 3 · 2026-05-27T23:17:14.876Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier",
  "core_problem": "How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?",
  "opportunity": "Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.",
  "landscape": "The landscape of RL-based multimodal reasoning training has exploded in early 2026 along seven axes:\n\n**Perception-gating methods:** PEARL (CVPR 2026) derives a perception checklist of factual sub-questions, computes a perceptual reward R̄_p, and uses it as a fidelity gate — blocking reasoning policy updates when perception fails. Gains: +6.6% over GRPO on MathVerse. Limitation: checks perception accuracy but not whether perceived facts are correctly *bound* to reasoning steps or whether integration is *complete*. PaLMR (CVPR 2026, arXiv:2603.06652) introduces V-GRPO (Vision-Guided GRPO) with a hierarchical reward R = S_vis × (α·S_ans + (1−α)·S_fmt), where S_vis is a binary visual fidelity gate computed via pairwise comparison against pseudo ground-truth image descriptions generated by Gemini. Achieves 70.9% on HallusionBench (+4.2pp over GRPO) with only 4,728 training instances and 88% model-human alignment. Limitation: uses external pseudo ground-truth for comparison rather than verifying the model's own explicit evidence citations; does not check completeness; binary gating provides no gradient signal for partial fidelity improvement.\n\n**Token-level credit reallocation methods:** VPPO (ICLR 2026) reweights by KL divergence on perturbed images. PGPO (Apr 2026) amplifies learning signals for visually-dependent tokens via threshold-gated advantage reallocation (+18.7% avg). VGPO (ACL 2026) adds visual attention compensation. AT-RL (Feb 2026) identifies ~15% anchor tokens via cross-modality connectivity for targeted credit assignment (+1.2% overhead, 32B surpasses 72B-Instruct). VICRA (2026) reallocates optimization toward visually-grounded tokens (+2.25 avg on Qwen2.5-VL-7B). KAWHI (Mar 2026) performs paragraph-level credit reallocation via structured attribution of vision-critical attention heads. SAYO (Feb 2026) introduces region-level visual attention reward (r_v = tanh(log(a_q/v_q))) on Qwen3-VL-8B. Collective limitation: all operate on statistical attention patterns rather than verifying the semantic correctness of evidence-to-reasoning binding.\n\n**Explicit evidence grounding in RL training:** TreeVGR (ICLR 2026) trains models to generate text-space bounding box coordinates as traceable evidence within reasoning trajectories, supervised via dual IoU reward (R_IoU = ½(R_IoU^R + R_IoU^P)) that balances precision and recall of spatial localization. Two-stage training (SFT on 37K samples + RL). Achieves +16.8 on V*Bench, +12.6 on MME-RealWorld. Limitation: verifies *spatial* localization via IoU but not the *semantic validity* of how localized evidence is used in reasoning — a correct bounding box around a labeled angle does not verify that the angle value was correctly read or correctly applied in an inference step. Does not check integration completeness. v1 (May 2026, arXiv:2505.18842) introduces a point-and-copy mechanism where the model selects relevant image patches and copies their embeddings back into the reasoning stream, maintaining visual grounding throughout multi-step reasoning. Trained via SFT on v1g (300K grounding-annotated traces); RL integration is noted as future work. Achieves 68.6% MathVista, 34.5% MathVision. Limitation: operates at the embedding/representation level — re-inserts visual features but does not produce explicit textual evidence citations that can be externally verified for semantic correctness; grounding is implicit in the representation space rather than auditable. VTPerception-R1 (arXiv:2509.24776) implements a two-stage framework (perception-augmented SFT + perception-aware RL) with three perception rewards: visual key-info coverage (R_vkey), textual key-info coverage (R_tkey), and consistency (R_cons = |F_ans∩E|/max(1,|F_ans|)). Achieves 82.5% AI2D, 71.0% MathVista. Limitation: R_vkey measures perception-level element coverage (are visual elements mentioned?) but does not verify binding validity (are inferences logically consistent with cited evidence?) or integration completeness (are all task-relevant facts addressed?). SIEVE (arXiv:2603.14117) trains models to iteratively re-access cached visual region embeddings during RL (GRPO with ℛ = λ₁ℛ_res + λ₂ℛ_format + λ₃ℛ_emb + λ₄ℛ_act), supporting multi-turn evidence refinement. Achieves +7.85 on V*Bench overall. Limitation: like v1, operates at the embedding level — re-inserted features improve grounding but don't produce explicit verifiable citations; iterative re-access addresses the evidence-loss problem but not semantic verification of how evidence supports conclusions.\n\n**Self-rewarding perception-reasoning decomposition:** Vision-SR1 (arXiv:2508.19652) decomposes reasoning into explicit &lt;visual_perception> and &lt;think> stages, requiring the model to first articulate a self-contained visual description, then reason from it. The visual reward is computed via self-rewarding: the frozen policy model is re-prompted to answer the question using only the generated visual perception text (without image access); if the correct answer is derived from perception alone, a visual reward of 1 is assigned. Uses GRPO with a decoupled reward-advantage framework that maintains separate advantages for visual and answer rewards. Three-stage training: SFT cold-start on 9K examples, then standard rollout with accuracy reward, then self-reward rollout. Achieves 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B (+1.4 over Vision-R1), 69.8 on HallusionBench. Key distinction from CFRL: (a) Vision-SR1 uses self-rewarding (same model judges itself) rather than an external distilled verifier — the reward is whether perception suffices to re-derive the answer, not whether each cited fact is *factually accurate* relative to the image; a hallucinated but internally consistent perception could score high. (b) Vision-SR1 checks perceptual *self-containment* (can you answer from perception alone?) while CFRL checks factual grounding accuracy (is the perception correct?), binding validity (does the inference follow from cited evidence?), and completeness (are all task-relevant facts covered). (c) Vision-SR1 does not verify the logical consistency between perceived evidence and drawn inferences — it treats perception and reasoning as decomposed stages but does not check whether the reasoning is faithful to the specific evidence cited.\n\n**Constrained/faithful training methods:** FGRPO (Apr 2026, arXiv:2604.08476) enforces consistency + semantic grounding + spatial grounding as constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7% and improving grounding by +13 points. Uses Qwen3-VL-30B-A3B-Instruct (MoE, ~3.3B active parameters) as the online judge during training. The semantic grounding reward R_S requires per-sentence VLM judge calls: each non-trivial visual sentence in the CoT is independently evaluated, resulting in ~30-55 judge calls per training sample. This is the closest competitor — but does not check integration completeness. Faithful-MR1 (May 2026) supervises a &lt;Focus> token's attention against image regions and uses counterfactual image intervention to reward attention concentration where vision causally matters. Operates on attention distributions rather than explicit evidence citations.\n\n**Structured verification and evaluation judges:** MJ1 (Mar 2026, arXiv:2603.07990) trains a 3B-active-parameter multimodal judge (based on Qwen3-VL-30B-A3B) using RL with a structured grounded verification chain: observations → claims → verification → evaluation → scoring, enforced via 11 required XML tags across 5 sequential stages. Achieves 77.0% on MMRB2, surpassing GPT-5 (72.2%) and Gemini-3-Pro (76.3%). Key distinction from CFRL: (a) MJ1 is an *evaluation-time* judge, not a training-time reward verifier; (b) MJ1 uses stage-separated grounding rather than inline evidence citations; (c) MJ1 performs pairwise response comparison, not composition property verification; (d) MJ1 does not check integration completeness. EVPV/Grounding the Score (Mar 2026) adds visual premise verification via constraint matching and reliability gating to PRMs — improves Best-of-N reranking but is *inference-only*. ViGoRL (2026) trains models to produce spatially grounded reasoning traces with coordinate-level evidence (86.4% on V*Bench) — addresses spatial grounding but not semantic binding validity. AutoRubric-R1V (arXiv:2510.14738) auto-generates rubric-based process rewards by distilling consistent reasoning checkpoints from successful trajectories via self-aggregation — rubric reward equals the fraction of satisfied checkpoints. Achieves +8.0 avg over Qwen2.5-VL-7B on 6 benchmarks. Distinct from CFRL: AutoRubric derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image; rubrics are answer-path-dependent rather than evidence-grounding-dependent. CoRGI (arXiv:2508.00378) performs post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal.\n\n**Evidence-aware GRPO variants:** PRCO (Mar 2026) decomposes into Observer+Solver with separate utility/outcome rewards (+7 pts). DocR1 (2026) uses evidence-page guided GRPO for document understanding. OpenMMReasoner (CVPR 2026) achieves +11.6% over Qwen2.5-VL-7B via two-stage SFT+RL recipe.\n\n**Attribution and evidence-loss diagnostics:** MuRGAt (Feb 2026, arXiv:2602.11509) introduces a benchmark for multimodal fact-level attribution requiring models to generate explicit citations specifying modality and temporal segments. Critically, MuRGAt finds that 'increasing reasoning depth or enforcing structured grounding often degrades accuracy' in zero-shot/few-shot settings — even strong MLLMs frequently hallucinate citations despite correct reasoning. This documents an accuracy-faithfulness tradeoff that CFRL must address. 'Don't Blink: Evidence Collapse during Multimodal Reasoning' (Apr 2026, arXiv:2604.04207) documents that reasoning VLMs progressively lose visual grounding as reasoning unfolds — attention to annotated evidence regions drops >50% — creating confident but ungrounded predictions that text-only monitoring cannot detect. 'Deeper Thought, Weaker Aim' (Mar 2026, arXiv:2603.14184) independently confirms this, showing reasoning prompts significantly reduce attention to question-critical image regions. 'Compose and Fuse' (ICLR 2026) identifies task-composition and fusion as main barriers. MathLens (Feb 2026) shows integration failures grow as a fraction of remaining errors. The PAR framework (Mar 2026) decomposes multimodal math reasoning into Perception–Alignment–Reasoning and identifies alignment fragmentation as a distinct failure mode.\n\n**The gap:** PEARL and PaLMR check perception but not binding or completeness; FGRPO checks consistency+grounding but not completeness, with ~5-8x higher cost per rollout vs. single-pass verification; Vision-SR1 decomposes perception and reasoning with self-rewarding but does not verify factual grounding accuracy, binding validity, or completeness; TreeVGR and ViGoRL verify spatial localization but not semantic reasoning validity; v1 and SIEVE re-access visual evidence at the embedding level but don't produce auditable textual citations; VTPerception-R1 checks perception-level coverage but not binding validity or completeness; MJ1 demonstrates structured grounded verification chains but operates at evaluation time; AutoRubric-R1V provides process supervision via trajectory-mined rubrics but not composition property verification against the image; CoRGI performs step-wise visual verification but is inference-only; attention-based methods (PGPO, SAYO, AT-RL, Faithful-MR1) use statistical proxies; EVPV is inference-only. No existing method unifies all three composition properties (evidence grounding, binding validity, integration completeness) in a single lightweight training-time verifier. MuRGAt's accuracy-faithfulness tradeoff highlights that naive enforcement of structured citation degrades performance — but this was observed under zero-shot prompting, not RL training with curriculum scheduling.",
  "inspired_by": "'Compose and Fuse' (ICLR 2026) explicit future direction for composition-aware training; MathLens integration-failure analysis; PAR framework's alignment decomposition; FGRPO's grounding+consistency insight (extended with completeness and efficiency); MJ1's structured verification chain (adapted from evaluation-time judge to training-time reward); PaLMR's visual fidelity gating (extended beyond binary gating to multi-property verification); TreeVGR's explicit evidence generation in RL (extended from spatial to semantic verification); v1's interleaved grounding paradigm (adapted from embedding-level to textual-citation-level); Vision-SR1's perception-reasoning decomposition with self-rewarding (extended from self-containment checking to external factual grounding + binding + completeness verification); MuRGAt's accuracy-faithfulness tradeoff (motivating curriculum training and accuracy-first reward scheduling); 'Don't Blink' and 'Deeper Thought, Weaker Aim' documenting evidence collapse (direct motivation for explicit evidence anchoring); 'An Imperfect Verifier is Good Enough' (Apr 2026) validating noisy-reward robustness for distilled verifiers; GeoSketch's symbolic reward for geometry; Geoparsing (Apr 2026) for formal diagram entity extraction; Chart-RVR's verifiable chart reasoning rewards (informing chart-domain binding checks); CHARGE's keypoint coverage metrics; Countdown-Code (2026) and PURE (2025) for reward hacking diagnosis and mitigation",
  "approach": "We propose Composition Fidelity RL (CFRL), which unifies evidence grounding, binding validity, and integration completeness verification in a single distilled composition verifier used as a GRPO training reward.\n\n**Structured output format:** The model generates responses with explicit &lt;observe entity='...' value='...'/> tags for visual evidence extraction and &lt;reason evidence='obs1,obs2' rule='...'> blocks for each reasoning step, requiring citation of specific observations and the inference rule applied. This explicit citation format enables automated verification — unlike attention-based methods that can only measure statistical dependency, or embedding-level methods (v1, SIEVE) that re-access visual features without producing auditable textual claims. Compared to TreeVGR's bounding-box coordinates, our citations capture *semantic* content ('radius = 5cm') rather than *spatial* location ([x1,y1,x2,y2]), enabling verification of whether the cited value is correct and whether the inference logically follows. Compared to MJ1's stage-separated verification chain, our format embeds evidence references *inline* with reasoning, creating direct referential links suitable for training-time throughput. Compared to Vision-SR1's &lt;visual_perception> block, our format provides *fine-grained, per-fact citations* (individual &lt;observe> tags) rather than a monolithic perception paragraph, enabling per-fact grounding verification and explicit evidence-to-inference linking via the evidence='obs1,obs2' attribute.\n\n**Addressing the accuracy-faithfulness tradeoff (MuRGAt):** MuRGAt (Feb 2026) found that enforcing structured grounding degrades accuracy in zero-shot/few-shot settings — models hallucinate citations despite correct reasoning. This is a direct challenge to CFRL's premise. We address it through four design choices: (1) *RL training develops citation as a learned skill*: unlike MuRGAt's zero-shot evaluation where citation is an imposed constraint, CFRL trains the model to produce faithful citations through reward optimization, allowing the model to develop integrated reasoning-citation capability rather than retrofitting citations onto existing reasoning. (2) *Accuracy-first curriculum scheduling*: Phase 0 (pre-curriculum) establishes answer accuracy via standard GRPO before introducing any citation requirements, ensuring the model's reasoning capability is preserved before grounding constraints are layered on. Citation rewards are introduced gradually with initial weight near zero, increasing only as the model demonstrates stable accuracy. (3) *Accuracy-dominant reward weighting*: R_accuracy receives weight α ≥ 0.4 throughout training, ensuring citation quality never dominates at the expense of answer correctness. If accuracy on a held-out validation set drops >2pp at any curriculum transition, citation reward weights are halved until accuracy recovers. (4) *Counterfactual validation* (safeguard #5) directly monitors for MuRGAt-style degradation by comparing tagged vs. untagged accuracy.\n\n**Composition Fidelity Verifier (CFV) — three-property checking:**\n(1) *Evidence grounding*: Checks whether cited visual facts (in &lt;observe> tags) correspond to actual image content. Uses a lightweight visual QA module that converts each citation into a yes/no visual question (e.g., 'Is the radius labeled as 5cm in the image?'). Inspired by PEARL's perception checklist but applied to model-generated citations rather than externally-derived sub-questions.\n(2) *Binding validity*: Checks logical consistency between cited evidence and the inference drawn. We define binding validity checks at two levels:\n\n  **Tier 1 — Domain-agnostic arithmetic + geometry symbolic (core contribution):**\n  - *Arithmetic verification* (all domains): Given numerical values extracted from &lt;observe> tags and a stated operation in the &lt;reason> block, verify computational correctness via symbolic execution. Concrete checks: (a) *Sum/difference/product/quotient consistency* — if obs1 cites 'value A = 45' and obs2 cites 'value B = 30', and the reason block claims 'difference = 15' with rule 'subtraction', verify 45−30=15. (b) *Ratio/percentage verification* — if 'Part = 120, Total = 400' and conclusion is '30%', verify 120/400=0.30. (c) *Comparison consistency* — if the reason block claims 'A > B' citing obs1 (A=45) and obs2 (B=30), verify 45>30. (d) *Multi-step arithmetic* — chain verification across sequential &lt;reason> blocks where one step's output is another's input. These checks are domain-agnostic: they apply equally to geometry problems (angle computations), chart problems (bar value comparisons, trend calculations), and diagram problems (counting, distance computations).\n  - *Geometry symbolic theorem matching*: Cited theorems/rules are matched against a geometry theorem library, and symbolic constraints are verified formally. For example, cited 'angle A=60°, angle B=90°' with rule 'triangle angle sum' → verify 60+90+x=180 → x=30°. Inspired by GeoSketch and the PAR framework.\n\n  **Tier 2 — Domain-specific binding checks (extension):**\n  - *Chart-specific*: (a) *Ordering consistency* — if 'Bar A > Bar B' is cited, verify against the extracted data table that value(A) > value(B). (b) *Extrema verification* — if 'X is the maximum value' is cited, verify X = max(all values in series). (c) *Trend verification* — if 'increasing from 2020 to 2023' is cited, verify monotonic increase in the relevant data points; trends are formally defined as: 'increasing' requires each successive value ≥ previous (strict: >), 'decreasing' requires ≤ (strict: <), with tolerance ε for noise. (d) *Aggregation verification* — if 'average = X' is cited, verify mean(values) ≈ X within 1% relative tolerance. These checks require the chart data table extracted in the completeness pipeline (Stage A), linking Tier 2 binding to Tier 2 completeness infrastructure.\n  - *Diagram-specific*: (a) *Structural relationship verification* — if 'A connects to B' is cited, verify edge (A,B) exists in the parsed graph from PGDP-Net. (b) *Attribute consistency* — if 'node A is labeled X' is cited, verify label(A) = X in the parsed representation. (c) *Cardinality verification* — if 'A has 3 connections' is cited, verify degree(A) = 3. (d) *Containment/hierarchy* — if 'A is inside B' is cited, verify the containment relation in the parsed spatial layout. These checks require the diagram graph representation from Stage A parsing.\n  - *Fallback for inapplicable checks*: When a &lt;reason> block involves qualitative reasoning that cannot be reduced to arithmetic or structural constraint checking (e.g., 'the diagram suggests a causal relationship between X and Y'), the binding check returns a neutral score (0.5) rather than penalizing, and the verifier flags it as 'unverifiable-binding' for monitoring. This prevents the binding reward from penalizing valid qualitative reasoning while maintaining signal for verifiable steps.\n\n(3) *Integration completeness*: Checks whether all task-relevant visual facts are cited somewhere in the reasoning chain via a three-stage domain-specific pipeline:\n\n  **Stage A — Visual Element Enumeration** (domain-specific, offline or cached):\n  - *Geometry*: Use Geoparsing (arXiv:2604.11600, Apr 2026) to produce a formal entity/relation set from the diagram. Geoparsing achieves 96.4 F1 overall (points 99.6, lines 98.0, circles 98.3, semantics 90.7) using a unified formal language.\n  - *Charts*: Use DePlot/UniChart-style chart derendering to extract a linearized data table of all data points, then apply CHARGE-style keypoint extraction to convert to self-contained factual statements.\n  - *Diagrams*: Use PGDP-Net-style graph parsing to extract a node-edge representation of diagram primitives and their relations.\n\n  **Stage B — Question-Conditioned Relevance Filtering**:\n  - Apply VisDoT-style (arXiv:2603.11631) question decomposition to generate ordered perception sub-questions. Match sub-questions against enumerated visual elements from Stage A to produce a *required visual fact set* F_required.\n  - Reliability estimate: Sub-question coverage as a ranking metric achieves 82% accuracy against human preferences (arXiv:2410.15531), with human inter-annotator agreement of 74.6% on sub-question classification — indicating this is an inherently noisy signal, which motivates our soft treatment of completeness (see below).\n  - For geometry, the symbolic checker provides an additional signal: any entity appearing in the formal solution path is automatically added to F_required.\n\n  **Stage C — Coverage Verification**:\n  - Compute coverage score: R_completeness = |F_cited ∩ F_required| / |F_required|.\n  - We target ≥80% recall of task-relevant facts, acknowledging that completeness checking is inherently approximate. The 80% threshold is motivated by CHARGE's finding that even SOTA MLLMs achieve only 73.9% coverage with ground-truth retrieval.\n  - For facts in F_required that are NOT cited, the verifier generates a soft penalty proportional to the estimated importance of the missing fact.\n\n**Verifier architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass. The input consists of the image + the model's full tagged response + a structured verification instruction. The CFV generates verification judgments sequentially as autoregressive output: for each &lt;observe> tag, it produces an inline grounding verdict (verified/unverified with confidence score); for each &lt;reason> block, it produces a binding validity verdict; and finally, it produces an overall completeness assessment. This is architecturally identical to how MJ1 generates its multi-stage verification chain in one forward pass — the grounding VQA for each observation is performed as internal sub-reasoning within the autoregressive generation, NOT as separate VQA calls. The output length scales with the number of observations and reasoning steps (~500-1500 tokens for typical responses with 4-8 observations), but requires only a single image encoding through the vision encoder.\n\n**Cost comparison with FGRPO (precise):** FGRPO requires S separate judge calls per rollout (S ≈ 5-8 visual sentences), each requiring its own image encoding through the 30B MoE model (3.3B active parameters). CFRL requires 1 verifier call per rollout with a single image encoding through the 4B dense model. Since image encoding is the dominant cost in VLM inference (processing hundreds of visual tokens through transformer layers), the savings from 1 vs. S encodings is the primary cost driver. Per-call text generation cost is roughly comparable: FGRPO generates S × ~150 = 750-1200 tokens total across all calls; CFRL generates ~500-1500 tokens in one call, at similar active parameter counts (3.3B MoE vs. 4B dense). The effective cost reduction is **~5-8x per rollout** (proportional to S), driven primarily by the single image encoding. Per training sample with K rollouts, FGRPO makes K×S judge calls vs. CFRL's K verifier calls — the same ~5-8x ratio holds. For Tier 1 (grounding + binding only), where binding validity uses lightweight symbolic/arithmetic checking outside the verifier, the verifier output is shorter (~300-800 tokens), further reducing per-call cost.\n\n**Staged contribution and risk mitigation (addressing system complexity):** The full CFRL system integrates multiple external tools and domain-specific pipelines, creating compounding failure risk. We structure the contribution in two defensible tiers:\n\n  *Tier 1 — Core contribution (grounding + binding):* Evidence grounding (VQA-based, all domains) and binding validity (domain-agnostic arithmetic verification + geometry symbolic theorem matching). This tier requires only the distilled 4B verifier and a geometry theorem library — no external parsing tools. Domain-agnostic arithmetic verification applies to chart and diagram problems too (any reasoning step involving numerical computation is checkable), providing cross-domain binding signal even without domain-specific infrastructure. This tier is self-contained, already differentiates from all existing methods (none verify binding validity as a training reward), and provides a defensible paper even if completeness checking and domain-specific binding prove too approximate. Estimated complexity: 1 distilled model + 1 theorem library.\n\n  *Tier 2 — Extension (completeness + domain-specific binding):* Integration completeness adds Geoparsing, DePlot/CHARGE, PGDP-Net, and VisDoT-style decomposition. Domain-specific binding for charts adds data-table-dependent checks (ordering, trends, extrema); for diagrams adds graph-dependent checks (structural relationships, attributes). Each integration is a potential failure point. Fallback strategies per component: (a) If Geoparsing underperforms on out-of-distribution diagrams, fall back to the distilled verifier's own visual element listing (lower accuracy but zero external dependency). (b) If relevance filtering is too noisy, use only the symbolic solver's required entities (geometry) or question-mentioned entities (charts/diagrams) as F_required — a conservative underestimate that still provides signal. (c) If domain-specific binding checks add noise rather than signal (e.g., trend verification on noisy data), fall back to Tier 1 arithmetic-only binding for that domain. (d) If end-to-end completeness R_completeness adds noise rather than signal, set δ=0 and report Tier 1 results as the core finding.\n\n  *Risk matrix:*\n  - Pipeline integration failure (MEDIUM risk): Mitigated by Tier 1/Tier 2 separation and per-component fallbacks.\n  - Verifier distillation quality (LOW risk): Validated via held-out test set; noise tolerance demonstrated by 'Imperfect Verifier' methodology.\n  - Accuracy-faithfulness tradeoff (MEDIUM risk): Mitigated by accuracy-first curriculum, accuracy-dominant reward weighting, and counterfactual monitoring (see MuRGAt discussion above).\n  - Tag gaming / Goodhart effects (LOW-MEDIUM risk): Mitigated by five anti-gaming safeguards (see below).\n  - Training instability from 5 reward components (MEDIUM risk): Mitigated by curriculum scheduling (components introduced sequentially, not simultaneously) and reward weight monitoring.\n\n**Verifier distillation:** The CFV is distilled from Qwen3-VL-235B-A22B on synthetically generated composition judgment pairs. We generate correct/incorrect binding examples by: (a) taking model solutions, (b) perturbing citations (wrong entity, wrong value, missing citation, irrelevant citation, logically inconsistent inference, arithmetic errors), (c) having the teacher label each perturbation type. Target: 50K examples across geometry, chart, and diagram domains, with balanced representation of arithmetic binding errors (Tier 1) and domain-specific binding errors (Tier 2). The distilled verifier (based on Qwen3-VL-4B) is validated on a held-out test set of 5K human-annotated composition judgments.\n\n**Verifier validation protocol**: Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with Tier 1 binding validated separately for arithmetic and geometry-symbolic components, (b) ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on binding validity falls below 75%, we activate the fallback: softening binding rewards to a probabilistic consistency score weighted by verifier confidence.\n\n**Anti-gaming safeguards** (addressing Goodhart's Law risk):\n  (1) *Low format weight*: Format compliance ≤0.05 in composite reward. Dominant signals come from verifiable content-level checks.\n  (2) *Verifiable citation grounding*: Evidence grounding is checked against actual image content via visual QA — un-gameable.\n  (3) *Answer-leak detection*: Embedding cosine similarity monitoring between &lt;observe> content and final answer, with penalty P_leak.\n  (4) *KL regularization against base policy*: Standard KL penalty + format/content reward ratio monitoring; divergence triggers early stopping.\n  (5) *Counterfactual validation*: Every 500 steps, evaluate with tags stripped. If tagged accuracy exceeds untagged by >5pp, signal format-dependent performance and trigger reward recalibration.\n\n**Training:** GRPO on Qwen3-VL-8B via veRL with composite reward R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness + ε·R_format − P_leak. Curriculum training: Phase 0 establishes baseline accuracy (week 1), Phase 1 trains grounding (weeks 1.5-2.5), Phase 2 adds binding validity (weeks 2.5-3.5), Phase 3 adds completeness (weeks 3.5-4.5). Training targets geometry (MathVerse, GeoQA+), chart (ChartQA, PlotQA), and diagram (AI2D, ScienceQA) tasks.\n\n**Key distinction from Vision-SR1:** Vision-SR1 decomposes reasoning into &lt;visual_perception> and &lt;think> stages and checks perceptual self-containment via self-rewarding — re-prompting the model without image access to verify the perception suffices. CFRL differs in three ways: (a) CFRL uses an external distilled verifier rather than self-rewarding — self-rewarding cannot detect hallucinated perceptions that happen to be internally consistent (a fabricated but plausible description could still support the correct answer), while external grounding verification checks each cited fact against the actual image. (b) CFRL provides fine-grained per-fact citations (&lt;observe> tags) rather than a monolithic perception block, enabling per-fact grounding verification and explicit evidence-to-inference linking. (c) CFRL verifies binding validity (does the inference logically follow from cited evidence?) and integration completeness, which Vision-SR1 does not address.\n\n**Key distinction from TreeVGR:** TreeVGR generates bounding-box coordinates as evidence and supervises spatial localization via dual IoU reward — verifying *where* the model attends. CFRL generates semantic textual citations and verifies *what* the model claims to see and *how* it reasons from those claims. These are complementary: TreeVGR could locate the correct region but misread the value; CFRL catches such semantic errors. TreeVGR does not check binding validity or integration completeness.\n\n**Key distinction from v1 and SIEVE:** Both re-access visual evidence at the embedding level — v1 via point-and-copy of patch embeddings, SIEVE via cached region embedding re-insertion. This maintains visual grounding in the model's internal representation but does not produce *explicit, auditable textual claims* about what was perceived. CFRL requires the model to articulate its visual evidence in natural language, enabling external verification of both the perception (grounding) and the reasoning (binding validity). v1 uses SFT only; SIEVE uses RL but without composition-level verification.\n\n**Key distinction from VTPerception-R1:** VTPerception-R1's R_vkey/R_tkey rewards check perception-level element coverage (whether visual/textual elements are mentioned in reasoning), while R_cons checks entity-attribute consistency. CFRL goes further in two ways: (a) binding validity checks logical inference consistency, not just entity-mention consistency, and (b) integration completeness checks coverage of all task-relevant facts via structured enumeration, not just key-info recall from a VLM scorer.\n\n**Key distinction from FGRPO:** FGRPO uses Qwen3-VL-30B-A3B-Instruct as per-sentence online judge, resulting in ~30-55 judge calls per training sample. Our single-pass CFV reduces this to ~K calls per sample (one per rollout), yielding ~5-8x cost reduction driven by single image encoding per rollout vs. S encodings. More importantly, CFRL adds completeness checking. FGRPO uses Lagrangian dual ascent; we use direct reward weighting with curriculum scheduling.\n\n**Key distinction from PaLMR:** PaLMR's V-GRPO uses binary visual fidelity gate (S_vis ∈ {0,1}) providing no gradient for partial improvement. CFRL provides continuous, multi-property reward signals. PaLMR does not require or verify explicit evidence citations.\n\n**Key distinction from MJ1:** MJ1 is evaluation-time judge with 5-stage pipeline (up to 6144 tokens). CFRL adapts structured verification to training-time with compact inline citations. CFRL checks completeness, which MJ1 does not.\n\n**Key distinction from PEARL:** PEARL checks perception accuracy of externally-generated sub-questions. CFRL checks grounding, validity, and completeness of the model's own explicit evidence citations.\n\n**Key distinction from AutoRubric-R1V:** AutoRubric-R1V provides process supervision by mining rubric checkpoints from successful trajectories — it checks whether the model's reasoning path conforms to patterns found in correct solutions. CFRL instead verifies composition properties against the image itself: whether cited evidence is factually grounded, inferences are valid, and coverage is complete. These are complementary: AutoRubric rewards path conformity, CFRL rewards evidence fidelity.\n\n**Key distinction from attention-based methods (PGPO, SAYO, Faithful-MR1):** These measure statistical attention patterns. CFRL requires and verifies explicit semantic citation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "950 (verifier distillation: 100h on 4xH100; Geoparsing/DePlot integration and symbolic checker development: 80h; completeness pipeline development: 70h; main GRPO training: 400h on 8xH100; ablations including verifier accuracy sweep, anti-gaming validation, and baselines: 300h)",
      "timeline": "10 weeks (1.5w setup + data + completeness pipeline + symbolic checker, 1.5w verifier training + validation, 3w main experiments with curriculum, 2.5w ablations + verifier accuracy study + anti-gaming analysis, 1.5w analysis and writing — overlapping phases)",
      "estimated_gpu_cost": "$1,250 (H100 spot at ~$1.30/GPU-hr on Spheron/RunPod 2026 rates)"
    },
    "human_in_loop": {
      "gpu_hours": "950 (same experimental requirements)",
      "timeline": "8 weeks (Claude accelerates verifier data generation, completeness pipeline scaffolding, experiment analysis)",
      "claude_api_cost": "$300 (code assistance, composition judgment labeling assistance, completeness annotation, paper drafting)",
      "estimated_gpu_cost": "$1,250"
    },
    "auto_research": {
      "gpu_hours": "1500 (additional hyperparameter sweeps for α/β/γ/δ/ε, verifier architecture search, verifier accuracy noise ablation, completeness pipeline ablation per domain, anti-gaming validation suite, extended baselines including PEARL+FGRPO+PaLMR+TreeVGR+Vision-SR1 reimplementation, symbolic checker coverage expansion)",
      "timeline": "7 weeks (parallelized experiment scheduling, automated verifier validation)",
      "claude_api_cost": "$1,000 (teacher labeling for verifier data: $600 for ~50K composition judgments via Qwen3-VL-235B; completeness annotation for chart/diagram domains: $100; experiment orchestration, analysis, and ablation design: $300)",
      "estimated_gpu_cost": "$1,950",
      "speed_bottleneck": "Verifier data generation requires teacher model (Qwen3-VL-235B) inference at ~50K examples; Geoparsing inference for geometry completeness pipeline; verifier validation requires human-annotated held-out set (5K examples); GRPO rollout reward evaluation is sequential per batch; curriculum phasing requires sequential training stages; anti-gaming counterfactual validation adds ~10% overhead per checkpoint"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated late Sep 2026, ~17 weeks from now — primary target with sufficient buffer for experiments + writing)",
    "AAAI 2027 (abstract: Jul 21, paper: Jul 28, 2026 — stretch goal, 8 weeks with zero buffer; feasible only with aggressive parallelization and if verifier distillation completes in week 2)",
    "CVPR 2027 (estimated ~Nov 2026, not yet announced — fallback if additional ablations needed)"
  ],
  "level": "top-tier",
  "key_references": [
    "Compose and Fuse: Revisiting the Foundational Bottlenecks in Multimodal Reasoning (ICLR 2026)",
    "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning [PEARL] (CVPR 2026)",
    "PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment [V-GRPO] (CVPR 2026, arXiv:2603.06652)",
    "MJ1: Multimodal Judgment via Grounded Verification (arXiv:2603.07990, Mar 2026)",
    "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv Mar 2026)",
    "Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization [FGRPO] (arXiv:2604.08476, Apr 2026)",
    "Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention (arXiv May 2026)",
    "TreeVGR: Traceable Evidence Enhanced Visual Grounded Reasoning (ICLR 2026, arXiv:2507.07999)",
    "v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv:2505.18842, May 2026)",
    "VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding (arXiv:2509.24776)",
    "SIEVE: Improving Visual Reasoning with Iterative Evidence Refinement (arXiv:2603.14117, Mar 2026)",
    "Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization (arXiv:2508.19652)",
    "AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning (arXiv:2510.14738)",
    "CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv:2508.00378)",
    "MuRGAt: Multimodal Fact-Level Attribution for Verifiable Reasoning (arXiv:2602.11509, Feb 2026)",
    "Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv:2604.04207, Apr 2026)",
    "Deeper Thought, Weaker Aim: Understanding and Mitigating Perceptual Impairment during Reasoning in MLLMs (arXiv:2603.14184, Mar 2026)",
    "Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models [PGPO] (arXiv Apr 2026)",
    "Credit Where It is Due: Cross-Modality Connectivity Drives Precise RL for MLLM Reasoning [AT-RL] (arXiv Feb 2026)",
    "Don't Lose Sight: Visually-Grounded Credit Assignment for Multimodal Reasoning [VICRA] (2026)",
    "Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs [SAYO] (arXiv Feb 2026)",
    "Grounded Reinforcement Learning for Visual Reasoning [ViGoRL] (arXiv 2026)",
    "What MLLMs Learn about When they Learn about Multimodal Reasoning [MathLens] (arXiv 2026)",
    "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)",
    "Deconstructing Multimodal Mathematical Reasoning: Towards a Unified Perception-Alignment-Reasoning Paradigm [PAR] (arXiv Mar 2026)",
    "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv Apr 2026)",
    "GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025/2026)",
    "Geoparsing: Unified Formal Language for Geometry Diagram Parsing (arXiv:2604.11600, Apr 2026)",
    "Benchmarking Multimodal RAG through a Chart-based Document Question-Answering Generation Framework [CHARGE] (arXiv:2502.14864, 2025)",
    "DePlot: One-shot Visual Language Reasoning by Plot-to-Table Translation (2023)",
    "VisDoT: Decomposition of Thought with Visual Interpretation Grounding (arXiv:2603.11631, Mar 2026, EACL 2026 Findings)",
    "Countdown-Code: A Testbed for Reward Hacking in RLVR (arXiv:2603.07084, Mar 2026)",
    "PURE: Pessimistic Unbiased Reward Estimation for RL with Noisy Rewards (arXiv:2504.15275, NeurIPS 2025)",
    "Spotlight on Token Perception for Multimodal Reinforcement Learning [VPPO] (ICLR 2026)",
    "Visually-Guided Policy Optimization for Multimodal Reasoning [VGPO] (ACL 2026)",
    "DocR1: Evidence Page-Guided GRPO for Multi-Page Document Understanding (arXiv 2026)",
    "OpenMMReasoner: Pushing the Frontiers for Multimodal Reasoning with an Open and General Recipe (CVPR 2026)",
    "From Sight to Insight: Improving Visual Reasoning Capabilities of Multimodal Models via RL (arXiv 2026)",
    "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)",
    "Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR [TGRL] (arXiv 2026)",
    "Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage (arXiv:2410.15531, NAACL 2025)",
    "PGDP-Net: Plane Geometry Diagram Parsing with Graph Neural Networks (IJCAI 2022)",
    "Chart-RVR: Reinforcement Learning with Verifiable Rewards for Explainable Chart Reasoning (arXiv:2510.10973)"
  ],
  "description": "We address the composition gap in multimodal reasoning training: while recent methods tackle perception gating (PEARL, PaLMR), attention-level credit reallocation (PGPO, SAYO, AT-RL, VICRA, KAWHI), grounding+consistency constraints (FGRPO), causal attention anchoring (Faithful-MR1), structured grounded evaluation (MJ1), self-rewarding perception decomposition (Vision-SR1), spatial evidence localization (TreeVGR, ViGoRL), embedding-level evidence re-access (v1, SIEVE), perception-level coverage rewards (VTPerception-R1), rubric-based process supervision (AutoRubric-R1V), post-hoc visual verification (CoRGI), and evidence-loss diagnostics ('Don't Blink', 'Deeper Thought, Weaker Aim'), none unifies evidence grounding, binding validity, and integration completeness verification in a single lightweight training-time verifier. We propose Composition Fidelity RL (CFRL), which requires models to generate explicit evidence citations (&lt;observe>/&lt;reason evidence=''>) and trains a distilled Composition Fidelity Verifier (CFV, 4B parameters) to check three properties: (1) evidence grounding — cited facts match image content, (2) binding validity — inferences are logically consistent with cited evidence, and (3) integration completeness — all task-relevant visual facts are cited. Binding validity is structured in two tiers: Tier 1 (core) provides domain-agnostic arithmetic verification (sum/difference/ratio/comparison consistency between cited values and computed results) and geometry symbolic theorem matching, applicable across all domains without external tools; Tier 2 (extension) adds domain-specific checks for charts (ordering consistency, extrema, trend monotonicity, aggregation) and diagrams (structural relationship, attribute, cardinality verification), requiring parsed data representations. The CFV performs all verification in a single autoregressive forward pass — processing the image once and generating inline grounding/binding verdicts for each observation and reasoning step sequentially — yielding ~5-8x cost reduction over FGRPO's per-sentence judge calls (driven by 1 vs. S ≈ 5-8 image encodings per rollout). The contribution is structured in two tiers: Tier 1 (core: grounding + arithmetic/geometric binding verifier, self-contained with no external tool dependencies) and Tier 2 (extension: completeness pipeline with domain-specific parsing + domain-specific binding checks), ensuring the paper is defensible even if completeness checking or domain-specific binding proves too approximate. Critically, we address MuRGAt's finding that enforcing structured grounding degrades accuracy in zero-shot settings through accuracy-first curriculum scheduling (Phase 0 establishes baseline accuracy before citation requirements), accuracy-dominant reward weighting (α ≥ 0.4), and counterfactual validation monitoring. The CFV is distilled from Qwen3-VL-235B on 50K synthetic composition judgments and validated on 5K held-out human-annotated examples, with noise-tolerance ablation. Unlike Vision-SR1 (self-rewarding checks perceptual self-containment but not factual accuracy or binding validity), we use an external verifier that checks each cited fact against the image. Unlike FGRPO (per-sentence judge), our single-pass verifier reduces cost ~5-8x. Unlike TreeVGR/ViGoRL (spatial localization via IoU), we verify semantic content and reasoning validity. Unlike v1/SIEVE (embedding-level re-access), we require auditable textual citations. Unlike VTPerception-R1 (perception-level coverage), we check binding validity and structured completeness. Unlike AutoRubric-R1V (trajectory-mined rubrics), we verify composition properties against the image. We incorporate anti-gaming safeguards against tag-format Goodhart effects: low format weight (≤0.05), verifiable citation grounding, answer-leak detection, KL regularization, and periodic counterfactual validation. We train Qwen3-VL-8B via GRPO on geometry, chart, and diagram tasks with curriculum scheduling. Key baselines: PEARL-7B (+6.6% over GRPO), FGRPO-7B (1.7% inconsistency, +13 grounding), PaLMR-7B (70.9% HallusionBench), TreeVGR-7B (+16.8 V*Bench), VTPerception-R1-7B (82.5% AI2D), Vision-SR1-7B (58.8 avg, 69.8 HallusionBench), PGPO (+18.7% avg), OpenMMReasoner-7B (+11.6%), AutoRubric-R1V-7B (+8.0 avg), MJ1 (77.0% MMRB2), and Faithful-MR1-7B.",
  "project_name": "composition_fidelity_rl",
  "source": "web_research",
  "changes_from_previous_revision": {
    "issue_1_vision_sr1": "Added Vision-SR1 (arXiv:2508.19652) as a new landscape subsection ('Self-rewarding perception-reasoning decomposition') with detailed technical description: uses &lt;visual_perception>/&lt;think>/&lt;answer> structured tags, self-rewarding via re-prompting the frozen policy model without image access to check perceptual self-containment, GRPO with decoupled reward-advantage framework, three-stage training (SFT cold-start → standard rollout → self-reward rollout), 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B. Differentiated from CFRL on three axes: (a) self-rewarding vs. external distilled verifier — self-rewarding cannot detect hallucinated but internally consistent perceptions, while CFRL's grounding verification checks each cited fact against the actual image; (b) perceptual self-containment checking vs. factual grounding accuracy + binding validity + completeness — Vision-SR1 tests whether perception suffices to re-derive the answer, not whether each fact is correct; (c) monolithic perception block vs. fine-grained per-fact &lt;observe> citations enabling per-fact verification and explicit evidence-to-inference linking. Added dedicated 'Key distinction from Vision-SR1' section in approach.",
    "issue_2_binding_validity_specification": "Substantially expanded binding validity with concrete, algorithmic specifications for all domains, organized in two tiers. Tier 1 (core, domain-agnostic): (a) Arithmetic verification — symbolic execution of sum/difference/product/quotient consistency, ratio/percentage verification, comparison consistency, and multi-step arithmetic chaining; applies to ALL domains (geometry, charts, diagrams) without external tools. (b) Geometry symbolic theorem matching (existing). Tier 2 (extension, domain-specific): (a) Chart-specific: ordering consistency against extracted data table, extrema verification (X = max(values)), trend verification with formal monotonicity definition (including tolerance ε for noise), aggregation verification (mean within 1% relative tolerance). (b) Diagram-specific: structural relationship verification against parsed graph (edge existence), attribute consistency (label matching), cardinality verification (degree check), containment/hierarchy verification. Added explicit fallback for qualitative reasoning: binding check returns neutral score (0.5) for steps that cannot be reduced to arithmetic or structural constraint checking, flagged as 'unverifiable-binding' for monitoring. Revised Tier 1/Tier 2 scoping: Tier 1 now includes domain-agnostic arithmetic + geometry symbolic (no external tools needed), Tier 2 adds completeness + domain-specific binding (requiring parsed data representations). This makes Tier 1 stronger — it provides cross-domain binding signal via arithmetic verification even without chart/diagram-specific infrastructure.",
    "issue_3_verifier_cost_model": "Clarified CFV architecture and cost model. The CFV performs all three property checks in a single autoregressive forward pass: given image + tagged response + verification instruction as input, it generates verification judgments for all observations and reasoning steps sequentially as autoregressive output. Grounding VQA for each &lt;observe> tag is performed as internal sub-reasoning within the autoregressive generation (inline grounding verdicts), NOT as separate VQA calls. This is architecturally identical to MJ1's single-pass multi-stage verification chain. Revised cost comparison: effective cost reduction is ~5-8x per rollout (revised from ~10-20x), driven by 1 image encoding vs. S ≈ 5-8 encodings. Per-call text generation cost is roughly comparable between CFRL (500-1500 verification tokens at 4B dense) and FGRPO (S × ~150 tokens at 3.3B active MoE). The primary savings come from the single image encoding — processing visual tokens through transformer layers is the dominant cost in VLM inference.",
    "issue_4_autorubric_corgi": "Added AutoRubric-R1V (arXiv:2510.14738) and CoRGI (arXiv:2508.00378) to the landscape under 'Structured verification and evaluation judges'. AutoRubric-R1V: auto-generates rubric-based process rewards via self-aggregation from successful trajectories, rubric reward = fraction of satisfied checkpoints, +8.0 avg on 6 benchmarks. Differentiated: derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image. CoRGI: post-hoc step-wise verification via Grounding DINO, decomposing rationales and grounding each step in visual evidence. Differentiated: inference-time only, does not serve as training-time reward. Added 'Key distinction from AutoRubric-R1V' section. Both added to key_references. Also added Chart-RVR (arXiv:2510.10973) to key_references as it informed the chart-domain binding validity specification."
  }
}

## Reviewer feedback (round 5)
Issues: ["LOW-MEDIUM: The proposal does not discuss the 'Format Tax' (arXiv:2604.03616, Apr 2026), which shows 7-11pp reasoning degradation from structured XML/JSON output in open-weight models. While this paper studies inference-time prompting (not RL training), it is a directly relevant risk that should be cited and distinguished. D-CoT (arXiv:2602.21786) provides counter-evidence showing trained tags get internalized — this supporting work should also be cited.", "LOW-MEDIUM: The additive reward structure (R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness) is actually a strength for noise tolerance — with additive combination, per-property errors partially cancel (~1/√N reduction) rather than compound multiplicatively. But this is not explicitly argued. The proposal discusses noise tolerance for individual signals (citing 'Imperfect Verifier') but does not explain why the additive structure prevents the compounding error problem that would plague a multiplicative/conjunctive combination. Making this argument explicit would strengthen the feasibility case.", "LOW: CoRGI (arXiv:2508.00378) has been withdrawn by its authors. The proposal should either remove this reference or note its withdrawal status. This is a minor issue since CoRGI is positioned as a tangential work (inference-only) and its removal does not affect the gap analysis.", "LOW: No precedent exists for a ≤4B model performing multi-property semantic verification (grounding + binding + completeness) in a single autoregressive pass for RL training. MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens — not as a training-time reward with throughput constraints. The proposal should acknowledge this gap more explicitly and discuss what minimum per-property accuracy would make the Tier 1 verifier useful (the 75% fallback threshold for binding is specified, but grounding and completeness thresholds are not)."]
Feedback: The proposal is approaching pass quality after five rounds of substantial improvement. Three focused changes would likely reach the threshold:

1. **Cite the Format Tax and D-CoT**: Add a brief paragraph acknowledging that 'The Format Tax' (arXiv:2604.03616) documents 7-11pp degradation from structured output in *prompted* open-weight models, but explicitly distinguish this from CFRL's RL-trained format: (a) D-CoT (arXiv:2602.21786) shows that models trained with structured tags internalize the structure and maintain performance even when tags are dropped at inference (+9.9% GPQA-diamond), (b) CFRL's curriculum develops citation as a learned skill via reward optimization, unlike MuRGAt's zero-shot format imposition where the degradation was observed. This turns a potential objection into a strength.

2. **Explicitly argue the additive reward advantage**: Add 1-2 sentences noting that the additive reward combination (weighted sum of independent verifier signals) is specifically chosen to avoid multiplicative error compounding. With additive combination and independent ~15% error per property, the noise in the composite signal shrinks rather than grows, keeping the training within the 'Imperfect Verifier' tolerance regime. This directly addresses the compounding error concern.

3. **Fix minor reference issues**: Note CoRGI's withdrawal. Specify minimum accuracy thresholds for grounding and completeness verification (currently only binding has a 75% fallback threshold).

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 5 轮修订，近 3 轮平均分从 3.6 到 3.8，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "442f40a9-bb5b-4a09-8a0b-defe60ece211",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T23:17:14.874Z_

```json
{
  "parentUuid": "442f40a9-bb5b-4a09-8a0b-defe60ece211",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
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
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "88c9c2fa-d631-431c-83cc-171804f7142a",
  "timestamp": "2026-05-27T23:17:14.874Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T23:17:14.874Z_

```json
{
  "parentUuid": "88c9c2fa-d631-431c-83cc-171804f7142a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "204b0661-9b9b-4258-948c-54925faa7a91",
  "timestamp": "2026-05-27T23:17:14.874Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "204b0661-9b9b-4258-948c-54925faa7a91",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Assistant

_source line 8 · 2026-05-27T23:17:23.882Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully. This is round 5, and the feedback suggests the proposal is "approaching pass quality" with "three focused changes" needed. The issues are all LOW or LOW-MEDIUM severity, which suggests minor fixes rather than major revision or pivot.

Let me break down what's needed:

1. **Format Tax + D-CoT citation**: Need to research these two papers and add appropriate discussion
2. **Additive reward advantage**: Need to explicitly argue why additive > multiplicative for noise tolerance
3. **Minor reference fixes**: CoRGI withdrawal, accuracy thresholds for grounding and completeness


The reviewer's framing of "three focused changes would likely reach the threshold" confirms these are targeted revisions, not a fundamental rethinking. I need to track down the specific papers mentioned—Format Tax and D-CoT—along with the current status of CoRGI to ensure I'm citing them accurately.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "204b0661-9b9b-4258-948c-54925faa7a91",
  "isSidechain": false,
  "requestId": "req_011CbTvhg7quGVdJiKJPCBCp",
  "type": "assistant",
  "uuid": "fec0aaf9-5e53-44f9-be7e-6eb2fd010120",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BCgaz5evYV4uqzFWYT738",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17462,
      "cache_read_input_tokens": 11014,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 399,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 17462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17462
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

_source line 9 · 2026-05-27T23:17:23.894Z_

I'll research the specific papers and issues raised by the reviewers before making revisions. Let me search for the Format Tax paper, D-CoT, and verify CoRGI's withdrawal status.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fec0aaf9-5e53-44f9-be7e-6eb2fd010120",
  "isSidechain": false,
  "requestId": "req_011CbTvhg7quGVdJiKJPCBCp",
  "type": "assistant",
  "uuid": "e08cf33e-09e3-4e91-bebe-c5ba8f459887",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BCgaz5evYV4uqzFWYT738",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17462,
      "cache_read_input_tokens": 11014,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 399,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 17462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17462
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

_source line 10 · 2026-05-27T23:17:24.138Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CkLFmwPGXpNaYHXMWLBpQW`</summary>

```json
{
  "query": "select:WebSearch,WebFetch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e08cf33e-09e3-4e91-bebe-c5ba8f459887",
  "isSidechain": false,
  "requestId": "req_011CbTvhg7quGVdJiKJPCBCp",
  "type": "assistant",
  "uuid": "9d5b866a-c377-47fc-8639-56e1aa1e45af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011BCgaz5evYV4uqzFWYT738",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17462,
      "cache_read_input_tokens": 11014,
      "output_tokens": 399,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17462,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 399,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 17462,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17462
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

_source line 11 · 2026-05-27T23:17:24.145Z_

<details><summary>↩ Tool result · `toolu_01CkLFmwPGXpNaYHXMWLBpQW`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9d5b866a-c377-47fc-8639-56e1aa1e45af",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "189beb9c-9c3e-40da-bcc2-aaa9eadf84ac",
  "toolUseResult": {
    "matches": [
      "WebSearch",
      "WebFetch"
    ],
    "query": "select:WebSearch,WebFetch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "9d5b866a-c377-47fc-8639-56e1aa1e45af",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-27T23:17:27.345Z_

Now let me research all the papers and issues in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "189beb9c-9c3e-40da-bcc2-aaa9eadf84ac",
  "isSidechain": false,
  "requestId": "req_011CbTviMrmo3szmyp12GWjn",
  "type": "assistant",
  "uuid": "84288081-455a-4325-b906-a5ed2e7ddf19",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dt7uYAD9xE2s1zgks5v5GZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 28476,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 28476,
          "cache_creation_input_tokens": 1418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1418
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

_source line 13 · 2026-05-27T23:17:27.631Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WMA6CY6GdKAukui4TNhX9K`</summary>

```json
{
  "query": "arXiv 2604.03616 \"Format Tax\" structured output reasoning degradation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84288081-455a-4325-b906-a5ed2e7ddf19",
  "isSidechain": false,
  "requestId": "req_011CbTviMrmo3szmyp12GWjn",
  "type": "assistant",
  "uuid": "9c693ba6-c57e-4b3a-bb34-f41a95c73c4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dt7uYAD9xE2s1zgks5v5GZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1418,
      "cache_read_input_tokens": 28476,
      "output_tokens": 84,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1418,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 84,
          "cache_read_input_tokens": 28476,
          "cache_creation_input_tokens": 1418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1418
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

_source line 14 · 2026-05-27T23:17:36.109Z_

<details><summary>↩ Tool result · `toolu_01WMA6CY6GdKAukui4TNhX9K`</summary>

```text
Web search results for query: "arXiv 2604.03616 "Format Tax" structured output reasoning degradation"

Links: [{"title":"[2604.03616] The Format Tax","url":"https://arxiv.org/abs/2604.03616"},{"title":"[2604.03616v1] The Format Tax","url":"https://arxiv.org/abs/2604.03616v1"},{"title":"The Format Tax","url":"https://arxiv.org/html/2604.03616v1"},{"title":"The Format Tax | Trending arXiv papers – Ribbit Ribbit","url":"https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"},{"title":"The Format Tax","url":"https://arxiv.org/pdf/2604.03616"},{"title":"Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models","url":"https://arxiv.org/html/2408.02442v1"},{"title":"The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models","url":"https://arxiv.org/html/2604.25359"},{"title":"Effects of structure on reasoning in instance-level Self-Discover","url":"https://arxiv.org/pdf/2507.03347"}]

I found the paper you're looking for. Here's what the research shows:

## "The Format Tax" (arXiv 2604.03616)

Structured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models.

The key findings of this paper by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick are:

**Source of Degradation:** While sampling bias accounts for only a fraction of the degradation, the dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied.

**Proposed Solution:** The paper points to a simple principle: decouple reasoning from formatting. Whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, separating the two concerns substantially recovers lost accuracy.

**Results:** Across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, decoupling recovers most lost accuracy. Additionally, most recent closed-weight models show little to no format tax, suggesting the problem is not inherent to structured generation but a gap that current open-weight models have yet to close.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c693ba6-c57e-4b3a-bb34-f41a95c73c4b",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "58f6db66-5f57-4d2d-ab50-1ca8e8e6ef8a",
  "toolUseResult": {
    "query": "arXiv 2604.03616 \"Format Tax\" structured output reasoning degradation",
    "results": [
      {
        "tool_use_id": "srvtoolu_017fJVF9z3mmLxEGqRT19LA9",
        "content": [
          {
            "title": "[2604.03616] The Format Tax",
            "url": "https://arxiv.org/abs/2604.03616"
          },
          {
            "title": "[2604.03616v1] The Format Tax",
            "url": "https://arxiv.org/abs/2604.03616v1"
          },
          {
            "title": "The Format Tax",
            "url": "https://arxiv.org/html/2604.03616v1"
          },
          {
            "title": "The Format Tax | Trending arXiv papers – Ribbit Ribbit",
            "url": "https://ribbitribbit.co/paper/arxiv.2604.03616-The-Format-Tax"
          },
          {
            "title": "The Format Tax",
            "url": "https://arxiv.org/pdf/2604.03616"
          },
          {
            "title": "Let Me Speak Freely? A Study on the Impact of Format Restrictions on Performance of Large Language Models",
            "url": "https://arxiv.org/html/2408.02442v1"
          },
          {
            "title": "The Structured Output Benchmark: A Multi-Source Benchmark for Evaluating Structured Output Quality in Large Language Models",
            "url": "https://arxiv.org/html/2604.25359"
          },
          {
            "title": "Effects of structure on reasoning in instance-level Self-Discover",
            "url": "https://arxiv.org/pdf/2507.03347"
          }
        ]
      },
      "I found the paper you're looking for. Here's what the research shows:\n\n## \"The Format Tax\" (arXiv 2604.03616)\n\nStructured output requirements—JSON, XML, LaTeX, Markdown—substantially degrade reasoning and writing performance across open-weight models.\n\nThe key findings of this paper by Ivan Yee Lee, Loris D'Antoni, and Taylor Berg-Kirkpatrick are:\n\n**Source of Degradation:** While sampling bias accounts for only a fraction of the degradation, the dominant cost enters at the prompt: format-requesting instructions alone cause most of the accuracy loss, before any decoder constraint is applied.\n\n**Proposed Solution:** The paper points to a simple principle: decouple reasoning from formatting. Whether by generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation, separating the two concerns substantially recovers lost accuracy.\n\n**Results:** Across six open-weight models, four API models, four formats, and tasks spanning math, science, logic, and writing, decoupling recovers most lost accuracy. Additionally, most recent closed-weight models show little to no format tax, suggesting the problem is not inherent to structured generation but a gap that current open-weight models have yet to close."
    ],
    "durationSeconds": 8.471812914,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c693ba6-c57e-4b3a-bb34-f41a95c73c4b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-27T23:17:38.743Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y3rC6U1g3yiypknXmnNgQa`</summary>

```json
{
  "query": "arXiv 2602.21786 D-CoT structured tags internalization trained models"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58f6db66-5f57-4d2d-ab50-1ca8e8e6ef8a",
  "isSidechain": false,
  "requestId": "req_011CbTvjEmAGTtbP36xoVHvz",
  "type": "assistant",
  "uuid": "db861eba-4796-4c4e-b488-0296ea7aa013",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RvqYdzUwy54cTfs5nxfhti",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 720,
      "cache_read_input_tokens": 29894,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 720,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 29894,
          "cache_creation_input_tokens": 720,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 720
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

_source line 16 · 2026-05-27T23:17:45.948Z_

<details><summary>↩ Tool result · `toolu_01Y3rC6U1g3yiypknXmnNgQa`</summary>

```text
Web search results for query: "arXiv 2602.21786 D-CoT structured tags internalization trained models"

Links: [{"title":"[2602.21786] D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models","url":"https://arxiv.org/abs/2602.21786"},{"title":"D-CoT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models","url":"https://arxiv.org/html/2602.21786"},{"title":"D-COT: Disciplined Chain-of-Thought Learning for Efficient ...","url":"https://arxiv.org/pdf/2602.21786"},{"title":"D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasonin…","url":"https://www.opentrain.ai/papers/d-cot-disciplined-chain-of-thought-learning-for-efficient-reasoning-in-small-lan--arxiv-2602.21786/"},{"title":"Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning","url":"https://arxiv.org/html/2502.04667v3"},{"title":"Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning","url":"https://arxiv.org/pdf/2502.04667"},{"title":"[2502.04667] Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning","url":"https://arxiv.org/abs/2502.04667"}]

Based on the search results, here's what I found about arXiv paper 2602.21786:

## D-CoT: Disciplined Chain-of-Thought Learning

The paper proposes Disciplined Chain-of-Thought (D-CoT), a novel framework that enforces a structured reasoning process using control tags -- such as for fact-checking and for multi-perspective exploration -- as auxiliary scaffolding during training.

### Key Innovation: Model Internalization

The model internalizes this disciplined thought structure, maintaining high performance even without explicit control tags during inference. This is a significant feature, as it means the structured reasoning process becomes embedded in the model itself rather than relying on explicit tags during use.

### Problem Being Addressed

Chain-of-Thought (CoT) distillation from Large Language Models (LLMs) often induces "overthinking" in Small Language Models (SLMs), leading to performance degradation and excessive token consumption. By optimizing the CoT trajectory, D-CoT suppresses reasoning drift and simultaneously achieves token reduction and performance improvement.

### Experimental Results

With only 5,000 training samples, D-CoT significantly boosts accuracy on GPQA-diamond by 9.9% and MMLU-Pro (0-shot) by 9.1%, while drastically reducing computational costs.

The paper was published on February 25, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "db861eba-4796-4c4e-b488-0296ea7aa013",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "a2805f87-dff5-4eae-87ff-ed4ad0464a65",
  "toolUseResult": {
    "query": "arXiv 2602.21786 D-CoT structured tags internalization trained models",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fjs8WL8MgSNe9Sbu4xd2vB",
        "content": [
          {
            "title": "[2602.21786] D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models",
            "url": "https://arxiv.org/abs/2602.21786"
          },
          {
            "title": "D-CoT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models",
            "url": "https://arxiv.org/html/2602.21786"
          },
          {
            "title": "D-COT: Disciplined Chain-of-Thought Learning for Efficient ...",
            "url": "https://arxiv.org/pdf/2602.21786"
          },
          {
            "title": "D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasonin…",
            "url": "https://www.opentrain.ai/papers/d-cot-disciplined-chain-of-thought-learning-for-efficient-reasoning-in-small-lan--arxiv-2602.21786/"
          },
          {
            "title": "Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning",
            "url": "https://arxiv.org/html/2502.04667v3"
          },
          {
            "title": "Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning",
            "url": "https://arxiv.org/pdf/2502.04667"
          },
          {
            "title": "[2502.04667] Compositional Generalization from Learned Skills via CoT Training: A Theoretical and Structural Analysis for Reasoning",
            "url": "https://arxiv.org/abs/2502.04667"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2602.21786:\n\n## D-CoT: Disciplined Chain-of-Thought Learning\n\nThe paper proposes Disciplined Chain-of-Thought (D-CoT), a novel framework that enforces a structured reasoning process using control tags -- such as for fact-checking and for multi-perspective exploration -- as auxiliary scaffolding during training.\n\n### Key Innovation: Model Internalization\n\nThe model internalizes this disciplined thought structure, maintaining high performance even without explicit control tags during inference. This is a significant feature, as it means the structured reasoning process becomes embedded in the model itself rather than relying on explicit tags during use.\n\n### Problem Being Addressed\n\nChain-of-Thought (CoT) distillation from Large Language Models (LLMs) often induces \"overthinking\" in Small Language Models (SLMs), leading to performance degradation and excessive token consumption. By optimizing the CoT trajectory, D-CoT suppresses reasoning drift and simultaneously achieves token reduction and performance improvement.\n\n### Experimental Results\n\nWith only 5,000 training samples, D-CoT significantly boosts accuracy on GPQA-diamond by 9.9% and MMLU-Pro (0-shot) by 9.1%, while drastically reducing computational costs.\n\nThe paper was published on February 25, 2026."
    ],
    "durationSeconds": 7.200360219000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "db861eba-4796-4c4e-b488-0296ea7aa013",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-27T23:17:48.518Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016CHjgmacLPFkwSJBWQiEBG`</summary>

```json
{
  "query": "arXiv 2508.00378 CoRGI withdrawn retracted chain-of-thought visual grounding"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a2805f87-dff5-4eae-87ff-ed4ad0464a65",
  "isSidechain": false,
  "requestId": "req_011CbTvjxo1CjrZaP7c3oH1w",
  "type": "assistant",
  "uuid": "16b715a0-94fe-4eb2-92ab-f8496deee9fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014p1d7atJCeBM4W6PSYwrZn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 811,
      "cache_read_input_tokens": 30614,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 811,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 30614,
          "cache_creation_input_tokens": 811,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 811
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

_source line 18 · 2026-05-27T23:17:55.099Z_

<details><summary>↩ Tool result · `toolu_016CHjgmacLPFkwSJBWQiEBG`</summary>

```text
Web search results for query: "arXiv 2508.00378 CoRGI withdrawn retracted chain-of-thought visual grounding"

Links: [{"title":"[2508.00378] CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding","url":"https://arxiv.org/abs/2508.00378"},{"title":"Computer Science Aug 2025","url":"https://www.arxiv.org/list/cs/2025-08?skip=150&show=500"},{"title":"Retracted: Genetic Algorithm in Data Mining of Colorectal Images","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10718703/"},{"title":"Mathematician withdraws preprint – 24 years after initial submission – Retraction Watch","url":"https://retractionwatch.com/2022/12/12/mathematician-withdraws-preprint-24-years-after-initial-submission/"},{"title":"Retracted: Identification and Validation of a Novel Prognostic Gene Model for Colorectal Cancer","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700771/"},{"title":"Sabine Hossenfelder: Backreaction: Withdrawal","url":"http://backreaction.blogspot.com/2007/08/withdrawal.html"},{"title":"Retracted randomized trials attributed to super-retractors and top-cited scientists with multiple retractions: secondary analysis of the VITALITY retrospective cohort","url":"https://www.medrxiv.org/content/10.1101/2025.11.23.25340834.full.pdf"}]

Based on the search results, I can provide you with information about arXiv paper 2508.00378:

CoRGI (Chain of Reasoning with Grounded Insights) is a framework that enhances reasoning reliability through post-hoc verification of chain-of-thought outputs. Given a VLM-generated rationale, CoRGI decomposes it into step-wise statements, grounds each step in visual evidence, and filters or corrects unsupported claims before producing the final answer.

The paper demonstrates that CoRGI consistently improves both answer accuracy and explanation faithfulness across multiple VLM backbones, including Qwen-2.5VL, LLaVA-1.6, and Gemma3-12B, when tested on five challenging benchmarks: VCR, ScienceQA, MMMU, MathVista, and HallusionBench.

Regarding the withdrawal status: The paper has been withdrawn, with the version history showing [v3] Tue, 14 Oct 2025 09:15:36 UTC (1 KB) (withdrawn). The authors noted that "The paper is not yet mature and needs further improvement" as their reason for the withdrawal.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16b715a0-94fe-4eb2-92ab-f8496deee9fd",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "cde9e950-3dcc-4b06-83bf-cc7aa350fd53",
  "toolUseResult": {
    "query": "arXiv 2508.00378 CoRGI withdrawn retracted chain-of-thought visual grounding",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GFk34fM7qjv17ADUuj8h3q",
        "content": [
          {
            "title": "[2508.00378] CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding",
            "url": "https://arxiv.org/abs/2508.00378"
          },
          {
            "title": "Computer Science Aug 2025",
            "url": "https://www.arxiv.org/list/cs/2025-08?skip=150&show=500"
          },
          {
            "title": "Retracted: Genetic Algorithm in Data Mining of Colorectal Images",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10718703/"
          },
          {
            "title": "Mathematician withdraws preprint – 24 years after initial submission – Retraction Watch",
            "url": "https://retractionwatch.com/2022/12/12/mathematician-withdraws-preprint-24-years-after-initial-submission/"
          },
          {
            "title": "Retracted: Identification and Validation of a Novel Prognostic Gene Model for Colorectal Cancer",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700771/"
          },
          {
            "title": "Sabine Hossenfelder: Backreaction: Withdrawal",
            "url": "http://backreaction.blogspot.com/2007/08/withdrawal.html"
          },
          {
            "title": "Retracted randomized trials attributed to super-retractors and top-cited scientists with multiple retractions: secondary analysis of the VITALITY retrospective cohort",
            "url": "https://www.medrxiv.org/content/10.1101/2025.11.23.25340834.full.pdf"
          }
        ]
      },
      "Based on the search results, I can provide you with information about arXiv paper 2508.00378:\n\nCoRGI (Chain of Reasoning with Grounded Insights) is a framework that enhances reasoning reliability through post-hoc verification of chain-of-thought outputs. Given a VLM-generated rationale, CoRGI decomposes it into step-wise statements, grounds each step in visual evidence, and filters or corrects unsupported claims before producing the final answer.\n\nThe paper demonstrates that CoRGI consistently improves both answer accuracy and explanation faithfulness across multiple VLM backbones, including Qwen-2.5VL, LLaVA-1.6, and Gemma3-12B, when tested on five challenging benchmarks: VCR, ScienceQA, MMMU, MathVista, and HallusionBench.\n\nRegarding the withdrawal status: The paper has been withdrawn, with the version history showing [v3] Tue, 14 Oct 2025 09:15:36 UTC (1 KB) (withdrawn). The authors noted that \"The paper is not yet mature and needs further improvement\" as their reason for the withdrawal."
    ],
    "durationSeconds": 6.577122349999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "16b715a0-94fe-4eb2-92ab-f8496deee9fd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-27T23:17:59.426Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01K75BK9X8bMBAEJCYKMZBDX`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.03616",
  "prompt": "Extract the key findings: 1) What specific models were tested? 2) What was the magnitude of reasoning degradation (exact percentages)? 3) What formats were tested (XML, JSON, etc.)? 4) What was the finding about closed-weight vs open-weight models? 5) What was the proposed decoupling solution? 6) Any findings specifically about RL-trained models vs prompted models?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cde9e950-3dcc-4b06-83bf-cc7aa350fd53",
  "isSidechain": false,
  "requestId": "req_011CbTvkdvUUbXxvHKnk3uBZ",
  "type": "assistant",
  "uuid": "30c1cc7f-bf33-4f37-a76a-4fafb056c1e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013QSr6xfr3wj4HyjU1B7JVm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 793,
      "cache_read_input_tokens": 31425,
      "output_tokens": 173,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 793,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 173,
          "cache_read_input_tokens": 31425,
          "cache_creation_input_tokens": 793,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 793
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

_source line 20 · 2026-05-27T23:18:04.360Z_

<details><summary>↩ Tool result · `toolu_01K75BK9X8bMBAEJCYKMZBDX`</summary>

```text
# Key Findings from "The Format Tax" Paper

Based on the abstract provided, here's what can be extracted:

**1) Models Tested:**
The paper evaluated "six open-weight models, four API models" but specific model names are not listed in this excerpt.

**2) Magnitude of Degradation:**
No exact percentages are provided in the abstract. It only states that structured output requirements "substantially degrade" performance.

**3) Formats Tested:**
The paper examined "JSON, XML, LaTeX, Markdown" as required output structures.

**4) Closed vs. Open-Weight Models:**
A significant finding was that "most recent closed-weight models show little to no format tax," whereas open-weight models experienced notable degradation. This suggests the problem is addressable rather than inherent.

**5) Decoupling Solution:**
The researchers found that "decouple reasoning from formatting" through two approaches: "generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation" substantially recovered lost accuracy.

**6) RL-Trained vs. Prompted Models:**
This distinction is not discussed in the provided abstract excerpt.

**Note:** For specific percentages, detailed model names, and additional findings, the full paper PDF would need to be consulted.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "30c1cc7f-bf33-4f37-a76a-4fafb056c1e3",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "1fe1f69b-eb36-4c79-8eea-e61e3eae0954",
  "toolUseResult": {
    "bytes": 45387,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Findings from \"The Format Tax\" Paper\n\nBased on the abstract provided, here's what can be extracted:\n\n**1) Models Tested:**\nThe paper evaluated \"six open-weight models, four API models\" but specific model names are not listed in this excerpt.\n\n**2) Magnitude of Degradation:**\nNo exact percentages are provided in the abstract. It only states that structured output requirements \"substantially degrade\" performance.\n\n**3) Formats Tested:**\nThe paper examined \"JSON, XML, LaTeX, Markdown\" as required output structures.\n\n**4) Closed vs. Open-Weight Models:**\nA significant finding was that \"most recent closed-weight models show little to no format tax,\" whereas open-weight models experienced notable degradation. This suggests the problem is addressable rather than inherent.\n\n**5) Decoupling Solution:**\nThe researchers found that \"decouple reasoning from formatting\" through two approaches: \"generating freeform first and reformatting in a second pass, or by enabling extended thinking within a single generation\" substantially recovered lost accuracy.\n\n**6) RL-Trained vs. Prompted Models:**\nThis distinction is not discussed in the provided abstract excerpt.\n\n**Note:** For specific percentages, detailed model names, and additional findings, the full paper PDF would need to be consulted.",
    "durationMs": 4930,
    "url": "https://arxiv.org/abs/2604.03616"
  },
  "sourceToolAssistantUUID": "30c1cc7f-bf33-4f37-a76a-4fafb056c1e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "1fe1f69b-eb36-4c79-8eea-e61e3eae0954",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Tool call

_source line 23 · 2026-05-27T23:18:09.303Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Hw5Biiu3PtGZLw3NmwmG5v`</summary>

```json
{
  "url": "https://arxiv.org/html/2604.03616v1",
  "prompt": "Extract: 1) The specific 7-11pp degradation numbers - what tasks/models show this range? 2) Which open-weight models were tested (exact names)? 3) Any discussion of whether RL training or fine-tuning mitigates the format tax? 4) The exact findings about XML format specifically. 5) Any distinction between inference-time prompting and training-time format enforcement? 6) Key tables or results showing the degradation magnitude."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1fe1f69b-eb36-4c79-8eea-e61e3eae0954",
  "isSidechain": false,
  "requestId": "req_011CbTvmKWiWixDphwqspRtJ",
  "type": "assistant",
  "uuid": "d540503e-cf69-456a-b25e-d67a24cabe89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0119JTqa51spSvMVSL4R3Gqn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 474,
      "cache_read_input_tokens": 32218,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 474,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 32218,
          "cache_creation_input_tokens": 474,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 474
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

_source line 24 · 2026-05-27T23:18:16.925Z_

<details><summary>↩ Tool result · `toolu_01Hw5Biiu3PtGZLw3NmwmG5v`</summary>

```text
# Key Findings from "The Format Tax" Research

## 1) Degradation Range Across Tasks/Models

The 7-11pp degradation appears across multiple combinations. Table 3 shows open-weight models averaging **-5.8pp to -8.7pp** across GPQA, MATH-500, and ZebraLogic. The paper notes that "accuracy decreases relative to freeform generation" consistently, though severity varies by task.

## 2) Open-Weight Models Tested

Six models were evaluated locally via vLLM:
- Qwen3-32b and Qwen3-8b
- OLMo3.1-32b and OLMo3-7b
- SmolLM3-3b
- Nemotron3-nano

## 3) Training Interventions

The paper does **not extensively discuss RL training or fine-tuning mitigation**. Instead, it emphasizes that newer closed-weight models (Claude-Haiku-4.5, GPT-5.4-nano) already demonstrate resistance to the tax, suggesting "the problem is solvable." The focus remains on inference-time strategies like 2-Turn generation and extended thinking.

## 4) XML Format Findings

XML showed "mixed degradation across models." The research indicates XML generally performed similarly to JSON and LaTeX, without consistently outperforming other formats.

## 5) Inference vs. Training Distinction

The study isolates **prompt-level costs entering before generation begins**, separating this from decoder-level constraints. However, it doesn't compare inference-time prompting against training-time format enforcement directly.

## 6) Key Degradation Results

Figure 1 and Table 3 demonstrate that format-requesting prompts alone cause most accuracy loss **before constrained decoding applies**—approximately **-3.9pp baseline versus -1.6pp additional from grammar constraints**.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d540503e-cf69-456a-b25e-d67a24cabe89",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "0420944a-062e-4ac3-8ac9-e40bf72fefc0",
  "toolUseResult": {
    "bytes": 802432,
    "code": 200,
    "codeText": "OK",
    "result": "# Key Findings from \"The Format Tax\" Research\n\n## 1) Degradation Range Across Tasks/Models\n\nThe 7-11pp degradation appears across multiple combinations. Table 3 shows open-weight models averaging **-5.8pp to -8.7pp** across GPQA, MATH-500, and ZebraLogic. The paper notes that \"accuracy decreases relative to freeform generation\" consistently, though severity varies by task.\n\n## 2) Open-Weight Models Tested\n\nSix models were evaluated locally via vLLM:\n- Qwen3-32b and Qwen3-8b\n- OLMo3.1-32b and OLMo3-7b\n- SmolLM3-3b\n- Nemotron3-nano\n\n## 3) Training Interventions\n\nThe paper does **not extensively discuss RL training or fine-tuning mitigation**. Instead, it emphasizes that newer closed-weight models (Claude-Haiku-4.5, GPT-5.4-nano) already demonstrate resistance to the tax, suggesting \"the problem is solvable.\" The focus remains on inference-time strategies like 2-Turn generation and extended thinking.\n\n## 4) XML Format Findings\n\nXML showed \"mixed degradation across models.\" The research indicates XML generally performed similarly to JSON and LaTeX, without consistently outperforming other formats.\n\n## 5) Inference vs. Training Distinction\n\nThe study isolates **prompt-level costs entering before generation begins**, separating this from decoder-level constraints. However, it doesn't compare inference-time prompting against training-time format enforcement directly.\n\n## 6) Key Degradation Results\n\nFigure 1 and Table 3 demonstrate that format-requesting prompts alone cause most accuracy loss **before constrained decoding applies**—approximately **-3.9pp baseline versus -1.6pp additional from grammar constraints**.",
    "durationMs": 7618,
    "url": "https://arxiv.org/html/2604.03616v1"
  },
  "sourceToolAssistantUUID": "d540503e-cf69-456a-b25e-d67a24cabe89",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-27T23:18:21.584Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Y8mLkhwvHscjBNnCeNbhGM`</summary>

```json
{
  "url": "https://arxiv.org/html/2602.21786",
  "prompt": "Extract: 1) The exact +9.9% GPQA-diamond result and context. 2) What control tags were used and how they work? 3) How does the model internalize structured tags - what evidence? 4) Performance with tags removed at inference time vs with tags. 5) What base models were used? 6) How many training samples? 7) Any discussion of format overhead or 'format tax' mitigation?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0420944a-062e-4ac3-8ac9-e40bf72fefc0",
  "isSidechain": false,
  "requestId": "req_011CbTvnFVQJJL84b98yWtQd",
  "type": "assistant",
  "uuid": "1deecd1a-1828-42d3-bdd0-fb12e109824d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015hvZWMUyJpSfmwZ9Ywnd4r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 629,
      "cache_read_input_tokens": 32692,
      "output_tokens": 179,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 629,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 179,
          "cache_read_input_tokens": 32692,
          "cache_creation_input_tokens": 629,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 629
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

_source line 26 · 2026-05-27T23:18:30.076Z_

<details><summary>↩ Tool result · `toolu_01Y8mLkhwvHscjBNnCeNbhGM`</summary>

```text
# D-CoT Key Findings Extract

## 1) GPQA-diamond +9.9% Result
The paper reports: "D-CoT (Dynamic/Custom) achieved 52.93% accuracy, outperforming the Base model (43.03%) by 9.9 points." This improvement occurred on the "extremely difficult science/expert questions" benchmark with only ~5,000 training samples.

## 2) Control Tags and Function
Three tags structure reasoning phases:

| Tag | Purpose |
|-----|---------|
| `&lt;TEMP_LOW>` | "Fact-checking, listing prerequisites, and constraints" |
| `&lt;TEMP_MID>` | "Normal response, algorithmic processing, and calculation" |
| `&lt;TEMP_HIGH>` | "Creative solutions, multi-perspective viewpoints" |

The sequence is flexible, determined by task requirements rather than fixed ordering.

## 3) Internalization Evidence
The model internalized discipline without explicit tags. The paper identifies three behavioral shifts:

- **Implicit fact organization**: Models begin with structured premise enumeration without tag prompts
- **Directed self-checking**: Models perform single, focused verification instead of entering endless "Wait, but..." loops
- **Suppressed unnecessary arithmetic**: Models skip lengthy step-by-step simulations

## 4) Performance: Tagged vs. Untagged Inference
Remarkably, the highest MMLU-Pro accuracy (64.73%) occurred *without* explicit tags during inference, compared to 62.92% with locked temperature and tags. This suggests "outputting control tags consumes inference resources...that could otherwise be allocated to reasoning."

## 5) Base Models
The study used **Qwen3-8B** as the training base, with teacher model generation via **Qwen3-235B-Instruct** through OpenRouter API.

## 6) Training Sample Count
The final dataset contained **5,079 Chosen/Rejected pairs** after decontamination filtering (originally 5,181 samples generated).

## 7) Format Overhead Discussion
The paper hypothesizes that explicit tags create overhead: they "consume inference resources (tokens and attention capacity)" and "may occasionally interrupt the model's natural reasoning flow." However, no explicit "format tax" quantification is provided beyond noting dynamic temperature improvements were marginal (0.51–1.52 points).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1deecd1a-1828-42d3-bdd0-fb12e109824d",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "2df96587-a7fd-4d9b-a68d-4e7e8c5b05f2",
  "toolUseResult": {
    "bytes": 74186,
    "code": 200,
    "codeText": "OK",
    "result": "# D-CoT Key Findings Extract\n\n## 1) GPQA-diamond +9.9% Result\nThe paper reports: \"D-CoT (Dynamic/Custom) achieved 52.93% accuracy, outperforming the Base model (43.03%) by 9.9 points.\" This improvement occurred on the \"extremely difficult science/expert questions\" benchmark with only ~5,000 training samples.\n\n## 2) Control Tags and Function\nThree tags structure reasoning phases:\n\n| Tag | Purpose |\n|-----|---------|\n| `&lt;TEMP_LOW>` | \"Fact-checking, listing prerequisites, and constraints\" |\n| `&lt;TEMP_MID>` | \"Normal response, algorithmic processing, and calculation\" |\n| `&lt;TEMP_HIGH>` | \"Creative solutions, multi-perspective viewpoints\" |\n\nThe sequence is flexible, determined by task requirements rather than fixed ordering.\n\n## 3) Internalization Evidence\nThe model internalized discipline without explicit tags. The paper identifies three behavioral shifts:\n\n- **Implicit fact organization**: Models begin with structured premise enumeration without tag prompts\n- **Directed self-checking**: Models perform single, focused verification instead of entering endless \"Wait, but...\" loops\n- **Suppressed unnecessary arithmetic**: Models skip lengthy step-by-step simulations\n\n## 4) Performance: Tagged vs. Untagged Inference\nRemarkably, the highest MMLU-Pro accuracy (64.73%) occurred *without* explicit tags during inference, compared to 62.92% with locked temperature and tags. This suggests \"outputting control tags consumes inference resources...that could otherwise be allocated to reasoning.\"\n\n## 5) Base Models\nThe study used **Qwen3-8B** as the training base, with teacher model generation via **Qwen3-235B-Instruct** through OpenRouter API.\n\n## 6) Training Sample Count\nThe final dataset contained **5,079 Chosen/Rejected pairs** after decontamination filtering (originally 5,181 samples generated).\n\n## 7) Format Overhead Discussion\nThe paper hypothesizes that explicit tags create overhead: they \"consume inference resources (tokens and attention capacity)\" and \"may occasionally interrupt the model's natural reasoning flow.\" However, no explicit \"format tax\" quantification is provided beyond noting dynamic temperature improvements were marginal (0.51–1.52 points).",
    "durationMs": 8488,
    "url": "https://arxiv.org/html/2602.21786"
  },
  "sourceToolAssistantUUID": "1deecd1a-1828-42d3-bdd0-fb12e109824d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-27T23:18:32.704Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WiuC1Bvg2jPaGTX4CWW1Sh`</summary>

```json
{
  "query": "additive vs multiplicative reward combination reinforcement learning noise tolerance error cancellation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2df96587-a7fd-4d9b-a68d-4e7e8c5b05f2",
  "isSidechain": false,
  "requestId": "req_011CbTvoDTtaMsgMLg9X1u4S",
  "type": "assistant",
  "uuid": "b8e03d50-ac4b-435a-86bd-e88d5a8611b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ToGJvXuJB6uNew8q5kAAXR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 724,
      "cache_read_input_tokens": 33321,
      "output_tokens": 66,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 724,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 66,
          "cache_read_input_tokens": 33321,
          "cache_creation_input_tokens": 724,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 724
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

_source line 28 · 2026-05-27T23:18:40.014Z_

<details><summary>↩ Tool result · `toolu_01WiuC1Bvg2jPaGTX4CWW1Sh`</summary>

```text
Web search results for query: "additive vs multiplicative reward combination reinforcement learning noise tolerance error cancellation"

Links: [{"title":"A multiplicative reinforcement learning model capturing learning dynamics and interindividual variability in mice - PMC","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3856837/"},{"title":"Multiplicative Rewards in Markovian Models","url":"https://arxiv.org/html/2504.18277"},{"title":"A multiplicative reinforcement learning model capturing learning dynamics and interindividual variability in mice | PNAS","url":"https://www.pnas.org/doi/10.1073/pnas.1312125110"},{"title":"Submodular Reinforcement Learning","url":"https://arxiv.org/pdf/2307.13372"},{"title":"Multiplicative Rewards in Markovian Models","url":"https://arxiv.org/pdf/2504.18277"},{"title":"An exact solution in Markov decision process with multiplicative rewards   as a general framework","url":"https://arxiv.org/pdf/2012.08074"},{"title":"Global Reinforcement Learning: Beyond Linear and Convex Rewards via   Submodular Semi-gradient Methods","url":"https://arxiv.org/pdf/2407.09905"}]

Based on the web search results, here's what I found about additive vs multiplicative reward combinations in reinforcement learning:

## Key Differences

Additive rewards accumulate by summing rewards obtained in each step, while multiplicative rewards are obtained by multiplying rewards instead.

## Learning Dynamics

In multiplicative learning rules, the starting connectivity values of the model strongly determine the shape of learning curves, in contrast to additive rules where learning speed is typically determined by a single parameter. Additionally, the additive model is learned more slowly during reversal training.

## Noise Tolerance

Notably, with multiplicative accumulation of rewards, the optimal policy is noise dependent in contrast to additive accumulation. This suggests that multiplicative approaches may handle noise differently than additive ones, potentially adapting policies based on noise characteristics.

## Mathematical Properties

One of the key differences to additive rewards is that with multiplicative rewards the expected value may diverge. The multiplicative scheme is shown to be a general framework that covers the additive one with arbitrary precision.

## Applications

While RL typically considers rewards as additive following the Markov assumption, in many important applications such as coverage control and informative path planning, rewards naturally have diminishing returns, suggesting contexts where non-additive (like multiplicative) approaches may be more appropriate.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b8e03d50-ac4b-435a-86bd-e88d5a8611b0",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "37cb9bf4-7d6c-4e81-b227-4766a3e4e3ca",
  "toolUseResult": {
    "query": "additive vs multiplicative reward combination reinforcement learning noise tolerance error cancellation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PxQRHhaDPRuSz5fTi9Y72q",
        "content": [
          {
            "title": "A multiplicative reinforcement learning model capturing learning dynamics and interindividual variability in mice - PMC",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3856837/"
          },
          {
            "title": "Multiplicative Rewards in Markovian Models",
            "url": "https://arxiv.org/html/2504.18277"
          },
          {
            "title": "A multiplicative reinforcement learning model capturing learning dynamics and interindividual variability in mice | PNAS",
            "url": "https://www.pnas.org/doi/10.1073/pnas.1312125110"
          },
          {
            "title": "Submodular Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2307.13372"
          },
          {
            "title": "Multiplicative Rewards in Markovian Models",
            "url": "https://arxiv.org/pdf/2504.18277"
          },
          {
            "title": "An exact solution in Markov decision process with multiplicative rewards   as a general framework",
            "url": "https://arxiv.org/pdf/2012.08074"
          },
          {
            "title": "Global Reinforcement Learning: Beyond Linear and Convex Rewards via   Submodular Semi-gradient Methods",
            "url": "https://arxiv.org/pdf/2407.09905"
          }
        ]
      },
      "Based on the web search results, here's what I found about additive vs multiplicative reward combinations in reinforcement learning:\n\n## Key Differences\n\nAdditive rewards accumulate by summing rewards obtained in each step, while multiplicative rewards are obtained by multiplying rewards instead.\n\n## Learning Dynamics\n\nIn multiplicative learning rules, the starting connectivity values of the model strongly determine the shape of learning curves, in contrast to additive rules where learning speed is typically determined by a single parameter. Additionally, the additive model is learned more slowly during reversal training.\n\n## Noise Tolerance\n\nNotably, with multiplicative accumulation of rewards, the optimal policy is noise dependent in contrast to additive accumulation. This suggests that multiplicative approaches may handle noise differently than additive ones, potentially adapting policies based on noise characteristics.\n\n## Mathematical Properties\n\nOne of the key differences to additive rewards is that with multiplicative rewards the expected value may diverge. The multiplicative scheme is shown to be a general framework that covers the additive one with arbitrary precision.\n\n## Applications\n\nWhile RL typically considers rewards as additive following the Markov assumption, in many important applications such as coverage control and informative path planning, rewards naturally have diminishing returns, suggesting contexts where non-additive (like multiplicative) approaches may be more appropriate."
    ],
    "durationSeconds": 7.305830306000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b8e03d50-ac4b-435a-86bd-e88d5a8611b0",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-27T23:18:40.019Z_

```json
{
  "parentUuid": "37cb9bf4-7d6c-4e81-b227-4766a3e4e3ca",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "40e4a12a-c073-4fbe-8b9e-6f8ed5b3e08e",
  "timestamp": "2026-05-27T23:18:40.019Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-27T23:18:43.359Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VNvhk7zcecbDRsezDF3Hr8`</summary>

```json
{
  "query": "\"small model\" \"4B\" OR \"3B\" verifier reward model multimodal verification single pass accuracy 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "40e4a12a-c073-4fbe-8b9e-6f8ed5b3e08e",
  "isSidechain": false,
  "requestId": "req_011CbTvowyFfZUiCE5nXR3AC",
  "type": "assistant",
  "uuid": "c032b6e4-7508-4a70-82d2-4a5af32d9c9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015t4horjymmaNsGVH6573uG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 792,
      "cache_read_input_tokens": 34045,
      "output_tokens": 78,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 792,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 78,
          "cache_read_input_tokens": 34045,
          "cache_creation_input_tokens": 792,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 792
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

_source line 31 · 2026-05-27T23:18:49.897Z_

<details><summary>↩ Tool result · `toolu_01VNvhk7zcecbDRsezDF3Hr8`</summary>

```text
Web search results for query: ""small model" "4B" OR "3B" verifier reward model multimodal verification single pass accuracy 2026"

Links: [{"title":"The 4B Class of 2026: Comparing Efficiency Across Emerging Reasoning Models · Technical news about AI, coding and all","url":"https://dasroot.net/posts/2026/04/4b-class-2026-comparing-efficiency-emerging-reasoning-models/"},{"title":"Mistral AI Releases Mistral Small 4: A 119B-Parameter MoE Model that Unifies Instruct, Reasoning, and Multimodal Workloads - MarkTechPost","url":"https://www.marktechpost.com/2026/03/16/mistral-ai-releases-mistral-small-4-a-119b-parameter-moe-model-that-unifies-instruct-reasoning-and-multimodal-workloads/"},{"title":"The Best Open-Source Small Language Models (SLMs) in 2026","url":"https://www.bentoml.com/blog/the-best-open-source-small-language-models"},{"title":"Small Language Model Leaderboard: Best Under 10B | Awesome Agents","url":"https://awesomeagents.ai/leaderboards/small-language-model-leaderboard/"},{"title":"Qwen3.6-35B-A3B: The Small Model That Codes Like a Giant","url":"https://www.labellerr.com/blog/qwen3-6-35b-a3b-open-source-ai-model/"},{"title":"MJ1: Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/pdf/2603.07990"},{"title":": Multimodal Judgment via Grounded Verification","url":"https://arxiv.org/html/2603.07990v1"}]

I found relevant results for your search. Here are the key findings:

## Small Model Verifier/Reward Models with 3B-4B Parameters

MJ1, with only 3B active parameters, achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro. MJ1 is an RL-trained multimodal judge that achieves state-of-the-art performance on MMRB2 with only 3B active parameters.

MJ1 substantially outperforms models with orders of magnitude more parameters, reinforcing findings that the training recipe matters more than model scale for judgment tasks.

## Other Relevant 3B-4B Models in 2026

Qwen3.6-35B-A3B is a breakthrough open-source AI model combining 35B capacity with 3B active parameters, released on April 16, 2026. It delivers strong coding, reasoning, and multimodal performance at a fraction of the cost.

SmolLM3-3B at the 3B scale outperforms Llama-3.2-3B and Qwen2.5-3B, while staying competitive with many 4B-class alternatives across 12 popular benchmarks.

The search results indicate that small models in the 3B-4B parameter range with multimodal capabilities have made significant advances in 2026, particularly in verification and judgment tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c032b6e4-7508-4a70-82d2-4a5af32d9c9d",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "d2413545-83a5-4e56-8c6d-d64673373905",
  "toolUseResult": {
    "query": "\"small model\" \"4B\" OR \"3B\" verifier reward model multimodal verification single pass accuracy 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MmokYb5r77dzoHvS46hmdu",
        "content": [
          {
            "title": "The 4B Class of 2026: Comparing Efficiency Across Emerging Reasoning Models · Technical news about AI, coding and all",
            "url": "https://dasroot.net/posts/2026/04/4b-class-2026-comparing-efficiency-emerging-reasoning-models/"
          },
          {
            "title": "Mistral AI Releases Mistral Small 4: A 119B-Parameter MoE Model that Unifies Instruct, Reasoning, and Multimodal Workloads - MarkTechPost",
            "url": "https://www.marktechpost.com/2026/03/16/mistral-ai-releases-mistral-small-4-a-119b-parameter-moe-model-that-unifies-instruct-reasoning-and-multimodal-workloads/"
          },
          {
            "title": "The Best Open-Source Small Language Models (SLMs) in 2026",
            "url": "https://www.bentoml.com/blog/the-best-open-source-small-language-models"
          },
          {
            "title": "Small Language Model Leaderboard: Best Under 10B | Awesome Agents",
            "url": "https://awesomeagents.ai/leaderboards/small-language-model-leaderboard/"
          },
          {
            "title": "Qwen3.6-35B-A3B: The Small Model That Codes Like a Giant",
            "url": "https://www.labellerr.com/blog/qwen3-6-35b-a3b-open-source-ai-model/"
          },
          {
            "title": "MJ1: Multimodal Judgment via Grounded Verification",
            "url": "https://arxiv.org/pdf/2603.07990"
          },
          {
            "title": ": Multimodal Judgment via Grounded Verification",
            "url": "https://arxiv.org/html/2603.07990v1"
          }
        ]
      },
      "I found relevant results for your search. Here are the key findings:\n\n## Small Model Verifier/Reward Models with 3B-4B Parameters\n\nMJ1, with only 3B active parameters, achieves 77.0% accuracy on MMRB2 and surpasses orders-of-magnitude larger models like Gemini-3-Pro. MJ1 is an RL-trained multimodal judge that achieves state-of-the-art performance on MMRB2 with only 3B active parameters.\n\nMJ1 substantially outperforms models with orders of magnitude more parameters, reinforcing findings that the training recipe matters more than model scale for judgment tasks.\n\n## Other Relevant 3B-4B Models in 2026\n\nQwen3.6-35B-A3B is a breakthrough open-source AI model combining 35B capacity with 3B active parameters, released on April 16, 2026. It delivers strong coding, reasoning, and multimodal performance at a fraction of the cost.\n\nSmolLM3-3B at the 3B scale outperforms Llama-3.2-3B and Qwen2.5-3B, while staying competitive with many 4B-class alternatives across 12 popular benchmarks.\n\nThe search results indicate that small models in the 3B-4B parameter range with multimodal capabilities have made significant advances in 2026, particularly in verification and judgment tasks."
    ],
    "durationSeconds": 6.533178770999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c032b6e4-7508-4a70-82d2-4a5af32d9c9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-27T23:18:52.961Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016wjSi4XWWNGygdCN51VnD3`</summary>

```json
{
  "query": "small verifier reward model accuracy threshold minimum useful reinforcement learning training 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d2413545-83a5-4e56-8c6d-d64673373905",
  "isSidechain": false,
  "requestId": "req_011CbTvpgMBW7bjiLVQ3RXPw",
  "type": "assistant",
  "uuid": "f450e5b3-07c8-4568-98b4-f3d1963ec776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01B5Si6o5Ydn5BmQbSUMcFSz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 904,
      "cache_read_input_tokens": 34837,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 904,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 34837,
          "cache_creation_input_tokens": 904,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 904
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

_source line 33 · 2026-05-27T23:19:01.542Z_

<details><summary>↩ Tool result · `toolu_016wjSi4XWWNGygdCN51VnD3`</summary>

```text
Web search results for query: "small verifier reward model accuracy threshold minimum useful reinforcement learning training 2025 2026"

Links: [{"title":"RLVR: Verifiable Rewards for Reliable Enterprise LLMs | Appen","url":"https://www.appen.com/blog/rlvr"},{"title":"Reinforcement Learning with Verifiable Rewards Implicitly ...","url":"https://arxiv.org/pdf/2506.14245"},{"title":"GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub","url":"https://github.com/opendilab/awesome-RLVR"},{"title":"Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo","url":"https://www.promptfoo.dev/blog/rlvr-explained/"},{"title":"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards","url":"https://arxiv.org/pdf/2604.07666"},{"title":"Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence","url":"https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"},{"title":"Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers","url":"https://arxiv.org/pdf/2510.00915"},{"title":"SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning","url":"https://arxiv.org/pdf/2512.03244"}]

Based on the search results, here's what I found about small verifier reward model accuracy thresholds in RLVR for 2025-2026:

## Key Findings on Verifier Accuracy Thresholds

Practitioners should prioritize moderate accuracy with high precision over perfect verification. This suggests that verifiers don't need to be perfectly accurate to be useful.

More specifically, a verifier catching 60% of errors creates a 40% gap, and models find and exploit these gaps. This highlights the practical minimum accuracy needed—verifiers need sufficient precision to avoid models learning to exploit undetected errors.

Fundamental questions remain about what accuracy RLVR actually requires of its verifier, and whether there is a point where the verifier is "good enough", indicating this is still an active research area as of 2025-2026.

## Important Caveats

The research reveals that verifiers have two types of failures: false positives (accepting incorrect solutions) and false negatives (rejecting correct ones). LLM judges can give 35%-66.8% false positive rates, while rule-based verifiers may reject valid solutions formatted differently or expressed in equivalent forms.

Interestingly, imperfect verification does not constitute a fundamental barrier to RLVR, though the specific accuracy threshold for "useful" training depends on the type of errors and verifier design.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f450e5b3-07c8-4568-98b4-f3d1963ec776",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "c7e1d56b-20ab-4020-b112-7db5e1abb0b3",
  "toolUseResult": {
    "query": "small verifier reward model accuracy threshold minimum useful reinforcement learning training 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NR79gWFnqVkqgYtAvomoNm",
        "content": [
          {
            "title": "RLVR: Verifiable Rewards for Reliable Enterprise LLMs | Appen",
            "url": "https://www.appen.com/blog/rlvr"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Implicitly ...",
            "url": "https://arxiv.org/pdf/2506.14245"
          },
          {
            "title": "GitHub - opendilab/awesome-RLVR: A curated list of reinforcement learning with verifiable rewards (continually updated) · GitHub",
            "url": "https://github.com/opendilab/awesome-RLVR"
          },
          {
            "title": "Reinforcement Learning with Verifiable Rewards Makes Models Faster, Not Smarter | Promptfoo",
            "url": "https://www.promptfoo.dev/blog/rlvr-explained/"
          },
          {
            "title": "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards",
            "url": "https://arxiv.org/pdf/2604.07666"
          },
          {
            "title": "Overcoming reward signal challenges: Verifiable rewards-based reinforcement learning with GRPO on SageMaker AI | Artificial Intelligence",
            "url": "https://aws.amazon.com/blogs/machine-learning/overcoming-reward-signal-challenges-verifiable-rewards-based-reinforcement-learning-with-grpo-on-sagemaker-ai/"
          },
          {
            "title": "Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers",
            "url": "https://arxiv.org/pdf/2510.00915"
          },
          {
            "title": "SPARK: Stepwise Process-Aware Rewards for Reference-Free Reinforcement Learning",
            "url": "https://arxiv.org/pdf/2512.03244"
          }
        ]
      },
      "Based on the search results, here's what I found about small verifier reward model accuracy thresholds in RLVR for 2025-2026:\n\n## Key Findings on Verifier Accuracy Thresholds\n\nPractitioners should prioritize moderate accuracy with high precision over perfect verification. This suggests that verifiers don't need to be perfectly accurate to be useful.\n\nMore specifically, a verifier catching 60% of errors creates a 40% gap, and models find and exploit these gaps. This highlights the practical minimum accuracy needed—verifiers need sufficient precision to avoid models learning to exploit undetected errors.\n\nFundamental questions remain about what accuracy RLVR actually requires of its verifier, and whether there is a point where the verifier is \"good enough\", indicating this is still an active research area as of 2025-2026.\n\n## Important Caveats\n\nThe research reveals that verifiers have two types of failures: false positives (accepting incorrect solutions) and false negatives (rejecting correct ones). LLM judges can give 35%-66.8% false positive rates, while rule-based verifiers may reject valid solutions formatted differently or expressed in equivalent forms.\n\nInterestingly, imperfect verification does not constitute a fundamental barrier to RLVR, though the specific accuracy threshold for \"useful\" training depends on the type of errors and verifier design."
    ],
    "durationSeconds": 8.576636465999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f450e5b3-07c8-4568-98b4-f3d1963ec776",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "c7e1d56b-20ab-4020-b112-7db5e1abb0b3",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Tool call

_source line 36 · 2026-05-27T23:19:05.960Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01AzzEFEauczqrGAMhV2wppV`</summary>

```json
{
  "url": "https://arxiv.org/abs/2604.07666",
  "prompt": "Extract: 1) What minimum verifier accuracy was found to be useful for RL training? 2) What specific noise levels were tested? 3) What was the finding about noise tolerance - at what point does noisy reward become harmful? 4) Any discussion of per-property accuracy thresholds for multi-component rewards?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e1d56b-20ab-4020-b112-7db5e1abb0b3",
  "isSidechain": false,
  "requestId": "req_011CbTvqYRDmpc1GveqVtv8U",
  "type": "assistant",
  "uuid": "25d7fe66-710f-48f6-bf25-5265d3b209cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VHNh1pcpCRhgYxnNHoQ9sm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 834,
      "cache_read_input_tokens": 35741,
      "output_tokens": 152,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 834,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 152,
          "cache_read_input_tokens": 35741,
          "cache_creation_input_tokens": 834,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 834
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

_source line 37 · 2026-05-27T23:19:10.549Z_

<details><summary>↩ Tool result · `toolu_01AzzEFEauczqrGAMhV2wppV`</summary>

```text
# Analysis of Paper Findings on Verifier Accuracy

Based on the arXiv abstract provided, here's what can be extracted:

**1) Minimum useful verifier accuracy:**
The paper states that "Noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline," suggesting systems remain effective with roughly 85% accuracy, though specific minimum thresholds aren't detailed in the abstract.

**2) Specific noise levels tested:**
The abstract confirms that "noise rates up to 15%" were evaluated, but doesn't enumerate intermediate testing points or provide granular noise level specifications.

**3) Noise tolerance findings:**
The research demonstrates that "imperfect verification does not constitute a fundamental barrier to RLVR," with the 15% noise threshold showing minimal performance degradation. However, the abstract doesn't specify where performance becomes substantially harmful.

**4) Per-property accuracy thresholds:**
No discussion of multi-component reward accuracy thresholds appears in the available abstract. The paper does recommend that "practitioners should prioritize moderate accuracy with high precision over perfect verification," but this discusses trade-offs rather than component-level specifications.

**Note:** The abstract alone provides limited technical details. The full paper would contain comprehensive methodology, detailed noise analyses, and specific threshold discussions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "25d7fe66-710f-48f6-bf25-5265d3b209cb",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "e842f55f-ffb4-4605-a1da-a394353f3512",
  "toolUseResult": {
    "bytes": 46251,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Paper Findings on Verifier Accuracy\n\nBased on the arXiv abstract provided, here's what can be extracted:\n\n**1) Minimum useful verifier accuracy:**\nThe paper states that \"Noise rates up to 15% yield peak validation accuracy within 2 percentage points of the clean baseline,\" suggesting systems remain effective with roughly 85% accuracy, though specific minimum thresholds aren't detailed in the abstract.\n\n**2) Specific noise levels tested:**\nThe abstract confirms that \"noise rates up to 15%\" were evaluated, but doesn't enumerate intermediate testing points or provide granular noise level specifications.\n\n**3) Noise tolerance findings:**\nThe research demonstrates that \"imperfect verification does not constitute a fundamental barrier to RLVR,\" with the 15% noise threshold showing minimal performance degradation. However, the abstract doesn't specify where performance becomes substantially harmful.\n\n**4) Per-property accuracy thresholds:**\nNo discussion of multi-component reward accuracy thresholds appears in the available abstract. The paper does recommend that \"practitioners should prioritize moderate accuracy with high precision over perfect verification,\" but this discusses trade-offs rather than component-level specifications.\n\n**Note:** The abstract alone provides limited technical details. The full paper would contain comprehensive methodology, detailed noise analyses, and specific threshold discussions.",
    "durationMs": 4584,
    "url": "https://arxiv.org/abs/2604.07666"
  },
  "sourceToolAssistantUUID": "25d7fe66-710f-48f6-bf25-5265d3b209cb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 38 · 2026-05-27T23:19:33.397Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to make the revisions. Let me synthesize what I've learned:

1. **Format Tax (arXiv:2604.03616)**: Shows 5.8-8.7pp degradation from structured output (XML, JSON, LaTeX, Markdown) in open-weight models. Tested Qwen3-32b, Qwen3-8b, OLMo3.1-32b, OLMo3-7b, SmolLM3-3b, Nemotron3-nano. Key finding: prompt-level instructions cause most of the cost (~3.9pp) before decoder constraints (~1.6pp additional). Closed-weight models show little/no format tax. 

2. **D-CoT (arXiv:2602.21786)**: Models trained with structured control tags internalize the structure, achieving highest MMLU-Pro accuracy (64.73%) without explicit tags during inference versus 62.92% with them. The approach shows substantial gains on GPQA-diamond and MMLU-Pro with just 5K training samples, using Qwen3-8B as the base model.

3. **CoRGI withdrawal**: Confirmed withdrawn on Oct 14, 2025, with reason "The paper is not yet mature and needs further improvement."

4. **Additive reward noise tolerance**: When combining signals additively with independent errors, the composite noise grows as √N rather than N, yielding an effective ~1/√N reduction per component.

5. **Verifier accuracy thresholds**: The "Imperfect Verifier" paper demonstrates that noise rates up to 15% maintain validation accuracy within 2 percentage points of the clean baseline, suggesting practitioners should focus on moderate accuracy paired with high precision.

Now I'm working through the revisions systematically. For the Format Tax issue, I need to acknowledge it as a potential risk in the landscape section, then address it in the approach by noting that prior Format Tax studies examined inference-time prompting rather than RL-trained formats, and cite D-CoT as evidence that trained tags get internalized and can be dropped at inference. I should also mention how CFRL's curriculum develops citation as a learned skill.

For the additive reward advantage, I'm adding an explicit argument for why additive combination outperforms multiplicative, grounding it in that √N noise reduction property and connecting it to the tolerance regime from the Imperfect Verifier work.

On the minor fixes, I need to note CoRGI's withdrawal from October 2025, set explicit minimum accuracy thresholds for grounding at ≥80% and completeness at ≥70%, and acknowledge that currently only binding has a 75% threshold.

For the 4B verifier precedent gap, I'm being more explicit about it and citing MJ1 as the closest precedent with 3B active parameters at evaluation time, then specifying per-property thresholds.

Generating the revised JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e842f55f-ffb4-4605-a1da-a394353f3512",
  "isSidechain": false,
  "requestId": "req_011CbTvrCXuzqbwnRzks9fyH",
  "type": "assistant",
  "uuid": "b34ad307-2192-465c-9055-08149d4bece6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgXirWs3mF8p7QgXXmYHk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 36575,
      "output_tokens": 5592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5592,
          "cache_read_input_tokens": 36575,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 39 · 2026-05-27T23:19:38.193Z_

Now I have all the information needed. Let me synthesize the findings and produce the complete revised proposal.

Key research findings:
- **Format Tax**: 5.8-8.7pp degradation on open-weight models (Qwen3-32b/8b, OLMo, SmolLM3, Nemotron) from structured output formats (XML, JSON, LaTeX, Markdown). Prompt-level format instructions cause ~3.9pp loss before decoder constraints add ~1.6pp more. Closed-weight models show little/no tax. Study is purely inference-time prompted, not RL-trained.
- **D-CoT**: Trained tags internalize — highest MMLU-Pro accuracy (64.73%) occurred *without* tags at inference vs 62.92% with tags. +9.9% GPQA-diamond with only 5K training samples on Qwen3-8B.
- **CoRGI**: Confirmed withdrawn Oct 14, 2025 ("not yet mature and needs further improvement").
- **Imperfect Verifier**: Noise rates up to 15% yield validation accuracy within 2pp of clean baseline.

All reviewer issues are LOW/LOW-MEDIUM and the reviewer explicitly says "three focused changes would likely reach the threshold" — this calls for targeted minor revisions, not a pivot.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b34ad307-2192-465c-9055-08149d4bece6",
  "isSidechain": false,
  "requestId": "req_011CbTvrCXuzqbwnRzks9fyH",
  "type": "assistant",
  "uuid": "183560f4-958a-435f-86b8-7630dc89cf00",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgXirWs3mF8p7QgXXmYHk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 36575,
      "output_tokens": 5592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5592,
          "cache_read_input_tokens": 36575,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 40 · 2026-05-27T23:21:28.641Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01LyWrqwQde8Ztgd46zj5Rqp`</summary>

```json
{
  "description": "Produce revised research JSON",
  "model": "opus",
  "prompt": "You are helping revise a research proposal based on reviewer feedback (round 5). The reviewer says the proposal is \"approaching pass quality\" and needs three focused changes. I've done all the research and now need you to produce the complete revised JSON.\n\n## Research findings for the revision:\n\n### 1. Format Tax (arXiv:2604.03616, Apr 2026)\n- By Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick\n- Tests 6 open-weight models (Qwen3-32b, Qwen3-8b, OLMo3.1-32b, OLMo3-7b, SmolLM3-3b, Nemotron3-nano) + 4 API models\n- 4 formats: JSON, XML, LaTeX, Markdown\n- Open-weight models: avg -5.8pp to -8.7pp on GPQA, MATH-500, ZebraLogic\n- Prompt-level format instructions cause ~3.9pp loss; decoder constraints add ~1.6pp more\n- Closed-weight models show little/no format tax\n- Proposed solution: decouple reasoning from formatting (2-pass or extended thinking)\n- DOES NOT study RL training or fine-tuning — purely inference-time prompting study\n\n### 2. D-CoT (arXiv:2602.21786, Feb 2026)\n- \"Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models\"\n- Uses control tags (&lt;TEMP_LOW>, &lt;TEMP_MID>, &lt;TEMP_HIGH>) as scaffolding during training\n- Key result: model internalizes structured tags — maintains/improves performance even WITHOUT tags at inference\n- Highest MMLU-Pro accuracy (64.73%) occurred WITHOUT tags vs 62.92% WITH tags\n- +9.9% GPQA-diamond, +9.1% MMLU-Pro with only 5,079 training samples on Qwen3-8B\n- Evidence of internalization: implicit fact organization, directed self-checking, suppressed unnecessary arithmetic\n\n### 3. CoRGI withdrawal\n- arXiv:2508.00378, withdrawn Oct 14, 2025\n- Reason: \"The paper is not yet mature and needs further improvement\"\n\n### 4. Imperfect Verifier (arXiv:2604.07666)\n- Noise rates up to 15% yield peak validation accuracy within 2pp of clean baseline\n- \"Imperfect verification does not constitute a fundamental barrier to RLVR\"\n- Recommendation: prioritize moderate accuracy with high precision\n\n## What needs to change (reviewer issues):\n\n### Issue 1 (LOW-MEDIUM): Cite Format Tax + D-CoT\nAdd to landscape and approach:\n- Acknowledge Format Tax documents 5.8-8.7pp degradation from structured XML/JSON in prompted open-weight models\n- Distinguish from CFRL: (a) D-CoT shows trained tags get internalized, performance maintained/improved when tags dropped, (b) CFRL trains citation via RL, not zero-shot prompting, (c) MuRGAt parallel — same zero-shot vs trained distinction\n- Add both to key_references\n\n### Issue 2 (LOW-MEDIUM): Explicitly argue additive reward advantage\nAdd 1-2 sentences in the approach explaining:\n- Additive reward (weighted sum) chosen specifically to avoid multiplicative error compounding\n- With N independent signals each having ~15% error, additive combination gives composite noise ~σ/√N (errors partially cancel) vs multiplicative where errors compound\n- This keeps training within the Imperfect Verifier tolerance regime\n\n### Issue 3 (LOW): Fix minor reference issues\n- Note CoRGI's withdrawal status in landscape\n- Specify minimum accuracy thresholds for grounding (≥80%) and completeness (≥70%), matching the existing 75% binding threshold\n- Add rationale for these thresholds\n\n### Issue 4 (LOW): Acknowledge 4B verifier precedent gap\n- More explicitly acknowledge no precedent for ≤4B multi-property semantic verification as training-time reward\n- MJ1 (3B active) is closest but evaluation-time with ~6144 output tokens\n- Specify what minimum per-property accuracy makes Tier 1 useful\n\n## INSTRUCTIONS:\n\nProduce a COMPLETE JSON object with ALL fields from the original, incorporating the changes above. The JSON should be valid and complete.\n\nHere is the original JSON to revise (I'll describe where each change goes):\n\n**In `opportunity`**: Add Format Tax + D-CoT discussion in the evidence-loss/diagnostic section. Note that Format Tax applies to inference-time prompting, not RL training, and D-CoT provides direct counter-evidence.\n\n**In `landscape`**: \n- Add a new paragraph/subsection about \"Format Tax and structured output overhead\" that covers both Format Tax and D-CoT\n- Update CoRGI reference to note withdrawal\n- Keep everything else the same\n\n**In `approach`**:\n- Add a paragraph about Format Tax mitigation after the MuRGAt paragraph (since it's a related concern about structured format degradation)\n- Add explicit additive reward advantage argument near the training/reward composition section\n- In the verifier validation protocol, add per-property accuracy thresholds for grounding (≥80%) and completeness (≥70%)\n- Acknowledge 4B verifier precedent gap more explicitly in the verifier architecture section\n\n**In `key_references`**: Add \"The Format Tax\" and \"D-CoT\" papers\n\n**In `changes_from_previous_revision`**: Document ALL changes made in this round\n\n**Set `change_type`**: \"minor\"\n\nNow here is the COMPLETE original JSON. Please produce the revised version with all changes integrated:\n\n{\n  \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier\",\n  \"core_problem\": \"How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?\",\n  \"opportunity\": \"Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.\",\n\nReplace the opportunity with one that ALSO adds: (7) Structured output formats themselves impose a 'Format Tax' — 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents 5.8–8.7pp reasoning degradation from XML/JSON requirements in prompted open-weight models — though this applies to inference-time prompting rather than RL-trained formats, and D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline and maintain or improve performance when tags are removed at inference time.\n\nFor the landscape, add this new subsection before \"The gap\":\n\n**Structured output overhead:** 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents that structured output requirements (JSON, XML, LaTeX, Markdown) degrade reasoning accuracy by 5.8–8.7pp across six open-weight models (Qwen3-32b/8b, OLMo3.1-32b/7b, SmolLM3-3b, Nemotron3-nano) on GPQA, MATH-500, and ZebraLogic, with most degradation arising from format-requesting prompt instructions (~3.9pp) rather than decoder constraints (~1.6pp). Critically, closed-weight models show little to no format tax, suggesting the problem is solvable through training rather than inherent to structured generation. D-CoT (arXiv:2602.21786, Feb 2026) provides direct counter-evidence for *trained* structured formats: models trained with control tags (&lt;TEMP_LOW>/&lt;TEMP_MID>/&lt;TEMP_HIGH>) internalize the discipline, achieving +9.9% GPQA-diamond and highest MMLU-Pro accuracy (64.73%) *without* tags at inference — exceeding tagged performance (62.92%) — with only 5K training samples on Qwen3-8B. This distinction between prompted format imposition (where the tax applies) and trained format internalization (where it does not) is directly relevant to CFRL's design.\n\nFor CoRGI in the landscape, update: \"CoRGI (arXiv:2508.00378, withdrawn Oct 2025) performed post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal. [Note: this paper was withdrawn by its authors as 'not yet mature'; we cite it for conceptual context only.]\"\n\nFor the approach, add after the MuRGAt paragraph and before the CFV section:\n\n**Addressing the Format Tax:** 'The Format Tax' (arXiv:2604.03616) documents 5.8–8.7pp reasoning degradation when open-weight models are *prompted* to produce structured XML/JSON output. While CFRL requires structured &lt;observe>/&lt;reason> tags, three factors distinguish our setting from the Format Tax regime: (1) *Trained vs. prompted format*: D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline — achieving highest accuracy *without* tags at inference (+9.9% GPQA-diamond, 64.73% vs. 62.92% MMLU-Pro on Qwen3-8B with 5K samples) — indicating that RL-trained format requirements do not incur the same tax as inference-time prompting. (2) *Curriculum-developed skill*: Like the MuRGAt distinction, CFRL develops citation as a learned skill via reward optimization across curriculum phases, not a zero-shot constraint. (3) *Counterfactual monitoring*: Safeguard #5 directly measures any format-induced degradation by comparing tagged vs. untagged accuracy every 500 steps, providing an empirical check against format tax emergence during training. If format-related degradation is detected (tagged accuracy < untagged − 2pp), we activate a mitigation protocol: reducing format reward weight and increasing the proportion of untagged rollouts to prevent the model from over-investing in format compliance at the expense of reasoning quality.\n\nFor the additive reward argument, add near the training section (after the composite reward equation):\n\n**Additive reward structure for noise tolerance:** The weighted-sum reward combination R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness + ε·R_format − P_leak is specifically chosen over multiplicative or conjunctive alternatives to prevent error compounding. With independent per-property verification errors of ~15% (within the 'Imperfect Verifier' tolerance regime), additive combination yields composite noise that partially cancels across components (~σ/√N reduction for N independent signals), keeping the effective noise well within the ≤15% threshold where RL training degrades by ≤2pp. A multiplicative combination (e.g., R = R_accuracy × R_grounding × R_binding) would compound errors: three signals each with 85% accuracy yield ~61% joint accuracy, pushing noise far beyond the tolerance boundary. The additive structure also provides graceful degradation — if one property's verifier underperforms, the remaining signals still provide useful gradient, whereas multiplicative combination would zero out the reward whenever any single property check fails.\n\nFor verifier validation, update to add per-property thresholds:\n\n**Verifier validation protocol**: Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with minimum deployment thresholds of ≥80% balanced accuracy for grounding (motivated by PEARL's perception checklist achieving ~85% agreement with human judgments), ≥75% for binding validity (where symbolic/arithmetic checks provide exact verification for Tier 1, with the threshold applying to the verifier's assessment of qualitative bindings), and ≥70% for completeness (set lower to reflect the inherent noisiness of relevance filtering, where human inter-annotator agreement is only 74.6% per arXiv:2410.15531). Tier 1 binding is validated separately for arithmetic (expected ~95%+ via symbolic execution) and geometry-symbolic components (expected ~85%+ via theorem library matching). (b) ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on any property falls below its deployment threshold, we activate property-specific fallbacks: for grounding, soften to probabilistic confidence scores; for binding, restrict to Tier 1 symbolic-only verification (which has near-perfect accuracy); for completeness, set δ=0 and report Tier 1 results as the core finding.\n\nFor the verifier architecture section, add acknowledgment of the precedent gap:\n\n**Verifier architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass. We acknowledge that no existing ≤4B model has been validated for multi-property semantic verification (grounding + binding + completeness) as a training-time reward signal — MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens and no throughput constraints. Our design bets on two factors that make this feasible: (1) the CFV output is shorter (~500-1500 tokens vs. MJ1's ~6144) because inline verification verdicts are more compact than MJ1's full grounded verification chain with pairwise comparison, and (2) Tier 1 binding validity relies on symbolic/arithmetic checking rather than learned semantic judgment, offloading the hardest verification subtask from the neural model. If the 4B model proves insufficient for multi-property verification in a single pass, our fallback is a two-pass architecture: a first pass for grounding verification and a second for binding/completeness, each with shorter output and more focused instruction — still yielding ≤2 calls per rollout vs. FGRPO's S ≈ 5-8.\n\nThen produce the COMPLETE JSON with ALL of these changes integrated, plus:\n- Updated key_references adding the two new papers\n- Updated changes_from_previous_revision documenting round 6 changes\n- change_type: \"minor\"\n\nMake sure the JSON is valid. Output ONLY the JSON, no other text.\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "183560f4-958a-435f-86b8-7630dc89cf00",
  "isSidechain": false,
  "requestId": "req_011CbTvrCXuzqbwnRzks9fyH",
  "type": "assistant",
  "uuid": "4e254796-96ef-4a1f-8633-483298f9a590",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01LgXirWs3mF8p7QgXXmYHk9",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 445,
      "cache_read_input_tokens": 36575,
      "output_tokens": 5592,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 445,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5592,
          "cache_read_input_tokens": 36575,
          "cache_creation_input_tokens": 445,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 445
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

_source line 41_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "4e254796-96ef-4a1f-8633-483298f9a590",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 42_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Tool result

_source line 43 · 2026-05-27T23:30:05.786Z_

<details><summary>↩ Tool result · `toolu_01LyWrqwQde8Ztgd46zj5Rqp`</summary>

````text
Since I can't write files or run python, I'll produce the complete JSON directly in my response. Let me make sure it's comprehensive and valid.

Here is the complete revised JSON:

```json
{
  "title": "Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier",
  "change_type": "minor",
  "core_problem": "How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?",
  "opportunity": "Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. (7) Structured output formats themselves impose a 'Format Tax' — 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents 5.8–8.7pp reasoning degradation from XML/JSON requirements in prompted open-weight models — though this applies to inference-time prompting rather than RL-trained formats, and D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline and maintain or improve performance when tags are removed at inference time. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.",
  "landscape": "**Evidence grounding and binding verification:** PEARL (CVPR 2026) introduces a perception checklist that gates reasoning on perception accuracy, achieving ~85% agreement with human judgments on visual fact verification. FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, but at multiplicative cost (~6-8 judge calls per sentence \u00d7 multiple sentences \u00d7 rollouts). MJ1 (Mar 2026) trains a 3B-active-parameter judge with a 5-stage grounded verification chain producing ~6144 output tokens, demonstrating that structured multi-property verification is feasible at small scale — but operates at evaluation time with no throughput constraints, not as a training-time reward signal. PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating. Vision-SR1 decomposes reasoning into perception and reasoning stages with structured tags, using self-reward. TreeVGR (ICLR 2026) and ViGoRL train models to generate spatial evidence via RL, but verify localization (bounding-box IoU) rather than reasoning validity.\n\n**Token-level credit and attention methods:** PGPO, SAYO, AT-RL, VICRA, and KAWHI reweight optimization toward visually-dependent tokens using attention-based or gradient-based proxies. Faithful-MR1 (May 2026) anchors attention to causal image regions. These methods use statistical proxies for visual dependency rather than verifying semantic correctness of how evidence is used in reasoning. v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access. SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL.\n\n**Completeness gap:** No existing method verifies integration completeness — whether all task-relevant visual facts are bound to reasoning steps. MathLens (Feb 2026) identifies completeness failures as the growing error fraction in multimodal reasoning. 'Don't Blink' (Apr 2026) shows this worsens as reasoning unfolds, with attention to evidence regions dropping >50% over the course of a reasoning chain.\n\n**Diagnostic frameworks:** The PAR framework (Mar 2026) diagnoses that 'alignment' — mapping perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone, motivating a dedicated binding validity check. MuRGAt (Feb 2026) documents that enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution — a critical cautionary finding that motivates developing citation as a trained skill via RL rather than imposing it as a zero-shot constraint.\n\n**Post-hoc verification:** CoRGI (arXiv:2508.00378, withdrawn Oct 2025) performed post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal. [Note: this paper was withdrawn by its authors as 'not yet mature'; we cite it for conceptual context only.]\n\n**Structured output overhead:** 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents that structured output requirements (JSON, XML, LaTeX, Markdown) degrade reasoning accuracy by 5.8\u20138.7pp across six open-weight models (Qwen3-32b/8b, OLMo3.1-32b/7b, SmolLM3-3b, Nemotron3-nano) on GPQA, MATH-500, and ZebraLogic, with most degradation arising from format-requesting prompt instructions (~3.9pp) rather than decoder constraints (~1.6pp). Critically, closed-weight models show little to no format tax, suggesting the problem is solvable through training rather than inherent to structured generation. D-CoT (arXiv:2602.21786, Feb 2026) provides direct counter-evidence for *trained* structured formats: models trained with control tags (&lt;TEMP_LOW>/&lt;TEMP_MID>/&lt;TEMP_HIGH>) internalize the discipline, achieving +9.9% GPQA-diamond and highest MMLU-Pro accuracy (64.73%) *without* tags at inference — exceeding tagged performance (62.92%) — with only 5K training samples on Qwen3-8B. This distinction between prompted format imposition (where the tax applies) and trained format internalization (where it does not) is directly relevant to CFRL's design.\n\n**Imperfect verification:** 'An Imperfect Verifier is Good Enough' (arXiv:2604.07666, 2026) demonstrates that noise rates up to 15% in reward signals yield peak validation accuracy within 2pp of clean baseline, establishing that imperfect verification does not constitute a fundamental barrier to RLVR. This directly motivates our verifier design: prioritize moderate accuracy with high precision rather than requiring perfect verification.\n\n**The gap:** No method unifies grounding verification, binding validity, and completeness checking in a single lightweight verifier that serves as a training-time reward signal. FGRPO checks grounding but not completeness, and at multiplicative cost. MJ1 demonstrates multi-property verification but at evaluation time only, with no throughput constraints. Attention-based methods use proxies rather than semantic verification. The opportunity is a distilled composition verifier (CFV) that performs all three checks in a single forward pass, enabling composition-faithful RL training at tractable cost.",
  "approach": "We propose Composition Fidelity RL (CFRL), a training framework that uses a single distilled Composition Fidelity Verifier (CFV) to provide a multi-property reward signal for RL training, unifying evidence grounding, binding validity, and integration completeness verification.\n\n**Structured citation format:** CFRL trains models to produce reasoning traces with explicit &lt;observe>...&lt;/observe> and &lt;reason>...&lt;/reason> tags, where each &lt;reason> block cites specific &lt;observe> blocks. This structured format enables automated verification of all three composition properties. Unlike zero-shot prompting approaches where MuRGAt (Feb 2026) documents accuracy degradation from enforced structured grounding, CFRL develops citation as a learned skill via RL reward optimization — the model learns to cite because citing improves reward, not because it is constrained to cite at inference time.\n\n**Addressing the Format Tax:** 'The Format Tax' (arXiv:2604.03616) documents 5.8\u20138.7pp reasoning degradation when open-weight models are *prompted* to produce structured XML/JSON output. While CFRL requires structured &lt;observe>/&lt;reason> tags, three factors distinguish our setting from the Format Tax regime: (1) *Trained vs. prompted format*: D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline — achieving highest accuracy *without* tags at inference (+9.9% GPQA-diamond, 64.73% vs. 62.92% MMLU-Pro on Qwen3-8B with 5K samples) — indicating that RL-trained format requirements do not incur the same tax as inference-time prompting. (2) *Curriculum-developed skill*: Like the MuRGAt distinction, CFRL develops citation as a learned skill via reward optimization across curriculum phases, not a zero-shot constraint. (3) *Counterfactual monitoring*: Safeguard #5 directly measures any format-induced degradation by comparing tagged vs. untagged accuracy every 500 steps, providing an empirical check against format tax emergence during training. If format-related degradation is detected (tagged accuracy < untagged \u2212 2pp), we activate a mitigation protocol: reducing format reward weight and increasing the proportion of untagged rollouts to prevent the model from over-investing in format compliance at the expense of reasoning quality.\n\n**Composition Fidelity Verifier (CFV) — architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass, producing inline verdicts for each &lt;observe>/&lt;reason> pair: (a) *Grounding*: Is the cited visual evidence factually present in the image? (b) *Binding validity*: Does the inference logically follow from the cited evidence? (c) *Completeness*: Are all task-relevant visual facts cited by at least one reasoning step? We acknowledge that no existing \u22644B model has been validated for multi-property semantic verification (grounding + binding + completeness) as a training-time reward signal — MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens and no throughput constraints. Our design bets on two factors that make this feasible: (1) the CFV output is shorter (~500-1500 tokens vs. MJ1's ~6144) because inline verification verdicts are more compact than MJ1's full grounded verification chain with pairwise comparison, and (2) Tier 1 binding validity relies on symbolic/arithmetic checking rather than learned semantic judgment, offloading the hardest verification subtask from the neural model. If the 4B model proves insufficient for multi-property verification in a single pass, our fallback is a two-pass architecture: a first pass for grounding verification and a second for binding/completeness, each with shorter output and more focused instruction — still yielding \u22642 calls per rollout vs. FGRPO's S \u2248 5-8. The CFV is distilled from a larger teacher verifier (Qwen3-VL-30B-A3B) using a curated verification dataset, with progressive distillation to maintain accuracy on each sub-task.\n\n**Tiered binding validity:** Binding validity verification is decomposed into two tiers: *Tier 1 (symbolic/arithmetic)*: For reasoning steps involving arithmetic, geometric, or logical operations, binding validity is checked via symbolic execution — parsing the cited evidence and the inference into formal representations and verifying logical entailment. Expected accuracy: ~95%+ for arithmetic (symbolic execution), ~85%+ for geometry-symbolic (theorem library matching). *Tier 2 (semantic/qualitative)*: For reasoning steps involving qualitative judgments (e.g., 'the object appears damaged'), binding validity requires the CFV's learned semantic judgment. This is the harder sub-task, where the 4B model's limitations are most likely to manifest. The tiered structure ensures that even if Tier 2 accuracy is modest, the overall binding signal remains useful because Tier 1 provides a reliable foundation. We specify a minimum per-property accuracy that makes Tier 1 useful as a standalone signal: if only Tier 1 binding is validated (symbolic/arithmetic), we require \u226590% balanced accuracy on Tier 1 items, which provides a meaningful training signal for the substantial fraction of mathematical/logical reasoning steps in our target benchmarks (MathVista, MMMU-Science).\n\n**Composite reward and training:** The RL training uses GRPO with a composite reward signal: R = \u03b1\u00b7R_accuracy + \u03b2\u00b7R_grounding + \u03b3\u00b7R_binding + \u03b4\u00b7R_completeness + \u03b5\u00b7R_format \u2212 P_leak, where R_accuracy is task correctness, R_grounding/R_binding/R_completeness are CFV-derived property scores, R_format rewards well-formed citation structure, and P_leak penalizes reasoning traces that 'leak' answers without citing evidence. Weights are set via curriculum: Phase 1 (accuracy + format only, \u03b1=1.0, \u03b5=0.3), Phase 2 (add grounding, \u03b2=0.3), Phase 3 (add binding + completeness, \u03b3=0.2, \u03b4=0.15). The binding threshold for crediting a reasoning step is set at 75%.\n\n**Additive reward structure for noise tolerance:** The weighted-sum reward combination R = \u03b1\u00b7R_accuracy + \u03b2\u00b7R_grounding + \u03b3\u00b7R_binding + \u03b4\u00b7R_completeness + \u03b5\u00b7R_format \u2212 P_leak is specifically chosen over multiplicative or conjunctive alternatives to prevent error compounding. With independent per-property verification errors of ~15% (within the 'Imperfect Verifier' tolerance regime), additive combination yields composite noise that partially cancels across components (~\u03c3/\u221aN reduction for N independent signals), keeping the effective noise well within the \u226415% threshold where RL training degrades by \u22642pp. A multiplicative combination (e.g., R = R_accuracy \u00d7 R_grounding \u00d7 R_binding) would compound errors: three signals each with 85% accuracy yield ~61% joint accuracy, pushing noise far beyond the tolerance boundary. The additive structure also provides graceful degradation — if one property's verifier underperforms, the remaining signals still provide useful gradient, whereas multiplicative combination would zero out the reward whenever any single property check fails.\n\n**Verifier validation protocol:** Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with minimum deployment thresholds of \u226580% balanced accuracy for grounding (motivated by PEARL's perception checklist achieving ~85% agreement with human judgments), \u226575% for binding validity (where symbolic/arithmetic checks provide exact verification for Tier 1, with the threshold applying to the verifier's assessment of qualitative bindings), and \u226570% for completeness (set lower to reflect the inherent noisiness of relevance filtering, where human inter-annotator agreement is only 74.6% per arXiv:2410.15531). Tier 1 binding is validated separately for arithmetic (expected ~95%+ via symbolic execution) and geometry-symbolic components (expected ~85%+ via theorem library matching). (b) Ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on any property falls below its deployment threshold, we activate property-specific fallbacks: for grounding, soften to probabilistic confidence scores; for binding, restrict to Tier 1 symbolic-only verification (which has near-perfect accuracy); for completeness, set \u03b4=0 and report Tier 1 results as the core finding.\n\n**Training safeguards:** (1) Reward hacking detection: monitor for traces that game citation format without meaningful content. (2) Curriculum gating: each phase requires validation accuracy above threshold before proceeding. (3) KL penalty against base model to prevent reward over-optimization. (4) Leak penalty P_leak to prevent answer-first-cite-later patterns. (5) Format tax monitoring: compare tagged vs. untagged accuracy every 500 steps; if tagged accuracy drops below untagged \u2212 2pp, reduce format reward weight and increase untagged rollout proportion.\n\n**Evaluation:** Primary benchmarks: MathVista (mathematical visual reasoning), MMMU (multi-discipline multimodal understanding), ScienceQA (science reasoning). Composition fidelity metrics: grounding precision/recall, binding accuracy, completeness coverage. Baselines: (1) Standard GRPO without composition reward, (2) FGRPO-style per-sentence VLM judge (cost comparison), (3) Ablations removing each reward component individually. Key ablations: (a) Full CFRL vs. accuracy-only RL vs. each property reward in isolation; (b) CFV at 4B vs. teacher verifier at 30B (quality-cost tradeoff); (c) Curriculum vs. simultaneous reward introduction; (d) Noise injection ablation following Imperfect Verifier methodology.",
  "key_references": [
    "PEARL: Perception-Gated Reasoning for Multimodal Large Language Models (CVPR 2026) — perception checklist gates reasoning; ~85% human agreement; motivates grounding threshold",
    "FGRPO: Fine-Grained Reinforcement from Perception Optimization (Apr 2026) — per-sentence VLM judge for grounding/consistency; primary cost comparison target",
    "Faithful-MR1: Faithful Multimodal Reasoning via Attention Anchoring (May 2026) — attention-based causal region grounding",
    "PaLMR: Process-Level Visual Fidelity via V-GRPO (CVPR 2026) — binary perception gating for process reward",
    "MJ1: Training a 3B Multi-Judge for Grounded Verification Chains (Mar 2026) — 5-stage verification at 3B active params, evaluation-time with ~6144 output tokens; closest precedent for multi-property verification at small scale",
    "MathLens: Diagnosing Completeness Failures in Multimodal Reasoning (Feb 2026) — identifies completeness as growing error fraction",
    "Don't Blink: Attention Decay in Long Multimodal Reasoning (Apr 2026) — evidence attention drops >50% over reasoning chains",
    "PAR Framework: Diagnosing Alignment as Distinct Failure Mode (Mar 2026) — motivates dedicated binding validity check",
    "MuRGAt: Structured Grounding Degrades Accuracy in Zero-Shot Settings (Feb 2026) — cautionary finding motivating trained vs. prompted distinction",
    "CoRGI: Post-Hoc Step-Wise CoT Verification via Visual Grounding (arXiv:2508.00378, withdrawn Oct 2025) — conceptually related verification chain; inference-time only; withdrawn as 'not yet mature'",
    "An Imperfect Verifier is Good Enough (arXiv:2604.07666, 2026) — noise up to 15% yields \u22642pp degradation; motivates additive reward structure and verifier tolerance thresholds",
    "The Format Tax: Structured Output Degrades Reasoning in Open-Weight Models (arXiv:2604.03616, Apr 2026) — documents 5.8\u20138.7pp degradation from XML/JSON in prompted open-weight models across GPQA, MATH-500, ZebraLogic; applies to inference-time prompting, not RL-trained formats",
    "D-CoT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models (arXiv:2602.21786, Feb 2026) — trained structured tags internalized; +9.9% GPQA-diamond, 64.73% MMLU-Pro without tags > 62.92% with tags; direct counter-evidence to format tax for trained formats",
    "TreeVGR: Training Models to Generate Bounding-Box Evidence via RL (ICLR 2026) — spatial grounding via dual IoU reward; verifies localization not reasoning validity",
    "Vision-SR1: Self-Reward via Perception-Reasoning Decomposition (2026) — structured tags with self-reward; checks self-containment not factual correctness",
    "PGPO / SAYO / AT-RL / VICRA / KAWHI — token-level credit methods reweighting toward visually-dependent tokens",
    "v1: Interleaved Visual Grounding via Point-and-Copy (May 2026) — 300K traces with embedding re-access",
    "SIEVE: Iterative Re-Access of Cached Visual Evidence During RL (Mar 2026) — embedding-level visual grounding",
    "VTPerception-R1: Perception-Aware RL with Visual/Textual/Consistency Rewards (2026)"
  ],
  "changes_from_previous_revision": [
    "Round 6 (minor revision): (1) Added 'The Format Tax' (arXiv:2604.03616) and D-CoT (arXiv:2602.21786) citations and discussion. In opportunity: added point (7) acknowledging the Format Tax documents 5.8\u20138.7pp degradation from structured XML/JSON in prompted open-weight models, while distinguishing that this applies to inference-time prompting and D-CoT provides counter-evidence for trained structured formats. In landscape: added new 'Structured output overhead' subsection covering Format Tax findings (3.9pp from prompt instructions, 1.6pp from decoder constraints, closed-weight models unaffected) and D-CoT counter-evidence (trained tags internalized, +9.9% GPQA-diamond, 64.73% MMLU-Pro without tags > 62.92% with tags on Qwen3-8B with 5K samples). In approach: added 'Addressing the Format Tax' paragraph distinguishing CFRL from the Format Tax regime via three factors (trained vs. prompted format with D-CoT evidence, curriculum-developed skill per MuRGAt distinction, counterfactual monitoring via Safeguard #5 with mitigation protocol). Added both papers to key_references.",
    "Round 6 (minor revision): (2) Added explicit additive reward advantage argument. New paragraph 'Additive reward structure for noise tolerance' explains that weighted-sum combination is specifically chosen to prevent error compounding \u2014 with ~15% independent per-property errors, additive combination yields ~\u03c3/\u221aN composite noise (errors partially cancel), keeping training within the Imperfect Verifier \u226415% tolerance regime where degradation is \u22642pp. Contrasts with multiplicative combination where three 85%-accurate signals yield only ~61% joint accuracy, exceeding tolerance. Notes graceful degradation: underperforming single-property verifier does not zero out reward.",
    "Round 6 (minor revision): (3) Fixed reference issues. Updated CoRGI entry in landscape to note withdrawal status (arXiv:2508.00378, withdrawn Oct 2025, 'not yet mature') and clarify it is cited for conceptual context only. Updated key_references entry for CoRGI similarly. Added per-property minimum accuracy thresholds to verifier validation protocol: \u226580% balanced accuracy for grounding (motivated by PEARL's ~85% human agreement), \u226575% for binding validity (threshold applies to qualitative bindings; Tier 1 symbolic has near-perfect accuracy), \u226570% for completeness (reflects inherent noisiness of relevance filtering, human inter-annotator agreement 74.6%). Added rationale for each threshold. Added separate Tier 1 validation for arithmetic (~95%+ via symbolic execution) and geometry-symbolic (~85%+ via theorem library matching). Added property-specific fallback protocols.",
    "Round 6 (minor revision): (4) Acknowledged 4B verifier precedent gap more explicitly. Added paragraph in CFV architecture section stating no existing \u22644B model has been validated for multi-property semantic verification as training-time reward signal. Cited MJ1 (3B active) as closest precedent but for evaluation-time judging with ~6144 output tokens and no throughput constraints. Identified two factors making 4B feasible: shorter CFV output (~500-1500 tokens vs. ~6144) and Tier 1 symbolic offloading. Specified two-pass fallback architecture if single-pass proves insufficient. Added minimum per-property accuracy specification for Tier 1 standalone utility (\u226590% balanced accuracy on Tier 1 items)."
  ]
}
```

Here is a summary of all changes integrated into the revised JSON:

**Issue 1 -- Format Tax + D-CoT citations (LOW-MEDIUM):**
- **Opportunity**: Added point (7) documenting 5.8-8.7pp Format Tax degradation from structured XML/JSON in prompted open-weight models, with the key distinction that this applies to inference-time prompting and D-CoT provides counter-evidence for trained formats.
- **Landscape**: Added new "Structured output overhead" subsection covering Format Tax findings (6 models, 3.9pp from prompt instructions, 1.6pp from decoder constraints, closed-weight unaffected) and D-CoT counter-evidence (tags internalized, +9.9% GPQA-diamond, 64.73% > 62.92% MMLU-Pro without tags on Qwen3-8B with 5K samples).
- **Approach**: Added "Addressing the Format Tax" paragraph with three distinguishing factors (trained vs. prompted per D-CoT, curriculum-developed skill per MuRGAt, counterfactual monitoring via Safeguard #5 with mitigation protocol).
- **Key references**: Added both "The Format Tax" (arXiv:2604.03616) and "D-CoT" (arXiv:2602.21786).

**Issue 2 -- Additive reward advantage (LOW-MEDIUM):**
- **Approach**: Added "Additive reward structure for noise tolerance" paragraph explaining weighted-sum chosen to prevent error compounding. With ~15% independent per-property errors, additive yields ~sigma/sqrt(N) composite noise vs. multiplicative yielding ~61% joint accuracy (three 85%-accurate signals). Notes graceful degradation property.

**Issue 3 -- Reference fixes (LOW):**
- **Landscape**: Updated CoRGI to note withdrawal status (arXiv:2508.00378, withdrawn Oct 2025, "not yet mature"), cited for conceptual context only.
- **Approach/Verifier validation**: Added per-property minimum accuracy thresholds: >=80% grounding (PEARL's ~85% agreement), >=75% binding (Tier 1 symbolic near-perfect), >=70% completeness (human IAA 74.6%). Added rationale for each. Added Tier 1 separate validation (arithmetic ~95%+, geometry-symbolic ~85%+). Added property-specific fallback protocols.

**Issue 4 -- 4B verifier precedent gap (LOW):**
- **Approach/CFV architecture**: Explicit acknowledgment that no existing <=4B model validated for multi-property semantic verification as training-time reward. MJ1 (3B active) closest but evaluation-time with ~6144 tokens. Two feasibility factors: shorter output (~500-1500 tokens) and Tier 1 symbolic offloading. Two-pass fallback architecture specified. Minimum Tier 1 standalone accuracy: >=90% balanced accuracy on Tier 1 items.

agentId: a755fbd23f7e43021 (use SendMessage with to: 'a755fbd23f7e43021' to continue this agent)
&lt;usage>total_tokens: 66710
tool_uses: 16
duration_ms: 517134&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "4e254796-96ef-4a1f-8633-483298f9a590",
  "isSidechain": false,
  "promptId": "1efcaffe-583d-43b5-bf3e-76ba4dc2f9a0",
  "type": "user",
  "uuid": "16e7e643-fa7f-4488-9ab8-8be77bd8be08",
  "toolUseResult": {
    "status": "completed",
    "prompt": "You are helping revise a research proposal based on reviewer feedback (round 5). The reviewer says the proposal is \"approaching pass quality\" and needs three focused changes. I've done all the research and now need you to produce the complete revised JSON.\n\n## Research findings for the revision:\n\n### 1. Format Tax (arXiv:2604.03616, Apr 2026)\n- By Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick\n- Tests 6 open-weight models (Qwen3-32b, Qwen3-8b, OLMo3.1-32b, OLMo3-7b, SmolLM3-3b, Nemotron3-nano) + 4 API models\n- 4 formats: JSON, XML, LaTeX, Markdown\n- Open-weight models: avg -5.8pp to -8.7pp on GPQA, MATH-500, ZebraLogic\n- Prompt-level format instructions cause ~3.9pp loss; decoder constraints add ~1.6pp more\n- Closed-weight models show little/no format tax\n- Proposed solution: decouple reasoning from formatting (2-pass or extended thinking)\n- DOES NOT study RL training or fine-tuning — purely inference-time prompting study\n\n### 2. D-CoT (arXiv:2602.21786, Feb 2026)\n- \"Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models\"\n- Uses control tags (&lt;TEMP_LOW>, &lt;TEMP_MID>, &lt;TEMP_HIGH>) as scaffolding during training\n- Key result: model internalizes structured tags — maintains/improves performance even WITHOUT tags at inference\n- Highest MMLU-Pro accuracy (64.73%) occurred WITHOUT tags vs 62.92% WITH tags\n- +9.9% GPQA-diamond, +9.1% MMLU-Pro with only 5,079 training samples on Qwen3-8B\n- Evidence of internalization: implicit fact organization, directed self-checking, suppressed unnecessary arithmetic\n\n### 3. CoRGI withdrawal\n- arXiv:2508.00378, withdrawn Oct 14, 2025\n- Reason: \"The paper is not yet mature and needs further improvement\"\n\n### 4. Imperfect Verifier (arXiv:2604.07666)\n- Noise rates up to 15% yield peak validation accuracy within 2pp of clean baseline\n- \"Imperfect verification does not constitute a fundamental barrier to RLVR\"\n- Recommendation: prioritize moderate accuracy with high precision\n\n## What needs to change (reviewer issues):\n\n### Issue 1 (LOW-MEDIUM): Cite Format Tax + D-CoT\nAdd to landscape and approach:\n- Acknowledge Format Tax documents 5.8-8.7pp degradation from structured XML/JSON in prompted open-weight models\n- Distinguish from CFRL: (a) D-CoT shows trained tags get internalized, performance maintained/improved when tags dropped, (b) CFRL trains citation via RL, not zero-shot prompting, (c) MuRGAt parallel — same zero-shot vs trained distinction\n- Add both to key_references\n\n### Issue 2 (LOW-MEDIUM): Explicitly argue additive reward advantage\nAdd 1-2 sentences in the approach explaining:\n- Additive reward (weighted sum) chosen specifically to avoid multiplicative error compounding\n- With N independent signals each having ~15% error, additive combination gives composite noise ~σ/√N (errors partially cancel) vs multiplicative where errors compound\n- This keeps training within the Imperfect Verifier tolerance regime\n\n### Issue 3 (LOW): Fix minor reference issues\n- Note CoRGI's withdrawal status in landscape\n- Specify minimum accuracy thresholds for grounding (≥80%) and completeness (≥70%), matching the existing 75% binding threshold\n- Add rationale for these thresholds\n\n### Issue 4 (LOW): Acknowledge 4B verifier precedent gap\n- More explicitly acknowledge no precedent for ≤4B multi-property semantic verification as training-time reward\n- MJ1 (3B active) is closest but evaluation-time with ~6144 output tokens\n- Specify what minimum per-property accuracy makes Tier 1 useful\n\n## INSTRUCTIONS:\n\nProduce a COMPLETE JSON object with ALL fields from the original, incorporating the changes above. The JSON should be valid and complete.\n\nHere is the original JSON to revise (I'll describe where each change goes):\n\n**In `opportunity`**: Add Format Tax + D-CoT discussion in the evidence-loss/diagnostic section. Note that Format Tax applies to inference-time prompting, not RL training, and D-CoT provides direct counter-evidence.\n\n**In `landscape`**: \n- Add a new paragraph/subsection about \"Format Tax and structured output overhead\" that covers both Format Tax and D-CoT\n- Update CoRGI reference to note withdrawal\n- Keep everything else the same\n\n**In `approach`**:\n- Add a paragraph about Format Tax mitigation after the MuRGAt paragraph (since it's a related concern about structured format degradation)\n- Add explicit additive reward advantage argument near the training/reward composition section\n- In the verifier validation protocol, add per-property accuracy thresholds for grounding (≥80%) and completeness (≥70%)\n- Acknowledge 4B verifier precedent gap more explicitly in the verifier architecture section\n\n**In `key_references`**: Add \"The Format Tax\" and \"D-CoT\" papers\n\n**In `changes_from_previous_revision`**: Document ALL changes made in this round\n\n**Set `change_type`**: \"minor\"\n\nNow here is the COMPLETE original JSON. Please produce the revised version with all changes integrated:\n\n{\n  \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier\",\n  \"core_problem\": \"How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?\",\n  \"opportunity\": \"Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.\",\n\nReplace the opportunity with one that ALSO adds: (7) Structured output formats themselves impose a 'Format Tax' — 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents 5.8–8.7pp reasoning degradation from XML/JSON requirements in prompted open-weight models — though this applies to inference-time prompting rather than RL-trained formats, and D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline and maintain or improve performance when tags are removed at inference time.\n\nFor the landscape, add this new subsection before \"The gap\":\n\n**Structured output overhead:** 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents that structured output requirements (JSON, XML, LaTeX, Markdown) degrade reasoning accuracy by 5.8–8.7pp across six open-weight models (Qwen3-32b/8b, OLMo3.1-32b/7b, SmolLM3-3b, Nemotron3-nano) on GPQA, MATH-500, and ZebraLogic, with most degradation arising from format-requesting prompt instructions (~3.9pp) rather than decoder constraints (~1.6pp). Critically, closed-weight models show little to no format tax, suggesting the problem is solvable through training rather than inherent to structured generation. D-CoT (arXiv:2602.21786, Feb 2026) provides direct counter-evidence for *trained* structured formats: models trained with control tags (&lt;TEMP_LOW>/&lt;TEMP_MID>/&lt;TEMP_HIGH>) internalize the discipline, achieving +9.9% GPQA-diamond and highest MMLU-Pro accuracy (64.73%) *without* tags at inference — exceeding tagged performance (62.92%) — with only 5K training samples on Qwen3-8B. This distinction between prompted format imposition (where the tax applies) and trained format internalization (where it does not) is directly relevant to CFRL's design.\n\nFor CoRGI in the landscape, update: \"CoRGI (arXiv:2508.00378, withdrawn Oct 2025) performed post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal. [Note: this paper was withdrawn by its authors as 'not yet mature'; we cite it for conceptual context only.]\"\n\nFor the approach, add after the MuRGAt paragraph and before the CFV section:\n\n**Addressing the Format Tax:** 'The Format Tax' (arXiv:2604.03616) documents 5.8–8.7pp reasoning degradation when open-weight models are *prompted* to produce structured XML/JSON output. While CFRL requires structured &lt;observe>/&lt;reason> tags, three factors distinguish our setting from the Format Tax regime: (1) *Trained vs. prompted format*: D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline — achieving highest accuracy *without* tags at inference (+9.9% GPQA-diamond, 64.73% vs. 62.92% MMLU-Pro on Qwen3-8B with 5K samples) — indicating that RL-trained format requirements do not incur the same tax as inference-time prompting. (2) *Curriculum-developed skill*: Like the MuRGAt distinction, CFRL develops citation as a learned skill via reward optimization across curriculum phases, not a zero-shot constraint. (3) *Counterfactual monitoring*: Safeguard #5 directly measures any format-induced degradation by comparing tagged vs. untagged accuracy every 500 steps, providing an empirical check against format tax emergence during training. If format-related degradation is detected (tagged accuracy < untagged − 2pp), we activate a mitigation protocol: reducing format reward weight and increasing the proportion of untagged rollouts to prevent the model from over-investing in format compliance at the expense of reasoning quality.\n\nFor the additive reward argument, add near the training section (after the composite reward equation):\n\n**Additive reward structure for noise tolerance:** The weighted-sum reward combination R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness + ε·R_format − P_leak is specifically chosen over multiplicative or conjunctive alternatives to prevent error compounding. With independent per-property verification errors of ~15% (within the 'Imperfect Verifier' tolerance regime), additive combination yields composite noise that partially cancels across components (~σ/√N reduction for N independent signals), keeping the effective noise well within the ≤15% threshold where RL training degrades by ≤2pp. A multiplicative combination (e.g., R = R_accuracy × R_grounding × R_binding) would compound errors: three signals each with 85% accuracy yield ~61% joint accuracy, pushing noise far beyond the tolerance boundary. The additive structure also provides graceful degradation — if one property's verifier underperforms, the remaining signals still provide useful gradient, whereas multiplicative combination would zero out the reward whenever any single property check fails.\n\nFor verifier validation, update to add per-property thresholds:\n\n**Verifier validation protocol**: Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with minimum deployment thresholds of ≥80% balanced accuracy for grounding (motivated by PEARL's perception checklist achieving ~85% agreement with human judgments), ≥75% for binding validity (where symbolic/arithmetic checks provide exact verification for Tier 1, with the threshold applying to the verifier's assessment of qualitative bindings), and ≥70% for completeness (set lower to reflect the inherent noisiness of relevance filtering, where human inter-annotator agreement is only 74.6% per arXiv:2410.15531). Tier 1 binding is validated separately for arithmetic (expected ~95%+ via symbolic execution) and geometry-symbolic components (expected ~85%+ via theorem library matching). (b) ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on any property falls below its deployment threshold, we activate property-specific fallbacks: for grounding, soften to probabilistic confidence scores; for binding, restrict to Tier 1 symbolic-only verification (which has near-perfect accuracy); for completeness, set δ=0 and report Tier 1 results as the core finding.\n\nFor the verifier architecture section, add acknowledgment of the precedent gap:\n\n**Verifier architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass. We acknowledge that no existing ≤4B model has been validated for multi-property semantic verification (grounding + binding + completeness) as a training-time reward signal — MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens and no throughput constraints. Our design bets on two factors that make this feasible: (1) the CFV output is shorter (~500-1500 tokens vs. MJ1's ~6144) because inline verification verdicts are more compact than MJ1's full grounded verification chain with pairwise comparison, and (2) Tier 1 binding validity relies on symbolic/arithmetic checking rather than learned semantic judgment, offloading the hardest verification subtask from the neural model. If the 4B model proves insufficient for multi-property verification in a single pass, our fallback is a two-pass architecture: a first pass for grounding verification and a second for binding/completeness, each with shorter output and more focused instruction — still yielding ≤2 calls per rollout vs. FGRPO's S ≈ 5-8.\n\nThen produce the COMPLETE JSON with ALL of these changes integrated, plus:\n- Updated key_references adding the two new papers\n- Updated changes_from_previous_revision documenting round 6 changes\n- change_type: \"minor\"\n\nMake sure the JSON is valid. Output ONLY the JSON, no other text.\n",
    "agentId": "a755fbd23f7e43021",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Since I can't write files or run python, I'll produce the complete JSON directly in my response. Let me make sure it's comprehensive and valid.\n\nHere is the complete revised JSON:\n\n```json\n{\n  \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier\",\n  \"change_type\": \"minor\",\n  \"core_problem\": \"How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?\",\n  \"opportunity\": \"Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. (7) Structured output formats themselves impose a 'Format Tax' — 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents 5.8–8.7pp reasoning degradation from XML/JSON requirements in prompted open-weight models — though this applies to inference-time prompting rather than RL-trained formats, and D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline and maintain or improve performance when tags are removed at inference time. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.\",\n  \"landscape\": \"**Evidence grounding and binding verification:** PEARL (CVPR 2026) introduces a perception checklist that gates reasoning on perception accuracy, achieving ~85% agreement with human judgments on visual fact verification. FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, but at multiplicative cost (~6-8 judge calls per sentence \\u00d7 multiple sentences \\u00d7 rollouts). MJ1 (Mar 2026) trains a 3B-active-parameter judge with a 5-stage grounded verification chain producing ~6144 output tokens, demonstrating that structured multi-property verification is feasible at small scale — but operates at evaluation time with no throughput constraints, not as a training-time reward signal. PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating. Vision-SR1 decomposes reasoning into perception and reasoning stages with structured tags, using self-reward. TreeVGR (ICLR 2026) and ViGoRL train models to generate spatial evidence via RL, but verify localization (bounding-box IoU) rather than reasoning validity.\\n\\n**Token-level credit and attention methods:** PGPO, SAYO, AT-RL, VICRA, and KAWHI reweight optimization toward visually-dependent tokens using attention-based or gradient-based proxies. Faithful-MR1 (May 2026) anchors attention to causal image regions. These methods use statistical proxies for visual dependency rather than verifying semantic correctness of how evidence is used in reasoning. v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access. SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL.\\n\\n**Completeness gap:** No existing method verifies integration completeness — whether all task-relevant visual facts are bound to reasoning steps. MathLens (Feb 2026) identifies completeness failures as the growing error fraction in multimodal reasoning. 'Don't Blink' (Apr 2026) shows this worsens as reasoning unfolds, with attention to evidence regions dropping >50% over the course of a reasoning chain.\\n\\n**Diagnostic frameworks:** The PAR framework (Mar 2026) diagnoses that 'alignment' — mapping perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone, motivating a dedicated binding validity check. MuRGAt (Feb 2026) documents that enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution — a critical cautionary finding that motivates developing citation as a trained skill via RL rather than imposing it as a zero-shot constraint.\\n\\n**Post-hoc verification:** CoRGI (arXiv:2508.00378, withdrawn Oct 2025) performed post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal. [Note: this paper was withdrawn by its authors as 'not yet mature'; we cite it for conceptual context only.]\\n\\n**Structured output overhead:** 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents that structured output requirements (JSON, XML, LaTeX, Markdown) degrade reasoning accuracy by 5.8\\u20138.7pp across six open-weight models (Qwen3-32b/8b, OLMo3.1-32b/7b, SmolLM3-3b, Nemotron3-nano) on GPQA, MATH-500, and ZebraLogic, with most degradation arising from format-requesting prompt instructions (~3.9pp) rather than decoder constraints (~1.6pp). Critically, closed-weight models show little to no format tax, suggesting the problem is solvable through training rather than inherent to structured generation. D-CoT (arXiv:2602.21786, Feb 2026) provides direct counter-evidence for *trained* structured formats: models trained with control tags (&lt;TEMP_LOW>/&lt;TEMP_MID>/&lt;TEMP_HIGH>) internalize the discipline, achieving +9.9% GPQA-diamond and highest MMLU-Pro accuracy (64.73%) *without* tags at inference — exceeding tagged performance (62.92%) — with only 5K training samples on Qwen3-8B. This distinction between prompted format imposition (where the tax applies) and trained format internalization (where it does not) is directly relevant to CFRL's design.\\n\\n**Imperfect verification:** 'An Imperfect Verifier is Good Enough' (arXiv:2604.07666, 2026) demonstrates that noise rates up to 15% in reward signals yield peak validation accuracy within 2pp of clean baseline, establishing that imperfect verification does not constitute a fundamental barrier to RLVR. This directly motivates our verifier design: prioritize moderate accuracy with high precision rather than requiring perfect verification.\\n\\n**The gap:** No method unifies grounding verification, binding validity, and completeness checking in a single lightweight verifier that serves as a training-time reward signal. FGRPO checks grounding but not completeness, and at multiplicative cost. MJ1 demonstrates multi-property verification but at evaluation time only, with no throughput constraints. Attention-based methods use proxies rather than semantic verification. The opportunity is a distilled composition verifier (CFV) that performs all three checks in a single forward pass, enabling composition-faithful RL training at tractable cost.\",\n  \"approach\": \"We propose Composition Fidelity RL (CFRL), a training framework that uses a single distilled Composition Fidelity Verifier (CFV) to provide a multi-property reward signal for RL training, unifying evidence grounding, binding validity, and integration completeness verification.\\n\\n**Structured citation format:** CFRL trains models to produce reasoning traces with explicit &lt;observe>...&lt;/observe> and &lt;reason>...&lt;/reason> tags, where each &lt;reason> block cites specific &lt;observe> blocks. This structured format enables automated verification of all three composition properties. Unlike zero-shot prompting approaches where MuRGAt (Feb 2026) documents accuracy degradation from enforced structured grounding, CFRL develops citation as a learned skill via RL reward optimization — the model learns to cite because citing improves reward, not because it is constrained to cite at inference time.\\n\\n**Addressing the Format Tax:** 'The Format Tax' (arXiv:2604.03616) documents 5.8\\u20138.7pp reasoning degradation when open-weight models are *prompted* to produce structured XML/JSON output. While CFRL requires structured &lt;observe>/&lt;reason> tags, three factors distinguish our setting from the Format Tax regime: (1) *Trained vs. prompted format*: D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline — achieving highest accuracy *without* tags at inference (+9.9% GPQA-diamond, 64.73% vs. 62.92% MMLU-Pro on Qwen3-8B with 5K samples) — indicating that RL-trained format requirements do not incur the same tax as inference-time prompting. (2) *Curriculum-developed skill*: Like the MuRGAt distinction, CFRL develops citation as a learned skill via reward optimization across curriculum phases, not a zero-shot constraint. (3) *Counterfactual monitoring*: Safeguard #5 directly measures any format-induced degradation by comparing tagged vs. untagged accuracy every 500 steps, providing an empirical check against format tax emergence during training. If format-related degradation is detected (tagged accuracy < untagged \\u2212 2pp), we activate a mitigation protocol: reducing format reward weight and increasing the proportion of untagged rollouts to prevent the model from over-investing in format compliance at the expense of reasoning quality.\\n\\n**Composition Fidelity Verifier (CFV) — architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass, producing inline verdicts for each &lt;observe>/&lt;reason> pair: (a) *Grounding*: Is the cited visual evidence factually present in the image? (b) *Binding validity*: Does the inference logically follow from the cited evidence? (c) *Completeness*: Are all task-relevant visual facts cited by at least one reasoning step? We acknowledge that no existing \\u22644B model has been validated for multi-property semantic verification (grounding + binding + completeness) as a training-time reward signal — MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens and no throughput constraints. Our design bets on two factors that make this feasible: (1) the CFV output is shorter (~500-1500 tokens vs. MJ1's ~6144) because inline verification verdicts are more compact than MJ1's full grounded verification chain with pairwise comparison, and (2) Tier 1 binding validity relies on symbolic/arithmetic checking rather than learned semantic judgment, offloading the hardest verification subtask from the neural model. If the 4B model proves insufficient for multi-property verification in a single pass, our fallback is a two-pass architecture: a first pass for grounding verification and a second for binding/completeness, each with shorter output and more focused instruction — still yielding \\u22642 calls per rollout vs. FGRPO's S \\u2248 5-8. The CFV is distilled from a larger teacher verifier (Qwen3-VL-30B-A3B) using a curated verification dataset, with progressive distillation to maintain accuracy on each sub-task.\\n\\n**Tiered binding validity:** Binding validity verification is decomposed into two tiers: *Tier 1 (symbolic/arithmetic)*: For reasoning steps involving arithmetic, geometric, or logical operations, binding validity is checked via symbolic execution — parsing the cited evidence and the inference into formal representations and verifying logical entailment. Expected accuracy: ~95%+ for arithmetic (symbolic execution), ~85%+ for geometry-symbolic (theorem library matching). *Tier 2 (semantic/qualitative)*: For reasoning steps involving qualitative judgments (e.g., 'the object appears damaged'), binding validity requires the CFV's learned semantic judgment. This is the harder sub-task, where the 4B model's limitations are most likely to manifest. The tiered structure ensures that even if Tier 2 accuracy is modest, the overall binding signal remains useful because Tier 1 provides a reliable foundation. We specify a minimum per-property accuracy that makes Tier 1 useful as a standalone signal: if only Tier 1 binding is validated (symbolic/arithmetic), we require \\u226590% balanced accuracy on Tier 1 items, which provides a meaningful training signal for the substantial fraction of mathematical/logical reasoning steps in our target benchmarks (MathVista, MMMU-Science).\\n\\n**Composite reward and training:** The RL training uses GRPO with a composite reward signal: R = \\u03b1\\u00b7R_accuracy + \\u03b2\\u00b7R_grounding + \\u03b3\\u00b7R_binding + \\u03b4\\u00b7R_completeness + \\u03b5\\u00b7R_format \\u2212 P_leak, where R_accuracy is task correctness, R_grounding/R_binding/R_completeness are CFV-derived property scores, R_format rewards well-formed citation structure, and P_leak penalizes reasoning traces that 'leak' answers without citing evidence. Weights are set via curriculum: Phase 1 (accuracy + format only, \\u03b1=1.0, \\u03b5=0.3), Phase 2 (add grounding, \\u03b2=0.3), Phase 3 (add binding + completeness, \\u03b3=0.2, \\u03b4=0.15). The binding threshold for crediting a reasoning step is set at 75%.\\n\\n**Additive reward structure for noise tolerance:** The weighted-sum reward combination R = \\u03b1\\u00b7R_accuracy + \\u03b2\\u00b7R_grounding + \\u03b3\\u00b7R_binding + \\u03b4\\u00b7R_completeness + \\u03b5\\u00b7R_format \\u2212 P_leak is specifically chosen over multiplicative or conjunctive alternatives to prevent error compounding. With independent per-property verification errors of ~15% (within the 'Imperfect Verifier' tolerance regime), additive combination yields composite noise that partially cancels across components (~\\u03c3/\\u221aN reduction for N independent signals), keeping the effective noise well within the \\u226415% threshold where RL training degrades by \\u22642pp. A multiplicative combination (e.g., R = R_accuracy \\u00d7 R_grounding \\u00d7 R_binding) would compound errors: three signals each with 85% accuracy yield ~61% joint accuracy, pushing noise far beyond the tolerance boundary. The additive structure also provides graceful degradation — if one property's verifier underperforms, the remaining signals still provide useful gradient, whereas multiplicative combination would zero out the reward whenever any single property check fails.\\n\\n**Verifier validation protocol:** Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with minimum deployment thresholds of \\u226580% balanced accuracy for grounding (motivated by PEARL's perception checklist achieving ~85% agreement with human judgments), \\u226575% for binding validity (where symbolic/arithmetic checks provide exact verification for Tier 1, with the threshold applying to the verifier's assessment of qualitative bindings), and \\u226570% for completeness (set lower to reflect the inherent noisiness of relevance filtering, where human inter-annotator agreement is only 74.6% per arXiv:2410.15531). Tier 1 binding is validated separately for arithmetic (expected ~95%+ via symbolic execution) and geometry-symbolic components (expected ~85%+ via theorem library matching). (b) Ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on any property falls below its deployment threshold, we activate property-specific fallbacks: for grounding, soften to probabilistic confidence scores; for binding, restrict to Tier 1 symbolic-only verification (which has near-perfect accuracy); for completeness, set \\u03b4=0 and report Tier 1 results as the core finding.\\n\\n**Training safeguards:** (1) Reward hacking detection: monitor for traces that game citation format without meaningful content. (2) Curriculum gating: each phase requires validation accuracy above threshold before proceeding. (3) KL penalty against base model to prevent reward over-optimization. (4) Leak penalty P_leak to prevent answer-first-cite-later patterns. (5) Format tax monitoring: compare tagged vs. untagged accuracy every 500 steps; if tagged accuracy drops below untagged \\u2212 2pp, reduce format reward weight and increase untagged rollout proportion.\\n\\n**Evaluation:** Primary benchmarks: MathVista (mathematical visual reasoning), MMMU (multi-discipline multimodal understanding), ScienceQA (science reasoning). Composition fidelity metrics: grounding precision/recall, binding accuracy, completeness coverage. Baselines: (1) Standard GRPO without composition reward, (2) FGRPO-style per-sentence VLM judge (cost comparison), (3) Ablations removing each reward component individually. Key ablations: (a) Full CFRL vs. accuracy-only RL vs. each property reward in isolation; (b) CFV at 4B vs. teacher verifier at 30B (quality-cost tradeoff); (c) Curriculum vs. simultaneous reward introduction; (d) Noise injection ablation following Imperfect Verifier methodology.\",\n  \"key_references\": [\n    \"PEARL: Perception-Gated Reasoning for Multimodal Large Language Models (CVPR 2026) — perception checklist gates reasoning; ~85% human agreement; motivates grounding threshold\",\n    \"FGRPO: Fine-Grained Reinforcement from Perception Optimization (Apr 2026) — per-sentence VLM judge for grounding/consistency; primary cost comparison target\",\n    \"Faithful-MR1: Faithful Multimodal Reasoning via Attention Anchoring (May 2026) — attention-based causal region grounding\",\n    \"PaLMR: Process-Level Visual Fidelity via V-GRPO (CVPR 2026) — binary perception gating for process reward\",\n    \"MJ1: Training a 3B Multi-Judge for Grounded Verification Chains (Mar 2026) — 5-stage verification at 3B active params, evaluation-time with ~6144 output tokens; closest precedent for multi-property verification at small scale\",\n    \"MathLens: Diagnosing Completeness Failures in Multimodal Reasoning (Feb 2026) — identifies completeness as growing error fraction\",\n    \"Don't Blink: Attention Decay in Long Multimodal Reasoning (Apr 2026) — evidence attention drops >50% over reasoning chains\",\n    \"PAR Framework: Diagnosing Alignment as Distinct Failure Mode (Mar 2026) — motivates dedicated binding validity check\",\n    \"MuRGAt: Structured Grounding Degrades Accuracy in Zero-Shot Settings (Feb 2026) — cautionary finding motivating trained vs. prompted distinction\",\n    \"CoRGI: Post-Hoc Step-Wise CoT Verification via Visual Grounding (arXiv:2508.00378, withdrawn Oct 2025) — conceptually related verification chain; inference-time only; withdrawn as 'not yet mature'\",\n    \"An Imperfect Verifier is Good Enough (arXiv:2604.07666, 2026) — noise up to 15% yields \\u22642pp degradation; motivates additive reward structure and verifier tolerance thresholds\",\n    \"The Format Tax: Structured Output Degrades Reasoning in Open-Weight Models (arXiv:2604.03616, Apr 2026) — documents 5.8\\u20138.7pp degradation from XML/JSON in prompted open-weight models across GPQA, MATH-500, ZebraLogic; applies to inference-time prompting, not RL-trained formats\",\n    \"D-CoT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models (arXiv:2602.21786, Feb 2026) — trained structured tags internalized; +9.9% GPQA-diamond, 64.73% MMLU-Pro without tags > 62.92% with tags; direct counter-evidence to format tax for trained formats\",\n    \"TreeVGR: Training Models to Generate Bounding-Box Evidence via RL (ICLR 2026) — spatial grounding via dual IoU reward; verifies localization not reasoning validity\",\n    \"Vision-SR1: Self-Reward via Perception-Reasoning Decomposition (2026) — structured tags with self-reward; checks self-containment not factual correctness\",\n    \"PGPO / SAYO / AT-RL / VICRA / KAWHI — token-level credit methods reweighting toward visually-dependent tokens\",\n    \"v1: Interleaved Visual Grounding via Point-and-Copy (May 2026) — 300K traces with embedding re-access\",\n    \"SIEVE: Iterative Re-Access of Cached Visual Evidence During RL (Mar 2026) — embedding-level visual grounding\",\n    \"VTPerception-R1: Perception-Aware RL with Visual/Textual/Consistency Rewards (2026)\"\n  ],\n  \"changes_from_previous_revision\": [\n    \"Round 6 (minor revision): (1) Added 'The Format Tax' (arXiv:2604.03616) and D-CoT (arXiv:2602.21786) citations and discussion. In opportunity: added point (7) acknowledging the Format Tax documents 5.8\\u20138.7pp degradation from structured XML/JSON in prompted open-weight models, while distinguishing that this applies to inference-time prompting and D-CoT provides counter-evidence for trained structured formats. In landscape: added new 'Structured output overhead' subsection covering Format Tax findings (3.9pp from prompt instructions, 1.6pp from decoder constraints, closed-weight models unaffected) and D-CoT counter-evidence (trained tags internalized, +9.9% GPQA-diamond, 64.73% MMLU-Pro without tags > 62.92% with tags on Qwen3-8B with 5K samples). In approach: added 'Addressing the Format Tax' paragraph distinguishing CFRL from the Format Tax regime via three factors (trained vs. prompted format with D-CoT evidence, curriculum-developed skill per MuRGAt distinction, counterfactual monitoring via Safeguard #5 with mitigation protocol). Added both papers to key_references.\",\n    \"Round 6 (minor revision): (2) Added explicit additive reward advantage argument. New paragraph 'Additive reward structure for noise tolerance' explains that weighted-sum combination is specifically chosen to prevent error compounding \\u2014 with ~15% independent per-property errors, additive combination yields ~\\u03c3/\\u221aN composite noise (errors partially cancel), keeping training within the Imperfect Verifier \\u226415% tolerance regime where degradation is \\u22642pp. Contrasts with multiplicative combination where three 85%-accurate signals yield only ~61% joint accuracy, exceeding tolerance. Notes graceful degradation: underperforming single-property verifier does not zero out reward.\",\n    \"Round 6 (minor revision): (3) Fixed reference issues. Updated CoRGI entry in landscape to note withdrawal status (arXiv:2508.00378, withdrawn Oct 2025, 'not yet mature') and clarify it is cited for conceptual context only. Updated key_references entry for CoRGI similarly. Added per-property minimum accuracy thresholds to verifier validation protocol: \\u226580% balanced accuracy for grounding (motivated by PEARL's ~85% human agreement), \\u226575% for binding validity (threshold applies to qualitative bindings; Tier 1 symbolic has near-perfect accuracy), \\u226570% for completeness (reflects inherent noisiness of relevance filtering, human inter-annotator agreement 74.6%). Added rationale for each threshold. Added separate Tier 1 validation for arithmetic (~95%+ via symbolic execution) and geometry-symbolic (~85%+ via theorem library matching). Added property-specific fallback protocols.\",\n    \"Round 6 (minor revision): (4) Acknowledged 4B verifier precedent gap more explicitly. Added paragraph in CFV architecture section stating no existing \\u22644B model has been validated for multi-property semantic verification as training-time reward signal. Cited MJ1 (3B active) as closest precedent but for evaluation-time judging with ~6144 output tokens and no throughput constraints. Identified two factors making 4B feasible: shorter CFV output (~500-1500 tokens vs. ~6144) and Tier 1 symbolic offloading. Specified two-pass fallback architecture if single-pass proves insufficient. Added minimum per-property accuracy specification for Tier 1 standalone utility (\\u226590% balanced accuracy on Tier 1 items).\"\n  ]\n}\n```\n\nHere is a summary of all changes integrated into the revised JSON:\n\n**Issue 1 -- Format Tax + D-CoT citations (LOW-MEDIUM):**\n- **Opportunity**: Added point (7) documenting 5.8-8.7pp Format Tax degradation from structured XML/JSON in prompted open-weight models, with the key distinction that this applies to inference-time prompting and D-CoT provides counter-evidence for trained formats.\n- **Landscape**: Added new \"Structured output overhead\" subsection covering Format Tax findings (6 models, 3.9pp from prompt instructions, 1.6pp from decoder constraints, closed-weight unaffected) and D-CoT counter-evidence (tags internalized, +9.9% GPQA-diamond, 64.73% > 62.92% MMLU-Pro without tags on Qwen3-8B with 5K samples).\n- **Approach**: Added \"Addressing the Format Tax\" paragraph with three distinguishing factors (trained vs. prompted per D-CoT, curriculum-developed skill per MuRGAt, counterfactual monitoring via Safeguard #5 with mitigation protocol).\n- **Key references**: Added both \"The Format Tax\" (arXiv:2604.03616) and \"D-CoT\" (arXiv:2602.21786).\n\n**Issue 2 -- Additive reward advantage (LOW-MEDIUM):**\n- **Approach**: Added \"Additive reward structure for noise tolerance\" paragraph explaining weighted-sum chosen to prevent error compounding. With ~15% independent per-property errors, additive yields ~sigma/sqrt(N) composite noise vs. multiplicative yielding ~61% joint accuracy (three 85%-accurate signals). Notes graceful degradation property.\n\n**Issue 3 -- Reference fixes (LOW):**\n- **Landscape**: Updated CoRGI to note withdrawal status (arXiv:2508.00378, withdrawn Oct 2025, \"not yet mature\"), cited for conceptual context only.\n- **Approach/Verifier validation**: Added per-property minimum accuracy thresholds: >=80% grounding (PEARL's ~85% agreement), >=75% binding (Tier 1 symbolic near-perfect), >=70% completeness (human IAA 74.6%). Added rationale for each. Added Tier 1 separate validation (arithmetic ~95%+, geometry-symbolic ~85%+). Added property-specific fallback protocols.\n\n**Issue 4 -- 4B verifier precedent gap (LOW):**\n- **Approach/CFV architecture**: Explicit acknowledgment that no existing <=4B model validated for multi-property semantic verification as training-time reward. MJ1 (3B active) closest but evaluation-time with ~6144 tokens. Two feasibility factors: shorter output (~500-1500 tokens) and Tier 1 symbolic offloading. Two-pass fallback architecture specified. Minimum Tier 1 standalone accuracy: >=90% balanced accuracy on Tier 1 items."
      }
    ],
    "totalDurationMs": 517134,
    "totalTokens": 66710,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 112,
      "cache_read_input_tokens": 59004,
      "output_tokens": 7593,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 112
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7593,
          "cache_read_input_tokens": 59004,
          "cache_creation_input_tokens": 112,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 112,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 3,
      "searchCount": 7,
      "bashCount": 3,
      "editFileCount": 3,
      "linesAdded": 108,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "4e254796-96ef-4a1f-8633-483298f9a590",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "16e7e643-fa7f-4488-9ab8-8be77bd8be08",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Assistant

_source line 46 · 2026-05-27T23:30:23.687Z_

<details><summary>Logged reasoning block</summary>

```text
The agent produced the revised JSON. Let me review the output carefully and make sure it's complete and accurate. The agent produced a good revision, but I need to verify:

1. The JSON includes all original fields (title, core_problem, opportunity, landscape, approach, resource_estimate, target_venues, level, key_references, description, project_name, source, changes_from_previous_revision, change_type, inspired_by)
2. All reviewer issues are addressed

Looking at the agent's output, I notice some fields are missing from the JSON:


- `resource_estimate` - missing
- `target_venues` - missing
- `level` - missing
- `description` - missing
- `project_name` - missing
- `source` - missing
- `inspired_by` - missing

Also, the `landscape` section was significantly restructured from the original, which might lose important detail. The original landscape was very comprehensive with detailed descriptions of each method. The revised landscape is more concise but may be missing critical information.

Additionally, the `key_references` list was significantly shortened from the original 40+ references to about 19. The reviewer said to ADD references, not remove them. I need to reconstruct the complete JSON myself, being careful to preserve all original content and ensure no fields are dropped or condensed inappropriately.

Looking at the reviewer's feedback more carefully, the requested changes are actually quite specific and additive: Format Tax + D-CoT discussion needs to be integrated into the opportunity, landscape, and approach sections; the additive reward advantage argument should be added to the approach; CoRGI withdrawal needs correction with per-property thresholds; and the 4B verifier precedent gap should be acknowledged. These are targeted additions, not wholesale restructuring. I should preserve the full original landscape with all its detailed method descriptions and keep all 40+ references intact while making these specific insertions.

Given the massive size of the original JSON, I'll need to write out the complete revised version carefully, making only the targeted additions the reviewer requested rather than condensing or restructuring anything.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16e7e643-fa7f-4488-9ab8-8be77bd8be08",
  "isSidechain": false,
  "requestId": "req_011CbTwgW6Ba1M98u8YuTs9E",
  "type": "assistant",
  "uuid": "71a59e20-704b-4cc7-88c3-fcbb99453d67",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPkV5ptkSnDZRqVGN73CMA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13262,
      "cache_read_input_tokens": 37020,
      "output_tokens": 18239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18239,
          "cache_read_input_tokens": 37020,
          "cache_creation_input_tokens": 13262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13262
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

_source line 47 · 2026-05-27T23:37:59.216Z_

The agent produced a good draft but significantly restructured the landscape and dropped many fields and references. I need to produce the final version myself, making targeted additions to the original while preserving all existing content. Let me construct the complete revision:

```json
{
  "title": "Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier",
  "change_type": "minor",
  "core_problem": "How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?",
  "opportunity": "Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along multiple axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. (7) Structured output formats themselves impose a 'Format Tax' — 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents 5.8–8.7pp reasoning degradation from XML/JSON requirements in prompted open-weight models — though this applies to inference-time prompting rather than RL-trained formats, and D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline and maintain or improve performance when tags are removed at inference time. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.",
  "landscape": "The landscape of RL-based multimodal reasoning training has exploded in early 2026 along seven axes:\n\n**Perception-gating methods:** PEARL (CVPR 2026) derives a perception checklist of factual sub-questions, computes a perceptual reward R̄_p, and uses it as a fidelity gate — blocking reasoning policy updates when perception fails. Gains: +6.6% over GRPO on MathVerse. Limitation: checks perception accuracy but not whether perceived facts are correctly *bound* to reasoning steps or whether integration is *complete*. PaLMR (CVPR 2026, arXiv:2603.06652) introduces V-GRPO (Vision-Guided GRPO) with a hierarchical reward R = S_vis × (α·S_ans + (1−α)·S_fmt), where S_vis is a binary visual fidelity gate computed via pairwise comparison against pseudo ground-truth image descriptions generated by Gemini. Achieves 70.9% on HallusionBench (+4.2pp over GRPO) with only 4,728 training instances and 88% model-human alignment. Limitation: uses external pseudo ground-truth for comparison rather than verifying the model's own explicit evidence citations; does not check completeness; binary gating provides no gradient signal for partial fidelity improvement.\n\n**Token-level credit reallocation methods:** VPPO (ICLR 2026) reweights by KL divergence on perturbed images. PGPO (Apr 2026) amplifies learning signals for visually-dependent tokens via threshold-gated advantage reallocation (+18.7% avg). VGPO (ACL 2026) adds visual attention compensation. AT-RL (Feb 2026) identifies ~15% anchor tokens via cross-modality connectivity for targeted credit assignment (+1.2% overhead, 32B surpasses 72B-Instruct). VICRA (2026) reallocates optimization toward visually-grounded tokens (+2.25 avg on Qwen2.5-VL-7B). KAWHI (Mar 2026) performs paragraph-level credit reallocation via structured attribution of vision-critical attention heads. SAYO (Feb 2026) introduces region-level visual attention reward (r_v = tanh(log(a_q/v_q))) on Qwen3-VL-8B. Collective limitation: all operate on statistical attention patterns rather than verifying the semantic correctness of evidence-to-reasoning binding.\n\n**Explicit evidence grounding in RL training:** TreeVGR (ICLR 2026) trains models to generate text-space bounding box coordinates as traceable evidence within reasoning trajectories, supervised via dual IoU reward (R_IoU = ½(R_IoU^R + R_IoU^P)) that balances precision and recall of spatial localization. Two-stage training (SFT on 37K samples + RL). Achieves +16.8 on V*Bench, +12.6 on MME-RealWorld. Limitation: verifies *spatial* localization via IoU but not the *semantic validity* of how localized evidence is used in reasoning — a correct bounding box around a labeled angle does not verify that the angle value was correctly read or correctly applied in an inference step. Does not check integration completeness. v1 (May 2026, arXiv:2505.18842) introduces a point-and-copy mechanism where the model selects relevant image patches and copies their embeddings back into the reasoning stream, maintaining visual grounding throughout multi-step reasoning. Trained via SFT on v1g (300K grounding-annotated traces); RL integration is noted as future work. Achieves 68.6% MathVista, 34.5% MathVision. Limitation: operates at the embedding/representation level — re-inserts visual features but does not produce explicit textual evidence citations that can be externally verified for semantic correctness; grounding is implicit in the representation space rather than auditable. VTPerception-R1 (arXiv:2509.24776) implements a two-stage framework (perception-augmented SFT + perception-aware RL) with three perception rewards: visual key-info coverage (R_vkey), textual key-info coverage (R_tkey), and consistency (R_cons = |F_ans∩E|/max(1,|F_ans|)). Achieves 82.5% AI2D, 71.0% MathVista. Limitation: R_vkey measures perception-level element coverage (are visual elements mentioned?) but does not verify binding validity (are inferences logically consistent with cited evidence?) or integration completeness (are all task-relevant facts addressed?). SIEVE (arXiv:2603.14117) trains models to iteratively re-access cached visual region embeddings during RL (GRPO with ℛ = λ₁ℛ_res + λ₂ℛ_format + λ₃ℛ_emb + λ₄ℛ_act), supporting multi-turn evidence refinement. Achieves +7.85 on V*Bench overall. Limitation: like v1, operates at the embedding level — re-inserted features improve grounding but don't produce explicit verifiable citations; iterative re-access addresses the evidence-loss problem but not semantic verification of how evidence supports conclusions.\n\n**Self-rewarding perception-reasoning decomposition:** Vision-SR1 (arXiv:2508.19652) decomposes reasoning into explicit &lt;visual_perception> and &lt;think> stages, requiring the model to first articulate a self-contained visual description, then reason from it. The visual reward is computed via self-rewarding: the frozen policy model is re-prompted to answer the question using only the generated visual perception text (without image access); if the correct answer is derived from perception alone, a visual reward of 1 is assigned. Uses GRPO with a decoupled reward-advantage framework that maintains separate advantages for visual and answer rewards. Three-stage training: SFT cold-start on 9K examples, then standard rollout with accuracy reward, then self-reward rollout. Achieves 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B (+1.4 over Vision-R1), 69.8 on HallusionBench. Key distinction from CFRL: (a) Vision-SR1 uses self-rewarding (same model judges itself) rather than an external distilled verifier — the reward is whether perception suffices to re-derive the answer, not whether each cited fact is *factually accurate* relative to the image; a hallucinated but internally consistent perception could score high. (b) Vision-SR1 checks perceptual *self-containment* (can you answer from perception alone?) while CFRL checks factual grounding accuracy (is the perception correct?), binding validity (does the inference follow from cited evidence?), and completeness (are all task-relevant facts covered). (c) Vision-SR1 does not verify the logical consistency between perceived evidence and drawn inferences — it treats perception and reasoning as decomposed stages but does not check whether the reasoning is faithful to the specific evidence cited.\n\n**Constrained/faithful training methods:** FGRPO (Apr 2026, arXiv:2604.08476) enforces consistency + semantic grounding + spatial grounding as constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7% and improving grounding by +13 points. Uses Qwen3-VL-30B-A3B-Instruct (MoE, ~3.3B active parameters) as the online judge during training. The semantic grounding reward R_S requires per-sentence VLM judge calls: each non-trivial visual sentence in the CoT is independently evaluated, resulting in ~30-55 judge calls per training sample. This is the closest competitor — but does not check integration completeness. Faithful-MR1 (May 2026) supervises a &lt;Focus> token's attention against image regions and uses counterfactual image intervention to reward attention concentration where vision causally matters. Operates on attention distributions rather than explicit evidence citations.\n\n**Structured verification and evaluation judges:** MJ1 (Mar 2026, arXiv:2603.07990) trains a 3B-active-parameter multimodal judge (based on Qwen3-VL-30B-A3B) using RL with a structured grounded verification chain: observations → claims → verification → evaluation → scoring, enforced via 11 required XML tags across 5 sequential stages. Achieves 77.0% on MMRB2, surpassing GPT-5 (72.2%) and Gemini-3-Pro (76.3%). Key distinction from CFRL: (a) MJ1 is an *evaluation-time* judge, not a training-time reward verifier; (b) MJ1 uses stage-separated grounding rather than inline evidence citations; (c) MJ1 performs pairwise response comparison, not composition property verification; (d) MJ1 does not check integration completeness. EVPV/Grounding the Score (Mar 2026) adds visual premise verification via constraint matching and reliability gating to PRMs — improves Best-of-N reranking but is *inference-only*. ViGoRL (2026) trains models to produce spatially grounded reasoning traces with coordinate-level evidence (86.4% on V*Bench) — addresses spatial grounding but not semantic binding validity. AutoRubric-R1V (arXiv:2510.14738) auto-generates rubric-based process rewards by distilling consistent reasoning checkpoints from successful trajectories via self-aggregation — rubric reward equals the fraction of satisfied checkpoints. Achieves +8.0 avg over Qwen2.5-VL-7B on 6 benchmarks. Distinct from CFRL: AutoRubric derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image; rubrics are answer-path-dependent rather than evidence-grounding-dependent. CoRGI (arXiv:2508.00378, withdrawn Oct 2025) performed post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal. [Note: this paper was withdrawn by its authors as 'not yet mature'; we cite it for conceptual context only.]\n\n**Structured output overhead:** 'The Format Tax' (arXiv:2604.03616, Apr 2026) documents that structured output requirements (JSON, XML, LaTeX, Markdown) degrade reasoning accuracy by 5.8–8.7pp across six open-weight models (Qwen3-32b/8b, OLMo3.1-32b/7b, SmolLM3-3b, Nemotron3-nano) on GPQA, MATH-500, and ZebraLogic, with most degradation arising from format-requesting prompt instructions (~3.9pp) rather than decoder constraints (~1.6pp). Critically, closed-weight models show little to no format tax, suggesting the problem is solvable through training rather than inherent to structured generation. D-CoT (arXiv:2602.21786, Feb 2026) provides direct counter-evidence for *trained* structured formats: models trained with control tags (&lt;TEMP_LOW>/&lt;TEMP_MID>/&lt;TEMP_HIGH>) internalize the discipline, achieving +9.9% GPQA-diamond and highest MMLU-Pro accuracy (64.73%) *without* tags at inference — exceeding tagged performance (62.92%) — with only 5K training samples on Qwen3-8B. This distinction between prompted format imposition (where the tax applies) and trained format internalization (where it does not) is directly relevant to CFRL's design.\n\n**Evidence-aware GRPO variants:** PRCO (Mar 2026) decomposes into Observer+Solver with separate utility/outcome rewards (+7 pts). DocR1 (2026) uses evidence-page guided GRPO for document understanding. OpenMMReasoner (CVPR 2026) achieves +11.6% over Qwen2.5-VL-7B via two-stage SFT+RL recipe.\n\n**Attribution and evidence-loss diagnostics:** MuRGAt (Feb 2026, arXiv:2602.11509) introduces a benchmark for multimodal fact-level attribution requiring models to generate explicit citations specifying modality and temporal segments. Critically, MuRGAt finds that 'increasing reasoning depth or enforcing structured grounding often degrades accuracy' in zero-shot/few-shot settings — even strong MLLMs frequently hallucinate citations despite correct reasoning. This documents an accuracy-faithfulness tradeoff that CFRL must address. 'Don't Blink: Evidence Collapse during Multimodal Reasoning' (Apr 2026, arXiv:2604.04207) documents that reasoning VLMs progressively lose visual grounding as reasoning unfolds — attention to annotated evidence regions drops >50% — creating confident but ungrounded predictions that text-only monitoring cannot detect. 'Deeper Thought, Weaker Aim' (Mar 2026, arXiv:2603.14184) independently confirms this, showing reasoning prompts significantly reduce attention to question-critical image regions. 'Compose and Fuse' (ICLR 2026) identifies task-composition and fusion as main barriers. MathLens (Feb 2026) shows integration failures grow as a fraction of remaining errors. The PAR framework (Mar 2026) decomposes multimodal math reasoning into Perception–Alignment–Reasoning and identifies alignment fragmentation as a distinct failure mode.\n\n**The gap:** PEARL and PaLMR check perception but not binding or completeness; FGRPO checks consistency+grounding but not completeness, with ~5-8x higher cost per rollout vs. single-pass verification; Vision-SR1 decomposes perception and reasoning with self-rewarding but does not verify factual grounding accuracy, binding validity, or completeness; TreeVGR and ViGoRL verify spatial localization but not semantic reasoning validity; v1 and SIEVE re-access visual evidence at the embedding level but don't produce auditable textual citations; VTPerception-R1 checks perception-level coverage but not binding validity or completeness; MJ1 demonstrates structured grounded verification chains but operates at evaluation time; AutoRubric-R1V provides process supervision via trajectory-mined rubrics but not composition property verification against the image; attention-based methods (PGPO, SAYO, AT-RL, Faithful-MR1) use statistical proxies; EVPV is inference-only. No existing method unifies all three composition properties (evidence grounding, binding validity, integration completeness) in a single lightweight training-time verifier. MuRGAt's accuracy-faithfulness tradeoff highlights that naive enforcement of structured citation degrades performance — but this was observed under zero-shot prompting, not RL training with curriculum scheduling. Similarly, the Format Tax documents degradation from prompted structured output — but D-CoT shows trained structured formats are internalized without accuracy loss, and CFRL's RL curriculum develops citation as a learned skill rather than an imposed constraint.",
  "inspired_by": "'Compose and Fuse' (ICLR 2026) explicit future direction for composition-aware training; MathLens integration-failure analysis; PAR framework's alignment decomposition; FGRPO's grounding+consistency insight (extended with completeness and efficiency); MJ1's structured verification chain (adapted from evaluation-time judge to training-time reward); PaLMR's visual fidelity gating (extended beyond binary gating to multi-property verification); TreeVGR's explicit evidence generation in RL (extended from spatial to semantic verification); v1's interleaved grounding paradigm (adapted from embedding-level to textual-citation-level); Vision-SR1's perception-reasoning decomposition with self-rewarding (extended from self-containment checking to external factual grounding + binding + completeness verification); MuRGAt's accuracy-faithfulness tradeoff (motivating curriculum training and accuracy-first reward scheduling); 'Don't Blink' and 'Deeper Thought, Weaker Aim' documenting evidence collapse (direct motivation for explicit evidence anchoring); 'An Imperfect Verifier is Good Enough' (Apr 2026) validating noisy-reward robustness for distilled verifiers; 'The Format Tax' (Apr 2026) documenting structured output degradation in prompted models (motivating trained-vs-prompted distinction and counterfactual format tax monitoring); D-CoT (Feb 2026) demonstrating trained tag internalization (supporting RL-trained citation viability); GeoSketch's symbolic reward for geometry; Geoparsing (Apr 2026) for formal diagram entity extraction; Chart-RVR's verifiable chart reasoning rewards (informing chart-domain binding checks); CHARGE's keypoint coverage metrics; Countdown-Code (2026) and PURE (2025) for reward hacking diagnosis and mitigation",
  "approach": "We propose Composition Fidelity RL (CFRL), which unifies evidence grounding, binding validity, and integration completeness verification in a single distilled composition verifier used as a GRPO training reward.\n\n**Structured output format:** The model generates responses with explicit &lt;observe entity='...' value='...'/> tags for visual evidence extraction and &lt;reason evidence='obs1,obs2' rule='...'> blocks for each reasoning step, requiring citation of specific observations and the inference rule applied. This explicit citation format enables automated verification — unlike attention-based methods that can only measure statistical dependency, or embedding-level methods (v1, SIEVE) that re-access visual features without producing auditable textual claims. Compared to TreeVGR's bounding-box coordinates, our citations capture *semantic* content ('radius = 5cm') rather than *spatial* location ([x1,y1,x2,y2]), enabling verification of whether the cited value is correct and whether the inference logically follows. Compared to MJ1's stage-separated verification chain, our format embeds evidence references *inline* with reasoning, creating direct referential links suitable for training-time throughput. Compared to Vision-SR1's &lt;visual_perception> block, our format provides *fine-grained, per-fact citations* (individual &lt;observe> tags) rather than a monolithic perception paragraph, enabling per-fact grounding verification and explicit evidence-to-inference linking via the evidence='obs1,obs2' attribute.\n\n**Addressing the accuracy-faithfulness tradeoff (MuRGAt):** MuRGAt (Feb 2026) found that enforcing structured grounding degrades accuracy in zero-shot/few-shot settings — models hallucinate citations despite correct reasoning. This is a direct challenge to CFRL's premise. We address it through four design choices: (1) *RL training develops citation as a learned skill*: unlike MuRGAt's zero-shot evaluation where citation is an imposed constraint, CFRL trains the model to produce faithful citations through reward optimization, allowing the model to develop integrated reasoning-citation capability rather than retrofitting citations onto existing reasoning. (2) *Accuracy-first curriculum scheduling*: Phase 0 (pre-curriculum) establishes answer accuracy via standard GRPO before introducing any citation requirements, ensuring the model's reasoning capability is preserved before grounding constraints are layered on. Citation rewards are introduced gradually with initial weight near zero, increasing only as the model demonstrates stable accuracy. (3) *Accuracy-dominant reward weighting*: R_accuracy receives weight α ≥ 0.4 throughout training, ensuring citation quality never dominates at the expense of answer correctness. If accuracy on a held-out validation set drops >2pp at any curriculum transition, citation reward weights are halved until accuracy recovers. (4) *Counterfactual validation* (safeguard #5) directly monitors for MuRGAt-style degradation by comparing tagged vs. untagged accuracy.\n\n**Addressing the Format Tax:** 'The Format Tax' (arXiv:2604.03616) documents 5.8–8.7pp reasoning degradation when open-weight models are *prompted* to produce structured XML/JSON output, with most degradation arising from format-requesting prompt instructions (~3.9pp) rather than decoder constraints (~1.6pp). While CFRL requires structured &lt;observe>/&lt;reason> tags, three factors distinguish our setting from the Format Tax regime: (1) *Trained vs. prompted format*: D-CoT (arXiv:2602.21786) demonstrates that models trained with structured tags internalize the discipline — achieving highest accuracy *without* tags at inference (+9.9% GPQA-diamond, 64.73% vs. 62.92% MMLU-Pro on Qwen3-8B with only 5K samples) — indicating that RL-trained format requirements do not incur the same tax as inference-time prompting. The Format Tax itself notes that closed-weight models (which undergo extensive RLHF/format training) show little to no degradation, consistent with the hypothesis that training eliminates the tax. (2) *Curriculum-developed skill*: Like the MuRGAt distinction, CFRL develops citation as a learned skill via reward optimization across curriculum phases, not a zero-shot constraint. The model learns to cite because citing improves reward, not because it is constrained to produce XML at inference time. (3) *Counterfactual monitoring*: Safeguard #5 directly measures any format-induced degradation by comparing tagged vs. untagged accuracy every 500 steps, providing an empirical check against format tax emergence during training. If format-related degradation is detected (tagged accuracy < untagged − 2pp), we activate a mitigation protocol: reducing format reward weight and increasing the proportion of untagged rollouts to prevent the model from over-investing in format compliance at the expense of reasoning quality.\n\n**Composition Fidelity Verifier (CFV) — three-property checking:**\n(1) *Evidence grounding*: Checks whether cited visual facts (in &lt;observe> tags) correspond to actual image content. Uses a lightweight visual QA module that converts each citation into a yes/no visual question (e.g., 'Is the radius labeled as 5cm in the image?'). Inspired by PEARL's perception checklist but applied to model-generated citations rather than externally-derived sub-questions.\n(2) *Binding validity*: Checks logical consistency between cited evidence and the inference drawn. We define binding validity checks at two levels:\n\n  **Tier 1 — Domain-agnostic arithmetic + geometry symbolic (core contribution):**\n  - *Arithmetic verification* (all domains): Given numerical values extracted from &lt;observe> tags and a stated operation in the &lt;reason> block, verify computational correctness via symbolic execution. Concrete checks: (a) *Sum/difference/product/quotient consistency* — if obs1 cites 'value A = 45' and obs2 cites 'value B = 30', and the reason block claims 'difference = 15' with rule 'subtraction', verify 45−30=15. (b) *Ratio/percentage verification* — if 'Part = 120, Total = 400' and conclusion is '30%', verify 120/400=0.30. (c) *Comparison consistency* — if the reason block claims 'A > B' citing obs1 (A=45) and obs2 (B=30), verify 45>30. (d) *Multi-step arithmetic* — chain verification across sequential &lt;reason> blocks where one step's output is another's input. These checks are domain-agnostic: they apply equally to geometry problems (angle computations), chart problems (bar value comparisons, trend calculations), and diagram problems (counting, distance computations).\n  - *Geometry symbolic theorem matching*: Cited theorems/rules are matched against a geometry theorem library, and symbolic constraints are verified formally. For example, cited 'angle A=60°, angle B=90°' with rule 'triangle angle sum' → verify 60+90+x=180 → x=30°. Inspired by GeoSketch and the PAR framework.\n\n  **Tier 2 — Domain-specific binding checks (extension):**\n  - *Chart-specific*: (a) *Ordering consistency* — if 'Bar A > Bar B' is cited, verify against the extracted data table that value(A) > value(B). (b) *Extrema verification* — if 'X is the maximum value' is cited, verify X = max(all values in series). (c) *Trend verification* — if 'increasing from 2020 to 2023' is cited, verify monotonic increase in the relevant data points; trends are formally defined as: 'increasing' requires each successive value ≥ previous (strict: >), 'decreasing' requires ≤ (strict: <), with tolerance ε for noise. (d) *Aggregation verification* — if 'average = X' is cited, verify mean(values) ≈ X within 1% relative tolerance. These checks require the chart data table extracted in the completeness pipeline (Stage A), linking Tier 2 binding to Tier 2 completeness infrastructure.\n  - *Diagram-specific*: (a) *Structural relationship verification* — if 'A connects to B' is cited, verify edge (A,B) exists in the parsed graph from PGDP-Net. (b) *Attribute consistency* — if 'node A is labeled X' is cited, verify label(A) = X in the parsed representation. (c) *Cardinality verification* — if 'A has 3 connections' is cited, verify degree(A) = 3. (d) *Containment/hierarchy* — if 'A is inside B' is cited, verify the containment relation in the parsed spatial layout. These checks require the diagram graph representation from Stage A parsing.\n  - *Fallback for inapplicable checks*: When a &lt;reason> block involves qualitative reasoning that cannot be reduced to arithmetic or structural constraint checking (e.g., 'the diagram suggests a causal relationship between X and Y'), the binding check returns a neutral score (0.5) rather than penalizing, and the verifier flags it as 'unverifiable-binding' for monitoring. This prevents the binding reward from penalizing valid qualitative reasoning while maintaining signal for verifiable steps.\n\n(3) *Integration completeness*: Checks whether all task-relevant visual facts are cited somewhere in the reasoning chain via a three-stage domain-specific pipeline:\n\n  **Stage A — Visual Element Enumeration** (domain-specific, offline or cached):\n  - *Geometry*: Use Geoparsing (arXiv:2604.11600, Apr 2026) to produce a formal entity/relation set from the diagram. Geoparsing achieves 96.4 F1 overall (points 99.6, lines 98.0, circles 98.3, semantics 90.7) using a unified formal language.\n  - *Charts*: Use DePlot/UniChart-style chart derendering to extract a linearized data table of all data points, then apply CHARGE-style keypoint extraction to convert to self-contained factual statements.\n  - *Diagrams*: Use PGDP-Net-style graph parsing to extract a node-edge representation of diagram primitives and their relations.\n\n  **Stage B — Question-Conditioned Relevance Filtering**:\n  - Apply VisDoT-style (arXiv:2603.11631) question decomposition to generate ordered perception sub-questions. Match sub-questions against enumerated visual elements from Stage A to produce a *required visual fact set* F_required.\n  - Reliability estimate: Sub-question coverage as a ranking metric achieves 82% accuracy against human preferences (arXiv:2410.15531), with human inter-annotator agreement of 74.6% on sub-question classification — indicating this is an inherently noisy signal, which motivates our soft treatment of completeness (see below).\n  - For geometry, the symbolic checker provides an additional signal: any entity appearing in the formal solution path is automatically added to F_required.\n\n  **Stage C — Coverage Verification**:\n  - Compute coverage score: R_completeness = |F_cited ∩ F_required| / |F_required|.\n  - We target ≥80% recall of task-relevant facts, acknowledging that completeness checking is inherently approximate. The 80% threshold is motivated by CHARGE's finding that even SOTA MLLMs achieve only 73.9% coverage with ground-truth retrieval.\n  - For facts in F_required that are NOT cited, the verifier generates a soft penalty proportional to the estimated importance of the missing fact.\n\n**Verifier architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass. The input consists of the image + the model's full tagged response + a structured verification instruction. The CFV generates verification judgments sequentially as autoregressive output: for each &lt;observe> tag, it produces an inline grounding verdict (verified/unverified with confidence score); for each &lt;reason> block, it produces a binding validity verdict; and finally, it produces an overall completeness assessment. This is architecturally identical to how MJ1 generates its multi-stage verification chain in one forward pass — the grounding VQA for each observation is performed as internal sub-reasoning within the autoregressive generation, NOT as separate VQA calls. The output length scales with the number of observations and reasoning steps (~500-1500 tokens for typical responses with 4-8 observations), but requires only a single image encoding through the vision encoder.\n\nWe acknowledge that no existing ≤4B model has been validated for multi-property semantic verification (grounding + binding + completeness) as a training-time reward signal with throughput constraints. MJ1 demonstrates 5-stage structured verification at 3B active parameters, but operates at evaluation time with ~6144 output tokens and no per-rollout latency budget. Our design bets on two factors that make this feasible: (1) the CFV output is substantially shorter (~500-1500 tokens vs. MJ1's ~6144) because inline verification verdicts are more compact than MJ1's full grounded verification chain with pairwise response comparison, and (2) Tier 1 binding validity relies primarily on symbolic/arithmetic checking rather than learned semantic judgment, offloading the hardest verification subtask from the neural model to deterministic execution. If the 4B model proves insufficient for multi-property verification in a single pass, our fallback is a two-pass architecture: a first pass for grounding verification and a second for binding/completeness, each with shorter output and more focused instruction — still yielding ≤2 calls per rollout vs. FGRPO's S ≈ 5-8.\n\n**Cost comparison with FGRPO (precise):** FGRPO requires S separate judge calls per rollout (S ≈ 5-8 visual sentences), each requiring its own image encoding through the 30B MoE model (3.3B active parameters). CFRL requires 1 verifier call per rollout with a single image encoding through the 4B dense model. Since image encoding is the dominant cost in VLM inference (processing hundreds of visual tokens through transformer layers), the savings from 1 vs. S encodings is the primary cost driver. Per-call text generation cost is roughly comparable: FGRPO generates S × ~150 = 750-1200 tokens total across all calls; CFRL generates ~500-1500 tokens in one call, at similar active parameter counts (3.3B MoE vs. 4B dense). The effective cost reduction is **~5-8x per rollout** (proportional to S), driven primarily by the single image encoding. Per training sample with K rollouts, FGRPO makes K×S judge calls vs. CFRL's K verifier calls — the same ~5-8x ratio holds. For Tier 1 (grounding + binding only), where binding validity uses lightweight symbolic/arithmetic checking outside the verifier, the verifier output is shorter (~300-800 tokens), further reducing per-call cost.\n\n**Staged contribution and risk mitigation (addressing system complexity):** The full CFRL system integrates multiple external tools and domain-specific pipelines, creating compounding failure risk. We structure the contribution in two defensible tiers:\n\n  *Tier 1 — Core contribution (grounding + binding):* Evidence grounding (VQA-based, all domains) and binding validity (domain-agnostic arithmetic verification + geometry symbolic theorem matching). This tier requires only the distilled 4B verifier and a geometry theorem library — no external parsing tools. Domain-agnostic arithmetic verification applies to chart and diagram problems too (any reasoning step involving numerical computation is checkable), providing cross-domain binding signal even without domain-specific infrastructure. This tier is self-contained, already differentiates from all existing methods (none verify binding validity as a training reward), and provides a defensible paper even if completeness checking and domain-specific binding prove too approximate. Estimated complexity: 1 distilled model + 1 theorem library.\n\n  *Tier 2 — Extension (completeness + domain-specific binding):* Integration completeness adds Geoparsing, DePlot/CHARGE, PGDP-Net, and VisDoT-style decomposition. Domain-specific binding for charts adds data-table-dependent checks (ordering, trends, extrema); for diagrams adds graph-dependent checks (structural relationships, attributes). Each integration is a potential failure point. Fallback strategies per component: (a) If Geoparsing underperforms on out-of-distribution diagrams, fall back to the distilled verifier's own visual element listing (lower accuracy but zero external dependency). (b) If relevance filtering is too noisy, use only the symbolic solver's required entities (geometry) or question-mentioned entities (charts/diagrams) as F_required — a conservative underestimate that still provides signal. (c) If domain-specific binding checks add noise rather than signal (e.g., trend verification on noisy data), fall back to Tier 1 arithmetic-only binding for that domain. (d) If end-to-end completeness R_completeness adds noise rather than signal, set δ=0 and report Tier 1 results as the core finding.\n\n  *Risk matrix:*\n  - Pipeline integration failure (MEDIUM risk): Mitigated by Tier 1/Tier 2 separation and per-component fallbacks.\n  - Verifier distillation quality (LOW risk): Validated via held-out test set; noise tolerance demonstrated by 'Imperfect Verifier' methodology.\n  - Accuracy-faithfulness tradeoff (MEDIUM risk): Mitigated by accuracy-first curriculum, accuracy-dominant reward weighting, and counterfactual monitoring (see MuRGAt discussion above).\n  - Format Tax emergence (LOW-MEDIUM risk): Mitigated by trained-vs-prompted distinction (D-CoT evidence), counterfactual monitoring (safeguard #5), and format reward weight reduction protocol.\n  - Tag gaming / Goodhart effects (LOW-MEDIUM risk): Mitigated by five anti-gaming safeguards (see below).\n  - Training instability from 5 reward components (MEDIUM risk): Mitigated by curriculum scheduling (components introduced sequentially, not simultaneously), reward weight monitoring, and additive reward structure (see below).\n\n**Verifier distillation:** The CFV is distilled from Qwen3-VL-235B-A22B on synthetically generated composition judgment pairs. We generate correct/incorrect binding examples by: (a) taking model solutions, (b) perturbing citations (wrong entity, wrong value, missing citation, irrelevant citation, logically inconsistent inference, arithmetic errors), (c) having the teacher label each perturbation type. Target: 50K examples across geometry, chart, and diagram domains, with balanced representation of arithmetic binding errors (Tier 1) and domain-specific binding errors (Tier 2). The distilled verifier (based on Qwen3-VL-4B) is validated on a held-out test set of 5K human-annotated composition judgments.\n\n**Verifier validation protocol**: Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with minimum deployment thresholds of ≥80% balanced accuracy for grounding (motivated by PEARL's perception checklist achieving ~85% agreement with human judgments, and the 'Imperfect Verifier' finding that ≤15% noise yields ≤2pp degradation), ≥75% for binding validity (where symbolic/arithmetic checks provide near-perfect verification for Tier 1, with the threshold applying to the verifier's assessment of qualitative Tier 2 bindings), and ≥70% for completeness (set lower to reflect the inherent noisiness of relevance filtering, where human inter-annotator agreement is only 74.6% per arXiv:2410.15531). Tier 1 binding is validated separately for arithmetic (expected ~95%+ via symbolic execution) and geometry-symbolic components (expected ~85%+ via theorem library matching). For Tier 1 standalone utility, we require ≥90% balanced accuracy on Tier 1 binding items, which provides a meaningful training signal for the substantial fraction of arithmetic/logical reasoning steps in our target benchmarks. (b) Ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on any property falls below its deployment threshold, we activate property-specific fallbacks: for grounding, soften to probabilistic confidence scores weighted by verifier certainty; for binding, restrict to Tier 1 symbolic-only verification (which has near-perfect accuracy); for completeness, set δ=0 and report Tier 1 results as the core finding.\n\n**Anti-gaming safeguards** (addressing Goodhart's Law risk):\n  (1) *Low format weight*: Format compliance ≤0.05 in composite reward. Dominant signals come from verifiable content-level checks.\n  (2) *Verifiable citation grounding*: Evidence grounding is checked against actual image content via visual QA — un-gameable.\n  (3) *Answer-leak detection*: Embedding cosine similarity monitoring between &lt;observe> content and final answer, with penalty P_leak.\n  (4) *KL regularization against base policy*: Standard KL penalty + format/content reward ratio monitoring; divergence triggers early stopping.\n  (5) *Counterfactual validation*: Every 500 steps, evaluate with tags stripped. If tagged accuracy exceeds untagged by >5pp, signal format-dependent performance and trigger reward recalibration. If tagged accuracy falls below untagged by >2pp, signal Format Tax emergence and reduce format reward weight.\n\n**Training:** GRPO on Qwen3-VL-8B via veRL with composite reward R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness + ε·R_format − P_leak.\n\n**Additive reward structure for noise tolerance:** The weighted-sum reward combination is specifically chosen over multiplicative or conjunctive alternatives to prevent error compounding. With independent per-property verification errors of ~15% (within the 'Imperfect Verifier' tolerance regime where noise yields ≤2pp degradation), additive combination yields composite noise that partially cancels across components (~σ/√N reduction for N independent signals), keeping the effective noise well within the ≤15% threshold. A multiplicative combination (e.g., R = R_accuracy × R_grounding × R_binding) would compound errors: three signals each with 85% accuracy yield ~61% joint accuracy, pushing noise far beyond the tolerance boundary. The additive structure also provides graceful degradation — if one property's verifier underperforms, the remaining signals still provide useful gradient, whereas multiplicative combination would zero out the reward whenever any single property check fails.\n\nCurriculum training: Phase 0 establishes baseline accuracy (week 1), Phase 1 trains grounding (weeks 1.5-2.5), Phase 2 adds binding validity (weeks 2.5-3.5), Phase 3 adds completeness (weeks 3.5-4.5). Training targets geometry (MathVerse, GeoQA+), chart (ChartQA, PlotQA), and diagram (AI2D, ScienceQA) tasks.\n\n**Key distinction from Vision-SR1:** Vision-SR1 decomposes reasoning into &lt;visual_perception> and &lt;think> stages and checks perceptual self-containment via self-rewarding — re-prompting the model without image access to verify the perception suffices. CFRL differs in three ways: (a) CFRL uses an external distilled verifier rather than self-rewarding — self-rewarding cannot detect hallucinated perceptions that happen to be internally consistent (a fabricated but plausible description could still support the correct answer), while external grounding verification checks each cited fact against the actual image. (b) CFRL provides fine-grained per-fact citations (&lt;observe> tags) rather than a monolithic perception block, enabling per-fact grounding verification and explicit evidence-to-inference linking. (c) CFRL verifies binding validity (does the inference logically follow from cited evidence?) and integration completeness, which Vision-SR1 does not address.\n\n**Key distinction from TreeVGR:** TreeVGR generates bounding-box coordinates as evidence and supervises spatial localization via dual IoU reward — verifying *where* the model attends. CFRL generates semantic textual citations and verifies *what* the model claims to see and *how* it reasons from those claims. These are complementary: TreeVGR could locate the correct region but misread the value; CFRL catches such semantic errors. TreeVGR does not check binding validity or integration completeness.\n\n**Key distinction from v1 and SIEVE:** Both re-access visual evidence at the embedding level — v1 via point-and-copy of patch embeddings, SIEVE via cached region embedding re-insertion. This maintains visual grounding in the model's internal representation but does not produce *explicit, auditable textual claims* about what was perceived. CFRL requires the model to articulate its visual evidence in natural language, enabling external verification of both the perception (grounding) and the reasoning (binding validity). v1 uses SFT only; SIEVE uses RL but without composition-level verification.\n\n**Key distinction from VTPerception-R1:** VTPerception-R1's R_vkey/R_tkey rewards check perception-level element coverage (whether visual/textual elements are mentioned in reasoning), while R_cons checks entity-attribute consistency. CFRL goes further in two ways: (a) binding validity checks logical inference consistency, not just entity-mention consistency, and (b) integration completeness checks coverage of all task-relevant facts via structured enumeration, not just key-info recall from a VLM scorer.\n\n**Key distinction from FGRPO:** FGRPO uses Qwen3-VL-30B-A3B-Instruct as per-sentence online judge, resulting in ~30-55 judge calls per training sample. Our single-pass CFV reduces this to ~K calls per sample (one per rollout), yielding ~5-8x cost reduction driven by single image encoding per rollout vs. S encodings. More importantly, CFRL adds completeness checking. FGRPO uses Lagrangian dual ascent; we use direct reward weighting with curriculum scheduling.\n\n**Key distinction from PaLMR:** PaLMR's V-GRPO uses binary visual fidelity gate (S_vis ∈ {0,1}) providing no gradient for partial improvement. CFRL provides continuous, multi-property reward signals. PaLMR does not require or verify explicit evidence citations.\n\n**Key distinction from MJ1:** MJ1 is evaluation-time judge with 5-stage pipeline (up to 6144 tokens). CFRL adapts structured verification to training-time with compact inline citations. CFRL checks completeness, which MJ1 does not.\n\n**Key distinction from PEARL:** PEARL checks perception accuracy of externally-generated sub-questions. CFRL checks grounding, validity, and completeness of the model's own explicit evidence citations.\n\n**Key distinction from AutoRubric-R1V:** AutoRubric-R1V provides process supervision by mining rubric checkpoints from successful trajectories — it checks whether the model's reasoning path conforms to patterns found in correct solutions. CFRL instead verifies composition properties against the image itself: whether cited evidence is factually grounded, inferences are valid, and coverage is complete. These are complementary: AutoRubric rewards path conformity, CFRL rewards evidence fidelity.\n\n**Key distinction from attention-based methods (PGPO, SAYO, Faithful-MR1):** These measure statistical attention patterns. CFRL requires and verifies explicit semantic citation.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "950 (verifier distillation: 100h on 4xH100; Geoparsing/DePlot integration and symbolic checker development: 80h; completeness pipeline development: 70h; main GRPO training: 400h on 8xH100; ablations including verifier accuracy sweep, anti-gaming validation, and baselines: 300h)",
      "timeline": "10 weeks (1.5w setup + data + completeness pipeline + symbolic checker, 1.5w verifier training + validation, 3w main experiments with curriculum, 2.5w ablations + verifier accuracy study + anti-gaming analysis, 1.5w analysis and writing — overlapping phases)",
      "estimated_gpu_cost": "$1,250 (H100 spot at ~$1.30/GPU-hr on Spheron/RunPod 2026 rates)"
    },
    "human_in_loop": {
      "gpu_hours": "950 (same experimental requirements)",
      "timeline": "8 weeks (Claude accelerates verifier data generation, completeness pipeline scaffolding, experiment analysis)",
      "claude_api_cost": "$300 (code assistance, composition judgment labeling assistance, completeness annotation, paper drafting)",
      "estimated_gpu_cost": "$1,250"
    },
    "auto_research": {
      "gpu_hours": "1500 (additional hyperparameter sweeps for α/β/γ/δ/ε, verifier architecture search, verifier accuracy noise ablation, completeness pipeline ablation per domain, anti-gaming validation suite, extended baselines including PEARL+FGRPO+PaLMR+TreeVGR+Vision-SR1 reimplementation, symbolic checker coverage expansion)",
      "timeline": "7 weeks (parallelized experiment scheduling, automated verifier validation)",
      "claude_api_cost": "$1,000 (teacher labeling for verifier data: $600 for ~50K composition judgments via Qwen3-VL-235B; completeness annotation for chart/diagram domains: $100; experiment orchestration, analysis, and ablation design: $300)",
      "estimated_gpu_cost": "$1,950",
      "speed_bottleneck": "Verifier data generation requires teacher model (Qwen3-VL-235B) inference at ~50K examples; Geoparsing inference for geometry completeness pipeline; verifier validation requires human-annotated held-out set (5K examples); GRPO rollout reward evaluation is sequential per batch; curriculum phasing requires sequential training stages; anti-gaming counterfactual validation adds ~10% overhead per checkpoint"
    }
  },
  "target_venues": [
    "ICLR 2027 (estimated late Sep 2026, ~17 weeks from now — primary target with sufficient buffer for experiments + writing)",
    "AAAI 2027 (abstract: Jul 21, paper: Jul 28, 2026 — stretch goal, 8 weeks with zero buffer; feasible only with aggressive parallelization and if verifier distillation completes in week 2)",
    "CVPR 2027 (estimated ~Nov 2026, not yet announced — fallback if additional ablations needed)"
  ],
  "level": "top-tier",
  "key_references": [
    "Compose and Fuse: Revisiting the Foundational Bottlenecks in Multimodal Reasoning (ICLR 2026)",
    "Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning [PEARL] (CVPR 2026)",
    "PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment [V-GRPO] (CVPR 2026, arXiv:2603.06652)",
    "MJ1: Multimodal Judgment via Grounded Verification (arXiv:2603.07990, Mar 2026)",
    "Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv Mar 2026)",
    "Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization [FGRPO] (arXiv:2604.08476, Apr 2026)",
    "Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention (arXiv May 2026)",
    "TreeVGR: Traceable Evidence Enhanced Visual Grounded Reasoning (ICLR 2026, arXiv:2507.07999)",
    "v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv:2505.18842, May 2026)",
    "VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding (arXiv:2509.24776)",
    "SIEVE: Improving Visual Reasoning with Iterative Evidence Refinement (arXiv:2603.14117, Mar 2026)",
    "Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization (arXiv:2508.19652)",
    "AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning (arXiv:2510.14738)",
    "CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv:2508.00378, withdrawn Oct 2025)",
    "MuRGAt: Multimodal Fact-Level Attribution for Verifiable Reasoning (arXiv:2602.11509, Feb 2026)",
    "Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv:2604.04207, Apr 2026)",
    "Deeper Thought, Weaker Aim: Understanding and Mitigating Perceptual Impairment during Reasoning in MLLMs (arXiv:2603.14184, Mar 2026)",
    "The Format Tax: Structured Output Degrades Reasoning in Open-Weight Models (arXiv:2604.03616, Apr 2026)",
    "D-CoT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models (arXiv:2602.21786, Feb 2026)",
    "Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models [PGPO] (arXiv Apr 2026)",
    "Credit Where It is Due: Cross-Modality Connectivity Drives Precise RL for MLLM Reasoning [AT-RL] (arXiv Feb 2026)",
    "Don't Lose Sight: Visually-Grounded Credit Assignment for Multimodal Reasoning [VICRA] (2026)",
    "Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs [SAYO] (arXiv Feb 2026)",
    "Grounded Reinforcement Learning for Visual Reasoning [ViGoRL] (arXiv 2026)",
    "What MLLMs Learn about When they Learn about Multimodal Reasoning [MathLens] (arXiv 2026)",
    "Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)",
    "Deconstructing Multimodal Mathematical Reasoning: Towards a Unified Perception-Alignment-Reasoning Paradigm [PAR] (arXiv Mar 2026)",
    "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv:2604.07666, Apr 2026)",
    "GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025/2026)",
    "Geoparsing: Unified Formal Language for Geometry Diagram Parsing (arXiv:2604.11600, Apr 2026)",
    "Benchmarking Multimodal RAG through a Chart-based Document Question-Answering Generation Framework [CHARGE] (arXiv:2502.14864, 2025)",
    "DePlot: One-shot Visual Language Reasoning by Plot-to-Table Translation (2023)",
    "VisDoT: Decomposition of Thought with Visual Interpretation Grounding (arXiv:2603.11631, Mar 2026, EACL 2026 Findings)",
    "Countdown-Code: A Testbed for Reward Hacking in RLVR (arXiv:2603.07084, Mar 2026)",
    "PURE: Pessimistic Unbiased Reward Estimation for RL with Noisy Rewards (arXiv:2504.15275, NeurIPS 2025)",
    "Spotlight on Token Perception for Multimodal Reinforcement Learning [VPPO] (ICLR 2026)",
    "Visually-Guided Policy Optimization for Multimodal Reasoning [VGPO] (ACL 2026)",
    "DocR1: Evidence Page-Guided GRPO for Multi-Page Document Understanding (arXiv 2026)",
    "OpenMMReasoner: Pushing the Frontiers for Multimodal Reasoning with an Open and General Recipe (CVPR 2026)",
    "From Sight to Insight: Improving Visual Reasoning Capabilities of Multimodal Models via RL (arXiv 2026)",
    "Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)",
    "Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR [TGRL] (arXiv 2026)",
    "Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage (arXiv:2410.15531, NAACL 2025)",
    "PGDP-Net: Plane Geometry Diagram Parsing with Graph Neural Networks (IJCAI 2022)",
    "Chart-RVR: Reinforcement Learning with Verifiable Rewards for Explainable Chart Reasoning (arXiv:2510.10973)"
  ],
  "description": "We address the composition gap in multimodal reasoning training: while recent methods tackle perception gating (PEARL, PaLMR), attention-level credit reallocation (PGPO, SAYO, AT-RL, VICRA, KAWHI), grounding+consistency constraints (FGRPO), causal attention anchoring (Faithful-MR1), structured grounded evaluation (MJ1), self-rewarding perception decomposition (Vision-SR1), spatial evidence localization (TreeVGR, ViGoRL), embedding-level evidence re-access (v1, SIEVE), perception-level coverage rewards (VTPerception-R1), rubric-based process supervision (AutoRubric-R1V), post-hoc visual verification (CoRGI, withdrawn), and evidence-loss diagnostics ('Don't Blink', 'Deeper Thought, Weaker Aim'), none unifies evidence grounding, binding validity, and integration completeness verification in a single lightweight training-time verifier. We propose Composition Fidelity RL (CFRL), which requires models to generate explicit evidence citations (&lt;observe>/&lt;reason evidence=''>) and trains a distilled Composition Fidelity Verifier (CFV, 4B parameters) to check three properties: (1) evidence grounding — cited facts match image content, (2) binding validity — inferences are logically consistent with cited evidence, and (3) integration completeness — all task-relevant visual facts are cited. Binding validity is structured in two tiers: Tier 1 (core) provides domain-agnostic arithmetic verification (sum/difference/ratio/comparison consistency between cited values and computed results) and geometry symbolic theorem matching, applicable across all domains without external tools; Tier 2 (extension) adds domain-specific checks for charts (ordering consistency, extrema, trend monotonicity, aggregation) and diagrams (structural relationship, attribute, cardinality verification), requiring parsed data representations. The CFV performs all verification in a single autoregressive forward pass — processing the image once and generating inline grounding/binding verdicts for each observation and reasoning step sequentially — yielding ~5-8x cost reduction over FGRPO's per-sentence judge calls (driven by 1 vs. S ≈ 5-8 image encodings per rollout). We acknowledge that no existing ≤4B model has been validated for multi-property semantic verification as a training-time reward signal; MJ1 (3B active) is the closest precedent but operates at evaluation time with ~6144 output tokens. Our design is supported by shorter CFV output (~500-1500 tokens) and Tier 1 symbolic offloading, with a two-pass fallback if single-pass proves insufficient. The contribution is structured in two tiers: Tier 1 (core: grounding + arithmetic/geometric binding verifier, self-contained with no external tool dependencies) and Tier 2 (extension: completeness pipeline with domain-specific parsing + domain-specific binding checks), ensuring the paper is defensible even if completeness checking or domain-specific binding proves too approximate. Critically, we address MuRGAt's finding that enforcing structured grounding degrades accuracy in zero-shot settings through accuracy-first curriculum scheduling (Phase 0 establishes baseline accuracy before citation requirements), accuracy-dominant reward weighting (α ≥ 0.4), and counterfactual validation monitoring. We also address 'The Format Tax' (arXiv:2604.03616), which documents 5.8–8.7pp degradation from structured XML/JSON in prompted open-weight models, by distinguishing CFRL's RL-trained citation format from prompted format imposition: D-CoT (arXiv:2602.21786) demonstrates that trained structured tags are internalized (+9.9% GPQA-diamond, highest MMLU-Pro accuracy without tags exceeding with-tag performance on Qwen3-8B), and CFRL's counterfactual monitoring (safeguard #5) empirically checks for format tax emergence during training. The additive reward structure (weighted sum of independent verifier signals) is specifically chosen to prevent multiplicative error compounding: with ~15% independent per-property errors, additive combination yields composite noise ~σ/√N that partially cancels, keeping training within the 'Imperfect Verifier' tolerance regime (≤15% noise → ≤2pp degradation), whereas a multiplicative combination would compound to ~61% joint accuracy. The CFV is distilled from Qwen3-VL-235B on 50K synthetic composition judgments and validated on 5K held-out human-annotated examples, with per-property minimum deployment thresholds (≥80% grounding, ≥75% binding, ≥70% completeness) and noise-tolerance ablation. Unlike Vision-SR1 (self-rewarding checks perceptual self-containment but not factual accuracy or binding validity), we use an external verifier that checks each cited fact against the image. Unlike FGRPO (per-sentence judge), our single-pass verifier reduces cost ~5-8x. Unlike TreeVGR/ViGoRL (spatial localization via IoU), we verify semantic content and reasoning validity. Unlike v1/SIEVE (embedding-level re-access), we require auditable textual citations. Unlike VTPerception-R1 (perception-level coverage), we check binding validity and structured completeness. Unlike AutoRubric-R1V (trajectory-mined rubrics), we verify composition properties against the image. We incorporate anti-gaming safeguards against tag-format Goodhart effects: low format weight (≤0.05), verifiable citation grounding, answer-leak detection, KL regularization, and periodic counterfactual validation (also serving as Format Tax monitoring). We train Qwen3-VL-8B via GRPO on geometry, chart, and diagram tasks with curriculum scheduling. Key baselines: PEARL-7B (+6.6% over GRPO), FGRPO-7B (1.7% inconsistency, +13 grounding), PaLMR-7B (70.9% HallusionBench), TreeVGR-7B (+16.8 V*Bench), VTPerception-R1-7B (82.5% AI2D), Vision-SR1-7B (58.8 avg, 69.8 HallusionBench), PGPO (+18.7% avg), OpenMMReasoner-7B (+11.6%), AutoRubric-R1V-7B (+8.0 avg), MJ1 (77.0% MMRB2), and Faithful-MR1-7B.",
  "project_name": "composition_fidelity_rl",
  "source": "web_research",
  "changes_from_previous_revision": {
    "issue_1_format_tax_dcot": "Added 'The Format Tax' (arXiv:2604.03616, Apr 2026) and D-CoT (arXiv:2602.21786, Feb 2026) citations and discussion throughout the proposal. In opportunity: added point (7) documenting 5.8–8.7pp degradation from structured XML/JSON in prompted open-weight models, with the key distinction that this applies to inference-time prompting and D-CoT provides counter-evidence for trained structured formats (tags internalized, highest accuracy achieved without tags at inference). In landscape: added new 'Structured output overhead' subsection covering Format Tax findings across 6 open-weight models (Qwen3-32b/8b, OLMo3.1-32b/7b, SmolLM3-3b, Nemotron3-nano) with decomposition of degradation sources (3.9pp from prompt instructions, 1.6pp from decoder constraints), note that closed-weight models show no tax, and D-CoT's counter-evidence (+9.9% GPQA-diamond, 64.73% > 62.92% MMLU-Pro without tags on Qwen3-8B with 5K samples). In approach: added dedicated 'Addressing the Format Tax' paragraph distinguishing CFRL from the Format Tax regime via three factors — (a) trained vs. prompted format with D-CoT internalization evidence and Format Tax's own observation that closed-weight models are unaffected, (b) curriculum-developed skill paralleling MuRGAt distinction, (c) counterfactual monitoring via safeguard #5 with explicit format tax mitigation protocol (reduce format weight, increase untagged rollouts when tagged accuracy < untagged − 2pp). Updated risk matrix to include Format Tax emergence as LOW-MEDIUM risk. Updated safeguard #5 to serve dual purpose (Goodhart detection and Format Tax monitoring). Both papers added to key_references and inspired_by.",
    "issue_2_additive_reward_advantage": "Added explicit 'Additive reward structure for noise tolerance' paragraph in the approach, near the composite reward equation and training section. Explains that weighted-sum combination is specifically chosen over multiplicative/conjunctive alternatives to prevent error compounding. With ~15% independent per-property errors, additive combination yields ~σ/√N composite noise (errors partially cancel across N independent signals), keeping effective noise within the 'Imperfect Verifier' ≤15% tolerance regime where RL training degrades by ≤2pp. Contrasts with multiplicative combination where three 85%-accurate signals yield only ~61% joint accuracy, far exceeding the tolerance boundary. Notes graceful degradation property: underperforming single-property verifier still allows useful gradient from remaining signals, whereas multiplicative combination zeros out reward when any single property check fails. Also added to description summary.",
    "issue_3_corgi_withdrawal_and_thresholds": "Updated CoRGI reference throughout: landscape entry now reads 'CoRGI (arXiv:2508.00378, withdrawn Oct 2025)' with note 'this paper was withdrawn by its authors as not yet mature; we cite it for conceptual context only.' Updated key_references entry and description to note withdrawal. Added per-property minimum accuracy thresholds to verifier validation protocol: ≥80% balanced accuracy for grounding (motivated by PEARL's ~85% human agreement and Imperfect Verifier's 15% noise tolerance), ≥75% for binding validity (threshold applies to qualitative Tier 2 bindings; Tier 1 symbolic has near-perfect accuracy), ≥70% for completeness (reflects inherent noisiness of relevance filtering, human inter-annotator agreement only 74.6% per arXiv:2410.15531). Added separate Tier 1 validation targets: arithmetic ~95%+ via symbolic execution, geometry-symbolic ~85%+ via theorem library matching. Added property-specific fallback protocols: grounding → probabilistic confidence scores; binding → restrict to Tier 1 symbolic-only; completeness → set δ=0. Added Tier 1 standalone utility threshold of ≥90% balanced accuracy on Tier 1 items.",
    "issue_4_4b_verifier_precedent": "Added explicit acknowledgment in verifier architecture section that no existing ≤4B model has been validated for multi-property semantic verification (grounding + binding + completeness) as a training-time reward signal with throughput constraints. Cited MJ1 (3B active parameters) as closest precedent but operating at evaluation time with ~6144 output tokens and no per-rollout latency budget. Identified two factors supporting feasibility: (1) substantially shorter CFV output (~500-1500 tokens vs. ~6144) due to compact inline verdicts vs. full pairwise comparison chain, and (2) Tier 1 symbolic/arithmetic offloading reduces the neural model's verification burden. Specified two-pass fallback architecture if single-pass proves insufficient (grounding pass + binding/completeness pass), still yielding ≤2 calls per rollout vs. FGRPO's 5-8. Added to description summary."
  }
}
```

## Summary of changes (Round 6, minor revision)

All four reviewer issues addressed with targeted additions:

1. **Format Tax + D-CoT** (LOW-MEDIUM → resolved): Added as point (7) in opportunity, new "Structured output overhead" landscape subsection, and dedicated "Addressing the Format Tax" approach paragraph. Key argument: Format Tax applies to *prompted* format (5.8–8.7pp loss), but D-CoT proves *trained* tags are internalized (64.73% MMLU-Pro without tags > 62.92% with tags). CFRL's RL curriculum develops citation as a trained skill, not a prompted constraint. Safeguard #5 now serves dual purpose as format tax monitor.

2. **Additive reward advantage** (LOW-MEDIUM → resolved): New paragraph explains weighted-sum chosen to prevent error compounding. With ~15% per-property error, additive noise ~σ/√N stays within Imperfect Verifier tolerance (≤2pp degradation), while multiplicative would compound to ~61% joint accuracy. Graceful degradation: one weak verifier doesn't zero out reward.

3. **CoRGI + thresholds** (LOW → resolved): CoRGI marked as withdrawn Oct 2025 throughout. Per-property deployment thresholds specified: ≥80% grounding, ≥75% binding, ≥70% completeness, with rationale for each and property-specific fallback protocols.

4. **4B verifier precedent** (LOW → resolved): Explicit acknowledgment of unprecedented nature, MJ1 as closest precedent (evaluation-time only), two feasibility factors (shorter output + Tier 1 symbolic offloading), and two-pass fallback architecture specified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "71a59e20-704b-4cc7-88c3-fcbb99453d67",
  "isSidechain": false,
  "requestId": "req_011CbTwgW6Ba1M98u8YuTs9E",
  "type": "assistant",
  "uuid": "4fae8439-5b4c-400e-be1c-8fd5fe8572c1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RPkV5ptkSnDZRqVGN73CMA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13262,
      "cache_read_input_tokens": 37020,
      "output_tokens": 18239,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13262,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 18239,
          "cache_read_input_tokens": 37020,
          "cache_creation_input_tokens": 13262,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13262
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

_source line 48_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "4fae8439-5b4c-400e-be1c-8fd5fe8572c1",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 49_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 50_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity…",
  "leafUuid": "4fae8439-5b4c-400e-be1c-8fd5fe8572c1",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---

### Runtime record

_source line 51_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise composition fidelity RL proposal based on round 5 feedback",
  "sessionId": "9c94f57c-4ce2-468b-8638-fea3e33c2121"
}
```

---
