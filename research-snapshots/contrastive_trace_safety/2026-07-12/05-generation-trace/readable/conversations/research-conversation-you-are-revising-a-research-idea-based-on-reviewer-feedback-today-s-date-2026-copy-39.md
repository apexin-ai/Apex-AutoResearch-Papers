# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 23
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-1/a9d6493b-2b10-47f3-a4b7-6416b94b4ede.jsonl`
- **Structured JSON:** [`c807c103f9324fa414ec.json`](../../sessions/c8/c807c103f9324fa414ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T06:32:57.295Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T06:32:57.295Z",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\",\n  \"core_problem\": \"Retrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. This 'what you retrieve matters' result directly motivates type-conditioned fix-patch retrieval: type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and, when addressed directly, become analytical contributions: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified into the wrong type partition, hard partitioning will underperform soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback to soft retrieval — turns potential weaknesses into measurable experimental variables that sharpen, rather than undermine, the core hypothesis.\",\n  \"opportunity\": \"ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation from a different angle: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Their core finding — that what you retrieve determines quality more than how you retrieve — directly motivates FTCR's retrieval design: fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar code but different root causes do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python; crucially, these ground-truth labels enable direct calibration of the few-shot type classifier, turning classifier error propagation from a latent risk into a measurable experimental variable. The confidence-gated hybrid (fall back to soft retrieval for low-confidence classifications) addresses the structural risk of hard partitioning and has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884) for general RAG systems. M-RAG (ACL 2024, arXiv 2405.16420) additionally validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis before evaluating it in the code repair setting.\",\n  \"landscape\": \"RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% with the same model and is not a SOTA claim. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning, and root cause is a continuous semantic descriptor, not a discrete category. SWE-Exp (arXiv 2507.23361, revised February 2026) is the most important concurrent work: it retrieves top N=10 issues 'most relevant in terms of error type' from an experience bank using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large encoder), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic pipeline. Three design differences distinguish SWE-Exp from FTCR: (1) retrieval mechanism — SWE-Exp uses soft cosine similarity with type as embedding metadata at retrieval time; FTCR partitions the index into discrete type sub-corpora at construction time, so only same-type pairs are ever candidates for a query; (2) retrieved artifact — SWE-Exp stores distilled problem perspectives and generalized modification strategies; FTCR retrieves concrete historical fix patches for direct template transfer; (3) scope — SWE-Exp is fully agentic and scoped to Python; FTCR is retrieval-only and covers C++, Java, and Python, using DebugBench's oracle type labels for cross-lingual calibration. The testable question SWE-Exp leaves open is whether hard construction-time partitioning outperforms soft retrieval-time type filtering for fix-template precision. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5 baseline. TypeRepair's context selection stage conditions on the identified defect type to select relevant within-project code context and to provide type-specific repair guidance in the LLM prompt — it does not retrieve from an external cross-repository fix corpus. TypeRepair is Java-only (Defects4J/QuixBugs); FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 historical fix patches. TypeRepair validates that defect type identification benefits LLM-based repair (supporting FTCR's core hypothesis) while leaving hard-vs-soft type-partitioned cross-repository retrieval entirely unexplored; FTCR addresses this gap directly. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information helps; their proposed AllianceCoder retrieves APIs via semantic description matching rather than code similarity. While the study targets code generation rather than repair, the 'what to retrieve matters more than how' finding motivates FTCR's choice of fix patches retrieved by type partition (sharing semantic repair structure) over code-similarity retrieval (sharing only surface features). DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair (236 bugs fixed with GPT-4); DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3 via self-directed debugging with runtime traces. Both update the Defects4J performance landscape but are orthogonal to FTCR's retrieval strategy focus — execution-level augmentation and retrieval strategy are independently improvable axes. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via LLM objective alignment. FTCR's structural departure from ReinFix is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) for a clean comparison that isolates partitioning as the primary architectural variable — noting that partitioning also reduces the effective retrieval pool to ~1/N_types of the full corpus, a corpus-size effect that a random-partition control ablation is designed to separate from type-matching precision. RetypeR (ICSME 2024, Hao et al.) applies a two-stage external+internal retrieval conditioned on Python type errors, establishing that type-specific retrieval helps for one narrow bug class and language; FTCR extends this principle to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates that multi-partition RAG consistently outperforms single-store RAG across NLP tasks (summarization: +11%, translation: +8%, dialogue: +12%), validating the general principle of partition-based retrieval before applying it to code repair. PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary (localization rather than cross-repository fix template retrieval). The APR survey (arXiv 2506.23749) reviews 63+ systems and identifies retrieval augmentation as the key enhancement, but no reviewed system applies hard taxonomic type classification as the retrieval partition key across multiple languages.\",\n  \"approach\": \"We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix-style soft root-cause embedding for cross-repository fix transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix for a clean comparison), same corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control (see below).\\n\\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. FTCR embodies this principle: rather than retrieving the most syntactically similar buggy code in the corpus, we retrieve fix patches — input/output transformation pairs — that share the same semantic repair operation. Type partitioning ensures that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to look syntactically similar but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\\n\\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\\n\\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy (four major types: Syntax, Reference, Logic, Multiple; 18 minor subtypes) via few-shot prompting using DebugBench's labeled examples as demonstrations; three annotation passes measure inter-run consistency. A per-type instance count table is computed and reported in the paper for transparency. For the combined Python+Java corpus (3,050 pairs), 18-type analysis is viable: Python instances dominate (~2,487) and yield an estimated mean of ~138 pairs per type. For Java-only ablations (~559 pairs, ~31 per type average), a minimum-threshold policy applies: types with fewer than 30 Java instances are merged into nearest-neighbor supercategories (e.g., Concurrency + Resource-Leak → Resource-Management; Format-Error + Syntax-Error → Low-Level, since compiled Defects4J/GitBug-Java bugs contain near-zero syntax errors). Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled. This avoids the degenerate case of k=5 retrieval from a 15-instance sub-index, which approximates exhaustive lookup rather than similarity-based retrieval.\\n\\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound; embedding cost is negligible (~$5–15 for corpus plus all evaluation queries at $0.13/1M tokens). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific and deconfounding the encoder-vs-partitioning comparison.\\n\\nType Classifier Calibration on DebugBench Ground Truth. Since DebugBench provides oracle type labels for 4,253 instances, a held-out 20% split (851 instances) directly measures our few-shot classifier's per-type precision and recall against ground truth, yielding an overall accuracy estimate. Cross-dataset zero-shot agreement is measured by applying the same classifier to a 10% random sample (~56 pairs) of the Java annotation set (Defects4J + GitBug-Java) with human-verified labels as oracle, yielding a cross-lingual label consistency score. This produces the NLP contribution: a falsifiable empirical claim that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels (Python/C++), transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\\n\\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect — hard partitioning reduces the effective retrieval pool to ~1/N_types of the full index, which independently affects recall — we add a random-partition baseline (Variant F): the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index. Any performance gap between FTCR (Variant E, hard type partition) and this control measures the precision benefit of type-matching net of pool-size reduction. This converts the comparison from 'clean but contested' to 'rigorous and unambiguous.'\\n\\nConfidence-Gated Retrieval Fallback. At inference time, the type classifier outputs a probability distribution over 18 categories. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval (identical to the ReinFix baseline). This confidence-gated hybrid is evaluated as a sixth system variant alongside: (A) text-similarity RAG (no type signal), (B) RELREPAIR (project-internal retrieval), (C) RepoRepair (documentation-guided), (D) ReinFix-style soft retrieval (re-implemented on same corpus and same encoder), (E) FTCR@hard-all, and (F) random-partition control (same N sub-indices, randomly assigned — corpus-size control). The confidence-gated fallback has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). The projected finding: correctly-classified high-confidence bugs show systematic gains from hard partitioning (+5–10% repair success on Defects4J where oracle type labels allow clean stratification); misclassified or low-confidence bugs show performance on par with or slightly below soft retrieval; the confidence gate recovers aggregate performance for ambiguous cases; the random-partition control falls between soft retrieval and FTCR@hard-all, confirming that type-matching rather than pool-size reduction drives the gain.\\n\\nPractical Utility: Retrieval as an Independently Upgradeable Module. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is deliberately positioned as the retrieval contribution in isolation, not a claim against the agentic pipeline ceiling. The motivation for isolating retrieval is architectural: DynaFix (arXiv 2512.24635) demonstrates that execution-level augmentation and retrieval strategy are independently improvable axes — it improves over ReinFix on Defects4J V2.0 by adding iterative execution feedback while keeping retrieval fixed. An improved retrieval module (FTCR vs. ReinFix-style soft retrieval) compounds with execution-level improvements: the delta between FTCR-augmented and ReinFix-augmented iterative repair pipelines measures the retrieval contribution at the pipeline level. Standalone evaluation isolates the retrieval hypothesis cleanly; the modular gain is what ICSE reviewers can act on independently of scaffolding choices.\\n\\nExpected Performance on SWE-bench Lite. We project FTCR to achieve 20–35% resolve rate with Claude Sonnet 4.6 in retrieval-only (non-agentic) mode, comparable to ReinFix-style retrieval on the same corpus. This is below the current SWE-bench Lite SOTA (~62.7%, Claude Opus 4.6, May 2026, agentic scaffolding) and below RepoRepair's 45.7% (documentation-guided multi-step localization). Lower aggregate performance than RepoRepair is explicitly defended: FTCR does not incorporate documentation-guided localization, which is an orthogonal architectural component. The primary SWE-bench Lite contribution is validating that the type-conditioned advantage observed on DebugBench transfers to real-world Python repositories, not claiming absolute SOTA.\\n\\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while SWE-bench Lite validates real-world transfer.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~88 H100-hours (~150 A100-hours equivalent)\",\n      \"gpu_utilization\": \"~30-40% utilized; high idle while researchers design annotation prompts, debug Defects4J Java-8 environments, manually review per-type count tables, and verify annotation consistency across passes\",\n      \"timeline\": \"4-6 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$450 (150 A100-hours × $3/h on RunPod/Lambda Labs)\",\n      \"embedding_api_cost\": \"~$5-15 (text-embedding-3-large for 3,050-pair corpus + evaluation queries, at $0.13/1M tokens; negligible relative to overall budget)\",\n      \"note\": \"Well within the 200 H100-hour hard budget\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~165 H100-hours (~280 A100-hours equivalent)\",\n      \"gpu_utilization\": \"~55-65% utilized; agent continuously queues embedding and evaluation jobs while human approves ablation configurations at decision gates\",\n      \"timeline\": \"6-8 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in for ablation approval, per-type count table review, confidence threshold tuning, and failure triage\",\n      \"claude_api_cost\": \"$200-400 (annotation: ~3,050 instances × ~$0.02/call ≈ $61; 3 annotation passes for consistency ≈ $183; DebugBench classifier calibration: 851 held-out instances × $0.02 ≈ $17; pipeline orchestration and repair: ~1,500 agent turns × $0.10/turn ≈ $150; buffer ~$50)\",\n      \"embedding_api_cost\": \"~$5-15 (text-embedding-3-large for corpus and evaluation queries)\",\n      \"estimated_gpu_cost\": \"~$840 (280 A100-hours × $3/h)\",\n      \"note\": \"Within the 200 H100-hour hard budget\",\n      \"risk_note\": \"Defects4J Docker reproducibility is the primary bottleneck — the Java-8 pre-filter eliminates ~9% upfront, but remaining instances still require environment triage. GitBug-Java's isolated Docker images significantly reduce this overhead for the Java supplement. Java per-type sparsity is the secondary risk: if the 6-8 type categories above threshold have unequal sizes, the Java ablation may be underpowered for the smallest categories.\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)\",\n      \"gpu_utilization\": \"near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants\",\n      \"ablation_scope\": \"Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java train → SWE-bench-Lite Python eval), classifier accuracy stratification (by confidence band)\",\n      \"timeline\": \"10-14 days with 2 A100 nodes running in parallel\",\n      \"team\": \"0 (initial ~4h setup for corpus pipeline, per-type sub-index construction scaffold, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)\",\n      \"claude_api_cost\": \"$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)\",\n      \"embedding_api_cost\": \"~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)\",\n      \"estimated_gpu_cost\": \"~$969 (323 A100-hours × $3/h)\",\n      \"speed_bottleneck\": \"GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls\",\n      \"risk_note\": \"Auto-assigned bug type labels may drift from human-interpretable categories without the three-pass consistency check; the confidence-gated hybrid adds a hyperparameter (τ) that requires tuning on the DebugBench held-out split before SWE-bench Lite evaluation. SWE-bench Lite infrastructure failures can silently inflate repair failure counts without human oversight.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICSE 2027 (mandatory abstract deadline June 23, 2026 — SOLE PRIMARY TARGET; best fit for SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation reviewers will expect; TypeRepair (SQJ 2026) comparison on Defects4J clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections about hard partitioning; random-partition control specifically converts the 'corpus-size confound' objection into a closed experimental question)\",\n    \"FSE 2027 (full paper deadline October 2, 2026 — backup venue if ICSE review cycle overlaps unfavorably; same SE audience, equally appropriate for a retrieval-architecture study with multi-language empirical evaluation)\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; must compare directly on Defects4J V1.2 using same text-embedding-3-large encoder; uses a unified vector database, not a specific named implementation]\",\n    \"SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; retrieves top N=10 issues by soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; stores distilled modification strategies, not fix patches; agentic, Python-only; achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet — differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, and multi-language scope]\",\n    \"TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0/QuixBugs (Java-only); validates that type conditioning improves LLM repair; context selection stage conditions type to select within-project context and generate type-specific prompting guidance, NOT cross-repository retrieval — FTCR's orthogonal contribution is type-conditioned retrieval of fix patches from an external ~3,050-pair cross-language corpus; must cite and explicitly differentiate]\",\n    \"What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [shows similar-code snippet retrieval degrades repository-level code generation by up to 15% on CoderEval/RepoExec while contextual + API info helps; motivates FTCR's type-conditioned fix-patch retrieval — type partitioning retrieves patches sharing semantic repair structure, not superficial code similarity; note the finding applies to code generation not repair, but the 'what to retrieve matters' principle is directly applicable]\",\n    \"ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor]\",\n    \"RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for one language and one error class — FTCR extends to 18 types and 3 languages]\",\n    \"DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs with GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes; retrieval improvement (FTCR) compounds with execution-level improvements (DynaFix-style)]\",\n    \"DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3 via runtime traces and debugging-driven conversational repair; updates Defects4J landscape but is orthogonal — no retrieval augmentation component]\",\n    \"D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates Defects4J performance landscape]\",\n    \"M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG validated on NLP tasks: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]\",\n    \"RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% on SWE-bench Lite using multi-step localization, orthogonal to FTCR's retrieval focus]\",\n    \"DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation with ground-truth 18-category labels across C++/Java/Python; held-out 20% split used for few-shot classifier calibration; synthetic-bug limitation acknowledged]\",\n    \"GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; supplement for Defects4J Java corpus]\",\n    \"SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances from 128 repos; used as scale corpus for Python retrieval index]\",\n    \"A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey confirming retrieval augmentation as key enhancement with no type-partitioned system identified]\",\n    \"What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]\",\n    \"PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]\",\n    \"RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]\",\n    \"CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism with retrieval quality scoring; precedent for the FTCR confidence-gated hybrid variant; note: withdrawn from ICLR 2025, unpublished — cite as preprint only]\"\n  ],\n  \"description\": \"FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft root-cause-augmented retrieval (ReinFix's approach, ICSE 2026) for cross-repository fix template transfer. ReinFix (ICSE 2026, arXiv 2506.23100) is the closest prior work — it embeds LLM-generated free-text root-cause descriptions jointly with buggy code into a unified vector database using text-embedding-3-large, showing +32/+38 bugs fixed on Defects4J V1.2/V2.0. FTCR's structural departure is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's empirically-validated taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable. Round 5 revisions address four issues: (a) TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) added to landscape and key_references with explicit differentiation — TypeRepair's 4-stage pipeline uses defect type to select within-project context and generate type-specific repair guidance (prompt engineering), not cross-repository retrieval; it covers Java only (Defects4J/QuixBugs) with 10 types; TypeRepair validates that type conditioning helps repair (supporting FTCR's hypothesis) while leaving cross-repo type-conditioned retrieval unexplored; (b) arXiv 2503.20589 (Gu et al., ICSE 2026) added as motivation rather than counterevidence — their finding that similar code snippet retrieval degrades code generation by 15% while structured knowledge helps motivates FTCR's type-conditioned fix-patch retrieval; type partitioning retrieves patches sharing semantic repair structure (the fix operator), not superficial code similarity; the paper targets code generation, not repair, making it an indirect motivator rather than a direct challenge; (c) practical utility framing added explicitly in approach — retrieval is an independently upgradeable module within agentic pipelines; DynaFix demonstrates retrieval and execution augmentation are independent axes; FTCR's retrieval gain compounds with DynaFix-style iterative repair; 20-35% standalone metric is the retrieval floor, not the pipeline ceiling; (d) EMNLP 2026 definitively removed — the May 25 ARR deadline is infeasible given that all experiments remain to be run; ICSE 2027 is the sole primary target; FSE 2027 is the backup; cross-lingual classifier findings can be submitted separately after ICSE results are complete. RetypeR (ICSME 2024) establishes type-specific retrieval for Python type errors specifically; FTCR extends to 18 categories across C++, Java, and Python. The retrieval corpus (~3,050 natural bug-fix pairs from SWE-bench non-Lite, BugsInPy, Defects4J V1.2, and GitBug-Java) requires no GPU training; the approach is fully inference-based. Target venues: ICSE 2027 (abstract June 23, primary), FSE 2027 (October 2, backup).\",\n  \"project_name\": \"failure_type_rag_repair\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 5)\nIssues: [\"CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.\", \"HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.\", \"MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.\", \"MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.\", \"LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated.\"]\nFeedback: This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.5 到 3.2，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T06:32:57.300Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T06:32:57.300Z",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

## Round 1

21 recorded events

### User

_source line 3 · 2026-05-10T06:32:57.340Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "core_problem": "Retrieval-augmented repair systems fall into two camps: code-text-similarity retrieval (RAP-Gen, RELREPAIR) and soft root-cause-augmented retrieval (ReinFix, ICSE 2026), which concatenates an LLM-generated free-text root-cause description with the buggy code into a unified embedding space using text-embedding-3-large. Neither approach exploits the structural regularity that bugs of the same semantic TYPE — null dereference, off-by-one, API misuse, type mismatch, concurrency — share fix templates even when code looks syntactically dissimilar. TypeRepair (SQJ 2026, Zhang et al.) validates that defect type identification improves LLM-based repair, but its mechanism is type-conditioned within-project context selection and type-specific prompt guidance — not retrieval from an external cross-repository fix corpus. The open question is whether hard categorical type partitioning of the retrieval index outperforms ReinFix's soft semantic root-cause augmentation for cross-repository fix transfer, particularly in a multi-language setting. An independent empirical finding (Gu et al., ICSE 2026, arXiv 2503.20589) strengthens the motivation: similar code snippet retrieval degrades code generation performance by up to 15%, while contextual and structured knowledge retrieval helps. This 'what you retrieve matters' result directly motivates type-conditioned fix-patch retrieval: type partitioning ensures retrieved patches share semantic repair structure (the fix operation) rather than superficial syntactic similarity, precisely avoiding the degradation trap Gu et al. identify. Two methodological challenges discipline the comparison and, when addressed directly, become analytical contributions: (1) corpus sparsity — a natural bug-fix corpus of ~3,050 pairs across 18 types yields only ~31 Java instances per type on average, requiring an explicit minimum-threshold and merge policy for rare types; and (2) classifier error propagation — when an incoming bug is misclassified into the wrong type partition, hard partitioning will underperform soft retrieval for those instances, making the performance gap conditional on classifier confidence. Addressing both challenges — by measuring classifier accuracy against DebugBench's ground-truth labels and adding a confidence-gated fallback to soft retrieval — turns potential weaknesses into measurable experimental variables that sharpen, rather than undermine, the core hypothesis.",
  "opportunity": "ReCode (CIKM 2025, arXiv 2509.02330) demonstrates algorithm-type-aware retrieval in competitive programming but is explicitly scoped to algorithmic tags (greedy, DP, graph). ReinFix (ICSE 2026, arXiv 2506.23100) advances toward root-cause-conditioned retrieval for real-world repositories, showing +32 bugs fixed on Defects4J V1.2 and +38 on V2.0, but its mechanism — LLM-generated free-text root-cause descriptions embedded jointly with buggy code in one unified vector database using text-embedding-3-large — is a soft, continuous approach without type-level partitioning. SWE-Exp (arXiv 2507.23361, revised February 2026) introduces an experience bank that retrieves the top N=10 issues 'most relevant in terms of error type' using soft cosine similarity over (issue-type + description) embeddings encoded by Multilingual-E5-Large; it stores distilled modification strategies rather than concrete fix patches, operates as a fully agentic pipeline, and is scoped to Python. SWE-Exp's type signal is a soft retrieval-time metadata feature, not a hard index-construction partition; FTCR's structural departure is to partition the retrieval corpus into discrete type sub-indices before any query is issued, enabling retrieval-pool precision rather than post-hoc reranking. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) independently validates that defect type identification improves LLM-based repair: its 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types achieves 272% improvement over GPT-3.5 on Defects4J V1.2/V2.0 and QuixBugs. Crucially, TypeRepair's context selection stage uses the identified type to select within-project code context and generate type-specific repair guidance for the LLM prompt — it retrieves no external cross-repository fix corpus. TypeRepair is Java-only; FTCR extends type-conditioned repair to C++/Java/Python with cross-repository retrieval of ~3,050 historical fix patches. TypeRepair establishes that type conditioning matters (validating FTCR's hypothesis) while leaving hard-vs-soft type-partitioned cross-repo retrieval entirely unexplored. Gu et al. (ICSE 2026, arXiv 2503.20589) provide independent empirical motivation from a different angle: retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information significantly helps. Their core finding — that what you retrieve determines quality more than how you retrieve — directly motivates FTCR's retrieval design: fix patches retrieved by type partition share the semantic repair operation (null-check insertion, bounds guard, API substitution), while patches retrieved by surface code similarity may look similar yet represent different fix operators, concentrating exactly the noise Gu et al. identify. DynaFix (arXiv 2512.24635) subsequently surpasses ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair, confirming that retrieval strategy and execution-level augmentation are independently improvable axes; FTCR operates on the retrieval strategy axis. RetypeR (ICSME 2024) applies type-specific retrieval but only for Python type errors (one narrow subcategory). The untested hypothesis is that hard categorical type partitioning — classify the incoming failure into one of N discrete semantic types, then retrieve only from the type-matched sub-corpus — yields better precision in retrieving transferable fix templates than ReinFix's joint embedding, because bugs within a type share syntactic fix motifs that bugs with merely similar code but different root causes do not. DebugBench uniquely provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python; crucially, these ground-truth labels enable direct calibration of the few-shot type classifier, turning classifier error propagation from a latent risk into a measurable experimental variable. The confidence-gated hybrid (fall back to soft retrieval for low-confidence classifications) addresses the structural risk of hard partitioning and has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884) for general RAG systems. M-RAG (ACL 2024, arXiv 2405.16420) additionally validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis before evaluating it in the code repair setting.",
  "landscape": "RELREPAIR (arXiv 2509.16701) retrieves relevant code from the same project using function names and comments, improving repair on Defects4J V1.2 by +17.1% and achieving 48.3% fix rate on ManySStuBs4J, but retrieves current project code rather than cross-repository historical fixes. RepoRepair (arXiv 2603.01048) achieves 45.7% on SWE-bench Lite via documentation-guided localization; the current SWE-bench Lite SOTA is approximately 62.7% (Claude Opus 4.6, May 2026) using agentic scaffolding — a different regime from FTCR's retrieval-only approach, which targets 20–35% with the same model and is not a SOTA claim. ReinFix (arXiv 2506.23100, ICSE 2026) is the closest prior work and primary baseline: it uses an LLM to generate a free-text root-cause description per bug, then embeds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning, and root cause is a continuous semantic descriptor, not a discrete category. SWE-Exp (arXiv 2507.23361, revised February 2026) is the most important concurrent work: it retrieves top N=10 issues 'most relevant in terms of error type' from an experience bank using soft cosine similarity over (issue-type + description) embeddings (Multilingual-E5-Large encoder), achieving 73.0% on SWE-bench Verified with Claude 4 Sonnet in a fully agentic pipeline. Three design differences distinguish SWE-Exp from FTCR: (1) retrieval mechanism — SWE-Exp uses soft cosine similarity with type as embedding metadata at retrieval time; FTCR partitions the index into discrete type sub-corpora at construction time, so only same-type pairs are ever candidates for a query; (2) retrieved artifact — SWE-Exp stores distilled problem perspectives and generalized modification strategies; FTCR retrieves concrete historical fix patches for direct template transfer; (3) scope — SWE-Exp is fully agentic and scoped to Python; FTCR is retrieval-only and covers C++, Java, and Python, using DebugBench's oracle type labels for cross-lingual calibration. The testable question SWE-Exp leaves open is whether hard construction-time partitioning outperforms soft retrieval-time type filtering for fix-template precision. TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) applies a 4-stage pipeline (localization → type ID → context selection → patch generation) with 10 defect types on Defects4J V1.2/V2.0 and QuixBugs, achieving 272% improvement over GPT-3.5 baseline. TypeRepair's context selection stage conditions on the identified defect type to select relevant within-project code context and to provide type-specific repair guidance in the LLM prompt — it does not retrieve from an external cross-repository fix corpus. TypeRepair is Java-only (Defects4J/QuixBugs); FTCR covers C++/Java/Python with external cross-repository retrieval of ~3,050 historical fix patches. TypeRepair validates that defect type identification benefits LLM-based repair (supporting FTCR's core hypothesis) while leaving hard-vs-soft type-partitioned cross-repository retrieval entirely unexplored; FTCR addresses this gap directly. Gu et al. (ICSE 2026, arXiv 2503.20589) empirically demonstrate that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% on CoderEval and RepoExec, while contextual code and API information helps; their proposed AllianceCoder retrieves APIs via semantic description matching rather than code similarity. While the study targets code generation rather than repair, the 'what to retrieve matters more than how' finding motivates FTCR's choice of fix patches retrieved by type partition (sharing semantic repair structure) over code-similarity retrieval (sharing only surface features). DynaFix (arXiv 2512.24635) outperforms ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair (236 bugs fixed with GPT-4); DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3 via self-directed debugging with runtime traces. Both update the Defects4J performance landscape but are orthogonal to FTCR's retrieval strategy focus — execution-level augmentation and retrieval strategy are independently improvable axes. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via LLM objective alignment. FTCR's structural departure from ReinFix is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) for a clean comparison that isolates partitioning as the primary architectural variable — noting that partitioning also reduces the effective retrieval pool to ~1/N_types of the full corpus, a corpus-size effect that a random-partition control ablation is designed to separate from type-matching precision. RetypeR (ICSME 2024, Hao et al.) applies a two-stage external+internal retrieval conditioned on Python type errors, establishing that type-specific retrieval helps for one narrow bug class and language; FTCR extends this principle to 18 categories across three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates that multi-partition RAG consistently outperforms single-store RAG across NLP tasks (summarization: +11%, translation: +8%, dialogue: +12%), validating the general principle of partition-based retrieval before applying it to code repair. PatchRecall (arXiv 2604.10481, April 2026) introduces history-based retrieval for file-level localization on SWE-bench — complementary (localization rather than cross-repository fix template retrieval). The APR survey (arXiv 2506.23749) reviews 63+ systems and identifies retrieval augmentation as the key enhancement, but no reviewed system applies hard taxonomic type classification as the retrieval partition key across multiple languages.",
  "approach": "We build FTCR (Failure-Type-Conditioned Retrieval), a pipeline whose central hypothesis is that hard categorical type partitioning of the retrieval index outperforms ReinFix-style soft root-cause embedding for cross-repository fix transfer. The key ablation — same model, same encoder (text-embedding-3-large, identical to ReinFix for a clean comparison), same corpus, varying only the indexing and retrieval key — isolates partitioning as the primary architectural variable, with the corpus-size confound separated by a random-partition control (see below).\n\nMotivation for Fix-Patch Retrieval by Type Rather Than Code Similarity. Gu et al. (ICSE 2026, arXiv 2503.20589) show that retrieving syntactically similar code snippets degrades repository-level code generation by up to 15% compared to retrieving structured knowledge; their finding generalizes to a principle: what you retrieve determines quality, and surface-level code similarity is a poor proxy for repair-relevant structure. FTCR embodies this principle: rather than retrieving the most syntactically similar buggy code in the corpus, we retrieve fix patches — input/output transformation pairs — that share the same semantic repair operation. Type partitioning ensures that a null-dereference query retrieves null-check insertion patches (same fix operator), not patches that happen to look syntactically similar but represent bounds-guard or API-substitution operations. Unlike TypeRepair (SQJ 2026), which uses defect type to condition prompt construction with within-project context, FTCR uses defect type to partition an external cross-repository corpus so that the retrieval pool contains only semantically aligned fix templates.\n\nRetrieval Corpus Construction. Four sources: the SWE-bench non-Lite split (~1,994 Python instances, post-2021 to reduce LLM contamination), BugsInPy (493 Python bugs, 17 projects), Defects4J V1.2 pre-filtered to Java-8-compatible bugs (~360 of 395, following the 91% reproducibility figure), and GitBug-Java (199 Java bugs from 2023 commits, isolated Docker environments). Total annotated corpus: approximately 3,050 natural bug-fix pairs (Python: ~2,487; Java: ~559).\n\nCorpus Sparsity Policy. Each pair is annotated with one of 18 semantic categories aligned with DebugBench's taxonomy (four major types: Syntax, Reference, Logic, Multiple; 18 minor subtypes) via few-shot prompting using DebugBench's labeled examples as demonstrations; three annotation passes measure inter-run consistency. A per-type instance count table is computed and reported in the paper for transparency. For the combined Python+Java corpus (3,050 pairs), 18-type analysis is viable: Python instances dominate (~2,487) and yield an estimated mean of ~138 pairs per type. For Java-only ablations (~559 pairs, ~31 per type average), a minimum-threshold policy applies: types with fewer than 30 Java instances are merged into nearest-neighbor supercategories (e.g., Concurrency + Resource-Leak → Resource-Management; Format-Error + Syntax-Error → Low-Level, since compiled Defects4J/GitBug-Java bugs contain near-zero syntax errors). Java ablation results are reported for the 6–8 resulting categories that each exceed 50 instances, with merged categories explicitly labeled. This avoids the degenerate case of k=5 retrieval from a 15-instance sub-index, which approximates exhaustive lookup rather than similarity-based retrieval.\n\nEncoder Specification. Primary encoder: text-embedding-3-large (OpenAI API), identical to ReinFix, to eliminate encoder choice as a confound; embedding cost is negligible (~$5–15 for corpus plus all evaluation queries at $0.13/1M tokens). Secondary ablation: CodeBERT-base substituted for both FTCR and the ReinFix-style baseline, verifying that the hard-vs-soft finding is not encoder-specific and deconfounding the encoder-vs-partitioning comparison.\n\nType Classifier Calibration on DebugBench Ground Truth. Since DebugBench provides oracle type labels for 4,253 instances, a held-out 20% split (851 instances) directly measures our few-shot classifier's per-type precision and recall against ground truth, yielding an overall accuracy estimate. Cross-dataset zero-shot agreement is measured by applying the same classifier to a 10% random sample (~56 pairs) of the Java annotation set (Defects4J + GitBug-Java) with human-verified labels as oracle, yielding a cross-lingual label consistency score. This produces the NLP contribution: a falsifiable empirical claim that LLM-inferred bug type labels achieve X% agreement with DebugBench ground-truth labels (Python/C++), transfer zero-shot to unseen Java bugs with Y% agreement, and are predictive of retrieval-augmented repair success — type-matched retrieval outperforms soft retrieval by Z% for correctly-classified bugs while underperforming by W% for misclassified bugs.\n\nRandom-Partition Control. To isolate the type-matching benefit from the corpus-size reduction effect — hard partitioning reduces the effective retrieval pool to ~1/N_types of the full index, which independently affects recall — we add a random-partition baseline (Variant F): the corpus is randomly partitioned into N equivalently-sized sub-indices, and each query retrieves from a randomly assigned sub-index. Any performance gap between FTCR (Variant E, hard type partition) and this control measures the precision benefit of type-matching net of pool-size reduction. This converts the comparison from 'clean but contested' to 'rigorous and unambiguous.'\n\nConfidence-Gated Retrieval Fallback. At inference time, the type classifier outputs a probability distribution over 18 categories. For instances where the top-class probability exceeds a calibrated threshold τ (tuned on held-out DebugBench validation split), FTCR applies hard type-partitioned retrieval. For instances below τ — typically multi-type or ambiguous bugs — it falls back to soft joint-embedding retrieval (identical to the ReinFix baseline). This confidence-gated hybrid is evaluated as a sixth system variant alongside: (A) text-similarity RAG (no type signal), (B) RELREPAIR (project-internal retrieval), (C) RepoRepair (documentation-guided), (D) ReinFix-style soft retrieval (re-implemented on same corpus and same encoder), (E) FTCR@hard-all, and (F) random-partition control (same N sub-indices, randomly assigned — corpus-size control). The confidence-gated fallback has principled precedent in CRAG (Yan et al., 2024; arXiv:2401.15884). The projected finding: correctly-classified high-confidence bugs show systematic gains from hard partitioning (+5–10% repair success on Defects4J where oracle type labels allow clean stratification); misclassified or low-confidence bugs show performance on par with or slightly below soft retrieval; the confidence gate recovers aggregate performance for ambiguous cases; the random-partition control falls between soft retrieval and FTCR@hard-all, confirming that type-matching rather than pool-size reduction drives the gain.\n\nPractical Utility: Retrieval as an Independently Upgradeable Module. FTCR's 20–35% standalone resolve rate on SWE-bench Lite is deliberately positioned as the retrieval contribution in isolation, not a claim against the agentic pipeline ceiling. The motivation for isolating retrieval is architectural: DynaFix (arXiv 2512.24635) demonstrates that execution-level augmentation and retrieval strategy are independently improvable axes — it improves over ReinFix on Defects4J V2.0 by adding iterative execution feedback while keeping retrieval fixed. An improved retrieval module (FTCR vs. ReinFix-style soft retrieval) compounds with execution-level improvements: the delta between FTCR-augmented and ReinFix-augmented iterative repair pipelines measures the retrieval contribution at the pipeline level. Standalone evaluation isolates the retrieval hypothesis cleanly; the modular gain is what ICSE reviewers can act on independently of scaffolding choices.\n\nExpected Performance on SWE-bench Lite. We project FTCR to achieve 20–35% resolve rate with Claude Sonnet 4.6 in retrieval-only (non-agentic) mode, comparable to ReinFix-style retrieval on the same corpus. This is below the current SWE-bench Lite SOTA (~62.7%, Claude Opus 4.6, May 2026, agentic scaffolding) and below RepoRepair's 45.7% (documentation-guided multi-step localization). Lower aggregate performance than RepoRepair is explicitly defended: FTCR does not incorporate documentation-guided localization, which is an orthogonal architectural component. The primary SWE-bench Lite contribution is validating that the type-conditioned advantage observed on DebugBench transfers to real-world Python repositories, not claiming absolute SOTA.\n\nDebugBench's synthetic-bug domain gap (LeetCode code, GPT-4-implanted bugs) is acknowledged; DebugBench results serve as type-controlled ablations with oracle labels while SWE-bench Lite validates real-world transfer.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~88 H100-hours (~150 A100-hours equivalent)",
      "gpu_utilization": "~30-40% utilized; high idle while researchers design annotation prompts, debug Defects4J Java-8 environments, manually review per-type count tables, and verify annotation consistency across passes",
      "timeline": "4-6 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$450 (150 A100-hours × $3/h on RunPod/Lambda Labs)",
      "embedding_api_cost": "~$5-15 (text-embedding-3-large for 3,050-pair corpus + evaluation queries, at $0.13/1M tokens; negligible relative to overall budget)",
      "note": "Well within the 200 H100-hour hard budget"
    },
    "human_in_loop": {
      "gpu_hours": "~165 H100-hours (~280 A100-hours equivalent)",
      "gpu_utilization": "~55-65% utilized; agent continuously queues embedding and evaluation jobs while human approves ablation configurations at decision gates",
      "timeline": "6-8 weeks",
      "team": "1 researcher, ~30 min/day check-in for ablation approval, per-type count table review, confidence threshold tuning, and failure triage",
      "claude_api_cost": "$200-400 (annotation: ~3,050 instances × ~$0.02/call ≈ $61; 3 annotation passes for consistency ≈ $183; DebugBench classifier calibration: 851 held-out instances × $0.02 ≈ $17; pipeline orchestration and repair: ~1,500 agent turns × $0.10/turn ≈ $150; buffer ~$50)",
      "embedding_api_cost": "~$5-15 (text-embedding-3-large for corpus and evaluation queries)",
      "estimated_gpu_cost": "~$840 (280 A100-hours × $3/h)",
      "note": "Within the 200 H100-hour hard budget",
      "risk_note": "Defects4J Docker reproducibility is the primary bottleneck — the Java-8 pre-filter eliminates ~9% upfront, but remaining instances still require environment triage. GitBug-Java's isolated Docker images significantly reduce this overhead for the Java supplement. Java per-type sparsity is the secondary risk: if the 6-8 type categories above threshold have unequal sizes, the Java ablation may be underpowered for the smallest categories."
    },
    "auto_research": {
      "gpu_hours": "~190 H100-hours (~323 A100-hours equivalent; capped to stay within 200 H100-hour budget)",
      "gpu_utilization": "near-zero idle; agent continuously queues DebugBench and SWE-bench Lite evaluation runs in parallel with index-rebuild experiments across taxonomy granularity variants",
      "ablation_scope": "Hard vs. soft retrieval key comparison (FTCR vs. ReinFix-style baseline), random-partition control (N equivalent-size random sub-indices to isolate type-matching from pool-size effect), confidence-gated hybrid (threshold τ sweep), taxonomy granularity (6-type coarse / 18-type fine / merged-Java), retrieval k (1/3/5/10), encoder choice (text-embedding-3-large primary / CodeBERT-base secondary), cross-dataset generalization (Defects4J-Java train → SWE-bench-Lite Python eval), classifier accuracy stratification (by confidence band)",
      "timeline": "10-14 days with 2 A100 nodes running in parallel",
      "team": "0 (initial ~4h setup for corpus pipeline, per-type sub-index construction scaffold, random-partition control scaffold, confidence-gated hybrid logic, and Docker environment configuration)",
      "claude_api_cost": "$500-850 (3-pass annotation of 3,050 pairs ≈ $183; DebugBench classifier calibration ≈ $17; multi-run orchestration ~5,000 agent turns × $0.10 ≈ $500; buffer ~$150)",
      "embedding_api_cost": "~$10-20 (text-embedding-3-large for corpus + all evaluation query embeddings; CodeBERT-base is self-hosted, no API cost)",
      "estimated_gpu_cost": "~$969 (323 A100-hours × $3/h)",
      "speed_bottleneck": "GPU count (single A100 serializes SWE-bench Lite at ~10 min/instance; 2+ nodes needed for meaningful parallelism) and Claude API rate limits on concurrent classification calls",
      "risk_note": "Auto-assigned bug type labels may drift from human-interpretable categories without the three-pass consistency check; the confidence-gated hybrid adds a hyperparameter (τ) that requires tuning on the DebugBench held-out split before SWE-bench Lite evaluation. SWE-bench Lite infrastructure failures can silently inflate repair failure counts without human oversight."
    }
  },
  "target_venues": [
    "ICSE 2027 (mandatory abstract deadline June 23, 2026 — SOLE PRIMARY TARGET; best fit for SE audience; full ReinFix comparison on Defects4J V1.2 provides the direct head-to-head evaluation reviewers will expect; TypeRepair (SQJ 2026) comparison on Defects4J clarifies FTCR's orthogonal contribution of cross-repository retrieval; per-type corpus sparsity table, random-partition control, and confidence-gated ablation address the three most likely reviewer objections about hard partitioning; random-partition control specifically converts the 'corpus-size confound' objection into a closed experimental question)",
    "FSE 2027 (full paper deadline October 2, 2026 — backup venue if ICSE review cycle overlaps unfavorably; same SE audience, equally appropriate for a retrieval-architecture study with multi-language empirical evaluation)"
  ],
  "level": "solid",
  "key_references": [
    "ReinFix: Repair Ingredients Are All You Need — Improving LLM-Based Program Repair via Repair Ingredients Search (ICSE 2026, arXiv 2506.23100) [primary competing baseline; must compare directly on Defects4J V1.2 using same text-embedding-3-large encoder; uses a unified vector database, not a specific named implementation]",
    "SWE-Exp: Experience-Driven Software Issue Resolution (arXiv 2507.23361, revised February 2026) [most important concurrent work; retrieves top N=10 issues by soft cosine similarity over (issue-type + description) embeddings using Multilingual-E5-Large; stores distilled modification strategies, not fix patches; agentic, Python-only; achieves 73.0% on SWE-bench Verified with Claude 4 Sonnet — differentiate by hard vs. soft partitioning at index-construction time, fix-template vs. strategy retrieval, and multi-language scope]",
    "TypeRepair: Towards Defect-Type-Aware Adaptive Program Repair: A Stage-Wise Approach with Large Language Models (Zhang et al., SQJ 2026, doi:10.1007/s11219-026-09751-w) [4-stage pipeline with 10 defect types on Defects4J V1.2/V2.0/QuixBugs (Java-only); validates that type conditioning improves LLM repair; context selection stage conditions type to select within-project context and generate type-specific prompting guidance, NOT cross-repository retrieval — FTCR's orthogonal contribution is type-conditioned retrieval of fix patches from an external ~3,050-pair cross-language corpus; must cite and explicitly differentiate]",
    "What to Retrieve for Effective Retrieval-Augmented Code Generation? An Empirical Study and Beyond (Gu et al., ICSE 2026, arXiv 2503.20589) [shows similar-code snippet retrieval degrades repository-level code generation by up to 15% on CoderEval/RepoExec while contextual + API info helps; motivates FTCR's type-conditioned fix-patch retrieval — type partitioning retrieves patches sharing semantic repair structure, not superficial code similarity; note the finding applies to code generation not repair, but the 'what to retrieve matters' principle is directly applicable]",
    "ReCode: Improving LLM-based Code Repair with Fine-Grained Retrieval-Augmented Generation (CIKM 2025, arXiv 2509.02330) [algorithm-type-conditioned retrieval in competitive programming — conceptual ancestor]",
    "RetypeR: Integrated Retrieval-based Automatic Program Repair for Python Type Errors (ICSME 2024, Hao et al.) [type-specific retrieval for one language and one error class — FTCR extends to 18 types and 3 languages]",
    "DynaFix: Iterative Automated Program Repair Driven by Execution-Level Dynamic Information (arXiv 2512.24635) [surpasses ReinFix on Defects4J V2.0 (236 bugs with GPT-4) using execution-level augmentation; demonstrates retrieval and execution augmentation are independently improvable axes; retrieval improvement (FTCR) compounds with execution-level improvements (DynaFix-style)]",
    "DebugRepair: Enhancing LLM-Based Automated Program Repair via Self-Directed Debugging (arXiv 2604.19305) [295 Defects4J bugs with DeepSeek-V3 via runtime traces and debugging-driven conversational repair; updates Defects4J landscape but is orthogonal — no retrieval augmentation component]",
    "D4C: Aligning the Objective of LLM-based Program Repair (ICSE 2025, arXiv 2404.08877) [180 Defects4J bugs via objective alignment; updates Defects4J performance landscape]",
    "M-RAG: Reinforcing Large Language Model Performance through Retrieval-Augmented Generation with Multiple Partitions (ACL 2024, arXiv 2405.16420) [multi-partition RAG validated on NLP tasks: +11% summarization, +8% translation, +12% dialogue; principled precedent for partition-based retrieval across domains]",
    "RELREPAIR: Enhancing Automated Program Repair by Retrieving Relevant Code (arXiv 2509.16701) [project-internal retrieval baseline]",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048) [documentation-guided localization baseline; 45.7% on SWE-bench Lite using multi-step localization, orthogonal to FTCR's retrieval focus]",
    "DebugBench: Evaluating Debugging Capability of Large Language Models (ACL Findings 2024) [primary evaluation with ground-truth 18-category labels across C++/Java/Python; held-out 20% split used for few-shot classifier calibration; synthetic-bug limitation acknowledged]",
    "GitBug-Java: A Reproducible Benchmark of Recent Java Bugs (MSR 2024, arXiv 2402.02961) [199 recent Java bugs in isolated Docker environments; supplement for Defects4J Java corpus]",
    "SWE-smith: Scaling Data for Software Engineering Agents (NeurIPS 2025, arXiv 2504.21798) [50k Python task instances from 128 repos; used as scale corpus for Python retrieval index]",
    "A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications (arXiv 2506.23749) [63-system survey confirming retrieval augmentation as key enhancement with no type-partitioned system identified]",
    "What Do They Fix? LLM-Aided Categorization of Security Patches (NDSS 2026, arXiv 2509.22796) [confirms LLM-based bug taxonomy inference is practical at scale]",
    "PatchRecall: Patch-Driven Retrieval for Automated Program Repair (arXiv 2604.10481) [history-based retrieval for file localization — complementary scope]",
    "RAP-Gen: Retrieval-Augmented Patch Generation with CodeT5 (ESEC/FSE 2023) [text-similarity RAG baseline]",
    "CRAG: Corrective Retrieval Augmented Generation (Yan et al., 2024; arXiv:2401.15884) [confidence-gated fallback mechanism with retrieval quality scoring; precedent for the FTCR confidence-gated hybrid variant; note: withdrawn from ICLR 2025, unpublished — cite as preprint only]"
  ],
  "description": "FTCR tests a specific hypothesis in retrieval-augmented program repair: hard categorical type partitioning of the retrieval index outperforms soft root-cause-augmented retrieval (ReinFix's approach, ICSE 2026) for cross-repository fix template transfer. ReinFix (ICSE 2026, arXiv 2506.23100) is the closest prior work — it embeds LLM-generated free-text root-cause descriptions jointly with buggy code into a unified vector database using text-embedding-3-large, showing +32/+38 bugs fixed on Defects4J V1.2/V2.0. FTCR's structural departure is to (1) classify incoming failures into one of 18 discrete semantic categories aligned with DebugBench's empirically-validated taxonomy, and (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) to isolate partitioning as the primary architectural variable. Round 5 revisions address four issues: (a) TypeRepair (SQJ 2026, Zhang et al., doi:10.1007/s11219-026-09751-w) added to landscape and key_references with explicit differentiation — TypeRepair's 4-stage pipeline uses defect type to select within-project context and generate type-specific repair guidance (prompt engineering), not cross-repository retrieval; it covers Java only (Defects4J/QuixBugs) with 10 types; TypeRepair validates that type conditioning helps repair (supporting FTCR's hypothesis) while leaving cross-repo type-conditioned retrieval unexplored; (b) arXiv 2503.20589 (Gu et al., ICSE 2026) added as motivation rather than counterevidence — their finding that similar code snippet retrieval degrades code generation by 15% while structured knowledge helps motivates FTCR's type-conditioned fix-patch retrieval; type partitioning retrieves patches sharing semantic repair structure (the fix operator), not superficial code similarity; the paper targets code generation, not repair, making it an indirect motivator rather than a direct challenge; (c) practical utility framing added explicitly in approach — retrieval is an independently upgradeable module within agentic pipelines; DynaFix demonstrates retrieval and execution augmentation are independent axes; FTCR's retrieval gain compounds with DynaFix-style iterative repair; 20-35% standalone metric is the retrieval floor, not the pipeline ceiling; (d) EMNLP 2026 definitively removed — the May 25 ARR deadline is infeasible given that all experiments remain to be run; ICSE 2027 is the sole primary target; FSE 2027 is the backup; cross-lingual classifier findings can be submitted separately after ICSE results are complete. RetypeR (ICSME 2024) establishes type-specific retrieval for Python type errors specifically; FTCR extends to 18 categories across C++, Java, and Python. The retrieval corpus (~3,050 natural bug-fix pairs from SWE-bench non-Lite, BugsInPy, Defects4J V1.2, and GitBug-Java) requires no GPU training; the approach is fully inference-based. Target venues: ICSE 2027 (abstract June 23, primary), FSE 2027 (October 2, backup).",
  "project_name": "failure_type_rag_repair",
  "source": "web_research"
}

## Reviewer feedback (round 5)
Issues: ["CRITICAL — Target venue violates user requirements: The user explicitly requested EMNLP 2026 (ARR deadline May 25, 2026, 15 days from today). The proposal now targets ICSE 2027 (abstract June 23, 2026) exclusively, a full year late and a different research community. Previous reviewers flagged EMNLP as infeasible given experiment state, but the requirement was not to change venues — it was to make the idea work within the constraint. If auto-research starts immediately (day 0), 10–14 days of experiments complete by ~May 23, leaving 2 days to finalize the paper for the May 25 ARR deadline. This is technically achievable but requires an explicit, committed execution plan with the NLP framing (X%/Y%/Z%/W% classifier calibration finding) as the lead contribution. The proposal must either restore EMNLP 2026 as the primary target with a day-by-day execution schedule, or explicitly acknowledge that it fails the user's venue constraint and accept that verdict.", "HIGH — 16-day timeline constraint met only by auto-research mode: The user's hard constraint is ≤16 days. Manual mode (4–6 months) and human-in-loop mode (6–8 weeks) exceed this by 8–12× and should not appear as viable execution paths in resource_estimate. The paper should flag auto-research (10–14 days) as the only constraint-compliant mode, or restructure the three modes to reflect feasible timelines.", "MEDIUM — InferFix (ESEC/FSE 2023, arXiv:2303.07263) is unmentioned prior art: Independently confirmed that InferFix uses bug type annotations and contrastive learning to retrieve 'semantically equivalent bugs and corresponding fixes of the same bug type' from an external repository corpus (InferredBugs, thousands of Java and C# repos). This is the closest non-trivial precursor to type-conditioned cross-repo repair retrieval and is not cited anywhere in the proposal. ICSE 2027 reviewers familiar with the APR literature will notice its absence. FTCR should differentiate explicitly: InferFix uses soft contrastive similarity (learned embedding grouping) not hard categorical index partitioning; it targets Java/C# from Infer static analysis findings, not the 18-category natural-bug taxonomy; and the corpus construction and evaluation differ. This differentiation is achievable in one paragraph but must be present.", "MEDIUM — Cross-system corpus quality confound inadequately flagged: The 'clean comparison' correctly uses the same 3,050-pair natural corpus for both FTCR and the ReinFix-style baseline, isolating partitioning as the variable. But any performance comparison against the published ReinFix results uses 100K TRANSFER corpus pairs (synthetic, from static analysis), creating a corpus quality × retrieval architecture confound that the random-partition control does not address. The paper must explicitly state: (a) intra-corpus ablations (FTCR vs. re-implemented ReinFix on 3,050 pairs) test the partitioning hypothesis cleanly, and (b) absolute comparisons against published ReinFix results reflect both architecture and corpus quality differences simultaneously.", "LOW — TypeRepair context-selection scope unverifiable from publicly accessible sources: The critical differentiation claim — that TypeRepair's Stage 3 selects within-project context only, not from an external cross-repo corpus — could not be independently confirmed due to paywall access to the SQJ article. The proposal states this confidently; it should note the evidentiary basis (e.g., 'TypeRepair evaluates exclusively on Defects4J/QuixBugs, which are within-project datasets, and the paper's supplementary prompt templates confirm type-specific in-project context selection rather than external retrieval') to avoid a reviewer flagging this differentiation as unsubstantiated."]
Feedback: This is the most polished version of FTCR to date. The random-partition control, confidence-gated hybrid, per-type merge policy, and ReinFix/SWE-Exp/TypeRepair differentiation all reflect genuine methodological rigor. Two actions would bring this to pass: (1) VENUE DECISION — the proposal must choose one of two paths and commit fully: either (a) restore EMNLP 2026 ARR (May 25) as the primary target with a specific day-by-day execution schedule (day 0-13: auto-research runs corpus annotation + DebugBench classifier calibration + Defects4J V1.2 ablations; day 13-15: paper writing with NLP lead framing the X%/Y%/Z%/W% falsifiable classifier finding), acknowledging the extreme timeline pressure; or (b) explicitly declare that the user's requirement cannot be met for EMNLP 2026 and accept ICSE 2027 as the sole target with a verdict of 'fail' on the original requirement. Leaving both venues while targeting neither by the May 25 deadline is a planning failure. (2) ADD INFERFIX — one paragraph in the landscape: 'InferFix (ESEC/FSE 2023, arXiv:2303.07263) retrieves fixes for bugs of the same type using contrastive-learned embeddings over bug type annotations, establishing type-aware retrieval for Java/C# static analysis bugs. FTCR differs in three respects: (a) hard categorical index partitioning at construction time rather than soft contrastive similarity at retrieval time; (b) 18-category natural-bug taxonomy across C++/Java/Python rather than InferBugs' Infer-specific defect categories; (c) direct comparison of hard vs. soft type conditioning as the scientific contribution.' If these two issues are resolved, the novelty and feasibility scores reach 3.5+ and the paper is close to a pass for ICSE 2027 (though not EMNLP 2026 unless the execution plan is credible).

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
这个 idea 已经经过 5 轮修订，近 3 轮的平均分从 3.5 到 3.2，没有明显改善。

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
  "promptId": "66948f3e-e47a-48d4-b2e4-79c02c6dc755",
  "type": "user",
  "uuid": "9396f90b-5c8c-4670-920a-34642ddeeb33",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T06:32:57.337Z_

```json
{
  "parentUuid": "9396f90b-5c8c-4670-920a-34642ddeeb33",
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
  "uuid": "79420c29-bee0-49e2-8182-f337ce77c482",
  "timestamp": "2026-05-10T06:32:57.337Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T06:32:57.337Z_

```json
{
  "parentUuid": "79420c29-bee0-49e2-8182-f337ce77c482",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5ff22b74-26f7-4ba9-b6f8-b54f9a186d00",
  "timestamp": "2026-05-10T06:32:57.337Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
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
  "leafUuid": "5ff22b74-26f7-4ba9-b6f8-b54f9a186d00",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Program Repair by EMNLP 2026",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Assistant

_source line 8 · 2026-05-10T06:33:25.540Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the situation carefully before deciding on the approach.

**Key Issues to Address:**

1. **CRITICAL**: EMNLP 2026 (ARR May 25, 2026) venue requirement - the proposal dropped this but the user explicitly wanted it. Need to either restore it with a credible execution plan OR explicitly declare failure.

2. **HIGH**: 16-day timeline constraint - only auto-research mode is viable.

3. **MEDIUM**: InferFix (ESEC/FSE 2023, arXiv:2303.07263) is missing from prior art.

4. **MEDIUM**: Cross-system corpus quality confound needs explicit flagging.


5. **LOW**: TypeRepair context-selection scope evidentiary basis.

After five rounds without significant score improvement, I'm questioning whether there are deeper structural problems here. The EMNLP versus ICSE tension is fundamental—this is an SE paper trying to fit an NLP venue, unless we lean harder into the NLP angle around classifier calibration metrics. InferFix is a genuine gap that needs addressing. And the core hypothesis about hard type partitioning seems to be getting lost in the execution.

I need to research InferFix directly, reassess whether EMNLP 2026 is actually viable, and decide if this requires a major revision. The venue choice alone would reshape the entire framing, and InferFix changes what we're competing against. With the ARR deadline just 15 days away and only 2-3 days for writing after research, the timeline is extremely tight but technically feasible if I move fast.

The core tension is that this is fundamentally an SE paper about automated repair, but EMNLP wants the NLP angle—classifier calibration—as the lead contribution. That's a risky reframing under time pressure, and submitting a rushed paper to the wrong venue could easily fail. I need to decide whether to commit fully to EMNLP with a credible execution plan or accept that ICSE 2027 is the more realistic target.

The reviewer's point is clear: if auto-research starts immediately, I could have experiments done by May 23 and finalize by the May 25 ARR deadline, but only with an explicit, committed plan. So I'm going to research InferFix and related work on type-conditioned retrieval for code repair, check the EMNLP 2026 ARR details, and then decide whether to restructure the proposal around the NLP framing or pivot to ICSE. I'll spawn a research agent to handle this in parallel while I think through the execution plan.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ff22b74-26f7-4ba9-b6f8-b54f9a186d00",
  "isSidechain": false,
  "requestId": "req_011CatRNGXVQT12yakpXWCXw",
  "type": "assistant",
  "uuid": "fe2c9e0c-ac23-4f77-89ea-d3bc2f2c03fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017vq6qkgvpRRHFX3X3mwqoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17485,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17485,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1452,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17485
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

_source line 9 · 2026-05-10T06:33:25.592Z_

I'll start by researching InferFix and related papers before making the revisions. Let me spawn a research agent to investigate the key gaps.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "fe2c9e0c-ac23-4f77-89ea-d3bc2f2c03fe",
  "isSidechain": false,
  "requestId": "req_011CatRNGXVQT12yakpXWCXw",
  "type": "assistant",
  "uuid": "30e704d7-a43f-462c-a5e9-68308edf89ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017vq6qkgvpRRHFX3X3mwqoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17485,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17485,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1452,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17485
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

_source line 10 · 2026-05-10T06:33:33.897Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01YBLpi6t6XwtHNzAgnS7WDZ`</summary>

```json
{
  "description": "Research InferFix and EMNLP feasibility for code repair paper",
  "subagent_type": "Explore",
  "prompt": "I need you to fetch and summarize key information from several papers for a research proposal revision. Please use WebFetch to read these papers and report back.\n\n1. **InferFix** (arXiv:2303.07263) - Fetch https://arxiv.org/abs/2303.07263 and read the abstract + methods section. I need to know:\n   - What type annotations does it use?\n   - How does contrastive learning retrieve fixes \"of the same bug type\"?\n   - What corpus (InferredBugs) and languages (Java/C#)?\n   - Is it hard categorical partitioning or soft similarity?\n   - How does it compare to FTCR's approach?\n\n2. **EMNLP ARR May 2026 deadline** - Search for \"EMNLP 2026 ARR deadline\" or \"ACL ARR 2026 May submission deadline\" to confirm the exact deadline. Try fetching https://2026.emnlp.org or https://aclrollingreview.org/dates\n\n3. **Recent type-conditioned code repair papers** - Search for any 2025-2026 papers that use \"bug type\" or \"defect type\" for retrieval-augmented repair that might be missing from this survey. Search arxiv for \"type-conditioned retrieval program repair 2025\" or \"defect type retrieval automated program repair\".\n\n4. **InferFix citations** - Search for papers that cite InferFix or build on it: \"InferFix\" site:arxiv.org OR \"type-aware retrieval program repair\"\n\nPlease fetch the actual paper pages and report concrete details, not guesses."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "30e704d7-a43f-462c-a5e9-68308edf89ca",
  "isSidechain": false,
  "requestId": "req_011CatRNGXVQT12yakpXWCXw",
  "type": "assistant",
  "uuid": "7867d648-2bdb-45e8-9777-0e46a99a701f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_017vq6qkgvpRRHFX3X3mwqoL",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 17485,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1452,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17485,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1452,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 17485,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17485
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

_source line 11 · 2026-05-10T06:35:37.721Z_

<details><summary>↩ Tool result · `toolu_01YBLpi6t6XwtHNzAgnS7WDZ`</summary>

```text
Perfect! I now have comprehensive information. Let me compile the final summary for the user.

---

## Summary Report: Research Proposal Information

I've completed a thorough search and fetch of the resources you requested. Here are the key findings:

### 1. **InferFix (arXiv:2303.07263) - Technical Details**

**Type Annotations:**
- InferFix uses **bug type annotations** from the Infer static analyzer (specifically focusing on null dereferences, resource leaks, and thread safety violations)
- The system crafts prompts carrying: bug type annotation, location information, relevant syntax hierarchies, and similar fixes from historic database

**Contrastive Learning & Retrieval Mechanism:**
- The Retriever component is "pretrained via contrastive learning objective, which aims at searching for **semantically equivalent bugs and corresponding fixes**"
- This employs a **hybrid approach**: combines bug type annotations (categorical) with "semantically similar fixes retrieved from an external non-parametric memory" (soft similarity based on continuous embeddings)
- It is **NOT hard categorical partitioning** but rather soft semantic similarity scoring
- Contrastive learning learns relationships between bugs and fixes in semantic space, allowing retrieval based on semantic closeness

**InferredBugs Corpus:**
- Metadata-rich dataset of bugs extracted by executing Infer static analyzer on change histories of thousands of **Java and C# repositories**
- Organized by programming language with distinct folders for Java and C#
- Dataset publicly available on GitHub (microsoft/InferredBugs)

**Performance:**
- Top-1 accuracy: **65.6% for C# and 76.8% for Java**
- Outperforms LLM baselines (code-cushman-001, text-davinci-003) with 11-55% relative improvement across bug types

**FTCR Comparison:**
- **Not found** in InferFix paper itself; however, FTCR refers to general "Fine-Tuning Code Repair" approaches
- InferFix differs by combining retrieval-augmented generation (RAG) with contrastive pre-training on a Retriever model
- InferFix achieves better results than fine-tuning-only baselines through hybrid retrieval + generation strategy

### 2. **EMNLP 2026 ARR Deadline - CONFIRMED**

**Deadline: May 25, 2026** (11:59 PM UTC-12:00 / Anywhere on Earth)

**Critical Note:** Since EMNLP and AACL share the ARR May 2026 cycle, authors must **explicitly select a target conference at submission time**, and this choice is binding.

**Other Key Dates:**
- Author registration form: Due May 27, 2026 EoD AoE
- Review completion: July 6 or meta-reviews by July 29
- Meta-review release: July 30, 2026
- EMNLP commitment deadline: August 2, 2026
- Acceptance notification: August 20, 2026

### 3. **Recent Type-Conditioned/Defect-Type-Aware Program Repair Papers (2025-2026)**

**TypeRepair (2026)** - Most directly relevant new work:
- Published: Software Quality Journal, 2026
- **Ten defect types** with tailored repair guidance
- Multi-stage framework: defect localization → defect type identification → context selection → patch generation
- Performance: 272.73% improvement over baseline LLM (GPT-3.5), 257.89% improvement (GPT-4) on Defects4J v2.0
- Independently repairs 33 bugs that no other method successfully fixes

**ReCode (2025)** - Algorithm-aware retrieval:
- Fine-grained retrieval-augmented generation
- **Algorithm-aware module** uses multi-label classification for algorithmic intent (recognizes that code integrates multiple paradigms)
- Narrows search space using algorithm type predictions
- Significantly reduces inference cost (3-4x fewer LLM calls in out-of-distribution settings)

**RetypeR (2024, ICSME)**:
- Retrieval-based repair for Python type errors
- Two-stage approach: external retrieval (from repositories) + internal retrieval
- AST-based retrieval method for fix patterns
- Evaluated on TypeBugs and BugsInPy benchmarks

**ReAPR (2025)**:
- Retrieval-augmented framework using CodeLlama(7B)
- Investigated two retrieval techniques: BM25 and Dense Passage Retrieval (DPR)
- Fixed 68 bugs (DPR) and 59 bugs (BM25)

### 4. **InferFix Citations & Related Work (2024-2025)**

InferFix is cited in:
- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1) - covers 62+ LLM-based repair systems (Jan 2022 - June 2025)
- Recent program repair surveys consistently reference InferFix as a key retrieval-augmented approach
- Microsoft Research blog: "Microsoft at ESEC/FSE 2023: AI techniques for a streamlined coding workflow"

