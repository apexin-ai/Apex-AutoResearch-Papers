# Research conversation: You are Reviewer R1 for a top ML venue review. Your focus: **Methods and Experiments**. Review standard: top ML venue, ~

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 20
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac47f85168ca4027f.jsonl`
- **Structured JSON:** [`975785b1a9dfa224c391.json`](../../sessions/97/975785b1a9dfa224c391.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

45 recorded events

### User

_source line 1 · 2026-05-16T08:14:34.530Z_

You are Reviewer R1 for a top ML venue review. Your focus: **Methods and Experiments**. Review standard: top ML venue, ~25% acceptance, 6-point scale (1=Strong Reject … 6=Strong Accept).

## Paper Summary
"Phase-Dependent Compound Sparsity: Strategy–Phase Interactions Modulate Severity in Efficient LLM Inference"

The paper studies compound sparsity (simultaneous attention head pruning + KV cache eviction) and argues that the resulting interaction severity is NOT a uniform constant but depends on eviction strategy and reasoning phase. Key claims:
1. Phase-modulated severity gradient: compound severity increases monotonically with sparsity, importance-based eviction >> random
2. Task-modulated strategy specificity: imp/random ratio is 15× on MATH-500, 2.3–3.8× on GSM8K, 2.3–3.2× on GPQA Diamond
3. Architecture-dependent interaction: LLaMA-8B replicates within-importance gradient (dz≈1.0) but strategy×phase interaction is weak (dz 0.18–0.33)
4. Discrimination collapse mechanism: head pruning degrades importance score discriminability (Gini/CV reduction)

## Experimental Design (from review_context.yaml — the full planned experiment list)
The paper was supposed to cover these experiments:
1. **c8_llama_n250_fixed**: LLaMA-8B n=250, 8 conditions on MATH-500. Expected: phase gradient stable (dz~1.0), imp_vs_rand weak (only s030 Bonferroni sig)
2. **gpqa_ds_importance_s015**: GPQA Diamond × DeepSeek × importance × s015 (n=198)
3. **gpqa_ds_full_pipeline**: GPQA Diamond full 10-run pipeline (DS+QW × importance×4 + random×2). Expected specificity ratio 2.3–3.2×
4. **qwen25_14b_math500**: Qwen2.5-14B × MATH-500 × 5 runs. Expected: monotonic, ~75-91% of 7B magnitude
5. **c10_lang_s020_s025_analysis**: Language switching at s020/s025, full chain dense→s030
6. **gpqa_think_validation**: GPQA &lt;/think> phase segmentation validation (kappa=0.82 expected)

## Paper Content (8 pages)

**Section 3 - Method:**
- Compound sparsity = head pruning + KV eviction simultaneously
- Interaction Intensity (II) = deviation of compound effect from sum of individual effects
- Phase segmentation: quantile-based division into low-sparsity (early reasoning) and high-sparsity (late reasoning) phases
- Validated against &lt;/think> markers: κ=0.88 MATH-500, κ=0.82 GPQA
- 4 sparsity levels: s015, s020, s025, s030
- 2 strategies: importance-based, random
- Stats: paired median difference, Wilcoxon with Bonferroni, bootstrap CIs (B=10000), Cohen's dz

**Section 4 - Experiments:**

Table 1 (MATH-500, n=500, importance):
- DS: median diff 0.39→1.21→3.99→8.48, Cohen's d 0.61 (s015) to 1.13 (s030)
- QW: median diff 0.07→0.31→1.07→3.16, Cohen's d 0.37 to 1.44
- Perfect monotonicity (ρ=1.0)

Table 2 (GPQA Diamond, n=198):
- DS importance: 0.24→0.68→1.85→3.92
- QW importance: 0.04→0.19→0.72→1.68
- DS random: –/–/0.58/1.21; QW random: –/–/0.31/0.72
- Imp/Random ratio: DS 3.2×, QW 2.3×

Table 3 (Cross-benchmark DS importance):
- MATH-500: 0.39/1.21/3.99/8.48
- GSM8K: 0.241/0.740/1.992/4.682
- GPQA: 0.24/0.68/1.85/3.92
- All monotonic (3/3)

Table 4 (Strategy specificity across benchmarks):
- MATH-500 DS: 15.5×/16.6×; QW: 2.7×/3.5×
- GSM8K DS: 3.8×/2.8×; QW: ~3×/~2.5×
- GPQA DS: 3.2×/3.2×; QW: 2.3×/2.3×

Table 5 (LLaMA-8B, n=250, MATH-500):
- Importance phase gradient dz: 0.98/1.05/1.08/0.97
- Random phase gradient dz: 0.33/0.37/0.42/0.44
- Imp vs Random dz: 0.18/0.24/0.28/0.33
- Bonferroni p: 0.34/0.12/0.065/0.018 (only s030 sig)

Table 6 (LLaMA n=250 vs n=50):
- All metrics stable, CIs narrower

Table 7 (Qwen2.5-14B, n=50):
- QW-14B: 0.055/0.28/0.92/2.35
- Ratio to 7B: 0.83×/0.91×/0.86×/0.74×
- Random s030: 0.68 (p=0.02), ratio 3.5×

Table 8 (Language switching):
- Switch rate: 0%→4%→14%→32%→40%
- Correlation with II: r=0.55

Section 4.7: GPQA phase validation κ=0.82

Section 5 (Discrimination Collapse):
- Gini/CV decrease under pruning across all models (30 problems each)
- Entropy redistribution: consistent on DS, inconsistent on QW
- Mechanism explains direction but not magnitude of cross-arch differences

## Your Task
Evaluate the paper on these dimensions:
1. **Methodological soundness**: Is II well-defined? Is the phase segmentation justified? Are the statistical tests appropriate?
2. **Experimental completeness**: Compare paper content against the planned experiments. Are key experiments missing? Are sample sizes adequate?
3. **Statistical rigor**: Are multiple comparison corrections applied properly? Are effect sizes reported and interpreted correctly? Any p-hacking concerns?
4. **Reproducibility**: Is there enough detail to replicate?
5. **Internal consistency**: Do the numbers add up? Are claims supported by the data shown?
6. **Weaknesses in experimental design**: confounds, alternative explanations, missing controls

Provide your assessment structured as:
- Summary of contributions (2-3 sentences)
- Strengths (bulleted)
- Weaknesses (bulleted, numbered W1, W2, ...)
- Questions for authors (numbered Q1, Q2, ...)
- Minor issues
- Preliminary score (1-6) and confidence (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "41d522dd-a785-4a41-841b-7d381b655a70",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-16T08:14:34.534Z_

```json
{
  "parentUuid": "41d522dd-a785-4a41-841b-7d381b655a70",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
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
  "uuid": "e3ec0e98-ea17-4e7c-8ab7-99d1d87bc8da",
  "timestamp": "2026-05-16T08:14:34.534Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 3 · 2026-05-16T08:14:44.292Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013gAAWa5bbtxUnXisB5v3m6`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__director_get_project_overview",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e3ec0e98-ea17-4e7c-8ab7-99d1d87bc8da",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uyD8dBR6gfN7EqEJTV",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "48aee927-5c03-468b-8342-51463ef162c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01M5NCokZ5ypNhh96Gw3J3EJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 15907,
      "cache_read_input_tokens": 0,
      "output_tokens": 105,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15907
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 105,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15907,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15907,
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

_source line 4 · 2026-05-16T08:14:44.303Z_

<details><summary>↩ Tool result · `toolu_013gAAWa5bbtxUnXisB5v3m6`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_get_project_overview"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "48aee927-5c03-468b-8342-51463ef162c8",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "cfaf3ab0-2e7d-4417-bf02-5d5bb6755c63",
  "sourceToolAssistantUUID": "48aee927-5c03-468b-8342-51463ef162c8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 5 · 2026-05-16T08:14:48.237Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_011h3he9yVaJF24ECmuev7SH`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "paper_provenance.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cfaf3ab0-2e7d-4417-bf02-5d5bb6755c63",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uywDhCxpQjmYdfRzjf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e6a25bf3-93c7-4648-8394-8ee3994370f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnqsYCj7mSDjaS2sPauReU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 15907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 6 · 2026-05-16T08:14:48.254Z_

<details><summary>↩ Tool result · `toolu_011h3he9yVaJF24ECmuev7SH`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/paper_provenance.yaml\", \"content\": \"paper:\\n  title: ''\\n  version: 46\\n  generated_at: '2026-05-14T09:35:02.234990+00:00'\\nclaims:\\n- id: C001\\n  location:\\n    section: background\\n    paragraph: 0\\n    sentence: 0\\n  text: mean/median ratio reaches 33.5x for low-sparsity phase at s=0.30\\n  type: quantitative\\n  evidence:\\n  - exp_id: v6_importance_s030\\n    metric: ii_low_mean / ii_low_median\\n    value: 1163.97 / 34.69 = 33.5\\n  decisions: []\\n  deprecated: false\\n- id: C002\\n  location:\\n    section: background\\n    paragraph: 0\\n    sentence: 0\\n  text: Bootstrap CI with B=10,000 resamples at problem level\\n  type: methodological\\n  evidence:\\n  - exp_id: v6_importance_s030\\n    metric: bootstrap_B\\n    value: 10000, confirmed in v6_analysis_results.json\\n  decisions: []\\n  deprecated: false\\n- id: C003\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Head pruning causes phase-dependent attention redistribution: entropy increases\\n    more in low-sparsity phases due to lower head redundancy'\\n  type: mechanistic_hypothesis\\n  evidence:\\n  - conceptual_argument\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C005\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Attention redistribution degrades discriminative power of importance scores,\\n    causing importance-based eviction to degenerate toward biased random eviction\\n    in low-sparsity phases\\n  type: mechanistic_hypothesis\\n  evidence:\\n  - conceptual_argument\\n  - crossover_phenomenon_C3\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C008\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Random eviction is immune to entropy-discrimination collapse because its decisions\\n    are independent of attention patterns\\n  type: explanatory\\n  evidence:\\n  - flat_gradient_C1\\n  decisions: []\\n  deprecated: true\\n- id: C012\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: 'The mechanism is architecture-general: any attention-mass-based importance\\n    metric combined with head pruning should exhibit phase-modulated compound severity'\\n  type: prediction\\n  evidence:\\n  - conceptual_argument\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C013\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Phase-modulated severity: n=500 median D (II_low - II_high) 0.39→1.21→3.99→8.48,\\n    robust d_z 0.77→0.94 (medium→large)'\\n  type: quantitative\\n  evidence:\\n  - exp_id: c2_n500_deepseek\\n    metric: median_D\\n    value: 's015=0.391, s020=1.215, s025=3.986, s030=8.481'\\n  - exp_id: c2_n500_deepseek\\n    metric: robust_dz_range\\n    value: '0.773 (s025→s030) to 0.944 (s015→s030)'\\n  - exp_id: c2_n500_deepseek\\n    metric: wilcoxon_bonf_k4\\n    value: 'all 4 levels p<1e-69'\\n  decisions:\\n  - D033\\n  - D035\\n  - D066\\n  deprecated: false\\n- id: C015\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: High-sparsity phase II < 1 at all sparsity levels (near-additive)\\n  type: quantitative\\n  evidence:\\n  - exp_id: deepseek_bf16_importance\\n    metric: ii_high_median\\n    value: 'pending bf16 data (fp16 reference: 0.23->0.88)'\\n  decisions: []\\n  deprecated: false\\n- id: C018\\n  location:\\n    section: discussion\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Crossover at s>=0.25: importance outperforms random in high-sparsity phase,\\n    underperforms in low-sparsity phase'\\n  type: qualitative\\n  evidence:\\n  - exp_id: mvp_v5_fixed_s025\\n    metric: ii_high_median\\n    value: 0.584 vs random 3.002\\n  - exp_id: mvp_v5_fixed_s025\\n    metric: ii_low_median\\n    value: 30.903 vs random 2.915\\n  decisions: []\\n  deprecated: false\\n- id: C019\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Compound sparsity severity is strategy-dependent: importance-based eviction\\n    produces monotonically increasing median difference (0.39→14.59, d=0.44→0.80)\\n    while random eviction shows no significant phase difference'\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  - deepseek_bf16_random\\n  decisions:\\n  - D015\\n  deprecated: true\\n- id: C019b\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Compound sparsity severity is strategy-dependent: importance-based eviction\\n    produces monotonically increasing median difference across all sparsity levels;\\n    random eviction NS at s015/s020 but significant at s025+ with effect size 3-39x\\n    smaller than importance (threshold ~s020-s025, D063)'\\n  type: empirical\\n  evidence:\\n  - c2_n500_deepseek\\n  - c2_qw_n500_r3\\n  decisions:\\n  - D015\\n  - D063\\n  deprecated: false\\n- id: C021\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Severity is phase-modulated: low-sparsity reasoning phases bear disproportionate\\n    compound degradation under importance-based eviction'\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  decisions:\\n  - D015\\n  deprecated: false\\n- id: C024\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Severity gradient growth is sub-exponential with decreasing growth rate\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  decisions: []\\n  deprecated: false\\n- id: C028\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'Phase-strategy crossover: importance-based eviction outperforms random in\\n    high-sparsity phase but underperforms in low-sparsity phase'\\n  type: empirical\\n  evidence:\\n  - deepseek_bf16_importance\\n  - deepseek_bf16_random\\n  decisions:\\n  - D015\\n  deprecated: false\\n- id: C033\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model replication on Qwen2.5-7B-Instruct qualitatively reproduces the\\n    phase-modulated severity gradient\\n  type: empirical\\n  evidence:\\n  - qwen_bf16_importance\\n  decisions: []\\n  deprecated: false\\n- id: C039\\n  location:\\n    section: results\\n    paragraph: 0\\n    sentence: 0\\n  text: 'DeepSeek: all 4 sparsity levels significant (Wilcoxon p<1e-69, Bonferroni\\n    k=4, robust d_z 0.77-0.94). Qwen: all 4 levels significant (p<1e-13, d_z\\n    0.63-0.92). JT dose-response: all groups p<1e-9.'\\n  type: statistical\\n  evidence:\\n  - exp_id: c2_n500_deepseek\\n    metric: wilcoxon_bonf_k4\\n    value: 'all 4 levels p<1e-69 (n=496)'\\n  - exp_id: c2_n500_deepseek\\n    metric: robust_dz\\n    value: '0.773/0.824/0.925/0.944'\\n  - exp_id: c2_qw_n500_r3\\n    metric: wilcoxon_bonf_k4\\n    value: 'all 4 levels p<1e-13 (n=475)'\\n  - exp_id: c2_qw_n500_r3\\n    metric: robust_dz\\n    value: '0.629/0.767/0.865/0.923'\\n  - metric: jt_test\\n    value: 'DS imp z=33.7 p<1e-200; QW imp z=30.1 p<1e-200'\\n  decisions:\\n  - D035\\n  - D036\\n  - D066\\n  deprecated: false\\n- id: C040\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Compound sparsity severity is strategy-dependent\\n  type: confirmed\\n  evidence:\\n  - 'n=500: DS importance median D 0.39→8.48 (all bonf_k4 p<1e-69); random NS at\\n    s015/s020, significant at s025+ (bonf_k4 p=0.006) but effect size 15-39x smaller\\n    (D063 threshold narrative)'\\n  - exp_id: c2_n500_deepseek\\n  - exp_id: c2_qw_n500_r3\\n  decisions:\\n  - C1\\n  - D063\\n  deprecated: false\\n- id: C042\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Severity is phase-modulated with monotonic increase\\n  type: confirmed\\n  evidence:\\n  - Bonferroni p less than 0.005 all levels\\n  - Cohen d 0.44 to 0.80\\n  decisions:\\n  - C2\\n  deprecated: false\\n- id: C045\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Phase-strategy crossover exists at s>=0.25\\n  type: confirmed\\n  evidence:\\n  - exp_id: c2_n500_deepseek\\n    metric: imp_vs_rand_s025\\n    value: 'imp median D=3.99 (low>>high) vs rand D=0.26 (nearly flat); importance\\n      concentrates severity in low phase while random distributes uniformly'\\n  - exp_id: c2_qw_n500_r3\\n    metric: imp_vs_rand_s025\\n    value: 'imp median D=1.07 vs rand D=0.39; same crossover pattern'\\n  - exp_id: c2_n500_deepseek\\n    metric: imp_vs_rand_bonf_k4\\n    value: 'all 4 sparsity levels p<1e-39'\\n  decisions:\\n  - C3\\n  - D066\\n  deprecated: false\\n- id: C049\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Entropy-discrimination collapse mechanism\\n  type: partially_confirmed\\n  evidence:\\n  - correlational support\\n  - causal validation pending\\n  decisions:\\n  - C4\\n  deprecated: false\\n- id: C054\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model replication on Qwen2.5-7B-Instruct\\n  type: confirmed\\n  evidence:\\n  - 4/4 PASS at s>=0.20\\n  - Spearman rho=1.0\\n  - permutation p=0.043\\n  decisions:\\n  - C5\\n  deprecated: false\\n- id: C060\\n  location:\\n    section: conclusion\\n    paragraph: 0\\n    sentence: 0\\n  text: Severity gradient is sub-exponential\\n  type: confirmed\\n  evidence:\\n  - decelerating growth rate\\n  decisions:\\n  - C6\\n  deprecated: false\\n- id: C061\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Compound sparsity severity is an emergent phase-strategy interaction\\n  type: confirmed\\n  evidence:\\n  - 'n=500: DS importance median D 0.39→8.48 (all p<1e-69); QW importance 0.07→3.15\\n    (all p<1e-13)'\\n  - 'random: NS at s015/s020, significant at s025+ with effect size 3-39x smaller\\n    than importance (D063 threshold ~s020-s025)'\\n  decisions:\\n  - C1\\n  - C2\\n  - D063\\n  deprecated: false\\n- id: C063\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Crossover at s=0.25\\n  type: confirmed\\n  evidence:\\n  - importance high=0.584 vs random=3.002\\n  - importance low=30.903 vs random=2.915\\n  decisions:\\n  - C3\\n  deprecated: false\\n- id: C066\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Cross-model replication\\n  type: confirmed\\n  evidence:\\n  - Spearman rho=1.0\\n  - permutation p=0.043\\n  decisions:\\n  - C5\\n  deprecated: false\\n- id: C070\\n  location:\\n    section: abstract\\n    paragraph: 0\\n    sentence: 0\\n  text: Entropy-discrimination collapse mechanism\\n  type: partially_confirmed\\n  evidence:\\n  - proposed mechanism\\n  - correlational support\\n  decisions:\\n  - C4\\n  deprecated: false\\n- id: C071\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Gini delta is negative across all 16 conditions (2 models x 2 strategies x\\n    4 sparsity levels), indicating robust KV discrimination collapse\\n  type: empirical\\n  evidence:\\n  - c4_entropy\\n  - qwen_c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C073\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: DeepSeek importance entropy delta is consistently negative (-0.040 to -0.047,\\n    std 0.02-0.03) across all sparsity levels\\n  type: empirical\\n  evidence:\\n  - c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C076\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Qwen importance entropy delta partially replicates (2/4 sparsity levels negative;\\n    s025 reverses to +0.045 with 22/30 problems positive)\\n  type: empirical\\n  evidence:\\n  - qwen_c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C080\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Qwen s025 entropy reversal is consistent across all three phase categories,\\n    not explained solely by mid-phase statistical power limitations\\n  type: empirical\\n  evidence:\\n  - qwen_c4_entropy\\n  decisions: []\\n  deprecated: true\\n- id: C081\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Discrimination collapse (Gini/CV decrease) is robustly observed across both\\n    models in all 16 tested conditions\\n  type: confirmed\\n  evidence:\\n  - c4_entropy_deepseek\\n  - c4_entropy_qwen\\n  decisions: []\\n  deprecated: false\\n- id: C083\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Entropy redistribution is consistent for DeepSeek (4/4 conditions) but partially\\n    replicates on Qwen (2/4 conditions)\\n  type: partially_confirmed\\n  evidence:\\n  - c4_entropy_deepseek\\n  - c4_entropy_qwen\\n  decisions: []\\n  deprecated: false\\n- id: C086\\n  location:\\n    section: analysis\\n    paragraph: 0\\n    sentence: 0\\n  text: Qwen s=0.25 entropy reversal is systematic across all three reasoning phases\\n    (22/30 problems positive)\\n  type: confirmed\\n  evidence:\\n  - c4_entropy_qwen\\n  decisions: []\\n  deprecated: false\\ntables:\\n- id: discrimination-metrics\\n  location:\\n    section: analysis\\n    table_number: 0\\n  caption: ''\\n  cells:\\n  - row: DeepSeek s=0.15\\n    col: Gini\\n    value: '-0.030'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s015_importance.gini_delta_mean\\n  - row: DeepSeek s=0.20\\n    col: Gini\\n    value: '-0.040'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s020_importance.gini_delta_mean\\n  - row: DeepSeek s=0.25\\n    col: Gini\\n    value: '-0.065'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s025_importance.gini_delta_mean\\n  - row: DeepSeek s=0.30\\n    col: Gini\\n    value: '-0.081'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s030_importance.gini_delta_mean\\n  - row: DeepSeek s=0.15\\n    col: CV\\n    value: '-0.56'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s015_importance.cv_delta_mean\\n  - row: DeepSeek s=0.20\\n    col: CV\\n    value: '-0.77'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s020_importance.cv_delta_mean\\n  - row: DeepSeek s=0.25\\n    col: CV\\n    value: '-1.29'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s025_importance.cv_delta_mean\\n  - row: DeepSeek s=0.30\\n    col: CV\\n    value: '-1.66'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s030_importance.cv_delta_mean\\n  - row: Qwen s=0.15\\n    col: Gini\\n    value: '-0.010'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s015_importance.gini_delta_mean\\n  - row: Qwen s=0.20\\n    col: Gini\\n    value: '-0.012'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s020_importance.gini_delta_mean\\n  - row: Qwen s=0.25\\n    col: Gini\\n    value: '-0.010'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s025_importance.gini_delta_mean\\n  - row: Qwen s=0.30\\n    col: Gini\\n    value: '-0.020'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s030_importance.gini_delta_mean\\n  - row: Qwen s=0.15\\n    col: CV\\n    value: '-0.05'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s015_importance.cv_delta_mean\\n  - row: Qwen s=0.20\\n    col: CV\\n    value: '-0.21'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s020_importance.cv_delta_mean\\n  - row: Qwen s=0.25\\n    col: CV\\n    value: '-1.49'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s025_importance.cv_delta_mean\\n  - row: Qwen s=0.30\\n    col: CV\\n    value: '-1.14'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s030_importance.cv_delta_mean\\n  deprecated: false\\n- id: entropy-deltas\\n  location:\\n    section: analysis\\n    table_number: 0\\n  caption: ''\\n  cells:\\n  - row: DeepSeek s=0.15\\n    col: entropy\\n    value: '-0.040'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s015_importance.entropy_delta_mean\\n  - row: DeepSeek s=0.20\\n    col: entropy\\n    value: '-0.047'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s020_importance.entropy_delta_mean\\n  - row: DeepSeek s=0.25\\n    col: entropy\\n    value: '-0.045'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s025_importance.entropy_delta_mean\\n  - row: DeepSeek s=0.30\\n    col: entropy\\n    value: '-0.044'\\n    source:\\n      exp_id: c4_entropy_deepseek\\n      metric: s030_importance.entropy_delta_mean\\n  - row: Qwen s=0.15\\n    col: entropy\\n    value: '-0.073'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s015_importance.entropy_delta_mean\\n  - row: Qwen s=0.20\\n    col: entropy\\n    value: '-0.076'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s020_importance.entropy_delta_mean\\n  - row: Qwen s=0.25\\n    col: entropy\\n    value: '+0.045'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s025_importance.entropy_delta_mean\\n  - row: Qwen s=0.30\\n    col: entropy\\n    value: '-0.007'\\n    source:\\n      exp_id: c4_entropy_qwen\\n      metric: s030_importance.entropy_delta_mean\\n  deprecated: false\\nfigures: []\\n_completeness:\\n  coverage: 24/24\\n  claims: 24\\n  tables: 2\\n  figures: 0\\n  tier_counts:\\n    tier1: 0\\n    tier2: 24\\n    tier3: 0\\n    tierX: 0\\n  last_checked: '2026-05-14T09:35:02.235034+00:00'\\n\", \"total_chars\": 16083, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e6a25bf3-93c7-4648-8394-8ee3994370f3",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "67089ad5-af36-426f-9918-0a6744f557c9",
  "sourceToolAssistantUUID": "e6a25bf3-93c7-4648-8394-8ee3994370f3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 7 · 2026-05-16T08:14:48.771Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01H9MnwF56nULBWXwwMCfH4e`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "decisions.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "67089ad5-af36-426f-9918-0a6744f557c9",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uywDhCxpQjmYdfRzjf",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "89383065-9d53-4a81-85c6-249f3b7e8501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PnqsYCj7mSDjaS2sPauReU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1426,
      "cache_read_input_tokens": 15907,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1426,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 48,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-16T08:14:49.079Z_

<details><summary>↩ Tool result · `toolu_01H9MnwF56nULBWXwwMCfH4e`</summary>

```text
Error: result (77,266 characters) exceeds maximum allowed tokens. Output has been saved to /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/da179c64-682b-4476-8ead-731d6820bfd5/tool-results/mcp-agent-ml-research-read_project_file-1778919289064.txt.
Format: JSON with schema: {result: string}
- For targeted queries (find a value, filter by field): use jq on the file directly.
- For analysis or summarization that requires reading the full content: first probe the structure (e.g., jq 'type, length, keys?' /home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/da179c64-682b-4476-8ead-731d6820bfd5/tool-results/mcp-agent-ml-research-read_project_file-1778919289064.txt), then extract slices with jq or python — Read's line-based offset/limit will not chunk this file.
- If the Agent tool is available, do this inside a subagent so the full output stays out of your main context. Give it the instruction above verbatim, and be explicit about what it must return — e.g. "/home/ubuntu/.claude-account-3/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-11-projects-phase-gated-compound-sparse/da179c64-682b-4476-8ead-731d6820bfd5/tool-results/mcp-agent-ml-research-read_project_file-1778919289064.txt is JSON with schema: {result: string}; probe the structure with jq (type/length/keys), then extract and read the content in full with jq or python, then summarize and quote any key findings verbatim." A vague "summarize this" may lose detail.

```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "89383065-9d53-4a81-85c6-249f3b7e8501",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "2d49d70f-21dc-44de-9f77-673809162683",
  "sourceToolAssistantUUID": "89383065-9d53-4a81-85c6-249f3b7e8501",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-16T08:14:52.833Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01StayPQR8NpY9gCYoRY9PCL`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "ROADMAP.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2d49d70f-21dc-44de-9f77-673809162683",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uzHCyMrcnfyLuFVkuY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c9d60770-d48d-40d2-a087-6afcf9bf777c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaUnQqmnhhDwFUKfZ8aHDB",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7289,
      "cache_read_input_tokens": 17333,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7289,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 50,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-16T08:14:52.843Z_

<details><summary>↩ Tool result · `toolu_01StayPQR8NpY9gCYoRY9PCL`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/ROADMAP.md\", \"content\": \"# phase-gated-compound-sparse — Research Dashboard\\n\\n> 最后更新: 2026-05-16 04:36 UTC | 更新原因: 目标会议更新为 EMNLP 2025 main + headline 验证通过 + GPU0 状态更新 + 远程 tex 同步\\n\\n> 核心文档链: paper_framing.md → experiment_plan.yaml → 本 ROADMAP\\n\\n## 核心方向\\n**Phase-modulated compound sparsity severity**：importance-based eviction 的 compound interaction severity 随 sparsity 单调递增（n=500 confirmed）。详见 paper_framing.md。\\n\\n## 目标会议\\nEMNLP 2025 main conference — **截稿 2026-05-25（距今 9 天）**（没中延 Findings）\\n\\n## 当前进展\\n- 阶段：**Round 10 修订收尾 → 接近 Round 11 提交**\\n- 129 实验完成（63 success / 17 negative / 17 failed），38 plan experiments 全部 done（coverage 92.1%）\\n- 实验侧：5/6 CPU 任务完成，仅剩 c8_llama_n250_fixed（GPU running）+ c10_lang_s020_s025（GPU running）\\n- 写作侧：4/4 主要修正完成（bib审计✅ abstract/intro✅ §4-7✅ appendix✅），headline 数字一致性已验证通过✅\\n\\n## ⚠️ Round 11 提交前 Blocking Checklist\\n- [x] **Headline 数字一致性**：本地 tex 全部使用 n=500 数据（Reviewer + Worker 双重验证通过）。远程旧副本 rsync 同步中\\n- [ ] c8_llama_n250_fixed 完成 + 结果写入论文\\n- [x] 用户确认目标会议：EMNLP 2025 main conference（没中延 Findings）\\n- [ ] Figure 1 PDF 生成 → 已派 Worker，生成中\\n- [x] 远程 tex 同步完成验证（74 文件 rsync，旧数字已清除）\\n- [ ] Round 11 提交\\n\\n## Round 10 修订进度\\n\\n### 实验任务\\n- [x] **P1-CPU** &lt;think> token position validation — DONE (D093: adaptive κ=0.8804)\\n- [x] **P1-CPU** Per-phase Gini decomposition — DONE (Reviewer PASS: DS+QW 30/30, low_delta > mid > high)\\n- [x] **P2-CPU** GSM8K power analysis — DONE (D092)\\n- [x] **P2-CPU** MATH-500 language switching — DONE (c10_lang_switching success)\\n- [ ] **P1-GPU** LLaMA n=250 — c8_llama_n250_fixed RUNNING（GPU2+3）\\n- [ ] c10_lang_s020_s025 — RUNNING（GPU1）\\n\\n### 写作任务（Paper Agent）\\n- [x] MUSTAFAR 删除 + bib 全量审计 — Reviewer PASS\\n- [x] Abstract/Intro rewrite — 完成，**headline 数字需验证**（见 Blocking Checklist）\\n- [x] §4-7 corrections — Reviewer PASS\\n- [x] Appendix fixes — 完成\\n\\n## GPU 状态\\n- RTX 6000 Pro ×4: westd-22162 cuda:0~3\\n- GPU0: c8_llama_gpu0_s025 RUNNING (PID 315052, preemptive acceleration)\\n- GPU1: c10_lang_s020_s025\\n- GPU2+3: c8_llama_n250_fixed\\n- 已用: ~36h / ~250h 预算\\n\\n## 审稿回溯·系统性问题（Round 10 Holistic Pass）\\n\\n### SYSTEMIC_ISSUE #1: 写作可信度 → Paper Agent 修正完成\\nR10-C1 (MUSTAFAR ✅), R10-W1 (overclaiming ✅), R10-W3 (H2O confound ✅), R10-W4 (GPU deanon ✅), R10-W5 (statistical gaps ✅), R10-W6 (clarity ✅)\\n\\n### SYSTEMIC_ISSUE #2: 实验证据厚度 → 5/6 完成\\nR10-C3 (LLaMA n=250 running), R10-C4 (&lt;think> ✅), R10-C5 (Gini ✅), R10-W5 (pilot CI ✅)\\n\\n### 非系统性 Critical: 定位调整\\nR10-C2 → Main conference（用户确认），没中延 Findings\\n\\n## Scope 扩展（Director 批准）\\n\\n### 线路 A: GPQA Diamond（非数学推理）\\n- [ ] 数据下载 + pipeline 适配（CPU Worker 进行中）\\n- [ ] DS + QW × importance × 4 sparsities + 2 random controls = 10 runs\\n- 等 GPU 释放后开跑\\n\\n### 线路 B: 14B 模型（scale 扩展）\\n- [ ] Qwen2.5-14B-Instruct 下载（CPU Worker 进行中）\\n- [ ] MATH-500 × importance × 4 sparsities + 1 random control = 5 runs\\n- 等模型下载 + GPU 释放后开跑\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D098 | 2026-05-16 | GPQA segmentation: quantile 三分为 primary，&lt;/think> 二 | gpqa_ds_importance_s015, c4_think_validation_math500 |\\n| D097 | 2026-05-16 | 撤回 D091 Findings track framing 决策，按 EMNLP main con | — |\\n| D096 | 2026-05-16 | Session 15 决策：c10 等 c5 释放 GPU、Paper Agent 启动 Findi | c5_per_phase_gini, c8_llama_n250_fixed, c10_lang_switching |\\n| D095 | 2026-05-16 | c8_llama_n250 数据丢失，GPU 2/3 立即重跑；c10 排队等 c5 释放 GPU | c8_llama_n250, c10_lang_switching, c5_per_phase_gini |\\n| D094 | 2026-05-16 | c8_llama_n250 数据全丢事故——c10 越权 GPU 使用导致级联失败，c8 需从头重跑 | c8_llama_n250, c10_lang_switching |\\n| D093 | 2026-05-16 | &lt;think> phase validation 达标：adaptive κ=0.8804, AUC | c4_think_validation_math500 |\\n| D092 | 2026-05-16 | c9 power analysis 仅报告 random 条件；importance 条件丢弃 t- | c9_gsm8k_power_analysis |\\n| D091 | 2026-05-16 | R10 审稿 Weak Reject (2.25/5)：接受 Findings track，启动 5 | c3_llama, think_phase_validation, c4_entropy |\\n| D090 | 2026-05-16 | Round 10 dual dose curve 完成：DS 5-point (0.74→0.04) | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2, acc_qw_s030_b1_8k, acc_qw_s025_b1_8k |\\n| D089 | 2026-05-16 | DS 8k v2 揭示双 regime 结构：s≤0.20 截断驱动（非截断 acc ~71% 稳定 | acc_ds_dense_8k_v2, acc_ds_s015_8k_v2, acc_ds_s020_8k_v2, acc_ds_s025_8k_v2, acc_ds_s030_8k_v2 |\\n\\n\", \"total_chars\": 4095, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c9d60770-d48d-40d2-a087-6afcf9bf777c",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "514cf067-e804-4418-b403-f6bab2af9a3b",
  "sourceToolAssistantUUID": "c9d60770-d48d-40d2-a087-6afcf9bf777c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-16T08:14:53.240Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0143SxVFAbqeRd1oJNCKQhjm`</summary>

```json
{
  "project": "phase-gated-compound-sparse",
  "file": "report.md",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "514cf067-e804-4418-b403-f6bab2af9a3b",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uzHCyMrcnfyLuFVkuY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bbf17125-e250-4065-8cc6-98c758d1f614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01YaUnQqmnhhDwFUKfZ8aHDB",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7289,
      "cache_read_input_tokens": 17333,
      "output_tokens": 203,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7289
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 203,
          "cache_read_input_tokens": 17333,
          "cache_creation_input_tokens": 7289,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7289,
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

_source line 12 · 2026-05-16T08:14:53.257Z_

<details><summary>↩ Tool result · `toolu_0143SxVFAbqeRd1oJNCKQhjm`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/report.md\", \"content\": \"# Handover — 2026-05-16\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n| exp_id | 假设 | 状态 | 关键指标 | W&B |\\n|--------|------|------|---------|-----|\\n| gpqa_ds_importance_s015 | Cross-task generalization: compound sparsity severity monotonically increases on GPQA Diamond (non-math reasoning) using quantile 3-segment phase decomposition (primary method). DS-R1 importance s015 as first condition. | — | — | — |\\n| c8_llama_gpu0_s025 | Pre-emptive run of LLaMA importance s025 on GPU 0 to accelerate c8_llama_n250_fixed (4-round serial → 3-round by pre-completing round 2 condition) | — | — | — |\\n| c8_llama_n250_fixed | — | — | — | — |\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **c10_lang_s020_s025** (success): —\\n- **c4_think_validation_math500** (success): —\\n  [c4_think_validation_math500](/api/workspace-files/projects/phase-gated-compound-sparse/artifacts/c4_think_validation_math500/data/c4_think_validation_math500.txt)\\n- **acc_qw_s025_b1_8k** (negative): 重跑 QW importance_s025 batch1 (problems 1-50) with max_new_tokens=8192，修复原 batch1 使用 2048 的 token 预算不匹配问题。\\n\\n## 趋势\\n成功 64 / 负向 17 / 失败 17 / 共 128\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\nwestd-22162: 无 GPU 信息\\n\\n## 告警\\n- mvp_interaction_index_profiling: 训练失败 — unknown\\n- mvp_ii_profiling_v4: 训练失败 — unknown\\n- mvp_ii_profiling_v4b: 训练失败 — unknown\\n- mvp_ii_profiling_v4c: 训练失败 — unknown\\n- mvp_ii_profiling_v4d: 训练失败 — unknown\\n- mvp_ii_profiling_v4-random: 训练失败 — unknown\\n- mvp_v4a_r2: 训练失败 — unknown\\n- mvp_v4b_r2: 训练失败 — unknown\\n- mvp_v4c_r2: 训练失败 — unknown\\n- mvp_v4_legacy_s025: 训练失败 — unknown\\n- mvp_v4_legacy_s035: 训练失败 — unknown\\n- mvp_v4_float32_s030: 已被终止 — unknown\\n- mvp_v5_fixed_s020: 已被终止 — unknown\\n- mvp_v5_fixed_s030: 已被终止 — unknown\\n- qwen_importance_s015: 已被终止 — unknown\\n- qwen_importance_s020: 已被终止 — unknown\\n- qwen_importance_s025: 已被终止 — unknown\\n- qwen_importance_s030: 已被终止 — unknown\\n- v6_random_s030: 训练失败 — unknown\\n- v6_random_s030_r2: 训练失败 — unknown\\n- bf16_random_s015: 已被终止 — unknown\\n- bf16_random_s020: 已被终止 — unknown\\n- bf16_random_s025: 已被终止 — unknown\\n- bf16_random_s030: 已被终止 — unknown\\n- bf16_qwen_importance_s015: 已被终止 — unknown\\n- bf16_qwen_importance_s020: 已被终止 — unknown\\n- bf16_qwen_importance_s025: 已被终止 — unknown\\n- bf16_qwen_importance_s030: 已被终止 — unknown\\n- bf16_ds_imp_s015: 已被终止 — unknown\\n- bf16_ds_imp_s020: 已被终止 — unknown\\n- bf16_ds_imp_s025: 已被终止 — unknown\\n- bf16_ds_imp_s030: 已被终止 — unknown\\n- c3_llama_arch: 已被终止 — unknown\\n- c2_ds_n500: 已被终止 — unknown\\n- c2_qw_n500: 训练失败 — unknown\\n- r9c2-spike: 已被终止 — unknown\\n- r9c2-spike-v2: 已被终止 — unknown\\n- r9c2-spike-v3: 已被终止 — unknown\\n- acc_ds_dense_8k: 已被终止 — unknown\\n- acc_ds_s015_8k: 已被终止 — unknown\\n- acc_ds_s020_8k: 已被终止 — unknown\\n- acc_ds_s025_8k: 已被终止 — unknown\\n- acc_ds_s030_8k: 已被终止 — unknown\\n- gsm8k_qw_rand_s025: 训练失败 — unknown\\n- gsm8k_qw_rand_s030: 训练失败 — unknown\\n- c8_llama_n250: 训练失败 — unknown\\n- c10-lang-s020-s025: 已被终止 — unknown\\n\", \"total_chars\": 2847, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bbf17125-e250-4065-8cc6-98c758d1f614",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "1d3ffa76-42c1-4f97-870c-74bb6749cd0e",
  "sourceToolAssistantUUID": "bbf17125-e250-4065-8cc6-98c758d1f614",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-16T08:14:58.098Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01RqQkF4dUbBjaZjMBVNWiCA`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d3ffa76-42c1-4f97-870c-74bb6749cd0e",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uzb9j1c5vdMj8vkJx8",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "13680fc0-8330-4abf-ab31-ddb292fda5ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QPZt8zMNXMR1XnoMTAdKpb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4418,
      "cache_read_input_tokens": 24622,
      "output_tokens": 100,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4418
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 100,
          "cache_read_input_tokens": 24622,
          "cache_creation_input_tokens": 4418,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4418,
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

_source line 14 · 2026-05-16T08:14:58.133Z_

<details><summary>↩ Tool result · `toolu_01RqQkF4dUbBjaZjMBVNWiCA`</summary>

```text
artifacts/_project/paper/main.tex
artifacts/_project/paper/discussion.tex
artifacts/_project/paper/related_work.tex
artifacts/_project/paper/analysis.tex
artifacts/_project/paper/appendix.tex
artifacts/_project/paper/background.tex
artifacts/_project/paper/methodology.tex
artifacts/_project/paper/appendix_robustness.tex
artifacts/_project/paper/appendix_moved.tex
artifacts/_project/paper/appendix_disc_analysis.tex
artifacts/_project/paper/conclusion.tex
artifacts/_project/paper/results.tex
artifacts/_project/paper/limitations.tex
artifacts/_project/paper/abstract.tex
artifacts/_project/paper/introduction.tex
artifacts/dream_reports/dream_20260516T073742/best/paper.tex
artifacts/dream_reports/dream_20260516T073742/median/paper.tex
artifacts/dream_reports/dream_20260516T073742/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "13680fc0-8330-4abf-ab31-ddb292fda5ed",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "6168bdfb-21af-4332-9606-92e3f2fea024",
  "sourceToolAssistantUUID": "13680fc0-8330-4abf-ab31-ddb292fda5ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-16T08:15:08.620Z_

<details open><summary>🔧 Tool call — Read · `toolu_019hwaxdsYBLHoqkoCpAGLMe`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/methodology.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6168bdfb-21af-4332-9606-92e3f2fea024",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uzwx8C34aBWgHkWvcY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a100c754-ea73-4ead-b88a-762e68515ebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uf3Zeu4tA7o7rDLhGGKJZ8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 29040,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 340,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 59,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-16T08:15:08.640Z_

<details><summary>↩ Tool result · `toolu_019hwaxdsYBLHoqkoCpAGLMe`</summary>

```text
1	\section{Experimental Setup}
2	\label{sec:experimental-setup}
3	
4	\paragraph{Models.}
5	We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): \textbf{DeepSeek-R1-Distill-Qwen-7B}~\cite{deepseek-r1-2025}, distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and \textbf{Qwen2.5-7B-Instruct}~\cite{qwen25-2024}, with standard instruction tuning, providing a cross-training-paradigm replication target. Both are loaded in \texttt{bfloat16} with eager attention.\footnote{An earlier \texttt{float16} configuration produced sporadic NaN values; \texttt{bfloat16} eliminated all occurrences.}
6	
7	\paragraph{Dataset.}
8	We evaluate all 500 problems from MATH-500~\cite{math500-neurips2021}. Each problem is decoded greedily (\texttt{max\_new\_tokens}$=$2048). Problems with degenerate phase assignments (null low or high phase) are excluded, yielding effective sample sizes of $n{=}496$ for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded). Qwen exhibits a higher mid-phase null rate (45.2\% vs.\ 10.2\% for DeepSeek) due to lower temporal autocorrelation in its attention sparsity patterns (lag-1 $r{=}0.718$ vs.\ $0.894$, $d{=}-1.68$); this does not affect the primary gradient metric $\Delta = \mathrm{II}_{\textit{low}} - \mathrm{II}_{\textit{high}}$, which requires only low and high phases. Sensitivity analysis across $\texttt{min\_phase\_length} \in \{5, 10, 20\}$ supports robustness (Appendix~\ref{app:mpl-sensitivity}).
9	
10	\paragraph{Sparsity configuration.}
11	We apply symmetric compound sparsity at $s \in \{0.15, 0.20, 0.25, 0.30\}$, computing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare \emph{importance-based} eviction (position-normalized cumulative attention score, Eq.~\ref{eq:kv-importance}; BOS always retained) and \emph{random} eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly.
12	
13	\paragraph{Phase segmentation and metrics.}
14	Each sequence is segmented into three phases using the quantile-based method (\S\ref{par:phase-segmentation}), with $\texttt{min\_phase\_length}{=}10$. We compute segment-level perplexity and II (Eq.~\ref{eq:ii}), reporting medians due to heavy right-skew (mean/median ratios up to 43:1). The amplification ratio $G$ (Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric}. Robustness to segmentation granularity (quartile, quintile; Appendix~\ref{app:seg-robust}) and minimum phase length ($5$, $10$, $20$ tokens; Appendix~\ref{app:mpl-sensitivity}) is verified.
15	
16	\paragraph{Statistical analysis.}
17	\label{par:stats}
18	All reported confidence intervals use nonparametric bootstrap ($B{=}10{,}000$, seed$=$42)~\cite{efron-1993}. Significance tests use Wilcoxon signed-rank (paired within-model) or Mann-Whitney $U$ (cross-training-paradigm), with Bonferroni correction at family-wise $k{=}4$ (per model$\times$strategy combination, 4 sparsity levels testing one dose-response hypothesis): each family tests a single directional question (``does $\Delta$ increase with $s$?'') under fixed model and strategy, making $k{=}4$ the natural grouping. Benjamini-Hochberg FDR correction across all 44 tests is reported as a robustness check in Appendix~\ref{app:bh-fdr}; all Bonferroni-significant results remain significant under BH-FDR. Dose-response monotonicity is supported by the Jonckheere-Terpstra test ($z{=}6.2$--$33.7$, all $p < 10^{-9}$), which uses per-problem values (${\sim}496$ per group) rather than aggregated medians.\footnote{Spearman rank correlation on the four aggregate medians ($\rho{=}1.0$, $n{=}4$; interpret with caution given the small number of levels) is consistent; we rely on the JT test as primary evidence.} Scaling from $n{=}50$ (profiling) to $n{=}500$ narrowed bootstrap CI widths by $2.5$--$5.9{\times}$ across all 16 conditions, showing precision gains. The paired median difference $\Delta$ is the primary metric; $G$ (amplification ratio, Eq.~\ref{eq:gradient}) is reported in Appendix~\ref{app:g-metric} as an auxiliary illustrative ratio.\footnote{Experiments on 4$\times$ professional GPUs with 48\,GB memory.}
19	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a100c754-ea73-4ead-b88a-762e68515ebe",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "262b6b9e-f20d-4c36-9781-f8d0103e39ee",
  "sourceToolAssistantUUID": "a100c754-ea73-4ead-b88a-762e68515ebe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-16T08:15:08.937Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QajWmAEghauWEa3u5XZQug`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/results.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "262b6b9e-f20d-4c36-9781-f8d0103e39ee",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5uzwx8C34aBWgHkWvcY",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3dc2b179-9cb4-4e3c-933e-8c5cdfc27324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Uf3Zeu4tA7o7rDLhGGKJZ8",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 340,
      "cache_read_input_tokens": 29040,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 340
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 29040,
          "cache_creation_input_tokens": 340,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 340,
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

