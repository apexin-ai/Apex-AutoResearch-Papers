# research sigma deep analysis

**collapse aware mixing** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 0
- **Tool calls:** 20
- **Original source:** `logs/workers/worker_research_sigma-deep-analysis_20260512T172849.log`
- **Structured JSON:** [`a3066490b076453c9199.json`](../../sessions/a3/a3066490b076453c9199.json)

## Before a recorded user message

56 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing",
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
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
  "uuid": "7e901ef6-035f-4a12-be9d-39d35338c8ce",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-18-projects-collapse-aware-mixing/memory/"
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
    "resetsAt": 1778612400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "a8383648-c80f-40ae-bce8-fe0f47b416d7",
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881"
}
```

---

### Assistant

_source line 4_

我先搜索 SIGMA 论文，然后读取我们项目的现有资料来做对比分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "0db4f371-a1f0-4fbd-bbb4-83a2c34abc20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bov4ctxcDhaRS3iBe2AdxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11294,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11294
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

_source line 5_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_014thCfqL32wtYmxLHENPpHd`</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
  "max_results": 4
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "af63b112-e86f-4492-a811-6058948a33c1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Bov4ctxcDhaRS3iBe2AdxF",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11294,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11294
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

_source line 6 · 2026-05-12T17:29:01.636Z_

<details><summary>↩ Tool result · `toolu_014thCfqL32wtYmxLHENPpHd`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "WebFetch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__read_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "02d08ab7-1bc7-4367-a707-511b9c3d7181",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "WebFetch",
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

<details><summary>Logged reasoning block</summary>

```text
Let me search for the SIGMA paper and read our project's existing materials in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "d9db43d3-41db-4b4b-b611-39e63801c1b3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFwQeNHWks6kEomCaVNYL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 23135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1732
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015KMtAA1pgAUmSVa9Hzffy1`</summary>

```json
{
  "query": "SIGMA spectral model collapse LLM 2026 Gram matrix"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "d45e4566-7f12-4785-ae96-f00a655d94f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFwQeNHWks6kEomCaVNYL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 23135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1732
      },
      "output_tokens": 18,
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

_source line 9_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GViBwECTDFvCMY8TKY6zx8`</summary>

```json
{
  "query": "SIGMA spectral indicator model collapse generative AI 2026 ICLR ICML NeurIPS arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "9e4e78b7-8af5-4d2f-b5d2-7d51f4ce1acd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFwQeNHWks6kEomCaVNYL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 23135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1732
      },
      "output_tokens": 18,
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

_source line 10_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01W2hXQhGX6UjsHFJ9kZVebw`</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "memory.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "1c3056a1-4214-450a-b4b6-adc8024288dc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFwQeNHWks6kEomCaVNYL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 23135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1732
      },
      "output_tokens": 18,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01DQbsRjjKNNyuttRBLzJnEw`</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "ideas.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "82793f7b-3968-483d-9783-899778dda18d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CFwQeNHWks6kEomCaVNYL5",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1732,
      "cache_read_input_tokens": 23135,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1732
      },
      "output_tokens": 18,
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

_source line 12 · 2026-05-12T17:29:12.768Z_

<details><summary>↩ Tool result · `toolu_015KMtAA1pgAUmSVa9Hzffy1`</summary>

```text
Web search results for query: "SIGMA spectral model collapse LLM 2026 Gram matrix"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"Predicting LLM Compression Degradation from Spectral Statistics","url":"https://arxiv.org/pdf/2604.18085"},{"title":"Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization","url":"https://arxiv.org/html/2605.05683"},{"title":"Downloads 2026","url":"https://iclr.cc/Downloads/2026"},{"title":"AI Updates Today (May 2026) – Latest AI Model Releases","url":"https://llm-stats.com/llm-updates"},{"title":"What is Model Collapse? Examples, Causes and Fixes","url":"https://www.analyticsvidhya.com/blog/2026/01/model-collapse/"},{"title":"Why Model Collapse In LLMs Is Inevitable With Self-Learning | Hackaday","url":"https://hackaday.com/2026/04/29/why-model-collapse-in-llms-is-inevitable-with-self-learning/"}]

Based on the search results, here's what I found about SIGMA and spectral model collapse in LLMs:

## SIGMA: Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

### Background on Model Collapse

Model collapse is a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

### The SIGMA Framework

By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space. Crucially, the stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models where full eigendecomposition is intractable.

### Key Features

The SIGMA metrics rely solely on output embeddings, allowing practitioners to track model collapse on deployed systems without accessing model weights or gradients.

The divergence between the conservative deterministic envelope and the sensitive stochastic scaling metric serves as a diagnostic signature for early-stage collapse, often preceding surface-level repetition artifacts.

The paper was submitted on January 6, 2026 and last revised on March 23, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "37a33fda-a6c1-4c4d-9968-3db27a3e27f7",
  "tool_use_result": {
    "query": "SIGMA spectral model collapse LLM 2026 Gram matrix",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EGqM8CxgwK7PFqHzAJpeBz",
        "content": [
          {
            "title": "[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/abs/2601.03385"
          },
          {
            "title": "SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://www.arxiv.org/pdf/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/html/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Collapse",
            "url": "https://arxiv.org/html/2601.03385v1"
          },
          {
            "title": "Predicting LLM Compression Degradation from Spectral Statistics",
            "url": "https://arxiv.org/pdf/2604.18085"
          },
          {
            "title": "Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization",
            "url": "https://arxiv.org/html/2605.05683"
          },
          {
            "title": "Downloads 2026",
            "url": "https://iclr.cc/Downloads/2026"
          },
          {
            "title": "AI Updates Today (May 2026) – Latest AI Model Releases",
            "url": "https://llm-stats.com/llm-updates"
          },
          {
            "title": "What is Model Collapse? Examples, Causes and Fixes",
            "url": "https://www.analyticsvidhya.com/blog/2026/01/model-collapse/"
          },
          {
            "title": "Why Model Collapse In LLMs Is Inevitable With Self-Learning | Hackaday",
            "url": "https://hackaday.com/2026/04/29/why-model-collapse-in-llms-is-inevitable-with-self-learning/"
          }
        ]
      },
      "Based on the search results, here's what I found about SIGMA and spectral model collapse in LLMs:\n\n## SIGMA: Spectral Insights for LLM Model Collapse\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.\n\n### Background on Model Collapse\n\nModel collapse is a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.\n\n### The SIGMA Framework\n\nBy deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space. Crucially, the stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models where full eigendecomposition is intractable.\n\n### Key Features\n\nThe SIGMA metrics rely solely on output embeddings, allowing practitioners to track model collapse on deployed systems without accessing model weights or gradients.\n\nThe divergence between the conservative deterministic envelope and the sensitive stochastic scaling metric serves as a diagnostic signature for early-stage collapse, often preceding surface-level repetition artifacts.\n\nThe paper was submitted on January 6, 2026 and last revised on March 23, 2026."
    ],
    "durationSeconds": 6.696541239999998
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-12T17:29:13.418Z_

<details><summary>↩ Tool result · `toolu_01GViBwECTDFvCMY8TKY6zx8`</summary>

```text
Web search results for query: "SIGMA spectral indicator model collapse generative AI 2026 ICLR ICML NeurIPS arXiv"

Links: [{"title":"[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/abs/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Model Collapse","url":"https://arxiv.org/html/2601.03385"},{"title":"Sigma: Scalable Spectral Insights for LLM Collapse","url":"https://arxiv.org/html/2601.03385v1"},{"title":"SIGMA: Scalable Spectral Insights for LLM Model Collapse","url":"https://www.arxiv.org/pdf/2601.03385v2"},{"title":"Model collapse - Wikipedia","url":"https://en.wikipedia.org/wiki/Model_collapse"},{"title":"Lazy Diffusion: Mitigating spectral collapse in generative diffusion-based stable autoregressive emulation of turbulent flows","url":"https://arxiv.org/html/2512.09572v1"},{"title":"Sigma AI — human context to accelerate next-gen AI - Sigma AI","url":"https://sigma.ai/"},{"title":"AI Model Collapse: Causes and Prevention - WitnessAI","url":"https://witness.ai/blog/ai-model-collapse/"},{"title":"AI Model Collapse: Causes, Early Signs, and How to Prevent It","url":"https://www.projectpro.io/article/ai-model-collapse/1177"},{"title":"An explanation of AI model collapse","url":"https://www.techtarget.com/whatis/video/An-explanation-of-AI-model-collapse"}]

I found relevant results about SIGMA! Here's what the search revealed:

## SIGMA: Scalable Spectral Insights for LLM Model Collapse

SIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.

### Key Features

SIGMA addresses "model collapse"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.

By deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space.

The stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models where full eigendecomposition is intractable.

### Practical Applications

SIGMA effectively captures the transition towards degenerate states, offering both theoretical insights into the mechanics of collapse and a practical, scalable tool for monitoring the health of recursive training pipelines.

### Publication Details

The paper was submitted to arXiv on January 6, 2026, with the latest version dated March 23, 2026. The paper is authored by Yi Gu and 6 other authors.

The research provides a scalable method for detecting model collapse in large language models by analyzing spectral properties rather than requiring full eigendecomposition of embedding matrices.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "4343bd1f-394b-4cb4-9b4e-9ba96123e788",
  "tool_use_result": {
    "query": "SIGMA spectral indicator model collapse generative AI 2026 ICLR ICML NeurIPS arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GmMkskLAupTDEh838HmoSu",
        "content": [
          {
            "title": "[2601.03385] SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/abs/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://arxiv.org/html/2601.03385"
          },
          {
            "title": "Sigma: Scalable Spectral Insights for LLM Collapse",
            "url": "https://arxiv.org/html/2601.03385v1"
          },
          {
            "title": "SIGMA: Scalable Spectral Insights for LLM Model Collapse",
            "url": "https://www.arxiv.org/pdf/2601.03385v2"
          },
          {
            "title": "Model collapse - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Model_collapse"
          },
          {
            "title": "Lazy Diffusion: Mitigating spectral collapse in generative diffusion-based stable autoregressive emulation of turbulent flows",
            "url": "https://arxiv.org/html/2512.09572v1"
          },
          {
            "title": "Sigma AI — human context to accelerate next-gen AI - Sigma AI",
            "url": "https://sigma.ai/"
          },
          {
            "title": "AI Model Collapse: Causes and Prevention - WitnessAI",
            "url": "https://witness.ai/blog/ai-model-collapse/"
          },
          {
            "title": "AI Model Collapse: Causes, Early Signs, and How to Prevent It",
            "url": "https://www.projectpro.io/article/ai-model-collapse/1177"
          },
          {
            "title": "An explanation of AI model collapse",
            "url": "https://www.techtarget.com/whatis/video/An-explanation-of-AI-model-collapse"
          }
        ]
      },
      "I found relevant results about SIGMA! Here's what the search revealed:\n\n## SIGMA: Scalable Spectral Insights for LLM Model Collapse\n\nSIGMA (Spectral Inequalities for Gram Matrix Analysis) is a unified framework that benchmarks model collapse through the spectral lens of the embedding Gram matrix.\n\n### Key Features\n\nSIGMA addresses \"model collapse\"—a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.\n\nBy deriving and utilizing deterministic and stochastic bounds on the matrix's spectrum, SIGMA provides a mathematically grounded metric to track the contraction of the representation space.\n\nThe stochastic formulation enables scalable estimation of these bounds, making the framework applicable to large-scale foundation models where full eigendecomposition is intractable.\n\n### Practical Applications\n\nSIGMA effectively captures the transition towards degenerate states, offering both theoretical insights into the mechanics of collapse and a practical, scalable tool for monitoring the health of recursive training pipelines.\n\n### Publication Details\n\nThe paper was submitted to arXiv on January 6, 2026, with the latest version dated March 23, 2026. The paper is authored by Yi Gu and 6 other authors.\n\nThe research provides a scalable method for detecting model collapse in large language models by analyzing spectral properties rather than requiring full eigendecomposition of embedding matrices."
    ],
    "durationSeconds": 6.884568610999999
  }
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-12T17:29:13.439Z_

<details><summary>↩ Tool result · `toolu_01W2hXQhGX6UjsHFJ9kZVebw`</summary>

````text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/memory.md\", \"content\": \"# Memory — collapse-aware-mixing\\n\\n## 竞争格局\\n\\n### SIGMA 已占据\\\"谱分析检测 collapse\\\"位置 (2026-05-12)\\nSIGMA (2026-01) 已将 Gram 矩阵谱分析用于 LLM model collapse 检测。**不能 claim \\\"首次将谱分析用于 collapse 检测\\\"。** 但 SIGMA 无控制机制、未验证 leading indicator。我们的 novelty = SIGMA 谱监控 + ERBP 理论动机 + EntroPIC PI 控制范式，首次组合成：谱有效秩 → PI 控制器 → 动态 real/synthetic 比例调节。推荐 framing：从 \\\"spectral metrics detect collapse\\\" → **\\\"from passive monitoring to active closed-loop control\\\"**。\\n\\n## 经验教训\\n\\n### 实验运行期间禁止修改依赖代码 (2026-05-12)\\nReviewer 指出：v5 pipeline 运行期间 Worker 修改了 metrics.py 和 pilot_pipeline.py。虽然当前 run 不受影响（进程已加载旧模块），但**今后实验进程运行期间不修改服务器上该实验依赖的代码文件**。新功能等 run 完成后再部署。\\n\\n### Pythia-1b + wikitext-103 + lr=1e-5 导致发散 (2026-05-12)\\nmvp_pilot_v4 在 G0 训练 760 步后 loss 维持 106-116（正常应为 2-4），PPL 溢出到 inf。独立诊断确认 ratio=1.00（非 transformers 报告 artifact，是真实发散）。grad_norm 43-113 无 NaN/Inf，训练速度稳定 2.08s/step，说明梯度计算正常但 loss landscape 不对。**lr=1e-5 对 Pythia-1b fine-tune wikitext-103 可能过大，下次考虑 2e-6 或更低。**\\n\\n### tmux + conda 环境激活 (2026-05-12)\\nsubmit_training_job 通过 tmux 执行命令，tmux 默认用 sh 而非 bash。bash -c 命令**必须**包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，否则 python3 找不到。mvp_pilot 因此崩溃。\\n\\n### AutoDL network_turbo 必须在 tmux 命令中显式激活 (2026-05-12)\\nsubmit_training_job 的命令在 tmux 新 session 中执行，不继承 Worker SSH session 的环境变量。因此 `source /etc/network_turbo` 必须写在 bash -c 命令里，否则 HuggingFace 不可达（`Errno 101: Network is unreachable`）。同时需设置：\\n- `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`\\n- `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`\\n- `HF_HUB_DISABLE_XET=1`\\n- `HF_HOME=/root/autodl-tmp/.hf_cache`\\n\\nmvp_pilot_v2 因此崩溃（tokenizer vocab_file 未缓存 → AttributeError）。\\n\\n### HF 数据集下载锁阻塞 (2026-05-12)\\ndry-run/测试后必须清理遗留 Python 进程，否则 HF dataset builder lock 会阻塞后续正式实验。PID 2371（测试用 `load_dataset('openwebtext')`）持锁 3.5+ 小时阻塞 mvp_pilot_v3。修复方法：`kill &lt;PID>` + 清理 `.lock` 和 `.incomplete` 文件。**提交正式实验前先 `ps aux | grep python` 检查遗留进程。**\\n\\n### flash_attention_2 → sdpa 回退 (2026-05-12)\\ncqa1-38874 上 flash-attn 编译失败（A6000 架构），train.py 已改用 sdpa（`attn_implementation=\\\"sdpa\\\"`）。\\n\\n### AutoDL 磁盘限制 (2026-05-12)\\n根分区 ~30GB，模型/数据/输出必须写 `/root/autodl-tmp/`。HF_HOME 也应指向数据盘。\\n\\n### pkill -f 自杀问题 (2026-05-12)\\n在 `bash -c \\\"...pkill -f pilot_pipeline...\\\"` 中执行 `pkill -f pilot_pipeline` 会匹配 bash 进程本身导致自杀（EXIT_CODE=129=128+SIGHUP）。解决方案：不在 submit_training_job 命令中包含 pkill，改用 kill_job 单独杀进程。\\n\\n### env_init.sh 简化启动 (2026-05-12)\\n将所有环境变量设置集中到 `/root/collapse-aware-mixing/env_init.sh`，launch script 只需 `source env_init.sh` 即可。减少命令长度和出错机会。\\n\\n## 代码决策\\n\\n### PI Controller 设计 (2026-05-12)\\n- 公式: `w_t = w_{t-1} - Kp*(r_t - r_{t-1}) - Ki*(r_t - r_target)`\\n- rank 下降 → w 增大（更多真实数据）；rank 恢复 → w 减小\\n- clamp 到 [w_min, w_max]，默认 [0.1, 0.9]\\n- 默认参数: Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5\\n\\n### AutoDL submit 命令模板 (2026-05-12)\\n```\\nbash -c \\\"source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; export HF_HOME=/root/autodl-tmp/.hf_cache; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/collapse-aware-mixing && python3 &lt;script> &lt;args> 2>&1 | tee /tmp/&lt;log>.log\\\"\\n```\\n\\n### logit KL divergence 待部署 (2026-05-12)\\n审计 Worker 已在服务器上补充了 `compute_logit_kl_divergence()`（metrics.py）和 pilot_pipeline.py 的 prev_model_dir 参数。但因 v5 运行中被修改，属违规操作。代码已在服务器上，v5 完成后的下一轮 run 自动生效。\\n\\n### analyze_g0.py 运行命令 (2026-05-12)\\n兼容性已验证通过。v5 完成后运行：\\n```\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\npython /root/collapse-aware-mixing/analyze_g0.py \\\\\\n    --checkpoint-dir /root/autodl-tmp/output/G0/training \\\\\\n    --output-dir /root/autodl-tmp/output/g0_analysis \\\\\\n    --model-name EleutherAI/pythia-1b\\n```\\n\\n## 服务器环境\\n\\n### cqa1-38874\\n- 1× RTX PRO 6000 96GB\\n- Python 3.12, PyTorch 2.10.0, transformers 4.57.6\\n- conda base 环境: `/root/miniconda3/`\\n- 项目代码: `/root/collapse-aware-mixing/`\\n- 输出目录: `/root/autodl-tmp/output/`\\n\", \"total_chars\": 3877, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "3df6e4f5-d284-4037-918e-a32951e02eaa",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/memory.md\\\", \\\"content\\\": \\\"# Memory — collapse-aware-mixing\\\\n\\\\n## 竞争格局\\\\n\\\\n### SIGMA 已占据\\\\\\\"谱分析检测 collapse\\\\\\\"位置 (2026-05-12)\\\\nSIGMA (2026-01) 已将 Gram 矩阵谱分析用于 LLM model collapse 检测。**不能 claim \\\\\\\"首次将谱分析用于 collapse 检测\\\\\\\"。** 但 SIGMA 无控制机制、未验证 leading indicator。我们的 novelty = SIGMA 谱监控 + ERBP 理论动机 + EntroPIC PI 控制范式，首次组合成：谱有效秩 → PI 控制器 → 动态 real/synthetic 比例调节。推荐 framing：从 \\\\\\\"spectral metrics detect collapse\\\\\\\" → **\\\\\\\"from passive monitoring to active closed-loop control\\\\\\\"**。\\\\n\\\\n## 经验教训\\\\n\\\\n### 实验运行期间禁止修改依赖代码 (2026-05-12)\\\\nReviewer 指出：v5 pipeline 运行期间 Worker 修改了 metrics.py 和 pilot_pipeline.py。虽然当前 run 不受影响（进程已加载旧模块），但**今后实验进程运行期间不修改服务器上该实验依赖的代码文件**。新功能等 run 完成后再部署。\\\\n\\\\n### Pythia-1b + wikitext-103 + lr=1e-5 导致发散 (2026-05-12)\\\\nmvp_pilot_v4 在 G0 训练 760 步后 loss 维持 106-116（正常应为 2-4），PPL 溢出到 inf。独立诊断确认 ratio=1.00（非 transformers 报告 artifact，是真实发散）。grad_norm 43-113 无 NaN/Inf，训练速度稳定 2.08s/step，说明梯度计算正常但 loss landscape 不对。**lr=1e-5 对 Pythia-1b fine-tune wikitext-103 可能过大，下次考虑 2e-6 或更低。**\\\\n\\\\n### tmux + conda 环境激活 (2026-05-12)\\\\nsubmit_training_job 通过 tmux 执行命令，tmux 默认用 sh 而非 bash。bash -c 命令**必须**包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，否则 python3 找不到。mvp_pilot 因此崩溃。\\\\n\\\\n### AutoDL network_turbo 必须在 tmux 命令中显式激活 (2026-05-12)\\\\nsubmit_training_job 的命令在 tmux 新 session 中执行，不继承 Worker SSH session 的环境变量。因此 `source /etc/network_turbo` 必须写在 bash -c 命令里，否则 HuggingFace 不可达（`Errno 101: Network is unreachable`）。同时需设置：\\\\n- `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`\\\\n- `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`\\\\n- `HF_HUB_DISABLE_XET=1`\\\\n- `HF_HOME=/root/autodl-tmp/.hf_cache`\\\\n\\\\nmvp_pilot_v2 因此崩溃（tokenizer vocab_file 未缓存 → AttributeError）。\\\\n\\\\n### HF 数据集下载锁阻塞 (2026-05-12)\\\\ndry-run/测试后必须清理遗留 Python 进程，否则 HF dataset builder lock 会阻塞后续正式实验。PID 2371（测试用 `load_dataset('openwebtext')`）持锁 3.5+ 小时阻塞 mvp_pilot_v3。修复方法：`kill &lt;PID>` + 清理 `.lock` 和 `.incomplete` 文件。**提交正式实验前先 `ps aux | grep python` 检查遗留进程。**\\\\n\\\\n### flash_attention_2 → sdpa 回退 (2026-05-12)\\\\ncqa1-38874 上 flash-attn 编译失败（A6000 架构），train.py 已改用 sdpa（`attn_implementation=\\\\\\\"sdpa\\\\\\\"`）。\\\\n\\\\n### AutoDL 磁盘限制 (2026-05-12)\\\\n根分区 ~30GB，模型/数据/输出必须写 `/root/autodl-tmp/`。HF_HOME 也应指向数据盘。\\\\n\\\\n### pkill -f 自杀问题 (2026-05-12)\\\\n在 `bash -c \\\\\\\"...pkill -f pilot_pipeline...\\\\\\\"` 中执行 `pkill -f pilot_pipeline` 会匹配 bash 进程本身导致自杀（EXIT_CODE=129=128+SIGHUP）。解决方案：不在 submit_training_job 命令中包含 pkill，改用 kill_job 单独杀进程。\\\\n\\\\n### env_init.sh 简化启动 (2026-05-12)\\\\n将所有环境变量设置集中到 `/root/collapse-aware-mixing/env_init.sh`，launch script 只需 `source env_init.sh` 即可。减少命令长度和出错机会。\\\\n\\\\n## 代码决策\\\\n\\\\n### PI Controller 设计 (2026-05-12)\\\\n- 公式: `w_t = w_{t-1} - Kp*(r_t - r_{t-1}) - Ki*(r_t - r_target)`\\\\n- rank 下降 → w 增大（更多真实数据）；rank 恢复 → w 减小\\\\n- clamp 到 [w_min, w_max]，默认 [0.1, 0.9]\\\\n- 默认参数: Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5\\\\n\\\\n### AutoDL submit 命令模板 (2026-05-12)\\\\n```\\\\nbash -c \\\\\\\"source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; export HF_HOME=/root/autodl-tmp/.hf_cache; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/collapse-aware-mixing && python3 &lt;script> &lt;args> 2>&1 | tee /tmp/&lt;log>.log\\\\\\\"\\\\n```\\\\n\\\\n### logit KL divergence 待部署 (2026-05-12)\\\\n审计 Worker 已在服务器上补充了 `compute_logit_kl_divergence()`（metrics.py）和 pilot_pipeline.py 的 prev_model_dir 参数。但因 v5 运行中被修改，属违规操作。代码已在服务器上，v5 完成后的下一轮 run 自动生效。\\\\n\\\\n### analyze_g0.py 运行命令 (2026-05-12)\\\\n兼容性已验证通过。v5 完成后运行：\\\\n```\\\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\\\npython /root/collapse-aware-mixing/analyze_g0.py \\\\\\\\\\\\n    --checkpoint-dir /root/autodl-tmp/output/G0/training \\\\\\\\\\\\n    --output-dir /root/autodl-tmp/output/g0_analysis \\\\\\\\\\\\n    --model-name EleutherAI/pythia-1b\\\\n```\\\\n\\\\n## 服务器环境\\\\n\\\\n### cqa1-38874\\\\n- 1× RTX PRO 6000 96GB\\\\n- Python 3.12, PyTorch 2.10.0, transformers 4.57.6\\\\n- conda base 环境: `/root/miniconda3/`\\\\n- 项目代码: `/root/collapse-aware-mixing/`\\\\n- 输出目录: `/root/autodl-tmp/output/`\\\\n\\\", \\\"total_chars\\\": 3877, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/memory.md\", \"content\": \"# Memory — collapse-aware-mixing\\n\\n## 竞争格局\\n\\n### SIGMA 已占据\\\"谱分析检测 collapse\\\"位置 (2026-05-12)\\nSIGMA (2026-01) 已将 Gram 矩阵谱分析用于 LLM model collapse 检测。**不能 claim \\\"首次将谱分析用于 collapse 检测\\\"。** 但 SIGMA 无控制机制、未验证 leading indicator。我们的 novelty = SIGMA 谱监控 + ERBP 理论动机 + EntroPIC PI 控制范式，首次组合成：谱有效秩 → PI 控制器 → 动态 real/synthetic 比例调节。推荐 framing：从 \\\"spectral metrics detect collapse\\\" → **\\\"from passive monitoring to active closed-loop control\\\"**。\\n\\n## 经验教训\\n\\n### 实验运行期间禁止修改依赖代码 (2026-05-12)\\nReviewer 指出：v5 pipeline 运行期间 Worker 修改了 metrics.py 和 pilot_pipeline.py。虽然当前 run 不受影响（进程已加载旧模块），但**今后实验进程运行期间不修改服务器上该实验依赖的代码文件**。新功能等 run 完成后再部署。\\n\\n### Pythia-1b + wikitext-103 + lr=1e-5 导致发散 (2026-05-12)\\nmvp_pilot_v4 在 G0 训练 760 步后 loss 维持 106-116（正常应为 2-4），PPL 溢出到 inf。独立诊断确认 ratio=1.00（非 transformers 报告 artifact，是真实发散）。grad_norm 43-113 无 NaN/Inf，训练速度稳定 2.08s/step，说明梯度计算正常但 loss landscape 不对。**lr=1e-5 对 Pythia-1b fine-tune wikitext-103 可能过大，下次考虑 2e-6 或更低。**\\n\\n### tmux + conda 环境激活 (2026-05-12)\\nsubmit_training_job 通过 tmux 执行命令，tmux 默认用 sh 而非 bash。bash -c 命令**必须**包含 `source /root/miniconda3/etc/profile.d/conda.sh && conda activate base`，否则 python3 找不到。mvp_pilot 因此崩溃。\\n\\n### AutoDL network_turbo 必须在 tmux 命令中显式激活 (2026-05-12)\\nsubmit_training_job 的命令在 tmux 新 session 中执行，不继承 Worker SSH session 的环境变量。因此 `source /etc/network_turbo` 必须写在 bash -c 命令里，否则 HuggingFace 不可达（`Errno 101: Network is unreachable`）。同时需设置：\\n- `REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt`\\n- `SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt`\\n- `HF_HUB_DISABLE_XET=1`\\n- `HF_HOME=/root/autodl-tmp/.hf_cache`\\n\\nmvp_pilot_v2 因此崩溃（tokenizer vocab_file 未缓存 → AttributeError）。\\n\\n### HF 数据集下载锁阻塞 (2026-05-12)\\ndry-run/测试后必须清理遗留 Python 进程，否则 HF dataset builder lock 会阻塞后续正式实验。PID 2371（测试用 `load_dataset('openwebtext')`）持锁 3.5+ 小时阻塞 mvp_pilot_v3。修复方法：`kill &lt;PID>` + 清理 `.lock` 和 `.incomplete` 文件。**提交正式实验前先 `ps aux | grep python` 检查遗留进程。**\\n\\n### flash_attention_2 → sdpa 回退 (2026-05-12)\\ncqa1-38874 上 flash-attn 编译失败（A6000 架构），train.py 已改用 sdpa（`attn_implementation=\\\"sdpa\\\"`）。\\n\\n### AutoDL 磁盘限制 (2026-05-12)\\n根分区 ~30GB，模型/数据/输出必须写 `/root/autodl-tmp/`。HF_HOME 也应指向数据盘。\\n\\n### pkill -f 自杀问题 (2026-05-12)\\n在 `bash -c \\\"...pkill -f pilot_pipeline...\\\"` 中执行 `pkill -f pilot_pipeline` 会匹配 bash 进程本身导致自杀（EXIT_CODE=129=128+SIGHUP）。解决方案：不在 submit_training_job 命令中包含 pkill，改用 kill_job 单独杀进程。\\n\\n### env_init.sh 简化启动 (2026-05-12)\\n将所有环境变量设置集中到 `/root/collapse-aware-mixing/env_init.sh`，launch script 只需 `source env_init.sh` 即可。减少命令长度和出错机会。\\n\\n## 代码决策\\n\\n### PI Controller 设计 (2026-05-12)\\n- 公式: `w_t = w_{t-1} - Kp*(r_t - r_{t-1}) - Ki*(r_t - r_target)`\\n- rank 下降 → w 增大（更多真实数据）；rank 恢复 → w 减小\\n- clamp 到 [w_min, w_max]，默认 [0.1, 0.9]\\n- 默认参数: Kp=0.01, Ki=0.005, r_target=50.0, w_init=0.5\\n\\n### AutoDL submit 命令模板 (2026-05-12)\\n```\\nbash -c \\\"source /etc/network_turbo 2>/dev/null; export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt; export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt; export HF_HUB_DISABLE_XET=1; export HF_HOME=/root/autodl-tmp/.hf_cache; source /root/miniconda3/etc/profile.d/conda.sh && conda activate base && cd /root/collapse-aware-mixing && python3 &lt;script> &lt;args> 2>&1 | tee /tmp/&lt;log>.log\\\"\\n```\\n\\n### logit KL divergence 待部署 (2026-05-12)\\n审计 Worker 已在服务器上补充了 `compute_logit_kl_divergence()`（metrics.py）和 pilot_pipeline.py 的 prev_model_dir 参数。但因 v5 运行中被修改，属违规操作。代码已在服务器上，v5 完成后的下一轮 run 自动生效。\\n\\n### analyze_g0.py 运行命令 (2026-05-12)\\n兼容性已验证通过。v5 完成后运行：\\n```\\nsource /root/miniconda3/etc/profile.d/conda.sh && conda activate base\\npython /root/collapse-aware-mixing/analyze_g0.py \\\\\\n    --checkpoint-dir /root/autodl-tmp/output/G0/training \\\\\\n    --output-dir /root/autodl-tmp/output/g0_analysis \\\\\\n    --model-name EleutherAI/pythia-1b\\n```\\n\\n## 服务器环境\\n\\n### cqa1-38874\\n- 1× RTX PRO 6000 96GB\\n- Python 3.12, PyTorch 2.10.0, transformers 4.57.6\\n- conda base 环境: `/root/miniconda3/`\\n- 项目代码: `/root/collapse-aware-mixing/`\\n- 输出目录: `/root/autodl-tmp/output/`\\n\", \"total_chars\": 3877, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
````

