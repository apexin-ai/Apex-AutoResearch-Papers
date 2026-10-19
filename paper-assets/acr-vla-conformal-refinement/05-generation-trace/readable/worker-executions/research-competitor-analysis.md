# research competitor analysis

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 44
- **Recorded user turns:** 0
- **Tool calls:** 15
- **Original source:** `logs/workers/worker_research_competitor-analysis_20260514T071515.log`
- **Structured JSON:** [`cbca479b3b1d286fd27d.json`](../../sessions/cb/cbca479b3b1d286fd27d.json)

## Before a recorded user message

44 recorded events

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
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement",
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
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
    "mcp__agent-ml-research__register_artifact",
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
  "uuid": "0fbafc38-49f4-40b5-8dbc-8b3c6140d329",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-2/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778760600,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "bd77d6fb-d861-4f52-b59c-9f4fcd7c848a",
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
Let me break this task down:

1. Read literature_map.yaml for existing info
2. WebSearch for each competitor paper
3. Write competitor_analysis.md
4. Save and register the artifact

Let me start by reading the literature map and searching for the papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "a5ad1e1f-b02a-4f83-8be8-5c30f6e35201",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015A235v33BCqBt9wpca3eEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11750,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11750
      },
      "output_tokens": 25,
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

_source line 5_

开始执行竞品分析任务。先读取已有文献信息，同时搜索四篇论文的细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "0d279a7d-3d64-4f2c-b89d-41ff0520959e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015A235v33BCqBt9wpca3eEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11750,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11750
      },
      "output_tokens": 25,
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

_source line 6_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01CD3Aozbdt7tGwvmMx7RQKa`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
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
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "4e6aa31e-2927-4ed4-87c5-25f4782d2471",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015A235v33BCqBt9wpca3eEj",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11750,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11750
      },
      "output_tokens": 25,
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

_source line 7 · 2026-05-14T07:15:28.214Z_

<details><summary>↩ Tool result · `toolu_01CD3Aozbdt7tGwvmMx7RQKa`</summary>

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
  "tool_name": "WebSearch"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__save_project_file"
}
```

```json
{
  "type": "tool_reference",
  "tool_name": "mcp__agent-ml-research__register_artifact"
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
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "267db8b4-daf1-4e4c-807e-0e5202a99b40",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "WebSearch",
      "mcp__agent-ml-research__save_project_file",
      "mcp__agent-ml-research__register_artifact"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,WebSearch,mcp__agent-ml-research__save_project_file,mcp__agent-ml-research__register_artifact",
    "total_deferred_tools": 23
  }
}
```

</details>

---

### Assistant

_source line 8_

<details><summary>Logged reasoning block</summary>

```text
Now let me read the literature map and search for all four papers in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "4b1d594b-594e-4420-913c-ef54e4f409dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5KKvRXzRq9TUNTdgiNDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 23591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1929
      },
      "output_tokens": 19,
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

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01Hac3hDRE1k2Z3uUddxziP4`</summary>

```json
{
  "project": "acr-vla-conformal-refinement",
  "file": "literature_map.yaml",
  "max_chars": 0
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "095ce843-dc4d-4d86-a769-820992b9375c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5KKvRXzRq9TUNTdgiNDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 23591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1929
      },
      "output_tokens": 19,
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

_source line 10 · 2026-05-14T07:15:32.529Z_

<details><summary>↩ Tool result · `toolu_01Hac3hDRE1k2Z3uUddxziP4`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\", \"total_chars\": 24446, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "21c5ac12-0368-4cfa-a480-ad2736205fca",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  - bibtex_key: \\\\\\\"a2c2_2025\\\\\\\"\\\\n    title: \\\\\\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\\\\\"\\\\n    authors: \\\\\\\"Sendai et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.23224\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.23224\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"angelopoulos2023gentle\\\\\\\"\\\\n    title: \\\\\\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\\\\\"\\\\n    authors: \\\\\\\"Angelopoulos & Bates\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Foundations and Trends in Machine Learning\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2107.07511\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"barber2023conformal\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction Beyond Exchangeability\\\\\\\"\\\\n    authors: \\\\\\\"Barber et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Annals of Statistics, 51(2):816-845\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2202.13415\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"black2024pi0\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2410.24164\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.24164\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"braun2025cgs\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\\\\\"\\\\n    authors: \\\\\\\"Braun et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.20941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.20941\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"brohan2023rt2\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv:2307.15818\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.15818\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chen2026reconvla\\\\\\\"\\\\n    title: \\\\\\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.16677\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.16677\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"digflow2025\\\\\\\"\\\\n    title: \\\\\\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.01715\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.01715\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"fei2025liberoplus\\\\\\\"\\\\n    title: \\\\\\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.13626\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.13626\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"ghosh2024octo\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Ghosh et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2405.12213\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.12213\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gibbs2021aci\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Inference Under Distribution Shift\\\\\\\"\\\\n    authors: \\\\\\\"Gibbs & Candès\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"NeurIPS 2021\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2106.00170\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"gu2025safe\\\\\\\"\\\\n    title: \\\\\\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Gu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.09937\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"kim2024openvla\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2406.09246\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.09246\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"ledoit2004well\\\\\\\"\\\\n    title: \\\\\\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\\\\\"\\\\n    authors: \\\\\\\"Ledoit & Wolf\\\\\\\"\\\\n    year: 2004\\\\n    venue: \\\\\\\"Journal of Multivariate Analysis, 88(2):365-411\\\\\\\"\\\\n    url: \\\\\\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lipman2023flow\\\\\\\"\\\\n    title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Lipman et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2210.02747\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2023libero\\\\\\\"\\\\n    title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2306.03310\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2026ttvla\\\\\\\"\\\\n    title: \\\\\\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.06748\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.06748\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"luan2026snapflow\\\\\\\"\\\\n    title: \\\\\\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\\\\\"\\\\n    authors: \\\\\\\"Luan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.05656\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.05656\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"robustvla2025\\\\\\\"\\\\n    title: \\\\\\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.01331\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.01331\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"romano2019cqr\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Quantile Regression\\\\\\\"\\\\n    authors: \\\\\\\"Romano et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1905.03222\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shafer2008tutorial\\\\\\\"\\\\n    title: \\\\\\\"A Tutorial on Conformal Prediction\\\\\\\"\\\\n    authors: \\\\\\\"Shafer & Vovk\\\\\\\"\\\\n    year: 2008\\\\n    venue: \\\\\\\"Journal of Machine Learning Research, 9:371-421\\\\\\\"\\\\n    url: \\\\\\\"https://jmlr.org/papers/v9/shafer08a.html\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shukor2025smolvla\\\\\\\"\\\\n    title: \\\\\\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\\\\\"\\\\n    authors: \\\\\\\"Shukor et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2506.01844\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.01844\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"srpo2025\\\\\\\"\\\\n    title: \\\\\\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.15605\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.15605\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"wang2025cploop\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Wang & Ning\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.16376\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16376\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"xing2026diu\\\\\\\"\\\\n    title: \\\\\\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\\\\\"\\\\n    authors: \\\\\\\"Xing et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.00941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.00941\\\\\\\"\\\\n    category: \\\\\\\"uq_flow_matching\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"yuan2026ups\\\\\\\"\\\\n    title: \\\\\\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\\\\\"\\\\n    authors: \\\\\\\"Yuan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.22474\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.22474\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"zhao2024conformalized\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\\\\\"\\\\n    authors: \\\\\\\"Zhao et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"RSS 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.07767\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"cosmos_policy_2026\\\\\\\"\\\\n    title: \\\\\\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.16163\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.16163\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_gse_2026\\\\\\\"\\\\n    title: \\\\\\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.06175\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.06175\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lakshminarayanan2017ensembles\\\\\\\"\\\\n    title: \\\\\\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\\\\\"\\\\n    authors: \\\\\\\"Lakshminarayanan et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"NeurIPS 2017\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1612.01474\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gal2016dropout\\\\\\\"\\\\n    title: \\\\\\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\\\\\"\\\\n    authors: \\\\\\\"Gal & Ghahramani\\\\\\\"\\\\n    year: 2016\\\\n    venue: \\\\\\\"ICML 2016\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1506.02142\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chi2023diffusion_policy\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"RSS 2023 / IJRR 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2303.04137\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Well-known paper, needs URL reachability confirmation\\\\\\\"\\\\n    relevance: \\\\\\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  # ===== New entries added 2026-05-14 =====\\\\n\\\\n  - bibtex_key: \\\\\\\"fan2025interpretable_mcp\\\\\\\"\\\\n    title: \\\\\\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\\\\\"\\\\n    authors: \\\\\\\"Fan & Sesia\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.15383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.15383\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"klein2025otcp\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction using Optimal Transport\\\\\\\"\\\\n    authors: \\\\\\\"Klein, Bethune, Ndiaye & Cuturi\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2502.03609\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.03609\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"zollo2025vla_calibration\\\\\\\"\\\\n    title: \\\\\\\"Confidence Calibration in Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zollo & Zemel\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17383\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17383\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"tang2026shifting_uncertainty\\\\\\\"\\\\n    title: \\\\\\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\\\\\"\\\\n    authors: \\\\\\\"Tang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2603.18342\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.18342\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lcp2025\\\\\\\"\\\\n    title: \\\\\\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.21955\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.21955\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"claps2025\\\\\\\"\\\\n    title: \\\\\\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.10294\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.10294\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"lucca2024\\\\\\\"\\\\n    title: \\\\\\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\\\\\"\\\\n    authors: \\\\\\\"Marques et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2409.08249\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2409.08249\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"sc_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\\\\\"\\\\n    authors: \\\\\\\"Li et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.21633\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.21633\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_pilot_2025\\\\\\\"\\\\n    title: \\\\\\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.14178\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.14178\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\\\\\"\\\\n    must_cite: true\\\\n    relation: \\\\\\\"competitor\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"acot_vla_2026\\\\\\\"\\\\n    title: \\\\\\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"AgibotTech\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"CVPR 2026, arXiv:2601.11404\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.11404\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"gonzales2026crc_cbf\\\\\\\"\\\\n    title: \\\\\\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\\\\\"\\\\n    authors: \\\\\\\"Gonzales et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"IROS 2025, arXiv:2603.10392\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2603.10392\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"safediffcon2025\\\\\\\"\\\\n    title: \\\\\\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2502.02205\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2502.02205\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"afil2026\\\\\\\"\\\\n    title: \\\\\\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Not specified\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.08434\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.08434\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"valle2025vla_uq_metrics\\\\\\\"\\\\n    title: \\\\\\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\\\\\"\\\\n    authors: \\\\\\\"Valle et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.17049\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.17049\\\\\\\"\\\\n    category: \\\\\\\"uq_vla\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"complementary\\\\\\\"\\\\n\\\\n  - bibtex_key: \\\\\\\"diffusionvla2024\\\\\\\"\\\\n    title: \\\\\\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\\\\\"\\\\n    authors: \\\\\\\"Wen et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"ICML 2025, arXiv:2412.03293\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2412.03293\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\\\\\"\\\\n    must_cite: false\\\\n    relation: \\\\\\\"background\\\\\\\"\\\\n\\\", \\\"total_chars\\\": 24446, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\\n  # ===== New entries added 2026-05-14 =====\\n\\n  - bibtex_key: \\\"fan2025interpretable_mcp\\\"\\n    title: \\\"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\\\"\\n    authors: \\\"Fan & Sesia\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.15383\\\"\\n    url: \\\"https://arxiv.org/abs/2512.15383\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"klein2025otcp\\\"\\n    title: \\\"Multivariate Conformal Prediction using Optimal Transport\\\"\\n    authors: \\\"Klein, Bethune, Ndiaye & Cuturi\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2502.03609\\\"\\n    url: \\\"https://arxiv.org/abs/2502.03609\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"zollo2025vla_calibration\\\"\\n    title: \\\"Confidence Calibration in Vision-Language-Action Models\\\"\\n    authors: \\\"Zollo & Zemel\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17383\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17383\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\\\"\\n    must_cite: true\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"tang2026shifting_uncertainty\\\"\\n    title: \\\"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\\\"\\n    authors: \\\"Tang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2603.18342\\\"\\n    url: \\\"https://arxiv.org/abs/2603.18342\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lcp2025\\\"\\n    title: \\\"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.21955\\\"\\n    url: \\\"https://arxiv.org/abs/2509.21955\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"claps2025\\\"\\n    title: \\\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.10294\\\"\\n    url: \\\"https://arxiv.org/abs/2512.10294\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"lucca2024\\\"\\n    title: \\\"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\\\"\\n    authors: \\\"Marques et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2409.08249\\\"\\n    url: \\\"https://arxiv.org/abs/2409.08249\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"sc_vla_2026\\\"\\n    title: \\\"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\\\"\\n    authors: \\\"Li et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.21633\\\"\\n    url: \\\"https://arxiv.org/abs/2602.21633\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"vla_pilot_2025\\\"\\n    title: \\\"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.14178\\\"\\n    url: \\\"https://arxiv.org/abs/2511.14178\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\\\"\\n    must_cite: true\\n    relation: \\\"competitor\\\"\\n\\n  - bibtex_key: \\\"acot_vla_2026\\\"\\n    title: \\\"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\\\"\\n    authors: \\\"AgibotTech\\\"\\n    year: 2026\\n    venue: \\\"CVPR 2026, arXiv:2601.11404\\\"\\n    url: \\\"https://arxiv.org/abs/2601.11404\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"gonzales2026crc_cbf\\\"\\n    title: \\\"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\\\"\\n    authors: \\\"Gonzales et al.\\\"\\n    year: 2026\\n    venue: \\\"IROS 2025, arXiv:2603.10392\\\"\\n    url: \\\"https://arxiv.org/abs/2603.10392\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"safediffcon2025\\\"\\n    title: \\\"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2025\\n    venue: \\\"ICML 2025, arXiv:2502.02205\\\"\\n    url: \\\"https://arxiv.org/abs/2502.02205\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\\n  - bibtex_key: \\\"afil2026\\\"\\n    title: \\\"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\\\"\\n    authors: \\\"Not specified\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.08434\\\"\\n    url: \\\"https://arxiv.org/abs/2605.08434\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"valle2025vla_uq_metrics\\\"\\n    title: \\\"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\\\"\\n    authors: \\\"Valle et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.17049\\\"\\n    url: \\\"https://arxiv.org/abs/2507.17049\\\"\\n    category: \\\"uq_vla\\\"\\n    verified: true\\n    relevance: \\\"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\\\"\\n    must_cite: false\\n    relation: \\\"complementary\\\"\\n\\n  - bibtex_key: \\\"diffusionvla2024\\\"\\n    title: \\\"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\\\"\\n    authors: \\\"Wen et al.\\\"\\n    year: 2024\\n    venue: \\\"ICML 2025, arXiv:2412.03293\\\"\\n    url: \\\"https://arxiv.org/abs/2412.03293\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\\\"\\n    must_cite: false\\n    relation: \\\"background\\\"\\n\", \"total_chars\": 24446, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Tool call

_source line 11_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YAVAuy1XygTHYTpzr1Wn2j`</summary>

