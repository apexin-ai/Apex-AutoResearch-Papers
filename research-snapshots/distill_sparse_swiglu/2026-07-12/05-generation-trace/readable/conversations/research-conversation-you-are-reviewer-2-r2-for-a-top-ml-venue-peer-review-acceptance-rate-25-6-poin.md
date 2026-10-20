# Research conversation: You are **Reviewer 2 (R2)** for a top ML venue peer review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reje

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 51
- **Recorded user turns:** 1
- **Tool calls:** 21
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ac9516e874bee4160.jsonl`
- **Structured JSON:** [`4e60fd3aef58cfe6d88c.json`](../../sessions/4e/4e60fd3aef58cfe6d88c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

51 recorded events

### User

_source line 1 · 2026-05-18T18:38:42.676Z_

You are **Reviewer 2 (R2)** for a top ML venue peer review (acceptance rate ~25%, 6-point scale: 1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Your focus: **Novelty, Positioning, Related Work, and Writing Quality**.

## Paper Summary

**Title**: "What Does KL Distillation Learn for SwiGLU Sparsity Prediction? Mask Pattern Discovery, Causal Decomposition, and Sparsity Regime Analysis"

The paper trains per-token contextual sparsity predictors using KL-divergence distillation for SwiGLU-based LLMs and investigates what KL learns that BCE does not. Four claimed contributions:
1. **Mask pattern discovery**: KL-trained predictors discover neuron importance patterns diverging 53% from magnitude-based masks. Three-seed causal ablation shows mask quality (not gradient coupling) is the primary driver, explaining 82–100%.
2. **Automated oracle discovery**: At 30% sparsity, BCE with magnitude oracles nearly matches KL (PPL 9.15 vs 8.82, Δ=0.33). KL's value is automated oracle discovery.
3. **Sparsity regime characterization**: 6-point sweep (25–50%) reveals continuous quality-sparsity tradeoff with PPL cliff at 40–45% and MMLU cliff at 35–40%.
4. **Conceptual contributions**: Formal loss taxonomy (2D: correction granularity × training signal coupling) and gradient SNR analysis (103× higher for KL).

## Related Work Section (verbatim)

**Training-free activation sparsity.** Several methods exploit the natural sparsity of SwiGLU activations without any training. WINA selects neurons based on weight norms. TEAL uses a combination of activation magnitude and weight importance scores, achieving a good tradeoff between simplicity and quality. R-Sparse extends this with running statistics. These methods require zero training cost but leave a quality gap that grows with sparsity level, motivating learned approaches.

**Learned sparsity predictors.** FastForward trains a small MLP predictor per FFN layer using BCE loss against magnitude-based binary masks, combined with a compensation MLP that corrects residual errors from imperfect mask prediction. ShadowLLM uses MSE loss at the per-layer level. Both treat the sparsity predictor as a binary classification problem and rely on post-hoc compensation to close the gap from mask imperfections.

**KL distillation for sparse inference.** SPON trains a static bias correction term using KL-divergence distillation from the dense model. The correction is input-independent, limiting its expressiveness. Our work extends KL distillation to per-token contextual predictors, filling a gap in the design space where coupled training signals meet fine-grained, input-adaptive predictions.

**Sparsity analysis and regime characterization.** Prior work on structured pruning has studied accuracy-sparsity tradeoffs, but the interaction between sparsity level, allocation strategy (uniform vs. global), and metric type (perplexity vs. downstream) in the context of activation sparsity for SwiGLU has not been systematically characterized. Our six-point regime analysis contributes to this understanding.

## Method Section Summary

- **Loss taxonomy** (Table 1): 2D grid with axes (correction granularity: static/per-layer/per-token) × (training signal coupling: decomposed BCE / intermediate MSE / coupled KL). Paper fills the "per-token × coupled KL" cell.
- **Gradient SNR**: Claims KL gradient SNR is ~103× higher than BCE due to output coupling term in chain rule. No formal derivation or empirical measurement shown — stated as a fact.
- **Training**: Lagrangian formulation with dual gradient ascent for sparsity constraint. Gumbel-sigmoid relaxation. Top-k at inference. Separate predictor per FFN layer.

## Key Results

- At 30% sparsity, BCE nearly matches KL (PPL 9.15 vs 8.82). The paper itself frames this as undermining KL's practical advantage.
- Causal ablation: 3-seed mean Δ=0.48 (std=0.36), gradient coupling = 0–18% depending on seed.
- 6-point regime sweep has 3 PPL monotonicity violations, no clean phase transitions.
- Cross-architecture (Mistral) and cross-scale (Qwen-14B) experiments are mentioned in setup but NO results are shown.
- LongBench: KL 30% retains 61% of dense (which itself is only 23.0).
- MT-Bench (Appendix): near-useless due to base model floor effect.

## Writing Observations

- The paper is 7 pages of main content + 2 pages of appendices (9 total).
- No figures in the paper — only tables.
- Many table entries are dashes (missing data), especially Table 2 (BCE+comp has all dashes), Table 6 (most category scores missing).
- The paper uses em-dashes in multiple places and some "-ing" participial constructions.
- Abstract is ~180 words, reasonably concise.
- No references/bibliography section is visible in the PDF (the paper appears to not include actual citation entries, only inline mentions of method names like "TEAL", "FastForward", "SPON", "ShadowLLM", "WINA", "R-Sparse").

## Your Review Task

Evaluate **novelty**, **positioning relative to prior work**, **writing quality**, and **presentation**. Address:

1. **Novelty assessment**: The paper fills one cell in its own taxonomy (per-token × KL). Is this technically novel? How incremental is it vs SPON (static × KL) and FastForward (per-token × BCE)? The key finding is that KL's advantage at 30% sparsity is only Δ=0.33 PPL — does this undermine the paper's own contribution?
2. **Related work coverage**: Is the coverage adequate for a top venue? Are there important missing references (e.g., MoEfication, Deja Vu, PowerInfer, other activation sparsity works)? Is positioning honest?
3. **Claim-evidence alignment**: For each of the 4 contributions, does the evidence support the claim? Are any claims overclaimed or underclaimed?
4. **Writing quality**: Check for AI writing patterns (em-dashes, -ing phrases, excessive transitions). Is the narrative coherent or does it read like an experiment report? Does the paper tell a compelling story?
5. **Presentation**: The paper has ZERO figures. Is this a problem? How are the many table dashes perceived? Is information density appropriate for a top venue?
6. **Bibliography**: The paper mentions method names but has no visible reference list. How serious is this?

Produce a structured review with:
- **Summary** (2-3 sentences)
- **Strengths** (bulleted)
- **Weaknesses** (bulleted, with severity: major/minor)
- **Questions for Authors**
- **Novelty Assessment** (explicit judgment on incrementality)
- **Score** (1-6) with **Confidence** (1-5)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "04437633-e2e6-4b43-9356-ba33b9946ca1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-18T18:38:42.680Z_

```json
{
  "parentUuid": "04437633-e2e6-4b43-9356-ba33b9946ca1",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
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
  "uuid": "d79a4e85-855f-4e6b-a119-d9863dc2161d",
  "timestamp": "2026-05-18T18:38:42.680Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

---

### Assistant

_source line 3 · 2026-05-18T18:38:45.915Z_



I'll conduct a thorough review by first reading the actual paper and supporting materials to ground my assessment.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d79a4e85-855f-4e6b-a119-d9863dc2161d",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXBW8VnDmN3Qsr94afm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ebdcd1e5-004a-4495-98fb-d39c7732b4d0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188zdTM9MemCrpWALpJu6Gt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9211,
      "cache_read_input_tokens": 8802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9211,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 4 · 2026-05-18T18:38:46.847Z_

<details open><summary>🔧 Tool call — Glob · `toolu_0161tQbQZcJC6xGhmxw3sjC1`</summary>

```json
{
  "pattern": "paper/**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ebdcd1e5-004a-4495-98fb-d39c7732b4d0",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXBW8VnDmN3Qsr94afm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45648b95-49b9-40b4-8cb4-40a32d562cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188zdTM9MemCrpWALpJu6Gt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9211,
      "cache_read_input_tokens": 8802,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 9211,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 6,
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

_source line 5 · 2026-05-18T18:38:46.879Z_

<details><summary>↩ Tool result · `toolu_0161tQbQZcJC6xGhmxw3sjC1`</summary>

```text
paper/main.tex
paper/ethics.tex
paper/related_work.tex
paper/conclusion.tex
paper/method.tex
paper/appendix.tex
paper/limitations.tex
paper/introduction.tex
paper/experiments.tex
paper/abstract.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45648b95-49b9-40b4-8cb4-40a32d562cdc",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "1cc3742d-6274-496f-a0c7-4ba7cd141780",
  "sourceToolAssistantUUID": "45648b95-49b9-40b4-8cb4-40a32d562cdc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 6 · 2026-05-18T18:38:47.556Z_

<details open><summary>🔧 Tool call — Glob · `toolu_013B5FWGAbYMg427tZFTWa1v`</summary>

```json
{
  "pattern": "paper/**/*.bib",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1cc3742d-6274-496f-a0c7-4ba7cd141780",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXBW8VnDmN3Qsr94afm",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "af12312d-f637-4171-88ca-a4c28c84f0c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0188zdTM9MemCrpWALpJu6Gt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9211,
      "cache_read_input_tokens": 8802,
      "output_tokens": 209,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 9211
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 209,
          "cache_read_input_tokens": 8802,
          "cache_creation_input_tokens": 9211,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 9211,
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

_source line 7 · 2026-05-18T18:38:47.582Z_

<details><summary>↩ Tool result · `toolu_013B5FWGAbYMg427tZFTWa1v`</summary>

```text
paper/references.bib
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "af12312d-f637-4171-88ca-a4c28c84f0c4",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "11ae4dfb-55dc-443c-aabe-4f2cb0812c9d",
  "sourceToolAssistantUUID": "af12312d-f637-4171-88ca-a4c28c84f0c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 8 · 2026-05-18T18:38:50.278Z_

<details open><summary>🔧 Tool call — Read · `toolu_018sMUraqu8w2gpSAEswxiYM`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "11ae4dfb-55dc-443c-aabe-4f2cb0812c9d",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXBsAHhFY2vf4MNbMKe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "45a70acd-6c7b-4005-98a2-b6eb4b6c4037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111YU4r4rHQ6nDBo7enFtnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 18013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1177,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 9 · 2026-05-18T18:38:50.289Z_

<details><summary>↩ Tool result · `toolu_018sMUraqu8w2gpSAEswxiYM`</summary>

```text
1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	\usepackage{times}
4	\usepackage{latexsym}
5	\usepackage[T1]{fontenc}
6	\usepackage[utf8]{inputenc}
7	\usepackage{microtype}
8	% \usepackage{inconsolata} % not available on this system
9	\usepackage{graphicx}
10	\graphicspath{{../figures/paper/}}
11	\usepackage{amsmath}
12	\usepackage{amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{enumitem}
16	
17	\title{Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs}
18	
19	\author{Anonymous}
20	
21	\begin{document}
22	\maketitle
23	
24	\begin{abstract}
25	\input{abstract}
26	\end{abstract}
27	
28	\input{introduction}
29	\input{related_work}
30	\input{method}
31	\input{experiments}
32	\input{conclusion}
33	\input{limitations}
34	\input{ethics}
35	
36	\bibliography{references}
37	
38	\input{appendix}
39	
40	\end{document}
41	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "45a70acd-6c7b-4005-98a2-b6eb4b6c4037",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "9c292fd4-3d33-47ef-a297-0775c1cd9037",
  "sourceToolAssistantUUID": "45a70acd-6c7b-4005-98a2-b6eb4b6c4037",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-18T18:38:50.749Z_

<details open><summary>🔧 Tool call — Read · `toolu_01BMrDNMkcRLgYPuF1PFXDWa`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c292fd4-3d33-47ef-a297-0775c1cd9037",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXBsAHhFY2vf4MNbMKe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b75b2843-fe71-4e39-b3a5-9f4155506ade",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111YU4r4rHQ6nDBo7enFtnR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 18013,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1177,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 72,
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

_source line 11 · 2026-05-18T18:38:50.757Z_

<details><summary>↩ Tool result · `toolu_01BMrDNMkcRLgYPuF1PFXDWa`</summary>

```text
1	We show that KL-trained sparsity predictors for SwiGLU LLMs discover neuron importance patterns that diverge 53\% from magnitude-based masks (per-layer Jaccard 47\%).
2	A causal ablation confirms that these mask patterns, not gradient coupling, drive quality: under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all four downstream tasks (max $\Delta$=0.79pp), while magnitude-trained BCE achieves 28.13$\pm$0.20.
3	The resulting predictor ($<$1\% of base parameters), trained with forward KL and Gumbel-Sigmoid relaxation on LLaMA-3.1-8B, renders post-hoc compensation (+67.2M params) redundant at both 30\% and 50\% sparsity.
4	At 30\%, KL reduces PPL degradation 18\% over TEAL; uniform allocation provides $7.5\times$ smaller cross-seed downstream $\sigma$.
5	At 50\%, the PPL advantage widens to 49\% but downstream tasks collapse to near-random regardless of allocation.
6	Evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B confirms the PPL advantage across 7--14B, though at 14B, MMLU falls 8pp below TEAL (63.7\% vs.\ 71.8\%), a scale-dependent gap not resolved by allocation strategy.
7	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b75b2843-fe71-4e39-b3a5-9f4155506ade",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "264dcda1-e8de-4c05-930c-280b1b4d369c",
  "sourceToolAssistantUUID": "b75b2843-fe71-4e39-b3a5-9f4155506ade",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-18T18:38:51.046Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AwUUXF3CJscaRkM4NzLLyi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "264dcda1-e8de-4c05-930c-280b1b4d369c",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXBsAHhFY2vf4MNbMKe",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0e6e4a5b-8da6-41da-af64-a97d56f5049a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0111YU4r4rHQ6nDBo7enFtnR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 18013,
      "output_tokens": 230,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1177
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 230,
          "cache_read_input_tokens": 18013,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1177,
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

_source line 13 · 2026-05-18T18:38:51.052Z_

<details><summary>↩ Tool result · `toolu_01AwUUXF3CJscaRkM4NzLLyi`</summary>

```text
1	\section{Introduction}
2	
3	SwiGLU feed-forward networks~\cite{shazeer2020glu} in modern LLMs exhibit high contextual sparsity: at any given token, a large fraction of FFN neurons contribute negligibly to the output.
4	Learned sparsity predictors~\cite{liu2023dejavu,gautam2026fastforward} exploit this property by training small networks to anticipate which neurons are important, but they universally rely on binary cross-entropy (BCE) loss, treating each neuron as an independent classification target.
5	Yet at inference, sparsity budgets are allocated globally: TEAL's top-$k$ mechanism~\cite{liu2025teal} ranks all neurons across all layers and retains only those above a model-wide threshold.
6	This mismatch between per-neuron training and global inference allocation has not been formally analyzed.
7	
8	Gradient analysis reveals a structural asymmetry: BCE's gradient $\partial \mathcal{L}_{\text{BCE}} / \partial s_j = \sigma(s_j) - m_j^*$ depends only on neuron $j$, while under KL divergence, the gradient couples each neuron to all others through the downstream Jacobian (\S\ref{sec:method:gradient}).
9	This suggests KL should outperform BCE under global allocation.
10	The empirical picture, however, reveals something more fundamental: KL-trained predictors discover neuron importance patterns that diverge 53\% from magnitude-based masks (per-layer Jaccard 47\%), and a causal ablation confirms that these learned mask patterns, not gradient coupling, are the primary quality driver.
11	Under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all downstream tasks ($\Delta$$<$1pp), while magnitude-trained BCE achieves 28.13$\pm$0.20.
12	
13	We instantiate a lightweight predictor (75.9M params, $<$1\% of base) trained with forward KL and Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} on LLaMA-3.1-8B~\cite{grattafiori2024llama3}.
14	With uniform allocation, the predictor achieves PPL 11.92 at 50\% sparsity (3-seed); under global top-$k$, PPL improves to 11.79 (49\% over TEAL).
15	At the recommended 30\% operating point, global top-$k$ amplifies cross-seed downstream standard deviation ($7.5\times$), motivating uniform allocation for deployment.
16	Evaluation on Mistral-7B-v0.3~\cite{jiang2023mistral} and Qwen-2.5-14B~\cite{qwen2024qwen25} confirms the PPL advantage at 7--14B, though 14B exhibits an MMLU gap (63.7\% vs.\ TEAL's 71.8\%) not resolved by allocation strategy.
17	Our contribution targets prediction quality and inference simplification; wall-clock speedup requires sparse kernel support not addressed here (Appendix~\ref{app:latency}).
18	
19	Our contributions are:
20	\begin{itemize}[nosep,leftmargin=*]
21	\item KL-trained predictors discover neuron importance patterns diverging 53\% from magnitude-based masks. A causal ablation proves that mask target quality, not gradient coupling, determines quality under global allocation (\S\ref{sec:mask_analysis}).
22	\item These superior mask patterns render post-hoc compensation (+67.2M params) redundant at both tested sparsity levels, yielding a simpler inference pipeline (\S\ref{sec:isocompute}).
23	\item Analysis of allocation-to-downstream interactions at 7--14B: non-monotonic allocation preference at 8B and scale-dependent effects at 14B (\S\ref{sec:scaling}).
24	\end{itemize}
25	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "0e6e4a5b-8da6-41da-af64-a97d56f5049a",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "7ab09a74-9a82-49ba-b123-527a1685f967",
  "sourceToolAssistantUUID": "0e6e4a5b-8da6-41da-af64-a97d56f5049a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 14 · 2026-05-18T18:38:54.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EGwrPsjBmXUwr7KFjaV3LJ`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7ab09a74-9a82-49ba-b123-527a1685f967",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXC8SoAXW64joQ5MDix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fa3b8b9c-6f70-4c7b-bebb-606a59644153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSJw7aEJNt7Q4SU2qGkxHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2039,
      "cache_read_input_tokens": 19190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2039,
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

_source line 15 · 2026-05-18T18:38:54.181Z_

<details><summary>↩ Tool result · `toolu_01EGwrPsjBmXUwr7KFjaV3LJ`</summary>

```text
1	\section{Related Work}
2	
3	\paragraph{Training-Free Activation Sparsity.}
4	TEAL~\cite{liu2025teal} applies global top-$k$ selection by activation magnitude and achieves 40--50\% sparsity with no training cost.
5	CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
6	All training-free methods determine masks from fixed statistics or input-independent criteria, while our predictor generates \emph{input-dependent} masks trained to minimize output-distribution divergence.
7	
8	\paragraph{Predictor-Based Contextual Sparsity.}
9	DejaVu~\cite{liu2023dejavu} introduced learned sparsity predictors trained via BCE to classify each neuron independently.
10	ShadowLLM~\cite{akhauri2024shadowllm} uses attention-based routing with per-layer MSE supervision for intermediate coupling within each layer but without end-to-end gradient signal.
11	FastForward~\cite{gautam2026fastforward} adds a 67.2M-parameter compensation network using BCE for mask prediction, adding inference latency.
12	SVD-CSP~\cite{serbin2026svdcsp} compresses sparsity predictors via SVD decomposition for reduced predictor overhead.
13	PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
14	MaskLLM~\cite{fang2024maskllm} also employs learnable masks with Gumbel relaxation and frozen weights, but targets N:M semi-structured \emph{weight} sparsity (2:4 patterns) via per-group categorical selection (Gumbel-Softmax), producing fixed masks independent of input tokens.
15	Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
16	The structural mismatch we characterize (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns eliminate cross-group budget competition.
17	All prior predictor-based methods use decomposed (BCE) or intermediate (MSE) objectives where each neuron's gradient is independent of other mask states.
18	Our contribution is primarily empirical: we observe that a coupled KL objective propagates gradients through all downstream layers and quantify when this matters for global allocation quality.
19	
20	\paragraph{Static Bias Correction.}
21	SPON~\cite{xu2026spon} learns input-independent bias vectors via closed-form KL minimization per layer, absorbed into weights at deployment.
22	Our method is fundamentally different: a per-token contextual predictor trained end-to-end across all layers, producing input-dependent masks.
23	SPON solves a static per-layer problem; we solve a global dynamic prediction problem. The two are weakly correlated (cosine similarity 0.196, $R^2$=0.038; \S\ref{sec:experiments}).
24	
25	\paragraph{Activation Function Engineering.}
26	ReLU Strikes Back~\cite{mirzadeh2024relu} replaces SiLU with ReLU for $>$90\% natural sparsity; TurboSparse~\cite{song2024turbosparse} and ProSparse~\cite{song2025prosparse} engineer extreme sparsity through activation modifications; the Sparsing Law~\cite{luo2024sparsinglaw} formalizes how activation density increases with training compute.
27	MiniTron~\cite{muralidharan2024minitron} combines structured pruning with distillation but modifies architecture permanently.
28	All require retraining or weight modification; our method is a plug-in predictor on \emph{unmodified} SwiGLU models.
29	
30	\paragraph{Weight Pruning, Distillation, and Routing.}
31	Wanda~\cite{sun2024wanda} and SparseGPT~\cite{frantar2023sparsegpt} produce static weight masks; Switch Transformers~\cite{fedus2022switch} and Mixture-of-Depths~\cite{raposo2024mod} achieve conditional computation through learned routing.
32	KL-based distillation~\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd} trains compact students; SparseLoRA~\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.
33	We apply the KL principle to train a sparsity predictor on unmodified dense models, using Gumbel-Sigmoid sampling~\cite{maddison2017concrete,louizos2018l0} for differentiable discrete mask optimization.
34	
35	\paragraph{MoE Routing and Gated Sparsity.}
36	Expert Choice routing~\cite{zhou2022expertchoice} lets each expert select its top-$k$ tokens under a fixed capacity budget, a global allocation perspective that parallels TEAL's neuron-level global top-$k$.
37	D2D-MoE~\cite{szatkowski2024d2dmoe} converts dense SwiGLU layers into dynamic-$k$ MoE by exploiting the same activation sparsity we target, but restructures the network into discrete experts rather than predicting masks on the original architecture.
38	Gated architectures beyond SwiGLU (e.g., Griffin's RG-LRU~\cite{de2024griffin}) produce analogous structured sparsity through their gating mechanisms, suggesting that output-distribution prediction may generalize beyond standard Transformer FFNs.
39	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fa3b8b9c-6f70-4c7b-bebb-606a59644153",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "54db2246-4f03-4c64-bbc6-687bddf4261d",
  "sourceToolAssistantUUID": "fa3b8b9c-6f70-4c7b-bebb-606a59644153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-18T18:38:54.706Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W4zuW39iyQbCpw9mzf5Qbv`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "54db2246-4f03-4c64-bbc6-687bddf4261d",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXC8SoAXW64joQ5MDix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6e928465-5259-4ec0-9eea-f5c4ff874697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSJw7aEJNt7Q4SU2qGkxHr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2039,
      "cache_read_input_tokens": 19190,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2039,
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

_source line 17 · 2026-05-18T18:38:54.716Z_

<details><summary>↩ Tool result · `toolu_01W4zuW39iyQbCpw9mzf5Qbv`</summary>

```text
1	\section{Method}
2	\label{sec:method}
3	
4	We present a KL distillation framework for training contextual sparsity predictors in SwiGLU-based language models.
5	The method replaces per-neuron binary classification (BCE) with an output-distribution objective that couples all pruning decisions through the model's forward pass and achieves competitive performance without auxiliary error compensation networks at inference.
6	
7	\subsection{Problem Formulation}
8	\label{sec:method:formulation}
9	
10	Consider a pretrained transformer with $L$ layers, each containing a SwiGLU feed-forward network~\cite{shazeer2020glu}.
11	For layer $\ell$, the FFN computes:
12	\begin{align}
13	\mathbf{y}^{(\ell)} = \bigl(\sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)},
14	\label{eq:swiglu}
15	\end{align}
16	where $\mathbf{x}^{(\ell)} \in \mathbb{R}^{d}$ is the hidden state after attention ($d{=}4096$), $\sigma$ denotes SiLU, $\mathbf{W}_g^{(\ell)}, \mathbf{W}_u^{(\ell)} \in \mathbb{R}^{d \times d_{\text{ff}}}$ and $\mathbf{W}_d^{(\ell)} \in \mathbb{R}^{d_{\text{ff}} \times d}$ are the gate, up-projection, and down-projection matrices, and $d_{\text{ff}}{=}14{,}336$.
17	
18	Define the gate activation $\mathbf{g}^{(\ell)} = \sigma(\mathbf{x}^{(\ell)} \mathbf{W}_g^{(\ell)}) \in \mathbb{R}^{d_{\text{ff}}}$.
19	Each element $g_j^{(\ell)}$ determines the contribution of neuron $j$ to the output.
20	We introduce a binary mask $\mathbf{m}^{(\ell)} \in \{0,1\}^{d_{\text{ff}}}$ that zeros out pruned neurons:
21	\begin{align}
22	\mathbf{y}_{\text{sparse}}^{(\ell)} = \bigl(\mathbf{m}^{(\ell)} \odot \mathbf{g}^{(\ell)} \odot \mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}\bigr) \mathbf{W}_d^{(\ell)}.
23	\label{eq:sparse_ffn}
24	\end{align}
25	Our goal is to learn a mask predictor $f_\theta^{(\ell)}(\mathbf{h}) \to \mathbf{s}^{(\ell)} \in (0,1)^{d_{\text{ff}}}$ that produces per-neuron importance scores from the pre-FFN hidden state $\mathbf{h}$.
26	At inference, the scores are fed to a global top-$k$ allocation mechanism~\cite{liu2025teal} that distributes the sparsity budget across layers non-uniformly, retaining the $(1{-}\rho) \times L \times d_{\text{ff}}$ highest-scoring neurons model-wide for a target sparsity ratio $\rho$.
27	
28	
29	\subsection{Predictor Architecture}
30	\label{sec:method:predictor}
31	
32	Each layer $\ell$ has an independent two-layer MLP predictor:
33	\begin{align}
34	f_\theta^{(\ell)}(\mathbf{h}) = \text{GELU}(\mathbf{h} \mathbf{W}_1^{(\ell)}) \, \mathbf{W}_2^{(\ell)},
35	\label{eq:predictor}
36	\end{align}
37	where $\mathbf{W}_1^{(\ell)} \in \mathbb{R}^{d \times d_b}$ and $\mathbf{W}_2^{(\ell)} \in \mathbb{R}^{d_b \times d_{\text{ff}}}$ with bottleneck dimension $d_b{=}128$.
38	The predictor takes the hidden state after attention (before the FFN) and outputs $d_{\text{ff}}$-dimensional logits $\mathbf{s}^{(\ell)}$, from which the mask is derived.
39	
40	Each predictor has $(4096 \times 128) + (128 \times 14336) = 2.37\text{M}$ parameters.
41	With 32 independent predictors (one per layer), the total overhead is 75.9M parameters, less than 1\% of the 8B base model.
42	The predictors operate independently across layers, requiring no cross-layer communication at inference.
43	
44	
45	\subsection{Gumbel-Sigmoid Relaxation}
46	\label{sec:method:gumbel}
47	
48	The hard mask $m_j = \mathbf{1}[s_j > \text{threshold}]$ is non-differentiable, preventing gradient flow from the KL objective through the mask to the predictor parameters.
49	We apply Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} to produce differentiable soft masks:
50	\begin{align}
51	\tilde{m}_j = \sigma_\tau\!\left(\log \frac{s_j}{1 - s_j} + g_1 - g_2\right), \quad g_1, g_2 \sim \text{Gumbel}(0,1),
52	\label{eq:gumbel}
53	\end{align}
54	where $\sigma_\tau(x) = \text{sigmoid}(x / \tau)$ and $\tau$ is a temperature parameter.
55	The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
56	
57	We anneal $\tau$ linearly from 1.0 to 0.1 over training.
58	At high temperature, the soft mask permits gradient flow through all neurons for broad exploration.
59	As temperature decreases, the mask concentrates on confident decisions, approximating the hard allocation used at inference.
60	
61	\paragraph{Comparison with Straight-Through Estimation.}
62	The straight-through estimator (STE)~\cite{bengio2013ste} applies a hard threshold in the forward pass and passes gradients through unchanged ($\partial m / \partial s = 1$).
63	In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the penalty weight and failure to converge to the target sparsity.
64	Gumbel relaxation eliminates this pathology, contributing a 34.5\% improvement (PPL 15.77 $\to$ 11.79 at 50\% sparsity), as we verify empirically in \S\ref{sec:experiments}.
65	
66	
67	\subsection{KL Divergence Training Objective}
68	\label{sec:method:kl}
69	
70	Let $\mathbf{z}_{\text{dense}}$ denote the output logits from a full dense forward pass, and $\mathbf{z}_{\text{sparse}}$ the logits from a forward pass with predictor-generated soft masks $\{\tilde{\mathbf{m}}^{(\ell)}\}_\ell$ applied at every layer.
71	We minimize the forward KL divergence between the dense and sparse output distributions:
72	\begin{align}
73	\mathcal{L}_{\text{KL}} = D_{\text{KL}}(p_{\text{dense}} \,\|\, p_{\text{sparse}}) = \sum_{v} p_{\text{dense}}^{(v)} \log \frac{p_{\text{dense}}^{(v)}}{p_{\text{sparse}}^{(v)}},
74	\label{eq:kl_loss}
75	\end{align}
76	where $p_{\text{dense}} = \text{softmax}(\mathbf{z}_{\text{dense}})$ and $p_{\text{sparse}} = \text{softmax}(\mathbf{z}_{\text{sparse}})$, summed over the vocabulary $v$ and averaged over sequence positions.
77	The base model is frozen; only the predictor parameters receive gradients.
78	
79	We use forward KL (mean-seeking) rather than reverse KL, as the goal is to preserve the dense model's primary predictions rather than explore alternative modes; \S\ref{sec:experiments} validates this choice with ablations over divergence direction (forward KL outperforms JSD by 6.4\% and reverse KL by 8.6\%).
80	No temperature scaling ($T{=}1$) is applied~\cite{hinton2015distilling}.
81	
82	
83	\subsection{Adaptive Penalty Sparsity Controller}
84	\label{sec:method:lagrangian}
85	
86	We enforce a model-level sparsity target $\rho$ via constrained optimization.
87	Let $\bar{s} = \frac{1}{L} \sum_\ell \frac{1}{d_{\text{ff}}} \sum_j \tilde{m}_j^{(\ell)}$ denote the average fraction of retained neurons.
88	The constrained problem is:
89	\begin{align}
90	\min_\theta \; \mathcal{L}_{\text{KL}} \quad \text{s.t.} \quad \bar{s} \leq 1 - \rho.
91	\label{eq:constrained}
92	\end{align}
93	We relax this via an adaptive penalty controller:
94	\begin{align}
95	\mathcal{L} = \mathcal{L}_{\text{KL}} + \lambda \cdot \text{clamp}(|\bar{s} - (1 - \rho)| - \epsilon, \min{=}0)^2,
96	\label{eq:lagrangian}
97	\end{align}
98	where $\epsilon = 0.02$ is a deadzone margin that prevents $\lambda$ from responding to small constraint violations.
99	The penalty weight $\lambda$ is updated multiplicatively at each step:
100	\begin{align}
101	\lambda \leftarrow \begin{cases} \lambda \times 2 & \text{if } \bar{s} > (1-\rho) + \epsilon \\ \lambda \times 0.5 & \text{if } \bar{s} < (1-\rho) - \epsilon \\ \lambda & \text{otherwise} \end{cases}
102	\label{eq:dual_update}
103	\end{align}
104	with $\lambda$ clamped to $[\lambda_{\text{floor}}, \lambda_{\max}]$ where $\lambda_{\text{floor}} = 0.01$ and $\lambda_{\max} \in \{1000, 5000\}$ depending on the target.
105	The geometric doubling requires only $\lambda_{\max}$ as a user-specified hyperparameter (no step-size tuning) and reaches target sparsity within 40--110 steps for 40--50\% targets; for 30\% and 70\% targets, $\lambda$ saturates at $\lambda_{\max}$ with 1.7--5.0\% residual deviation (Appendix~\ref{app:lagrangian}, Figure~\ref{fig:lagrangian_dynamics}). The deadzone prevents oscillation once sparsity is within $\pm$2\%.\footnote{Our update rule resembles the augmented Lagrangian method but replaces gradient-based dual updates with a multiplicative schedule for training stability. We term it an adaptive penalty controller to distinguish from formal dual methods that guarantee KKT satisfaction.}
106	
107	
108	\subsection{Gradient-Based Motivation: BCE vs.\ KL}
109	\label{sec:method:gradient}
110	
111	We analyze the structural difference between BCE and KL training signals to build intuition for why KL distillation may be better suited to global top-$k$ inference. The analysis is suggestive; \S\ref{sec:mask_analysis} provides causal confirmation that mask target quality, not gradient coupling, drives the advantage.
112	
113	\paragraph{BCE gradient structure.}
114	The standard approach trains the predictor against oracle masks $m_j^* = \mathbf{1}[|g_j| \geq \text{top-}k\text{ threshold}]$ derived from the dense model's activation magnitudes, where the threshold is the global top-$k$ cutoff across all layers (matching TEAL's inference protocol).
115	The loss decomposes per neuron:
116	\begin{align}
117	\mathcal{L}_{\text{BCE}} = -\frac{1}{d_{\text{ff}}} \sum_{j=1}^{d_{\text{ff}}} \bigl[ m_j^* \log \sigma(s_j) + (1 - m_j^*) \log(1 - \sigma(s_j)) \bigr].
118	\label{eq:bce}
119	\end{align}
120	The gradient with respect to predictor logit $s_j$ is:
121	\begin{align}
122	\frac{\partial \mathcal{L}_{\text{BCE}}}{\partial s_j} = \sigma(s_j) - m_j^*.
123	\label{eq:bce_grad}
124	\end{align}
125	This gradient depends \emph{only} on neuron $j$'s own prediction and target.
126	Each neuron is trained independently; there is no inter-neuron coupling in the learning signal.
127	
128	\paragraph{KL gradient structure.}
129	Under KL distillation, the gradient for predictor logit $s_j^{(\ell)}$ in layer $\ell$ is:
130	\begin{align}
131	\frac{\partial \mathcal{L}_{\text{KL}}}{\partial s_j^{(\ell)}} = \underbrace{\frac{\partial \mathcal{L}_{\text{KL}}}{\partial \mathbf{z}_{\text{sparse}}}}_{\text{(a)}} \cdot \underbrace{\frac{\partial \mathbf{z}_{\text{sparse}}}{\partial \mathbf{h}^{(\ell)}}}_{\text{(b)}} \cdot \underbrace{\frac{\partial \mathbf{h}^{(\ell)}}{\partial \tilde{m}_j^{(\ell)}}}_{\text{(c)}} \cdot \underbrace{\frac{\partial \tilde{m}_j^{(\ell)}}{\partial s_j^{(\ell)}}}_{\text{(d)}},
132	\label{eq:kl_grad}
133	\end{align}
134	where each factor has a distinct role:
135	\begin{itemize}
136	\item[\textbf{(a)}] The KL gradient at the output, reflecting how each logit component deviates from the dense distribution.
137	\item[\textbf{(b)}] The Jacobian through all downstream layers from layer $\ell$'s output to the final logits. This factor couples neuron $j$'s gradient to the state of every other retained neuron in layers $\ell, \ell{+}1, \ldots, L$, because the sparse hidden state propagates through subsequent attention and FFN operations.
138	\item[\textbf{(c)}] The local mask effect: $\partial \mathbf{h}^{(\ell)} / \partial \tilde{m}_j^{(\ell)} = (g_j^{(\ell)} \cdot [\mathbf{x}^{(\ell)} \mathbf{W}_u^{(\ell)}]_j) \cdot \mathbf{W}_{d,j}^{(\ell)}$, projecting through the down-projection to affect the full $d$-dimensional hidden state.
139	\item[\textbf{(d)}] The Gumbel-Sigmoid derivative: the differentiable path from logit to mask.
140	\end{itemize}
141	
142	\paragraph{The structural mismatch.}
143	The key observation is that factor (b) makes the KL gradient for neuron $j$ depend on \emph{all} other neurons' mask values.
144	BCE's factorized gradient (Eq.~\ref{eq:bce_grad}) optimizes each neuron's prediction accuracy in isolation, but TEAL inference selects neurons via a global ranking across all layers.
145	Under global top-$k$, the decision to retain neuron $j$ depends on the scores of all other neurons, a combinatorial interaction that BCE cannot capture.
146	
147	Concretely, BCE achieves high per-neuron accuracy ($>$90\% oracle agreement) yet produces poor output under TEAL, because it optimizes a proxy misaligned with output preservation under global budget allocation.
148	KL directly optimizes the end-to-end objective, with gradients that reflect inter-neuron dependencies through the computation graph.
149	
150	\paragraph{Empirical verification.}
151	Measuring gradient SNR\footnote{$\text{SNR}_\ell = \|\mathbb{E}[\nabla_{\theta_\ell} \mathcal{L}]\|_2^2 / \text{Var}[\nabla_{\theta_\ell} \mathcal{L}]$, expectation over mini-batches.} over 7 checkpoints (steps 0--300) on LLaMA-3.1-8B (C4 data) with 95\% bootstrap CI, KL achieves $5.14\times$ higher SNR than BCE at convergence ($5.877{\times}10^{-3}$ vs.\ $1.144{\times}10^{-3}$ at step 300), concentrated in early layers where factor~(b)'s Jacobian traverses the full remaining network; late layers show reduced advantage.
152	The trajectory is non-monotonic: BCE SNR exceeds KL during mid-training (steps 100--250) before KL's advantage emerges at convergence, consistent with KL's gradient coupling becoming effective only after the predictor learns a coarse mask structure (Appendix~\ref{app:snr_extended}).
153	
154	\subsection{Two-Dimensional Taxonomy of Sparsity Prediction Methods}
155	\label{sec:method:taxonomy}
156	
157	We organize prior work along two axes that capture the essential design decisions for sparsity prediction: \emph{correction granularity} (how the mask adapts to input) and \emph{training signal coupling} (whether the objective captures inter-neuron dependencies). These axes are motivated by our gradient analysis (\S\ref{sec:method:gradient}): granularity determines what information the predictor conditions on, while coupling determines whether the training signal reflects global allocation effects.
158	
159	\begin{table}[t]
160	\centering
161	\caption{Taxonomy of learned sparsity prediction methods along correction granularity (rows) and training signal coupling (columns). Our method fills the previously unexplored Per-token $\times$ Coupled cell.}
162	\label{tab:taxonomy}
163	\resizebox{\columnwidth}{!}{
164	\begin{tabular}{lccc}
165	\toprule
166	 & Decomposed (BCE) & Intermediate (MSE) & Coupled (KL) \\
167	\midrule
168	Static & --- & --- & SPON \\
169	Per-token & DejaVu, FastForward & ShadowLLM, D2DMoE & \textbf{Ours} \\
170	\bottomrule
171	\end{tabular}}
172	\end{table}
173	
174	\paragraph{Correction granularity.}
175	\emph{Static} methods~\cite{xu2026spon} learn a fixed bias vector per layer that does not depend on the input token.
176	\emph{Per-token} methods~\cite{liu2023dejavu,gautam2026fastforward,akhauri2024shadowllm,szatkowski2024d2dmoe} produce a unique mask for each input position, conditioning on the token's hidden state at each layer.
177	
178	\paragraph{Training signal coupling.}
179	\emph{Decomposed} objectives (BCE) treat each neuron independently, optimizing per-element classification against an oracle mask.
180	\emph{Intermediate} objectives (MSE on hidden states) capture local coupling within a single layer but not end-to-end output effects.
181	\emph{Coupled} objectives (KL on output distribution) propagate gradients through the full forward pass, reflecting how all mask decisions jointly affect the final distribution.
182	
183	SPON~\cite{xu2026spon} distills a per-layer bias via KL but cannot adapt to per-input neuron importance (static $\times$ coupled).
184	DejaVu~\cite{liu2023dejavu} and FastForward~\cite{gautam2026fastforward} achieve per-token granularity but use BCE, losing inter-neuron coupling: their decomposed gradient (Eq.~\ref{eq:bce_grad}) is blind to cross-neuron interactions under global allocation.
185	D2DMoE~\cite{szatkowski2024d2dmoe} provides intermediate coupling (MSE on hidden states) but not end-to-end output effects.
186	Our method combines per-token prediction with coupled KL training (Table~\ref{tab:taxonomy}), propagating gradients through all downstream layers.
187	
188	\begin{figure}[t]
189	\centering
190	\includegraphics[width=\columnwidth]{fig1_overview.pdf}
191	\caption{Method overview: a lightweight per-layer predictor produces importance scores trained via KL divergence with Gumbel-Sigmoid relaxation. At inference, scores feed TEAL's global top-$k$ allocation without compensation networks.}
192	\label{fig:overview}
193	\end{figure}
194	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6e928465-5259-4ec0-9eea-f5c4ff874697",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "633a064f-628e-4e25-a0cb-580f26000cb2",
  "sourceToolAssistantUUID": "6e928465-5259-4ec0-9eea-f5c4ff874697",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-18T18:38:54.887Z_

<details open><summary>🔧 Tool call — Read · `toolu_012Bs2jCKQy6xQeqPssBN86P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "633a064f-628e-4e25-a0cb-580f26000cb2",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXC8SoAXW64joQ5MDix",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "9df99a66-7c87-4120-9a89-24f484b621bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RSJw7aEJNt7Q4SU2qGkxHr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2039,
      "cache_read_input_tokens": 19190,
      "output_tokens": 232,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2039
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 232,
          "cache_read_input_tokens": 19190,
          "cache_creation_input_tokens": 2039,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2039,
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

_source line 19 · 2026-05-18T18:38:54.898Z_

<details><summary>↩ Tool result · `toolu_012Bs2jCKQy6xQeqPssBN86P`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	
6	\paragraph{Model and Predictor.}
7	We evaluate on LLaMA-3.1-8B~\cite{grattafiori2024llama3}, which uses SwiGLU FFN blocks~\cite{shazeer2020glu} with $d_{\text{model}}=4096$ and $d_{\text{ff}}=14336$ across 32 layers.
8	The sparsity predictor is a two-layer MLP with 2.37M parameters per layer (75.9M total), implemented as Linear($4096 \to 128$) + GELU + Linear($128 \to 14336$), trained to produce per-neuron importance scores that minimize output-distribution divergence under sparsity.
9	
10	\paragraph{Training.}
11	All predictors are trained for 1000 steps on WikiText-103 with sequence length 2048 and batch size 4, using AdamW~\cite{loshchilov2019adamw} with learning rate $1 \times 10^{-3}$, weight decay $5 \times 10^{-2}$, and cosine decay.
12	The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
13	
14	\paragraph{Evaluation.}
15	We report perplexity on WikiText-2~\cite{merity2017pointer} (seq\_len=2048) and downstream accuracy on ARC-Challenge (25-shot), WinoGrande (5-shot), MMLU (5-shot), and GSM8K (8-shot).
16	
17	\paragraph{Inference Protocol.}
18	At inference, the predictor produces per-neuron scores that are passed to TEAL's global top-$k$ allocation mechanism~\cite{liu2025teal}, which distributes the sparsity budget across layers non-uniformly.
19	We term this \textit{predictor-TEAL}: the predictor replaces TEAL's magnitude-based scoring while retaining its allocation strategy.
20	
21	\paragraph{Baselines.}
22	We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
23	
24	
25	\subsection{Main Results}
26	
27	Table~\ref{tab:main} presents the primary comparison. We recommend uniform allocation for deployment (best downstream preservation); global allocation is analyzed to understand allocation-quality tradeoffs (\S\ref{sec:scaling}).
28	At 30\% sparsity, KL distillation with global TEAL allocation achieves PPL 8.96$\pm$0.02 (3-seed) and reduces TEAL's degradation from dense (10.97 $\to$ 8.96, an 18\% improvement). % exp_id: kl30_3seed_global
29	The advantage holds across additional downstream benchmarks (Appendix~\ref{app:downstream}).
30	Uniform allocation at 30\% provides stable downstream performance (MMLU 40.7$\pm$1.3\%, 3-seed) while global top-$k$ exhibits high seed variance (35.7$\pm$9.5\%), with late-layer starvation (L31 retention 28.4\%) interacting with predictor initialization (\S\ref{sec:scaling}). % exp_id: bench_kl30_uniform, kl30_3seed
31	
32	At 50\% sparsity, KL distillation over vanilla TEAL widens the PPL advantage: 11.79 vs.\ 23.31, a 49\% reduction. % exp_id: bench_kl50_global, bench_teal50
33	The predictor generalizes to C4 validation at both 30\% (PPL 16.03$\pm$0.01, 2-seed) and 50\% (52.5\% over TEAL; Appendix~\ref{app:ood}).
34	However, all methods exhibit downstream collapse on MMLU (28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, both $\approx$ random, 3-seed) and GSM8K ($<$2.2\%); this is a capacity-limited regime where no allocation strategy can recover. % exp_id: bench_kl50_global, d030_kl50_uniform, multi_seed_kl50_global
35	
36	\begin{table}[t]
37	\centering
38	\caption{Main results on LLaMA-3.1-8B. PPL$\downarrow$ on WikiText-2; accuracy$\uparrow$ on downstream tasks. \textbf{Bold}: best among compensation-free methods per sparsity level. BCE follows the DejaVu~\cite{liu2023dejavu} predictor pipeline (per-neuron BCE on magnitude oracles) with a FastForward-style~\cite{gautam2026fastforward} compensation network (67.2M params) applied post-masking; no TEAL allocation. Entries with $\pm$ report 3-seed mean$\pm$std ($s \in \{42, 123, 456\}$); 50\% uniform PPL is 3-seed ($11.92 \pm 0.07$; Appendix~\ref{app:stability}); remaining entries use seed 42.}
39	\label{tab:main}
40	\resizebox{\columnwidth}{!}{
41	\begin{tabular}{llccccc}
42	\toprule
43	Sparsity & Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
44	\midrule
45	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
46	\midrule
47	\multirow{3}{*}{30\%}
48	& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
49	& KL global (Ours) & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & \textbf{8.0$\pm$0.7} \\ % exp_id: kl30_3seed_global
50	& KL uniform & \textbf{8.82$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
51	\midrule
52	\multirow{4}{*}{50\%}
53	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
54	& KL global (Ours) & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 28.1$\pm$0.2 & 1.29 \\ % exp_id: multi_seed_kl50_global
55	& KL uniform & 11.92$\pm$0.07 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\ % exp_id: multi_seed_kl50_uniform
56	& BCE (2700 steps)$^\ast$ & 28.13$\pm$0.20 & 27.6$\pm$0.6 & 51.8$\pm$0.6 & 26.1$\pm$0.5 & 2.1$\pm$0.2 \\ % exp_id: bce50_3seed
57	\bottomrule
58	\end{tabular}}
59	\end{table}
60	
61	
62	\subsection{Extended Training Analysis}
63	\label{sec:isocompute}
64	
65	To test whether BCE simply requires more compute, we train it for 2700 steps (2.71$\times$ the KL step budget, approximately equal wall-clock time: $\sim$46 min BCE vs.\ $\sim$45 min KL on RTX PRO 6000).
66	The BCE predictor achieves PPL 28.13$\pm$0.20 (3-seed), still 2.39$\times$ worse than KL at 1000 steps (PPL 11.79). % exp_id: bce50_3seed
67	The difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL (28.13 vs.\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
68	Coupled training correlates with better output preservation; the causal ablation in \S\ref{sec:mask_analysis} confirms that target quality, not gradient coupling, is the primary driver.
69	
70	
71	\subsection{Mask Pattern Analysis}
72	\label{sec:mask_analysis}
73	
74	To understand \emph{what} the KL predictor learns, we compare KL-derived masks against magnitude-based oracle masks (the BCE training targets) at 50\% sparsity on WikiText-2.
75	Per-layer Jaccard similarity between the two mask types averages 47\% across 32 layers: the KL predictor discovers a neuron importance ranking that diverges 53\% from activation magnitude.
76	Despite this divergence, KL achieves PPL 11.79 vs.\ BCE's 28.13$\pm$0.20, confirming that output-distribution fidelity, not magnitude agreement, determines mask quality under global allocation. % exp_id: bench_kl50_global, bce50_3seed, c1_mask_overlap
77	
78	\paragraph{Causal Ablation: Target Quality vs.\ Gradient Coupling.}
79	To disentangle whether KL's advantage stems from its coupled gradient pathway or from the mask patterns it discovers, we train a standard BCE predictor on KL-derived oracle masks instead of magnitude-based masks.
80	Under controlled evaluation (TEAL 50\% uniform allocation at matched sparsity), BCE trained on KL targets matches the KL predictor within statistical noise across all five metrics (PPL 11.96 vs.\ 11.96; ARC-c 32.17 vs.\ 32.59; WinoGrande 63.14 vs.\ 62.35; MMLU 27.79 vs.\ 27.92; GSM8K 2.05 vs.\ 1.97; max $\Delta$=0.79pp). % exp_id: c1_bce_kl_targets_teal50u, c1_kl_teal50u
81	Standard BCE on magnitude masks yields PPL 28.13$\pm$0.20 (3-seed, Table~\ref{tab:main}), $2.4\times$ worse.
82	Target quality, not gradient coupling, is the sole driver of KL's advantage; the coupled gradient is a means to discover better targets, not an independent source of quality. % exp_id: bce50_3seed
83	
84	Since BCE on KL targets matches KL across all metrics, one might consider a two-stage pipeline (train KL, extract oracle masks, retrain with BCE).
85	This offers no practical advantage: the final BCE predictor equals the KL predictor while adding an extra training phase; the KL predictor already produces contextual per-input masks directly.
86	
87	
88	\subsection{Ablation Studies}
89	
90	Table~\ref{tab:ablation} isolates the contribution of each design choice at 50\% sparsity.
91	
92	\begin{table}[t]
93	\centering
94	\caption{Ablation at 50\% sparsity on LLaMA-3.1-8B (WikiText-2 PPL$\downarrow$, unified benchmark protocol).}
95	\label{tab:ablation}
96	\small
97	\begin{tabular}{lcc}
98	\toprule
99	Configuration & PPL$\downarrow$ & $\Delta$ from Ours \\
100	\midrule
101	\multicolumn{3}{l}{\textit{KL-based variants}} \\
102	Forward KL + Gumbel (Ours) & \textbf{11.79} & --- \\ % exp_id: bench_kl50_global
103	JSD (symmetric) + Gumbel & 12.54 & +0.75 \\ % exp_id: jsd_ablation_s42
104	Reverse KL + Gumbel & 12.80 & +1.01 \\ % exp_id: reverse_kl_ablation_s42
105	Forward KL + STE & 15.77 & +3.98 \\ % exp_id: ste_baseline_s42
106	\midrule
107	\multicolumn{3}{l}{\textit{BCE-based variants}} \\
108	BCE + Compensation (hard mask) & 25.44 & +13.65 \\ % exp_id: bce_comp_staged_s42
109	BCE (no compensation) & 27.97 & +16.18 \\ % exp_id: eval_bce_v3_s42
110	BCE + Gumbel + Penalty (no KL) & 38.02 & +26.23 \\ % exp_id: bce_gumbel_lagrangian_isolation
111	\bottomrule
112	\end{tabular}
113	\end{table}
114	
115	\paragraph{Gumbel vs.\ STE.}
116	Replacing Gumbel-Sigmoid with STE~\cite{bengio2013ste} degrades PPL from 11.79 to 15.77 (+3.98), accounting for 34.5\% of the improvement over vanilla TEAL. % exp_id: ste_baseline_s42
117	
118	\paragraph{Divergence Direction.}
119	Forward KL (mode-covering) outperforms JSD (+6.4\%) and reverse KL (+8.6\%), consistent with the SNR analysis in \S\ref{sec:method:gradient}: complete teacher supervision is associated with better global allocation quality. % exp_id: jsd_ablation_s42, reverse_kl_ablation_s42
120	This contrasts with MiniLLM~\cite{gu2024minillm} (reverse KL for generation); in mask prediction, mode-covering ensures no important neuron is omitted.
121	
122	\paragraph{SPON Contribution.}
123	Adding SPON~\cite{xu2026spon} bias correction reduces PPL from 12.08 to 11.79 (2.4\% relative); see \S\ref{sec:spon} for decomposition.\footnote{SPON analysis uses \texttt{evaluate.py}; main results use the unified benchmark.} % exp_id: spon_2048_s42, mvp_kl_norm_v2_s42
124	
125	\paragraph{Loss Function Isolation.}
126	BCE with identical Gumbel-Sigmoid and penalty yields PPL 38.02, worse than vanilla BCE (27.97): the penalty interferes with per-neuron optimization without global coordination. % exp_id: bce_gumbel_lagrangian_isolation
127	The loss effect ($\Delta$PPL=26.23) is $6.6\times$ the relaxation effect ($\Delta$PPL=3.98).
128	
129	\paragraph{Compensation Redundancy.}
130	Adding compensation~\cite{gautam2026fastforward} (+67.2M params) to KL provides no benefit at either tested sparsity: at 50\%, all five metrics are identical to KL-only; at 30\%, PPL 8.97$\pm$0.01 vs.\ 8.96$\pm$0.03 (2-seed). BCE requires compensation (27.97$\to$25.44), yet remains $2.16\times$ worse than KL without it. Training converges by step 700 (Appendix~\ref{app:comp_convergence}). % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42, bce_comp_staged_s42
131	
132	\paragraph{Hyperparameter Robustness.}
133	Appendix~\ref{app:db_sensitivity} confirms robustness to predictor capacity ($d_b$, $<$3\%), temperature ($<$1.8\%), and training steps (saturated by 800). % exp_id: db_sensitivity_sweep, tau_schedule_sweep, training_steps_sweep
134	
135	
136	\subsection{Sparsity Scaling and Regime Analysis}
137	\label{sec:scaling}
138	
139	Table~\ref{tab:scaling} and Figure~\ref{fig:sparsity_sweep} show PPL as a function of sparsity for the KL predictor under global allocation and vanilla TEAL.
140	
141	\begin{figure}[t]
142	\centering
143	\includegraphics[width=\columnwidth]{fig2_sparsity_sweep.pdf}
144	\caption{Perplexity scaling with sparsity. The KL predictor's advantage grows disproportionately as more neurons are pruned.}
145	\label{fig:sparsity_sweep}
146	\end{figure}
147	
148	\begin{table}[t]
149	\centering
150	\caption{PPL scaling with sparsity (WikiText-2). KL advantage grows disproportionately with sparsity.}
151	\label{tab:scaling}
152	\small
153	\begin{tabular}{lccc}
154	\toprule
155	Sparsity & KL (Ours) & TEAL vanilla & Relative advantage \\
156	\midrule
157	30\% & \textbf{8.96} & 10.97 & 18\% \\ % exp_id: kl30_3seed_global
158	50\% & \textbf{11.79} & 23.31 & 49\% \\ % exp_id: bench_kl50_global
159	70\% & \textbf{17.91} & 100.11 & 82\% \\ % exp_id: kl_70_global_teal
160	\bottomrule
161	\end{tabular}
162	\end{table}
163	
164	The KL advantage grows from 18\% at 30\% to 82\% at 70\%, where TEAL collapses (PPL 100.11) while the learned predictor maintains coherent allocation.
165	In absolute terms, KL/Dense degradation is $1.47\times$ at 30\%, $1.93\times$ at 50\%, and $2.93\times$ at 70\%, compared to TEAL/Dense ratios of $1.79\times$, $3.81\times$, and $16.4\times$ respectively.
166	
167	\paragraph{Allocation Behavior Across Sparsity Levels.}
168	Table~\ref{tab:phase} presents global vs.\ uniform allocation at three sparsity levels and reveals qualitative shifts in allocation preference. Denser sampling (e.g., 35\% sparsity) would be needed to precisely locate region boundaries.
169	
170	\begin{table}[t]
171	\centering
172	\caption{Allocation analysis: global (TEAL) vs.\ uniform per-layer allocation across sparsity levels. Entries with $\pm$ report 3-seed mean$\pm$std; remaining entries use seed 42. Each row uses a predictor trained at the respective sparsity target.}
173	\label{tab:phase}
174	\resizebox{\columnwidth}{!}{
175	\begin{tabular}{llccccc}
176	\toprule
177	Sparsity & Allocation & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
178	\midrule
179	0\% & Dense & 6.12 & 58.28 & 78.06 & 65.27 & 48.75 \\
180	\midrule
181	\multirow{3}{*}{30\%}
182	& TEAL vanilla & 10.97 & 42.32 & 66.06 & 38.61 & 7.88 \\ % exp_id: bench_teal30
183	& KL global & 8.96$\pm$0.02 & \textbf{43.8$\pm$3.6} & \textbf{70.2$\pm$0.9} & 35.7$\pm$9.5 & \textbf{8.0$\pm$0.7} \\ % exp_id: kl30_3seed_global
184	& KL uniform & \textbf{8.82$\pm$0.02} & 43.7$\pm$2.5 & 68.9$\pm$0.4 & \textbf{40.7$\pm$1.3} & 7.5$\pm$0.1 \\ % exp_id: bench_kl30_uniform, kl30_s123_uniform, kl30_s456_uniform
185	\midrule
186	\multirow{2}{*}{40\%}
187	& KL global & 10.12 & 40.96 & 65.35 & \textbf{38.06} & \textbf{5.00} \\ % exp_id: bench_kl40_global
188	& KL uniform & \textbf{8.36} & \textbf{41.81} & \textbf{67.17} & 30.68 & 3.94 \\ % exp_id: d030_kl40_uniform
189	\midrule
190	\multirow{3}{*}{50\%}
191	& TEAL vanilla & 23.31 & 28.41 & 53.04 & \textbf{28.32} & 1.97 \\ % exp_id: bench_teal50
192	& KL global & \textbf{11.79} & \textbf{32.85} & \textbf{63.46} & 28.1$\pm$0.2 & 1.29 \\ % exp_id: multi_seed_kl50_global
193	& KL uniform & 11.92$\pm$0.07 & 32.76 & 62.90 & 28.0$\pm$0.6 & \textbf{2.12} \\ % exp_id: multi_seed_kl50_uniform
194	\bottomrule
195	\end{tabular}}
196	\end{table}
197	
198	The allocation preference appears \emph{non-monotonic} across the sampled sparsity levels (7--8B scale). We observe distinct qualitative behaviors:
199	
200	\noindent\textbf{Budget-surplus ($\leq$30\%).}
201	Uniform allocation provides $7.5\times$ smaller cross-seed MMLU $\sigma$ (1.3pp vs.\ 9.5pp), eliminating catastrophic seed-dependent degradation under global top-$k$ (MMLU 35.7$\pm$9.5\% vs.\ 40.7$\pm$1.3\%, 3-seed); the instability is allocation-induced, not from the distillation objective (PPL cross-seed CV $<$ 0.3\%; Appendix~\ref{app:lagrangian}). % exp_id: kl30_3seed
202	
203	\noindent\textbf{Budget-constrained ($\sim$40\%).}
204	The preference reverses: global achieves MMLU 38.06\% vs.\ uniform's 30.68\% (+7.4pp). % exp_id: bench_kl40_global, d030_kl40_uniform
205	PPL remains low (8.36) but downstream accuracy degrades; PPL is a poor proxy for reasoning.
206	
207	\noindent\textbf{Capacity-limited ($\geq$50\%).}
208	Global/uniform gap vanishes (MMLU 28.1$\pm$0.2\% vs.\ 28.0$\pm$0.6\%, $\sigma\leq$0.6pp; contrast 9.5pp at 30\%), consistent with capacity limitation. % exp_id: multi_seed_kl50_global, multi_seed_kl50_uniform
209	Late-layer starvation persists across levels (Figure~\ref{fig:retention}; Appendix~\ref{app:db_sensitivity}).
210	
211	
212	\paragraph{SPON Orthogonality.}
213	\label{sec:spon}
214	SPON~\cite{xu2026spon} bias correction is weakly correlated with the KL predictor (cosine similarity 0.196, $R^2$=0.038) and yields only 2.4\% PPL improvement; the predictor already captures most recoverable signal. % exp_id: spon_decomposition, spon_2048_s42, mvp_kl_norm_v2_s42
215	
216	\paragraph{Cross-Architecture Validation.}
217	\label{sec:cross_arch}
218	On Mistral-7B-v0.3~\cite{jiang2023mistral}, the KL advantage ratio is consistent with LLaMA-8B (within 8\% at $\leq$50\% sparsity; Appendix~\ref{app:cross_arch}).
219	
220	\paragraph{Scale Generalization: Qwen-2.5-14B.}
221	\phantomsection\label{sec:14b}
222	On Qwen-2.5-14B~\cite{qwen2024qwen25} at 30\%, KL's PPL advantage generalizes ($1.47\times$ dense, Table~\ref{tab:14b} in Appendix~\ref{app:14b}), but MMLU falls below TEAL (63.7 vs.\ 71.8\%), suggesting higher knowledge density causes KL's output-preservation objective to sacrifice task-specific pathways; uniform allocation recovers only +0.8pp. % exp_id: qwen14b_kl30_s42, qwen14b_teal30_eval, qwen14b_kl30_uniform
223	
224	\paragraph{Inference Efficiency.}
225	The pipeline adds 6.4\% overhead while removing the compensation network ($-$2.7\% latency, $-$67.2M params; Appendix~\ref{app:latency}).
226	
227	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9df99a66-7c87-4120-9a89-24f484b621bb",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "7be6c48b-5219-4fed-8644-397e95017b4d",
  "sourceToolAssistantUUID": "9df99a66-7c87-4120-9a89-24f484b621bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 20 · 2026-05-18T18:38:59.755Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FcgmCzbphRoXHw5cemMWXm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7be6c48b-5219-4fed-8644-397e95017b4d",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXCQZR19b63djKfUYFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f90ab36d-0a46-4b62-b98f-8056482a6d93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FT1GFRiza8BrEfu8VZp9BX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14759,
      "cache_read_input_tokens": 21229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 21 · 2026-05-18T18:38:59.760Z_

<details><summary>↩ Tool result · `toolu_01FcgmCzbphRoXHw5cemMWXm`</summary>

```text
1	\appendix
2	
3	\section{Inference Efficiency}
4	\label{app:latency}
5	
6	Table~\ref{tab:latency} reports inference throughput on a single NVIDIA RTX PRO 6000 Blackwell Server Edition GPU (batch size 1, sequence length 2048, fp16, averaged over 100 forward passes).
7	
8	\begin{table}[h]
9	\centering
10	\caption{Inference latency on LLaMA-3.1-8B (RTX PRO 6000 Blackwell, batch=1, seq=2048, fp16, 100 forward passes). Overhead is relative to dense inference.}
11	\label{tab:latency}
12	\small
13	\begin{tabular}{llcccc}
14	\toprule
15	Method & Sparsity & ms/fwd & tok/s & Overhead \\
16	\midrule
17	Dense & 0\% & 119.11$\pm$0.57 & 17{,}195 & --- \\
18	\midrule
19	KL predictor-only & 30\% & 126.64$\pm$0.70 & 16{,}172 & +6.3\% \\ % exp_id: latency_bench
20	KL predictor-only & 50\% & 126.78$\pm$0.31 & 16{,}154 & +6.4\% \\ % exp_id: latency_bench
21	\midrule
22	Predictor + compensation & 30\% & 129.94$\pm$0.75 & 15{,}761 & +9.1\% \\ % exp_id: latency_bench
23	Predictor + compensation & 50\% & 129.71$\pm$0.53 & 15{,}789 & +8.9\% \\ % exp_id: latency_bench
24	\bottomrule
25	\end{tabular}
26	\end{table}
27	
28	The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
29	Eliminating the compensation network saves an additional $\sim$2.7\% latency overhead and 67.2M parameters (the per-layer GEMV required for output rescaling); KL distillation thus provides both quality and efficiency advantages over BCE-based approaches.
30	The overhead is near-identical at 30\% and 50\% sparsity because the predictor runs the same computation regardless of target sparsity; only the top-$k$ threshold changes.
31	
32	Note that the current implementation uses unstructured element-wise masks, which do not translate to wall-clock speedup without sparse kernel support.
33	The pipeline adds $\sim$6.4\% overhead; net acceleration requires kernel-level sparse computation optimizations (e.g., Triton block-sparse, cuSPARSE) that are beyond the scope of this work.
34	Our contribution is prediction quality and inference simplification (removing the compensation network), not end-to-end latency reduction.
35	
36	
37	\section{Predictor Bottleneck Sensitivity}
38	\label{app:db_sensitivity}
39	
40	Table~\ref{tab:db_sensitivity} reports the effect of predictor bottleneck dimension $d_b$ on PPL at 50\% sparsity under both TEAL global allocation (the paper's primary inference protocol) and per-token evaluation.
41	
42	\begin{table}[h]
43	\centering
44	\caption{Predictor bottleneck sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$). TEAL global is the primary inference protocol; per-token shown for reference.}
45	\label{tab:db_sensitivity}
46	\small
47	\begin{tabular}{lcccc}
48	\toprule
49	$d_b$ & Params & TEAL global & $\Delta$ & Per-token \\
50	\midrule
51	64 & 38.2M (0.48\%) & 12.076 & +0.9\% & 10.16 \\ % exp_id: db_sensitivity_sweep
52	128 & 75.9M (0.95\%) & 11.963 & --- & 9.218 \\ % exp_id: db_sensitivity_sweep
53	256 & 151.5M (1.89\%) & 12.105 & +1.2\% & 8.586 \\ % exp_id: db_sensitivity_sweep
54	512 & 302.5M (3.77\%) & 12.315 & +2.9\% & 7.93 \\ % exp_id: db_sensitivity_sweep
55	\bottomrule
56	\end{tabular}
57	\end{table}
58	
59	Under TEAL global allocation, increasing $d_b$ beyond 128 provides no benefit (PPL slightly worsens), while per-token evaluation shows monotonic improvement (10.16$\to$7.93).
60	This divergence indicates that the global top-$k$ allocation mechanism, not predictor capacity, is the binding constraint: additional predictor capacity produces better per-neuron scores, but the global ranking and budget distribution cannot exploit them.
61	The $d_b{=}128$ configuration (75.9M params, $<$1\% of base model) is therefore optimal for the TEAL inference protocol.
62	
63	\subsection{Temperature Schedule Sensitivity}
64	\label{app:tau_sensitivity}
65	
66	\begin{table}[h]
67	\centering
68	\caption{Temperature schedule sensitivity at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
69	\label{tab:tau_sensitivity}
70	\small
71	\begin{tabular}{lc}
72	\toprule
73	$\tau$ Schedule & PPL$\downarrow$ \\
74	\midrule
75	Fixed $\tau{=}0.5$ & \textbf{11.861} \\ % exp_id: tau_schedule_sweep
76	Linear $1.0 \to 0.1$ (default) & 11.963 \\ % exp_id: tau_schedule_sweep
77	Fixed $\tau{=}0.1$ & 12.072 \\ % exp_id: tau_schedule_sweep
78	\bottomrule
79	\end{tabular}
80	\end{table}
81	
82	Temperature schedule has minimal impact ($<$1.8\% PPL variation).
83	The linear annealing default is a conservative choice; even removing annealing entirely (fixed $\tau{=}0.5$) yields comparable performance.
84	
85	\subsection{Training Convergence}
86	\label{app:training_convergence}
87	
88	\begin{table}[h]
89	\centering
90	\caption{Training convergence at 50\% sparsity (WikiText-2 PPL$\downarrow$, TEAL global).}
91	\label{tab:training_convergence}
92	\small
93	\begin{tabular}{cc}
94	\toprule
95	Steps & PPL$\downarrow$ \\
96	\midrule
97	200 & 15.158 \\ % exp_id: training_steps_sweep
98	400 & 12.538 \\ % exp_id: training_steps_sweep
99	600 & 12.046 \\ % exp_id: training_steps_sweep
100	800 & 11.907 \\ % exp_id: training_steps_sweep
101	1000 & \textbf{11.906} \\ % exp_id: training_steps_sweep
102	\bottomrule
103	\end{tabular}
104	\end{table}
105	
106	Training converges rapidly: 95\% of the quality gap closes by step 600, and performance saturates by step 800 ($\Delta < 0.001$ between 800 and 1000 steps).
107	Our default of 1000 steps provides a conservative margin.
108	
109	
110	\section{Adaptive Penalty Controller Dynamics}
111	\label{app:lagrangian}
112	
113	Table~\ref{tab:lagrangian} reports the convergence of the adaptive penalty controller across sparsity targets.
114	The geometric doubling pattern ($1 \to 2 \to 4 \to 8 \to \ldots$) enables $\lambda$ to reach steady state within $\sim$10 steps; the deadzone ($\epsilon = 0.02$) then stabilizes $\lambda$ once actual sparsity is within $\pm$2\% of the target.
115	
116	\begin{table}[h]
117	\centering
118	\caption{Penalty controller convergence across sparsity targets (multiplicative schedule, margin $\epsilon=0.02$, 1000 training steps). Deviation is $|$actual $-$ target$|$ / target.}
119	\label{tab:lagrangian}
120	\small
121	\begin{tabular}{lccccc}
122	\toprule
123	Target $\rho$ & $\lambda_{\max}$ & Final $\lambda$ & Actual sparsity & Deviation \\
124	\midrule
125	30\% & 5000 & 5000 (cap) & 0.285 & 5.0\% \\ % exp_id: kl_30pct_s42
126	40\% & 5000 & 625 & 0.398 & 0.5\% \\ % exp_id: kl_40pct_s42
127	50\% & 1000 & 8 & 0.504 & 0.8\% \\ % exp_id: kl_50pct_s42
128	70\% & 1000 & 1000 (cap) & 0.688 & 1.7\% \\ % exp_id: kl_70pct_s42
129	\bottomrule
130	\end{tabular}
131	\end{table}
132	
133	At 50\% sparsity, the SwiGLU gate distribution already clusters near the target, so $\lambda$ remains low (8); the constraint is nearly satisfied by the initial predictor outputs.
134	At 30\% and 70\%, the gap between the gate prior and target is larger, driving $\lambda$ to its respective caps.
135	The 40\% target converges to $\lambda = 625$ with only 0.5\% deviation; this precision reflects a regime where the target is reachable without $\lambda$ saturation.
136	
137	\begin{figure}[h]
138	\centering
139	\includegraphics[width=\columnwidth]{lagrangian_dynamics.pdf}
140	\caption{Adaptive penalty controller convergence across sparsity targets. Upper panel: penalty weight $\lambda$ (log scale) over training steps. The 30\% target requires extreme penalty ($\lambda \to 5000$) to suppress activations below their natural density, while 50\% needs only $\lambda \approx 8$ since SwiGLU gates already cluster near this sparsity. Lower panel: actual sparsity (solid) converges to the target (dashed) within $\sim$10 steps via geometric doubling.}
141	\label{fig:lagrangian_dynamics}
142	\end{figure}
143	
144	Temperature $\tau$ is annealed linearly from 1.0 to 0.1 over 1000 steps.
145	A mild loss increase in the final $\sim$100 steps is expected: as masks become more binary ($\tau \to 0$), discrete rounding noise slightly increases KL divergence, consistent with convergence toward the hard-mask inference regime.
146	
147	The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
148	For the recommended 30\% operating point, actual sparsity is $\approx$28.5\% (5\% deviation). This does not affect conclusions: TEAL at interpolated 28.5\% actual sparsity yields PPL$\approx$10.7 (vs.\ 10.97 at exact 30\%), a $<$0.3 PPL difference negligible relative to the KL vs.\ TEAL gap (8.96 vs.\ 10.97).
149	
150	
151	\section{Out-of-Distribution Evaluation}
152	\label{app:ood}
153	
154	To address concerns about data homogeneity between training (WikiText-103) and evaluation (WikiText-2), we evaluate on C4~\cite{raffel2020c4} validation set under TEAL global allocation.
155	
156	\begin{table}[h]
157	\centering
158	\caption{Out-of-distribution evaluation on C4 validation (PPL$\downarrow$). 30\% KL reports 2-seed mean$\pm$std; other entries use seed 42.}
159	\label{tab:ood}
160	\small
161	\begin{tabular}{llc}
162	\toprule
163	Sparsity & Method & C4 PPL$\downarrow$ \\
164	\midrule
165	0\% & Dense & 9.21 \\
166	\midrule
167	30\% & KL predictor (Ours) & \textbf{16.03$\pm$0.01} \\ % exp_id: c4_ood_kl30_s42, c4_ood_kl30_s123
168	\midrule
169	\multirow{2}{*}{50\%} & KL predictor (Ours) & \textbf{18.40} \\ % exp_id: eval_c4_ood_kl50
170	& TEAL vanilla & 38.75 \\
171	\bottomrule
172	\end{tabular}
173	\end{table}
174	
175	At the recommended 30\% operating point, the KL predictor achieves C4 PPL 16.03$\pm$0.01 (2-seed, $1.74\times$ dense), confirming OOD generalization at the deployment-relevant sparsity level.
176	At 50\%, the KL predictor achieves 52.5\% relative advantage over TEAL (18.40 vs.\ 38.75), comparable to the 49\% advantage on WikiText-2 (11.79 vs.\ 23.31), confirming that KL-trained predictions generalize across distributions.
177	
178	
179	\section{Per-Layer Retention Analysis}
180	\label{app:retention}
181	
182	\begin{figure}[h]
183	\centering
184	\includegraphics[width=\columnwidth]{per_layer_retention_chart.pdf}
185	\caption{Per-layer neuron retention under global top-$k$ allocation at 30\%, 50\%, and 70\% sparsity. Dashed lines indicate uniform retention baselines. Late layers (L24--31) are consistently starved due to long-tailed activation distributions, with retention dropping to 28.4\% (L31) even at 30\% sparsity. At 70\%, starvation extends to mid-layers (L10--12: 16.7--20.1\%), explaining the transition to the capacity-limited regime.}
186	\label{fig:retention}
187	\end{figure}
188	
189	
190	\section{Training Stability}
191	\label{app:stability}
192	
193	Three-seed evaluation ($s \in \{42, 123, 456\}$) at 50\% sparsity under uniform allocation yields PPL $11.92 \pm 0.07$ (CV=0.6\%); training is stable across random initializations. % exp_id: multi_seed_kl50_uniform
194	Downstream metrics are similarly stable: ARC-c $33.8 \pm 1.2$\%, WinoGrande $62.9 \pm 0.1$\%, MMLU $28.0 \pm 0.6$\%, GSM8K $2.2 \pm 0.1$\%.
195	
196	Under global allocation at 50\%, MMLU is equally stable: $28.1 \pm 0.2$\% (s42=27.89, s123=28.34, s456=27.94); the near-random performance is therefore capacity-limited rather than seed-sensitive ($\sigma$=0.2pp vs.\ 9.5pp at 30\% global). % exp_id: multi_seed_kl50_global
197	The low standard deviation across both allocation strategies indicates that the KL training landscape is well-conditioned for this predictor architecture, with low sensitivity to initialization.
198	
199	
200	\section{Extended SNR Analysis}
201	\label{app:snr_extended}
202	
203	We measure per-layer gradient SNR at 7 checkpoints (steps 0, 50, 100, 150, 200, 250, 300) with 95\% bootstrap confidence intervals.
204	The SNR trajectory is non-monotonic: KL starts with higher SNR at step 0, but BCE surpasses KL during mid-training (steps 100--250) as its per-neuron classification objective concentrates gradients on the remaining hard neurons. KL's advantage re-emerges in later training and reaches $5.14\times$ at convergence (step 300: $5.877{\times}10^{-3}$ vs.\ $1.144{\times}10^{-3}$). % exp_id: snr_extended_r6w3
205	This reversal is consistent with KL's gradient coupling becoming effective only after the predictor has learned a coarse mask structure: early training explores broadly (lower SNR), while convergence concentrates signal through the inter-neuron Jacobian pathway (\S\ref{sec:method:gradient}).
206	
207	
208	\section{Extended Downstream Evaluation}
209	\label{app:downstream}
210	
211	Table~\ref{tab:downstream} compares Dense, KL 30\% (uniform allocation), and TEAL 30\% on three additional downstream benchmarks not included in the main results.
212	
213	\begin{table}[h]
214	\centering
215	\caption{Extended downstream benchmarks at 30\% sparsity (LLaMA-3.1-8B, seed 42). HellaSwag: 10-shot normalized acc; PIQA: 0-shot normalized acc; BoolQ: 0-shot acc.}
216	\label{tab:downstream}
217	\small
218	\begin{tabular}{lccc}
219	\toprule
220	Method & HellaSwag & PIQA & BoolQ \\
221	\midrule
222	Dense & \textbf{82.33} & \textbf{80.74} & \textbf{82.94} \\
223	KL 30\% uniform & 72.70 & 75.95 & 76.85 \\ % exp_id: downstream_extended_kl30_s42
224	TEAL 30\% vanilla & 66.70 & 73.61 & 68.50 \\ % exp_id: downstream_teal30_baseline
225	\bottomrule
226	\end{tabular}
227	\end{table}
228	
229	The KL predictor outperforms TEAL on all three benchmarks. On HellaSwag, it preserves 88.3\% of dense accuracy (72.70 vs.\ 82.33) vs.\ 81.0\% for TEAL (66.70). BoolQ shows the largest gap: 92.7\% vs.\ 82.6\% preservation. PIQA shows a smaller differential (94.1\% vs.\ 91.2\%).
230	
231	
232	\section{Compensation Training Convergence}
233	\label{app:comp_convergence}
234	
235	All compensation networks~\cite{gautam2026fastforward} were trained for 1000 steps (lr=$10^{-4}$, batch size 4, seq length 2048). Training loss plateaus by step 700 across all valid runs: 30\% s42 (final loss 0.70), 30\% s456 (0.68), 50\% s42 (1.07), with fluctuations remaining within 0.08 loss units for the final 300 steps. The compensation network converges but provides no quality improvement over the KL predictor alone, confirming that the redundancy result reflects predictor self-sufficiency rather than insufficient compensation training. % exp_id: kl_comp_30_s42, kl_comp_30_s456, kl_comp_50_s42
236	
237	
238	\section{Qwen-2.5-14B Detailed Results}
239	\label{app:14b}
240	
241	\begin{table}[h]
242	\centering
243	\caption{Qwen-2.5-14B at 30\% sparsity. \textbf{Bold}: best sparse per column per group. BCE collapses to 6.4\% native sparsity (\S\ref{sec:method:gradient}), so forced global top-$k$ is used.}
244	\label{tab:14b}
245	\small
246	\begin{tabular}{lccccc}
247	\toprule
248	Method & PPL$\downarrow$ & ARC-c & WG & MMLU & GSM8K \\
249	\midrule
250	Dense & 5.19 & 67.58 & 81.06 & 79.77 & 87.57 \\
251	\midrule
252	\multicolumn{6}{l}{\emph{Global top-$k$ allocation}} \\
253	KL (Ours) & \textbf{7.62} & 57.17 & 72.06 & 63.72 & 48.82 \\ % exp_id: qwen14b_kl30_s42
254	TEAL & 8.73 & 56.83 & \textbf{72.69} & \textbf{71.83} & 49.51 \\ % exp_id: qwen14b_teal30_eval
255	BCE & 8.76 & \textbf{57.59} & 72.61 & 71.67 & \textbf{53.07} \\ % exp_id: qwen14b_bce30_s42_eval
256	\midrule
257	\multicolumn{6}{l}{\emph{Uniform allocation}} \\
258	KL (Ours) & \textbf{7.63} & 54.44 & \textbf{72.45} & 64.49 & --- \\ % exp_id: qwen14b_kl30_uniform
259	TEAL & 8.01 & \textbf{55.29} & 69.85 & \textbf{66.34} & --- \\ % exp_id: qwen14b_teal30_uniform
260	\bottomrule
261	\end{tabular}
262	\end{table}
263	
264	
265	\section{Cross-Architecture Comparison}
266	\label{app:cross_arch}
267	
268	Table~\ref{tab:cross_arch} evaluates on Mistral-7B-v0.3~\cite{jiang2023mistral} (GQA + sliding window, dense PPL 5.52).
269	
270	\begin{table}[h]
271	\centering
272	\caption{Cross-architecture comparison (WikiText-2 PPL$\downarrow$). Adv = TEAL\,/\,KL ratio. LLaMA uses global top-$k$; Mistral uses uniform allocation (matched within each architecture).}
273	\label{tab:cross_arch}
274	\small
275	\begin{tabular}{l@{\hspace{4pt}}cc@{\hspace{3pt}}c@{\hspace{6pt}}|@{\hspace{6pt}}cc@{\hspace{3pt}}c}
276	\toprule
277	 & \multicolumn{3}{c}{Mistral-7B} & \multicolumn{3}{c}{LLaMA-8B} \\
278	 & KL & TEAL & Adv & KL & TEAL & Adv \\
279	\midrule
280	30\% & \textbf{6.77} & 8.38 & 1.24$\times$ & \textbf{8.96} & 10.97 & 1.22$\times$ \\ % exp_id: kl_30_mistral, teal_30_mistral, kl30_3seed_global
281	50\% & \textbf{8.65} & 18.31 & 2.12$\times$ & \textbf{11.79} & 23.31 & 1.98$\times$ \\ % exp_id: kl_50_mistral, teal_50_mistral
282	70\% & \textbf{13.33} & 61.72 & 4.63$\times$ & \textbf{17.91} & 100.11 & 5.59$\times$ \\ % exp_id: kl_70_mistral, teal_70_mistral
283	\bottomrule
284	\end{tabular}
285	\end{table}
286	
287	The KL advantage ratio is consistent across architectures (within 8\% at $\leq$50\% sparsity), confirming that the benefit of output-distribution coupling is not architecture-specific.
288	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f90ab36d-0a46-4b62-b98f-8056482a6d93",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "02c3602b-cd4c-4ecb-9fbe-1367b6d5c4b1",
  "sourceToolAssistantUUID": "f90ab36d-0a46-4b62-b98f-8056482a6d93",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-18T18:39:00.240Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Ker1tFYobihBeCYn2aci8P`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02c3602b-cd4c-4ecb-9fbe-1367b6d5c4b1",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXCQZR19b63djKfUYFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e9589398-b451-4052-a29b-b072c82193f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FT1GFRiza8BrEfu8VZp9BX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14759,
      "cache_read_input_tokens": 21229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 23 · 2026-05-18T18:39:00.245Z_

<details><summary>↩ Tool result · `toolu_01Ker1tFYobihBeCYn2aci8P`</summary>

```text
1	\section{Conclusion}
2	\label{sec:conclusion}
3	\vspace{-4pt}
4	
5	KL distillation discovers neuron importance patterns that diverge 53\% from magnitude-based masks; a causal ablation confirms target quality, not gradient coupling, as the primary driver.
6	A predictor ($<$1\% of base) halves TEAL's perplexity across 7--14B, rendering compensation (+67.2M params) redundant.
7	At 30\%, uniform allocation delivers $7.5\times$ smaller cross-seed $\sigma$; at 14B, the PPL advantage persists but an MMLU gap emerges, warranting further investigation.
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e9589398-b451-4052-a29b-b072c82193f9",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "940cfef9-8161-4c2e-8cd3-743e4edae101",
  "sourceToolAssistantUUID": "e9589398-b451-4052-a29b-b072c82193f9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-18T18:39:00.539Z_

<details open><summary>🔧 Tool call — Read · `toolu_016Vn7QxeqgQrnPc4WbDuh8E`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "940cfef9-8161-4c2e-8cd3-743e4edae101",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXCQZR19b63djKfUYFd",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "76f296cb-4540-4c07-baad-4d24e4624f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FT1GFRiza8BrEfu8VZp9BX",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14759,
      "cache_read_input_tokens": 21229,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 14759,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 38,
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

_source line 25 · 2026-05-18T18:39:00.544Z_

<details><summary>↩ Tool result · `toolu_016Vn7QxeqgQrnPc4WbDuh8E`</summary>

```text
1	\section*{Limitations}
2	
3	Our primary evaluation uses WikiText-2 perplexity, and downstream benchmarks reveal that perplexity is a poor proxy for reasoning ability at moderate sparsity: 40\% sparsity achieves PPL 8.36 but MMLU already degrades, motivating 30\% as the recommended operating point for downstream fidelity.
4	Training requires 1000 steps on WikiText-103 ($\sim$45 minutes on RTX PRO 6000 for KL, $\sim$17 minutes for BCE), but a separate predictor must be trained for each sparsity target.
5	Our recommended operating point (30\% sparsity, uniform allocation) is validated at 7--8B scale; at 14B, the MMLU gap persists regardless of allocation strategy (\S\ref{sec:14b}). Scaling to 70B remains untested.
6	Out-of-distribution evaluation (Appendix~\ref{app:ood}) covers 30\% and 50\% sparsity on C4; extending to 70\% is left to future work.
7	The causal ablation (\S\ref{sec:mask_analysis}) confirms that mask target quality, not gradient coupling, is the primary driver of KL's advantage. However, the mechanism by which KL's coupled gradient discovers superior mask patterns during training remains incompletely characterized; future work could trace per-layer mask divergence trajectories across training to identify when and where the patterns diverge.
8	At 30\% sparsity, global allocation exhibits 9.5pp cross-seed MMLU standard deviation (3-seed); allocation strategy interacts with predictor initialization in task-specific ways. This variance is MMLU-specific, as ARC, WinoGrande, and GSM8K show stable performance across seeds under both allocation strategies.
9	While we motivate our work with inference speedup potential, actual wall-clock acceleration depends on sparse kernel implementations (e.g., Triton, cuSPARSE) and hardware-specific memory access patterns; this work focuses on prediction quality rather than systems optimization.
10	Future directions include N:M structured sparsity for hardware-native acceleration, scaling to 13B+ models, and training a single predictor that serves multiple sparsity targets simultaneously.
11	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "76f296cb-4540-4c07-baad-4d24e4624f48",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "0f75e53f-ddc2-4034-a933-309d09eadf32",
  "sourceToolAssistantUUID": "76f296cb-4540-4c07-baad-4d24e4624f48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-18T18:39:04.931Z_

<details open><summary>🔧 Tool call — Read · `toolu_01Wmdq6syPeUocQQBzSMSrLP`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f75e53f-ddc2-4034-a933-309d09eadf32",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXCqpCsdYiU9bzzNUfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eafe374e-3988-4dc7-b0fc-0051799b31dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXuhLTphoPhBtF5Pxefb37",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7694,
      "cache_read_input_tokens": 35988,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7694,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 39,
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

_source line 27 · 2026-05-18T18:39:04.937Z_

<details><summary>↩ Tool result · `toolu_01Wmdq6syPeUocQQBzSMSrLP`</summary>

```text
1	% =============================================================================
2	% Direction 1: KL distillation for structured/activation sparsity
3	% =============================================================================
4	
5	@inproceedings{fang2024maskllm,
6	  title = {MaskLLM: Learnable Semi-Structured Sparsity for Large Language Models},
7	  author = {Gongfan Fang and Hongxu Yin and Saurav Muralidharan and Greg Heinrich and Jeff Pool and Jan Kautz and Pavlo Molchanov and Xinchao Wang},
8	  year = {2024},
9	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
10	  url = {https://arxiv.org/abs/2409.17481},
11	}
12	
13	@inproceedings{xu2026spon,
14	  title = {Resting Neurons, Active Insights: Robustify Activation Sparsity for Large Language Models},
15	  author = {Haotian Xu and Jiannan Yang and Tian Gao and Tsui-Wei Weng and Tengfei Ma},
16	  year = {2025},
17	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
18	  url = {https://arxiv.org/abs/2512.12744},
19	}
20	
21	@inproceedings{muralidharan2024minitron,
22	  title = {Compact Language Models via Pruning and Knowledge Distillation},
23	  author = {Saurav Muralidharan and Sharath Turuvekere Sreenivas and Raviraj Joshi and Marcin Chochowski and Mostofa Patwary and Mohammad Shoeybi and Bryan Catanzaro and Jan Kautz and Pavlo Molchanov},
24	  year = {2024},
25	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
26	  url = {https://arxiv.org/abs/2407.14679},
27	}
28	
29	
30	% =============================================================================
31	% Direction 3: SPON and learnable bias correction for sparsity
32	% =============================================================================
33	
34	@article{gautam2026fastforward,
35	  title = {Fast Forward: Accelerating LLM Prefill with Predictive FFN Sparsity},
36	  author = {Aayush Gautam and Mukul Gagrani and Junyoung Park and Mingu Lee and Chiris Lott and Narasimha Reddy},
37	  year = {2026},
38	  journal = {arXiv preprint arXiv:2602.00397},
39	  url = {https://arxiv.org/abs/2602.00397},
40	}
41	
42	
43	% =============================================================================
44	% Direction 4: Predictor-based activation sparsity
45	% =============================================================================
46	
47	@inproceedings{liu2025teal,
48	  title = {Training-Free Activation Sparsity in Large Language Models},
49	  author = {James Liu and Pragaash Ponnusamy and Tianle Cai and Han Guo and Yoon Kim and Ben Athiwaratkun},
50	  year = {2025},
51	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
52	  url = {https://arxiv.org/abs/2408.14690},
53	}
54	
55	@inproceedings{liu2023dejavu,
56	  title = {Deja Vu: Contextual Sparsity for Efficient LLMs at Inference Time},
57	  author = {Zichang Liu and Jue Wang and Tri Dao and Tianyi Zhou and Binhang Yuan and Zhao Song and Anshumali Shrivastava and Ce Zhang and Yuandong Tian and Christopher Re and Beidi Chen},
58	  year = {2023},
59	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
60	  url = {https://arxiv.org/abs/2310.17157},
61	}
62	
63	@inproceedings{akhauri2024shadowllm,
64	  title = {ShadowLLM: Predictor-based Contextual Sparsity for Large Language Models},
65	  author = {Yash Akhauri and Ahmed F AbouElhamayed and Jordan Dotzel and Zhiru Zhang and Alexander M Rush and Safeen Huda and Mohamed S Abdelfattah},
66	  year = {2024},
67	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
68	  url = {https://arxiv.org/abs/2406.16635},
69	}
70	
71	
72	@article{lee2024cats,
73	  title = {CATS: Contextually-Aware Thresholding for Sparsity in Large Language Models},
74	  author = {Donghyun Lee and Je-Yong Lee and Genghan Zhang and Mo Tiwari and Azalia Mirhoseini},
75	  year = {2024},
76	  journal = {arXiv preprint arXiv:2404.08763},
77	  url = {https://arxiv.org/abs/2404.08763},
78	}
79	
80	@inproceedings{zhang2025rsparse,
81	  title = {R-Sparse: Rank-Aware Activation Sparsity for Efficient LLM Inference},
82	  author = {Zhenyu Zhang and Zechun Liu and Yuandong Tian and Harshit Khaitan and Zhangyang Wang and Steven Li},
83	  year = {2025},
84	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
85	  url = {https://arxiv.org/abs/2504.19449},
86	}
87	
88	@inproceedings{federici2025dip,
89	  title = {Efficient LLM Inference using Dynamic Input Pruning and Cache-Aware Masking},
90	  author = {Marco Federici and Davide Belli and Mart van Baalen and Amir Jalalirad and Andrii Skliar and Bence Major and Markus Nagel and Paul Whatmough},
91	  year = {2024},
92	  booktitle = {Proceedings of Machine Learning and Systems (MLSys)},
93	  url = {https://arxiv.org/abs/2412.01380},
94	}
95	
96	@inproceedings{shin2025sparseinfer,
97	  title = {SparseInfer: Training-free Prediction of Activation Sparsity for Fast LLM Inference},
98	  author = {Jiho Shin and Hoeseok Yang and Youngmin Yi},
99	  year = {2025},
100	  booktitle = {Proceedings of the Design, Automation \& Test in Europe Conference (DATE)},
101	  url = {https://arxiv.org/abs/2411.12692},
102	}
103	
104	@article{serbin2026svdcsp,
105	  title = {SVD Contextual Sparsity Predictors for Fast LLM Inference},
106	  author = {Georgii Serbin and Kirill Koshkin and Zhongao Sun and Anastasiya Bistrigova and C.C. Korikov},
107	  year = {2026},
108	  journal = {arXiv preprint arXiv:2603.14110},
109	  url = {https://arxiv.org/abs/2603.14110},
110	}
111	
112	% =============================================================================
113	% Activation function replacement and sparsity enhancement
114	% =============================================================================
115	
116	@inproceedings{mirzadeh2024relu,
117	  title = {ReLU Strikes Back: Exploiting Activation Sparsity in Large Language Models},
118	  author = {Iman Mirzadeh and Keivan Alizadeh and Sachin Mehta and Carlo C Del Mundo and Oncel Tuzel and Golnoosh Samei and Mohammad Rastegari and Mehrdad Farajtabar},
119	  year = {2024},
120	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
121	  url = {https://arxiv.org/abs/2310.04564},
122	}
123	
124	@article{song2024turbosparse,
125	  title = {Turbo Sparse: Achieving LLM SOTA Performance with Minimal Activated Parameters},
126	  author = {Yixin Song and Haotong Xie and Zhengyan Zhang and Bo Wen and Li Ma and Zeyu Mi and Haibo Chen},
127	  year = {2024},
128	  journal = {arXiv preprint arXiv:2406.05955},
129	  url = {https://arxiv.org/abs/2406.05955},
130	}
131	
132	@inproceedings{song2025prosparse,
133	  title = {ProSparse: Introducing and Enhancing Intrinsic Activation Sparsity within Large Language Models},
134	  author = {Chenyang Song and Xu Han and Zhengyan Zhang and Shengding Hu and Xiyu Shi and Kuai Li and Chen Chen and Zhiyuan Liu and Guangli Li and Tao Yang and Maosong Sun},
135	  year = {2025},
136	  booktitle = {Proceedings of the International Conference on Computational Linguistics (COLING)},
137	  url = {https://arxiv.org/abs/2402.13516},
138	}
139	
140	@article{luo2024sparsinglaw,
141	  title = {Sparsing Law: Towards Large Language Models with Greater Activation Sparsity},
142	  author = {Yuqi Luo and Chenyang Song and Xu Han and Yingfa Chen and Chaojun Xiao and Xiaojun Meng and Liqun Deng and Jiansheng Wei and Zhiyuan Liu and Maosong Sun},
143	  year = {2024},
144	  journal = {arXiv preprint arXiv:2411.02335},
145	  url = {https://arxiv.org/abs/2411.02335},
146	}
147	
148	
149	@inproceedings{song2024powerinfer,
150	  title = {PowerInfer: Fast Large Language Model Serving with a Consumer-grade GPU},
151	  author = {Yixin Song and Zeyu Mi and Haotong Xie and Haibo Chen},
152	  year = {2024},
153	  booktitle = {Proceedings of the ACM Symposium on Operating Systems Principles (SOSP)},
154	  url = {https://arxiv.org/abs/2312.12456},
155	}
156	
157	
158	% =============================================================================
159	% KL distillation and knowledge distillation
160	% =============================================================================
161	
162	@inproceedings{kim2016sequencekd,
163	  title = {Sequence-Level Knowledge Distillation},
164	  author = {Yoon Kim and Alexander M. Rush},
165	  year = {2016},
166	  booktitle = {Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP)},
167	  url = {https://arxiv.org/abs/1606.07947},
168	}
169	
170	@inproceedings{gu2024minillm,
171	  title = {MiniLLM: Knowledge Distillation of Large Language Models},
172	  author = {Yuxian Gu and Li Dong and Furu Wei and Minlie Huang},
173	  year = {2024},
174	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
175	  url = {https://openreview.net/forum?id=5h0qf7IBZZ},
176	}
177	
178	@inproceedings{agarwal2024gkd,
179	  title = {On-Policy Distillation of Language Models: Learning from Self-Generated Mistakes},
180	  author = {Rishabh Agarwal and Nino Vieillard and Yongchao Zhou and Piotr Stanczyk and Sabela Ramos and Matthieu Geist and Olivier Bachem},
181	  year = {2024},
182	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
183	  url = {https://openreview.net/forum?id=3zKtaqxLhW},
184	}
185	
186	@inproceedings{khaki2025sparselora,
187	  title = {SparseLoRA: Accelerating LLM Fine-Tuning with Contextual Sparsity},
188	  author = {Samir Khaki and Xiuyu Li and Junxian Guo and Ligeng Zhu and Konstantinos N. Plataniotis and Amir Yazdanbakhsh and Kurt Keutzer and Song Han and Zhijian Liu},
189	  year = {2025},
190	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
191	  url = {https://proceedings.mlr.press/v267/khaki25a.html},
192	}
193	
194	@article{raposo2024mod,
195	  title = {Mixture-of-Depths: Dynamically allocating compute in transformer-based language models},
196	  author = {David Raposo and Sam Ritter and Blake Richards and Timothy Lillicrap and Peter Conway Humphreys and Adam Santoro},
197	  year = {2024},
198	  journal = {arXiv preprint arXiv:2404.02258},
199	  url = {https://arxiv.org/abs/2404.02258},
200	}
201	
202	@article{sanh2019distilbert,
203	  title = {DistilBERT, a distilled version of BERT: smaller, faster, cheaper and lighter},
204	  author = {Victor Sanh and Lysandre Debut and Julien Chaumond and Thomas Wolf},
205	  year = {2019},
206	  journal = {arXiv preprint arXiv:1910.01108},
207	  url = {https://arxiv.org/abs/1910.01108},
208	}
209	
210	% =============================================================================
211	% Weight pruning methods
212	% =============================================================================
213	
214	@inproceedings{sun2024wanda,
215	  title = {A Simple and Effective Pruning Approach for Large Language Models},
216	  author = {Mingjie Sun and Zhuang Liu and Anna Bair and J. Zico Kolter},
217	  year = {2024},
218	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
219	  url = {https://arxiv.org/abs/2306.11695},
220	}
221	
222	@inproceedings{frantar2023sparsegpt,
223	  title = {SparseGPT: Massive Language Models Can Be Accurately Pruned in One-Shot},
224	  author = {Elias Frantar and Dan Alistarh},
225	  year = {2023},
226	  booktitle = {Proceedings of the International Conference on Machine Learning (ICML)},
227	  url = {https://arxiv.org/abs/2301.00774},
228	}
229	
230	% =============================================================================
231	% Conditional computation and MoE
232	% =============================================================================
233	
234	@inproceedings{szatkowski2024d2dmoe,
235	  title = {Exploiting Activation Sparsity with Dense to Dynamic-$k$ Mixture-of-Experts Conversion},
236	  author = {Filip Szatkowski and Bartosz W{\'o}jcik and Miko{\l}aj Pi{\'o}rczy{\'n}ski and Simone Scardapane},
237	  year = {2024},
238	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
239	  volume = {37},
240	  url = {https://arxiv.org/abs/2310.04361},
241	}
242	
243	@article{fedus2022switch,
244	  title = {Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity},
245	  author = {William Fedus and Barret Zoph and Noam Shazeer},
246	  year = {2022},
247	  journal = {Journal of Machine Learning Research},
248	  volume = {23},
249	  number = {120},
250	  pages = {1--40},
251	  url = {https://arxiv.org/abs/2101.03961},
252	}
253	
254	% =============================================================================
255	% MoE routing and gated architectures
256	% =============================================================================
257	
258	@inproceedings{zhou2022expertchoice,
259	  title = {Mixture-of-Experts with Expert Choice Routing},
260	  author = {Yanqi Zhou and Tao Lei and Hanxiao Liu and Nan Du and Yanping Huang and Vincent Zhao and Andrew M. Dai and Zhifeng Chen and Quoc V. Le and James Laudon},
261	  year = {2022},
262	  booktitle = {Advances in Neural Information Processing Systems (NeurIPS)},
263	  volume = {35},
264	  url = {https://arxiv.org/abs/2202.09368},
265	}
266	
267	@article{de2024griffin,
268	  title = {Griffin: Mixing Gated Linear Recurrences with Local Attention for Efficient Language Models},
269	  author = {Soham De and Samuel L. Smith and Anushan Fernando and Aleksandar Botev and George Cristian-Muraru and Albert Gu and Ruba Haroun and Leonard Berrada and Yutian Chen and Srivatsan Srinivasan and Guillaume Desjardins and Arnaud Doucet and David Budden and Yee Whye Teh and Razvan Pascanu and Nando De Freitas and Caglar Gulcehre},
270	  year = {2024},
271	  journal = {arXiv preprint arXiv:2402.19427},
272	  url = {https://arxiv.org/abs/2402.19427},
273	}
274	
275	
276	% =============================================================================
277	% Relaxation methods (Gumbel/Concrete)
278	% =============================================================================
279	
280	@inproceedings{louizos2018l0,
281	  title = {Learning Sparse Neural Networks through $L_0$ Regularization},
282	  author = {Christos Louizos and Max Welling and Diederik P. Kingma},
283	  year = {2018},
284	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
285	  url = {https://arxiv.org/abs/1712.01312},
286	}
287	
288	@inproceedings{maddison2017concrete,
289	  title = {The Concrete Distribution: A Continuous Relaxation of Discrete Random Variables},
290	  author = {Chris J. Maddison and Andriy Mnih and Yee Whye Teh},
291	  year = {2017},
292	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
293	  url = {https://arxiv.org/abs/1611.00712},
294	}
295	
296	% =============================================================================
297	% Foundational references
298	% =============================================================================
299	
300	@article{grattafiori2024llama3,
301	  title = {The Llama 3 Herd of Models},
302	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and Abhinav Pandey and Abhishek Kadian and Ahmad Al-Dahle and Aieleen Lakber and Aimin Chen and Ait Mokhtar Salma and Ajay Menon},
303	  year = {2024},
304	  journal = {arXiv preprint arXiv:2407.21783},
305	  url = {https://arxiv.org/abs/2407.21783},
306	}
307	
308	@article{qwen2024qwen25,
309	  title = {Qwen2.5 Technical Report},
310	  author = {Qwen Team},
311	  year = {2024},
312	  journal = {arXiv preprint arXiv:2412.15115},
313	  url = {https://arxiv.org/abs/2412.15115},
314	}
315	
316	@article{jiang2023mistral,
317	  title = {Mistral 7B},
318	  author = {Albert Q. Jiang and Alexandre Sablayrolles and Arthur Mensch and Chris Bamford and Devendra Singh Chaplot and Diego de las Casas and Florian Bressand and Gianna Lengyel and Guillaume Lample and Lucile Saulnier},
319	  year = {2023},
320	  journal = {arXiv preprint arXiv:2310.06825},
321	  url = {https://arxiv.org/abs/2310.06825},
322	}
323	
324	@inproceedings{jang2017gumbel,
325	  title = {Categorical Reparameterization with Gumbel-Softmax},
326	  author = {Eric Jang and Shixiang Gu and Ben Poole},
327	  year = {2017},
328	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
329	  url = {https://arxiv.org/abs/1611.01144},
330	}
331	
332	@article{shazeer2020glu,
333	  title = {GLU Variants Improve Transformer},
334	  author = {Noam Shazeer},
335	  year = {2020},
336	  journal = {arXiv preprint arXiv:2002.05202},
337	  url = {https://arxiv.org/abs/2002.05202},
338	}
339	
340	@inproceedings{merity2017pointer,
341	  title = {Pointer Sentinel Mixture Models},
342	  author = {Stephen Merity and Caiming Xiong and James Bradbury and Richard Socher},
343	  year = {2017},
344	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
345	  url = {https://arxiv.org/abs/1609.07843},
346	}
347	
348	@inproceedings{hinton2015distilling,
349	  title = {Distilling the Knowledge in a Neural Network},
350	  author = {Geoffrey Hinton and Oriol Vinyals and Jeff Dean},
351	  year = {2015},
352	  booktitle = {NeurIPS 2014 Deep Learning Workshop},
353	  url = {https://arxiv.org/abs/1503.02531},
354	}
355	
356	@article{bengio2013ste,
357	  title = {Estimating or Propagating Gradients Through Stochastic Neurons for Conditional Computation},
358	  author = {Yoshua Bengio and Nicholas L\'{e}onard and Aaron Courville},
359	  year = {2013},
360	  journal = {arXiv preprint arXiv:1308.3432},
361	  url = {https://arxiv.org/abs/1308.3432},
362	}
363	
364	@inproceedings{loshchilov2019adamw,
365	  title = {Decoupled Weight Decay Regularization},
366	  author = {Ilya Loshchilov and Frank Hutter},
367	  year = {2019},
368	  booktitle = {Proceedings of the International Conference on Learning Representations (ICLR)},
369	  url = {https://arxiv.org/abs/1711.05101},
370	}
371	
372	@article{raffel2020c4,
373	  title = {Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer},
374	  author = {Colin Raffel and Noam Shazeer and Adam Roberts and Katherine Lee and Sharan Narang and Michael Matena and Yanqi Zhou and Wei Li and Peter J. Liu},
375	  year = {2020},
376	  journal = {Journal of Machine Learning Research},
377	  volume = {21},
378	  number = {140},
379	  pages = {1--67},
380	  url = {https://arxiv.org/abs/1910.10683},
381	}
382	
383	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eafe374e-3988-4dc7-b0fc-0051799b31dd",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "ed5ae4e3-62e0-4a94-9ab1-8a8e97637f78",
  "sourceToolAssistantUUID": "eafe374e-3988-4dc7-b0fc-0051799b31dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-18T18:39:05.399Z_

<details open><summary>🔧 Tool call — Read · `toolu_01MP5z64pf4MCwMnn9Q42bFi`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ed5ae4e3-62e0-4a94-9ab1-8a8e97637f78",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXCqpCsdYiU9bzzNUfH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "534636d7-000d-4d44-b035-6f57b29cc744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PXuhLTphoPhBtF5Pxefb37",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7694,
      "cache_read_input_tokens": 35988,
      "output_tokens": 160,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7694
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 160,
          "cache_read_input_tokens": 35988,
          "cache_creation_input_tokens": 7694,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7694,
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

_source line 29 · 2026-05-18T18:39:05.404Z_

<details><summary>↩ Tool result · `toolu_01MP5z64pf4MCwMnn9Q42bFi`</summary>

```text
1	\section*{Ethics Statement}
2	
3	This work proposes a training method for sparsity predictors in pretrained language models, evaluated on publicly available models (LLaMA-3.1-8B, Mistral-7B-v0.3) and standard benchmarks (WikiText-2, WikiText-103, C4, ARC, WinoGrande, MMLU, GSM8K).
4	No new data collection, annotation, or human subjects are involved.
5	The method does not alter model outputs beyond the sparsity-induced degradation we analyze; it introduces no new generation capabilities or safety risks beyond those inherent in the base models.
6	Compute requirements are modest (1000 training steps, $\sim$45 minutes on a single GPU for KL training), presenting minimal environmental concern relative to the pretrained models we evaluate on.
7	We release no model weights or user-facing systems; our contribution is analytical (understanding KL distillation for sparsity) rather than deployment-oriented.
8	
9	\section*{Responsible NLP Research Checklist}
10	
11	\paragraph{A. Limitations and Risks.}
12	\begin{itemize}[nosep,leftmargin=*]
13	\item[\textbf{A1.}] Limitations are discussed in the Limitations section. Key limitations: evaluation limited to 7--8B models; perplexity is an imperfect proxy for downstream quality; wall-clock speedup requires sparse kernel support not implemented here.
14	\item[\textbf{A2.}] No foreseeable risks specific to this work beyond those inherent in the base language models. The method does not enable new capabilities or applications.
15	\end{itemize}
16	
17	\paragraph{B. Scientific Artifacts.}
18	\begin{itemize}[nosep,leftmargin=*]
19	\item[\textbf{B1.}] Yes. All models (LLaMA-3.1-8B~\cite{grattafiori2024llama3}, Mistral-7B-v0.3~\cite{jiang2023mistral}), datasets (WikiText~\cite{merity2017pointer}, C4~\cite{raffel2020c4}), and methods (TEAL~\cite{liu2025teal}, SPON~\cite{xu2026spon}) are cited with original references.
20	\item[\textbf{B2.}] LLaMA-3.1 is released under the Llama 3.1 Community License; Mistral-7B under Apache 2.0. WikiText and C4 are publicly available research datasets. Our use is consistent with their intended purposes.
21	\item[\textbf{B3.}] N/A. We do not release new artifacts in this submission.
22	\item[\textbf{B4.}] N/A. No personally identifiable information or offensive content is involved.
23	\item[\textbf{B5.}] N/A. No new datasets created.
24	\item[\textbf{B6.}] N/A. No crowdsourced data.
25	\end{itemize}
26	
27	\paragraph{C. Computational Experiments.}
28	\begin{itemize}[nosep,leftmargin=*]
29	\item[\textbf{C1.}] Yes. Model sizes (8B base, 75.9M predictor), training compute (1000 steps, batch 4, seq 2048), optimizer (AdamW~\cite{loshchilov2019adamw}, lr=$10^{-3}$, cosine decay), and GPU (NVIDIA RTX PRO 6000 Blackwell for both training and latency measurement) are reported in \S4.1 and Appendix A.
30	\item[\textbf{C2.}] Yes. Hyperparameters are fully specified: bottleneck $d_b{=}128$, temperature schedule $\tau: 1.0 \to 0.1$, sparsity penalty parameters ($\epsilon{=}0.02$, $\lambda_{\max}$), weight decay $5{\times}10^{-2}$.
31	\item[\textbf{C3.}] Yes. Three-seed evaluation reported (PPL std=0.07, CV$<$1\%; Appendix E).
32	\item[\textbf{C4.}] Yes. All evaluation uses established metrics (perplexity, accuracy) on standard benchmarks with standard few-shot protocols (ARC 25-shot, WinoGrande 5-shot, MMLU 5-shot, GSM8K 8-shot).
33	\end{itemize}
34	
35	\paragraph{D. Human Subjects.}
36	\begin{itemize}[nosep,leftmargin=*]
37	\item[\textbf{D1--D5.}] N/A. No human subjects, crowdsourcing, or annotation involved.
38	\end{itemize}
39	
40	\paragraph{E. AI Assistants.}
41	\begin{itemize}[nosep,leftmargin=*]
42	\item[\textbf{E1.}] AI writing assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were produced and verified by the authors.
43	\end{itemize}
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "534636d7-000d-4d44-b035-6f57b29cc744",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "9e104f12-0879-4cb2-a1a4-a92b03cbd3ff",
  "sourceToolAssistantUUID": "534636d7-000d-4d44-b035-6f57b29cc744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 30 · 2026-05-18T18:39:08.763Z_

Now let me check for figures and the compiled PDF state.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9e104f12-0879-4cb2-a1a4-a92b03cbd3ff",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXDBTQ6SrJE75rdWiPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "dfffbeda-1436-42a3-b35b-7ad84532f946",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHxZ7JnRTZiLWma6QLuYPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8116,
      "cache_read_input_tokens": 43682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8116,
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

_source line 31 · 2026-05-18T18:39:10.657Z_

<details open><summary>🔧 Tool call — Glob · `toolu_011oBTEKXRYt6Jw89kYuFoBg`</summary>

```json
{
  "pattern": "figures/paper/**/*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dfffbeda-1436-42a3-b35b-7ad84532f946",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXDBTQ6SrJE75rdWiPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f1baab88-cdf9-4d2f-958f-fbc8df41d153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHxZ7JnRTZiLWma6QLuYPV",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8116,
      "cache_read_input_tokens": 43682,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8116,
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

### Tool result

_source line 32 · 2026-05-18T18:39:10.693Z_

<details><summary>↩ Tool result · `toolu_011oBTEKXRYt6Jw89kYuFoBg`</summary>

```text
figures/paper/fig1_overview.pdf
figures/paper/fig1_overview.png
figures/paper/gen_fig3.py
figures/paper/fig3_subsumption.pdf
figures/paper/fig3_subsumption.png
figures/paper/gen_fig2.py
figures/paper/fig2_sparsity_sweep.pdf
figures/paper/fig2_sparsity_sweep.png
figures/paper/lagrangian_dynamics.pdf
figures/paper/per_layer_retention_chart.pdf
figures/paper/per_layer_retention_chart.png
figures/paper/gen_gradient_snr.py
figures/paper/gradient_snr_comparison.pdf
figures/paper/gradient_snr_comparison.png
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f1baab88-cdf9-4d2f-958f-fbc8df41d153",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "c0db34fc-2b39-4c7f-a6f1-5821bc86a186",
  "sourceToolAssistantUUID": "f1baab88-cdf9-4d2f-958f-fbc8df41d153",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 33 · 2026-05-18T18:39:11.227Z_

<details open><summary>🔧 Tool call — Read · `toolu_014BT4yFbittt8h64MxHc6F6`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/main.bbl"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c0db34fc-2b39-4c7f-a6f1-5821bc86a186",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXDBTQ6SrJE75rdWiPN",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2eab6bdf-fed9-432f-9897-c2ae452492bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QHxZ7JnRTZiLWma6QLuYPV",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8116,
      "cache_read_input_tokens": 43682,
      "output_tokens": 187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8116
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 187,
          "cache_read_input_tokens": 43682,
          "cache_creation_input_tokens": 8116,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8116,
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

_source line 34 · 2026-05-18T18:39:11.233Z_

<details><summary>↩ Tool result · `toolu_014BT4yFbittt8h64MxHc6F6`</summary>

```text
1	\begin{thebibliography}{41}
2	\providecommand{\natexlab}[1]{#1}
3	
4	\bibitem[{Agarwal et~al.(2024)Agarwal, Vieillard, Zhou, Stanczyk, Ramos, Geist,
5	  and Bachem}]{agarwal2024gkd}
6	Rishabh Agarwal, Nino Vieillard, Yongchao Zhou, Piotr Stanczyk, Sabela Ramos,
7	  Matthieu Geist, and Olivier Bachem. 2024.
8	\newblock \href {https://openreview.net/forum?id=3zKtaqxLhW} {On-policy
9	  distillation of language models: Learning from self-generated mistakes}.
10	\newblock In \emph{Proceedings of the International Conference on Learning
11	  Representations (ICLR)}.
12	
13	\bibitem[{Akhauri et~al.(2024)Akhauri, AbouElhamayed, Dotzel, Zhang, Rush,
14	  Huda, and Abdelfattah}]{akhauri2024shadowllm}
15	Yash Akhauri, Ahmed~F AbouElhamayed, Jordan Dotzel, Zhiru Zhang, Alexander~M
16	  Rush, Safeen Huda, and Mohamed~S Abdelfattah. 2024.
17	\newblock \href {https://arxiv.org/abs/2406.16635} {Shadowllm: Predictor-based
18	  contextual sparsity for large language models}.
19	\newblock In \emph{Proceedings of the Conference on Empirical Methods in
20	  Natural Language Processing (EMNLP)}.
21	
22	\bibitem[{Bengio et~al.(2013)Bengio, L\'{e}onard, and
23	  Courville}]{bengio2013ste}
24	Yoshua Bengio, Nicholas L\'{e}onard, and Aaron Courville. 2013.
25	\newblock \href {https://arxiv.org/abs/1308.3432} {Estimating or propagating
26	  gradients through stochastic neurons for conditional computation}.
27	\newblock \emph{arXiv preprint arXiv:1308.3432}.
28	
29	\bibitem[{De et~al.(2024)De, Smith, Fernando, Botev, Cristian-Muraru, Gu,
30	  Haroun, Berrada, Chen, Srinivasan, Desjardins, Doucet, Budden, Teh, Pascanu,
31	  Freitas, and Gulcehre}]{de2024griffin}
32	Soham De, Samuel~L. Smith, Anushan Fernando, Aleksandar Botev, George
33	  Cristian-Muraru, Albert Gu, Ruba Haroun, Leonard Berrada, Yutian Chen,
34	  Srivatsan Srinivasan, Guillaume Desjardins, Arnaud Doucet, David Budden,
35	  Yee~Whye Teh, Razvan Pascanu, Nando~De Freitas, and Caglar Gulcehre. 2024.
36	\newblock \href {https://arxiv.org/abs/2402.19427} {Griffin: Mixing gated
37	  linear recurrences with local attention for efficient language models}.
38	\newblock \emph{arXiv preprint arXiv:2402.19427}.
39	
40	\bibitem[{Fang et~al.(2024)Fang, Yin, Muralidharan, Heinrich, Pool, Kautz,
41	  Molchanov, and Wang}]{fang2024maskllm}
42	Gongfan Fang, Hongxu Yin, Saurav Muralidharan, Greg Heinrich, Jeff Pool, Jan
43	  Kautz, Pavlo Molchanov, and Xinchao Wang. 2024.
44	\newblock \href {https://arxiv.org/abs/2409.17481} {Maskllm: Learnable
45	  semi-structured sparsity for large language models}.
46	\newblock In \emph{Advances in Neural Information Processing Systems
47	  (NeurIPS)}.
48	
49	\bibitem[{Federici et~al.(2024)Federici, Belli, van Baalen, Jalalirad, Skliar,
50	  Major, Nagel, and Whatmough}]{federici2025dip}
51	Marco Federici, Davide Belli, Mart van Baalen, Amir Jalalirad, Andrii Skliar,
52	  Bence Major, Markus Nagel, and Paul Whatmough. 2024.
53	\newblock \href {https://arxiv.org/abs/2412.01380} {Efficient llm inference
54	  using dynamic input pruning and cache-aware masking}.
55	\newblock In \emph{Proceedings of Machine Learning and Systems (MLSys)}.
56	
57	\bibitem[{Fedus et~al.(2022)Fedus, Zoph, and Shazeer}]{fedus2022switch}
58	William Fedus, Barret Zoph, and Noam Shazeer. 2022.
59	\newblock \href {https://arxiv.org/abs/2101.03961} {Switch transformers:
60	  Scaling to trillion parameter models with simple and efficient sparsity}.
61	\newblock \emph{Journal of Machine Learning Research}, 23(120):1--40.
62	
63	\bibitem[{Frantar and Alistarh(2023)}]{frantar2023sparsegpt}
64	Elias Frantar and Dan Alistarh. 2023.
65	\newblock \href {https://arxiv.org/abs/2301.00774} {Sparsegpt: Massive language
66	  models can be accurately pruned in one-shot}.
67	\newblock In \emph{Proceedings of the International Conference on Machine
68	  Learning (ICML)}.
69	
70	\bibitem[{Gautam et~al.(2026)Gautam, Gagrani, Park, Lee, Lott, and
71	  Reddy}]{gautam2026fastforward}
72	Aayush Gautam, Mukul Gagrani, Junyoung Park, Mingu Lee, Chiris Lott, and
73	  Narasimha Reddy. 2026.
74	\newblock \href {https://arxiv.org/abs/2602.00397} {Fast forward: Accelerating
75	  llm prefill with predictive ffn sparsity}.
76	\newblock \emph{arXiv preprint arXiv:2602.00397}.
77	
78	\bibitem[{Grattafiori et~al.(2024)Grattafiori, Dubey, Jauhri, Pandey, Kadian,
79	  Al-Dahle, Lakber, Chen, Salma, and Menon}]{grattafiori2024llama3}
80	Aaron Grattafiori, Abhimanyu Dubey, Abhinav Jauhri, Abhinav Pandey, Abhishek
81	  Kadian, Ahmad Al-Dahle, Aieleen Lakber, Aimin Chen, Ait~Mokhtar Salma, and
82	  Ajay Menon. 2024.
83	\newblock \href {https://arxiv.org/abs/2407.21783} {The llama 3 herd of
84	  models}.
85	\newblock \emph{arXiv preprint arXiv:2407.21783}.
86	
87	\bibitem[{Gu et~al.(2024)Gu, Dong, Wei, and Huang}]{gu2024minillm}
88	Yuxian Gu, Li~Dong, Furu Wei, and Minlie Huang. 2024.
89	\newblock \href {https://openreview.net/forum?id=5h0qf7IBZZ} {Minillm:
90	  Knowledge distillation of large language models}.
91	\newblock In \emph{Proceedings of the International Conference on Learning
92	  Representations (ICLR)}.
93	
94	\bibitem[{Hinton et~al.(2015)Hinton, Vinyals, and Dean}]{hinton2015distilling}
95	Geoffrey Hinton, Oriol Vinyals, and Jeff Dean. 2015.
96	\newblock \href {https://arxiv.org/abs/1503.02531} {Distilling the knowledge in
97	  a neural network}.
98	\newblock In \emph{NeurIPS 2014 Deep Learning Workshop}.
99	
100	\bibitem[{Jang et~al.(2017)Jang, Gu, and Poole}]{jang2017gumbel}
101	Eric Jang, Shixiang Gu, and Ben Poole. 2017.
102	\newblock \href {https://arxiv.org/abs/1611.01144} {Categorical
103	  reparameterization with gumbel-softmax}.
104	\newblock In \emph{Proceedings of the International Conference on Learning
105	  Representations (ICLR)}.
106	
107	\bibitem[{Jiang et~al.(2023)Jiang, Sablayrolles, Mensch, Bamford, Chaplot,
108	  de~las Casas, Bressand, Lengyel, Lample, and Saulnier}]{jiang2023mistral}
109	Albert~Q. Jiang, Alexandre Sablayrolles, Arthur Mensch, Chris Bamford,
110	  Devendra~Singh Chaplot, Diego de~las Casas, Florian Bressand, Gianna Lengyel,
111	  Guillaume Lample, and Lucile Saulnier. 2023.
112	\newblock \href {https://arxiv.org/abs/2310.06825} {Mistral 7b}.
113	\newblock \emph{arXiv preprint arXiv:2310.06825}.
114	
115	\bibitem[{Khaki et~al.(2025)Khaki, Li, Guo, Zhu, Plataniotis, Yazdanbakhsh,
116	  Keutzer, Han, and Liu}]{khaki2025sparselora}
117	Samir Khaki, Xiuyu Li, Junxian Guo, Ligeng Zhu, Konstantinos~N. Plataniotis,
118	  Amir Yazdanbakhsh, Kurt Keutzer, Song Han, and Zhijian Liu. 2025.
119	\newblock \href {https://proceedings.mlr.press/v267/khaki25a.html} {Sparselora:
120	  Accelerating llm fine-tuning with contextual sparsity}.
121	\newblock In \emph{Proceedings of the International Conference on Machine
122	  Learning (ICML)}.
123	
124	\bibitem[{Kim and Rush(2016)}]{kim2016sequencekd}
125	Yoon Kim and Alexander~M. Rush. 2016.
126	\newblock \href {https://arxiv.org/abs/1606.07947} {Sequence-level knowledge
127	  distillation}.
128	\newblock In \emph{Proceedings of the Conference on Empirical Methods in
129	  Natural Language Processing (EMNLP)}.
130	
131	\bibitem[{Lee et~al.(2024)Lee, Lee, Zhang, Tiwari, and
132	  Mirhoseini}]{lee2024cats}
133	Donghyun Lee, Je-Yong Lee, Genghan Zhang, Mo~Tiwari, and Azalia Mirhoseini.
134	  2024.
135	\newblock \href {https://arxiv.org/abs/2404.08763} {Cats: Contextually-aware
136	  thresholding for sparsity in large language models}.
137	\newblock \emph{arXiv preprint arXiv:2404.08763}.
138	
139	\bibitem[{Liu et~al.(2025)Liu, Ponnusamy, Cai, Guo, Kim, and
140	  Athiwaratkun}]{liu2025teal}
141	James Liu, Pragaash Ponnusamy, Tianle Cai, Han Guo, Yoon Kim, and Ben
142	  Athiwaratkun. 2025.
143	\newblock \href {https://arxiv.org/abs/2408.14690} {Training-free activation
144	  sparsity in large language models}.
145	\newblock In \emph{Proceedings of the International Conference on Learning
146	  Representations (ICLR)}.
147	
148	\bibitem[{Liu et~al.(2023)Liu, Wang, Dao, Zhou, Yuan, Song, Shrivastava, Zhang,
149	  Tian, Re, and Chen}]{liu2023dejavu}
150	Zichang Liu, Jue Wang, Tri Dao, Tianyi Zhou, Binhang Yuan, Zhao Song, Anshumali
151	  Shrivastava, Ce~Zhang, Yuandong Tian, Christopher Re, and Beidi Chen. 2023.
152	\newblock \href {https://arxiv.org/abs/2310.17157} {Deja vu: Contextual
153	  sparsity for efficient llms at inference time}.
154	\newblock In \emph{Proceedings of the International Conference on Machine
155	  Learning (ICML)}.
156	
157	\bibitem[{Loshchilov and Hutter(2019)}]{loshchilov2019adamw}
158	Ilya Loshchilov and Frank Hutter. 2019.
159	\newblock \href {https://arxiv.org/abs/1711.05101} {Decoupled weight decay
160	  regularization}.
161	\newblock In \emph{Proceedings of the International Conference on Learning
162	  Representations (ICLR)}.
163	
164	\bibitem[{Louizos et~al.(2018)Louizos, Welling, and Kingma}]{louizos2018l0}
165	Christos Louizos, Max Welling, and Diederik~P. Kingma. 2018.
166	\newblock \href {https://arxiv.org/abs/1712.01312} {Learning sparse neural
167	  networks through $l_0$ regularization}.
168	\newblock In \emph{Proceedings of the International Conference on Learning
169	  Representations (ICLR)}.
170	
171	\bibitem[{Luo et~al.(2024)Luo, Song, Han, Chen, Xiao, Meng, Deng, Wei, Liu, and
172	  Sun}]{luo2024sparsinglaw}
173	Yuqi Luo, Chenyang Song, Xu~Han, Yingfa Chen, Chaojun Xiao, Xiaojun Meng, Liqun
174	  Deng, Jiansheng Wei, Zhiyuan Liu, and Maosong Sun. 2024.
175	\newblock \href {https://arxiv.org/abs/2411.02335} {Sparsing law: Towards large
176	  language models with greater activation sparsity}.
177	\newblock \emph{arXiv preprint arXiv:2411.02335}.
178	
179	\bibitem[{Maddison et~al.(2017)Maddison, Mnih, and Teh}]{maddison2017concrete}
180	Chris~J. Maddison, Andriy Mnih, and Yee~Whye Teh. 2017.
181	\newblock \href {https://arxiv.org/abs/1611.00712} {The concrete distribution:
182	  A continuous relaxation of discrete random variables}.
183	\newblock In \emph{Proceedings of the International Conference on Learning
184	  Representations (ICLR)}.
185	
186	\bibitem[{Merity et~al.(2017)Merity, Xiong, Bradbury, and
187	  Socher}]{merity2017pointer}
188	Stephen Merity, Caiming Xiong, James Bradbury, and Richard Socher. 2017.
189	\newblock \href {https://arxiv.org/abs/1609.07843} {Pointer sentinel mixture
190	  models}.
191	\newblock In \emph{Proceedings of the International Conference on Learning
192	  Representations (ICLR)}.
193	
194	\bibitem[{Mirzadeh et~al.(2024)Mirzadeh, Alizadeh, Mehta, Mundo, Tuzel, Samei,
195	  Rastegari, and Farajtabar}]{mirzadeh2024relu}
196	Iman Mirzadeh, Keivan Alizadeh, Sachin Mehta, Carlo C~Del Mundo, Oncel Tuzel,
197	  Golnoosh Samei, Mohammad Rastegari, and Mehrdad Farajtabar. 2024.
198	\newblock \href {https://arxiv.org/abs/2310.04564} {Relu strikes back:
199	  Exploiting activation sparsity in large language models}.
200	\newblock In \emph{Proceedings of the International Conference on Learning
201	  Representations (ICLR)}.
202	
203	\bibitem[{Muralidharan et~al.(2024)Muralidharan, Sreenivas, Joshi, Chochowski,
204	  Patwary, Shoeybi, Catanzaro, Kautz, and Molchanov}]{muralidharan2024minitron}
205	Saurav Muralidharan, Sharath~Turuvekere Sreenivas, Raviraj Joshi, Marcin
206	  Chochowski, Mostofa Patwary, Mohammad Shoeybi, Bryan Catanzaro, Jan Kautz,
207	  and Pavlo Molchanov. 2024.
208	\newblock \href {https://arxiv.org/abs/2407.14679} {Compact language models via
209	  pruning and knowledge distillation}.
210	\newblock In \emph{Advances in Neural Information Processing Systems
211	  (NeurIPS)}.
212	
213	\bibitem[{Raffel et~al.(2020)Raffel, Shazeer, Roberts, Lee, Narang, Matena,
214	  Zhou, Li, and Liu}]{raffel2020c4}
215	Colin Raffel, Noam Shazeer, Adam Roberts, Katherine Lee, Sharan Narang, Michael
216	  Matena, Yanqi Zhou, Wei Li, and Peter~J. Liu. 2020.
217	\newblock \href {https://arxiv.org/abs/1910.10683} {Exploring the limits of
218	  transfer learning with a unified text-to-text transformer}.
219	\newblock \emph{Journal of Machine Learning Research}, 21(140):1--67.
220	
221	\bibitem[{Raposo et~al.(2024)Raposo, Ritter, Richards, Lillicrap, Humphreys,
222	  and Santoro}]{raposo2024mod}
223	David Raposo, Sam Ritter, Blake Richards, Timothy Lillicrap, Peter~Conway
224	  Humphreys, and Adam Santoro. 2024.
225	\newblock \href {https://arxiv.org/abs/2404.02258} {Mixture-of-depths:
226	  Dynamically allocating compute in transformer-based language models}.
227	\newblock \emph{arXiv preprint arXiv:2404.02258}.
228	
229	\bibitem[{Sanh et~al.(2019)Sanh, Debut, Chaumond, and
230	  Wolf}]{sanh2019distilbert}
231	Victor Sanh, Lysandre Debut, Julien Chaumond, and Thomas Wolf. 2019.
232	\newblock \href {https://arxiv.org/abs/1910.01108} {Distilbert, a distilled
233	  version of bert: smaller, faster, cheaper and lighter}.
234	\newblock \emph{arXiv preprint arXiv:1910.01108}.
235	
236	\bibitem[{Serbin et~al.(2026)Serbin, Koshkin, Sun, Bistrigova, and
237	  Korikov}]{serbin2026svdcsp}
238	Georgii Serbin, Kirill Koshkin, Zhongao Sun, Anastasiya Bistrigova, and C.C.
239	  Korikov. 2026.
240	\newblock \href {https://arxiv.org/abs/2603.14110} {Svd contextual sparsity
241	  predictors for fast llm inference}.
242	\newblock \emph{arXiv preprint arXiv:2603.14110}.
243	
244	\bibitem[{Shazeer(2020)}]{shazeer2020glu}
245	Noam Shazeer. 2020.
246	\newblock \href {https://arxiv.org/abs/2002.05202} {Glu variants improve
247	  transformer}.
248	\newblock \emph{arXiv preprint arXiv:2002.05202}.
249	
250	\bibitem[{Shin et~al.(2025)Shin, Yang, and Yi}]{shin2025sparseinfer}
251	Jiho Shin, Hoeseok Yang, and Youngmin Yi. 2025.
252	\newblock \href {https://arxiv.org/abs/2411.12692} {Sparseinfer: Training-free
253	  prediction of activation sparsity for fast llm inference}.
254	\newblock In \emph{Proceedings of the Design, Automation \& Test in Europe
255	  Conference (DATE)}.
256	
257	\bibitem[{Song et~al.(2025)Song, Han, Zhang, Hu, Shi, Li, Chen, Liu, Li, Yang,
258	  and Sun}]{song2025prosparse}
259	Chenyang Song, Xu~Han, Zhengyan Zhang, Shengding Hu, Xiyu Shi, Kuai Li, Chen
260	  Chen, Zhiyuan Liu, Guangli Li, Tao Yang, and Maosong Sun. 2025.
261	\newblock \href {https://arxiv.org/abs/2402.13516} {Prosparse: Introducing and
262	  enhancing intrinsic activation sparsity within large language models}.
263	\newblock In \emph{Proceedings of the International Conference on Computational
264	  Linguistics (COLING)}.
265	
266	\bibitem[{Song et~al.(2024{\natexlab{a}})Song, Mi, Xie, and
267	  Chen}]{song2024powerinfer}
268	Yixin Song, Zeyu Mi, Haotong Xie, and Haibo Chen. 2024{\natexlab{a}}.
269	\newblock \href {https://arxiv.org/abs/2312.12456} {Powerinfer: Fast large
270	  language model serving with a consumer-grade gpu}.
271	\newblock In \emph{Proceedings of the ACM Symposium on Operating Systems
272	  Principles (SOSP)}.
273	
274	\bibitem[{Song et~al.(2024{\natexlab{b}})Song, Xie, Zhang, Wen, Ma, Mi, and
275	  Chen}]{song2024turbosparse}
276	Yixin Song, Haotong Xie, Zhengyan Zhang, Bo~Wen, Li~Ma, Zeyu Mi, and Haibo
277	  Chen. 2024{\natexlab{b}}.
278	\newblock \href {https://arxiv.org/abs/2406.05955} {Turbo sparse: Achieving llm
279	  sota performance with minimal activated parameters}.
280	\newblock \emph{arXiv preprint arXiv:2406.05955}.
281	
282	\bibitem[{Sun et~al.(2024)Sun, Liu, Bair, and Kolter}]{sun2024wanda}
283	Mingjie Sun, Zhuang Liu, Anna Bair, and J.~Zico Kolter. 2024.
284	\newblock \href {https://arxiv.org/abs/2306.11695} {A simple and effective
285	  pruning approach for large language models}.
286	\newblock In \emph{Proceedings of the International Conference on Learning
287	  Representations (ICLR)}.
288	
289	\bibitem[{Szatkowski et~al.(2024)Szatkowski, W{\'o}jcik, Pi{\'o}rczy{\'n}ski,
290	  and Scardapane}]{szatkowski2024d2dmoe}
291	Filip Szatkowski, Bartosz W{\'o}jcik, Miko{\l}aj Pi{\'o}rczy{\'n}ski, and
292	  Simone Scardapane. 2024.
293	\newblock \href {https://arxiv.org/abs/2310.04361} {Exploiting activation
294	  sparsity with dense to dynamic-$k$ mixture-of-experts conversion}.
295	\newblock In \emph{Advances in Neural Information Processing Systems
296	  (NeurIPS)}, volume~37.
297	
298	\bibitem[{Team(2024)}]{qwen2024qwen25}
299	Qwen Team. 2024.
300	\newblock \href {https://arxiv.org/abs/2412.15115} {Qwen2.5 technical report}.
301	\newblock \emph{arXiv preprint arXiv:2412.15115}.
302	
303	\bibitem[{Xu et~al.(2025)Xu, Yang, Gao, Weng, and Ma}]{xu2026spon}
304	Haotian Xu, Jiannan Yang, Tian Gao, Tsui-Wei Weng, and Tengfei Ma. 2025.
305	\newblock \href {https://arxiv.org/abs/2512.12744} {Resting neurons, active
306	  insights: Robustify activation sparsity for large language models}.
307	\newblock In \emph{Proceedings of the International Conference on Machine
308	  Learning (ICML)}.
309	
310	\bibitem[{Zhang et~al.(2025)Zhang, Liu, Tian, Khaitan, Wang, and
311	  Li}]{zhang2025rsparse}
312	Zhenyu Zhang, Zechun Liu, Yuandong Tian, Harshit Khaitan, Zhangyang Wang, and
313	  Steven Li. 2025.
314	\newblock \href {https://arxiv.org/abs/2504.19449} {R-sparse: Rank-aware
315	  activation sparsity for efficient llm inference}.
316	\newblock In \emph{Proceedings of the International Conference on Learning
317	  Representations (ICLR)}.
318	
319	\bibitem[{Zhou et~al.(2022)Zhou, Lei, Liu, Du, Huang, Zhao, Dai, Chen, Le, and
320	  Laudon}]{zhou2022expertchoice}
321	Yanqi Zhou, Tao Lei, Hanxiao Liu, Nan Du, Yanping Huang, Vincent Zhao,
322	  Andrew~M. Dai, Zhifeng Chen, Quoc~V. Le, and James Laudon. 2022.
323	\newblock \href {https://arxiv.org/abs/2202.09368} {Mixture-of-experts with
324	  expert choice routing}.
325	\newblock In \emph{Advances in Neural Information Processing Systems
326	  (NeurIPS)}, volume~35.
327	
328	\end{thebibliography}
329	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2eab6bdf-fed9-432f-9897-c2ae452492bc",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "aa23eb8a-3a74-4873-9764-966d6703b5e2",
  "sourceToolAssistantUUID": "2eab6bdf-fed9-432f-9897-c2ae452492bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 35 · 2026-05-18T18:39:14.290Z_

Now let me check the paper images to understand the figures.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa23eb8a-3a74-4873-9764-966d6703b5e2",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXDcUo9TzhzEkpZNfrE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "52e48be1-3068-4b48-ba63-261f2d22a8dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FQh1CWi4cPa3ghaBA9zZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7825,
      "cache_read_input_tokens": 51798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7825,
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

_source line 36 · 2026-05-18T18:39:16.456Z_

<details open><summary>🔧 Tool call — Read · `toolu_01LAG3Fks7C4y2mb8GECqUUA`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper/fig1_overview.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "52e48be1-3068-4b48-ba63-261f2d22a8dc",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXDcUo9TzhzEkpZNfrE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "eec46fe8-8497-4cea-8c53-9b2ae273062b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FQh1CWi4cPa3ghaBA9zZP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7825,
      "cache_read_input_tokens": 51798,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7825,
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

### Tool result

_source line 37 · 2026-05-18T18:39:16.480Z_

<details><summary>↩ Tool result · `toolu_01LAG3Fks7C4y2mb8GECqUUA`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "eec46fe8-8497-4cea-8c53-9b2ae273062b",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "c9f1e370-41c4-469b-a7db-e4e2d0f0ea43",
  "sourceToolAssistantUUID": "eec46fe8-8497-4cea-8c53-9b2ae273062b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-18T18:39:16.601Z_

<details open><summary>🔧 Tool call — Read · `toolu_014ALrxGfHPZjC311k4tpTEW`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/figures/paper/fig2_sparsity_sweep.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c9f1e370-41c4-469b-a7db-e4e2d0f0ea43",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXDcUo9TzhzEkpZNfrE",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5d53ae1-dd83-4708-bc84-a3822be918b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_011FQh1CWi4cPa3ghaBA9zZP",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7825,
      "cache_read_input_tokens": 51798,
      "output_tokens": 186,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7825
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 186,
          "cache_read_input_tokens": 51798,
          "cache_creation_input_tokens": 7825,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7825,
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

_source line 39 · 2026-05-18T18:39:16.870Z_

<details><summary>↩ Tool result · `toolu_014ALrxGfHPZjC311k4tpTEW`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/png"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5d53ae1-dd83-4708-bc84-a3822be918b6",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "16c00034-fdb1-4c2f-aeb3-90de6f759617",
  "sourceToolAssistantUUID": "f5d53ae1-dd83-4708-bc84-a3822be918b6",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-18T18:39:20.506Z_

Now let me check for any em-dash or writing pattern issues in the tex files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "16c00034-fdb1-4c2f-aeb3-90de6f759617",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXE2PyLtwvwV4r1oQNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "0cadcf2d-af29-4ad3-b5a3-0b87d2cdedcc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaW2ujT2DRywkjTVEDCRbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 59623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2181,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 41 · 2026-05-18T18:39:21.499Z_

<details open><summary>🔧 Tool call — Bash · `toolu_01LkquUGcZpfgeKVkYtu3czS`</summary>

```json
{
  "command": "grep -n \"—\\|–\" /home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper/*.tex 2>/dev/null | head -30",
  "description": "Search for em-dash and en-dash in tex files"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0cadcf2d-af29-4ad3-b5a3-0b87d2cdedcc",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXE2PyLtwvwV4r1oQNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "98e2ae0c-6051-421d-a04b-cca38bbde739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaW2ujT2DRywkjTVEDCRbp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 59623,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2181,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 42 · 2026-05-18T18:39:21.665Z_

<details><summary>↩ Tool result · `toolu_01LkquUGcZpfgeKVkYtu3czS`</summary>

```text
(Bash completed with no output)
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "98e2ae0c-6051-421d-a04b-cca38bbde739",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "d75716ae-353c-444e-b6e1-cb5326b9fb60",
  "sourceToolAssistantUUID": "98e2ae0c-6051-421d-a04b-cca38bbde739",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Tool call

_source line 43 · 2026-05-18T18:39:22.597Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01T5ZYpdxg1SkSqdtLJsbFYx`</summary>

```json
{
  "pattern": "ing,|ing\\.",
  "glob": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d75716ae-353c-444e-b6e1-cb5326b9fb60",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXE2PyLtwvwV4r1oQNH",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4ebe9610-725e-4e7c-9193-905de78c254a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RaW2ujT2DRywkjTVEDCRbp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2181,
      "cache_read_input_tokens": 59623,
      "output_tokens": 275,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2181
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 275,
          "cache_read_input_tokens": 59623,
          "cache_creation_input_tokens": 2181,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2181,
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

_source line 44 · 2026-05-18T18:39:22.618Z_

<details><summary>↩ Tool result · `toolu_01T5ZYpdxg1SkSqdtLJsbFYx`</summary>

```text
paper/related_work.tex:5:CATS~\cite{lee2024cats} adapts per-layer thresholds for SiLU/SwiGLU activations; R-Sparse~\cite{zhang2025rsparse} predicts sparsity from rank-aware SVD projections; DIP~\cite{federici2025dip} combines dynamic input pruning with cache-aware masking; SparseInfer~\cite{shin2025sparseinfer} predicts activation sparsity patterns from attention outputs without additional training.
paper/related_work.tex:13:PowerInfer~\cite{song2024powerinfer} exploits power-law activation frequencies for GPU--CPU scheduling.
paper/related_work.tex:15:Both share the principle of frozen weights + learnable masks + KL training, but solve distinct optimization problems: MaskLLM finds optimal static N:M patterns within fixed groups, while we predict dynamic per-token masks under a global budget constraint.
paper/related_work.tex:16:The structural mismatch we characterize (per-neuron gradient decomposition vs.\ global top-$k$) does not arise in MaskLLM's per-group categorical setting, where N:M patterns eliminate cross-group budget competition.
paper/related_work.tex:25:\paragraph{Activation Function Engineering.}
paper/related_work.tex:30:\paragraph{Weight Pruning, Distillation, and Routing.}
paper/related_work.tex:31:Wanda~\cite{sun2024wanda} and SparseGPT~\cite{frantar2023sparsegpt} produce static weight masks; Switch Transformers~\cite{fedus2022switch} and Mixture-of-Depths~\cite{raposo2024mod} achieve conditional computation through learned routing.
paper/related_work.tex:32:KL-based distillation~\cite{kim2016sequencekd,sanh2019distilbert,gu2024minillm,agarwal2024gkd} trains compact students; SparseLoRA~\cite{khaki2025sparselora} exploits contextual sparsity for fine-tuning.
paper/experiments.tex:10:\paragraph{Training.}
paper/experiments.tex:12:The KL predictor uses Gumbel-Sigmoid relaxation~\cite{jang2017gumbel} with temperature $\tau=1.0$ annealed to $0.1$ over training.
paper/experiments.tex:67:The difference is systematic, not due to architectural or compute limitations: both predictors use identical architectures and TEAL allocation, yet BCE achieves +7pp oracle F1 (0.613 vs.\ 0.540) with 139\% worse PPL (28.13 vs.\ 11.79). KL's near-random precision (0.51) is consistent with learning a mask optimized for distributional fidelity rather than magnitude matching. % exp_id: f1_oracle_analysis, bce_isocompute_s42
paper/experiments.tex:68:Coupled training correlates with better output preservation; the causal ablation in \S\ref{sec:mask_analysis} confirms that target quality, not gradient coupling, is the primary driver.
paper/experiments.tex:78:\paragraph{Causal Ablation: Target Quality vs.\ Gradient Coupling.}
paper/experiments.tex:82:Target quality, not gradient coupling, is the sole driver of KL's advantage; the coupled gradient is a means to discover better targets, not an independent source of quality. % exp_id: bce50_3seed
paper/experiments.tex:205:PPL remains low (8.36) but downstream accuracy degrades; PPL is a poor proxy for reasoning.
paper/conclusion.tex:5:KL distillation discovers neuron importance patterns that diverge 53\% from magnitude-based masks; a causal ablation confirms target quality, not gradient coupling, as the primary driver.
paper/method.tex:55:The Gumbel noise provides stochastic exploration of mask configurations during training, while the temperature controls sharpness: as $\tau \to 0$, $\tilde{m}_j$ approaches a binary decision.
paper/method.tex:57:We anneal $\tau$ linearly from 1.0 to 0.1 over training.
paper/method.tex:63:In our setting, STE produces discontinuous gradient signals: small parameter changes can flip many neurons simultaneously, causing violent oscillations in the penalty weight and failure to converge to the target sparsity.
paper/method.tex:111:We analyze the structural difference between BCE and KL training signals to build intuition for why KL distillation may be better suited to global top-$k$ inference. The analysis is suggestive; \S\ref{sec:mask_analysis} provides causal confirmation that mask target quality, not gradient coupling, drives the advantage.
paper/method.tex:178:\paragraph{Training signal coupling.}
paper/appendix.tex:28:The full KL-sparse pipeline adds 6.4\% overhead to dense inference (126.78 vs.\ 119.11\,ms/forward), of which the predictor's 32-layer forward pass contributes 3.17\,ms (2.7\%); the remainder arises from mask application and sparse FFN indexing.
paper/appendix.tex:140:\caption{Adaptive penalty controller convergence across sparsity targets. Upper panel: penalty weight $\lambda$ (log scale) over training steps. The 30\% target requires extreme penalty ($\lambda \to 5000$) to suppress activations below their natural density, while 50\% needs only $\lambda \approx 8$ since SwiGLU gates already cluster near this sparsity. Lower panel: actual sparsity (solid) converges to the target (dashed) within $\sim$10 steps via geometric doubling.}
paper/appendix.tex:147:The controller reliably drives actual sparsity to within 5\% of the target across all tested regimes, with $\lambda$ spanning three orders of magnitude (8 to 5000) via geometric doubling.
paper/appendix.tex:235:[Omitted long matching line]
paper/limitations.tex:7:The causal ablation (\S\ref{sec:mask_analysis}) confirms that mask target quality, not gradient coupling, is the primary driver of KL's advantage. However, the mechanism by which KL's coupled gradient discovers superior mask patterns during training remains incompletely characterized; future work could trace per-layer mask divergence trajectories across training to identify when and where the patterns diverge.
paper/introduction.tex:10:The empirical picture, however, reveals something more fundamental: KL-trained predictors discover neuron importance patterns that diverge 53\% from magnitude-based masks (per-layer Jaccard 47\%), and a causal ablation confirms that these learned mask patterns, not gradient coupling, are the primary quality driver.
paper/introduction.tex:21:\item KL-trained predictors discover neuron importance patterns diverging 53\% from magnitude-based masks. A causal ablation proves that mask target quality, not gradient coupling, determines quality under global allocation (\S\ref{sec:mask_analysis}).
paper/abstract.tex:2:A causal ablation confirms that these mask patterns, not gradient coupling, drive quality: under controlled 50\% evaluation, BCE trained on KL-derived targets exactly matches KL across perplexity and all four downstream tasks (max $\Delta$=0.79pp), while magnitude-trained BCE achieves 28.13$\pm$0.20.
paper/ethics.tex:37:\item[\textbf{D1--D5.}] N/A. No human subjects, crowdsourcing, or annotation involved.
paper/ethics.tex:42:\item[\textbf{E1.}] AI writing assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were produced and verified by the authors.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ebe9610-725e-4e7c-9193-905de78c254a",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "554ee042-06bd-4e66-8f14-fd346d59c7bb",
  "sourceToolAssistantUUID": "4ebe9610-725e-4e7c-9193-905de78c254a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 45 · 2026-05-18T18:39:26.737Z_

Now I have a thorough understanding of the paper. Let me also check what WINA is, since it's mentioned as a baseline but I want to verify its reference.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "554ee042-06bd-4e66-8f14-fd346d59c7bb",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXESu7Jnzmhr9ho9MFt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e8e90027-34ab-4740-b0a6-e54ddd16b7f2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByBrRZBsnUQAG75EP7MmRd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 61804,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2225,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 46 · 2026-05-18T18:39:27.158Z_

<details open><summary>🔧 Tool call — Grep · `toolu_01LB95fze4zX4yDV6QqVW3Ho`</summary>

```json
{
  "pattern": "WINA",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu/paper",
  "output_mode": "content"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8e90027-34ab-4740-b0a6-e54ddd16b7f2",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXESu7Jnzmhr9ho9MFt",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cac339e7-9ff3-48c8-a370-de3d219ff492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ByBrRZBsnUQAG75EP7MmRd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2225,
      "cache_read_input_tokens": 61804,
      "output_tokens": 158,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2225
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 158,
          "cache_read_input_tokens": 61804,
          "cache_creation_input_tokens": 2225,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2225,
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

_source line 47 · 2026-05-18T18:39:27.190Z_

<details><summary>↩ Tool result · `toolu_01LB95fze4zX4yDV6QqVW3Ho`</summary>

```text
paper/experiments.tex:22:We compare against: (1) \textbf{Vanilla TEAL}~\cite{liu2025teal}, which uses activation magnitudes directly; (2) \textbf{BCE predictor} (DejaVu-style~\cite{liu2023dejavu}), trained with per-neuron binary cross-entropy on magnitude-based oracle masks for 1000 and 2700 steps; (3) \textbf{Uniform allocation}, which distributes the sparsity budget equally across layers; and (4) \textbf{WINA}~\cite{liu2025teal}, an importance-weighted variant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cac339e7-9ff3-48c8-a370-de3d219ff492",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "07f6b22e-a197-4e46-8bea-a06b89fdc5ec",
  "sourceToolAssistantUUID": "cac339e7-9ff3-48c8-a370-de3d219ff492",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 48 · 2026-05-18T18:39:29.972Z_

Now let me submit the review report via the MCP tool.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "07f6b22e-a197-4e46-8bea-a06b89fdc5ec",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXEnd2PLcnafpeZbkFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "18ca0bb5-c9d3-4c49-89e6-4f9e228792a9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kofdHoGEXSF2YouZSbunK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 64029,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 323,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 2,
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

_source line 49 · 2026-05-18T18:39:30.176Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_013RTRvXyHPoDxohZuXTubXK`</summary>

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
  "parentUuid": "18ca0bb5-c9d3-4c49-89e6-4f9e228792a9",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXEnd2PLcnafpeZbkFs",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "db9e722a-9b2d-48e5-be8f-53fc3e40023d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015kofdHoGEXSF2YouZSbunK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 323,
      "cache_read_input_tokens": 64029,
      "output_tokens": 103,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 323
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 103,
          "cache_read_input_tokens": 64029,
          "cache_creation_input_tokens": 323,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 323,
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

_source line 50 · 2026-05-18T18:39:30.178Z_

<details><summary>↩ Tool result · `toolu_013RTRvXyHPoDxohZuXTubXK`</summary>

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
  "parentUuid": "db9e722a-9b2d-48e5-be8f-53fc3e40023d",
  "isSidechain": true,
  "promptId": "15e03be2-6778-47f5-b247-136630963b1f",
  "agentId": "ac9516e874bee4160",
  "type": "user",
  "uuid": "c575ffdb-89ad-484d-85bf-4eaa38bbb600",
  "sourceToolAssistantUUID": "db9e722a-9b2d-48e5-be8f-53fc3e40023d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-18T18:40:41.360Z_



Now I have thoroughly read the full paper. Let me compile my review.

---

## Review: R2 (Novelty, Positioning, Related Work, Writing Quality)

### Summary

This paper trains per-token contextual sparsity predictors for SwiGLU-based LLMs using forward KL divergence distillation from the dense model, replacing the standard BCE-against-magnitude-oracles approach. The central empirical finding is that KL-trained predictors discover neuron importance masks that diverge 53% from magnitude-based masks (Jaccard 47%), and a causal ablation shows that mask target quality, not gradient coupling per se, is the primary driver of KL's advantage. The paper also shows that post-hoc compensation networks become redundant under KL training, and provides a sparsity regime analysis across 30-70% sparsity with cross-architecture validation on Mistral-7B and Qwen-14B.

### Strengths

- **Honest, self-undermining analysis.** The paper's causal ablation (BCE on KL-derived targets matches KL) is unusually candid. Rather than overselling gradient coupling, the authors correctly identify that KL's value is in automated oracle discovery. This intellectual honesty raises credibility.

- **Well-structured taxonomy.** The 2D taxonomy (correction granularity x training signal coupling) is a useful organizational contribution that clarifies the design space. Placing existing methods (DejaVu, SPON, ShadowLLM, D2DMoE) in this grid helps readers understand relative positioning.

- **Thorough Related Work for this subfield.** The Related Work section is substantially improved from what the task summary suggested. It covers training-free methods (TEAL, CATS, R-Sparse, DIP, SparseInfer), predictor-based methods (DejaVu, ShadowLLM, FastForward, SVD-CSP, PowerInfer, MaskLLM), static correction (SPON), activation function engineering (ReLU Strikes Back, TurboSparse, ProSparse, Sparsing Law), weight pruning (Wanda, SparseGPT), MoE routing (Expert Choice, D2D-MoE, Griffin), and distillation (sequence KD, DistilBERT, MiniLLM, GKD). With 37 references in the bibliography, coverage is adequate.

- **Compensation redundancy result.** Showing that KL renders the +67.2M compensation network unnecessary at both 30% and 50% is a clean practical contribution that simplifies the inference pipeline.

- **Multi-seed reporting.** Three-seed evaluation with standard deviations throughout is good practice. The identification of high MMLU seed variance under global allocation (9.5pp) is a useful finding.

- **The paper does have figures.** Contrary to the task summary, the LaTeX source includes Figure 1 (method overview/taxonomy), Figure 2 (sparsity sweep plot), Figure 3 (in appendix: Lagrangian dynamics), and Figure 4 (per-layer retention). The sparsity sweep figure is clear and informative.

### Weaknesses

- **(Major) The core contribution is incremental.** The paper fills one cell in its own taxonomy: per-token x coupled KL. The technical novelty is combining existing components (Gumbel-Sigmoid from Concrete/L0 literature, KL distillation from standard KD, per-token MLP predictors from DejaVu). No new architecture, loss function, or algorithm is proposed. The paper's own causal ablation shows that the KL objective's primary value is discovering better oracle masks, not the coupled gradient pathway that the gradient analysis section motivates. This significantly weakens the methodological contribution: the "method" is essentially "use KL instead of BCE," and the paper shows this mainly matters because magnitude-based oracles are suboptimal targets.

- **(Major) The paper undermines its own practical value at 30% sparsity.** At the recommended 30% operating point, KL achieves PPL 8.82 vs. TEAL's 10.97 (a meaningful but not dramatic improvement), while downstream metrics show modest gains (ARC-c +1.4pp, WG +2.8pp) with MMLU actually worse under global allocation (35.7 vs. 38.6). The paper does not compare against BCE with better oracle masks at 30%, which its own analysis suggests should close the gap. At 50%, downstream tasks collapse to near-random regardless of method. The practical operating window where KL meaningfully outperforms simpler approaches appears narrow.

- **(Major) No wall-clock speedup demonstrated.** The paper adds 6.4% overhead to dense inference and explicitly states that "net acceleration requires kernel-level sparse computation optimizations." For an efficiency-motivated paper, showing only prediction quality without any actual speedup is a significant gap. The paper is honest about this limitation, but it substantially reduces practical impact.

- **(Major) Qwen-14B MMLU regression is inadequately explained.** At 14B scale, KL's MMLU falls 8pp below TEAL (63.7% vs. 71.8%), which is a large gap on the most important downstream benchmark. The explanation ("higher knowledge density causes KL's output-preservation objective to sacrifice task-specific pathways") is speculative and unsupported. This result raises serious concerns about the method's scalability, the claimed primary motivation.

- **(Minor) Gradient SNR claim is revised but still overreached.** The original task summary mentioned "10^3x higher SNR." The actual paper reports 5.14x at convergence with a non-monotonic trajectory where BCE exceeds KL during mid-training. The causal ablation then shows gradient coupling is NOT the driver. The SNR analysis occupies significant space in the Method section for what turns out to be a red herring by the paper's own admission.

- **(Minor) Missing data in important comparisons.** Table 5 (Qwen-14B) has missing GSM8K entries for uniform allocation. The paper does not include BCE results in the main comparison table at 30% sparsity (only at 50%). The cross-architecture (Mistral) and cross-scale (Qwen-14B) results are relegated to the appendix with only PPL (Mistral) or incomplete downstream metrics (Qwen).

- **(Minor) Training on WikiText-103, evaluating on WikiText-2.** These are from the same source (Wikipedia), making the "out-of-distribution" framing of C4 evaluation the real test. C4 PPL at 30% is 16.03 (1.74x dense), which is substantially worse than the WikiText-2 ratio (8.82/6.12 = 1.44x), suggesting some overfitting to the WikiText domain.

- **(Minor) Writing quality is generally good but has residual issues.** The paper avoids em-dashes (good), but some sentences are overly long and complex. The Method section front-loads the gradient coupling analysis as motivation, only for the Experiments section to show it is not the primary driver. This creates a narrative inconsistency where the theoretical motivation is undermined by the empirical finding. The paper would benefit from restructuring to lead with "KL discovers better masks" rather than "KL has coupled gradients."

- **(Minor) Figure 1 is a taxonomy table, not a method overview figure.** The caption says "Method overview" but the figure is the taxonomy grid. A proper architectural diagram showing the predictor-TEAL pipeline would aid comprehension. The paper lacks a visual method overview.

### Questions for Authors

1. Have you tried training BCE with oracle masks derived from activation-weighted importance (rather than pure magnitude) to see if the gap narrows? Your causal ablation implies the oracle target is the key variable, so characterizing what makes KL's discovered masks superior would strengthen the contribution.

2. Why is 30% sparsity recommended when you have no wall-clock speedup at any sparsity level? What is the deployment scenario where PPL improvement without latency improvement is valuable?

3. For the Qwen-14B MMLU regression: have you analyzed which layers or neuron groups differ between KL and TEAL masks at 14B? Is the regression consistent across seeds?

4. The adaptive penalty controller has 5% deviation at 30% (actual 28.5%). How sensitive are the comparisons to this mismatch? You compare KL at ~28.5% effective sparsity against TEAL at exactly 30%.

5. Training takes 1000 steps on WikiText-103 (~45 min). Would longer training or larger/more diverse training data close the C4 generalization gap?

6. MaskLLM uses the same principle (frozen weights + learnable masks + KL training) for N:M sparsity. Have you considered evaluating your method with N:M structure for hardware-friendly acceleration?

### Novelty Assessment

The technical novelty is **low-to-moderate**. The method combines three existing ideas (per-token MLP predictor, KL distillation, Gumbel-Sigmoid relaxation) without introducing new components. The paper's own analysis shows the key contribution is not the method but the empirical finding that KL discovers better oracle masks. This is a valid empirical contribution, but the "filling one cell in a taxonomy" framing makes the incremental nature transparent. The taxonomy itself and the causal ablation methodology are the most novel aspects, but they are analytical rather than methodological contributions.

Compared to SPON (static x KL) and FastForward (per-token x BCE), this work's increment is the combination, which is predictable from the taxonomy. The causal ablation finding that mask quality, not gradient coupling, drives the advantage is genuinely interesting but also somewhat deflating for the method's novelty: it implies a simpler two-stage approach (use any method to discover good masks, then train a fast BCE predictor on those masks) could achieve similar results.

### Score: 3 (Weak Reject / Findings-level)

### Confidence: 4 (High)

**Justification:** The paper is technically sound with honest analysis, adequate experiments, and good writing quality. However, the contribution is primarily empirical (KL discovers better masks than magnitude-based oracles), the practical impact is limited (no wall-clock speedup, narrow useful operating range, scalability concerns at 14B), and the technical novelty of combining existing components is low. The causal ablation is the strongest intellectual contribution but paradoxically undermines the method's novelty by showing the gradient coupling mechanism is not the driver. For EMNLP main conference (score 4.0 threshold), the contribution is insufficient. For Findings (score 3.0), the empirical analysis and honest methodology meet the bar, contingent on addressing the narrative inconsistency between gradient motivation and empirical conclusion.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c575ffdb-89ad-484d-85bf-4eaa38bbb600",
  "isSidechain": true,
  "agentId": "ac9516e874bee4160",
  "requestId": "req_011CbAXF1STGzyy4sEkxmkCp",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "4b5d69e1-aa5c-4a3b-bdf1-e84461ab0447",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_14/projects/distill_sparse_swiglu",
  "sessionId": "263fa585-9870-446a-8635-ded3c7ec2e0a",
  "version": "2.1.126",
  "gitBranch": "master",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X2PquvpMz6xv1YSQXxn7xR",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 681,
      "cache_read_input_tokens": 64352,
      "output_tokens": 2521,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 681
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 2521,
          "cache_read_input_tokens": 64352,
          "cache_creation_input_tokens": 681,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 681,
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