**Related Type-Aware Approaches:**
- **ComPass**: Uses contrastive learning for patch correctness assessment
- **ContraCode**: Contrastive learning for type inference (8.9% improvement over TypeScript's built-in)
- **PyTy**: Gradual-typing error repair in Python with mypy diagnostics injected into sequences

### Key Insight for Your Proposal

The **critical distinction** in type-conditioned approaches is:
- **InferFix**: Uses Infer's hard bug types + soft semantic retrieval (hybrid)
- **ReCode**: Uses algorithmic category classification (multi-label, not hard partitioning)
- **TypeRepair**: Uses ten explicit defect types with tailored reasoning per type
- The trend is moving toward **explict type/defect categorization** combined with **adaptive, multi-stage reasoning** rather than pure semantic retrieval

---

**Sources:**
- [InferFix: End-to-End Program Repair with LLMs](https://arxiv.org/abs/2303.07263)
- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)
- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)
- [ReCode: Improving LLM-based Code Repair](https://arxiv.org/html/2509.02330v1)
- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)
- [RetypeR at ICSME 2024](https://conf.researchr.org/details/icsme-2024/icsme-2024-papers/20/RetypeR-Integrated-Retrieval-based-Automatic-Program-Repair-for-Python-Type-Errors)
- [InferredBugs Dataset](https://github.com/microsoft/InferredBugs)
- [Infer Static Analyzer - All Issue Types](https://fbinfer.com/docs/all-issue-types/)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7867d648-2bdb-45e8-9777-0e46a99a701f",
  "isSidechain": false,
  "promptId": "66948f3e-e47a-48d4-b2e4-79c02c6dc755",
  "type": "user",
  "uuid": "58664c44-3058-41c5-ad37-fd18b6a63c82",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need you to fetch and summarize key information from several papers for a research proposal revision. Please use WebFetch to read these papers and report back.\n\n1. **InferFix** (arXiv:2303.07263) - Fetch https://arxiv.org/abs/2303.07263 and read the abstract + methods section. I need to know:\n   - What type annotations does it use?\n   - How does contrastive learning retrieve fixes \"of the same bug type\"?\n   - What corpus (InferredBugs) and languages (Java/C#)?\n   - Is it hard categorical partitioning or soft similarity?\n   - How does it compare to FTCR's approach?\n\n2. **EMNLP ARR May 2026 deadline** - Search for \"EMNLP 2026 ARR deadline\" or \"ACL ARR 2026 May submission deadline\" to confirm the exact deadline. Try fetching https://2026.emnlp.org or https://aclrollingreview.org/dates\n\n3. **Recent type-conditioned code repair papers** - Search for any 2025-2026 papers that use \"bug type\" or \"defect type\" for retrieval-augmented repair that might be missing from this survey. Search arxiv for \"type-conditioned retrieval program repair 2025\" or \"defect type retrieval automated program repair\".\n\n4. **InferFix citations** - Search for papers that cite InferFix or build on it: \"InferFix\" site:arxiv.org OR \"type-aware retrieval program repair\"\n\nPlease fetch the actual paper pages and report concrete details, not guesses.",
    "agentId": "ac2288b5aa261f364",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I now have comprehensive information. Let me compile the final summary for the user.\n\n---\n\n## Summary Report: Research Proposal Information\n\nI've completed a thorough search and fetch of the resources you requested. Here are the key findings:\n\n### 1. **InferFix (arXiv:2303.07263) - Technical Details**\n\n**Type Annotations:**\n- InferFix uses **bug type annotations** from the Infer static analyzer (specifically focusing on null dereferences, resource leaks, and thread safety violations)\n- The system crafts prompts carrying: bug type annotation, location information, relevant syntax hierarchies, and similar fixes from historic database\n\n**Contrastive Learning & Retrieval Mechanism:**\n- The Retriever component is \"pretrained via contrastive learning objective, which aims at searching for **semantically equivalent bugs and corresponding fixes**\"\n- This employs a **hybrid approach**: combines bug type annotations (categorical) with \"semantically similar fixes retrieved from an external non-parametric memory\" (soft similarity based on continuous embeddings)\n- It is **NOT hard categorical partitioning** but rather soft semantic similarity scoring\n- Contrastive learning learns relationships between bugs and fixes in semantic space, allowing retrieval based on semantic closeness\n\n**InferredBugs Corpus:**\n- Metadata-rich dataset of bugs extracted by executing Infer static analyzer on change histories of thousands of **Java and C# repositories**\n- Organized by programming language with distinct folders for Java and C#\n- Dataset publicly available on GitHub (microsoft/InferredBugs)\n\n**Performance:**\n- Top-1 accuracy: **65.6% for C# and 76.8% for Java**\n- Outperforms LLM baselines (code-cushman-001, text-davinci-003) with 11-55% relative improvement across bug types\n\n**FTCR Comparison:**\n- **Not found** in InferFix paper itself; however, FTCR refers to general \"Fine-Tuning Code Repair\" approaches\n- InferFix differs by combining retrieval-augmented generation (RAG) with contrastive pre-training on a Retriever model\n- InferFix achieves better results than fine-tuning-only baselines through hybrid retrieval + generation strategy\n\n### 2. **EMNLP 2026 ARR Deadline - CONFIRMED**\n\n**Deadline: May 25, 2026** (11:59 PM UTC-12:00 / Anywhere on Earth)\n\n**Critical Note:** Since EMNLP and AACL share the ARR May 2026 cycle, authors must **explicitly select a target conference at submission time**, and this choice is binding.\n\n**Other Key Dates:**\n- Author registration form: Due May 27, 2026 EoD AoE\n- Review completion: July 6 or meta-reviews by July 29\n- Meta-review release: July 30, 2026\n- EMNLP commitment deadline: August 2, 2026\n- Acceptance notification: August 20, 2026\n\n### 3. **Recent Type-Conditioned/Defect-Type-Aware Program Repair Papers (2025-2026)**\n\n**TypeRepair (2026)** - Most directly relevant new work:\n- Published: Software Quality Journal, 2026\n- **Ten defect types** with tailored repair guidance\n- Multi-stage framework: defect localization → defect type identification → context selection → patch generation\n- Performance: 272.73% improvement over baseline LLM (GPT-3.5), 257.89% improvement (GPT-4) on Defects4J v2.0\n- Independently repairs 33 bugs that no other method successfully fixes\n\n**ReCode (2025)** - Algorithm-aware retrieval:\n- Fine-grained retrieval-augmented generation\n- **Algorithm-aware module** uses multi-label classification for algorithmic intent (recognizes that code integrates multiple paradigms)\n- Narrows search space using algorithm type predictions\n- Significantly reduces inference cost (3-4x fewer LLM calls in out-of-distribution settings)\n\n**RetypeR (2024, ICSME)**:\n- Retrieval-based repair for Python type errors\n- Two-stage approach: external retrieval (from repositories) + internal retrieval\n- AST-based retrieval method for fix patterns\n- Evaluated on TypeBugs and BugsInPy benchmarks\n\n**ReAPR (2025)**:\n- Retrieval-augmented framework using CodeLlama(7B)\n- Investigated two retrieval techniques: BM25 and Dense Passage Retrieval (DPR)\n- Fixed 68 bugs (DPR) and 59 bugs (BM25)\n\n### 4. **InferFix Citations & Related Work (2024-2025)**\n\nInferFix is cited in:\n- [A Survey of LLM-based Automated Program Repair: Taxonomies, Design Paradigms, and Applications](https://arxiv.org/html/2506.23749v1) - covers 62+ LLM-based repair systems (Jan 2022 - June 2025)\n- Recent program repair surveys consistently reference InferFix as a key retrieval-augmented approach\n- Microsoft Research blog: \"Microsoft at ESEC/FSE 2023: AI techniques for a streamlined coding workflow\"\n\n**Related Type-Aware Approaches:**\n- **ComPass**: Uses contrastive learning for patch correctness assessment\n- **ContraCode**: Contrastive learning for type inference (8.9% improvement over TypeScript's built-in)\n- **PyTy**: Gradual-typing error repair in Python with mypy diagnostics injected into sequences\n\n### Key Insight for Your Proposal\n\nThe **critical distinction** in type-conditioned approaches is:\n- **InferFix**: Uses Infer's hard bug types + soft semantic retrieval (hybrid)\n- **ReCode**: Uses algorithmic category classification (multi-label, not hard partitioning)\n- **TypeRepair**: Uses ten explicit defect types with tailored reasoning per type\n- The trend is moving toward **explict type/defect categorization** combined with **adaptive, multi-stage reasoning** rather than pure semantic retrieval\n\n---\n\n**Sources:**\n- [InferFix: End-to-End Program Repair with LLMs](https://arxiv.org/abs/2303.07263)\n- [EMNLP 2026 Call for Main Conference Papers](https://2026.emnlp.org/calls/main_conference_papers/)\n- [ACL Rolling Review Dates](http://aclrollingreview.org/dates)\n- [ReCode: Improving LLM-based Code Repair](https://arxiv.org/html/2509.02330v1)\n- [A Survey of LLM-based Automated Program Repair](https://arxiv.org/html/2506.23749v1)\n- [RetypeR at ICSME 2024](https://conf.researchr.org/details/icsme-2024/icsme-2024-papers/20/RetypeR-Integrated-Retrieval-based-Automatic-Program-Repair-for-Python-Type-Errors)\n- [InferredBugs Dataset](https://github.com/microsoft/InferredBugs)\n- [Infer Static Analyzer - All Issue Types](https://fbinfer.com/docs/all-issue-types/)"
      }
    ],
    "totalDurationMs": 123816,
    "totalTokens": 42800,
    "totalToolUseCount": 29,
    "usage": {
      "input_tokens": 885,
      "cache_creation_input_tokens": 2328,
      "cache_read_input_tokens": 37828,
      "output_tokens": 1759,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2328
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 885,
          "output_tokens": 1759,
          "cache_read_input_tokens": 37828,
          "cache_creation_input_tokens": 2328,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2328,
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
      "otherToolCount": 29
    }
  },
  "sourceToolAssistantUUID": "7867d648-2bdb-45e8-9777-0e46a99a701f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-10T06:36:41.780Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the key information I need. Let me synthesize:

**InferFix Key Facts:**
- Uses **Infer static analyzer** bug type annotations (null dereferences, resource leaks, thread safety)
- Uses **contrastive learning** to learn embeddings for "semantically equivalent bugs and corresponding fixes"
- Corpus: **InferredBugs** - Java and C# repos
- Mechanism: **Hybrid** - combines categorical bug type with soft semantic similarity in continuous embedding space
- NOT hard categorical index partitioning
- 65.6% C# and 76.8% Java top-1 accuracy


- InferFix is constrained to Infer's detection capabilities (null dereferences, resource leaks, thread safety), whereas FTCR covers 18 natural bug categories across a broader spectrum
- The key technical difference is that InferFix learns soft embeddings where bug type acts as a signal but retrieval remains similarity-based, while FTCR partitions its index hard by category at construction time
- InferFix trains on static analysis artifacts from InferredBugs, whereas FTCR draws from real-world bug-fix pairs across SWE-bench, BugsInPy, and Defects4J
- InferFix evaluates against Infer-detected bugs while FTCR uses DebugBench and SWE-bench Lite

With the EMNLP deadline 15 days away, auto-research can realistically finish in 10-14 days, leaving 2-3 days for writing, which is extremely tight but technically feasible if I frame this as an NLP contribution from the start.

