# Research conversation: Read /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md and extract: (1)

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 5
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-1/agent-a8379fcc020347a2e.jsonl`
- **Structured JSON:** [`e36f57d252b67f27c54e.json`](../../sessions/e3/e36f57d252b67f27c54e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

5 recorded events

### User

_source line 1 · 2026-05-19T20:28:12.220Z_

Read /home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md and extract: (1) the Core Claims (C1/C2/C3), (2) the listed Reviewer Concerns / preemptive defenses, (3) any "known weaknesses" or "attack surfaces" mentioned. Report concisely.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "c4d4f0db-2852-40ad-afac-040fa0e315f4",
  "agentId": "a8379fcc020347a2e",
  "type": "user",
  "uuid": "3d6fe27a-8743-4b80-bbb5-52178795ccc5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm"
}
```

</details>

---

### Assistant

_source line 2 · 2026-05-19T20:28:13.389Z_

I'll read the paper_framing.md file and extract the requested information.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d6fe27a-8743-4b80-bbb5-52178795ccc5",
  "isSidechain": true,
  "agentId": "a8379fcc020347a2e",
  "requestId": "req_011CbCZLgsebmhHwLhbpg1fc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "27a09a43-a22f-47cf-8523-9c5f0172c1d5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MkSAW1eUfeedSffU2UjrR3",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 18244,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 522,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 3,
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

_source line 3 · 2026-05-19T20:28:13.659Z_

<details open><summary>🔧 Tool call — Read · `toolu_01XqdnTEMZ4ugETTc3nqwz1e`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/paper_framing.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "27a09a43-a22f-47cf-8523-9c5f0172c1d5",
  "isSidechain": true,
  "agentId": "a8379fcc020347a2e",
  "requestId": "req_011CbCZLgsebmhHwLhbpg1fc",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "884ed247-b679-42fa-b4b2-0848de88be76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01MkSAW1eUfeedSffU2UjrR3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 522,
      "cache_read_input_tokens": 18244,
      "output_tokens": 106,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 522
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 106,
          "cache_read_input_tokens": 18244,
          "cache_creation_input_tokens": 522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 522,
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

_source line 4 · 2026-05-19T20:28:13.667Z_

<details><summary>↩ Tool result · `toolu_01XqdnTEMZ4ugETTc3nqwz1e`</summary>

