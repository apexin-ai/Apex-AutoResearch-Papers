# paper fix response letter refs

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 72
- **Recorded user turns:** 0
- **Tool calls:** 28
- **Original source:** `logs/workers/worker_paper_fix_response_letter_refs_20260523T051014.log`
- **Structured JSON:** [`0f64987d8063f8ff6485.json`](../../sessions/0f/0f64987d8063f8ff6485.json)

## Before a recorded user message

72 recorded events

### Log line

_source line 1_

Warning: no stdin data received in 3s, proceeding without it. If piping from a slow command, redirect stdin explicitly: < /dev/null to skip, or wait longer.

---

### System

_source line 2_

```json
{
  "type": "system",
  "subtype": "init",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen",
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "tools": [
    "Task",
    "AskUserQuestion",
    "Bash",
    "CronCreate",
    "CronDelete",
    "CronList",
    "Edit",
    "EnterPlanMode",
    "EnterWorktree",
    "ExitPlanMode",
    "ExitWorktree",
    "Glob",
    "Grep",
    "ListMcpResourcesTool",
    "Monitor",
    "NotebookEdit",
    "PushNotification",
    "Read",
    "ReadMcpResourceTool",
    "RemoteTrigger",
    "ScheduleWakeup",
    "Skill",
    "TaskOutput",
    "TaskStop",
    "TodoWrite",
    "ToolSearch",
    "WebFetch",
    "WebSearch",
    "Write",
    "mcp__agent-ml-research__append_idea",
    "mcp__agent-ml-research__read_project_file",
    "mcp__agent-ml-research__save_project_file"
  ],
  "mcp_servers": [
    {
      "name": "agent-ml-research",
      "status": "connected"
    }
  ],
  "model": "claude-opus-4-6",
  "permissionMode": "bypassPermissions",
  "slash_commands": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api",
    "clear",
    "compact",
    "context",
    "heapdump",
    "init",
    "review",
    "security-review",
    "extra-usage",
    "usage",
    "insights",
    "team-onboarding"
  ],
  "apiKeySource": "none",
  "claude_code_version": "2.1.126",
  "output_style": "default",
  "agents": [
    "claude",
    "Explore",
    "general-purpose",
    "Plan",
    "statusline-setup"
  ],
  "skills": [
    "update-config",
    "debug",
    "simplify",
    "batch",
    "fewer-permission-prompts",
    "loop",
    "schedule",
    "claude-api"
  ],
  "plugins": [],
  "analytics_disabled": false,
  "uuid": "e729e14a-01c3-4e19-b859-cc6b5f0b0119",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude/projects/-home-ubuntu--agent-ml-research-idea-gen-0520-2-projects-irt-equated-bench-regen/memory/"
  },
  "fast_mode_state": "off"
}
```

---

### Runtime record

_source line 3_

```json
{
  "type": "rate_limit_event",
  "rate_limit_info": {
    "status": "allowed",
    "resetsAt": 1779527400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "aa35f9a3-03bf-4fd3-b679-33f36344ebe2",
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e"
}
```

---

### Assistant

_source line 4_

I'll start by reading the aux file and the response letter in parallel to understand the current state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "aa04c202-6dee-428c-9440-104f38949a90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmeUDyihzGVKU7Lp8MBvvC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13028
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 5_

<details open><summary>🔧 Tool call — Read · `toolu_013dehKZA6YMQKLyxvD1Rmtg`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "55b17b44-d4a7-4e9e-af22-6252635f3486",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmeUDyihzGVKU7Lp8MBvvC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13028
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-23T05:10:27.130Z_

<details><summary>↩ Tool result · reported error · `toolu_013dehKZA6YMQKLyxvD1Rmtg`</summary>

```text
File content (28099 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "548c36ce-54d7-4620-a4b8-b3a566ec2dd6",
  "tool_use_result": "Error: File content (28099 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file."
}
```

</details>

---

### Tool call

_source line 7_

<details open><summary>🔧 Tool call — Read · `toolu_018S2ktc6J3ZW2PfmMqcjimu`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "1fd388a6-fbff-4637-ad94-1291e82a996a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EmeUDyihzGVKU7Lp8MBvvC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 13028,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 13028
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-23T05:10:27.183Z_

<details><summary>↩ Tool result · `toolu_018S2ktc6J3ZW2PfmMqcjimu`</summary>

```text
1	# Author Response
2	
3	We thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.
4	
5	---
6	
7	## Reviewer 1
8	
9	### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis
10	
11	**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.
12	
13	**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:
14	
15	| Tier | Families | Mean size | ICC | DEFF | Adj. C% |
16	|------|----------|-----------|-----|------|---------|
17	| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |
18	| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |
19	| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |
20	| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |
21	
22	Tier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).
23	
24	We now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*
25	
26	**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\rho = -0.009$, $p = 0.96$; Appendix E).
27	
28	**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\text{ref} + N_\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*
29	
30	### [R1-W2] Graduated De-Duplication Definition
31	
32	**Concern**: De-duplication was one of three convergence methods but was never formally defined.
33	
34	**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \text{all}$ is deterministic).
35	
36	C% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\pm$ 0.9% ($N \approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*
37	
38	### [R1-W3] Semi-Synthetic ΔTPR Generalizability
39	
40	**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.
41	
42	**Response**: We now provide two complementary analyses beyond binary flipping:
43	
44	1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.
45	
46	2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\rho$ ($-0.676 \pm 0.005$ vs. observed $-0.597$) and direction reversal ($\chi^2 = 634 \pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\rho_\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.
47	
48	The revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*
49	
50	### [R1-W4] Causal Ambiguity and Framing Tension
51	
52	**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.
53	
54	**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):
55	
56	1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.
57	
58	2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\rho_\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).
59	
60	We revised the framing throughout: Contribution 1 is now positioned as "empirical demonstration that global exposure and differential functioning are orthogonal constructs" rather than "ground truth meta-critique." §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*
61	
62	### [R1-W6] K=10 Non-Uniform DIF Leakage
63	
64	**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.
65	
66	**Response**: We strengthened the caveat in §4.2: the K=10 peak "may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation." C% is stable across $K \geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*
67	
68	### [R1-W10] 1:1 Matching Details
69	
70	**Concern**: Matching method, balance check, and sample size impact were not reported.
71	
72	**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*
73	
74	---
75	
76	## Reviewer 2
77	
78	### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol
79	
80	**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.
81	
82	**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:
83	
84	1. **Framing alignment**: Contribution 1 is reframed from "ground truth meta-critique" to "empirical demonstration that global exposure and differential functioning are orthogonal constructs." All "category error" and "meta-critique" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*
85	
86	2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:
87	   - E2 (logistic regression): OR = 4.75 for difficulty $\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.
88	   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\rho$ and $\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).
89	
90	3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*
91	
92	### [R2-W2] Ground Truth Meta-Critique Framing
93	
94	**Concern**: "Category error in prevailing validation methodology" is circular; should reframe as empirical finding.
95	
96	**Response**: Contribution 1 is now "Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964)." All "category error" language removed. *(Revised in paper, §1)*
97	
98	### [R2-W3] Methodological Novelty
99	
100	**Concern**: MH-DIF is a standard method; contributions are primarily empirical.
101	
102	**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.
103	
104	### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation
105	
106	**Concern**: The difficulty-direction interaction ($\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).
107	
108	**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:
109	
110	1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\rho = -0.079$; $\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.
111	
112	2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\rho_\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.
113	
114	We emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as "arguing against a *pure* difficulty-dependent contamination account" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*
115	
116	### [R2-W6] MMLU Item Quality Exclusion Evidence
117	
118	**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; "ruled out" is too strong.
119	
120	**Response**: We revised the wording from "ruled out" to "no enrichment detected" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*
121	
122	### [R2-W7] GSM1K Exploratory Analysis Weight
123	
124	**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.
125	
126	**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as "an exploratory cross-benchmark signal... but the small sample requires replication." The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*
127	
128	### [R2-W8] enlargethispage Format
129	
130	**Concern**: `\enlargethispage*{14\baselineskip}` ($\approx$2.5 inches) risks AC format rejection.
131	
132	**Response**: Reduced to $\leq 4$`\baselineskip` in §4.3 and $10$`\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*
133	
134	### [R2-W9] Abstract Scope Mismatch
135	
136	**Concern**: "5,227 models" is the MMLU count; GSM8K uses 6,702.
137	
138	**Response**: Abstract now reads "5,227 MMLU models." *(Revised in paper, Abstract)*
139	
140	### [R2-Q3/Q6] ≥500 Model Threshold
141	
142	**Concern**: Power analysis shows $N \geq 80$ per cohort suffices; ≥500 total models is overly conservative.
143	
144	**Response**: We softened the threshold in §5.2: "≥500 models" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that "smaller corpora may suffice with fewer strata." New experiment E1 confirms this:
145	
146	$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*
147	
148	### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)
149	
150	**Concern**: Shorter temporal windows producing higher C% is counterintuitive.
151	
152	**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*
153	
154	---
155	
156	## Meta-Reviewer
157	
158	### [MR-1] Missing References
159	
160	**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).
161	
162	**Response**: We verified all three citations:
163	- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).
164	- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).
165	- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.
166	
167	Additionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*
168	
169	---
170	
171	## Additional Corrections
172	
173	### [DATA-1] Rank-Bucket Data Error
174	
175	During internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\Delta\text{rank} \in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*
176	
177	---
178	
179	## Summary of Changes
180	
181	| ID | Issue | Type | Status |
182	|----|-------|------|--------|
183	| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |
184	| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |
185	| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |
186	| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |
187	| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |
188	| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |
189	| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |
190	| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |
191	| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |
192	| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |
193	| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |
194	| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |
195	| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |
196	| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |
197	| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |
198	| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |
199	| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |
200	| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |
201	| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |
202	| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |
203	| — | Unused bib entries (7) | Proactive | Cleaned |
204	
205	### New Experimental Evidence
206	
207	| Label | Experiment | Key Result | Location |
208	|-------|-----------|------------|----------|
209	| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |
210	| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |
211	| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\rho_\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |
212	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "e1d62174-5cda-4d22-8228-e291b04b4732",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
      "content": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix E).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
      "numLines": 212,
      "startLine": 1,
      "totalLines": 212
    }
  }
}
```

</details>

---

### Assistant

_source line 9_

<details><summary>Logged reasoning block</summary>

```text
Now let me search the aux file for the relevant labels to confirm the correct numbering.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "002fa4d4-21c5-4f22-a020-1ece138620b9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXizGFAfYaKk6S39YETj8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6659,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6659
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 10_

