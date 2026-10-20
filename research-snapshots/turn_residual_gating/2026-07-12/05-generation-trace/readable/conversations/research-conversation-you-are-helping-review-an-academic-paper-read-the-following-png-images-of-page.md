# Research conversation: You are helping review an academic paper. Read the following PNG images of pages 4-6 of the paper and provide a DETAILED

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 10
- **Recorded user turns:** 1
- **Tool calls:** 3
- **Original source:** `logs/chats/exported-trajectories/account-3/agent-a1a91bfa0b98ff8d0.jsonl`
- **Structured JSON:** [`a7ac47e1b6ae13ffa4f5.json`](../../sessions/a7/a7ac47e1b6ae13ffa4f5.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Round 1

10 recorded events

### User

_source line 1 · 2026-05-14T12:55:38.589Z_

You are helping review an academic paper. Read the following PNG images of pages 4-6 of the paper and provide a DETAILED transcription/summary of ALL content on each page. Include:
- All text content (section headings, body text, methodology details)
- All figure/table descriptions and their captions with all data values
- All equations and their numbering
- All footnotes
- Page layout observations

The images are at:
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png
- /home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png

Be extremely thorough - this is for peer review. Report EVERYTHING you see on each page, preserving the logical structure. Pay special attention to table values, equation details, and methodology specifics.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": true,
  "promptId": "5d5cecfd-5407-423c-913f-64eb717b21d0",
  "agentId": "a1a91bfa0b98ff8d0",
  "type": "user",
  "uuid": "82785d93-492c-4ea2-a82d-fb62faf96748",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 2 · 2026-05-14T12:55:38.592Z_

```json
{
  "parentUuid": "82785d93-492c-4ea2-a82d-fb62faf96748",
  "isSidechain": true,
  "agentId": "a1a91bfa0b98ff8d0",
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
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
      "mcp__agent-ml-research__cleanup_pdf_images",
      "mcp__agent-ml-research__pdf_to_images",
      "mcp__agent-ml-research__review_reviewer_post_to_director",
      "mcp__agent-ml-research__verify_references"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "5e2b6b15-c33d-474d-9381-b5a4b63baba0",
  "timestamp": "2026-05-14T12:55:38.592Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 3 · 2026-05-14T12:55:41.013Z_

I'll read all three images simultaneously.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5e2b6b15-c33d-474d-9381-b5a4b63baba0",
  "isSidechain": true,
  "agentId": "a1a91bfa0b98ff8d0",
  "requestId": "req_011Cb2VnVs65WA6nXb5cwR6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "bf9a9347-55ed-4e23-8f5c-51617c11cf9b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y6RicyG3jp5Uv4x17Cv3Nt",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8624,
      "cache_read_input_tokens": 8130,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 8624,
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

_source line 4 · 2026-05-14T12:55:41.621Z_

<details open><summary>🔧 Tool call — Read · `toolu_01EPLacCXtNW37EvyAVTBvpV`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf9a9347-55ed-4e23-8f5c-51617c11cf9b",
  "isSidechain": true,
  "agentId": "a1a91bfa0b98ff8d0",
  "requestId": "req_011Cb2VnVs65WA6nXb5cwR6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "f78d7555-ecf7-4828-aaab-ec3536ff3466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y6RicyG3jp5Uv4x17Cv3Nt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8624,
      "cache_read_input_tokens": 8130,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 8130,
          "cache_creation_input_tokens": 8624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8624,
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

_source line 5 · 2026-05-14T12:55:42.024Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WgTgeQCsCFVZj5CUvWUgbG`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f78d7555-ecf7-4828-aaab-ec3536ff3466",
  "isSidechain": true,
  "agentId": "a1a91bfa0b98ff8d0",
  "requestId": "req_011Cb2VnVs65WA6nXb5cwR6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "8086ba48-2325-4c21-bcee-5f67cfe5c10d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y6RicyG3jp5Uv4x17Cv3Nt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8624,
      "cache_read_input_tokens": 8130,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 8130,
          "cache_creation_input_tokens": 8624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8624,
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

_source line 6 · 2026-05-14T12:55:42.641Z_

<details open><summary>🔧 Tool call — Read · `toolu_01VBirdN1FYSMTyX4Kzb7Bds`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/artifacts/_project/paper/_pdf_images/main_a1a036_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8086ba48-2325-4c21-bcee-5f67cfe5c10d",
  "isSidechain": true,
  "agentId": "a1a91bfa0b98ff8d0",
  "requestId": "req_011Cb2VnVs65WA6nXb5cwR6W",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "fe25f332-207f-4581-9ea6-4aefb19fe508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01Y6RicyG3jp5Uv4x17Cv3Nt",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 8624,
      "cache_read_input_tokens": 8130,
      "output_tokens": 287,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 8624
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 287,
          "cache_read_input_tokens": 8130,
          "cache_creation_input_tokens": 8624,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 8624,
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

_source line 7 · 2026-05-14T12:55:52.117Z_

<details><summary>↩ Tool result · `toolu_01EPLacCXtNW37EvyAVTBvpV`</summary>

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
  "parentUuid": "f78d7555-ecf7-4828-aaab-ec3536ff3466",
  "isSidechain": true,
  "promptId": "5d5cecfd-5407-423c-913f-64eb717b21d0",
  "agentId": "a1a91bfa0b98ff8d0",
  "type": "user",
  "uuid": "393ec904-7e83-444b-8ad8-c6ff51f61ffc",
  "sourceToolAssistantUUID": "f78d7555-ecf7-4828-aaab-ec3536ff3466",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-14T12:55:53.505Z_

<details><summary>↩ Tool result · `toolu_01VBirdN1FYSMTyX4Kzb7Bds`</summary>

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
  "parentUuid": "fe25f332-207f-4581-9ea6-4aefb19fe508",
  "isSidechain": true,
  "promptId": "5d5cecfd-5407-423c-913f-64eb717b21d0",
  "agentId": "a1a91bfa0b98ff8d0",
  "type": "user",
  "uuid": "86023e76-97a8-4719-8680-dd3855dff236",
  "sourceToolAssistantUUID": "fe25f332-207f-4581-9ea6-4aefb19fe508",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 9 · 2026-05-14T12:55:53.533Z_

<details><summary>↩ Tool result · `toolu_01WgTgeQCsCFVZj5CUvWUgbG`</summary>

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
  "parentUuid": "8086ba48-2325-4c21-bcee-5f67cfe5c10d",
  "isSidechain": true,
  "promptId": "5d5cecfd-5407-423c-913f-64eb717b21d0",
  "agentId": "a1a91bfa0b98ff8d0",
  "type": "user",
  "uuid": "0621b730-ab1b-4fd6-98ce-15e63052b071",
  "sourceToolAssistantUUID": "8086ba48-2325-4c21-bcee-5f67cfe5c10d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 10 · 2026-05-14T12:57:14.340Z_

Here is the detailed transcription of all content on pages 4–6:

---

## PAGE 4 (main_a1a036_p4.png)

### Layout
Two-column format. Left column continues Section 3 (method), right column begins Section 4 (Experimental Setup) and Section 5 (Results).

---

### Left Column (continuation of prior section)

**Quantile-based segmentation.** Tokens are partitioned into **high-**, **mid-**, and **low-sparsity** phases by the textile boundaries of {π_i}. Segments shorter than 10 tokens are merged into adjacent phases. The segmentation is data-driven and requires only attention weights.

*(Table 1 caption appears here — see below)*

---

### Section 4: Experimental Setup

**4.1 Models**

We evaluate two 7B-parameter instruction-tuned models sharing the Qwen2 backbone (28 layers, 28 heads with 4-group GQA): **DeepSeek-R1-Distill-Qwen-7B** (DeepSeek-AI, 2025), distilled from DeepSeek-R1, produces explicit chain-of-thought traces with pronounced phase structure. **Qwen2.5-7B-Instruct** (Yang et al. 2024) provides standard model replication with standard instruction tuning rather than reasoning distillation. Both models are loaded in BFloat16 with custom attention to permit direct manipulation of attention matrices.¹

---

**4.2 Dataset**

We evaluate on a 50-problem stratified subset of MATH-500 (Hendrycks et al., 2021), sampling uniformly across levels 3–5 (difficulty levels 3, 4, 5). Each problem is decoded greedily (max_new_tokens=2048).

---

**4.3 Configuration and Metrics**

We apply symmetric compound sparsity: for level s ∈ {0.15, 0.20, 0.25, 0.30}, the same fraction s of attention heads and KV cache entries are removed. For each problem, we compute perplexity under four conditions: dense, attention-only pruning, KV-only, and **importance-based**. We compare **importance-based** eviction (position-normalized cumulative attention, Eq. 3; BOS always retained) against a **random** baseline. Heads are pruned per layer by Frobenius norm under importance-based eviction and uniformly at random otherwise.

Each sequence is segmented into three reasoning phases using the quantile-based method of §3.3 (min_phase_length=10). For each condition and phase, we compute the Interaction Index (Eq. 4) and severity gradient (Eq. 5), reporting medians as central tendency. Statistical validation uses nonparametric bootstrap (B=10,000) with paired permutation tests; details in Appendix D.²

---

**Footnotes:**
¹ "An earlier float16 configuration produced sporadic NaN values in Layer 27 of DeepSeek-R1-Distill-Qwen-7B. float16 eliminated entirely."

² "Experiments were conducted on 4× NVIDIA RTX PRO 6000 Blackwell Server Edition 96 GB GPUs."

---

### Right Column — Table 1 and Section 5

**Table 1.** Median compound severity difference (Δ = Ĥ_bas − Ĥ_dist) by eviction strategy and sparsity level on DeepSeek-R1-Distill-Qwen-7B (n=50) MATH-500 problems.

| Strategy | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|----------|--------|--------|--------|--------|
| Importance | 0.06 | 0.08 | 7.16 | 14.59 |
| Random | 0.01 | 0.02 | 0.54 | 1.54 |

---

### Section 5: Results

**5.1 Strategy-Dependent Severity (C1)**

The compound severity difference reveals a stark dependence on eviction strategy. Table 1 reports the median compound severity difference Δ = Ĥ_bas − Ĥ_dist across 50 problems for each strategy and sparsity level. Under importance-based eviction, compound sparsity produces substantial super-additive degradation that grows with sparsity: Δ increases from 0.06 at s=0.15 to 14.59 at s=0.30, a 37× amplification. Under random eviction, the severity difference shows no systematic growth, remaining near zero (−0.02 to 1.54).

This strategy dependence indicates that compound sparsity severity is not an intrinsic property of the compression level. Rather, the same sparsity configuration produces qualitatively different compound behavior depending on the eviction strategy — an emergent phase-strategy interaction whose structure we unpack in the following subsections.

---

## PAGE 5 (main_a1a036_p5.png)

### Layout
Two-column format. Contains Figure 1 (left column), Figure 2 (right column), Section 5.2, and Section 5.3.

---

### Figure 1 (left column)

**Caption:** "Figure 1: Severity gradient (G) as a function of sparsity level s. Importance-based eviction (solid) exhibits an increasing gradient from 69× to 274×, while random eviction (dashed) remains flat near 1×. Shaded regions denote 95% bootstrap confidence intervals."

*Description:* A line plot with sparsity level s on the x-axis (range approximately 0.13 to 0.30) and Severity gradient G on the y-axis. Two series: "Importance-based" (solid line, rising steeply) and "Random" (dashed line, near-flat). The importance-based curve rises sharply, especially between s=0.20 and s=0.30.

---

### Left column text (Section 5.2 begins)

Continuing from page 4 — sparsity levels, confirming that phase modulation is specific to the emergent interaction between head pruning and importance-based scoring.

The gradient growth is sub-exponential: successive ratios of the median severity difference Δ between adjacent sparsity levels are 3.8×, 4.8×, and 2.0× — a decreasing terminal growth rate, consistent with a ceiling effect as compound degradation in the low-sparsity phase approaches saturation. The severity gradient G exhibits the same pattern, with consecutive ratios of 1.5×, 2.2×, and 1.2×. Figure 1 visualizes this trajectory, contrasting the steep importance-based curve against the flat random baseline.

We report medians throughout because the II distribution is right-skewed: the mean severity difference exceeds the median by a factor of 1.6:1 at s=0.30 under importance-based eviction (mean Δ = 22.94 vs. median Δ = 14.59). The median resists the influence of outlier problems with exceptionally long reasoning traces, while bootstrap confidence intervals (95%) account for this skewness via the resampling distribution.

---

**5.3 Phase-Strategy Crossover (C3)**

The phase-modulated gradient produces a striking qualitative phenomenon: a crossover in which importance-based eviction is simultaneously the better and worse strategy depending on the reasoning phase. At s=0.25, importance-based eviction yields a lower II than random in the high-sparsity phase (Ĥ_high = 0.032 vs. 0.818), but a higher II in the low-sparsity phase (Ĥ_low = 7.196 vs. 1.363). The difference-in-difference is remarkable — importance-based eviction has 5.3× higher II in the low-sparsity phase, reversing the strategy ranking.

---

### Figure 2 (right column)

**Caption:** "Figure 2: Strategy-dependent crossover at s=0.25. Grouped bar chart of median II by eviction strategy and reasoning phase. Importance-based eviction outperforms random in the high-sparsity phase but produces 5.3× higher II in the low-sparsity phase, reversing the strategy ranking."

*Description:* A grouped bar chart with three groups on the x-axis: "High-sparsity phase", "Mid-sparsity phase", "Low-sparsity phase". Y-axis is "Median II" on a log scale (range approximately 10⁻² to 10¹). Two bars per group: "Importance-based" (blue/solid) and "Random" (red/striped). In the high-sparsity phase, importance-based bar is lower; in the low-sparsity phase, importance-based bar is markedly higher than random.

---

### Right column text (cont. of 5.3)

Figure 2 displays the crossover structure as a heatmap of per-phase II values across strategies and sparsity levels.

The crossover emerges from an emergent phase-strategy interaction: in the high-sparsity phase — where attention is already focused — importance-based eviction preserves genuinely critical positions, yielding lower compound severity than random eviction. In the low-sparsity phase, however, head pruning redistributes attention mass across surviving heads, altering the importance score landscape in a way that couples the two sparsity mechanisms (§6). The result is that targeted eviction inadvertently removes positions that would have been protected under the re-ranked attention score ranking — producing higher compound severity than the explicitly random baseline.

The crossover is present at all four tested sparsity levels (s ≥ 0.15): at each level, importance-based eviction achieves lower II in the high-sparsity phase but higher II in the low-sparsity phase relative to random eviction. The magnitude of the low-phase reversal grows from 0.6× at s=0.15 to 5.4× at s=0.20, before moderating to 3.6× at s=0.30 as random eviction severity also rises.

---

## PAGE 6 (main_a1a036_p6.png)

### Layout
Two-column format. Contains Table 2, Table 3, Table 4, Section 5.4, Section 5.5, and beginning of Section 6.

---

### Table 2 (top left, spanning approximately half-column width)

**Caption:** "Table 2: Interaction index (II) by eviction strategy, reasoning phase, and sparsity level. Values are problem-level medians across 50 problems. Δ = Ĥ_bas − Ĥ_dist is the median severity difference. G = Ĥ_bas/Ĥ_dist quantifies phase-dependent II."

| s | Strategy | Ĥ_high | Ĥ_mid | Ĥ_low | Δ | G |
|---|----------|--------|-------|-------|---|---|
| 0.15 | Importance | 0.006 | 0.081 | 0.908 | 0.39 | 69 |
| 0.15 | Random | 0.007 | 0.029 | 0.103 | 0.10 | 4.1 |
| 0.20 | Importance | 0.015 | 0.203 | 1.486 | 1.48 | 101 |
| 0.20 | Random | 0.292 | 0.350 | 1.406 | 1.78 | 7 |
| 0.25 | Importance | 0.032 | 1.118 | 7.196 | 14.59 | **222** |
| 0.25 | Random | 0.818 | 0.932 | 1.363 | 0.54 | 1.7 |
| 0.30 | Importance | 0.053 | 1.263 | 14.639 | 14.59 | **274** |
| 0.30 | Random | 2.503 | 2.592 | 4.041 | 1.54 | 1.8 |

*(Note: Some values may have slight transcription variance given image resolution — exact numbers should be verified against source PDF.)*

---

### Table 3 (bottom left)

**Caption:** "Table 3: Cross-model replication: median compound severity difference (Δ = Ĥ_bas − Ĥ_dist − Ĥ_dist) under importance-based eviction."

| Model | s=0.15 | s=0.20 | s=0.25 | s=0.30 |
|-------|--------|--------|--------|--------|
| DeepSeek-R1-7B | 0.39 | 1.48 | 7.16 | 14.59 |
| Qwen2.5-7B | 0.04 | 0.23 | 0.44 | 0.80 |

"Both models share the Qwen2 architecture but differ in training (distillation vs. instruction tuning). DeepSeek-R1-7B = DeepSeek-R1-Distill-Qwen-7B; Qwen2.5-7B = Qwen2.5-7B-Instruct."

---

### Table 4 (top right)

**Caption:** "Table 4: Paired d_s for phase-dependent II (low → high) under importance-based eviction. Bootstrap 95% CIs (B=10,000)."

| | DS-d_s | Δ | [CI] | QW d_s | |
|--|--------|---|------|--------|--|
| 0.15 | 0.44 | 0.52 | [0.20, 0.47] | 0.28 | 0.05 [−0.11, 0.11]* |
| 0.20 | 0.68 | 1.15 | [0.15, 2.16] | 0.40 | — |
| 0.25 | 0.94 | 20.16 | [10.16, 31.0] | 0.62 | — |
| 0.30 | 0.94 | 38.29 | [16.10, 71.0] | 2.62 | [1.72, 3.61] |

*Marginal at s=0.15; not significant (p_corr ≥ 0.20).*

---

### Section 5.4 Cross-Model Replication (C5)

To establish cross-model replication, we run importance-based eviction experiments on Qwen2.5-7B-Instruct, which shares the Qwen2 backbone. Table 3 compares the median severity difference across both models.

Qwen2.5-7B-Instruct qualitatively reproduces the monotonic severity gradient: Δ increases from 0.04 at s=0.15 to 2.03 at s=0.30 (Table 3), paralleling DeepSeek's trajectory at approximately one-fifth the absolute magnitude. Both models yield strictly increasing patterns across sparsities (DeepSeek: 0.44 → 0.80; Qwen: 0.28 → 1.02; Table 4), with Spearman ρ = 1.0 between the four-point sequences (gradient permutation p = 0.04). Full per-problem concordance analysis and random eviction controls appear in Appendix C.

The replication suggests that the phase-modulated severity gradient is an emergent property of how compound sparsity interacts with attention dynamics in Transformer-based reasoning, not an artifact of DeepSeek's distillation-induced phase structure. Generalization to other architectures remains an open question (§7.1).

---

### Section 5.5 Statistical Validation (C6)

All four sparsity levels reject H₀ (no strategy difference) via paired permutation tests after Bonferroni correction (p_corr < 0.005). Paired effect sizes (d_s) grow monotonically: DeepSeek from 0.44 (small) to 0.80 (large); Qwen from 0.28 (marginal) to 1.02 (large). Table 4 reports full d_s values and bootstrap CIs; details in Appendix D.

---

### Section 6: Analysis: Mechanisms of Phase-Modulated Severity

Why is compound severity phase-modulated for importance-based but not random eviction? We identify **discrimination collapse** as the primary mechanism, with a secondary entropy redistribution effect that is model-dependent.

**6.1 Discrimination Collapse Under Head Pruning**

The KV-importance score (Eq. 3) aggregates attention mass across surviving heads. Head pruning makes the cumulative importance distribution more uniform, reducing the gap between highly-attended and rarely-attended positions. We measure this via the **Gini coefficient** (inequality of importance scores) and **coefficient of variation (CV)**.

Table 5 shows consistent negative deltas across...

*(Section 6.1 text is cut off at the bottom of page 6.)*

---

### Summary of Key Numerical Values Across Pages 4–6

- Table 1: Δ peaks at 14.59 (importance, s=0.30) vs. 1.54 (random, s=0.30)
- Figure 1: G rises from 69× to 274× for importance-based; stays ~1× for random
- Figure 2: 5.3× reversal at s=0.25 in low-sparsity phase
- Table 2: G = 274 at s=0.30 importance-based; G = 1.8 at s=0.30 random
- Table 3: DeepSeek Δ = 14.59 at s=0.30; Qwen Δ = 0.80
- Table 4: d_s reaches 0.94 / 38.29 CI-bounded at s=0.30 for DeepSeek

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0621b730-ab1b-4fd6-98ce-15e63052b071",
  "isSidechain": true,
  "agentId": "a1a91bfa0b98ff8d0",
  "requestId": "req_011Cb2VobuWDfg9uaDHuSbGv",
  "attributionAgent": "general-purpose",
  "type": "assistant",
  "uuid": "2280fcfa-5ddd-40c1-8821-c16c40abbd43",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_11/projects/phase-gated-compound-sparse/.claude/sessions/review_reviewer_2_d0398257",
  "sessionId": "bfa63e26-fdd4-4cf2-9c52-defc70917f56",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-sonnet-4-6",
    "id": "msg_01GYRKsJmAGen5PyzLYzMUKB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 2283,
      "cache_read_input_tokens": 16754,
      "output_tokens": 4427,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2283
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 4427,
          "cache_read_input_tokens": 16754,
          "cache_creation_input_tokens": 2283,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2283,
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