```text
1	# Paper Framing — simgate-modular-routing
2	
3	## Target Venue
4	- **EMNLP 2026 Main Conference — Long Paper (8 pages + references)**
5	- Deadline: ARR May 25, 2026 (10 days remaining)
6	- D050: Upgraded from short paper (4p, Findings) per user directive
7	
8	## Core Insight
9	
10	**[D126 Framework-centric pivot]** We develop a **diagnostic framework** — episode-level counterfactual analysis — for understanding when and why deterministic computation helps LLM agents. Per-step oracle labeling degenerates to 97.4% ties in sparse-reward settings; our framework overcomes this by comparing complete episode outcomes under pure-internal and pure-deterministic strategies. Applied to ScienceWorld as a case study, the framework reveals that **death avoidance accounts for ~90% of routing signal** (78.9% of non-tie labels from death asymmetry [A]; DAF=90.41% at P=100 [A]; r=0.9698, p=8.12e-07 [A] across 11 task types / 245 episodes [A]; source: plan-012-full). The framework further diagnoses that routing is nearly unnecessary (oracle ≈ always-deterministic, 96.3% agreement [A]), turning the router negative result into a validated framework prediction rather than a limitation. The contribution is the reusable diagnostic methodology + the case study finding, not the router architecture itself.
11	
12	## Core Claims (3 claims for long paper) — [D126 reordered: framework-first]
13	
14	**C1 (Diagnostic framework: episode-level counterfactual analysis)**: Per-step oracle labeling degenerates in sparse-reward environments (97.4% tie rate on ScienceWorld). We propose episode-level counterfactual analysis — running complete episodes under pure-internal and pure-deterministic strategies — as a **reusable diagnostic framework** that overcomes this circularity and decomposes routing signal into interpretable components (death avoidance vs non-death performance). The framework produces three diagnostic outputs: (1) penalty-independent label fraction (what % of routing decisions stem from catastrophic failure?), (2) Death Avoidance Factor decomposition (how much of the performance gap is death-driven?), (3) oracle degeneracy detection (is routing necessary at all?). Router training on framework-produced labels yields an **informative negative**: episode-level independent eval 47.1±2.2% < majority-vote 50.0% (8-seed cross-split, D089), and data scaling (25%–800%) shows no improvement — consistent with the framework's diagnosis that signal is task-type-level, not step-level learnable.
15	
16	**C2 (Case study finding: death avoidance dominates ScienceWorld routing)**: Applied to ScienceWorld (11 task types, 245 episodes [A]), the framework reveals that **death avoidance is the dominant routing mechanism**: 78.9% of non-tie labels from death asymmetry [A], DAF=90.41% at P=100 [A] (Δ_full=+29.60, Δ_nd=+2.84 [A]), r=0.9698 (p=8.12e-07) [A]. Death rates: internal 42.9% / deterministic 16.3% [A]. Episode-level label distribution: det-preferred 86 / internal-preferred 9 / no-preference 150 [A]. Key exception: find-non-living-thing (n=40, zero deaths, Δ_full=+9.58, all non-death) [A]. The framework further diagnoses oracle degeneracy: 96.3% of oracle decisions match always-deterministic [A], meaning routing is nearly unnecessary — a framework prediction validated by the router negative result (C1). Death dominance resists four axes of intervention: retry (48→43.5%), Reflexion (48→34%, DAF>100% at N≥3), 10× scaling to 72B (DAF=92.4%), and prompt warning (48→37%).
17	
18	**C3 (Cross-validation: model families + environment boundary probes)**: 
19	- **Cross-model**: Llama-3.1-8B full replication (N=220, 11 tasks): internal DR 41.4%, det DR 11.4%, ΔDR=+30.0pp, DAF=88.2%, direction consistency 10/10. Internal vulnerability ~42% is model-independent; det safety is model-dependent (16.3% vs 11.4%). Qwen-72B (N=255): DAF=92.4%, death dominance persists across capability levels.
20	- **Cross-domain boundary probes**: MATH (N=795, code interpreter): no catastrophic failure → no routing signal (+0.5pp, McNemar p=0.81). ALFWorld (135 games): 94.6% of non-tie labels favor information-advantaged strategy — qualitatively different mechanism (information asymmetry, not death avoidance), diagnosed by framework without modification.
21	
22	**D013 note (updated for framework-centric)**: C2 no longer claims "selective > unconditional." Router ≈ always-det is a **framework prediction** (oracle degeneracy detected), not a limitation. Keyword heuristic structurally fails (D014) — further evidence that the signal the framework detects is not capturable by simple heuristics.
23	
24	## Positioning vs Tool-Use Literature (Dream-driven addition)
25	
26	**Critical gap identified by all 3 Dream tiers**: The core pipeline (counterfactual labels → SFT small classifier → selective invocation) is standard in tool-use learning. Must position against:
27	- **Toolformer** (Schick et al. 2024): Self-supervised tool-use learning via API call insertion. SimGate differs: hindsight labels from environment forking (not self-supervised), safety-aware framing (not general tool selection).
28	- **ART** (Paranjape et al. 2023): Automated tool selection via LLM reasoning. SimGate: dedicated lightweight router, not LLM-as-router.
29	- **Chameleon** (Lu et al. 2024): LLM-as-planner routing to diverse tools. SimGate: single modality (deterministic computation), explicit small router.
30	- **ToolkenGPT** (Hao et al. 2024): Token-level tool triggers. SimGate: step-level routing with counterfactual labels.
31	
32	**Our differentiation** [D126 framework-centric]: (1) **Diagnostic framework**, not tool selector — we provide a reusable methodology for decomposing routing signal, not a better router. (2) Episode-level counterfactual labeling overcomes per-step oracle circularity (97.4% tie rate). (3) Framework produces interpretable diagnostics: label fraction, DAF decomposition, oracle degeneracy detection. (4) Router negative result is a **validated framework prediction** (oracle degeneracy → routing unnecessary → router should fail), not a limitation. (5) Cross-domain boundary probes (MATH, ALFWorld) demonstrate framework generalizability.
33	
34	**Paper must include a dedicated Related Work section** (not just intro paragraphs). Minimum coverage: tool-use learning (Toolformer, ART, Chameleon), adaptive computation (CogRouter, ARES, Mixture-of-Depths), world model routing (ITP-R, Dyna-Think), agent frameworks (ReAct).
35	
36	## Story Spine — [D126 framework-centric]
37	
38	- **Problem**: LLM agents can route between internal reasoning and deterministic external computation (simulators, code interpreters), but existing approaches learn WHEN to route without understanding WHAT the routing signal actually captures. Per-step oracle labeling degenerates in sparse-reward settings (97.4% tie rate on ScienceWorld). Tool-use methods (Toolformer, ART, Chameleon) learn general tool selection but don't decompose WHY tool invocation helps. The field lacks a diagnostic methodology for understanding routing signal composition.
39	
40	- **Our contribution**: We develop episode-level counterfactual analysis as a diagnostic framework. By comparing complete episode outcomes under pure-internal and pure-deterministic strategies, the framework decomposes routing signal into interpretable components and detects oracle degeneracy. **ScienceWorld case study**: the framework reveals death avoidance accounts for ~90% of routing signal [A] (78.9% of non-tie labels from death asymmetry), and diagnoses that routing is nearly unnecessary (96.3% oracle-det agreement). This dominance resists four axes of intervention (retry, Reflexion, 10× scaling, prompt warning). Cross-model replication (Llama-8B: DAF=88.2%, Qwen-72B: DAF=92.4%) confirms generality. Cross-domain probes (MATH: no death → no signal; ALFWorld: information asymmetry, not death) demonstrate framework applicability beyond the primary case study. Router training yields an informative negative (47.1% < majority-vote 50.0%) — a framework prediction, not a limitation.
41	
42	- **Headline result template**: "We develop episode-level counterfactual analysis as a diagnostic framework for understanding when and why deterministic computation helps LLM agents. On ScienceWorld (11 task types, 245 episodes), the framework reveals that death avoidance accounts for 78.9% of routing labels and 90.4% of the performance gap (DAF; r=0.97, p<10⁻⁶), a finding that replicates across model families (Llama-8B, Qwen-72B) and resists four standard agent improvements. Cross-domain probes confirm the framework generalizes: no catastrophic failure → no routing signal."
43	
44	## Paper Structure (8-page long paper)
45	
46	| Section | Pages | Content |
47	|---------|-------|---------|
48	| Abstract | 0.3 | Counterfactual analysis framing, death avoidance finding (multi-model), headline numbers, cross-domain evidence |
49	| Introduction | 1.2 | Problem (LLM catastrophic failures) + gap (per-step oracle degeneracy) + contribution (methodology + finding + cross-model/domain validation) |
50	| Related Work | 1.0 | Tool-use learning (Toolformer/ART/Chameleon/ToolkenGPT), adaptive computation (CogRouter/ARES/MoD), world model routing (ITP-R/Dyna-Think), safe RL, counterfactual-in-RL (Amitai/Gajcin/Olson) |
51	| Method | 1.5 | Full formalism: counterfactual framework definition, labeling pipeline (pseudocode/algorithm), DAF derivation + properties, router architecture, death decomposition framework |
52	| Experiments | 3.0 | §4.1 ScienceWorld death decomposition (core, Qwen2.5-7B); §4.2 Multi-model validation (Model B on same tasks); §4.3 Cross-domain negative contrast: MATH 795 problems (internal ≈ code interpreter → confirms death avoidance mechanism); §4.4 Temporal analysis + failure modes; §4.5 Ablations (router, labeling quality, keyword baseline structural failure) |
53	| Discussion | 0.5 | Implications for router design, scaling predictions (stronger models → lower death rate → lower DAF), when methodology applies vs doesn't |
54	| Conclusion | 0.5 | Summary + limitations + future work |
55	| References | ~1.0 | Not counted in 8-page limit |
56	
57	## Anticipated Reviewer Concerns & Mitigations
58	
59	1. **"Novelty is incremental — just SFT a small model to classify"**
60	   - Mitigation [D126 framework-centric]: Contribution is the **diagnostic framework** (episode-level counterfactual analysis), not the router. Router negative result is a **framework prediction** (oracle degeneracy detected → routing unnecessary → router should fail), not a limitation. R1 explicitly endorsed: "如果选择 framework-centric 路线，novelty 质疑就会被大幅缓解." Framework produces three diagnostic outputs applicable to any agent-tool routing scenario.
61	
62	2. **"Only one benchmark (ScienceWorld)"**
63	   - Mitigation [UPGRADED for long paper]: Multi-model validation (§4.2) shows finding holds across model families. MATH 795-problem evaluation (§4.3) demonstrates cross-domain applicability (code interpreter as deterministic oracle). ALFWorld exploratory evidence in Discussion.
64	
65	3. **"Comparison unfair — CogRouter uses RL (CoPO), you use SFT"**
66	   - Mitigation: Our primary comparison is SimGate vs ablated baselines (always-internal, always-deterministic, random, heuristic) — all same training budget. CogRouter/ITP-R cited from papers for context.
67	
68	4. **"Death avoidance is trivial — just always use deterministic"**
69	   - Mitigation: We do NOT claim selective > unconditional deterministic. Our contribution is the empirical finding that death avoidance dominates routing signal (~90% [A]), and the methodology that reveals this. Always-deterministic is a strong baseline — the interesting question is WHY (death avoidance), not WHETHER to route selectively. Plan-011 rule-based comparison + plan-012 death decomposition quantify this.
70	
71	5. **"DAgger gap — SFT on pure-strategy trajectories may not transfer to mixed-strategy deployment"**
72	   - Mitigation: Acknowledge explicitly (cite Ross et al. 2011). Plan C exacerbates this: router trains on always-internal/always-deterministic trajectories but deploys on mixed. Report train/test gap. If significant, discuss DAgger-style iterative relabeling as extension. Note: Plan C's episode-level labels avoid oracle circularity (no per-step tie-breaking), which is a methodological advantage even if distribution shift remains.
73	
74	6. **"ScienceWorld's -100 penalty inflates gains"** (Dream all 3 tiers)
75	   - Mitigation: Report gains WITH and WITHOUT death episodes separately. If non-death gains are small, honestly acknowledge that the primary value is catastrophic failure prevention — this IS our framing. Also report: what fraction of routing labels are genuine vs tie-break artifacts.
76	
77	7. **"Missing tool-use literature — this is just Toolformer"** (Dream all 3 tiers, CRITICAL)
78	   - Mitigation: Dedicated Related Work section. Position against Toolformer/ART/Chameleon. Differentiation: counterfactual trajectory labeling (not self-supervised), safety-aware framing (not general tool selection), explicit modular router (not LLM-as-router). (4) Episode-level counterfactual labeling — overcomes per-step oracle circularity in sparse-reward environments (97.4% tie rate).
79	
80	8. **"Rule-based routing baseline missing"** (Dream median + worst)
81	   - Mitigation: **D014 resolved — keyword routing structurally fails.** Two keyword lists tested: v1 (generic verbs incl. connect) → ≈always-det (85.8%); v2 (science-only: heat/boil/melt/freeze) → ≈always-internal (4.9%, near-zero hits). ScienceWorld actions use generic interaction verbs, not science keywords. Paper positions this as "structural failure analysis" — keyword heuristics fundamentally cannot capture routing signal in this environment, supporting the need for learned/observation-based approaches. D014: keywords v2 (science-only verbs), v1 had connect/disconnect degeneracy.
82	
83	## Venue Fit Risks (Long Paper, Main Track)
84	
85	- EMNLP LLM Agents track is a natural fit (tool use + planning + evaluation)
86	- Long paper needs: breadth (multi-model + cross-domain) + depth (temporal analysis + failure taxonomy) + methodology contribution
87	- Risk: "Analysis paper, no method contribution" — [D126] framework-centric pivot directly addresses this: C1 IS the methodology contribution. Algorithm box + formal definitions + three diagnostic outputs elevate from ad hoc to principled.
88	- Risk: "Death avoidance is the only signal" — mitigate: multi-model validation shows it's a general phenomenon; MATH shows methodology generalizes; Discussion section addresses when/why this applies.
89	- Risk: Router ≈ always-det → [D126] reframed as framework prediction (oracle degeneracy detected), not novelty concern. **D014: keyword routing structurally fails** — further validates framework's diagnostic value.
90	- Risk: Scaling concern (stronger models → less death → less routing signal) — address honestly in Discussion as a feature not bug: the methodology DETECTS when routing adds value.
91	
92	## Key Differences from IDEA_BRIEF / Short Paper
93	
94	1. **D050 scope expansion**: From short paper (4p, ScienceWorld only) to long paper (8p, multi-model + cross-domain).
95	2. **C3 added**: Cross-model generality claim (pending multi-model experiment).
96	3. **MATH upgraded**: From "future work" to §4.3 full evaluation (795 problems).
97	4. **Structure**: Full Related Work + Discussion sections; Method expanded with formalism.
98	5. **D126 Framing pivoted**: From finding-centric ("we found death avoidance dominates") to framework-centric ("we develop a diagnostic framework; ScienceWorld case study reveals death avoidance dominates"). R1 endorsed this pivot.
99	
100	## Robustness Check (30-task prescreening, appendix only)
101	
102	A broader prescreening analysis across 30 task types / 249 episodes [B] provides robustness support: Δ_full=+38.33 [B], Δ_nd=+0.48 [B], DAF=98.75% [B], r=0.9864 [B]. The higher DAF in prescreening reflects the inclusion of many low-n task types where death dominance is even more pronounced. These numbers appear only in the appendix.
103	
104	## 数据源权威声明
105	
106	- **主表（A）**: plan-012-full, 11 tasks / 245 episodes — 所有主文引用
107	- **Robustness（B）**: prescreening, 30 tasks / 249 episodes — 仅 appendix
108	- **绝对不引用**: death_decomposition_report.json（文件名误导，实际是 30-task 数据）
109	- **绝对不引用**: results/plan_c_test_labels/implicit_sft.jsonl（标签损坏，no-preference→internal 映射错误）
110	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "884ed247-b679-42fa-b4b2-0848de88be76",
  "isSidechain": true,
  "promptId": "c4d4f0db-2852-40ad-afac-040fa0e315f4",
  "agentId": "a8379fcc020347a2e",
  "type": "user",
  "uuid": "c9cf2b3e-b02b-49c3-a16a-f33cb048fde3",
  "sourceToolAssistantUUID": "884ed247-b679-42fa-b4b2-0848de88be76",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm"
}
```