Let me search the aux file for the specific labels.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "6e0029d1-bde4-49dd-87e9-317b05e9bf11",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXizGFAfYaKk6S39YETj8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6659,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6659
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — Grep · `toolu_01WWVbuWZ9iQ2hq4NXGyLs1F`</summary>

```json
{
  "pattern": "newlabel\\{(tab:k3_power|tab:deff_stratified|app:uncertainty|app:dedup_k|app:icc_family|app:rank_reversal)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "a46579fd-c944-4fc1-bbff-ff1d3147b040",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXizGFAfYaKk6S39YETj8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6659,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6659
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 12 · 2026-05-23T05:10:37.666Z_

<details><summary>↩ Tool result · `toolu_01WWVbuWZ9iQ2hq4NXGyLs1F`</summary>

```text
1444:\newlabel{tab:k3_power}{{5}{13}{Detection power: K=3 vs K=5 at $|\Delta _{\mathrm {MH}}| \geq 1.0$}{table.caption.26}{}}
1445:\newlabel{tab:k3_power@cref}{{[table][5][]5}{[1][13][]13}{}{}{}}
1596:\newlabel{tab:deff_stratified}{{9}{15}{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\ C\% applies tier-specific DEFF to all items}{table.caption.35}{}}
1597:\newlabel{tab:deff_stratified@cref}{{[table][9][]9}{[1][14][]15}{}{}{}}
1601:\newlabel{app:uncertainty}{{D}{15}{Uncertainty Quantification Comparison}{appendix.D}{}}
1602:\newlabel{app:uncertainty@cref}{{[section][4][]D}{[1][14][]15}{}{}{}}
1678:\newlabel{app:icc_family}{{H}{16}{Within-Family Similarity by Family Size}{appendix.H}{}}
1679:\newlabel{app:icc_family@cref}{{[section][8][]H}{[1][16][]16}{}{}{}}
1700:\newlabel{app:dedup_k}{{I}{16}{Graduated De-Duplication Sensitivity}{appendix.I}{}}
1701:\newlabel{app:dedup_k@cref}{{[section][9][]I}{[1][16][]16}{}{}{}}
1722:\newlabel{app:rank_reversal}{{J}{16}{Rank-Reversal by Distance}{appendix.J}{}}
1723:\newlabel{app:rank_reversal@cref}{{[section][10][]J}{[1][16][]16}{}{}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "ecea172a-b8d5-42e1-aab7-068c6eaa2530",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1444:\\newlabel{tab:k3_power}{{5}{13}{Detection power: K=3 vs K=5 at $|\\Delta _{\\mathrm {MH}}| \\geq 1.0$}{table.caption.26}{}}\n1445:\\newlabel{tab:k3_power@cref}{{[table][5][]5}{[1][13][]13}{}{}{}}\n1596:\\newlabel{tab:deff_stratified}{{9}{15}{Size-stratified DEFF analysis. ICC and DEFF computed per tier; Adj.\\ C\\% applies tier-specific DEFF to all items}{table.caption.35}{}}\n1597:\\newlabel{tab:deff_stratified@cref}{{[table][9][]9}{[1][14][]15}{}{}{}}\n1601:\\newlabel{app:uncertainty}{{D}{15}{Uncertainty Quantification Comparison}{appendix.D}{}}\n1602:\\newlabel{app:uncertainty@cref}{{[section][4][]D}{[1][14][]15}{}{}{}}\n1678:\\newlabel{app:icc_family}{{H}{16}{Within-Family Similarity by Family Size}{appendix.H}{}}\n1679:\\newlabel{app:icc_family@cref}{{[section][8][]H}{[1][16][]16}{}{}{}}\n1700:\\newlabel{app:dedup_k}{{I}{16}{Graduated De-Duplication Sensitivity}{appendix.I}{}}\n1701:\\newlabel{app:dedup_k@cref}{{[section][9][]I}{[1][16][]16}{}{}{}}\n1722:\\newlabel{app:rank_reversal}{{J}{16}{Rank-Reversal by Distance}{appendix.J}{}}\n1723:\\newlabel{app:rank_reversal@cref}{{[section][10][]J}{[1][16][]16}{}{}{}}",
    "numLines": 12
  }
}
```

</details>

---

### Tool call

_source line 13_

<details open><summary>🔧 Tool call — Grep · `toolu_01SRamSYXVB9oDYHcu6eUdJR`</summary>

```json
{
  "pattern": "GSM1K|gsm1k",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "68e6a541-f803-4b96-af13-afbd024da7e0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EXizGFAfYaKk6S39YETj8S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6659,
      "cache_read_input_tokens": 24869,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6659
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-23T05:10:38.525Z_

<details><summary>↩ Tool result · `toolu_01SRamSYXVB9oDYHcu6eUdJR`</summary>

```text
1705:[Omitted long matching line]
1706:[Omitted long matching line]
1707:\newlabel{app:fig_gsm1k@cref}{{[figure][5][]5}{[1][15][]16}{}{}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "d7377848-689c-4e45-aa20-354a2bbe78eb",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1705:[Omitted long matching line]\n1706:[Omitted long matching line]\n1707:\\newlabel{app:fig_gsm1k@cref}{{[figure][5][]5}{[1][15][]16}{}{}{}}",
    "numLines": 3
  }
}
```

</details>

---

### Assistant

_source line 15_

<details><summary>Logged reasoning block</summary>

```text
Let me find the GSM1K section label to confirm it's §4.7.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "7fc24fa8-b52f-4ff3-b75c-36f5035f7782",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfErv9JzUafwKD3KE2xSS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 31528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 16_

Let me find the GSM1K section reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "f4adbd4d-4793-4a0a-a193-5cafb651b9e3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfErv9JzUafwKD3KE2xSS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 31528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 17_

<details open><summary>🔧 Tool call — Grep · `toolu_01RM1d9nkEPBV5PjfLoM2ieb`</summary>

```json
{
  "pattern": "newlabel\\{sec:gsm|gsm1k|cross.benchmark",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "f9940f2f-19ae-41d8-bdbd-b039e2daeeb1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MfErv9JzUafwKD3KE2xSS6",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 940,
      "cache_read_input_tokens": 31528,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 940
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-23T05:10:42.498Z_

<details><summary>↩ Tool result · `toolu_01RM1d9nkEPBV5PjfLoM2ieb`</summary>

```text
783:[Omitted long matching line]
784:\newlabel{tab:cross_benchmark@cref}{{[table][3][]3}{[1][8][]8}{}{}{}}
811:\newlabel{sec:gsm8k}{{4.7}{8}{Cross-Benchmark Validation}{subsection.4.7}{}}
812:\newlabel{sec:gsm8k@cref}{{[subsection][7][4]4.7}{[1][8][]8}{}{}{}}
1706:[Omitted long matching line]
1707:\newlabel{app:fig_gsm1k@cref}{{[figure][5][]5}{[1][15][]16}{}{}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "d1f0bd87-ea23-4426-9858-31cb89e1ec94",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "783:[Omitted long matching line]\n784:\\newlabel{tab:cross_benchmark@cref}{{[table][3][]3}{[1][8][]8}{}{}{}}\n811:\\newlabel{sec:gsm8k}{{4.7}{8}{Cross-Benchmark Validation}{subsection.4.7}{}}\n812:\\newlabel{sec:gsm8k@cref}{{[subsection][7][4]4.7}{[1][8][]8}{}{}{}}\n1706:[Omitted long matching line]\n1707:\\newlabel{app:fig_gsm1k@cref}{{[figure][5][]5}{[1][15][]16}{}{}{}}",
    "numLines": 6
  }
}
```

</details>

---

### Assistant

_source line 19_

Confirmed all labels. The aux file confirms:
- `tab:k3_power` → Table 5
- `tab:deff_stratified` → Table 9
- `app:uncertainty` → Appendix D
- `app:dedup_k` → Appendix I
- `app:icc_family` → Appendix H
- `app:rank_reversal` → Appendix J
- `sec:gsm8k` → §4.7

Now let me find all occurrences that need fixing in the response letter.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "86e8b7b9-4c13-420f-98b2-cf4ab3575235",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xMwWMhMBeVM7uZUp8wgiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 32468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 20_

<details open><summary>🔧 Tool call — Grep · `toolu_011UV2PcPpVKEQAfQP5d6d1M`</summary>

```json
{
  "pattern": "Table A\\.|Appendix [A-F][^-]|§4\\.6",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "output_mode": "content",
  "-n": true
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "9dd79a4f-9825-4059-96f9-2a447e712b40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019xMwWMhMBeVM7uZUp8wgiY",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 373,
      "cache_read_input_tokens": 32468,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 373
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-23T05:10:48.763Z_

<details><summary>↩ Tool result · `toolu_011UV2PcPpVKEQAfQP5d6d1M`</summary>

```text
13:**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:
24:We now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*
26:**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\rho = -0.009$, $p = 0.96$; Appendix E).
28:**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\text{ref} + N_\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*
34:**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \text{all}$ is deterministic).
36:[Omitted long matching line]
44:1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.
48:The revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*
56:1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.
58:2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\rho_\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).
72:**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*
114:We emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as "arguing against a *pure* difficulty-dependent contamination account" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*
126:**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as "an exploratory cross-benchmark signal... but the small sample requires replication." The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*
146:$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*
152:**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*
175:During internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\Delta\text{rank} \in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*
183:| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |
184:| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |
185:| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |
188:| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |
189:| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |
190:| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |
195:| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |
198:| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |
200:| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |
202:| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |
209:| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "c2a46721-dc7a-4a6d-92b6-8a9f6218e5b6",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "13:**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n24:We now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n26:**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix E).\n28:**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n34:**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n36:[Omitted long matching line]\n44:1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n48:The revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n56:1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n58:2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n72:**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n114:We emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n126:**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n146:$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n152:**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n175:During internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n183:| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n184:| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n185:| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n188:| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n189:| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n190:| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n195:| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n198:| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n200:| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n202:| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n209:| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |",
    "numLines": 27
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Now I have a clear picture. Let me map out all the replacements needed:

1. **Table A.3** (line 13, 183) → **Table 9** (confirmed: `tab:deff_stratified` = Table 9)
2. **Table A.2** (line 146, 146, 209) → **Table 5** (confirmed: `tab:k3_power` = Table 5)
3. **Appendix B (§app:uncertainty)** (line 152) → **Appendix D** (confirmed: `app:uncertainty` = Appendix D)


4. **Appendix D (§app:dedup_k)** (line 34) → **Appendix I** (confirmed: `app:dedup_k` = Appendix I)
5. **Appendix E** (line 26, 189) → **Appendix H** (confirmed: `app:icc_family` = Appendix H)
6. **Appendix F (§app:rank_reversal)** (line 175, 202) → **Appendix J** (confirmed: `app:rank_reversal` = Appendix J)
7. **§4.6** (line 126, 195) → **§4.7** (confirmed: `sec:gsm8` reference)

Now I need to figure out what Appendix C actually maps to—it shows up on lines 13, 24, 28, 183, and 189, but I'm seeing some inconsistencies with the other appendices. Let me trace through which label keys correspond to A and B, since those are appearing frequently across multiple lines but the references don't seem to match up cleanly with the section labels I've already identified. I need to focus on the specific replacements the user provided rather than trying to identify all possible label changes. Looking at their mapping, I see the key distinction that "Appendix B" becomes "Appendix D" when referring to app:uncertainty, while "Appendix D" becomes "Appendix I" when referring to app:dedup_k. Let me verify what needs to happen with Appendix A and C before proceeding with the replacements.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "cecfdb16-03eb-49b0-9b80-68aa3b054bae",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABUyk6ehq2R6nMymRJFqJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 32841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2397
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Assistant

_source line 23_

Let me also verify Appendix A and C references in the aux file, in case they need fixing too.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "a21b79bf-17d9-4d85-9385-500de52b2f07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABUyk6ehq2R6nMymRJFqJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 32841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2397
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 24_

<details open><summary>🔧 Tool call — Grep · `toolu_01MpnYZLstvDDftEfFx12NSU`</summary>