The core question needs to be whether LLM-inferred bug type labels match DebugBench ground truth and whether this signal improves retrieval—that's the NLP angle EMNLP will accept. Given the user's original request for EMNLP 2026 and that it's achievable, I'm committing to this timeline with a concrete day-by-day plan starting with the auto-research pipeline setup.

Over the next two weeks, I'll calibrate the classifier on held-out instances while annotating the corpus, then build the type-partitioned indices and run baseline comparisons. The ablations across DebugBench variants and SWE-bench follow, with control experiments and encoder comparisons filling the middle stretch. Results compilation and paper writing compress into the final days before the May 25 deadline.

Now I'm assessing what needs to change: restoring EMNLP as the target venue is the biggest shift since it reframes the entire paper from a software engineering angle to an NLP one. I also need to streamline the resource estimate to focus only on auto-research mode, add InferFix to the related work with proper differentiation, clarify the corpus confound issue in the methodology, and strengthen the evidentiary basis for TypeRepair. These revisions are substantial enough to warrant a complete rewrite of the JSON structure. as PRIMARY with specific execution plan. ICSE 2027 as backup.

2. **resource_estimate**: Remove manual and human-in-loop modes (they exceed the 16-day constraint). Keep only auto-research. Add a day-by-day execution schedule.

3. **landscape**: Add InferFix paragraph with proper differentiation.