</details>

---

### Tool result

_source line 15 · 2026-05-12T17:29:13.454Z_

<details><summary>↩ Tool result · `toolu_01DQbsRjjKNNyuttRBLzJnEw`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'collapse-aware-mixing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "38c83178-6cb6-44de-b648-a2a34cf27d04",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No ideas.md found for 'collapse-aware-mixing'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No ideas.md found for 'collapse-aware-mixing'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 16_

<details><summary>Logged reasoning block</summary>

```text
I found the SIGMA paper on arXiv: 2601.03385. Let me fetch the full paper content and also read our project's ROADMAP and any other relevant files to understand our method better.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "8b22bc8e-44df-4930-9f7f-cefba59311c8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017c6PkZqUBr5JtjXygxjUyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4443,
      "cache_read_input_tokens": 24867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4443
      },
      "output_tokens": 9,
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

_source line 17_

找到了 SIGMA 论文 (arXiv:2601.03385)。现在获取论文详细内容和我们项目的更多资料。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "05a925be-4eef-49b2-8883-fd4efc8d09d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017c6PkZqUBr5JtjXygxjUyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4443,
      "cache_read_input_tokens": 24867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4443
      },
      "output_tokens": 9,
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

_source line 18_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01G6fj6KHDKjFksD1Syq9QAH`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03385",
  "prompt": "Extract the COMPLETE technical details of the SIGMA paper. I need:\n\n1. EXACT spectral metrics used (effective rank? spectral norm? condition number? eigenvalue distribution? what specific formula?)\n2. Which layers are analyzed (embedding layer only? all layers? specific layers?)\n3. The deterministic vs stochastic bounds - what exactly are they?\n4. Did they validate leading indicator properties? If so, what is the time lead over perplexity?\n5. Experimental setup: model sizes, datasets, number of training generations, batch sizes\n6. Do they propose any control mechanism or mitigation strategy? Or purely monitoring/detection?\n7. Their definition of the Gram matrix - is it token embeddings, or weight matrices?\n8. Key equations and theorems\n9. Limitations they acknowledge\n10. The \"scalable estimation\" method - how do they avoid full eigendecomposition?\n\nBe thorough - extract every technical detail available."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "6d79d47b-618e-4273-990b-3d6dc7e8af20",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017c6PkZqUBr5JtjXygxjUyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4443,
      "cache_read_input_tokens": 24867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4443
      },
      "output_tokens": 9,
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

_source line 19_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01Toi49CTvmmWSBoAhWeWpWd`</summary>

```json
{
  "url": "https://arxiv.org/abs/2601.03385",
  "prompt": "Extract: 1) Full list of authors and affiliations, 2) Complete abstract, 3) Publication venue (is it accepted at any conference like ICLR 2026, ICML 2026?), 4) Paper version history, 5) Any mentions of code availability or GitHub repo"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "d6d4becc-2716-427e-ad6c-7fbd83ad35f0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017c6PkZqUBr5JtjXygxjUyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4443,
      "cache_read_input_tokens": 24867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4443
      },
      "output_tokens": 9,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01L2pCaYWqbij1rRJKkGhkUv`</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "ROADMAP.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "15ccde7c-7b59-44e4-b71b-bb9733c2b237",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017c6PkZqUBr5JtjXygxjUyJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4443,
      "cache_read_input_tokens": 24867,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4443
      },
      "output_tokens": 9,
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

_source line 21 · 2026-05-12T17:29:34.628Z_

<details><summary>↩ Tool result · `toolu_01Toi49CTvmmWSBoAhWeWpWd`</summary>

```text
# SIGMA: Scalable Spectral Insights for LLM Model Collapse - Paper Details

## 1) Authors and Affiliations
The paper lists seven authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue. However, **specific institutional affiliations are not displayed on this abstract page**.

## 2) Complete Abstract
The authors present their framework as addressing "model collapse"—"a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality." They propose SIGMA, which uses "deterministic and stochastic bounds on the matrix's spectrum" to track representation space contraction and monitor "the health of recursive training pipelines."

## 3) Publication Venue
**No conference acceptance is mentioned.** The paper is posted on arXiv (identifier 2601.03385) as a preprint with the CS.LG (Machine Learning) classification. There is no indication of acceptance at ICLR 2026, ICML 2026, or any other venue.

## 4) Paper Version History
- **v1**: Submitted January 6, 2026 (122 KB)
- **v2**: January 19, 2026 (120 KB)
- **v3**: March 23, 2026 (120 KB) — current version

## 5) Code Availability
**No code repository or GitHub link is mentioned** on this abstract page. The page includes sections for code availability tools (alphaXiv, CatalyzeX, etc.), but none are populated with actual links.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "ba1c64f2-6559-44f5-a541-29ef6d39ac72",
  "tool_use_result": {
    "bytes": 48242,
    "code": 200,
    "codeText": "OK",
    "result": "# SIGMA: Scalable Spectral Insights for LLM Model Collapse - Paper Details\n\n## 1) Authors and Affiliations\nThe paper lists seven authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, and Alexander Aue. However, **specific institutional affiliations are not displayed on this abstract page**.\n\n## 2) Complete Abstract\nThe authors present their framework as addressing \"model collapse\"—\"a degenerative process where recursive training on model-generated content leads to a contraction of distributional variance and representational quality.\" They propose SIGMA, which uses \"deterministic and stochastic bounds on the matrix's spectrum\" to track representation space contraction and monitor \"the health of recursive training pipelines.\"\n\n## 3) Publication Venue\n**No conference acceptance is mentioned.** The paper is posted on arXiv (identifier 2601.03385) as a preprint with the CS.LG (Machine Learning) classification. There is no indication of acceptance at ICLR 2026, ICML 2026, or any other venue.\n\n## 4) Paper Version History\n- **v1**: Submitted January 6, 2026 (122 KB)\n- **v2**: January 19, 2026 (120 KB)\n- **v3**: March 23, 2026 (120 KB) — current version\n\n## 5) Code Availability\n**No code repository or GitHub link is mentioned** on this abstract page. The page includes sections for code availability tools (alphaXiv, CatalyzeX, etc.), but none are populated with actual links.",
    "durationMs": 6489,
    "url": "https://arxiv.org/abs/2601.03385"
  }
}
```

</details>

---

### Tool result

_source line 22 · 2026-05-12T17:29:45.324Z_

<details><summary>↩ Tool result · `toolu_01G6fj6KHDKjFksD1Syq9QAH`</summary>

````text
# Technical Details of the SIGMA Framework for LLM Model Collapse Detection

## 1. EXACT SPECTRAL METRICS

**Primary Metric: Log-Determinant of Gram Matrix**
The core metric is `log|G| = log(∏λⱼ) = Σlog(λⱼ)` where λⱼ are eigenvalues. Two derived diagnostics track collapse:

- **Track I (Deterministic)**: `𝒢_KF^(k)(δ) = log det(Im + 1/(β̂_k+δ) G_A^(k))`
- **Track II (Stochastic)**: `𝒰_LLN,cov^(k)(δ) = log det(G_A^(k)+δI_m) - m log n_A`

These measure eigenspectrum contraction without full decomposition.

## 2. LAYERS ANALYZED

The framework analyzes **embedding layers only**. Specifically, sentence embeddings X_i ∈ ℝ^m where m=384 (embedding dimension). The Gram matrix G=MM^T is constructed from embedding vectors, not weight matrices or hidden states.

## 3. DETERMINISTIC VS STOCHASTIC BOUNDS

**Theorem 1 (Deterministic Bound):**
```
det(G_A^(k)) ≤ det(G^(k)) ≤ ∏(λᵢ(G_A^(k)) + β_k)
```
where β_k = λ_max(G_B^(k)) is the spectral radius of unobserved data. Distribution-free but loose in practice.

**Theorem 2 (Stochastic Scaling Bound):**
```
det(G^(k)) ≤ K·(n_k/n_A)^m det(G_A)
```
Assumes i.i.d. column vectors from distribution with positive-definite covariance C. Enables scalable estimation.

**Theorem 3 (Error Estimation):**
Provides confidence intervals with precision scaling as `1/√n_A`, not total corpus size n_k.

## 4. LEADING INDICATOR VALIDATION

**No explicit time-lead analysis over perplexity is provided.** The paper evaluates Sigma metrics against model generation quality through two settings (S1: data recursion only; S2: data+weight recursion) but does not report quantitative lead times compared to standard language modeling loss metrics.

## 5. EXPERIMENTAL SETUP

| Parameter | Value |
|-----------|-------|
| Model | OPT-125M (facebook/opt-125m) |
| Dataset | TECH corpus (N=1000 contexts of 64 tokens) |
| Generations | 50 (g=0 to g=50) |
| Epochs/generation | 5 |
| Batch size | 16 |
| Learning rate | 2×10⁻⁵ |
| Synthetic fraction | α=0.0 (pure synthetic) |
| Embedding dimension (m) | 384 |
| Observed block size (n_A) | > m (specific value not stated) |

## 6. CONTROL MECHANISMS

The paper is **purely diagnostic/monitoring-focused**. No mitigation strategies or corrective mechanisms are proposed. Authors acknowledge future work: "Future Work aims to transition from monitoring states to predicting dynamics by viewing the LLM training loop through the lens of Koopman Operator Theory."

## 7. GRAM MATRIX DEFINITION

The Gram matrix is constructed from **token/sentence embeddings**, not weight matrices:
```
G^(k) := M^(k)(M^(k))^T = Σⱼ vⱼ^(k)(vⱼ^(k))^T ∈ S⁺^m
```
where M^(k) ∈ ℝ^(m×n_k) concatenates embedding vectors as columns. **Not weight matrices of the neural network.**

## 8. KEY EQUATIONS AND THEOREMS

**Theorem 1**: Deterministic spectral bound via Weyl's inequality and Ky Fan dominance

**Theorem 2**: Stochastic scaling law—full Gram determinant scales by (n_k/n_A)^m times observed sub-Gram determinant

**Theorem 3**: Central Limit Theorem for log-determinant estimation with explicit finite-sample error bounds

**Normalized Gain (Equation 3.18)**:
```
𝒢_KF^(k)(δ) = Σ log(1 + λᵢ(G_A^(k))/(β̂_k+δ))
```
Decreases monotonically as observed eigenvalues contract.

## 9. ACKNOWLEDGED LIMITATIONS

1. **Conservativeness of Track I**: Worst-case tail-energy budget β̂_k=(n_k-n_A)ρ can be loose for anisotropic covariance matrices
2. **Track II statistical dependence**: Law-of-Large-Numbers scaling assumes stationarity; may converge slowly under heavy-tailed distributions
3. **No weight-internal diagnostics**: Framework is "black-box friendly" but sacrifices access to gradient/activation information
4. **Modest data-only drift**: Under S1 (restart-from-base), Track II drifts ≈-0.94 per generation—gradual rather than sharp
5. **Lack of predictive power**: Paper measures collapse states but does not predict failure before output degradation becomes visible

## 10. SCALABLE ESTIMATION METHOD

**Avoids full eigendecomposition via sub-sampling:**

1. **Partial Gram Computation**: Compute G_A^(k) using only n_A > m observed columns, leaving n_k-n_A unobserved
2. **Log-Determinant via Cholesky**: Use `log det(S) = 2 Σ log L_ii` on regularized matrices G_A^(k) + δI_m (not eigenvalues)
3. **Scaling Correction**: Apply Theorem 2 scaling m log(n_k/n_A) to estimate full Gram determinant
4. **Computation Cost**: O(m³) Cholesky decomposition independent of total corpus size n_k

**Critical Insight (Equation 3.13):**
Estimation error depends on observed block size n_A, not unobserved corpus size n_k. Precision requirement `nA ≳ (z_α/2 σ/ε)²` for target precision ε.

---

## Additional Technical Notes

- **Regularization parameter δ > 0** is fixed across checkpoints to stabilize near singular matrices
- **Preprocessing enforces ‖vⱼ^(k)‖² ≤ ρ** to make tail-energy budget computable
- **Two-track design**: Track I (deterministic envelope) and Track II (statistical estimator) divergence signals early collapse before conservative bound tightens
- **Surface-form diagnostics** (Distinct-2 bigram ratio, n-gram HHI) provided for interpretability but not incorporated into collapse metric
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "01204bc5-382b-4f3e-bec5-299515bcad69",
  "tool_use_result": {
    "bytes": 512682,
    "code": 200,
    "codeText": "OK",
    "result": "# Technical Details of the SIGMA Framework for LLM Model Collapse Detection\n\n## 1. EXACT SPECTRAL METRICS\n\n**Primary Metric: Log-Determinant of Gram Matrix**\nThe core metric is `log|G| = log(∏λⱼ) = Σlog(λⱼ)` where λⱼ are eigenvalues. Two derived diagnostics track collapse:\n\n- **Track I (Deterministic)**: `𝒢_KF^(k)(δ) = log det(Im + 1/(β̂_k+δ) G_A^(k))`\n- **Track II (Stochastic)**: `𝒰_LLN,cov^(k)(δ) = log det(G_A^(k)+δI_m) - m log n_A`\n\nThese measure eigenspectrum contraction without full decomposition.\n\n## 2. LAYERS ANALYZED\n\nThe framework analyzes **embedding layers only**. Specifically, sentence embeddings X_i ∈ ℝ^m where m=384 (embedding dimension). The Gram matrix G=MM^T is constructed from embedding vectors, not weight matrices or hidden states.\n\n## 3. DETERMINISTIC VS STOCHASTIC BOUNDS\n\n**Theorem 1 (Deterministic Bound):**\n```\ndet(G_A^(k)) ≤ det(G^(k)) ≤ ∏(λᵢ(G_A^(k)) + β_k)\n```\nwhere β_k = λ_max(G_B^(k)) is the spectral radius of unobserved data. Distribution-free but loose in practice.\n\n**Theorem 2 (Stochastic Scaling Bound):**\n```\ndet(G^(k)) ≤ K·(n_k/n_A)^m det(G_A)\n```\nAssumes i.i.d. column vectors from distribution with positive-definite covariance C. Enables scalable estimation.\n\n**Theorem 3 (Error Estimation):**\nProvides confidence intervals with precision scaling as `1/√n_A`, not total corpus size n_k.\n\n## 4. LEADING INDICATOR VALIDATION\n\n**No explicit time-lead analysis over perplexity is provided.** The paper evaluates Sigma metrics against model generation quality through two settings (S1: data recursion only; S2: data+weight recursion) but does not report quantitative lead times compared to standard language modeling loss metrics.\n\n## 5. EXPERIMENTAL SETUP\n\n| Parameter | Value |\n|-----------|-------|\n| Model | OPT-125M (facebook/opt-125m) |\n| Dataset | TECH corpus (N=1000 contexts of 64 tokens) |\n| Generations | 50 (g=0 to g=50) |\n| Epochs/generation | 5 |\n| Batch size | 16 |\n| Learning rate | 2×10⁻⁵ |\n| Synthetic fraction | α=0.0 (pure synthetic) |\n| Embedding dimension (m) | 384 |\n| Observed block size (n_A) | > m (specific value not stated) |\n\n## 6. CONTROL MECHANISMS\n\nThe paper is **purely diagnostic/monitoring-focused**. No mitigation strategies or corrective mechanisms are proposed. Authors acknowledge future work: \"Future Work aims to transition from monitoring states to predicting dynamics by viewing the LLM training loop through the lens of Koopman Operator Theory.\"\n\n## 7. GRAM MATRIX DEFINITION\n\nThe Gram matrix is constructed from **token/sentence embeddings**, not weight matrices:\n```\nG^(k) := M^(k)(M^(k))^T = Σⱼ vⱼ^(k)(vⱼ^(k))^T ∈ S⁺^m\n```\nwhere M^(k) ∈ ℝ^(m×n_k) concatenates embedding vectors as columns. **Not weight matrices of the neural network.**\n\n## 8. KEY EQUATIONS AND THEOREMS\n\n**Theorem 1**: Deterministic spectral bound via Weyl's inequality and Ky Fan dominance\n\n**Theorem 2**: Stochastic scaling law—full Gram determinant scales by (n_k/n_A)^m times observed sub-Gram determinant\n\n**Theorem 3**: Central Limit Theorem for log-determinant estimation with explicit finite-sample error bounds\n\n**Normalized Gain (Equation 3.18)**:\n```\n𝒢_KF^(k)(δ) = Σ log(1 + λᵢ(G_A^(k))/(β̂_k+δ))\n```\nDecreases monotonically as observed eigenvalues contract.\n\n## 9. ACKNOWLEDGED LIMITATIONS\n\n1. **Conservativeness of Track I**: Worst-case tail-energy budget β̂_k=(n_k-n_A)ρ can be loose for anisotropic covariance matrices\n2. **Track II statistical dependence**: Law-of-Large-Numbers scaling assumes stationarity; may converge slowly under heavy-tailed distributions\n3. **No weight-internal diagnostics**: Framework is \"black-box friendly\" but sacrifices access to gradient/activation information\n4. **Modest data-only drift**: Under S1 (restart-from-base), Track II drifts ≈-0.94 per generation—gradual rather than sharp\n5. **Lack of predictive power**: Paper measures collapse states but does not predict failure before output degradation becomes visible\n\n## 10. SCALABLE ESTIMATION METHOD\n\n**Avoids full eigendecomposition via sub-sampling:**\n\n1. **Partial Gram Computation**: Compute G_A^(k) using only n_A > m observed columns, leaving n_k-n_A unobserved\n2. **Log-Determinant via Cholesky**: Use `log det(S) = 2 Σ log L_ii` on regularized matrices G_A^(k) + δI_m (not eigenvalues)\n3. **Scaling Correction**: Apply Theorem 2 scaling m log(n_k/n_A) to estimate full Gram determinant\n4. **Computation Cost**: O(m³) Cholesky decomposition independent of total corpus size n_k\n\n**Critical Insight (Equation 3.13):**\nEstimation error depends on observed block size n_A, not unobserved corpus size n_k. Precision requirement `nA ≳ (z_α/2 σ/ε)²` for target precision ε.\n\n---\n\n## Additional Technical Notes\n\n- **Regularization parameter δ > 0** is fixed across checkpoints to stabilize near singular matrices\n- **Preprocessing enforces ‖vⱼ^(k)‖² ≤ ρ** to make tail-energy budget computable\n- **Two-track design**: Track I (deterministic envelope) and Track II (statistical estimator) divergence signals early collapse before conservative bound tightens\n- **Surface-form diagnostics** (Distinct-2 bigram ratio, n-gram HHI) provided for interpretability but not incorporated into collapse metric",
    "durationMs": 20164,
    "url": "https://arxiv.org/html/2601.03385"
  }
}
````

</details>

---

### Tool result

_source line 23 · 2026-05-12T17:29:45.344Z_

<details><summary>↩ Tool result · `toolu_01L2pCaYWqbij1rRJKkGhkUv`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/ROADMAP.md\", \"content\": \"# collapse-aware-mixing — Research Dashboard\\n\\n> 最后更新: 2026-05-12 14:06 UTC | 更新原因: D003 数据切换 + 参数更新 + 基础设施教训记录\\n\\n## 核心方向\\n谱塌缩指标（embedding Gram 矩阵有效秩）驱动 PI 控制器，动态调节迭代 LLM 预训练中合成/真实数据混合比例。连接 SIGMA 的谱监控与 ERBP 的熵-储库框架，将被动监控升级为主动闭环控制。详见 IDEA_BRIEF.md。\\n\\n## 当前进展\\n- 阶段：MVP 验证\\n- 目标会议：EMNLP 2026 ARR（DDL 2026-05-25，剩 13 天）\\n- 实验：mvp_pilot v1/v2/v3 均失败（基础设施问题），v4 部署中\\n- 基础设施：cqa1-38874 1×RTX PRO 6000 96GB (cuda:0)\\n- ⚠️ GPU 空转 5+ 小时（09:05 至今）\\n\\n## MVP 验证方案（D003 更新）\\n**核心假设**：谱有效秩在迭代合成训练的 collapse 过程中，比 PPL 更早发出退化信号（leading indicator）。\\n\\n**实验设计**：Pythia-1B，3 代 × 100M tokens（D003: 从 500M 降至 100M），真实数据 wikitext-103-raw-v1（D003: 从 OpenWebText 切换），每 10M tokens 一个 checkpoint（每代 ~10 个 checkpoint）。\\n\\n**指标**：谱有效秩、token 级预测熵方差、n-gram 熵、词表覆盖率、PPL（held-out 真实数据）、代际 KL 散度（含完整分布报告）。\\n\\n### GO 标准（同时满足）\\n1. **谱领先性**：谱有效秩在某 checkpoint t 下降 ≥1σ（σ = G0 阶段 checkpoint 间有效秩的标准差），而此时 PPL 尚未从 G0 基线上升 ≥2 points（绝对值）或 ≥5%（相对值）\\n2. **非平稳性**：代际 KL 散度 > 0.1 nats（报告完整 KL 分布 + 阈值合理性说明）\\n\\n### NO-GO 决策树\\n| 场景 | 判定 | 行动 |\\n|------|------|------|\\n| 谱领先 + KL>0.1 | **GO** | 进入 research，primary framing（leading indicator → 闭环控制） |\\n| 谱与 PPL 同步下降，但谱粒度更细（CV 更小） | **Conditional GO** | pivot 到 secondary framing（higher-resolution indicator） |\\n| KL < 0.1 但 collapse 可测 | **延展** | 加 1 代观察；仍 < 0.1 → kill 自适应控制 claim |\\n| 谱不下降 / PPL 先于谱下降 | **KILL** | 谱指标对 autoregressive LLM collapse 无效 |\\n| 2 代内无 collapse 迹象 | **延展** | 扩到 3 代；仍无 → kill |\\n\\n**资源**：~1-2 GPU-hours（wikitext-103 规模）。\\n\\n## 代码状态\\n- ✅ pilot_pipeline.py（4 bug 修复）\\n- ✅ metrics.py（完整 KL 报告）\\n- ✅ controller.py（14/14 测试通过）\\n- ✅ main_experiment.py（3 bug 修复：optimizer state / KL / golden ratio）\\n- ✅ golden_ratio_baseline.py\\n- ✅ env_init.sh + preflight.sh（系统性修复）\\n- ✅ launch_pilot_v4.sh\\n\\n## 基础设施教训\\nv1-v3 连续崩溃暴露两个系统性缺陷（详见 Reviewer 复盘）：\\n1. 环境初始化未程序化 → 已修复：env_init.sh 标准 preamble\\n2. Worker 间无互斥 → 已缓解：preflight.sh pre-flight checklist\\n\\n## 近期任务\\n- [ ] ⚠️ mvp_pilot_v4 启动训练（最高优先级，GPU 空转中）\\n- [ ] MVP GO/NO-GO 判定\\n- [ ] MVP GO 后写 paper_framing.md + experiment_plan.yaml\\n\\n## GPU 预算\\n- MVP pilot：~1-2 GPU-hours（wikitext-103 规模）\\n- 全量实验（含 ablation）：~195-215 H100-hours\\n- 目标配置：8× H100（全量阶段需扩容）\\n- 当前：1×RTX PRO 6000 96GB @ cqa1-38874\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-12 | 文献调研确认 SIGMA 已占据\\\"谱分析检测 collapse\\\"，framing 方向确定为\\\"pas | mvp_pilot_v5 |\\n| D005 | 2026-05-12 | 确认真发散（ratio=1.00），v5 降 LR 至 2e-6 + warmup 0.05 重跑 | mvp_pilot_v4, mvp_pilot_v5 |\\n| D004 | 2026-05-12 | mvp_pilot_v4 发散确认，启动 v5 debug-first 方案 | mvp_pilot_v4 |\\n| D003 | 2026-05-12 | MVP 真实数据从 OpenWebText 切换到 wikitext-103，tokens_per_ | mvp_pilot, mvp_pilot_v2, mvp_pilot_v3 |\\n| D002 | 2026-05-12 | 量化 MVP GO/NO-GO 标准：PPL ≥2pts 或 ≥5% 为显著上升，谱领先 ≥1σ；补 | — |\\n| D001 | 2026-05-12 | MVP 方案：Phase 0 pilot 验证谱有效秩作为塌缩 leading indicator | — |\\n\\n\", \"total_chars\": 2721, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "914c9d94-7fef-48bd-ae03-4ffc04954998",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/ROADMAP.md\\\", \\\"content\\\": \\\"# collapse-aware-mixing — Research Dashboard\\\\n\\\\n> 最后更新: 2026-05-12 14:06 UTC | 更新原因: D003 数据切换 + 参数更新 + 基础设施教训记录\\\\n\\\\n## 核心方向\\\\n谱塌缩指标（embedding Gram 矩阵有效秩）驱动 PI 控制器，动态调节迭代 LLM 预训练中合成/真实数据混合比例。连接 SIGMA 的谱监控与 ERBP 的熵-储库框架，将被动监控升级为主动闭环控制。详见 IDEA_BRIEF.md。\\\\n\\\\n## 当前进展\\\\n- 阶段：MVP 验证\\\\n- 目标会议：EMNLP 2026 ARR（DDL 2026-05-25，剩 13 天）\\\\n- 实验：mvp_pilot v1/v2/v3 均失败（基础设施问题），v4 部署中\\\\n- 基础设施：cqa1-38874 1×RTX PRO 6000 96GB (cuda:0)\\\\n- ⚠️ GPU 空转 5+ 小时（09:05 至今）\\\\n\\\\n## MVP 验证方案（D003 更新）\\\\n**核心假设**：谱有效秩在迭代合成训练的 collapse 过程中，比 PPL 更早发出退化信号（leading indicator）。\\\\n\\\\n**实验设计**：Pythia-1B，3 代 × 100M tokens（D003: 从 500M 降至 100M），真实数据 wikitext-103-raw-v1（D003: 从 OpenWebText 切换），每 10M tokens 一个 checkpoint（每代 ~10 个 checkpoint）。\\\\n\\\\n**指标**：谱有效秩、token 级预测熵方差、n-gram 熵、词表覆盖率、PPL（held-out 真实数据）、代际 KL 散度（含完整分布报告）。\\\\n\\\\n### GO 标准（同时满足）\\\\n1. **谱领先性**：谱有效秩在某 checkpoint t 下降 ≥1σ（σ = G0 阶段 checkpoint 间有效秩的标准差），而此时 PPL 尚未从 G0 基线上升 ≥2 points（绝对值）或 ≥5%（相对值）\\\\n2. **非平稳性**：代际 KL 散度 > 0.1 nats（报告完整 KL 分布 + 阈值合理性说明）\\\\n\\\\n### NO-GO 决策树\\\\n| 场景 | 判定 | 行动 |\\\\n|------|------|------|\\\\n| 谱领先 + KL>0.1 | **GO** | 进入 research，primary framing（leading indicator → 闭环控制） |\\\\n| 谱与 PPL 同步下降，但谱粒度更细（CV 更小） | **Conditional GO** | pivot 到 secondary framing（higher-resolution indicator） |\\\\n| KL < 0.1 但 collapse 可测 | **延展** | 加 1 代观察；仍 < 0.1 → kill 自适应控制 claim |\\\\n| 谱不下降 / PPL 先于谱下降 | **KILL** | 谱指标对 autoregressive LLM collapse 无效 |\\\\n| 2 代内无 collapse 迹象 | **延展** | 扩到 3 代；仍无 → kill |\\\\n\\\\n**资源**：~1-2 GPU-hours（wikitext-103 规模）。\\\\n\\\\n## 代码状态\\\\n- ✅ pilot_pipeline.py（4 bug 修复）\\\\n- ✅ metrics.py（完整 KL 报告）\\\\n- ✅ controller.py（14/14 测试通过）\\\\n- ✅ main_experiment.py（3 bug 修复：optimizer state / KL / golden ratio）\\\\n- ✅ golden_ratio_baseline.py\\\\n- ✅ env_init.sh + preflight.sh（系统性修复）\\\\n- ✅ launch_pilot_v4.sh\\\\n\\\\n## 基础设施教训\\\\nv1-v3 连续崩溃暴露两个系统性缺陷（详见 Reviewer 复盘）：\\\\n1. 环境初始化未程序化 → 已修复：env_init.sh 标准 preamble\\\\n2. Worker 间无互斥 → 已缓解：preflight.sh pre-flight checklist\\\\n\\\\n## 近期任务\\\\n- [ ] ⚠️ mvp_pilot_v4 启动训练（最高优先级，GPU 空转中）\\\\n- [ ] MVP GO/NO-GO 判定\\\\n- [ ] MVP GO 后写 paper_framing.md + experiment_plan.yaml\\\\n\\\\n## GPU 预算\\\\n- MVP pilot：~1-2 GPU-hours（wikitext-103 规模）\\\\n- 全量实验（含 ablation）：~195-215 H100-hours\\\\n- 目标配置：8× H100（全量阶段需扩容）\\\\n- 当前：1×RTX PRO 6000 96GB @ cqa1-38874\\\\n\\\\n## 关键决策日志\\\\n\\\\n| ID | 日期 | 摘要 | 关联实验 |\\\\n|----|------|------|----------|\\\\n| D006 | 2026-05-12 | 文献调研确认 SIGMA 已占据\\\\\\\"谱分析检测 collapse\\\\\\\"，framing 方向确定为\\\\\\\"pas | mvp_pilot_v5 |\\\\n| D005 | 2026-05-12 | 确认真发散（ratio=1.00），v5 降 LR 至 2e-6 + warmup 0.05 重跑 | mvp_pilot_v4, mvp_pilot_v5 |\\\\n| D004 | 2026-05-12 | mvp_pilot_v4 发散确认，启动 v5 debug-first 方案 | mvp_pilot_v4 |\\\\n| D003 | 2026-05-12 | MVP 真实数据从 OpenWebText 切换到 wikitext-103，tokens_per_ | mvp_pilot, mvp_pilot_v2, mvp_pilot_v3 |\\\\n| D002 | 2026-05-12 | 量化 MVP GO/NO-GO 标准：PPL ≥2pts 或 ≥5% 为显著上升，谱领先 ≥1σ；补 | — |\\\\n| D001 | 2026-05-12 | MVP 方案：Phase 0 pilot 验证谱有效秩作为塌缩 leading indicator | — |\\\\n\\\\n\\\", \\\"total_chars\\\": 2721, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/ROADMAP.md\", \"content\": \"# collapse-aware-mixing — Research Dashboard\\n\\n> 最后更新: 2026-05-12 14:06 UTC | 更新原因: D003 数据切换 + 参数更新 + 基础设施教训记录\\n\\n## 核心方向\\n谱塌缩指标（embedding Gram 矩阵有效秩）驱动 PI 控制器，动态调节迭代 LLM 预训练中合成/真实数据混合比例。连接 SIGMA 的谱监控与 ERBP 的熵-储库框架，将被动监控升级为主动闭环控制。详见 IDEA_BRIEF.md。\\n\\n## 当前进展\\n- 阶段：MVP 验证\\n- 目标会议：EMNLP 2026 ARR（DDL 2026-05-25，剩 13 天）\\n- 实验：mvp_pilot v1/v2/v3 均失败（基础设施问题），v4 部署中\\n- 基础设施：cqa1-38874 1×RTX PRO 6000 96GB (cuda:0)\\n- ⚠️ GPU 空转 5+ 小时（09:05 至今）\\n\\n## MVP 验证方案（D003 更新）\\n**核心假设**：谱有效秩在迭代合成训练的 collapse 过程中，比 PPL 更早发出退化信号（leading indicator）。\\n\\n**实验设计**：Pythia-1B，3 代 × 100M tokens（D003: 从 500M 降至 100M），真实数据 wikitext-103-raw-v1（D003: 从 OpenWebText 切换），每 10M tokens 一个 checkpoint（每代 ~10 个 checkpoint）。\\n\\n**指标**：谱有效秩、token 级预测熵方差、n-gram 熵、词表覆盖率、PPL（held-out 真实数据）、代际 KL 散度（含完整分布报告）。\\n\\n### GO 标准（同时满足）\\n1. **谱领先性**：谱有效秩在某 checkpoint t 下降 ≥1σ（σ = G0 阶段 checkpoint 间有效秩的标准差），而此时 PPL 尚未从 G0 基线上升 ≥2 points（绝对值）或 ≥5%（相对值）\\n2. **非平稳性**：代际 KL 散度 > 0.1 nats（报告完整 KL 分布 + 阈值合理性说明）\\n\\n### NO-GO 决策树\\n| 场景 | 判定 | 行动 |\\n|------|------|------|\\n| 谱领先 + KL>0.1 | **GO** | 进入 research，primary framing（leading indicator → 闭环控制） |\\n| 谱与 PPL 同步下降，但谱粒度更细（CV 更小） | **Conditional GO** | pivot 到 secondary framing（higher-resolution indicator） |\\n| KL < 0.1 但 collapse 可测 | **延展** | 加 1 代观察；仍 < 0.1 → kill 自适应控制 claim |\\n| 谱不下降 / PPL 先于谱下降 | **KILL** | 谱指标对 autoregressive LLM collapse 无效 |\\n| 2 代内无 collapse 迹象 | **延展** | 扩到 3 代；仍无 → kill |\\n\\n**资源**：~1-2 GPU-hours（wikitext-103 规模）。\\n\\n## 代码状态\\n- ✅ pilot_pipeline.py（4 bug 修复）\\n- ✅ metrics.py（完整 KL 报告）\\n- ✅ controller.py（14/14 测试通过）\\n- ✅ main_experiment.py（3 bug 修复：optimizer state / KL / golden ratio）\\n- ✅ golden_ratio_baseline.py\\n- ✅ env_init.sh + preflight.sh（系统性修复）\\n- ✅ launch_pilot_v4.sh\\n\\n## 基础设施教训\\nv1-v3 连续崩溃暴露两个系统性缺陷（详见 Reviewer 复盘）：\\n1. 环境初始化未程序化 → 已修复：env_init.sh 标准 preamble\\n2. Worker 间无互斥 → 已缓解：preflight.sh pre-flight checklist\\n\\n## 近期任务\\n- [ ] ⚠️ mvp_pilot_v4 启动训练（最高优先级，GPU 空转中）\\n- [ ] MVP GO/NO-GO 判定\\n- [ ] MVP GO 后写 paper_framing.md + experiment_plan.yaml\\n\\n## GPU 预算\\n- MVP pilot：~1-2 GPU-hours（wikitext-103 规模）\\n- 全量实验（含 ablation）：~195-215 H100-hours\\n- 目标配置：8× H100（全量阶段需扩容）\\n- 当前：1×RTX PRO 6000 96GB @ cqa1-38874\\n\\n## 关键决策日志\\n\\n| ID | 日期 | 摘要 | 关联实验 |\\n|----|------|------|----------|\\n| D006 | 2026-05-12 | 文献调研确认 SIGMA 已占据\\\"谱分析检测 collapse\\\"，framing 方向确定为\\\"pas | mvp_pilot_v5 |\\n| D005 | 2026-05-12 | 确认真发散（ratio=1.00），v5 降 LR 至 2e-6 + warmup 0.05 重跑 | mvp_pilot_v4, mvp_pilot_v5 |\\n| D004 | 2026-05-12 | mvp_pilot_v4 发散确认，启动 v5 debug-first 方案 | mvp_pilot_v4 |\\n| D003 | 2026-05-12 | MVP 真实数据从 OpenWebText 切换到 wikitext-103，tokens_per_ | mvp_pilot, mvp_pilot_v2, mvp_pilot_v3 |\\n| D002 | 2026-05-12 | 量化 MVP GO/NO-GO 标准：PPL ≥2pts 或 ≥5% 为显著上升，谱领先 ≥1σ；补 | — |\\n| D001 | 2026-05-12 | MVP 方案：Phase 0 pilot 验证谱有效秩作为塌缩 leading indicator | — |\\n\\n\", \"total_chars\": 2721, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 24_

<details><summary>Logged reasoning block</summary>

```text
I now have very detailed information about SIGMA. Let me also try to get the full paper PDF for any additional details I might have missed, and read our project's paper_framing.md and any other relevant files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "7f151aa8-5a4e-4682-8090-888407e6c3aa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXLdxhzm9BAz9ffKEgqeNg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4949,
      "cache_read_input_tokens": 29310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4949
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