```json
{
  "query": "SC-VLA sparse world imagination residual RL action refinement arXiv 2602.21633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "ca6fcb5d-8307-4620-8b5b-dc0490f6e509",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5KKvRXzRq9TUNTdgiNDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 23591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1929
      },
      "output_tokens": 19,
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Szmxxf8NAhGcwVuRx2dWvN`</summary>

```json
{
  "query": "VLA-Pilot inference-time policy steering evolutionary diffusion optimizer arXiv 2511.14178"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "440ff3a6-5be8-4b83-a4a8-78734fef14dd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5KKvRXzRq9TUNTdgiNDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 23591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1929
      },
      "output_tokens": 19,
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01D91cqa4eiWomm5BC2R7r8m`</summary>

```json
{
  "query": "ACoT-VLA action chain-of-thought CVPR 2026 arXiv 2601.11404"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "83b7d467-afed-4870-a064-f2e6998212e4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5KKvRXzRq9TUNTdgiNDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 23591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1929
      },
      "output_tokens": 19,
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01QEJ691NgYBjPtgn6yJTgWK`</summary>

```json
{
  "query": "ReconVLA conformal prediction VLA action correction arXiv 2604.16677"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "79ab21ea-dd8e-4d1d-8770-abc4249f6621",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S5KKvRXzRq9TUNTdgiNDXU",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 1929,
      "cache_read_input_tokens": 23591,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1929
      },
      "output_tokens": 19,
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

_source line 15 · 2026-05-14T07:15:39.528Z_

<details><summary>↩ Tool result · `toolu_01Szmxxf8NAhGcwVuRx2dWvN`</summary>

```text
Web search results for query: "VLA-Pilot inference-time policy steering evolutionary diffusion optimizer arXiv 2511.14178"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"[2511.14178] Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/abs/2511.14178"},{"title":"VLS: Steering Pretrained Robot Policies via Vision–Language Models","url":"https://arxiv.org/html/2602.03973v1"},{"title":"Paper page - VLS: Steering Pretrained Robot Policies via Vision-Language Models","url":"https://huggingface.co/papers/2602.03973"},{"title":"[2411.16627] Inference-Time Policy Steering through Human Interactions","url":"https://arxiv.org/abs/2411.16627"},{"title":"[2602.03973] VLS: Steering Pretrained Robot Policies via Vision-Language Models","url":"https://arxiv.org/abs/2602.03973"},{"title":"[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/abs/2512.02834"},{"title":"Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://arxiv.org/html/2512.02834v1"},{"title":"(PDF) Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://www.researchgate.net/publication/398269618_Steering_Vision-Language-Action_Models_as_Anti-Exploration_A_Test-Time_Scaling_Approach"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"}]

Based on the search results, here's what I found about arXiv paper 2511.14178:

## VLA-Pilot Overview

VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection. The paper is titled "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion."

The method has been evaluated on both simulation and real-world experiments across distinct robotic embodiments.

The paper was submitted in November 2025 and accepted in March 2026, making it a very recent contribution to the field of Vision-Language-Action (VLA) models in robotics. The approach addresses the challenge of deploying pre-trained VLA models without requiring additional fine-tuning, which represents a significant practical advantage for robotic applications.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "f353f0c9-82a1-4429-b650-c24f17eaba63",
  "tool_use_result": {
    "query": "VLA-Pilot inference-time policy steering evolutionary diffusion optimizer arXiv 2511.14178",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AmEdet965YtF9wStoikj6o",
        "content": [
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178"
          },
          {
            "title": "[2511.14178] Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/abs/2511.14178"
          },
          {
            "title": "VLS: Steering Pretrained Robot Policies via Vision–Language Models",
            "url": "https://arxiv.org/html/2602.03973v1"
          },
          {
            "title": "Paper page - VLS: Steering Pretrained Robot Policies via Vision-Language Models",
            "url": "https://huggingface.co/papers/2602.03973"
          },
          {
            "title": "[2411.16627] Inference-Time Policy Steering through Human Interactions",
            "url": "https://arxiv.org/abs/2411.16627"
          },
          {
            "title": "[2602.03973] VLS: Steering Pretrained Robot Policies via Vision-Language Models",
            "url": "https://arxiv.org/abs/2602.03973"
          },
          {
            "title": "[2512.02834] Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/abs/2512.02834"
          },
          {
            "title": "Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://arxiv.org/html/2512.02834v1"
          },
          {
            "title": "(PDF) Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://www.researchgate.net/publication/398269618_Steering_Vision-Language-Action_Models_as_Anti-Exploration_A_Test-Time_Scaling_Approach"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2509.00328v1"
          }
        ]
      },
      "Based on the search results, here's what I found about arXiv paper 2511.14178:\n\n## VLA-Pilot Overview\n\nVLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection. The paper is titled \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion.\"\n\nThe method has been evaluated on both simulation and real-world experiments across distinct robotic embodiments.\n\nThe paper was submitted in November 2025 and accepted in March 2026, making it a very recent contribution to the field of Vision-Language-Action (VLA) models in robotics. The approach addresses the challenge of deploying pre-trained VLA models without requiring additional fine-tuning, which represents a significant practical advantage for robotic applications."
    ],
    "durationSeconds": 4.6705877970000005
  }
}
```

</details>

---

### Tool result

_source line 16 · 2026-05-14T07:15:40.350Z_

<details><summary>↩ Tool result · `toolu_01YAVAuy1XygTHYTpzr1Wn2j`</summary>

```text
Web search results for query: "SC-VLA sparse world imagination residual RL action refinement arXiv 2602.21633"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"Self-Improving Vision-Language-Action Models with Data Generation via Residual RL","url":"https://arxiv.org/html/2511.00091v1"},{"title":"World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy","url":"https://arxiv.org/html/2602.06508v1"},{"title":"RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models","url":"https://arxiv.org/html/2602.12628v1"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"Interesting Directions in Vision-Language-Action Model Research","url":"https://itcanthink.substack.com/p/interesting-directions-in-vision"},{"title":"WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL","url":"https://arxiv.org/html/2602.13977v1"},{"title":"[2602.19710] Universal Pose Pretraining for Generalizable Vision-Language-Action Policies","url":"https://arxiv.org/abs/2602.19710"}]

I found the research paper you're looking for. Here's what the search results show:

SC-VLA (Self-Correcting VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.

**Key Components:**

1. **Sparse World Imagination (SPI)**: The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

2. **Online Action Refinement (OAR)**: This module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.

3. **Residual RL Integration**: SC-VLA integrates sparse world imagination with residual reinforcement learning for online action refinement, with reward signals that are endogenous, derived purely from the internal consistency of world imagination rather than external dense supervision.

**Performance:**

SC-VLA achieved state-of-the-art performance on robot manipulation tasks, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

The paper was published on February 25, 2026, and the code is available on GitHub at the Kisaragi0/SC-VLA repository.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "73226d67-2f78-47ae-864f-31097367968e",
  "tool_use_result": {
    "query": "SC-VLA sparse world imagination residual RL action refinement arXiv 2602.21633",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VzWt7QKZG54gb68SKmitmK",
        "content": [
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633.pdf"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data Generation via Residual RL",
            "url": "https://arxiv.org/html/2511.00091v1"
          },
          {
            "title": "World-VLA-Loop: Closed-Loop Learning of Video World Model and VLA Policy",
            "url": "https://arxiv.org/html/2602.06508v1"
          },
          {
            "title": "RLinf-Co: Reinforcement Learning–Based Sim–Real Co-Training for VLA Models",
            "url": "https://arxiv.org/html/2602.12628v1"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "Interesting Directions in Vision-Language-Action Model Research",
            "url": "https://itcanthink.substack.com/p/interesting-directions-in-vision"
          },
          {
            "title": "WoVR: World Models as Reliable Simulators for Post-Training VLA Policies with RL",
            "url": "https://arxiv.org/html/2602.13977v1"
          },
          {
            "title": "[2602.19710] Universal Pose Pretraining for Generalizable Vision-Language-Action Policies",
            "url": "https://arxiv.org/abs/2602.19710"
          }
        ]
      },
      "I found the research paper you're looking for. Here's what the search results show:\n\nSC-VLA (Self-Correcting VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.\n\n**Key Components:**\n\n1. **Sparse World Imagination (SPI)**: The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.\n\n2. **Online Action Refinement (OAR)**: This module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.\n\n3. **Residual RL Integration**: SC-VLA integrates sparse world imagination with residual reinforcement learning for online action refinement, with reward signals that are endogenous, derived purely from the internal consistency of world imagination rather than external dense supervision.\n\n**Performance:**\n\nSC-VLA achieved state-of-the-art performance on robot manipulation tasks, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\nThe paper was published on February 25, 2026, and the code is available on GitHub at the Kisaragi0/SC-VLA repository."
    ],
    "durationSeconds": 6.435115114
  }
}
```

</details>

---

### Tool result

_source line 17 · 2026-05-14T07:15:42.888Z_

<details><summary>↩ Tool result · `toolu_01QEJ691NgYBjPtgn6yJTgWK`</summary>

```text
Web search results for query: "ReconVLA conformal prediction VLA action correction arXiv 2604.16677"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"[2604.21232] ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures","url":"https://arxiv.org/abs/2604.21232"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"Conformal Predictions for Human Action Recognition with Vision-Language Models","url":"https://arxiv.org/html/2502.06631"},{"title":"[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification","url":"https://arxiv.org/abs/2107.07511"},{"title":"Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models","url":"https://arxiv.org/html/2604.13991"},{"title":"[2604.16217] Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations","url":"https://arxiv.org/abs/2604.16217"},{"title":"[2604.21595] A Kernel Nonconformity Score for Multivariate Conformal Prediction","url":"https://arxiv.org/abs/2604.21595"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction","url":"https://arxiv.org/html/2509.04018"}]

Based on the search results, I found information about the paper you're looking for:

ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.

The method also extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.

The paper addresses a key limitation of Vision-Language-Action models: VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.

Technically, the approach incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it "doesn't know" or is likely to fail before a catastrophe occurs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "986ba3eb-9bcb-4410-9ac1-8f149c1088b6",
  "tool_use_result": {
    "query": "ReconVLA conformal prediction VLA action correction arXiv 2604.16677",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LTk2s8Nr7gi5T9ZDe7fQb9",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "[2604.21232] ReCAPA: Hierarchical Predictive Correction to Mitigate Cascading Failures",
            "url": "https://arxiv.org/abs/2604.21232"
          },
          {
            "title": "[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/abs/2508.10333"
          },
          {
            "title": "Conformal Predictions for Human Action Recognition with Vision-Language Models",
            "url": "https://arxiv.org/html/2502.06631"
          },
          {
            "title": "[2107.07511] A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification",
            "url": "https://arxiv.org/abs/2107.07511"
          },
          {
            "title": "Adaptive Conformal Prediction for Improving Factuality of Generations by Large Language Models",
            "url": "https://arxiv.org/html/2604.13991"
          },
          {
            "title": "[2604.16217] Beyond Surface Statistics: Robust Conformal Prediction for LLMs via Internal Representations",
            "url": "https://arxiv.org/abs/2604.16217"
          },
          {
            "title": "[2604.21595] A Kernel Nonconformity Score for Multivariate Conformal Prediction",
            "url": "https://arxiv.org/abs/2604.21595"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction",
            "url": "https://arxiv.org/html/2509.04018"
          }
        ]
      },
      "Based on the search results, I found information about the paper you're looking for:\n\nReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success.\n\nThe method also extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.\n\nThe paper addresses a key limitation of Vision-Language-Action models: VLAs provide no calibrated measure of confidence in their action predictions, thus limiting their reliability in real-world settings where uncertainty and failures must be anticipated.\n\nTechnically, the approach incorporates conformal quantile regression (CQR)-based uncertainty quantification into the VLA's action generation process and its state monitoring, allowing the robot to detect when it \"doesn't know\" or is likely to fail before a catastrophe occurs."
    ],
    "durationSeconds": 6.102808758999999
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T07:15:43.143Z_

<details><summary>↩ Tool result · `toolu_01D91cqa4eiWomm5BC2R7r8m`</summary>

```text
Web search results for query: "ACoT-VLA action chain-of-thought CVPR 2026 arXiv 2601.11404"

Links: [{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"Workflow runs · AgibotTech/ACoT-VLA","url":"https://github.com/AgibotTech/ACoT-VLA/actions"},{"title":"Releases · AgibotTech/ACoT-VLA","url":"https://github.com/AgibotTech/ACoT-VLA/releases"},{"title":"Activity · AgibotTech/ACoT-VLA","url":"https://github.com/AgibotTech/ACoT-VLA/activity"},{"title":"CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33233"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"ACoT-VLA/uv.lock at main · AgibotTech/ACoT-VLA","url":"https://github.com/AgibotTech/ACoT-VLA/blob/main/uv.lock"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/pdf/2601.11404"}]

Based on the search results, here's information about ACoT-VLA (arXiv 2601.11404):

## Overview

ACoT-VLA is a novel architecture that materializes the Action Chain-of-Thought (ACoT) paradigm, introducing two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR).

## Core Concept

The Action Chain-of-Thought (ACoT) paradigm formulates the reasoning process as a structured sequence of coarse action intents that guide the final policy. The EAR proposes coarse reference trajectories as explicit action-level reasoning steps, while the IAR extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.

## Performance

Extensive experiments in real-world and simulation environments demonstrate the superiority of the method, achieving 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. ACoT-VLA achieves state-of-the-art performance on multiple simulation benchmarks and exhibits superior robustness under distribution shifts.

## Publication

The paper is presented at CVPR 2026 with arXiv preprint arXiv:2601.11404. The repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "069c0cf3-b467-4a5c-939b-d8c0d71e1db0",
  "tool_use_result": {
    "query": "ACoT-VLA action chain-of-thought CVPR 2026 arXiv 2601.11404",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Pc8aW2zV6gTP3yVSxBz6Qf",
        "content": [
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2601.11404"
          },
          {
            "title": "Workflow runs · AgibotTech/ACoT-VLA",
            "url": "https://github.com/AgibotTech/ACoT-VLA/actions"
          },
          {
            "title": "Releases · AgibotTech/ACoT-VLA",
            "url": "https://github.com/AgibotTech/ACoT-VLA/releases"
          },
          {
            "title": "Activity · AgibotTech/ACoT-VLA",
            "url": "https://github.com/AgibotTech/ACoT-VLA/activity"
          },
          {
            "title": "CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2025/poster/33233"
          },
          {
            "title": "[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"
          },
          {
            "title": "ACoT-VLA/uv.lock at main · AgibotTech/ACoT-VLA",
            "url": "https://github.com/AgibotTech/ACoT-VLA/blob/main/uv.lock"
          },
          {
            "title": "(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/pdf/2601.11404"
          }
        ]
      },
      "Based on the search results, here's information about ACoT-VLA (arXiv 2601.11404):\n\n## Overview\n\nACoT-VLA is a novel architecture that materializes the Action Chain-of-Thought (ACoT) paradigm, introducing two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR).\n\n## Core Concept\n\nThe Action Chain-of-Thought (ACoT) paradigm formulates the reasoning process as a structured sequence of coarse action intents that guide the final policy. The EAR proposes coarse reference trajectories as explicit action-level reasoning steps, while the IAR extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.\n\n## Performance\n\nExtensive experiments in real-world and simulation environments demonstrate the superiority of the method, achieving 98.5%, 84.1%, and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively. ACoT-VLA achieves state-of-the-art performance on multiple simulation benchmarks and exhibits superior robustness under distribution shifts.\n\n## Publication\n\nThe paper is presented at CVPR 2026 with arXiv preprint arXiv:2601.11404. The repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026."
    ],
    "durationSeconds": 6.791543613999998
  }
}
```

