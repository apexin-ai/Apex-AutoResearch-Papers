# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-2/19bf699c-697e-4469-8fdb-f6b0b20226f6.jsonl`
- **Structured JSON:** [`4d4c6108a0da6d149e15.json`](../../sessions/4d/4d4c6108a0da6d149e15.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:59:17.967Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:59:17.967Z",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\",\n  \"project_name\": \"answer_fidelity_free_trace\",\n  \"source\": \"web_research\",\n  \"core_problem\": \"GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally tend to generate answers in the target language even when traces are mixed—a training-induced tendency (arXiv 2505.14815, §4.2 attributes this to 'supervision or reward signals focused on the final answer') that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.\",\n  \"opportunity\": \"'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—§4.2, Finding 2 of that paper states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to models being 'trained with supervision or reward signals focused on the final answer'—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Tables 8–9), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\",\n  \"landscape\": \"M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. arXiv 2505.15257 ('When Less Language is More', May 2025) achieves language-reasoning disentanglement at inference time via SVD-based activation ablation—projecting language-specific subspaces out of mid-layer hidden states during the forward pass—with no training required, reporting results comparable to RL (PPO) on MGSM. Our method differs categorically: we achieve answer-surface fidelity via a GRPO reward during standard RL fine-tuning, with no inference-time modification to activations or architecture. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows (§4.2, Finding 2) that 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' attributing this to 'supervision or reward signals focused on the final answer'; it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\\n\\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (§5.2, Figure 6, Tables 8–9) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\\n\\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (§5.2, Figure 6, Tables 8–9) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\\n\\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.\",\n  \"approach\": \"We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\\n\\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\\n\\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (§4.2, Finding 2) states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language'; the §4.2 analysis explicitly notes that 'the final answers remain more aligned with the input language,' attributing this to 'supervision or reward signals focused on the final answer'—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\\n\\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\\n\\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\\n\\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\\n\\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\\n\\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per §5.2, Figure 6, and Tables 8–9), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\\n\\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\\n\\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\\n\\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (§4.2, Finding 2) that 'supervision or reward signals focused on the final answer' produce the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\\n\\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~105-175 H100-hours (4 ablation conditions × 2 seeds × ~12-15 H100-hours/run on Qwen3-7B with LoRA rank-16 on 4×H100 = ~96-120 H100-hours training; secondary Swahili experiment ~15 H100-hours; inference evals including MMLU-ProX 0-shot across 7 languages, XQuAD across 4 languages, pretrained-base cross-task eval, XCOPA, XStoryCloze ~20 H100-hours; sequential debugging adds ~20 H100-hours overhead; upper-end arithmetic: 120 + 15 + 20 + 20 = 175 H100-hours)\",\n      \"gpu_utilization\": \"Low (~40-50% effective); GPU idles waiting for researcher to iterate on SFVG reward code and analyze SFVG activation trajectories and correct-language rate logs per language\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$315-525 at $3.00/H100-hr\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~147-182 H100-hours (agent queues ablation conditions in parallel; XQuAD inference ~2 H100-hours added to transfer eval suite; human approves experimental design at 4 key checkpoints: after first non-Latin-script run to verify SFVG Gate 2 activation, after vanilla GRPO baseline, after primary ablation completion, before secondary Swahili experiment)\",\n      \"gpu_utilization\": \"Moderate (~65-75% effective)\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150-300 (~1,500-3,000 agent turns for experiment design, SFVG log parsing, correct-language rate monitoring, LID-activation trajectory monitoring, MMLU-ProX and XQuAD inference and result analysis)\",\n      \"estimated_gpu_cost\": \"~$441-546\",\n      \"risk_note\": \"Key risk: SFVG Gate 2 (frame-presence check) must be verified to activate before Gate 3 (LID scoring). Human checkpoint after first non-Latin-script run is essential. SFVG gate activation rate and correct-language rate per language per step are the primary diagnostic signals, logged in TRL GRPOTrainer reward callback. Secondary risk: if model learns bare-numeral answers that satisfy Gate 1 but not Gate 2, the LID reward is perpetually inactive—detectable from flat Gate 2 activation curve. Correct-language rate log provides additional signal: if it is low for Latin-script languages under the universal prompt, the language-explicit ablation is promoted to primary.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~172-215 H100-hours. Grid is fixed at LoRA rank-16 throughout (rank sensitivity is scoped to manual-mode follow-up only; the original claim of sweeping rank ∈ {8,16,32} was removed as it would require 24-36 training runs totalling 288-540 H100-hours, far exceeding the 200 H100-hour budget). The constrained auto-mode grid is: (i) λ sweep {0.1, 0.2, 0.3, 0.5} for the answer-only SFVG condition × 1 seed (exploratory), = 4 runs × ~13 H100-hours = ~52 H100-hours; (ii) best λ re-run × 2 seeds for final reporting = 2 runs × ~13 H100-hours = ~26 H100-hours; (iii) 3 fixed-hyperparameter baselines (vanilla GRPO, whole-trace LC, PB-RLSVR) × 2 seeds = 6 runs × ~13 H100-hours = ~78 H100-hours; (iv) secondary Swahili experiment = ~15 H100-hours; (v) inference evals including pretrained-base cross-task checkpoint on XCOPA/XStoryCloze/MMLU-ProX/XQuAD = ~20 H100-hours. Total: ~191 H100-hours, fitting within the 200 H100-hour budget. The supplementary language-explicit prompt ablation (Gate 2 activation rate and correct-language rate comparison) is run as a short inference-only evaluation on the converged answer-only SFVG model (~3 H100-hours) and is included in the inference budget.\",\n      \"gpu_utilization\": \"Near-zero idle (~85-90% effective)\",\n      \"timeline\": \"5-10 days given 8+ H100s simultaneously\",\n      \"team\": \"0 (initial setup: ~2-3 hours to configure LoRA GRPOTrainer reward functions, SFVG gate logic with script-adaptive thresholds and correct-language rate logging, and evaluation harness including MMLU-ProX and XQuAD 0-shot pipelines)\",\n      \"claude_api_cost\": \"$300-600 (~3,000-6,000 agent turns for iterative design, SFVG log analysis, correct-language rate trajectory analysis, reward-hacking detection, cross-task transfer analysis, write-up drafting)\",\n      \"estimated_gpu_cost\": \"~$516-645\",\n      \"speed_bottleneck\": \"H100 cluster availability; fastText LID inference latency (mitigated by applying LID only to non-numeric answer content rather than the full trace, which is substantially shorter)\",\n      \"risk_note\": \"Primary risk: SFVG Gate 2 (frame-presence check) flat activation means model is producing bare numerals—detectable from Gate 2 activation curve, triggerable by adjusting system-prompt phrasing or adding format reward weight. Must be caught before training runs complete. Secondary risk: script-adaptive thresholds (8/5/3 chars for Latin/Thai/CJK) may require tuning; initial runs should log per-language gate failure breakdown and correct-language rate. Auto mode must trigger alert if Gate 2 activation drops below 50% for any language after step 200 (indicates model is not learning sentence frames), or if correct-language rate drops below 70% for any Latin-script language under the universal prompt (indicates cross-Latin-script confusion degrading LID reward signal). If the correct-language rate is systematically low for Latin-script languages under the universal prompt, the language-explicit prompt variant is promoted from supplementary to primary.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR submission deadline May 25, 2026)\"\n  ],\n  \"key_references\": [\n    \"When Verifiable Rewards Switch the Language: Cross-lingual Collapse in Chain-of-Thought (arXiv 2506.05850, Jun 2025)\",\n    \"Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes (arXiv 2505.14815, May 2025)\",\n    \"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners (arXiv 2505.15257, May 2025)\",\n    \"Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning / M-Thinker (arXiv 2510.07300, Oct 2025)\",\n    \"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, Oct 2025)\",\n    \"Long Chain-of-Thought Reasoning Across Languages (arXiv 2508.14828, Aug 2025)\",\n    \"Making Qwen3 Think in Korean with Reinforcement Learning (arXiv 2508.10355, Aug 2025)\",\n    \"Aligning Multilingual Reasoning with Verifiable Semantics from a High-Resource Expert Model / PB-RLSVR (arXiv 2509.25543, Sep 2025)\",\n    \"Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought (arXiv 2510.04230, Oct 2025)\",\n    \"ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection (arXiv 2602.21887, Feb 2026)\",\n    \"Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training / TRIT (arXiv 2602.05940, Feb 2026)\",\n    \"Language as a Latent Variable for Reasoning Optimization / polyGRPO (arXiv 2604.21593, Apr 2026)\",\n    \"TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models (arXiv 2604.26553, Apr 2026)\",\n    \"What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features (arXiv 2604.04720, Apr 2026)\",\n    \"ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance (arXiv 2604.12378, Apr 2026)\",\n    \"MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation (arXiv 2503.10497, EMNLP 2025 Main)\",\n    \"XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (arXiv 2305.11938, EMNLP 2023 Findings)\"\n  ],\n  \"description\": \"We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers: §4.2, Finding 2 states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to 'supervision or reward signals focused on the final answer'; and (b) Latin-script (English) reasoning yields optimal accuracy (§5.2, Figure 6, Tables 8–9: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (§4.2, Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\\n\\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\\n\\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\\n\\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal], and arXiv 2505.15257 [training-free SVD activation ablation at inference time]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features or hidden-state geometry without proposing a GRPO reward that decouples trace from answer constraint. Target: EMNLP 2026 Findings.\"\n}\n\n## Reviewer feedback (round 8)\nIssues: [\"FACTUAL CITATION ERROR PERSISTING (Round 7 correction was wrong) — Independent verification of arXiv 2505.14815 confirms that Table 10 documents the performance comparison across script control strategies for non-Latin/Han-script languages (Arabic, Hindi, Japanese), where the 44–115% accuracy gains for Latin-script-constrained reasoning appear. Tables 8 and 9 contain the language inventory (Table 8: 15 languages with scripts) and script composition across difficulty levels (Table 9: Hindi analysis), NOT accuracy gains. The Round 7 reviewer erroneously stated Table 10 was K&K baseline data and instructed the generator to change to 'Tables 8–9.' The generator complied, replacing a correct citation with an incorrect one. The Round 8 proposal now cites 'gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Tables 8–9' in THREE locations (opportunity section, landscape section, description section). ALL THREE must be corrected back to '§5.2, Figure 6, and Table 10.'\"]\nFeedback: One mechanical fix required before this paper is Findings-ready. In the opportunity section, landscape section, and description section, replace 'Tables 8–9' with 'Table 10' in all references to the 44–115% accuracy gains from Latin-script-constrained reasoning in arXiv 2505.14815. Specifically: 'gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Tables 8–9' → 'gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Table 10' (three locations). The Round 7 reviewer's claim that Table 10 contained K&K baseline performance was incorrect; Table 10 is the accuracy comparison table across script control strategies, Tables 8–9 contain language metadata. All other issues from Rounds 1–7 are resolved: §4.2 Finding 2 verified verbatim, SVD characterization in 2505.15257 confirmed correct, ReasonXL differentiated, Ki et al. integrated, polyGRPO comparison present, MMLU-ProX and XQuAD included, pretrained-base checkpoint added, correct-language rate metric specified, compute within 200-hour budget, XTREME-UP exclusion argued. After correcting the table numbers, submit.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:59:17.970Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:59:17.970Z",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

## Round 1

17 recorded events

### User

_source line 3 · 2026-05-10T08:59:17.991Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO",
  "project_name": "answer_fidelity_free_trace",
  "source": "web_research",
  "core_problem": "GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally tend to generate answers in the target language even when traces are mixed—a training-induced tendency (arXiv 2505.14815, §4.2 attributes this to 'supervision or reward signals focused on the final answer') that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.",
  "opportunity": "'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—§4.2, Finding 2 of that paper states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to models being 'trained with supervision or reward signals focused on the final answer'—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Tables 8–9), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.",
  "landscape": "M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. arXiv 2505.15257 ('When Less Language is More', May 2025) achieves language-reasoning disentanglement at inference time via SVD-based activation ablation—projecting language-specific subspaces out of mid-layer hidden states during the forward pass—with no training required, reporting results comparable to RL (PPO) on MGSM. Our method differs categorically: we achieve answer-surface fidelity via a GRPO reward during standard RL fine-tuning, with no inference-time modification to activations or architecture. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows (§4.2, Finding 2) that 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' attributing this to 'supervision or reward signals focused on the final answer'; it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\n\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (§5.2, Figure 6, Tables 8–9) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\n\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (§5.2, Figure 6, Tables 8–9) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\n\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.",
  "approach": "We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\n\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\n\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (§4.2, Finding 2) states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language'; the §4.2 analysis explicitly notes that 'the final answers remain more aligned with the input language,' attributing this to 'supervision or reward signals focused on the final answer'—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\n\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\n\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\n\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\n\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\n\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per §5.2, Figure 6, and Tables 8–9), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\n\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\n\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\n\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (§4.2, Finding 2) that 'supervision or reward signals focused on the final answer' produce the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\n\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~105-175 H100-hours (4 ablation conditions × 2 seeds × ~12-15 H100-hours/run on Qwen3-7B with LoRA rank-16 on 4×H100 = ~96-120 H100-hours training; secondary Swahili experiment ~15 H100-hours; inference evals including MMLU-ProX 0-shot across 7 languages, XQuAD across 4 languages, pretrained-base cross-task eval, XCOPA, XStoryCloze ~20 H100-hours; sequential debugging adds ~20 H100-hours overhead; upper-end arithmetic: 120 + 15 + 20 + 20 = 175 H100-hours)",
      "gpu_utilization": "Low (~40-50% effective); GPU idles waiting for researcher to iterate on SFVG reward code and analyze SFVG activation trajectories and correct-language rate logs per language",
      "timeline": "6-10 weeks",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$315-525 at $3.00/H100-hr"
    },
    "human_in_loop": {
      "gpu_hours": "~147-182 H100-hours (agent queues ablation conditions in parallel; XQuAD inference ~2 H100-hours added to transfer eval suite; human approves experimental design at 4 key checkpoints: after first non-Latin-script run to verify SFVG Gate 2 activation, after vanilla GRPO baseline, after primary ablation completion, before secondary Swahili experiment)",
      "gpu_utilization": "Moderate (~65-75% effective)",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150-300 (~1,500-3,000 agent turns for experiment design, SFVG log parsing, correct-language rate monitoring, LID-activation trajectory monitoring, MMLU-ProX and XQuAD inference and result analysis)",
      "estimated_gpu_cost": "~$441-546",
      "risk_note": "Key risk: SFVG Gate 2 (frame-presence check) must be verified to activate before Gate 3 (LID scoring). Human checkpoint after first non-Latin-script run is essential. SFVG gate activation rate and correct-language rate per language per step are the primary diagnostic signals, logged in TRL GRPOTrainer reward callback. Secondary risk: if model learns bare-numeral answers that satisfy Gate 1 but not Gate 2, the LID reward is perpetually inactive—detectable from flat Gate 2 activation curve. Correct-language rate log provides additional signal: if it is low for Latin-script languages under the universal prompt, the language-explicit ablation is promoted to primary."
    },
    "auto_research": {
      "gpu_hours": "~172-215 H100-hours. Grid is fixed at LoRA rank-16 throughout (rank sensitivity is scoped to manual-mode follow-up only; the original claim of sweeping rank ∈ {8,16,32} was removed as it would require 24-36 training runs totalling 288-540 H100-hours, far exceeding the 200 H100-hour budget). The constrained auto-mode grid is: (i) λ sweep {0.1, 0.2, 0.3, 0.5} for the answer-only SFVG condition × 1 seed (exploratory), = 4 runs × ~13 H100-hours = ~52 H100-hours; (ii) best λ re-run × 2 seeds for final reporting = 2 runs × ~13 H100-hours = ~26 H100-hours; (iii) 3 fixed-hyperparameter baselines (vanilla GRPO, whole-trace LC, PB-RLSVR) × 2 seeds = 6 runs × ~13 H100-hours = ~78 H100-hours; (iv) secondary Swahili experiment = ~15 H100-hours; (v) inference evals including pretrained-base cross-task checkpoint on XCOPA/XStoryCloze/MMLU-ProX/XQuAD = ~20 H100-hours. Total: ~191 H100-hours, fitting within the 200 H100-hour budget. The supplementary language-explicit prompt ablation (Gate 2 activation rate and correct-language rate comparison) is run as a short inference-only evaluation on the converged answer-only SFVG model (~3 H100-hours) and is included in the inference budget.",
      "gpu_utilization": "Near-zero idle (~85-90% effective)",
      "timeline": "5-10 days given 8+ H100s simultaneously",
      "team": "0 (initial setup: ~2-3 hours to configure LoRA GRPOTrainer reward functions, SFVG gate logic with script-adaptive thresholds and correct-language rate logging, and evaluation harness including MMLU-ProX and XQuAD 0-shot pipelines)",
      "claude_api_cost": "$300-600 (~3,000-6,000 agent turns for iterative design, SFVG log analysis, correct-language rate trajectory analysis, reward-hacking detection, cross-task transfer analysis, write-up drafting)",
      "estimated_gpu_cost": "~$516-645",
      "speed_bottleneck": "H100 cluster availability; fastText LID inference latency (mitigated by applying LID only to non-numeric answer content rather than the full trace, which is substantially shorter)",
      "risk_note": "Primary risk: SFVG Gate 2 (frame-presence check) flat activation means model is producing bare numerals—detectable from Gate 2 activation curve, triggerable by adjusting system-prompt phrasing or adding format reward weight. Must be caught before training runs complete. Secondary risk: script-adaptive thresholds (8/5/3 chars for Latin/Thai/CJK) may require tuning; initial runs should log per-language gate failure breakdown and correct-language rate. Auto mode must trigger alert if Gate 2 activation drops below 50% for any language after step 200 (indicates model is not learning sentence frames), or if correct-language rate drops below 70% for any Latin-script language under the universal prompt (indicates cross-Latin-script confusion degrading LID reward signal). If the correct-language rate is systematically low for Latin-script languages under the universal prompt, the language-explicit prompt variant is promoted from supplementary to primary."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR submission deadline May 25, 2026)"
  ],
  "key_references": [
    "When Verifiable Rewards Switch the Language: Cross-lingual Collapse in Chain-of-Thought (arXiv 2506.05850, Jun 2025)",
    "Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes (arXiv 2505.14815, May 2025)",
    "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners (arXiv 2505.15257, May 2025)",
    "Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning / M-Thinker (arXiv 2510.07300, Oct 2025)",
    "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, Oct 2025)",
    "Long Chain-of-Thought Reasoning Across Languages (arXiv 2508.14828, Aug 2025)",
    "Making Qwen3 Think in Korean with Reinforcement Learning (arXiv 2508.10355, Aug 2025)",
    "Aligning Multilingual Reasoning with Verifiable Semantics from a High-Resource Expert Model / PB-RLSVR (arXiv 2509.25543, Sep 2025)",
    "Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought (arXiv 2510.04230, Oct 2025)",
    "ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection (arXiv 2602.21887, Feb 2026)",
    "Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training / TRIT (arXiv 2602.05940, Feb 2026)",
    "Language as a Latent Variable for Reasoning Optimization / polyGRPO (arXiv 2604.21593, Apr 2026)",
    "TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models (arXiv 2604.26553, Apr 2026)",
    "What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features (arXiv 2604.04720, Apr 2026)",
    "ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance (arXiv 2604.12378, Apr 2026)",
    "MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation (arXiv 2503.10497, EMNLP 2025 Main)",
    "XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (arXiv 2305.11938, EMNLP 2023 Findings)"
  ],
  "description": "We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers: §4.2, Finding 2 states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to 'supervision or reward signals focused on the final answer'; and (b) Latin-script (English) reasoning yields optimal accuracy (§5.2, Figure 6, Tables 8–9: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (§4.2, Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\n\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\n\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\n\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal], and arXiv 2505.15257 [training-free SVD activation ablation at inference time]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features or hidden-state geometry without proposing a GRPO reward that decouples trace from answer constraint. Target: EMNLP 2026 Findings."
}

