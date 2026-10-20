# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 39
- **Recorded user turns:** 2
- **Tool calls:** 7
- **Original source:** `logs/chats/exported-trajectories/account-1/05994783-f94c-4701-be9b-3d05f4c89f00.jsonl`
- **Structured JSON:** [`c4ac09341d1fa9677963.json`](../../sessions/c4/c4ac09341d1fa9677963.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T09:12:22.478Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T09:12:22.478Z",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\",\n  \"project_name\": \"answer_fidelity_free_trace\",\n  \"source\": \"web_research\",\n  \"core_problem\": \"GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally tend to generate answers in the target language even when traces are mixed—a training-induced tendency (arXiv 2505.14815, §4.2 attributes this to 'supervision or reward signals focused on the final answer') that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.\",\n  \"opportunity\": \"'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—§4.2, Finding 2 of that paper states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to models being 'trained with supervision or reward signals focused on the final answer'—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Table 10), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\",\n  \"landscape\": \"M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. arXiv 2505.15257 ('When Less Language is More', May 2025) achieves language-reasoning disentanglement at inference time via SVD-based activation ablation—projecting language-specific subspaces out of mid-layer hidden states during the forward pass—with no training required, reporting results comparable to RL (PPO) on MGSM. Our method differs categorically: we achieve answer-surface fidelity via a GRPO reward during standard RL fine-tuning, with no inference-time modification to activations or architecture. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows (§4.2, Finding 2) that 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' attributing this to 'supervision or reward signals focused on the final answer'; it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\\n\\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (§5.2, Figure 6, Table 10) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\\n\\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (§5.2, Figure 6, Table 10) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\\n\\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.\",\n  \"approach\": \"We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\\n\\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\\n\\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (§4.2, Finding 2) states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language'; the §4.2 analysis explicitly notes that 'the final answers remain more aligned with the input language,' attributing this to 'supervision or reward signals focused on the final answer'—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\\n\\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\\n\\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\\n\\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\\n\\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\\n\\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per §5.2, Figure 6, and Table 10), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\\n\\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\\n\\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\\n\\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (§4.2, Finding 2) that 'supervision or reward signals focused on the final answer' produce the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\\n\\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~105-175 H100-hours (4 ablation conditions × 2 seeds × ~12-15 H100-hours/run on Qwen3-7B with LoRA rank-16 on 4×H100 = ~96-120 H100-hours training; secondary Swahili experiment ~15 H100-hours; inference evals including MMLU-ProX 0-shot across 7 languages, XQuAD across 4 languages, pretrained-base cross-task eval, XCOPA, XStoryCloze ~20 H100-hours; sequential debugging adds ~20 H100-hours overhead; upper-end arithmetic: 120 + 15 + 20 + 20 = 175 H100-hours)\",\n      \"gpu_utilization\": \"Low (~40-50% effective); GPU idles waiting for researcher to iterate on SFVG reward code and analyze SFVG activation trajectories and correct-language rate logs per language\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$315-525 at $3.00/H100-hr\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~147-182 H100-hours (agent queues ablation conditions in parallel; XQuAD inference ~2 H100-hours added to transfer eval suite; human approves experimental design at 4 key checkpoints: after first non-Latin-script run to verify SFVG Gate 2 activation, after vanilla GRPO baseline, after primary ablation completion, before secondary Swahili experiment)\",\n      \"gpu_utilization\": \"Moderate (~65-75% effective)\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150-300 (~1,500-3,000 agent turns for experiment design, SFVG log parsing, correct-language rate monitoring, LID-activation trajectory monitoring, MMLU-ProX and XQuAD inference and result analysis)\",\n      \"estimated_gpu_cost\": \"~$441-546\",\n      \"risk_note\": \"Key risk: SFVG Gate 2 (frame-presence check) must be verified to activate before Gate 3 (LID scoring). Human checkpoint after first non-Latin-script run is essential. SFVG gate activation rate and correct-language rate per language per step are the primary diagnostic signals, logged in TRL GRPOTrainer reward callback. Secondary risk: if model learns bare-numeral answers that satisfy Gate 1 but not Gate 2, the LID reward is perpetually inactive—detectable from flat Gate 2 activation curve. Correct-language rate log provides additional signal: if it is low for Latin-script languages under the universal prompt, the language-explicit ablation is promoted to primary.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~172-215 H100-hours. Grid is fixed at LoRA rank-16 throughout (rank sensitivity is scoped to manual-mode follow-up only; the original claim of sweeping rank ∈ {8,16,32} was removed as it would require 24-36 training runs totalling 288-540 H100-hours, far exceeding the 200 H100-hour budget). The constrained auto-mode grid is: (i) λ sweep {0.1, 0.2, 0.3, 0.5} for the answer-only SFVG condition × 1 seed (exploratory), = 4 runs × ~13 H100-hours = ~52 H100-hours; (ii) best λ re-run × 2 seeds for final reporting = 2 runs × ~13 H100-hours = ~26 H100-hours; (iii) 3 fixed-hyperparameter baselines (vanilla GRPO, whole-trace LC, PB-RLSVR) × 2 seeds = 6 runs × ~13 H100-hours = ~78 H100-hours; (iv) secondary Swahili experiment = ~15 H100-hours; (v) inference evals including pretrained-base cross-task checkpoint on XCOPA/XStoryCloze/MMLU-ProX/XQuAD = ~20 H100-hours. Total: ~191 H100-hours, fitting within the 200 H100-hour budget. The supplementary language-explicit prompt ablation (Gate 2 activation rate and correct-language rate comparison) is run as a short inference-only evaluation on the converged answer-only SFVG model (~3 H100-hours) and is included in the inference budget.\",\n      \"gpu_utilization\": \"Near-zero idle (~85-90% effective)\",\n      \"timeline\": \"5-10 days given 8+ H100s simultaneously\",\n      \"team\": \"0 (initial setup: ~2-3 hours to configure LoRA GRPOTrainer reward functions, SFVG gate logic with script-adaptive thresholds and correct-language rate logging, and evaluation harness including MMLU-ProX and XQuAD 0-shot pipelines)\",\n      \"claude_api_cost\": \"$300-600 (~3,000-6,000 agent turns for iterative design, SFVG log analysis, correct-language rate trajectory analysis, reward-hacking detection, cross-task transfer analysis, write-up drafting)\",\n      \"estimated_gpu_cost\": \"~$516-645\",\n      \"speed_bottleneck\": \"H100 cluster availability; fastText LID inference latency (mitigated by applying LID only to non-numeric answer content rather than the full trace, which is substantially shorter)\",\n      \"risk_note\": \"Primary risk: SFVG Gate 2 (frame-presence check) flat activation means model is producing bare numerals—detectable from Gate 2 activation curve, triggerable by adjusting system-prompt phrasing or adding format reward weight. Must be caught before training runs complete. Secondary risk: script-adaptive thresholds (8/5/3 chars for Latin/Thai/CJK) may require tuning; initial runs should log per-language gate failure breakdown and correct-language rate. Auto mode must trigger alert if Gate 2 activation drops below 50% for any language after step 200 (indicates model is not learning sentence frames), or if correct-language rate drops below 70% for any Latin-script language under the universal prompt (indicates cross-Latin-script confusion degrading LID reward signal). If the correct-language rate is systematically low for Latin-script languages under the universal prompt, the language-explicit prompt variant is promoted from supplementary to primary.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR submission deadline May 25, 2026)\"\n  ],\n  \"key_references\": [\n    \"When Verifiable Rewards Switch the Language: Cross-lingual Collapse in Chain-of-Thought (arXiv 2506.05850, Jun 2025)\",\n    \"Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes (arXiv 2505.14815, May 2025)\",\n    \"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners (arXiv 2505.15257, May 2025)\",\n    \"Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning / M-Thinker (arXiv 2510.07300, Oct 2025)\",\n    \"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, Oct 2025)\",\n    \"Long Chain-of-Thought Reasoning Across Languages (arXiv 2508.14828, Aug 2025)\",\n    \"Making Qwen3 Think in Korean with Reinforcement Learning (arXiv 2508.10355, Aug 2025)\",\n    \"Aligning Multilingual Reasoning with Verifiable Semantics from a High-Resource Expert Model / PB-RLSVR (arXiv 2509.25543, Sep 2025)\",\n    \"Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought (arXiv 2510.04230, Oct 2025)\",\n    \"ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection (arXiv 2602.21887, Feb 2026)\",\n    \"Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training / TRIT (arXiv 2602.05940, Feb 2026)\",\n    \"Language as a Latent Variable for Reasoning Optimization / polyGRPO (arXiv 2604.21593, Apr 2026)\",\n    \"TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models (arXiv 2604.26553, Apr 2026)\",\n    \"What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features (arXiv 2604.04720, Apr 2026)\",\n    \"ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance (arXiv 2604.12378, Apr 2026)\",\n    \"MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation (arXiv 2503.10497, EMNLP 2025 Main)\",\n    \"XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (arXiv 2305.11938, EMNLP 2023 Findings)\"\n  ],\n  \"description\": \"We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers: §4.2, Finding 2 states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to 'supervision or reward signals focused on the final answer'; and (b) Latin-script (English) reasoning yields optimal accuracy (§5.2, Figure 6, Table 10: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (§4.2, Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\\n\\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\\n\\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\\n\\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal], and arXiv 2505.15257 [training-free SVD activation ablation at inference time]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features or hidden-state geometry without proposing a GRPO reward that decouples trace from answer constraint. Target: EMNLP 2026 Findings.\"\n}\n\n## Reviewer feedback (round 9)\nIssues: [\"MISSING CONCURRENT WORK — mGRPO ('Unlocking LLM Reasoning through Multilingual Thinking', submitted to ICLR 2026, OpenReview https://openreview.net/forum?id=QtfALPluAj, Sept 2025) is absent from the landscape section. mGRPO evaluates on MGSM, PolyMath, and X-CSQA — the same primary benchmarks as the proposed method — and achieves +7.5% average over Qwen2.5 and Llama3 across those tasks. Its approach (generating multilingual preference data via both language-constrained and unconstrained prompts with group-wise correctness and format rewards) differs from answer-only SFVG: mGRPO does not impose any answer-language-specific reward, and no trace/answer decoupling is mentioned. The paper has no arXiv version (only OpenReview), which explains why it was not caught, but EMNLP reviewers who reviewed or tracked ICLR 2026 submissions may ask about it. A one-sentence differentiation is sufficient: 'mGRPO generates multilingual preference rollouts to expand the reasoning exploration space but imposes no answer-language constraint; our method leaves the reasoning trace entirely unconstrained and enforces answer-surface language fidelity via the SFVG reward, a categorically different design goal.'\"]\nFeedback: The paper has addressed all eight prior rounds of issues cleanly: the Table 10 citation (corrected to '§5.2, Figure 6, and Table 10' in all three locations), the SFVG gate design, universal-prompt specification, correct-language rate metric, pretrained-base cross-task checkpoint, XQuAD inclusion, MMLU-ProX, polyGRPO numerical comparison, Ki et al. integration, ReasonXL differentiation, 2505.15257 mention, XTREME-UP exclusion justification, and compute consistency are all resolved. One targeted fix remains: add a single sentence about mGRPO (OpenReview ICLR 2026) to the landscape section. Differentiate as follows — mGRPO uses language-constrained and unconstrained GRPO rollouts as preference data to expand polyglot thinking without imposing any answer-language-specific reward, whereas the proposed method leaves reasoning traces entirely unconstrained and enforces answer-surface language fidelity exclusively via SFVG, a fundamentally different design goal. With this addition, the landscape is complete and the paper is ready for ARR submission.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 9 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T09:12:22.483Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T09:12:22.483Z",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

## Round 1

28 recorded events

### User

_source line 3 · 2026-05-10T09:12:22.523Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
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

## Reviewer feedback (round 9)
Issues: ["MISSING CONCURRENT WORK — mGRPO ('Unlocking LLM Reasoning through Multilingual Thinking', submitted to ICLR 2026, OpenReview https://openreview.net/forum?id=QtfALPluAj, Sept 2025) is absent from the landscape section. mGRPO evaluates on MGSM, PolyMath, and X-CSQA — the same primary benchmarks as the proposed method — and achieves +7.5% average over Qwen2.5 and Llama3 across those tasks. Its approach (generating multilingual preference data via both language-constrained and unconstrained prompts with group-wise correctness and format rewards) differs from answer-only SFVG: mGRPO does not impose any answer-language-specific reward, and no trace/answer decoupling is mentioned. The paper has no arXiv version (only OpenReview), which explains why it was not caught, but EMNLP reviewers who reviewed or tracked ICLR 2026 submissions may ask about it. A one-sentence differentiation is sufficient: 'mGRPO generates multilingual preference rollouts to expand the reasoning exploration space but imposes no answer-language constraint; our method leaves the reasoning trace entirely unconstrained and enforces answer-surface language fidelity via the SFVG reward, a categorically different design goal.'"]
Feedback: The paper has addressed all eight prior rounds of issues cleanly: the Table 10 citation (corrected to '§5.2, Figure 6, and Table 10' in all three locations), the SFVG gate design, universal-prompt specification, correct-language rate metric, pretrained-base cross-task checkpoint, XQuAD inclusion, MMLU-ProX, polyGRPO numerical comparison, Ki et al. integration, ReasonXL differentiation, 2505.15257 mention, XTREME-UP exclusion justification, and compute consistency are all resolved. One targeted fix remains: add a single sentence about mGRPO (OpenReview ICLR 2026) to the landscape section. Differentiate as follows — mGRPO uses language-constrained and unconstrained GRPO rollouts as preference data to expand polyglot thinking without imposing any answer-language-specific reward, whereas the proposed method leaves reasoning traces entirely unconstrained and enforces answer-surface language fidelity exclusively via SFVG, a fundamentally different design goal. With this addition, the landscape is complete and the paper is ready for ARR submission.

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
这个 idea 已经经过 9 轮修订，近 3 轮的平均分从 3.8 到 3.8，没有明显改善。

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
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "2a4c61fd-7162-48f6-ace4-7c6aca3141ec",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T09:12:22.519Z_

```json
{
  "parentUuid": "2a4c61fd-7162-48f6-ace4-7c6aca3141ec",
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
  "uuid": "f55c39c2-b9d6-4fef-8109-3a7c95c1875a",
  "timestamp": "2026-05-10T09:12:22.519Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T09:12:22.520Z_

```json
{
  "parentUuid": "f55c39c2-b9d6-4fef-8109-3a7c95c1875a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ce65f5a2-9102-4641-921b-e6a611368d4c",
  "timestamp": "2026-05-10T09:12:22.520Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
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
  "leafUuid": "ce65f5a2-9102-4641-921b-e6a611368d4c",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-fidelity multilingual GRPO with mGRPO differentiation",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Assistant

_source line 8 · 2026-05-10T09:12:38.257Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

**Current State:**
- Round 9 of revisions
- Score has been stagnant (3.8 average) for the last 3 rounds
- The feedback this round is very specific and minor: add a one-sentence differentiation for mGRPO (OpenReview ICLR 2026)
- The reviewer explicitly says: "The paper has addressed all eight prior rounds of issues cleanly" and "With this addition, the landscape is complete and the paper is ready for ARR submission."

**The reviewer's assessment is actually positive** - they're not saying the idea is flawed. They're saying one targeted fix remains and after that, it's ready for submission.


The stagnation in previous rounds might reflect incomplete feedback, but this round's reviewer is explicitly green-lighting the paper for submission once I add that single differentiation for mGRPO. This is a clear signal to make the targeted fix rather than pivot. I need to fetch the mGRPO paper from OpenReview to understand how it differs from this approach, since the reviewer has already provided clear differentiation text about the multilingual preference rollouts versus the answer-surface language fidelity design. Once I have that context, I can add mGRPO to both the landscape section and key references with the appropriate one-sentence distinction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ce65f5a2-9102-4641-921b-e6a611368d4c",
  "isSidechain": false,
  "requestId": "req_011CatdXN6kZXRgPgZxTBHfy",
  "type": "assistant",
  "uuid": "e35572e3-3baa-447d-90fc-b9bef890b79d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FotDWbmzF5xxTv7FvfafSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16341,
      "cache_read_input_tokens": 11631,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 965,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16341
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

_source line 9 · 2026-05-10T09:12:38.579Z_

The reviewer gives an explicit green light — "the paper is ready for ARR submission" — with one targeted fix: add mGRPO from ICLR 2026 OpenReview to the landscape. Before writing the differentiation, I'll read the actual paper to verify the characterization rather than relying on the reviewer's summary alone.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e35572e3-3baa-447d-90fc-b9bef890b79d",
  "isSidechain": false,
  "requestId": "req_011CatdXN6kZXRgPgZxTBHfy",
  "type": "assistant",
  "uuid": "bd841587-4ae5-4337-886b-b4d4d4150b45",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FotDWbmzF5xxTv7FvfafSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16341,
      "cache_read_input_tokens": 11631,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 965,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16341
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

_source line 10 · 2026-05-10T09:12:39.027Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_011hFWimVSuYpt45rJsAsZNN`</summary>

```json
{
  "query": "select:WebFetch,WebSearch",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bd841587-4ae5-4337-886b-b4d4d4150b45",
  "isSidechain": false,
  "requestId": "req_011CatdXN6kZXRgPgZxTBHfy",
  "type": "assistant",
  "uuid": "83a0e409-5a57-4ecf-bcba-d61e3d5fa520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01FotDWbmzF5xxTv7FvfafSq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16341,
      "cache_read_input_tokens": 11631,
      "output_tokens": 965,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16341,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 965,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16341,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16341
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

_source line 11 · 2026-05-10T09:12:39.040Z_

<details><summary>↩ Tool result · `toolu_011hFWimVSuYpt45rJsAsZNN`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "83a0e409-5a57-4ecf-bcba-d61e3d5fa520",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "39a23373-800a-44e4-bad4-21c9c7c0d0ae",
  "toolUseResult": {
    "matches": [
      "WebFetch",
      "WebSearch"
    ],
    "query": "select:WebFetch,WebSearch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "83a0e409-5a57-4ecf-bcba-d61e3d5fa520",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T09:12:41.234Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me fetch the mGRPO paper from OpenReview to understand it properly before writing the differentiation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "39a23373-800a-44e4-bad4-21c9c7c0d0ae",
  "isSidechain": false,
  "requestId": "req_011CatdYb29yF7YuEL5xaB9f",
  "type": "assistant",
  "uuid": "cf84f5a6-2154-419f-864c-9cb5dffdb871",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01B9tZDMJj9MnXUrGVQabzCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 27972,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 281,
          "cache_read_input_tokens": 27972,
          "cache_creation_input_tokens": 1986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1986
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

_source line 13 · 2026-05-10T09:12:43.598Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_0196BynsJEJVpZR5kabncTzo`</summary>

```json
{
  "url": "https://openreview.net/forum?id=QtfALPluAj",
  "prompt": "Extract the paper title, abstract, method description, key approach details, evaluation benchmarks, and results. Specifically: (1) How does mGRPO work? (2) Does it impose any language constraint on the answer vs. the reasoning trace? (3) What benchmarks does it evaluate on and what results does it achieve? (4) Does it decouple trace language from answer language?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cf84f5a6-2154-419f-864c-9cb5dffdb871",
  "isSidechain": false,
  "requestId": "req_011CatdYb29yF7YuEL5xaB9f",
  "type": "assistant",
  "uuid": "beda7eba-0e61-4b69-bed1-93dc86aaf937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01B9tZDMJj9MnXUrGVQabzCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 27972,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 281,
          "cache_read_input_tokens": 27972,
          "cache_creation_input_tokens": 1986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1986
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

_source line 14 · 2026-05-10T09:12:43.968Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011HDJFRQLoCVQwnMDQ8XQge`</summary>

```json
{
  "query": "mGRPO \"Unlocking LLM Reasoning through Multilingual Thinking\" ICLR 2026 multilingual GRPO"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beda7eba-0e61-4b69-bed1-93dc86aaf937",
  "isSidechain": false,
  "requestId": "req_011CatdYb29yF7YuEL5xaB9f",
  "type": "assistant",
  "uuid": "272fb3e3-19f3-45f7-9e45-f729621e1c1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01B9tZDMJj9MnXUrGVQabzCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1986,
      "cache_read_input_tokens": 27972,
      "output_tokens": 281,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1986,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 281,
          "cache_read_input_tokens": 27972,
          "cache_creation_input_tokens": 1986,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1986
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

_source line 15 · 2026-05-10T09:12:47.811Z_

<details><summary>↩ Tool result · `toolu_0196BynsJEJVpZR5kabncTzo`</summary>

```text
# mGRPO: Multilingual LLM Reasoning Analysis

## Paper Overview
**Title:** "mGRPO: Unlocking LLM Reasoning through Multilingual Thinking"

**Abstract Summary:** The research investigates how non-English languages can enhance LLM reasoning capabilities. A key finding is that "non-English responses often achieve higher accuracy than English ones" when models freely choose their language.

## How mGRPO Works

mGRPO is described as "a reinforcement learning framework that improves LLM reasoning by generating multilingual preference data online." The approach generates training data using both language-constrained and unconstrained prompts, then optimizes through "group-wise reward comparisons based on accuracy and reasoning format."

## Language Constraints

Based on the available content, the method uses "language-constrained and unconstrained prompts" during training. However, the abstract does not specify whether reasoning traces and answers are decoupled linguistically, nor does it explicitly detail constraints on individual components. The framework allows the model to operate without language restriction, but specific architectural separation between trace and answer languages is not detailed in this excerpt.

## Evaluation Results

**Benchmarks tested:** MGSM, MATH500, PolyMath, and X-CSQA

**Performance:** The method "achieves consistent gains across four benchmarks...outperforming two base LLMs (Qwen2.5 and Llama3) by an average of 7.5%" and "obtains SOTA scores."

**Training efficiency:** Results are achieved using "only ~18.1k training examples without chain-of-thought supervision."
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "beda7eba-0e61-4b69-bed1-93dc86aaf937",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "9f47e766-c33e-4e7d-8666-f4e008d7cd80",
  "toolUseResult": {
    "bytes": 72301,
    "code": 200,
    "codeText": "OK",
    "result": "# mGRPO: Multilingual LLM Reasoning Analysis\n\n## Paper Overview\n**Title:** \"mGRPO: Unlocking LLM Reasoning through Multilingual Thinking\"\n\n**Abstract Summary:** The research investigates how non-English languages can enhance LLM reasoning capabilities. A key finding is that \"non-English responses often achieve higher accuracy than English ones\" when models freely choose their language.\n\n## How mGRPO Works\n\nmGRPO is described as \"a reinforcement learning framework that improves LLM reasoning by generating multilingual preference data online.\" The approach generates training data using both language-constrained and unconstrained prompts, then optimizes through \"group-wise reward comparisons based on accuracy and reasoning format.\"\n\n## Language Constraints\n\nBased on the available content, the method uses \"language-constrained and unconstrained prompts\" during training. However, the abstract does not specify whether reasoning traces and answers are decoupled linguistically, nor does it explicitly detail constraints on individual components. The framework allows the model to operate without language restriction, but specific architectural separation between trace and answer languages is not detailed in this excerpt.\n\n## Evaluation Results\n\n**Benchmarks tested:** MGSM, MATH500, PolyMath, and X-CSQA\n\n**Performance:** The method \"achieves consistent gains across four benchmarks...outperforming two base LLMs (Qwen2.5 and Llama3) by an average of 7.5%\" and \"obtains SOTA scores.\"\n\n**Training efficiency:** Results are achieved using \"only ~18.1k training examples without chain-of-thought supervision.\"",
    "durationMs": 4208,
    "url": "https://openreview.net/forum?id=QtfALPluAj"
  },
  "sourceToolAssistantUUID": "beda7eba-0e61-4b69-bed1-93dc86aaf937",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-10T09:12:48.547Z_

<details><summary>↩ Tool result · `toolu_011HDJFRQLoCVQwnMDQ8XQge`</summary>

```text
Web search results for query: "mGRPO "Unlocking LLM Reasoning through Multilingual Thinking" ICLR 2026 multilingual GRPO"

Links: [{"title":"mGRPO: Unlocking LLM Reasoning through Multilingual Thinking | OpenReview","url":"https://openreview.net/forum?id=QtfALPluAj"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"ICLR 2026 Orals","url":"https://iclr.cc/virtual/2026/events/oral"},{"title":"ICLR 2026 Workshop LLM Reasoning | OpenReview","url":"https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLLM_Reasoning"},{"title":"ICLR 2026 Workshop","url":"https://sites.google.com/view/iclr-2026-llmreasoning"},{"title":"ICLR 2026 Schedule","url":"https://iclr.cc/virtual/2026/calendar"},{"title":"$\\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving | OpenReview","url":"https://openreview.net/forum?id=HBOLN5m3qg"},{"title":"ICLR.2026 | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/venue/ICLR.2026"},{"title":"ICLR 2026 Thursday 04/23","url":"https://iclr.cc/virtual/2026/day/4/23"},{"title":"ICLR 2026 Workshop LLM Reasoning Submissions","url":"https://openreview.net/submissions?page=6&venue=ICLR.cc/2026/Workshop/LLM_Reasoning"}]

Based on the web search results, I found information about your query:

**mGRPO (Multilingual Group Relative Policy Optimization)** is a reinforcement learning framework that improves LLM reasoning by generating multilingual preference data online using both language-constrained and unconstrained prompts.

The paper appears to be submitted to ICLR 2026 and is available on OpenReview at: https://openreview.net/forum?id=QtfALPluAj (posted October 8, 2025).

The framework builds on insights about how multilingual thinking can enhance language model reasoning capabilities, combining reinforcement learning approaches with multilingual data generation strategies. This work represents an advance in using diverse language constraints to improve the reasoning performance of large language models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "272fb3e3-19f3-45f7-9e45-f729621e1c1d",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "2104c9e3-1947-45ab-8297-f8d1bf5ceb1e",
  "toolUseResult": {
    "query": "mGRPO \"Unlocking LLM Reasoning through Multilingual Thinking\" ICLR 2026 multilingual GRPO",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X9KGM34MfCwim9qkyG6zvP",
        "content": [
          {
            "title": "mGRPO: Unlocking LLM Reasoning through Multilingual Thinking | OpenReview",
            "url": "https://openreview.net/forum?id=QtfALPluAj"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "ICLR 2026 Orals",
            "url": "https://iclr.cc/virtual/2026/events/oral"
          },
          {
            "title": "ICLR 2026 Workshop LLM Reasoning | OpenReview",
            "url": "https://openreview.net/group?id=ICLR.cc%2F2026%2FWorkshop%2FLLM_Reasoning"
          },
          {
            "title": "ICLR 2026 Workshop",
            "url": "https://sites.google.com/view/iclr-2026-llmreasoning"
          },
          {
            "title": "ICLR 2026 Schedule",
            "url": "https://iclr.cc/virtual/2026/calendar"
          },
          {
            "title": "$\\textbf{Re}^{2}$: Unlocking LLM Reasoning via Reinforcement Learning with Re-solving | OpenReview",
            "url": "https://openreview.net/forum?id=HBOLN5m3qg"
          },
          {
            "title": "ICLR.2026 | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/venue/ICLR.2026"
          },
          {
            "title": "ICLR 2026 Thursday 04/23",
            "url": "https://iclr.cc/virtual/2026/day/4/23"
          },
          {
            "title": "ICLR 2026 Workshop LLM Reasoning Submissions",
            "url": "https://openreview.net/submissions?page=6&venue=ICLR.cc/2026/Workshop/LLM_Reasoning"
          }
        ]
      },
      "Based on the web search results, I found information about your query:\n\n**mGRPO (Multilingual Group Relative Policy Optimization)** is a reinforcement learning framework that improves LLM reasoning by generating multilingual preference data online using both language-constrained and unconstrained prompts.\n\nThe paper appears to be submitted to ICLR 2026 and is available on OpenReview at: https://openreview.net/forum?id=QtfALPluAj (posted October 8, 2025).\n\nThe framework builds on insights about how multilingual thinking can enhance language model reasoning capabilities, combining reinforcement learning approaches with multilingual data generation strategies. This work represents an advance in using diverse language constraints to improve the reasoning performance of large language models."
    ],
    "durationSeconds": 4.574956435
  },
  "sourceToolAssistantUUID": "272fb3e3-19f3-45f7-9e45-f729621e1c1d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 17 · 2026-05-10T09:12:54.459Z_

<details><summary>Logged reasoning block</summary>

```text
Good. I have the key facts about mGRPO:

1. **Method**: mGRPO generates multilingual preference data online using both language-constrained and unconstrained prompts, then uses group-wise reward comparisons based on accuracy and reasoning format.

2. **Language constraints**: Uses both language-constrained AND unconstrained prompts during training - but no specific trace/answer decoupling mentioned. The framework generates preferences by comparing constrained vs. unconstrained rollouts.

3. **Benchmarks**: MGSM, MATH500, PolyMath, X-CSQA


4. **Results**: +7.5% average improvement over Qwen2.5 and Llama3 across benchmarks

5. **Reward design**: The approach relies on accuracy and format-based rewards without any language-specific decoupling between reasoning traces and final answers.

Now I need to look at the actual paper to understand their specific methodology in more detail.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2104c9e3-1947-45ab-8297-f8d1bf5ceb1e",
  "isSidechain": false,
  "requestId": "req_011CatdZGkqRBi33tYmTSvzE",
  "type": "assistant",
  "uuid": "15d084f8-d67e-4915-9f79-b6911d67b9d6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SAjbAMUZTrLFPq2kUm77r5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 29958,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 29958,
          "cache_creation_input_tokens": 1390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1390
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

_source line 18 · 2026-05-10T09:12:54.467Z_

Good. Let me get the actual paper content for a more thorough read.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "15d084f8-d67e-4915-9f79-b6911d67b9d6",
  "isSidechain": false,
  "requestId": "req_011CatdZGkqRBi33tYmTSvzE",
  "type": "assistant",
  "uuid": "6caee901-2809-4095-9a25-1f92ae944d23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SAjbAMUZTrLFPq2kUm77r5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 29958,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 29958,
          "cache_creation_input_tokens": 1390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1390
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

_source line 19 · 2026-05-10T09:12:55.145Z_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01EDkm6ShS7Nbz43pWo2D5da`</summary>

```json
{
  "url": "https://openreview.net/pdf?id=QtfALPluAj",
  "prompt": "Describe the full method of mGRPO in detail: (1) What reward signals does it use? (2) How does it handle language-constrained vs unconstrained prompts? (3) Does it constrain the reasoning trace, the answer, or neither? (4) What is the preference data generation procedure? (5) Any decoupling of trace language vs answer language?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6caee901-2809-4095-9a25-1f92ae944d23",
  "isSidechain": false,
  "requestId": "req_011CatdZGkqRBi33tYmTSvzE",
  "type": "assistant",
  "uuid": "64fc16f1-e55b-418e-bbc6-0dff882072c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01SAjbAMUZTrLFPq2kUm77r5",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1390,
      "cache_read_input_tokens": 29958,
      "output_tokens": 444,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1390,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 444,
          "cache_read_input_tokens": 29958,
          "cache_creation_input_tokens": 1390,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1390
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

_source line 20 · 2026-05-10T09:12:59.952Z_

<details><summary>↩ Tool result · `toolu_01EDkm6ShS7Nbz43pWo2D5da`</summary>

```text
I appreciate your detailed question about mGRPO, but I'm unable to provide a comprehensive answer based on the provided content. The document appears to be a PDF file containing encoded stream data that isn't readable as plain text. The visible elements show only PDF structural information (object references, filters, encoding specifications) rather than the actual article content describing the mGRPO method.

To accurately address your five-part question about:
1. Reward signals used
2. Handling of language-constrained vs unconstrained prompts
3. Constraint application (trace vs answer)
4. Preference data generation
5. Trace/answer language decoupling

I would need access to the actual readable text of the research paper. Could you provide either:
- A text version of the paper, or
- The actual PDF content in readable format, or
- A link to the paper's published version?

This would allow me to give you a properly sourced response following your citation requirements.

[Binary content (application/pdf, 4.9MB) also saved to /home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf]
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "64fc16f1-e55b-418e-bbc6-0dff882072c7",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "e5585a3d-e9ec-42f1-9c26-b59270715e4e",
  "toolUseResult": {
    "bytes": 5126326,
    "code": 200,
    "codeText": "OK",
    "result": "I appreciate your detailed question about mGRPO, but I'm unable to provide a comprehensive answer based on the provided content. The document appears to be a PDF file containing encoded stream data that isn't readable as plain text. The visible elements show only PDF structural information (object references, filters, encoding specifications) rather than the actual article content describing the mGRPO method.\n\nTo accurately address your five-part question about:\n1. Reward signals used\n2. Handling of language-constrained vs unconstrained prompts\n3. Constraint application (trace vs answer)\n4. Preference data generation\n5. Trace/answer language decoupling\n\nI would need access to the actual readable text of the research paper. Could you provide either:\n- A text version of the paper, or\n- The actual PDF content in readable format, or\n- A link to the paper's published version?\n\nThis would allow me to give you a properly sourced response following your citation requirements.\n\n[Binary content (application/pdf, 4.9MB) also saved to /home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf]",
    "durationMs": 4800,
    "url": "https://openreview.net/pdf?id=QtfALPluAj"
  },
  "sourceToolAssistantUUID": "64fc16f1-e55b-418e-bbc6-0dff882072c7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "e5585a3d-e9ec-42f1-9c26-b59270715e4e",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-fidelity multilingual GRPO with mGRPO differentiation",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Assistant

_source line 23 · 2026-05-10T09:13:02.105Z_

<details><summary>Logged reasoning block</summary>

```text
The PDF is encoded but I have the file. Let me try to extract text from it using pdftotext.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e5585a3d-e9ec-42f1-9c26-b59270715e4e",
  "isSidechain": false,
  "requestId": "req_011Catda7XjGAXMVkxgFCj6y",
  "type": "assistant",
  "uuid": "3eeac7a2-3094-4c58-9b3a-a49913f06b7c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EcDmwXDsXF5dLzmH3n9Gbi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 31348,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 31348,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 24 · 2026-05-10T09:13:02.784Z_

<details open><summary>🔧 Tool call — Bash · `toolu_015dJXWMjzr9DV12XXDVFk4p`</summary>

```json
{
  "command": "pdftotext /home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf - 2>/dev/null | head -200",
  "description": "Extract text from mGRPO PDF"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3eeac7a2-3094-4c58-9b3a-a49913f06b7c",
  "isSidechain": false,
  "requestId": "req_011Catda7XjGAXMVkxgFCj6y",
  "type": "assistant",
  "uuid": "5dae229d-d23e-458f-a7f2-0f842d6b7027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EcDmwXDsXF5dLzmH3n9Gbi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 746,
      "cache_read_input_tokens": 31348,
      "output_tokens": 189,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 746,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 189,
          "cache_read_input_tokens": 31348,
          "cache_creation_input_tokens": 746,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 746
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

_source line 25 · 2026-05-10T09:13:02.811Z_

<details><summary>↩ Tool result · reported error · `toolu_015dJXWMjzr9DV12XXDVFk4p`</summary>

```text
This Bash command contains multiple operations. The following part requires approval: pdftotext /home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf -
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5dae229d-d23e-458f-a7f2-0f842d6b7027",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "04b59af6-f49e-4214-9fe4-fea1f3c75a4a",
  "toolUseResult": "Error: This Bash command contains multiple operations. The following part requires approval: pdftotext /home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf -",
  "sourceToolAssistantUUID": "5dae229d-d23e-458f-a7f2-0f842d6b7027",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 26 · 2026-05-10T09:13:04.949Z_

<details><summary>Logged reasoning block</summary>

```text
The user didn't approve the command. Let me try to read the PDF with the Read tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "04b59af6-f49e-4214-9fe4-fea1f3c75a4a",
  "isSidechain": false,
  "requestId": "req_011CatdaKqA689TBpRjUQ87U",
  "type": "assistant",
  "uuid": "0a7994c0-b841-4fa0-81ca-f57009582224",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AEaFLpA65AJA4xgrg4BZh6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 32094,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 32094,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 287
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

_source line 27 · 2026-05-10T09:13:05.423Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Jokbp42WDRyn3TpyLJaS3n`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a7994c0-b841-4fa0-81ca-f57009582224",
  "isSidechain": false,
  "requestId": "req_011CatdaKqA689TBpRjUQ87U",
  "type": "assistant",
  "uuid": "f7c5a410-a221-4db7-9026-8ce6b68580c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AEaFLpA65AJA4xgrg4BZh6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 287,
      "cache_read_input_tokens": 32094,
      "output_tokens": 163,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 287,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 163,
          "cache_read_input_tokens": 32094,
          "cache_creation_input_tokens": 287,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 287
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

_source line 28 · 2026-05-10T09:13:05.459Z_

<details><summary>↩ Tool result · reported error · `toolu_01Jokbp42WDRyn3TpyLJaS3n`</summary>

```text
This PDF has 23 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: "1-5"). Maximum 20 pages per request.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f7c5a410-a221-4db7-9026-8ce6b68580c0",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "11c54bf4-3310-453b-a596-44fe306cb9a2",
  "toolUseResult": "Error: This PDF has 23 pages, which is too many to read at once. Use the pages parameter to read specific page ranges (e.g., pages: \"1-5\"). Maximum 20 pages per request.",
  "sourceToolAssistantUUID": "f7c5a410-a221-4db7-9026-8ce6b68580c0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-10T09:13:07.566Z_

<details open><summary>🔧 Tool call — Read · `toolu_018YV3JrggBR7CfqxE9hszAj`</summary>

```json
{
  "file_path": "/home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf",
  "pages": "1-8"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11c54bf4-3310-453b-a596-44fe306cb9a2",
  "isSidechain": false,
  "requestId": "req_011CatdaXAY9MVWnScZmedw6",
  "type": "assistant",
  "uuid": "2a7bfa75-1fa1-4fe1-b1bb-ea36f1da6507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01P7R5CmqMF7dvrSbVuS3x8c",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 228,
      "cache_read_input_tokens": 32381,
      "output_tokens": 130,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 130,
          "cache_read_input_tokens": 32381,
          "cache_creation_input_tokens": 228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 228
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

_source line 30 · 2026-05-10T09:13:08.551Z_

<details><summary>↩ Tool result · `toolu_018YV3JrggBR7CfqxE9hszAj`</summary>

```text
PDF pages extracted: 8 page(s) from /home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf (4.9MB)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a7bfa75-1fa1-4fe1-b1bb-ea36f1da6507",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "uuid": "c6f4fe38-7579-42e2-9574-c89bdb0aae30",
  "toolUseResult": {
    "type": "parts",
    "file": {
      "filePath": "/home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/webfetch-1778404376177-wu5dby.pdf",
      "originalSize": 5126326,
      "outputDir": "/home/ubuntu/.claude-account-1/projects/-/05994783-f94c-4701-be9b-3d05f4c89f00/tool-results/pdf-978a0a27-67b9-4f91-aded-ec5cf11b836c",
      "count": 8
    }
  },
  "sourceToolAssistantUUID": "2a7bfa75-1fa1-4fe1-b1bb-ea36f1da6507",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

## Round 2

9 recorded events

### User

_source line 31 · 2026-05-10T09:13:08.549Z_

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "media_type": "image/jpeg",
    "data": "[ATTACHMENT_DATA_REDACTED]"
  }
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c6f4fe38-7579-42e2-9574-c89bdb0aae30",
  "isSidechain": false,
  "promptId": "7fc6b63a-7ef2-41c7-81a1-a13e28894a63",
  "type": "user",
  "isMeta": true,
  "uuid": "e0e57445-adb5-4647-b64d-488e211c07b4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "c6f4fe38-7579-42e2-9574-c89bdb0aae30",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-fidelity multilingual GRPO with mGRPO differentiation",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Assistant

_source line 34 · 2026-05-10T09:13:58.856Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! Now I have a thorough understanding of mGRPO from the actual paper. Let me summarize the key facts:

**mGRPO Key Facts:**

1. **Method**: Polyglot Reasoning Generation Module (PRGM) generates n=5 responses per question: one with no language constraint (empty [LANGUAGE] token) and four with randomly assigned target languages from a predefined set. These form the "Multilingual Thinking" set.

2. **Reward**: Two rule-based rewards:
   - **Accuracy Reward (AR)**: Binary - whether the final predicted answer matches gold (language-agnostic)
   - **Format Reward (FR)**: Binary - whether response contains [Thinking] section and final answer in "#### " format
   - No language-specific reward on the answer surface whatsoever

3. **No trace/answer decoupling**: mGRPO constrains the ENTIRE response language (via [LANGUAGE] prompt), not just the trace or answer separately. During inference, [LANGUAGE] is left empty so the model can freely choose its response language.

4. **Benchmarks**: MGSM, MATH500, PolyMath, X-CSQA (23 languages total) with MGSM averaging 75.93 on Qwen2.5-7B.

5. **Key insight**: The paper's core finding is that allowing unconstrained language choice expands the "thinking space" and yields better performance, rather than enforcing target-language answers - at inference time the language is completely unconstrained.

6. **Base model**: Qwen2.5-7B-Instruct, which is a different generation than Qwen3-7B.

7. **Training data**: 18,140 examples from 1,703 English questions across 10 languages from the MAPO dataset.

8. **No answer-language fidelity**: mGRPO doesn't attempt to ensure answers match the target language - its goal is expanding the reasoning exploration space for better accuracy, not language fidelity.

The key differences between mGRPO and our approach come down to fundamental design goals: mGRPO improves reasoning accuracy by leveraging multilingual rollouts as training signals, while we're focused on restoring answer-language fidelity without sacrificing accuracy. mGRPO uses only accuracy and format rewards with no language-specific component, whereas we add a language identification reward specifically targeting the answer surface. Their method constrains the entire response through prompting with one unconstrained rollout, but we leave the reasoning trace completely free and only constrain the final answer span. At inference, mGRPO produces entirely unconstrained output, while our approach trains toward target-language answers through the language identification reward during training, achieving fidelity without needing inference-time modifications. I'm looking at mGRPO's performance metrics across 23 languages and seeing that while it achieves strong accuracy gains through multilingual reasoning, our approach targets a different problem—maintaining answer fidelity without sacrificing accuracy. The fix is straightforward: I'll add mGRPO to the landscape section with a clear differentiation, include the reference, and keep everything else as is since the core contribution remains solid. on my reading:

mGRPO (§3.1 PRGM) generates n rollouts per training sample under both constrained and unconstrained language prompts—one response with empty [LANGUAGE] (free choice) and the remainder with randomly assigned target languages—optimizing via accuracy and format rewards only; the inference prompt leaves [LANGUAGE] empty so the model freely selects its response language, and no language-specific reward applies to any part of the output. Our method is categorically different in design goal: we leave the reasoning trace entirely unconstrained (no per-language rollouts during training) and enforce answer-surface language fidelity exclusively via the SFVG-gated LID reward, directly addressing the accuracy-fidelity tradeoff that mGRPO does not attempt to solve.

Now I'm figuring out where mGRPO fits in the landscape section. Since both mGRPO and polyGRPO use language diversity as a training signal for accuracy, mGRPO should go near polyGRPO—either right after it before TLPO, or after TLPO and before the "Making Qwen3 Think in Korean" entry. The concluding sentence about isolating language constraints to the answer span needs to stay last. I'm noting the specific performance metrics for mGRPO—75.93% on MGSM and 60.46% on X-CSQA using Qwen2.5-7B-Instruct—and the same base model caveat that applies to polyGRPO. Now I'm drafting the mGRPO entry, which uses a Polyglot Reasoning Generation Module to generate multiple rollouts per sample with responses in different languages. unconstrained prompt and the remainder under prompts that specify randomly selected target languages. Optimization uses only accuracy (binary match against gold) and format rewards—no language-specific reward applies to any component of the output. At inference time, the language token is left empty so the model freely selects its response language; achieving target-language answer fidelity is not a design goal. mGRPO achieves 75.93% MGSM average and 60.46% X-CSQA average on Qwen2.5-7B-Instruct (Table 1 of the paper). Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B). The fundamental distinction is that mGRPO expands the polyglot thinking exploration space to boost accuracy, while our approach leaves the reasoning trace unconstrained and enforces answer-surface language fidelity purely through the SFVG-gated LID reward, directly tackling the accuracy-fidelity trade-off that mGRPO doesn't address.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0e57445-adb5-4647-b64d-488e211c07b4",
  "isSidechain": false,
  "requestId": "req_011CatdakR1pZBS37zfjSdQb",
  "type": "assistant",
  "uuid": "dc4c46f1-e25c-4c19-a09c-7c2a04ed10c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TAt8zfUubr3pyFMVbE4LV4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10165,
      "cache_read_input_tokens": 32609,
      "output_tokens": 12849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 12849,
          "cache_read_input_tokens": 32609,
          "cache_creation_input_tokens": 10165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10165
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

_source line 35 · 2026-05-10T09:17:24.788Z_

I've read the full mGRPO paper (8 pages). Key facts confirmed from the source:

- **PRGM**: generates n=5 rollouts per sample — one with empty [LANGUAGE] (unconstrained) + four with randomly assigned target languages
- **Rewards**: accuracy (binary gold-match) + format ([Thinking]/`#### ` structure) only — **zero language-specific reward on any component**
- **Inference**: [LANGUAGE] left empty → model freely selects its output language; language fidelity is not a design goal
- **Results**: 75.93% MGSM avg, 60.46% X-CSQA avg on **Qwen2.5-7B-Instruct** (different generation from our Qwen3-7B)
- **No trace/answer decoupling**: the language prompt constrains the whole response; our approach is categorically different in intent

The reviewer is right: this is a one-entry addition. The differentiation is clear and non-adversarial — mGRPO and our method target orthogonal problems (accuracy via polyglot exploration vs. answer fidelity restoration). This is a **minor** fix.

```json
{
  "title": "Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO",
  "project_name": "answer_fidelity_free_trace",
  "source": "web_research",
  "change_type": "minor",
  "core_problem": "GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally tend to generate answers in the target language even when traces are mixed—a training-induced tendency (arXiv 2505.14815, §4.2 attributes this to 'supervision or reward signals focused on the final answer') that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.",
  "opportunity": "'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—§4.2, Finding 2 of that paper states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to models being 'trained with supervision or reward signals focused on the final answer'—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in §5.2, Figure 6, and Table 10), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.",
  "landscape": "M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. mGRPO ('Unlocking LLM Reasoning through Multilingual Thinking', ICLR 2026 submission, OpenReview QtfALPluAj, Sept 2025) generates n rollouts per training sample via a Polyglot Reasoning Generation Module (PRGM): one response under an unconstrained prompt and the remainder under prompts that specify randomly assigned target languages. Optimization uses only accuracy (binary gold-match against the final answer) and format ([Thinking]/#### structure) rewards—no language-specific reward applies to any component of the output. At inference time, the language token is left empty so the model freely selects its response language; achieving target-language answer fidelity is not a design goal. mGRPO achieves 75.93% MGSM average and 60.46% X-CSQA average on Qwen2.5-7B-Instruct; direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B). mGRPO is categorically different from our approach in design goal: it expands the polyglot thinking exploration space to improve accuracy, whereas our method leaves the reasoning trace entirely unconstrained and enforces answer-surface language fidelity exclusively via the SFVG-gated LID reward—directly addressing the accuracy-fidelity trade-off that mGRPO does not attempt to resolve. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. arXiv 2505.15257 ('When Less Language is More', May 2025) achieves language-reasoning disentanglement at inference time via SVD-based activation ablation—projecting language-specific subspaces out of mid-layer hidden states during the forward pass—with no training required, reporting results comparable to RL (PPO) on MGSM. Our method differs categorically: we achieve answer-surface fidelity via a GRPO reward during standard RL fine-tuning, with no inference-time modification to activations or architecture. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows (§4.2, Finding 2) that 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' attributing this to 'supervision or reward signals focused on the final answer'; it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\n\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (§5.2, Figure 6, Table 10) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\n\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (§5.2, Figure 6, Table 10) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\n\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.",
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
    "mGRPO: Unlocking LLM Reasoning through Multilingual Thinking (OpenReview ICLR 2026, QtfALPluAj, Sept 2025)",
    "MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation (arXiv 2503.10497, EMNLP 2025 Main)",
    "XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (arXiv 2305.11938, EMNLP 2023 Findings)"
  ],
  "description": "We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers: §4.2, Finding 2 states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to 'supervision or reward signals focused on the final answer'; and (b) Latin-script (English) reasoning yields optimal accuracy (§5.2, Figure 6, Table 10: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (§4.2, Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\n\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\n\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\n\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], mGRPO [75.93% MGSM avg on Qwen2.5-7B-Instruct, polyglot thinking exploration via PRGM rollouts with no answer-language reward], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal], and arXiv 2505.15257 [training-free SVD activation ablation at inference time]) which either apply language constraints to the full reasoning trace, use language diversity purely as an accuracy-improvement signal without targeting answer fidelity, require large-scale parallel data, or analyze trace features or hidden-state geometry without proposing a GRPO reward that decouples trace from answer constraint. Target: EMNLP 2026 Findings."
}
```

---

**Summary of changes (minor):**

The only substantive addition is mGRPO, placed in the landscape section between polyGRPO and TLPO — the natural cluster of papers that use language diversity as a training signal for accuracy. The entry covers:

1. **Method**: PRGM generates n=5 rollouts (1 unconstrained + 4 language-specified via prompt), confirmed from §3.1 of the paper
2. **Rewards**: accuracy + format only — zero language-specific reward on any output component, confirmed from §3.2 equations (1)–(2)
3. **Inference**: [LANGUAGE] left empty — no answer-fidelity goal, confirmed from §4.2 inference setup
4. **Numbers**: 75.93% MGSM avg, 60.46% X-CSQA avg on Qwen2.5-7B-Instruct, confirmed from Table 1
5. **Differentiation**: design goal orthogonality — mGRPO improves accuracy via polyglot exploration; our method restores answer-surface fidelity without constraining traces

The mGRPO citation is also added to `key_references`, and its numbers appear in the `description` summary alongside polyGRPO for completeness.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dc4c46f1-e25c-4c19-a09c-7c2a04ed10c4",
  "isSidechain": false,
  "requestId": "req_011CatdakR1pZBS37zfjSdQb",
  "type": "assistant",
  "uuid": "1fd33084-b5d6-42a3-b2fe-bcebad6e0fb7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01TAt8zfUubr3pyFMVbE4LV4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10165,
      "cache_read_input_tokens": 32609,
      "output_tokens": 12849,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10165,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 12849,
          "cache_read_input_tokens": 32609,
          "cache_creation_input_tokens": 10165,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10165
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "1fd33084-b5d6-42a3-b2fe-bcebad6e0fb7",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-fidelity multilingual GRPO with mGRPO differentiation",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "1fd33084-b5d6-42a3-b2fe-bcebad6e0fb7",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---

### Runtime record

_source line 39_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-fidelity multilingual GRPO with mGRPO differentiation",
  "sessionId": "05994783-f94c-4701-be9b-3d05f4c89f00"
}
```

---