</details>

---

### Assistant

_source line 19_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the literature map and initial search results. Let me search for more detailed information about each paper's specific methods, experimental results, and limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "751aa798-b4a7-4b0f-adc5-20addf10681a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBRc2eaaHYmwQdkneFdnRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 25520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 20_

已获取基础信息。搜索更多细节以补充方法和实验数据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "2809ad46-d36f-49f4-b0b5-f10232e21d1d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBRc2eaaHYmwQdkneFdnRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 25520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 21_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M77eK4HLwXuLqKJsXncgVr`</summary>

```json
{
  "query": "SC-VLA self-correcting VLA auxiliary predictive heads sparse future state prediction performance LIBERO results 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "89e7ec8e-c440-4e05-8402-d584989b9820",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBRc2eaaHYmwQdkneFdnRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 25520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 22_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01M25PyDy3v7C596CzMY7Ygp`</summary>

```json
{
  "query": "VLA-Pilot MLLM verifier evolutionary diffusion action optimizer zero-shot deployment performance results benchmark"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "b61396c6-c1da-458d-ad7e-70180d0651d8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBRc2eaaHYmwQdkneFdnRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 25520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 23_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B1jVMGdApYLSC9xTSwBBPP`</summary>

```json
{
  "query": "ACoT-VLA explicit action reasoner implicit action reasoner LIBERO-Plus 84.1 architecture details training"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "319dcec7-6dd6-4ca2-b6c9-378afe48cb57",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBRc2eaaHYmwQdkneFdnRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 25520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Ei1KWASuc8N4nvocoVAMkZ`</summary>

```json
{
  "query": "ReconVLA arXiv 2604.16677 conformal quantile regression failure detection VLA uncertainty calibration results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "ee73d888-fe72-4d16-b8ac-e9ce6f592d4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RBRc2eaaHYmwQdkneFdnRy",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 764,
      "cache_creation_input_tokens": 12673,
      "cache_read_input_tokens": 25520,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 12673
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

_source line 25 · 2026-05-14T07:15:57.528Z_

<details><summary>↩ Tool result · `toolu_01M25PyDy3v7C596CzMY7Ygp`</summary>

```text
Web search results for query: "VLA-Pilot MLLM verifier evolutionary diffusion action optimizer zero-shot deployment performance results benchmark"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play...","url":"https://arxiv.org/abs/2511.14178"},{"title":"RoboAlign: Learning Test-Time Reasoning for Language Action Alignment in Vision Language Action Models","url":"https://arxiv.org/html/2603.21341"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"},{"title":"Case Studies of Foundation Model Integration in Embodied ...","url":"https://aclanthology.org/2025.findings-emnlp.69.pdf"},{"title":"Demonstration-Free Robotic Control via LLM Agents","url":"https://arxiv.org/html/2601.20334"},{"title":"Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect","url":"https://www.sciencedirect.com/science/article/pii/S1566253525011248"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"2025-9-18 ThinkAct: Vision-Language-Action Reasoning via","url":"https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"},{"title":"FAST: Efficient Action Tokenization for Vision-Language-Action Models","url":"https://www.pi.website/download/fast.pdf"}]

I found relevant results about VLA-Pilot. Here's what the search revealed:

## VLA-Pilot Overview

VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection.

## Key Technical Components

The core approach leverages Multimodal Large Language Models (MLLMs) as open-world verifiers to enhance generalization, and employs an Evolutionary Diffusion process as an action optimizer to improve task alignment. Specifically, VLA-Pilot employs an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs.

## Performance Results

Under out-of-distribution (OOD) settings, VLA-Pilot maintains strong performance with an average success rate of 0.50, while baseline methods V-GPS and FOREWARN drop to 0.12 and 0.19 respectively. This generalization capability stems from the use of MLLMs for open-world objective reasoning, in contrast to the dataset-specific verifiers used by baselines.

## Evaluation

VLA-Pilot was evaluated on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios. Experimental results demonstrate that VLA-Pilot substantially boosts the success rates of off-the-shelf pre-trained VLA policies, enabling robust zero-shot generalization to diverse tasks and embodiments.

## Latency Analysis

The overall inference time is 2.41 seconds, with the main bottleneck lying in MLLM-based reward reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "908f4f04-495f-44ba-a271-7eb4fef1f6f7",
  "tool_use_result": {
    "query": "VLA-Pilot MLLM verifier evolutionary diffusion action optimizer zero-shot deployment performance results benchmark",
    "results": [
      {
        "tool_use_id": "srvtoolu_01XimfdyvjEXvvSQy8hGJo8J",
        "content": [
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178"
          },
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play...",
            "url": "https://arxiv.org/abs/2511.14178"
          },
          {
            "title": "RoboAlign: Learning Test-Time Reasoning for Language Action Alignment in Vision Language Action Models",
            "url": "https://arxiv.org/html/2603.21341"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          },
          {
            "title": "Case Studies of Foundation Model Integration in Embodied ...",
            "url": "https://aclanthology.org/2025.findings-emnlp.69.pdf"
          },
          {
            "title": "Demonstration-Free Robotic Control via LLM Agents",
            "url": "https://arxiv.org/html/2601.20334"
          },
          {
            "title": "Multimodal fusion with vision-language-action models for robotic manipulation: A systematic review - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/pii/S1566253525011248"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "2025-9-18 ThinkAct: Vision-Language-Action Reasoning via",
            "url": "https://jasper0314-huang.github.io/assets/pdf/neurips25_thinkact.pdf"
          },
          {
            "title": "FAST: Efficient Action Tokenization for Vision-Language-Action Models",
            "url": "https://www.pi.website/download/fast.pdf"
          }
        ]
      },
      "I found relevant results about VLA-Pilot. Here's what the search revealed:\n\n## VLA-Pilot Overview\n\nVLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection.\n\n## Key Technical Components\n\nThe core approach leverages Multimodal Large Language Models (MLLMs) as open-world verifiers to enhance generalization, and employs an Evolutionary Diffusion process as an action optimizer to improve task alignment. Specifically, VLA-Pilot employs an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs.\n\n## Performance Results\n\nUnder out-of-distribution (OOD) settings, VLA-Pilot maintains strong performance with an average success rate of 0.50, while baseline methods V-GPS and FOREWARN drop to 0.12 and 0.19 respectively. This generalization capability stems from the use of MLLMs for open-world objective reasoning, in contrast to the dataset-specific verifiers used by baselines.\n\n## Evaluation\n\nVLA-Pilot was evaluated on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios. Experimental results demonstrate that VLA-Pilot substantially boosts the success rates of off-the-shelf pre-trained VLA policies, enabling robust zero-shot generalization to diverse tasks and embodiments.\n\n## Latency Analysis\n\nThe overall inference time is 2.41 seconds, with the main bottleneck lying in MLLM-based reward reasoning."
    ],
    "durationSeconds": 7.580711093000005
  }
}
```

</details>

---

### Tool result

_source line 26 · 2026-05-14T07:15:58.566Z_

<details><summary>↩ Tool result · `toolu_01B1jVMGdApYLSC9xTSwBBPP`</summary>

```text
Web search results for query: "ACoT-VLA explicit action reasoner implicit action reasoner LIBERO-Plus 84.1 architecture details training"

Links: [{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v1"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | Takara TLDR","url":"https://tldr.takara.ai/p/2601.11404"},{"title":"Daily Papers - Hugging Face","url":"https://huggingface.co/papers?q=Vision-Language-Action+(VLA)+model"},{"title":"CoT-VLA","url":"https://cot-vla.github.io/"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv","url":"https://www.alphaxiv.org/overview/2601.11404"}]

Based on the search results, here's comprehensive information about ACoT-VLA:

## Architecture Overview

ACoT-VLA is a novel architecture that materializes the Action Chain-of-Thought (ACoT) paradigm through two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR).

### Explicit Action Reasoner (EAR)

The Explicit Action Reasoner (EAR) is instantiated as a lightweight transformer that synthesizes kinematically plausible action references as explicit action-space guidance. It is a Transformer-based module that synthesizes a coarse reference trajectory, providing explicit action-space guidance.

### Implicit Action Reasoner (IAR)

The Implicit Action Reasoner (IAR) infers latent action priors by applying cross-attention modeling between downsampled multimodal representations and learnable queries, providing implicit behavioral priors.

## LIBERO-Plus 84.1% Performance

Combining EAR and IAR achieves a success rate of 84.1%, demonstrating their complementary effects, with EAR providing explicit motion guidance, while IAR supplies dense representation-level priors.

The individual contributions are significant:
- Adding the EAR module yields a clear gain over the baseline, increasing the average success rate from baseline to 83.7%
- Incorporating only the IAR improves the performance to 80.4%, indicating that decoding the latent action-related semantics within the vision–language backbone provides useful behavioral priors

## Training Details

The LIBERO benchmark provides 50 human-teleoperated demonstrations per task for policy training. Models are trained on the LIBERO dataset, with the LLM backbone frozen during training.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "33058dcd-34be-47b4-bced-ee46fcfbf437",
  "tool_use_result": {
    "query": "ACoT-VLA explicit action reasoner implicit action reasoner LIBERO-Plus 84.1 architecture details training",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VoFSq4bykfvR5Cvah1BCZj",
        "content": [
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.11404v1"
          },
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"
          },
          {
            "title": "Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2601.11404"
          },
          {
            "title": "(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"
          },
          {
            "title": "[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2601.11404"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | Takara TLDR",
            "url": "https://tldr.takara.ai/p/2601.11404"
          },
          {
            "title": "Daily Papers - Hugging Face",
            "url": "https://huggingface.co/papers?q=Vision-Language-Action+(VLA)+model"
          },
          {
            "title": "CoT-VLA",
            "url": "https://cot-vla.github.io/"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2601.11404"
          }
        ]
      },
      "Based on the search results, here's comprehensive information about ACoT-VLA:\n\n## Architecture Overview\n\nACoT-VLA is a novel architecture that materializes the Action Chain-of-Thought (ACoT) paradigm through two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR).\n\n### Explicit Action Reasoner (EAR)\n\nThe Explicit Action Reasoner (EAR) is instantiated as a lightweight transformer that synthesizes kinematically plausible action references as explicit action-space guidance. It is a Transformer-based module that synthesizes a coarse reference trajectory, providing explicit action-space guidance.\n\n### Implicit Action Reasoner (IAR)\n\nThe Implicit Action Reasoner (IAR) infers latent action priors by applying cross-attention modeling between downsampled multimodal representations and learnable queries, providing implicit behavioral priors.\n\n## LIBERO-Plus 84.1% Performance\n\nCombining EAR and IAR achieves a success rate of 84.1%, demonstrating their complementary effects, with EAR providing explicit motion guidance, while IAR supplies dense representation-level priors.\n\nThe individual contributions are significant:\n- Adding the EAR module yields a clear gain over the baseline, increasing the average success rate from baseline to 83.7%\n- Incorporating only the IAR improves the performance to 80.4%, indicating that decoding the latent action-related semantics within the vision–language backbone provides useful behavioral priors\n\n## Training Details\n\nThe LIBERO benchmark provides 50 human-teleoperated demonstrations per task for policy training. Models are trained on the LIBERO dataset, with the LLM backbone frozen during training."
    ],
    "durationSeconds": 7.748325448000004
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-14T07:16:01.430Z_

<details><summary>↩ Tool result · `toolu_01Ei1KWASuc8N4nvocoVAMkZ`</summary>