## Reviewer feedback (round 8)
Issues: ["FACTUAL CITATION ERROR PERSISTING (Round 7 correction was wrong) — Independent verification of arXiv 2505.14815 confirms that Table 10 documents the performance comparison across script control strategies for non-Latin/Han-script languages (Arabic, Hindi, Japanese), where the 44–115% accuracy gains for Latin-script-constrained reasoning appear. Tables 8 and 9 contain the language inventory (Table 8: 15 languages with scripts) and script composition across difficulty levels (Table 9: Hindi analysis), NOT accuracy gains. The Round 7 reviewer erroneously stated Table 10 was K&K baseline data and instructed the generator to change to 'Tables 8–9.' The generator complied, replacing a correct citation with an incorrect one. The Round 8 proposal now cites 'gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Tables 8–9' in THREE locations (opportunity section, landscape section, description section). ALL THREE must be corrected back to '§5.2, Figure 6, and Table 10.'"]
Feedback: One mechanical fix required before this paper is Findings-ready. In the opportunity section, landscape section, and description section, replace 'Tables 8–9' with 'Table 10' in all references to the 44–115% accuracy gains from Latin-script-constrained reasoning in arXiv 2505.14815. Specifically: 'gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Tables 8–9' → 'gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Table 10' (three locations). The Round 7 reviewer's claim that Table 10 contained K&K baseline performance was incorrect; Table 10 is the accuracy comparison table across script control strategies, Tables 8–9 contain language metadata. All other issues from Rounds 1–7 are resolved: §4.2 Finding 2 verified verbatim, SVD characterization in 2505.15257 confirmed correct, ReasonXL differentiated, Ki et al. integrated, polyGRPO comparison present, MMLU-ProX and XQuAD included, pretrained-base checkpoint added, correct-language rate metric specified, compute within 200-hour budget, XTREME-UP exclusion argued. After correcting the table numbers, submit.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.
- Address each issue specifically.