4. **approach**: 
   - Add explicit corpus quality confound clarification
   - Note TypeRepair evidentiary basis
   - Frame NLP contribution (X%/Y%/Z%/W%) as LEAD

5. **key_references**: Add InferFix

6. **core_problem** and **opportunity**: May need minor updates to foreground the NLP angle

7. **description**: Update to reflect round 6 changes

For InferFix, I need to highlight how it differs from FTCR: it uses contrastive-learned embeddings to retrieve fixes for bugs of the same type, where the retriever is pretrained to cluster semantically equivalent bugs and fixes based on Infer's static-analysis bug type annotations. The key distinctions are that InferFix applies soft contrastive similarity at retrieval time rather than hard type partitioning, operates only on Infer-detectable defect categories rather than the broader 18-category taxonomy, and draws from a corpus generated by Infer's static analysis runs.

For the EMNLP framing, the core contribution is investigating whether LLM-inferred semantic bug type labels across the 18 categories align with ground-truth human annotations from DebugBench, and whether encoding this type signal as hard categorical retrieval partitioning outperforms softer root-cause-augmented retrieval approaches for cross-repository repair.

The empirical evaluation hinges on four key metrics: the few-shot LLM classifier accuracy against DebugBench ground truth, zero-shot cross-lingual transfer performance on Java bugs, repair improvement rates when instances are correctly classified under hard type partitioning versus soft retrieval, and repair degradation when misclassification occurs. Together these measurements reveal exactly when categorical type conditioning helps versus hurts — a finding directly applicable to any retrieval system relying on LLM-generated categorical labels. This is genuinely NLP-relevant because it centers on evaluating the quality and downstream reliability of LLM-generated annotations, which aligns with EMNLP's established focus.

