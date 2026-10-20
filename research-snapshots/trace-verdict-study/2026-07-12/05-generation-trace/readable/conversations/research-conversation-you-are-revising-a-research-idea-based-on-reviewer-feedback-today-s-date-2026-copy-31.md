# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af.jsonl`
- **Structured JSON:** [`953d497cbac2f7ac63fd.json`](../../sessions/95/953d497cbac2f7ac63fd.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T08:33:37.114Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T08:33:37.114Z",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\",\n  \"project_name\": \"answer_fidelity_free_trace\",\n  \"source\": \"web_research\",\n  \"core_problem\": \"GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally produce target-language final answers even when traces are mixed—a training-induced tendency (arXiv 2505.14815, Finding 2 attributes this to supervision signals focused on final answers) that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.\",\n  \"opportunity\": \"'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—Finding 2 of that paper explicitly states 'the final answers remain more aligned with the input language,' attributing this to training supervision focused on final answers—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in Table 10), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced tendency (documented as Finding 2 of arXiv 2505.14815) to produce target-language answers, which GRPO correctness training alone erodes.\",\n  \"landscape\": \"M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows final answers naturally align with input language in pretrained models (Finding 2); it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\\n\\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (Table 10) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\\n\\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (Table 10) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\\n\\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.\",\n  \"approach\": \"We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\\n\\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\\n\\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (Finding 2) explicitly states that 'the final answers remain more aligned with the input language' even when reasoning traces are mixed, and attributes this to training supervision signals focused on final answers—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\\n\\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\\n\\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\\n\\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\\n\\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\\n\\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per Table 10), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, Finding 2), which GRPO correctness training alone erodes.\\n\\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\\n\\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\\n\\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (Finding 2) that training supervision focused on final answers produces the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\\n\\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~105-175 H100-hours (4 ablation conditions × 2 seeds × ~12-15 H100-hours/run on Qwen3-7B with LoRA rank-16 on 4×H100 = ~96-120 H100-hours training; secondary Swahili experiment ~15 H100-hours; inference evals including MMLU-ProX 0-shot across 7 languages, XQuAD across 4 languages, pretrained-base cross-task eval, XCOPA, XStoryCloze ~20 H100-hours; sequential debugging adds ~20 H100-hours overhead; upper-end arithmetic: 120 + 15 + 20 + 20 = 175 H100-hours)\",\n      \"gpu_utilization\": \"Low (~40-50% effective); GPU idles waiting for researcher to iterate on SFVG reward code and analyze SFVG activation trajectories and correct-language rate logs per language\",\n      \"timeline\": \"6-10 weeks\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$315-525 at $3.00/H100-hr\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~147-182 H100-hours (agent queues ablation conditions in parallel; XQuAD inference ~2 H100-hours added to transfer eval suite; human approves experimental design at 4 key checkpoints: after first non-Latin-script run to verify SFVG Gate 2 activation, after vanilla GRPO baseline, after primary ablation completion, before secondary Swahili experiment)\",\n      \"gpu_utilization\": \"Moderate (~65-75% effective)\",\n      \"timeline\": \"4-6 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$150-300 (~1,500-3,000 agent turns for experiment design, SFVG log parsing, correct-language rate monitoring, LID-activation trajectory monitoring, MMLU-ProX and XQuAD inference and result analysis)\",\n      \"estimated_gpu_cost\": \"~$441-546\",\n      \"risk_note\": \"Key risk: SFVG Gate 2 (frame-presence check) must be verified to activate before Gate 3 (LID scoring). Human checkpoint after first non-Latin-script run is essential. SFVG gate activation rate and correct-language rate per language per step are the primary diagnostic signals, logged in TRL GRPOTrainer reward callback. Secondary risk: if model learns bare-numeral answers that satisfy Gate 1 but not Gate 2, the LID reward is perpetually inactive—detectable from flat Gate 2 activation curve. Correct-language rate log provides additional signal: if it is low for Latin-script languages under the universal prompt, the language-explicit ablation is promoted to primary.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~172-215 H100-hours. Grid is fixed at LoRA rank-16 throughout (rank sensitivity is scoped to manual-mode follow-up only; the original claim of sweeping rank ∈ {8,16,32} was removed as it would require 24-36 training runs totalling 288-540 H100-hours, far exceeding the 200 H100-hour budget). The constrained auto-mode grid is: (i) λ sweep {0.1, 0.2, 0.3, 0.5} for the answer-only SFVG condition × 1 seed (exploratory), = 4 runs × ~13 H100-hours = ~52 H100-hours; (ii) best λ re-run × 2 seeds for final reporting = 2 runs × ~13 H100-hours = ~26 H100-hours; (iii) 3 fixed-hyperparameter baselines (vanilla GRPO, whole-trace LC, PB-RLSVR) × 2 seeds = 6 runs × ~13 H100-hours = ~78 H100-hours; (iv) secondary Swahili experiment = ~15 H100-hours; (v) inference evals including pretrained-base cross-task checkpoint on XCOPA/XStoryCloze/MMLU-ProX/XQuAD = ~20 H100-hours. Total: ~191 H100-hours, fitting within the 200 H100-hour budget. The supplementary language-explicit prompt ablation (Gate 2 activation rate and correct-language rate comparison) is run as a short inference-only evaluation on the converged answer-only SFVG model (~3 H100-hours) and is included in the inference budget.\",\n      \"gpu_utilization\": \"Near-zero idle (~85-90% effective)\",\n      \"timeline\": \"5-10 days given 8+ H100s simultaneously\",\n      \"team\": \"0 (initial setup: ~2-3 hours to configure LoRA GRPOTrainer reward functions, SFVG gate logic with script-adaptive thresholds and correct-language rate logging, and evaluation harness including MMLU-ProX and XQuAD 0-shot pipelines)\",\n      \"claude_api_cost\": \"$300-600 (~3,000-6,000 agent turns for iterative design, SFVG log analysis, correct-language rate trajectory analysis, reward-hacking detection, cross-task transfer analysis, write-up drafting)\",\n      \"estimated_gpu_cost\": \"~$516-645\",\n      \"speed_bottleneck\": \"H100 cluster availability; fastText LID inference latency (mitigated by applying LID only to non-numeric answer content rather than the full trace, which is substantially shorter)\",\n      \"risk_note\": \"Primary risk: SFVG Gate 2 (frame-presence check) flat activation means model is producing bare numerals—detectable from Gate 2 activation curve, triggerable by adjusting system-prompt phrasing or adding format reward weight. Must be caught before training runs complete. Secondary risk: script-adaptive thresholds (8/5/3 chars for Latin/Thai/CJK) may require tuning; initial runs should log per-language gate failure breakdown and correct-language rate. Auto mode must trigger alert if Gate 2 activation drops below 50% for any language after step 200 (indicates model is not learning sentence frames), or if correct-language rate drops below 70% for any Latin-script language under the universal prompt (indicates cross-Latin-script confusion degrading LID reward signal). If the correct-language rate is systematically low for Latin-script languages under the universal prompt, the language-explicit prompt variant is promoted from supplementary to primary.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 Findings (ARR submission deadline May 25, 2026)\"\n  ],\n  \"key_references\": [\n    \"When Verifiable Rewards Switch the Language: Cross-lingual Collapse in Chain-of-Thought (arXiv 2506.05850, Jun 2025)\",\n    \"Language Mixing in Reasoning Language Models: Patterns, Impact, and Internal Causes (arXiv 2505.14815, May 2025)\",\n    \"Think Natively: Unlocking Multilingual Reasoning with Consistency-Enhanced Reinforcement Learning / M-Thinker (arXiv 2510.07300, Oct 2025)\",\n    \"Why Do Multilingual Reasoning Gaps Emerge in Reasoning Language Models? (arXiv 2510.27269, Oct 2025)\",\n    \"Long Chain-of-Thought Reasoning Across Languages (arXiv 2508.14828, Aug 2025)\",\n    \"Making Qwen3 Think in Korean with Reinforcement Learning (arXiv 2508.10355, Aug 2025)\",\n    \"Aligning Multilingual Reasoning with Verifiable Semantics from a High-Resource Expert Model / PB-RLSVR (arXiv 2509.25543, Sep 2025)\",\n    \"Pushing on Multilingual Reasoning Models with Language-Mixed Chain-of-Thought (arXiv 2510.04230, Oct 2025)\",\n    \"ExpLang: Improved Exploration and Exploitation in LLM Reasoning with On-Policy Thinking Language Selection (arXiv 2602.21887, Feb 2026)\",\n    \"Self-Improving Multilingual Long Reasoning via Translation-Reasoning Integrated Training / TRIT (arXiv 2602.05940, Feb 2026)\",\n    \"Language as a Latent Variable for Reasoning Optimization / polyGRPO (arXiv 2604.21593, Apr 2026)\",\n    \"TLPO: Token-Level Policy Optimization for Mitigating Language Confusion in Large Language Models (arXiv 2604.26553, Apr 2026)\",\n    \"What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features (arXiv 2604.04720, Apr 2026)\",\n    \"ReasonXL: Shifting LLM Reasoning Language Without Sacrificing Performance (arXiv 2604.12378, Apr 2026)\",\n    \"MMLU-ProX: A Multilingual Benchmark for Advanced Large Language Model Evaluation (arXiv 2503.10497, EMNLP 2025 Main)\",\n    \"XTREME-UP: A User-Centric Scarce-Data Benchmark for Under-Represented Languages (arXiv 2305.11938, EMNLP 2023 Findings)\"\n  ],\n  \"description\": \"We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers, which naturally align with input language as explicitly stated in Finding 2 ('the final answers remain more aligned with the input language'), with this alignment attributed to training supervision signals focused on final answers; and (b) Latin-script (English) reasoning yields optimal accuracy (Table 10: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\\n\\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\\n\\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\\n\\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, and ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features without proposing a reward design that decouples trace from answer constraint. Target: EMNLP 2026 Findings.\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"CARRY-OVER (Round 5, unresolved in Round 6) — The 2505.14815 'Finding 2' exact quote is still unverified. The proposal uses 'arXiv 2505.14815 (Finding 2) explicitly states \\\"the final answers remain more aligned with the input language\\\"' in three separate sections of the paper (opportunity, approach, description), presenting it as a verbatim quote with a named finding number. The abstract of 2505.14815 establishes that language mixing is concentrated in reasoning traces and that script-constrained decoding improves accuracy, but does NOT explicitly state final-answer alignment in the abstract. The Round 5 reviewer asked for either 'the precise location in the paper where this finding appears, or hedge the framing.' The Round 6 generator added 'Finding 2' as a location label but maintained the exact-quote framing. If 2505.14815 does not have a labeled 'Finding 2' with this verbatim content, every instance of this claim across the paper will draw reviewer rejection. The generator must either (a) verify the full paper contains a 'Finding 2' with this text and add the section/table reference alongside the quote, or (b) reframe as 'consistent with 2505.14815's finding that language mixing concentrates in intermediate steps while final answers show less mixing, we infer that...' — i.e., an inference from the paper's documented findings rather than a direct quotation of a named finding.\", \"MISSING RELEVANT PRIOR WORK — arXiv 2505.15257 ('When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners', May 2025) is absent from the landscape section despite sharing the 'language-reasoning disentanglement' framing verbatim. This paper is training-free (inference-time activation ablation via SVD) and therefore categorically different from the proposed reward-design approach — but EMNLP Multilingualism reviewers will know it and expect a citation. The generator should add it to the landscape as an inference-time contrast: '2505.15257 addresses language-reasoning disentanglement at inference time via activation ablation, requiring no training; our method achieves answer-surface fidelity via a GRPO reward that requires no architectural modification or inference overhead.' One sentence is sufficient.\"]\nFeedback: The paper has resolved all Round 1–5 issues cleanly and is genuinely one targeted revision away from Findings-ready. Two fixes remain, both requiring no new experiments. (1) Resolve the 2505.14815 Finding 2 attribution: read the full paper at https://arxiv.org/abs/2505.14815 and either confirm that 'Finding 2' exists verbatim with this text and add the section reference (e.g., '§3.2, Finding 2'), or replace the exact-quote framing with an inference ('consistent with 2505.14815's documented finding that language mixing concentrates in intermediate reasoning steps, we infer that final-answer language alignment is more robust — a signal that GRPO's language-agnostic correctness reward erodes'). This framing is scientifically accurate and does not weaken the paper's argument. (2) Add one sentence about arXiv 2505.15257 to the landscape section under 'Language-Mixed CoT' or as a standalone entry: '2505.15257 achieves language-reasoning disentanglement at inference time via SVD-based activation ablation with no training overhead; our method differs by achieving answer-surface fidelity via a GRPO reward applicable during standard RL fine-tuning without inference-time modification.' Both fixes are mechanical — no new training, no new experiments.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T08:33:37.119Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T08:33:37.119Z",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-10T08:33:37.159Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO",
  "project_name": "answer_fidelity_free_trace",
  "source": "web_research",
  "core_problem": "GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally produce target-language final answers even when traces are mixed—a training-induced tendency (arXiv 2505.14815, Finding 2 attributes this to supervision signals focused on final answers) that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.",
  "opportunity": "'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—Finding 2 of that paper explicitly states 'the final answers remain more aligned with the input language,' attributing this to training supervision focused on final answers—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in Table 10), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced tendency (documented as Finding 2 of arXiv 2505.14815) to produce target-language answers, which GRPO correctness training alone erodes.",
  "landscape": "M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows final answers naturally align with input language in pretrained models (Finding 2); it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\n\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (Table 10) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\n\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (Table 10) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\n\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.",
  "approach": "We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\n\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\n\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (Finding 2) explicitly states that 'the final answers remain more aligned with the input language' even when reasoning traces are mixed, and attributes this to training supervision signals focused on final answers—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\n\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\n\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\n\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\n\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\n\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per Table 10), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, Finding 2), which GRPO correctness training alone erodes.\n\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\n\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\n\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (Finding 2) that training supervision focused on final answers produces the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\n\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.",
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
  "description": "We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers, which naturally align with input language as explicitly stated in Finding 2 ('the final answers remain more aligned with the input language'), with this alignment attributed to training supervision signals focused on final answers; and (b) Latin-script (English) reasoning yields optimal accuracy (Table 10: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\n\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\n\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\n\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, and ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features without proposing a reward design that decouples trace from answer constraint. Target: EMNLP 2026 Findings."
}