## 深度调研要求（每一轮修订都必须执行）

不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。
   - 搜索最新的相关论文（arXiv, conference proceedings）
   - 搜索 benchmark/leaderboard 确认当前 SOTA
   - 搜索可能遗漏的相关工作和 concurrent work

2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，
   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。

3. **深度思考**：在修订之前，先独立思考以下问题：
   - 这个 idea 的核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach 来解决同一个核心问题？
   - 修订后的 idea 相比上一版有什么本质性的改进？

4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，
   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。

## 针对 Review 意见的定向搜索

对 reviewer 指出的每个问题，执行以下搜索流程：

1. **如果 reviewer 说'已有类似工作'**：
   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读
   - 搜索该论文的 cited-by，找到后续跟进工作
   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot

2. **如果 reviewer 说'SOTA 过时'**：
   - 用 Papers With Code 查看当前排行榜
   - 搜索过去 6 个月的最新方法
   - 更新你的 landscape 和 baseline

3. **如果 reviewer 说'可行性有问题'**：
   - 搜索类似规模实验的实际成本和时间线
   - 搜索 GitHub 上是否有可复用的实现
   - 搜索相关数据集/模型的可获取性

4. **如果 reviewer 说'novelty 不足'**：
   - 对核心方法尽量做 3-5 种不同关键词组合的搜索
   - 搜索相邻领域是否有类似思路
   - 如果确实 novelty 不足，考虑 major revision 或 pivot