```text
Web search results for query: "ReconVLA arXiv 2604.16677 conformal quantile regression failure detection VLA uncertainty calibration results"

Links: [{"title":"[1905.03222] Conformalized Quantile Regression","url":"https://arxiv.org/abs/1905.03222"},{"title":"Conformalized Quantile Regression Yaniv Romano Department of Statistics","url":"https://arxiv.org/pdf/1905.03222"},{"title":"Behind the Noise: Conformal Quantile Regression Reveals Emergent Representations","url":"https://arxiv.org/html/2505.08176v1"},{"title":"Conformalized High-Density Quantile Regression via Dynamic Prototypes-based Probability Density Estimation","url":"https://arxiv.org/html/2411.01266"},{"title":"Conformal Quantile Regression for Neural Probabilistic Constitutive Modeling","url":"https://arxiv.org/html/2601.17437"},{"title":"[PDF] Conformalized Quantile Regression | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Conformalized-Quantile-Regression-Romano-Patterson/6f9dc6f8519e927d948a13aa7ae0df336f443eb9"},{"title":"Localized Conformal Multi-Quantile Regression","url":"https://arxiv.org/html/2411.19523"},{"title":"improved conformalized quantile regression","url":"https://arxiv.org/pdf/2207.02808"},{"title":"Conformalized Quantile Regression | alphaXiv","url":"https://www.alphaxiv.org/abs/1905.03222"},{"title":"Conformalized quantile regression - Technion - Israel Institute of Technology","url":"https://cris.technion.ac.il/en/publications/conformalized-quantile-regression/"}]

Let me search more specifically for the ReconVLA paper:

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://vla-safe.github.io/"},{"title":"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/html/2603.18342"},{"title":"An Uncertainty-Guided and Failure-Aware Vision-Language-Action Model Control Framework for Robotics","url":"https://mavmatrix.uta.edu/materialscieng_theses/145/"},{"title":"SAFE: Multitask Failure Detection for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.09937v2"},{"title":"[2603.18342] Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/abs/2603.18342"},{"title":"GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub","url":"https://github.com/vla-safe/SAFE"},{"title":"Ask Before You Act: Token-Level Uncertainty for Intervention in Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=NX0euXAv98"},{"title":"FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"},{"title":"Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/pdf/2603.18342"}]

Based on the search results, I found the ReconVLA paper (arXiv 2604.16677). Here's what I found about this work:

## ReconVLA: Uncertainty-Guided and Failure-Aware VLA Framework

ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals for robotic control using Vision-Language-Action models.

### Key Technical Approach

The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. ReconVLA augments the base model with two uncertainty-aware components: (i) a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability, and (ii) an SMD-based detector that monitors latent state distributions to identify OOD or failure-prone conditions.

### Failure Detection Mechanism

The method extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.

### Key Advantages

ReconVLA achieves these capabilities without any retraining or modification of the underlying model. The framework conducts a systematic analysis of uncertainty in the VLA policy's action-generation process and explicitly decomposes the sources of unreliability into two key types: (i) input uncertainty, arising from imperfect or OOD observations that is reflected in the agent's internal state representation, and (ii) noise uncertainty, stemming from stochastic variations in the generative policy.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "ee69c76f-4c12-4d32-8432-eae5cf0832e2",
  "tool_use_result": {
    "query": "ReconVLA arXiv 2604.16677 conformal quantile regression failure detection VLA uncertainty calibration results",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D6wsGbftZXUEuST1LDwBtu",
        "content": [
          {
            "title": "[1905.03222] Conformalized Quantile Regression",
            "url": "https://arxiv.org/abs/1905.03222"
          },
          {
            "title": "Conformalized Quantile Regression Yaniv Romano Department of Statistics",
            "url": "https://arxiv.org/pdf/1905.03222"
          },
          {
            "title": "Behind the Noise: Conformal Quantile Regression Reveals Emergent Representations",
            "url": "https://arxiv.org/html/2505.08176v1"
          },
          {
            "title": "Conformalized High-Density Quantile Regression via Dynamic Prototypes-based Probability Density Estimation",
            "url": "https://arxiv.org/html/2411.01266"
          },
          {
            "title": "Conformal Quantile Regression for Neural Probabilistic Constitutive Modeling",
            "url": "https://arxiv.org/html/2601.17437"
          },
          {
            "title": "[PDF] Conformalized Quantile Regression | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Conformalized-Quantile-Regression-Romano-Patterson/6f9dc6f8519e927d948a13aa7ae0df336f443eb9"
          },
          {
            "title": "Localized Conformal Multi-Quantile Regression",
            "url": "https://arxiv.org/html/2411.19523"
          },
          {
            "title": "improved conformalized quantile regression",
            "url": "https://arxiv.org/pdf/2207.02808"
          },
          {
            "title": "Conformalized Quantile Regression | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/1905.03222"
          },
          {
            "title": "Conformalized quantile regression - Technion - Israel Institute of Technology",
            "url": "https://cris.technion.ac.il/en/publications/conformalized-quantile-regression/"
          }
        ]
      },
      "Let me search more specifically for the ReconVLA paper:",
      {
        "tool_use_id": "srvtoolu_011aLGsGho8Haa92nb5fq711",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://vla-safe.github.io/"
          },
          {
            "title": "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/html/2603.18342"
          },
          {
            "title": "An Uncertainty-Guided and Failure-Aware Vision-Language-Action Model Control Framework for Robotics",
            "url": "https://mavmatrix.uta.edu/materialscieng_theses/145/"
          },
          {
            "title": "SAFE: Multitask Failure Detection for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.09937v2"
          },
          {
            "title": "[2603.18342] Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/abs/2603.18342"
          },
          {
            "title": "GitHub - vla-safe/SAFE: This is the official repository for \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\" (NeurIPS 2025) · GitHub",
            "url": "https://github.com/vla-safe/SAFE"
          },
          {
            "title": "Ask Before You Act: Token-Level Uncertainty for Intervention in Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=NX0euXAv98"
          },
          {
            "title": "FPC-VLA: A Vision-Language-Action Framework with a Supervisor for Failure Prediction and Correction - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S095741742600655X"
          },
          {
            "title": "Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/pdf/2603.18342"
          }
        ]
      },
      "Based on the search results, I found the ReconVLA paper (arXiv 2604.16677). Here's what I found about this work:\n\n## ReconVLA: Uncertainty-Guided and Failure-Aware VLA Framework\n\nReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals for robotic control using Vision-Language-Action models.\n\n### Key Technical Approach\n\nThe approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. ReconVLA augments the base model with two uncertainty-aware components: (i) a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability, and (ii) an SMD-based detector that monitors latent state distributions to identify OOD or failure-prone conditions.\n\n### Failure Detection Mechanism\n\nThe method extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.\n\n### Key Advantages\n\nReconVLA achieves these capabilities without any retraining or modification of the underlying model. The framework conducts a systematic analysis of uncertainty in the VLA policy's action-generation process and explicitly decomposes the sources of unreliability into two key types: (i) input uncertainty, arising from imperfect or OOD observations that is reflected in the agent's internal state representation, and (ii) noise uncertainty, stemming from stochastic variations in the generative policy."
    ],
    "durationSeconds": 9.866744156000001
  }
}
```

</details>

---

### Tool result

_source line 28 · 2026-05-14T07:16:01.575Z_

<details><summary>↩ Tool result · `toolu_01M77eK4HLwXuLqKJsXncgVr`</summary>

```text
Web search results for query: "SC-VLA self-correcting VLA auxiliary predictive heads sparse future state prediction performance LIBERO results 2026"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/pdf/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors","url":"https://arxiv.org/html/2604.21241"},{"title":"A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/html/2405.17418v2"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance","url":"https://arxiv.org/html/2507.22424v1"},{"title":"[2603.08361] $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation","url":"https://arxiv.org/abs/2603.08361"},{"title":"[2405.17418] A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation","url":"https://arxiv.org/abs/2405.17418"}]

Now let me search for LIBERO results and performance metrics:

Links: [{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2026/poster/38735"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/abs/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models","url":"https://arxiv.org/html/2603.28301"},{"title":"PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation","url":"https://www.mdpi.com/2073-8994/18/3/394"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"}]

Now let me search for SC-VLA specific LIBERO performance metrics:

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models","url":"https://arxiv.org/html/2602.01811"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of ...","url":"https://arxiv.org/pdf/2510.03827"},{"title":"LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization","url":"https://arxiv.org/html/2510.03827v1"},{"title":"[2602.19710] Universal Pose Pretraining for Generalizable Vision-Language-Action Policies","url":"https://arxiv.org/abs/2602.19710"},{"title":"VLA Model Leaderboard (beta)","url":"https://allenai.github.io/vla-evaluation-harness/leaderboard/"}]

Based on my web search results, I can provide you with comprehensive information about SC-VLA and its performance:

## SC-VLA Overview

SC-VLA (Self-Correcting VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination. The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.

## Key Technical Components

The online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states. SC-VLA is equipped with Sparse World Imagination (SPI) to forecast task progress and future trajectory trends, and Online Action Refinement (OAR) to dynamically optimize policies via residual adjustments and reshaped rewards.

## Performance Results

Evaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

SC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.

## Publication

The paper was published on arxiv on February 25, 2026, titled "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination" (arXiv:2602.21633). 

Note: While my search results confirm SC-VLA's strong performance metrics on ManiSkill and ARX5 real-world benchmarks, the specific detailed LIBERO benchmark results table was not fully visible in the search results I retrieved.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "273ccfa0-1a6b-49e4-888b-39bed53ec20d",
  "tool_use_result": {
    "query": "SC-VLA self-correcting VLA auxiliary predictive heads sparse future state prediction performance LIBERO results 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014sLcAfcnXvwYDAJLrXs2a2",
        "content": [
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/pdf/2602.21633"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"
          },
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "CorridorVLA: Explicit Spatial Constraints for Generative Action Heads via Sparse Anchors",
            "url": "https://arxiv.org/html/2604.21241"
          },
          {
            "title": "A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation",
            "url": "https://arxiv.org/html/2405.17418v2"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          },
          {
            "title": "Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance",
            "url": "https://arxiv.org/html/2507.22424v1"
          },
          {
            "title": "[2603.08361] $Δ$VLA: Prior-Guided Vision-Language-Action Models via World Knowledge Variation",
            "url": "https://arxiv.org/abs/2603.08361"
          },
          {
            "title": "[2405.17418] A Self-Correcting Vision-Language-Action Model for Fast and Slow System Manipulation",
            "url": "https://arxiv.org/abs/2405.17418"
          }
        ]
      },
      "Now let me search for LIBERO results and performance metrics:",
      {
        "tool_use_id": "srvtoolu_017b57FsmUMFtXhWt8tLxTPZ",
        "content": [
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "CVPR Poster LIBERO-Plus: A Progressive Robustness Benchmark for Visual-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2026/poster/38735"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "[2510.13626] LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-Para: A Diagnostic Benchmark and Metrics for Paraphrase Robustness in VLA Models",
            "url": "https://arxiv.org/html/2603.28301"
          },
          {
            "title": "PI-VLA: Adaptive Symmetry-Aware Decision-Making for Long-Horizon Vision–Language–Action Manipulation",
            "url": "https://www.mdpi.com/2073-8994/18/3/394"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          }
        ]
      },
      "Now let me search for SC-VLA specific LIBERO performance metrics:",
      {
        "tool_use_id": "srvtoolu_013rgghSL13QYkJGcAmEbQNS",
        "content": [
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "From Knowing to Doing Precisely: A General Self-Correction and Termination Framework for VLA models",
            "url": "https://arxiv.org/html/2602.01811"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633.pdf"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of ...",
            "url": "https://arxiv.org/pdf/2510.03827"
          },
          {
            "title": "LIBERO-PRO: Towards Robust and Fair Evaluation of Vision-Language-Action Models Beyond Memorization",
            "url": "https://arxiv.org/html/2510.03827v1"
          },
          {
            "title": "[2602.19710] Universal Pose Pretraining for Generalizable Vision-Language-Action Policies",
            "url": "https://arxiv.org/abs/2602.19710"
          },
          {
            "title": "VLA Model Leaderboard (beta)",
            "url": "https://allenai.github.io/vla-evaluation-harness/leaderboard/"
          }
        ]
      },
      "Based on my web search results, I can provide you with comprehensive information about SC-VLA and its performance:\n\n## SC-VLA Overview\n\nSC-VLA (Self-Correcting VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination. The method integrates auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution.\n\n## Key Technical Components\n\nThe online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states. SC-VLA is equipped with Sparse World Imagination (SPI) to forecast task progress and future trajectory trends, and Online Action Refinement (OAR) to dynamically optimize policies via residual adjustments and reshaped rewards.\n\n## Performance Results\n\nEvaluations on challenging robot manipulation tasks from simulation benchmarks and real-world settings demonstrate that SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\nSC-VLA achieves superior performance on ManiSkill and real-world ARX5 benchmarks, surpassing baselines in both success rate and execution throughput.\n\n## Publication\n\nThe paper was published on arxiv on February 25, 2026, titled \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\" (arXiv:2602.21633). \n\nNote: While my search results confirm SC-VLA's strong performance metrics on ManiSkill and ARX5 real-world benchmarks, the specific detailed LIBERO benchmark results table was not fully visible in the search results I retrieved."
    ],
    "durationSeconds": 12.700945698999996
  }
}
```

</details>

---

### Assistant

_source line 29_

<details><summary>Logged reasoning block</summary>

```text
Good, I now have substantial information. Let me search for a few more specific details - especially ReconVLA's specific performance numbers, VLA-Pilot's architecture details, and SC-VLA's limitations.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "00fa9a56-e200-4a05-b9c4-cf89dcce4d80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL4xQnVHhvvcvHyoW13WzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3345,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 38193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

_source line 30_

搜索更多具体数据和细节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "f8bf9172-ff3e-41e4-9f97-c16db820eca3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL4xQnVHhvvcvHyoW13WzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3345,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 38193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_015G6VVGwpCGL6uMJ53Ld3vR`</summary>

```json
{
  "query": "ReconVLA uncertainty-guided failure-aware VLA framework performance success rate LIBERO benchmark results 2604.16677"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "07a86c5a-79fa-46bd-9c60-536028d8a451",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL4xQnVHhvvcvHyoW13WzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3345,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 38193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

_source line 32_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S1gJDjnLHpFTfjeeAGeTFL`</summary>

```json
{
  "query": "VLA-Pilot embodied evolutionary diffusion EPS-CoT architecture two-stage optimization simulation real-world results"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "3cd4e359-d6a7-465b-90d8-6864963700fc",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL4xQnVHhvvcvHyoW13WzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3345,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 38193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

_source line 33_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KscqPRsUgQ1nNFF9CZ4CBd`</summary>

```json
{
  "query": "SC-VLA sparse predictive imagination ManiSkill success rate training overhead limitations residual policy"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "feb3289a-ecc8-42ea-bca4-9becc746e054",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DL4xQnVHhvvcvHyoW13WzA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3345,
      "cache_creation_input_tokens": 3165,
      "cache_read_input_tokens": 38193,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3165
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

_source line 34 · 2026-05-14T07:16:13.476Z_

<details><summary>↩ Tool result · `toolu_015G6VVGwpCGL6uMJ53Ld3vR`</summary>

```text
Web search results for query: "ReconVLA uncertainty-guided failure-aware VLA framework performance success rate LIBERO benchmark results 2604.16677"

