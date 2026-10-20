# Research conversation: [系统通知 — worker_done:worker_code_exp_019_supervised_verifier_20260515T100946]: Worker worker_code_exp_019_supervised_veri — Part 3 of 3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap (July export snapshot)** · Conversation logs

[← Part 2](part-002.md) · [Transcript overview](../research-conversation-worker-done-worker-code-exp-019-supervised-verifier-20260515t100946-worker-wor.md) · [Structured JSON](../../../sessions/b2/b2c972260b9bdd6c7a28.json)

## Round 32

### Tool call

_source line 502 · 2026-05-15T11:48:28.239Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01BDC3BmoqUDQ1jLhdjVPtYp`</summary>

```json
{
  "description": "Read paper LaTeX files",
  "subagent_type": "Explore",
  "prompt": "I need to find all .tex files in the paper directory for the struct_self_consist_ie project. The paper is likely in /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ or a subdirectory. Look for directories containing main.tex, paper.tex, or similar LaTeX main files. Also check for a \"paper\" or \"latex\" subdirectory. Search breadth: medium."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6edf0088-c893-4066-8b9e-0e26f9caa0a2",
  "isSidechain": false,
  "requestId": "req_011Cb4JTSyA2Wu7sLZv4aAmd",
  "type": "assistant",
  "uuid": "27f15046-73db-4566-abab-e54746a3330c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_013gyagme1PLdp5pdCAyFdZN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1402,
      "cache_read_input_tokens": 78842,
      "output_tokens": 367,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1402,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 367,
          "cache_read_input_tokens": 78842,
          "cache_creation_input_tokens": 1402,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1402
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

_source line 503 · 2026-05-15T11:48:46.058Z_

<details><summary>↩ Tool result · `toolu_01BDC3BmoqUDQ1jLhdjVPtYp`</summary>

```text
Perfect! I found all the .tex files in the project. Here's a summary of the LaTeX files organized by location:

## Main Paper Directory

The primary paper source is located at:
- **/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/**

**Main LaTeX file:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`

**Section files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`

**Root-level paper files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex`

## Artifacts Directory

Generated paper.tex files in dream reports:
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/{best,median,worst}/paper.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/{best,median,worst}/paper.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/{best,median,worst}/paper.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/{best,median,worst}/paper.tex`

**Project artifact files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex`

**Table files:**
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex`
- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex`

## Summary

You have **38 total .tex files** across the project. The main paper source is in the `/docs/paper/` directory with `main.tex` as the entry point, organized into sections. Additional generated files are stored in `/artifacts/` for different experimental variants and table generation.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "27f15046-73db-4566-abab-e54746a3330c",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "60a41ab6-dcbf-43e1-b827-f157d137463b",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to find all .tex files in the paper directory for the struct_self_consist_ie project. The paper is likely in /home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/ or a subdirectory. Look for directories containing main.tex, paper.tex, or similar LaTeX main files. Also check for a \"paper\" or \"latex\" subdirectory. Search breadth: medium.",
    "agentId": "ab797380793121bf0",
    "agentType": "Explore",
    "content": [
      {
        "type": "text",
        "text": "Perfect! I found all the .tex files in the project. Here's a summary of the LaTeX files organized by location:\n\n## Main Paper Directory\n\nThe primary paper source is located at:\n- **/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/**\n\n**Main LaTeX file:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex`\n\n**Section files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/method.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/related_work.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex`\n\n**Root-level paper files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/abstract.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/discussion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/conclusion.tex`\n\n## Artifacts Directory\n\nGenerated paper.tex files in dream reports:\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T093336/{best,median,worst}/paper.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T105303/{best,median,worst}/paper.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260514T203201/{best,median,worst}/paper.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/dream_reports/dream_20260515T092545/{best,median,worst}/paper.tex`\n\n**Project artifact files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/abstract.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/introduction.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/related_work.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/experiments.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/discussion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/conclusion.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/limitations.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/_project/paper/freeform_ablation_appendix_table.tex`\n\n**Table files:**\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/bootstrap_ci_tables.tex`\n- `/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/freeform_ablation_appendix_table.tex`\n\n## Summary\n\nYou have **38 total .tex files** across the project. The main paper source is in the `/docs/paper/` directory with `main.tex` as the entry point, organized into sections. Additional generated files are stored in `/artifacts/` for different experimental variants and table generation."
      }
    ],
    "totalDurationMs": 17813,
    "totalTokens": 25708,
    "totalToolUseCount": 3,
    "usage": {
      "input_tokens": 680,
      "cache_creation_input_tokens": 2913,
      "cache_read_input_tokens": 20717,
      "output_tokens": 1398,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 2913
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 680,
          "output_tokens": 1398,
          "cache_read_input_tokens": 20717,
          "cache_creation_input_tokens": 2913,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 2913,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 1,
      "bashCount": 2,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 0
    }
  },
  "sourceToolAssistantUUID": "27f15046-73db-4566-abab-e54746a3330c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Runtime record

_source line 504 · 2026-05-15T11:48:46.088Z_

```json
{
  "parentUuid": "60a41ab6-dcbf-43e1-b827-f157d137463b",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "856ae6a4-9b66-4a98-9751-d532f03ec4fe",
  "timestamp": "2026-05-15T11:48:46.088Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

---


### Assistant

_source line 505 · 2026-05-15T11:48:49.223Z_

<details><summary>Logged reasoning block</summary>

```text
Now I need to read the actual paper files to do the review. Let me read the key sections in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "856ae6a4-9b66-4a98-9751-d532f03ec4fe",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "a539c781-1aac-47a5-bbb1-0e18da009e8f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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

_source line 506 · 2026-05-15T11:48:49.710Z_

<details open><summary>🔧 Tool call — Read · `toolu_01CEVyYWTe4cJmQnXF8RfHyL`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a539c781-1aac-47a5-bbb1-0e18da009e8f",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "8554fc5d-3819-4cb1-b2d3-8d03afb37180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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

_source line 507 · 2026-05-15T11:48:49.725Z_

<details><summary>↩ Tool result · `toolu_01CEVyYWTe4cJmQnXF8RfHyL`</summary>

```text
1	\begin{abstract}
2	Test-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.
3	We evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.
4	These signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom---a \textit{correlation-selection gap}.
5	Four of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.
6	Neither succeeds: log-probability scores are compressed into effective ties for 60\% of instances, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.
7	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
8	Signal rankings further depend on task complexity, with findings consistent across model families.
9	\end{abstract}
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8554fc5d-3819-4cb1-b2d3-8d03afb37180",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "0f29df51-6a41-47b3-a78f-a7fc0926716c",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/abstract.tex",
      "content": "\\begin{abstract}\nTest-time scaling through repeated sampling promises quality gains for LLM-based information extraction (IE), but whether confidence signals can identify the best output among multiple candidates remains untested for structured tasks.\nWe evaluate five confidence signals from three families across NER and relation extraction on three benchmarks with two 8B-parameter model families.\nThese signals achieve strong quality estimation, yet none significantly improves sample selection over greedy decoding despite 13--18 percentage points of oracle headroom---a \\textit{correlation-selection gap}.\nFour of five signals are instance-level by construction and cannot rank candidates; the key empirical question is whether log-probability---the sole per-sample signal---or consensus-proximity selection can bridge this gap.\nNeither succeeds: log-probability scores are compressed into effective ties for 60\\% of instances, while consensus-proximity (MBR decoding) fails because utility correlates with quality across instances but not within them.\nA controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.\nSignal rankings further depend on task complexity, with findings consistent across model families.\n\\end{abstract}\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "8554fc5d-3819-4cb1-b2d3-8d03afb37180",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool call

_source line 508 · 2026-05-15T11:48:50.177Z_

<details open><summary>🔧 Tool call — Read · `toolu_01B1UCUyYCCTgAE9ihHFZcGp`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0f29df51-6a41-47b3-a78f-a7fc0926716c",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "4fec7e36-3bb2-4d6e-b776-2d5147678ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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

_source line 509 · 2026-05-15T11:48:50.183Z_

<details><summary>↩ Tool result · `toolu_01B1UCUyYCCTgAE9ihHFZcGp`</summary>

```text
1	\section{Introduction}\label{sec:introduction}
2	
3	Self-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.
4	On discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \citealp{wang2023selfconsistency}).
5	More broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \cite{snell2024scaling, brown2024monkeys}.
6	These results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.
7	For tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.
8	But information extraction (IE) poses a fundamentally different challenge.
9	The output is not a single token or number; it is a \textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.
10	There is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.
11	Can self-consistency still provide useful signal in this structured setting?
12	
13	Prior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \textit{quality estimation} (which inputs does the model handle reliably?) and \textit{sample selection} (which of $N$ outputs is best?).
14	These require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.
15	Self-consistency methods for discrete answers \cite{wang2023selfconsistency, chen2024usc} and weighted variants \cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.
16	The most relevant study, \citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.
17	Our work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\rho{=}0.038$ (n.s.) and LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$)---that would be invisible on a single dataset.
18	
19	Structured IE requires schema-compliant output, making constrained decoding \cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\% valid JSON rate (\S\ref{sec:ablation}).}
20	All experiments use constrained decoding, the regime under which structured IE is practically deployed.
21	
22	Our central finding is the \textbf{correlation-selection gap} (Figure~\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.
23	By construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.
24	The non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.
25	Both fail: MBR utility correlates with F1 across instances but not within them (\S\ref{sec:discussion}); log-probability scores are severely compressed (60\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
26	A controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\S\ref{sec:ablation}).
27	
28	\begin{figure*}[t]
29	\centering
30	\includegraphics[width=\textwidth]{fig_overview}
31	\caption{The correlation-selection gap. \textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}
32	\label{fig:overview}
33	\end{figure*}
34	
35	We systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \cite{luan2018scierc}, CoNLL-2003 \cite{tjongkimsang2003conll}, and WNUT-17 \cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.
36	Our contributions are:
37	\begin{enumerate}
38	    \item \textbf{The correlation-selection gap and its diagnosis.}
39	    We demonstrate that strong quality estimation ($\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).
40	    Log-probability---the only per-sample signal---fails due to score compression (60\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).
41	    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.
42	
43	    \item \textbf{A systematic evaluation framework.}
44	    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.
45	
46	    \item \textbf{Task-complexity boundary conditions.}
47	    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.
48	    At the capability boundary (WNUT-17, 52\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.
49	    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).
50	\end{enumerate}
51	
52	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4fec7e36-3bb2-4d6e-b776-2d5147678ca9",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "a4d9e21f-d82d-40c8-ac31-1e68ca658744",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/introduction.tex",
      "content": "\\section{Introduction}\\label{sec:introduction}\n\nSelf-consistency---sampling multiple outputs and aggregating them---has become a powerful strategy for improving language model reasoning.\nOn discrete-answer tasks such as arithmetic and commonsense QA, majority voting over chain-of-thought samples yields large gains: +18 percentage points on GSM8K (PaLM-540B; \\citealp{wang2023selfconsistency}).\nMore broadly, test-time compute scaling through repeated sampling and selection has emerged as a complementary axis to model scaling, offering substantial quality improvements at inference time \\cite{snell2024scaling, brown2024monkeys}.\nThese results rest on a shared assumption: that among $N$ stochastic samples, a selection mechanism can identify better outputs.\nFor tasks with a single correct answer, this assumption holds naturally---the majority vote is the selector.\nBut information extraction (IE) poses a fundamentally different challenge.\nThe output is not a single token or number; it is a \\textit{set} of entities or relations with internal dependencies, where two samples may extract overlapping but non-identical structures.\nThere is no obvious majority to vote on, partial agreement is the norm rather than the exception, and the space of valid outputs is combinatorially large.\nCan self-consistency still provide useful signal in this structured setting?\n\nPrior work on confidence estimation for LLM-based IE has conflated two distinct objectives: \\textit{quality estimation} (which inputs does the model handle reliably?) and \\textit{sample selection} (which of $N$ outputs is best?).\nThese require fundamentally different signal properties: the former benefits from instance-level aggregation, while the latter demands per-sample discrimination.\nSelf-consistency methods for discrete answers \\cite{wang2023selfconsistency, chen2024usc} and weighted variants \\cite{taubenfeld2025cisc, kang2025selfcertainty} assume outputs can be grouped by equivalence---an assumption that breaks for entity sets with partial overlap.\nThe most relevant study, \\citet{nedellec2026consistency}, examines consistency--accuracy correlations for LLM-based IE, finding results that our quality-estimation analysis corroborates.\nOur work extends theirs in three directions: (i)~structural matching beyond surface-level agreement, (ii)~testing whether quality estimation translates to best-of-$N$ selection (it does not), and (iii)~a difficulty gradient revealing non-obvious findings---WNUT-17 conditional correlations collapse to $\\rho{=}0.038$ (n.s.) and LP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$)---that would be invisible on a single dataset.\n\nStructured IE requires schema-compliant output, making constrained decoding \\cite{willard2023guided} the standard inference strategy---without it, a substantial fraction of outputs from general-purpose models are unparseable.\\footnote{Fine-tuned models may retain format compliance without grammar constraints: our free-form ablation achieves 99.95\\% valid JSON rate (\\S\\ref{sec:ablation}).}\nAll experiments use constrained decoding, the regime under which structured IE is practically deployed.\n\nOur central finding is the \\textbf{correlation-selection gap} (Figure~\\ref{fig:overview}): consistency-based signals achieve strong quality estimation ($\\rho$ up to 0.38, AUROC up to 0.75) but fail at sample selection despite 13--18~pp of oracle headroom.\nBy construction, four of five signals assign identical scores to all candidates from the same input, precluding per-sample discrimination.\nThe non-trivial questions are whether (a)~consensus-proximity selection---instantiating MBR decoding \\cite{eikema2022sampling, freitag2022high, muller2021understanding} with structural utility functions---can recover discrimination, and (b)~whether log-probability, the only per-sample signal, can exploit the headroom.\nBoth fail: MBR utility correlates with F1 across instances but not within them (\\S\\ref{sec:discussion}); log-probability scores are severely compressed (60\\% of instances effectively tied), though where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\nA controlled free-form decoding ablation confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding (\\S\\ref{sec:ablation}).\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_overview}\n\\caption{The correlation-selection gap. \\textbf{Left}: consistency signals predict instance-level quality---high agreement correlates with high F1. \\textbf{Right}: instance-level signals assign identical scores to all $N$ candidates, precluding sample selection. Consensus-proximity selection does not recover per-sample discrimination.}\n\\label{fig:overview}\n\\end{figure*}\n\nWe systematically compare five confidence signals from three families---structural (entity voting confidence [VC], Soft Jaccard [SJ]), surface (exact match [EM], Fleiss' $\\kappa$ [FK]), and model-internal (log-probability [LP])---across NER and RE on SciERC \\cite{luan2018scierc}, CoNLL-2003 \\cite{tjongkimsang2003conll}, and WNUT-17 \\cite{derczynski2017wnut}, using Qwen3-8B and LLaMA-3.1-8B.\nOur contributions are:\n\\begin{enumerate}\n    \\item \\textbf{The correlation-selection gap and its diagnosis.}\n    We demonstrate that strong quality estimation ($\\rho{=}0.38$, AUROC${=}0.75$) coexists with selection failure ($p{>}0.39$, 13--18~pp oracle headroom).\n    Log-probability---the only per-sample signal---fails due to score compression (60\\% of instances effectively tied); where compression is mitigated, it becomes a significant selector ($+2.9$~pp, $p{=}0.01$).\n    A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific.\n\n    \\item \\textbf{A systematic evaluation framework.}\n    We compare five confidence signals from three families---structural, surface, and model-internal---across quality estimation, binary discrimination, and sample selection, showing that these metrics decouple and single-metric evaluation risks selecting the wrong signal.\n\n    \\item \\textbf{Task-complexity boundary conditions.}\n    Signal rankings shift with task difficulty: EM leads on easy tasks, SJ on hard tasks---consistent across two model families at 8B scale, though with model-dependent magnitude.\n    At the capability boundary (WNUT-17, 52\\% zero F1), conditional correlations collapse to non-significance and LP exhibits strong negative correlation ($\\rho{=}{-}0.410$), indicating overconfidence on out-of-distribution inputs.\n    NER findings span three datasets; RE conclusions rest on SciERC alone (preliminary).\n\\end{enumerate}\n\n",
      "numLines": 52,
      "startLine": 1,
      "totalLines": 52
    }
  },
  "sourceToolAssistantUUID": "4fec7e36-3bb2-4d6e-b776-2d5147678ca9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool call

_source line 510 · 2026-05-15T11:48:50.655Z_

<details open><summary>🔧 Tool call — Read · `toolu_01GcibyL75c6rECgs5iKcU38`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a4d9e21f-d82d-40c8-ac31-1e68ca658744",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "312d0968-9615-4149-8e33-57b6ee9a779e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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

_source line 511 · 2026-05-15T11:48:50.660Z_

<details><summary>↩ Tool result · `toolu_01GcibyL75c6rECgs5iKcU38`</summary>

```text
1	\section{Discussion}\label{sec:discussion}
2	
3	\paragraph{Practical recommendations.}
4	For per-instance quality ranking, VC provides the strongest rank correlation ($\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).
5	Signal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.
6	When model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\ref{tab:wnut}).
7	
8	\paragraph{Why the gap exists: two layers.}
9	\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.
10	Consensus-proximity selection (\S\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\ref{tab:selection}).
11	\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.
12	LP scores are severely compressed: 60\% of instances have a within-sample range below 0.05, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$; Appendix~\ref{app:logprob_ties}).
13	In the 40\% of instances where compression is mitigated (LP range ${\geq}0.05$, $n{=}210$), LP \textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\rho$: 0.08$\to$0.39).
14	This diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.
15	A controlled ablation (\S\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.
16	Diversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\ref{app:calibration}) may compound this.
17	
18	\paragraph{Connection to MBR decoding.}
19	Our selection strategies instantiate minimum Bayes risk (MBR) decoding \cite{eikema2022sampling, muller2021understanding}: each selects $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.
20	Despite MBR's success in machine translation \cite{freitag2022high} and its extension to summarization, code generation, and captioning \cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.
21	\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.
22	
23	\paragraph{Score compression is task-inherent.}\label{sec:ablation}
24	A natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.
25	We test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\%, 4406/4408; Table~\ref{tab:freeform_ablation}).
26	LP variance is essentially unchanged (within-instance std ratio $0.97{\times}$, tied fraction 59.7\%$\to$57.7\%).
27	NER selection gains remain negligible ($+0.18$~pp free-form vs.\ $+0.59$~pp constrained).
28	This rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.
29	The correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.
30	Notably, the fine-tuned model achieved 99.95\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.
31	
32	\paragraph{What drives the universal gap?}
33	Our analysis reveals two complementary mechanisms.
34	First, the free-form ablation exposes a task-specific interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form), a reversal that is universal across all 7 relation types and driven by selective variance reallocation ($p{<}0.0001$).
35	The win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).
36	This interaction does not generalize to NER, where selection remains negligible under both regimes.
37	Second, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\times}$ increase in within-instance LP range for the newly non-tied subset.
38	Despite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.
39	Free-form decoding also slightly improves quality estimation (NER VC $\rho$: 0.379$\to$0.409), though this does not translate to selection gains.
40	
41	\paragraph{Methodological implications.}
42	The decoupling of quality estimation ($\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.
43	Effective selection likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.
44	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "312d0968-9615-4149-8e33-57b6ee9a779e",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "0a9c66bd-b243-46aa-b395-eccf28db7ccc",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/discussion.tex",
      "content": "\\section{Discussion}\\label{sec:discussion}\n\n\\paragraph{Practical recommendations.}\nFor per-instance quality ranking, VC provides the strongest rank correlation ($\\rho{=}0.38$), though EM leads binary discrimination (AUROC${=}0.749$); under conditional filtering, EM leads on both NER and RE ($\\rho{=}0.360$, $0.417$; RE: preliminary, single benchmark).\nSignal rankings depend on task difficulty---EM dominates easy tasks (CoNLL), VC and SJ dominate hard tasks (SciERC)---directionally consistent across tested model families, though with model-dependent magnitude.\nWhen model capability is insufficient (WNUT-17), all signals converge toward non-significant conditional correlations (Table~\\ref{tab:wnut}).\n\n\\paragraph{Why the gap exists: two layers.}\n\\textit{Layer 1 (definitional):} Four of five signals are instance-level aggregates that assign a single score per input; they cannot rank candidates by construction.\nConsensus-proximity selection (\\S\\ref{sec:evaluation}) does not recover per-sample discrimination (Table~\\ref{tab:selection}).\n\\textit{Layer 2 (score compression):} Log-probability, the only per-sample signal, also fails to exploit the 13--18~pp oracle headroom.\nLP scores are severely compressed: 60\\% of instances have a within-sample range below 0.05, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$; Appendix~\\ref{app:logprob_ties}).\nIn the 40\\% of instances where compression is mitigated (LP range ${\\geq}0.05$, $n{=}210$), LP \\textit{significantly} outperforms greedy ($+2.9$~pp, $p{=}0.01$; within-instance $\\rho$: 0.08$\\to$0.39).\nThis diagnostic confirms that LP carries useful per-sample quality information; score compression is the primary mechanistic bottleneck.\nA controlled ablation (\\S\\ref{sec:ablation}) confirms that this compression is intrinsic to the model and task, not an artifact of constrained decoding.\nDiversity-stratified analysis confirms the gap persists even among high-diversity instances (Appendix~\\ref{app:diversity}); RE miscalibration (ECE 0.109--0.339, preliminary; Appendix~\\ref{app:calibration}) may compound this.\n\n\\paragraph{Connection to MBR decoding.}\nOur selection strategies instantiate minimum Bayes risk (MBR) decoding \\cite{eikema2022sampling, muller2021understanding}: each selects $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} U(y_i, y_j)$ with utility $U$ defined by SJ, EM, or entity overlap.\nDespite MBR's success in machine translation \\cite{freitag2022high} and its extension to summarization, code generation, and captioning \\cite{jinnai2024mbr}, all variants fail here because the utility functions correlate with F1 at the instance level but not within a single instance---the mathematical essence of the correlation-selection gap.\n\\citet{eikema2025structured} study structure-conditional MBR decoding and find that standard utility functions degrade on structured outputs---consistent with our finding that consensus-proximity selection fails in IE despite its success in machine translation.\n\n\\paragraph{Score compression is task-inherent.}\\label{sec:ablation}\nA natural hypothesis is that LP compression is an artifact of constrained decoding's restricted token space.\nWe test this via controlled ablation: generating free-form (unconstrained) outputs on the same instances with post-hoc JSON parsing (parse rate 99.95\\%, 4406/4408; Table~\\ref{tab:freeform_ablation}).\nLP variance is essentially unchanged (within-instance std ratio $0.97{\\times}$, tied fraction 59.7\\%$\\to$57.7\\%).\nNER selection gains remain negligible ($+0.18$~pp free-form vs.\\ $+0.59$~pp constrained).\nThis rules out constrained decoding as the cause of compression and establishes LP compression as inherent to structured output generation.\nThe correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy.\nNotably, the fine-tuned model achieved 99.95\\% parse rate without grammar constraints, suggesting that constrained decoding's format-compliance role may be redundant for sufficiently fine-tuned models.\n\n\\paragraph{What drives the universal gap?}\nOur analysis reveals two complementary mechanisms.\nFirst, the free-form ablation exposes a task-specific interaction: RE LP selection flips from $-0.68$~pp (constrained) to $+1.69$~pp (free-form), a reversal that is universal across all 7 relation types and driven by selective variance reallocation ($p{<}0.0001$).\nThe win/loss ratio shifts from 36:59 (constrained) to 45:45 (free-form), with the gains concentrated on relation-dense instances (mean 3.3 gold relations).\nThis interaction does not generalize to NER, where selection remains negligible under both regimes.\nSecond, the non-tied subset ($n{=}210$) is partially reshuffled under free-form decoding: Jaccard similarity between the constrained and free-form non-tied sets is 0.472, indicating that 87 instances newly gain LP discrimination while others lose it, yielding a $3{\\times}$ increase in within-instance LP range for the newly non-tied subset.\nDespite this reshuffling, aggregate NER selection gains remain negligible---score compression is not a fixed property of specific instances but rather a pervasive regime that shifts across instances without producing net selection improvement.\nFree-form decoding also slightly improves quality estimation (NER VC $\\rho$: 0.379$\\to$0.409), though this does not translate to selection gains.\n\n\\paragraph{Methodological implications.}\nThe decoupling of quality estimation ($\\rho$), binary discrimination (AUROC), and sample selection (best-of-$N$ F1) means evaluating on a single metric risks selecting the wrong signal for the intended use case.\nEffective selection likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers, venktesh2025trust}; $N$-scaling analysis (Appendix~\\ref{app:additional}) shows $N{=}8$ captures most quality estimation benefit.\n",
      "numLines": 44,
      "startLine": 1,
      "totalLines": 44
    }
  },
  "sourceToolAssistantUUID": "312d0968-9615-4149-8e33-57b6ee9a779e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool call

_source line 512 · 2026-05-15T11:48:51.115Z_

<details open><summary>🔧 Tool call — Read · `toolu_01ENnP9yw1xACfKn7pQiEwzt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a9c66bd-b243-46aa-b395-eccf28db7ccc",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "3ee8a96a-9a06-4f2d-91b2-7db9fd327441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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

