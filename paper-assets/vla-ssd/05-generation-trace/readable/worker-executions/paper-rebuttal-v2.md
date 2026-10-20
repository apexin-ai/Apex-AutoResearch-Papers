# paper rebuttal v2

**Instruction Routing in Fine-Tuned Vision-Language-Action Models: A Cross-Architecture Analysis** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 11
- **Recorded user turns:** 0
- **Tool calls:** 2
- **Original source:** `logs/workers/worker_paper_rebuttal_v2_20260525T200245.log`
- **Structured JSON:** [`e7e9b264b7fa009a8c17.json`](../../sessions/e7/e7e9b264b7fa009a8c17.json)

## Before a recorded user message

11 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd",
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
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
  "uuid": "d73df828-12ca-4359-9c20-6603574133d9",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-15-projects-vla-ssd/memory/"
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
    "resetsAt": 1779756000,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "666e96b1-58cf-48de-a118-6871be29ba62",
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me read the v1 rebuttal file first, then make the required modifications to create v2.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "3a4eec67-dc51-4389-8c6e-ac07aa35d951",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2HhmnvpbfnuhAXvAJgDtj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12835,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12835
      },
      "output_tokens": 23,
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

<details open><summary>🔧 Tool call — Read · `toolu_01SohcKxtZd3rbk22iPXDSwX`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v1.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "17989c90-b7d9-400c-be8f-d2bbf3ec27de",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01C2HhmnvpbfnuhAXvAJgDtj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 12835,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12835
      },
      "output_tokens": 23,
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

_source line 6 · 2026-05-25T20:02:59.349Z_

<details><summary>↩ Tool result · `toolu_01SohcKxtZd3rbk22iPXDSwX`</summary>