```json
{
  "pattern": "newlabel\\{app:(mixed_mechanism|interaction|method_details|deff|family|icc)",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/paper/main.aux",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "8cec07ba-48f6-44f3-ae80-6e689f8c8a24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ABUyk6ehq2R6nMymRJFqJX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2397,
      "cache_read_input_tokens": 32841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2397
      },
      "output_tokens": 8,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 25 · 2026-05-23T05:11:14.839Z_

<details><summary>↩ Tool result · `toolu_01MpnYZLstvDDftEfFx12NSU`</summary>

```text
1324:\newlabel{app:method_details}{{A}{12}{Method Details}{appendix.A}{}}
1325:\newlabel{app:method_details@cref}{{[section][1][]A}{[1][12][]12}{}{}{}}
1470:\newlabel{app:interaction}{{A.2}{13}{Difficulty--model-type interaction}{section*.29}{}}
1471:\newlabel{app:interaction@cref}{{[subsection][2][1]A.2}{[1][13][]13}{}{}{}}
1485:\newlabel{app:mixed_mechanism}{{A.2}{13}{Mixed-mechanism injection}{section*.30}{}}
1486:\newlabel{app:mixed_mechanism@cref}{{[subsection][2][1]A.2}{[1][13][]13}{}{}{}}
1550:\newlabel{app:deff}{{C}{14}{Design Effect Estimation}{appendix.C}{}}
1551:\newlabel{app:deff@cref}{{[section][3][]C}{[1][14][]14}{}{}{}}
1678:\newlabel{app:icc_family}{{H}{16}{Within-Family Similarity by Family Size}{appendix.H}{}}
1679:\newlabel{app:icc_family@cref}{{[section][8][]H}{[1][16][]16}{}{}{}}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "a04110a8-2b03-495a-9516-e4e2ae42db35",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "1324:\\newlabel{app:method_details}{{A}{12}{Method Details}{appendix.A}{}}\n1325:\\newlabel{app:method_details@cref}{{[section][1][]A}{[1][12][]12}{}{}{}}\n1470:\\newlabel{app:interaction}{{A.2}{13}{Difficulty--model-type interaction}{section*.29}{}}\n1471:\\newlabel{app:interaction@cref}{{[subsection][2][1]A.2}{[1][13][]13}{}{}{}}\n1485:\\newlabel{app:mixed_mechanism}{{A.2}{13}{Mixed-mechanism injection}{section*.30}{}}\n1486:\\newlabel{app:mixed_mechanism@cref}{{[subsection][2][1]A.2}{[1][13][]13}{}{}{}}\n1550:\\newlabel{app:deff}{{C}{14}{Design Effect Estimation}{appendix.C}{}}\n1551:\\newlabel{app:deff@cref}{{[section][3][]C}{[1][14][]14}{}{}{}}\n1678:\\newlabel{app:icc_family}{{H}{16}{Within-Family Similarity by Family Size}{appendix.H}{}}\n1679:\\newlabel{app:icc_family@cref}{{[section][8][]H}{[1][16][]16}{}{}{}}",
    "numLines": 10
  }
}
```

</details>

---

### Assistant

_source line 26_

Appendix A and C are correct in the draft. Now I have the full picture. Let me do all the replacements. I'll go through each one carefully.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "79f4faa0-0ad5-4a52-aa7a-38e1bf45f43b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgpoKCiX8LZbRENvsszgWW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1696,
      "cache_read_input_tokens": 35238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1696
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 27_

<details open><summary>🔧 Tool call — Edit · `toolu_01GjWz4QLSTewhPg93EjqetB`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2).",
  "new_string": "**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "8d6ab8e7-6452-4f69-8437-d45bf3de6422",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HgpoKCiX8LZbRENvsszgWW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1696,
      "cache_read_input_tokens": 35238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1696
      },
      "output_tokens": 2,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-23T05:11:21.986Z_

<details><summary>↩ Tool result · `toolu_01GjWz4QLSTewhPg93EjqetB`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "2a375eda-ace2-4238-8cf2-f92292029c94",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2).",
    "newString": "**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2).",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix E).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 10,
        "oldLines": 7,
        "newStart": 10,
        "newLines": 7,
        "lines": [
          " ",
          " **Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.",
          " ",
          "-**Response**: We added a size-stratified DEFF analysis (Table A.3 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:",
          "+**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:",
          " ",
          " | Tier | Families | Mean size | ICC | DEFF | Adj. C% |",
          " |------|----------|-----------|-----|------|---------|"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 29_

<details open><summary>🔧 Tool call — Edit · `toolu_016DJSRYP4Lqkj7JwAA8VPko`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "Appendix E).",
  "new_string": "Appendix H)."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "de2957e1-eac0-4a87-91e6-cc9f02b5eec8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HRt73pk7fdSWSYoNBodXCb",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 308,
      "cache_read_input_tokens": 36934,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 308
      },
      "output_tokens": 67,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-23T05:11:26.658Z_

<details><summary>↩ Tool result · `toolu_016DJSRYP4Lqkj7JwAA8VPko`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "1c901d8d-cfa6-4aa9-831d-69ad4627fb1b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "Appendix E).",
    "newString": "Appendix H).",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix E).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 23,
        "oldLines": 7,
        "newStart": 23,
        "newLines": 7,
        "lines": [
          " ",
          " We now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*",
          " ",
          "-**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix E).",
          "+**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).",
          " ",
          " **Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 31_

<details open><summary>🔧 Tool call — Edit · `toolu_01Doq5Pfo7B6o3JCZyh2Gs9U`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "We added a formal definition in Appendix D (§app:dedup_k)",
  "new_string": "We added a formal definition in Appendix I (§app:dedup_k)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "aa5f5bac-9f0b-47f8-963e-0ecd311f4a62",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013BLUD36XxhthZDRS9KyNBP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 219,
      "cache_read_input_tokens": 37242,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 219
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-23T05:11:29.746Z_

<details><summary>↩ Tool result · `toolu_01Doq5Pfo7B6o3JCZyh2Gs9U`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "949d68a2-85c8-46a7-a91f-92d806b1f0b2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "We added a formal definition in Appendix D (§app:dedup_k)",
    "newString": "We added a formal definition in Appendix I (§app:dedup_k)",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 31,
        "oldLines": 7,
        "newStart": 31,
        "newLines": 7,
        "lines": [
          " ",
          " **Concern**: De-duplication was one of three convergence methods but was never formally defined.",
          " ",
          "-**Response**: We added a formal definition in Appendix D (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).",
          "+**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).",
          " ",
          " C% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Edit · `toolu_01QEcDGAW6iwsGNhZHuian7z`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "*(Revised in paper, §4.2 + Appendix D)*",
  "new_string": "*(Revised in paper, §4.2 + Appendix I)*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "fb5d592c-99b1-4fdf-bd85-aa83ee06a890",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011B3Eq3uqe8evNH3xrQewHv",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 245,
      "cache_read_input_tokens": 37461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 245
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 34 · 2026-05-23T05:11:36.876Z_

<details><summary>↩ Tool result · `toolu_01QEcDGAW6iwsGNhZHuian7z`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "f854db5b-1fb7-460c-8267-5e15c8b96c61",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "*(Revised in paper, §4.2 + Appendix D)*",
    "newString": "*(Revised in paper, §4.2 + Appendix I)*",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 33,
        "oldLines": 7,
        "newStart": 33,
        "newLines": 7,
        "lines": [
          " ",
          " **Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).",
          " ",
          "-C% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix D)*",
          "+C% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*",
          " ",
          " ### [R1-W3] Semi-Synthetic ΔTPR Generalizability",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Edit · `toolu_016wjf7UxUUrUeUFEryzWYJX`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "We reduced the GSM1K analysis to a single sentence in §4.6",
  "new_string": "We reduced the GSM1K analysis to a single sentence in §4.7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "04285f47-eb7a-4f60-8000-3dd71178a914",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017WC1fZpfwRJuCzc5ybSYBq",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 37706,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-23T05:11:40.306Z_

<details><summary>↩ Tool result · `toolu_016wjf7UxUUrUeUFEryzWYJX`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "4a7bfa01-d868-4c2b-b088-d2c2405eaab2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "We reduced the GSM1K analysis to a single sentence in §4.6",
    "newString": "We reduced the GSM1K analysis to a single sentence in §4.7",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 123,
        "oldLines": 7,
        "newStart": 123,
        "newLines": 7,
        "lines": [
          " ",
          " **Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.",
          " ",
          "-**Response**: We reduced the GSM1K analysis to a single sentence in §4.6 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*",
          "+**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*",
          " ",
          " ### [R2-W8] enlargethispage Format",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 37_

<details open><summary>🔧 Tool call — Edit · `toolu_01DDpaGYVFjF6mrrA5ipcr4R`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "*(Revised in paper, §4.6)*",
  "new_string": "*(Revised in paper, §4.7)*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "4c96cc5f-5a0a-4593-bd1d-25c80d90bb92",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EssKNJWA35yqSctjcZNij8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 243,
      "cache_read_input_tokens": 37949,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 243
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 38 · 2026-05-23T05:11:42.884Z_

<details><summary>↩ Tool result · `toolu_01DDpaGYVFjF6mrrA5ipcr4R`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "e9cdb953-1b81-49d1-98df-c5d84726a01c",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "*(Revised in paper, §4.6)*",
    "newString": "*(Revised in paper, §4.7)*",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 123,
        "oldLines": 7,
        "newStart": 123,
        "newLines": 7,
        "lines": [
          " ",
          " **Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.",
          " ",
          "-**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.6)*",
          "+**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*",
          " ",
          " ### [R2-W8] enlargethispage Format",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 39_

<details open><summary>🔧 Tool call — Edit · `toolu_01WQxVtn7RXLMfTj3B9UXXui`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*",
  "new_string": "AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "eead97ef-4bfb-4ec9-b472-f08699927f8e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QnXr6SpS8qnazSUabCjJyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 38192,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 40 · 2026-05-23T05:11:48.019Z_

<details><summary>↩ Tool result · `toolu_01WQxVtn7RXLMfTj3B9UXXui`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "d0db120d-beb4-4a77-84f9-4edd90c2584f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*",
    "newString": "AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 143,
        "oldLines": 7,
        "newStart": 143,
        "newLines": 7,
        "lines": [
          " ",
          " **Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:",
          " ",
          "-$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table A.2). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table A.2)*",
          "+$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*",
          " ",
          " ### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Edit · `toolu_018qau54uNoQKzfkESWXhUja`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "We added an explanation in Appendix B (§app:uncertainty)",
  "new_string": "We added an explanation in Appendix D (§app:uncertainty)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "96e3a7d9-3924-4032-9e33-c8dfc8b57d63",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YZZaoNrqtjZH9QNqJwG2ez",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 447,
      "cache_read_input_tokens": 38423,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 447
      },
      "output_tokens": 65,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-23T05:11:51.443Z_

<details><summary>↩ Tool result · `toolu_018qau54uNoQKzfkESWXhUja`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "c66eba9d-46c1-4552-80df-19d4dbb010d7",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "We added an explanation in Appendix B (§app:uncertainty)",
    "newString": "We added an explanation in Appendix D (§app:uncertainty)",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 149,
        "oldLines": 7,
        "newStart": 149,
        "newLines": 7,
        "lines": [
          " ",
          " **Concern**: Shorter temporal windows producing higher C% is counterintuitive.",
          " ",
          "-**Response**: We added an explanation in Appendix B (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*",
          "+**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 43_

<details open><summary>🔧 Tool call — Edit · `toolu_01S4tHJYVfswpV5RzELHN3wD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "*(Revised in paper, Appendix B)*",
  "new_string": "*(Revised in paper, Appendix D)*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "c093977e-2c7c-46f2-8820-6fa3aa71ae19",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AiV5h64UoseZ6vugGE2kSU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 38870,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-23T05:11:54.660Z_