_source line 513 · 2026-05-15T11:48:51.121Z_

<details><summary>↩ Tool result · `toolu_01ENnP9yw1xACfKn7pQiEwzt`</summary>

```text
1	\section{Conclusion}\label{sec:conclusion}
2	
3	We demonstrate that consistency signals are effective quality estimators ($\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \textit{correlation-selection gap}.
4	By construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.
5	Where compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.
6	A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.
7	Signal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.
8	RE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.
9	Trained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.
10	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3ee8a96a-9a06-4f2d-91b2-7db9fd327441",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "1d270984-9449-49e4-a814-28515287318a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/conclusion.tex",
      "content": "\\section{Conclusion}\\label{sec:conclusion}\n\nWe demonstrate that consistency signals are effective quality estimators ($\\rho$ up to 0.38, AUROC up to 0.75) for LLM-based structured IE, but fail at sample selection---the \\textit{correlation-selection gap}.\nBy construction, four of five signals assign identical scores to all candidates from the same input; log-probability, the only per-sample signal, also fails ($p{>}0.39$) despite 13--18~pp oracle headroom due to score compression.\nWhere compression is mitigated, LP becomes a significant selector ($+2.9$~pp, $p{=}0.01$); consensus-proximity selection (MBR decoding) similarly fails as utility correlates with quality across instances but not within them.\nA controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.\nSignal rankings depend on task difficulty, with consistent ordering across two model families at 8B scale.\nRE findings rest on SciERC alone (preliminary, single benchmark) and warrant multi-benchmark validation.\nTrained verifiers, scaling to 70B+ models, and conformal prediction are promising directions for closing the gap.\n",
      "numLines": 10,
      "startLine": 1,
      "totalLines": 10
    }
  },
  "sourceToolAssistantUUID": "3ee8a96a-9a06-4f2d-91b2-7db9fd327441",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool call

_source line 514 · 2026-05-15T11:48:52.062Z_

<details open><summary>🔧 Tool call — Read · `toolu_01SCiHMbzCqhCn9BhurMiDvc`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d270984-9449-49e4-a814-28515287318a",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "c93adc0b-c7e2-4505-b64e-25ad3e57ebc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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

_source line 515 · 2026-05-15T11:48:52.067Z_

<details><summary>↩ Tool result · `toolu_01SCiHMbzCqhCn9BhurMiDvc`</summary>

```text
1	Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.
2	RE selection failure persists even when restricting to non-zero F1 instances (Appendix~\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.
3	WNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.
4	
5	We evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.
6	A 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.
7	Larger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.
8	
9	Our analysis of selection potential uses only unsupervised signals.
10	We do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.
11	
12	We evaluate at $N{=}8$ and $N{=}16$.
13	The behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.
14	
15	On CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\rho{=}0.431$ vs.\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.
16	Our free-form ablation (\S\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.
17	
18	Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking} active, injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.
19	At inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.
20	The empty blocks may weakly affect first-token probability distributions during training, but the absence of any reasoning content limits their representational impact; we do not expect this inconsistency to alter our quantitative conclusions.
21	
22	Finally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.
23	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c93adc0b-c7e2-4505-b64e-25ad3e57ebc9",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "6eaa3677-3524-4a5e-a5ef-910fb12e448e",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/limitations.tex",
      "content": "Our evaluation covers three datasets but only one RE benchmark (SciERC), where 40\\% of instances receive zero F1, compressing the discriminable range and limiting signal differentiation for relation extraction.\nRE selection failure persists even when restricting to non-zero F1 instances (Appendix~\\ref{app:re_conditional_selection}), ruling out floor effects as the sole explanation, but generalization to other RE benchmarks remains unvalidated.\nWNUT-17 confirms the capability boundary of our approach, but our positive results on formal-domain text (CoNLL, SciERC) have not been validated on informal or noisy text where models achieve non-trivial performance.\n\nWe evaluate two model families (Qwen3-8B and LLaMA-3.1-8B), both at 8B parameters.\nA 3-seed robustness analysis confirms that signal rankings are stable across seeds ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}), but whether our findings---particularly the correlation-selection gap and the difficulty-dependent signal ordering---hold for larger models (70B+) or closed-source APIs remains untested.\nLarger models may produce higher-quality and more diverse samples, potentially altering the signal landscape.\n\nOur analysis of selection potential uses only unsupervised signals.\nWe do not train a dedicated verifier or reward model, leaving unknown how much of the oracle headroom a supervised approach could recover.\n\nWe evaluate at $N{=}8$ and $N{=}16$.\nThe behavior of confidence signals at larger sample sizes (e.g., $N{=}64$ or $N{=}128$) is unknown, and $N$-scaling gains are setting-dependent: SJ improves by $+0.052$ on Qwen SciERC NER but only $+0.016$ on LLaMA SciERC NER when doubling from $N{=}8$ to $N{=}16$.\n\nOn CoNLL with LLaMA, the SJ--FK gap is only 0.003 ($\\rho{=}0.431$ vs.\\ $0.428$), so the structural advantage over surface signals may not generalize to all simple-schema datasets.\nOur free-form ablation (\\S\\ref{sec:ablation}) confirms that LP score compression persists without constrained decoding, but was conducted on a single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.\n\nQwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking} active, injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens, no reasoning chain) before each response; CoNLL and WNUT checkpoints disabled this feature.\nAt inference time, constrained decoding suppresses thinking tokens in all configurations, so they do not appear in generated samples.\nThe empty blocks may weakly affect first-token probability distributions during training, but the absence of any reasoning content limits their representational impact; we do not expect this inconsistency to alter our quantitative conclusions.\n\nFinally, log-probability was excluded from the temperature comparison ($T{=}0.7$ vs.\\ $T{=}1.0$) due to missing $T{=}0.7$ LP data, leaving its temperature sensitivity uncharacterized.\n",
      "numLines": 23,
      "startLine": 1,
      "totalLines": 23
    }
  },
  "sourceToolAssistantUUID": "c93adc0b-c7e2-4505-b64e-25ad3e57ebc9",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool call

_source line 516 · 2026-05-15T11:48:52.188Z_

<details open><summary>🔧 Tool call — Read · `toolu_019tq5V331KDnKRueop9UfJY`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6eaa3677-3524-4a5e-a5ef-910fb12e448e",
  "isSidechain": false,
  "requestId": "req_011Cb4JVdsYmbij5W4QBWJiz",
  "type": "assistant",
  "uuid": "517fb4b3-bb8c-4c2c-9f62-0462c7930a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DmQjMTUabuErtnLAsLmKaQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1880,
      "cache_read_input_tokens": 80244,
      "output_tokens": 500,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1880,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 500,
          "cache_read_input_tokens": 80244,
          "cache_creation_input_tokens": 1880,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1880
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


### Runtime record

_source line 517_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Paper Agent 触发审查]: ## D072 Framing Update Review Request  **变更范围**: D072 将论文从 \"regime-specific bottleneck under constrained decoding\" 改为 \"universal correlation-selection gap\"。主要受影响章节: title, abstract…",
  "leafUuid": "517fb4b3-bb8c-4c2c-9f62-0462c7930a31",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Runtime record

_source line 518_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker verification completion status",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Tool result

_source line 519 · 2026-05-15T11:48:52.606Z_

<details><summary>↩ Tool result · `toolu_019tq5V331KDnKRueop9UfJY`</summary>