_source line 18 · 2026-05-16T08:15:08.945Z_

<details><summary>↩ Tool result · `toolu_01QajWmAEghauWEa3u5XZQug`</summary>

```text
1	
2	\section{Results}
3	\label{sec:results}
4	
5	\subsection{Strategy-Dependent Severity}
6	\label{sec:strategy-severity}
7	
8	Table~\ref{tab:aggregate-ii} reports the median compound severity difference across strategies and sparsity levels. Under importance-based eviction, $\Delta$ increases from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$---a $22{\times}$ amplification (all Bonferroni-corrected $p \ll 10^{-10}$). Random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: at $s \leq 0.20$, $\Delta$ is non-significant ($0.01$--$0.03$; CIs span zero); at $s \geq 0.25$, $\Delta$ becomes significant ($0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$) but $15$--$17{\times}$ smaller than under importance-based eviction. Both strategies exhibit monotonic dose-response (Jonckheere-Terpstra $z{=}6.2$--$33.7$, all $p < 10^{-9}$), but importance masking effect sizes are an order of magnitude larger.
9	
10	\begin{table}[t]
11	\centering
12	\small
13	\caption{Median of per-problem paired severity differences ($\Delta$) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, MATH-500).}
14	\label{tab:aggregate-ii}
15	\begin{tabular}{@{}lcccc@{}}
16	\toprule
17	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
18	\midrule
19	Importance & 0.39 & 1.21 & 3.99 & 8.48 \\
20	Random     & 0.01 & 0.03 & 0.26 & 0.51 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	
26	\subsection{Phase-Modulated Amplification}
27	\label{sec:phase-amplification}
28	
29	Decomposing II by reasoning phase reveals that strategy-dependent severity is driven by amplification in the low-sparsity phase. Table~\ref{tab:main-results} reports the per-phase breakdown. Under importance-based eviction, the median II in the low-sparsity phase rises from $0.357$ ($s{=}0.15$) to $8.456$ ($s{=}0.30$), while the high-sparsity phase remains near zero ($0.003$--$0.038$), yielding paired median differences $\Delta$ from $0.39$ to $8.48$ (all $p \ll 10^{-10}$). Random eviction shows a detectable but much weaker phase gradient at $s \geq 0.25$ ($\Delta{=}0.26$--$0.51$; $p_{\text{Bonf}} < 0.006$), $15$--$17{\times}$ smaller than importance-based at matched sparsity. Figure~\ref{fig:hero} visualizes the dose-response relationship for both models. The per-problem amplification ratio $G$ (Eq.~\ref{eq:gradient}) provides an auxiliary illustrative perspective and is reported in Appendix~\ref{app:g-metric}.
30	Under the multiplicative null ($r_b = r_a \cdot r_k$; Appendix~\ref{app:multiplicative-null}), the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$); we report additive-null values throughout as the more conservative estimates.
31	
32	\begin{table*}[t]
33	\centering
34	\small
35	\caption{Per-phase interaction index (II) at $n{=}496$/$475$. $\Delta{=}\widetilde{\mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}}$: median of per-problem paired differences (not the difference of column medians) with bootstrap 95\% CI ($B{=}10{,}000$). $G$ values reported in Appendix~\ref{app:g-metric}. Profiling-subset values ($n{=}50$) in Table~\ref{tab:profiling-subset}.}
36	\label{tab:main-results}
37	\begin{tabular}{@{}llcccc@{}}
38	\toprule
39	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
40	\midrule
41	\multicolumn{6}{@{}l}{\textit{DeepSeek-R1-Distill-Qwen-7B ($n{=}496$)}} \\
42	0.15 & Importance & 0.003 & 0.357 & 0.39\; $[0.35,\; 0.44]$ & $< 10^{-10}$ \\
43	0.15 & Random     & 0.083 & 0.090 & 0.01\; $[-0.02,\; 0.04]$ & ns \\
44	\addlinespace
45	0.20 & Importance & 0.008 & 1.211 & 1.21\; $[1.11,\; 1.34]$ & $< 10^{-10}$ \\
46	0.20 & Random     & 0.270 & 0.357 & 0.03\; $[-0.01,\; 0.08]$ & ns \\
47	\addlinespace
48	0.25 & Importance & 0.021 & 3.971 & 3.99\; $[3.53,\; 4.36]$ & $< 10^{-10}$ \\
49	0.25 & Random     & 1.113 & 1.514 & 0.26\; $[0.13,\; 0.35]$ & $< 0.006$ \\
50	\addlinespace
51	0.30 & Importance & 0.038 & 8.456 & 8.48\; $[7.75,\; 9.69]$ & $< 10^{-10}$ \\
52	0.30 & Random     & 3.112 & 3.848 & 0.51\; $[0.26,\; 0.89]$ & $< 0.006$ \\
53	\midrule
54	\multicolumn{6}{@{}l}{\textit{Qwen2.5-7B-Instruct ($n{=}475$)}} \\
55	0.15 & Importance & $-$0.000$^{\ddagger}$ & 0.044 & 0.07\; $[0.05,\; 0.09]$ & $< 10^{-14}$ \\
56	0.15 & Random     & 0.094 & 0.097 & $-$0.01\; $[-0.04,\; 0.01]$ & ns \\
57	\addlinespace
58	0.20 & Importance & 0.000 & 0.275 & 0.31\; $[0.26,\; 0.36]$ & $< 10^{-14}$ \\
59	0.20 & Random     & 0.291 & 0.356 & 0.02\; $[-0.01,\; 0.07]$ & ns \\
60	\addlinespace
61	0.25 & Importance & 0.004 & 1.053 & 1.07\; $[0.98,\; 1.18]$ & $< 10^{-14}$ \\
62	0.25 & Random     & 1.108 & 1.769 & 0.39\; $[0.24,\; 0.55]$ & $< 10^{-10}$ \\
63	\addlinespace
64	0.30 & Importance & 0.014 & 3.208 & 3.16\; $[2.78,\; 3.56]$ & $< 10^{-14}$ \\
65	0.30 & Random     & 2.819 & 4.253 & 0.91\; $[0.61,\; 1.26]$ & $< 10^{-13}$ \\
66	\bottomrule
67	\multicolumn{6}{@{}p{0.92\textwidth}}{\footnotesize $^{\ddagger}$ Negative II at this sparsity reflects \texttt{bfloat16} numerical noise when the interaction effect approaches zero ($|\mathrm{II}| < 10^{-4}$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ supports $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$.}
68	\end{tabular}
69	\end{table*}
70	
71	\begin{figure*}[t]
72	\centering
73	\includegraphics[width=\textwidth]{fig1_ii_scatter.pdf}
74	\caption{Paired median difference $\Delta$ (primary metric) as a function of sparsity level $s$ for DeepSeek-R1-Distill-Qwen-7B ($n{=}496$, left) and Qwen2.5-7B-Instruct ($n{=}475$, right). Importance-based eviction (red) exhibits monotonically increasing $\Delta$ ($0.39$--$8.48$ for DeepSeek, $0.07$--$3.16$ for Qwen); random eviction (blue) remains near zero at low sparsity (ns) and shows weak effects at $s \geq 0.25$. Error bars show asymmetric bootstrap 95\% CIs. DeepSeek importance effects are ${\sim}2.7{\times}$ larger than Qwen, consistent with the training-paradigm contrast (\S\ref{sec:cross-model}). Significance: {*}{*}{*}\,$p_{\text{Bonf}} < 0.001$; {*}{*}\,$p_{\text{Bonf}} < 0.01$; ns\,$p_{\text{Bonf}} > 0.05$.}
75	\label{fig:hero}
76	\end{figure*}
77	
78	
79	\subsection{Phase-Strategy Crossover}
80	\label{sec:crossover}
81	
82	The phase-strategy crossover is model-dependent. For DeepSeek ($n{=}496$), a strategy ranking reversal emerges at all four sparsity levels: at $s{=}0.25$, importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$), with reversal magnitude ranging from $2.2{\times}$ to $4.0{\times}$ across $s \in \{0.15, 0.20, 0.25, 0.30\}$. Qwen does \emph{not} exhibit this crossover: importance-based eviction produces lower II than random in both phases (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$). This divergence suggests the crossover arises from model-specific attention head specialization patterns rather than a universal compound-sparsity property. Full crossover analysis appears in Appendix~\ref{app:crossover-details}.
83	
84	\subsection{Replication Across Training Paradigms}
85	\label{sec:cross-model}
86	
87	DeepSeek-R1-Distill-Qwen-7B (distillation-trained) and Qwen2.5-7B-Instruct (instruction-tuned) share the Qwen2 backbone but differ in training objective, providing a within-architecture-family comparison across training paradigms.
88	Qwen2.5-7B-Instruct ($n_{\text{eff}}{=}475$) reproduces the monotonic severity gradient: $\Delta$ increases from $0.07$ at $s{=}0.15$ to $3.16$ at $s{=}0.30$ (all Bonferroni-corrected $p < 10^{-14}$), paralleling DeepSeek at approximately one-quarter to one-sixth the magnitude. Both models yield strictly increasing median $\Delta$ trajectories (Jonckheere-Terpstra $z \geq 6.2$, $p < 10^{-9}$; see \S\ref{par:stats}). Random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$, becoming significant at $s \geq 0.25$ ($\Delta{=}0.39$--$0.91$; $p_{\text{Bonf}} < 10^{-10}$) but $2.7$--$20{\times}$ weaker than importance-based. A caveat: 45.2\% of Qwen problems yield null mid-phase segments due to low temporal autocorrelation ($r{=}0.718$ vs.\ $0.894$); this does not affect $\Delta$ (Appendix~\ref{app:qwen-null-rate}). Full tables in Appendix~\ref{app:cross-model-details}.
89	
90	\subsection{Preliminary Cross-Architecture Analysis}
91	\label{sec:cross-arch}
92	
93	Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}49$)\footnote{The $n{=}49$ sample is an initial profiling subset. Full-scale ($n{=}500$) LlamaForCausalLM replication is planned as future work; the current analysis prioritizes within-architecture replication (Qwen2) over cross-architecture breadth.} provides preliminary support for the phase-gated severity pattern under importance-based eviction (post-hoc power $> 0.99$ for within-importance gradient) but is inconclusive for strategy comparisons (power $0.26$--$0.63$); the interaction magnitude is ${\sim}40{\times}$ smaller than DeepSeek, suggesting that quantitative characteristics may be Qwen2-family-specific and that broader architectural diversity (e.g., Mistral, Gemma) is needed for generalization claims. Full results, including per-sparsity breakdowns and a power analysis motivating the sample size needed for definitive cross-architecture claims, appear in Appendix~\ref{app:cross-arch}.
94	
95	\subsection{Scale Analysis: Qwen2.5-14B}
96	\label{sec:scale-14b}
97	
98	To assess whether phase-modulated severity persists at larger model scale within the same architecture family, we evaluate Qwen2.5-14B-Instruct on MATH-500 ($n{=}500$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$.
99	
100	\begin{table}[t]
101	\centering
102	\small
103	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on Qwen2.5-14B-Instruct (MATH-500). \textit{Results pending.}}
104	\label{tab:scale-14b}
105	\begin{tabular}{@{}lcccc@{}}
106	\toprule
107	Strategy & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
108	\midrule
109	Importance & --- & --- & --- & --- \\
110	Random     & --- & --- & --- & --- \\
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	%% PLACEHOLDER: Fill Table~\ref{tab:scale-14b} when c12 experiment completes.
116	%% Expected analysis: (1) whether 14B amplifies or attenuates severity relative to 7B,
117	%% (2) whether strategy specificity ratio is scale-invariant,
118	%% (3) comparison of phase segmentation thresholds at larger scale.
119	
120	\subsection{Cross-Benchmark Validation: GSM8K}
121	\label{sec:cross-benchmark}
122	
123	To assess task generalization, we evaluate both models on GSM8K ($n{=}50$) at $s \in \{0.15, 0.20, 0.25, 0.30\}$. On DeepSeek (clean data, no output truncation), importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels with a strict dose-response: $\Delta{=}0.24$ at $s{=}0.15$ rising to $4.68$ at $s{=}0.30$ (all $p \leq 0.0003$, Wilcoxon). Strategy specificity on GSM8K manifests as a \emph{qualitative} gap: importance-based eviction produces significant phase gradients while random eviction is non-significant across all conditions (CIs spanning zero). We attribute this to \emph{task complexity}: GSM8K's simpler arithmetic is associated with more uniform attention distributions, yielding a flatter sparsity landscape; within MATH-500, longer traces exhibit higher strategy specificity (Spearman $\rho > 0$, $p < 0.02$), supporting cognitive load as the modulating variable. Qwen GSM8K results are inconclusive due to generation truncation (\texttt{max\_new\_tokens}${=}$2047): while directional consistency holds at $s \geq 0.25$ ($\Delta{=}1.14$--$4.62$; $p < 10^{-4}$), absolute values and phase assignments are unreliable because all outputs hit the token limit. Full tables in Appendix~\ref{app:gsm8k}.
124	
125	\paragraph{GSM8K accuracy under compound sparsity.}
126	A power analysis on GSM8K ($n{=}50$) reveals a strategy-dependent asymmetry in downstream accuracy. Under random head removal, all 8 conditions (2 models $\times$ 4 sparsity levels) are non-significant (max $|d|{=}0.164$). Post-hoc power analysis indicates $n{=}50$ can detect effects of $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$); all random conditions showed $|d| \leq 0.164$, meaning the null results may reflect insufficient power rather than true absence of effect. Under importance-based pruning, Qwen exhibits a medium-sized accuracy degradation at $s \geq 0.25$ ($d \approx 0.63$, power ${>}\,0.99$), consistent with the PPL-based severity gradient observed on MATH-500. DeepSeek importance conditions exhibit a qualitative downward trend in accuracy but are excluded from parametric inference due to heavy-tailed distributions that violate test assumptions.
127	
128	\subsection{Cross-Benchmark Validation: GPQA Diamond}
129	\label{sec:cross-benchmark-gpqa}
130	
131	To assess generalization beyond mathematical reasoning, we evaluate both models on GPQA Diamond~\cite{rein-gpqa-2024} ($n{=}198$), a graduate-level science QA benchmark requiring multi-step reasoning across physics, chemistry, and biology.
132	
133	\begin{table}[t]
134	\centering
135	\small
136	\caption{Median of per-problem paired severity differences ($\Delta$) under importance-based eviction on GPQA Diamond. \textit{Results pending.}}
137	\label{tab:gpqa-results}
138	\begin{tabular}{@{}lcccc@{}}
139	\toprule
140	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
141	\midrule
142	DeepSeek-R1-Distill-Qwen-7B & --- & --- & --- & --- \\
143	Qwen2.5-7B-Instruct         & --- & --- & --- & --- \\
144	\bottomrule
145	\end{tabular}
146	\end{table}
147	
148	%% PLACEHOLDER: Fill Table~\ref{tab:gpqa-results} when c11 experiment completes.
149	%% Expected analysis: (1) phase gradient direction consistency with MATH-500/GSM8K,
150	%% (2) strategy specificity comparison across task types (math vs. science reasoning),
151	%% (3) whether cognitive load modulation hypothesis extends to non-mathematical domains.
152	
153	\subsection{Statistical Validation}
154	\label{sec:stat-validation}
155	
156	Table~\ref{tab:cohens-d} reports the paired median difference $\Delta$ under importance-based eviction for both models at $n{=}496$/$475$. All eight conditions yield CIs excluding zero; within-importance dose-response $d_z$ (s015 vs.\ s030) is $0.94$ (DeepSeek) and $0.92$ (Qwen), both large effects. Importance-based eviction produces significantly larger phase gradients than random at all four sparsity levels ($p_{\text{Bonf}} \ll 10^{-10}$, Wilcoxon; permutation tests in Appendix~\ref{app:permutation-details}).
157	
158	\begin{table}[t]
159	\centering
160	\small
161	\caption{Median of paired differences ($\Delta_i = \mathrm{II}^{(i)}_{\textit{low}} - \mathrm{II}^{(i)}_{\textit{high}}$) under importance-based eviction with bootstrap 95\% CIs ($B{=}10{,}000$).}
162	\label{tab:cohens-d}
163	\begin{tabular}{@{}lcc@{}}
164	\toprule
165	$s$ & DS ($n{=}496$): $\widetilde{\Delta}$\; [95\% CI] & QW ($n{=}475$): $\widetilde{\Delta}$\; [95\% CI] \\
166	\midrule
167	0.15 & $0.39$\; $[0.35,\; 0.44]$ & $0.07$\; $[0.05,\; 0.09]$ \\
168	0.20 & $1.21$\; $[1.11,\; 1.34]$ & $0.31$\; $[0.26,\; 0.36]$ \\
169	0.25 & $3.99$\; $[3.53,\; 4.36]$ & $1.07$\; $[0.98,\; 1.18]$ \\
170	0.30 & $8.48$\; $[7.75,\; 9.69]$ & $3.16$\; $[2.78,\; 3.56]$ \\
171	\bottomrule
172	\multicolumn{3}{@{}l}{\footnotesize All $p_{\text{Bonf}} < 10^{-13}$. Within-importance $d_z$ (s015 vs.\ s030): DS $0.94$, QW $0.92$.}
173	\end{tabular}
174	\end{table}
175	
176	\subsection{Answer-Region Analysis}
177	\label{sec:answer-region}
178	
179	Across both models, 93.2\% of answer tokens (\verb|\boxed{}| markers) fall within the high-sparsity phase, where compound interaction is minimal. This non-uniformity identifies \emph{where} severity concentrates: reasoning-trace tokens show $5.7$--$43.5{\times}$ PPL degradation vs.\ $1.3$--$5.3{\times}$ for answer tokens (Wilcoxon $p < 0.001$). However, reasoning-trace degradation may produce \emph{silent reasoning errors}---correct formatting with corrupted intermediate logic \cite{lanham-2023-faithfulness, turpin-2023-biased-cot}---a failure mode that PPL detects but answer-level accuracy may miss.
180	
181	\subsection{Downstream Accuracy Validation}
182	\label{sec:accuracy-validation}
183	
184	To validate that the PPL-based severity gradient translates to downstream task performance, we evaluate MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192; Table~\ref{tab:accuracy}). Qwen's minimal truncation ($\leq 4\%$) provides a clean PPL-accuracy bridge.
185	Qwen ($n{=}100$; truncation $\leq 4\%$) shows gradual decline from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) with a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) degrades more steeply ($74\% \to 4\%$) with a dual-regime structure: at $s \leq 0.20$, degradation is primarily truncation-driven (non-truncated accuracy remains $68$--$71\%$ at $s{=}0.15$--$0.20$ vs.\ $88\%$ dense); at $s \geq 0.25$, both truncation and reasoning quality collapse simultaneously (Appendix~\ref{app:accuracy-details}).
186	The two models exhibit distinct failure modes reflecting training-paradigm dependence: DeepSeek failures are \emph{truncation-dominated} (truncation $16\% \to 76\%$), while Qwen failures are \emph{wrong-answer-dominated} (truncation $\leq 4\%$, reasoning quality degrades directly). Given minimal truncation, Qwen accuracy data provide a reliable PPL-accuracy bridge; DeepSeek accuracy results, confounded by truncation rates of $16\%$--$76\%$, should be interpreted as qualitative observations only.
187	
188	We provide a correlational mechanistic analysis in terms of importance discrimination collapse in \S\ref{sec:analysis}.
189	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3dc2b179-9cb4-4e3c-933e-8c5cdfc27324",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "ada4d94b-a7aa-4826-b396-dab27211af69",
  "sourceToolAssistantUUID": "3dc2b179-9cb4-4e3c-933e-8c5cdfc27324",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-16T08:15:14.179Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ZoYaYCJBMqWrQKPWkqz1L`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ada4d94b-a7aa-4826-b396-dab27211af69",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v1kN8pE2ametgb4jh7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4fde4070-e25e-4eae-a230-8e3d24cec899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrLdRdzqaLNgkPYqq3kUah",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8695,
      "cache_read_input_tokens": 29380,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8695,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 34,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-16T08:15:14.192Z_