```text
1	# Anticipated Reviewer Response Letter
2	
3	We thank the reviewers for their careful evaluation. Below we address six anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.
4	
5	---
6	
7	## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)
8	
9	The sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.
10	
11	We attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. [2026] similarly document closed-loop difficulties on LIBERO). This negative result is reported in Appendix §A.16 (Extended Discussion: "closed-loop behavioral validation... remains a priority for future work").
12	
13	Regarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix §A.16). The paper explicitly qualifies this as "directionally consistent but underpowered" (§6) and frames it as observational evidence rather than a confirmed causal link.
14	
15	---
16	
17	## Q2: Only validated on LIBERO—how does this generalize?
18	
19	LIBERO (Liu et al. 2023) is the standard evaluation benchmark for VLA fine-tuning studies, used by OpenVLA, TracVLA, NORA, and concurrent work (Fang et al. 2026, Swann et al. 2026). Our evaluation spans **4 task suites** (Goal, Spatial, Object, Long-Horizon) that vary substantially in instruction complexity, object diversity, and planning horizon (§3.1).
20	
21	The stronger generalization argument comes from **cross-architecture consistency**: exit collapse and counterfactual sensitivity replicate across three distinct backbone families—**Llama-2-7B** (32 layers, MHA), **Phi-3-mini** (32 layers, MHA), and **Qwen2.5-VL-3B** (36 layers, GQA)—spanning 3B to 7B parameters with different pretraining corpora and attention mechanisms. The pattern holds despite qualitatively different reference profiles (§4.5, Appendix §A.16): TracVLA reference starts with saturated L1 attention (32/32 heads) while NORA reference starts at 13–14/16. That the same exit-collapse pattern emerges from these divergent starting points is stronger evidence of generality than observing it on multiple benchmarks within a single architecture.
22	
23	We explicitly acknowledge that **flow-matching (π₀) and diffusion-based (Octo) architectures may differ** (§6, Limitations) and list this as a concrete direction for future work. The paper's claims are scoped to causal-decoder VLAs.
24	
25	---
26	
27	## Q3: No closed-loop evaluation (SR=0)—what is the significance of representational analysis?
28	
29	Closed-loop SR=0 is not unique to our work. The VLA community faces well-documented reproducibility challenges: OpenVLA's original release noted sensitivity to hardware and software configurations; Fang et al. (2026) report similar difficulties on LIBERO-CF. Our attempted closed-loop evaluation yielded SR=0/3, which we report transparently rather than omit.
30	
31	**Representational analysis does not require closed-loop success.** This methodological stance has extensive precedent in NLP interpretability: the probing literature (Belinkov 2022, cited in §2) routinely analyzes internal representations without requiring models to achieve SOTA on downstream tasks. Probing measures what information is *accessible* at each layer, independent of whether the full pipeline successfully executes the task end-to-end. Similarly, RSA and attention profiling characterize geometric organization without assuming perfect behavior.
32	
33	The **behavioral correlation (ρ=0.583)** uses *published* success rates from the original papers (Kim et al. 2024; Zheng et al. 2024; Hung et al. 2025), not our own closed-loop evaluations. This leverages community-validated numbers while our contribution focuses on the representational analysis itself.
34	
35	Practically, **ΔR² as a diagnostic metric** has value precisely because it does not require closed-loop evaluation: it can assess whether a VLA checkpoint exhibits healthy representational structure (ΔR² < 0.10 indicates preserved exit structure) without expensive rollout infrastructure (§6, Practical Implications). This makes it a complementary tool to behavioral evaluation, not a substitute.
36	
37	---
38	
39	## Q4: "First cross-architecture decomposition"—basis for this claim? Distinction from Kachaev et al.?
40	
41	The claim (§4.6, line 176: "a first cross-architecture decomposition of VLA instruction routing") is grounded in systematic literature comparison. All prior representational analyses of VLAs target a single architecture:
42	
43	- **Grant et al. (2026)**: visual dominance in a single VLA
44	- **Haon et al. (2025)**: sparse semantic directions in OpenVLA only
45	- **Swann et al. (2026)**: interpretable features, large-scale behavioral but single-architecture representational probing per model
46	- **Buurmeijer et al. (2026)**: low-level motor feature probing in OpenVLA only
47	
48	**Kachaev et al. (2025)** study *visual representation collapse* during VLA fine-tuning—a distinct phenomenon from instruction routing. Their analysis is conducted exclusively on OpenVLA. Our work quantifies a complementary phenomenon (layer-wise action-probe decodability via ΔR²) and critically, **distinguishes training-associated from inherited effects** across three architectures (§2, Concurrent Work paragraph; §4.6). This decomposition—showing that exit collapse is training-associated while L1 attention is inherited—requires cross-architecture comparison by design and is absent from all prior single-architecture studies.
49	
50	The **3×4 matrix** (3 architectures × 4 suites, 10 filled cells; Table 1) with systematic trained/reference comparisons at each cell is structurally unprecedented in the VLA interpretability literature. The claim is hedged with "with this caveat" referring to the probe-vs-causal-reliance distinction stated in the same sentence.
51	
52	---
53	
54	## Q5: NLP controls only use chat fine-tuning—wouldn't a more task-specific NLP control be needed?
55	
56	Chat fine-tuning is the **maximally relevant control** for our hypothesis. The question being tested is: "Is exit collapse a generic artifact of instruction-following fine-tuning, or is it specific to action-oriented (VLA) training?" Chat-finetuned models share the critical property of being **instruction-following systems fine-tuned on the same backbone**, but lack action heads, robot demonstration data, and vision-action grounding. If exit collapse were a generic consequence of fine-tuning a pretrained LM to follow instructions, chat models should exhibit it.
57	
58	Three backbone families were tested (§4.3, Table in Appendix §A.19):
59	- **Llama-2-7b-chat** (OpenVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.001
60	- **Phi-3-mini-4k-instruct** (TracVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000
61	- **Qwen2.5-3B-Instruct** (NORA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000
62	
63	All three produce **perfectly flat R² profiles** (ΔR² = 0.000), contrasting with VLM-to-VLA collapse (ΔR² = 0.156–0.455). A more task-specific NLP control (e.g., code generation, summarization) would be *further* from VLA fine-tuning in training objective—making it a *weaker* control. Chat instruction-tuning is the closest NLP analog to VLA instruction-following; its complete failure to produce exit collapse provides the strongest evidence that the phenomenon is specific to action-grounded training. We note in §6 (Limitations) that NLP controls cover all three backbone families, though the analysis operates at the representation level rather than requiring matched data distributions.
64	
65	---
66	
67	## Q6: Why use effect size thresholds rather than significance testing?
68	
69	With **N=63,228 observations** per cell, traditional null-hypothesis significance testing becomes uninformative: virtually every comparison reaches p < 0.001 regardless of practical magnitude. This is a well-known limitation of p-values in large-sample settings (Wasserstein & Lazar 2016, ASA Statement on Statistical Significance).
70	
71	Our **ΔR² > 0.10 threshold** has dual justification (§3.3, Appendix §A.8):
72	1. **Semantic meaning**: 10% absolute change in explained variance represents a substantive shift in action decodability
73	2. **Robustness**: the threshold is not boundary-sensitive—any value in **(0.097, 0.156)** produces identical grouping (Appendix Table 6). The gap between the largest non-collapse value (0.097, TracVLA Long reference) and smallest collapse value (0.156, TracVLA Spatial trained) spans 0.059, providing a clean separation zone
74	
75	Statistical validation accompanies the effect-size framework:
76	- **Permutation test**: randomly reassigning 9 cells to two groups (10,000 permutations) yields **p=0.008** for the observed min-max gap (Appendix §A.7)
77	- **Bootstrap CIs**: Monte Carlo cross-validation (n=1,000 iterations) with demo-level splitting; VLM-to-VLA CIs lie entirely above zero (lower bounds ≥ 0.09; Table 1)
78	- **Cohen's d** for counterfactual sensitivity (medium-to-large: d=0.45–1.52; §4.4, Table 2)
79	- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix §A.18)
80	
81	This approach aligns with modern statistical best practice: report effect sizes with confidence intervals as primary evidence, use significance tests as supplementary confirmation, and validate threshold robustness via sensitivity analysis.
82	
83	---
84	
85	## Summary of Preemptive Measures Already in the Paper
86	
87	The manuscript includes the following preemptive defenses against anticipated concerns:
88	
89	- **Demo-level splitting** (§3.3): eliminates within-trajectory leakage; reduces R² from 0.7–0.9 to 0.4–0.6, quantifying pseudo-replication inflation
90	- **Threshold robustness analysis** (§3.3, Appendix §A.8): any threshold in (0.097, 0.156) yields identical grouping
91	- **Permutation test** (Appendix §A.7): p=0.008 for VLA-to-VLA vs. VLM-to-VLA separation
92	- **Three NLP controls** (§4.3, Appendix §A.19): all three backbone families tested, all ΔR²=0.000
93	- **Bonferroni correction** (Appendix §A.18): 48/63 tests survive; all 8 core tests remain significant
94	- **Linear probe replication** (Appendix §A.13): consistent with MLP probe patterns, ruling out capacity artifacts
95	- **Explicit metric incommensurability** (§4.4): Cohen's d vs. cosine distance clearly separated; cross-metric ratios explicitly flagged as invalid
96	- **Claim-Evidence figure** (Appendix §A.20, Figure): each finding paired with supporting evidence and acknowledged scope boundary
97	- **Comprehensive Limitations** (§6): N=2 VLM-to-VLA transitions, LIBERO-only, causal-decoder only, open-loop, single checkpoint, underpowered behavioral correlation—all explicitly stated
98	- **Training-type asymmetry disclosure** (§3.1): OpenVLA VLA-to-VLA vs. TracVLA/NORA VLM-to-VLA clearly distinguished throughout
99	- **Concurrent work differentiation** (§2): Fang et al. (behavioral vs. representational), Buurmeijer et al. (motor features vs. instruction routing), Kachaev et al. (visual collapse vs. action decodability)
100	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "d438bd58-c2a5-4942-97d3-c3e1dd679879",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v1.md",
      "content": "# Anticipated Reviewer Response Letter\n\nWe thank the reviewers for their careful evaluation. Below we address six anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.\n\n---\n\n## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)\n\nThe sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.\n\nWe attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. [2026] similarly document closed-loop difficulties on LIBERO). This negative result is reported in Appendix §A.16 (Extended Discussion: \"closed-loop behavioral validation... remains a priority for future work\").\n\nRegarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix §A.16). The paper explicitly qualifies this as \"directionally consistent but underpowered\" (§6) and frames it as observational evidence rather than a confirmed causal link.\n\n---\n\n## Q2: Only validated on LIBERO—how does this generalize?\n\nLIBERO (Liu et al. 2023) is the standard evaluation benchmark for VLA fine-tuning studies, used by OpenVLA, TracVLA, NORA, and concurrent work (Fang et al. 2026, Swann et al. 2026). Our evaluation spans **4 task suites** (Goal, Spatial, Object, Long-Horizon) that vary substantially in instruction complexity, object diversity, and planning horizon (§3.1).\n\nThe stronger generalization argument comes from **cross-architecture consistency**: exit collapse and counterfactual sensitivity replicate across three distinct backbone families—**Llama-2-7B** (32 layers, MHA), **Phi-3-mini** (32 layers, MHA), and **Qwen2.5-VL-3B** (36 layers, GQA)—spanning 3B to 7B parameters with different pretraining corpora and attention mechanisms. The pattern holds despite qualitatively different reference profiles (§4.5, Appendix §A.16): TracVLA reference starts with saturated L1 attention (32/32 heads) while NORA reference starts at 13–14/16. That the same exit-collapse pattern emerges from these divergent starting points is stronger evidence of generality than observing it on multiple benchmarks within a single architecture.\n\nWe explicitly acknowledge that **flow-matching (π₀) and diffusion-based (Octo) architectures may differ** (§6, Limitations) and list this as a concrete direction for future work. The paper's claims are scoped to causal-decoder VLAs.\n\n---\n\n## Q3: No closed-loop evaluation (SR=0)—what is the significance of representational analysis?\n\nClosed-loop SR=0 is not unique to our work. The VLA community faces well-documented reproducibility challenges: OpenVLA's original release noted sensitivity to hardware and software configurations; Fang et al. (2026) report similar difficulties on LIBERO-CF. Our attempted closed-loop evaluation yielded SR=0/3, which we report transparently rather than omit.\n\n**Representational analysis does not require closed-loop success.** This methodological stance has extensive precedent in NLP interpretability: the probing literature (Belinkov 2022, cited in §2) routinely analyzes internal representations without requiring models to achieve SOTA on downstream tasks. Probing measures what information is *accessible* at each layer, independent of whether the full pipeline successfully executes the task end-to-end. Similarly, RSA and attention profiling characterize geometric organization without assuming perfect behavior.\n\nThe **behavioral correlation (ρ=0.583)** uses *published* success rates from the original papers (Kim et al. 2024; Zheng et al. 2024; Hung et al. 2025), not our own closed-loop evaluations. This leverages community-validated numbers while our contribution focuses on the representational analysis itself.\n\nPractically, **ΔR² as a diagnostic metric** has value precisely because it does not require closed-loop evaluation: it can assess whether a VLA checkpoint exhibits healthy representational structure (ΔR² < 0.10 indicates preserved exit structure) without expensive rollout infrastructure (§6, Practical Implications). This makes it a complementary tool to behavioral evaluation, not a substitute.\n\n---\n\n## Q4: \"First cross-architecture decomposition\"—basis for this claim? Distinction from Kachaev et al.?\n\nThe claim (§4.6, line 176: \"a first cross-architecture decomposition of VLA instruction routing\") is grounded in systematic literature comparison. All prior representational analyses of VLAs target a single architecture:\n\n- **Grant et al. (2026)**: visual dominance in a single VLA\n- **Haon et al. (2025)**: sparse semantic directions in OpenVLA only\n- **Swann et al. (2026)**: interpretable features, large-scale behavioral but single-architecture representational probing per model\n- **Buurmeijer et al. (2026)**: low-level motor feature probing in OpenVLA only\n\n**Kachaev et al. (2025)** study *visual representation collapse* during VLA fine-tuning—a distinct phenomenon from instruction routing. Their analysis is conducted exclusively on OpenVLA. Our work quantifies a complementary phenomenon (layer-wise action-probe decodability via ΔR²) and critically, **distinguishes training-associated from inherited effects** across three architectures (§2, Concurrent Work paragraph; §4.6). This decomposition—showing that exit collapse is training-associated while L1 attention is inherited—requires cross-architecture comparison by design and is absent from all prior single-architecture studies.\n\nThe **3×4 matrix** (3 architectures × 4 suites, 10 filled cells; Table 1) with systematic trained/reference comparisons at each cell is structurally unprecedented in the VLA interpretability literature. The claim is hedged with \"with this caveat\" referring to the probe-vs-causal-reliance distinction stated in the same sentence.\n\n---\n\n## Q5: NLP controls only use chat fine-tuning—wouldn't a more task-specific NLP control be needed?\n\nChat fine-tuning is the **maximally relevant control** for our hypothesis. The question being tested is: \"Is exit collapse a generic artifact of instruction-following fine-tuning, or is it specific to action-oriented (VLA) training?\" Chat-finetuned models share the critical property of being **instruction-following systems fine-tuned on the same backbone**, but lack action heads, robot demonstration data, and vision-action grounding. If exit collapse were a generic consequence of fine-tuning a pretrained LM to follow instructions, chat models should exhibit it.\n\nThree backbone families were tested (§4.3, Table in Appendix §A.19):\n- **Llama-2-7b-chat** (OpenVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.001\n- **Phi-3-mini-4k-instruct** (TracVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000\n- **Qwen2.5-3B-Instruct** (NORA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000\n\nAll three produce **perfectly flat R² profiles** (ΔR² = 0.000), contrasting with VLM-to-VLA collapse (ΔR² = 0.156–0.455). A more task-specific NLP control (e.g., code generation, summarization) would be *further* from VLA fine-tuning in training objective—making it a *weaker* control. Chat instruction-tuning is the closest NLP analog to VLA instruction-following; its complete failure to produce exit collapse provides the strongest evidence that the phenomenon is specific to action-grounded training. We note in §6 (Limitations) that NLP controls cover all three backbone families, though the analysis operates at the representation level rather than requiring matched data distributions.\n\n---\n\n## Q6: Why use effect size thresholds rather than significance testing?\n\nWith **N=63,228 observations** per cell, traditional null-hypothesis significance testing becomes uninformative: virtually every comparison reaches p < 0.001 regardless of practical magnitude. This is a well-known limitation of p-values in large-sample settings (Wasserstein & Lazar 2016, ASA Statement on Statistical Significance).\n\nOur **ΔR² > 0.10 threshold** has dual justification (§3.3, Appendix §A.8):\n1. **Semantic meaning**: 10% absolute change in explained variance represents a substantive shift in action decodability\n2. **Robustness**: the threshold is not boundary-sensitive—any value in **(0.097, 0.156)** produces identical grouping (Appendix Table 6). The gap between the largest non-collapse value (0.097, TracVLA Long reference) and smallest collapse value (0.156, TracVLA Spatial trained) spans 0.059, providing a clean separation zone\n\nStatistical validation accompanies the effect-size framework:\n- **Permutation test**: randomly reassigning 9 cells to two groups (10,000 permutations) yields **p=0.008** for the observed min-max gap (Appendix §A.7)\n- **Bootstrap CIs**: Monte Carlo cross-validation (n=1,000 iterations) with demo-level splitting; VLM-to-VLA CIs lie entirely above zero (lower bounds ≥ 0.09; Table 1)\n- **Cohen's d** for counterfactual sensitivity (medium-to-large: d=0.45–1.52; §4.4, Table 2)\n- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix §A.18)\n\nThis approach aligns with modern statistical best practice: report effect sizes with confidence intervals as primary evidence, use significance tests as supplementary confirmation, and validate threshold robustness via sensitivity analysis.\n\n---\n\n## Summary of Preemptive Measures Already in the Paper\n\nThe manuscript includes the following preemptive defenses against anticipated concerns:\n\n- **Demo-level splitting** (§3.3): eliminates within-trajectory leakage; reduces R² from 0.7–0.9 to 0.4–0.6, quantifying pseudo-replication inflation\n- **Threshold robustness analysis** (§3.3, Appendix §A.8): any threshold in (0.097, 0.156) yields identical grouping\n- **Permutation test** (Appendix §A.7): p=0.008 for VLA-to-VLA vs. VLM-to-VLA separation\n- **Three NLP controls** (§4.3, Appendix §A.19): all three backbone families tested, all ΔR²=0.000\n- **Bonferroni correction** (Appendix §A.18): 48/63 tests survive; all 8 core tests remain significant\n- **Linear probe replication** (Appendix §A.13): consistent with MLP probe patterns, ruling out capacity artifacts\n- **Explicit metric incommensurability** (§4.4): Cohen's d vs. cosine distance clearly separated; cross-metric ratios explicitly flagged as invalid\n- **Claim-Evidence figure** (Appendix §A.20, Figure): each finding paired with supporting evidence and acknowledged scope boundary\n- **Comprehensive Limitations** (§6): N=2 VLM-to-VLA transitions, LIBERO-only, causal-decoder only, open-loop, single checkpoint, underpowered behavioral correlation—all explicitly stated\n- **Training-type asymmetry disclosure** (§3.1): OpenVLA VLA-to-VLA vs. TracVLA/NORA VLM-to-VLA clearly distinguished throughout\n- **Concurrent work differentiation** (§2): Fang et al. (behavioral vs. representational), Buurmeijer et al. (motor features vs. instruction routing), Kachaev et al. (visual collapse vs. action decodability)\n",
      "numLines": 100,
      "startLine": 1,
      "totalLines": 100
    }
  }
}
```