```text
1	\section{Notation}\label{app:notation}
2	
3	Table~\ref{tab:notation} summarizes the notation used throughout the paper.
4	
5	\begin{table}[h]
6	\centering
7	\small
8	\begin{tabular}{cl}
9	\toprule
10	Symbol & Meaning \\
11	\midrule
12	$\mathcal{M}$ & Language model \\
13	$x$ & Input instance \\
14	$y_i$ & $i$-th stochastic sample \\
15	$N$ & Number of samples \\
16	$T$ & Sampling temperature \\
17	$c(\cdot)$ & Confidence signal \\
18	SJ & Soft Jaccard similarity \\
19	FK & Fleiss' $\kappa$ \\
20	EM & Exact-match voting rate \\
21	VC ($c_{\mathrm{vc}}$) & Entity voting confidence \\
22	LP ($c_{\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\
23	\bottomrule
24	\end{tabular}
25	\caption{Notation used throughout the paper.}
26	\label{tab:notation}
27	\end{table}
28	
29	\section{Robustness Analysis}\label{app:robustness}
30	
31	\begin{table}[t]
32	\centering
33	\small
34	\caption{Signal robustness across configurations (Spearman $\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\pm\sigma$). $^\dagger$Mean over 3 seeds ($\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}
35	\label{tab:robustness}
36	\begin{tabular}{llcc}
37	\toprule
38	& & NER $\rho$ & RE $\rho$ \\
39	\midrule
40	\multicolumn{4}{l}{\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\
41	\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\
42	\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\
43	\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\
44	\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\
45	\midrule
46	\multicolumn{4}{l}{\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\
47	\quad SJ & $N{=}8$  & 0.360 & 0.250 \\
48	\quad SJ & $N{=}16$ & 0.412$^\dagger$ & 0.281 \\
49	\quad FK & $N{=}8$  & 0.267 & 0.275 \\
50	\quad FK & $N{=}16$ & 0.280 & 0.279 \\
51	\midrule
52	\multicolumn{4}{l}{\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\
53	\quad SJ &  & $0.463{\pm}0.007$ & --- \\
54	\quad FK &  & $0.455{\pm}0.006$ & --- \\
55	\quad EM &  & $0.460{\pm}0.008$ & --- \\
56	\quad VC &  & $0.458{\pm}0.003$ & --- \\
57	\quad LP &  & $0.310{\pm}0.005$ & --- \\
58	\bottomrule
59	\end{tabular}
60	\end{table}
61	
62	\begin{figure}[t]
63	\centering
64	\includegraphics[width=\columnwidth]{fig_temperature_robustness}
65	\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}
66	\label{fig:temperature_robustness}
67	\end{figure}
68	
69	\paragraph{Temperature sensitivity.}
70	SJ NER $\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.
71	FK shows mixed behavior: NER $\rho$ drops by 0.054, while RE $\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.
72	Across all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\ 0.321 at $T{=}0.7$; 0.360 vs.\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.
73	
74	\paragraph{Sample size scaling.}
75	Increasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\rho$ rises from 0.360 to $0.412{\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.
76	The magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.
77	LLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\Delta\rho{\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\ref{tab:quality_estimation}).
78	FK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.
79	VC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\Delta{\leq}0.021$).
80	SJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.
81	
82	\paragraph{Transfer across model families.}
83	LLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\rho{=}0.325{\pm}0.021$, FK $\rho{=}0.256{\pm}0.024$).
84	On CoNLL, the gap across model families is minimal (Table~\ref{tab:quality_estimation}): SJ achieves $\rho{=}0.431$ (LLaMA) vs.\ 0.436 (Qwen), $\Delta{=}0.005$.
85	At $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\rho{=}0.411$ vs.\ LP 0.259, $\Delta{=}{+}0.152$), Qwen CoNLL (EM $\rho{=}0.463$ vs.\ LP 0.328, $\Delta{=}{+}0.135$), LLaMA SciERC (VC $\rho{=}0.452$ vs.\ LP 0.277, $\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\rho{=}0.463{\pm}0.007$ vs.\ LP $0.310{\pm}0.005$, $\Delta{=}{+}0.153$).
86	
87	\section{Calibration Analysis}\label{app:calibration}
88	
89	\begin{figure*}[t]
90	\centering
91	\includegraphics[width=\textwidth]{fig_reliability}
92	\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}
93	\label{fig:reliability}
94	\end{figure*}
95	
96	Reliability diagrams use 10 equal-width bins.
97	NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.
98	
99	\section{Additional Analyses}\label{app:additional}
100	
101	\paragraph{Per-relation diagnostic.}
102	RE signal degradation is relation-specific.
103	\textsc{Feature-Of} has near-zero correlation ($\rho{=}0.004$), while \textsc{Hyponym-Of} achieves $\rho{=}0.646$.
104	The primary bottleneck is entity span errors, which account for 55.5\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.
105	We note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.
106	
107	\paragraph{Capability stratification.}
108	For NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\rho{=}0.547$, compared to $\rho{=}0.415$ for 1--2 entities.
109	The SJ advantage over LP remains stable across sentence-length quartiles ($\Delta\rho{\approx}0.08$--$0.20$).
110	For RE, SJ $\rho$ increases monotonically with sentence length (Q1: 0.110 $\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.
111	Both proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.
112	For RE, entity count and relation count are strongly correlated ($\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.
113	On the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\rho{=}0.630$, LP $\rho{=}0.554$, and SJ $\rho{=}0.502$---all far above the full-set levels.
114	Richer relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.
115	
116	\paragraph{Length vs.\ log-probability.}
117	Figure~\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\rho{=}0.386$, $n{=}4{,}232$; RE: $\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \textit{higher}, not lower, token-averaged log-probability under constrained decoding.
118	
119	\begin{figure}[t]
120	\centering
121	\includegraphics[width=\columnwidth]{fig_length_logprob_scatter}
122	\caption{Output length vs.\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\rho{=}0.386$; RE: $\rho{=}0.326$) rule out length-penalty confounding.}
123	\label{fig:length_logprob_scatter}
124	\end{figure}
125	
126	\paragraph{Evaluation circularity and LOO-SJ equivalence.}
127	Consensus-proximity selection chooses $\hat{y} = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$.
128	Leave-one-out SJ (LOO-SJ) for sample $y_i$ is $\text{LOO-SJ}_i = \frac{1}{N-1}\sum_{j \neq i} \text{SJ}(y_i, y_j)$.
129	Since the $\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\arg\max_{y_i} \text{LOO-SJ}_i = \arg\max_{y_i} \sum_{j \neq i} \text{SJ}(y_i, y_j)$, making the two selection rules equivalent.
130	Standard (non-LOO) SJ adds the self-comparison term $\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.
131	Empirically, LOO-SJ yields $\Delta\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\times}10^{-4}$ (negligible at the individual prediction level).
132	Evaluation circularity is negligible.
133	
134	\paragraph{Conditional filtering details.}
135	On LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\rho{=}0.405$ while FK drops to $\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.
136	At $N{=}16$, the divergence persists: SJ maintains $\rho{=}0.308$ on conditional RE while LP drops to $\rho{=}{-}0.026$.
137	EM ranks first across all four tested conditional configurations---SciERC NER ($\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\rho{=}0.466$), CoNLL LLaMA 3-seed ($\rho{=}0.462$), and SciERC RE ($\rho{=}0.417$)---despite full-set rankings ranging from \#1 (CoNLL Qwen) to \#5 (SciERC RE).
138	On the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.
139	On the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.
140	The margin over SJ is largest on RE ($\Delta\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\Delta\rho{=}{+}0.002$), where all signals converge near $\rho{\approx}0.46$.
141	
142	\paragraph{WNUT-17 full signal analysis.}
143	Table~\ref{tab:wnut} reports all five signals on WNUT-17.
144	VC achieves $\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\rho{=}0.038$ ($p{=}0.49$).
145	LP shows the reverse pattern: full-set $\rho{=}{-}0.410$ but conditional $\rho{=}0.350$, the highest among all signals on the conditional set.
146	This inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.
147	
148	\begin{table}[t]
149	\centering
150	\small
151	\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\rho$; its conditional $\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}
152	\label{tab:wnut}
153	\begin{tabular}{lccccc}
154	\toprule
155	Signal & $\rho$ & $p$ & AUROC & Cond.\ $\rho$ & Cond.\ $p$ \\
156	\midrule
157	VC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\
158	FK      & .125 & .001 & .555 & .169 & .002 \\
159	SJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\
160	EM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\
161	LP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\
162	\bottomrule
163	\end{tabular}
164	\end{table}
165	
166	\paragraph{Cross-configuration selection analysis.}
167	Table~\ref{tab:cross_selection} extends the selection analysis to four additional configurations.
168	On LLaMA SciERC, where output diversity remains substantial (18\% identical outputs, 39\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\ref{tab:selection}).
169	On CoNLL, 57--88\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.
170	
171	\begin{table*}[t]
172	\centering
173	\small
174	\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}
175	\label{tab:cross_selection}
176	\begin{tabular}{llccccccc}
177	\toprule
178	Config & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\
179	\midrule
180	LLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \textbf{.652} & .633 \\
181	LLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \textbf{.649} & \textbf{.649} & .640 & .646 & .640 \\
182	Qwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \textbf{.899} & .893 & .898 & .897 & .895 \\
183	LLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \textbf{.925} & .924 & .924 & .923 \\
184	\bottomrule
185	\end{tabular}
186	\end{table*}
187	
188	\paragraph{Diminishing returns of $N$-scaling.}
189	Our $N{=}8$ and $N{=}16$ comparisons (Table~\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \cite{brown2024monkeys, snell2024scaling}.
190	For quality estimation, structural signals benefit consistently but sublinearly: SJ $\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\Delta\rho{\leq}0.021$).
191	Structural signals leverage $\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.
192	This asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\rho{=}0.431$ on LLaMA CoNLL (vs.\ LP $\rho{=}0.307$, $\Delta{=}{+}0.124$), and the gap \textit{widens} at $N{=}16$ ($\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.
193	For sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.
194	The practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.
195	
196	\section{Bootstrap CI for Signal Comparisons}\label{app:bootstrap_signal}
197	
198	Table~\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\rho$ and pairwise $\Delta\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).
199	The SJ--LP gap ($\Delta\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \S\ref{sec:qe_results}.
200	The VC--SJ gap ($\Delta\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.
201	The SJ--EM gap ($\Delta\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.
202	
203	\begin{table}[t]
204	\centering
205	\small
206	\caption{Bootstrap 95\% CIs for signal $\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\Delta\rho$; ``Sig.'' indicates whether the 95\% CI excludes zero.}
207	\label{tab:bootstrap_signal_ci}
208	\begin{tabular}{lcc}
209	\toprule
210	Signal & $\rho$ & 95\% CI \\
211	\midrule
212	VC & +0.379 & [+0.299, +0.456] \\
213	SJ & +0.360 & [+0.277, +0.437] \\
214	EM & +0.295 & [+0.212, +0.371] \\
215	FK & +0.267 & [+0.176, +0.354] \\
216	LP & +0.205 & [+0.119, +0.291] \\
217	\bottomrule
218	\end{tabular}
219	
220	\vspace{0.5em}
221	
222	\begin{tabular}{lccc}
223	\toprule
224	Comparison & $\Delta\rho$ & 95\% CI & Sig. \\
225	\midrule
226	SJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\
227	VC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\
228	SJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\dagger$ \\
229	\bottomrule
230	\end{tabular}
231	
232	\smallskip
233	{\footnotesize $^\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\alpha_{\text{adj}}{=}0.005$).}
234	\end{table}
235	
236	\section{Diversity and Selection Analysis}\label{app:diversity}
237	
238	\paragraph{Output diversity quantification.}
239	Table~\ref{tab:diversity} summarizes output diversity across configurations.
240	On SciERC, output diversity is substantial: Qwen produces 43\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.
241	LLaMA shows similar diversity (39\% unique, F1 std 0.11).
242	On CoNLL, diversity collapses: 57\% (Qwen) to 88\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.
243	WNUT-17 shows 55\% identical outputs, driven by the 52\% zero-F1 rate.
244	
245	\begin{table}[t]
246	\centering
247	\small
248	\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}
249	\label{tab:diversity}
250	\begin{tabular}{lcc}
251	\toprule
252	Config & Identical & Unique \\
253	\midrule
254	Qwen/SciERC & 11\% & 43\% \\
255	LLaMA/SciERC & 18\% & 39\% \\
256	Qwen/CoNLL & 57\% & --- \\
257	LLaMA/CoNLL & 88\% & --- \\
258	WNUT-17 & 55\% & --- \\
259	\bottomrule
260	\end{tabular}
261	\end{table}
262	
263	\paragraph{Oracle-improvable fraction.}
264	Across SciERC configurations, 39--42\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\% (164/397, $+$45.3~pp), LLaMA NER 39.3\% (208/529, $+$33.7~pp).
265	On CoNLL, only 4--9\% of instances are improvable, confirming the ceiling effect.
266	
267	\paragraph{Diversity-stratified selection gap.}
268	On the 44\% of Qwen SciERC instances with high diversity (${\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.
269	LLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.
270	This rules out insufficient diversity as an explanation for the correlation-selection gap.
271	
272	\paragraph{TOST equivalence testing.}
273	The primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\% CI [$-$3.0, $+$4.2]~pp spanning zero.
274	Table~\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\delta$.
275	The $\delta$ values are anchored to oracle headroom (13--18~pp): $\delta{=}5$~pp corresponds to forgoing 28--38\% of the available headroom, $\delta{=}3$~pp forgoing 17--23\%, and $\delta{=}2$~pp less than 15\%.
276	The breakpoint $\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\sim}$10\% of oracle headroom) to 3.4~pp (FK, ${\sim}$26\%) on NER, and from approximately 2.9~pp (LP, ${\sim}$16\%) to 6.5~pp (VC, ${\sim}$36\%) on RE.
277	On NER ($n{=}529$), at $\delta{=}{\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\delta{=}{\pm}3$~pp, four of five signals pass; at $\delta{=}{\pm}5$~pp, all five pass.
278	On RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\delta{=}{\pm}5$~pp due to systematic underperformance ($\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).
279	The effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.
280	
281	\begin{table}[t]
282	\centering
283	\small
284	\caption{TOST equivalence testing: signals vs.\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \checkmark: equivalent at $p{<}0.05$; \texttimes: not equivalent. $\Delta$: mean F1 difference (signal $-$ greedy).}
285	\label{tab:tost}
286	\begin{tabular}{l cccc cccc}
287	\toprule
288	& \multicolumn{4}{c}{\textbf{NER}} & \multicolumn{4}{c}{\textbf{RE}} \\
289	\cmidrule(lr){2-5} \cmidrule(lr){6-9}
290	Signal & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 & $\Delta$ & $\pm$2 & $\pm$3 & $\pm$5 \\
291	\midrule
292	LP & +0.6 & \checkmark & \checkmark & \checkmark & $-$0.9 & \texttimes & \checkmark & \checkmark \\
293	SJ & +0.1 & \checkmark & \checkmark & \checkmark & $-$1.8 & \texttimes & \texttimes & \checkmark \\
294	FK & $-$0.5 & \texttimes & \checkmark & \checkmark & $-$1.6 & \texttimes & \texttimes & \checkmark \\
295	EM & $-$0.8 & \texttimes & \checkmark & \checkmark & $-$3.2 & \texttimes & \texttimes & \texttimes \\
296	VC & $-$1.0 & \texttimes & \texttimes & \checkmark & $-$4.5 & \texttimes & \texttimes & \texttimes \\
297	\bottomrule
298	\end{tabular}
299	\end{table}
300	
301	\section{Multi-Seed Stability}\label{app:multiseed}
302	
303	Table~\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).
304	On NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\sigma{\leq}0.025$ for all signals.
305	On RE (Qwen only, preliminary), VC remains the top signal ($\rho{=}0.309{\pm}0.024$), but LP rises to \#2 ($\rho{=}0.297{\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.
306	LLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.
307	
308	\begin{table}[t]
309	\centering
310	\small
311	\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\sigma{\leq}0.025$).}
312	\label{tab:multiseed}
313	\begin{tabular}{lccccc}
314	\toprule
315	& LP & FK & SJ & VC & EM \\
316	\midrule
317	\multicolumn{6}{l}{\textit{NER Spearman $\rho$ (mean $\pm\sigma$)}} \\
318	Qwen & .217${\pm}$.013 & .254${\pm}$.016 & .364${\pm}$.018 & .386${\pm}$.019 & .307${\pm}$.008 \\
319	LLaMA & .162${\pm}$.025 & .256${\pm}$.024 & .325${\pm}$.021 & .384${\pm}$.014 & .279${\pm}$.011 \\
320	\midrule
321	\multicolumn{6}{l}{\textit{RE Spearman $\rho$ (mean $\pm\sigma$, Qwen)}} \\
322	Qwen & .297${\pm}$.022 & .290${\pm}$.012 & .249${\pm}$.002 & .309${\pm}$.024 & .135${\pm}$.016 \\
323	\midrule
324	\multicolumn{6}{l}{\textit{NER AUROC (mean $\pm\sigma$)}} \\
325	Qwen & .613${\pm}$.002 & .618${\pm}$.009 & .684${\pm}$.009 & .697${\pm}$.010 & .661${\pm}$.010 \\
326	LLaMA & .577${\pm}$.007 & .616${\pm}$.011 & .655${\pm}$.010 & .689${\pm}$.005 & .636${\pm}$.006 \\
327	\bottomrule
328	\end{tabular}
329	\end{table}
330	
331	\section{Training Configuration}\label{app:training}
332	
333	Both models are fine-tuned with identical hyperparameters (Table~\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.
334	
335	\begin{table}[t]
336	\centering
337	\small
338	\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}
339	\label{tab:training}
340	\begin{tabular}{ll}
341	\toprule
342	Parameter & Value \\
343	\midrule
344	LoRA rank / $\alpha$ & 32 / 64 \\
345	LoRA target & All linear modules \\
346	LoRA dropout & 0 \\
347	Optimizer & AdamW \\
348	Learning rate & 2e-4, cosine schedule \\
349	Warmup ratio & 0.1 \\
350	Effective batch size & 16 (2 $\times$ grad.\ accum.\ 8) \\
351	Epochs & 5 \\
352	Max sequence length & 2048 \\
353	Precision & bf16 \\
354	Gradient checkpointing & Enabled \\
355	Max gradient norm & 1.0 \\
356	Training seed & 42 \\
357	Framework & LLaMA Factory \\
358	\midrule
359	\multicolumn{2}{l}{\textit{Dataset-specific}} \\
360	SciERC split & 1861 / 275 / 551 \\
361	CoNLL / WNUT & +\,load\_best\_model\_at\_end, \\
362	& eval\_steps${=}$200, save\_limit${=}$5 \\
363	\bottomrule
364	\end{tabular}
365	\end{table}
366	
367	\paragraph{Prompt template.}
368	For NER, we use a structured prompt:
369	\begin{quote}
370	\small
371	\texttt{System:} You are an expert in Named Entity Recognition.\\
372	\texttt{User:} Extract all named entities from the following text. Output as JSON.\\
373	Text: \texttt{\{input\_text\}}\\
374	Entity types: \texttt{\{schema\_types\}}
375	\end{quote}
376	RE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.
377	
378	\paragraph{Constrained decoding.}
379	Inference uses vLLM with XGrammar-based JSON schema enforcement \cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.
380	This eliminates format errors but may compress per-sample diversity by restricting the output space.\footnote{SciERC training used \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \texttt{enable\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \S\ref{sec:setup} and Limitations for discussion of this confound.}
381	
382	\section{Log-Probability Score Compression}\label{app:logprob_ties}
383	
384	Under constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\ref{tab:logprob_ties}).
385	The median within-instance LP range is only 0.041, and 75\% of pairwise comparisons are effective ties ($|\Delta|{<}0.026$).
386	At $\varepsilon{=}0.05$, 60.3\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.
387	For comparison, SJ has only 12.5\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.
388	
389	\begin{table}[t]
390	\centering
391	\small
392	\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\varepsilon$.}
393	\label{tab:logprob_ties}
394	\begin{tabular}{lc}
395	\toprule
396	$\varepsilon$ threshold & Tied instances (\%) \\
397	\midrule
398	0.01 & 1.1\% \\
399	0.05 & 60.3\% \\
400	0.1  & ${\sim}$84\% \\
401	0.5  & ${\sim}$99\% \\
402	\bottomrule
403	\end{tabular}
404	\end{table}
405	
406	\paragraph{Non-tied subset.}
407	Among instances with LP range ${\geq}0.05$ ($n{=}210$, 40\% of total), log-probability selection \textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\rho(\text{LP}, \text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).
408	This confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.
409	A free-form decoding ablation (Appendix~\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.
410	
411	\section{RE Conditional Selection}\label{app:re_conditional_selection}
412	
413	Table~\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.
414	Of $n{=}397$ RE instances, 238 (60\%) have non-zero F1 and 159 (40\%) have zero F1.
415	All five signals underperform greedy on both subsets.
416	On the non-zero subset, selection performance is \textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.
417	Oracle headroom exists (0.757 vs.\ 0.674) but no signal exploits it, ruling out the 40\% zero-F1 floor effect as the explanation for RE selection failure.
418	
419	\begin{table}[t]
420	\centering
421	\small
422	\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}
423	\label{tab:re_cond_selection}
424	\begin{tabular}{lcc}
425	\toprule
426	Method & Full ($n{=}397$) & Non-zero ($n{=}238$) \\
427	\midrule
428	Oracle & 0.585 & 0.757 \\
429	\midrule
430	LP & 0.395 & 0.600 \\
431	SJ & 0.386 & 0.604 \\
432	EM & 0.372 & 0.583 \\
433	VC & 0.359 & 0.574 \\
434	\midrule
435	Greedy & 0.404 & 0.674 \\
436	\bottomrule
437	\end{tabular}
438	\end{table}
439	
440	\section{Free-Form Decoding Ablation}\label{app:freeform_ablation}
441	
442	Table~\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).
443	Free-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\%, 4406/4408).
444	LP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\times}$), and NER selection gains remain negligible under both regimes (Panel~B).
445	RE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\ $-0.68$~pp constrained).
446	Quality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).
447	
448	\begin{table*}[t]
449	\centering
450	\caption{Comparison of constrained vs.\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}
451	\label{tab:freeform_ablation}
452	
453	\vspace{2pt}
454	{\small\textsc{Panel A: Logprob Distribution}}
455	\vspace{2pt}
456	
457	\begin{tabular}{lccc}
458	\toprule
459	Metric & Constrained & Free-form & $\Delta$ \\
460	\midrule
461	Mean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\
462	Mean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\
463	Tied fraction ($\varepsilon{=}0.05$) & 59.7\% & 57.7\% & $-$2.0\,pp \\
464	\bottomrule
465	\end{tabular}
466	
467	\vspace{8pt}
468	
469	{\small\textsc{Panel B: Selection F1}}
470	\vspace{2pt}
471	
472	\begin{tabular}{llccc}
473	\toprule
474	Task & Method & Constrained & Free-form & $\Delta$ \\
475	\midrule
476	\multirow{3}{*}{NER}
477	  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\
478	  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\
479	  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\
480	\midrule
481	\multirow{3}{*}{RE}
482	  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\
483	  & LP-selected   & 0.2845 & 0.3050 & \textbf{$+$0.0205} \\
484	  & Selection gap & $-$0.0068 & $+$0.0169 & \textbf{$+$0.0237} \\
485	\bottomrule
486	\end{tabular}
487	
488	\vspace{8pt}
489	
490	{\small\textsc{Panel C: QE Signal Quality (Spearman $\rho$)}}
491	\vspace{2pt}
492	
493	\begin{tabular}{l ccc ccc}
494	\toprule
495	 & \multicolumn{3}{c}{NER ($n{=}529$)} & \multicolumn{3}{c}{RE ($n{=}397$)} \\
496	\cmidrule(lr){2-4} \cmidrule(lr){5-7}
497	Signal & Constr. & Free & $\Delta$ & Constr. & Free & $\Delta$ \\
498	\midrule
499	SJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\
500	FK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\
501	LP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\
502	EM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\
503	VC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\
504	\bottomrule
505	\end{tabular}
506	
507	\vspace{8pt}
508	
509	{\small\textsc{Panel D: Parse Rate (Free-form)}}
510	\vspace{2pt}
511	
512	\begin{tabular}{lc}
513	\toprule
514	Metric & Value \\
515	\midrule
516	Total samples          & 4408 \\
517	Parse rate             & 99.95\% \\
518	Instances 8/8 valid    & 549\,/\,551 (99.6\%) \\
519	\bottomrule
520	\end{tabular}
521	
522	\end{table*}
523	
524	\section{LP Selection Failure Stability}\label{app:lp_failure_stability}
525	
526	We analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.
527	
528	\paragraph{Pairwise overlap.}
529	LP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.
530	The 3-way intersection contains 34 instances (27.9\% of any-seed failures), confirming a stable failure core.
531	
532	\paragraph{Instance complexity drives failure.}
533	Table~\ref{tab:stable_failures} stratifies instances by failure stability.
534	Stable failures (all 3 seeds) involve more gold relations (2.12 vs.\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.
535	Failure rate increases monotonically with gold relation count: 4.3\% at 1 relation, 20.7\% at 3 relations, 26.2\% at 6 relations.
536	
537	\begin{table}[t]
538	\centering
539	\small
540	\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}
541	\label{tab:stable_failures}
542	\begin{tabular}{lcccc}
543	\toprule
544	Group & $n$ & Gold rels & Greedy F1 & LP $\Delta$F1 \\
545	\midrule
546	Stable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\
547	Fail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\
548	Fail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\
549	Never fail & 429 & 1.62 & 0.429 & $+$0.041 \\
550	\bottomrule
551	\end{tabular}
552	\end{table}
553	
554	\paragraph{Flip instances.}
555	Only 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).
556	These instances show large constrained LP errors ($\Delta{=}{-}0.430$) that reverse under free-form decoding ($\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.
557	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "517fb4b3-bb8c-4c2c-9f62-0462c7930a31",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "5b682fb9-a93b-42f2-9c5d-7174d882d61d",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/appendix.tex",
      "content": "\\section{Notation}\\label{app:notation}\n\nTable~\\ref{tab:notation} summarizes the notation used throughout the paper.\n\n\\begin{table}[h]\n\\centering\n\\small\n\\begin{tabular}{cl}\n\\toprule\nSymbol & Meaning \\\\\n\\midrule\n$\\mathcal{M}$ & Language model \\\\\n$x$ & Input instance \\\\\n$y_i$ & $i$-th stochastic sample \\\\\n$N$ & Number of samples \\\\\n$T$ & Sampling temperature \\\\\n$c(\\cdot)$ & Confidence signal \\\\\nSJ & Soft Jaccard similarity \\\\\nFK & Fleiss' $\\kappa$ \\\\\nEM & Exact-match voting rate \\\\\nVC ($c_{\\mathrm{vc}}$) & Entity voting confidence \\\\\nLP ($c_{\\mathrm{lp}}$) & Log-probability (mean token log-likelihood) \\\\\n\\bottomrule\n\\end{tabular}\n\\caption{Notation used throughout the paper.}\n\\label{tab:notation}\n\\end{table}\n\n\\section{Robustness Analysis}\\label{app:robustness}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Signal robustness across configurations (Spearman $\\rho$). Top: temperature on Qwen SciERC. Middle: sample size on Qwen SciERC. Bottom: transfer across model families (both 8B) (LLaMA CoNLL $N{=}16$, 3-seed mean $\\pm\\sigma$). $^\\dagger$Mean over 3 seeds ($\\sigma{=}0.025$; individual: 0.428, 0.424, 0.384).}\n\\label{tab:robustness}\n\\begin{tabular}{llcc}\n\\toprule\n& & NER $\\rho$ & RE $\\rho$ \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Temperature} (Qwen SciERC, $N{=}8$)} \\\\\n\\quad SJ & $T{=}0.7$ & 0.388 & 0.234 \\\\\n\\quad SJ & $T{=}1.0$ & 0.360 & 0.250 \\\\\n\\quad FK & $T{=}0.7$ & 0.321 & 0.184 \\\\\n\\quad FK & $T{=}1.0$ & 0.267 & 0.275 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Sample size} (Qwen SciERC, $T{=}1.0$)} \\\\\n\\quad SJ & $N{=}8$  & 0.360 & 0.250 \\\\\n\\quad SJ & $N{=}16$ & 0.412$^\\dagger$ & 0.281 \\\\\n\\quad FK & $N{=}8$  & 0.267 & 0.275 \\\\\n\\quad FK & $N{=}16$ & 0.280 & 0.279 \\\\\n\\midrule\n\\multicolumn{4}{l}{\\textit{Across model families} (LLaMA CoNLL, $N{=}16$, 3 seeds)} \\\\\n\\quad SJ &  & $0.463{\\pm}0.007$ & --- \\\\\n\\quad FK &  & $0.455{\\pm}0.006$ & --- \\\\\n\\quad EM &  & $0.460{\\pm}0.008$ & --- \\\\\n\\quad VC &  & $0.458{\\pm}0.003$ & --- \\\\\n\\quad LP &  & $0.310{\\pm}0.005$ & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_temperature_robustness}\n\\caption{Temperature robustness on SciERC ($N{=}8$). Top: NER; bottom: RE. SJ maintains stable $\\rho$ across $T{=}0.7$ and $T{=}1.0$, while FK shows mixed sensitivity. LP $T{=}0.7$ data unavailable.}\n\\label{fig:temperature_robustness}\n\\end{figure}\n\n\\paragraph{Temperature sensitivity.}\nSJ NER $\\rho$ shifts from 0.388 ($T{=}0.7$) to 0.360 ($T{=}1.0$), a difference of 0.028 whose bootstrap confidence interval includes zero.\nFK shows mixed behavior: NER $\\rho$ drops by 0.054, while RE $\\rho$ increases by 0.091, likely reflecting reduced diversity at lower temperature interacting differently across tasks.\nAcross all comparisons, the SJ--FK relative ordering is preserved at both temperatures on NER (0.388 vs.\\ 0.321 at $T{=}0.7$; 0.360 vs.\\ 0.267 at $T{=}1.0$), indicating a stable signal hierarchy despite numerically small temperature effects.\n\n\\paragraph{Sample size scaling.}\nIncreasing from $N{=}8$ to $N{=}16$ improves SJ on Qwen SciERC NER: $\\rho$ rises from 0.360 to $0.412{\\pm}0.025$ (three seeds: 0.428, 0.424, 0.384), a gain of $+0.052$.\nThe magnitude of $N$-scaling gains is setting-dependent---LLaMA SciERC NER yields $+0.016$ and Qwen CoNLL NER $+0.014$---though the direction is consistently positive.\nLLaMA CoNLL exhibits the most uniform scaling: all four consistency signals gain $\\Delta\\rho{\\approx}{+}0.030$ (range: $+0.027$ to $+0.032$) while LP gains only $+0.003$ (Table~\\ref{tab:quality_estimation}).\nFK $N$-scaling is inconsistent: degradation on SciERC ($-0.007$ to $-0.019$) but improvement on CoNLL with LLaMA ($+0.027$), suggesting sensitivity to both model and task characteristics.\nVC $N$-scaling is consistently positive ($+0.005$ on Qwen CoNLL, $+0.018$ on LLaMA SciERC, $+0.062$ on Qwen SciERC), while LP is approximately $N$-invariant ($\\Delta{\\leq}0.021$).\nSJ, EM, and VC scale consistently across all tested settings; only FK shows setting-dependent variation, suggesting that structural and binary-agreement signals are the most robust to $N$.\n\n\\paragraph{Transfer across model families.}\nLLaMA-3.1-8B-Instruct replicates the structural-over-surface ordering on SciERC NER (SJ $\\rho{=}0.325{\\pm}0.021$, FK $\\rho{=}0.256{\\pm}0.024$).\nOn CoNLL, the gap across model families is minimal (Table~\\ref{tab:quality_estimation}): SJ achieves $\\rho{=}0.431$ (LLaMA) vs.\\ 0.436 (Qwen), $\\Delta{=}0.005$.\nAt $N{=}16$, the structural-over-LP advantage holds across all four tested settings: Qwen SciERC (VC $\\rho{=}0.411$ vs.\\ LP 0.259, $\\Delta{=}{+}0.152$), Qwen CoNLL (EM $\\rho{=}0.463$ vs.\\ LP 0.328, $\\Delta{=}{+}0.135$), LLaMA SciERC (VC $\\rho{=}0.452$ vs.\\ LP 0.277, $\\Delta{=}{+}0.175$), and LLaMA CoNLL 3-seed (SJ $\\rho{=}0.463{\\pm}0.007$ vs.\\ LP $0.310{\\pm}0.005$, $\\Delta{=}{+}0.153$).\n\n\\section{Calibration Analysis}\\label{app:calibration}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_reliability}\n\\caption{Reliability diagrams on SciERC ($N{=}8$, $T{=}1.0$). Top: mean F1 vs.\\ binned confidence; bottom: instance counts per bin. Left: NER; right: RE. NER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE shows greater miscalibration (ECE 0.109--0.339), reflecting the difficulty of calibrating confidence for compound extraction tasks.}\n\\label{fig:reliability}\n\\end{figure*}\n\nReliability diagrams use 10 equal-width bins.\nNER signals are reasonably well-calibrated (calibration ECE 0.069--0.096), while RE exhibits greater miscalibration (ECE 0.109--0.339), indicating that translating consistency scores into calibrated confidence estimates is feasible for NER but remains challenging for compound extraction tasks.\n\n\\section{Additional Analyses}\\label{app:additional}\n\n\\paragraph{Per-relation diagnostic.}\nRE signal degradation is relation-specific.\n\\textsc{Feature-Of} has near-zero correlation ($\\rho{=}0.004$), while \\textsc{Hyponym-Of} achieves $\\rho{=}0.646$.\nThe primary bottleneck is entity span errors, which account for 55.5\\% of RE false negatives---a prerequisite failure that consistency signals cannot detect, as they measure agreement among equally incorrect extractions.\nWe note that RE analysis relies on a single dataset (SciERC); generalization to other RE benchmarks remains to be validated.\n\n\\paragraph{Capability stratification.}\nFor NER, SJ effectiveness scales with structural complexity: on SciERC instances with 6+ entities, $\\rho{=}0.547$, compared to $\\rho{=}0.415$ for 1--2 entities.\nThe SJ advantage over LP remains stable across sentence-length quartiles ($\\Delta\\rho{\\approx}0.08$--$0.20$).\nFor RE, SJ $\\rho$ increases monotonically with sentence length (Q1: 0.110 $\\to$ Q4: 0.473; Fisher $z$-test $p{=}0.004$), indicating that longer, more relation-dense sentences provide richer structure for consistency-based estimation.\nBoth proxies are weakly correlated with F1 ($|r|{<}0.15$), confirming they capture input complexity rather than directly predicting output quality; however, entity count and sentence length are themselves moderately correlated ($\\rho{=}0.650$), so they reflect overlapping rather than independent complexity dimensions.\nFor RE, entity count and relation count are strongly correlated ($\\rho{=}0.769$) and thus reflect a single structural complexity dimension rather than independent axes.\nOn the high-complexity RE subset ($n{=}81$, high relation count), signals improve substantially: VC reaches $\\rho{=}0.630$, LP $\\rho{=}0.554$, and SJ $\\rho{=}0.502$---all far above the full-set levels.\nRicher relational structure provides more signal for consistency-based estimation, complementing the task-level boundary established by WNUT-17: structural signals are most effective within a ``sweet spot'' of sufficient model capability and sufficient output complexity.\n\n\\paragraph{Length vs.\\ log-probability.}\nFigure~\\ref{fig:length_logprob_scatter} shows that mean log-probability is weakly positively correlated with output length (NER: $\\rho{=}0.386$, $n{=}4{,}232$; RE: $\\rho{=}0.326$, $n{=}3{,}176$), ruling out length-penalty confounding as an explanation for LP's selection failure: longer outputs receive \\textit{higher}, not lower, token-averaged log-probability under constrained decoding.\n\n\\begin{figure}[t]\n\\centering\n\\includegraphics[width=\\columnwidth]{fig_length_logprob_scatter}\n\\caption{Output length vs.\\ mean log-probability on SciERC ($N{=}8$, $T{=}1.0$). Positive correlations (NER: $\\rho{=}0.386$; RE: $\\rho{=}0.326$) rule out length-penalty confounding.}\n\\label{fig:length_logprob_scatter}\n\\end{figure}\n\n\\paragraph{Evaluation circularity and LOO-SJ equivalence.}\nConsensus-proximity selection chooses $\\hat{y} = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nLeave-one-out SJ (LOO-SJ) for sample $y_i$ is $\\text{LOO-SJ}_i = \\frac{1}{N-1}\\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$.\nSince the $\\frac{1}{N-1}$ constant is shared across all candidates within an instance, $\\arg\\max_{y_i} \\text{LOO-SJ}_i = \\arg\\max_{y_i} \\sum_{j \\neq i} \\text{SJ}(y_i, y_j)$, making the two selection rules equivalent.\nStandard (non-LOO) SJ adds the self-comparison term $\\text{SJ}(y_i, y_i) = 1$ to each candidate, which is constant and thus does not affect ranking.\nEmpirically, LOO-SJ yields $\\Delta\\rho{=}{-}0.014$ relative to standard SJ (a correlation-level difference), with a maximum per-instance score difference of $3.1{\\times}10^{-4}$ (negligible at the individual prediction level).\nEvaluation circularity is negligible.\n\n\\paragraph{Conditional filtering details.}\nOn LLaMA conditional RE (non-zero F1 instances), SJ recovers to $\\rho{=}0.405$ while FK drops to $\\rho{=}0.259$, confirming that structural advantage is robust across both models and evaluation conditions.\nAt $N{=}16$, the divergence persists: SJ maintains $\\rho{=}0.308$ on conditional RE while LP drops to $\\rho{=}{-}0.026$.\nEM ranks first across all four tested conditional configurations---SciERC NER ($\\rho{=}0.360$), CoNLL Qwen $N{=}16$ ($\\rho{=}0.466$), CoNLL LLaMA 3-seed ($\\rho{=}0.462$), and SciERC RE ($\\rho{=}0.417$)---despite full-set rankings ranging from \\#1 (CoNLL Qwen) to \\#5 (SciERC RE).\nOn the full set, EM is diluted by trivial agreement: instances where all $N$ samples produce identical (possibly incorrect) outputs receive EM${=}1$ regardless of quality, compressing the signal's dynamic range.\nOn the conditional set---where the model demonstrably produces varied outputs---exact agreement becomes the strongest quality signal.\nThe margin over SJ is largest on RE ($\\Delta\\rho{=}{+}0.171$), where compound extraction decisions amplify output variability, and smallest on CoNLL LLaMA ($\\Delta\\rho{=}{+}0.002$), where all signals converge near $\\rho{\\approx}0.46$.\n\n\\paragraph{WNUT-17 full signal analysis.}\nTable~\\ref{tab:wnut} reports all five signals on WNUT-17.\nVC achieves $\\rho{=}0.724$ (AUROC${=}0.913$) on the full set, but conditional analysis (non-zero F1 instances) reveals this is entirely driven by the zero/non-zero boundary: conditional $\\rho{=}0.038$ ($p{=}0.49$).\nLP shows the reverse pattern: full-set $\\rho{=}{-}0.410$ but conditional $\\rho{=}0.350$, the highest among all signals on the conditional set.\nThis inversion confirms that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Quality estimation on WNUT-17 (Qwen, $N{=}8$, $T{=}1.0$, $n{=}689$ after filtering gold-empty instances). Cond: non-zero F1 instances ($n{=}334$). LP exhibits strong negative full-set $\\rho$; its conditional $\\rho$ reverses to the highest among all signals, confirming that full-set correlations on high-failure-rate datasets conflate binary success prediction with quality gradation.}\n\\label{tab:wnut}\n\\begin{tabular}{lccccc}\n\\toprule\nSignal & $\\rho$ & $p$ & AUROC & Cond.\\ $\\rho$ & Cond.\\ $p$ \\\\\n\\midrule\nVC      & .724 & ${<}$1e-112 & .913 & .038 & .487 \\\\\nFK      & .125 & .001 & .555 & .169 & .002 \\\\\nSJ      & .089 & .020 & .517 & .288 & ${<}$1e-7 \\\\\nEM      & .050 & .194 & .487 & .333 & ${<}$1e-9 \\\\\nLP & $-$.410 & ${<}$1e-28 & .219 & .350 & ${<}$1e-10 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Cross-configuration selection analysis.}\nTable~\\ref{tab:cross_selection} extends the selection analysis to four additional configurations.\nOn LLaMA SciERC, where output diversity remains substantial (18\\% identical outputs, 39\\% unique), LP achieves the highest selection F1 (0.652) at $N{=}8$ but still falls within bootstrap noise of greedy (0.646), replicating the gap observed on Qwen SciERC (Table~\\ref{tab:selection}).\nOn CoNLL, 57--88\\% of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect (greedy F1 ${\\approx}$0.91--0.92) rather than signal failure; selection analysis on these configurations is uninformative because there is little per-sample variance for any signal to exploit.\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 across configurations ($T{=}1.0$). SJ: Soft Jaccard, FK: Fleiss' $\\kappa$, EM: Exact Match, LP: Log-prob, VC: Voting Confidence. Best non-oracle signal per row in \\textbf{bold}. No signal significantly outperforms greedy in any configuration; CoNLL shows especially tight clustering where greedy already exceeds 0.90.}\n\\label{tab:cross_selection}\n\\begin{tabular}{llccccccc}\n\\toprule\nConfig & $n$ & Greedy & Oracle & SJ & FK & EM & LP & VC \\\\\n\\midrule\nLLaMA/SciERC $N{=}8$ & 529 & .646 & .778 & .643 & .639 & .634 & \\textbf{.652} & .633 \\\\\nLLaMA/SciERC $N{=}16$ & 529 & .645 & .806 & \\textbf{.649} & \\textbf{.649} & .640 & .646 & .640 \\\\\nQwen/CoNLL $N{=}8$ & 2{,}756 & .908 & .948 & \\textbf{.899} & .893 & .898 & .897 & .895 \\\\\nLLaMA/CoNLL $N{=}8$ & 2{,}756 & .924 & .943 & .924 & \\textbf{.925} & .924 & .924 & .923 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\paragraph{Diminishing returns of $N$-scaling.}\nOur $N{=}8$ and $N{=}16$ comparisons (Table~\\ref{tab:robustness}) characterize the marginal value of additional samples for test-time scaling \\cite{brown2024monkeys, snell2024scaling}.\nFor quality estimation, structural signals benefit consistently but sublinearly: SJ $\\rho$ improves by $+0.052$ (Qwen SciERC, 3-seed mean) and $+0.032$ (LLaMA CoNLL, 3-seed mean) when doubling from $N{=}8$ to $N{=}16$, while log-probability is approximately $N$-invariant ($\\Delta\\rho{\\leq}0.021$).\nStructural signals leverage $\\binom{N}{2}$ pairwise comparisons (28 pairs at $N{=}8$, 120 at $N{=}16$), but the $\\rho$ improvement is far less than proportional, indicating diminishing information per additional comparison.\nThis asymmetry gives structural signals a relative advantage in the compute-constrained regime: at $N{=}8$, SJ already achieves $\\rho{=}0.431$ on LLaMA CoNLL (vs.\\ LP $\\rho{=}0.307$, $\\Delta{=}{+}0.124$), and the gap \\textit{widens} at $N{=}16$ ($\\Delta{=}{+}0.153$) because structural signals continue to benefit from additional pairwise evidence while LP does not.\nFor sample selection, additional samples increase the oracle upper bound---more draws raise the probability of a high-quality candidate---but signal-based selection remains flat because the selector's inability to identify the best candidate is a granularity limitation, not a sample size limitation.\nThe practical implication is that $N{=}8$ captures most of the achievable quality estimation benefit; further scaling widens rather than closes the correlation-selection gap absent stronger per-sample selectors.\n\n\\section{Bootstrap CI for Signal Comparisons}\\label{app:bootstrap_signal}\n\nTable~\\ref{tab:bootstrap_signal_ci} reports bootstrap confidence intervals for individual signal $\\rho$ and pairwise $\\Delta\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$).\nThe SJ--LP gap ($\\Delta\\rho{=}{+}0.155$) is clearly significant, confirming the structural advantage reported in \\S\\ref{sec:qe_results}.\nThe VC--SJ gap ($\\Delta\\rho{=}{+}0.019$) is not significant, indicating that these two structural signals perform comparably.\nThe SJ--EM gap ($\\Delta\\rho{=}{+}0.065$) is borderline significant, with the CI lower bound at $+0.003$ and upper bound at $+0.130$.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Bootstrap 95\\% CIs for signal $\\rho$ on SciERC NER ($N{=}8$, $n{=}529$, $B{=}10{,}000$, seed${=}42$). Top: individual signals. Bottom: pairwise $\\Delta\\rho$; ``Sig.'' indicates whether the 95\\% CI excludes zero.}\n\\label{tab:bootstrap_signal_ci}\n\\begin{tabular}{lcc}\n\\toprule\nSignal & $\\rho$ & 95\\% CI \\\\\n\\midrule\nVC & +0.379 & [+0.299, +0.456] \\\\\nSJ & +0.360 & [+0.277, +0.437] \\\\\nEM & +0.295 & [+0.212, +0.371] \\\\\nFK & +0.267 & [+0.176, +0.354] \\\\\nLP & +0.205 & [+0.119, +0.291] \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{0.5em}\n\n\\begin{tabular}{lccc}\n\\toprule\nComparison & $\\Delta\\rho$ & 95\\% CI & Sig. \\\\\n\\midrule\nSJ $-$ LP & +0.155 & [+0.074, +0.234] & Yes \\\\\nVC $-$ SJ & +0.019 & [$-$0.033, +0.073] & No \\\\\nSJ $-$ EM & +0.065 & [+0.003, +0.130] & Marginal$^\\dagger$ \\\\\n\\bottomrule\n\\end{tabular}\n\n\\smallskip\n{\\footnotesize $^\\dagger$Marginally significant without multiple comparison correction; would not survive Bonferroni correction for 10 pairwise comparisons ($\\alpha_{\\text{adj}}{=}0.005$).}\n\\end{table}\n\n\\section{Diversity and Selection Analysis}\\label{app:diversity}\n\n\\paragraph{Output diversity quantification.}\nTable~\\ref{tab:diversity} summarizes output diversity across configurations.\nOn SciERC, output diversity is substantial: Qwen produces 43\\% unique outputs per instance (mean 3.5 distinct out of $N{=}8$), with per-sample F1 standard deviation of 0.144 and mean pairwise SJ of 0.703.\nLLaMA shows similar diversity (39\\% unique, F1 std 0.11).\nOn CoNLL, diversity collapses: 57\\% (Qwen) to 88\\% (LLaMA) of instances produce identical outputs across all $N$ samples, reflecting a ceiling effect where greedy F1 already exceeds 0.90.\nWNUT-17 shows 55\\% identical outputs, driven by the 52\\% zero-F1 rate.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Output diversity across configurations ($N{=}8$, $T{=}1.0$). ``Identical'' = fraction of instances with all $N$ outputs identical. ``Unique'' = mean fraction of distinct outputs per instance.}\n\\label{tab:diversity}\n\\begin{tabular}{lcc}\n\\toprule\nConfig & Identical & Unique \\\\\n\\midrule\nQwen/SciERC & 11\\% & 43\\% \\\\\nLLaMA/SciERC & 18\\% & 39\\% \\\\\nQwen/CoNLL & 57\\% & --- \\\\\nLLaMA/CoNLL & 88\\% & --- \\\\\nWNUT-17 & 55\\% & --- \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Oracle-improvable fraction.}\nAcross SciERC configurations, 39--42\\% of instances contain at least one sample with F1 exceeding greedy: Qwen NER 42.0\\% (222/529, mean headroom $+$31.9~pp among improvable instances), Qwen RE 41.3\\% (164/397, $+$45.3~pp), LLaMA NER 39.3\\% (208/529, $+$33.7~pp).\nOn CoNLL, only 4--9\\% of instances are improvable, confirming the ceiling effect.\n\n\\paragraph{Diversity-stratified selection gap.}\nOn the 44\\% of Qwen SciERC instances with high diversity (${\\geq}4$ unique outputs among 8 samples, $n{=}232$), oracle headroom reaches $+$16.3~pp, yet all consistency-based signals (SJ, FK, EM, VC) select at or below greedy, and LP---the only per-sample signal---achieves merely $+$0.8~pp.\nLLaMA replicates this pattern: on its high-diversity subset ($n{=}186$), oracle headroom reaches $+$20.1~pp while consistency signals remain at or below greedy and LP captures only $+$2.0~pp.\nThis rules out insufficient diversity as an explanation for the correlation-selection gap.\n\n\\paragraph{TOST equivalence testing.}\nThe primary evidence against selection gains comes from effect sizes and confidence intervals: Cohen's $d{=}0.038$ for the best signal (NER LP) and bootstrap 95\\% CI [$-$3.0, $+$4.2]~pp spanning zero.\nTable~\\ref{tab:tost} supplements this with two one-sided tests (TOST), testing whether each signal's selection F1 is equivalent to greedy within a bound $\\delta$.\nThe $\\delta$ values are anchored to oracle headroom (13--18~pp): $\\delta{=}5$~pp corresponds to forgoing 28--38\\% of the available headroom, $\\delta{=}3$~pp forgoing 17--23\\%, and $\\delta{=}2$~pp less than 15\\%.\nThe breakpoint $\\delta^*$---the minimum equivalence margin at which each signal passes TOST---ranges from approximately 1.3~pp (SJ, ${\\sim}$10\\% of oracle headroom) to 3.4~pp (FK, ${\\sim}$26\\%) on NER, and from approximately 2.9~pp (LP, ${\\sim}$16\\%) to 6.5~pp (VC, ${\\sim}$36\\%) on RE.\nOn NER ($n{=}529$), at $\\delta{=}{\\pm}2$~pp, SJ and LP are confirmed equivalent to greedy (TOST $p{<}0.05$); at $\\delta{=}{\\pm}3$~pp, four of five signals pass; at $\\delta{=}{\\pm}5$~pp, all five pass.\nOn RE ($n{=}397$, preliminary), EM and VC fail equivalence even at $\\delta{=}{\\pm}5$~pp due to systematic underperformance ($\\Delta{=}{-}3.2$~pp and $-4.5$~pp respectively).\nThe effect sizes are negligible ($d{=}0.038$) and confidence intervals span zero, with TOST confirming equivalence at practically meaningful margins.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{TOST equivalence testing: signals vs.\\ greedy on SciERC ($N{=}8$, $T{=}1.0$). \\checkmark: equivalent at $p{<}0.05$; \\texttimes: not equivalent. $\\Delta$: mean F1 difference (signal $-$ greedy).}\n\\label{tab:tost}\n\\begin{tabular}{l cccc cccc}\n\\toprule\n& \\multicolumn{4}{c}{\\textbf{NER}} & \\multicolumn{4}{c}{\\textbf{RE}} \\\\\n\\cmidrule(lr){2-5} \\cmidrule(lr){6-9}\nSignal & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 & $\\Delta$ & $\\pm$2 & $\\pm$3 & $\\pm$5 \\\\\n\\midrule\nLP & +0.6 & \\checkmark & \\checkmark & \\checkmark & $-$0.9 & \\texttimes & \\checkmark & \\checkmark \\\\\nSJ & +0.1 & \\checkmark & \\checkmark & \\checkmark & $-$1.8 & \\texttimes & \\texttimes & \\checkmark \\\\\nFK & $-$0.5 & \\texttimes & \\checkmark & \\checkmark & $-$1.6 & \\texttimes & \\texttimes & \\checkmark \\\\\nEM & $-$0.8 & \\texttimes & \\checkmark & \\checkmark & $-$3.2 & \\texttimes & \\texttimes & \\texttimes \\\\\nVC & $-$1.0 & \\texttimes & \\texttimes & \\checkmark & $-$4.5 & \\texttimes & \\texttimes & \\texttimes \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Multi-Seed Stability}\\label{app:multiseed}\n\nTable~\\ref{tab:multiseed} reports quality estimation metrics across three random seeds for both model families on SciERC ($N{=}8$, $T{=}1.0$).\nOn NER, the signal ranking VC${>}$SJ${>}$EM${>}$FK${>}$LP is identical across all six model-seed combinations, with $\\sigma{\\leq}0.025$ for all signals.\nOn RE (Qwen only, preliminary), VC remains the top signal ($\\rho{=}0.309{\\pm}0.024$), but LP rises to \\#2 ($\\rho{=}0.297{\\pm}0.022$), above FK, SJ, and EM---a reversal from the NER ranking that reflects RE's higher sensitivity to per-sample scoring.\nLLaMA absolute values are systematically lower than Qwen on NER, consistent with the directionally-consistent-but-magnitude-dependent characterization in the main text.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Multi-seed quality estimation on SciERC ($N{=}8$, $T{=}1.0$, seeds: 42, 123, 456). NER: both models; RE: Qwen only (preliminary). Signal ranking is stable across seeds ($\\sigma{\\leq}0.025$).}\n\\label{tab:multiseed}\n\\begin{tabular}{lccccc}\n\\toprule\n& LP & FK & SJ & VC & EM \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER Spearman $\\rho$ (mean $\\pm\\sigma$)}} \\\\\nQwen & .217${\\pm}$.013 & .254${\\pm}$.016 & .364${\\pm}$.018 & .386${\\pm}$.019 & .307${\\pm}$.008 \\\\\nLLaMA & .162${\\pm}$.025 & .256${\\pm}$.024 & .325${\\pm}$.021 & .384${\\pm}$.014 & .279${\\pm}$.011 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{RE Spearman $\\rho$ (mean $\\pm\\sigma$, Qwen)}} \\\\\nQwen & .297${\\pm}$.022 & .290${\\pm}$.012 & .249${\\pm}$.002 & .309${\\pm}$.024 & .135${\\pm}$.016 \\\\\n\\midrule\n\\multicolumn{6}{l}{\\textit{NER AUROC (mean $\\pm\\sigma$)}} \\\\\nQwen & .613${\\pm}$.002 & .618${\\pm}$.009 & .684${\\pm}$.009 & .697${\\pm}$.010 & .661${\\pm}$.010 \\\\\nLLaMA & .577${\\pm}$.007 & .616${\\pm}$.011 & .655${\\pm}$.010 & .689${\\pm}$.005 & .636${\\pm}$.006 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Training Configuration}\\label{app:training}\n\nBoth models are fine-tuned with identical hyperparameters (Table~\\ref{tab:training}) to ensure comparisons across model families reflect model differences rather than training confounds.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Training configuration. Both Qwen3-8B and LLaMA-3.1-8B-Instruct use identical settings unless noted.}\n\\label{tab:training}\n\\begin{tabular}{ll}\n\\toprule\nParameter & Value \\\\\n\\midrule\nLoRA rank / $\\alpha$ & 32 / 64 \\\\\nLoRA target & All linear modules \\\\\nLoRA dropout & 0 \\\\\nOptimizer & AdamW \\\\\nLearning rate & 2e-4, cosine schedule \\\\\nWarmup ratio & 0.1 \\\\\nEffective batch size & 16 (2 $\\times$ grad.\\ accum.\\ 8) \\\\\nEpochs & 5 \\\\\nMax sequence length & 2048 \\\\\nPrecision & bf16 \\\\\nGradient checkpointing & Enabled \\\\\nMax gradient norm & 1.0 \\\\\nTraining seed & 42 \\\\\nFramework & LLaMA Factory \\\\\n\\midrule\n\\multicolumn{2}{l}{\\textit{Dataset-specific}} \\\\\nSciERC split & 1861 / 275 / 551 \\\\\nCoNLL / WNUT & +\\,load\\_best\\_model\\_at\\_end, \\\\\n& eval\\_steps${=}$200, save\\_limit${=}$5 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Prompt template.}\nFor NER, we use a structured prompt:\n\\begin{quote}\n\\small\n\\texttt{System:} You are an expert in Named Entity Recognition.\\\\\n\\texttt{User:} Extract all named entities from the following text. Output as JSON.\\\\\nText: \\texttt{\\{input\\_text\\}}\\\\\nEntity types: \\texttt{\\{schema\\_types\\}}\n\\end{quote}\nRE follows the same structure with ``Relation Extraction'' and relation type lists substituted accordingly.\n\n\\paragraph{Constrained decoding.}\nInference uses vLLM with XGrammar-based JSON schema enforcement \\cite{willard2023guided}, which constrains outputs to valid entity/relation structures matching the target schema.\nThis eliminates format errors but may compress per-sample diversity by restricting the output space.\\footnote{SciERC training used \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), injecting empty \\texttt{&lt;think>&lt;/think>} blocks (4--5 tokens) into each training response with loss computation; CoNLL and WNUT explicitly set \\texttt{enable\\_thinking=False}. Constrained decoding at inference time enforces JSON-only output, suppressing thinking tokens. See \\S\\ref{sec:setup} and Limitations for discussion of this confound.}\n\n\\section{Log-Probability Score Compression}\\label{app:logprob_ties}\n\nUnder constrained decoding, log-probability scores are severely compressed within instances, limiting per-sample discrimination (Table~\\ref{tab:logprob_ties}).\nThe median within-instance LP range is only 0.041, and 75\\% of pairwise comparisons are effective ties ($|\\Delta|{<}0.026$).\nAt $\\varepsilon{=}0.05$, 60.3\\% of instances have a within-sample range below the threshold, leaving LP unable to meaningfully distinguish candidates.\nFor comparison, SJ has only 12.5\\% tied instances at the same threshold---SJ's advantage over LP for selection is one of score resolution, not information content.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Log-probability score compression on SciERC NER ($N{=}8$, $n{=}529$). ``Tied'' = fraction of instances where within-instance LP range ${<}\\varepsilon$.}\n\\label{tab:logprob_ties}\n\\begin{tabular}{lc}\n\\toprule\n$\\varepsilon$ threshold & Tied instances (\\%) \\\\\n\\midrule\n0.01 & 1.1\\% \\\\\n0.05 & 60.3\\% \\\\\n0.1  & ${\\sim}$84\\% \\\\\n0.5  & ${\\sim}$99\\% \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Non-tied subset.}\nAmong instances with LP range ${\\geq}0.05$ ($n{=}210$, 40\\% of total), log-probability selection \\textit{significantly} outperforms greedy ($+2.9$~pp F1, $p{=}0.01$), and within-instance $\\rho(\\text{LP}, \\text{F1})$ rises from 0.08 (tied subset) to 0.39 (non-tied subset).\nThis confirms that LP carries useful per-sample quality information but is resolution-limited---the signal exists but is compressed below the discrimination threshold for most instances.\nA free-form decoding ablation (Appendix~\\ref{app:freeform_ablation}) confirms this compression is intrinsic, not decoding-regime-specific.\n\n\\section{RE Conditional Selection}\\label{app:re_conditional_selection}\n\nTable~\\ref{tab:re_cond_selection} extends the selection analysis to the RE non-zero F1 subset.\nOf $n{=}397$ RE instances, 238 (60\\%) have non-zero F1 and 159 (40\\%) have zero F1.\nAll five signals underperform greedy on both subsets.\nOn the non-zero subset, selection performance is \\textit{worse} than on the full set (e.g., VC: $-10.0$~pp on non-zero vs.\\ $-4.5$~pp on full set), because greedy is already strong on non-zero instances (F1${=}0.674$) and signals actively select inferior samples.\nOracle headroom exists (0.757 vs.\\ 0.674) but no signal exploits it, ruling out the 40\\% zero-F1 floor effect as the explanation for RE selection failure.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE selection F1 on SciERC ($N{=}8$, $T{=}1.0$). Full set ($n{=}397$) and non-zero F1 subset ($n{=}238$). No signal outperforms greedy on either subset.}\n\\label{tab:re_cond_selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & Full ($n{=}397$) & Non-zero ($n{=}238$) \\\\\n\\midrule\nOracle & 0.585 & 0.757 \\\\\n\\midrule\nLP & 0.395 & 0.600 \\\\\nSJ & 0.386 & 0.604 \\\\\nEM & 0.372 & 0.583 \\\\\nVC & 0.359 & 0.574 \\\\\n\\midrule\nGreedy & 0.404 & 0.674 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\section{Free-Form Decoding Ablation}\\label{app:freeform_ablation}\n\nTable~\\ref{tab:freeform_ablation} compares constrained and free-form decoding across four dimensions on SciERC ($N{=}8$, $T{=}1.0$, Qwen3-8B).\nFree-form decoding removes grammar constraints entirely; outputs are parsed post-hoc (parse rate 99.95\\%, 4406/4408).\nLP score distributions are nearly identical across regimes (Panel~A: within-instance std ratio $0.97{\\times}$), and NER selection gains remain negligible under both regimes (Panel~B).\nRE LP selection flips positive under free-form decoding ($+1.69$~pp vs.\\ $-0.68$~pp constrained).\nQuality estimation improves modestly for most signals under free-form decoding (Panel~C), with the largest gain for FK ($+0.053$ NER, $+0.039$ RE).\n\n\\begin{table*}[t]\n\\centering\n\\caption{Comparison of constrained vs.\\ free-form decoding on SciERC (Qwen3-8B, $N{=}8$, $T{=}1.0$, seed=42).}\n\\label{tab:freeform_ablation}\n\n\\vspace{2pt}\n{\\small\\textsc{Panel A: Logprob Distribution}}\n\\vspace{2pt}\n\n\\begin{tabular}{lccc}\n\\toprule\nMetric & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\nMean LP std        & 0.0206 & 0.0199 & $-$0.0007 \\\\\nMean LP range      & 0.0623 & 0.0599 & $-$0.0024 \\\\\nTied fraction ($\\varepsilon{=}0.05$) & 59.7\\% & 57.7\\% & $-$2.0\\,pp \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel B: Selection F1}}\n\\vspace{2pt}\n\n\\begin{tabular}{llccc}\n\\toprule\nTask & Method & Constrained & Free-form & $\\Delta$ \\\\\n\\midrule\n\\multirow{3}{*}{NER}\n  & Greedy        & 0.6182 & 0.6204 & $+$0.0022 \\\\\n  & LP-selected   & 0.6241 & 0.6222 & $-$0.0019 \\\\\n  & Selection gap & $+$0.0059 & $+$0.0018 & $-$0.0041 \\\\\n\\midrule\n\\multirow{3}{*}{RE}\n  & Greedy        & 0.2913 & 0.2880 & $-$0.0033 \\\\\n  & LP-selected   & 0.2845 & 0.3050 & \\textbf{$+$0.0205} \\\\\n  & Selection gap & $-$0.0068 & $+$0.0169 & \\textbf{$+$0.0237} \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel C: QE Signal Quality (Spearman $\\rho$)}}\n\\vspace{2pt}\n\n\\begin{tabular}{l ccc ccc}\n\\toprule\n & \\multicolumn{3}{c}{NER ($n{=}529$)} & \\multicolumn{3}{c}{RE ($n{=}397$)} \\\\\n\\cmidrule(lr){2-4} \\cmidrule(lr){5-7}\nSignal & Constr. & Free & $\\Delta$ & Constr. & Free & $\\Delta$ \\\\\n\\midrule\nSJ & 0.360 & 0.377 & $+$0.018 & 0.250 & 0.273 & $+$0.023 \\\\\nFK & 0.267 & 0.320 & $+$0.053 & 0.275 & 0.315 & $+$0.039 \\\\\nLP & 0.205 & 0.213 & $+$0.008 & 0.266 & 0.304 & $+$0.038 \\\\\nEM & 0.295 & 0.317 & $+$0.023 & 0.134 & 0.137 & $+$0.002 \\\\\nVC & 0.379 & 0.409 & $+$0.030 & 0.350 & 0.323 & $-$0.026 \\\\\n\\bottomrule\n\\end{tabular}\n\n\\vspace{8pt}\n\n{\\small\\textsc{Panel D: Parse Rate (Free-form)}}\n\\vspace{2pt}\n\n\\begin{tabular}{lc}\n\\toprule\nMetric & Value \\\\\n\\midrule\nTotal samples          & 4408 \\\\\nParse rate             & 99.95\\% \\\\\nInstances 8/8 valid    & 549\\,/\\,551 (99.6\\%) \\\\\n\\bottomrule\n\\end{tabular}\n\n\\end{table*}\n\n\\section{LP Selection Failure Stability}\\label{app:lp_failure_stability}\n\nWe analyze RE LP selection failures across three random seeds (constrained decoding, $N{=}8$, $T{=}1.0$, Qwen3-8B) to assess whether failures are systematic or stochastic.\n\n\\paragraph{Pairwise overlap.}\nLP selection failures (instances where LP-selected F1 $<$ greedy F1) show moderate cross-seed stability: the average pairwise Jaccard similarity is 0.42 (range: 0.38--0.46), indicating that failures are partially systematic---driven by instance complexity---but not fully deterministic.\nThe 3-way intersection contains 34 instances (27.9\\% of any-seed failures), confirming a stable failure core.\n\n\\paragraph{Instance complexity drives failure.}\nTable~\\ref{tab:stable_failures} stratifies instances by failure stability.\nStable failures (all 3 seeds) involve more gold relations (2.12 vs.\\ 1.62 for never-fail instances) and higher greedy F1 (0.688 vs.\\ 0.429), indicating that LP mis-selects on instances where the model already performs well---precisely the instances where selection would be most valuable.\nFailure rate increases monotonically with gold relation count: 4.3\\% at 1 relation, 20.7\\% at 3 relations, 26.2\\% at 6 relations.\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{RE LP selection failure stability across 3 seeds (SciERC, $N{=}8$). Stable failures concentrate on relation-dense instances with high greedy F1.}\n\\label{tab:stable_failures}\n\\begin{tabular}{lcccc}\n\\toprule\nGroup & $n$ & Gold rels & Greedy F1 & LP $\\Delta$F1 \\\\\n\\midrule\nStable fail (3 seeds) & 34 & 2.12 & 0.688 & $-$0.499 \\\\\nFail 2+ seeds & 26 & 2.46 & 0.774 & $-$0.450 \\\\\nFail 1 seed & 62 & 2.32 & 0.692 & $-$0.239 \\\\\nNever fail & 429 & 1.62 & 0.429 & $+$0.041 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\n\\paragraph{Flip instances.}\nOnly 5 RE instances with gold relations flip from LP failure (constrained) to LP success (free-form), with mean gold relation count 3.67 (well above the population mean of 1.86).\nThese instances show large constrained LP errors ($\\Delta{=}{-}0.430$) that reverse under free-form decoding ($\\Delta{=}{+}0.503$), but their rarity (5/397) confirms that the RE selection flip is driven by aggregate variance reallocation rather than systematic instance-level correction.\n",
      "numLines": 557,
      "startLine": 1,
      "totalLines": 557
    }
  },
  "sourceToolAssistantUUID": "517fb4b3-bb8c-4c2c-9f62-0462c7930a31",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Runtime record

_source line 520_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Paper Agent 触发审查]: ## D072 Framing Update Review Request  **变更范围**: D072 将论文从 \"regime-specific bottleneck under constrained decoding\" 改为 \"universal correlation-selection gap\"。主要受影响章节: title, abstract…",
  "leafUuid": "5b682fb9-a93b-42f2-9c5d-7174d882d61d",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Runtime record

_source line 521_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker verification completion status",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Assistant

_source line 522 · 2026-05-15T11:48:56.900Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the paper. Let me also read the experiments section to check for any residual "regime-specific" language, and to verify the title section.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5b682fb9-a93b-42f2-9c5d-7174d882d61d",
  "isSidechain": false,
  "requestId": "req_011Cb4JW7kb8AbTXkZC3ttNT",
  "type": "assistant",
  "uuid": "edcc9efc-ba75-4c48-a076-a4d73c82ac0e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct4MRGXjcvmNsP4FofRxjR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19673,
      "cache_read_input_tokens": 82124,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 82124,
          "cache_creation_input_tokens": 19673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19673
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


### Assistant

_source line 523 · 2026-05-15T11:48:57.832Z_

Now let me check the title and experiments sections for residual "regime-specific" language, and cross-verify key numbers.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "edcc9efc-ba75-4c48-a076-a4d73c82ac0e",
  "isSidechain": false,
  "requestId": "req_011Cb4JW7kb8AbTXkZC3ttNT",
  "type": "assistant",
  "uuid": "df6059cf-a9c3-4a39-84a3-b244c2b7f13b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct4MRGXjcvmNsP4FofRxjR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19673,
      "cache_read_input_tokens": 82124,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 82124,
          "cache_creation_input_tokens": 19673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19673
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

_source line 524 · 2026-05-15T11:48:59.728Z_

<details open><summary>🔧 Tool call — Read · `toolu_01A6SZ7hBLjunA9pBJA2m47n`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "df6059cf-a9c3-4a39-84a3-b244c2b7f13b",
  "isSidechain": false,
  "requestId": "req_011Cb4JW7kb8AbTXkZC3ttNT",
  "type": "assistant",
  "uuid": "ebda362f-41b4-4753-8370-48bc9da3fec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct4MRGXjcvmNsP4FofRxjR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19673,
      "cache_read_input_tokens": 82124,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 82124,
          "cache_creation_input_tokens": 19673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19673
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

_source line 525 · 2026-05-15T11:49:00.236Z_

<details><summary>↩ Tool result · `toolu_01WPZM1opZMtRkt6nzqCsVJ2`</summary>

```text
1	\section{Experiments}
2	\label{sec:experiments}
3	
4	\subsection{Experimental Setup}
5	\label{sec:setup}
6	
7	\paragraph{Datasets.}
8	We evaluate on three English IE benchmarks spanning a difficulty gradient.
9	\textbf{SciERC} \cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).
10	\textbf{CoNLL-2003} \cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\approx}$91\% micro F1.
11	\textbf{WNUT-17} \cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\% zero F1).
12	
13	\paragraph{Models and sampling.}
14	Both \textbf{Qwen3-8B} and \textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\alpha{=}64$) for 5 epochs using LLaMA Factory \cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.
15	We note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \texttt{enable\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \texttt{&lt;think>\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \texttt{enable\_thinking=False}.
16	No reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.
17	This constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.
18	We discuss implications in the Limitations section.
19	We draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}). A 3-seed stability analysis ($\sigma{\leq}0.025$; Table~\ref{tab:multiseed}, Appendix~\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}
20	Quality estimation uses Spearman $\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).
21	Inference uses vLLM with constrained decoding \cite{willard2023guided}.
22	
23	%% ============================================================
24	\subsection{Quality Estimation Results}
25	\label{sec:qe_results}
26	
27	\begin{table*}[t]
28	\centering
29	\small
30	\caption{Quality estimation across tasks and models (Spearman $\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\ref{tab:robustness} (Appendix~\ref{app:robustness}).}
31	\label{tab:quality_estimation}
32	\begin{tabular}{ll cc cc cc cc}
33	\toprule
34	& & \multicolumn{2}{c}{\textbf{SciERC NER}} & \multicolumn{2}{c}{\textbf{SciERC RE}} & \multicolumn{2}{c}{\textbf{CoNLL (Qwen)}} & \multicolumn{2}{c}{\textbf{CoNLL (LLaMA)}} \\
35	\cmidrule(lr){3-4} \cmidrule(lr){5-6} \cmidrule(lr){7-8} \cmidrule(lr){9-10}
36	Signal & Family & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC & $\rho$ & AUC \\
37	\midrule
38	VC & Structural & \textbf{.379} & .684 & \textbf{.350} & .693 & .424 & .789 & .426 & .709 \\
39	SJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \textbf{.431} & .704 \\
40	FK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\
41	EM  & Surface    & .295 & \textbf{.749} & .134 & \textbf{.706} & \textbf{.451} & \textbf{.816} & \textbf{.431} & .705 \\
42	LP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \textbf{.761} \\
43	\bottomrule
44	\end{tabular}
45	\end{table*}
46	
47	\begin{figure*}[t]
48	\centering
49	\includegraphics[width=\textwidth]{fig_signal_heatmap}
50	\caption{Quality estimation heatmap (Spearman $\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$), while LP RE collapses to near-zero ($\rho{=}0.011$).}
51	\label{fig:signal_heatmap}
52	\end{figure*}
53	
54	Table~\ref{tab:quality_estimation} presents rank correlation ($\rho$) and AUROC for five confidence signals across tasks and models.
55	
56	\paragraph{Difficulty-dependent signal complementarity.}
57	On SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\rho{=}0.379$ and SJ $\rho{=}0.360$, both outperforming surface ($\rho{\leq}0.295$) and LP ($\rho{=}0.205$).
58	This advantage persists on RE (VC $\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\% zero-F1 floor effect.
59	VC and SJ show moderate instance-level correlation (NER: $\rho{=}0.659$; RE: $\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\ span-level set overlap.
60	While the best $\rho{=}0.38$ (VC) explains approximately 14\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\footnote{For scale context, semantic entropy \cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}
61	Pairwise bootstrap CIs confirm the SJ advantage over LP ($\Delta\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\Delta\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\ref{tab:bootstrap_signal_ci}, Appendix~\ref{app:bootstrap_signal}).
62	
63	\paragraph{$\rho$--AUROC dissociation.}
64	Signal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\rho$ (0.295), preferred for binary quality triage; structural signals ($\rho{\geq}0.36$) are better for fine-grained ranking.
65	On CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\rho$ (0.307), confirming this pattern across datasets.
66	
67	\paragraph{Signal rankings shift with task difficulty.}
68	On CoNLL (greedy F1${\approx}$0.91), EM leads ($\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.
69	When most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.
70	This crossover---EM${>}$SJ on easy tasks vs.\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.
71	Stability across the two model families (both 8B) is strong: SJ achieves $\rho{=}0.436$ (Qwen) vs.\ $0.431$ (LLaMA) on CoNLL ($\Delta{=}0.005$, within 3-seed $\sigma{\approx}0.007$).
72	On WNUT-17, where 52\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\rho{=}0.038$, n.s.; Table~\ref{tab:wnut}).
73	LP exhibits strong \textit{negative} correlation ($\rho{=}{-}0.410$, AUROC${=}0.219$).
74	We hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.
75	On the conditional set, all signals collapse toward weak or non-significant correlations ($\rho{\leq}0.35$), with SJ achieving only $\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.
76	
77	\paragraph{Conditional filtering.}
78	Filtering to non-zero F1 instances reshuffles rankings (Figure~\ref{fig:signal_heatmap}, right).
79	EM emerges as the strongest conditional signal on both NER ($\rho{=}0.360$) and RE ($\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\to}0.300$; FK NER: $0.267{\to}0.176$).
80	LP RE collapses to $\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.
81	This creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\ref{app:additional} for details).
82	
83	%% ============================================================
84	\subsection{The Correlation-Selection Gap}
85	\label{sec:selection_gap}
86	
87	\begin{figure*}[t]
88	\centering
89	\includegraphics[width=\textwidth]{fig_selection_gap}
90	\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\rho$. Despite $\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\ref{tab:selection}). Dashed line indicates oracle upper bound.}
91	\label{fig:selection_gap}
92	\end{figure*}
93	
94	\begin{table}[t]
95	\centering
96	\small
97	\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \textbf{bold}. EM selects the plurality output; despite a 42\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}
98	\label{tab:selection}
99	\begin{tabular}{lcc}
100	\toprule
101	Method & NER F1 & RE F1 \\
102	\midrule
103	Oracle & 0.776 & 0.585 \\
104	\midrule
105	LP           & \textbf{0.650} & 0.395 \\
106	SJ       & 0.645 & 0.386 \\
107	EM        & 0.636 & 0.372 \\
108	VC                 & 0.634 & 0.359 \\
109	\midrule
110	Greedy ($T{=}0$)   & 0.644 & \textbf{0.404} \\
111	Random             & 0.608 & 0.354 \\
112	\bottomrule
113	\end{tabular}
114	\end{table}
115	
116	Despite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\ref{tab:selection}, Figure~\ref{fig:selection_gap}).
117	Four of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.
118	The non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.
119	We anchor this analysis on SciERC, where output diversity is substantial: only 11--18\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.
120	
121	\paragraph{No significant improvement over greedy.}
122	We exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).
123	On NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).
124	LP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).
125	On RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.
126	TOST equivalence testing confirms most signals are indistinguishable from greedy at ${\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\pm}5$~pp (Table~\ref{tab:tost}, Appendix~\ref{app:diversity}).
127	VC ($\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\textit{below} greedy.
128	The gap extends to CoNLL (ceiling effect, 57--88\% identical outputs) and WNUT-17 (capability boundary; Table~\ref{tab:cross_selection}).
129	
130	\paragraph{Quality estimation $\neq$ output selection.}
131	Instance-level confidence signals predict \textit{which inputs} the model handles reliably, not \textit{which output} among $N$ candidates is best.
132	When per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.
133	This gap has direct consequences for test-time scaling in IE \cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \cite{cobbe2021verifiers}.
134	
135	%% ============================================================
136	\subsection{Robustness}
137	\label{sec:robustness_main}
138	
139	Consistency-based signals show robust performance across $T{\in}\{0.7, 1.0\}$ (SJ NER $\Delta\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\Delta\rho{=}{+}0.135$ to ${+}0.175$; Table~\ref{tab:robustness}, Appendix~\ref{app:robustness}).
140	NER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\rho{\approx}0.28$ for $N{=}16$.
141	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "753c1fd0-bb98-4209-bfe4-86999e236606",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "8e5e903f-0802-458b-96f2-b9e5f8384007",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex",
      "content": "\\section{Experiments}\n\\label{sec:experiments}\n\n\\subsection{Experimental Setup}\n\\label{sec:setup}\n\n\\paragraph{Datasets.}\nWe evaluate on three English IE benchmarks spanning a difficulty gradient.\n\\textbf{SciERC} \\cite{luan2018scierc} contains 551 test instances annotated for joint NER (6 types) and RE (7 types).\n\\textbf{CoNLL-2003} \\cite{tjongkimsang2003conll} provides 3{,}453 test sentences with 4 entity types, where models achieve ${\\approx}$91\\% micro F1.\n\\textbf{WNUT-17} \\cite{derczynski2017wnut} consists of 1{,}287 social media instances with emerging entities, used to probe method boundaries (52\\% zero F1).\n\n\\paragraph{Models and sampling.}\nBoth \\textbf{Qwen3-8B} and \\textbf{LLaMA-3.1-8B-Instruct} are fine-tuned with LoRA (rank$=$32, $\\alpha{=}64$) for 5 epochs using LLaMA Factory \\cite{zheng2024llamafactory} under identical training procedures, ensuring comparisons across the two model families (both at 8B scale) reflect model differences rather than training confounds.\nWe note a training confound for SciERC: Qwen3-8B's SciERC checkpoint was trained with \\texttt{enable\\_thinking=True} (LLaMA Factory 0.9.4 default), which prepends empty \\texttt{&lt;think>\\textbackslash n&lt;/think>} blocks (4--5 tokens) to each training response and includes them in the loss computation; CoNLL-2003 and WNUT-17 checkpoints explicitly set \\texttt{enable\\_thinking=False}.\nNo reasoning content is present (the blocks are always empty), and constrained decoding at inference time enforces JSON-only output, so thinking tokens do not appear in generated samples.\nThis constitutes a minor train--test distribution mismatch for SciERC ($<$0.3\\% of the 2048-token training window); CoNLL-2003 and WNUT-17 are unaffected.\nWe discuss implications in the Limitations section.\nWe draw $N{=}8$ samples at $T{=}1.0$ (primary; single seed, seed${=}42$), with $N{=}16$ for scaling experiments.\\footnote{$N{=}16$ results for CoNLL (Qwen) and SciERC (LLaMA) are in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}). A 3-seed stability analysis ($\\sigma{\\leq}0.025$; Table~\\ref{tab:multiseed}, Appendix~\\ref{app:multiseed}) confirms that signal rankings are identical across seeds.}\nQuality estimation uses Spearman $\\rho$ and AUROC; downstream utility uses best-of-$N$ selection F1 with exact span matching (NER) and head-tail-label matching (RE).\nInference uses vLLM with constrained decoding \\cite{willard2023guided}.\n\n%% ============================================================\n\\subsection{Quality Estimation Results}\n\\label{sec:qe_results}\n\n\\begin{table*}[t]\n\\centering\n\\small\n\\caption{Quality estimation across tasks and models (Spearman $\\rho$ and AUROC; $N{=}8$, seed${=}42$). Best value per column in \\textbf{bold}. SciERC evaluates joint NER (6 types) and RE (7 types, single benchmark---preliminary); CoNLL evaluates NER (4 types). $N{=}16$ results appear in Table~\\ref{tab:robustness} (Appendix~\\ref{app:robustness}).}\n\\label{tab:quality_estimation}\n\\begin{tabular}{ll cc cc cc cc}\n\\toprule\n& & \\multicolumn{2}{c}{\\textbf{SciERC NER}} & \\multicolumn{2}{c}{\\textbf{SciERC RE}} & \\multicolumn{2}{c}{\\textbf{CoNLL (Qwen)}} & \\multicolumn{2}{c}{\\textbf{CoNLL (LLaMA)}} \\\\\n\\cmidrule(lr){3-4} \\cmidrule(lr){5-6} \\cmidrule(lr){7-8} \\cmidrule(lr){9-10}\nSignal & Family & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC & $\\rho$ & AUC \\\\\n\\midrule\nVC & Structural & \\textbf{.379} & .684 & \\textbf{.350} & .693 & .424 & .789 & .426 & .709 \\\\\nSJ  & Structural & .360 & .692 & .250 & .670 & .436 & .801 & \\textbf{.431} & .704 \\\\\nFK & Surface & .267 & .629 & .275 & .609 & .400 & .774 & .428 & .703 \\\\\nEM  & Surface    & .295 & \\textbf{.749} & .134 & \\textbf{.706} & \\textbf{.451} & \\textbf{.816} & \\textbf{.431} & .705 \\\\\nLP     & Model      & .205 & .578 & .266 & .600 & .316 & .753 & .307 & \\textbf{.761} \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table*}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_signal_heatmap}\n\\caption{Quality estimation heatmap (Spearman $\\rho$) across five signals and four configurations. Left: full evaluation set; right: conditional set (non-zero F1 instances). On the full set, structural signals dominate on SciERC while all signals converge on CoNLL. On the conditional set, EM emerges as the strongest signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$), while LP RE collapses to near-zero ($\\rho{=}0.011$).}\n\\label{fig:signal_heatmap}\n\\end{figure*}\n\nTable~\\ref{tab:quality_estimation} presents rank correlation ($\\rho$) and AUROC for five confidence signals across tasks and models.\n\n\\paragraph{Difficulty-dependent signal complementarity.}\nOn SciERC NER (complex schema, 6 types), structural signals lead: VC achieves $\\rho{=}0.379$ and SJ $\\rho{=}0.360$, both outperforming surface ($\\rho{\\leq}0.295$) and LP ($\\rho{=}0.205$).\nThis advantage persists on RE (VC $\\rho{=}0.350$; preliminary, single benchmark), though all signals weaken due to the 40\\% zero-F1 floor effect.\nVC and SJ show moderate instance-level correlation (NER: $\\rho{=}0.659$; RE: $\\rho{=}0.605$), indicating information overlap but not redundancy; their differential behavior across difficulty levels reflects the complementary granularity of entity-level frequency vs.\\ span-level set overlap.\nWhile the best $\\rho{=}0.38$ (VC) explains approximately 14\\% of F1 variance, the best AUROC reaches 0.749 (EM), indicating strong binary discriminative power for the quality/failure classification most relevant to practitioners in quality-aware routing.\\footnote{For scale context, semantic entropy \\cite{kuhn2023semantic} achieves comparable AUROC on discrete-answer QA, though direct comparison is not meaningful due to fundamentally different output spaces and evaluation protocols.}\nPairwise bootstrap CIs confirm the SJ advantage over LP ($\\Delta\\rho{=}{+}0.155$, CI excludes zero) but not over EM ($\\Delta\\rho{=}{+}0.065$, marginal under Bonferroni correction; Table~\\ref{tab:bootstrap_signal_ci}, Appendix~\\ref{app:bootstrap_signal}).\n\n\\paragraph{$\\rho$--AUROC dissociation.}\nSignal choice depends on the intended use: on NER, EM leads AUROC (0.749) despite ranking third in $\\rho$ (0.295), preferred for binary quality triage; structural signals ($\\rho{\\geq}0.36$) are better for fine-grained ranking.\nOn CoNLL with LLaMA, LP leads AUROC (0.761) yet trails in $\\rho$ (0.307), confirming this pattern across datasets.\n\n\\paragraph{Signal rankings shift with task difficulty.}\nOn CoNLL (greedy F1${\\approx}$0.91), EM leads ($\\rho{=}0.451$, AUROC${=}0.816$), surpassing SJ and VC.\nWhen most samples are near-correct, binary agreement captures remaining variance more efficiently than set-level similarity.\nThis crossover---EM${>}$SJ on easy tasks vs.\\ SJ${>}$EM on hard tasks---demonstrates difficulty-dependent complementarity rather than a universal structural advantage, suggesting practitioners should match signal type to expected task difficulty.\nStability across the two model families (both 8B) is strong: SJ achieves $\\rho{=}0.436$ (Qwen) vs.\\ $0.431$ (LLaMA) on CoNLL ($\\Delta{=}0.005$, within 3-seed $\\sigma{\\approx}0.007$).\nOn WNUT-17, where 52\\% of instances receive zero F1, full-set correlations are misleading: VC achieves $\\rho{=}0.724$ (AUROC${=}0.913$), but this is entirely driven by the zero/non-zero boundary (conditional $\\rho{=}0.038$, n.s.; Table~\\ref{tab:wnut}).\nLP exhibits strong \\textit{negative} correlation ($\\rho{=}{-}0.410$, AUROC${=}0.219$).\nWe hypothesize that this reversal reflects overconfidence on out-of-distribution inputs \\citep{xiong2024llm}: the model assigns high log-probabilities to fluent but incorrect entity patterns (e.g., common noun phrases that resemble but do not match rare WNUT entity types), while producing lower scores for genuinely uncertain outputs where it correctly hedges.\nOn the conditional set, all signals collapse toward weak or non-significant correlations ($\\rho{\\leq}0.35$), with SJ achieving only $\\rho{=}0.089$ ($p{=}0.020$) on the full set---suggesting a capability boundary beyond which consistency signals capture binary success/failure but not quality gradation.\n\n\\paragraph{Conditional filtering.}\nFiltering to non-zero F1 instances reshuffles rankings (Figure~\\ref{fig:signal_heatmap}, right).\nEM emerges as the strongest conditional signal on both NER ($\\rho{=}0.360$) and RE ($\\rho{=}0.417$; preliminary), while VC and FK drop substantially (VC NER: $0.379{\\to}0.300$; FK NER: $0.267{\\to}0.176$).\nLP RE collapses to $\\rho{=}0.011$, confirming its full-set correlation was driven by zero/non-zero separation.\nThis creates a natural complementarity: VC and SJ are preferred on the full set, while EM provides the most precise ranking within the non-trivial subset (see Appendix~\\ref{app:additional} for details).\n\n%% ============================================================\n\\subsection{The Correlation-Selection Gap}\n\\label{sec:selection_gap}\n\n\\begin{figure*}[t]\n\\centering\n\\includegraphics[width=\\textwidth]{fig_selection_gap}\n\\caption{The correlation-selection gap on SciERC ($N{=}8$, $T{=}1.0$). Left: NER; right: RE. Bars show best-of-$N$ selection F1; the line marks quality estimation $\\rho$. Despite $\\rho$ up to 0.38, no signal significantly outperforms greedy on either task ($p{=}0.39$ for NER LP, the best signal; Table~\\ref{tab:selection}). Dashed line indicates oracle upper bound.}\n\\label{fig:selection_gap}\n\\end{figure*}\n\n\\begin{table}[t]\n\\centering\n\\small\n\\caption{Best-of-$N$ selection F1 on SciERC ($N{=}8$, $T{=}1.0$). RE results are from a single benchmark (preliminary). Best non-oracle result per column in \\textbf{bold}. EM selects the plurality output; despite a 42\\% pairwise exact-match rate, EM selection underperforms greedy on both tasks.}\n\\label{tab:selection}\n\\begin{tabular}{lcc}\n\\toprule\nMethod & NER F1 & RE F1 \\\\\n\\midrule\nOracle & 0.776 & 0.585 \\\\\n\\midrule\nLP           & \\textbf{0.650} & 0.395 \\\\\nSJ       & 0.645 & 0.386 \\\\\nEM        & 0.636 & 0.372 \\\\\nVC                 & 0.634 & 0.359 \\\\\n\\midrule\nGreedy ($T{=}0$)   & 0.644 & \\textbf{0.404} \\\\\nRandom             & 0.608 & 0.354 \\\\\n\\bottomrule\n\\end{tabular}\n\\end{table}\n\nDespite strong quality estimation, confidence signals yield limited gains when used for best-of-$N$ selection (Table~\\ref{tab:selection}, Figure~\\ref{fig:selection_gap}).\nFour of five signals are instance-level aggregates that assign a single score per input regardless of which sample is evaluated; they cannot rank candidates by construction.\nThe non-trivial question is whether log-probability---the only per-sample signal---can exploit the oracle headroom.\nWe anchor this analysis on SciERC, where output diversity is substantial: only 11--18\\% of instances produce identical outputs across all $N{=}8$ samples, with 39--43\\% unique outputs per instance (mean 3.5 distinct outputs), per-sample F1 standard deviation of 0.11--0.14, and mean pairwise SJ of 0.703.\n\n\\paragraph{No significant improvement over greedy.}\nWe exclude 22 instances with empty gold annotations ($n{=}529$) and evaluate significance via instance-level paired bootstrap resampling ($B{=}10{,}000$).\nOn NER, the oracle (0.776) reveals 13.2~pp of headroom above greedy (0.644).\nLP achieves the highest selection F1 (0.650, +0.6~pp), but this is not significant ($p{=}0.39$; 95\\% CI: [$-$3.0, +4.2]~pp; Cohen's $d{=}0.038$).\nOn RE, the best signal (LP, 0.395) falls below greedy (0.404, $-0.9$\\,pp, $p{=}0.80$), while 18.1~pp of oracle headroom remains.\nTOST equivalence testing confirms most signals are indistinguishable from greedy at ${\\pm}2$--$3$~pp on NER; on RE, EM and VC fail equivalence even at ${\\pm}5$~pp (Table~\\ref{tab:tost}, Appendix~\\ref{app:diversity}).\nVC ($\\rho{=}0.379$, the best quality estimator) selects to only 0.634 on NER---\\textit{below} greedy.\nThe gap extends to CoNLL (ceiling effect, 57--88\\% identical outputs) and WNUT-17 (capability boundary; Table~\\ref{tab:cross_selection}).\n\n\\paragraph{Quality estimation $\\neq$ output selection.}\nInstance-level confidence signals predict \\textit{which inputs} the model handles reliably, not \\textit{which output} among $N$ candidates is best.\nWhen per-sample variance is low relative to instance-level difficulty, even perfect quality estimation cannot discriminate among near-identical candidates.\nThis gap has direct consequences for test-time scaling in IE \\cite{brown2024monkeys, snell2024scaling}: closing it likely requires per-sample signals such as trained verifiers \\cite{cobbe2021verifiers}.\n\n%% ============================================================\n\\subsection{Robustness}\n\\label{sec:robustness_main}\n\nConsistency-based signals show robust performance across $T{\\in}\\{0.7, 1.0\\}$ (SJ NER $\\Delta\\rho{=}0.028$, bootstrap CI includes zero) and sublinear gains from $N{=}8$ to $N{=}16$, with structural signals maintaining their advantage over LP across all settings ($\\Delta\\rho{=}{+}0.135$ to ${+}0.175$; Table~\\ref{tab:robustness}, Appendix~\\ref{app:robustness}).\nNER signals are reasonably calibrated (ECE 0.069--0.096; Appendix~\\ref{app:calibration}), while RE miscalibration (ECE 0.109--0.339) and compound errors impose a ceiling at $\\rho{\\approx}0.28$ for $N{=}16$.\n",
      "numLines": 141,
      "startLine": 1,
      "totalLines": 141
    }
  },
  "sourceToolAssistantUUID": "753c1fd0-bb98-4209-bfe4-86999e236606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool result

