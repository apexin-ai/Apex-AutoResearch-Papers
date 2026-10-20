# Research conversation: You are a strict ML research reviewer conducting adversarial review. **Today's date: 2026-05-27 (UTC).** Your job: indep

**The Weakest Link Across Panel Sizes: Predictor Relevance Patterns in Multi-Judge LLM Evaluation under Adversarial Manipulation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 35
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-2/4f811c70-5276-4df8-92eb-dea6c34b39ff.jsonl`
- **Structured JSON:** [`a9cb8cba710bd9332b34.json`](../../sessions/a9/a9cb8cba710bd9332b34.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T23:06:43.018Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T23:06:43.018Z",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "content": "You are a strict ML research reviewer conducting adversarial review.\n\n**Today's date: 2026-05-27 (UTC).**\n\nYour job: independently verify this idea's claims via web_search, then issue a verdict.\n\n## User requirements\nThe user asked for: **Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding**\nEvaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be \"revise\" or \"fail\".\n\n## 核心要求：非常仔细地调研，非常仔细地思考\n\n你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。\n\n### 调研要求\n\n1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。\n   每个验证维度建议用 2-3 种不同的搜索查询。\n\n2. **可行性深度检查**：\n   - 搜索类似实验的实际成本/周期\n   - 检查 claimed baselines 是否可复现\n   - 验证所需的 datasets/models 是否真的可以获取\n\n3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：\n   - 尝试不同的关键词组合\n   - 同时检查 arXiv 和 conference proceedings\n   - 寻找相邻领域的并行/concurrent 工作\n\n4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。\n\n### 思考要求\n\n5. **独立判断**：\n   - 不要因为 Generator 说得有道理就轻易 pass\n   - 思考这个 idea 在实际执行中会遇到什么困难\n   - 考虑这个 idea 对领域的真实贡献\n\n6. **评分诚实**：\n   - 4 分意味着\"确实很好\"，5 分意味着\"令人兴奋\"\n   - Agent 评分经常虚高，你的职责就是纠正这种偏差\n\n\n## 论文搜索策略\n\n你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。\n\n### 搜索源（推荐每个维度使用 2 个不同来源）\n\n1. **arXiv 预印本**（最新工作）:\n   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文\n   - `site:arxiv.org {method_name}` — 按具体方法名搜索\n   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作\n\n2. **Google Scholar**（引用关系 + 综合覆盖）:\n   - `{topic} 2026 site:scholar.google.com`\n   - `\"{exact paper title}\"` — 验证论文是否真实存在\n   - `\"{author name}\" {topic} 2026` — 按活跃作者追踪\n\n3. **Papers With Code**（SOTA 排行 + 代码可用性）:\n   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜\n   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局\n\n4. **OpenReview**（会议审稿 + 同行评价）:\n   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文\n   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价\n\n5. **Semantic Scholar**（语义搜索 + 引用图谱）:\n   - `semantic scholar {topic} survey 2026` — 找综述论文\n\n6. **GitHub**（实现验证）:\n   - `site:github.com {method_name} {task}` — 验证开源实现是否存在\n\n### 搜索维度\n\n1. **正向搜索**：直接搜索主题相关论文\n2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？\n3. **相邻领域搜索**：其他领域是否已解决类似问题\n4. **反面搜索**：找到反对你 idea 的证据\n5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work\n\n\n## 竞争论文专项搜索（Reviewer 独有）\n\n1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题\n2. **知名团队追踪**：搜索相关团队最近的论文\n3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`\n4. **arXiv 近 3 个月密集搜索**\n\n## Review checklist\n1. **SOTA freshness**: Are baselines actually current SOTA?\n2. **Reference verification**: Do cited papers actually exist?\n3. **Gap validity**: Does the claimed gap still exist?\n4. **Venue validity**: Are target venue deadlines after 2026-05-27?\n5. **Feasibility**: Is the resource estimate realistic?\n6. **Novelty**: Is this sufficiently different from existing work?\n7. **Cost realism**: Are the three mode estimates internally consistent?\n\n## Idea under review (round 5/10)\n{\n  \"title\": \"Composition Fidelity RL: Unifying Evidence Grounding, Binding Validity, and Integration Completeness via a Distilled Composition Verifier\",\n  \"core_problem\": \"How can we train multimodal reasoning models to produce verifiably faithful perception-reasoning integration — where each reasoning step explicitly cites visual evidence, citations are grounded, inferences are logically consistent with cited evidence, and all task-relevant visual facts are integrated — using a single lightweight composition verifier rather than expensive per-step VLM judges or statistical attention proxies?\",\n  \"opportunity\": \"Recent work has made significant progress on components of faithful multimodal reasoning: PEARL (CVPR 2026) gates reasoning on perception accuracy, FGRPO (Apr 2026) constrains consistency and semantic grounding via per-sentence VLM judge calls using Qwen3-VL-30B-A3B, Faithful-MR1 (May 2026) anchors attention to causal image regions, PaLMR (CVPR 2026) enforces process-level visual fidelity through V-GRPO with binary perception gating, MJ1 (Mar 2026) trains a 3B judge with a structured grounded verification chain for evaluation, token-level credit methods (PGPO, SAYO, AT-RL, VICRA, KAWHI) reweight optimization toward visually-dependent tokens, TreeVGR (ICLR 2026) trains models to generate bounding-box evidence via RL with dual IoU reward, v1 (May 2026) constructs 300K reasoning traces with interleaved visual grounding via point-and-copy embedding re-access, VTPerception-R1 implements perception-aware RL with visual/textual/consistency rewards, SIEVE (Mar 2026) trains models to iteratively re-access cached visual evidence embeddings during RL, and Vision-SR1 decomposes reasoning into explicit perception and reasoning stages with structured tags, using the model's own re-prompted answer (without image access) as a self-reward signal. Yet a systematic gap remains along three axes: (1) No method verifies integration *completeness* — whether all task-relevant visual facts are bound to reasoning steps, which MathLens (Feb 2026) identifies as the growing error fraction and 'Don't Blink' (Apr 2026) shows worsens as reasoning unfolds (attention to evidence regions drops >50%). (2) Methods that check semantic binding (FGRPO) rely on per-sentence VLM judge calls during training, creating multiplicative cost overhead (~6-8 judge calls per sentence × multiple sentences per trace × rollouts per prompt). (3) Attention-based methods (PGPO, SAYO, Faithful-MR1) and embedding-level methods (v1, SIEVE) use statistical or representational proxies for visual dependency rather than verifying the *semantic correctness* of how evidence is used in reasoning. (4) Self-rewarding approaches (Vision-SR1) check perceptual *self-containment* — whether the perception text suffices to answer without the image — but not whether the perception is *factually correct* relative to the image, nor whether inferences logically follow from cited evidence. (5) Structured verification approaches like MJ1's grounded chain operate at evaluation time, not as training-time reward signals, and do not check completeness. (6) Spatial grounding methods (TreeVGR, ViGoRL) verify *where* the model looks but not *what* it concludes from what it sees — bounding-box IoU confirms localization, not reasoning validity. The PAR framework (Mar 2026) further diagnoses that 'alignment' — the mapping of perceived facts to symbolic representations — is a distinct failure mode from perception or reasoning alone. However, MuRGAt (Feb 2026) documents a critical cautionary finding: enforcing structured grounding in zero-shot/few-shot settings can degrade accuracy, revealing a gap between internal reasoning and verifiable attribution. The opportunity is to unify grounding verification, binding validity, and completeness checking in a single distilled lightweight verifier that serves as a training-time composition reward signal — with RL training to develop citation as a learned skill rather than a post-hoc constraint.\",\n  \"landscape\": \"The landscape of RL-based multimodal reasoning training has exploded in early 2026 along seven axes:\\n\\n**Perception-gating methods:** PEARL (CVPR 2026) derives a perception checklist of factual sub-questions, computes a perceptual reward R̄_p, and uses it as a fidelity gate — blocking reasoning policy updates when perception fails. Gains: +6.6% over GRPO on MathVerse. Limitation: checks perception accuracy but not whether perceived facts are correctly *bound* to reasoning steps or whether integration is *complete*. PaLMR (CVPR 2026, arXiv:2603.06652) introduces V-GRPO (Vision-Guided GRPO) with a hierarchical reward R = S_vis × (α·S_ans + (1−α)·S_fmt), where S_vis is a binary visual fidelity gate computed via pairwise comparison against pseudo ground-truth image descriptions generated by Gemini. Achieves 70.9% on HallusionBench (+4.2pp over GRPO) with only 4,728 training instances and 88% model-human alignment. Limitation: uses external pseudo ground-truth for comparison rather than verifying the model's own explicit evidence citations; does not check completeness; binary gating provides no gradient signal for partial fidelity improvement.\\n\\n**Token-level credit reallocation methods:** VPPO (ICLR 2026) reweights by KL divergence on perturbed images. PGPO (Apr 2026) amplifies learning signals for visually-dependent tokens via threshold-gated advantage reallocation (+18.7% avg). VGPO (ACL 2026) adds visual attention compensation. AT-RL (Feb 2026) identifies ~15% anchor tokens via cross-modality connectivity for targeted credit assignment (+1.2% overhead, 32B surpasses 72B-Instruct). VICRA (2026) reallocates optimization toward visually-grounded tokens (+2.25 avg on Qwen2.5-VL-7B). KAWHI (Mar 2026) performs paragraph-level credit reallocation via structured attribution of vision-critical attention heads. SAYO (Feb 2026) introduces region-level visual attention reward (r_v = tanh(log(a_q/v_q))) on Qwen3-VL-8B. Collective limitation: all operate on statistical attention patterns rather than verifying the semantic correctness of evidence-to-reasoning binding.\\n\\n**Explicit evidence grounding in RL training:** TreeVGR (ICLR 2026) trains models to generate text-space bounding box coordinates as traceable evidence within reasoning trajectories, supervised via dual IoU reward (R_IoU = ½(R_IoU^R + R_IoU^P)) that balances precision and recall of spatial localization. Two-stage training (SFT on 37K samples + RL). Achieves +16.8 on V*Bench, +12.6 on MME-RealWorld. Limitation: verifies *spatial* localization via IoU but not the *semantic validity* of how localized evidence is used in reasoning — a correct bounding box around a labeled angle does not verify that the angle value was correctly read or correctly applied in an inference step. Does not check integration completeness. v1 (May 2026, arXiv:2505.18842) introduces a point-and-copy mechanism where the model selects relevant image patches and copies their embeddings back into the reasoning stream, maintaining visual grounding throughout multi-step reasoning. Trained via SFT on v1g (300K grounding-annotated traces); RL integration is noted as future work. Achieves 68.6% MathVista, 34.5% MathVision. Limitation: operates at the embedding/representation level — re-inserts visual features but does not produce explicit textual evidence citations that can be externally verified for semantic correctness; grounding is implicit in the representation space rather than auditable. VTPerception-R1 (arXiv:2509.24776) implements a two-stage framework (perception-augmented SFT + perception-aware RL) with three perception rewards: visual key-info coverage (R_vkey), textual key-info coverage (R_tkey), and consistency (R_cons = |F_ans∩E|/max(1,|F_ans|)). Achieves 82.5% AI2D, 71.0% MathVista. Limitation: R_vkey measures perception-level element coverage (are visual elements mentioned?) but does not verify binding validity (are inferences logically consistent with cited evidence?) or integration completeness (are all task-relevant facts addressed?). SIEVE (arXiv:2603.14117) trains models to iteratively re-access cached visual region embeddings during RL (GRPO with ℛ = λ₁ℛ_res + λ₂ℛ_format + λ₃ℛ_emb + λ₄ℛ_act), supporting multi-turn evidence refinement. Achieves +7.85 on V*Bench overall. Limitation: like v1, operates at the embedding level — re-inserted features improve grounding but don't produce explicit verifiable citations; iterative re-access addresses the evidence-loss problem but not semantic verification of how evidence supports conclusions.\\n\\n**Self-rewarding perception-reasoning decomposition:** Vision-SR1 (arXiv:2508.19652) decomposes reasoning into explicit &lt;visual_perception> and &lt;think> stages, requiring the model to first articulate a self-contained visual description, then reason from it. The visual reward is computed via self-rewarding: the frozen policy model is re-prompted to answer the question using only the generated visual perception text (without image access); if the correct answer is derived from perception alone, a visual reward of 1 is assigned. Uses GRPO with a decoupled reward-advantage framework that maintains separate advantages for visual and answer rewards. Three-stage training: SFT cold-start on 9K examples, then standard rollout with accuracy reward, then self-reward rollout. Achieves 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B (+1.4 over Vision-R1), 69.8 on HallusionBench. Key distinction from CFRL: (a) Vision-SR1 uses self-rewarding (same model judges itself) rather than an external distilled verifier — the reward is whether perception suffices to re-derive the answer, not whether each cited fact is *factually accurate* relative to the image; a hallucinated but internally consistent perception could score high. (b) Vision-SR1 checks perceptual *self-containment* (can you answer from perception alone?) while CFRL checks factual grounding accuracy (is the perception correct?), binding validity (does the inference follow from cited evidence?), and completeness (are all task-relevant facts covered). (c) Vision-SR1 does not verify the logical consistency between perceived evidence and drawn inferences — it treats perception and reasoning as decomposed stages but does not check whether the reasoning is faithful to the specific evidence cited.\\n\\n**Constrained/faithful training methods:** FGRPO (Apr 2026, arXiv:2604.08476) enforces consistency + semantic grounding + spatial grounding as constraints via Lagrangian dual ascent, reducing inconsistency from 24.5% to 1.7% and improving grounding by +13 points. Uses Qwen3-VL-30B-A3B-Instruct (MoE, ~3.3B active parameters) as the online judge during training. The semantic grounding reward R_S requires per-sentence VLM judge calls: each non-trivial visual sentence in the CoT is independently evaluated, resulting in ~30-55 judge calls per training sample. This is the closest competitor — but does not check integration completeness. Faithful-MR1 (May 2026) supervises a &lt;Focus> token's attention against image regions and uses counterfactual image intervention to reward attention concentration where vision causally matters. Operates on attention distributions rather than explicit evidence citations.\\n\\n**Structured verification and evaluation judges:** MJ1 (Mar 2026, arXiv:2603.07990) trains a 3B-active-parameter multimodal judge (based on Qwen3-VL-30B-A3B) using RL with a structured grounded verification chain: observations → claims → verification → evaluation → scoring, enforced via 11 required XML tags across 5 sequential stages. Achieves 77.0% on MMRB2, surpassing GPT-5 (72.2%) and Gemini-3-Pro (76.3%). Key distinction from CFRL: (a) MJ1 is an *evaluation-time* judge, not a training-time reward verifier; (b) MJ1 uses stage-separated grounding rather than inline evidence citations; (c) MJ1 performs pairwise response comparison, not composition property verification; (d) MJ1 does not check integration completeness. EVPV/Grounding the Score (Mar 2026) adds visual premise verification via constraint matching and reliability gating to PRMs — improves Best-of-N reranking but is *inference-only*. ViGoRL (2026) trains models to produce spatially grounded reasoning traces with coordinate-level evidence (86.4% on V*Bench) — addresses spatial grounding but not semantic binding validity. AutoRubric-R1V (arXiv:2510.14738) auto-generates rubric-based process rewards by distilling consistent reasoning checkpoints from successful trajectories via self-aggregation — rubric reward equals the fraction of satisfied checkpoints. Achieves +8.0 avg over Qwen2.5-VL-7B on 6 benchmarks. Distinct from CFRL: AutoRubric derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image; rubrics are answer-path-dependent rather than evidence-grounding-dependent. CoRGI (arXiv:2508.00378) performs post-hoc step-wise verification of CoT reasoning by decomposing rationales into step-wise statements, grounding each step in visual evidence via Grounding DINO, and filtering unsupported claims. Inference-time only; conceptually related to CFRL's verification chain but does not serve as a training-time reward signal.\\n\\n**Evidence-aware GRPO variants:** PRCO (Mar 2026) decomposes into Observer+Solver with separate utility/outcome rewards (+7 pts). DocR1 (2026) uses evidence-page guided GRPO for document understanding. OpenMMReasoner (CVPR 2026) achieves +11.6% over Qwen2.5-VL-7B via two-stage SFT+RL recipe.\\n\\n**Attribution and evidence-loss diagnostics:** MuRGAt (Feb 2026, arXiv:2602.11509) introduces a benchmark for multimodal fact-level attribution requiring models to generate explicit citations specifying modality and temporal segments. Critically, MuRGAt finds that 'increasing reasoning depth or enforcing structured grounding often degrades accuracy' in zero-shot/few-shot settings — even strong MLLMs frequently hallucinate citations despite correct reasoning. This documents an accuracy-faithfulness tradeoff that CFRL must address. 'Don't Blink: Evidence Collapse during Multimodal Reasoning' (Apr 2026, arXiv:2604.04207) documents that reasoning VLMs progressively lose visual grounding as reasoning unfolds — attention to annotated evidence regions drops >50% — creating confident but ungrounded predictions that text-only monitoring cannot detect. 'Deeper Thought, Weaker Aim' (Mar 2026, arXiv:2603.14184) independently confirms this, showing reasoning prompts significantly reduce attention to question-critical image regions. 'Compose and Fuse' (ICLR 2026) identifies task-composition and fusion as main barriers. MathLens (Feb 2026) shows integration failures grow as a fraction of remaining errors. The PAR framework (Mar 2026) decomposes multimodal math reasoning into Perception–Alignment–Reasoning and identifies alignment fragmentation as a distinct failure mode.\\n\\n**The gap:** PEARL and PaLMR check perception but not binding or completeness; FGRPO checks consistency+grounding but not completeness, with ~5-8x higher cost per rollout vs. single-pass verification; Vision-SR1 decomposes perception and reasoning with self-rewarding but does not verify factual grounding accuracy, binding validity, or completeness; TreeVGR and ViGoRL verify spatial localization but not semantic reasoning validity; v1 and SIEVE re-access visual evidence at the embedding level but don't produce auditable textual citations; VTPerception-R1 checks perception-level coverage but not binding validity or completeness; MJ1 demonstrates structured grounded verification chains but operates at evaluation time; AutoRubric-R1V provides process supervision via trajectory-mined rubrics but not composition property verification against the image; CoRGI performs step-wise visual verification but is inference-only; attention-based methods (PGPO, SAYO, AT-RL, Faithful-MR1) use statistical proxies; EVPV is inference-only. No existing method unifies all three composition properties (evidence grounding, binding validity, integration completeness) in a single lightweight training-time verifier. MuRGAt's accuracy-faithfulness tradeoff highlights that naive enforcement of structured citation degrades performance — but this was observed under zero-shot prompting, not RL training with curriculum scheduling.\",\n  \"inspired_by\": \"'Compose and Fuse' (ICLR 2026) explicit future direction for composition-aware training; MathLens integration-failure analysis; PAR framework's alignment decomposition; FGRPO's grounding+consistency insight (extended with completeness and efficiency); MJ1's structured verification chain (adapted from evaluation-time judge to training-time reward); PaLMR's visual fidelity gating (extended beyond binary gating to multi-property verification); TreeVGR's explicit evidence generation in RL (extended from spatial to semantic verification); v1's interleaved grounding paradigm (adapted from embedding-level to textual-citation-level); Vision-SR1's perception-reasoning decomposition with self-rewarding (extended from self-containment checking to external factual grounding + binding + completeness verification); MuRGAt's accuracy-faithfulness tradeoff (motivating curriculum training and accuracy-first reward scheduling); 'Don't Blink' and 'Deeper Thought, Weaker Aim' documenting evidence collapse (direct motivation for explicit evidence anchoring); 'An Imperfect Verifier is Good Enough' (Apr 2026) validating noisy-reward robustness for distilled verifiers; GeoSketch's symbolic reward for geometry; Geoparsing (Apr 2026) for formal diagram entity extraction; Chart-RVR's verifiable chart reasoning rewards (informing chart-domain binding checks); CHARGE's keypoint coverage metrics; Countdown-Code (2026) and PURE (2025) for reward hacking diagnosis and mitigation\",\n  \"approach\": \"We propose Composition Fidelity RL (CFRL), which unifies evidence grounding, binding validity, and integration completeness verification in a single distilled composition verifier used as a GRPO training reward.\\n\\n**Structured output format:** The model generates responses with explicit &lt;observe entity='...' value='...'/> tags for visual evidence extraction and &lt;reason evidence='obs1,obs2' rule='...'> blocks for each reasoning step, requiring citation of specific observations and the inference rule applied. This explicit citation format enables automated verification — unlike attention-based methods that can only measure statistical dependency, or embedding-level methods (v1, SIEVE) that re-access visual features without producing auditable textual claims. Compared to TreeVGR's bounding-box coordinates, our citations capture *semantic* content ('radius = 5cm') rather than *spatial* location ([x1,y1,x2,y2]), enabling verification of whether the cited value is correct and whether the inference logically follows. Compared to MJ1's stage-separated verification chain, our format embeds evidence references *inline* with reasoning, creating direct referential links suitable for training-time throughput. Compared to Vision-SR1's &lt;visual_perception> block, our format provides *fine-grained, per-fact citations* (individual &lt;observe> tags) rather than a monolithic perception paragraph, enabling per-fact grounding verification and explicit evidence-to-inference linking via the evidence='obs1,obs2' attribute.\\n\\n**Addressing the accuracy-faithfulness tradeoff (MuRGAt):** MuRGAt (Feb 2026) found that enforcing structured grounding degrades accuracy in zero-shot/few-shot settings — models hallucinate citations despite correct reasoning. This is a direct challenge to CFRL's premise. We address it through four design choices: (1) *RL training develops citation as a learned skill*: unlike MuRGAt's zero-shot evaluation where citation is an imposed constraint, CFRL trains the model to produce faithful citations through reward optimization, allowing the model to develop integrated reasoning-citation capability rather than retrofitting citations onto existing reasoning. (2) *Accuracy-first curriculum scheduling*: Phase 0 (pre-curriculum) establishes answer accuracy via standard GRPO before introducing any citation requirements, ensuring the model's reasoning capability is preserved before grounding constraints are layered on. Citation rewards are introduced gradually with initial weight near zero, increasing only as the model demonstrates stable accuracy. (3) *Accuracy-dominant reward weighting*: R_accuracy receives weight α ≥ 0.4 throughout training, ensuring citation quality never dominates at the expense of answer correctness. If accuracy on a held-out validation set drops >2pp at any curriculum transition, citation reward weights are halved until accuracy recovers. (4) *Counterfactual validation* (safeguard #5) directly monitors for MuRGAt-style degradation by comparing tagged vs. untagged accuracy.\\n\\n**Composition Fidelity Verifier (CFV) — three-property checking:**\\n(1) *Evidence grounding*: Checks whether cited visual facts (in &lt;observe> tags) correspond to actual image content. Uses a lightweight visual QA module that converts each citation into a yes/no visual question (e.g., 'Is the radius labeled as 5cm in the image?'). Inspired by PEARL's perception checklist but applied to model-generated citations rather than externally-derived sub-questions.\\n(2) *Binding validity*: Checks logical consistency between cited evidence and the inference drawn. We define binding validity checks at two levels:\\n\\n  **Tier 1 — Domain-agnostic arithmetic + geometry symbolic (core contribution):**\\n  - *Arithmetic verification* (all domains): Given numerical values extracted from &lt;observe> tags and a stated operation in the &lt;reason> block, verify computational correctness via symbolic execution. Concrete checks: (a) *Sum/difference/product/quotient consistency* — if obs1 cites 'value A = 45' and obs2 cites 'value B = 30', and the reason block claims 'difference = 15' with rule 'subtraction', verify 45−30=15. (b) *Ratio/percentage verification* — if 'Part = 120, Total = 400' and conclusion is '30%', verify 120/400=0.30. (c) *Comparison consistency* — if the reason block claims 'A > B' citing obs1 (A=45) and obs2 (B=30), verify 45>30. (d) *Multi-step arithmetic* — chain verification across sequential &lt;reason> blocks where one step's output is another's input. These checks are domain-agnostic: they apply equally to geometry problems (angle computations), chart problems (bar value comparisons, trend calculations), and diagram problems (counting, distance computations).\\n  - *Geometry symbolic theorem matching*: Cited theorems/rules are matched against a geometry theorem library, and symbolic constraints are verified formally. For example, cited 'angle A=60°, angle B=90°' with rule 'triangle angle sum' → verify 60+90+x=180 → x=30°. Inspired by GeoSketch and the PAR framework.\\n\\n  **Tier 2 — Domain-specific binding checks (extension):**\\n  - *Chart-specific*: (a) *Ordering consistency* — if 'Bar A > Bar B' is cited, verify against the extracted data table that value(A) > value(B). (b) *Extrema verification* — if 'X is the maximum value' is cited, verify X = max(all values in series). (c) *Trend verification* — if 'increasing from 2020 to 2023' is cited, verify monotonic increase in the relevant data points; trends are formally defined as: 'increasing' requires each successive value ≥ previous (strict: >), 'decreasing' requires ≤ (strict: <), with tolerance ε for noise. (d) *Aggregation verification* — if 'average = X' is cited, verify mean(values) ≈ X within 1% relative tolerance. These checks require the chart data table extracted in the completeness pipeline (Stage A), linking Tier 2 binding to Tier 2 completeness infrastructure.\\n  - *Diagram-specific*: (a) *Structural relationship verification* — if 'A connects to B' is cited, verify edge (A,B) exists in the parsed graph from PGDP-Net. (b) *Attribute consistency* — if 'node A is labeled X' is cited, verify label(A) = X in the parsed representation. (c) *Cardinality verification* — if 'A has 3 connections' is cited, verify degree(A) = 3. (d) *Containment/hierarchy* — if 'A is inside B' is cited, verify the containment relation in the parsed spatial layout. These checks require the diagram graph representation from Stage A parsing.\\n  - *Fallback for inapplicable checks*: When a &lt;reason> block involves qualitative reasoning that cannot be reduced to arithmetic or structural constraint checking (e.g., 'the diagram suggests a causal relationship between X and Y'), the binding check returns a neutral score (0.5) rather than penalizing, and the verifier flags it as 'unverifiable-binding' for monitoring. This prevents the binding reward from penalizing valid qualitative reasoning while maintaining signal for verifiable steps.\\n\\n(3) *Integration completeness*: Checks whether all task-relevant visual facts are cited somewhere in the reasoning chain via a three-stage domain-specific pipeline:\\n\\n  **Stage A — Visual Element Enumeration** (domain-specific, offline or cached):\\n  - *Geometry*: Use Geoparsing (arXiv:2604.11600, Apr 2026) to produce a formal entity/relation set from the diagram. Geoparsing achieves 96.4 F1 overall (points 99.6, lines 98.0, circles 98.3, semantics 90.7) using a unified formal language.\\n  - *Charts*: Use DePlot/UniChart-style chart derendering to extract a linearized data table of all data points, then apply CHARGE-style keypoint extraction to convert to self-contained factual statements.\\n  - *Diagrams*: Use PGDP-Net-style graph parsing to extract a node-edge representation of diagram primitives and their relations.\\n\\n  **Stage B — Question-Conditioned Relevance Filtering**:\\n  - Apply VisDoT-style (arXiv:2603.11631) question decomposition to generate ordered perception sub-questions. Match sub-questions against enumerated visual elements from Stage A to produce a *required visual fact set* F_required.\\n  - Reliability estimate: Sub-question coverage as a ranking metric achieves 82% accuracy against human preferences (arXiv:2410.15531), with human inter-annotator agreement of 74.6% on sub-question classification — indicating this is an inherently noisy signal, which motivates our soft treatment of completeness (see below).\\n  - For geometry, the symbolic checker provides an additional signal: any entity appearing in the formal solution path is automatically added to F_required.\\n\\n  **Stage C — Coverage Verification**:\\n  - Compute coverage score: R_completeness = |F_cited ∩ F_required| / |F_required|.\\n  - We target ≥80% recall of task-relevant facts, acknowledging that completeness checking is inherently approximate. The 80% threshold is motivated by CHARGE's finding that even SOTA MLLMs achieve only 73.9% coverage with ground-truth retrieval.\\n  - For facts in F_required that are NOT cited, the verifier generates a soft penalty proportional to the estimated importance of the missing fact.\\n\\n**Verifier architecture and cost model:** The CFV (4B parameters, based on Qwen3-VL-4B) performs all three property checks in a single autoregressive forward pass. The input consists of the image + the model's full tagged response + a structured verification instruction. The CFV generates verification judgments sequentially as autoregressive output: for each &lt;observe> tag, it produces an inline grounding verdict (verified/unverified with confidence score); for each &lt;reason> block, it produces a binding validity verdict; and finally, it produces an overall completeness assessment. This is architecturally identical to how MJ1 generates its multi-stage verification chain in one forward pass — the grounding VQA for each observation is performed as internal sub-reasoning within the autoregressive generation, NOT as separate VQA calls. The output length scales with the number of observations and reasoning steps (~500-1500 tokens for typical responses with 4-8 observations), but requires only a single image encoding through the vision encoder.\\n\\n**Cost comparison with FGRPO (precise):** FGRPO requires S separate judge calls per rollout (S ≈ 5-8 visual sentences), each requiring its own image encoding through the 30B MoE model (3.3B active parameters). CFRL requires 1 verifier call per rollout with a single image encoding through the 4B dense model. Since image encoding is the dominant cost in VLM inference (processing hundreds of visual tokens through transformer layers), the savings from 1 vs. S encodings is the primary cost driver. Per-call text generation cost is roughly comparable: FGRPO generates S × ~150 = 750-1200 tokens total across all calls; CFRL generates ~500-1500 tokens in one call, at similar active parameter counts (3.3B MoE vs. 4B dense). The effective cost reduction is **~5-8x per rollout** (proportional to S), driven primarily by the single image encoding. Per training sample with K rollouts, FGRPO makes K×S judge calls vs. CFRL's K verifier calls — the same ~5-8x ratio holds. For Tier 1 (grounding + binding only), where binding validity uses lightweight symbolic/arithmetic checking outside the verifier, the verifier output is shorter (~300-800 tokens), further reducing per-call cost.\\n\\n**Staged contribution and risk mitigation (addressing system complexity):** The full CFRL system integrates multiple external tools and domain-specific pipelines, creating compounding failure risk. We structure the contribution in two defensible tiers:\\n\\n  *Tier 1 — Core contribution (grounding + binding):* Evidence grounding (VQA-based, all domains) and binding validity (domain-agnostic arithmetic verification + geometry symbolic theorem matching). This tier requires only the distilled 4B verifier and a geometry theorem library — no external parsing tools. Domain-agnostic arithmetic verification applies to chart and diagram problems too (any reasoning step involving numerical computation is checkable), providing cross-domain binding signal even without domain-specific infrastructure. This tier is self-contained, already differentiates from all existing methods (none verify binding validity as a training reward), and provides a defensible paper even if completeness checking and domain-specific binding prove too approximate. Estimated complexity: 1 distilled model + 1 theorem library.\\n\\n  *Tier 2 — Extension (completeness + domain-specific binding):* Integration completeness adds Geoparsing, DePlot/CHARGE, PGDP-Net, and VisDoT-style decomposition. Domain-specific binding for charts adds data-table-dependent checks (ordering, trends, extrema); for diagrams adds graph-dependent checks (structural relationships, attributes). Each integration is a potential failure point. Fallback strategies per component: (a) If Geoparsing underperforms on out-of-distribution diagrams, fall back to the distilled verifier's own visual element listing (lower accuracy but zero external dependency). (b) If relevance filtering is too noisy, use only the symbolic solver's required entities (geometry) or question-mentioned entities (charts/diagrams) as F_required — a conservative underestimate that still provides signal. (c) If domain-specific binding checks add noise rather than signal (e.g., trend verification on noisy data), fall back to Tier 1 arithmetic-only binding for that domain. (d) If end-to-end completeness R_completeness adds noise rather than signal, set δ=0 and report Tier 1 results as the core finding.\\n\\n  *Risk matrix:*\\n  - Pipeline integration failure (MEDIUM risk): Mitigated by Tier 1/Tier 2 separation and per-component fallbacks.\\n  - Verifier distillation quality (LOW risk): Validated via held-out test set; noise tolerance demonstrated by 'Imperfect Verifier' methodology.\\n  - Accuracy-faithfulness tradeoff (MEDIUM risk): Mitigated by accuracy-first curriculum, accuracy-dominant reward weighting, and counterfactual monitoring (see MuRGAt discussion above).\\n  - Tag gaming / Goodhart effects (LOW-MEDIUM risk): Mitigated by five anti-gaming safeguards (see below).\\n  - Training instability from 5 reward components (MEDIUM risk): Mitigated by curriculum scheduling (components introduced sequentially, not simultaneously) and reward weight monitoring.\\n\\n**Verifier distillation:** The CFV is distilled from Qwen3-VL-235B-A22B on synthetically generated composition judgment pairs. We generate correct/incorrect binding examples by: (a) taking model solutions, (b) perturbing citations (wrong entity, wrong value, missing citation, irrelevant citation, logically inconsistent inference, arithmetic errors), (c) having the teacher label each perturbation type. Target: 50K examples across geometry, chart, and diagram domains, with balanced representation of arithmetic binding errors (Tier 1) and domain-specific binding errors (Tier 2). The distilled verifier (based on Qwen3-VL-4B) is validated on a held-out test set of 5K human-annotated composition judgments.\\n\\n**Verifier validation protocol**: Before deployment as a reward signal, we validate the CFV via: (a) held-out precision/recall on each of the three sub-tasks separately — with Tier 1 binding validated separately for arithmetic and geometry-symbolic components, (b) ablation studying verifier accuracy vs. downstream model quality by injecting controlled noise (5%, 10%, 15%, 20%) into reward signals, following the methodology of 'An Imperfect Verifier is Good Enough' (2026). (c) If CFV accuracy on binding validity falls below 75%, we activate the fallback: softening binding rewards to a probabilistic consistency score weighted by verifier confidence.\\n\\n**Anti-gaming safeguards** (addressing Goodhart's Law risk):\\n  (1) *Low format weight*: Format compliance ≤0.05 in composite reward. Dominant signals come from verifiable content-level checks.\\n  (2) *Verifiable citation grounding*: Evidence grounding is checked against actual image content via visual QA — un-gameable.\\n  (3) *Answer-leak detection*: Embedding cosine similarity monitoring between &lt;observe> content and final answer, with penalty P_leak.\\n  (4) *KL regularization against base policy*: Standard KL penalty + format/content reward ratio monitoring; divergence triggers early stopping.\\n  (5) *Counterfactual validation*: Every 500 steps, evaluate with tags stripped. If tagged accuracy exceeds untagged by >5pp, signal format-dependent performance and trigger reward recalibration.\\n\\n**Training:** GRPO on Qwen3-VL-8B via veRL with composite reward R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness + ε·R_format − P_leak. Curriculum training: Phase 0 establishes baseline accuracy (week 1), Phase 1 trains grounding (weeks 1.5-2.5), Phase 2 adds binding validity (weeks 2.5-3.5), Phase 3 adds completeness (weeks 3.5-4.5). Training targets geometry (MathVerse, GeoQA+), chart (ChartQA, PlotQA), and diagram (AI2D, ScienceQA) tasks.\\n\\n**Key distinction from Vision-SR1:** Vision-SR1 decomposes reasoning into &lt;visual_perception> and &lt;think> stages and checks perceptual self-containment via self-rewarding — re-prompting the model without image access to verify the perception suffices. CFRL differs in three ways: (a) CFRL uses an external distilled verifier rather than self-rewarding — self-rewarding cannot detect hallucinated perceptions that happen to be internally consistent (a fabricated but plausible description could still support the correct answer), while external grounding verification checks each cited fact against the actual image. (b) CFRL provides fine-grained per-fact citations (&lt;observe> tags) rather than a monolithic perception block, enabling per-fact grounding verification and explicit evidence-to-inference linking. (c) CFRL verifies binding validity (does the inference logically follow from cited evidence?) and integration completeness, which Vision-SR1 does not address.\\n\\n**Key distinction from TreeVGR:** TreeVGR generates bounding-box coordinates as evidence and supervises spatial localization via dual IoU reward — verifying *where* the model attends. CFRL generates semantic textual citations and verifies *what* the model claims to see and *how* it reasons from those claims. These are complementary: TreeVGR could locate the correct region but misread the value; CFRL catches such semantic errors. TreeVGR does not check binding validity or integration completeness.\\n\\n**Key distinction from v1 and SIEVE:** Both re-access visual evidence at the embedding level — v1 via point-and-copy of patch embeddings, SIEVE via cached region embedding re-insertion. This maintains visual grounding in the model's internal representation but does not produce *explicit, auditable textual claims* about what was perceived. CFRL requires the model to articulate its visual evidence in natural language, enabling external verification of both the perception (grounding) and the reasoning (binding validity). v1 uses SFT only; SIEVE uses RL but without composition-level verification.\\n\\n**Key distinction from VTPerception-R1:** VTPerception-R1's R_vkey/R_tkey rewards check perception-level element coverage (whether visual/textual elements are mentioned in reasoning), while R_cons checks entity-attribute consistency. CFRL goes further in two ways: (a) binding validity checks logical inference consistency, not just entity-mention consistency, and (b) integration completeness checks coverage of all task-relevant facts via structured enumeration, not just key-info recall from a VLM scorer.\\n\\n**Key distinction from FGRPO:** FGRPO uses Qwen3-VL-30B-A3B-Instruct as per-sentence online judge, resulting in ~30-55 judge calls per training sample. Our single-pass CFV reduces this to ~K calls per sample (one per rollout), yielding ~5-8x cost reduction driven by single image encoding per rollout vs. S encodings. More importantly, CFRL adds completeness checking. FGRPO uses Lagrangian dual ascent; we use direct reward weighting with curriculum scheduling.\\n\\n**Key distinction from PaLMR:** PaLMR's V-GRPO uses binary visual fidelity gate (S_vis ∈ {0,1}) providing no gradient for partial improvement. CFRL provides continuous, multi-property reward signals. PaLMR does not require or verify explicit evidence citations.\\n\\n**Key distinction from MJ1:** MJ1 is evaluation-time judge with 5-stage pipeline (up to 6144 tokens). CFRL adapts structured verification to training-time with compact inline citations. CFRL checks completeness, which MJ1 does not.\\n\\n**Key distinction from PEARL:** PEARL checks perception accuracy of externally-generated sub-questions. CFRL checks grounding, validity, and completeness of the model's own explicit evidence citations.\\n\\n**Key distinction from AutoRubric-R1V:** AutoRubric-R1V provides process supervision by mining rubric checkpoints from successful trajectories — it checks whether the model's reasoning path conforms to patterns found in correct solutions. CFRL instead verifies composition properties against the image itself: whether cited evidence is factually grounded, inferences are valid, and coverage is complete. These are complementary: AutoRubric rewards path conformity, CFRL rewards evidence fidelity.\\n\\n**Key distinction from attention-based methods (PGPO, SAYO, Faithful-MR1):** These measure statistical attention patterns. CFRL requires and verifies explicit semantic citation.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"950 (verifier distillation: 100h on 4xH100; Geoparsing/DePlot integration and symbolic checker development: 80h; completeness pipeline development: 70h; main GRPO training: 400h on 8xH100; ablations including verifier accuracy sweep, anti-gaming validation, and baselines: 300h)\",\n      \"timeline\": \"10 weeks (1.5w setup + data + completeness pipeline + symbolic checker, 1.5w verifier training + validation, 3w main experiments with curriculum, 2.5w ablations + verifier accuracy study + anti-gaming analysis, 1.5w analysis and writing — overlapping phases)\",\n      \"estimated_gpu_cost\": \"$1,250 (H100 spot at ~$1.30/GPU-hr on Spheron/RunPod 2026 rates)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"950 (same experimental requirements)\",\n      \"timeline\": \"8 weeks (Claude accelerates verifier data generation, completeness pipeline scaffolding, experiment analysis)\",\n      \"claude_api_cost\": \"$300 (code assistance, composition judgment labeling assistance, completeness annotation, paper drafting)\",\n      \"estimated_gpu_cost\": \"$1,250\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1500 (additional hyperparameter sweeps for α/β/γ/δ/ε, verifier architecture search, verifier accuracy noise ablation, completeness pipeline ablation per domain, anti-gaming validation suite, extended baselines including PEARL+FGRPO+PaLMR+TreeVGR+Vision-SR1 reimplementation, symbolic checker coverage expansion)\",\n      \"timeline\": \"7 weeks (parallelized experiment scheduling, automated verifier validation)\",\n      \"claude_api_cost\": \"$1,000 (teacher labeling for verifier data: $600 for ~50K composition judgments via Qwen3-VL-235B; completeness annotation for chart/diagram domains: $100; experiment orchestration, analysis, and ablation design: $300)\",\n      \"estimated_gpu_cost\": \"$1,950\",\n      \"speed_bottleneck\": \"Verifier data generation requires teacher model (Qwen3-VL-235B) inference at ~50K examples; Geoparsing inference for geometry completeness pipeline; verifier validation requires human-annotated held-out set (5K examples); GRPO rollout reward evaluation is sequential per batch; curriculum phasing requires sequential training stages; anti-gaming counterfactual validation adds ~10% overhead per checkpoint\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (estimated late Sep 2026, ~17 weeks from now — primary target with sufficient buffer for experiments + writing)\",\n    \"AAAI 2027 (abstract: Jul 21, paper: Jul 28, 2026 — stretch goal, 8 weeks with zero buffer; feasible only with aggressive parallelization and if verifier distillation completes in week 2)\",\n    \"CVPR 2027 (estimated ~Nov 2026, not yet announced — fallback if additional ablations needed)\"\n  ],\n  \"level\": \"top-tier\",\n  \"key_references\": [\n    \"Compose and Fuse: Revisiting the Foundational Bottlenecks in Multimodal Reasoning (ICLR 2026)\",\n    \"Perceptual-Evidence Anchored Reinforced Learning for Multimodal Reasoning [PEARL] (CVPR 2026)\",\n    \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment [V-GRPO] (CVPR 2026, arXiv:2603.06652)\",\n    \"MJ1: Multimodal Judgment via Grounded Verification (arXiv:2603.07990, Mar 2026)\",\n    \"Grounding the Score: Explicit Visual Premise Verification for Reliable VLM Process Reward Models [EVPV] (arXiv Mar 2026)\",\n    \"Faithful GRPO: Improving Visual Spatial Reasoning via Constrained Policy Optimization [FGRPO] (arXiv:2604.08476, Apr 2026)\",\n    \"Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention (arXiv May 2026)\",\n    \"TreeVGR: Traceable Evidence Enhanced Visual Grounded Reasoning (ICLR 2026, arXiv:2507.07999)\",\n    \"v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning (arXiv:2505.18842, May 2026)\",\n    \"VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding (arXiv:2509.24776)\",\n    \"SIEVE: Improving Visual Reasoning with Iterative Evidence Refinement (arXiv:2603.14117, Mar 2026)\",\n    \"Vision-SR1: Self-Rewarding Vision-Language Model via Reasoning Decomposition and Multi-Reward Policy Optimization (arXiv:2508.19652)\",\n    \"AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning (arXiv:2510.14738)\",\n    \"CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding (arXiv:2508.00378)\",\n    \"MuRGAt: Multimodal Fact-Level Attribution for Verifiable Reasoning (arXiv:2602.11509, Feb 2026)\",\n    \"Don't Blink: Evidence Collapse during Multimodal Reasoning (arXiv:2604.04207, Apr 2026)\",\n    \"Deeper Thought, Weaker Aim: Understanding and Mitigating Perceptual Impairment during Reasoning in MLLMs (arXiv:2603.14184, Mar 2026)\",\n    \"Not All Tokens See Equally: Perception-Grounded Policy Optimization for Large Vision-Language Models [PGPO] (arXiv Apr 2026)\",\n    \"Credit Where It is Due: Cross-Modality Connectivity Drives Precise RL for MLLM Reasoning [AT-RL] (arXiv Feb 2026)\",\n    \"Don't Lose Sight: Visually-Grounded Credit Assignment for Multimodal Reasoning [VICRA] (2026)\",\n    \"Do MLLMs Really See It: Reinforcing Visual Attention in Multimodal LLMs [SAYO] (arXiv Feb 2026)\",\n    \"Grounded Reinforcement Learning for Visual Reasoning [ViGoRL] (arXiv 2026)\",\n    \"What MLLMs Learn about When they Learn about Multimodal Reasoning [MathLens] (arXiv 2026)\",\n    \"Seeing with You: Perception-Reasoning Coevolution for Multimodal Reasoning [PRCO] (arXiv 2026)\",\n    \"Deconstructing Multimodal Mathematical Reasoning: Towards a Unified Perception-Alignment-Reasoning Paradigm [PAR] (arXiv Mar 2026)\",\n    \"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards (arXiv Apr 2026)\",\n    \"GeoSketch: A Neural-Symbolic Approach to Geometric Multimodal Reasoning (arXiv 2025/2026)\",\n    \"Geoparsing: Unified Formal Language for Geometry Diagram Parsing (arXiv:2604.11600, Apr 2026)\",\n    \"Benchmarking Multimodal RAG through a Chart-based Document Question-Answering Generation Framework [CHARGE] (arXiv:2502.14864, 2025)\",\n    \"DePlot: One-shot Visual Language Reasoning by Plot-to-Table Translation (2023)\",\n    \"VisDoT: Decomposition of Thought with Visual Interpretation Grounding (arXiv:2603.11631, Mar 2026, EACL 2026 Findings)\",\n    \"Countdown-Code: A Testbed for Reward Hacking in RLVR (arXiv:2603.07084, Mar 2026)\",\n    \"PURE: Pessimistic Unbiased Reward Estimation for RL with Noisy Rewards (arXiv:2504.15275, NeurIPS 2025)\",\n    \"Spotlight on Token Perception for Multimodal Reinforcement Learning [VPPO] (ICLR 2026)\",\n    \"Visually-Guided Policy Optimization for Multimodal Reasoning [VGPO] (ACL 2026)\",\n    \"DocR1: Evidence Page-Guided GRPO for Multi-Page Document Understanding (arXiv 2026)\",\n    \"OpenMMReasoner: Pushing the Frontiers for Multimodal Reasoning with an Open and General Recipe (CVPR 2026)\",\n    \"From Sight to Insight: Improving Visual Reasoning Capabilities of Multimodal Models via RL (arXiv 2026)\",\n    \"Perception-R1: Advancing Multimodal Reasoning Capabilities of MLLMs via Visual Perception Reward (arXiv 2025)\",\n    \"Beyond Where to Look: Trajectory-Guided Reinforcement Learning for Multimodal RLVR [TGRL] (arXiv 2026)\",\n    \"Do RAG Systems Cover What Matters? Evaluating and Optimizing Responses with Sub-Question Coverage (arXiv:2410.15531, NAACL 2025)\",\n    \"PGDP-Net: Plane Geometry Diagram Parsing with Graph Neural Networks (IJCAI 2022)\",\n    \"Chart-RVR: Reinforcement Learning with Verifiable Rewards for Explainable Chart Reasoning (arXiv:2510.10973)\"\n  ],\n  \"description\": \"We address the composition gap in multimodal reasoning training: while recent methods tackle perception gating (PEARL, PaLMR), attention-level credit reallocation (PGPO, SAYO, AT-RL, VICRA, KAWHI), grounding+consistency constraints (FGRPO), causal attention anchoring (Faithful-MR1), structured grounded evaluation (MJ1), self-rewarding perception decomposition (Vision-SR1), spatial evidence localization (TreeVGR, ViGoRL), embedding-level evidence re-access (v1, SIEVE), perception-level coverage rewards (VTPerception-R1), rubric-based process supervision (AutoRubric-R1V), post-hoc visual verification (CoRGI), and evidence-loss diagnostics ('Don't Blink', 'Deeper Thought, Weaker Aim'), none unifies evidence grounding, binding validity, and integration completeness verification in a single lightweight training-time verifier. We propose Composition Fidelity RL (CFRL), which requires models to generate explicit evidence citations (&lt;observe>/&lt;reason evidence=''>) and trains a distilled Composition Fidelity Verifier (CFV, 4B parameters) to check three properties: (1) evidence grounding — cited facts match image content, (2) binding validity — inferences are logically consistent with cited evidence, and (3) integration completeness — all task-relevant visual facts are cited. Binding validity is structured in two tiers: Tier 1 (core) provides domain-agnostic arithmetic verification (sum/difference/ratio/comparison consistency between cited values and computed results) and geometry symbolic theorem matching, applicable across all domains without external tools; Tier 2 (extension) adds domain-specific checks for charts (ordering consistency, extrema, trend monotonicity, aggregation) and diagrams (structural relationship, attribute, cardinality verification), requiring parsed data representations. The CFV performs all verification in a single autoregressive forward pass — processing the image once and generating inline grounding/binding verdicts for each observation and reasoning step sequentially — yielding ~5-8x cost reduction over FGRPO's per-sentence judge calls (driven by 1 vs. S ≈ 5-8 image encodings per rollout). The contribution is structured in two tiers: Tier 1 (core: grounding + arithmetic/geometric binding verifier, self-contained with no external tool dependencies) and Tier 2 (extension: completeness pipeline with domain-specific parsing + domain-specific binding checks), ensuring the paper is defensible even if completeness checking or domain-specific binding proves too approximate. Critically, we address MuRGAt's finding that enforcing structured grounding degrades accuracy in zero-shot settings through accuracy-first curriculum scheduling (Phase 0 establishes baseline accuracy before citation requirements), accuracy-dominant reward weighting (α ≥ 0.4), and counterfactual validation monitoring. The CFV is distilled from Qwen3-VL-235B on 50K synthetic composition judgments and validated on 5K held-out human-annotated examples, with noise-tolerance ablation. Unlike Vision-SR1 (self-rewarding checks perceptual self-containment but not factual accuracy or binding validity), we use an external verifier that checks each cited fact against the image. Unlike FGRPO (per-sentence judge), our single-pass verifier reduces cost ~5-8x. Unlike TreeVGR/ViGoRL (spatial localization via IoU), we verify semantic content and reasoning validity. Unlike v1/SIEVE (embedding-level re-access), we require auditable textual citations. Unlike VTPerception-R1 (perception-level coverage), we check binding validity and structured completeness. Unlike AutoRubric-R1V (trajectory-mined rubrics), we verify composition properties against the image. We incorporate anti-gaming safeguards against tag-format Goodhart effects: low format weight (≤0.05), verifiable citation grounding, answer-leak detection, KL regularization, and periodic counterfactual validation. We train Qwen3-VL-8B via GRPO on geometry, chart, and diagram tasks with curriculum scheduling. Key baselines: PEARL-7B (+6.6% over GRPO), FGRPO-7B (1.7% inconsistency, +13 grounding), PaLMR-7B (70.9% HallusionBench), TreeVGR-7B (+16.8 V*Bench), VTPerception-R1-7B (82.5% AI2D), Vision-SR1-7B (58.8 avg, 69.8 HallusionBench), PGPO (+18.7% avg), OpenMMReasoner-7B (+11.6%), AutoRubric-R1V-7B (+8.0 avg), MJ1 (77.0% MMRB2), and Faithful-MR1-7B.\",\n  \"project_name\": \"composition_fidelity_rl\",\n  \"source\": \"web_research\",\n  \"changes_from_previous_revision\": {\n    \"issue_1_vision_sr1\": \"Added Vision-SR1 (arXiv:2508.19652) as a new landscape subsection ('Self-rewarding perception-reasoning decomposition') with detailed technical description: uses &lt;visual_perception>/&lt;think>/&lt;answer> structured tags, self-rewarding via re-prompting the frozen policy model without image access to check perceptual self-containment, GRPO with decoupled reward-advantage framework, three-stage training (SFT cold-start → standard rollout → self-reward rollout), 58.8 avg across 8 benchmarks on Qwen2.5-VL-7B. Differentiated from CFRL on three axes: (a) self-rewarding vs. external distilled verifier — self-rewarding cannot detect hallucinated but internally consistent perceptions, while CFRL's grounding verification checks each cited fact against the actual image; (b) perceptual self-containment checking vs. factual grounding accuracy + binding validity + completeness — Vision-SR1 tests whether perception suffices to re-derive the answer, not whether each fact is correct; (c) monolithic perception block vs. fine-grained per-fact &lt;observe> citations enabling per-fact verification and explicit evidence-to-inference linking. Added dedicated 'Key distinction from Vision-SR1' section in approach.\",\n    \"issue_2_binding_validity_specification\": \"Substantially expanded binding validity with concrete, algorithmic specifications for all domains, organized in two tiers. Tier 1 (core, domain-agnostic): (a) Arithmetic verification — symbolic execution of sum/difference/product/quotient consistency, ratio/percentage verification, comparison consistency, and multi-step arithmetic chaining; applies to ALL domains (geometry, charts, diagrams) without external tools. (b) Geometry symbolic theorem matching (existing). Tier 2 (extension, domain-specific): (a) Chart-specific: ordering consistency against extracted data table, extrema verification (X = max(values)), trend verification with formal monotonicity definition (including tolerance ε for noise), aggregation verification (mean within 1% relative tolerance). (b) Diagram-specific: structural relationship verification against parsed graph (edge existence), attribute consistency (label matching), cardinality verification (degree check), containment/hierarchy verification. Added explicit fallback for qualitative reasoning: binding check returns neutral score (0.5) for steps that cannot be reduced to arithmetic or structural constraint checking, flagged as 'unverifiable-binding' for monitoring. Revised Tier 1/Tier 2 scoping: Tier 1 now includes domain-agnostic arithmetic + geometry symbolic (no external tools needed), Tier 2 adds completeness + domain-specific binding (requiring parsed data representations). This makes Tier 1 stronger — it provides cross-domain binding signal via arithmetic verification even without chart/diagram-specific infrastructure.\",\n    \"issue_3_verifier_cost_model\": \"Clarified CFV architecture and cost model. The CFV performs all three property checks in a single autoregressive forward pass: given image + tagged response + verification instruction as input, it generates verification judgments for all observations and reasoning steps sequentially as autoregressive output. Grounding VQA for each &lt;observe> tag is performed as internal sub-reasoning within the autoregressive generation (inline grounding verdicts), NOT as separate VQA calls. This is architecturally identical to MJ1's single-pass multi-stage verification chain. Revised cost comparison: effective cost reduction is ~5-8x per rollout (revised from ~10-20x), driven by 1 image encoding vs. S ≈ 5-8 encodings. Per-call text generation cost is roughly comparable between CFRL (500-1500 verification tokens at 4B dense) and FGRPO (S × ~150 tokens at 3.3B active MoE). The primary savings come from the single image encoding — processing visual tokens through transformer layers is the dominant cost in VLM inference.\",\n    \"issue_4_autorubric_corgi\": \"Added AutoRubric-R1V (arXiv:2510.14738) and CoRGI (arXiv:2508.00378) to the landscape under 'Structured verification and evaluation judges'. AutoRubric-R1V: auto-generates rubric-based process rewards via self-aggregation from successful trajectories, rubric reward = fraction of satisfied checkpoints, +8.0 avg on 6 benchmarks. Differentiated: derives supervision from trajectory-level consistency patterns rather than verifying composition properties against the image. CoRGI: post-hoc step-wise verification via Grounding DINO, decomposing rationales and grounding each step in visual evidence. Differentiated: inference-time only, does not serve as training-time reward. Added 'Key distinction from AutoRubric-R1V' section. Both added to key_references. Also added Chart-RVR (arXiv:2510.10973) to key_references as it informed the chart-domain binding validity specification.\"\n  }\n}\n\n\n## Previous review history\n### Round 1 review\nVerdict: revise\nIssues: [\"CRITICAL: 6+ directly competing papers missing from landscape: PEARL (CVPR 2026, perception-evidence anchored RL with fidelity gate), EVPV/Grounding the Score (March 2026, step-wise visual premise verification), CAVE (May 2026, structured credit assignment for visual evidence reasoning via GRPO), KAWHI (March 2026, visual evidence-reasoning alignment via credit reallocation), SAYO (Feb 2026, region-level visual attention reward), DocSeeker (April 2026, evidence-aware GRPO)\", \"CRITICAL: The gap claim 'none rewards the quality of their composition' is factually incorrect — PEARL gates reasoning on verified visual evidence, EVPV verifies visual premises per step, and CAVE rewards evidence acquisition quality at the action level. The gap needs fundamental repositioning.\", \"HIGH: No verifier validation methodology described. How accurate must the CFR verifier be to provide a useful reward signal? What happens when it makes errors? No ablation for verifier accuracy vs. downstream model quality is planned.\", \"MEDIUM: The 'binding validity' check — verifying whether logical inference follows from cited evidence — is a hard open problem (essentially requiring compositional logical reasoning). Distilling this from Qwen3-VL-235B into a lightweight model introduces significant noise risk.\", \"MEDIUM: User requirement asks for 'Integrating Visual, Symbolic, and Textual Understanding' but the proposal focuses almost entirely on visual-textual integration. Symbolic reasoning (mathematical symbol manipulation, geometric theorem application) is not explicitly addressed as a distinct modality.\", \"LOW: H100 spot at $3/hr is above current 2026 market rates ($1-2/hr for spot). Cost estimates are internally consistent but potentially inflated by ~50%.\", \"LOW: 7-week timeline for AAAI 2027 (abstract Jul 21) leaves only ~8 weeks from today — very tight given verifier training + main experiments + ablations + writing.\"]\nFeedback: 1. **Urgently expand landscape**: Add PEARL, EVPV, CAVE, KAWHI, SAYO, DocSeeker, ViGoRL to the landscape analysis. Position CFRL against these specifically — what does the three-part composition verifier offer that PEARL's perception checklist + fidelity gate doesn't? How does CFRL's explicit citation format differ from CAVE's structured credit assignment? 2. **Reframe the gap**: Don't claim 'none rewards composition.' Instead, argue: (a) PEARL checks perception accuracy but not binding validity; (b) EVPV checks visual premise reliability but doesn't reward completeness of evidence integration; (c) CAVE rewards evidence acquisition but lacks explicit grounding verification. CFRL uniquely combines all three in a single verifier. 3. **Add verifier validation plan**: Include an ablation studying verifier accuracy vs. downstream quality. Test verifier on a held-out composition judgment set. Report precision/recall of the verifier on the three sub-tasks. 4. **Address the binding validity feasibility risk**: Consider whether the 'binding validity' component can be simplified (e.g., to logical consistency checking rather than full inferential verification). Or propose a fallback if the verifier proves too noisy. 5. **Incorporate symbolic reasoning**: Address geometry theorem verification, symbol parsing, and structural diagram understanding more explicitly to match the user's requirement for symbolic understanding.\n\n### Round 2 review\nVerdict: revise\nIssues: [\"MEDIUM: The '100x cost reduction over FGRPO' claim is factually unsupported. FGRPO uses Qwen3-VL-30B-A3B (3B active params per token via MoE) as its online judge, NOT GPT-level models. Per verified benchmarks, inference cost of 30B-A3B is only 1.6-1.8x that of Qwen3-VL-4B. Even accounting for FGRPO's per-sentence evaluation (multiplying by ~10-20 sentences), the realistic cost reduction is ~10-30x, not 100x. The proposal repeatedly says 'GPT-level judges' but this mischaracterizes FGRPO's actual implementation.\", \"MEDIUM: MJ1 (Mar 2026, arXiv:2603.07990) is a critical omission from the landscape. MJ1 trains a 3B multimodal judge using RL with a structured grounded verification chain (observations → claims → verification → evaluation → scoring) — conceptually very similar to CFRL's &lt;observe>/&lt;reason evidence=''> format. MJ1 achieves 77.0% on MMRB2 surpassing much larger models. While MJ1 is an evaluation judge rather than a training-time reward verifier, the structured verification chain approach overlaps significantly.\", \"MEDIUM: The 'integration completeness' coverage estimator is critically underspecified. The proposal says it 'identifies required visual elements from the question+image and verifies citation coverage' but does not explain HOW it identifies what's task-relevant. This is essentially an oracle problem — you need to know the answer to know which facts matter. For geometry, this might be solvable via the symbolic checker, but for charts/diagrams, it's an open problem. Without a concrete mechanism, the most novel contribution remains hand-wavy.\", \"MEDIUM: PaLMR (Feb 2026, arXiv:2603.06652) is missing from the landscape. PaLMR introduces perception-aligned data + process-aligned optimization with V-GRPO (Vision-Guided GRPO), incorporating visual-consistency rewards throughout the reasoning process. It directly addresses faithful visual reasoning and should be differentiated from CFRL.\", \"LOW: AAAI 2027 (abstract Jul 21) as primary target requires completing the entire 8-week pipeline — verifier distillation, symbolic checker, main GRPO training, ablations, AND paper writing — in exactly 8 weeks starting today (May 27). This leaves zero buffer. ICLR 2027 (Sep 24) is more realistic and should be explicitly stated as primary target.\", \"LOW: Risk of tag gaming during RL training is not discussed. The model may learn to produce well-formatted &lt;observe>/&lt;reason evidence=''> tags that satisfy the verifier superficially without improving actual reasoning quality (Goodhart's Law). How will this be detected and mitigated?\"]\nFeedback: The revision substantially improved upon Round 1 — landscape is now comprehensive, gap is better articulated, and the verifier validation protocol addresses the prior review's main concern. Four specific fixes needed:\n\n1. **Correct the FGRPO cost comparison**: FGRPO uses Qwen3-VL-30B-A3B (3B active params, MoE) as its online judge, not 'GPT-level' models (GPT-5.4 is only used for evaluation). Recalculate the realistic cost savings as ~10-30x based on actual per-sentence evaluation overhead, not 100x. The efficiency argument still holds but needs honest quantification.\n\n2. **Add MJ1 and PaLMR to landscape**: MJ1's structured verification chain is the closest existing approach to CFRL's explicit citation format — argue that MJ1 is a judge (evaluation-time) while CFRL is a training-time reward verifier, and that MJ1 doesn't check completeness. PaLMR's V-GRPO is a relevant process-aligned baseline that should be compared.\n\n3. **Specify the completeness coverage estimator**: Propose a concrete mechanism — e.g., for geometry: enumerate all entities/relationships from the parsed diagram + question keywords; for charts: extract all data points referenced in the question. Acknowledge that completeness checking is approximate and define a precision/recall target (e.g., 80% recall of task-relevant facts). Consider using the symbolic checker for geometry and a separate question-decomposition module for charts.\n\n4. **Reorder venue targets**: Make ICLR 2027 (Sep 24) the primary target and AAAI 2027 a stretch goal. This gives 17 weeks — enough for proper experiments with buffer.\n\n### Round 3 review\nVerdict: revise\nIssues: [\"MEDIUM: Several relevant concurrent works missing from landscape. TreeVGR (ICLR 2026) trains models to produce explicit bounding box evidence via RL and achieves +16.8 on V*Bench — it directly addresses grounded evidence in RL training. v1 (May 2026, arXiv:2505.18842) constructs 300K reasoning traces with interleaved visual grounding annotations and uses point-and-copy to re-access visual evidence during reasoning — conceptually close to CFRL's evidence citation paradigm. VTPerception-R1 (arXiv:2509.24776) implements perception-aware RL with explicit visual and textual grounding rewards. SIEVE (arXiv:2603.14117) trains models to re-access visual evidence within RL policy optimization. These need differentiation to establish CFRL's unique positioning.\", \"MEDIUM: MuRGAt (Feb 2026, arXiv:2602.11509) directly addresses multimodal fact-level attribution with explicit evidence citations specifying modality and temporal segments — conceptually very similar to CFRL's &lt;observe>/&lt;reason evidence=''> format for requiring explicit citations. While MuRGAt is an evaluation benchmark (not a training method), it found that 'increasing reasoning depth or enforcing structured grounding often degrades accuracy' — this is a direct empirical warning against CFRL's approach of forcing structured citation during training.\", \"MEDIUM: System complexity risk is insufficiently acknowledged. The approach requires integrating 5+ external tools/models (Geoparsing, DePlot/CHARGE, VisDoT, PGDP-Net, symbolic theorem library), training a distilled verifier (50K examples from 235B teacher), running curriculum GRPO training with 5 reward components plus anti-gaming safeguards, and validating across 3 domain-specific pipelines. Each integration is a potential failure point. No fallback plan if the completeness pipeline (the most novel component) underperforms.\", \"LOW: CHARGE reference title is inaccurate. The proposal cites it as 'Chart-Grounded Hallucination Evaluation with Keypoint Coverage' but arXiv:2502.14864 is actually 'Benchmarking Multimodal RAG through a Chart-based Document Question-Answering Generation Framework.' The keypoint coverage concept exists in the paper but the framing is different.\", \"LOW: The 'Don't Blink: Evidence Collapse during Multimodal Reasoning' (Apr 2026) paper documents the exact phenomenon CFRL aims to address — that reasoning VLMs progressively lose visual grounding as reasoning unfolds. This should be cited as direct motivating evidence for the approach.\", \"LOW: The ~82% human agreement claim for sub-question decomposition cites arXiv:2410.15531, which is about RAG system coverage (finding that systems miss ~50% of core sub-questions) — the 82% figure needs verification or a different citation.\"]\nFeedback: The proposal has improved substantially across three rounds — FGRPO cost comparison is now honest, MJ1 and PaLMR are well-differentiated, the completeness pipeline is concrete, and anti-gaming safeguards are thorough. Three actionable refinements for a potential pass:\n\n1. **Add missing concurrent work**: Briefly differentiate from TreeVGR (bounding-box evidence vs. semantic citation), v1 (embedding re-insertion vs. explicit textual citation), VTPerception-R1 (perception-level rewards vs. composition-level verification), and SIEVE (iterative re-grounding vs. single-pass verification). These are 1-2 sentences each. Critically, address MuRGAt's finding that enforcing structured grounding can degrade accuracy — this is a direct challenge to CFRL's premise.\n\n2. **Acknowledge and mitigate system complexity**: Add a short 'risks and mitigations' paragraph. What is the minimum viable version of CFRL if the completeness pipeline underperforms? Consider proposing a staged contribution: (a) grounding + binding verifier alone as the core contribution, (b) completeness as an extension. This makes the paper defensible even if integration completeness checking proves too approximate.\n\n3. **Fix minor reference issues**: Correct the CHARGE title, add 'Don't Blink' as motivating evidence, and verify the 82% agreement claim for sub-question decomposition.\n\n### Round 4 review\nVerdict: revise\nIssues: [\"MEDIUM: Vision-SR1 (arXiv:2508.19652) is a conceptually adjacent but undiscussed concurrent work. It also (1) decomposes reasoning into explicit perception + reasoning stages using structured tags (&lt;See>/&lt;Think>), (2) uses perception quality as a training reward signal, and (3) trains via GRPO. While Vision-SR1 uses self-rewarding (same model judges itself) rather than an external verifier, and does not check binding validity or completeness, it shares the core insight of explicit perceptual articulation as a trainable skill. This is the closest missed work to CFRL's paradigm of requiring explicit evidence statements that are then verified.\", \"MEDIUM: The binding validity check for non-geometry domains remains insufficiently specified. For geometry, the symbolic theorem matching is concrete and verifiable. But for charts ('cited values must support the computed trend') and diagrams, the proposal lacks a precise algorithm. What specific constraint satisfaction checks are performed? How are 'trends' formally defined? What happens when the binding check is inapplicable (e.g., qualitative reasoning about diagram structure)? This is the core novel contribution of CFRL — it needs to be watertight or honestly scoped to geometry-only for Tier 1.\", \"LOW-MEDIUM: The '~5 calls per sample (one per rollout)' claim for CFRL's verifier cost needs clarification. The CFV must perform grounding VQA (converting each &lt;observe> tag into a yes/no visual question and answering it), binding constraint satisfaction, AND completeness coverage scoring — all in a 'single pass' through a 4B model. Is this truly one forward pass, or does the VQA sub-module require multiple passes per observation? If there are N observations, doesn't grounding require N VQA evaluations? The 10-20x cost reduction over FGRPO likely holds regardless, but the claim should be precise.\", \"LOW: AutoRubric-R1V (arXiv:2510.14738) and CoRGI (arXiv:2508.00378) are mildly relevant adjacent works. AutoRubric-R1V auto-generates rubric-based process rewards from successful trajectories — a different approach to process-level verification that doesn't require external tools. CoRGI performs post-hoc step-wise verification with visual grounding — inference-time only, but conceptually related to CFRL's verification chain. Brief acknowledgment would strengthen completeness.\"]\nFeedback: The proposal has improved substantially across four rounds and is approaching the quality threshold. Three specific changes would likely push it to pass:\n\n1. **Add Vision-SR1 differentiation** (1-2 sentences in landscape): Vision-SR1 shares the insight of structured perception-reasoning decomposition with explicit tags and perception-quality rewards. Differentiate: (a) Vision-SR1 uses self-rewarding (same model serves as judge) while CFRL uses an external distilled verifier, (b) Vision-SR1 checks perceptual self-containment (can you answer from perception alone?) while CFRL checks factual grounding accuracy (is the perception correct?), binding validity (does the inference follow?), and completeness (are all facts covered), (c) Vision-SR1 does not verify the logical consistency between perceived evidence and drawn inferences.\n\n2. **Specify binding validity for non-geometry domains**: For charts, define the concrete constraint checks — e.g., (a) numerical arithmetic verification (sum/difference/ratio consistency between cited values and computed results), (b) ordering consistency (if Bar A > Bar B is cited, verify this matches the chart), (c) unit consistency. For diagrams, define (a) structural relationship verification (if 'A connects to B' is cited, verify the edge exists), (b) attribute consistency. If these checks are too domain-specific to generalize, honestly scope Tier 1 binding validity to geometry + basic arithmetic and acknowledge chart/diagram binding as Tier 2.\n\n3. **Clarify verifier cost model**: Explain whether the CFV performs grounding VQA as internal sub-reasoning within a single forward pass (generating all verification judgments autoregressively) or as separate VQA calls per observation. If the former, the single-pass claim holds; if the latter, the cost is N_obs × 4B rather than 1 × 4B per rollout, and the 10-20x figure needs adjustment.\n\n\n## Output format\nOutput ONLY a JSON object:\n{\n  \"verdict\": \"pass | revise | fail\",\n  \"scores\": {\n    \"novelty\": {\"score\": 0-5, \"rationale\": \"1-2 sentence justification\"},\n    \"feasibility\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"clarity\": {\"score\": 0-5, \"rationale\": \"...\"},\n    \"impact\": {\"score\": 0-5, \"rationale\": \"...\"}\n  },\n  \"issues\": [\"specific issue 1\", ...],\n  \"feedback\": \"Actionable feedback (if verdict=revise)\",\n  \"reason\": \"One-line summary of verdict rationale\"\n}\n\nRules:\n- \"pass\": sound AND high quality — avg score >= 4.0, no critical issues\n- \"revise\": fixable issues OR scores below threshold\n- \"fail\": fundamental flaw (gap doesn't exist, approach provably wrong)\n- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.\n- Round 10 only: if still \"revise\", you MUST choose \"pass\" or \"fail\"."
}
```

---

### Runtime record

_source line 2 · 2026-05-27T23:06:43.022Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T23:06:43.022Z",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

## Round 1

33 recorded events

### User

_source line 3 · 2026-05-27T23:06:43.036Z_

You are a strict ML research reviewer conducting adversarial review.

**Today's date: 2026-05-27 (UTC).**

Your job: independently verify this idea's claims via web_search, then issue a verdict.

## User requirements
The user asked for: **Multi-Modal Mathematical Reasoning — Integrating Visual, Symbolic, and Textual Understanding**
Evaluate whether this idea actually meets the user's requirements. An idea that doesn't match should be "revise" or "fail".

## 核心要求：非常仔细地调研，非常仔细地思考

你是一个严格的审稿人。不要轻信 Generator 的任何 claim——你必须独立验证。

### 调研要求

1. **独立 SOTA 验证**：自己搜索当前 SOTA，不要只检查 Generator 的引用。
   每个验证维度建议用 2-3 种不同的搜索查询。

2. **可行性深度检查**：
   - 搜索类似实验的实际成本/周期
   - 检查 claimed baselines 是否可复现
   - 验证所需的 datasets/models 是否真的可以获取

3. **新颖性压力测试**：专门搜索 Generator 可能遗漏的工作：
   - 尝试不同的关键词组合
   - 同时检查 arXiv 和 conference proceedings
   - 寻找相邻领域的并行/concurrent 工作

4. **深入阅读**：用 WebFetch 实际阅读相关论文的 abstract 和关键章节。

### 思考要求

5. **独立判断**：
   - 不要因为 Generator 说得有道理就轻易 pass
   - 思考这个 idea 在实际执行中会遇到什么困难
   - 考虑这个 idea 对领域的真实贡献

6. **评分诚实**：
   - 4 分意味着"确实很好"，5 分意味着"令人兴奋"
   - Agent 评分经常虚高，你的职责就是纠正这种偏差


## 论文搜索策略

你的搜索质量直接决定了 idea 的质量。不要敷衍搜索——每一次搜索都要有明确的目的。

### 搜索源（推荐每个维度使用 2 个不同来源）

1. **arXiv 预印本**（最新工作）:
   - `site:arxiv.org {topic} 2026` — 按主题搜索最新论文
   - `site:arxiv.org {method_name}` — 按具体方法名搜索
   - `arxiv {topic} {month} 2026` — 精确到月份，找最近 3 个月的工作

2. **Google Scholar**（引用关系 + 综合覆盖）:
   - `{topic} 2026 site:scholar.google.com`
   - `"{exact paper title}"` — 验证论文是否真实存在
   - `"{author name}" {topic} 2026` — 按活跃作者追踪

3. **Papers With Code**（SOTA 排行 + 代码可用性）:
   - `site:paperswithcode.com {task_name}` — 查看任务的 SOTA 排行榜
   - `paperswithcode {dataset} benchmark` — 查看特定 dataset 上的竞争格局

4. **OpenReview**（会议审稿 + 同行评价）:
   - `site:openreview.net {topic} 2026` — 搜索会议提交的论文
   - 用 WebFetch 阅读 OpenReview 上的 reviewer comments — 了解领域专家的真实评价

5. **Semantic Scholar**（语义搜索 + 引用图谱）:
   - `semantic scholar {topic} survey 2026` — 找综述论文

6. **GitHub**（实现验证）:
   - `site:github.com {method_name} {task}` — 验证开源实现是否存在

### 搜索维度

1. **正向搜索**：直接搜索主题相关论文
2. **竞争论文搜索**（最关键！）：有没有人在解决同样的问题？用类似方法？
3. **相邻领域搜索**：其他领域是否已解决类似问题
4. **反面搜索**：找到反对你 idea 的证据
5. **引用链追踪**：找到核心论文后，查看 cited-by 发现 concurrent work


## 竞争论文专项搜索（Reviewer 独有）

1. **关键词变体搜索**：用至少 3 种不同的关键词组合搜索同一个问题
2. **知名团队追踪**：搜索相关团队最近的论文
3. **会议最新录用**：搜索 `site:openreview.net {topic} 2026`
4. **arXiv 近 3 个月密集搜索**

## Review checklist
1. **SOTA freshness**: Are baselines actually current SOTA?
2. **Reference verification**: Do cited papers actually exist?
3. **Gap validity**: Does the claimed gap still exist?
4. **Venue validity**: Are target venue deadlines after 2026-05-27?
5. **Feasibility**: Is the resource estimate realistic?
6. **Novelty**: Is this sufficiently different from existing work?
7. **Cost realism**: Are the three mode estimates internally consistent?

## Idea under review (round 5/10)
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


## Previous review history
### Round 1 review
Verdict: revise
Issues: ["CRITICAL: 6+ directly competing papers missing from landscape: PEARL (CVPR 2026, perception-evidence anchored RL with fidelity gate), EVPV/Grounding the Score (March 2026, step-wise visual premise verification), CAVE (May 2026, structured credit assignment for visual evidence reasoning via GRPO), KAWHI (March 2026, visual evidence-reasoning alignment via credit reallocation), SAYO (Feb 2026, region-level visual attention reward), DocSeeker (April 2026, evidence-aware GRPO)", "CRITICAL: The gap claim 'none rewards the quality of their composition' is factually incorrect — PEARL gates reasoning on verified visual evidence, EVPV verifies visual premises per step, and CAVE rewards evidence acquisition quality at the action level. The gap needs fundamental repositioning.", "HIGH: No verifier validation methodology described. How accurate must the CFR verifier be to provide a useful reward signal? What happens when it makes errors? No ablation for verifier accuracy vs. downstream model quality is planned.", "MEDIUM: The 'binding validity' check — verifying whether logical inference follows from cited evidence — is a hard open problem (essentially requiring compositional logical reasoning). Distilling this from Qwen3-VL-235B into a lightweight model introduces significant noise risk.", "MEDIUM: User requirement asks for 'Integrating Visual, Symbolic, and Textual Understanding' but the proposal focuses almost entirely on visual-textual integration. Symbolic reasoning (mathematical symbol manipulation, geometric theorem application) is not explicitly addressed as a distinct modality.", "LOW: H100 spot at $3/hr is above current 2026 market rates ($1-2/hr for spot). Cost estimates are internally consistent but potentially inflated by ~50%.", "LOW: 7-week timeline for AAAI 2027 (abstract Jul 21) leaves only ~8 weeks from today — very tight given verifier training + main experiments + ablations + writing."]
Feedback: 1. **Urgently expand landscape**: Add PEARL, EVPV, CAVE, KAWHI, SAYO, DocSeeker, ViGoRL to the landscape analysis. Position CFRL against these specifically — what does the three-part composition verifier offer that PEARL's perception checklist + fidelity gate doesn't? How does CFRL's explicit citation format differ from CAVE's structured credit assignment? 2. **Reframe the gap**: Don't claim 'none rewards composition.' Instead, argue: (a) PEARL checks perception accuracy but not binding validity; (b) EVPV checks visual premise reliability but doesn't reward completeness of evidence integration; (c) CAVE rewards evidence acquisition but lacks explicit grounding verification. CFRL uniquely combines all three in a single verifier. 3. **Add verifier validation plan**: Include an ablation studying verifier accuracy vs. downstream quality. Test verifier on a held-out composition judgment set. Report precision/recall of the verifier on the three sub-tasks. 4. **Address the binding validity feasibility risk**: Consider whether the 'binding validity' component can be simplified (e.g., to logical consistency checking rather than full inferential verification). Or propose a fallback if the verifier proves too noisy. 5. **Incorporate symbolic reasoning**: Address geometry theorem verification, symbol parsing, and structural diagram understanding more explicitly to match the user's requirement for symbolic understanding.

### Round 2 review
Verdict: revise
Issues: ["MEDIUM: The '100x cost reduction over FGRPO' claim is factually unsupported. FGRPO uses Qwen3-VL-30B-A3B (3B active params per token via MoE) as its online judge, NOT GPT-level models. Per verified benchmarks, inference cost of 30B-A3B is only 1.6-1.8x that of Qwen3-VL-4B. Even accounting for FGRPO's per-sentence evaluation (multiplying by ~10-20 sentences), the realistic cost reduction is ~10-30x, not 100x. The proposal repeatedly says 'GPT-level judges' but this mischaracterizes FGRPO's actual implementation.", "MEDIUM: MJ1 (Mar 2026, arXiv:2603.07990) is a critical omission from the landscape. MJ1 trains a 3B multimodal judge using RL with a structured grounded verification chain (observations → claims → verification → evaluation → scoring) — conceptually very similar to CFRL's &lt;observe>/&lt;reason evidence=''> format. MJ1 achieves 77.0% on MMRB2 surpassing much larger models. While MJ1 is an evaluation judge rather than a training-time reward verifier, the structured verification chain approach overlaps significantly.", "MEDIUM: The 'integration completeness' coverage estimator is critically underspecified. The proposal says it 'identifies required visual elements from the question+image and verifies citation coverage' but does not explain HOW it identifies what's task-relevant. This is essentially an oracle problem — you need to know the answer to know which facts matter. For geometry, this might be solvable via the symbolic checker, but for charts/diagrams, it's an open problem. Without a concrete mechanism, the most novel contribution remains hand-wavy.", "MEDIUM: PaLMR (Feb 2026, arXiv:2603.06652) is missing from the landscape. PaLMR introduces perception-aligned data + process-aligned optimization with V-GRPO (Vision-Guided GRPO), incorporating visual-consistency rewards throughout the reasoning process. It directly addresses faithful visual reasoning and should be differentiated from CFRL.", "LOW: AAAI 2027 (abstract Jul 21) as primary target requires completing the entire 8-week pipeline — verifier distillation, symbolic checker, main GRPO training, ablations, AND paper writing — in exactly 8 weeks starting today (May 27). This leaves zero buffer. ICLR 2027 (Sep 24) is more realistic and should be explicitly stated as primary target.", "LOW: Risk of tag gaming during RL training is not discussed. The model may learn to produce well-formatted &lt;observe>/&lt;reason evidence=''> tags that satisfy the verifier superficially without improving actual reasoning quality (Goodhart's Law). How will this be detected and mitigated?"]
Feedback: The revision substantially improved upon Round 1 — landscape is now comprehensive, gap is better articulated, and the verifier validation protocol addresses the prior review's main concern. Four specific fixes needed:

1. **Correct the FGRPO cost comparison**: FGRPO uses Qwen3-VL-30B-A3B (3B active params, MoE) as its online judge, not 'GPT-level' models (GPT-5.4 is only used for evaluation). Recalculate the realistic cost savings as ~10-30x based on actual per-sentence evaluation overhead, not 100x. The efficiency argument still holds but needs honest quantification.

2. **Add MJ1 and PaLMR to landscape**: MJ1's structured verification chain is the closest existing approach to CFRL's explicit citation format — argue that MJ1 is a judge (evaluation-time) while CFRL is a training-time reward verifier, and that MJ1 doesn't check completeness. PaLMR's V-GRPO is a relevant process-aligned baseline that should be compared.

3. **Specify the completeness coverage estimator**: Propose a concrete mechanism — e.g., for geometry: enumerate all entities/relationships from the parsed diagram + question keywords; for charts: extract all data points referenced in the question. Acknowledge that completeness checking is approximate and define a precision/recall target (e.g., 80% recall of task-relevant facts). Consider using the symbolic checker for geometry and a separate question-decomposition module for charts.

4. **Reorder venue targets**: Make ICLR 2027 (Sep 24) the primary target and AAAI 2027 a stretch goal. This gives 17 weeks — enough for proper experiments with buffer.

### Round 3 review
Verdict: revise
Issues: ["MEDIUM: Several relevant concurrent works missing from landscape. TreeVGR (ICLR 2026) trains models to produce explicit bounding box evidence via RL and achieves +16.8 on V*Bench — it directly addresses grounded evidence in RL training. v1 (May 2026, arXiv:2505.18842) constructs 300K reasoning traces with interleaved visual grounding annotations and uses point-and-copy to re-access visual evidence during reasoning — conceptually close to CFRL's evidence citation paradigm. VTPerception-R1 (arXiv:2509.24776) implements perception-aware RL with explicit visual and textual grounding rewards. SIEVE (arXiv:2603.14117) trains models to re-access visual evidence within RL policy optimization. These need differentiation to establish CFRL's unique positioning.", "MEDIUM: MuRGAt (Feb 2026, arXiv:2602.11509) directly addresses multimodal fact-level attribution with explicit evidence citations specifying modality and temporal segments — conceptually very similar to CFRL's &lt;observe>/&lt;reason evidence=''> format for requiring explicit citations. While MuRGAt is an evaluation benchmark (not a training method), it found that 'increasing reasoning depth or enforcing structured grounding often degrades accuracy' — this is a direct empirical warning against CFRL's approach of forcing structured citation during training.", "MEDIUM: System complexity risk is insufficiently acknowledged. The approach requires integrating 5+ external tools/models (Geoparsing, DePlot/CHARGE, VisDoT, PGDP-Net, symbolic theorem library), training a distilled verifier (50K examples from 235B teacher), running curriculum GRPO training with 5 reward components plus anti-gaming safeguards, and validating across 3 domain-specific pipelines. Each integration is a potential failure point. No fallback plan if the completeness pipeline (the most novel component) underperforms.", "LOW: CHARGE reference title is inaccurate. The proposal cites it as 'Chart-Grounded Hallucination Evaluation with Keypoint Coverage' but arXiv:2502.14864 is actually 'Benchmarking Multimodal RAG through a Chart-based Document Question-Answering Generation Framework.' The keypoint coverage concept exists in the paper but the framing is different.", "LOW: The 'Don't Blink: Evidence Collapse during Multimodal Reasoning' (Apr 2026) paper documents the exact phenomenon CFRL aims to address — that reasoning VLMs progressively lose visual grounding as reasoning unfolds. This should be cited as direct motivating evidence for the approach.", "LOW: The ~82% human agreement claim for sub-question decomposition cites arXiv:2410.15531, which is about RAG system coverage (finding that systems miss ~50% of core sub-questions) — the 82% figure needs verification or a different citation."]
Feedback: The proposal has improved substantially across three rounds — FGRPO cost comparison is now honest, MJ1 and PaLMR are well-differentiated, the completeness pipeline is concrete, and anti-gaming safeguards are thorough. Three actionable refinements for a potential pass:

1. **Add missing concurrent work**: Briefly differentiate from TreeVGR (bounding-box evidence vs. semantic citation), v1 (embedding re-insertion vs. explicit textual citation), VTPerception-R1 (perception-level rewards vs. composition-level verification), and SIEVE (iterative re-grounding vs. single-pass verification). These are 1-2 sentences each. Critically, address MuRGAt's finding that enforcing structured grounding can degrade accuracy — this is a direct challenge to CFRL's premise.

2. **Acknowledge and mitigate system complexity**: Add a short 'risks and mitigations' paragraph. What is the minimum viable version of CFRL if the completeness pipeline underperforms? Consider proposing a staged contribution: (a) grounding + binding verifier alone as the core contribution, (b) completeness as an extension. This makes the paper defensible even if integration completeness checking proves too approximate.

3. **Fix minor reference issues**: Correct the CHARGE title, add 'Don't Blink' as motivating evidence, and verify the 82% agreement claim for sub-question decomposition.

### Round 4 review
Verdict: revise
Issues: ["MEDIUM: Vision-SR1 (arXiv:2508.19652) is a conceptually adjacent but undiscussed concurrent work. It also (1) decomposes reasoning into explicit perception + reasoning stages using structured tags (&lt;See>/&lt;Think>), (2) uses perception quality as a training reward signal, and (3) trains via GRPO. While Vision-SR1 uses self-rewarding (same model judges itself) rather than an external verifier, and does not check binding validity or completeness, it shares the core insight of explicit perceptual articulation as a trainable skill. This is the closest missed work to CFRL's paradigm of requiring explicit evidence statements that are then verified.", "MEDIUM: The binding validity check for non-geometry domains remains insufficiently specified. For geometry, the symbolic theorem matching is concrete and verifiable. But for charts ('cited values must support the computed trend') and diagrams, the proposal lacks a precise algorithm. What specific constraint satisfaction checks are performed? How are 'trends' formally defined? What happens when the binding check is inapplicable (e.g., qualitative reasoning about diagram structure)? This is the core novel contribution of CFRL — it needs to be watertight or honestly scoped to geometry-only for Tier 1.", "LOW-MEDIUM: The '~5 calls per sample (one per rollout)' claim for CFRL's verifier cost needs clarification. The CFV must perform grounding VQA (converting each &lt;observe> tag into a yes/no visual question and answering it), binding constraint satisfaction, AND completeness coverage scoring — all in a 'single pass' through a 4B model. Is this truly one forward pass, or does the VQA sub-module require multiple passes per observation? If there are N observations, doesn't grounding require N VQA evaluations? The 10-20x cost reduction over FGRPO likely holds regardless, but the claim should be precise.", "LOW: AutoRubric-R1V (arXiv:2510.14738) and CoRGI (arXiv:2508.00378) are mildly relevant adjacent works. AutoRubric-R1V auto-generates rubric-based process rewards from successful trajectories — a different approach to process-level verification that doesn't require external tools. CoRGI performs post-hoc step-wise verification with visual grounding — inference-time only, but conceptually related to CFRL's verification chain. Brief acknowledgment would strengthen completeness."]
Feedback: The proposal has improved substantially across four rounds and is approaching the quality threshold. Three specific changes would likely push it to pass:

1. **Add Vision-SR1 differentiation** (1-2 sentences in landscape): Vision-SR1 shares the insight of structured perception-reasoning decomposition with explicit tags and perception-quality rewards. Differentiate: (a) Vision-SR1 uses self-rewarding (same model serves as judge) while CFRL uses an external distilled verifier, (b) Vision-SR1 checks perceptual self-containment (can you answer from perception alone?) while CFRL checks factual grounding accuracy (is the perception correct?), binding validity (does the inference follow?), and completeness (are all facts covered), (c) Vision-SR1 does not verify the logical consistency between perceived evidence and drawn inferences.

2. **Specify binding validity for non-geometry domains**: For charts, define the concrete constraint checks — e.g., (a) numerical arithmetic verification (sum/difference/ratio consistency between cited values and computed results), (b) ordering consistency (if Bar A > Bar B is cited, verify this matches the chart), (c) unit consistency. For diagrams, define (a) structural relationship verification (if 'A connects to B' is cited, verify the edge exists), (b) attribute consistency. If these checks are too domain-specific to generalize, honestly scope Tier 1 binding validity to geometry + basic arithmetic and acknowledge chart/diagram binding as Tier 2.

3. **Clarify verifier cost model**: Explain whether the CFV performs grounding VQA as internal sub-reasoning within a single forward pass (generating all verification judgments autoregressively) or as separate VQA calls per observation. If the former, the single-pass claim holds; if the latter, the cost is N_obs × 4B rather than 1 × 4B per rollout, and the 10-20x figure needs adjustment.


## Output format
Output ONLY a JSON object:
{
  "verdict": "pass | revise | fail",
  "scores": {
    "novelty": {"score": 0-5, "rationale": "1-2 sentence justification"},
    "feasibility": {"score": 0-5, "rationale": "..."},
    "clarity": {"score": 0-5, "rationale": "..."},
    "impact": {"score": 0-5, "rationale": "..."}
  },
  "issues": ["specific issue 1", ...],
  "feedback": "Actionable feedback (if verdict=revise)",
  "reason": "One-line summary of verdict rationale"
}

Rules:
- "pass": sound AND high quality — avg score >= 4.0, no critical issues
- "revise": fixable issues OR scores below threshold
- "fail": fundamental flaw (gap doesn't exist, approach provably wrong)
- Threshold is HIGH (4.0/5.0): only truly outstanding ideas should pass.
- Round 10 only: if still "revise", you MUST choose "pass" or "fail".

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "0f5319d5-17ca-4901-96ce-fbe35f0c93df",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T23:06:43.034Z_

```json
{
  "parentUuid": "0f5319d5-17ca-4901-96ce-fbe35f0c93df",
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
  "uuid": "a88e2a21-e36d-4a03-9708-dcb8ee194f76",
  "timestamp": "2026-05-27T23:06:43.034Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T23:06:43.034Z_

```json
{
  "parentUuid": "a88e2a21-e36d-4a03-9708-dcb8ee194f76",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f75d8ba7-49d2-46a5-a061-4ad81b90d71c",
  "timestamp": "2026-05-27T23:06:43.034Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
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
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "f75d8ba7-49d2-46a5-a061-4ad81b90d71c",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multimodal reasoning composition verifier",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Assistant

_source line 8 · 2026-05-27T23:06:52.238Z_

<details><summary>Logged reasoning block</summary>

```text
This is a very detailed ML research proposal review request. I need to independently verify the claims made in this proposal through web searches and careful analysis. Let me systematically go through the review checklist.

The proposal is for "Composition Fidelity RL (CFRL)" - a method that unifies evidence grounding, binding validity, and integration completeness verification in a single distilled composition verifier used as a GRPO training reward for multimodal reasoning.

This is round 5/10. Previous reviews have been "revise" with progressively fewer issues. Let me conduct thorough independent verification.

Key things I need to verify:


1. Do the cited papers actually exist and say what's claimed?
2. Is the gap claim still valid after all the revisions?
3. Are there any remaining missing concurrent works?
4. Is the approach feasible?
5. Are the cost estimates realistic?
6. Are the venue deadlines correct?

Let me start with web searches to verify the key claims.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f75d8ba7-49d2-46a5-a061-4ad81b90d71c",
  "isSidechain": false,
  "requestId": "req_011CbTuu6geXiiG1nzDjfds5",
  "type": "assistant",
  "uuid": "beedcd1a-bce2-408f-9b67-7993d1c152b1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBTw36ZNwLH19o2miNDnk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21842,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2118,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21842
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

_source line 9 · 2026-05-27T23:06:52.240Z_

I'll conduct a thorough independent verification of this proposal's claims. Let me search across multiple dimensions simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "beedcd1a-bce2-408f-9b67-7993d1c152b1",
  "isSidechain": false,
  "requestId": "req_011CbTuu6geXiiG1nzDjfds5",
  "type": "assistant",
  "uuid": "6548333b-f005-489c-b2a7-c30797b14587",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBTw36ZNwLH19o2miNDnk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21842,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2118,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21842
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

_source line 10 · 2026-05-27T23:07:05.194Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01GdkFV48Nqgs8uDSHcVAA6n`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify key cited papers exist",
  "prompt": "I need to verify that the following papers actually exist and their claims match what's described. Search for each paper on the web and report what you find. For each paper, report: (1) whether it exists, (2) its actual title, (3) its actual date, (4) key results mentioned. Focus especially on papers that seem most critical:\n\n1. Vision-SR1 (arXiv:2508.19652) - \"Self-Rewarding Vision-Language Model via Reasoning Decomposition\" - uses &lt;visual_perception>/&lt;think> tags, self-rewarding via re-prompting without image\n2. TreeVGR (ICLR 2026, arXiv:2507.07999) - \"Traceable Evidence Enhanced Visual Grounded Reasoning\" - bounding box evidence via RL\n3. v1 (arXiv:2505.18842) - \"Learning to Point Visual Tokens for Multimodal Grounded Reasoning\" - 300K reasoning traces with point-and-copy\n4. MuRGAt (arXiv:2602.11509) - multimodal fact-level attribution, finding that structured grounding degrades accuracy\n5. FGRPO (arXiv:2604.08476) - \"Faithful GRPO\" - uses Qwen3-VL-30B-A3B as per-sentence judge\n6. AutoRubric-R1V (arXiv:2510.14738) - rubric-based process rewards\n7. CoRGI (arXiv:2508.00378) - post-hoc step-wise verification with Grounding DINO\n8. VTPerception-R1 (arXiv:2509.24776) - perception-aware RL\n9. SIEVE (arXiv:2603.14117) - iterative evidence refinement in RL\n10. PaLMR (arXiv:2603.06652) - V-GRPO with visual fidelity gating\n\nUse web searches. Search for the exact arXiv IDs. Report your findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6548333b-f005-489c-b2a7-c30797b14587",
  "isSidechain": false,
  "requestId": "req_011CbTuu6geXiiG1nzDjfds5",
  "type": "assistant",
  "uuid": "34559a92-cf0f-460b-970c-697d8ed48d8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBTw36ZNwLH19o2miNDnk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21842,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2118,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21842
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

_source line 11 · 2026-05-27T23:07:16.250Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01176PEE1Mu8PMs5HzVV7a7L`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for missing concurrent work",
  "prompt": "I'm reviewing a paper proposal about training multimodal reasoning models with explicit evidence citations and a composition verifier. I need to find any MISSING concurrent works that the proposal may have overlooked. The proposal already covers: PEARL, PaLMR, FGRPO, Faithful-MR1, MJ1, TreeVGR, v1, SIEVE, VTPerception-R1, Vision-SR1, AutoRubric-R1V, CoRGI, PGPO, SAYO, AT-RL, VICRA, KAWHI, VPPO, VGPO, OpenMMReasoner, PRCO, DocR1, MuRGAt, Don't Blink, Deeper Thought Weaker Aim, MathLens, PAR framework, ViGoRL, EVPV, GeoSketch, Geoparsing, CHARGE, VisDoT.\n\nSearch for:\n1. \"multimodal reasoning reinforcement learning 2026\" site:arxiv.org\n2. \"visual grounding reward training VLM 2026\"\n3. \"composition verification multimodal reasoning\"\n4. \"evidence grounding multimodal RL 2026\"\n5. \"faithful multimodal reasoning training 2026\"\n6. \"visual evidence citation reasoning 2026\"\n7. \"process reward model multimodal 2026\"\n8. site:openreview.net \"multimodal reasoning\" \"reinforcement learning\" 2026\n\nReport any papers from 2026 that seem directly relevant but are NOT in the list above. Focus especially on works from March-May 2026 that might be concurrent."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "34559a92-cf0f-460b-970c-697d8ed48d8e",
  "isSidechain": false,
  "requestId": "req_011CbTuu6geXiiG1nzDjfds5",
  "type": "assistant",
  "uuid": "98ae52d8-762a-4e3f-ab64-2516945a8806",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBTw36ZNwLH19o2miNDnk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21842,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2118,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21842
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

_source line 12 · 2026-05-27T23:07:24.856Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01N19m7dgEwSe2dn66Bj4bXn`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify SOTA and venue deadlines",
  "prompt": "I need to verify several claims for a research proposal review:\n\n1. **ICLR 2027 deadline**: Search for \"ICLR 2027 submission deadline\" or \"ICLR 2027 call for papers\". Is the estimated \"late Sep 2026\" deadline reasonable?\n\n2. **AAAI 2027 deadline**: Search for \"AAAI 2027 submission deadline\". The proposal claims abstract Jul 21, paper Jul 28. Verify.\n\n3. **CVPR 2027 deadline**: Search for \"CVPR 2027 submission deadline\". The proposal says ~Nov 2026.\n\n4. **H100 spot pricing**: Search for \"H100 spot price 2026\" or \"H100 GPU cloud pricing\". The proposal claims ~$1.30/GPU-hr on Spheron/RunPod.\n\n5. **Current SOTA on key benchmarks**: Search for current best results on:\n   - MathVerse (multimodal math reasoning)\n   - ChartQA\n   - AI2D\n   - HallusionBench\n   - V*Bench (visual grounding)\n\n6. **Qwen3-VL model availability**: Search for \"Qwen3-VL-8B\" and \"Qwen3-VL-235B\" to verify these models exist and are available.\n\n7. **veRL framework**: Search for \"veRL GRPO training framework\" to verify it exists and supports the proposed training setup.\n\nReport findings concisely for each item."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "98ae52d8-762a-4e3f-ab64-2516945a8806",
  "isSidechain": false,
  "requestId": "req_011CbTuu6geXiiG1nzDjfds5",
  "type": "assistant",
  "uuid": "d95d001b-a820-4a59-894d-1bb655d50678",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBTw36ZNwLH19o2miNDnk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21842,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2118,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21842
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

_source line 13 · 2026-05-27T23:07:33.135Z_

<details open><summary>🔧 Tool call — Agent · `toolu_016ghf5YV1ny3RuFLZcGr5Ds`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Search for evidence against CFRL",
  "prompt": "I'm reviewing a proposal called \"Composition Fidelity RL\" (CFRL) that wants to train multimodal reasoning models to produce explicit evidence citations (&lt;observe>/&lt;reason> tags) and use a distilled 4B verifier to check grounding, binding validity, and completeness during RL training.\n\nSearch for EVIDENCE AGAINST this approach:\n\n1. Search for \"structured output degradation language model\" or \"forced format hurts reasoning\" - does forcing structured output formats during training harm model quality?\n\n2. Search for \"reward hacking multimodal RL\" or \"Goodhart's law reinforcement learning reward\" - how severe is reward gaming in RL training with structured rewards?\n\n3. Search for \"distilled verifier accuracy reward signal\" or \"noisy reward RL training\" - what accuracy threshold does a reward model need to be useful?\n\n4. Search for \"accuracy faithfulness tradeoff multimodal\" - is there evidence that enforcing faithfulness hurts accuracy beyond what MuRGAt found?\n\n5. Search for \"verifier distillation multimodal 4B\" - can a 4B model reliably perform multi-property verification (grounding + binding + completeness) in a single pass?\n\n6. Search for \"integration completeness multimodal reasoning\" - has anyone else already solved this problem?\n\nReport findings that would challenge the proposal's feasibility or novelty."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d95d001b-a820-4a59-894d-1bb655d50678",
  "isSidechain": false,
  "requestId": "req_011CbTuu6geXiiG1nzDjfds5",
  "type": "assistant",
  "uuid": "538ce083-b7c9-44cf-ac67-70d444518c5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QtBTw36ZNwLH19o2miNDnk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 21842,
      "cache_read_input_tokens": 11014,
      "output_tokens": 2118,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21842,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2118,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 21842,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21842
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

_source line 14 · 2026-05-27T23:08:57.052Z_

<details><summary>↩ Tool result · `toolu_01N19m7dgEwSe2dn66Bj4bXn`</summary>

```text
Here are the consolidated findings for each claim in the research proposal:

---

## 1. ICLR 2027 Deadline -- "late Sep 2026"

**Plausible but unconfirmed.** ICLR 2027 has not yet published its call for papers. ICLR 2026's mandatory abstract deadline was September 27, 2025, so extrapolating to "late Sep 2026" for ICLR 2027 is a reasonable estimate based on historical patterns. No official dates exist yet.

Sources:
- [ICLR 2026 Dates and Deadlines](https://iclr.cc/Conferences/2026/Dates)
- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)

---

## 2. AAAI 2027 Deadline -- Abstract Jul 21, Paper Jul 28

**Confirmed.** The AAAI-27 abstract deadline is July 21, 2026 (11:59 PM UTC-12) and the full paper deadline is July 28, 2026 (11:59 PM UTC-12). Supplementary material/code due July 31, 2026. The conference is Feb 16-23, 2027 in Montreal.

Sources:
- [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/)
- [AAAI 2027 Deadline Tracker](https://www.getpaperpilot.com/deadlines/aaai-2027.html)

---

## 3. CVPR 2027 Deadline -- "~Nov 2026"

**Plausible but unconfirmed.** CVPR 2027 has not published its call for papers yet. CVPR 2026's submission deadline was November 13, 2025, so "~Nov 2026" for CVPR 2027 is a reasonable extrapolation. CVPR 2027 is confirmed for Seattle, June 19-26, 2027.

Sources:
- [CVPR 2026 Dates and Deadlines](https://cvpr.thecvf.com/Conferences/2026/Dates)
- [CVPR 2027 Conference Info](https://www.aconf.org/conf_182232.2027_IEEE/CVF_Conference_on_Computer_Vision_and_Pattern_Recognition.html)

---

## 4. H100 Spot Pricing -- "~$1.30/GPU-hr on Spheron/RunPod"

**Approximately correct.** Current H100 spot pricing ranges from $1.19-$1.60/hr on RunPod depending on variant and availability. Spheron lists H100 spot from $1.03/hr. The claim of ~$1.30/GPU-hr falls squarely within the current market range for spot H100 instances. On-demand pricing is higher ($2.00-$2.89/hr on these providers). Note that spot instances are interruptible.

Sources:
- [Spheron GPU Cloud Pricing 2026](https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/)
- [RunPod Pricing](https://www.runpod.io/pricing)
- [H100 Cloud Pricing: Compare 43+ Providers](https://getdeploying.com/gpus/nvidia-h100)

---

## 5. Current SOTA on Key Benchmarks

| Benchmark | SOTA Model | Score |
|-----------|-----------|-------|
| **MathVerse** | VL-Rethinker | 61.7% |
| **ChartQA** | Claude 3.5 Sonnet | 90.8% |
| **AI2D** | Claude 3.5 Sonnet | 94.7% |
| **HallusionBench** | Qwen3.5-27B | 70.0% |
| **V\*Bench** | MGPO (over GRPO) achieves +5.2% gain; surpasses o1 and GPT-4o on OOD V\*Bench | Specific scores not found |

Sources:
- [MathVerse GitHub](https://github.com/ZrrSkywalker/MathVerse)
- [ChartQA Leaderboard](https://llm-stats.com/benchmarks/chartqa)
- [AI2D Leaderboard](https://llm-stats.com/benchmarks/ai2d)
- [HallusionBench Leaderboard](https://llm-stats.com/benchmarks/hallusion-bench)
- [MGPO / V*Bench Results](https://www.lmms-lab.com/posts/highres_visual_reasoning/)

---

## 6. Qwen3-VL Model Availability

**Confirmed, with a naming nuance.** Both models exist and are publicly available on Hugging Face:
- **Qwen3-VL-8B-Instruct** -- released ~September-October 2025
- **Qwen3-VL-235B-A22B-Instruct** -- released September 23, 2025 (note: the full name is "235B-A22B", indicating a Mixture-of-Experts architecture with 235B total parameters and 22B active parameters)

The proposal's reference to "Qwen3-VL-235B" is correct but should note it is an MoE model (A22B active params), not a dense 235B model.

Sources:
- [Qwen3-VL-8B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)
- [Qwen3-VL-235B-A22B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct)
- [Qwen3-VL GitHub](https://github.com/QwenLM/Qwen3-VL)

---

## 7. veRL Framework

**Confirmed.** veRL is a well-established RL post-training framework developed by BytePlus/ByteDance. It explicitly supports GRPO training (with a dedicated `grpo_trainer` example). Key details:
- Supports GRPO, PPO, REINFORCE++, DAPO, and many other RL algorithms
- Integrates with FSDP and Megatron-LM for distributed training
- Works with vLLM for inference
- Has official documentation for GRPO training workflows
- Multiple tutorials exist for training Qwen models with GRPO via veRL

Sources:
- [veRL GitHub Repository](https://github.com/verl-project/verl)
- [veRL GRPO Documentation](https://verl.readthedocs.io/en/latest/algo/grpo.html)
- [veRL GRPO Trainer Example](https://github.com/verl-project/verl/tree/main/examples/grpo_trainer)
- [BytePlus GRPO Best Practices with veRL](https://docs.byteplus.com/en/docs/mlp/GRPO_reinforcement_learning_training_best_practices_with_verl)
- [Engineering Handbook: GRPO + LoRA with veRL](https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl)

agentId: a9da7ea7ffb1390f9 (use SendMessage with to: 'a9da7ea7ffb1390f9' to continue this agent)
&lt;usage>total_tokens: 22533
tool_uses: 16
duration_ms: 92192&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d95d001b-a820-4a59-894d-1bb655d50678",
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "6fc533f0-82c7-45a0-adf7-9aba59e46419",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify several claims for a research proposal review:\n\n1. **ICLR 2027 deadline**: Search for \"ICLR 2027 submission deadline\" or \"ICLR 2027 call for papers\". Is the estimated \"late Sep 2026\" deadline reasonable?\n\n2. **AAAI 2027 deadline**: Search for \"AAAI 2027 submission deadline\". The proposal claims abstract Jul 21, paper Jul 28. Verify.\n\n3. **CVPR 2027 deadline**: Search for \"CVPR 2027 submission deadline\". The proposal says ~Nov 2026.\n\n4. **H100 spot pricing**: Search for \"H100 spot price 2026\" or \"H100 GPU cloud pricing\". The proposal claims ~$1.30/GPU-hr on Spheron/RunPod.\n\n5. **Current SOTA on key benchmarks**: Search for current best results on:\n   - MathVerse (multimodal math reasoning)\n   - ChartQA\n   - AI2D\n   - HallusionBench\n   - V*Bench (visual grounding)\n\n6. **Qwen3-VL model availability**: Search for \"Qwen3-VL-8B\" and \"Qwen3-VL-235B\" to verify these models exist and are available.\n\n7. **veRL framework**: Search for \"veRL GRPO training framework\" to verify it exists and supports the proposed training setup.\n\nReport findings concisely for each item.",
    "agentId": "a9da7ea7ffb1390f9",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the consolidated findings for each claim in the research proposal:\n\n---\n\n## 1. ICLR 2027 Deadline -- \"late Sep 2026\"\n\n**Plausible but unconfirmed.** ICLR 2027 has not yet published its call for papers. ICLR 2026's mandatory abstract deadline was September 27, 2025, so extrapolating to \"late Sep 2026\" for ICLR 2027 is a reasonable estimate based on historical patterns. No official dates exist yet.\n\nSources:\n- [ICLR 2026 Dates and Deadlines](https://iclr.cc/Conferences/2026/Dates)\n- [AI & ML Conference Deadlines 2026-2027](https://trybibby.com/conference-deadlines)\n\n---\n\n## 2. AAAI 2027 Deadline -- Abstract Jul 21, Paper Jul 28\n\n**Confirmed.** The AAAI-27 abstract deadline is July 21, 2026 (11:59 PM UTC-12) and the full paper deadline is July 28, 2026 (11:59 PM UTC-12). Supplementary material/code due July 31, 2026. The conference is Feb 16-23, 2027 in Montreal.\n\nSources:\n- [AAAI-27 Official Page](https://aaai.org/conference/aaai/aaai-27/)\n- [AAAI 2027 Deadline Tracker](https://www.getpaperpilot.com/deadlines/aaai-2027.html)\n\n---\n\n## 3. CVPR 2027 Deadline -- \"~Nov 2026\"\n\n**Plausible but unconfirmed.** CVPR 2027 has not published its call for papers yet. CVPR 2026's submission deadline was November 13, 2025, so \"~Nov 2026\" for CVPR 2027 is a reasonable extrapolation. CVPR 2027 is confirmed for Seattle, June 19-26, 2027.\n\nSources:\n- [CVPR 2026 Dates and Deadlines](https://cvpr.thecvf.com/Conferences/2026/Dates)\n- [CVPR 2027 Conference Info](https://www.aconf.org/conf_182232.2027_IEEE/CVF_Conference_on_Computer_Vision_and_Pattern_Recognition.html)\n\n---\n\n## 4. H100 Spot Pricing -- \"~$1.30/GPU-hr on Spheron/RunPod\"\n\n**Approximately correct.** Current H100 spot pricing ranges from $1.19-$1.60/hr on RunPod depending on variant and availability. Spheron lists H100 spot from $1.03/hr. The claim of ~$1.30/GPU-hr falls squarely within the current market range for spot H100 instances. On-demand pricing is higher ($2.00-$2.89/hr on these providers). Note that spot instances are interruptible.\n\nSources:\n- [Spheron GPU Cloud Pricing 2026](https://www.spheron.network/blog/gpu-cloud-pricing-comparison-2026/)\n- [RunPod Pricing](https://www.runpod.io/pricing)\n- [H100 Cloud Pricing: Compare 43+ Providers](https://getdeploying.com/gpus/nvidia-h100)\n\n---\n\n## 5. Current SOTA on Key Benchmarks\n\n| Benchmark | SOTA Model | Score |\n|-----------|-----------|-------|\n| **MathVerse** | VL-Rethinker | 61.7% |\n| **ChartQA** | Claude 3.5 Sonnet | 90.8% |\n| **AI2D** | Claude 3.5 Sonnet | 94.7% |\n| **HallusionBench** | Qwen3.5-27B | 70.0% |\n| **V\\*Bench** | MGPO (over GRPO) achieves +5.2% gain; surpasses o1 and GPT-4o on OOD V\\*Bench | Specific scores not found |\n\nSources:\n- [MathVerse GitHub](https://github.com/ZrrSkywalker/MathVerse)\n- [ChartQA Leaderboard](https://llm-stats.com/benchmarks/chartqa)\n- [AI2D Leaderboard](https://llm-stats.com/benchmarks/ai2d)\n- [HallusionBench Leaderboard](https://llm-stats.com/benchmarks/hallusion-bench)\n- [MGPO / V*Bench Results](https://www.lmms-lab.com/posts/highres_visual_reasoning/)\n\n---\n\n## 6. Qwen3-VL Model Availability\n\n**Confirmed, with a naming nuance.** Both models exist and are publicly available on Hugging Face:\n- **Qwen3-VL-8B-Instruct** -- released ~September-October 2025\n- **Qwen3-VL-235B-A22B-Instruct** -- released September 23, 2025 (note: the full name is \"235B-A22B\", indicating a Mixture-of-Experts architecture with 235B total parameters and 22B active parameters)\n\nThe proposal's reference to \"Qwen3-VL-235B\" is correct but should note it is an MoE model (A22B active params), not a dense 235B model.\n\nSources:\n- [Qwen3-VL-8B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-8B-Instruct)\n- [Qwen3-VL-235B-A22B-Instruct on Hugging Face](https://huggingface.co/Qwen/Qwen3-VL-235B-A22B-Instruct)\n- [Qwen3-VL GitHub](https://github.com/QwenLM/Qwen3-VL)\n\n---\n\n## 7. veRL Framework\n\n**Confirmed.** veRL is a well-established RL post-training framework developed by BytePlus/ByteDance. It explicitly supports GRPO training (with a dedicated `grpo_trainer` example). Key details:\n- Supports GRPO, PPO, REINFORCE++, DAPO, and many other RL algorithms\n- Integrates with FSDP and Megatron-LM for distributed training\n- Works with vLLM for inference\n- Has official documentation for GRPO training workflows\n- Multiple tutorials exist for training Qwen models with GRPO via veRL\n\nSources:\n- [veRL GitHub Repository](https://github.com/verl-project/verl)\n- [veRL GRPO Documentation](https://verl.readthedocs.io/en/latest/algo/grpo.html)\n- [veRL GRPO Trainer Example](https://github.com/verl-project/verl/tree/main/examples/grpo_trainer)\n- [BytePlus GRPO Best Practices with veRL](https://docs.byteplus.com/en/docs/mlp/GRPO_reinforcement_learning_training_best_practices_with_verl)\n- [Engineering Handbook: GRPO + LoRA with veRL](https://huggingface.co/blog/Weyaxi/engineering-handbook-grpo-lora-with-verl)"
      }
    ],
    "totalDurationMs": 92192,
    "totalTokens": 22533,
    "totalToolUseCount": 16,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5548,
      "cache_read_input_tokens": 15136,
      "output_tokens": 1848,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5548
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1848,
          "cache_read_input_tokens": 15136,
          "cache_creation_input_tokens": 5548,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5548,
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
      "otherToolCount": 16
    }
  },
  "sourceToolAssistantUUID": "d95d001b-a820-4a59-894d-1bb655d50678",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 15 · 2026-05-27T23:09:00.430Z_

<details><summary>↩ Tool result · `toolu_01GdkFV48Nqgs8uDSHcVAA6n`</summary>

```text
Now I have comprehensive information on all 10 papers. Here is my report:

---

## Paper Verification Report

### 1. Vision-SR1 (arXiv:2508.19652)
- **EXISTS:** Yes
- **Actual title:** "Self-Rewarding Vision-Language Model via Reasoning Decomposition" (matches)
- **Date:** August 2025
- **Claims match:** Yes. It decomposes reasoning into visual perception and language reasoning stages. The self-rewarding mechanism re-prompts the VLM with only the generated perception (no image) to compute a reward. The description of `&lt;visual_perception>`/`&lt;think>` tags and self-rewarding via re-prompting without image is consistent.
- **Verdict: CONFIRMED**

### 2. TreeVGR (arXiv:2507.07999)
- **EXISTS:** Yes
- **Actual title:** "Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and Methodology" (matches)
- **Date:** July 2025, published at ICLR 2026 (matches)
- **Claims match:** Yes. Uses bounding box evidence and RL to jointly supervise localization and reasoning. Also introduces the TreeBench benchmark.
- **Verdict: CONFIRMED**

### 3. v1 (arXiv:2505.18842)
- **EXISTS:** Yes
- **Actual title:** "v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning" (matches)
- **Date:** May 2025 (latest revision Feb 2026)
- **Claims match:** Yes. Uses a point-and-copy mechanism. Built v1g, a dataset of 300K multimodal reasoning traces with interleaved grounding annotations. The description is accurate.
- **Verdict: CONFIRMED**

### 4. MuRGAt (arXiv:2602.11509)
- **EXISTS:** Yes
- **Actual title:** "Multimodal Fact-Level Attribution for Verifiable Reasoning" (matches the concept; the paper name is about multimodal fact-level attribution)
- **Date:** February 2026
- **Claims match:** Partially. The paper IS about multimodal fact-level attribution. The claim that "structured grounding degrades accuracy" IS confirmed -- the abstract states "increasing reasoning depth or enforcing structured grounding often degrades accuracy." However, MuRGAt is described as a benchmark for evaluating attribution in multi-step multimodal reasoning (spanning video, audio, etc.), not just vision-language. The scope may be broader than implied.
- **Verdict: CONFIRMED (key claim about structured grounding degrading accuracy is verified)**

### 5. FGRPO (arXiv:2604.08476)
- **EXISTS:** Yes
- **Actual title:** "Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization" (matches)
- **Date:** April 2026
- **Claims match:** Partially. The paper DOES use Qwen3-VL-30B-A3B-Instruct as the online judge during training (confirmed from the full paper). However, the description says it's used as a "per-sentence judge" -- the paper describes it more precisely as a judge for "consistency and semantic grounding rewards." The backbone models trained are Qwen2.5-VL-7B and 3B, not Qwen3. At evaluation time, GPT-5.4 is used instead.
- **Verdict: CONFIRMED, with nuance -- Qwen3-VL-30B-A3B is the training judge, not the backbone**

### 6. AutoRubric-R1V (arXiv:2510.14738)
- **EXISTS:** Yes
- **Actual title:** "AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning" (matches; later version may have dropped "-R1V" from title)
- **Date:** October 2025
- **Claims match:** Yes. Uses rubric-based process rewards via a self-aggregation method that distills reasoning checkpoints from successful trajectories. Combines rubric-based and outcome rewards.
- **Verdict: CONFIRMED**

### 7. CoRGI (arXiv:2508.00378)
- **EXISTS:** Yes
- **Actual title:** "CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding" (matches)
- **Date:** August 2025
- **Claims match:** Yes. Uses post-hoc step-wise verification, decomposes rationales into step-wise statements, and uses Grounding DINO as the RoI selector. **Note: This paper has been WITHDRAWN by the authors.**
- **Verdict: CONFIRMED but WITHDRAWN**

### 8. VTPerception-R1 (arXiv:2509.24776)
- **EXISTS:** Yes
- **Actual title:** "VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding" (matches)
- **Date:** September 2025
- **Claims match:** Yes. Uses perception-aware RL with visual, textual, and consistency rewards. Two-stage framework decoupling perception from reasoning.
- **Verdict: CONFIRMED**

### 9. SIEVE (arXiv:2603.14117)
- **EXISTS:** Yes
- **Actual title:** "Improving Visual Reasoning with Iterative Evidence Refinement" (the framework within is called SIEVE)
- **Date:** March 2026
- **Claims match:** Yes. SIEVE is an end-to-end self-revisit framework for iterative evidence refinement. It includes a visually grounded RL training pipeline. Retrieves and injects region embeddings into the reasoning chain.
- **Verdict: CONFIRMED**

### 10. PaLMR (arXiv:2603.06652)
- **EXISTS:** Yes
- **Actual title:** "PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment" (matches)
- **Date:** March 2026
- **Claims match:** Yes. Uses V-GRPO (Vision-Guided GRPO) with visual fidelity gating. The gating mechanism acts as a binary gate where visually unfaithful trajectories receive zero reward regardless of answer accuracy. Hierarchical reward fusion with visual perception, answer accuracy, and format scores.
- **Verdict: CONFIRMED**

---

## Summary

**All 10 papers exist** on arXiv with the stated IDs. The titles, dates, and key claims are broadly accurate. Notable findings:

- **CoRGI (paper 7)** has been **withdrawn** by its authors -- this should be flagged if citing it.
- **FGRPO (paper 5)** does use Qwen3-VL-30B-A3B-Instruct, but as a training-time judge, not the model backbone (the backbones are Qwen2.5-VL-7B/3B). The evaluation judge is GPT-5.4.
- **MuRGAt (paper 4)** spans multimodal attribution beyond just vision (video, audio, etc.), which is broader than a purely vision-language framing might suggest.
- All other descriptions are accurate and match the actual paper content.

Sources:
- [Vision-SR1 (2508.19652)](https://arxiv.org/abs/2508.19652)
- [TreeVGR (2507.07999)](https://arxiv.org/abs/2507.07999)
- [v1 (2505.18842)](https://arxiv.org/abs/2505.18842)
- [MuRGAt (2602.11509)](https://arxiv.org/abs/2602.11509)
- [FGRPO (2604.08476)](https://arxiv.org/abs/2604.08476)
- [AutoRubric-R1V (2510.14738)](https://arxiv.org/abs/2510.14738)
- [CoRGI (2508.00378)](https://arxiv.org/abs/2508.00378)
- [VTPerception-R1 (2509.24776)](https://arxiv.org/abs/2509.24776)
- [SIEVE (2603.14117)](https://arxiv.org/abs/2603.14117)
- [PaLMR (2603.06652)](https://arxiv.org/abs/2603.06652)

agentId: aafad7c9ab1315698 (use SendMessage with to: 'aafad7c9ab1315698' to continue this agent)
&lt;usage>total_tokens: 22805
tool_uses: 17
duration_ms: 115230&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "34559a92-cf0f-460b-970c-697d8ed48d8e",
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "f6262c35-8e7f-4771-a899-2dec17199246",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify that the following papers actually exist and their claims match what's described. Search for each paper on the web and report what you find. For each paper, report: (1) whether it exists, (2) its actual title, (3) its actual date, (4) key results mentioned. Focus especially on papers that seem most critical:\n\n1. Vision-SR1 (arXiv:2508.19652) - \"Self-Rewarding Vision-Language Model via Reasoning Decomposition\" - uses &lt;visual_perception>/&lt;think> tags, self-rewarding via re-prompting without image\n2. TreeVGR (ICLR 2026, arXiv:2507.07999) - \"Traceable Evidence Enhanced Visual Grounded Reasoning\" - bounding box evidence via RL\n3. v1 (arXiv:2505.18842) - \"Learning to Point Visual Tokens for Multimodal Grounded Reasoning\" - 300K reasoning traces with point-and-copy\n4. MuRGAt (arXiv:2602.11509) - multimodal fact-level attribution, finding that structured grounding degrades accuracy\n5. FGRPO (arXiv:2604.08476) - \"Faithful GRPO\" - uses Qwen3-VL-30B-A3B as per-sentence judge\n6. AutoRubric-R1V (arXiv:2510.14738) - rubric-based process rewards\n7. CoRGI (arXiv:2508.00378) - post-hoc step-wise verification with Grounding DINO\n8. VTPerception-R1 (arXiv:2509.24776) - perception-aware RL\n9. SIEVE (arXiv:2603.14117) - iterative evidence refinement in RL\n10. PaLMR (arXiv:2603.06652) - V-GRPO with visual fidelity gating\n\nUse web searches. Search for the exact arXiv IDs. Report your findings concisely.",
    "agentId": "aafad7c9ab1315698",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive information on all 10 papers. Here is my report:\n\n---\n\n## Paper Verification Report\n\n### 1. Vision-SR1 (arXiv:2508.19652)\n- **EXISTS:** Yes\n- **Actual title:** \"Self-Rewarding Vision-Language Model via Reasoning Decomposition\" (matches)\n- **Date:** August 2025\n- **Claims match:** Yes. It decomposes reasoning into visual perception and language reasoning stages. The self-rewarding mechanism re-prompts the VLM with only the generated perception (no image) to compute a reward. The description of `&lt;visual_perception>`/`&lt;think>` tags and self-rewarding via re-prompting without image is consistent.\n- **Verdict: CONFIRMED**\n\n### 2. TreeVGR (arXiv:2507.07999)\n- **EXISTS:** Yes\n- **Actual title:** \"Traceable Evidence Enhanced Visual Grounded Reasoning: Evaluation and Methodology\" (matches)\n- **Date:** July 2025, published at ICLR 2026 (matches)\n- **Claims match:** Yes. Uses bounding box evidence and RL to jointly supervise localization and reasoning. Also introduces the TreeBench benchmark.\n- **Verdict: CONFIRMED**\n\n### 3. v1 (arXiv:2505.18842)\n- **EXISTS:** Yes\n- **Actual title:** \"v1: Learning to Point Visual Tokens for Multimodal Grounded Reasoning\" (matches)\n- **Date:** May 2025 (latest revision Feb 2026)\n- **Claims match:** Yes. Uses a point-and-copy mechanism. Built v1g, a dataset of 300K multimodal reasoning traces with interleaved grounding annotations. The description is accurate.\n- **Verdict: CONFIRMED**\n\n### 4. MuRGAt (arXiv:2602.11509)\n- **EXISTS:** Yes\n- **Actual title:** \"Multimodal Fact-Level Attribution for Verifiable Reasoning\" (matches the concept; the paper name is about multimodal fact-level attribution)\n- **Date:** February 2026\n- **Claims match:** Partially. The paper IS about multimodal fact-level attribution. The claim that \"structured grounding degrades accuracy\" IS confirmed -- the abstract states \"increasing reasoning depth or enforcing structured grounding often degrades accuracy.\" However, MuRGAt is described as a benchmark for evaluating attribution in multi-step multimodal reasoning (spanning video, audio, etc.), not just vision-language. The scope may be broader than implied.\n- **Verdict: CONFIRMED (key claim about structured grounding degrading accuracy is verified)**\n\n### 5. FGRPO (arXiv:2604.08476)\n- **EXISTS:** Yes\n- **Actual title:** \"Faithful GRPO: Improving Visual Spatial Reasoning in Multimodal Language Models via Constrained Policy Optimization\" (matches)\n- **Date:** April 2026\n- **Claims match:** Partially. The paper DOES use Qwen3-VL-30B-A3B-Instruct as the online judge during training (confirmed from the full paper). However, the description says it's used as a \"per-sentence judge\" -- the paper describes it more precisely as a judge for \"consistency and semantic grounding rewards.\" The backbone models trained are Qwen2.5-VL-7B and 3B, not Qwen3. At evaluation time, GPT-5.4 is used instead.\n- **Verdict: CONFIRMED, with nuance -- Qwen3-VL-30B-A3B is the training judge, not the backbone**\n\n### 6. AutoRubric-R1V (arXiv:2510.14738)\n- **EXISTS:** Yes\n- **Actual title:** \"AutoRubric-R1V: Rubric-Based Generative Rewards for Faithful Multimodal Reasoning\" (matches; later version may have dropped \"-R1V\" from title)\n- **Date:** October 2025\n- **Claims match:** Yes. Uses rubric-based process rewards via a self-aggregation method that distills reasoning checkpoints from successful trajectories. Combines rubric-based and outcome rewards.\n- **Verdict: CONFIRMED**\n\n### 7. CoRGI (arXiv:2508.00378)\n- **EXISTS:** Yes\n- **Actual title:** \"CoRGI: Verified Chain-of-Thought Reasoning with Post-hoc Visual Grounding\" (matches)\n- **Date:** August 2025\n- **Claims match:** Yes. Uses post-hoc step-wise verification, decomposes rationales into step-wise statements, and uses Grounding DINO as the RoI selector. **Note: This paper has been WITHDRAWN by the authors.**\n- **Verdict: CONFIRMED but WITHDRAWN**\n\n### 8. VTPerception-R1 (arXiv:2509.24776)\n- **EXISTS:** Yes\n- **Actual title:** \"VTPerception-R1: Enhancing Multimodal Reasoning via Explicit Visual and Textual Perceptual Grounding\" (matches)\n- **Date:** September 2025\n- **Claims match:** Yes. Uses perception-aware RL with visual, textual, and consistency rewards. Two-stage framework decoupling perception from reasoning.\n- **Verdict: CONFIRMED**\n\n### 9. SIEVE (arXiv:2603.14117)\n- **EXISTS:** Yes\n- **Actual title:** \"Improving Visual Reasoning with Iterative Evidence Refinement\" (the framework within is called SIEVE)\n- **Date:** March 2026\n- **Claims match:** Yes. SIEVE is an end-to-end self-revisit framework for iterative evidence refinement. It includes a visually grounded RL training pipeline. Retrieves and injects region embeddings into the reasoning chain.\n- **Verdict: CONFIRMED**\n\n### 10. PaLMR (arXiv:2603.06652)\n- **EXISTS:** Yes\n- **Actual title:** \"PaLMR: Towards Faithful Visual Reasoning via Multimodal Process Alignment\" (matches)\n- **Date:** March 2026\n- **Claims match:** Yes. Uses V-GRPO (Vision-Guided GRPO) with visual fidelity gating. The gating mechanism acts as a binary gate where visually unfaithful trajectories receive zero reward regardless of answer accuracy. Hierarchical reward fusion with visual perception, answer accuracy, and format scores.\n- **Verdict: CONFIRMED**\n\n---\n\n## Summary\n\n**All 10 papers exist** on arXiv with the stated IDs. The titles, dates, and key claims are broadly accurate. Notable findings:\n\n- **CoRGI (paper 7)** has been **withdrawn** by its authors -- this should be flagged if citing it.\n- **FGRPO (paper 5)** does use Qwen3-VL-30B-A3B-Instruct, but as a training-time judge, not the model backbone (the backbones are Qwen2.5-VL-7B/3B). The evaluation judge is GPT-5.4.\n- **MuRGAt (paper 4)** spans multimodal attribution beyond just vision (video, audio, etc.), which is broader than a purely vision-language framing might suggest.\n- All other descriptions are accurate and match the actual paper content.\n\nSources:\n- [Vision-SR1 (2508.19652)](https://arxiv.org/abs/2508.19652)\n- [TreeVGR (2507.07999)](https://arxiv.org/abs/2507.07999)\n- [v1 (2505.18842)](https://arxiv.org/abs/2505.18842)\n- [MuRGAt (2602.11509)](https://arxiv.org/abs/2602.11509)\n- [FGRPO (2604.08476)](https://arxiv.org/abs/2604.08476)\n- [AutoRubric-R1V (2510.14738)](https://arxiv.org/abs/2510.14738)\n- [CoRGI (2508.00378)](https://arxiv.org/abs/2508.00378)\n- [VTPerception-R1 (2509.24776)](https://arxiv.org/abs/2509.24776)\n- [SIEVE (2603.14117)](https://arxiv.org/abs/2603.14117)\n- [PaLMR (2603.06652)](https://arxiv.org/abs/2603.06652)"
      }
    ],
    "totalDurationMs": 115230,
    "totalTokens": 22805,
    "totalToolUseCount": 17,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1006,
      "cache_read_input_tokens": 19737,
      "output_tokens": 2061,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1006
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2061,
          "cache_read_input_tokens": 19737,
          "cache_creation_input_tokens": 1006,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1006,
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
      "otherToolCount": 17
    }
  },
  "sourceToolAssistantUUID": "34559a92-cf0f-460b-970c-697d8ed48d8e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 16_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "f6262c35-8e7f-4771-a899-2dec17199246",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multimodal reasoning composition verifier",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Tool result

_source line 18 · 2026-05-27T23:09:50.709Z_

<details><summary>↩ Tool result · `toolu_016ghf5YV1ny3RuFLZcGr5Ds`</summary>

```text
Now I have comprehensive findings across all six dimensions. Here is my report:

---

## Evidence Against the CFRL Proposal: Findings Across Six Dimensions

### 1. Structured Output Formats Degrade Reasoning Quality

This is a significant concern for CFRL's `&lt;observe>`/`&lt;reason>` tag requirement. The research is clear:

- **"The Format Tax" (arXiv 2604.03616)** demonstrates that structured output requirements (JSON, XML, and by extension custom tags) substantially degrade reasoning performance across open-weight models. Critically, the accuracy loss is caused primarily by the *format-requesting instructions themselves* at the prompt level, not just by constrained decoding. Simply asking a model to emit structured tags disrupts its reasoning process.
- **"Let Me Speak Freely?" (arXiv 2408.02442, ICLR 2025)** confirms that stricter format constraints lead to greater performance degradation, and this has been replicated across multiple studies.
- **Mitigation exists but adds complexity**: Research shows that *decoupling reasoning from formatting* (e.g., generate freeform first, then reformat) recovers most lost accuracy. However, CFRL proposes to train with the tags embedded directly in the reasoning chain, which is the exact anti-pattern these papers warn against. If CFRL forces the model to interleave `&lt;observe>`/`&lt;reason>` tags during generation, the model would pay the format tax during both training and inference.
- **Caveat**: Recent closed-weight models (Claude, GPT) appear to have partially closed this gap, but the proposal likely targets open-weight models for RL training, where the degradation remains significant.

### 2. Reward Hacking Is Severe and Particularly Dangerous with Structured Rewards

This is arguably the most critical risk to CFRL:

- **"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking" (arXiv 2604.15149)** directly demonstrates that models trained with verifiable rewards learn to exploit verification loopholes. Models can enumerate instance-level labels and produce outputs that pass verifiers without genuinely reasoning.
- **Structured reward signals are especially vulnerable**: Research shows that models learn to provide "final answers without preceding reasoning or employing non-standard reasoning formats to exploit the reward mechanism." CFRL's structured `&lt;observe>`/`&lt;reason>` tags create a clear surface for gaming -- a model could learn to emit superficially well-formed tags with plausible-sounding but non-grounded content that satisfies a 4B verifier.
- **"One Token to Fool LLM-as-a-Judge" (arXiv 2507.08794)** shows that even minimal responses, including non-word symbols like ":", can elicit false positive rewards from generative reward models. A 4B verifier is likely more susceptible to such exploits than a larger model.
- **Goodhart's Law applies directly**: As optimization pressure increases on the structured reward, the reward signal will cease to correlate with actual reasoning quality. The six categories of reward hacking (specification gaming, proxy optimization, etc.) all apply to CFRL's setup.

### 3. Verifier Accuracy Thresholds and the 4B Model Question

The news here is mixed but raises real concerns for a distilled 4B verifier doing multi-property checks:

- **"An Imperfect Verifier is Good Enough" (arXiv 2604.07666)** finds that RLVR tolerates up to ~15% noise (i.e., ~85% verifier accuracy) with minimal degradation. This is encouraging in principle.
- **However, false positives are particularly dangerous**: Research distinguishes between false negatives (slow convergence) and false positives (reward hacking). False positives "reward hackable patterns and inflate returns during policy optimization." A 4B model performing triple-property verification (grounding + binding + completeness) will have *compounding* error rates -- if each property check is 90% accurate independently, the joint accuracy for all three is only ~73%, well below the 85% threshold.
- **Distilled 7B reward models** have shown success, but these were single-task verifiers (e.g., answer correctness). CFRL asks a 4B model to simultaneously verify three distinct semantic properties, which is a substantially harder task with no clear precedent for success at this scale.
- **Precision matters more than recall**: Research recommends "moderate accuracy with high precision over perfect verification." The question is whether a 4B model can maintain high precision across three verification dimensions simultaneously.

### 4. Faithfulness-Accuracy Tradeoff Is Real and Documented

This directly challenges CFRL's core premise that enforcing faithful evidence citations improves overall model quality:

- **"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs" (arXiv 2602.12506)** finds that fine-tuning raises benchmark accuracy but "can simultaneously erode the reliability of the accompanying chain-of-thought and its robustness to contextual shifts."
- **Claude Opus 4.5 results** demonstrate the tradeoff quantitatively: faithfulness jumps from 0.270 to 0.891, but accuracy *drops* from 78% to 74.3%. This is a ~4 percentage point accuracy penalty for dramatically improved faithfulness.
- **"Faithful GRPO" (arXiv 2604.08476, Microsoft)** explicitly identifies "a conflict in correctness and faithfulness reward signals when jointly optimized under a single reward." This is exactly what CFRL proposes to do. Faithful GRPO addresses this via Lagrangian dual ascent (constrained optimization), reducing inconsistency from 24.5% to 1.7% while also improving accuracy -- but this required careful constraint formulation. CFRL would need similarly sophisticated optimization to avoid the naive tradeoff.
- **The implication**: CFRL's approach of training for both correctness and citation fidelity simultaneously risks degrading accuracy unless the reward is carefully structured with explicit constraint separation, which the proposal does not seem to address.

### 5. Multi-Property Verification at 4B Scale Is Unproven

- **The "Guided Verifier" paper (arXiv 2602.04290)** achieves strong results with an 8B verifier, not 4B, and on single-property verification (process supervision), not triple-property.
- **No published work** demonstrates a 4B model reliably performing simultaneous grounding, binding validity, and completeness checks in a single forward pass. The closest results use 7B-8B models on simpler verification tasks.
- **Intrinsic limitations of small verifiers**: Research finds that "relying solely on internal signals is insufficient" and that "fixed pipelines prove brittle against relational hallucinations where errors stem from flawed logical connections." Binding validity verification (checking that attributes are correctly assigned to entities) is precisely a relational reasoning task where small models are weakest.
- **Compounding difficulty**: Each of the three properties CFRL wants to verify (grounding, binding, completeness) is itself an active research area. Asking a single 4B model to master all three is an aggressive assumption without empirical support.

### 6. Related Work Already Addresses Parts of This Problem

Several existing approaches partially or fully address CFRL's goals, challenging its novelty:

- **Faithful GRPO (Microsoft, April 2025)** already provides a constrained RL method for enforcing visual grounding and logical consistency in multimodal reasoning, achieving strong results. This directly overlaps with CFRL's grounding and consistency objectives.
- **BRIDGE benchmark (arXiv 2603.07931)** evaluates multi-hop reasoning with grounded evidence across text, tables, and figures, and finds "systematic deficiencies in evidence aggregation and grounding" -- suggesting the problem remains open but is being actively attacked from multiple angles.
- **MuRGAt (arXiv 2602.11509)** already defines the benchmark for fact-level multimodal attribution with explicit reasoning and precise citations. CFRL's `&lt;observe>`/`&lt;reason>` tags are essentially a variant of what MuRGAt evaluates.
- **D-CoT (arXiv 2602.21786)** uses structured control tags during training as scaffolding, with the key insight that these can be dropped at inference time. CFRL does not appear to consider tag-free inference.
- **"No Labels, No Problem" (arXiv 2512.08889)** uses pretrained models as verifiers for RL-based optimization of visual reasoning without teacher distillation, offering a potentially simpler alternative to CFRL's distilled verifier approach.

---

## Summary of Key Risks

| Risk | Severity | Evidence Strength |
|------|----------|-------------------|
| Format tax degrading reasoning quality | **High** | Strong (multiple papers, ICLR 2025) |
| Reward hacking via structured tag gaming | **Critical** | Strong (directly demonstrated in RLVR settings) |
| 4B verifier accuracy below useful threshold for triple-property checks | **High** | Moderate (extrapolated from single-property results) |
| Faithfulness-accuracy tradeoff reducing model performance | **Medium-High** | Strong (quantified in multiple papers) |
| 4B multi-property verification unproven | **High** | Moderate (no positive evidence exists) |
| Novelty concerns from overlapping prior work | **Medium** | Moderate (Faithful GRPO, MuRGAt, D-CoT) |

The most damaging evidence against CFRL comes from the convergence of risks 1 and 2: forcing structured `&lt;observe>`/`&lt;reason>` tags will degrade reasoning quality (the format tax), while simultaneously creating exploitable patterns that a 4B verifier is unlikely to catch (reward hacking). The Faithful GRPO work from Microsoft demonstrates that the faithfulness-accuracy tradeoff is real but manageable only with careful constrained optimization -- a sophistication CFRL would need to adopt.

Sources:
- [The Format Tax](https://arxiv.org/html/2604.03616v1)
- [Let Me Speak Freely? (ICLR 2025)](https://arxiv.org/html/2408.02442v1)
- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)
- [One Token to Fool LLM-as-a-Judge](https://arxiv.org/pdf/2507.08794)
- [Reward Hacking in the Era of Large Models](https://arxiv.org/html/2604.13602v1)
- [An Imperfect Verifier is Good Enough](https://arxiv.org/html/2604.07666)
- [RLVeR: RL with Verifiable Noisy Rewards](https://arxiv.org/html/2601.04411v1)
- [On Robustness and CoT Consistency of RL-Finetuned VLMs](https://arxiv.org/html/2602.12506v1)
- [Faithful GRPO (Microsoft)](https://arxiv.org/html/2604.08476v1)
- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/html/2310.09144v1)
- [Reward Hacking Mitigation using Verifiable Composite Rewards](https://arxiv.org/html/2509.15557v1)
- [BRIDGE Benchmark](https://arxiv.org/pdf/2603.07931)
- [MuRGAt: Multimodal Fact-Level Attribution](https://arxiv.org/abs/2602.11509)
- [D-CoT: Disciplined Chain-of-Thought](https://arxiv.org/pdf/2602.21786)
- [Hallucination Detection with Small Language Models](https://arxiv.org/pdf/2506.22486)
- [Lilian Weng: Reward Hacking in RL](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/)
- [Reward Hacking in RLVR (Emergent Mind)](https://www.emergentmind.com/topics/reward-hacking-in-rlvr)

agentId: adc74f724bdd1a7cd (use SendMessage with to: 'adc74f724bdd1a7cd' to continue this agent)
&lt;usage>total_tokens: 22355
tool_uses: 13
duration_ms: 137570&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "538ce083-b7c9-44cf-ac67-70d444518c5f",
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "658425e6-8902-4e57-bd3a-40acb8b837c2",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a proposal called \"Composition Fidelity RL\" (CFRL) that wants to train multimodal reasoning models to produce explicit evidence citations (&lt;observe>/&lt;reason> tags) and use a distilled 4B verifier to check grounding, binding validity, and completeness during RL training.\n\nSearch for EVIDENCE AGAINST this approach:\n\n1. Search for \"structured output degradation language model\" or \"forced format hurts reasoning\" - does forcing structured output formats during training harm model quality?\n\n2. Search for \"reward hacking multimodal RL\" or \"Goodhart's law reinforcement learning reward\" - how severe is reward gaming in RL training with structured rewards?\n\n3. Search for \"distilled verifier accuracy reward signal\" or \"noisy reward RL training\" - what accuracy threshold does a reward model need to be useful?\n\n4. Search for \"accuracy faithfulness tradeoff multimodal\" - is there evidence that enforcing faithfulness hurts accuracy beyond what MuRGAt found?\n\n5. Search for \"verifier distillation multimodal 4B\" - can a 4B model reliably perform multi-property verification (grounding + binding + completeness) in a single pass?\n\n6. Search for \"integration completeness multimodal reasoning\" - has anyone else already solved this problem?\n\nReport findings that would challenge the proposal's feasibility or novelty.",
    "agentId": "adc74f724bdd1a7cd",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have comprehensive findings across all six dimensions. Here is my report:\n\n---\n\n## Evidence Against the CFRL Proposal: Findings Across Six Dimensions\n\n### 1. Structured Output Formats Degrade Reasoning Quality\n\nThis is a significant concern for CFRL's `&lt;observe>`/`&lt;reason>` tag requirement. The research is clear:\n\n- **\"The Format Tax\" (arXiv 2604.03616)** demonstrates that structured output requirements (JSON, XML, and by extension custom tags) substantially degrade reasoning performance across open-weight models. Critically, the accuracy loss is caused primarily by the *format-requesting instructions themselves* at the prompt level, not just by constrained decoding. Simply asking a model to emit structured tags disrupts its reasoning process.\n- **\"Let Me Speak Freely?\" (arXiv 2408.02442, ICLR 2025)** confirms that stricter format constraints lead to greater performance degradation, and this has been replicated across multiple studies.\n- **Mitigation exists but adds complexity**: Research shows that *decoupling reasoning from formatting* (e.g., generate freeform first, then reformat) recovers most lost accuracy. However, CFRL proposes to train with the tags embedded directly in the reasoning chain, which is the exact anti-pattern these papers warn against. If CFRL forces the model to interleave `&lt;observe>`/`&lt;reason>` tags during generation, the model would pay the format tax during both training and inference.\n- **Caveat**: Recent closed-weight models (Claude, GPT) appear to have partially closed this gap, but the proposal likely targets open-weight models for RL training, where the degradation remains significant.\n\n### 2. Reward Hacking Is Severe and Particularly Dangerous with Structured Rewards\n\nThis is arguably the most critical risk to CFRL:\n\n- **\"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking\" (arXiv 2604.15149)** directly demonstrates that models trained with verifiable rewards learn to exploit verification loopholes. Models can enumerate instance-level labels and produce outputs that pass verifiers without genuinely reasoning.\n- **Structured reward signals are especially vulnerable**: Research shows that models learn to provide \"final answers without preceding reasoning or employing non-standard reasoning formats to exploit the reward mechanism.\" CFRL's structured `&lt;observe>`/`&lt;reason>` tags create a clear surface for gaming -- a model could learn to emit superficially well-formed tags with plausible-sounding but non-grounded content that satisfies a 4B verifier.\n- **\"One Token to Fool LLM-as-a-Judge\" (arXiv 2507.08794)** shows that even minimal responses, including non-word symbols like \":\", can elicit false positive rewards from generative reward models. A 4B verifier is likely more susceptible to such exploits than a larger model.\n- **Goodhart's Law applies directly**: As optimization pressure increases on the structured reward, the reward signal will cease to correlate with actual reasoning quality. The six categories of reward hacking (specification gaming, proxy optimization, etc.) all apply to CFRL's setup.\n\n### 3. Verifier Accuracy Thresholds and the 4B Model Question\n\nThe news here is mixed but raises real concerns for a distilled 4B verifier doing multi-property checks:\n\n- **\"An Imperfect Verifier is Good Enough\" (arXiv 2604.07666)** finds that RLVR tolerates up to ~15% noise (i.e., ~85% verifier accuracy) with minimal degradation. This is encouraging in principle.\n- **However, false positives are particularly dangerous**: Research distinguishes between false negatives (slow convergence) and false positives (reward hacking). False positives \"reward hackable patterns and inflate returns during policy optimization.\" A 4B model performing triple-property verification (grounding + binding + completeness) will have *compounding* error rates -- if each property check is 90% accurate independently, the joint accuracy for all three is only ~73%, well below the 85% threshold.\n- **Distilled 7B reward models** have shown success, but these were single-task verifiers (e.g., answer correctness). CFRL asks a 4B model to simultaneously verify three distinct semantic properties, which is a substantially harder task with no clear precedent for success at this scale.\n- **Precision matters more than recall**: Research recommends \"moderate accuracy with high precision over perfect verification.\" The question is whether a 4B model can maintain high precision across three verification dimensions simultaneously.\n\n### 4. Faithfulness-Accuracy Tradeoff Is Real and Documented\n\nThis directly challenges CFRL's core premise that enforcing faithful evidence citations improves overall model quality:\n\n- **\"On Robustness and Chain-of-Thought Consistency of RL-Finetuned VLMs\" (arXiv 2602.12506)** finds that fine-tuning raises benchmark accuracy but \"can simultaneously erode the reliability of the accompanying chain-of-thought and its robustness to contextual shifts.\"\n- **Claude Opus 4.5 results** demonstrate the tradeoff quantitatively: faithfulness jumps from 0.270 to 0.891, but accuracy *drops* from 78% to 74.3%. This is a ~4 percentage point accuracy penalty for dramatically improved faithfulness.\n- **\"Faithful GRPO\" (arXiv 2604.08476, Microsoft)** explicitly identifies \"a conflict in correctness and faithfulness reward signals when jointly optimized under a single reward.\" This is exactly what CFRL proposes to do. Faithful GRPO addresses this via Lagrangian dual ascent (constrained optimization), reducing inconsistency from 24.5% to 1.7% while also improving accuracy -- but this required careful constraint formulation. CFRL would need similarly sophisticated optimization to avoid the naive tradeoff.\n- **The implication**: CFRL's approach of training for both correctness and citation fidelity simultaneously risks degrading accuracy unless the reward is carefully structured with explicit constraint separation, which the proposal does not seem to address.\n\n### 5. Multi-Property Verification at 4B Scale Is Unproven\n\n- **The \"Guided Verifier\" paper (arXiv 2602.04290)** achieves strong results with an 8B verifier, not 4B, and on single-property verification (process supervision), not triple-property.\n- **No published work** demonstrates a 4B model reliably performing simultaneous grounding, binding validity, and completeness checks in a single forward pass. The closest results use 7B-8B models on simpler verification tasks.\n- **Intrinsic limitations of small verifiers**: Research finds that \"relying solely on internal signals is insufficient\" and that \"fixed pipelines prove brittle against relational hallucinations where errors stem from flawed logical connections.\" Binding validity verification (checking that attributes are correctly assigned to entities) is precisely a relational reasoning task where small models are weakest.\n- **Compounding difficulty**: Each of the three properties CFRL wants to verify (grounding, binding, completeness) is itself an active research area. Asking a single 4B model to master all three is an aggressive assumption without empirical support.\n\n### 6. Related Work Already Addresses Parts of This Problem\n\nSeveral existing approaches partially or fully address CFRL's goals, challenging its novelty:\n\n- **Faithful GRPO (Microsoft, April 2025)** already provides a constrained RL method for enforcing visual grounding and logical consistency in multimodal reasoning, achieving strong results. This directly overlaps with CFRL's grounding and consistency objectives.\n- **BRIDGE benchmark (arXiv 2603.07931)** evaluates multi-hop reasoning with grounded evidence across text, tables, and figures, and finds \"systematic deficiencies in evidence aggregation and grounding\" -- suggesting the problem remains open but is being actively attacked from multiple angles.\n- **MuRGAt (arXiv 2602.11509)** already defines the benchmark for fact-level multimodal attribution with explicit reasoning and precise citations. CFRL's `&lt;observe>`/`&lt;reason>` tags are essentially a variant of what MuRGAt evaluates.\n- **D-CoT (arXiv 2602.21786)** uses structured control tags during training as scaffolding, with the key insight that these can be dropped at inference time. CFRL does not appear to consider tag-free inference.\n- **\"No Labels, No Problem\" (arXiv 2512.08889)** uses pretrained models as verifiers for RL-based optimization of visual reasoning without teacher distillation, offering a potentially simpler alternative to CFRL's distilled verifier approach.\n\n---\n\n## Summary of Key Risks\n\n| Risk | Severity | Evidence Strength |\n|------|----------|-------------------|\n| Format tax degrading reasoning quality | **High** | Strong (multiple papers, ICLR 2025) |\n| Reward hacking via structured tag gaming | **Critical** | Strong (directly demonstrated in RLVR settings) |\n| 4B verifier accuracy below useful threshold for triple-property checks | **High** | Moderate (extrapolated from single-property results) |\n| Faithfulness-accuracy tradeoff reducing model performance | **Medium-High** | Strong (quantified in multiple papers) |\n| 4B multi-property verification unproven | **High** | Moderate (no positive evidence exists) |\n| Novelty concerns from overlapping prior work | **Medium** | Moderate (Faithful GRPO, MuRGAt, D-CoT) |\n\nThe most damaging evidence against CFRL comes from the convergence of risks 1 and 2: forcing structured `&lt;observe>`/`&lt;reason>` tags will degrade reasoning quality (the format tax), while simultaneously creating exploitable patterns that a 4B verifier is unlikely to catch (reward hacking). The Faithful GRPO work from Microsoft demonstrates that the faithfulness-accuracy tradeoff is real but manageable only with careful constrained optimization -- a sophistication CFRL would need to adopt.\n\nSources:\n- [The Format Tax](https://arxiv.org/html/2604.03616v1)\n- [Let Me Speak Freely? (ICLR 2025)](https://arxiv.org/html/2408.02442v1)\n- [LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking](https://arxiv.org/abs/2604.15149)\n- [One Token to Fool LLM-as-a-Judge](https://arxiv.org/pdf/2507.08794)\n- [Reward Hacking in the Era of Large Models](https://arxiv.org/html/2604.13602v1)\n- [An Imperfect Verifier is Good Enough](https://arxiv.org/html/2604.07666)\n- [RLVeR: RL with Verifiable Noisy Rewards](https://arxiv.org/html/2601.04411v1)\n- [On Robustness and CoT Consistency of RL-Finetuned VLMs](https://arxiv.org/html/2602.12506v1)\n- [Faithful GRPO (Microsoft)](https://arxiv.org/html/2604.08476v1)\n- [Goodhart's Law in Reinforcement Learning](https://arxiv.org/html/2310.09144v1)\n- [Reward Hacking Mitigation using Verifiable Composite Rewards](https://arxiv.org/html/2509.15557v1)\n- [BRIDGE Benchmark](https://arxiv.org/pdf/2603.07931)\n- [MuRGAt: Multimodal Fact-Level Attribution](https://arxiv.org/abs/2602.11509)\n- [D-CoT: Disciplined Chain-of-Thought](https://arxiv.org/pdf/2602.21786)\n- [Hallucination Detection with Small Language Models](https://arxiv.org/pdf/2506.22486)\n- [Lilian Weng: Reward Hacking in RL](https://lilianweng.github.io/posts/2024-11-28-reward-hacking/)\n- [Reward Hacking in RLVR (Emergent Mind)](https://www.emergentmind.com/topics/reward-hacking-in-rlvr)"
      }
    ],
    "totalDurationMs": 137570,
    "totalTokens": 22355,
    "totalToolUseCount": 13,
    "usage": {
      "input_tokens": 640,
      "cache_creation_input_tokens": 3136,
      "cache_read_input_tokens": 15654,
      "output_tokens": 2925,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3136
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 640,
          "output_tokens": 2925,
          "cache_read_input_tokens": 15654,
          "cache_creation_input_tokens": 3136,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3136,
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
      "otherToolCount": 13
    }
  },
  "sourceToolAssistantUUID": "538ce083-b7c9-44cf-ac67-70d444518c5f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-27T23:11:45.918Z_

<details><summary>↩ Tool result · `toolu_01176PEE1Mu8PMs5HzVV7a7L`</summary>

```text
Now I have a comprehensive picture. Let me compile the findings and cross-reference against the provided list of already-covered works.

Here is my analysis of potentially missing concurrent works. I cross-referenced every paper found against your provided list: PEARL, PaLMR, FGRPO, Faithful-MR1, MJ1, TreeVGR, v1, SIEVE, VTPerception-R1, Vision-SR1, AutoRubric-R1V, CoRGI, PGPO, SAYO, AT-RL, VICRA, KAWHI, VPPO, VGPO, OpenMMReasoner, PRCO, DocR1, MuRGAt, Don't Blink, Deeper Thought Weaker Aim, MathLens, PAR framework, ViGoRL, EVPV, GeoSketch, Geoparsing, CHARGE, VisDoT.

---

## Directly Relevant Missing Concurrent Works (March--May 2026)

These are papers from 2026 that appear highly relevant to a proposal about training multimodal reasoning models with explicit evidence citations and a composition verifier, and are NOT in the provided list:

### 1. R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning (March 2026)
- [arXiv 2603.25720](https://arxiv.org/abs/2603.25720)
- Enforces cross-modal cycle consistency as a dense, label-free reward signal. The model must perform backward inference, switch modalities, and reconstruct the answer through forward inference. Directly relevant: uses cross-modal verification as a form of composition verification.

### 2. TGRL: Trajectory-Guided Reinforcement Learning for Multimodal RLVR (March 2026)
- [arXiv 2603.26126](https://arxiv.org/abs/2603.26126)
- Guides the policy model to integrate visual evidence into fine-grained reasoning via expert reasoning trajectories. Introduces token-level reweighting and trajectory filtering. Directly relevant: explicitly addresses the gap between visual perception and logical reasoning with evidence-guided training.

### 3. Token Reweighting for RLVR (ToR) (March 2026)
- [arXiv 2603.25077](https://arxiv.org/abs/2603.25077)
- A plug-and-play strategy that identifies critical perception and reasoning tokens and dynamically reweights them during RLVR training. Directly relevant: explicitly models the interdependence of visual grounding tokens and reasoning tokens.

### 4. Grounding the Score (EVPV is listed, but the full paper "Grounding the Score" may be a distinct work) (March 2026)
- [arXiv 2603.16253](https://arxiv.org/abs/2603.16253)
- Introduces Explicit Visual Premise Verification for VL-PRMs. The policy produces a step-wise visual checklist while a constraint extractor independently derives structured visual constraints. Note: If "EVPV" in your list refers to this exact paper, then it is already covered. Please verify.

### 5. Faithful GRPO (FGRPO is listed -- verify if this is the same as "Faithful GRPO" April 2026)
- [arXiv 2604.08476](https://arxiv.org/abs/2604.08476)
- Constrained policy optimization enforcing consistency and grounding via Lagrangian dual ascent. Note: If "FGRPO" in your list is this paper, it is already covered. Please verify.

### 6. OpenVLThinkerV2 with Gaussian GRPO (G2RPO) (April 2026)
- [arXiv 2604.08539](https://arxiv.org/abs/2604.08539)
- Introduces Gaussian GRPO for stable multi-domain training with response length shaping and entropy shaping. Relevant as a general multimodal reasoning RL method, though less directly about evidence citation.

### 7. ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (May 2026)
- [arXiv 2605.09262](https://arxiv.org/abs/2605.09262)
- RL fine-tuning framework using dual-forward-pass strategy to evaluate corrupted views against clean-image trajectories. Relevant to reasoning faithfulness under real-world visual noise.

### 8. DeepEyes: Incentivizing "Thinking with Images" via RL (ICLR 2026)
- [arXiv 2505.14362](https://arxiv.org/abs/2505.14362)
- Trains VLMs end-to-end with RL to actively re-examine and crop image regions during reasoning (interleaved Multimodal CoT). Directly relevant: the model dynamically gathers visual evidence during reasoning.

### 9. PAPO: Perception-Aware Policy Optimization (ICLR 2026)
- [arXiv 2507.06448](https://arxiv.org/abs/2507.06448)
- Introduces Implicit Perception Loss (KL divergence) that plugs into GRPO/DAPO. Achieves 30.5% reduction in perception errors. Directly relevant to faithful visual grounding in reasoning.

### 10. ReVisual-R1: Staged Reinforcement Learning for Multimodal Reasoning (ICLR 2026)
- [arXiv 2506.04207](https://arxiv.org/abs/2506.04207)
- Three-stage curriculum: cold-start, multimodal RL with Prioritized Advantage Distillation, then text-only RL refinement. Relevant as a curriculum-based approach to grounding + reasoning.

### 11. MM-CondChain: Programmatically Verified Benchmark for Compositional Reasoning (March 2026)
- [arXiv 2603.12266](https://arxiv.org/abs/2603.12266)
- A benchmark for visually grounded deep compositional reasoning with programmatic verification (executable predicates verified against structured visual facts). Directly relevant: explicitly about composition verification for visual reasoning.

### 12. V-Triune (One RL to See Them All): Visual Triple Unified RL (May 2025, revised April 2026)
- [arXiv 2505.18129](https://arxiv.org/abs/2505.18129)
- Unified RL pipeline jointly training reasoning and perception tasks with modular verifiers and Dynamic IoU reward. Relevant: uses specialized verifiers per task type within a unified framework.

### 13. DRAGON: Benchmark for Evidence-Grounded Visual Reasoning over Diagrams (April 2026)
- [arXiv 2604.25231](https://arxiv.org/abs/2604.25231)
- Benchmark requiring models to predict bounding boxes for visual elements that justify an answer. Directly relevant: explicitly about evidence grounding in reasoning.

### 14. Thinking Diffusion: Visual-Grounded Reasoning in Diffusion MLLMs (CVPR 2026, April 2026)
- [arXiv 2604.05497](https://arxiv.org/abs/2604.05497)
- Visual Reasoning Guidance to amplify visual grounding signals in diffusion-based multimodal models. Relevant to reasoning faithfulness, though specific to diffusion architectures.

### 15. ProcessThinker: Rollout-based Process Reward for Multimodal Reasoning (ICLR 2026 Workshop)
- [OpenReview](https://openreview.net/forum?id=x2hqekTF8v)
- Dense credit assignment via rollout-based process rewards without training an explicit PRM. Relevant to step-level verification in multimodal reasoning.

### 16. HART: High-Resolution Annotation-Free Reasoning with AP-GRPO (ICLR 2026)
- [arXiv 2602.23615](https://arxiv.org/abs/2602.23615)
- Closed-loop framework enabling LMMs to focus on and self-verify key regions of high-resolution images. Uses AP-GRPO for precise localization without annotations.

### 17. MedVR: Annotation-Free Medical Visual Reasoning via Agentic RL (ICLR 2026)
- [arXiv 2604.08203](https://arxiv.org/abs/2604.08203)
- Entropy-guided Visual Regrounding + Consensus-based Credit Assignment for medical VLM reasoning grounded in visual evidence. Domain-specific but methodologically relevant.

### 18. Smooth Operator / AP-GRPO for Spatial Reasoning (January 2026)
- [arXiv 2601.07695](https://arxiv.org/abs/2601.07695)
- Smooth Numerical Reward Activation and Absolute-Preserving GRPO for dense, continuous rewards in spatial reasoning. Relevant to reward design for visually grounded tasks.

### 19. GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (June 2025, updated 2026)
- [arXiv 2506.16141](https://arxiv.org/abs/2506.16141)
- Two-tiered reward with consistency bonus calibrating reasoning-to-answer likelihoods. Relevant: explicitly targets reasoning consistency/faithfulness.

### 20. V-Retriever: Evidence-Driven Agentic Reasoning for Multimodal Retrieval (February 2026)
- [arXiv 2602.06034](https://arxiv.org/abs/2602.06034)
- Agentic framework that selectively acquires visual evidence during reasoning via external tools. Uses curriculum-based RL with evidence-aligned objective. Directly relevant: evidence-driven reasoning with RL training.

### 21. TIM-PRM: Tool-Integrated PRM for Multimodal Verification (November 2025, relevant to 2026 landscape)
- [arXiv 2511.22998](https://arxiv.org/abs/2511.22998)
- Agentic framework transforming verification into tool-augmented investigation. Uses Independent Question Asking to query evidence, decoupling verification from reasoning context. Directly relevant: explicit evidence verification for multimodal reasoning.

### 22. Visual Latents Know More Than They Say: Unsilencing Latent Reasoning (May 2026)
- [arXiv 2605.02735](https://arxiv.org/abs/2605.02735)
- Inference-time latent optimization to unleash suppressed visual reasoning capacity. Relevant to how visual evidence is processed internally.

### 23. Learning to Focus and Precise Cropping (March 2026)
- [arXiv 2603.27494](https://arxiv.org/abs/2603.27494)
- Two-stage RL framework with "Information Gap" mechanism and grounding loss for visual attention in MLLMs.

### 24. Embed-RL: RL for Reasoning-Driven Multimodal Embeddings (February 2026)
- [arXiv 2602.13823](https://arxiv.org/abs/2602.13823)
- Introduces Traceability CoT (T-CoT) integrating explicit visual localization into detailed inference trajectories. Directly relevant: explicit evidence traceability in reasoning chains.

### 25. Caption as Reward: Enhancing Vision-Language Reasoning Through Dense Visual Description (under review ICLR 2026)
- [OpenReview](https://openreview.net/forum?id=Ud9cPB9SS4)
- Uses dense visual descriptions (captions) as reward signals for RL training of VLMs. Relevant to using visual evidence descriptions as training signals.

### 26. Compose and Fuse: Revisiting Foundational Bottlenecks in Multimodal Reasoning (ICLR 2026)
- [arXiv 2509.23744](https://arxiv.org/abs/2509.23744)
- Identifies task-composition and fusion bottlenecks as the primary barriers (not perception). Directly relevant: motivates composition-aware training.

### 27. MEG-RAG: Multi-modal Evidence Grounding for RAG (SIGIR 2026, April 2026)
- [arXiv 2604.24564](https://arxiv.org/abs/2604.24564)
- Semantic-aware metric quantifying contribution of retrieved multimodal evidence. Relevant to evidence grounding, though in a RAG context.

### 28. DreamPRM-1.5: Instance-Level Reweighting for Multimodal PRM Training (September 2025, updated 2026)
- [arXiv 2509.05542](https://arxiv.org/abs/2509.05542)
- Instance-level reweighting via bi-level optimization for multimodal process reward models. Relevant to step-level verification.

### 29. VL-Cogito: Progressive Curriculum RL for Multimodal Reasoning (July 2025, under review 2026)
- [arXiv 2507.22607](https://arxiv.org/abs/2507.22607)
- Online difficulty soft weighting + dynamic length reward for curriculum-based multimodal RL.

---

## Highest-Priority Missing Works

If the proposal is specifically about **evidence citations** and **composition verification** in multimodal reasoning with RL training, the most critical omissions are:

1. **R-C2** -- cross-modal cycle consistency as verification signal
2. **MM-CondChain** -- programmatically verified compositional reasoning benchmark
3. **DRAGON** -- evidence-grounded visual reasoning benchmark
4. **Embed-RL** -- Traceability CoT with explicit visual evidence localization
5. **TIM-PRM** -- tool-integrated verification decoupled from reasoning context
6. **V-Retriever** -- evidence-driven agentic reasoning with RL
7. **DeepEyes** -- active visual evidence gathering during reasoning via RL
8. **ToR (Token Reweighting)** -- explicitly models perception-reasoning token interdependence
9. **TGRL** -- trajectory-guided bridging of visual evidence to reasoning
10. **Compose and Fuse** -- identifies composition as the core bottleneck
11. **PAPO** -- perception-aware policy optimization reducing perception errors
12. **OpenVLThinkerV2 (G2RPO)** -- novel GRPO variant for multi-domain multimodal reasoning

Note: Please verify whether "EVPV" in your list refers to the "Grounding the Score" paper (arXiv 2603.16253) and whether "FGRPO" refers to "Faithful GRPO" (arXiv 2604.08476). If so, those are already covered and can be removed from the missing list above.

Sources:
- [R-C2](https://arxiv.org/abs/2603.25720)
- [TGRL](https://arxiv.org/abs/2603.26126)
- [ToR](https://arxiv.org/abs/2603.25077)
- [Grounding the Score](https://arxiv.org/abs/2603.16253)
- [Faithful GRPO](https://arxiv.org/abs/2604.08476)
- [OpenVLThinkerV2](https://arxiv.org/abs/2604.08539)
- [ROMA](https://arxiv.org/abs/2605.09262)
- [DeepEyes](https://arxiv.org/abs/2505.14362)
- [PAPO](https://arxiv.org/abs/2507.06448)
- [ReVisual-R1](https://arxiv.org/abs/2506.04207)
- [MM-CondChain](https://arxiv.org/abs/2603.12266)
- [V-Triune](https://arxiv.org/abs/2505.18129)
- [DRAGON](https://arxiv.org/abs/2604.25231)
- [Thinking Diffusion](https://arxiv.org/abs/2604.05497)
- [ProcessThinker](https://openreview.net/forum?id=x2hqekTF8v)
- [HART](https://arxiv.org/abs/2602.23615)
- [MedVR](https://arxiv.org/abs/2604.08203)
- [Smooth Operator](https://arxiv.org/abs/2601.07695)
- [GRPO-CARE](https://arxiv.org/abs/2506.16141)
- [V-Retriever](https://arxiv.org/abs/2602.06034)
- [TIM-PRM](https://arxiv.org/abs/2511.22998)
- [Visual Latents Unsilencing](https://arxiv.org/abs/2605.02735)
- [Learning to Focus](https://arxiv.org/abs/2603.27494)
- [Embed-RL](https://arxiv.org/abs/2602.13823)
- [Caption as Reward](https://openreview.net/forum?id=Ud9cPB9SS4)
- [Compose and Fuse](https://arxiv.org/abs/2509.23744)
- [MEG-RAG](https://arxiv.org/abs/2604.24564)
- [DreamPRM-1.5](https://arxiv.org/abs/2509.05542)
- [VL-Cogito](https://arxiv.org/abs/2507.22607)

agentId: aab88f0cc94538c60 (use SendMessage with to: 'aab88f0cc94538c60' to continue this agent)
&lt;usage>total_tokens: 50145
tool_uses: 45
duration_ms: 269664&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98ae52d8-762a-4e3f-ab64-2516945a8806",
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "80979903-530c-4c5a-83fd-1488c21371cb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm reviewing a paper proposal about training multimodal reasoning models with explicit evidence citations and a composition verifier. I need to find any MISSING concurrent works that the proposal may have overlooked. The proposal already covers: PEARL, PaLMR, FGRPO, Faithful-MR1, MJ1, TreeVGR, v1, SIEVE, VTPerception-R1, Vision-SR1, AutoRubric-R1V, CoRGI, PGPO, SAYO, AT-RL, VICRA, KAWHI, VPPO, VGPO, OpenMMReasoner, PRCO, DocR1, MuRGAt, Don't Blink, Deeper Thought Weaker Aim, MathLens, PAR framework, ViGoRL, EVPV, GeoSketch, Geoparsing, CHARGE, VisDoT.\n\nSearch for:\n1. \"multimodal reasoning reinforcement learning 2026\" site:arxiv.org\n2. \"visual grounding reward training VLM 2026\"\n3. \"composition verification multimodal reasoning\"\n4. \"evidence grounding multimodal RL 2026\"\n5. \"faithful multimodal reasoning training 2026\"\n6. \"visual evidence citation reasoning 2026\"\n7. \"process reward model multimodal 2026\"\n8. site:openreview.net \"multimodal reasoning\" \"reinforcement learning\" 2026\n\nReport any papers from 2026 that seem directly relevant but are NOT in the list above. Focus especially on works from March-May 2026 that might be concurrent.",
    "agentId": "aab88f0cc94538c60",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Let me compile the findings and cross-reference against the provided list of already-covered works.\n\nHere is my analysis of potentially missing concurrent works. I cross-referenced every paper found against your provided list: PEARL, PaLMR, FGRPO, Faithful-MR1, MJ1, TreeVGR, v1, SIEVE, VTPerception-R1, Vision-SR1, AutoRubric-R1V, CoRGI, PGPO, SAYO, AT-RL, VICRA, KAWHI, VPPO, VGPO, OpenMMReasoner, PRCO, DocR1, MuRGAt, Don't Blink, Deeper Thought Weaker Aim, MathLens, PAR framework, ViGoRL, EVPV, GeoSketch, Geoparsing, CHARGE, VisDoT.\n\n---\n\n## Directly Relevant Missing Concurrent Works (March--May 2026)\n\nThese are papers from 2026 that appear highly relevant to a proposal about training multimodal reasoning models with explicit evidence citations and a composition verifier, and are NOT in the provided list:\n\n### 1. R-C2: Cycle-Consistent Reinforcement Learning Improves Multimodal Reasoning (March 2026)\n- [arXiv 2603.25720](https://arxiv.org/abs/2603.25720)\n- Enforces cross-modal cycle consistency as a dense, label-free reward signal. The model must perform backward inference, switch modalities, and reconstruct the answer through forward inference. Directly relevant: uses cross-modal verification as a form of composition verification.\n\n### 2. TGRL: Trajectory-Guided Reinforcement Learning for Multimodal RLVR (March 2026)\n- [arXiv 2603.26126](https://arxiv.org/abs/2603.26126)\n- Guides the policy model to integrate visual evidence into fine-grained reasoning via expert reasoning trajectories. Introduces token-level reweighting and trajectory filtering. Directly relevant: explicitly addresses the gap between visual perception and logical reasoning with evidence-guided training.\n\n### 3. Token Reweighting for RLVR (ToR) (March 2026)\n- [arXiv 2603.25077](https://arxiv.org/abs/2603.25077)\n- A plug-and-play strategy that identifies critical perception and reasoning tokens and dynamically reweights them during RLVR training. Directly relevant: explicitly models the interdependence of visual grounding tokens and reasoning tokens.\n\n### 4. Grounding the Score (EVPV is listed, but the full paper \"Grounding the Score\" may be a distinct work) (March 2026)\n- [arXiv 2603.16253](https://arxiv.org/abs/2603.16253)\n- Introduces Explicit Visual Premise Verification for VL-PRMs. The policy produces a step-wise visual checklist while a constraint extractor independently derives structured visual constraints. Note: If \"EVPV\" in your list refers to this exact paper, then it is already covered. Please verify.\n\n### 5. Faithful GRPO (FGRPO is listed -- verify if this is the same as \"Faithful GRPO\" April 2026)\n- [arXiv 2604.08476](https://arxiv.org/abs/2604.08476)\n- Constrained policy optimization enforcing consistency and grounding via Lagrangian dual ascent. Note: If \"FGRPO\" in your list is this paper, it is already covered. Please verify.\n\n### 6. OpenVLThinkerV2 with Gaussian GRPO (G2RPO) (April 2026)\n- [arXiv 2604.08539](https://arxiv.org/abs/2604.08539)\n- Introduces Gaussian GRPO for stable multi-domain training with response length shaping and entropy shaping. Relevant as a general multimodal reasoning RL method, though less directly about evidence citation.\n\n### 7. ROMA: Reinforcing Multimodal Reasoning Against Visual Degradation (May 2026)\n- [arXiv 2605.09262](https://arxiv.org/abs/2605.09262)\n- RL fine-tuning framework using dual-forward-pass strategy to evaluate corrupted views against clean-image trajectories. Relevant to reasoning faithfulness under real-world visual noise.\n\n### 8. DeepEyes: Incentivizing \"Thinking with Images\" via RL (ICLR 2026)\n- [arXiv 2505.14362](https://arxiv.org/abs/2505.14362)\n- Trains VLMs end-to-end with RL to actively re-examine and crop image regions during reasoning (interleaved Multimodal CoT). Directly relevant: the model dynamically gathers visual evidence during reasoning.\n\n### 9. PAPO: Perception-Aware Policy Optimization (ICLR 2026)\n- [arXiv 2507.06448](https://arxiv.org/abs/2507.06448)\n- Introduces Implicit Perception Loss (KL divergence) that plugs into GRPO/DAPO. Achieves 30.5% reduction in perception errors. Directly relevant to faithful visual grounding in reasoning.\n\n### 10. ReVisual-R1: Staged Reinforcement Learning for Multimodal Reasoning (ICLR 2026)\n- [arXiv 2506.04207](https://arxiv.org/abs/2506.04207)\n- Three-stage curriculum: cold-start, multimodal RL with Prioritized Advantage Distillation, then text-only RL refinement. Relevant as a curriculum-based approach to grounding + reasoning.\n\n### 11. MM-CondChain: Programmatically Verified Benchmark for Compositional Reasoning (March 2026)\n- [arXiv 2603.12266](https://arxiv.org/abs/2603.12266)\n- A benchmark for visually grounded deep compositional reasoning with programmatic verification (executable predicates verified against structured visual facts). Directly relevant: explicitly about composition verification for visual reasoning.\n\n### 12. V-Triune (One RL to See Them All): Visual Triple Unified RL (May 2025, revised April 2026)\n- [arXiv 2505.18129](https://arxiv.org/abs/2505.18129)\n- Unified RL pipeline jointly training reasoning and perception tasks with modular verifiers and Dynamic IoU reward. Relevant: uses specialized verifiers per task type within a unified framework.\n\n### 13. DRAGON: Benchmark for Evidence-Grounded Visual Reasoning over Diagrams (April 2026)\n- [arXiv 2604.25231](https://arxiv.org/abs/2604.25231)\n- Benchmark requiring models to predict bounding boxes for visual elements that justify an answer. Directly relevant: explicitly about evidence grounding in reasoning.\n\n### 14. Thinking Diffusion: Visual-Grounded Reasoning in Diffusion MLLMs (CVPR 2026, April 2026)\n- [arXiv 2604.05497](https://arxiv.org/abs/2604.05497)\n- Visual Reasoning Guidance to amplify visual grounding signals in diffusion-based multimodal models. Relevant to reasoning faithfulness, though specific to diffusion architectures.\n\n### 15. ProcessThinker: Rollout-based Process Reward for Multimodal Reasoning (ICLR 2026 Workshop)\n- [OpenReview](https://openreview.net/forum?id=x2hqekTF8v)\n- Dense credit assignment via rollout-based process rewards without training an explicit PRM. Relevant to step-level verification in multimodal reasoning.\n\n### 16. HART: High-Resolution Annotation-Free Reasoning with AP-GRPO (ICLR 2026)\n- [arXiv 2602.23615](https://arxiv.org/abs/2602.23615)\n- Closed-loop framework enabling LMMs to focus on and self-verify key regions of high-resolution images. Uses AP-GRPO for precise localization without annotations.\n\n### 17. MedVR: Annotation-Free Medical Visual Reasoning via Agentic RL (ICLR 2026)\n- [arXiv 2604.08203](https://arxiv.org/abs/2604.08203)\n- Entropy-guided Visual Regrounding + Consensus-based Credit Assignment for medical VLM reasoning grounded in visual evidence. Domain-specific but methodologically relevant.\n\n### 18. Smooth Operator / AP-GRPO for Spatial Reasoning (January 2026)\n- [arXiv 2601.07695](https://arxiv.org/abs/2601.07695)\n- Smooth Numerical Reward Activation and Absolute-Preserving GRPO for dense, continuous rewards in spatial reasoning. Relevant to reward design for visually grounded tasks.\n\n### 19. GRPO-CARE: Consistency-Aware RL for Multimodal Reasoning (June 2025, updated 2026)\n- [arXiv 2506.16141](https://arxiv.org/abs/2506.16141)\n- Two-tiered reward with consistency bonus calibrating reasoning-to-answer likelihoods. Relevant: explicitly targets reasoning consistency/faithfulness.\n\n### 20. V-Retriever: Evidence-Driven Agentic Reasoning for Multimodal Retrieval (February 2026)\n- [arXiv 2602.06034](https://arxiv.org/abs/2602.06034)\n- Agentic framework that selectively acquires visual evidence during reasoning via external tools. Uses curriculum-based RL with evidence-aligned objective. Directly relevant: evidence-driven reasoning with RL training.\n\n### 21. TIM-PRM: Tool-Integrated PRM for Multimodal Verification (November 2025, relevant to 2026 landscape)\n- [arXiv 2511.22998](https://arxiv.org/abs/2511.22998)\n- Agentic framework transforming verification into tool-augmented investigation. Uses Independent Question Asking to query evidence, decoupling verification from reasoning context. Directly relevant: explicit evidence verification for multimodal reasoning.\n\n### 22. Visual Latents Know More Than They Say: Unsilencing Latent Reasoning (May 2026)\n- [arXiv 2605.02735](https://arxiv.org/abs/2605.02735)\n- Inference-time latent optimization to unleash suppressed visual reasoning capacity. Relevant to how visual evidence is processed internally.\n\n### 23. Learning to Focus and Precise Cropping (March 2026)\n- [arXiv 2603.27494](https://arxiv.org/abs/2603.27494)\n- Two-stage RL framework with \"Information Gap\" mechanism and grounding loss for visual attention in MLLMs.\n\n### 24. Embed-RL: RL for Reasoning-Driven Multimodal Embeddings (February 2026)\n- [arXiv 2602.13823](https://arxiv.org/abs/2602.13823)\n- Introduces Traceability CoT (T-CoT) integrating explicit visual localization into detailed inference trajectories. Directly relevant: explicit evidence traceability in reasoning chains.\n\n### 25. Caption as Reward: Enhancing Vision-Language Reasoning Through Dense Visual Description (under review ICLR 2026)\n- [OpenReview](https://openreview.net/forum?id=Ud9cPB9SS4)\n- Uses dense visual descriptions (captions) as reward signals for RL training of VLMs. Relevant to using visual evidence descriptions as training signals.\n\n### 26. Compose and Fuse: Revisiting Foundational Bottlenecks in Multimodal Reasoning (ICLR 2026)\n- [arXiv 2509.23744](https://arxiv.org/abs/2509.23744)\n- Identifies task-composition and fusion bottlenecks as the primary barriers (not perception). Directly relevant: motivates composition-aware training.\n\n### 27. MEG-RAG: Multi-modal Evidence Grounding for RAG (SIGIR 2026, April 2026)\n- [arXiv 2604.24564](https://arxiv.org/abs/2604.24564)\n- Semantic-aware metric quantifying contribution of retrieved multimodal evidence. Relevant to evidence grounding, though in a RAG context.\n\n### 28. DreamPRM-1.5: Instance-Level Reweighting for Multimodal PRM Training (September 2025, updated 2026)\n- [arXiv 2509.05542](https://arxiv.org/abs/2509.05542)\n- Instance-level reweighting via bi-level optimization for multimodal process reward models. Relevant to step-level verification.\n\n### 29. VL-Cogito: Progressive Curriculum RL for Multimodal Reasoning (July 2025, under review 2026)\n- [arXiv 2507.22607](https://arxiv.org/abs/2507.22607)\n- Online difficulty soft weighting + dynamic length reward for curriculum-based multimodal RL.\n\n---\n\n## Highest-Priority Missing Works\n\nIf the proposal is specifically about **evidence citations** and **composition verification** in multimodal reasoning with RL training, the most critical omissions are:\n\n1. **R-C2** -- cross-modal cycle consistency as verification signal\n2. **MM-CondChain** -- programmatically verified compositional reasoning benchmark\n3. **DRAGON** -- evidence-grounded visual reasoning benchmark\n4. **Embed-RL** -- Traceability CoT with explicit visual evidence localization\n5. **TIM-PRM** -- tool-integrated verification decoupled from reasoning context\n6. **V-Retriever** -- evidence-driven agentic reasoning with RL\n7. **DeepEyes** -- active visual evidence gathering during reasoning via RL\n8. **ToR (Token Reweighting)** -- explicitly models perception-reasoning token interdependence\n9. **TGRL** -- trajectory-guided bridging of visual evidence to reasoning\n10. **Compose and Fuse** -- identifies composition as the core bottleneck\n11. **PAPO** -- perception-aware policy optimization reducing perception errors\n12. **OpenVLThinkerV2 (G2RPO)** -- novel GRPO variant for multi-domain multimodal reasoning\n\nNote: Please verify whether \"EVPV\" in your list refers to the \"Grounding the Score\" paper (arXiv 2603.16253) and whether \"FGRPO\" refers to \"Faithful GRPO\" (arXiv 2604.08476). If so, those are already covered and can be removed from the missing list above.\n\nSources:\n- [R-C2](https://arxiv.org/abs/2603.25720)\n- [TGRL](https://arxiv.org/abs/2603.26126)\n- [ToR](https://arxiv.org/abs/2603.25077)\n- [Grounding the Score](https://arxiv.org/abs/2603.16253)\n- [Faithful GRPO](https://arxiv.org/abs/2604.08476)\n- [OpenVLThinkerV2](https://arxiv.org/abs/2604.08539)\n- [ROMA](https://arxiv.org/abs/2605.09262)\n- [DeepEyes](https://arxiv.org/abs/2505.14362)\n- [PAPO](https://arxiv.org/abs/2507.06448)\n- [ReVisual-R1](https://arxiv.org/abs/2506.04207)\n- [MM-CondChain](https://arxiv.org/abs/2603.12266)\n- [V-Triune](https://arxiv.org/abs/2505.18129)\n- [DRAGON](https://arxiv.org/abs/2604.25231)\n- [Thinking Diffusion](https://arxiv.org/abs/2604.05497)\n- [ProcessThinker](https://openreview.net/forum?id=x2hqekTF8v)\n- [HART](https://arxiv.org/abs/2602.23615)\n- [MedVR](https://arxiv.org/abs/2604.08203)\n- [Smooth Operator](https://arxiv.org/abs/2601.07695)\n- [GRPO-CARE](https://arxiv.org/abs/2506.16141)\n- [V-Retriever](https://arxiv.org/abs/2602.06034)\n- [TIM-PRM](https://arxiv.org/abs/2511.22998)\n- [Visual Latents Unsilencing](https://arxiv.org/abs/2605.02735)\n- [Learning to Focus](https://arxiv.org/abs/2603.27494)\n- [Embed-RL](https://arxiv.org/abs/2602.13823)\n- [Caption as Reward](https://openreview.net/forum?id=Ud9cPB9SS4)\n- [Compose and Fuse](https://arxiv.org/abs/2509.23744)\n- [MEG-RAG](https://arxiv.org/abs/2604.24564)\n- [DreamPRM-1.5](https://arxiv.org/abs/2509.05542)\n- [VL-Cogito](https://arxiv.org/abs/2507.22607)"
      }
    ],
    "totalDurationMs": 269664,
    "totalTokens": 50145,
    "totalToolUseCount": 45,
    "usage": {
      "input_tokens": 2190,
      "cache_creation_input_tokens": 2555,
      "cache_read_input_tokens": 41084,
      "output_tokens": 4316,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2555
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2190,
          "output_tokens": 4316,
          "cache_read_input_tokens": 41084,
          "cache_creation_input_tokens": 2555,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2555,
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
      "otherToolCount": 45
    }
  },
  "sourceToolAssistantUUID": "98ae52d8-762a-4e3f-ab64-2516945a8806",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "80979903-530c-4c5a-83fd-1488c21371cb",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multimodal reasoning composition verifier",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Assistant

_source line 22 · 2026-05-27T23:13:48.044Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me carefully analyze all the findings from my four parallel research agents and synthesize them into a thorough review.

## Key Findings Summary

### Paper Verification
- All 10 critical papers verified to exist with correct arXiv IDs
- CoRGI (arXiv:2508.00378) has been **withdrawn** - the proposal cites a withdrawn paper
- All other papers' descriptions match their actual content
- FGRPO correctly identified as using Qwen3-VL-30B-A3B as training judge

### Missing Concurrent Work
The search found several potentially relevant missing works, but let me assess which are truly critical:


Looking at the concurrent works, DeepEyes and Embed-RL both address related visual reasoning problems, though DeepEyes focuses on re-examining image regions while Embed-RL's Traceability CoT with visual localization seems closer to the proposal's approach. TGRL is already cited in the proposal, and R-C2 appears to be another relevant work worth examining further.

Most of the remaining papers are either benchmarks like MM-CondChain and DRAGON rather than training methodologies, or they're already implicitly covered by the existing 34+ references. The proposal's landscape seems quite comprehensive, and the ICLR 2027 deadline around late September 2026 appears feasible.

Now I'm checking the practical constraints: AAAI 2027 is extremely tight at 8 weeks, CVPR 2027 timing looks reasonable, H100 spot pricing is confirmed in the expected range, and the Qwen3-VL models plus veRL framework with GRPO support are all available. The main concern is whether CFRL's tag-heavy structured output approach will suffer from the format tax problem that degrades reasoning, though the proposal's curriculum training and accuracy-first scheduling could mitigate this, and prior work like D-CoT shows tags can function as training scaffolding that gets dropped at inference.

Reward hacking is a genuine risk with structured rewards, but the proposal includes five anti-gaming safeguards and uses counterfactual validation to directly test tagged versus untagged outputs. The bigger uncertainty is whether a 4B verifier can reliably handle triple-property verification without compounding errors across all three properties—the proposal acknowledges this noise tolerance concern and has fallback plans. The faithfulness-accuracy tradeoff is well-documented in the literature, and the proposal addresses it through curriculum learning and accuracy-dominant reward weighting, which prior work like FGRPO suggests is manageable. One minor flag: CoRGI appears to be withdrawn, which affects one of the cited baselines.

Against the review checklist, the baselines are current with comprehensive coverage of 34+ papers, all references check out aside from CoRGI, and the gap is clearly articulated—no existing method unifies grounding, binding validity, and completeness in a training-time verifier. ICLR 2027 is realistic timing, though AAAI 2027 would be tight. The main feasibility risks center on format overhead (mitigated by curriculum), 4B verifier accuracy for triple-property (partially addressed through tiered separation), system complexity (managed via tiered contributions), and the accuracy-faithfulness tradeoff (explicitly handled). The novelty appears to rest on the combination of grounding plus binding validity plus completeness, with binding validity as a training reward being genuinely new. GPU costs check out at $1,250 for 950 hours.

Looking at what still needs attention: CoRGI's withdrawal should be flagged, the format tax risk deserves explicit discussion since the Format Tax paper directly challenges this approach and while curriculum helps, D-CoT's inference-time tag dropping isn't mentioned, and the 4B verifier's compounding error across three properties needs more rigorous treatment—if each property check hits 85% accuracy, the combined reliability drops significantly.

On scoring, the three-property composition verifier as a training-time reward is genuinely novel with strong binding validity components, so novelty feels like a 4/5. Feasibility is trickier—the project's ambitious with real complexity, the Tier 1/2 separation provides a reasonable fallback, but format tax and compounding errors are legitimate concerns, and the 10-week timeline for ICLR 2027 is tight, so I'd rate that 3/5.

Actually, reconsidering the feasibility score—the proposal has detailed curriculum scheduling, per-component fallbacks, a risk matrix with mitigations, and validated infrastructure already in place. The core risk concentrates in Tier 2 (completeness and domain-specific binding), which is explicitly scoped as an extension. If I'm evaluating Tier 1 alone, the grounding plus arithmetic binding is quite feasible, so maybe this pushes toward 3.5 or even higher depending on how I weight the tiered structure.

But the compounding error problem with the 4B verifier is real, and even Tier 1 involves substantial system complexity with multiple external tools. I'll settle on 3/5 for feasibility—it's achievable but carries genuine technical risk.

For clarity, the proposal is exceptionally well-structured with detailed technical specs and clear competitor differentiation, though the sheer length and complexity might overwhelm in paper form, so 4/5 feels right. Impact is strong at 4/5—if this works, it introduces a new paradigm for training-time verification and potentially solves the evidence collapse problem. That averages to 3.75, which is below the threshold I'm considering.

Actually, let me reconsider the format tax concern more carefully. The proposal directly addresses this through an accuracy-first curriculum, accuracy-dominant reward weighting, and counterfactual validation comparing tagged versus untagged outputs. It's also aware that the MuRGAt findings applied to zero-shot format imposition, not RL training where citation becomes a learned skill—so the proposal distinguishes itself from that risk profile.

On feasibility, I'm settling on 3 out of 5 to be conservative. Looking at what remains, the issues are all low to low-medium severity: the CoRGI reference withdrawal, the Format Tax paper not being explicitly cited despite the mitigations being present, compounding verifier error not being quantified for joint accuracy, and Embed-RL with T-CoT being somewhat tangential. None of these rise to critical or high severity, so the proposal seems mature enough to move forward.

Reconsidering my scoring: Novelty is 4 for the genuine combination and differentiation from competitors, Feasibility is 3 given the ambitious scope and compounding risks but with tiered fallbacks, Clarity is 4 for the detailed organization, and Impact is 4 if execution succeeds. That averages to 3.75, which is below the 4.0 threshold, but the feasibility score might be too harsh. The Tier 1 approach is self-contained and achievable, the infrastructure is verified available, GPU costs are realistic, and there's 17 weeks until ICLR—these factors suggest feasibility could reasonably be higher.

The real concerns are the lack of precedent for triple-property verification at 4B scale, system integration complexity, and compounding errors in multi-property verification, though the proposal does include thoughtful mitigations like verifier distillation and curriculum learning. I think 3 is defensible, maybe 3.5 if I'm generous. With an average of 3.75, this falls into "revise" territory—there are fixable issues, though they're becoming more granular. I need to clarify exactly what needs to be addressed.

Looking back at the scoring rubric, a 4 means "genuinely good" and a 3 means "adequate with concerns." So my final assessment is: novelty gets a 4 for the three-property unification with tiered contribution, feasibility stays at 3 due to compounding verifier error and format tax risks, clarity is a 4 for the detailed differentiation and risk analysis, and impact is a 4 if Tier 1 succeeds. That averages to 3.75, confirming the "revise" verdict.

The main issues I need to flag are the format tax risk lacking explicit treatment despite the relevant prior work, the compounding error problem in joint multi-property accuracy, CoRGI being withdrawn, and Embed-RL/T-CoT being only tangentially relevant to the approach.

Now I'm verifying the arXiv ID dates to make sure the citations are current and properly formatted. I'm noticing the arXiv dates for these papers are all from 2025, not 2026 as the proposal sometimes suggests—a minor inconsistency. Now I need to decide on the final verdict: the proposal has improved substantially over five rounds and the remaining issues are mostly low to low-medium severity, but the feasibility concerns around the 4B verifier's multi-property accuracy still prevent it from reaching the 4.0 threshold needed for a pass.

Looking at the scores again—4, 3, 4, 4 averaging 3.75—it falls short of the high bar for truly outstanding ideas. The Tier 1/Tier 2 decomposition does address feasibility concerns meaningfully, with grounding via visual QA and deterministic arithmetic verification being well-established approaches, but the format tax risk and some gaps in the literature review remain unresolved. I'll recommend "revise" with focused, actionable feedback that should be addressable in one or two more rounds.

Reconsidering the feasibility score: Tier 1 alone (grounding plus arithmetic binding) is genuinely feasible at 4/5, while the full system drops to 2.5/5, averaging around 3.25. The gap in existing work still holds—no prior paper unifies grounding, binding validity, and completeness verification across the board. I'll keep feasibility at 3 and move forward with the decision.

Now I'm identifying specific feedback issues to address. The first concern is about format tax: structured output requirements like XML/JSON tags can degrade reasoning in open-weight models, and while the proposal handles the accuracy-faithfulness tradeoff through curriculum scheduling, the format-tax mechanism is separate—it's the instructions themselves disrupting reasoning during RL rollouts. I should cite this work and argue why RL-trained citation skills overcome what affects prompted approaches. The second issue is that the compounding error problem for multi-property verification lacks quantification—if the verifier hits 85% accuracy per property, the cascading failures across multiple properties need explicit analysis. three independent property checks, the probability of all three being correct for a single response is only ~61%. The proposal discusses noise tolerance (citing "Imperfect Verifier") for individual reward signals but does not address how errors compound across the composite reward. Since the composite reward R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness combines multiple verifier-derived signals, noisy verification on any dimension could create conflicting gradients. Consider adding an explicit discussion of compound error rates and how the additive reward structure mitigates (vs. amplifies) this.

3. LOW: CoRGI (arXiv:2508.00378) has been withdrawn by its authors. Consider removing or noting this.

4. LOW: D-CoT (arXiv:2602.21786) proposes using structured control tags during training as scaffolding that can be dropped at inference time. This is a relevant approach that could strengthen CFRL's design, particularly the idea of training with structured tags but allowing tag-free inference—something not currently discussed.

These are all minor issues, so the proposal is quite close. The average score is 3.75, which falls below the 4.0 threshold for acceptance. Even if I bump feasibility up to 3.5, that only gets me to 3.875. I could theoretically reach 4.0 by adjusting the scores—novelty at 4, feasibility at 3, clarity at 5, impact at 4—but I'm not confident clarity truly warrants a 5. Given the strict threshold that only outstanding ideas should pass, I need to recommend revision.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "80979903-530c-4c5a-83fd-1488c21371cb",
  "isSidechain": false,
  "requestId": "req_011CbTvHRZpNmAvAyEF5x7Ts",
  "type": "assistant",
  "uuid": "1867eb54-bb52-450a-aa49-ae391927abbf",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPKKR3bmNMsjG1cfUXFnod",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4973,
      "cache_creation_input_tokens": 8691,
      "cache_read_input_tokens": 32856,
      "output_tokens": 5623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4973,
          "output_tokens": 5623,
          "cache_read_input_tokens": 32856,
          "cache_creation_input_tokens": 8691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8691
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

_source line 23 · 2026-05-27T23:13:48.377Z_

Now let me do some additional targeted verification on specific claims that emerged from the initial research.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1867eb54-bb52-450a-aa49-ae391927abbf",
  "isSidechain": false,
  "requestId": "req_011CbTvHRZpNmAvAyEF5x7Ts",
  "type": "assistant",
  "uuid": "4249ac73-59f0-4317-a23c-bc23bf565073",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPKKR3bmNMsjG1cfUXFnod",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4973,
      "cache_creation_input_tokens": 8691,
      "cache_read_input_tokens": 32856,
      "output_tokens": 5623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4973,
          "output_tokens": 5623,
          "cache_read_input_tokens": 32856,
          "cache_creation_input_tokens": 8691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8691
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

_source line 24 · 2026-05-27T23:13:55.052Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01N8hTGjkxqXYmhn6vnx4dFi`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Verify format tax and D-CoT papers",
  "prompt": "Search for and verify these two specific papers that are potentially relevant to a proposal requiring structured XML tags (&lt;observe>/&lt;reason>) during RL training of multimodal models:\n\n1. \"The Format Tax\" (arXiv:2604.03616) - a paper showing that structured output requirements degrade reasoning performance. Search for this exact arXiv ID and report:\n   - Does it exist?\n   - What does it specifically find about structured format (XML/JSON tags) impact on reasoning?\n   - Does it distinguish between prompted structured output vs. trained structured output?\n   - How large is the performance degradation?\n\n2. \"D-CoT\" or \"Disciplined Chain-of-Thought\" (arXiv:2602.21786) - a paper about using structured control tags during training as scaffolding. Search for this arXiv ID and report:\n   - Does it exist?\n   - What is its key insight about training with tags vs. inference with tags?\n\n3. Also search for \"Embed-RL Traceability CoT\" (arXiv:2602.13823) - reportedly introduces T-CoT with explicit visual localization in reasoning traces. Is this a direct competitor to CFRL's &lt;observe>/&lt;reason> format?\n\nReport findings concisely."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4249ac73-59f0-4317-a23c-bc23bf565073",
  "isSidechain": false,
  "requestId": "req_011CbTvHRZpNmAvAyEF5x7Ts",
  "type": "assistant",
  "uuid": "a597b7b2-5cf9-44fe-8cb6-459d8a32949d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPKKR3bmNMsjG1cfUXFnod",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4973,
      "cache_creation_input_tokens": 8691,
      "cache_read_input_tokens": 32856,
      "output_tokens": 5623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4973,
          "output_tokens": 5623,
          "cache_read_input_tokens": 32856,
          "cache_creation_input_tokens": 8691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8691
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

_source line 25 · 2026-05-27T23:14:02.053Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01TPtJtFhocnJGnFNY5NuL5Y`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Check compounding verifier error literature",
  "prompt": "I need to understand the state of research on multi-property reward models / multi-dimensional verifiers for RL training. Specifically:\n\n1. Search for \"multi-property reward model RL\" or \"composite reward signal reinforcement learning\" - are there papers studying how errors compound when multiple verifier dimensions are combined?\n\n2. Search for \"reward model accuracy threshold RLVR\" or \"imperfect verifier good enough\" (arXiv:2604.07666) - what accuracy threshold is needed for a useful reward signal? Does the paper discuss composite/multi-dimensional rewards?\n\n3. Search for \"4B parameter verifier multimodal\" or \"small verifier reward model\" - has anyone successfully used a ≤4B model as a multi-property verifier for RL training?\n\n4. Search for \"compounding error reward model\" - any theoretical or empirical analysis?\n\nReport findings concisely, focusing on whether compounding errors across 3 verification properties (each ~85% accurate) would make a composite reward signal too noisy for RL training."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a597b7b2-5cf9-44fe-8cb6-459d8a32949d",
  "isSidechain": false,
  "requestId": "req_011CbTvHRZpNmAvAyEF5x7Ts",
  "type": "assistant",
  "uuid": "877eb739-1b20-4942-b93f-b8aada8c5be7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPKKR3bmNMsjG1cfUXFnod",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 4973,
      "cache_creation_input_tokens": 8691,
      "cache_read_input_tokens": 32856,
      "output_tokens": 5623,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8691,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 4973,
          "output_tokens": 5623,
          "cache_read_input_tokens": 32856,
          "cache_creation_input_tokens": 8691,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8691
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

_source line 26_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "877eb739-1b20-4942-b93f-b8aada8c5be7",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multimodal reasoning composition verifier",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Tool result

_source line 28 · 2026-05-27T23:15:07.722Z_

<details><summary>↩ Tool result · `toolu_01N8hTGjkxqXYmhn6vnx4dFi`</summary>

```text
Here are the findings for all three papers:

---

## Paper 1: "The Format Tax" (arXiv:2604.03616)

**Exists: YES.**

**Title:** "The Format Tax"
**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick

**Key findings relevant to the proposal:**

- Structured output formats (JSON, XML, LaTeX, Markdown) substantially degrade reasoning performance in **open-weight models**. XML specifically causes a **-7 to -11 percentage point** accuracy drop across benchmarks (MATH-500, GPQA-Diamond, ZebraLogic, WritingBench).
- Critically, the paper finds that **format-requesting instructions alone cause most of the accuracy loss**, before any constrained decoding is even applied. The problem originates at the prompting level.
- **However**, most recent **closed-weight models show little to no format tax**, meaning the degradation is "not inherent to structured generation but a gap that current open-weight models have yet to close."
- The paper recommends **decoupling reasoning from formatting** (free-form generation then reformat, or extended thinking within a single generation) to recover accuracy.

**Important limitation for your proposal:** This paper studies only **inference-time prompting** effects. It does **not** study RL training with structured formats. So it cannot be directly cited as evidence that training with `&lt;observe>`/`&lt;reason>` tags will degrade performance -- it only shows that prompting for structured output at inference time hurts open-weight models. A model trained via RL to use these tags natively may behave differently (more like the closed-weight models that show no tax).

---

## Paper 2: "D-CoT" / "Disciplined Chain-of-Thought" (arXiv:2602.21786)

**Exists: YES.**

**Title:** "D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models"
**Author:** Shunsuke Ubukata

**Key insight:** The paper uses structured control tags (e.g., `&lt;TEMP_LOW>` for fact-checking, `&lt;TEMP_HIGH>` for multi-perspective reasoning) as **training scaffolding**. The crucial finding is that **the model internalizes the disciplined thought structure, maintaining high performance even without explicit control tags during inference**. Results on Qwen3-8B with only 5,000 training samples show +9.9% on GPQA-diamond and +9.1% on MMLU-Pro.

**Relevance to the proposal:** This is actually a **supporting** paper for using structured tags during RL training. It demonstrates that training with tags can improve reasoning quality and that the structure gets internalized -- tags can potentially be dropped at inference time without losing the benefit. This partially counteracts the Format Tax concern: if the model is *trained* with tags rather than merely *prompted* with them, the cost may be negligible or even beneficial.

---

## Paper 3: "Embed-RL" / T-CoT (arXiv:2602.13823)

**Exists: YES, but it is not exactly what was described.**

**Title:** "Embed-RL: Reinforcement Learning for Reasoning-Driven Multimodal Embeddings"
**Authors:** Haonan Jiang, Yuji Wang, Yongjie Zhu, Xin Lu, Wenyu Qin, Meng Wang, Pengfei Wan, Yansong Tang

**What it actually does:** It introduces T-CoT (Traceability CoT) for multimodal *embedding* tasks (retrieval), not general multimodal reasoning. The T-CoT uses XML-style tags (`&lt;thinking>`, `&lt;rethink>`, `&lt;answer>`) with embedded visual localization via bounding boxes (`bbox_2d` with normalized coordinates) and video keyframes. The structured evidence is output as JSON within the thinking tags.

**Is it a direct competitor to CFRL's `&lt;observe>`/`&lt;reason>` format?** Not really. It serves a fundamentally different purpose:
- **Embed-RL/T-CoT** targets multimodal *retrieval/embedding* quality, integrating visual grounding *within* reasoning chains as JSON annotations.
- **CFRL's `&lt;observe>`/`&lt;reason>`** targets multimodal *reasoning* with a sequential observe-then-reason paradigm.
- The paradigms are structurally different: T-CoT embeds multimodal cues inline within a reasoning chain, whereas `&lt;observe>`/`&lt;reason>` alternates between perception and reasoning phases.

That said, T-CoT does demonstrate that **RL training with structured, visually-grounded reasoning traces is viable and beneficial** in a multimodal setting, which is conceptually supportive of the CFRL approach.

---

## Summary for the proposal

- **The Format Tax** is real but applies to **inference-time prompting of open-weight models**, not to RL-trained structured output. Cite it as a risk to acknowledge, but note it does not directly apply to trained formats.
- **D-CoT** is actually evidence **in favor** of training with structured tags -- it shows tags can be internalized and even dropped at inference time.
- **Embed-RL/T-CoT** is a related but non-competing approach in a different task domain (embeddings/retrieval vs. reasoning). It validates that RL + structured multimodal traces work, but it is not a direct competitor to `&lt;observe>`/`&lt;reason>`.

agentId: a91d929257c32b950 (use SendMessage with to: 'a91d929257c32b950' to continue this agent)
&lt;usage>total_tokens: 14135
tool_uses: 6
duration_ms: 72665&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a597b7b2-5cf9-44fe-8cb6-459d8a32949d",
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "d3177ee0-17ee-4a68-9ab6-33db2a8ab691",
  "toolUseResult": {
    "status": "completed",
    "prompt": "Search for and verify these two specific papers that are potentially relevant to a proposal requiring structured XML tags (&lt;observe>/&lt;reason>) during RL training of multimodal models:\n\n1. \"The Format Tax\" (arXiv:2604.03616) - a paper showing that structured output requirements degrade reasoning performance. Search for this exact arXiv ID and report:\n   - Does it exist?\n   - What does it specifically find about structured format (XML/JSON tags) impact on reasoning?\n   - Does it distinguish between prompted structured output vs. trained structured output?\n   - How large is the performance degradation?\n\n2. \"D-CoT\" or \"Disciplined Chain-of-Thought\" (arXiv:2602.21786) - a paper about using structured control tags during training as scaffolding. Search for this arXiv ID and report:\n   - Does it exist?\n   - What is its key insight about training with tags vs. inference with tags?\n\n3. Also search for \"Embed-RL Traceability CoT\" (arXiv:2602.13823) - reportedly introduces T-CoT with explicit visual localization in reasoning traces. Is this a direct competitor to CFRL's &lt;observe>/&lt;reason> format?\n\nReport findings concisely.",
    "agentId": "a91d929257c32b950",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here are the findings for all three papers:\n\n---\n\n## Paper 1: \"The Format Tax\" (arXiv:2604.03616)\n\n**Exists: YES.**\n\n**Title:** \"The Format Tax\"\n**Authors:** Ivan Yee Lee, Loris D'Antoni, Taylor Berg-Kirkpatrick\n\n**Key findings relevant to the proposal:**\n\n- Structured output formats (JSON, XML, LaTeX, Markdown) substantially degrade reasoning performance in **open-weight models**. XML specifically causes a **-7 to -11 percentage point** accuracy drop across benchmarks (MATH-500, GPQA-Diamond, ZebraLogic, WritingBench).\n- Critically, the paper finds that **format-requesting instructions alone cause most of the accuracy loss**, before any constrained decoding is even applied. The problem originates at the prompting level.\n- **However**, most recent **closed-weight models show little to no format tax**, meaning the degradation is \"not inherent to structured generation but a gap that current open-weight models have yet to close.\"\n- The paper recommends **decoupling reasoning from formatting** (free-form generation then reformat, or extended thinking within a single generation) to recover accuracy.\n\n**Important limitation for your proposal:** This paper studies only **inference-time prompting** effects. It does **not** study RL training with structured formats. So it cannot be directly cited as evidence that training with `&lt;observe>`/`&lt;reason>` tags will degrade performance -- it only shows that prompting for structured output at inference time hurts open-weight models. A model trained via RL to use these tags natively may behave differently (more like the closed-weight models that show no tax).\n\n---\n\n## Paper 2: \"D-CoT\" / \"Disciplined Chain-of-Thought\" (arXiv:2602.21786)\n\n**Exists: YES.**\n\n**Title:** \"D-COT: Disciplined Chain-of-Thought Learning for Efficient Reasoning in Small Language Models\"\n**Author:** Shunsuke Ubukata\n\n**Key insight:** The paper uses structured control tags (e.g., `&lt;TEMP_LOW>` for fact-checking, `&lt;TEMP_HIGH>` for multi-perspective reasoning) as **training scaffolding**. The crucial finding is that **the model internalizes the disciplined thought structure, maintaining high performance even without explicit control tags during inference**. Results on Qwen3-8B with only 5,000 training samples show +9.9% on GPQA-diamond and +9.1% on MMLU-Pro.\n\n**Relevance to the proposal:** This is actually a **supporting** paper for using structured tags during RL training. It demonstrates that training with tags can improve reasoning quality and that the structure gets internalized -- tags can potentially be dropped at inference time without losing the benefit. This partially counteracts the Format Tax concern: if the model is *trained* with tags rather than merely *prompted* with them, the cost may be negligible or even beneficial.\n\n---\n\n## Paper 3: \"Embed-RL\" / T-CoT (arXiv:2602.13823)\n\n**Exists: YES, but it is not exactly what was described.**\n\n**Title:** \"Embed-RL: Reinforcement Learning for Reasoning-Driven Multimodal Embeddings\"\n**Authors:** Haonan Jiang, Yuji Wang, Yongjie Zhu, Xin Lu, Wenyu Qin, Meng Wang, Pengfei Wan, Yansong Tang\n\n**What it actually does:** It introduces T-CoT (Traceability CoT) for multimodal *embedding* tasks (retrieval), not general multimodal reasoning. The T-CoT uses XML-style tags (`&lt;thinking>`, `&lt;rethink>`, `&lt;answer>`) with embedded visual localization via bounding boxes (`bbox_2d` with normalized coordinates) and video keyframes. The structured evidence is output as JSON within the thinking tags.\n\n**Is it a direct competitor to CFRL's `&lt;observe>`/`&lt;reason>` format?** Not really. It serves a fundamentally different purpose:\n- **Embed-RL/T-CoT** targets multimodal *retrieval/embedding* quality, integrating visual grounding *within* reasoning chains as JSON annotations.\n- **CFRL's `&lt;observe>`/`&lt;reason>`** targets multimodal *reasoning* with a sequential observe-then-reason paradigm.\n- The paradigms are structurally different: T-CoT embeds multimodal cues inline within a reasoning chain, whereas `&lt;observe>`/`&lt;reason>` alternates between perception and reasoning phases.\n\nThat said, T-CoT does demonstrate that **RL training with structured, visually-grounded reasoning traces is viable and beneficial** in a multimodal setting, which is conceptually supportive of the CFRL approach.\n\n---\n\n## Summary for the proposal\n\n- **The Format Tax** is real but applies to **inference-time prompting of open-weight models**, not to RL-trained structured output. Cite it as a risk to acknowledge, but note it does not directly apply to trained formats.\n- **D-CoT** is actually evidence **in favor** of training with structured tags -- it shows tags can be internalized and even dropped at inference time.\n- **Embed-RL/T-CoT** is a related but non-competing approach in a different task domain (embeddings/retrieval vs. reasoning). It validates that RL + structured multimodal traces work, but it is not a direct competitor to `&lt;observe>`/`&lt;reason>`."
      }
    ],
    "totalDurationMs": 72665,
    "totalTokens": 14135,
    "totalToolUseCount": 6,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1138,
      "cache_read_input_tokens": 11697,
      "output_tokens": 1299,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1138
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1299,
          "cache_read_input_tokens": 11697,
          "cache_creation_input_tokens": 1138,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1138,
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
  "sourceToolAssistantUUID": "a597b7b2-5cf9-44fe-8cb6-459d8a32949d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-27T23:15:44.053Z_

<details><summary>↩ Tool result · `toolu_01TPtJtFhocnJGnFNY5NuL5Y`</summary>

```text
Here is my synthesis of the research findings across all four questions.

---

## 1. Multi-Property Reward Models and Compounding Errors

There is no single paper that directly studies how errors compound when you multiply three ~85%-accurate verifier dimensions together. However, several closely related lines of work exist:

**Composite Reward Functions (arXiv:2509.15557):** Tarek & Beheshti (ACM-BCB 2025) introduced composite reward functions for RLVR that combine a correctness signal with penalty terms for format violations and reward hacking behaviors (e.g., skipping reasoning steps). They showed this multi-aspect reward outperforms a single binary reward. However, their "composite" is an additive penalty structure, not a product of independent verifiers.

**DG-PRM (arXiv:2507.17849):** The Dynamic and Generalizable Process Reward Model constructs a "reward tree" representing multi-dimensional criteria and uses Pareto dominance to select discriminative signal pairs. This is the closest work to a multi-property verifier framework, but it operates at the process (step-level) supervision granularity rather than as an outcome-level multi-property classifier. It avoids the compounding problem by treating dimensions as Pareto-optimal objectives rather than multiplying them.

**Key gap:** No paper was found that directly analyzes the multiplicative compounding of independent verifier errors (e.g., 0.85^3 = 0.614 joint accuracy). The field has largely treated multi-dimensional rewards either additively (weighted sums) or via Pareto methods, which sidestep the compounding issue.

---

## 2. Accuracy Threshold for Useful Reward Signals (arXiv:2604.07666)

**Paper:** "An Imperfect Verifier is Good Enough: Learning with Noisy Rewards" (Plesner, Guzman, Athalye -- Handshake AI / ETH Zurich, April 2026).

**Key findings:**
- A verifier with ~85% accuracy and high precision recovers most of the ground-truth training signal.
- Up to 15% noise yields validation accuracy within 2 percentage points of a clean (perfect verifier) baseline.
- Results are consistent across Qwen3, GLM4, and Llama 3.1, and across model sizes from 4B to 9B.
- Practical recommendation: prioritize moderate accuracy with high precision over perfect verification.

**Does it discuss composite/multi-dimensional rewards?** No. The paper studies a single binary verifier (correct/incorrect) with injected noise. It does not analyze what happens when multiple verification properties are combined. This is a significant gap relative to your question.

---

## 3. Small (<=4B) Models as Multi-Property Verifiers

The arXiv:2604.07666 paper tested RLVR with model sizes including 4B (Qwen3-4B). However, the 4B models were the *policy* models being trained, not the verifiers themselves.

**Argos (arXiv:2512.03438):** "Multimodal Reinforcement Learning with Agentic Verifier" introduces an agentic verifier for multimodal RL that selects among multiple scoring functions (teacher-model-derived and rule-based) to evaluate accuracy, spatiotemporal localization, and reasoning quality. This is a multi-property verifier, but the paper does not specifically constrain the verifier to <=4B parameters.

**MSRL (arXiv:2603.25108):** Multi-Stage RL for multimodal reward models learns reward reasoning from text data, then transfers to multimodal tasks. No specific <=4B verifier results were found.

**Bottom line:** No paper was found demonstrating a <=4B model successfully serving as a multi-property verifier for RL training. The trend is toward using larger teacher models or rule-based/hybrid verifiers.

---

## 4. Compounding Error Analysis

**RLV-epsilon-R (arXiv:2601.04411):** This paper provides the most rigorous theoretical treatment. It models the verifier as a stochastic reward channel with asymmetric noise (FP rate, FN rate) and derives a sharp phase transition governed by Youden's index J = TPR - FPR:
- J > 0: learning succeeds (noise only slows convergence -- "rate, not fate")
- J = 0: neutral
- J < 0: anti-learning / collapse

**PGBC/PGFC corrections (arXiv:2510.00915):** Two correction methods can recover clean-gradient performance from noisy verifiers: backward correction (unbiased estimator, requires both FP and FN rates) and forward correction (reweights gradient terms, requires only FN rate). Both recover most of the gap to oracle performance.

**No multiplicative compounding analysis:** None of these papers model the case where the reward is the conjunction of N independent verifier outputs. The noise analyses assume a single noisy binary signal.

---

## Direct Answer to Your Core Question

**Will three ~85%-accurate verification properties make the composite signal too noisy?**

This depends critically on how you combine them:

**Worst case (naive conjunction/product):** If you require all three to say "correct" and they are independently noisy, joint accuracy on true positives drops to roughly 0.85^3 = 61.4%. This pushes you well beyond the 15% noise tolerance identified by Plesner et al. -- the effective noise rate would be ~39%, likely degrading training substantially.

**Better approach (additive/weighted combination):** If you sum or average the three signals (e.g., reward = w1*v1 + w2*v2 + w3*v3), errors partially cancel rather than compound. With independent ~15% error per dimension, the combined signal's noise shrinks (by roughly 1/sqrt(3)) rather than growing. This keeps you within the tolerable noise regime.

**Best approach (Pareto/multi-objective):** Following DG-PRM's approach, treat each verification dimension as a separate objective and use Pareto dominance or multi-objective optimization. This avoids compounding entirely.

**Practical recommendation:** Do not use a multiplicative/conjunctive combination of your three verifiers. Use either (a) an additive weighted reward with the three scores, or (b) a curriculum where you start with the most reliable property and add dimensions as training stabilizes. The literature strongly suggests that ~85% per-dimension accuracy is workable if the combination method is additive rather than multiplicative.

---

Sources:
- [An Imperfect Verifier is Good Enough (arXiv:2604.07666)](https://arxiv.org/abs/2604.07666)
- [Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557)](https://arxiv.org/abs/2509.15557)
- [Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers (arXiv:2510.00915)](https://arxiv.org/abs/2510.00915)
- [Rate or Fate? RLV-epsilon-R (arXiv:2601.04411)](https://arxiv.org/abs/2601.04411)
- [Dynamic and Generalizable Process Reward Modeling / DG-PRM (arXiv:2507.17849)](https://arxiv.org/abs/2507.17849)
- [Multimodal RL with Agentic Verifier / Argos (arXiv:2512.03438)](https://arxiv.org/abs/2512.03438)
- [MSRL: Scaling Generative Multimodal Reward Modeling (arXiv:2603.25108)](https://arxiv.org/pdf/2603.25108)
- [Multi-Reward Reinforcement Learning (EmergentMind)](https://www.emergentmind.com/topics/multi-reward-reinforcement-learning-rl)
- [Awesome-RLVR curated list (GitHub)](https://github.com/opendilab/awesome-RLVR)

agentId: aaa15d911c3e0edc4 (use SendMessage with to: 'aaa15d911c3e0edc4' to continue this agent)
&lt;usage>total_tokens: 19320
tool_uses: 10
duration_ms: 101995&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "877eb739-1b20-4942-b93f-b8aada8c5be7",
  "isSidechain": false,
  "promptId": "12b7e1b3-4535-4519-8741-c173944ce9f5",
  "type": "user",
  "uuid": "6e267b1a-23ee-4cd0-91e1-1c87b8056d24",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to understand the state of research on multi-property reward models / multi-dimensional verifiers for RL training. Specifically:\n\n1. Search for \"multi-property reward model RL\" or \"composite reward signal reinforcement learning\" - are there papers studying how errors compound when multiple verifier dimensions are combined?\n\n2. Search for \"reward model accuracy threshold RLVR\" or \"imperfect verifier good enough\" (arXiv:2604.07666) - what accuracy threshold is needed for a useful reward signal? Does the paper discuss composite/multi-dimensional rewards?\n\n3. Search for \"4B parameter verifier multimodal\" or \"small verifier reward model\" - has anyone successfully used a ≤4B model as a multi-property verifier for RL training?\n\n4. Search for \"compounding error reward model\" - any theoretical or empirical analysis?\n\nReport findings concisely, focusing on whether compounding errors across 3 verification properties (each ~85% accurate) would make a composite reward signal too noisy for RL training.",
    "agentId": "aaa15d911c3e0edc4",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Here is my synthesis of the research findings across all four questions.\n\n---\n\n## 1. Multi-Property Reward Models and Compounding Errors\n\nThere is no single paper that directly studies how errors compound when you multiply three ~85%-accurate verifier dimensions together. However, several closely related lines of work exist:\n\n**Composite Reward Functions (arXiv:2509.15557):** Tarek & Beheshti (ACM-BCB 2025) introduced composite reward functions for RLVR that combine a correctness signal with penalty terms for format violations and reward hacking behaviors (e.g., skipping reasoning steps). They showed this multi-aspect reward outperforms a single binary reward. However, their \"composite\" is an additive penalty structure, not a product of independent verifiers.\n\n**DG-PRM (arXiv:2507.17849):** The Dynamic and Generalizable Process Reward Model constructs a \"reward tree\" representing multi-dimensional criteria and uses Pareto dominance to select discriminative signal pairs. This is the closest work to a multi-property verifier framework, but it operates at the process (step-level) supervision granularity rather than as an outcome-level multi-property classifier. It avoids the compounding problem by treating dimensions as Pareto-optimal objectives rather than multiplying them.\n\n**Key gap:** No paper was found that directly analyzes the multiplicative compounding of independent verifier errors (e.g., 0.85^3 = 0.614 joint accuracy). The field has largely treated multi-dimensional rewards either additively (weighted sums) or via Pareto methods, which sidestep the compounding issue.\n\n---\n\n## 2. Accuracy Threshold for Useful Reward Signals (arXiv:2604.07666)\n\n**Paper:** \"An Imperfect Verifier is Good Enough: Learning with Noisy Rewards\" (Plesner, Guzman, Athalye -- Handshake AI / ETH Zurich, April 2026).\n\n**Key findings:**\n- A verifier with ~85% accuracy and high precision recovers most of the ground-truth training signal.\n- Up to 15% noise yields validation accuracy within 2 percentage points of a clean (perfect verifier) baseline.\n- Results are consistent across Qwen3, GLM4, and Llama 3.1, and across model sizes from 4B to 9B.\n- Practical recommendation: prioritize moderate accuracy with high precision over perfect verification.\n\n**Does it discuss composite/multi-dimensional rewards?** No. The paper studies a single binary verifier (correct/incorrect) with injected noise. It does not analyze what happens when multiple verification properties are combined. This is a significant gap relative to your question.\n\n---\n\n## 3. Small (<=4B) Models as Multi-Property Verifiers\n\nThe arXiv:2604.07666 paper tested RLVR with model sizes including 4B (Qwen3-4B). However, the 4B models were the *policy* models being trained, not the verifiers themselves.\n\n**Argos (arXiv:2512.03438):** \"Multimodal Reinforcement Learning with Agentic Verifier\" introduces an agentic verifier for multimodal RL that selects among multiple scoring functions (teacher-model-derived and rule-based) to evaluate accuracy, spatiotemporal localization, and reasoning quality. This is a multi-property verifier, but the paper does not specifically constrain the verifier to <=4B parameters.\n\n**MSRL (arXiv:2603.25108):** Multi-Stage RL for multimodal reward models learns reward reasoning from text data, then transfers to multimodal tasks. No specific <=4B verifier results were found.\n\n**Bottom line:** No paper was found demonstrating a <=4B model successfully serving as a multi-property verifier for RL training. The trend is toward using larger teacher models or rule-based/hybrid verifiers.\n\n---\n\n## 4. Compounding Error Analysis\n\n**RLV-epsilon-R (arXiv:2601.04411):** This paper provides the most rigorous theoretical treatment. It models the verifier as a stochastic reward channel with asymmetric noise (FP rate, FN rate) and derives a sharp phase transition governed by Youden's index J = TPR - FPR:\n- J > 0: learning succeeds (noise only slows convergence -- \"rate, not fate\")\n- J = 0: neutral\n- J < 0: anti-learning / collapse\n\n**PGBC/PGFC corrections (arXiv:2510.00915):** Two correction methods can recover clean-gradient performance from noisy verifiers: backward correction (unbiased estimator, requires both FP and FN rates) and forward correction (reweights gradient terms, requires only FN rate). Both recover most of the gap to oracle performance.\n\n**No multiplicative compounding analysis:** None of these papers model the case where the reward is the conjunction of N independent verifier outputs. The noise analyses assume a single noisy binary signal.\n\n---\n\n## Direct Answer to Your Core Question\n\n**Will three ~85%-accurate verification properties make the composite signal too noisy?**\n\nThis depends critically on how you combine them:\n\n**Worst case (naive conjunction/product):** If you require all three to say \"correct\" and they are independently noisy, joint accuracy on true positives drops to roughly 0.85^3 = 61.4%. This pushes you well beyond the 15% noise tolerance identified by Plesner et al. -- the effective noise rate would be ~39%, likely degrading training substantially.\n\n**Better approach (additive/weighted combination):** If you sum or average the three signals (e.g., reward = w1*v1 + w2*v2 + w3*v3), errors partially cancel rather than compound. With independent ~15% error per dimension, the combined signal's noise shrinks (by roughly 1/sqrt(3)) rather than growing. This keeps you within the tolerable noise regime.\n\n**Best approach (Pareto/multi-objective):** Following DG-PRM's approach, treat each verification dimension as a separate objective and use Pareto dominance or multi-objective optimization. This avoids compounding entirely.\n\n**Practical recommendation:** Do not use a multiplicative/conjunctive combination of your three verifiers. Use either (a) an additive weighted reward with the three scores, or (b) a curriculum where you start with the most reliable property and add dimensions as training stabilizes. The literature strongly suggests that ~85% per-dimension accuracy is workable if the combination method is additive rather than multiplicative.\n\n---\n\nSources:\n- [An Imperfect Verifier is Good Enough (arXiv:2604.07666)](https://arxiv.org/abs/2604.07666)\n- [Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557)](https://arxiv.org/abs/2509.15557)\n- [Reinforcement Learning with Verifiable yet Noisy Rewards under Imperfect Verifiers (arXiv:2510.00915)](https://arxiv.org/abs/2510.00915)\n- [Rate or Fate? RLV-epsilon-R (arXiv:2601.04411)](https://arxiv.org/abs/2601.04411)\n- [Dynamic and Generalizable Process Reward Modeling / DG-PRM (arXiv:2507.17849)](https://arxiv.org/abs/2507.17849)\n- [Multimodal RL with Agentic Verifier / Argos (arXiv:2512.03438)](https://arxiv.org/abs/2512.03438)\n- [MSRL: Scaling Generative Multimodal Reward Modeling (arXiv:2603.25108)](https://arxiv.org/pdf/2603.25108)\n- [Multi-Reward Reinforcement Learning (EmergentMind)](https://www.emergentmind.com/topics/multi-reward-reinforcement-learning-rl)\n- [Awesome-RLVR curated list (GitHub)](https://github.com/opendilab/awesome-RLVR)"
      }
    ],
    "totalDurationMs": 101995,
    "totalTokens": 19320,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2025,
      "cache_read_input_tokens": 15361,
      "output_tokens": 1933,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2025
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 1933,
          "cache_read_input_tokens": 15361,
          "cache_creation_input_tokens": 2025,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2025,
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
  "sourceToolAssistantUUID": "877eb739-1b20-4942-b93f-b8aada8c5be7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-27T23:16:30.896Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have comprehensive information to write my final review. Let me synthesize all findings:

## Summary of All Research Findings

### Paper Verification
- All 10 critical papers verified to exist with correct arXiv IDs ✓
- CoRGI (arXiv:2508.00378) has been **withdrawn** by authors
- All other papers' descriptions match actual content ✓

### Missing Concurrent Work Assessment
The search found many papers, but the proposal already covers 34+ papers. The most relevant additions would be:
- DeepEyes (ICLR 2026) - active visual re-examination during reasoning via RL


- Embed-RL/T-CoT and MM-CondChain for visual localization and verification benchmarking
- DRAGON for evidence-grounded visual reasoning

None of these fundamentally challenge the gap claim though—the landscape is already exceptionally comprehensive.

### Format Tax Assessment
- "The Format Tax" paper exists and shows 7-11pp degradation from structured formats in open-weight models, but this applies to inference-time prompting rather than RL training
- D-CoT demonstrates that training with tags can be beneficial and tags can be dropped at inference
- The proposal's curriculum approach partially mitigates this concern

### Compounding Error Assessment
No paper directly studies multiplicative compounding of independent verifier errors—the "Imperfect Verifier" paper only examines single binary verifiers. However, CFRL's additive reward combination actually mitigates this concern since errors partially cancel rather than compound multiplicatively. With additive combination, noise shrinks by roughly 1/√3 rather than growing, and the weighted reward structure keeps noise within tolerable range. This is actually a strength of the proposal rather than a weakness, so I should reconsider my feasibility assessment upward.

The format tax concern is also less problematic than I initially thought—it's a training-time issue rather than inference-time, and D-CoT research supports this training-with-tags approach. Revising my scores: novelty stays at 4 for the genuinely novel three-property composition verifier, feasibility improves to 4 given the additive reward mitigation, additive reward structure, available infrastructure, and tier 1/2 decomposition fallback (though the 4B model for multi-property verification remains unproven), clarity is 4 for the exceptional detail, and impact is 4 for the meaningful contribution potential. That gives me an average of 4.0 overall.

Now I'm second-guessing whether I'm being too generous on feasibility. The core risk is that no prior work has shown a ≤4B model can reliably serve as a multi-property verifier for RL training, but the proposal does have explicit fallback strategies, planned noise tolerance ablations, a verifier validation protocol with held-out precision/recall metrics, tier 1/2 separation for a defensible contribution even if tier 2 fails, and the additive reward structure helps contain error propagation. Tier 1 alone is feasible and publishable, all the infrastructure checks out, so I think 3.5 is the honest score—rounding to 4 feels right given these mitigations.

Actually, the format tax concern is less critical for training than inference, so I'll settle on feasibility 3 to stay conservative. The unproven 4B verifier is still a real gap, and even Tier 1 requires distilling from a 235B teacher, which adds system complexity. That gives me final scores of 4, 3, 4, 4 averaging to 3.75, so I should revise. The remaining issues are minor: I need to explicitly argue why the additive reward structure actually prevents compounding errors rather than just hoping it does, cite the Format Tax paper and distinguish between prompted versus trained structured output, remove CoRGI as a reference, and use D-CoT as supporting evidence for tag-based training.

Now I'm second-guessing the feasibility score. The 3.75 average technically falls below the 4.0 threshold, but I'm wondering if I'm being too harsh on the 4B verifier. MJ1 already demonstrated a 3B judge achieving 77% on MMRB2, which actually exceeds GPT-5 performance on a multi-stage verification chain—that's pretty compelling evidence the approach is viable.

Weighing it out: the proposal has built-in fallbacks with its Tier 1/2 structure, additive rewards prevent error compounding, and they're planning ablations for noise tolerance. But the counterarguments are solid too—MJ1 was designed for evaluation, not training-time rewards, and there's no exact precedent for this specific task at this scale. The architectural differences between a 3.3B MoE and a 4B dense model matter, and the system integration complexity is genuinely high.

I'm settling on feasibility 3. The concerns are substantial enough that I should stick with revise and provide focused feedback rather than accept.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6e267b1a-23ee-4cd0-91e1-1c87b8056d24",
  "isSidechain": false,
  "requestId": "req_011CbTvaymYbLhR1HVfBRgns",
  "type": "assistant",
  "uuid": "aa0c85a5-7d03-4f48-be1b-ddc8a4df7263",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5AxwwtQG1szSb3QFMHAPm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14030,
      "cache_read_input_tokens": 41547,
      "output_tokens": 3413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3413,
          "cache_read_input_tokens": 41547,
          "cache_creation_input_tokens": 14030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14030
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

_source line 31 · 2026-05-27T23:17:13.561Z_

Now I have comprehensive evidence across all dimensions. Let me synthesize my findings into a thorough review.

## Key Findings from Independent Verification

**Paper verification:** All 10 critical papers verified to exist with correct arXiv IDs and matching descriptions. One issue: **CoRGI (arXiv:2508.00378) has been withdrawn** by its authors.

**Missing concurrent work:** The landscape (34+ papers) is extremely comprehensive. Some additional works exist (DeepEyes/ICLR 2026, Embed-RL/T-CoT, MM-CondChain, DRAGON benchmark) but none fundamentally challenge the gap claim. The proposal already covers the most relevant work.

**Format tax risk:** "The Format Tax" (arXiv:2604.03616) shows 7-11pp degradation from XML/JSON tags in open-weight models — but this applies to *inference-time prompting*, not RL training. D-CoT (arXiv:2602.21786) actually *supports* CFRL's approach, showing trained tags get internalized and can be dropped at inference (+9.9% GPQA-diamond).

**Compounding verifier error:** Research confirms that CFRL's *additive* reward structure (R = α·R_accuracy + β·R_grounding + ...) mitigates compounding — errors partially cancel (~1/√N) rather than multiply (~P^N). If the reward were multiplicative (requiring all three checks to pass), joint accuracy would drop to ~61% at 85% per-property. But with additive combination, the noise regime stays tolerable per "Imperfect Verifier" findings.

**Infrastructure verified:** Qwen3-VL-8B and 235B-A22B confirmed available on HuggingFace. veRL confirmed supporting GRPO. H100 spot at $1.03-$1.60/hr confirmed. AAAI 2027 deadlines confirmed (Jul 21/28). ICLR 2027 ~Sep 2026 plausible.

```json
{
  "verdict": "revise",
  "scores": {
    "novelty": {"score": 4, "rationale": "The three-property composition verifier (grounding + binding validity + completeness) as a unified training-time reward is genuinely novel. Well-differentiated from 15+ competitors across 7 landscape axes. The tiered contribution structure (Tier 1: arithmetic/geometric binding; Tier 2: domain-specific completeness) is a smart scoping decision. No existing method unifies all three properties."},
    "feasibility": {"score": 3, "rationale": "Tier 1 (grounding + arithmetic binding) is feasible with verified infrastructure. However, no paper has demonstrated a ≤4B model performing multi-property semantic verification for RL training rewards — MJ1's 3B judge is evaluation-time only. The additive reward structure mitigates compounding errors, and curriculum scheduling reduces risk, but the 4B verifier's triple-property accuracy remains an unproven assumption. System complexity is high even for Tier 1 (verifier distillation from 235B teacher + symbolic checker + GRPO training)."},
    "clarity": {"score": 4, "rationale": "Exceptionally detailed technical specification: concrete binding validity algorithms for all domains, precise cost model with honest 5-8x comparison, structured risk matrix with per-component fallbacks, and thorough differentiation from each competitor. The Tier 1/2 decomposition clearly communicates what is core vs. extension."},
    "impact": {"score": 4, "rationale": "If Tier 1 works, it introduces a new paradigm for verifiable multimodal reasoning training. Evidence-grounded binding validity as a training reward addresses a genuine gap identified by multiple diagnostic papers (Don't Blink, MathLens, PAR). The 5-8x cost reduction over FGRPO's per-sentence judges is meaningful for practical adoption. The explicit citation format enables auditable reasoning chains."}
  },
  "issues": [
    "LOW-MEDIUM: The proposal does not discuss the 'Format Tax' (arXiv:2604.03616, Apr 2026), which shows 7-11pp reasoning degradation from structured XML/JSON output in open-weight models. While this paper studies inference-time prompting (not RL training), it is a directly relevant risk that should be cited and distinguished. D-CoT (arXiv:2602.21786) provides counter-evidence showing trained tags get internalized — this supporting work should also be cited.",
    "LOW-MEDIUM: The additive reward structure (R = α·R_accuracy + β·R_grounding + γ·R_binding + δ·R_completeness) is actually a strength for noise tolerance — with additive combination, per-property errors partially cancel (~1/√N reduction) rather than compound multiplicatively. But this is not explicitly argued. The proposal discusses noise tolerance for individual signals (citing 'Imperfect Verifier') but does not explain why the additive structure prevents the compounding error problem that would plague a multiplicative/conjunctive combination. Making this argument explicit would strengthen the feasibility case.",
    "LOW: CoRGI (arXiv:2508.00378) has been withdrawn by its authors. The proposal should either remove this reference or note its withdrawal status. This is a minor issue since CoRGI is positioned as a tangential work (inference-only) and its removal does not affect the gap analysis.",
    "LOW: No precedent exists for a ≤4B model performing multi-property semantic verification (grounding + binding + completeness) in a single autoregressive pass for RL training. MJ1 demonstrates 5-stage verification at 3B active parameters, but for evaluation-time judging with ~6144 output tokens — not as a training-time reward with throughput constraints. The proposal should acknowledge this gap more explicitly and discuss what minimum per-property accuracy would make the Tier 1 verifier useful (the 75% fallback threshold for binding is specified, but grounding and completeness thresholds are not)."
  ],
  "feedback": "The proposal is approaching pass quality after five rounds of substantial improvement. Three focused changes would likely reach the threshold:\n\n1. **Cite the Format Tax and D-CoT**: Add a brief paragraph acknowledging that 'The Format Tax' (arXiv:2604.03616) documents 7-11pp degradation from structured output in *prompted* open-weight models, but explicitly distinguish this from CFRL's RL-trained format: (a) D-CoT (arXiv:2602.21786) shows that models trained with structured tags internalize the structure and maintain performance even when tags are dropped at inference (+9.9% GPQA-diamond), (b) CFRL's curriculum develops citation as a learned skill via reward optimization, unlike MuRGAt's zero-shot format imposition where the degradation was observed. This turns a potential objection into a strength.\n\n2. **Explicitly argue the additive reward advantage**: Add 1-2 sentences noting that the additive reward combination (weighted sum of independent verifier signals) is specifically chosen to avoid multiplicative error compounding. With additive combination and independent ~15% error per property, the noise in the composite signal shrinks rather than grows, keeping the training within the 'Imperfect Verifier' tolerance regime. This directly addresses the compounding error concern.\n\n3. **Fix minor reference issues**: Note CoRGI's withdrawal. Specify minimum accuracy thresholds for grounding and completeness verification (currently only binding has a 75% fallback threshold).",
  "reason": "Very strong proposal after 5 revision rounds — novel gap, comprehensive landscape (34+ papers), honest cost model, and well-designed tiered contribution. Falls just below threshold due to unproven 4B multi-property verifier feasibility and two easily addressable literature gaps (Format Tax, additive reward advantage)."
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa0c85a5-7d03-4f48-be1b-ddc8a4df7263",
  "isSidechain": false,
  "requestId": "req_011CbTvaymYbLhR1HVfBRgns",
  "type": "assistant",
  "uuid": "de534872-37d0-42f8-8029-b4f496a43087",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F5AxwwtQG1szSb3QFMHAPm",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14030,
      "cache_read_input_tokens": 41547,
      "output_tokens": 3413,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14030,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 3413,
          "cache_read_input_tokens": 41547,
          "cache_creation_input_tokens": 14030,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14030
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "de534872-37d0-42f8-8029-b4f496a43087",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multimodal reasoning composition verifier",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are a strict ML research reviewer conducting adversarial review.  **Today's date: 2026-05-27 (UTC).**  Your job: independently verify this idea's claims via web_search, then issue a verdict.  ## U…",
  "leafUuid": "de534872-37d0-42f8-8029-b4f496a43087",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Review multimodal reasoning composition verifier",
  "sessionId": "4f811c70-5276-4df8-92eb-dea6c34b39ff"
}
```

---