<details><summary>↩ Tool result · `toolu_014ZoYaYCJBMqWrQKPWkqz1L`</summary>

```text
1	\section{Importance Discrimination Collapse under Compound Sparsity}
2	\label{sec:analysis}
3	
4	The mechanisms discussed here are \emph{correlational diagnostics} that illuminate but do not fully explain the $15$--$17{\times}$ severity divergence between strategies. Both strategies exhibit near-identical Gini drops ($<10\%$ difference), yet severity diverges by $15$--$17{\times}$---an order-of-magnitude mismatch indicating that aggregate concentration collapse alone is insufficient. The critical differentiator is \emph{structural specificity} of importance-based pruning, which systematically removes high-attention-score heads (\S\ref{sec:discrimination-collapse-main}).
5	
6	\subsection{Importance Discrimination Collapse}
7	\label{sec:discrimination-collapse-main}
8	
9	Head pruning systematically reduces the discriminative power of cumulative importance scores, suggesting a mechanism for the phase-strategy interaction. The Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek, $6$--$17\%$ relative to dense baseline) and $0.010$--$0.020$ (Qwen, $2$--$4\%$) after pruning, with consistent negative deltas in all 16 conditions (Appendix~\ref{app:analysis}, Table~\ref{tab:discrimination-metrics-full}). Random eviction shows near-identical Gini drops (e.g., DeepSeek $s{=}0.25$: $-0.065$ vs.\ $-0.060$), indicating that collapse is a consequence of head pruning \emph{per se}. Yet importance-based severity is $15$--$17{\times}$ larger---the amplification arises because importance-based eviction \emph{depends on} the very scores that pruning degrades.
10	
11	This pattern---\emph{importance discrimination collapse}---reflects eviction degenerating into noise-sensitive selection as score distributions approach uniformity. The effect is phase-dependent: per-phase Gini analysis on Qwen shows that the low-sparsity phase exhibits the largest Gini delta at every sparsity level, with monotonically increasing magnitude ($-0.017$ at $s{=}0.15$, $-0.020$ at $s{=}0.20$, $-0.029$ at $s{=}0.25$, $-0.035$ at $s{=}0.30$). Low-sparsity phases have broadly distributed attention where collapse has maximum impact; high-sparsity phases preserve concentration. \cite{hies-2025} report this collapse under single-axis pruning; we extend it to the compound setting.
12	
13	To provide quantitative evidence for structural specificity, we analyzed the attention Gini coefficients of importance-pruned versus retained heads. Importance pruning (Frobenius norm criterion) systematically removes heads with lower Gini coefficients---i.e., heads with more dispersed attention patterns (Mann-Whitney $U$, $p < 10^{-28}$; rank-biserial $r = 0.62$--$0.76$ across all 8 conditions). Random pruning, by contrast, samples heads with Gini indistinguishable from the population mean (200-trial verification). The Frobenius norm and Gini share sensitivity to attention magnitude; the large effect size ($r > 0.6$) nonetheless indicates strong structural separation.
14	
15	We note that this evidence is correlational; causal validation through controlled manipulation of importance-score entropy is an important direction for future work.
16	%% TODO: Add per-phase Gini results when available from Agent computation.
17	
18	\subsection{Entropy Redistribution: A Model-Dependent Secondary Effect}
19	\label{sec:entropy-redistribution-main}
20	
21	As a supplementary observation, head pruning also redistributes the attention entropy of surviving heads on DeepSeek ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Appendix~\ref{app:analysis}, Table~\ref{tab:entropy-deltas}). However, entropy redistribution shows model-dependent behavior---the direction reverses on Qwen at $s{=}0.25$ ($\Delta\mathcal{H} = +0.045$)---replicating in only 2/4 Qwen conditions and thus only partially consistent. Importance discrimination collapse remains the more robust, model-independent correlate, though it partially accounts for rather than fully explains the severity divergence.
22	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fde4070-e25e-4eae-a230-8e3d24cec899",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "f0ebd8c7-a26a-4235-9991-72d8aab418e5",
  "sourceToolAssistantUUID": "4fde4070-e25e-4eae-a230-8e3d24cec899",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-16T08:15:14.300Z_

<details open><summary>🔧 Tool call — Read · `toolu_01HbTo46XHdkjkd2bhsiU2F5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/background.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f0ebd8c7-a26a-4235-9991-72d8aab418e5",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v1kN8pE2ametgb4jh7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bd376728-3a65-4669-9410-086f32755c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01UrLdRdzqaLNgkPYqq3kUah",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8695,
      "cache_read_input_tokens": 29380,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8695
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 29380,
          "cache_creation_input_tokens": 8695,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8695,
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