<details><summary>↩ Tool result · `toolu_01S4tHJYVfswpV5RzELHN3wD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "061c5612-36ef-4c95-8f0d-b89aa8ffc2fa",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "*(Revised in paper, Appendix B)*",
    "newString": "*(Revised in paper, Appendix D)*",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 149,
        "oldLines": 7,
        "newStart": 149,
        "newLines": 7,
        "lines": [
          " ",
          " **Concern**: Shorter temporal windows producing higher C% is counterintuitive.",
          " ",
          "-**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix B)*",
          "+**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 45_

<details open><summary>🔧 Tool call — Edit · `toolu_01CcJB3e7kctNN6i336Tkc8N`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "error in Appendix F (§app:rank_reversal)",
  "new_string": "error in Appendix J (§app:rank_reversal)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "6769e97c-6761-4687-86a4-8244666dd4ba",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KtLfv7KWyVhJnMbMAqfPz7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 231,
      "cache_read_input_tokens": 39107,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 231
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 46 · 2026-05-23T05:11:57.465Z_

<details><summary>↩ Tool result · `toolu_01CcJB3e7kctNN6i336Tkc8N`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "4b446626-bf73-49f0-8bba-a40e99be8319",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "error in Appendix F (§app:rank_reversal)",
    "newString": "error in Appendix J (§app:rank_reversal)",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 172,
        "oldLines": 7,
        "newStart": 172,
        "newLines": 7,
        "lines": [
          " ",
          " ### [DATA-1] Rank-Bucket Data Error",
          " ",
          "-During internal review, we identified an error in Appendix F (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*",
          "+During internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 47_

<details open><summary>🔧 Tool call — Edit · `toolu_01G5661R9ZW2CxRRPC7iQaB8`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "*(Corrected in paper, Appendix F)*",
  "new_string": "*(Corrected in paper, Appendix J)*"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "2217210d-220c-48ce-8de0-53963214e366",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01F4MYNgYEfja2c34eAzy43M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 237,
      "cache_read_input_tokens": 39338,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 237
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 48 · 2026-05-23T05:11:59.824Z_

<details><summary>↩ Tool result · `toolu_01G5661R9ZW2CxRRPC7iQaB8`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "4121ceab-b496-445d-aafb-e5a9548e5b79",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "*(Corrected in paper, Appendix F)*",
    "newString": "*(Corrected in paper, Appendix J)*",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 172,
        "oldLines": 7,
        "newStart": 172,
        "newLines": 7,
        "lines": [
          " ",
          " ### [DATA-1] Rank-Bucket Data Error",
          " ",
          "-During internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix F)*",
          "+During internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*",
          " ",
          " ---",
          " "
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 49_

Now fix the summary table entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "5a431081-746c-4cef-a6ea-4d2d63d9e8fe",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpJrMimaozUZ8LR77LnfPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 39575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 50_

<details open><summary>🔧 Tool call — Edit · `toolu_01KJ95NoqZKFr4qNdL9T4yhJ`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "Revised (§4.2, Appendix C, Table A.3)",
  "new_string": "Revised (§4.2, Appendix C, Table 9)"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "dd6ae90f-fe8e-4938-b680-6847402c98e7",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XpJrMimaozUZ8LR77LnfPs",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 233,
      "cache_read_input_tokens": 39575,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 233
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 51 · 2026-05-23T05:12:03.307Z_

<details><summary>↩ Tool result · `toolu_01KJ95NoqZKFr4qNdL9T4yhJ`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "dd2a932f-f46f-42c0-80c1-fe1b825078f1",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "Revised (§4.2, Appendix C, Table A.3)",
    "newString": "Revised (§4.2, Appendix C, Table 9)",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 180,
        "oldLines": 7,
        "newStart": 180,
        "newLines": 7,
        "lines": [
          " ",
          " | ID | Issue | Type | Status |",
          " |----|-------|------|--------|",
          "-| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table A.3) |",
          "+| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |",
          " | R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |",
          " | R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |",
          " | R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 52_

<details open><summary>🔧 Tool call — Edit · `toolu_01UmnUDZHWYDYhhtcnCaN1B4`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |",
  "new_string": "| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "c989cbf5-8120-470b-a158-f75263746ece",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YMoXtcyRacD8XkPnkkVP8A",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 250,
      "cache_read_input_tokens": 39808,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 250
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-23T05:12:06.846Z_

<details><summary>↩ Tool result · `toolu_01UmnUDZHWYDYhhtcnCaN1B4`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "5c137a37-71f9-4c8d-8da8-b5a0f6258743",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |",
    "newString": "| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 181,
        "oldLines": 7,
        "newStart": 181,
        "newLines": 7,
        "lines": [
          " | ID | Issue | Type | Status |",
          " |----|-------|------|--------|",
          " | R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |",
          "-| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix D) |",
          "+| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |",
          " | R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |",
          " | R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |",
          " | R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 54_

<details open><summary>🔧 Tool call — Edit · `toolu_01C4hCLebthZhvyeazCbmSug`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |",
  "new_string": "| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "1d171454-4802-45e8-a36a-bb3ba463cfa4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WdKfXdPxSSYnaLs7swLtW1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 267,
      "cache_read_input_tokens": 40058,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 267
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 55 · 2026-05-23T05:12:10.479Z_

<details><summary>↩ Tool result · `toolu_01C4hCLebthZhvyeazCbmSug`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "6b175b27-3db0-40a5-9f6e-c6a8faff366b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |",
    "newString": "| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 186,
        "oldLines": 7,
        "newStart": 186,
        "newLines": 7,
        "lines": [
          " | R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |",
          " | R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |",
          " | R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |",
          "-| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, E) |",
          "+| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |",
          " | R1-Q2 | Singleton handling | Question | Answered (Appendix C) |",
          " | R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |",
          " | R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 56_

<details open><summary>🔧 Tool call — Edit · `toolu_01KnUZk8LvgeMp8tjjbybc6i`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |",
  "new_string": "| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.7) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "a468094a-d6d9-424e-a36a-f079c83bde68",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SGzSDq7XU9fzxWtsKRvGnj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 259,
      "cache_read_input_tokens": 40325,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 259
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 57 · 2026-05-23T05:12:14.381Z_

<details><summary>↩ Tool result · `toolu_01KnUZk8LvgeMp8tjjbybc6i`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "de3cf018-0ed9-4044-b810-16c7e39d502b",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |",
    "newString": "| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.7) |",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 192,
        "oldLines": 7,
        "newStart": 192,
        "newLines": 7,
        "lines": [
          " | R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |",
          " | R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |",
          " | R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |",
          "-| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.6) |",
          "+| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.7) |",
          " | R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |",
          " | R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |",
          " | R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 58_

<details open><summary>🔧 Tool call — Edit · `toolu_01KhrkvsXG3oWawXk6V98Daw`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |",
  "new_string": "| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "859bbd86-08e1-44f6-99f6-5570c790e7d0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019BFKN2dA4VANmiqy2p66Pf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 271,
      "cache_read_input_tokens": 40584,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 271
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 59 · 2026-05-23T05:12:17.890Z_

<details><summary>↩ Tool result · `toolu_01KhrkvsXG3oWawXk6V98Daw`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "46e92a85-c2d9-4852-b273-0d7dc5758855",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |",
    "newString": "| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.7) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 197,
        "oldLines": 7,
        "newStart": 197,
        "newLines": 7,
        "lines": [
          " | R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |",
          " | R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |",
          " | R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |",
          "-| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix B) |",
          "+| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |",
          " | MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |",
          " | DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |",
          " | — | Unused bib entries (7) | Proactive | Cleaned |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 60_

<details open><summary>🔧 Tool call — Edit · `toolu_01A9frUoEVSMPv5N1fQP1LgS`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |",
  "new_string": "| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix J) |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "781b715c-a82b-494a-8ba9-a482ceff1e87",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RwRPMRe8vmAupa6hBFbqqX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 367,
      "cache_read_input_tokens": 40855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 367
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-23T05:12:21.004Z_

<details><summary>↩ Tool result · `toolu_01A9frUoEVSMPv5N1fQP1LgS`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "faf8cd62-a63f-40be-ab75-51e5f2fbcf06",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |",
    "newString": "| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix J) |",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.7) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 199,
        "oldLines": 7,
        "newStart": 199,
        "newLines": 7,
        "lines": [
          " | R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |",
          " | R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |",
          " | MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |",
          "-| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix F) |",
          "+| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix J) |",
          " | — | Unused bib entries (7) | Proactive | Cleaned |",
          " ",
          " ### New Experimental Evidence"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Tool call

_source line 62_

<details open><summary>🔧 Tool call — Edit · `toolu_014cYPtCfa2yGEyXZkdwEVJN`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "old_string": "| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |",
  "new_string": "| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table 5 |"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "8205f7f4-8857-4a09-bc75-7e7db611bc4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UwCggLPnh9buDDHF1GDaFe",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 263,
      "cache_read_input_tokens": 41222,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 263
      },
      "output_tokens": 72,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 63 · 2026-05-23T05:12:25.135Z_

<details><summary>↩ Tool result · `toolu_014cYPtCfa2yGEyXZkdwEVJN`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "27d686c4-7af3-4eae-be61-b713e3956e71",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
    "oldString": "| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |",
    "newString": "| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table 5 |",
    "originalFile": "# Author Response\n\nWe thank the reviewers for their thorough and constructive feedback. Below we address each concern with specific revisions and new experimental evidence. All paper modifications reference the revised manuscript; appendix additions are marked with section numbers.\n\n---\n\n## Reviewer 1\n\n### [R1-W1] DEFF Correction Range (13.5%–29.2%) and Size-Stratified Analysis\n\n**Concern**: The two-fold gap between simple-mean DEFF (29.2%) and weighted-mean DEFF (13.5%) leaves the headline number's uncertainty underestimated. The reviewer requested size-stratified ICC evidence and a sensitivity curve.\n\n**Response**: We added a size-stratified DEFF analysis (Table 9 in Appendix C, revised §4.2). The key finding directly addresses the reviewer's concern:\n\n| Tier | Families | Mean size | ICC | DEFF | Adj. C% |\n|------|----------|-----------|-----|------|---------|\n| 2–10 | 9 | 5.3 | 0.246 | 2.07 | 31.3% |\n| 11–50 | 11 | 22.1 | 0.226 | 5.78 | 24.6% |\n| 51–200 | 8 | 91.4 | 0.137 | 13.34 | 13.7% |\n| >200 | 2 | 431.0 | 0.082 | 36.11 | 9.0% |\n\nTier-level ICC *decreases* monotonically from 0.246 (small families) to 0.082 (mega-families), confirming that mega-families are internally heterogeneous. The weighted-mean variant's effective cluster size ($\\bar{m}=254$) implies each family member is functionally identical — the stratified analysis shows this is empirically false. The conservative 13.5% bound is driven entirely by the two mega-families (Mistral, Llama-3), while small families (where ICC is highest) contribute negligible DEFF correction (Adj. C% = 31.3%).\n\nWe now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n\n**Family definition sensitivity** (R1-Q1): Merging sub-generations (e.g., Llama-2 + Llama-3 into coarse families; 22 families) changes C% by ≤0.3 pp. Within-family similarity shows no dependence on family size (Spearman $\\rho = -0.009$, $p = 0.96$; Appendix H).\n\n**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n\n### [R1-W2] Graduated De-Duplication Definition\n\n**Concern**: De-duplication was one of three convergence methods but was never formally defined.\n\n**Response**: We added a formal definition in Appendix I (§app:dedup_k): for each value of $K$ (max models retained per family), $K$ members are sampled uniformly at random; remaining family members are excluded from both reference and focal cohorts, and MH-DIF is recomputed on the reduced sample (5 independent draws per $K$; $K = \\text{all}$ is deterministic).\n\nC% increases monotonically from 0.3% ($K=1$) to 31.3% ($K=\\text{all}$). At each fixed $K$, within-$K$ variance is negligible (SD < 1.5 pp), confirming the signal scales with statistical power rather than within-family redundancy. At $K=20$, C% = 19.7% $\\pm$ 0.9% ($N \\approx 450$); the gap from 31.3% reflects reduced power, not reduced bias. We revised the convergence argument from three methods to two (simple-mean DEFF 29.2% + cluster bootstrap lower bound 26.7%), as the de-duplication result at $K=20$ (19.7%) reflects a power reduction rather than independent validation. *(Revised in paper, §4.2 + Appendix I)*\n\n### [R1-W3] Semi-Synthetic ΔTPR Generalizability\n\n**Concern**: Binary response flipping is a worst-case uniform pattern; the real contamination mechanism may be difficulty-dependent, making ΔTPR = +0.508 an upper bound.\n\n**Response**: We now provide two complementary analyses beyond binary flipping:\n\n1. **Difficulty-dependent injection** (Appendix A, §app:mixed_mechanism): Three injection schemes (uniform, difficulty-dependent, mixed) produce distinguishable $\\rho$ signatures (capability-like: +0.77 vs. contamination-like: −0.52; zero seed overlap). This confirms the semi-synthetic framework can differentiate contamination mechanisms, though mapping to real-data mechanisms requires further work.\n\n2. **Mixed-mechanism semi-synthetic analysis** (new experiment E3; §app:mixed_mechanism): Scheme D applies difficulty-dependent injection to base models and uniform injection to instruct models. Across 20 seeds, it reproduces the overall $\\rho$ ($-0.676 \\pm 0.005$ vs. observed $-0.597$) and direction reversal ($\\chi^2 = 634 \\pm 184$ vs. observed 562.7), but cannot match the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$, a 3.8x gap). This residual gap persists across all tested parameters.\n\nThe revised §4.5 now explicitly states that binary flipping ΔTPR is an upper-bound estimate, while the new analyses extend the framework to non-uniform mechanisms. *(Revised in paper, §4.5 + §5.1 + Appendix A)*\n\n### [R1-W4] Causal Ambiguity and Framing Tension\n\n**Concern**: DIF cannot distinguish contamination from legitimate capability evolution; the four exclusion arguments are of uneven strength; framing oscillates between contamination critique and psychometric audit.\n\n**Response**: We have substantially strengthened the causal discussion in §5.1 with two new analyses (see also detailed response under R2-W1/R2-Q1):\n\n1. **Logistic regression** (new experiment E2; Appendix A, §app:interaction): The difficulty $\\times$ model-type interaction is significant (OR = 4.75, $p < 10^{-188}$; $N = 8{,}585$ items). Controlling for difficulty, model type remains a strong independent predictor of DIF direction (OR = 4.24, $p < 10^{-225}$). A pure difficulty-dependent contamination account cannot explain why base and instruct models show opposite DIF direction patterns on the same items.\n\n2. **Mixed-mechanism simulation** (new experiment E3; Appendix A, §app:mixed_mechanism): Even the best-fitting mixed injection scheme cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap), suggesting instruct-model DIF is at least partially driven by non-contamination mechanisms (e.g., alignment-induced capability shifts).\n\nWe revised the framing throughout: Contribution 1 is now positioned as \"empirical demonstration that global exposure and differential functioning are orthogonal constructs\" rather than \"ground truth meta-critique.\" §5.1 explicitly presents difficulty-dependent contamination as an alternative explanation and uses the base-vs-instruct decomposition as a partial (not complete) rebuttal. The paper's position is that DIF detects *that* items function differently, not *why* — the three mechanisms (contamination, capability evolution, training methodology) are non-exclusive and our evidence constrains but does not fully resolve the ambiguity. *(Revised in paper, §1 + §5.1)*\n\n### [R1-W6] K=10 Non-Uniform DIF Leakage\n\n**Concern**: The K=10 non-monotonic peak (35.9%) may reflect non-uniform DIF captured by finer stratification, undermining uniform DIF stability across K.\n\n**Response**: We strengthened the caveat in §4.2: the K=10 peak \"may reflect MH's partial sensitivity to non-uniform DIF at finer stratifications, rather than more precise uniform DIF estimation.\" C% is stable across $K \\geq 5$ (31.3%–35.9%); the non-monotonicity at K=10 is interpretive, not methodological. We recommend $K=5$ as the most conservative standard choice. *(Revised in paper, §4.2)*\n\n### [R1-W10] 1:1 Matching Details\n\n**Concern**: Matching method, balance check, and sample size impact were not reported.\n\n**Response**: We added full matching details to Appendix A (§app:method_details): 1:1 nearest-neighbor matching with caliper of 0.02 on normalized accuracy ($\\approx 0.14$ SD). Balance verified by Cohen's $d = -0.17$ on matched pairs ($N = 638$ per group), confirming minimal residual ability confounding. *(Revised in paper, Appendix A)*\n\n---\n\n## Reviewer 2\n\n### [R2-W1/W4] Causal Ambiguity and DIF Audit Protocol\n\n**Concern**: DIF cannot distinguish contamination from capability evolution; the audit protocol (Monitor/Flag/Act) does not differentiate DIF causes; framing in Introduction vs. Discussion is inconsistent.\n\n**Response**: We agree that causal disambiguation is beyond MH-DIF's scope, and we have revised the framing accordingly:\n\n1. **Framing alignment**: Contribution 1 is reframed from \"ground truth meta-critique\" to \"empirical demonstration that global exposure and differential functioning are orthogonal constructs.\" All \"category error\" and \"meta-critique\" language has been removed. The Introduction and Discussion now use consistent terminology. *(Revised in paper, §1 + §5.1)*\n\n2. **Strengthened exclusion arguments**: Two new experiments directly address the causal gap:\n   - E2 (logistic regression): OR = 4.75 for difficulty $\\times$ model-type interaction ($p < 10^{-188}$), with model type remaining a strong independent predictor after controlling for difficulty (OR = 4.24, $p < 10^{-225}$). This is inconsistent with pure difficulty-dependent contamination.\n   - E3 (mixed-mechanism simulation): The best-fitting scheme reproduces the overall $\\rho$ and $\\chi^2$ reversal but cannot match the instruct gradient (simulated $-0.302$ vs. observed $-0.079$; 3.8x gap across all tested parameters).\n\n3. **Audit protocol scope**: §5.2 now clarifies that the three-tier protocol is designed for *measurement maintenance* (detecting when items function differently) rather than *causal diagnosis*. The action levels address the practical consequence (ranking distortion) regardless of cause: even if DIF reflects genuine capability change, items that function differently across cohorts compromise cross-temporal comparability. *(Revised in paper, §5.1 + §5.2)*\n\n### [R2-W2] Ground Truth Meta-Critique Framing\n\n**Concern**: \"Category error in prevailing validation methodology\" is circular; should reframe as empirical finding.\n\n**Response**: Contribution 1 is now \"Orthogonal constructs: DIF flags and web-overlap contamination labels capture empirically independent signals (Jaccard = 0.206, enrichment = 0.964).\" All \"category error\" language removed. *(Revised in paper, §1)*\n\n### [R2-W3] Methodological Novelty\n\n**Concern**: MH-DIF is a standard method; contributions are primarily empirical.\n\n**Response (rebuttal-only)**: We acknowledge that MH-DIF is an established method (Holland & Thayer, 1988) and do not claim methodological novelty in the DIF procedure itself. Our contributions are: (1) the empirical finding that global exposure and differential functioning are orthogonal constructs, which has direct implications for contamination detection validation; (2) the cross-subject matching adaptation with its constructive ΔFPR = 0 guarantee; and (3) the largest-scale temporal DIF audit in LLM evaluation (5,227 models × 12,508 items × 6 benchmarks). We believe this combination of empirical scale, surprising negative results, and practical protocol constitutes a meaningful contribution to the LLM evaluation community, consistent with EMNLP's emphasis on empirical findings.\n\n### [R2-Q1/Q3] Difficulty-Dependent Contamination as Alternative Explanation\n\n**Concern**: The difficulty-direction interaction ($\\rho = -0.597$) could be explained by difficulty-dependent contamination: easy items uniformly contaminated (DIF-A), hard items differentially contaminated (DIF-C).\n\n**Response**: We now explicitly discuss this alternative in §5.1 and provide two pieces of evidence that constrain (though do not eliminate) it:\n\n1. **Base-vs-instruct direction reversal**: Base models ($N=1{,}409$) are 60.1% reference-favoring with strong difficulty gradient ($\\rho = -0.570$), while instruct models ($N=478$) are 65.6% focal-favoring with near-zero gradient ($\\rho = -0.079$; $\\chi^2 = 562.7$, $p < 10^{-124}$). A pure difficulty-dependent contamination account predicts identical DIF direction for both model types on the same items — the observed reversal is inconsistent with this prediction.\n\n2. **Mixed-mechanism simulation** (E3): Even when applying difficulty-dependent injection to base models and uniform injection to instruct models simultaneously, the simulation cannot reproduce the near-zero instruct gradient (simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$; 3.8x gap). This residual gap suggests instruct-model DIF is at least partially driven by non-contamination mechanisms.\n\nWe emphasize that this is a *partial* rebuttal: it constrains the space of viable explanations but does not fully resolve the causal question. §5.1 now frames the evidence as \"arguing against a *pure* difficulty-dependent contamination account\" rather than ruling out contamination entirely. *(Revised in paper, §5.1 + Appendix A)*\n\n### [R2-W6] MMLU Item Quality Exclusion Evidence\n\n**Concern**: Gema enrichment CI upper bound of 1.27 is compatible with a 27% inflation; \"ruled out\" is too strong.\n\n**Response**: We revised the wording from \"ruled out\" to \"no enrichment detected\" (Gema et al. enrichment = 0.92; $p = 0.23$). We agree that absence of evidence is not evidence of absence, and the revised text reflects this epistemic status. *(Revised in paper, §5.1)*\n\n### [R2-W7] GSM1K Exploratory Analysis Weight\n\n**Concern**: N=33, p=0.036 is not robust; the analysis receives disproportionate framing weight.\n\n**Response**: We reduced the GSM1K analysis to a single sentence in §4.7 and explicitly marked it as \"an exploratory cross-benchmark signal... but the small sample requires replication.\" The correlation ($r = -0.478$, $p = 0.005$, $N = 33$) is presented as suggestive, not confirmatory. *(Revised in paper, §4.7)*\n\n### [R2-W8] enlargethispage Format\n\n**Concern**: `\\enlargethispage*{14\\baselineskip}` ($\\approx$2.5 inches) risks AC format rejection.\n\n**Response**: Reduced to $\\leq 4$`\\baselineskip` in §4.3 and $10$`\\baselineskip` in §5. The Discussion section retains moderate expansion due to the new E2/E3 content, but stays within safe typographic margins. *(Revised in paper)*\n\n### [R2-W9] Abstract Scope Mismatch\n\n**Concern**: \"5,227 models\" is the MMLU count; GSM8K uses 6,702.\n\n**Response**: Abstract now reads \"5,227 MMLU models.\" *(Revised in paper, Abstract)*\n\n### [R2-Q3/Q6] ≥500 Model Threshold\n\n**Concern**: Power analysis shows $N \\geq 80$ per cohort suffices; ≥500 total models is overly conservative.\n\n**Response**: We softened the threshold in §5.2: \"≥500 models\" is presented as a practical guideline for the standard $K=5$ design, with the explicit note that \"smaller corpora may suffice with fewer strata.\" New experiment E1 confirms this:\n\n$K=3$ and $K=5$ yield near-identical detection power: TPR difference $< 0.02$ across all 30 conditions (within Monte Carlo noise). At $N \\geq 80$, $K=3$ achieves TPR = 0.454–0.571, AUC = 0.905 at $N=100$ (Table 5). Researchers with smaller model corpora can therefore use $K=3$ strata with no appreciable power loss. *(Revised in paper, §5.2 + Appendix A, Table 5)*\n\n### [R2-Q5] Half-Year C% (34.4%) Higher Than Annual (31.3%)\n\n**Concern**: Shorter temporal windows producing higher C% is counterintuitive.\n\n**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n\n---\n\n## Meta-Reviewer\n\n### [MR-1] Missing References\n\n**Concern**: Three references missing — Kamata & Binici (2003), Alzahrani et al. (2024), MMLU-Pro (Wang et al., 2024).\n\n**Response**: We verified all three citations:\n- **Alzahrani et al. (2024)** — already in bibliography (cited in Related Work).\n- **MMLU-Pro (Wang et al., 2024)** — already in bibliography (cited in §2).\n- **Kamata & Binici (2003)** — an unpublished doctoral thesis on random-effect DIF models. We considered adding it but opted not to, as the work was never published in a peer-reviewed venue. Our DEFF correction follows the Rao & Scott (1992) approach, which is the standard survey-sampling reference for design effects in clustered data.\n\nAdditionally, we cleaned 7 unused bibliography entries to improve reference hygiene. *(Revised in paper, references)*\n\n---\n\n## Additional Corrections\n\n### [DATA-1] Rank-Bucket Data Error\n\nDuring internal review, we identified an error in Appendix J (§app:rank_reversal): the reversal rate for $\\Delta\\text{rank} \\in [50, 200)$ was incorrectly reported as 6.3% (no source); the correct value from the analysis is 15.1%. We also added the missing $[200, 500)$ bucket (4.0%). The corrected distribution is: 35.2% ($< 50$), 15.1% ($[50, 200)$), 4.0% ($[200, 500)$), 0.6% ($[500, 1000)$), 0.0% ($> 1000$). *(Corrected in paper, Appendix J)*\n\n---\n\n## Summary of Changes\n\n| ID | Issue | Type | Status |\n|----|-------|------|--------|\n| R1-W1 | DEFF correction range + size-stratified analysis | Must-Fix | Revised (§4.2, Appendix C, Table 9) |\n| R1-W2 | Graduated de-duplication definition | Must-Fix | Revised (Appendix I) |\n| R1-W3 | Semi-synthetic ΔTPR generalizability | Should-Fix | Revised (§4.5, §5.1, Appendix A) + new E2/E3 |\n| R1-W4 | Causal ambiguity and framing | Must-Fix | Revised (§1, §5.1) + new E2/E3 |\n| R1-W6 | K=10 NUDIF caveat | Should-Fix | Revised (§4.2) |\n| R1-W10 | 1:1 matching details | Should-Fix | Revised (Appendix A) |\n| R1-Q1 | Family definition sensitivity | Question | Answered (Appendix C, H) |\n| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n| R2-W1/W4 | Causal ambiguity + audit protocol | Must-Fix | Revised (§5.1, §5.2) + new E2/E3 |\n| R2-W2 | Ground truth meta-critique framing | Should-Fix | Revised (§1) |\n| R2-W3 | Methodological novelty | Should-Fix | Rebuttal-only |\n| R2-W6 | Item quality exclusion wording | Should-Fix | Revised (§5.1) |\n| R2-W7 | GSM1K exploratory weight | Nice-to-Have | Revised (§4.7) |\n| R2-W8 | enlargethispage format | Nice-to-Have | Revised (§4.3, §5) |\n| R2-W9 | Abstract scope | Nice-to-Have | Revised (Abstract) |\n| R2-Q1 | Difficulty-dependent contamination | Question | Answered (§5.1, Appendix A) + new E2/E3 |\n| R2-Q3 | ≥500 threshold justification | Question | Revised (§5.2) + new E1 |\n| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |\n| MR-1 | Missing references | Nice-to-Have | Verified; 2/3 already present |\n| DATA-1 | Rank-bucket data error | Proactive | Corrected (Appendix J) |\n| — | Unused bib entries (7) | Proactive | Cleaned |\n\n### New Experimental Evidence\n\n| Label | Experiment | Key Result | Location |\n|-------|-----------|------------|----------|\n| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |\n| E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |\n| E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |\n",
    "structuredPatch": [
      {
        "oldStart": 206,
        "oldLines": 6,
        "newStart": 206,
        "newLines": 6,
        "lines": [
          " ",
          " | Label | Experiment | Key Result | Location |",
          " |-------|-----------|------------|----------|",
          "-| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table A.2 |",
          "+| E1 | K=3 vs K=5 power simulation | TPR diff < 0.02; AUC = 0.905 at N=100 | Table 5 |",
          " | E2 | Difficulty × model-type logistic regression | OR = 4.75, $p < 10^{-188}$; OR = 4.24, $p < 10^{-225}$ | §app:interaction |",
          " | E3 | Mixed-mechanism semi-synthetic simulation | Simulated $\\rho_\\text{instruct} = -0.302$ vs. observed $-0.079$ (3.8x gap) | §app:mixed_mechanism |"
        ]
      }
    ],
    "userModified": false,
    "replaceAll": false
  }
}
```

