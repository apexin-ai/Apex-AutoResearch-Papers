# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "tit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 33
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/8fc053cf-e20a-48d4-a0fc-7b2966f0b112.jsonl`
- **Structured JSON:** [`8ec5212a522cf56a143b.json`](../../sessions/8e/8ec5212a522cf56a143b.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T20:23:32.230Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T20:23:32.230Z",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",\n  \"core_problem\": \"Generative PRMs (ThinkPRM, GenPRM, R-PRM) produce CoT verification rationales, but R-Align (Feb 2026) shows existing GenRMs exhibit substantial Spurious Correctness -- label-correct decisions with misaligned rationales -- and 'Outcome Accuracy is Not Enough' finds approximately 40% rationale consistency with human judgments. R-PRM demonstrates that reasoning-driven evaluation substantially improves accuracy (+13.9 F1 on ProcessBench), yet even rich multi-dimensional reasoning analyses lack formal grounding and have unknown faithfulness. Can we train generative verifiers whose rationales are grounded in structured formal proof artifacts, reducing spurious correctness and producing the first PRMs with formally traceable error explanations?\",\n  \"opportunity\": \"GenRM reviewer 3 raised the unresolved concern that CoT rationales may be 'plausible-sounding but unfaithful reasoning that happens to correlate with correct verdicts.' FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can generate step-level error labels transferring across 12 benchmarks, but FoVer explicitly restricts to classification-based PRMs producing only binary labels, excluding generative/reasoning-based PRMs. R-PRM (EMNLP 2025) shows that reasoning-driven step evaluation -- generating multi-dimensional analyses before judgments -- substantially improves PRM accuracy (+13.9 F1 on ProcessBench via DPO), but its rationales are trained on LLM-generated seed data without formal grounding and faithfulness is not evaluated. ThinkPRM generates rich verification CoTs but trains on synthetic rationales of unknown faithfulness. The untried bridge is extracting structured proof artifacts -- Z3 counterexamples, Isabelle proof state information -- from FoVer's verification pipeline and using them as grounding signals for ThinkPRM-style rationale generation. This fills the gap that reasoning-driven methods (R-PRM, ThinkPRM, GenPRM) leave open: not just whether the PRM gets the label right, but whether its explanation is formally traceable to the actual mathematical error. Critically, Faithful Autoformalization (Amrollahi et al., April 2026) has now validated and quantified the roundtrip verification mechanism we adopt for quality filtering, showing 45-66% baseline equivalence rates improvable to 78-86% with standard diagnosis-guided repair or up to 91-95% with cross-model diagnosis -- providing empirical grounding for our data pipeline feasibility. Moreover, FoVer itself demonstrates easy-to-difficult transfer: PRMs trained on GSM8K-level data significantly improve step-level verification on MATH (88.0% vs 78.2% baseline), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%), suggesting that improving rationale faithfulness on foundational domains propagates to harder reasoning tasks.\",\n  \"landscape\": \"ThinkPRM (arXiv 2025) achieves 8% improvement on GPQA-Diamond over discriminative verifiers using only 1% of PRM800K labels (specifically 1K synthetic verification CoTs filtered to ~8K step labels), but its rationales lack formal grounding. GenPRM (AAAI 2026) combines CoT with code verification, enabling 1.5B models to outperform GPT-4o on ProcessBench using only 23K training examples. R-PRM (EMNLP 2025) introduces reasoning-driven process reward modeling: it generates multi-dimensional step analyses (Previous Steps Analysis, Now Step Analysis, Data Source Analysis, Consistency Analysis, Calculation Analysis) followed by binary judgments. Using Qwen2.5-Math-7B-Instruct as the base model, R-PRM-7B-DPO achieves 70.4 F1 on ProcessBench (+13.9 over Qwen2.5-Math-7B-PRM800K at 58.5 F1) and +8.5 F1 on PRMBench, with consistent +8.6 accuracy improvements on six downstream math reasoning datasets via best-of-N selection. R-PRM trains on ~289K SFT samples and ~269K DPO pairs bootstrapped from PRM800K annotations, achieving comparable performance to Qwen2.5-Math-PRM with only ~15% of its data volume. Critically, while R-PRM produces rich natural-language reasoning for each step evaluation, it does not evaluate rationale faithfulness -- the analyses are trained on LLM-generated seed data and may exhibit the same spurious correctness that R-Align identifies in other GenRMs. R-PRM demonstrates the ceiling of what reasoning-driven evaluation achieves without formal grounding: substantial accuracy gains, but with unknown rationale fidelity to the actual mathematical errors. FoVer (ACL 2026 Findings) uses Z3/Isabelle for automated step-level labeling with easy-to-difficult transfer (trained on GSM8K-level, evaluates on MATH/AIME/Olympiad), but produces only binary labels and explicitly excludes reasoning-based PRMs citing 'substantially higher computational costs.' FoVer-40K contains 40,000 balanced training steps (20K formal logic from FLDx2 + 20K theorem proving from GSM8K-level problems) with 50% error rate, generated from solutions by Llama 3.1 8B and Qwen 2.5 7B; the raw unbalanced pipeline output is substantially larger (~216K steps from 10K problems per task across both models). 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) is concurrent work that synthesizes PRM training data through a four-stage pipeline: constructing correct symbolic reasoning chains from rule templates, injecting template-aware errors into intermediate steps, symbolically recomputing subsequent steps to maintain trajectory consistency, and verifying that injected errors are not derivable from the prefix. They produce 20K paired (correct, erroneous) trajectories across 11 error types (7 truth-state: drop_condition, implication_misuse, or_and_confusion, partial_evaluation, xor_as_or, xor_as_equiv, vacuous_truth_error; 4 structural: converse_error, redundant_step, missing_prerequisite, circular_reference), translated into natural-language processes for PRM training. Their method improves best-of-8 reranking on logical reasoning benchmarks (Llama-3.1-8B: 0.528 -> 0.591, Qwen-2.5-7B: 0.567 -> 0.615 average F1), with limited transfer to mathematics (ProcessBench GSM8K: 21.2% F1). The key methodological distinction from our work: they generate controlled synthetic errors through template-based injection for accuracy-focused PRM training, while we extract genuine proof artifacts from naturally occurring errors in LLM solutions for faithfulness-focused rationale grounding. Their error diversity is constrained by predefined templates (an acknowledged limitation), while our artifacts reflect the actual distribution of errors that LLMs make. The two approaches are complementary -- their controlled error injection could extend the diversity of training scenarios, while our proof-artifact extraction provides traceable explanations of why each error is wrong. RM-R1 (ICLR 2026) trains reasoning reward models with explicit rationale chains but without formal grounding. R-Align (Feb 2026) introduces the Spurious Correctness (S-Corr) metric showing existing GenRMs exhibit substantial spuriously correct decisions (the abstract reports 'substantial S-Corr even for competitive GenRMs'; specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract), providing the key diagnostic our work aims to improve. 'Outcome Accuracy is Not Enough' (Qwen team, Feb 2026, arXiv 2602.04649) introduces a competing non-formal approach to improving rationale quality: they define Rationale Consistency via MetaJudge, which decomposes human rationales into atomic claims and performs strict one-to-one semantic matching against model justifications, finding frontier GenRMs achieve only ~40% rationale consistency. They train with a multiplicative hybrid signal R_final = R_rationale * R_outcome via GRPO, achieving RM-Bench 87.1% and JudgeBench 82.0% (+5% over outcome-only baselines, +7% on Arena Hard v2 creative writing during RLHF). Crucially, their approach targets Judge faithfulness (evaluation rationale quality) rather than Solver verification, and relies on soft semantic matching against human annotations -- providing broader applicability but weaker guarantees than formal artifact tracing. Their acknowledged limitation is scalability: computing rationale consistency still requires high-quality human annotations. Our formal grounding provides deterministic, traceable guarantees within Z3/Isabelle's decidable scope, while their approach extends to any domain with human annotations. The two methods are complementary: formal grounding where verification tools cover the domain, hybrid consistency training for broader applicability. Think-RM (NeurIPS 2025) shows that deep, long-horizon reasoning inside reward models -- including self-reflection and hypothetical reasoning -- is critical for accurate evaluation, achieving +8% over CoT-GenRMs on RM-Bench. Proof-RM (Feb 2026) provides a scalable pipeline for training reward models on mathematical proof verification with RL stabilization ('LLM-as-a-RM-for-RM'), reaching 82.4% accuracy at 32B on competition-level proofs (IMO/CMO/USAMO), but produces scores rather than formally grounded rationales. Safe (ACL 2025) demonstrates Lean 4 step-level verification of NL math reasoning with the FormalStep benchmark (30,809 formal statements), achieving interpretable verification evidence complementary to PRM scores -- the closest work on formal verification for step-level reasoning, but producing verification states rather than natural-language rationales. FaithCoT-Bench (ICLR 2026) benchmarks CoT faithfulness, finding LLM-as-judge methods achieve 65-77 F1 for detecting unfaithfulness. Faithful Autoformalization (arXiv 2604.25031, Amrollahi et al., Stanford) proposes and quantifies a roundtrip verification mechanism (formalize -> back-translate -> re-formalize -> Z3 equivalence check) achieving 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model performs diagnosis and repair), or up to 91-95% with cross-model diagnosis (Claude performs diagnosis while GPT executes the pipeline) -- the cross-model improvement demonstrates that the diagnosis function is the performance bottleneck, not the pipeline itself. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) finds no systematic gaming in unified generation (Fleiss kappa 0.92) but reveals that DeepSeek-R1 mistranslates premises in two-stage pipelines, producing internally consistent but unfaithful outputs undetectable by LLM-as-judge -- a vulnerability partially addressed by Z3 formal equivalence checks but fundamentally bounded at the NL-to-formal boundary. FormalRewardBench (arXiv 2605.10141, May 2026) shows frontier LLMs achieve only 59.8% pairwise accuracy on formal proof evaluation (Lean 4, MiniF2F problems) while specialized provers achieve only 24.4%, revealing a generation-evaluation gap that motivates using formal tools (not LLMs) as ground truth for rationale grounding. VPRMs (arXiv 2601.17223, Jan 2026) demonstrate that deterministic rule-based step verification dramatically outperforms neural PRMs (87.9% vs 52.4% for GPT-4 on medical evidence synthesis), but are limited to domains with explicit procedural guidelines -- our approach extends this paradigm from rule-based to proof-based verification with stronger mathematical guarantees but narrower initial scope. PRoSFI (arXiv March 2026) uses formal verification as a reward signal during RL training of generators via structured formal intermediaries -- targets generator training, not verifier rationale grounding. HERMES (ICML 2026) interleaves informal reasoning with Lean4-verified proof steps for generators. GroundedPRM (NeurIPS 2025 Workshop) uses MCTS plus tool execution for fidelity-aware supervision with execution-based grounding. MATH-VF (arXiv 2025) combines SymPy+Z3 for step-wise formal verification on MATH-500 and ProcessBench, producing corrective feedback beyond binary labels -- demonstrating that Z3-based step verification can extend to domains beyond GSM8K-level arithmetic. 'Outcome Accuracy is Not Enough' (arXiv Feb 2026) demonstrates approximately 40% rationale consistency with human judgments for frontier GenRMs (specifically 'around 0.4' per the paper), underscoring the need for formal grounding. FormalMATH (arXiv 2025) benchmarks formal theorem proving with 5,560 Lean4 problems showing even the strongest provers achieve only 16.46% success under practical budgets, with pronounced domain bias favoring algebra over calculus/applied math -- grounding our scope restriction to GSM8K-level problems. No existing work connects structured formal proof artifacts to generative PRM rationale training: FoVer provides binary labels without explanations, ThinkPRM/GenPRM/R-PRM provide explanations without formal grounding, Safe provides formal verification states without NL rationales, Proof-RM scores proof quality without rationale generation, R-Align diagnoses spurious correctness without formal remedies, VPRMs use rule-based not proof-based verification, CVPDS uses template-based error injection rather than genuine proof artifact extraction, and 'Outcome Accuracy is Not Enough' improves rationale quality through soft semantic matching rather than deterministic formal grounding.\",\n  \"inspired_by\": \"Field guide Gap 6 (faithfulness of CoT verification rationales in GenRM -- 'never fully resolved'), R-Align's demonstration that substantial GenRM decisions are spuriously correct, R-PRM's demonstration that reasoning-driven evaluation improves accuracy without addressing faithfulness, FormalRewardBench's finding that LLMs cannot reliably evaluate formal proofs (motivating tool-based grounding), and the untried bridge between FoVer's formal proof artifacts and ThinkPRM's rationale generation\",\n  \"approach\": \"We scope our primary contribution to domains where FoVer's formal verification pipeline is validated: GSM8K-level arithmetic (Isabelle) and first-order logic tasks (Z3 on FOLIO/LogicNLI). We evaluate transfer to harder domains as a secondary analysis, with dedicated experiments testing whether formal grounding's faithfulness benefits propagate via the same easy-to-difficult mechanism FoVer demonstrated for accuracy, and whether reduced S-Corr translates to improved downstream policy training.\\n\\nPhase 1 -- Data Preparation and Proof Artifact Extraction (~3-4 weeks engineering). We begin from FoVer-40K, the published balanced training dataset containing 40,000 steps (20K formal logic + 20K theorem proving) at 50% error rate. This yields 20,000 error steps as the base for artifact extraction. Additionally, we augment the base data by re-running FoVer's open-source pipeline on additional problems: FoVer sampled only 10,000 problems per task from much larger source datasets -- FLDx2 contains 100K+ formal logic problems, while MetaMathQA provides 395K math problems. By sampling an additional 10K problems per task and generating solutions from one additional LLM (e.g., Qwen3-8B), we estimate producing ~40K additional error steps at similar error rates (logic ~42%, proof ~14%), yielding a combined pool of ~30K error steps for artifact extraction. We extract artifacts in two tracks: (a) For Z3-verified logic steps, we extract structured counterexamples from SAT results. Z3 natively produces satisfying models when a formula is satisfiable, so for each incorrect step we obtain variable assignments demonstrating the error. This is primarily a parsing and templating task (~1-2 weeks). We estimate ~95% of incorrect logic steps yield extractable counterexamples, since Z3 reliably produces models for SAT results. (b) For Isabelle-verified theorem proving steps, we modify FoVer's Isabelle wrapper to capture proof state information at failure points -- the current goal, available hypotheses, and which tactic failed (~2-3 weeks, requiring deeper Isabelle API integration). We estimate ~60-70% of incorrect steps yield usable proof state artifacts, as some failures occur in preprocessing before meaningful state is available. Pilot validation: we run artifact extraction on a 2K-step sample (1K logic, 1K arithmetic) in week 1 to calibrate yield estimates before full-scale extraction. This pilot also calibrates cross-domain roundtrip equivalence rates (see Phase 2), since math/logic formalization may differ from Amrollahi et al.'s statutory text domain in both directions: math/logic has lower linguistic ambiguity (potentially favoring higher equivalence rates) but higher formalization difficulty for non-trivial steps involving implicit mathematical conventions (potentially favoring lower rates). The pilot's empirical calibration resolves this directional uncertainty before committing to full-scale synthesis.\\n\\nPhase 2 -- Proof-Grounded Rationale Synthesis (~3 weeks). We use Qwen3-32B to synthesize natural-language verification rationales grounded in extracted artifacts. Each rationale template incorporates the specific artifact (e.g., 'Step 3 claims x+y>10, but the counterexample x=3, y=2 shows this fails' for Z3; 'The proof state after step 4 has unsolved goal involving P(n+1), but the applied tactic only handles the base case' for Isabelle). We apply roundtrip consistency filtering adapted from Amrollahi et al. (2604.25031): each generated rationale is re-formalized and checked for Z3/Isabelle semantic equivalence with the original artifact. Amrollahi et al. report 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model) or 91-95% with cross-model diagnosis (a separate LLM performs only the diagnosis step while the primary model executes the pipeline). We implement standard same-model diagnosis-guided repair using Qwen3-32B as both diagnostician and pipeline executor, following their finding that scoped stage-level diagnosis outperforms random-stage repair. We do not implement cross-model diagnosis in the initial pipeline to avoid the additional complexity and cost of routing diagnosis through a separate LLM, but note it as an available improvement lever if standard repair yields insufficient throughput. Given the directional uncertainty in cross-domain transfer (math/logic vs. statutory text), we conservatively estimate 50-65% baseline pass rate on our domains, improvable to 70-85% with standard diagnosis-guided repair. The Phase 1 pilot on 2K steps will empirically calibrate these estimates before full-scale synthesis. Data yield estimate with two scenarios:\\n\\n  Scenario A (FoVer-40K only, conservative): Starting from ~20K error steps -> ~16K with extractable artifacts (9.5K Z3 at 95% + 6.5K Isabelle at 65%) -> ~11.2-13.6K after roundtrip+repair filtering at ~70-85% -> ~9.5-11.6K after ~15% final quality filtering. Final: ~9-12K proof-grounded rationales.\\n\\n  Scenario B (FoVer-40K + augmented pipeline): Starting from ~30K error steps -> ~24K with extractable artifacts (15K Z3 + 9K Isabelle) -> ~16.8-20.4K after roundtrip filtering -> ~14.3-17.3K after quality filtering. Final: ~14-17K proof-grounded rationales.\\n\\n  Data sufficiency argument: ThinkPRM achieves competitive performance with only 1K synthetic verification CoTs (~8K step labels), GenPRM uses 23K training examples, and R-PRM uses ~289K SFT samples but achieves comparable performance to Qwen2.5-Math-PRM with only ~15% of its data. Our conservative Scenario A of ~9-12K formally grounded rationales represents ~10x ThinkPRM's training data and is comparable to GenPRM's scale. Moreover, our rationales carry richer supervision signal than any of these: each rationale is traceable to a specific formal proof artifact with verified semantic grounding, whereas ThinkPRM's rationales are filtered only on label match, GenPRM's use execution-based but not proof-based verification, and R-PRM's are bootstrapped from LLM-generated seed data without formal grounding. We thus expect higher per-example training signal quality, partially compensating for any quantity gap.\\n\\nPhase 3 -- SFT Training (~2 weeks). We fine-tune Qwen3-14B (or DeepSeek-R1-Distill-Qwen-14B) as a generative PRM on the proof-grounded rationales following ThinkPRM's SFT recipe. We train separate models on Z3-grounded logic rationales, Isabelle-grounded arithmetic rationales, and the combined set to enable ablation of each grounding source's contribution.\\n\\nPhase 4 -- Evaluation (~3-4 weeks). Verification accuracy is evaluated on: (primary) ProcessBench-GSM8K subset, FOLIO, LogicNLI; (transfer) ProcessBench-MATH/Olympiad subsets, MATH-500 best-of-N; targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N scores as baselines. Rationale faithfulness is assessed via three independent metrics, strictly separated from training: (1) R-Align's Spurious Correctness (S-Corr) as the primary automated faithfulness metric, computed by comparing rationale reasoning against golden reference judgments from ProcessBench annotations; (2) FaithCoT-Bench detection metrics (precision, recall, F1); (3) human evaluation on 150-200 randomly sampled rationales, rating formal grounding quality and error identification accuracy. Roundtrip consistency is reported ONLY as a supplementary training-data-quality indicator and correlation analysis (does higher roundtrip score predict higher human-rated quality?), not as a primary evaluation metric or novel contribution.\\n\\nCritically, Phase 4 includes two dedicated experiments that go beyond standard PRM evaluation:\\n\\n(A) Faithfulness transfer experiment. We measure S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for: (a) our formally grounded model trained only on GSM8K-level/FOL rationales; (b) ThinkPRM-14B baseline; (c) GenPRM-7B baseline; (d) R-PRM-7B-DPO baseline (the strongest reasoning-based PRM without formal grounding -- testing whether rich reasoning analyses alone reduce S-Corr); (e) an ablation model trained on FoVer-40K binary labels (no formal rationale grounding). This experiment disentangles four claims: (i) does formal grounding reduce S-Corr on in-domain tasks (GSM8K, FOL)? (ii) does the S-Corr reduction transfer to harder domains (MATH, Olympiad) via the same easy-to-difficult mechanism FoVer demonstrated for accuracy? (iii) does the transfer specifically require rationale-level formal grounding, or does any FoVer-derived training signal suffice? (iv) does R-PRM's reasoning-driven evaluation reduce S-Corr relative to simpler baselines -- isolating whether accuracy-improving reasoning also improves faithfulness, or whether formal grounding provides an orthogonal faithfulness benefit? If (i) holds but (ii) doesn't, we still demonstrate improved faithfulness within the validated scope. If both hold, we provide the first empirical evidence that formal rationale grounding at the foundational training-data level propagates to harder reasoning tasks.\\n\\n(B) Downstream policy experiment. To close the full causal chain (formal grounding -> reduced S-Corr -> better downstream policy), we conduct a small-scale rejection sampling experiment. We generate N=8 candidate solutions per problem for 500 GSM8K and 500 MATH problems using Qwen2.5-Math-1.5B-Instruct as the policy model, then select the best response according to each PRM: (a) our formally grounded PRM; (b) ThinkPRM-14B; (c) R-PRM-7B-DPO; (d) FoVer-trained discriminative PRM (binary labels). We report pass@1 accuracy of the selected solutions (best-of-N evaluation) and, as a stronger test, perform rejection sampling fine-tuning (RFT): we fine-tune Qwen2.5-Math-1.5B on the top-ranked solutions selected by each PRM (filtering to solutions verified as correct), then evaluate the resulting policy models on held-out MATH-500 and GSM8K test sets. R-Align demonstrates that S-Corr predicts RLHF policy degeneration (as established in the paper's experimental analysis); our experiment directly tests whether formally grounded rationale selection -- by reducing spurious correctness in the reward signal -- yields better-trained policies. This is a modest-cost experiment (~50-80 GPU hours for generation + RFT on 1.5B model) that could provide the strongest possible impact argument. Even a 1-2 point accuracy improvement on MATH-500 pass@1 via formally grounded selection would validate the full pipeline.\\n\\nImpact beyond easy domains: Three arguments justify the broader significance of improving rationale faithfulness on GSM8K-level and FOL tasks. (1) Training-data origin: GSM8K-level problems are the primary source for PRM training data construction (PRM800K, FoVer, OmegaPRM's 1.5M annotations all derive from or include GSM8K/MATH). Improving the faithfulness of rationales at this foundational level improves the training signal for all downstream applications. (2) Transfer prediction: R-Align demonstrates that S-Corr on evaluation benchmarks predicts policy degeneration during RLHF (as established in the paper's experimental analysis), and FoVer demonstrates easy-to-difficult accuracy transfer -- PRMs trained on GSM8K-level data improve verification on MATH (88.0% vs 78.2%), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%). Our faithfulness transfer experiment (above) directly tests whether reducing S-Corr at the source level propagates via the same mechanism, transforming this from a theoretical chain to empirical evidence. (3) Methodology contribution: The proof-artifact-to-rationale bridge is a general technique independent of problem difficulty. Initial validation on computationally tractable domains is standard practice -- FoVer itself started with GSM8K-level validation before demonstrating broad transfer, and CVPDS (arXiv 2605.02395) similarly validates on logical reasoning before testing mathematical transfer. As formal verification tools extend to harder domains (e.g., Lean 4 integration via Safe's autoformalization pipeline, or SymPy+Z3 via MATH-VF), the same methodology applies directly.\\n\\nAcknowledged Limitations and Mitigations. (1) Scope: FoVer's formal verification is validated on GSM8K-level arithmetic and FOL logic. Extending to competition math faces fundamental barriers -- Z3 is undecidable for nonlinear integer arithmetic (confirmed by 'SMT and Functional Equation Solving over the Reals,' 2025), and FormalMATH shows only 16.46% LLM prover success on Lean4 problems. MATH-500 and GPQA-Diamond are explicitly positioned as stretch goals requiring future formalization extensions: specifically, Lean 4 integration (via Safe's autoformalization pipeline) for algebraic reasoning, or SymPy+Z3 (via MATH-VF's approach) for computational verification. (2) Gaming vulnerability: Kim et al. (2604.19459) show two-stage formalization pipelines are vulnerable to premise mistranslation. Our Z3 formal equivalence check provides stronger detection than LLM-as-judge for axiom-fabrication-type errors (would catch GPT-5's 107 fabricated axioms in their study), but cannot fully guard against symmetric mistranslation at the NL-to-formal boundary. We mitigate via: (a) roundtrip verification from Amrollahi et al., which catches asymmetric errors; (b) NLI-based drift analysis as a secondary signal; (c) restricting to domains (FOL, arithmetic) where formalization ambiguity is lower than natural language. (3) FormalRewardBench shows even frontier LLMs achieve only 59.8% on formal proof evaluation, but our approach uses formal verification tools (Z3, Isabelle) as ground truth rather than LLMs as proof evaluators, sidestepping the generation-evaluation gap within Z3/Isabelle's decidable scope. (4) Cross-domain roundtrip uncertainty: Amrollahi et al.'s roundtrip equivalence rates were measured on statutory text, while our pipeline operates on math/logic formalization. These domains may differ in opposing ways: math/logic has lower linguistic ambiguity and more standardized notation (potentially yielding higher equivalence rates), but non-trivial mathematical steps involve implicit conventions and multi-step dependencies that may resist clean formalization (potentially yielding lower rates). Our Phase 1 pilot validation on 2K steps is specifically designed to calibrate this cross-domain transfer before committing to full-scale synthesis, and we report pilot equivalence rates alongside Amrollahi et al.'s statutory text rates to enable direct comparison. (5) Complementarity with non-formal approaches: 'Outcome Accuracy is Not Enough' (Qwen team, 2602.04649) achieves strong rationale quality improvements through soft semantic matching against human annotations without formal grounding. Our approach provides stronger guarantees (deterministic formal traceability) within a narrower scope; their approach provides broader coverage (any domain with annotations) with softer guarantees. Future work should explore combining formal grounding for in-scope domains with hybrid consistency training for broader coverage. (6) Relationship to concurrent data synthesis work: CVPDS (arXiv 2605.02395) provides an alternative approach to generating verified PRM training data through template-based error injection. While methodologically distinct from proof-artifact extraction, both approaches aim to improve PRM training data quality through formal/symbolic verification. Our approaches are complementary: CVPDS offers controllable error diversity but is constrained by predefined templates, while our method extracts artifacts from naturally occurring LLM errors but requires successful formal verification. Combining controlled error injection with proof-artifact rationale grounding is a promising future direction.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"500-700 (solution generation for augmented data ~80h, rationale synthesis with Qwen3-32B ~120h, SFT on 14B model 4xA100 ~100h, evaluation including faithfulness transfer experiment ~100h, downstream policy experiment ~60h, ablations ~90h)\",\n      \"engineering_time\": \"Z3 counterexample parsing: ~1-2 weeks; Isabelle proof state extraction: ~2-3 weeks; augmented data generation: ~1 week; roundtrip filter + diagnosis repair: ~1 week; downstream RFT pipeline: ~0.5 weeks; integration/testing: ~1 week. Total: 6-8 weeks engineering.\",\n      \"timeline\": \"15-19 weeks\",\n      \"estimated_gpu_cost\": \"$1000-1700 (A100 80GB at ~$2.00/hr on Vast.ai/Spheron)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"500-700 (irreducible training/inference costs unchanged)\",\n      \"engineering_time\": \"3-5 weeks (Claude accelerates Z3 parsing code, Isabelle wrapper modifications, rationale template design, augmented data pipeline, evaluation harness, RFT pipeline)\",\n      \"timeline\": \"11-15 weeks\",\n      \"claude_api_cost\": \"$500-800 (Sonnet 4.6 for pipeline code generation and data analysis, ~100-200M tokens)\",\n      \"estimated_gpu_cost\": \"$1000-1700\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"550-750 (slightly higher from automated ablation sweeps, augmented data generation, faithfulness transfer experiment, downstream policy experiment, and pilot experiments)\",\n      \"engineering_time\": \"2-3 weeks (Claude handles most Z3/Isabelle parsing engineering)\",\n      \"timeline\": \"8-11 weeks\",\n      \"claude_api_cost\": \"$1500-2500 (Sonnet 4.6 for end-to-end pipeline orchestration, rationale quality filtering, iterative ablation design, ~400-700M tokens)\",\n      \"estimated_gpu_cost\": \"$1100-1800\",\n      \"speed_bottleneck\": \"Isabelle proof state extraction engineering (~2-3 weeks irreducible due to Isabelle API complexity); Z3 counterexample extraction is faster (~1-2 weeks). Formal verification throughput (~2-10s per Z3 step, 15-60s per Isabelle step) is parallelizable across CPU cores. Augmented data generation adds ~1 week for solution generation and verification. Downstream RFT experiment is fast (~50-80h GPU) but depends on Phase 3 model completion.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (projected abstracts Sep 19, full papers Sep 24, 2026 -- 17 weeks; projected from ICLR 2026 pattern, official CFP not yet published as of May 2026; comfortable for human_in_loop and auto_research timelines)\",\n    \"ARR October 2026 cycle -> commitment to NAACL 2027 or ACL 2027 (comfortable backup NLP venue)\",\n    \"AAAI 2027 (abstracts Jul 21, full papers Jul 28, 2026 -- 8 weeks from today, feasible only with auto_research timeline and Z3-only scoped initial submission)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Process Reward Models That Think (arXiv 2025, ThinkPRM)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, She et al.)\",\n    \"Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, FoVer)\",\n    \"Controllable and Verifiable Process Data Synthesis for Process Reward Models (arXiv 2605.02395, May 2026, Chi & Wang)\",\n    \"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026)\",\n    \"RM-R1: Reward Modeling as Reasoning (ICLR 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026, Amrollahi et al.)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 @ ICLR 2026, Kim et al.)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2605.10141, May 2026)\",\n    \"Beyond Outcome Verification: Verifiable Process Reward Models (arXiv 2601.17223, Jan 2026, VPRMs)\",\n    \"Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)\",\n    \"R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging (arXiv Feb 2026)\",\n    \"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models (NeurIPS 2025)\",\n    \"Proof-RM: A Scalable and Generalizable Reward Model for Math Proof (arXiv Feb 2026)\",\n    \"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)\",\n    \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026, PRoSFI)\",\n    \"Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models (arXiv 2602.04649, Feb 2026, Qwen team)\",\n    \"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2025, MATH-VF)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of LLMs (arXiv 2025)\",\n    \"Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024, OmegaPRM)\",\n    \"GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling (NeurIPS 2025 Workshop)\"\n  ],\n  \"description\": \"We propose Proof-Grounded Generative PRMs, the first process reward models whose verification rationales are traceable to structured formal proof artifacts. Current generative PRMs (ThinkPRM, GenPRM, R-PRM, RM-R1) produce chain-of-thought verification rationales trained on synthetic data of unknown faithfulness -- R-Align shows GenRM decisions exhibit substantial spurious correctness (right label, wrong reasoning), and frontier GenRMs achieve only approximately 40% rationale consistency with human judgments. R-PRM (EMNLP 2025) demonstrates that reasoning-driven evaluation substantially improves PRM accuracy (70.4 F1 on ProcessBench, +13.9 over baselines), but its multi-dimensional analyses are trained on LLM-bootstrapped data and rationale faithfulness is not evaluated. Separately, FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can produce accurate step-level error labels transferring across 12 benchmarks, but generates only binary labels and explicitly excludes reasoning-based PRMs. A concurrent approach (CVPDS, arXiv 2605.02395) synthesizes PRM data through template-based symbolic error injection across 11 error types with 20K instances, but targets accuracy through controlled error diversity rather than rationale faithfulness through proof-artifact grounding. A non-formal approach ('Outcome Accuracy is Not Enough,' Qwen team) improves rationale quality through hybrid consistency-outcome training via soft semantic matching against human annotations, achieving RM-Bench 87.1% (+5% over baselines) -- but relies on human annotation availability and provides softer guarantees than formal artifact tracing. We bridge the formal gap by: (1) extending FoVer's Z3 pipeline to extract structured counterexamples from SAT results and modifying its Isabelle wrapper to capture proof state information at failure points -- going beyond binary labels to structured artifacts (~3-4 weeks engineering, with pilot validation on 2K steps to calibrate both yield and cross-domain roundtrip equivalence rates); (2) synthesizing verification rationales grounded in these artifacts using Qwen3-32B, with roundtrip consistency filtering adapted from Amrollahi et al.'s (2604.25031) validated mechanism (45-66% baseline equivalence, 78-86% with standard diagnosis-guided repair, up to 91-95% with cross-model diagnosis; we implement standard same-model repair and conservatively estimate 70-85% post-repair rates on math/logic given cross-domain uncertainty); (3) fine-tuning Qwen3-14B as a generative PRM on these rationales. Starting from FoVer-40K's 20K error steps, we estimate ~9-12K proof-grounded rationales (Scenario A); augmenting FoVer's pipeline with additional problems from the much larger source datasets yields ~14-17K (Scenario B). Both scenarios exceed ThinkPRM's training data (1K rationales / 8K step labels) by an order of magnitude, and our rationales carry richer per-example signal via formal artifact tracing. We scope primary evaluation to domains where FoVer is validated -- GSM8K-level arithmetic and FOL logic (FOLIO, LogicNLI) -- targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N as baselines. Rationale faithfulness is assessed via R-Align's Spurious Correctness metric and FaithCoT-Bench as primary measures, plus human evaluation on 150-200 examples, with roundtrip consistency strictly demoted to a supplementary training-quality indicator. We include two dedicated experiments beyond standard PRM evaluation: (A) a faithfulness transfer experiment measuring S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for our GSM8K-trained model versus baselines (including R-PRM-7B-DPO, the strongest reasoning-based baseline without formal grounding) and a binary-label ablation, directly testing whether formal rationale grounding propagates faithfulness improvements to harder domains; (B) a downstream policy experiment conducting rejection sampling fine-tuning of Qwen2.5-Math-1.5B using solutions selected by each PRM on 500 GSM8K + 500 MATH problems, testing whether reduced S-Corr from formally grounded rationales translates to improved policy training -- closing the full causal chain from formal grounding to downstream impact that R-Align's S-Corr-to-RLHF correlation predicts. We argue broader impact via three mechanisms: (a) GSM8K-level is the origin of most PRM training data; (b) FoVer demonstrates easy-to-difficult accuracy transfer (MATH: 88.0% vs 78.2%, Olympiad: 84.0% vs 76.2%) and R-Align shows S-Corr predicts RLHF degeneration; (c) the proof-artifact-to-rationale methodology is domain-independent. We acknowledge scope limitations (Z3 undecidability for nonlinear arithmetic; FormalMATH's 16.46% prover success), gaming vulnerabilities in two-stage pipelines (Kim et al.), cross-domain roundtrip uncertainty (math/logic may differ from statutory text in both directions), complementarity with both non-formal approaches (Qwen team's hybrid training) and concurrent data synthesis methods (CVPDS's template-based error injection).\",\n  \"project_name\": \"proof_grounded_genprm\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"issue_1_faithful_autoformalization_numbers\": \"ADDRESSED (MODERATE, round 4). Corrected landscape statement from '85-95% with diagnosis-guided repair' to precise numbers verified from Table 1, Section 7.1 of Amrollahi et al.: standard diagnosis-guided repair (same model) achieves 77.9%-85.7% equivalence, while cross-model diagnosis (Claude performs diagnosis, GPT executes pipeline) achieves 90.7%-94.7%. All instances updated throughout.\",\n    \"issue_2_hybrid_training_positioning\": \"ADDRESSED (MODERATE, round 4). Added 'Outcome Accuracy is Not Enough' (Qwen team, arXiv 2602.04649) to the landscape with detailed positioning as complementary non-formal approach.\",\n    \"issue_3_faithfulness_transfer_experiment\": \"ADDRESSED (MINOR, round 4). Added dedicated faithfulness transfer experiment to Phase 4 with four-way comparison and ablation.\",\n    \"issue_4_crossdomain_roundtrip_uncertainty\": \"ADDRESSED (MINOR, round 4). Added explicit acknowledgment of cross-domain uncertainty with pilot calibration strategy.\",\n    \"issue_5_rprm_baseline\": \"ADDRESSED (MODERATE, round 5). Added R-PRM (EMNLP 2025, She et al.) comprehensively to the landscape with detailed methodology and results: reasoning-driven multi-dimensional step analysis (Previous Steps, Now Step, Data Source, Consistency, Calculation Analysis), R-PRM-7B-DPO achieving 70.4 F1 on ProcessBench (+13.9 over baselines), +8.5 F1 on PRMBench, +8.6 accuracy on downstream math reasoning. Positioned as the strongest reasoning-based PRM baseline that demonstrates the ceiling of accuracy-focused reasoning without formal grounding -- rich analyses but untested faithfulness. R-PRM sharpens our value proposition: if reasoning-driven evaluation already provides substantial accuracy gains, formal grounding must provide ADDITIONAL benefits, specifically traceable rationale faithfulness rather than just accuracy. Added R-PRM-7B-DPO as a baseline in both the faithfulness transfer experiment (testing whether reasoning-driven analysis alone reduces S-Corr, adding a fourth claim to disentangle) and the accuracy evaluation (targeting its 70.4 F1). Updated core_problem, opportunity, gap analysis, data sufficiency argument, and evaluation baselines accordingly.\",\n    \"issue_6_cvpds_concurrent_work\": \"ADDRESSED (MODERATE, round 5). Added 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) to the landscape with detailed methodology: four-stage pipeline (correct chain synthesis from rule templates, template-aware error injection across 11 error types, symbolic recomputation for trajectory consistency, prefix non-derivability verification), 20K instances, best-of-8 results (Llama-3.1-8B: 0.528->0.591, Qwen-2.5-7B: 0.567->0.615), limited math transfer (ProcessBench GSM8K: 21.2% F1). Key distinction clearly articulated: CVPDS generates controlled synthetic errors through template-based injection for accuracy-focused PRM training; our approach extracts genuine proof artifacts from naturally occurring LLM errors for faithfulness-focused rationale grounding. Their error diversity is template-constrained (acknowledged limitation); our artifacts reflect actual LLM error distributions. Positioned as complementary -- combining controlled error injection with proof-artifact grounding noted as future direction. Added to gap analysis and new limitation (6).\",\n    \"issue_7_downstream_rlhf_experiment\": \"ADDRESSED (MINOR, round 5). Added Phase 4(B) downstream policy experiment: best-of-N selection + rejection sampling fine-tuning (RFT) of Qwen2.5-Math-1.5B using solutions selected by each PRM (our formally grounded PRM, ThinkPRM-14B, R-PRM-7B-DPO, FoVer discriminative PRM). Generates N=8 candidates per problem for 500 GSM8K + 500 MATH problems, selects best via each PRM, fine-tunes 1.5B policy on correct selected solutions, evaluates on held-out test sets. This closes the full causal chain: formal grounding -> reduced S-Corr -> better policy training. Modest cost (~50-80 GPU hours) for potentially the strongest impact argument. Resource estimates updated to include this experiment (GPU hours increased by ~50-80h across all tiers, engineering time increased by ~0.5 weeks).\",\n    \"issue_8_iclr2027_deadline_tentative\": \"ADDRESSED (MINOR, round 5). ICLR 2027 deadline now explicitly noted as 'projected from ICLR 2026 pattern, official CFP not yet published as of May 2026' in target venues.\",\n    \"issue_9_ralign_claims_clarification\": \"ADDRESSED (MINOR, round 5). R-Align description now distinguishes between abstract-level claims ('substantial S-Corr even for competitive GenRMs') and full-paper experimental details ('specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract'). All references to R-Align's RLHF prediction now use 'as established in the paper's experimental analysis' rather than implying the specific evidence comes from the abstract.\"\n  }\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"MINOR: R-PRM baseline F1 misquoted as 58.5 throughout the proposal; the published EMNLP version and GitHub results table show Qwen2.5-Math-7B-PRM800K achieves 56.5 F1 (not 58.5), consistent with 70.4 - 56.5 = +13.9 improvement. The improvement claim (+13.9) and the R-PRM-7B-DPO score (70.4) are correct, but the baseline number needs correction from 58.5 to 56.5.\", \"MINOR: StepProof (arXiv 2506.10558) performs step-by-step Isabelle-based autoformalization and verification on GSM8K — operating in exactly the domain and tool setting of this proposal. While it targets proof autoformalization rather than PRM rationale training, it provides relevant engineering insights for Isabelle proof state handling and should be acknowledged.\", \"MINOR: 'Learning to Disprove: Formal Counterexample Generation with Large Language Models' (arXiv 2603.19514, March 2026) trains LLMs to generate formal counterexamples verified in Lean 4 via a symbolic mutation strategy. While using Lean 4 rather than Z3/Isabelle, the conceptual parallel of using formal counterexamples as training signals is relevant and demonstrates scalable counterexample generation.\", \"STRUCTURAL: The average score (3.75) is below the 4.0 threshold primarily due to the inherent scope limitation — formal grounding is validated only on easy domains where its practical value is lower, while the harder domains where it would be most impactful are beyond current formalization capabilities. This is honestly acknowledged but remains the fundamental barrier to a higher impact score.\"]\nFeedback: The proposal has matured significantly through 6 rounds — all critical issues from rounds 1-4 are fully resolved, and the landscape is now best-in-class for this area. Three minor fixes remain:\n\n(1) CORRECT THE R-PRM BASELINE: Change 'Qwen2.5-Math-7B-PRM800K at 58.5 F1' to '56.5 F1' throughout. The published EMNLP version and GitHub table confirm: R-PRM-7B-DPO 70.4 - Qwen2.5-Math-7B-PRM800K 56.5 = +13.9 F1. Your improvement claim is correct; only the baseline number needs updating.\n\n(2) ACKNOWLEDGE StepProof and 'Learning to Disprove': StepProof operates in your exact domain (step-by-step Isabelle verification on GSM8K) and provides relevant engineering precedent. 'Learning to Disprove' demonstrates formal counterexample generation at scale. Neither threatens novelty but both inform feasibility.\n\n(3) IMPACT CEILING: The fundamental challenge is that the average score (3.75) is dragged below 4.0 by impact (3.5) and feasibility (3.5), both constrained by the scope limitation. To potentially push impact higher, consider strengthening the argument that GSM8K/FOL-level formal grounding is inherently valuable BEYOND transfer — e.g., for safety-critical applications where traceable error explanations are required regardless of domain difficulty, or for PRM interpretability/debugging where understanding WHY a step is wrong matters more than just detecting it. The 'training data origin' argument is your strongest impact lever — consider making it more central.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 6 轮修订，近 3 轮平均分从 3.9 到 3.8，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T20:23:32.233Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T20:23:32.233Z",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

## Round 1

31 recorded events

### User

_source line 3 · 2026-05-27T20:23:32.274Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "title": "Formally Grounded Faithful Rationales for Generative PRMs",
  "core_problem": "Generative PRMs (ThinkPRM, GenPRM, R-PRM) produce CoT verification rationales, but R-Align (Feb 2026) shows existing GenRMs exhibit substantial Spurious Correctness -- label-correct decisions with misaligned rationales -- and 'Outcome Accuracy is Not Enough' finds approximately 40% rationale consistency with human judgments. R-PRM demonstrates that reasoning-driven evaluation substantially improves accuracy (+13.9 F1 on ProcessBench), yet even rich multi-dimensional reasoning analyses lack formal grounding and have unknown faithfulness. Can we train generative verifiers whose rationales are grounded in structured formal proof artifacts, reducing spurious correctness and producing the first PRMs with formally traceable error explanations?",
  "opportunity": "GenRM reviewer 3 raised the unresolved concern that CoT rationales may be 'plausible-sounding but unfaithful reasoning that happens to correlate with correct verdicts.' FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can generate step-level error labels transferring across 12 benchmarks, but FoVer explicitly restricts to classification-based PRMs producing only binary labels, excluding generative/reasoning-based PRMs. R-PRM (EMNLP 2025) shows that reasoning-driven step evaluation -- generating multi-dimensional analyses before judgments -- substantially improves PRM accuracy (+13.9 F1 on ProcessBench via DPO), but its rationales are trained on LLM-generated seed data without formal grounding and faithfulness is not evaluated. ThinkPRM generates rich verification CoTs but trains on synthetic rationales of unknown faithfulness. The untried bridge is extracting structured proof artifacts -- Z3 counterexamples, Isabelle proof state information -- from FoVer's verification pipeline and using them as grounding signals for ThinkPRM-style rationale generation. This fills the gap that reasoning-driven methods (R-PRM, ThinkPRM, GenPRM) leave open: not just whether the PRM gets the label right, but whether its explanation is formally traceable to the actual mathematical error. Critically, Faithful Autoformalization (Amrollahi et al., April 2026) has now validated and quantified the roundtrip verification mechanism we adopt for quality filtering, showing 45-66% baseline equivalence rates improvable to 78-86% with standard diagnosis-guided repair or up to 91-95% with cross-model diagnosis -- providing empirical grounding for our data pipeline feasibility. Moreover, FoVer itself demonstrates easy-to-difficult transfer: PRMs trained on GSM8K-level data significantly improve step-level verification on MATH (88.0% vs 78.2% baseline), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%), suggesting that improving rationale faithfulness on foundational domains propagates to harder reasoning tasks.",
  "landscape": "ThinkPRM (arXiv 2025) achieves 8% improvement on GPQA-Diamond over discriminative verifiers using only 1% of PRM800K labels (specifically 1K synthetic verification CoTs filtered to ~8K step labels), but its rationales lack formal grounding. GenPRM (AAAI 2026) combines CoT with code verification, enabling 1.5B models to outperform GPT-4o on ProcessBench using only 23K training examples. R-PRM (EMNLP 2025) introduces reasoning-driven process reward modeling: it generates multi-dimensional step analyses (Previous Steps Analysis, Now Step Analysis, Data Source Analysis, Consistency Analysis, Calculation Analysis) followed by binary judgments. Using Qwen2.5-Math-7B-Instruct as the base model, R-PRM-7B-DPO achieves 70.4 F1 on ProcessBench (+13.9 over Qwen2.5-Math-7B-PRM800K at 58.5 F1) and +8.5 F1 on PRMBench, with consistent +8.6 accuracy improvements on six downstream math reasoning datasets via best-of-N selection. R-PRM trains on ~289K SFT samples and ~269K DPO pairs bootstrapped from PRM800K annotations, achieving comparable performance to Qwen2.5-Math-PRM with only ~15% of its data volume. Critically, while R-PRM produces rich natural-language reasoning for each step evaluation, it does not evaluate rationale faithfulness -- the analyses are trained on LLM-generated seed data and may exhibit the same spurious correctness that R-Align identifies in other GenRMs. R-PRM demonstrates the ceiling of what reasoning-driven evaluation achieves without formal grounding: substantial accuracy gains, but with unknown rationale fidelity to the actual mathematical errors. FoVer (ACL 2026 Findings) uses Z3/Isabelle for automated step-level labeling with easy-to-difficult transfer (trained on GSM8K-level, evaluates on MATH/AIME/Olympiad), but produces only binary labels and explicitly excludes reasoning-based PRMs citing 'substantially higher computational costs.' FoVer-40K contains 40,000 balanced training steps (20K formal logic from FLDx2 + 20K theorem proving from GSM8K-level problems) with 50% error rate, generated from solutions by Llama 3.1 8B and Qwen 2.5 7B; the raw unbalanced pipeline output is substantially larger (~216K steps from 10K problems per task across both models). 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) is concurrent work that synthesizes PRM training data through a four-stage pipeline: constructing correct symbolic reasoning chains from rule templates, injecting template-aware errors into intermediate steps, symbolically recomputing subsequent steps to maintain trajectory consistency, and verifying that injected errors are not derivable from the prefix. They produce 20K paired (correct, erroneous) trajectories across 11 error types (7 truth-state: drop_condition, implication_misuse, or_and_confusion, partial_evaluation, xor_as_or, xor_as_equiv, vacuous_truth_error; 4 structural: converse_error, redundant_step, missing_prerequisite, circular_reference), translated into natural-language processes for PRM training. Their method improves best-of-8 reranking on logical reasoning benchmarks (Llama-3.1-8B: 0.528 -> 0.591, Qwen-2.5-7B: 0.567 -> 0.615 average F1), with limited transfer to mathematics (ProcessBench GSM8K: 21.2% F1). The key methodological distinction from our work: they generate controlled synthetic errors through template-based injection for accuracy-focused PRM training, while we extract genuine proof artifacts from naturally occurring errors in LLM solutions for faithfulness-focused rationale grounding. Their error diversity is constrained by predefined templates (an acknowledged limitation), while our artifacts reflect the actual distribution of errors that LLMs make. The two approaches are complementary -- their controlled error injection could extend the diversity of training scenarios, while our proof-artifact extraction provides traceable explanations of why each error is wrong. RM-R1 (ICLR 2026) trains reasoning reward models with explicit rationale chains but without formal grounding. R-Align (Feb 2026) introduces the Spurious Correctness (S-Corr) metric showing existing GenRMs exhibit substantial spuriously correct decisions (the abstract reports 'substantial S-Corr even for competitive GenRMs'; specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract), providing the key diagnostic our work aims to improve. 'Outcome Accuracy is Not Enough' (Qwen team, Feb 2026, arXiv 2602.04649) introduces a competing non-formal approach to improving rationale quality: they define Rationale Consistency via MetaJudge, which decomposes human rationales into atomic claims and performs strict one-to-one semantic matching against model justifications, finding frontier GenRMs achieve only ~40% rationale consistency. They train with a multiplicative hybrid signal R_final = R_rationale * R_outcome via GRPO, achieving RM-Bench 87.1% and JudgeBench 82.0% (+5% over outcome-only baselines, +7% on Arena Hard v2 creative writing during RLHF). Crucially, their approach targets Judge faithfulness (evaluation rationale quality) rather than Solver verification, and relies on soft semantic matching against human annotations -- providing broader applicability but weaker guarantees than formal artifact tracing. Their acknowledged limitation is scalability: computing rationale consistency still requires high-quality human annotations. Our formal grounding provides deterministic, traceable guarantees within Z3/Isabelle's decidable scope, while their approach extends to any domain with human annotations. The two methods are complementary: formal grounding where verification tools cover the domain, hybrid consistency training for broader applicability. Think-RM (NeurIPS 2025) shows that deep, long-horizon reasoning inside reward models -- including self-reflection and hypothetical reasoning -- is critical for accurate evaluation, achieving +8% over CoT-GenRMs on RM-Bench. Proof-RM (Feb 2026) provides a scalable pipeline for training reward models on mathematical proof verification with RL stabilization ('LLM-as-a-RM-for-RM'), reaching 82.4% accuracy at 32B on competition-level proofs (IMO/CMO/USAMO), but produces scores rather than formally grounded rationales. Safe (ACL 2025) demonstrates Lean 4 step-level verification of NL math reasoning with the FormalStep benchmark (30,809 formal statements), achieving interpretable verification evidence complementary to PRM scores -- the closest work on formal verification for step-level reasoning, but producing verification states rather than natural-language rationales. FaithCoT-Bench (ICLR 2026) benchmarks CoT faithfulness, finding LLM-as-judge methods achieve 65-77 F1 for detecting unfaithfulness. Faithful Autoformalization (arXiv 2604.25031, Amrollahi et al., Stanford) proposes and quantifies a roundtrip verification mechanism (formalize -> back-translate -> re-formalize -> Z3 equivalence check) achieving 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model performs diagnosis and repair), or up to 91-95% with cross-model diagnosis (Claude performs diagnosis while GPT executes the pipeline) -- the cross-model improvement demonstrates that the diagnosis function is the performance bottleneck, not the pipeline itself. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) finds no systematic gaming in unified generation (Fleiss kappa 0.92) but reveals that DeepSeek-R1 mistranslates premises in two-stage pipelines, producing internally consistent but unfaithful outputs undetectable by LLM-as-judge -- a vulnerability partially addressed by Z3 formal equivalence checks but fundamentally bounded at the NL-to-formal boundary. FormalRewardBench (arXiv 2605.10141, May 2026) shows frontier LLMs achieve only 59.8% pairwise accuracy on formal proof evaluation (Lean 4, MiniF2F problems) while specialized provers achieve only 24.4%, revealing a generation-evaluation gap that motivates using formal tools (not LLMs) as ground truth for rationale grounding. VPRMs (arXiv 2601.17223, Jan 2026) demonstrate that deterministic rule-based step verification dramatically outperforms neural PRMs (87.9% vs 52.4% for GPT-4 on medical evidence synthesis), but are limited to domains with explicit procedural guidelines -- our approach extends this paradigm from rule-based to proof-based verification with stronger mathematical guarantees but narrower initial scope. PRoSFI (arXiv March 2026) uses formal verification as a reward signal during RL training of generators via structured formal intermediaries -- targets generator training, not verifier rationale grounding. HERMES (ICML 2026) interleaves informal reasoning with Lean4-verified proof steps for generators. GroundedPRM (NeurIPS 2025 Workshop) uses MCTS plus tool execution for fidelity-aware supervision with execution-based grounding. MATH-VF (arXiv 2025) combines SymPy+Z3 for step-wise formal verification on MATH-500 and ProcessBench, producing corrective feedback beyond binary labels -- demonstrating that Z3-based step verification can extend to domains beyond GSM8K-level arithmetic. 'Outcome Accuracy is Not Enough' (arXiv Feb 2026) demonstrates approximately 40% rationale consistency with human judgments for frontier GenRMs (specifically 'around 0.4' per the paper), underscoring the need for formal grounding. FormalMATH (arXiv 2025) benchmarks formal theorem proving with 5,560 Lean4 problems showing even the strongest provers achieve only 16.46% success under practical budgets, with pronounced domain bias favoring algebra over calculus/applied math -- grounding our scope restriction to GSM8K-level problems. No existing work connects structured formal proof artifacts to generative PRM rationale training: FoVer provides binary labels without explanations, ThinkPRM/GenPRM/R-PRM provide explanations without formal grounding, Safe provides formal verification states without NL rationales, Proof-RM scores proof quality without rationale generation, R-Align diagnoses spurious correctness without formal remedies, VPRMs use rule-based not proof-based verification, CVPDS uses template-based error injection rather than genuine proof artifact extraction, and 'Outcome Accuracy is Not Enough' improves rationale quality through soft semantic matching rather than deterministic formal grounding.",
  "inspired_by": "Field guide Gap 6 (faithfulness of CoT verification rationales in GenRM -- 'never fully resolved'), R-Align's demonstration that substantial GenRM decisions are spuriously correct, R-PRM's demonstration that reasoning-driven evaluation improves accuracy without addressing faithfulness, FormalRewardBench's finding that LLMs cannot reliably evaluate formal proofs (motivating tool-based grounding), and the untried bridge between FoVer's formal proof artifacts and ThinkPRM's rationale generation",
  "approach": "We scope our primary contribution to domains where FoVer's formal verification pipeline is validated: GSM8K-level arithmetic (Isabelle) and first-order logic tasks (Z3 on FOLIO/LogicNLI). We evaluate transfer to harder domains as a secondary analysis, with dedicated experiments testing whether formal grounding's faithfulness benefits propagate via the same easy-to-difficult mechanism FoVer demonstrated for accuracy, and whether reduced S-Corr translates to improved downstream policy training.\n\nPhase 1 -- Data Preparation and Proof Artifact Extraction (~3-4 weeks engineering). We begin from FoVer-40K, the published balanced training dataset containing 40,000 steps (20K formal logic + 20K theorem proving) at 50% error rate. This yields 20,000 error steps as the base for artifact extraction. Additionally, we augment the base data by re-running FoVer's open-source pipeline on additional problems: FoVer sampled only 10,000 problems per task from much larger source datasets -- FLDx2 contains 100K+ formal logic problems, while MetaMathQA provides 395K math problems. By sampling an additional 10K problems per task and generating solutions from one additional LLM (e.g., Qwen3-8B), we estimate producing ~40K additional error steps at similar error rates (logic ~42%, proof ~14%), yielding a combined pool of ~30K error steps for artifact extraction. We extract artifacts in two tracks: (a) For Z3-verified logic steps, we extract structured counterexamples from SAT results. Z3 natively produces satisfying models when a formula is satisfiable, so for each incorrect step we obtain variable assignments demonstrating the error. This is primarily a parsing and templating task (~1-2 weeks). We estimate ~95% of incorrect logic steps yield extractable counterexamples, since Z3 reliably produces models for SAT results. (b) For Isabelle-verified theorem proving steps, we modify FoVer's Isabelle wrapper to capture proof state information at failure points -- the current goal, available hypotheses, and which tactic failed (~2-3 weeks, requiring deeper Isabelle API integration). We estimate ~60-70% of incorrect steps yield usable proof state artifacts, as some failures occur in preprocessing before meaningful state is available. Pilot validation: we run artifact extraction on a 2K-step sample (1K logic, 1K arithmetic) in week 1 to calibrate yield estimates before full-scale extraction. This pilot also calibrates cross-domain roundtrip equivalence rates (see Phase 2), since math/logic formalization may differ from Amrollahi et al.'s statutory text domain in both directions: math/logic has lower linguistic ambiguity (potentially favoring higher equivalence rates) but higher formalization difficulty for non-trivial steps involving implicit mathematical conventions (potentially favoring lower rates). The pilot's empirical calibration resolves this directional uncertainty before committing to full-scale synthesis.\n\nPhase 2 -- Proof-Grounded Rationale Synthesis (~3 weeks). We use Qwen3-32B to synthesize natural-language verification rationales grounded in extracted artifacts. Each rationale template incorporates the specific artifact (e.g., 'Step 3 claims x+y>10, but the counterexample x=3, y=2 shows this fails' for Z3; 'The proof state after step 4 has unsolved goal involving P(n+1), but the applied tactic only handles the base case' for Isabelle). We apply roundtrip consistency filtering adapted from Amrollahi et al. (2604.25031): each generated rationale is re-formalized and checked for Z3/Isabelle semantic equivalence with the original artifact. Amrollahi et al. report 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model) or 91-95% with cross-model diagnosis (a separate LLM performs only the diagnosis step while the primary model executes the pipeline). We implement standard same-model diagnosis-guided repair using Qwen3-32B as both diagnostician and pipeline executor, following their finding that scoped stage-level diagnosis outperforms random-stage repair. We do not implement cross-model diagnosis in the initial pipeline to avoid the additional complexity and cost of routing diagnosis through a separate LLM, but note it as an available improvement lever if standard repair yields insufficient throughput. Given the directional uncertainty in cross-domain transfer (math/logic vs. statutory text), we conservatively estimate 50-65% baseline pass rate on our domains, improvable to 70-85% with standard diagnosis-guided repair. The Phase 1 pilot on 2K steps will empirically calibrate these estimates before full-scale synthesis. Data yield estimate with two scenarios:\n\n  Scenario A (FoVer-40K only, conservative): Starting from ~20K error steps -> ~16K with extractable artifacts (9.5K Z3 at 95% + 6.5K Isabelle at 65%) -> ~11.2-13.6K after roundtrip+repair filtering at ~70-85% -> ~9.5-11.6K after ~15% final quality filtering. Final: ~9-12K proof-grounded rationales.\n\n  Scenario B (FoVer-40K + augmented pipeline): Starting from ~30K error steps -> ~24K with extractable artifacts (15K Z3 + 9K Isabelle) -> ~16.8-20.4K after roundtrip filtering -> ~14.3-17.3K after quality filtering. Final: ~14-17K proof-grounded rationales.\n\n  Data sufficiency argument: ThinkPRM achieves competitive performance with only 1K synthetic verification CoTs (~8K step labels), GenPRM uses 23K training examples, and R-PRM uses ~289K SFT samples but achieves comparable performance to Qwen2.5-Math-PRM with only ~15% of its data. Our conservative Scenario A of ~9-12K formally grounded rationales represents ~10x ThinkPRM's training data and is comparable to GenPRM's scale. Moreover, our rationales carry richer supervision signal than any of these: each rationale is traceable to a specific formal proof artifact with verified semantic grounding, whereas ThinkPRM's rationales are filtered only on label match, GenPRM's use execution-based but not proof-based verification, and R-PRM's are bootstrapped from LLM-generated seed data without formal grounding. We thus expect higher per-example training signal quality, partially compensating for any quantity gap.\n\nPhase 3 -- SFT Training (~2 weeks). We fine-tune Qwen3-14B (or DeepSeek-R1-Distill-Qwen-14B) as a generative PRM on the proof-grounded rationales following ThinkPRM's SFT recipe. We train separate models on Z3-grounded logic rationales, Isabelle-grounded arithmetic rationales, and the combined set to enable ablation of each grounding source's contribution.\n\nPhase 4 -- Evaluation (~3-4 weeks). Verification accuracy is evaluated on: (primary) ProcessBench-GSM8K subset, FOLIO, LogicNLI; (transfer) ProcessBench-MATH/Olympiad subsets, MATH-500 best-of-N; targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N scores as baselines. Rationale faithfulness is assessed via three independent metrics, strictly separated from training: (1) R-Align's Spurious Correctness (S-Corr) as the primary automated faithfulness metric, computed by comparing rationale reasoning against golden reference judgments from ProcessBench annotations; (2) FaithCoT-Bench detection metrics (precision, recall, F1); (3) human evaluation on 150-200 randomly sampled rationales, rating formal grounding quality and error identification accuracy. Roundtrip consistency is reported ONLY as a supplementary training-data-quality indicator and correlation analysis (does higher roundtrip score predict higher human-rated quality?), not as a primary evaluation metric or novel contribution.\n\nCritically, Phase 4 includes two dedicated experiments that go beyond standard PRM evaluation:\n\n(A) Faithfulness transfer experiment. We measure S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for: (a) our formally grounded model trained only on GSM8K-level/FOL rationales; (b) ThinkPRM-14B baseline; (c) GenPRM-7B baseline; (d) R-PRM-7B-DPO baseline (the strongest reasoning-based PRM without formal grounding -- testing whether rich reasoning analyses alone reduce S-Corr); (e) an ablation model trained on FoVer-40K binary labels (no formal rationale grounding). This experiment disentangles four claims: (i) does formal grounding reduce S-Corr on in-domain tasks (GSM8K, FOL)? (ii) does the S-Corr reduction transfer to harder domains (MATH, Olympiad) via the same easy-to-difficult mechanism FoVer demonstrated for accuracy? (iii) does the transfer specifically require rationale-level formal grounding, or does any FoVer-derived training signal suffice? (iv) does R-PRM's reasoning-driven evaluation reduce S-Corr relative to simpler baselines -- isolating whether accuracy-improving reasoning also improves faithfulness, or whether formal grounding provides an orthogonal faithfulness benefit? If (i) holds but (ii) doesn't, we still demonstrate improved faithfulness within the validated scope. If both hold, we provide the first empirical evidence that formal rationale grounding at the foundational training-data level propagates to harder reasoning tasks.\n\n(B) Downstream policy experiment. To close the full causal chain (formal grounding -> reduced S-Corr -> better downstream policy), we conduct a small-scale rejection sampling experiment. We generate N=8 candidate solutions per problem for 500 GSM8K and 500 MATH problems using Qwen2.5-Math-1.5B-Instruct as the policy model, then select the best response according to each PRM: (a) our formally grounded PRM; (b) ThinkPRM-14B; (c) R-PRM-7B-DPO; (d) FoVer-trained discriminative PRM (binary labels). We report pass@1 accuracy of the selected solutions (best-of-N evaluation) and, as a stronger test, perform rejection sampling fine-tuning (RFT): we fine-tune Qwen2.5-Math-1.5B on the top-ranked solutions selected by each PRM (filtering to solutions verified as correct), then evaluate the resulting policy models on held-out MATH-500 and GSM8K test sets. R-Align demonstrates that S-Corr predicts RLHF policy degeneration (as established in the paper's experimental analysis); our experiment directly tests whether formally grounded rationale selection -- by reducing spurious correctness in the reward signal -- yields better-trained policies. This is a modest-cost experiment (~50-80 GPU hours for generation + RFT on 1.5B model) that could provide the strongest possible impact argument. Even a 1-2 point accuracy improvement on MATH-500 pass@1 via formally grounded selection would validate the full pipeline.\n\nImpact beyond easy domains: Three arguments justify the broader significance of improving rationale faithfulness on GSM8K-level and FOL tasks. (1) Training-data origin: GSM8K-level problems are the primary source for PRM training data construction (PRM800K, FoVer, OmegaPRM's 1.5M annotations all derive from or include GSM8K/MATH). Improving the faithfulness of rationales at this foundational level improves the training signal for all downstream applications. (2) Transfer prediction: R-Align demonstrates that S-Corr on evaluation benchmarks predicts policy degeneration during RLHF (as established in the paper's experimental analysis), and FoVer demonstrates easy-to-difficult accuracy transfer -- PRMs trained on GSM8K-level data improve verification on MATH (88.0% vs 78.2%), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%). Our faithfulness transfer experiment (above) directly tests whether reducing S-Corr at the source level propagates via the same mechanism, transforming this from a theoretical chain to empirical evidence. (3) Methodology contribution: The proof-artifact-to-rationale bridge is a general technique independent of problem difficulty. Initial validation on computationally tractable domains is standard practice -- FoVer itself started with GSM8K-level validation before demonstrating broad transfer, and CVPDS (arXiv 2605.02395) similarly validates on logical reasoning before testing mathematical transfer. As formal verification tools extend to harder domains (e.g., Lean 4 integration via Safe's autoformalization pipeline, or SymPy+Z3 via MATH-VF), the same methodology applies directly.\n\nAcknowledged Limitations and Mitigations. (1) Scope: FoVer's formal verification is validated on GSM8K-level arithmetic and FOL logic. Extending to competition math faces fundamental barriers -- Z3 is undecidable for nonlinear integer arithmetic (confirmed by 'SMT and Functional Equation Solving over the Reals,' 2025), and FormalMATH shows only 16.46% LLM prover success on Lean4 problems. MATH-500 and GPQA-Diamond are explicitly positioned as stretch goals requiring future formalization extensions: specifically, Lean 4 integration (via Safe's autoformalization pipeline) for algebraic reasoning, or SymPy+Z3 (via MATH-VF's approach) for computational verification. (2) Gaming vulnerability: Kim et al. (2604.19459) show two-stage formalization pipelines are vulnerable to premise mistranslation. Our Z3 formal equivalence check provides stronger detection than LLM-as-judge for axiom-fabrication-type errors (would catch GPT-5's 107 fabricated axioms in their study), but cannot fully guard against symmetric mistranslation at the NL-to-formal boundary. We mitigate via: (a) roundtrip verification from Amrollahi et al., which catches asymmetric errors; (b) NLI-based drift analysis as a secondary signal; (c) restricting to domains (FOL, arithmetic) where formalization ambiguity is lower than natural language. (3) FormalRewardBench shows even frontier LLMs achieve only 59.8% on formal proof evaluation, but our approach uses formal verification tools (Z3, Isabelle) as ground truth rather than LLMs as proof evaluators, sidestepping the generation-evaluation gap within Z3/Isabelle's decidable scope. (4) Cross-domain roundtrip uncertainty: Amrollahi et al.'s roundtrip equivalence rates were measured on statutory text, while our pipeline operates on math/logic formalization. These domains may differ in opposing ways: math/logic has lower linguistic ambiguity and more standardized notation (potentially yielding higher equivalence rates), but non-trivial mathematical steps involve implicit conventions and multi-step dependencies that may resist clean formalization (potentially yielding lower rates). Our Phase 1 pilot validation on 2K steps is specifically designed to calibrate this cross-domain transfer before committing to full-scale synthesis, and we report pilot equivalence rates alongside Amrollahi et al.'s statutory text rates to enable direct comparison. (5) Complementarity with non-formal approaches: 'Outcome Accuracy is Not Enough' (Qwen team, 2602.04649) achieves strong rationale quality improvements through soft semantic matching against human annotations without formal grounding. Our approach provides stronger guarantees (deterministic formal traceability) within a narrower scope; their approach provides broader coverage (any domain with annotations) with softer guarantees. Future work should explore combining formal grounding for in-scope domains with hybrid consistency training for broader coverage. (6) Relationship to concurrent data synthesis work: CVPDS (arXiv 2605.02395) provides an alternative approach to generating verified PRM training data through template-based error injection. While methodologically distinct from proof-artifact extraction, both approaches aim to improve PRM training data quality through formal/symbolic verification. Our approaches are complementary: CVPDS offers controllable error diversity but is constrained by predefined templates, while our method extracts artifacts from naturally occurring LLM errors but requires successful formal verification. Combining controlled error injection with proof-artifact rationale grounding is a promising future direction.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "500-700 (solution generation for augmented data ~80h, rationale synthesis with Qwen3-32B ~120h, SFT on 14B model 4xA100 ~100h, evaluation including faithfulness transfer experiment ~100h, downstream policy experiment ~60h, ablations ~90h)",
      "engineering_time": "Z3 counterexample parsing: ~1-2 weeks; Isabelle proof state extraction: ~2-3 weeks; augmented data generation: ~1 week; roundtrip filter + diagnosis repair: ~1 week; downstream RFT pipeline: ~0.5 weeks; integration/testing: ~1 week. Total: 6-8 weeks engineering.",
      "timeline": "15-19 weeks",
      "estimated_gpu_cost": "$1000-1700 (A100 80GB at ~$2.00/hr on Vast.ai/Spheron)"
    },
    "human_in_loop": {
      "gpu_hours": "500-700 (irreducible training/inference costs unchanged)",
      "engineering_time": "3-5 weeks (Claude accelerates Z3 parsing code, Isabelle wrapper modifications, rationale template design, augmented data pipeline, evaluation harness, RFT pipeline)",
      "timeline": "11-15 weeks",
      "claude_api_cost": "$500-800 (Sonnet 4.6 for pipeline code generation and data analysis, ~100-200M tokens)",
      "estimated_gpu_cost": "$1000-1700"
    },
    "auto_research": {
      "gpu_hours": "550-750 (slightly higher from automated ablation sweeps, augmented data generation, faithfulness transfer experiment, downstream policy experiment, and pilot experiments)",
      "engineering_time": "2-3 weeks (Claude handles most Z3/Isabelle parsing engineering)",
      "timeline": "8-11 weeks",
      "claude_api_cost": "$1500-2500 (Sonnet 4.6 for end-to-end pipeline orchestration, rationale quality filtering, iterative ablation design, ~400-700M tokens)",
      "estimated_gpu_cost": "$1100-1800",
      "speed_bottleneck": "Isabelle proof state extraction engineering (~2-3 weeks irreducible due to Isabelle API complexity); Z3 counterexample extraction is faster (~1-2 weeks). Formal verification throughput (~2-10s per Z3 step, 15-60s per Isabelle step) is parallelizable across CPU cores. Augmented data generation adds ~1 week for solution generation and verification. Downstream RFT experiment is fast (~50-80h GPU) but depends on Phase 3 model completion."
    }
  },
  "target_venues": [
    "ICLR 2027 (projected abstracts Sep 19, full papers Sep 24, 2026 -- 17 weeks; projected from ICLR 2026 pattern, official CFP not yet published as of May 2026; comfortable for human_in_loop and auto_research timelines)",
    "ARR October 2026 cycle -> commitment to NAACL 2027 or ACL 2027 (comfortable backup NLP venue)",
    "AAAI 2027 (abstracts Jul 21, full papers Jul 28, 2026 -- 8 weeks from today, feasible only with auto_research timeline and Z3-only scoped initial submission)"
  ],
  "level": "top-tier",
  "key_references": [
    "Process Reward Models That Think (arXiv 2025, ThinkPRM)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)",
    "R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, She et al.)",
    "Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, FoVer)",
    "Controllable and Verifiable Process Data Synthesis for Process Reward Models (arXiv 2605.02395, May 2026, Chi & Wang)",
    "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026)",
    "RM-R1: Reward Modeling as Reasoning (ICLR 2026)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026, Amrollahi et al.)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 @ ICLR 2026, Kim et al.)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2605.10141, May 2026)",
    "Beyond Outcome Verification: Verifiable Process Reward Models (arXiv 2601.17223, Jan 2026, VPRMs)",
    "Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)",
    "R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging (arXiv Feb 2026)",
    "Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models (NeurIPS 2025)",
    "Proof-RM: A Scalable and Generalizable Reward Model for Math Proof (arXiv Feb 2026)",
    "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)",
    "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026, PRoSFI)",
    "Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models (arXiv 2602.04649, Feb 2026, Qwen team)",
    "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2025, MATH-VF)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of LLMs (arXiv 2025)",
    "Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024, OmegaPRM)",
    "GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling (NeurIPS 2025 Workshop)"
  ],
  "description": "We propose Proof-Grounded Generative PRMs, the first process reward models whose verification rationales are traceable to structured formal proof artifacts. Current generative PRMs (ThinkPRM, GenPRM, R-PRM, RM-R1) produce chain-of-thought verification rationales trained on synthetic data of unknown faithfulness -- R-Align shows GenRM decisions exhibit substantial spurious correctness (right label, wrong reasoning), and frontier GenRMs achieve only approximately 40% rationale consistency with human judgments. R-PRM (EMNLP 2025) demonstrates that reasoning-driven evaluation substantially improves PRM accuracy (70.4 F1 on ProcessBench, +13.9 over baselines), but its multi-dimensional analyses are trained on LLM-bootstrapped data and rationale faithfulness is not evaluated. Separately, FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can produce accurate step-level error labels transferring across 12 benchmarks, but generates only binary labels and explicitly excludes reasoning-based PRMs. A concurrent approach (CVPDS, arXiv 2605.02395) synthesizes PRM data through template-based symbolic error injection across 11 error types with 20K instances, but targets accuracy through controlled error diversity rather than rationale faithfulness through proof-artifact grounding. A non-formal approach ('Outcome Accuracy is Not Enough,' Qwen team) improves rationale quality through hybrid consistency-outcome training via soft semantic matching against human annotations, achieving RM-Bench 87.1% (+5% over baselines) -- but relies on human annotation availability and provides softer guarantees than formal artifact tracing. We bridge the formal gap by: (1) extending FoVer's Z3 pipeline to extract structured counterexamples from SAT results and modifying its Isabelle wrapper to capture proof state information at failure points -- going beyond binary labels to structured artifacts (~3-4 weeks engineering, with pilot validation on 2K steps to calibrate both yield and cross-domain roundtrip equivalence rates); (2) synthesizing verification rationales grounded in these artifacts using Qwen3-32B, with roundtrip consistency filtering adapted from Amrollahi et al.'s (2604.25031) validated mechanism (45-66% baseline equivalence, 78-86% with standard diagnosis-guided repair, up to 91-95% with cross-model diagnosis; we implement standard same-model repair and conservatively estimate 70-85% post-repair rates on math/logic given cross-domain uncertainty); (3) fine-tuning Qwen3-14B as a generative PRM on these rationales. Starting from FoVer-40K's 20K error steps, we estimate ~9-12K proof-grounded rationales (Scenario A); augmenting FoVer's pipeline with additional problems from the much larger source datasets yields ~14-17K (Scenario B). Both scenarios exceed ThinkPRM's training data (1K rationales / 8K step labels) by an order of magnitude, and our rationales carry richer per-example signal via formal artifact tracing. We scope primary evaluation to domains where FoVer is validated -- GSM8K-level arithmetic and FOL logic (FOLIO, LogicNLI) -- targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N as baselines. Rationale faithfulness is assessed via R-Align's Spurious Correctness metric and FaithCoT-Bench as primary measures, plus human evaluation on 150-200 examples, with roundtrip consistency strictly demoted to a supplementary training-quality indicator. We include two dedicated experiments beyond standard PRM evaluation: (A) a faithfulness transfer experiment measuring S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for our GSM8K-trained model versus baselines (including R-PRM-7B-DPO, the strongest reasoning-based baseline without formal grounding) and a binary-label ablation, directly testing whether formal rationale grounding propagates faithfulness improvements to harder domains; (B) a downstream policy experiment conducting rejection sampling fine-tuning of Qwen2.5-Math-1.5B using solutions selected by each PRM on 500 GSM8K + 500 MATH problems, testing whether reduced S-Corr from formally grounded rationales translates to improved policy training -- closing the full causal chain from formal grounding to downstream impact that R-Align's S-Corr-to-RLHF correlation predicts. We argue broader impact via three mechanisms: (a) GSM8K-level is the origin of most PRM training data; (b) FoVer demonstrates easy-to-difficult accuracy transfer (MATH: 88.0% vs 78.2%, Olympiad: 84.0% vs 76.2%) and R-Align shows S-Corr predicts RLHF degeneration; (c) the proof-artifact-to-rationale methodology is domain-independent. We acknowledge scope limitations (Z3 undecidability for nonlinear arithmetic; FormalMATH's 16.46% prover success), gaming vulnerabilities in two-stage pipelines (Kim et al.), cross-domain roundtrip uncertainty (math/logic may differ from statutory text in both directions), complementarity with both non-formal approaches (Qwen team's hybrid training) and concurrent data synthesis methods (CVPDS's template-based error injection).",
  "project_name": "proof_grounded_genprm",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_faithful_autoformalization_numbers": "ADDRESSED (MODERATE, round 4). Corrected landscape statement from '85-95% with diagnosis-guided repair' to precise numbers verified from Table 1, Section 7.1 of Amrollahi et al.: standard diagnosis-guided repair (same model) achieves 77.9%-85.7% equivalence, while cross-model diagnosis (Claude performs diagnosis, GPT executes pipeline) achieves 90.7%-94.7%. All instances updated throughout.",
    "issue_2_hybrid_training_positioning": "ADDRESSED (MODERATE, round 4). Added 'Outcome Accuracy is Not Enough' (Qwen team, arXiv 2602.04649) to the landscape with detailed positioning as complementary non-formal approach.",
    "issue_3_faithfulness_transfer_experiment": "ADDRESSED (MINOR, round 4). Added dedicated faithfulness transfer experiment to Phase 4 with four-way comparison and ablation.",
    "issue_4_crossdomain_roundtrip_uncertainty": "ADDRESSED (MINOR, round 4). Added explicit acknowledgment of cross-domain uncertainty with pilot calibration strategy.",
    "issue_5_rprm_baseline": "ADDRESSED (MODERATE, round 5). Added R-PRM (EMNLP 2025, She et al.) comprehensively to the landscape with detailed methodology and results: reasoning-driven multi-dimensional step analysis (Previous Steps, Now Step, Data Source, Consistency, Calculation Analysis), R-PRM-7B-DPO achieving 70.4 F1 on ProcessBench (+13.9 over baselines), +8.5 F1 on PRMBench, +8.6 accuracy on downstream math reasoning. Positioned as the strongest reasoning-based PRM baseline that demonstrates the ceiling of accuracy-focused reasoning without formal grounding -- rich analyses but untested faithfulness. R-PRM sharpens our value proposition: if reasoning-driven evaluation already provides substantial accuracy gains, formal grounding must provide ADDITIONAL benefits, specifically traceable rationale faithfulness rather than just accuracy. Added R-PRM-7B-DPO as a baseline in both the faithfulness transfer experiment (testing whether reasoning-driven analysis alone reduces S-Corr, adding a fourth claim to disentangle) and the accuracy evaluation (targeting its 70.4 F1). Updated core_problem, opportunity, gap analysis, data sufficiency argument, and evaluation baselines accordingly.",
    "issue_6_cvpds_concurrent_work": "ADDRESSED (MODERATE, round 5). Added 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) to the landscape with detailed methodology: four-stage pipeline (correct chain synthesis from rule templates, template-aware error injection across 11 error types, symbolic recomputation for trajectory consistency, prefix non-derivability verification), 20K instances, best-of-8 results (Llama-3.1-8B: 0.528->0.591, Qwen-2.5-7B: 0.567->0.615), limited math transfer (ProcessBench GSM8K: 21.2% F1). Key distinction clearly articulated: CVPDS generates controlled synthetic errors through template-based injection for accuracy-focused PRM training; our approach extracts genuine proof artifacts from naturally occurring LLM errors for faithfulness-focused rationale grounding. Their error diversity is template-constrained (acknowledged limitation); our artifacts reflect actual LLM error distributions. Positioned as complementary -- combining controlled error injection with proof-artifact grounding noted as future direction. Added to gap analysis and new limitation (6).",
    "issue_7_downstream_rlhf_experiment": "ADDRESSED (MINOR, round 5). Added Phase 4(B) downstream policy experiment: best-of-N selection + rejection sampling fine-tuning (RFT) of Qwen2.5-Math-1.5B using solutions selected by each PRM (our formally grounded PRM, ThinkPRM-14B, R-PRM-7B-DPO, FoVer discriminative PRM). Generates N=8 candidates per problem for 500 GSM8K + 500 MATH problems, selects best via each PRM, fine-tunes 1.5B policy on correct selected solutions, evaluates on held-out test sets. This closes the full causal chain: formal grounding -> reduced S-Corr -> better policy training. Modest cost (~50-80 GPU hours) for potentially the strongest impact argument. Resource estimates updated to include this experiment (GPU hours increased by ~50-80h across all tiers, engineering time increased by ~0.5 weeks).",
    "issue_8_iclr2027_deadline_tentative": "ADDRESSED (MINOR, round 5). ICLR 2027 deadline now explicitly noted as 'projected from ICLR 2026 pattern, official CFP not yet published as of May 2026' in target venues.",
    "issue_9_ralign_claims_clarification": "ADDRESSED (MINOR, round 5). R-Align description now distinguishes between abstract-level claims ('substantial S-Corr even for competitive GenRMs') and full-paper experimental details ('specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract'). All references to R-Align's RLHF prediction now use 'as established in the paper's experimental analysis' rather than implying the specific evidence comes from the abstract."
  }
}

## Reviewer feedback (round 6)
Issues: ["MINOR: R-PRM baseline F1 misquoted as 58.5 throughout the proposal; the published EMNLP version and GitHub results table show Qwen2.5-Math-7B-PRM800K achieves 56.5 F1 (not 58.5), consistent with 70.4 - 56.5 = +13.9 improvement. The improvement claim (+13.9) and the R-PRM-7B-DPO score (70.4) are correct, but the baseline number needs correction from 58.5 to 56.5.", "MINOR: StepProof (arXiv 2506.10558) performs step-by-step Isabelle-based autoformalization and verification on GSM8K — operating in exactly the domain and tool setting of this proposal. While it targets proof autoformalization rather than PRM rationale training, it provides relevant engineering insights for Isabelle proof state handling and should be acknowledged.", "MINOR: 'Learning to Disprove: Formal Counterexample Generation with Large Language Models' (arXiv 2603.19514, March 2026) trains LLMs to generate formal counterexamples verified in Lean 4 via a symbolic mutation strategy. While using Lean 4 rather than Z3/Isabelle, the conceptual parallel of using formal counterexamples as training signals is relevant and demonstrates scalable counterexample generation.", "STRUCTURAL: The average score (3.75) is below the 4.0 threshold primarily due to the inherent scope limitation — formal grounding is validated only on easy domains where its practical value is lower, while the harder domains where it would be most impactful are beyond current formalization capabilities. This is honestly acknowledged but remains the fundamental barrier to a higher impact score."]
Feedback: The proposal has matured significantly through 6 rounds — all critical issues from rounds 1-4 are fully resolved, and the landscape is now best-in-class for this area. Three minor fixes remain:

(1) CORRECT THE R-PRM BASELINE: Change 'Qwen2.5-Math-7B-PRM800K at 58.5 F1' to '56.5 F1' throughout. The published EMNLP version and GitHub table confirm: R-PRM-7B-DPO 70.4 - Qwen2.5-Math-7B-PRM800K 56.5 = +13.9 F1. Your improvement claim is correct; only the baseline number needs updating.

(2) ACKNOWLEDGE StepProof and 'Learning to Disprove': StepProof operates in your exact domain (step-by-step Isabelle verification on GSM8K) and provides relevant engineering precedent. 'Learning to Disprove' demonstrates formal counterexample generation at scale. Neither threatens novelty but both inform feasibility.

(3) IMPACT CEILING: The fundamental challenge is that the average score (3.75) is dragged below 4.0 by impact (3.5) and feasibility (3.5), both constrained by the scope limitation. To potentially push impact higher, consider strengthening the argument that GSM8K/FOL-level formal grounding is inherently valuable BEYOND transfer — e.g., for safety-critical applications where traceable error explanations are required regardless of domain difficulty, or for PRM interpretability/debugging where understanding WHY a step is wrong matters more than just detecting it. The 'training data origin' argument is your strongest impact lever — consider making it more central.

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
经过 6 轮修订，近 3 轮平均分从 3.9 到 3.8，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "type": "user",
  "uuid": "b2e3455b-c75c-431d-9e82-824baece8c0f",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T20:23:32.272Z_

```json
{
  "parentUuid": "b2e3455b-c75c-431d-9e82-824baece8c0f",
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
  "uuid": "e4df7f35-4de2-4b79-9e5d-17a9be25300a",
  "timestamp": "2026-05-27T20:23:32.272Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T20:23:32.272Z_

```json
{
  "parentUuid": "e4df7f35-4de2-4b79-9e5d-17a9be25300a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e1e5ceaf-66fc-46a5-95ab-758f5f108605",
  "timestamp": "2026-05-27T20:23:32.272Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",   \"core_pr…",
  "leafUuid": "e1e5ceaf-66fc-46a5-95ab-758f5f108605",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise formal PRM rationale proposal with R-PRM baseline correction",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Assistant

_source line 8 · 2026-05-27T20:23:57.303Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully before deciding on my approach.

The key issues are:
1. MINOR: R-PRM baseline F1 correction (58.5 → 56.5)
2. MINOR: Acknowledge StepProof and "Learning to Disprove"
3. MINOR: (but really structural) Impact ceiling due to scope limitation
4. STRUCTURAL: Average score 3.75 below 4.0 threshold, primarily due to inherent scope limitation

The reviewer notes that after 6 rounds, the score has been stagnating (3.9 → 3.8). The fundamental issue is that formal grounding is validated only on easy domains where its practical value is lower.
 
Now I'm wrestling with whether to make targeted fixes or attempt something more substantial. The core problem is that I can only formally ground rationales on simple domains like GSM8K and FOL, yet the real value of faithful explanations matters most for harder problems—that's a fundamental mismatch that surface-level corrections won't fix. I could stick with minor edits and likely stay around 3.75, or I could reframe the entire contribution to position easy-domain scope as an advantage for safety-critical applications and PRM interpretability rather than a limitation.

The reviewer's feedback is pointing toward something stronger: treating this as a diagnostic tool for understanding why PRMs fail on hard problems by examining whether their rationale behavior holds up on formally verifiable subproblems, and drawing an analogy to how RLHF researchers care about reward model faithfulness to prevent reward hacking. The "training data origin" argument becomes the linchpin here—faithful rationales prevent the reward signal from being gamed, regardless of problem difficulty.

I'm also considering whether to expand scope through formal verification tools or reframe the entire contribution as a study on PRM faithfulness rather than just a training method, though the proposal is already quite developed and the reviewer's core concern seems to be about impact rather than completeness.

The real work ahead is addressing the framing issue—I need to find those missing references first, then figure out how to reposition the contribution to better articulate its significance without fundamentally changing the methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1e5ceaf-66fc-46a5-95ab-758f5f108605",
  "isSidechain": false,
  "requestId": "req_011CbThTNxpR42yXbXSTFrFv",
  "type": "assistant",
  "uuid": "433cc7e8-40ed-4535-a5a3-0b4e1cc8694f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FiVJ1dzkujpp4YCQQT8T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14517,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1861,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14517
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

_source line 9 · 2026-05-27T20:23:57.306Z_

Let me start by researching the new papers and thinking deeply about the impact ceiling issue before deciding on the revision strategy.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "433cc7e8-40ed-4535-a5a3-0b4e1cc8694f",
  "isSidechain": false,
  "requestId": "req_011CbThTNxpR42yXbXSTFrFv",
  "type": "assistant",
  "uuid": "b1d377ef-389f-4aea-bce4-bc40117d68ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FiVJ1dzkujpp4YCQQT8T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14517,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1861,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14517
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

_source line 10 · 2026-05-27T20:24:01.062Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01UkmnWRLDQGDqtQhTRS1Px7`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research StepProof paper",
  "prompt": "I need to research the paper \"StepProof\" (arXiv 2506.10558) which performs step-by-step Isabelle-based autoformalization and verification on GSM8K. \n\nPlease:\n1. Search the web for \"StepProof arXiv 2506.10558 Isabelle GSM8K step-by-step\"\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2506.10558\n3. Search for any related discussions or citations\n\nI need: the full title, authors, key methodology (how they do step-by-step Isabelle verification), their results on GSM8K, any engineering insights about Isabelle proof state handling, and how this relates to formal verification for process reward models. Report in detail (300-500 words)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b1d377ef-389f-4aea-bce4-bc40117d68ae",
  "isSidechain": false,
  "requestId": "req_011CbThTNxpR42yXbXSTFrFv",
  "type": "assistant",
  "uuid": "c67235cc-e857-4c80-b722-94993994e470",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FiVJ1dzkujpp4YCQQT8T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14517,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1861,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14517
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

_source line 11 · 2026-05-27T20:24:03.474Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01NoAPZK6DycfiDcm837G9y6`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research Learning to Disprove paper",
  "prompt": "I need to research the paper \"Learning to Disprove: Formal Counterexample Generation with Large Language Models\" (arXiv 2603.19514, March 2026). \n\nPlease:\n1. Search the web for \"Learning to Disprove formal counterexample generation LLM arXiv 2603.19514\"\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2603.19514\n3. Search for any related discussions\n\nI need: the full title, authors, key methodology (symbolic mutation strategy, how they train LLMs to generate formal counterexamples in Lean 4), their results, scale of counterexample generation, and how this relates to using formal counterexamples as training signals for verification. Report in detail (300-500 words)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c67235cc-e857-4c80-b722-94993994e470",
  "isSidechain": false,
  "requestId": "req_011CbThTNxpR42yXbXSTFrFv",
  "type": "assistant",
  "uuid": "987960c0-986b-4bcf-a401-1fca0c52ddcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FiVJ1dzkujpp4YCQQT8T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14517,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1861,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14517
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

_source line 12 · 2026-05-27T20:24:09.857Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015tDsY6xGc7cun81wxEevRc`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research safety-critical math verification and PRM interpretability",
  "prompt": "I need to research the value proposition of formally traceable mathematical error explanations for safety-critical applications and PRM interpretability. This is for a research paper about process reward models (PRMs) that verify math reasoning steps.\n\nPlease search for:\n1. \"safety-critical math verification\" OR \"trustworthy mathematical reasoning\" OR \"interpretable reward model\"\n2. \"process reward model interpretability\" OR \"PRM debugging\" OR \"reward model faithfulness safety\"\n3. \"formal verification AI safety\" OR \"verifiable AI reasoning\" applications in critical domains\n4. Any recent papers (2025-2026) on reward model faithfulness for alignment/safety\n\nI'm looking for arguments and evidence that formally traceable error explanations in mathematical reasoning are valuable BEYOND just improving accuracy — specifically for:\n- Safety-critical applications (finance, engineering, medicine) where knowing WHY a step is wrong matters\n- PRM interpretability/debugging (understanding failure modes of reward models)\n- Alignment: preventing reward hacking by ensuring the reward signal is faithful\n- Training data quality: GSM8K-level problems as the foundation for all PRM training data\n\nReport any relevant papers, arguments, or evidence in 400-600 words."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "987960c0-986b-4bcf-a401-1fca0c52ddcc",
  "isSidechain": false,
  "requestId": "req_011CbThTNxpR42yXbXSTFrFv",
  "type": "assistant",
  "uuid": "490f3231-82fa-4315-bfdd-363f8d0e6614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012FiVJ1dzkujpp4YCQQT8T8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 14517,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1861,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14517,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1861,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 14517,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14517
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

_source line 13 · 2026-05-27T20:25:03.163Z_

<details><summary>↩ Tool result · `toolu_01NoAPZK6DycfiDcm837G9y6`</summary>

```text
Here is the detailed report on the paper.

---

**Title:** Learning to Disprove: Formal Counterexample Generation with Large Language Models

**Authors:** Zenan Li, Zhaoyu Li, Kaiyu Yang, Xiaoxing Ma, and Zhendong Su (ETH Zurich, University of Toronto, MiroMind, Nanjing University)

**arXiv ID:** 2603.19514 (submitted March 19, 2026)

**Core Motivation and Problem.** Current AI-for-mathematics research overwhelmingly targets proof construction -- proving true statements. This paper addresses the neglected complementary skill: discovering counterexamples to disprove false statements. The authors formalize the task as *formal counterexample generation*, requiring an LLM not only to propose a concrete counterexample but also to produce a machine-checkable proof in the Lean 4 theorem prover that the counterexample indeed invalidates the claim.

**Symbolic Mutation Strategy.** The key data-synthesis innovation is a three-step symbolic mutation pipeline. Starting from a formally proved theorem of the form `forall x, H1(x) -> H2(x) -> C(x)`, the method (1) analyzes the original proof trace to identify which hypotheses are necessary, (2) discards one essential hypothesis (e.g., H1), producing a mutated -- now false -- statement `H2(x) -> C(x)`, and (3) verifies via Lean 4 that the mutation is indeed invalid. This yields two companion tasks: find an x* satisfying the remaining hypothesis path, and show that x* violates the dropped hypothesis. Applied to four theorem sources (Mathlib, Lean Workbook, MiniF2F, PutnamBench), the strategy produced **575,039 counterexample instances from 321,929 seed theorems**, at an average rate of 0.3--0.7 seconds per theorem.

**Multi-Reward Expert Iteration.** Training uses a dual-model architecture: Qwen3-8B generates counterexample candidates while DeepSeek-Prover-V2-7B constructs the formal proofs. A combined reward score `r = alpha * I(dropped-hypothesis proof) + (1-alpha) * I(mutated-statement proof)` (with alpha = 0.8) weights training examples for supervised fine-tuning. The easier dropped-hypothesis reward activates more frequently, providing a learning signal even when the model cannot yet solve the harder full disproof, creating a curriculum-like effect. Training ran for 56 iterations of 10K examples each over one epoch.

**Benchmarks and Results.** The authors introduce three new benchmarks: *For-Counter* (1,058 problems formalized from CounterMath), *Veri-Formalize* (3,000 unprovable formalization problems), and *Veri-Reason* (3,000 problems from failed proof attempts). On For-Counter at Pass@1, the system solves 222 problems -- a **74% improvement** over the strongest baseline (127). Gains on Veri-Reason and Veri-Formalize are 47% and 56% respectively at Pass@1. The multi-reward approach also outperforms single-reward ablations (49% vs. 43% Pass@1 on validation).

**Connection to Verification Training Signals.** The formal counterexamples close a feedback loop: Lean 4 verification of both the mutated-statement and dropped-hypothesis proofs generates dual reward signals that directly refine the model via weighted SFT. This means counterexamples are not just end products but serve as verifiable training signals -- correct counterexamples with machine-checked proofs become high-weight training data, enabling the model to progressively tackle harder disproof tasks. This paradigm demonstrates that formal refutation can complement formal proof as a scalable, automatically verified supervision source for mathematical reasoning.

**Note:** The paper was initially submitted to ICLR 2026 (September 2025) and later withdrawn; the arXiv version (March 2026) appears to be a revised posting.

Sources:
- [arXiv Abstract Page](https://arxiv.org/abs/2603.19514)
- [arXiv HTML Full Paper](https://arxiv.org/html/2603.19514v1)
- [OpenReview Submission](https://openreview.net/forum?id=EBa52sye9K)

agentId: ac834b3e9f20d97fe (use SendMessage with to: 'ac834b3e9f20d97fe' to continue this agent)
&lt;usage>total_tokens: 14555
tool_uses: 6
duration_ms: 59685&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "987960c0-986b-4bcf-a401-1fca0c52ddcc",
  "isSidechain": false,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "type": "user",
  "uuid": "65f3775f-33e4-44e9-81de-e6dcd4ef2ac0",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the paper \"Learning to Disprove: Formal Counterexample Generation with Large Language Models\" (arXiv 2603.19514, March 2026). \n\nPlease:\n1. Search the web for \"Learning to Disprove formal counterexample generation LLM arXiv 2603.19514\"\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2603.19514\n3. Search for any related discussions\n\nI need: the full title, authors, key methodology (symbolic mutation strategy, how they train LLMs to generate formal counterexamples in Lean 4), their results, scale of counterexample generation, and how this relates to using formal counterexamples as training signals for verification. Report in detail (300-500 words).",
    "agentId": "ac834b3e9f20d97fe",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the detailed report on the paper.\n\n---\n\n**Title:** Learning to Disprove: Formal Counterexample Generation with Large Language Models\n\n**Authors:** Zenan Li, Zhaoyu Li, Kaiyu Yang, Xiaoxing Ma, and Zhendong Su (ETH Zurich, University of Toronto, MiroMind, Nanjing University)\n\n**arXiv ID:** 2603.19514 (submitted March 19, 2026)\n\n**Core Motivation and Problem.** Current AI-for-mathematics research overwhelmingly targets proof construction -- proving true statements. This paper addresses the neglected complementary skill: discovering counterexamples to disprove false statements. The authors formalize the task as *formal counterexample generation*, requiring an LLM not only to propose a concrete counterexample but also to produce a machine-checkable proof in the Lean 4 theorem prover that the counterexample indeed invalidates the claim.\n\n**Symbolic Mutation Strategy.** The key data-synthesis innovation is a three-step symbolic mutation pipeline. Starting from a formally proved theorem of the form `forall x, H1(x) -> H2(x) -> C(x)`, the method (1) analyzes the original proof trace to identify which hypotheses are necessary, (2) discards one essential hypothesis (e.g., H1), producing a mutated -- now false -- statement `H2(x) -> C(x)`, and (3) verifies via Lean 4 that the mutation is indeed invalid. This yields two companion tasks: find an x* satisfying the remaining hypothesis path, and show that x* violates the dropped hypothesis. Applied to four theorem sources (Mathlib, Lean Workbook, MiniF2F, PutnamBench), the strategy produced **575,039 counterexample instances from 321,929 seed theorems**, at an average rate of 0.3--0.7 seconds per theorem.\n\n**Multi-Reward Expert Iteration.** Training uses a dual-model architecture: Qwen3-8B generates counterexample candidates while DeepSeek-Prover-V2-7B constructs the formal proofs. A combined reward score `r = alpha * I(dropped-hypothesis proof) + (1-alpha) * I(mutated-statement proof)` (with alpha = 0.8) weights training examples for supervised fine-tuning. The easier dropped-hypothesis reward activates more frequently, providing a learning signal even when the model cannot yet solve the harder full disproof, creating a curriculum-like effect. Training ran for 56 iterations of 10K examples each over one epoch.\n\n**Benchmarks and Results.** The authors introduce three new benchmarks: *For-Counter* (1,058 problems formalized from CounterMath), *Veri-Formalize* (3,000 unprovable formalization problems), and *Veri-Reason* (3,000 problems from failed proof attempts). On For-Counter at Pass@1, the system solves 222 problems -- a **74% improvement** over the strongest baseline (127). Gains on Veri-Reason and Veri-Formalize are 47% and 56% respectively at Pass@1. The multi-reward approach also outperforms single-reward ablations (49% vs. 43% Pass@1 on validation).\n\n**Connection to Verification Training Signals.** The formal counterexamples close a feedback loop: Lean 4 verification of both the mutated-statement and dropped-hypothesis proofs generates dual reward signals that directly refine the model via weighted SFT. This means counterexamples are not just end products but serve as verifiable training signals -- correct counterexamples with machine-checked proofs become high-weight training data, enabling the model to progressively tackle harder disproof tasks. This paradigm demonstrates that formal refutation can complement formal proof as a scalable, automatically verified supervision source for mathematical reasoning.\n\n**Note:** The paper was initially submitted to ICLR 2026 (September 2025) and later withdrawn; the arXiv version (March 2026) appears to be a revised posting.\n\nSources:\n- [arXiv Abstract Page](https://arxiv.org/abs/2603.19514)\n- [arXiv HTML Full Paper](https://arxiv.org/html/2603.19514v1)\n- [OpenReview Submission](https://openreview.net/forum?id=EBa52sye9K)"
      }
    ],
    "totalDurationMs": 59685,
    "totalTokens": 14555,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 190,
      "cache_creation_input_tokens": 1535,
      "cache_read_input_tokens": 11794,
      "output_tokens": 1036,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1535
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 190,
          "output_tokens": 1036,
          "cache_read_input_tokens": 11794,
          "cache_creation_input_tokens": 1535,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1535,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 6
    }
  },
  "sourceToolAssistantUUID": "987960c0-986b-4bcf-a401-1fca0c52ddcc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T20:25:05.323Z_

<details><summary>↩ Tool result · `toolu_015tDsY6xGc7cun81wxEevRc`</summary>

```text
Here is the research report:

---

**The Value Proposition of Formally Traceable Mathematical Error Explanations for Safety-Critical Applications and PRM Interpretability**

**Safety-Critical Applications: Why "Wrong" Is Not Enough.** In domains like finance, medicine, and engineering, knowing *that* a reasoning step failed is far less valuable than knowing *why* it failed. The "Safe" framework (2025) demonstrates this by translating each mathematical reasoning step into Lean 4 formal language and generating machine-checkable proofs, providing interpretable and verifiable evidence of correctness rather than opaque binary judgments. This contrasts sharply with current PRMs and self-consistency methods, which "operate as opaque boxes and do not provide checkable evidence for their judgments." Formal verification has long been standard in aerospace (flight control software), automotive (ISO 26262 for airbag controllers), and semiconductor design. As AI reasoning enters these domains, the same rigor is demanded. A recent systematic literature review in *Frontiers in AI* (2026) and work on AgentVerify (2026) both emphasize that formal methods -- model checking, theorem proving, abstract interpretation -- are essential for detecting vulnerabilities and unintended behaviors in AI systems deployed in high-stakes settings.

**PRM Interpretability and Debugging.** Current PRMs suffer from well-documented failure modes: they "latch onto shallow consistency cues rather than learning true causal reasoning structures" and "often overcredit incorrect steps, yielding high false positive rates." PathFinder-PRM addresses this by introducing hierarchical error typing -- explicitly categorizing errors into math vs. consistency categories before estimating step optimality -- which decouples error detection from reward assignment and yields enhanced interpretability. The LEMMA framework and ErrorAtlas taxonomy further demonstrate that fine-grained error categorization reveals "not just where, but *why* models go wrong -- a level of granularity not attainable with standard benchmarks alone." Error categories such as question misinterpretation, calculation error, circular logic, and step inconsistency provide actionable debugging signals that binary correct/incorrect labels cannot.

**Alignment and Reward Hacking Prevention.** Anthropic's 2025 paper on "Natural Emergent Misalignment from Reward Hacking in Production RL" and a comprehensive 2026 survey document how reward hacking exploits faithfulness bias and chain-of-thought hacking. Process supervision is intended to mitigate this by scoring intermediate steps, but when PRMs themselves are unfaithful, the problem compounds. Formally traceable error explanations create an auditable chain: if a PRM penalizes a step, the formal trace shows *which mathematical property* was violated, making reward hacking detectable. The FUR framework measures faithfulness by erasing reasoning steps from model parameters, but formal traces offer a more direct path -- grounding reward signals in checkable mathematical claims rather than learned heuristics.

**Training Data Quality: The GSM8K Foundation.** A 2025 paper on "Generalizable Process Reward Models via Formally Verified Training Data" directly addresses this, using Isabelle to formally verify GSM8K-level solutions and annotate step-level error labels. The core bottleneck for PRMs remains "obtaining fine-grained step-level annotations" -- PRM800K required human experts to label 75K questions. Formal verification tools can automate this annotation with mathematical guarantees, and recent work like ACTPRM achieves state-of-the-art performance with only 20% of annotation costs. Since GSM8K-level arithmetic is the foundation upon which more complex PRM training is built, ensuring this foundation is formally verified prevents error propagation into harder mathematical domains.

---

Sources:
- [Safe: Step-aware Formal Verification for Math LLMs](https://arxiv.org/abs/2506.04592)
- [A Survey of Process Reward Models](https://arxiv.org/html/2510.08049v3)
- [Generalizable PRMs via Formally Verified Training Data](https://arxiv.org/pdf/2505.15960)
- [Error Typing for Smarter Rewards: PathFinder-PRM](https://arxiv.org/pdf/2505.19706)
- [Reward Hacking in the Era of Large Models](https://arxiv.org/html/2604.13602v1)
- [Natural Emergent Misalignment from Reward Hacking (Anthropic)](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf)
- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/html/2503.21295v1)
- [Reward Modeling for RL-Based LLM Survey](https://arxiv.org/pdf/2602.09305)
- [LEMMA: Learning from Errors for Mathematical Advancement](https://arxiv.org/html/2503.17439v2)
- [Formal Methods for Safety-Critical ML (Frontiers, 2026)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1749956/full)
- [Pitfalls of Rule- and Model-based Verifiers](https://arxiv.org/html/2505.22203v1)
- [Formal Verification in AI and Why It Matters](https://predictablemachines.com/blog/formal-verification-in-ai-and-why-it-matters/)
- [Emergent Formal Verification Across Six Domains](https://arxiv.org/abs/2603.21149)
- [Proof-RM: Scalable Reward Model for Math Proof](https://arxiv.org/pdf/2602.02377)
- [The Lessons of Developing Process Reward Models](https://arxiv.org/pdf/2501.07301)

agentId: a8c1834e61c6879dc (use SendMessage with to: 'a8c1834e61c6879dc' to continue this agent)
&lt;usage>total_tokens: 16072
tool_uses: 7
duration_ms: 55462&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "490f3231-82fa-4315-bfdd-363f8d0e6614",
  "isSidechain": false,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "type": "user",
  "uuid": "d089e9e6-8d9e-401b-b1b8-7db278803a79",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the value proposition of formally traceable mathematical error explanations for safety-critical applications and PRM interpretability. This is for a research paper about process reward models (PRMs) that verify math reasoning steps.\n\nPlease search for:\n1. \"safety-critical math verification\" OR \"trustworthy mathematical reasoning\" OR \"interpretable reward model\"\n2. \"process reward model interpretability\" OR \"PRM debugging\" OR \"reward model faithfulness safety\"\n3. \"formal verification AI safety\" OR \"verifiable AI reasoning\" applications in critical domains\n4. Any recent papers (2025-2026) on reward model faithfulness for alignment/safety\n\nI'm looking for arguments and evidence that formally traceable error explanations in mathematical reasoning are valuable BEYOND just improving accuracy — specifically for:\n- Safety-critical applications (finance, engineering, medicine) where knowing WHY a step is wrong matters\n- PRM interpretability/debugging (understanding failure modes of reward models)\n- Alignment: preventing reward hacking by ensuring the reward signal is faithful\n- Training data quality: GSM8K-level problems as the foundation for all PRM training data\n\nReport any relevant papers, arguments, or evidence in 400-600 words.",
    "agentId": "a8c1834e61c6879dc",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is the research report:\n\n---\n\n**The Value Proposition of Formally Traceable Mathematical Error Explanations for Safety-Critical Applications and PRM Interpretability**\n\n**Safety-Critical Applications: Why \"Wrong\" Is Not Enough.** In domains like finance, medicine, and engineering, knowing *that* a reasoning step failed is far less valuable than knowing *why* it failed. The \"Safe\" framework (2025) demonstrates this by translating each mathematical reasoning step into Lean 4 formal language and generating machine-checkable proofs, providing interpretable and verifiable evidence of correctness rather than opaque binary judgments. This contrasts sharply with current PRMs and self-consistency methods, which \"operate as opaque boxes and do not provide checkable evidence for their judgments.\" Formal verification has long been standard in aerospace (flight control software), automotive (ISO 26262 for airbag controllers), and semiconductor design. As AI reasoning enters these domains, the same rigor is demanded. A recent systematic literature review in *Frontiers in AI* (2026) and work on AgentVerify (2026) both emphasize that formal methods -- model checking, theorem proving, abstract interpretation -- are essential for detecting vulnerabilities and unintended behaviors in AI systems deployed in high-stakes settings.\n\n**PRM Interpretability and Debugging.** Current PRMs suffer from well-documented failure modes: they \"latch onto shallow consistency cues rather than learning true causal reasoning structures\" and \"often overcredit incorrect steps, yielding high false positive rates.\" PathFinder-PRM addresses this by introducing hierarchical error typing -- explicitly categorizing errors into math vs. consistency categories before estimating step optimality -- which decouples error detection from reward assignment and yields enhanced interpretability. The LEMMA framework and ErrorAtlas taxonomy further demonstrate that fine-grained error categorization reveals \"not just where, but *why* models go wrong -- a level of granularity not attainable with standard benchmarks alone.\" Error categories such as question misinterpretation, calculation error, circular logic, and step inconsistency provide actionable debugging signals that binary correct/incorrect labels cannot.\n\n**Alignment and Reward Hacking Prevention.** Anthropic's 2025 paper on \"Natural Emergent Misalignment from Reward Hacking in Production RL\" and a comprehensive 2026 survey document how reward hacking exploits faithfulness bias and chain-of-thought hacking. Process supervision is intended to mitigate this by scoring intermediate steps, but when PRMs themselves are unfaithful, the problem compounds. Formally traceable error explanations create an auditable chain: if a PRM penalizes a step, the formal trace shows *which mathematical property* was violated, making reward hacking detectable. The FUR framework measures faithfulness by erasing reasoning steps from model parameters, but formal traces offer a more direct path -- grounding reward signals in checkable mathematical claims rather than learned heuristics.\n\n**Training Data Quality: The GSM8K Foundation.** A 2025 paper on \"Generalizable Process Reward Models via Formally Verified Training Data\" directly addresses this, using Isabelle to formally verify GSM8K-level solutions and annotate step-level error labels. The core bottleneck for PRMs remains \"obtaining fine-grained step-level annotations\" -- PRM800K required human experts to label 75K questions. Formal verification tools can automate this annotation with mathematical guarantees, and recent work like ACTPRM achieves state-of-the-art performance with only 20% of annotation costs. Since GSM8K-level arithmetic is the foundation upon which more complex PRM training is built, ensuring this foundation is formally verified prevents error propagation into harder mathematical domains.\n\n---\n\nSources:\n- [Safe: Step-aware Formal Verification for Math LLMs](https://arxiv.org/abs/2506.04592)\n- [A Survey of Process Reward Models](https://arxiv.org/html/2510.08049v3)\n- [Generalizable PRMs via Formally Verified Training Data](https://arxiv.org/pdf/2505.15960)\n- [Error Typing for Smarter Rewards: PathFinder-PRM](https://arxiv.org/pdf/2505.19706)\n- [Reward Hacking in the Era of Large Models](https://arxiv.org/html/2604.13602v1)\n- [Natural Emergent Misalignment from Reward Hacking (Anthropic)](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf)\n- [R-PRM: Reasoning-Driven Process Reward Modeling](https://arxiv.org/html/2503.21295v1)\n- [Reward Modeling for RL-Based LLM Survey](https://arxiv.org/pdf/2602.09305)\n- [LEMMA: Learning from Errors for Mathematical Advancement](https://arxiv.org/html/2503.17439v2)\n- [Formal Methods for Safety-Critical ML (Frontiers, 2026)](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1749956/full)\n- [Pitfalls of Rule- and Model-based Verifiers](https://arxiv.org/html/2505.22203v1)\n- [Formal Verification in AI and Why It Matters](https://predictablemachines.com/blog/formal-verification-in-ai-and-why-it-matters/)\n- [Emergent Formal Verification Across Six Domains](https://arxiv.org/abs/2603.21149)\n- [Proof-RM: Scalable Reward Model for Math Proof](https://arxiv.org/pdf/2602.02377)\n- [The Lessons of Developing Process Reward Models](https://arxiv.org/pdf/2501.07301)"
      }
    ],
    "totalDurationMs": 55462,
    "totalTokens": 16072,
    "totalToolUseCount": 7,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1619,
      "cache_read_input_tokens": 13064,
      "output_tokens": 1388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1619
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1388,
          "cache_read_input_tokens": 13064,
          "cache_creation_input_tokens": 1619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1619,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 7
    }
  },
  "sourceToolAssistantUUID": "490f3231-82fa-4315-bfdd-363f8d0e6614",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",   \"core_pr…",
  "leafUuid": "d089e9e6-8d9e-401b-b1b8-7db278803a79",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise formal PRM rationale proposal with R-PRM baseline correction",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Tool result

_source line 17 · 2026-05-27T20:25:07.037Z_

<details><summary>↩ Tool result · `toolu_01UkmnWRLDQGDqtQhTRS1Px7`</summary>

```text
Here is my detailed report on the StepProof paper.

---

**Full Title:** "StepProof: Step-by-step verification of natural language mathematical proofs"

**Authors:** Xiaolin Hu, Qinghua Zhou, Bogdan Grechuk, Ivan Y. Tyukin

**arXiv ID:** 2506.10558 (v1: June 12, 2025; v2: June 30, 2025). Subject areas: Logic in Computer Science (cs.LO), Artificial Intelligence (cs.AI).

**Methodology.** StepProof addresses a core limitation of existing autoformalization: conventional methods attempt to formalize and verify an entire proof monolithically, offering only binary pass/fail feedback. StepProof instead treats each sentence in a natural-language proof as a verifiable sub-proposition. The system decomposes the informal proof into individual steps, then uses an LLM (Llama3 8B-Instruct, with single-example few-shot prompting at temperature 0.3) to translate each step into Isabelle/HOL. Each formalized step is verified individually by Isabelle2024 (using only the Main library). Crucially, the proof state is managed incrementally: when a step succeeds, both the formalized output and the original informal content are packaged as input context for the next step, maintaining a cumulative proof stack. When a step fails, the system can backtrack -- retaining all previously verified steps and clearing only the erroneous one. The per-step token budget is 256 (versus 1024 for full-proof baselines), which reduces output noise. The Isabelle integration uses "isabelle-client" as a service proxy to the Isabelle2024 prover, running on a single NVIDIA A4000 16GB GPU.

**Results on GSM8K.** GSM8K problems average 4-5 proof steps each. In head-to-head comparison, StepProof achieves a 6.10% single-attempt proof pass rate versus 5.30% for the full-proof strategy (a 15.1% relative improvement). Formalization time drops 38.9% (5.83s vs. 9.54s per problem), and proof checking time improves 39.5% (130s vs. 215s). With 10 attempts, StepProof reaches a 27.9% proof passing rate, outperforming the "Don't Trust: Verify" baseline at 25.3% (which uses 64 attempts) and majority voting at 16.2% (also 64 attempts). A step-level metric shows 38.1% of proofs achieve at least 50% step completion after 10 attempts.

**Engineering Insights on Isabelle Proof State.** The incremental architecture is the key engineering contribution. Rather than submitting a complete formal proof to Isabelle and receiving a single verdict, StepProof maintains a running proof context that accumulates verified lemmas/steps. This enables fine-grained error localization and selective backtracking. The interactive interface uses a color-coded scheme: green (verified), yellow (suspended but assumed true for forward progress), and unmarked (failed). The yellow "suspension" mechanism is notable -- it allows the system to skip a hard-to-formalize step while preserving the proof context, then return to it later.

**Relationship to Process Reward Models.** StepProof's step-level pass rate metric (the proportion of verified steps, not just binary proof success) provides exactly the kind of granular supervision signal that Process Reward Models (PRMs) need. The closely related work "FoVer: Efficient PRM Training Data Synthesis via Formal Verification" (arXiv 2505.15960, Kamoi et al.) makes this connection explicit: it uses formal verification tools (Z3, Isabelle) to automatically generate step-level correctness labels for training PRMs, eliminating the need for expensive human annotation. StepProof's decomposition-and-verify paradigm could serve as a data generation pipeline for PRMs -- each step's verification outcome is a ground-truth label for whether that reasoning step is correct. The key distinction is that StepProof targets inference-time verification (checking proofs as they are written), while FoVer targets training-time data synthesis, but the underlying mechanism of step-level formal verification is shared.

Sources:
- [StepProof on arXiv](https://arxiv.org/abs/2506.10558)
- [StepProof HTML version](https://arxiv.org/html/2506.10558v2)
- [Quantum Zeitgeist coverage](https://quantumzeitgeist.com/ai-verifies-mathematical-proofs-step-by-step-improving-formal-verification-success/)
- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)
- [StepProof on ResearchGate](https://www.researchgate.net/publication/392628910_StepProof_Step-by-step_verification_of_natural_language_mathematical_proofs)
- [StepProof on OpenReview](https://openreview.net/pdf?id=EXaKfdsw04)

agentId: a8303300378f7528f (use SendMessage with to: 'a8303300378f7528f' to continue this agent)
&lt;usage>total_tokens: 15579
tool_uses: 8
duration_ms: 65969&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c67235cc-e857-4c80-b722-94993994e470",
  "isSidechain": false,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "type": "user",
  "uuid": "7e7ff689-7adf-4149-83e2-860851bee500",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the paper \"StepProof\" (arXiv 2506.10558) which performs step-by-step Isabelle-based autoformalization and verification on GSM8K. \n\nPlease:\n1. Search the web for \"StepProof arXiv 2506.10558 Isabelle GSM8K step-by-step\"\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2506.10558\n3. Search for any related discussions or citations\n\nI need: the full title, authors, key methodology (how they do step-by-step Isabelle verification), their results on GSM8K, any engineering insights about Isabelle proof state handling, and how this relates to formal verification for process reward models. Report in detail (300-500 words).",
    "agentId": "a8303300378f7528f",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my detailed report on the StepProof paper.\n\n---\n\n**Full Title:** \"StepProof: Step-by-step verification of natural language mathematical proofs\"\n\n**Authors:** Xiaolin Hu, Qinghua Zhou, Bogdan Grechuk, Ivan Y. Tyukin\n\n**arXiv ID:** 2506.10558 (v1: June 12, 2025; v2: June 30, 2025). Subject areas: Logic in Computer Science (cs.LO), Artificial Intelligence (cs.AI).\n\n**Methodology.** StepProof addresses a core limitation of existing autoformalization: conventional methods attempt to formalize and verify an entire proof monolithically, offering only binary pass/fail feedback. StepProof instead treats each sentence in a natural-language proof as a verifiable sub-proposition. The system decomposes the informal proof into individual steps, then uses an LLM (Llama3 8B-Instruct, with single-example few-shot prompting at temperature 0.3) to translate each step into Isabelle/HOL. Each formalized step is verified individually by Isabelle2024 (using only the Main library). Crucially, the proof state is managed incrementally: when a step succeeds, both the formalized output and the original informal content are packaged as input context for the next step, maintaining a cumulative proof stack. When a step fails, the system can backtrack -- retaining all previously verified steps and clearing only the erroneous one. The per-step token budget is 256 (versus 1024 for full-proof baselines), which reduces output noise. The Isabelle integration uses \"isabelle-client\" as a service proxy to the Isabelle2024 prover, running on a single NVIDIA A4000 16GB GPU.\n\n**Results on GSM8K.** GSM8K problems average 4-5 proof steps each. In head-to-head comparison, StepProof achieves a 6.10% single-attempt proof pass rate versus 5.30% for the full-proof strategy (a 15.1% relative improvement). Formalization time drops 38.9% (5.83s vs. 9.54s per problem), and proof checking time improves 39.5% (130s vs. 215s). With 10 attempts, StepProof reaches a 27.9% proof passing rate, outperforming the \"Don't Trust: Verify\" baseline at 25.3% (which uses 64 attempts) and majority voting at 16.2% (also 64 attempts). A step-level metric shows 38.1% of proofs achieve at least 50% step completion after 10 attempts.\n\n**Engineering Insights on Isabelle Proof State.** The incremental architecture is the key engineering contribution. Rather than submitting a complete formal proof to Isabelle and receiving a single verdict, StepProof maintains a running proof context that accumulates verified lemmas/steps. This enables fine-grained error localization and selective backtracking. The interactive interface uses a color-coded scheme: green (verified), yellow (suspended but assumed true for forward progress), and unmarked (failed). The yellow \"suspension\" mechanism is notable -- it allows the system to skip a hard-to-formalize step while preserving the proof context, then return to it later.\n\n**Relationship to Process Reward Models.** StepProof's step-level pass rate metric (the proportion of verified steps, not just binary proof success) provides exactly the kind of granular supervision signal that Process Reward Models (PRMs) need. The closely related work \"FoVer: Efficient PRM Training Data Synthesis via Formal Verification\" (arXiv 2505.15960, Kamoi et al.) makes this connection explicit: it uses formal verification tools (Z3, Isabelle) to automatically generate step-level correctness labels for training PRMs, eliminating the need for expensive human annotation. StepProof's decomposition-and-verify paradigm could serve as a data generation pipeline for PRMs -- each step's verification outcome is a ground-truth label for whether that reasoning step is correct. The key distinction is that StepProof targets inference-time verification (checking proofs as they are written), while FoVer targets training-time data synthesis, but the underlying mechanism of step-level formal verification is shared.\n\nSources:\n- [StepProof on arXiv](https://arxiv.org/abs/2506.10558)\n- [StepProof HTML version](https://arxiv.org/html/2506.10558v2)\n- [Quantum Zeitgeist coverage](https://quantumzeitgeist.com/ai-verifies-mathematical-proofs-step-by-step-improving-formal-verification-success/)\n- [FoVer: Efficient PRM Training Data Synthesis via Formal Verification](https://arxiv.org/abs/2505.15960)\n- [StepProof on ResearchGate](https://www.researchgate.net/publication/392628910_StepProof_Step-by-step_verification_of_natural_language_mathematical_proofs)\n- [StepProof on OpenReview](https://openreview.net/pdf?id=EXaKfdsw04)"
      }
    ],
    "totalDurationMs": 65969,
    "totalTokens": 15579,
    "totalToolUseCount": 8,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 795,
      "cache_read_input_tokens": 13560,
      "output_tokens": 1223,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 795
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1223,
          "cache_read_input_tokens": 13560,
          "cache_creation_input_tokens": 795,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 795,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 8
    }
  },
  "sourceToolAssistantUUID": "c67235cc-e857-4c80-b722-94993994e470",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 18 · 2026-05-27T20:26:03.757Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the research results. Let me synthesize:

**StepProof** (arXiv 2506.10558, June 2025):
- Step-by-step Isabelle verification on GSM8K
- Achieves 6.10% single-attempt proof pass rate (vs 5.30% for full-proof)
- 27.9% with 10 attempts
- Key engineering insight: incremental proof state accumulation, color-coded verification status, "suspension" mechanism for hard steps
- Directly relevant to our Isabelle proof state extraction in Phase 1


- **Learning to Disprove** (arXiv 2603.19514, March 2026) takes a complementary approach by training models to generate formal counterexamples in Lean 4 through symbolic mutation, achieving 74% improvement over baselines with multi-reward expert iteration—this connects to using formal counterexamples as training signals. The safety argument here is that interpretable verification evidence beats opaque binary judgments, which PathFinder-PRM addresses through hierarchical error typing.

Now I'm seeing the core issue: the current framing limits impact because it's positioned as "formally grounded rationales on easy domains," but the real contribution is demonstrating that formal proof artifacts can serve as ground-truth supervision for verifying rationale faithfulness. That's a stronger value proposition—establishing the first methodology for producing verifiably faithful verification rationales with applications beyond just accuracy improvement.

The three practical applications reframe the "easy domain" limitation as actually a strength: PRM diagnostics and debugging benefit from having a reference standard for measuring rationale faithfulness across all PRMs, safety-critical deployment needs auditable reasoning on exactly these kinds of arithmetic problems, and GSM8K-level rationale faithfulness prevents corrupted supervision signals from cascading through the entire training pipeline. This positions the work as improving the foundation and enabling deployment in contexts where explainability is legally required.

Now I'm considering what methodological precedents to draw on — StepProof's incremental proof state management directly applies to the Phase 1 Isabelle work, and Learning to Disprove's 575K counterexamples show that formal counterexample generation can scale. I should revise the proposal substantially by reframing the core problem and opportunity around these three value propositions rather than transfer, fix the R-PRM baseline, add those two papers to the landscape, and strengthen the impact argument throughout. This warrants a major revision since I'm fundamentally reshaping how the contribution is positioned.

Let me draft this carefully, preserving the existing content while reframing formal grounding as inherently valuable, integrating the new references meaningfully, correcting the baseline from 58.5 to 56.5, and making the training data origin argument more central. I should also double-check the math: 70.4 - 56.5 = 13.9, which is correct for the improvement gap.

The key reframing is shifting from "can we train PRMs with formally grounded rationales?" to "can formal proof artifacts serve as ground-truth supervision for PRM rationale faithfulness?"

—which opens up three distinct value propositions: enabling verifiably faithful error explanations for safety-critical domains like finance and medicine, providing a reference standard for measuring any PRM's faithfulness, and establishing GSM8K as the foundation where faithful rationales improve everything downstream. I'm also considering whether a Phase 4(C) experiment specifically evaluating safety-critical use cases—showing that formally grounded rationales provide actionable debugging information—would strengthen the argument that formal grounding has inherent value beyond just transfer learning.

Actually, the stronger methodological contribution is to use our formally grounded rationales as a diagnostic framework for evaluating other PRMs. When Z3 or Isabelle proves a step wrong with a specific counterexample, we have ground truth for what the error is, and we can measure whether other PRMs like ThinkPRM or GenPRM correctly identify that same error in their rationales. This gives us a new metric—error identification precision—that measures whether a PRM's rationale pinpoints the mathematical error that formal verification identifies, providing the first scalable way to evaluate PRM rationale quality beyond just accuracy.

I should be strategic about the revision scope since the reviewer already confirmed the landscape is solid and critical issues are resolved. The main gap is impact framing, so I'll focus on substantially rewriting the core problem and opportunity sections to emphasize inherent value, add a Phase 4 diagnostic benchmark experiment, fix the minor issues like the R-PRM numbers and new papers, and keep everything else largely as is. This warrants a major change type given how much the framing shifts.

Writing the revised JSON now...

For the description field, I need to weave together the three inherent value propositions, incorporate the StepProof and Learning to Disprove references, fix the R-PRM baseline, and articulate the diagnostic benchmark contribution and safety-critical angle.

StepProof's 27.9% proof pass rate on GSM8K is lower than it might seem because they're proving entire solutions rather than just extracting proof states at failure points like we're doing, and their incremental proof state management directly informs our Phase 1(b) Isabelle work and reduces engineering risk. Learning to Disprove's scale of 575K counterexamples from 321K seed theorems is compelling, though they use Lean 4 instead of Z3/Isabelle, but the core insight about formal counterexamples as training signals parallels our approach.

Now I'm finalizing the plan and structuring the JSON around the major revisions: reframing the core problem from "can we train PRMs with formally grounded rationales" to "can formal proof artifacts serve as ground-truth supervision for PRM rationale faithfulness with three applications beyond accuracy," foregrounding the three inherent-value propositions around safety-critical deployment, PRM diagnostics, and training data integrity, and adding Phase 4(C) as a formal faithfulness diagnostic using Z3 counterexamples.

Writing the JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7e7ff689-7adf-4149-83e2-860851bee500",
  "isSidechain": false,
  "requestId": "req_011CbThaN3CtevPSgPYDLqtc",
  "type": "assistant",
  "uuid": "67c7af66-50e9-46eb-bec7-3d1b7ea9baa8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgvwfZad2hbcLtpbq73VSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2621,
      "cache_creation_input_tokens": 3182,
      "cache_read_input_tokens": 25531,
      "output_tokens": 16639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2621,
          "output_tokens": 16639,
          "cache_read_input_tokens": 25531,
          "cache_creation_input_tokens": 3182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3182
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

_source line 19 · 2026-05-27T20:26:09.820Z_

Now let me think deeply about the revision strategy before writing the output.

The research reveals:

1. **StepProof**: Step-by-step Isabelle verification on GSM8K with incremental proof state management — directly relevant engineering precedent for our Phase 1(b). Achieves 27.9% proof pass rate (10 attempts), with key insight of accumulative proof state + suspension mechanism for hard steps.

2. **Learning to Disprove**: 575K formal counterexamples from 321K seed theorems via symbolic mutation in Lean 4. Demonstrates scalable formal counterexample generation. Multi-reward expert iteration training. Conceptual parallel to our Z3 counterexample extraction.

3. **Safety/interpretability arguments**: Strong evidence that formally traceable error explanations have inherent value for safety-critical deployment, PRM diagnostics, and reward hacking prevention — independent of domain difficulty.

The fundamental insight is that the score is stuck at 3.75 because the proposal **apologizes** for easy-domain scope rather than **owning** it as inherently valuable. A **major reframing** is warranted — same method, but reshaped contribution that makes easy-domain formal grounding a feature, not a limitation. I'll add a diagnostic benchmark contribution (using formal proof artifacts as ground-truth error specifications to evaluate ANY PRM's rationale quality) and foreground safety-critical applications.

Let me now produce the complete revised proposal:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67c7af66-50e9-46eb-bec7-3d1b7ea9baa8",
  "isSidechain": false,
  "requestId": "req_011CbThaN3CtevPSgPYDLqtc",
  "type": "assistant",
  "uuid": "22875224-384a-4246-831e-277b27e54a73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgvwfZad2hbcLtpbq73VSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2621,
      "cache_creation_input_tokens": 3182,
      "cache_read_input_tokens": 25531,
      "output_tokens": 16639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2621,
          "output_tokens": 16639,
          "cache_read_input_tokens": 25531,
          "cache_creation_input_tokens": 3182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3182
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

_source line 20 · 2026-05-27T20:31:59.283Z_

<details open><summary>🔧 Tool call — Write · `toolu_01CVs3DjTz8NuLcTZCXY4guw`</summary>

```json
{
  "file_path": "/tmp/revised_proposal_round7.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs: Proof Artifacts as Ground-Truth Supervision for Verifiable Error Explanations\",\n  \"core_problem\": \"Generative PRMs (ThinkPRM, GenPRM, R-PRM) produce CoT verification rationales, but R-Align (Feb 2026) shows existing GenRMs exhibit substantial Spurious Correctness -- label-correct decisions with misaligned rationales -- and 'Outcome Accuracy is Not Enough' finds approximately 40% rationale consistency with human judgments. R-PRM demonstrates that reasoning-driven evaluation substantially improves accuracy (+13.9 F1 on ProcessBench), yet even rich multi-dimensional reasoning analyses lack formal grounding and have unknown faithfulness. More fundamentally, there is no scalable ground-truth methodology for evaluating WHETHER a PRM's rationale correctly identifies the actual mathematical error: human evaluation doesn't scale, LLM-as-judge achieves only 65-77 F1 for detecting unfaithfulness (FaithCoT-Bench), and existing automated metrics (S-Corr, MetaJudge) rely on reference annotations unavailable for most domains. Can we use formal proof artifacts -- Z3 counterexamples, Isabelle proof state information -- both as training supervision for faithful rationale generation AND as ground-truth error specifications for evaluating rationale quality across any PRM, establishing a methodology that is inherently valuable on foundational domains regardless of transfer to harder problems?\",\n  \"opportunity\": \"The field faces a measurement problem alongside a training problem: we lack ground-truth for what constitutes a faithful PRM rationale. GenRM reviewer 3 raised the unresolved concern that CoT rationales may be 'plausible-sounding but unfaithful reasoning that happens to correlate with correct verdicts.' But detecting this requires knowing what the ACTUAL error is -- which formal verification uniquely provides. FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can generate step-level error labels transferring across 12 benchmarks, but FoVer explicitly restricts to classification-based PRMs producing only binary labels, excluding generative/reasoning-based PRMs. R-PRM (EMNLP 2025) shows that reasoning-driven step evaluation -- generating multi-dimensional analyses before judgments -- substantially improves PRM accuracy (+13.9 F1 on ProcessBench via DPO), but its rationales are trained on LLM-generated seed data without formal grounding and faithfulness is not evaluated. ThinkPRM generates rich verification CoTs but trains on synthetic rationales of unknown faithfulness. The untried bridge is extracting structured proof artifacts -- Z3 counterexamples, Isabelle proof state information -- from FoVer's verification pipeline and using them as both (a) grounding signals for ThinkPRM-style rationale generation and (b) ground-truth error specifications for a new diagnostic evaluation methodology. This fills two gaps simultaneously: the training gap (reasoning-driven methods leave rationale faithfulness ungrounded) and the evaluation gap (no scalable automated method exists for measuring whether a PRM's explanation correctly identifies the mathematical error). Three arguments establish the inherent value of this contribution on foundational domains, independent of transfer to harder problems: (1) Safety-critical deployment: GSM8K-level arithmetic IS the domain for financial calculations, engineering computations, and medical dosing -- applications where knowing WHY a step is wrong is legally and operationally required, not just whether it's wrong. Current PRMs provide only opaque scores or unverified rationales for these critical applications. (2) PRM diagnostics and debugging: Formally grounded rationales establish a reference standard for measuring rationale quality across ALL PRMs -- analogous to how PRM800K provides ground-truth step labels, our formally grounded error specifications provide ground-truth explanations, enabling the first automated methodology for evaluating whether any PRM's rationale correctly identifies the actual mathematical error. (3) Training data integrity: GSM8K-level problems are the primary source for PRM training data construction (PRM800K, FoVer, OmegaPRM's 1.5M annotations all derive from or include GSM8K/MATH). Ensuring rationale faithfulness at this foundational level prevents corrupted supervision signals from propagating to all downstream applications -- improving the foundation rather than patching the symptoms. Critically, Faithful Autoformalization (Amrollahi et al., April 2026) has now validated and quantified the roundtrip verification mechanism we adopt for quality filtering, showing 45-66% baseline equivalence rates improvable to 78-86% with standard diagnosis-guided repair or up to 91-95% with cross-model diagnosis -- providing empirical grounding for our data pipeline feasibility. Moreover, FoVer itself demonstrates easy-to-difficult transfer: PRMs trained on GSM8K-level data significantly improve step-level verification on MATH (88.0% vs 78.2% baseline), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%), suggesting that improving rationale faithfulness on foundational domains propagates to harder reasoning tasks -- though we treat this as a secondary hypothesis to test rather than a core claim.\",\n  \"landscape\": \"ThinkPRM (arXiv 2025) achieves 8% improvement on GPQA-Diamond over discriminative verifiers using only 1% of PRM800K labels (specifically 1K synthetic verification CoTs filtered to ~8K step labels), but its rationales lack formal grounding. GenPRM (AAAI 2026) combines CoT with code verification, enabling 1.5B models to outperform GPT-4o on ProcessBench using only 23K training examples. R-PRM (EMNLP 2025) introduces reasoning-driven process reward modeling: it generates multi-dimensional step analyses (Previous Steps Analysis, Now Step Analysis, Data Source Analysis, Consistency Analysis, Calculation Analysis) followed by binary judgments. Using Qwen2.5-Math-7B-Instruct as the base model, R-PRM-7B-DPO achieves 70.4 F1 on ProcessBench (+13.9 over Qwen2.5-Math-7B-PRM800K at 56.5 F1) and +8.5 F1 on PRMBench, with consistent +8.6 accuracy improvements on six downstream math reasoning datasets via best-of-N selection. R-PRM trains on ~289K SFT samples and ~269K DPO pairs bootstrapped from PRM800K annotations, achieving comparable performance to Qwen2.5-Math-PRM with only ~15% of its data volume. Critically, while R-PRM produces rich natural-language reasoning for each step evaluation, it does not evaluate rationale faithfulness -- the analyses are trained on LLM-generated seed data and may exhibit the same spurious correctness that R-Align identifies in other GenRMs. R-PRM demonstrates the ceiling of what reasoning-driven evaluation achieves without formal grounding: substantial accuracy gains, but with unknown rationale fidelity to the actual mathematical errors. FoVer (ACL 2026 Findings) uses Z3/Isabelle for automated step-level labeling with easy-to-difficult transfer (trained on GSM8K-level, evaluates on MATH/AIME/Olympiad), but produces only binary labels and explicitly excludes reasoning-based PRMs citing 'substantially higher computational costs.' FoVer-40K contains 40,000 balanced training steps (20K formal logic from FLDx2 + 20K theorem proving from GSM8K-level problems) with 50% error rate, generated from solutions by Llama 3.1 8B and Qwen 2.5 7B; the raw unbalanced pipeline output is substantially larger (~216K steps from 10K problems per task across both models). 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) is concurrent work that synthesizes PRM training data through a four-stage pipeline: constructing correct symbolic reasoning chains from rule templates, injecting template-aware errors into intermediate steps, symbolically recomputing subsequent steps to maintain trajectory consistency, and verifying that injected errors are not derivable from the prefix. They produce 20K paired (correct, erroneous) trajectories across 11 error types (7 truth-state: drop_condition, implication_misuse, or_and_confusion, partial_evaluation, xor_as_or, xor_as_equiv, vacuous_truth_error; 4 structural: converse_error, redundant_step, missing_prerequisite, circular_reference), translated into natural-language processes for PRM training. Their method improves best-of-8 reranking on logical reasoning benchmarks (Llama-3.1-8B: 0.528 -> 0.591, Qwen-2.5-7B: 0.567 -> 0.615 average F1), with limited transfer to mathematics (ProcessBench GSM8K: 21.2% F1). The key methodological distinction from our work: they generate controlled synthetic errors through template-based injection for accuracy-focused PRM training, while we extract genuine proof artifacts from naturally occurring errors in LLM solutions for faithfulness-focused rationale grounding. Their error diversity is constrained by predefined templates (an acknowledged limitation), while our artifacts reflect the actual distribution of errors that LLMs make. The two approaches are complementary -- their controlled error injection could extend the diversity of training scenarios, while our proof-artifact extraction provides traceable explanations of why each error is wrong. StepProof (arXiv 2506.10558, Hu et al., June 2025) performs step-by-step Isabelle-based autoformalization and verification on GSM8K, achieving 27.9% proof pass rate with 10 attempts (vs. 25.3% for full-proof baselines with 64 attempts). The key engineering contribution is incremental proof state management: verified steps accumulate into context for subsequent steps, failed steps can be selectively backtracked, and a 'suspension' mechanism allows skipping hard-to-formalize steps while preserving proof context. StepProof provides directly relevant engineering precedent for our Phase 1(b) Isabelle proof state extraction -- their interactive interface with color-coded verification status (green=verified, yellow=suspended, unmarked=failed) and accumulative proof stack demonstrate feasibility of fine-grained Isabelle proof state manipulation, though their goal is proof construction rather than proof artifact extraction for rationale grounding. 'Learning to Disprove: Formal Counterexample Generation with Large Language Models' (arXiv 2603.19514, Li et al., March 2026) trains LLMs to generate formal counterexamples verified in Lean 4 via a symbolic mutation strategy, producing 575,039 counterexample instances from 321,929 seed theorems. Their multi-reward expert iteration achieves 74% improvement over baselines on their For-Counter benchmark. While using Lean 4 rather than Z3/Isabelle, the conceptual parallel of using formal counterexamples as verified training signals directly supports our approach. Their scale (575K instances) demonstrates that formal counterexample generation is tractable, and their finding that dual reward signals (dropped-hypothesis proof + mutated-statement proof) improve training efficiency suggests our proof-artifact-grounded rationales may similarly provide richer supervision than binary labels. The key distinction is that they train generators to produce counterexamples, while we extract counterexamples from verification tools to ground verifier rationales. RM-R1 (ICLR 2026) trains reasoning reward models with explicit rationale chains but without formal grounding. R-Align (Feb 2026) introduces the Spurious Correctness (S-Corr) metric showing existing GenRMs exhibit substantial spuriously correct decisions (the abstract reports 'substantial S-Corr even for competitive GenRMs'; specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract), providing the key diagnostic our work aims to improve. 'Outcome Accuracy is Not Enough' (Qwen team, Feb 2026, arXiv 2602.04649) introduces a competing non-formal approach to improving rationale quality: they define Rationale Consistency via MetaJudge, which decomposes human rationales into atomic claims and performs strict one-to-one semantic matching against model justifications, finding frontier GenRMs achieve only ~40% rationale consistency. They train with a multiplicative hybrid signal R_final = R_rationale * R_outcome via GRPO, achieving RM-Bench 87.1% and JudgeBench 82.0% (+5% over outcome-only baselines, +7% on Arena Hard v2 creative writing during RLHF). Crucially, their approach targets Judge faithfulness (evaluation rationale quality) rather than Solver verification, and relies on soft semantic matching against human annotations -- providing broader applicability but weaker guarantees than formal artifact tracing. Their acknowledged limitation is scalability: computing rationale consistency still requires high-quality human annotations. Our formal grounding provides deterministic, traceable guarantees within Z3/Isabelle's decidable scope, while their approach extends to any domain with human annotations. The two methods are complementary: formal grounding where verification tools cover the domain, hybrid consistency training for broader applicability. Think-RM (NeurIPS 2025) shows that deep, long-horizon reasoning inside reward models -- including self-reflection and hypothetical reasoning -- is critical for accurate evaluation, achieving +8% over CoT-GenRMs on RM-Bench. Proof-RM (Feb 2026) provides a scalable pipeline for training reward models on mathematical proof verification with RL stabilization ('LLM-as-a-RM-for-RM'), reaching 82.4% accuracy at 32B on competition-level proofs (IMO/CMO/USAMO), but produces scores rather than formally grounded rationales. Safe (ACL 2025) demonstrates Lean 4 step-level verification of NL math reasoning with the FormalStep benchmark (30,809 formal statements), achieving interpretable verification evidence complementary to PRM scores -- the closest work on formal verification for step-level reasoning, but producing verification states rather than natural-language rationales. FaithCoT-Bench (ICLR 2026) benchmarks CoT faithfulness, finding LLM-as-judge methods achieve 65-77 F1 for detecting unfaithfulness. Faithful Autoformalization (arXiv 2604.25031, Amrollahi et al., Stanford) proposes and quantifies a roundtrip verification mechanism (formalize -> back-translate -> re-formalize -> Z3 equivalence check) achieving 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model performs diagnosis and repair), or up to 91-95% with cross-model diagnosis (Claude performs diagnosis while GPT executes the pipeline) -- the cross-model improvement demonstrates that the diagnosis function is the performance bottleneck, not the pipeline itself. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) finds no systematic gaming in unified generation (Fleiss kappa 0.92) but reveals that DeepSeek-R1 mistranslates premises in two-stage pipelines, producing internally consistent but unfaithful outputs undetectable by LLM-as-judge -- a vulnerability partially addressed by Z3 formal equivalence checks but fundamentally bounded at the NL-to-formal boundary. FormalRewardBench (arXiv 2605.10141, May 2026) shows frontier LLMs achieve only 59.8% pairwise accuracy on formal proof evaluation (Lean 4, MiniF2F problems) while specialized provers achieve only 24.4%, revealing a generation-evaluation gap that motivates using formal tools (not LLMs) as ground truth for rationale grounding. VPRMs (arXiv 2601.17223, Jan 2026) demonstrate that deterministic rule-based step verification dramatically outperforms neural PRMs (87.9% vs 52.4% for GPT-4 on medical evidence synthesis), but are limited to domains with explicit procedural guidelines -- our approach extends this paradigm from rule-based to proof-based verification with stronger mathematical guarantees but narrower initial scope. PRoSFI (arXiv March 2026) uses formal verification as a reward signal during RL training of generators via structured formal intermediaries -- targets generator training, not verifier rationale grounding. HERMES (ICML 2026) interleaves informal reasoning with Lean4-verified proof steps for generators. GroundedPRM (NeurIPS 2025 Workshop) uses MCTS plus tool execution for fidelity-aware supervision with execution-based grounding. MATH-VF (arXiv 2025) combines SymPy+Z3 for step-wise formal verification on MATH-500 and ProcessBench, producing corrective feedback beyond binary labels -- demonstrating that Z3-based step verification can extend to domains beyond GSM8K-level arithmetic. 'Outcome Accuracy is Not Enough' (arXiv Feb 2026) demonstrates approximately 40% rationale consistency with human judgments for frontier GenRMs (specifically 'around 0.4' per the paper), underscoring the need for formal grounding. FormalMATH (arXiv 2025) benchmarks formal theorem proving with 5,560 Lean4 problems showing even the strongest provers achieve only 16.46% success under practical budgets, with pronounced domain bias favoring algebra over calculus/applied math -- grounding our scope restriction to GSM8K-level problems. No existing work connects structured formal proof artifacts to generative PRM rationale training or uses them as ground-truth error specifications for rationale quality evaluation: FoVer provides binary labels without explanations, ThinkPRM/GenPRM/R-PRM provide explanations without formal grounding, Safe provides formal verification states without NL rationales, Proof-RM scores proof quality without rationale generation, StepProof performs step-level Isabelle verification but targets proof construction rather than rationale grounding, Learning to Disprove generates formal counterexamples but for generator training rather than verifier rationale quality, R-Align diagnoses spurious correctness without formal remedies, VPRMs use rule-based not proof-based verification, CVPDS uses template-based error injection rather than genuine proof artifact extraction, and 'Outcome Accuracy is Not Enough' improves rationale quality through soft semantic matching rather than deterministic formal grounding.\",\n  \"inspired_by\": \"Field guide Gap 6 (faithfulness of CoT verification rationales in GenRM -- 'never fully resolved'), R-Align's demonstration that substantial GenRM decisions are spuriously correct, R-PRM's demonstration that reasoning-driven evaluation improves accuracy without addressing faithfulness, FormalRewardBench's finding that LLMs cannot reliably evaluate formal proofs (motivating tool-based grounding), the untried bridge between FoVer's formal proof artifacts and ThinkPRM's rationale generation, and the broader insight that PRM rationale faithfulness lacks a ground-truth evaluation methodology analogous to PRM800K's step-level labels\",\n  \"approach\": \"We make three contributions: (1) a training methodology that grounds generative PRM rationales in formal proof artifacts, (2) a diagnostic evaluation methodology (FormalFaithBench) that uses proof artifacts as ground-truth error specifications for measuring any PRM's rationale quality, and (3) empirical evidence on the inherent value of formally grounded rationales for safety-critical applications, PRM diagnostics, and training data integrity. We scope primary evaluation to domains where FoVer's formal verification pipeline is validated: GSM8K-level arithmetic (Isabelle) and first-order logic tasks (Z3 on FOLIO/LogicNLI). We evaluate transfer to harder domains as a secondary analysis.\\n\\nPhase 1 -- Data Preparation and Proof Artifact Extraction (~3-4 weeks engineering). We begin from FoVer-40K, the published balanced training dataset containing 40,000 steps (20K formal logic + 20K theorem proving) at 50% error rate. This yields 20,000 error steps as the base for artifact extraction. Additionally, we augment the base data by re-running FoVer's open-source pipeline on additional problems: FoVer sampled only 10,000 problems per task from much larger source datasets -- FLDx2 contains 100K+ formal logic problems, while MetaMathQA provides 395K math problems. By sampling an additional 10K problems per task and generating solutions from one additional LLM (e.g., Qwen3-8B), we estimate producing ~40K additional error steps at similar error rates (logic ~42%, proof ~14%), yielding a combined pool of ~30K error steps for artifact extraction. We extract artifacts in two tracks: (a) For Z3-verified logic steps, we extract structured counterexamples from SAT results. Z3 natively produces satisfying models when a formula is satisfiable, so for each incorrect step we obtain variable assignments demonstrating the error. This is primarily a parsing and templating task (~1-2 weeks). We estimate ~95% of incorrect logic steps yield extractable counterexamples, since Z3 reliably produces models for SAT results. (b) For Isabelle-verified theorem proving steps, we modify FoVer's Isabelle wrapper to capture proof state information at failure points -- the current goal, available hypotheses, and which tactic failed (~2-3 weeks, requiring deeper Isabelle API integration). StepProof (Hu et al., 2025) provides directly relevant engineering precedent: their incremental proof state management system demonstrates feasibility of fine-grained Isabelle proof state manipulation with accumulative verified-step context, selective backtracking, and proof state suspension -- reducing our engineering risk for this track. We estimate ~60-70% of incorrect steps yield usable proof state artifacts, as some failures occur in preprocessing before meaningful state is available. Pilot validation: we run artifact extraction on a 2K-step sample (1K logic, 1K arithmetic) in week 1 to calibrate yield estimates before full-scale extraction. This pilot also calibrates cross-domain roundtrip equivalence rates (see Phase 2), since math/logic formalization may differ from Amrollahi et al.'s statutory text domain in both directions: math/logic has lower linguistic ambiguity (potentially favoring higher equivalence rates) but higher formalization difficulty for non-trivial steps involving implicit mathematical conventions (potentially favoring lower rates). The pilot's empirical calibration resolves this directional uncertainty before committing to full-scale synthesis.\\n\\nPhase 2 -- Proof-Grounded Rationale Synthesis (~3 weeks). We use Qwen3-32B to synthesize natural-language verification rationales grounded in extracted artifacts. Each rationale template incorporates the specific artifact (e.g., 'Step 3 claims x+y>10, but the counterexample x=3, y=2 shows this fails' for Z3; 'The proof state after step 4 has unsolved goal involving P(n+1), but the applied tactic only handles the base case' for Isabelle). We apply roundtrip consistency filtering adapted from Amrollahi et al. (2604.25031): each generated rationale is re-formalized and checked for Z3/Isabelle semantic equivalence with the original artifact. Amrollahi et al. report 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model) or 91-95% with cross-model diagnosis (a separate LLM performs only the diagnosis step while the primary model executes the pipeline). We implement standard same-model diagnosis-guided repair using Qwen3-32B as both diagnostician and pipeline executor, following their finding that scoped stage-level diagnosis outperforms random-stage repair. We do not implement cross-model diagnosis in the initial pipeline to avoid the additional complexity and cost of routing diagnosis through a separate LLM, but note it as an available improvement lever if standard repair yields insufficient throughput. Given the directional uncertainty in cross-domain transfer (math/logic vs. statutory text), we conservatively estimate 50-65% baseline pass rate on our domains, improvable to 70-85% with standard diagnosis-guided repair. The Phase 1 pilot on 2K steps will empirically calibrate these estimates before full-scale synthesis. Data yield estimate with two scenarios:\\n\\n  Scenario A (FoVer-40K only, conservative): Starting from ~20K error steps -> ~16K with extractable artifacts (9.5K Z3 at 95% + 6.5K Isabelle at 65%) -> ~11.2-13.6K after roundtrip+repair filtering at ~70-85% -> ~9.5-11.6K after ~15% final quality filtering. Final: ~9-12K proof-grounded rationales.\\n\\n  Scenario B (FoVer-40K + augmented pipeline): Starting from ~30K error steps -> ~24K with extractable artifacts (15K Z3 + 9K Isabelle) -> ~16.8-20.4K after roundtrip filtering -> ~14.3-17.3K after quality filtering. Final: ~14-17K proof-grounded rationales.\\n\\n  Data sufficiency argument: ThinkPRM achieves competitive performance with only 1K synthetic verification CoTs (~8K step labels), GenPRM uses 23K training examples, and R-PRM uses ~289K SFT samples but achieves comparable performance to Qwen2.5-Math-PRM with only ~15% of its data. Our conservative Scenario A of ~9-12K formally grounded rationales represents ~10x ThinkPRM's training data and is comparable to GenPRM's scale. Moreover, our rationales carry richer supervision signal than any of these: each rationale is traceable to a specific formal proof artifact with verified semantic grounding, whereas ThinkPRM's rationales are filtered only on label match, GenPRM's use execution-based but not proof-based verification, and R-PRM's are bootstrapped from LLM-generated seed data without formal grounding. Learning to Disprove (Li et al., 2026) demonstrates at scale (575K counterexamples from 321K seed theorems) that formal counterexamples serve as effective training signals, supporting our premise that proof artifacts provide rich supervision. We thus expect higher per-example training signal quality, partially compensating for any quantity gap.\\n\\nPhase 3 -- SFT Training (~2 weeks). We fine-tune Qwen3-14B (or DeepSeek-R1-Distill-Qwen-14B) as a generative PRM on the proof-grounded rationales following ThinkPRM's SFT recipe. We train separate models on Z3-grounded logic rationales, Isabelle-grounded arithmetic rationales, and the combined set to enable ablation of each grounding source's contribution.\\n\\nPhase 4 -- Evaluation (~4-5 weeks). Verification accuracy is evaluated on: (primary) ProcessBench-GSM8K subset, FOLIO, LogicNLI; (transfer) ProcessBench-MATH/Olympiad subsets, MATH-500 best-of-N; targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N scores as baselines. Rationale faithfulness is assessed via three independent metrics, strictly separated from training: (1) R-Align's Spurious Correctness (S-Corr) as the primary automated faithfulness metric, computed by comparing rationale reasoning against golden reference judgments from ProcessBench annotations; (2) FaithCoT-Bench detection metrics (precision, recall, F1); (3) human evaluation on 150-200 randomly sampled rationales, rating formal grounding quality and error identification accuracy. Roundtrip consistency is reported ONLY as a supplementary training-data-quality indicator and correlation analysis (does higher roundtrip score predict higher human-rated quality?), not as a primary evaluation metric or novel contribution.\\n\\nPhase 4 includes three dedicated experiments beyond standard PRM evaluation:\\n\\n(A) Faithfulness transfer experiment. We measure S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for: (a) our formally grounded model trained only on GSM8K-level/FOL rationales; (b) ThinkPRM-14B baseline; (c) GenPRM-7B baseline; (d) R-PRM-7B-DPO baseline (the strongest reasoning-based PRM without formal grounding -- testing whether rich reasoning analyses alone reduce S-Corr); (e) an ablation model trained on FoVer-40K binary labels (no formal rationale grounding). This experiment disentangles four claims: (i) does formal grounding reduce S-Corr on in-domain tasks (GSM8K, FOL)? (ii) does the S-Corr reduction transfer to harder domains (MATH, Olympiad) via the same easy-to-difficult mechanism FoVer demonstrated for accuracy? (iii) does the transfer specifically require rationale-level formal grounding, or does any FoVer-derived training signal suffice? (iv) does R-PRM's reasoning-driven evaluation reduce S-Corr relative to simpler baselines -- isolating whether accuracy-improving reasoning also improves faithfulness, or whether formal grounding provides an orthogonal faithfulness benefit? If (i) holds but (ii) doesn't, we still demonstrate improved faithfulness within the validated scope. If both hold, we provide the first empirical evidence that formal rationale grounding at the foundational training-data level propagates to harder reasoning tasks.\\n\\n(B) Downstream policy experiment. To close the full causal chain (formal grounding -> reduced S-Corr -> better downstream policy), we conduct a small-scale rejection sampling experiment. We generate N=8 candidate solutions per problem for 500 GSM8K and 500 MATH problems using Qwen2.5-Math-1.5B-Instruct as the policy model, then select the best response according to each PRM: (a) our formally grounded PRM; (b) ThinkPRM-14B; (c) R-PRM-7B-DPO; (d) FoVer-trained discriminative PRM (binary labels). We report pass@1 accuracy of the selected solutions (best-of-N evaluation) and, as a stronger test, perform rejection sampling fine-tuning (RFT): we fine-tune Qwen2.5-Math-1.5B on the top-ranked solutions selected by each PRM (filtering to solutions verified as correct), then evaluate the resulting policy models on held-out MATH-500 and GSM8K test sets. R-Align demonstrates that S-Corr predicts RLHF policy degeneration (as established in the paper's experimental analysis); our experiment directly tests whether formally grounded rationale selection -- by reducing spurious correctness in the reward signal -- yields better-trained policies. This is a modest-cost experiment (~50-80 GPU hours for generation + RFT on 1.5B model) that could provide the strongest possible impact argument.\\n\\n(C) FormalFaithBench: Diagnostic evaluation of PRM rationale quality. This experiment constitutes a standalone methodological contribution. For each error step where we have extracted a formal proof artifact (Z3 counterexample or Isabelle proof state), we define a ground-truth 'error specification': the specific mathematical property violated, the concrete counterexample or proof state demonstrating the violation, and the minimal conditions under which the error manifests. We then evaluate whether each baseline PRM's rationale for the same step correctly identifies the error specified by the formal artifact, measured via three automated metrics: (i) Error Identification Rate (EIR): does the rationale mention the specific mathematical property that is violated? (ii) Counterexample Alignment (CA): for Z3 steps, does the rationale's explanation align with the formal counterexample's variable assignments? (iii) Proof State Match (PSM): for Isabelle steps, does the rationale reference the proof obligation that actually fails? We evaluate these metrics across our formally grounded PRM, ThinkPRM-14B, GenPRM-7B, R-PRM-7B-DPO, and a vanilla Qwen3-14B prompted with verification instructions. This produces the first automated, scalable benchmark for PRM rationale quality with formal ground truth -- analogous to how ProcessBench evaluates step-level label accuracy, FormalFaithBench evaluates step-level explanation accuracy. We construct the benchmark from ~2-3K held-out error steps (not used in training) with extracted artifacts, and we validate the automated metrics against human judgments on a 200-step subset to establish metric reliability. This contribution is valuable regardless of whether our trained PRM achieves state-of-the-art accuracy: even if formal grounding provides marginal accuracy improvements, the diagnostic methodology enables the community to measure and improve rationale faithfulness across any PRM.\\n\\nImpact beyond the accuracy-transfer framing: We foreground three inherent value propositions that make this work impactful regardless of domain difficulty. (1) Safety-critical deployment: GSM8K-level arithmetic -- multi-step calculations involving unit conversions, proportional reasoning, and chained arithmetic -- is precisely the domain where AI math reasoning is being deployed in practice for financial compliance, engineering safety margins, and pharmaceutical dosing calculations. In these applications, regulators and auditors require not just that a verification system flags an error, but that the flagging comes with a traceable explanation identifying the specific mathematical property violated. Current PRMs provide opaque scores (discriminative) or unverified rationales (generative); formally grounded rationales provide the first verifiably faithful error explanations suitable for auditable deployment. (2) PRM diagnostics: FormalFaithBench (Phase 4C) provides the first automated methodology for measuring whether a PRM's rationale correctly identifies the actual mathematical error, filling a critical evaluation gap. Current metrics (S-Corr, MetaJudge) measure alignment with reference judgments but cannot determine whether the PRM understood the error or reached the right label through spurious reasoning. Our formal error specifications provide deterministic ground truth for this question. (3) Training data integrity: The PRM training ecosystem is built on GSM8K/MATH-derived data. PRM800K labels 75K GSM8K/MATH solutions, OmegaPRM generates 1.5M annotations from similar distributions, FoVer-40K derives from GSM8K-level problems. If rationale quality at this foundational level is unreliable (and R-Align/MetaJudge show ~40-60% spurious correctness/inconsistency rates), the corruption propagates through the entire training pipeline. Improving faithfulness at the source is a leverage point, not a limitation.\\n\\nAcknowledged Limitations and Mitigations. (1) Scope: FoVer's formal verification is validated on GSM8K-level arithmetic and FOL logic. Extending to competition math faces fundamental barriers -- Z3 is undecidable for nonlinear integer arithmetic (confirmed by 'SMT and Functional Equation Solving over the Reals,' 2025), and FormalMATH shows only 16.46% LLM prover success on Lean4 problems. MATH-500 and GPQA-Diamond are explicitly positioned as stretch goals requiring future formalization extensions: specifically, Lean 4 integration (via Safe's autoformalization pipeline) for algebraic reasoning, or SymPy+Z3 (via MATH-VF's approach) for computational verification. We treat this scope limitation as a design choice rather than a weakness: foundational domains are where formal grounding provides deterministic guarantees and where the practical applications (safety-critical, diagnostics, training data) are most compelling. (2) Gaming vulnerability: Kim et al. (2604.19459) show two-stage formalization pipelines are vulnerable to premise mistranslation. Our Z3 formal equivalence check provides stronger detection than LLM-as-judge for axiom-fabrication-type errors (would catch GPT-5's 107 fabricated axioms in their study), but cannot fully guard against symmetric mistranslation at the NL-to-formal boundary. We mitigate via: (a) roundtrip verification from Amrollahi et al., which catches asymmetric errors; (b) NLI-based drift analysis as a secondary signal; (c) restricting to domains (FOL, arithmetic) where formalization ambiguity is lower than natural language. (3) FormalRewardBench shows even frontier LLMs achieve only 59.8% on formal proof evaluation, but our approach uses formal verification tools (Z3, Isabelle) as ground truth rather than LLMs as proof evaluators, sidestepping the generation-evaluation gap within Z3/Isabelle's decidable scope. (4) Cross-domain roundtrip uncertainty: Amrollahi et al.'s roundtrip equivalence rates were measured on statutory text, while our pipeline operates on math/logic formalization. These domains may differ in opposing ways: math/logic has lower linguistic ambiguity and more standardized notation (potentially yielding higher equivalence rates), but non-trivial mathematical steps involve implicit conventions and multi-step dependencies that may resist clean formalization (potentially yielding lower rates). Our Phase 1 pilot validation on 2K steps is specifically designed to calibrate this cross-domain transfer before committing to full-scale synthesis, and we report pilot equivalence rates alongside Amrollahi et al.'s statutory text rates to enable direct comparison. (5) Complementarity with non-formal approaches: 'Outcome Accuracy is Not Enough' (Qwen team, 2602.04649) achieves strong rationale quality improvements through soft semantic matching against human annotations without formal grounding. Our approach provides stronger guarantees (deterministic formal traceability) within a narrower scope; their approach provides broader coverage (any domain with annotations) with softer guarantees. Future work should explore combining formal grounding for in-scope domains with hybrid consistency training for broader coverage. (6) Relationship to concurrent data synthesis work: CVPDS (arXiv 2605.02395) provides an alternative approach to generating verified PRM training data through template-based error injection. While methodologically distinct from proof-artifact extraction, both approaches aim to improve PRM training data quality through formal/symbolic verification. Our approaches are complementary: CVPDS offers controllable error diversity but is constrained by predefined templates, while our method extracts artifacts from naturally occurring LLM errors but requires successful formal verification. Combining controlled error injection with proof-artifact rationale grounding is a promising future direction. (7) FormalFaithBench scope: The diagnostic benchmark is limited to domains where formal verification produces extractable artifacts (currently FOL and GSM8K-level arithmetic). However, the methodology extends naturally as formal verification tools expand to new domains (Lean 4 for algebra via Safe, SymPy+Z3 for computation via MATH-VF), and the benchmark design is explicitly modular to accommodate new artifact types.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"550-750 (solution generation for augmented data ~80h, rationale synthesis with Qwen3-32B ~120h, SFT on 14B model 4xA100 ~100h, evaluation including faithfulness transfer experiment ~100h, downstream policy experiment ~60h, FormalFaithBench construction and evaluation ~40h, ablations ~90h)\",\n      \"engineering_time\": \"Z3 counterexample parsing: ~1-2 weeks; Isabelle proof state extraction: ~2-3 weeks; augmented data generation: ~1 week; roundtrip filter + diagnosis repair: ~1 week; FormalFaithBench metric implementation: ~1 week; downstream RFT pipeline: ~0.5 weeks; integration/testing: ~1 week. Total: 7-9 weeks engineering.\",\n      \"timeline\": \"16-20 weeks\",\n      \"estimated_gpu_cost\": \"$1100-1800 (A100 80GB at ~$2.00/hr on Vast.ai/Spheron)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"550-750 (irreducible training/inference costs unchanged)\",\n      \"engineering_time\": \"4-6 weeks (Claude accelerates Z3 parsing code, Isabelle wrapper modifications, rationale template design, augmented data pipeline, FormalFaithBench metrics, evaluation harness, RFT pipeline)\",\n      \"timeline\": \"12-16 weeks\",\n      \"claude_api_cost\": \"$600-900 (Sonnet 4.6 for pipeline code generation and data analysis, ~120-220M tokens)\",\n      \"estimated_gpu_cost\": \"$1100-1800\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"600-800 (slightly higher from automated ablation sweeps, augmented data generation, faithfulness transfer experiment, downstream policy experiment, FormalFaithBench construction, and pilot experiments)\",\n      \"engineering_time\": \"2-3 weeks (Claude handles most Z3/Isabelle parsing engineering)\",\n      \"timeline\": \"9-12 weeks\",\n      \"claude_api_cost\": \"$1700-2800 (Sonnet 4.6 for end-to-end pipeline orchestration, rationale quality filtering, FormalFaithBench metric design, iterative ablation design, ~450-750M tokens)\",\n      \"estimated_gpu_cost\": \"$1200-1900\",\n      \"speed_bottleneck\": \"Isabelle proof state extraction engineering (~2-3 weeks irreducible due to Isabelle API complexity, though StepProof's engineering precedent reduces unknowns); Z3 counterexample extraction is faster (~1-2 weeks). Formal verification throughput (~2-10s per Z3 step, 15-60s per Isabelle step) is parallelizable across CPU cores. Augmented data generation adds ~1 week for solution generation and verification. Downstream RFT experiment is fast (~50-80h GPU) but depends on Phase 3 model completion. FormalFaithBench construction parallelizes with Phase 3 training.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (projected abstracts Sep 19, full papers Sep 24, 2026 -- 17 weeks; projected from ICLR 2026 pattern, official CFP not yet published as of May 2026; comfortable for human_in_loop and auto_research timelines)\",\n    \"ARR October 2026 cycle -> commitment to NAACL 2027 or ACL 2027 (comfortable backup NLP venue)\",\n    \"AAAI 2027 (abstracts Jul 21, full papers Jul 28, 2026 -- 8 weeks from today, feasible only with auto_research timeline and Z3-only scoped initial submission)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Process Reward Models That Think (arXiv 2025, ThinkPRM)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, She et al.)\",\n    \"Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, FoVer)\",\n    \"Controllable and Verifiable Process Data Synthesis for Process Reward Models (arXiv 2605.02395, May 2026, Chi & Wang)\",\n    \"StepProof: Step-by-step verification of natural language mathematical proofs (arXiv 2506.10558, June 2025, Hu et al.)\",\n    \"Learning to Disprove: Formal Counterexample Generation with Large Language Models (arXiv 2603.19514, March 2026, Li et al.)\",\n    \"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026)\",\n    \"RM-R1: Reward Modeling as Reasoning (ICLR 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026, Amrollahi et al.)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 @ ICLR 2026, Kim et al.)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2605.10141, May 2026)\",\n    \"Beyond Outcome Verification: Verifiable Process Reward Models (arXiv 2601.17223, Jan 2026, VPRMs)\",\n    \"Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)\",\n    \"R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging (arXiv Feb 2026)\",\n    \"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models (NeurIPS 2025)\",\n    \"Proof-RM: A Scalable and Generalizable Reward Model for Math Proof (arXiv Feb 2026)\",\n    \"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)\",\n    \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026, PRoSFI)\",\n    \"Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models (arXiv 2602.04649, Feb 2026, Qwen team)\",\n    \"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2025, MATH-VF)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of LLMs (arXiv 2025)\",\n    \"Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024, OmegaPRM)\",\n    \"GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling (NeurIPS 2025 Workshop)\"\n  ],\n  \"description\": \"We propose Proof-Grounded Generative PRMs, the first process reward models whose verification rationales are traceable to structured formal proof artifacts, and FormalFaithBench, the first automated benchmark for evaluating PRM rationale quality against formal ground truth. Current generative PRMs (ThinkPRM, GenPRM, R-PRM, RM-R1) produce chain-of-thought verification rationales trained on synthetic data of unknown faithfulness -- R-Align shows GenRM decisions exhibit substantial spurious correctness (right label, wrong reasoning), and frontier GenRMs achieve only approximately 40% rationale consistency with human judgments. R-PRM (EMNLP 2025) demonstrates that reasoning-driven evaluation substantially improves PRM accuracy (70.4 F1 on ProcessBench, +13.9 over Qwen2.5-Math-7B-PRM800K at 56.5 F1), but its multi-dimensional analyses are trained on LLM-bootstrapped data and rationale faithfulness is not evaluated. Separately, FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can produce accurate step-level error labels transferring across 12 benchmarks, but generates only binary labels and explicitly excludes reasoning-based PRMs. A concurrent approach (CVPDS, arXiv 2605.02395) synthesizes PRM data through template-based symbolic error injection across 11 error types with 20K instances, but targets accuracy through controlled error diversity rather than rationale faithfulness through proof-artifact grounding. A non-formal approach ('Outcome Accuracy is Not Enough,' Qwen team) improves rationale quality through hybrid consistency-outcome training via soft semantic matching against human annotations, achieving RM-Bench 87.1% (+5% over baselines) -- but relies on human annotation availability and provides softer guarantees than formal artifact tracing. We make three contributions bridging the formal gap. First, we extend FoVer's verification pipeline to extract structured proof artifacts -- Z3 counterexamples from SAT results and Isabelle proof state information at failure points -- going beyond binary labels to structured error specifications. StepProof (Hu et al., 2025) provides engineering precedent for fine-grained Isabelle proof state manipulation on GSM8K, and Learning to Disprove (Li et al., 2026) demonstrates at scale (575K instances) that formal counterexamples serve as effective training signals. Second, we synthesize verification rationales grounded in these artifacts using Qwen3-32B with roundtrip consistency filtering adapted from Amrollahi et al.'s (2604.25031) validated mechanism (45-66% baseline equivalence, 78-86% with standard diagnosis-guided repair, up to 91-95% with cross-model diagnosis; we implement standard same-model repair and conservatively estimate 70-85% post-repair rates on math/logic given cross-domain uncertainty), then fine-tune Qwen3-14B as a generative PRM on these rationales. Starting from FoVer-40K's 20K error steps, we estimate ~9-12K proof-grounded rationales (Scenario A); augmenting FoVer's pipeline with additional problems from the much larger source datasets yields ~14-17K (Scenario B). Both scenarios exceed ThinkPRM's training data (1K rationales / 8K step labels) by an order of magnitude, and our rationales carry richer per-example signal via formal artifact tracing. Third, we introduce FormalFaithBench: a diagnostic benchmark that uses ~2-3K held-out proof artifacts as ground-truth error specifications, measuring whether any PRM's rationale correctly identifies the specific mathematical error via three automated metrics (Error Identification Rate, Counterexample Alignment, Proof State Match), validated against 200 human judgments. This fills a critical evaluation gap: just as ProcessBench measures step-level label accuracy, FormalFaithBench measures step-level explanation accuracy -- the first automated methodology for evaluating PRM rationale quality with formal ground truth. We scope primary evaluation to domains where FoVer is validated -- GSM8K-level arithmetic and FOL logic (FOLIO, LogicNLI) -- targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N as baselines. Rationale faithfulness is assessed via R-Align's Spurious Correctness metric and FaithCoT-Bench as primary measures, plus human evaluation on 150-200 examples, with roundtrip consistency strictly demoted to a supplementary training-quality indicator. We foreground three inherent value propositions that make this work impactful on foundational domains regardless of transfer: (1) Safety-critical deployment: GSM8K-level arithmetic -- multi-step calculations involving unit conversions, proportional reasoning, and chained arithmetic -- is the domain where AI math reasoning is being deployed for financial compliance, engineering safety margins, and pharmaceutical dosing, where auditable error explanations are legally required. (2) PRM diagnostics: FormalFaithBench provides the community with the first automated tool for measuring whether any PRM's rationale correctly identifies the actual mathematical error, enabling systematic debugging of PRM failure modes beyond label accuracy. (3) Training data integrity: GSM8K is the foundation of PRM training pipelines (PRM800K, FoVer, OmegaPRM); improving rationale faithfulness at this level prevents corrupted supervision from propagating to all downstream applications. We additionally include three dedicated experiments: (A) a faithfulness transfer experiment measuring S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for our GSM8K-trained model versus baselines (including R-PRM-7B-DPO, the strongest reasoning-based baseline without formal grounding) and a binary-label ablation, directly testing whether formal rationale grounding propagates faithfulness improvements to harder domains; (B) a downstream policy experiment conducting rejection sampling fine-tuning of Qwen2.5-Math-1.5B using solutions selected by each PRM on 500 GSM8K + 500 MATH problems, testing whether reduced S-Corr translates to improved policy training; (C) FormalFaithBench evaluation of five PRMs (our model, ThinkPRM-14B, GenPRM-7B, R-PRM-7B-DPO, prompted Qwen3-14B) with metric reliability validation against human judgments. We acknowledge scope limitations (Z3 undecidability for nonlinear arithmetic; FormalMATH's 16.46% prover success), treat them as a design choice favoring deterministic guarantees on foundational domains, and position the methodology as extensible as formal verification tools expand.\",\n  \"project_name\": \"proof_grounded_genprm\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"issue_1_faithful_autoformalization_numbers\": \"ADDRESSED (MODERATE, round 4). Corrected landscape statement from '85-95% with diagnosis-guided repair' to precise numbers verified from Table 1, Section 7.1 of Amrollahi et al.: standard diagnosis-guided repair (same model) achieves 77.9%-85.7% equivalence, while cross-model diagnosis (Claude performs diagnosis, GPT executes pipeline) achieves 90.7%-94.7%. All instances updated throughout.\",\n    \"issue_2_hybrid_training_positioning\": \"ADDRESSED (MODERATE, round 4). Added 'Outcome Accuracy is Not Enough' (Qwen team, arXiv 2602.04649) to the landscape with detailed positioning as complementary non-formal approach.\",\n    \"issue_3_faithfulness_transfer_experiment\": \"ADDRESSED (MINOR, round 4). Added dedicated faithfulness transfer experiment to Phase 4 with four-way comparison and ablation.\",\n    \"issue_4_crossdomain_roundtrip_uncertainty\": \"ADDRESSED (MINOR, round 4). Added explicit acknowledgment of cross-domain uncertainty with pilot calibration strategy.\",\n    \"issue_5_rprm_baseline\": \"ADDRESSED (MODERATE, round 5). Added R-PRM (EMNLP 2025, She et al.) comprehensively to the landscape with detailed methodology and results.\",\n    \"issue_6_cvpds_concurrent_work\": \"ADDRESSED (MODERATE, round 5). Added CVPDS (arXiv 2605.02395, Chi & Wang, May 2026) to the landscape with detailed methodology.\",\n    \"issue_7_downstream_rlhf_experiment\": \"ADDRESSED (MINOR, round 5). Added Phase 4(B) downstream policy experiment.\",\n    \"issue_8_iclr2027_deadline_tentative\": \"ADDRESSED (MINOR, round 5). ICLR 2027 deadline now explicitly noted as projected.\",\n    \"issue_9_ralign_claims_clarification\": \"ADDRESSED (MINOR, round 5). R-Align description now distinguishes between abstract-level and full-paper claims.\",\n    \"issue_10_rprm_baseline_f1_correction\": \"ADDRESSED (MINOR, round 7). Corrected Qwen2.5-Math-7B-PRM800K baseline from 58.5 F1 to 56.5 F1 throughout. The improvement claim (+13.9 F1) and R-PRM-7B-DPO score (70.4 F1) remain correct: 70.4 - 56.5 = 13.9.\",\n    \"issue_11_stepproof_acknowledgment\": \"ADDRESSED (MINOR, round 7). Added StepProof (arXiv 2506.10558, Hu et al., June 2025) to landscape with detailed methodology: step-by-step Isabelle-based autoformalization on GSM8K, incremental proof state management with accumulative context and selective backtracking, 27.9% proof pass rate. Referenced as engineering precedent in Phase 1(b) for Isabelle proof state extraction, reducing engineering risk. Added to gap analysis.\",\n    \"issue_12_learning_to_disprove_acknowledgment\": \"ADDRESSED (MINOR, round 7). Added 'Learning to Disprove' (arXiv 2603.19514, Li et al., March 2026) to landscape: symbolic mutation strategy producing 575K counterexample instances from 321K seed theorems in Lean 4, 74% improvement over baselines, multi-reward expert iteration. Positioned as demonstrating scalable formal counterexample generation as training signals -- conceptual parallel supporting our approach. Distinguished: they train generators to produce counterexamples, we extract counterexamples from tools to ground verifier rationales. Referenced in data sufficiency argument.\",\n    \"issue_13_impact_ceiling_reframing\": \"ADDRESSED (STRUCTURAL, round 7). MAJOR REFRAMING: Restructured the entire value proposition to foreground three inherent-value arguments that make easy-domain formal grounding valuable REGARDLESS of transfer. (1) Safety-critical deployment: GSM8K-level arithmetic IS the deployment domain for financial compliance, engineering safety margins, pharmaceutical dosing -- applications requiring auditable error explanations. (2) PRM diagnostics: Introduced FormalFaithBench (Phase 4C), a new methodological contribution providing the first automated benchmark for PRM rationale quality with formal ground truth, measuring Error Identification Rate, Counterexample Alignment, and Proof State Match. This is valuable regardless of our trained PRM's accuracy -- even if formal grounding provides marginal accuracy improvements, the diagnostic methodology enables the community to measure and improve rationale faithfulness across any PRM. (3) Training data integrity: Made the 'GSM8K as foundation' argument more central -- PRM800K, OmegaPRM, FoVer all build on GSM8K-level data, so improving faithfulness at this level is a high-leverage intervention. Restructured core_problem to frame the measurement gap alongside the training gap. Repositioned scope limitation as a design choice rather than weakness. Updated title, approach, description, and impact arguments throughout.\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22875224-384a-4246-831e-277b27e54a73",
  "isSidechain": false,
  "requestId": "req_011CbThaN3CtevPSgPYDLqtc",
  "type": "assistant",
  "uuid": "f7f87207-43b5-4362-8fcd-d78bff3af495",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WgvwfZad2hbcLtpbq73VSU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2621,
      "cache_creation_input_tokens": 3182,
      "cache_read_input_tokens": 25531,
      "output_tokens": 16639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3182,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2621,
          "output_tokens": 16639,
          "cache_read_input_tokens": 25531,
          "cache_creation_input_tokens": 3182,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3182
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

_source line 21 · 2026-05-27T20:31:59.291Z_

<details><summary>↩ Tool result · reported error · `toolu_01CVs3DjTz8NuLcTZCXY4guw`</summary>

```text
Claude requested permissions to write to /tmp/revised_proposal_round7.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7f87207-43b5-4362-8fcd-d78bff3af495",
  "isSidechain": false,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "type": "user",
  "uuid": "62688371-910b-4268-aa8f-8822296c0fd2",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_proposal_round7.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "f7f87207-43b5-4362-8fcd-d78bff3af495",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",   \"core_pr…",
  "leafUuid": "62688371-910b-4268-aa8f-8822296c0fd2",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise formal PRM rationale proposal with R-PRM baseline correction",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Tool call

_source line 24 · 2026-05-27T20:37:40.825Z_

<details open><summary>🔧 Tool call — Write · `toolu_01D7dY3FZmDrSvdeQuWgTFry`</summary>

```json
{
  "file_path": "/tmp/revised_proposal_round7.json",
  "content": "{\n  \"change_type\": \"major\",\n  \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs: Proof Artifacts as Ground-Truth Supervision for Verifiable Error Explanations\",\n  \"core_problem\": \"Generative PRMs (ThinkPRM, GenPRM, R-PRM) produce CoT verification rationales, but R-Align (Feb 2026) shows existing GenRMs exhibit substantial Spurious Correctness -- label-correct decisions with misaligned rationales -- and 'Outcome Accuracy is Not Enough' finds approximately 40% rationale consistency with human judgments. R-PRM demonstrates that reasoning-driven evaluation substantially improves accuracy (+13.9 F1 on ProcessBench), yet even rich multi-dimensional reasoning analyses lack formal grounding and have unknown faithfulness. More fundamentally, there is no scalable ground-truth methodology for evaluating WHETHER a PRM's rationale correctly identifies the actual mathematical error: human evaluation doesn't scale, LLM-as-judge achieves only 65-77 F1 for detecting unfaithfulness (FaithCoT-Bench), and existing automated metrics (S-Corr, MetaJudge) rely on reference annotations unavailable for most domains. Can we use formal proof artifacts -- Z3 counterexamples, Isabelle proof state information -- both as training supervision for faithful rationale generation AND as ground-truth error specifications for evaluating rationale quality across any PRM, establishing a methodology that is inherently valuable on foundational domains regardless of transfer to harder problems?\",\n  \"opportunity\": \"The field faces a measurement problem alongside a training problem: we lack ground-truth for what constitutes a faithful PRM rationale. GenRM reviewer 3 raised the unresolved concern that CoT rationales may be 'plausible-sounding but unfaithful reasoning that happens to correlate with correct verdicts.' But detecting this requires knowing what the ACTUAL error is -- which formal verification uniquely provides. FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can generate step-level error labels transferring across 12 benchmarks, but FoVer explicitly restricts to classification-based PRMs producing only binary labels, excluding generative/reasoning-based PRMs. R-PRM (EMNLP 2025) shows that reasoning-driven step evaluation -- generating multi-dimensional analyses before judgments -- substantially improves PRM accuracy (+13.9 F1 on ProcessBench via DPO), but its rationales are trained on LLM-generated seed data without formal grounding and faithfulness is not evaluated. ThinkPRM generates rich verification CoTs but trains on synthetic rationales of unknown faithfulness. The untried bridge is extracting structured proof artifacts -- Z3 counterexamples, Isabelle proof state information -- from FoVer's verification pipeline and using them as both (a) grounding signals for ThinkPRM-style rationale generation and (b) ground-truth error specifications for a new diagnostic evaluation methodology (FormalFaithBench). This fills two gaps simultaneously: the training gap (reasoning-driven methods leave rationale faithfulness ungrounded) and the evaluation gap (no scalable automated method exists for measuring whether a PRM's explanation correctly identifies the mathematical error). Three arguments establish the inherent value of this contribution on foundational domains, independent of transfer to harder problems: (1) Safety-critical deployment: GSM8K-level arithmetic IS the domain for financial calculations, engineering computations, and medical dosing -- applications where knowing WHY a step is wrong is legally and operationally required, not just whether it's wrong. Current PRMs provide only opaque scores or unverified rationales for these critical applications. (2) PRM diagnostics and debugging: Formally grounded error specifications establish a reference standard for measuring rationale quality across ALL PRMs -- analogous to how PRM800K provides ground-truth step labels, our FormalFaithBench provides ground-truth explanations, enabling the first automated methodology for evaluating whether any PRM's rationale correctly identifies the actual mathematical error. (3) Training data integrity: GSM8K-level problems are the primary source for PRM training data construction (PRM800K, FoVer, OmegaPRM's 1.5M annotations all derive from or include GSM8K/MATH). Ensuring rationale faithfulness at this foundational level prevents corrupted supervision signals from propagating to all downstream applications -- improving the foundation rather than patching the symptoms. Critically, Faithful Autoformalization (Amrollahi et al., April 2026) has now validated and quantified the roundtrip verification mechanism we adopt for quality filtering, showing 45-66% baseline equivalence rates improvable to 78-86% with standard diagnosis-guided repair or up to 91-95% with cross-model diagnosis -- providing empirical grounding for our data pipeline feasibility. Moreover, FoVer itself demonstrates easy-to-difficult transfer: PRMs trained on GSM8K-level data significantly improve step-level verification on MATH (88.0% vs 78.2% baseline), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%), suggesting that improving rationale faithfulness on foundational domains may propagate to harder reasoning tasks -- though we treat this as a secondary hypothesis to test rather than a core claim.\",\n  \"landscape\": \"ThinkPRM (arXiv 2025) achieves 8% improvement on GPQA-Diamond over discriminative verifiers using only 1% of PRM800K labels (specifically 1K synthetic verification CoTs filtered to ~8K step labels), but its rationales lack formal grounding. GenPRM (AAAI 2026) combines CoT with code verification, enabling 1.5B models to outperform GPT-4o on ProcessBench using only 23K training examples. R-PRM (EMNLP 2025) introduces reasoning-driven process reward modeling: it generates multi-dimensional step analyses (Previous Steps Analysis, Now Step Analysis, Data Source Analysis, Consistency Analysis, Calculation Analysis) followed by binary judgments. Using Qwen2.5-Math-7B-Instruct as the base model, R-PRM-7B-DPO achieves 70.4 F1 on ProcessBench (+13.9 over Qwen2.5-Math-7B-PRM800K at 56.5 F1) and +8.5 F1 on PRMBench, with consistent +8.6 accuracy improvements on six downstream math reasoning datasets via best-of-N selection. R-PRM trains on ~289K SFT samples and ~269K DPO pairs bootstrapped from PRM800K annotations, achieving comparable performance to Qwen2.5-Math-PRM with only ~15% of its data volume. Critically, while R-PRM produces rich natural-language reasoning for each step evaluation, it does not evaluate rationale faithfulness -- the analyses are trained on LLM-generated seed data and may exhibit the same spurious correctness that R-Align identifies in other GenRMs. R-PRM demonstrates the ceiling of what reasoning-driven evaluation achieves without formal grounding: substantial accuracy gains, but with unknown rationale fidelity to the actual mathematical errors. FoVer (ACL 2026 Findings) uses Z3/Isabelle for automated step-level labeling with easy-to-difficult transfer (trained on GSM8K-level, evaluates on MATH/AIME/Olympiad), but produces only binary labels and explicitly excludes reasoning-based PRMs citing 'substantially higher computational costs.' FoVer-40K contains 40,000 balanced training steps (20K formal logic from FLDx2 + 20K theorem proving from GSM8K-level problems) with 50% error rate, generated from solutions by Llama 3.1 8B and Qwen 2.5 7B; the raw unbalanced pipeline output is substantially larger (~216K steps from 10K problems per task across both models). 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) is concurrent work that synthesizes PRM training data through a four-stage pipeline: constructing correct symbolic reasoning chains from rule templates, injecting template-aware errors into intermediate steps, symbolically recomputing subsequent steps to maintain trajectory consistency, and verifying that injected errors are not derivable from the prefix. They produce 20K paired (correct, erroneous) trajectories across 11 error types (7 truth-state: drop_condition, implication_misuse, or_and_confusion, partial_evaluation, xor_as_or, xor_as_equiv, vacuous_truth_error; 4 structural: converse_error, redundant_step, missing_prerequisite, circular_reference), translated into natural-language processes for PRM training. Their method improves best-of-8 reranking on logical reasoning benchmarks (Llama-3.1-8B: 0.528 -> 0.591, Qwen-2.5-7B: 0.567 -> 0.615 average F1), with limited transfer to mathematics (ProcessBench GSM8K: 21.2% F1). The key methodological distinction from our work: they generate controlled synthetic errors through template-based injection for accuracy-focused PRM training, while we extract genuine proof artifacts from naturally occurring errors in LLM solutions for faithfulness-focused rationale grounding. Their error diversity is constrained by predefined templates (an acknowledged limitation), while our artifacts reflect the actual distribution of errors that LLMs make. The two approaches are complementary -- their controlled error injection could extend the diversity of training scenarios, while our proof-artifact extraction provides traceable explanations of why each error is wrong. StepProof (arXiv 2506.10558, Hu et al., June 2025) performs step-by-step Isabelle-based autoformalization and verification on GSM8K, achieving 27.9% proof pass rate with 10 attempts (vs. 25.3% for full-proof baselines with 64 attempts). The key engineering contribution is incremental proof state management: verified steps accumulate into context for subsequent steps, failed steps can be selectively backtracked, and a 'suspension' mechanism allows skipping hard-to-formalize steps while preserving proof context. StepProof provides directly relevant engineering precedent for our Phase 1(b) Isabelle proof state extraction -- their interactive interface with color-coded verification status (green=verified, yellow=suspended, unmarked=failed) and accumulative proof stack demonstrate feasibility of fine-grained Isabelle proof state manipulation, though their goal is proof construction rather than proof artifact extraction for rationale grounding. 'Learning to Disprove: Formal Counterexample Generation with Large Language Models' (arXiv 2603.19514, Li et al., March 2026) trains LLMs to generate formal counterexamples verified in Lean 4 via a symbolic mutation strategy, producing 575,039 counterexample instances from 321,929 seed theorems. Their multi-reward expert iteration achieves 74% improvement over baselines on their For-Counter benchmark. While using Lean 4 rather than Z3/Isabelle, the conceptual parallel of using formal counterexamples as verified training signals directly supports our approach. Their scale (575K instances) demonstrates that formal counterexample generation is tractable, and their finding that dual reward signals improve training efficiency suggests our proof-artifact-grounded rationales may similarly provide richer supervision than binary labels. The key distinction is that they train generators to produce counterexamples, while we extract counterexamples from verification tools to ground verifier rationales. RM-R1 (ICLR 2026) trains reasoning reward models with explicit rationale chains but without formal grounding. R-Align (Feb 2026) introduces the Spurious Correctness (S-Corr) metric showing existing GenRMs exhibit substantial spuriously correct decisions (the abstract reports 'substantial S-Corr even for competitive GenRMs'; specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract), providing the key diagnostic our work aims to improve. 'Outcome Accuracy is Not Enough' (Qwen team, Feb 2026, arXiv 2602.04649) introduces a competing non-formal approach to improving rationale quality: they define Rationale Consistency via MetaJudge, which decomposes human rationales into atomic claims and performs strict one-to-one semantic matching against model justifications, finding frontier GenRMs achieve only ~40% rationale consistency. They train with a multiplicative hybrid signal R_final = R_rationale * R_outcome via GRPO, achieving RM-Bench 87.1% and JudgeBench 82.0% (+5% over outcome-only baselines, +7% on Arena Hard v2 creative writing during RLHF). Crucially, their approach targets Judge faithfulness (evaluation rationale quality) rather than Solver verification, and relies on soft semantic matching against human annotations -- providing broader applicability but weaker guarantees than formal artifact tracing. Their acknowledged limitation is scalability: computing rationale consistency still requires high-quality human annotations. Our formal grounding provides deterministic, traceable guarantees within Z3/Isabelle's decidable scope, while their approach extends to any domain with human annotations. The two methods are complementary: formal grounding where verification tools cover the domain, hybrid consistency training for broader applicability. Think-RM (NeurIPS 2025) shows that deep, long-horizon reasoning inside reward models -- including self-reflection and hypothetical reasoning -- is critical for accurate evaluation, achieving +8% over CoT-GenRMs on RM-Bench. Proof-RM (Feb 2026) provides a scalable pipeline for training reward models on mathematical proof verification with RL stabilization ('LLM-as-a-RM-for-RM'), reaching 82.4% accuracy at 32B on competition-level proofs (IMO/CMO/USAMO), but produces scores rather than formally grounded rationales. Safe (ACL 2025) demonstrates Lean 4 step-level verification of NL math reasoning with the FormalStep benchmark (30,809 formal statements), achieving interpretable verification evidence complementary to PRM scores -- the closest work on formal verification for step-level reasoning, but producing verification states rather than natural-language rationales. FaithCoT-Bench (ICLR 2026) benchmarks CoT faithfulness, finding LLM-as-judge methods achieve 65-77 F1 for detecting unfaithfulness. Faithful Autoformalization (arXiv 2604.25031, Amrollahi et al., Stanford) proposes and quantifies a roundtrip verification mechanism (formalize -> back-translate -> re-formalize -> Z3 equivalence check) achieving 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model performs diagnosis and repair), or up to 91-95% with cross-model diagnosis (Claude performs diagnosis while GPT executes the pipeline) -- the cross-model improvement demonstrates that the diagnosis function is the performance bottleneck, not the pipeline itself. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) finds no systematic gaming in unified generation (Fleiss kappa 0.92) but reveals that DeepSeek-R1 mistranslates premises in two-stage pipelines, producing internally consistent but unfaithful outputs undetectable by LLM-as-judge -- a vulnerability partially addressed by Z3 formal equivalence checks but fundamentally bounded at the NL-to-formal boundary. FormalRewardBench (arXiv 2605.10141, May 2026) shows frontier LLMs achieve only 59.8% pairwise accuracy on formal proof evaluation (Lean 4, MiniF2F problems) while specialized provers achieve only 24.4%, revealing a generation-evaluation gap that motivates using formal tools (not LLMs) as ground truth for rationale grounding. VPRMs (arXiv 2601.17223, Jan 2026) demonstrate that deterministic rule-based step verification dramatically outperforms neural PRMs (87.9% vs 52.4% for GPT-4 on medical evidence synthesis), but are limited to domains with explicit procedural guidelines -- our approach extends this paradigm from rule-based to proof-based verification with stronger mathematical guarantees but narrower initial scope. PRoSFI (arXiv March 2026) uses formal verification as a reward signal during RL training of generators via structured formal intermediaries -- targets generator training, not verifier rationale grounding. HERMES (ICML 2026) interleaves informal reasoning with Lean4-verified proof steps for generators. GroundedPRM (NeurIPS 2025 Workshop) uses MCTS plus tool execution for fidelity-aware supervision with execution-based grounding. MATH-VF (arXiv 2025) combines SymPy+Z3 for step-wise formal verification on MATH-500 and ProcessBench, producing corrective feedback beyond binary labels -- demonstrating that Z3-based step verification can extend to domains beyond GSM8K-level arithmetic. FormalMATH (arXiv 2025) benchmarks formal theorem proving with 5,560 Lean4 problems showing even the strongest provers achieve only 16.46% success under practical budgets, with pronounced domain bias favoring algebra over calculus/applied math -- grounding our scope restriction to GSM8K-level problems. No existing work connects structured formal proof artifacts to generative PRM rationale training or uses them as ground-truth error specifications for rationale quality evaluation: FoVer provides binary labels without explanations, ThinkPRM/GenPRM/R-PRM provide explanations without formal grounding, Safe provides formal verification states without NL rationales, Proof-RM scores proof quality without rationale generation, StepProof performs step-level Isabelle verification but targets proof construction rather than rationale grounding, Learning to Disprove generates formal counterexamples but for generator training rather than verifier rationale quality, R-Align diagnoses spurious correctness without formal remedies, VPRMs use rule-based not proof-based verification, CVPDS uses template-based error injection rather than genuine proof artifact extraction, and 'Outcome Accuracy is Not Enough' improves rationale quality through soft semantic matching rather than deterministic formal grounding.\",\n  \"approach\": \"We make three contributions: (1) a training methodology that grounds generative PRM rationales in formal proof artifacts, (2) FormalFaithBench, a diagnostic evaluation benchmark that uses proof artifacts as ground-truth error specifications for measuring any PRM's rationale quality, and (3) empirical evidence on the inherent value of formally grounded rationales for safety-critical applications, PRM diagnostics, and training data integrity. We scope primary evaluation to domains where FoVer's formal verification pipeline is validated: GSM8K-level arithmetic (Isabelle) and first-order logic tasks (Z3 on FOLIO/LogicNLI). We evaluate transfer to harder domains as a secondary analysis, with dedicated experiments testing whether formal grounding's faithfulness benefits propagate via the same easy-to-difficult mechanism FoVer demonstrated for accuracy, and whether reduced S-Corr translates to improved downstream policy training.\\n\\nPhase 1 -- Data Preparation and Proof Artifact Extraction (~3-4 weeks engineering). We begin from FoVer-40K, the published balanced training dataset containing 40,000 steps (20K formal logic + 20K theorem proving) at 50% error rate. This yields 20,000 error steps as the base for artifact extraction. Additionally, we augment the base data by re-running FoVer's open-source pipeline on additional problems: FoVer sampled only 10,000 problems per task from much larger source datasets -- FLDx2 contains 100K+ formal logic problems, while MetaMathQA provides 395K math problems. By sampling an additional 10K problems per task and generating solutions from one additional LLM (e.g., Qwen3-8B), we estimate producing ~40K additional error steps at similar error rates (logic ~42%, proof ~14%), yielding a combined pool of ~30K error steps for artifact extraction. We extract artifacts in two tracks: (a) For Z3-verified logic steps, we extract structured counterexamples from SAT results. Z3 natively produces satisfying models when a formula is satisfiable, so for each incorrect step we obtain variable assignments demonstrating the error. This is primarily a parsing and templating task (~1-2 weeks). We estimate ~95% of incorrect logic steps yield extractable counterexamples, since Z3 reliably produces models for SAT results. (b) For Isabelle-verified theorem proving steps, we modify FoVer's Isabelle wrapper to capture proof state information at failure points -- the current goal, available hypotheses, and which tactic failed (~2-3 weeks, requiring deeper Isabelle API integration). StepProof (Hu et al., 2025) provides directly relevant engineering precedent: their incremental proof state management system on GSM8K demonstrates feasibility of fine-grained Isabelle proof state manipulation with accumulative verified-step context, selective backtracking, and proof state suspension -- reducing our engineering risk for this track. We estimate ~60-70% of incorrect steps yield usable proof state artifacts, as some failures occur in preprocessing before meaningful state is available. Pilot validation: we run artifact extraction on a 2K-step sample (1K logic, 1K arithmetic) in week 1 to calibrate yield estimates before full-scale extraction. This pilot also calibrates cross-domain roundtrip equivalence rates (see Phase 2), since math/logic formalization may differ from Amrollahi et al.'s statutory text domain in both directions: math/logic has lower linguistic ambiguity (potentially favoring higher equivalence rates) but higher formalization difficulty for non-trivial steps involving implicit mathematical conventions (potentially favoring lower rates). The pilot's empirical calibration resolves this directional uncertainty before committing to full-scale synthesis.\\n\\nPhase 2 -- Proof-Grounded Rationale Synthesis (~3 weeks). We use Qwen3-32B to synthesize natural-language verification rationales grounded in extracted artifacts. Each rationale template incorporates the specific artifact (e.g., 'Step 3 claims x+y>10, but the counterexample x=3, y=2 shows this fails' for Z3; 'The proof state after step 4 has unsolved goal involving P(n+1), but the applied tactic only handles the base case' for Isabelle). We apply roundtrip consistency filtering adapted from Amrollahi et al. (2604.25031): each generated rationale is re-formalized and checked for Z3/Isabelle semantic equivalence with the original artifact. Amrollahi et al. report 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model) or 91-95% with cross-model diagnosis (a separate LLM performs only the diagnosis step while the primary model executes the pipeline). We implement standard same-model diagnosis-guided repair using Qwen3-32B as both diagnostician and pipeline executor, following their finding that scoped stage-level diagnosis outperforms random-stage repair. We do not implement cross-model diagnosis in the initial pipeline to avoid the additional complexity and cost of routing diagnosis through a separate LLM, but note it as an available improvement lever if standard repair yields insufficient throughput. Given the directional uncertainty in cross-domain transfer (math/logic vs. statutory text), we conservatively estimate 50-65% baseline pass rate on our domains, improvable to 70-85% with standard diagnosis-guided repair. The Phase 1 pilot on 2K steps will empirically calibrate these estimates before full-scale synthesis. Data yield estimate with two scenarios:\\n\\n  Scenario A (FoVer-40K only, conservative): Starting from ~20K error steps -> ~16K with extractable artifacts (9.5K Z3 at 95% + 6.5K Isabelle at 65%) -> ~11.2-13.6K after roundtrip+repair filtering at ~70-85% -> ~9.5-11.6K after ~15% final quality filtering. Final: ~9-12K proof-grounded rationales.\\n\\n  Scenario B (FoVer-40K + augmented pipeline): Starting from ~30K error steps -> ~24K with extractable artifacts (15K Z3 + 9K Isabelle) -> ~16.8-20.4K after roundtrip filtering -> ~14.3-17.3K after quality filtering. Final: ~14-17K proof-grounded rationales.\\n\\n  Data sufficiency argument: ThinkPRM achieves competitive performance with only 1K synthetic verification CoTs (~8K step labels), GenPRM uses 23K training examples, and R-PRM uses ~289K SFT samples but achieves comparable performance to Qwen2.5-Math-PRM with only ~15% of its data. Our conservative Scenario A of ~9-12K formally grounded rationales represents ~10x ThinkPRM's training data and is comparable to GenPRM's scale. Moreover, our rationales carry richer supervision signal than any of these: each rationale is traceable to a specific formal proof artifact with verified semantic grounding, whereas ThinkPRM's rationales are filtered only on label match, GenPRM's use execution-based but not proof-based verification, and R-PRM's are bootstrapped from LLM-generated seed data without formal grounding. Learning to Disprove (Li et al., 2026) demonstrates at scale (575K counterexamples from 321K seed theorems) that formal counterexamples serve as effective training signals, supporting our premise that proof artifacts provide rich supervision. We thus expect higher per-example training signal quality, partially compensating for any quantity gap.\\n\\nPhase 3 -- SFT Training (~2 weeks). We fine-tune Qwen3-14B (or DeepSeek-R1-Distill-Qwen-14B) as a generative PRM on the proof-grounded rationales following ThinkPRM's SFT recipe. We train separate models on Z3-grounded logic rationales, Isabelle-grounded arithmetic rationales, and the combined set to enable ablation of each grounding source's contribution.\\n\\nPhase 4 -- Evaluation (~4-5 weeks). Verification accuracy is evaluated on: (primary) ProcessBench-GSM8K subset, FOLIO, LogicNLI; (transfer) ProcessBench-MATH/Olympiad subsets, MATH-500 best-of-N; targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N scores as baselines. Rationale faithfulness is assessed via three independent metrics, strictly separated from training: (1) R-Align's Spurious Correctness (S-Corr) as the primary automated faithfulness metric, computed by comparing rationale reasoning against golden reference judgments from ProcessBench annotations; (2) FaithCoT-Bench detection metrics (precision, recall, F1); (3) human evaluation on 150-200 randomly sampled rationales, rating formal grounding quality and error identification accuracy. Roundtrip consistency is reported ONLY as a supplementary training-data-quality indicator and correlation analysis (does higher roundtrip score predict higher human-rated quality?), not as a primary evaluation metric or novel contribution.\\n\\nCritically, Phase 4 includes three dedicated experiments that go beyond standard PRM evaluation:\\n\\n(A) Faithfulness transfer experiment. We measure S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for: (a) our formally grounded model trained only on GSM8K-level/FOL rationales; (b) ThinkPRM-14B baseline; (c) GenPRM-7B baseline; (d) R-PRM-7B-DPO baseline (the strongest reasoning-based PRM without formal grounding -- testing whether rich reasoning analyses alone reduce S-Corr); (e) an ablation model trained on FoVer-40K binary labels (no formal rationale grounding). This experiment disentangles four claims: (i) does formal grounding reduce S-Corr on in-domain tasks (GSM8K, FOL)? (ii) does the S-Corr reduction transfer to harder domains (MATH, Olympiad) via the same easy-to-difficult mechanism FoVer demonstrated for accuracy? (iii) does the transfer specifically require rationale-level formal grounding, or does any FoVer-derived training signal suffice? (iv) does R-PRM's reasoning-driven evaluation reduce S-Corr relative to simpler baselines -- isolating whether accuracy-improving reasoning also improves faithfulness, or whether formal grounding provides an orthogonal faithfulness benefit? If (i) holds but (ii) doesn't, we still demonstrate improved faithfulness within the validated scope. If both hold, we provide the first empirical evidence that formal rationale grounding at the foundational training-data level propagates to harder reasoning tasks.\\n\\n(B) Downstream policy experiment. To close the full causal chain (formal grounding -> reduced S-Corr -> better downstream policy), we conduct a small-scale rejection sampling experiment. We generate N=8 candidate solutions per problem for 500 GSM8K and 500 MATH problems using Qwen2.5-Math-1.5B-Instruct as the policy model, then select the best response according to each PRM: (a) our formally grounded PRM; (b) ThinkPRM-14B; (c) R-PRM-7B-DPO; (d) FoVer-trained discriminative PRM (binary labels). We report pass@1 accuracy of the selected solutions (best-of-N evaluation) and, as a stronger test, perform rejection sampling fine-tuning (RFT): we fine-tune Qwen2.5-Math-1.5B on the top-ranked solutions selected by each PRM (filtering to solutions verified as correct), then evaluate the resulting policy models on held-out MATH-500 and GSM8K test sets. R-Align demonstrates that S-Corr predicts RLHF policy degeneration (as established in the paper's experimental analysis); our experiment directly tests whether formally grounded rationale selection -- by reducing spurious correctness in the reward signal -- yields better-trained policies. This is a modest-cost experiment (~50-80 GPU hours for generation + RFT on 1.5B model) that could provide the strongest possible impact argument.\\n\\n(C) FormalFaithBench: Diagnostic evaluation of PRM rationale quality. This experiment constitutes a standalone methodological contribution. For each error step where we have extracted a formal proof artifact (Z3 counterexample or Isabelle proof state), we define a ground-truth 'error specification': the specific mathematical property violated, the concrete counterexample or proof state demonstrating the violation, and the minimal conditions under which the error manifests. We then evaluate whether each baseline PRM's rationale for the same step correctly identifies the error specified by the formal artifact, measured via three automated metrics: (i) Error Identification Rate (EIR): does the rationale mention the specific mathematical property that is violated? (ii) Counterexample Alignment (CA): for Z3 steps, does the rationale's explanation align with the formal counterexample's variable assignments? (iii) Proof State Match (PSM): for Isabelle steps, does the rationale reference the proof obligation that actually fails? We evaluate these metrics across our formally grounded PRM, ThinkPRM-14B, GenPRM-7B, R-PRM-7B-DPO, and a vanilla Qwen3-14B prompted with verification instructions. This produces the first automated, scalable benchmark for PRM rationale quality with formal ground truth -- analogous to how ProcessBench evaluates step-level label accuracy, FormalFaithBench evaluates step-level explanation accuracy. We construct the benchmark from ~2-3K held-out error steps (not used in training) with extracted artifacts, and we validate the automated metrics against human judgments on a 200-step subset to establish metric reliability. This contribution is valuable regardless of whether our trained PRM achieves state-of-the-art accuracy: even if formal grounding provides marginal accuracy improvements, the diagnostic methodology enables the community to measure and improve rationale faithfulness across any PRM.\\n\\nImpact beyond the accuracy-transfer framing: We foreground three inherent value propositions that make this work impactful regardless of domain difficulty. (1) Safety-critical deployment: GSM8K-level arithmetic -- multi-step calculations involving unit conversions, proportional reasoning, and chained arithmetic -- is precisely the domain where AI math reasoning is being deployed in practice for financial compliance, engineering safety margins, and pharmaceutical dosing calculations. In these applications, regulators and auditors require not just that a verification system flags an error, but that the flagging comes with a traceable explanation identifying the specific mathematical property violated. Current PRMs provide opaque scores (discriminative) or unverified rationales (generative); formally grounded rationales provide the first verifiably faithful error explanations suitable for auditable deployment. (2) PRM diagnostics: FormalFaithBench (Phase 4C) provides the first automated methodology for measuring whether a PRM's rationale correctly identifies the actual mathematical error, filling a critical evaluation gap. Current metrics (S-Corr, MetaJudge) measure alignment with reference judgments but cannot determine whether the PRM understood the error or reached the right label through spurious reasoning. Our formal error specifications provide deterministic ground truth for this question. (3) Training data integrity: The PRM training ecosystem is built on GSM8K/MATH-derived data. PRM800K labels 75K GSM8K/MATH solutions, OmegaPRM generates 1.5M annotations from similar distributions, FoVer-40K derives from GSM8K-level problems. If rationale quality at this foundational level is unreliable (and R-Align/MetaJudge show ~40-60% spurious correctness/inconsistency rates), the corruption propagates through the entire training pipeline. Improving faithfulness at the source is a leverage point, not a limitation.\\n\\nAcknowledged Limitations and Mitigations. (1) Scope: FoVer's formal verification is validated on GSM8K-level arithmetic and FOL logic. Extending to competition math faces fundamental barriers -- Z3 is undecidable for nonlinear integer arithmetic (confirmed by 'SMT and Functional Equation Solving over the Reals,' 2025), and FormalMATH shows only 16.46% LLM prover success on Lean4 problems. MATH-500 and GPQA-Diamond are explicitly positioned as stretch goals requiring future formalization extensions: specifically, Lean 4 integration (via Safe's autoformalization pipeline) for algebraic reasoning, or SymPy+Z3 (via MATH-VF's approach) for computational verification. We treat this scope limitation as a design choice rather than a weakness: foundational domains are where formal grounding provides deterministic guarantees and where the practical applications (safety-critical, diagnostics, training data) are most compelling. (2) Gaming vulnerability: Kim et al. (2604.19459) show two-stage formalization pipelines are vulnerable to premise mistranslation. Our Z3 formal equivalence check provides stronger detection than LLM-as-judge for axiom-fabrication-type errors (would catch GPT-5's 107 fabricated axioms in their study), but cannot fully guard against symmetric mistranslation at the NL-to-formal boundary. We mitigate via: (a) roundtrip verification from Amrollahi et al., which catches asymmetric errors; (b) NLI-based drift analysis as a secondary signal; (c) restricting to domains (FOL, arithmetic) where formalization ambiguity is lower than natural language. (3) FormalRewardBench shows even frontier LLMs achieve only 59.8% on formal proof evaluation, but our approach uses formal verification tools (Z3, Isabelle) as ground truth rather than LLMs as proof evaluators, sidestepping the generation-evaluation gap within Z3/Isabelle's decidable scope. (4) Cross-domain roundtrip uncertainty: Amrollahi et al.'s roundtrip equivalence rates were measured on statutory text, while our pipeline operates on math/logic formalization. These domains may differ in opposing ways: math/logic has lower linguistic ambiguity and more standardized notation (potentially yielding higher equivalence rates), but non-trivial mathematical steps involve implicit conventions and multi-step dependencies that may resist clean formalization (potentially yielding lower rates). Our Phase 1 pilot validation on 2K steps is specifically designed to calibrate this cross-domain transfer before committing to full-scale synthesis, and we report pilot equivalence rates alongside Amrollahi et al.'s statutory text rates to enable direct comparison. (5) Complementarity with non-formal approaches: 'Outcome Accuracy is Not Enough' (Qwen team, 2602.04649) achieves strong rationale quality improvements through soft semantic matching against human annotations without formal grounding. Our approach provides stronger guarantees (deterministic formal traceability) within a narrower scope; their approach provides broader coverage (any domain with annotations) with softer guarantees. Future work should explore combining formal grounding for in-scope domains with hybrid consistency training for broader coverage. (6) Relationship to concurrent data synthesis work: CVPDS (arXiv 2605.02395) provides an alternative approach to generating verified PRM training data through template-based error injection. While methodologically distinct from proof-artifact extraction, both approaches aim to improve PRM training data quality through formal/symbolic verification. Our approaches are complementary: CVPDS offers controllable error diversity but is constrained by predefined templates, while our method extracts artifacts from naturally occurring LLM errors but requires successful formal verification. Combining controlled error injection with proof-artifact rationale grounding is a promising future direction. (7) FormalFaithBench scope: The diagnostic benchmark is limited to domains where formal verification produces extractable artifacts (currently FOL and GSM8K-level arithmetic). However, the methodology extends naturally as formal verification tools expand to new domains (Lean 4 for algebra via Safe, SymPy+Z3 for computation via MATH-VF), and the benchmark design is explicitly modular to accommodate new artifact types.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"550-750 (solution generation for augmented data ~80h, rationale synthesis with Qwen3-32B ~120h, SFT on 14B model 4xA100 ~100h, evaluation including faithfulness transfer experiment ~100h, downstream policy experiment ~60h, FormalFaithBench construction and evaluation ~40h, ablations ~90h)\",\n      \"engineering_time\": \"Z3 counterexample parsing: ~1-2 weeks; Isabelle proof state extraction: ~2-3 weeks; augmented data generation: ~1 week; roundtrip filter + diagnosis repair: ~1 week; FormalFaithBench metric implementation: ~1 week; downstream RFT pipeline: ~0.5 weeks; integration/testing: ~1 week. Total: 7-9 weeks engineering.\",\n      \"timeline\": \"16-20 weeks\",\n      \"estimated_gpu_cost\": \"$1100-1800 (A100 80GB at ~$2.00/hr on Vast.ai/Spheron)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"550-750 (irreducible training/inference costs unchanged)\",\n      \"engineering_time\": \"4-6 weeks (Claude accelerates Z3 parsing code, Isabelle wrapper modifications, rationale template design, augmented data pipeline, FormalFaithBench metrics, evaluation harness, RFT pipeline)\",\n      \"timeline\": \"12-16 weeks\",\n      \"claude_api_cost\": \"$600-900 (Sonnet 4.6 for pipeline code generation and data analysis, ~120-220M tokens)\",\n      \"estimated_gpu_cost\": \"$1100-1800\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"600-800 (slightly higher from automated ablation sweeps, augmented data generation, faithfulness transfer experiment, downstream policy experiment, FormalFaithBench construction, and pilot experiments)\",\n      \"engineering_time\": \"2-3 weeks (Claude handles most Z3/Isabelle parsing engineering)\",\n      \"timeline\": \"9-12 weeks\",\n      \"claude_api_cost\": \"$1700-2800 (Sonnet 4.6 for end-to-end pipeline orchestration, rationale quality filtering, FormalFaithBench metric design, iterative ablation design, ~450-750M tokens)\",\n      \"estimated_gpu_cost\": \"$1200-1900\",\n      \"speed_bottleneck\": \"Isabelle proof state extraction engineering (~2-3 weeks irreducible due to Isabelle API complexity, though StepProof's engineering precedent reduces unknowns); Z3 counterexample extraction is faster (~1-2 weeks). Formal verification throughput (~2-10s per Z3 step, 15-60s per Isabelle step) is parallelizable across CPU cores. Augmented data generation adds ~1 week for solution generation and verification. Downstream RFT experiment is fast (~50-80h GPU) but depends on Phase 3 model completion. FormalFaithBench construction parallelizes with Phase 3 training.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (projected abstracts Sep 19, full papers Sep 24, 2026 -- 17 weeks; projected from ICLR 2026 pattern, official CFP not yet published as of May 2026; comfortable for human_in_loop and auto_research timelines)\",\n    \"ARR October 2026 cycle -> commitment to NAACL 2027 or ACL 2027 (comfortable backup NLP venue)\",\n    \"AAAI 2027 (abstracts Jul 21, full papers Jul 28, 2026 -- 8 weeks from today, feasible only with auto_research timeline and Z3-only scoped initial submission)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Process Reward Models That Think (arXiv 2025, ThinkPRM)\",\n    \"GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)\",\n    \"R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, She et al.)\",\n    \"Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, FoVer)\",\n    \"Controllable and Verifiable Process Data Synthesis for Process Reward Models (arXiv 2605.02395, May 2026, Chi & Wang)\",\n    \"StepProof: Step-by-step verification of natural language mathematical proofs (arXiv 2506.10558, June 2025, Hu et al.)\",\n    \"Learning to Disprove: Formal Counterexample Generation with Large Language Models (arXiv 2603.19514, March 2026, Li et al.)\",\n    \"FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026)\",\n    \"RM-R1: Reward Modeling as Reasoning (ICLR 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026, Amrollahi et al.)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 @ ICLR 2026, Kim et al.)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2605.10141, May 2026)\",\n    \"Beyond Outcome Verification: Verifiable Process Reward Models (arXiv 2601.17223, Jan 2026, VPRMs)\",\n    \"Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)\",\n    \"R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging (arXiv Feb 2026)\",\n    \"Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models (NeurIPS 2025)\",\n    \"Proof-RM: A Scalable and Generalizable Reward Model for Math Proof (arXiv Feb 2026)\",\n    \"HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)\",\n    \"Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026, PRoSFI)\",\n    \"Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models (arXiv 2602.04649, Feb 2026, Qwen team)\",\n    \"Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2025, MATH-VF)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of LLMs (arXiv 2025)\",\n    \"Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024, OmegaPRM)\",\n    \"GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling (NeurIPS 2025 Workshop)\"\n  ],\n  \"description\": \"We propose Proof-Grounded Generative PRMs, the first process reward models whose verification rationales are traceable to structured formal proof artifacts, and FormalFaithBench, the first automated benchmark for evaluating PRM rationale quality against formal ground truth. Current generative PRMs (ThinkPRM, GenPRM, R-PRM, RM-R1) produce chain-of-thought verification rationales trained on synthetic data of unknown faithfulness -- R-Align shows GenRM decisions exhibit substantial spurious correctness (right label, wrong reasoning), and frontier GenRMs achieve only approximately 40% rationale consistency with human judgments. R-PRM (EMNLP 2025) demonstrates that reasoning-driven evaluation substantially improves PRM accuracy (70.4 F1 on ProcessBench, +13.9 over Qwen2.5-Math-7B-PRM800K at 56.5 F1), but its multi-dimensional analyses are trained on LLM-bootstrapped data and rationale faithfulness is not evaluated. More fundamentally, the field lacks a scalable ground-truth methodology for evaluating WHETHER a PRM's rationale correctly identifies the actual mathematical error: human evaluation doesn't scale, LLM-as-judge achieves only 65-77 F1 (FaithCoT-Bench), and existing automated metrics rely on reference annotations unavailable for most domains. Separately, FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can produce accurate step-level error labels transferring across 12 benchmarks, but generates only binary labels and explicitly excludes reasoning-based PRMs. A concurrent approach (CVPDS, arXiv 2605.02395) synthesizes PRM data through template-based symbolic error injection across 11 error types with 20K instances, but targets accuracy through controlled error diversity rather than rationale faithfulness through proof-artifact grounding. A non-formal approach ('Outcome Accuracy is Not Enough,' Qwen team) improves rationale quality through hybrid consistency-outcome training via soft semantic matching against human annotations, achieving RM-Bench 87.1% (+5% over baselines) -- but relies on human annotation availability and provides softer guarantees than formal artifact tracing. We make three contributions bridging the formal gap. First, we extend FoVer's verification pipeline to extract structured proof artifacts -- Z3 counterexamples from SAT results and Isabelle proof state information at failure points -- going beyond binary labels to structured error specifications. StepProof (Hu et al., 2025) provides engineering precedent for fine-grained Isabelle proof state manipulation on GSM8K, and Learning to Disprove (Li et al., 2026) demonstrates at scale (575K instances) that formal counterexamples serve as effective training signals. Second, we synthesize verification rationales grounded in these artifacts using Qwen3-32B with roundtrip consistency filtering adapted from Amrollahi et al.'s (2604.25031) validated mechanism (45-66% baseline equivalence, 78-86% with standard diagnosis-guided repair, up to 91-95% with cross-model diagnosis; we implement standard same-model repair and conservatively estimate 70-85% post-repair rates on math/logic given cross-domain uncertainty), then fine-tune Qwen3-14B as a generative PRM on these rationales. Starting from FoVer-40K's 20K error steps, we estimate ~9-12K proof-grounded rationales (Scenario A); augmenting FoVer's pipeline yields ~14-17K (Scenario B). Both scenarios exceed ThinkPRM's training data by an order of magnitude with richer per-example signal via formal artifact tracing. Third, we introduce FormalFaithBench: a diagnostic benchmark using ~2-3K held-out proof artifacts as ground-truth error specifications, measuring whether any PRM's rationale correctly identifies the specific mathematical error via three automated metrics (Error Identification Rate, Counterexample Alignment, Proof State Match), validated against 200 human judgments. This fills a critical evaluation gap analogous to ProcessBench for labels: FormalFaithBench evaluates step-level explanation accuracy with formal ground truth. We scope primary evaluation to FoVer-validated domains -- GSM8K-level arithmetic and FOL logic -- targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N as baselines. We foreground three inherent value propositions making this work impactful on foundational domains regardless of transfer: (1) Safety-critical deployment: GSM8K-level arithmetic is the domain for financial compliance, engineering safety margins, and pharmaceutical dosing -- applications requiring auditable error explanations, not just error detection. (2) PRM diagnostics: FormalFaithBench provides the first automated methodology for measuring whether ANY PRM's rationale correctly identifies the actual mathematical error, enabling systematic debugging of PRM failure modes. (3) Training data integrity: GSM8K is the foundation of PRM training pipelines (PRM800K, FoVer, OmegaPRM); improving rationale faithfulness at this level prevents corrupted supervision from propagating. We additionally include three dedicated experiments: (A) faithfulness transfer measuring S-Corr on ProcessBench-MATH/Olympiad for our model versus baselines including R-PRM-7B-DPO and a binary-label ablation; (B) downstream policy via rejection sampling fine-tuning of Qwen2.5-Math-1.5B on 500 GSM8K + 500 MATH problems; (C) FormalFaithBench evaluation of five PRMs with metric reliability validation. We acknowledge scope limitations (Z3 undecidability for nonlinear arithmetic; FormalMATH's 16.46% prover success), treat them as a design choice favoring deterministic guarantees on foundational domains, and position the methodology as extensible as formal verification tools expand.\",\n  \"project_name\": \"proof_grounded_genprm\",\n  \"source\": \"web_research\",\n  \"reviewer_response\": {\n    \"issue_1_faithful_autoformalization_numbers\": \"ADDRESSED (MODERATE, round 4). Corrected landscape statement from '85-95% with diagnosis-guided repair' to precise numbers verified from Table 1, Section 7.1 of Amrollahi et al.: standard diagnosis-guided repair (same model) achieves 77.9%-85.7% equivalence, while cross-model diagnosis (Claude performs diagnosis, GPT executes pipeline) achieves 90.7%-94.7%. All instances updated throughout.\",\n    \"issue_2_hybrid_training_positioning\": \"ADDRESSED (MODERATE, round 4). Added 'Outcome Accuracy is Not Enough' (Qwen team, arXiv 2602.04649) to the landscape with detailed positioning as complementary non-formal approach.\",\n    \"issue_3_faithfulness_transfer_experiment\": \"ADDRESSED (MINOR, round 4). Added dedicated faithfulness transfer experiment to Phase 4 with four-way comparison and ablation.\",\n    \"issue_4_crossdomain_roundtrip_uncertainty\": \"ADDRESSED (MINOR, round 4). Added explicit acknowledgment of cross-domain uncertainty with pilot calibration strategy.\",\n    \"issue_5_rprm_baseline\": \"ADDRESSED (MODERATE, round 5). Added R-PRM (EMNLP 2025, She et al.) comprehensively to the landscape with detailed methodology and results.\",\n    \"issue_6_cvpds_concurrent_work\": \"ADDRESSED (MODERATE, round 5). Added CVPDS (arXiv 2605.02395, Chi & Wang, May 2026) to the landscape with detailed methodology.\",\n    \"issue_7_downstream_rlhf_experiment\": \"ADDRESSED (MINOR, round 5). Added Phase 4(B) downstream policy experiment.\",\n    \"issue_8_iclr2027_deadline_tentative\": \"ADDRESSED (MINOR, round 5). ICLR 2027 deadline now explicitly noted as projected.\",\n    \"issue_9_ralign_claims_clarification\": \"ADDRESSED (MINOR, round 5). R-Align description now distinguishes between abstract-level and full-paper claims.\",\n    \"issue_10_rprm_baseline_f1_correction\": \"ADDRESSED (MINOR, round 7). Corrected Qwen2.5-Math-7B-PRM800K baseline from 58.5 F1 to 56.5 F1 throughout. The improvement claim (+13.9 F1) and R-PRM-7B-DPO score (70.4 F1) remain correct: 70.4 - 56.5 = 13.9.\",\n    \"issue_11_stepproof_acknowledgment\": \"ADDRESSED (MINOR, round 7). Added StepProof (arXiv 2506.10558, Hu et al., June 2025) to landscape with detailed methodology: step-by-step Isabelle-based autoformalization on GSM8K, incremental proof state management with accumulative context and selective backtracking, 27.9% proof pass rate. Referenced as engineering precedent in Phase 1(b) for Isabelle proof state extraction, reducing engineering risk. Added to key references and gap analysis.\",\n    \"issue_12_learning_to_disprove_acknowledgment\": \"ADDRESSED (MINOR, round 7). Added 'Learning to Disprove' (arXiv 2603.19514, Li et al., March 2026) to landscape: symbolic mutation strategy producing 575K counterexample instances from 321K seed theorems in Lean 4, 74% improvement over baselines, multi-reward expert iteration. Positioned as demonstrating scalable formal counterexample generation as training signals -- conceptual parallel supporting our approach. Distinguished: they train generators to produce counterexamples, we extract counterexamples from tools to ground verifier rationales. Referenced in data sufficiency argument. Added to key references and gap analysis.\",\n    \"issue_13_impact_ceiling_reframing\": \"ADDRESSED (STRUCTURAL, round 7). MAJOR REFRAMING of the contribution's value proposition. Instead of positioning formal grounding as primarily valuable through transfer to harder domains (which remains a secondary hypothesis), we now foreground three inherent-value propositions that make easy-domain formal grounding valuable regardless of transfer: (1) Safety-critical deployment: GSM8K-level arithmetic IS the deployment domain for financial compliance, engineering safety margins, pharmaceutical dosing -- applications where auditable error explanations are legally required, not just error detection. (2) PRM diagnostics: Introduced FormalFaithBench as a second core contribution (Phase 4C) -- the first automated benchmark for PRM rationale quality with formal ground truth, measuring Error Identification Rate, Counterexample Alignment, and Proof State Match. This is valuable regardless of our trained PRM's accuracy because it provides the community with a tool for measuring and improving rationale faithfulness across ANY PRM. Analogous to ProcessBench for step labels but for step explanations. (3) Training data integrity: Made the 'GSM8K as foundation' argument central -- PRM800K, OmegaPRM, FoVer all build on GSM8K-level data, so improving faithfulness at this level is a high-leverage intervention, not a limitation. Restructured core_problem to frame the evaluation gap alongside the training gap. Updated title to reflect dual contribution. Repositioned scope limitation as a deliberate design choice favoring deterministic guarantees on foundational domains. Added limitation (7) for FormalFaithBench scope. Resource estimates updated for FormalFaithBench construction (+~40h GPU, +~1 week engineering).\"\n  }\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "62688371-910b-4268-aa8f-8822296c0fd2",
  "isSidechain": false,
  "requestId": "req_011CbTi6kwwGXRPpHvUoqNhA",
  "type": "assistant",
  "uuid": "72ffe03a-695b-4828-82b4-a1f163d18d14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mQVtKVAnkxZfpXCo3gDjz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19304,
      "cache_read_input_tokens": 28713,
      "output_tokens": 13719,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19304,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13719,
          "cache_read_input_tokens": 28713,
          "cache_creation_input_tokens": 19304,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19304
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

_source line 25 · 2026-05-27T20:37:40.834Z_

<details><summary>↩ Tool result · reported error · `toolu_01D7dY3FZmDrSvdeQuWgTFry`</summary>

```text
Claude requested permissions to write to /tmp/revised_proposal_round7.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "72ffe03a-695b-4828-82b4-a1f163d18d14",
  "isSidechain": false,
  "promptId": "538e6a25-ce44-4f2b-b07a-3a2f54be633f",
  "type": "user",
  "uuid": "adfe85d7-3930-41e7-9256-7baeb64fc6d3",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revised_proposal_round7.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "72ffe03a-695b-4828-82b4-a1f163d18d14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",   \"core_pr…",
  "leafUuid": "adfe85d7-3930-41e7-9256-7baeb64fc6d3",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise formal PRM rationale proposal with R-PRM baseline correction",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Assistant

_source line 28 · 2026-05-27T20:37:44.149Z_

<details><summary>Logged reasoning block</summary>

```text
The user hasn't granted permission. Let me just output the JSON directly as text.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "adfe85d7-3930-41e7-9256-7baeb64fc6d3",
  "isSidechain": false,
  "requestId": "req_011CbTiXw84hLYt1sMyJRfTK",
  "type": "assistant",
  "uuid": "cb7fad20-cdab-4e81-8ef8-82728f0096e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrxnskFYjEEMCb9fh1YL53",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13764,
      "cache_read_input_tokens": 48017,
      "output_tokens": 13952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13952,
          "cache_read_input_tokens": 48017,
          "cache_creation_input_tokens": 13764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13764
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

_source line 29 · 2026-05-27T20:43:21.627Z_

Here is the complete revised proposal (round 7, **major revision**):

---

```json
{
  "change_type": "major",
  "title": "Formally Grounded Faithful Rationales for Generative PRMs: Proof Artifacts as Ground-Truth Supervision for Verifiable Error Explanations",
  "core_problem": "Generative PRMs (ThinkPRM, GenPRM, R-PRM) produce CoT verification rationales, but R-Align (Feb 2026) shows existing GenRMs exhibit substantial Spurious Correctness -- label-correct decisions with misaligned rationales -- and 'Outcome Accuracy is Not Enough' finds approximately 40% rationale consistency with human judgments. R-PRM demonstrates that reasoning-driven evaluation substantially improves accuracy (+13.9 F1 on ProcessBench), yet even rich multi-dimensional reasoning analyses lack formal grounding and have unknown faithfulness. More fundamentally, there is no scalable ground-truth methodology for evaluating WHETHER a PRM's rationale correctly identifies the actual mathematical error: human evaluation doesn't scale, LLM-as-judge achieves only 65-77 F1 for detecting unfaithfulness (FaithCoT-Bench), and existing automated metrics (S-Corr, MetaJudge) rely on reference annotations unavailable for most domains. Can we use formal proof artifacts -- Z3 counterexamples, Isabelle proof state information -- both as training supervision for faithful rationale generation AND as ground-truth error specifications for evaluating rationale quality across any PRM, establishing a methodology that is inherently valuable on foundational domains regardless of transfer to harder problems?",
  "opportunity": "The field faces a measurement problem alongside a training problem: we lack ground-truth for what constitutes a faithful PRM rationale. GenRM reviewer 3 raised the unresolved concern that CoT rationales may be 'plausible-sounding but unfaithful reasoning that happens to correlate with correct verdicts.' But detecting this requires knowing what the ACTUAL error is -- which formal verification uniquely provides. FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can generate step-level error labels transferring across 12 benchmarks, but FoVer explicitly restricts to classification-based PRMs producing only binary labels, excluding generative/reasoning-based PRMs. R-PRM (EMNLP 2025) shows that reasoning-driven step evaluation -- generating multi-dimensional analyses before judgments -- substantially improves PRM accuracy (+13.9 F1 on ProcessBench via DPO), but its rationales are trained on LLM-generated seed data without formal grounding and faithfulness is not evaluated. ThinkPRM generates rich verification CoTs but trains on synthetic rationales of unknown faithfulness. The untried bridge is extracting structured proof artifacts -- Z3 counterexamples, Isabelle proof state information -- from FoVer's verification pipeline and using them as both (a) grounding signals for ThinkPRM-style rationale generation and (b) ground-truth error specifications for a new diagnostic evaluation methodology (FormalFaithBench). This fills two gaps simultaneously: the training gap (reasoning-driven methods leave rationale faithfulness ungrounded) and the evaluation gap (no scalable automated method exists for measuring whether a PRM's explanation correctly identifies the mathematical error). Three arguments establish the inherent value of this contribution on foundational domains, independent of transfer to harder problems: (1) Safety-critical deployment: GSM8K-level arithmetic IS the domain for financial calculations, engineering computations, and medical dosing -- applications where knowing WHY a step is wrong is legally and operationally required, not just whether it's wrong. Current PRMs provide only opaque scores or unverified rationales for these critical applications. (2) PRM diagnostics and debugging: Formally grounded error specifications establish a reference standard for measuring rationale quality across ALL PRMs -- analogous to how PRM800K provides ground-truth step labels, our FormalFaithBench provides ground-truth explanations, enabling the first automated methodology for evaluating whether any PRM's rationale correctly identifies the actual mathematical error. (3) Training data integrity: GSM8K-level problems are the primary source for PRM training data construction (PRM800K, FoVer, OmegaPRM's 1.5M annotations all derive from or include GSM8K/MATH). Ensuring rationale faithfulness at this foundational level prevents corrupted supervision signals from propagating to all downstream applications -- improving the foundation rather than patching the symptoms. Critically, Faithful Autoformalization (Amrollahi et al., April 2026) has now validated and quantified the roundtrip verification mechanism we adopt for quality filtering, showing 45-66% baseline equivalence rates improvable to 78-86% with standard diagnosis-guided repair or up to 91-95% with cross-model diagnosis -- providing empirical grounding for our data pipeline feasibility. Moreover, FoVer itself demonstrates easy-to-difficult transfer: PRMs trained on GSM8K-level data significantly improve step-level verification on MATH (88.0% vs 78.2% baseline), OlympiadBench (84.0% vs 76.2%), and Omni-Math (84.5% vs 73.6%), suggesting that improving rationale faithfulness on foundational domains may propagate to harder reasoning tasks -- though we treat this as a secondary hypothesis to test rather than a core claim.",
  "landscape": "ThinkPRM (arXiv 2025) achieves 8% improvement on GPQA-Diamond over discriminative verifiers using only 1% of PRM800K labels (specifically 1K synthetic verification CoTs filtered to ~8K step labels), but its rationales lack formal grounding. GenPRM (AAAI 2026) combines CoT with code verification, enabling 1.5B models to outperform GPT-4o on ProcessBench using only 23K training examples. R-PRM (EMNLP 2025) introduces reasoning-driven process reward modeling: it generates multi-dimensional step analyses (Previous Steps Analysis, Now Step Analysis, Data Source Analysis, Consistency Analysis, Calculation Analysis) followed by binary judgments. Using Qwen2.5-Math-7B-Instruct as the base model, R-PRM-7B-DPO achieves 70.4 F1 on ProcessBench (+13.9 over Qwen2.5-Math-7B-PRM800K at 56.5 F1) and +8.5 F1 on PRMBench, with consistent +8.6 accuracy improvements on six downstream math reasoning datasets via best-of-N selection. R-PRM trains on ~289K SFT samples and ~269K DPO pairs bootstrapped from PRM800K annotations, achieving comparable performance to Qwen2.5-Math-PRM with only ~15% of its data volume. Critically, while R-PRM produces rich natural-language reasoning for each step evaluation, it does not evaluate rationale faithfulness -- the analyses are trained on LLM-generated seed data and may exhibit the same spurious correctness that R-Align identifies in other GenRMs. R-PRM demonstrates the ceiling of what reasoning-driven evaluation achieves without formal grounding: substantial accuracy gains, but with unknown rationale fidelity to the actual mathematical errors. FoVer (ACL 2026 Findings) uses Z3/Isabelle for automated step-level labeling with easy-to-difficult transfer (trained on GSM8K-level, evaluates on MATH/AIME/Olympiad), but produces only binary labels and explicitly excludes reasoning-based PRMs citing 'substantially higher computational costs.' FoVer-40K contains 40,000 balanced training steps (20K formal logic from FLDx2 + 20K theorem proving from GSM8K-level problems) with 50% error rate, generated from solutions by Llama 3.1 8B and Qwen 2.5 7B; the raw unbalanced pipeline output is substantially larger (~216K steps from 10K problems per task across both models). 'Controllable and Verifiable Process Data Synthesis for Process Reward Models' (arXiv 2605.02395, Chi & Wang, May 2026) is concurrent work that synthesizes PRM training data through a four-stage pipeline: constructing correct symbolic reasoning chains from rule templates, injecting template-aware errors into intermediate steps, symbolically recomputing subsequent steps to maintain trajectory consistency, and verifying that injected errors are not derivable from the prefix. They produce 20K paired (correct, erroneous) trajectories across 11 error types (7 truth-state: drop_condition, implication_misuse, or_and_confusion, partial_evaluation, xor_as_or, xor_as_equiv, vacuous_truth_error; 4 structural: converse_error, redundant_step, missing_prerequisite, circular_reference), translated into natural-language processes for PRM training. Their method improves best-of-8 reranking on logical reasoning benchmarks (Llama-3.1-8B: 0.528 -> 0.591, Qwen-2.5-7B: 0.567 -> 0.615 average F1), with limited transfer to mathematics (ProcessBench GSM8K: 21.2% F1). The key methodological distinction from our work: they generate controlled synthetic errors through template-based injection for accuracy-focused PRM training, while we extract genuine proof artifacts from naturally occurring errors in LLM solutions for faithfulness-focused rationale grounding. Their error diversity is constrained by predefined templates (an acknowledged limitation), while our artifacts reflect the actual distribution of errors that LLMs make. The two approaches are complementary -- their controlled error injection could extend the diversity of training scenarios, while our proof-artifact extraction provides traceable explanations of why each error is wrong. StepProof (arXiv 2506.10558, Hu et al., June 2025) performs step-by-step Isabelle-based autoformalization and verification on GSM8K, achieving 27.9% proof pass rate with 10 attempts (vs. 25.3% for full-proof baselines with 64 attempts). The key engineering contribution is incremental proof state management: verified steps accumulate into context for subsequent steps, failed steps can be selectively backtracked, and a 'suspension' mechanism allows skipping hard-to-formalize steps while preserving proof context. StepProof provides directly relevant engineering precedent for our Phase 1(b) Isabelle proof state extraction -- their interactive interface with color-coded verification status (green=verified, yellow=suspended, unmarked=failed) and accumulative proof stack demonstrate feasibility of fine-grained Isabelle proof state manipulation, though their goal is proof construction rather than proof artifact extraction for rationale grounding. 'Learning to Disprove: Formal Counterexample Generation with Large Language Models' (arXiv 2603.19514, Li et al., March 2026) trains LLMs to generate formal counterexamples verified in Lean 4 via a symbolic mutation strategy, producing 575,039 counterexample instances from 321,929 seed theorems. Their multi-reward expert iteration achieves 74% improvement over baselines on their For-Counter benchmark. While using Lean 4 rather than Z3/Isabelle, the conceptual parallel of using formal counterexamples as verified training signals directly supports our approach. Their scale (575K instances) demonstrates that formal counterexample generation is tractable, and their finding that dual reward signals improve training efficiency suggests our proof-artifact-grounded rationales may similarly provide richer supervision than binary labels. The key distinction is that they train generators to produce counterexamples, while we extract counterexamples from verification tools to ground verifier rationales. RM-R1 (ICLR 2026) trains reasoning reward models with explicit rationale chains but without formal grounding. R-Align (Feb 2026) introduces the Spurious Correctness (S-Corr) metric showing existing GenRMs exhibit substantial spuriously correct decisions (the abstract reports 'substantial S-Corr even for competitive GenRMs'; specific rates per model and the experimental evidence that higher S-Corr predicts downstream policy degeneration during RLHF are detailed in the full paper's experimental tables rather than the publicly excerptable abstract), providing the key diagnostic our work aims to improve. 'Outcome Accuracy is Not Enough' (Qwen team, Feb 2026, arXiv 2602.04649) introduces a competing non-formal approach to improving rationale quality: they define Rationale Consistency via MetaJudge, which decomposes human rationales into atomic claims and performs strict one-to-one semantic matching against model justifications, finding frontier GenRMs achieve only ~40% rationale consistency. They train with a multiplicative hybrid signal R_final = R_rationale * R_outcome via GRPO, achieving RM-Bench 87.1% and JudgeBench 82.0% (+5% over outcome-only baselines, +7% on Arena Hard v2 creative writing during RLHF). Crucially, their approach targets Judge faithfulness (evaluation rationale quality) rather than Solver verification, and relies on soft semantic matching against human annotations -- providing broader applicability but weaker guarantees than formal artifact tracing. Their acknowledged limitation is scalability: computing rationale consistency still requires high-quality human annotations. Our formal grounding provides deterministic, traceable guarantees within Z3/Isabelle's decidable scope, while their approach extends to any domain with human annotations. The two methods are complementary: formal grounding where verification tools cover the domain, hybrid consistency training for broader applicability. Think-RM (NeurIPS 2025) shows that deep, long-horizon reasoning inside reward models -- including self-reflection and hypothetical reasoning -- is critical for accurate evaluation, achieving +8% over CoT-GenRMs on RM-Bench. Proof-RM (Feb 2026) provides a scalable pipeline for training reward models on mathematical proof verification with RL stabilization ('LLM-as-a-RM-for-RM'), reaching 82.4% accuracy at 32B on competition-level proofs (IMO/CMO/USAMO), but produces scores rather than formally grounded rationales. Safe (ACL 2025) demonstrates Lean 4 step-level verification of NL math reasoning with the FormalStep benchmark (30,809 formal statements), achieving interpretable verification evidence complementary to PRM scores -- the closest work on formal verification for step-level reasoning, but producing verification states rather than natural-language rationales. FaithCoT-Bench (ICLR 2026) benchmarks CoT faithfulness, finding LLM-as-judge methods achieve 65-77 F1 for detecting unfaithfulness. Faithful Autoformalization (arXiv 2604.25031, Amrollahi et al., Stanford) proposes and quantifies a roundtrip verification mechanism (formalize -> back-translate -> re-formalize -> Z3 equivalence check) achieving 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model performs diagnosis and repair), or up to 91-95% with cross-model diagnosis (Claude performs diagnosis while GPT executes the pipeline) -- the cross-model improvement demonstrates that the diagnosis function is the performance bottleneck, not the pipeline itself. 'Do LLMs Game Formalization?' (arXiv 2604.19459, VerifAI-2 @ ICLR 2026) finds no systematic gaming in unified generation (Fleiss kappa 0.92) but reveals that DeepSeek-R1 mistranslates premises in two-stage pipelines, producing internally consistent but unfaithful outputs undetectable by LLM-as-judge -- a vulnerability partially addressed by Z3 formal equivalence checks but fundamentally bounded at the NL-to-formal boundary. FormalRewardBench (arXiv 2605.10141, May 2026) shows frontier LLMs achieve only 59.8% pairwise accuracy on formal proof evaluation (Lean 4, MiniF2F problems) while specialized provers achieve only 24.4%, revealing a generation-evaluation gap that motivates using formal tools (not LLMs) as ground truth for rationale grounding. VPRMs (arXiv 2601.17223, Jan 2026) demonstrate that deterministic rule-based step verification dramatically outperforms neural PRMs (87.9% vs 52.4% for GPT-4 on medical evidence synthesis), but are limited to domains with explicit procedural guidelines -- our approach extends this paradigm from rule-based to proof-based verification with stronger mathematical guarantees but narrower initial scope. PRoSFI (arXiv March 2026) uses formal verification as a reward signal during RL training of generators via structured formal intermediaries -- targets generator training, not verifier rationale grounding. HERMES (ICML 2026) interleaves informal reasoning with Lean4-verified proof steps for generators. GroundedPRM (NeurIPS 2025 Workshop) uses MCTS plus tool execution for fidelity-aware supervision with execution-based grounding. MATH-VF (arXiv 2025) combines SymPy+Z3 for step-wise formal verification on MATH-500 and ProcessBench, producing corrective feedback beyond binary labels -- demonstrating that Z3-based step verification can extend to domains beyond GSM8K-level arithmetic. FormalMATH (arXiv 2025) benchmarks formal theorem proving with 5,560 Lean4 problems showing even the strongest provers achieve only 16.46% success under practical budgets, with pronounced domain bias favoring algebra over calculus/applied math -- grounding our scope restriction to GSM8K-level problems. No existing work connects structured formal proof artifacts to generative PRM rationale training or uses them as ground-truth error specifications for rationale quality evaluation: FoVer provides binary labels without explanations, ThinkPRM/GenPRM/R-PRM provide explanations without formal grounding, Safe provides formal verification states without NL rationales, Proof-RM scores proof quality without rationale generation, StepProof performs step-level Isabelle verification but targets proof construction rather than rationale grounding, Learning to Disprove generates formal counterexamples but for generator training rather than verifier rationale quality, R-Align diagnoses spurious correctness without formal remedies, VPRMs use rule-based not proof-based verification, CVPDS uses template-based error injection rather than genuine proof artifact extraction, and 'Outcome Accuracy is Not Enough' improves rationale quality through soft semantic matching rather than deterministic formal grounding.",
  "inspired_by": "Field guide Gap 6 (faithfulness of CoT verification rationales in GenRM -- 'never fully resolved'), R-Align's demonstration that substantial GenRM decisions are spuriously correct, R-PRM's demonstration that reasoning-driven evaluation improves accuracy without addressing faithfulness, FormalRewardBench's finding that LLMs cannot reliably evaluate formal proofs (motivating tool-based grounding), the untried bridge between FoVer's formal proof artifacts and ThinkPRM's rationale generation, and the broader insight that PRM rationale faithfulness lacks a ground-truth evaluation methodology analogous to PRM800K's step-level labels",
  "approach": "We make three contributions: (1) a training methodology that grounds generative PRM rationales in formal proof artifacts, (2) FormalFaithBench, a diagnostic evaluation benchmark that uses proof artifacts as ground-truth error specifications for measuring any PRM's rationale quality, and (3) empirical evidence on the inherent value of formally grounded rationales for safety-critical applications, PRM diagnostics, and training data integrity. We scope primary evaluation to domains where FoVer's formal verification pipeline is validated: GSM8K-level arithmetic (Isabelle) and first-order logic tasks (Z3 on FOLIO/LogicNLI). We evaluate transfer to harder domains as a secondary analysis, with dedicated experiments testing whether formal grounding's faithfulness benefits propagate via the same easy-to-difficult mechanism FoVer demonstrated for accuracy, and whether reduced S-Corr translates to improved downstream policy training.\n\nPhase 1 -- Data Preparation and Proof Artifact Extraction (~3-4 weeks engineering). We begin from FoVer-40K, the published balanced training dataset containing 40,000 steps (20K formal logic + 20K theorem proving) at 50% error rate. This yields 20,000 error steps as the base for artifact extraction. Additionally, we augment the base data by re-running FoVer's open-source pipeline on additional problems: FoVer sampled only 10,000 problems per task from much larger source datasets -- FLDx2 contains 100K+ formal logic problems, while MetaMathQA provides 395K math problems. By sampling an additional 10K problems per task and generating solutions from one additional LLM (e.g., Qwen3-8B), we estimate producing ~40K additional error steps at similar error rates (logic ~42%, proof ~14%), yielding a combined pool of ~30K error steps for artifact extraction. We extract artifacts in two tracks: (a) For Z3-verified logic steps, we extract structured counterexamples from SAT results. Z3 natively produces satisfying models when a formula is satisfiable, so for each incorrect step we obtain variable assignments demonstrating the error. This is primarily a parsing and templating task (~1-2 weeks). We estimate ~95% of incorrect logic steps yield extractable counterexamples, since Z3 reliably produces models for SAT results. (b) For Isabelle-verified theorem proving steps, we modify FoVer's Isabelle wrapper to capture proof state information at failure points -- the current goal, available hypotheses, and which tactic failed (~2-3 weeks, requiring deeper Isabelle API integration). StepProof (Hu et al., 2025) provides directly relevant engineering precedent: their incremental proof state management system on GSM8K demonstrates feasibility of fine-grained Isabelle proof state manipulation with accumulative verified-step context, selective backtracking, and proof state suspension -- reducing our engineering risk for this track. We estimate ~60-70% of incorrect steps yield usable proof state artifacts, as some failures occur in preprocessing before meaningful state is available. Pilot validation: we run artifact extraction on a 2K-step sample (1K logic, 1K arithmetic) in week 1 to calibrate yield estimates before full-scale extraction. This pilot also calibrates cross-domain roundtrip equivalence rates (see Phase 2), since math/logic formalization may differ from Amrollahi et al.'s statutory text domain in both directions: math/logic has lower linguistic ambiguity (potentially favoring higher equivalence rates) but higher formalization difficulty for non-trivial steps involving implicit mathematical conventions (potentially favoring lower rates). The pilot's empirical calibration resolves this directional uncertainty before committing to full-scale synthesis.\n\nPhase 2 -- Proof-Grounded Rationale Synthesis (~3 weeks). We use Qwen3-32B to synthesize natural-language verification rationales grounded in extracted artifacts. Each rationale template incorporates the specific artifact (e.g., 'Step 3 claims x+y>10, but the counterexample x=3, y=2 shows this fails' for Z3; 'The proof state after step 4 has unsolved goal involving P(n+1), but the applied tactic only handles the base case' for Isabelle). We apply roundtrip consistency filtering adapted from Amrollahi et al. (2604.25031): each generated rationale is re-formalized and checked for Z3/Isabelle semantic equivalence with the original artifact. Amrollahi et al. report 45-66% baseline equivalence on statutory text, improvable to 78-86% with standard diagnosis-guided repair (same model) or 91-95% with cross-model diagnosis (a separate LLM performs only the diagnosis step while the primary model executes the pipeline). We implement standard same-model diagnosis-guided repair using Qwen3-32B as both diagnostician and pipeline executor, following their finding that scoped stage-level diagnosis outperforms random-stage repair. We do not implement cross-model diagnosis in the initial pipeline to avoid the additional complexity and cost of routing diagnosis through a separate LLM, but note it as an available improvement lever if standard repair yields insufficient throughput. Given the directional uncertainty in cross-domain transfer (math/logic vs. statutory text), we conservatively estimate 50-65% baseline pass rate on our domains, improvable to 70-85% with standard diagnosis-guided repair. The Phase 1 pilot on 2K steps will empirically calibrate these estimates before full-scale synthesis. Data yield estimate with two scenarios:\n\n  Scenario A (FoVer-40K only, conservative): Starting from ~20K error steps -> ~16K with extractable artifacts (9.5K Z3 at 95% + 6.5K Isabelle at 65%) -> ~11.2-13.6K after roundtrip+repair filtering at ~70-85% -> ~9.5-11.6K after ~15% final quality filtering. Final: ~9-12K proof-grounded rationales.\n\n  Scenario B (FoVer-40K + augmented pipeline): Starting from ~30K error steps -> ~24K with extractable artifacts (15K Z3 + 9K Isabelle) -> ~16.8-20.4K after roundtrip filtering -> ~14.3-17.3K after quality filtering. Final: ~14-17K proof-grounded rationales.\n\n  Data sufficiency argument: ThinkPRM achieves competitive performance with only 1K synthetic verification CoTs (~8K step labels), GenPRM uses 23K training examples, and R-PRM uses ~289K SFT samples but achieves comparable performance to Qwen2.5-Math-PRM with only ~15% of its data. Our conservative Scenario A of ~9-12K formally grounded rationales represents ~10x ThinkPRM's training data and is comparable to GenPRM's scale. Moreover, our rationales carry richer supervision signal than any of these: each rationale is traceable to a specific formal proof artifact with verified semantic grounding, whereas ThinkPRM's rationales are filtered only on label match, GenPRM's use execution-based but not proof-based verification, and R-PRM's are bootstrapped from LLM-generated seed data without formal grounding. Learning to Disprove (Li et al., 2026) demonstrates at scale (575K counterexamples from 321K seed theorems) that formal counterexamples serve as effective training signals, supporting our premise that proof artifacts provide rich supervision. We thus expect higher per-example training signal quality, partially compensating for any quantity gap.\n\nPhase 3 -- SFT Training (~2 weeks). We fine-tune Qwen3-14B (or DeepSeek-R1-Distill-Qwen-14B) as a generative PRM on the proof-grounded rationales following ThinkPRM's SFT recipe. We train separate models on Z3-grounded logic rationales, Isabelle-grounded arithmetic rationales, and the combined set to enable ablation of each grounding source's contribution.\n\nPhase 4 -- Evaluation (~4-5 weeks). Verification accuracy is evaluated on: (primary) ProcessBench-GSM8K subset, FOLIO, LogicNLI; (transfer) ProcessBench-MATH/Olympiad subsets, MATH-500 best-of-N; targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N scores as baselines. Rationale faithfulness is assessed via three independent metrics, strictly separated from training: (1) R-Align's Spurious Correctness (S-Corr) as the primary automated faithfulness metric, computed by comparing rationale reasoning against golden reference judgments from ProcessBench annotations; (2) FaithCoT-Bench detection metrics (precision, recall, F1); (3) human evaluation on 150-200 randomly sampled rationales, rating formal grounding quality and error identification accuracy. Roundtrip consistency is reported ONLY as a supplementary training-data-quality indicator and correlation analysis (does higher roundtrip score predict higher human-rated quality?), not as a primary evaluation metric or novel contribution.\n\nCritically, Phase 4 includes three dedicated experiments that go beyond standard PRM evaluation:\n\n(A) Faithfulness transfer experiment. We measure S-Corr on ProcessBench-MATH and ProcessBench-Olympiad for: (a) our formally grounded model trained only on GSM8K-level/FOL rationales; (b) ThinkPRM-14B baseline; (c) GenPRM-7B baseline; (d) R-PRM-7B-DPO baseline (the strongest reasoning-based PRM without formal grounding -- testing whether rich reasoning analyses alone reduce S-Corr); (e) an ablation model trained on FoVer-40K binary labels (no formal rationale grounding). This experiment disentangles four claims: (i) does formal grounding reduce S-Corr on in-domain tasks (GSM8K, FOL)? (ii) does the S-Corr reduction transfer to harder domains (MATH, Olympiad) via the same easy-to-difficult mechanism FoVer demonstrated for accuracy? (iii) does the transfer specifically require rationale-level formal grounding, or does any FoVer-derived training signal suffice? (iv) does R-PRM's reasoning-driven evaluation reduce S-Corr relative to simpler baselines -- isolating whether accuracy-improving reasoning also improves faithfulness, or whether formal grounding provides an orthogonal faithfulness benefit? If (i) holds but (ii) doesn't, we still demonstrate improved faithfulness within the validated scope. If both hold, we provide the first empirical evidence that formal rationale grounding at the foundational training-data level propagates to harder reasoning tasks.\n\n(B) Downstream policy experiment. To close the full causal chain (formal grounding -> reduced S-Corr -> better downstream policy), we conduct a small-scale rejection sampling experiment. We generate N=8 candidate solutions per problem for 500 GSM8K and 500 MATH problems using Qwen2.5-Math-1.5B-Instruct as the policy model, then select the best response according to each PRM: (a) our formally grounded PRM; (b) ThinkPRM-14B; (c) R-PRM-7B-DPO; (d) FoVer-trained discriminative PRM (binary labels). We report pass@1 accuracy of the selected solutions (best-of-N evaluation) and, as a stronger test, perform rejection sampling fine-tuning (RFT): we fine-tune Qwen2.5-Math-1.5B on the top-ranked solutions selected by each PRM (filtering to solutions verified as correct), then evaluate the resulting policy models on held-out MATH-500 and GSM8K test sets. R-Align demonstrates that S-Corr predicts RLHF policy degeneration (as established in the paper's experimental analysis); our experiment directly tests whether formally grounded rationale selection -- by reducing spurious correctness in the reward signal -- yields better-trained policies. This is a modest-cost experiment (~50-80 GPU hours for generation + RFT on 1.5B model) that could provide the strongest possible impact argument.\n\n(C) FormalFaithBench: Diagnostic evaluation of PRM rationale quality. This experiment constitutes a standalone methodological contribution. For each error step where we have extracted a formal proof artifact (Z3 counterexample or Isabelle proof state), we define a ground-truth 'error specification': the specific mathematical property violated, the concrete counterexample or proof state demonstrating the violation, and the minimal conditions under which the error manifests. We then evaluate whether each baseline PRM's rationale for the same step correctly identifies the error specified by the formal artifact, measured via three automated metrics: (i) Error Identification Rate (EIR): does the rationale mention the specific mathematical property that is violated? (ii) Counterexample Alignment (CA): for Z3 steps, does the rationale's explanation align with the formal counterexample's variable assignments? (iii) Proof State Match (PSM): for Isabelle steps, does the rationale reference the proof obligation that actually fails? We evaluate these metrics across our formally grounded PRM, ThinkPRM-14B, GenPRM-7B, R-PRM-7B-DPO, and a vanilla Qwen3-14B prompted with verification instructions. This produces the first automated, scalable benchmark for PRM rationale quality with formal ground truth -- analogous to how ProcessBench evaluates step-level label accuracy, FormalFaithBench evaluates step-level explanation accuracy. We construct the benchmark from ~2-3K held-out error steps (not used in training) with extracted artifacts, and we validate the automated metrics against human judgments on a 200-step subset to establish metric reliability. This contribution is valuable regardless of whether our trained PRM achieves state-of-the-art accuracy: even if formal grounding provides marginal accuracy improvements, the diagnostic methodology enables the community to measure and improve rationale faithfulness across any PRM.\n\nImpact beyond the accuracy-transfer framing: We foreground three inherent value propositions that make this work impactful regardless of domain difficulty. (1) Safety-critical deployment: GSM8K-level arithmetic -- multi-step calculations involving unit conversions, proportional reasoning, and chained arithmetic -- is precisely the domain where AI math reasoning is being deployed in practice for financial compliance, engineering safety margins, and pharmaceutical dosing calculations. In these applications, regulators and auditors require not just that a verification system flags an error, but that the flagging comes with a traceable explanation identifying the specific mathematical property violated. Current PRMs provide opaque scores (discriminative) or unverified rationales (generative); formally grounded rationales provide the first verifiably faithful error explanations suitable for auditable deployment. (2) PRM diagnostics: FormalFaithBench (Phase 4C) provides the first automated methodology for measuring whether a PRM's rationale correctly identifies the actual mathematical error, filling a critical evaluation gap. Current metrics (S-Corr, MetaJudge) measure alignment with reference judgments but cannot determine whether the PRM understood the error or reached the right label through spurious reasoning. Our formal error specifications provide deterministic ground truth for this question. (3) Training data integrity: The PRM training ecosystem is built on GSM8K/MATH-derived data. PRM800K labels 75K GSM8K/MATH solutions, OmegaPRM generates 1.5M annotations from similar distributions, FoVer-40K derives from GSM8K-level problems. If rationale quality at this foundational level is unreliable (and R-Align/MetaJudge show ~40-60% spurious correctness/inconsistency rates), the corruption propagates through the entire training pipeline. Improving faithfulness at the source is a leverage point, not a limitation.\n\nAcknowledged Limitations and Mitigations. (1) Scope: FoVer's formal verification is validated on GSM8K-level arithmetic and FOL logic. Extending to competition math faces fundamental barriers -- Z3 is undecidable for nonlinear integer arithmetic (confirmed by 'SMT and Functional Equation Solving over the Reals,' 2025), and FormalMATH shows only 16.46% LLM prover success on Lean4 problems. MATH-500 and GPQA-Diamond are explicitly positioned as stretch goals requiring future formalization extensions: specifically, Lean 4 integration (via Safe's autoformalization pipeline) for algebraic reasoning, or SymPy+Z3 (via MATH-VF's approach) for computational verification. We treat this scope limitation as a design choice rather than a weakness: foundational domains are where formal grounding provides deterministic guarantees and where the practical applications (safety-critical, diagnostics, training data) are most compelling. (2) Gaming vulnerability: Kim et al. (2604.19459) show two-stage formalization pipelines are vulnerable to premise mistranslation. Our Z3 formal equivalence check provides stronger detection than LLM-as-judge for axiom-fabrication-type errors (would catch GPT-5's 107 fabricated axioms in their study), but cannot fully guard against symmetric mistranslation at the NL-to-formal boundary. We mitigate via: (a) roundtrip verification from Amrollahi et al., which catches asymmetric errors; (b) NLI-based drift analysis as a secondary signal; (c) restricting to domains (FOL, arithmetic) where formalization ambiguity is lower than natural language. (3) FormalRewardBench shows even frontier LLMs achieve only 59.8% on formal proof evaluation, but our approach uses formal verification tools (Z3, Isabelle) as ground truth rather than LLMs as proof evaluators, sidestepping the generation-evaluation gap within Z3/Isabelle's decidable scope. (4) Cross-domain roundtrip uncertainty: Amrollahi et al.'s roundtrip equivalence rates were measured on statutory text, while our pipeline operates on math/logic formalization. These domains may differ in opposing ways: math/logic has lower linguistic ambiguity and more standardized notation (potentially yielding higher equivalence rates), but non-trivial mathematical steps involve implicit conventions and multi-step dependencies that may resist clean formalization (potentially yielding lower rates). Our Phase 1 pilot validation on 2K steps is specifically designed to calibrate this cross-domain transfer before committing to full-scale synthesis, and we report pilot equivalence rates alongside Amrollahi et al.'s statutory text rates to enable direct comparison. (5) Complementarity with non-formal approaches: 'Outcome Accuracy is Not Enough' (Qwen team, 2602.04649) achieves strong rationale quality improvements through soft semantic matching against human annotations without formal grounding. Our approach provides stronger guarantees (deterministic formal traceability) within a narrower scope; their approach provides broader coverage (any domain with annotations) with softer guarantees. Future work should explore combining formal grounding for in-scope domains with hybrid consistency training for broader coverage. (6) Relationship to concurrent data synthesis work: CVPDS (arXiv 2605.02395) provides an alternative approach to generating verified PRM training data through template-based error injection. While methodologically distinct from proof-artifact extraction, both approaches aim to improve PRM training data quality through formal/symbolic verification. Our approaches are complementary: CVPDS offers controllable error diversity but is constrained by predefined templates, while our method extracts artifacts from naturally occurring LLM errors but requires successful formal verification. Combining controlled error injection with proof-artifact rationale grounding is a promising future direction. (7) FormalFaithBench scope: The diagnostic benchmark is limited to domains where formal verification produces extractable artifacts (currently FOL and GSM8K-level arithmetic). However, the methodology extends naturally as formal verification tools expand to new domains (Lean 4 for algebra via Safe, SymPy+Z3 for computation via MATH-VF), and the benchmark design is explicitly modular to accommodate new artifact types.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "550-750 (solution generation for augmented data ~80h, rationale synthesis with Qwen3-32B ~120h, SFT on 14B model 4xA100 ~100h, evaluation including faithfulness transfer experiment ~100h, downstream policy experiment ~60h, FormalFaithBench construction and evaluation ~40h, ablations ~90h)",
      "engineering_time": "Z3 counterexample parsing: ~1-2 weeks; Isabelle proof state extraction: ~2-3 weeks; augmented data generation: ~1 week; roundtrip filter + diagnosis repair: ~1 week; FormalFaithBench metric implementation: ~1 week; downstream RFT pipeline: ~0.5 weeks; integration/testing: ~1 week. Total: 7-9 weeks engineering.",
      "timeline": "16-20 weeks",
      "estimated_gpu_cost": "$1100-1800 (A100 80GB at ~$2.00/hr on Vast.ai/Spheron)"
    },
    "human_in_loop": {
      "gpu_hours": "550-750 (irreducible training/inference costs unchanged)",
      "engineering_time": "4-6 weeks (Claude accelerates Z3 parsing code, Isabelle wrapper modifications, rationale template design, augmented data pipeline, FormalFaithBench metrics, evaluation harness, RFT pipeline)",
      "timeline": "12-16 weeks",
      "claude_api_cost": "$600-900 (Sonnet 4.6 for pipeline code generation and data analysis, ~120-220M tokens)",
      "estimated_gpu_cost": "$1100-1800"
    },
    "auto_research": {
      "gpu_hours": "600-800 (slightly higher from automated ablation sweeps, augmented data generation, faithfulness transfer experiment, downstream policy experiment, FormalFaithBench construction, and pilot experiments)",
      "engineering_time": "2-3 weeks (Claude handles most Z3/Isabelle parsing engineering)",
      "timeline": "9-12 weeks",
      "claude_api_cost": "$1700-2800 (Sonnet 4.6 for end-to-end pipeline orchestration, rationale quality filtering, FormalFaithBench metric design, iterative ablation design, ~450-750M tokens)",
      "estimated_gpu_cost": "$1200-1900",
      "speed_bottleneck": "Isabelle proof state extraction engineering (~2-3 weeks irreducible due to Isabelle API complexity, though StepProof's engineering precedent reduces unknowns); Z3 counterexample extraction is faster (~1-2 weeks). Formal verification throughput (~2-10s per Z3 step, 15-60s per Isabelle step) is parallelizable across CPU cores. Augmented data generation adds ~1 week for solution generation and verification. Downstream RFT experiment is fast (~50-80h GPU) but depends on Phase 3 model completion. FormalFaithBench construction parallelizes with Phase 3 training."
    }
  },
  "target_venues": [
    "ICLR 2027 (projected abstracts Sep 19, full papers Sep 24, 2026 -- 17 weeks; projected from ICLR 2026 pattern, official CFP not yet published as of May 2026; comfortable for human_in_loop and auto_research timelines)",
    "ARR October 2026 cycle -> commitment to NAACL 2027 or ACL 2027 (comfortable backup NLP venue)",
    "AAAI 2027 (abstracts Jul 21, full papers Jul 28, 2026 -- 8 weeks from today, feasible only with auto_research timeline and Z3-only scoped initial submission)"
  ],
  "level": "top-tier",
  "key_references": [
    "Process Reward Models That Think (arXiv 2025, ThinkPRM)",
    "GenPRM: Scaling Test-Time Compute of Process Reward Models via Generative Reasoning (AAAI 2026)",
    "R-PRM: Reasoning-Driven Process Reward Modeling (EMNLP 2025, She et al.)",
    "Efficient PRM Training Data Synthesis via Formal Verification (ACL Findings 2026, FoVer)",
    "Controllable and Verifiable Process Data Synthesis for Process Reward Models (arXiv 2605.02395, May 2026, Chi & Wang)",
    "StepProof: Step-by-step verification of natural language mathematical proofs (arXiv 2506.10558, June 2025, Hu et al.)",
    "Learning to Disprove: Formal Counterexample Generation with Large Language Models (arXiv 2603.19514, March 2026, Li et al.)",
    "FaithCoT-Bench: Benchmarking Instance-Level Faithfulness of Chain-of-Thought Reasoning (ICLR 2026)",
    "RM-R1: Reward Modeling as Reasoning (ICLR 2026)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv 2604.25031, April 2026, Amrollahi et al.)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv 2604.19459, VerifAI-2 @ ICLR 2026, Kim et al.)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv 2605.10141, May 2026)",
    "Beyond Outcome Verification: Verifiable Process Reward Models (arXiv 2601.17223, Jan 2026, VPRMs)",
    "Safe: Enhancing Mathematical Reasoning via Retrospective Step-aware Formal Verification (ACL 2025)",
    "R-Align: Enhancing Generative Reward Models through Rationale-Centric Meta-Judging (arXiv Feb 2026)",
    "Think-RM: Enabling Long-Horizon Reasoning in Generative Reward Models (NeurIPS 2025)",
    "Proof-RM: A Scalable and Generalizable Reward Model for Math Proof (arXiv Feb 2026)",
    "HERMES: Towards Efficient and Verifiable Mathematical Reasoning in LLMs (ICML 2026)",
    "Learning to Generate Formally Verifiable Step-by-Step Logic Reasoning via Structured Formal Intermediaries (arXiv 2026, PRoSFI)",
    "Outcome Accuracy is Not Enough: Aligning the Reasoning Process of Reward Models (arXiv 2602.04649, Feb 2026, Qwen team)",
    "Step-Wise Formal Verification for LLM-Based Mathematical Problem Solving (arXiv 2025, MATH-VF)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of LLMs (arXiv 2025)",
    "Improve Mathematical Reasoning in Language Models by Automated Process Supervision (arXiv 2024, OmegaPRM)",
    "GroundedPRM: Tree-Guided and Fidelity-Aware Process Reward Modeling (NeurIPS 2025 Workshop)"
  ],
  "description": "We propose Proof-Grounded Generative PRMs, the first process reward models whose verification rationales are traceable to structured formal proof artifacts, and FormalFaithBench, the first automated benchmark for evaluating PRM rationale quality against formal ground truth. Current generative PRMs (ThinkPRM, GenPRM, R-PRM, RM-R1) produce chain-of-thought verification rationales trained on synthetic data of unknown faithfulness -- R-Align shows GenRM decisions exhibit substantial spurious correctness (right label, wrong reasoning), and frontier GenRMs achieve only approximately 40% rationale consistency with human judgments. R-PRM (EMNLP 2025) demonstrates that reasoning-driven evaluation substantially improves PRM accuracy (70.4 F1 on ProcessBench, +13.9 over Qwen2.5-Math-7B-PRM800K at 56.5 F1), but its multi-dimensional analyses are trained on LLM-bootstrapped data and rationale faithfulness is not evaluated. More fundamentally, the field lacks a scalable ground-truth methodology for evaluating WHETHER a PRM's rationale correctly identifies the actual mathematical error: human evaluation doesn't scale, LLM-as-judge achieves only 65-77 F1 (FaithCoT-Bench), and existing automated metrics rely on reference annotations unavailable for most domains. Separately, FoVer (ACL 2026 Findings) demonstrated that formal verification tools (Z3, Isabelle) can produce accurate step-level error labels transferring across 12 benchmarks, but generates only binary labels and explicitly excludes reasoning-based PRMs. A concurrent approach (CVPDS, arXiv 2605.02395) synthesizes PRM data through template-based symbolic error injection across 11 error types with 20K instances, but targets accuracy through controlled error diversity rather than rationale faithfulness through proof-artifact grounding. A non-formal approach ('Outcome Accuracy is Not Enough,' Qwen team) improves rationale quality through hybrid consistency-outcome training via soft semantic matching against human annotations, achieving RM-Bench 87.1% (+5% over baselines) -- but relies on human annotation availability and provides softer guarantees than formal artifact tracing. We make three contributions bridging the formal gap. First, we extend FoVer's verification pipeline to extract structured proof artifacts -- Z3 counterexamples from SAT results and Isabelle proof state information at failure points -- going beyond binary labels to structured error specifications. StepProof (Hu et al., 2025) provides engineering precedent for fine-grained Isabelle proof state manipulation on GSM8K, and Learning to Disprove (Li et al., 2026) demonstrates at scale (575K instances) that formal counterexamples serve as effective training signals. Second, we synthesize verification rationales grounded in these artifacts using Qwen3-32B with roundtrip consistency filtering adapted from Amrollahi et al.'s (2604.25031) validated mechanism (45-66% baseline equivalence, 78-86% with standard diagnosis-guided repair, up to 91-95% with cross-model diagnosis; we implement standard same-model repair and conservatively estimate 70-85% post-repair rates on math/logic given cross-domain uncertainty), then fine-tune Qwen3-14B as a generative PRM on these rationales. Starting from FoVer-40K's 20K error steps, we estimate ~9-12K proof-grounded rationales (Scenario A); augmenting FoVer's pipeline yields ~14-17K (Scenario B). Both scenarios exceed ThinkPRM's training data by an order of magnitude with richer per-example signal via formal artifact tracing. Third, we introduce FormalFaithBench: a diagnostic benchmark using ~2-3K held-out proof artifacts as ground-truth error specifications, measuring whether any PRM's rationale correctly identifies the specific mathematical error via three automated metrics (Error Identification Rate, Counterexample Alignment, Proof State Match), validated against 200 human judgments. This fills a critical evaluation gap analogous to ProcessBench for labels: FormalFaithBench evaluates step-level explanation accuracy with formal ground truth. We scope primary evaluation to FoVer-validated domains -- GSM8K-level arithmetic and FOL logic -- targeting R-PRM-7B-DPO F1 (70.4), GenPRM-7B F1, and ThinkPRM-14B best-of-N as baselines. We foreground three inherent value propositions making this work impactful on foundational domains regardless of transfer: (1) Safety-critical deployment: GSM8K-level arithmetic is the domain for financial compliance, engineering safety margins, and pharmaceutical dosing -- applications requiring auditable error explanations, not just error detection. (2) PRM diagnostics: FormalFaithBench provides the first automated methodology for measuring whether ANY PRM's rationale correctly identifies the actual mathematical error, enabling systematic debugging of PRM failure modes. (3) Training data integrity: GSM8K is the foundation of PRM training pipelines (PRM800K, FoVer, OmegaPRM); improving rationale faithfulness at this level prevents corrupted supervision from propagating. We additionally include three dedicated experiments: (A) faithfulness transfer measuring S-Corr on ProcessBench-MATH/Olympiad for our model versus baselines including R-PRM-7B-DPO and a binary-label ablation; (B) downstream policy via rejection sampling fine-tuning of Qwen2.5-Math-1.5B on 500 GSM8K + 500 MATH problems; (C) FormalFaithBench evaluation of five PRMs with metric reliability validation. We acknowledge scope limitations (Z3 undecidability for nonlinear arithmetic; FormalMATH's 16.46% prover success), treat them as a design choice favoring deterministic guarantees on foundational domains, and position the methodology as extensible as formal verification tools expand.",
  "project_name": "proof_grounded_genprm",
  "source": "web_research",
  "reviewer_response": {
    "issue_1_faithful_autoformalization_numbers": "ADDRESSED (MODERATE, round 4).",
    "issue_2_hybrid_training_positioning": "ADDRESSED (MODERATE, round 4).",
    "issue_3_faithfulness_transfer_experiment": "ADDRESSED (MINOR, round 4).",
    "issue_4_crossdomain_roundtrip_uncertainty": "ADDRESSED (MINOR, round 4).",
    "issue_5_rprm_baseline": "ADDRESSED (MODERATE, round 5).",
    "issue_6_cvpds_concurrent_work": "ADDRESSED (MODERATE, round 5).",
    "issue_7_downstream_rlhf_experiment": "ADDRESSED (MINOR, round 5).",
    "issue_8_iclr2027_deadline_tentative": "ADDRESSED (MINOR, round 5).",
    "issue_9_ralign_claims_clarification": "ADDRESSED (MINOR, round 5).",
    "issue_10_rprm_baseline_f1_correction": "ADDRESSED (MINOR, round 7). Corrected Qwen2.5-Math-7B-PRM800K baseline from 58.5 F1 to 56.5 F1 throughout. The improvement claim (+13.9 F1) and R-PRM-7B-DPO score (70.4 F1) remain correct: 70.4 - 56.5 = 13.9.",
    "issue_11_stepproof_acknowledgment": "ADDRESSED (MINOR, round 7). Added StepProof (arXiv 2506.10558, Hu et al., June 2025) to landscape: step-by-step Isabelle verification on GSM8K, incremental proof state management, 27.9% proof pass rate. Referenced as engineering precedent in Phase 1(b). Added to key references and gap analysis.",
    "issue_12_learning_to_disprove_acknowledgment": "ADDRESSED (MINOR, round 7). Added Learning to Disprove (arXiv 2603.19514, Li et al., March 2026) to landscape: 575K counterexamples from 321K seed theorems via symbolic mutation in Lean 4. Distinguished from our approach (they train generators, we ground verifier rationales). Added to key references, gap analysis, and data sufficiency argument.",
    "issue_13_impact_ceiling_reframing": "ADDRESSED (STRUCTURAL, round 7). MAJOR REFRAMING: (1) Elevated FormalFaithBench to a core contribution -- first automated benchmark for PRM rationale quality with formal ground truth, measuring EIR/CA/PSM metrics, valuable regardless of our trained PRM's accuracy. (2) Foregrounded safety-critical deployment argument: GSM8K-level arithmetic IS the deployment domain for auditable applications. (3) Made training data integrity argument central: improving faithfulness at GSM8K level is a leverage point, not a limitation. (4) Reframed core_problem to identify both training gap and evaluation gap. (5) Repositioned scope as design choice, not weakness. (6) Demoted transfer to secondary hypothesis rather than core claim."
  }
}
```

---

## Summary of Changes (Round 7 — Major Revision)

### What changed and why:

**1. R-PRM baseline correction** (MINOR → fixed): Changed `58.5 F1` → `56.5 F1` for Qwen2.5-Math-7B-PRM800K throughout. The +13.9 improvement claim (70.4 - 56.5) was already correct.

**2. StepProof acknowledged** (MINOR → added): Added to landscape with engineering details (incremental proof state management, accumulative context, selective backtracking, 27.9% pass rate on GSM8K). Referenced in Phase 1(b) as engineering precedent that reduces Isabelle integration risk.

**3. Learning to Disprove acknowledged** (MINOR → added): Added with full methodology (symbolic mutation, 575K counterexamples from 321K seed theorems, multi-reward expert iteration). Distinguished from our work (they train generators to produce counterexamples; we extract counterexamples from tools to ground verifier rationales). Referenced in data sufficiency argument.

**4. MAJOR REFRAMING to address impact ceiling** (STRUCTURAL):

The fundamental change: instead of the primary value proposition being "transfer from easy to hard domains" (with easy-domain scope as a limitation), the proposal now **foregrounds three inherent-value propositions** that make formal grounding on foundational domains valuable regardless of whether transfer works:

- **Safety-critical deployment**: GSM8K-level arithmetic *is the deployment domain* for financial compliance, engineering safety margins, and pharmaceutical dosing. Auditable error explanations are legally required in these applications — this isn't "easy domain" work, it's the actual use case.

- **FormalFaithBench (new core contribution)**: Introduced as Phase 4(C) — the first automated benchmark for PRM rationale quality with formal ground truth. Measures Error Identification Rate, Counterexample Alignment, and Proof State Match, validated against 200 human judgments. This is valuable even if our trained PRM shows marginal accuracy improvements, because it gives the community a tool for evaluating ANY PRM's explanation quality. The analogy: just as ProcessBench measures step-level label accuracy, FormalFaithBench measures step-level explanation accuracy.

- **Training data integrity**: Made the "GSM8K as foundation" argument more central — PRM800K, OmegaPRM, and FoVer all build on GSM8K-level data. Improving faithfulness at this level is a high-leverage intervention, not a limitation.

The core_problem was restructured to identify both a **training gap** (rationales lack formal grounding) and an **evaluation gap** (no scalable ground-truth for measuring rationale quality). Transfer to harder domains is now positioned as a secondary hypothesis to test, not the core claim.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb7fad20-cdab-4e81-8ef8-82728f0096e3",
  "isSidechain": false,
  "requestId": "req_011CbTiXw84hLYt1sMyJRfTK",
  "type": "assistant",
  "uuid": "111c4738-56d4-4a35-b25a-3ce0a00485d5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KrxnskFYjEEMCb9fh1YL53",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13764,
      "cache_read_input_tokens": 48017,
      "output_tokens": 13952,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13764,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13952,
          "cache_read_input_tokens": 48017,
          "cache_creation_input_tokens": 13764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13764
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

_source line 30_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",   \"core_pr…",
  "leafUuid": "111c4738-56d4-4a35-b25a-3ce0a00485d5",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 31_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise formal PRM rationale proposal with R-PRM baseline correction",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"title\": \"Formally Grounded Faithful Rationales for Generative PRMs\",   \"core_pr…",
  "leafUuid": "111c4738-56d4-4a35-b25a-3ce0a00485d5",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise formal PRM rationale proposal with R-PRM baseline correction",
  "sessionId": "8fc053cf-e20a-48d4-a0fc-7b2966f0b112"
}
```

---