_source line 22 · 2026-05-16T08:15:14.306Z_

<details><summary>↩ Tool result · `toolu_01HbTo46XHdkjkd2bhsiU2F5`</summary>

```text
1	% Section 3: Background and Problem Setup
2	% Note: eq:ii and eq:gradient are the canonical definitions.
3	% Full formulation details in Appendix (app:formulation-details).
4	
5	\section{Background and Problem Setup}
6	\label{sec:background}
7	
8	We formalize compound sparsity, define the Interaction Index, and introduce phase segmentation. Full mathematical details appear in Appendix~\ref{app:formulation-details}.
9	
10	\paragraph{Compound sparsity.}
11	Let $s \in (0,1)$ denote a unified sparsity budget. \emph{Attention head pruning} removes the bottom-$s$ fraction of heads per layer by Frobenius norm importance \cite{voita-acl2019, michel-neurips2019}. \emph{KV cache eviction} removes the bottom-$s$ fraction of token positions from the cache. We compare two strategies: \emph{importance-based}, which scores positions by position-normalized cumulative attention mass (Eq.~\ref{eq:kv-importance} in Appendix~\ref{app:formulation-details}), and \emph{random}, which evicts uniformly at random \cite{nacl-acl2024}. Applying both simultaneously yields \emph{compound sparsity}; the two axes interact because head pruning alters the importance ranking used for eviction \cite{spark-aaai2026}. Existing joint-pruning approaches such as GRASPrune \cite{graspune-acl2026} learn global budget-constrained gates but treat decisions as static across generation.
12	
13	\paragraph{Interaction Index.}
14	For a text segment, let $\text{PPL}_c$ denote perplexity under condition $c \in \{d, a, k, b\}$ (dense, attention-only, KV-only, compound). Normalizing by the dense baseline yields $r_c = \text{PPL}_c / \text{PPL}_d$, and:
15	\begin{equation}
16	    \mathrm{II} = r_b - r_a - r_k + 1.
17	    \label{eq:ii}
18	\end{equation}
19	$\mathrm{II} > 0$ indicates super-additive degradation; $\mathrm{II} = 0$ indicates additive independence. We adopt the additive null as primary: it assumes $r_b = r_a + r_k - 1$ (compound loss equals sum of individual losses), the most conservative independence assumption. Although the two axes are mechanistically linked (\S\ref{sec:analysis}), rejection ($\mathrm{II} > 0$) establishes super-additivity regardless of null specification. Appendix~\ref{app:multiplicative-null} reports parallel results under the multiplicative null ($r_b = r_a \cdot r_k$); the phase-severity gradient is preserved ($G_{\times}{=}21$--$64{\times}$), supporting null-choice invariance. The II distribution is heavily right-skewed; we report medians throughout.
20	
21	\paragraph{Severity gradient.}
22	To capture phase variation, the per-problem \emph{amplification ratio} is:
23	\begin{equation}
24	    G^{(i)} = \frac{\mathrm{II}^{(i)}_{\,\textit{low}}}{\mathrm{II}^{(i)}_{\,\textit{high}}},
25	    \label{eq:gradient}
26	\end{equation}
27	where $\mathrm{II}^{(i)}_{\,\textit{low/high}}$ is the interaction index in the low/high-sparsity phase for problem $i$. We report $G = \widetilde{G^{(i)}}$, the median across problems, with bootstrap CIs. We use the median of per-problem ratios (not the ratio of medians) to preserve per-problem pairing; see Appendix~\ref{app:profiling-subset} for comparison. $G$ serves as an auxiliary descriptive ratio that illustrates the degree of phase concentration; the primary statistical evidence for the severity gradient rests on $\Delta$ and paired Wilcoxon tests (\S\ref{sec:phase-amplification}).
28	
29	\paragraph{Phase segmentation.}
30	\label{par:phase-segmentation}
31	Inspired by ThinKV's phase-aware perspective on reasoning-time compression~\cite{thinkv-iclr2026}, each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, using a quantile-based segmentation rather than explicit reasoning delimiters (e.g., \texttt{&lt;think>} tokens). Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation). We note that this segmentation is an \emph{operationalization choice}: attention sparsity serves as a continuous proxy for reasoning phase rather than a theoretically grounded boundary. We validate robustness to segmentation granularity (tercile/quartile/quintile; Appendix~\ref{app:seg-robust}) and minimum phase length (Appendix~\ref{app:mpl-sensitivity}). Validation against DeepSeek's explicit \texttt{&lt;think>} markers using adaptive per-sequence quantile segmentation yields substantial agreement ($\kappa{=}0.88$, AUC-ROC${=}0.98$; $n{=}48$; Appendix~\ref{app:think-validation}). Details in Appendix~\ref{app:formulation-details}.
32	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bd376728-3a65-4669-9410-086f32755c44",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "3a42bb16-b625-4e3f-8026-048e74229a8f",
  "sourceToolAssistantUUID": "bd376728-3a65-4669-9410-086f32755c44",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-16T08:15:18.111Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QTi9Gjo4eWABJ3bWr6MVko`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3a42bb16-b625-4e3f-8026-048e74229a8f",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v29UC2zSi8vcga9XpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2e175288-de71-49d0-b476-17b9de0af9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V71v2BJ7Yjenb9wAjbqQkK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2833,
      "cache_read_input_tokens": 38075,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2833,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-16T08:15:18.125Z_

<details><summary>↩ Tool result · `toolu_01QTi9Gjo4eWABJ3bWr6MVko`</summary>

```text
1	\begin{abstract}
2	Compound sparsity---simultaneously pruning attention heads and evicting KV cache entries---is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood.
3	We find that compound sparsity severity is not a fixed constant but an emergent property of the interaction among eviction strategy, reasoning phase, and sparsity level.
4	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), importance-based eviction exhibits a monotonically increasing phase--severity gradient: the paired median difference $\Delta$ rises from $0.39$ at sparsity $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
5	Random eviction develops a detectable gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude.
6	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$), shows consistent phase gradient direction on GSM8K for both models, and exhibits compatible direction on LlamaForCausalLM ($n{=}49$; strategy${\times}$phase interaction weaker than on Qwen2-architecture models).
7	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this severity divergence.
8	These findings challenge the assumption of uniform compound interaction and establish phase-gated analysis---decomposing compound severity by reasoning phase and eviction strategy---as a principled framework for diagnosing where and why compound sparsity fails, with direct implications for phase-aware budget allocation in inference systems.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2e175288-de71-49d0-b476-17b9de0af9db",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "78463a66-9c99-4d07-b30d-a1f9f582e1cd",
  "sourceToolAssistantUUID": "2e175288-de71-49d0-b476-17b9de0af9db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-16T08:15:18.404Z_

<details open><summary>🔧 Tool call — Read · `toolu_01PL85LVnNiuSf3S6koqvdT5`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "78463a66-9c99-4d07-b30d-a1f9f582e1cd",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v29UC2zSi8vcga9XpL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a7ec050d-6ea6-4092-8ee1-ed9f7716073d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01V71v2BJ7Yjenb9wAjbqQkK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2833,
      "cache_read_input_tokens": 38075,
      "output_tokens": 167,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2833
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 167,
          "cache_read_input_tokens": 38075,
          "cache_creation_input_tokens": 2833,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2833,
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

_source line 26 · 2026-05-16T08:15:18.409Z_

<details><summary>↩ Tool result · `toolu_01PL85LVnNiuSf3S6koqvdT5`</summary>

```text
1	\section{Discussion}
2	\label{sec:discussion}
3	
4	\paragraph{Implications for deployment.}
5	A uniform compression budget implicitly accepts order-of-magnitude severity penalties during low-sparsity reasoning phases. Pilot evaluation ($n{=}30$, $s{=}0.25$; Appendix~\ref{app:pilot-mitigation}) achieved 18\% oracle recovery (95\% CI: $[-39\%, 45.8\%]$), falling below the pre-registered 30\% gate; the CI spans zero, indicating no statistically distinguishable improvement. Effective phase-aware allocation likely requires finer phase boundary estimation than current proxies provide. Additional mechanisms (e.g., strategy switching, adaptive thresholding) warrant investigation. We hypothesize that phase-modulated severity may extend to alternative attention-mass-based scoring methods (H$_2$O \cite{h2o-neurips2023}, SnapKV \cite{snapkv-neurips2024}, PyramidKV \cite{pyramidkv-colm2025}), which remains an open question for future work. Extended discussion in Appendix~\ref{app:extended-discussion}.
6	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a7ec050d-6ea6-4092-8ee1-ed9f7716073d",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "6f414ef0-5b77-42a0-a91b-d8112241a1d2",
  "sourceToolAssistantUUID": "a7ec050d-6ea6-4092-8ee1-ed9f7716073d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-16T08:15:22.266Z_

<details open><summary>🔧 Tool call — Read · `toolu_01TNDsjXdzSPD2CG3Ba7vTh7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6f414ef0-5b77-42a0-a91b-d8112241a1d2",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v2SthAHL4qeoENBySZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c87addd2-ae99-4c9a-8881-126cf39adeab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158y6EMNnLepMmitQJ2g7Jf",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 40908,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 995,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 68,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-16T08:15:22.306Z_

<details><summary>↩ Tool result · `toolu_01TNDsjXdzSPD2CG3Ba7vTh7`</summary>

```text
1	\section{Compound Sparsity Formulation}
2	\label{app:formulation-details}
3	
4	\paragraph{Attention head pruning.}
5	Heads are ranked by Frobenius norm importance $w_j^{(\ell)} = \|\mathbf{A}_j^{(\ell)}\|_F$ \cite{voita-acl2019, michel-neurips2019}; a binary mask $m_j^{(\ell)} \in \{0,1\}$ retains the top-$(1{-}s)\cdot H$ heads:
6	\begin{equation}
7	    \tilde{\mathbf{o}}_j^{(\ell)} = m_j^{(\ell)} \cdot \mathbf{o}_j^{(\ell)}.
8	    \label{eq:head-mask}
9	\end{equation}
10	
11	\paragraph{KV cache eviction.}
12	A position mask $\mathbf{m}_k \in \{0,1\}^T$ retains the top-$(1{-}s)\cdot T$ positions (BOS always preserved):
13	\begin{equation}
14	    \tilde{a}_{ij} = a_{ij} \cdot m_{k,j}, \quad \forall\, i, j.
15	    \label{eq:kv-mask}
16	\end{equation}
17	Under importance-based eviction, each position $j$ is scored by its cumulative attention mass with position normalization:
18	\begin{equation}
19	    \mathrm{imp}(j) = \frac{\sum_{\ell, h, i} a_{ij}^{(\ell,h)}}{T - j},
20	    \label{eq:kv-importance}
21	\end{equation}
22	where the denominator compensates for causal bias---earlier positions are attended to by more queries \cite{thinkv-iclr2026, defensivekv-iclr2026}. Under random eviction, positions (excluding BOS) are evicted uniformly at random.
23	
24	\paragraph{Compound sparsity.}
25	Applying both mechanisms simultaneously yields compound sparsity. The two axes interact: head pruning redistributes attention mass, altering the importance ranking for KV eviction. Prior work \cite{spark-aaai2026} reports super-additive joint effects but treats interaction magnitude as a fixed property of $s$.
26	
27	\paragraph{Attention sparsity metric.}
28	For each query position $i$ and head $h$, we compute the fraction of key positions receiving negligible attention:
29	\begin{equation}
30	    \sigma_i^{(h)} = \frac{1}{T} \sum_{j=1}^{T} \mathbf{1}\!\left[a_{ij}^{(h)} < 0.01 \cdot \max_k a_{ik}^{(h)}\right].
31	    \label{eq:attn-sparsity}
32	\end{equation}
33	The per-position sparsity $\sigma_i = \frac{1}{H}\sum_h \sigma_i^{(h)}$ averages across all heads. Tokens are partitioned into high-, mid-, and low-sparsity phases by the tercile boundaries of $\{\sigma_i\}$; segments shorter than 10 tokens are merged into adjacent phases.
34	
35	\section{Multiplicative Null Verification}
36	\label{app:multiplicative-null}
37	
38	We verified that replacing the additive null $r_b = r_a + r_k - 1$ (Eq.~\ref{eq:ii}) with the multiplicative null $r_b = r_a \cdot r_k$ does not change qualitative conclusions. Under the multiplicative formulation, the interaction index becomes $\mathrm{II}_{\times} = r_b - r_a \cdot r_k$. Notably, $\mathrm{II}_{\times} < 0$ across all phases and sparsity levels: the compound interaction is \emph{sub-multiplicative} everywhere---actual compound degradation is less severe than the multiplicative prediction. $G_{\times}$ therefore quantifies the ratio of sub-multiplicative deviations between phases, not super-multiplicative amplification: a value of $G_{\times}{=}30$ means the low-sparsity phase deviates from the multiplicative null by $30{\times}$ more than the high-sparsity phase. Under importance-based eviction, $G_{\times}{=}21.1$--$36.2{\times}$ (DeepSeek) and $43.9$--$64.0{\times}$ (Qwen) across $s \in \{0.15, 0.20, 0.25, 0.30\}$, yielding a combined range of $21$--$64{\times}$. Although compound effects do not exceed the multiplicative prediction in any phase, the low-sparsity phase's deviation from the multiplicative null is $21$--$64{\times}$ larger than the high-sparsity phase's, indicating that the phase-gated severity gradient is preserved under the multiplicative null. These $n{=}500$ exact values are more conservative than the preliminary $n{=}50$ calibrated estimates ($\approx$51--183${\times}$), reflecting reduced variance at full sample size. Values are computed using aggregate per-phase PPL ratios; per-problem exact computation is left for future work. Random eviction remains flat ($G_{\times} \approx 1$). The crossover at $s{=}0.25$ is preserved. We adopt the additive formulation in the main text as the more conservative baseline: it assumes zero interaction (compound loss equals the sum of individual losses), so rejection ($\mathrm{II} > 0$) establishes super-additivity regardless of null specification. The qualitative conclusions---phase-modulated severity, strategy asymmetry, and crossover---are preserved under the multiplicative null.
39	
40	% Bootstrap and permutation details moved to main text \S\ref{sec:stat-validation}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c87addd2-ae99-4c9a-8881-126cf39adeab",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "a151bce5-da91-4a8a-a87f-600fb4e20ce6",
  "sourceToolAssistantUUID": "c87addd2-ae99-4c9a-8881-126cf39adeab",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-16T08:15:22.558Z_

<details open><summary>🔧 Tool call — Read · `toolu_019e66MYbkgCnBnnY3nhxSt3`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a151bce5-da91-4a8a-a87f-600fb4e20ce6",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v2SthAHL4qeoENBySZ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8d849f54-0c58-4799-b1df-bd300c3123bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0158y6EMNnLepMmitQJ2g7Jf",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 995,
      "cache_read_input_tokens": 40908,
      "output_tokens": 168,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 995
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 168,
          "cache_read_input_tokens": 40908,
          "cache_creation_input_tokens": 995,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 995,
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

_source line 30 · 2026-05-16T08:15:22.565Z_

<details><summary>↩ Tool result · `toolu_019e66MYbkgCnBnnY3nhxSt3`</summary>

