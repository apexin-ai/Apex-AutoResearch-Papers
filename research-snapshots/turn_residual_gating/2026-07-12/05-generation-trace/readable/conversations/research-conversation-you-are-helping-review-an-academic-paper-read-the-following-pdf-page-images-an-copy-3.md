# Research conversation: You are helping review an academic paper. Read the following PDF page images and provide a detailed summary of the conte

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 4
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-ab89d0e2030cc79d8.jsonl`
- **Structured JSON:** [`b53b4ae9362dc82ecae4.json`](../../sessions/b5/b53b4ae9362dc82ecae4.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

12 recorded events

### User

_source line 1 · 2026-05-15T13:44:15.833Z_

You are helping review an academic paper. Read the following PDF page images and provide a detailed summary of the content on each page. Report verbatim any key definitions, equations, claims, and numbers.

Read these image files one by one:
1. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p1.png
2. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p2.png
3. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p3.png
4. /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p4.png

For each page, report:
- Section headings
- All equations with their equation numbers
- Key claims and findings (quote the exact text)
- All table/figure content
- Sample sizes (n=?) mentioned
- Any statistical values (p-values, confidence intervals, effect sizes)

Be extremely thorough. Do not skip any content.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "6df1793b-25b1-46eb-8c31-ea8c9d86bd28",
  "agentId": "ab89d0e2030cc79d8",
  "type": "user",
  "uuid": "78397405-5953-4777-b41e-2637c32eb112",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-15T13:44:15.841Z_

```json
{
  "parentUuid": "78397405-5953-4777-b41e-2637c32eb112",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "addedLines": [
      "EnterWorktree",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch",
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "9fa2f60d-cd28-4f4a-934d-a8b924584da2",
  "timestamp": "2026-05-15T13:44:15.841Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-15T13:44:18.467Z_



I'll read all four page images to provide a detailed analysis.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fa2f60d-cd28-4f4a-934d-a8b924584da2",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "requestId": "req_011Cb4TJTXC1BE3iApBbG6ai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "d44f8c5f-38f2-41ae-b2ea-48eebd51e184",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138LhyzC8LijH51kkuS9Xtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15956,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15956,
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

_source line 4 · 2026-05-15T13:44:19.441Z_

<details open><summary>🔧 Tool call — Read · `toolu_01W4irEoRWycxJkjFsSRHKVG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d44f8c5f-38f2-41ae-b2ea-48eebd51e184",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "requestId": "req_011Cb4TJTXC1BE3iApBbG6ai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f8c20adf-33ed-4d8f-ab12-acaee3191d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138LhyzC8LijH51kkuS9Xtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15956,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15956,
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

_source line 5 · 2026-05-15T13:44:19.911Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QQdEGVpQqv2D6J4xDuVWgj`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f8c20adf-33ed-4d8f-ab12-acaee3191d62",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "requestId": "req_011Cb4TJTXC1BE3iApBbG6ai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "7901a7bf-a2f3-4cb2-92b4-fab23a6a726d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138LhyzC8LijH51kkuS9Xtd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15956,
      "cache_read_input_tokens": 0,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 15956,
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

_source line 6 · 2026-05-15T13:44:20.775Z_

<details open><summary>🔧 Tool call — Read · `toolu_01QtpLbYn6cJ6dURwbo3raf4`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7901a7bf-a2f3-4cb2-92b4-fab23a6a726d",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "requestId": "req_011Cb4TJTXC1BE3iApBbG6ai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "1f5acdbf-3026-4be9-9e79-29aba4b826b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138LhyzC8LijH51kkuS9Xtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15956,
      "cache_read_input_tokens": 0,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 360,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15956,
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

### Tool call

_source line 7 · 2026-05-15T13:44:20.936Z_

<details open><summary>🔧 Tool call — Read · `toolu_01FYRHr4F7RdwT7gikoXyWUY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f5acdbf-3026-4be9-9e79-29aba4b826b5",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "requestId": "req_011Cb4TJTXC1BE3iApBbG6ai",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "60e12ea2-2f53-4b04-8ca0-bc974d2b16f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0138LhyzC8LijH51kkuS9Xtd",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 15956,
      "cache_read_input_tokens": 0,
      "output_tokens": 360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 15956
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 360,
          "cache_read_input_tokens": 0,
          "cache_creation_input_tokens": 15956,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 15956,
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

_source line 8 · 2026-05-15T13:44:22.461Z_

<details><summary>↩ Tool result · `toolu_01W4irEoRWycxJkjFsSRHKVG`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f8c20adf-33ed-4d8f-ab12-acaee3191d62",
  "isSidechain": true,
  "promptId": "6df1793b-25b1-46eb-8c31-ea8c9d86bd28",
  "agentId": "ab89d0e2030cc79d8",
  "type": "user",
  "uuid": "fdf29214-7a20-4d89-897a-3a5b61b65274",
  "sourceToolAssistantUUID": "f8c20adf-33ed-4d8f-ab12-acaee3191d62",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-15T13:44:25.334Z_

<details><summary>↩ Tool result · `toolu_01QQdEGVpQqv2D6J4xDuVWgj`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7901a7bf-a2f3-4cb2-92b4-fab23a6a726d",
  "isSidechain": true,
  "promptId": "6df1793b-25b1-46eb-8c31-ea8c9d86bd28",
  "agentId": "ab89d0e2030cc79d8",
  "type": "user",
  "uuid": "67bd7445-25b4-458e-94c0-e311ef3c837a",
  "sourceToolAssistantUUID": "7901a7bf-a2f3-4cb2-92b4-fab23a6a726d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-15T13:44:25.502Z_

<details><summary>↩ Tool result · `toolu_01QtpLbYn6cJ6dURwbo3raf4`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1f5acdbf-3026-4be9-9e79-29aba4b826b5",
  "isSidechain": true,
  "promptId": "6df1793b-25b1-46eb-8c31-ea8c9d86bd28",
  "agentId": "ab89d0e2030cc79d8",
  "type": "user",
  "uuid": "2bab0fcf-462d-49dd-963d-1eb4244a2d84",
  "sourceToolAssistantUUID": "1f5acdbf-3026-4be9-9e79-29aba4b826b5",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 11 · 2026-05-15T13:44:26.422Z_

<details><summary>↩ Tool result · `toolu_01FYRHr4F7RdwT7gikoXyWUY`</summary>

````text
```json
{
  "type": "image",
  "source": {
    "type": "base64",
    "data": "[ATTACHMENT_DATA_REDACTED]",
    "media_type": "image/jpeg"
  }
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "60e12ea2-2f53-4b04-8ca0-bc974d2b16f0",
  "isSidechain": true,
  "promptId": "6df1793b-25b1-46eb-8c31-ea8c9d86bd28",
  "agentId": "ab89d0e2030cc79d8",
  "type": "user",
  "uuid": "d0501f29-0cc5-4ac0-81d1-3ae5b6bfaf3d",
  "sourceToolAssistantUUID": "60e12ea2-2f53-4b04-8ca0-bc974d2b16f0",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-15T13:46:22.396Z_



Here is a detailed page-by-page summary of the paper.

---

## Page 1

### Title
**Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models**

**Anonymous ACL submission**

### Section: Abstract
Key claims and definitions (verbatim excerpts):

- "Compound sparsity—simultaneously pruning attention heads and evicting KV cache entries—is essential for efficient LLM inference but produces super-additive quality degradation whose structure is poorly understood."
- "We show that compound severity is not phase-invariant: it is an emergent phase–strategy interaction with amplification ratios (G) from 7.5× (cv=0.15, 99% CI [1.1, 14.0]) to 78× (cv=0.30, 99% CI [63.3, 96.3]) across reasoning phases in mathematical reasoning models."
- "On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems, n_obs = {0.11, 0.20, 0.25, 0.30}), importance-based eviction produces a monotonically increasing severity gradient from the high-sparsity phase to low-sparsity reasoning phase (median Δ = 0.39 → 8.46, all Bonferroni-corrected p < 10⁻⁴)."
- "Random eviction develops a detectable phase gradient only above s ≥ 0.20 (non-significant at s ≤ 0.20, where significance: 2.3×, weaker), confirming importance-based eviction as the dominant driver."
- "A crossover converges at s ≈ 0.25: importance-based eviction outperforms random in high-sparsity phases yet underperforms in low-sparsity phases—a qualitative reversal in strategy ranking."
- "The pattern replicates on Qwen2.5-7B-Instruct (n_obs=473, Δ = 0.07 → 3.16, all p < 10⁻³), with preliminary cross-architecture evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2 family architectures."
- "We present downstream collateral—head pruning flattening cumulative importance scores—as a correlational diagnostic: both strategies exhibit near-identical Gini drops, yet severity diverges by 7–17×, implicating the structural specificity of importance-based pruning as the key differentiator."

### Section: 1 Introduction

Key claims:

- "Long-context language models place acute pressure on the key-value (KV) cache, which grows linearly with sequence length (Kwon et al., 2023; Pope et al., 2023)."
- "Prior work treats compound interaction magnitude as roughly constant across generation (Liao et al., 2026; von Rad et al., 2026), despite evidence that pruning sensitivity depends on representational phase (Shi et al., 2026) and that no single sparse attention strategy dominates across generation stages (Nawrot et al., 2025)."
- "This assumption is problematic for reasoning models, whose generations alternate between broadly distributed attention (exploratory reasoning) and sharply concentrated attention (structured computation) (Ramachandran et al., 2026)."
- "On DeepSeek-R1-Distill-Qwen-7B (500 MATH-500 problems), the median phase difference rises from 0.39 at s=0.15 to 8.48 at s=0.30 (all Bonferroni-corrected p < 10⁻⁴); the Jonckheere-Terpstra z=33.7, p < 10⁻⁴)."
- "The pattern replicates on Qwen2.5-7B-Instruct (Δ = 0.07 → 3.16; all p < 10⁻³); preliminary evidence from DeepSeek-R1-Distill-Llama-8B (LlamaForCausalLM) suggests the phenomenon may extend beyond Qwen2 but at ~1/40 the magnitude and with substantially weaker strategy contrast."
- "Random eviction develops a detectable but weak phase gradient only above s ≥ 0.20 (3.20× — smaller than importance-based), confirming that the dominant gradient is an emergent phase-strategy interaction."
- "We present preliminary correlational evidence for discrimination collapse—head pruning flattening cumulative importance scores—as a contributing factor, with the structural specificity of importance-based pruning (which selectively removes high-score heads) as a key differentiator from random pruning."

---

## Page 2

### Section: 1 Introduction (continued)

- "Why can't existing single-axis findings predict our results? HIES (Choi et al., 2025) characterizes score collapse on a single compression axis; ThinkKV (Ramachandran et al., 2026) introduces phase-aware eviction without compound interaction; Nawrot et al. (2025) document strategy nondom­inance across generation stages."
- "A linear combination of these insights would predict that compound degradation either (i) uniformly amplifies, or (ii) follows the dominant single-axis pattern."
- "Instead, we observe a severity gradient spanning over an order of magnitude (G=7.5–79.8× for importance gradient vs. G ≈ 1 for random), an effect absent from any single-axis analysis."
- "In DeepSeek, this first manifests as a strategy ranking crossover at s=0.25; Qwen shows consistent importance dominance without crossover, indicating the crossover is model-dependent."
- "The compound interaction exceeds the multiplicative null by 2.7× in the low-sparsity phase while falling below it in the high-sparsity phase (Appendix B). This emergent coupling is not deducible from single-axis characteristics alone."

**This work is a diagnostic study**: "we characterize a previously unknown interaction effect rather than proposing a mitigation method."

Contributions:
1. "We identify a phase–strategy interaction: importance-based eviction exhibits a severity gradient across reasoning phases that is 3–30× larger than under random eviction (§5)."
2. "We show this gradient increases monotonically with sparsity and replicates across two Qwen2-architecture models (DeepSeek-R1-Distill-Qwen-7B and Qwen2.5-7B-Instruct), with exploratory evidence from a LlamaForCausalLM model suggesting the phenomenon may extend beyond Qwen2 (§5)."
3. "We provide a diagnostic analysis revealing that aggregate score collapse (Gini) is necessary but not sufficient for severity amplification, pointing to structural specificity of pruned heads as the key differentiator (§6)."

### Section: 2 Related Work

**Compound compression**: 
- "Combining multiple compression axes produces non-additive errors (Liao et al., 2026) report super-additive degradation when combining channel pruning with token eviction"
- "(Morafati et al., 2025) formalize compound error for quantization and sparsity, (von Rad et al., 2026) evaluate compound compression across 40+ benchmarks, revealing that reasoning capabilities degrade disproportionately (Ma et al., 2026) characterize independent phase transition points per compression dimension, implying the joint safe region is the intersection of per-dimension safe zones."
- "GRASPrune (Wang et al., 2026) learns global budget-constrained gates for joint pruning but treats decisions as static across generation."
- "PM-KVQ (Liu et al., 2026b) demonstrates that progressive quantization—gradually reducing bit-width over the generation process—mitigates cumulative error in long-CoT reasoning, implicitly introducing a temporal dimension to compression severity that resonates with our finding that compound interaction is phase-dependent."

---

## Page 3

### Section: 2 Related Work (continued)

**KV cache eviction**: 
- "Ada-KV (Feng et al., 2025) introduces per-head adaptive budgets; SnapKV (Li et al., 2024) compresses from a fixed observation window"
- "(Feng et al., 2026) show worst-case loss 2.2–4.3× higher than expected under standard aggregation."
- "(Choi et al., 2025) independently show that importance-based discrimination collapses under heavy single-axis pruning. Our work extends this to the compound setting, revealing that collapse is amplified by the interaction of two compression axes and modulated by reasoning phase—a phenomenon absent in single-axis analysis."

**Crossover effect (§5.3)**: "is a prediction that single-axis frameworks cannot generate. RLKV (Xu et al., 2025) uses reinforcement learning to identify reasoning-critical heads and selectively preserve their KV caches, demonstrating that head-level importance varies significantly for reasoning tasks."

**Phase-aware inference**: "ThinkKV (Ramachandran et al., 2026) applies different KV strategies per phase but without compound interaction. (Shi et al., 2026) find pruning sensitivity depends on 'silent' vs. 'decisive' representation phases."

### Section: 3 Background and Problem Setting

**Compound sparsity**: "Let s ∈ (0,1) denote a unified sparsity budget. Attention head pruning removes the bottom-s fraction of heads per layer by Frobenius-norm importance (Voita et al., 2019; Michel et al., 2019). KV cache eviction removes the bottom-s fraction of token positions from the cache. We compare two strategies: importance-based, which scores positions by position-normalized cumulative attention mass (Eq. 5 in Appendix A), and random, which evicts uniformly at random (Chen et al., 2024)."

"Applying both simultaneously yields compound sparsity; the two axes interact because head pruning alters the importance ranking used for eviction (Liao et al., 2026)."

**Interaction Index**: "For a text segment, let PPL_c denote perplexity under condition c ∈ {d, a, k, b} (dense, attention-only, KV-only, compound). Normalize by the dense baseline yields r_c = PPL_c / PPL_d, and:"

**Equation (1)**:
$$\text{II} = r_c - r_a - r_k + 1$$

- "II > 0 indicates super-additive degradation; II = 0 indicates additive independence."
- "We adopt the additive null because the two axes operate on disjoint dimensions; qualitative conclusions hold under the multiplicative null (Appendix B)."
- "Because the II distribution is heavily right-skewed, we report medians throughout."

**Severity gradient**: "To capture phase variation, the per-problem amplification ratio is:"

**Equation (2)**:
$$G^{(i)} = \frac{\text{II}_{low}^{(i)}}{\text{II}_{high}^{(i)}}$$

- "where II^(i)_{low/high} is the interaction index in the low/high-sparsity phase for problem i."
- "We report G = G^(i)_0, the median across problems, with bootstrap CI."
- "We use the median of per-problem ratios (not the ratio of medians) to preserve per-problem pairing; see Appendix D for comparison. G >> 1 indicates phase-concentrated severity."

**Phase segmentation**: "Inspired by ThinkKV's phase-aware perspective on reasoning-time computation (Ramachandran et al., 2026), each generated sequence is partitioned into three phases (low-, mid-, high-sparsity) by tercile boundaries of per-position attention sparsity, using min_phase_length=10."
- "Low-sparsity phases correspond to broadly distributed attention (exploratory reasoning); high-sparsity phases to concentrated attention (structured computation)."

### Section: 4 Experimental Setup

**Models**: "We evaluate on two 7B-parameter models sharing the Qwen2 backbone (28 layers, 28 heads, 4-group GQA): DeepSeek-R1-Distill-Qwen-7B (DeepSeek-AI, 2025), distilled from DeepSeek-R1 with explicit chain-of-thought traces yielding pronounced phase structure; and Qwen2.5-7B-Instruct (Yang et al., 2024), with standard instruction tuning, providing a cross-model replica-tion target. Both are loaded in bf16 cast to f16 with eager attention.¹"

¹ footnote: "An earlier f16at16 configuration produced sporadic NaN values; bf16at16 eliminated all occurrences."

---

## Page 4

### Section: 4 Experimental Setup (continued)

**Dataset**: "We evaluate all 500 problems from MATH-500 (Hendrycks et al., 2021). Each problem is decoded greedily (max_new_tokens: 2048). Problems with degenerate phase assignments (null low or high phases) are excluded, yielding effective sample sizes of n = 496 for DeepSeek (4 excluded) and n = 475 for Qwen (25 excluded). Qwen"

"exhibits a higher mid-phase null rate (45.2% vs. 10.2% for DeepSeek) due to lower temporal auto-correlation in its attention sparsity patterns (lag-1 r=0.718 vs. 0.891, p_diff < 1.6×; this does not affect the primary gradient metric Δ = II_low − II_high, which requires only low and high phases."

"Sensitivity analysis across min_phase_length ∈ {5, 10, 20} confirms robustness (Appendix M)."

**Sparsity configuration**: "We apply symmetric compound sparsity at s ∈ {0.15, 0.20, 0.25, 0.30}, comparing perplexity under four conditions: dense, attention-only, KV-only, and compound. We compare importance-based eviction (position-normalized cumulative attention score, Eq. 5; BOS always retained) and random eviction (uniform). Heads are pruned per layer by Frobenius norm; under random eviction, both heads and positions are selected uniformly."

**Phase segmentation and metrics**: "Each sequence is segmented into three phases using the quantile-based method (§3), with min_phase_length=10. We compute segment-level perplexity, II (Eq. 1), and G (Eq. 2), reporting medians across problems to ensure robustness (deviation up to 43:1)."

"Robustness to segmentation granularity (quartile, quintile; Appendix N) and minimum phase length (5, 10, 20 tokens; Appendix M) is verified."

**Statistical analysis**: "All reported confidence intervals use nonparametric bootstrap (B=10,000 iterations—note §4.2 (Efron and Tibshirani, 1993). Significance tests use Wilcoxon signed-rank (paired within-model) or Mann-Whitney U (cross-model), with Bonferroni correction at family-wise α = 1 (per model×strategy combination: 4 sparsity levels testing one dose-response hypothesis). Benjamini-Hochberg FDR correction across all 44 tests is reported as a robustness check in Appendix I; all Bonferroni-significant results remain significant under BH-FDR."

"Dose-response monotonicity is confirmed by the Jonckheere-Terpstra test (z=6.2–33.7, all p < 10⁻⁷), which uses per-problem values (n=496 per group) rather than aggregated medians.²"

"Scaling from n=50 (profiling) to n=500 narrowed bootstrap CI width by 2.5×-5.9× across all 16 conditions, directly demonstrating precision gains. G"

²footnote: "Spearman rank correlation on the four aggregate medians (rₛ= 1.0, exact permutation p = 0.042, one-tailed) is consistent but has limited power at n=4 levels; we rely on the JT test as primary evidence."

### Additional statistical values visible:

- **Sample sizes**: n=496 (DeepSeek, 4 excluded from 500), n=475 (Qwen, 25 excluded from 500)
- **Bootstrap iterations**: B=10,000
- **Models**: 7B-parameter, 28 layers, 28 heads, 4-group GQA
- **Sparsity levels tested**: s ∈ {0.15, 0.20, 0.25, 0.30}
- **Jonckheere-Terpstra**: z = 6.2–33.7, all p < 10⁻⁷
- **Lag-1 autocorrelation**: r = 0.718 (Qwen) vs. 0.891 (DeepSeek), p_diff < 1.6×
- **Mid-phase null rate**: 45.2% (Qwen) vs. 10.2% (DeepSeek)
- **Bootstrap CI width reduction**: 2.5×–5.9× when scaling n=50 to n=500

---

**Summary of equations across all 4 pages:**

| Eq. # | Definition |
|-------|-----------|
| (1) | II = r_c − r_a − r_k + 1 (Interaction Index) |
| (2) | G^(i) = II_low^(i) / II_high^(i) (Per-problem amplification ratio) |

**Key numerical claims across all pages:**

- Amplification ratios G range from 7.5× (cv=0.15) to 78× (cv=0.30)
- Median Δ = 0.39 → 8.46 across sparsity levels (DeepSeek)
- Δ = 0.07 → 3.16 (Qwen replication)
- All Bonferroni-corrected p < 10⁻⁴ (DeepSeek), p < 10⁻³ (Qwen)
- Jonckheere-Terpstra z = 33.7, p < 10⁻⁴ (DeepSeek)
- Crossover at s ≈ 0.25 (DeepSeek, model-dependent)
- Compound interaction exceeds multiplicative null by 2.7× in low-sparsity phase
- Random eviction phase gradient detectable only at s ≥ 0.20, magnitude 3.20× (vs. 7.5–78× for importance-based)
- 99% CI for G at cv=0.15: [1.1, 14.0]; at cv=0.30: [63.3, 96.3]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0501f29-0cc5-4ac0-81d1-3ae5b6bfaf3d",
  "isSidechain": true,
  "agentId": "ab89d0e2030cc79d8",
  "requestId": "req_011Cb4TKG6PLg63o5zGRkbK6",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "ad80a69e-ae0e-4357-831d-371b534af4dc",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_1_a349de4f",
  "sessionId": "6800e980-8ff4-4c1b-b16a-22a299d19954",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A6w7FnicQCKWrqv19jeMvV",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2738,
      "cache_read_input_tokens": 15956,
      "output_tokens": 4630,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2738
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4630,
          "cache_read_input_tokens": 15956,
          "cache_creation_input_tokens": 2738,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2738,
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