_source line 526 · 2026-05-15T11:48:59.734Z_

<details><summary>↩ Tool result · `toolu_01A6SZ7hBLjunA9pBJA2m47n`</summary>

```text
1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	\usepackage{graphicx}
12	\usepackage{booktabs}
13	\usepackage{amsmath}
14	\usepackage{amssymb}
15	\usepackage{multirow}
16	\usepackage{xcolor}
17	\usepackage{subcaption}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Strong Predictors, Weak Selectors:\\ Why Confidence Signals Cannot Scale Structured Information Extraction}
22	
23	\author{Anonymous}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{sections/abstract}
29	\input{sections/introduction}
30	\input{sections/related_work}
31	\input{sections/method}
32	\input{sections/experiments}
33	\input{sections/discussion}
34	\input{sections/conclusion}
35	
36	\section*{Limitations}
37	\input{sections/limitations}
38	
39	\section*{Ethics Statement}
40	All experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).
41	CoNLL-2003 is based on the Reuters news corpus; we use the publicly available version and comply with its academic license terms.
42	No new human data was collected or annotated for this study.
43	Our findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.
44	
45	\bibliography{references}
46	
47	\appendix
48	\input{sections/appendix}
49	
50	\end{document}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebda362f-41b4-4753-8370-48bc9da3fec8",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "cc401418-e597-4aef-9ffc-a3f27e8cb410",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/main.tex",
      "content": "\\documentclass[11pt]{article}\n\n\\usepackage[review]{acl}\n\n\\usepackage{times}\n\\usepackage{latexsym}\n\\usepackage[T1]{fontenc}\n\\usepackage[utf8]{inputenc}\n\\usepackage{microtype}\n\\usepackage{inconsolata}\n\\usepackage{graphicx}\n\\usepackage{booktabs}\n\\usepackage{amsmath}\n\\usepackage{amssymb}\n\\usepackage{multirow}\n\\usepackage{xcolor}\n\\usepackage{subcaption}\n\n\\graphicspath{{figures/}}\n\n\\title{Strong Predictors, Weak Selectors:\\\\ Why Confidence Signals Cannot Scale Structured Information Extraction}\n\n\\author{Anonymous}\n\n\\begin{document}\n\\maketitle\n\n\\input{sections/abstract}\n\\input{sections/introduction}\n\\input{sections/related_work}\n\\input{sections/method}\n\\input{sections/experiments}\n\\input{sections/discussion}\n\\input{sections/conclusion}\n\n\\section*{Limitations}\n\\input{sections/limitations}\n\n\\section*{Ethics Statement}\nAll experiments use publicly available benchmarks (SciERC, CoNLL-2003, WNUT-17) and open-weight models (Qwen3-8B, LLaMA-3.1-8B).\nCoNLL-2003 is based on the Reuters news corpus; we use the publicly available version and comply with its academic license terms.\nNo new human data was collected or annotated for this study.\nOur findings on signal limitations could inform more reliable deployment of IE systems by guiding practitioners toward appropriate confidence signals for their use case.\n\n\\bibliography{references}\n\n\\appendix\n\\input{sections/appendix}\n\n\\end{document}",
      "numLines": 50,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "ebda362f-41b4-4753-8370-48bc9da3fec8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Tool call

_source line 527 · 2026-05-15T11:49:00.229Z_

<details open><summary>🔧 Tool call — Read · `toolu_01WPZM1opZMtRkt6nzqCsVJ2`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cc401418-e597-4aef-9ffc-a3f27e8cb410",
  "isSidechain": false,
  "requestId": "req_011Cb4JW7kb8AbTXkZC3ttNT",
  "type": "assistant",
  "uuid": "753c1fd0-bb98-4209-bfe4-86999e236606",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ct4MRGXjcvmNsP4FofRxjR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 19673,
      "cache_read_input_tokens": 82124,
      "output_tokens": 259,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 19673,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 259,
          "cache_read_input_tokens": 82124,
          "cache_creation_input_tokens": 19673,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 19673
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


### Runtime record

_source line 528_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Paper Agent 触发审查]: ## D072 Framing Update Review Request  **变更范围**: D072 将论文从 \"regime-specific bottleneck under constrained decoding\" 改为 \"universal correlation-selection gap\"。主要受影响章节: title, abstract…",
  "leafUuid": "8e5e903f-0802-458b-96f2-b9e5f8384007",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Runtime record

_source line 529_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker verification completion status",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Runtime record

_source line 530_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker verification completion status",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Runtime record

_source line 531 · 2026-05-15T11:51:40.285Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-15T11:51:40.285Z",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "content": "[系统通知 — worker_done:worker_code_exp_011_ood_cross_dataset_20260515T113645]:\nWorker worker_code_exp_011_ood_cross_dataset_20260515T113645 已完成（status=done），请审查 Agent 的处理结果。"
}
```