- Use WebSearch to find updated information if the reviewer flagged outdated claims.
- You have full freedom in how much to change:
  - Minor fix: if only specific details are wrong, correct them and keep everything else.
  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.
  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.
- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.
- In the output JSON, include a "change_type" field with one of: "minor", "major", or "pivot" to indicate the scope of your changes.
- Output the revised idea as a COMPLETE JSON object (same schema as original, plus "change_type").

## 停滞提醒
这个 idea 已经经过 8 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

请认真思考：
- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？
- 如果你认为问题出在 approach 而非 framing，可以做 major revision。
- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。
- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。

最终由你判断——做你认为最能提升 idea 质量的选择。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4909b2b0-2449-4849-9337-10c95a9de91e",
  "type": "user",
  "uuid": "efddd076-1b42-407a-843f-bf385906fd3b",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:59:17.989Z_

```json
{
  "parentUuid": "efddd076-1b42-407a-843f-bf385906fd3b",
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
  "uuid": "addaa8a5-a4ec-481b-919a-8a0001ba9a18",
  "timestamp": "2026-05-10T08:59:17.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:59:17.990Z_

```json
{
  "parentUuid": "addaa8a5-a4ec-481b-919a-8a0001ba9a18",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9fbae772-2cc7-4627-9837-31ef58bea18b",
  "timestamp": "2026-05-10T08:59:17.990Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "9fbae772-2cc7-4627-9837-31ef58bea18b",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Correct table citations in multilingual GRPO answer fidelity reward",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:00:18.133Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before making any decisions.

**Current State:**
- This is round 8 of revisions
- The reviewer feedback is very specific and mechanical: fix a citation error where "Tables 8–9" should be "Table 10" in three specific locations
- The reviewer says "All other issues from Rounds 1–7 are resolved" and instructs to "submit" after this fix

**The Stagnation Warning:**
The idea has been through 8 rounds with no significant improvement in scores (3.5 average for last 3 rounds). However, the reviewer in Round 8 is saying the paper is ready to submit after one mechanical fix. This is actually positive progress - the reviewer is satisfied with everything except the citation error.
 
So I need to verify whether the citation should actually reference Table 10 instead of Tables 8-9, make that correction across all three locations, and then decide whether to proceed with the fix or reconsider the overall direction. The reviewer is being clear that this is the final hurdle before submission, so I should verify the citation is correct before moving forward. The reviewer has independently verified the arXiv paper and confirmed that Table 10 is the correct reference for the accuracy gains across script control strategies, while Tables 8 and 9 contain different content entirely—the language inventory and script composition data. So the previous round's change to Tables 8–9 was actually incorrect, and I need to revert to Table 10 in those three locations.

I'm now identifying the exact text replacements needed: changing "Tables 8–9" back to "Table 10" in the opportunity section, the landscape section, and the description section. Since this is a straightforward factual correction based on verified information, I'll mark it as a minor change and keep everything else intact. I'm finding the same reference appearing in multiple sections of the document—the landscape section about ReasonXL's design, the description section about Latin-script reasoning, and it looks like there might be another instance I'm still locating. Let me trace through each mention to see if they all point to the same tables or if some need correction. I'm finding the same citation appearing across multiple sections—the approach, opportunity, landscape, and description all reference §5.2, Figure 6, and Tables 8–9 from arXiv 2505.14815. The reviewer flagged three locations, but I'm seeing at least five distinct mentions of these specific figures and tables throughout the document, so I need to consolidate these redundant citations. I need to replace all instances of "Tables 8–9" with "Table 10" throughout the document to be thorough. Let me carefully scan the approach and description sections again to catch every occurrence, including those that might appear in different contexts beyond just the specific phrase the reviewer highlighted. I'm realizing the reviewer is pointing to a specific correction—all instances of those citation references need to be standardized to "§5.2, Figure 6, and Table 10" instead of the variations I've been using. I've found multiple places where this appears across the landscape and approach sections, so I should go through and update them all consistently rather than leaving some with different table numbers. Now I'm systematically going through the JSON to replace all instances of "Tables 8–9" with "Table 10" wherever they appear alongside the arXiv 2505.14815 citation—I've identified the specific sections that need updating: the opportunity section has one reference, the landscape section has two, and the approach section has at least one more to fix. I'm identifying the specific locations where "Tables 8–9" needs to be changed to "Table 10" in the context of the 44–115% accuracy gains — there are instances in the opportunity section, the landscape section discussing ReasonXL, and likely more throughout the document. Let me go through the JSON systematically and make these corrections across all affected fields. I'm systematically going through the document to find every instance where "Tables 8–9" needs to be changed to "Table 10". I've identified several occurrences across the opportunity, landscape, and approach sections, and I'm now compiling the complete corrected JSON with all the necessary updates applied throughout.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fbae772-2cc7-4627-9837-31ef58bea18b",
  "isSidechain": false,
  "requestId": "req_011CatcXXSxDipm6G7A4y671",
  "type": "assistant",
  "uuid": "7ce0edce-9f45-47fc-a9a5-92d63c744749",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MZAHUA2GCbaiVQLXHeDgaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16328,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4623,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-10T09:00:18.809Z_

Looking at this carefully: the reviewer feedback is mechanical — fix "Tables 8–9" → "Table 10" in all three (possibly more) locations where arXiv 2505.14815 §5.2 accuracy gains are cited. The reviewer has cleared all other issues and says "submit."

Given 8 rounds of iteration, let me verify the citation before touching anything, then apply the fix cleanly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ce0edce-9f45-47fc-a9a5-92d63c744749",
  "isSidechain": false,
  "requestId": "req_011CatcXXSxDipm6G7A4y671",
  "type": "assistant",
  "uuid": "c4a84a42-fa4c-4e7d-ae4b-ce9cc2ffdf62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MZAHUA2GCbaiVQLXHeDgaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16328,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4623,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-10T09:00:23.671Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01JnEswDc517vSVz9RFVttUq`</summary>

```json
{
  "description": "Verify arXiv 2505.14815 table structure",
  "subagent_type": "Explore",
  "prompt": "I need to verify the table structure of arXiv paper 2505.14815 (\"Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes\"). Specifically, I need to know:\n\n1. What does Table 10 contain? Does it contain accuracy comparisons across script control strategies (Latin vs. non-Latin) for non-Latin/Han-script languages like Arabic, Hindi, Japanese? Does it show the 44–115% accuracy gains when reasoning is constrained to Latin script?\n2. What do Tables 8 and 9 contain? Are they language metadata tables (language inventory, script composition across difficulty levels)?\n\nPlease fetch the paper from https://arxiv.org/abs/2505.14815 and https://arxiv.org/pdf/2505.14815 to check the table descriptions in §5.2. I need the factual answer: does Table 10 (not Tables 8–9) document the 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script?\n\nReport in under 150 words with the specific table contents as described in the paper."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4a84a42-fa4c-4e7d-ae4b-ce9cc2ffdf62",
  "isSidechain": false,
  "requestId": "req_011CatcXXSxDipm6G7A4y671",
  "type": "assistant",
  "uuid": "2d48a8de-76ca-4094-82ed-663bec87603a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01MZAHUA2GCbaiVQLXHeDgaq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16328,
      "cache_read_input_tokens": 11631,
      "output_tokens": 4623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16328,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4623,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16328
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-10T09:00:47.257Z_

<details><summary>↩ Tool result · `toolu_01JnEswDc517vSVz9RFVttUq`</summary>

```text
I was unable to extract the specific table contents from the paper using the available web tools. The PDF fetch and search queries returned metadata but not the detailed table data you requested.

**Unable to verify**: I cannot confirm from the sources accessed whether Table 10 (vs. Tables 8–9) documents the 44–115% accuracy gains for non-Latin-script inputs under Latin-script reasoning constraints. The abstract confirms constrained decoding improves accuracy, but the specific table contents, metrics, and numerical comparisons require direct PDF access that the tools could not render.

To verify this, you'll need to:
- Access the full PDF directly via your institution or arXiv
- Search §5.2 for table captions and contents
- Verify which table (8, 9, or 10) shows the script control strategy comparisons

Sources:
- [arXiv 2505.14815 abstract](https://arxiv.org/abs/2505.14815)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2d48a8de-76ca-4094-82ed-663bec87603a",
  "isSidechain": false,
  "promptId": "4909b2b0-2449-4849-9337-10c95a9de91e",
  "type": "user",
  "uuid": "1eac4dfe-4376-4af6-911b-04f7675517d7",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the table structure of arXiv paper 2505.14815 (\"Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes\"). Specifically, I need to know:\n\n1. What does Table 10 contain? Does it contain accuracy comparisons across script control strategies (Latin vs. non-Latin) for non-Latin/Han-script languages like Arabic, Hindi, Japanese? Does it show the 44–115% accuracy gains when reasoning is constrained to Latin script?\n2. What do Tables 8 and 9 contain? Are they language metadata tables (language inventory, script composition across difficulty levels)?\n\nPlease fetch the paper from https://arxiv.org/abs/2505.14815 and https://arxiv.org/pdf/2505.14815 to check the table descriptions in §5.2. I need the factual answer: does Table 10 (not Tables 8–9) document the 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script?\n\nReport in under 150 words with the specific table contents as described in the paper.",
    "agentId": "a008d28d9c9a481bb",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "I was unable to extract the specific table contents from the paper using the available web tools. The PDF fetch and search queries returned metadata but not the detailed table data you requested.\n\n**Unable to verify**: I cannot confirm from the sources accessed whether Table 10 (vs. Tables 8–9) documents the 44–115% accuracy gains for non-Latin-script inputs under Latin-script reasoning constraints. The abstract confirms constrained decoding improves accuracy, but the specific table contents, metrics, and numerical comparisons require direct PDF access that the tools could not render.\n\nTo verify this, you'll need to:\n- Access the full PDF directly via your institution or arXiv\n- Search §5.2 for table captions and contents\n- Verify which table (8, 9, or 10) shows the script control strategy comparisons\n\nSources:\n- [arXiv 2505.14815 abstract](https://arxiv.org/abs/2505.14815)"
      }
    ],
    "totalDurationMs": 23579,
    "totalTokens": 19343,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 764,
      "cache_read_input_tokens": 18358,
      "output_tokens": 216,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 764
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 216,
          "cache_read_input_tokens": 18358,
          "cache_creation_input_tokens": 764,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 764,
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
      "otherToolCount": 3
    }
  },
  "sourceToolAssistantUUID": "2d48a8de-76ca-4094-82ed-663bec87603a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "1eac4dfe-4376-4af6-911b-04f7675517d7",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Correct table citations in multilingual GRPO answer fidelity reward",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Assistant