_source line 25_

获取了大量技术细节。再补充一些信息来完善分析。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "15f0a7b4-3978-4040-86e9-6f1c6e02290f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXLdxhzm9BAz9ffKEgqeNg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4949,
      "cache_read_input_tokens": 29310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4949
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

_source line 26_

<details open><summary>🔧 Tool call — WebFetch · `toolu_01FcNoRMf6VXzce7rtem8cVT`</summary>

```json
{
  "url": "https://arxiv.org/html/2601.03385",
  "prompt": "Extract ALL details about:\n1. The experimental results - what happens to Track I and Track II metrics across generations? Do they decline monotonically? What are the actual numerical values?\n2. Setting S1 vs S2 - what exactly is the difference? S1 is data recursion only, S2 is data+weight recursion - explain in detail\n3. Surface-form diagnostics mentioned (Distinct-2, HHI) - what do these show?\n4. The relationship between their spectral metrics and perplexity/loss - do they correlate? Is one earlier than the other?\n5. Their discussion of related work - what other spectral methods do they cite?\n6. Any mention of \"effective rank\", \"entropy\", \"PI controller\", \"control\", \"mixing ratio\", \"synthetic data ratio\", or \"data mixing\"\n7. The exact model architecture used (OPT-125M details)\n8. Future work section - what do they plan next?\n9. Any mention of ERBP, EntroPIC, or reservoir-based approaches\n10. Their theoretical contribution vs empirical contribution - which is stronger?"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "b980e112-2740-4767-b115-9e211d795267",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXLdxhzm9BAz9ffKEgqeNg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4949,
      "cache_read_input_tokens": 29310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4949
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

_source line 27_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01U2iMzhgHEyy4PUW3GRVeiD`</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "paper_framing.md",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "3d2a548f-6429-4268-9da2-2b5747ec622b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FXLdxhzm9BAz9ffKEgqeNg",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4949,
      "cache_read_input_tokens": 29310,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4949
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

_source line 28 · 2026-05-12T17:30:18.217Z_

<details><summary>↩ Tool result · `toolu_01FcNoRMf6VXzce7rtem8cVT`</summary>

```text
# Analysis of Sigma Paper: Key Details

## 1. Experimental Results

**Track II (Δ𝒰_LLN,cov)** shows dramatic decline in Setting S2:
- S1: final drift ≈ -151, slope ≈ -0.941 (gradual)
- S2: final drift ≈ -1537, slope ≈ -42.621 (steep acceleration)

**Track I (Δ𝒢_KF)** remains stable:
- S1: final drift ≈ -142, slope ≈ -0.918
- S2: final drift ≈ -2.426, slope ≈ +2.350 (near-flat or slightly positive)

The paper describes how "Track II contracts by more than an order of magnitude" in S2 while "Track I remains near zero," representing "early collapse" where observed spectrum contracts but the conservative envelope stays permissive.

## 2. Setting S1 vs S2 Detailed Comparison

**S1 (Restart-from-base):** "Each generation regenerates a fresh synthetic data pool, but training always restarts from the same base model." Isolates data recursion's effect without weight carryover.

**S2 (True recursion):** "We do not restart from a fixed base checkpoint. Instead, we carry the model weights forward across generations." Creates compounding feedback where parameters shaped by earlier generations influence subsequent synthetic generation.

The authors explain S2 exhibits "self-distillation" early on, quietly removing low-probability alternatives before outputs look obviously repetitive.

## 3. Surface-Form Diagnostics

**Distinct-2:** Ratio of unique bigrams to total bigrams. Lower values indicate increased short-range phrase reuse.

**HHI (n-gram):** Herfindahl-Hirschman Index over n-gram frequencies. Higher values indicate concentrated, repeated phrases—measuring whether few n-grams dominate the corpus.

The paper treats these as "contextual, not definitional" and does not claim they define collapse; they contextualize geometric contraction.

## 4. Relationship to Perplexity/Loss

**Not discussed in provided content.** The paper focuses purely on embedding Gram matrix spectral properties and surface-form repetition metrics. No correlation analysis with perplexity or training loss is reported. This appears to be a deliberate focus on representation geometry rather than task performance.

## 5. Related Work on Spectral Methods

The paper cites classical uses of the Gram matrix in NLP (Lodhi et al. 2002; Levy & Goldberg 2014) as "widely used in classical NLP as an intuitive method to encode variable quantities of natural language embeddings." However, the provided excerpt does not cite other recent spectral-analysis frameworks for collapse monitoring. Most citations address collapse phenomenology (Shumailov et al., Dohmatob et al., Seddik et al.) rather than spectral techniques.

## 6. Keywords: Effective Rank, Entropy, Control Structures

**Not found.** The paper does not mention effective rank, entropy, PI controller, mixing ratio, or control-theoretic approaches. It focuses on deterministic and stochastic spectral bounds rather than adaptive control or entropy-based monitoring.

## 7. Model Architecture

**OPT-125M** from Meta (facebook/opt-125m): 125 million parameters, fine-tuned with AdamW optimizer, learning rate 2×10⁻⁵, FP16 precision. Embeddings extracted with "frozen sentence encoder" at dimension m=384.

## 8. Future Work

Authors plan to "transition from monitoring states to predicting dynamics by viewing the LLM training loop through the lens of **Koopman Operator Theory**." The goal is to characterize eigenvalues of the Koopman operator to predict "asymptotic behaviors–such as the rate of convergence to degenerate fixed points" and identify "stable eigen-distributions that resist collapse."

## 9. ERBP, EntroPIC, Reservoir-Based Approaches

**Not mentioned.** The paper does not reference ERBP, EntroPIC, or reservoir-based methods.

## 10. Theoretical vs. Empirical Contribution

**Theoretical contribution is primary.** The paper derives three formal theorems (deterministic bound, stochastic scaling bound, stochastic error term) with rigorous proofs. Empirical validation is limited to a single controlled domain (TECH from DecayBench) with one model size. The authors explicitly state experiments use "fine-tuning to simulate the recursion loop" but acknowledge this is "validation" rather than comprehensive empirical breadth.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "21392975-36b8-426b-baff-6df2b20734df",
  "tool_use_result": {
    "bytes": 512682,
    "code": 200,
    "codeText": "OK",
    "result": "# Analysis of Sigma Paper: Key Details\n\n## 1. Experimental Results\n\n**Track II (Δ𝒰_LLN,cov)** shows dramatic decline in Setting S2:\n- S1: final drift ≈ -151, slope ≈ -0.941 (gradual)\n- S2: final drift ≈ -1537, slope ≈ -42.621 (steep acceleration)\n\n**Track I (Δ𝒢_KF)** remains stable:\n- S1: final drift ≈ -142, slope ≈ -0.918\n- S2: final drift ≈ -2.426, slope ≈ +2.350 (near-flat or slightly positive)\n\nThe paper describes how \"Track II contracts by more than an order of magnitude\" in S2 while \"Track I remains near zero,\" representing \"early collapse\" where observed spectrum contracts but the conservative envelope stays permissive.\n\n## 2. Setting S1 vs S2 Detailed Comparison\n\n**S1 (Restart-from-base):** \"Each generation regenerates a fresh synthetic data pool, but training always restarts from the same base model.\" Isolates data recursion's effect without weight carryover.\n\n**S2 (True recursion):** \"We do not restart from a fixed base checkpoint. Instead, we carry the model weights forward across generations.\" Creates compounding feedback where parameters shaped by earlier generations influence subsequent synthetic generation.\n\nThe authors explain S2 exhibits \"self-distillation\" early on, quietly removing low-probability alternatives before outputs look obviously repetitive.\n\n## 3. Surface-Form Diagnostics\n\n**Distinct-2:** Ratio of unique bigrams to total bigrams. Lower values indicate increased short-range phrase reuse.\n\n**HHI (n-gram):** Herfindahl-Hirschman Index over n-gram frequencies. Higher values indicate concentrated, repeated phrases—measuring whether few n-grams dominate the corpus.\n\nThe paper treats these as \"contextual, not definitional\" and does not claim they define collapse; they contextualize geometric contraction.\n\n## 4. Relationship to Perplexity/Loss\n\n**Not discussed in provided content.** The paper focuses purely on embedding Gram matrix spectral properties and surface-form repetition metrics. No correlation analysis with perplexity or training loss is reported. This appears to be a deliberate focus on representation geometry rather than task performance.\n\n## 5. Related Work on Spectral Methods\n\nThe paper cites classical uses of the Gram matrix in NLP (Lodhi et al. 2002; Levy & Goldberg 2014) as \"widely used in classical NLP as an intuitive method to encode variable quantities of natural language embeddings.\" However, the provided excerpt does not cite other recent spectral-analysis frameworks for collapse monitoring. Most citations address collapse phenomenology (Shumailov et al., Dohmatob et al., Seddik et al.) rather than spectral techniques.\n\n## 6. Keywords: Effective Rank, Entropy, Control Structures\n\n**Not found.** The paper does not mention effective rank, entropy, PI controller, mixing ratio, or control-theoretic approaches. It focuses on deterministic and stochastic spectral bounds rather than adaptive control or entropy-based monitoring.\n\n## 7. Model Architecture\n\n**OPT-125M** from Meta (facebook/opt-125m): 125 million parameters, fine-tuned with AdamW optimizer, learning rate 2×10⁻⁵, FP16 precision. Embeddings extracted with \"frozen sentence encoder\" at dimension m=384.\n\n## 8. Future Work\n\nAuthors plan to \"transition from monitoring states to predicting dynamics by viewing the LLM training loop through the lens of **Koopman Operator Theory**.\" The goal is to characterize eigenvalues of the Koopman operator to predict \"asymptotic behaviors–such as the rate of convergence to degenerate fixed points\" and identify \"stable eigen-distributions that resist collapse.\"\n\n## 9. ERBP, EntroPIC, Reservoir-Based Approaches\n\n**Not mentioned.** The paper does not reference ERBP, EntroPIC, or reservoir-based methods.\n\n## 10. Theoretical vs. Empirical Contribution\n\n**Theoretical contribution is primary.** The paper derives three formal theorems (deterministic bound, stochastic scaling bound, stochastic error term) with rigorous proofs. Empirical validation is limited to a single controlled domain (TECH from DecayBench) with one model size. The authors explicitly state experiments use \"fine-tuning to simulate the recursion loop\" but acknowledge this is \"validation\" rather than comprehensive empirical breadth.",
    "durationMs": 17440,
    "url": "https://arxiv.org/html/2601.03385"
  }
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-12T17:30:18.252Z_

<details><summary>↩ Tool result · `toolu_01U2iMzhgHEyy4PUW3GRVeiD`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_framing.md found for 'collapse-aware-mixing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "37ce069a-1f40-402a-8c5d-6f41c1e74e88",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No paper_framing.md found for 'collapse-aware-mixing'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No paper_framing.md found for 'collapse-aware-mixing'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 30_

<details><summary>Logged reasoning block</summary>

```text
Now I have very comprehensive information about SIGMA. Let me also read our project's IDEA_BRIEF.md and any existing literature map or architecture files.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "4d0e11d9-4895-4b6a-852d-6354081d8ad0",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FugUs4id4sFEkwZRx6iu1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 34259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1716
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