Links: [{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"An Uncertainty-Guided and Failure-Aware Vision-Language-Action Model Control Framework for Robotics","url":"https://mavmatrix.uta.edu/materialscieng_theses/145/"},{"title":"GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub","url":"https://github.com/OpenHelix-Team/ReconVLA"},{"title":"LIBERO Benchmark: Vision-Language-Action in Robotics","url":"https://www.emergentmind.com/topics/libero"},{"title":"GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub","url":"https://github.com/sylvestf/LIBERO-plus"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://sylvestf.github.io/LIBERO-plus/"},{"title":"EfficientVLA: Training-Free Acceleration and Compression ...","url":"https://openreview.net/pdf?id=SELYlDHZk2"},{"title":"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.13626v1"},{"title":"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning","url":"https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"},{"title":"Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models","url":"https://huggingface.co/papers/2510.13626"}]

Based on the search results, I found information about ReconVLA (paper 2604.16677):

ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. 

ReconVLA extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.

Regarding performance results, the research evaluates the method in both simulation and via physical robot experiments across diverse manipulation tasks, with results showing that conformalized action predictions consistently improve failure anticipation, reduce catastrophic errors, and provide a calibrated measure of confidence without retraining or modifying the underlying VLA.

The paper was published on arXiv on April 17, 2026 by researchers at The University of Texas at Arlington. However, the search results do not contain specific numerical performance metrics or success rate percentages on the LIBERO benchmark—the results focus more on the methodological contributions and qualitative improvements rather than specific benchmark numbers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "85ddda30-1603-4095-834b-43e3629b6a48",
  "tool_use_result": {
    "query": "ReconVLA uncertainty-guided failure-aware VLA framework performance success rate LIBERO benchmark results 2604.16677",
    "results": [
      {
        "tool_use_id": "srvtoolu_011ZXdLJ2UnndYj9SaBKXpG5",
        "content": [
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "An Uncertainty-Guided and Failure-Aware Vision-Language-Action Model Control Framework for Robotics",
            "url": "https://mavmatrix.uta.edu/materialscieng_theses/145/"
          },
          {
            "title": "GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub",
            "url": "https://github.com/OpenHelix-Team/ReconVLA"
          },
          {
            "title": "LIBERO Benchmark: Vision-Language-Action in Robotics",
            "url": "https://www.emergentmind.com/topics/libero"
          },
          {
            "title": "GitHub - sylvestf/LIBERO-plus: Official repository of LIBERO-plus, a generalized benchmark for in-depth robustness analysis of vision-language-action models. · GitHub",
            "url": "https://github.com/sylvestf/LIBERO-plus"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://sylvestf.github.io/LIBERO-plus/"
          },
          {
            "title": "EfficientVLA: Training-Free Acceleration and Compression ...",
            "url": "https://openreview.net/pdf?id=SELYlDHZk2"
          },
          {
            "title": "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.13626v1"
          },
          {
            "title": "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning",
            "url": "https://papers.neurips.cc/paper_files/paper/2023/file/8c3c666820ea055a77726d66fc7d447f-Paper-Datasets_and_Benchmarks.pdf"
          },
          {
            "title": "Paper page - LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2510.13626"
          }
        ]
      },
      "Based on the search results, I found information about ReconVLA (paper 2604.16677):\n\nReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals. The approach applies conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success. \n\nReconVLA extends conformal prediction to the robot state space to detect outliers or unsafe states before failures occur, providing a simple yet effective failure detection mechanism that complements the action-level uncertainty.\n\nRegarding performance results, the research evaluates the method in both simulation and via physical robot experiments across diverse manipulation tasks, with results showing that conformalized action predictions consistently improve failure anticipation, reduce catastrophic errors, and provide a calibrated measure of confidence without retraining or modifying the underlying VLA.\n\nThe paper was published on arXiv on April 17, 2026 by researchers at The University of Texas at Arlington. However, the search results do not contain specific numerical performance metrics or success rate percentages on the LIBERO benchmark—the results focus more on the methodological contributions and qualitative improvements rather than specific benchmark numbers."
    ],
    "durationSeconds": 6.857602075000003
  }
}
```

</details>

---

### Tool result

_source line 35 · 2026-05-14T07:16:15.929Z_

<details><summary>↩ Tool result · `toolu_01KscqPRsUgQ1nNFF9CZ4CBd`</summary>

```text
Web search results for query: "SC-VLA sparse predictive imagination ManiSkill success rate training overhead limitations residual policy"

Links: [{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"},{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models","url":"https://arxiv.org/html/2510.06710"},{"title":"Jump-Start Reinforcement Learning with Vision-Language-Action Regularization","url":"https://arxiv.org/html/2604.13733"},{"title":"GitHub - cytoplastm/KC-VLA: Keyframe-Chaining VLA, resolving non-Markovian ambiguity via Sparse Semantic History · GitHub","url":"https://github.com/cytoplastm/KC-VLA"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"},{"title":"VQ-VLA: Improving Vision-Language-Action Models via Scaling","url":"https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"},{"title":"Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking","url":"https://arxiv.org/html/2602.24143v1"},{"title":"[Literature Review] VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers","url":"https://www.themoonlight.io/en/review/vq-vla-improving-vision-language-action-models-via-scaling-vector-quantized-action-tokenizers"}]

I found relevant information about SC-VLA (Self-Correcting VLA) and its performance. Here are the key findings:

## SC-VLA Overview

SC-VLA is a Self-Correcting VLA framework designed to enhance physical grounding through intrinsic self-improvement, equipped with Sparse World Imagination (SPI) to forecast task progress and future trajectory trends, and Online Action Refinement (OAR) to dynamically optimize policies via residual adjustments and reshaped rewards.

## ManiSkill Success Rates

With the introduction of residual reinforcement learning, SC-VLA (SPI, OAR) achieves an average success rate of 86%. On the challenging PegInsertion task, SC-VLA (SPI) improves the success rate by 28% and 10% over pretrained models such as π₀ and GR00T N1.5, respectively.

## Performance Advantages

SC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.

## Key Components

Sparse world imagination is designed by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. The online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.

The search results demonstrate that SC-VLA represents an effective approach to improving Vision-Language-Action models through sparse predictive imagination and residual policy learning on ManiSkill benchmark tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "fb4df116-8d89-4f59-b240-3c4a59bcdc07",
  "tool_use_result": {
    "query": "SC-VLA sparse predictive imagination ManiSkill success rate training overhead limitations residual policy",
    "results": [
      {
        "tool_use_id": "srvtoolu_01UCZ3cQgDPwZz4tJsmo2Koz",
        "content": [
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          },
          {
            "title": "[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/abs/2602.21633"
          },
          {
            "title": "RLinf-VLA: A Unified and Efficient Framework for Reinforcement Learning of Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.06710"
          },
          {
            "title": "Jump-Start Reinforcement Learning with Vision-Language-Action Regularization",
            "url": "https://arxiv.org/html/2604.13733"
          },
          {
            "title": "GitHub - cytoplastm/KC-VLA: Keyframe-Chaining VLA, resolving non-Markovian ambiguity via Sparse Semantic History · GitHub",
            "url": "https://github.com/cytoplastm/KC-VLA"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Wang_VQ-VLA_Improving_Vision-Language-Action_Models_via_Scaling_Vector-Quantized_Action_Tokenizers_ICCV_2025_paper.pdf"
          },
          {
            "title": "VQ-VLA: Improving Vision-Language-Action Models via Scaling",
            "url": "https://xiaoxiao0406.github.io/vqvla.github.io/static/pdfs/VQ-VLA.pdf"
          },
          {
            "title": "Robust Skills, Brittle Grounding: Diagnosing Restricted Generalization in Vision-Language Action Policies via Multi-Object Picking",
            "url": "https://arxiv.org/html/2602.24143v1"
          },
          {
            "title": "[Literature Review] VQ-VLA: Improving Vision-Language-Action Models via Scaling Vector-Quantized Action Tokenizers",
            "url": "https://www.themoonlight.io/en/review/vq-vla-improving-vision-language-action-models-via-scaling-vector-quantized-action-tokenizers"
          }
        ]
      },
      "I found relevant information about SC-VLA (Self-Correcting VLA) and its performance. Here are the key findings:\n\n## SC-VLA Overview\n\nSC-VLA is a Self-Correcting VLA framework designed to enhance physical grounding through intrinsic self-improvement, equipped with Sparse World Imagination (SPI) to forecast task progress and future trajectory trends, and Online Action Refinement (OAR) to dynamically optimize policies via residual adjustments and reshaped rewards.\n\n## ManiSkill Success Rates\n\nWith the introduction of residual reinforcement learning, SC-VLA (SPI, OAR) achieves an average success rate of 86%. On the challenging PegInsertion task, SC-VLA (SPI) improves the success rate by 28% and 10% over pretrained models such as π₀ and GR00T N1.5, respectively.\n\n## Performance Advantages\n\nSC-VLA achieves state-of-the-art performance, yielding the highest task throughput with 16% fewer steps and a 9% higher success rate than the best-performing baselines, alongside a 14% gain in real-world experiments.\n\n## Key Components\n\nSparse world imagination is designed by integrating auxiliary predictive heads to forecast current task progress and future trajectory trends, thereby constraining the policy to encode short-term physical evolution. The online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on the predicted sparse future states.\n\nThe search results demonstrate that SC-VLA represents an effective approach to improving Vision-Language-Action models through sparse predictive imagination and residual policy learning on ManiSkill benchmark tasks."
    ],
    "durationSeconds": 7.580869909000001
  }
}
```

</details>

---

### Tool result

_source line 36 · 2026-05-14T07:16:18.139Z_

<details><summary>↩ Tool result · `toolu_01S1gJDjnLHpFTfjeeAGeTFL`</summary>

```text
Web search results for query: "VLA-Pilot embodied evolutionary diffusion EPS-CoT architecture two-stage optimization simulation real-world results"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v1"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play...","url":"https://arxiv.org/abs/2511.14178"},{"title":"VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory","url":"https://arxiv.org/html/2601.08665v1"},{"title":"Robotic computing system and embodied AI evolution: an algorithm-hardware co-design perspective","url":"https://www.jos.ac.cn/en/article/doi/10.1088/1674-4926/25020034?viewType=HTML"},{"title":"A Survey on Efficient Vision-Language-Action Models","url":"https://arxiv.org/html/2510.24795v1"},{"title":"Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process | OpenReview","url":"https://openreview.net/forum?id=UvQOcw2oCD"},{"title":"Igniting VLMs toward the Embodied Space","url":"https://arxiv.org/html/2509.11766v1"},{"title":"Unified Diffusion VLA Overview","url":"https://www.emergentmind.com/topics/unified-diffusion-vla"},{"title":"GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub","url":"https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"}]

Based on the search results, I found comprehensive information about VLA-Pilot with its embodied evolutionary diffusion and EPS-CoT architecture. Here's what I discovered:

## VLA-Pilot Overview

VLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection.

## Architecture Components

The system employs a two-stage optimization approach with several key components:

1. **EPS-CoT (Embodied Policy Steering Chain-of-Thought)**: VLA-Pilot first employs an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs. EPS-CoT incorporates embodied augmentation, which enhances the reasoning by integrating spatial keypoints of robot end-effector position and object location extracted via vision foundation models, and infers the task-aligned steering objective and generates the corresponding scoring reward code.

2. **Evolutionary Diffusion**: VLA-Pilot introduces a novel Evolutionary Diffusion algorithm to optimize action proposals sampled from the pre-trained VLA policies.

3. **Iterative Steering Refinement**: VLA-Pilot steers a pre-trained VLA policy at inference-time via three key steps: 1) Steering Objective Reasoning employs EPS-CoT module to reason a task-aligned steering objective reward from the given task context; 2) Action Proposal Optimization leverages Evolutionary Diffusion to score and optimize action proposals from the pre-trained VLA based on the reasoned objective reward, and executes the highest-scoring proposal; 3) Iterative Steering Refinement integrates post-execution reflection into the EPS-CoT reasoning loop.

## Real-World Results

Compared to the pre-trained DiVLA baseline, VLA-Pilot achieves notable performance gains across all tasks: +0.23 in Mug Handling, +0.21 in Bag Handling, +0.22 in Basket Flipping, and +0.31 in Table Bussing. VLA-Pilot was deployed on the Franka Panda robot in a zero-shot setting.

## Ablation Study Results

Removing EPS-CoT results in an 8% MSR drop, Replacing Evolutionary Diffusion with selection-only reduces MSR by 11%, and Removing Iterative Steering Refinement causes 5% MSR drop.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "0780069f-a068-4760-bec8-99c0809c1d6c",
  "tool_use_result": {
    "query": "VLA-Pilot embodied evolutionary diffusion EPS-CoT architecture two-stage optimization simulation real-world results",
    "results": [
      {
        "tool_use_id": "srvtoolu_014c712KpVMeJGSy5Ztxkbhv",
        "content": [
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v1"
          },
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play...",
            "url": "https://arxiv.org/abs/2511.14178"
          },
          {
            "title": "VLingNav: Embodied Navigation with Adaptive Reasoning and Visual-Assisted Linguistic Memory",
            "url": "https://arxiv.org/html/2601.08665v1"
          },
          {
            "title": "Robotic computing system and embodied AI evolution: an algorithm-hardware co-design perspective",
            "url": "https://www.jos.ac.cn/en/article/doi/10.1088/1674-4926/25020034?viewType=HTML"
          },
          {
            "title": "A Survey on Efficient Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2510.24795v1"
          },
          {
            "title": "Unified Diffusion VLA: Vision-Language-Action Model via Joint Discrete Denosing Diffusion Process | OpenReview",
            "url": "https://openreview.net/forum?id=UvQOcw2oCD"
          },
          {
            "title": "Igniting VLMs toward the Embodied Space",
            "url": "https://arxiv.org/html/2509.11766v1"
          },
          {
            "title": "Unified Diffusion VLA Overview",
            "url": "https://www.emergentmind.com/topics/unified-diffusion-vla"
          },
          {
            "title": "GitHub - jonyzhang2023/awesome-embodied-vla-va-vln: A curated list of state-of-the-art research in embodied AI, focusing on vision-language-action (VLA) models, vision-language navigation (VLN), and related multimodal learning approaches. · GitHub",
            "url": "https://github.com/jonyzhang2023/awesome-embodied-vla-va-vln"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about VLA-Pilot with its embodied evolutionary diffusion and EPS-CoT architecture. Here's what I discovered:\n\n## VLA-Pilot Overview\n\nVLA-Pilot is a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection.\n\n## Architecture Components\n\nThe system employs a two-stage optimization approach with several key components:\n\n1. **EPS-CoT (Embodied Policy Steering Chain-of-Thought)**: VLA-Pilot first employs an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs. EPS-CoT incorporates embodied augmentation, which enhances the reasoning by integrating spatial keypoints of robot end-effector position and object location extracted via vision foundation models, and infers the task-aligned steering objective and generates the corresponding scoring reward code.\n\n2. **Evolutionary Diffusion**: VLA-Pilot introduces a novel Evolutionary Diffusion algorithm to optimize action proposals sampled from the pre-trained VLA policies.\n\n3. **Iterative Steering Refinement**: VLA-Pilot steers a pre-trained VLA policy at inference-time via three key steps: 1) Steering Objective Reasoning employs EPS-CoT module to reason a task-aligned steering objective reward from the given task context; 2) Action Proposal Optimization leverages Evolutionary Diffusion to score and optimize action proposals from the pre-trained VLA based on the reasoned objective reward, and executes the highest-scoring proposal; 3) Iterative Steering Refinement integrates post-execution reflection into the EPS-CoT reasoning loop.\n\n## Real-World Results\n\nCompared to the pre-trained DiVLA baseline, VLA-Pilot achieves notable performance gains across all tasks: +0.23 in Mug Handling, +0.21 in Bag Handling, +0.22 in Basket Flipping, and +0.31 in Table Bussing. VLA-Pilot was deployed on the Franka Panda robot in a zero-shot setting.\n\n## Ablation Study Results\n\nRemoving EPS-CoT results in an 8% MSR drop, Replacing Evolutionary Diffusion with selection-only reduces MSR by 11%, and Removing Iterative Steering Refinement causes 5% MSR drop."
    ],
    "durationSeconds": 10.581197111999995
  }
}
```

</details>

---

### Assistant

_source line 37_

<details><summary>Logged reasoning block</summary>

```text
I now have sufficient information to write a comprehensive competitor analysis. Let me compile all the data and write the competitor_analysis.md file.