</details>

---

### Assistant

_source line 64_

All replacements done. Now let me verify no stale references remain.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "f94a2b0f-8e02-4443-af7d-11271a9c23b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaUR9ZBitbMQjBKTbFoabu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 41485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool call

_source line 65_

<details open><summary>🔧 Tool call — Grep · `toolu_0187mUdEzgUL6qJKNcLG2L38`</summary>

```json
{
  "pattern": "Table A\\.",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "35d416b0-42cb-42ec-8e74-25649ce49c7b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaUR9ZBitbMQjBKTbFoabu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 41485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 66 · 2026-05-23T05:12:29.856Z_

<details><summary>↩ Tool result · `toolu_0187mUdEzgUL6qJKNcLG2L38`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "783e1f63-446d-4952-a29a-c37312fb8711",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Tool call

_source line 67_

<details open><summary>🔧 Tool call — Grep · `toolu_01VnjAWxJ6wsWtz9tzu4S31i`</summary>

```json
{
  "pattern": "Appendix [B-F][ )]",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "3d944f17-2cdd-4bd0-9049-e3a414d323cc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaUR9ZBitbMQjBKTbFoabu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 41485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-23T05:12:31.269Z_

<details><summary>↩ Tool result · `toolu_01VnjAWxJ6wsWtz9tzu4S31i`</summary>

```text
24:We now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*
28:**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\text{ref} + N_\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*
152:**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*
190:| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |
200:| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "7659edb2-961f-464f-9090-6ac0195d9cc7",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "24:We now report the full range [13.5%, 29.2%] as power uncertainty (revised §4.2) and adopt ~27–29% as the primary estimate supported by two convergent methods (simple-mean DEFF 29.2%, cluster bootstrap lower bound 26.7%). Even the conservative 13.5% exceeds the random-split baseline by 75x. *(Revised in paper, §4.2 + Appendix C)*\n28:**Singleton handling** (R1-Q2): Of the 5,227 models, 3,343 lack family assignments; these are retained in DIF analysis but excluded from DEFF/ICC estimation. Within the temporal DIF cohorts ($N_\\text{ref} + N_\\text{foc} = 1{,}887$), 1,884 (99.8%) belong to identified families with $\\geq 2$ members, so DEFF estimates cover nearly the full analysis population. *(Clarified in Appendix C)*\n152:**Response**: We added an explanation in Appendix D (§app:uncertainty): shorter temporal windows yield fewer models that span both half-year periods, producing reference and focal groups with less overlapping ability distributions and consequently inflated DIF detection rates. The higher C% reflects more polarized cohort composition, not greater item instability. *(Revised in paper, Appendix D)*\n190:| R1-Q2 | Singleton handling | Question | Answered (Appendix C) |\n200:| R2-Q5 | Half-year C% > annual | Question | Answered (Appendix D) |",
    "numLines": 5
  }
}
```

</details>

---

### Tool call

_source line 69_

<details open><summary>🔧 Tool call — Grep · `toolu_01CuAVVeFVYc7wnWcg9JZt6G`</summary>

```json
{
  "pattern": "§4\\.6",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/projects/irt_equated_bench_regen/artifacts/response_letter_draft.md",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "baa85df0-fe96-4585-924a-242c6c5b8069",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PaUR9ZBitbMQjBKTbFoabu",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 302,
      "cache_read_input_tokens": 41485,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 302
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Tool result

_source line 70 · 2026-05-23T05:12:31.996Z_

<details><summary>↩ Tool result · `toolu_01CuAVVeFVYc7wnWcg9JZt6G`</summary>

```text
No matches found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "27c1f9a9-f228-4768-9f09-cea921b7d0fc",
  "tool_use_result": {
    "mode": "content",
    "numFiles": 0,
    "filenames": [],
    "content": "",
    "numLines": 0
  }
}
```

</details>

---

### Assistant

_source line 71_

No stale references remain. The remaining "Appendix C" references are correct (`app:deff` = Appendix C) and the "Appendix D" references now correctly point to `app:uncertainty` = Appendix D.

**17 replacements made across the file:**

| # | Line | Old | New |
|---|------|-----|-----|
| 1 | 13 | Table A.3 | Table 9 |
| 2 | 26 | Appendix E | Appendix H |
| 3 | 34 | Appendix D (§app:dedup_k) | Appendix I |
| 4 | 36 | Appendix D (in revision note) | Appendix I |
| 5 | 126 | §4.6 (GSM1K sentence) | §4.7 |
| 6 | 126 | §4.6 (revision note) | §4.7 |
| 7 | 146 | Table A.2 (×2 in same line) | Table 5 |
| 8 | 152 | Appendix B (§app:uncertainty) | Appendix D |
| 9 | 152 | Appendix B (revision note) | Appendix D |
| 10 | 175 | Appendix F (§app:rank_reversal) | Appendix J |
| 11 | 175 | Appendix F (revision note) | Appendix J |
| 12 | 183 | Table A.3 (summary table) | Table 9 |
| 13 | 184 | Appendix D (summary table) | Appendix I |
| 14 | 189 | Appendix E (summary table) | Appendix H |
| 15 | 195 | §4.6 (summary table) | §4.7 |
| 16 | 200 | Appendix B (summary table) | Appendix D |
| 17 | 202 | Appendix F (summary table) | Appendix J |
| 18 | 209 | Table A.2 (experiment table) | Table 5 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "uuid": "94635eae-d893-4a3e-950a-2af48ee69d31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DBeHNjs7xL6dnQ3GooFW4y",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 41787,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 849
      },
      "output_tokens": 1,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null,
    "context_management": null
  }
}
```