</details>

---

### Assistant

_source line 5 · 2026-05-19T20:28:29.610Z_

Based on the paper_framing.md file, here is the extracted information:

## **1. Core Claims (C1/C2/C3)**

**C1 — Diagnostic Framework (Episode-level Counterfactual Analysis)**
- Per-step oracle labeling degenerates to 97.4% tie rate in sparse-reward environments (ScienceWorld)
- Proposes episode-level counterfactual analysis as a reusable diagnostic framework
- Framework produces three diagnostic outputs: (1) penalty-independent label fraction, (2) Death Avoidance Factor (DAF) decomposition, (3) oracle degeneracy detection
- Router training result: 47.1±2.2% < majority-vote 50.0% (informative negative, consistent with framework prediction that signal is task-level, not step-level learnable)

**C2 — Case Study Finding (Death Avoidance Dominates ScienceWorld)**
- On ScienceWorld (11 task types, 245 episodes): death avoidance accounts for 78.9% of non-tie labels and DAF=90.41% at P=100
- Death rates: internal 42.9% / deterministic 16.3%
- Oracle degeneracy: 96.3% of oracle decisions match always-deterministic (routing nearly unnecessary)
- Death dominance resists: retry, Reflexion, 10× scaling to 72B, and prompt warning
- Exception: find-non-living-thing task (zero deaths, all non-death signal)

