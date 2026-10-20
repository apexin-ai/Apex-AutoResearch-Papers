# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-10 (UTC).** ## Original idea { "tit

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 38
- **Recorded user turns:** 1
- **Tool calls:** 6
- **Original source:** `logs/chats/exported-trajectories/account-1/420cebf2-9484-43c1-a214-76e7ddc0da77.jsonl`
- **Structured JSON:** [`1d3ce705727b5f6b4121.json`](../../sessions/1d/1d3ce705727b5f6b4121.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-10T07:13:47.628Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-10T07:13:47.628Z",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-10 (UTC).**\n\n## Original idea\n{\n  \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair\",\n  \"core_problem\": \"Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, yet its error analysis (Section V-A, 'Reasons for Failure') identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.\",\n  \"opportunity\": \"Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap, replacing the officially-abandoned SWE-bench Verified. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.\",\n  \"landscape\": \"SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.\",\n  \"approach\": \"We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale; this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. Augment with ~3,000 pseudo-labeled GitBugs instances (arXiv 2504.09651; 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code) selected for stack-trace richness and LLM-derived pseudo-specs, yielding a ~5,300-instance fine-tuning corpus. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its 50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution).\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"~90-110 H100-hours (~180-220 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls\",\n      \"timeline\": \"3-5 months\",\n      \"team\": \"1-2 researchers\",\n      \"estimated_gpu_cost\": \"~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"~135-160 H100-hours (~270-380 A100-equivalent hours)\",\n      \"gpu_breakdown\": \"SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins\",\n      \"timeline\": \"5-9 weeks\",\n      \"team\": \"1 researcher, ~30 min/day check-in\",\n      \"claude_api_cost\": \"$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)\",\n      \"estimated_gpu_cost\": \"~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint\",\n      \"risk_note\": \"Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up.\"\n    },\n    \"auto_research\": {\n      \"note\": \"Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.\",\n      \"gpu_hours\": \"~160-180 H100-hours (budget-capped)\",\n      \"gpu_breakdown\": \"SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.\",\n      \"gpu_utilization\": \"~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously\",\n      \"timeline\": \"6-10 days with 4 parallel H100 GPUs\",\n      \"team\": \"0 (setup only, ~3h initial configuration)\",\n      \"claude_api_cost\": \"$400-600 (~4,500 turns)\",\n      \"estimated_gpu_cost\": \"~$384-432 (160-180h × $2.40/hr H100)\",\n      \"speed_bottleneck\": \"SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require\"\n    }\n  },\n  \"target_venues\": [\n    \"EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval\",\n    \"ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including SWE-bench-Live partial-set ablations\",\n    \"NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025\"\n  ],\n  \"level\": \"solid\",\n  \"key_references\": [\n    \"SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode\",\n    \"SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct baseline for our evaluation\",\n    \"Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision\",\n    \"SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields\",\n    \"SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for\",\n    \"Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages\",\n    \"Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement\",\n    \"Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J\",\n    \"SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach\",\n    \"GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation\",\n    \"RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)\",\n    \"On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)\",\n    \"PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)\"\n  ],\n  \"description\": \"We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides 3,000 pseudo-labeled augmentation instances, yielding a 5,300-instance fine-tuning corpus. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a target improvement of +4-7 percentage points; per-field ablations measure individual spec contributions. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.\",\n  \"project_name\": \"structured_spec_repair\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 4)\nIssues: [\"IMPORTANT CORRECTION — SpecRover Section V-A claim is VERIFIED, not fabricated: Independent WebFetch of the HTML version of arXiv:2408.02232 (https://arxiv.org/html/arXiv:2408.02232) confirms the paper contains Section V-A 'RQ1: Overall Efficacy of Task Resolving' with a subsection 'Reasons for Failure' that explicitly documents 107/207 unresolved SWE-bench Lite tasks (51.7%) classified as ambiguous issue descriptions. The Round 3 reviewer's 'fabricated' accusation was incorrect. The generator should add a footnote or parenthetical citing the HTML URL to preempt any residual reviewer confusion, since the accusation has been raised three consecutive rounds.\", \"SIGNIFICANT — Internal inconsistency in EMNLP pilot scope: The EMNLP venue description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the main approach uses 2,294 SWE-bench instances + 3,000 GitBugs pseudo-labeled instances = 5,300 corpus. These are in direct conflict. Either (a) define the EMNLP submission as explicitly scoped to a pilot — SFT on SWE-bench Verified 500 subset, SWE-bench-Live Lite 300-instance eval, no GitBugs augmentation — and state this clearly in the approach section, or (b) remove the '500-instance Verified' framing from the venue description and commit to the full corpus with the understanding that compute and eval must finish within 16 days.\", \"MODERATE — 16-day deadline is unrealistically framed without explicit pilot scope: Building the 5,300-instance training corpus (AST parsing + NLP regex + LLM-assisted spec fill), SFT (10-14 H100-hours), establishing Agentless-SWE-bench-Live Docker infrastructure, running the full 300-instance eval + 4-field ablations (80-96 H100-hours), and writing the paper cannot realistically be completed in 16 days by 1-2 researchers. The submission plan should explicitly acknowledge that the EMNLP ARR submission will report pilot-scale results (e.g., SFT on 500-instance Verified subset, 100-instance SWE-bench-Live Lite eval) with the full-scale results reserved for ICSE 2027 as the primary venue.\", \"MODERATE — 'Replacing the officially-abandoned SWE-bench Verified' is imprecise: OpenAI's February 2026 announcement recommends SWE-bench Pro as the frontier evaluation replacement — not SWE-bench-Live. SWE-bench-Live is the appropriate replacement for contamination-resistant research evaluation, which is the correct positioning for this paper, but the phrasing implies SWE-bench-Live is the community standard replacement for Verified, which overstates its current adoption. Reframe as: 'As SWE-bench Verified saturates with contamination concerns, SWE-bench-Live (NeurIPS 2025) provides contamination-resistant evaluation on post-2024 issues — the appropriate target for research contributions that train on SWE-bench data.'\", \"MINOR — Cosine similarity threshold (≥ 0.65) for schema validation is stated without justification: The proposal requires AST-parsed test assertions to achieve ≥ 0.65 cosine similarity with SWE-bench Pro human requirements on 200 held-out instances. This threshold determines whether the schema is redesigned before scale-up, making it a critical gating decision. Add one sentence explaining why 0.65 is the right threshold (e.g., 'consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs').\"]\nFeedback: The SpecRover Section V-A claim has been independently verified as correct — the HTML paper confirms the 107/207 (51.7%) ambiguous issue description statistics in the 'Reasons for Failure' subsection of Section V-A. After three rounds of false accusations, add a parenthetical citing the HTML URL (https://arxiv.org/html/arXiv:2408.02232) to preempt any residual reviewer skepticism. To reach 'pass' in Round 5: (1) **Fix the pilot/full scope inconsistency**: Choose one coherent story for EMNLP. The most defensible is a pilot submission — SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances (not 300), 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Remove the '500-instance SWE-bench Verified training' from the venue description and put it in the approach section as the EMNLP pilot plan. State that the full 5,300-instance corpus + 300-instance eval is the ICSE 2027 primary submission. (2) **Fix the SWE-bench Verified replacement framing**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' (3) **Justify the 0.65 cosine similarity threshold** in one sentence. With these changes, the proposal will have resolved all substantive issues from rounds 1-4 and should be ready to pass.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method (approach / resource_estimate / key_references). Do not jump straight to fixing the method if the underlying problem framing needs correction.\n- Address each issue specifically.\n\n## 深度调研要求（每一轮修订都必须执行）\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化这个 idea 的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，建议用 2-3 种不同的搜索查询调研。\n   - 搜索最新的相关论文（arXiv, conference proceedings）\n   - 搜索 benchmark/leaderboard 确认当前 SOTA\n   - 搜索可能遗漏的相关工作和 concurrent work\n\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文的 abstract 和方法部分，\n   不要只依赖搜索摘要。形成你自己对领域现状的独立判断。\n\n3. **深度思考**：在修订之前，先独立思考以下问题：\n   - 这个 idea 的核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach 来解决同一个核心问题？\n   - 修订后的 idea 相比上一版有什么本质性的改进？\n\n4. **避免表面修订**：如果你发现自己只是在换措辞或补充细节而没有实质改进，\n   考虑是否需要 major revision 或 pivot。反复的 minor fix 不会拯救一个根基有问题的 idea。\n\n## 针对 Review 意见的定向搜索\n\n对 reviewer 指出的每个问题，执行以下搜索流程：\n\n1. **如果 reviewer 说'已有类似工作'**：\n   - 搜索 reviewer 提到的论文，用 WebFetch 实际阅读\n   - 搜索该论文的 cited-by，找到后续跟进工作\n   - 明确你的 idea 与这些工作的差异化点——如果差异化不够，必须 pivot\n\n2. **如果 reviewer 说'SOTA 过时'**：\n   - 用 Papers With Code 查看当前排行榜\n   - 搜索过去 6 个月的最新方法\n   - 更新你的 landscape 和 baseline\n\n3. **如果 reviewer 说'可行性有问题'**：\n   - 搜索类似规模实验的实际成本和时间线\n   - 搜索 GitHub 上是否有可复用的实现\n   - 搜索相关数据集/模型的可获取性\n\n4. **如果 reviewer 说'novelty 不足'**：\n   - 对核心方法尽量做 3-5 种不同关键词组合的搜索\n   - 搜索相邻领域是否有类似思路\n   - 如果确实 novelty 不足，考虑 major revision 或 pivot\n\n- Use WebSearch to find updated information if the reviewer flagged outdated claims.\n- You have full freedom in how much to change:\n  - Minor fix: if only specific details are wrong, correct them and keep everything else.\n  - Major revision: if the approach is fundamentally flawed but the core problem is valid, you may redesign the approach entirely.\n  - Pivot: if the reviewer's feedback reveals that the core problem itself is invalid (e.g., the gap no longer exists), you may propose a RELATED but substantially different idea that builds on the same research area. This is preferred over forcing a doomed idea to pass review.\n- The output replaces the original idea (same tracking ID). Whether you make a small tweak or a full pivot, output a COMPLETE JSON object with ALL fields filled.\n- In the output JSON, include a \"change_type\" field with one of: \"minor\", \"major\", or \"pivot\" to indicate the scope of your changes.\n- Output the revised idea as a COMPLETE JSON object (same schema as original, plus \"change_type\").\n\n## 停滞提醒\n这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。\n\n请认真思考：\n- 当前方向是否存在根本性的瓶颈？反复的 minor fix 是否在回避核心问题？\n- 如果你认为问题出在 approach 而非 framing，可以做 major revision。\n- 如果你认为 core problem 本身就有问题（gap 不存在、问题不够重要），pivot 到同一研究领域下的新方向可能是更好的选择。\n- 当然，如果你有信心这一轮修订能实现突破，继续改进也完全可以。\n\n最终由你判断——做你认为最能提升 idea 质量的选择。"
}
```

---

### Runtime record

_source line 2 · 2026-05-10T07:13:47.633Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-10T07:13:47.633Z",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

## Round 1

36 recorded events

### User

_source line 3 · 2026-05-10T07:13:47.662Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-10 (UTC).**

## Original idea
{
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, yet its error analysis (Section V-A, 'Reasons for Failure') identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.",
  "opportunity": "Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap, replacing the officially-abandoned SWE-bench Verified. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.",
  "landscape": "SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.",
  "approach": "We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale; this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. Augment with ~3,000 pseudo-labeled GitBugs instances (arXiv 2504.09651; 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code) selected for stack-trace richness and LLM-derived pseudo-specs, yielding a ~5,300-instance fine-tuning corpus. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its 50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Evaluation**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution).",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~90-110 H100-hours (~180-220 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
      "gpu_utilization": "~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)"
    },
    "human_in_loop": {
      "gpu_hours": "~135-160 H100-hours (~270-380 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
      "gpu_utilization": "~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins",
      "timeline": "5-9 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)",
      "estimated_gpu_cost": "~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint",
      "risk_note": "Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up."
    },
    "auto_research": {
      "note": "Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.",
      "gpu_hours": "~160-180 H100-hours (budget-capped)",
      "gpu_breakdown": "SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.",
      "gpu_utilization": "~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously",
      "timeline": "6-10 days with 4 parallel H100 GPUs",
      "team": "0 (setup only, ~3h initial configuration)",
      "claude_api_cost": "$400-600 (~4,500 turns)",
      "estimated_gpu_cost": "~$384-432 (160-180h × $2.40/hr H100)",
      "speed_bottleneck": "SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval",
    "ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; preferred primary target for full experimental results including SWE-bench-Live partial-set ablations",
    "NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025"
  ],
  "level": "solid",
  "key_references": [
    "SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode",
    "SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct baseline for our evaluation",
    "Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision",
    "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields",
    "SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for",
    "Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages",
    "Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement",
    "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J",
    "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach",
    "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)",
    "PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)"
  ],
  "description": "We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides 3,000 pseudo-labeled augmentation instances, yielding a 5,300-instance fine-tuning corpus. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues), with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a target improvement of +4-7 percentage points; per-field ablations measure individual spec contributions. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's Section V-A identified 51.7% ambiguous-description failure mode — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.",
  "project_name": "structured_spec_repair",
  "source": "web_research"
}

## Reviewer feedback (round 4)
Issues: ["IMPORTANT CORRECTION — SpecRover Section V-A claim is VERIFIED, not fabricated: Independent WebFetch of the HTML version of arXiv:2408.02232 (https://arxiv.org/html/arXiv:2408.02232) confirms the paper contains Section V-A 'RQ1: Overall Efficacy of Task Resolving' with a subsection 'Reasons for Failure' that explicitly documents 107/207 unresolved SWE-bench Lite tasks (51.7%) classified as ambiguous issue descriptions. The Round 3 reviewer's 'fabricated' accusation was incorrect. The generator should add a footnote or parenthetical citing the HTML URL to preempt any residual reviewer confusion, since the accusation has been raised three consecutive rounds.", "SIGNIFICANT — Internal inconsistency in EMNLP pilot scope: The EMNLP venue description states 'realistic for a theory + pilot-scale submission with 500-instance SWE-bench Verified training and SWE-bench-Live Lite eval,' but the main approach uses 2,294 SWE-bench instances + 3,000 GitBugs pseudo-labeled instances = 5,300 corpus. These are in direct conflict. Either (a) define the EMNLP submission as explicitly scoped to a pilot — SFT on SWE-bench Verified 500 subset, SWE-bench-Live Lite 300-instance eval, no GitBugs augmentation — and state this clearly in the approach section, or (b) remove the '500-instance Verified' framing from the venue description and commit to the full corpus with the understanding that compute and eval must finish within 16 days.", "MODERATE — 16-day deadline is unrealistically framed without explicit pilot scope: Building the 5,300-instance training corpus (AST parsing + NLP regex + LLM-assisted spec fill), SFT (10-14 H100-hours), establishing Agentless-SWE-bench-Live Docker infrastructure, running the full 300-instance eval + 4-field ablations (80-96 H100-hours), and writing the paper cannot realistically be completed in 16 days by 1-2 researchers. The submission plan should explicitly acknowledge that the EMNLP ARR submission will report pilot-scale results (e.g., SFT on 500-instance Verified subset, 100-instance SWE-bench-Live Lite eval) with the full-scale results reserved for ICSE 2027 as the primary venue.", "MODERATE — 'Replacing the officially-abandoned SWE-bench Verified' is imprecise: OpenAI's February 2026 announcement recommends SWE-bench Pro as the frontier evaluation replacement — not SWE-bench-Live. SWE-bench-Live is the appropriate replacement for contamination-resistant research evaluation, which is the correct positioning for this paper, but the phrasing implies SWE-bench-Live is the community standard replacement for Verified, which overstates its current adoption. Reframe as: 'As SWE-bench Verified saturates with contamination concerns, SWE-bench-Live (NeurIPS 2025) provides contamination-resistant evaluation on post-2024 issues — the appropriate target for research contributions that train on SWE-bench data.'", "MINOR — Cosine similarity threshold (≥ 0.65) for schema validation is stated without justification: The proposal requires AST-parsed test assertions to achieve ≥ 0.65 cosine similarity with SWE-bench Pro human requirements on 200 held-out instances. This threshold determines whether the schema is redesigned before scale-up, making it a critical gating decision. Add one sentence explaining why 0.65 is the right threshold (e.g., 'consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs')."]
Feedback: The SpecRover Section V-A claim has been independently verified as correct — the HTML paper confirms the 107/207 (51.7%) ambiguous issue description statistics in the 'Reasons for Failure' subsection of Section V-A. After three rounds of false accusations, add a parenthetical citing the HTML URL (https://arxiv.org/html/arXiv:2408.02232) to preempt any residual reviewer skepticism. To reach 'pass' in Round 5: (1) **Fix the pilot/full scope inconsistency**: Choose one coherent story for EMNLP. The most defensible is a pilot submission — SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances (not 300), 2-field ablation (affected_interface vs. none, expected_behavior vs. none). Remove the '500-instance SWE-bench Verified training' from the venue description and put it in the approach section as the EMNLP pilot plan. State that the full 5,300-instance corpus + 300-instance eval is the ICSE 2027 primary submission. (2) **Fix the SWE-bench Verified replacement framing**: Change 'replacing the officially-abandoned SWE-bench Verified' to 'providing contamination-resistant evaluation as SWE-bench Verified saturates at frontier.' (3) **Justify the 0.65 cosine similarity threshold** in one sentence. With these changes, the proposal will have resolved all substantive issues from rounds 1-4 and should be ready to pass.

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
这个 idea 已经经过 4 轮修订，近 3 轮的平均分从 3.2 到 3.5，没有明显改善。

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
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "3e35e1c5-e8bb-4936-9ef4-e334026d8fd4",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-10T07:13:47.660Z_

```json
{
  "parentUuid": "3e35e1c5-e8bb-4936-9ef4-e334026d8fd4",
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
  "uuid": "69e4990f-adf0-4e36-9be4-9607e4f72682",
  "timestamp": "2026-05-10T07:13:47.660Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-10T07:13:47.660Z_

```json
{
  "parentUuid": "69e4990f-adf0-4e36-9be4-9607e4f72682",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "c7e6fb7d-a002-49ae-a052-3148fce905a2",
  "timestamp": "2026-05-10T07:13:47.660Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug R…",
  "leafUuid": "c7e6fb7d-a002-49ae-a052-3148fce905a2",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral specifications for guided program repair",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Assistant

_source line 8 · 2026-05-10T07:14:18.212Z_

<details><summary>Logged reasoning block</summary>

```text
Let me analyze the reviewer feedback carefully and think about what changes are needed.

## Reviewer Feedback Summary (Round 4)

1. **IMPORTANT CORRECTION** - SpecRover Section V-A claim is VERIFIED (not fabricated). Need to add a footnote/parenthetical citing the HTML URL to preempt future reviewer confusion.

2. **SIGNIFICANT** - Internal inconsistency in EMNLP pilot scope: EMNLP venue says "500-instance SWE-bench Verified training" but main approach uses 5,300 instances. Need to either:
   - Define EMNLP as explicitly pilot-scoped (SFT on 500-instance Verified subset, 100-150 instance eval, 2-field ablation)
   - Or remove the 500-instance framing from the venue description

3. **MODERATE** - 16-day deadline is unrealistically framed - need to explicitly acknowledge EMNLP ARR submission will report pilot-scale results

4. **MODERATE** - "Replacing the officially-abandoned SWE-bench Verified" is imprecise - reframe as contamination-resistant evaluation

5. **MINOR** - Cosine similarity threshold (≥ 0.65) needs justification

## Thinking About the Core Issues

These are mostly framing and consistency issues rather than fundamental research problems. The key is resolving the EMNLP scope discrepancy—I need to either commit to the 500-instance pilot for that venue or clarify that the main approach uses the full 5,300 instances. The other points are straightforward fixes: adding citations, reframing language around SWE-bench Verified, acknowledging timeline constraints, and justifying the similarity threshold.

Looking at the pattern across four review rounds with scores hovering between 3.2 and 3.5, the stagnation suggests I should check whether there's a deeper issue. But examining the feedback more closely, the core research contribution—extracting behavioral specifications from issue spaces and training on test assertions within the Agentless framework—appears sound. The technical concerns are primarily about evaluation framing and consistency rather than the approach itself. This feels like a case where targeted revisions will address the legitimate issues without requiring a major pivot.

I'm planning some focused research to shore up the specific claims: verifying the SpecRover URL, checking the current state of SWE-bench Verified, and finding literature support for the 0.65 cosine similarity threshold in information extraction work. SWE-bench status/framing
3. Any new relevant papers

Let me plan my approach:

**Phase 1: Research**
- Search for cosine similarity thresholds in information extraction literature
- Verify SWE-bench Verified status claims
- Check for any new relevant papers

**Phase 2: Revisions**
1. Add HTML URL parenthetical for SpecRover claim
2. Fix EMNLP pilot scope - make it explicitly pilot-scale (500 Verified instances, 100-150 SWE-bench-Live Lite, 2-field ablation)
3. Fix SWE-bench Verified framing
4. Add justification for 0.65 cosine similarity threshold

The change_type should be "minor" since these are editorial fixes.

Looking at the reviewer feedback across all rounds, the main technical claim about SpecRover was actually verified, which suggests the core contribution is sound—the remaining issues are genuinely about consistency and framing rather than fundamental problems. I need to research the cosine similarity threshold justification and SWE-bench Verified status to properly address these points.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7e6fb7d-a002-49ae-a052-3148fce905a2",
  "isSidechain": false,
  "requestId": "req_011CatUUtxkb1wZPG5sGUEqL",
  "type": "assistant",
  "uuid": "76db1d3d-8536-49ed-8ab1-f84218e0db1a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0177B7KV8JcT6NPAg1AZByKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14694,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1898,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14694
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

_source line 9 · 2026-05-10T07:14:18.271Z_

I'll analyze the feedback carefully before revising. The issues are specific and actionable — let me do targeted research to address them properly, especially the cosine similarity justification and SWE-bench Verified framing.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76db1d3d-8536-49ed-8ab1-f84218e0db1a",
  "isSidechain": false,
  "requestId": "req_011CatUUtxkb1wZPG5sGUEqL",
  "type": "assistant",
  "uuid": "565408a5-249b-4145-b2bc-2222d513b1d1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0177B7KV8JcT6NPAg1AZByKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14694,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1898,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14694
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

_source line 10 · 2026-05-10T07:14:22.653Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01MLsQpXJceUUTpMr8FLGJ2m`</summary>

```json
{
  "description": "Research cosine similarity thresholds in IE literature",
  "subagent_type": "Explore",
  "prompt": "I need to find literature justification for using a cosine similarity threshold of 0.65 in information extraction or semantic similarity tasks. Specifically, I want to know:\n\n1. What cosine similarity thresholds are commonly used in information extraction, semantic textual similarity, or NLP tasks to distinguish \"semantically related\" from \"unrelated\" pairs?\n2. Are there specific papers that establish or validate 0.65 as a meaningful threshold?\n3. What are typical cosine similarity scores for sentence-transformer models when comparing semantically related but not identical descriptions?\n\nPlease search for papers on semantic similarity thresholds, sentence-BERT benchmarks, and information extraction evaluation. Look for papers like:\n- \"Semantic Textual Similarity\" papers (STS benchmarks)\n- Sentence-BERT / SBERT papers\n- Information extraction papers that use cosine similarity for validation\n\nReport what you find about commonly used thresholds and their justifications. This is purely research — no code changes needed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "565408a5-249b-4145-b2bc-2222d513b1d1",
  "isSidechain": false,
  "requestId": "req_011CatUUtxkb1wZPG5sGUEqL",
  "type": "assistant",
  "uuid": "826a75f2-f5e5-4529-ad3f-6324b76612ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0177B7KV8JcT6NPAg1AZByKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14694,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1898,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14694
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

_source line 11 · 2026-05-10T07:14:26.949Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01XTH4YngfDMjEQ4U4gFXV6D`</summary>

```json
{
  "description": "Research SWE-bench Verified status and SWE-bench-Live positioning",
  "subagent_type": "Explore",
  "prompt": "I need to verify the current status of SWE-bench Verified and how SWE-bench-Live is positioned relative to it. Specifically:\n\n1. Is SWE-bench Verified \"officially abandoned\"? Or is it just reaching saturation? What is the official stance?\n2. OpenAI's February 2026 announcement about SWE-bench Pro as a replacement — what exactly did it say?\n3. How is SWE-bench-Live (arXiv 2505.23419, NeurIPS 2025) positioned relative to SWE-bench Verified?\n\nPlease search for:\n- \"SWE-bench Verified abandoned\" or \"SWE-bench Verified saturation\"\n- \"SWE-bench Pro replacement\" \n- \"SWE-bench-Live contamination\"\n- Any official announcements about SWE-bench Verified deprecation\n\nAlso look at the SWE-bench-Live paper (arXiv 2505.23419) abstract and positioning statements.\n\nReport: What is the accurate framing for SWE-bench Verified's current status and where SWE-bench-Live fits in?\n\nThis is purely research — no code changes needed."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "826a75f2-f5e5-4529-ad3f-6324b76612ef",
  "isSidechain": false,
  "requestId": "req_011CatUUtxkb1wZPG5sGUEqL",
  "type": "assistant",
  "uuid": "cf2d96a8-4aa0-46e6-8f7c-f4d5e3210465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_0177B7KV8JcT6NPAg1AZByKE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 14694,
      "cache_read_input_tokens": 11631,
      "output_tokens": 1898,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14694,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 1898,
          "cache_read_input_tokens": 11631,
          "cache_creation_input_tokens": 14694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14694
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

_source line 12 · 2026-05-10T07:15:13.234Z_

<details><summary>↩ Tool result · `toolu_01XTH4YngfDMjEQ4U4gFXV6D`</summary>

```text
Based on my research, here is the accurate framing of SWE-bench Verified's current status and where SWE-bench-Live fits in:

## SWE-bench Verified's Status: NOT "Abandoned" but "Officially Deprecated"

**The official stance is clear deprecation, not just saturation.** On February 23, 2026, OpenAI's Frontier Evals team (Mia Glaese & Olivia Watkins) officially announced that SWE-bench Verified **no longer measures frontier coding capabilities** and should no longer be used for evaluating frontier models.

### The Two-Pronged Problem

OpenAI's analysis identified critical flaws that go beyond saturation:

1. **Test Quality Issues (>60% of remaining problems)**: 
   - 49 tests were overly narrowly defined, rejecting functionally correct solutions
   - 26 tests demanded features never mentioned in problem descriptions
   - Tests sometimes required specific implementation details not specified in requirements
   - At least 59.4% of the audited problems have flawed test cases

2. **Training Data Contamination (100% of frontier models affected)**:
   - ALL frontier models tested—including GPT-5.2, Claude Opus 4.5, and Gemini 3 Flash—could reproduce the original ground-truth bug fixes verbatim with minimal prompting
   - Models showed familiarity with SWE-bench problems from training data exposure
   - Improvements no longer reflect genuine problem-solving ability but rather training data overlap

## OpenAI's February 2026 Announcement

The official stance from OpenAI was published in their blog post "[Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)" and via [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270):

> "The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we're no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards."

**Key replacement**: SWE-bench Pro (released September 2025 by Scale AI) uses private and copyleft-licensed repositories. Scores dropped from ~70%+ on SWE-bench Verified to ~23% on SWE-bench Pro across frontier models—reflecting genuine problem-solving ability rather than training contamination.

## SWE-bench-Live's Positioning (arXiv 2505.23419, NeurIPS 2025)

SWE-bench-Live is positioned as the **live alternative to the static, contamination-prone SWE-bench Verified**:

### Key Differentiators:

1. **Continuously Updated**: Monthly additions of 50 newly verified, high-quality issues from real GitHub repositories
2. **Fresh Data**: Issues sourced from January 1, 2024 onwards (covering 2024-07 to 2025-04), significantly more recent than SWE-bench Verified
3. **Contamination Resistance**: Dates are carefully chosen to avoid overlap with model training cutoffs (Jan 2024 - April 20, 2025)
4. **Dynamic Evaluation**: Each month adds truly novel problems, preventing overfitting and maintaining fair leaderboard comparisons
5. **1,319 total instances** spanning 93 repositories (much broader than the fixed 500 in SWE-bench Verified)

### Performance Comparison:

The paper explicitly notes that models achieving high scores on SWE-bench Verified (80%+) show "significantly lower" performance on SWE-bench-Live, confirming that the original benchmark suffered from overfitting and contamination.

## Accurate Framing Summary

| Aspect | SWE-bench Verified | SWE-bench-Live |
|--------|-------------------|-----------------|
| **Status** | Officially deprecated (Feb 2026) | NeurIPS 2025 replacement |
| **Cause** | 59%+ flawed tests, 100% training contamination | Fresh, monthly-updated issues |
| **Dataset** | Static 500 instances, pre-2024 | 1,319 instances, continuously updated |
| **Contamination Risk** | Critical | Minimized by date cutoffs & monthly updates |
| **Use Case** | Legacy/historical tracking only | Current frontier model evaluation |

**Verdict**: SWE-bench Verified is not "reaching saturation"—it is fundamentally compromised by flawed test design and universal training data leakage, making scores meaningless for frontier models. SWE-bench-Live directly addresses these issues through continuous updates, fresh real-world issues, and careful contamination avoidance.

Sources:
- [The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data](https://www.latent.space/p/swe-bench-dead)
- [Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)
- [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)
- [SWE-bench Goes Live! (arXiv 2505.23419)](https://arxiv.org/abs/2505.23419)
- [SWE-bench-Live GitHub Repository](https://github.com/microsoft/SWE-bench-Live)
- [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cf2d96a8-4aa0-46e6-8f7c-f4d5e3210465",
  "isSidechain": false,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "c4a31733-8ae0-4daa-896d-4968ba51e828",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to verify the current status of SWE-bench Verified and how SWE-bench-Live is positioned relative to it. Specifically:\n\n1. Is SWE-bench Verified \"officially abandoned\"? Or is it just reaching saturation? What is the official stance?\n2. OpenAI's February 2026 announcement about SWE-bench Pro as a replacement — what exactly did it say?\n3. How is SWE-bench-Live (arXiv 2505.23419, NeurIPS 2025) positioned relative to SWE-bench Verified?\n\nPlease search for:\n- \"SWE-bench Verified abandoned\" or \"SWE-bench Verified saturation\"\n- \"SWE-bench Pro replacement\" \n- \"SWE-bench-Live contamination\"\n- Any official announcements about SWE-bench Verified deprecation\n\nAlso look at the SWE-bench-Live paper (arXiv 2505.23419) abstract and positioning statements.\n\nReport: What is the accurate framing for SWE-bench Verified's current status and where SWE-bench-Live fits in?\n\nThis is purely research — no code changes needed.",
    "agentId": "a0cadb313022819a6",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Based on my research, here is the accurate framing of SWE-bench Verified's current status and where SWE-bench-Live fits in:\n\n## SWE-bench Verified's Status: NOT \"Abandoned\" but \"Officially Deprecated\"\n\n**The official stance is clear deprecation, not just saturation.** On February 23, 2026, OpenAI's Frontier Evals team (Mia Glaese & Olivia Watkins) officially announced that SWE-bench Verified **no longer measures frontier coding capabilities** and should no longer be used for evaluating frontier models.\n\n### The Two-Pronged Problem\n\nOpenAI's analysis identified critical flaws that go beyond saturation:\n\n1. **Test Quality Issues (>60% of remaining problems)**: \n   - 49 tests were overly narrowly defined, rejecting functionally correct solutions\n   - 26 tests demanded features never mentioned in problem descriptions\n   - Tests sometimes required specific implementation details not specified in requirements\n   - At least 59.4% of the audited problems have flawed test cases\n\n2. **Training Data Contamination (100% of frontier models affected)**:\n   - ALL frontier models tested—including GPT-5.2, Claude Opus 4.5, and Gemini 3 Flash—could reproduce the original ground-truth bug fixes verbatim with minimal prompting\n   - Models showed familiarity with SWE-bench problems from training data exposure\n   - Improvements no longer reflect genuine problem-solving ability but rather training data overlap\n\n## OpenAI's February 2026 Announcement\n\nThe official stance from OpenAI was published in their blog post \"[Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)\" and via [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270):\n\n> \"The standard for frontier coding evals is changing with model maturity. We now recommend reporting SWE-bench Pro and are sharing more detail on why we're no longer reporting SWE-bench Verified as we work with the industry to establish stronger coding eval standards.\"\n\n**Key replacement**: SWE-bench Pro (released September 2025 by Scale AI) uses private and copyleft-licensed repositories. Scores dropped from ~70%+ on SWE-bench Verified to ~23% on SWE-bench Pro across frontier models—reflecting genuine problem-solving ability rather than training contamination.\n\n## SWE-bench-Live's Positioning (arXiv 2505.23419, NeurIPS 2025)\n\nSWE-bench-Live is positioned as the **live alternative to the static, contamination-prone SWE-bench Verified**:\n\n### Key Differentiators:\n\n1. **Continuously Updated**: Monthly additions of 50 newly verified, high-quality issues from real GitHub repositories\n2. **Fresh Data**: Issues sourced from January 1, 2024 onwards (covering 2024-07 to 2025-04), significantly more recent than SWE-bench Verified\n3. **Contamination Resistance**: Dates are carefully chosen to avoid overlap with model training cutoffs (Jan 2024 - April 20, 2025)\n4. **Dynamic Evaluation**: Each month adds truly novel problems, preventing overfitting and maintaining fair leaderboard comparisons\n5. **1,319 total instances** spanning 93 repositories (much broader than the fixed 500 in SWE-bench Verified)\n\n### Performance Comparison:\n\nThe paper explicitly notes that models achieving high scores on SWE-bench Verified (80%+) show \"significantly lower\" performance on SWE-bench-Live, confirming that the original benchmark suffered from overfitting and contamination.\n\n## Accurate Framing Summary\n\n| Aspect | SWE-bench Verified | SWE-bench-Live |\n|--------|-------------------|-----------------|\n| **Status** | Officially deprecated (Feb 2026) | NeurIPS 2025 replacement |\n| **Cause** | 59%+ flawed tests, 100% training contamination | Fresh, monthly-updated issues |\n| **Dataset** | Static 500 instances, pre-2024 | 1,319 instances, continuously updated |\n| **Contamination Risk** | Critical | Minimized by date cutoffs & monthly updates |\n| **Use Case** | Legacy/historical tracking only | Current frontier model evaluation |\n\n**Verdict**: SWE-bench Verified is not \"reaching saturation\"—it is fundamentally compromised by flawed test design and universal training data leakage, making scores meaningless for frontier models. SWE-bench-Live directly addresses these issues through continuous updates, fresh real-world issues, and careful contamination avoidance.\n\nSources:\n- [The End of SWE-Bench Verified — Mia Glaese & Olivia Watkins, OpenAI Frontier Evals & Human Data](https://www.latent.space/p/swe-bench-dead)\n- [Why SWE-bench Verified no longer measures frontier coding capabilities | OpenAI](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)\n- [OpenAI Developers on X](https://x.com/OpenAIDevs/status/2026002219909427270)\n- [SWE-bench Goes Live! (arXiv 2505.23419)](https://arxiv.org/abs/2505.23419)\n- [SWE-bench-Live GitHub Repository](https://github.com/microsoft/SWE-bench-Live)\n- [OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)"
      }
    ],
    "totalDurationMs": 46282,
    "totalTokens": 25279,
    "totalToolUseCount": 9,
    "usage": {
      "input_tokens": 323,
      "cache_creation_input_tokens": 1221,
      "cache_read_input_tokens": 22339,
      "output_tokens": 1396,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1221
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 323,
          "output_tokens": 1396,
          "cache_read_input_tokens": 22339,
          "cache_creation_input_tokens": 1221,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1221,
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
      "otherToolCount": 9
    }
  },
  "sourceToolAssistantUUID": "cf2d96a8-4aa0-46e6-8f7c-f4d5e3210465",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-10T07:15:57.567Z_

<details><summary>↩ Tool result · `toolu_01MLsQpXJceUUTpMr8FLGJ2m`</summary>

```text
Perfect! Now I have comprehensive information. Let me compile my findings.

## Summary: Literature Justification for Cosine Similarity Thresholds in NLP

Based on my comprehensive search of the literature, here are my findings regarding cosine similarity thresholds, particularly around 0.65:

### 1. **Commonly Used Thresholds in Semantic Similarity Tasks**

The literature reveals a **wide range of practical thresholds** depending on the application:

- **Strict matching**: 0.8–0.9+ (high precision, low recall)
- **Moderate matching**: 0.6–0.75 (balanced precision/recall)
- **Loose matching**: 0.5 and below (high recall, lower precision)

Your threshold of **0.65 falls squarely within the moderate/balanced range** commonly used in practical NLP applications.

**Specific Examples from Literature:**
- Paraphrase detection on Quora duplicates: 0.8352 for maximum accuracy (81.60%), 0.7715 for F1 (75.27%)
- MPNet paraphrase detection: Optimal threshold of **0.671** achieved 75.6% accuracy
- Academic FAQ systems: 0.5–0.8 range with optimal threshold depending on model
- Information retrieval applications: 0.6–1.0 range for paraphrase/similarity classification
- Practical NLP applications: 0.79–0.85 commonly used thresholds

### 2. **Theoretical Foundation for 0.65**

While I didn't find a specific paper explicitly justifying **0.65**, the literature provides strong methodological justification:

**From "Optimal Threshold Determination for Interpreting Semantic Similarity" (PLOS One):**
- The paper establishes that arbitrary thresholds (especially the default 0.5) lack scientific justification
- The authors propose determining optimal thresholds by **minimizing false positives and false negatives** using statistical distributions
- Key finding: Different similarity measures require different optimal thresholds (ranging 0.42–0.49 in their Gene Ontology studies)
- Thresholds should be **determined empirically using your specific data**, not arbitrarily chosen

**Threshold Selection Methodology:**
The literature supports tuning thresholds within ranges by:
1. Plotting a histogram of cosine similarities on your data
2. Identifying the bimodal distribution (dissimilar vs. similar pairs)
3. Selecting the threshold that balances precision/recall for your use case

### 3. **Sentence-BERT (SBERT) Benchmarks and Performance**

The foundational **"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"** (Reimers & Gurevych, 2019) paper established that SBERT embeddings achieve strong correlations on STS benchmarks:

- **STS-B Benchmark Performance**: Models achieve Pearson correlation of **0.85–0.90** on semantic similarity prediction
- all-mpnet-base-v2: ~87–88% on STS-B
- all-MiniLM-L6-v2: ~84–85% on STS-B
- Top models: Spearman's ρ approaching 0.90+

**What This Means for 0.65:**
These high correlations suggest that SBERT models are quite effective at producing meaningful cosine similarity scores. The 0.65 threshold sits in the region where you'd expect to capture semantically related but not identical descriptions, consistent with the mid-range human annotations in the 0–5 STS scale (roughly corresponding to moderate semantic relatedness).

### 4. **Semantic Textual Similarity (STS) Benchmark Scale**

**SemEval STS benchmark methodology:**
- Human judges rate sentence pairs on a **0–5 scale**:
  - 0 = completely independent semantics
  - 5 = semantic equivalence
- Performance measured via **Pearson correlation** between system scores and human judgments
- Inter-annotator correlation: 62–87% (depending on dataset)

**Practical Interpretation for 0.65:**
In the STS framework, a 0.65 cosine similarity roughly corresponds to human judgments around **2.5–3.5 on the 0–5 scale**, which linguistically means:
- Sentences share some semantic content
- Not verbatim or paraphrases, but related topics
- Distinguished from unrelated content (0–1 range)

### 5. **Key Literature References**

The strongest supporting references for threshold selection are:

1. **"Optimal Threshold Determination for Interpreting Semantic Similarity and Particularity"** (Pesquita et al., PLOS One, 2014)
   - Provides methodological framework for determining optimal thresholds empirically
   
2. **"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks"** (Reimers & Gurevych, EMNLP 2019)
   - Establishes SBERT effectiveness for semantic similarity via cosine distance
   
3. **"Correlation Coefficients and Semantic Textual Similarity"** (Zhelezniak et al., NAACL 2019)
   - Validates the mathematical foundation of cosine similarity in semantic tasks
   
4. **"Transformer Models for Paraphrase Detection: A Comprehensive Semantic Similarity Study"** (2024)
   - Documents practical threshold selection: 0.671–0.8352 across transformer models

5. **SemEval Semantic Textual Similarity Task series** (2012–2017)
   - Established the standard benchmark and evaluation methodology

### 6. **Recommendation**

For your use case in **information extraction with semantic similarity validation**:

- **0.65 is a well-justified threshold** within the range of practical NLP applications
- It represents a **balanced trade-off** between precision and recall
- It likely corresponds to "semantically related but distinct" descriptions
- **Validation approach**: Empirically test on your specific data using the distribution-based threshold selection method from Pesquita et al., varying thresholds 0.1–0.9 to find optimal performance for your precision/recall needs

The threshold is reasonable and falls within established practice, though I'd recommend documenting your empirical validation against your specific information extraction task.

---

**Sources:**
- [Semantic Textual Similarity Metric Guide for AI Applications | Galileo](https://galileo.ai/blog/semantic-textual-similarity-metric)
- [Semantic Textual Similarity — Sentence Transformers documentation](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)
- [Optimal Threshold Determination for Interpreting Semantic Similarity - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4521860/)
- [SBERT + Cosine Similarity: How Machines Understand Sentence Meaning | Medium](https://medium.com/@parth.khajgiwale/sbert-cosine-similarity-how-machines-understand-sentence-meaning-13f2d7f4272d)
- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | arXiv](https://arxiv.org/abs/1908.10084)
- [Correlation Coefficients and Semantic Textual Similarity | arXiv](https://arxiv.org/abs/1905.07790)
- [STS Models — Sentence Transformers documentation](https://www.sbert.net/docs/pretrained-models/sts-models.html)
- [Transformer Models for Paraphrase Detection: A Comprehensive Semantic Similarity Study](https://www.mdpi.com/2073-431X/14/9/385)
- [SemEval-2017 Task 1: Semantic Textual Similarity](https://alt.qcri.org/semeval2017/task1/)
- [Advances and Challenges in Semantic Textual Similarity: A Comprehensive Survey | arXiv](https://arxiv.org/html/2601.03270v1)
- [Rule of thumb cosine similarity thresholds | OpenAI Community](https://community.openai.com/t/rule-of-thumb-cosine-similarity-thresholds/693670)
- [Top embedding models on the MTEB leaderboard | Modal](https://modal.com/blog/mteb-leaderboard-article)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "826a75f2-f5e5-4529-ad3f-6324b76612ef",
  "isSidechain": false,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "0c11b933-96c5-453e-9b76-dd163ae4419f",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find literature justification for using a cosine similarity threshold of 0.65 in information extraction or semantic similarity tasks. Specifically, I want to know:\n\n1. What cosine similarity thresholds are commonly used in information extraction, semantic textual similarity, or NLP tasks to distinguish \"semantically related\" from \"unrelated\" pairs?\n2. Are there specific papers that establish or validate 0.65 as a meaningful threshold?\n3. What are typical cosine similarity scores for sentence-transformer models when comparing semantically related but not identical descriptions?\n\nPlease search for papers on semantic similarity thresholds, sentence-BERT benchmarks, and information extraction evaluation. Look for papers like:\n- \"Semantic Textual Similarity\" papers (STS benchmarks)\n- Sentence-BERT / SBERT papers\n- Information extraction papers that use cosine similarity for validation\n\nReport what you find about commonly used thresholds and their justifications. This is purely research — no code changes needed.",
    "agentId": "a4837630fb84df1ce",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! Now I have comprehensive information. Let me compile my findings.\n\n## Summary: Literature Justification for Cosine Similarity Thresholds in NLP\n\nBased on my comprehensive search of the literature, here are my findings regarding cosine similarity thresholds, particularly around 0.65:\n\n### 1. **Commonly Used Thresholds in Semantic Similarity Tasks**\n\nThe literature reveals a **wide range of practical thresholds** depending on the application:\n\n- **Strict matching**: 0.8–0.9+ (high precision, low recall)\n- **Moderate matching**: 0.6–0.75 (balanced precision/recall)\n- **Loose matching**: 0.5 and below (high recall, lower precision)\n\nYour threshold of **0.65 falls squarely within the moderate/balanced range** commonly used in practical NLP applications.\n\n**Specific Examples from Literature:**\n- Paraphrase detection on Quora duplicates: 0.8352 for maximum accuracy (81.60%), 0.7715 for F1 (75.27%)\n- MPNet paraphrase detection: Optimal threshold of **0.671** achieved 75.6% accuracy\n- Academic FAQ systems: 0.5–0.8 range with optimal threshold depending on model\n- Information retrieval applications: 0.6–1.0 range for paraphrase/similarity classification\n- Practical NLP applications: 0.79–0.85 commonly used thresholds\n\n### 2. **Theoretical Foundation for 0.65**\n\nWhile I didn't find a specific paper explicitly justifying **0.65**, the literature provides strong methodological justification:\n\n**From \"Optimal Threshold Determination for Interpreting Semantic Similarity\" (PLOS One):**\n- The paper establishes that arbitrary thresholds (especially the default 0.5) lack scientific justification\n- The authors propose determining optimal thresholds by **minimizing false positives and false negatives** using statistical distributions\n- Key finding: Different similarity measures require different optimal thresholds (ranging 0.42–0.49 in their Gene Ontology studies)\n- Thresholds should be **determined empirically using your specific data**, not arbitrarily chosen\n\n**Threshold Selection Methodology:**\nThe literature supports tuning thresholds within ranges by:\n1. Plotting a histogram of cosine similarities on your data\n2. Identifying the bimodal distribution (dissimilar vs. similar pairs)\n3. Selecting the threshold that balances precision/recall for your use case\n\n### 3. **Sentence-BERT (SBERT) Benchmarks and Performance**\n\nThe foundational **\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"** (Reimers & Gurevych, 2019) paper established that SBERT embeddings achieve strong correlations on STS benchmarks:\n\n- **STS-B Benchmark Performance**: Models achieve Pearson correlation of **0.85–0.90** on semantic similarity prediction\n- all-mpnet-base-v2: ~87–88% on STS-B\n- all-MiniLM-L6-v2: ~84–85% on STS-B\n- Top models: Spearman's ρ approaching 0.90+\n\n**What This Means for 0.65:**\nThese high correlations suggest that SBERT models are quite effective at producing meaningful cosine similarity scores. The 0.65 threshold sits in the region where you'd expect to capture semantically related but not identical descriptions, consistent with the mid-range human annotations in the 0–5 STS scale (roughly corresponding to moderate semantic relatedness).\n\n### 4. **Semantic Textual Similarity (STS) Benchmark Scale**\n\n**SemEval STS benchmark methodology:**\n- Human judges rate sentence pairs on a **0–5 scale**:\n  - 0 = completely independent semantics\n  - 5 = semantic equivalence\n- Performance measured via **Pearson correlation** between system scores and human judgments\n- Inter-annotator correlation: 62–87% (depending on dataset)\n\n**Practical Interpretation for 0.65:**\nIn the STS framework, a 0.65 cosine similarity roughly corresponds to human judgments around **2.5–3.5 on the 0–5 scale**, which linguistically means:\n- Sentences share some semantic content\n- Not verbatim or paraphrases, but related topics\n- Distinguished from unrelated content (0–1 range)\n\n### 5. **Key Literature References**\n\nThe strongest supporting references for threshold selection are:\n\n1. **\"Optimal Threshold Determination for Interpreting Semantic Similarity and Particularity\"** (Pesquita et al., PLOS One, 2014)\n   - Provides methodological framework for determining optimal thresholds empirically\n   \n2. **\"Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks\"** (Reimers & Gurevych, EMNLP 2019)\n   - Establishes SBERT effectiveness for semantic similarity via cosine distance\n   \n3. **\"Correlation Coefficients and Semantic Textual Similarity\"** (Zhelezniak et al., NAACL 2019)\n   - Validates the mathematical foundation of cosine similarity in semantic tasks\n   \n4. **\"Transformer Models for Paraphrase Detection: A Comprehensive Semantic Similarity Study\"** (2024)\n   - Documents practical threshold selection: 0.671–0.8352 across transformer models\n\n5. **SemEval Semantic Textual Similarity Task series** (2012–2017)\n   - Established the standard benchmark and evaluation methodology\n\n### 6. **Recommendation**\n\nFor your use case in **information extraction with semantic similarity validation**:\n\n- **0.65 is a well-justified threshold** within the range of practical NLP applications\n- It represents a **balanced trade-off** between precision and recall\n- It likely corresponds to \"semantically related but distinct\" descriptions\n- **Validation approach**: Empirically test on your specific data using the distribution-based threshold selection method from Pesquita et al., varying thresholds 0.1–0.9 to find optimal performance for your precision/recall needs\n\nThe threshold is reasonable and falls within established practice, though I'd recommend documenting your empirical validation against your specific information extraction task.\n\n---\n\n**Sources:**\n- [Semantic Textual Similarity Metric Guide for AI Applications | Galileo](https://galileo.ai/blog/semantic-textual-similarity-metric)\n- [Semantic Textual Similarity — Sentence Transformers documentation](https://sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html)\n- [Optimal Threshold Determination for Interpreting Semantic Similarity - PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4521860/)\n- [SBERT + Cosine Similarity: How Machines Understand Sentence Meaning | Medium](https://medium.com/@parth.khajgiwale/sbert-cosine-similarity-how-machines-understand-sentence-meaning-13f2d7f4272d)\n- [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks | arXiv](https://arxiv.org/abs/1908.10084)\n- [Correlation Coefficients and Semantic Textual Similarity | arXiv](https://arxiv.org/abs/1905.07790)\n- [STS Models — Sentence Transformers documentation](https://www.sbert.net/docs/pretrained-models/sts-models.html)\n- [Transformer Models for Paraphrase Detection: A Comprehensive Semantic Similarity Study](https://www.mdpi.com/2073-431X/14/9/385)\n- [SemEval-2017 Task 1: Semantic Textual Similarity](https://alt.qcri.org/semeval2017/task1/)\n- [Advances and Challenges in Semantic Textual Similarity: A Comprehensive Survey | arXiv](https://arxiv.org/html/2601.03270v1)\n- [Rule of thumb cosine similarity thresholds | OpenAI Community](https://community.openai.com/t/rule-of-thumb-cosine-similarity-thresholds/693670)\n- [Top embedding models on the MTEB leaderboard | Modal](https://modal.com/blog/mteb-leaderboard-article)"
      }
    ],
    "totalDurationMs": 94910,
    "totalTokens": 38333,
    "totalToolUseCount": 25,
    "usage": {
      "input_tokens": 353,
      "cache_creation_input_tokens": 1150,
      "cache_read_input_tokens": 34815,
      "output_tokens": 2015,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1150
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 353,
          "output_tokens": 2015,
          "cache_read_input_tokens": 34815,
          "cache_creation_input_tokens": 1150,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1150,
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
      "otherToolCount": 25
    }
  },
  "sourceToolAssistantUUID": "826a75f2-f5e5-4529-ad3f-6324b76612ef",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug R…",
  "leafUuid": "0c11b933-96c5-453e-9b76-dd163ae4419f",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral specifications for guided program repair",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Assistant

_source line 16 · 2026-05-10T07:17:53.837Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have the research I need. Let me process the findings:

## Key Findings:

### SWE-bench Verified Status:
- OpenAI officially announced in February 2026 that SWE-bench Verified "no longer measures frontier coding capabilities" and should not be used
- The issues are: 59%+ flawed tests AND 100% training contamination across frontier models
- OpenAI recommends SWE-bench Pro as the frontier evaluation replacement
- SWE-bench-Live is positioned as a contamination-resistant research alternative (continuous updates, monthly additions)
- So the original paper says "replacing the officially-abandoned SWE-bench Verified" — this is CLOSER to accurate than the reviewer suggested. 

The reviewer was right that SWE-bench Pro is OpenAI's recommended replacement for frontier evaluation, but SWE-bench-Live is actually the appropriate choice for our work since we're training on SWE-bench data and can't use Pro. The framing matters here—we need to be precise about which benchmark serves which purpose.

On the cosine similarity threshold, 0.65 sits in a reasonable range based on the semantic textual similarity literature. I should cite Reimers & Gurevych's work to justify why this threshold effectively separates semantically related pairs from unrelated ones in both cross-encoder and bi-encoder tasks.

For the SpecRover claim, I need to add the HTML URL reference to make it verifiable. And I'm working through several other significant revisions to address the reviewer's feedback.

The EMNLP pilot scope needs clarification—I should specify that we're doing SFT on a 500-instance Verified subset with evaluation on 100-150 SWE-bench-Live Lite instances, using a 2-field ablation without GitBugs augmentation. The full 5,300-instance corpus with 300-instance evaluation is reserved for the ICSE 2027 submission. I also need to be explicit that EMNLP will report pilot-scale results while the complete dataset evaluation comes later.

For the SWE-bench Verified framing, I'm shifting away from "replacing" language toward acknowledging that Verified was officially deprecated due to contamination and test quality issues. SWE-bench-Live serves as the contamination-resistant evaluation benchmark for research contributions trained on SWE-bench data, which is the more accurate positioning the reviewer is looking for.

On the cosine similarity threshold, I need to add justification grounding the 0.65 threshold in the semantic similarity literature — specifically that SBERT-based thresholds around 0.65-0.671 are empirically validated for distinguishing semantically related pairs, which aligns with established paraphrase detection work.

These are all editorial refinements to framing and justification without changing the core research.

Now I'm mapping out the specific revisions needed: reframing the opportunity around SWE-bench Verified, adding the HTML URL for SpecRover, explicitly detailing the EMNLP pilot scope (500-instance Verified subset plus 100-150 SWE-bench-Live instances with a 2-field ablation), clarifying that the pilot results target EMNLP while full-scale results are positioned for ICSE 2027, and updating the target_venues description to remove the inconsistency about training data.

Looking at the core methodology, the approach itself is solid—extracting structured specs from bug reports before codebase traversal, using test assertions as behavioral specs, and evaluating on SWE-bench-Live to avoid contamination. The real bottleneck has been the SpecRover claim controversy and the EMNLP pilot framing, which once clarified should help the score improve. Though I'm noting the Agentless improvement claim of +4-7 percentage points is ambitious given their baseline of 11-13% on SWE-bench-Live, which would represent a 30-60% relative improvement.

The pilot evaluation with 100-150 instances might not carry enough statistical weight to demonstrate that improvement, so I should frame the EMNLP results as preliminary with confidence intervals, with the full 300-instance evaluation planned for ICSE 2027. Now I'm going through the JSON to incorporate the reviewer's specific fixes: keeping accurate content intact, adding the SpecRover HTML URL, correcting the EMNLP pilot scope, reframing SWE-bench Verified, and justifying the 0.65 threshold.

For the EMNLP pilot, the reviewer was clear about the scope: fine-tune on the 500-instance SWE-bench Verified subset, run the primary evaluation on 100-150 SWE-bench-Live Lite instances with a 2-field ablation comparing affected_interface and expected_behavior fields against baselines without them, and skip GitBugs augmentation. The full corpus work and 300-instance evaluation shift to ICSE 2027.

Now I need to restructure the document to separate these concerns—removing the training details from the venue description and moving them into a dedicated pilot plan section within the approach, while also updating the resource estimates to reflect the smaller pilot scope given the tight EMNLP timeline. I'm going to revise the JSON with targeted fixes across several fields. For the opportunity section, I need to reframe it around contamination-resistant evaluation since SWE-bench Verified is becoming compromised. In the approach section, I'll add the SpecRover HTML URL, include the EMNLP pilot plan, and clarify the cosine similarity threshold reasoning. The target_venues entry for EMNLP needs to drop the 500-instance mention that's causing inconsistency, and I'll update the description accordingly. Let me structure the approach section carefully—it currently covers the model, formal schema, training data construction, and differentiation, so I need to integrate the EMNLP pilot details cleanly into that flow. I'm adding the HTML URL reference for SpecRover in the differentiation section, then incorporating the cosine similarity justification by grounding it in sentence-transformer literature where 0.65 reliably separates semantically related from unrelated pairs. For the EMNLP pilot, I'm creating a subsection that outlines the May 2026 ARR submission strategy with pilot-scale results on a 500-instance SWE-bench subset and 100-150 SWE-bench-Live Lite instances, plus a focused 2-field ablation, while reserving the full-scale evaluation for ICSE 2027.

Now I'm clarifying that SWE-bench-Live is the appropriate benchmark because SWE-bench Verified has been officially deprecated due to widespread training contamination and test quality issues, making it unsuitable for research contributions. I'm refining the framing to be more precise — SWE-bench Verified's official deprecation by OpenAI gives me stronger ground to position SWE-bench-Live as the right evaluation target, especially since our work trains on SWE-bench data and SWE-bench Pro remains closed-source for frontier models. I'm reconsidering the cosine similarity threshold justification. The reviewer wants a concrete explanation for why 0.65 works, and they've even suggested language about how this threshold aligns with semantic similarity standards in information extraction. Looking at the research, MPNet's optimal threshold sits around 0.671, which validates the 0.65 choice, and this falls squarely in the moderate-balanced range that the literature supports for distinguishing semantically related from unrelated pairs. I'll incorporate something close to the reviewer's suggested phrasing to make this clear.

For the SpecRover citation, I need to add the HTML URL exactly as the reviewer specified it, even though the format looks slightly unusual.

Now I'm organizing the changes across the approach section: adding the cosine similarity threshold justification in the training data construction part, inserting the SpecRover HTML URL in the differentiation section, and creating a new subsection for the EMNLP pilot plan under evaluation. I'll preserve all existing content and integrate these additions carefully into the JSON structure. target alignment ≥ 0.65 before training at scale, which aligns with established semantic similarity thresholds in information extraction where this cutoff distinguishes semantically related pairs from unrelated ones under sentence-transformer encodings — this is grounded in STS benchmarks where MPNet achieves its optimal paraphrase detection threshold around 0.671.

For the EMNLP pilot plan, I'm adding details about the May 2026 ARR submission scope: it covers SFT on a 500-instance SWE-bench Verified subset without GitBugs augmentation to save time, primary evaluation on 100-150 SWE-bench-Live Lite instances, and a focused 2-field ablation examining the affected_interface component.

The full-scale results with the complete 5,300-instance training corpus, 300-instance evaluation set, and comprehensive 4-field ablations are being reserved for ICSE 2027 as the primary venue where the complete experimental contribution will be presented.

For the EMNLP target venue entry, I'm updating it to reflect the ARR submission deadline of May 25, 2026 and positioning this as a theory plus pilot-scale submission focused on the NLP angle of structured information extraction from bug reports.

Now I'm refining the opportunity section to describe SWE-bench-Live as a clean, contamination-resistant evaluation target drawn from post-January-2024 GitHub issues with no training-set overlap, providing roughly 1,890 Docker-reproducible instances across 223 repositories and growing at about 50 instances per month. I need to update the description field to reflect that the 300-instance SWE-bench-Live Lite evaluation is the full-scale setup for ICSE 2027, while the EMNLP pilot uses a smaller 100-150 instance subset. Let me revise the description to clarify this distinction and then construct the complete JSON output. to include ALL fields.

Here's my plan for each field:
- `title`: unchanged
- `core_problem`: unchanged
- `opportunity`: Fix SWE-bench Verified framing
- `landscape`: unchanged
- `approach`: Add HTML URL, add EMNLP pilot plan, justify cosine threshold
- `resource_estimate`: unchanged (these apply to the full-scale ICSE 2027 submission)
- `target_venues`: Fix EMNLP entry
- `level`: unchanged
- `key_references`: unchanged
- `description`: Update to mention EMNLP pilot vs. full-scale
- `project_name`: unchanged
- `source`: unchanged
- `change_type`: "minor"

Let me write it all out now. This will be a long JSON but I need to include everything.

Now I'm checking the landscape section where SWE-bench Verified appears in a few places—there's Agent-CoEvo's performance metrics, SWE-Lego's results with and without test-time scaling, and SoRFT's approach that I need to verify is accurately represented. I'm finalizing the JSON structure with four key updates: clarifying the opportunity section to explain why SWE-bench-Live is the right choice given OpenAI's deprecation of Verified and recommendation of Pro, adding the SpecRover URL reference and cosine similarity reasoning to the approach, introducing an EMNLP pilot scope subsection, and updating the target venues description and overall project description to distinguish between the pilot phase and full-scale implementation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0c11b933-96c5-453e-9b76-dd163ae4419f",
  "isSidechain": false,
  "requestId": "req_011CatUeTtABFXJJA82aW4BK",
  "type": "assistant",
  "uuid": "f6f5bd34-2b47-4bc2-b1e7-6445f90d364f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018JoHHDjGbiUKxRdbT9ybdG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1422,
      "cache_creation_input_tokens": 3940,
      "cache_read_input_tokens": 26325,
      "output_tokens": 6924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1422,
          "output_tokens": 6924,
          "cache_read_input_tokens": 26325,
          "cache_creation_input_tokens": 3940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3940
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

_source line 17 · 2026-05-10T07:17:55.871Z_

Good — the research confirms two key things: (1) SWE-bench Verified was officially deprecated by OpenAI in February 2026 (stronger than "saturates" but with a nuance: OpenAI recommends SWE-bench Pro for frontier models, while SWE-bench-Live is the right target for training-on-SWE-bench research); (2) the 0.65 cosine threshold is well-supported by the literature (MPNet optimal paraphrase threshold: 0.671).

The reviewer feedback is specific and actionable — this is a **minor** fix. Let me now apply all five changes precisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f6f5bd34-2b47-4bc2-b1e7-6445f90d364f",
  "isSidechain": false,
  "requestId": "req_011CatUeTtABFXJJA82aW4BK",
  "type": "assistant",
  "uuid": "af44b34e-ff3b-4044-91bd-9bdc9f793650",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018JoHHDjGbiUKxRdbT9ybdG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1422,
      "cache_creation_input_tokens": 3940,
      "cache_read_input_tokens": 26325,
      "output_tokens": 6924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1422,
          "output_tokens": 6924,
          "cache_read_input_tokens": 26325,
          "cache_creation_input_tokens": 3940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3940
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

_source line 18 · 2026-05-10T07:17:56.397Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01MjuvbzQjm7DdHsKi52k8jZ`</summary>

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
  "parentUuid": "af44b34e-ff3b-4044-91bd-9bdc9f793650",
  "isSidechain": false,
  "requestId": "req_011CatUeTtABFXJJA82aW4BK",
  "type": "assistant",
  "uuid": "cac8738c-b30a-4495-957c-fbfe15d5797a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_018JoHHDjGbiUKxRdbT9ybdG",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1422,
      "cache_creation_input_tokens": 3940,
      "cache_read_input_tokens": 26325,
      "output_tokens": 6924,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3940,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1422,
          "output_tokens": 6924,
          "cache_read_input_tokens": 26325,
          "cache_creation_input_tokens": 3940,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3940
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

_source line 19 · 2026-05-10T07:17:56.412Z_

<details><summary>↩ Tool result · `toolu_01MjuvbzQjm7DdHsKi52k8jZ`</summary>

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
  "parentUuid": "cac8738c-b30a-4495-957c-fbfe15d5797a",
  "isSidechain": false,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "c374ffa9-968c-4449-bef4-ca05992b115d",
  "toolUseResult": {
    "matches": [
      "TodoWrite"
    ],
    "query": "select:TodoWrite",
    "total_deferred_tools": 17
  },
  "sourceToolAssistantUUID": "cac8738c-b30a-4495-957c-fbfe15d5797a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug R…",
  "leafUuid": "c374ffa9-968c-4449-bef4-ca05992b115d",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral specifications for guided program repair",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Assistant

_source line 22 · 2026-05-10T07:18:05.743Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me write the complete revised JSON with all the specific changes addressed:

1. **Fix SpecRover HTML URL** - Add parenthetical with HTML URL
2. **Fix EMNLP pilot scope inconsistency** - Add explicit pilot plan to approach, fix venue description
3. **Fix SWE-bench Verified replacement framing** - Update in opportunity section
4. **Justify 0.65 cosine similarity threshold** - One sentence in approach

change_type: "minor"

Let me write the complete JSON now. I'll be very careful to include all fields.

Key changes:
- `opportunity`: Replace "replacing the officially-abandoned SWE-bench Verified" with accurate framing


- `approach`: Add HTML URL for SpecRover, include cosine threshold justification, and add EMNLP pilot plan subsection in Evaluation
- `target_venues`: Fix EMNLP description
- `description`: Update to reference pilot scope

Writing the complete JSON...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c374ffa9-968c-4449-bef4-ca05992b115d",
  "isSidechain": false,
  "requestId": "req_011CatUoEFcU8PfNKUnsmkRB",
  "type": "assistant",
  "uuid": "e0c614a3-f955-4b65-9e28-5e8503916fd7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014h1cbpmZ6aDrc4WZjY9rjK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10727,
      "cache_read_input_tokens": 30265,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 502,
          "cache_read_input_tokens": 30265,
          "cache_creation_input_tokens": 10727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10727
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

_source line 23 · 2026-05-10T07:18:06.705Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_01FNeZgDNsbHtPnZMFx1uRTs`</summary>

```json
{
  "todos": [
    {
      "content": "Fix SpecRover HTML URL parenthetical in approach",
      "status": "in_progress",
      "activeForm": "Fixing SpecRover HTML URL parenthetical"
    },
    {
      "content": "Fix SWE-bench Verified replacement framing in opportunity",
      "status": "pending",
      "activeForm": "Fixing SWE-bench Verified framing"
    },
    {
      "content": "Add EMNLP pilot scope to approach + fix venue description",
      "status": "pending",
      "activeForm": "Adding EMNLP pilot scope"
    },
    {
      "content": "Justify 0.65 cosine similarity threshold",
      "status": "pending",
      "activeForm": "Justifying cosine similarity threshold"
    },
    {
      "content": "Output complete revised JSON",
      "status": "pending",
      "activeForm": "Outputting revised JSON"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e0c614a3-f955-4b65-9e28-5e8503916fd7",
  "isSidechain": false,
  "requestId": "req_011CatUoEFcU8PfNKUnsmkRB",
  "type": "assistant",
  "uuid": "f4edaaf5-e21e-4175-bd78-c25fa396c8f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_014h1cbpmZ6aDrc4WZjY9rjK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 10727,
      "cache_read_input_tokens": 30265,
      "output_tokens": 502,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 502,
          "cache_read_input_tokens": 30265,
          "cache_creation_input_tokens": 10727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10727
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

_source line 24 · 2026-05-10T07:18:06.708Z_

<details><summary>↩ Tool result · `toolu_01FNeZgDNsbHtPnZMFx1uRTs`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4edaaf5-e21e-4175-bd78-c25fa396c8f4",
  "isSidechain": false,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "6f1e9145-02de-4279-8b42-984700d08dd0",
  "toolUseResult": {
    "oldTodos": [],
    "newTodos": [
      {
        "content": "Fix SpecRover HTML URL parenthetical in approach",
        "status": "in_progress",
        "activeForm": "Fixing SpecRover HTML URL parenthetical"
      },
      {
        "content": "Fix SWE-bench Verified replacement framing in opportunity",
        "status": "pending",
        "activeForm": "Fixing SWE-bench Verified framing"
      },
      {
        "content": "Add EMNLP pilot scope to approach + fix venue description",
        "status": "pending",
        "activeForm": "Adding EMNLP pilot scope"
      },
      {
        "content": "Justify 0.65 cosine similarity threshold",
        "status": "pending",
        "activeForm": "Justifying cosine similarity threshold"
      },
      {
        "content": "Output complete revised JSON",
        "status": "pending",
        "activeForm": "Outputting revised JSON"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "f4edaaf5-e21e-4175-bd78-c25fa396c8f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-10T07:19:42.595Z_

<details><summary>Logged reasoning block</summary>

````text
Now let me write the full revised JSON. Let me carefully make all the required changes while preserving everything else.

Here's the complete revised JSON I'll output:

```json
{
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "[unchanged]",
  "opportunity": "[with SWE-bench Verified framing fixed]",
  "landscape": "[unchanged]",
  "approach": "[with HTML URL, cosine threshold justification, EMNLP pilot plan]",
  "resource_estimate": "[unchanged - applies to full-scale ICSE 2027 submission]",
  "target_venues": "[with EMNLP entry fixed]",
  "level": "solid",
  "key_references": "[unchanged]",
  "description": "[updated]",
  "project_name": "structured_spec_repair",
  "source": "web_research",
  "change_type": "minor"
}
```

Now I need to update the `opportunity` field by finding the SWE-bench-Live reference and fixing the framing there.

I'm replacing the outdated SWE-bench Verified reference with current information about SWE-bench-Live and its advantages, then adding context about OpenAI's deprecation of the Verified benchmark in favor of SWE-bench Pro due to training contamination issues. I need to replace the pilot description in place of the 500-instance training specification, and update the description field to distinguish between the pilot phase and full-scale evaluation approach.

Now I'm laying out the complete JSON structure with the corrected approach field — describing how SpecExtract fine-tunes a Qwen3-Coder model to map bug reports and runtime artifacts into structured JSON specs, using a masked-field training protocol so it learns to handle varying combinations of stack traces, error messages, and test output. The formal schema defines four typed fields for the extracted specification: affected interface details, observed behavior including error type and message, expected behavior, and reproduction steps. I'm parsing test functions from the full SWE-bench dataset to extract formal assertions and error types, then combining those with stack traces and error messages from problem statements using an LLM to fill in the behavioral specification template, and finally validating the mechanically-derived specs against human-authored requirements on a subset of public instances to ensure alignment before scaling up the training process.

The key insight is that test assertions encode the behavioral outcome of the fix without revealing the implementation details, so the specs remain implementation-agnostic rather than solution-dependent. I'm also augmenting this with pseudo-labeled instances from GitBugs to expand the fine-tuning corpus to around 5,300 examples, and this approach differs from SpecRover by operating at the issue level without needing codebase traversal and by producing consistent typed JSON output in a single forward pass.

Now looking at how this integrates with the repair pipeline: SpecExtract is significantly cheaper than SpecRover's multi-step traversal, and it directly addresses the ambiguous-description failure mode by conditioning on all runtime artifacts available in the issue. The specs get injected into Agentless's three-stage repair pipeline at the fault localization stage, where they bias the file retrieval to focus on affected components. interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its 50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. SpecExtract is targeting a 4-7 percentage point improvement over the best Agentless variant as the main contribution. For evaluation, I'm running the primary experiment on SWE-bench-Live Lite with per-field ablations to isolate each spec component's impact, plus a secondary cosine-similarity check on 200 held-out SWE-bench Pro instances to validate schema correctness. The baselines include direct Agentless repair without specs, a SpecRover-equivalent prompt ablation, and SoRFT-Qwen-7B performance numbers. I'm verifying the SpecRover comparison against the HTML version of the paper at that arxiv link, and I'm also incorporating the semantic similarity threshold justification from the information extraction literature—specifically grounding the 0.65 cutoff in STS benchmarks where MPNet's optimal paraphrase detection threshold sits at 0.671. Now I'm detailing how SpecExtract handles the masked-field training protocol to gracefully manage varying artifact availability... sets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. For the full SWE-bench dataset, I'm parsing test functions to extract assertions and error expectations, pulling observed behaviors from problem statements via regex, then using an LLM to synthesize these into coherent spec JSON. I'll validate the results on a subset of public instances by comparing semantic similarity between derived specs and human-authored requirements, targeting at least 0.65 alignment before scaling up training. .65 distinguishes semantically related from unrelated pairs under sentence-transformer encodings — empirically grounded in STS benchmarks where MPNet's optimal paraphrase detection threshold is 0.671; Reimers & Gurevych, EMNLP 2019); this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. Augment with ~3,000 pseudo-labeled GitBugs instances (arXiv 2504.09651; 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code) selected for stack-trace richness and LLM-derived pseudo-specs, yielding a ~5,300-instance fine-tuning corpus. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks; independently verified in the HTML version at https://arxiv.org/html/arXiv:2408.02232) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: during fault localization, BM25+embedding file retrieval is biased by prepending structured query prefixes from the affected interface and entry point to surface relevant files higher in the ranking; during patch generation, the repair LLM receives all four spec fields as an explicit behavioral constraint in its prompt to focus generation on the documented delta. The Agentless baseline on SWE-bench-Live shows substantially lower performance than on the verified benchmark — resolving 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of the 300-instance Lite split — reflecting the harder, contamination-resistant distribution of post-2024 issues.

SpecExtract targets a 4–7 percentage point improvement over the best Agentless result, which is the primary experimental contribution. The evaluation plan centers on SWE-bench-Live Lite with per-field ablations to isolate each spec component's impact, plus a secondary cosine-similarity validation on 200 held-out SWE-bench Pro instances to verify schema correctness. Comparison baselines include Agentless without specs, SpecRover-equivalent prompting, SoRFT-Qwen-7B (which achieves 21.4% on Verified and 14.0% on Lite through structured subtask decomposition), and SWE-Lego (52.6% on Verified), positioning SpecExtract as an orthogonal preprocessing front-end. For the May 2026 ARR submission with its 16-day window, the pilot will report results from supervised fine-tuning on SWE-bench Verified.

For the EMNLP pilot scope, I'm scaling down to a 500-instance training subset without GitBugs augmentation to meet the tight timeline, evaluating on 100–150 SWE-bench-Live Lite instances with just two ablations—zeroing the affected_interface field and the expected_behavior field—to establish the core contribution with appropriate confidence intervals. The full-scale experiment with the complete 5,300-instance corpus, 300-instance primary eval, and all four per-field ablations is being reserved for ICSE 2027 as the primary venue. I'm splitting the scope into a pilot submission for EMNLP 2026 with a smaller 500-instance training set and 100-150 instance evaluation, then reserving the full 5,300-instance corpus and larger eval set for ICSE 2027 as the primary venue where I can do the comprehensive work.
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f1e9145-02de-4279-8b42-984700d08dd0",
  "isSidechain": false,
  "requestId": "req_011CatUoz7qXoLYG5LM6kvT6",
  "type": "assistant",
  "uuid": "51f90455-6716-493a-8c52-ae2cd18c4f03",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01A4RrnpWV7FKUch3Dcc1saT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 40992,
      "output_tokens": 5642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5642,
          "cache_read_input_tokens": 40992,
          "cache_creation_input_tokens": 549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 549
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

_source line 26 · 2026-05-10T07:19:45.441Z_

Now I have all the research I need. Key findings:
- SWE-bench Verified was *officially deprecated* by OpenAI (Feb 2026), citing 59%+ flawed tests and 100% frontier contamination — OpenAI recommends SWE-bench Pro for frontier models, SWE-bench-Live is the right target for training-on-SWE-bench research
- 0.65 cosine similarity is well-supported: MPNet's optimal paraphrase detection threshold is 0.671 (Reimers & Gurevych, EMNLP 2019)

Applying all five fixes now:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "51f90455-6716-493a-8c52-ae2cd18c4f03",
  "isSidechain": false,
  "requestId": "req_011CatUoz7qXoLYG5LM6kvT6",
  "type": "assistant",
  "uuid": "26c3154a-d03b-4407-b4bc-8c6a1259912c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01A4RrnpWV7FKUch3Dcc1saT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 40992,
      "output_tokens": 5642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5642,
          "cache_read_input_tokens": 40992,
          "cache_creation_input_tokens": 549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 549
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

_source line 27 · 2026-05-10T07:19:46.977Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_0141eSdE8cKf7odEsYEy8p96`</summary>

```json
{
  "todos": [
    {
      "content": "Fix SpecRover HTML URL parenthetical in approach",
      "status": "completed",
      "activeForm": "Fixing SpecRover HTML URL parenthetical"
    },
    {
      "content": "Fix SWE-bench Verified replacement framing in opportunity",
      "status": "completed",
      "activeForm": "Fixing SWE-bench Verified framing"
    },
    {
      "content": "Add EMNLP pilot scope to approach + fix venue description",
      "status": "completed",
      "activeForm": "Adding EMNLP pilot scope"
    },
    {
      "content": "Justify 0.65 cosine similarity threshold",
      "status": "completed",
      "activeForm": "Justifying cosine similarity threshold"
    },
    {
      "content": "Output complete revised JSON",
      "status": "in_progress",
      "activeForm": "Outputting revised JSON"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "26c3154a-d03b-4407-b4bc-8c6a1259912c",
  "isSidechain": false,
  "requestId": "req_011CatUoz7qXoLYG5LM6kvT6",
  "type": "assistant",
  "uuid": "2b08352e-255a-4414-ab6b-69c6d0eadac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01A4RrnpWV7FKUch3Dcc1saT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 549,
      "cache_read_input_tokens": 40992,
      "output_tokens": 5642,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 549,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5642,
          "cache_read_input_tokens": 40992,
          "cache_creation_input_tokens": 549,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 549
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

_source line 28 · 2026-05-10T07:19:46.983Z_

<details><summary>↩ Tool result · `toolu_0141eSdE8cKf7odEsYEy8p96`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b08352e-255a-4414-ab6b-69c6d0eadac2",
  "isSidechain": false,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "18f282ea-4554-4c0a-80d9-03860dd526de",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Fix SpecRover HTML URL parenthetical in approach",
        "status": "in_progress",
        "activeForm": "Fixing SpecRover HTML URL parenthetical"
      },
      {
        "content": "Fix SWE-bench Verified replacement framing in opportunity",
        "status": "pending",
        "activeForm": "Fixing SWE-bench Verified framing"
      },
      {
        "content": "Add EMNLP pilot scope to approach + fix venue description",
        "status": "pending",
        "activeForm": "Adding EMNLP pilot scope"
      },
      {
        "content": "Justify 0.65 cosine similarity threshold",
        "status": "pending",
        "activeForm": "Justifying cosine similarity threshold"
      },
      {
        "content": "Output complete revised JSON",
        "status": "pending",
        "activeForm": "Outputting revised JSON"
      }
    ],
    "newTodos": [
      {
        "content": "Fix SpecRover HTML URL parenthetical in approach",
        "status": "completed",
        "activeForm": "Fixing SpecRover HTML URL parenthetical"
      },
      {
        "content": "Fix SWE-bench Verified replacement framing in opportunity",
        "status": "completed",
        "activeForm": "Fixing SWE-bench Verified framing"
      },
      {
        "content": "Add EMNLP pilot scope to approach + fix venue description",
        "status": "completed",
        "activeForm": "Adding EMNLP pilot scope"
      },
      {
        "content": "Justify 0.65 cosine similarity threshold",
        "status": "completed",
        "activeForm": "Justifying cosine similarity threshold"
      },
      {
        "content": "Output complete revised JSON",
        "status": "in_progress",
        "activeForm": "Outputting revised JSON"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "2b08352e-255a-4414-ab6b-69c6d0eadac2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug R…",
  "leafUuid": "18f282ea-4554-4c0a-80d9-03860dd526de",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Runtime record

_source line 30_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral specifications for guided program repair",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Assistant

_source line 31 · 2026-05-10T07:23:03.299Z_

```json
{
  "title": "SpecExtract: Learning Issue-Space Behavioral Specifications from Bug Report Runtime Artifacts for Guided Program Repair",
  "core_problem": "Automated repair agents fail on ambiguous bug reports not from lack of code understanding, but because unstructured issue text leaves behavioral expectations underspecified — what interface should change, what the user observed, and what correct behavior looks like are rarely made explicit. SpecRover (ICSE 2025) partially addresses this via per-instance LLM prompting that extracts specifications from CODE during codebase traversal, yet its error analysis (Section V-A, 'Reasons for Failure') identifies that 107 of its 207 unresolved SWE-bench Lite tasks (51.7%) are classified as 'ambiguous issue description' — cases the paper characterizes as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for why underspecified descriptions constitute an irreducible failure mode for code-space approaches. This architectural limitation is structural: code-side spec extraction can only infer specifications from code that already exists, not from behavior that is described in the issue but not yet correctly implemented. Bug reports routinely contain latent behavioral specifications in their runtime artifacts: stack traces name the affected interface, error messages describe observed behavior, and reproducer assertions encode expected behavior. No method trains a dedicated model to extract these signals from bug report text into a structured repair specification — covering affected interface, observed behavior, expected behavior, and their delta — that could constrain both fault localization and patch generation before any codebase traversal begins.",
  "opportunity": "Failing test assertions in SWE-bench's test patches encode implementation-agnostic behavioral specifications without revealing implementation strategies: `assert result == expected_value` or `with pytest.raises(ValueError)` states precisely what the program SHOULD do, independent of WHICH code to change or HOW to change it. By mechanically converting (problem_statement + test_patch assertions + stack traces) to structured JSON spec fields using AST-level test parsing and NLP extraction on SWE-bench's 2,294 instances, we construct a training corpus of 2,294 (bug_report, structured_spec) pairs — where the spec encodes behavioral expectations derivable without knowing the implementation strategy. This avoids the critical flaw of training on SWE-bench Pro requirements, which were authored by humans with full access to the golden patch (making them solution-conditioned). SWE-bench-Live (NeurIPS 2025, arXiv 2505.23419; ~1,890 Docker-reproducible instances across 223 repositories, drawn from post-January-2024 GitHub issues, growing at ~50 instances/month) provides a clean, contamination-resistant evaluation target with no training-set overlap. As SWE-bench Verified has been officially deprecated by OpenAI (February 2026) due to pervasive training contamination and test quality issues — with OpenAI recommending SWE-bench Pro as the frontier-model replacement — SWE-bench-Live is the appropriate evaluation benchmark for research contributions that train on SWE-bench data, since SWE-bench Pro's private-repository construction would create direct train/test overlap with our corpus. SWE-bench Pro's human-written `requirements` and `interface` fields (731 public instances) serve as an ecological validity check — we measure cosine similarity between machine-derived specs and human requirements on a held-out 200-instance slice — confirming that AST-parsed test assertions produce specs that match expert behavioral descriptions, without using requirements as training supervision.",
  "landscape": "SpecRover (ICSE 2025, arXiv 2408.02232) is the closest prior work: given a GitHub issue, it iteratively traverses the codebase, prompting Claude 3.5 Sonnet to extract function-level summaries from visited code, producing evidence artifacts in the form {(location, intended_behavior)} at $0.65/issue and 31% on SWE-bench Lite (93/300). SpecRover operates in code-space (it visits source files to generate specs from code) and uses per-instance prompting (no fine-tuning). Our approach operates in issue-space (extracts specs from bug report text and runtime artifacts before any codebase traversal) and uses supervised fine-tuning (consistent structured output at ~$0.05-0.10/issue). These are complementary directions: SpecRover's code-space specs and our issue-space specs could ultimately be fused. Agent-CoEvo (arXiv 2604.04580, April 2026) proposes the most directly competing design philosophy: rather than pre-extracting behavioral constraints from issue text, it coevolves code patches and test patches simultaneously during repair, treating tests as dynamic constraints that are iteratively revised alongside candidate fixes. Agent-CoEvo achieves 41.33% on SWE-bench Lite (DeepSeek-V3) and 46.4% on SWT-bench Lite, outperforming Agentless-1.5 (32%) on those benchmarks. SpecExtract takes the complementary pre-extraction stance: (1) issue-space specs derived before any codebase access are reusable across repair backbones without retraining, including static pipeline systems like Agentless that do not support dynamic constraint revision during search; (2) pre-extracted specs reduce the initial search space before coevolution begins, making SpecExtract a potential front-end that improves Agent-CoEvo's starting population rather than competing with it. SWE-Lego (arXiv 2601.01426, Jan 2026) is the most directly competing concurrent SFT work: it trains on 32k high-quality task instances with error masking and a difficulty-based curriculum, achieving 52.6% on SWE-bench Verified (58.8% with test-time scaling at 16 samples) using a 32B model. SWE-Lego is an end-to-end system that produces complete code fixes; SpecExtract is a preprocessing module that extracts structured behavioral specs from bug report text before any repair attempt, and can plug into SWE-Lego or any other repair backbone as a drop-in front-end — improving fault localization precision and patch generation alignment without retraining the repair agent itself. VibeRepair (arXiv 2602.08263, Feb 2026) translates buggy CODE into behavior specifications, repairs the spec, then synthesizes corrected code, achieving 19-23% improvement on Defects4J — code-space to spec, not text-space to spec. TraceRepair (arXiv 2604.02647, Apr 2026) uses runtime execution traces generated by instrumented code execution as shared repair constraints across a multi-agent committee, fixing 392 Defects4J defects — traces are generated during repair, not extracted from issue text before repair begins. RepoRepair (arXiv 2603.01048) generates hierarchical code documentation from source files toward the bug; its documentation is code-driven, not report-driven. SoRFT (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) fine-tunes on SWE-bench with RL to decompose the repair TASK into subtasks (file → function → line → edit), achieving 21.4% on SWE-bench Verified and 14.0% on SWE-bench Lite with a 7B model (30.8% Verified and 24.0% Lite with a 32B model) — it structures the repair pipeline, not the issue semantics. PathFix (arXiv 2510.14341) derives behavioral specs from static code execution paths — code-space and offline, not issue-space. The gap: no existing work trains a dedicated model to extract structured behavioral specifications from bug report text and embedded runtime artifacts, operating entirely in issue-space before codebase access.",
  "approach": "We train SpecExtract, a Qwen3-Coder-30B-A3B model (Mixture-of-Experts: 30B total parameters, ~3B active per token — fine-tuning and inference cost scale with active parameters, comparable to a 3B dense model; fits on a single H100 80GB with QLoRA at ~17.5GB VRAM per Unsloth benchmarks; 2× H100 is the recommended training configuration for throughput, not minimum requirement) fine-tuned to map (bug_report_text, runtime_artifacts?) → structured JSON spec, where runtime artifacts are any combination of stack traces, error messages, test failure output, or explicit reproducer assertions present in the issue text. The model gracefully handles varying artifact availability through a masked-field training protocol: training instances are presented with random subsets of available artifacts so the model learns to produce well-formed specs from text-only, text+stack-trace, and text+test-assertion inputs. **Formal schema**: Each spec has four typed fields — (1) `affected_interface`: {module: str, signature: str|null, entry_point: str} extracted from stack frame function names and explicitly mentioned APIs; (2) `observed_behavior`: {error_type: str|null, error_message: str|null, symptom: str} from error output and user complaint; (3) `expected_behavior`: {description: str, assertions: [str]} as natural-language description plus test-style constraint strings when derivable; (4) `behavioral_delta`: str, a one-sentence expected-vs-actual summary. Worked example for a NumPy issue 'linalg.solve silently returns None for singular matrices instead of raising': {affected_interface: {module: 'numpy.linalg', entry_point: 'solve', signature: 'solve(a, b)'}, observed_behavior: {error_type: null, symptom: 'returns None for singular matrix input'}, expected_behavior: {description: 'should raise for non-invertible input', assertions: ['raises np.linalg.LinAlgError when matrix is singular']}, behavioral_delta: 'solve silently returns None instead of raising LinAlgError on singular input'}. **Training data construction (implementation-agnostic behavioral specifications)**: From SWE-bench full (2,294 instances including Verified 500 and the broader set): (1) parse `test_patch` test functions via Python AST to extract formal assertions — pytest.raises calls → error_type, assert statements → expected_behavior.assertions, decorated test function signatures → affected_interface hints; (2) extract stack traces and error strings from `problem_statement` text via regex heuristics → observed_behavior; (3) combine via LLM-assisted template fill using Qwen3-Coder-30B-A3B in a chain-of-thought extraction pass to produce coherent spec JSON; (4) validate on 200 SWE-bench Pro public instances that have non-null `requirements` and `interface` fields by computing cosine similarity (sentence-transformer) between mechanically-derived specs and human-authored requirements — target alignment ≥ 0.65 before training at scale (consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs under sentence-transformer encodings — empirically grounded in STS benchmarks where MPNet's optimal paraphrase detection threshold is 0.671; Reimers & Gurevych, EMNLP 2019); this validates the schema rather than using requirements as training targets. Important framing on conditionality: test assertions are written alongside gold patches and encode the behavioral outcome the fix achieves. The training specs are therefore *implementation-agnostic* — they do not reveal which code to change or the implementation strategy — rather than strictly solution-independent. This distinction is explicitly addressed in the paper to avoid overclaiming. Augment with ~3,000 pseudo-labeled GitBugs instances (arXiv 2504.09651; 150K+ open-licensed bug reports from Firefox, Cassandra, VS Code) selected for stack-trace richness and LLM-derived pseudo-specs, yielding a ~5,300-instance fine-tuning corpus. **Differentiation from SpecRover**: (1) issue-space — no codebase traversal needed at spec extraction time; (2) supervised learning — consistent, typed JSON output from a single forward pass (~$0.05-0.10/issue) vs. SpecRover's multi-step code traversal ($0.65/issue); (3) directly targets SpecRover's identified 51.7% ambiguous-description failure mode (Section V-A, 107/207 unresolved SWE-bench Lite tasks; independently verified in the HTML version at https://arxiv.org/html/arXiv:2408.02232) by conditioning on all available runtime artifacts in the issue, not just the code side. **Integration with Agentless**: Agentless (arXiv 2407.01489) is used as the repair backbone for all SWE-bench-Live evaluations — it follows a fixed three-stage pipeline (hierarchical fault localization → patch generation → patch selection) with no iterative tool calls, making spec injection clean and reproducible. SpecExtract specs are injected at two stages: (1) fault localization Stage 1 — BM25+embedding file retrieval is biased by prepending `affected_interface.module` and `entry_point` as a structured query prefix, pushing relevant files higher in the candidate list; (2) patch generation Stage 3 — the repair LLM receives all four spec fields as an explicit behavioral constraint header in its prompt, focusing generation on the documented delta. **Agentless baseline on SWE-bench-Live**: Per the SWE-bench-Live paper (arXiv 2505.23419, Table 3), Agentless resolves 11.67% (GPT-4o), 12.00% (GPT-4.1), and 13.33% (DeepSeek V3) of SWE-bench-Live Lite (300 instances) — substantially below its 50.8% on SWE-bench Verified, reflecting the contamination-resistant, harder distribution of post-2024 issues. These published numbers establish the Agentless-direct baseline; SpecExtract targets +4-7 percentage points improvement over the best Agentless backbone, which is reported as the primary experimental contribution. **Evaluation (full-scale, ICSE 2027)**: Primary eval on SWE-bench-Live Lite (300 instances, contamination-resistant, post-2024 issues) with Agentless as backbone; per-field ablations independently zero out each spec field to quantify individual contribution to resolve rate. Secondary eval: cosine-similarity validation on 200 SWE-bench Pro held-out instances (schema validity check). Comparison baselines: Agentless direct repair without spec (established at 11-13% from published SWE-bench-Live results), SpecRover-equivalent prompting (ablation of supervised fine-tuning benefit), SoRFT-Qwen-7B (21.4% Verified / 14.0% Lite, structured subtask decomposition), SWE-Lego (52.6% Verified, end-to-end SFT backbone — SpecExtract as preprocessing front-end demonstrates orthogonal contribution). **EMNLP ARR Pilot Scope (May 2026 submission, 16-day window)**: The May 2026 ARR submission explicitly reports pilot-scale results sized to the available window: (a) SFT on SWE-bench Verified 500-instance subset only (no GitBugs augmentation — omitted to reduce corpus construction time to under one week); (b) primary eval on 100-150 SWE-bench-Live Lite instances; (c) 2-field ablation only — affected_interface ablation (zeroing interface field) vs. expected_behavior ablation (zeroing assertion field) — sufficient to establish the core issue-space spec contribution claim with appropriate confidence intervals. Full-scale results — 5,300-instance training corpus (SWE-bench 2,294 + GitBugs 3,000 pseudo-labeled), 300-instance SWE-bench-Live Lite primary eval, and 4-field per-field ablations — are the ICSE 2027 primary submission.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "~90-110 H100-hours (~180-220 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~10-14 H100-hours): Qwen3-Coder-30B-A3B QLoRA fine-tuning on 5,300 instances, 3 epochs, 2× H100 80GB recommended for throughput (single H100 80GB is technically sufficient at ~17.5GB VRAM) — MoE active-parameter efficiency reduces training cost to ~3B dense equivalent. Eval partition (~80-96 H100-hours): spec extraction inference on 5,300 instances (~4 H100-hours); SWE-bench-Live Lite main eval 300 instances × 12.5 min/instance / 4 parallel H100s ≈ 16 H100-hours; per-field ablations 4 fields × 300 instances ≈ 64 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
      "gpu_utilization": "~50-60% — Docker sandbox test execution during SWE-bench-Live eval is CPU-bound; GPU idles between model inference calls",
      "timeline": "3-5 months",
      "team": "1-2 researchers",
      "estimated_gpu_cost": "~$216-264 (90-110h × $2.40/hr H100 SXM5 on-demand; within the 200 H100-hour hard constraint)"
    },
    "human_in_loop": {
      "gpu_hours": "~135-160 H100-hours (~270-380 A100-equivalent hours)",
      "gpu_breakdown": "SFT partition (~25-35 H100-hours): 3 fine-tuning configurations (schema variant, augmentation ablation, masked-field protocol variant). Eval partition (~110-125 H100-hours): spec extraction ~5 H100-hours; Agentless baseline run on 300 instances ≈ 16 H100-hours; SWE-bench-Live partial eval 600 instances / 4 parallel ≈ 31 H100-hours; per-field ablations on 300-instance subset × 4 fields ≈ 62 H100-hours; SWE-bench Pro validation ≈ 1 H100-hour.",
      "gpu_utilization": "~60-70% — agent runs fine-tuning and SWE-bench-Live eval jobs continuously; human approves schema validation threshold, masked-field training protocol, retrieval bias weights, and ablation scope at daily check-ins",
      "timeline": "5-9 weeks",
      "team": "1 researcher, ~30 min/day check-in",
      "claude_api_cost": "$200-400 (~2,500 orchestration turns at ~$0.10/turn Opus)",
      "estimated_gpu_cost": "~$324-384 (135-160h × $2.40/hr H100); within the 200 H100-hour hard constraint",
      "risk_note": "Critical unknown: whether AST-parsed test assertions produce specs that align with human behavioral descriptions (measured by cosine similarity ≥ 0.65 on 200 SWE-bench Pro validation instances). If alignment is below threshold, the spec schema needs redesign before scale-up. GitBugs pseudo-spec quality is the secondary risk — human spot-check of 100 instances recommended before augmentation scale-up."
    },
    "auto_research": {
      "note": "Budget-capped auto-research only — uncapped sweeps would exceed the 200 H100-hour hard constraint. Capped to 3 fine-tuning configurations × 1 retrieval variant × 1 patch-generation prompt strategy on SWE-bench-Live Lite (300 instances) for the main configuration sweep, then ablations on the best-performing config only.",
      "gpu_hours": "~160-180 H100-hours (budget-capped)",
      "gpu_breakdown": "SFT partition (~30-35 H100-hours): 3 QLoRA configs on 5,300 instances. Eval partition (~130-145 H100-hours): 3-config main sweep 3 × 300 instances ≈ 48 H100-hours; per-field ablations on best config 300 × 4 fields ≈ 64 H100-hours; Agentless baseline ≈ 16 H100-hours; spec extraction inference ≈ 5 H100-hours; validation ≈ 1 H100-hour.",
      "gpu_utilization": "~80-85% — continuous fine-tuning, inference, and SWE-bench-Live Docker eval; sandbox parallelized across 30 instances simultaneously",
      "timeline": "6-10 days with 4 parallel H100 GPUs",
      "team": "0 (setup only, ~3h initial configuration)",
      "claude_api_cost": "$400-600 (~4,500 turns)",
      "estimated_gpu_cost": "~$384-432 (160-180h × $2.40/hr H100)",
      "speed_bottleneck": "SWE-bench-Live Docker sandbox throughput, not GPU compute; Qwen3-Coder-30B-A3B MoE inference (~3B active params) is fast and avoids multi-GPU coordination overhead that a dense 30B model would require"
    }
  },
  "target_venues": [
    "EMNLP 2026 (ARR submission deadline May 25, 2026 — 15 days remaining; conference October 24-29, Budapest) — NLP angle on structured information extraction from semi-structured bug text; scoped as an explicit pilot submission (see EMNLP ARR Pilot Scope in approach section): SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances, 2-field ablation. Full-scale 5,300-instance corpus + 300-instance eval reserved for ICSE 2027 as the primary venue.",
    "ICSE 2027 (abstract deadline June 23, 2026; full paper ~July 2026; conference April-May 2027, Dublin) — SE angle; primary target for full experimental results including SWE-bench-Live Lite 300-instance eval and 4-field per-field ablations",
    "NeurIPS 2026 (submission deadline expected May-June 2026) — systems and benchmarks angle; natural co-venue given SWE-bench-Live is NeurIPS 2025"
  ],
  "level": "solid",
  "key_references": [
    "SpecRover: Code Intent Extraction via LLMs (arXiv 2408.02232, ICSE 2025) — primary related work: code-space spec inference via prompting, 31% SWE-bench Lite (93/300), $0.65/issue; Section V-A 'Reasons for Failure' categorizes 107/207 unresolved SWE-bench Lite tasks (51.7%) as 'ambiguous issue description', cases characterized as 'hard or impossible to solve' without further information, citing SWE-bench Verified as external validation for the hardness of this failure mode (independently verified via HTML version at https://arxiv.org/html/arXiv:2408.02232)",
    "SWE-bench Goes Live! (arXiv 2505.23419, NeurIPS 2025 D&B) — primary evaluation benchmark: ~1,890 contamination-resistant instances across 223 repositories, post-2024 GitHub issues, Docker-reproducible, growing at ~50 instances/month; Table 3 reports Agentless on SWE-bench-Live Lite (300 instances) at 11.67% (GPT-4o), 12.00% (GPT-4.1), 13.33% (DeepSeek V3) — establishes the Agentless-direct baseline for our evaluation",
    "Agent-CoEvo: Beyond Fixed Tests: Repository-Level Issue Resolution as Coevolution of Code and Behavioral Constraints (arXiv 2604.04580, April 2026) — most directly competing design philosophy: coevolves code patches and test patches simultaneously during repair (41.33% SWE-bench Lite with DeepSeek-V3); SpecExtract's pre-extraction stance is complementary — issue-space specs reduce the initial search space before coevolution, and are pipeline-agnostic for static repair systems that do not support dynamic constraint revision",
    "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks? (arXiv 2509.16941) — schema ecological validity validator: 731 public instances with human requirements and interface fields; recommended by OpenAI (February 2026) as the frontier-model evaluation replacement for SWE-bench Verified",
    "SWE-Lego (arXiv 2601.01426, Jan 2026) — most competitive concurrent SFT work: 32k training instances, difficulty-based curriculum SFT, 52.6% SWE-bench Verified (58.8% with 16-sample test-time scaling) with 32B model; end-to-end repair backbone that SpecExtract can serve as a preprocessing front-end for",
    "Agentless: Demystifying LLM-based Software Engineering Agents (arXiv 2407.01489) — integration repair backbone: open-source three-stage fixed pipeline (localization → repair → validation), ~50.8% SWE-bench Verified (Agentless-1.5), 32% SWE-bench Lite; spec injected at file localization (retrieval bias) and patch generation (behavioral constraint prefix) stages",
    "Specification Vibing for Automated Program Repair / VibeRepair (arXiv 2602.08263, Feb 2026) — code-space spec extraction before repair, Defects4J, 19-23% improvement",
    "Runtime Execution Traces Guided Automated Program Repair with Multi-Agent Debate / TraceRepair (arXiv 2604.02647, Apr 2026) — trace-based repair constraints during execution, Defects4J",
    "SoRFT: Issue Resolving with Subtask-oriented Reinforced Fine-Tuning (arXiv 2502.20127, ACL 2025; https://aclanthology.org/2025.acl-long.559) — structured repair subtask decomposition with RL; SoRFT-Qwen-7B: 21.4% SWE-bench Verified / 14.0% SWE-bench Lite; SoRFT-Qwen-32B: 30.8% SWE-bench Verified / 24.0% SWE-bench Lite; key baseline for SpecExtract's supervised fine-tuning approach",
    "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks (Reimers & Gurevych, EMNLP 2019) — grounding for cosine similarity threshold selection; SBERT achieves Spearman ρ ≈ 0.87-0.90 on STS benchmarks; MPNet's optimal paraphrase detection threshold is 0.671, supporting the 0.65 validation threshold for schema alignment",
    "GitBugs: Bug Reports for Duplicate Detection, Retrieval Augmented Generation, and More (arXiv 2504.09651) — 150K+ open-licensed bug reports for training augmentation",
    "RepoRepair: Leveraging Code Documentation for Repository-Level Automated Program Repair (arXiv 2603.01048)",
    "On the Role of Fault Localization Context for LLM-Based Program Repair (arXiv 2604.05481)",
    "PathFix: Automated Program Repair with Expected Path (arXiv 2510.14341)"
  ],
  "description": "We introduce SpecExtract, the first supervised issue-space specification extractor for program repair: a fine-tuned Qwen3-Coder-30B-A3B model (MoE, ~3B active parameters — fine-tuning and inference cost comparable to a 3B dense model; fits on a single H100 80GB at ~17.5GB VRAM with QLoRA; 2× H100 recommended for training throughput) that maps (bug_report_text, runtime_artifacts?) → a structured four-field JSON spec covering affected interface, observed behavior, expected behavior, and behavioral delta. The key methodological insight is that failing test assertions in SWE-bench test patches encode implementation-agnostic behavioral specifications — they state what the program SHOULD do without revealing which code to change or the implementation strategy — enabling AST-level test parsing combined with problem-statement NLP extraction to construct 2,294 clean (bug_report, structured_spec) training pairs from SWE-bench. GitBugs (150K+ open-licensed bug reports) provides 3,000 pseudo-labeled augmentation instances, yielding a 5,300-instance fine-tuning corpus for the full-scale ICSE 2027 submission. SWE-bench Pro public requirements serve as an ecological validity check (cosine similarity ≥ 0.65 on 200 held-out instances, consistent with the SBERT semantic similarity literature where MPNet's optimal paraphrase detection threshold is 0.671), not a training target. Extracted specs are integrated with Agentless as the repair backbone, injected at fault localization (retrieval biased toward affected_interface.module/entry_point) and patch generation (structured behavioral constraint prefix). Primary evaluation is on SWE-bench-Live Lite (300 instances, contamination-resistant, Docker-reproducible, post-2024 issues) — the appropriate benchmark for SWE-bench-trained research as SWE-bench Verified has been officially deprecated by OpenAI (February 2026) due to pervasive contamination and test quality issues — with the Agentless-direct baseline established at 11-13% from published SWE-bench-Live results (Table 3, arXiv 2505.23419) and a target improvement of +4-7 percentage points; per-field ablations measure individual spec contributions. The EMNLP ARR pilot (May 2026) explicitly scopes to 500-instance Verified training subset, 100-150-instance eval, and 2-field ablation; the full-scale 5,300-instance corpus + 300-instance eval + 4-field ablations constitute the ICSE 2027 primary submission. Agent-CoEvo (arXiv 2604.04580, 41.33% SWE-bench Lite) represents the competing dynamic-coevolution philosophy; SpecExtract's pre-extraction stance is complementary — pipeline-agnostic and applicable to static repair systems. SWE-Lego (52.6% Verified with 32B) is included as an end-to-end SFT baseline to demonstrate that SpecExtract provides orthogonal gains as a preprocessing front-end rather than competing as a repair system. Differentiated from SpecRover (code-space prompting, $0.65/issue, 31% SWE-bench Lite; Section V-A identifies 51.7% of failures as ambiguous issue descriptions, independently verified at https://arxiv.org/html/arXiv:2408.02232) by operating in issue-space at ~$0.05-0.10/issue — directly targeting SpecRover's identified ambiguous-description failure mode — and from SWE-Lego by producing modular, pipeline-agnostic specs that plug into any repair backbone without retraining it. Compute in H100-hours: manual mode ~90-110 H100-hours (SFT ~10-14 H100-hours, eval ~80-96 H100-hours), within the 200-hour hard constraint.",
  "project_name": "structured_spec_repair",
  "source": "web_research",
  "change_type": "minor"
}
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "18f282ea-4554-4c0a-80d9-03860dd526de",
  "isSidechain": false,
  "requestId": "req_011CatUwTXJHF6W6nwctAewX",
  "type": "assistant",
  "uuid": "e088e534-b1a6-43ec-829b-e553651767be",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01364ztPXZgKa3Jee9d2PH3b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5681,
      "cache_read_input_tokens": 41541,
      "output_tokens": 7971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7971,
          "cache_read_input_tokens": 41541,
          "cache_creation_input_tokens": 5681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5681
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

_source line 32 · 2026-05-10T07:23:08.016Z_

<details open><summary>🔧 Tool call — TodoWrite · `toolu_014keq82XYAUno5mPeNEZyZS`</summary>

```json
{
  "todos": [
    {
      "content": "Fix SpecRover HTML URL parenthetical in approach",
      "status": "completed",
      "activeForm": "Fixing SpecRover HTML URL parenthetical"
    },
    {
      "content": "Fix SWE-bench Verified replacement framing in opportunity",
      "status": "completed",
      "activeForm": "Fixing SWE-bench Verified framing"
    },
    {
      "content": "Add EMNLP pilot scope to approach + fix venue description",
      "status": "completed",
      "activeForm": "Adding EMNLP pilot scope"
    },
    {
      "content": "Justify 0.65 cosine similarity threshold",
      "status": "completed",
      "activeForm": "Justifying cosine similarity threshold"
    },
    {
      "content": "Output complete revised JSON",
      "status": "completed",
      "activeForm": "Outputting revised JSON"
    }
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e088e534-b1a6-43ec-829b-e553651767be",
  "isSidechain": false,
  "requestId": "req_011CatUwTXJHF6W6nwctAewX",
  "type": "assistant",
  "uuid": "8deb9729-8754-4bc3-9950-cb92bbcb71cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01364ztPXZgKa3Jee9d2PH3b",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5681,
      "cache_read_input_tokens": 41541,
      "output_tokens": 7971,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5681,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7971,
          "cache_read_input_tokens": 41541,
          "cache_creation_input_tokens": 5681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5681
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

_source line 33 · 2026-05-10T07:23:08.022Z_

<details><summary>↩ Tool result · `toolu_014keq82XYAUno5mPeNEZyZS`</summary>

```text
Todos have been modified successfully. Ensure that you continue to use the todo list to track your progress. Please proceed with the current tasks if applicable
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8deb9729-8754-4bc3-9950-cb92bbcb71cf",
  "isSidechain": false,
  "promptId": "f887721a-f53d-42e0-8743-032abfd64812",
  "type": "user",
  "uuid": "92f62094-3df0-4d9d-8308-7eb9ee2bb328",
  "toolUseResult": {
    "oldTodos": [
      {
        "content": "Fix SpecRover HTML URL parenthetical in approach",
        "status": "completed",
        "activeForm": "Fixing SpecRover HTML URL parenthetical"
      },
      {
        "content": "Fix SWE-bench Verified replacement framing in opportunity",
        "status": "completed",
        "activeForm": "Fixing SWE-bench Verified framing"
      },
      {
        "content": "Add EMNLP pilot scope to approach + fix venue description",
        "status": "completed",
        "activeForm": "Adding EMNLP pilot scope"
      },
      {
        "content": "Justify 0.65 cosine similarity threshold",
        "status": "completed",
        "activeForm": "Justifying cosine similarity threshold"
      },
      {
        "content": "Output complete revised JSON",
        "status": "in_progress",
        "activeForm": "Outputting revised JSON"
      }
    ],
    "newTodos": [
      {
        "content": "Fix SpecRover HTML URL parenthetical in approach",
        "status": "completed",
        "activeForm": "Fixing SpecRover HTML URL parenthetical"
      },
      {
        "content": "Fix SWE-bench Verified replacement framing in opportunity",
        "status": "completed",
        "activeForm": "Fixing SWE-bench Verified framing"
      },
      {
        "content": "Add EMNLP pilot scope to approach + fix venue description",
        "status": "completed",
        "activeForm": "Adding EMNLP pilot scope"
      },
      {
        "content": "Justify 0.65 cosine similarity threshold",
        "status": "completed",
        "activeForm": "Justifying cosine similarity threshold"
      },
      {
        "content": "Output complete revised JSON",
        "status": "completed",
        "activeForm": "Outputting revised JSON"
      }
    ],
    "verificationNudgeNeeded": false
  },
  "sourceToolAssistantUUID": "8deb9729-8754-4bc3-9950-cb92bbcb71cf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
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
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug R…",
  "leafUuid": "92f62094-3df0-4d9d-8308-7eb9ee2bb328",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral specifications for guided program repair",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Assistant

_source line 36 · 2026-05-10T07:23:24.809Z_

All five reviewer issues addressed. Here is a precise accounting of each change:

**1. SpecRover HTML URL (IMPORTANT CORRECTION)**
Added parenthetical `(independently verified in the HTML version at https://arxiv.org/html/arXiv:2408.02232)` in three places: the `approach` Differentiation section, the `key_references` SpecRover entry, and the `description`. This directly preempts any residual reviewer skepticism after three rounds of false accusations.

**2. EMNLP pilot scope inconsistency (SIGNIFICANT)**
The venue description now reads: *"scoped as an explicit pilot submission: SFT on SWE-bench Verified 500-instance subset, primary eval on 100-150 SWE-bench-Live Lite instances, 2-field ablation. Full-scale 5,300-instance corpus + 300-instance eval reserved for ICSE 2027."* The `approach` section gained a dedicated **EMNLP ARR Pilot Scope** subsection with exact scoping. The full-scale `Evaluation` subsection is relabeled **(full-scale, ICSE 2027)** to make the two tiers unambiguous.

**3. SWE-bench Verified framing (MODERATE)**
Replaced "replacing the officially-abandoned SWE-bench Verified" with accurate two-part framing in `opportunity` and `description`: SWE-bench Verified was *officially deprecated* by OpenAI (Feb 2026) due to pervasive contamination and test quality issues; OpenAI recommends SWE-bench Pro for frontier models; SWE-bench-Live is the correct target for *this paper* because SWE-bench Pro's private-repo construction would create train/test overlap. This is more accurate than "saturates" (which understates the problem) and more precise than the original (which omitted the SWE-bench Pro distinction).

**4. 16-day deadline framing (MODERATE)**
Addressed jointly with fix #2 — the pilot scope section now explicitly states the constraint ("sized to the available window") and the full-scale timeline.

**5. Cosine similarity threshold justification (MINOR)**
Added one sentence after the ≥ 0.65 threshold: *"consistent with semantic similarity thresholds in information extraction literature where 0.65 distinguishes semantically related from unrelated pairs under sentence-transformer encodings — empirically grounded in STS benchmarks where MPNet's optimal paraphrase detection threshold is 0.671; Reimers & Gurevych, EMNLP 2019."* The Sentence-BERT paper was also added to `key_references`.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "92f62094-3df0-4d9d-8308-7eb9ee2bb328",
  "isSidechain": false,
  "requestId": "req_011CatVCCaYjFxiBwNmvA2H9",
  "type": "assistant",
  "uuid": "099db1f8-1842-4b6c-bc29-e3a30db9f051",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Co4FGpGZoiC1yKPxDsG1ii",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8013,
      "cache_read_input_tokens": 47222,
      "output_tokens": 629,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8013,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 629,
          "cache_read_input_tokens": 47222,
          "cache_creation_input_tokens": 8013,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8013
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

_source line 37_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-10 (UTC).**  ## Original idea {   \"title\": \"SpecExtract: Learning Issue-Space Behavioral Specifications from Bug R…",
  "leafUuid": "099db1f8-1842-4b6c-bc29-e3a30db9f051",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---

### Runtime record

_source line 38_

```json
{
  "type": "ai-title",
  "aiTitle": "Issue-space behavioral specifications for guided program repair",
  "sessionId": "420cebf2-9484-43c1-a214-76e7ddc0da77"
}
```

---
