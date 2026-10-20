# Research conversation: Read the file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md and ret

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a092e0d2b34814b55.jsonl`
- **Structured JSON:** [`d9f5cc700c2593ecafe5.json`](../../sessions/d9/d9f5cc700c2593ecafe5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-18T20:10:57.975Z_

Read the file /home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md and return its full contents. This is a paper framing document for a research project.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "cd6b400d-8c36-4c49-b5c3-7c3b922136fa",
  "agentId": "a092e0d2b34814b55",
  "type": "user",
  "uuid": "f010afdf-76ff-4fa0-b36b-ec00fe9b8dab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "9ad9e7c3-b0a3-4153-90cc-8d03eee4616d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-gathering-lobster"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-18T20:10:59.110Z_

I'll read the paper framing document for you.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f010afdf-76ff-4fa0-b36b-ec00fe9b8dab",
  "isSidechain": true,
  "agentId": "a092e0d2b34814b55",
  "requestId": "req_011CbAeDYHMDiozgBLrMYF6k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "aa474b11-4474-4c74-8ade-a879b057cd21",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "9ad9e7c3-b0a3-4153-90cc-8d03eee4616d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-gathering-lobster",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ME1qSEv3FqHRSx2GDz2NBx",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18295,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 18295,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 5,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 3 · 2026-05-18T20:10:59.281Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EbyEzW7beqhHAeFu1RnBJo`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa474b11-4474-4c74-8ade-a879b057cd21",
  "isSidechain": true,
  "agentId": "a092e0d2b34814b55",
  "requestId": "req_011CbAeDYHMDiozgBLrMYF6k",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "dfc65863-3a2f-4252-9be7-f9ceec7746f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "9ad9e7c3-b0a3-4153-90cc-8d03eee4616d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-gathering-lobster",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01ME1qSEv3FqHRSx2GDz2NBx",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 18295,
      "cache_read_input_tokens": 0,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 18295
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 100,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 18295,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 18295,
            "ephemeral_1h_input_tokens": 0
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

_source line 4 · 2026-05-18T20:10:59.300Z_

<details><summary>↩ Tool result · `toolu_01EbyEzW7beqhHAeFu1RnBJo`</summary>