</details>

---

### Task result

_source line 72_

No stale references remain. The remaining "Appendix C" references are correct (`app:deff` = Appendix C) and the "Appendix D" references now correctly point to `app:uncertainty` = Appendix D.

**17 replacements made across the file:**

| # | Line | Old | New |
|---|------|-----|-----|
| 1 | 13 | Table A.3 | Table 9 |
| 2 | 26 | Appendix E | Appendix H |
| 3 | 34 | Appendix D (§app:dedup_k) | Appendix I |
| 4 | 36 | Appendix D (in revision note) | Appendix I |
| 5 | 126 | §4.6 (GSM1K sentence) | §4.7 |
| 6 | 126 | §4.6 (revision note) | §4.7 |
| 7 | 146 | Table A.2 (×2 in same line) | Table 5 |
| 8 | 152 | Appendix B (§app:uncertainty) | Appendix D |
| 9 | 152 | Appendix B (revision note) | Appendix D |
| 10 | 175 | Appendix F (§app:rank_reversal) | Appendix J |
| 11 | 175 | Appendix F (revision note) | Appendix J |
| 12 | 183 | Table A.3 (summary table) | Table 9 |
| 13 | 184 | Appendix D (summary table) | Appendix I |
| 14 | 189 | Appendix E (summary table) | Appendix H |
| 15 | 195 | §4.6 (summary table) | §4.7 |
| 16 | 200 | Appendix B (summary table) | Appendix D |
| 17 | 202 | Appendix F (summary table) | Appendix J |
| 18 | 209 | Table A.2 (experiment table) | Table 5 |

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 138586,
  "duration_api_ms": 139302,
  "num_turns": 29,
  "stop_reason": "end_turn",
  "session_id": "a375251f-45a3-407a-81ad-20fbd87cbe8e",
  "total_cost_usd": 0.82144275,
  "usage": {
    "input_tokens": 27,
    "cache_creation_input_tokens": 30795,
    "cache_read_input_tokens": 915706,
    "output_tokens": 6793,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 30795,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 540,
        "cache_read_input_tokens": 41787,
        "cache_creation_input_tokens": 849,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 849
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1076,
      "outputTokens": 17,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001161,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 27,
      "outputTokens": 6793,
      "cacheReadInputTokens": 915706,
      "cacheCreationInputTokens": 30795,
      "webSearchRequests": 0,
      "costUSD": 0.82028175,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "86c893e5-508f-4b48-b037-6601c7ffdeb3"
}
```

</details>

---