**C3 — Cross-Validation (Model Families + Environment Boundary Probes)**
- **Cross-model**: Llama-3.1-8B (N=220): internal DR 41.4%, det DR 11.4%, DAF=88.2%; Qwen-72B (N=255): DAF=92.4%
- **Cross-domain**: MATH (795 problems): no catastrophic failure → no routing signal (+0.5pp); ALFWorld (135 games): 94.6% of non-tie labels favor information-advantaged strategy (different mechanism—information asymmetry, not death avoidance)

## **2. Reviewer Concerns & Mitigations**

1. **Novelty incremental**: Reframed as framework contribution (diagnostic methodology), not router architecture; router negative result is a validated framework prediction
2. **Only one benchmark**: Mitigated by multi-model validation (§4.2) and cross-domain evaluation (MATH §4.3, ALFWorld)
3. **Unfair comparison**: Primary comparison is SimGate vs ablated baselines (same training budget), not CogRouter
4. **Death avoidance trivial**: Paper does NOT claim selective > unconditional; contribution is the empirical finding + methodology
5. **DAgger gap**: Acknowledged explicitly; episode-level labels avoid oracle circularity (methodological advantage despite distribution shift)
6. **ScienceWorld -100 penalty inflates gains**: Report gains with/without death episodes separately; acknowledge primary value is catastrophic failure prevention
7. **Missing tool-use literature**: Dedicated Related Work section with Toolformer/ART/Chameleon positioning; differentiation is counterfactual trajectory labeling (not self-supervised) + safety-aware framing
8. **Rule-based routing baseline missing**: D014 resolved — keyword routing structurally fails; v1 always-det (85.8%), v2 near-zero hits (4.9%)