</details>

---

### Assistant

_source line 7_

Now I'll create the v2 with all four modifications applied.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "bb027502-8574-4e10-bd15-123ebb6d37ce",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoNRaHWmoGLyGe6BdnbTK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3567,
      "cache_read_input_tokens": 24676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3567
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

_source line 8_

<details open><summary>🔧 Tool call — Write · `toolu_01E83CSmfZnYomLDkjkue9uY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md",
  "content": "# Anticipated Reviewer Response Letter\n\nWe thank the reviewers for their careful evaluation. Below we address nine anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.\n\n---\n\n## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)\n\nThe sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.\n\nWe attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. [2026] similarly document closed-loop difficulties on LIBERO). This negative result is reported in the Appendix (Extended Discussion, 'Closed-loop evaluation attempt' paragraph).\n\nRegarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix, Extended Discussion). The paper explicitly qualifies this as \"directionally consistent but underpowered\" (§6) and frames it as observational evidence rather than a confirmed causal link.\n\n---\n\n## Q2: Only validated on LIBERO—how does this generalize?\n\nLIBERO (Liu et al. 2023) is the standard evaluation benchmark for VLA fine-tuning studies, used by OpenVLA, TracVLA, NORA, and concurrent work (Fang et al. 2026, Swann et al. 2026). Our evaluation spans **4 task suites** (Goal, Spatial, Object, Long-Horizon) that vary substantially in instruction complexity, object diversity, and planning horizon (§3.1).\n\nThe stronger generalization argument comes from **cross-architecture consistency**: exit collapse and counterfactual sensitivity replicate across three distinct backbone families—**Llama-2-7B** (32 layers, MHA), **Phi-3-mini** (32 layers, MHA), and **Qwen2.5-VL-3B** (36 layers, GQA)—spanning 3B to 7B parameters with different pretraining corpora and attention mechanisms. The pattern holds despite qualitatively different reference profiles (§4.5, Appendix, Extended Discussion): TracVLA reference starts with saturated L1 attention (32/32 heads) while NORA reference starts at 13–14/16. That the same exit-collapse pattern emerges from these divergent starting points is stronger evidence of generality than observing it on multiple benchmarks within a single architecture.\n\nWe explicitly acknowledge that **flow-matching (π₀) and diffusion-based (Octo) architectures may differ** (§6, Limitations) and list this as a concrete direction for future work. The paper's claims are scoped to causal-decoder VLAs.\n\n---\n\n## Q3: No closed-loop evaluation (SR=0)—what is the significance of representational analysis?\n\nClosed-loop SR=0 is not unique to our work. The VLA community faces well-documented reproducibility challenges: OpenVLA's original release noted sensitivity to hardware and software configurations; Fang et al. (2026) report similar difficulties on LIBERO-CF. Our attempted closed-loop evaluation yielded SR=0/3, which we report transparently rather than omit.\n\n**Representational analysis does not require closed-loop success.** This methodological stance has extensive precedent in NLP interpretability: the probing literature (Belinkov 2022, cited in §2) routinely analyzes internal representations without requiring models to achieve SOTA on downstream tasks. Probing measures what information is *accessible* at each layer, independent of whether the full pipeline successfully executes the task end-to-end. Similarly, RSA and attention profiling characterize geometric organization without assuming perfect behavior.\n\nThe **behavioral correlation (ρ=0.583)** uses *published* success rates from the original papers (Kim et al. 2024; Zheng et al. 2024; Hung et al. 2025), not our own closed-loop evaluations. This leverages community-validated numbers while our contribution focuses on the representational analysis itself.\n\nPractically, **ΔR² as a diagnostic metric** has value precisely because it does not require closed-loop evaluation: it can assess whether a VLA checkpoint exhibits healthy representational structure (ΔR² < 0.10 indicates preserved exit structure) without expensive rollout infrastructure (§6, Practical Implications). This makes it a complementary tool to behavioral evaluation, not a substitute.\n\n---\n\n## Q4: \"First cross-architecture decomposition\"—basis for this claim? Distinction from Kachaev et al.?\n\nThe claim (§4.6, line 176: \"a first cross-architecture decomposition of VLA instruction routing\") is grounded in systematic literature comparison. All prior representational analyses of VLAs target a single architecture:\n\n- **Grant et al. (2026)**: visual dominance in a single VLA\n- **Haon et al. (2025)**: sparse semantic directions in OpenVLA only\n- **Swann et al. (2026)**: interpretable features, large-scale behavioral but single-architecture representational probing per model\n- **Buurmeijer et al. (2026)**: low-level motor feature probing in OpenVLA only\n\n**Kachaev et al. (2025)** study *visual representation collapse* during VLA fine-tuning—a distinct phenomenon from instruction routing. Their analysis is conducted exclusively on OpenVLA. Our work quantifies a complementary phenomenon (layer-wise action-probe decodability via ΔR²) and critically, **distinguishes training-associated from inherited effects** across three architectures (§2, Concurrent Work paragraph; §4.6). This decomposition—showing that exit collapse is training-associated while L1 attention is inherited—requires cross-architecture comparison by design and is absent from all prior single-architecture studies.\n\nThe **3×4 matrix** (3 architectures × 4 suites, 10 filled cells; Table 1) with systematic trained/reference comparisons at each cell is structurally unprecedented in the VLA interpretability literature. The claim is hedged with \"with this caveat\" referring to the probe-vs-causal-reliance distinction stated in the same sentence.\n\n---\n\n## Q5: NLP controls only use chat fine-tuning—wouldn't a more task-specific NLP control be needed?\n\nChat fine-tuning is the **maximally relevant control** for our hypothesis. The question being tested is: \"Is exit collapse a generic artifact of instruction-following fine-tuning, or is it specific to action-oriented (VLA) training?\" Chat-finetuned models share the critical property of being **instruction-following systems fine-tuned on the same backbone**, but lack action heads, robot demonstration data, and vision-action grounding. If exit collapse were a generic consequence of fine-tuning a pretrained LM to follow instructions, chat models should exhibit it.\n\nThree backbone families were tested (§4.3, Table in Appendix, NLP Finetuning Controls):\n- **Llama-2-7b-chat** (OpenVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.001\n- **Phi-3-mini-4k-instruct** (TracVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000\n- **Qwen2.5-3B-Instruct** (NORA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000\n\nAll three produce **perfectly flat R² profiles** (ΔR² = 0.000), contrasting with VLM-to-VLA collapse (ΔR² = 0.156–0.455). A more task-specific NLP control (e.g., code generation, summarization) would be *further* from VLA fine-tuning in training objective—making it a *weaker* control. Chat instruction-tuning is the closest NLP analog to VLA instruction-following; its complete failure to produce exit collapse provides the strongest evidence that the phenomenon is specific to action-grounded training. We note in §6 (Limitations) that NLP controls cover all three backbone families, though the analysis operates at the representation level rather than requiring matched data distributions.\n\n---\n\n## Q6: Why use effect size thresholds rather than significance testing?\n\nWith **N=63,228 observations** per cell, traditional null-hypothesis significance testing becomes uninformative: virtually every comparison reaches p < 0.001 regardless of practical magnitude. This is a well-known limitation of p-values in large-sample settings (Wasserstein & Lazar 2016, ASA Statement on Statistical Significance).\n\nOur **ΔR² > 0.10 threshold** has dual justification (§3.3, Appendix, Threshold Robustness and Permutation Test):\n1. **Semantic meaning**: 10% absolute change in explained variance represents a substantive shift in action decodability\n2. **Robustness**: the threshold is not boundary-sensitive—any value in **(0.097, 0.156)** produces identical grouping (Appendix Table 6). The gap between the largest non-collapse value (0.097, TracVLA Long reference) and smallest collapse value (0.156, TracVLA Spatial trained) spans 0.059, providing a clean separation zone\n\nStatistical validation accompanies the effect-size framework:\n- **Permutation test**: randomly reassigning 9 cells to two groups (10,000 permutations) yields **p=0.008** for the observed min-max gap (Appendix, Threshold Robustness and Permutation Test)\n- **Bootstrap CIs**: Monte Carlo cross-validation (n=1,000 iterations) with demo-level splitting; VLM-to-VLA CIs lie entirely above zero (lower bounds ≥ 0.09; Table 1)\n- **Cohen's d** for counterfactual sensitivity (medium-to-large: d=0.45–1.52; §4.4, Table 2)\n- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix, Bonferroni Correction)\n\nThis approach aligns with modern statistical best practice: report effect sizes with confidence intervals as primary evidence, use significance tests as supplementary confirmation, and validate threshold robustness via sensitivity analysis.\n\n---\n\n## Q7: N=2 VLM→VLA transitions—how does this generalize beyond two models?\n\nThe N=2 VLM→VLA transitions (TracVLA and NORA) may appear small, but the evidential weight of these two transitions exceeds what raw count suggests for three reasons.\n\n**Structural diversity between the two transitions.** TracVLA and NORA differ on nearly every design axis: backbone family (Phi-3-mini vs. Qwen2.5-VL), parameter count (3.8B vs. 3B), attention mechanism (MHA vs. GQA), pretraining corpus (Microsoft vs. Alibaba), and vision encoder integration strategy. Observing identical exit-collapse patterns (ΔR² = 0.156–0.455) across such structurally divergent models provides stronger evidence of generality than N=5 repetitions within a single architecture family, where shared inductive biases could explain the consistency.\n\n**Total evidence includes the negative control.** OpenVLA contributes 4 VLA→VLA cells where ΔR² remains below 0.10 (0/4 cells exhibit collapse). Combined with the 6 VLM→VLA cells showing collapse, the design provides **10 independently-tested cells** with a clean binary separation—collapse occurs if and only if the transition is VLM→VLA.\n\n**Precedent in mechanistic interpretability.** Many high-impact studies in NLP mechanistic interpretability establish general claims from 2–3 models: induction heads (Olsson et al. 2022) use 2 model sizes; the IOI circuit (Wang et al. 2023) is demonstrated in GPT-2 only; superposition (Elhage et al. 2022) uses toy models plus one transformer. Our cross-architecture design with controlled comparisons at each cell exceeds the standard in this subfield.\n\nThe paper explicitly scopes this limitation: \"N=2 VLM-to-VLA transitions is insufficient for strong causal claims\" (§6). We frame our contribution as the first characterization that motivates targeted follow-up, not as a definitive universal law.\n\n---\n\n## Q8: Probing measures decodability, not causal reliance—how do you know the model actually uses this information?\n\nThe paper acknowledges this limitation directly in §4.6 (Synthesis): \"These probes measure decodability, not causal reliance.\" We consider this distinction important to state but insufficient to dismiss the findings, for several reasons.\n\n**Characterization precedes causal intervention.** Even without causal proof, establishing *where* information resides and *how* training reorganizes it is a necessary first step toward understanding. The analogy to neuroscience is instructive: fMRI cannot establish causal necessity, yet functional imaging has been foundational for building models of brain organization that subsequently guided causal interventions (TMS, lesion studies). Our probing results serve the same cartographic function for VLA internals.\n\n**Complementary behavioral evidence.** The counterfactual perturbation analysis (§4.4) provides direct behavioral evidence that instruction content *does* influence action outputs: swapping instructions between task suites produces medium-to-large action divergence (Cohen's d = 0.45–1.52, Table 2). This does not prove that the specific layers identified by probing are causally necessary, but it establishes that instruction information is functionally utilized somewhere in the pipeline.\n\n**Intervention evidence from dose-response ablation.** The attention head ablation (Appendix, Extended Discussion) provides intervention-level evidence: progressively removing instruction-dominant L1 heads produces monotonic increases in action divergence (d = 0.48–0.64), confirming that the attention structures we identify carry functionally relevant signals.\n\n**Convergent triangulation.** Three methodologically distinct approaches point to the same conclusion: probing identifies *where* instruction information concentrates, perturbation confirms *whether* instruction content affects behavior, and ablation demonstrates *contribution* of identified structures. No single method is sufficient alone, but their convergence substantially strengthens the overall picture.\n\n---\n\n## Q9: Why not analyze training dynamics (multiple checkpoints)?\n\nThe paper explicitly identifies this as a limitation in §6 (Discussion): \"tracing collapse onset remains for future work.\" The absence of training dynamics is a deliberate scope choice driven by practical constraints, not an oversight.\n\n**Checkpoint availability.** Our cross-architecture design relies on community-released final checkpoints (OpenVLA, TracVLA, NORA). None of these projects have published intermediate training checkpoints. Conducting training-dynamics analysis would require either (a) retraining these models from scratch with checkpoint saving—a substantial compute investment (~500+ GPU-hours per architecture) that transforms the project from an analytical study into a training study—or (b) waiting for the community to release such checkpoints.\n\n**Complementary research questions.** Our paper answers \"what exists at the end of training\" rather than \"how it develops during training.\" Both questions are scientifically valuable, but they require fundamentally different experimental designs. A cross-architecture endpoint study (ours) reveals what is *common* across diverse training procedures; a training-dynamics study reveals *when* and *how* a phenomenon emerges within a single procedure. These are complementary, not substitutable.\n\n**Partial dynamics insight from the existing design.** Although we lack temporal resolution within a single training run, the VLM→VLA vs. VLA→VLA comparison provides coarse-grained dynamics information: exit collapse emerges during the first VLM→VLA fine-tuning transition and does not intensify during subsequent VLA→VLA fine-tuning (OpenVLA cells: all ΔR² < 0.10). This constrains when collapse occurs (early in action-grounded training) even without intermediate checkpoints.\n\n**Our contribution is the first anatomical characterization.** Before studying dynamics, one must first establish *what* to track. Our ΔR² metric and the exit-collapse phenomenon provide a concrete, quantifiable target for future training-dynamics studies. We view this as laying the foundation rather than leaving a gap.\n\n---\n\n## Summary of Preemptive Measures Already in the Paper\n\nThe manuscript includes the following preemptive defenses against anticipated concerns:\n\n- **Demo-level splitting** (§3.3): eliminates within-trajectory leakage; reduces R² from 0.7–0.9 to 0.4–0.6, quantifying pseudo-replication inflation\n- **Threshold robustness analysis** (§3.3, Appendix, Threshold Robustness and Permutation Test): any threshold in (0.097, 0.156) yields identical grouping\n- **Permutation test** (Appendix, Threshold Robustness and Permutation Test): p=0.008 for VLA-to-VLA vs. VLM-to-VLA separation\n- **Three NLP controls** (§4.3, Appendix, NLP Finetuning Controls): all three backbone families tested, all ΔR²=0.000\n- **Bonferroni correction** (Appendix, Bonferroni Correction): 48/63 tests survive; all 8 core tests remain significant\n- **Linear probe replication** (Appendix, Linear Probe Replication): consistent with MLP probe patterns, ruling out capacity artifacts\n- **Explicit metric incommensurability** (§4.4): Cohen's d vs. cosine distance clearly separated; cross-metric ratios explicitly flagged as invalid\n- **Claim-Evidence figure** (Appendix, Claim-Evidence Summary, Figure): each finding paired with supporting evidence and acknowledged scope boundary\n- **Comprehensive Limitations** (§6): N=2 VLM-to-VLA transitions, LIBERO-only, causal-decoder only, open-loop, single checkpoint, underpowered behavioral correlation—all explicitly stated\n- **Training-type asymmetry disclosure** (§3.1): OpenVLA VLA-to-VLA vs. TracVLA/NORA VLM-to-VLA clearly distinguished throughout\n- **Concurrent work differentiation** (§2): Fang et al. (behavioral vs. representational), Buurmeijer et al. (motor features vs. instruction routing), Kachaev et al. (visual collapse vs. action decodability)\n- **Closed-loop attempt documented** (Appendix, Extended Discussion): SR=0/3 reported transparently rather than omitted\n- **Probing caveat** (§4.6): explicit \"decodability, not causal reliance\" disclaimer\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "dfd840fb-f04b-4eee-91f1-803440356ba6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XoNRaHWmoGLyGe6BdnbTK1",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3567,
      "cache_read_input_tokens": 24676,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3567
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

_source line 9 · 2026-05-25T20:04:17.061Z_

<details><summary>↩ Tool result · `toolu_01E83CSmfZnYomLDkjkue9uY`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "aa44251b-b134-4bcc-9524-5c152f944388",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_15/projects/vla-ssd/artifacts/anticipated_rebuttal_v2.md",
    "content": "# Anticipated Reviewer Response Letter\n\nWe thank the reviewers for their careful evaluation. Below we address nine anticipated questions, referencing specific sections, tables, and figures in the manuscript and appendix.\n\n---\n\n## Q1: Behavioral correlation underpowered (ρ=0.583, p=0.10, n=9)\n\nThe sample size **n=9** is determined by the cross-architecture matrix design: 3 architectures × 4 LIBERO suites yields 12 cells, of which 10 are filled (NORA Object and Long-Horizon checkpoints are unavailable; §3.1, Table 1). One cell (NORA Goal) is excluded due to bootstrap CI instability from an exit-layer R² ≈ −0.006 artifact (Table 1, footnote b), leaving **9 usable cells**. Expanding n requires either additional VLA architectures with published LIBERO success rates or additional benchmark suites—both beyond the scope of this initial cross-architecture characterization.\n\nWe attempted closed-loop evaluation but achieved **SR=0/3** across tested configurations, consistent with known reproducibility challenges in the VLA community (the OpenVLA authors report substantial variation across hardware setups; Fang et al. [2026] similarly document closed-loop difficulties on LIBERO). This negative result is reported in the Appendix (Extended Discussion, 'Closed-loop evaluation attempt' paragraph).\n\nRegarding statistical interpretation: **|ρ|=0.583 constitutes a large effect size** by conventional criteria (|ρ|>0.5; Cohen 1988). The p=0.10 reflects insufficient statistical power at n=9, not absence of effect. Within-suite comparisons are uniformly positive: on Goal (n=3 architectures), ΔR² and success rate are perfectly rank-correlated (ρ=1.0), and every remaining suite shows the same direction (Appendix, Extended Discussion). The paper explicitly qualifies this as \"directionally consistent but underpowered\" (§6) and frames it as observational evidence rather than a confirmed causal link.\n\n---\n\n## Q2: Only validated on LIBERO—how does this generalize?\n\nLIBERO (Liu et al. 2023) is the standard evaluation benchmark for VLA fine-tuning studies, used by OpenVLA, TracVLA, NORA, and concurrent work (Fang et al. 2026, Swann et al. 2026). Our evaluation spans **4 task suites** (Goal, Spatial, Object, Long-Horizon) that vary substantially in instruction complexity, object diversity, and planning horizon (§3.1).\n\nThe stronger generalization argument comes from **cross-architecture consistency**: exit collapse and counterfactual sensitivity replicate across three distinct backbone families—**Llama-2-7B** (32 layers, MHA), **Phi-3-mini** (32 layers, MHA), and **Qwen2.5-VL-3B** (36 layers, GQA)—spanning 3B to 7B parameters with different pretraining corpora and attention mechanisms. The pattern holds despite qualitatively different reference profiles (§4.5, Appendix, Extended Discussion): TracVLA reference starts with saturated L1 attention (32/32 heads) while NORA reference starts at 13–14/16. That the same exit-collapse pattern emerges from these divergent starting points is stronger evidence of generality than observing it on multiple benchmarks within a single architecture.\n\nWe explicitly acknowledge that **flow-matching (π₀) and diffusion-based (Octo) architectures may differ** (§6, Limitations) and list this as a concrete direction for future work. The paper's claims are scoped to causal-decoder VLAs.\n\n---\n\n## Q3: No closed-loop evaluation (SR=0)—what is the significance of representational analysis?\n\nClosed-loop SR=0 is not unique to our work. The VLA community faces well-documented reproducibility challenges: OpenVLA's original release noted sensitivity to hardware and software configurations; Fang et al. (2026) report similar difficulties on LIBERO-CF. Our attempted closed-loop evaluation yielded SR=0/3, which we report transparently rather than omit.\n\n**Representational analysis does not require closed-loop success.** This methodological stance has extensive precedent in NLP interpretability: the probing literature (Belinkov 2022, cited in §2) routinely analyzes internal representations without requiring models to achieve SOTA on downstream tasks. Probing measures what information is *accessible* at each layer, independent of whether the full pipeline successfully executes the task end-to-end. Similarly, RSA and attention profiling characterize geometric organization without assuming perfect behavior.\n\nThe **behavioral correlation (ρ=0.583)** uses *published* success rates from the original papers (Kim et al. 2024; Zheng et al. 2024; Hung et al. 2025), not our own closed-loop evaluations. This leverages community-validated numbers while our contribution focuses on the representational analysis itself.\n\nPractically, **ΔR² as a diagnostic metric** has value precisely because it does not require closed-loop evaluation: it can assess whether a VLA checkpoint exhibits healthy representational structure (ΔR² < 0.10 indicates preserved exit structure) without expensive rollout infrastructure (§6, Practical Implications). This makes it a complementary tool to behavioral evaluation, not a substitute.\n\n---\n\n## Q4: \"First cross-architecture decomposition\"—basis for this claim? Distinction from Kachaev et al.?\n\nThe claim (§4.6, line 176: \"a first cross-architecture decomposition of VLA instruction routing\") is grounded in systematic literature comparison. All prior representational analyses of VLAs target a single architecture:\n\n- **Grant et al. (2026)**: visual dominance in a single VLA\n- **Haon et al. (2025)**: sparse semantic directions in OpenVLA only\n- **Swann et al. (2026)**: interpretable features, large-scale behavioral but single-architecture representational probing per model\n- **Buurmeijer et al. (2026)**: low-level motor feature probing in OpenVLA only\n\n**Kachaev et al. (2025)** study *visual representation collapse* during VLA fine-tuning—a distinct phenomenon from instruction routing. Their analysis is conducted exclusively on OpenVLA. Our work quantifies a complementary phenomenon (layer-wise action-probe decodability via ΔR²) and critically, **distinguishes training-associated from inherited effects** across three architectures (§2, Concurrent Work paragraph; §4.6). This decomposition—showing that exit collapse is training-associated while L1 attention is inherited—requires cross-architecture comparison by design and is absent from all prior single-architecture studies.\n\nThe **3×4 matrix** (3 architectures × 4 suites, 10 filled cells; Table 1) with systematic trained/reference comparisons at each cell is structurally unprecedented in the VLA interpretability literature. The claim is hedged with \"with this caveat\" referring to the probe-vs-causal-reliance distinction stated in the same sentence.\n\n---\n\n## Q5: NLP controls only use chat fine-tuning—wouldn't a more task-specific NLP control be needed?\n\nChat fine-tuning is the **maximally relevant control** for our hypothesis. The question being tested is: \"Is exit collapse a generic artifact of instruction-following fine-tuning, or is it specific to action-oriented (VLA) training?\" Chat-finetuned models share the critical property of being **instruction-following systems fine-tuned on the same backbone**, but lack action heads, robot demonstration data, and vision-action grounding. If exit collapse were a generic consequence of fine-tuning a pretrained LM to follow instructions, chat models should exhibit it.\n\nThree backbone families were tested (§4.3, Table in Appendix, NLP Finetuning Controls):\n- **Llama-2-7b-chat** (OpenVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.001\n- **Phi-3-mini-4k-instruct** (TracVLA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000\n- **Qwen2.5-3B-Instruct** (NORA backbone): ΔR² = 0.000, mean R² = 0.155 ± 0.000\n\nAll three produce **perfectly flat R² profiles** (ΔR² = 0.000), contrasting with VLM-to-VLA collapse (ΔR² = 0.156–0.455). A more task-specific NLP control (e.g., code generation, summarization) would be *further* from VLA fine-tuning in training objective—making it a *weaker* control. Chat instruction-tuning is the closest NLP analog to VLA instruction-following; its complete failure to produce exit collapse provides the strongest evidence that the phenomenon is specific to action-grounded training. We note in §6 (Limitations) that NLP controls cover all three backbone families, though the analysis operates at the representation level rather than requiring matched data distributions.\n\n---\n\n## Q6: Why use effect size thresholds rather than significance testing?\n\nWith **N=63,228 observations** per cell, traditional null-hypothesis significance testing becomes uninformative: virtually every comparison reaches p < 0.001 regardless of practical magnitude. This is a well-known limitation of p-values in large-sample settings (Wasserstein & Lazar 2016, ASA Statement on Statistical Significance).\n\nOur **ΔR² > 0.10 threshold** has dual justification (§3.3, Appendix, Threshold Robustness and Permutation Test):\n1. **Semantic meaning**: 10% absolute change in explained variance represents a substantive shift in action decodability\n2. **Robustness**: the threshold is not boundary-sensitive—any value in **(0.097, 0.156)** produces identical grouping (Appendix Table 6). The gap between the largest non-collapse value (0.097, TracVLA Long reference) and smallest collapse value (0.156, TracVLA Spatial trained) spans 0.059, providing a clean separation zone\n\nStatistical validation accompanies the effect-size framework:\n- **Permutation test**: randomly reassigning 9 cells to two groups (10,000 permutations) yields **p=0.008** for the observed min-max gap (Appendix, Threshold Robustness and Permutation Test)\n- **Bootstrap CIs**: Monte Carlo cross-validation (n=1,000 iterations) with demo-level splitting; VLM-to-VLA CIs lie entirely above zero (lower bounds ≥ 0.09; Table 1)\n- **Cohen's d** for counterfactual sensitivity (medium-to-large: d=0.45–1.52; §4.4, Table 2)\n- **Bonferroni correction**: 63 tests total, 48/63 (76%) pass family-wise correction; all 8 core tests survive at α_adj = 7.94×10⁻⁴ (Appendix, Bonferroni Correction)\n\nThis approach aligns with modern statistical best practice: report effect sizes with confidence intervals as primary evidence, use significance tests as supplementary confirmation, and validate threshold robustness via sensitivity analysis.\n\n---\n\n## Q7: N=2 VLM→VLA transitions—how does this generalize beyond two models?\n\nThe N=2 VLM→VLA transitions (TracVLA and NORA) may appear small, but the evidential weight of these two transitions exceeds what raw count suggests for three reasons.\n\n**Structural diversity between the two transitions.** TracVLA and NORA differ on nearly every design axis: backbone family (Phi-3-mini vs. Qwen2.5-VL), parameter count (3.8B vs. 3B), attention mechanism (MHA vs. GQA), pretraining corpus (Microsoft vs. Alibaba), and vision encoder integration strategy. Observing identical exit-collapse patterns (ΔR² = 0.156–0.455) across such structurally divergent models provides stronger evidence of generality than N=5 repetitions within a single architecture family, where shared inductive biases could explain the consistency.\n\n**Total evidence includes the negative control.** OpenVLA contributes 4 VLA→VLA cells where ΔR² remains below 0.10 (0/4 cells exhibit collapse). Combined with the 6 VLM→VLA cells showing collapse, the design provides **10 independently-tested cells** with a clean binary separation—collapse occurs if and only if the transition is VLM→VLA.\n\n**Precedent in mechanistic interpretability.** Many high-impact studies in NLP mechanistic interpretability establish general claims from 2–3 models: induction heads (Olsson et al. 2022) use 2 model sizes; the IOI circuit (Wang et al. 2023) is demonstrated in GPT-2 only; superposition (Elhage et al. 2022) uses toy models plus one transformer. Our cross-architecture design with controlled comparisons at each cell exceeds the standard in this subfield.\n\nThe paper explicitly scopes this limitation: \"N=2 VLM-to-VLA transitions is insufficient for strong causal claims\" (§6). We frame our contribution as the first characterization that motivates targeted follow-up, not as a definitive universal law.\n\n---\n\n## Q8: Probing measures decodability, not causal reliance—how do you know the model actually uses this information?\n\nThe paper acknowledges this limitation directly in §4.6 (Synthesis): \"These probes measure decodability, not causal reliance.\" We consider this distinction important to state but insufficient to dismiss the findings, for several reasons.\n\n**Characterization precedes causal intervention.** Even without causal proof, establishing *where* information resides and *how* training reorganizes it is a necessary first step toward understanding. The analogy to neuroscience is instructive: fMRI cannot establish causal necessity, yet functional imaging has been foundational for building models of brain organization that subsequently guided causal interventions (TMS, lesion studies). Our probing results serve the same cartographic function for VLA internals.\n\n**Complementary behavioral evidence.** The counterfactual perturbation analysis (§4.4) provides direct behavioral evidence that instruction content *does* influence action outputs: swapping instructions between task suites produces medium-to-large action divergence (Cohen's d = 0.45–1.52, Table 2). This does not prove that the specific layers identified by probing are causally necessary, but it establishes that instruction information is functionally utilized somewhere in the pipeline.\n\n**Intervention evidence from dose-response ablation.** The attention head ablation (Appendix, Extended Discussion) provides intervention-level evidence: progressively removing instruction-dominant L1 heads produces monotonic increases in action divergence (d = 0.48–0.64), confirming that the attention structures we identify carry functionally relevant signals.\n\n**Convergent triangulation.** Three methodologically distinct approaches point to the same conclusion: probing identifies *where* instruction information concentrates, perturbation confirms *whether* instruction content affects behavior, and ablation demonstrates *contribution* of identified structures. No single method is sufficient alone, but their convergence substantially strengthens the overall picture.\n\n---\n\n## Q9: Why not analyze training dynamics (multiple checkpoints)?\n\nThe paper explicitly identifies this as a limitation in §6 (Discussion): \"tracing collapse onset remains for future work.\" The absence of training dynamics is a deliberate scope choice driven by practical constraints, not an oversight.\n\n**Checkpoint availability.** Our cross-architecture design relies on community-released final checkpoints (OpenVLA, TracVLA, NORA). None of these projects have published intermediate training checkpoints. Conducting training-dynamics analysis would require either (a) retraining these models from scratch with checkpoint saving—a substantial compute investment (~500+ GPU-hours per architecture) that transforms the project from an analytical study into a training study—or (b) waiting for the community to release such checkpoints.\n\n**Complementary research questions.** Our paper answers \"what exists at the end of training\" rather than \"how it develops during training.\" Both questions are scientifically valuable, but they require fundamentally different experimental designs. A cross-architecture endpoint study (ours) reveals what is *common* across diverse training procedures; a training-dynamics study reveals *when* and *how* a phenomenon emerges within a single procedure. These are complementary, not substitutable.\n\n**Partial dynamics insight from the existing design.** Although we lack temporal resolution within a single training run, the VLM→VLA vs. VLA→VLA comparison provides coarse-grained dynamics information: exit collapse emerges during the first VLM→VLA fine-tuning transition and does not intensify during subsequent VLA→VLA fine-tuning (OpenVLA cells: all ΔR² < 0.10). This constrains when collapse occurs (early in action-grounded training) even without intermediate checkpoints.\n\n**Our contribution is the first anatomical characterization.** Before studying dynamics, one must first establish *what* to track. Our ΔR² metric and the exit-collapse phenomenon provide a concrete, quantifiable target for future training-dynamics studies. We view this as laying the foundation rather than leaving a gap.\n\n---\n\n## Summary of Preemptive Measures Already in the Paper\n\nThe manuscript includes the following preemptive defenses against anticipated concerns:\n\n- **Demo-level splitting** (§3.3): eliminates within-trajectory leakage; reduces R² from 0.7–0.9 to 0.4–0.6, quantifying pseudo-replication inflation\n- **Threshold robustness analysis** (§3.3, Appendix, Threshold Robustness and Permutation Test): any threshold in (0.097, 0.156) yields identical grouping\n- **Permutation test** (Appendix, Threshold Robustness and Permutation Test): p=0.008 for VLA-to-VLA vs. VLM-to-VLA separation\n- **Three NLP controls** (§4.3, Appendix, NLP Finetuning Controls): all three backbone families tested, all ΔR²=0.000\n- **Bonferroni correction** (Appendix, Bonferroni Correction): 48/63 tests survive; all 8 core tests remain significant\n- **Linear probe replication** (Appendix, Linear Probe Replication): consistent with MLP probe patterns, ruling out capacity artifacts\n- **Explicit metric incommensurability** (§4.4): Cohen's d vs. cosine distance clearly separated; cross-metric ratios explicitly flagged as invalid\n- **Claim-Evidence figure** (Appendix, Claim-Evidence Summary, Figure): each finding paired with supporting evidence and acknowledged scope boundary\n- **Comprehensive Limitations** (§6): N=2 VLM-to-VLA transitions, LIBERO-only, causal-decoder only, open-loop, single checkpoint, underpowered behavioral correlation—all explicitly stated\n- **Training-type asymmetry disclosure** (§3.1): OpenVLA VLA-to-VLA vs. TracVLA/NORA VLM-to-VLA clearly distinguished throughout\n- **Concurrent work differentiation** (§2): Fang et al. (behavioral vs. representational), Buurmeijer et al. (motor features vs. instruction routing), Kachaev et al. (visual collapse vs. action decodability)\n- **Closed-loop attempt documented** (Appendix, Extended Discussion): SR=0/3 reported transparently rather than omitted\n- **Probing caveat** (§4.6): explicit \"decodability, not causal reliance\" disclaimer\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
```