_source line 31_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MoV8criSgFQ4K28E6cjzan`</summary>

```json
{
  "project": "collapse-aware-mixing",
  "file": "literature_map.yaml",
  "max_chars": 12000
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "fafaf7a3-4be0-4adf-a2de-9891c85deb90",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FugUs4id4sFEkwZRx6iu1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 34259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1716
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

_source line 32 · 2026-05-12T17:30:25.682Z_

<details><summary>↩ Tool result · `toolu_01MoV8criSgFQ4K28E6cjzan`</summary>

```text
{"result":"{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'collapse-aware-mixing'.\", \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "9d518e56-6845-46ba-85be-08e9d3c6e613",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": false, \\\"data\\\": {}, \\\"error\\\": \\\"No literature_map.yaml found for 'collapse-aware-mixing'.\\\", \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": false, \"data\": {}, \"error\": \"No literature_map.yaml found for 'collapse-aware-mixing'.\", \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 33_

<details open><summary>🔧 Tool call — Glob · `toolu_011FW9kmGWXFFZqrQrZH5qoz`</summary>

```json
{
  "pattern": "**/IDEA_BRIEF*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "b1ca67f9-318c-4322-ad24-86630071616d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FugUs4id4sFEkwZRx6iu1S",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1716,
      "cache_read_input_tokens": 34259,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1716
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

_source line 34 · 2026-05-12T17:30:26.932Z_

<details><summary>↩ Tool result · `toolu_011FW9kmGWXFFZqrQrZH5qoz`</summary>

```text
docs/IDEA_BRIEF.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "62d893fc-fc13-4663-99ff-8981984d6e04",
  "tool_use_result": {
    "filenames": [
      "docs/IDEA_BRIEF.md"
    ],
    "durationMs": 14,
    "numFiles": 1,
    "truncated": false
  }
}
```

</details>

---

### Tool call

_source line 35_

<details open><summary>🔧 Tool call — Read · `toolu_01RKXabmEbZKG6AdduDyQMRt`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/docs/IDEA_BRIEF.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "da463216-214c-4a9c-aad2-c0498fb9e854",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DGDxVnk32FqiXUExhLSXAh",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 369,
      "cache_read_input_tokens": 35975,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 369
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

_source line 36 · 2026-05-12T17:30:29.811Z_

<details><summary>↩ Tool result · `toolu_01RKXabmEbZKG6AdduDyQMRt`</summary>

```text
1	# Idea Brief: Spectral Collapse-Aware Adaptive Mixing via Entropy-Reservoir PI Control for Iterative Synthetic-Real LLM Pretraining
2	
3	
4	- **Idea ID**: `idea_012`
5	- **Created**: 2026-05-12
6	- **Approved**: 2026-05-12
7	- **Source**: foreign:be-idea-gen-0509-4
8	- **Level**: top-tier
9	- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026) — primary target, 15 days from today. Three contributions: spectral collapse indicator for closed-loop control, PI-ERBP stability connection (tiered: design guidance guaranteed, formal proof aspirational), pilot-validated improvement margin via KL-based non-stationarity measurement., AAAI 2027 (deadline projected July-August 2026) — extended version with Tier 3 formal proof (if not achieved for EMNLP), formal κ/s_min bounds for specific architectures, additional conditions (ForTIFAI-TCE combination, AC-ODM comparison), and 6+ generation experiments, ICLR 2027 (estimated deadline September-October 2026) — alternative venue for extended version
10	
11	## Seed Topic
12	
13	Target: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme "New Missions for NLP Research" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.
14	
15	Direction: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.
16	
17	Contribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.
18	
19	HARD CONSTRAINTS:
20	1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.
21	2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.
22	3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.
23	
24	This is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.
25	
26	Tag: direction=data_governance, contribution_type=method. target_venues=["EMNLP 2026 Main", "EMNLP 2026 Findings"].
27	
28	## Core Problem
29	
30	Current approaches to mixing synthetic and real data in iterative LLM pretraining either use static ratios (golden-ratio weighting, fixed proportions) or apply generic online optimization (Aioli via loss-based feedback, GRAPE via minimax DRO) without monitoring for collapse-specific dynamics. Static mixing ratios — including the golden-ratio weighting (arXiv:2502.18049) — optimize over the restricted class of fixed weights: the golden ratio 1/φ minimizes asymptotic steady-state error as a constant weight across all generations under iterative dynamics where estimation error compounds via the recurrence Err̄(θ̂_t) = (1−w)²Err̄(θ̂_{t−1}) + [(1−w)²k + w²]tr(Σ₀⁻¹). However, a generation-dependent weight schedule w_t that allocates less real data early (when synthetic quality is high and the model is close to the true distribution) and more late (when drift has accumulated) can improve over any fixed weight — the classic static-vs-dynamic optimization gap. Bakshi & Chakraborty (arXiv:2602.10531) formalize the generation-specific structure via the recurrence R_t = (n_0/n_t)R_0 + ((n_t-1)/n_t)(1-α_t)² R_{t-1}, where the contamination propagation factor (1-α_t)² depends on generation-specific synthetic quality — their analysis of both fixed and decaying weight schedules motivates generation-dependent mixing, though they do not prove that static ratios are suboptimal. Training-objective modifications like truncated cross-entropy (ForTIFAI) and token-level editing (ToEdit) increase collapse tolerance but do not control data composition dynamically. While DCES monitors cluster dispersion for adaptive sampling in classification self-training, no existing method for autoregressive LLM pretraining uses online spectral collapse indicators to dynamically adjust the synthetic-to-real data ratio across model generations. Recent dynamic mixing methods optimize general domain proportions using loss or gradient signals that cannot distinguish between benign loss variation and collapse-induced representational narrowing. SIGMA (arXiv:2601.03385) demonstrates that spectral analysis of embedding Gram matrices can detect collapse onset in LLMs, but uses it only for monitoring, not for closed-loop control. The Topology Collapse Index (arXiv:2604.26984) mentions 'data mix adjustments' as a potential application but implements only monitoring without any feedback mechanism. DiSF (arXiv:2504.20644) uses eigenvalue uniformity for offline data file selection, and SSO (arXiv:2601.08393) enforces spectral constraints on weight matrices during optimization — both adjacent uses of spectral metrics that do not address online mixing ratio control. The ERBP framework (arXiv:2512.14879) proves that avoiding collapse in self-referential learning requires maintaining sufficient entropy-reservoir coupling — specifically, the condition λ·s_min > κ (where λ is the coupling coefficient, s_min is the entropy lower bound of the reservoir distribution, and κ is the optimization imperfection bound) — but provides no mechanism to dynamically adjust this coupling during training, and explicitly identifies the multi-round dynamics analysis as 'a significant theoretical undertaking and a key direction for future research.' Crucially, theoretical work (Barzilai & Shamir, ICML 2025; Bakshi & Chakraborty, 2026; ERBP, 2025) proves that avoiding collapse requires structural assumptions beyond MLE consistency — simply accumulating data is insufficient without monitoring whether those conditions hold and adjusting accordingly. Dynamic regret theory (Zinkevich, ICML 2003; Besbes et al., Operations Research 2015) establishes that any fixed policy incurs regret O(√(T·P_T)) where P_T is the path length (cumulative non-stationarity) — in iterative training where synthetic quality degrades across generations, P_T grows, making the improvement of an adaptive policy over any fixed policy increasingly significant. This motivates a controller that uses spectral collapse indicators to dynamically adjust the entropy-reservoir coupling (i.e., real data fraction) in a generation-aware manner, exploiting the static-vs-dynamic optimization gap that even the optimal fixed weight (golden ratio) cannot close.
31	
32	## Opportunity / Why Now
33	
34	Recent evidence shows model collapse is condition-dependent: rephrased synthetic data may not trigger collapse at foreseeable scales (Kang et al., EMNLP 2025), while model-generated content under replace workflows does degrade quality (Kazdan et al., ICML 2025). Schaeffer et al. (ICML 2025) further narrow the genuine threat to specific data workflows. Two recent theoretical advances create a precise opportunity: (1) The ERBP framework (arXiv:2512.14879) proves that self-referential training dynamics can be stabilized by an entropy reservoir with coupling satisfying λ·s_min > κ (where s_min is the reservoir's entropy lower bound and κ bounds optimization imperfection), providing closed-form rates and a sufficient condition for maintaining a non-trivial entropy floor — but does not prescribe how to dynamically set λ during training, and explicitly acknowledges that characterizing multi-round dynamics is an open problem. For the KL divergence generator (natural for language models), ERBP shows L_F = 1 analytically, simplifying the stability bound but leaving two empirical quantities: κ (optimization imperfection) and s_min (reservoir entropy). (2) SIGMA (arXiv:2601.03385) shows the log-determinant of the embedding Gram matrix provides scalable, early-warning spectral collapse detection in LLMs — Track II detects collapse substantially earlier than conservative Track I metrics, with over an order of magnitude more sensitivity — but uses this only for post-hoc monitoring, not active control. Together, these create a clear gap: a controller that monitors spectral collapse indicators and dynamically adjusts the entropy-reservoir coupling (real data fraction) to maintain the ERBP stability condition. The potential advantage of adaptive over fixed-weight control follows from the static-vs-dynamic optimization gap: the golden ratio (1/φ) is the optimal constant weight under the iterative error recurrence (arXiv:2502.18049), but it cannot respond to the actual per-generation synthetic quality. Early generations, where the model is still close to the true distribution, produce high-quality synthetic data requiring less real-data correction, while later generations accumulate drift requiring more. A generation-dependent weight schedule can exploit this structure. The expected magnitude of improvement depends on the degree of non-stationarity. Shumailov et al. (Nature 2024) report perplexity degradation of 20-28 points over 9 generations under pure replacement, indicating substantial non-stationarity. Dynamic mixing methods in the general domain setting (DoReMi, Aioli) show 0.3-12 perplexity point improvements and up to 6.5 percentage point downstream gains depending on distribution shift magnitude. However, when the static baseline is already near-optimal (as the golden ratio is, being derived under iterative dynamics), the adaptive advantage may be smaller — potentially <1 perplexity point in low-non-stationarity regimes. Our pilot (Phase 0) measures inter-generation KL divergence to quantify the actual non-stationarity in our setting, providing a concrete estimate of the expected improvement margin before committing to the full experiment. We define explicit success thresholds (see approach). Three recent dynamic mixing methods are conceptually related but use generic signals: Aioli (ICLR 2025, arXiv:2411.05735) uses loss-based online adaptation; GRAPE (NeurIPS 2025) uses minimax DRO for multi-target robustness. AC-ODM (arXiv:2505.23878) and TiKMiX (arXiv:2508.17677) proposed actor-critic RL and gradient-based Group Influence respectively, but both were withdrawn from ICLR 2026 review — we cite their technical approaches for completeness but note their unvalidated status. None monitors spectral representational health or connects to information-geometric stability conditions. Adjacent uses of spectral metrics for active training control exist — SSO (arXiv:2601.08393) enforces spectral constraints on weight matrices during LLM pretraining optimization, DiSF (arXiv:2504.20644) uses eigenvalue uniformity for offline data file selection, and the Topology Collapse Index (arXiv:2604.26984) mentions 'data mix adjustments' as a potential application but implements only monitoring — yet no published work integrates spectral collapse indicators into a closed-loop controller for dynamically adjusting the synthetic-to-real data ratio during iterative pretraining. A PI controller with spectral collapse-risk estimation fills this specific gap: classical control with well-understood stability properties (vs. RL without convergence guarantees), cheap inference-time spectral features (vs. gradient computation), and theoretically grounded collapse-specific signals connected to ERBP's sufficient stability condition (vs. generic loss). Feasible on Pythia-1B across 5 generations within ~190 H100-hours, targeting EMNLP 2026.
35	
36	## Landscape (SOTA & Limitations)
37	
38	**Static mixing approaches.** Golden ratio weighting (arXiv:2502.18049, Feb 2025) proves that weighting real data by 1/φ minimizes asymptotic steady-state error as a constant weight under iterative dynamics where estimation error compounds via the recurrence Err̄(θ̂_t) = (1−w)²Err̄(θ̂_{t−1}) + [(1−w)²k + w²]tr(Σ₀⁻¹) — applicable to Gaussian, GLM, and nonparametric settings. Crucially, this result optimizes over the restricted class of fixed weights: the paper models iterative training with compounding errors but does not analyze generation-dependent weight schedules w_t, leaving open whether adaptive weights can improve over the golden ratio. Preventing Model Collapse Under Overparametrization (arXiv:2509.22341) derives optimal static mixing ratios without adaptive adjustment. The accumulate strategy (Gerstgrasser et al., ICLR 2025) prevents collapse by retaining all prior data but does not optimize the mixing ratio. Bakshi & Chakraborty (arXiv:2602.10531) derive the recurrence R_t = (n_0/n_t)R_0 + ((n_t-1)/n_t)(1-α_t)²R_{t-1} and analyze both fixed (constant α) and decaying (α_t → 0) weight schedules, characterizing convergence conditions for each. Their analysis shows the contamination propagation factor (1-α_t)² depends on generation-specific synthetic quality, motivating generation-dependent weights — though they do not prove that static ratios are fundamentally suboptimal. The paper discusses 'naturally adaptive' weights in Appendix E as supplementary analysis and notes that estimating mixture weights in practice 'remains a challenge.'
39	
40	**Dynamic mixing approaches — generic.** Aioli (ICLR 2025, arXiv:2411.05735) dynamically adjusts domain proportions via loss-based signals, achieving 0.27-12.0 perplexity point improvements over static baselines depending on distribution shift magnitude — but targets general domain optimization rather than collapse dynamics. GRAPE (arXiv:2505.20380, NeurIPS 2025) uses minimax DRO for group-robust multi-target adaptive pretraining. DoReMi (NeurIPS 2023) achieves +6.5 percentage points average few-shot accuracy over The Pile's default domain weights (a known-suboptimal static baseline) and 2.6× convergence speedup. DoGraph (arXiv:2604.07963, Apr 2026) addresses domain weight optimization. AC-ODM (arXiv:2505.23878, May 2025) proposed actor-critic RL (DDPG) for dynamic domain weight adjustment, claiming 71% faster convergence — but was withdrawn from ICLR 2026. TiKMiX (arXiv:2508.17677, Aug 2025) proposed gradient-based Group Influence with 2% average gains at 20% of REGMIX's compute — also withdrawn from ICLR 2026. We cite AC-ODM and TiKMiX for their technical approaches (actor-critic and gradient-based control respectively) but note their unvalidated peer-review status; Aioli and GRAPE are the established accepted-paper baselines. Data Mixing Agent (arXiv:2507.15640, Jul 2025) learns RL-based domain reweighting for continual pretraining — targets catastrophic forgetting, not collapse. The data mixing survey (Chen et al., arXiv:2604.16380, Mar 2026) taxonomizes approaches, identifying limited transferability as a key open challenge. Next-Generation LLM Training (arXiv:2603.14712, Mar 2026) proposes a unified data-model interaction training system with dynamic data selection and reweighting, but does not use spectral collapse indicators or address synthetic-vs-real mixing.
41	
42	**PID control in machine learning.** An et al. (CVPR 2018) established PID control for deep network optimization, framing PID-inspired approaches as 'motivated by the outstanding performance of PID controllers in automatic control' — providing design intuition from control theory with empirical validation, rather than closed-loop stability proofs for nonlinear DNN dynamics (up to 50% training acceleration). PIDAO (Chen et al., Nature Communications 2024) extends this with formal convergence analysis for convex objectives. Li et al. (arXiv:1908.10920, 2019) frame deep learning as optimal control for 'principled guidance for architecture and algorithm design.' All apply PID to optimizer dynamics (parameter updates), not to data composition. Recent work on data-driven adaptive PID (arXiv:2510.04591, Oct 2025) demonstrates physics-informed approaches to stability-guaranteed PID tuning. Beyond Quadratic Costs (arXiv:2505.00319, 2025) derives stabilizing controllers using Bregman divergence cost functions via Riccati-like identities.
43	
44	**Collapse-specific methods — surface metrics.** DCES (Electronics, Feb 2026) monitors intra-cluster dispersion for adaptive sampling in classification. ForTIFAI (arXiv:2509.08972, Sep 2025) introduces TCE loss achieving 2.3× greater collapse tolerance, modifying training objectives rather than data composition. ToEdit (arXiv:2412.14689, ICML 2025) proposes token-level editing with theoretical guarantees — operates on data synthesis rather than mixing ratio control, making it complementary. Surplexity (arXiv:2410.12341, Oct 2024) provides perplexity-based surprise metrics for offline data filtering.
45	
46	**Collapse-specific methods — spectral, topological, and information-geometric.** SIGMA (arXiv:2601.03385, Jan 2026) introduces spectral analysis of the embedding Gram matrix for scalable LLM collapse monitoring. Their log-determinant metric tracks representation space contraction, with Track II detecting collapse substantially earlier than Track I — demonstrating over an order of magnitude greater sensitivity. Critically, SIGMA validates spectral metrics as early-warning collapse indicators in LLMs, but uses them only for monitoring, not closed-loop control. RankMe (Garrido et al., ICML 2023, arXiv:2210.02885) directly validates that spectral effective rank (exponential of Shannon entropy of normalized singular values) serves as a label-free, computationally lightweight proxy for representation quality and dimensional collapse in self-supervised learning — correlating with downstream performance without requiring labels. Monitoring Neural Training with Topology (arXiv:2604.26984, Apr 2026) proposes a composite Collapse Index based on Modular Morse Homology — providing topology-aware online monitoring and mentioning 'data mix adjustments' as a potential application, but implementing only monitoring without any feedback mechanism. Escaping Mode Collapse in LLM Generation via Geometric Regulation (arXiv:2605.00435, May 2026) proposes RMR, operating at inference time rather than training-time data mixing, making it complementary. DiSF (arXiv:2504.20644, Apr 2025) combats dimensional collapse in LLM pretraining data by selecting files with uniform eigenvalues (1.5× training efficiency), demonstrating that effective rank captures data diversity directly — an offline data selection method using spectral metrics, complementary to but distinct from online mixing ratio control. SSO (arXiv:2601.08393, Jan 2026) enforces strict module-wise spectral constraints on weight matrices during LLM pretraining optimization, consistently outperforming AdamW and Muon — an active use of spectral metrics for training control, but applied to weight-space optimization rather than data composition. Spectral Lens (arXiv:2605.05683, May 2026) shows activation covariance spectra forecast downstream token efficiency — validating spectral features as leading indicators of training dynamics. ERBP (arXiv:2512.14879, Dec 2025) provides an information-geometric unification using the Bregman projection framework — proving that entropy-reservoir coupling satisfying λ·s_min > κ (with L_F = 1 for KL divergence) guarantees a non-trivial entropy floor. ERBP explicitly states that 'analyzing the existence and uniqueness of solutions to the self-referential fixed-point equation' is 'a significant theoretical undertaking and a key direction for future research,' and that 'characterising how optimiser noise compounds over many rounds is an important practical question.' Shi et al. (arXiv:2509.16499, NeurIPS 2025 Spotlight) demonstrate entropy-driven collapse in diffusion models and propose entropy-based data selection.
47	
48	**Theoretical foundations.** Dynamic regret theory establishes that any fixed policy incurs regret O(√(T·P_T)) where P_T is the path length quantifying cumulative non-stationarity (Zinkevich, ICML 2003; Besbes et al., Operations Research 2015). In iterative synthetic-real training, P_T grows across generations as synthetic quality shifts — bounding the cost of any fixed weight relative to the best generation-dependent schedule. Barzilai & Shamir (ICML 2025) prove non-asymptotic bounds showing collapse avoidance requires structural assumptions beyond MLE consistency. Strong Model Collapse (ICLR 2025) shows even 1/1000 synthetic fraction can prevent scaling improvements.
49	
50	**Collapse condition characterization.** Schaeffer et al. (ICML 2025) identify 8 definitions and argue prominent scenarios rely on unrealistic assumptions. Kang et al. (EMNLP 2025) find rephrased synthetic data does NOT collapse at foreseeable scales while model-generated content does. Kazdan et al. (ICML 2025) characterize replace/accumulate/fixed-compute workflows.
51	
52	No published work integrates spectral collapse indicators into a closed-loop controller for dynamically adjusting the synthetic-to-real data ratio during iterative autoregressive LLM pretraining. Adjacent uses of spectral metrics exist for active training control (SSO for weight-matrix spectral constraints, DiSF for offline data file selection) and for collapse monitoring with aspirational mentions of interventions (Topology Collapse Index), but none implements closed-loop feedback between spectral representational health signals and data composition in the iterative synthetic-real setting.
53	
54	## Proposed Approach
55	
56	**Core method: Entropy-reservoir PI controller with spectral collapse-risk estimation.** We implement a PI controller that monitors online collapse risk via spectral analysis of the model's output embeddings, adjusting the synthetic-to-real data sampling ratio to maintain the ERBP sufficient stability condition across 5 generations of iterative Pythia-1B pretraining (2B tokens per generation). The method has three novel components: (1) a spectral collapse indicator based on the embedding Gram matrix integrated into a closed-loop controller (extending SIGMA's monitoring to active control), (2) a theoretical contribution connecting PI control design to ERBP's entropy-reservoir framework (with explicit tiered framing — see below), and (3) empirical validation that spectral indicators provide higher-resolution collapse signals than perplexity in autoregressive LLMs.
57	
58	**Theoretical motivation: Why adaptive control can improve over the optimal fixed weight.** The golden-ratio weighting (1/φ) is the optimal constant weight under iterative dynamics where estimation error compounds via the recurrence Err̄(θ̂_t) = (1−w)²Err̄(θ̂_{t−1}) + [(1−w)²k + w²]tr(Σ₀⁻¹) (arXiv:2502.18049). This result optimizes over the restricted class of fixed weights — the paper models iterative training with compounding errors but constrains the policy to use the same w at every generation. A generation-dependent weight schedule w_t that responds to actual per-generation synthetic quality can improve over any fixed weight: early generations, where the model is close to the true distribution, produce high-quality synthetic data requiring less real-data correction, while later generations accumulate drift requiring more. This is the standard static-vs-dynamic optimization gap, bounded by dynamic regret theory: Zinkevich (ICML 2003) and Besbes et al. (Operations Research 2015) establish that any fixed policy incurs regret O(√(T·P_T)) where P_T is the path length — the cost of being static grows with the cumulative non-stationarity of synthetic quality across generations. Bakshi & Chakraborty (arXiv:2602.10531) provide additional structural motivation: their recurrence R_t = (n_0/n_t)R_0 + ((n_t-1)/n_t)(1-α_t)² R_{t-1} shows the contamination propagation factor (1-α_t)² depends on generation-specific synthetic quality, and their analysis of both fixed and decaying weight schedules characterizes convergence conditions for each regime — motivating generation-dependent weights without proving that static ratios are fundamentally suboptimal.
59	
60	**Expected improvement magnitude and success thresholds.** The adaptive advantage over fixed-weight mixing depends on the degree of non-stationarity in the synthetic distribution. When the static baseline is already near-optimal (as the golden ratio is, being derived under iterative dynamics), the improvement margin may be smaller than comparisons to naive baselines suggest. Aioli's improvement over static baselines averages 0.27 perplexity points (up to 12 in extreme distribution shift), and DoReMi's 6.5pp downstream gain is over The Pile's default domain weights — a known-suboptimal static baseline. We define explicit success thresholds: (a) **Primary success**: >1 perplexity point improvement over golden-ratio static mixing at generation 5, or >1.5% downstream accuracy improvement on HellaSwag/ARC-Challenge. This would demonstrate that collapse-aware adaptive control provides meaningful gains over the best fixed weight. (b) **Secondary success**: If the mixing ratio improvement is smaller but statistically significant (<1 perplexity point), we frame the contribution as demonstrating the value of spectral indicators for collapse monitoring — showing that spectral effective rank provides higher-resolution representational health signals than perplexity-based metrics, with marginal but consistent control benefit. This secondary framing has independent value: a validated spectral collapse indicator that can be integrated into any data mixing framework. (c) **Negative result (still publishable)**: If the adaptive controller does not improve over golden-ratio mixing, this constitutes evidence that the golden ratio is near-optimal not just as a fixed weight but across generation-dependent policies in our setting — a non-trivial empirical finding that strengthens the golden-ratio result.
61	
62	**Phase 0: Pilot experiment (reduced scale, ~5 H100-hours).** Before the main experiment, we run a diagnostic pilot: train Pythia-1B for 2 generations with 100% synthetic data (pure replacement, 500M tokens per generation) tracking both perplexity and spectral/diversity metrics at every checkpoint (~50M token intervals). This pilot serves three purposes: (a) validates the 'spectral collapse precedes perplexity degradation' hypothesis for autoregressive LLMs; (b) provides collapse trajectory exemplars for probe calibration and estimates of the ERBP constants κ and s_min; (c) **quantifies the inter-generation distribution shift** by computing KL divergence between G_0→G_1 and G_1→G_2 synthetic distributions, providing an empirical estimate of P_T that predicts the adaptive controller's improvement margin.
63	
64	**Estimating s_min and κ from the pilot.** The ERBP stability condition λ·s_min > κ requires estimating two empirical quantities: (1) κ (optimization imperfection bound) = √(2ε_max), estimated from the maximum per-step training loss deviation during stable G_0 training. (2) s_min (entropy lower bound of the reservoir distribution) — for the real training data serving as entropy reservoir, s_min represents the minimum entropy rate of P_data. We estimate this by computing the empirical token-level entropy of the real training corpus (a plug-in estimator that converges for large corpora), cross-validated against the model's best-achieved cross-entropy (which provides an upper bound on H(P_data)). For English text, s_min is bracketed between ~0.6 bits/char (Shannon's lower bound from human prediction experiments) and the best model's cross-entropy rate. We report s_min as this bracketed range and verify the ERBP condition holds for our chosen operating point. The key insight is that s_min depends only on the fixed real data distribution — it does not change across generations — so a single estimate suffices for the entire experiment.
65	
66	**Secondary value proposition (if hypothesis partially holds).** Even if spectral and perplexity metrics degrade concurrently rather than sequentially, the spectral effective rank provides a continuous, fine-grained representation health signal versus perplexity's scalar aggregate over token-level losses. Perplexity can remain stable while the embedding space contracts along specific dimensions (dimensional collapse) — the model produces acceptable average log-likelihood but has lost representational diversity. RankMe (Garrido et al., ICML 2023) directly validates this: spectral effective rank correlates with downstream performance in self-supervised learning without labels, demonstrating it captures representational quality that loss-based metrics miss. The spectral indicator enables proportional control responses to representational narrowing before it accumulates to impact perplexity.
67	
68	**Spectral collapse-risk estimator (novel indicator).** We train a lightweight linear probe mapping a multi-dimensional feature vector to a scalar collapse-risk score. The key novel feature is the spectral effective rank of the output embedding Gram matrix, inspired by SIGMA (arXiv:2601.03385) and validated by RankMe (ICML 2023) as a representation quality proxy, but applied here in a closed-loop control context rather than for monitoring or offline selection (as in DiSF's eigenvalue-based file selection). Features (computed at evaluation checkpoints every ~200M tokens on 50K generated samples):
69	- **(Novel in control context) Spectral effective rank**: Compute the Gram matrix G = E·Eᵀ of generated-text embeddings (using the model's final-layer hidden states), then compute effective rank as exp(H(σ)) where H(σ) is the entropy of the normalized singular value distribution. This captures dimensional collapse directly, as validated by SIGMA, DiSF (arXiv:2504.20644), RankMe, and Spectral Lens (arXiv:2605.05683).
70	- **(Novel) Token-level prediction entropy variance**: For each generated token, compute the entropy of the next-token probability distribution; report the variance across all tokens. High variance indicates selective confidence (healthy); low variance indicates uniform overconfidence (pathological collapse) or uniform uncertainty.
71	- Unigram/bigram/trigram entropy (standard surface-level features)
72	- Vocabulary coverage rate and tail-token frequency mass
73	- Perplexity divergence and perplexity acceleration (second derivative)
74	
75	**Probe calibration (resolving the bootstrapping problem).** Phase 1 (G_0 training): At checkpoints during G_0, record feature vectors as the healthy baseline distribution. Phase 2 (pilot data): The 100%-synthetic pilot provides a complete collapse trajectory. The probe is trained to predict collapse risk = normalized distance along the trajectory from healthy baseline (risk=0) toward pilot collapse endpoint (risk=1).
76	
77	**Theoretical contribution: PI stability via ERBP connection (tiered framing).** We present the theoretical contribution in a tiered structure that honestly reflects what is achievable:
78	
79	*Tier 1 (standalone, days 1-2): Discrete-time PI stability analysis.* We derive conditions on PI gains (Kp, Ki) under which the controlled mixing ratio converges to a stable equilibrium, using standard discrete-time control theory. This is a self-contained result: for the linearized error dynamics matrix A = [[1+Kp·∂r/∂λ, Ki·∂r/∂λ], [1, 1]], we derive the eigenvalue conditions |λᵢ(A)| < 1 that guarantee convergence. This requires only standard control theory and is achievable in 2 days.
80	
81	*Tier 2 (after pilot, day 3): ERBP-motivated controller design.* We use the ERBP condition λ·s_min > κ to set the 
82	
83	## Resource Estimate
84	
85	- **auto**: {'breakdown': 'Same structure but fully automated pipeline. Includes automatic retry logic (up to 2 retries per failed generation: +15 H100-hours buffer). Automated probe retraining and spectral computation: +10 H100-hours. Pilot runs automatically before main experiments with programmatic dual GO/NO-GO threshold (spectral lead + KL > 0.1).', 'estimated_gpu_cost': '$490-$680 (at $2-3/hr H100 spot pricing)', 'gpu_hours': '~195-215 H100-hours', 'gpu_utilization': '~85-90% (no human idle time, continuous pipeline execution)', 'team': '1 researcher for pipeline setup and final analysis', 'timeline': '6-8 days wall-clock compute with 8 H100 GPUs. Remaining 7-9 days for analysis, stability proof attempt (Tier 3), and paper writing.'}
86	- **human_in_loop**: {'breakdown': 'Same structure as manual mode, but researcher monitors pilot results before proceeding (reducing wasted compute on an unfounded hypothesis). Failed conditions terminated early, saving ~15-20 H100-hours.', 'estimated_gpu_cost': '$380-$530 (at $2-3/hr H100 spot pricing)', 'gpu_hours': '~155-175 H100-hours', 'gpu_utilization': '~60-70% (lower due to human review gaps between generations)', 'team': '1 researcher actively monitoring, 1 researcher for analysis/theory writing in parallel', 'timeline': '15 days with 8 H100 GPUs (human review adds 0.5-1 day between generation blocks but improves debugging efficiency and enables earlier termination of failed conditions)'}
87	- **manual**: {'breakdown': 'Pilot (2 generations × 500M tokens + comprehensive evaluation at every 50M-token checkpoint + KL divergence computation between synthetic distributions): ~6 H100-hours. Shared G_0 (training 2B tokens + generating 300M synthetic tokens + spectral feature computation + probe calibration + s_min/κ estimation): ~17 H100-hours. Per divergent condition (G_1 through G_4: training + generation + spectral evaluation + Gram matrix computation): ~40 H100-hours × 3 main conditions = ~120 H100-hours. Ablations (2 runs × 2 divergent generations each, simplified evaluation): ~22 H100-hours. Evaluation and analysis overhead (including spectral computations, inter-generation KL tracking): ~7 H100-hours.', 'estimated_gpu_cost': '$420-$570 (at $2-3/hr H100 spot pricing)', 'gpu_hours': '~170-190 H100-hours', 'gpu_utilization': '~70-80% effective utilization; idle time during spectral evaluation, probe calibration, and result analysis between generations', 'team': '1-2 researchers with LLM pretraining experience', 'timeline': '15 days (May 10-25, 2026) with 8 H100 GPUs. Days 1-2: Formalize Tier 1 (standalone eigenvalue stability derivation, independent of experiments), pipeline setup, verify training infrastructure, launch pilot (runs in parallel with theory work). Day 3: Complete pilot, validate spectral-vs-perplexity relationship (GO/NO-GO #1), compute inter-generation KL (GO/NO-GO #2: KL > 0.1 nats confirms substantial non-stationarity), estimate κ and s_min, complete Tier 2 ERBP connection (set control target λ* = κ/s_min + margin), calibrate probe, begin G_0. Days 4-5: Complete G_0, generate synthetic data, attempt Tier 3 derivation in parallel. Days 6-10: Run 3 main conditions (G_1 through G_4, parallelizable across GPU subsets). Days 11-12: Ablation runs and final evaluations. Days 13-15: Figures, write paper, finalize theoretical presentation at achieved tier. Front-loaded Tier 1 (days 1-2) eliminates timeline coupling between theory and experiments. Dual GO/NO-GO on day 3 determines both the framing (early warning vs. higher resolution) and expected effect size (large KL → large improvement).'}
88	
89	## Key References
90	
91	- Golden Ratio Weighting Prevents Model Collapse (arXiv:2502.18049, 2025)
92	- Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (Gerstgrasser et al., ICLR 2025)
93	- Aioli: A Unified Optimization Framework for Language Model Data Mixing (ICLR 2025, arXiv:2411.05735)
94	- ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse (arXiv:2509.08972, 2025)
95	- How to Synthesize Text Data without Model Collapse? / ToEdit (arXiv:2412.14689, ICML 2025)
96	- Actor-Critic based Online Data Mixing For Language Model Pre-Training — AC-ODM (arXiv:2505.23878, May 2025; withdrawn from ICLR 2026)
97	- TiKMiX: Take Data Influence into Dynamic Mixture for Language Model Pre-training (arXiv:2508.17677, Aug 2025; withdrawn from ICLR 2026)
98	- GRAPE: Optimize Data Mixture for Group Robust Multi-target Adaptive Pretraining (arXiv:2505.20380, NeurIPS 2025)
99	- Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training (arXiv:2507.15640, Jul 2025)
100	- A PID Controller Approach for Stochastic Optimization of Deep Networks (An et al., CVPR 2018)
101	- Accelerated Optimization in Deep Learning with a PID Controller — PIDAO (Chen et al., Nature Communications 2024)
102	- An Optimal Control Perspective on Deep Learning and Related Theories (Li et al., arXiv:1908.10920, 2019)
103	- Beyond Quadratic Costs: A Bregman Divergence Approach to H-infinity Control (arXiv:2505.00319, 2025)
104	- Data-Driven Adaptive PID Control Based on Physics-Informed Neural Networks (arXiv:2510.04591, Oct 2025)
105	- SIGMA: Scalable Spectral Insights for LLM Model Collapse (arXiv:2601.03385, Jan 2026)
106	- RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank (Garrido et al., ICML 2023, arXiv:2210.02885)
107	- Combatting Dimensional Collapse in LLM Pre-Training Data via Diversified File Selection — DiSF (arXiv:2504.20644, Apr 2025)
108	- Controlled LLM Training on Spectral Sphere — SSO (arXiv:2601.08393, Jan 2026)
109	- Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization (arXiv:2605.05683, May 2026)
110	- Entropy-Reservoir Bregman Projection: An Information-Geometric Unification of Model Collapse — ERBP (arXiv:2512.14879, Dec 2025)
111	- A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (Shi et al., arXiv:2509.16499, NeurIPS 2025 Spotlight)
112	- Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling — DCES (Electronics, Feb 2026)
113	- Learning by Surprise: Surplexity for Mitigating Model Collapse (arXiv:2410.12341, 2024)
114	- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., arXiv:2503.03150, ICML 2025)
115	- Demystifying Synthetic Data in LLM Pre-training (Kang et al., EMNLP 2025, arXiv:2510.01631)
116	- Collapse or Thrive? Perils and Promises of Synthetic Data (Kazdan et al., ICML 2025)
117	- From Collapse to Improvement: Statistical Perspectives on Iterative Training (Bakshi & Chakraborty, arXiv:2602.10531, Feb 2026)
118	- When Models Don't Collapse: On the Consistency of Iterative MLE (Barzilai & Shamir, arXiv:2505.19046, ICML 2025)
119	- Strong Model Collapse (ICLR 2025, arXiv:2410.04840)
120	- Data Mixing for Large Language Models Pretraining: A Survey and Outlook (Chen et al., arXiv:2604.16380, Mar 2026)
121	- DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)
122	- Machine-generated text detection prevents language model collapse (Drayson et al., arXiv:2502.15654, 2025)
123	- Rethinking Data Mixing from the Perspective of LLMs — DoGraph (arXiv:2604.07963, 2026)
124	- Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios (arXiv:2509.22341, 2025)
125	- AI models collapse when trained on recursively generated data (Shumailov et al., Nature 2024)
126	- Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers (arXiv:2410.07799, ICML 2025)
127	- Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index (arXiv:2604.26984, Apr 2026)
128	- Escaping Mode Collapse in LLM Generation via Geometric Regulation (arXiv:2605.00435, May 2026)
129	- Online Convex Programming and Generalized Infinitesimal Gradient Ascent (Zinkevich, ICML 2003)
130	- Non-Stationary Stochastic Optimization (Besbes, Gur & Zeevi, Operations Research 2015)
131	- Towards Next-Generation LLM Training: From the Perspective of Data (arXiv:2603.14712, Mar 2026)
132	
133	## Reviewer Evaluation
134	
135	**Scores**:
136	  - clarity: **{'rationale': 'Exceptionally well-organized: explicit success thresholds (>1pp perplexity, >1.5% downstream), tiered theoretical contribution with honest scope acknowledgment, phased experimental design with clear GO/NO-GO criteria, and multiple publishable framings (primary, secondary, negative result). The intellectual honesty about improvement margins and theoretical difficulty is exemplary.', 'score': 4}**/5
137	  - feasibility: **{'rationale': 'Compute verified independently: Pythia-1B at 2B tokens per generation costs ~8 H100-hours; total ~185 H100-hours fits the 200-hour constraint. EMNLP deadline confirmed May 25. Timeline is tight but de-risked by front-loaded theory (days 1-2), dual GO/NO-GO gates (day 3), tiered theoretical framing, and the fact that 3 conditions can partially parallelize across 8 GPUs.', 'score': 4}**/5
138	  - impact: **{'rationale': 'Addresses the EMNLP 2026 special theme on data contamination and synthetic data feedback loops directly. The contribution operates at two levels: (1) establishing spectral indicators as closed-loop control signals for data governance (extending SIGMA/DiSF from monitoring/offline to active control), and (2) providing the first empirical test of whether adaptive mixing meaningfully beats the optimal fixed weight under iterative dynamics. Even the secondary framing (spectral indicators as higher-resolution collapse signals) has independent community value.', 'score': 4}**/5
139	  - novelty: **{'rationale': 'The specific integration of spectral collapse indicators into a closed-loop PI controller for synthetic-to-real ratio adjustment is independently verified as a genuine gap. Individual components (PI control, spectral metrics, adaptive mixing) are established, but the combination addresses a specific unsolved problem with a clear theoretical grounding via ERBP. PDS (ICLR 2025 Oral) uses control theory for data selection but is offline/PMP-based/non-spectral — different enough to not undermine novelty.', 'score': 4}**/5
140	
141	## Human Review Note
142	
143	## Agent 审核结果（完整三阶段 pipeline）
144	
145	**Verdict**: PASS
146	
147	**入口三重共识 (X)**: 23.0%
148	**终审自评 (Y)**: 35.0%
149	**出口三重共识 (Z)**: 34.0%
150	**Z 区间**: [28.0%, 39.0%]
151	**真实提升 (Z-X)**: +11.0 pp
152	**幻觉幅度 (Y-Z)**: +1.0 pp
153	**出口一致性**: 高
154	**出口三次评估**: [34.0, 37.0, 31.0]
155	
156	### 优化方案 / 拒绝详情
157	【优化方案】
158	
159	1. **[标题]** — 从 "Spectral Collapse-Aware Adaptive Mixing via Entropy-Reservoir PI Control for Iterative Synthetic-Real LLM Pretraining" 改为 "Spectral Collapse Indicators as Closed-Loop Control Signals for Adaptive Synthetic-Real Data Mixing in Iterative Language Model Pretraining"。去掉控制论术语密度（"PI Control"、"Entropy-Reservoir"），前置 "Spectral Collapse Indicators" 和 "Language Model"，让 EMNLP reviewer 在标题层即感知 NLP relevance。 — [Significance / venue fit]
160	
161	2. **[核心叙事弧线 — Introduction 全面重构]** — 原始 proposal 以 PI controller 设计为叙事中心，四个 contribution 工程式平铺。改为 NLP 研究问题驱动的叙事：先提出"迭代合成预训练如何系统性损害语言能力？退化是均匀的还是结构化的？"，再引出"因此需要能捕捉退化结构的信号（spectral rank）而非标量聚合（perplexity）"，最后引出"基于此设计闭环控制器作为精确控制 collapse 程度的工具"。CC1/CC2 从研究对象变为服务于 NLP 研究问题的 instrument。这是从原始 proposal 到最终版本最根本性的转变。 — [Novelty + Significance — 从 "又一个 adaptive mixing method" 变为 "NLP investigation of structured linguistic collapse + spectral control as instrument"]
162	
163	3. **[新增 2×2 定位矩阵 — Figure 1]** — 原始 proposal 以文字列表罗列 Aioli/SIGMA/DiSF 等相关工作的定位。改为 (signal type: loss-based vs. spectral) × (usage mode: offline/monitoring vs. online closed-loop) 的 2×2 可视化矩阵，明确标注本文占据的空白象限。放在 Introduction 第一页，让 reviewer 30 秒内抓住核心 positioning。 — [Novelty / Clarity — 降低 reviewer 误判 novelty 的概率]
164	
165	4. **[新增 Key Insight 章节 — Leading vs. Lagging Indicator 假设 + Toy Model Sketch]** — 原始 proposal 对 spectral vs. perplexity 的差异只有隐含的工程直觉。新增独立章节，构建三层论证：(a) 引用 Jing et al. 2022 "Understanding Dimensional Collapse" 建立类比（loss plateaus while representations degenerate）；(b) 提供 toy model sketch——线性 representation 在高斯混合下，spectral rank 对方向性收缩的响应先于 cross-entropy 对聚合分布偏移的响应，因为 loss components 可互相抵消而 spectral entropy 不能；(c) 明确标注为 pre-registered hypothesis 而非 assumption，实验设计含显式验证。 — [Technical Soundness + Novelty — 将 empirical finding 升级为 "theory-motivated prediction + experimental validation" 的双层结构]
166	
167	5. **[新增 Non-trivial Integration Challenges 章节]** — 原始 proposal 无此讨论，容易被 reviewer 解读为"把 RankMe 指标插入 PI controller 的 trivial 工程集成"。新增三点非平凡性论证：(a) 离散代际信号的量化噪声与平滑设计；(b) setpoint 跨规
168	
169	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "318bd24e-1d88-4118-b154-0a4d9d70badb",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/docs/IDEA_BRIEF.md",
      "content": "# Idea Brief: Spectral Collapse-Aware Adaptive Mixing via Entropy-Reservoir PI Control for Iterative Synthetic-Real LLM Pretraining\n\n\n- **Idea ID**: `idea_012`\n- **Created**: 2026-05-12\n- **Approved**: 2026-05-12\n- **Source**: foreign:be-idea-gen-0509-4\n- **Level**: top-tier\n- **Target Venues**: EMNLP 2026 (ARR submission deadline: May 25, 2026) — primary target, 15 days from today. Three contributions: spectral collapse indicator for closed-loop control, PI-ERBP stability connection (tiered: design guidance guaranteed, formal proof aspirational), pilot-validated improvement margin via KL-based non-stationarity measurement., AAAI 2027 (deadline projected July-August 2026) — extended version with Tier 3 formal proof (if not achieved for EMNLP), formal κ/s_min bounds for specific architectures, additional conditions (ForTIFAI-TCE combination, AC-ODM comparison), and 6+ generation experiments, ICLR 2027 (estimated deadline September-October 2026) — alternative venue for extended version\n\n## Seed Topic\n\nTarget: EMNLP 2026, ARR submission deadline 2026-05-25 (16 days from today 2026-05-09). Track: Machine Learning for NLP / Resources and Evaluation. Aligns with EMNLP 2026 special theme \"New Missions for NLP Research\" which explicitly calls for work on data contamination, synthetic data feedback loops, and data governance.\n\nDirection: Synthetic data quality, model collapse prevention, contamination detection. In-scope: synthetic data verification/filtering methods, detecting training data contamination in benchmarks, methods to break recursive data feedback loops, data mixing strategies that prevent quality degradation, principled synthetic data generation with quality guarantees.\n\nContribution type: METHOD ONLY. Must propose a concrete detection algorithm, filtering pipeline, or training recipe — not just an observation about model collapse. Method + analysis OK.\n\nHARD CONSTRAINTS:\n1. Compute: ≤200 H100-hours total. Model collapse experiments need multiple training iterations — budget for small models (1B-3B) across 3-5 generations.\n2. Time: ≤16 days. Use small open models (Pythia, OLMo-1B, Qwen-0.5B/1.8B) for iterative collapse experiments.\n3. Eval: perplexity degradation curves, downstream task quality (MMLU, HellaSwag), diversity metrics (self-BLEU, n-gram entropy), contamination detection accuracy.\n\nThis is a hot EMNLP 2026 special theme area with relatively few established methods — high novelty potential.\n\nTag: direction=data_governance, contribution_type=method. target_venues=[\"EMNLP 2026 Main\", \"EMNLP 2026 Findings\"].\n\n## Core Problem\n\nCurrent approaches to mixing synthetic and real data in iterative LLM pretraining either use static ratios (golden-ratio weighting, fixed proportions) or apply generic online optimization (Aioli via loss-based feedback, GRAPE via minimax DRO) without monitoring for collapse-specific dynamics. Static mixing ratios — including the golden-ratio weighting (arXiv:2502.18049) — optimize over the restricted class of fixed weights: the golden ratio 1/φ minimizes asymptotic steady-state error as a constant weight across all generations under iterative dynamics where estimation error compounds via the recurrence Err̄(θ̂_t) = (1−w)²Err̄(θ̂_{t−1}) + [(1−w)²k + w²]tr(Σ₀⁻¹). However, a generation-dependent weight schedule w_t that allocates less real data early (when synthetic quality is high and the model is close to the true distribution) and more late (when drift has accumulated) can improve over any fixed weight — the classic static-vs-dynamic optimization gap. Bakshi & Chakraborty (arXiv:2602.10531) formalize the generation-specific structure via the recurrence R_t = (n_0/n_t)R_0 + ((n_t-1)/n_t)(1-α_t)² R_{t-1}, where the contamination propagation factor (1-α_t)² depends on generation-specific synthetic quality — their analysis of both fixed and decaying weight schedules motivates generation-dependent mixing, though they do not prove that static ratios are suboptimal. Training-objective modifications like truncated cross-entropy (ForTIFAI) and token-level editing (ToEdit) increase collapse tolerance but do not control data composition dynamically. While DCES monitors cluster dispersion for adaptive sampling in classification self-training, no existing method for autoregressive LLM pretraining uses online spectral collapse indicators to dynamically adjust the synthetic-to-real data ratio across model generations. Recent dynamic mixing methods optimize general domain proportions using loss or gradient signals that cannot distinguish between benign loss variation and collapse-induced representational narrowing. SIGMA (arXiv:2601.03385) demonstrates that spectral analysis of embedding Gram matrices can detect collapse onset in LLMs, but uses it only for monitoring, not for closed-loop control. The Topology Collapse Index (arXiv:2604.26984) mentions 'data mix adjustments' as a potential application but implements only monitoring without any feedback mechanism. DiSF (arXiv:2504.20644) uses eigenvalue uniformity for offline data file selection, and SSO (arXiv:2601.08393) enforces spectral constraints on weight matrices during optimization — both adjacent uses of spectral metrics that do not address online mixing ratio control. The ERBP framework (arXiv:2512.14879) proves that avoiding collapse in self-referential learning requires maintaining sufficient entropy-reservoir coupling — specifically, the condition λ·s_min > κ (where λ is the coupling coefficient, s_min is the entropy lower bound of the reservoir distribution, and κ is the optimization imperfection bound) — but provides no mechanism to dynamically adjust this coupling during training, and explicitly identifies the multi-round dynamics analysis as 'a significant theoretical undertaking and a key direction for future research.' Crucially, theoretical work (Barzilai & Shamir, ICML 2025; Bakshi & Chakraborty, 2026; ERBP, 2025) proves that avoiding collapse requires structural assumptions beyond MLE consistency — simply accumulating data is insufficient without monitoring whether those conditions hold and adjusting accordingly. Dynamic regret theory (Zinkevich, ICML 2003; Besbes et al., Operations Research 2015) establishes that any fixed policy incurs regret O(√(T·P_T)) where P_T is the path length (cumulative non-stationarity) — in iterative training where synthetic quality degrades across generations, P_T grows, making the improvement of an adaptive policy over any fixed policy increasingly significant. This motivates a controller that uses spectral collapse indicators to dynamically adjust the entropy-reservoir coupling (i.e., real data fraction) in a generation-aware manner, exploiting the static-vs-dynamic optimization gap that even the optimal fixed weight (golden ratio) cannot close.\n\n## Opportunity / Why Now\n\nRecent evidence shows model collapse is condition-dependent: rephrased synthetic data may not trigger collapse at foreseeable scales (Kang et al., EMNLP 2025), while model-generated content under replace workflows does degrade quality (Kazdan et al., ICML 2025). Schaeffer et al. (ICML 2025) further narrow the genuine threat to specific data workflows. Two recent theoretical advances create a precise opportunity: (1) The ERBP framework (arXiv:2512.14879) proves that self-referential training dynamics can be stabilized by an entropy reservoir with coupling satisfying λ·s_min > κ (where s_min is the reservoir's entropy lower bound and κ bounds optimization imperfection), providing closed-form rates and a sufficient condition for maintaining a non-trivial entropy floor — but does not prescribe how to dynamically set λ during training, and explicitly acknowledges that characterizing multi-round dynamics is an open problem. For the KL divergence generator (natural for language models), ERBP shows L_F = 1 analytically, simplifying the stability bound but leaving two empirical quantities: κ (optimization imperfection) and s_min (reservoir entropy). (2) SIGMA (arXiv:2601.03385) shows the log-determinant of the embedding Gram matrix provides scalable, early-warning spectral collapse detection in LLMs — Track II detects collapse substantially earlier than conservative Track I metrics, with over an order of magnitude more sensitivity — but uses this only for post-hoc monitoring, not active control. Together, these create a clear gap: a controller that monitors spectral collapse indicators and dynamically adjusts the entropy-reservoir coupling (real data fraction) to maintain the ERBP stability condition. The potential advantage of adaptive over fixed-weight control follows from the static-vs-dynamic optimization gap: the golden ratio (1/φ) is the optimal constant weight under the iterative error recurrence (arXiv:2502.18049), but it cannot respond to the actual per-generation synthetic quality. Early generations, where the model is still close to the true distribution, produce high-quality synthetic data requiring less real-data correction, while later generations accumulate drift requiring more. A generation-dependent weight schedule can exploit this structure. The expected magnitude of improvement depends on the degree of non-stationarity. Shumailov et al. (Nature 2024) report perplexity degradation of 20-28 points over 9 generations under pure replacement, indicating substantial non-stationarity. Dynamic mixing methods in the general domain setting (DoReMi, Aioli) show 0.3-12 perplexity point improvements and up to 6.5 percentage point downstream gains depending on distribution shift magnitude. However, when the static baseline is already near-optimal (as the golden ratio is, being derived under iterative dynamics), the adaptive advantage may be smaller — potentially <1 perplexity point in low-non-stationarity regimes. Our pilot (Phase 0) measures inter-generation KL divergence to quantify the actual non-stationarity in our setting, providing a concrete estimate of the expected improvement margin before committing to the full experiment. We define explicit success thresholds (see approach). Three recent dynamic mixing methods are conceptually related but use generic signals: Aioli (ICLR 2025, arXiv:2411.05735) uses loss-based online adaptation; GRAPE (NeurIPS 2025) uses minimax DRO for multi-target robustness. AC-ODM (arXiv:2505.23878) and TiKMiX (arXiv:2508.17677) proposed actor-critic RL and gradient-based Group Influence respectively, but both were withdrawn from ICLR 2026 review — we cite their technical approaches for completeness but note their unvalidated status. None monitors spectral representational health or connects to information-geometric stability conditions. Adjacent uses of spectral metrics for active training control exist — SSO (arXiv:2601.08393) enforces spectral constraints on weight matrices during LLM pretraining optimization, DiSF (arXiv:2504.20644) uses eigenvalue uniformity for offline data file selection, and the Topology Collapse Index (arXiv:2604.26984) mentions 'data mix adjustments' as a potential application but implements only monitoring — yet no published work integrates spectral collapse indicators into a closed-loop controller for dynamically adjusting the synthetic-to-real data ratio during iterative pretraining. A PI controller with spectral collapse-risk estimation fills this specific gap: classical control with well-understood stability properties (vs. RL without convergence guarantees), cheap inference-time spectral features (vs. gradient computation), and theoretically grounded collapse-specific signals connected to ERBP's sufficient stability condition (vs. generic loss). Feasible on Pythia-1B across 5 generations within ~190 H100-hours, targeting EMNLP 2026.\n\n## Landscape (SOTA & Limitations)\n\n**Static mixing approaches.** Golden ratio weighting (arXiv:2502.18049, Feb 2025) proves that weighting real data by 1/φ minimizes asymptotic steady-state error as a constant weight under iterative dynamics where estimation error compounds via the recurrence Err̄(θ̂_t) = (1−w)²Err̄(θ̂_{t−1}) + [(1−w)²k + w²]tr(Σ₀⁻¹) — applicable to Gaussian, GLM, and nonparametric settings. Crucially, this result optimizes over the restricted class of fixed weights: the paper models iterative training with compounding errors but does not analyze generation-dependent weight schedules w_t, leaving open whether adaptive weights can improve over the golden ratio. Preventing Model Collapse Under Overparametrization (arXiv:2509.22341) derives optimal static mixing ratios without adaptive adjustment. The accumulate strategy (Gerstgrasser et al., ICLR 2025) prevents collapse by retaining all prior data but does not optimize the mixing ratio. Bakshi & Chakraborty (arXiv:2602.10531) derive the recurrence R_t = (n_0/n_t)R_0 + ((n_t-1)/n_t)(1-α_t)²R_{t-1} and analyze both fixed (constant α) and decaying (α_t → 0) weight schedules, characterizing convergence conditions for each. Their analysis shows the contamination propagation factor (1-α_t)² depends on generation-specific synthetic quality, motivating generation-dependent weights — though they do not prove that static ratios are fundamentally suboptimal. The paper discusses 'naturally adaptive' weights in Appendix E as supplementary analysis and notes that estimating mixture weights in practice 'remains a challenge.'\n\n**Dynamic mixing approaches — generic.** Aioli (ICLR 2025, arXiv:2411.05735) dynamically adjusts domain proportions via loss-based signals, achieving 0.27-12.0 perplexity point improvements over static baselines depending on distribution shift magnitude — but targets general domain optimization rather than collapse dynamics. GRAPE (arXiv:2505.20380, NeurIPS 2025) uses minimax DRO for group-robust multi-target adaptive pretraining. DoReMi (NeurIPS 2023) achieves +6.5 percentage points average few-shot accuracy over The Pile's default domain weights (a known-suboptimal static baseline) and 2.6× convergence speedup. DoGraph (arXiv:2604.07963, Apr 2026) addresses domain weight optimization. AC-ODM (arXiv:2505.23878, May 2025) proposed actor-critic RL (DDPG) for dynamic domain weight adjustment, claiming 71% faster convergence — but was withdrawn from ICLR 2026. TiKMiX (arXiv:2508.17677, Aug 2025) proposed gradient-based Group Influence with 2% average gains at 20% of REGMIX's compute — also withdrawn from ICLR 2026. We cite AC-ODM and TiKMiX for their technical approaches (actor-critic and gradient-based control respectively) but note their unvalidated peer-review status; Aioli and GRAPE are the established accepted-paper baselines. Data Mixing Agent (arXiv:2507.15640, Jul 2025) learns RL-based domain reweighting for continual pretraining — targets catastrophic forgetting, not collapse. The data mixing survey (Chen et al., arXiv:2604.16380, Mar 2026) taxonomizes approaches, identifying limited transferability as a key open challenge. Next-Generation LLM Training (arXiv:2603.14712, Mar 2026) proposes a unified data-model interaction training system with dynamic data selection and reweighting, but does not use spectral collapse indicators or address synthetic-vs-real mixing.\n\n**PID control in machine learning.** An et al. (CVPR 2018) established PID control for deep network optimization, framing PID-inspired approaches as 'motivated by the outstanding performance of PID controllers in automatic control' — providing design intuition from control theory with empirical validation, rather than closed-loop stability proofs for nonlinear DNN dynamics (up to 50% training acceleration). PIDAO (Chen et al., Nature Communications 2024) extends this with formal convergence analysis for convex objectives. Li et al. (arXiv:1908.10920, 2019) frame deep learning as optimal control for 'principled guidance for architecture and algorithm design.' All apply PID to optimizer dynamics (parameter updates), not to data composition. Recent work on data-driven adaptive PID (arXiv:2510.04591, Oct 2025) demonstrates physics-informed approaches to stability-guaranteed PID tuning. Beyond Quadratic Costs (arXiv:2505.00319, 2025) derives stabilizing controllers using Bregman divergence cost functions via Riccati-like identities.\n\n**Collapse-specific methods — surface metrics.** DCES (Electronics, Feb 2026) monitors intra-cluster dispersion for adaptive sampling in classification. ForTIFAI (arXiv:2509.08972, Sep 2025) introduces TCE loss achieving 2.3× greater collapse tolerance, modifying training objectives rather than data composition. ToEdit (arXiv:2412.14689, ICML 2025) proposes token-level editing with theoretical guarantees — operates on data synthesis rather than mixing ratio control, making it complementary. Surplexity (arXiv:2410.12341, Oct 2024) provides perplexity-based surprise metrics for offline data filtering.\n\n**Collapse-specific methods — spectral, topological, and information-geometric.** SIGMA (arXiv:2601.03385, Jan 2026) introduces spectral analysis of the embedding Gram matrix for scalable LLM collapse monitoring. Their log-determinant metric tracks representation space contraction, with Track II detecting collapse substantially earlier than Track I — demonstrating over an order of magnitude greater sensitivity. Critically, SIGMA validates spectral metrics as early-warning collapse indicators in LLMs, but uses them only for monitoring, not closed-loop control. RankMe (Garrido et al., ICML 2023, arXiv:2210.02885) directly validates that spectral effective rank (exponential of Shannon entropy of normalized singular values) serves as a label-free, computationally lightweight proxy for representation quality and dimensional collapse in self-supervised learning — correlating with downstream performance without requiring labels. Monitoring Neural Training with Topology (arXiv:2604.26984, Apr 2026) proposes a composite Collapse Index based on Modular Morse Homology — providing topology-aware online monitoring and mentioning 'data mix adjustments' as a potential application, but implementing only monitoring without any feedback mechanism. Escaping Mode Collapse in LLM Generation via Geometric Regulation (arXiv:2605.00435, May 2026) proposes RMR, operating at inference time rather than training-time data mixing, making it complementary. DiSF (arXiv:2504.20644, Apr 2025) combats dimensional collapse in LLM pretraining data by selecting files with uniform eigenvalues (1.5× training efficiency), demonstrating that effective rank captures data diversity directly — an offline data selection method using spectral metrics, complementary to but distinct from online mixing ratio control. SSO (arXiv:2601.08393, Jan 2026) enforces strict module-wise spectral constraints on weight matrices during LLM pretraining optimization, consistently outperforming AdamW and Muon — an active use of spectral metrics for training control, but applied to weight-space optimization rather than data composition. Spectral Lens (arXiv:2605.05683, May 2026) shows activation covariance spectra forecast downstream token efficiency — validating spectral features as leading indicators of training dynamics. ERBP (arXiv:2512.14879, Dec 2025) provides an information-geometric unification using the Bregman projection framework — proving that entropy-reservoir coupling satisfying λ·s_min > κ (with L_F = 1 for KL divergence) guarantees a non-trivial entropy floor. ERBP explicitly states that 'analyzing the existence and uniqueness of solutions to the self-referential fixed-point equation' is 'a significant theoretical undertaking and a key direction for future research,' and that 'characterising how optimiser noise compounds over many rounds is an important practical question.' Shi et al. (arXiv:2509.16499, NeurIPS 2025 Spotlight) demonstrate entropy-driven collapse in diffusion models and propose entropy-based data selection.\n\n**Theoretical foundations.** Dynamic regret theory establishes that any fixed policy incurs regret O(√(T·P_T)) where P_T is the path length quantifying cumulative non-stationarity (Zinkevich, ICML 2003; Besbes et al., Operations Research 2015). In iterative synthetic-real training, P_T grows across generations as synthetic quality shifts — bounding the cost of any fixed weight relative to the best generation-dependent schedule. Barzilai & Shamir (ICML 2025) prove non-asymptotic bounds showing collapse avoidance requires structural assumptions beyond MLE consistency. Strong Model Collapse (ICLR 2025) shows even 1/1000 synthetic fraction can prevent scaling improvements.\n\n**Collapse condition characterization.** Schaeffer et al. (ICML 2025) identify 8 definitions and argue prominent scenarios rely on unrealistic assumptions. Kang et al. (EMNLP 2025) find rephrased synthetic data does NOT collapse at foreseeable scales while model-generated content does. Kazdan et al. (ICML 2025) characterize replace/accumulate/fixed-compute workflows.\n\nNo published work integrates spectral collapse indicators into a closed-loop controller for dynamically adjusting the synthetic-to-real data ratio during iterative autoregressive LLM pretraining. Adjacent uses of spectral metrics exist for active training control (SSO for weight-matrix spectral constraints, DiSF for offline data file selection) and for collapse monitoring with aspirational mentions of interventions (Topology Collapse Index), but none implements closed-loop feedback between spectral representational health signals and data composition in the iterative synthetic-real setting.\n\n## Proposed Approach\n\n**Core method: Entropy-reservoir PI controller with spectral collapse-risk estimation.** We implement a PI controller that monitors online collapse risk via spectral analysis of the model's output embeddings, adjusting the synthetic-to-real data sampling ratio to maintain the ERBP sufficient stability condition across 5 generations of iterative Pythia-1B pretraining (2B tokens per generation). The method has three novel components: (1) a spectral collapse indicator based on the embedding Gram matrix integrated into a closed-loop controller (extending SIGMA's monitoring to active control), (2) a theoretical contribution connecting PI control design to ERBP's entropy-reservoir framework (with explicit tiered framing — see below), and (3) empirical validation that spectral indicators provide higher-resolution collapse signals than perplexity in autoregressive LLMs.\n\n**Theoretical motivation: Why adaptive control can improve over the optimal fixed weight.** The golden-ratio weighting (1/φ) is the optimal constant weight under iterative dynamics where estimation error compounds via the recurrence Err̄(θ̂_t) = (1−w)²Err̄(θ̂_{t−1}) + [(1−w)²k + w²]tr(Σ₀⁻¹) (arXiv:2502.18049). This result optimizes over the restricted class of fixed weights — the paper models iterative training with compounding errors but constrains the policy to use the same w at every generation. A generation-dependent weight schedule w_t that responds to actual per-generation synthetic quality can improve over any fixed weight: early generations, where the model is close to the true distribution, produce high-quality synthetic data requiring less real-data correction, while later generations accumulate drift requiring more. This is the standard static-vs-dynamic optimization gap, bounded by dynamic regret theory: Zinkevich (ICML 2003) and Besbes et al. (Operations Research 2015) establish that any fixed policy incurs regret O(√(T·P_T)) where P_T is the path length — the cost of being static grows with the cumulative non-stationarity of synthetic quality across generations. Bakshi & Chakraborty (arXiv:2602.10531) provide additional structural motivation: their recurrence R_t = (n_0/n_t)R_0 + ((n_t-1)/n_t)(1-α_t)² R_{t-1} shows the contamination propagation factor (1-α_t)² depends on generation-specific synthetic quality, and their analysis of both fixed and decaying weight schedules characterizes convergence conditions for each regime — motivating generation-dependent weights without proving that static ratios are fundamentally suboptimal.\n\n**Expected improvement magnitude and success thresholds.** The adaptive advantage over fixed-weight mixing depends on the degree of non-stationarity in the synthetic distribution. When the static baseline is already near-optimal (as the golden ratio is, being derived under iterative dynamics), the improvement margin may be smaller than comparisons to naive baselines suggest. Aioli's improvement over static baselines averages 0.27 perplexity points (up to 12 in extreme distribution shift), and DoReMi's 6.5pp downstream gain is over The Pile's default domain weights — a known-suboptimal static baseline. We define explicit success thresholds: (a) **Primary success**: >1 perplexity point improvement over golden-ratio static mixing at generation 5, or >1.5% downstream accuracy improvement on HellaSwag/ARC-Challenge. This would demonstrate that collapse-aware adaptive control provides meaningful gains over the best fixed weight. (b) **Secondary success**: If the mixing ratio improvement is smaller but statistically significant (<1 perplexity point), we frame the contribution as demonstrating the value of spectral indicators for collapse monitoring — showing that spectral effective rank provides higher-resolution representational health signals than perplexity-based metrics, with marginal but consistent control benefit. This secondary framing has independent value: a validated spectral collapse indicator that can be integrated into any data mixing framework. (c) **Negative result (still publishable)**: If the adaptive controller does not improve over golden-ratio mixing, this constitutes evidence that the golden ratio is near-optimal not just as a fixed weight but across generation-dependent policies in our setting — a non-trivial empirical finding that strengthens the golden-ratio result.\n\n**Phase 0: Pilot experiment (reduced scale, ~5 H100-hours).** Before the main experiment, we run a diagnostic pilot: train Pythia-1B for 2 generations with 100% synthetic data (pure replacement, 500M tokens per generation) tracking both perplexity and spectral/diversity metrics at every checkpoint (~50M token intervals). This pilot serves three purposes: (a) validates the 'spectral collapse precedes perplexity degradation' hypothesis for autoregressive LLMs; (b) provides collapse trajectory exemplars for probe calibration and estimates of the ERBP constants κ and s_min; (c) **quantifies the inter-generation distribution shift** by computing KL divergence between G_0→G_1 and G_1→G_2 synthetic distributions, providing an empirical estimate of P_T that predicts the adaptive controller's improvement margin.\n\n**Estimating s_min and κ from the pilot.** The ERBP stability condition λ·s_min > κ requires estimating two empirical quantities: (1) κ (optimization imperfection bound) = √(2ε_max), estimated from the maximum per-step training loss deviation during stable G_0 training. (2) s_min (entropy lower bound of the reservoir distribution) — for the real training data serving as entropy reservoir, s_min represents the minimum entropy rate of P_data. We estimate this by computing the empirical token-level entropy of the real training corpus (a plug-in estimator that converges for large corpora), cross-validated against the model's best-achieved cross-entropy (which provides an upper bound on H(P_data)). For English text, s_min is bracketed between ~0.6 bits/char (Shannon's lower bound from human prediction experiments) and the best model's cross-entropy rate. We report s_min as this bracketed range and verify the ERBP condition holds for our chosen operating point. The key insight is that s_min depends only on the fixed real data distribution — it does not change across generations — so a single estimate suffices for the entire experiment.\n\n**Secondary value proposition (if hypothesis partially holds).** Even if spectral and perplexity metrics degrade concurrently rather than sequentially, the spectral effective rank provides a continuous, fine-grained representation health signal versus perplexity's scalar aggregate over token-level losses. Perplexity can remain stable while the embedding space contracts along specific dimensions (dimensional collapse) — the model produces acceptable average log-likelihood but has lost representational diversity. RankMe (Garrido et al., ICML 2023) directly validates this: spectral effective rank correlates with downstream performance in self-supervised learning without labels, demonstrating it captures representational quality that loss-based metrics miss. The spectral indicator enables proportional control responses to representational narrowing before it accumulates to impact perplexity.\n\n**Spectral collapse-risk estimator (novel indicator).** We train a lightweight linear probe mapping a multi-dimensional feature vector to a scalar collapse-risk score. The key novel feature is the spectral effective rank of the output embedding Gram matrix, inspired by SIGMA (arXiv:2601.03385) and validated by RankMe (ICML 2023) as a representation quality proxy, but applied here in a closed-loop control context rather than for monitoring or offline selection (as in DiSF's eigenvalue-based file selection). Features (computed at evaluation checkpoints every ~200M tokens on 50K generated samples):\n- **(Novel in control context) Spectral effective rank**: Compute the Gram matrix G = E·Eᵀ of generated-text embeddings (using the model's final-layer hidden states), then compute effective rank as exp(H(σ)) where H(σ) is the entropy of the normalized singular value distribution. This captures dimensional collapse directly, as validated by SIGMA, DiSF (arXiv:2504.20644), RankMe, and Spectral Lens (arXiv:2605.05683).\n- **(Novel) Token-level prediction entropy variance**: For each generated token, compute the entropy of the next-token probability distribution; report the variance across all tokens. High variance indicates selective confidence (healthy); low variance indicates uniform overconfidence (pathological collapse) or uniform uncertainty.\n- Unigram/bigram/trigram entropy (standard surface-level features)\n- Vocabulary coverage rate and tail-token frequency mass\n- Perplexity divergence and perplexity acceleration (second derivative)\n\n**Probe calibration (resolving the bootstrapping problem).** Phase 1 (G_0 training): At checkpoints during G_0, record feature vectors as the healthy baseline distribution. Phase 2 (pilot data): The 100%-synthetic pilot provides a complete collapse trajectory. The probe is trained to predict collapse risk = normalized distance along the trajectory from healthy baseline (risk=0) toward pilot collapse endpoint (risk=1).\n\n**Theoretical contribution: PI stability via ERBP connection (tiered framing).** We present the theoretical contribution in a tiered structure that honestly reflects what is achievable:\n\n*Tier 1 (standalone, days 1-2): Discrete-time PI stability analysis.* We derive conditions on PI gains (Kp, Ki) under which the controlled mixing ratio converges to a stable equilibrium, using standard discrete-time control theory. This is a self-contained result: for the linearized error dynamics matrix A = [[1+Kp·∂r/∂λ, Ki·∂r/∂λ], [1, 1]], we derive the eigenvalue conditions |λᵢ(A)| < 1 that guarantee convergence. This requires only standard control theory and is achievable in 2 days.\n\n*Tier 2 (after pilot, day 3): ERBP-motivated controller design.* We use the ERBP condition λ·s_min > κ to set the \n\n## Resource Estimate\n\n- **auto**: {'breakdown': 'Same structure but fully automated pipeline. Includes automatic retry logic (up to 2 retries per failed generation: +15 H100-hours buffer). Automated probe retraining and spectral computation: +10 H100-hours. Pilot runs automatically before main experiments with programmatic dual GO/NO-GO threshold (spectral lead + KL > 0.1).', 'estimated_gpu_cost': '$490-$680 (at $2-3/hr H100 spot pricing)', 'gpu_hours': '~195-215 H100-hours', 'gpu_utilization': '~85-90% (no human idle time, continuous pipeline execution)', 'team': '1 researcher for pipeline setup and final analysis', 'timeline': '6-8 days wall-clock compute with 8 H100 GPUs. Remaining 7-9 days for analysis, stability proof attempt (Tier 3), and paper writing.'}\n- **human_in_loop**: {'breakdown': 'Same structure as manual mode, but researcher monitors pilot results before proceeding (reducing wasted compute on an unfounded hypothesis). Failed conditions terminated early, saving ~15-20 H100-hours.', 'estimated_gpu_cost': '$380-$530 (at $2-3/hr H100 spot pricing)', 'gpu_hours': '~155-175 H100-hours', 'gpu_utilization': '~60-70% (lower due to human review gaps between generations)', 'team': '1 researcher actively monitoring, 1 researcher for analysis/theory writing in parallel', 'timeline': '15 days with 8 H100 GPUs (human review adds 0.5-1 day between generation blocks but improves debugging efficiency and enables earlier termination of failed conditions)'}\n- **manual**: {'breakdown': 'Pilot (2 generations × 500M tokens + comprehensive evaluation at every 50M-token checkpoint + KL divergence computation between synthetic distributions): ~6 H100-hours. Shared G_0 (training 2B tokens + generating 300M synthetic tokens + spectral feature computation + probe calibration + s_min/κ estimation): ~17 H100-hours. Per divergent condition (G_1 through G_4: training + generation + spectral evaluation + Gram matrix computation): ~40 H100-hours × 3 main conditions = ~120 H100-hours. Ablations (2 runs × 2 divergent generations each, simplified evaluation): ~22 H100-hours. Evaluation and analysis overhead (including spectral computations, inter-generation KL tracking): ~7 H100-hours.', 'estimated_gpu_cost': '$420-$570 (at $2-3/hr H100 spot pricing)', 'gpu_hours': '~170-190 H100-hours', 'gpu_utilization': '~70-80% effective utilization; idle time during spectral evaluation, probe calibration, and result analysis between generations', 'team': '1-2 researchers with LLM pretraining experience', 'timeline': '15 days (May 10-25, 2026) with 8 H100 GPUs. Days 1-2: Formalize Tier 1 (standalone eigenvalue stability derivation, independent of experiments), pipeline setup, verify training infrastructure, launch pilot (runs in parallel with theory work). Day 3: Complete pilot, validate spectral-vs-perplexity relationship (GO/NO-GO #1), compute inter-generation KL (GO/NO-GO #2: KL > 0.1 nats confirms substantial non-stationarity), estimate κ and s_min, complete Tier 2 ERBP connection (set control target λ* = κ/s_min + margin), calibrate probe, begin G_0. Days 4-5: Complete G_0, generate synthetic data, attempt Tier 3 derivation in parallel. Days 6-10: Run 3 main conditions (G_1 through G_4, parallelizable across GPU subsets). Days 11-12: Ablation runs and final evaluations. Days 13-15: Figures, write paper, finalize theoretical presentation at achieved tier. Front-loaded Tier 1 (days 1-2) eliminates timeline coupling between theory and experiments. Dual GO/NO-GO on day 3 determines both the framing (early warning vs. higher resolution) and expected effect size (large KL → large improvement).'}\n\n## Key References\n\n- Golden Ratio Weighting Prevents Model Collapse (arXiv:2502.18049, 2025)\n- Is Model Collapse Inevitable? Breaking the Curse of Recursion by Accumulating Real and Synthetic Data (Gerstgrasser et al., ICLR 2025)\n- Aioli: A Unified Optimization Framework for Language Model Data Mixing (ICLR 2025, arXiv:2411.05735)\n- ForTIFAI: Fending Off Recursive Training Induced Failure for AI Model Collapse (arXiv:2509.08972, 2025)\n- How to Synthesize Text Data without Model Collapse? / ToEdit (arXiv:2412.14689, ICML 2025)\n- Actor-Critic based Online Data Mixing For Language Model Pre-Training — AC-ODM (arXiv:2505.23878, May 2025; withdrawn from ICLR 2026)\n- TiKMiX: Take Data Influence into Dynamic Mixture for Language Model Pre-training (arXiv:2508.17677, Aug 2025; withdrawn from ICLR 2026)\n- GRAPE: Optimize Data Mixture for Group Robust Multi-target Adaptive Pretraining (arXiv:2505.20380, NeurIPS 2025)\n- Data Mixing Agent: Learning to Re-weight Domains for Continual Pre-training (arXiv:2507.15640, Jul 2025)\n- A PID Controller Approach for Stochastic Optimization of Deep Networks (An et al., CVPR 2018)\n- Accelerated Optimization in Deep Learning with a PID Controller — PIDAO (Chen et al., Nature Communications 2024)\n- An Optimal Control Perspective on Deep Learning and Related Theories (Li et al., arXiv:1908.10920, 2019)\n- Beyond Quadratic Costs: A Bregman Divergence Approach to H-infinity Control (arXiv:2505.00319, 2025)\n- Data-Driven Adaptive PID Control Based on Physics-Informed Neural Networks (arXiv:2510.04591, Oct 2025)\n- SIGMA: Scalable Spectral Insights for LLM Model Collapse (arXiv:2601.03385, Jan 2026)\n- RankMe: Assessing the Downstream Performance of Pretrained Self-Supervised Representations by Their Rank (Garrido et al., ICML 2023, arXiv:2210.02885)\n- Combatting Dimensional Collapse in LLM Pre-Training Data via Diversified File Selection — DiSF (arXiv:2504.20644, Apr 2025)\n- Controlled LLM Training on Spectral Sphere — SSO (arXiv:2601.08393, Jan 2026)\n- Spectral Lens: Activation and Gradient Spectra as Diagnostics of LLM Optimization (arXiv:2605.05683, May 2026)\n- Entropy-Reservoir Bregman Projection: An Information-Geometric Unification of Model Collapse — ERBP (arXiv:2512.14879, Dec 2025)\n- A Closer Look at Model Collapse: From a Generalization-to-Memorization Perspective (Shi et al., arXiv:2509.16499, NeurIPS 2025 Spotlight)\n- Countering Model Collapse in Iterative Self-Training via Dynamic Center-Edge Sampling — DCES (Electronics, Feb 2026)\n- Learning by Surprise: Surplexity for Mitigating Model Collapse (arXiv:2410.12341, 2024)\n- Position: Model Collapse Does Not Mean What You Think (Schaeffer et al., arXiv:2503.03150, ICML 2025)\n- Demystifying Synthetic Data in LLM Pre-training (Kang et al., EMNLP 2025, arXiv:2510.01631)\n- Collapse or Thrive? Perils and Promises of Synthetic Data (Kazdan et al., ICML 2025)\n- From Collapse to Improvement: Statistical Perspectives on Iterative Training (Bakshi & Chakraborty, arXiv:2602.10531, Feb 2026)\n- When Models Don't Collapse: On the Consistency of Iterative MLE (Barzilai & Shamir, arXiv:2505.19046, ICML 2025)\n- Strong Model Collapse (ICLR 2025, arXiv:2410.04840)\n- Data Mixing for Large Language Models Pretraining: A Survey and Outlook (Chen et al., arXiv:2604.16380, Mar 2026)\n- DoReMi: Optimizing Data Mixtures Speeds Up Language Model Pretraining (NeurIPS 2023)\n- Machine-generated text detection prevents language model collapse (Drayson et al., arXiv:2502.15654, 2025)\n- Rethinking Data Mixing from the Perspective of LLMs — DoGraph (arXiv:2604.07963, 2026)\n- Preventing Model Collapse Under Overparametrization: Optimal Mixing Ratios (arXiv:2509.22341, 2025)\n- AI models collapse when trained on recursively generated data (Shumailov et al., Nature 2024)\n- Mind the Gap: A Spectral Analysis of Rank Collapse and Signal Propagation in Attention Layers (arXiv:2410.07799, ICML 2025)\n- Monitoring Neural Training with Topology: A Footprint-Predictable Collapse Index (arXiv:2604.26984, Apr 2026)\n- Escaping Mode Collapse in LLM Generation via Geometric Regulation (arXiv:2605.00435, May 2026)\n- Online Convex Programming and Generalized Infinitesimal Gradient Ascent (Zinkevich, ICML 2003)\n- Non-Stationary Stochastic Optimization (Besbes, Gur & Zeevi, Operations Research 2015)\n- Towards Next-Generation LLM Training: From the Perspective of Data (arXiv:2603.14712, Mar 2026)\n\n## Reviewer Evaluation\n\n**Scores**:\n  - clarity: **{'rationale': 'Exceptionally well-organized: explicit success thresholds (>1pp perplexity, >1.5% downstream), tiered theoretical contribution with honest scope acknowledgment, phased experimental design with clear GO/NO-GO criteria, and multiple publishable framings (primary, secondary, negative result). The intellectual honesty about improvement margins and theoretical difficulty is exemplary.', 'score': 4}**/5\n  - feasibility: **{'rationale': 'Compute verified independently: Pythia-1B at 2B tokens per generation costs ~8 H100-hours; total ~185 H100-hours fits the 200-hour constraint. EMNLP deadline confirmed May 25. Timeline is tight but de-risked by front-loaded theory (days 1-2), dual GO/NO-GO gates (day 3), tiered theoretical framing, and the fact that 3 conditions can partially parallelize across 8 GPUs.', 'score': 4}**/5\n  - impact: **{'rationale': 'Addresses the EMNLP 2026 special theme on data contamination and synthetic data feedback loops directly. The contribution operates at two levels: (1) establishing spectral indicators as closed-loop control signals for data governance (extending SIGMA/DiSF from monitoring/offline to active control), and (2) providing the first empirical test of whether adaptive mixing meaningfully beats the optimal fixed weight under iterative dynamics. Even the secondary framing (spectral indicators as higher-resolution collapse signals) has independent community value.', 'score': 4}**/5\n  - novelty: **{'rationale': 'The specific integration of spectral collapse indicators into a closed-loop PI controller for synthetic-to-real ratio adjustment is independently verified as a genuine gap. Individual components (PI control, spectral metrics, adaptive mixing) are established, but the combination addresses a specific unsolved problem with a clear theoretical grounding via ERBP. PDS (ICLR 2025 Oral) uses control theory for data selection but is offline/PMP-based/non-spectral — different enough to not undermine novelty.', 'score': 4}**/5\n\n## Human Review Note\n\n## Agent 审核结果（完整三阶段 pipeline）\n\n**Verdict**: PASS\n\n**入口三重共识 (X)**: 23.0%\n**终审自评 (Y)**: 35.0%\n**出口三重共识 (Z)**: 34.0%\n**Z 区间**: [28.0%, 39.0%]\n**真实提升 (Z-X)**: +11.0 pp\n**幻觉幅度 (Y-Z)**: +1.0 pp\n**出口一致性**: 高\n**出口三次评估**: [34.0, 37.0, 31.0]\n\n### 优化方案 / 拒绝详情\n【优化方案】\n\n1. **[标题]** — 从 \"Spectral Collapse-Aware Adaptive Mixing via Entropy-Reservoir PI Control for Iterative Synthetic-Real LLM Pretraining\" 改为 \"Spectral Collapse Indicators as Closed-Loop Control Signals for Adaptive Synthetic-Real Data Mixing in Iterative Language Model Pretraining\"。去掉控制论术语密度（\"PI Control\"、\"Entropy-Reservoir\"），前置 \"Spectral Collapse Indicators\" 和 \"Language Model\"，让 EMNLP reviewer 在标题层即感知 NLP relevance。 — [Significance / venue fit]\n\n2. **[核心叙事弧线 — Introduction 全面重构]** — 原始 proposal 以 PI controller 设计为叙事中心，四个 contribution 工程式平铺。改为 NLP 研究问题驱动的叙事：先提出\"迭代合成预训练如何系统性损害语言能力？退化是均匀的还是结构化的？\"，再引出\"因此需要能捕捉退化结构的信号（spectral rank）而非标量聚合（perplexity）\"，最后引出\"基于此设计闭环控制器作为精确控制 collapse 程度的工具\"。CC1/CC2 从研究对象变为服务于 NLP 研究问题的 instrument。这是从原始 proposal 到最终版本最根本性的转变。 — [Novelty + Significance — 从 \"又一个 adaptive mixing method\" 变为 \"NLP investigation of structured linguistic collapse + spectral control as instrument\"]\n\n3. **[新增 2×2 定位矩阵 — Figure 1]** — 原始 proposal 以文字列表罗列 Aioli/SIGMA/DiSF 等相关工作的定位。改为 (signal type: loss-based vs. spectral) × (usage mode: offline/monitoring vs. online closed-loop) 的 2×2 可视化矩阵，明确标注本文占据的空白象限。放在 Introduction 第一页，让 reviewer 30 秒内抓住核心 positioning。 — [Novelty / Clarity — 降低 reviewer 误判 novelty 的概率]\n\n4. **[新增 Key Insight 章节 — Leading vs. Lagging Indicator 假设 + Toy Model Sketch]** — 原始 proposal 对 spectral vs. perplexity 的差异只有隐含的工程直觉。新增独立章节，构建三层论证：(a) 引用 Jing et al. 2022 \"Understanding Dimensional Collapse\" 建立类比（loss plateaus while representations degenerate）；(b) 提供 toy model sketch——线性 representation 在高斯混合下，spectral rank 对方向性收缩的响应先于 cross-entropy 对聚合分布偏移的响应，因为 loss components 可互相抵消而 spectral entropy 不能；(c) 明确标注为 pre-registered hypothesis 而非 assumption，实验设计含显式验证。 — [Technical Soundness + Novelty — 将 empirical finding 升级为 \"theory-motivated prediction + experimental validation\" 的双层结构]\n\n5. **[新增 Non-trivial Integration Challenges 章节]** — 原始 proposal 无此讨论，容易被 reviewer 解读为\"把 RankMe 指标插入 PI controller 的 trivial 工程集成\"。新增三点非平凡性论证：(a) 离散代际信号的量化噪声与平滑设计；(b) setpoint 跨规\n\n",
      "numLines": 169,
      "startLine": 1,
      "totalLines": 169
    }
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
I now have comprehensive information about both SIGMA and our project. Let me compile the deep analysis report and save it as an artifact.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "878c4496-b0e1-4890-b809-65989552555b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxbQqgck1TicfmWdDkxV1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 36344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12531
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

_source line 38_

信息已充分。现在编写分析报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "484eb367-e508-4623-b957-254a72387a1b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxbQqgck1TicfmWdDkxV1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 36344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12531
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

_source line 39_

<details open><summary>🔧 Tool call — Bash · `toolu_01DUesAczRUp5rxytjL9h5d3`</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/",
  "description": "List existing artifacts"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "19b41253-646b-4f69-98de-544a0e43b58c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01AxbQqgck1TicfmWdDkxV1B",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 12531,
      "cache_read_input_tokens": 36344,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12531
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

_source line 40 · 2026-05-12T17:30:35.521Z_

<details><summary>↩ Tool result · `toolu_01DUesAczRUp5rxytjL9h5d3`</summary>

```text
_project
code
diag_mvp_pilot_v4.md
literature_survey_spectral_collapse.md
manifest.yaml
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "b8ca9ea6-26d6-4b22-a8b4-fadd74286f9d",
  "tool_use_result": {
    "stdout": "_project\ncode\ndiag_mvp_pilot_v4.md\nliterature_survey_spectral_collapse.md\nmanifest.yaml",
    "stderr": "",
    "interrupted": false,
    "isImage": false,
    "noOutputExpected": false
  }
}
```

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — Write · `toolu_01Q2Po966uBCoU7MHsmcVPnw`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md",
  "content": "# SIGMA Deep Analysis: Precise Differentiation from Collapse-Aware Mixing\n\n> Generated: 2026-05-12 | Source: arXiv:2601.03385 v3 (2026-03-23)\n> Authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\n> Venue: arXiv preprint (no conference acceptance as of 2026-05)\n\n---\n\n## 1. SIGMA 技术方法详解\n\n### 1.1 谱指标：log-determinant, 非有效秩\n\nSIGMA 的核心指标是 **Gram 矩阵的 log-determinant**（`log|G| = Σ log(λⱼ)`），而非 spectral effective rank。具体实现为两条并行的诊断轨道：\n\n| | Track I (确定性) | Track II (随机性) |\n|---|---|---|\n| **公式** | `𝒢_KF(δ) = Σ log(1 + λᵢ(G_A)/(β̂_k+δ))` | `𝒰_LLN,cov(δ) = log det(G_A+δI) - m·log(n_A)` |\n| **理论基础** | Weyl 不等式 + Ky Fan 优超 | 大数定律缩放 |\n| **性质** | 保守的上界包络（distribution-free） | 灵敏的统计估计量 |\n| **敏感度** | 低（S2 下几乎平坦，slope ≈ +2.35） | 高（S2 下 slope ≈ -42.6） |\n\n**关键区别**：SIGMA 用 log-determinant（特征值的对数之和），我们用 **spectral effective rank = exp(H(σ))**（归一化奇异值分布的 Shannon 熵的指数）。两者虽然都基于谱分析，但数学定义不同：\n- log-det 对所有特征值等权求和，对小特征值的变化极其敏感（log 在零附近放大）\n- effective rank 先归一化为概率分布再算熵，反映的是谱的\"均匀程度\"而非\"总量\"\n- effective rank 有界（∈ [1, m]），更适合作为控制器输入信号\n\n### 1.2 分析层级：仅 embedding 层\n\nSIGMA 分析的是 **sentence embeddings**（m=384 维），使用冻结的 sentence encoder 提取。不分析 weight matrices、hidden states 或 attention patterns。\n\nGram 矩阵定义：`G = M·Mᵀ ∈ S⁺ᵐ`，其中 M ∈ ℝ^(m×n) 将 embedding 向量排列为列。\n\n我们的方法同样使用 embedding 层 Gram 矩阵，但用模型自身的 final-layer hidden states（非外部 sentence encoder），更直接反映模型内部表征健康度。\n\n### 1.3 可扩展估计：子采样 + Cholesky\n\nSIGMA 避免全矩阵特征分解的方法：\n1. 仅计算 n_A 列的子 Gram 矩阵 G_A（n_A > m 即可）\n2. 用 Cholesky 分解计算 log-det（`log det = 2Σ log Lᵢᵢ`），O(m³) 复杂度\n3. 通过 Theorem 2 的缩放律 `m·log(n/n_A)` 估计全 Gram 矩阵的 log-det\n4. Theorem 3 给出估计误差的置信区间，精度仅依赖 n_A，与总语料大小 n 无关\n\n### 1.4 实验设置\n\n| 参数 | SIGMA | 我们（MVP pilot） |\n|------|-------|-------------------|\n| 模型 | OPT-125M (125M) | Pythia-1B (1B) |\n| 数据集 | TECH corpus (1000 contexts × 64 tokens) | wikitext-103-raw-v1 |\n| 迭代代数 | 50 代 | 3 代（pilot），5 代（full） |\n| 每代 epoch | 5 | - |\n| 合成比例 | α=0.0（纯合成） | 动态调节（PI 控制） |\n| Embedding 维度 | 384（外部 encoder） | 模型自身 hidden dim |\n| 评估指标 | log-det, Distinct-2, HHI | effective rank, PPL, KL, n-gram entropy |\n\n### 1.5 两种实验设置\n\n- **S1 (Restart-from-base)**：每代重新生成合成数据，但训练总是从同一个 base model 重启。隔离数据递归效应。\n- **S2 (True recursion)**：权重跨代继续训练，形成自蒸馏反馈环。\n\n实验结果：\n- S1: Track II 缓慢下降（slope ≈ -0.94/代，50 代后总漂移 ≈ -151）\n- S2: Track II 急剧下降（slope ≈ -42.6/代，50 代后总漂移 ≈ -1537），而 Track I 几乎不变\n- 两条轨道的发散本身被用作早期 collapse 的诊断信号\n\n---\n\n## 2. Leading Indicator 验证\n\n### SIGMA 未做的事情\n\n**SIGMA 未验证 leading indicator 特性。** 论文未报告：\n- 谱指标与 perplexity 的时序对比\n- 谱指标相对于 PPL 的提前预警时间\n- 谱指标与下游任务性能的相关性分析\n\nSIGMA 仅展示了 Track I 与 Track II 的发散模式作为 collapse 的诊断签名，但未与传统性能指标（PPL、loss）做时序竞赛。论文明确承认缺乏预测能力：\"measures collapse states but does not predict failure before output degradation becomes visible\"。\n\n### 我们的差异化机会\n\n这是一个关键的 contribution 空间。我们的 MVP pilot 核心假设正是验证 **spectral effective rank 作为 PPL 的 leading indicator**——即谱有效秩在 PPL 尚未显著上升时已经开始下降。这是 SIGMA 完全未触及的。\n\n---\n\n## 3. 控制机制\n\n### SIGMA：纯监控，无控制\n\nSIGMA 是一个 **纯诊断/监控框架**。论文未提出任何：\n- 数据混合比例调节\n- 训练干预策略\n- 反馈控制机制\n- 缓解措施建议\n\n未来工作方向是 Koopman Operator Theory——从\"监控状态\"过渡到\"预测动力学\"，但仍然是预测，不是控制。\n\n### 我们：闭环 PI 控制\n\n我们的核心 novelty：\n- 谱有效秩 → PI 控制器输入\n- PI 控制器 → 实时调节 real/synthetic 混合比例 w_t\n- 公式：`w_t = w_{t-1} - Kp·(r_t - r_{t-1}) - Ki·(r_t - r_target)`\n- rank 下降 → 增加真实数据比例；rank 恢复 → 减少真实数据比例\n- 有离散时间稳定性分析（Tier 1）和 ERBP 连接（Tier 2）\n\n---\n\n## 4. 精确对比矩阵\n\n| 维度 | SIGMA | 我们 (Collapse-Aware Mixing) |\n|------|-------|------------------------------|\n| **谱指标** | log-determinant of Gram matrix | spectral effective rank = exp(H(σ)) |\n| **分析对象** | 外部 sentence encoder embeddings (m=384) | 模型自身 final-layer hidden states |\n| **诊断 vs 控制** | 纯监控/诊断 | 闭环 PI 控制器 |\n| **Leading indicator** | 未验证 | 核心假设 + 实验验证 |\n| **数据混合** | 未涉及（纯合成 α=0） | real/synthetic 动态混合比例 |\n| **理论贡献** | 确定性/随机性谱界（3 个定理） | PI 稳定性 + ERBP 连接（tiered） |\n| **控制理论** | 无 | 离散时间 PI 稳定性条件 |\n| **ERBP 连接** | 无 | λ·s_min > κ 条件驱动 setpoint |\n| **实验规模** | OPT-125M, 50 代, 极小数据 | Pythia-1B, 3-5 代, wikitext-103 |\n| **应用场景** | 递归训练管线健康监控 | 迭代合成预训练的数据治理 |\n| **代码** | 未公开 | - |\n| **发表状态** | arXiv preprint (未被会议接收) | 目标 EMNLP 2026 |\n\n---\n\n## 5. SIGMA 的局限性 = 我们的 Contribution 空间\n\n### 5.1 无控制机制（最大差异）\nSIGMA 在检测到 collapse 后无法做任何事情。我们将谱信号接入闭环控制器，实现\"从被动监控到主动干预\"。\n\n### 5.2 未验证 leading indicator\nSIGMA 未与 PPL/loss 做时序对比。我们的 pilot 明确测试谱有效秩是否领先于 PPL 下降。\n\n### 5.3 纯合成设置，未考虑混合场景\nSIGMA 实验仅在 α=0（100% 合成）设置下运行，未研究 real/synthetic 混合场景。我们的方法核心就是动态混合。\n\n### 5.4 极小实验规模\nOPT-125M + 1000 条 64-token 上下文（~64K tokens）。我们用 Pythia-1B + wikitext-103（~100M tokens/代），更接近实际预训练规模。\n\n### 5.5 外部 encoder 依赖\nSIGMA 依赖冻结的外部 sentence encoder (384 维) 提取 embeddings。这引入了额外依赖，且 encoder 本身可能对某些 collapse 模式不敏感。我们直接用模型自身的 hidden states。\n\n### 5.6 理论聚焦于界，非控制\nSIGMA 的三个定理建立的是谱界（bounds），不涉及如何利用这些信号做决策。我们建立 PI 控制器稳定性条件并连接到 ERBP 的信息几何框架。\n\n### 5.7 Track I 保守性\nTrack I 在 S2 设置下几乎平坦（slope ≈ +2.35），对 true recursion collapse 不敏感。两条轨道的发散虽然可以作为诊断信号，但需要同时维护两个指标增加了复杂度。我们的 effective rank 是单一标量信号。\n\n### 5.8 无预测/预判能力\n论文自承\"measures collapse states but does not predict failure\"。Koopman operator 方向是未来工作。\n\n---\n\n## 6. Paper Positioning 素材\n\n### 6.1 Introduction 定位（建议措辞）\n\n> Recent work has shown that spectral analysis of embedding Gram matrices can detect representational collapse in LLMs. SIGMA (Gu et al., 2026) derives deterministic and stochastic bounds on the log-determinant of the Gram matrix, providing a scalable monitoring framework that captures collapse-induced contraction of the representation space. However, SIGMA operates purely as a diagnostic tool — detecting collapse states post-hoc without providing mechanisms for intervention or prevention. We take the next step: integrating spectral collapse indicators into a closed-loop PI controller that dynamically adjusts the synthetic-to-real data mixing ratio to actively prevent collapse during iterative training.\n\n### 6.2 Related Work 定位（建议段落）\n\n> **Spectral collapse monitoring.** SIGMA (Gu et al., 2026) introduces a two-track framework for monitoring model collapse via the log-determinant of the embedding Gram matrix. Their deterministic bound (Track I) provides a conservative envelope via Weyl's inequality, while the stochastic estimator (Track II) offers greater sensitivity, detecting collapse an order of magnitude earlier than Track I in true-recursion settings. However, SIGMA differs from our approach in several key respects: (1) they use the log-determinant metric, while we use spectral effective rank (exp(H(σ))), which provides a bounded, normalized signal more suitable as a controller input; (2) they analyze embeddings from a frozen external sentence encoder rather than the model's own representations; (3) they validate only on OPT-125M with a corpus of ~64K tokens across 50 generations, while we target Pythia-1B scale with 100M+ tokens per generation; and most critically, (4) they use spectral metrics purely for monitoring, whereas we integrate them into a PI controller for active data composition adjustment. SIGMA explicitly identifies the transition from monitoring to prediction as future work; we address the complementary gap of transitioning from monitoring to control.\n\n### 6.3 核心 Framing\n\n**一句话定位**：SIGMA 证明了\"谱分析能检测 collapse\"；我们回答\"检测到 collapse 后怎么办\"。\n\n**Contribution 矩阵定位**（2×2 象限图）：\n\n```\n                  Offline/Monitoring    Online/Closed-loop\n                  ─────────────────    ──────────────────\nLoss-based    │   DoReMi, Aioli       AC-ODM (withdrawn)\n              │\nSpectral      │   SIGMA, DiSF         ★ Ours ★\n```\n\n我们占据的是 **spectral × online closed-loop** 的空白象限。\n\n### 6.4 不应 claim 的\n\n- ~~首次将谱分析用于 LLM collapse 检测~~（SIGMA 在先）\n- ~~首次使用 Gram 矩阵分析 collapse~~（SIGMA 在先）\n- ~~首次提出 scalable 的谱 collapse 指标~~（SIGMA 的子采样方法在先）\n\n### 6.5 可以 claim 的\n\n1. **首次将谱 collapse 指标用于闭环控制**（SIGMA 纯监控，DiSF 是离线选择，SSO 是权重空间）\n2. **首次验证 effective rank 作为 PPL 的 leading indicator**（SIGMA 未做时序对比）\n3. **首次连接 ERBP 稳定性条件与 PI 控制器设计**（ERBP 未提供动态调节机制）\n4. **首次在迭代 synthetic-real 混合场景下实现自适应数据比例控制**（有别于 generic domain mixing 的 Aioli/GRAPE）\n\n---\n\n## 7. 风险评估\n\n| 风险 | 概率 | 影响 | 缓解 |\n|------|------|------|------|\n| Reviewer 认为我们只是\"SIGMA + PI controller 的 trivial 拼接\" | 中 | 高 | 强调 non-trivial integration challenges（信号量化噪声、setpoint 跨规模迁移、ERBP 连接），用 toy model 论证 effective rank 与 log-det 的本质差异 |\n| SIGMA 在 camera-ready 前被 ICML/NeurIPS 接收，reviewer 期待与其对比实验 | 低 | 中 | 准备 log-det vs effective rank 的消融实验作为 appendix |\n| Reviewer 要求解释为何不直接使用 SIGMA 的 log-det 而用 effective rank | 高 | 低 | effective rank 有界 [1,m] 适合控制器输入，log-det 无界且对正则化参数 δ 敏感 |\n\n---\n\n## 8. 补充：SIGMA 未引用/未涉及的框架\n\nSIGMA 未引用 ERBP、EntroPIC、RankMe，也未涉及 PI/PID 控制、数据混合优化、或 dynamic regret theory。这些都是我们独立的理论支柱。\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "8e0792df-d027-4bbf-9697-1d742db4a9f9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WXV9RHDTm36cuc89WQPLQz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 203,
      "cache_read_input_tokens": 48875,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 203
      },
      "output_tokens": 59,
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

_source line 42 · 2026-05-12T17:32:28.928Z_

<details><summary>↩ Tool result · `toolu_01Q2Po966uBCoU7MHsmcVPnw`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "978ffaf6-2677-47c3-932b-c5b67d199df2",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md",
    "content": "# SIGMA Deep Analysis: Precise Differentiation from Collapse-Aware Mixing\n\n> Generated: 2026-05-12 | Source: arXiv:2601.03385 v3 (2026-03-23)\n> Authors: Yi Gu, Lingyou Pang, Xiangkun Ye, Tianyu Wang, Jianyu Lin, Carey E. Priebe, Alexander Aue\n> Venue: arXiv preprint (no conference acceptance as of 2026-05)\n\n---\n\n## 1. SIGMA 技术方法详解\n\n### 1.1 谱指标：log-determinant, 非有效秩\n\nSIGMA 的核心指标是 **Gram 矩阵的 log-determinant**（`log|G| = Σ log(λⱼ)`），而非 spectral effective rank。具体实现为两条并行的诊断轨道：\n\n| | Track I (确定性) | Track II (随机性) |\n|---|---|---|\n| **公式** | `𝒢_KF(δ) = Σ log(1 + λᵢ(G_A)/(β̂_k+δ))` | `𝒰_LLN,cov(δ) = log det(G_A+δI) - m·log(n_A)` |\n| **理论基础** | Weyl 不等式 + Ky Fan 优超 | 大数定律缩放 |\n| **性质** | 保守的上界包络（distribution-free） | 灵敏的统计估计量 |\n| **敏感度** | 低（S2 下几乎平坦，slope ≈ +2.35） | 高（S2 下 slope ≈ -42.6） |\n\n**关键区别**：SIGMA 用 log-determinant（特征值的对数之和），我们用 **spectral effective rank = exp(H(σ))**（归一化奇异值分布的 Shannon 熵的指数）。两者虽然都基于谱分析，但数学定义不同：\n- log-det 对所有特征值等权求和，对小特征值的变化极其敏感（log 在零附近放大）\n- effective rank 先归一化为概率分布再算熵，反映的是谱的\"均匀程度\"而非\"总量\"\n- effective rank 有界（∈ [1, m]），更适合作为控制器输入信号\n\n### 1.2 分析层级：仅 embedding 层\n\nSIGMA 分析的是 **sentence embeddings**（m=384 维），使用冻结的 sentence encoder 提取。不分析 weight matrices、hidden states 或 attention patterns。\n\nGram 矩阵定义：`G = M·Mᵀ ∈ S⁺ᵐ`，其中 M ∈ ℝ^(m×n) 将 embedding 向量排列为列。\n\n我们的方法同样使用 embedding 层 Gram 矩阵，但用模型自身的 final-layer hidden states（非外部 sentence encoder），更直接反映模型内部表征健康度。\n\n### 1.3 可扩展估计：子采样 + Cholesky\n\nSIGMA 避免全矩阵特征分解的方法：\n1. 仅计算 n_A 列的子 Gram 矩阵 G_A（n_A > m 即可）\n2. 用 Cholesky 分解计算 log-det（`log det = 2Σ log Lᵢᵢ`），O(m³) 复杂度\n3. 通过 Theorem 2 的缩放律 `m·log(n/n_A)` 估计全 Gram 矩阵的 log-det\n4. Theorem 3 给出估计误差的置信区间，精度仅依赖 n_A，与总语料大小 n 无关\n\n### 1.4 实验设置\n\n| 参数 | SIGMA | 我们（MVP pilot） |\n|------|-------|-------------------|\n| 模型 | OPT-125M (125M) | Pythia-1B (1B) |\n| 数据集 | TECH corpus (1000 contexts × 64 tokens) | wikitext-103-raw-v1 |\n| 迭代代数 | 50 代 | 3 代（pilot），5 代（full） |\n| 每代 epoch | 5 | - |\n| 合成比例 | α=0.0（纯合成） | 动态调节（PI 控制） |\n| Embedding 维度 | 384（外部 encoder） | 模型自身 hidden dim |\n| 评估指标 | log-det, Distinct-2, HHI | effective rank, PPL, KL, n-gram entropy |\n\n### 1.5 两种实验设置\n\n- **S1 (Restart-from-base)**：每代重新生成合成数据，但训练总是从同一个 base model 重启。隔离数据递归效应。\n- **S2 (True recursion)**：权重跨代继续训练，形成自蒸馏反馈环。\n\n实验结果：\n- S1: Track II 缓慢下降（slope ≈ -0.94/代，50 代后总漂移 ≈ -151）\n- S2: Track II 急剧下降（slope ≈ -42.6/代，50 代后总漂移 ≈ -1537），而 Track I 几乎不变\n- 两条轨道的发散本身被用作早期 collapse 的诊断信号\n\n---\n\n## 2. Leading Indicator 验证\n\n### SIGMA 未做的事情\n\n**SIGMA 未验证 leading indicator 特性。** 论文未报告：\n- 谱指标与 perplexity 的时序对比\n- 谱指标相对于 PPL 的提前预警时间\n- 谱指标与下游任务性能的相关性分析\n\nSIGMA 仅展示了 Track I 与 Track II 的发散模式作为 collapse 的诊断签名，但未与传统性能指标（PPL、loss）做时序竞赛。论文明确承认缺乏预测能力：\"measures collapse states but does not predict failure before output degradation becomes visible\"。\n\n### 我们的差异化机会\n\n这是一个关键的 contribution 空间。我们的 MVP pilot 核心假设正是验证 **spectral effective rank 作为 PPL 的 leading indicator**——即谱有效秩在 PPL 尚未显著上升时已经开始下降。这是 SIGMA 完全未触及的。\n\n---\n\n## 3. 控制机制\n\n### SIGMA：纯监控，无控制\n\nSIGMA 是一个 **纯诊断/监控框架**。论文未提出任何：\n- 数据混合比例调节\n- 训练干预策略\n- 反馈控制机制\n- 缓解措施建议\n\n未来工作方向是 Koopman Operator Theory——从\"监控状态\"过渡到\"预测动力学\"，但仍然是预测，不是控制。\n\n### 我们：闭环 PI 控制\n\n我们的核心 novelty：\n- 谱有效秩 → PI 控制器输入\n- PI 控制器 → 实时调节 real/synthetic 混合比例 w_t\n- 公式：`w_t = w_{t-1} - Kp·(r_t - r_{t-1}) - Ki·(r_t - r_target)`\n- rank 下降 → 增加真实数据比例；rank 恢复 → 减少真实数据比例\n- 有离散时间稳定性分析（Tier 1）和 ERBP 连接（Tier 2）\n\n---\n\n## 4. 精确对比矩阵\n\n| 维度 | SIGMA | 我们 (Collapse-Aware Mixing) |\n|------|-------|------------------------------|\n| **谱指标** | log-determinant of Gram matrix | spectral effective rank = exp(H(σ)) |\n| **分析对象** | 外部 sentence encoder embeddings (m=384) | 模型自身 final-layer hidden states |\n| **诊断 vs 控制** | 纯监控/诊断 | 闭环 PI 控制器 |\n| **Leading indicator** | 未验证 | 核心假设 + 实验验证 |\n| **数据混合** | 未涉及（纯合成 α=0） | real/synthetic 动态混合比例 |\n| **理论贡献** | 确定性/随机性谱界（3 个定理） | PI 稳定性 + ERBP 连接（tiered） |\n| **控制理论** | 无 | 离散时间 PI 稳定性条件 |\n| **ERBP 连接** | 无 | λ·s_min > κ 条件驱动 setpoint |\n| **实验规模** | OPT-125M, 50 代, 极小数据 | Pythia-1B, 3-5 代, wikitext-103 |\n| **应用场景** | 递归训练管线健康监控 | 迭代合成预训练的数据治理 |\n| **代码** | 未公开 | - |\n| **发表状态** | arXiv preprint (未被会议接收) | 目标 EMNLP 2026 |\n\n---\n\n## 5. SIGMA 的局限性 = 我们的 Contribution 空间\n\n### 5.1 无控制机制（最大差异）\nSIGMA 在检测到 collapse 后无法做任何事情。我们将谱信号接入闭环控制器，实现\"从被动监控到主动干预\"。\n\n### 5.2 未验证 leading indicator\nSIGMA 未与 PPL/loss 做时序对比。我们的 pilot 明确测试谱有效秩是否领先于 PPL 下降。\n\n### 5.3 纯合成设置，未考虑混合场景\nSIGMA 实验仅在 α=0（100% 合成）设置下运行，未研究 real/synthetic 混合场景。我们的方法核心就是动态混合。\n\n### 5.4 极小实验规模\nOPT-125M + 1000 条 64-token 上下文（~64K tokens）。我们用 Pythia-1B + wikitext-103（~100M tokens/代），更接近实际预训练规模。\n\n### 5.5 外部 encoder 依赖\nSIGMA 依赖冻结的外部 sentence encoder (384 维) 提取 embeddings。这引入了额外依赖，且 encoder 本身可能对某些 collapse 模式不敏感。我们直接用模型自身的 hidden states。\n\n### 5.6 理论聚焦于界，非控制\nSIGMA 的三个定理建立的是谱界（bounds），不涉及如何利用这些信号做决策。我们建立 PI 控制器稳定性条件并连接到 ERBP 的信息几何框架。\n\n### 5.7 Track I 保守性\nTrack I 在 S2 设置下几乎平坦（slope ≈ +2.35），对 true recursion collapse 不敏感。两条轨道的发散虽然可以作为诊断信号，但需要同时维护两个指标增加了复杂度。我们的 effective rank 是单一标量信号。\n\n### 5.8 无预测/预判能力\n论文自承\"measures collapse states but does not predict failure\"。Koopman operator 方向是未来工作。\n\n---\n\n## 6. Paper Positioning 素材\n\n### 6.1 Introduction 定位（建议措辞）\n\n> Recent work has shown that spectral analysis of embedding Gram matrices can detect representational collapse in LLMs. SIGMA (Gu et al., 2026) derives deterministic and stochastic bounds on the log-determinant of the Gram matrix, providing a scalable monitoring framework that captures collapse-induced contraction of the representation space. However, SIGMA operates purely as a diagnostic tool — detecting collapse states post-hoc without providing mechanisms for intervention or prevention. We take the next step: integrating spectral collapse indicators into a closed-loop PI controller that dynamically adjusts the synthetic-to-real data mixing ratio to actively prevent collapse during iterative training.\n\n### 6.2 Related Work 定位（建议段落）\n\n> **Spectral collapse monitoring.** SIGMA (Gu et al., 2026) introduces a two-track framework for monitoring model collapse via the log-determinant of the embedding Gram matrix. Their deterministic bound (Track I) provides a conservative envelope via Weyl's inequality, while the stochastic estimator (Track II) offers greater sensitivity, detecting collapse an order of magnitude earlier than Track I in true-recursion settings. However, SIGMA differs from our approach in several key respects: (1) they use the log-determinant metric, while we use spectral effective rank (exp(H(σ))), which provides a bounded, normalized signal more suitable as a controller input; (2) they analyze embeddings from a frozen external sentence encoder rather than the model's own representations; (3) they validate only on OPT-125M with a corpus of ~64K tokens across 50 generations, while we target Pythia-1B scale with 100M+ tokens per generation; and most critically, (4) they use spectral metrics purely for monitoring, whereas we integrate them into a PI controller for active data composition adjustment. SIGMA explicitly identifies the transition from monitoring to prediction as future work; we address the complementary gap of transitioning from monitoring to control.\n\n### 6.3 核心 Framing\n\n**一句话定位**：SIGMA 证明了\"谱分析能检测 collapse\"；我们回答\"检测到 collapse 后怎么办\"。\n\n**Contribution 矩阵定位**（2×2 象限图）：\n\n```\n                  Offline/Monitoring    Online/Closed-loop\n                  ─────────────────    ──────────────────\nLoss-based    │   DoReMi, Aioli       AC-ODM (withdrawn)\n              │\nSpectral      │   SIGMA, DiSF         ★ Ours ★\n```\n\n我们占据的是 **spectral × online closed-loop** 的空白象限。\n\n### 6.4 不应 claim 的\n\n- ~~首次将谱分析用于 LLM collapse 检测~~（SIGMA 在先）\n- ~~首次使用 Gram 矩阵分析 collapse~~（SIGMA 在先）\n- ~~首次提出 scalable 的谱 collapse 指标~~（SIGMA 的子采样方法在先）\n\n### 6.5 可以 claim 的\n\n1. **首次将谱 collapse 指标用于闭环控制**（SIGMA 纯监控，DiSF 是离线选择，SSO 是权重空间）\n2. **首次验证 effective rank 作为 PPL 的 leading indicator**（SIGMA 未做时序对比）\n3. **首次连接 ERBP 稳定性条件与 PI 控制器设计**（ERBP 未提供动态调节机制）\n4. **首次在迭代 synthetic-real 混合场景下实现自适应数据比例控制**（有别于 generic domain mixing 的 Aioli/GRAPE）\n\n---\n\n## 7. 风险评估\n\n| 风险 | 概率 | 影响 | 缓解 |\n|------|------|------|------|\n| Reviewer 认为我们只是\"SIGMA + PI controller 的 trivial 拼接\" | 中 | 高 | 强调 non-trivial integration challenges（信号量化噪声、setpoint 跨规模迁移、ERBP 连接），用 toy model 论证 effective rank 与 log-det 的本质差异 |\n| SIGMA 在 camera-ready 前被 ICML/NeurIPS 接收，reviewer 期待与其对比实验 | 低 | 中 | 准备 log-det vs effective rank 的消融实验作为 appendix |\n| Reviewer 要求解释为何不直接使用 SIGMA 的 log-det 而用 effective rank | 高 | 低 | effective rank 有界 [1,m] 适合控制器输入，log-det 无界且对正则化参数 δ 敏感 |\n\n---\n\n## 8. 补充：SIGMA 未引用/未涉及的框架\n\nSIGMA 未引用 ERBP、EntroPIC、RankMe，也未涉及 PI/PID 控制、数据混合优化、或 dynamic regret theory。这些都是我们独立的理论支柱。\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Assistant

_source line 43_

注册 artifact。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "6d766eb3-5475-4298-ab5a-c8f4f534144f",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SGacysqpS2mXJhHsCGJkF4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4769,
      "cache_read_input_tokens": 49078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4769
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

_source line 44_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0198K3na86SkxBpEazpWypD7`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__append_idea",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "8a32987e-c5b0-49ec-b762-b999ef0e8bb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SGacysqpS2mXJhHsCGJkF4",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4769,
      "cache_read_input_tokens": 49078,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4769
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

_source line 45 · 2026-05-12T17:32:33.095Z_

<details><summary>↩ Tool result · `toolu_0198K3na86SkxBpEazpWypD7`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__append_idea"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "ff009c70-3157-41c4-97b8-4bed0d239ac2",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__append_idea"
    ],
    "query": "select:mcp__agent-ml-research__append_idea",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Let me register the artifact using the appropriate tool. Let me search for the register_artifact tool.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "5325ae2d-8e19-404e-8446-e7e36f0efa82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAMYJpmPQqZhJTzvSDhmf9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 53847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 47_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016EwsYRgBMkh6ddG9jBH7MD`</summary>

