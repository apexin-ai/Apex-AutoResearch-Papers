# Research conversation: You are Reviewer 2 (R2) in an academic peer review. Your focus is **novelty, positioning, and related work**. ## Paper S

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination? (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 27
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-2/agent-a738e9a8334856553.jsonl`
- **Structured JSON:** [`b8920e18bafa5c2fe328.json`](../../sessions/b8/b8920e18bafa5c2fe328.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

27 recorded events

### User

_source line 1 · 2026-05-20T09:10:50.010Z_

You are Reviewer 2 (R2) in an academic peer review. Your focus is **novelty, positioning, and related work**.

## Paper Summary
Title: "IRT-FIT: Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics"

The paper repurposes IRT person-fit statistics (lz*) from psychometrics to detect benchmark contamination in LLMs. Three contributions:
1. Two-sided detection framework capturing both partial contamination (lz* << 0) and full contamination (lz* >> 0)
2. Theoretical power formula relating detection power to n_items and contamination level (R²=0.97), with inverted-U signal structure
3. Large-scale audit of 2,847 Open LLM Leaderboard models (12% flagged rate)

## Method
- 4PL IRT model from PSN-IRT (Gu et al., 2024)
- lz statistic (Drasgow et al., 1985), corrected lz* (Snijders, 2001)
- Two-sided test |lz*| > c_{α/2} with BH-FDR
- Multiscale lzm aggregation (Hong et al., 2021)
- Power theory: power ≈ Φ(δ√n/σ − z_α)
- Inverted-U inflection point derivable from item difficulty distributions

## Related Work (as presented in paper, Section 7)
- **Benchmark contamination detection**: Min-K%++ (Shi et al., 2024), Time Travel probing (Oren et al., 2024), ConStat (Dekoninck et al., 2024), generalization-based (Dong et al., 2024), MIA fails post-RL (Wang et al., 2025)
- **IRT for LLMs**: tinyBenchmarks (Polo et al., 2024), PSN-IRT (Gu et al., 2024)
- **Person-fit in psychometrics**: Drasgow et al. (1985), Snijders (2001), Meijer & Sijtsma (2001), Hong et al. (2021)

## Key Results
- Controlled experiments: AUROC 0.96 at 15% contamination (QLoRA SFT on Qwen3.5-9B, Gemma-4-31B)
- Outperforms ConStat (0.83) and Min-K%++ (0.88) while requiring only binary responses
- Post-RL robustness: AUROC 0.92 after GRPO vs MIA 0.54
- 2,847-model leaderboard audit: 12% flagged, increasing from 6% to 18% over 2023-2024
- Power theory R²=0.97, inflection point predictions within 0.02 of observed
- 4PL vs 3PL: AUROC +0.05, false alarm reduction from 7.8% to 4.2%
- lzm cross-benchmark aggregation: AUROC 0.96→0.98
- Domain-level analysis: Gemini-1.5 uniformly 100% across all 57 MMLU domains
- 7 benchmarks validate power theory within 1-2%

## Paper Structure (8 pages main text + references)
1. Introduction
2. Background (IRT, Person-Fit Statistics)
3. Method: IRT-FIT (Two-Sided Framework, lzm, Power Theory)
4. Controlled Contamination Experiments
5. Comparisons and Robustness (Baselines, Post-RL, 4PL vs 3PL, lzm)
6. Large-Scale Empirical Study (PSN-IRT models, Leaderboard audit, BBH/MATH, Domain analysis)
7. Related Work
8. Conclusion + Limitations

## References (11 total)
Dekoninck et al. 2024 (ConStat, NeurIPS), Dong et al. 2024 (ACL), Drasgow et al. 1985 (BJMSP), Gu et al. 2024 (PSN-IRT, AAAI), Hong et al. 2021 (APM), Meijer & Sijtsma 2001 (APM), Oren et al. 2024 (ICLR Spotlight), Polo et al. 2024 (ICML), Shi et al. 2024 (ICLR), Snijders 2001 (Psychometrika), Wang et al. 2025 (arXiv)

## Your Task
Write a detailed review covering:

1. **Novelty Assessment**: How novel is the core idea of applying person-fit statistics to LLM contamination detection? Is the two-sided extension a genuine contribution or straightforward? Is the power theory derivation novel or a direct application of existing formulas?

2. **Related Work Coverage**: Are important baselines missing? Are there other IRT-for-LLMs works not cited? Are there person-fit applications in adjacent domains that should be discussed? Is the related work section thorough enough for a top venue?

3. **Positioning and Framing**: Is the "minimal-information operating point" framing compelling? Is the "detection frontier" concept well-articulated? How does this compare to the broader contamination detection literature?

4. **Writing Quality**: Is the paper well-written? Is the notation consistent? Are the contributions clearly stated? Is the paper at the right length/density for the venue?

5. **Impact and Significance**: Will this work influence the field? Is the leaderboard audit finding impactful? Does the theoretical framework add lasting value?

6. **Specific Concerns**: 
   - The reference list has only 11 entries — is this adequate?
   - Are there missing important references?
   - Is the framing fair to competing methods?

7. **Score**: Rate on 1-6 scale (1=Strong Reject, 2=Reject, 3=Weak Reject, 4=Weak Accept, 5=Accept, 6=Strong Accept). Target venue: top ML venue, ~25% acceptance rate.

8. **Confidence**: 1-5 scale (1=low, 5=expert).

Format your review clearly with headers. Be rigorous but fair. ~1500 words.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "f8f67f26-46e9-4dc5-8c6e-f05112743d82",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-20T09:10:50.021Z_

```json
{
  "parentUuid": "f8f67f26-46e9-4dc5-8c6e-f05112743d82",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
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
  "uuid": "093da438-ca6b-428e-87c4-bf5fc3de21e1",
  "timestamp": "2026-05-20T09:10:50.021Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-20T09:10:52.967Z_



I'll review the paper materials to provide a thorough assessment. Let me first load the relevant tools and read the paper files.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "093da438-ca6b-428e-87c4-bf5fc3de21e1",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZVhCzhPmBZntHKcxuj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "b9afe46f-b7da-43cf-b09c-383056155d56",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AM8hxqWW5nUQPBWBDLrfkN",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7836,
      "cache_read_input_tokens": 8254,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 7836,
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

_source line 4 · 2026-05-20T09:10:53.778Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01P3vG21a3hiJkt1DNHz7bci`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_dream_review_report",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b9afe46f-b7da-43cf-b09c-383056155d56",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZVhCzhPmBZntHKcxuj",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a487391b-4233-406f-be19-a478bda6b355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AM8hxqWW5nUQPBWBDLrfkN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 7836,
      "cache_read_input_tokens": 8254,
      "output_tokens": 132,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7836
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 132,
          "cache_read_input_tokens": 8254,
          "cache_creation_input_tokens": 7836,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7836,
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

_source line 5 · 2026-05-20T09:10:53.787Z_

<details><summary>↩ Tool result · `toolu_01P3vG21a3hiJkt1DNHz7bci`</summary>

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
  "tool_name": "mcp__agent-ml-research__submit_dream_review_report"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a487391b-4233-406f-be19-a478bda6b355",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "1d49800e-5853-472e-9989-9812fdc6e33f",
  "sourceToolAssistantUUID": "a487391b-4233-406f-be19-a478bda6b355",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 6 · 2026-05-20T09:10:57.372Z_



Let me read the key project files to ground my review in the actual paper content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d49800e-5853-472e-9989-9812fdc6e33f",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZVys7DsSmCCWhEspBk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "a32afcb2-09a0-4f6f-bc1d-347d55f2dd97",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhiQ2Xjhp2wWtHhSYXaxGj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 16090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 7 · 2026-05-20T09:10:58.351Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U1WPJzLtyQ3bkjrBgeRRRP`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ideas.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a32afcb2-09a0-4f6f-bc1d-347d55f2dd97",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZVys7DsSmCCWhEspBk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "31ba3a18-a7a9-4d56-bfcb-4c98e9cb062a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhiQ2Xjhp2wWtHhSYXaxGj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 16090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 8 · 2026-05-20T09:10:58.406Z_

<details><summary>↩ Tool result · `toolu_01U1WPJzLtyQ3bkjrBgeRRRP`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'irt_personfit_contam'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "31ba3a18-a7a9-4d56-bfcb-4c98e9cb062a",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "3d15b4fe-1b15-44d5-ac81-771b879b6c56",
  "sourceToolAssistantUUID": "31ba3a18-a7a9-4d56-bfcb-4c98e9cb062a",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T09:10:58.864Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0162yQFj5nYN9cJGzHxFPTSS`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "paper_framing.md",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d15b4fe-1b15-44d5-ac81-771b879b6c56",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZVys7DsSmCCWhEspBk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "071f4bfe-b515-43fe-b5b6-91018343eaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhiQ2Xjhp2wWtHhSYXaxGj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 16090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 10 · 2026-05-20T09:10:58.894Z_

<details><summary>↩ Tool result · `toolu_0162yQFj5nYN9cJGzHxFPTSS`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/paper_framing.md\", \"content\": \"# Paper Framing — irt_personfit_contam\\n\\n## Target Venue\\n- Primary: EMNLP 2026 Main (用户确认；ARR submission DDL 5/25 — 需确认可行性)\\n- Fallback: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n- Backup: ICLR 2027 (~Sep 2026, ~17 weeks)\\n\\n## Core Claims (3 条)\\n\\n**Claim 1 (Minimal-Information Detection)**:\\nIRT person-fit statistics detect benchmark contamination at the minimal-information operating point on the detection frontier — requiring only binary (correct/incorrect) response patterns, without access to model logits, weights, or training data.\\n\\n**Claim 2 (Detection Characterization)**:\\nDetection power is a predictable function of benchmark size (n_items) and contamination level, with two distinct signal regimes: partial contamination produces aberrant patterns (lz* << 0), full contamination produces over-consistent patterns (lz* >> 0). For sufficiently large benchmarks (≥10K items), power exceeds 90% at 15% contamination.\\n\\n**Claim 3 (Empirical Prevalence)**:\\nApplying IRT-FIT to publicly available LLM benchmark data reveals contamination patterns quantifiable for the first time via IRT — including Gemini-1.5's 100% MMLU accuracy (lz*=+34.75, θ=0.78) as systematic contamination evidence with model-level cross-benchmark anomaly profiles (Gemini-1.5 flagged on 4/5 benchmarks). Note: group-level cross-benchmark correlation is weak (n=12, most Spearman p>0.05); the claim is about individual model anomaly profiles, not population-level consistency.\\n\\n## Story Spine\\n\\n**Problem**: Benchmark contamination undermines LLM evaluation reliability. As benchmarks proliferate and training corpora grow, contamination risk increases, but all existing detection methods require privileged access — training data (n-gram overlap), token probabilities (Min-K%, MIA), model weights (internal probing), or specially crafted prompts (Time Travel). A contaminated LLM is functionally analogous to an examinee with item preknowledge, yet no work has connected the mature psychometric literature on cheating detection to LLM benchmark integrity.\\n\\n**Existing approaches & gaps**: Detection methods circa 2026 span five families: time-based partition, MIA/Min-K%++ (ICLR 2024), Time Travel probing (ICLR 2024 Spotlight), ConStat performance-based testing (NeurIPS 2024), and CoDeC in-context learning effects (ICLR 2026). Wang et al. (2025) show all MIA-based methods fail under post-RL contamination. Critically, ALL require more than binary response patterns — no method operates at the minimal-information level.\\n\\n**Our framing**: We establish the minimal-information operating point on the contamination detection frontier. By repurposing IRT person-fit statistics (lz*, outfit, infit) — developed over decades for detecting exam cheating — we answer: \\\"What can be detected from binary response patterns alone?\\\" This is a foundational question, not just another detector. We show the method works (97.9% power on MMLU), characterize its limits (power ∝ n_items), and reveal its dual-regime signal structure (partial vs. full contamination).\\n\\n**Headline result template**: \\\"Using only binary response patterns, IRT-FIT detects benchmark contamination with 97.9% power on MMLU (14K items) and identifies Gemini-1.5's 100% MMLU accuracy as contamination (lz*=+34.75) — a signal invisible to existing detectors that require model internals.\\\"\\n\\n## Venue Fit Risks\\n\\n- **EMNLP**: NLP evaluation methodology fits well. Risk: \\\"no new NLP model/technique\\\" → mitigate by positioning as foundational evaluation methodology with direct community impact (leaderboard integrity).\\n- **AAAI**: PSN-IRT was AAAI 2026 Oral — strong psychometrics+AI audience. Risk: less NLP-specific reviewer pool.\\n- **Cross-discipline concern**: IRT/psychometrics may be unfamiliar to ML reviewers → need self-contained exposition in Section 3 (IRT background), avoid jargon, provide intuitive explanations.\\n\\n## Anticipated Reviewer Concerns & Planned Responses\\n\\n| # | Concern | Response Strategy | Supporting Experiment |\\n|---|---------|------------------|----------------------|\\n| R1 | \\\"Just applying existing IRT to LLMs\\\" | Frame as establishing new operating point, not cross-domain transfer. Person-fit for contamination is unexplored. Downgrade \\\"cross-domain\\\" from contribution to background. | — |\\n| R2 | \\\"No ground truth contamination labels\\\" | Controlled contamination experiment (fine-tune clean models on benchmark items). Phase B anomalies are converging evidence, not proof. | exp-ctrl-contam |\\n| R3 | \\\"Power too low for small benchmarks\\\" | Present power function analysis as contribution, not limitation. Derive theoretical relationship. | exp-power-theory |\\n| R4 | \\\"Only 12 models\\\" | Expand to Open LLM Leaderboard v1 models + newly evaluated models. | exp-leaderboard-audit |\\n| R5 | \\\"SFT generalization smooths signal\\\" | Controlled experiment includes domain-level analysis. Discuss hard-item contamination resistance. | exp-ctrl-contam |\\n| R6 | \\\"Single-sided test misses full contamination\\\" | Two-sided detection framework is a core contribution. Gemini-1.5 case study demonstrates. | exp-two-sided |\\n| R7 | \\\"Post-RL contamination?\\\" | Hypothesis test: GRPO after SFT contamination on Qwen 3.5-9B. | exp-post-rl |\\n| R8 | \\\"4PL vs 3PL — does d parameter matter?\\\" | Ablation comparing 4PL vs 3PL(d=1) detection sensitivity. | exp-4pl-ablation |\\n\\n## Key Narrative Elements (from External Review)\\n\\n1. **Detection frontier framing** — Systematically rank all methods by information access level (binary < rephrased retest < token probs < logits < weights). IRT-FIT defines the bottom of this frontier.\\n2. **Leaderboard audit as core** — Full scan of Open LLM Leaderboard v1 (7K+ models) is IRT-FIT's unique capability. ConStat needs re-test, gray-box needs live model access. This is the biggest differentiator.\\n3. **Inverted-U as theoretical characterization** — Not just empirical observation. Derive from: (a) contamination→0%: signal drowned in sampling noise; (b) contamination→100%: identifiability collapse (uniform high performance indistinguishable from true high ability in binary responses).\\n4. **Scope precision** — Target: \\\"intentional SFT contamination / leaderboard gaming\\\". Pretraining exposure → smooth distributional improvement, not in scope. Honest scoping > vague claims.\\n\\n## MVP Evidence Summary\\n\\n- **Phase A (simulation)**: Null check passed (4PL compatible with lz* theory). MMLU power@15%=97.9%. Power ∝ n_items confirmed.\\n- **Phase B (real data)**: Gemini-1.5 (student_id=3) MMLU acc=1.000, θ=0.78, lz*=+34.75. Cross-benchmark: GSM8K lz*=-15.71, HumanEval lz*=-12.37. All benchmarks SD >> 0.5.\\n- **Key insight from MVP**: Two-sided detection is essential — full contamination produces lz* >> 0 (over-consistent), not lz* << 0 (aberrant).\\n\", \"total_chars\": 6737, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "071f4bfe-b515-43fe-b5b6-91018343eaa9",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "93c6941f-ab98-4ad0-aac7-6ab788f85c00",
  "sourceToolAssistantUUID": "071f4bfe-b515-43fe-b5b6-91018343eaa9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-20T09:10:59.400Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01UvS6rH61D4pB8PJqUDtbTN`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "literature_map.yaml",
  "max_chars": 20000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "93c6941f-ab98-4ad0-aac7-6ab788f85c00",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZVys7DsSmCCWhEspBk",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "c1225809-2139-44f0-be28-eadfc85b0e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GhiQ2Xjhp2wWtHhSYXaxGj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1912,
      "cache_read_input_tokens": 16090,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 1912,
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

_source line 12 · 2026-05-20T09:10:59.450Z_

<details><summary>↩ Tool result · `toolu_01UvS6rH61D4pB8PJqUDtbTN`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/literature_map.yaml\", \"content\": \"meta:\\n  last_updated: '2026-05-20T08:00:00Z'\\n  total_papers: 10\\ncategories:\\n  - key: irt-llm\\n    label: IRT for LLM Evaluation\\n  - key: contamination-detection\\n    label: Benchmark Contamination Detection\\n  - key: person-fit\\n    label: Person-Fit Statistics (Psychometrics)\\n  - key: post-rl-contamination\\n    label: Post-RL Contamination\\npapers:\\n  psnirt2026:\\n    title: \\\"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\\\"\\n    authors: []\\n    year: 2026\\n    venue: AAAI 2026 Oral\\n    url: \\\"https://arxiv.org/abs/2505.15055\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: psnirt2026\\n    category: irt-llm\\n    role: foundation\\n    relevance: \\\"Provides calibrated 4PL item parameters (a,b,c,d) for 41,871 items across 11 benchmarks — the item bank our method builds on\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  atlas2025:\\n    title: \\\"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2511.04689\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: atlas2025\\n    category: irt-llm\\n    role: background\\n    relevance: \\\"ATLAS uses IRT for adaptive testing efficiency; related IRT-for-LLM work but not person-fit\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  constat2024:\\n    title: \\\"ConStat: Performance-Based Contamination Detection in Large Language Models\\\"\\n    authors: []\\n    year: 2024\\n    venue: NeurIPS 2024\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: constat2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Performance-based contamination detector — primary baseline; requires re-test with modified items\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  minkprob2024:\\n    title: \\\"Detecting Pretraining Data from Large Language Models\\\"\\n    authors: []\\n    year: 2024\\n    venue: ICLR 2024\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: minkprob2024\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"Min-K% Probability MIA-based detector — baseline; requires token probabilities (not black-box)\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  wang2025fragility:\\n    title: \\\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\\\"\\n    authors: []\\n    year: 2025\\n    venue: \\\"\\\"\\n    url: \\\"https://arxiv.org/abs/2510.02386\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: wang2025fragility\\n    category: post-rl-contamination\\n    role: foundation\\n    relevance: \\\"Shows all MIA-based detectors fail under post-RL contamination — motivates our black-box approach\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  selfcritique2026:\\n    title: \\\"Detecting Data Contamination from Reinforcement Learning Post-training\\\"\\n    authors: []\\n    year: 2026\\n    venue: ICLR 2026\\n    url: \\\"https://arxiv.org/abs/2510.09259\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: selfcritique2026\\n    category: post-rl-contamination\\n    role: direct-competitor\\n    relevance: \\\"Self-Critique detects post-RL contamination via entropy-sequence policy collapse — baseline for post-RL setting\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  codec2026:\\n    title: \\\"Detecting Data Contamination in LLMs via In-Context Learning\\\"\\n    authors: []\\n    year: 2026\\n    venue: ICLR 2026\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: codec2026\\n    category: contamination-detection\\n    role: direct-competitor\\n    relevance: \\\"CoDeC measures ICL effects on memorized vs unseen data — baseline\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  sinharay2017:\\n    title: \\\"Which Statistic Should Be Used to Detect Item Preknowledge?\\\"\\n    authors: []\\n    year: 2017\\n    venue: JEBS\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: sinharay2017\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Power analysis for preknowledge detection — peak detection at 10-30% preknowledge; core theoretical basis\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  karabatsos2003:\\n    title: \\\"Comparing the Aberrant Response Detection Performance of Thirty-Six Person-Fit Statistics\\\"\\n    authors: []\\n    year: 2003\\n    venue: Applied Measurement in Education\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: karabatsos2003\\n    category: person-fit\\n    role: foundation\\n    relevance: \\\"Comprehensive comparison of 36 person-fit statistics — guides our choice of lz* as primary statistic\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\\n  hong2021lzm:\\n    title: \\\"Asymptotically Corrected Person Fit Statistics for Multidimensional Constructs with Simple Structure and Mixed Item Types\\\"\\n    authors: []\\n    year: 2021\\n    venue: Psychometrika\\n    url: \\\"\\\"\\n    doi: \\\"\\\"\\n    bibtex_key: hong2021lzm\\n    category: person-fit\\n    role: method-component\\n    relevance: \\\"lzm multiscale aggregation for multidimensional constructs — our Level 2 aggregated contamination score\\\"\\n    abstract: \\\"\\\"\\n    semantic_scholar_id: \\\"\\\"\\n    verified: false\\n    added_by: director\\n    added_at: '2026-05-20T08:00:00Z'\\n\", \"total_chars\": 5591, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1225809-2139-44f0-be28-eadfc85b0e7e",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "a96c097f-dbda-4847-a775-a7174016f532",
  "sourceToolAssistantUUID": "c1225809-2139-44f0-be28-eadfc85b0e7e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 13 · 2026-05-20T09:11:02.864Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Tzwzk7LS6a7WhJNfPUPgtu`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "report.md",
  "max_chars": 25000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a96c097f-dbda-4847-a775-a7174016f532",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZWPhp8YCzfPUZK2oVJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "6a1bcad1-5c09-4828-8cca-2058771d44bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN9mTMPgjCGP434VW2xmYA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4984,
      "cache_read_input_tokens": 18002,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 4984,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 55,
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

_source line 14 · 2026-05-20T09:11:02.924Z_

<details><summary>↩ Tool result · `toolu_01Tzwzk7LS6a7WhJNfPUPgtu`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/report.md\", \"content\": \"# Handover — 2026-05-20\\n\\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\\n\\n## 运行中\\n（无）\\n\\n## 待处理\\n（无）\\n\\n## 近期结论\\n- **phase_b_personfit** (success): Real LLM benchmark response data from PSN-IRT 12 models shows significant inter-model variation in person-fit statistics (lz*, outfit, infit), with specific models exhibiting anomalous patterns indicative of benchmark contamination — particularly Gemini-1.5 with accuracy-ability dissociation\\n- **sim_001** (negative): Under 4PL IRT model, lz* person-fit statistic can detect partial benchmark contamination (5-30% items) with >80% power at α=0.05, and detection power follows an inverted-U curve across contamination levels (low contamination undetectable, moderate contamination most detectable, high contamination mimics high ability)\\n  [null_check_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/null_check_summary.json) | [simulation_summary](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/data/simulation_summary.json) | [power_curves_combined](/api/workspace-files/projects/irt_personfit_contam/artifacts/sim_001/chart/power_curves.png)\\n\\n## 趋势\\n成功 1 / 负向 1 / 失败 0 / 共 2\\n\\n## 下一步\\n（无活跃 idea，请通过 ideas.md 添加）\\n\\n## 资源状态\\n（无服务器配置）\\n\\n## 告警\\n（无）\\n\", \"total_chars\": 1225, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a1bcad1-5c09-4828-8cca-2058771d44bb",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "8d096c9a-933a-4184-8df6-625e827f5edc",
  "sourceToolAssistantUUID": "6a1bcad1-5c09-4828-8cca-2058771d44bb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-20T09:11:03.220Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_0156JwXboXUnojJTkHTCzVF4`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "ROADMAP.md",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8d096c9a-933a-4184-8df6-625e827f5edc",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZWPhp8YCzfPUZK2oVJ",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "cfb8f5f5-a1a4-4e90-8dd6-9a84ded42cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BN9mTMPgjCGP434VW2xmYA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4984,
      "cache_read_input_tokens": 18002,
      "output_tokens": 205,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 4984
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 205,
          "cache_read_input_tokens": 18002,
          "cache_creation_input_tokens": 4984,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 4984,
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

_source line 16 · 2026-05-20T09:11:03.247Z_

<details><summary>↩ Tool result · `toolu_0156JwXboXUnojJTkHTCzVF4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/ROADMAP.md\", \"content\": \"# irt_personfit_contam — Research Dashboard\\n\\n> 最后更新: 2026-05-20 08:27 UTC | 更新原因: MVP 通过, 进入 research 阶段; 引用 paper_framing.md + experiment_plan.yaml; Dream 已启动\\n\\n## 核心方向\\n用 IRT person-fit 统计量在 information access 谱系最底层（仅 binary response pattern，无需 logits/weights/training data）检测 LLM benchmark 污染。详见 `paper_framing.md`。\\n\\n## 目标会议\\n- **Primary**: EMNLP 2026（用户确认 \\\"emnlp可行\\\"；ARR submission DDL 5/25 — 已追问可行性，等回复）\\n- **Fallback**: AAAI 2027 (abstract 7/21, full paper 7/28, ~10 weeks)\\n\\n## 当前阶段: Research（MVP 已通过 2026-05-20）\\n\\n### MVP 结果摘要\\n- **Phase A (simulation)**: Null check ✅, MMLU power@15%=97.9%, power ∝ n_items\\n- **Phase B (real data)**: Gemini-1.5 MMLU acc=1.0/θ=0.78/lz*=+34.75（全面污染信号）; 所有 benchmark SD >> 0.5; 多模型 lz* < -1.96\\n- **关键发现**: 需双侧检测（full contamination → lz* >> 0, partial → lz* << 0）\\n- **Inverted-U**: 仅 MMLU/HellaSwag 在 50% 以内展现真正下降（Reviewer 修正）\\n\\n### Core Claims (from paper_framing.md)\\n1. **Minimal-information detection**: Person-fit stats 在检测前沿最底层 work\\n2. **Detection characterization**: Power ∝ n_items + 双侧信号结构 + inverted-U 理论化\\n3. **Empirical prevalence**: Gemini-1.5 case study + 跨模型/跨 benchmark 污染模式\\n\\n### Experiment Plan Status (from experiment_plan.yaml)\\n**P0 (headline)**:\\n- [ ] `exp-two-sided` — 双侧检测框架（CPU, 进行中）\\n- [ ] `exp-extended-sim` — 扩展模拟 60-100%（CPU, 进行中）\\n- [ ] `exp-ctrl-contam` — 控制实验 Qwen3.5-9B + Gemma-4-31B（~80 GPU-hrs, depends on two-sided）\\n- [ ] `exp-power-theory` — Power 理论推导（CPU, depends on extended-sim）\\n\\n**P1 (robustness)**:\\n- [ ] `exp-leaderboard-audit` — Open LLM Leaderboard v1 扫描（~20 GPU-hrs）\\n- [ ] `exp-4pl-ablation` — 4PL vs 3PL 检测对比（CPU）\\n- [ ] `exp-baseline-comparison` — vs ConStat/Min-K%++（~30 GPU-hrs）\\n- [ ] `exp-multiscale-lzm` — 跨 benchmark 聚合统计量（CPU）\\n\\n**P2 (expanded scope)**:\\n- [ ] `exp-post-rl` — Post-RL 假设检验（~40 GPU-hrs）\\n- [ ] `exp-extra-benchmarks` — BBH/MATH 扩展（~10 GPU-hrs）\\n- [ ] `exp-domain-analysis` — MMLU domain-level 分析（CPU）\\n\\n### Dream 状态\\n- `dream_20260520T082549`: pending（full review mode），等待回调后再批准 P0 实验\\n\\n## 近期任务\\n- [ ] 等 Dream 回调 → 审阅模拟审稿 → 决定是否调整 framing/plan\\n- [ ] exp-two-sided 重分析（Agent 执行中）\\n- [ ] exp-extended-sim 扩展模拟（Agent 执行中）\\n- [ ] GPU 服务器 bjb2-36806 环境配置（Agent 执行中）\\n- [ ] 确认目标会议（等用户回复 EMNLP DDL 问题）\\n\\n## GPU 预算\\n- 已分配: 4× RTX 5090 32GB (bjb2-36806)\\n- P0: ~80 GPU-hrs | P1: ~50 GPU-hrs | P2: ~50 GPU-hrs | Total: ~180 GPU-hrs\\n- 当前使用: 0（环境配置中）\\n\\n## 12 模型身份 (PSN-IRT)\\n| ID | θ | Model | 异常信号 |\\n|----|---|-------|---------|\\n| 0 | 1.46 | 360GPT2-Pro | — |\\n| 1 | 3.77 | DeepSeek-V3 | θ 远超第二名 |\\n| 2 | 1.14 | Doubao-pro | — |\\n| 3 | 0.78 | **Gemini-1.5** | **MMLU acc=1.0, lz*=+34.75** |\\n| 4 | -3.38 | Gemma-2B-it | — |\\n| 5 | 1.73 | Hunyuan-Turbo | — |\\n| 6 | -1.37 | Mistral-7B-v0.1 | — |\\n| 7 | 0.93 | Moonshot-v1 | — |\\n| 8 | 0.96 | Qwen-Plus | — |\\n| 9 | -0.13 | Qwen2.5-3B | — |\\n| 10 | -1.89 | Vicuna-7B-v1.3 | — |\\n| 11 | 0.77 | Yi-Lightning | — |\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-20 | Phase B 必须用 benchmark-specific θ (MLE)，不能用 PSN-IRT | exp-two-sided |\\n| D005 | 2026-05-20 | Phase B Pass + 发现双侧检测需求: Model 3 MMLU 100% acc/lz* | sim_001, phase_b_personfit |\\n| D004 | 2026-05-20 | Phase A Partial Pass: 方法机制验证成功，power 随 n_items 递减为 | sim_001 |\\n| D003 | 2026-05-20 | 修正 benchmark 分类: ARC-C 降为小(295 items); MVP 不混用 Tru | — |\\n| D002 | 2026-05-20 | 根据 Reviewer 审查细化 MVP: 加入 PSN-IRT 参数 null distribut | — |\\n| D001 | 2026-05-20 | MVP 采用两阶段验证: Phase A 模拟验证（无GPU）+ Phase B 真实数据探测 | — |\\n\\n\", \"total_chars\": 3399, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cfb8f5f5-a1a4-4e90-8dd6-9a84ded42cb1",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "b4c93318-17de-446c-8451-e14adb8deb99",
  "sourceToolAssistantUUID": "cfb8f5f5-a1a4-4e90-8dd6-9a84ded42cb1",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-20T09:11:06.844Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01YAXnyWFCgXtcn4WcauduTg`</summary>

```json
{
  "project": "irt_personfit_contam",
  "file": "memory.md",
  "max_chars": 15000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b4c93318-17de-446c-8451-e14adb8deb99",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZWg4a27PT252qFJFJ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "e1b8dbad-661c-48ad-a874-793f9b4669bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bp3Gfq931DPKqHA97YnaGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 22986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 18 · 2026-05-20T09:11:06.899Z_

<details><summary>↩ Tool result · `toolu_01YAXnyWFCgXtcn4WcauduTg`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/memory.md\", \"content\": \"# Memory — irt_personfit_contam\\n\\n## OOM 教训 (2026-05-20)\\n- 7.6GB RAM 机器上，N_SIM×n_items float64 矩阵不能一次性分配。MMLU 10K×14042×8B ≈ 1.07GB 单个矩阵，compute_lz_star 内部创建 ~7 个同尺寸中间数组 → OOM\\n- 解决方案：BATCH_SIZE=500 分批计算 + N_SIM 降至 2000（统计效力足够）\\n- generate_response 和 compute_lz_star 都需要分批\\n\\n## sim_001 关键发现 (2026-05-20)\\n- **Null check 全通过**：PSN-IRT 神经网络估计的 4PL 参数与经典 IRT 兼容，lz* ≈ N(0,1)\\n  - 大 benchmark（GSM8K/HellaSwag/MMLU）KS p 全部 > 0.01\\n  - 小 benchmark（HumanEval/ARC-C）KS p < 0.01，但属预期（items 太少，CLT 近似弱）\\n- **检测力与 n_items 强正相关**：MMLU(14042)=97.9% >> HellaSwag(10042)=73.3% >> GSM8K(1319)=57.8% >> ARC-C(295)=12.9%\\n- **Inverted-U 所有 benchmark 可观测**：power 在 25-50% contamination 达峰，100% 全部 NaN（全答对 → MLE 不收敛）\\n- **100% contamination 导致全 NaN**：所有 response = 1 → theta_hat 退化到 boundary → lz* 无效。这不是 bug，是 IRT 的固有限制\\n- **Hypothesis 部分证伪**：\\\">80% power at 15% contamination\\\" 仅 MMLU 达标，HellaSwag/GSM8K 未达标。但方法确实 work，只是 power 阈值设得太激进\\n\\n## PSN-IRT 12 模型身份 (2026-05-20)\\n\\n**来源**：arXiv:2505.15055 (AAAI 2026 Oral)，GitHub repo `Joe-Hall-Lee/PSN-IRT`\\n**识别方法**：论文 Section 4.1 列出全部 12 个模型名；`data/combine.csv` 行序 = student_id，经验证为字母序排列。DeepSeek-V3 = student_id=1 由论文 Section 5.2 确认（\\\"ability well above 3.0\\\"）。\\n\\n| student_id | θ | 正确率 | 模型名称 | 类型 | 置信度 |\\n|---|---|---|---|---|---|\\n| 0 | 1.46 | 80.6% | 360GPT2-Pro | API 强模型 | ✅ 确定 |\\n| 1 | 3.77 | 85.7% | DeepSeek-V3 | API 强模型 | ✅ 确定（论文确认） |\\n| 2 | 1.14 | 78.9% | Doubao-pro | API 强模型 | ✅ 确定 |\\n| 3 | 0.78 | 84.5% | Gemini-1.5 | API 强模型 | ✅ 确定 |\\n| 4 | -3.38 | 23.1% | Gemma-2B-it | 开源弱模型(2B) | ✅ 确定 |\\n| 5 | 1.73 | 82.1% | Hunyuan-Turbo | API 强模型 | ✅ 确定 |\\n| 6 | -1.37 | 40.0% | Mistral-7B-Instruct-v0.1 | 开源弱模型(7B) | ✅ 确定 |\\n| 7 | 0.93 | 77.0% | Moonshot-v1 | API 强模型 | ✅ 确定 |\\n| 8 | 0.96 | 76.3% | Qwen-Plus | API 强模型 | ✅ 确定 |\\n| 9 | -0.13 | 60.4% | Qwen2.5-3B-Instruct | 开源弱模型(3B) | ✅ 确定 |\\n| 10 | -1.89 | 31.6% | Vicuna-7B-v1.3 | 开源弱模型(7B) | ✅ 确定 |\\n| 11 | 0.77 | 75.2% | Yi-Lightning | API 强模型 | ✅ 确定 |\\n\\n### 识别依据\\n\\n1. **论文明确列出**：Section 4.1 给出全部 12 个模型名，分为 8 个强模型 + 4 个弱模型\\n2. **字母序验证**：`combine.csv` 12 行对应 student_id 0-11，按模型名字母序排列\\n3. **交叉验证**：\\n   - DeepSeek-V3 (id=1) θ=3.77 → 论文称 \\\"ability well above 3.0\\\" ✅\\n   - 4 个弱模型 (Gemma-2B, Mistral-7B, Qwen2.5-3B, Vicuna-7B) 对应 id=4,6,9,10，正确率 23-60% ✅\\n   - 8 个强模型对应 id=0,1,2,3,5,7,8,11，正确率 75-86% ✅\\n\\n### 异常 response pattern 观察\\n\\nGemini-1.5 (id=3) 有显著的 raw accuracy 与 IRT ability 不一致：\\n- 正确率排名 #2 (84.5%)，但 θ 排名仅 #7 (0.78)\\n- 这意味着 4PL IRT 模型检测到 Gemini-1.5 的 response pattern 异常（如：容易题答错、难题答对）\\n- 与之对比：DeepSeek-V3 正确率 #1 (85.7%) 且 θ #1 (3.77)，response pattern 一致性强\\n\\n### 已知污染讨论\\n\\n- **DeepSeek-V3**：社区讨论过 GSM8K/MMLU 可能的训练集重叠，但无定论。θ=3.77 远超第二名(1.73)值得关注\\n- **Qwen 系列**：Qwen-Plus 和 Qwen2.5-3B 的训练数据规模巨大，web crawl 可能包含 benchmark 数据\\n- **Gemini-1.5**：IRT ability 与 raw accuracy 的大幅偏差是最值得深入分析的信号\\n- **Vicuna-7B-v1.3**：基于 LLaMA-1，LLaMA-1 训练数据已知包含部分 benchmark 相关文本\\n\", \"total_chars\": 2792, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "e1b8dbad-661c-48ad-a874-793f9b4669bd",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "e4117f7b-8875-4d78-9e8a-4e674693328f",
  "sourceToolAssistantUUID": "e1b8dbad-661c-48ad-a874-793f9b4669bd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-20T09:11:07.137Z_

<details open><summary>🔧 Tool call — Glob · `toolu_01LmWMLfxAVkQ2PHiVsLKEZK`</summary>

```json
{
  "pattern": "**/*.tex",
  "path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e4117f7b-8875-4d78-9e8a-4e674693328f",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZWg4a27PT252qFJFJ7",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f834c022-8e54-4d8f-b1a8-e67f79c915dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bp3Gfq931DPKqHA97YnaGk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2979,
      "cache_read_input_tokens": 22986,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 2979,
        "ephemeral_1h_input_tokens": 0
      },
      "output_tokens": 66,
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

_source line 20 · 2026-05-20T09:11:07.252Z_

<details><summary>↩ Tool result · `toolu_01LmWMLfxAVkQ2PHiVsLKEZK`</summary>

```text
artifacts/dream_reports/dream_20260520T082549/best/paper.tex
artifacts/dream_reports/dream_20260520T082549/median/paper.tex
artifacts/dream_reports/dream_20260520T082549/worst/paper.tex
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f834c022-8e54-4d8f-b1a8-e67f79c915dd",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "90c2d650-5471-4b20-b34d-32bc0357dad0",
  "sourceToolAssistantUUID": "f834c022-8e54-4d8f-b1a8-e67f79c915dd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 21 · 2026-05-20T09:11:10.053Z_

<details open><summary>🔧 Tool call — Read · `toolu_01AyAvb6GLsJXpMh8bzRZ72s`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "90c2d650-5471-4b20-b34d-32bc0357dad0",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZWxrcoLtEbxgyd5jQB",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "3165d626-9831-4c51-b34b-efeb647665a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QEbUtoZNMsvQpUhUC8qHmg",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2495,
      "cache_read_input_tokens": 25965,
      "output_tokens": 122,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2495
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 122,
          "cache_read_input_tokens": 25965,
          "cache_creation_input_tokens": 2495,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2495,
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

_source line 22 · 2026-05-20T09:11:10.094Z_

<details><summary>↩ Tool result · `toolu_01AyAvb6GLsJXpMh8bzRZ72s`</summary>

```text
1	\documentclass[11pt,a4paper]{article}
2	\usepackage[utf8]{inputenc}
3	\usepackage[T1]{fontenc}
4	\usepackage{amsmath,amssymb,amsfonts}
5	\usepackage{booktabs}
6	\usepackage{graphicx}
7	\usepackage{multirow}
8	\usepackage{tabularx}
9	\usepackage[margin=2.5cm]{geometry}
10	\usepackage{natbib}
11	\usepackage{hyperref}
12	\usepackage{xcolor}
13	\usepackage{array}
14	\usepackage{caption}
15	
16	\newcolumntype{R}{>{\raggedleft\arraybackslash}p{1.2cm}}
17	\newcolumntype{L}{>{\raggedright\arraybackslash}p{2.8cm}}
18	
19	\title{IRT-FIT: Detecting Benchmark Contamination in Large Language Models\\via Item Response Theory Person-Fit Statistics}
20	
21	\author{Anonymous}
22	\date{}
23	
24	\begin{document}
25	\maketitle
26	
27	% ============================================================
28	\begin{abstract}
29	Benchmark contamination undermines the reliability of LLM evaluation, yet all existing detection methods require privileged access---training data, token probabilities, model weights, or specially crafted prompts. We establish the \emph{minimal-information operating point} on the contamination detection frontier by repurposing Item Response Theory (IRT) person-fit statistics, which require only binary (correct/incorrect) response patterns. Our framework, \textbf{IRT-FIT}, introduces three contributions: (1) a two-sided detection framework capturing both partial contamination (aberrant patterns, $l_{z}^{*} \ll 0$) and full contamination (over-consistent patterns, $l_{z}^{*} \gg 0$); (2) a theoretical characterization showing detection power is a predictable function of benchmark size ($n_{\text{items}}$) and contamination level, with an analytically derivable inverted-U signal structure ($R^2=0.97$); and (3) a large-scale audit of 2{,}847 Open LLM Leaderboard models revealing a 12\% overall contamination flag rate. In controlled experiments with ground-truth contamination (QLoRA SFT on Qwen3.5-9B and Gemma-4-31B), IRT-FIT achieves AUROC 0.96 at 15\% contamination and 0.82 at 5\%---outperforming ConStat (0.83/0.61) and Min-K\%++ (0.88/0.72) while requiring strictly less information. The person-fit signal survives post-RL training (AUROC 0.92 after GRPO), whereas MIA-based methods degrade to near-chance (AUROC 0.54). IRT-FIT is the only method that simultaneously addresses partial, full, and post-RL contamination at the minimal-information level.
30	\end{abstract}
31	
32	% ============================================================
33	\section{Introduction}
34	\label{sec:intro}
35	
36	Benchmark contamination---the inclusion of evaluation data in training corpora---is a growing threat to LLM evaluation integrity. As training data scales to trillions of tokens and benchmarks proliferate, the probability of inadvertent or intentional overlap increases. This undermines the fundamental assumption that benchmark performance reflects genuine capability.
37	
38	Existing detection methods span a spectrum of information requirements. N-gram overlap methods require access to training data. Membership inference attacks (MIA) and Min-K\%++ \citep{shi2024detecting} require token-level log-probabilities. Time Travel probing \citep{oren2024proving} requires specially crafted prompts. ConStat \citep{dekoninck2024constat} requires the ability to re-test models on rephrased items. \citet{wang2025reassessing} demonstrate that all MIA-based methods fail under post-RL contamination, highlighting the fragility of token-level signals.
39	
40	A contaminated LLM answering benchmark questions is functionally analogous to an examinee with item preknowledge---a problem studied for decades in psychometrics under the rubric of \emph{person-fit analysis}. Person-fit statistics such as $l_z^*$ \citep{snijders2001person} detect aberrant response patterns: examinees who answer difficult items correctly while failing easy ones, or who answer all items correctly including those far beyond their estimated ability. These statistics require only binary response data and a calibrated item bank---precisely the information available from standard LLM benchmark evaluation.
41	
42	We introduce \textbf{IRT-FIT}, a framework that establishes the \emph{minimal-information operating point} on the contamination detection frontier. Our contributions are:
43	
44	\begin{enumerate}
45	    \item \textbf{Minimal-information detection.} We show that IRT person-fit statistics detect benchmark contamination using only binary response patterns, achieving AUROC 0.96 at 15\% contamination---outperforming methods requiring token probabilities or re-testing.
46	    \item \textbf{Theoretical characterization.} We derive an analytic power formula relating detection power to benchmark size and contamination level ($R^2=0.97$), and prove that the inverted-U signal structure has a predictable inflection point determined by item difficulty distributions.
47	    \item \textbf{Large-scale empirical evidence.} We audit 2{,}847 Open LLM Leaderboard models, revealing a 12\% contamination flag rate increasing from 6\% (2023 Q1) to 18\% (2024 Q1). We identify Gemini-1.5's 100\% MMLU accuracy as systematic contamination ($l_z^*=+34.75$, $\hat{\theta}=0.78$).
48	\end{enumerate}
49	
50	% ============================================================
51	\section{Background}
52	\label{sec:background}
53	
54	\subsection{Item Response Theory}
55	
56	IRT models the probability of a correct response as a function of examinee ability $\theta$ and item parameters. We adopt the four-parameter logistic (4PL) model:
57	\begin{equation}
58	P_i(\theta) = c_i + (d_i - c_i) \cdot \frac{1}{1 + e^{-a_i(\theta - b_i)}}
59	\label{eq:4pl}
60	\end{equation}
61	where $a_i$ is discrimination, $b_i$ is difficulty, $c_i$ is the guessing parameter, and $d_i$ is the feasibility (upper asymptote) parameter. The 3PL model is the special case $d_i=1$.
62	
63	\subsection{Person-Fit Statistics}
64	
65	The $l_z$ statistic \citep{drasgow1985appropriateness} measures the fit of an individual response pattern to the IRT model:
66	\begin{equation}
67	l_z = \frac{\sum_{i=1}^{n} \left[ x_i \log P_i(\hat{\theta}) + (1-x_i) \log(1-P_i(\hat{\theta})) \right] - E[l_0]}{SD[l_0]}
68	\end{equation}
69	where $x_i \in \{0,1\}$ is the response to item $i$ and $\hat{\theta}$ is the MLE of ability. \citet{snijders2001person} derived the corrected statistic $l_z^*$ that accounts for estimation error in $\hat{\theta}$, yielding $l_z^* \sim N(0,1)$ under the null hypothesis of model fit.
70	
71	% ============================================================
72	\section{Method: IRT-FIT}
73	\label{sec:method}
74	
75	\subsection{Two-Sided Detection Framework}
76	
77	Traditional person-fit analysis tests only $l_z^* < c_{\alpha}$ (aberrant patterns). We extend to two-sided testing because contamination produces two distinct signal regimes:
78	
79	\begin{itemize}
80	    \item \textbf{Partial contamination} ($l_z^* \ll 0$): The model memorizes a subset of items, answering difficult contaminated items correctly while failing easy non-contaminated items---an aberrant pattern.
81	    \item \textbf{Full contamination} ($l_z^* \gg 0$): The model memorizes all items, producing a response pattern that is \emph{over-consistent}---all items correct, including those far beyond estimated ability.
82	\end{itemize}
83	
84	We apply the two-sided test $|l_z^*| > c_{\alpha/2}$ with Benjamini--Hochberg FDR control for multiple comparisons across models and benchmarks.
85	
86	\subsection{Multiscale Aggregation ($l_{zm}$)}
87	
88	Following \citet{hong2021multiscale}, we aggregate per-benchmark $l_z^*$ values into a single model-level index:
89	\begin{equation}
90	l_{zm} = \frac{1}{\sqrt{K}} \sum_{k=1}^{K} |l_{z,k}^*|
91	\end{equation}
92	where $K$ is the number of benchmarks evaluated. Under the null, $l_{zm}$ is approximately standard normal (verified by Kolmogorov--Smirnov test, $p=0.312$).
93	
94	\subsection{Power Theory}
95	
96	Building on Snijders' variance formula, we derive the detection power as:
97	\begin{equation}
98	\text{power} \approx \Phi\!\left(\frac{\delta \sqrt{n}}{\sigma_{l_z^*}} - z_{\alpha}\right)
99	\label{eq:power}
100	\end{equation}
101	where $\delta = E[\log L_{\text{contam}} - \log L_{\text{clean}}]$ per item is the expected log-likelihood shift induced by contamination, and $n$ is the number of items. The inverted-U inflection point $c^*$ satisfies:
102	\begin{equation}
103	c^* = \arg\min_{c} \left| E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=c\right] - E_\theta\!\left[\sum_i f(x_i, P_i) \mid \text{contam}=0\right] \right|
104	\end{equation}
105	where $f(x_i, P_i) = x_i \log P_i + (1-x_i)\log(1-P_i)$.
106	
107	% ============================================================
108	\section{Controlled Contamination Experiments}
109	\label{sec:controlled}
110	
111	\subsection{Ground-Truth Contamination}
112	\label{sec:ctrl-contam}
113	
114	We inject known contamination via QLoRA SFT on two base models (Qwen3.5-9B and Gemma-4-31B), training on 0\%/5\%/10\%/15\%/25\%/50\% of MMLU items to establish a ground-truth contamination--$l_z^*$ mapping.
115	
116	\begin{table}[t]
117	\centering
118	\caption{Controlled contamination: $l_z^*$ by model and contamination level (MMLU).}
119	\label{tab:ctrl-contam}
120	\small
121	\begin{tabular}{llrrrr}
122	\toprule
123	\textbf{Model} & \textbf{Contam.} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{Flag} \\
124	\midrule
125	Qwen3.5-9B & 0\% & .721 & 1.42 & 0.08 & .047 \\
126	Qwen3.5-9B & 5\% & .738 & 1.51 & $-$3.72 & .82 \\
127	Qwen3.5-9B & 10\% & .756 & 1.59 & $-$6.45 & .94 \\
128	Qwen3.5-9B & 15\% & .764 & 1.63 & $-$8.91 & .97 \\
129	Qwen3.5-9B & 25\% & .787 & 1.71 & $-$11.34 & .99 \\
130	Qwen3.5-9B & 50\% & .831 & 1.89 & $-$4.82 & .87 \\
131	\midrule
132	Gemma-4-31B & 0\% & .793 & 1.81 & 0.15 & .041 \\
133	Gemma-4-31B & 5\% & .808 & 1.88 & $-$3.21 & .78 \\
134	Gemma-4-31B & 15\% & .831 & 1.97 & $-$7.63 & .95 \\
135	Gemma-4-31B & 50\% & .874 & 2.14 & $-$5.14 & .84 \\
136	\bottomrule
137	\end{tabular}
138	\end{table}
139	
140	\begin{table}[t]
141	\centering
142	\caption{Detection performance (AUROC) by contamination level.}
143	\label{tab:auroc}
144	\small
145	\begin{tabular}{lrrrr}
146	\toprule
147	\textbf{Contam.} & \textbf{Qwen} & \textbf{Gemma} & \textbf{Pooled} & \textbf{Cohen's $d$} \\
148	\midrule
149	5\% & 0.84 & 0.80 & 0.82 & 1.1 \\
150	10\% & 0.93 & 0.91 & 0.92 & 1.8 \\
151	15\% & 0.97 & 0.95 & 0.96 & 2.3 \\
152	25\% & 0.99 & 0.98 & 0.99 & 2.8 \\
153	50\% & 0.94 & 0.91 & 0.93 & 1.6 \\
154	\bottomrule
155	\end{tabular}
156	\end{table}
157	
158	Table~\ref{tab:ctrl-contam} shows a monotonic increase in $|l_z^*|$ from 0\% to 25\% contamination, followed by a decrease at 50\%---the inverted-U pattern. Both models exhibit consistent behavior (effect size difference $<$15\%), ruling out model-specific artifacts. False positive rate at $\alpha=0.05$ is well-calibrated: 0.047 (Qwen) and 0.041 (Gemma). The minimum detectable contamination level is 5\% (AUROC 0.82, Table~\ref{tab:auroc}).
159	
160	\begin{table}[t]
161	\centering
162	\caption{Contamination selectivity: accuracy change on contaminated vs.\ non-contaminated items (Qwen3.5-9B).}
163	\label{tab:selectivity}
164	\small
165	\begin{tabular}{lrrrr}
166	\toprule
167	\textbf{Contam.} & \multicolumn{2}{c}{\textbf{Contam.\ Items}} & \multicolumn{2}{c}{\textbf{Non-Contam.\ Items}} \\
168	\cmidrule(lr){2-3} \cmidrule(lr){4-5}
169	 & Before & Lift & Before & Lift \\
170	\midrule
171	5\% & .56 & +.31 & .73 & +.014 \\
172	15\% & .54 & +.30 & .73 & +.018 \\
173	25\% & .55 & +.31 & .73 & +.024 \\
174	50\% & .57 & +.31 & .73 & +.037 \\
175	\bottomrule
176	\end{tabular}
177	\end{table}
178	
179	Table~\ref{tab:selectivity} confirms that SFT contamination is highly selective: accuracy on contaminated items increases by $\sim$31 percentage points, while non-contaminated items show only 1.4--3.7\% generalization. The generalization ratio is 0.12, far too small to smooth the aberrant pattern.
180	
181	\subsection{Inverted-U Signal Characterization}
182	\label{sec:inverted-u}
183	
184	We extend simulations to 60\%/75\%/90\%/100\% contamination levels, characterizing the complete inverted-U curve across four benchmarks.
185	
186	\begin{table}[t]
187	\centering
188	\caption{$l_z^*$ as a function of contamination level (mean $\pm$ SD, 100 replications).}
189	\label{tab:inverted-u}
190	\small
191	\begin{tabular}{lrrrr}
192	\toprule
193	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
194	\midrule
195	0\% & 0.01 & 0.03 & $-$0.02 & 0.01 \\
196	5\% & $-$3.41 & $-$1.82 & $-$1.34 & $-$0.42 \\
197	10\% & $-$6.12 & $-$3.45 & $-$2.51 & $-$0.78 \\
198	15\% & $-$8.31 & $-$4.72 & $-$3.38 & $-$1.02 \\
199	25\% & $-$12.08 & $-$6.21 & $-$4.53 & $-$1.31 \\
200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3165d626-9831-4c51-b34b-efeb647665a5",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "0a31211d-b409-456b-acc9-b0c249c10181",
  "sourceToolAssistantUUID": "3165d626-9831-4c51-b34b-efeb647665a5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-20T09:11:15.349Z_

<details open><summary>🔧 Tool call — Read · `toolu_0122CpRWYPckAS1o96QXT8o8`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "offset": 200,
  "limit": 400
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a31211d-b409-456b-acc9-b0c249c10181",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZXBaavnzzc1HKS1gNr",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2a778347-6761-4053-8bc2-3ede91615fb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EYRTFoSQYMMLof6F18dKSt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5011,
      "cache_read_input_tokens": 28460,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 5011
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 28460,
          "cache_creation_input_tokens": 5011,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 5011,
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

_source line 24 · 2026-05-20T09:11:15.365Z_

<details><summary>↩ Tool result · `toolu_0122CpRWYPckAS1o96QXT8o8`</summary>

```text
200	50\% & $-$5.73 & $-$2.89 & $-$1.67 & $-$0.43 \\
201	60\% & $-$1.24 & 0.82 & $-$0.34 & 0.21 \\
202	75\% & 8.42 & 5.67 & 3.21 & 1.12 \\
203	90\% & 19.31 & 12.45 & 6.78 & 2.34 \\
204	100\% & 28.50 & 18.20 & 8.70 & 3.01 \\
205	\bottomrule
206	\end{tabular}
207	\end{table}
208	
209	\begin{table}[t]
210	\centering
211	\caption{Two-sided detection power at various contamination levels.}
212	\label{tab:two-sided-power}
213	\small
214	\begin{tabular}{lrrrr}
215	\toprule
216	\textbf{Contam.} & \textbf{MMLU} & \textbf{HSwag} & \textbf{GSM8K} & \textbf{ARC-C} \\
217	\midrule
218	5\% & .780 & .340 & .220 & .060 \\
219	15\% & .979 & .733 & .578 & .129 \\
220	25\% & .998 & .891 & .743 & .201 \\
221	50\% & .872 & .514 & .298 & .080 \\
222	75\% & .991 & .934 & .712 & .187 \\
223	100\% & 1.000 & .998 & .962 & .478 \\
224	\bottomrule
225	\end{tabular}
226	\end{table}
227	
228	Tables~\ref{tab:inverted-u} and \ref{tab:two-sided-power} reveal the inverted-U structure. The $l_z^*$ signal peaks negatively around 25\% contamination (MMLU: $-$12.08), crosses zero near 60--65\%, and becomes strongly positive at high contamination (100\%: +28.50). The inflection point varies by benchmark: 0.65 (MMLU), 0.60 (HellaSwag), 0.70 (GSM8K), consistent with differences in item difficulty distributions. Two-sided power dips at the inflection point (50\% contamination) but recovers for higher levels, whereas one-sided testing would have zero power above the inflection.
229	
230	\subsection{Power Theory Derivation}
231	\label{sec:power-theory}
232	
233	Equation~\ref{eq:power} predicts detection power as a function of $n_{\text{items}}$. Table~\ref{tab:power-theory} shows the theory fits simulation data with $R^2=0.97$.
234	
235	\begin{table}[t]
236	\centering
237	\caption{Theoretical vs.\ simulated power at 15\% contamination.}
238	\label{tab:power-theory}
239	\small
240	\begin{tabular}{rrrr}
241	\toprule
242	$n_{\text{items}}$ & \textbf{Predicted} & \textbf{Simulated} & \textbf{$|\Delta|$} \\
243	\midrule
244	100 & .089 & .092 & .003 \\
245	500 & .312 & .298 & .014 \\
246	1{,}000 & .491 & .503 & .012 \\
247	1{,}319 & .578 & .578 & .000 \\
248	5{,}000 & .862 & .851 & .011 \\
249	10{,}042 & .964 & .958 & .006 \\
250	14{,}042 & .981 & .979 & .002 \\
251	\bottomrule
252	\end{tabular}
253	\end{table}
254	
255	\begin{table}[t]
256	\centering
257	\caption{Inverted-U inflection point: predicted vs.\ observed.}
258	\label{tab:inflection}
259	\small
260	\begin{tabular}{lrrrr}
261	\toprule
262	\textbf{Benchmark} & $n$ & \textbf{Pred.} & \textbf{Obs.} & $|\Delta|$ \\
263	\midrule
264	MMLU & 14{,}042 & 0.64 & 0.65 & 0.01 \\
265	HellaSwag & 10{,}042 & 0.59 & 0.60 & 0.01 \\
266	GSM8K & 1{,}319 & 0.68 & 0.70 & 0.02 \\
267	ARC-C & 1{,}172 & 0.62 & 0.64 & 0.02 \\
268	HumanEval & 164 & 0.61 & 0.63 & 0.02 \\
269	\bottomrule
270	\end{tabular}
271	\end{table}
272	
273	\begin{table}[t]
274	\centering
275	\caption{Minimum $n_{\text{items}}$ for 80\% power at various contamination levels.}
276	\label{tab:min-n}
277	\small
278	\begin{tabular}{lrr}
279	\toprule
280	\textbf{Contam.} & \textbf{Theory} & \textbf{Simulation} \\
281	\midrule
282	5\% & 9{,}800 & 10{,}200 \\
283	10\% & 4{,}700 & 4{,}900 \\
284	15\% & 3{,}200 & 3{,}350 \\
285	25\% & 1{,}800 & 1{,}900 \\
286	\bottomrule
287	\end{tabular}
288	\end{table}
289	
290	Table~\ref{tab:inflection} shows the inflection point can be predicted from item difficulty distributions alone, with error $\leq$0.02. Table~\ref{tab:min-n} provides practitioners with concrete guidance: detecting 15\% contamination requires $\geq$3{,}200 items; detecting 5\% contamination requires $\geq$9{,}800 items. This explains why ARC-C (1{,}172 items) yields only 12.9\% power---not a method failure, but insufficient information.
291	
292	% ============================================================
293	\section{Comparisons and Robustness}
294	\label{sec:comparison}
295	
296	\subsection{Baseline Comparison}
297	\label{sec:baselines}
298	
299	\begin{table}[t]
300	\centering
301	\caption{Baseline comparison on controlled contamination ground truth.}
302	\label{tab:baseline}
303	\small
304	\begin{tabular}{llrrrr}
305	\toprule
306	\textbf{Method} & \textbf{Info Required} & \textbf{5\%} & \textbf{15\%} & \textbf{25\%} & \textbf{Type-I} \\
307	\midrule
308	IRT-FIT & binary & .82 & .96 & .99 & .042 \\
309	ConStat & binary + retest & .61 & .83 & .91 & .053 \\
310	Min-K\%++ & token log-probs & .72 & .88 & .95 & .048 \\
311	\bottomrule
312	\end{tabular}
313	\end{table}
314	
315	\begin{table}[t]
316	\centering
317	\caption{Detection frontier: information access vs.\ detection power (AUROC at 15\% contam.).}
318	\label{tab:frontier}
319	\small
320	\begin{tabular}{llrl}
321	\toprule
322	\textbf{Info Level} & \textbf{Method} & \textbf{AUROC} & \textbf{Scalability} \\
323	\midrule
324	Binary only & IRT-FIT & .96 & Any model w/ scores \\
325	Binary + retest & ConStat & .83 & Requires live access \\
326	Token probs & Min-K\%++ & .88 & Requires API logprobs \\
327	Training data & N-gram & --- & Requires training data \\
328	Weights & Probing & --- & Requires open weights \\
329	\bottomrule
330	\end{tabular}
331	\end{table}
332	
333	IRT-FIT achieves the highest AUROC while requiring the least information (Table~\ref{tab:baseline}). The advantage over ConStat (+0.13 at 15\%) stems from IRT-FIT's use of item-level response patterns rather than aggregate performance statistics. The advantage over Min-K\%++ (+0.08) is notable given that Min-K\%++ has access to richer token-level information. Table~\ref{tab:frontier} positions these results on the detection frontier.
334	
335	\subsection{Post-RL Robustness}
336	\label{sec:post-rl}
337	
338	\citet{wang2025reassessing} show that MIA-based methods fail after reinforcement learning. We test whether IRT-FIT survives post-RL by applying GRPO training to a contaminated Qwen3.5-9B (15\% MMLU SFT contamination).
339	
340	\begin{table}[t]
341	\centering
342	\caption{Pre- vs.\ post-RL person-fit (Qwen3.5-9B, 15\% MMLU contamination).}
343	\label{tab:post-rl}
344	\small
345	\begin{tabular}{lrrrrr}
346	\toprule
347	\textbf{Stage} & \textbf{Acc.} & $\hat{\theta}$ & $l_z^*$ & \textbf{AUROC} & \textbf{Power} \\
348	\midrule
349	Clean & .721 & 1.42 & 0.08 & --- & --- \\
350	Post-SFT & .764 & 1.63 & $-$8.91 & .96 & .97 \\
351	Post-SFT+GRPO & .776 & 1.71 & $-$7.12 & .92 & .91 \\
352	\bottomrule
353	\end{tabular}
354	\end{table}
355	
356	\begin{table}[t]
357	\centering
358	\caption{Person-fit vs.\ MIA: post-RL robustness comparison.}
359	\label{tab:post-rl-comparison}
360	\small
361	\begin{tabular}{lrrrl}
362	\toprule
363	\textbf{Method} & \textbf{Pre-RL} & \textbf{Post-RL} & \textbf{Retain.} & \textbf{Info} \\
364	\midrule
365	IRT-FIT & .96 & .92 & 96\% & binary \\
366	Min-K\%++ & .88 & .62 & 70\% & token probs \\
367	MIA (ref.) & .71 & .54 & 76\% & token probs + ref \\
368	\bottomrule
369	\end{tabular}
370	\end{table}
371	
372	GRPO reduces the $l_z^*$ signal by only 20\% ($-$8.91 $\to$ $-$7.12), retaining 96\% of AUROC (Table~\ref{tab:post-rl}). In contrast, MIA degrades to near-chance (0.54) because RL recalibrates token-level probability distributions while leaving binary response patterns largely intact (Table~\ref{tab:post-rl-comparison}). Item-level analysis confirms: contaminated items retain 97.6\% of their accuracy after GRPO (0.84 $\to$ 0.82), while non-contaminated items gain +1\%. RL changes \emph{how confident} the model is, but not \emph{whether it answers correctly} on memorized items.
373	
374	\subsection{4PL vs.\ 3PL Ablation}
375	\label{sec:ablation}
376	
377	\begin{table}[t]
378	\centering
379	\caption{4PL vs.\ 3PL detection performance.}
380	\label{tab:4pl-3pl}
381	\small
382	\begin{tabular}{lrrr}
383	\toprule
384	\textbf{Metric} & \textbf{4PL} & \textbf{3PL} & $\Delta$ \\
385	\midrule
386	AUROC @ 15\% & .960 & .910 & +.050 \\
387	False alarm ($\alpha$=.05) & .042 & .078 & $-$.036 \\
388	Power @ 15\% MMLU & .979 & .934 & +.045 \\
389	Power @ 5\% MMLU & .780 & .690 & +.090 \\
390	Mean $|l_z^*|$ clean & 0.83 & 1.17 & $-$0.34 \\
391	Mean $|l_z^*|$ contam.\ 15\% & 8.91 & 8.04 & +0.87 \\
392	\bottomrule
393	\end{tabular}
394	\end{table}
395	
396	\begin{table}[t]
397	\centering
398	\caption{Impact of $d$ parameter by item difficulty band.}
399	\label{tab:d-param}
400	\small
401	\begin{tabular}{lrrrr}
402	\toprule
403	\textbf{Difficulty} & $n$ & Mean $d$ & $\Delta l_z^*$ clean & $\Delta l_z^*$ contam. \\
404	\midrule
405	$<0.5$ (easy) & 2{,}814 & .97 & $-$0.08 & 0.12 \\
406	0.5--1.5 & 5{,}621 & .93 & $-$0.21 & 0.43 \\
407	1.5--2.5 & 3{,}891 & .89 & $-$0.38 & 0.78 \\
408	$>2.5$ (hard) & 1{,}716 & .82 & $-$0.67 & 1.45 \\
409	\bottomrule
410	\end{tabular}
411	\end{table}
412	
413	The 4PL model improves over 3PL primarily through better calibration on high-difficulty items (Table~\ref{tab:4pl-3pl}). The $d$ parameter absorbs natural variation in ceiling performance, reducing false alarms from 7.8\% to 4.2\%. The improvement concentrates on items with difficulty $>$2.5, where $d<0.85$ (Table~\ref{tab:d-param}). These are precisely the items where contamination signals are strongest, making the 4PL advantage non-trivial for detection despite modest overall improvement.
414	
415	\subsection{Multiscale $l_{zm}$ Statistic}
416	\label{sec:lzm}
417	
418	\begin{table}[t]
419	\centering
420	\caption{$l_{zm}$ results on PSN-IRT 12 models.}
421	\label{tab:lzm}
422	\small
423	\begin{tabular}{lrrl}
424	\toprule
425	\textbf{Model} & $l_{zm}$ & \textbf{Flag} & \textbf{\#Bench.\ Flagged} \\
426	\midrule
427	Gemini-1.5 & 18.42 & YES & 3 \\
428	GPT-4 & $-$0.87 & no & 0 \\
429	Llama-2-70B & $-$3.21 & YES & 1 \\
430	Claude-3-Opus & 0.42 & no & 0 \\
431	Mistral-7B & $-$2.45 & no & 0 \\
432	\bottomrule
433	\end{tabular}
434	\end{table}
435	
436	\begin{table}[t]
437	\centering
438	\caption{$l_{zm}$ vs.\ single-benchmark detection (15\% contamination).}
439	\label{tab:lzm-vs-single}
440	\small
441	\begin{tabular}{lrrr}
442	\toprule
443	\textbf{Method} & \textbf{AUROC} & \textbf{Power} & \textbf{FA Rate} \\
444	\midrule
445	$l_z^*$ (MMLU only) & .96 & .979 & .042 \\
446	$l_z^*$ (best single) & .96 & .979 & .042 \\
447	$l_{zm}$ (all benchmarks) & .98 & .990 & .037 \\
448	\bottomrule
449	\end{tabular}
450	\end{table}
451	
452	Cross-benchmark aggregation via $l_{zm}$ yields a modest but consistent improvement: AUROC increases from 0.96 to 0.98 (Table~\ref{tab:lzm-vs-single}). The gain comes from information pooling across $\sim$27K total items and from the fact that genuine contamination signals are correlated across benchmarks while false positives are not. The null distribution is well-calibrated (KS $p=0.312$). Gemini-1.5 produces the most extreme $l_{zm}=18.42$, aggregating both positive (MMLU) and negative (GSM8K, HumanEval) regime signals.
453	
454	% ============================================================
455	\section{Large-Scale Empirical Study}
456	\label{sec:empirical}
457	
458	\subsection{Two-Sided Detection on PSN-IRT Models}
459	\label{sec:two-sided}
460	
461	We apply the two-sided framework to 12 models from the PSN-IRT dataset across 5 benchmarks (60 model-benchmark pairs).
462	
463	\begin{table}[t]
464	\centering
465	\caption{Two-sided detection results (selected model-benchmark pairs).}
466	\label{tab:two-sided-results}
467	\small
468	\begin{tabular}{llrrl}
469	\toprule
470	\textbf{Model} & \textbf{Bench.} & $l_z^*$ & \textbf{Side} & \textbf{Flag} \\
471	\midrule
472	Gemini-1.5 & MMLU & +34.75 & positive & YES \\
473	Gemini-1.5 & GSM8K & $-$15.71 & negative & YES \\
474	Gemini-1.5 & HumanEval & $-$12.37 & negative & YES \\
475	GPT-4 & MMLU & $-$1.23 & --- & no \\
476	Llama-2-70B & ARC-C & $-$3.87 & negative & YES \\
477	\bottomrule
478	\end{tabular}
479	\end{table}
480	
481	\begin{table}[t]
482	\centering
483	\caption{One-sided vs.\ two-sided detection comparison (FDR = 0.05).}
484	\label{tab:one-vs-two}
485	\small
486	\begin{tabular}{lrrrr}
487	\toprule
488	\textbf{Method} & \textbf{Total} & \textbf{Partial} & \textbf{Full} & \textbf{FDR} \\
489	\midrule
490	One-sided ($l_z^* < c$) & 2 & 2 & 0 & .05 \\
491	Two-sided ($|l_z^*| > c$) & 4 & 2 & 2 & .05 \\
492	\bottomrule
493	\end{tabular}
494	\end{table}
495	
496	Gemini-1.5 on MMLU ($l_z^*=+34.75$, 95\% CI $[32.1, 37.4]$) exemplifies the positive regime: 100\% accuracy with estimated $\hat{\theta}=0.78$ indicates systematic memorization, not extraordinary ability (Table~\ref{tab:two-sided-results}). One-sided testing completely misses this signal and the two additional flagged models at the positive extreme (Table~\ref{tab:one-vs-two}).
497	
498	\subsection{Leaderboard Audit}
499	\label{sec:leaderboard}
500	
501	We run inference on 2{,}847 models from Open LLM Leaderboard v1, computing $l_z^*$ for each model-benchmark pair (18.5 GPU-hours total).
502	
503	\begin{table}[t]
504	\centering
505	\caption{Leaderboard audit summary.}
506	\label{tab:leaderboard}
507	\small
508	\begin{tabular}{lrrrrr}
509	\toprule
510	\textbf{Bench.} & $n$ & \textbf{Neg.} & \textbf{Pos.} & \textbf{Rate} & \textbf{Med.\ $l_z^*$} \\
511	\midrule
512	MMLU & 2{,}847 & 312 & 115 & .15 & $-$6.73 \\
513	HSwag & 2{,}847 & 198 & 58 & .09 & $-$4.21 \\
514	ARC-C & 2{,}847 & 142 & 57 & .07 & $-$3.12 \\
515	GSM8K & 2{,}182 & 178 & 63 & .11 & $-$5.42 \\
516	Overall & 2{,}847 & 255 & 87 & .12 & --- \\
517	\bottomrule
518	\end{tabular}
519	\end{table}
520	
521	\begin{table}[t]
522	\centering
523	\caption{Contamination rate by time period.}
524	\label{tab:temporal}
525	\small
526	\begin{tabular}{lrrr}
527	\toprule
528	\textbf{Period} & \textbf{Models} & \textbf{Flagged} & \textbf{Rate} \\
529	\midrule
530	2023 Q1--Q2 & 487 & 29 & .06 \\
531	2023 Q3--Q4 & 891 & 98 & .11 \\
532	2024 Q1--Q2 & 1{,}103 & 198 & .18 \\
533	2024 Q3+ & 366 & 51 & .14 \\
534	\bottomrule
535	\end{tabular}
536	\end{table}
537	
538	\begin{table}[t]
539	\centering
540	\caption{Most anomalous models (top 3 by $|l_z^*|$).}
541	\label{tab:top-anomalous}
542	\small
543	\begin{tabular}{llrrrl}
544	\toprule
545	\textbf{Model} & \textbf{Bench.} & \textbf{Acc.} & $l_z^*$ & \textbf{Side} & \textbf{Params} \\
546	\midrule
547	anon-7b-v3 & MMLU & .847 & $-$22.4 & neg & 7B \\
548	llm-ft-2b & MMLU & .912 & +18.7 & pos & 2B \\
549	bench-tuned-3b & GSM8K & .891 & $-$17.3 & neg & 3B \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	The audit reveals 342 flagged models (12\% overall), with MMLU most affected at 15\% (Table~\ref{tab:leaderboard}). Contamination rates increase from 6\% in early 2023 to 18\% in early 2024 (Table~\ref{tab:temporal}), consistent with the proliferation of benchmark-tuned models on the leaderboard. Table~\ref{tab:top-anomalous} shows the most extreme cases, including a 2B-parameter model achieving 91.2\% MMLU accuracy ($l_z^*=+18.7$) and a 7B model with $l_z^*=-22.4$. Cross-benchmark consistency is 34\%: about one-third of flagged models show anomalies on multiple benchmarks.
555	
556	\subsection{Additional Benchmarks: BBH and MATH}
557	\label{sec:extra-bench}
558	
559	\begin{table}[t]
560	\centering
561	\caption{Power analysis across all 7 benchmarks (15\% contamination).}
562	\label{tab:power-all}
563	\small
564	\begin{tabular}{lrrrr}
565	\toprule
566	\textbf{Benchmark} & $n$ & \textbf{Sim.} & \textbf{Pred.} & \textbf{5\%} \\
567	\midrule
568	HumanEval & 164 & .243 & .231 & .07 \\
569	ARC-C & 1{,}172 & .129 & .142 & .04 \\
570	GSM8K & 1{,}319 & .578 & .561 & .22 \\
571	MATH & 5{,}000 & .840 & .830 & .44 \\
572	BBH & 6{,}511 & .890 & .880 & .52 \\
573	HellaSwag & 10{,}042 & .733 & .748 & .34 \\
574	MMLU & 14{,}042 & .979 & .981 & .78 \\
575	\bottomrule
576	\end{tabular}
577	\end{table}
578	
579	Adding BBH (6{,}511 items) and MATH (5{,}000 items) fills the power gap between GSM8K and HellaSwag (Table~\ref{tab:power-all}). All seven benchmarks fall within 1--2\% of theoretical predictions, further validating the power formula. ARC-C is a notable outlier: its power (0.129) is much lower than GSM8K (0.578) despite similar $n_{\text{items}}$ (1{,}172 vs.\ 1{,}319), indicating that item discrimination quality also affects power---a factor captured by the $\delta$ term in Equation~\ref{eq:power}.
580	
581	\subsection{MMLU Domain-Level Analysis}
582	\label{sec:domain}
583	
584	\begin{table}[t]
585	\centering
586	\caption{MMLU domain-level $l_z^*$: Gemini-1.5 vs.\ GPT-4 (selected domains).}
587	\label{tab:domain}
588	\small
589	\begin{tabular}{lrrrrr}
590	\toprule
591	\textbf{Domain} & $n$ & \multicolumn{2}{c}{\textbf{Gemini-1.5}} & \multicolumn{2}{c}{\textbf{GPT-4}} \\
592	\cmidrule(lr){3-4} \cmidrule(lr){5-6}
593	 & & Acc. & $l_z^*$ & Acc. & $l_z^*$ \\
594	\midrule
595	abstract\_algebra & 100 & 1.00 & +0.83 & .73 & $-$0.42 \\
596	prof\_medicine & 272 & 1.00 & +4.21 & .85 & +0.67 \\
597	hs\_mathematics & 270 & 1.00 & +2.14 & .41 & $-$1.23 \\
598	college\_chem & 100 & 1.00 & +0.91 & .47 & +0.31 \\
599	miscellaneous & 783 & 1.00 & +7.89 & .87 & +0.42 \\
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2a778347-6761-4053-8bc2-3ede91615fb3",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "7670b3d6-9616-46fb-9efc-367c48891477",
  "sourceToolAssistantUUID": "2a778347-6761-4053-8bc2-3ede91615fb3",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-20T09:11:20.922Z_

<details open><summary>🔧 Tool call — Read · `toolu_0162j9LTeqvtp5rYa1z1QkE7`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam/artifacts/dream_reports/dream_20260520T082549/best/paper.tex",
  "offset": 600,
  "limit": 200
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7670b3d6-9616-46fb-9efc-367c48891477",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZXaGM25MWR71SYth25",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f5687ca4-e408-4312-b680-03b9de094dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01U4NSYe5tuTH2TngqSQuBFk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7930,
      "cache_read_input_tokens": 33471,
      "output_tokens": 139,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 7930
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 139,
          "cache_read_input_tokens": 33471,
          "cache_creation_input_tokens": 7930,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 7930,
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

_source line 26 · 2026-05-20T09:11:20.935Z_

<details><summary>↩ Tool result · `toolu_0162j9LTeqvtp5rYa1z1QkE7`</summary>

```text
600	clinical\_know & 265 & 1.00 & +3.87 & .79 & $-$0.18 \\
601	\bottomrule
602	\end{tabular}
603	\end{table}
604	
605	\begin{table}[t]
606	\centering
607	\caption{Domain-level power as a function of $n_{\text{items}}$.}
608	\label{tab:domain-power}
609	\small
610	\begin{tabular}{lrrr}
611	\toprule
612	$n_{\text{items}}$ \textbf{bin} & \textbf{Domains} & \textbf{Power} & \textbf{Pred.} \\
613	\midrule
614	100--150 & 22 & .18 & .17 \\
615	150--300 & 21 & .31 & .33 \\
616	300--600 & 9 & .52 & .50 \\
617	600--1{,}000 & 3 & .64 & .67 \\
618	$>$1{,}000 & 2 & .72 & .74 \\
619	\bottomrule
620	\end{tabular}
621	\end{table}
622	
623	Gemini-1.5 achieves 100\% accuracy across all 57 MMLU domains, with uniformly positive $l_z^*$ values ranging from +0.8 to +12.3 (Table~\ref{tab:domain}). This uniformity rules out the innocent explanation that Gemini-1.5 is simply exceptionally strong in certain domains---no model genuinely excels equally across abstract algebra, clinical knowledge, and high school mathematics without occasionally erring. GPT-4, by contrast, shows normally distributed $l_z^*$ (SD=0.82) with zero domains flagged. The 57 MMLU domains provide 57 additional validation points for the power theory (Table~\ref{tab:domain-power}), with predicted power matching observed power within 2--3 percentage points across all domain size bins.
624	
625	% ============================================================
626	\section{Related Work}
627	\label{sec:related}
628	
629	\paragraph{Benchmark contamination detection.}
630	\citet{shi2024detecting} introduce Min-K\%++ for membership inference using token-level likelihood. \citet{oren2024proving} propose Time Travel testing via prompting. \citet{dekoninck2024constat} use performance consistency across rephrased items. \citet{dong2024generalization} study generalization-based detection. \citet{wang2025reassessing} show all MIA-based methods fail post-RL. Our work establishes a strictly lower information requirement.
631	
632	\paragraph{IRT for LLMs.}
633	\citet{polo2024tinybenchmarks} use IRT for efficient benchmarking. \citet{gu2024psnirt} calibrate 4PL IRT models on LLM response data (PSN-IRT). We build on PSN-IRT's item parameters but pivot from benchmarking to contamination detection via person-fit analysis.
634	
635	\paragraph{Person-fit in psychometrics.}
636	\citet{drasgow1985appropriateness} introduce $l_z$; \citet{snijders2001person} derive the corrected $l_z^*$. \citet{meijer2001methodology} survey applications including cheating detection. \citet{hong2021multiscale} propose multiscale aggregation. We are the first to apply person-fit statistics to LLM evaluation.
637	
638	% ============================================================
639	\section{Conclusion}
640	\label{sec:conclusion}
641	
642	We introduced IRT-FIT, a framework that detects benchmark contamination using only binary response patterns---the minimal-information operating point on the detection frontier. Three findings stand out: (1) person-fit statistics achieve AUROC 0.96 at 15\% contamination, surpassing methods requiring token probabilities or re-testing; (2) detection power follows a predictable analytic function of benchmark size ($R^2=0.97$), with the inverted-U signal structure theoretically derivable from item difficulty distributions; (3) a leaderboard-scale audit of 2{,}847 models reveals 12\% overall contamination rates, increasing from 6\% to 18\% over 2023--2024.
643	
644	The person-fit signal survives post-RL training (AUROC 0.92 after GRPO) while MIA degrades to near-chance (0.54), because binary response patterns are robust to the probability recalibration that RL induces. IRT-FIT is the only method that simultaneously addresses partial contamination (aberrant patterns), full contamination (over-consistent patterns), and post-RL contamination at the minimal-information level.
645	
646	\paragraph{Limitations.}
647	Detection power depends on benchmark size: benchmarks with fewer than $\sim$3{,}200 items have limited power at 15\% contamination ($<$80\%). The method targets intentional SFT-style contamination and leaderboard gaming; gradual pretraining exposure that yields smooth capability improvement is not in scope. The 4PL IRT model assumes unidimensionality, which may not hold for heterogeneous benchmarks.
648	
649	% ============================================================
650	\bibliographystyle{plainnat}
651	\begin{thebibliography}{20}
652	
653	\bibitem[Dekoninck et~al.(2024)]{dekoninck2024constat}
654	Jasper Dekoninck, Mark Niklas M{\"u}ller, and Martin Vechev.
655	\newblock ConStat: Performance-based contamination detection in large language models.
656	\newblock In \emph{NeurIPS}, 2024.
657	
658	\bibitem[Dong et~al.(2024)]{dong2024generalization}
659	Yihong Dong, Xue Jiang, Huanyu Liu, Zhi Jin, and Ge Li.
660	\newblock Generalization or memorization: Data contamination and trustworthy evaluation for large language models.
661	\newblock In \emph{ACL}, 2024.
662	
663	\bibitem[Drasgow et~al.(1985)]{drasgow1985appropriateness}
664	Fritz Drasgow, Michael~V. Levine, and Mary~E. Williams.
665	\newblock Appropriateness measurement with polychotomous item response models and standardized indices.
666	\newblock \emph{British Journal of Mathematical and Statistical Psychology}, 38(1):67--86, 1985.
667	
668	\bibitem[Gu et~al.(2024)]{gu2024psnirt}
669	Guanyu Gu, Yixiao Li, and Yun-Fei Liu.
670	\newblock PSN-IRT: A psychometric benchmark calibration framework for large language models.
671	\newblock In \emph{AAAI}, 2024.
672	
673	\bibitem[Hong et~al.(2021)]{hong2021multiscale}
674	Sophia Hong, David~J. Lin, and Ying Cheng.
675	\newblock Multiscale person-fit statistics.
676	\newblock \emph{Applied Psychological Measurement}, 45(6):417--434, 2021.
677	
678	\bibitem[Meijer and Sijtsma(2001)]{meijer2001methodology}
679	Rob~R. Meijer and Klaas Sijtsma.
680	\newblock Methodology review: Evaluating person fit.
681	\newblock \emph{Applied Psychological Measurement}, 25(2):107--135, 2001.
682	
683	\bibitem[Oren et~al.(2024)]{oren2024proving}
684	Yonatan Oren, Nicole Meister, Niladri~S. Chatterji, Faisal Ladhak, and Tatsunori Hashimoto.
685	\newblock Proving test set contamination in black-box language models.
686	\newblock In \emph{ICLR (Spotlight)}, 2024.
687	
688	\bibitem[Polo et~al.(2024)]{polo2024tinybenchmarks}
689	Felipe~Maia Polo, Lucas Weber, Leshem Choshen, Yuekai Sun, Gongjun Xu, and Mikhail Yurochkin.
690	\newblock tinyBenchmarks: evaluating LLMs with fewer examples.
691	\newblock In \emph{ICML}, 2024.
692	
693	\bibitem[Shi et~al.(2024)]{shi2024detecting}
694	Weijia Shi, Anirudh Ajith, Mengzhou Xia, Yangsibo Huang, Daogao Liu, Terra Blevins, Danqi Chen, and Luke Zettlemoyer.
695	\newblock Detecting pretraining data from large language models.
696	\newblock In \emph{ICLR}, 2024.
697	
698	\bibitem[Snijders(2001)]{snijders2001person}
699	Tom~A.B. Snijders.
700	\newblock Asymptotic null distribution of person fit statistics with estimated item parameters.
701	\newblock \emph{Psychometrika}, 66(3):331--342, 2001.
702	
703	\bibitem[Wang et~al.(2025)]{wang2025reassessing}
704	Cheng Wang, Yiwei Wang, Bryan Hooi, and Yujun Cai.
705	\newblock Reassessing contamination detection: MIA fails under post-RL training.
706	\newblock \emph{arXiv preprint arXiv:2501.xxxxx}, 2025.
707	
708	\end{thebibliography}
709	
710	\end{document}
711	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f5687ca4-e408-4312-b680-03b9de094dc7",
  "isSidechain": true,
  "promptId": "2fdb3cc9-c2a8-48d5-8d9f-6a00d3c4edd2",
  "agentId": "a738e9a8334856553",
  "type": "user",
  "uuid": "02b877f1-9a41-4344-b071-ebe9a14c5625",
  "sourceToolAssistantUUID": "f5687ca4-e408-4312-b680-03b9de094dc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 27 · 2026-05-20T09:12:35.135Z_

Now I have a thorough understanding of the full paper. Let me compose the review.

---

## Review: IRT-FIT — Detecting Benchmark Contamination in Large Language Models via Item Response Theory Person-Fit Statistics

**Reviewer 2 (R2): Novelty, Positioning, and Related Work**

---

### 1. Novelty Assessment

**Core idea: person-fit statistics for LLM contamination.** The conceptual mapping -- contaminated LLM as examinee with item preknowledge -- is clean and well-motivated. To my knowledge, no prior work has applied person-fit statistics (lz, lz*, outfit/infit) to detect benchmark contamination in LLMs. The psychometrics community has used these tools for cheating detection in human testing for decades, but the cross-domain transfer is non-trivial: it requires validating that 4PL IRT parameters estimated by neural networks (PSN-IRT) are compatible with classical person-fit theory, and that LLM response patterns under contamination produce analogous statistical signatures to human examinees with preknowledge. The null-distribution verification (lz* approximately N(0,1) under PSN-IRT parameters) is an important sanity check that cannot be taken for granted.

**Two-sided extension.** This is a genuine contribution. The observation that partial contamination yields lz* << 0 (aberrant: hard items correct, easy items wrong) while full contamination yields lz* >> 0 (over-consistent: everything correct, including items beyond estimated ability) is not obvious from the psychometrics literature, where two-sided testing exists but is not standard practice. The empirical demonstration that one-sided testing misses the Gemini-1.5 case entirely is compelling. That said, proposing |lz*| > c_{alpha/2} is technically straightforward once the two regimes are identified. The intellectual contribution is the observation of the two regimes, not the statistical test itself.

**Power theory.** The power formula (Eq. 4) is a relatively direct application of the standard power formula for standardized test statistics, substituting the per-item log-likelihood shift delta. The R^2=0.97 fit is impressive, but the derivation is more an exercise in careful parameter estimation than a theoretical breakthrough. The inverted-U inflection point derivation is more interesting -- predicting c* from item difficulty distributions alone, within 0.02 of observed, provides genuine practical value. However, I would not call this "theory" in the strong sense; it is a well-validated empirical approximation.

**Overall novelty: moderate-to-high.** The novelty is concentrated in: (a) the cross-domain connection itself, (b) the two-regime signal structure, and (c) the leaderboard-scale audit capability. The individual technical pieces (lz*, two-sided testing, power analysis) are mostly existing tools composed in a new way. This is respectable for a top venue, but the paper should be more transparent about what is novel methodology versus novel application.

---

### 2. Related Work Coverage

**The reference list is alarmingly thin.** 11 references for an 8-page paper at a top venue is far below the expected density (typically 30-50+). Several important gaps:

**Missing contamination detection methods:**
- CoDeC (ICLR 2026) -- mentioned in the paper_framing notes but absent from the paper. This is a significant omission since it operates at a different information level.
- Self-Critique (ICLR 2026) for post-RL contamination detection -- directly relevant to the post-RL experiments in Section 5.2.
- Golchin & Surdeanu (2024) "Time Travel in LLMs" and related rephrasing-based methods beyond Oren et al.
- Sainz et al. (2023) "NLP Evaluation in trouble" and other early contamination survey/position papers.
- Yang et al. (2023) "Rethinking Benchmark and Contamination" -- one of the earliest systematic treatments.

**Missing IRT-for-LLM works:**
- ATLAS (2025) for adaptive testing -- acknowledged in the literature_map.yaml but not cited in the paper.
- Lalor et al. (2019) on IRT for NLP evaluation.
- Vania et al. (2021) on comparing test sets with IRT.
- Martinez-Plumed et al. (2019) on IRT for AI evaluation more broadly.

**Missing person-fit works:**
- Karabatsos (2003), comparing 36 person-fit statistics -- in the literature map but uncited. This is important for justifying the choice of lz* over alternatives.
- Sinharay (2017) on preknowledge detection power -- also in the literature map but missing from the paper. This is the most directly relevant psychometric precedent.
- St-Onge et al. (2011) on person-fit for cheating detection in computerized adaptive testing.

**Missing broader context:**
- No discussion of test security literature from educational measurement (e.g., Wollack & Schoenig, 2018).
- No mention of computerized adaptive testing (CAT) applications where person-fit is routinely used for real-time cheating detection -- this would strengthen the motivation.

The related work section reads like a minimum viable bibliography. For EMNLP, reviewers will expect thorough coverage of both the NLP evaluation and psychometrics sides.

---

### 3. Positioning and Framing

**"Minimal-information operating point" framing.** This is the paper's strongest rhetorical device. The detection frontier concept -- ranking methods by information access (binary < retest < token probs < logits < weights) -- provides a clear organizing principle. The claim that IRT-FIT defines the bottom of this frontier is precise and verifiable. I find this compelling.

**However, the framing overstates the comparison to baselines.** The paper claims IRT-FIT "outperforms" ConStat and Min-K%++ while requiring less information. This is true on the controlled experiments, but the comparison is not entirely fair:
- ConStat is designed for a different use case (detecting contamination via performance drop on rephrased items) and does not use item-level IRT parameters. If ConStat had access to the same 4PL item bank, the comparison might differ.
- Min-K%++ operates on raw text, not multiple-choice binary responses. The information access hierarchy is orthogonal to detection power -- "less information" does not automatically mean "harder problem." Binary responses from a 14K-item benchmark may contain more contamination-relevant signal than token-level probabilities on a few sequences.
- The paper does not discuss that IRT-FIT requires a pre-calibrated item bank (the PSN-IRT parameters), which is itself a substantial prerequisite. This should be explicitly acknowledged as a dependency.

**The "only method that simultaneously addresses partial, full, and post-RL contamination" claim** in the abstract is strong. It would be more precise to say "at the minimal-information level" -- Self-Critique (ICLR 2026) addresses post-RL contamination, just at a different information level.

---

### 4. Writing Quality

**Strengths:** The paper is well-structured, with a logical flow from background through controlled experiments to large-scale application. The tables are information-dense and well-formatted. The notation is consistent throughout.

**Weaknesses:**
- The paper is table-heavy (17+ tables in 8 pages). Some tables could be consolidated or moved to an appendix. Tables 7, 8, 9 (lzm results) could be merged. The density is borderline for readability.
- The Background section is too compressed for readers unfamiliar with IRT. The 4PL model equation (Eq. 1) is presented without intuition for what each parameter means in the LLM context.
- The lzm formula (Eq. 3) uses absolute values of lz*, which discards the sign information. The paper does not justify why this is appropriate rather than using signed values or a chi-square-type aggregation.
- Some notation inconsistencies: sometimes "contam." sometimes "contamination" in table headers; "Bench." vs "Benchmark" varies.

---

### 5. Impact and Significance

**The leaderboard audit is the most impactful contribution.** The ability to retroactively audit 2,847 models using only publicly available binary response data is a unique capability. No competing method can do this at scale on historical data. The finding that contamination rates increased from 6% to 18% over 2023-2024 is newsworthy and actionable for the community.

**The power theory provides lasting practical value.** The minimum n_items table (Table 8) gives practitioners concrete guidance. The prediction that ARC-C's low detection rate is a benchmark-size issue, not a method failure, is the kind of insight that changes how people design benchmarks.

**Long-term influence: moderate.** The method fills a genuine gap, but contamination detection is an arms race. SFT contamination (the paper's scope) may become less relevant as models move toward RL-based training. The post-RL results are encouraging but limited to one RL algorithm (GRPO). The paper honestly acknowledges that pretraining exposure is out of scope, but this is the dominant contamination pathway in practice.

---

### 6. Specific Concerns

1. **11 references is inadequate.** This is the single largest weakness for venue acceptance. A reviewer unfamiliar with person-fit statistics cannot assess the novelty claim without seeing the full psychometric literature discussed. The missing references identified above are not obscure -- they are standard citations in their respective fields.

2. **Gemini-1.5 100% MMLU accuracy is a known anomaly.** The paper presents this as a discovery, but Google's MMLU results have been publicly questioned before. The paper should cite prior discussions and clarify what IRT-FIT adds beyond confirming a known anomaly.

3. **The controlled experiment uses QLoRA SFT, which is a specific contamination mechanism.** The paper should discuss how the signal might differ under: (a) full-parameter SFT, (b) continued pretraining on benchmark items mixed with other data, (c) data augmentation / paraphrasing of benchmark items before training.

4. **No confidence intervals on AUROC.** The paper reports point estimates only. Bootstrap confidence intervals would strengthen the baseline comparison -- the 0.96 vs 0.88 difference may not be statistically significant given the sample size.

5. **The leaderboard audit lacks external validation.** Are the 12% flagged models independently known to be contaminated? Without even a small external validation set, the audit results are suggestive but not confirmatory.

6. **PSN-IRT dependency.** The method is entirely dependent on pre-calibrated IRT item parameters from PSN-IRT. If these parameters have systematic biases (e.g., from the specific 12 models used for calibration), the downstream person-fit statistics inherit those biases. This is under-discussed.

---

### 7. Score

**Overall Assessment: 3.5 (Borderline Conference)**

The paper presents a well-motivated cross-domain connection with solid experimental support and a genuinely useful large-scale application. The "minimal-information operating point" framing is compelling. However, the severely thin reference list, missing important baselines (CoDeC, Self-Critique), lack of confidence intervals, and insufficient discussion of the PSN-IRT dependency prevent a confident accept. The novelty is real but incremental -- the individual components are existing tools, and the main contribution is their composition and validation in a new domain. With 25-30 additional references, a Self-Critique baseline comparison, confidence intervals on AUROCs, and a frank discussion of the item bank dependency, this could reach 4.0.

---

### 8. Confidence

**4 out of 5.** I have strong familiarity with contamination detection methods and moderate familiarity with IRT/person-fit statistics. I am less confident in assessing the correctness of the power theory derivation relative to the psychometrics literature.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "02b877f1-9a41-4344-b071-ebe9a14c5625",
  "isSidechain": true,
  "agentId": "a738e9a8334856553",
  "requestId": "req_011CbDZXzAmXmXDB4Jbwi7ku",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d27d2411-002b-4544-b8de-dce5eac5b1bc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam",
  "sessionId": "5313366d-c419-4c21-b601-a692e3b34542",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VDuT3VdDSh2sPspnkpN9wS",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2703,
      "cache_read_input_tokens": 41401,
      "output_tokens": 2829,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2703
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2829,
          "cache_read_input_tokens": 41401,
          "cache_creation_input_tokens": 2703,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2703,
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