Now I'm clarifying the path forward based on the reviewer feedback. For ICSE 2027, I need to resolve two core issues: commit to a specific venue and integrate InferFix into the work. For EMNLP 2026, there's an additional requirement of a credible execution plan. Since this is already the most polished version, the main work is committing to EMNLP 2026 with a detailed day-by-day timeline, adding InferFix to the landscape and references, explicitly flagging the corpus confound, and limiting the resource estimate to auto-research mode only. This is fundamentally a major revision focused on these targeted improvements.

I'm reconsidering whether to pivot given five rounds of stagnating scores, but the evidence suggests I shouldn't. The core hypothesis about hard categorical type partitioning outperforming soft embeddings is sound and testable. The reviewer's feedback indicates the real blockers were venue-related and the missing InferFix comparison, not fundamental flaws in the hypothesis itself. EMNLP 2026 does seem like the right fit since the work involves natural language processing and computational linguistics aspects, so I'll move forward with the structured revisions rather than abandoning the direction. Now I'm mapping out the specific sections I need to revise: clarifying the corpus confounds and TypeRepair's evidence base, anchoring everything to the NLP framing, then laying out a concrete day-by-day execution timeline for EMNLP 2026 with ICSE 2027 as a fallback, and adding InferFix to the references and landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "58664c44-3058-41c5-ad37-fd18b6a63c82",
  "isSidechain": false,
  "requestId": "req_011CatRa61Jy2KabsYvs6akh",
  "type": "assistant",
  "uuid": "cc1d6479-65ee-4f89-82e7-5889815f68ca",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UAttjTqVvNMuD2uu8UGaMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 29116,
      "output_tokens": 2874,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2874,
          "cache_read_input_tokens": 29116,
          "cache_creation_input_tokens": 3219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3219
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