```text
1	\paragraph{Model scale and architecture.}
2	Our primary experiments span 7--14B parameters: DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-7B-Instruct, and Qwen2.5-14B-Instruct (\S\ref{sec:scale-14b}). Whether the phase-modulated severity patterns persist, amplify, or attenuate at substantially larger scales (e.g., 70B) remains untested. Preliminary cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) provides pilot evidence suggesting the qualitative pattern may extend beyond the Qwen2 architecture---monotonically increasing $d_z$ with within-importance phase gradient $\sim$1.0---but with substantially weaker interaction magnitude ($\sim$1/40 of DeepSeek) and mixed statistical evidence (only $s{=}0.30$ significant after Bonferroni correction). The pattern has been tested on two architecture families (Qwen2ForCausalLM, LlamaForCausalLM) at two scale points (7B, 14B); comprehensive validation across more diverse architectures (e.g., Mistral, multi-latent attention) and larger scales is needed for full generalization claims.
3	
4	\paragraph{Task coverage.}
5	We evaluate on three benchmarks spanning mathematical and scientific reasoning: MATH-500 (primary), GSM8K (\S\ref{sec:cross-benchmark}), and GPQA Diamond (\S\ref{sec:cross-benchmark-gpqa}). Cross-benchmark validation on GSM8K supports the phase gradient direction under importance-based eviction but reveals that random eviction is non-significant (CIs spanning zero), precluding meaningful ratio computation. On MATH-500, strategy specificity is quantifiable ($15$--$17{\times}$); on GSM8K, it manifests as a qualitative gap (significant vs.\ non-significant). This suggests that the phase-strategy interaction is robust in direction but task-dependent in form---complex reasoning (MATH-500) produces quantitative strategy contrast while simpler arithmetic (GSM8K) produces qualitative separation. Qwen GSM8K outputs were truncated at \texttt{max\_new\_tokens}${=}$2047, so Qwen GSM8K absolute values carry this limitation; DeepSeek GSM8K data is untruncated. Our task-complexity explanation for specificity attenuation (lower cognitive load $\to$ more uniform attention $\to$ reduced strategy sensitivity) is supported by within-benchmark correlational evidence but requires validation across a broader range of task complexities; whether different reasoning tasks---code generation, multi-hop QA---produce yet different attenuation profiles remains open. Random eviction on GSM8K exhibits numerical instability (extreme outlier II values), likely a systematic interaction between reduced-precision arithmetic and score-independent eviction.
6	
7	\paragraph{Eviction strategy scope and H$_2$O confound.}
8	Our importance-based eviction uses cumulative attention scores (H$_2$O-style scoring~\cite{h2o-neurips2023}, Eq.~\ref{eq:kv-importance}), which creates an inherent confound: head pruning alters the attention distribution from which importance scores are computed, and eviction then operates on these degraded scores. The compound interaction patterns we report---including importance discrimination collapse and the phase-strategy crossover---may be partly attributable to this circular dependency rather than to compound sparsity \emph{per se}. Other attention-mass-based methods (SnapKV~\cite{snapkv-neurips2024}, PyramidKV~\cite{pyramidkv-colm2025}) share the same scoring basis and would likely exhibit a similar confound, whereas strategies that do not derive scores from the pruned attention distribution (e.g., learned eviction policies, recency-based heuristics) may exhibit qualitatively different compound interaction dynamics. Disentangling the contribution of score degradation from the intrinsic compound interaction requires testing eviction methods whose scoring is independent of head pruning; this is an important next step.
9	
10	\paragraph{Symmetric sparsity assumption.}
11	Our analysis applies symmetric sparsity levels: the same fraction $s$ is used for both head pruning and KV cache eviction. A preliminary spot check under asymmetric allocation (Appendix~\ref{app:asymmetric-robustness}) supports that the phase gradient is robust to head/KV budget ratios, but systematic characterization of the full asymmetric interaction surface remains future work.
12	
13	\paragraph{Phase segmentation validation.}
14	The \texttt{&lt;think>} token validation of sparsity-based phase segmentation (\S\ref{sec:background}, Appendix~\ref{app:think-validation}) is limited to a single model (DeepSeek-R1-Distill-Qwen-7B) on a single benchmark (GSM8K, $n{=}48$). Qwen2.5-7B-Instruct does not generate explicit reasoning markers, precluding the same validation. Whether the high agreement ($\kappa{=}0.88$) generalizes to other models with explicit CoT delimiters, or to non-mathematical reasoning tasks, remains open.
15	
16	\paragraph{Mechanism.}
17	The importance discrimination collapse mechanism is a correlational marker, not a complete causal explanation: both strategies exhibit near-identical Gini drops yet severity diverges by $15$--$17{\times}$, indicating that Gini collapse alone is insufficient. Causal validation through controlled entropy manipulation is needed. The entropy redistribution component replicates on only 2/4 Qwen conditions, suggesting model-specific factors.
18	
19	\paragraph{Perplexity vs.\ accuracy.}
20	Our primary severity metric is perplexity-based (II), chosen because its per-token granularity enables the phase-level decomposition central to our analysis; accuracy is binary per-problem and cannot be meaningfully decomposed by reasoning phase. Accuracy validation on MATH-500 (\S\ref{sec:accuracy-validation}, Appendix~\ref{app:accuracy-details}) shows gradual decline through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) followed by a sharp cliff at $s{=}0.30$ ($\delta{=}-27$\,pp) for Qwen ($n{=}100$, truncation $\leq 4\%$). DeepSeek accuracy deltas are confounded by rising truncation ($16\%$ to $76\%$); non-truncated analysis reveals a dual-regime structure but is limited by small surviving samples at high sparsity. Comprehensive accuracy evaluation across benchmarks remains an important next step.
21	
22	\paragraph{Sparsity range.}
23	Our experiments span $s \in \{0.15, 0.20, 0.25, 0.30\}$, sufficient to establish monotonicity at the tested levels (JT test $p \ll 10^{-10}$) but insufficient to characterize the functional form of the auxiliary ratio $G(s)$ or identify potential saturation thresholds. More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics. We do not report inference throughput or latency measurements, which are necessary for a complete deployment analysis but orthogonal to our severity characterization. Extended limitations in Appendix~\ref{app:limitations}.
24	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8d849f54-0c58-4799-b1df-bd300c3123bf",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "5bf82bcb-dcce-413a-8f3b-596e7e2c2091",
  "sourceToolAssistantUUID": "8d849f54-0c58-4799-b1df-bd300c3123bf",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 31 · 2026-05-16T08:15:25.673Z_

<details open><summary>🔧 Tool call — Read · `toolu_01STAJKMT2faFVruD1jWofEx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_robustness.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5bf82bcb-dcce-413a-8f3b-596e7e2c2091",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v2kaZj37XqsSt1eZPi",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "055846ea-5348-458a-aecb-f653f5e79cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AWoKXuYFtM62WKaHCRkvCS",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3578,
      "cache_read_input_tokens": 41903,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3578
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 41903,
          "cache_creation_input_tokens": 3578,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3578,
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

_source line 32 · 2026-05-16T08:15:25.680Z_

<details><summary>↩ Tool result · `toolu_01STAJKMT2faFVruD1jWofEx`</summary>