## Reviewer feedback (round 6)
Issues: ["CARRY-OVER (Round 5, unresolved in Round 6) — The 2505.14815 'Finding 2' exact quote is still unverified. The proposal uses 'arXiv 2505.14815 (Finding 2) explicitly states \"the final answers remain more aligned with the input language\"' in three separate sections of the paper (opportunity, approach, description), presenting it as a verbatim quote with a named finding number. The abstract of 2505.14815 establishes that language mixing is concentrated in reasoning traces and that script-constrained decoding improves accuracy, but does NOT explicitly state final-answer alignment in the abstract. The Round 5 reviewer asked for either 'the precise location in the paper where this finding appears, or hedge the framing.' The Round 6 generator added 'Finding 2' as a location label but maintained the exact-quote framing. If 2505.14815 does not have a labeled 'Finding 2' with this verbatim content, every instance of this claim across the paper will draw reviewer rejection. The generator must either (a) verify the full paper contains a 'Finding 2' with this text and add the section/table reference alongside the quote, or (b) reframe as 'consistent with 2505.14815's finding that language mixing concentrates in intermediate steps while final answers show less mixing, we infer that...' — i.e., an inference from the paper's documented findings rather than a direct quotation of a named finding.", "MISSING RELEVANT PRIOR WORK — arXiv 2505.15257 ('When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners', May 2025) is absent from the landscape section despite sharing the 'language-reasoning disentanglement' framing verbatim. This paper is training-free (inference-time activation ablation via SVD) and therefore categorically different from the proposed reward-design approach — but EMNLP Multilingualism reviewers will know it and expect a citation. The generator should add it to the landscape as an inference-time contrast: '2505.15257 addresses language-reasoning disentanglement at inference time via activation ablation, requiring no training; our method achieves answer-surface fidelity via a GRPO reward that requires no architectural modification or inference overhead.' One sentence is sufficient."]
Feedback: The paper has resolved all Round 1–5 issues cleanly and is genuinely one targeted revision away from Findings-ready. Two fixes remain, both requiring no new experiments. (1) Resolve the 2505.14815 Finding 2 attribution: read the full paper at https://arxiv.org/abs/2505.14815 and either confirm that 'Finding 2' exists verbatim with this text and add the section reference (e.g., '§3.2, Finding 2'), or replace the exact-quote framing with an inference ('consistent with 2505.14815's documented finding that language mixing concentrates in intermediate reasoning steps, we infer that final-answer language alignment is more robust — a signal that GRPO's language-agnostic correctness reward erodes'). This framing is scientifically accurate and does not weaken the paper's argument. (2) Add one sentence about arXiv 2505.15257 to the landscape section under 'Language-Mixed CoT' or as a standalone entry: '2505.15257 achieves language-reasoning disentanglement at inference time via SVD-based activation ablation with no training overhead; our method differs by achieving answer-surface fidelity via a GRPO reward applicable during standard RL fine-tuning without inference-time modification.' Both fixes are mechanical — no new training, no new experiments.

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
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.5，没有明显改善。

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
  "promptId": "576e5cea-536f-47bf-a211-acc677686f48",
  "type": "user",
  "uuid": "893be954-f437-4724-b76f-236a101680cc",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T08:33:37.156Z_