Key findings summary:

**SC-VLA:**
- Core: Sparse World Imagination (SPI) + Online Action Refinement (OAR) via residual RL
- SPI: Auxiliary predictive heads for task progress + future trajectory trends
- OAR: Progress-dependent dense rewards + residual adjustments
- Results: 86% avg on ManiSkill, 9% higher success rate, 16% fewer steps, 14% real-world gain


- Requires RL training with residual policy and additional predictive heads, lacks statistical guarantees, evaluated on ManiSkill and ARX5 real-world benchmarks

**VLA-Pilot:**
- Core: MLLM verifier using spatial keypoints and open-world reasoning for scoring, paired with an evolutionary diffusion optimizer that samples and refines action proposals
- Zero-shot capability without fine-tuning needed
- Results: +0.21-0.31 improvement over DiVLA baseline, achieving 0.50 average performance on out-of-distribution tasks
- Inference bottleneck at 2.41 seconds due to MLLM, tested on 6 real-world Franka Panda tasks, no statistical guarantees

**ACoT-VLA:**
- Core: Action Chain-of-Thought combining a lightweight transformer for coarse trajectory generation with cross-attention mechanisms that extract latent action priors from multimodal representations
- Results: 98.5% on LIBERO, 84.1% on LIBERO-Plus, 47.4% on VLABench
- Requires task-specific training with 50 demonstrations per task while keeping the LLM backbone frozen, published at CVPR 2026

**ReconVLA:**
- Core: C

ReconVLA uses a QR-based uncertainty estimator paired with a state anomaly detector, applying post-hoc conformal prediction to action tokens without requiring retraining, and detects failures through state-space conformal prediction while decomposing input and noise uncertainty into a single scalar value rather than per-degree-of-freedom estimates.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "2538a64d-dcfb-4ca5-99ed-d73acfedde8b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DfxhLu18nQfKSR14zg87o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 5658,
      "cache_read_input_tokens": 41358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5658
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

_source line 38_

信息充足，开始撰写竞品分析文档。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "c1ba1464-a988-4813-9f5a-209f97f5de31",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DfxhLu18nQfKSR14zg87o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 5658,
      "cache_read_input_tokens": 41358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5658
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

_source line 39_

<details open><summary>🔧 Tool call — Write · `toolu_017rtbxd5uyzaX3DnyAr3TJ7`</summary>

````json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitor_analysis.md",
  "content": "# ACR-VLA Competitor Analysis\n\n> 生成日期: 2026-05-14\n\n## 方法对比表\n\n| 维度 | ACR-VLA (Ours) | SC-VLA | VLA-Pilot | ACoT-VLA | ReconVLA |\n|------|---------------|--------|-----------|----------|----------|\n| **核心机制** | Per-DOF conformal statistics + learned CRM correction | Sparse world imagination + residual RL refinement | MLLM verifier + evolutionary diffusion optimizer | Action chain-of-thought (EAR+IAR) | CQR uncertainty + SMD failure detection |\n| **方法类别** | Inference-time statistical correction | Inference-time RL refinement | Inference-time MLLM-guided steering | Training-time reasoning augmentation | Inference-time uncertainty gating |\n| **是否需要额外训练** | CRM 需要训练（~轻量 MLP）；VLA backbone 冻结 | 需要训练 residual policy + auxiliary heads | 不需要（zero-shot plug-and-play） | 需要训练 EAR+IAR 模块 | 不需要（post-hoc calibration） |\n| **不确定性量化** | Per-DOF (40D) conformal intervals via CGS | 无显式 UQ；用 task progress prediction 间接评估 | 无显式 UQ；MLLM 打分替代 | 无 UQ；通过 CoT reasoning 隐式提升可靠性 | Scalar CQR-based confidence + state-space anomaly |\n| **统计保证** | ✅ Marginal coverage guarantee via CP; online ACI+COC 维持 | ❌ 无 | ❌ 无 | ❌ 无 | ✅ Marginal coverage via CQR（scalar level） |\n| **Per-DOF 粒度** | ✅ 40D 维度独立 intervals + selective correction | ❌ 全局 residual adjustment | ❌ 全局 action scoring | ❌ 全局 CoT reasoning | ❌ Scalar aggregation（丢失维度信息） |\n| **在线适应** | ✅ ACI+COC 在线调阈值 | ✅ Online RL refinement（需交互） | ✅ Iterative steering refinement | ❌ 静态模型 | ❌ Static calibration set |\n| **推理开销** | K 次 flow-matching 采样 + CGS + CRM（~中等） | Residual policy forward + world model prediction（~低-中） | MLLM reasoning + evolutionary search（~高，2.41s/step） | EAR+IAR forward（~低） | 多次采样 + CQR quantile computation（~中等） |\n| **主要 benchmark** | LIBERO / LIBERO-Plus | ManiSkill / ARX5 real-world | 6 real-world tasks (Franka Panda) | LIBERO / LIBERO-Plus / VLABench | LIBERO (待确认具体数据) |\n| **代表性结果** | TBD (实验中) | ManiSkill avg 86%; +9% SR, -16% steps | OOD avg 0.50 vs baseline 0.12-0.19 | LIBERO 98.5%, LIBERO-Plus 84.1% | 改善 failure anticipation（具体 SR 未公开） |\n\n## 逐竞品深度分析\n\n### SC-VLA (arXiv:2602.21633)\n\n**方法概述**：SC-VLA 通过 Sparse World Imagination (SPI) 和 Online Action Refinement (OAR) 实现自我纠正。SPI 在 VLA backbone 上附加辅助预测头，预测当前任务进度和未来轨迹趋势（sparse future states），从而迫使 policy 编码短期物理演化信息。OAR 利用这些预测构建 progress-dependent dense reward，通过 residual RL 在线调整动作。\n\n**关键设计决策**：\n- **Endogenous rewards**：奖励信号完全来自 world imagination 的内部一致性，不依赖外部 dense supervision\n- **Sparse prediction**：只预测关键未来状态而非完整 world model，降低计算开销\n- **Residual policy**：保留原始 VLA 输出，仅学习 residual correction\n\n**实验结果**：\n- ManiSkill 平均成功率 86%，PegInsertion 比 π₀/GR00T N1.5 高 28%/10%\n- 任务吞吐量最高（-16% steps），成功率 +9%\n- 真实世界 ARX5 实验 +14%\n\n**局限性**：\n1. **需要 RL 训练**：residual policy 和 auxiliary heads 需在目标任务上训练，限制 zero-shot 泛化\n2. **无统计保证**：correction 基于 RL reward shaping，无法量化不确定性或提供 coverage guarantee\n3. **全局纠正**：residual 作用在整个 action vector 上，无法区分哪些维度需要纠正\n4. **未在 LIBERO-Plus 评估**：主要在 ManiSkill 上验证，与 ACR-VLA 的 benchmark 不完全重叠\n\n**与 ACR-VLA 的本质区别**：SC-VLA 通过 learned world model + RL 做 action refinement，是 \"学出来的纠正\"；ACR-VLA 通过 conformal statistics 做 \"有保证的纠正\"。SC-VLA 无法告诉你 \"哪个维度不确定\"，也无法在不重新训练的情况下适应新任务。\n\n---\n\n### VLA-Pilot (arXiv:2511.14178)\n\n**方法概述**：VLA-Pilot 采用三阶段 inference-time steering：(1) EPS-CoT (Embodied Policy Steering Chain-of-Thought) 利用 MLLM 推理 task-aligned steering objective 并生成 scoring reward code；(2) Evolutionary Diffusion 从 frozen VLA 采样多个 action proposals，基于 MLLM reward 进行进化优化；(3) Iterative Steering Refinement 将执行后反馈整合到下一轮 EPS-CoT 推理中。\n\n**关键设计决策**：\n- **MLLM as open-world verifier**：利用 VLM 的开放世界推理能力进行动作评估，不限于预定义 reward\n- **Evolutionary optimization on diffusion latents**：在 diffusion denoising 过程中进行进化搜索，而非简单 best-of-K selection\n- **Spatial keypoints augmentation**：EPS-CoT 融合 robot end-effector 和 object 的空间关键点信息\n\n**实验结果**：\n- 6 个真实世界任务（Franka Panda），相比 DiVLA baseline 提升 +0.21~+0.31\n- OOD 场景平均成功率 0.50，vs baseline V-GPS 0.12 / FOREWARN 0.19\n- Ablation：去掉 EPS-CoT → -8% MSR，去掉 Evolutionary Diffusion → -11% MSR\n\n**局限性**：\n1. **推理延迟极高**：2.41s/step，MLLM reasoning 是瓶颈，不适合实时控制\n2. **依赖 MLLM 质量**：steering 效果完全取决于 MLLM 的推理质量，无 fallback\n3. **无统计保证**：MLLM scoring 是启发式的，无法提供 calibrated confidence\n4. **无 simulation benchmark 对比**：主要在真实世界评估，缺乏 LIBERO 等标准 benchmark 数据\n\n**与 ACR-VLA 的本质区别**：VLA-Pilot 用 MLLM 做 \"智能评委\" 来选/优化动作，是 language-guided 的启发式方法；ACR-VLA 用 conformal prediction 做 distribution-free statistical correction。VLA-Pilot 的优势在 zero-shot OOD 泛化（靠 MLLM 的开放世界知识），劣势在延迟和缺乏理论保证。\n\n---\n\n### ACoT-VLA (arXiv:2601.11404, CVPR 2026)\n\n**方法概述**：ACoT-VLA 提出 Action Chain-of-Thought 范式，将动作推理过程分解为两个互补组件：(1) Explicit Action Reasoner (EAR)——轻量 Transformer 生成粗粒度参考轨迹作为显式动作空间引导；(2) Implicit Action Reasoner (IAR)——通过 cross-attention 从 multimodal representations 中提取 latent action priors。两者共同形成 ACoT conditioning，引导下游 action head 的生成。\n\n**关键设计决策**：\n- **双推理器架构**：EAR 提供 kinematically plausible 的运动学引导，IAR 提供 dense semantic priors\n- **Training-time integration**：EAR+IAR 在训练时与 VLA 联合优化（LLM backbone 冻结），属于训练阶段方法\n- **50 demos/task**：仅需少量示教数据\n\n**实验结果**：\n- LIBERO 98.5%，LIBERO-Plus **84.1%**（当前最高之一），VLABench 47.4%\n- Ablation：仅 EAR → 83.7%，仅 IAR → 80.4%，双路径互补效应显著\n- AgibotTech 开源，ICRA 2026 AgiBot World Challenge 官方 baseline\n\n**局限性**：\n1. **Training-time 方法**：需要在目标任务上训练 EAR+IAR，不是 plug-and-play\n2. **无不确定性量化**：CoT reasoning 不输出 confidence，无法识别何时 \"不确定\"\n3. **静态模型**：部署后不在线适应，calibration drift 无法处理\n4. **与 ACR-VLA 互补**：ACoT 提升 VLA 基础能力，ACR-VLA 在其之上提供 safety net\n\n**与 ACR-VLA 的本质区别**：ACoT-VLA 是 training-time 的 \"思考能力增强\"，让 VLA 在生成动作前先做结构化推理。ACR-VLA 是 inference-time 的 \"统计安全网\"，在 VLA 生成动作后检测和纠正异常。两者正交且互补——可以先用 ACoT 增强 VLA backbone，再套 ACR-VLA 做 conformal correction。\n\n---\n\n### ReconVLA (arXiv:2604.16677)\n\n**方法概述**：ReconVLA 将 conformal prediction 应用于 VLA action token 输出，提供两层保护：(1) CQR-based action uncertainty estimator——对 VLA 的多次采样输出计算 conformalized quantile regression intervals，用于量化动作级不确定性；(2) SMD-based state anomaly detector——监控 latent state distributions 检测 OOD/failure-prone 条件。框架将不确定性分解为 input uncertainty（OOD observations）和 noise uncertainty（generative stochasticity）。\n\n**关键设计决策**：\n- **Post-hoc, no retraining**：完全在 frozen VLA 上 post-hoc 应用，与 ACR-VLA 理念一致\n- **Scalar CQR**：使用标准 CQR 产生 scalar-level confidence，非 per-DOF\n- **Static calibration**：使用固定 calibration set，不做在线适应\n- **Dual uncertainty decomposition**：input vs noise uncertainty 有利于 root cause analysis\n\n**局限性**：\n1. **Scalar uncertainty**：CQR 输出聚合为 scalar 置信度，丢失维度级信息——无法告诉你 \"第 3 个关节不确定但其余都好\"\n2. **Static calibration**：calibration set 固定后不更新，distribution shift 下 coverage 可能退化\n3. **Detection-only vs correction**：ReconVLA 的 UQ 主要用于 failure detection 和 action selection，不做 learned correction（从 K candidates 选而非合成新 action）\n4. **实验数据有限**：具体 success rate 数据未充分公开，方法验证深度待加强\n\n**与 ACR-VLA 的本质区别**：ReconVLA 是 ACR-VLA 最直接的竞争者——同样使用 conformal prediction + frozen VLA。关键差异在三个层面：\n\n| 差异维度 | ACR-VLA | ReconVLA |\n|---------|---------|----------|\n| UQ 粒度 | Per-DOF 40D intervals (CGS) | Scalar CQR aggregation |\n| 纠正策略 | Learned CRM 合成新动作 | Sample selection from K candidates |\n| 在线适应 | ACI+COC 在线阈值调整 | Static calibration |\n\nACR-VLA 在每个维度上都比 ReconVLA 更进一步：更细粒度的 UQ → 更精准的纠正 → 更鲁棒的在线部署。\n\n---\n\n## ACR-VLA 独特卖点 (USP)\n\n### 1. Statistical Guarantees from Conformal Prediction\n- 提供 distribution-free marginal coverage guarantee，不依赖模型假设\n- SC-VLA 和 VLA-Pilot 完全无统计保证；ACoT-VLA 无 UQ 能力\n- ReconVLA 有 CP 保证但仅在 scalar level\n\n### 2. Per-DOF Granularity (Dimension-Selective Correction)\n- 40D 维度独立的 conformal intervals 通过 CGS (Conformalized Gaussian Scoring)\n- 唯一能做到 \"第 3 个关节 ±0.02 rad 不确定，第 7 个关节 ±0.15 rad 很不确定\" 的方法\n- 其他所有方法要么无 UQ（SC-VLA/VLA-Pilot/ACoT-VLA），要么 scalar aggregation（ReconVLA）\n- **核心论点**：机器人动作是 structured 的（position/orientation/gripper 有不同语义），scalar UQ 会将关键维度的异常淹没在整体均值中\n\n### 3. Learned Correction (CRM) vs Sample Selection\n- CRM 学习在 conformal interval 约束下合成新动作，而非从 K candidates 中选\n- SC-VLA 用 residual RL 做纠正（但需要环境交互训练）\n- VLA-Pilot 用 evolutionary search 优化（但依赖 MLLM scoring）\n- ReconVLA 仅做 sample selection（信息利用率低——只用了 1/K 的采样信息）\n- **核心论点**：当 K 个样本都不够好时，selection 失效；CRM 可以合成更优动作\n\n### 4. Online Adaptation via ACI+COC\n- Adaptive Conformal Inference + Coverage-Oriented Calibration 实现在线阈值自适应\n- 处理 deployment 中的 distribution shift，coverage guarantee 在线维持\n- SC-VLA 需要在线 RL 交互（costly），VLA-Pilot 需要 MLLM 每步推理（slow）\n- ACoT-VLA 和 ReconVLA 都是 static models，无法在线适应\n- **核心论点**：real-world deployment 必然遇到 distribution shift，static calibration 的 coverage 会退化\n\n### 5. No Additional Training for VLA Backbone\n- VLA backbone 完全冻结，仅需训练轻量 CRM\n- SC-VLA 需训练 residual policy + auxiliary heads；ACoT-VLA 需训练 EAR+IAR\n- VLA-Pilot 和 ReconVLA 同样 training-free（对 backbone），但各有其他局限\n\n---\n\n## Related Work 定位建议\n\n### 推荐的 Related Work 叙事结构\n\n**Paragraph 1: VLA Foundation & Robustness Problem**\n- 引出 VLA 范式 (RT-2, OpenVLA, pi0, SmolVLA) 及其脆弱性问题\n- 引用 LIBERO-Plus 的 robustness evaluation 结果\n\n**Paragraph 2: Training-Time Robustness Methods**\n- ACoT-VLA (action reasoning)、RobustVLA/SRPO (RL post-training)、DiG-Flow (geometric regularization)\n- 定位：这些方法提升 VLA 基础能力，但部署后无法适应新分布\n- 关键句：\"These training-time approaches are orthogonal and complementary to ACR-VLA's inference-time correction.\"\n\n**Paragraph 3: Inference-Time Correction Methods**\n- SC-VLA (world model + residual RL)、VLA-Pilot (MLLM steering)、A2C2 (async chunk correction)\n- 定位：同为 inference-time，但缺乏统计保证和维度粒度\n- 关键句：\"While effective, these methods provide no formal uncertainty quantification or coverage guarantees.\"\n\n**Paragraph 4: Uncertainty Quantification for VLAs**\n- ReconVLA (CQR on action tokens)、SAFE (internal feature CP)、Zollo & Zemel (VLA calibration)\n- 定位：ReconVLA 是最近的竞争者，但 scalar UQ + static calibration + selection-only\n- 关键句：\"ReconVLA applies CQR to VLA action tokens but aggregates to scalar uncertainty, losing the per-DOF granularity critical for structured robot actions.\"\n\n**Paragraph 5: Conformal Prediction in Robotics**\n- Conformalized Teleoperation (RSS'24)、CP-Loop、CLAPS、SafeDiffCon\n- 定位：CP 在 robotics 的成功应用，但尚未有 per-DOF multivariate CP + learned correction for VLAs\n- 关键句：\"ACR-VLA bridges multivariate conformal prediction with VLA action correction, uniquely combining per-DOF statistical guarantees with learned dimension-selective refinement.\"\n\n### 关键差异化表述（供论文使用）\n\n> \"Unlike SC-VLA which requires task-specific residual RL training, VLA-Pilot which introduces 2.4s MLLM latency per step, and ReconVLA which aggregates to scalar uncertainty, ACR-VLA provides **per-DOF conformal intervals** with **online coverage guarantees** and **learned correction** that synthesizes improved actions beyond sample selection — all without modifying the frozen VLA backbone.\"\n\n---\n\n## 竞争格局总结\n\n```\n                    Training-Time ←────────→ Inference-Time\n                         │                        │\n    ACoT-VLA ────────────┤                        │\n    (CoT reasoning,      │                        │\n     LIBERO+ 84.1%)      │                        │\n                         │    SC-VLA ─────────────┤\n                         │    (Residual RL,        │\n                         │     needs RL training)  │\n                         │                        │\n                         │    VLA-Pilot ──────────┤\n                         │    (MLLM steering,      │\n                         │     2.41s latency)      │\n                         │                        │\n                         │    ReconVLA ───────────┤\n                         │    (Scalar CP,          │\n                         │     detection only)     │\n                         │                        │\n                         │    ACR-VLA (Ours) ─────┤\n                         │    (Per-DOF CP +        │\n                         │     learned correction  │\n                         │     + online adaptation)│\n\n    Has Statistical Guarantee: ACR-VLA ✅, ReconVLA ✅(scalar), Others ❌\n    Per-DOF Granularity:       ACR-VLA ✅, Others ❌\n    Online Adaptation:         ACR-VLA ✅, SC-VLA ✅(RL), VLA-Pilot ✅(MLLM), Others ❌\n```\n"
}
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "ea087e3c-ddc0-4a02-a2df-7711a22d54a6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012DfxhLu18nQfKSR14zg87o",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1044,
      "cache_creation_input_tokens": 5658,
      "cache_read_input_tokens": 41358,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5658
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