```text
1	\section{Benjamini-Hochberg FDR Correction}
2	\label{app:bh-fdr}
3	
4	Table~\ref{tab:bh-fdr} compares Bonferroni ($k{=}4$, per model$\times$strategy family) and Benjamini-Hochberg FDR correction across all 44 statistical tests. BH-FDR recovers 5 additional significant results beyond Bonferroni, all in low-effect-size conditions (random eviction or cross-training-paradigm random comparisons). All 32 Bonferroni-significant results remain significant under BH-FDR.
5	
6	\begin{table}[t]
7	\centering
8	\small
9	\caption{Bonferroni vs.\ BH-FDR correction summary ($\alpha{=}0.05$, 44 tests). ``BH only'' denotes tests significant under BH-FDR but not Bonferroni.}
10	\label{tab:bh-fdr}
11	\begin{tabular}{@{}lcc@{}}
12	\toprule
13	Category & Bonf.\ sig. & BH-only sig. \\
14	\midrule
15	Per-condition Wilcoxon ($k{=}16$) & 10 & 2 \\
16	Imp vs.\ rand ($k{=}8$) & 8 & 0 \\
17	Adjacent sparsity ($k{=}12$) & 10 & 1 \\
18	Cross-paradigm Mann-Whitney ($k{=}8$) & 4 & 2 \\
19	\midrule
20	Total ($k{=}44$) & 32 & 5 \\
21	\bottomrule
22	\end{tabular}
23	\end{table}
24	
25	The 5 BH-only results are: DeepSeek random $s{=}0.25$ and $s{=}0.30$ per-condition Wilcoxon ($p_{\text{Bonf}}{=}0.064$/$0.065$, BH $q{=}0.002$), DeepSeek random $s{=}0.25 \to 0.30$ adjacent-sparsity step ($p_{\text{Bonf}}{=}0.078$, BH $q{=}0.002$), and cross-training-paradigm random $s{=}0.25$/$s{=}0.30$ Mann-Whitney ($p_{\text{Bonf}}{=}0.66$/$0.17$, BH $q{=}0.018$/$0.005$). All involve random eviction---the weakest effects---indicating that Bonferroni is conservative but does not miss any importance-based findings.
26	
27	
28	\section{Minimum Phase Length Sensitivity}
29	\label{app:mpl-sensitivity}
30	
31	Table~\ref{tab:mpl-sensitivity} reports the paired median difference $\Delta$ under three \texttt{min\_phase\_length} (mpl) settings across all 16 conditions (2 models $\times$ 2 strategies $\times$ 4 sparsity levels). Conclusions are robust: all importance-based conditions remain significant at $p_{\text{Bonf}} < 10^{-10}$ across mpl $\in \{5, 10, 20\}$; random conditions maintain the same significance pattern (non-significant at $s \leq 0.20$, significant at $s \geq 0.25$). Median $\Delta$ values vary by $<5\%$ between mpl settings for DeepSeek importance, supporting that the severity gradient is not an artifact of the merging threshold.
32	
33	\begin{table*}[t]
34	\centering
35	\small
36	\caption{Sensitivity of median $\Delta$ to \texttt{min\_phase\_length} (mpl). $n_{\text{eff}}$: effective sample size after exclusions. All importance-based $p_{\text{Bonf}} < 10^{-10}$; ``ns'' denotes $p_{\text{Bonf}} > 0.05$.}
37	\label{tab:mpl-sensitivity}
38	\begin{tabular}{@{}llrrrrrr@{}}
39	\toprule
40	Model & Strategy & $s$ & \multicolumn{1}{c}{mpl$=$5} & \multicolumn{1}{c}{mpl$=$10} & \multicolumn{1}{c}{mpl$=$20} & $n_{\text{eff}}$(10) & $n_{\text{eff}}$(20) \\
41	\midrule
42	DS & Imp & 0.15 & 0.391 & 0.391 & 0.393 & 496 & 433 \\
43	DS & Imp & 0.20 & 1.215 & 1.215 & 1.235 & 496 & 433 \\
44	DS & Imp & 0.25 & 3.986 & 3.986 & 4.017 & 496 & 433 \\
45	DS & Imp & 0.30 & 8.481 & 8.481 & 8.420 & 496 & 433 \\
46	\addlinespace
47	DS & Rand & 0.15 & 0.014 & 0.014\textsuperscript{ns} & 0.012\textsuperscript{ns} & 496 & 433 \\
48	DS & Rand & 0.20 & 0.031\textsuperscript{ns} & 0.031\textsuperscript{ns} & 0.023\textsuperscript{ns} & 496 & 433 \\
49	DS & Rand & 0.25 & 0.257 & 0.257 & 0.190 & 496 & 433 \\
50	DS & Rand & 0.30 & 0.510 & 0.510 & 0.410 & 496 & 433 \\
51	\addlinespace
52	QW & Imp & 0.15 & 0.066 & 0.066 & 0.066 & 475 & 289 \\
53	QW & Imp & 0.20 & 0.307 & 0.307 & 0.325 & 475 & 289 \\
54	QW & Imp & 0.25 & 1.074 & 1.074 & 1.106 & 475 & 289 \\
55	QW & Imp & 0.30 & 3.155 & 3.155 & 3.581 & 475 & 289 \\
56	\addlinespace
57	QW & Rand & 0.15 & $-$0.011\textsuperscript{ns} & $-$0.011\textsuperscript{ns} & $-$0.011\textsuperscript{ns} & 475 & 289 \\
58	QW & Rand & 0.20 & 0.015\textsuperscript{ns} & 0.015\textsuperscript{ns} & 0.015\textsuperscript{ns} & 475 & 289 \\
59	QW & Rand & 0.25 & 0.393 & 0.393 & 0.266 & 475 & 289 \\
60	QW & Rand & 0.30 & 0.913 & 0.913 & 0.788 & 475 & 289 \\
61	\bottomrule
62	\end{tabular}
63	\end{table*}
64	
65	The main effect of increasing mpl is reduced $n_{\text{eff}}$: at mpl$=$20, DeepSeek retains 433/500 problems and Qwen retains 289/500 (mid-null rate rises to 71.2\% and 84.6\%, respectively). Despite this sample reduction, all significance conclusions hold.
66	
67	
68	\section{Segmentation Robustness}
69	\label{app:seg-robust}
70	
71	Table~\ref{tab:seg-robust} reports the paired median difference $\Delta$ under tercile, quartile, and quintile segmentation for both models under importance-based eviction. Phase gradient direction and statistical significance are preserved under quartile and quintile segmentation ($n{=}50$ spot check), indicating that the tercile-based findings are not an artifact of the segmentation choice.
72	
73	\begin{table*}[t]
74	\centering
75	\small
76	\caption{Segmentation robustness: median $\Delta$ under tercile ($n{=}496$/$475$), quartile ($n{=}50$ spot check), and quintile ($n{=}50$ spot check) segmentation. Importance-based eviction; all $p_{\text{Bonf}} < 10^{-7}$.}
77	\label{tab:seg-robust}
78	\begin{tabular}{@{}llccc@{}}
79	\toprule
80	Model & $s$ & Tercile & Quartile\; [95\% CI] & Quintile\; [95\% CI] \\
81	\midrule
82	\multirow{4}{*}{DeepSeek} & 0.15 & 0.391 & 0.491\; $[0.44,\; 0.70]$ & 0.505\; $[0.33,\; 0.71]$ \\
83	& 0.20 & 1.215 & 1.388\; $[1.05,\; 1.79]$ & 1.197\; $[1.02,\; 1.76]$ \\
84	& 0.25 & 3.986 & 4.322\; $[3.62,\; 8.06]$ & 4.960\; $[3.80,\; 9.02]$ \\
85	& 0.30 & 8.481 & 12.930\; $[9.83,\; 19.10]$ & 11.548\; $[10.06,\; 18.51]$ \\
86	\addlinespace
87	\multirow{4}{*}{Qwen} & 0.15 & 0.066 & 0.226\; $[0.14,\; 0.27]$ & 0.203\; $[0.13,\; 0.26]$ \\
88	& 0.20 & 0.307 & 0.561\; $[0.35,\; 0.77]$ & 0.517\; $[0.29,\; 0.75]$ \\
89	& 0.25 & 1.074 & 1.870\; $[1.05,\; 2.44]$ & 1.801\; $[1.13,\; 2.38]$ \\
90	& 0.30 & 3.155 & 4.097\; $[2.91,\; 4.94]$ & 4.009\; $[3.28,\; 5.34]$ \\
91	\bottomrule
92	\end{tabular}
93	\end{table*}
94	
95	The quartile and quintile $\Delta$ values are comparable to or slightly larger than tercile values because finer-grained segmentation isolates more extreme phases (the ``lowest'' quintile captures a more concentrated low-sparsity segment than the lowest tercile). The monotonic dose-response ($\Delta$ increasing with $s$) is preserved across all three segmentation schemes for both models, supporting that the severity gradient is not an artifact of the tercile segmentation choice.
96	
97	
98	\section{Robustness to Asymmetric Sparsity Allocation}
99	\label{app:asymmetric-robustness}
100	
101	Our main experiments use symmetric sparsity ($s_{\text{head}} = s_{\text{KV}} = s$). To verify that the phase-gated severity gradient does not depend on this symmetric assumption, we evaluate two asymmetric configurations at a fixed total sparsity budget equivalent to $s{=}0.25$, using importance-based eviction on DeepSeek-R1-Distill-Qwen-7B.
102	
103	\begin{table}[h]
104	\centering
105	\small
106	\caption{Asymmetric sparsity robustness: per-phase II under two head/KV allocations (DeepSeek, importance-based eviction, $n{=}50$ spot check).}
107	\label{tab:asymmetric-robust}
108	\begin{tabular}{@{}lcccccc@{}}
109	\toprule
110	Config & $s_{\text{head}}$ & $s_{\text{KV}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\Delta$ \\
111	\midrule
112	A (KV-heavy) & 0.20 & 0.30 & 19.51 & 6.05 & 0.38 & $+$19.13 \\
113	B (head-heavy) & 0.30 & 0.20 & 18.77 & 3.97 & 0.52 & $+$18.25 \\
114	\addlinespace
115	Symmetric & 0.25 & 0.25 & 3.97 & --- & 0.02 & $+$3.99 \\
116	\bottomrule
117	\end{tabular}
118	\end{table}
119	
120	Both asymmetric configurations produce large positive $\Delta$ ($+19.13$ and $+18.25$), supporting that the phase-gated severity gradient is robust to the head/KV allocation ratio. The KV-heavy configuration (A) exhibits higher mid-phase II ($6.05$ vs.\ $3.97$), suggesting that the KV eviction axis has a stronger impact on intermediate reasoning phases. Both asymmetric $\Delta$ values exceed the symmetric baseline ($3.99$), consistent with one axis operating at $s{=}0.30$---above the symmetric maximum tested---which amplifies overall severity. A systematic investigation of the full asymmetric interaction surface is left for future work.
121	
122	
123	\section{Outlier Robustness Analysis}
124	\label{app:outlier-robustness}
125	
126	The extreme mean/median ratio (up to $97{,}640{:}1$ in individual conditions) reflects heavy-tailed II distributions driven by near-zero denominators in specific problems. We verify robustness via symmetric winsorization at $5\%$ and $10\%$ levels. All median-based statistics---paired median difference $\Delta$, Wilcoxon signed-rank $p$-values, and amplification ratio $G$---are strictly invariant under winsorization, as expected for rank-based estimators. The five core claims---compound exceeds individual, importance exceeds random, monotonic dose-response, $G \gg 1$ for importance (auxiliary illustration of phase concentration), $G \approx 1$ for random---are fully robust. The extreme outlier severity further validates our choice of median-based inference over mean-based alternatives. $G$ values in this robustness analysis follow the ratio-of-medians convention (Table~\ref{tab:profiling-subset}); the primary $G$ definition (Eq.~\ref{eq:gradient}) is similarly invariant as a median of per-problem ratios.
127	
128	
129	\section{\texttt{&lt;think>} Token Phase Validation}
130	\label{app:think-validation}
131	
132	DeepSeek-R1-Distill-Qwen-7B generates explicit \texttt{&lt;think>}...\texttt{&lt;/think>} delimiters that demarcate chain-of-thought reasoning from final answers, providing a model-generated ground truth for reasoning phase boundaries. We evaluate whether our attention-sparsity-based phase segmentation (\S\ref{par:phase-segmentation}) recovers these boundaries on GSM8K ($n{=}48$ problems with valid phase assignments), using adaptive per-sequence quantile segmentation rather than a fixed global threshold.
133	
134	\paragraph{Naming convention.}
135	A note on terminology: DeepSeek's \texttt{&lt;think>} phase (active reasoning) exhibits \emph{low} attention sparsity---attention is broadly distributed across many positions during exploratory computation. Conversely, the answer phase exhibits \emph{high} attention sparsity---attention concentrates on a few positions during structured output. Thus PACS ``low-sparsity phase'' corresponds to the model's thinking phase, and ``high-sparsity phase'' to the answer phase. The physical phenomenon is consistent: broadly distributed attention characterizes reasoning in both frameworks.
136	
137	\paragraph{Token-level agreement.}
138	We binarize each token as ``thinking'' (inside \texttt{&lt;think>}) or ``answer'' (outside) and compare against the sparsity-based phase assignment. The adaptive segmentation achieves substantial agreement: $\kappa{=}0.88$ (per-problem mean $0.85$, median $0.88$), with token-level accuracy of $94.2\%$. Per-problem AUC-ROC is $0.98$ (median $0.99$), indicating near-perfect discriminability between thinking and answer phases based on attention sparsity alone. Of problems, $75\%$ achieve $\kappa \geq 0.80$ and $100\%$ achieve $\kappa \geq 0.60$. The \texttt{&lt;think>} phase exhibits significantly lower attention sparsity than the answer phase ($0.656$ vs.\ $0.763$; Cohen's $d{=}-0.80$), indicating that attention distribution breadth reliably distinguishes reasoning from structured computation.
139	
140	\paragraph{Boundary proximity.}
141	The median distance between the sparsity-based phase boundary and the nearest \texttt{&lt;think>}/\texttt{&lt;/think>} delimiter is 1 token, with $81.2\%$ of boundaries falling within 10 tokens. This tight alignment indicates that the attention sparsity transition closely tracks the model's self-identified shift from exploratory reasoning to structured answer generation.
142	
143	\paragraph{Phase composition and II correlation.}
144	We examine whether the fraction of thinking tokens within each phase correlates with compound severity (II). At the mid-phase level, the thinking-token fraction correlates with II (Spearman $\rho{=}0.49$, $p < 0.001$), consistent with mid-phase segments that contain more reasoning content being more vulnerable to compound sparsity. Low- and high-phase correlations are non-significant, as expected: these phases are compositionally dominated by thinking or answer tokens, respectively, leaving insufficient variance for correlation.
145	
146	\paragraph{MATH-500 indirect validation.}
147	Direct $\kappa$ validation requires explicit \texttt{&lt;think>} delimiters, available only on GSM8K. On MATH-500 ($n{=}500$), we instead assess \emph{temporal ordering consistency}: the fraction of problems where the low-sparsity phase precedes the high-sparsity phase, consistent with a thinking-then-answering generation structure. DeepSeek achieves a temporal ordering score of $0.576$ with $100\%$ of problems exhibiting the expected direction (low-sparsity before high-sparsity). Qwen, which lacks \texttt{&lt;think>} delimiters, shows weaker but directionally consistent temporal ordering ($0.479$). This indirect evidence supports the validity of sparsity-based phase segmentation on MATH-500 but does not constitute direct $\kappa$ validation.
148	
149	\paragraph{Scope.}
150	The direct $\kappa$ validation ($\kappa{=}0.88$, $n{=}48$) is limited to DeepSeek-R1-Distill-Qwen-7B on GSM8K; MATH-500 has only indirect (temporal ordering) validation. Qwen2.5-7B-Instruct does not produce explicit reasoning delimiters, precluding direct $\kappa$ validation on either benchmark. Phase segmentation is computed on the dense model's attention patterns and is independent of sparsity level, so the agreement statistics are reported once rather than per-$s$.
151	
152	
153	\subsection{Non-Think Token Quality Under Compound Sparsity}
154	\label{app:nt-samples}
155	
156	Tokens generated outside \texttt{&lt;think>}...\texttt{&lt;/think>} delimiters---i.e., the final answer tokens---fall predominantly in the high-sparsity attention phase, where compound interaction is minimal (\S\ref{sec:answer-region}: 93.2\% of \verb|\boxed{}| markers reside in the high-sparsity phase). We illustrate the differential impact of compound sparsity on non-think (answer) versus think (reasoning) tokens with two representative examples from the GSM8K validation set (DeepSeek-R1-Distill-Qwen-7B, $s{=}0.25$, importance-based eviction).
157	
158	\paragraph{Example 1: Preserved answer, degraded reasoning.}
159	Under compound sparsity, the non-think answer tokens (\texttt{The answer is 42}) are generated with near-baseline perplexity (PPL ratio $1.2{\times}$), while the preceding think-phase tokens exhibit $4.8{\times}$ PPL inflation. The final answer remains correct despite substantial reasoning-trace degradation---a ``silent reasoning error'' scenario where intermediate logic is corrupted but the output format masks the damage.
160	
161	\paragraph{Example 2: Cascading failure at high sparsity.}
162	At $s{=}0.30$, reasoning-phase PPL inflation ($11.3{\times}$) propagates into the answer phase: the model produces a syntactically valid but numerically incorrect \verb|\boxed{}| output (PPL ratio $3.1{\times}$ on answer tokens vs.\ $1.1{\times}$ at $s{=}0.15$). This illustrates the sparsity threshold beyond which compound severity breaches the phase boundary, consistent with the accuracy cliff observed for Qwen at $s{=}0.30$ ($\delta{=}-27$\,pp; Table~\ref{tab:accuracy}).
163	
164	\paragraph{Implication.}
165	These examples illustrate that pruning-induced compound severity is phase-selective: non-think tokens are relatively protected at moderate sparsity ($s \leq 0.25$) because they coincide with the high-sparsity attention phase where importance scores retain discriminative power. At higher sparsity ($s{=}0.30$), discrimination collapse (\S\ref{sec:discrimination-collapse-main}) erodes this protection, and compound severity spills into the answer phase.
166	
167	
168	\section{Amplification Ratio ($G$) Details}
169	\label{app:g-metric}
170	
171	The per-problem amplification ratio $G^{(i)} = \mathrm{II}^{(i)}_{\textit{low}} / \mathrm{II}^{(i)}_{\textit{high}}$ (Eq.~\ref{eq:gradient}) provides an auxiliary illustrative perspective on the primary metric $\Delta$. Table~\ref{tab:g-metric} reports $G$ with bootstrap 95\% CIs for all conditions. $G$ serves as a visualization aid; primary statistical evidence for the phase-modulated severity gradient is provided by $\Delta$ and the associated Wilcoxon tests (\S\ref{sec:phase-amplification}).
172	
173	\begin{table*}[t]
174	\centering
175	\small
176	\caption{Per-problem amplification ratio $G$ (median of $G^{(i)}$) with bootstrap 95\% CIs ($B{=}10{,}000$). $G$ serves as an auxiliary visualization of phase concentration; primary statistical evidence for the severity gradient is provided by the Interaction Index $\Delta$ (\S\ref{sec:phase-amplification}). $G \gg 1$ suggests phase-concentrated severity; $G \approx 1$ suggests uniform severity across phases.}
177	\label{tab:g-metric}
178	\begin{tabular}{@{}llcc@{}}
179	\toprule
180	$s$ & Strategy & $G$\; [95\% CI] (DeepSeek) & $G$\; [95\% CI] (Qwen) \\
181	\midrule
182	0.15 & Importance & $\mathbf{7.5}$\; $[4.1,\; 11.4]$ & n.d.$^{\dagger}$ \\
183	0.15 & Random     & 0.5\; $[0.4,\; 0.6]$ & 0.7\; $[0.4,\; 0.8]$ \\
184	\addlinespace
185	0.20 & Importance & $\mathbf{17.9}$\; $[12.7,\; 26.3]$ & $\mathbf{2.6}$\; $[0.5,\; 5.1]$ \\
186	0.20 & Random     & 0.8\; $[0.6,\; 0.9]$ & 0.9\; $[0.7,\; 1.0]$ \\
187	\addlinespace
188	0.25 & Importance & $\mathbf{49.1}$\; $[40.1,\; 57.8]$ & $\mathbf{9.5}$\; $[5.2,\; 14.8]$ \\
189	0.25 & Random     & 1.1\; $[1.0,\; 1.2]$ & 1.3\; $[1.2,\; 1.4]$ \\
190	\addlinespace
191	0.30 & Importance & $\mathbf{79.8}$\; $[63.3,\; 96.5]$ & $\mathbf{36.9}$\; $[25.3,\; 49.1]$ \\
192	0.30 & Random     & 1.1\; $[1.0,\; 1.3]$ & 1.3\; $[1.2,\; 1.4]$ \\
193	\bottomrule
194	\multicolumn{4}{@{}p{0.85\textwidth}}{\footnotesize $^{\dagger}$ $\widetilde{\mathrm{II}}_{\textit{high}} \approx 0$; ratio undefined ($G$ CI: $[-0.2, 0.9]$). $\Delta{=}0.07$, $p{=}8.7 \times 10^{-15}$ supports $\mathrm{II}_{\textit{low}} > \mathrm{II}_{\textit{high}}$.}
195	\end{tabular}
196	\end{table*}
197	
198	The $G$ values illustrate that phase-concentrated severity is associated with importance-based eviction ($G{=}7.5$--$79.8{\times}$ for DeepSeek, $2.6$--$36.9{\times}$ for Qwen), while random eviction suggests weak modulation at $s \geq 0.25$ ($G \approx 1.1$--$1.3$; CIs exclude 1) and near-uniform severity at $s \leq 0.20$ (CIs span or touch 1). The monotonic increase in $G$ with sparsity is consistent with the $\Delta$ dose-response in Table~\ref{tab:main-results}, but $G$ should be interpreted as a descriptive ratio rather than an independent statistical test---the formal evidence rests on the paired $\Delta$ and associated Wilcoxon tests.
199	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "055846ea-5348-458a-aecb-f653f5e79cf0",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "38c69eb2-7af3-48f8-b04e-48280b9efbf0",
  "sourceToolAssistantUUID": "055846ea-5348-458a-aecb-f653f5e79cf0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-16T08:15:35.043Z_

<details open><summary>🔧 Tool call — Read · `toolu_0128xPytCf8Tu2HgpMP2m67t`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_moved.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c69eb2-7af3-48f8-b04e-48280b9efbf0",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v2zDMPA1ptgicxp1VL",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8419df8e-d9e5-4d07-8245-57cb45578b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hn8pqRgJFZUEBKnjrPwwnm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7274,
      "cache_read_input_tokens": 45481,
      "output_tokens": 95,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7274
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 95,
          "cache_read_input_tokens": 45481,
          "cache_creation_input_tokens": 7274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7274,
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

_source line 34 · 2026-05-16T08:15:35.059Z_

<details><summary>↩ Tool result · `toolu_0128xPytCf8Tu2HgpMP2m67t`</summary>

```text
1	
2	\section{Phase-Strategy Crossover Details}
3	\label{app:crossover-details}
4	
5	On DeepSeek ($n{=}496$), a strategy ranking reversal emerges at $s{=}0.25$ (Figure~\ref{fig:crossover}): importance-based eviction yields \emph{lower} II than random in the high-sparsity phase ($0.021$ vs.\ $1.113$) but \emph{higher} II in the low-sparsity phase ($3.971$ vs.\ $1.514$---a $2.6{\times}$ reversal; both $p < 10^{-4}$). This crossover is observed at all four sparsity levels, with reversal magnitude of $4.0{\times}$ at $s{=}0.15$, $3.4{\times}$ at $s{=}0.20$, $2.6{\times}$ at $s{=}0.25$, and $2.2{\times}$ at $s{=}0.30$ (decreasing as random eviction severity rises). The reversal arises because head pruning redistributes attention mass, altering importance rankings in a way that couples the two sparsity mechanisms in low-sparsity phases (\S\ref{sec:discrimination-collapse-main}). Qwen does not exhibit a crossover: importance-based eviction produces lower II than random in both phases across all sparsity levels (e.g., at $s{=}0.25$: high $0.004$ vs.\ $1.108$; low $1.053$ vs.\ $1.769$).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig3_crossover.pdf}
10	\caption{Strategy-dependent crossover at $s{=}0.25$ on DeepSeek ($n{=}496$). Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces $2.6{\times}$ higher II in the low-sparsity phase, reversing the strategy ranking.}
11	\label{fig:crossover}
12	\end{figure}
13	
14	
15	\section{Profiling Subset Per-Phase Breakdown}
16	\label{app:profiling-subset}
17	
18	\begin{table*}[t]
19	\centering
20	\small
21	\caption{Per-phase interaction index (II) from the $n{=}50$ profiling subset (DeepSeek-R1-Distill-Qwen-7B). This preliminary table does not include per-condition bootstrap CIs; full-scale values with bootstrap 95\% CIs ($B{=}10{,}000$) at $n{=}496$ appear in Table~\ref{tab:main-results}, and strategy-contrast CIs for this subset appear in the permutation test (Table~\ref{tab:permutation}). $G$ values use the ratio-of-medians definition ($\widetilde{\mathrm{II}}_{\textit{low}} / \widetilde{\mathrm{II}}_{\textit{high}}$) and serve as an auxiliary illustration of phase concentration; the primary evidence is $\Delta$ (see Appendix~\ref{app:g-metric}). At low sparsity ($s{=}0.15$), the ratio-of-medians and per-problem definitions diverge ($7.5{\times}$ vs.\ $69{\times}$) because per-problem ratios are sensitive to near-zero $\mathrm{II}_{\textit{high}}$ values.}
22	\label{tab:profiling-subset}
23	\begin{tabular}{@{}llccccr@{}}
24	\toprule
25	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{mid}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$ & $G$ \\
26	\midrule
27	0.15 & Importance & 0.006 & 0.081 & 0.398 & 0.39 & $\mathbf{69}$ \\
28	0.15 & Random     & 0.093 & 0.097 & 0.103 & 0.01 & 1.1 \\
29	\addlinespace
30	0.20 & Importance & 0.015 & 0.203 & 1.496 & 1.48 & $\mathbf{103}$ \\
31	0.20 & Random     & 0.292 & 0.350 & 0.276 & $-$0.02 & 0.9 \\
32	\addlinespace
33	0.25 & Importance & 0.032 & 1.118 & 7.196 & 7.16 & $\mathbf{222}$ \\
34	0.25 & Random     & 0.818 & 0.932 & 1.363 & 0.54 & 1.7 \\
35	\addlinespace
36	0.30 & Importance & 0.053 & 2.283 & 14.639 & 14.59 & $\mathbf{274}$ \\
37	0.30 & Random     & 2.503 & 2.592 & 4.041 & 1.54 & 1.6 \\
38	\bottomrule
39	\end{tabular}
40	\end{table*}
41	
42	The $n{=}50$ profiling subset served as a preliminary calibration; all importance-based $\Delta$ values were subsequently replicated at $n{=}496$ with bootstrap 95\% CIs excluding zero (Table~\ref{tab:main-results}: $\Delta{=}0.39$\;$[0.35,\;0.44]$ to $8.48$\;$[7.75,\;9.69]$). The paired permutation test on this subset ($n{=}49$; Table~\ref{tab:permutation}) provides bootstrap 95\% CIs for the strategy contrast ($\widetilde{\Delta}_{\text{imp}} - \widetilde{\Delta}_{\text{rand}}$), all excluding zero after Bonferroni correction.
43	
44	
45	\section{Cross-Training-Paradigm Replication Details}
46	\label{app:cross-model-details}
47	
48	Both models share the Qwen2ForCausalLM backbone (28 layers, 28 heads, 4-group GQA) but differ in training: DeepSeek uses reasoning distillation from DeepSeek-R1, while Qwen2.5 uses standard instruction tuning without explicit reasoning delimiters. This within-architecture-family comparison enables assessment of training methodology effects on the compound sparsity interaction, though causal attribution is limited by the observational design.
49	
50	Despite lacking explicit \texttt{&lt;think>} delimiters, Qwen2.5-7B-Instruct exhibits sufficient variation in attention sparsity to permit phase segmentation via the same quantile-based method (\S\ref{par:phase-segmentation}). Twenty-five of the 500 problems are excluded due to degenerate phase assignments, yielding $n{=}475$ valid problems for Qwen (vs.\ $n{=}496$ for DeepSeek).
51	
52	\paragraph{Per-phase effective sample size.}
53	\label{app:qwen-null-rate}
54	Table~\ref{tab:qwen-effective-n} reports the per-phase effective sample size for Qwen2.5-7B-Instruct, defined as the number of problems with non-null phase segments (segment length $\geq$ \texttt{min\_phase\_length}). The mid-phase null rate (45.2\%) reflects problems where mid-sparsity tokens do not form contiguous runs above the merging threshold; this does not affect the low--high contrast ($\Delta$) used in the primary analysis.
55	
56	\begin{table}[t]
57	\centering
58	\small
59	\caption{Per-phase effective sample size for Qwen2.5-7B-Instruct ($n_{\text{eff}} = 475$). Phase segmentation is performed once on dense-model attention patterns and is independent of sparsity level.}
60	\label{tab:qwen-effective-n}
61	\begin{tabular}{@{}lcccc@{}}
62	\toprule
63	Phase & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
64	\midrule
65	High & 475 & 475 & 475 & 475 \\
66	Mid  & 274 & 274 & 274 & 274 \\
67	Low  & 475 & 475 & 475 & 475 \\
68	\bottomrule
69	\end{tabular}
70	\end{table}
71	
72	Table~\ref{tab:cross-model} reports the cross-training-paradigm comparison. Qwen reproduces the monotonic severity gradient at ${\sim}1/5$ of DeepSeek's magnitude. Figure~\ref{fig:cross-model} visualizes this comparison.
73	
74	\begin{table}[t]
75	\centering
76	\small
77	\caption{Cross-training-paradigm comparison of median compound severity difference ($\Delta$) under importance-based eviction.}
78	\label{tab:cross-model}
79	\begin{tabular}{@{}lcccc@{}}
80	\toprule
81	Model & $s{=}0.15$ & $s{=}0.20$ & $s{=}0.25$ & $s{=}0.30$ \\
82	\midrule
83	DeepSeek-R1-Distill-Qwen-7B ($n{=}496$) & 0.39 & 1.21 & 3.99 & 8.48 \\
84	Qwen2.5-7B-Instruct ($n{=}475$)         & 0.07 & 0.31 & 1.07 & 3.16 \\
85	\bottomrule
86	\end{tabular}
87	\end{table}
88	
89	\begin{figure}[t]
90	\centering
91	\includegraphics[width=\columnwidth]{fig5_crossmodel.pdf}
92	\caption{Cross-training-paradigm comparison of the median severity difference under importance-based eviction ($n{=}496$/$475$). Both DeepSeek (solid) and Qwen (dashed) exhibit monotonically increasing $\Delta$ with sparsity; Qwen's magnitude is approximately one-quarter to one-sixth of DeepSeek's.}
93	\label{fig:cross-model}
94	\end{figure}
95	
96	\paragraph{Per-problem concordance.}
97	The per-problem concordance across models is not significant (mean $\rho = -0.107$, $p = 0.926$), indicating that while the aggregate gradient direction replicates, the specific problems driving severity differ between models---consistent with model-specific attention patterns rather than a universal per-problem vulnerability ranking.
98	
99	\paragraph{Random eviction control.}
100	As a control, random eviction on Qwen mirrors DeepSeek: non-significant at $s \leq 0.20$ ($\Delta$: $-0.01$, $0.02$; CIs span zero) but significant at $s \geq 0.25$ ($\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$). Where significant, the random phase gradient is $2.7$--$3.5{\times}$ weaker than importance-based ($0.39$ vs.\ $1.07$ at $s{=}0.25$; $0.91$ vs.\ $3.16$ at $s{=}0.30$), supporting strategy-specific amplification.
101	
102	
103	\section{Permutation Test Details}
104	\label{app:permutation-details}
105	
106	For each problem $i$ and sparsity level $s$, we compute the compound severity difference $\Delta_i^{(\text{strat})} = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under each eviction strategy. The test statistic is the median of the paired difference $\widetilde{\Delta} = \text{median}_i\!\bigl(\Delta_i^{(\text{imp})} - \Delta_i^{(\text{rand})}\bigr)$, measuring whether importance-based eviction produces systematically larger phase-dependent severity than random eviction. We permute strategy labels $10{,}000$ times to construct the null distribution and apply Bonferroni correction for 4 sparsity-level comparisons.
107	
108	Per-problem distributions of the paired severity difference $\Delta_i = \mathrm{II}_{\textit{low},i} - \mathrm{II}_{\textit{high},i}$ under importance-based eviction are right-skewed at all sparsity levels, with mean/median ratios ranging from $1.2{\times}$ ($s{=}0.15$) to $1.6{\times}$ ($s{=}0.30$) for DeepSeek and $1.1{\times}$ to $1.4{\times}$ for Qwen.
109	
110	The permutation null distributions are approximately symmetric around zero at all sparsity levels. At $s{=}0.15$, the observed statistic falls at the $99.92$th percentile of the null ($p_{\text{Bonf}} = 0.0032$); at $s \geq 0.20$, no permutation exceeds the observed statistic.
111	
112	Table~\ref{tab:permutation} reports the results. All four sparsity levels reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$), with observed median differences increasing monotonically from $0.37$ at $s{=}0.15$ to $9.85$ at $s{=}0.30$. The monotonic growth of both the point estimate and the CI lower bound ($0.19 \to 0.69 \to 1.66 \to 6.70$) supports that compound severity amplification strengthens with sparsity---not merely in central tendency but also in worst-case lower bounds. Figure~\ref{fig:permtest-forest} presents these results as a forest plot.
113	
114	\begin{table}[t]
115	\centering
116	\small
117	\caption{Paired permutation test for compound severity: importance vs.\ random eviction on DeepSeek-R1-Distill-Qwen-7B ($n{=}49$ profiling subset, $10{,}000$ permutations, Bonferroni-corrected). The monotonic $\Delta$ pattern is supported at $n{=}496$ (Table~\ref{tab:aggregate-ii}).}
118	\label{tab:permutation}
119	\begin{tabular}{@{}rrcl@{}}
120	\toprule
121	$s$ & Observed $\widetilde{\Delta}$ & 95\% CI & $p_{\text{Bonf}}$ \\
122	\midrule
123	0.15 & 0.37 & $[0.19,\; 0.62]$ & 0.0032 \\
124	0.20 & 0.97 & $[0.69,\; 1.49]$ & ${<}\,0.001$ \\
125	0.25 & 3.34 & $[1.66,\; 6.64]$ & ${<}\,0.001$ \\
126	0.30 & 9.85 & $[6.70,\; 16.29]$ & ${<}\,0.001$ \\
127	\bottomrule
128	\end{tabular}
129	\end{table}
130	
131	\begin{figure}[t]
132	\centering
133	\includegraphics[width=\columnwidth]{fig4_bootstrap.pdf}
134	\caption{Forest plot of permutation test results. Horizontal bars show 95\% permutation CIs; diamonds mark observed median differences $\widetilde{\Delta}$. All CIs lie entirely above zero, supporting significant strategy-dependent severity at every sparsity level.}
135	\label{fig:permtest-forest}
136	\end{figure}
137	
138	
139	\section{Cross-Architecture Analysis}
140	\label{app:cross-arch}
141	
142	To test whether the phase-modulated severity pattern extends beyond the Qwen2 architecture, we replicate the experiment on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, 8B parameters; $n{=}49$ paired problems). Table~\ref{tab:llama-cross-arch} reports the strategy-dependent severity comparison across sparsity levels.
143	
144	The evidence for a strategy contrast on LLaMA is mixed: at $s{=}0.15$, the bootstrap CI excludes zero ($[0.002, 0.043]$) but the Bonferroni-corrected Wilcoxon test is non-significant ($p_{\text{Bonf}}{=}0.219$); conversely, at $s{=}0.30$ the CI spans zero ($[-0.069, 0.544]$) while the Wilcoxon test reaches significance ($p_{\text{Bonf}}{=}0.029$). At intermediate levels ($s \in \{0.20, 0.25\}$), neither CI nor Wilcoxon reaches significance. The median paired difference increases monotonically ($\widetilde{\Delta}$: $0.020 \to 0.356$), consistent with a genuine but weak trend---providing preliminary support for the cross-architecture hypothesis while underscoring the substantially weaker interaction on LlamaForCausalLM.\footnote{The CI/Wilcoxon discrepancy reflects differing power profiles under small $n$ with heavy-tailed distributions: the percentile bootstrap CI is based on the resampled median distribution and is less sensitive to tail observations, while the Wilcoxon signed-rank test uses signed ranks and is more sensitive to tail outliers. This inconsistency itself supports the conservative ``mixed/weak evidence'' interpretation.}
145	
146	The absolute magnitude is architecture-dependent: LLaMA severity differences are ${\sim}40{\times}$ smaller than DeepSeek and ${\sim}7{\times}$ smaller than Qwen. Notably, random eviction on LLaMA also exhibits a non-trivial phase gradient ($d_z$: $0.35 \to 0.44$), substantially reducing the strategy contrast that is the hallmark of the phase-strategy interaction on Qwen2 models. This suggests that the strength of the strategy$\times$phase interaction---not merely the severity gradient itself---is architecture-dependent. The directional pattern---importance producing larger phase gradients than random---is qualitatively consistent across all three models, but the LLaMA evidence should be interpreted as preliminary given the weak interaction magnitude and partial statistical significance.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Cross-architecture validation on DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM). $\widetilde{\Delta}$: median paired difference (importance $-$ random) with bootstrap 95\% CI ($B{=}10{,}000$); $p$: Bonferroni-corrected Wilcoxon signed-rank $p$ ($k{=}4$). $n{=}49$ paired problems.}
152	\label{tab:llama-cross-arch}
153	\begin{tabular}{@{}lcc@{}}
154	\toprule
155	$s$ & $\widetilde{\Delta}$\; [95\% CI] & $p_{\text{Bonf}}$ \\
156	\midrule
157	0.15 & $0.020$\; $[0.002,\; 0.043]$ & $0.219$ \\
158	0.20 & $0.022$\; $[-0.090,\; 0.187]$ & $0.253$ \\
159	0.25 & $0.095$\; $[-0.004,\; 0.303]$ & $0.083$ \\
160	0.30 & $0.356$\; $[-0.069,\; 0.544]$ & $\mathbf{0.029}$ \\
161	\bottomrule
162	\end{tabular}
163	\end{table}
164	
165	\paragraph{Post-hoc power analysis.}
166	We computed post-hoc power via bootstrap simulation ($B{=}10{,}000$) to assess what claims the $n{=}49$ sample can and cannot support. For the within-importance phase gradient (testing $\Delta_{\text{imp}} > 0$), power exceeds $0.99$ at all four sparsity levels, indicating that the sample is sufficient to detect the importance-based severity gradient. For strategy comparisons (testing $\Delta_{\text{imp}} - \Delta_{\text{rand}} > 0$), power ranges from $0.26$ ($s{=}0.15$) to $0.63$ ($s{=}0.30$), indicating that the sample is underpowered for detecting strategy-level differences at their observed effect sizes. Extrapolating from the observed effect sizes and variance, $n \geq 200$ paired problems would be needed to achieve $0.80$ power for the strategy comparison at $s{=}0.30$. This motivates the conservative interpretation in \S\ref{sec:cross-arch}: the within-importance gradient is supported, but the strategy$\times$phase interaction requires larger-scale replication.
167	
168	
169	\section{Analysis: Importance Discrimination Collapse}
170	\label{app:analysis}
171	
172	\subsection{Importance Discrimination Collapse}
173	\label{sec:discrimination-collapse}
174	
175	Head pruning reduces the number of heads contributing to cumulative importance scores, collapsing the score distribution. Table~\ref{tab:discrimination-metrics-full} quantifies this effect: the Gini coefficient decreases by $0.030$--$0.081$ (DeepSeek) and $0.010$--$0.020$ (Qwen) after pruning, with consistent negative deltas across all 16 conditions (both models $\times$ 4 sparsity levels $\times$ 2 strategies). The CV delta is likewise negative in all 8 importance-based conditions. The same pattern holds under random eviction, indicating that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
176	
177	\begin{table}[t]
178	\centering
179	\caption{Importance discrimination collapse under importance-based eviction. $\Delta\mathrm{Gini}$ and $\Delta\mathrm{CV}$ are post-pruning minus baseline; negative values indicate reduced discriminative power.}
180	\label{tab:discrimination-metrics-full}
181	\small
182	\begin{tabular}{llrr}
183	\toprule
184	Model & $s$ & $\Delta\mathrm{Gini}$ & $\Delta\mathrm{CV}$ \\
185	\midrule
186	DeepSeek & $0.15$ & $-0.030$ & $-0.56$ \\
187	DeepSeek & $0.20$ & $-0.040$ & $-0.77$ \\
188	DeepSeek & $0.25$ & $-0.065$ & $-1.29$ \\
189	DeepSeek & $0.30$ & $-0.081$ & $-1.66$ \\
190	\midrule
191	Qwen & $0.15$ & $-0.010$ & $-0.05$ \\
192	Qwen & $0.20$ & $-0.012$ & $-0.21$ \\
193	Qwen & $0.25$ & $-0.010$ & $-1.49$ \\
194	Qwen & $0.30$ & $-0.020$ & $-1.14$ \\
195	\bottomrule
196	\end{tabular}
197	\end{table}
198	
199	When importance scores lose discriminability, thresholding degenerates into noise-sensitive selection---functionally approaching biased random eviction. This is phase-dependent: in low-sparsity phases, attention is already broadly distributed, so pruning-induced collapse has maximum impact; in high-sparsity phases, concentration is preserved. Random eviction is immune because its decisions are independent of score quality, consistent with $G \approx 1$.
200	
201	\subsection{Entropy Redistribution}
202	\label{sec:entropy-redistribution}
203	
204	Beyond importance discrimination collapse, we examine whether head pruning also redistributes the attention entropy of surviving heads. We measure the mean attention entropy per head:
205	\begin{equation}
206	    \mathcal{H}_i^{(h)} = -\sum_{j=1}^{T} a_{ij}^{(h)} \log a_{ij}^{(h)}
207	    \label{eq:attn-entropy}
208	\end{equation}
209	and compute $\Delta\mathcal{H}$ as the change from baseline (no pruning) to the pruned condition.
210	
211	For DeepSeek under importance-based eviction, the entropy delta is consistently negative across all four sparsity levels ($\Delta\mathcal{H} \in [-0.047, -0.040]$; Table~\ref{tab:entropy-deltas}), indicating that importance-based pruning systematically selects heads whose removal concentrates attention in the surviving heads, reinforcing importance discrimination collapse.
212	
213	For Qwen, the entropy pattern only partially replicates. The delta is negative at $s{=}0.15$ ($\Delta\mathcal{H} = -0.073$) and $s{=}0.20$ ($-0.076$), consistent with DeepSeek. However, at $s{=}0.25$, the delta reverses to $+0.045$, with 22 of 30 problems showing positive entropy change. At $s{=}0.30$, the delta is near zero ($-0.007$). The $s{=}0.25$ reversal is systematic rather than a statistical artifact: it is consistent across all three reasoning phases (low: $+0.042$, mid: $+0.034$, high: $+0.017$). We interpret this as a genuine model-specific difference, possibly arising from distinct head specialization patterns: Qwen's instruction tuning (vs.\ DeepSeek's distillation-based training) may produce head configurations where removing 25\% of heads triggers compensatory broadening rather than concentration.
214	
215	We characterize importance discrimination collapse as the robust, model-independent driver of the phase-strategy interaction, with entropy redistribution as a secondary amplifier that is consistent in DeepSeek but model-dependent in Qwen.
216	
217	\begin{table}[t]
218	\centering
219	\caption{Attention entropy deltas ($\Delta\mathcal{H}$) under importance-based eviction. DeepSeek shows consistent entropy compression; Qwen partially replicates with a reversal at $s{=}0.25$.}
220	\label{tab:entropy-deltas}
221	\small
222	\begin{tabular}{llr}
223	\toprule
224	Model & $s$ & $\Delta\mathcal{H}$ \\
225	\midrule
226	DeepSeek & $0.15$ & $-0.040$ \\
227	DeepSeek & $0.20$ & $-0.047$ \\
228	DeepSeek & $0.25$ & $-0.045$ \\
229	DeepSeek & $0.30$ & $-0.044$ \\
230	\midrule
231	Qwen & $0.15$ & $-0.073$ \\
232	Qwen & $0.20$ & $-0.076$ \\
233	Qwen & $0.25$ & $+0.045$ \\
234	Qwen & $0.30$ & $-0.007$ \\
235	\bottomrule
236	\end{tabular}
237	\end{table}
238	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8419df8e-d9e5-4d07-8245-57cb45578b5e",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "f170016b-3fdc-49c8-a872-c289acf9ac2f",
  "sourceToolAssistantUUID": "8419df8e-d9e5-4d07-8245-57cb45578b5e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-16T08:15:42.791Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AuMoYa4tqc5yyZkiKSWGpx`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/appendix_disc_analysis.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f170016b-3fdc-49c8-a872-c289acf9ac2f",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v3gEeYFU7eFh674o95",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4a11ed00-2916-45c1-853c-fc90dba5c557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017QiCKY6fc1roCxgNKajmMk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7465,
      "cache_read_input_tokens": 52755,
      "output_tokens": 97,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7465
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 97,
          "cache_read_input_tokens": 52755,
          "cache_creation_input_tokens": 7465,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7465,
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

