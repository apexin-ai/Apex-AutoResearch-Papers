# Research conversation: You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **methods and experiments**. You must be calibra

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 3
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a8f39573a6a14d297.jsonl`
- **Structured JSON:** [`1db08776caf2d547d4b0.json`](../../sessions/1d/1db08776caf2d547d4b0.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

3 recorded events

### User

_source line 1 · 2026-05-23T20:01:05.797Z_

You are Reviewer 1 (R1) for an EMNLP 2026 ARR submission. Your focus is **methods and experiments**. You must be calibrated to EMNLP acceptance rates (~21% main, ~30% Findings).

## Scoring scale (ARR Overall Assessment, 0.5 increments)
- 5 = Award consideration (top 2.5%)
- 4 = Main conference accept
- 3 = Findings accept
- 2 = Resubmit next cycle
- 1 = Do not resubmit

## Paper summary

**Title**: "Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families"

The paper studies how policy ambiguity in natural-language policies causes safety violations in LLM agents. Using a matched-pair design on τ²-bench with 2,997 episodes, 5 models (GPT-5.4, GPT-4.1, Claude Sonnet 4.6, Qwen3-235B, DeepSeek-V3), and 6 ambiguity types, it claims:
- C1: +34pp violation increase (OR=15.1, p<0.0001) — universal across all models
- C2: Type hierarchy (χ²=28.02, p=3.6e-5, V=0.137) — incompleteness highest (53.6%), coreferential lowest (31.6%)
- C3: Layer effect (spec vs linguistic, Δ=6.08pp, p=0.017) — but fragile, dissolves in within-judge subgroups
- C4: Model×type interaction — auth_scope ranges 52pp across models (12%-64%)

Contributions: (1) causal quantification with perturbation control, (2) model×type interaction, (3) benchmark release of 300 clause pairs.

## Key methodological details

**Design**: Matched-pair within-clause. 300 clause pairs (amb + unamb), 50 per type, 6 types in 2 layers (spec: auth_scope, cond_prec, incompleteness; ling: lexical, coreferential, scopal).

**Judge calibration** (Table 2): Human-LLM κw=0.807, human inter-annotator κ=0.762, cross-judge κw=0.685. N=100 stratified episodes, 2 human raters. All pass pre-registered thresholds. No same-family bias.

**Realism validation** (Table 3): KS tests vs DRIP-R on 4 metrics. 2/4 significant (sentence length p=.028, parse depth p=.039). Synthetic clauses ~5 tokens longer and ~0.7 parse levels deeper — attributed to matched-pair requiring disambiguation text.

**Perturbation control** (Table 4): 30 clause pairs with synonym/reorder changes, 300 episodes. Δperturb=-0.67pp (CI [-8.0, 6.67]), ratio=0.02. PASS on all thresholds. This is the causal identification strategy.

**Test-retest reliability** (Table 5): 30 clauses × 3 replicates × 2 conditions × 2 models = 360 episodes. ICC=0.919 overall. Linguistic types ICC 0.976-0.989, spec types 0.807-0.857.

**Error analysis** (Appendix A): 614 traces coded by 2 LLM coders. LLM-LLM κ=0.517. Disambiguation awareness 4.1-10.7%, surface adoption >88%.

**Human re-annotation** (Appendix B): 25 traces. Human-LLM κ=0.22 (poor), human-human κ=0.48 (moderate). LLM coders use keyword-driven labels. Paper demotes all failure mode analysis to "exploratory."

**SOPBench replication** (Appendix C): 100 clause pairs × 2 conditions × 5 models on Healthcare+Bank. Overall Δ=14.2pp (vs 34pp). Only 3/5 models significant. Type rank ρ=0.20 (n.s.).

**DeBERTa classifier** (Appendix D): Binary F1=0.78, macro F1=0.55.

## Statistical details from the paper
- C1: Logistic regression condition coef=2.278, z=19.65. Token delta coef=0.022, p=0.0005.
- C2: V=0.137 (below 0.20 medium threshold). Power=0.993, MDE=0.093. TOST: 4/15 pairs equivalent at ±10pp.
- C3: Pooled p=0.017; GPT-4.1 judged p=0.059; GPT-5.4 judged p=0.157. Reported as "suggestive."
- C4: Model χ²=31.02, p=3e-6, V=0.102. DeepSeek: χ²=6.31, p=0.277 (no type differentiation). GPT-5.4: χ²=23.44, p=0.0003. Fleiss κ=0.384 for inter-model clause-level agreement.
- Systematic nocuity: 27% of ambiguous episodes have all models converge on same wrong answer.

## Your task

Write a detailed review covering:

1. **Summary** (2-3 sentences)
2. **Strengths** (bullet points, focus on methodology and experimental rigor)
3. **Weaknesses** (bullet points, focus on methodology and experimental gaps)
4. **Questions for authors**
5. **Soundness** (1-5)
6. **Excitement** (1-5)
7. **Reproducibility** (1-5)
8. **Overall Assessment** (use the ARR scale above, half-point increments)
9. **Confidence** (1-5)

Be rigorous. Consider: Is the causal identification valid? Are the statistical tests appropriate? Is N=25 for human re-annotation sufficient? Does the SOPBench attenuation undermine generalizability? Is V=0.137 for C2 practically meaningful? Is C3 actually supported? What about the 2/4 KS test failures for realism? Does 1 model (DeepSeek) having no type differentiation weaken C4? How does the matched-pair token-length asymmetry (35.2 vs 18.4 disambiguation tokens) interact with results?


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "ee32ce64-7c91-43e2-9ce4-ff86f6d668ed",
  "agentId": "a8f39573a6a14d297",
  "type": "user",
  "uuid": "6ce76176-9885-4702-a5c4-577c321ce200",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "b364c86e-c33c-4dfc-add1-ad49dc9f2992",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-23T20:01:05.803Z_

```json
{
  "parentUuid": "6ce76176-9885-4702-a5c4-577c321ce200",
  "isSidechain": true,
  "agentId": "a8f39573a6a14d297",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterWorktree",
      "ExitWorktree",
      "ListMcpResourcesTool",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "ReadMcpResourceTool",
      "RemoteTrigger",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__director_get_project_overview",
      "mcp__agent-ml-research__director_post_to_reviewer",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__submit_dream_review_report"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "8c6baff4-5ed9-4ba0-aa00-62ba19ce4bfa",
  "timestamp": "2026-05-23T20:01:05.803Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "b364c86e-c33c-4dfc-add1-ad49dc9f2992",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-23T20:02:17.412Z_



## Review: "Measuring Differential Vulnerability to Policy Ambiguity Across LLM Agent Families"

---

### 1. Summary

This paper investigates how ambiguity in natural-language policies causes safety violations in LLM-based agents, using a matched-pair perturbation design across 5 models, 6 ambiguity types, and ~3,000 episodes on the tau-squared benchmark. The authors report a large universal effect (+34pp violation increase), a type hierarchy with small effect size, a fragile layer distinction, and model-by-type interactions. The work is methodologically ambitious in its attempt at causal identification through perturbation control and includes extensive calibration, but several findings are weaker than presented and generalizability remains uncertain.

---

### 2. Strengths

- **Perturbation control design is well-conceived.** The synonym/reorder control (Table 4, Delta=-0.67pp, CI covering zero) is the right idea for ruling out surface-form confounds. This is the strongest methodological contribution and is rarely seen in LLM safety evaluation work.

- **Judge calibration is thorough and above standard.** Weighted kappa of 0.807 for human-LLM agreement, with a no-same-family-bias check, exceeds what most papers in this space provide. The pre-registered thresholds add credibility.

- **Test-retest reliability is high.** ICC=0.919 overall across 360 episodes demonstrates that the measurement instrument is stable, which is a prerequisite for all downstream claims. The spec/linguistic ICC split (0.807-0.857 vs 0.976-0.989) is honestly reported and informative.

- **Honest self-correction on C3.** The authors report the pooled p=0.017 but then show it dissolves within judge subgroups (p=0.059, p=0.157) and appropriately downgrade the claim to "suggestive." This is good scientific practice that builds trust in the other claims.

- **Matched-pair within-clause design** removes between-clause confounds that plague most prompt-perturbation studies. Each ambiguous clause has a specific unambiguous counterpart, which is a cleaner comparison than typical category-level contrasts.

- **Scale and coverage.** 5 models spanning 4 provider families, 300 clause pairs, ~3,000 episodes is a substantial evaluation for this type of study.

- **Demoting the failure-mode analysis to exploratory** given the poor human-LLM kappa (0.22) on trace coding is the right call and shows methodological self-awareness.

---

### 3. Weaknesses

- **Token-length asymmetry is a serious confound.** Disambiguation tokens average 35.2 vs 18.4 — ambiguous clauses are systematically shorter. The logistic regression includes a token-delta covariate (coef=0.022, p=0.0005), but this coefficient is *significant*, meaning length *does* predict violations even after controlling for condition. The perturbation control uses synonym/reorder changes that preserve approximate length, so it does not address the *systematic* length asymmetry between ambiguous and unambiguous conditions. The causal claim for C1 therefore rests on the assumption that the length effect is fully captured by a linear covariate, which is not tested (no nonlinear terms, no length-matched subset analysis). This is the paper's most important methodological gap.

- **Realism validation partially fails.** 2 of 4 KS tests are significant (sentence length p=.028, parse depth p=.039), meaning synthetic clauses are distributional outliers on half the tested dimensions. The explanation (matched-pair requiring extra disambiguation text) is plausible but *exactly describes a systematic confound* — if real-world ambiguous policies are shorter and simpler, then the benchmark inflates the effect by using unnaturally long/complex ambiguous clauses. No robustness check is provided (e.g., filtering to the subset of clauses that fall within the real-world distribution).

- **SOPBench replication substantially attenuates results.** Delta drops from 34pp to 14.2pp, only 3/5 models reach significance, and the type-rank correlation is rho=0.20 (n.s.). The authors attribute this to domain differences, but this is exactly the generalizability test — and it shows the effect is benchmark-dependent. The type hierarchy (C2) in particular does not replicate at all, which undermines the claim that incompleteness is universally the most dangerous type.

- **C2 effect size is trivially small.** V=0.137 is below the conventional 0.20 threshold for a "medium" effect. The 22pp spread (53.6% to 31.6%) sounds large in absolute terms, but Cramer's V accounts for the marginals and sample size. The TOST analysis shows only 4/15 pairwise comparisons are equivalent at +/-10pp, meaning the type hierarchy is "not nothing" but also "not clearly structured" — many pairs are in an ambiguous zone where we can neither confirm a difference nor rule one out.

- **C4 is driven by DeepSeek's lack of differentiation.** The interaction claim partly relies on DeepSeek showing chi-squared=6.31, p=0.277 (no type effect), which could reflect model capability rather than a genuine interaction. DeepSeek may simply be worse at following policies generally, floor-effecting type differences. The paper does not test for floor/ceiling effects or provide type-specific violation rates for DeepSeek to assess this.

- **N=25 for human re-annotation is underpowered for its purpose.** The paper uses this to validate LLM trace coding, finds kappa=0.22, and correctly demotes the failure-mode analysis. But the poor agreement also means we have *no validated understanding of why models fail*, which limits the paper's practical utility. More importantly, human-human kappa=0.48 suggests the coding scheme itself is unreliable, not just the LLM coders.

- **Single benchmark (primarily).** The main results are on tau-squared-bench only. SOPBench is relegated to an appendix and shows attenuation. The 300 clause pairs are all authored by the research team (or generated/curated by them), raising questions about construct validity — do these 6 types exhaust the relevant ambiguity space? No theoretical justification or coverage analysis is provided for the typology.

- **No behavioral baselines.** The paper compares ambiguous vs. unambiguous but never compares against other known safety-relevant perturbations (e.g., jailbreaks, adversarial prompts). Without this, we cannot calibrate whether +34pp is large or small relative to other safety risks. The OR=15.1 sounds dramatic but is relative to a low baseline violation rate under unambiguous conditions.

---

### 4. Questions for Authors

1. **Length confound**: Have you run analyses on a length-matched subset (e.g., clauses where ambiguous and unambiguous versions differ by <5 tokens)? Does the +34pp effect hold? Have you tested quadratic or interaction terms for token delta in the logistic regression?

2. **SOPBench attenuation**: The type-rank rho=0.20 is non-significant. Do you view C2 as replicated or not? If the type hierarchy is benchmark-specific, what is the generalizable contribution?

3. **DeepSeek floor effect**: What is DeepSeek's overall violation rate under ambiguous conditions? If it is near ceiling (e.g., >60%), the lack of type differentiation is expected and does not constitute a genuine model-by-type interaction.

4. **Realism gap**: For the 2 metrics where KS tests are significant, can you show that restricting to clauses within the real-world distribution does not change the main results?

5. **Perturbation control scope**: The control uses synonym/reorder on *unambiguous* clauses (if I read correctly). Does it also include perturbations of *ambiguous* clauses to verify that meaning-preserving changes to ambiguous text also preserve violation rates?

6. **Typology coverage**: How were the 6 types selected? Is there a linguistic or legal taxonomy that justifies these as exhaustive or representative? Could other types (e.g., presupposition failures, pragmatic implicature) yield different patterns?

7. **Convergent nocuity (27%)**: This is an interesting finding but seems post-hoc. Is there any analysis of *which* clauses produce convergent failures? Are they disproportionately from one type?

---

### 5. Soundness: 3/5

The perturbation control and judge calibration are strong, but the token-length asymmetry is a real confound that is not adequately addressed. The causal claim for C1 is plausible but not airtight. C2 has trivial effect size and does not replicate on SOPBench. C3 is honestly reported as fragile. C4 may be partially artifactual (DeepSeek floor effect). The partial realism validation failure adds further uncertainty.

### 6. Excitement: 3/5

The research question is timely and practically important — policy ambiguity is a real deployment concern for LLM agents. The matched-pair perturbation design is a genuine methodological contribution. However, the findings are somewhat expected (ambiguity causes more violations — yes), the type hierarchy is weak and non-replicating, and the lack of validated failure-mode analysis limits actionable insights. The benchmark release of 300 clause pairs has value but would benefit from broader validation.

### 7. Reproducibility: 4/5

The paper provides substantial methodological detail: clause counts, episode counts, statistical tests, confidence intervals, pre-registered thresholds, and mentions a benchmark release. The matched-pair design is clearly described. Points deducted because: (a) the clause generation/curation process is not fully detailed (how were ambiguities crafted?), and (b) the benchmark release is promised but its current availability is unclear.

### 8. Overall Assessment: 3.0

**Findings-level accept.** The paper addresses a relevant problem with a well-designed perturbation framework and thorough calibration, which are genuine contributions. However: (1) the token-length confound weakens the causal claim; (2) the type hierarchy has trivially small effect size and fails to replicate; (3) the layer distinction (C3) is acknowledged as unsupported; (4) SOPBench shows substantial attenuation, raising generalizability concerns; and (5) the failure-mode analysis is invalidated by its own human evaluation. The work is honest and methodologically competent but the findings are not strong or novel enough for the main conference. The matched-pair design and perturbation control methodology are the lasting contributions, suitable for Findings.

### 9. Confidence: 4/5

I have carefully examined the statistical claims, study design, and calibration procedures. I am familiar with LLM evaluation methodology and matched-pair experimental designs. My main uncertainty is whether the token-length issue is as consequential as I suspect — a length-matched subset analysis could resolve this either way.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c6baff4-5ed9-4ba0-aa00-62ba19ce4bfa",
  "isSidechain": true,
  "agentId": "a8f39573a6a14d297",
  "requestId": "req_011CbL6WTh4QkT3ftZZswco1",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1301fcf9-1aa1-437c-8482-c45bf004a3b7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety",
  "sessionId": "b364c86e-c33c-4dfc-add1-ad49dc9f2992",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016AR23EVork4iSKDyQzg9uN",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9275,
      "cache_read_input_tokens": 7667,
      "output_tokens": 2600,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9275
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2600,
          "cache_read_input_tokens": 7667,
          "cache_creation_input_tokens": 9275,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9275,
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