```json
{
  "parentUuid": "893be954-f437-4724-b76f-236a101680cc",
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
  "uuid": "df2adecc-a12b-49ae-9400-01362b0ee840",
  "timestamp": "2026-05-10T08:33:37.156Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T08:33:37.156Z_

```json
{
  "parentUuid": "df2adecc-a12b-49ae-9400-01362b0ee840",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "b20eabf6-09ba-4395-9891-1c8b2102df86",
  "timestamp": "2026-05-10T08:33:37.156Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
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
  "leafUuid": "b20eabf6-09ba-4395-9891-1c8b2102df86",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-only GRPO reward for multilingual fidelity",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Assistant

_source line 8 · 2026-05-10T08:33:54.249Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before proceeding.

The paper has been through 6 rounds of revision with stagnating scores (3.5/5 average for the last 3 rounds). The reviewer feedback for Round 6 has two specific issues:

1. **Unverified "Finding 2" quote from arXiv 2505.14815** - The paper uses a verbatim quote claiming "Finding 2 explicitly states 'the final answers remain more aligned with the input language'" but this hasn't been verified. I need to actually read the paper.


2. **Missing prior work arXiv 2505.15257** - "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners" is absent from the landscape.

Both are mechanical fixes requiring no new experiments. But with three consecutive rounds stuck at 3.5/5, I'm wondering if there's something more fundamental I'm missing. The core contribution—that GRPO training causes cross-lingual collapse and applying language consistency constraints only to final answers rather than reasoning traces mitigates this—seems sound and grounded in the cited work. I should verify these citations and fill the gap in related work, but I'm also questioning whether the paper's framing or experimental design needs deeper reconsideration to break through this plateau. I need to fetch both papers to verify the claims and understand the positioning—let me use the Agent tool to pull arXiv 2505.14815 and 2505.15257 in parallel so I can check the "Finding 2" existence and see how the prior work landscape should be framed.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b20eabf6-09ba-4395-9891-1c8b2102df86",
  "isSidechain": false,
  "requestId": "req_011CataZwtwkXXN1pHmfYEYJ",
  "type": "assistant",
  "uuid": "c085c4e6-82fd-4e69-ab37-1269e183aa3e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015eJvbU2UX9jFSyL69oyyND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16184,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1222,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16184
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

_source line 9 · 2026-05-10T08:33:54.273Z_

I'll address both issues systematically. First, let me fetch both papers in parallel — I need to verify the "Finding 2" claim in arXiv 2505.14815 and read arXiv 2505.15257 to draft the landscape addition.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c085c4e6-82fd-4e69-ab37-1269e183aa3e",
  "isSidechain": false,
  "requestId": "req_011CataZwtwkXXN1pHmfYEYJ",
  "type": "assistant",
  "uuid": "458627b7-3d24-4fcc-9227-350ae7d94a04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015eJvbU2UX9jFSyL69oyyND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16184,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1222,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16184
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

_source line 10 · 2026-05-10T08:33:57.767Z_

<details open><summary>🔧 Tool call — Agent · `toolu_015zGdvC8ZZqFF2pLvGrXSZU`</summary>

```json
{
  "description": "Fetch arXiv 2505.14815 full paper",
  "prompt": "Fetch the full content of https://arxiv.org/abs/2505.14815 and also try https://arxiv.org/pdf/2505.14815 (the PDF page). I need to find:\n1. Whether the paper has explicitly numbered \"Findings\" (Finding 1, Finding 2, etc.)\n2. The exact text of any Finding related to \"final answers remain more aligned with the input language\" or final-answer language alignment\n3. The section number and page where this finding appears\n4. What the abstract and main findings sections say about language mixing in intermediate steps vs. final answers\n5. Any mention of \"training supervision signals focused on final answers\"\n\nPlease return the relevant verbatim text from the paper, especially any numbered findings. This is critical for verifying a citation claim.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "458627b7-3d24-4fcc-9227-350ae7d94a04",
  "isSidechain": false,
  "requestId": "req_011CataZwtwkXXN1pHmfYEYJ",
  "type": "assistant",
  "uuid": "5481cd70-f409-4736-b0f3-f7b7571c7f08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015eJvbU2UX9jFSyL69oyyND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16184,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1222,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16184
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

_source line 11 · 2026-05-10T08:33:59.867Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012s64arLghCkzguRDP1UKGs`</summary>

```json
{
  "description": "Fetch arXiv 2505.15257 abstract and methods",
  "prompt": "Fetch the content of https://arxiv.org/abs/2505.15257 — the paper titled \"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners\" (May 2025). I need:\n1. The abstract in full\n2. The core method — specifically whether it's training-free / inference-time\n3. Whether it uses SVD-based activation ablation (as claimed in reviewer feedback)\n4. What \"language-reasoning disentanglement\" means in this paper's context\n5. Key results (which languages, which benchmarks)\n6. How it differs from reward-based training approaches\n\nPlease return verbatim abstract and a summary of the method section.",
  "subagent_type": "general-purpose"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5481cd70-f409-4736-b0f3-f7b7571c7f08",
  "isSidechain": false,
  "requestId": "req_011CataZwtwkXXN1pHmfYEYJ",
  "type": "assistant",
  "uuid": "18e0ed34-bd22-46b0-beed-617c848e8671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_015eJvbU2UX9jFSyL69oyyND",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 16184,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1222,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16184,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1222,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 16184,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16184
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

_source line 12 · 2026-05-10T08:34:45.767Z_

<details><summary>↩ Tool result · `toolu_012s64arLghCkzguRDP1UKGs`</summary>

```text
Here is a complete report on the paper.

---

## Paper: "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners"
**arXiv:** 2505.15257 | **Submitted:** May 21, 2025 | **Authors:** Weixiang Zhao et al.

---

### 1. Full Abstract (verbatim)

"Multilingual reasoning remains a significant challenge for large language models (LLMs), with performance disproportionately favoring high-resource languages. Drawing inspiration from cognitive neuroscience, which suggests that human reasoning functions largely independently of language processing, we hypothesize that LLMs similarly encode reasoning and language as separable components that can be disentangled to enhance multilingual reasoning. To evaluate this, we perform a causal intervention by ablating language-specific representations at inference time. Experiments on 10 open-weight LLMs spanning 11 typologically diverse languages show that this language-specific ablation consistently boosts multilingual reasoning performance. Layer-wise analyses further confirm that language and reasoning representations can be effectively disentangled throughout the model, yielding improved multilingual reasoning capabilities, while preserving top-layer language features remains essential for maintaining linguistic fidelity. Compared to post-training methods such as supervised fine-tuning or reinforcement learning, our training-free language-reasoning disentanglement achieves comparable or superior results with minimal computational overhead. These findings shed light on the internal mechanisms underlying multilingual reasoning in LLMs and suggest a lightweight and interpretable strategy for improving cross-lingual generalization."

---

### 2. Core Method — Training-Free / Inference-Time

Yes, it is explicitly **training-free and inference-time only**. No weight updates or fine-tuning are performed. The intervention is applied during the forward pass.

**Mechanically, it works in two steps:**

**Step 1 — SVD-based subspace identification.** The authors compute mean hidden representations for each language at every layer, then apply **Singular Value Decomposition (SVD)** to decompose the multilingual latent space into two orthogonal components: a *language-specific subspace* and a *language-agnostic (reasoning) subspace*. So yes, SVD-based activation ablation is confirmed — the reviewer feedback was accurate.

**Step 2 — Projection-based ablation.** At inference time, for any hidden state **h** at mid-layers, they apply:

> **h_hat = h − λ · Mₛᵀ Mₛ h**

where **Mₛ** is the language-specific subspace basis (from SVD) and **λ** controls ablation strength. This projects out the language-specific component while preserving the language-agnostic reasoning signal. Critically, **top-layer language features are re-injected / preserved** to maintain linguistic fidelity in the output (so the model still produces the correct target language).

---

### 3. SVD-Based Activation Ablation — Confirmed

Yes. The method is explicitly SVD-based. SVD is applied to the matrix of per-language mean representations to extract the low-dimensional language-specific subspace, which is then removed from hidden activations via orthogonal projection. This is the core technical mechanism.

---

### 4. What "Language-Reasoning Disentanglement" Means Here

The paper's thesis — motivated by cognitive neuroscience — is that LLMs, like humans, encode **reasoning** and **language surface form** as separable internal structures. "Language-reasoning disentanglement" refers to surgically removing the language-identifying signal (the part of the hidden state that encodes *which* language is being used) from mid-layer activations, so that the model's reasoning machinery operates on a more language-neutral representation. The hypothesis is that cross-lingual reasoning is bottlenecked by language-specific features contaminating the reasoning subspace, and stripping those features lets the model generalize its reasoning capability across languages.

---

### 5. Key Results

**Benchmarks:**
- **MGSM** — multilingual mathematical reasoning (primary)
- **XWinograd** — commonsense inference
- **M-MMLU** — knowledge-intensive question answering

**Languages (11 total across resource levels):**
- High-resource: English, Spanish, French, German, Chinese, Japanese, Russian
- Mid-resource: Thai, Telugu
- Low-resource: Bengali, Swahili

**Models:** 10 open-weight LLMs tested (specific model list in paper body).

**Representative numbers on MGSM (Qwen-2.5-3B-Instruct):**
| Method | Accuracy |
|---|---|
| Baseline | 55.78% |
| **LRD (this paper)** | **59.02%** |
| Supervised Fine-tuning | 49.09% |
| Reinforcement Learning (PPO) | 60.33% |

The method consistently boosts performance across all 11 languages and is particularly beneficial for low- and mid-resource languages where the baseline is weakest.

---

### 6. How It Differs from Reward-Based Training Approaches

| Dimension | This paper (LRD) | Reward-based / RL / SFT |
|---|---|---|
| Training required | None | Yes (RL with PPO, or SFT on labeled data) |
| Computational cost | Minimal (matrix projection at inference) | High (policy gradient updates, reward modeling) |
| Model weights modified | No | Yes |
| Interpretability | High — directly targets identified subspace | Low — emergent from reward signal |
| Performance vs. SFT | Superior (59.02% vs. 49.09%) | SFT underperforms |
| Performance vs. RL (PPO) | Comparable (59.02% vs. 60.33%) | RL slightly higher but at large training cost |

The key claim is that **comparable multilingual reasoning gains can be achieved without any training**, purely by understanding and manipulating the internal geometry of representations — making the approach both more practical (no data/compute for training) and more interpretable (the subspace being ablated has a clear semantic meaning).

agentId: a56d7cc782c03b222 (use SendMessage with to: 'a56d7cc782c03b222' to continue this agent)
&lt;usage>total_tokens: 12974
tool_uses: 3
duration_ms: 45895&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "18e0ed34-bd22-46b0-beed-617c848e8671",
  "isSidechain": false,
  "promptId": "576e5cea-536f-47bf-a211-acc677686f48",
  "type": "user",
  "uuid": "376c871d-c0cd-4b79-b385-22075ecf17e6",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Fetch the content of https://arxiv.org/abs/2505.15257 — the paper titled \"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners\" (May 2025). I need:\n1. The abstract in full\n2. The core method — specifically whether it's training-free / inference-time\n3. Whether it uses SVD-based activation ablation (as claimed in reviewer feedback)\n4. What \"language-reasoning disentanglement\" means in this paper's context\n5. Key results (which languages, which benchmarks)\n6. How it differs from reward-based training approaches\n\nPlease return verbatim abstract and a summary of the method section.",
    "agentId": "a56d7cc782c03b222",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is a complete report on the paper.\n\n---\n\n## Paper: \"When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners\"\n**arXiv:** 2505.15257 | **Submitted:** May 21, 2025 | **Authors:** Weixiang Zhao et al.\n\n---\n\n### 1. Full Abstract (verbatim)\n\n\"Multilingual reasoning remains a significant challenge for large language models (LLMs), with performance disproportionately favoring high-resource languages. Drawing inspiration from cognitive neuroscience, which suggests that human reasoning functions largely independently of language processing, we hypothesize that LLMs similarly encode reasoning and language as separable components that can be disentangled to enhance multilingual reasoning. To evaluate this, we perform a causal intervention by ablating language-specific representations at inference time. Experiments on 10 open-weight LLMs spanning 11 typologically diverse languages show that this language-specific ablation consistently boosts multilingual reasoning performance. Layer-wise analyses further confirm that language and reasoning representations can be effectively disentangled throughout the model, yielding improved multilingual reasoning capabilities, while preserving top-layer language features remains essential for maintaining linguistic fidelity. Compared to post-training methods such as supervised fine-tuning or reinforcement learning, our training-free language-reasoning disentanglement achieves comparable or superior results with minimal computational overhead. These findings shed light on the internal mechanisms underlying multilingual reasoning in LLMs and suggest a lightweight and interpretable strategy for improving cross-lingual generalization.\"\n\n---\n\n### 2. Core Method — Training-Free / Inference-Time\n\nYes, it is explicitly **training-free and inference-time only**. No weight updates or fine-tuning are performed. The intervention is applied during the forward pass.\n\n**Mechanically, it works in two steps:**\n\n**Step 1 — SVD-based subspace identification.** The authors compute mean hidden representations for each language at every layer, then apply **Singular Value Decomposition (SVD)** to decompose the multilingual latent space into two orthogonal components: a *language-specific subspace* and a *language-agnostic (reasoning) subspace*. So yes, SVD-based activation ablation is confirmed — the reviewer feedback was accurate.\n\n**Step 2 — Projection-based ablation.** At inference time, for any hidden state **h** at mid-layers, they apply:\n\n> **h_hat = h − λ · Mₛᵀ Mₛ h**\n\nwhere **Mₛ** is the language-specific subspace basis (from SVD) and **λ** controls ablation strength. This projects out the language-specific component while preserving the language-agnostic reasoning signal. Critically, **top-layer language features are re-injected / preserved** to maintain linguistic fidelity in the output (so the model still produces the correct target language).\n\n---\n\n### 3. SVD-Based Activation Ablation — Confirmed\n\nYes. The method is explicitly SVD-based. SVD is applied to the matrix of per-language mean representations to extract the low-dimensional language-specific subspace, which is then removed from hidden activations via orthogonal projection. This is the core technical mechanism.\n\n---\n\n### 4. What \"Language-Reasoning Disentanglement\" Means Here\n\nThe paper's thesis — motivated by cognitive neuroscience — is that LLMs, like humans, encode **reasoning** and **language surface form** as separable internal structures. \"Language-reasoning disentanglement\" refers to surgically removing the language-identifying signal (the part of the hidden state that encodes *which* language is being used) from mid-layer activations, so that the model's reasoning machinery operates on a more language-neutral representation. The hypothesis is that cross-lingual reasoning is bottlenecked by language-specific features contaminating the reasoning subspace, and stripping those features lets the model generalize its reasoning capability across languages.\n\n---\n\n### 5. Key Results\n\n**Benchmarks:**\n- **MGSM** — multilingual mathematical reasoning (primary)\n- **XWinograd** — commonsense inference\n- **M-MMLU** — knowledge-intensive question answering\n\n**Languages (11 total across resource levels):**\n- High-resource: English, Spanish, French, German, Chinese, Japanese, Russian\n- Mid-resource: Thai, Telugu\n- Low-resource: Bengali, Swahili\n\n**Models:** 10 open-weight LLMs tested (specific model list in paper body).\n\n**Representative numbers on MGSM (Qwen-2.5-3B-Instruct):**\n| Method | Accuracy |\n|---|---|\n| Baseline | 55.78% |\n| **LRD (this paper)** | **59.02%** |\n| Supervised Fine-tuning | 49.09% |\n| Reinforcement Learning (PPO) | 60.33% |\n\nThe method consistently boosts performance across all 11 languages and is particularly beneficial for low- and mid-resource languages where the baseline is weakest.\n\n---\n\n### 6. How It Differs from Reward-Based Training Approaches\n\n| Dimension | This paper (LRD) | Reward-based / RL / SFT |\n|---|---|---|\n| Training required | None | Yes (RL with PPO, or SFT on labeled data) |\n| Computational cost | Minimal (matrix projection at inference) | High (policy gradient updates, reward modeling) |\n| Model weights modified | No | Yes |\n| Interpretability | High — directly targets identified subspace | Low — emergent from reward signal |\n| Performance vs. SFT | Superior (59.02% vs. 49.09%) | SFT underperforms |\n| Performance vs. RL (PPO) | Comparable (59.02% vs. 60.33%) | RL slightly higher but at large training cost |\n\nThe key claim is that **comparable multilingual reasoning gains can be achieved without any training**, purely by understanding and manipulating the internal geometry of representations — making the approach both more practical (no data/compute for training) and more interpretable (the subspace being ablated has a clear semantic meaning)."
      }
    ],
    "totalDurationMs": 45895,
    "totalTokens": 12974,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 698,
      "cache_read_input_tokens": 10833,
      "output_tokens": 1442,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 698
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1442,
          "cache_read_input_tokens": 10833,
          "cache_creation_input_tokens": 698,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 698,
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
  "sourceToolAssistantUUID": "18e0ed34-bd22-46b0-beed-617c848e8671",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T08:35:33.950Z_