_source line 36 · 2026-05-16T08:15:42.800Z_

<details><summary>↩ Tool result · `toolu_01AuMoYa4tqc5yyZkiKSWGpx`</summary>

```text
1	\section{Importance Discrimination Collapse Details}
2	\label{app:discrimination-collapse-details}
3	
4	This cross-model consistency (Table~\ref{tab:discrimination-metrics-full}) supports importance discrimination collapse as a robust consequence of compound sparsity. When importance scores lose discriminative power, thresholding the bottom-$s$ fraction becomes noise-sensitive: small perturbations change which positions cross the eviction boundary. In the limit of perfectly uniform scores, importance-based eviction degenerates into an arbitrary selection functionally equivalent to biased random eviction. The same pattern holds under random eviction (DeepSeek: $-0.031$ to $-0.071$; Qwen: $-0.019$ to $-0.046$), indicating that importance discrimination collapse is a consequence of head pruning \emph{per se}, not of the eviction strategy.
5	
6	
7	\section{Extended Discussion}
8	\label{app:extended-discussion}
9	
10	\paragraph{On the predictability of phase-modulated severity.}
11	The compound interaction is not uniformly fragile---it is selectively fragile in a phase-dependent manner ($\widetilde{\mathrm{II}}_{\text{high}} < 0.06$ at $s \leq 0.30$).
12	
13	\paragraph{Random masking as falsification control.}
14	At $n{=}500$, random eviction develops a detectable but weak phase gradient above $s \approx 0.20$: non-significant at $s \leq 0.20$ for both models, but significant at $s \geq 0.25$ (DS: $\Delta{=}0.26$--$0.51$, $p_{\text{Bonf}} < 0.006$; QW: $\Delta{=}0.39$--$0.91$, $p_{\text{Bonf}} < 10^{-10}$). Where significant, the random phase gradient is $2.7$--$17{\times}$ weaker than importance-based (restricted to conditions where both strategies are significant, $s \geq 0.25$), supporting that the dominant amplification is strategy-specific.
15	
16	\paragraph{Entropy mechanism boundary conditions.}
17	Directly measuring per-head entropy shifts across architecturally distinct models---and identifying what training-time properties determine whether entropy concentrates or disperses under head pruning---would clarify the boundary conditions of the full mechanism.
18	
19	
20	\section{Pilot Mitigation Experiment}
21	\label{app:pilot-mitigation}
22	
23	We explored oracle phase-aware budget reallocation, shifting sparsity budget from high-severity low-sparsity phases to low-severity high-sparsity phases ($n{=}30$ problems at $s{=}0.25$). Oracle recovery---the fraction of compound interaction eliminated by phase-aware allocation---reached 18\% (95\% CI: $[-39\%, 45.8\%]$; Wilcoxon $p = 0.002$), below the pre-registered 30\% gate for claiming practical mitigation. A heuristic variant achieved 32\% recovery (95\% CI: $[-22.8\%, 66\%]$; $p = 0.024$). \textbf{Critically, 95\% bootstrap CIs for both conditions span zero}, meaning neither recovery estimate is statistically distinguishable from no improvement. \textbf{Gate status: FAIL}---neither oracle nor heuristic recovery meets the pre-registered threshold, and neither is statistically distinguishable from zero improvement. These results indicate that phase-aware budget reallocation alone is insufficient to neutralize the severity gradient; effective mitigation likely requires joint optimization of budget allocation and eviction strategy selection across phases.
24	
25	
26	\section{Extended Limitations}
27	\label{app:limitations}
28	
29	\paragraph{Model scale.}
30	All experiments are conducted at the 7B parameter scale.
31	Whether the phase-modulated severity patterns persist, amplify, or attenuate at larger scales (e.g., 70B) remains untested.
32	Larger models may exhibit different attention redundancy structures that alter the importance discrimination collapse dynamics (and the model-dependent entropy component may behave differently at scale).
33	
34	
35	\paragraph{Architectural scope.}
36	Our two models---DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct---share the Qwen2ForCausalLM architecture.
37	The cross-training-paradigm replication (\S\ref{sec:cross-model}) suggests that the findings are not artifacts of a single model's weights, though both models share the same Qwen2ForCausalLM architecture.
38	Pilot cross-architecture evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, \S\ref{sec:cross-arch}, Appendix~\ref{app:cross-arch}) suggests qualitatively consistent within-importance phase gradients ($d_z \sim 1.0$) but a substantially weaker strategy $\times$ phase interaction than in Qwen2-based architectures; random pruning also exhibits a non-trivial phase gradient on LLaMA, reducing the strategy contrast. This preliminary evidence ($s{=}0.30$ Wilcoxon $p_{\text{Bonf}}{=}0.029$; $s \leq 0.25$ non-significant) is consistent with the qualitative pattern extending beyond Qwen2 but is insufficient for definitive cross-architecture claims; quantitative impact is architecture-dependent. Comprehensive cross-architecture validation across more diverse designs (e.g., Mistral, multi-latent attention architectures) and scales remains an important next step.
39	
40	
41	\paragraph{Task coverage.}
42	We evaluate exclusively on MATH-500, a mathematical reasoning benchmark.
43	Different reasoning tasks---code generation, commonsense reasoning, multi-hop question answering---may induce different phase structures with different sparsity distributions, potentially altering the severity gradient profile.
44	Generalizing the phase-strategy interaction to broader reasoning domains is an important next step.
45	
46	
47	\paragraph{Statistical scope.}
48	Bootstrap confidence intervals use $B{=}10{,}000$ resamples (seed$=$42). The primary analysis uses $n{=}496$ paired problems for DeepSeek (4 excluded) and $n{=}475$ for Qwen (25 excluded); the permutation test (Table~\ref{tab:permutation}) uses $n{=}49$ from an initial profiling subset.
49	The severity difference distribution is right-skewed (mean/median ratios up to $43{:}1$), motivating our use of medians and nonparametric tests rather than parametric alternatives.
50	All four profiling-subset permutation tests reject $H_0$ after Bonferroni correction ($p_{\text{Bonf}} < 0.005$; Table~\ref{tab:permutation}), with CI lower bounds increasing from $0.19$ to $6.70$---supporting the effect direction at every sparsity level. At $n{=}496$, Wilcoxon signed-rank tests support all conditions with $p_{\text{Bonf}} < 10^{-13}$ (Table~\ref{tab:cohens-d}). The permutation CIs at higher sparsity are wider (e.g., $[6.70,\; 16.29]$ at $s{=}0.30$), reflecting genuine variance in per-problem severity amplification.
51	
52	At $n{=}500$, random eviction on both models becomes significant at $s \geq 0.25$ (Qwen: $\Delta{=}0.39$, $p_{\text{Bonf}} < 10^{-10}$ at $s{=}0.25$; $\Delta{=}0.91$, $p_{\text{Bonf}} < 10^{-13}$ at $s{=}0.30$; bootstrap CIs exclude zero).
53	These effects are genuine but $2.7$--$20{\times}$ weaker than importance-based eviction at the same sparsity levels, consistent with a weak phase gradient that is detectable at sufficient sample size but not the primary driver of compound severity.
54	
55	\paragraph{Sparsity range.}
56	Our primary analysis spans $s \in \{0.15, 0.20, 0.25, 0.30\}$; pilot data at $s{=}0.10$ and $s{=}0.35$ exist (6 total sparsity levels) but are not included in the main analysis due to limited sample size at these boundary conditions. Monotonicity is established at the tested sparsity levels (JT test $p \ll 10^{-10}$); the functional form of $G(s)$ between and beyond these levels is not characterized.
57	More extreme sparsity ($s > 0.50$) may exhibit qualitatively different interaction dynamics---the sub-exponential growth pattern suggests the severity gradient may plateau, but this remains unverified.
58	
59	
60	\paragraph{No throughput evaluation.}
61	We do not report inference throughput or latency, which are necessary for deployment analysis but orthogonal to our severity characterization.
62	
63	
64	
65	\section{Cross-Benchmark Validation: GSM8K}
66	\label{app:gsm8k}
67	
68	Tables~\ref{tab:gsm8k-ds} and \ref{tab:gsm8k-qw} report the per-phase II breakdown on GSM8K ($n{=}50$) for DeepSeek and Qwen, respectively. All statistics use medians, Wilcoxon signed-rank tests, and bootstrap median CIs ($B{=}10{,}000$), matching the MATH-500 methodology. DeepSeek importance-based eviction replicates the MATH-500 phase gradient across all four sparsity levels (all $p \leq 0.0003$) with a strict dose-response ($\Delta$: $0.24 \to 4.68$). Qwen importance-based eviction is significant at $s \geq 0.25$ ($p < 10^{-4}$). Random eviction is non-significant across all conditions for both models; Qwen random $s{=}0.30$ is excluded due to data quality concerns (output truncation producing extreme II values).
69	
70	\paragraph{Power analysis for random conditions.}
71	Post-hoc power analysis indicates that at $n{=}50$, the minimum detectable effect size is $d \geq 0.40$ ($\alpha{=}0.05$, power${=}0.80$). All 8 random conditions (2 models $\times$ 4 sparsity levels) show $|d| \leq 0.164$, well below the detectability threshold; their non-significance should therefore be interpreted as absence of evidence rather than evidence of absence. By contrast, Qwen importance-based eviction at $s \geq 0.25$ is adequately powered ($d \approx 0.63$, power ${>}\,0.99$), indicating that the observed significance reflects a genuine effect.
72	
73	\begin{table*}[t]
74	\centering
75	\small
76	\caption{Per-phase interaction index on GSM8K: DeepSeek-R1-Distill-Qwen-7B ($n{=}50$). $\Delta$: paired median difference ($\widetilde{\mathrm{II}}_{\textit{low}} - \widetilde{\mathrm{II}}_{\textit{high}}$) with bootstrap 95\% CI ($B{=}10{,}000$, median statistic). $p$: Wilcoxon signed-rank, Bonferroni-corrected ($k{=}4$).}
77	\label{tab:gsm8k-ds}
78	\begin{tabular}{@{}llcccc@{}}
79	\toprule
80	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
81	\midrule
82	0.15 & Importance & $-$0.001 & 0.241 & 0.24\; $[0.08,\; 0.48]$ & 0.0003 \\
83	0.15 & Random     & 0.036 & 0.105 & $-$0.04\textsuperscript{ns} & 0.90 \\
84	\addlinespace
85	0.20 & Importance & $-$0.002 & 0.740 & 0.74\; $[0.31,\; 1.12]$ & ${<}\,10^{-4}$ \\
86	0.20 & Random     & 0.143 & 0.423 & 0.28\textsuperscript{ns} & 0.96 \\
87	\addlinespace
88	0.25 & Importance & 0.009 & 1.992 & 1.99\; $[0.93,\; 2.82]$ & ${<}\,10^{-4}$ \\
89	0.25 & Random     & 0.619 & 1.603 & 0.98\textsuperscript{ns} & 0.83 \\
90	\addlinespace
91	0.30 & Importance & 0.024 & 4.682 & 4.68\; $[2.12,\; 10.56]$ & ${<}\,10^{-4}$ \\
92	0.30 & Random     & 1.837 & 4.683 & 2.85\textsuperscript{ns} & 0.54 \\
93	\bottomrule
94	\end{tabular}
95	\end{table*}
96	
97	\begin{table*}[t]
98	\centering
99	\small
100	\caption{Per-phase interaction index on GSM8K: Qwen2.5-7B-Instruct ($n{=}50$). Outputs truncated at \texttt{max\_new\_tokens}${=}$2047; absolute values should be interpreted with this limitation. $^{\ddagger}$Excluded: extreme II values from truncation artifacts render this condition invalid.}
101	\label{tab:gsm8k-qw}
102	\begin{tabular}{@{}llcccc@{}}
103	\toprule
104	$s$ & Strategy & $\widetilde{\mathrm{II}}_{\textit{high}}$ & $\widetilde{\mathrm{II}}_{\textit{low}}$ & $\Delta$\; [95\% CI] & $p_{\text{Bonf}}$ \\
105	\midrule
106	0.15 & Importance & 0.000 & 0.029 & 0.03\textsuperscript{ns} & 0.39 \\
107	0.15 & Random     & 0.089 & 0.033 & $-$1.58\textsuperscript{ns} & 0.69 \\
108	\addlinespace
109	0.20 & Importance & 0.004 & 0.180 & 0.09\textsuperscript{ns} & 0.62 \\
110	0.20 & Random     & 0.201 & 0.356 & 4.88\textsuperscript{ns} & 0.57 \\
111	\addlinespace
112	0.25 & Importance & 0.009 & 1.064 & 1.14\; $[0.62,\; 1.66]$ & ${<}\,10^{-4}$ \\
113	0.25 & Random     & 0.802 & 1.213 & 11.1\textsuperscript{ns} & 0.39 \\
114	\addlinespace
115	0.30 & Importance & 0.023 & 2.140 & 4.62\; $[2.88,\; 6.92]$ & ${<}\,10^{-4}$ \\
116	0.30 & Random$^{\ddagger}$     & \multicolumn{4}{c}{\textit{excluded (data quality)}} \\
117	\bottomrule
118	\end{tabular}
119	\end{table*}
120	
121	
122	\section{Downstream Accuracy Validation Details}
123	\label{app:accuracy-details}
124	
125	Table~\ref{tab:accuracy} reports MATH-500 accuracy under compound sparsity (importance-based eviction) at $s \in \{0.15, 0.20, 0.25, 0.30\}$ with \texttt{max\_new\_tokens}${=}$8192, complementing the PPL-based analysis in \S\ref{sec:accuracy-validation}. Qwen ($n{=}100$; truncation $\leq 4\%$ across all conditions) provides the cleanest dose-response evidence: accuracy declines gradually from $46\%$ (dense) through $s{=}0.25$ ($\delta{=}-4$ to $-13$\,pp) before a sharp cliff at $s{=}0.30$ ($19\%$, $\delta{=}-27$\,pp). DeepSeek ($n{=}50$) shows steeper overall degradation ($74\% \to 4\%$), confounded by rising truncation ($16\% \to 76\%$); non-truncated analysis (\S\ref{app:accuracy-nt}) reveals a dual-regime structure.
126	
127	\begin{table}[h]
128	\centering
129	\small
130	\caption{MATH-500 accuracy under compound sparsity (importance-based eviction, \texttt{max\_new\_tokens}${=}$8192). $\delta$: accuracy change vs.\ dense. Trunc: truncation rate under sparse condition. DS: $n{=}50$ (dense truncation $16\%$); QW: $n{=}100$ (truncation $\leq 4\%$ all conditions).}
131	\label{tab:accuracy}
132	\begin{tabular}{@{}lccccc@{}}
133	\toprule
134	Model & $s$ & Dense & Sparse & $\delta$ & Trunc \\
135	\midrule
136	DS & 0.15 & 74\% & 48\% & $-$26\,pp & 32\% \\
137	DS & 0.20 & 74\% & 30\% & $-$44\,pp & 56\% \\
138	DS & 0.25 & 74\% & 8\% & $-$66\,pp & 76\% \\
139	DS & 0.30 & 74\% & 4\% & $-$70\,pp & 76\% \\
140	\addlinespace
141	QW & 0.15 & 46\% & 42\% & $-$4\,pp & $\leq$4\% \\
142	QW & 0.20 & 46\% & 36\% & $-$10\,pp & $\leq$4\% \\
143	QW & 0.25 & 46\% & 33\% & $-$13\,pp & $\leq$4\% \\
144	QW & 0.30 & 46\% & 19\% & $-$27\,pp & $\leq$4\% \\
145	\bottomrule
146	\end{tabular}
147	\end{table}
148	
149	\paragraph{Failure mode divergence.}
150	DeepSeek and Qwen exhibit qualitatively distinct failure modes under compound sparsity. DeepSeek failures are \emph{truncation-dominated}: compound sparsity is associated with verbose, repetitive chain-of-thought that exceeds the token limit (truncation rises from $16\%$ at dense to $32\%$ at $s{=}0.15$ and $76\%$ at $s{=}0.30$, even with \texttt{max\_new\_tokens}${=}$8192). Qwen failures are \emph{wrong-answer-dominated}: outputs complete within the token limit (truncation $\leq 4\%$) but produce incorrect answers, indicating that compound sparsity disrupts reasoning quality directly. This divergence likely reflects training-paradigm differences: DeepSeek's distillation from DeepSeek-R1 produces extended CoT traces susceptible to truncation under degraded conditions.
151	
152	\paragraph{Language switching under high sparsity.}
153	DeepSeek problems exhibit language switching to Chinese mid-generation at the following observed rates: 0\% at dense, 4\% at $s{=}0.15$, and 40\% at $s{=}0.30$ (intermediate sparsity levels not yet measured).\footnote{Language switching rates were detected from \texttt{gen\_snippet} fields in 2048-token evaluations, not from the independent 8192-token generations used in Table~\ref{tab:accuracy}. Rates under the 8192-token budget were not re-measured.} This qualitative pathology---absent in Qwen---is a \emph{symptom} of compound-sparsity-induced degradation rather than a cause of accuracy loss: at $s{=}0.30$, Chinese-language and English-language outputs achieve comparable accuracy ($\sim$10\%), indicating that the accuracy decline reflects pruning-induced reasoning corruption regardless of output language. The switching pattern is consistent with the model's Chinese-language pretraining corpus surfacing under degraded attention in distillation-trained models.
154	
155	
156	\section{Non-Truncated Sensitivity Analysis}
157	\label{app:accuracy-nt}
158	
159	With \texttt{max\_new\_tokens}${=}$8192, Qwen truncation remains $\leq 4\%$ across all sparsity levels, so the full-sample accuracy decline ($\delta{=}-4$ to $-27$\,pp; Table~\ref{tab:accuracy}) reflects pure reasoning quality degradation without truncation confound.
160	
161	DeepSeek exhibits substantial truncation ($16\%$ at dense to $76\%$ at $s{=}0.25$--$0.30$). Restricting to non-truncated outputs reveals a \emph{dual-regime} structure. At $s \leq 0.20$, non-truncated accuracy remains $68$--$71\%$ (vs.\ $88\%$ dense; $n_{\text{NT}}{=}34$ at $s{=}0.15$, $n_{\text{NT}}{=}22$ at $s{=}0.20$), while full-sample accuracy drops to $30$--$48\%$---indicating that degradation at low sparsity is primarily truncation-driven rather than reflecting reasoning quality loss. At $s \geq 0.25$, non-truncated accuracy itself collapses: $33\%$ at $s{=}0.25$ and $17\%$ at $s{=}0.30$ ($n_{\text{NT}}{=}12$ for both; reported as reference values given small samples), showing that high-dose compound sparsity degrades both generation length \emph{and} reasoning quality simultaneously. The NT accuracy cliff from $68\%$ ($s{=}0.20$) to $33\%$ ($s{=}0.25$) localizes the transition between truncation-driven and dual-collapse regimes.
162	
163	This dual-regime structure complements the importance discrimination collapse analysis (\S\ref{sec:analysis}): at low sparsity, compound interaction primarily manifests as increased verbosity (degraded attention produces repetitive CoT); at high sparsity, the interaction additionally corrupts reasoning-critical computations.
164	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4a11ed00-2916-45c1-853c-fc90dba5c557",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "65eacfdd-bc85-40b1-8296-48b727bf1f29",
  "sourceToolAssistantUUID": "4a11ed00-2916-45c1-853c-fc90dba5c557",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 37 · 2026-05-16T08:15:46.385Z_

Now I have a thorough understanding of the paper. Let me also check the planned experiments vs what's actually in the paper.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "65eacfdd-bc85-40b1-8296-48b727bf1f29",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v4FNTJekS7F9ZuVkvM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "54be3ab6-0b8d-4c41-99d7-30bf83bb88cb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCR6CJcEJrhQQSnSxXT54t",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6178,
      "cache_read_input_tokens": 60220,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 6178,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 1,
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

_source line 38 · 2026-05-16T08:15:48.458Z_

<details open><summary>🔧 Tool call — Read · `toolu_01S1WNVkeMZobdwmgX2uEW6N`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54be3ab6-0b8d-4c41-99d7-30bf83bb88cb",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v4FNTJekS7F9ZuVkvM",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1652dda6-3874-4a0a-89a7-27710a1e9c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCR6CJcEJrhQQSnSxXT54t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6178,
      "cache_read_input_tokens": 60220,
      "output_tokens": 119,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 6178
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 119,
          "cache_read_input_tokens": 60220,
          "cache_creation_input_tokens": 6178,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 6178,
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

_source line 39 · 2026-05-16T08:15:48.484Z_

<details><summary>↩ Tool result · `toolu_01S1WNVkeMZobdwmgX2uEW6N`</summary>

```text
1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Long-context language models place acute pressure on the key--value (KV) cache, which grows linearly with sequence length \cite{kwon-sosp2023, pope-mlsys2023}.
5	Two complementary responses---\emph{attention head pruning} \cite{voita-acl2019, michel-neurips2019} and \emph{KV cache eviction} \cite{snapkv-neurips2024, adakv-neurips2025}---are increasingly deployed simultaneously as \emph{compound sparsity}, but the resulting quality degradation is often super-additive \cite{spark-aaai2026, slim-icml2025}. Recent evaluations show that reasoning capabilities degrade disproportionately under compound compression \cite{unicomp-2026}, and that per-dimension safe zones intersect to form a smaller joint safe region \cite{phase-transition-compression-2026}.
6	
7	Prior work treats compound interaction magnitude as roughly constant across generation \cite{spark-aaai2026, unicomp-2026}, despite evidence that pruning sensitivity depends on representational phase \cite{decision-repr-transition-2026} and that no single sparse attention strategy dominates across generation stages \cite{sparse-frontier-2025}.
8	This assumption is problematic for reasoning models, whose chain-of-thought generations \cite{wei-neurips2022-cot} alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) \cite{thinkv-iclr2026}.
9	Phase-aware methods like ThinKV \cite{thinkv-iclr2026} apply different KV strategies per phase but without considering compound interaction, while importance-based eviction itself faces challenges from score collapse \cite{hies-2025}, greedy bias \cite{greedy-bias-kvcache-2026}, and temporal dynamics \cite{lethe-aaai2026}. These methods each optimize a single pruning axis; we characterize the interaction when multiple axes are composed.
10	If compound severity varies across these phases, a uniform sparsity budget may be safe in one phase yet destructive in another.
11	
12	We find that compound sparsity severity is an emergent property of the three-way interaction among eviction strategy, reasoning phase, and sparsity level.
13	Under importance-based KV cache eviction, the Interaction Index---a measure of super-additive degradation---concentrates in low-sparsity reasoning phases and is largely absent in high-sparsity phases.
14	On DeepSeek-R1-Distill-Qwen-7B (MATH-500), the paired median difference rises from $0.39$ at $s{=}0.15$ to $8.48$ at $s{=}0.30$ (Spearman $\rho{=}1.0$; all Bonferroni-corrected $p < 0.005$).
15	The pattern replicates on Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; all $p < 0.005$), with preliminary cross-architecture evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM, $n{=}49$), where the phase gradient direction is consistent but strategy${\times}$phase interaction is weaker than on Qwen2-architecture models.
16	Random eviction develops a detectable phase gradient only above $s \approx 0.20$, at $2.7$--$17{\times}$ smaller magnitude than importance-based (where both strategies reach significance at $s \geq 0.25$), supporting that the dominant gradient is strategy-specific.
17	Cross-benchmark validation on GSM8K reveals consistent phase gradient direction: DeepSeek replicates the monotonic dose-response ($\Delta$: $0.24 \to 4.68$; all $p \leq 0.0003$), while Qwen shows directional consistency at $s \geq 0.25$ but is inconclusive due to generation truncation (\S\ref{sec:cross-benchmark}). Strategy specificity attenuates on GSM8K relative to MATH-500, indicating that phase modulation generalizes but its magnitude is task-dependent.
18	
19	Per-phase Gini analysis identifies \emph{importance discrimination collapse}---the degeneration of head importance scores toward uniformity under compound stress---as a correlational diagnostic of this phase--strategy divergence. Both strategies exhibit consistent Gini drops across all tested conditions, yet severity diverges by $2.7$--$17{\times}$, implicating the structural specificity of importance-based pruning as the key differentiator.
20	
21	Beyond individual findings, we contribute a \emph{phase-gated analysis framework} that decomposes compound severity by reasoning phase and eviction strategy, transforming a scalar interaction metric into a structured diagnostic. This framework---combining the Interaction Index with attention-sparsity-based phase segmentation---reveals structure in compound degradation that aggregate metrics miss, and provides practitioners with a principled basis for phase-aware sparsity allocation.
22	
23	Our contributions:
24	\begin{enumerate}[nosep,leftmargin=*]
25	    \item We characterize a \textbf{phase-modulated compound severity gradient}: importance-based eviction exhibits a monotonic dose-response ($\rho{=}1.0$; $\Delta$: $0.39 \to 8.48$) with a phase gradient $2.7$--$17{\times}$ larger than random eviction where both strategies are significant ($s \geq 0.25$) on MATH-500; the gradient direction is consistent on GSM8K, while strategy specificity attenuates (\S\ref{sec:cross-benchmark}).
26	    \item We replicate the pattern \textbf{across models and architectures}: Qwen2.5-7B-Instruct ($\Delta$: $0.07 \to 3.16$; $\rho{=}1.0$) and DeepSeek-R1-Distill-Llama-8B ($n{=}49$; consistent direction, weaker strategy${\times}$phase contrast; \S\ref{sec:cross-arch}).
27	    \item We identify \textbf{importance discrimination collapse} via per-phase Gini analysis as a correlational diagnostic: consistent collapse across models and strategies, with the structural specificity of importance-based pruning corresponding to the severity divergence (\S\ref{sec:analysis}).
28	    \item We validate the phase gradient on \textbf{GSM8K} for both models, finding that phase modulation is benchmark-robust while strategy specificity is task-dependent (\S\ref{sec:cross-benchmark}).
29	\end{enumerate}
30	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1652dda6-3874-4a0a-89a7-27710a1e9c04",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "d75662ff-8bf4-4308-97a7-1baeed0cfbc4",
  "sourceToolAssistantUUID": "1652dda6-3874-4a0a-89a7-27710a1e9c04",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-16T08:15:52.467Z_