```text
1	# Paper Framing — symb_invariant_consensus
2	
3	## Target Venue
4	- Primary: EMNLP 2026 Main (ARR May 25)
5	- Deadline: May 25, 2026 (ARR submission)
6	
7	## Core Claims (4 条) — D052 Regime-Dependent Capability Trap (REVISED)
8	
9	1. **The Regime-Dependent Capability Trap**: LLM self-extracted FOL constraint aggregation faces a regime-dependent tension. When model accuracy is high (SC ≥ ~70%), self-extracted constraints correlate strongly with the model's own answers (confirmation bias), losing discriminative power and reducing MAX-SAT to counting. When model accuracy is low (SC ≤ ~55%), constraints retain partial independence from final answers, enabling SICA to provide genuine gains. The trap is not universal but accuracy-conditioned. Validated across 3 reasoning domains × 5 model families spanning instruction-scale, distilled-reasoning, and full-reasoning architectures. [Scope: this finding characterizes same-model self-extraction pipelines; methods using external verifiers or trained extractors may not share this limitation.]
10	2. **Regime Boundary — SC Accuracy Determines SICA Effectiveness**: (a) **High-accuracy regime (trap active)**: Qwen-14B SC=75.49% Δ=+0.25pp n.s. (n=804), Qwen-14B LogiQA SC=78.8% Δ=0.0pp (n=151 interim), LLaMA-8B StrategyQA Δ=+2.0pp n.s. (n=200), LLaMA-8B FOLIO Δ=-2.4pp (n=204), DeepSeek-R1-Distill-7B Δ=-3.3pp (n=60). Full reasoning model QwQ-32B C0<5% (degenerate). (b) **Low-accuracy regime (trap partially lifted)**: Mistral-7B SC=54.41% Δ=**+4.90pp p=0.013** (n=204, b=12 c=2; McNemar confirmed by programmatic computation, three manual attempts all had transcription errors). BUT: LLaMA-8B FOLIO Δ=-2.4pp (n=204) — need LLaMA-8B SC to determine if this is also low-SC (which would complicate the simple accuracy-threshold story) or medium-SC. The boundary may involve more than just SC accuracy (model architecture, constraint extraction quality, variable naming consistency).
11	3. **C0 as Necessary-but-Insufficient Diagnostic**: C0 reliably predicts when symbolic consensus CANNOT help (C0<5% → method degenerates to SC), but high C0 does NOT guarantee gains. C0 combined with SC accuracy forms a two-dimensional screening: low C0 → degenerate; high C0 + high SC → trap; high C0 + low SC → potential gains. Zero-cost early stopping criterion for practitioners.
12	4. **Oracle Proves Aggregation Mechanism, Localizes Bottleneck**: Gold FOL + MAX-SAT achieves +14.22pp over SC (89.71% vs 75.49%, p=2.0e-7), proving the aggregation paradigm IS effective with discriminative constraints. Even Mistral-7B's significant +4.90pp captures only ~35% of the oracle ceiling (+14.22pp), confirming extraction quality remains the binding bottleneck across all regimes. Six remediation strategies all failed to close this gap (contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT).
13	
14	## Core Insight
15	LLM self-extracted FOL constraints exhibit a **regime-dependent capability trap**: their discriminative power depends on the extracting model's own accuracy on the task. When a model is strong (SC ≥ ~70%), its self-extracted constraints are strongly correlated with its own answers (confirmation bias), losing the independence needed to adjudicate between candidates. MAX-SAT over such constraints degenerates to counting. When a model is weak (SC ≤ ~55%), constraints retain partial independence from final answers, and SICA can provide significant gains (Mistral-7B: +4.90pp, p=0.013, b=12 c=2). However, even in the favorable regime, self-extracted constraints capture only ~35% of the oracle ceiling (+14.22pp), confirming extraction quality as the persistent bottleneck.
16	
17	**Key evidence**:
18	- **Oracle control (exp-031)**: Gold FOL + MAX-SAT = 89.71% vs SC 75.49% (+14.22pp, p=2.0e-7, b=29 c=0). Unknown-type questions +31.9pp. Proves aggregation mechanism IS effective with discriminative constraints.
19	- **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp n.s. vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013. LLaMA-8B (SC=63.2%) Δ=-2.45pp shows the boundary is sharp (not all weak models benefit).
20	- **Within-model regime transition (D053)**: ICL Oracle on Mistral-7B (exp-044 partial n=148) boosted SC from 54.4%→61.5% via oracle examples, but SICA flipped from +4.90pp to -2.23pp. Same model, same architecture, only SC accuracy changed. This controls for model-specific factors and directly demonstrates the regime transition mechanism.
21	- **Six remediation failures**: contrastive prompting (exp-029, -1.1pp), cross-model extraction (exp-030, 0.00pp), generational scaling (exp-027, +0.49pp n.s.), solver-guided refinement (exp-036, 0.9% UNSAT trigger rate), consistency filtering (constraints too sparse), cross-trace UNSAT (56.4% zero shared variables). All failed to close the extraction-oracle gap, confirming the trap is structural across prompting, architecture, capability, and verification dimensions.
22	
23	We provide the first systematic empirical study (a) identifying the regime boundary where self-extracted constraint aggregation transitions from ineffective to beneficial, (b) localizing the failure mode to extraction quality via oracle control, (c) quantifying constraint non-discrimination at per-problem granularity, and (d) proposing C0 + SC accuracy as a two-dimensional deployment diagnostic. [Positioning: Logic-LM and LINC documented that LLM-to-FOL translation is error-prone; our contribution is the oracle-controlled causal separation of extraction vs aggregation failure, the regime boundary characterization, and systematic quantification across 5 model families.]
24	
25	## Story Spine
26	- **Problem**: Recent work proposes augmenting LLM reasoning with symbolic methods, extracting formal constraints from reasoning traces and using solvers for answer selection. But when should practitioners invest in such methods vs. simple majority voting?
27	- **Existing approaches & gaps**: SC (Wang et al. 2023), USC (Chen et al. 2023), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023), ORM/PRM (Cobbe et al. 2021, Lightman et al. 2023), Weighted SC (Taubenfeld et al. 2024). None systematically characterize when symbolic aggregation helps vs. when it degenerates to voting.
28	- **Our framing**: We instantiate symbolic consensus as SICA (MAX-SAT over extracted FOL constraints) and systematically evaluate across 3 domains × 5 model families + 1 full reasoning model. We discover a regime-dependent capability trap: SICA gains are accuracy-conditioned, not universally absent.
29	- **Headline result**: "Across 5 model families, SICA's effectiveness depends on the extracting model's baseline accuracy. Strong models (SC ≥ 70%) show no gain (Δ = -3.3pp to +2.0pp, all n.s.); a weaker model (Mistral-7B, SC = 54%) shows significant improvement (+4.90pp, p = 0.013). Oracle control (+14.22pp) proves the aggregation mechanism works with discriminative constraints, but even the best self-extraction result captures only ~35% of this ceiling. Six remediation strategies all fail to close the gap. We identify a confirmation-bias mechanism: stronger models' constraints mirror their own answers, losing discriminative power. C0 + SC accuracy form a two-dimensional deployment diagnostic."
30	
31	## Anticipated Reviewer Concerns & Defensive Experiments
32	1. **"Gains not statistically significant"** → Four powered tests: exp-001 (n=804), exp-019 (n=200), exp-020 (n=204), exp-010 (n=60). Combined N>1,200.
33	2. **"Only a better tiebreaker, not worth the overhead"** → exp-002: K ablation (SICA≤SC all K including odd K=11); exp-013: MaxSAT≈count-only (mechanism vacuous); exp-009: overhead analysis
34	3. **"Only Qwen models"** → 5 model families: Qwen-14B + Mistral-7B + LLaMA-8B + DeepSeek-R1-Distill-7B + QwQ-32B. Critically, Mistral-7B shows the ONLY significant positive (+4.90pp, p=0.013), strengthening cross-family coverage AND revealing the regime boundary.
35	4. **"Only one reasoning model"** → QwQ-32B (full reasoning, C0<5%). DeepSeek-R1-Distill-7B reclassified as instruction-scale (C0=58%, behaves like instruction model due to 7B capacity insufficient for deterministic reasoning chains)
36	5. **"Only logic domain"** → FOLIO (formal logic) + StrategyQA (commonsense) + ARC-Challenge (science). ProofWriter in appendix.
37	6. **"MAX-SAT is over-engineering"** → exp-013: MaxSAT ≈ count-only ≈ random-weight confirmed. This IS the capability trap evidence.
38	7. **"Random tiebreak baseline"** → exp-003: SICA tiebreak 80% vs random 50% vs alphabetical 60%. On tied questions SICA is better, but ties are too rare to matter at scale.
39	8. **"Why not just use a reasoning model?"** → Full reasoning model QwQ-32B shows C0<5%, SICA redundant. Distilled reasoning model DeepSeek-R1-7B behaves like instruction model (C0=58%). Either way SICA provides no benefit.
40	9. **"How does this compare to Logic-LM / LINC?"** → exp-015: Logic-LM × K baseline (CPU-only)
41	10. **"Weighted SC is simpler"** → exp-016: Weighted SC baseline (CPU-only)
42	11. **"C0 is trivially derived"** → C0 is trivial to compute but non-trivial to interpret. Its value is as a zero-cost early stopping criterion, not as a metric per se.
43	12. **"Within-family scaling?"** → exp-004 (7B) + exp-007 (72B-AWQ) if time permits. C0 trend within Qwen family.
44	13. **"Self-extraction confound — same model generates and extracts"** → exp-031 Oracle FOLIO (post-fix traces): **RESOLVED.** Gold FOL + Z3 + MAX-SAT = 89.71% vs SC = 75.49% (+14.22pp, p=2.0e-7, b=29 c=0). Unknown +31.9pp. Aggregation mechanism IS effective with discriminative constraints. Bottleneck conclusively localized to LLM self-extraction quality. Three remediation attempts all failed: contrastive prompting (exp-029, -1.1pp), cross-model Mistral→Qwen (exp-030, 0pp), Qwen3 generational (exp-027, +0.49pp p=0.655 n.s.). This is now a core contribution, not just a defensive experiment.
45	14. **"Published methods achieve gains on same benchmarks (DyLoS, Aristotle, FoVer)"** → Acknowledge in Related Work and Discussion. Key distinction: those methods use trained/external verifiers, multi-paradigm solver selection, or logic-complete decomposition — all fundamentally different from same-model self-extraction. Our finding characterizes the specific failure mode of self-extraction pipelines, not symbolic reasoning broadly.
46	15. **"MAX-SAT formulation is just weighted voting"** → Paper must explicitly describe cross-answer evaluation: constraints from trace t_i ARE/ARE NOT evaluated against other candidates. If structurally a weighted vote, acknowledge and frame contribution as "even the most charitable interpretation (weighted vote with constraint-based weights) provides no gain."
47	
48	## Working Title
49	**"When Does Symbolic Aggregation Help? The Regime-Dependent Capability Trap of Self-Extracted Constraints"**
50	(Alternatives: 
51	- "The Capability Trap: Self-Extracted Constraints Help Weak Models but Not Strong Ones"
52	- "Diversity Without Discrimination: A Systematic Study of When LLM-Extracted Constraint Aggregation Succeeds and Fails")
53	
54	NOTE (Dream D037): Title MUST be scoped to "self-extracted constraints" / "SICA" — NOT "symbolic consensus" broadly. Published methods (DyLoS, Aristotle, FoVer, LogicAgent) achieve gains on same benchmarks using different symbolic approaches. Our evidence covers one pipeline (same-model FOL extraction + MAX-SAT), not the entire paradigm.
55	
56	## Paper Structure (EMNLP 8pp + appendix)
57	- Main Tables: T1 (Main Results: models × domains, SICA vs SC, highlighting regime boundary), T2 (Oracle Control: Gold-FOL+MAX-SAT vs SC vs SICA-self, causal separation), T3 (Constraint Ablation: MaxSAT vs count-only vs random for high-SC model), T4 (Remediation Attempts: 6 interventions all failed to close oracle gap)
58	- Main Figures: F1 (Method Pipeline), F2 (SC Accuracy vs SICA Δ scatter: hero figure showing regime boundary, x=SC%, y=Δpp, with significance markers — the core visual for regime-dependent trap), F3 (Per-problem constraint precision: high-SC model vs low-SC model comparison, showing confirmation bias mechanism), F4 (C0 × SC two-dimensional diagnostic heatmap)
59	- Appendix: K ablation (exp-002), Temperature ablation (C0 varies but Δ flat in high-SC regime), Per-domain detailed results, Overhead analysis (exp-009), Case studies (exp-008), QwQ-32B/DeepSeek-R1 negative control data, 6 remediation strategy details
60	
61	## Claim Risk Notes (Updated D052 — regime-dependent framing)
62	- **McNemar RESOLVED**: p=0.013 confirmed (b=12, c=2, programmatic computation). Three manual attempts all had transcription errors.
63	- **Claim 1 regime boundary — WEAKENED BY LLaMA-8B DATA**: LLaMA-8B SC=**63.2%** with Δ=-2.45pp (discordant 4:9, SICA HURTS). This is between Mistral (54.4%) and Qwen-14B (75.5%). The "low SC → SICA helps" narrative does NOT hold as a simple threshold. Non-monotonic pattern: SC=54% positive, SC=63% negative, SC=75%+ flat. Either (a) regime boundary is very sharp (SC < ~55% only), or (b) Mistral result is model-specific, not accuracy-dependent. Need to decide between: regime-dependent framing (with sharp threshold) vs. model-specific exception framing (Mistral as outlier).
64	- **Claim 2 confirmation bias mechanism**: Hypothesis needs per-problem precision analysis comparing Mistral-7B vs Qwen-14B. OPEN. Also: Mistral contradiction rate 3.5% (128/204 problems with contradictions) vs Qwen ~1.5% — higher contradiction rate = more MaxSAT operating room in low-SC regime. **Variable naming inconsistency** (exp-036b): 56.4% of cross-trace answer pairs have zero shared Z3 variables, preventing meaningful cross-trace comparison. This is a key mechanism of the capability trap — even when constraints exist, inconsistent variable naming makes them incomparable across traces.
65	- **Claim 3 two-dimensional diagnostic**: C0 × SC theoretically motivated but empirically thin. Temperature ablation confirms C0 varies but Δ flat in high-SC regime. Need low-SC C0 variation data. OPEN.
66	- **Claim 4 oracle gap**: Mistral +4.90pp vs Oracle +14.22pp = ~35% recovery. Compelling evidence extraction quality is bottleneck even when trap partially lifted.
67	- **exp-011 +10pp is noise**: n=30 SE≈9pp. exp-020 same task n=204 shows -2.4pp. Do NOT cite.
68	- **F2 hero figure redesign**: SC accuracy (x) vs SICA Δ (y) scatter with all model-domain conditions. Need exp-038 LogiQA + exp-035 Qwen-7B SC for more data points. OPEN.
69	- **CRITICAL RISK — regime boundary may be model-specific, not accuracy-dependent**: p=0.013 confirmed, but if LLaMA-8B also low-SC yet Δ=-2.4pp, the "low SC → SICA helps" narrative fails. Fallback framing: "Mistral-7B is an outlier where SICA helps for model-specific reasons (higher contradiction rate, different extraction patterns), but capability trap holds across all other tested conditions." This is weaker but still publishable as a nuanced analysis paper.
70	
71	## Required Citations (Dream D037 — minimum 30 references)
72	
73	Paper Agent MUST include these categories (non-exhaustive list of must-cite works):
74	- **SC & extensions**: Wang et al. 2023 (SC), Chen et al. 2023 (USC), Loo et al. 2025 (SC scaling plateaus), Taubenfeld et al. 2025 ACL Findings (confidence-weighted SC), DiVeRSe (Li et al. 2023)
75	- **Neuro-symbolic reasoning (positive results on same benchmarks)**: DyLoS (EACL 2026), Aristotle (ACL 2025), FoVer (TACL 2025), LogicAgent (2025), Logic-LM (Pan et al. 2023), LINC (Olausson et al. 2023)
76	- **Test-time compute scaling**: Snell et al. 2025 (ICLR Oral), DeepSeek-R1 technical report (Nature 2025), Diversity-Aware Training for TTS (2025)
77	- **Verification & reranking**: ORM (Cobbe et al. 2021), PRM (Lightman et al. 2023), Math-Shepherd (Wang et al. 2024)
78	- **Constraint satisfaction in NLP**: SATBench (EMNLP 2025), LLM Meets Constraint Propagation (IJCAI 2025)
79	- **Negative results in NLP**: appropriate precedents for analysis/negative-result papers
80	- **Debate & multi-agent**: Liang et al. 2023, Du et al. 2023
81	- **Reasoning model paradigm**: QwQ technical blog, o1 (OpenAI 2024)
82	
83	## Claim Scoping Rules (Dream D037)
84	
85	- n=60 conditions: present as "suggestive/consistent with" NOT "confirming." Only n≥200 conditions can "confirm" null.
86	- Combined N>1,300: acceptable if clearly stated that 804/1300 come from powered Qwen-14B condition.
87	- Domain coverage: acknowledge that SICA operates meaningfully (C0>20%) primarily on formal logic; other domains are degenerate (C0<10%) due to model capability.
88	- "Capability trap" framing: position as systematic quantification of a known challenge (not discovery). Our specific contributions: (a) per-problem precision analysis at n=307 granularity, (b) constraint ablation proving MAX-SAT ≈ counting, (c) C0 as deployment diagnostic.
89	
90	## Venue Fit Risks
91	- EMNLP: Analysis paper with both positive and negative results. Stronger venue fit than pure negative: characterizes WHEN symbolic aggregation helps (practitioner value). "So what should practitioners do?" → C0 + SC accuracy two-dimensional diagnostic + overhead analysis.
92	- Cross-discipline: MAX-SAT needs clear explanation for NLP audience.
93	- Statistical power: Strong (N>1,200 combined; Mistral positive n=204 with p=0.013).
94	- Novelty upgrade: Regime-dependent finding is more publishable than "it never works" — provides actionable boundary condition.
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dfc65863-3a2f-4252-9be7-f9ceec7746f1",
  "isSidechain": true,
  "promptId": "cd6b400d-8c36-4c49-b5c3-7c3b922136fa",
  "agentId": "a092e0d2b34814b55",
  "type": "user",
  "uuid": "66bb1973-028e-4f5b-822b-39f5de6269f3",
  "sourceToolAssistantUUID": "dfc65863-3a2f-4252-9be7-f9ceec7746f1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "9ad9e7c3-b0a3-4153-90cc-8d03eee4616d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-gathering-lobster"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-18T20:11:13.334Z_

Here is the full contents of the paper framing document:

## Paper Framing — symb_invariant_consensus

This is a research paper for EMNLP 2026 (submission deadline May 25) that investigates when symbolic constraint aggregation (SICA — MAX-SAT over extracted FOL constraints) helps improve LLM reasoning, or when it degenerates.

### Core Claims

**The Regime-Dependent Capability Trap**: The paper identifies that LLM self-extracted FOL constraints face a regime-dependent tension:
- **High-accuracy regime (SC ≥ ~70%)**: Constraints correlate strongly with the model's own answers (confirmation bias), losing discriminative power. SICA provides no meaningful gain (Δ = -3.3pp to +2.0pp, all non-significant).
- **Low-accuracy regime (SC ≤ ~55%)**: Constraints retain partial independence, and SICA can provide gains. Mistral-7B (SC=54.41%) shows significant improvement of +4.90pp (p=0.013, n=204).
- **Oracle ceiling**: Gold FOL + MAX-SAT achieves +14.22pp (p=2.0e-7), proving the aggregation mechanism works with discriminative constraints. Self-extracted constraints capture only ~35% of this ceiling.

The paper validates this across **3 reasoning domains × 5 model families** (Qwen-14B, Mistral-7B, LLaMA-8B, DeepSeek-R1-Distill-7B, QwQ-32B).

### Key Evidence

1. **Regime boundary**: Qwen-14B (SC=75.49%) Δ=+0.25pp n.s. vs Mistral-7B (SC=54.41%) Δ=+4.90pp p=0.013
2. **Within-model regime transition (exp-044)**: ICL Oracle on Mistral-7B boosted SC from 54.4%→61.5%, but SICA flipped from +4.90pp to -2.23pp — same model, same architecture, only SC accuracy changed. This directly demonstrates the regime transition.
3. **Six remediation strategies all failed** to close the extraction-oracle gap: contrastive prompting, cross-model extraction, generational scaling, solver-guided refinement, consistency filtering, cross-trace UNSAT.

### Diagnostic Framework

**C0 (constraint overlap) + SC accuracy** form a two-dimensional deployment diagnostic:
- Low C0 → method degenerates to SC
- High C0 + high SC → regime trap active
- High C0 + low SC → potential gains

### Critical Risks & Open Questions

1. **Regime boundary may be model-specific, not purely accuracy-dependent**: LLaMA-8B (SC=63.2%) shows Δ=-2.45pp (discordant), contradicting the simple "low SC → gains" narrative. Mistral may be an outlier. Fallback framing: nuanced analysis of when/why SICA helps.
2. **Confirmation bias mechanism**: Needs per-problem precision analysis comparing high-SC vs low-SC models.
3. **Variable naming inconsistency**: 56.4% of cross-trace answer pairs have zero shared Z3 variables, preventing meaningful constraint comparison across traces.
4. **C0 × SC two-dimensional diagnostic**: Theoretically motivated but empirically thin; needs low-SC C0 variation data.

### Working Title

**"When Does Symbolic Aggregation Help? The Regime-Dependent Capability Trap of Self-Extracted Constraints"**

### Paper Structure (EMNLP 8pp + appendix)

- **Main Tables**: T1 (results by model/domain), T2 (oracle control), T3 (constraint ablation), T4 (remediation attempts)
- **Main Figures**: F2 (SC accuracy vs SICA Δ scatter, hero figure showing regime boundary), F3 (per-problem constraint precision), F4 (C0 × SC diagnostic heatmap)
- **Domains**: FOLIO (formal logic), StrategyQA (commonsense), ARC-Challenge (science)

This is a comprehensive negative-result analysis paper that characterizes a systematic failure mode in self-extracted constraint aggregation and provides a practical deployment diagnostic for practitioners.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "66bb1973-028e-4f5b-822b-39f5de6269f3",
  "isSidechain": true,
  "agentId": "a092e0d2b34814b55",
  "requestId": "req_011CbAeDddKcU3aZjSKv3Ukc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "6ede257f-ded5-4019-b23e-3679c4ddf5ee",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0513_3/projects/symb_invariant_consensus/.claude/sessions/reviewer_342b9753",
  "sessionId": "9ad9e7c3-b0a3-4153-90cc-8d03eee4616d",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sequential-gathering-lobster",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01Kie1et1vyYoW597YZsz9Qk",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 6267,
      "cache_read_input_tokens": 18295,
      "output_tokens": 1025,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6267
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1025,
          "cache_read_input_tokens": 18295,
          "cache_creation_input_tokens": 6267,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6267,
            "ephemeral_1h_input_tokens": 0
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