---


### Runtime record

_source line 532 · 2026-05-15T11:51:40.285Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-15T11:51:40.285Z",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


## Round 33

## Round 33

2 recorded events


### User

_source line 533 · 2026-05-15T11:51:40.275Z_

Continue from where you left off.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "8e5e903f-0802-458b-96f2-b9e5f8384007",
  "isSidechain": false,
  "promptId": "4b2b2b6c-8db8-44fa-a601-496b6d9efc1f",
  "type": "user",
  "isMeta": true,
  "uuid": "e7a12420-8ee4-46dc-8556-3b22925fe97e",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Assistant

_source line 534 · 2026-05-15T11:51:40.275Z_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7a12420-8ee4-46dc-8556-3b22925fe97e",
  "isSidechain": false,
  "type": "assistant",
  "uuid": "f4ed34c2-ad5f-491b-a97a-02d5a583f35f",
  "isApiErrorMessage": false,
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "id": "74e926b0-09fc-44c5-97ea-11078e7e2dc3",
    "container": null,
    "model": "&lt;synthetic>",
    "stop_reason": "stop_sequence",
    "stop_sequence": "",
    "type": "message",
    "usage": {
      "input_tokens": 0,
      "output_tokens": 0,
      "cache_creation_input_tokens": 0,
      "cache_read_input_tokens": 0,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": null,
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": null,
      "iterations": null,
      "speed": null
    },
    "context_management": null
  }
}
```

</details>

---


## Round 34

## Round 34

13 recorded events


### User

_source line 535 · 2026-05-15T11:51:40.373Z_

[系统通知 — worker_done:worker_code_exp_011_ood_cross_dataset_20260515T113645]:
Worker worker_code_exp_011_ood_cross_dataset_20260515T113645 已完成（status=done），请审查 Agent 的处理结果。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f4ed34c2-ad5f-491b-a97a-02d5a583f35f",
  "isSidechain": false,
  "promptId": "4b2b2b6c-8db8-44fa-a601-496b6d9efc1f",
  "type": "user",
  "uuid": "9d508bfc-72ae-47a9-aa19-f8bd80d2dbff",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Runtime record

_source line 536 · 2026-05-15T11:51:40.372Z_

```json
{
  "parentUuid": "9d508bfc-72ae-47a9-aa19-f8bd80d2dbff",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "31601fa2-7d90-4f2d-8ef7-8bfbfe70e82a",
  "timestamp": "2026-05-15T11:51:40.372Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

---


### Assistant

_source line 537 · 2026-05-15T11:52:33.535Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive view of the paper. Let me systematically go through the 7 audit points:

### Audit Point 1: Framing Consistency (regime-specific → universal gap)

Let me check for residual "regime-specific" or "specific to constrained decoding" claims:

**Abstract**: "A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding." ✓ Universal framing.

**Introduction**: 
- Line 19: "All experiments use constrained decoding, the regime under which structured IE is practically deployed." — This states a fact about the experimental setup, not a claim about the gap being regime-specific. OK.


- Line 26: "A controlled free-form decoding ablation confirms that this compression is intrinsic, not decoding-regime-specific." ✓
- Line 41 (Contribution 1): "A controlled ablation confirms that compression is intrinsic, not decoding-regime-specific." ✓

**Discussion**: The key passages consistently frame this as a fundamental challenge—the LP variance stays essentially flat at 0.97× and the tied fraction drops only 2 percentage points, while the Discussion section explicitly states "The correlation-selection gap is therefore a fundamental challenge for test-time scaling in structured IE, not an artifact of any particular decoding strategy." The section also uses "universal gap" language throughout. ✓

**Conclusion** and **Limitations**: Both reinforce that the free-form ablation on SciERC with Qwen3-8B confirms the compression persists without constrained decoding, though generalization to other datasets and model families remains open. ✓

**Appendix**: The logprob_ties section mirrors this finding—the ablation confirms intrinsic compression independent of decoding regime. ✓

The paper's title "Strong Predictors, Weak Selectors: Why Confidence Signals Cannot Scale" captures the core tension throughout.

Now I'm checking the Introduction for consistency. Line 19-20 states all experiments use constrained decoding since that's how structured IE is deployed in practice, but then the free-form ablation appears in line 26—which technically contradicts the "all experiments" claim. Let me trace through the exact wording to see if this needs clarification.

The footnote actually resolves this nicely by explaining that fine-tuned models can maintain format compliance without grammar constraints, and the free-form ablation achieves 99.95% valid JSON. So the statement "all experiments use constrained decoding" is referring to the primary experiments, while the ablation is properly distinguished as a separate analysis. This is a minor tension but acceptable given how it's framed.

The universality framing holds up—there's no residual claim that the gap is specific to constrained decoding. The ablation actually strengthens the universal gap argument rather than undermining it.

Now I'm checking the ablation paragraph claims against the actual data. The LP variance numbers check out—the ratio of free-form to constrained standard deviation is 0.966, which matches the reported 0.97×, and the tied fraction drops from 59.7% to 57.7% as stated. For the NER selection gains, I'm verifying that the constrained model shows +0.59 percentage points while free-form shows only +0.18 percentage points.

The parse rate claim of 99.95% with 4406/4408 instances parses correctly is confirmed in the ablation report. On the claim strength itself, I notice the discussion asserts that this "establishes LP compression as inherent to structured output generation," which is a fairly strong statement given it's based on a single dataset and model. The Limitations section does properly hedge this, and the follow-up about the correlation-selection gap being a "fundamental challenge" is appropriately cautious, so the overall framing holds up.

Moving into the next section about what drives the universal gap, I'm examining the RE LP selection analysis. I'm verifying the win/loss ratio shift holds across the data, then checking the relation density metrics and the substantial overlap between constrained and free-form non-tied sets, along with the expanded discrimination range in newly non-tied instances and the NER variance correlation improvements.

Now I'm cross-checking the specific claims about universality across relation types—the reversal only appears in seed42, so calling it "universal" technically means across all 7 relation types rather than all seeds, which is accurate but could be clearer. The Mann-Whitney test supports the variance reallocation mechanism, though "driven by" edges toward causal language that's acceptable given the context. The numbers check out overall, though some phrasing could be more precise about the scope of the findings.

Looking at the abstract, introduction, and conclusion statements about the ablation—they're essentially saying the same thing across all three sections, which is good for consistency. The contribution statement in the introduction is a shorter version of the same core claim, so everything aligns properly.

Now examining the title's claim strength. "Cannot Scale" is a pretty absolute statement, but the paper's scope is actually limited—just two 8B models tested on a handful of datasets (NER and RE tasks in English). The evidence shows current confidence signals fail at scaling, but the discussion mentions trained verifiers could potentially address this gap, so "Cannot" overstates the case. Similarly, claiming this holds for all "Structured Information Extraction" when only testing NER and RE is too broad. The title would be more accurate with softer language like "Fail to Scale" that reflects what the experiments actually demonstrate rather than making a universal impossibility claim.

That said, negative-result papers in NLP conferences often use provocative titles with "Cannot," and the subtitle "Strong Predictors, Weak Selectors" does capture the actual finding accurately. The paper explains the mechanism behind the failure, and the Limitations section does acknowledge the constraints around model scale and task scope. I'd flag this as a warning—the title pushes the boundaries of what the evidence supports, but it's not out of line for this venue.

Now checking the numerical consistency across sections, particularly the ablation data. The LP standard deviation ratio of 0.97× appears consistently in the Discussion's ablation section and should match what's in the Appendix tables.

The tied fraction numbers also check out: 59.7% to 57.7% is cited consistently across the Discussion and Appendix, while the Abstract's "60% of instances" is a rounded version of the constrained LP tied fraction, which aligns with how it's referenced in the Introduction. Everything tracks together properly. So the ablation analysis uses all 551 instances and shows 59.7% tied, while the NER-filtered subset of 529 instances shows 60.3% tied—the difference comes from 22 instances with empty gold annotations. The "60%" figure in the main text rounds from either value, so that's consistent. Now checking the parse rate: 4406/4408 equals 99.9546%, which rounds to 99.95%, and this matches across both the Discussion and Appendix.

Moving through the selection gaps, the NER results show +0.18 pp for free-form and +0.59 pp for constrained, while RE LP flips from −0.68 pp constrained to +1.69 pp free-form—all these numbers align with the appendix metrics. For the QE signals, the NER VC correlation improves from 0.379 to 0.409 across constrained and free-form conditions.

The limitations section properly acknowledges that the free-form ablation was restricted to SciERC with Qwen3-8B, leaving generalization across other datasets, model families, and scales as an open question. Now I'm checking the consistency of the N=16 three-seed data and RE multiseed results...

Looking at the robustness table in the appendix, the SJ N=16 correlation is reported as 0.412† with a footnote indicating it's the mean over 3 seeds (σ=0.025) with individual values of 0.428, 0.424, and 0.384. But when I cross-reference this against the n16_3seed_scs_analysis file, the individual seed values don't match—that analysis shows seed42=0.3984, seed123=0.4234, seed456=0.4098 with a mean of 0.4105, which is different from what the paper reports.

Let me verify the math on the paper's reported values: those three numbers (0.428, 0.424, 0.384) do average to 0.412 with a standard deviation around 0.024-0.025, which checks out. But the analysis file shows completely different individual values that produce a mean of 0.4105 and a much smaller standard deviation of 0.0102—these datasets are fundamentally inconsistent. I'm seeing the table structure now — the middle section shows sample size effects on Qwen SciERC, with SJ at N=16 achieving 0.412 for NER with those individual seed values (0.428, 0.424, 0.384), though there's still this discrepancy between the reported standard deviation of 0.025 and what my analysis calculated at 0.0102. There's a clear mismatch between the robustness tab values for SJ N=16 (0.428, 0.424, 0.384, mean=0.412, σ=0.025) and what the n16_3seed_scs_analysis shows (0.3984, 0.4234, 0.4098, mean=0.4105, σ=0.0102)—the older computation in the paper likely used different parameters or a different instance subset than the more recent analysis. I'm tracking down a genuine data inconsistency — the paper reports SJ N=16 as 0.412 with individual values of 0.428, 0.424, 0.384, but the latest analysis shows 0.4105 with 0.3984, 0.4234, 0.4098 instead. The RE values also diverge: paper says 0.281 while the current analysis gives 0.2758. I need to check the FK values next to see if there's a pattern here. I'm verifying the standard deviation calculations for the N16 analysis—the reported σ=0.0102 for SJ NER doesn't match what I'm getting when I compute it from the individual seed values, which gives me around 0.0125 instead.

Looking at the discrepancy more carefully, it seems the N16 report is using population standard deviation (dividing by 3) while the paper uses sample standard deviation (dividing by 2), which explains the difference. But the real problem here is that the actual values themselves don't match between the two sources—the paper reports (0.428, 0.424, 0.384) while the N16 analysis has (0.3984, 0.4234, 0.4098), which is a more fundamental inconsistency than just the statistical calculation method.

I should trace back through the analysis files to see if the paper's values came from an earlier version. The 3seed_5signal_tables.md file predates the N16 analysis, so it might contain the original numbers the paper used. This looks like exactly the kind of data mismatch the patch inventory was flagged to address—the paper still contains outdated values that need updating.

Now I'm checking the LLaMA CoNLL robustness metrics from the paper against what's in the registry, and the numbers are completely different scales—the paper shows values like 0.463 for SJ while the registry shows 0.1815, which suggests these might be measuring different things or the paper is using normalized scores. The paper's robustness table uses conditional analysis on instances with non-zero F1 scores, while the registry computes metrics across the full dataset — that's why the values diverge so dramatically. Looking at the actual analysis files confirms this: the LLaMA CoNLL N=16 data shows 2642 conditional instances out of 2756 total, and now I'm seeing similar discrepancies in the Qwen SciERC numbers where the paper reports 0.412 but the latest analysis shows slightly different individual seed values. Looking more carefully at the actual values, the paper's tab:robustness reports individual scores of 0.428, 0.424, and 0.384 with a mean of 0.412, but the n16_3seed_scs_analysis.md file shows 0.3984, 0.4234, 0.4098 with a mean of 0.4105 — there's a clear discrepancy in at least the first seed value that I need to investigate further. 424, 0.384. These values don't match any clear ordering, so let me compare what I'm seeing: the paper shows 0.428, 0.424, 0.384 in descending order, while the N16 analysis has 0.4234, 0.4098, 0.3984 across three seeds. The paper's robustness tab might be pulling from an earlier N=16 computation before the complete three-seed dataset was finalized. I'm flagging this discrepancy—the individual seed values are completely different even though the means are nearly identical (0.412 vs 0.411), and I notice the paper only compares SJ and FK at N=16 while the analysis includes all five signals. The RE values are also close but not exact (0.281 vs 0.2758).

Now I'm checking the multiseed tab to see if those values align better. The paper's Qwen row shows NER values across all five signals with their standard deviations, and comparing them to the markdown analysis, most are matching when rounded—LP, FK, and the others appear consistent, though I need to verify the full set. Now I'm verifying the multiseed stability metrics from the LLaMA NER table, checking that the rounded values match the full precision data across all five methods. Continuing to verify the Qwen results—SJ, VC, and EM all check out. Now I'm moving on to the NER AUROC metrics, comparing the paper's multiseed values against the stability table and confirming they match across LP, FK, and SJ so far. I'm verifying the LLaMA NER AUROC results match between the paper and table across all datasets, and they all check out. Now I need to look into the LLaMA SciERC correction mentioned in the paper's appendix about robustness. The patch has already been applied—the paper now shows the corrected values. I'm noticing the patch inventory was created today but the paper already contains the fresh data from exp_018, so either the patch was applied beforehand or the inventory became outdated quickly. Regardless, the current version is correct. Now I'm focusing on the main discrepancy I found: the tab:robustness section shows SJ N=16 NER at 0.412 overall but 0.428 for individual results, which needs investigation. The means are nearly identical, but the individual seed values diverge significantly—the paper reports much higher variance than my analysis. I'm wondering if the paper used a different methodology, perhaps computing correlation across all 551 instances rather than just the 529 with NER annotations, which would explain why instances without gold entities could skew the results. Let me check the other analysis files to see if I can trace where these values come from. I'm also noticing discrepancies in the FK values—the NER is off by 0.003 but the RE differs by 0.017, which is more significant. Looking at the paper's discussion of N-scaling in the robustness section, it references individual seed values for SJ that would need updating; with the new analysis, the reported gain drops slightly from +0.052 to +0.047, though the difference is minor.

This "+0.052" figure appears in multiple places throughout the paper—the Limitations section mentions it for SJ's improvement on Qwen SciERC NER, and the appendix's diminishing returns paragraph also cites it—so I need to track down all these references and update them consistently. The N=8 data checks out across all tables, but the N=16 data in the robustness tab is where the inconsistency originates, and I'm now compiling everything to address this systematically. The gain value would shift from "+0.052" to "+0.047" with the corrected N=16 numbers, which affects several downstream sections including the robustness scaling discussion and limitations. Now I'm checking whether constrained decoding is still being claimed as a cause of the performance gap — scanning through the introduction, discussion, ablation section, and appendix to verify it's properly ruled out rather than presented as an explanation.

Looking at the dimensional scores: the correlation-selection gap feels like a genuine contribution, and the ablation work that rules out decoding artifacts is novel. The paper is well-organized with consistent messaging across abstract, intro, and conclusion. The main soundness issues are the N=16 data inconsistency in the robustness table, a slightly overclaimed title, and the ablation being limited to a single seed and dataset, though these are appropriately caveated.

The significance is moderate—it's a negative result with diagnostic value that identifies a useful gap concept, but the practical impact is limited since it diagnoses rather than solves the problem. Overall, I'd rate this around 6-7: the paper has a clear narrative, solid experimental coverage for what it tests, and the framing transition is well-executed, though the data inconsistency needs correction.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8e5e903f-0802-458b-96f2-b9e5f8384007",
  "isSidechain": false,
  "requestId": "req_011Cb4JWghEqGvip8B5imeXS",
  "type": "assistant",
  "uuid": "882ecc60-befe-449d-b33d-7a6d81db141f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALDvcUZ9tK8V8AmcHf2mKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5605,
      "cache_read_input_tokens": 101797,
      "output_tokens": 11817,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11817,
          "cache_read_input_tokens": 101797,
          "cache_creation_input_tokens": 5605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5605
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


### Assistant

_source line 538 · 2026-05-15T11:52:33.537Z_

I need to check one more data source to verify a potential discrepancy in the N=16 values.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "882ecc60-befe-449d-b33d-7a6d81db141f",
  "isSidechain": false,
  "requestId": "req_011Cb4JWghEqGvip8B5imeXS",
  "type": "assistant",
  "uuid": "b3a30ae9-0a6e-4d44-8416-ae009209e7eb",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALDvcUZ9tK8V8AmcHf2mKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5605,
      "cache_read_input_tokens": 101797,
      "output_tokens": 11817,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11817,
          "cache_read_input_tokens": 101797,
          "cache_creation_input_tokens": 5605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5605
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

_source line 539 · 2026-05-15T11:52:35.023Z_

<details open><summary>🔧 Tool call — Read · `toolu_0151f3aG4YaLSmbkCuXdmEsS`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/3seed_summary/3seed_5signal_tables.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b3a30ae9-0a6e-4d44-8416-ae009209e7eb",
  "isSidechain": false,
  "requestId": "req_011Cb4JWghEqGvip8B5imeXS",
  "type": "assistant",
  "uuid": "aae8d7aa-f74c-439c-8a09-6b9788377669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01ALDvcUZ9tK8V8AmcHf2mKw",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5605,
      "cache_read_input_tokens": 101797,
      "output_tokens": 11817,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5605,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 11817,
          "cache_read_input_tokens": 101797,
          "cache_creation_input_tokens": 5605,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5605
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

_source line 540 · 2026-05-15T11:52:35.034Z_

<details><summary>↩ Tool result · `toolu_0151f3aG4YaLSmbkCuXdmEsS`</summary>

```text
1	# NER 3-Seed 5-Signal Summary (SciERC, N=16, T=1.0, 551 instances)
2	
3	## Table 1: Spearman ρ (Full, n=529)
4	
5	| Signal | seed42 | seed123 | seed456 | Mean | SD |
6	|-------------|--------|---------|---------|-------|-------|
7	| voting_conf | 0.441 | 0.413 | 0.411 | 0.422 | 0.017 |
8	| SJ | 0.428 | 0.424 | 0.384 | 0.412 | 0.025 |
9	| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |
10	| FK | 0.281 | 0.275 | 0.223 | 0.260 | 0.032 |
11	| logprob | 0.219 | 0.251 | 0.232 | 0.234 | 0.016 |
12	
13	## Table 2: Spearman ρ (Conditional, n≈477-479)
14	
15	| Signal | seed42 | seed123 | seed456 | Mean | SD |
16	|-------------|--------|---------|---------|-------|-------|
17	| EM | 0.415 | 0.404 | 0.406 | 0.408 | 0.006 |
18	| SJ | 0.369 | 0.376 | 0.349 | 0.365 | 0.014 |
19	| voting_conf | 0.353 | 0.339 | 0.346 | 0.346 | 0.007 |
20	| FK | 0.193 | 0.178 | 0.157 | 0.176 | 0.019 |
21	| logprob | 0.156 | 0.173 | 0.171 | 0.166 | 0.009 |
22	
23	## Table 3: AUROC (Full, n=529)
24	
25	| Signal | seed42 | seed123 | seed456 | Mean | SD |
26	|-------------|--------|---------|---------|-------|-------|
27	| EM | 0.790 | 0.781 | 0.768 | 0.780 | 0.011 |
28	| SJ | 0.737 | 0.736 | 0.711 | 0.728 | 0.015 |
29	| voting_conf | 0.734 | 0.717 | 0.712 | 0.721 | 0.012 |
30	| FK | 0.610 | 0.627 | 0.577 | 0.605 | 0.025 |
31	| logprob | 0.587 | 0.606 | 0.594 | 0.596 | 0.010 |
32	
33	## Table 4: AUROC (Conditional, n≈477-479)
34	
35	| Signal | seed42 | seed123 | seed456 | Mean | SD |
36	|-------------|--------|---------|---------|-------|-------|
37	| EM | 0.797 | 0.787 | 0.780 | 0.788 | 0.009 |
38	| SJ | 0.719 | 0.721 | 0.699 | 0.713 | 0.013 |
39	| voting_conf | 0.712 | 0.698 | 0.694 | 0.701 | 0.010 |
40	| FK | 0.589 | 0.605 | 0.561 | 0.585 | 0.023 |
41	| logprob | 0.569 | 0.584 | 0.576 | 0.577 | 0.008 |
42	
43	## Key Findings
44	
45	- **structural > surface: 3/3 seeds.** SJ beats FK in all seeds; all structure-based signals (EM, SJ, voting_conf) beat logprob.
46	- **Ranking stability:** Top-3 (EM, SJ, voting_conf) vs bottom-2 (FK, logprob) is perfectly consistent across all seeds and both splits.
47	- **Conditional split ranking is perfectly consistent:** EM > SJ > voting_conf > FK > logprob in all 3 seeds.
48	- **EM leads in AUROC** (0.780 full, 0.788 conditional) despite mid-tier ρ — it's the best binary discriminator.
49	- **voting_conf and SJ trade #1 in full ρ** — practically tied (0.422 vs 0.412), but SJ has higher SD (0.025 vs 0.017).
50	- **FK and logprob are the weakest signals** with mean ρ < 0.26 full, < 0.18 conditional.
51	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "aae8d7aa-f74c-439c-8a09-6b9788377669",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "8d60d54b-24f9-4bad-90b5-642e0ac8f003",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/artifacts/3seed_summary/3seed_5signal_tables.md",
      "content": "# NER 3-Seed 5-Signal Summary (SciERC, N=16, T=1.0, 551 instances)\n\n## Table 1: Spearman ρ (Full, n=529)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| voting_conf | 0.441 | 0.413 | 0.411 | 0.422 | 0.017 |\n| SJ | 0.428 | 0.424 | 0.384 | 0.412 | 0.025 |\n| EM | 0.335 | 0.337 | 0.316 | 0.329 | 0.011 |\n| FK | 0.281 | 0.275 | 0.223 | 0.260 | 0.032 |\n| logprob | 0.219 | 0.251 | 0.232 | 0.234 | 0.016 |\n\n## Table 2: Spearman ρ (Conditional, n≈477-479)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| EM | 0.415 | 0.404 | 0.406 | 0.408 | 0.006 |\n| SJ | 0.369 | 0.376 | 0.349 | 0.365 | 0.014 |\n| voting_conf | 0.353 | 0.339 | 0.346 | 0.346 | 0.007 |\n| FK | 0.193 | 0.178 | 0.157 | 0.176 | 0.019 |\n| logprob | 0.156 | 0.173 | 0.171 | 0.166 | 0.009 |\n\n## Table 3: AUROC (Full, n=529)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| EM | 0.790 | 0.781 | 0.768 | 0.780 | 0.011 |\n| SJ | 0.737 | 0.736 | 0.711 | 0.728 | 0.015 |\n| voting_conf | 0.734 | 0.717 | 0.712 | 0.721 | 0.012 |\n| FK | 0.610 | 0.627 | 0.577 | 0.605 | 0.025 |\n| logprob | 0.587 | 0.606 | 0.594 | 0.596 | 0.010 |\n\n## Table 4: AUROC (Conditional, n≈477-479)\n\n| Signal | seed42 | seed123 | seed456 | Mean | SD |\n|-------------|--------|---------|---------|-------|-------|\n| EM | 0.797 | 0.787 | 0.780 | 0.788 | 0.009 |\n| SJ | 0.719 | 0.721 | 0.699 | 0.713 | 0.013 |\n| voting_conf | 0.712 | 0.698 | 0.694 | 0.701 | 0.010 |\n| FK | 0.589 | 0.605 | 0.561 | 0.585 | 0.023 |\n| logprob | 0.569 | 0.584 | 0.576 | 0.577 | 0.008 |\n\n## Key Findings\n\n- **structural > surface: 3/3 seeds.** SJ beats FK in all seeds; all structure-based signals (EM, SJ, voting_conf) beat logprob.\n- **Ranking stability:** Top-3 (EM, SJ, voting_conf) vs bottom-2 (FK, logprob) is perfectly consistent across all seeds and both splits.\n- **Conditional split ranking is perfectly consistent:** EM > SJ > voting_conf > FK > logprob in all 3 seeds.\n- **EM leads in AUROC** (0.780 full, 0.788 conditional) despite mid-tier ρ — it's the best binary discriminator.\n- **voting_conf and SJ trade #1 in full ρ** — practically tied (0.422 vs 0.412), but SJ has higher SD (0.025 vs 0.017).\n- **FK and logprob are the weakest signals** with mean ρ < 0.26 full, < 0.18 conditional.\n",
      "numLines": 51,
      "startLine": 1,
      "totalLines": 51
    }
  },
  "sourceToolAssistantUUID": "aae8d7aa-f74c-439c-8a09-6b9788377669",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---


### Runtime record

_source line 541 · 2026-05-15T11:52:35.083Z_

```json
{
  "parentUuid": "8d60d54b-24f9-4bad-90b5-642e0ac8f003",
  "isSidechain": false,
  "attachment": {
    "type": "todo_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "1ef671fe-1780-4ff9-abdd-f990d322594b",
  "timestamp": "2026-05-15T11:52:35.083Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

---


### Runtime record

_source line 542_

```json
{
  "type": "last-prompt",
  "lastPrompt": "[Paper Agent 触发审查]: ## D072 Framing Update Review Request  **变更范围**: D072 将论文从 \"regime-specific bottleneck under constrained decoding\" 改为 \"universal correlation-selection gap\"。主要受影响章节: title, abstract…",
  "leafUuid": "1ef671fe-1780-4ff9-abdd-f990d322594b",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Runtime record

_source line 543_

```json
{
  "type": "ai-title",
  "aiTitle": "Review worker verification completion status",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9"
}
```

---


### Assistant

_source line 544 · 2026-05-15T11:53:18.309Z_

<details><summary>Logged reasoning block</summary>

```text
Now I see! The 3seed_5signal_tables.md has:
- SJ seed42=0.428, seed123=0.424, seed456=0.384, Mean=0.412, SD=0.025

This MATCHES the paper tab:robustness values exactly! So the paper used the 3seed_5signal_tables.md as its source.

But the n16_3seed_scs_analysis.md (created today) has different values:
- SJ seed42=0.3984, seed123=0.4234, seed456=0.4098, mean=0.4105, σ=0.0102


So I've got two different computations of the same metric—both supposedly measuring SJ Spearman ρ on N=16 Qwen SciERC NER across 529 instances, but with slightly different results. The older file from May 14 gives a mean of 0.412, while the newer one from May 15 gives 0.411. The discrepancy must come from how the computation script was implemented.

Looking deeper, I notice the voting confidence values also diverge between the two files—the May 14 version shows a mean of 0.422 while May 15 shows 0.4092. This suggests the underlying calculation methodology shifted between these dates, not just a minor rounding difference.

Since every signal changed systematically, I'm thinking this points to a fundamental shift in how the metrics were computed—whether that's a different implementation of the Spearman correlation, different filtering logic for what qualifies as a valid gold entity, or possibly a change in the reference metric being used for comparison.

The old 3seed_5signal_tables.md came from compute_3seed_summary.py, while the new n16_3seed_scs_analysis.md was generated by today's analysis worker. What's interesting is that the N=8 baseline appears consistent across multiple sources—the paper's multiseed tab and Table E both align—but the N=16 values diverge. The new analysis shows SJ improving by 0.0464 from N=8 to N=16, whereas the paper reported a 0.052 improvement using the older N=16 numbers, so I need to figure out which computation is actually correct. I'm checking the timestamps on the seed456 experiment — it was created May 14 but with a retry_count of 1, suggesting the first attempt failed and the successful run completed May 15. This means the old analysis from May 14 18:34 likely used incomplete or failed data for seed456, which would explain why that N=16 value (0.384 for SJ) differs from the newer computation.

The new analysis from today should be authoritative since all seeds have now completed successfully. Looking at the EM values across both analyses, seed42 and seed123 are fairly consistent between old and new, but seed456 shows a notable jump from 0.316 to 0.3363, confirming the old value was based on corrupted data. The robustness tab needs to be updated with these corrected values.

Checking the LP metrics reveals a more complex picture—seed42 and seed123 also show meaningful differences between the old and new runs, not just seed456, which suggests the discrepancy might stem from something broader than a single failed seed run.

Looking at the file headers, I notice the old summary references 551 instances while Table 1 in the paper cites 529—this could indicate different filtering criteria or instance selection methods were applied between the two analyses. Without access to the actual computation scripts, I can't definitively determine which version is correct, but this represents a critical data consistency problem that needs resolution before the paper can proceed with confidence in its reported numbers.

Now I need to compile all my findings and structure them according to the §5.3 template for this Paper Agent review.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1ef671fe-1780-4ff9-abdd-f990d322594b",
  "isSidechain": false,
  "requestId": "req_011Cb4JnWt5gFzV7T19sZyiq",
  "type": "assistant",
  "uuid": "6a17c8c0-4501-42ef-9d37-c9ff3a226776",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3PLvJ4dtGhgpdxYUSStJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13234,
      "cache_read_input_tokens": 107402,
      "output_tokens": 5717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5717,
          "cache_read_input_tokens": 107402,
          "cache_creation_input_tokens": 13234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13234
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


### Assistant

_source line 545 · 2026-05-15T11:53:19.181Z_

关键发现：paper tab:robustness 使用的 N=16 数值来自旧的 3seed_5signal_tables.md（5月14日），与今天的 n16_3seed_scs_analysis.md 存在系统性差异。需要确定哪组数据是权威来源。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a17c8c0-4501-42ef-9d37-c9ff3a226776",
  "isSidechain": false,
  "requestId": "req_011Cb4JnWt5gFzV7T19sZyiq",
  "type": "assistant",
  "uuid": "b59d667d-edd9-4701-94b6-91c5457d0cc8",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3PLvJ4dtGhgpdxYUSStJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13234,
      "cache_read_input_tokens": 107402,
      "output_tokens": 5717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5717,
          "cache_read_input_tokens": 107402,
          "cache_creation_input_tokens": 13234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13234
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

_source line 546 · 2026-05-15T11:54:34.725Z_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__reviewer_post_to_director · `toolu_016Pf3apMFiinuRJxUS9BBug`</summary>

```json
{
  "text": "## [写作评审] D072 Framing Update Review\n\n维度评分（1-4，4 为最好）：\n- Originality: 3     ← correlation-selection gap 概念和 free-form ablation 排除 decoding artifact 有贡献\n- Clarity: 3         ← 段落结构清晰，ablation 叙事从 Abstract→Intro→Discussion→Conclusion 一致\n- Soundness: 2       ← N=16 数值存在跨源不一致（见下方 critical），部分 claim 强度超出 evidence\n- Significance: 3    ← 对 test-time scaling in IE 的诊断价值实际，trained verifier 方向明确\n- Presentation: 3    ← 4-panel table 信息密度高，LP failure stability 表格有效\n\nOverall（1-10）: 5\n\n---\n\n## 审查点 1: Framing 一致性 (regime-specific → universal gap)\n\n**结论: PASS**\n\n全文已完整从 \"regime-specific\" 转为 \"universal gap\"。逐一核查：\n- Abstract L7: \"intrinsic to the model and task, not an artifact of constrained decoding\" ✓\n- Introduction L26: 同上 ✓\n- Contribution C1 L41: \"intrinsic, not decoding-regime-specific\" ✓\n- Discussion §ablation L28-29: \"fundamental challenge... not an artifact of any particular decoding strategy\" ✓\n- Discussion §universal gap L32: 段落标题 \"What drives the universal gap?\" ✓\n- Conclusion L6: 同上 ✓\n- Appendix logprob_ties: \"not decoding-regime-specific\" ✓\n\nIntroduction L20 \"All experiments use constrained decoding\" 是实验事实描述，不构成 gap 归因。无残留 regime-specific 声明。\n\n---\n\n## 审查点 2: 新增 ablation 段落数据准确性\n\n**结论: PASS (数值) + WARNING (claim 强度)**\n\n### §Score compression is task-inherent (Discussion L23-30)\n\n逐项验证（对照 freeform_ablation_results.md 和 ablation_report.json）：\n- LP std ratio 0.97×: 0.0199/0.0206=0.966 ≈ 0.97× ✓\n- Tied fraction 59.7%→57.7%: 原始数据完全匹配 ✓\n- NER selection +0.18pp vs +0.59pp: 0.0018 vs 0.0059 ✓\n- Parse rate 99.95%, 4406/4408: ✓\n\n### §What drives the universal gap? (Discussion L32-39)\n\n逐项验证（对照 freeform_ablation_deep_analysis.md）：\n- RE flip -0.68pp→+1.69pp: ✓\n- \"universal across all 7 relation types\": deep_analysis §1.1 确认 ✓\n- \"selective variance reallocation (p<0.0001)\": §1.5 Mann-Whitney test ✓\n- Win/loss 36:59→45:45: §1.6 ✓\n- \"mean 3.3 gold relations\": §1.4 flip instances 特征 ✓\n- Jaccard 0.472: §2.1 ✓\n- 87 instances newly gain: §2.1 ✓\n- 3× LP range increase: §2.2 (0.0321→0.0978) ✓\n- VC ρ 0.379→0.409: Panel C constrained=0.3792→free=0.4089 ≈ 0.379→0.409 ✓\n\n- [severity: warning] **\"a reversal that is universal across all 7 relation types\" — \"universal\" 在此指 7 种关系类型全部翻转。数据仅来自 seed=42 的单次 ablation。multiseed_flip_overlap_analysis 已确认 free-form 仅 seed42 可用。建议加 \"(seed=42)\" 修饰符或在段尾注明 single-seed caveat。**\n\n---\n\n## 审查点 3: Abstract/Intro/Conclusion ablation 一句话总结一致性\n\n**结论: PASS**\n\n三处措辞几乎相同：\n- Abstract L7: \"A controlled free-form decoding ablation confirms that score compression is intrinsic to the model and task, not an artifact of constrained decoding.\"\n- Introduction L26: 同上 + 引用 §ref\n- Conclusion L6: 同上\n\nContribution C1 (L41) 使用缩写 \"intrinsic, not decoding-regime-specific\" — 语义一致。\n\n---\n\n## 审查点 4: Title claim 强度\n\n**结论: WARNING**\n\n- [severity: warning] **Title \"Why Confidence Signals **Cannot** Scale Structured Information Extraction\" 中 \"Cannot\" 是不可能性声明，但论文实际证明的是\"5 个无监督信号在 2 个 8B 模型上 fail to scale\"。**\n  - Limitations L6 承认 \"whether our findings hold for larger models (70B+) or closed-source APIs remains untested\"\n  - Discussion L43 明确指出 \"trained verifiers\" 可能 close the gap\n  - \"Cannot\" 暗示原则性不可能，但论文结论是经验性失败 + 机制解释\n  - **建议**: \"Fail to\" 替代 \"Cannot\"，或保留 \"Cannot\" 但限定为 \"Cannot Yet\" / \"Do Not\"\n  - 注：NLP 顶会负面结果标题常用 provocative 措辞，不构成 dealbreaker，但审稿人可能攻击这一点\n\n---\n\n## 审查点 5: 数值跨章节一致性\n\n**结论: PASS（ablation 数据跨章节完全一致）**\n\n逐项核查：\n- \"60% tied\": Abstract/Intro/Discussion 均引用 60%（constrained NER ε=0.05 实际 60.3%，ablation 全集 59.7%）。四舍五入一致 ✓\n- LP std ratio 0.97×: Discussion L26 ✓\n- Tied 59.7%→57.7%: Discussion L26, Appendix Panel A ✓\n- Parse rate 99.95%: Discussion L25, Introduction footnote, Appendix Panel D ✓\n- NER/RE selection gaps: Discussion 与 Appendix Panel B ✓\n\n---\n\n## 审查点 6: Limitations ablation scope\n\n**结论: PASS**\n\nLimitations L16 正确标注：\"single dataset (SciERC) with one model (Qwen3-8B); whether the intrinsic compression finding generalizes to other datasets, model families, or model scales remains untested.\" 完整覆盖三个维度。\n\n---\n\n## 审查点 7: N=16 三种子数据与 RE multiseed 一致性\n\n**结论: CRITICAL**\n\n### 7a. tab:multiseed (N=8) — PASS\n\nPaper tab:multiseed 所有数值与 multi_seed_stability_table.md 交叉验证通过（逐个核对 10 行 × 5 信号 × mean/σ，全部匹配四舍五入后的值）。\n\nRE 行（Qwen only）已正确添加。LLaMA SciERC NER AUROC 行已添加。\n\n### 7b. LLaMA SciERC 数字更正（发现5）— PASS\n\n**已修正！** Paper appendix robustness 现在显示 SJ ρ=0.325±0.021, FK ρ=0.256±0.024（匹配 exp_018 fresh 数据），旧值 SJ=0.363, FK=0.327 已被替换。\n\n### 7c. tab:robustness N=16 数据 — CRITICAL\n\n- [severity: critical] **Paper tab:robustness 使用的 N=16 SJ 三种子数据来自旧源 `3seed_5signal_tables.md`（2026-05-14T18:34），与今天新计算的 `n16_3seed_scs_analysis.md`（2026-05-15T11:39）存在系统性差异。**\n\n  | Signal | 旧值(paper用) seed42/123/456 | 新值(n16分析) seed42/123/456 |\n  |--------|------------------------------|------------------------------|\n  | SJ | 0.428/0.424/0.384 (mean=0.412, σ=0.025) | 0.398/0.423/0.410 (mean=0.411, σ=0.010) |\n  | VC | 0.441/0.413/0.411 (mean=0.422, σ=0.017) | 0.399/0.384/0.445 (mean=0.409, σ=0.026) |\n  | EM | 0.335/0.337/0.316 (mean=0.329, σ=0.011) | 0.339/0.344/0.336 (mean=0.340, σ=0.003) |\n  | FK | 0.281/0.275/0.223 (mean=0.260, σ=0.032) | 0.288/0.290/0.272 (mean=0.283, σ=0.008) |\n  | LP | 0.219/0.251/0.232 (mean=0.234, σ=0.016) | 0.237/0.239/0.242 (mean=0.239, σ=0.002) |\n\n  **差异特征**：\n  - 两组计算均声称使用 n=529（gold entities non-empty），但个体种子值系统性不同\n  - 旧值 σ 普遍更大（SJ: 0.025 vs 0.010, FK: 0.032 vs 0.008）——旧计算可能使用了 seed456 失败重试前的不完整数据（registry 显示 exp_001_n16_seed456 retry_count=1，首次运行可能在旧分析时尚未正确完成）\n  - Mean 差异较小（SJ 0.412 vs 0.411），但 VC 排名翻转：旧值 VC>SJ (0.422 vs 0.412)，新值 SJ≈VC (0.411 vs 0.409)\n\n  **受影响位置**（如新值为正确值）：\n  1. `tab:robustness` 的 SJ N=16 行及脚注 (0.412→0.411, σ=0.025→0.010, individual values)\n  2. Appendix §Sample size scaling: \"SJ ρ rises from 0.360 to **0.412±0.025** (three seeds: **0.428, 0.424, 0.384**), a gain of **+0.052**\" → 需改为 0.411±0.010, gain=+0.047\n  3. Limitations L13: \"SJ improves by **+0.052** on Qwen SciERC NER\" → 需改为 +0.047\n  4. Appendix diminishing returns: \"SJ ρ improves by **+0.052** (Qwen SciERC, 3-seed mean)\" → 同上\n  5. FK N=16 RE: paper=0.279 vs n16分析=0.296（差 0.017）\n\n  **必须行动**: 确定哪组 N=16 计算是权威来源。我的判断：新分析（n16_3seed_scs_analysis.md）更可能正确，因为 (a) 在所有三个种子实验确认完成后计算，(b) 旧分析创建时 seed456 可能使用了首次失败运行的数据。建议 Worker 重新运行旧脚本验证，或直接采用新分析值更新论文。\n\n---\n\n## 其他发现\n\n- [severity: info] Appendix §LP Selection Failure Stability: 数据与 multiseed_flip_overlap_analysis.md 完全一致。Jaccard 0.42, stable failures 34 instances, flip instances 5 均正确。措辞 \"partially systematic\" 恰当。\n\n- [severity: info] Appendix freeform ablation 4-panel table: Panel A/B/C/D 所有数值此前已独立验证与 ablation_report.json 100% 一致。\n\n- [severity: info] Discussion §MBR 段落引用 eikema2025structured 的一致性发现——\"standard utility functions degrade on structured outputs\"。这个引用补充了论文叙事，但我无法独立验证该论文是否真实存在（2025 年出版物可能超出我的 verify 范围）。如有 reference-audit skill 可用，建议运行。",
  "project": "struct_self_consist_ie"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b59d667d-edd9-4701-94b6-91c5457d0cc8",
  "isSidechain": false,
  "requestId": "req_011Cb4JnWt5gFzV7T19sZyiq",
  "type": "assistant",
  "uuid": "c102ae76-1b88-4d1b-becb-cadfd7460d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01G3PLvJ4dtGhgpdxYUSStJM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 13234,
      "cache_read_input_tokens": 107402,
      "output_tokens": 5717,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13234,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 5717,
          "cache_read_input_tokens": 107402,
          "cache_creation_input_tokens": 13234,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13234
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

_source line 547 · 2026-05-15T11:54:38.634Z_

<details><summary>↩ Tool result · `toolu_016Pf3apMFiinuRJxUS9BBug`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c102ae76-1b88-4d1b-becb-cadfd7460d47",
  "isSidechain": false,
  "promptId": "2f85aa5a-385a-4139-b18a-71b898181743",
  "type": "user",
  "uuid": "72e8528a-372b-4a42-bcbd-4fec5bde35eb",
  "toolUseResult": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"director_session\\\": \\\"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\\\"}, \\\"error\\\": \\\"\\\"}\"}",
  "mcpMeta": {
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"director_session\": \"feishu:group:oc_1b56445332d8ca2b4964b30f300f0e00:director\"}, \"error\": \"\"}"
    }
  },
  "sourceToolAssistantUUID": "c102ae76-1b88-4d1b-becb-cadfd7460d47",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0514_1/projects/struct_self_consist_ie/.claude/sessions/reviewer_0064dd56",
  "sessionId": "87b5e1ab-0e84-4cd7-80a1-2356c4e5a8e9",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "slug": "wobbly-snuggling-unicorn"
}
```

</details>

---
