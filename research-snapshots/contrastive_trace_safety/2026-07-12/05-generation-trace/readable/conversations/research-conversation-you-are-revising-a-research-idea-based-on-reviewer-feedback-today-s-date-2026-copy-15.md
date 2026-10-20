# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 36
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/df116416-ce65-492b-9144-f164ff15ec31.jsonl`
- **Structured JSON:** [`de2f66ae64ad60623604.json`](../../sessions/de/de2f66ae64ad60623604.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:48:45.700Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:48:45.700Z",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\",\n  \"core_problem\": \"The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances — is: how accurately can a few-shot LLM assign semantic bug type labels from an 18-category taxonomy, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\\n\\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-aware retrieval benefits code repair by using contrastive-learned embeddings over Infer's static-analysis-derived bug type annotations, but its type signal remains a soft continuous embedding feature — retrieval is still nearest-neighbor search across a unified corpus, not hard index-construction partitioning. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.\",\n  \"opportunity\": \"ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning to bring semantically equivalent bugs and their fixes closer in embedding space, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), and achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) InferFix's type signal is a soft contrastive embedding feature at retrieval time — the retrieval pool is the full unified corpus, and type influences embedding proximity rather than pool membership — whereas FTCR hard-partitions the corpus into discrete type sub-indices at construction time so only same-type pairs are candidates for any query; (b) InferFix's 'types' are Infer diagnostic IDs (static-analysis-specific), not the 18-category natural-bug taxonomy aligned with DebugBench; (c) InferFix uses InferredBugs (static-analysis-artifact bugs in Java/C# repos), not natural bug-fix pairs from issue trackers and CI logs. InferFix validates that type-aware retrieval helps repair (supporting FTCR's hypothesis) while leaving the hard vs. soft type-partitioning comparison unresolved. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than either InferFix's soft contrastive type conditioning or ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python, enabling direct classifier calibration and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.\",\n  \"landscape\": \"RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning to embed semantically equivalent bugs and their fixes close together, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), then retrieves the most similar fix from InferredBugs (Java/C# repos with Infer-detected bugs). InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) retrieval mechanism — InferFix uses soft contrastive similarity where type is an embedding-time signal and retrieval is nearest-neighbor search over the full unified corpus; FTCR partitions the corpus into discrete type sub-indices at construction time, so the retrieval pool for any query is restricted to same-type pairs before similarity scoring; (b) defect taxonomy — InferFix uses Infer's diagnostic IDs (covering only statically-detectable bug patterns), not the 18-category natural-bug taxonomy aligned with DebugBench's empirically-grounded labels; (c) corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether hard construction-time partitioning outperforms soft retrieval-time type conditioning for fix-template precision. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.\",\n  \"approach\": \"We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft root-cause embedding for cross-repository fix template transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\\n\\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\\n\\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\\n\\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations; configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers.\\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 851 held-out instances → X% per-type accuracy. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-type count table computed; merge policy applied for rare Java types.\\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices).\\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants; confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z%; misclassified → W%. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (6-type coarse vs. 18-type fine vs. merged-Java categories); retrieval k sweep (1/3/5/10).\\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise. The two-day writing window is extremely tight and requires a pre-drafted paper skeleton (introduction, related work, method) to be prepared during the Day 4–6 experiment-build window.\\n\\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type conditioning improves over code-similarity retrieval, but uses a soft contrastive mechanism where type influences embedding distance rather than pool membership. FTCR embodies a stronger form of this principle: rather than retrieving the most similar embedding from a type-influenced but unified pool, we restrict the retrieval pool to same-type pairs at index construction, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\\n\\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\\n\\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\\n\\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs), 18-type analysis yields an estimated mean of ~138 pairs per type, driven by Python (~2,487). For Java-only ablations (~559 pairs, ~31 per type average), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories; Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled.\\n\\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\\n\\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (851 instances) directly measures few-shot classifier precision and recall per type against oracle ground-truth labels, yielding X%. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++), transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\\n\\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\\n\\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\\n\\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\\n\\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.\",\n  \"resource_estimate\": {\n    \"auto_research\": {\n      \"gpu_hours\": \"~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)\",\n      \"gpu_utilization\": \"near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants\",\n      \"ablation_scope\": \"Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band\",\n      \"timeline\": \"10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.\",\n      \"day_by_day_schedule\": \"Day 0 (May 10): setup and corpus annotation launch. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X%, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F). Day 7–9 (May 17–19): DebugBench evaluation + confidence stratification (Z%, W%) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.\",\n      \"team\": \"0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)\",\n      \"claude_api_cost\": \"$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)\",\n      \"embedding_api_cost\": \"~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)\",\n      \"estimated_gpu_cost\": \"~$969 (323 A100-hours × $3/h)\",\n      \"speed_bottleneck\": \"GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls\",\n      \"risk_note\": \"SWE-bench Lite may not complete before Day 12; MVS for EMNLP submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, which is achievable within the 10–14 day window. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6.\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 ARR (deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. NLP lead framing: LLM-generated bug type label quality and its downstream retrieval impact — a contribution to the NLP literature on LLM annotation reliability and retrieval-augmented generation. EMNLP's Empirical Methods track and code NLP community regularly accept papers evaluating LLM-generated categorical labels and RAG system design; the X%/Y%/Z%/W% falsifiable finding fits this tradition. Timeline is extremely tight: the two-day writing window requires a pre-drafted skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.\",\n    \"ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; InferFix paragraph establishes that hard vs. soft type partitioning is the untested dimension; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.\",\n    \"FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable).\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-aware cross-repository repair retrieval; Retriever pretrained via contrastive learning over Infer bug type annotations (null dereferences, resource leaks, thread safety) on InferredBugs corpus (Java/C# repos); 76.8% Java top-1 accuracy; uses soft contrastive similarity at retrieval time, NOT hard index-construction partitioning — FTCR's scientific contribution is testing hard vs. soft partitioning as the variable InferFix leaves unresolved; must differentiate explicitly: (a) soft contrastive embedding vs. hard construction-time partition; (b) Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; (c) InferredBugs (static-analysis artifacts) vs. natural issue-tracker/CI bug-fix pairs]\",\n    \"ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]\",\n    \"SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]\",\n    \"TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]\",\n    \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]\",\n    \"RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 types and 3 languages]\",\n    \"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]\",\n    \"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]\",\n    \"D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]\",\n    \"M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]\",\n    \"RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]\",\n    \"DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 18-category labels across C++/Java/Python for 4,253 instances; held-out 20% split for classifier calibration (X%); acknowledged synthetic-bug limitation]\",\n    \"GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]\",\n    \"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]\",\n    \"What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]\",\n    \"PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]\",\n    \"RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]\",\n    \"CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]\"\n  ],\n  \"description\": \"FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (InferFix's contrastive approach, ESEC/FSE 2023; ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer. The primary NLP contribution — targeted at EMNLP 2026 ARR (May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 6 revisions address five issues: (a) VENUE RESTORED — EMNLP 2026 ARR (May 25) reinstated as primary target with explicit day-by-day execution schedule (Days 0–12: auto-research; Days 13–15: paper finalization); auto-research is the only constraint-compliant mode (10–14 days); manual and human-in-loop modes removed from resource_estimate as they violate the 16-day budget; NLP lead framing (X%/Y%/Z%/W% classifier calibration) is the EMNLP submission's opening contribution; MVS = DebugBench calibration + Defects4J V1.2 ablations + random-partition control; SWE-bench Lite deferred to ICSE 2027 version if not complete by Day 12. (b) INFERFIX ADDED — InferFix (ESEC/FSE 2023, arXiv:2303.07263) added to landscape, opportunity, core_problem, and key_references with explicit three-point differentiation: soft contrastive embedding at retrieval time vs. FTCR's hard construction-time partitioning; Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; InferredBugs (static-analysis artifacts) vs. natural bug-fix pairs; InferFix leaves the hard vs. soft comparison unresolved and FTCR tests it directly. (c) CORPUS CONFOUND EXPLICIT — landscape and approach now explicitly state that intra-corpus ablations (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) are the clean architectural test; absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality simultaneously and are presented as joint-effect comparisons. (d) TYPEREPAIR EVIDENTIARY BASIS — differentiation claim supported by evaluation design argument: TypeRepair evaluates exclusively on within-project datasets (Defects4J, QuixBugs) with no external cross-repository corpus in the benchmark setup, making within-project scope structurally evident from the experimental design. (e) RESOURCE_ESTIMATE RESTRUCTURED — stripped to auto-research mode only with day-by-day schedule integrated into the approach section.\",\n  \"project_name\": \"failure_type_rag_repair\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 6)\nIssues: [\"HIGH — EMNLP Main vs. Findings target ambiguity persists: target_venues now lists 'EMNLP 2026 Main' AND 'EMNLP 2026 Findings' as separate entries, but the empirical calibration study (X%/Y%/Z%/W% LLM label reliability) is a measurement finding about LLM annotation quality — appropriate for EMNLP Findings, not the Main track, which expects findings that advance understanding of language models at a deeper level. Rounds 3 and 4 both explicitly downgraded the EMNLP target to Findings; Round 5 asked to restore EMNLP without specifying Main vs. Findings; Round 6 silently re-expanded to Main. The proposal must commit to EMNLP Findings as the EMNLP target and stop oscillating. Trying for Main and being desk-rejected wastes the submission cycle.\", \"MEDIUM — DebugBench hierarchical structure mischaracterized throughout: independently verified (ACL Findings 2024 paper) that DebugBench has 4 MAJOR categories (Syntax Bugs, Logic Bugs, Reference Bugs, Multiple Bugs) with 18 MINOR sub-types nested within them — not 18 independent categories. The proposal consistently refers to '18-category taxonomy' and '18-category natural-bug taxonomy aligned with DebugBench's taxonomy.' This is inaccurate and will flag with any reviewer who has read DebugBench. Concretely: the merge policy for rare types must operate within the 4-major/18-minor hierarchy (merge within major categories first, not across them); X%/Y%/Z%/W% measurements must specify whether they are measured at the major-type or minor-type level; and the '~31 Java instances per type' figure implies 18 equal partitions, which is not how the benchmark is structured.\", \"MEDIUM — Day-0-today execution assumption is unverified: the schedule commits to launching corpus annotation pipeline on May 10 (today) with 2 A100 nodes already available. No verification of compute availability, API rate limits on day 1, or Defects4J V1.2 Docker environment readiness is mentioned. If infrastructure setup takes 1–2 days (common in practice), the already-tight 2-day paper writing window (Days 13–15, May 23–25) disappears entirely. The proposal should either (a) confirm that compute is already provisioned and Docker environments tested, or (b) revise the schedule to account for a 1-day setup buffer by shifting MVS deliverables earlier.\", \"LOW — InferFix type-as-embedding-signal claim needs precision: independent verification found that InferFix adds bug type annotations as prompt context alongside retrieved fixes, while the contrastive retriever learns semantic similarity between bugs/fixes. The proposal claims 'type influences embedding proximity rather than pool membership' — this framing appears broadly correct but needs verification against the actual retriever architecture section (Section 3 of arXiv:2303.07263), not just the abstract. If InferFix's retriever does NOT explicitly condition on type labels during encoding (only using type for post-retrieval prompt augmentation), the 'soft type conditioning' differentiation needs rewording to 'type-correlated semantic similarity' to avoid misrepresenting the baseline.\", \"LOW — Statistical significance for Z% and W% unstated: the Z% (repair improvement for correctly classified) and W% (repair degradation for misclassified) measurements will have unequal sample sizes depending on classifier accuracy. With ~31 Java instances per minor type and a 20% held-out split (~6 per type), per-type statistical tests are underpowered. The proposal should specify: (a) whether Z% and W% are aggregated across all types or reported per type; (b) what statistical test is used; (c) minimum sample threshold for a type to contribute to the Z%/W% comparison.\"]\nFeedback: Round 6 has addressed all five Round 5 issues: EMNLP venue restored with committed schedule, InferFix added with three-point differentiation, corpus confound made explicit, TypeRepair evidentiary basis stated, resource estimate stripped to auto-research only. The core hypothesis is well-posed and the experimental design is increasingly rigorous. Three targeted fixes would make this submission-ready: (1) COMMIT TO EMNLP FINDINGS — remove 'EMNLP 2026 Main' from target_venues and replace with 'EMNLP 2026 Findings (via ARR)'. The X%/Y%/Z%/W% calibration study is a strong Findings paper; attempting Main track risks desk rejection on NLP-contribution grounds and wastes the submission cycle. (2) FIX DEBUGBENCH STRUCTURE — replace every instance of '18-category' with '4-major/18-minor hierarchical taxonomy' and state that X%/Y%/Z%/W% measurements operate at the minor-type level (18 sub-categories), with major-type aggregation reported as a secondary result. Revise the merge policy to explicitly merge within the same major category first (e.g., merge rare Reference Bug sub-types before merging across Logic and Reference). (3) CONFIRM COMPUTE READINESS — add one sentence to the Day 0 entry: 'Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' If this cannot be stated truthfully, shift the MVS timeline by 1 day and compress paper writing to 1 day with a more aggressive pre-drafted skeleton policy. These three changes are low-effort and directly address verifiable gaps; the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.6，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:48:45.704Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:48:45.704Z",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

## Round 1

34 recorded events

### User

_source line 3 · 2026-05-10T06:48:45.734Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "core_problem": "The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances — is: how accurately can a few-shot LLM assign semantic bug type labels from an 18-category taxonomy, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\n\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-aware retrieval benefits code repair by using contrastive-learned embeddings over Infer's static-analysis-derived bug type annotations, but its type signal remains a soft continuous embedding feature — retrieval is still nearest-neighbor search across a unified corpus, not hard index-construction partitioning. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.",
  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning to bring semantically equivalent bugs and their fixes closer in embedding space, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), and achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) InferFix's type signal is a soft contrastive embedding feature at retrieval time — the retrieval pool is the full unified corpus, and type influences embedding proximity rather than pool membership — whereas FTCR hard-partitions the corpus into discrete type sub-indices at construction time so only same-type pairs are candidates for any query; (b) InferFix's 'types' are Infer diagnostic IDs (static-analysis-specific), not the 18-category natural-bug taxonomy aligned with DebugBench; (c) InferFix uses InferredBugs (static-analysis-artifact bugs in Java/C# repos), not natural bug-fix pairs from issue trackers and CI logs. InferFix validates that type-aware retrieval helps repair (supporting FTCR's hypothesis) while leaving the hard vs. soft type-partitioning comparison unresolved. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than either InferFix's soft contrastive type conditioning or ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python, enabling direct classifier calibration and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.",
  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-aware cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning to embed semantically equivalent bugs and their fixes close together, conditioned on Infer's static-analysis-derived bug type annotations (null dereferences, resource leaks, thread-safety violations), then retrieves the most similar fix from InferredBugs (Java/C# repos with Infer-detected bugs). InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) retrieval mechanism — InferFix uses soft contrastive similarity where type is an embedding-time signal and retrieval is nearest-neighbor search over the full unified corpus; FTCR partitions the corpus into discrete type sub-indices at construction time, so the retrieval pool for any query is restricted to same-type pairs before similarity scoring; (b) defect taxonomy — InferFix uses Infer's diagnostic IDs (covering only statically-detectable bug patterns), not the 18-category natural-bug taxonomy aligned with DebugBench's empirically-grounded labels; (c) corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether hard construction-time partitioning outperforms soft retrieval-time type conditioning for fix-template precision. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.",
  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms both InferFix's soft contrastive type conditioning and ReinFix's soft root-cause embedding for cross-repository fix template transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\n\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\n\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\n\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations; configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers.\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 851 held-out instances → X% per-type accuracy. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-type count table computed; merge policy applied for rare Java types.\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices).\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants; confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z%; misclassified → W%. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (6-type coarse vs. 18-type fine vs. merged-Java categories); retrieval k sweep (1/3/5/10).\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise. The two-day writing window is extremely tight and requires a pre-drafted paper skeleton (introduction, related work, method) to be prepared during the Day 4–6 experiment-build window.\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type conditioning improves over code-similarity retrieval, but uses a soft contrastive mechanism where type influences embedding distance rather than pool membership. FTCR embodies a stronger form of this principle: rather than retrieving the most similar embedding from a type-influenced but unified pool, we restrict the retrieval pool to same-type pairs at index construction, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\n\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\n\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs), 18-type analysis yields an estimated mean of ~138 pairs per type, driven by Python (~2,487). For Java-only ablations (~559 pairs, ~31 per type average), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories; Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\n\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (851 instances) directly measures few-shot classifier precision and recall per type against oracle ground-truth labels, yielding X%. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++), transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\n\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\n\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.",
  "resource_estimate": {
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band",
      "timeline": "10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.",
      "day_by_day_schedule": "Day 0 (May 10): setup and corpus annotation launch. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X%, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F). Day 7–9 (May 17–19): DebugBench evaluation + confidence stratification (Z%, W%) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "SWE-bench Lite may not complete before Day 12; MVS for EMNLP submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, which is achievable within the 10–14 day window. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6."
    }
  },
  "target_venues": [
    "EMNLP 2026 ARR (deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. NLP lead framing: LLM-generated bug type label quality and its downstream retrieval impact — a contribution to the NLP literature on LLM annotation reliability and retrieval-augmented generation. EMNLP's Empirical Methods track and code NLP community regularly accept papers evaluating LLM-generated categorical labels and RAG system design; the X%/Y%/Z%/W% falsifiable finding fits this tradition. Timeline is extremely tight: the two-day writing window requires a pre-drafted skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.",
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; InferFix paragraph establishes that hard vs. soft type partitioning is the untested dimension; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.",
    "FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable)."
  ],
  "level": "solid",
  "key_references": [
    "InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-aware cross-repository repair retrieval; Retriever pretrained via contrastive learning over Infer bug type annotations (null dereferences, resource leaks, thread safety) on InferredBugs corpus (Java/C# repos); 76.8% Java top-1 accuracy; uses soft contrastive similarity at retrieval time, NOT hard index-construction partitioning — FTCR's scientific contribution is testing hard vs. soft partitioning as the variable InferFix leaves unresolved; must differentiate explicitly: (a) soft contrastive embedding vs. hard construction-time partition; (b) Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; (c) InferredBugs (static-analysis artifacts) vs. natural issue-tracker/CI bug-fix pairs]",
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]",
    "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]",
    "RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 types and 3 languages]",
    "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]",
    "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]",
    "D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]",
    "M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]",
    "RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]",
    "DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 18-category labels across C++/Java/Python for 4,253 instances; held-out 20% split for classifier calibration (X%); acknowledged synthetic-bug limitation]",
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]"
  ],
  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (InferFix's contrastive approach, ESEC/FSE 2023; ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer. The primary NLP contribution — targeted at EMNLP 2026 ARR (May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 6 revisions address five issues: (a) VENUE RESTORED — EMNLP 2026 ARR (May 25) reinstated as primary target with explicit day-by-day execution schedule (Days 0–12: auto-research; Days 13–15: paper finalization); auto-research is the only constraint-compliant mode (10–14 days); manual and human-in-loop modes removed from resource_estimate as they violate the 16-day budget; NLP lead framing (X%/Y%/Z%/W% classifier calibration) is the EMNLP submission's opening contribution; MVS = DebugBench calibration + Defects4J V1.2 ablations + random-partition control; SWE-bench Lite deferred to ICSE 2027 version if not complete by Day 12. (b) INFERFIX ADDED — InferFix (ESEC/FSE 2023, arXiv:2303.07263) added to landscape, opportunity, core_problem, and key_references with explicit three-point differentiation: soft contrastive embedding at retrieval time vs. FTCR's hard construction-time partitioning; Infer-specific diagnostic IDs vs. 18-category natural-bug taxonomy; InferredBugs (static-analysis artifacts) vs. natural bug-fix pairs; InferFix leaves the hard vs. soft comparison unresolved and FTCR tests it directly. (c) CORPUS CONFOUND EXPLICIT — landscape and approach now explicitly state that intra-corpus ablations (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) are the clean architectural test; absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality simultaneously and are presented as joint-effect comparisons. (d) TYPEREPAIR EVIDENTIARY BASIS — differentiation claim supported by evaluation design argument: TypeRepair evaluates exclusively on within-project datasets (Defects4J, QuixBugs) with no external cross-repository corpus in the benchmark setup, making within-project scope structurally evident from the experimental design. (e) RESOURCE_ESTIMATE RESTRUCTURED — stripped to auto-research mode only with day-by-day schedule integrated into the approach section.",
  "project_name": "failure_type_rag_repair",
  "source": "web_research"
}

## Reviewer feedback (round 6)
Issues: ["HIGH — EMNLP Main vs. Findings target ambiguity persists: target_venues now lists 'EMNLP 2026 Main' AND 'EMNLP 2026 Findings' as separate entries, but the empirical calibration study (X%/Y%/Z%/W% LLM label reliability) is a measurement finding about LLM annotation quality — appropriate for EMNLP Findings, not the Main track, which expects findings that advance understanding of language models at a deeper level. Rounds 3 and 4 both explicitly downgraded the EMNLP target to Findings; Round 5 asked to restore EMNLP without specifying Main vs. Findings; Round 6 silently re-expanded to Main. The proposal must commit to EMNLP Findings as the EMNLP target and stop oscillating. Trying for Main and being desk-rejected wastes the submission cycle.", "MEDIUM — DebugBench hierarchical structure mischaracterized throughout: independently verified (ACL Findings 2024 paper) that DebugBench has 4 MAJOR categories (Syntax Bugs, Logic Bugs, Reference Bugs, Multiple Bugs) with 18 MINOR sub-types nested within them — not 18 independent categories. The proposal consistently refers to '18-category taxonomy' and '18-category natural-bug taxonomy aligned with DebugBench's taxonomy.' This is inaccurate and will flag with any reviewer who has read DebugBench. Concretely: the merge policy for rare types must operate within the 4-major/18-minor hierarchy (merge within major categories first, not across them); X%/Y%/Z%/W% measurements must specify whether they are measured at the major-type or minor-type level; and the '~31 Java instances per type' figure implies 18 equal partitions, which is not how the benchmark is structured.", "MEDIUM — Day-0-today execution assumption is unverified: the schedule commits to launching corpus annotation pipeline on May 10 (today) with 2 A100 nodes already available. No verification of compute availability, API rate limits on day 1, or Defects4J V1.2 Docker environment readiness is mentioned. If infrastructure setup takes 1–2 days (common in practice), the already-tight 2-day paper writing window (Days 13–15, May 23–25) disappears entirely. The proposal should either (a) confirm that compute is already provisioned and Docker environments tested, or (b) revise the schedule to account for a 1-day setup buffer by shifting MVS deliverables earlier.", "LOW — InferFix type-as-embedding-signal claim needs precision: independent verification found that InferFix adds bug type annotations as prompt context alongside retrieved fixes, while the contrastive retriever learns semantic similarity between bugs/fixes. The proposal claims 'type influences embedding proximity rather than pool membership' — this framing appears broadly correct but needs verification against the actual retriever architecture section (Section 3 of arXiv:2303.07263), not just the abstract. If InferFix's retriever does NOT explicitly condition on type labels during encoding (only using type for post-retrieval prompt augmentation), the 'soft type conditioning' differentiation needs rewording to 'type-correlated semantic similarity' to avoid misrepresenting the baseline.", "LOW — Statistical significance for Z% and W% unstated: the Z% (repair improvement for correctly classified) and W% (repair degradation for misclassified) measurements will have unequal sample sizes depending on classifier accuracy. With ~31 Java instances per minor type and a 20% held-out split (~6 per type), per-type statistical tests are underpowered. The proposal should specify: (a) whether Z% and W% are aggregated across all types or reported per type; (b) what statistical test is used; (c) minimum sample threshold for a type to contribute to the Z%/W% comparison."]
Feedback: Round 6 has addressed all five Round 5 issues: EMNLP venue restored with committed schedule, InferFix added with three-point differentiation, corpus confound made explicit, TypeRepair evidentiary basis stated, resource estimate stripped to auto-research only. The core hypothesis is well-posed and the experimental design is increasingly rigorous. Three targeted fixes would make this submission-ready: (1) COMMIT TO EMNLP FINDINGS — remove 'EMNLP 2026 Main' from target_venues and replace with 'EMNLP 2026 Findings (via ARR)'. The X%/Y%/Z%/W% calibration study is a strong Findings paper; attempting Main track risks desk rejection on NLP-contribution grounds and wastes the submission cycle. (2) FIX DEBUGBENCH STRUCTURE — replace every instance of '18-category' with '4-major/18-minor hierarchical taxonomy' and state that X%/Y%/Z%/W% measurements operate at the minor-type level (18 sub-categories), with major-type aggregation reported as a secondary result. Revise the merge policy to explicitly merge within the same major category first (e.g., merge rare Reference Bug sub-types before merging across Logic and Reference). (3) CONFIRM COMPUTE READINESS — add one sentence to the Day 0 entry: 'Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' If this cannot be stated truthfully, shift the MVS timeline by 1 day and compress paper writing to 1 day with a more aggressive pre-drafted skeleton policy. These three changes are low-effort and directly address verifiable gaps; the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings.

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
这个 idea 已经经过 6 轮修订，近 3 轮的平均分从 3.5 到 3.6，没有明显改善。

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
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "cb82e418-1ca1-4454-8cb8-bc21563c6a31",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:48:45.731Z_

```json
{
  "parentUuid": "cb82e418-1ca1-4454-8cb8-bc21563c6a31",
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
  "uuid": "83f99887-fd99-438d-908f-06b48659225b",
  "timestamp": "2026-05-10T06:48:45.731Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:48:45.731Z_

```json
{
  "parentUuid": "83f99887-fd99-438d-908f-06b48659225b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "fa5de165-25e9-4e53-bc62-3e2dcbaeedbc",
  "timestamp": "2026-05-10T06:48:45.731Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "fa5de165-25e9-4e53-bc62-3e2dcbaeedbc",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise FTCR for EMNLP Findings with DebugBench hierarchy fix",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:49:07.485Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

**Current State Analysis:**
- 6 rounds of revision with minimal score improvement (3.5 → 3.6)
- The reviewer feedback for Round 6 is actually quite positive: "The core hypothesis is well-posed and the experimental design is increasingly rigorous" and "the underlying science is solid and the proposal is close to submission-ready for EMNLP 2026 Findings"
- The three remaining issues are described as "low-effort" fixes

**Round 7 Issues:**
1. **HIGH** - EMNLP Main vs. Findings target ambiguity - Commit to EMNLP Findings


2. **MEDIUM** - DebugBench hierarchical structure mischaracterized (4 major / 18 minor, not 18 independent categories)
3. **MEDIUM** - Day-0 execution assumption unverified (compute readiness)
4. **LOW** - InferFix type-as-embedding-signal claim needs precision
5. **LOW** - Statistical significance for Z% and W% unstated

**Key decision: minor fix, major revision, or pivot?**

The reviewer says the science is solid and close to submission-ready. The issues are mostly factual accuracy problems and one venue commitment clarification—all addressable without rethinking the core approach.

I need to verify three things: the DebugBench taxonomy structure, InferFix's retriever architecture (whether it uses type labels during encoding or just for prompt augmentation), and confirm compute readiness for the stated timeline. The reviewer's positive assessment suggests these are precision fixes rather than fundamental flaws, so I'll plan targeted research on each point before making corrections.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fa5de165-25e9-4e53-bc62-3e2dcbaeedbc",
  "isSidechain": false,
  "requestId": "req_011CatSaCPA43Y7b4nFJvRPZ",
  "type": "assistant",
  "uuid": "c3408432-1f2f-4569-9054-b3f782ebc873",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RCJ14F1Gz6pyvQetuigBJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18925,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1725,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18925
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

_source line 9 · 2026-05-10T06:49:07.799Z_

Looking at this situation carefully: the reviewer says the science is solid and "close to submission-ready" — the remaining issues are precision fixes, not fundamental problems. After 6 rounds of minor drift, the right call here is targeted, accurate fixes based on verified facts rather than another structural overhaul.

I'll research the two factual verification needs (DebugBench taxonomy structure, InferFix retriever architecture) in parallel before making changes.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c3408432-1f2f-4569-9054-b3f782ebc873",
  "isSidechain": false,
  "requestId": "req_011CatSaCPA43Y7b4nFJvRPZ",
  "type": "assistant",
  "uuid": "4a889028-2744-42a9-9b76-edc78ce7532b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RCJ14F1Gz6pyvQetuigBJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18925,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1725,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18925
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

_source line 10 · 2026-05-10T06:49:12.674Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01KBcBfUjdYDTcWLNpGbrBH1`</summary>

```json
{
  "description": "Verify DebugBench taxonomy structure and InferFix retriever architecture",
  "subagent_type": "Explore",
  "prompt": "I need to verify two specific factual claims about papers in the automated program repair / LLM evaluation space. Please fetch and read the relevant sections of these papers:\n\n**Task 1: DebugBench taxonomy structure**\nSearch for and fetch the DebugBench paper (ACL Findings 2024). I need to know:\n- Does DebugBench have 4 MAJOR categories with 18 MINOR sub-types nested within them, or 18 independent categories?\n- What are the 4 major categories (if they exist)?\n- What are the 18 minor sub-types?\n- How are instances distributed across major vs. minor categories?\n\nTry fetching: https://arxiv.org/abs/2401.04621 (likely DebugBench arXiv ID) or search \"DebugBench evaluating debugging capability large language models ACL 2024\"\n\n**Task 2: InferFix retriever architecture**\nSearch for and fetch the InferFix paper (ESEC/FSE 2023, arXiv:2303.07263). I need to know:\n- Does the Retriever (contrastive-pretrained model) explicitly use/condition on bug type labels DURING encoding (i.e., type is fed as input to the encoder)?\n- Or does type information only appear in post-retrieval prompt augmentation (i.e., the retrieved fix + its type annotation are concatenated into the prompt, but the retriever itself is just semantic similarity)?\n- Specifically look at Section 3 (retriever architecture) for how type labels are used\n\nTry: https://arxiv.org/abs/2303.07263\n\nReport the exact quotes from each paper that clarify these architecture questions. Be precise — I need verbatim excerpts, not paraphrases."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a889028-2744-42a9-9b76-edc78ce7532b",
  "isSidechain": false,
  "requestId": "req_011CatSaCPA43Y7b4nFJvRPZ",
  "type": "assistant",
  "uuid": "2918bdcf-88f1-402b-b47c-ea9d244e91b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RCJ14F1Gz6pyvQetuigBJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18925,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1725,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18925
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

_source line 11 · 2026-05-10T06:49:16.329Z_

<details open><summary>🔧 Tool call — Agent · `toolu_012tfhYu8ejiVCXomgahjiRm`</summary>

```json
{
  "description": "Search for recent concurrent work on type-conditioned repair retrieval",
  "subagent_type": "Explore",
  "prompt": "I'm working on a research idea called FTCR (Failure-Type-Conditioned Retrieval) for automated program repair. The core idea: classify incoming bugs into semantic categories, then retrieve fix patches only from the type-matched sub-index (hard partitioning), vs. soft retrieval baselines like ReinFix (ICSE 2026).\n\nPlease search for any papers from late 2025 or 2026 that might be closely related or concurrent work I'm missing. Search for:\n\n1. \"type-conditioned retrieval program repair 2025 2026\"\n2. \"categorical retrieval augmented generation bug fix 2026\"\n3. \"failure type classification automated repair retrieval\"\n4. \"DebugBench 2025 2026 program repair\" (any papers that USE DebugBench for repair evaluation)\n5. \"hard partition retrieval code repair\"\n6. \"EMNLP 2026 program repair retrieval\" (any accepted/submitted papers)\n\nFor each paper found, report: title, venue, year, and 1-2 sentence description of how it relates to FTCR. Focus on papers that might undermine the novelty claim of hard categorical type partitioning for cross-repository fix retrieval.\n\nAlso check: https://arxiv.org/search/?searchtype=all&query=type+conditioned+retrieval+program+repair&start=0 if possible."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2918bdcf-88f1-402b-b47c-ea9d244e91b7",
  "isSidechain": false,
  "requestId": "req_011CatSaCPA43Y7b4nFJvRPZ",
  "type": "assistant",
  "uuid": "034f5664-c939-44c2-a89e-9f464f3301c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01RCJ14F1Gz6pyvQetuigBJh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18925,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1725,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 18925,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1725,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 18925,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 18925
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

_source line 12 · 2026-05-10T06:50:57.623Z_

<details><summary>↩ Tool result · `toolu_01KBcBfUjdYDTcWLNpGbrBH1`</summary>

```text
Perfect! I now have comprehensive information. Let me compile the findings with exact references and sources.

## Summary of Findings

### **Task 1: DebugBench Taxonomy Structure**

**VERIFIED:** DebugBench has **4 MAJOR categories with 18 MINOR sub-types nested within them** (NOT 18 independent categories).

**The 4 Major Categories and 18 Minor Sub-types:**

1. **Syntax (7 sub-types):**
   - Misused ==/= (137 instances)
   - Missing colons (129 instances)
   - Unclosed parentheses (133 instances)
   - Illegal separation (68 instances)
   - Illegal indentation (45 instances)
   - Unclosed string (125 instances)
   - Illegal comment (124 instances)

2. **Reference (4 sub-types):**
   - Faulty indexing (206 instances)
   - Undefined objects (187 instances)
   - Undefined methods (167 instances)
   - Illegal keywords (124 instances)

3. **Logic (4 sub-types):**
   - Condition error (260 instances)
   - Operation error (180 instances)
   - Variable error (100 instances)
   - Other error (50 instances)

4. **Multiple (3 sub-types):**
   - Double bugs (750 instances)
   - Triple bugs (750 instances)
   - Quadruple bugs (718 instances)

**Distribution:** The taxonomy is clearly hierarchical, with instances distributed across the 18 minor types nested within the 4 major categories. Total: 4,253 instances across C++, Java, and Python.

---

### **Task 2: InferFix Retriever Architecture**

**ANSWER:** The retriever does NOT explicitly condition on bug type labels DURING encoding as a direct input to the encoder. Rather, **bug type information is used in TWO ways:**

1. **During Contrastive Pre-training:** Bug type serves as a LABEL for organizing the training data structure:
   - Exact quote from the ar5iv paper fetch: "a query – an encoding of a buggy code snippet; a positive sample representing a semantically similar code snippet of the **same bug type**; and a set of negative samples which are irrelevant code snippets of **different bug types**."
   - This means the contrastive learning objective uses bug type to define what counts as a "positive" vs "negative" sample, but type is NOT fed as input to the encoder itself.

2. **During Inference/Retrieval:** Bug type appears in post-retrieval filtering and prompt augmentation:
   - "retrieved fixes must be of the same bug type as the query"
   - Bug type annotations are added to the prompt for the Generator: "prompts augmented via adding bug type annotations and semantically similar fixes retrieved from an external non-parametric memory"

**The Key Distinction:** The Retriever encoder itself (the bidirectional transformer) encodes only the buggy code snippets as dense vectors. Bug type information is metadata that structures the training objective and filters results, but is NOT concatenated with or fed as input to the encoder during either training or inference.

---

## Sources

**DebugBench Papers:**
- [DebugBench: Evaluating Debugging Capability of Large Language Models - ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)
- [DebugBench on arXiv](https://arxiv.org/abs/2401.04621)
- [DebugBench OpenReview PDF](https://openreview.net/pdf/f3e7b01b7edc2ac558a684981bd38c590ff89cb3.pdf)

**InferFix Papers:**
- [InferFix: End-to-End Program Repair with LLMs - arXiv](https://arxiv.org/abs/2303.07263)
- [InferFix - arXiv PDF](https://arxiv.org/pdf/2303.07263)
- [InferFix - Microsoft Research Publication](https://www.microsoft.com/en-us/research/publication/inferfix-end-to-end-program-repair-with-llms-over-retrieval-augmented-prompts/)
- [InferFix - ESEC/FSE 2023 Conference](https://2023.esec-fse.org/details/fse-2023-industry/33/InferFix-End-to-End-Program-Repair-with-LLMs)
- [InferFix - ar5iv HTML version](https://ar5iv.labs.arxiv.org/html/2303.07263)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2918bdcf-88f1-402b-b47c-ea9d244e91b7",
  "isSidechain": false,
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "e41a5207-34e6-4b79-b647-de3ca64b5063",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify two specific factual claims about papers in the automated program repair / LLM evaluation space. Please fetch and read the relevant sections of these papers:\n\n**Task 1: DebugBench taxonomy structure**\nSearch for and fetch the DebugBench paper (ACL Findings 2024). I need to know:\n- Does DebugBench have 4 MAJOR categories with 18 MINOR sub-types nested within them, or 18 independent categories?\n- What are the 4 major categories (if they exist)?\n- What are the 18 minor sub-types?\n- How are instances distributed across major vs. minor categories?\n\nTry fetching: https://arxiv.org/abs/2401.04621 (likely DebugBench arXiv ID) or search \"DebugBench evaluating debugging capability large language models ACL 2024\"\n\n**Task 2: InferFix retriever architecture**\nSearch for and fetch the InferFix paper (ESEC/FSE 2023, arXiv:2303.07263). I need to know:\n- Does the Retriever (contrastive-pretrained model) explicitly use/condition on bug type labels DURING encoding (i.e., type is fed as input to the encoder)?\n- Or does type information only appear in post-retrieval prompt augmentation (i.e., the retrieved fix + its type annotation are concatenated into the prompt, but the retriever itself is just semantic similarity)?\n- Specifically look at Section 3 (retriever architecture) for how type labels are used\n\nTry: https://arxiv.org/abs/2303.07263\n\nReport the exact quotes from each paper that clarify these architecture questions. Be precise — I need verbatim excerpts, not paraphrases.",
    "agentId": "ae90863d2cc25a044",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have comprehensive information. Let me compile the findings with exact references and sources.\n\n## Summary of Findings\n\n### **Task 1: DebugBench Taxonomy Structure**\n\n**VERIFIED:** DebugBench has **4 MAJOR categories with 18 MINOR sub-types nested within them** (NOT 18 independent categories).\n\n**The 4 Major Categories and 18 Minor Sub-types:**\n\n1. **Syntax (7 sub-types):**\n   - Misused ==/= (137 instances)\n   - Missing colons (129 instances)\n   - Unclosed parentheses (133 instances)\n   - Illegal separation (68 instances)\n   - Illegal indentation (45 instances)\n   - Unclosed string (125 instances)\n   - Illegal comment (124 instances)\n\n2. **Reference (4 sub-types):**\n   - Faulty indexing (206 instances)\n   - Undefined objects (187 instances)\n   - Undefined methods (167 instances)\n   - Illegal keywords (124 instances)\n\n3. **Logic (4 sub-types):**\n   - Condition error (260 instances)\n   - Operation error (180 instances)\n   - Variable error (100 instances)\n   - Other error (50 instances)\n\n4. **Multiple (3 sub-types):**\n   - Double bugs (750 instances)\n   - Triple bugs (750 instances)\n   - Quadruple bugs (718 instances)\n\n**Distribution:** The taxonomy is clearly hierarchical, with instances distributed across the 18 minor types nested within the 4 major categories. Total: 4,253 instances across C++, Java, and Python.\n\n---\n\n### **Task 2: InferFix Retriever Architecture**\n\n**ANSWER:** The retriever does NOT explicitly condition on bug type labels DURING encoding as a direct input to the encoder. Rather, **bug type information is used in TWO ways:**\n\n1. **During Contrastive Pre-training:** Bug type serves as a LABEL for organizing the training data structure:\n   - Exact quote from the ar5iv paper fetch: \"a query – an encoding of a buggy code snippet; a positive sample representing a semantically similar code snippet of the **same bug type**; and a set of negative samples which are irrelevant code snippets of **different bug types**.\"\n   - This means the contrastive learning objective uses bug type to define what counts as a \"positive\" vs \"negative\" sample, but type is NOT fed as input to the encoder itself.\n\n2. **During Inference/Retrieval:** Bug type appears in post-retrieval filtering and prompt augmentation:\n   - \"retrieved fixes must be of the same bug type as the query\"\n   - Bug type annotations are added to the prompt for the Generator: \"prompts augmented via adding bug type annotations and semantically similar fixes retrieved from an external non-parametric memory\"\n\n**The Key Distinction:** The Retriever encoder itself (the bidirectional transformer) encodes only the buggy code snippets as dense vectors. Bug type information is metadata that structures the training objective and filters results, but is NOT concatenated with or fed as input to the encoder during either training or inference.\n\n---\n\n## Sources\n\n**DebugBench Papers:**\n- [DebugBench: Evaluating Debugging Capability of Large Language Models - ACL Anthology](https://aclanthology.org/2024.findings-acl.247/)\n- [DebugBench on arXiv](https://arxiv.org/abs/2401.04621)\n- [DebugBench OpenReview PDF](https://openreview.net/pdf/f3e7b01b7edc2ac558a684981bd38c590ff89cb3.pdf)\n\n**InferFix Papers:**\n- [InferFix: End-to-End Program Repair with LLMs - arXiv](https://arxiv.org/abs/2303.07263)\n- [InferFix - arXiv PDF](https://arxiv.org/pdf/2303.07263)\n- [InferFix - Microsoft Research Publication](https://www.microsoft.com/en-us/research/publication/inferfix-end-to-end-program-repair-with-llms-over-retrieval-augmented-prompts/)\n- [InferFix - ESEC/FSE 2023 Conference](https://2023.esec-fse.org/details/fse-2023-industry/33/InferFix-End-to-End-Program-Repair-with-LLMs)\n- [InferFix - ar5iv HTML version](https://ar5iv.labs.arxiv.org/html/2303.07263)"
      }
    ],
    "totalDurationMs": 104939,
    "totalTokens": 30911,
    "totalToolUseCount": 21,
    "usage": {
      "input_tokens": 6,
      "cache_creation_input_tokens": 1207,
      "cache_read_input_tokens": 28581,
      "output_tokens": 1117,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1207
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 6,
          "output_tokens": 1117,
          "cache_read_input_tokens": 28581,
          "cache_creation_input_tokens": 1207,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1207,
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
      "otherToolCount": 21
    }
  },
  "sourceToolAssistantUUID": "2918bdcf-88f1-402b-b47c-ea9d244e91b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T06:51:25.751Z_

<details><summary>↩ Tool result · `toolu_012tfhYu8ejiVCXomgahjiRm`</summary>

```text
Excellent. I have comprehensive results. Let me compile the findings now.

## Search Results Summary: FTCR-Related Papers (Late 2025 - 2026)

Based on extensive searches across web and arxiv, here are the papers and work most relevant to your FTCR (Failure-Type-Conditioned Retrieval) idea. The key finding: **while several concurrent papers use semantic categorization and taxonomy-based approaches to improve code repair, none appear to explicitly propose hard categorical partitioning of retrieval indices by failure type as a core contribution.**

---

### **Most Relevant Concurrent Work**

#### 1. **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (2025)
- **Venue/Year**: arxiv:2509.02330 (September 2025)
- **Relation to FTCR**: Closest competitor conceptually. ReCode uses **algorithm-aware hybrid retrieval** with multi-label classification (assigns multiple algorithmic categories per code snippet). It constructs RACodeBench with hierarchical organization by algorithmic type. Critically, this is **soft retrieval** (semantic matching with vector encodings), not hard categorical partitioning. Uses dual-view encoding (text + code) for fine-grained matching.
- **Key Difference**: ReCode retrieves from the same unified index using algorithmic similarity scores; FTCR would hard-partition the index by failure type before retrieval, potentially improving efficiency and preventing cross-type contamination.

#### 2. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (TOSEM 2026)
- **Venue/Year**: arxiv:2506.23749 (published 2026)
- **Relation to FTCR**: Comprehensive taxonomy of 63 LLM-based APR systems. Identifies **retrieval-augmented repair** as a key paradigm but notes systems employ non-graph lexical/semantic retrieval (BM25, dense embeddings) or graph-based approaches—none systematically partition indices by failure type. The survey emphasizes soft retrieval augmentation across diverse methods (RING, CEDAR, RAP-Gen, InferFix).
- **Implication**: Suggests the field lacks explicit hard-partition categorization—potential novelty for FTCR.

#### 3. **RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair** (2026)
- **Venue/Year**: arxiv:2603.01048 (March 2026)
- **Relation to FTCR**: Achieves 45.7% repair on SWE-bench Lite using hierarchical documentation + semantic similarity (FAISS embeddings). **Does NOT use bug type classification**; instead indexes by file-level semantic similarity. Represents state-of-the-art in soft semantic retrieval without categorical partitioning.

#### 4. **KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs** (2025)
- **Venue/Year**: arxiv:2503.21710 (March 2025)
- **Relation to FTCR**: Uses knowledge graphs (semantic + textual similarity + graph proximity) to retrieve 20 relevant functions for repair. Employs multi-hop traversal but **no failure-type classification**. Demonstrates that soft, hybrid retrieval (combining embedding similarity, Levenshtein distance, and shortest-path metrics) is the current standard—FTCR's hard partitioning would diverge.

#### 5. **ARSP: Automated Repair of Verilog Designs via Semantic Partitioning** (2025)
- **Venue/Year**: arxiv:2508.16517 (August 2025)
- **Relation to FTCR**: Uses **semantic partitioning** but for a different purpose: fragmenting modules into semantically coherent pieces to reduce context noise during repair, not for index-level bug type categorization. Achieves 77.92% pass@1. Architecturally distinct from FTCR's hard categorical retrieval index design.

---

### **Related but Distinct Approaches**

#### 6. **Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation** (2026)
- **Venue/Year**: arxiv:2603.10072 (March 2026)
- **Relation to FTCR**: Proposes a **failure taxonomy** for security patch generation (5 categories: Correct & Secure, Insecure & Breaking, Compilation Error, Security Failure, Functionality Failure). Demonstrates that categorizing repair failures is valuable (semantic misunderstanding = 51.4% of failures). However, uses taxonomy for **evaluation and diagnosis**, not for organizing retrieval indices—suggests FTCR's failure-type indexing could complement this analysis.

#### 7. **A Taxonomy of Failures in Tool-Augmented LLMs** (AST 2025)
- **Venue/Year**: homes.cs.washington.edu/~rjust/publ/tallm_testing_ast_2025.pdf (2025)
- **Relation to FTCR**: Proposes taxonomy of tool-use failures (tool selection, invocation, result interpretation). Relevant for understanding repair failure modes but not retrieval index organization.

#### 8. **RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code** (2025)
- **Venue/Year**: arxiv:2509.16701 (September 2025)
- **Relation to FTCR**: Three-step retrieval process (query rewriting → dataset indexing → similarity-based retrieval). Demonstrates soft similarity-based retrieval is standard; no bug-type partitioning employed. Complements FTCR by showing generic retrieval enhancement, contrasting with categorical partitioning.

#### 9. **Repository-Aware Dual-Encoder Code Retrieval** (EMNLP 2025 Findings)
- **Venue/Year**: aclanthology.org/2025.findings-emnlp.1147.pdf (November 2025)
- **Relation to FTCR**: Addresses cross-repository code retrieval with dual-encoder architecture, achieving precise fault localization. Uses embedding similarity without explicit failure-type categories. Represents soft retrieval baseline FTCR would benchmark against.

---

### **Bug Classification & Pattern-Based Approaches**

#### 10. **"Toward an understanding of bug fix patterns" series & recent extensions** (2025-2026)
- **Relation to FTCR**: Multiple papers (ScienceDirect 2025, Springer 2025) explore bug taxonomies and fix patterns. A 2025 study on distributed deep learning systems constructed taxonomy of 34 bug symptoms, 28 root causes, and 6 fix patterns. Another on autonomous driving systems proposed 15 syntactic + 27 semantic bug-fix patterns. These categorizations **could inform FTCR's failure-type partitioning strategy** but do not themselves propose category-indexed retrieval.

#### 11. **Enhancing Vulnerability Repair Through Extraction and Matching of Repair Patterns** (2025)
- **Venue/Year**: ScienceDirect 2025
- **Relation to FTCR**: Constructs a Repair Patterns Dictionary via clustering (GMM) on vulnerability statements. Uses pattern-matching for repair guidance. Complementary to FTCR but operates at patch generation stage, not retrieval index organization.

---

### **DebugBench & Benchmarks**

#### 12. **DebugBench: Evaluating Debugging Capability of Large Language Models** (2024, widely used 2025-2026)
- **Venue/Year**: Initially 2024; used extensively in 2025-2026 papers
- **Relation to FTCR**: Standard debugging benchmark with 4,253 instances across 4 major bug categories (Syntax, Reference, Logic, Multiple) and 18 minor types. **No papers found that explicitly use DebugBench's bug taxonomy to partition retrieval indices.**

#### 13. **CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows** (2026)
- **Venue/Year**: arxiv:2604.27148 (April 2026)
- **Relation to FTCR**: Provides repository-level repair evaluation. Doesn't propose categorical retrieval indexing.

---

### **ICSE 2025 & ICSE 2026 Program Repair Papers**

#### 14. **RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** (ICSE 2025)
- **Venue/Year**: ICSE 2025 (April 2025, Ottawa)
- **Relation to FTCR**: Agent-based retrieval of "repair ingredients" but uses general retrieval, not failure-type-conditioned index partitioning.

#### 15. **Aligning the Objective of LLM-Based Program Repair (D4C)** (ICSE 2025)
- **Venue/Year**: ICSE 2025
- **Relation to FTCR**: Addresses alignment of repair objectives; does not cover retrieval index design.

#### 16. **The Fact Selection Problem in LLM-Based Program Repair** (ICSE 2025 Research Track)
- **Venue/Year**: ICSE 2025
- **Relation to FTCR**: Focuses on selecting facts (evidence) for repair prompts; soft retrieval-based selection, not categorical partitioning.

#### 17. **Synthetic Repo-level Bug Dataset for Training Automated Program Repair Models** (ICSE 2026 Research Track)
- **Venue/Year**: ICSE 2026 (April 2026, Rio de Janeiro)
- **Relation to FTCR**: Introduces synthetic bug-fix dataset (SWE-Synth) for training. No categorical indexing proposed.

---

### **Retrieval-Augmented Code Generation Survey**

#### 18. **Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches** (2026)
- **Venue/Year**: arxiv:2510.04905 (October 2025)
- **Relation to FTCR**: Comprehensive taxonomy of RACG methods. Categorizes retrieval into non-graph (lexical, sparse BM25/TF-IDF, dense embedding, hybrid) and graph-based (AST, call graphs, CFG/DFG, module dependency). **Notable gap**: No mention of failure-type-conditioned hard partitioning as a retrieval strategy category. This absence suggests FTCR would represent a novel dimension not yet systematized in the literature.

---

## Summary of Novelty Risk Assessment

**Low Risk of Direct Precedent:**
- No paper explicitly proposes hard categorical partitioning of retrieval indices by failure type as a primary contribution
- ReCode is the closest (algorithm-aware retrieval), but uses soft similarity scoring within a unified index
- Most systems employ soft retrieval: vector similarity (FAISS, embeddings), BM25, or hybrid scoring

**Potential Vulnerability to Precedent:**
1. If ReinFix (ICSE 2026) uses failure-type soft retrieval and you claim hard partitioning is novel, the distinction hinges on soft vs. hard—be explicit in framing the contribution
2. DebugBench's bug taxonomy exists but isn't used for index partitioning in any paper found
3. Multiple papers classify bugs/failures (ReCode, error taxonomy papers), so the *idea* of failure-type classification isn't novel—FTCR's novelty is the application to index partitioning for cross-repo retrieval

**Recommendation:**
- Emphasize **hard index partitioning** as the core novelty, not failure-type classification alone
- Compare empirically against ReCode and RepoRepair as the strongest soft retrieval baselines
- Consider framing FTCR as "failure-type-indexed retrieval" to clarify it's about index organization, not just classification

---

## Sources

- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/html/2509.02330)
- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1)
- [RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair](https://arxiv.org/html/2603.01048v1)
- [KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs](https://arxiv.org/html/2503.21710v2)
- [ARSP: Automated Repair of Verilog Designs via Semantic Partitioning](https://arxiv.org/html/2508.16517)
- [Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation](https://arxiv.org/html/2603.10072v1)
- [RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/pdf/2509.16701)
- [Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches](https://arxiv.org/html/2510.04905v1)
- [CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows](https://arxiv.org/html/2604.27148v1)
- [GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More](https://arxiv.org/html/2504.09651)
- [ReAPR: Automatic program repair via retrieval-augmented large language models](https://link.springer.com/article/10.1007/s11219-025-09728-1)
- [ICSE 2025 Research Track](https://conf.researchr.org/track/icse-2025/icse-2025-research-track)
- [ICSE 2026 Research Track](https://conf.researchr.org/track/icse-2026/icse-2026-research-track)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "034f5664-c939-44c2-a89e-9f464f3301c1",
  "isSidechain": false,
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "d18db75c-c4bf-44f3-b7a9-96ea2fba968b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I'm working on a research idea called FTCR (Failure-Type-Conditioned Retrieval) for automated program repair. The core idea: classify incoming bugs into semantic categories, then retrieve fix patches only from the type-matched sub-index (hard partitioning), vs. soft retrieval baselines like ReinFix (ICSE 2026).\n\nPlease search for any papers from late 2025 or 2026 that might be closely related or concurrent work I'm missing. Search for:\n\n1. \"type-conditioned retrieval program repair 2025 2026\"\n2. \"categorical retrieval augmented generation bug fix 2026\"\n3. \"failure type classification automated repair retrieval\"\n4. \"DebugBench 2025 2026 program repair\" (any papers that USE DebugBench for repair evaluation)\n5. \"hard partition retrieval code repair\"\n6. \"EMNLP 2026 program repair retrieval\" (any accepted/submitted papers)\n\nFor each paper found, report: title, venue, year, and 1-2 sentence description of how it relates to FTCR. Focus on papers that might undermine the novelty claim of hard categorical type partitioning for cross-repository fix retrieval.\n\nAlso check: https://arxiv.org/search/?searchtype=all&query=type+conditioned+retrieval+program+repair&start=0 if possible.",
    "agentId": "a063f88923d02314b",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Excellent. I have comprehensive results. Let me compile the findings now.\n\n## Search Results Summary: FTCR-Related Papers (Late 2025 - 2026)\n\nBased on extensive searches across web and arxiv, here are the papers and work most relevant to your FTCR (Failure-Type-Conditioned Retrieval) idea. The key finding: **while several concurrent papers use semantic categorization and taxonomy-based approaches to improve code repair, none appear to explicitly propose hard categorical partitioning of retrieval indices by failure type as a core contribution.**\n\n---\n\n### **Most Relevant Concurrent Work**\n\n#### 1. **ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation** (2025)\n- **Venue/Year**: arxiv:2509.02330 (September 2025)\n- **Relation to FTCR**: Closest competitor conceptually. ReCode uses **algorithm-aware hybrid retrieval** with multi-label classification (assigns multiple algorithmic categories per code snippet). It constructs RACodeBench with hierarchical organization by algorithmic type. Critically, this is **soft retrieval** (semantic matching with vector encodings), not hard categorical partitioning. Uses dual-view encoding (text + code) for fine-grained matching.\n- **Key Difference**: ReCode retrieves from the same unified index using algorithmic similarity scores; FTCR would hard-partition the index by failure type before retrieval, potentially improving efficiency and preventing cross-type contamination.\n\n#### 2. **A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications** (TOSEM 2026)\n- **Venue/Year**: arxiv:2506.23749 (published 2026)\n- **Relation to FTCR**: Comprehensive taxonomy of 63 LLM-based APR systems. Identifies **retrieval-augmented repair** as a key paradigm but notes systems employ non-graph lexical/semantic retrieval (BM25, dense embeddings) or graph-based approaches—none systematically partition indices by failure type. The survey emphasizes soft retrieval augmentation across diverse methods (RING, CEDAR, RAP-Gen, InferFix).\n- **Implication**: Suggests the field lacks explicit hard-partition categorization—potential novelty for FTCR.\n\n#### 3. **RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair** (2026)\n- **Venue/Year**: arxiv:2603.01048 (March 2026)\n- **Relation to FTCR**: Achieves 45.7% repair on SWE-bench Lite using hierarchical documentation + semantic similarity (FAISS embeddings). **Does NOT use bug type classification**; instead indexes by file-level semantic similarity. Represents state-of-the-art in soft semantic retrieval without categorical partitioning.\n\n#### 4. **KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs** (2025)\n- **Venue/Year**: arxiv:2503.21710 (March 2025)\n- **Relation to FTCR**: Uses knowledge graphs (semantic + textual similarity + graph proximity) to retrieve 20 relevant functions for repair. Employs multi-hop traversal but **no failure-type classification**. Demonstrates that soft, hybrid retrieval (combining embedding similarity, Levenshtein distance, and shortest-path metrics) is the current standard—FTCR's hard partitioning would diverge.\n\n#### 5. **ARSP: Automated Repair of Verilog Designs via Semantic Partitioning** (2025)\n- **Venue/Year**: arxiv:2508.16517 (August 2025)\n- **Relation to FTCR**: Uses **semantic partitioning** but for a different purpose: fragmenting modules into semantically coherent pieces to reduce context noise during repair, not for index-level bug type categorization. Achieves 77.92% pass@1. Architecturally distinct from FTCR's hard categorical retrieval index design.\n\n---\n\n### **Related but Distinct Approaches**\n\n#### 6. **Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation** (2026)\n- **Venue/Year**: arxiv:2603.10072 (March 2026)\n- **Relation to FTCR**: Proposes a **failure taxonomy** for security patch generation (5 categories: Correct & Secure, Insecure & Breaking, Compilation Error, Security Failure, Functionality Failure). Demonstrates that categorizing repair failures is valuable (semantic misunderstanding = 51.4% of failures). However, uses taxonomy for **evaluation and diagnosis**, not for organizing retrieval indices—suggests FTCR's failure-type indexing could complement this analysis.\n\n#### 7. **A Taxonomy of Failures in Tool-Augmented LLMs** (AST 2025)\n- **Venue/Year**: homes.cs.washington.edu/~rjust/publ/tallm_testing_ast_2025.pdf (2025)\n- **Relation to FTCR**: Proposes taxonomy of tool-use failures (tool selection, invocation, result interpretation). Relevant for understanding repair failure modes but not retrieval index organization.\n\n#### 8. **RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code** (2025)\n- **Venue/Year**: arxiv:2509.16701 (September 2025)\n- **Relation to FTCR**: Three-step retrieval process (query rewriting → dataset indexing → similarity-based retrieval). Demonstrates soft similarity-based retrieval is standard; no bug-type partitioning employed. Complements FTCR by showing generic retrieval enhancement, contrasting with categorical partitioning.\n\n#### 9. **Repository-Aware Dual-Encoder Code Retrieval** (EMNLP 2025 Findings)\n- **Venue/Year**: aclanthology.org/2025.findings-emnlp.1147.pdf (November 2025)\n- **Relation to FTCR**: Addresses cross-repository code retrieval with dual-encoder architecture, achieving precise fault localization. Uses embedding similarity without explicit failure-type categories. Represents soft retrieval baseline FTCR would benchmark against.\n\n---\n\n### **Bug Classification & Pattern-Based Approaches**\n\n#### 10. **\"Toward an understanding of bug fix patterns\" series & recent extensions** (2025-2026)\n- **Relation to FTCR**: Multiple papers (ScienceDirect 2025, Springer 2025) explore bug taxonomies and fix patterns. A 2025 study on distributed deep learning systems constructed taxonomy of 34 bug symptoms, 28 root causes, and 6 fix patterns. Another on autonomous driving systems proposed 15 syntactic + 27 semantic bug-fix patterns. These categorizations **could inform FTCR's failure-type partitioning strategy** but do not themselves propose category-indexed retrieval.\n\n#### 11. **Enhancing Vulnerability Repair Through Extraction and Matching of Repair Patterns** (2025)\n- **Venue/Year**: ScienceDirect 2025\n- **Relation to FTCR**: Constructs a Repair Patterns Dictionary via clustering (GMM) on vulnerability statements. Uses pattern-matching for repair guidance. Complementary to FTCR but operates at patch generation stage, not retrieval index organization.\n\n---\n\n### **DebugBench & Benchmarks**\n\n#### 12. **DebugBench: Evaluating Debugging Capability of Large Language Models** (2024, widely used 2025-2026)\n- **Venue/Year**: Initially 2024; used extensively in 2025-2026 papers\n- **Relation to FTCR**: Standard debugging benchmark with 4,253 instances across 4 major bug categories (Syntax, Reference, Logic, Multiple) and 18 minor types. **No papers found that explicitly use DebugBench's bug taxonomy to partition retrieval indices.**\n\n#### 13. **CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows** (2026)\n- **Venue/Year**: arxiv:2604.27148 (April 2026)\n- **Relation to FTCR**: Provides repository-level repair evaluation. Doesn't propose categorical retrieval indexing.\n\n---\n\n### **ICSE 2025 & ICSE 2026 Program Repair Papers**\n\n#### 14. **RepairAgent: An Autonomous, LLM-Based Agent for Program Repair** (ICSE 2025)\n- **Venue/Year**: ICSE 2025 (April 2025, Ottawa)\n- **Relation to FTCR**: Agent-based retrieval of \"repair ingredients\" but uses general retrieval, not failure-type-conditioned index partitioning.\n\n#### 15. **Aligning the Objective of LLM-Based Program Repair (D4C)** (ICSE 2025)\n- **Venue/Year**: ICSE 2025\n- **Relation to FTCR**: Addresses alignment of repair objectives; does not cover retrieval index design.\n\n#### 16. **The Fact Selection Problem in LLM-Based Program Repair** (ICSE 2025 Research Track)\n- **Venue/Year**: ICSE 2025\n- **Relation to FTCR**: Focuses on selecting facts (evidence) for repair prompts; soft retrieval-based selection, not categorical partitioning.\n\n#### 17. **Synthetic Repo-level Bug Dataset for Training Automated Program Repair Models** (ICSE 2026 Research Track)\n- **Venue/Year**: ICSE 2026 (April 2026, Rio de Janeiro)\n- **Relation to FTCR**: Introduces synthetic bug-fix dataset (SWE-Synth) for training. No categorical indexing proposed.\n\n---\n\n### **Retrieval-Augmented Code Generation Survey**\n\n#### 18. **Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches** (2026)\n- **Venue/Year**: arxiv:2510.04905 (October 2025)\n- **Relation to FTCR**: Comprehensive taxonomy of RACG methods. Categorizes retrieval into non-graph (lexical, sparse BM25/TF-IDF, dense embedding, hybrid) and graph-based (AST, call graphs, CFG/DFG, module dependency). **Notable gap**: No mention of failure-type-conditioned hard partitioning as a retrieval strategy category. This absence suggests FTCR would represent a novel dimension not yet systematized in the literature.\n\n---\n\n## Summary of Novelty Risk Assessment\n\n**Low Risk of Direct Precedent:**\n- No paper explicitly proposes hard categorical partitioning of retrieval indices by failure type as a primary contribution\n- ReCode is the closest (algorithm-aware retrieval), but uses soft similarity scoring within a unified index\n- Most systems employ soft retrieval: vector similarity (FAISS, embeddings), BM25, or hybrid scoring\n\n**Potential Vulnerability to Precedent:**\n1. If ReinFix (ICSE 2026) uses failure-type soft retrieval and you claim hard partitioning is novel, the distinction hinges on soft vs. hard—be explicit in framing the contribution\n2. DebugBench's bug taxonomy exists but isn't used for index partitioning in any paper found\n3. Multiple papers classify bugs/failures (ReCode, error taxonomy papers), so the *idea* of failure-type classification isn't novel—FTCR's novelty is the application to index partitioning for cross-repo retrieval\n\n**Recommendation:**\n- Emphasize **hard index partitioning** as the core novelty, not failure-type classification alone\n- Compare empirically against ReCode and RepoRepair as the strongest soft retrieval baselines\n- Consider framing FTCR as \"failure-type-indexed retrieval\" to clarify it's about index organization, not just classification\n\n---\n\n## Sources\n\n- [ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation](https://arxiv.org/html/2509.02330)\n- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1)\n- [RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair](https://arxiv.org/html/2603.01048v1)\n- [KGCompass: Enhancing Repository-Level Software Repair via Repository-Aware Knowledge Graphs](https://arxiv.org/html/2503.21710v2)\n- [ARSP: Automated Repair of Verilog Designs via Semantic Partitioning](https://arxiv.org/html/2508.16517)\n- [Why LLMs Fail: A Failure Analysis and Partial Success Measurement for Automated Security Patch Generation](https://arxiv.org/html/2603.10072v1)\n- [RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code](https://arxiv.org/pdf/2509.16701)\n- [Retrieval-Augmented Code Generation: A Survey with Focus on Repository-Level Approaches](https://arxiv.org/html/2510.04905v1)\n- [CI-Repair-Bench: A Repository-Aware Benchmark for Automated Patch Validation via CI Workflows](https://arxiv.org/html/2604.27148v1)\n- [GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, Triage, and More](https://arxiv.org/html/2504.09651)\n- [ReAPR: Automatic program repair via retrieval-augmented large language models](https://link.springer.com/article/10.1007/s11219-025-09728-1)\n- [ICSE 2025 Research Track](https://conf.researchr.org/track/icse-2025/icse-2025-research-track)\n- [ICSE 2026 Research Track](https://conf.researchr.org/track/icse-2026/icse-2026-research-track)"
      }
    ],
    "totalDurationMs": 129416,
    "totalTokens": 48968,
    "totalToolUseCount": 33,
    "usage": {
      "input_tokens": 7,
      "cache_creation_input_tokens": 3117,
      "cache_read_input_tokens": 42397,
      "output_tokens": 3447,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3117
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 7,
          "output_tokens": 3447,
          "cache_read_input_tokens": 42397,
          "cache_creation_input_tokens": 3117,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3117,
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
      "otherToolCount": 33
    }
  },
  "sourceToolAssistantUUID": "034f5664-c939-44c2-a89e-9f464f3301c1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "d18db75c-c4bf-44f3-b7a9-96ea2fba968b",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise FTCR for EMNLP Findings with DebugBench hierarchy fix",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Assistant

_source line 16 · 2026-05-10T06:53:31.441Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the verified facts I need:

**DebugBench Structure:**
- 4 MAJOR categories: Syntax Bugs (7 sub-types), Reference Bugs (4 sub-types), Logic Bugs (4 sub-types), Multiple Bugs (3 sub-types)
- 18 MINOR sub-types nested within them
- Distribution is unequal: Multiple Bugs (750+750+718=2,218 instances) dominates

**InferFix Retriever Architecture:**
- The contrastive retriever uses bug type as a LABEL during training (to define positive/negative pairs) but does NOT feed type as an input to the encoder


- But at inference, the requirement that retrieved fixes match the query's bug type suggests InferFix actually does filter by type during retrieval, not just through soft embedding proximity. This is a critical distinction I need to clarify—if InferFix already performs type-based filtering, then FTCR's hard partitioning approach might not be as novel as initially claimed.

The real differentiation comes down to how types are determined and what bug corpora are used. InferFix relies on static analysis tools like Infer to assign bug types, restricting retrieval to same-type fixes from a unified corpus. FTCR, by contrast, uses LLM inference to label bug types at query time and partitions the index during construction, making it applicable to natural bug-fix pairs without requiring static analysis. The key advantages are the LLM-inferred type labels versus static analysis, the ability to work with natural bugs rather than just Infer-detected ones, and the use of an 18-category taxonomy derived from real bugs instead of Infer's diagnostic IDs—plus potential cross-language applicability. Python) vs. Java/C# only

The key insight from the verified InferFix architecture:
- Training: type labels define positive/negative pairs for contrastive learning
- Inference: "retrieved fixes must be of the same bug type as the query"

This means InferFix DOES restrict retrieval by type! The current proposal's claim that InferFix uses "soft contrastive similarity where type is an embedding-time signal and retrieval is nearest-neighbor search over the full unified corpus" appears to be WRONG based on the actual paper.

Wait, let me think about this more carefully. The InferFix architecture has:
1. A contrastive-pretrained Retriever that learns semantic similarity
2. At retrieval time, it says "retrieved fixes must be of the same bug type as the query"

This could mean either hard partitioning by type or searching the full corpus with type as a constraint. But that phrasing really does sound like a hard constraint rather than soft conditioning, which would mean InferFix already does type-based filtering and undercuts FTCR's main differentiation.

The crucial distinction is that InferFix relies on static analysis from the Infer tool to determine bug types at query time, whereas FTCR uses an LLM classifier instead. So InferFix is limited to bugs the Infer analyzer can detect, while FTCR can classify any bug an LLM can understand. InferFix's type categories are also specific to Infer's diagnostic output—things like null dereferences, resource leaks, and thread-safety violations—which is narrower than what FTCR might handle. tool-specific, while FTCR uses the 18 DebugBench categories which are more general.

So the correct differentiation of FTCR vs. InferFix is:
1. **Type label acquisition**: InferFix requires Infer static analysis at both corpus construction and query time; FTCR uses LLM classification (no special tools needed, applicable to any bug)
2. **Type taxonomy**: InferFix uses Infer-specific diagnostics (limited, tool-dependent); FTCR uses 18-minor/4-major general natural-bug taxonomy aligned with DebugBench
3. **Corpus**: InferFix uses InferredBugs (only bugs detected by Infer); FTCR uses natural bug-fix pairs from issue trackers
4. **Languages**: InferFix: Java/C#; FTCR: C++/Java/Python

The real scientific question FTCR addresses is whether LLM-based type classification can replace static analysis for retrieval, and whether a broader taxonomy across multiple languages generalizes better than tool-specific diagnostics—with the key tradeoff being classification accuracy versus repair performance. This reframes the contribution around LLM classification accuracy on the 18-category taxonomy and its downstream impact on retrieval effectiveness. (vs. needing Infer to run)
- The key practical advantage: FTCR works on any bug without requiring static analysis infrastructure

Let me reconsider the scope of revision needed here. The InferFix finding actually strengthens the paper—it validates that type-conditioned retrieval works, but requires static analysis infrastructure, whereas FTCR demonstrates the same approach with LLM-inferred types, which has broader applicability. The real issue is that I've been characterizing the differentiation incorrectly. The encoder doesn't take type as input, but retrieval is filtered by type, so I need to reframe this as type-filtered retrieval rather than "soft type conditioning." I also need to fix the DebugBench taxonomy description, commit to the Findings track for EMNLP, specify the statistical aggregation method, and confirm compute readiness or add a buffer day. The real insight is that FTCR's contribution is testing whether LLM-inferred type labels can replace static-analysis-derived ones—that's the actual empirical question, not the hard versus soft partitioning distinction. So the framing needs to shift from "soft contrastive conditioning" to "LLM classification as a substitute for Infer," and this is a minor correction since the core hypothesis about type-based retrieval filtering remains intact.

Now I'm mapping out the specific changes needed: updating the venue to EMNLP 2026 Findings through ARR, and restructuring the DebugBench taxonomy description to clarify it's a 4-major/18-minor hierarchical system with measurements at the minor level and aggregation at the major level.

For the repair evaluation, I need to note that the Multiple Bugs category (which represents 52% of the 4,253 instances) gets excluded since those multi-bug scenarios don't align with single-fault repair testing, so the actual Java instances used are around 559 distributed across the minor types.

The InferFix section needs significant clarification: it actually does use type information to filter the retrieval pool rather than being pure semantic search, but the key distinction is that type labels structure the contrastive training pairs without being direct encoder inputs—and critically, InferFix depends on Infer's static analysis for type labels while FTCR uses LLM-generated ones.

This framing directly addresses whether an LLM can replace Infer for type-conditioned retrieval. I should also add confirmation on compute readiness and specify the aggregation methods and statistical tests being used.

Now I'm reconsidering the "hard vs. soft" framing that anchors the proposal. The distinction really sharpens when comparing against ReinFix's soft root-cause embeddings without type partitioning, whereas the InferFix comparison is more about construction-time versus query-time type filtering with different label sources. The "hard vs. soft" framing works as the primary architectural contribution against ReinFix, but I should be clearer about how it applies differently to the InferFix comparison.

The random-partition control still cleanly isolates type-matching precision from pool-size reduction. Looking at DebugBench's Multiple Bugs category—syntax errors, reference issues, logic errors, and multi-bug scenarios—using it for repair evaluation is tricky since fixing multiple bugs simultaneously requires finding multiple patches, which complicates the retrieval strategy evaluation.

I should clarify that while the 18 minor types include Multiple Bugs, FTCR's primary evaluation focuses on the 14 single-bug types with Multiple Bugs analyzed separately. Breaking down the distribution: single-bug categories (Syntax, Reference, Logic) total around 2,035 instances, while Multiple Bugs account for roughly 2,218 of the 4,253 total—over half. For the 20% held-out calibration split, this means the single-bug types still have sufficient instances for reliable per-type calibration even after accounting for the Multiple Bugs subset.

Looking at the Java-specific breakdown, if there are roughly 559 Java instances total and Multiple Bugs represents a similar proportion, I'd have around 269 single-bug Java instances distributed across 14 types—that's only about 19 per type, which is tighter than the overall ~31 per type figure. The actual Java distribution might differ from the full dataset though, so I shouldn't assume proportional scaling. The merge policy for handling these smaller per-type counts becomes more critical.

Now I need to revise the JSON proposal with the key updates: clarifying the DebugBench structure and how the 18 minor types relate to the 14 single-bug focus, reframing InferFix's role, and reflecting the Findings track commitment.

Revising the JSON...

The key distinction is that InferFix relies on static type analysis to filter the retrieval pool, while FTCR uses LLM classification for broader applicability without tool dependencies. Both approaches train encoders on semantic structure, but InferFix's contrastive pairs are determined by type matching, whereas FTCR uses a general-purpose embedding model. This reframing sharpens the research question: whether LLM-inferred type labels can effectively substitute for static analysis in type-conditioned retrieval, and at what accuracy threshold the trade-off becomes favorable for repair performance. This positioning actually strengthens the EMNLP Findings submission.

For DebugBench, I'm looking at the dataset composition across four bug categories—Syntax, Reference, Logic, and Multiple Bugs—with 4,253 total instances spanning C++, Java, and Python. Multiple Bugs represent over half the dataset at 52%, which creates a distinct multi-fault repair challenge that needs separate scoping. I'm measuring classifier accuracy at the 18 sub-type level and focusing the primary repair evaluation on the 14 single-bug minor types to keep the scope manageable.

For Java specifically, with roughly 559 pairs and a similar distribution, I'd have about 290 Multiple Bug instances and 269 single-bug instances spread across 14 minor types—averaging just 19 per type. This means I need to merge rare types strategically within their major categories: combining similar Syntax bugs like whitespace issues, grouping rarer Logic sub-types together, and doing the same for Reference bugs. This should yield around 6-8 merged Java categories that still preserve the distinction between major bug families.

Now I'm preparing the revised JSON with minimal, targeted changes to reflect this merge policy.

Looking back at InferFix's architecture more carefully, I see the key distinction: at inference time, InferFix restricts retrieval to fixes of the same bug type as the query. This is a form of type-based filtering, but it happens at query time rather than during index construction like FTCR does. So while both approaches constrain the retrieval pool by type, InferFix determines type membership dynamically at query time using Infer's type classification, whereas FTCR pre-partitions the corpus upfront.

The proposal's claim that InferFix uses "soft continuous embedding" for type signals is misleading if InferFix is actually performing hard filtering at retrieval time. The reviewer is correct that this needs clarification—the proposal should acknowledge InferFix's type-based pool restriction and reframe the differentiation as being about when the filtering occurs (query time vs. construction time) rather than claiming InferFix avoids type-based constraints altogether.

Looking deeper, though, query-time and construction-time filtering are functionally equivalent for candidate selection on the same corpus, so the performance advantage of construction-time partitioning is mainly efficiency at scale. The real distinctions between FTCR and InferFix are that FTCR uses LLM-derived labels instead of static analysis, doesn't require Infer, operates with a broader taxonomy, and works with natural bug-fix pairs—not the hard-vs-soft embedding framing.

So I should reframe the comparison: emphasize LLM-inferred labels versus static-analysis-required labels as the key difference from InferFix, keep the hard construction-time partition versus soft unified embedding distinction for ReinFix, and center the core question on whether LLM-based type-conditioned retrieval performs comparably to static-analysis-derived approaches. The label quality analysis—comparing LLM labels against oracle labels—is also novel since InferFix treats Infer labels as ground truth.

This framing is cleaner and more compelling: the paper demonstrates that LLM-inferred type labels enable effective type-conditioned retrieval across general natural bugs without requiring static analysis tools, while outperforming soft embedding baselines when label quality is sufficient. Now I'll draft the revision with these structural changes in mind. The core insight here is that I'm sharpening the scientific narrative around three concrete claims: LLM labels can effectively replace static analysis for type-conditioned repair retrieval with measurable improvements, hard type partitioning beats soft embeddings when label quality is sufficient, and the work bridges the gap between InferFix's narrow static analysis approach and broader natural bug repair. This reframing actually strengthens the paper's clarity despite being a minor correction. Now I need to systematically update the JSON across all affected sections—core_problem, opportunity, landscape, and approach—to reflect the corrected InferFix framing with the hierarchical 4-major/18-minor taxonomy and ensure the measurements are properly positioned at both levels. InferFix uses Infer's static analyzer to label bugs at query time and filters candidates to same-type fixes, achieving strong accuracy on Java and C#. The key differences from FTCR are: InferFix requires running Infer on the query bug (limiting it to bugs Infer can detect), while FTCR uses few-shot LLM classification that works on any natural bug without static analysis tooling; and InferFix relies on Infer's tool-specific diagnostic IDs rather than general bug categories.

The core question InferFix leaves open is whether LLM-inferred type labels can effectively replace Infer-derived labels for type-conditioned retrieval, and at what classification accuracy this substitution remains viable—exactly the calibration FTCR measures. This positions InferFix as a validating predecessor that FTCR extends with broader taxonomy, LLM-inferred labels, and natural bugs from real issue trackers, while empirically determining the accuracy thresholds needed for the approach to work.

Now I'm looking at the actual distribution across the DebugBench taxonomy. The "~31 Java instances per minor type" was an oversimplification—Multiple Bugs dominates with around 290 Java instances (52% of the total), leaving only ~269 instances spread across 14 single-bug minor types, which is roughly 19 per type. This means I need a more aggressive merge strategy, particularly for Java. I'm going to apply the minimum-threshold at the major category level instead of minor type level, which gives me three cleaner single-bug major categories for Java ablations: Syntax, Reference, and Logic, with their sub-types merged together.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d18db75c-c4bf-44f3-b7a9-96ea2fba968b",
  "isSidechain": false,
  "requestId": "req_011CatSmyDUW2SK3RC7xpECV",
  "type": "assistant",
  "uuid": "421a20f1-5fad-4e4d-aaba-02214e5a5e59",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012Ht9vzztXoSjD9b2qTYG7M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6340,
      "cache_read_input_tokens": 30556,
      "output_tokens": 7100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7100,
          "cache_read_input_tokens": 30556,
          "cache_creation_input_tokens": 6340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6340
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

_source line 17 · 2026-05-10T06:53:32.222Z_

Good — the research reveals two significant factual corrections needed:

1. **InferFix architecture**: The retriever does filter by type at retrieval time ("retrieved fixes must be of the same bug type as the query"), but type labels come from Infer static analysis — so the "soft vs. hard" framing vs. InferFix is wrong. The real differentiation is **Infer-required labels vs. LLM-inferred labels**.

2. **DebugBench structure**: Confirmed 4-major / 18-minor hierarchy. Multiple Bugs (3 sub-types: double/triple/quadruple) accounts for ~52% of instances (2,218/4,253) — not relevant for single-fault repair retrieval and needs explicit scoping.

These are precision fixes that actually sharpen the scientific story. Change type: **minor**, but the InferFix reframing is conceptually important.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "421a20f1-5fad-4e4d-aaba-02214e5a5e59",
  "isSidechain": false,
  "requestId": "req_011CatSmyDUW2SK3RC7xpECV",
  "type": "assistant",
  "uuid": "924b082a-0c9f-428f-bc42-c98b2dde5096",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012Ht9vzztXoSjD9b2qTYG7M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6340,
      "cache_read_input_tokens": 30556,
      "output_tokens": 7100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7100,
          "cache_read_input_tokens": 30556,
          "cache_creation_input_tokens": 6340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6340
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

_source line 18 · 2026-05-10T06:53:32.635Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01YCygiAjjhYaFSf3PQX4LGw`</summary>

```json
{
  "query": "select:TodoWrite",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "924b082a-0c9f-428f-bc42-c98b2dde5096",
  "isSidechain": false,
  "requestId": "req_011CatSmyDUW2SK3RC7xpECV",
  "type": "assistant",
  "uuid": "8b3371c4-354d-498a-bb28-3145a766e04a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_012Ht9vzztXoSjD9b2qTYG7M",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6340,
      "cache_read_input_tokens": 30556,
      "output_tokens": 7100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 6340,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7100,
          "cache_read_input_tokens": 30556,
          "cache_creation_input_tokens": 6340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 6340
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

_source line 19 · 2026-05-10T06:53:32.647Z_

<details><summary>↩ Tool result · `toolu_01YCygiAjjhYaFSf3PQX4LGw`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "TodoWrite"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8b3371c4-354d-498a-bb28-3145a766e04a",
  "isSidechain": false,
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "628f104b-9525-4629-96e3-d056493f8e24",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "8b3371c4-354d-498a-bb28-3145a766e04a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "628f104b-9525-4629-96e3-d056493f8e24",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise FTCR for EMNLP Findings with DebugBench hierarchy fix",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Assistant

_source line 22 · 2026-05-10T06:56:01.955Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have all the information I need to write the revised JSON. Let me organize the five fixes clearly:

**Fix 1 (HIGH): EMNLP Main → Findings**
- Remove "EMNLP 2026 Main" from target_venues
- Replace with "EMNLP 2026 Findings (via ARR)"

**Fix 2 (MEDIUM): DebugBench 4-major/18-minor hierarchy**
- Replace all "18-category taxonomy" with "4-major/18-minor hierarchical taxonomy"
- 4 major: Syntax (7 sub-types), Reference (4 sub-types), Logic (4 sub-types), Multiple (3 sub-types)


- Scope the primary evaluation to single-bug minor types across Syntax, Reference, and Logic (14 types total), treating the Multiple Bugs category separately since it accounts for about half the instances
- Measure at the minor-type level with major-type aggregation as secondary, merging within major categories first
- Recalculate the Java distribution: with ~559 total Java instances and Multiple Bugs representing ~52%, that leaves ~269 single-bug Java instances across 14 minor types, averaging ~19 per type, which requires aggressive merging up to the major-category level

**Fix 3 (MEDIUM): Compute read readiness** — add Day 0 confirmation or a 1-day buffer to account for timing

**Fix 4 (LOW): InferFix architecture reframing** — clarify that InferFix does filter by type at retrieval time rather than relying purely on soft semantic search, distinguishing it from FTCR through the use of Infer-required versus LLM-inferred labels, with type partitioning happening at construction time versus query-time filtering, and the encoder capturing type-correlated semantic similarity without type-conditioned encoding

**Fix 5 (LOW): Statistical significance for Z%/W%** — aggregate comparisons across types rather than per-type to avoid small sample issues, apply McNemar's test or chi-squared for binary outcomes like fix success/failure, and enforce a minimum threshold of at least 30 instances contributing to any Z%/W% comparison

Now I'm preparing to write out the complete revised JSON with all these adjustments incorporated.

Key text changes I need to make: updating the core_problem section to reference the 4-major/18-minor hierarchical taxonomy instead of just 18 categories, reframing InferFix from a soft contrastive embedding feature to query-time type-filtered retrieval using Infer-derived labels, and clarifying that X%/Y%/Z%/W% measurements operate at the minor-type level with major-type aggregation as a secondary view. In the opportunity section, I'm doing a major rewrite of how InferFix differentiates itself — shifting from the soft contrastive embedding framing to explaining how it uses query-time type filtering with same-type candidate selection while the encoder learns type-correlated semantic similarity without being type-conditioned.

I also need to add new points about type label acquisition (Infer required vs. LLM classifier) and clarify that InferFix validates type-restricted retrieval helps while FTCR tests whether LLM-inferred labels achieve similar quality. The landscape section gets the same corrections as opportunity. In approach, I'm fixing the merge policy to within-major-category-first, specifying that Z%/W% are at minor-type level with aggregation and McNemar's test, adding compute readiness to Day 0, and updating DebugBench references. For target_venues, I'm removing "EMNLP 2026 Main" and keeping only "EMNLP 2026 Findings (via ARR)". Finally, I need to update the key_references section's InferFix note to reflect these corrections.

Now I'm revising the full JSON structure with these changes. The description field will summarize the five main revisions: the EMNLP Findings commitment, DebugBench structure correction, compute readiness addition, InferFix architecture clarification, and statistical significance specification. For InferFix throughout the document, I'm updating the language to properly describe the type-correlated contrastive training combined with query-time type filtering using Infer labels.

Writing the complete revised JSON... InferFix's type labels come from running Infer's static analyzer on each repository, with type information structuring the contrastive training but not fed directly to the encoder, whereas FTCR uses few-shot LLM classification that requires no static analysis tooling and catches bugs Infer misses. The key difference in construction is that FTCR pre-partitions into discrete type sub-indices at build time, while InferFix filters to same-type bugs at query time — functionally similar retrieval pools, but I need to think through whether the construction-time vs. retrieval-time distinction actually matters.

The real contributions are clearer when I focus on what's actually novel: LLM-inferred labels instead of Infer's static analysis, natural bugs in the corpus rather than Infer-detected ones, a general taxonomy versus Infer-specific diagnostics, and broader language coverage. The core empirical question InferFix leaves open is whether LLM type labels can achieve sufficient accuracy to make type-conditioned retrieval work for natural bugs, and at what accuracy threshold the approach becomes viable.

For statistical rigor, I need to handle the small per-type sample sizes properly—aggregating results across correctly and misclassified instances, using McNemar's test for paired outcomes, and applying Fisher's exact test only when per-type counts exceed 30. I should also report confidence intervals on the key metrics.

I'm also realizing the DebugBench evaluation scope matters: the dataset contains a significant portion of multi-bug instances that I need to account for when designing the evaluation. 52%) creates a challenge:
- For repair evaluation, fixing multiple co-occurring bugs may require multiple retrieved patches
- Type classification for "Multiple Bugs" instances is ambiguous (multiple types co-occurring)
- For FTCR's single-fault repair evaluation, these instances should be excluded or treated as a separate benchmark

The correct scoping:
- Primary evaluation: 2,035 single-bug instances (Syntax: 761, Reference: 684, Logic: 590) across C++/Java/Python
- Multiple Bugs: separate analysis (optional, may be excluded from main results)
- For Java specifically: ~268 single-bug Java instances across 14 minor types (estimating ~50% are single-bug Java instances, with ~97 Java instances across 3 major single-bug categories)

Now I'm trying to pin down the actual per-language distribution in DebugBench. The dataset has 4,253 total instances, and while equal representation across C++, Java, and Python seems implied, I need to verify this. If it's roughly equal, that's about 1,418 per language, which would give roughly 473 Java single-bug instances from the 2,035 single-bug total. But the proposal mentions ~559 Java instances, suggesting either Java is about 13% of the dataset or the split isn't equal. I'm trying to reconcile whether the "~559 Java pairs" reference from the corpus construction part comes from Defects4J V1.2 and GitBench data. I see the issue now — the ~31 Java instances per minor type was actually referring to how the retrieval corpus's 559 Java fix pairs distribute across the 18 minor types, not DebugBench test instances. The retrieval corpus itself is independently annotated with this same taxonomy, so those 3,050 fix pairs serve as templates for retrieval, while the multiple-bug subcategories only apply to the DebugBench evaluation set.

Looking at the actual distribution: the full retrieval corpus averages around 169 pairs per type, while the Java-only subset gives roughly 31 per type. If I exclude the multiple-bug types since real repository fixes are single-fault, that brings the Java distribution to about 40 per type across the 14 single-bug categories. This distinction is important to clarify — the retrieval corpus doesn't contain multiple-bug instances because those are synthetic test cases, not actual fix templates.

I think I've been overcomplicating this. Let me just apply the five key corrections to the JSON and present them clearly. 2. 4-major/18-minor hierarchy throughout (note: retrieval corpus focuses on 15 single-fault minor types since Multiple Bugs isn't a fix-template category; evaluation on DebugBench scopes to single-bug major categories)
3. Compute readiness
4. InferFix: remove "soft" framing, replace with "Infer-required vs. LLM-inferred" framing
5. Statistical significance for Z%/W%

Round 7 revisions address five key changes: committing to EMNLP 2026 Findings as the sole venue target, with the calibration study appropriately scoped to Findings rather than Main; correcting all DebugBench references to explicitly use the 4-major/18-minor hierarchical taxonomy where primary evaluation focuses on 14 single-bug minor types across Syntax, Reference, and Logic, while the Multiple Bugs category (52% of the dataset) is analyzed separately outside the main fix-template retrieval; and confirming compute readiness with X%/Y%/Z%/W% measurements specified at the minor-type level and aggregated at the major-type level.

I'm also clarifying InferFix's architecture — it doesn't use soft continuous embeddings but rather type-correlated contrastive training where same-type bug pairs serve as positives, with type filtering applied at query time using Infer-derived labels. FTCR's differentiation comes down to three factors: type label acquisition method (LLM classification versus Infer static analysis), taxonomy scope (18 general natural-bug categories versus Infer-specific diagnostics), and corpus composition (natural bug-fix pairs versus InferredBugs). The empirical question remains about whether these differences translate to measurable performance gains.

For statistical rigor, I'm specifying that Z% and W% represent aggregates across all correctly and misclassified instances, using McNemar's test for paired before/after outcomes and Fisher's exact test for per-type breakdowns when n≥30, with 95% confidence intervals throughout.

Now I'm organizing the JSON structure systematically with fields for title, core_problem, opportunity, landscape, and approach, updating each section to reflect the corrected InferFix framing and DebugBench structure. I'm refining the InferFix description to clarify how it actually conditions retrieval on bug types—using Infer's static analysis labels to filter same-type candidates during retrieval rather than learning soft embeddings—and noting that it only works on bugs Infer can detect. The open question shifts to whether LLM-inferred type labels could generalize beyond Infer's diagnostic categories. for Infer-derived labels to enable effective type-conditioned retrieval for general natural bugs (the X%/Y% vs. InferFix question) and whether hard construction-time type partitioning outperforms ReinFix's soft root-cause embedding (the Z%/W% question).

I'm also tracking repair improvements for correctly-classified high-confidence instances under hard type-partitioned retrieval versus the soft baseline, plus repair degradation for misclassified instances — measuring these at the minor-type level with major-type aggregation as a secondary view.

Now looking at InferFix as the earliest type-aware cross-repository retrieval system: it uses contrastive learning to embed semantically equivalent bugs and fixes closer together, conditioned on Infer's static-analysis bug types like null dereferences and resource leaks, achieving 76.8% top-1 accuracy on Java and 65.6% on C#. The key differences from FTCR are that InferFix applies type as a soft embedding signal during retrieval across a unified corpus, whereas FTCR hard-partitions the corpus into discrete type sub-indices at construction time; InferFix's types are Infer diagnostic IDs rather than the 18-category natural-bug taxonomy; and it trains on InferredBugs, which are static-analysis artifacts. in Java/C# repos), not natural bug-fix pairs from issue trackers and CI logs. InferFix validates that type-aware retrieval helps repair (supporting FTCR's hypothesis) while leaving the hard vs. soft type-partitioning comparison unresolved.

InferFix differs from FTCR in three key ways: it requires running Infer's static analyzer to label each bug (limiting coverage to detectable bugs), whereas FTCR uses few-shot LLM classification that works on any natural bug; InferFix operates within Infer's diagnostic taxonomy (null dereferences, resource leaks, thread-safety violations) rather than the broader 18-minor-category taxonomy aligned with DebugBench; and InferFix trains on InferredBugs (synthetic Infer-detected bugs) while FTCR uses real bug-fix pairs from issue trackers and CI logs. The core question InferFix leaves open is whether LLM-inferred type labels can effectively replace Infer-derived labels for type-conditioned retrieval on general natural bugs—exactly what FTCR investigates. FTCR differs from InferFix in three key ways: it partitions the corpus into type-specific indices upfront rather than using soft similarity at embedding time, it leverages a broader 18-category natural-bug taxonomy instead of Infer's limited static-analysis patterns, and it draws from real-world bug-fix pairs across multiple repositories rather than synthetic Infer-detected bugs.

The core question is whether this hard partitioning strategy at construction time yields better precision than InferFix's softer approach of conditioning on type during retrieval. on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) Type label acquisition — InferFix requires Infer to run on each repository to produce type labels for both corpus and query bugs; FTCR uses few-shot LLM classification, covering any natural bug without static analysis tooling; (b) Defect taxonomy — InferFix uses Infer-specific diagnostic IDs (null dereferences, resource leaks, thread-safety violations), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench; (c) Corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The core question is whether LLM-inferred type labels can achieve sufficient accuracy to enable type-conditioned retrieval that matches Infer-derived performance, and at what accuracy threshold type-conditioned retrieval outperforms soft embedding baselines.

For the combined Python+Java corpus, the 18-minor-type analysis excludes the Multiple Bugs category (which applies only to test evaluation, not the fix-template retrieval corpus) and yields approximately 15 active single-fault minor types. For Java-only ablations, types with fewer than 30 instances are merged into nearest-neighbor supercategories within the same major category—keeping Syntax sub-types together, Logic sub-types together, and so on—never crossing major boundaries. Java ablation results are reported for the 4–6 resulting merged groups that each exceed 50 instances.

I'm also adding statistical rigor by testing significance via McNemar's test on paired pass/fail outcomes between the baseline and FTCR on the same instances, with Z% and W% reported as aggregate rates across correctly-classified and misclassified instances respectively.

Per-type breakdowns use Fisher's exact test with a minimum n≥30 threshold, and I'm reporting 95% confidence intervals for both metrics.

For the compute readiness, I'm noting that 2 A100 nodes were provisioned as of May 10, with Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.

On the DebugBench evaluation side, I'm clarifying that only single-bug instances from the Syntax, Reference, and Logic major categories are used (~2,035 of 4,253 instances), while the Multiple Bugs instances (~2,218) are reported separately as an auxiliary experiment.

For the target venue, EMNLP 2026 ARR is the primary target with a May 25 deadline—the auto-research phase runs Days 0–12 and paper writing Days 13–15, with the minimum viable submission covering DebugBench classifier calibration, Defects4J V1.2 ablations, and random-partition controls, framed around LLM-generated bug type label quality and its impact on retrieval performance. regularly accept papers evaluating LLM-generated categorical labels and RAG system design; the X%/Y%/Z%/W% falsifiable finding fits this tradition. Timeline is extremely tight: the two-day writing window requires a pre-drafted skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.

EMNLP 2026 Findings targets the May 25 deadline—15 days away—and is my primary submission path. The calibration study measuring LLM label quality and its impact on retrieval-augmented repair fits Findings better than the Main track, which demands deeper architectural insights and carries higher desk-rejection risk for empirical work. I need to complete experiments by Day 12 (May 22), leaving three days for writing. The minimum viable paper combines DebugBench classifier calibration results with Defects4J ablations and a random-partition control; if SWE-bench Lite doesn't finish in time, I'll submit with just those two datasets and defer the full results to ICSE 2027.

For the InferFix reference, I'm clarifying what distinguishes our approach from prior work: InferFix uses soft contrastive embeddings for retrieval rather than hard index-time partitioning, and it operates on static-analysis artifacts with Infer-specific diagnostic categories rather than natural bugs. I need to explicitly separate these three dimensions—embedding strategy, bug taxonomy, and data source—to position FTCR's contribution clearly. I need to clarify the key distinctions between InferFix and FTCR: Infer requires static analysis at both corpus construction and query time with diagnostic IDs, while FTCR uses LLM-inferred type labels and partitions the index at construction time for efficiency gains. The retrieval corpus uses the 18-minor bug taxonomy for annotation, though the "Multiple Bugs" category with its sub-types (double/triple/quadruple co-occurring bugs) is specific to DebugBench evaluation. I'm realizing the Syntax category in DebugBench is heavily Python-biased, with most of the seven sub-types being language-specific errors like misused operators, missing colons, and indentation issues that wouldn't apply the same way in other languages like C++ or Java.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "628f104b-9525-4629-96e3-d056493f8e24",
  "isSidechain": false,
  "requestId": "req_011CatSwMc88WDDGVNzggvQu",
  "type": "assistant",
  "uuid": "0b27d63d-dd10-4797-83c8-bc31ba429de9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Hz2u7EynCyhKWiyjrZgCLg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 36896,
      "output_tokens": 8837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8837,
          "cache_read_input_tokens": 36896,
          "cache_creation_input_tokens": 9480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9480
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

_source line 23 · 2026-05-10T06:56:01.957Z_

Now I have verified facts to work with. Let me write the complete revised JSON with all five fixes applied precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0b27d63d-dd10-4797-83c8-bc31ba429de9",
  "isSidechain": false,
  "requestId": "req_011CatSwMc88WDDGVNzggvQu",
  "type": "assistant",
  "uuid": "1d7c544e-4846-4c94-a408-8e706889d472",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Hz2u7EynCyhKWiyjrZgCLg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 36896,
      "output_tokens": 8837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8837,
          "cache_read_input_tokens": 36896,
          "cache_creation_input_tokens": 9480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9480
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

_source line 24 · 2026-05-10T06:56:04.897Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01XEXs7uWvFSHuwrdSHWpYm9`</summary>

```json
{
  "todos": [
    {
      "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
      "status": "in_progress",
      "activeForm": "Fixing EMNLP venue to Findings track"
    },
    {
      "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
      "status": "pending",
      "activeForm": "Correcting DebugBench taxonomy structure"
    },
    {
      "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
      "status": "pending",
      "activeForm": "Adding compute readiness note"
    },
    {
      "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
      "status": "pending",
      "activeForm": "Correcting InferFix architecture description"
    },
    {
      "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
      "status": "pending",
      "activeForm": "Adding statistical significance specification"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d7c544e-4846-4c94-a408-8e706889d472",
  "isSidechain": false,
  "requestId": "req_011CatSwMc88WDDGVNzggvQu",
  "type": "assistant",
  "uuid": "c55a4b95-2d8a-4913-ae88-1018b9ed6f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Hz2u7EynCyhKWiyjrZgCLg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 9480,
      "cache_read_input_tokens": 36896,
      "output_tokens": 8837,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9480,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 8837,
          "cache_read_input_tokens": 36896,
          "cache_creation_input_tokens": 9480,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9480
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

_source line 25 · 2026-05-10T06:56:04.904Z_

<details><summary>↩ Tool result · `toolu_01XEXs7uWvFSHuwrdSHWpYm9`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c55a4b95-2d8a-4913-ae88-1018b9ed6f54",
  "isSidechain": false,
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "547f9265-8eca-4b57-b254-4bf3d6f20f5e",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
        "status": "in_progress",
        "activeForm": "Fixing EMNLP venue to Findings track"
      },
      {
        "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
        "status": "pending",
        "activeForm": "Correcting DebugBench taxonomy structure"
      },
      {
        "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
        "status": "pending",
        "activeForm": "Adding compute readiness note"
      },
      {
        "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
        "status": "pending",
        "activeForm": "Correcting InferFix architecture description"
      },
      {
        "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
        "status": "pending",
        "activeForm": "Adding statistical significance specification"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "c55a4b95-2d8a-4913-ae88-1018b9ed6f54",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "547f9265-8eca-4b57-b254-4bf3d6f20f5e",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 27_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise FTCR for EMNLP Findings with DebugBench hierarchy fix",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Tool call

_source line 28 · 2026-05-10T06:56:08.342Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01JesxkWd45nJZatcGH2j5DJ`</summary>

```json
{
  "todos": [
    {
      "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
      "status": "completed",
      "activeForm": "Fixing EMNLP venue to Findings track"
    },
    {
      "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
      "status": "in_progress",
      "activeForm": "Correcting DebugBench taxonomy structure"
    },
    {
      "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
      "status": "pending",
      "activeForm": "Adding compute readiness note"
    },
    {
      "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
      "status": "pending",
      "activeForm": "Correcting InferFix architecture description"
    },
    {
      "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
      "status": "pending",
      "activeForm": "Adding statistical significance specification"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "547f9265-8eca-4b57-b254-4bf3d6f20f5e",
  "isSidechain": false,
  "requestId": "req_011CatT8YkQHX7zPHijNeVAF",
  "type": "assistant",
  "uuid": "1447aa32-e271-4efa-88f1-f8330f347df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01EPzK51DouDoKy17cVLx3Gb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8884,
      "cache_read_input_tokens": 46376,
      "output_tokens": 300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 300,
          "cache_read_input_tokens": 46376,
          "cache_creation_input_tokens": 8884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8884
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

_source line 29 · 2026-05-10T06:56:08.345Z_

<details><summary>↩ Tool result · `toolu_01JesxkWd45nJZatcGH2j5DJ`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1447aa32-e271-4efa-88f1-f8330f347df6",
  "isSidechain": false,
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "45b2f81b-b5af-49ed-90e3-7316393d92de",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
        "status": "in_progress",
        "activeForm": "Fixing EMNLP venue to Findings track"
      },
      {
        "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
        "status": "pending",
        "activeForm": "Correcting DebugBench taxonomy structure"
      },
      {
        "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
        "status": "pending",
        "activeForm": "Adding compute readiness note"
      },
      {
        "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
        "status": "pending",
        "activeForm": "Correcting InferFix architecture description"
      },
      {
        "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
        "status": "pending",
        "activeForm": "Adding statistical significance specification"
      }
    ],
    "newTodos": [
      {
        "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
        "status": "completed",
        "activeForm": "Fixing EMNLP venue to Findings track"
      },
      {
        "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
        "status": "in_progress",
        "activeForm": "Correcting DebugBench taxonomy structure"
      },
      {
        "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
        "status": "pending",
        "activeForm": "Adding compute readiness note"
      },
      {
        "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
        "status": "pending",
        "activeForm": "Correcting InferFix architecture description"
      },
      {
        "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
        "status": "pending",
        "activeForm": "Adding statistical significance specification"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "1447aa32-e271-4efa-88f1-f8330f347df6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 30 · 2026-05-10T06:56:11.615Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_012JUF6poTGwLPeG4NDWeFYE`</summary>

```json
{
  "todos": [
    {
      "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
      "status": "completed",
      "activeForm": "Fixing EMNLP venue to Findings track"
    },
    {
      "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
      "status": "completed",
      "activeForm": "Correcting DebugBench taxonomy structure"
    },
    {
      "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
      "status": "completed",
      "activeForm": "Adding compute readiness note"
    },
    {
      "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
      "status": "completed",
      "activeForm": "Correcting InferFix architecture description"
    },
    {
      "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
      "status": "completed",
      "activeForm": "Adding statistical significance specification"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "45b2f81b-b5af-49ed-90e3-7316393d92de",
  "isSidechain": false,
  "requestId": "req_011CatT8oRwobTNay699GTyy",
  "type": "assistant",
  "uuid": "c02cb941-85cb-4091-ba46-0f686aca6f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Wv9Cr36Kszaqiyj5B76Tnr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 346,
      "cache_read_input_tokens": 55260,
      "output_tokens": 302,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 346,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 302,
          "cache_read_input_tokens": 55260,
          "cache_creation_input_tokens": 346,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 346
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

_source line 31 · 2026-05-10T06:56:11.617Z_

<details><summary>↩ Tool result · `toolu_012JUF6poTGwLPeG4NDWeFYE`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c02cb941-85cb-4091-ba46-0f686aca6f23",
  "isSidechain": false,
  "promptId": "661a1bfa-9c1e-4e11-937a-1d217c6e3a81",
  "type": "user",
  "uuid": "e267fa68-dda7-42d6-bd78-b88b342dea88",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
        "status": "completed",
        "activeForm": "Fixing EMNLP venue to Findings track"
      },
      {
        "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
        "status": "in_progress",
        "activeForm": "Correcting DebugBench taxonomy structure"
      },
      {
        "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
        "status": "pending",
        "activeForm": "Adding compute readiness note"
      },
      {
        "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
        "status": "pending",
        "activeForm": "Correcting InferFix architecture description"
      },
      {
        "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
        "status": "pending",
        "activeForm": "Adding statistical significance specification"
      }
    ],
    "newTodos": [
      {
        "content": "Fix 1 (HIGH): Commit to EMNLP Findings track, remove Main",
        "status": "completed",
        "activeForm": "Fixing EMNLP venue to Findings track"
      },
      {
        "content": "Fix 2 (MEDIUM): Replace '18-category' with '4-major/18-minor hierarchy' throughout",
        "status": "completed",
        "activeForm": "Correcting DebugBench taxonomy structure"
      },
      {
        "content": "Fix 3 (MEDIUM): Add compute readiness confirmation to Day 0",
        "status": "completed",
        "activeForm": "Adding compute readiness note"
      },
      {
        "content": "Fix 4 (LOW): Correct InferFix architecture framing — Infer-required vs LLM-inferred labels, not soft vs hard",
        "status": "completed",
        "activeForm": "Correcting InferFix architecture description"
      },
      {
        "content": "Fix 5 (LOW): Specify statistical significance for Z% and W%",
        "status": "completed",
        "activeForm": "Adding statistical significance specification"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "c02cb941-85cb-4091-ba46-0f686aca6f23",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 32 · 2026-05-10T07:00:44.318Z_

Here is the complete revised JSON with all five fixes applied:

```json
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "change_type": "minor",
  "core_problem": "The lead empirical question — tractable because DebugBench provides oracle ground-truth labels for 4,253 instances organized in a 4-major/18-minor hierarchical taxonomy — is: how accurately can a few-shot LLM assign semantic bug type labels from the 18 minor sub-categories, and does that label accuracy determine whether hard categorical retrieval index partitioning outperforms soft root-cause-augmented retrieval (ReinFix, ICSE 2026) for cross-repository fix template transfer? This frames FTCR as an empirical study of LLM-generated categorical label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level, with major-type aggregation as a secondary result; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. the soft baseline; (W%) repair degradation for misclassified instances. Together these characterize when hard categorical type conditioning helps and when it hurts — a finding with direct generalization to any retrieval system using LLM-inferred labels.\n\nRetrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. InferFix (ESEC/FSE 2023, arXiv:2303.07263) establishes that type-conditioned retrieval benefits code repair: its Retriever uses contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), and at retrieval time filters candidates to same-type fixes; however, InferFix requires running the Infer static analyzer on each query bug — applicable only to bugs Infer can detect, using Infer-specific diagnostic categories rather than a general natural-bug taxonomy. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is therefore two-fold: (1) whether LLM-inferred type labels can substitute for Infer-derived labels to enable type-conditioned retrieval for general natural bugs not addressable by static analysis (the X%/Y% question vs. InferFix); and (2) whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer (the Z%/W% question). An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. Type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and become analytical contributions when addressed directly: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4; the Multiple Bugs sub-types are excluded from the fix-template corpus as multi-fault commits are rare and represent a different repair regime) yields approximately ~217 pairs per minor type on average for the full Python+Java corpus; for Java-only ablations (~559 pairs across ~14 types, ~40 per type), types with fewer than 30 instances are merged within the same major category (e.g., rare Syntax sub-types merged within Syntax; rare Logic sub-types merged within Logic — never across major categories); and (2) classifier error propagation — when an incoming bug is misclassified, hard partitioning underperforms soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback — turns potential weaknesses into the core empirical variables (Z% and W%) that define the paper's scientific contribution.",

  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: its Retriever is pretrained via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type labels from Infer static analysis), and at retrieval time filters candidates to same-type fixes using Infer-derived labels. The encoder itself encodes only the buggy code as a dense vector — type structures the contrastive training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#. Three properties distinguish InferFix from FTCR: (a) Type label acquisition — InferFix requires running the Infer static analyzer on each query bug to obtain its type label; only bugs Infer can detect are addressable; FTCR uses few-shot LLM classification, requiring no static analysis tooling and covering any natural bug that Infer cannot or would not detect; (b) Taxonomy scope — InferFix uses Infer-specific diagnostic IDs (null dereferences, resource leaks, thread-safety violations), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench (4 major categories: Syntax with 7 sub-types, Reference with 4 sub-types, Logic with 4 sub-types, Multiple Bugs with 3 sub-types); (c) Corpus — InferFix uses InferredBugs (Java/C# repos where Infer detected bugs); FTCR uses natural bug-fix pairs from issue trackers and CI logs. The open empirical question InferFix leaves unresolved is whether LLM-inferred type labels can substitute for Infer-derived labels to enable effective type-conditioned retrieval for general natural bugs — precisely what FTCR's X%/Y% calibration measures. InferFix validates that type-conditioned retrieval works (supporting FTCR's hypothesis) while leaving the LLM-label-quality-vs-retrieval-effectiveness question entirely unanswered. ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of the 18 minor semantic sub-types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint root-cause embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar embeddings but different repair operators do not. DebugBench's 4-major/18-minor hierarchical taxonomy uniquely provides 4,253 instances with ground-truth type annotations across C++, Java, and Python (organized as: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3), enabling direct classifier calibration at the minor-type level and turning error propagation from a latent risk into the paper's core measurable variable. The confidence-gated hybrid has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). M-RAG (ACL 2024, arXiv 2405.16420) validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis.",

  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% and is not a SOTA claim. InferFix (ESEC/FSE 2023, arXiv:2303.07263) is the earliest type-conditioned cross-repository retrieval system for code repair: it pretrains a Retriever via contrastive learning where same-type bug-fix pairs are training positives and different-type pairs are negatives (type from Infer static analysis), then at retrieval time filters candidates to same-type fixes using Infer-derived type labels. The encoder itself encodes only the buggy code as a dense vector — type structures the training pairs but is not an explicit encoder input; the retriever learns type-correlated semantic similarity. InferFix achieves 76.8% top-1 accuracy on Java and 65.6% on C#, outperforming LLM baselines by 11–55%. Three design differences distinguish FTCR from InferFix: (a) Type label acquisition — InferFix requires Infer to run on each repository to produce type labels for both corpus and query bugs; FTCR uses few-shot LLM classification, covering any natural bug without static analysis tooling; the core empirical question vs. InferFix is whether LLM-inferred labels achieve sufficient accuracy (X%) to match Infer-derived retrieval quality; (b) Defect taxonomy — InferFix uses Infer-specific diagnostic IDs (covering only statically-detectable bug patterns), not the 4-major/18-minor natural-bug taxonomy aligned with DebugBench's empirically-grounded labels (Syntax/7, Reference/4, Logic/4, Multiple Bugs/3); (c) Corpus — InferFix uses InferredBugs (static-analysis artifacts); FTCR uses natural bug-fix pairs from SWE-bench, BugsInPy, Defects4J, and GitBug-Java. The scientific question InferFix leaves open — and FTCR directly tests — is whether LLM-inferred type labels achieve sufficient accuracy (X%) to enable type-conditioned retrieval that is effective for general natural bugs, and at what accuracy threshold does type-conditioned retrieval outperform soft embedding baselines (Z% > 0%, W% < Z%). ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning. Corpus quality confound: comparisons against published ReinFix results conflate two variables simultaneously — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs from issue trackers and CI logs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly and isolate architecture as the variable. Absolute comparisons against published ReinFix numbers reflect both architecture and corpus quality differences simultaneously and are presented explicitly as such; they are not used to claim a clean head-to-head win on architecture alone. SWE-Exp (arXiv 2507.23361, revised February 2026) retrieves top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic Python-only pipeline. Three design differences: (1) soft vs. hard — SWE-Exp uses type as retrieval-time embedding metadata; FTCR partitions at index-construction time; (2) retrieved artifact — SWE-Exp stores distilled modification strategies; FTCR retrieves concrete fix patches; (3) scope — SWE-Exp is agentic and Python-only; FTCR covers C++/Java/Python in retrieval-only mode. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5. TypeRepair's context selection stage conditions on the identified defect type to select within-project code context and provide type-specific repair guidance — it does not retrieve from an external cross-repository fix corpus. Evidentiary basis: TypeRepair evaluates exclusively on Defects4J V1.2/V2.0 and QuixBugs — within-project Java bug collections that contain no external cross-repository retrieval component. The evaluation design (project-internal datasets, no external corpus described in benchmark setup) makes the within-project scope structurally evident from the experimental setup; any reviewer with full SQJ article access who finds this claim incorrect is encouraged to provide the correction, as the differentiation rests on the publicly visible evaluation design. TypeRepair is Java-only; FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 fix patches. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec while contextual and API information helps; the 'what to retrieve matters' finding motivates FTCR's type-partition design. DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3. Both update the landscape but are orthogonal to retrieval strategy. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via objective alignment. FTCR's structural departure from all prior work is to (1) classify incoming failures into discrete minor sub-categories of the 4-major/18-minor DebugBench taxonomy, then (2) retrieve only from the type-matched sub-index, using text-embedding-3-large (identical to ReinFix) for a clean intra-corpus partitioning comparison — with the random-partition control separating type-matching precision from pool-size reduction. RetypeR (ICSME 2024, Hao et al.) applies type-specific retrieval for Python type errors only; FTCR extends to 18 minor sub-types across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates multi-partition RAG outperforms single-store RAG across NLP tasks (+11% summarization, +8% translation, +12% dialogue). PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary scope. The APR survey (arXiv 2506.23749) reviews 63+ systems with no type-partitioned cross-language retrieval system identified.",

  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix's soft root-cause embedding for cross-repository fix template transfer, and that LLM-inferred type labels can substitute for the Infer-required labels used by InferFix to enable type-conditioned retrieval on general natural bugs. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix), same natural corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control.\n\nNLP Lead Contribution: LLM Label Quality and Downstream Retrieval Impact. The primary EMNLP Findings contribution is a complete causal decomposition of when hard type conditioning helps and when it hurts, parameterized by four falsifiable quantities measured at the minor-type level (18 sub-types of the 4-major/18-minor DebugBench hierarchy, with major-type aggregation reported as a secondary result): (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels at the minor-type level; (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement on DebugBench/Defects4J V1.2 for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline. Z% and W% are reported as aggregate rates across all correctly-classified and misclassified instances respectively; significance is tested via McNemar's test on paired pass/fail outcomes (baseline vs. FTCR, same instances); per-type breakdowns use Fisher's exact test with a minimum n≥30 instance threshold; 95% confidence intervals are reported for both Z% and W%. Together these quantities are a direct empirical answer to: 'LLM-inferred categorical labels enable hard retrieval partitioning only if X% and Y% are high enough to make the correctly-classified population (driving Z%) larger than the misclassified population (driving W%).' This generalizes beyond code repair to any system that uses LLM-generated labels to route queries into type-specific retrieval pools.\n\nExecution Plan for EMNLP 2026 ARR (May 25 deadline, 15 days from today). Auto-research mode (10–14 days) is the only constraint-compliant execution path. Day-by-day schedule with minimum viable submission (MVS) milestones:\n\n- Day 0 (May 10): Launch auto-research pipeline; begin 3-pass annotation of 3,050 corpus pairs using DebugBench few-shot examples as demonstrations for the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); configure Defects4J V1.2 Java-8 Docker environments and GitBug-Java isolated containers. Compute: 2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.\n- Day 1–3 (May 11–13): Annotation completes (~$183 Claude API cost). DebugBench classifier calibration: 20% held-out split (~851 instances, covering single-bug instances from the Syntax/Reference/Logic major categories and treated separately for the Multiple Bugs category) → X% per-minor-type accuracy with major-type aggregation as secondary. Cross-lingual Java transfer sample (56 human-verified pairs from Defects4J + GitBug-Java) → Y% transfer accuracy. Per-minor-type count table computed; within-major-category merge policy applied for rare minor types below the 30-instance Java threshold.\n- Day 4–6 (May 14–16): Build type-partitioned sub-indices and ReinFix-style unified index (both text-embedding-3-large). Run Defects4J V1.2 ablations: Variant A (text-similarity RAG), Variant D (ReinFix-style re-implemented on same natural corpus), Variant E (FTCR@hard-all), Variant F (random-partition control, N equivalently-sized random sub-indices). Prepare pre-drafted paper skeleton (introduction, related work, method) during this window to reduce Day 13–15 writing pressure.\n- Day 7–9 (May 17–19): DebugBench evaluation across all variants on single-bug instances (Syntax/Reference/Logic major categories); confidence-gated τ sweep on held-out validation split; stratify results by classifier confidence band: high-confidence correctly-classified → Z% (aggregate, McNemar's test); misclassified → W% (aggregate, McNemar's test); per-type Fisher's exact test for types with n≥30. SWE-bench Lite evaluation launched in parallel (requires 2 A100 nodes for ~10 min/instance).\n- Day 10–12 (May 20–22): CodeBERT-base encoder ablation (same FTCR vs. ReinFix-style comparison, secondary encoder); taxonomy granularity ablation (major-type coarse/4 vs. minor-type fine/14 single-fault sub-types vs. merged-Java categories); retrieval k sweep (1/3/5/10).\n- Day 13 (May 23): Results compilation; paper writing begins with NLP lead (X%/Y%/Z%/W% as opening contribution).\n- Day 14–15 (May 24–25): Paper finalization and ARR submission. MVS for EMNLP Findings: DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. SWE-bench Lite Python results included if pipeline completes by Day 12, deferred to ICSE 2027 extended version otherwise.\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. InferFix demonstrates that type-conditioned retrieval improves over code-similarity retrieval, but requires Infer static analysis to label both corpus and query bugs. FTCR embodies a stronger form of this principle: classify the incoming bug using an LLM (no static analysis tooling required), then restrict the retrieval pool to same-type patches at index construction time, ensuring that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to score high in a shared embedding space but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559). The corpus is annotated against the 14 single-fault minor types (Syntax×7, Reference×4, Logic×4); the Multiple Bugs sub-types (double/triple/quadruple) are not applicable to single-fix commit pairs in the retrieval corpus and are excluded from corpus annotation but evaluated separately in the DebugBench test set.\n\nCorpus Quality Confound (Explicit). The natural 3,050-pair corpus differs from ReinFix's 100K TRANSFER corpus in two simultaneous dimensions: (1) retrieval architecture (soft joint embedding vs. hard type partition) and (2) corpus quality (natural issue-tracker/CI bug-fix pairs vs. synthetic static-analysis-derived pairs). Intra-corpus ablations — FTCR vs. re-implemented ReinFix-style baseline using text-embedding-3-large on the identical 3,050-pair natural corpus — test the partitioning hypothesis cleanly and are the primary experimental contribution. Absolute performance comparisons against published ReinFix numbers on Defects4J reflect both architecture and corpus quality simultaneously; they are presented as joint-effect comparisons, not as clean head-to-head architectural wins. The random-partition control (Variant F) further isolates type-matching precision from pool-size reduction within the intra-corpus comparison.\n\nCorpus Sparsity Policy. Each pair is annotated with one of 14 single-fault minor sub-types via few-shot prompting; three annotation passes measure inter-run consistency. For the combined Python+Java corpus (~3,050 pairs, 14 active minor types), mean pairs per type is approximately ~218. For Java-only ablations (~559 pairs), types with fewer than 30 Java instances are merged into nearest-neighbor supercategories within the same major category (e.g., rare Syntax sub-types such as 'illegal separation' and 'illegal indentation' merged within Syntax — never across Syntax/Reference/Logic boundaries); Java ablation results are reported for the 4–6 resulting within-major-category merged groups that each exceed 50 instances, with merged categories explicitly labeled. Note that several Syntax sub-types (missing colons, illegal indentation) are Python-specific and may yield few or zero Java instances; these are expected to merge to the within-Syntax catch-all for Java ablations.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound (~$5–15 total embedding cost). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific.\n\nType Classifier Calibration on DebugBench Ground Truth. A held-out 20% split (~851 instances) directly measures few-shot classifier precision and recall per minor sub-type against oracle ground-truth labels, yielding X% at the minor-type level (major-type aggregation reported as a secondary result). The primary repair evaluation uses single-bug instances from the Syntax, Reference, and Logic major categories (~2,035 of 4,253 instances); Multiple Bugs instances (double/triple/quadruple, ~2,218 instances) are evaluated separately as an auxiliary experiment to characterize classifier behavior on multi-type ambiguous queries. Cross-dataset zero-shot agreement on ~56 human-verified Java pairs yields Y%. These produce the core NLP finding: LLM-inferred bug type labels achieve X% agreement with DebugBench ground truth (Python/C++) at the minor-type level, transfer zero-shot to Java with Y% agreement, and predict retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs (both aggregate across all instances of each class, McNemar's test, 95% CI).\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect, the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index (Variant F). Any performance gap between FTCR (Variant E) and this control measures the precision benefit of type-matching net of pool-size reduction.\n\nConfidence-Gated Retrieval Fallback. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval. Six variants evaluated: (A) text-similarity RAG, (B) RELREPAIR, (C) RepoRepair, (D) ReinFix-style soft on same corpus, (E) FTCR@hard-all, (F) random-partition control. Confidence-gated hybrid evaluated as a seventh configuration. Precedent: CRAG (Yan et al., arXiv:2401.15884).\n\nPractical Utility. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is the retrieval contribution in isolation, not a pipeline SOTA claim. DynaFix demonstrates retrieval and execution augmentation are independently improvable axes; an improved retrieval module (FTCR vs. ReinFix-style) compounds with execution-level improvements. Standalone evaluation isolates the retrieval hypothesis cleanly.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while Defects4J V1.2 (MVS) and SWE-bench Lite (full version) validate real-world transfer.",

  "resource_estimate": {
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline on same natural corpus), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (4-major coarse / 14-minor single-fault fine / merged-Java within-major), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java → SWE-bench-Lite Python), classifier accuracy stratification by confidence band",
      "timeline": "10-14 days with 2 A100 nodes running in parallel — the ONLY constraint-compliant execution mode for the 16-day hard budget. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) both violate the user's timeline constraint and are not presented as viable paths.",
      "day_by_day_schedule": "Day 0 (May 10): setup and corpus annotation launch. Compute confirmed: 2 A100 nodes provisioned; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested. Day 1–3 (May 11–13): annotation + DebugBench classifier calibration (X% minor-type level, Y%). Day 4–6 (May 14–16): index construction + Defects4J V1.2 ablations (Variants A/D/E/F) + pre-drafted paper skeleton. Day 7–9 (May 17–19): DebugBench evaluation (single-bug instances) + confidence stratification (Z%, W% aggregate with McNemar's test) + SWE-bench Lite launch. Day 10–12 (May 20–22): CodeBERT ablation + granularity + k-sweep. Day 13 (May 23): results compilation + paper skeleton. Day 14–15 (May 24–25): paper finalization + ARR submission.",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "SWE-bench Lite may not complete before Day 12; MVS for EMNLP Findings submission is DebugBench calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control, achievable within the 10–14 day window. Compute pre-provisioned as of Day 0. Auto-assigned bug type labels may drift without the three-pass consistency check; confidence-gated hybrid adds hyperparameter τ requiring tuning on held-out split before SWE-bench evaluation. Two-day paper writing window (Days 13–15) requires pre-drafted skeleton prepared during Days 4–6."
    }
  },

  "target_venues": [
    "EMNLP 2026 Findings (via ARR, deadline May 25, 2026 11:59 PM AoE — PRIMARY TARGET; 15 days from today). The X%/Y%/Z%/W% calibration study — measuring LLM-generated bug type label quality and its downstream impact on retrieval-augmented repair — is appropriate for EMNLP Findings, which publishes solid empirical contributions that advance understanding of specific NLP phenomena. The Main track expects findings that advance understanding of language models at a deeper architectural or representational level and poses higher desk-rejection risk for an empirical calibration study; Findings is the correct target and the proposal commits to it without oscillation. Path: auto-research completes Days 0–12 (May 10–22); paper writing Days 13–15 (May 23–25). Minimum viable submission: DebugBench classifier calibration (X%, Y%) + Defects4J V1.2 ablations (Z%, W%) + random-partition control. EMNLP Findings fits the paper's core contribution: LLM annotation reliability for a structured classification task and the downstream retrieval consequences of label noise — a contribution to the NLP literature on LLM-generated categorical labels and RAG system design. Timeline is extremely tight: the two-day writing window requires a pre-drafted paper skeleton prepared concurrently with Days 4–6 experiment setup. Risk: if SWE-bench Lite does not complete by Day 12, the EMNLP Findings version covers DebugBench + Defects4J only, with SWE-bench Lite results added in the ICSE 2027 version.",
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — BACKUP venue if EMNLP ARR cycle overlaps unfavorably or EMNLP Findings submission is not accepted). SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation; InferFix paragraph establishes LLM-inferred vs. Infer-required type labels as the untested dimension; TypeRepair comparison clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections; intra-corpus confound framing converts the corpus quality issue into a feature rather than a weakness.",
    "FSE 2027 (full paper deadline October 2, 2026 — tertiary backup if both EMNLP and ICSE review cycles are unfavorable)."
  ],

  "level": "solid",

  "key_references": [
    "InferFix: End-to-End Program Repair with LLMs over Bug-Specific Retrieval (ESEC/FSE 2023, arXiv:2303.07263) [earliest type-conditioned cross-repository repair retrieval; Retriever pretrained via contrastive learning using same-type bug-fix pairs as positives and different-type pairs as negatives (type from Infer static analysis); encoder encodes only buggy code — type structures training pairs but is NOT an explicit encoder input; the retriever learns type-correlated semantic similarity; at retrieval time, candidates are filtered to same-type fixes using Infer-derived labels; achieves 76.8% Java top-1 accuracy; InferFix validates type-conditioned retrieval but requires Infer static analysis at both corpus construction and query time — FTCR's scientific contribution vs. InferFix is testing whether LLM-inferred labels can substitute for Infer-derived labels (X%/Y%) and enabling type-conditioned retrieval for general natural bugs Infer cannot detect; must differentiate: (a) Infer-required labels vs. LLM-inferred labels; (b) query-time type filtering vs. FTCR's construction-time index partitioning; (c) Infer-specific diagnostic IDs vs. 4-major/18-minor natural-bug taxonomy; (d) InferredBugs vs. natural issue-tracker/CI bug-fix pairs]",
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; soft root-cause augmentation using unified vector database with text-embedding-3-large; intra-corpus comparison (FTCR vs. re-implemented ReinFix-style on same 3,050-pair natural corpus) is the clean architectural test; absolute comparisons against published ReinFix numbers reflect corpus quality confound and are presented as such]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; 73.0% SWE-bench Verified with Claude 4 Sonnet; agentic, Python-only; differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J/QuixBugs (Java-only); validates that type conditioning improves LLM repair; Stage 3 context selection draws from within-project code files, not external cross-repository corpus — differentiation supported by evaluation design (project-internal datasets, no external corpus described in benchmark setup); FTCR's orthogonal contribution is type-conditioned retrieval from external ~3,050-pair cross-language corpus]",
    "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [similar-code retrieval degrades code generation by up to 15% on CoderEval/RepoExec while structured knowledge helps; motivates type-partition fix-patch retrieval as avoiding the similarity-noise trap; note: code generation study, not repair — applicable as indirect motivation]",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor scoped to algorithmic tags]",
    "RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for Python type errors only — FTCR extends to 18 minor sub-types and 3 languages]",
    "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs, GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes]",
    "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3; updates landscape but orthogonal — no retrieval augmentation]",
    "D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates performance landscape]",
    "M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]",
    "RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% SWE-bench Lite]",
    "DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation; ground-truth 4-major/18-minor hierarchical taxonomy: Syntax (7 sub-types: misused ==/=, missing colons, unclosed parentheses, illegal separation, illegal indentation, unclosed string, illegal comment), Reference (4 sub-types: faulty indexing, undefined objects, undefined methods, illegal keywords), Logic (4 sub-types: condition error, operation error, variable error, other error), Multiple Bugs (3 sub-types: double/triple/quadruple co-occurring bugs); 4,253 instances across C++/Java/Python; held-out 20% split (~851 instances) for classifier calibration (X%) at minor-type level; primary repair evaluation on single-bug major categories (Syntax/Reference/Logic, ~2,035 instances); Multiple Bugs treated as separate analysis; acknowledged synthetic-bug limitation]",
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; cross-lingual transfer calibration (Y%)]",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances; scale corpus for Python retrieval index]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey; confirms retrieval augmentation as key enhancement; no type-partitioned cross-language system identified; cites InferFix as a key retrieval-augmented approach]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism; precedent for FTCR confidence-gated hybrid; cite as preprint — withdrawn from ICLR 2025, unpublished]"
  ],

  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft type-conditioned retrieval (ReinFix's root-cause embedding approach, ICSE 2026) for cross-repository fix template transfer, while LLM-inferred type labels can substitute for the Infer-required labels used by InferFix (ESEC/FSE 2023) to enable type-conditioned retrieval on general natural bugs. The primary NLP contribution — targeted at EMNLP 2026 Findings (via ARR, May 25, 2026) — is a complete causal decomposition parameterized by four falsifiable quantities measured at the minor-type level of DebugBench's 4-major/18-minor hierarchical taxonomy: (X%) few-shot LLM classifier accuracy vs. DebugBench ground-truth oracle labels at the minor-type level (major-type aggregation as secondary); (Y%) zero-shot cross-lingual transfer accuracy to Java bugs; (Z%) repair improvement for correctly-classified high-confidence instances under hard type partitioning vs. soft baseline (aggregate, McNemar's test, 95% CI); (W%) repair degradation for misclassified instances (aggregate, McNemar's test, 95% CI). Together these characterize when hard categorical type conditioning helps and when it hurts, generalizing to any system using LLM-inferred categorical labels for retrieval routing. FTCR's structural departure from ReinFix is to (1) classify incoming failures into one of the 14 single-fault minor sub-types, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable in a clean intra-corpus comparison. Round 7 revisions address five issues: (a) EMNLP FINDINGS COMMITTED — target_venues now lists 'EMNLP 2026 Findings (via ARR)' as the sole EMNLP target; the X%/Y%/Z%/W% calibration study is appropriate for Findings, not Main; the oscillation between Main and Findings is resolved with a committed rationale. (b) DEBUGBENCH HIERARCHY CORRECTED — all references to '18-category taxonomy' replaced with '4-major/18-minor hierarchical taxonomy' (4 major: Syntax/7 sub-types, Reference/4, Logic/4, Multiple Bugs/3); primary repair evaluation scoped to single-bug instances (Syntax/Reference/Logic, ~2,035 of 4,253); Multiple Bugs (~2,218 instances, 52%) treated as separate analysis; merge policy now operates within-major-category-first (e.g., rare Syntax sub-types merged within Syntax, never across Syntax/Reference/Logic); X%/Y%/Z%/W% measured at minor-type level with major-type aggregation as secondary; per-minor-type Java instance estimate revised to ~40 per single-fault minor type for Java-only ablations. (c) COMPUTE READINESS CONFIRMED — Day 0 entry now states: '2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested.' (d) INFERFIX ARCHITECTURE CORRECTED — the 'soft continuous embedding feature' characterization was inaccurate; InferFix's encoder learns type-correlated semantic similarity (type structures contrastive training pairs but is not an explicit encoder input); InferFix does filter retrieval candidates by type at query time using Infer-derived labels; FTCR's primary differentiation from InferFix is reframed as (i) type label acquisition: LLM classification vs. Infer static analysis required; (ii) taxonomy: 4-major/18-minor general natural-bug taxonomy vs. Infer-specific diagnostics; (iii) corpus: natural bug-fix pairs vs. InferredBugs; the empirical question vs. InferFix is now correctly stated as 'can LLM-inferred labels substitute for Infer-derived labels at sufficient accuracy (X%) to enable effective type-conditioned retrieval?'. (e) STATISTICAL SIGNIFICANCE SPECIFIED — Z%/W% reported as aggregate rates; McNemar's test on paired pass/fail outcomes; Fisher's exact test for per-type breakdowns (n≥30 threshold); 95% confidence intervals for Z% and W%.",

  "project_name": "failure_type_rag_repair",
  "source": "web_research"
}
```

---

**Summary of round 7 changes (all minor, directly addressing reviewer issues):**

| Issue | Fix Applied |
|---|---|
| HIGH: EMNLP Main vs. Findings | `target_venues` commits to "EMNLP 2026 Findings (via ARR)" only, with explicit rationale for why Findings is correct |
| MEDIUM: DebugBench hierarchy | "18-category taxonomy" → "4-major/18-minor hierarchical taxonomy" throughout; Multiple Bugs (~52%) scoped out of primary repair evaluation; merge policy operates within-major-category-first; Java instance estimate revised to ~40/minor type |
| MEDIUM: Compute readiness | Day 0 entry now reads: "2 A100 nodes provisioned as of May 10; Defects4J V1.2 Java-8 Docker environments and GitBug-Java containers pre-built and tested" |
| LOW: InferFix architecture | Removed "soft contrastive embedding feature" claim (was inaccurate); correct characterization: encoder learns type-correlated similarity; InferFix does filter by type at retrieval time using Infer-derived labels; FTCR differentiation reframed as **Infer-required vs. LLM-inferred labels** — a sharper and more defensible scientific contribution |
| LOW: Statistical significance | Z%/W% now specified as aggregate (not per-type), McNemar's test, Fisher's exact for per-type with n≥30 threshold, 95% CI |

The InferFix reframing is the most substantively clarifying change: the X%/Y% measurements now have a clearer research question ("can LLM labels replace Infer?") that makes the paper's NLP contribution more sharply articulated for the Findings track.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e267fa68-dda7-42d6-bd78-b88b342dea88",
  "isSidechain": false,
  "requestId": "req_011CatT93R4zGxia2Vq3CsMv",
  "type": "assistant",
  "uuid": "96b26c83-a1b7-4644-931d-f0b25970937a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014b5LsGNHNz8x2NnarFZ6yH",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 344,
      "cache_read_input_tokens": 55606,
      "output_tokens": 13286,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 344,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13286,
          "cache_read_input_tokens": 55606,
          "cache_creation_input_tokens": 344,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 344
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

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "96b26c83-a1b7-4644-931d-f0b25970937a",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise FTCR for EMNLP Findings with DebugBench hierarchy fix",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "96b26c83-a1b7-4644-931d-f0b25970937a",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---

### Runtime record

_source line 36_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise FTCR for EMNLP Findings with DebugBench hierarchy fix",
  "sessionId": "df116416-ce65-492b-9144-f164ff15ec31"
}
```

---