_source line 14 · 2026-05-10T09:00:57.025Z_

<details><summary>Logged reasoning block</summary>

```text
I can't verify the table contents directly from the tools. But the reviewer has done "independent verification" and is confident. Since:

1. The reviewer states this is a factual correction verified independently
2. The original Round 7 reviewer apparently made an error by changing "Table 10" to "Tables 8-9"
3. The Round 8 reviewer is correcting this back
4. The correction is going BACK to what it was originally (before Round 7 broke it)

I'll trust the reviewer's verification and proceed with the fix. The logic also makes sense: Tables 8 and 9 being "language inventory" and "script composition" tables are metadata tables, while Table 10 being the "accuracy comparison across script control strategies" is the performance table that would show the 44-115% gains.


The reviewer's Round 8 feedback is essentially a green light—all prior issues are resolved and I just need to make this table reference correction. I'll now systematically go through the JSON and replace every instance of "Tables 8–9" with "Table 10" in the relevant sections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1eac4dfe-4376-4af6-911b-04f7675517d7",
  "isSidechain": false,
  "requestId": "req_011Catce7ENWdFU4SLjcFE6B",
  "type": "assistant",
  "uuid": "0dc0d08e-7875-4a2f-98cf-7a41b788a930",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KiyYZmk8MVNHvuSog63eCz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 27959,
      "output_tokens": 10175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10175,
          "cache_read_input_tokens": 27959,
          "cache_creation_input_tokens": 4837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4837
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Assistant

_source line 15 · 2026-05-10T09:04:15.394Z_

The PDF is not directly parseable via tools. The reviewer states they performed independent verification and this is a correction *back* to "Table 10" from a Round 7 error. The internal logic is sound (Tables 8–9 as metadata tables, Table 10 as the accuracy comparison table). I'll apply the fix to all instances.

The stagnation warning is worth examining: the Round 8 reviewer explicitly says "all other issues from Rounds 1–7 are resolved" and "submit." The stagnation in scores reflects cumulative iterative fixes, not unresolved problems — the reviewer is clearing this for submission with one mechanical correction. This is a **minor fix**.

Here is the corrected JSON with all "Tables 8–9" → "Table 10" replacements in every reference to arXiv 2505.14815 §5.2 accuracy gains:

```json
{
  "change_type": "minor",
  "title": "Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO",
  "project_name": "answer_fidelity_free_trace",
  "source": "web_research",
  "core_problem": "GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally tend to generate answers in the target language even when traces are mixed—a training-induced tendency (arXiv 2505.14815, §4.2 attributes this to 'supervision or reward signals focused on the final answer') that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.",
  "opportunity": "'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—§4.2, Finding 2 of that paper states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to models being 'trained with supervision or reward signals focused on the final answer'—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Table 10), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.",
  "landscape": "M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. arXiv 2505.15257 ('When Less Language is More', May 2025) achieves language-reasoning disentanglement at inference time via SVD-based activation ablation—projecting language-specific subspaces out of mid-layer hidden states during the forward pass—with no training required, reporting results comparable to RL (PPO) on MGSM. Our method differs categorically: we achieve answer-surface fidelity via a GRPO reward during standard RL fine-tuning, with no inference-time modification to activations or architecture. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows (§4.2, Finding 2) that 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' attributing this to 'supervision or reward signals focused on the final answer'; it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\n\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (§5.2, Figure 6, Table 10) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\n\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (§5.2, Figure 6, Table 10) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\n\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.",
  "approach": "We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\n\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\n\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (§4.2, Finding 2) states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language'; the §4.2 analysis explicitly notes that 'the final answers remain more aligned with the input language,' attributing this to 'supervision or reward signals focused on the final answer'—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\n\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\n\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\n\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\n\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\n\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per §5.2, Figure 6, and Table 10), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\n\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\n\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\n\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (§4.2, Finding 2) that 'supervision or reward signals focused on the final answer' produce the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\n\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~105-175 H100-hours (4 ablation conditions × 2 seeds × ~12-15 H100-hours/run on Qwen3-7B with LoRA rank-16 on 4×H100 = ~96-120 H100-hours training; secondary Swahili experiment ~15 H100-hours; inference evals including MMLU-ProX 0-shot across 7 languages, XQuAD across 4 languages, pretrained-base cross-task eval, XCOPA, XStoryCloze ~20 H100-hours; sequential debugging adds ~20 H100-hours overhead; upper-end arithmetic: 120 + 15 + 20 + 20 = 175 H100-hours)",
      "gpu_utilization": "Low (~40-50% effective); GPU idles waiting for researcher to iterate on SFVG reward code and analyze SFVG activation trajectories and correct-language rate logs per language",
      "timeline": "6-10 weeks",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$315-525 at $3.00/H100-hr"
    },
    "human_in_loop": {
      "gpu_hours": "~147-182 H100-hours (agent queues ablation conditions in parallel; XQuAD inference ~2 H100-hours added to transfer eval suite; human approves experimental design at 4 key checkpoints: after first non-Latin-script run to verify SFVG Gate 2 activation, after vanilla GRPO baseline, after primary ablation completion, before secondary Swahili experiment)",
      "gpu_utilization": "Moderate (~65-75% effective)",
      "timeline": "4-6 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$150-300 (~1,500-3,000 agent turns for experiment design, SFVG log parsing, correct-language rate monitoring, LID-activation trajectory monitoring, MMLU-ProX and XQuAD inference and result analysis)",
      "estimated_gpu_cost": "~$441-546",
      "risk_note": "Key risk: SFVG Gate 2 (frame-presence check) must be verified to activate before Gate 3 (LID scoring). Human checkpoint after first non-Latin-script run is essential. SFVG gate activation rate and correct-language rate per language per step are the primary diagnostic signals, logged in TRL GRPOTrainer reward callback. Secondary risk: if model learns bare-numeral answers that satisfy Gate 1 but not Gate 2, the LID reward is perpetually inactive—detectable from flat Gate 2 activation curve. Correct-language rate log provides additional signal: if it is low for Latin-script languages under the universal prompt, the language-explicit ablation is promoted to primary."
    },
    "auto_research": {
      "gpu_hours": "~172-215 H100-hours. Grid is fixed at LoRA rank-16 throughout (rank sensitivity is scoped to manual-mode follow-up only; the original claim of sweeping rank ∈ {8,16,32} was removed as it would require 24-36 training runs totalling 288-540 H100-hours, far exceeding the 200 H100-hour budget). The constrained auto-mode grid is: (i) λ sweep {0.1, 0.2, 0.3, 0.5} for the answer-only SFVG condition × 1 seed (exploratory), = 4 runs × ~13 H100-hours = ~52 H100-hours; (ii) best λ re-run × 2 seeds for final reporting = 2 runs × ~13 H100-hours = ~26 H100-hours; (iii) 3 fixed-hyperparameter baselines (vanilla GRPO, whole-trace LC, PB-RLSVR) × 2 seeds = 6 runs × ~13 H100-hours = ~78 H100-hours; (iv) secondary Swahili experiment = ~15 H100-hours; (v) inference evals including pretrained-base cross-task checkpoint on XCOPA/XStoryCloze/MMLU-ProX/XQuAD = ~20 H100-hours. Total: ~191 H100-hours, fitting within the 200 H100-hour budget. The supplementary language-explicit prompt ablation (Gate 2 activation rate and correct-language rate comparison) is run as a short inference-only evaluation on the converged answer-only SFVG model (~3 H100-hours) and is included in the inference budget.",
      "gpu_utilization": "Near-zero idle (~85-90% effective)",
      "timeline": "5-10 days given 8+ H100s simultaneously",
      "team": "0 (initial setup: ~2-3 hours to configure LoRA GRPOTrainer reward functions, SFVG gate logic with script-adaptive thresholds and correct-language rate logging, and evaluation harness including MMLU-ProX and XQuAD 0-shot pipelines)",
      "claude_api_cost": "$300-600 (~3,000-6,000 agent turns for iterative design, SFVG log analysis, correct-language rate trajectory analysis, reward-hacking detection, cross-task transfer analysis, write-up drafting)",
      "estimated_gpu_cost": "~$516-645",
      "speed_bottleneck": "H100 cluster availability; fastText LID inference latency (mitigated by applying LID only to non-numeric answer content rather than the full trace, which is substantially shorter)",
      "risk_note": "Primary risk: SFVG Gate 2 (frame-presence check) flat activation means model is producing bare numerals—detectable from Gate 2 activation curve, triggerable by adjusting system-prompt phrasing or adding format reward weight. Must be caught before training runs complete. Secondary risk: script-adaptive thresholds (8/5/3 chars for Latin/Thai/CJK) may require tuning; initial runs should log per-language gate failure breakdown and correct-language rate. Auto mode must trigger alert if Gate 2 activation drops below 50% for any language after step 200 (indicates model is not learning sentence frames), or if correct-language rate drops below 70% for any Latin-script language under the universal prompt (indicates cross-Latin-script confusion degrading LID reward signal). If the correct-language rate is systematically low for Latin-script languages under the universal prompt, the language-explicit prompt variant is promoted from supplementary to primary."
    }
  },
  "target_venues": [
    "EMNLP 2026 Findings (ARR submission deadline May 25, 2026)"
  ],
  "key_references": [
    "When Verifiable Rewards Switch the Language: Cross-lingual Collapse in Chain-of-Thought (arXiv 2506.05850, Jun 2025)",
    "Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes (arXiv 2505.14815, May 2025)",
    "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners (arXiv 2505.15257, May 2025)",
    "Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning / M-Thinker (arXiv 2510.07300, Oct 2025)",
    "Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, Oct 2025)",
    "Long Chain-of-Thought Reasoning Across Languages (arXiv 2508.14828, Aug 2025)",
    "Making Qwen3 Think in Korean with Reinforcement Learning (arXiv 2508.10355, Aug 2025)",
    "Aligning Multilingual Reasoning with Verifiable Semantics from a High-Resource Expert Model / PB-RLSVR (arXiv 2509.25543, Sep 2025)",
    "Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought (arXiv 2510.04230, Oct 2025)",
    "ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection (arXiv 2602.21887, Feb 2026)",
    "Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training / TRIT (arXiv 2602.05940, Feb 2026)",
    "Language as a Latent Variable for Reasoning Optimization / polyGRPO (arXiv 2604.21593, Apr 2026)",
    "TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models (arXiv 2604.26553, Apr 2026)",
    "What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features (arXiv 2604.04720, Apr 2026)",
    "ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance (arXiv 2604.12378, Apr 2026)",
    "MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation (arXiv 2503.10497, EMNLP 2025 Main)",
    "XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (arXiv 2305.11938, EMNLP 2023 Findings)"
  ],
  "description": "We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers: §4.2, Finding 2 states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to 'supervision or reward signals focused on the final answer'; and (b) Latin-script (English) reasoning yields optimal accuracy (§5.2, Figure 6, Table 10: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (§4.2, Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\n\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\n\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\n\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal], and arXiv 2505.15257 [training-free SVD activation ablation at inference time]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features or hidden-state geometry without proposing a GRPO reward that decouples trace from answer constraint. Target: EMNLP 2026 Findings."
}
```

---

**Summary of changes (minor fix):**

Five instances of `Tables 8–9` corrected to `Table 10` in the context of arXiv 2505.14815 §5.2 accuracy gains:

| Location | Before | After |
|---|---|---|
| `opportunity` | `§5.2, Figure 6, and Tables 8–9` | `§5.2, Figure 6, and Table 10` |
| `landscape` (ReasonXL paragraph) | `(§5.2, Figure 6, Tables 8–9) shows imposes an accuracy penalty` | `(§5.2, Figure 6, Table 10) shows imposes an accuracy penalty` |
| `landscape` (Ki et al. paragraph) | `(§5.2, Figure 6, Tables 8–9) and arXiv 2506.05850` | `(§5.2, Figure 6, Table 10) and arXiv 2506.05850` |
| `approach` (GRPO optimization paragraph) | `per §5.2, Figure 6, and Tables 8–9` | `per §5.2, Figure 6, and Table 10` |
| `description` | `(§5.2, Figure 6, Tables 8–9: 44–115% accuracy gains` | `(§5.2, Figure 6, Table 10: 44–115% accuracy gains` |

The reviewer flagged three canonical locations (opportunity, landscape, description); the approach section contained a fourth instance that is corrected here for internal consistency. No other content was modified. All other issues from rounds 1–7 remain addressed as confirmed by the Round 8 reviewer.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0dc0d08e-7875-4a2f-98cf-7a41b788a930",
  "isSidechain": false,
  "requestId": "req_011Catce7ENWdFU4SLjcFE6B",
  "type": "assistant",
  "uuid": "efcd7e18-3d39-43e6-a8f2-42b574a82beb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01KiyYZmk8MVNHvuSog63eCz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4837,
      "cache_read_input_tokens": 27959,
      "output_tokens": 10175,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4837,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 10175,
          "cache_read_input_tokens": 27959,
          "cache_creation_input_tokens": 4837,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4837
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    }
  }
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "efcd7e18-3d39-43e6-a8f2-42b574a82beb",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Correct table citations in multilingual GRPO answer fidelity reward",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "efcd7e18-3d39-43e6-a8f2-42b574a82beb",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Correct table citations in multilingual GRPO answer fidelity reward",
  "sessionId": "19bf699c-697e-4469-8fdb-f6b0b20226f6"
}
```

---