<details><summary>↩ Tool result · `toolu_015zGdvC8ZZqFF2pLvGrXSZU`</summary>

```text
I now have consistent, well-corroborated results across four separate fetches (abstract page, PDF page, HuggingFace, and HTML version). Here is the full verified report:

---

## Findings from arXiv:2505.14815 — "Language Mixing in Reasoning Language Models"

### Verification status

The paper's numbered findings and surrounding text were confirmed consistently across four independent fetches (arxiv.org/abs, arxiv.org/pdf, huggingface.co/papers, and arxiv.org/html). The HTML version (arxiv.org/html/2505.14815v1) is the most reliable source.

---

### 1. Yes — the paper has explicitly numbered Findings

The paper contains exactly **8 explicitly numbered Findings**, formatted as bold headers (e.g., "Finding 2") within Section 4.

---

### 2. The exact Finding related to final-answer language alignment

**Finding 2** (verbatim):
> "RLMs mix languages during reasoning, yet tend to generate answers in the input language."

---

### 3. Section and location of Finding 2

Finding 2 appears in **Section 4.2 (Results)** within Section 4 ("Language Mixing Patterns"). The paper does not use traditional page numbers in its HTML rendering; it is within the first major results subsection of the paper.

---

### 4. Abstract + Section 4 on intermediate steps vs. final answers

**Abstract** (verbatim):
> "Reasoning language models (RLMs) excel at complex tasks by leveraging a chain-of-thought process to generate structured intermediate steps. However, language mixing, i.e., reasoning steps containing tokens from languages other than the prompt, has been observed in their outputs and shown to affect performance, though its impact remains debated. We present the first systematic study of language mixing in RLMs, examining its patterns, impact, and internal causes across 15 languages, 7 task difficulty levels, and 18 subject areas, and show how all three factors influence language mixing. Moreover, we demonstrate that the choice of reasoning language significantly affects performance: forcing models to reason in Latin or Han scripts via constrained decoding notably improves accuracy. Finally, we show that the script composition of reasoning traces closely aligns with that of the model's internal representations, indicating that language mixing reflects latent processing preferences in RLMs. Our findings provide actionable insights for optimizing multilingual reasoning and open new directions for controlling reasoning languages to build more interpretable and adaptable RLMs."

**Section 4.2 paragraph following Finding 2** (verbatim):
> "While reasoning traces exhibit language mixing, the final answers remain more aligned with the input language. This indicates that language mixing occurs primarily in the intermediate reasoning phase, not in the final output. This behavior is unsurprising, as reasoning models are generally trained with supervision or reward signals focused on the final answer, encouraging alignment with the input language, while leaving the reasoning steps unconstrained. As a result, models are free to mix languages during reasoning if it helps them reach a correct answer more effectively."

---

### 5. Exact sentence on "training supervision signals focused on final answers"

(Verbatim, from Section 4.2):
> "This behavior is unsurprising, as reasoning models are generally trained with supervision or reward signals focused on the final answer, encouraging alignment with the input language, while leaving the reasoning steps unconstrained."

Note: the paper uses the phrase **"supervision or reward signals focused on the final answer"** — not "training supervision signals focused on final answers" verbatim, though the meaning is identical.

---

### All 8 Findings (verbatim)

| # | Text |
|---|------|
| Finding 1 | "Language mixing is most prevalent when the input is neither English nor Chinese." |
| Finding 2 | "RLMs mix languages during reasoning, yet tend to generate answers in the input language." |
| Finding 3 | "The degree of language mixing increases with task difficulty." |
| Finding 4 | "Language mixing is more pronounced in STEM subjects." |
| Finding 5 | "Distillation amplifies language mixing." |
| Finding 6 | "Non-Latin/Han-script languages benefit significantly from reasoning in Latin or Han scripts." |
| Finding 7 | "Latin and Han-script languages favor their native script." |
| Finding 8 | "Language mixing reflects the internal processing patterns of RLMs, as reasoning traces mirror the model's preferred scripts." |

---

### Citation verification summary

The claim that "final answers remain more aligned with the input language" is **directly supported** by the paper — it appears as the explanatory text immediately following Finding 2 in Section 4.2. The phrase "training supervision signals focused on final answers" is a close paraphrase of the verbatim text: *"supervision or reward signals focused on the final answer."* The paper does explicitly make both claims, but the exact phrasing in the paper uses "supervision or reward signals," not "training supervision signals."

agentId: ab25efebf6032de6e (use SendMessage with to: 'ab25efebf6032de6e' to continue this agent)
&lt;usage>total_tokens: 16501
tool_uses: 10
duration_ms: 96175&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5481cd70-f409-4736-b0f3-f7b7571c7f08",
  "isSidechain": false,
  "promptId": "576e5cea-536f-47bf-a211-acc677686f48",
  "type": "user",
  "uuid": "5738e851-6d66-409f-994b-3aa9643b740b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Fetch the full content of https://arxiv.org/abs/2505.14815 and also try https://arxiv.org/pdf/2505.14815 (the PDF page). I need to find:\n1. Whether the paper has explicitly numbered \"Findings\" (Finding 1, Finding 2, etc.)\n2. The exact text of any Finding related to \"final answers remain more aligned with the input language\" or final-answer language alignment\n3. The section number and page where this finding appears\n4. What the abstract and main findings sections say about language mixing in intermediate steps vs. final answers\n5. Any mention of \"training supervision signals focused on final answers\"\n\nPlease return the relevant verbatim text from the paper, especially any numbered findings. This is critical for verifying a citation claim.",
    "agentId": "ab25efebf6032de6e",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have consistent, well-corroborated results across four separate fetches (abstract page, PDF page, HuggingFace, and HTML version). Here is the full verified report:\n\n---\n\n## Findings from arXiv:2505.14815 — \"Language Mixing in Reasoning Language Models\"\n\n### Verification status\n\nThe paper's numbered findings and surrounding text were confirmed consistently across four independent fetches (arxiv.org/abs, arxiv.org/pdf, huggingface.co/papers, and arxiv.org/html). The HTML version (arxiv.org/html/2505.14815v1) is the most reliable source.\n\n---\n\n### 1. Yes — the paper has explicitly numbered Findings\n\nThe paper contains exactly **8 explicitly numbered Findings**, formatted as bold headers (e.g., \"Finding 2\") within Section 4.\n\n---\n\n### 2. The exact Finding related to final-answer language alignment\n\n**Finding 2** (verbatim):\n> \"RLMs mix languages during reasoning, yet tend to generate answers in the input language.\"\n\n---\n\n### 3. Section and location of Finding 2\n\nFinding 2 appears in **Section 4.2 (Results)** within Section 4 (\"Language Mixing Patterns\"). The paper does not use traditional page numbers in its HTML rendering; it is within the first major results subsection of the paper.\n\n---\n\n### 4. Abstract + Section 4 on intermediate steps vs. final answers\n\n**Abstract** (verbatim):\n> \"Reasoning language models (RLMs) excel at complex tasks by leveraging a chain-of-thought process to generate structured intermediate steps. However, language mixing, i.e., reasoning steps containing tokens from languages other than the prompt, has been observed in their outputs and shown to affect performance, though its impact remains debated. We present the first systematic study of language mixing in RLMs, examining its patterns, impact, and internal causes across 15 languages, 7 task difficulty levels, and 18 subject areas, and show how all three factors influence language mixing. Moreover, we demonstrate that the choice of reasoning language significantly affects performance: forcing models to reason in Latin or Han scripts via constrained decoding notably improves accuracy. Finally, we show that the script composition of reasoning traces closely aligns with that of the model's internal representations, indicating that language mixing reflects latent processing preferences in RLMs. Our findings provide actionable insights for optimizing multilingual reasoning and open new directions for controlling reasoning languages to build more interpretable and adaptable RLMs.\"\n\n**Section 4.2 paragraph following Finding 2** (verbatim):\n> \"While reasoning traces exhibit language mixing, the final answers remain more aligned with the input language. This indicates that language mixing occurs primarily in the intermediate reasoning phase, not in the final output. This behavior is unsurprising, as reasoning models are generally trained with supervision or reward signals focused on the final answer, encouraging alignment with the input language, while leaving the reasoning steps unconstrained. As a result, models are free to mix languages during reasoning if it helps them reach a correct answer more effectively.\"\n\n---\n\n### 5. Exact sentence on \"training supervision signals focused on final answers\"\n\n(Verbatim, from Section 4.2):\n> \"This behavior is unsurprising, as reasoning models are generally trained with supervision or reward signals focused on the final answer, encouraging alignment with the input language, while leaving the reasoning steps unconstrained.\"\n\nNote: the paper uses the phrase **\"supervision or reward signals focused on the final answer\"** — not \"training supervision signals focused on final answers\" verbatim, though the meaning is identical.\n\n---\n\n### All 8 Findings (verbatim)\n\n| # | Text |\n|---|------|\n| Finding 1 | \"Language mixing is most prevalent when the input is neither English nor Chinese.\" |\n| Finding 2 | \"RLMs mix languages during reasoning, yet tend to generate answers in the input language.\" |\n| Finding 3 | \"The degree of language mixing increases with task difficulty.\" |\n| Finding 4 | \"Language mixing is more pronounced in STEM subjects.\" |\n| Finding 5 | \"Distillation amplifies language mixing.\" |\n| Finding 6 | \"Non-Latin/Han-script languages benefit significantly from reasoning in Latin or Han scripts.\" |\n| Finding 7 | \"Latin and Han-script languages favor their native script.\" |\n| Finding 8 | \"Language mixing reflects the internal processing patterns of RLMs, as reasoning traces mirror the model's preferred scripts.\" |\n\n---\n\n### Citation verification summary\n\nThe claim that \"final answers remain more aligned with the input language\" is **directly supported** by the paper — it appears as the explanatory text immediately following Finding 2 in Section 4.2. The phrase \"training supervision signals focused on final answers\" is a close paraphrase of the verbatim text: *\"supervision or reward signals focused on the final answer.\"* The paper does explicitly make both claims, but the exact phrasing in the paper uses \"supervision or reward signals,\" not \"training supervision signals.\""
      }
    ],
    "totalDurationMs": 96175,
    "totalTokens": 16501,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 624,
      "cache_read_input_tokens": 14731,
      "output_tokens": 1145,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1145,
          "cache_read_input_tokens": 14731,
          "cache_creation_input_tokens": 624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 624,
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
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "5481cd70-f409-4736-b0f3-f7b7571c7f08",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 14_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "5738e851-6d66-409f-994b-3aa9643b740b",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-only GRPO reward for multilingual fidelity",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Assistant

_source line 16 · 2026-05-10T08:36:32.811Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have all the information I need to make the revisions. Let me summarize what I found:

**For arXiv 2505.14815:**

Finding 2 DOES exist and is verbatim: "RLMs mix languages during reasoning, yet tend to generate answers in the input language."

The explanatory text following Finding 2 (Section 4.2) says:
> "While reasoning traces exhibit language mixing, the final answers remain more aligned with the input language. This indicates that language mixing occurs primarily in the intermediate reasoning phase, not in the final output. This behavior is unsurprising, as reasoning models are generally trained with supervision or reward signals focused on the final answer, encouraging alignment with the input language, while leaving the reasoning steps unconstrained."
 
So the key distinction is that Finding 2 itself uses the phrasing "tend to generate answers in the input language," while the explanatory text that follows uses "the final answers remain more aligned with the input language." The paper's attribution appears to conflate these two phrasings—presenting the explanatory language as if it were the Finding 2 statement itself, when in fact the explanatory text comes after the Finding 2 header. I need to correct how I'm citing Finding 2 from the paper—the exact quote should be "RLMs mix languages during reasoning, yet tend to generate answers in the input language" from §4.2, not "the final answers remain more aligned with the input language," which is actually from the explanatory text that follows Finding 2. The training supervision phrase also needs to be quoted precisely as "supervision or reward signals focused on the final answer." For arXiv 2505.15257, I'm noting it uses a training-free, inference-time SVD-based activation ablation approach. I need to correct the citation for Finding 2 throughout the paper. The original source states "RLMs mix languages during reasoning, yet tend to generate answers in the input language" rather than just focusing on the final answer alignment. I should update the opportunity section to accurately reflect this quote and its attribution to training supervision focused on final answers, making sure the citation is precise and consistent wherever it appears. the final answers remain more aligned with the input language because models are trained with supervision or reward signals that focus on the final answer. I should also add arXiv 2505.15257 to the landscape section—it uses SVD-based activation ablation at inference time to disentangle language from reasoning without any training, achieving results comparable to RL methods on MGSM, whereas our approach achieves answer fidelity through GRPO rewards during standard RL fine-tuning without requiring inference-time modifications.

Given the reviewer's feedback that this is "genuinely one targeted revision away from Findings-ready," I think a minor fix makes sense here rather than a major pivot. Both issues are mechanical and the core idea is sound, so I'll update the JSON to correct the Finding 2 citation throughout and add the 2505.15257 entry to the landscape.

Now I'm going through each section to update the citations. In the opportunity section, I need to replace the paraphrased quote with the actual Finding 2 language about how RLMs mix languages during reasoning but generate answers in the input language, then add the §4.2 analysis that explains this is due to supervision focused on final answers. The approach section needs the same treatment, updating the citation format and ensuring the quote accurately reflects what the paper states. I'm refining the citations to be more precise—adding section numbers and pulling the exact quotes from the paper to show how the findings about answer-language alignment connect to our approach of decoupling correctness rewards from language preservation.

Now I need to integrate the new paper 2505.15257 into the landscape section, placing it alongside the existing Language-Mixed CoT entry to show how different methods address the language-mixing problem, then update the key references list accordingly. that 'the final answers remain more aligned with the input language,' attributing this to models being trained with supervision or reward signals focused on the final answer—so the answer span acts as the natural language anchor, and language-agnostic correctness rewards undermine this by removing the language signal.

In the approach section, I'm refining how I present the evidence: the arXiv paper explicitly documents that while RLMs mix languages during reasoning, they consistently generate answers in the input language, with the analysis showing this stems from training supervision centered on final answers. This confirms the answer span is the natural anchor and that language-agnostic rewards erode this alignment.

For the second point, GRPO's optimization naturally pushes reasoning toward English—the dominant pretraining language, which aligns with the finding that Latin-script reasoning achieves optimal accuracy. The model develops English-mediated internal reasoning while still producing target-language surface answers, directly operationalizing the SFT finding as an RL reward. Crucially, my reward design doesn't fight this tendency; instead it restores the model's training-induced alignment between answer language and input language, which standard GRPO correctness training alone would erode.

The baseline validates the mechanistic claim that supervision focused on final answers produces this natural answer-language alignment. I'm also noting that my approach restores the model's training-induced tendency to produce target-language answers, and I should add that arXiv 2505.15257 addresses language-reasoning disentanglement through a different mechanism.

arXiv 2505.15257 uses SVD-based activation ablation at inference time to project out language-specific subspaces from hidden states without any training, achieving results comparable to RL on MGSM. My method is fundamentally different—I'm using a GRPO reward during standard RL fine-tuning to achieve answer-surface fidelity, with no inference-time modifications needed.

For the description section, arXiv 2505.14815 (§4.2, Finding 2) explicitly documents that RLMs mix languages during reasoning but tend to generate answers in the input language, and the analysis shows that training supervision signals focused on final answers are what create this alignment—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this by removing the language signal.

I'm also updating the operational framing to reference §4.2 and Finding 2 from arXiv 2505.14815 when describing how I'm restoring the model's training-induced tendency to produce target-language answers.

Adding the new reference "When Less Language is More: Language-Reasoning Disentanglement Makes LLMs Better Multilingual Reasoners" (arXiv 2505.15257, May 2025) to the key references section.

Now I'm carefully revising the complete JSON structure to incorporate these minor updates while preserving everything else exactly as it is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5738e851-6d66-409f-994b-3aa9643b740b",
  "isSidechain": false,
  "requestId": "req_011CataiZL8rJ9A44LvyDGTG",
  "type": "assistant",
  "uuid": "bf5f9ac9-fdb8-461d-8d12-69615ed33ca8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018symeL2T2Xa3uM18eRycpz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1544,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 27815,
      "output_tokens": 14007,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1544,
          "output_tokens": 14007,
          "cache_read_input_tokens": 27815,
          "cache_creation_input_tokens": 2469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2469
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

_source line 17 · 2026-05-10T08:39:45.621Z_

I now have everything I need. Key findings:

1. **Finding 2 is real** — its verbatim text is: *"RLMs mix languages during reasoning, yet tend to generate answers in the input language."* The phrase "the final answers remain more aligned with the input language" appears in the §4.2 **explanatory body text** immediately following the Finding 2 header, not as the Finding 2 statement itself. The attribution to training supervision is verbatim: *"supervision or reward signals focused on the final answer."* So the fix is: quote Finding 2 correctly and attribute the body text to §4.2 rather than conflating it with Finding 2's header.

2. **arXiv 2505.15257** is confirmed training-free, SVD-based activation ablation at inference time, achieving results comparable to PPO RL (59.02% vs 60.33% on MGSM with Qwen-2.5-3B-Instruct) with no weight updates.

Both fixes are mechanical. The change type is **minor** — no pivot or major revision needed. The reviewer explicitly says "one targeted revision away from Findings-ready."

```json
{
  "title": "Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO",
  "project_name": "answer_fidelity_free_trace",
  "source": "web_research",
  "change_type": "minor",
  "core_problem": "GRPO training for multilingual reasoning induces cross-lingual collapse—models default to English chain-of-thought within a few hundred updates regardless of input language (arXiv 2506.05850)—while language consistency rewards that prevent collapse impose a 5–10 percentage-point accuracy penalty. A mechanistic study (arXiv 2505.14815) explains why: language mixing occurs primarily in intermediate reasoning steps, not final answers, and internal representations are Latin-script-dominated regardless of input language. This means (a) constraining the reasoning trace to the target language forces a suboptimal reasoning substrate, causing the accuracy penalty, and (b) pretrained models naturally tend to generate answers in the target language even when traces are mixed—a training-induced tendency (arXiv 2505.14815, §4.2 attributes this to 'supervision or reward signals focused on the final answer') that GRPO correctness training erodes because the reward focuses only on numeric accuracy, not surface language. The accuracy-fidelity trade-off therefore has a structural cause: whole-trace language constraints fight the model's natural optimization toward English-mediated reasoning, whereas only the answer-surface behavior needs to be anchored. This paper explicitly scopes its primary claims to mid-to-high-resource languages (German, French, Spanish, Russian, Chinese, Japanese, Thai) where English-pivot reasoning is beneficial (arXiv 2508.14828); genuinely low-resource languages are excluded from primary claims.",
  "opportunity": "'Cross-lingual Collapse' (arXiv 2506.05850) precisely quantifies that GRPO amplifies pretraining language imbalances and that language consistency reward 'mitigates this drift with a large drop in accuracy.' arXiv 2505.14815 ('Language Mixing in Reasoning Language Models') provides the mechanistic grounding: (a) language mixing is concentrated in intermediate reasoning steps, not final answers—§4.2, Finding 2 of that paper states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to models being 'trained with supervision or reward signals focused on the final answer'—meaning final-answer language is a natural anchor that GRPO's language-agnostic correctness reward erodes; (b) forcing reasoning in Latin or Han scripts substantially improves accuracy (gains of 44–115% for non-Latin inputs documented in Table 10), confirming that English-dominant traces are an optimization asset, not a bug; and (c) the script composition of reasoning traces mirrors internal representations (Finding 8), showing that language mixing reflects latent processing preferences that reward pressure should not fight. For mid-to-high-resource languages, arXiv 2508.14828 additionally shows that fine-tuning on English-mediated reasoning traces outperforms native-language distillation—establishing the SFT inductive bias we operationalize as an RL reward. Selective translation at inference (arXiv 2510.27269) confirms English-trace reasoning with target-language answers achieves 88.0 average accuracy by translating only 20% of inputs. These jointly motivate the same minimal training fix—reward correctness language-agnostically, reward the FINAL ANSWER for target-language surface fidelity, leave intermediate traces unconstrained—but now with mechanistic grounding: we are restoring the model's training-induced tendency (documented in §4.2, Finding 2 of arXiv 2505.14815) to produce target-language answers, which GRPO correctness training alone erodes.",
  "landscape": "M-Thinker (arXiv 2510.07300) applies Language Consistency (LC) and Cross-lingual Thinking Alignment (CTA) rewards constraining the entire trace-plus-answer to the target language; this mitigates collapse but imposes language constraints on reasoning traces, maintaining the accuracy penalty that 2505.14815 attributes to forcing a suboptimal reasoning substrate. BRIDGE / M2A ('Learn Globally, Speak Locally', 2025) uses SFT and GRPO with translated questions and a multilingual alignment reward that includes language consistency between input and full generated output; like M-Thinker, it does not decouple trace from answer language constraint. ExpLang (arXiv 2602.21887, Feb 2026) uses on-policy thinking language selection as a unified exploration/exploitation signal across 12 non-English languages on Qwen3-4B; language tags apply before the thinking tag, covering the complete response—no trace/answer decoupling. polyGRPO (arXiv 2604.21593) treats language as an exploration signal via diverse-language rollouts with correctness-only reward, achieving 75.93% multilingual MGSM average and 60.46% multilingual X-CSQA average on Qwen2.5-7B-Instruct (vs. base model 54.27% on X-CSQA). It does not constrain the answer language separately; the best condition is language-unconstrained, and the paper reports no answer-language fidelity metric. Direct numerical comparison with our method is confounded by the base model generation difference (Qwen2.5-7B-Instruct vs. Qwen3-7B); however, unlike polyGRPO, our method explicitly enforces target-language answer surface and provides a mechanistic account grounded in arXiv 2505.14815 for why answer-only constraint suffices without an accuracy penalty. TLPO (arXiv 2604.26553) mitigates language confusion via token-level updates throughout the full response; categorically different from our approach of explicitly permitting English-trace reasoning rather than suppressing language-switching tokens. 'Making Qwen3 Think in Korean' (arXiv 2508.10355) is a single-language case study using a two-stage fine-tune with an oracle judge, not a generalizable reward design. TRIT (arXiv 2602.05940) jointly trains translation and reasoning, requiring explicit bilingual supervision. Language-Mixed CoT (arXiv 2510.04230) addresses trace-language through data construction, not reward design. arXiv 2505.15257 ('When Less Language is More', May 2025) achieves language-reasoning disentanglement at inference time via SVD-based activation ablation—projecting language-specific subspaces out of mid-layer hidden states during the forward pass—with no training required, reporting results comparable to RL (PPO) on MGSM. Our method differs categorically: we achieve answer-surface fidelity via a GRPO reward during standard RL fine-tuning, with no inference-time modification to activations or architecture. PB-RLSVR (arXiv 2509.25543) uses whole-response semantic reward from an external expert model. 'Language Mixing in Reasoning Language Models' (arXiv 2505.14815) characterizes language mixing patterns and shows (§4.2, Finding 2) that 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' attributing this to 'supervision or reward signals focused on the final answer'; it does not address GRPO reward design. 'Long CoT Reasoning Across Languages' (arXiv 2508.14828) provides the SFT inductive bias—English-mediated reasoning with target-language surface answers—that we operationalize as an RL reward.\n\nReasonXL (arXiv 2604.12378, Apr 2026) introduces a large-scale parallel corpus of cross-domain reasoning traces and adapts LLMs via SFT followed by RLVR to reason entirely in a desired target language, reporting that resulting models match or exceed baseline performance across five European languages (English, German, French, Italian, and Spanish). Three structural differences separate ReasonXL from the proposed approach. First, ReasonXL requires constructing over 2 million aligned reasoning-trace samples per language as supervised training data—a resource bottleneck that makes the method inapplicable to languages lacking large-scale parallel corpora; our method achieves answer-surface fidelity via reward design alone with no parallel data requirement, making it applicable wherever a language identification signal exists. Second, ReasonXL covers only Latin-script European languages and explicitly does not address Thai, Chinese, or Japanese; our SFVG gate thresholds are script-adaptive (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), precisely targeting the non-Latin-script challenge that ReasonXL leaves unaddressed. Third—and most fundamentally—ReasonXL's design goal is to force reasoning traces into the target language, replicating the constraint that arXiv 2505.14815 (Table 10) shows imposes an accuracy penalty for non-Latin-script languages; our method leaves traces entirely unconstrained and rewards only the answer surface, avoiding this cost by design.\n\nKi et al. (arXiv 2604.04720, 'What Makes Good Multilingual Reasoning? Disentangling Reasoning Traces with Measurable Features', Apr 2026) define measurable reasoning features spanning multilingual alignment, reasoning step, and reasoning flow dimensions—evaluated on MGSM-Rev2 and AIME 2024–25 across Distill-DeepSeek and Qwen3 model series (the same base model family we use)—finding that 'most features are positively associated with accuracy, but the strength of association varies considerably across languages and can even reverse in some.' They explicitly 'challenge English-centric reward designs' and advocate for 'adaptive objectives that accommodate language-specific reasoning patterns.' This paper directly engages our core theoretical premise, and the engagement is mutually reinforcing rather than adversarial. 2604.04720 critiques reward designs that IMPOSE English reasoning patterns on non-English inputs via explicit trace constraints—precisely the design implemented by M-Thinker's LC reward, ExpLang's language tags, and ReasonXL's SFT+RLVR trace alignment, which we also oppose. Our approach does the opposite: GRPO optimization naturally produces English-dominant reasoning traces (arXiv 2505.14815), but we neither reward nor penalize trace language—traces are left entirely free. The 'adaptive objectives' 2604.04720 advocates are operationalized in our method at the answer surface level, where script-adaptive LID thresholds (≥8 characters for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK) implement exactly the language-specific accommodation they recommend. Critically, 2604.04720's finding that trace-level feature-accuracy associations vary and reverse across languages constitutes independent empirical support for our design: if the optimal reasoning-trace composition differs across languages, constraining the trace to a single language standard (as whole-trace LC rewards do, and as ReasonXL's SFT pipeline does) risks suppressing language-specific optimal reasoning patterns—the accuracy penalty documented by arXiv 2505.14815 (Table 10) and arXiv 2506.05850. Our method avoids this cost entirely by leaving the trace unconstrained.\n\nNo existing work isolates the language constraint exclusively to the answer span in a GRPO reward formulation.",
  "approach": "We fine-tune Qwen3-7B using LoRA (rank-16, alpha-16, TRL GRPOTrainer) with three reward components: (1) a verifiable correctness reward evaluated language-agnostically via numeric/symbolic answer extraction from &lt;answer>…&lt;/answer> delimiters; (2) a sentence-frame format reward (weight 0.1) that fires when the answer span contains a valid numeric value AND a sufficient sentence frame (defined below), incentivizing the model to produce complete sentences rather than bare numerals; and (3) a target-language compliance reward applied exclusively to the final answer span using fastText LID, weighted at λ=0.3.\n\nSystem Prompt Design: A single universal English-language system prompt is used across all seven target languages: 'Solve the following math problem step by step. Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags.' Critically, the system prompt does not name the target language; the model must infer the target language from the question text alone. This is the harder generalization condition but reflects realistic deployment where a multilingual model receives questions without explicit language labels. A supplementary ablation uses a language-explicit variant ('…as a complete sentence in [LANGUAGE], inside &lt;answer>…&lt;/answer> tags') for each of the seven languages; we report SFVG Gate 2 activation rates disaggregated by language for both prompt variants. This comparison directly tests whether explicit language cues in the prompt accelerate sentence-frame adoption, and whether SFVG Gate 2 activation rates differ systematically across scripts (Latin/Cyrillic vs. CJK/Thai) under the universal prompt.\n\nSentence-Frame Answer Format: The system prompt instructs the model to express its final answer as a complete sentence in the target language (e.g., 'Die Antwort lautet 42.' for German) inside the &lt;answer> tag. This design is motivated by two converging findings: (a) arXiv 2505.14815 (§4.2, Finding 2) states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language'; the §4.2 analysis explicitly notes that 'the final answers remain more aligned with the input language,' attributing this to 'supervision or reward signals focused on the final answer'—confirming that the answer span is the natural language anchor and that language-agnostic correctness rewards erode this alignment by removing the language signal; and (b) fastText LID cannot reliably detect language from bare numerals, so sentence-frame content is a prerequisite for the LID reward to function.\n\nSentence-Frame Validity Gate (SFVG): Replaces the prior 'answer-validity gate.' Three conditions must be satisfied before the LID reward fires, with all three logged per language per step in the ablation analysis: Gate 1 (Numeric presence): regex confirms a valid numeric answer exists inside the answer tag; Gate 2 (Frame presence): the non-numeric content of the answer span meets a script-adaptive minimum—≥8 characters for Latin/Cyrillic scripts (German, French, Spanish, Russian), ≥5 for Thai script, ≥3 for CJK logographic scripts (Chinese, Japanese)—ensuring the answer is a complete sentence frame rather than a bare numeral or a single-word suffix; Gate 3 (LID confidence): fastText LID applied to the non-numeric answer content returns confidence ≥0.6 for the expected target language.\n\nThe SFVG design eliminates two distinct failure modes simultaneously. The LID-on-numerics failure (bare '42' → no language signal) is blocked by Gate 2, which rejects answer spans with insufficient non-numeric content. The residual reward-hacking mode—appending a single target-language token to a bare numeral (e.g., '42 да' for Russian, where 'да' = 2 Cyrillic chars < 8-char threshold)—is also blocked by Gate 2, since 'да' alone fails the ≥8-character frame-presence check. Both failure modes are explicitly reported in the method section with examples.\n\nPer-Language Correct-Language Rate: In addition to the three SFVG gate activation rates, a fourth diagnostic metric is logged per language per step: the correct-language rate, defined as the fraction of Gate-2-passing answer spans for which fastText LID's top-1 prediction matches the expected target language. This is a zero-cost logging addition requiring no new experiments. The correct-language rate is essential for validating the universal-prompt design for Latin-script languages (German, French, Spanish): under a prompt that says 'in the same language as the question' without naming the target language, the model may produce a sentence frame in the wrong target language (e.g., a Spanish-language frame for a French question). Such cross-Latin-script errors cause Gate 3 to fail—since Gate 3 requires ≥0.6 LID confidence for the expected target language—resulting in silently zero LID reward that is not detectable from Gate 2 or Gate 3 activation rates alone. The correct-language rate directly surfaces this failure mode and enables diagnosis of whether the universal prompt provides sufficient language signal for typologically similar Latin-script languages. Results are reported separately for the universal-prompt and language-explicit-prompt ablation conditions, quantifying the frequency and distribution of cross-Latin-script confusion in each setting.\n\nLID Activation Trajectory Analysis: SFVG Gate 2 pass-rate per language per step is reported as a first-class ablation metric in the paper. This trajectory provides mechanistic insight into how the model progressively learns to produce sentence-frame answers as training proceeds—an emergent curriculum from format reward to LID reward—and constitutes a novel empirical contribution absent from all prior multilingual GRPO papers. Gate 2 activation rates are reported separately for the universal-prompt and language-explicit-prompt conditions, quantifying the cost of language inference from question context alone.\n\nSince GRPO's optimization pressure naturally drives traces toward English (the dominant pretraining language, consistent with arXiv 2505.14815's finding that Latin-script reasoning yields optimal accuracy per Table 10), the model acquires English-mediated internal reasoning while producing target-language surface answers—directly operationalizing arXiv 2508.14828's SFT finding as an RL reward. Critically, our reward design does not fight this tendency; it restores the model's training-induced natural alignment between answer surface language and input language (arXiv 2505.14815, §4.2 Finding 2), which GRPO correctness training alone erodes.\n\nCross-Task Language Fidelity Transfer (Second Empirical Pillar): The paper's second research question is whether language fidelity achieved via trace constraint (whole-trace LC reward, M-Thinker baseline) differs qualitatively from fidelity achieved via answer-only constraint (ours). Our hypothesis, grounded in arXiv 2505.14815's finding that constraining trace language forces a suboptimal reasoning substrate, is that whole-trace LC reward causes language-rigidity that degrades cross-task language fidelity on commonsense reasoning tasks, whereas answer-only constraint produces robust language fidelity that transfers. This is tested via inference-only evaluation on XCOPA (causal commonsense, Chinese and Thai), XStoryCloze (story completion, Chinese, Spanish, Russian), XQuAD (extractive reading comprehension, German/Spanish/Russian/Chinese; ~2 H100-hours additional inference covering 4 of the 7 primary MGSM languages), and MMLU-ProX (arXiv 2503.10497, EMNLP 2025 Main; 0-shot inference across all 7 MGSM languages, available at li-lab/MMLU-ProX on HuggingFace). XQuAD is included to provide a structured extractive QA task that complements the commonsense and story-completion tasks already in the transfer suite; it covers the subset of our MGSM languages for which XQuAD data exists.\n\nEvaluation Scope and XTREME-UP: XTREME-UP (arXiv 2305.11938, EMNLP 2023 Findings) is explicitly out of scope for two independent structural reasons. First, XTREME-UP is designed for under-represented languages (88 languages, scarce-data regime), whereas this paper's primary claims are scoped to mid-to-high-resource languages following arXiv 2508.14828; the paper's language coverage and XTREME-UP's coverage are disjoint by design. Second, XTREME-UP's tasks—ASR, OCR, machine translation, autocomplete, semantic parsing, and transliteration—are user-centric technologies with no math reasoning component, making the benchmark structurally inapplicable to a math GRPO study. XQuAD, included above, covers the structured-prediction QA transfer evaluation that intersects with our language set and task type.\n\nCross-task evaluation includes four reference checkpoints: (1) the pretrained Qwen3-7B base model before any GRPO fine-tuning, (2) vanilla GRPO fine-tuned, (3) whole-trace LC reward (M-Thinker baseline), and (4) answer-only SFVG (ours). Adding the pretrained base checkpoint costs no additional training (pure inference) and is necessary to establish whether whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level—as opposed to merely failing to preserve it. This baseline directly validates the mechanistic claim from arXiv 2505.14815 (§4.2, Finding 2) that 'supervision or reward signals focused on the final answer' produce the natural answer-language alignment, and that GRPO fine-tuning with language-agnostic correctness reward is the degradation source. PB-RLSVR (arXiv 2509.25543) is included as a fifth checkpoint. If whole-trace LC reward degrades cross-task language fidelity below the pretrained base while answer-only SFVG preserves or exceeds the base model's natural fidelity, this constitutes a strong mechanistic finding about the generalization cost of over-constraining trace language.\n\nPrimary scope: seven mid-to-high-resource MGSM languages (German, French, Spanish, Russian, Chinese, Japanese, Thai). Low-resource languages are explicitly excluded from primary claims citing arXiv 2508.14828. A secondary Swahili experiment with an NLLB-200 translation bridge characterizes the low-resource boundary. We build on the public M-Thinker codebase and ablate four conditions: (a) vanilla GRPO, (b) whole-trace LC reward (M-Thinker baseline), (c) answer-only language reward with SFVG (ours), (d) PB-RLSVR (arXiv 2509.25543). Primary evaluation: MGSM, MMATH, and PolyMath across 7 languages. Transfer evaluation (inference only, 5 checkpoints): XCOPA, XStoryCloze, XQuAD, and MMLU-ProX. Expected outcome: near-100% SFVG activation by mid-training, near-100% answer fidelity, no statistically significant accuracy penalty over vanilla GRPO for mid-to-high-resource languages, and preserved or improved cross-task fidelity relative to the whole-trace LC baseline and relative to the pretrained base checkpoint.",
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
  "description": "We address the accuracy-fidelity trade-off in multilingual GRPO training, explicitly scoped to mid-to-high-resource languages where English-pivot reasoning is beneficial (arXiv 2508.14828). The paper's theoretical grounding comes from arXiv 2505.14815, which shows that (a) language mixing in reasoning models is concentrated in intermediate steps—not final answers: §4.2, Finding 2 states 'RLMs mix languages during reasoning, yet tend to generate answers in the input language,' with the §4.2 analysis explicitly noting that 'the final answers remain more aligned with the input language' and attributing this to 'supervision or reward signals focused on the final answer'; and (b) Latin-script (English) reasoning yields optimal accuracy (Table 10: 44–115% accuracy gains for non-Latin-script inputs when reasoning is constrained to Latin script), meaning English-dominant traces are an asset. Our approach decouples the two objectives: correctness is rewarded language-agnostically, while target-language fidelity is enforced exclusively on the final answer segment—operationally restoring the model's training-induced tendency to produce target-language answers (§4.2, Finding 2, arXiv 2505.14815), which GRPO correctness training alone erodes. Ki et al. (arXiv 2604.04720), who challenge English-centric reward designs that IMPOSE trace language constraints and call for adaptive objectives, provide independent empirical support: if trace-level feature-accuracy associations vary and reverse across languages, constraining the trace suppresses language-specific optimal reasoning—precisely the accuracy penalty our design avoids.\n\nThe core mechanism is the Sentence-Frame Validity Gate (SFVG): the model is prompted via a universal English system prompt ('Express your final answer as a complete sentence in the same language as the question, inside &lt;answer>…&lt;/answer> tags') to produce answers as complete target-language sentences (e.g., 'Die Antwort lautet 42.'). The LID reward fires only when (Gate 1) a valid numeric value is present, (Gate 2) the non-numeric content meets a script-adaptive minimum (≥8 chars for Latin/Cyrillic, ≥5 for Thai, ≥3 for CJK), and (Gate 3) fastText LID confidence on the non-numeric content ≥0.6 for the expected target language. A fourth diagnostic metric—the per-language correct-language rate (fraction of Gate-2-passing spans where LID top-1 matches expected target language)—is logged per language per step at zero additional cost. This metric is essential for detecting cross-Latin-script confusion (e.g., Spanish frames for French questions) that causes silent Gate 3 failures under the universal prompt; the language-explicit prompt ablation quantifies whether this confusion is resolved by explicit language cues. The universal prompt does not name the target language; the model infers it from the question. SFVG gate activation rates and correct-language rates disaggregated by language and step are reported as first-class ablation metrics.\n\nThe second empirical pillar tests whether language fidelity achieved through trace constraint (M-Thinker baseline) differs qualitatively from fidelity achieved through answer-only constraint. Cross-task evaluation on XCOPA (Chinese, Thai), XStoryCloze (Chinese, Spanish, Russian), XQuAD (German, Spanish, Russian, Chinese; ~2 H100-hours, covering 4 of 7 primary languages with extractive QA), and MMLU-ProX (all 7 MGSM languages, 0-shot) uses five reference checkpoints: (1) pretrained Qwen3-7B base (no fine-tuning), (2) vanilla GRPO, (3) whole-trace LC reward (M-Thinker), (4) answer-only SFVG (ours), and (5) PB-RLSVR. The pretrained base checkpoint validates that whole-trace LC reward actively degrades cross-task language fidelity below the base model's natural level. XTREME-UP (arXiv 2305.11938) is out of scope: it targets under-represented languages (88 languages, scarce-data regime) disjoint from our mid-to-high-resource scope, and its tasks—ASR, OCR, MT, autocomplete, semantic parsing—have no math reasoning component; XQuAD serves the structured-prediction QA evaluation that reviewers may expect.\n\nImplementation: LoRA (rank-16) GRPO on Qwen3-7B via TRL GRPOTrainer. Auto-mode grid: λ ∈ {0.1, 0.2, 0.3, 0.5} × 1 seed (exploratory sweep) + best λ × 2 seeds, LoRA rank fixed at 16 throughout (~191 H100-hours total including XQuAD inference, within 200 H100-hour budget). Primary evaluation: MGSM, MMATH, PolyMath. Transfer evaluation: XCOPA, XStoryCloze, XQuAD, MMLU-ProX. Secondary Swahili experiment characterizes the low-resource boundary. Differentiated from all concurrent work (ExpLang, polyGRPO [MGSM 75.93% avg on Qwen2.5-7B-Instruct], TLPO, M-Thinker, BRIDGE/M2A, Ki et al. 2604.04720, ReasonXL [2M+ parallel samples/language, Latin-script-only, trace-in-target-language goal], and arXiv 2505.15257 [training-free SVD activation ablation at inference time]) which either apply language constraints to the full reasoning trace, require large-scale parallel data, or analyze trace features or hidden-state geometry without proposing a GRPO reward that decouples trace from answer constraint. Target: EMNLP 2026 Findings."
}
```

---

**Summary of changes (minor):**

**Issue 1 — Finding 2 attribution fixed throughout:**
The paper now correctly quotes Finding 2's verbatim header text (*"RLMs mix languages during reasoning, yet tend to generate answers in the input language"*, §4.2) and attributes the explanatory phrase "the final answers remain more aligned with the input language" to the §4.2 body text following Finding 2 — not as the Finding 2 statement itself. The training-supervision attribution is corrected to the paper's exact phrasing: *"supervision or reward signals focused on the final answer."* All three sections (opportunity, approach, description) are updated consistently.

**Issue 2 — arXiv 2505.15257 added:**
Added to the landscape with a one-sentence categorical contrast (training-free SVD activation ablation vs. GRPO reward during RL fine-tuning), added to `key_references`, and referenced in the description's differentiation paragraph. The paper's confirmed details (SVD-based projection, inference-time only, no weight updates, MGSM results comparable to PPO) match the reviewer's characterization exactly.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf5f9ac9-fdb8-461d-8d12-69615ed33ca8",
  "isSidechain": false,
  "requestId": "req_011CataiZL8rJ9A44LvyDGTG",
  "type": "assistant",
  "uuid": "cbe6ce90-c27a-4932-9585-0d6207c1db7b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018symeL2T2Xa3uM18eRycpz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1544,
      "cache_creation_input_tokens": 2469,
      "cache_read_input_tokens": 27815,
      "output_tokens": 14007,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2469,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1544,
          "output_tokens": 14007,
          "cache_read_input_tokens": 27815,
          "cache_creation_input_tokens": 2469,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2469
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

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "cbe6ce90-c27a-4932-9585-0d6207c1db7b",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-only GRPO reward for multilingual fidelity",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Answer-Fidelity Reward with Free Reasoning Trace in Multilingual GRPO\"…",
  "leafUuid": "cbe6ce90-c27a-4932-9585-0d6207c1db7b",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise answer-only GRPO reward for multilingual fidelity",
  "sessionId": "ff1922a4-6d2b-4e1f-b093-fdbaaae9d3af"
}
```

---