```json
{
  "query": "register_artifact",
  "max_results": 3
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "19de4634-67d6-4cef-b1c4-b6e7032254a3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WAMYJpmPQqZhJTzvSDhmf9",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 401,
      "cache_read_input_tokens": 53847,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 401
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

_source line 48 · 2026-05-12T17:32:37.469Z_

<details><summary>↩ Tool result · `toolu_016EwsYRgBMkh6ddG9jBH7MD`</summary>

```text
No matching deferred tools found
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "628183ae-9dbd-4774-8aab-88ee61a1b6ad",
  "tool_use_result": {
    "matches": [],
    "query": "register_artifact",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Tool call

_source line 49_

<details open><summary>🔧 Tool call — Grep · `toolu_01GCaH8hkNybUmmSAv1SNBwQ`</summary>

```json
{
  "pattern": "register_artifact",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
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
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "9b3f7f53-2876-4e1f-ab97-08ca8836eb15",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ja8wU9s9kUCMYdz7sSrj9b",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 129,
      "cache_read_input_tokens": 54248,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 129
      },
      "output_tokens": 63,
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

_source line 50 · 2026-05-12T17:32:40.466Z_

<details><summary>↩ Tool result · `toolu_01GCaH8hkNybUmmSAv1SNBwQ`</summary>

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
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "45ab1743-b4cf-4cd3-9c12-8e2d0641e1cf",
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

_source line 51_

<details open><summary>🔧 Tool call — Read · `toolu_012441LKiCG7JV4NLE2cnnjF`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "b819819b-ea99-4bfb-a431-d007a003b4cf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018CuMy3jkdRQCgCF6EXCcEk",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 137,
      "cache_read_input_tokens": 54377,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 137
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

_source line 52 · 2026-05-12T17:32:43.495Z_

<details><summary>↩ Tool result · `toolu_012441LKiCG7JV4NLE2cnnjF`</summary>

```text
1	- id: art_20260512_fb1679
2	  name: MVP Pilot 实验代码
3	  type: intermediate
4	  description: 'Pythia-1B 迭代合成训练 pilot 代码：训练循环 (HF Trainer) + 6 项崩塌检测指标 (谱有效秩/token
5	    熵方差/n-gram 熵/词表覆盖率/PPL/代际 KL) + 合成数据生成 + 全流程编排。文件: config.py, data_utils.py, metrics.py,
6	    generate.py, train.py, pilot_pipeline.py, requirements.txt'
7	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/pilot_pipeline.py
8	  url: null
9	  project: collapse-aware-mixing
10	  exp_id: null
11	  skill: ''
12	  created_at: '2026-05-12T08:58:15.853621+00:00'
13	  tags:
14	  - code
15	  - mvp
16	  - pilot
17	  - spectral-rank
18	  - model-collapse
19	- id: art_20260512_b8e7c5
20	  name: controller.py
21	  type: intermediate
22	  description: Discrete-time PI controller for collapse-aware real/synthetic data
23	    mixing (CollapseAwareController + ControllerConfig)
24	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/controller.py
25	  url: null
26	  project: collapse-aware-mixing
27	  exp_id: null
28	  skill: ''
29	  created_at: '2026-05-12T11:23:30.104218+00:00'
30	  tags:
31	  - controller
32	  - pi-controller
33	  - code
34	- id: art_20260512_8f8ca7
35	  name: test_controller.py
36	  type: intermediate
37	  description: '14 unit tests for PI controller: steady state, rank drop, recovery,
38	    clamp, reset, history'
39	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/test_controller.py
40	  url: null
41	  project: collapse-aware-mixing
42	  exp_id: null
43	  skill: ''
44	  created_at: '2026-05-12T11:23:32.519716+00:00'
45	  tags:
46	  - test
47	  - controller
48	  - code
49	- id: art_20260512_5fef4c
50	  name: golden_ratio_baseline.py
51	  type: intermediate
52	  description: Fixed-ratio real/synthetic mixing baseline. G0 100% real, G1+ mixed
53	    at --real_ratio. Outputs JSON summary.
54	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/golden_ratio_baseline.py
55	  url: null
56	  project: collapse-aware-mixing
57	  exp_id: null
58	  skill: ''
59	  created_at: '2026-05-12T12:08:30.601225+00:00'
60	  tags:
61	  - baseline
62	  - code
63	- id: art_20260512_e09205
64	  name: main_experiment.py
65	  type: intermediate
66	  description: 'Full comparative experiment: pure_synthetic vs fixed_mix vs pi_controller.
67	    Shared G0 + independent G1+ conditions. Outputs per-condition + cross-condition
68	    comparison.'
69	  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/main_experiment.py
70	  url: null
71	  project: collapse-aware-mixing
72	  exp_id: null
73	  skill: ''
74	  created_at: '2026-05-12T12:08:36.180477+00:00'
75	  tags:
76	  - experiment
77	  - code
78	- id: art_20260512_e800e5
79	  name: literature_survey_spectral_collapse
80	  type: report
81	  description: 谱指标 × model collapse 文献调研：SIGMA/ERBP/EntroPIC/DIDS 对比分析，novelty gap
82	    评估，paper framing 建议
83	  path: projects/collapse-aware-mixing/artifacts/_project/report/literature_survey_spectral_collapse.md
84	  url: null
85	  project: collapse-aware-mixing
86	  exp_id: null
87	  skill: ''
88	  created_at: '2026-05-12T17:26:36.847365+00:00'
89	  tags:
90	  - literature
91	  - novelty
92	  - framing
93	  - SIGMA
94	  - ERBP
95	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "3420a13e-d879-4631-ae04-a472ab634965",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
      "content": "- id: art_20260512_fb1679\n  name: MVP Pilot 实验代码\n  type: intermediate\n  description: 'Pythia-1B 迭代合成训练 pilot 代码：训练循环 (HF Trainer) + 6 项崩塌检测指标 (谱有效秩/token\n    熵方差/n-gram 熵/词表覆盖率/PPL/代际 KL) + 合成数据生成 + 全流程编排。文件: config.py, data_utils.py, metrics.py,\n    generate.py, train.py, pilot_pipeline.py, requirements.txt'\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/pilot_pipeline.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T08:58:15.853621+00:00'\n  tags:\n  - code\n  - mvp\n  - pilot\n  - spectral-rank\n  - model-collapse\n- id: art_20260512_b8e7c5\n  name: controller.py\n  type: intermediate\n  description: Discrete-time PI controller for collapse-aware real/synthetic data\n    mixing (CollapseAwareController + ControllerConfig)\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/controller.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T11:23:30.104218+00:00'\n  tags:\n  - controller\n  - pi-controller\n  - code\n- id: art_20260512_8f8ca7\n  name: test_controller.py\n  type: intermediate\n  description: '14 unit tests for PI controller: steady state, rank drop, recovery,\n    clamp, reset, history'\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/test_controller.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T11:23:32.519716+00:00'\n  tags:\n  - test\n  - controller\n  - code\n- id: art_20260512_5fef4c\n  name: golden_ratio_baseline.py\n  type: intermediate\n  description: Fixed-ratio real/synthetic mixing baseline. G0 100% real, G1+ mixed\n    at --real_ratio. Outputs JSON summary.\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/golden_ratio_baseline.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T12:08:30.601225+00:00'\n  tags:\n  - baseline\n  - code\n- id: art_20260512_e09205\n  name: main_experiment.py\n  type: intermediate\n  description: 'Full comparative experiment: pure_synthetic vs fixed_mix vs pi_controller.\n    Shared G0 + independent G1+ conditions. Outputs per-condition + cross-condition\n    comparison.'\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/main_experiment.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T12:08:36.180477+00:00'\n  tags:\n  - experiment\n  - code\n- id: art_20260512_e800e5\n  name: literature_survey_spectral_collapse\n  type: report\n  description: 谱指标 × model collapse 文献调研：SIGMA/ERBP/EntroPIC/DIDS 对比分析，novelty gap\n    评估，paper framing 建议\n  path: projects/collapse-aware-mixing/artifacts/_project/report/literature_survey_spectral_collapse.md\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T17:26:36.847365+00:00'\n  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP\n",
      "numLines": 95,
      "startLine": 1,
      "totalLines": 95
    }
  }
}
```

</details>

---

### Tool call

_source line 53_

<details open><summary>🔧 Tool call — Edit · `toolu_01QyVmnjgH9GB246gE78L9go`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
  "old_string": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP",
  "new_string": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP\n- id: art_20260512_a3d1f0\n  name: SIGMA 深度分析报告\n  type: report\n  description: SIGMA (arXiv:2601.03385) 全文技术分析：log-det vs effective rank、无控制机制、未验证\n    leading indicator、实验规模局限。含精确对比矩阵、paper positioning 素材、Related Work 建议措辞。\n  path: projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T19:30:00.000000+00:00'\n  tags:\n  - literature\n  - SIGMA\n  - positioning\n  - related-work\n  - novelty"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "daea29c7-15f0-4126-a4c8-e1b31603ee7d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DXZzai6Pxp17oxNGj2Xg7c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1392,
      "cache_read_input_tokens": 54514,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1392
      },
      "output_tokens": 36,
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

_source line 54 · 2026-05-12T17:32:56.821Z_

<details><summary>↩ Tool result · `toolu_01QyVmnjgH9GB246gE78L9go`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "19ba8b35-19f3-4f18-8281-e670c6e39ed2",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_18/projects/collapse-aware-mixing/artifacts/manifest.yaml",
    "oldString": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP",
    "newString": "  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP\n- id: art_20260512_a3d1f0\n  name: SIGMA 深度分析报告\n  type: report\n  description: SIGMA (arXiv:2601.03385) 全文技术分析：log-det vs effective rank、无控制机制、未验证\n    leading indicator、实验规模局限。含精确对比矩阵、paper positioning 素材、Related Work 建议措辞。\n  path: projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T19:30:00.000000+00:00'\n  tags:\n  - literature\n  - SIGMA\n  - positioning\n  - related-work\n  - novelty",
    "originalFile": "- id: art_20260512_fb1679\n  name: MVP Pilot 实验代码\n  type: intermediate\n  description: 'Pythia-1B 迭代合成训练 pilot 代码：训练循环 (HF Trainer) + 6 项崩塌检测指标 (谱有效秩/token\n    熵方差/n-gram 熵/词表覆盖率/PPL/代际 KL) + 合成数据生成 + 全流程编排。文件: config.py, data_utils.py, metrics.py,\n    generate.py, train.py, pilot_pipeline.py, requirements.txt'\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/pilot_pipeline.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T08:58:15.853621+00:00'\n  tags:\n  - code\n  - mvp\n  - pilot\n  - spectral-rank\n  - model-collapse\n- id: art_20260512_b8e7c5\n  name: controller.py\n  type: intermediate\n  description: Discrete-time PI controller for collapse-aware real/synthetic data\n    mixing (CollapseAwareController + ControllerConfig)\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/controller.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T11:23:30.104218+00:00'\n  tags:\n  - controller\n  - pi-controller\n  - code\n- id: art_20260512_8f8ca7\n  name: test_controller.py\n  type: intermediate\n  description: '14 unit tests for PI controller: steady state, rank drop, recovery,\n    clamp, reset, history'\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/test_controller.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T11:23:32.519716+00:00'\n  tags:\n  - test\n  - controller\n  - code\n- id: art_20260512_5fef4c\n  name: golden_ratio_baseline.py\n  type: intermediate\n  description: Fixed-ratio real/synthetic mixing baseline. G0 100% real, G1+ mixed\n    at --real_ratio. Outputs JSON summary.\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/golden_ratio_baseline.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T12:08:30.601225+00:00'\n  tags:\n  - baseline\n  - code\n- id: art_20260512_e09205\n  name: main_experiment.py\n  type: intermediate\n  description: 'Full comparative experiment: pure_synthetic vs fixed_mix vs pi_controller.\n    Shared G0 + independent G1+ conditions. Outputs per-condition + cross-condition\n    comparison.'\n  path: projects/collapse-aware-mixing/artifacts/_project/intermediate/main_experiment.py\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T12:08:36.180477+00:00'\n  tags:\n  - experiment\n  - code\n- id: art_20260512_e800e5\n  name: literature_survey_spectral_collapse\n  type: report\n  description: 谱指标 × model collapse 文献调研：SIGMA/ERBP/EntroPIC/DIDS 对比分析，novelty gap\n    评估，paper framing 建议\n  path: projects/collapse-aware-mixing/artifacts/_project/report/literature_survey_spectral_collapse.md\n  url: null\n  project: collapse-aware-mixing\n  exp_id: null\n  skill: ''\n  created_at: '2026-05-12T17:26:36.847365+00:00'\n  tags:\n  - literature\n  - novelty\n  - framing\n  - SIGMA\n  - ERBP\n",
    "structuredPatch": [
      {
        "oldStart": 92,
        "oldLines": 3,
        "newStart": 92,
        "newLines": 20,
        "lines": [
          "   - framing",
          "   - SIGMA",
          "   - ERBP",
          "+- id: art_20260512_a3d1f0",
          "+  name: SIGMA 深度分析报告",
          "+  type: report",
          "+  description: SIGMA (arXiv:2601.03385) 全文技术分析：log-det vs effective rank、无控制机制、未验证",
          "+    leading indicator、实验规模局限。含精确对比矩阵、paper positioning 素材、Related Work 建议措辞。",
          "+  path: projects/collapse-aware-mixing/artifacts/sigma_deep_analysis.md",
          "+  url: null",
          "+  project: collapse-aware-mixing",
          "+  exp_id: null",
          "+  skill: ''",
          "+  created_at: '2026-05-12T19:30:00.000000+00:00'",
          "+  tags:",
          "+  - literature",
          "+  - SIGMA",
          "+  - positioning",
          "+  - related-work",
          "+  - novelty"
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

_source line 55_

报告已保存至 `artifacts/sigma_deep_analysis.md`。核心发现：

**SIGMA 与我们的 4 个关键差异：**

1. **谱指标不同**：SIGMA 用 log-determinant（`Σ log λⱼ`），我们用 spectral effective rank（`exp(H(σ))`）。后者有界 [1,m]，更适合作为控制器输入。

2. **纯监控 vs 闭环控制**：SIGMA 无任何干预/控制机制，未来工作方向是 Koopman operator 预测（仍是被动）。我们有 PI 控制器做实时 real/synthetic 比例调节。

3. **未验证 leading indicator**：SIGMA 未做谱指标与 PPL 的时序对比，自承"measures collapse states but does not predict failure"。这是我们的核心假设验证。

4. **实验设置差异大**：OPT-125M + 64K tokens + 外部 sentence encoder vs 我们的 Pythia-1B + wikitext-103 + 模型自身 hidden states。

**Positioning 一句话**：SIGMA 证明了"谱分析能检测 collapse"；我们回答"检测到之后怎么办"——从 passive monitoring 到 active closed-loop control。

Sources:
- [SIGMA: Scalable Spectral Insights for LLM Model Collapse](https://arxiv.org/abs/2601.03385)
- [SIGMA HTML full text](https://arxiv.org/html/2601.03385)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "uuid": "11c55cbc-2110-4126-ab97-869f0654d36d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GWfu3uhrGj6pKgaH6brkqp",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 463,
      "cache_read_input_tokens": 55906,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 463
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

_source line 56_

报告已保存至 `artifacts/sigma_deep_analysis.md`。核心发现：

**SIGMA 与我们的 4 个关键差异：**

1. **谱指标不同**：SIGMA 用 log-determinant（`Σ log λⱼ`），我们用 spectral effective rank（`exp(H(σ))`）。后者有界 [1,m]，更适合作为控制器输入。

2. **纯监控 vs 闭环控制**：SIGMA 无任何干预/控制机制，未来工作方向是 Koopman operator 预测（仍是被动）。我们有 PI 控制器做实时 real/synthetic 比例调节。

3. **未验证 leading indicator**：SIGMA 未做谱指标与 PPL 的时序对比，自承"measures collapse states but does not predict failure"。这是我们的核心假设验证。

4. **实验设置差异大**：OPT-125M + 64K tokens + 外部 sentence encoder vs 我们的 Pythia-1B + wikitext-103 + 模型自身 hidden states。

**Positioning 一句话**：SIGMA 证明了"谱分析能检测 collapse"；我们回答"检测到之后怎么办"——从 passive monitoring 到 active closed-loop control。

Sources:
- [SIGMA: Scalable Spectral Insights for LLM Model Collapse](https://arxiv.org/abs/2601.03385)
- [SIGMA HTML full text](https://arxiv.org/html/2601.03385)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 256081,
  "duration_api_ms": 274420,
  "num_turns": 21,
  "stop_reason": "end_turn",
  "session_id": "4cc3deb9-7265-42d2-8133-7e6f6342b881",
  "total_cost_usd": 0.920296,
  "usage": {
    "input_tokens": 20,
    "cache_creation_input_tokens": 44528,
    "cache_read_input_tokens": 566576,
    "output_tokens": 8057,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 44528,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 438,
        "cache_read_input_tokens": 55906,
        "cache_creation_input_tokens": 463,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 463
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 116503,
      "outputTokens": 4136,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 2,
      "costUSD": 0.15718300000000002,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 20,
      "outputTokens": 8057,
      "cacheReadInputTokens": 566576,
      "cacheCreationInputTokens": 44528,
      "webSearchRequests": 0,
      "costUSD": 0.7631129999999999,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "12e3237e-0557-430b-a535-d3846d82d099"
}
```

</details>

---