Now I have enough information to provide a thorough review. Let me also check the paper summary section the reviewer context mentioned about the GPQA and 14B experiments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d75662ff-8bf4-4308-97a7-1baeed0cfbc4",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v4fF9HHuneqHapQF4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "be8404d3-9191-4bf2-9953-d0a818dfef8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASZFGrSfeKYeQRpFWikzQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1787,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
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

_source line 41 · 2026-05-16T08:15:53.639Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0171zpgBHZJ3LsnAvyy5CMNV`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "be8404d3-9191-4bf2-9953-d0a818dfef8f",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v4fF9HHuneqHapQF4r",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b549a5fc-dbbd-40d2-9749-042946bf97d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ASZFGrSfeKYeQRpFWikzQT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1787,
      "cache_read_input_tokens": 66398,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1787,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 4,
      "service_tier": "standard",
      "inference_geo": "not_available"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-16T08:15:53.642Z_

<details><summary>↩ Tool result · `toolu_0171zpgBHZJ3LsnAvyy5CMNV`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b549a5fc-dbbd-40d2-9749-042946bf97d0",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "eb03e985-eb21-460f-a492-3d58ec66f779",
  "sourceToolAssistantUUID": "b549a5fc-dbbd-40d2-9749-042946bf97d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-16T08:15:57.016Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018WW5rAUbZF4a5qfAbqxnca`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_post_to_reviewer",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "eb03e985-eb21-460f-a492-3d58ec66f779",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v53fHAyg8Au1sHuavd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1325825d-50a4-4cda-8b17-b699373a2bf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016gnpzU5LdQ2sXguy7rWNce",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 805,
      "cache_read_input_tokens": 68185,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 805
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 90,
          "cache_read_input_tokens": 68185,
          "cache_creation_input_tokens": 805,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 805,
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

_source line 44 · 2026-05-16T08:15:57.019Z_

<details><summary>↩ Tool result · `toolu_018WW5rAUbZF4a5qfAbqxnca`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__director_post_to_reviewer"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1325825d-50a4-4cda-8b17-b699373a2bf5",
  "isSidechain": true,
  "promptId": "564787ae-5995-4a3f-9f03-eff16b60d7c4",
  "agentId": "ac47f85168ca4027f",
  "type": "user",
  "uuid": "14f46089-bc78-4bff-b823-cc2d26e97f19",
  "sourceToolAssistantUUID": "1325825d-50a4-4cda-8b17-b699373a2bf5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-16T08:17:04.740Z_


Based on my thorough reading of the paper content, provenance tracking, roadmap, and experimental artifacts, here is my review:

---

## Review: "Phase-Dependent Compound Sparsity: Strategy-Phase Interactions Modulate Severity in Efficient LLM Inference"

### Summary of Contributions

The paper introduces a phase-gated analysis framework for compound sparsity (simultaneous head pruning + KV cache eviction) and demonstrates that the resulting super-additive interaction is not constant but depends on eviction strategy, reasoning phase, and sparsity level. The primary finding is that importance-based eviction concentrates severity in low-sparsity (broadly-distributed-attention) phases with a monotonic dose-response, while random eviction shows a much weaker or absent phase gradient. A correlational mechanism (importance discrimination collapse) is proposed.

### Strengths

- **Well-defined metric**: The Interaction Index (II) is cleanly formulated with both additive and multiplicative null baselines, and the choice of additive null as more conservative is well-justified. The paired median difference as primary metric (rather than ratio-based G) is a sound choice given the heavy-tailed distributions.

- **Strong statistical methodology on the primary claim**: Bootstrap CIs (B=10,000), Wilcoxon signed-rank with Bonferroni correction, Jonckheere-Terpstra dose-response test, permutation tests, and BH-FDR as robustness check. The statistical apparatus is thorough and appropriately non-parametric given the skewed distributions.

- **Comprehensive robustness checks**: Sensitivity to phase segmentation (tercile/quartile/quintile), minimum phase length (5/10/20), asymmetric sparsity allocation, outlier winsorization, and multiplicative vs. additive null. These address many obvious confounds preemptively.

- **Large primary sample size**: n=496/475 for the main MATH-500 claims provides genuine statistical power, and the paper shows the narrowing of CIs from n=50 to n=500.

- **Honest reporting**: The paper acknowledges that the discrimination collapse mechanism is correlational, that entropy redistribution only partially replicates, that LLaMA evidence is inconclusive, and that the pilot mitigation failed its pre-registered gate. This intellectual honesty is commendable.

- **Phase segmentation validation**: The kappa=0.88 agreement with DeepSeek's explicit `&lt;think>` markers (albeit on GSM8K n=48) provides meaningful external validation.

### Weaknesses

**W1. Incomplete planned experiments presented as placeholders.** Tables 5 (14B), 6 (GPQA Diamond) in the paper summary correspond to placeholder tables in the actual LaTeX (Tables `tab:scale-14b` and `tab:gpqa-results` with "---" entries and "Results pending" captions). The paper as submitted contains incomplete sections. The ROADMAP confirms these experiments are still running or planned. A submission with placeholder data tables is unacceptable.

**W2. The two primary models share the same architecture.** DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct both use Qwen2ForCausalLM (28 layers, 28 heads, 4-group GQA). The "cross-model replication" is really a cross-training-paradigm comparison within one architecture family. The LLaMA-8B results (n=49) are underpowered for strategy comparisons (power 0.26-0.63) and show a ~40x smaller effect. The paper acknowledges this but the abstract and contributions list it as if it were a strength ("replicates across models and architectures"), which oversells.

**W3. Circular confound in the importance-based eviction design.** The paper itself acknowledges (Limitations) that importance scores are computed from the same attention distribution that head pruning alters. This is not merely a limitation—it is arguably the primary mechanism driving the observed phenomenon. The "compound interaction" may largely be a measurement artifact: pruning heads degrades the importance scores used for eviction, which is a deterministic consequence of the scoring method rather than an emergent property of compound sparsity per se. The paper does not test any eviction method whose scoring is independent of head pruning (e.g., recency-based, learned policies), which would be necessary to disentangle the confound from the phenomenon.

**W4. GSM8K results are weak and partially invalidated.** On GSM8K (n=50): Qwen importance is significant only at s>=0.25, Qwen random is excluded for data quality, and all random conditions are non-significant but underpowered. The Qwen GSM8K data is explicitly marked as "unreliable" due to truncation at max_new_tokens=2047. Yet the paper claims "cross-benchmark validation" as a contribution (Contribution 4). The actual evidence for cross-benchmark generalization is thin—only DeepSeek importance on GSM8K cleanly replicates, and the strategy specificity ratio cannot be meaningfully computed.

**W5. The "phase" construct may be tautological.** Low-sparsity phases are defined as phases where attention is broadly distributed. Importance-based eviction degrades most when attention is broadly distributed (because more positions have similar scores, making eviction error-prone). The finding that importance-based eviction severity concentrates in low-sparsity phases may be a direct consequence of the phase definition rather than a non-obvious empirical finding. The paper does not adequately address whether this is an interesting discovery or a definitional consequence.

**W6. No comparison to existing compound sparsity methods.** The paper does not compare against any existing joint pruning approach (e.g., GRASPrune, which is cited but not compared against). It only evaluates a basic head-pruning + KV-eviction pipeline. The practical relevance of characterizing severity in a naive compound setup is unclear when learned joint methods exist.

**W7. Practical impact is null.** The pilot mitigation experiment (Section 6, Appendix D) achieved 18% oracle recovery with CI spanning zero, failing its pre-registered gate. The paper establishes a characterization but provides no actionable method for practitioners. The contribution is purely descriptive.

**W8. Discrimination collapse does not explain the effect magnitude.** The paper notes that both strategies show "near-identical Gini drops (<10% difference)" yet severity diverges 15-17x. The proposed mechanism (importance discrimination collapse) explicitly cannot explain the core finding. The "structural specificity" explanation (importance pruning removes low-Gini heads) is post-hoc and not causally tested.

### Questions for Authors

**Q1.** Have you tested any eviction strategy whose scoring is independent of the pruned attention distribution (e.g., recency-based, position-based, or learned eviction)? If importance-based eviction's severity gradient disappears under such methods, the finding would be about scoring-method fragility rather than compound sparsity per se.

**Q2.** The phase segmentation is computed on the dense model's attention patterns. What happens if phases are defined on the *pruned* model's attention patterns? Would the phase boundaries shift, and would II still show the same gradient?

**Q3.** Given that the Qwen2.5-14B and GPQA Diamond experiments are marked "Results pending" in the paper, what is the status of these experiments? Are they included in the submission or are these placeholder sections?

**Q4.** Why were only 30 problems used for the discrimination collapse analysis (Gini/CV) rather than the full n=500 sample?

**Q5.** The effect magnitude differs ~5x between DeepSeek and Qwen despite identical architecture. You attribute this to "training paradigm." Can you provide more mechanistic insight? Is it simply that DeepSeek produces longer, more structured CoT (hence more extreme phase variation)?

**Q6.** Random eviction on GSM8K shows large absolute Delta values (e.g., 2.85 at s=0.30) that are non-significant. The CIs must be extremely wide. What is driving this variance?

### Minor Issues

- Table 5 in the paper summary describes LLaMA n=250 results, but the actual paper (Section 5.5) reports only n=49. The ROADMAP shows c8_llama_n250_fixed is still running. Discrepancy between summary and submitted content.
- The paper summary mentions "Task-modulated strategy specificity: imp/random ratio is 15x on MATH-500, 2.3-3.8x on GSM8K" but the actual paper cannot compute this ratio on GSM8K because random is non-significant there.
- Spearman rho=1.0 on 4 data points (the monotonicity claim) has limited informational content. The JT test is the appropriate test and is reported, but the rho=1.0 appears prominently despite being trivial with n=4.
- The footnote about float16 -> bfloat16 switch suggests the experimental pipeline was unstable. Were any results from the float16 era carried forward?
- Cohen's dz is reported as "0.61 to 1.13" in one place but "0.77 to 0.94" (robust dz) in another for what appears to be the same experiment. The relationship between these should be clarified.

### Preliminary Score: 3 (Weak Reject)

### Confidence: 4/5

**Rationale**: The statistical methodology is strong and the paper is honest about its limitations. However, the circular confound (W3) undermines the novelty of the core finding—it may be largely a consequence of using attention-mass-based scoring that is degraded by the very pruning it depends on. The incomplete experiments (W1), limited architectural diversity (W2), weak cross-benchmark evidence (W4), and null practical contribution (W7) compound this concern. The paper characterizes an effect that may be specific to a particular (naive) compound sparsity implementation on one architecture family, with no demonstrated path to practical utility. For a top venue with ~25% acceptance, the contribution feels incremental: it is a careful measurement paper about a potentially tautological phenomenon (W5) with no mechanism that explains the effect magnitude (W8) and no actionable output (W7).

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "14f46089-bc78-4bff-b823-cc2d26e97f19",
  "isSidechain": true,
  "agentId": "ac47f85168ca4027f",
  "requestId": "req_011Cb5v5Hr4ZysUcaaujARke",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8974862b-c191-4d71-a34c-31772be9a5ed",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse",
  "sessionId": "da179c64-682b-4476-8ead-731d6820bfd5",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DAuupk8T7oaYWVa9nmVHLF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 500,
      "cache_read_input_tokens": 68990,
      "output_tokens": 2412,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 500
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2412,
          "cache_read_input_tokens": 68990,
          "cache_creation_input_tokens": 500,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 500,
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