_source line 40 · 2026-05-14T07:18:33.767Z_

<details><summary>↩ Tool result · `toolu_017rtbxd5uyzaX3DnyAr3TJ7`</summary>

```text
File created successfully at: /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitor_analysis.md
```

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "b294e43b-fff6-4781-8ea3-48c906895b79",
  "tool_use_result": {
    "type": "create",
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitor_analysis.md",
    "content": "# ACR-VLA Competitor Analysis\n\n> 生成日期: 2026-05-14\n\n## 方法对比表\n\n| 维度 | ACR-VLA (Ours) | SC-VLA | VLA-Pilot | ACoT-VLA | ReconVLA |\n|------|---------------|--------|-----------|----------|----------|\n| **核心机制** | Per-DOF conformal statistics + learned CRM correction | Sparse world imagination + residual RL refinement | MLLM verifier + evolutionary diffusion optimizer | Action chain-of-thought (EAR+IAR) | CQR uncertainty + SMD failure detection |\n| **方法类别** | Inference-time statistical correction | Inference-time RL refinement | Inference-time MLLM-guided steering | Training-time reasoning augmentation | Inference-time uncertainty gating |\n| **是否需要额外训练** | CRM 需要训练（~轻量 MLP）；VLA backbone 冻结 | 需要训练 residual policy + auxiliary heads | 不需要（zero-shot plug-and-play） | 需要训练 EAR+IAR 模块 | 不需要（post-hoc calibration） |\n| **不确定性量化** | Per-DOF (40D) conformal intervals via CGS | 无显式 UQ；用 task progress prediction 间接评估 | 无显式 UQ；MLLM 打分替代 | 无 UQ；通过 CoT reasoning 隐式提升可靠性 | Scalar CQR-based confidence + state-space anomaly |\n| **统计保证** | ✅ Marginal coverage guarantee via CP; online ACI+COC 维持 | ❌ 无 | ❌ 无 | ❌ 无 | ✅ Marginal coverage via CQR（scalar level） |\n| **Per-DOF 粒度** | ✅ 40D 维度独立 intervals + selective correction | ❌ 全局 residual adjustment | ❌ 全局 action scoring | ❌ 全局 CoT reasoning | ❌ Scalar aggregation（丢失维度信息） |\n| **在线适应** | ✅ ACI+COC 在线调阈值 | ✅ Online RL refinement（需交互） | ✅ Iterative steering refinement | ❌ 静态模型 | ❌ Static calibration set |\n| **推理开销** | K 次 flow-matching 采样 + CGS + CRM（~中等） | Residual policy forward + world model prediction（~低-中） | MLLM reasoning + evolutionary search（~高，2.41s/step） | EAR+IAR forward（~低） | 多次采样 + CQR quantile computation（~中等） |\n| **主要 benchmark** | LIBERO / LIBERO-Plus | ManiSkill / ARX5 real-world | 6 real-world tasks (Franka Panda) | LIBERO / LIBERO-Plus / VLABench | LIBERO (待确认具体数据) |\n| **代表性结果** | TBD (实验中) | ManiSkill avg 86%; +9% SR, -16% steps | OOD avg 0.50 vs baseline 0.12-0.19 | LIBERO 98.5%, LIBERO-Plus 84.1% | 改善 failure anticipation（具体 SR 未公开） |\n\n## 逐竞品深度分析\n\n### SC-VLA (arXiv:2602.21633)\n\n**方法概述**：SC-VLA 通过 Sparse World Imagination (SPI) 和 Online Action Refinement (OAR) 实现自我纠正。SPI 在 VLA backbone 上附加辅助预测头，预测当前任务进度和未来轨迹趋势（sparse future states），从而迫使 policy 编码短期物理演化信息。OAR 利用这些预测构建 progress-dependent dense reward，通过 residual RL 在线调整动作。\n\n**关键设计决策**：\n- **Endogenous rewards**：奖励信号完全来自 world imagination 的内部一致性，不依赖外部 dense supervision\n- **Sparse prediction**：只预测关键未来状态而非完整 world model，降低计算开销\n- **Residual policy**：保留原始 VLA 输出，仅学习 residual correction\n\n**实验结果**：\n- ManiSkill 平均成功率 86%，PegInsertion 比 π₀/GR00T N1.5 高 28%/10%\n- 任务吞吐量最高（-16% steps），成功率 +9%\n- 真实世界 ARX5 实验 +14%\n\n**局限性**：\n1. **需要 RL 训练**：residual policy 和 auxiliary heads 需在目标任务上训练，限制 zero-shot 泛化\n2. **无统计保证**：correction 基于 RL reward shaping，无法量化不确定性或提供 coverage guarantee\n3. **全局纠正**：residual 作用在整个 action vector 上，无法区分哪些维度需要纠正\n4. **未在 LIBERO-Plus 评估**：主要在 ManiSkill 上验证，与 ACR-VLA 的 benchmark 不完全重叠\n\n**与 ACR-VLA 的本质区别**：SC-VLA 通过 learned world model + RL 做 action refinement，是 \"学出来的纠正\"；ACR-VLA 通过 conformal statistics 做 \"有保证的纠正\"。SC-VLA 无法告诉你 \"哪个维度不确定\"，也无法在不重新训练的情况下适应新任务。\n\n---\n\n### VLA-Pilot (arXiv:2511.14178)\n\n**方法概述**：VLA-Pilot 采用三阶段 inference-time steering：(1) EPS-CoT (Embodied Policy Steering Chain-of-Thought) 利用 MLLM 推理 task-aligned steering objective 并生成 scoring reward code；(2) Evolutionary Diffusion 从 frozen VLA 采样多个 action proposals，基于 MLLM reward 进行进化优化；(3) Iterative Steering Refinement 将执行后反馈整合到下一轮 EPS-CoT 推理中。\n\n**关键设计决策**：\n- **MLLM as open-world verifier**：利用 VLM 的开放世界推理能力进行动作评估，不限于预定义 reward\n- **Evolutionary optimization on diffusion latents**：在 diffusion denoising 过程中进行进化搜索，而非简单 best-of-K selection\n- **Spatial keypoints augmentation**：EPS-CoT 融合 robot end-effector 和 object 的空间关键点信息\n\n**实验结果**：\n- 6 个真实世界任务（Franka Panda），相比 DiVLA baseline 提升 +0.21~+0.31\n- OOD 场景平均成功率 0.50，vs baseline V-GPS 0.12 / FOREWARN 0.19\n- Ablation：去掉 EPS-CoT → -8% MSR，去掉 Evolutionary Diffusion → -11% MSR\n\n**局限性**：\n1. **推理延迟极高**：2.41s/step，MLLM reasoning 是瓶颈，不适合实时控制\n2. **依赖 MLLM 质量**：steering 效果完全取决于 MLLM 的推理质量，无 fallback\n3. **无统计保证**：MLLM scoring 是启发式的，无法提供 calibrated confidence\n4. **无 simulation benchmark 对比**：主要在真实世界评估，缺乏 LIBERO 等标准 benchmark 数据\n\n**与 ACR-VLA 的本质区别**：VLA-Pilot 用 MLLM 做 \"智能评委\" 来选/优化动作，是 language-guided 的启发式方法；ACR-VLA 用 conformal prediction 做 distribution-free statistical correction。VLA-Pilot 的优势在 zero-shot OOD 泛化（靠 MLLM 的开放世界知识），劣势在延迟和缺乏理论保证。\n\n---\n\n### ACoT-VLA (arXiv:2601.11404, CVPR 2026)\n\n**方法概述**：ACoT-VLA 提出 Action Chain-of-Thought 范式，将动作推理过程分解为两个互补组件：(1) Explicit Action Reasoner (EAR)——轻量 Transformer 生成粗粒度参考轨迹作为显式动作空间引导；(2) Implicit Action Reasoner (IAR)——通过 cross-attention 从 multimodal representations 中提取 latent action priors。两者共同形成 ACoT conditioning，引导下游 action head 的生成。\n\n**关键设计决策**：\n- **双推理器架构**：EAR 提供 kinematically plausible 的运动学引导，IAR 提供 dense semantic priors\n- **Training-time integration**：EAR+IAR 在训练时与 VLA 联合优化（LLM backbone 冻结），属于训练阶段方法\n- **50 demos/task**：仅需少量示教数据\n\n**实验结果**：\n- LIBERO 98.5%，LIBERO-Plus **84.1%**（当前最高之一），VLABench 47.4%\n- Ablation：仅 EAR → 83.7%，仅 IAR → 80.4%，双路径互补效应显著\n- AgibotTech 开源，ICRA 2026 AgiBot World Challenge 官方 baseline\n\n**局限性**：\n1. **Training-time 方法**：需要在目标任务上训练 EAR+IAR，不是 plug-and-play\n2. **无不确定性量化**：CoT reasoning 不输出 confidence，无法识别何时 \"不确定\"\n3. **静态模型**：部署后不在线适应，calibration drift 无法处理\n4. **与 ACR-VLA 互补**：ACoT 提升 VLA 基础能力，ACR-VLA 在其之上提供 safety net\n\n**与 ACR-VLA 的本质区别**：ACoT-VLA 是 training-time 的 \"思考能力增强\"，让 VLA 在生成动作前先做结构化推理。ACR-VLA 是 inference-time 的 \"统计安全网\"，在 VLA 生成动作后检测和纠正异常。两者正交且互补——可以先用 ACoT 增强 VLA backbone，再套 ACR-VLA 做 conformal correction。\n\n---\n\n### ReconVLA (arXiv:2604.16677)\n\n**方法概述**：ReconVLA 将 conformal prediction 应用于 VLA action token 输出，提供两层保护：(1) CQR-based action uncertainty estimator——对 VLA 的多次采样输出计算 conformalized quantile regression intervals，用于量化动作级不确定性；(2) SMD-based state anomaly detector——监控 latent state distributions 检测 OOD/failure-prone 条件。框架将不确定性分解为 input uncertainty（OOD observations）和 noise uncertainty（generative stochasticity）。\n\n**关键设计决策**：\n- **Post-hoc, no retraining**：完全在 frozen VLA 上 post-hoc 应用，与 ACR-VLA 理念一致\n- **Scalar CQR**：使用标准 CQR 产生 scalar-level confidence，非 per-DOF\n- **Static calibration**：使用固定 calibration set，不做在线适应\n- **Dual uncertainty decomposition**：input vs noise uncertainty 有利于 root cause analysis\n\n**局限性**：\n1. **Scalar uncertainty**：CQR 输出聚合为 scalar 置信度，丢失维度级信息——无法告诉你 \"第 3 个关节不确定但其余都好\"\n2. **Static calibration**：calibration set 固定后不更新，distribution shift 下 coverage 可能退化\n3. **Detection-only vs correction**：ReconVLA 的 UQ 主要用于 failure detection 和 action selection，不做 learned correction（从 K candidates 选而非合成新 action）\n4. **实验数据有限**：具体 success rate 数据未充分公开，方法验证深度待加强\n\n**与 ACR-VLA 的本质区别**：ReconVLA 是 ACR-VLA 最直接的竞争者——同样使用 conformal prediction + frozen VLA。关键差异在三个层面：\n\n| 差异维度 | ACR-VLA | ReconVLA |\n|---------|---------|----------|\n| UQ 粒度 | Per-DOF 40D intervals (CGS) | Scalar CQR aggregation |\n| 纠正策略 | Learned CRM 合成新动作 | Sample selection from K candidates |\n| 在线适应 | ACI+COC 在线阈值调整 | Static calibration |\n\nACR-VLA 在每个维度上都比 ReconVLA 更进一步：更细粒度的 UQ → 更精准的纠正 → 更鲁棒的在线部署。\n\n---\n\n## ACR-VLA 独特卖点 (USP)\n\n### 1. Statistical Guarantees from Conformal Prediction\n- 提供 distribution-free marginal coverage guarantee，不依赖模型假设\n- SC-VLA 和 VLA-Pilot 完全无统计保证；ACoT-VLA 无 UQ 能力\n- ReconVLA 有 CP 保证但仅在 scalar level\n\n### 2. Per-DOF Granularity (Dimension-Selective Correction)\n- 40D 维度独立的 conformal intervals 通过 CGS (Conformalized Gaussian Scoring)\n- 唯一能做到 \"第 3 个关节 ±0.02 rad 不确定，第 7 个关节 ±0.15 rad 很不确定\" 的方法\n- 其他所有方法要么无 UQ（SC-VLA/VLA-Pilot/ACoT-VLA），要么 scalar aggregation（ReconVLA）\n- **核心论点**：机器人动作是 structured 的（position/orientation/gripper 有不同语义），scalar UQ 会将关键维度的异常淹没在整体均值中\n\n### 3. Learned Correction (CRM) vs Sample Selection\n- CRM 学习在 conformal interval 约束下合成新动作，而非从 K candidates 中选\n- SC-VLA 用 residual RL 做纠正（但需要环境交互训练）\n- VLA-Pilot 用 evolutionary search 优化（但依赖 MLLM scoring）\n- ReconVLA 仅做 sample selection（信息利用率低——只用了 1/K 的采样信息）\n- **核心论点**：当 K 个样本都不够好时，selection 失效；CRM 可以合成更优动作\n\n### 4. Online Adaptation via ACI+COC\n- Adaptive Conformal Inference + Coverage-Oriented Calibration 实现在线阈值自适应\n- 处理 deployment 中的 distribution shift，coverage guarantee 在线维持\n- SC-VLA 需要在线 RL 交互（costly），VLA-Pilot 需要 MLLM 每步推理（slow）\n- ACoT-VLA 和 ReconVLA 都是 static models，无法在线适应\n- **核心论点**：real-world deployment 必然遇到 distribution shift，static calibration 的 coverage 会退化\n\n### 5. No Additional Training for VLA Backbone\n- VLA backbone 完全冻结，仅需训练轻量 CRM\n- SC-VLA 需训练 residual policy + auxiliary heads；ACoT-VLA 需训练 EAR+IAR\n- VLA-Pilot 和 ReconVLA 同样 training-free（对 backbone），但各有其他局限\n\n---\n\n## Related Work 定位建议\n\n### 推荐的 Related Work 叙事结构\n\n**Paragraph 1: VLA Foundation & Robustness Problem**\n- 引出 VLA 范式 (RT-2, OpenVLA, pi0, SmolVLA) 及其脆弱性问题\n- 引用 LIBERO-Plus 的 robustness evaluation 结果\n\n**Paragraph 2: Training-Time Robustness Methods**\n- ACoT-VLA (action reasoning)、RobustVLA/SRPO (RL post-training)、DiG-Flow (geometric regularization)\n- 定位：这些方法提升 VLA 基础能力，但部署后无法适应新分布\n- 关键句：\"These training-time approaches are orthogonal and complementary to ACR-VLA's inference-time correction.\"\n\n**Paragraph 3: Inference-Time Correction Methods**\n- SC-VLA (world model + residual RL)、VLA-Pilot (MLLM steering)、A2C2 (async chunk correction)\n- 定位：同为 inference-time，但缺乏统计保证和维度粒度\n- 关键句：\"While effective, these methods provide no formal uncertainty quantification or coverage guarantees.\"\n\n**Paragraph 4: Uncertainty Quantification for VLAs**\n- ReconVLA (CQR on action tokens)、SAFE (internal feature CP)、Zollo & Zemel (VLA calibration)\n- 定位：ReconVLA 是最近的竞争者，但 scalar UQ + static calibration + selection-only\n- 关键句：\"ReconVLA applies CQR to VLA action tokens but aggregates to scalar uncertainty, losing the per-DOF granularity critical for structured robot actions.\"\n\n**Paragraph 5: Conformal Prediction in Robotics**\n- Conformalized Teleoperation (RSS'24)、CP-Loop、CLAPS、SafeDiffCon\n- 定位：CP 在 robotics 的成功应用，但尚未有 per-DOF multivariate CP + learned correction for VLAs\n- 关键句：\"ACR-VLA bridges multivariate conformal prediction with VLA action correction, uniquely combining per-DOF statistical guarantees with learned dimension-selective refinement.\"\n\n### 关键差异化表述（供论文使用）\n\n> \"Unlike SC-VLA which requires task-specific residual RL training, VLA-Pilot which introduces 2.4s MLLM latency per step, and ReconVLA which aggregates to scalar uncertainty, ACR-VLA provides **per-DOF conformal intervals** with **online coverage guarantees** and **learned correction** that synthesizes improved actions beyond sample selection — all without modifying the frozen VLA backbone.\"\n\n---\n\n## 竞争格局总结\n\n```\n                    Training-Time ←────────→ Inference-Time\n                         │                        │\n    ACoT-VLA ────────────┤                        │\n    (CoT reasoning,      │                        │\n     LIBERO+ 84.1%)      │                        │\n                         │    SC-VLA ─────────────┤\n                         │    (Residual RL,        │\n                         │     needs RL training)  │\n                         │                        │\n                         │    VLA-Pilot ──────────┤\n                         │    (MLLM steering,      │\n                         │     2.41s latency)      │\n                         │                        │\n                         │    ReconVLA ───────────┤\n                         │    (Scalar CP,          │\n                         │     detection only)     │\n                         │                        │\n                         │    ACR-VLA (Ours) ─────┤\n                         │    (Per-DOF CP +        │\n                         │     learned correction  │\n                         │     + online adaptation)│\n\n    Has Statistical Guarantee: ACR-VLA ✅, ReconVLA ✅(scalar), Others ❌\n    Per-DOF Granularity:       ACR-VLA ✅, Others ❌\n    Online Adaptation:         ACR-VLA ✅, SC-VLA ✅(RL), VLA-Pilot ✅(MLLM), Others ❌\n```\n",
    "structuredPatch": [],
    "originalFile": null,
    "userModified": false
  }
}
````