_source line 13 · 2026-05-10T06:36:41.785Z_

Good, I have the InferFix details and EMNLP deadline confirmation. Let me now write the full revised proposal.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc1d6479-65ee-4f89-82e7-5889815f68ca",
  "isSidechain": false,
  "requestId": "req_011CatRa61Jy2KabsYvs6akh",
  "type": "assistant",
  "uuid": "8220dca2-e14f-4205-bb04-babcd6c5c21c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UAttjTqVvNMuD2uu8UGaMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 29116,
      "output_tokens": 2874,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2874,
          "cache_read_input_tokens": 29116,
          "cache_creation_input_tokens": 3219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3219
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

_source line 14 · 2026-05-10T06:36:41.903Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01W85buzks3zLxm8g3xkAVwm`</summary>

```json
{
  "query": "select:WebFetch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8220dca2-e14f-4205-bb04-babcd6c5c21c",
  "isSidechain": false,
  "requestId": "req_011CatRa61Jy2KabsYvs6akh",
  "type": "assistant",
  "uuid": "43b0448d-30c1-44e3-8a03-2f4c2436fca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01UAttjTqVvNMuD2uu8UGaMu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3219,
      "cache_read_input_tokens": 29116,
      "output_tokens": 2874,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3219,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2874,
          "cache_read_input_tokens": 29116,
          "cache_creation_input_tokens": 3219,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3219
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

_source line 15 · 2026-05-10T06:36:41.914Z_

<details><summary>↩ Tool result · `toolu_01W85buzks3zLxm8g3xkAVwm`</summary>

````text
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
  "parentUuid": "43b0448d-30c1-44e3-8a03-2f4c2436fca7",
  "isSidechain": false,
  "promptId": "66948f3e-e47a-48d4-b2e4-79c02c6dc755",
  "type": "user",
  "uuid": "e7c70c28-5e5c-46f8-8420-b2ee48924835",
  "toolUseResult": {
    "matches": [
      "WebFetch"
    ],
    "query": "select:WebFetch",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "43b0448d-30c1-44e3-8a03-2f4c2436fca7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "e7c70c28-5e5c-46f8-8420-b2ee48924835",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Program Repair by EMNLP 2026",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Assistant

_source line 18 · 2026-05-10T06:39:54.761Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough information to write the complete revised JSON. Let me compile what I know:

**InferFix (arXiv:2303.07263):**
- Uses Infer static analyzer bug type annotations (null dereferences, resource leaks, thread safety)
- Retriever pretrained via contrastive learning to bring semantically equivalent bugs+fixes closer in embedding space
- Bug type is an embedding-time signal, NOT a hard construction-time index partition
- Corpus: InferredBugs (Java and C# repos, Infer-detected bugs)
- Top-1 accuracy: 65.6% C#, 76.8% Java


- Published at ESEC/FSE 2023

For EMNLP 2026, I'm looking at the timeline—the ARR deadline is May 25 with only 15 days remaining, and auto-research would take 10-14 days leaving just 2 days for paper writing, which is technically possible but extremely tight. I need to restore EMNLP 2026 as the primary target with a concrete day-by-day execution plan, update the resource estimate to focus only on auto-research mode, and integrate InferFix into the landscape section.

Now I'm framing the NLP contribution carefully: the primary angle is an empirical study of how well few-shot LLMs assign semantic type labels to bugs and whether that accuracy translates to better retrieval-augmented repair outcomes. The core NLP question becomes measuring label assignment accuracy against DebugBench ground truth, with secondary findings around zero-shot cross-lingual transfer to Java and quantified downstream impacts on repair success rates for correctly-typed versus misclassified instances.

Generating the JSON structure... I'm refining the core problem statement to emphasize the NLP angle — measuring how accurately few-shot LLMs label bugs from the 18-category taxonomy, then testing whether correct labels enable hard categorical retrieval to outperform soft augmented approaches like ReinFix. DebugBench's ground-truth labels across C++, Java, and Python let me quantify both the classifier accuracy and the downstream repair gains or losses depending on label correctness. Now I'm mapping out the execution timeline, starting with the annotation pipeline and Docker setup for the Defects4J evaluation. bugs) and GitBug-Java (199 bugs).

Day 1-3 (May 11-13): Annotation completes (3,050 × 3 passes at ~$183 Claude API cost). DebugBench held-out calibration (851 instances, 20% split) measures few-shot classifier accuracy (X%); cross-lingual Java annotation sample (~56 pairs, human-verified) measures transfer accuracy (Y%). Per-type count table computed; merge policy applied for rare Java types.

Day 4-6 (May 14-16): Build type-partitioned sub-indices and ReinFix-style unified index (both using text-embedding-3-large, identical encoder). Run Defects4J V1.2 ablations across multiple variants including text-similarity RAG, ReinFix-style soft matching, and random-partition controls.

Day 7-9 (May 17-19): Evaluate all variants on DebugBench with confidence-gated hybrid approach and parameter sweeps, then test cross-dataset transfer on SWE-bench Lite with Python code. Stratify results by classifier confidence bands to see which predictions are reliable.

Day 10-12 (May 20-22): Run ablations on encoder choice, taxonomy granularity (coarse vs. fine-grained types), retrieval k values, and per-type repair success to understand what drives performance.

Day 13 (May 23): Compile results and start writing with the key classifier calibration findings as the opening contribution.

Day 14-15 (May 24-25): Finalize paper and submit to ARR.

The minimum viable submission focuses on classifier calibration metrics plus Defects4J ablations and controls, with SWE-bench Lite results included only if the pipeline finishes in time. I'm also noting that TypeRepair's evaluation is limited to within-project datasets like Defects4J and QuixBugs, where context selection pulls from the same project rather than external corpora. I'm settling on what I can actually verify: TypeRepair uses Defects4J and QuixBugs, which are within-project datasets, and the system retrieves context from the project being repaired rather than an external corpus. Now I'm organizing my findings into a structured JSON format to capture the key aspects of this work.

The core empirical question hinges on whether an LLM can accurately assign bug type labels from an 18-category taxonomy using DebugBench's ground-truth labels, and whether that categorical accuracy translates to better retrieval performance when partitioning by failure type versus using soft augmentation approaches like ReinFix for cross-repository fix transfer.

I'm measuring four key quantities to characterize when hard type conditioning helps: few-shot classifier accuracy against DebugBench labels, zero-shot cross-lingual transfer to Java, repair gains for correctly-classified bugs under hard partitioning, and repair losses for misclassified ones. This directly shows the downstream impact of label quality on retrieval-augmented repair.

Most retrieval-augmented repair systems either use code-text similarity matching or soft root-cause augmentation that embeds free-text descriptions alongside buggy code, but neither exploits the structural regularity that bugs of the same semantic type share.

InferFix and TypeRepair both validate that type information improves repair, but they use soft embeddings or in-project context selection rather than hard categorical partitioning of a cross-repository fix corpus. The key question is whether hard type-based retrieval partitioning actually outperforms these softer approaches when retrieving fixes from external repositories.

Recent empirical work shows that similar code snippet retrieval can actually hurt generation performance by up to 15%, while structured knowledge retrieval helps — this directly supports the idea that type-partitioned retrieval would avoid syntactic similarity traps by ensuring retrieved patches share the same repair structure. The main challenge is corpus sparsity: with only around 3,050 bug-fix pairs across 18 types, the retrieval index becomes quite sparse.

When a bug gets misclassified into the wrong type partition, the hard partitioning approach will underperform compared to soft retrieval methods, so the performance gains depend on how confident the classifier is. I'm addressing both issues by measuring classifier accuracy against ground-truth labels and adding a confidence-gated fallback to soft retrieval, which transforms these potential weaknesses into measurable experimental variables that actually strengthen the core hypothesis.

ReCode demonstrates algorithm-type-aware retrieval in competitive programming but focuses narrowly on algorithmic tags like greedy and dynamic programming, while ReinFix moves toward root-cause conditioning—

achieving +32 and +38 bug fixes on different Defects4J versions—but uses a soft continuous approach with LLM-generated descriptions embedded in a unified vector space rather than hard type partitioning. InferFix is the earliest type-aware retrieval system for code repair, using contrastive learning to cluster semantically equivalent bugs and fixes based on static-analysis-derived bug types like null dereferences and resource leaks, reaching 76.8% top-1 accuracy on Java and 65.6% on C#.

Now comparing InferFix to FTCR more directly: InferFix applies type conditioning as a soft embedding feature during retrieval—queries still find the most similar match across type boundaries—whereas FTCR hard-partitions the corpus into separate type indices upfront so only same-type candidates compete. InferFix's types come from Infer's diagnostic categories rather than the 18-category natural-bug taxonomy I'm using, and its corpus consists of bugs detected by running Infer on repository histories instead of real bug-fix pairs from issue trackers. So InferFix validates that type-aware retrieval improves repair outcomes, supporting my hypothesis, though it leaves open the question of whether hard partitioning and natural-bug taxonomy categories would perform even better.

SWE-Exp takes a similar soft approach—it retrieves the top 10 most relevant issues using soft cosine similarity over embeddings that combine issue type and description—but stores distilled strategies rather than concrete patches and operates as a fully agentic pipeline for Python. The key structural difference with FTCR is that I'm partitioning the retrieval corpus into discrete type sub-indices before any query arrives, which gives me retrieval-pool precision rather than relying on post-hoc reranking. TypeRepair independently validates that defect type identification improves repair outcomes, further supporting the core hypothesis.

TypeRepair's 4-stage pipeline across 10 defect types achieves a 272% improvement over GPT-3.5 on standard benchmarks, and critically, it uses the identified type to select within-project context and generate type-specific repair guidance—but it retrieves no external cross-repository fix corpus. Since TypeRepair is Java-only, FTCR extends this type-conditioned approach to C++, Java, and Python while pulling from ~3,050 historical fix patches across repositories. This means TypeRepair validates that type conditioning matters but leaves the hard-vs-soft partitioned cross-repo retrieval question completely open, which is exactly where FTCR's contribution sits.

Gu et al. provide independent empirical support from a different angle: syntactically similar code snippets actually degrade repository-level code generation by up to 15%, while contextual code and API information help significantly. Their key insight—that what you retrieve matters more than how you retrieve it—directly supports FTCR's design: fix patches grouped by type partition share the same semantic repair operation (null-check insertion, bounds guard, API substitution), whereas patches retrieved by surface similarity might look alike but represent different fix operators, which is exactly the noise Gu et al. identified. DynaFix later surpasses ReinFix on the same benchmarks using execution-level dynamic information and iterative repair, showing that retrieval strategy and execution-level augmentation are independent improvement axes—and FTCR focuses specifically on the retrieval strategy side.

RetypeR takes a type-specific retrieval approach but only for Python type errors, a narrow subcategory. The core hypothesis I'm testing is whether hard categorical type partitioning—classifying the incoming failure into one of N discrete semantic types and retrieving only from that type's sub-corpus—yields better precision for transferable fix templates than InferFix's contrastive soft embedding or ReinFix's joint root-cause embedding. The reasoning is that bugs within a type share syntactic fix motifs that bugs with merely similar code or similar root-cause descriptions but different repair operators don't share. DebugBench is uniquely valuable here because it provides 4,253 instances with ground-truth 18-category type annotations across C++, Java, and Python, and these labels let me directly calibrate the few-shot type classifier, turning classifier error propagation from a hidden risk into a measurable experimental variable.

A confidence-gated hybrid approach that falls back to soft retrieval for low-confidence classifications mitigates the structural risk of hard partitioning, and this has principled precedent in CRAG for general RAG systems. M-RAG further validates that partition-based retrieval consistently outperforms single-store retrieval across NLP tasks, providing domain-general support for the partition hypothesis before I test it in code repair.

Now I'm noting that RELREPAIR retrieves relevant code from the same project using function names and comments, achieving a +17.1% improvement on Defects4J V1.2 and a 48.3% fix rate on ManySStuBs.

InferFix is the earliest type-aware cross-repository retrieval system for code repair, using contrastive learning to embed semantically equivalent bugs and their fixes close together, conditioned on Infer's type information — it's earlier than RepoRepair and represents a different approach than the retrieval-only methods I'm targeting.

InferFix achieves strong results on Java (76.8% top-1 accuracy) and C# (65.6%), outperforming earlier language models significantly. The key distinction between FTCR and InferFix is architectural: InferFix uses soft contrastive similarity where type is an embedding-time signal, while FTCR partitions the corpus into discrete type sub-indices upfront, restricting the retrieval pool to same-type pairs before similarity scoring.

Beyond the retrieval mechanism, FTCR differs in its defect taxonomy—using 18 empirically-grounded categories aligned with DebugBench rather than Infer's diagnostic IDs—and its corpus, drawing from natural bug-fix pairs in issue trackers and CI logs instead of static-analysis artifacts. The core scientific question is whether hard construction-time partitioning outperforms soft retrieval-time type conditioning for precision.

ReinFix is the closest baseline, using an LLM to generate free-text root-cause descriptions per bug before embedding them for retrieval. eds (buggy_code + root_cause_text) as a single concatenated string into a unified vector database using text-embedding-3-large, built from 100K samples of the TRANSFER corpus (1M bug-fix pairs). Retrieval is by cosine similarity over this joint embedding — no type-level partitioning, and root cause is a continuous semantic descriptor, not a discrete category. **Corpus quality confound: comparisons against published ReinFix results conflate two variables — retrieval architecture (soft joint embedding vs. hard type partition) and corpus quality (100K TRANSFER synthetic pairs vs. 3,050 natural bug-fix pairs). Intra-corpus ablations (FTCR vs. re-implemented ReinFix-style baseline on the same 3,050-pair natural corpus using the same text-embedding-3-large encoder) test the partitioning hypothesis cleanly; absolute performance comparisons against published ReinFix numbers simultaneously reflect both architecture and corpus quality differences.** SWE-Exp is the most relevant concurrent work, achieving 73.0% on SWE-bench Verified by retrieving the top 10 most relevant issues from an experience bank using soft cosine similarity over type-augmented embeddings with Multilingual-E5-Large. The key distinction between SWE-Exp and FTCR lies in how they handle type information: SWE-Exp applies soft cosine similarity with type as metadata at retrieval time, while FTCR partitions the index into discrete type sub-corpora upfront so only same-type pairs are candidates for any query.

SWE-Exp stores distilled problem perspectives and generalized strategies, whereas FTCR retrieves concrete historical patches for direct template transfer. SWE-Exp is fully agentic and Python-only, while FTCR is retrieval-only and covers C++, Java, and Python using DebugBench's oracle type labels for calibration. TypeRepair applies a 4-stage pipeline across 10 defect types on Defects4J and QuixBugs, achieving 272% improvement over GPT-3.5.

The core testable hypothesis is whether hard construction-time type partitioning outperforms soft retrieval-time filtering for precision in fix-template matching.

TypeRepair's context selection stage uses the identified defect type to pull relevant within-project code and provide type-specific repair guidance, but doesn't retrieve from an external cross-repository corpus. The evaluation is scoped to within-project Java datasets (Defects4J and QuixBugs) with no external retrieval component, making the architectural difference clear. FTCR, by contrast, covers multiple languages and retrieves from ~3,050 historical fix patches across repositories, while TypeRepair validates that defect type identification itself provides measurable benefits.

Recent work by Gu et al. shows that syntactically similar code snippets can actually hurt repository-level code generation performance, whereas semantic context and API information help more — this finding supports FTCR's strategy of retrieving fix patches partitioned by type (which share semantic repair structure) rather than relying on surface-level code similarity. DynaFix presents another relevant comparison point. ) outperforms ReinFix on Defects4J V2.0 using execution-level dynamic information and iterative repair (236 bugs fixed with GPT-4); DebugRepair (arXiv 2604.19305) achieves 295 Defects4J bugs with DeepSeek-V3 via self-directed debugging with runtime traces. Both update the Defects4J performance landscape but are orthogonal to FTCR's retrieval strategy focus — execution-level augmentation and retrieval strategy are independently improvable axes. D4C (ICSE 2025, arXiv 2404.08877) repairs 180 Defects4J bugs via LLM objective alignment. FTCR's structural departure from ReinFix is to (1) classify incoming failures into discrete categories, then (2) retrieve only from the type-matched sub-index, using the identical encoder (text-embedding-3-large) for a clean comparison that isolates partitioning as the primary architectural variable. This partitioning also reduces the effective retrieval pool to ~1/N_types of the full corpus, a corpus-size effect that a random-partition control ablation is designed to separate from type-matching precision. RetypeR (ICSME 2024, Hao et al.) applies two-stage external+internal retrieval conditioned on Python type errors, establishing that type-specific retrieval helps for one narrow bug class and language; FTCR extends this principle across 18 categories and three languages. M-RAG (ACL 2024, arXiv 2405.16420) demonstrates that multi-partition RAG consistently outperforms single-store RAG across NLP tasks, validating the general effectiveness of partitioned retrieval.

PatchRecall (arXiv 2604.10481) introduces history-based retrieval for file-level localization on SWE-bench — complementary to FTCR's cross-repository fix template retrieval. The APR survey (arXiv 2506.23749) reviews 63+ systems and identifies retrieval augmentation as the key enhancement, but no reviewed system applies hard taxonomic type classification as the retrieval partition key across multiple languages. I need to frame this work with an NLP lead perspective, clarify the corpus confound through the random-partition ablation, establish the TypeRepair evidentiary basis, and note the execution timeline — this is auto-research mode only with a day-by-day plan. EMNLP 2026 is the primary target venue with ARR submission May 25. day-by-day plan, ICSE 2027 backup.

---

Let me now write the full JSON. I'll be comprehensive.

Actually for the approach section, I need to preserve most of the existing approach content (which is solid) and add:
1. NLP lead framing as a new subsection at the top
2. Execution timeline
3. Corpus confound explicit flagging (add to "Retrieval Corpus Construction" section or a separate note)
4. TypeRepair evidentiary basis

Let me write the full approach section:

**NLP Lead Framing (EMNLP Contribution)**. The primary scientific contribution targeted at EMNLP 2026 is an empirical characterization of LLM-generated bug type label quality and its downstream retrieval impact, yielding four falsifiable quantities: (X%) few-shot LLM classifier accuracy against DebugBench ground-truth oracle labels (851 held-out instances, 20% split); (Y%) zero-shot cross-lingual transfer accuracy of the same classifier to Java bugs (human-verified sample of ~56 Defects4J/GitBug-Java pairs); (Z%) repair improvement on DebugBench and Defects4J V1.2 for correctly-classified high-confidence instances under hard type-partitioned retrieval vs. soft joint-embedding baseline; (W%) repair degradation for misclassified instances under hard partitioning vs. same baseline.

These four metrics together form a complete causal story: hard type partitioning works when the classifier is accurate and fails when it isn't, with the confidence threshold acting as a safety valve that routes uncertain cases back to soft retrieval. This is a testable hypothesis about LLM label quality and retrieval design that extends beyond code repair to any system relying on LLM-inferred categorical labels.

**Execution Plan for EMNLP 2026 ARR (May 25 deadline)**. Auto-research mode is the only feasible path given the 10–14 day window versus the 16-day hard budget. I'm laying out a day-by-day schedule with minimum viable submission checkpoints, starting with launching the auto-research pipeline and beginning the three-pass annotation of the 3,050 corpus pairs using DebugBench few-shot setup on Day 0.

Days 1–3 focus on completing the annotation (budgeted at ~$183 in Claude API costs), calibrating the DebugBench classifier on 851 held-out instances to measure per-type accuracy, and running the cross-lingual Java transfer test on a human-verified sample of 56 pairs to establish Y%. Days 4–6 involve building the type-partitioned sub-indices and a unified ReinFix-style index using text-embedding-3-large, then running Defects4J V1.2 ablations comparing text-similarity retrieval against the ReinFix re-implementation on the full 3,050-pair natural corpus.

Days 7–9 evaluate DebugBench across all variants with confidence-gated τ sweeps on the validation split, stratifying results by classifier confidence to separate correctly-typed high-confidence cases from misclassified ones, while launching SWE-bench Lite evaluation in parallel (10 minutes per instance on 2 A100 nodes). Days 10–12 run the CodeBERT-base encoder ablation, testing different taxonomy granularities (6-type coarse, 18-type fine, merged-Java) and sweeping retrieval k values, with SWE-bench Lite results compiled if the pipeline finishes. Day 13 wraps up with results compilation and the start of paper writing with the NLP lead.

Days 14–15 finalize the paper and submit to ARR, with the EMNLP minimum viable submission consisting of DebugBench calibration results plus Defects4J V1.2 ablations and the random-partition control, optionally including SWE-bench Lite if complete or deferring it to the ICSE 2027 version. The submission is feasible but the two-day writing window is extremely tight, requiring a pre-drafted paper skeleton during the experiment phase.

Now I'm ready to construct the full JSON structure, and I need to think through how to categorize the changes—the main ones being venue restructuring and resource adjustments.

Writing the JSON structure...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7c70c28-5e5c-46f8-8420-b2ee48924835",
  "isSidechain": false,
  "requestId": "req_011CatRepVHyN9BV5XkW7ubz",
  "type": "assistant",
  "uuid": "220e72fc-2ac8-4956-bc55-1a35f819a727",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AbT8VUbSMWHCV27WCb3xCZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3384,
      "cache_read_input_tokens": 32335,
      "output_tokens": 19587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3384,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 19587,
          "cache_read_input_tokens": 32335,
          "cache_creation_input_tokens": 3384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3384
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

_source line 19 · 2026-05-10T06:43:38.445Z_

I have the key information I need. Let me now write the complete revised proposal addressing all five reviewer issues.

Key findings from research:
- **InferFix** uses Infer's static-analysis bug type annotations + contrastive-learned *soft* embeddings (NOT hard partitioning); corpus is InferredBugs (Java/C#, static-analysis-detected bugs); 76.8% Java top-1 accuracy
- **EMNLP 2026 ARR deadline confirmed: May 25, 2026** — 15 days from today, achievable with auto-research (10-14 days) + 2 days writing
- The NLP framing (X%/Y%/Z%/W% classifier calibration) is the right lead for EMNLP

This is a **major revision**: restoring EMNLP 2026 with a day-by-day execution plan, restructuring to NLP-lead framing, adding InferFix, stripping resource_estimate to auto-research only, and flagging the corpus confound explicitly.

```json
{
  "title": "Failure-Type-Conditioned Retrieval Augmentation for Repository Repair",
  "change_type": "major",
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
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "220e72fc-2ac8-4956-bc55-1a35f819a727",
  "isSidechain": false,
  "requestId": "req_011CatRepVHyN9BV5XkW7ubz",
  "type": "assistant",
  "uuid": "16535921-a0a6-40ae-9008-18d6c0348845",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01AbT8VUbSMWHCV27WCb3xCZ",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 3384,
      "cache_read_input_tokens": 32335,
      "output_tokens": 19587,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3384,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 19587,
          "cache_read_input_tokens": 32335,
          "cache_creation_input_tokens": 3384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3384
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "16535921-a0a6-40ae-9008-18d6c0348845",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Program Repair by EMNLP 2026",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"Failure-Type-Conditioned Retrieval Augmentation for Repository Repair\"…",
  "leafUuid": "16535921-a0a6-40ae-9008-18d6c0348845",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---

### Runtime record

_source line 23_

```json
{
  "type": "ai-title",
  "aiTitle": "Failure-Type-Conditioned Retrieval for Program Repair by EMNLP 2026",
  "sessionId": "a9d6493b-2b10-47f3-a4b7-6416b94b4ede"
}
```

---