</details>

---

### Assistant

_source line 10_

v2 已写入。变更汇总：

1. **硬编码 appendix 编号** — 所有 `§A.7/8/13/16/18/19/20` 替换为描述性标题（"Appendix, Extended Discussion"、"Appendix, NLP Finetuning Controls" 等）
2. **Q1 修正** — closed-loop 引用改为 "Appendix (Extended Discussion, 'Closed-loop evaluation attempt' paragraph)"
3. **Q3 修正** — 同步更新了所有硬编码引用
4. **新增 Q7-Q9** — N=2 推广性（~250 词）、Probing ≠ causal reliance（~270 词）、Training dynamics（~280 词）
5. **Summary 追加** — 两条新 preemptive measure（closed-loop attempt documented + probing caveat）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "uuid": "b55d30d3-1add-46e6-9ca3-9505a5ed2848",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017rGcueb9bgLXqSBW2RgRyV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4866,
      "cache_read_input_tokens": 28243,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4866
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

_source line 11_

v2 已写入。变更汇总：

1. **硬编码 appendix 编号** — 所有 `§A.7/8/13/16/18/19/20` 替换为描述性标题（"Appendix, Extended Discussion"、"Appendix, NLP Finetuning Controls" 等）
2. **Q1 修正** — closed-loop 引用改为 "Appendix (Extended Discussion, 'Closed-loop evaluation attempt' paragraph)"
3. **Q3 修正** — 同步更新了所有硬编码引用
4. **新增 Q7-Q9** — N=2 推广性（~250 词）、Probing ≠ causal reliance（~270 词）、Training dynamics（~280 词）
5. **Summary 追加** — 两条新 preemptive measure（closed-loop attempt documented + probing caveat）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 92093,
  "duration_api_ms": 93292,
  "num_turns": 3,
  "stop_reason": "end_turn",
  "session_id": "9bad4df6-b0ff-4a9e-a6e6-e6a93a48bc17",
  "total_cost_usd": 0.297546,
  "usage": {
    "input_tokens": 5,
    "cache_creation_input_tokens": 21268,
    "cache_read_input_tokens": 64760,
    "output_tokens": 5180,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 21268,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 240,
        "cache_read_input_tokens": 28243,
        "cache_creation_input_tokens": 4866,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 4866
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 2621,
      "outputTokens": 19,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.002716,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5,
      "outputTokens": 5180,
      "cacheReadInputTokens": 64760,
      "cacheCreationInputTokens": 21268,
      "webSearchRequests": 0,
      "costUSD": 0.29483,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "bf29b19f-1f84-426e-9926-6e28ad319beb"
}
```

</details>

---