</details>

---

### Tool call

_source line 41_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__register_artifact · `toolu_01AS4zc6DvPXWEv9kjAMaaik`</summary>

```json
{
  "name": "ACR-VLA Competitor Analysis",
  "type": "report",
  "description": "ACR-VLA 三个主要竞品（SC-VLA, VLA-Pilot, ACoT-VLA）及最直接竞争者 ReconVLA 的深度对比分析，含方法对比表、逐竞品分析、USP 提炼和 Related Work 定位建议",
  "project": "acr-vla-conformal-refinement",
  "source_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/competitor_analysis.md",
  "tags": [
    "competitor-analysis",
    "related-work",
    "positioning"
  ]
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "ba39e4ae-c980-46d3-945d-7f4c716fad40",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SEaTsSpYz6H98AWic5TD89",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7410,
      "cache_read_input_tokens": 47016,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7410
      },
      "output_tokens": 54,
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

_source line 42 · 2026-05-14T07:18:39.979Z_

<details><summary>↩ Tool result · `toolu_01AS4zc6DvPXWEv9kjAMaaik`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_621600\", \"name\": \"ACR-VLA Competitor Analysis\", \"type\": \"report\", \"description\": \"ACR-VLA 三个主要竞品（SC-VLA, VLA-Pilot, ACoT-VLA）及最直接竞争者 ReconVLA 的深度对比分析，含方法对比表、逐竞品分析、USP 提炼和 Related Work 定位建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T07:18:39.913515+00:00\", \"tags\": [\"competitor-analysis\", \"related-work\", \"positioning\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "3d73f23a-7e2e-49de-81bf-4fc067652614",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"artifact\\\": {\\\"id\\\": \\\"art_20260514_621600\\\", \\\"name\\\": \\\"ACR-VLA Competitor Analysis\\\", \\\"type\\\": \\\"report\\\", \\\"description\\\": \\\"ACR-VLA 三个主要竞品（SC-VLA, VLA-Pilot, ACoT-VLA）及最直接竞争者 ReconVLA 的深度对比分析，含方法对比表、逐竞品分析、USP 提炼和 Related Work 定位建议\\\", \\\"path\\\": \\\"projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md\\\", \\\"url\\\": null, \\\"project\\\": \\\"acr-vla-conformal-refinement\\\", \\\"exp_id\\\": null, \\\"skill\\\": \\\"\\\", \\\"created_at\\\": \\\"2026-05-14T07:18:39.913515+00:00\\\", \\\"tags\\\": [\\\"competitor-analysis\\\", \\\"related-work\\\", \\\"positioning\\\"]}, \\\"manifest\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\\\"}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"artifact\": {\"id\": \"art_20260514_621600\", \"name\": \"ACR-VLA Competitor Analysis\", \"type\": \"report\", \"description\": \"ACR-VLA 三个主要竞品（SC-VLA, VLA-Pilot, ACoT-VLA）及最直接竞争者 ReconVLA 的深度对比分析，含方法对比表、逐竞品分析、USP 提炼和 Related Work 定位建议\", \"path\": \"projects/acr-vla-conformal-refinement/artifacts/_project/report/competitor_analysis.md\", \"url\": null, \"project\": \"acr-vla-conformal-refinement\", \"exp_id\": null, \"skill\": \"\", \"created_at\": \"2026-05-14T07:18:39.913515+00:00\", \"tags\": [\"competitor-analysis\", \"related-work\", \"positioning\"]}, \"manifest\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/artifacts/manifest.yaml\"}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 43_

`artifacts/competitor_analysis.md` 已完成并注册（`art_20260514_621600`）。

文档包含：
- **方法对比表**：10 个维度横向对比 ACR-VLA vs SC-VLA / VLA-Pilot / ACoT-VLA / ReconVLA
- **逐竞品深度分析**：方法、设计决策、实验结果、局限性、与 ACR-VLA 的本质区别
- **4 个 USP 提炼**：Per-DOF granularity、learned correction、statistical guarantees、online adaptation
- **Related Work 定位建议**：5 段叙事结构 + 可直接用于论文的差异化表述

核心发现：ReconVLA 是最直接竞争者（同用 CP + frozen VLA），但 ACR-VLA 在三个层面超越——Per-DOF vs scalar UQ、learned CRM vs sample selection、ACI+COC online adaptation vs static calibration。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "uuid": "6be2afb2-3cc2-4fc9-a9ee-fd2419000fb5",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJ9tqjmhBLzMjubfKEKsQK",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 641,
      "cache_read_input_tokens": 54426,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 641
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

_source line 44_

`artifacts/competitor_analysis.md` 已完成并注册（`art_20260514_621600`）。

文档包含：
- **方法对比表**：10 个维度横向对比 ACR-VLA vs SC-VLA / VLA-Pilot / ACoT-VLA / ReconVLA
- **逐竞品深度分析**：方法、设计决策、实验结果、局限性、与 ACR-VLA 的本质区别
- **4 个 USP 提炼**：Per-DOF granularity、learned correction、statistical guarantees、online adaptation
- **Related Work 定位建议**：5 段叙事结构 + 可直接用于论文的差异化表述

核心发现：ReconVLA 是最直接竞争者（同用 CP + frozen VLA），但 ACR-VLA 在三个层面超越——Per-DOF vs scalar UQ、learned CRM vs sample selection、ACI+COC online adaptation vs static calibration。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 207185,
  "duration_api_ms": 268975,
  "num_turns": 16,
  "stop_reason": "end_turn",
  "session_id": "8496414d-454b-4d81-ba42-734e5dd836d9",
  "total_cost_usd": 1.0177100000000001,
  "usage": {
    "input_tokens": 5161,
    "cache_creation_input_tokens": 43226,
    "cache_read_input_tokens": 241945,
    "output_tokens": 8086,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 43226,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 271,
        "cache_read_input_tokens": 54426,
        "cache_creation_input_tokens": 641,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 641
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 229655,
      "outputTokens": 5793,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 14,
      "costUSD": 0.3986200000000001,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 5161,
      "outputTokens": 8086,
      "cacheReadInputTokens": 241945,
      "cacheCreationInputTokens": 43226,
      "webSearchRequests": 0,
      "costUSD": 0.61909,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "34fba513-6da3-4a9b-93cb-3228012f286d"
}
```

</details>

---