## **3. Known Weaknesses / Attack Surfaces**

- **Scaling concern** (discussed in §91): Stronger models → less death → lower DAF; addressed honestly in Discussion as "a feature not a bug" — methodology detects when routing adds value
- **Router ≈ always-deterministic degeneracy**: Reframed as oracle degeneracy framework prediction (not limitation); keyword heuristics fail structurally (D014)
- **Distribution shift (DAgger gap)**: Router trains on pure-strategy trajectories; acknowledged as explicit limitation with mitigation path (iterative relabeling)
- **Venue risk — "Analysis paper, no method"**: Mitigated by framework-centric pivot; C1 IS methodology contribution with formalism + algorithm box + diagnostic outputs
- **Death signal may not generalize**: Mitigated by cross-model validation; MATH shows framework generalizes even when death mechanism absent

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9cf2b3e-b02b-49c3-a16a-f33cb048fde3",
  "isSidechain": true,
  "agentId": "a8379fcc020347a2e",
  "requestId": "req_011CbCZLoAAxqsJiTMaUSG9d",
  "attributionAgent": "Explore",
  "type": "assistant",
  "uuid": "550020a0-b30e-4375-ae68-9a9f385c00c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_12/projects/simgate-modular-routing/.claude/sessions/reviewer_65b870d4",
  "sessionId": "6f930a9e-f0ae-4c02-bcff-b720c0f808d0",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "sharded-scribbling-charm",
  "message": {
    "model": "claude-haiku-4-5-20251001",
    "id": "msg_01NKcfKhpFj5PPWfropmoc1b",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5,
      "cache_creation_input_tokens": 5641,
      "cache_read_input_tokens": 18766,
      "output_tokens": 1022,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5641
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5,
          "output_tokens": 1022,
          "cache_read_input_tokens": 18766,
          "cache_creation_input_tokens": 5641,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5641,
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
