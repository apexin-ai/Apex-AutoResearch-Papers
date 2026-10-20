# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 21
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-2/d8521c40-2131-41e0-b2da-32601bc8ea03.jsonl`
- **Structured JSON:** [`eccbd10d1b5e69099c78.json`](../../sessions/ec/eccbd10d1b5e69099c78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:48:18.944Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:48:18.944Z",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment\",\n  \"project_name\": \"cls_lora_cultural_preservation\",\n  \"source\": \"web_research\",\n  \"level\": \"solid\",\n  \"core_problem\": \"Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.\",\n  \"opportunity\": \"'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.\",\n  \"landscape\": \"INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\\n\\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\\n\\nTwo directly related selective-LoRA methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective.\",\n  \"approach\": \"We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\\n\\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\\n\\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\\n\\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use held-out splits of CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\\n\\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\\n\\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~230h A100 80GB (~92h H100 equivalent)\",\n      \"gpu_utilization\": \"~30–40% effective; GPU idles while the researcher inspects probe accuracy heatmaps to select layer partition boundaries, designs ablation grids, and iterates on training scripts between runs\",\n      \"timeline\": \"4–6 months\",\n      \"team\": \"1–2 researchers\",\n      \"estimated_gpu_cost\": \"~$345–475 (A100 at $1.49–2.06/hr via RunPod/Lambda); additional ~30h reflects new ablation runs (condition (b), ~12h) and XCOPA/XStoryCloze/MGSM evaluation (~18h)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~155h A100 80GB (~62h H100 equivalent)\",\n      \"gpu_utilization\": \"~60–70% effective; agent queues probing and LoRA sweep experiments overnight, researcher reviews layer partition heatmaps and approves next ablation tier once daily, cutting idle time ~50% vs. manual\",\n      \"timeline\": \"6–8 weeks\",\n      \"team\": \"1 researcher, ~30min/day check-in\",\n      \"claude_api_cost\": \"$150–250 (~1000–1500 conversation turns at $0.10–0.15/turn with Opus)\",\n      \"estimated_gpu_cost\": \"~$231–319 (A100 at $1.49–2.06/hr); additional ~25h reflects new ablation condition (b) runs and supplementary benchmark evaluations\",\n      \"risk_note\": \"Key risk: agent may commit to a suboptimal layer partition if probe accuracy curves are bimodal or noisy; the automated entropy-based partition fallback reduces (but does not eliminate) this risk; daily human review of the partition heatmap before LoRA runs remains the essential gate\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~310–360h A100 80GB (~122–144h H100 equivalent); within the ≤200h H100 hard constraint\",\n      \"gpu_utilization\": \"~85–90% effective; agent continuously queues the next experiment upon completion with no human approval bottleneck—idle only during brief checkpoint evaluation transitions\",\n      \"sweep\": \"3 LoRA rank values (8, 16, 32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs; plus ~12 baseline runs (full-LoRA, Surgical Steering, INCLINE, Source-Shielded Updates); plus ~4–6 new ablation runs for condition (b) (full LoRA + KL only, 2 models × 2–3 seeds); plus Stage 1 structural diagnostic runs; plus ~18–24h for XCOPA/XStoryCloze/MGSM evaluation across all checkpoints via lm-evaluation-harness\",\n      \"timeline\": \"5–8 days with 4–6 concurrent A100 GPUs (or 3–5 days with H100s)\",\n      \"team\": \"0 (2–3h of initial harness setup and config-space definition)\",\n      \"claude_api_cost\": \"$200–350 (~1500–2500 turns across experiment planning, result parsing, and ablation branching)\",\n      \"estimated_gpu_cost\": \"~$462–742 (A100 at $1.49–2.06/hr); increase from prior estimate reflects ~4–6 new condition (b) training runs and ~18–24h benchmark evaluation\",\n      \"speed_bottleneck\": \"Number of concurrent GPUs and the ~1h cultural benchmark evaluation per checkpoint; XCOPA/XStoryCloze/MGSM evaluation can be parallelized across checkpoints on separate GPUs via lm-evaluation-harness\",\n      \"risk_note\": \"Bimodal probe distributions are handled by an automated entropy-based partition fallback. The Stage 1 structural diagnostic provides an early signal: if cultural probe accuracy is unaffected by full-LoRA training, the layer-freezing strategy is validated before the main sweep begins, allowing early termination of degenerate configurations. If XCOPA performance drops relative to full-LoRA baseline, this is flagged as a scope constraint and reported transparently rather than silently absorbed.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026\",\n    \"EACL 2027 (ARR submission deadline August 3, 2026) — primary target for human-in-loop or manual mode\",\n    \"AAAI 2027 (submission deadline expected July–August 2026, TBC)\"\n  ],\n  \"key_references\": [\n    \"Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page)\",\n    \"Neuron-Level Analysis of Cultural Understanding in Large Language Models (arXiv:2510.08284, Yamamoto et al., ICLR 2026)\",\n    \"Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention / INCLINE (ACL 2025 Outstanding Paper, arXiv:2410.12462)\",\n    \"Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs (ACL 2025, arXiv:2502.14830, Liu & Niehues)\",\n    \"Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025 short paper, arXiv:2506.01675)\",\n    \"MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation (ACL 2025, aclanthology.org/2025.acl-long.762)\",\n    \"Continually Adding New Languages to Multilingual Language Models / LayRA (arXiv:2509.11414, September 2025)\",\n    \"Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)\",\n    \"AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)\",\n    \"CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)\",\n    \"Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)\",\n    \"Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)\",\n    \"Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)\",\n    \"LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)\",\n    \"XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)\",\n    \"Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)\",\n    \"Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)\"\n  ],\n  \"description\": \"Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\\n\\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\\n\\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on held-out splits of CulturalBench (ACL 2025, publicly available for training use); SemEval-2026 Task 7 data (BLEnD) reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\\n\\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). The cultural-preservation objective remains the categorical novelty absent from both. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks.\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"CRITICAL — CulturalBench is not available for training use. The paper claims Stage 2 cultural-localization probes are trained on 'held-out splits of CulturalBench (ACL 2025)...which is publicly available for training use.' This is factually wrong: the CulturalBench paper explicitly states 'our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.' Using CulturalBench for probe training violates its terms. The Stage 2 probe training data source must be replaced with a training-permitted cultural knowledge resource (e.g., multilingual Wikipedia cultural-domain sentences, MKQA, World Values Survey items, or a custom culturally-grounded QA dataset without OpenAI annotation-platform restrictions). SemEval-2026 Task 7 (BLEnD) is correctly identified as evaluation-only and is not the issue here.\", \"MINOR — Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, updated Feb 2026) applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters) and achieves strong cross-lingual alignment while preserving general capabilities, with adaptation concentrated in down-projection weights of later layers. Although its objective (language performance improvement) differs from CLS-LoRA's (cultural preservation), the layer-selective sparse-fine-tuning approach is closely related and should be acknowledged in the landscape section to preempt reviewer comparisons.\"]\nFeedback: Round 6 resolves all three Round 5 issues cleanly (XCOPA/XStoryCloze/MGSM added, 2×2 ablation with condition (b) included, Stage 1 separate-probe protocol specified). One critical correction remains before this can pass review:\n\n**Fix the CulturalBench training-use claim (critical, ~2 hours of work).** The CulturalBench paper explicitly states the dataset is prohibited from training use due to its OpenAI annotation-platform terms. Replace the Stage 2 cultural-localization probe training source with a dataset that permits training. Strong alternatives: (a) multilingual Wikipedia paragraphs from culture-specific articles, filtered by Wikidata cultural-domain tags — widely available, CC-BY licensed, and covers the 45+ cultural regions needed; (b) MKQA (multilingual knowledge questions, Apache 2.0), which covers culturally-grounded factual questions across languages; (c) a small GPT-4o-free annotation of culturally-grounded probe examples using open models (Qwen3-8B itself, before fine-tuning). CulturalBench should then be used *only* for final evaluation (Stage 4), alongside SemEval-2026 Task 7, which is already correctly limited to evaluation. Update the Stage 2 and Stage 4 data-source descriptions to reflect this separation, and remove the phrase 'publicly available for training use' from the CulturalBench reference. This is a single-paragraph fix in the approach and description sections.\n\n**Also add Sparse Subnetwork Enhancement (arXiv:2510.13580) to the landscape (minor, ~20 minutes).** Note that it improves underrepresented-language performance via language-neuron subnetwork selection, and differentiate on objective (language capability vs. cultural knowledge preservation) and partition axis (language-identity neurons vs. factual-cultural semantic axis).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\")."
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:48:18.950Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:48:18.950Z",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

## Round 1

19 recorded events

### User

_source line 3 · 2026-05-10T07:48:18.992Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment",
  "project_name": "cls_lora_cultural_preservation",
  "source": "web_research",
  "level": "solid",
  "core_problem": "Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.",
  "opportunity": "'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.",
  "landscape": "INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\n\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\n\nTwo directly related selective-LoRA methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective.",
  "approach": "We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\n\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\n\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\n\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use held-out splits of CulturalBench (ACL 2025; 1,696 human-verified questions across 45 global regions), which is publicly available for training use. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\n\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\n\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~230h A100 80GB (~92h H100 equivalent)",
      "gpu_utilization": "~30–40% effective; GPU idles while the researcher inspects probe accuracy heatmaps to select layer partition boundaries, designs ablation grids, and iterates on training scripts between runs",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$345–475 (A100 at $1.49–2.06/hr via RunPod/Lambda); additional ~30h reflects new ablation runs (condition (b), ~12h) and XCOPA/XStoryCloze/MGSM evaluation (~18h)"
    },
    "human_in_loop": {
      "gpu_hours": "~155h A100 80GB (~62h H100 equivalent)",
      "gpu_utilization": "~60–70% effective; agent queues probing and LoRA sweep experiments overnight, researcher reviews layer partition heatmaps and approves next ablation tier once daily, cutting idle time ~50% vs. manual",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$150–250 (~1000–1500 conversation turns at $0.10–0.15/turn with Opus)",
      "estimated_gpu_cost": "~$231–319 (A100 at $1.49–2.06/hr); additional ~25h reflects new ablation condition (b) runs and supplementary benchmark evaluations",
      "risk_note": "Key risk: agent may commit to a suboptimal layer partition if probe accuracy curves are bimodal or noisy; the automated entropy-based partition fallback reduces (but does not eliminate) this risk; daily human review of the partition heatmap before LoRA runs remains the essential gate"
    },
    "auto_research": {
      "gpu_hours": "~310–360h A100 80GB (~122–144h H100 equivalent); within the ≤200h H100 hard constraint",
      "gpu_utilization": "~85–90% effective; agent continuously queues the next experiment upon completion with no human approval bottleneck—idle only during brief checkpoint evaluation transitions",
      "sweep": "3 LoRA rank values (8, 16, 32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs; plus ~12 baseline runs (full-LoRA, Surgical Steering, INCLINE, Source-Shielded Updates); plus ~4–6 new ablation runs for condition (b) (full LoRA + KL only, 2 models × 2–3 seeds); plus Stage 1 structural diagnostic runs; plus ~18–24h for XCOPA/XStoryCloze/MGSM evaluation across all checkpoints via lm-evaluation-harness",
      "timeline": "5–8 days with 4–6 concurrent A100 GPUs (or 3–5 days with H100s)",
      "team": "0 (2–3h of initial harness setup and config-space definition)",
      "claude_api_cost": "$200–350 (~1500–2500 turns across experiment planning, result parsing, and ablation branching)",
      "estimated_gpu_cost": "~$462–742 (A100 at $1.49–2.06/hr); increase from prior estimate reflects ~4–6 new condition (b) training runs and ~18–24h benchmark evaluation",
      "speed_bottleneck": "Number of concurrent GPUs and the ~1h cultural benchmark evaluation per checkpoint; XCOPA/XStoryCloze/MGSM evaluation can be parallelized across checkpoints on separate GPUs via lm-evaluation-harness",
      "risk_note": "Bimodal probe distributions are handled by an automated entropy-based partition fallback. The Stage 1 structural diagnostic provides an early signal: if cultural probe accuracy is unaffected by full-LoRA training, the layer-freezing strategy is validated before the main sweep begins, allowing early termination of degenerate configurations. If XCOPA performance drops relative to full-LoRA baseline, this is flagged as a scope constraint and reported transparently rather than silently absorbed."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026",
    "EACL 2027 (ARR submission deadline August 3, 2026) — primary target for human-in-loop or manual mode",
    "AAAI 2027 (submission deadline expected July–August 2026, TBC)"
  ],
  "key_references": [
    "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page)",
    "Neuron-Level Analysis of Cultural Understanding in Large Language Models (arXiv:2510.08284, Yamamoto et al., ICLR 2026)",
    "Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention / INCLINE (ACL 2025 Outstanding Paper, arXiv:2410.12462)",
    "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs (ACL 2025, arXiv:2502.14830, Liu & Niehues)",
    "Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025 short paper, arXiv:2506.01675)",
    "MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation (ACL 2025, aclanthology.org/2025.acl-long.762)",
    "Continually Adding New Languages to Multilingual Language Models / LayRA (arXiv:2509.11414, September 2025)",
    "Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)",
    "AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)",
    "CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)",
    "Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)",
    "Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)",
    "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)",
    "LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)",
    "XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)",
    "Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)",
    "Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)"
  ],
  "description": "Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\n\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\n\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on held-out splits of CulturalBench (ACL 2025, publicly available for training use); SemEval-2026 Task 7 data (BLEnD) reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\n\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). The cultural-preservation objective remains the categorical novelty absent from both. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks."
}

## Reviewer feedback (round 6)
Issues: ["CRITICAL — CulturalBench is not available for training use. The paper claims Stage 2 cultural-localization probes are trained on 'held-out splits of CulturalBench (ACL 2025)...which is publicly available for training use.' This is factually wrong: the CulturalBench paper explicitly states 'our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.' Using CulturalBench for probe training violates its terms. The Stage 2 probe training data source must be replaced with a training-permitted cultural knowledge resource (e.g., multilingual Wikipedia cultural-domain sentences, MKQA, World Values Survey items, or a custom culturally-grounded QA dataset without OpenAI annotation-platform restrictions). SemEval-2026 Task 7 (BLEnD) is correctly identified as evaluation-only and is not the issue here.", "MINOR — Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, updated Feb 2026) applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters) and achieves strong cross-lingual alignment while preserving general capabilities, with adaptation concentrated in down-projection weights of later layers. Although its objective (language performance improvement) differs from CLS-LoRA's (cultural preservation), the layer-selective sparse-fine-tuning approach is closely related and should be acknowledged in the landscape section to preempt reviewer comparisons."]
Feedback: Round 6 resolves all three Round 5 issues cleanly (XCOPA/XStoryCloze/MGSM added, 2×2 ablation with condition (b) included, Stage 1 separate-probe protocol specified). One critical correction remains before this can pass review:

**Fix the CulturalBench training-use claim (critical, ~2 hours of work).** The CulturalBench paper explicitly states the dataset is prohibited from training use due to its OpenAI annotation-platform terms. Replace the Stage 2 cultural-localization probe training source with a dataset that permits training. Strong alternatives: (a) multilingual Wikipedia paragraphs from culture-specific articles, filtered by Wikidata cultural-domain tags — widely available, CC-BY licensed, and covers the 45+ cultural regions needed; (b) MKQA (multilingual knowledge questions, Apache 2.0), which covers culturally-grounded factual questions across languages; (c) a small GPT-4o-free annotation of culturally-grounded probe examples using open models (Qwen3-8B itself, before fine-tuning). CulturalBench should then be used *only* for final evaluation (Stage 4), alongside SemEval-2026 Task 7, which is already correctly limited to evaluation. Update the Stage 2 and Stage 4 data-source descriptions to reflect this separation, and remove the phrase 'publicly available for training use' from the CulturalBench reference. This is a single-paragraph fix in the approach and description sections.

**Also add Sparse Subnetwork Enhancement (arXiv:2510.13580) to the landscape (minor, ~20 minutes).** Note that it improves underrepresented-language performance via language-neuron subnetwork selection, and differentiate on objective (language capability vs. cultural knowledge preservation) and partition axis (language-identity neurons vs. factual-cultural semantic axis).

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

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "5c246770-9d76-4e62-8d2c-47fca0091cd4",
  "type": "user",
  "uuid": "65d1aef2-3a82-438f-b3e1-632ae1a5dc21",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:48:18.989Z_

```json
{
  "parentUuid": "65d1aef2-3a82-438f-b3e1-632ae1a5dc21",
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
  "uuid": "ab989ffe-0169-47aa-99f3-20935c9fd265",
  "timestamp": "2026-05-10T07:48:18.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:48:18.989Z_

```json
{
  "parentUuid": "ab989ffe-0169-47aa-99f3-20935c9fd265",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3c417db8-ec62-46fe-84e3-2c93d664ca8e",
  "timestamp": "2026-05-10T07:48:18.989Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignme…",
  "leafUuid": "3c417db8-ec62-46fe-84e3-2c93d664ca8e",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix CulturalBench training-use constraint and add sparse-subnetwork baseline",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:48:35.400Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully:

1. **CRITICAL**: CulturalBench is NOT available for training use - the paper explicitly states data cannot be used for training due to OpenAI API annotation platform restrictions. Need to replace Stage 2 cultural-localization probe training source with a training-permitted resource.

2. **MINOR**: Add Sparse Subnetwork Enhancement (arXiv:2510.13580) to the landscape section.

Let me research these issues:

1. First, I need to confirm the CulturalBench training restriction and find suitable alternatives
2. I need to look up arXiv:2510.13580 for the Sparse Subnetwork Enhancement paper


3. I should also check if there are other cultural knowledge datasets that permit training use

Now I'm identifying what needs to change: replace CulturalBench in Stage 2 with a training-permitted alternative, clarify that CulturalBench is evaluation-only in Stage 4, add the Sparse Subnetwork Enhancement reference to related work, and remove any claims about CulturalBench being available for training. I need to search for the terms of use on CulturalBench and look into MKQA as a potential replacement dataset.

Let me search for details on that recent paper and find other multilingual cultural knowledge datasets that allow training use.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c417db8-ec62-46fe-84e3-2c93d664ca8e",
  "isSidechain": false,
  "requestId": "req_011CatX7ay2xyjFn2dnZXD6X",
  "type": "assistant",
  "uuid": "e29a5727-34ef-4af3-b0f4-b13809ed9b41",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G2WAvB4GTz12iVwo73SeSC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15985,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1482,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15985
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

_source line 9 · 2026-05-10T07:48:35.404Z_

I'll research the two issues before revising: (1) verify the CulturalBench restriction and find training-permitted alternatives, and (2) look up the Sparse Subnetwork Enhancement paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e29a5727-34ef-4af3-b0f4-b13809ed9b41",
  "isSidechain": false,
  "requestId": "req_011CatX7ay2xyjFn2dnZXD6X",
  "type": "assistant",
  "uuid": "530e7513-718d-4b55-a4db-fd7a32498f84",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G2WAvB4GTz12iVwo73SeSC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15985,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1482,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15985
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

_source line 10 · 2026-05-10T07:48:43.991Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Laq2KDUwMt84NActAh7Eku`</summary>

```json
{
  "description": "Research CulturalBench training restrictions and alternatives",
  "subagent_type": "general-purpose",
  "prompt": "I need to research two things for a research paper revision:\n\n1. **CulturalBench license/terms**: The paper at ACL 2025 about CulturalBench (a cultural knowledge benchmark with 1,696 human-verified questions across 45 global regions) allegedly has a clause prohibiting training use because it was annotated using OpenAI APIs. Please:\n   - Search for \"CulturalBench dataset license training\" to find the official terms\n   - Try to fetch the CulturalBench paper abstract: https://arxiv.org/abs/2404.15238 (this might be the right arxiv ID - search if needed)\n   - Check if there's a HuggingFace page for CulturalBench and note any license restrictions\n   - Search for \"CulturalBench OpenAI annotation training prohibited\"\n\n2. **Alternative training-permitted cultural knowledge datasets**: I need training-permitted multilingual cultural knowledge datasets that could be used to train linear probes for detecting cultural knowledge in LLM layer activations. Please search for:\n   - MKQA dataset license (it should be Apache 2.0) - confirm it covers culturally-grounded questions across languages\n   - \"multilingual cultural knowledge dataset training permitted license\"\n   - \"multilingual Wikipedia cultural domain training data\"\n   - Any other cultural QA datasets that explicitly permit training use (not just evaluation)\n   - Look for datasets like CulturalX, GlobalOpinionQA, WorldValuesSurvey-derived datasets, or similar\n\n3. **arXiv:2510.13580** - \"Sparse Subnetwork Enhancement for Underrepresented Languages\" - please fetch and summarize:\n   - Fetch https://arxiv.org/abs/2510.13580 to get the full abstract and method description\n   - Note: key claims are that it applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters), achieves strong cross-lingual alignment while preserving general capabilities, and adaptation is concentrated in down-projection weights of later layers\n\nPlease provide concrete details including license types, dataset sizes, language coverage, and direct quotes from abstracts where relevant."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "530e7513-718d-4b55-a4db-fd7a32498f84",
  "isSidechain": false,
  "requestId": "req_011CatX7ay2xyjFn2dnZXD6X",
  "type": "assistant",
  "uuid": "419416b1-9aaf-4ca6-9aa6-1ca848e74bca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G2WAvB4GTz12iVwo73SeSC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15985,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1482,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15985
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

_source line 11 · 2026-05-10T07:48:49.747Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01R3exACCZyXmoBpBoLpyDiv`</summary>

```json
{
  "description": "Search for multilingual cultural probe datasets and recent related work",
  "subagent_type": "general-purpose",
  "prompt": "I'm revising a research paper on cultural knowledge preservation in multilingual LLMs. I need to find training-permitted datasets for cultural knowledge probing. Please search for:\n\n1. **CulturalBench ACL 2025**: Search for \"CulturalBench ACL 2025 cultural benchmark\" to find its paper and any license/terms info. The paper is about 1,696 culturally-grounded questions across 45 global regions. Check: https://arxiv.org/abs/2404.15238 or similar\n\n2. **MKQA dataset**: Fetch https://arxiv.org/abs/2007.15207 or search for \"MKQA multilingual knowledge questions Apache license\" to confirm:\n   - License (should be Apache 2.0)\n   - Coverage (how many languages, what question types)\n   - Whether it includes culturally-grounded factual questions\n\n3. **WorldValuesSurvey or similar culturally-rich datasets**: Search for:\n   - \"World Values Survey dataset NLP training\"\n   - \"GlobalOpinionQA dataset license\"\n   - \"multilingual cultural QA training dataset CC-BY OR Apache\"\n   - \"CulturalX dataset multilingual\" \n\n4. **Recent cultural probing work**: Search for any papers in 2024-2025 that train probes for cultural knowledge detection and what datasets they use for probe training (not just evaluation).\n\n5. Also check: Is there a \"BLEnD\" or \"SemEval-2026 Task 7\" dataset for cultural knowledge - what are its terms?\n\nProvide dataset names, licenses, language counts, and any relevant URLs/arxiv IDs."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "419416b1-9aaf-4ca6-9aa6-1ca848e74bca",
  "isSidechain": false,
  "requestId": "req_011CatX7ay2xyjFn2dnZXD6X",
  "type": "assistant",
  "uuid": "683864d2-0c34-47f9-9bf1-6c666d3292d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01G2WAvB4GTz12iVwo73SeSC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15985,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1482,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 15985,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1482,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 15985,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 15985
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

_source line 12 · 2026-05-10T07:51:21.162Z_

<details><summary>↩ Tool result · `toolu_01Laq2KDUwMt84NActAh7Eku`</summary>

```text
I now have comprehensive information across all three research areas. Here is the full report:

---

## 1. CulturalBench — License, Terms, and Training Restriction

**Correct arXiv ID:** The paper is at arXiv:2410.02677 (not 2404.15238). Full title: "CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming."

**Authors:** Yu Ying Chiu, Liwei Jiang, Bill Yuchen Lin, Chan Young Park, Shuyue Stella Li, Sahithya Ravi, Mehar Bhatia, Maria Antoniak, Yulia Tsvetkov, Vered Shwartz, Yejin Choi.

**Dataset facts:**
- 1,696 human-written and human-verified questions (the HuggingFace card lists 1,227 in Easy format + 4,908 binary judgments in Hard format = 6,135 rows total)
- 45 global regions, 17 topic categories
- Human accuracy: 92.4–92.6%; best LLM (GPT-4o): 61.5% on Hard; worst (Llama3-8b): 21.4%

**Training restriction — confirmed with exact quote.** The paper's HTML (arXiv:2410.02677v2) states explicitly:

> "our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training."

**Official license:** CC-BY-4.0 — released publicly at [huggingface.co/datasets/kellycyy/CulturalBench](https://huggingface.co/datasets/kellycyy/CulturalBench). The CC-BY-4.0 license itself permits training use, but the OpenAI API usage terms during annotation create a contractual prohibition on training use, overriding what CC-BY-4.0 would otherwise allow. This means CulturalBench is **evaluation-only** in practice due to the API terms of service constraint.

**Annotation methodology:** 3-stage pipeline — (1) Human-AI red-teaming question generation using GPT-4o, (2) human quality verification by 5 independent annotators from the target region, (3) majority-vote filtering requiring ≥4/5 agreement.

---

## 2. Alternative Training-Permitted Cultural Knowledge Datasets

### MKQA (Multilingual Knowledge Questions and Answers)
- **License:** CC-BY-SA 3.0 (not Apache 2.0 — this needs to be corrected in your paper)
- **Size:** 10,000 Q&A pairs × 26 languages = 260,000 total pairs
- **Languages:** Arabic, Chinese (3 variants), Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Khmer, Korean, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Vietnamese
- **Important caveat for your use case:** MKQA explicitly notes that "a large majority of these queries are geographically invariant, meaning that their answer is not culturally or geographically dependent (less than 4% of answers are rendered incorrect by geographical and cultural context)." Questions are translated from Google Natural Questions (English-origin), not independently sourced per language. This makes it a weak proxy for cultural knowledge specifically.
- **Training use:** Permitted under CC-BY-SA 3.0 (with ShareAlike conditions)
- Source: [github.com/apple/ml-mkqa](https://github.com/apple/ml-mkqa), [huggingface.co/datasets/apple/mkqa](https://huggingface.co/datasets/apple/mkqa)

### TyDi QA
- **License:** Apache 2.0 (confirmed via Google Research Datasets)
- **Size:** ~200,000 human-annotated Q&A pairs in 11 typologically diverse languages
- **Languages:** Arabic, Bengali, Finnish, Indonesian, Japanese, Korean, Russian, Swahili, Telugu, Thai, English
- **Cultural grounding:** Stronger than MKQA — questions written natively in each language without translation, capturing language-specific information needs
- **Training use:** Fully permitted
- Source: [github.com/google-research-datasets/tydiqa](https://github.com/google-research-datasets/tydiqa)

### GlobalOpinionQA (Durmus et al., 2023 / Anthropic)
- **License:** CC-BY-NC-SA 4.0 — the NonCommercial clause means **training for commercial use is prohibited**; academic/research training may be permissible depending on interpretation
- **Size:** 1K–10K samples
- **Content:** Subjective opinion questions adapted from World Values Survey (WVS) and Pew Global Attitudes Survey (GAS); response distributions by country
- **Language:** English only (questions in English, but country-level response distributions)
- **Caveat:** Covers opinion/values, not factual cultural knowledge; English-only
- Source: [huggingface.co/datasets/Anthropic/llm_global_opinions](https://huggingface.co/datasets/Anthropic/llm_global_opinions)

### WorldValuesBench
- **License:** Restricted — raw WVS data cannot be redistributed; users must request access directly from [worldvaluessurvey.org](https://www.worldvaluessurvey.org/). The derived benchmark (arXiv:2404.16308) has 20M+ examples from 94,728 WVS participants across 64 countries/societies. **Not freely redistributable for training.**

### CulturaX
- **License:** Inherits from source datasets (mC4 + OSCAR corpora); requires user authentication and consent form on HuggingFace; not a single clean license
- **Size:** 6.3 trillion tokens, 16 TB, 167 languages, 3.2B+ documents
- **Content:** General web text (CommonCrawl-derived), not curated cultural knowledge QA
- **Training use:** Permitted with consent agreement; appropriate for pretraining but not targeted cultural QA training
- Source: [huggingface.co/datasets/uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)

### Belebele (Meta)
- **License:** CC-BY-SA 4.0 (reading comprehension passages); note the training portion is CC-BY-NC in parts
- **Size:** 122 language variants, parallel reading comprehension
- **Training use:** Evaluation-focused; NC clause in training split limits use
- Source: [github.com/facebookresearch/belebele](https://github.com/facebookresearch/belebele)

### SIB-200
- **License:** CC-BY-SA 4.0
- **Size:** 205 languages/dialects; topic classification dataset based on Flores-200
- **Training use:** Permitted under CC-BY-SA 4.0
- **Note:** Topic classification, not cultural knowledge QA per se

### Wikipedia (via Wikimedia dumps)
- **License:** CC-BY-SA 4.0 (text); fully open
- **Relevance:** The strongest openly licensed source of cultural domain knowledge across many languages. Wikipedia articles are organized by cultural domain (cuisine, history, customs, religion, geography), making language-filtered Wikipedia dumps useful for training cultural knowledge probes. Commonly used as a base for cultural QA dataset construction.

### Common Corpus (Pleias)
- **License:** Fully permissive/open, documented provenance
- **Size:** 2+ trillion tokens; 30+ languages with ≥1B tokens each
- **Content:** Scientific articles, government/legal documents, code, cultural heritage (books, newspapers)
- **Training use:** Explicitly designed for LLM training with full permission
- Source: [thealliance.ai/blog/pleias-releases-common-corpus](https://thealliance.ai/blog/pleias-releases-common-corpus-open-multilingual-dataset-for-llm-training)

**Summary recommendation for linear probe training:** TyDi QA (Apache 2.0, natively multilingual, 200K pairs) is the cleanest choice for training-permitted multilingual QA with some cultural grounding. For pure cultural knowledge, language-filtered Wikipedia dumps (CC-BY-SA 4.0) are the most defensible large-scale option. MKQA (CC-BY-SA 3.0) can be used but is largely geographically invariant. GlobalOpinionQA's NC clause makes it unsuitable if the research has any commercial downstream path.

---

## 3. arXiv:2510.13580 — "Sparse Subnetwork Enhancement for Underrepresented Languages"

**Full title:** "Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models"

**Authors:** Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, Simon Ostermann

**Abstract (paraphrased with key quotes):** The paper proposes targeted fine-tuning of "sparse, language-associated subnetworks" identified using Language Activation Probability Entropy (LAPE), described as "an information-theoretic metric that reliably captures language-specific activation patterns." The method updates only 0.2–1% of model parameters while outperforming full fine-tuning, LoRA, IA3, and random-subset baselines across 12 mid- and low-resource languages. Models tested: Llama-3.1-8B, Mistral-Nemo-12B, Aya-Expanse-8B. The authors release language neuron sets for 100+ languages.

**Parameter efficiency (exact figures):**
- Llama-3.1-8B: 0.18% (Georgian) to 0.92% (Welsh) of parameters modified
- General range: 0.2–1% across all models

**Down-projection finding (directly relevant to your claim):** The paper's mechanistic analysis finds that "down_proj exhibits substantially larger weight changes, particularly in later layers," with changes being "3–5× larger than up/gate projections in later layers." The interpretation given is that down-projections serve as "the primary site of linguistic re-wiring during adaptation," while gate and up projections "jointly create a gated feature space" with smaller, more clustered changes, suggesting they perform "re-weighting" rather than fundamental restructuring. Language-specific neurons concentrate in upper layers.

**Cross-lingual alignment results:**
- Sparse (language neuron) fine-tuning: **90.5%** average cosine similarity
- Random-subset fine-tuning: 87.7%
- LoRA: 87.5%
- Full fine-tuning: 87.3% (worst, despite updating all parameters)

**Benchmark results (Llama-3.1-8B, avg. across 12 languages):**

| Method | FLORES | BELEBELE | SIB-200 | Avg. |
|---|---|---|---|---|
| Base | 28.82 | 66.52 | 40.89 | 29.56 |
| Full FT | 11.44 | 21.22 | 11.23 | 11.88 |
| FFN FT | 25.06 | 38.35 | 21.65 | 21.81 |
| LoRA | 28.00 | 56.61 | 33.37 | 28.41 |
| IA3 | 29.61 | 64.33 | 42.20 | 30.05 |
| Random N-s | 30.95 | 59.82 | 34.07 | 29.89 |
| **Lang. N-s (proposed)** | **31.37** | **66.84** | **44.94** | **33.02** |

**General capability preservation (MMLU):**
- Base: 63.08%
- Sparse FT: 63.01% (near-perfect preservation)
- Full FT: 25.50% (catastrophic forgetting)
- LoRA: 56.10% (notable degradation)

**Verification of your paper's claims:** All three key claims check out: (1) <1% parameter modification (confirmed: 0.2–1%); (2) strong cross-lingual alignment (90.5% cosine similarity, best of all methods); (3) adaptation concentrated in down-projection weights of later layers (3–5× larger weight changes vs. up/gate projections, concentrated in upper layers).

---

Sources:
- [CulturalBench arXiv:2410.02677v2](https://arxiv.org/html/2410.02677v2)
- [CulturalBench HuggingFace Dataset](https://huggingface.co/datasets/kellycyy/CulturalBench)
- [arXiv:2510.13580 (Sparse Subnetwork Enhancement)](https://arxiv.org/abs/2510.13580)
- [MKQA GitHub (Apple)](https://github.com/apple/ml-mkqa)
- [MKQA HuggingFace](https://huggingface.co/datasets/apple/mkqa)
- [TyDi QA GitHub](https://github.com/google-research-datasets/tydiqa)
- [GlobalOpinionQA HuggingFace](https://huggingface.co/datasets/Anthropic/llm_global_opinions)
- [WorldValuesBench arXiv:2404.16308](https://arxiv.org/abs/2404.16308)
- [CulturaX HuggingFace](https://huggingface.co/datasets/uonlp/CulturaX)
- [Belebele GitHub](https://github.com/facebookresearch/belebele)
- [SIB-200 arXiv](https://arxiv.org/abs/2309.07445)
- [Common Corpus announcement](https://thealliance.ai/blog/pleias-releases-common-corpus-open-multilingual-dataset-for-llm-training)
- [Demystifying OpenAI Terms re: Dataset Licenses](https://erichartford.com/demystifying-openais-terms-of-use-with-regards-to-dataset-licenses)

agentId: a6dc5c6454eb2045c (use SendMessage with to: 'a6dc5c6454eb2045c' to continue this agent)
&lt;usage>total_tokens: 29778
tool_uses: 19
duration_ms: 157165&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "419416b1-9aaf-4ca6-9aa6-1ca848e74bca",
  "isSidechain": false,
  "promptId": "5c246770-9d76-4e62-8d2c-47fca0091cd4",
  "type": "user",
  "uuid": "bba48180-a45e-449b-a03e-fe8302e09d6b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research two things for a research paper revision:\n\n1. **CulturalBench license/terms**: The paper at ACL 2025 about CulturalBench (a cultural knowledge benchmark with 1,696 human-verified questions across 45 global regions) allegedly has a clause prohibiting training use because it was annotated using OpenAI APIs. Please:\n   - Search for \"CulturalBench dataset license training\" to find the official terms\n   - Try to fetch the CulturalBench paper abstract: https://arxiv.org/abs/2404.15238 (this might be the right arxiv ID - search if needed)\n   - Check if there's a HuggingFace page for CulturalBench and note any license restrictions\n   - Search for \"CulturalBench OpenAI annotation training prohibited\"\n\n2. **Alternative training-permitted cultural knowledge datasets**: I need training-permitted multilingual cultural knowledge datasets that could be used to train linear probes for detecting cultural knowledge in LLM layer activations. Please search for:\n   - MKQA dataset license (it should be Apache 2.0) - confirm it covers culturally-grounded questions across languages\n   - \"multilingual cultural knowledge dataset training permitted license\"\n   - \"multilingual Wikipedia cultural domain training data\"\n   - Any other cultural QA datasets that explicitly permit training use (not just evaluation)\n   - Look for datasets like CulturalX, GlobalOpinionQA, WorldValuesSurvey-derived datasets, or similar\n\n3. **arXiv:2510.13580** - \"Sparse Subnetwork Enhancement for Underrepresented Languages\" - please fetch and summarize:\n   - Fetch https://arxiv.org/abs/2510.13580 to get the full abstract and method description\n   - Note: key claims are that it applies targeted sparse fine-tuning of language-associated subnetworks (<1% of parameters), achieves strong cross-lingual alignment while preserving general capabilities, and adaptation is concentrated in down-projection weights of later layers\n\nPlease provide concrete details including license types, dataset sizes, language coverage, and direct quotes from abstracts where relevant.",
    "agentId": "a6dc5c6454eb2045c",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information across all three research areas. Here is the full report:\n\n---\n\n## 1. CulturalBench — License, Terms, and Training Restriction\n\n**Correct arXiv ID:** The paper is at arXiv:2410.02677 (not 2404.15238). Full title: \"CulturalBench: A Robust, Diverse, and Challenging Cultural Benchmark by Human-AI CulturalTeaming.\"\n\n**Authors:** Yu Ying Chiu, Liwei Jiang, Bill Yuchen Lin, Chan Young Park, Shuyue Stella Li, Sahithya Ravi, Mehar Bhatia, Maria Antoniak, Yulia Tsvetkov, Vered Shwartz, Yejin Choi.\n\n**Dataset facts:**\n- 1,696 human-written and human-verified questions (the HuggingFace card lists 1,227 in Easy format + 4,908 binary judgments in Hard format = 6,135 rows total)\n- 45 global regions, 17 topic categories\n- Human accuracy: 92.4–92.6%; best LLM (GPT-4o): 61.5% on Hard; worst (Llama3-8b): 21.4%\n\n**Training restriction — confirmed with exact quote.** The paper's HTML (arXiv:2410.02677v2) states explicitly:\n\n> \"our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training.\"\n\n**Official license:** CC-BY-4.0 — released publicly at [huggingface.co/datasets/kellycyy/CulturalBench](https://huggingface.co/datasets/kellycyy/CulturalBench). The CC-BY-4.0 license itself permits training use, but the OpenAI API usage terms during annotation create a contractual prohibition on training use, overriding what CC-BY-4.0 would otherwise allow. This means CulturalBench is **evaluation-only** in practice due to the API terms of service constraint.\n\n**Annotation methodology:** 3-stage pipeline — (1) Human-AI red-teaming question generation using GPT-4o, (2) human quality verification by 5 independent annotators from the target region, (3) majority-vote filtering requiring ≥4/5 agreement.\n\n---\n\n## 2. Alternative Training-Permitted Cultural Knowledge Datasets\n\n### MKQA (Multilingual Knowledge Questions and Answers)\n- **License:** CC-BY-SA 3.0 (not Apache 2.0 — this needs to be corrected in your paper)\n- **Size:** 10,000 Q&A pairs × 26 languages = 260,000 total pairs\n- **Languages:** Arabic, Chinese (3 variants), Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Khmer, Korean, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Vietnamese\n- **Important caveat for your use case:** MKQA explicitly notes that \"a large majority of these queries are geographically invariant, meaning that their answer is not culturally or geographically dependent (less than 4% of answers are rendered incorrect by geographical and cultural context).\" Questions are translated from Google Natural Questions (English-origin), not independently sourced per language. This makes it a weak proxy for cultural knowledge specifically.\n- **Training use:** Permitted under CC-BY-SA 3.0 (with ShareAlike conditions)\n- Source: [github.com/apple/ml-mkqa](https://github.com/apple/ml-mkqa), [huggingface.co/datasets/apple/mkqa](https://huggingface.co/datasets/apple/mkqa)\n\n### TyDi QA\n- **License:** Apache 2.0 (confirmed via Google Research Datasets)\n- **Size:** ~200,000 human-annotated Q&A pairs in 11 typologically diverse languages\n- **Languages:** Arabic, Bengali, Finnish, Indonesian, Japanese, Korean, Russian, Swahili, Telugu, Thai, English\n- **Cultural grounding:** Stronger than MKQA — questions written natively in each language without translation, capturing language-specific information needs\n- **Training use:** Fully permitted\n- Source: [github.com/google-research-datasets/tydiqa](https://github.com/google-research-datasets/tydiqa)\n\n### GlobalOpinionQA (Durmus et al., 2023 / Anthropic)\n- **License:** CC-BY-NC-SA 4.0 — the NonCommercial clause means **training for commercial use is prohibited**; academic/research training may be permissible depending on interpretation\n- **Size:** 1K–10K samples\n- **Content:** Subjective opinion questions adapted from World Values Survey (WVS) and Pew Global Attitudes Survey (GAS); response distributions by country\n- **Language:** English only (questions in English, but country-level response distributions)\n- **Caveat:** Covers opinion/values, not factual cultural knowledge; English-only\n- Source: [huggingface.co/datasets/Anthropic/llm_global_opinions](https://huggingface.co/datasets/Anthropic/llm_global_opinions)\n\n### WorldValuesBench\n- **License:** Restricted — raw WVS data cannot be redistributed; users must request access directly from [worldvaluessurvey.org](https://www.worldvaluessurvey.org/). The derived benchmark (arXiv:2404.16308) has 20M+ examples from 94,728 WVS participants across 64 countries/societies. **Not freely redistributable for training.**\n\n### CulturaX\n- **License:** Inherits from source datasets (mC4 + OSCAR corpora); requires user authentication and consent form on HuggingFace; not a single clean license\n- **Size:** 6.3 trillion tokens, 16 TB, 167 languages, 3.2B+ documents\n- **Content:** General web text (CommonCrawl-derived), not curated cultural knowledge QA\n- **Training use:** Permitted with consent agreement; appropriate for pretraining but not targeted cultural QA training\n- Source: [huggingface.co/datasets/uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)\n\n### Belebele (Meta)\n- **License:** CC-BY-SA 4.0 (reading comprehension passages); note the training portion is CC-BY-NC in parts\n- **Size:** 122 language variants, parallel reading comprehension\n- **Training use:** Evaluation-focused; NC clause in training split limits use\n- Source: [github.com/facebookresearch/belebele](https://github.com/facebookresearch/belebele)\n\n### SIB-200\n- **License:** CC-BY-SA 4.0\n- **Size:** 205 languages/dialects; topic classification dataset based on Flores-200\n- **Training use:** Permitted under CC-BY-SA 4.0\n- **Note:** Topic classification, not cultural knowledge QA per se\n\n### Wikipedia (via Wikimedia dumps)\n- **License:** CC-BY-SA 4.0 (text); fully open\n- **Relevance:** The strongest openly licensed source of cultural domain knowledge across many languages. Wikipedia articles are organized by cultural domain (cuisine, history, customs, religion, geography), making language-filtered Wikipedia dumps useful for training cultural knowledge probes. Commonly used as a base for cultural QA dataset construction.\n\n### Common Corpus (Pleias)\n- **License:** Fully permissive/open, documented provenance\n- **Size:** 2+ trillion tokens; 30+ languages with ≥1B tokens each\n- **Content:** Scientific articles, government/legal documents, code, cultural heritage (books, newspapers)\n- **Training use:** Explicitly designed for LLM training with full permission\n- Source: [thealliance.ai/blog/pleias-releases-common-corpus](https://thealliance.ai/blog/pleias-releases-common-corpus-open-multilingual-dataset-for-llm-training)\n\n**Summary recommendation for linear probe training:** TyDi QA (Apache 2.0, natively multilingual, 200K pairs) is the cleanest choice for training-permitted multilingual QA with some cultural grounding. For pure cultural knowledge, language-filtered Wikipedia dumps (CC-BY-SA 4.0) are the most defensible large-scale option. MKQA (CC-BY-SA 3.0) can be used but is largely geographically invariant. GlobalOpinionQA's NC clause makes it unsuitable if the research has any commercial downstream path.\n\n---\n\n## 3. arXiv:2510.13580 — \"Sparse Subnetwork Enhancement for Underrepresented Languages\"\n\n**Full title:** \"Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models\"\n\n**Authors:** Daniil Gurgurov, Tanja Baeumel, Josef van Genabith, Simon Ostermann\n\n**Abstract (paraphrased with key quotes):** The paper proposes targeted fine-tuning of \"sparse, language-associated subnetworks\" identified using Language Activation Probability Entropy (LAPE), described as \"an information-theoretic metric that reliably captures language-specific activation patterns.\" The method updates only 0.2–1% of model parameters while outperforming full fine-tuning, LoRA, IA3, and random-subset baselines across 12 mid- and low-resource languages. Models tested: Llama-3.1-8B, Mistral-Nemo-12B, Aya-Expanse-8B. The authors release language neuron sets for 100+ languages.\n\n**Parameter efficiency (exact figures):**\n- Llama-3.1-8B: 0.18% (Georgian) to 0.92% (Welsh) of parameters modified\n- General range: 0.2–1% across all models\n\n**Down-projection finding (directly relevant to your claim):** The paper's mechanistic analysis finds that \"down_proj exhibits substantially larger weight changes, particularly in later layers,\" with changes being \"3–5× larger than up/gate projections in later layers.\" The interpretation given is that down-projections serve as \"the primary site of linguistic re-wiring during adaptation,\" while gate and up projections \"jointly create a gated feature space\" with smaller, more clustered changes, suggesting they perform \"re-weighting\" rather than fundamental restructuring. Language-specific neurons concentrate in upper layers.\n\n**Cross-lingual alignment results:**\n- Sparse (language neuron) fine-tuning: **90.5%** average cosine similarity\n- Random-subset fine-tuning: 87.7%\n- LoRA: 87.5%\n- Full fine-tuning: 87.3% (worst, despite updating all parameters)\n\n**Benchmark results (Llama-3.1-8B, avg. across 12 languages):**\n\n| Method | FLORES | BELEBELE | SIB-200 | Avg. |\n|---|---|---|---|---|\n| Base | 28.82 | 66.52 | 40.89 | 29.56 |\n| Full FT | 11.44 | 21.22 | 11.23 | 11.88 |\n| FFN FT | 25.06 | 38.35 | 21.65 | 21.81 |\n| LoRA | 28.00 | 56.61 | 33.37 | 28.41 |\n| IA3 | 29.61 | 64.33 | 42.20 | 30.05 |\n| Random N-s | 30.95 | 59.82 | 34.07 | 29.89 |\n| **Lang. N-s (proposed)** | **31.37** | **66.84** | **44.94** | **33.02** |\n\n**General capability preservation (MMLU):**\n- Base: 63.08%\n- Sparse FT: 63.01% (near-perfect preservation)\n- Full FT: 25.50% (catastrophic forgetting)\n- LoRA: 56.10% (notable degradation)\n\n**Verification of your paper's claims:** All three key claims check out: (1) <1% parameter modification (confirmed: 0.2–1%); (2) strong cross-lingual alignment (90.5% cosine similarity, best of all methods); (3) adaptation concentrated in down-projection weights of later layers (3–5× larger weight changes vs. up/gate projections, concentrated in upper layers).\n\n---\n\nSources:\n- [CulturalBench arXiv:2410.02677v2](https://arxiv.org/html/2410.02677v2)\n- [CulturalBench HuggingFace Dataset](https://huggingface.co/datasets/kellycyy/CulturalBench)\n- [arXiv:2510.13580 (Sparse Subnetwork Enhancement)](https://arxiv.org/abs/2510.13580)\n- [MKQA GitHub (Apple)](https://github.com/apple/ml-mkqa)\n- [MKQA HuggingFace](https://huggingface.co/datasets/apple/mkqa)\n- [TyDi QA GitHub](https://github.com/google-research-datasets/tydiqa)\n- [GlobalOpinionQA HuggingFace](https://huggingface.co/datasets/Anthropic/llm_global_opinions)\n- [WorldValuesBench arXiv:2404.16308](https://arxiv.org/abs/2404.16308)\n- [CulturaX HuggingFace](https://huggingface.co/datasets/uonlp/CulturaX)\n- [Belebele GitHub](https://github.com/facebookresearch/belebele)\n- [SIB-200 arXiv](https://arxiv.org/abs/2309.07445)\n- [Common Corpus announcement](https://thealliance.ai/blog/pleias-releases-common-corpus-open-multilingual-dataset-for-llm-training)\n- [Demystifying OpenAI Terms re: Dataset Licenses](https://erichartford.com/demystifying-openais-terms-of-use-with-regards-to-dataset-licenses)"
      }
    ],
    "totalDurationMs": 157165,
    "totalTokens": 29778,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 1090,
      "cache_creation_input_tokens": 1721,
      "cache_read_input_tokens": 23480,
      "output_tokens": 3487,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1721
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1090,
          "output_tokens": 3487,
          "cache_read_input_tokens": 23480,
          "cache_creation_input_tokens": 1721,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1721,
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
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "419416b1-9aaf-4ca6-9aa6-1ca848e74bca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignme…",
  "leafUuid": "bba48180-a45e-449b-a03e-fe8302e09d6b",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix CulturalBench training-use constraint and add sparse-subnetwork baseline",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Tool result

_source line 15 · 2026-05-10T07:51:33.762Z_

<details><summary>↩ Tool result · `toolu_01R3exACCZyXmoBpBoLpyDiv`</summary>

```text
I now have comprehensive data across all five research areas. Here is the full report:

---

## Cultural Knowledge Datasets for Multilingual LLM Research: Licenses, Coverage, and Usability

---

### 1. CulturalBench (ACL 2025)

- **Full title:** "CulturalBench: A Robust, Diverse and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming"
- **ArXiv ID:** [2410.02677](https://arxiv.org/abs/2410.02677) (note: the correct ID is 2410.02677, not 2404.15238 as initially referenced)
- **Venue:** ACL 2025 (63rd Annual Meeting, Vienna)
- **Dataset size:** 1,696 human-written and human-verified questions (your figure was correct; some sources cite 1,227, but the v2 paper confirms 1,696)
- **Geographic coverage:** 45 global regions, including underrepresented ones like Bangladesh, Zimbabwe, and Peru
- **Topic categories:** 17 diverse topics (food preferences, greeting etiquette, and more)
- **License:** CC BY 4.0 — permits sharing, adaptation, and use in training with attribution
- **Evaluation design:** Two setups — CulturalBench-Easy and CulturalBench-Hard (same questions, different framing). Best model accuracy on Hard: 28.7–61.5% (vs. 92.4% human)
- **Training use:** The dataset is framed primarily as an evaluation benchmark, but the CC BY 4.0 license does not restrict training use
- **ACL Anthology:** [https://aclanthology.org/2025.acl-long.1247/](https://aclanthology.org/2025.acl-long.1247/)

---

### 2. MKQA (Multilingual Knowledge Questions and Answers)

- **Full title:** "MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering"
- **ArXiv ID:** [2007.15207](https://arxiv.org/abs/2007.15207)
- **Published in:** Transactions of the Association for Computational Linguistics (TACL)
- **GitHub:** [https://github.com/apple/ml-mkqa](https://github.com/apple/ml-mkqa) (maintained by Apple ML)
- **License:** CC BY-SA 3.0 (Creative Commons Attribution-ShareAlike 3.0) — NOT Apache 2.0 as sometimes reported; verify via the [official README](https://github.com/apple/ml-mkqa/blob/main/README.md)
- **Size:** 10,000 question-answer pairs per language; 260,000 total pairs across 26 languages
- **Languages (26):** Arabic, Chinese (Simplified, Hong Kong, Traditional), Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Khmer, Korean, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Vietnamese
- **Question types:** 8 answer-type categories — Entity, Long answer, Unanswerable, Date, Number, Number with unit, Short phrase, Binary
- **Cultural grounding:** Questions are sampled from Google Natural Questions (primarily English/Western-oriented), then translated; the dataset is not specifically designed for culturally-grounded facts but does span cross-lingual factual QA
- **Training use:** No explicit evaluation-only restriction; the README does not prohibit training use
- **HuggingFace:** [https://huggingface.co/datasets/apple/mkqa](https://huggingface.co/datasets/apple/mkqa)

---

### 3. Culturally-Rich Datasets

#### GlobalOpinionQA (Anthropic/Durmus et al., 2023)
- **ArXiv:** [2306.16388](https://arxiv.org/abs/2306.16388)
- **HuggingFace:** [Anthropic/llm_global_opinions](https://huggingface.co/datasets/Anthropic/llm_global_opinions)
- **License:** CC BY-NC-SA 4.0 — non-commercial use only; derivatives must carry the same license; attribution required
- **Source data:** Questions drawn from the World Values Survey (WVS) and Pew Global Attitudes Survey
- **Format:** Country-level opinion distributions (not per-speaker labels); English-language questions only
- **Size:** 1K–10K samples
- **Cultural grounding:** High — covers subjective opinions on social, political, and ethical issues across many countries
- **Training restriction:** NC clause bars commercial training; academic probe training is permissible with attribution

#### CulturaX (Multilingual pre-training corpus)
- **ArXiv:** [2309.09400](https://arxiv.org/abs/2309.09400); published at LREC-COLING 2024
- **HuggingFace:** [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)
- **License:** Inherits from mC4 and OSCAR — effectively CC BY-NC 4.0 / restricted academic use; consult both parent dataset licenses before use
- **Size:** 6.3 trillion tokens across 167 languages
- **Purpose:** Pre-training corpus (not a QA or probing dataset); useful for training multilingual models but not structured for cultural probing
- **Training use:** Permitted for non-commercial research; check OSCAR and mC4 license pages carefully

#### WorldValuesBench (NLP adaptation of WVS)
- **ArXiv:** [2404.16308](https://arxiv.org/html/2404.16308v1)
- **GitHub:** [Demon702/WorldValuesBench](https://github.com/Demon702/WorldValuesBench)
- **Size:** 20+ million examples for multi-cultural value prediction
- **License/restriction:** Raw WVS data cannot be redistributed; users must download the raw WVS Wave 7 data themselves from [worldvaluessurvey.org](https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp) and run the processing pipeline. WVS permits non-profit use with registration only — not training-open in the usual sense
- **Training use:** Restricted; not freely redistributable; WVS license requires notification upon publication use

#### World Values Survey (WVS) itself
- **License:** Available without restrictions for not-for-profit purposes only; registration required; redistribution of raw data not permitted
- **NLP training use:** Not directly training-permitted without navigating WVS data agreement

---

### 4. Recent Cultural Probing Work (2024–2025) and Their Training Datasets

#### CultureLLM (NeurIPS 2024)
- **ArXiv:** [2402.10946](https://arxiv.org/abs/2402.10946)
- **GitHub:** [Scarelette/CultureLLM](https://github.com/Scarelette/CultureLLM)
- **Training approach:** Uses 50 WVS seed samples per culture, then applies semantic data augmentation to generate training data; fine-tunes culture-specific LLMs for 9 cultures
- **WVS topics used:** Social values, migration, security, science and technology, religious values, ethical values, political interest
- **Paper license:** CC BY 4.0; however, WVS seed data carries WVS's own restrictions (see above)
- **Training use:** Code and augmented data are shared, but WVS-derived seed data requires WVS agreement

#### INCLUDE (ICLR 2025)
- **ArXiv:** [2411.19799](https://arxiv.org/html/2411.19799v1)
- **License:** CC BY 4.0 — fully permissive for training use with attribution
- **Size:** 197,243 MCQA pairs from 1,926 local examinations
- **Coverage:** 44 written languages, 52 countries, 15 scripts
- **Cultural grounding:** High — sourced from regional educational, professional, and practical exams written by native speakers; not translated from English
- **Training use:** Explicitly permitted under CC BY 4.0; strongly suitable for probe training

#### Global MMLU (Cohere for AI, ACL 2025)
- **ArXiv:** [2412.03304](https://arxiv.org/abs/2412.03304)
- **HuggingFace:** [CohereForAI/Global-MMLU](https://huggingface.co/datasets/CohereForAI/Global-MMLU)
- **License:** Apache 2.0 — the most permissive option found; allows commercial and training use freely
- **Size:** ~600,000 questions across 42 languages (~14,300 per language)
- **Cultural grounding:** Moderate — includes cultural sensitivity annotations (Culturally Sensitive vs. Culturally Agnostic flags); 28% of questions flagged as requiring culturally sensitive knowledge
- **Training use:** Fully permitted; Apache 2.0 is unrestricted

---

### 5. BLEnD and SemEval-2026 Task 7

#### BLEnD (NeurIPS 2024 Datasets & Benchmarks Track)
- **ArXiv:** [2406.09948](https://arxiv.org/abs/2406.09948)
- **GitHub:** [nlee0212/BLEnD](https://github.com/nlee0212/BLEnD)
- **NeurIPS proceedings:** [https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets_and_Benchmarks_Track.html](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets_and_Benchmarks_Track.html)
- **License:** CC BY-SA 4.0 — permits training use with attribution and ShareAlike requirement
- **Size:** 52,600 question-answer pairs
- **Coverage:** 16 countries/regions, 13 languages including low-resource ones (Amharic, Assamese, Azerbaijani, Hausa, Sundanese)
- **Topic categories:** Food, sports, family, education, holidays/celebrations/leisure, work-life
- **Cultural grounding:** Very high — questions concern everyday life knowledge not found in Wikipedia; written by local annotators

#### SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures
- **ArXiv:** [2605.02601](https://arxiv.org/abs/2605.02601)
- **GitHub:** [BLEnD-SemEval2026/SemEval-2026-Task-7](https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7)
- **Codabench:** [https://www.codabench.org/competitions/10281/](https://www.codabench.org/competitions/10281/)
- **Relationship to BLEnD:** Task 7 is an extended version of BLEnD, expanding coverage to 30+ language-culture pairs (17 new pairs beyond the original 13)
- **License for Task 7 data:** Not yet explicitly published as of this writing
- **Training restriction:** Explicitly prohibited — the task rules state participants may not use the data for training, fine-tuning, few-shot learning, or any other form of model modification. The SemEval-2026 Task 7 data is evaluation-only by design

---

### Summary Table

| Dataset | License | Languages | Questions | Training-Permitted |
|---|---|---|---|---|
| CulturalBench (ACL 2025) | CC BY 4.0 | N/A (English MCQ) | 1,696 | Yes (license permits it) |
| MKQA | CC BY-SA 3.0 | 26 | 260,000 | Yes (no restriction stated) |
| GlobalOpinionQA | CC BY-NC-SA 4.0 | 1 (English) | 1K–10K | Non-commercial only |
| CulturaX | mC4 + OSCAR (NC) | 167 | 6.3T tokens | Non-commercial only |
| WorldValuesBench | WVS agreement required | Multi | 20M+ | Restricted (non-profit, no redistribution) |
| INCLUDE (ICLR 2025) | CC BY 4.0 | 44 | 197,243 | Yes |
| Global MMLU (ACL 2025) | Apache 2.0 | 42 | ~600,000 | Yes (fully open) |
| BLEnD (NeurIPS 2024) | CC BY-SA 4.0 | 13 | 52,600 | Yes |
| SemEval-2026 Task 7 | TBD | 30+ | TBD (BLEnD extension) | No — explicitly prohibited |
| CultureLLM training data | CC BY 4.0 (paper); WVS (seeds) | 9 cultures | Augmented from WVS | Partial (augmented data yes; seeds require WVS agreement) |

---

### Key Recommendation for Probe Training

The cleanest options for training cultural knowledge probes with no licensing friction are:

1. **Global MMLU** (Apache 2.0) — largest, 42 languages, culturally annotated
2. **INCLUDE** (CC BY 4.0) — highest cultural authenticity, sourced from local exams in 52 countries
3. **BLEnD** (CC BY-SA 4.0) — strongest everyday cultural grounding, 13 languages, NeurIPS 2024

Avoid SemEval-2026 Task 7 data for training (explicitly prohibited), and be cautious with GlobalOpinionQA (NC clause) and WorldValuesBench/WVS (requires data agreement and non-profit restriction).

Sources:
- [CulturalBench - ACL Anthology](https://aclanthology.org/2025.acl-long.1247/)
- [CulturalBench - arXiv 2410.02677](https://arxiv.org/abs/2410.02677)
- [MKQA - arXiv 2007.15207](https://arxiv.org/abs/2007.15207)
- [MKQA GitHub (Apple)](https://github.com/apple/ml-mkqa)
- [GlobalOpinionQA - arXiv 2306.16388](https://arxiv.org/abs/2306.16388)
- [GlobalOpinionQA - HuggingFace](https://huggingface.co/datasets/Anthropic/llm_global_opinions)
- [CulturaX - arXiv 2309.09400](https://arxiv.org/abs/2309.09400)
- [CulturaX - HuggingFace](https://huggingface.co/datasets/uonlp/CulturaX)
- [WorldValuesBench - arXiv 2404.16308](https://arxiv.org/html/2404.16308v1)
- [World Values Survey official documentation](https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp)
- [BLEnD - arXiv 2406.09948](https://arxiv.org/abs/2406.09948)
- [BLEnD GitHub](https://github.com/nlee0212/BLEnD)
- [BLEnD NeurIPS 2024 proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets_and_Benchmarks_Track.html)
- [SemEval-2026 Task 7 - arXiv 2605.02601](https://arxiv.org/abs/2605.02601)
- [SemEval-2026 Task 7 GitHub](https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7)
- [SemEval-2026 Task 7 Codabench](https://www.codabench.org/competitions/10281/)
- [INCLUDE - ICLR 2025 OpenReview](https://openreview.net/forum?id=k3gCieTXeY)
- [Global MMLU - arXiv 2412.03304](https://arxiv.org/abs/2412.03304)
- [Global MMLU - HuggingFace](https://huggingface.co/datasets/CohereForAI/Global-MMLU)
- [CultureLLM - arXiv 2402.10946](https://arxiv.org/abs/2402.10946)
- [CultureLLM GitHub](https://github.com/Scarelette/CultureLLM)

agentId: ae09ebb9391fb2f07 (use SendMessage with to: 'ae09ebb9391fb2f07' to continue this agent)
&lt;usage>total_tokens: 31399
tool_uses: 22
duration_ms: 164010&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "683864d2-0c34-47f9-9bf1-6c666d3292d4",
  "isSidechain": false,
  "promptId": "5c246770-9d76-4e62-8d2c-47fca0091cd4",
  "type": "user",
  "uuid": "9317d872-0f93-49e7-a853-98ee6196d21a",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm revising a research paper on cultural knowledge preservation in multilingual LLMs. I need to find training-permitted datasets for cultural knowledge probing. Please search for:\n\n1. **CulturalBench ACL 2025**: Search for \"CulturalBench ACL 2025 cultural benchmark\" to find its paper and any license/terms info. The paper is about 1,696 culturally-grounded questions across 45 global regions. Check: https://arxiv.org/abs/2404.15238 or similar\n\n2. **MKQA dataset**: Fetch https://arxiv.org/abs/2007.15207 or search for \"MKQA multilingual knowledge questions Apache license\" to confirm:\n   - License (should be Apache 2.0)\n   - Coverage (how many languages, what question types)\n   - Whether it includes culturally-grounded factual questions\n\n3. **WorldValuesSurvey or similar culturally-rich datasets**: Search for:\n   - \"World Values Survey dataset NLP training\"\n   - \"GlobalOpinionQA dataset license\"\n   - \"multilingual cultural QA training dataset CC-BY OR Apache\"\n   - \"CulturalX dataset multilingual\" \n\n4. **Recent cultural probing work**: Search for any papers in 2024-2025 that train probes for cultural knowledge detection and what datasets they use for probe training (not just evaluation).\n\n5. Also check: Is there a \"BLEnD\" or \"SemEval-2026 Task 7\" dataset for cultural knowledge - what are its terms?\n\nProvide dataset names, licenses, language counts, and any relevant URLs/arxiv IDs.",
    "agentId": "ae09ebb9391fb2f07",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive data across all five research areas. Here is the full report:\n\n---\n\n## Cultural Knowledge Datasets for Multilingual LLM Research: Licenses, Coverage, and Usability\n\n---\n\n### 1. CulturalBench (ACL 2025)\n\n- **Full title:** \"CulturalBench: A Robust, Diverse and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming\"\n- **ArXiv ID:** [2410.02677](https://arxiv.org/abs/2410.02677) (note: the correct ID is 2410.02677, not 2404.15238 as initially referenced)\n- **Venue:** ACL 2025 (63rd Annual Meeting, Vienna)\n- **Dataset size:** 1,696 human-written and human-verified questions (your figure was correct; some sources cite 1,227, but the v2 paper confirms 1,696)\n- **Geographic coverage:** 45 global regions, including underrepresented ones like Bangladesh, Zimbabwe, and Peru\n- **Topic categories:** 17 diverse topics (food preferences, greeting etiquette, and more)\n- **License:** CC BY 4.0 — permits sharing, adaptation, and use in training with attribution\n- **Evaluation design:** Two setups — CulturalBench-Easy and CulturalBench-Hard (same questions, different framing). Best model accuracy on Hard: 28.7–61.5% (vs. 92.4% human)\n- **Training use:** The dataset is framed primarily as an evaluation benchmark, but the CC BY 4.0 license does not restrict training use\n- **ACL Anthology:** [https://aclanthology.org/2025.acl-long.1247/](https://aclanthology.org/2025.acl-long.1247/)\n\n---\n\n### 2. MKQA (Multilingual Knowledge Questions and Answers)\n\n- **Full title:** \"MKQA: A Linguistically Diverse Benchmark for Multilingual Open Domain Question Answering\"\n- **ArXiv ID:** [2007.15207](https://arxiv.org/abs/2007.15207)\n- **Published in:** Transactions of the Association for Computational Linguistics (TACL)\n- **GitHub:** [https://github.com/apple/ml-mkqa](https://github.com/apple/ml-mkqa) (maintained by Apple ML)\n- **License:** CC BY-SA 3.0 (Creative Commons Attribution-ShareAlike 3.0) — NOT Apache 2.0 as sometimes reported; verify via the [official README](https://github.com/apple/ml-mkqa/blob/main/README.md)\n- **Size:** 10,000 question-answer pairs per language; 260,000 total pairs across 26 languages\n- **Languages (26):** Arabic, Chinese (Simplified, Hong Kong, Traditional), Danish, Dutch, English, Finnish, French, German, Hebrew, Hungarian, Italian, Japanese, Khmer, Korean, Malay, Norwegian, Polish, Portuguese, Russian, Spanish, Swedish, Thai, Turkish, Vietnamese\n- **Question types:** 8 answer-type categories — Entity, Long answer, Unanswerable, Date, Number, Number with unit, Short phrase, Binary\n- **Cultural grounding:** Questions are sampled from Google Natural Questions (primarily English/Western-oriented), then translated; the dataset is not specifically designed for culturally-grounded facts but does span cross-lingual factual QA\n- **Training use:** No explicit evaluation-only restriction; the README does not prohibit training use\n- **HuggingFace:** [https://huggingface.co/datasets/apple/mkqa](https://huggingface.co/datasets/apple/mkqa)\n\n---\n\n### 3. Culturally-Rich Datasets\n\n#### GlobalOpinionQA (Anthropic/Durmus et al., 2023)\n- **ArXiv:** [2306.16388](https://arxiv.org/abs/2306.16388)\n- **HuggingFace:** [Anthropic/llm_global_opinions](https://huggingface.co/datasets/Anthropic/llm_global_opinions)\n- **License:** CC BY-NC-SA 4.0 — non-commercial use only; derivatives must carry the same license; attribution required\n- **Source data:** Questions drawn from the World Values Survey (WVS) and Pew Global Attitudes Survey\n- **Format:** Country-level opinion distributions (not per-speaker labels); English-language questions only\n- **Size:** 1K–10K samples\n- **Cultural grounding:** High — covers subjective opinions on social, political, and ethical issues across many countries\n- **Training restriction:** NC clause bars commercial training; academic probe training is permissible with attribution\n\n#### CulturaX (Multilingual pre-training corpus)\n- **ArXiv:** [2309.09400](https://arxiv.org/abs/2309.09400); published at LREC-COLING 2024\n- **HuggingFace:** [uonlp/CulturaX](https://huggingface.co/datasets/uonlp/CulturaX)\n- **License:** Inherits from mC4 and OSCAR — effectively CC BY-NC 4.0 / restricted academic use; consult both parent dataset licenses before use\n- **Size:** 6.3 trillion tokens across 167 languages\n- **Purpose:** Pre-training corpus (not a QA or probing dataset); useful for training multilingual models but not structured for cultural probing\n- **Training use:** Permitted for non-commercial research; check OSCAR and mC4 license pages carefully\n\n#### WorldValuesBench (NLP adaptation of WVS)\n- **ArXiv:** [2404.16308](https://arxiv.org/html/2404.16308v1)\n- **GitHub:** [Demon702/WorldValuesBench](https://github.com/Demon702/WorldValuesBench)\n- **Size:** 20+ million examples for multi-cultural value prediction\n- **License/restriction:** Raw WVS data cannot be redistributed; users must download the raw WVS Wave 7 data themselves from [worldvaluessurvey.org](https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp) and run the processing pipeline. WVS permits non-profit use with registration only — not training-open in the usual sense\n- **Training use:** Restricted; not freely redistributable; WVS license requires notification upon publication use\n\n#### World Values Survey (WVS) itself\n- **License:** Available without restrictions for not-for-profit purposes only; registration required; redistribution of raw data not permitted\n- **NLP training use:** Not directly training-permitted without navigating WVS data agreement\n\n---\n\n### 4. Recent Cultural Probing Work (2024–2025) and Their Training Datasets\n\n#### CultureLLM (NeurIPS 2024)\n- **ArXiv:** [2402.10946](https://arxiv.org/abs/2402.10946)\n- **GitHub:** [Scarelette/CultureLLM](https://github.com/Scarelette/CultureLLM)\n- **Training approach:** Uses 50 WVS seed samples per culture, then applies semantic data augmentation to generate training data; fine-tunes culture-specific LLMs for 9 cultures\n- **WVS topics used:** Social values, migration, security, science and technology, religious values, ethical values, political interest\n- **Paper license:** CC BY 4.0; however, WVS seed data carries WVS's own restrictions (see above)\n- **Training use:** Code and augmented data are shared, but WVS-derived seed data requires WVS agreement\n\n#### INCLUDE (ICLR 2025)\n- **ArXiv:** [2411.19799](https://arxiv.org/html/2411.19799v1)\n- **License:** CC BY 4.0 — fully permissive for training use with attribution\n- **Size:** 197,243 MCQA pairs from 1,926 local examinations\n- **Coverage:** 44 written languages, 52 countries, 15 scripts\n- **Cultural grounding:** High — sourced from regional educational, professional, and practical exams written by native speakers; not translated from English\n- **Training use:** Explicitly permitted under CC BY 4.0; strongly suitable for probe training\n\n#### Global MMLU (Cohere for AI, ACL 2025)\n- **ArXiv:** [2412.03304](https://arxiv.org/abs/2412.03304)\n- **HuggingFace:** [CohereForAI/Global-MMLU](https://huggingface.co/datasets/CohereForAI/Global-MMLU)\n- **License:** Apache 2.0 — the most permissive option found; allows commercial and training use freely\n- **Size:** ~600,000 questions across 42 languages (~14,300 per language)\n- **Cultural grounding:** Moderate — includes cultural sensitivity annotations (Culturally Sensitive vs. Culturally Agnostic flags); 28% of questions flagged as requiring culturally sensitive knowledge\n- **Training use:** Fully permitted; Apache 2.0 is unrestricted\n\n---\n\n### 5. BLEnD and SemEval-2026 Task 7\n\n#### BLEnD (NeurIPS 2024 Datasets & Benchmarks Track)\n- **ArXiv:** [2406.09948](https://arxiv.org/abs/2406.09948)\n- **GitHub:** [nlee0212/BLEnD](https://github.com/nlee0212/BLEnD)\n- **NeurIPS proceedings:** [https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets_and_Benchmarks_Track.html](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets_and_Benchmarks_Track.html)\n- **License:** CC BY-SA 4.0 — permits training use with attribution and ShareAlike requirement\n- **Size:** 52,600 question-answer pairs\n- **Coverage:** 16 countries/regions, 13 languages including low-resource ones (Amharic, Assamese, Azerbaijani, Hausa, Sundanese)\n- **Topic categories:** Food, sports, family, education, holidays/celebrations/leisure, work-life\n- **Cultural grounding:** Very high — questions concern everyday life knowledge not found in Wikipedia; written by local annotators\n\n#### SemEval-2026 Task 7: Everyday Knowledge Across Diverse Languages and Cultures\n- **ArXiv:** [2605.02601](https://arxiv.org/abs/2605.02601)\n- **GitHub:** [BLEnD-SemEval2026/SemEval-2026-Task-7](https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7)\n- **Codabench:** [https://www.codabench.org/competitions/10281/](https://www.codabench.org/competitions/10281/)\n- **Relationship to BLEnD:** Task 7 is an extended version of BLEnD, expanding coverage to 30+ language-culture pairs (17 new pairs beyond the original 13)\n- **License for Task 7 data:** Not yet explicitly published as of this writing\n- **Training restriction:** Explicitly prohibited — the task rules state participants may not use the data for training, fine-tuning, few-shot learning, or any other form of model modification. The SemEval-2026 Task 7 data is evaluation-only by design\n\n---\n\n### Summary Table\n\n| Dataset | License | Languages | Questions | Training-Permitted |\n|---|---|---|---|---|\n| CulturalBench (ACL 2025) | CC BY 4.0 | N/A (English MCQ) | 1,696 | Yes (license permits it) |\n| MKQA | CC BY-SA 3.0 | 26 | 260,000 | Yes (no restriction stated) |\n| GlobalOpinionQA | CC BY-NC-SA 4.0 | 1 (English) | 1K–10K | Non-commercial only |\n| CulturaX | mC4 + OSCAR (NC) | 167 | 6.3T tokens | Non-commercial only |\n| WorldValuesBench | WVS agreement required | Multi | 20M+ | Restricted (non-profit, no redistribution) |\n| INCLUDE (ICLR 2025) | CC BY 4.0 | 44 | 197,243 | Yes |\n| Global MMLU (ACL 2025) | Apache 2.0 | 42 | ~600,000 | Yes (fully open) |\n| BLEnD (NeurIPS 2024) | CC BY-SA 4.0 | 13 | 52,600 | Yes |\n| SemEval-2026 Task 7 | TBD | 30+ | TBD (BLEnD extension) | No — explicitly prohibited |\n| CultureLLM training data | CC BY 4.0 (paper); WVS (seeds) | 9 cultures | Augmented from WVS | Partial (augmented data yes; seeds require WVS agreement) |\n\n---\n\n### Key Recommendation for Probe Training\n\nThe cleanest options for training cultural knowledge probes with no licensing friction are:\n\n1. **Global MMLU** (Apache 2.0) — largest, 42 languages, culturally annotated\n2. **INCLUDE** (CC BY 4.0) — highest cultural authenticity, sourced from local exams in 52 countries\n3. **BLEnD** (CC BY-SA 4.0) — strongest everyday cultural grounding, 13 languages, NeurIPS 2024\n\nAvoid SemEval-2026 Task 7 data for training (explicitly prohibited), and be cautious with GlobalOpinionQA (NC clause) and WorldValuesBench/WVS (requires data agreement and non-profit restriction).\n\nSources:\n- [CulturalBench - ACL Anthology](https://aclanthology.org/2025.acl-long.1247/)\n- [CulturalBench - arXiv 2410.02677](https://arxiv.org/abs/2410.02677)\n- [MKQA - arXiv 2007.15207](https://arxiv.org/abs/2007.15207)\n- [MKQA GitHub (Apple)](https://github.com/apple/ml-mkqa)\n- [GlobalOpinionQA - arXiv 2306.16388](https://arxiv.org/abs/2306.16388)\n- [GlobalOpinionQA - HuggingFace](https://huggingface.co/datasets/Anthropic/llm_global_opinions)\n- [CulturaX - arXiv 2309.09400](https://arxiv.org/abs/2309.09400)\n- [CulturaX - HuggingFace](https://huggingface.co/datasets/uonlp/CulturaX)\n- [WorldValuesBench - arXiv 2404.16308](https://arxiv.org/html/2404.16308v1)\n- [World Values Survey official documentation](https://www.worldvaluessurvey.org/WVSDocumentationWVL.jsp)\n- [BLEnD - arXiv 2406.09948](https://arxiv.org/abs/2406.09948)\n- [BLEnD GitHub](https://github.com/nlee0212/BLEnD)\n- [BLEnD NeurIPS 2024 proceedings](https://proceedings.neurips.cc/paper_files/paper/2024/hash/8eb88844dafefa92a26aaec9f3acad93-Abstract-Datasets_and_Benchmarks_Track.html)\n- [SemEval-2026 Task 7 - arXiv 2605.02601](https://arxiv.org/abs/2605.02601)\n- [SemEval-2026 Task 7 GitHub](https://github.com/BLEnD-SemEval2026/SemEval-2026-Task-7)\n- [SemEval-2026 Task 7 Codabench](https://www.codabench.org/competitions/10281/)\n- [INCLUDE - ICLR 2025 OpenReview](https://openreview.net/forum?id=k3gCieTXeY)\n- [Global MMLU - arXiv 2412.03304](https://arxiv.org/abs/2412.03304)\n- [Global MMLU - HuggingFace](https://huggingface.co/datasets/CohereForAI/Global-MMLU)\n- [CultureLLM - arXiv 2402.10946](https://arxiv.org/abs/2402.10946)\n- [CultureLLM GitHub](https://github.com/Scarelette/CultureLLM)"
      }
    ],
    "totalDurationMs": 164010,
    "totalTokens": 31399,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 394,
      "cache_read_input_tokens": 26776,
      "output_tokens": 4228,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 394
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 4228,
          "cache_read_input_tokens": 26776,
          "cache_creation_input_tokens": 394,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 394,
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
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "683864d2-0c34-47f9-9bf1-6c666d3292d4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 16 · 2026-05-10T07:52:49.129Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information to revise the research idea. Let me synthesize what I've learned:

1. **CulturalBench training restriction**: CONFIRMED. The paper (arXiv:2410.02677) explicitly states the data cannot be used for training due to OpenAI API annotation platform terms. However, the CC-BY-4.0 license technically allows training - but the API terms create a contractual prohibition. The paper should remove the claim that CulturalBench is "publicly available for training use."

Interestingly, the second agent found that the ACL Anthology entry shows CulturalBench under CC BY 4.0, and one agent suggests the license technically permits training but the OpenAI API usage terms override this. 

The paper explicitly states that the annotation platform using OpenAI APIs disallowed the collected data for training purposes, so CulturalBench is evaluation-only in practice and I need to find alternatives for Stage 2 probe training.

2. **Best alternatives for Stage 2 probe training**: INCLUDE (ICLR 2025, CC BY 4.0) with 197,243 MCQA pairs across 44 languages and 52 countries sourced from local exams offers the highest cultural authenticity, while Global MMLU (Apache 2.0) provides around 600,000 questions in 42 languages with cultural sensitivity annotations.

BLEnD (NeurIPS 2024, CC BY-SA 4.0) has 52,600 Q&A pairs in 13 languages, but I need to be careful here—the original BLEnD dataset is training-permitted, but the SemEval-2026 Task 7 extension built on it is evaluation-only. I could use the original BLEnD training split for Stage 2 probe training while reserving the SemEval-2026 Task 7 version for final evaluation, though I need to think through whether mixing the two versions creates any data leakage issues.

Actually, since BLEnD and SemEval-2026 Task 7 are overlapping datasets, using BLEnD for training and Task 7 for evaluation feels ambiguous. I'll go with INCLUDE and Global MMLU instead—they're completely separate from my evaluation sets. So for Stage 2 probe training, I'll use INCLUDE (ICLR 2025, CC BY 4.0, 197K pairs across 44 languages) as my primary cultural-localization dataset.

I can supplement it with language-filtered Wikipedia paragraphs from culture-specific articles, and keep TyDiQA and XQUAD for factual transfer learning. CulturalBench and SemEval-2026 Task 7 stay evaluation-only.

Now I'm weighing whether INCLUDE and Global MMLU are truly measuring cultural knowledge versus factual knowledge—the probe needs to distinguish between them. INCLUDE comes from regional exams which grounds it culturally, but I need to verify it's not just factual knowledge.

For the cultural probe training, I should focus on datasets that specifically test cultural knowledge across multiple languages with appropriate licensing. INCLUDE filtered for cultural domains like food, customs, and history works well alongside multilingual Wikipedia articles on cultural topics. Global MMLU's culturally-sensitive subset with its annotations across 42 languages is also valuable. I'll combine INCLUDE with cultural domain filtering and multilingual Wikipedia cultural articles as my Stage 2 training data.

Now looking at a sparse subnetwork approach from recent research—the authors use Language Activation Probability Entropy to isolate language-specific subnetworks that comprise less than 1% of model parameters. They tested this on Llama-3.1-8B, Mistral-Nemo-12B, and Aya-Expanse-8B, finding that language adaptation concentrates in the down-projection weights of later layers. The method achieves 90.5% cross-lingual alignment while outperforming full fine-tuning and other parameter-efficient approaches, though the focus is on improving underrepresented language performance rather than cultural preservation specifically.

For the revision, I need to update the data sources in Stage 2—replacing the CulturalBench training reference with INCLUDE and Wikipedia cultural domain articles instead, while keeping CulturalBench as evaluation-only in Stage 4. I should also remove the "publicly available for training use" phrase and add this sparse subnetwork enhancement to the landscape section, updating the key references to include INCLUDE, Global MMLU, and the arXiv paper.

The core issue is that CulturalBench's CC BY 4.0 license is overridden by an explicit contractual restriction from OpenAI API usage, so it can't be used for training despite the permissive license. INCLUDE is the better replacement—it's CC BY 4.0 licensed with 197K MCQA pairs across 44 languages and 52 countries.

For Stage 2, I'll revise the training approach to use INCLUDE as the primary source for cultural-localization probes, supplemented by filtered Wikipedia articles tagged with cultural domains. I should also mention Global MMLU as an alternative option given its culturally-sensitive annotations. The Stage 4 evaluation setup stays the same with CulturalBench and SemEval-2026 Task 7 remaining as evaluation benchmarks.

For the landscape section, I'm adding a note about Sparse Subnetwork Enhancement for underrepresented languages.

This approach identifies tiny language-specific subnetworks using entropy-based activation metrics and fine-tunes only those parameters, achieving strong cross-lingual alignment while maintaining general knowledge across multiple model architectures. The key difference from CLS-LoRA is the focus: this method targets language performance improvements on translation and classification tasks, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction tuning. Now I'm checking which other sections need updates—core_problem, opportunity, resource_estimate, and target_venues all look fine since they don't reference CulturalBench training. Let me locate the exact phrase in the approach section about CulturalBench being available for training use and correct that, then I'll generate the full revised JSON with all the targeted modifications. For cultural-localization probes, I'm using INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs spanning 44 languages and 52 countries), filtered to cultural-domain categories like customs, food, celebrations, and social norms, plus language-filtered Wikipedia paragraphs from culture-specific articles with Wikidata cultural-domain tags (CC-BY-SA 4.0). CulturalBench can't be used for training since its annotation platform relied on OpenAI APIs with terms prohibiting training use, so it's reserved for final evaluation in Stage 4 alongside SemEval-2026 Task 7. For factual-transfer probes, I'm using held-out splits of TyDiQA and XQUAD, with SemEval-2026 Task 7 data strictly reserved for evaluation per the task rules, and no new annotation needed. I'm noticing that CulturalBench is mentioned in the approach section but missing from the key_references list, so I should add it there with the proper citation details to maintain consistency across the document. I'm now constructing the JSON with these updates, making sure the references are properly formatted and the stage descriptions accurately reflect the data sources and evaluation methodology.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9317d872-0f93-49e7-a853-98ee6196d21a",
  "isSidechain": false,
  "requestId": "req_011CatXMwK3AsUJ94SgQFjkB",
  "type": "assistant",
  "uuid": "0ffe8567-77f7-4610-9d74-c08f346994ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019wKr3xyUqDfyvH6PBrfqu1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9399,
      "cache_read_input_tokens": 27616,
      "output_tokens": 14248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14248,
          "cache_read_input_tokens": 27616,
          "cache_creation_input_tokens": 9399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9399
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

_source line 17 · 2026-05-10T07:56:30.576Z_

Now I have all the information I need. Let me synthesize the findings before writing the revision:

**CulturalBench**: Confirmed evaluation-only. The paper (arXiv:2410.02677) explicitly states: *"our annotation platform, which involves using OpenAI APIs, disallowed the collected data to be used for training."* Despite a CC-BY-4.0 nominal license, the OpenAI API terms create a contractual prohibition on training use.

**Best training-permitted replacements for Stage 2 cultural probes**:
- **INCLUDE** (ICLR 2025, CC BY 4.0) — 197K MCQA pairs from regional examinations across 44 languages/52 countries; strongest cultural authenticity from native sources
- **Multilingual Wikipedia cultural-domain articles** (CC-BY-SA 4.0) — widely multilingual, filterable by Wikidata tags

**arXiv:2510.13580 (Sparse Subnetwork Enhancement)**: Uses LAPE metric to identify language-associated neurons (<1% of parameters); achieves 90.5% cross-lingual alignment; adaptation concentrated in down-projection weights of later layers. Objective is language performance improvement (not cultural preservation); partition axis is language-identity (not factual-vs-cultural semantic axis).

This is a **minor** revision — fixing a factual error about training permissions and adding one related work entry.

```json
{
  "title": "Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignment",
  "project_name": "cls_lora_cultural_preservation",
  "source": "web_research",
  "level": "solid",
  "change_type": "minor",
  "core_problem": "Cross-lingual fine-tuning systematically suppresses culturally-grounded, language-specific knowledge while improving factual transfer—a phenomenon called 'cultural erasure.' Mechanistic work (arXiv:2504.10191) demonstrates that in pre-trained instruction-tuned models, cultural knowledge is spatially localized in specific layers and steerable via linear activation vectors, suggesting particular layer indices implement cultural routing pathways. Whether this spatial localization persists after LoRA instruction fine-tuning—and whether cross-lingual fine-tuning causes behavioral erasure (routing pathway disruption), representational erasure (information loss), or both—remains empirically untested. No training-time method prevents either failure mode, forcing practitioners to choose between cross-lingual capability and cultural authenticity. A complementary mechanistic uncertainty reinforces the need for per-model empirical investigation: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deeper-layer localization (layers 19–30, approximately 45–71% depth in Gemma2-9b-it) identified via activation-steering analysis in arXiv:2504.10191. The two methodologies measure different constructs—discrete high-influence neurons versus distributed activation-space subspaces—and their disagreement means the culturally-critical layer partition cannot be reliably imported from prior work for an arbitrary target model; it must be discovered empirically.",
  "opportunity": "'Rethinking Cross-lingual Alignment' (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026) rigorously demonstrates that every tested cross-lingual alignment approach degrades cultural localization across all six languages, and proposes Surgical Steering as a remedy—but only at inference time, requiring per-query layer manipulation and offering no prevention during training. The finding that factual transfer and cultural localization are optimally steerable at different model layers is actionable: applying LoRA selectively to factual-transfer layers while freezing cultural-knowledge layers during instruction fine-tuning would prevent erasure at the source. arXiv:2504.10191 establishes that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors in specific layers (notably layers 19–30 in Gemma2-9b-it, with peaks at layers 23 and 30), supporting the hypothesis that particular layer indices implement cultural routing pathways. CLS-LoRA's freezing strategy is designed to exploit this structure: if that spatial localization persists after LoRA fine-tuning (behavioral erasure—routing disrupted but representations intact), freezing those layers during training prevents routing disruption; if fine-tuning also degrades the representations themselves (representational erasure), the KL-divergence penalty anchors cultural-layer activations to their pretrained distribution. Stage 1 empirically distinguishes these two failure modes before the main sweep begins. Crucially, the layer partition question is now a live empirical debate in the literature: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) independently find culture-relevant neurons in shallow-to-middle MLP layers using gradient attribution, while activation-steering work (arXiv:2504.10191, arXiv:2510.26024) localizes cultural steerability in deeper layers. This genuine methodological disagreement elevates Stage 2 probing from a validation step to the principled empirical resolution of an open question—CLS-LoRA discovers the culturally-critical partition for each target model rather than assuming it from any single prior study. This is feasible with any open-source dense multilingual model via a lightweight per-layer probing step.",
  "landscape": "INCLINE (arXiv:2410.12462, ACL 2025 outstanding paper) aligns internal representations from low-resource to high-resource languages via learned projection matrices derived from parallel sentences, improving cross-lingual task performance but not distinguishing factual from cultural knowledge. Middle-Layer Representation Alignment (arXiv:2502.14830, ACL 2025, Liu & Niehues) provides the empirical foundation for CLS-LoRA's factual-transfer layer partition: through translation retrieval probing across 1,190 language pairs on Llama 3 and Qwen 2.5, it establishes that layer 16 (50% depth in a 32-layer model) is the key integration point for cross-lingual semantic alignment, and that incorporating a middle-layer alignment objective consistently improves cross-lingual task performance particularly for lower-resource languages. CLS-LoRA extends this by additionally protecting cultural-knowledge layers from LoRA updates—arXiv:2504.10191 identifies layers 19–30 (approximately 45–71% depth in Gemma2-9b-it's 42-layer architecture, with peak cultural activation at layers 23 and 30) as critical for cultural routing, and Stage 2 probing empirically determines the analogous partition for each target model—a protection axis entirely absent from Liu & Niehues, whose work does not distinguish factual from cultural knowledge and proposes no cultural preservation objective. Cross-Lingual Transfer of Cultural Knowledge (arXiv:2506.01675, ACL 2025 short paper, Zhang et al.) provides empirical background showing cultural knowledge transfer is asymmetric: high-resource language pairs exhibit bidirectional transfer while low-resource languages primarily export cultural knowledge to English without reciprocal benefit, driven by a frequency-based pretraining data mechanism. This asymmetry directly motivates training-time prevention of cultural erasure—low-resource languages are disproportionately at risk and most in need of the protection CLS-LoRA provides. AlignX (arXiv:2509.24338, EMNLP 2025) and CM-Align (arXiv:2509.08541) apply two-stage and consistency-based multilingual alignment respectively, both optimizing convergence without a cultural preservation objective. Language Surgery/ITLC (arXiv:2506.12450) disentangles language-specific from agnostic information through latent injection at inference time, but does not train models to preserve this distinction. Alignment through steering (arXiv:2505.12584) adds a learned residual-stream vector at a single layer; it outperforms many baselines but still does not model the factual-cultural layer split. Surgical Steering (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 the first author's publication page lists this as an arXiv preprint without a confirmed proceedings venue) is the only method addressing the cultural erasure problem, and is strictly an inference-time patch over an already-erased model. arXiv:2504.10191 ('Localized Cultural Knowledge is Conserved and Controllable in LLMs', April 2025) demonstrates that in pre-trained instruction-tuned models, cultural knowledge exists as spatially localized steerable activation-space vectors—mechanistic analysis on Gemma2-9b-it (42 layers) identifies layers 19–30 as critical for cultural activation, with peak effects at layers 23 and 30 (approximately 55–71% depth)—and can be controlled via linear steering at inference time. This establishes spatial localization of cultural knowledge in pre-trained models, motivating CLS-LoRA's hypothesis that specific layer indices implement cultural routing pathways; whether this localization persists after LoRA instruction fine-tuning is precisely what Stage 1 tests.\n\nYamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) conduct a neuron-level analysis of cultural understanding using a gradient-based scoring method with additional filtering for precise refinement. They identify both culture-general neurons (supporting cultural understanding across cultures) and culture-specific neurons (tied to individual cultures), which together comprise less than 1% of all neurons and are concentrated in shallow-to-middle MLP layers—not in the deeper layers identified by activation-steering analysis in arXiv:2504.10191. Suppressing these neurons degrades cultural benchmark performance by up to 30% while leaving general NLU tasks largely unaffected. This finding is in apparent tension with the deeper-layer localization from arXiv:2504.10191 and arXiv:2510.26024, reflecting a genuine methodological distinction: gradient attribution identifies discrete neurons with the highest individual causal influence, which may be sparse and concentrated in earlier layers; activation-steering subspaces reflect distributed representational geometry that implements cultural routing across many layers and may peak in depth-profile at different points. CLS-LoRA's Stage 2 probing directly bridges this debate: rather than assuming either result, it measures per-layer probe accuracy on each target model and discovers the cultural-knowledge partition empirically. If shallow neurons (Yamamoto et al.) dominate, Stage 2 will assign those layers to the frozen cultural partition; if deeper subspaces (arXiv:2504.10191) dominate, Stage 2 will assign those layers instead. Stage 2 is thus a model-specific resolution mechanism that makes CLS-LoRA robust to methodological disagreements in the mechanistic literature.\n\nTwo directly related selective-LoRA methods require explicit differentiation. MLAS-LoRA (ACL 2025, aclanthology.org/2025.acl-long.762) detects language-aware neurons in a teacher model and injects extracted knowledge into language-pair-specific LoRA modules in a student model for multilingual machine translation, achieving +1.7 BLEU on average. While MLAS-LoRA and CLS-LoRA both employ a probe-then-selective-LoRA pipeline, they differ on three critical axes: (1) task domain—MLAS-LoRA targets MT translation quality whereas CLS-LoRA targets cultural knowledge preservation during instruction fine-tuning; (2) partition dimension—MLAS-LoRA partitions along language-pair specificity (language-A vs language-B neurons) whereas CLS-LoRA partitions along the factual-transfer vs cultural-localization semantic axis, which cuts across language pairs; and (3) objective—MLAS-LoRA optimizes translation accuracy via teacher-student knowledge distillation whereas CLS-LoRA optimizes a cultural-preservation signal with no distillation component. The cultural-preservation objective is the categorical novelty: no prior selective-LoRA work defines a 'keep culturally-grounded outputs intact' training signal. LayRA (arXiv:2509.11414, September 2025) proposes layer-selective LoRA for continual multilingual language addition, applying LoRA to initial and final transformer layers (the first 10 and last 2 layers, plus embeddings and LM head) while freezing intermediate layers. The partition rationale—that multilingual models encode source-language inputs in initial layers, reason in English in middle layers, and decode into the target language in final layers—leads to a source-language-encoding vs English-reasoning vs target-language-decoding functional partition axis. CLS-LoRA differs on three dimensions: (1) objective—LayRA enables new-language addition without catastrophic forgetting of existing languages, whereas CLS-LoRA preserves cultural knowledge during cross-lingual instruction fine-tuning; (2) partition axis—LayRA's functional encoding/reasoning/decoding axis is defined over language identity and cuts uniformly across all languages, whereas CLS-LoRA's factual-transfer vs cultural-localization semantic axis cuts across language-pair specificity; (3) partition method—LayRA hard-codes specific layer indices derived from qualitative linguistic reasoning, whereas CLS-LoRA uses empirical per-layer probing to discover the partition for each target model, enabling adaptation to the contested mechanistic landscape. The cultural-preservation objective remains the categorical novelty absent from LayRA. Source-Shielded Updates (arXiv:2512.04844, Nov 2025) proposes column-wise parameter freezing to prevent catastrophic forgetting of source-language task performance during target-language adaptation—addressing cross-lingual interference but not the factual-vs-cultural layer distinction or cultural knowledge preservation as a first-class objective. Sparse Subnetwork Enhancement for Underrepresented Languages (arXiv:2510.13580, Gurgurov et al., updated February 2026) identifies language-associated sparse subnetworks comprising less than 1% of model parameters using Language Activation Probability Entropy (LAPE), an information-theoretic metric that captures language-specific activation patterns, and fine-tunes only those parameters. On Llama-3.1-8B, Mistral-Nemo-12B, and Aya-Expanse-8B across 12 mid- and low-resource languages, it achieves 90.5% cross-lingual alignment (cosine similarity)—the best of any tested method—while preserving general capabilities (MMLU: 63.01% vs. 63.08% base), outperforming full fine-tuning, LoRA, and IA3. Adaptation is concentrated in down-projection weights of later layers, with weight changes 3–5× larger than up/gate projections. CLS-LoRA differs from Sparse Subnetwork Enhancement on two axes: (1) objective—Sparse Subnetwork Enhancement targets language performance improvement on translation and classification benchmarks (FLORES, SIB-200, BELEBELE) whereas CLS-LoRA targets cultural knowledge preservation during cross-lingual instruction fine-tuning; and (2) partition axis—LAPE identifies language-identity neurons (neurons that activate specifically for a given language, cutting across semantic content) whereas CLS-LoRA partitions along the factual-transfer vs. cultural-localization semantic axis, which cuts across language identity rather than tracking it. The cultural-preservation objective remains absent from Sparse Subnetwork Enhancement.",
  "approach": "We propose Cultural-Layer-Selective LoRA (CLS-LoRA), a training-time method that prevents cultural erasure without sacrificing factual cross-lingual transfer. The pipeline has four stages.\n\nMechanistic bridge. Our layer-freezing strategy rests on a hypothesis connecting inference-time observations to training-time interventions: the layer indices most sensitive to cultural-vs-factual activation steering at inference time (arXiv:2510.26024, corroborated by cultural customization vectors in arXiv:2504.10191 concentrated at layers 19–30 in Gemma2-9b-it) identify the weight matrices that implement cultural routing. LoRA updates modify precisely these weight matrices; applying LoRA to cultural-knowledge layers may therefore disrupt the routing pathways through which culturally-grounded representations reach outputs. This hypothesis involves a genuine empirical uncertainty that the literature has not resolved: Yamamoto et al. (2026, arXiv:2510.08284, ICLR 2026) use gradient-based neuron attribution and find culture-relevant neurons concentrated in shallow-to-middle MLP layers, in apparent tension with the deep-layer activation-steering localization from arXiv:2504.10191. The discrepancy most likely reflects the difference between measuring discrete high-influence neurons (gradient attribution captures sparse, individually causal units that may be early in the network) versus measuring distributed activation subspaces (steering analysis captures the geometry of representational routing, which may span many layers and peak later). Neither result invalidates the other; they measure different aspects of how cultural knowledge is implemented. Stage 2 probing is designed precisely for this uncertainty: by measuring per-layer probe accuracy directly on each target model's representations, it discovers the culturally-critical partition without assuming either methodological lens is correct—if shallow neurons dominate functionally, Stage 2 identifies shallow layers as the cultural partition; if deeper subspaces dominate, Stage 2 identifies those instead. Whether the representations themselves persist as recoverable vectors after full LoRA fine-tuning (behavioral erasure) or are also degraded (representational erasure) is a separate open empirical question—Stage 1 provides this answer. Freezing the empirically-identified cultural-knowledge layers during training preserves both the routing weights and the residual-stream geometry that steerability depends on, addressing both failure modes by design.\n\nStage 1 — Structural diagnostic: Before the main sweep, we run full-LoRA instruction fine-tuning on a held-out model checkpoint and measure per-layer cultural probe accuracy before and after. Stage 1 trains separate linear probes on each checkpoint's frozen representations—one probe trained and evaluated on the pretrained-checkpoint's layer activations, one probe trained and evaluated on the post-LoRA-checkpoint's layer activations—using the same held-out cultural question split for both. This ensures accuracy differences reflect genuine representational change rather than activation-space reorganization: applying a single probe trained on pretrained representations cross-checkpoint to post-LoRA representations would fail if LoRA remaps the activation geometry without destroying cultural information (behavioral erasure), conflating reorganization with information loss; separate per-checkpoint probes make the comparison clean and the behavioral-vs-representational distinction interpretable. If probe accuracy is maintained post-training, erasure is confirmed as behavioral (pathway disruption) and layer freezing is the correct intervention; if probe accuracy drops, erasure is partly representational and the KL-divergence regularizer in Stage 3 becomes critical. This diagnostic sharpens the mechanistic story and validates the layer-freezing strategy regardless of which failure mode dominates. An automated entropy-based partition fallback replaces human inspection when probe curves are bimodal or noisy, reducing the agent failure mode from prior review.\n\nStage 2 — Layer profiling: Lightweight linear probes (one per transformer layer) are trained on a small parallel corpus to produce per-layer factual-transfer and cultural-localization accuracy scores, yielding a principled layer partition. For factual transfer, the empirical expectation from arXiv:2502.14830 (Liu & Niehues) is approximately middle layers (~50% model depth). For cultural knowledge, arXiv:2504.10191 identifies layers 19–30 as critical in Gemma2-9b-it (approximately 45–71% depth in a 42-layer model, with peak effects at layers 23 and 30); Yamamoto et al. (arXiv:2510.08284, ICLR 2026) find culture-relevant neurons in shallow-to-middle MLP layers via gradient attribution. Stage 2 probing empirically determines the partition boundaries for each target model—Qwen3-8B (36 layers) and Aya-23-8B—rather than hard-coding percentages from either prior study; this is the methodologically sound response to the contested mechanistic landscape. For cultural-localization probes, we use INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs sourced from regional examinations across 44 languages and 52 countries, arXiv:2411.19799), filtered for cultural-domain categories (customs, food, celebrations, social norms), supplemented by language-filtered Wikipedia paragraphs extracted from culture-specific articles tagged with Wikidata cultural-domain categories (CC-BY-SA 4.0, widely multilingual). CulturalBench (arXiv:2410.02677, ACL 2025) cannot be used for probe training because the authors explicitly state that the annotation platform used OpenAI APIs under terms that disallow using the collected data for training; CulturalBench is therefore reserved strictly for final evaluation in Stage 4. For factual-transfer probes, we use held-out splits of TyDiQA and XQUAD. SemEval-2026 Task 7 data (BLEnD extension) is reserved strictly for final evaluation and is not used in probe training, consistent with the task's evaluation-only rules (confirmed via the official task repository). No new annotation is required.\n\nStage 3 — Selective LoRA training: LoRA adapters (via Hugging Face PEFT target_modules) are inserted exclusively into factual-transfer layers and trained with standard instruction fine-tuning loss on multilingual instruction data, while cultural-knowledge layers remain fully frozen. An optional auxiliary KL-divergence penalty on a held-out cultural probe set discourages residual drift in frozen layers' downstream activations. To establish that layer freezing is the operative mechanism rather than KL regularization alone, Stage 3 includes a 2×2 ablation: (a) full LoRA without KL penalty (existing baseline); (b) full LoRA with KL-divergence penalty on cultural-layer activations (regularization-only baseline, new); (c) CLS-LoRA with layer freezing and no KL penalty (freezing-only; already present in the sweep as the no-regularization variant); (d) CLS-LoRA with layer freezing and KL penalty (proposed method). Condition (b) is the critical addition: it tests whether KL regularization alone, without the complexity of a learned layer partition, achieves equivalent cultural preservation. If (b) matches (d), the partitioning step is unnecessary overhead; if (c) and (d) both outperform (b), layer freezing is confirmed as the operative mechanism. Approximately 4–6 additional training runs (condition (b) only; 2 models × 2–3 seeds) are added to the auto sweep; conditions (a), (c), and (d) are already covered by existing runs.\n\nStage 4 — Evaluation: Experiments run on Qwen3-8B (primary: confirmed dense, 36 transformer layers, 119 languages and dialects, 8.2B parameters) and Aya-23-8B (secondary: confirmed dense decoder-only, 23 languages, 8B parameters) for cross-architecture generalization. All Qwen3-8B experiments are conducted in non-thinking mode (enable_thinking=False in the chat template), ensuring consistent direct-generation behavior during both LoRA fine-tuning and cultural localization probing without interference from chain-of-thought reasoning pathways. LLaMA 4 Scout is excluded—its 48-block, 16-expert MoE architecture makes the factual-vs-cultural layer partition from arXiv:2510.26024, established on dense models, methodologically inapplicable without separate MoE-specific validation. Evaluation uses CulturalBench (arXiv:2410.02677, ACL 2025; 1,696 human-verified questions across 45 global regions, evaluation-only) and SemEval-2026 Task 7 as primary cultural metrics. To verify that CLS-LoRA does not regress on capabilities orthogonal to cultural localization and factual QA, Stage 4 adds three supplementary evaluation tracks via lm-evaluation-harness: cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; lm-eval task group xcopa_[lang]); cross-lingual narrative understanding (XStoryCloze, 11 languages, zero-shot; lm-eval task group xstorycloze); and multilingual arithmetic chain-of-thought (MGSM, 11 languages, direct mode; lm-eval task mgsm_direct). Each benchmark requires approximately 2–4 GPU-hours per model; together they add ~18–24h A100 total across both target models and all evaluated checkpoints. XCOPA is the most mechanistically relevant: if Stage 2's cultural-knowledge layer partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain commonsense transfer—an outcome that would be reported transparently and interpreted as a scope constraint on the method (cultural preservation trades off against commonsense transfer in those layers) rather than treated as an uncontrolled failure. MGSM verifies that the factual-transfer LoRA updates preserve multilingual arithmetic reasoning. All three benchmarks use standard zero-shot or direct evaluation protocols already in lm-evaluation-harness and require no additional training data. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; we therefore employ the explicitly defined fallback evaluation—a 2D scatter of cross-lingual factual accuracy (XQUAD/TyDiQA) vs cultural localization accuracy (CulturalBench) across languages, normalized to the pre-fine-tuning baseline, yielding the same transfer-localization interpretive framework. We compare against full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA (adapted to the instruction-FT setting), and Source-Shielded Updates baselines to demonstrate that CLS-LoRA Pareto-dominates prior methods in the transfer-localization trade-off space.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~230h A100 80GB (~92h H100 equivalent)",
      "gpu_utilization": "~30–40% effective; GPU idles while the researcher inspects probe accuracy heatmaps to select layer partition boundaries, designs ablation grids, and iterates on training scripts between runs",
      "timeline": "4–6 months",
      "team": "1–2 researchers",
      "estimated_gpu_cost": "~$345–475 (A100 at $1.49–2.06/hr via RunPod/Lambda); additional ~30h reflects new ablation runs (condition (b), ~12h) and XCOPA/XStoryCloze/MGSM evaluation (~18h)"
    },
    "human_in_loop": {
      "gpu_hours": "~155h A100 80GB (~62h H100 equivalent)",
      "gpu_utilization": "~60–70% effective; agent queues probing and LoRA sweep experiments overnight, researcher reviews layer partition heatmaps and approves next ablation tier once daily, cutting idle time ~50% vs. manual",
      "timeline": "6–8 weeks",
      "team": "1 researcher, ~30min/day check-in",
      "claude_api_cost": "$150–250 (~1000–1500 conversation turns at $0.10–0.15/turn with Opus)",
      "estimated_gpu_cost": "~$231–319 (A100 at $1.49–2.06/hr); additional ~25h reflects new ablation condition (b) runs and supplementary benchmark evaluations",
      "risk_note": "Key risk: agent may commit to a suboptimal layer partition if probe accuracy curves are bimodal or noisy; the automated entropy-based partition fallback reduces (but does not eliminate) this risk; daily human review of the partition heatmap before LoRA runs remains the essential gate"
    },
    "auto_research": {
      "gpu_hours": "~310–360h A100 80GB (~122–144h H100 equivalent); within the ≤200h H100 hard constraint",
      "gpu_utilization": "~85–90% effective; agent continuously queues the next experiment upon completion with no human approval bottleneck—idle only during brief checkpoint evaluation transitions",
      "sweep": "3 LoRA rank values (8, 16, 32) × 2 layer partition thresholds × 2 model families (Qwen3-8B, Aya-23-8B) × 2 regularization strengths × 2 seeds = 48 core training runs; plus ~12 baseline runs (full-LoRA, Surgical Steering, INCLINE, Source-Shielded Updates); plus ~4–6 new ablation runs for condition (b) (full LoRA + KL only, 2 models × 2–3 seeds); plus Stage 1 structural diagnostic runs; plus ~18–24h for XCOPA/XStoryCloze/MGSM evaluation across all checkpoints via lm-evaluation-harness",
      "timeline": "5–8 days with 4–6 concurrent A100 GPUs (or 3–5 days with H100s)",
      "team": "0 (2–3h of initial harness setup and config-space definition)",
      "claude_api_cost": "$200–350 (~1500–2500 turns across experiment planning, result parsing, and ablation branching)",
      "estimated_gpu_cost": "~$462–742 (A100 at $1.49–2.06/hr); increase from prior estimate reflects ~4–6 new condition (b) training runs and ~18–24h benchmark evaluation",
      "speed_bottleneck": "Number of concurrent GPUs and the ~1h cultural benchmark evaluation per checkpoint; XCOPA/XStoryCloze/MGSM evaluation can be parallelized across checkpoints on separate GPUs via lm-evaluation-harness",
      "risk_note": "Bimodal probe distributions are handled by an automated entropy-based partition fallback. The Stage 1 structural diagnostic provides an early signal: if cultural probe accuracy is unaffected by full-LoRA training, the layer-freezing strategy is validated before the main sweep begins, allowing early termination of degenerate configurations. If XCOPA performance drops relative to full-LoRA baseline, this is flagged as a scope constraint and reported transparently rather than silently absorbed."
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026; commitment deadline August 2, 2026) — viable only with auto-research mode given the 15-day window from May 10, 2026",
    "EACL 2027 (ARR submission deadline August 3, 2026) — primary target for human-in-loop or manual mode",
    "AAAI 2027 (submission deadline expected July–August 2026, TBC)"
  ],
  "key_references": [
    "Rethinking Cross-lingual Alignment: Balancing Transfer and Cultural Erasure in Multilingual LLMs (arXiv:2510.26024, Han, Agrawal & Briakou, submitted Oct 2025, submitted to ICLR 2026; as of May 2026 listed as arXiv preprint on the first author's publication page)",
    "Neuron-Level Analysis of Cultural Understanding in Large Language Models (arXiv:2510.08284, Yamamoto et al., ICLR 2026)",
    "Bridging the Language Gaps in Large Language Models with Inference-Time Cross-Lingual Intervention / INCLINE (ACL 2025 Outstanding Paper, arXiv:2410.12462)",
    "Middle-Layer Representation Alignment for Cross-Lingual Transfer in Fine-Tuned LLMs (ACL 2025, arXiv:2502.14830, Liu & Niehues)",
    "Cross-Lingual Transfer of Cultural Knowledge: An Asymmetric Phenomenon (ACL 2025 short paper, arXiv:2506.01675)",
    "MLAS-LoRA: Language-Aware Parameters Detection and LoRA-Based Knowledge Transfer for Multilingual Machine Translation (ACL 2025, aclanthology.org/2025.acl-long.762)",
    "Continually Adding New Languages to Multilingual Language Models / LayRA (arXiv:2509.11414, September 2025)",
    "Mitigating Catastrophic Forgetting in Target Language Adaptation of LLMs via Source-Shielded Updates (arXiv:2512.04844, Nov 2025)",
    "Sparse Subnetwork Enhancement for Underrepresented Languages in Large Language Models (arXiv:2510.13580, Gurgurov et al., updated February 2026)",
    "AlignX: Advancing Multilingual Large Language Models with Multilingual Representation Alignment (EMNLP 2025, arXiv:2509.24338)",
    "CM-Align: Consistency-based Multilingual Alignment for Large Language Models (arXiv:2509.08541, 2025)",
    "Language Surgery in Multilingual Large Language Models / ITLC (arXiv:2506.12450, 2025)",
    "Improving Multilingual Language Models by Aligning Representations through Steering (arXiv:2505.12584, 2025)",
    "Localized Cultural Knowledge is Conserved and Controllable in Large Language Models (arXiv:2504.10191, 2025)",
    "CulturalBench: A Robust, Diverse, and Challenging Benchmark for Measuring LMs' Cultural Knowledge Through Human-AI Red-Teaming (ACL 2025, arXiv:2410.02677; evaluation-only — training use prohibited by OpenAI API annotation-platform terms)",
    "INCLUDE: Evaluating Multilingual Language Understanding with Regional Knowledge (ICLR 2025, arXiv:2411.19799; CC BY 4.0; 197,243 MCQA pairs across 44 languages and 52 countries; used for Stage 2 cultural-localization probe training)",
    "LoRA: Low-Rank Adaptation of Large Language Models (ICLR 2022, arXiv:2106.09685)",
    "XCOPA: Evaluation of Causal Commonsense Reasoning in Multiple Languages (EMNLP 2020, arXiv:2005.00333, Ponti et al.)",
    "Few-shot Learning with Multilingual Language Models / XStoryCloze (arXiv:2112.10668, Lin et al., 2022)",
    "Language Models are Multilingual Chain-of-Thought Reasoners / MGSM (arXiv:2210.03057, Shi et al., 2022)"
  ],
  "description": "Cross-lingual instruction fine-tuning demonstrably erases culturally-localized knowledge across all tested alignment approaches—yet no training-time prevention exists. Mechanistic work (arXiv:2504.10191) shows that in pre-trained instruction-tuned models, cultural knowledge is spatially localized as steerable activation-space vectors (in Gemma2-9b-it's 42-layer architecture, layers 19–30, with peak effects at layers 23 and 30 corresponding to approximately 55–71% model depth), suggesting specific layer indices implement cultural routing pathways. A parallel ICLR 2026 result (Yamamoto et al., arXiv:2510.08284) reaches an apparently different conclusion using gradient-based neuron attribution: culture-relevant neurons are concentrated in shallow-to-middle MLP layers. This methodological discrepancy—discrete high-influence neurons (gradient attribution) versus distributed representational subspaces (activation steering)—reflects different aspects of cultural knowledge implementation and constitutes a live empirical debate in the literature. Whether cultural localization persists after LoRA instruction fine-tuning—and whether erasure is behavioral (routing disruption) or representational (information loss)—is the empirical question Stage 1 answers. We propose Cultural-Layer-Selective LoRA (CLS-LoRA), which prevents both failure modes through a four-stage pipeline.\n\nA mechanistic bridge paragraph (placed before Stage 1) formalizes the training-time implication and acknowledges the mechanistic debate: the layer indices most sensitive to cultural activation steering at inference time identify weight matrices that implement cultural routing; LoRA updates to those weights may disrupt routing pathways; freezing those layers preserves both routing weights and residual-stream geometry. The contested layer localization (deep-layer subspaces per arXiv:2504.10191/arXiv:2510.26024 versus shallow-to-middle neurons per Yamamoto et al. ICLR 2026) is resolved not by choosing a side but by Stage 2 probing: measuring per-layer probe accuracy directly on each target model discovers the culturally-critical partition empirically, making CLS-LoRA robust to methodological disagreements in the mechanistic literature. Stage 1 distinguishes behavioral from representational erasure and determines whether KL regularization is necessary; crucially, Stage 1 trains separate linear probes on each checkpoint's frozen representations—one on the pretrained-checkpoint activations and one on the post-LoRA-checkpoint activations, both evaluated on the same held-out cultural split—so that accuracy differences reflect genuine representational change rather than activation-space reorganization.\n\nStage 2 runs lightweight linear probes to partition layers: factual-transfer probes trained on TyDiQA/XQUAD held-out splits; cultural-localization probes trained on INCLUDE (ICLR 2025, CC BY 4.0; 197,243 MCQA pairs from regional examinations across 44 languages and 52 countries, arXiv:2411.19799), filtered for cultural-domain categories (customs, food, celebrations, social norms), supplemented by multilingual Wikipedia paragraphs from culture-specific articles tagged with Wikidata cultural-domain categories (CC-BY-SA 4.0). CulturalBench (arXiv:2410.02677, ACL 2025) is reserved for Stage 4 evaluation only: the CulturalBench authors explicitly state that the annotation platform used OpenAI APIs under terms that prohibit using the collected data for training. SemEval-2026 Task 7 data (BLEnD extension) is also reserved strictly for final evaluation per its evaluation-only rules. Stage 2 determines the actual partition boundaries for each target model rather than hard-coding architecture-specific percentages from any single prior study—the principled response to the contested mechanistic landscape. Stage 3 applies LoRA exclusively to factual-transfer layers with an optional KL-divergence penalty; a 2×2 ablation isolates each component's contribution: (a) full LoRA no KL (baseline), (b) full LoRA + KL only (regularization-only, new), (c) CLS-LoRA frozen no KL (freezing-only), (d) CLS-LoRA frozen + KL (proposed method). Condition (b) is the critical new ablation: if it matches (d), layer partitioning is unnecessary overhead; if (c) and (d) outperform (b), layer freezing is confirmed as the operative mechanism. Stage 4 experiments run on Qwen3-8B (non-thinking mode, enable_thinking=False) and Aya-23-8B; primary evaluation uses CulturalBench (1,696 human-verified questions across 45 global regions, evaluation-only) and SemEval-2026 Task 7. Supplementary capability-regression evaluation via lm-evaluation-harness covers cross-lingual commonsense reasoning (XCOPA, 11 languages, zero-shot; task: xcopa_[lang]), narrative understanding (XStoryCloze, 11 languages, zero-shot; task: xstorycloze), and multilingual arithmetic (MGSM, 11 languages, direct mode; task: mgsm_direct); each requires ~2–4h per model and together add ~18–24h A100. If Stage 2's cultural-knowledge partition overlaps with commonsense-encoding layers, CLS-LoRA's freezing may constrain XCOPA transfer—a mechanistically informative finding reported transparently. arXiv:2510.26024 (submitted to ICLR 2026, OpenReview: forum?id=8DBHkEe0sm; as of May 2026, the first author's publication page lists it as an arXiv preprint without a confirmed proceedings venue) does not have publicly available evaluation code; the fallback evaluation framework (2D scatter of factual vs. cultural accuracy across languages, normalized to pretrained baseline) is specified explicitly and yields the same interpretive structure.\n\nCLS-LoRA is differentiated from MLAS-LoRA (ACL 2025) across three axes: task domain (MT quality vs cultural preservation), partition dimension (language-pair specificity vs factual-cultural semantic axis), and objective (translation accuracy via distillation vs cultural preservation with no distillation). CLS-LoRA is differentiated from LayRA (arXiv:2509.11414) across three axes: objective (language addition vs cultural knowledge preservation during instruction fine-tuning), partition axis (LayRA's source-encoding/English-reasoning/target-decoding functional axis vs CLS-LoRA's factual-transfer/cultural-localization semantic axis), and partition method (LayRA hard-codes layer indices from qualitative reasoning vs CLS-LoRA uses per-model empirical probing). CLS-LoRA is differentiated from Sparse Subnetwork Enhancement (arXiv:2510.13580) across two axes: objective (language performance improvement via LAPE-identified language-identity neurons vs cultural knowledge preservation during instruction fine-tuning) and partition axis (language-identity neurons that cut across semantic content vs the factual-transfer/cultural-localization semantic axis that cuts across language identity). The cultural-preservation objective remains the categorical novelty absent from all three. The auto-research sweep covers ~64–71 training runs (~122–144h H100), within the ≤200h H100 constraint, targeting a Pareto improvement over full-LoRA, Surgical Steering, INCLINE, MLAS-LoRA, and Source-Shielded Updates in the transfer-localization trade-off space, with XCOPA/XStoryCloze/MGSM as orthogonal capability regression checks."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0ffe8567-77f7-4610-9d74-c08f346994ae",
  "isSidechain": false,
  "requestId": "req_011CatXMwK3AsUJ94SgQFjkB",
  "type": "assistant",
  "uuid": "24d8af91-5031-41de-a863-728301f3d213",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_019wKr3xyUqDfyvH6PBrfqu1",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9399,
      "cache_read_input_tokens": 27616,
      "output_tokens": 14248,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9399,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14248,
          "cache_read_input_tokens": 27616,
          "cache_creation_input_tokens": 9399,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9399
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignme…",
  "leafUuid": "24d8af91-5031-41de-a863-728301f3d213",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix CulturalBench training-use constraint and add sparse-subnetwork baseline",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Layer-Selective LoRA Against Cultural Erasure in Cross-Lingual Alignme…",
  "leafUuid": "24d8af91-5031-41de-a863-728301f3d213",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Fix CulturalBench training-use constraint and add sparse-subnetwork baseline",
  "sessionId": "d8521c40-2131-41e0-b2da-32601bc8ea03"
}
```

---
