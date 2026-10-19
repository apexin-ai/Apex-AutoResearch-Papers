# research paper research

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 88
- **Recorded user turns:** 0
- **Tool calls:** 33
- **Original source:** `logs/workers/worker_research_paper-research_20260514T031618.log`
- **Structured JSON:** [`24fb5673c1b78ec07f2f.json`](../../sessions/24/24fb5673c1b78ec07f2f.json)

## Before a recorded user message

88 recorded events

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
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
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
  "uuid": "e20054c9-d97d-4aff-a97a-eb19a88e7b2d",
  "memory_paths": {
    "auto": "/home/ubuntu/.claude-account-1/projects/-home-ubuntu--agent-ml-research-idea-gen-0509-8-projects-acr-vla-conformal-refinement/memory/"
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
    "resetsAt": 1778744400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "3d5f7001-7a1d-46f3-b087-8811fd505cbf",
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f"
}
```

---

### Assistant

_source line 4_

I'll start by reading the current literature map, then search for recent papers across the specified directions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "f68e68f4-dedc-465d-99b6-c1481893d8ca",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149JDAUCgEXtoZKbjNNnf6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11450,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11450
      },
      "output_tokens": 4,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_017dXoVqCyBw1YcbyUE5g4DA`</summary>

```json
{
  "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
  "max_results": 2
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "1ed5d110-c840-42ec-8e16-2261a56ebbe3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0149JDAUCgEXtoZKbjNNnf6M",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 11450,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11450
      },
      "output_tokens": 4,
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

_source line 6 · 2026-05-14T03:16:28.759Z_

<details><summary>↩ Tool result · `toolu_017dXoVqCyBw1YcbyUE5g4DA`</summary>

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
  "tool_name": "mcp__agent-ml-research__read_project_file"
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
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "5e1f0f1c-4452-47d4-af79-281a5360ab35",
  "tool_use_result": {
    "matches": [
      "WebSearch",
      "mcp__agent-ml-research__read_project_file"
    ],
    "query": "select:WebSearch,mcp__agent-ml-research__read_project_file",
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
Let me read the current literature map first, then launch parallel web searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "2b3fdb7f-43d4-4973-9160-229639d8defa",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aySGouf3UA1SEGed5Ltf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 23291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 959
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_01MXpJHfDfx88wLAJnTFBwFy`</summary>

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
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "b96c8c69-bdf4-487e-91d6-8e7248a762f6",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019aySGouf3UA1SEGed5Ltf8",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 959,
      "cache_read_input_tokens": 23291,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 959
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

_source line 9 · 2026-05-14T03:16:32.776Z_

<details><summary>↩ Tool result · `toolu_01MXpJHfDfx88wLAJnTFBwFy`</summary>

```text
{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\", \"total_chars\": 15535, \"truncated\": false}, \"error\": null, \"metadata\": {}}"}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "4876a599-5132-4d5e-bab0-7615cc7af927",
  "tool_use_result": {
    "content": "{\"result\":\"{\\\"success\\\": true, \\\"data\\\": {\\\"path\\\": \\\"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\\\", \\\"content\\\": \\\"papers:\\\\n  - bibtex_key: \\\\\\\"a2c2_2025\\\\\\\"\\\\n    title: \\\\\\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\\\\\"\\\\n    authors: \\\\\\\"Sendai et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2509.23224\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2509.23224\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"angelopoulos2023gentle\\\\\\\"\\\\n    title: \\\\\\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\\\\\"\\\\n    authors: \\\\\\\"Angelopoulos & Bates\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Foundations and Trends in Machine Learning\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2107.07511\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"barber2023conformal\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction Beyond Exchangeability\\\\\\\"\\\\n    authors: \\\\\\\"Barber et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"Annals of Statistics, 51(2):816-845\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2202.13415\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"black2024pi0\\\\\\\"\\\\n    title: \\\\\\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\\\\\"\\\\n    authors: \\\\\\\"Black et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2410.24164\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2410.24164\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"braun2025cgs\\\\\\\"\\\\n    title: \\\\\\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\\\\\"\\\\n    authors: \\\\\\\"Braun et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2507.20941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2507.20941\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"brohan2023rt2\\\\\\\"\\\\n    title: \\\\\\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Brohan et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"arXiv:2307.15818\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2307.15818\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chen2026reconvla\\\\\\\"\\\\n    title: \\\\\\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\\\\\"\\\\n    authors: \\\\\\\"Chen et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.16677\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.16677\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"digflow2025\\\\\\\"\\\\n    title: \\\\\\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2512.01715\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2512.01715\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"fei2025liberoplus\\\\\\\"\\\\n    title: \\\\\\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.13626\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.13626\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"ghosh2024octo\\\\\\\"\\\\n    title: \\\\\\\"Octo: An Open-Source Generalist Robot Policy\\\\\\\"\\\\n    authors: \\\\\\\"Ghosh et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2405.12213\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2405.12213\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gibbs2021aci\\\\\\\"\\\\n    title: \\\\\\\"Adaptive Conformal Inference Under Distribution Shift\\\\\\\"\\\\n    authors: \\\\\\\"Gibbs & Candès\\\\\\\"\\\\n    year: 2021\\\\n    venue: \\\\\\\"NeurIPS 2021\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2106.00170\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"gu2025safe\\\\\\\"\\\\n    title: \\\\\\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Gu et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"NeurIPS 2025\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.09937\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"kim2024openvla\\\\\\\"\\\\n    title: \\\\\\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"arXiv:2406.09246\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.09246\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"ledoit2004well\\\\\\\"\\\\n    title: \\\\\\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\\\\\"\\\\n    authors: \\\\\\\"Ledoit & Wolf\\\\\\\"\\\\n    year: 2004\\\\n    venue: \\\\\\\"Journal of Multivariate Analysis, 88(2):365-411\\\\\\\"\\\\n    url: \\\\\\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lipman2023flow\\\\\\\"\\\\n    title: \\\\\\\"Flow Matching for Generative Modeling\\\\\\\"\\\\n    authors: \\\\\\\"Lipman et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"ICLR 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2210.02747\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2023libero\\\\\\\"\\\\n    title: \\\\\\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"NeurIPS 2023\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2306.03310\\\\\\\"\\\\n    category: \\\\\\\"other\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"liu2026ttvla\\\\\\\"\\\\n    title: \\\\\\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\\\\\"\\\\n    authors: \\\\\\\"Liu et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.06748\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.06748\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"luan2026snapflow\\\\\\\"\\\\n    title: \\\\\\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\\\\\"\\\\n    authors: \\\\\\\"Luan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2604.05656\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2604.05656\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"robustvla2025\\\\\\\"\\\\n    title: \\\\\\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Zhang et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.01331\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.01331\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"romano2019cqr\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Quantile Regression\\\\\\\"\\\\n    authors: \\\\\\\"Romano et al.\\\\\\\"\\\\n    year: 2019\\\\n    venue: \\\\\\\"NeurIPS 2019\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1905.03222\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shafer2008tutorial\\\\\\\"\\\\n    title: \\\\\\\"A Tutorial on Conformal Prediction\\\\\\\"\\\\n    authors: \\\\\\\"Shafer & Vovk\\\\\\\"\\\\n    year: 2008\\\\n    venue: \\\\\\\"Journal of Machine Learning Research, 9:371-421\\\\\\\"\\\\n    url: \\\\\\\"https://jmlr.org/papers/v9/shafer08a.html\\\\\\\"\\\\n    category: \\\\\\\"cp_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"shukor2025smolvla\\\\\\\"\\\\n    title: \\\\\\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\\\\\"\\\\n    authors: \\\\\\\"Shukor et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2506.01844\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2506.01844\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"srpo2025\\\\\\\"\\\\n    title: \\\\\\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\\\\\"\\\\n    authors: \\\\\\\"Fei et al.\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2511.15605\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2511.15605\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"wang2025cploop\\\\\\\"\\\\n    title: \\\\\\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\\\\\"\\\\n    authors: \\\\\\\"Wang & Ning\\\\\\\"\\\\n    year: 2025\\\\n    venue: \\\\\\\"arXiv:2510.16376\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2510.16376\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"xing2026diu\\\\\\\"\\\\n    title: \\\\\\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\\\\\"\\\\n    authors: \\\\\\\"Xing et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.00941\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.00941\\\\\\\"\\\\n    category: \\\\\\\"uq_flow_matching\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"yuan2026ups\\\\\\\"\\\\n    title: \\\\\\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\\\\\"\\\\n    authors: \\\\\\\"Yuan et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2602.22474\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2602.22474\\\\\\\"\\\\n    category: \\\\\\\"inference_correction\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"zhao2024conformalized\\\\\\\"\\\\n    title: \\\\\\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\\\\\"\\\\n    authors: \\\\\\\"Zhao et al.\\\\\\\"\\\\n    year: 2024\\\\n    venue: \\\\\\\"RSS 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2406.07767\\\\\\\"\\\\n    category: \\\\\\\"cp_robotics\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\\\\\"\\\\n    must_cite: true\\\\n\\\\n  - bibtex_key: \\\\\\\"cosmos_policy_2026\\\\\\\"\\\\n    title: \\\\\\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\\\\\"\\\\n    authors: \\\\\\\"Kim et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2601.16163\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2601.16163\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"vla_gse_2026\\\\\\\"\\\\n    title: \\\\\\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\\\\\"\\\\n    authors: \\\\\\\"Jiang et al.\\\\\\\"\\\\n    year: 2026\\\\n    venue: \\\\\\\"arXiv:2605.06175\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2605.06175\\\\\\\"\\\\n    category: \\\\\\\"vla_robustness_training\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"lakshminarayanan2017ensembles\\\\\\\"\\\\n    title: \\\\\\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\\\\\"\\\\n    authors: \\\\\\\"Lakshminarayanan et al.\\\\\\\"\\\\n    year: 2017\\\\n    venue: \\\\\\\"NeurIPS 2017\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1612.01474\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"gal2016dropout\\\\\\\"\\\\n    title: \\\\\\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\\\\\"\\\\n    authors: \\\\\\\"Gal & Ghahramani\\\\\\\"\\\\n    year: 2016\\\\n    venue: \\\\\\\"ICML 2016\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/1506.02142\\\\\\\"\\\\n    category: \\\\\\\"uq_foundation\\\\\\\"\\\\n    verified: true\\\\n    relevance: \\\\\\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\\\\\"\\\\n    must_cite: false\\\\n\\\\n  - bibtex_key: \\\\\\\"chi2023diffusion_policy\\\\\\\"\\\\n    title: \\\\\\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\\\\\"\\\\n    authors: \\\\\\\"Chi et al.\\\\\\\"\\\\n    year: 2023\\\\n    venue: \\\\\\\"RSS 2023 / IJRR 2024\\\\\\\"\\\\n    url: \\\\\\\"https://arxiv.org/abs/2303.04137\\\\\\\"\\\\n    category: \\\\\\\"vla_foundation\\\\\\\"\\\\n    verified: false\\\\n    verification_note: \\\\\\\"Well-known paper, needs URL reachability confirmation\\\\\\\"\\\\n    relevance: \\\\\\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\\\\\"\\\\n    must_cite: true\\\\n\\\", \\\"total_chars\\\": 15535, \\\"truncated\\\": false}, \\\"error\\\": null, \\\"metadata\\\": {}}\"}",
    "structuredContent": {
      "result": "{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml\", \"content\": \"papers:\\n  - bibtex_key: \\\"a2c2_2025\\\"\\n    title: \\\"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\\\"\\n    authors: \\\"Sendai et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2509.23224\\\"\\n    url: \\\"https://arxiv.org/abs/2509.23224\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"angelopoulos2023gentle\\\"\\n    title: \\\"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\\\"\\n    authors: \\\"Angelopoulos & Bates\\\"\\n    year: 2023\\n    venue: \\\"Foundations and Trends in Machine Learning\\\"\\n    url: \\\"https://arxiv.org/abs/2107.07511\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"barber2023conformal\\\"\\n    title: \\\"Conformal Prediction Beyond Exchangeability\\\"\\n    authors: \\\"Barber et al.\\\"\\n    year: 2023\\n    venue: \\\"Annals of Statistics, 51(2):816-845\\\"\\n    url: \\\"https://arxiv.org/abs/2202.13415\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"black2024pi0\\\"\\n    title: \\\"pi0: A Vision-Language-Action Flow Model for General Robot Control\\\"\\n    authors: \\\"Black et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2410.24164\\\"\\n    url: \\\"https://arxiv.org/abs/2410.24164\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"braun2025cgs\\\"\\n    title: \\\"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\\\"\\n    authors: \\\"Braun et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2507.20941\\\"\\n    url: \\\"https://arxiv.org/abs/2507.20941\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"brohan2023rt2\\\"\\n    title: \\\"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\\\"\\n    authors: \\\"Brohan et al.\\\"\\n    year: 2023\\n    venue: \\\"arXiv:2307.15818\\\"\\n    url: \\\"https://arxiv.org/abs/2307.15818\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chen2026reconvla\\\"\\n    title: \\\"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\\\"\\n    authors: \\\"Chen et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.16677\\\"\\n    url: \\\"https://arxiv.org/abs/2604.16677\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"digflow2025\\\"\\n    title: \\\"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2512.01715\\\"\\n    url: \\\"https://arxiv.org/abs/2512.01715\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"fei2025liberoplus\\\"\\n    title: \\\"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.13626\\\"\\n    url: \\\"https://arxiv.org/abs/2510.13626\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"ghosh2024octo\\\"\\n    title: \\\"Octo: An Open-Source Generalist Robot Policy\\\"\\n    authors: \\\"Ghosh et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2405.12213\\\"\\n    url: \\\"https://arxiv.org/abs/2405.12213\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gibbs2021aci\\\"\\n    title: \\\"Adaptive Conformal Inference Under Distribution Shift\\\"\\n    authors: \\\"Gibbs & Candès\\\"\\n    year: 2021\\n    venue: \\\"NeurIPS 2021\\\"\\n    url: \\\"https://arxiv.org/abs/2106.00170\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"gu2025safe\\\"\\n    title: \\\"SAFE: Multitask Failure Detection for Vision-Language-Action Models\\\"\\n    authors: \\\"Gu et al.\\\"\\n    year: 2025\\n    venue: \\\"NeurIPS 2025\\\"\\n    url: \\\"https://arxiv.org/abs/2506.09937\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"kim2024openvla\\\"\\n    title: \\\"OpenVLA: An Open-Source Vision-Language-Action Model\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2024\\n    venue: \\\"arXiv:2406.09246\\\"\\n    url: \\\"https://arxiv.org/abs/2406.09246\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"ledoit2004well\\\"\\n    title: \\\"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\\\"\\n    authors: \\\"Ledoit & Wolf\\\"\\n    year: 2004\\n    venue: \\\"Journal of Multivariate Analysis, 88(2):365-411\\\"\\n    url: \\\"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lipman2023flow\\\"\\n    title: \\\"Flow Matching for Generative Modeling\\\"\\n    authors: \\\"Lipman et al.\\\"\\n    year: 2023\\n    venue: \\\"ICLR 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2210.02747\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2023libero\\\"\\n    title: \\\"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2023\\n    venue: \\\"NeurIPS 2023\\\"\\n    url: \\\"https://arxiv.org/abs/2306.03310\\\"\\n    category: \\\"other\\\"\\n    verified: true\\n    relevance: \\\"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"liu2026ttvla\\\"\\n    title: \\\"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\\\"\\n    authors: \\\"Liu et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.06748\\\"\\n    url: \\\"https://arxiv.org/abs/2601.06748\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"luan2026snapflow\\\"\\n    title: \\\"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\\\"\\n    authors: \\\"Luan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2604.05656\\\"\\n    url: \\\"https://arxiv.org/abs/2604.05656\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"robustvla2025\\\"\\n    title: \\\"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\\\"\\n    authors: \\\"Zhang et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.01331\\\"\\n    url: \\\"https://arxiv.org/abs/2511.01331\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"romano2019cqr\\\"\\n    title: \\\"Conformalized Quantile Regression\\\"\\n    authors: \\\"Romano et al.\\\"\\n    year: 2019\\n    venue: \\\"NeurIPS 2019\\\"\\n    url: \\\"https://arxiv.org/abs/1905.03222\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shafer2008tutorial\\\"\\n    title: \\\"A Tutorial on Conformal Prediction\\\"\\n    authors: \\\"Shafer & Vovk\\\"\\n    year: 2008\\n    venue: \\\"Journal of Machine Learning Research, 9:371-421\\\"\\n    url: \\\"https://jmlr.org/papers/v9/shafer08a.html\\\"\\n    category: \\\"cp_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"shukor2025smolvla\\\"\\n    title: \\\"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\\\"\\n    authors: \\\"Shukor et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2506.01844\\\"\\n    url: \\\"https://arxiv.org/abs/2506.01844\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"srpo2025\\\"\\n    title: \\\"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\\\"\\n    authors: \\\"Fei et al.\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2511.15605\\\"\\n    url: \\\"https://arxiv.org/abs/2511.15605\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"wang2025cploop\\\"\\n    title: \\\"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\\\"\\n    authors: \\\"Wang & Ning\\\"\\n    year: 2025\\n    venue: \\\"arXiv:2510.16376\\\"\\n    url: \\\"https://arxiv.org/abs/2510.16376\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"xing2026diu\\\"\\n    title: \\\"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\\\"\\n    authors: \\\"Xing et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.00941\\\"\\n    url: \\\"https://arxiv.org/abs/2605.00941\\\"\\n    category: \\\"uq_flow_matching\\\"\\n    verified: true\\n    relevance: \\\"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"yuan2026ups\\\"\\n    title: \\\"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\\\"\\n    authors: \\\"Yuan et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2602.22474\\\"\\n    url: \\\"https://arxiv.org/abs/2602.22474\\\"\\n    category: \\\"inference_correction\\\"\\n    verified: true\\n    relevance: \\\"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"zhao2024conformalized\\\"\\n    title: \\\"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\\\"\\n    authors: \\\"Zhao et al.\\\"\\n    year: 2024\\n    venue: \\\"RSS 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2406.07767\\\"\\n    category: \\\"cp_robotics\\\"\\n    verified: true\\n    relevance: \\\"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\\\"\\n    must_cite: true\\n\\n  - bibtex_key: \\\"cosmos_policy_2026\\\"\\n    title: \\\"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\\\"\\n    authors: \\\"Kim et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2601.16163\\\"\\n    url: \\\"https://arxiv.org/abs/2601.16163\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: true\\n    relevance: \\\"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"vla_gse_2026\\\"\\n    title: \\\"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\\\"\\n    authors: \\\"Jiang et al.\\\"\\n    year: 2026\\n    venue: \\\"arXiv:2605.06175\\\"\\n    url: \\\"https://arxiv.org/abs/2605.06175\\\"\\n    category: \\\"vla_robustness_training\\\"\\n    verified: true\\n    relevance: \\\"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"lakshminarayanan2017ensembles\\\"\\n    title: \\\"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\\\"\\n    authors: \\\"Lakshminarayanan et al.\\\"\\n    year: 2017\\n    venue: \\\"NeurIPS 2017\\\"\\n    url: \\\"https://arxiv.org/abs/1612.01474\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"gal2016dropout\\\"\\n    title: \\\"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\\\"\\n    authors: \\\"Gal & Ghahramani\\\"\\n    year: 2016\\n    venue: \\\"ICML 2016\\\"\\n    url: \\\"https://arxiv.org/abs/1506.02142\\\"\\n    category: \\\"uq_foundation\\\"\\n    verified: true\\n    relevance: \\\"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\\\"\\n    must_cite: false\\n\\n  - bibtex_key: \\\"chi2023diffusion_policy\\\"\\n    title: \\\"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\\\"\\n    authors: \\\"Chi et al.\\\"\\n    year: 2023\\n    venue: \\\"RSS 2023 / IJRR 2024\\\"\\n    url: \\\"https://arxiv.org/abs/2303.04137\\\"\\n    category: \\\"vla_foundation\\\"\\n    verified: false\\n    verification_note: \\\"Well-known paper, needs URL reachability confirmation\\\"\\n    relevance: \\\"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\\\"\\n    must_cite: true\\n\", \"total_chars\": 15535, \"truncated\": false}, \"error\": null, \"metadata\": {}}"
    }
  }
}
```

</details>

---

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Good, I have the current literature map with 31 entries. Now let me launch parallel web searches across the specified directions to find new papers from 2025-2026.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "a78094e8-cf10-40f3-ae72-be01a32ffc6e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 11_

已有 31 篇文献。开始搜索新论文。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "2a2ab15d-a959-4ca9-a79b-0d3a00a1c8b4",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 12_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EWeNekfgchEhZgXpjjckX7`</summary>

```json
{
  "query": "\"conformal prediction\" robot manipulation action 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "4998f3c7-5842-4995-8849-4d0573125e4a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 13_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JH2ZECggnED5AfZgEZzhW6`</summary>

```json
{
  "query": "\"action refinement\" \"vision language action\" VLA 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "5bf4c4b1-d75d-4b67-89ae-8147a153ef80",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 14_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015mi4y1rfvPwLnihY2vfsGm`</summary>

```json
{
  "query": "ReconVLA \"sample consensus\" robot VLA multi-sample inference 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "4741d974-74d1-4cff-9062-ca6d00f9455d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 15_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01GkRfFGSBnTW84C4zhF47DZ`</summary>

```json
{
  "query": "\"per-dimension uncertainty\" robot learning action space 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "7e2d4cec-1e4b-434f-a350-be691166eb18",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 16_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01C4bxWcFwjCDu3tTtRKjnF3`</summary>

```json
{
  "query": "\"multi-sample inference\" diffusion policy VLA action selection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "588e25b8-dd78-4068-8447-5cac44c3f16c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01H7NQNvVpGdbeYs5iA9AWMA",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 6466,
      "cache_read_input_tokens": 24250,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 6466
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

_source line 17 · 2026-05-14T03:16:46.375Z_

<details><summary>↩ Tool result · `toolu_01EWeNekfgchEhZgXpjjckX7`</summary>

```text
Web search results for query: ""conformal prediction" robot manipulation action 2025 2026 arxiv"

Links: [{"title":"Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v4/"},{"title":"Learning Robot Safety from Sparse Human Feedback using Conformal Prediction","url":"https://arxiv.org/html/2501.04823"},{"title":"Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v3"},{"title":"Interaction-aware Conformal Prediction for Crowd Navigation","url":"https://arxiv.org/html/2502.06221"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392v1"},{"title":"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/html/2406.07767v2"},{"title":"[2501.04823] Learning Robot Safety from Sparse Human Feedback using Conformal Prediction","url":"https://arxiv.org/abs/2501.04823"},{"title":"[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions","url":"https://arxiv.org/abs/2406.07767"},{"title":"[2502.06221] Interaction-aware Conformal Prediction for Crowd Navigation","url":"https://arxiv.org/abs/2502.06221"},{"title":"[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/abs/2509.21955"}]

Based on the web search results, here are recent papers on conformal prediction applied to robot manipulation and action selection from arXiv (2025-2026):

## Recent Arxiv Papers

**1. Conformalized Teleoperation (2024)**
This paper addresses the challenge that assistive robotic arms have more degrees-of-freedom than a human teleoperator can control with low-dimensional inputs like a joystick, and determines if learned black-box mappings can confidently infer a user's intended high-dimensional action from low-dimensional inputs. The approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts.

**2. Learning Robot Safety from Sparse Human Feedback (January 2025)**
This work learns about robot safety by showing policy trajectories to a human who flags unsafe behavior, and from this binary feedback, uses the statistical method of conformal prediction to identify a region of states guaranteed to contain a user-specified fraction of future policy errors.

**3. Safe Probabilistic Planning for Human-Robot Interaction (March 2026)**
This paper presents a novel probabilistic safe control framework for human-robot interaction that combines control barrier functions with conformal risk control to provide formal safety guarantees while considering complex human behavior, and uses conformal risk control to quantify and control the prediction errors in safety values.

**4. Learnable Conformal Prediction for Robotic Planning and Perception (September 2025)**
Deep learning models in robotics often output poorly calibrated confidence estimates, and this work addresses this with Learnable Conformal Prediction (LCP), which replaces fixed nonconformity scores with a lightweight neural function that leverages geometric, semantic, and task-specific features to produce context-aware uncertainty sets.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "564d9c4a-24ed-4851-b408-871850a6bce1",
  "tool_use_result": {
    "query": "\"conformal prediction\" robot manipulation action 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01D5QXH6iLRqryKyDvZo1gat",
        "content": [
          {
            "title": "Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368v4/"
          },
          {
            "title": "Learning Robot Safety from Sparse Human Feedback using Conformal Prediction",
            "url": "https://arxiv.org/html/2501.04823"
          },
          {
            "title": "Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368v3"
          },
          {
            "title": "Interaction-aware Conformal Prediction for Crowd Navigation",
            "url": "https://arxiv.org/html/2502.06221"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392v1"
          },
          {
            "title": "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "https://arxiv.org/html/2406.07767v2"
          },
          {
            "title": "[2501.04823] Learning Robot Safety from Sparse Human Feedback using Conformal Prediction",
            "url": "https://arxiv.org/abs/2501.04823"
          },
          {
            "title": "[2406.07767] Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions",
            "url": "https://arxiv.org/abs/2406.07767"
          },
          {
            "title": "[2502.06221] Interaction-aware Conformal Prediction for Crowd Navigation",
            "url": "https://arxiv.org/abs/2502.06221"
          },
          {
            "title": "[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/abs/2509.21955"
          }
        ]
      },
      "Based on the web search results, here are recent papers on conformal prediction applied to robot manipulation and action selection from arXiv (2025-2026):\n\n## Recent Arxiv Papers\n\n**1. Conformalized Teleoperation (2024)**\nThis paper addresses the challenge that assistive robotic arms have more degrees-of-freedom than a human teleoperator can control with low-dimensional inputs like a joystick, and determines if learned black-box mappings can confidently infer a user's intended high-dimensional action from low-dimensional inputs. The approach leverages adaptive conformal prediction which adjusts the intervals over time, reducing the uncertainty bounds when the mapping is performant and increasing the bounds when the mapping consistently mis-predicts.\n\n**2. Learning Robot Safety from Sparse Human Feedback (January 2025)**\nThis work learns about robot safety by showing policy trajectories to a human who flags unsafe behavior, and from this binary feedback, uses the statistical method of conformal prediction to identify a region of states guaranteed to contain a user-specified fraction of future policy errors.\n\n**3. Safe Probabilistic Planning for Human-Robot Interaction (March 2026)**\nThis paper presents a novel probabilistic safe control framework for human-robot interaction that combines control barrier functions with conformal risk control to provide formal safety guarantees while considering complex human behavior, and uses conformal risk control to quantify and control the prediction errors in safety values.\n\n**4. Learnable Conformal Prediction for Robotic Planning and Perception (September 2025)**\nDeep learning models in robotics often output poorly calibrated confidence estimates, and this work addresses this with Learnable Conformal Prediction (LCP), which replaces fixed nonconformity scores with a lightweight neural function that leverages geometric, semantic, and task-specific features to produce context-aware uncertainty sets."
    ],
    "durationSeconds": 7.5300677090000026
  }
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-14T03:16:48.432Z_

<details><summary>↩ Tool result · `toolu_01C4bxWcFwjCDu3tTtRKjnF3`</summary>

```text
Web search results for query: ""multi-sample inference" diffusion policy VLA action selection 2025 2026"

Links: [{"title":"GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub","url":"https://github.com/real-stanford/diffusion_policy"},{"title":"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://diffusion-policy.cs.columbia.edu/"},{"title":"DiffusionVLA: Autoregressive Reasoning and Diffusion Policies for Generalizable Vision-Language-Action Models","url":"https://diffusion-vla.github.io/"},{"title":"[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion","url":"https://arxiv.org/abs/2303.04137"},{"title":"State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss","url":"https://mbreuss.github.io/blog_post_iclr_26_vla.html"},{"title":"Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025","url":"https://journals.sagepub.com/doi/full/10.1177/02783649241273668"},{"title":"Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11","url":"https://dl.acm.org/doi/10.1177/02783649241273668"},{"title":"Frontiers | Diffusion models for robotic manipulation: a survey","url":"https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"IMLE Policy: Fast and Sample Efficient Visuomotor Policy Learning via Implicit Maximum Likelihood Estimation","url":"https://arxiv.org/html/2502.12371v2"}]

Based on the search results, I found relevant information about diffusion policies, VLAs (Vision-Language-Action models), and recent developments in action selection and inference methods:

## Key Findings

**Diffusion Policy and Action Generation:**
Diffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process, and learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps.

**VLA Research Trends at ICLR 2026:**
An analysis of 164 Vision-Language-Action model submissions at ICLR 2026 reveals trends in discrete diffusion VLAs, reasoning models, and current benchmark trends.

**Recent Inference Alternatives:**
Recent work has explored alternatives to standard diffusion inference. Flow matching has been used to generate actions from observations preprocessed by VLMs to solve flexible and dynamic tasks, offering a robust alternative to traditional diffusion mechanisms.

**Sample-Efficient Methods:**
IMLE Policy enables single-step action generation, improving inference speed by 97.3% compared to Diffusion Policy, while outperforming single-step Flow Matching.

**VLA Frameworks:**
DiVLA, a framework combining autoregression models with diffusion models for learning visuomotor policy, was accepted by ICML 2025.

The search results indicate active research into improving inference efficiency and action selection strategies in diffusion-based policies and VLAs, with multiple competing approaches emerging in 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "dccbff9f-d4e9-4cf3-8243-66c168eea4bb",
  "tool_use_result": {
    "query": "\"multi-sample inference\" diffusion policy VLA action selection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_011KtRskctdB8H97MKXqx9BR",
        "content": [
          {
            "title": "GitHub - real-stanford/diffusion_policy: [RSS 2023] Diffusion Policy Visuomotor Policy Learning via Action Diffusion · GitHub",
            "url": "https://github.com/real-stanford/diffusion_policy"
          },
          {
            "title": "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://diffusion-policy.cs.columbia.edu/"
          },
          {
            "title": "DiffusionVLA: Autoregressive Reasoning and Diffusion Policies for Generalizable Vision-Language-Action Models",
            "url": "https://diffusion-vla.github.io/"
          },
          {
            "title": "[2303.04137] Diffusion Policy: Visuomotor Policy Learning via Action Diffusion",
            "url": "https://arxiv.org/abs/2303.04137"
          },
          {
            "title": "State of Vision-Language-Action (VLA) Research at ICLR 2026 – Moritz Reuss",
            "url": "https://mbreuss.github.io/blog_post_iclr_26_vla.html"
          },
          {
            "title": "Diffusion policy: Visuomotor policy learning via action diffusion - Cheng Chi, Zhenjia Xu, Siyuan Feng, Eric Cousineau, Yilun Du, Benjamin Burchfiel, Russ Tedrake, Shuran Song, 2025",
            "url": "https://journals.sagepub.com/doi/full/10.1177/02783649241273668"
          },
          {
            "title": "Diffusion policy: : Visuomotor policy learning via action diffusion: International Journal of Robotics Research: Vol 44, No 10-11",
            "url": "https://dl.acm.org/doi/10.1177/02783649241273668"
          },
          {
            "title": "Frontiers | Diffusion models for robotic manipulation: a survey",
            "url": "https://www.frontiersin.org/journals/robotics-and-ai/articles/10.3389/frobt.2025.1606247/full"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "IMLE Policy: Fast and Sample Efficient Visuomotor Policy Learning via Implicit Maximum Likelihood Estimation",
            "url": "https://arxiv.org/html/2502.12371v2"
          }
        ]
      },
      "Based on the search results, I found relevant information about diffusion policies, VLAs (Vision-Language-Action models), and recent developments in action selection and inference methods:\n\n## Key Findings\n\n**Diffusion Policy and Action Generation:**\nDiffusion Policy represents a robot's visuomotor policy as a conditional denoising diffusion process, and learns the gradient of the action-distribution score function and iteratively optimizes with respect to this gradient field during inference via a series of stochastic Langevin dynamics steps.\n\n**VLA Research Trends at ICLR 2026:**\nAn analysis of 164 Vision-Language-Action model submissions at ICLR 2026 reveals trends in discrete diffusion VLAs, reasoning models, and current benchmark trends.\n\n**Recent Inference Alternatives:**\nRecent work has explored alternatives to standard diffusion inference. Flow matching has been used to generate actions from observations preprocessed by VLMs to solve flexible and dynamic tasks, offering a robust alternative to traditional diffusion mechanisms.\n\n**Sample-Efficient Methods:**\nIMLE Policy enables single-step action generation, improving inference speed by 97.3% compared to Diffusion Policy, while outperforming single-step Flow Matching.\n\n**VLA Frameworks:**\nDiVLA, a framework combining autoregression models with diffusion models for learning visuomotor policy, was accepted by ICML 2025.\n\nThe search results indicate active research into improving inference efficiency and action selection strategies in diffusion-based policies and VLAs, with multiple competing approaches emerging in 2025-2026."
    ],
    "durationSeconds": 6.750583326
  }
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-14T03:16:48.441Z_

<details><summary>↩ Tool result · `toolu_01JH2ZECggnED5AfZgEZzhW6`</summary>

```text
Web search results for query: ""action refinement" "vision language action" VLA 2025 2026"

Links: [{"title":"[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/abs/2505.04769"},{"title":"Frontiers | ActionX: pre-training action experts with reinforcement learning for vision-language action models","url":"https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2026.1806605/full"},{"title":"Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v2"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"Vision-Language-Action (VLA) Guide for 2026","url":"https://hyscaler.com/insights/vision-language-action-vla-guide/"},{"title":"2nd 3D-LLM/VLA Workshop | CVPR 2026","url":"https://3d-llm-vla.github.io/"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Vision-Language-Action Models: Concepts, Progress, Applications and Challenges","url":"https://arxiv.org/html/2505.04769v1"},{"title":"Vision-language-action model - Wikipedia","url":"https://en.wikipedia.org/wiki/Vision-language-action_model"}]

Here are the search results for "action refinement" "vision language action" VLA 2025 2026:

## Overview of VLA Models (2025-2026)

Vision-Language-Action (VLA) models mark a transformative advancement in artificial intelligence, aiming to unify perception, natural language understanding, and embodied action within a single computational framework.

## Action Refinement in VLA Systems

Upon encountering variations (e.g., a tilted bottle or slippery grip), Helix's agentic AI module performs micro-policy refinement in real time, adjusting its grip based on feedback. This demonstrates how modern VLA systems implement real-time action refinement mechanisms.

Additionally, reinforcement learning feedback loops enable continuous improvement. As the robot executes tasks, it receives feedback about success or failure, reward signals, and corrections from human operators. This feedback drives ongoing policy refinement, allowing the system to adapt to new objects, environments, and task variations.

## Recent Advances and Methods

Several notable approaches to action refinement have emerged:

- **Action Chain-of-Thought (ACoT)**: Action Chain-of-Thought (ACoT) is a reasoning paradigm where the deliberative process is formulated as structured action intents, enabling grounded and long-horizon policy learning.

- **ActionX Framework**: ActionX is a pretraining framework that learns Action eXperts using reinforcement learning while leveraging a frozen, pretrained Vision-Language Model (VLM) backbone.

- **Human-Robot Collaboration**: Human–Robot Collaboration research has explored interactive learning loops where humans and VLA models refine each other's performance. Collaborative frameworks integrate limited expert interventions into VLA decision-making, reducing operator workload while enriching model training data.

The field continues to rapidly evolve with significant research activities ongoing through 2026, as evidenced by upcoming conferences and workshops focused on VLA development.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "6444ab88-8dae-4a3f-80d8-143fe7c659b5",
  "tool_use_result": {
    "query": "\"action refinement\" \"vision language action\" VLA 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KAwgd89UwNvn94hEpsXDuH",
        "content": [
          {
            "title": "[2505.04769] Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/abs/2505.04769"
          },
          {
            "title": "Frontiers | ActionX: pre-training action experts with reinforcement learning for vision-language action models",
            "url": "https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2026.1806605/full"
          },
          {
            "title": "Vision-Language-Action (VLA) Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v2"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"
          },
          {
            "title": "Vision-Language-Action (VLA) Guide for 2026",
            "url": "https://hyscaler.com/insights/vision-language-action-vla-guide/"
          },
          {
            "title": "2nd 3D-LLM/VLA Workshop | CVPR 2026",
            "url": "https://3d-llm-vla.github.io/"
          },
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Vision-Language-Action Models: Concepts, Progress, Applications and Challenges",
            "url": "https://arxiv.org/html/2505.04769v1"
          },
          {
            "title": "Vision-language-action model - Wikipedia",
            "url": "https://en.wikipedia.org/wiki/Vision-language-action_model"
          }
        ]
      },
      "Here are the search results for \"action refinement\" \"vision language action\" VLA 2025 2026:\n\n## Overview of VLA Models (2025-2026)\n\nVision-Language-Action (VLA) models mark a transformative advancement in artificial intelligence, aiming to unify perception, natural language understanding, and embodied action within a single computational framework.\n\n## Action Refinement in VLA Systems\n\nUpon encountering variations (e.g., a tilted bottle or slippery grip), Helix's agentic AI module performs micro-policy refinement in real time, adjusting its grip based on feedback. This demonstrates how modern VLA systems implement real-time action refinement mechanisms.\n\nAdditionally, reinforcement learning feedback loops enable continuous improvement. As the robot executes tasks, it receives feedback about success or failure, reward signals, and corrections from human operators. This feedback drives ongoing policy refinement, allowing the system to adapt to new objects, environments, and task variations.\n\n## Recent Advances and Methods\n\nSeveral notable approaches to action refinement have emerged:\n\n- **Action Chain-of-Thought (ACoT)**: Action Chain-of-Thought (ACoT) is a reasoning paradigm where the deliberative process is formulated as structured action intents, enabling grounded and long-horizon policy learning.\n\n- **ActionX Framework**: ActionX is a pretraining framework that learns Action eXperts using reinforcement learning while leveraging a frozen, pretrained Vision-Language Model (VLM) backbone.\n\n- **Human-Robot Collaboration**: Human–Robot Collaboration research has explored interactive learning loops where humans and VLA models refine each other's performance. Collaborative frameworks integrate limited expert interventions into VLA decision-making, reducing operator workload while enriching model training data.\n\nThe field continues to rapidly evolve with significant research activities ongoing through 2026, as evidenced by upcoming conferences and workshops focused on VLA development."
    ],
    "durationSeconds": 8.579912642
  }
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-14T03:16:48.805Z_

<details><summary>↩ Tool result · `toolu_01GkRfFGSBnTW84C4zhF47DZ`</summary>

```text
Web search results for query: ""per-dimension uncertainty" robot learning action space 2025 2026"

Links: [{"title":"ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics","url":"https://arxiv.org/html/2603.18336v2"},{"title":"MotuBrain: An Advanced World Action Model for Robot Control","url":"https://arxiv.org/html/2604.27792v2"},{"title":"World Action Models are Zero-shot Policies","url":"https://arxiv.org/html/2602.15922v1"},{"title":"Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising","url":"https://arxiv.org/html/2604.26694v2"},{"title":"Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning | Science Robotics","url":"https://www.science.org/doi/10.1126/scirobotics.ads5033"},{"title":"Mask World Model: Predicting What Matters for Robust Robot Policy Learning","url":"https://arxiv.org/pdf/2604.19683"},{"title":"SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World RL","url":"https://arxiv.org/html/2506.04147"},{"title":"LeRobot: An Open-Source Library for End-to-End Robot ...","url":"https://arxiv.org/pdf/2602.22818"},{"title":"CoRL 2026 - Call for Papers","url":"https://www.corl.org/contributions/call-for-papers"},{"title":"Robotics Mar 2025","url":"https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"}]

Based on the search results, I found relevant research on uncertainty in robot learning and action space design from 2025-2026, though the specific term "per-dimension uncertainty" doesn't appear as a primary focus in these results. Here's what the recent literature shows:

## Key Findings

**Uncertainty in Robot Learning:**

Three sources of uncertainty arise jointly during execution: perceptual uncertainty from noisy and delayed observations, parametric uncertainty from inaccurate physical parameter estimation, and structural uncertainty from imperfect dynamics models. Robust manipulation under uncertainty is fundamentally a unification problem: when perceptual, parametric, and structural uncertainties are handled independently, their errors accumulate throughout the pipeline, calling for a unified framework that represents, propagates, and constrains them jointly.

**Action Space and Control:**

Recent work from 2025-2026 has focused on learned action spaces and latent action representations. SLAC is a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space, training this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety.

**Uncertainty Estimation:**

Integrating stronger uncertainty estimation, explicit memory, and online test-time adaptation may further improve robustness in open-world settings where disturbances and task variations cannot be fully covered during training.

The research landscape emphasizes joint representation and propagation of uncertainty across multiple dimensions of robot learning, though specific per-dimension uncertainty formulations may be developing approaches not yet widely documented in publicly available papers.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "b01e2f23-2c05-4bec-88b9-0da518ad54d8",
  "tool_use_result": {
    "query": "\"per-dimension uncertainty\" robot learning action space 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xwf6784Rm8UqZ4NSpooLJi",
        "content": [
          {
            "title": "ManiDreams: An Open-Source Library for Robust Object Manipulation via Uncertainty-aware Task-specific Intuitive Physics",
            "url": "https://arxiv.org/html/2603.18336v2"
          },
          {
            "title": "MotuBrain: An Advanced World Action Model for Robot Control",
            "url": "https://arxiv.org/html/2604.27792v2"
          },
          {
            "title": "World Action Models are Zero-shot Policies",
            "url": "https://arxiv.org/html/2602.15922v1"
          },
          {
            "title": "Unified 4D World Action Modeling from Video Priors with Asynchronous Denoising",
            "url": "https://arxiv.org/html/2604.26694v2"
          },
          {
            "title": "Precise and dexterous robotic manipulation via human-in-the-loop reinforcement learning | Science Robotics",
            "url": "https://www.science.org/doi/10.1126/scirobotics.ads5033"
          },
          {
            "title": "Mask World Model: Predicting What Matters for Robust Robot Policy Learning",
            "url": "https://arxiv.org/pdf/2604.19683"
          },
          {
            "title": "SLAC: Simulation-Pretrained Latent Action Space for Whole-Body Real-World RL",
            "url": "https://arxiv.org/html/2506.04147"
          },
          {
            "title": "LeRobot: An Open-Source Library for End-to-End Robot ...",
            "url": "https://arxiv.org/pdf/2602.22818"
          },
          {
            "title": "CoRL 2026 - Call for Papers",
            "url": "https://www.corl.org/contributions/call-for-papers"
          },
          {
            "title": "Robotics Mar 2025",
            "url": "https://arxiv.org/list/cs.RO/2025-03?skip=225&show=500"
          }
        ]
      },
      "Based on the search results, I found relevant research on uncertainty in robot learning and action space design from 2025-2026, though the specific term \"per-dimension uncertainty\" doesn't appear as a primary focus in these results. Here's what the recent literature shows:\n\n## Key Findings\n\n**Uncertainty in Robot Learning:**\n\nThree sources of uncertainty arise jointly during execution: perceptual uncertainty from noisy and delayed observations, parametric uncertainty from inaccurate physical parameter estimation, and structural uncertainty from imperfect dynamics models. Robust manipulation under uncertainty is fundamentally a unification problem: when perceptual, parametric, and structural uncertainties are handled independently, their errors accumulate throughout the pipeline, calling for a unified framework that represents, propagates, and constrains them jointly.\n\n**Action Space and Control:**\n\nRecent work from 2025-2026 has focused on learned action spaces and latent action representations. SLAC is a method that renders real-world RL feasible for complex embodiments by leveraging a low-fidelity simulator to pretrain a task-agnostic latent action space, training this latent action space via a customized unsupervised skill discovery method designed to promote temporal abstraction, disentanglement, and safety.\n\n**Uncertainty Estimation:**\n\nIntegrating stronger uncertainty estimation, explicit memory, and online test-time adaptation may further improve robustness in open-world settings where disturbances and task variations cannot be fully covered during training.\n\nThe research landscape emphasizes joint representation and propagation of uncertainty across multiple dimensions of robot learning, though specific per-dimension uncertainty formulations may be developing approaches not yet widely documented in publicly available papers."
    ],
    "durationSeconds": 7.583246298999999
  }
}
```

</details>

---

### Tool result

_source line 21 · 2026-05-14T03:16:49.012Z_

<details><summary>↩ Tool result · `toolu_015mi4y1rfvPwLnihY2vfsGm`</summary>

```text
Web search results for query: "ReconVLA "sample consensus" robot VLA multi-sample inference 2025 2026"

Links: [{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/abs/2508.10333"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://arxiv.org/html/2508.10333v1"},{"title":"GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub","url":"https://github.com/OpenHelix-Team/ReconVLA"},{"title":"DeeR-VLA: Dynamic Inference of Multimodal Large ...","url":"https://openreview.net/pdf?id=QKp3nhPU41"},{"title":"GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub","url":"https://github.com/openvla/openvla"},{"title":"ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver","url":"https://zionchow.github.io/ReconVLA/"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"VLA-Grasp: a vision-language-action modeling with cross-modality fusion for task-oriented grasping | Complex & Intelligent Systems | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s40747-025-01893-x"}]

Based on my search results, I found information relevant to your query about ReconVLA and multi-sample inference. Here's what I discovered:

## ReconVLA Overview

There are actually two different ReconVLA papers:

1. **ReconVLA: Uncertainty-Guided Framework** - This version presents a framework where a pretrained VLA policy produces action outputs and internal state estimates from visual observations and language instructions. ReconVLA augments this with two uncertainty-aware components: a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability, and an SMD-based detector that monitors latent state distributions to identify out-of-distribution or failure-prone conditions.

2. **ReconVLA: Reconstructive Vision-Language-Action Model** - This proposes a reconstructive VLA model with an implicit grounding paradigm where, conditioned on the model's visual outputs, a diffusion transformer aims to reconstruct the gaze region of the image which corresponds to target manipulated objects. This process prompts the VLA model to learn fine-grained representations and accurately allocate visual attention.

## Multi-Sample Inference

Regarding multi-sample inference, the first ReconVLA paper addresses this: Generative VLA policies can produce multiple candidate action sequences for the same observation due to their stochastic sampling, such as different noise realizations in a diffusion policy. These actions often exhibit different levels of reliability, which can lead to unstable execution if a low-quality sample is chosen. The CQR Action Selection component evaluates the uncertainty of multiple noise-conditioned action samples and selects the action with the lowest predicted uncertainty for execution.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "afc1f28d-69f6-496b-8d0b-7b0b23e0510f",
  "tool_use_result": {
    "query": "ReconVLA \"sample consensus\" robot VLA multi-sample inference 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YWK9y3Er2FHmiHzMyWRKWm",
        "content": [
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "[2508.10333] ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/abs/2508.10333"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://arxiv.org/html/2508.10333v1"
          },
          {
            "title": "GitHub - OpenHelix-Team/ReconVLA: Official implementation of ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver. · GitHub",
            "url": "https://github.com/OpenHelix-Team/ReconVLA"
          },
          {
            "title": "DeeR-VLA: Dynamic Inference of Multimodal Large ...",
            "url": "https://openreview.net/pdf?id=QKp3nhPU41"
          },
          {
            "title": "GitHub - openvla/openvla: OpenVLA: An open-source vision-language-action model for robotic manipulation. · GitHub",
            "url": "https://github.com/openvla/openvla"
          },
          {
            "title": "ReconVLA: Reconstructive Vision-Language-Action Model as Effective Robot Perceiver",
            "url": "https://zionchow.github.io/ReconVLA/"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "VLA-Grasp: a vision-language-action modeling with cross-modality fusion for task-oriented grasping | Complex & Intelligent Systems | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s40747-025-01893-x"
          }
        ]
      },
      "Based on my search results, I found information relevant to your query about ReconVLA and multi-sample inference. Here's what I discovered:\n\n## ReconVLA Overview\n\nThere are actually two different ReconVLA papers:\n\n1. **ReconVLA: Uncertainty-Guided Framework** - This version presents a framework where a pretrained VLA policy produces action outputs and internal state estimates from visual observations and language instructions. ReconVLA augments this with two uncertainty-aware components: a CQR-based estimator that computes calibrated action-level uncertainty to guide reliable action selection under generative variability, and an SMD-based detector that monitors latent state distributions to identify out-of-distribution or failure-prone conditions.\n\n2. **ReconVLA: Reconstructive Vision-Language-Action Model** - This proposes a reconstructive VLA model with an implicit grounding paradigm where, conditioned on the model's visual outputs, a diffusion transformer aims to reconstruct the gaze region of the image which corresponds to target manipulated objects. This process prompts the VLA model to learn fine-grained representations and accurately allocate visual attention.\n\n## Multi-Sample Inference\n\nRegarding multi-sample inference, the first ReconVLA paper addresses this: Generative VLA policies can produce multiple candidate action sequences for the same observation due to their stochastic sampling, such as different noise realizations in a diffusion policy. These actions often exhibit different levels of reliability, which can lead to unstable execution if a low-quality sample is chosen. The CQR Action Selection component evaluates the uncertainty of multiple noise-conditioned action samples and selects the action with the lowest predicted uncertainty for execution."
    ],
    "durationSeconds": 8.27386853
  }
}
```

</details>

---

### Assistant

_source line 22_

<details><summary>Logged reasoning block</summary>

```text
Good, I found several leads. Let me now do more targeted searches to find papers I haven't seen yet, especially:
1. The "Learnable Conformal Prediction" paper (2509.21955)
2. ACoT-VLA (CVPR 2026)
3. Safe Probabilistic Planning with Conformal Risk Control (2603.10392)
4. DiffusionVLA
5. IMLE Policy
6. The ICLR 2026 VLA blog post for leads
7. More specific searches on conformal prediction + VLA

Let me search for more specific things.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "a890dffd-e28e-4fcd-aece-9cc2361cac12",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 23_

Found several leads. Let me dig deeper on specific papers and additional directions.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "df1efc59-e1fc-47c5-8a67-7276099d8860",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PSdzrR9ihsmfVwYogMuzh1`</summary>

```json
{
  "query": "ACoT-VLA \"action chain-of-thought\" CVPR 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "7db67343-579a-4e5d-8246-a11b05d2ac82",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 25_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CKE6xQ9xdRisNg87qCKKCx`</summary>

```json
{
  "query": "DiffusionVLA autoregressive diffusion VLA arxiv 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "fde515d1-cf14-434c-8ce9-1c74c70762bd",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_019DfyzKE2meBEgdN95haZcK`</summary>

```json
{
  "query": "\"conformal prediction\" VLA policy uncertainty calibration robot 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "838d47a9-c541-4588-9651-0095d0490e29",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UFrY62Ft6quCFWna9Pb66m`</summary>

```json
{
  "query": "\"learnable conformal prediction\" robotic planning perception arxiv 2509.21955"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "19525153-a569-4754-b5dd-68d97cc74f4b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 28_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RVBvE46mZ965nVCj5vNuyX`</summary>

```json
{
  "query": "conformal prediction \"action space\" \"degree of freedom\" multivariate robot 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "ebf12b7f-7439-4533-b1b2-5fef12865729",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DcEJSaV1hBiFuMcfzdHyp7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1855,
      "cache_creation_input_tokens": 3228,
      "cache_read_input_tokens": 30716,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3228
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

_source line 29 · 2026-05-14T03:17:05.658Z_

<details><summary>↩ Tool result · `toolu_01PSdzrR9ihsmfVwYogMuzh1`</summary>

```text
Web search results for query: "ACoT-VLA "action chain-of-thought" CVPR 2026 arxiv"

Links: [{"title":"[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/abs/2601.11404"},{"title":"GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub","url":"https://github.com/AgibotTech/ACoT-VLA"},{"title":"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://arxiv.org/html/2601.11404v1"},{"title":"[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/abs/2503.22020"},{"title":"[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"},{"title":"CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/html/2503.22020v1"},{"title":"(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"},{"title":"Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models","url":"https://huggingface.co/papers/2601.11404"},{"title":"CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models","url":"https://cvpr.thecvf.com/virtual/2025/poster/33233"},{"title":"[2603.22280] DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models","url":"https://arxiv.org/abs/2603.22280"}]

Based on the search results, I found comprehensive information about ACoT-VLA:

## ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models

ACoT-VLA is the official implementation of "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models" accepted at CVPR 2026.

### Core Concept

Action Chain-of-Thought (ACoT) is a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.

### Architecture

The architecture introduces two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR). The former proposes coarse reference trajectories as explicit action-level reasoning steps, while the latter extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.

### Key Results

The method achieves state-of-the-art performance on multiple benchmarks, with 98.5%, 84.1% and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively.

### Paper Details

The paper was first submitted on January 16, 2026, with a second version on March 30, 2026. The arXiv identifier is 2601.11404, and the repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "336770be-9019-440b-8c3c-78e64e805185",
  "tool_use_result": {
    "query": "ACoT-VLA \"action chain-of-thought\" CVPR 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_019YNLpTNkjmgGz6BsVS1iNi",
        "content": [
          {
            "title": "[2601.11404] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2601.11404"
          },
          {
            "title": "GitHub - AgibotTech/ACoT-VLA: [CVPR 2026] Official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" · GitHub",
            "url": "https://github.com/AgibotTech/ACoT-VLA"
          },
          {
            "title": "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2601.11404v1"
          },
          {
            "title": "[2503.22020] CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2503.22020"
          },
          {
            "title": "[Quick Review] ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://liner.com/review/acotvla-action-chainofthought-for-visionlanguageaction-models"
          },
          {
            "title": "CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2503.22020v1"
          },
          {
            "title": "(PDF) ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/399875837_ACoT-VLA_Action_Chain-of-Thought_for_Vision-Language-Action_Models"
          },
          {
            "title": "Paper page - ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models",
            "url": "https://huggingface.co/papers/2601.11404"
          },
          {
            "title": "CVPR Poster CoT-VLA: Visual Chain-of-Thought Reasoning for Vision-Language-Action Models",
            "url": "https://cvpr.thecvf.com/virtual/2025/poster/33233"
          },
          {
            "title": "[2603.22280] DualCoT-VLA: Visual-Linguistic Chain of Thought via Parallel Reasoning for Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2603.22280"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about ACoT-VLA:\n\n## ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\n\nACoT-VLA is the official implementation of \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\" accepted at CVPR 2026.\n\n### Core Concept\n\nAction Chain-of-Thought (ACoT) is a paradigm where the reasoning process itself is formulated as a structured sequence of coarse action intents that guide the final policy.\n\n### Architecture\n\nThe architecture introduces two complementary components: an Explicit Action Reasoner (EAR) and Implicit Action Reasoner (IAR). The former proposes coarse reference trajectories as explicit action-level reasoning steps, while the latter extracts latent action priors from internal representations of multimodal input, co-forming an ACoT that conditions the downstream action head to enable grounded policy learning.\n\n### Key Results\n\nThe method achieves state-of-the-art performance on multiple benchmarks, with 98.5%, 84.1% and 47.4% on LIBERO, LIBERO-Plus and VLABench, respectively.\n\n### Paper Details\n\nThe paper was first submitted on January 16, 2026, with a second version on March 30, 2026. The arXiv identifier is 2601.11404, and the repository serves as the official baseline implementation for the AgiBot World Challenge @ ICRA 2026."
    ],
    "durationSeconds": 7.1948078490000045
  }
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-14T03:17:06.500Z_

<details><summary>↩ Tool result · `toolu_01CKE6xQ9xdRisNg87qCKKCx`</summary>

```text
Web search results for query: "DiffusionVLA autoregressive diffusion VLA arxiv 2025 2026"

Links: [{"title":"DiffusionVLA: Autoregressive Reasoning and Diffusion Policies for Generalizable Vision-Language-Action Models","url":"https://diffusion-vla.github.io/"},{"title":"Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression","url":"https://arxiv.org/html/2412.03293v1"},{"title":"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/html/2412.03293v2"},{"title":"[2412.03293] Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning","url":"https://arxiv.org/abs/2412.03293"},{"title":"arXiv:2503.10631v3 [cs.CV] 23 Jun 2025","url":"https://arxiv.org/pdf/2503.10631"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/html/2508.20072v1"},{"title":"HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model","url":"https://arxiv.org/html/2503.10631v1"},{"title":"[2508.20072] Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies","url":"https://arxiv.org/abs/2508.20072"},{"title":"Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies | OpenReview","url":"https://openreview.net/forum?id=YWeNCMxdhM"},{"title":"Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | alphaXiv","url":"https://www.alphaxiv.org/overview/2412.03293v1"}]

I found several relevant papers on DiffusionVLA and related autoregressive diffusion VLA models. Here are the key findings:

## DiffusionVLA (DiVLA)

DiffusionVLA was accepted by ICML 2025. DiffusionVLA is a novel framework that integrates autoregressive reasoning with diffusion policies to address the limitations of existing methods: while autoregressive Vision-Language-Action (VLA) models lack precise and robust action generation, diffusion-based policies inherently lack reasoning capabilities.

The core approach involves:
- Autoregressive reasoning — a task decomposition and explanation process enabled by a pre-trained VLM — to guide diffusion-based action policies, with a reasoning injection module that directly embeds self-generated reasoning phrases into the policy learning process
- A next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations, and a diffusion model is attached to generate robust action outputs

Performance capabilities include:
- The smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task
- The model scales from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size

## Related Work

Other recent papers combining autoregressive and diffusion approaches include HybridVLA, which seamlessly integrates diffusion modeling into the autoregressive next-token prediction within a single LLM, and Discrete Diffusion VLA, a unified-transformer policy that models discretized action chunks with discrete diffusion.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "6dd9ed38-1b78-4fa0-982e-dad43b37e538",
  "tool_use_result": {
    "query": "DiffusionVLA autoregressive diffusion VLA arxiv 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DgfgWZFzaCp92B5ZXsr3i2",
        "content": [
          {
            "title": "DiffusionVLA: Autoregressive Reasoning and Diffusion Policies for Generalizable Vision-Language-Action Models",
            "url": "https://diffusion-vla.github.io/"
          },
          {
            "title": "Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression",
            "url": "https://arxiv.org/html/2412.03293v1"
          },
          {
            "title": "Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning",
            "url": "https://arxiv.org/html/2412.03293v2"
          },
          {
            "title": "[2412.03293] Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning",
            "url": "https://arxiv.org/abs/2412.03293"
          },
          {
            "title": "arXiv:2503.10631v3 [cs.CV] 23 Jun 2025",
            "url": "https://arxiv.org/pdf/2503.10631"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/html/2508.20072v1"
          },
          {
            "title": "HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model",
            "url": "https://arxiv.org/html/2503.10631v1"
          },
          {
            "title": "[2508.20072] Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies",
            "url": "https://arxiv.org/abs/2508.20072"
          },
          {
            "title": "Discrete Diffusion VLA: Bringing Discrete Diffusion to Action Decoding in Vision-Language-Action Policies | OpenReview",
            "url": "https://openreview.net/forum?id=YWeNCMxdhM"
          },
          {
            "title": "Diffusion-VLA: Scaling Robot Foundation Models via Unified Diffusion and Autoregression | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2412.03293v1"
          }
        ]
      },
      "I found several relevant papers on DiffusionVLA and related autoregressive diffusion VLA models. Here are the key findings:\n\n## DiffusionVLA (DiVLA)\n\nDiffusionVLA was accepted by ICML 2025. DiffusionVLA is a novel framework that integrates autoregressive reasoning with diffusion policies to address the limitations of existing methods: while autoregressive Vision-Language-Action (VLA) models lack precise and robust action generation, diffusion-based policies inherently lack reasoning capabilities.\n\nThe core approach involves:\n- Autoregressive reasoning — a task decomposition and explanation process enabled by a pre-trained VLM — to guide diffusion-based action policies, with a reasoning injection module that directly embeds self-generated reasoning phrases into the policy learning process\n- A next-token prediction objective, enabling the model to reason effectively over the user's query in the context of current observations, and a diffusion model is attached to generate robust action outputs\n\nPerformance capabilities include:\n- The smallest DiffusionVLA-2B runs 82Hz on a single A6000 GPU and can train from scratch on less than 50 demonstrations for a complex task\n- The model scales from 2B to 72B parameters, showcasing improved generalization capabilities with increased model size\n\n## Related Work\n\nOther recent papers combining autoregressive and diffusion approaches include HybridVLA, which seamlessly integrates diffusion modeling into the autoregressive next-token prediction within a single LLM, and Discrete Diffusion VLA, a unified-transformer policy that models discretized action chunks with discrete diffusion."
    ],
    "durationSeconds": 7.655754686
  }
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-14T03:17:07.933Z_

<details><summary>↩ Tool result · `toolu_019DfyzKE2meBEgdN95haZcK`</summary>

```text
Web search results for query: ""conformal prediction" VLA policy uncertainty calibration robot 2025 2026 arxiv"

Links: [{"title":"[2604.27149] ConformaDecompose: Explaining Uncertainty via Calibration Localization","url":"https://arxiv.org/abs/2604.27149"},{"title":"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration","url":"https://um-arm-lab.github.io/lucca/"},{"title":"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/html/2509.21955v1"},{"title":"[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/abs/2509.21955"},{"title":"Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling","url":"https://arxiv.org/html/2508.05634v1"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383v2"},{"title":"Another Fit Bites the Dust: Conformal Prediction as a Calibration Standard for Machine Learning in High-Energy Physics","url":"https://arxiv.org/html/2512.17048v1"},{"title":"[2604.08885] Uncertainty-Aware Transformers: Conformal Prediction for Language Models","url":"https://arxiv.org/abs/2604.08885"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392v1"},{"title":"Proceedings of Machine Learning Research vol vvv:1–25, 2026","url":"https://arxiv.org/pdf/2602.12616"}]

I found several relevant papers on arXiv related to conformal prediction, uncertainty calibration, and robotics from 2025-2026. Here are the key findings:

## Recent Research on Conformal Prediction in Robotics

**Vision-Language-Action (VLA) Models with Calibration:**

A recent study examines confidence calibration in vision-language-action (VLA) foundation models, establishing a confidence baseline for VLAs and introducing lightweight techniques to remedy miscalibration including prompt ensembles and action-wise Platt scaling.

**Learnable Conformal Prediction for Robotic Planning:**

Learnable Conformal Prediction (LCP) addresses the limitation that conformal prediction relies on fixed nonconformity scores that ignore context, by replacing fixed scores with a lightweight neural function that leverages geometric, semantic, and task-specific features to produce context-aware uncertainty sets. LCP maintains conformal prediction's theoretical guarantees while reducing prediction set sizes by 18% in classification, tightening detection intervals by 52%, and improving path planning safety from 72% to 91% success with minimal overhead.

**Uncertainty in Dynamics Models:**

Local Uncertainty Conformal Calibration (LUCCa) is a conformal prediction-based approach that calibrates the aleatoric uncertainty estimates provided by dynamics models to generate probabilistically-valid prediction regions.

**Safe Planning with Conformal Risk Control:**

A framework combines conformal risk control with control-theoretic safety constraints to achieve provable safety guarantees in human-robot interactions, specifically applying conformal risk control to algorithmically tune a safety margin for a safety constraint expressed using Control Barrier Functions.

These papers represent cutting-edge work in applying conformal prediction methods to robotics for uncertainty quantification and safety-critical control.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "44effba0-b814-46c4-a368-0771acf5f207",
  "tool_use_result": {
    "query": "\"conformal prediction\" VLA policy uncertainty calibration robot 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BAbqCTf48H2dbzDVy8emde",
        "content": [
          {
            "title": "[2604.27149] ConformaDecompose: Explaining Uncertainty via Calibration Localization",
            "url": "https://arxiv.org/abs/2604.27149"
          },
          {
            "title": "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration",
            "url": "https://um-arm-lab.github.io/lucca/"
          },
          {
            "title": "Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/html/2509.21955v1"
          },
          {
            "title": "[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/abs/2509.21955"
          },
          {
            "title": "Towards Generalizable Safety in Crowd Navigation via Conformal Uncertainty Handling",
            "url": "https://arxiv.org/html/2508.05634v1"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2507.17383v2"
          },
          {
            "title": "Another Fit Bites the Dust: Conformal Prediction as a Calibration Standard for Machine Learning in High-Energy Physics",
            "url": "https://arxiv.org/html/2512.17048v1"
          },
          {
            "title": "[2604.08885] Uncertainty-Aware Transformers: Conformal Prediction for Language Models",
            "url": "https://arxiv.org/abs/2604.08885"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392v1"
          },
          {
            "title": "Proceedings of Machine Learning Research vol vvv:1–25, 2026",
            "url": "https://arxiv.org/pdf/2602.12616"
          }
        ]
      },
      "I found several relevant papers on arXiv related to conformal prediction, uncertainty calibration, and robotics from 2025-2026. Here are the key findings:\n\n## Recent Research on Conformal Prediction in Robotics\n\n**Vision-Language-Action (VLA) Models with Calibration:**\n\nA recent study examines confidence calibration in vision-language-action (VLA) foundation models, establishing a confidence baseline for VLAs and introducing lightweight techniques to remedy miscalibration including prompt ensembles and action-wise Platt scaling.\n\n**Learnable Conformal Prediction for Robotic Planning:**\n\nLearnable Conformal Prediction (LCP) addresses the limitation that conformal prediction relies on fixed nonconformity scores that ignore context, by replacing fixed scores with a lightweight neural function that leverages geometric, semantic, and task-specific features to produce context-aware uncertainty sets. LCP maintains conformal prediction's theoretical guarantees while reducing prediction set sizes by 18% in classification, tightening detection intervals by 52%, and improving path planning safety from 72% to 91% success with minimal overhead.\n\n**Uncertainty in Dynamics Models:**\n\nLocal Uncertainty Conformal Calibration (LUCCa) is a conformal prediction-based approach that calibrates the aleatoric uncertainty estimates provided by dynamics models to generate probabilistically-valid prediction regions.\n\n**Safe Planning with Conformal Risk Control:**\n\nA framework combines conformal risk control with control-theoretic safety constraints to achieve provable safety guarantees in human-robot interactions, specifically applying conformal risk control to algorithmically tune a safety margin for a safety constraint expressed using Control Barrier Functions.\n\nThese papers represent cutting-edge work in applying conformal prediction methods to robotics for uncertainty quantification and safety-critical control."
    ],
    "durationSeconds": 8.143079495999999
  }
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-14T03:17:08.817Z_

<details><summary>↩ Tool result · `toolu_01UFrY62Ft6quCFWna9Pb66m`</summary>

```text
Web search results for query: ""learnable conformal prediction" robotic planning perception arxiv 2509.21955"

Links: [{"title":"[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/abs/2509.21955"},{"title":"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/html/2509.21955"},{"title":"Machine Learning Sep 2025","url":"https://arxiv.org/list/cs.LG/2025-09?skip=3775&show=2000"},{"title":"Uncertainty-Guided Inference-Time Depth Adaptation for Transformer-Based Visual Tracking","url":"https://arxiv.org/html/2602.16160v1"},{"title":"1 Safe Planning in Unknown Environments using Conformalized Semantic Maps","url":"https://arxiv.org/pdf/2509.25124"},{"title":"Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v1"},{"title":"Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model | OpenReview","url":"https://openreview.net/forum?id=VeO03T59Sh"},{"title":"Conformal Prediction for Semantically-Aware Autonomous ...","url":"https://raw.githubusercontent.com/mlresearch/v270/main/assets/doula25a/doula25a.pdf"},{"title":"[PDF] Seeing with Partial Certainty: Conformal Prediction ...","url":"https://www.semanticscholar.org/paper/b38046ac7caff6c1a5befe70dbc0531d84175a37"},{"title":"[2509.25124] Safe Planning in Unknown Environments using Conformalized Semantic Maps","url":"https://arxiv.org/abs/2509.25124"}]

I found the paper! Here's a summary of the research:

## Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception

The paper addresses the problem that deep learning models in robotics often output point estimates with poorly calibrated confidences, offering no native mechanism to quantify predictive reliability under novel, noisy, or out-of-distribution inputs.

### The Proposed Method

While conformal prediction (CP) provides distribution-free coverage guarantees, its reliance on fixed nonconformity scores ignores context and can yield intervals that are overly conservative or unsafe. The authors introduce Learnable Conformal Prediction (LCP), which replaces fixed scores with a lightweight neural function that leverages geometric, semantic, and task-specific features.

### Key Results

Calibration over these learned scores preserves the finite-sample coverage guarantees of CP while producing intervals that shrink in simple cases and expand in difficult ones. 

The authors evaluate LCP for robotic path planning under noisy and incomplete sensing on the MRPB benchmark, object detection with uncertainty calibration on COCO, BDD100K, and Cityscapes, and image classification on CIFAR-100, HAM10000, and ImageNet. Across these benchmarks, LCP consistently improves the safety–efficiency trade-off.

On the MRPB benchmark, LCP raised navigation success to 91.5% with only 4.5% path inflation, compared to 12.2% for Standard CP. For object detection, it reduced interval widths by 46–54% at 90% coverage, and in classification it cut set sizes by 4.7–9.9%.

The paper was submitted to arXiv on September 26, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "a2d71959-4f86-4d81-882b-0a1228e785e6",
  "tool_use_result": {
    "query": "\"learnable conformal prediction\" robotic planning perception arxiv 2509.21955",
    "results": [
      {
        "tool_use_id": "srvtoolu_011WDtcEDG52zWz7n1wnceQg",
        "content": [
          {
            "title": "[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/abs/2509.21955"
          },
          {
            "title": "Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/html/2509.21955"
          },
          {
            "title": "Machine Learning Sep 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-09?skip=3775&show=2000"
          },
          {
            "title": "Uncertainty-Guided Inference-Time Depth Adaptation for Transformer-Based Visual Tracking",
            "url": "https://arxiv.org/html/2602.16160v1"
          },
          {
            "title": "1 Safe Planning in Unknown Environments using Conformalized Semantic Maps",
            "url": "https://arxiv.org/pdf/2509.25124"
          },
          {
            "title": "Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368v1"
          },
          {
            "title": "Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model | OpenReview",
            "url": "https://openreview.net/forum?id=VeO03T59Sh"
          },
          {
            "title": "Conformal Prediction for Semantically-Aware Autonomous ...",
            "url": "https://raw.githubusercontent.com/mlresearch/v270/main/assets/doula25a/doula25a.pdf"
          },
          {
            "title": "[PDF] Seeing with Partial Certainty: Conformal Prediction ...",
            "url": "https://www.semanticscholar.org/paper/b38046ac7caff6c1a5befe70dbc0531d84175a37"
          },
          {
            "title": "[2509.25124] Safe Planning in Unknown Environments using Conformalized Semantic Maps",
            "url": "https://arxiv.org/abs/2509.25124"
          }
        ]
      },
      "I found the paper! Here's a summary of the research:\n\n## Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\n\nThe paper addresses the problem that deep learning models in robotics often output point estimates with poorly calibrated confidences, offering no native mechanism to quantify predictive reliability under novel, noisy, or out-of-distribution inputs.\n\n### The Proposed Method\n\nWhile conformal prediction (CP) provides distribution-free coverage guarantees, its reliance on fixed nonconformity scores ignores context and can yield intervals that are overly conservative or unsafe. The authors introduce Learnable Conformal Prediction (LCP), which replaces fixed scores with a lightweight neural function that leverages geometric, semantic, and task-specific features.\n\n### Key Results\n\nCalibration over these learned scores preserves the finite-sample coverage guarantees of CP while producing intervals that shrink in simple cases and expand in difficult ones. \n\nThe authors evaluate LCP for robotic path planning under noisy and incomplete sensing on the MRPB benchmark, object detection with uncertainty calibration on COCO, BDD100K, and Cityscapes, and image classification on CIFAR-100, HAM10000, and ImageNet. Across these benchmarks, LCP consistently improves the safety–efficiency trade-off.\n\nOn the MRPB benchmark, LCP raised navigation success to 91.5% with only 4.5% path inflation, compared to 12.2% for Standard CP. For object detection, it reduced interval widths by 46–54% at 90% coverage, and in classification it cut set sizes by 4.7–9.9%.\n\nThe paper was submitted to arXiv on September 26, 2025."
    ],
    "durationSeconds": 8.086563414000004
  }
}
```

</details>

---

### Tool result

_source line 33 · 2026-05-14T03:17:10.072Z_

<details><summary>↩ Tool result · `toolu_01RVBvE46mZ965nVCj5vNuyX`</summary>

```text
Web search results for query: "conformal prediction "action space" "degree of freedom" multivariate robot 2025 2026"

Links: [{"title":"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/html/2509.21955"},{"title":"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration","url":"https://um-arm-lab.github.io/lucca/"},{"title":"ICML Poster Optimal transport-based conformal prediction","url":"https://icml.cc/virtual/2025/poster/44266"},{"title":"[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception","url":"https://arxiv.org/abs/2509.21955"},{"title":"Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024","url":"https://www.roboticsproceedings.org/rss20/p008.pdf"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392v1"},{"title":"Adaptive Conformal Prediction for Motion Planning among ...","url":"https://proceedings.mlr.press/v211/dixit23a/dixit23a.pdf"},{"title":"Conformal Prediction Conference 2026","url":"https://copa-conference.com/"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"Publications","url":"https://depts.washington.edu/ctrl/publications/"}]

I found several highly relevant research papers and projects combining conformal prediction with robotics and multi-degree-of-freedom action spaces. Here are the key findings:

## Recent Work on Conformal Prediction for Robotics (2025-2026)

**Learnable Conformal Prediction for Robotic Planning and Perception**
Deep learning models in robotics often output point estimates with poorly calibrated confidences, offering no native mechanism to quantify predictive reliability under novel, noisy, or out-of-distribution inputs. Conformal prediction addresses this gap by providing distribution-free coverage guarantees, yet its reliance on fixed nonconformity scores ignores context and can yield intervals that are overly conservative or unsafe. This approach maintains CP's theoretical guarantees while reducing prediction set sizes by 18% in classification, tightening detection intervals by 52%, and improving path planning safety from 72% to 91% success with minimal overhead.

**Conformalized Teleoperation with Multi-DOF Action Space**
A particularly relevant application addresses exactly what your query highlights: conformal methods are leveraged to quantify if the robot's learned controller can reliably lift the human's low-DoF input (joystick) to their desired high-DoF action (7 joint velocities).

**Local Uncertainty Conformal Calibration (LUCCa)**
LUCCa provides probabilistically valid prediction regions for the robot's future states accounting for both aleatoric and epistemic uncertainty, and calibrates the uncertainty locally relative to the system's state-action space, leading to prediction regions that are representative of predictive uncertainty and therefore useful for planning.

**Safe Human-Robot Interaction with Conformal Risk Control**
The approach uses conformal risk control to quantify and control the prediction errors in CBF safety values and establishes formal guarantees on the probability of constraint satisfaction during interaction.

These recent developments show active research applying conformal prediction to multivariate robot control problems with formal uncertainty quantification guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "baaf776b-4826-400e-8ec4-3483d0475c11",
  "tool_use_result": {
    "query": "conformal prediction \"action space\" \"degree of freedom\" multivariate robot 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0138t8ETw1MoBh7hAebot9ZJ",
        "content": [
          {
            "title": "Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/html/2509.21955"
          },
          {
            "title": "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration",
            "url": "https://um-arm-lab.github.io/lucca/"
          },
          {
            "title": "ICML Poster Optimal transport-based conformal prediction",
            "url": "https://icml.cc/virtual/2025/poster/44266"
          },
          {
            "title": "[2509.21955] Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception",
            "url": "https://arxiv.org/abs/2509.21955"
          },
          {
            "title": "Robotics: Science and Systems 2024 Delft, Netherlands, July 15-July 19, 2024",
            "url": "https://www.roboticsproceedings.org/rss20/p008.pdf"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392v1"
          },
          {
            "title": "Adaptive Conformal Prediction for Motion Planning among ...",
            "url": "https://proceedings.mlr.press/v211/dixit23a/dixit23a.pdf"
          },
          {
            "title": "Conformal Prediction Conference 2026",
            "url": "https://copa-conference.com/"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          },
          {
            "title": "Publications",
            "url": "https://depts.washington.edu/ctrl/publications/"
          }
        ]
      },
      "I found several highly relevant research papers and projects combining conformal prediction with robotics and multi-degree-of-freedom action spaces. Here are the key findings:\n\n## Recent Work on Conformal Prediction for Robotics (2025-2026)\n\n**Learnable Conformal Prediction for Robotic Planning and Perception**\nDeep learning models in robotics often output point estimates with poorly calibrated confidences, offering no native mechanism to quantify predictive reliability under novel, noisy, or out-of-distribution inputs. Conformal prediction addresses this gap by providing distribution-free coverage guarantees, yet its reliance on fixed nonconformity scores ignores context and can yield intervals that are overly conservative or unsafe. This approach maintains CP's theoretical guarantees while reducing prediction set sizes by 18% in classification, tightening detection intervals by 52%, and improving path planning safety from 72% to 91% success with minimal overhead.\n\n**Conformalized Teleoperation with Multi-DOF Action Space**\nA particularly relevant application addresses exactly what your query highlights: conformal methods are leveraged to quantify if the robot's learned controller can reliably lift the human's low-DoF input (joystick) to their desired high-DoF action (7 joint velocities).\n\n**Local Uncertainty Conformal Calibration (LUCCa)**\nLUCCa provides probabilistically valid prediction regions for the robot's future states accounting for both aleatoric and epistemic uncertainty, and calibrates the uncertainty locally relative to the system's state-action space, leading to prediction regions that are representative of predictive uncertainty and therefore useful for planning.\n\n**Safe Human-Robot Interaction with Conformal Risk Control**\nThe approach uses conformal risk control to quantify and control the prediction errors in CBF safety values and establishes formal guarantees on the probability of constraint satisfaction during interaction.\n\nThese recent developments show active research applying conformal prediction to multivariate robot control problems with formal uncertainty quantification guarantees."
    ],
    "durationSeconds": 8.952515145999998
  }
}
```

</details>

---

### Assistant

_source line 34_

<details><summary>Logged reasoning block</summary>

```text
Let me now search for more specific papers that I've identified as potentially relevant:

1. "Confidence Calibration in Vision-Language-Action Models" (2507.17383)
2. LUCCa - Local Uncertainty Conformal Calibration
3. Safe Probabilistic Planning with Conformal Risk Control (2603.10392)
4. CoA-VLA (Chain-of-Affordance)
5. Any other VLA robustness/inference-time correction papers
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "e47093d0-5840-4143-8d7e-ac2d87491ac3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

_source line 35_

Found more leads. Let me search for specific papers I've identified.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "89e2bcb4-3356-44de-bf3d-d216c1f172b2",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

_source line 36_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NVWi9bN3FvSND2A8QNATJj`</summary>

```json
{
  "query": "\"Confidence Calibration in Vision-Language-Action Models\" arxiv 2507.17383"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "34ddd87d-47c8-466e-8bfc-c7587276efc9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

_source line 37_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012ySYDHM49qCtvxKTLznfYy`</summary>

```json
{
  "query": "LUCCa \"local uncertainty conformal calibration\" dynamics model robot arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "83b59b7f-227e-4503-8787-b87162a5bb5c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

_source line 38_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DRpZwUoo46Wqd6FJoSfw2w`</summary>

```json
{
  "query": "\"safe probabilistic planning\" \"conformal risk control\" human-robot arxiv 2603.10392"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "1a09e166-c46f-4bca-b564-fc81897e3da1",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_0153PsTs9kRHvW613QHEY1AM`</summary>

```json
{
  "query": "CoA-VLA \"chain of affordance\" vision language action ICCV 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "e695f5d4-6c91-47be-bbfe-366a0892759a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

_source line 40_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015FeMYnYCeyWdM8kej12hDC`</summary>

```json
{
  "query": "VLA inference-time correction residual policy robot 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "aeafa807-9b94-4d86-b49d-d986c47c876e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JckEXGTYUrEjp4vCCZUPsz",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 7159,
      "cache_read_input_tokens": 33944,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 7159
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

_source line 41 · 2026-05-14T03:17:25.331Z_

<details><summary>↩ Tool result · `toolu_01NVWi9bN3FvSND2A8QNATJj`</summary>

```text
Web search results for query: ""Confidence Calibration in Vision-Language-Action Models" arxiv 2507.17383"

Links: [{"title":"[2507.17383] Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/abs/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383"},{"title":"Confidence Calibration in Vision-Language-Action Models Thomas Zollo","url":"https://arxiv.org/pdf/2507.17383"},{"title":"(PDF) Confidence Calibration in Vision-Language-Action Models","url":"https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"},{"title":"Confidence Calibration in Vision-Language-Action Models | OpenReview","url":"https://openreview.net/forum?id=aiPC7jAd2f"},{"title":"confidence-calibration-in-vision-language-action-models - Ask this paper | Bohrium","url":"https://www.bohrium.com/paper-details/confidence-calibration-in-vision-language-action-models/1155114182379569160-108625"},{"title":"An Empirical Study Into What Matters for Calibrating Vision–Language Models","url":"https://arxiv.org/html/2402.07417v2"},{"title":"[2604.09529] VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning","url":"https://arxiv.org/abs/2604.09529"},{"title":"Machine Learning Jul 2025","url":"https://www.arxiv.org/list/cs.LG/2025-07?skip=2650&show=25"},{"title":"Confidence Calibration in Contrastive Vision-Language Models | SpringerLink","url":"https://link.springer.com/chapter/10.1007/978-3-031-94969-2_9"}]

## Search Results for arxiv 2507.17383

I found the paper you're looking for. Here's what I found:

**Title:** "Confidence Calibration in Vision-Language-Action Models"

**Authors:** Thomas P Zollo and Richard Zemel

**arXiv ID:** 2507.17383

**Key Information:**

The study presents a first-of-its-kind examination of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands.

The research establishes a confidence baseline for VLAs, examines how task success relates to calibration error and how calibration evolves over time, and introduces two lightweight techniques to remedy the miscalibration: prompt ensembles and action-wise Platt scaling.

A well-calibrated robot policy produces confidence estimates that align with its probability of task success, for example, the robot should succeed on 95% of instances for which it expresses 95% confidence.

The paper was submitted on July 23, 2025, and last revised on December 22, 2025. You can access the full paper on [arXiv](https://arxiv.org/abs/2507.17383).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "fd4550e8-0d09-4116-ba31-26a9d153e679",
  "tool_use_result": {
    "query": "\"Confidence Calibration in Vision-Language-Action Models\" arxiv 2507.17383",
    "results": [
      {
        "tool_use_id": "srvtoolu_012V9E9L9LpcMCcXkfNJKoxb",
        "content": [
          {
            "title": "[2507.17383] Confidence Calibration in Vision-Language-Action Models",
            "url": "https://arxiv.org/abs/2507.17383"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2507.17383"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models Thomas Zollo",
            "url": "https://arxiv.org/pdf/2507.17383"
          },
          {
            "title": "(PDF) Confidence Calibration in Vision-Language-Action Models",
            "url": "https://www.researchgate.net/publication/393966020_Confidence_Calibration_in_Vision-Language-Action_Models"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models | OpenReview",
            "url": "https://openreview.net/forum?id=aiPC7jAd2f"
          },
          {
            "title": "confidence-calibration-in-vision-language-action-models - Ask this paper | Bohrium",
            "url": "https://www.bohrium.com/paper-details/confidence-calibration-in-vision-language-action-models/1155114182379569160-108625"
          },
          {
            "title": "An Empirical Study Into What Matters for Calibrating Vision–Language Models",
            "url": "https://arxiv.org/html/2402.07417v2"
          },
          {
            "title": "[2604.09529] VL-Calibration: Decoupled Confidence Calibration for Large Vision-Language Models Reasoning",
            "url": "https://arxiv.org/abs/2604.09529"
          },
          {
            "title": "Machine Learning Jul 2025",
            "url": "https://www.arxiv.org/list/cs.LG/2025-07?skip=2650&show=25"
          },
          {
            "title": "Confidence Calibration in Contrastive Vision-Language Models | SpringerLink",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-94969-2_9"
          }
        ]
      },
      "## Search Results for arxiv 2507.17383\n\nI found the paper you're looking for. Here's what I found:\n\n**Title:** \"Confidence Calibration in Vision-Language-Action Models\"\n\n**Authors:** Thomas P Zollo and Richard Zemel\n\n**arXiv ID:** 2507.17383\n\n**Key Information:**\n\nThe study presents a first-of-its-kind examination of confidence calibration in vision-language-action (VLA) foundation models, which map visual observations and natural language instructions to low-level robot motor commands.\n\nThe research establishes a confidence baseline for VLAs, examines how task success relates to calibration error and how calibration evolves over time, and introduces two lightweight techniques to remedy the miscalibration: prompt ensembles and action-wise Platt scaling.\n\nA well-calibrated robot policy produces confidence estimates that align with its probability of task success, for example, the robot should succeed on 95% of instances for which it expresses 95% confidence.\n\nThe paper was submitted on July 23, 2025, and last revised on December 22, 2025. You can access the full paper on [arXiv](https://arxiv.org/abs/2507.17383)."
    ],
    "durationSeconds": 6.211019028999996
  }
}
```

</details>

---

### Tool result

_source line 42 · 2026-05-14T03:17:26.764Z_

<details><summary>↩ Tool result · `toolu_01DRpZwUoo46Wqd6FJoSfw2w`</summary>

```text
Web search results for query: ""safe probabilistic planning" "conformal risk control" human-robot arxiv 2603.10392"

Links: [{"title":"[2603.10392] Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/abs/2603.10392"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://arxiv.org/html/2603.10392"},{"title":"Publications","url":"https://depts.washington.edu/ctrl/publications/"},{"title":"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control","url":"https://jakeagonzales.github.io/crc-cbf-website/"},{"title":"Heterogeneous Predictor-based Risk-Aware Planning with Conformal Prediction in Dense, Uncertain Environments","url":"https://arxiv.org/html/2507.11920"},{"title":"Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions","url":"https://arxiv.org/html/2310.05921v3"},{"title":"Safe and Stable Neural Network Dynamical Systems for Robot Motion Planning","url":"https://arxiv.org/html/2511.20593"},{"title":"Safe POMDP Online Planning among Dynamic Agents via Adaptive Conformal Prediction","url":"https://arxiv.org/html/2404.15557v1"},{"title":"Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v3"},{"title":"Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction","url":"https://arxiv.org/html/2402.15368v4/"}]

I found the paper you're looking for. Here's what I found:

## Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control (arXiv:2603.10392)

**Overview:**
This paper presents a novel probabilistic safe control framework for human-robot interaction that combines control barrier functions (CBFs) with conformal risk control to provide formal safety guarantees while considering complex human behavior.

**Key Technical Contributions:**

1. **Methodology**: The approach uses conformal risk control to quantify and control the prediction errors in CBF safety values and establishes formal guarantees on the probability of constraint satisfaction during interaction.

2. **Adaptive Safety Margins**: The paper introduces an algorithm that dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context.

3. **Implementation**: The practical implementation does not rely on any distributional assumptions or worst-case bounds, and is both computationally efficient for real-time control and theoretically grounded.

**Experimental Results:**
Through experiments on human-robot navigation scenarios, the approach significantly reduces collision rates and safety violations as compared to baseline methods while maintaining high success rates in goal-reaching tasks and efficient control.

**Authors and Status:**
The paper is authored by Jake Gonzales, Kazuki Mizuta, Karen Leung, and Lillian J. Ratliff from the University of Washington, and it was accepted to the IEEE/RSJ International Conference on Intelligent Robots & Systems in 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "de8f4693-a7dc-4bde-8262-6b77491ed50b",
  "tool_use_result": {
    "query": "\"safe probabilistic planning\" \"conformal risk control\" human-robot arxiv 2603.10392",
    "results": [
      {
        "tool_use_id": "srvtoolu_01MvZBXNGL5tGUgVwSPtR5KG",
        "content": [
          {
            "title": "[2603.10392] Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/abs/2603.10392"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://arxiv.org/html/2603.10392"
          },
          {
            "title": "Publications",
            "url": "https://depts.washington.edu/ctrl/publications/"
          },
          {
            "title": "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control",
            "url": "https://jakeagonzales.github.io/crc-cbf-website/"
          },
          {
            "title": "Heterogeneous Predictor-based Risk-Aware Planning with Conformal Prediction in Dense, Uncertain Environments",
            "url": "https://arxiv.org/html/2507.11920"
          },
          {
            "title": "Conformal Decision Theory: Safe Autonomous Decisions from Imperfect Predictions",
            "url": "https://arxiv.org/html/2310.05921v3"
          },
          {
            "title": "Safe and Stable Neural Network Dynamical Systems for Robot Motion Planning",
            "url": "https://arxiv.org/html/2511.20593"
          },
          {
            "title": "Safe POMDP Online Planning among Dynamic Agents via Adaptive Conformal Prediction",
            "url": "https://arxiv.org/html/2404.15557v1"
          },
          {
            "title": "Safe Task Planning for Language-Instructed Multi-Robot Systems using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368v3"
          },
          {
            "title": "Probabilistically Correct Language-based Multi-Robot Planning using Conformal Prediction",
            "url": "https://arxiv.org/html/2402.15368v4/"
          }
        ]
      },
      "I found the paper you're looking for. Here's what I found:\n\n## Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control (arXiv:2603.10392)\n\n**Overview:**\nThis paper presents a novel probabilistic safe control framework for human-robot interaction that combines control barrier functions (CBFs) with conformal risk control to provide formal safety guarantees while considering complex human behavior.\n\n**Key Technical Contributions:**\n\n1. **Methodology**: The approach uses conformal risk control to quantify and control the prediction errors in CBF safety values and establishes formal guarantees on the probability of constraint satisfaction during interaction.\n\n2. **Adaptive Safety Margins**: The paper introduces an algorithm that dynamically adjusts the safety margins produced by conformal risk control based on the current interaction context.\n\n3. **Implementation**: The practical implementation does not rely on any distributional assumptions or worst-case bounds, and is both computationally efficient for real-time control and theoretically grounded.\n\n**Experimental Results:**\nThrough experiments on human-robot navigation scenarios, the approach significantly reduces collision rates and safety violations as compared to baseline methods while maintaining high success rates in goal-reaching tasks and efficient control.\n\n**Authors and Status:**\nThe paper is authored by Jake Gonzales, Kazuki Mizuta, Karen Leung, and Lillian J. Ratliff from the University of Washington, and it was accepted to the IEEE/RSJ International Conference on Intelligent Robots & Systems in 2025."
    ],
    "durationSeconds": 6.846552787999993
  }
}
```

</details>

---

### Tool result

_source line 43 · 2026-05-14T03:17:26.980Z_

<details><summary>↩ Tool result · `toolu_012ySYDHM49qCtvxKTLznfYy`</summary>

```text
Web search results for query: "LUCCa "local uncertainty conformal calibration" dynamics model robot arxiv"

Links: [{"title":"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration","url":"https://arxiv.org/html/2409.08249v1"},{"title":"[2409.08249] Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration","url":"https://arxiv.org/abs/2409.08249"},{"title":"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration","url":"https://paperreading.club/page?id=251263"},{"title":"Luis F S Marques - University of Michigan - Academia.edu","url":"https://umich.academia.edu/LuisMarques"},{"title":"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups","url":"https://arxiv.org/html/2512.10294"},{"title":"Uncertainty-Aware Online Extrinsic Calibration: A Conformal Prediction Approach","url":"https://arxiv.org/html/2501.06878"},{"title":"[2512.10294] Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups","url":"https://arxiv.org/abs/2512.10294"},{"title":"[2604.27149] ConformaDecompose: Explaining Uncertainty via Calibration Localization","url":"https://arxiv.org/abs/2604.27149"},{"title":"[2501.06878] Uncertainty-Aware Online Extrinsic Calibration: A Conformal Prediction Approach","url":"https://arxiv.org/abs/2501.06878"},{"title":"ConformaDecompose: Explaining Uncertainty via Calibration LocalizationThis is an accepted author version of a paper to appear in the proceedings of the World Explainable AI Conference (Springer). The final authenticated version will be available via Springer.","url":"https://arxiv.org/html/2604.27149"}]

I found the paper you were looking for! Here are the key details:

## LUCCa: Local Uncertainty Conformal Calibration

Local Uncertainty Conformal Calibration (LUCCa) is a conformal prediction-based approach that calibrates the aleatoric uncertainty estimates provided by dynamics models to generate probabilistically-valid prediction regions of the system's state.

### Problem Statement

Robot dynamics approximations can be inaccurate when encountering novel environments, and uncertainty estimates alone are not enough to properly estimate the uncertainty of a model in a novel environment where the actual dynamics can change. Accounting for both epistemic and aleatoric dynamics uncertainty in a theoretically-grounded way remains an open problem.

### Key Features

The method is a probabilistically-valid conformal prediction-based approach that accounts for epistemic uncertainty by calibrating the aleatoric uncertainty estimates provided by dynamics predictors, with calibration performed locally in the state-action space, leading to uncertainty estimates that are useful for planning.

### Applications

The prediction regions of the calibrated model can be chained in an MPC scheme to devise provably safe robot trajectories. The method was validated by constructing probabilistically-safe plans for a double-integrator under significant changes in dynamics.

**arXiv Paper:** 2409.08249 - "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration" (September 2024)


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "7769c281-650f-4819-a574-486473fec55b",
  "tool_use_result": {
    "query": "LUCCa \"local uncertainty conformal calibration\" dynamics model robot arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WozcQzzMtX2Mz8wfpPkj9A",
        "content": [
          {
            "title": "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration",
            "url": "https://arxiv.org/html/2409.08249v1"
          },
          {
            "title": "[2409.08249] Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration",
            "url": "https://arxiv.org/abs/2409.08249"
          },
          {
            "title": "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration",
            "url": "https://paperreading.club/page?id=251263"
          },
          {
            "title": "Luis F S Marques - University of Michigan - Academia.edu",
            "url": "https://umich.academia.edu/LuisMarques"
          },
          {
            "title": "Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups",
            "url": "https://arxiv.org/html/2512.10294"
          },
          {
            "title": "Uncertainty-Aware Online Extrinsic Calibration: A Conformal Prediction Approach",
            "url": "https://arxiv.org/html/2501.06878"
          },
          {
            "title": "[2512.10294] Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups",
            "url": "https://arxiv.org/abs/2512.10294"
          },
          {
            "title": "[2604.27149] ConformaDecompose: Explaining Uncertainty via Calibration Localization",
            "url": "https://arxiv.org/abs/2604.27149"
          },
          {
            "title": "[2501.06878] Uncertainty-Aware Online Extrinsic Calibration: A Conformal Prediction Approach",
            "url": "https://arxiv.org/abs/2501.06878"
          },
          {
            "title": "ConformaDecompose: Explaining Uncertainty via Calibration LocalizationThis is an accepted author version of a paper to appear in the proceedings of the World Explainable AI Conference (Springer). The final authenticated version will be available via Springer.",
            "url": "https://arxiv.org/html/2604.27149"
          }
        ]
      },
      "I found the paper you were looking for! Here are the key details:\n\n## LUCCa: Local Uncertainty Conformal Calibration\n\nLocal Uncertainty Conformal Calibration (LUCCa) is a conformal prediction-based approach that calibrates the aleatoric uncertainty estimates provided by dynamics models to generate probabilistically-valid prediction regions of the system's state.\n\n### Problem Statement\n\nRobot dynamics approximations can be inaccurate when encountering novel environments, and uncertainty estimates alone are not enough to properly estimate the uncertainty of a model in a novel environment where the actual dynamics can change. Accounting for both epistemic and aleatoric dynamics uncertainty in a theoretically-grounded way remains an open problem.\n\n### Key Features\n\nThe method is a probabilistically-valid conformal prediction-based approach that accounts for epistemic uncertainty by calibrating the aleatoric uncertainty estimates provided by dynamics predictors, with calibration performed locally in the state-action space, leading to uncertainty estimates that are useful for planning.\n\n### Applications\n\nThe prediction regions of the calibrated model can be chained in an MPC scheme to devise provably safe robot trajectories. The method was validated by constructing probabilistically-safe plans for a double-integrator under significant changes in dynamics.\n\n**arXiv Paper:** 2409.08249 - \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\" (September 2024)"
    ],
    "durationSeconds": 7.549610096999997
  }
}
```

</details>

---

### Tool result

_source line 44 · 2026-05-14T03:17:28.016Z_

<details><summary>↩ Tool result · `toolu_0153PsTs9kRHvW613QHEY1AM`</summary>

```text
Web search results for query: "CoA-VLA "chain of affordance" vision language action ICCV 2025"

Links: [{"title":"CoA-VLA: Improving Vision-Language-Action Models via ...","url":"https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"},{"title":"Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://chain-of-affordance.github.io/"},{"title":"ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"},{"title":"Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/issues/5"},{"title":"[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/abs/2412.20451"},{"title":"ICCV Poster CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance","url":"https://iccv.thecvf.com/virtual/2025/poster/542"},{"title":"bibtex - ICCV 2025 Open Access Repository","url":"https://openaccess.thecvf.com/ICCV2025?day=2025-10-21"},{"title":"CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance","url":"https://arxiv.org/html/2412.20451v2"},{"title":"[PDF] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance | Semantic Scholar","url":"https://www.semanticscholar.org/paper/CoA-VLA:-Improving-Vision-Language-Action-Models-Li-Zhu/5760cc722b5eabc14487e9c497a78038ab46f37d"},{"title":"(PDF) Improving Vision-Language-Action Models via Chain-of-Affordance","url":"https://www.researchgate.net/publication/387539786_Improving_Vision-Language-Action_Models_via_Chain-of-Affordance"}]

## Search Results for CoA-VLA

I found comprehensive information about the CoA-VLA paper. Here's what the search revealed:

### Overview

CoA-VLA is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion.

### The Four Types of Affordances

The model prompts the system to consider four types of affordances before taking action: (1) object affordance - what object to manipulate and where it is; (2) grasp affordance - the specific object part to grasp; (3) spatial affordance - the optimal space to place the object; and (4) movement affordance - the collision-free path for movement.

### Technical Approach

Each affordance is transformed into two prompting formats: visual affordance and textual affordance, with a novel vision-language co-injection module that integrates this knowledge into the policy network.

### Performance Results

CoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks. Additionally, CoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses and identifying free space.

### Publication

The paper was published at ICCV 2025 by authors including Jinming Li, Yichen Zhu, Zhibin Tang, and others. The preprint is available on arXiv (2412.20451), and a project website is available at chain-of-affordance.github.io.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "c6bd06e1-8aba-4c5e-9dec-41bee238b6e0",
  "tool_use_result": {
    "query": "CoA-VLA \"chain of affordance\" vision language action ICCV 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01P7gd3zi5JbY8rHnxi68yz4",
        "content": [
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via ...",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/papers/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.pdf"
          },
          {
            "title": "Improving Vision-Language-Action Models via Chain-of-Affordance",
            "url": "https://chain-of-affordance.github.io/"
          },
          {
            "title": "ICCV 2025 Open Access Repository",
            "url": "https://openaccess.thecvf.com/content/ICCV2025/html/Li_CoA-VLA_Improving_Vision-Language-Action_Models_via_Visual-Text_Chain-of-Affordance_ICCV_2025_paper.html"
          },
          {
            "title": "Add CoA-VLA (Chain-of-Affordance) · Issue #5 · keon/awesome-physical-ai",
            "url": "https://github.com/keon/awesome-physical-ai/issues/5"
          },
          {
            "title": "[2412.20451] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/abs/2412.20451"
          },
          {
            "title": "ICCV Poster CoA-VLA: Improving Vision-Language-Action Models via Visual-Text Chain-of-Affordance",
            "url": "https://iccv.thecvf.com/virtual/2025/poster/542"
          },
          {
            "title": "bibtex - ICCV 2025 Open Access Repository",
            "url": "https://openaccess.thecvf.com/ICCV2025?day=2025-10-21"
          },
          {
            "title": "CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance",
            "url": "https://arxiv.org/html/2412.20451v2"
          },
          {
            "title": "[PDF] CoA-VLA: Improving Vision-Language-Action Models via Visual-Textual Chain-of-Affordance | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/CoA-VLA:-Improving-Vision-Language-Action-Models-Li-Zhu/5760cc722b5eabc14487e9c497a78038ab46f37d"
          },
          {
            "title": "(PDF) Improving Vision-Language-Action Models via Chain-of-Affordance",
            "url": "https://www.researchgate.net/publication/387539786_Improving_Vision-Language-Action_Models_via_Chain-of-Affordance"
          }
        ]
      },
      "## Search Results for CoA-VLA\n\nI found comprehensive information about the CoA-VLA paper. Here's what the search revealed:\n\n### Overview\n\nCoA-VLA is a novel approach to scaling robot models by incorporating reasoning in the format of sequential robot affordances to facilitate task completion.\n\n### The Four Types of Affordances\n\nThe model prompts the system to consider four types of affordances before taking action: (1) object affordance - what object to manipulate and where it is; (2) grasp affordance - the specific object part to grasp; (3) spatial affordance - the optimal space to place the object; and (4) movement affordance - the collision-free path for movement.\n\n### Technical Approach\n\nEach affordance is transformed into two prompting formats: visual affordance and textual affordance, with a novel vision-language co-injection module that integrates this knowledge into the policy network.\n\n### Performance Results\n\nCoA-VLA outperforms state-of-the-art robot foundation models, including OpenVLA and Octo, on a variety of tasks. Additionally, CoA-VLA exhibits strong generalization capabilities, including recognizing unseen object poses and identifying free space.\n\n### Publication\n\nThe paper was published at ICCV 2025 by authors including Jinming Li, Yichen Zhu, Zhibin Tang, and others. The preprint is available on arXiv (2412.20451), and a project website is available at chain-of-affordance.github.io."
    ],
    "durationSeconds": 7.049812983999996
  }
}
```

</details>

---

### Tool result

_source line 45 · 2026-05-14T03:17:29.863Z_

<details><summary>↩ Tool result · `toolu_015FeMYnYCeyWdM8kej12hDC`</summary>

```text
Web search results for query: "VLA inference-time correction residual policy robot 2025 2026 arxiv"

Links: [{"title":"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning","url":"https://arxiv.org/html/2601.06748v1"},{"title":"Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge","url":"https://arxiv.org/html/2512.06951v1"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178v2"},{"title":"[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/abs/2505.18719"},{"title":"awesome-physical-ai/README.md at main · keon/awesome-physical-ai","url":"https://github.com/keon/awesome-physical-ai/blob/main/README.md"},{"title":"Self-Improving Vision-Language-Action Models with Data ...","url":"https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633"},{"title":"VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning","url":"https://arxiv.org/html/2505.18719v1"},{"title":"[2506.07127] Human-assisted Robotic Policy Refinement via Action Preference Optimization","url":"https://arxiv.org/abs/2506.07127"}]

I found several relevant research papers from the search results. Here are the key findings related to VLA inference-time correction and residual policy robots from 2025-2026:

## Key Papers Found:

1. **On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning** (January 2026)
   This paper proposes a Test-Time Reinforcement Learning framework for VLA (TT-VLA) that performs online inference-time policy fine-tuning efficiently without retraining cycles, preserving SFT/training-time RL priors while closing the loop with dense inference-time reward signals.

2. **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** (ICLR 2026 Submission)
   This paper presents a residual RL method collecting data with frozen VLA and small residual policy. Residual interventions provide high-quality data with recovery behavior. It finally finetunes VLA using SFT and achieves 99% on LIBERO.

3. **Self-Correcting VLA: Online Action Refinement via Sparse World Imagination** (February 2026)
   This framework, called Self-Correcting VLA (SC-VLA), jointly generates actions while predicting sparse future states, enabling fine-grained trajectory refinement via residual reinforcement learning for complex manipulation tasks.

4. **Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering** (March 2026)
   This paper presents VLA-Pilot, a plug-and-play inference-time policy steering method that enables zero-shot generalization of frozen VLA policies across diverse downstream tasks and embodiments, without requiring any additional policy fine-tuning or data collection.

5. **VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning** (May 2025)
   VLA-RL benefits from increased test-time optimization, indicating an early spark of inference scaling laws in robotics, with performance consistently improving with increased test-time computation.

These papers represent the cutting edge of VLA research in 2025-2026, focusing on inference-time adaptation, residual policies, and test-time optimization for robotic manipulation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "a8937c5c-058e-4fff-bec5-361d67018d7c",
  "tool_use_result": {
    "query": "VLA inference-time correction residual policy robot 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VuDbX8yprKTmAb8yrpuL8c",
        "content": [
          {
            "title": "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning",
            "url": "https://arxiv.org/html/2601.06748v1"
          },
          {
            "title": "Task adaptation of Vision-Language-Action model: 1st Place Solution for the 2025 BEHAVIOR Challenge",
            "url": "https://arxiv.org/html/2512.06951v1"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion",
            "url": "https://arxiv.org/html/2511.14178v2"
          },
          {
            "title": "[2505.18719] VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/abs/2505.18719"
          },
          {
            "title": "awesome-physical-ai/README.md at main · keon/awesome-physical-ai",
            "url": "https://github.com/keon/awesome-physical-ai/blob/main/README.md"
          },
          {
            "title": "Self-Improving Vision-Language-Action Models with Data ...",
            "url": "https://wenlixiao.com/self-improve-VLA-PLD/assets/doc/pld-fullpaper.pdf"
          },
          {
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination",
            "url": "https://arxiv.org/html/2602.21633"
          },
          {
            "title": "VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning",
            "url": "https://arxiv.org/html/2505.18719v1"
          },
          {
            "title": "[2506.07127] Human-assisted Robotic Policy Refinement via Action Preference Optimization",
            "url": "https://arxiv.org/abs/2506.07127"
          }
        ]
      },
      "I found several relevant research papers from the search results. Here are the key findings related to VLA inference-time correction and residual policy robots from 2025-2026:\n\n## Key Papers Found:\n\n1. **On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning** (January 2026)\n   This paper proposes a Test-Time Reinforcement Learning framework for VLA (TT-VLA) that performs online inference-time policy fine-tuning efficiently without retraining cycles, preserving SFT/training-time RL priors while closing the loop with dense inference-time reward signals.\n\n2. **Self-Improving Vision-Language-Action Models with Data Generation via Residual RL** (ICLR 2026 Submission)\n   This paper presents a residual RL method collecting data with frozen VLA and small residual policy. Residual interventions provide high-quality data with recovery behavior. It finally finetunes VLA using SFT and achieves 99% on LIBERO.\n\n3. **Self-Correcting VLA: Online Action Refinement via Sparse World Imagination** (February 2026)\n   This framework, called Self-Correcting VLA (SC-VLA), jointly generates actions while predicting sparse future states, enabling fine-grained trajectory refinement via residual reinforcement learning for complex manipulation tasks.\n\n4. **Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering** (March 2026)\n   This paper presents VLA-Pilot, a plug-and-play inference-time policy steering method that enables zero-shot generalization of frozen VLA policies across diverse downstream tasks and embodiments, without requiring any additional policy fine-tuning or data collection.\n\n5. **VLA-RL: Towards Masterful and General Robotic Manipulation with Scalable Reinforcement Learning** (May 2025)\n   VLA-RL benefits from increased test-time optimization, indicating an early spark of inference scaling laws in robotics, with performance consistently improving with increased test-time computation.\n\nThese papers represent the cutting edge of VLA research in 2025-2026, focusing on inference-time adaptation, residual policies, and test-time optimization for robotic manipulation."
    ],
    "durationSeconds": 8.623381589999997
  }
}
```

</details>

---

### Assistant

_source line 46_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I found several new papers that are not in the existing literature map. Let me search for a few more specific papers:

1. Self-Correcting VLA (SC-VLA) - 2602.21633
2. VLA-Pilot - 2511.14178
3. "Confidence Calibration in VLA" - 2507.17383 (already found details)
4. "Lies We Can Trust" - Conformalized Nonholonomic Lie Groups - 2512.10294
5. Let me also search for more on multivariate conformal prediction

Let me do targeted searches.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "0b7c4365-254a-4b5d-95c5-36d284befd44",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXeiVoj8M666AAYT24uJZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 41103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
      },
      "output_tokens": 32,
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

<details open><summary>🔧 Tool call — WebSearch · `toolu_01E9DsbthdAuJpGZkmeVfxwj`</summary>

```json
{
  "query": "\"Self-Correcting VLA\" \"online action refinement\" \"sparse world imagination\" arxiv 2602.21633"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "5ea9bec6-579c-4cf7-8624-33e31e1a0450",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXeiVoj8M666AAYT24uJZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 41103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
      },
      "output_tokens": 32,
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

_source line 48_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01CueU1X6BvLgF3vditdAaWC`</summary>

```json
{
  "query": "VLA-Pilot \"plug-and-play\" \"inference-time\" \"policy steering\" embodied evolutionary diffusion arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "3252954e-f481-4605-914d-94ef86a4cd07",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXeiVoj8M666AAYT24uJZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 41103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
      },
      "output_tokens": 32,
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

_source line 49_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YMzWcTB2gfQWLbvifkm5Ha`</summary>

```json
{
  "query": "\"multivariate conformal prediction\" \"per-coordinate\" OR \"marginal coverage\" OR \"componentwise\" 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "9207b41a-f599-48c9-b64a-4c099f23b11e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXeiVoj8M666AAYT24uJZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 41103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
      },
      "output_tokens": 32,
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

_source line 50_

<details open><summary>🔧 Tool call — WebSearch · `toolu_011VTPXek45NsP8V86cTy1kW`</summary>

```json
{
  "query": "\"Lies We Can Trust\" conformalized nonholonomic Lie groups action uncertainty arxiv 2512"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "fa7d4be1-89f3-4f74-a198-e941744d5eb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXeiVoj8M666AAYT24uJZr",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 5118,
      "cache_read_input_tokens": 41103,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 5118
      },
      "output_tokens": 32,
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

_source line 51 · 2026-05-14T03:17:40.904Z_

<details><summary>↩ Tool result · `toolu_01E9DsbthdAuJpGZkmeVfxwj`</summary>

```text
Web search results for query: ""Self-Correcting VLA" "online action refinement" "sparse world imagination" arxiv 2602.21633"

Links: [{"title":"[2602.21633] Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/abs/2602.21633"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination","url":"https://arxiv.org/html/2602.21633.pdf"},{"title":"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS","url":"https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"},{"title":"GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub","url":"https://github.com/Kisaragi0/SC-VLA"}]

I found the paper! Here are the key details:

Self-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.

**Main Problem Addressed:**
Standard vision-language-action models rely on fitting statistical data priors, limiting their robust understanding of physical dynamics. Reinforcement learning enhances physical grounding through exploration but typically relies on external reward signals isolated from the agent's internal states. World action models integrate imagination and control for predictive planning, yet they rely on implicit context modeling and lack explicit mechanisms for self-improvement.

**Key Technical Components:**
1. Sparse world imagination uses auxiliary predictive heads to forecast current task progress and future trajectory trends, constraining the policy to encode short-term physical evolution.
2. An online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.

**Results:**
SC-VLA achieves state-of-the-art performance with 16% fewer steps, a 9% higher success rate than best-performing baselines, and a 14% gain in real-world experiments.

The paper was published on February 25, 2026, and demonstrates superior performance on ManiSkill and real-world ARX5 benchmarks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "ec4e2592-d6fa-4cfc-82d1-9f5b3789ae41",
  "tool_use_result": {
    "query": "\"Self-Correcting VLA\" \"online action refinement\" \"sparse world imagination\" arxiv 2602.21633",
    "results": [
      {
        "tool_use_id": "srvtoolu_01X7JhXJkUWgYotvBknjEJSZ",
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
            "title": "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination - ADS",
            "url": "https://ui.adsabs.harvard.edu/abs/2026arXiv260221633L/abstract"
          },
          {
            "title": "GitHub - Kisaragi0/SC-VLA: Self-CorrectingVLA:OnlineActionRefinementviaSparseWorldImagination · GitHub",
            "url": "https://github.com/Kisaragi0/SC-VLA"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\nSelf-Correcting VLA (SC-VLA) achieves self-improvement by intrinsically guiding action refinement through sparse imagination.\n\n**Main Problem Addressed:**\nStandard vision-language-action models rely on fitting statistical data priors, limiting their robust understanding of physical dynamics. Reinforcement learning enhances physical grounding through exploration but typically relies on external reward signals isolated from the agent's internal states. World action models integrate imagination and control for predictive planning, yet they rely on implicit context modeling and lack explicit mechanisms for self-improvement.\n\n**Key Technical Components:**\n1. Sparse world imagination uses auxiliary predictive heads to forecast current task progress and future trajectory trends, constraining the policy to encode short-term physical evolution.\n2. An online action refinement module reshapes progress-dependent dense rewards, adjusting trajectory orientation based on predicted sparse future states.\n\n**Results:**\nSC-VLA achieves state-of-the-art performance with 16% fewer steps, a 9% higher success rate than best-performing baselines, and a 14% gain in real-world experiments.\n\nThe paper was published on February 25, 2026, and demonstrates superior performance on ManiSkill and real-world ARX5 benchmarks."
    ],
    "durationSeconds": 4.984766864999997
  }
}
```

</details>

---

### Tool result

_source line 52 · 2026-05-14T03:17:44.345Z_

<details><summary>↩ Tool result · `toolu_01CueU1X6BvLgF3vditdAaWC`</summary>

```text
Web search results for query: "VLA-Pilot "plug-and-play" "inference-time" "policy steering" embodied evolutionary diffusion arxiv"

Links: [{"title":"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/html/2511.14178"},{"title":"[2511.14178] Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion","url":"https://arxiv.org/abs/2511.14178"},{"title":"VLS: Steering Pretrained Robot Policies via Vision–Language Models","url":"https://arxiv.org/html/2602.03973v1"},{"title":"Paper page - EvoVLA: Self-Evolving Vision-Language-Action Model","url":"https://huggingface.co/papers/2511.16166"},{"title":"Paper page - Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach","url":"https://huggingface.co/papers/2512.02834"},{"title":"VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots","url":"https://arxiv.org/html/2512.24673"},{"title":"Inference-Time Policy Steering Through Human Interactions | Request PDF","url":"https://www.researchgate.net/publication/395222028_Inference-Time_Policy_Steering_Through_Human_Interactions"},{"title":"FASTER: Rethinking Real-Time Flow VLAs","url":"https://arxiv.org/html/2603.19199"},{"title":"Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments","url":"https://arxiv.org/html/2602.09430"},{"title":"Mechanistic Interpretability for Steering Vision-Language-Action Models","url":"https://arxiv.org/html/2509.00328v1"}]

I found the paper! Here's what the search results reveal about VLA-Pilot:

## Overview

VLA-Pilot is a plug-and-play inference-time policy steering method that enables zero-shot generalization of frozen VLA policies across diverse downstream tasks and embodiments, without requiring any additional policy fine-tuning or data collection.

## Key Approach

The core idea is to leverage Multimodal Large Language Models (MLLMs) as open-world verifiers to enhance generalization, and to employ an Evolutionary Diffusion process as an action optimizer to improve task alignment.

VLA-Pilot first employs an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs, which removes the need for training task-specific verifiers and significantly improves generalization to out-of-distribution tasks.

## Core Components

VLA-Pilot introduces a novel Evolutionary Diffusion algorithm to optimize action proposals sampled from the pre-trained VLA policies.

## Experimental Results

Extensive experiments were conducted across six real-world manipulation tasks and two distinct robotic embodiments. VLA-Pilot achieves performance comparable to supervised fine-tuning approaches. Additionally, VLA-Pilot achieves zero-shot generalization on the Franka robot, maintaining consistent task performance across four single-arm tasks.

The paper was published on arXiv as paper 2511.14178 in November 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "d6834621-0839-4495-abc2-e4c28a77242c",
  "tool_use_result": {
    "query": "VLA-Pilot \"plug-and-play\" \"inference-time\" \"policy steering\" embodied evolutionary diffusion arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01F3ZbLzV3J6CmWxJ8BsQHW1",
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
            "title": "Paper page - EvoVLA: Self-Evolving Vision-Language-Action Model",
            "url": "https://huggingface.co/papers/2511.16166"
          },
          {
            "title": "Paper page - Steering Vision-Language-Action Models as Anti-Exploration: A Test-Time Scaling Approach",
            "url": "https://huggingface.co/papers/2512.02834"
          },
          {
            "title": "VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots",
            "url": "https://arxiv.org/html/2512.24673"
          },
          {
            "title": "Inference-Time Policy Steering Through Human Interactions | Request PDF",
            "url": "https://www.researchgate.net/publication/395222028_Inference-Time_Policy_Steering_Through_Human_Interactions"
          },
          {
            "title": "FASTER: Rethinking Real-Time Flow VLAs",
            "url": "https://arxiv.org/html/2603.19199"
          },
          {
            "title": "Sci-VLA: Agentic VLA Inference Plugin for Long-Horizon Tasks in Scientific Experiments",
            "url": "https://arxiv.org/html/2602.09430"
          },
          {
            "title": "Mechanistic Interpretability for Steering Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2509.00328v1"
          }
        ]
      },
      "I found the paper! Here's what the search results reveal about VLA-Pilot:\n\n## Overview\n\nVLA-Pilot is a plug-and-play inference-time policy steering method that enables zero-shot generalization of frozen VLA policies across diverse downstream tasks and embodiments, without requiring any additional policy fine-tuning or data collection.\n\n## Key Approach\n\nThe core idea is to leverage Multimodal Large Language Models (MLLMs) as open-world verifiers to enhance generalization, and to employ an Evolutionary Diffusion process as an action optimizer to improve task alignment.\n\nVLA-Pilot first employs an Embodied Policy Steering Chain-of-Thought (EPS-CoT) module to infer steering objectives reward using the open-world reasoning capabilities of MLLMs, which removes the need for training task-specific verifiers and significantly improves generalization to out-of-distribution tasks.\n\n## Core Components\n\nVLA-Pilot introduces a novel Evolutionary Diffusion algorithm to optimize action proposals sampled from the pre-trained VLA policies.\n\n## Experimental Results\n\nExtensive experiments were conducted across six real-world manipulation tasks and two distinct robotic embodiments. VLA-Pilot achieves performance comparable to supervised fine-tuning approaches. Additionally, VLA-Pilot achieves zero-shot generalization on the Franka robot, maintaining consistent task performance across four single-arm tasks.\n\nThe paper was published on arXiv as paper 2511.14178 in November 2025."
    ],
    "durationSeconds": 7.490530865000008
  }
}
```

</details>

---

### Tool result

_source line 53 · 2026-05-14T03:17:44.810Z_

<details><summary>↩ Tool result · `toolu_011VTPXek45NsP8V86cTy1kW`</summary>

```text
Web search results for query: ""Lies We Can Trust" conformalized nonholonomic Lie groups action uncertainty arxiv 2512"

Links: [{"title":"[2512.10294] Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups","url":"https://arxiv.org/abs/2512.10294"},{"title":"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups","url":"https://arxiv.org/html/2512.10294"},{"title":"Search | arXiv e-print repository","url":"https://arxiv.org/search/cs?searchtype=author&query=Berenson,+D"},{"title":"[2604.04962] Geometric Integrators for Nonholonomic Systems on Lie Groups","url":"https://arxiv.org/abs/2604.04962"},{"title":"Non-smooth trajectory tracking and its corresponding path in the plane. | Download Scientific Diagram","url":"https://www.researchgate.net/figure/Non-smooth-trajectory-tracking-and-its-corresponding-path-in-the-plane_fig4_318030416"},{"title":"Representations of Lie groups","url":"https://arxiv.org/html/2401.01446v2"},{"title":"(PDF) Logarithmic control, trajectory tracking, and formation for nonholonomic vehicles on Lie group SE(2)","url":"https://www.researchgate.net/publication/318030416_Logarithmic_control_trajectory_tracking_and_formation_for_nonholonomic_vehicles_on_Lie_group_SE2"},{"title":"DISCOVERING LIE GROUPS WITH FLOW MATCHING","url":"https://arxiv.org/pdf/2512.20043"},{"title":"Lie Group Symmetry Discovery and Enforcement Using Vector FieldsThis work is an extension of Symmetry Discovery Beyond Affine Transformations []. \\fundingThis research was supported in part by the NSF under Grants 2212325 [K.M.], CIF-2212327 [A.M.], and CIF-2338855 [A.M.].","url":"https://arxiv.org/html/2505.08219v1"},{"title":"arXiv:0901.4076v2 [math.HO] 27 Oct 2009","url":"https://arxiv.org/pdf/0901.4076"}]

I found the paper! Here are the key details:

**"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups"**

**ArXiv:** 2512.10294

**Main Contribution:**
The paper proposes Conformal Lie-group Action Prediction Sets (CLAPS), a symmetry-aware conformal prediction-based algorithm that constructs, for a given action, a set guaranteed to contain the resulting system configuration at a user-defined probability.

**Key Features:**
- The assurance holds under both aleatoric and epistemic uncertainty, non-asymptotically, and does not require strong assumptions about the true system dynamics, the uncertainty sources, or the quality of the approximate dynamics model.

- While current conformal methods treat robots as Euclidean points, many systems have non-Euclidean configurations, and this work rigorously analyzes configuration errors using Lie groups, extending previous Euclidean Space theoretical guarantees to SE(2).

- CLAPS can be applied as a post-hoc calibration layer on top of Lie-algebraic Gaussian uncertainty estimators, turning approximate covariances into provably calibrated ones and producing regions that are smaller than a Euclidean baseline while still containing the true configuration at the user-defined probability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "c6f19bff-79c4-4a21-afa9-476013774433",
  "tool_use_result": {
    "query": "\"Lies We Can Trust\" conformalized nonholonomic Lie groups action uncertainty arxiv 2512",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VQdet9FbDdoTvrgQ2YAkS8",
        "content": [
          {
            "title": "[2512.10294] Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups",
            "url": "https://arxiv.org/abs/2512.10294"
          },
          {
            "title": "Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups",
            "url": "https://arxiv.org/html/2512.10294"
          },
          {
            "title": "Search | arXiv e-print repository",
            "url": "https://arxiv.org/search/cs?searchtype=author&query=Berenson,+D"
          },
          {
            "title": "[2604.04962] Geometric Integrators for Nonholonomic Systems on Lie Groups",
            "url": "https://arxiv.org/abs/2604.04962"
          },
          {
            "title": "Non-smooth trajectory tracking and its corresponding path in the plane. | Download Scientific Diagram",
            "url": "https://www.researchgate.net/figure/Non-smooth-trajectory-tracking-and-its-corresponding-path-in-the-plane_fig4_318030416"
          },
          {
            "title": "Representations of Lie groups",
            "url": "https://arxiv.org/html/2401.01446v2"
          },
          {
            "title": "(PDF) Logarithmic control, trajectory tracking, and formation for nonholonomic vehicles on Lie group SE(2)",
            "url": "https://www.researchgate.net/publication/318030416_Logarithmic_control_trajectory_tracking_and_formation_for_nonholonomic_vehicles_on_Lie_group_SE2"
          },
          {
            "title": "DISCOVERING LIE GROUPS WITH FLOW MATCHING",
            "url": "https://arxiv.org/pdf/2512.20043"
          },
          {
            "title": "Lie Group Symmetry Discovery and Enforcement Using Vector FieldsThis work is an extension of Symmetry Discovery Beyond Affine Transformations []. \\fundingThis research was supported in part by the NSF under Grants 2212325 [K.M.], CIF-2212327 [A.M.], and CIF-2338855 [A.M.].",
            "url": "https://arxiv.org/html/2505.08219v1"
          },
          {
            "title": "arXiv:0901.4076v2 [math.HO] 27 Oct 2009",
            "url": "https://arxiv.org/pdf/0901.4076"
          }
        ]
      },
      "I found the paper! Here are the key details:\n\n**\"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"**\n\n**ArXiv:** 2512.10294\n\n**Main Contribution:**\nThe paper proposes Conformal Lie-group Action Prediction Sets (CLAPS), a symmetry-aware conformal prediction-based algorithm that constructs, for a given action, a set guaranteed to contain the resulting system configuration at a user-defined probability.\n\n**Key Features:**\n- The assurance holds under both aleatoric and epistemic uncertainty, non-asymptotically, and does not require strong assumptions about the true system dynamics, the uncertainty sources, or the quality of the approximate dynamics model.\n\n- While current conformal methods treat robots as Euclidean points, many systems have non-Euclidean configurations, and this work rigorously analyzes configuration errors using Lie groups, extending previous Euclidean Space theoretical guarantees to SE(2).\n\n- CLAPS can be applied as a post-hoc calibration layer on top of Lie-algebraic Gaussian uncertainty estimators, turning approximate covariances into provably calibrated ones and producing regions that are smaller than a Euclidean baseline while still containing the true configuration at the user-defined probability."
    ],
    "durationSeconds": 6.609524974999993
  }
}
```

</details>

---

### Tool result

_source line 54 · 2026-05-14T03:17:47.074Z_

<details><summary>↩ Tool result · `toolu_01YMzWcTB2gfQWLbvifkm5Ha`</summary>

```text
Web search results for query: ""multivariate conformal prediction" "per-coordinate" OR "marginal coverage" OR "componentwise" 2025 2026 arxiv"

Links: [{"title":"[2507.20941] Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/abs/2507.20941"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/pdf/2507.20941"},{"title":"Multivariate Standardized Residuals for Conformal Prediction","url":"https://arxiv.org/html/2507.20941"},{"title":"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization","url":"https://arxiv.org/html/2512.15383"},{"title":"Conditional Coverage Diagnostics for Conformal Prediction","url":"https://arxiv.org/html/2512.11779v1"},{"title":"[2605.12341] Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting","url":"https://arxiv.org/abs/2605.12341"},{"title":"Interpretable Multivariate Conformal Prediction with Fast ...","url":"https://arxiv.org/pdf/2512.15383"},{"title":"[2603.27189] Conformal Prediction Assessment: A Framework for Conditional Coverage Evaluation and Selection","url":"https://arxiv.org/abs/2603.27189"},{"title":"CONTRA: Conformal Prediction Region via Normalizing Flow Transformation","url":"https://arxiv.org/html/2605.08561"},{"title":"Multivariate Conformal Prediction using Optimal Transport","url":"https://arxiv.org/html/2502.03609v1"}]

I found several relevant papers on multivariate conformal prediction from 2025-2026 arxiv. Here are the key results:

## Recent Multivariate Conformal Prediction Papers (2025-2026)

**1. Multivariate Standardized Residuals for Conformal Prediction**
Submitted July 28, 2025 (latest version May 7, 2026), authors Sacha Braun, Eugène Berta, Michael I. Jordan, Francis Bach. While split conformal prediction guarantees marginal coverage, approaching the stronger property of conditional coverage is essential for reliable uncertainty quantification. The paper proposes a natural extension of normalization to the multivariate setting, effectively whitening the residuals to decouple output correlations and standardize local variance.

**2. Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization**
Dated December 17, 2025. This work develops a transductive conformal prediction method that uses a similar standardization idea but avoids wasteful data splitting by reusing the entire calibration data to estimate the scaling parameters, all while retaining finite-sample guarantees and manageable computational costs. The simplest approach to obtain hyper-rectangular prediction sets is to apply univariate conformal prediction to each output and then take the Cartesian product of the resulting intervals, but a conservative Bonferroni adjustment is often too conservative.

**3. Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting**
This framework extends conformal prediction to vector-valued score functions with multiple simultaneous calibration variables. Submitted May 12, 2026.

**4. Multivariate Conformal Prediction using Optimal Transport**
February 5, 2025. This work extends conformal prediction techniques to multivariate score functions by leveraging optimal transport ordering, which offers a principled way to define and compute a higher-dimensional quantile and cumulative distribution function, resulting in distribution-free uncertainty sets that capture the joint behavior of multivariate predictions.

**5. Conditional Coverage Diagnostics for Conformal Prediction**
December 12, 2025. Conformal prediction's simplicity hides an important drawback: it only guarantees marginal coverage, which means that the constructed prediction set contains the true outcome with probability 1-α on average across the population.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "eabf791d-7ae3-4940-bdb2-2a05f104ff3b",
  "tool_use_result": {
    "query": "\"multivariate conformal prediction\" \"per-coordinate\" OR \"marginal coverage\" OR \"componentwise\" 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PiEbm74yRiP9JaS69p96f8",
        "content": [
          {
            "title": "[2507.20941] Multivariate Standardized Residuals for Conformal Prediction",
            "url": "https://arxiv.org/abs/2507.20941"
          },
          {
            "title": "Multivariate Conformal Prediction via Conformalized Gaussian Scoring",
            "url": "https://arxiv.org/pdf/2507.20941"
          },
          {
            "title": "Multivariate Standardized Residuals for Conformal Prediction",
            "url": "https://arxiv.org/html/2507.20941"
          },
          {
            "title": "Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization",
            "url": "https://arxiv.org/html/2512.15383"
          },
          {
            "title": "Conditional Coverage Diagnostics for Conformal Prediction",
            "url": "https://arxiv.org/html/2512.11779v1"
          },
          {
            "title": "[2605.12341] Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting",
            "url": "https://arxiv.org/abs/2605.12341"
          },
          {
            "title": "Interpretable Multivariate Conformal Prediction with Fast ...",
            "url": "https://arxiv.org/pdf/2512.15383"
          },
          {
            "title": "[2603.27189] Conformal Prediction Assessment: A Framework for Conditional Coverage Evaluation and Selection",
            "url": "https://arxiv.org/abs/2603.27189"
          },
          {
            "title": "CONTRA: Conformal Prediction Region via Normalizing Flow Transformation",
            "url": "https://arxiv.org/html/2605.08561"
          },
          {
            "title": "Multivariate Conformal Prediction using Optimal Transport",
            "url": "https://arxiv.org/html/2502.03609v1"
          }
        ]
      },
      "I found several relevant papers on multivariate conformal prediction from 2025-2026 arxiv. Here are the key results:\n\n## Recent Multivariate Conformal Prediction Papers (2025-2026)\n\n**1. Multivariate Standardized Residuals for Conformal Prediction**\nSubmitted July 28, 2025 (latest version May 7, 2026), authors Sacha Braun, Eugène Berta, Michael I. Jordan, Francis Bach. While split conformal prediction guarantees marginal coverage, approaching the stronger property of conditional coverage is essential for reliable uncertainty quantification. The paper proposes a natural extension of normalization to the multivariate setting, effectively whitening the residuals to decouple output correlations and standardize local variance.\n\n**2. Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization**\nDated December 17, 2025. This work develops a transductive conformal prediction method that uses a similar standardization idea but avoids wasteful data splitting by reusing the entire calibration data to estimate the scaling parameters, all while retaining finite-sample guarantees and manageable computational costs. The simplest approach to obtain hyper-rectangular prediction sets is to apply univariate conformal prediction to each output and then take the Cartesian product of the resulting intervals, but a conservative Bonferroni adjustment is often too conservative.\n\n**3. Multi-Variable Conformal Prediction: Optimizing Prediction Sets without Data Splitting**\nThis framework extends conformal prediction to vector-valued score functions with multiple simultaneous calibration variables. Submitted May 12, 2026.\n\n**4. Multivariate Conformal Prediction using Optimal Transport**\nFebruary 5, 2025. This work extends conformal prediction techniques to multivariate score functions by leveraging optimal transport ordering, which offers a principled way to define and compute a higher-dimensional quantile and cumulative distribution function, resulting in distribution-free uncertainty sets that capture the joint behavior of multivariate predictions.\n\n**5. Conditional Coverage Diagnostics for Conformal Prediction**\nDecember 12, 2025. Conformal prediction's simplicity hides an important drawback: it only guarantees marginal coverage, which means that the constructed prediction set contains the true outcome with probability 1-α on average across the population."
    ],
    "durationSeconds": 9.21463740800001
  }
}
```

</details>

---

### Assistant

_source line 55_

<details><summary>Logged reasoning block</summary>

```text
I found several more papers. Let me also search for a few more specific topics:
1. The "Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization" paper - this is very relevant since it's about per-coordinate conformal prediction
2. "Multi-Variable Conformal Prediction" (2605.12341) - very recent
3. "Multivariate Conformal Prediction using Optimal Transport" (2502.03609)
4. Let me also check for "conformal prediction diffusion model" or "flow matching uncertainty"

Let me also look for a few more VLA papers that might be relevant.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "685a8723-a61a-4f8c-8d81-7d027548fab9",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147w5bJwBxxEwq2fjnX7gRC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 3017,
      "cache_read_input_tokens": 46221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3017
      },
      "output_tokens": 10,
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

_source line 56_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018kZwjx82f7QEziwLNpFvkz`</summary>

```json
{
  "query": "\"interpretable multivariate conformal prediction\" \"fast transductive standardization\" arxiv 2512.15383"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "d165e256-bd9b-4645-81c2-81f46695aa5e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147w5bJwBxxEwq2fjnX7gRC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 3017,
      "cache_read_input_tokens": 46221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3017
      },
      "output_tokens": 10,
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

_source line 57_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FqVDAEYYoW7f9T9ksyuEMs`</summary>

```json
{
  "query": "\"conformal prediction\" \"flow matching\" OR \"diffusion model\" uncertainty quantification 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "7aabbab3-359c-4e7f-98c0-b600370c8a22",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147w5bJwBxxEwq2fjnX7gRC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 3017,
      "cache_read_input_tokens": 46221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3017
      },
      "output_tokens": 10,
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

_source line 58_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LL97Nh3eWhxT7Kg5WF2SPj`</summary>

```json
{
  "query": "VLA uncertainty estimation failure detection robot manipulation 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "9a885bc5-b90b-4d5e-bf50-e77ec5e85b24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0147w5bJwBxxEwq2fjnX7gRC",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 967,
      "cache_creation_input_tokens": 3017,
      "cache_read_input_tokens": 46221,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3017
      },
      "output_tokens": 10,
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

_source line 59 · 2026-05-14T03:18:00.420Z_

<details><summary>↩ Tool result · `toolu_018kZwjx82f7QEziwLNpFvkz`</summary>

```text
Web search results for query: ""interpretable multivariate conformal prediction" "fast transductive standardization" arxiv 2512.15383"

Links: [{"title":"[2512.15383] Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization","url":"https://arxiv.org/abs/2512.15383"},{"title":"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization","url":"https://arxiv.org/html/2512.15383v1"},{"title":"(PDF) Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization","url":"https://www.researchgate.net/publication/398805792_Interpretable_Multivariate_Conformal_Prediction_with_Fast_Transductive_Standardization"},{"title":"Interpretable Multivariate Conformal Prediction with Fast ...","url":"https://arxiv.org/pdf/2512.15383"},{"title":"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/2512.15383"},{"title":"[Literature Review] Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization","url":"https://www.themoonlight.io/en/review/interpretable-multivariate-conformal-prediction-with-fast-transductive-standardization"},{"title":"Statistics Papers on X: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization. https://t.co/RRMJOnBhzD\" / X","url":"https://x.com/StatsPapers/status/2001663595994636534"},{"title":"GitHub - ElSacho/Multivariate_Standardized_Residuals: Repository for the paper \"Multivariate Standardized Residuals for Conformal Prediction\" · GitHub","url":"https://github.com/ElSacho/Multivariate_Standardized_Residuals"},{"title":"Multivariate Conformal Prediction via Conformalized Gaussian Scoring","url":"https://arxiv.org/html/2507.20941v1"},{"title":"Volume-Sorted Prediction Set: Efficient Conformal Prediction for Multi-Target Regression","url":"https://arxiv.org/html/2503.02205v1"}]

I found the research paper you're looking for. Here are the key details:

**Paper:** Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization (arXiv 2512.15383)

**Authors:** Yunjie Fan and one other author (the co-author is Matteo Sesia from the University of Southern California)

**Publication Date:** December 17, 2025

**Main Contribution:** The paper proposes a conformal prediction method for constructing tight simultaneous prediction intervals for multiple, potentially related, numerical outputs given a single input. This method can be combined with any multi-target regression model and guarantees finite-sample coverage.

**Key Innovation:** The core idea is a novel coordinate-wise standardization procedure that makes residuals across output dimensions directly comparable, estimating suitable scaling parameters using the calibration data themselves. This does not require modeling of cross-output dependence nor auxiliary sample splitting.

**Performance:** Experiments on simulated and real data demonstrate this method can produce tighter prediction intervals than existing baselines while maintaining valid simultaneous coverage.

The paper is available on arXiv and can be accessed through the direct link https://arxiv.org/abs/2512.15383.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "eccfce9a-37a7-4f5c-a3ca-e139274570c3",
  "tool_use_result": {
    "query": "\"interpretable multivariate conformal prediction\" \"fast transductive standardization\" arxiv 2512.15383",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QPjP5CXfrfbKovE8SZRENf",
        "content": [
          {
            "title": "[2512.15383] Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization",
            "url": "https://arxiv.org/abs/2512.15383"
          },
          {
            "title": "Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization",
            "url": "https://arxiv.org/html/2512.15383v1"
          },
          {
            "title": "(PDF) Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization",
            "url": "https://www.researchgate.net/publication/398805792_Interpretable_Multivariate_Conformal_Prediction_with_Fast_Transductive_Standardization"
          },
          {
            "title": "Interpretable Multivariate Conformal Prediction with Fast ...",
            "url": "https://arxiv.org/pdf/2512.15383"
          },
          {
            "title": "Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/2512.15383"
          },
          {
            "title": "[Literature Review] Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization",
            "url": "https://www.themoonlight.io/en/review/interpretable-multivariate-conformal-prediction-with-fast-transductive-standardization"
          },
          {
            "title": "Statistics Papers on X: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization. https://t.co/RRMJOnBhzD\" / X",
            "url": "https://x.com/StatsPapers/status/2001663595994636534"
          },
          {
            "title": "GitHub - ElSacho/Multivariate_Standardized_Residuals: Repository for the paper \"Multivariate Standardized Residuals for Conformal Prediction\" · GitHub",
            "url": "https://github.com/ElSacho/Multivariate_Standardized_Residuals"
          },
          {
            "title": "Multivariate Conformal Prediction via Conformalized Gaussian Scoring",
            "url": "https://arxiv.org/html/2507.20941v1"
          },
          {
            "title": "Volume-Sorted Prediction Set: Efficient Conformal Prediction for Multi-Target Regression",
            "url": "https://arxiv.org/html/2503.02205v1"
          }
        ]
      },
      "I found the research paper you're looking for. Here are the key details:\n\n**Paper:** Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization (arXiv 2512.15383)\n\n**Authors:** Yunjie Fan and one other author (the co-author is Matteo Sesia from the University of Southern California)\n\n**Publication Date:** December 17, 2025\n\n**Main Contribution:** The paper proposes a conformal prediction method for constructing tight simultaneous prediction intervals for multiple, potentially related, numerical outputs given a single input. This method can be combined with any multi-target regression model and guarantees finite-sample coverage.\n\n**Key Innovation:** The core idea is a novel coordinate-wise standardization procedure that makes residuals across output dimensions directly comparable, estimating suitable scaling parameters using the calibration data themselves. This does not require modeling of cross-output dependence nor auxiliary sample splitting.\n\n**Performance:** Experiments on simulated and real data demonstrate this method can produce tighter prediction intervals than existing baselines while maintaining valid simultaneous coverage.\n\nThe paper is available on arXiv and can be accessed through the direct link https://arxiv.org/abs/2512.15383."
    ],
    "durationSeconds": 5.9452270500000015
  }
}
```

</details>

---

### Tool result

_source line 60 · 2026-05-14T03:18:02.606Z_

<details><summary>↩ Tool result · `toolu_01FqVDAEYYoW7f9T9ksyuEMs`</summary>

```text
Web search results for query: ""conformal prediction" "flow matching" OR "diffusion model" uncertainty quantification 2025 2026"

Links: [{"title":"Conformal Prediction for Uncertainty-Aware Planning with ...","url":"https://openreview.net/pdf?id=VeO03T59Sh"},{"title":"Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model | OpenReview","url":"https://openreview.net/forum?id=VeO03T59Sh"},{"title":"Model Uncertainty Quantification by Conformal Prediction in Continual Learning | OpenReview","url":"https://openreview.net/forum?id=PHhW4PEm2D"},{"title":"ICML Poster From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control","url":"https://icml.cc/virtual/2025/poster/44969"},{"title":"Flow-based Conformal Prediction for Multi-dimensional Time Series | OpenReview","url":"https://openreview.net/forum?id=z2hzMjbHCT"},{"title":"Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/fe318a2b6c699808019a456b706cd845-Abstract-Conference.html"},{"title":"NeurIPS Poster Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model","url":"https://neurips.cc/virtual/2023/poster/71449"},{"title":"Conformal Prediction: A Data Perspective | ACM Computing Surveys","url":"https://dl.acm.org/doi/10.1145/3736575"},{"title":"ConformaSegment: A Conformal Prediction-Based, Uncertainty-Aware, and Model-Agnostic Explainability Framework for Time-Series Forecasting | Springer Nature Link (formerly SpringerLink)","url":"https://link.springer.com/chapter/10.1007/978-3-032-08330-2_11"},{"title":"PlanCP - Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model","url":"https://msl.stanford.edu/projects/plancp"}]

Here are the search results for your query about conformal prediction, flow matching/diffusion models, and uncertainty quantification from 2025-2026:

## Recent Research Highlights

### Conformal Prediction with Diffusion Models

SafeDiffCon introduces uncertainty quantile as model uncertainty quantification to achieve optimal control under safety constraints through both post-training and inference phases. The approach post-trains a pre-trained diffusion model to generate control sequences that better satisfy safety constraints while achieving improved control objectives via a reweighted diffusion loss, which incorporates the uncertainty quantile estimated using conformal prediction. This work was presented at ICML 2025.

### Flow-Based Conformal Prediction for Time Series

A novel conformal prediction method for time series using flow with classifier-free guidance has been proposed (November 2025). The method provides theoretical guarantees by establishing exact non-asymptotic marginal coverage and finite-sample bound on conditional coverage.

### Conformal Prediction in Continual Learning

A conformal prediction based method for model uncertainty quantification in continual learning (CPCL) has been proposed, with theoretical proof of asymptotic coverage guarantee (June 2025).

### Time-Series Explainability Framework

ConformaSegment is a model-agnostic explainability framework that enhances time-series interpretability by identifying critical segments while quantifying prediction uncertainty through conformal prediction to generate reliable prediction intervals with guaranteed coverage rates (2026 publication).

These recent works demonstrate the growing integration of conformal prediction techniques with modern generative models like diffusion and flow models for improved uncertainty quantification across various domains.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "d15f41da-3db6-4be0-b3b2-e27720cc68e9",
  "tool_use_result": {
    "query": "\"conformal prediction\" \"flow matching\" OR \"diffusion model\" uncertainty quantification 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RQ6VpL8yC8kFyWvgcGRLmy",
        "content": [
          {
            "title": "Conformal Prediction for Uncertainty-Aware Planning with ...",
            "url": "https://openreview.net/pdf?id=VeO03T59Sh"
          },
          {
            "title": "Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model | OpenReview",
            "url": "https://openreview.net/forum?id=VeO03T59Sh"
          },
          {
            "title": "Model Uncertainty Quantification by Conformal Prediction in Continual Learning | OpenReview",
            "url": "https://openreview.net/forum?id=PHhW4PEm2D"
          },
          {
            "title": "ICML Poster From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control",
            "url": "https://icml.cc/virtual/2025/poster/44969"
          },
          {
            "title": "Flow-based Conformal Prediction for Multi-dimensional Time Series | OpenReview",
            "url": "https://openreview.net/forum?id=z2hzMjbHCT"
          },
          {
            "title": "Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2023/hash/fe318a2b6c699808019a456b706cd845-Abstract-Conference.html"
          },
          {
            "title": "NeurIPS Poster Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model",
            "url": "https://neurips.cc/virtual/2023/poster/71449"
          },
          {
            "title": "Conformal Prediction: A Data Perspective | ACM Computing Surveys",
            "url": "https://dl.acm.org/doi/10.1145/3736575"
          },
          {
            "title": "ConformaSegment: A Conformal Prediction-Based, Uncertainty-Aware, and Model-Agnostic Explainability Framework for Time-Series Forecasting | Springer Nature Link (formerly SpringerLink)",
            "url": "https://link.springer.com/chapter/10.1007/978-3-032-08330-2_11"
          },
          {
            "title": "PlanCP - Conformal Prediction for Uncertainty-Aware Planning with Diffusion Dynamics Model",
            "url": "https://msl.stanford.edu/projects/plancp"
          }
        ]
      },
      "Here are the search results for your query about conformal prediction, flow matching/diffusion models, and uncertainty quantification from 2025-2026:\n\n## Recent Research Highlights\n\n### Conformal Prediction with Diffusion Models\n\nSafeDiffCon introduces uncertainty quantile as model uncertainty quantification to achieve optimal control under safety constraints through both post-training and inference phases. The approach post-trains a pre-trained diffusion model to generate control sequences that better satisfy safety constraints while achieving improved control objectives via a reweighted diffusion loss, which incorporates the uncertainty quantile estimated using conformal prediction. This work was presented at ICML 2025.\n\n### Flow-Based Conformal Prediction for Time Series\n\nA novel conformal prediction method for time series using flow with classifier-free guidance has been proposed (November 2025). The method provides theoretical guarantees by establishing exact non-asymptotic marginal coverage and finite-sample bound on conditional coverage.\n\n### Conformal Prediction in Continual Learning\n\nA conformal prediction based method for model uncertainty quantification in continual learning (CPCL) has been proposed, with theoretical proof of asymptotic coverage guarantee (June 2025).\n\n### Time-Series Explainability Framework\n\nConformaSegment is a model-agnostic explainability framework that enhances time-series interpretability by identifying critical segments while quantifying prediction uncertainty through conformal prediction to generate reliable prediction intervals with guaranteed coverage rates (2026 publication).\n\nThese recent works demonstrate the growing integration of conformal prediction techniques with modern generative models like diffusion and flow models for improved uncertainty quantification across various domains."
    ],
    "durationSeconds": 7.170080868999998
  }
}
```

</details>

---

### Tool result

_source line 61 · 2026-05-14T03:18:03.440Z_

<details><summary>↩ Tool result · `toolu_01LL97Nh3eWhxT7Kg5WF2SPj`</summary>

```text
Web search results for query: "VLA uncertainty estimation failure detection robot manipulation 2025 2026 arxiv"

Links: [{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control","url":"https://arxiv.org/html/2604.16677v1"},{"title":"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.08434v2"},{"title":"Early Failure Detection in Autonomous Surgical Soft-Tissue Manipulation via Uncertainty Quantification","url":"https://arxiv.org/html/2501.10561"},{"title":"Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey","url":"https://arxiv.org/html/2508.13073v1"},{"title":"An Uncertainty-Guided and Failure-Aware Vision-Language-Action Model Control Framework for Robotics","url":"https://mavmatrix.uta.edu/materialscieng_theses/145/"},{"title":"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://arxiv.org/html/2507.17049v2"},{"title":"Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey","url":"https://arxiv.org/html/2510.17111v3"},{"title":"GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub","url":"https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"},{"title":"[2507.17049] Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://arxiv.org/abs/2507.17049"}]

I found several highly relevant papers on arXiv related to VLA (Vision-Language-Action) models with uncertainty estimation and failure detection for robot manipulation:

## Key Findings

**ReconVLA** (Most Recent - April 2026): ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals by applying conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success, and extending conformal prediction to the robot state space to detect outliers or unsafe states before failures occur.

**Failing Forward** (May 2026): SAFE (Gu et al., 2026) introduces a multitask failure detection framework based on internal VLA representations, while UNISafe (Seo et al., 2025) proposes uncertainty-aware latent safety filters to prevent out-of-distribution failures.

**SafeVLA** (September 2025): SafeVLA explores VLA from a safety perspective, proposing a constrained-learning alignment mechanism to prevent high-risk behaviors while maintaining task performance, and incorporating a safety critic network into the VLA architecture to estimate risk levels.

**Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots** (July 2025): Researchers propose five quality metrics designed to assess whether a task is performed in a high-quality manner and eight uncertainty metrics to quantify the VLA model's confidence during task execution.

These papers represent the latest research in the field addressing the challenge of making VLA models more reliable through uncertainty estimation and failure detection mechanisms.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "f022a129-b32d-40b0-b45d-0ae75adb5346",
  "tool_use_result": {
    "query": "VLA uncertainty estimation failure detection robot manipulation 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_018BQUyTDUrcc3HjJfdYYkM2",
        "content": [
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control",
            "url": "https://arxiv.org/html/2604.16677v1"
          },
          {
            "title": "Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2605.08434v2"
          },
          {
            "title": "Early Failure Detection in Autonomous Surgical Soft-Tissue Manipulation via Uncertainty Quantification",
            "url": "https://arxiv.org/html/2501.10561"
          },
          {
            "title": "Large VLM-based Vision-Language-Action Models for Robotic Manipulation: A Survey",
            "url": "https://arxiv.org/html/2508.13073v1"
          },
          {
            "title": "An Uncertainty-Guided and Failure-Aware Vision-Language-Action Model Control Framework for Robotics",
            "url": "https://mavmatrix.uta.edu/materialscieng_theses/145/"
          },
          {
            "title": "Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots",
            "url": "https://arxiv.org/html/2507.17049v2"
          },
          {
            "title": "Efficient Vision-Language-Action Models for Embodied Manipulation: A Systematic Survey",
            "url": "https://arxiv.org/html/2510.17111v3"
          },
          {
            "title": "GitHub - JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation: A curated list of large VLM-based VLA models for robotic manipulation. · GitHub",
            "url": "https://github.com/JiuTian-VL/Large-VLM-based-VLA-for-Robotic-Manipulation"
          },
          {
            "title": "[2507.17049] Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots",
            "url": "https://arxiv.org/abs/2507.17049"
          }
        ]
      },
      "I found several highly relevant papers on arXiv related to VLA (Vision-Language-Action) models with uncertainty estimation and failure detection for robot manipulation:\n\n## Key Findings\n\n**ReconVLA** (Most Recent - April 2026): ReconVLA is a reliable conformal model that produces uncertainty-guided and failure-aware control signals by applying conformal prediction directly to the action token outputs of pretrained VLA policies, yielding calibrated uncertainty estimates that correlate with execution quality and task success, and extending conformal prediction to the robot state space to detect outliers or unsafe states before failures occur.\n\n**Failing Forward** (May 2026): SAFE (Gu et al., 2026) introduces a multitask failure detection framework based on internal VLA representations, while UNISafe (Seo et al., 2025) proposes uncertainty-aware latent safety filters to prevent out-of-distribution failures.\n\n**SafeVLA** (September 2025): SafeVLA explores VLA from a safety perspective, proposing a constrained-learning alignment mechanism to prevent high-risk behaviors while maintaining task performance, and incorporating a safety critic network into the VLA architecture to estimate risk levels.\n\n**Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots** (July 2025): Researchers propose five quality metrics designed to assess whether a task is performed in a high-quality manner and eight uncertainty metrics to quantify the VLA model's confidence during task execution.\n\nThese papers represent the latest research in the field addressing the challenge of making VLA models more reliable through uncertainty estimation and failure detection mechanisms."
    ],
    "durationSeconds": 7.546041532000003
  }
}
```

</details>

---

### Assistant

_source line 62_

<details><summary>Logged reasoning block</summary>

```text
Let me gather a few more details on specific papers and also look for any papers I might have missed. Let me search for:

1. "Evaluating Uncertainty and Quality of VLA-enabled Robots" (2507.17049)
2. "Failing Forward" (2605.08434)
3. VLA-Pilot (arxiv 2511.14178) details
4. SafeDiffCon - conformal prediction with diffusion models for safe control
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "4a79b063-9886-43f9-a3a4-92f86a7a820a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeCRjtxHZ7EmStmHbnabBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 49238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4097
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

_source line 63_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Y9yeWidYJULeXvae9vKbXL`</summary>

```json
{
  "query": "\"evaluating uncertainty quality\" VLA robot arxiv 2507.17049 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "2f5f7dd4-9146-40b0-9e27-f7189eecf706",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeCRjtxHZ7EmStmHbnabBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 49238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4097
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

_source line 64_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013XSSUwGZqzgFxLgr1BadEM`</summary>

```json
{
  "query": "\"failing forward\" adaptive failure-informed VLA arxiv 2605.08434"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "9a9ae1d3-ed0f-4e7b-8f60-e1af5a35686b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeCRjtxHZ7EmStmHbnabBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 49238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4097
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

_source line 65_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JHy8niJsfywDZSACCv97Wz`</summary>

```json
{
  "query": "SafeDiffCon \"conformal prediction\" diffusion safe control ICML 2025 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "45d720d4-f924-4c30-9c0e-5fbebb484d70",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GeCRjtxHZ7EmStmHbnabBT",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4097,
      "cache_read_input_tokens": 49238,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4097
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

_source line 66 · 2026-05-14T03:18:14.542Z_

<details><summary>↩ Tool result · `toolu_01Y9yeWidYJULeXvae9vKbXL`</summary>

```text
Web search results for query: ""evaluating uncertainty quality" VLA robot arxiv 2507.17049 authors"

Links: [{"title":"[2507.17049] Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://arxiv.org/abs/2507.17049"},{"title":"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://arxiv.org/html/2507.17049"},{"title":"(PDF) Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://www.researchgate.net/publication/393965006_Evaluating_Uncertainty_and_Quality_of_Visual_Language_Action-enabled_Robots"},{"title":"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots | alphaXiv","url":"https://www.alphaxiv.org/overview/2507.17049v1"},{"title":"Results of Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots","url":"https://zenodo.org/records/16315133"},{"title":"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/html/2603.18342"},{"title":"Vision Language Action Models in Robotic Manipulation: A Systematic Review","url":"https://arxiv.org/html/2507.10672v1"},{"title":"Confidence Calibration in Vision-Language-Action Models","url":"https://arxiv.org/html/2507.17383"},{"title":"Robotics | Cool Papers - Immersive Paper Discovery","url":"https://papers.cool/arxiv/cs.RO"},{"title":"[2603.18342] Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/abs/2603.18342"}]

Based on the search results, I found the paper you're looking for:

The arxiv paper 2507.17049 is titled "Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots" and was authored by Pablo Valle, Chengjie Lu, Shaukat Ali, and Aitor Arrieta.

The paper focuses on Visual Language Action (VLA) models, which are a multi-modal class of AI systems that integrate visual perception, natural language understanding, and action planning to enable agents to interpret their environment, comprehend instructions, and perform embodied tasks autonomously.

The main contribution is the proposal of eight uncertainty metrics and five quality metrics specifically designed for VLA models for robotic manipulation tasks. The results reveal that several metrics show moderate to strong correlation with human assessments, and some of the metrics can discriminate between high-, medium-, and low-quality executions from unsuccessful tasks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "502d7a7a-1fdf-462c-a637-1cf1b5f1a2b7",
  "tool_use_result": {
    "query": "\"evaluating uncertainty quality\" VLA robot arxiv 2507.17049 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RwHb55HFViz5Aq2E12QCfs",
        "content": [
          {
            "title": "[2507.17049] Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots",
            "url": "https://arxiv.org/abs/2507.17049"
          },
          {
            "title": "Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots",
            "url": "https://arxiv.org/html/2507.17049"
          },
          {
            "title": "(PDF) Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots",
            "url": "https://www.researchgate.net/publication/393965006_Evaluating_Uncertainty_and_Quality_of_Visual_Language_Action-enabled_Robots"
          },
          {
            "title": "Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots | alphaXiv",
            "url": "https://www.alphaxiv.org/overview/2507.17049v1"
          },
          {
            "title": "Results of Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots",
            "url": "https://zenodo.org/records/16315133"
          },
          {
            "title": "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/html/2603.18342"
          },
          {
            "title": "Vision Language Action Models in Robotic Manipulation: A Systematic Review",
            "url": "https://arxiv.org/html/2507.10672v1"
          },
          {
            "title": "Confidence Calibration in Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2507.17383"
          },
          {
            "title": "Robotics | Cool Papers - Immersive Paper Discovery",
            "url": "https://papers.cool/arxiv/cs.RO"
          },
          {
            "title": "[2603.18342] Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/abs/2603.18342"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe arxiv paper 2507.17049 is titled \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\" and was authored by Pablo Valle, Chengjie Lu, Shaukat Ali, and Aitor Arrieta.\n\nThe paper focuses on Visual Language Action (VLA) models, which are a multi-modal class of AI systems that integrate visual perception, natural language understanding, and action planning to enable agents to interpret their environment, comprehend instructions, and perform embodied tasks autonomously.\n\nThe main contribution is the proposal of eight uncertainty metrics and five quality metrics specifically designed for VLA models for robotic manipulation tasks. The results reveal that several metrics show moderate to strong correlation with human assessments, and some of the metrics can discriminate between high-, medium-, and low-quality executions from unsuccessful tasks."
    ],
    "durationSeconds": 5.016693658000004
  }
}
```

</details>

---

### Tool result

_source line 67 · 2026-05-14T03:18:16.979Z_

<details><summary>↩ Tool result · `toolu_013XSSUwGZqzgFxLgr1BadEM`</summary>

```text
Web search results for query: ""failing forward" adaptive failure-informed VLA arxiv 2605.08434"

Links: [{"title":"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models","url":"https://arxiv.org/html/2605.08434v2"},{"title":"[2210.00279] Failure-informed adaptive sampling for PINNs","url":"https://arxiv.org/abs/2210.00279"},{"title":"One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy","url":"https://arxiv.org/html/2605.07931v1"},{"title":"[2302.01529] Failure-informed adaptive sampling for PINNs, Part II: combining with re-sampling and subset simulation","url":"https://arxiv.org/abs/2302.01529"},{"title":"When Descent Is Too Stable: Event-Triggered Hamiltonian Learning to Optimize","url":"https://arxiv.org/html/2605.06868"},{"title":"SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models","url":"https://arxiv.org/html/2506.03574v1"},{"title":"Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning","url":"https://arxiv.org/html/2605.05544"},{"title":"Pure Vision Language Action (VLA) Models: A Comprehensive Survey","url":"https://arxiv.org/html/2509.19012v1"},{"title":"Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents","url":"https://arxiv.org/html/2605.06908"},{"title":"[2605.06934] Learned Lyapunov Shielding for Adaptive Control","url":"https://arxiv.org/abs/2605.06934"}]

Based on the search results, I found the paper you're looking for! Here's information about "Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models":

## Overview

The paper addresses the limitation of vision-language-action (VLA) models that rely on success-only behavioral cloning, which leaves them brittle, and proposes Adaptive Failure-Informed Learning (AFIL), an end-to-end framework that leverages failure trajectories as adaptive negative guidance for diffusion- and flow-based VLA policies.

## Key Components

AFIL uses a pretrained VLA to generate failure rollouts online, avoiding handcrafted failure-mode design or human-in-the-loop recovery, and jointly trains Dual Action Generators (DAGs) for successful and failed behaviors while sharing a common vision-language backbone.

## How It Works

During sampling, the failure generator adaptively steers action generation away from failure-prone regions and toward more reliable success modes, with guidance strength determined by the per-diffusion-step distance between success and failure distributions.

## Results

Experiments across in-domain and out-of-domain robotic manipulation tasks, covering both short- and long-horizon settings, show that AFIL consistently improves task success rates and robustness over existing VLA baselines.

The paper was authored by researchers at United Imaging Intelligence and the University of Illinois Urbana-Champaign, and the version referenced was updated on May 12, 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "793e97f7-189e-476f-83ed-5f11ceb09674",
  "tool_use_result": {
    "query": "\"failing forward\" adaptive failure-informed VLA arxiv 2605.08434",
    "results": [
      {
        "tool_use_id": "srvtoolu_018WqEziLQrij7QZL3B14JcU",
        "content": [
          {
            "title": "Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2605.08434v2"
          },
          {
            "title": "[2210.00279] Failure-informed adaptive sampling for PINNs",
            "url": "https://arxiv.org/abs/2210.00279"
          },
          {
            "title": "One Token Per Frame: Reconsidering Visual Bandwidth in World Models for VLA Policy",
            "url": "https://arxiv.org/html/2605.07931v1"
          },
          {
            "title": "[2302.01529] Failure-informed adaptive sampling for PINNs, Part II: combining with re-sampling and subset simulation",
            "url": "https://arxiv.org/abs/2302.01529"
          },
          {
            "title": "When Descent Is Too Stable: Event-Triggered Hamiltonian Learning to Optimize",
            "url": "https://arxiv.org/html/2605.06868"
          },
          {
            "title": "SwitchVLA: Execution-Aware Task Switching for Vision-Language-Action Models",
            "url": "https://arxiv.org/html/2506.03574v1"
          },
          {
            "title": "Adaptive Q-Chunking for Offline-to-Online Reinforcement Learning",
            "url": "https://arxiv.org/html/2605.05544"
          },
          {
            "title": "Pure Vision Language Action (VLA) Models: A Comprehensive Survey",
            "url": "https://arxiv.org/html/2509.19012v1"
          },
          {
            "title": "Same Signal, Opposite Meaning: Direction-Informed Adaptive Learning for LLM Agents",
            "url": "https://arxiv.org/html/2605.06908"
          },
          {
            "title": "[2605.06934] Learned Lyapunov Shielding for Adaptive Control",
            "url": "https://arxiv.org/abs/2605.06934"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for! Here's information about \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\":\n\n## Overview\n\nThe paper addresses the limitation of vision-language-action (VLA) models that rely on success-only behavioral cloning, which leaves them brittle, and proposes Adaptive Failure-Informed Learning (AFIL), an end-to-end framework that leverages failure trajectories as adaptive negative guidance for diffusion- and flow-based VLA policies.\n\n## Key Components\n\nAFIL uses a pretrained VLA to generate failure rollouts online, avoiding handcrafted failure-mode design or human-in-the-loop recovery, and jointly trains Dual Action Generators (DAGs) for successful and failed behaviors while sharing a common vision-language backbone.\n\n## How It Works\n\nDuring sampling, the failure generator adaptively steers action generation away from failure-prone regions and toward more reliable success modes, with guidance strength determined by the per-diffusion-step distance between success and failure distributions.\n\n## Results\n\nExperiments across in-domain and out-of-domain robotic manipulation tasks, covering both short- and long-horizon settings, show that AFIL consistently improves task success rates and robustness over existing VLA baselines.\n\nThe paper was authored by researchers at United Imaging Intelligence and the University of Illinois Urbana-Champaign, and the version referenced was updated on May 12, 2026."
    ],
    "durationSeconds": 7.049853642000002
  }
}
```

</details>

---

### Tool result

_source line 68 · 2026-05-14T03:18:17.350Z_

<details><summary>↩ Tool result · `toolu_01JHy8niJsfywDZSACCv97Wz`</summary>

```text
Web search results for query: "SafeDiffCon "conformal prediction" diffusion safe control ICML 2025 arxiv"

Links: [{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control","url":"https://arxiv.org/html/2502.02205"},{"title":"ICML Poster From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control","url":"https://icml.cc/virtual/2025/poster/44969"},{"title":"[2502.02205] From Uncertain to Safe: Conformal Fine-Tuning of Diffusion Models for Safe PDE Control","url":"https://arxiv.org/abs/2502.02205"},{"title":"GitHub - AI4Science-WestlakeU/safediffcon: [ICML2025] SafeDiffCon is a diffusion model for safe PDE Control.","url":"https://github.com/AI4Science-WestlakeU/safediffcon"},{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models","url":"https://arxiv.org/pdf/2502.02205"},{"title":"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control | OpenReview","url":"https://openreview.net/forum?id=XGJ33p4qwt&noteId=q2qh0U2HX9"},{"title":"SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | OpenReview","url":"https://openreview.net/forum?id=ig2wk7kK9J"},{"title":"Computer Science Feb 2025","url":"https://www.arxiv.org/list/cs/2025-02?skip=1150&show=25"},{"title":"[2208.02814] Conformal Risk Control","url":"https://arxiv.org/abs/2208.02814"},{"title":"[2302.03791] How to Trust Your Diffusion Model: A Convex Optimization Approach to Conformal Risk Control","url":"https://arxiv.org/abs/2302.03791"}]

I found comprehensive results about SafeDiffCon. Here's what the search revealed:

## SafeDiffCon Overview

SafeDiffCon is a method that adapts diffusion models to varying safety constraints by quantifying their uncertainty. The paper "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control" was accepted to ICML 2025, with arXiv identifier 2502.02205.

## Key Methodology

SafeDiffCon introduces the uncertainty quantile as model uncertainty quantification to achieve optimal control under safety constraints through both post-training and inference phases, with post-training incorporating the uncertainty quantile estimated using conformal prediction via a reweighted diffusion loss. During inference, the diffusion model dynamically adjusts both its generation process and parameters through iterative guidance and fine-tuning, conditioned on control targets while simultaneously integrating the estimated uncertainty quantile.

## Experimental Results

SafeDiffCon was evaluated on three control tasks: 1D Burgers' equation, 2D incompressible fluid, and controlled nuclear fusion problem, with results demonstrating that SafeDiffCon is the only method that satisfies all safety constraints whereas other classical and deep learning baselines fail, while also achieving the best control performance.

## Code Availability

The official implementation is available at: https://github.com/AI4Science-WestlakeU/safediffcon


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "210b476f-ff20-4ca9-808c-6bccdae21e49",
  "tool_use_result": {
    "query": "SafeDiffCon \"conformal prediction\" diffusion safe control ICML 2025 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01YDyMvy1Mgcsf9ARw83zVSM",
        "content": [
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control",
            "url": "https://arxiv.org/html/2502.02205"
          },
          {
            "title": "ICML Poster From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control",
            "url": "https://icml.cc/virtual/2025/poster/44969"
          },
          {
            "title": "[2502.02205] From Uncertain to Safe: Conformal Fine-Tuning of Diffusion Models for Safe PDE Control",
            "url": "https://arxiv.org/abs/2502.02205"
          },
          {
            "title": "GitHub - AI4Science-WestlakeU/safediffcon: [ICML2025] SafeDiffCon is a diffusion model for safe PDE Control.",
            "url": "https://github.com/AI4Science-WestlakeU/safediffcon"
          },
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models",
            "url": "https://arxiv.org/pdf/2502.02205"
          },
          {
            "title": "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control | OpenReview",
            "url": "https://openreview.net/forum?id=XGJ33p4qwt&noteId=q2qh0U2HX9"
          },
          {
            "title": "SafeDiffuser: Safe Planning with Diffusion Probabilistic Models | OpenReview",
            "url": "https://openreview.net/forum?id=ig2wk7kK9J"
          },
          {
            "title": "Computer Science Feb 2025",
            "url": "https://www.arxiv.org/list/cs/2025-02?skip=1150&show=25"
          },
          {
            "title": "[2208.02814] Conformal Risk Control",
            "url": "https://arxiv.org/abs/2208.02814"
          },
          {
            "title": "[2302.03791] How to Trust Your Diffusion Model: A Convex Optimization Approach to Conformal Risk Control",
            "url": "https://arxiv.org/abs/2302.03791"
          }
        ]
      },
      "I found comprehensive results about SafeDiffCon. Here's what the search revealed:\n\n## SafeDiffCon Overview\n\nSafeDiffCon is a method that adapts diffusion models to varying safety constraints by quantifying their uncertainty. The paper \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\" was accepted to ICML 2025, with arXiv identifier 2502.02205.\n\n## Key Methodology\n\nSafeDiffCon introduces the uncertainty quantile as model uncertainty quantification to achieve optimal control under safety constraints through both post-training and inference phases, with post-training incorporating the uncertainty quantile estimated using conformal prediction via a reweighted diffusion loss. During inference, the diffusion model dynamically adjusts both its generation process and parameters through iterative guidance and fine-tuning, conditioned on control targets while simultaneously integrating the estimated uncertainty quantile.\n\n## Experimental Results\n\nSafeDiffCon was evaluated on three control tasks: 1D Burgers' equation, 2D incompressible fluid, and controlled nuclear fusion problem, with results demonstrating that SafeDiffCon is the only method that satisfies all safety constraints whereas other classical and deep learning baselines fail, while also achieving the best control performance.\n\n## Code Availability\n\nThe official implementation is available at: https://github.com/AI4Science-WestlakeU/safediffcon"
    ],
    "durationSeconds": 6.981082556999987
  }
}
```

</details>

---

### Assistant

_source line 69_

<details><summary>Logged reasoning block</summary>

```text
I also found a very interesting paper: "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model" (2603.18342). Let me search for that one, and also check for one or two more.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "c84f7655-6dfc-46a6-a346-a90499fb375d",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA1gkPQQhBJoxpohgbZBf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 53335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 70_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Mwh3sP9BLRSxKK5iZzHUGT`</summary>

```json
{
  "query": "\"shifting uncertainty to critical moments\" VLA uncertainty quantification arxiv 2603.18342"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "95d61eb8-b88e-45b4-9f82-499c7855a61b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA1gkPQQhBJoxpohgbZBf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 53335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 71_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018jEZjQR1YNPuFpqbfx3uzq`</summary>

```json
{
  "query": "\"multivariate conformal prediction\" \"optimal transport\" arxiv 2502.03609 authors"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "26a74735-9ec9-4fa7-a484-beca4a50a77b",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JA1gkPQQhBJoxpohgbZBf2",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2711,
      "cache_read_input_tokens": 53335,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2711
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

_source line 72 · 2026-05-14T03:18:27.853Z_

<details><summary>↩ Tool result · `toolu_018jEZjQR1YNPuFpqbfx3uzq`</summary>

```text
Web search results for query: ""multivariate conformal prediction" "optimal transport" arxiv 2502.03609 authors"

Links: [{"title":"[2502.03609] Multivariate Conformal Prediction using Optimal Transport","url":"https://arxiv.org/abs/2502.03609"},{"title":"Multivariate Conformal Prediction using Optimal Transport","url":"https://arxiv.org/html/2502.03609v1"},{"title":"(PDF) Multivariate Conformal Prediction using Optimal Transport","url":"https://www.researchgate.net/publication/388791631_Multivariate_Conformal_Prediction_using_Optimal_Transport"},{"title":"[PDF] Multivariate Conformal Prediction using Optimal Transport | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-using-Optimal-Klein-B%C3%A9thune/e6ceea1f7e5d881dcf32e43719a364519cffa4a4"},{"title":"NEURAL OPTIMAL TRANSPORT MEETS MULTIVARIATE CONFORMAL PREDICTION","url":"https://arxiv.org/pdf/2509.25444"},{"title":"Multivariate Conformal Prediction using Optimal Transport | OpenReview","url":"https://openreview.net/forum?id=haEAhTexqm"},{"title":"Conformal Predictive Portfolio Selection","url":"https://arxiv.org/html/2410.16333"},{"title":"dblp: Multivariate Conformal Prediction using Optimal Transport.","url":"https://dblp.org/rec/journals/corr/abs-2502-03609.html"},{"title":"Multivariate Conformal Prediction using Optimal Transport | alphaXiv","url":"https://www.alphaxiv.org/abs/2502.03609"},{"title":"Beyond Uncertainty Sets: Leveraging Optimal Transport to Extend Conformal Predictive Distribution to Multivariate Settings","url":"https://arxiv.org/html/2511.15146v1"}]

Based on the search results, I found the information about arxiv paper 2502.03609 on multivariate conformal prediction using optimal transport.

## Paper Details

**Title:** Multivariate Conformal Prediction using Optimal Transport

**Authors:** Michal Klein, Louis Bethune, Eugene Ndiaye, and Marco Cuturi

**Submission Date:** February 5, 2025

## Overview

The method, OTCP, offers a principled framework for constructing conformal prediction sets in multidimensional settings, preserving distribution-free coverage guarantees with finite data samples. 

The challenge in extending conformal prediction scores to multivariate spaces lies in the fact that no canonical order for vectors exists. To address this, the authors leverage a natural extension of multivariate score ranking based on optimal transport (OT).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "250cfd2b-ee03-43c3-a489-57ae2adddcb4",
  "tool_use_result": {
    "query": "\"multivariate conformal prediction\" \"optimal transport\" arxiv 2502.03609 authors",
    "results": [
      {
        "tool_use_id": "srvtoolu_01BeSBA4DCALjuABh6LxAj6J",
        "content": [
          {
            "title": "[2502.03609] Multivariate Conformal Prediction using Optimal Transport",
            "url": "https://arxiv.org/abs/2502.03609"
          },
          {
            "title": "Multivariate Conformal Prediction using Optimal Transport",
            "url": "https://arxiv.org/html/2502.03609v1"
          },
          {
            "title": "(PDF) Multivariate Conformal Prediction using Optimal Transport",
            "url": "https://www.researchgate.net/publication/388791631_Multivariate_Conformal_Prediction_using_Optimal_Transport"
          },
          {
            "title": "[PDF] Multivariate Conformal Prediction using Optimal Transport | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Multivariate-Conformal-Prediction-using-Optimal-Klein-B%C3%A9thune/e6ceea1f7e5d881dcf32e43719a364519cffa4a4"
          },
          {
            "title": "NEURAL OPTIMAL TRANSPORT MEETS MULTIVARIATE CONFORMAL PREDICTION",
            "url": "https://arxiv.org/pdf/2509.25444"
          },
          {
            "title": "Multivariate Conformal Prediction using Optimal Transport | OpenReview",
            "url": "https://openreview.net/forum?id=haEAhTexqm"
          },
          {
            "title": "Conformal Predictive Portfolio Selection",
            "url": "https://arxiv.org/html/2410.16333"
          },
          {
            "title": "dblp: Multivariate Conformal Prediction using Optimal Transport.",
            "url": "https://dblp.org/rec/journals/corr/abs-2502-03609.html"
          },
          {
            "title": "Multivariate Conformal Prediction using Optimal Transport | alphaXiv",
            "url": "https://www.alphaxiv.org/abs/2502.03609"
          },
          {
            "title": "Beyond Uncertainty Sets: Leveraging Optimal Transport to Extend Conformal Predictive Distribution to Multivariate Settings",
            "url": "https://arxiv.org/html/2511.15146v1"
          }
        ]
      },
      "Based on the search results, I found the information about arxiv paper 2502.03609 on multivariate conformal prediction using optimal transport.\n\n## Paper Details\n\n**Title:** Multivariate Conformal Prediction using Optimal Transport\n\n**Authors:** Michal Klein, Louis Bethune, Eugene Ndiaye, and Marco Cuturi\n\n**Submission Date:** February 5, 2025\n\n## Overview\n\nThe method, OTCP, offers a principled framework for constructing conformal prediction sets in multidimensional settings, preserving distribution-free coverage guarantees with finite data samples. \n\nThe challenge in extending conformal prediction scores to multivariate spaces lies in the fact that no canonical order for vectors exists. To address this, the authors leverage a natural extension of multivariate score ranking based on optimal transport (OT)."
    ],
    "durationSeconds": 5.165469188999996
  }
}
```

</details>

---

### Tool result

_source line 73 · 2026-05-14T03:18:32.154Z_

<details><summary>↩ Tool result · `toolu_01Mwh3sP9BLRSxKK5iZzHUGT`</summary>

```text
Web search results for query: ""shifting uncertainty to critical moments" VLA uncertainty quantification arxiv 2603.18342"

Links: [{"title":"[2603.18342] Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/abs/2603.18342"},{"title":"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model","url":"https://arxiv.org/html/2603.18342"},{"title":"Shifting Uncertainty to Critical Moments: Towards Reliable","url":"https://arxiv.org/pdf/2603.18342"},{"title":"[2603.08981] Uncertainty quantification for critical energy systems during compound extremes via BMW-GAM","url":"https://arxiv.org/abs/2603.08981"},{"title":"[2603.29941] Better than Average: Spatially-Aware Aggregation of Segmentation Uncertainty Improves Downstream Performance","url":"https://arxiv.org/abs/2603.29941"},{"title":"[2603.29466] An Isotropic Approach to Efficient Uncertainty Quantification with Gradient Norms","url":"https://arxiv.org/abs/2603.29466"},{"title":"[2603.24259] Uncertainty Quantification of Spline Predictors on Compact Riemannian Manifolds","url":"https://arxiv.org/abs/2603.24259"},{"title":"[2603.19804] Uncertainty Quantification Via the Posterior Predictive Variance","url":"https://arxiv.org/abs/2603.19804"},{"title":"Uncertainty Quantification of Spline Predictors on Compact Riemannian Manifolds","url":"https://arxiv.org/html/2603.24259"},{"title":"Temporal Evaluation of Uncertainty Quantification Under Distribution Shift | Springer Nature Link","url":"https://link.springer.com/chapter/10.1007/978-3-031-72381-0_11"}]

I found the paper! Here's information about arxiv paper 2603.18342:

**Title:** "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model"

**Authors:** Yanchuan Tang, Taowen Wang, Yuefei Chen, Boxuan Zhang, Qiang Guan, and Ruixiang Tang from Rutgers University and Kent State University

**Main Topic:** Vision-Language-Action (VLA) models enable general-purpose robotic policies by mapping visual observations and language instructions to low-level actions, but they often lack reliable introspection.

**Key Problem Addressed:** A common practice is to compute a token-level uncertainty signal and take its mean over a rollout. However, mean aggregation can dilute short-lived but safety-critical uncertainty spikes in continuous control. The paper terms this the "Averaging Trap" - successful trajectories often contain high-entropy segments due to benign noise or non-critical micro-adjustments, while failure cases may exhibit low entropy for the majority of execution, masking the transient spikes that actually cause the failure.

**Proposed Solutions:** The paper proposes a unified uncertainty quantification approach that uses max-based sliding window pooling to preserve transient risk signals and applies motion-aware stability weighting to emphasize high-frequency action oscillations associated with unstable behaviors.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "d2c4d480-15f7-41ef-8ab6-aa7ed6de71d2",
  "tool_use_result": {
    "query": "\"shifting uncertainty to critical moments\" VLA uncertainty quantification arxiv 2603.18342",
    "results": [
      {
        "tool_use_id": "srvtoolu_012DdK1RqxvzV7CVioSmDTFF",
        "content": [
          {
            "title": "[2603.18342] Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/abs/2603.18342"
          },
          {
            "title": "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model",
            "url": "https://arxiv.org/html/2603.18342"
          },
          {
            "title": "Shifting Uncertainty to Critical Moments: Towards Reliable",
            "url": "https://arxiv.org/pdf/2603.18342"
          },
          {
            "title": "[2603.08981] Uncertainty quantification for critical energy systems during compound extremes via BMW-GAM",
            "url": "https://arxiv.org/abs/2603.08981"
          },
          {
            "title": "[2603.29941] Better than Average: Spatially-Aware Aggregation of Segmentation Uncertainty Improves Downstream Performance",
            "url": "https://arxiv.org/abs/2603.29941"
          },
          {
            "title": "[2603.29466] An Isotropic Approach to Efficient Uncertainty Quantification with Gradient Norms",
            "url": "https://arxiv.org/abs/2603.29466"
          },
          {
            "title": "[2603.24259] Uncertainty Quantification of Spline Predictors on Compact Riemannian Manifolds",
            "url": "https://arxiv.org/abs/2603.24259"
          },
          {
            "title": "[2603.19804] Uncertainty Quantification Via the Posterior Predictive Variance",
            "url": "https://arxiv.org/abs/2603.19804"
          },
          {
            "title": "Uncertainty Quantification of Spline Predictors on Compact Riemannian Manifolds",
            "url": "https://arxiv.org/html/2603.24259"
          },
          {
            "title": "Temporal Evaluation of Uncertainty Quantification Under Distribution Shift | Springer Nature Link",
            "url": "https://link.springer.com/chapter/10.1007/978-3-031-72381-0_11"
          }
        ]
      },
      "I found the paper! Here's information about arxiv paper 2603.18342:\n\n**Title:** \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n\n**Authors:** Yanchuan Tang, Taowen Wang, Yuefei Chen, Boxuan Zhang, Qiang Guan, and Ruixiang Tang from Rutgers University and Kent State University\n\n**Main Topic:** Vision-Language-Action (VLA) models enable general-purpose robotic policies by mapping visual observations and language instructions to low-level actions, but they often lack reliable introspection.\n\n**Key Problem Addressed:** A common practice is to compute a token-level uncertainty signal and take its mean over a rollout. However, mean aggregation can dilute short-lived but safety-critical uncertainty spikes in continuous control. The paper terms this the \"Averaging Trap\" - successful trajectories often contain high-entropy segments due to benign noise or non-critical micro-adjustments, while failure cases may exhibit low entropy for the majority of execution, masking the transient spikes that actually cause the failure.\n\n**Proposed Solutions:** The paper proposes a unified uncertainty quantification approach that uses max-based sliding window pooling to preserve transient risk signals and applies motion-aware stability weighting to emphasize high-frequency action oscillations associated with unstable behaviors."
    ],
    "durationSeconds": 9.991249635
  }
}
```

</details>

---

### Assistant

_source line 74_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive picture. Let me compile the new papers that are NOT in the existing literature map. Let me identify which ones are truly new and relevant:

Already in the map (31 entries):
- a2c2_2025
- angelopoulos2023gentle
- barber2023conformal
- black2024pi0
- braun2025cgs
- brohan2023rt2
- chen2026reconvla
- digflow2025
- fei2025liberoplus
- ghosh2024octo
- gibbs2021aci
- gu2025safe


- kim2024openvla
- ledoit2004well
- lipman2023flow
- liu2023libero
- liu2026ttvla
- luan2026snapflow
- robustvla2025
- romano2019cqr
- shafer2008tutorial
- shukor2025smolvla
- srpo2025
- wang2025cploop
- xing2026diu
- yuan2026ups
- zhao2024conformalized
- cosmos_policy_2026
- vla_gse_2026
- lakshminarayanan2017ensembles
- gal2016

dropout
- chi2023diffusion_policy

I'm identifying three additional papers to integrate into the map: one on learnable conformal prediction for robotic planning, another examining confidence calibration specifically in VLAs with ensemble and scaling techniques, and a third on self-correcting VLAs that refine actions through sparse world imagination and residual reinforcement learning.

Now I'm looking at four more papers to add: VLA-Pilot, which uses an MLLM verifier with evolutionary diffusion for inference-time policy steering; an interpretable multivariate conformal prediction approach using fast transductive standardization for per-DOF intervals; an optimal transport-based method for multivariate CP scoring; and CLAPS, which appears to be about conformalized Lie-group approaches.

Continuing through the list, LUCCa provides local conformal calibration for robot dynamics uncertainty, ACoT-VLA improves VLA robustness through action chain-of-thought reasoning, and there's a method for shifting uncertainty quantification toward critical moments in VLA using max-pooling to detect uncertainty spikes.

Safe probabilistic planning combines conformal risk control with control barrier functions, SafeDiffCon applies conformal prediction to diffusion-based control policies, and AFIL takes a failure-informed approach to improve VLA robustness. Valle et al. provide metrics for evaluating both uncertainty and quality in VLA systems, while DiffusionVLA combines autoregressive reasoning with diffusion policies.

Now I'm narrowing down to the most impactful papers—those directly addressing conformal prediction with robotics, VLA inference-time correction, and per-DOF uncertainty quantification from 2025-2026. I'll add all the relevant ones to the literature map since they all fit our scope. Looking at what's already documented, ReconVLA is the closest existing work, and the interpretable multivariate conformal prediction paper is particularly valuable for our per-DOF decomposition approach. I haven't found any direct competitors doing exactly per-DOF conformal prediction with VLAs, which strengthens our novelty position.

Updating the YAML file...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "1cbaffe1-2e36-4ad7-9643-faa04b4bfe24",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8b39eVbkpQat24KXCifcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 1051,
      "cache_read_input_tokens": 56046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1051
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

_source line 75_

Now I have a comprehensive picture. No direct competitor doing per-DOF conformal + VLA was found (our novelty is safe). Let me compile and write the new entries.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "d84247ad-4fc9-417f-814a-359f5bb5199e",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8b39eVbkpQat24KXCifcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 1051,
      "cache_read_input_tokens": 56046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1051
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

_source line 76_

<details open><summary>🔧 Tool call — Read · `toolu_01G1iVv3zUfLswDSVU9rjRbm`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "2568c6fa-0860-401c-98ac-925734d3c650",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8b39eVbkpQat24KXCifcW",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 751,
      "cache_creation_input_tokens": 1051,
      "cache_read_input_tokens": 56046,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 1051
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

_source line 77 · 2026-05-14T03:19:13.741Z_

<details><summary>↩ Tool result · `toolu_01G1iVv3zUfLswDSVU9rjRbm`</summary>

```text
1	papers:
2	  - bibtex_key: "a2c2_2025"
3	    title: "Leave No Observation Behind: Real-time Correction for VLA Action Chunks"
4	    authors: "Sendai et al."
5	    year: 2025
6	    venue: "arXiv:2509.23224"
7	    url: "https://arxiv.org/abs/2509.23224"
8	    category: "inference_correction"
9	    verified: true
10	    relevance: "Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA."
11	    must_cite: true
12	
13	  - bibtex_key: "angelopoulos2023gentle"
14	    title: "A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification"
15	    authors: "Angelopoulos & Bates"
16	    year: 2023
17	    venue: "Foundations and Trends in Machine Learning"
18	    url: "https://arxiv.org/abs/2107.07511"
19	    category: "cp_foundation"
20	    verified: true
21	    relevance: "Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA."
22	    must_cite: true
23	
24	  - bibtex_key: "barber2023conformal"
25	    title: "Conformal Prediction Beyond Exchangeability"
26	    authors: "Barber et al."
27	    year: 2023
28	    venue: "Annals of Statistics, 51(2):816-845"
29	    url: "https://arxiv.org/abs/2202.13415"
30	    category: "cp_foundation"
31	    verified: true
32	    relevance: "Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment."
33	    must_cite: false
34	
35	  - bibtex_key: "black2024pi0"
36	    title: "pi0: A Vision-Language-Action Flow Model for General Robot Control"
37	    authors: "Black et al."
38	    year: 2024
39	    venue: "arXiv:2410.24164"
40	    url: "https://arxiv.org/abs/2410.24164"
41	    category: "vla_foundation"
42	    verified: true
43	    relevance: "Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0."
44	    must_cite: false
45	
46	  - bibtex_key: "braun2025cgs"
47	    title: "Multivariate Conformal Prediction via Conformalized Gaussian Scoring"
48	    authors: "Braun et al."
49	    year: 2025
50	    venue: "arXiv:2507.20941"
51	    url: "https://arxiv.org/abs/2507.20941"
52	    category: "cp_foundation"
53	    verified: true
54	    relevance: "Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component."
55	    must_cite: true
56	
57	  - bibtex_key: "brohan2023rt2"
58	    title: "RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control"
59	    authors: "Brohan et al."
60	    year: 2023
61	    venue: "arXiv:2307.15818"
62	    url: "https://arxiv.org/abs/2307.15818"
63	    category: "vla_foundation"
64	    verified: true
65	    relevance: "Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon."
66	    must_cite: false
67	
68	  - bibtex_key: "chen2026reconvla"
69	    title: "ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control"
70	    authors: "Chen et al."
71	    year: 2026
72	    venue: "arXiv:2604.16677"
73	    url: "https://arxiv.org/abs/2604.16677"
74	    category: "inference_correction"
75	    verified: true
76	    relevance: "Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach."
77	    must_cite: true
78	
79	  - bibtex_key: "digflow2025"
80	    title: "DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models"
81	    authors: "Zhang et al."
82	    year: 2025
83	    venue: "arXiv:2512.01715"
84	    url: "https://arxiv.org/abs/2512.01715"
85	    category: "vla_robustness_training"
86	    verified: true
87	    relevance: "Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction."
88	    must_cite: true
89	
90	  - bibtex_key: "fei2025liberoplus"
91	    title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
92	    authors: "Fei et al."
93	    year: 2025
94	    venue: "arXiv:2510.13626"
95	    url: "https://arxiv.org/abs/2510.13626"
96	    category: "other"
97	    verified: true
98	    relevance: "Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments."
99	    must_cite: true
100	
101	  - bibtex_key: "ghosh2024octo"
102	    title: "Octo: An Open-Source Generalist Robot Policy"
103	    authors: "Ghosh et al."
104	    year: 2024
105	    venue: "arXiv:2405.12213"
106	    url: "https://arxiv.org/abs/2405.12213"
107	    category: "vla_foundation"
108	    verified: true
109	    relevance: "Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution."
110	    must_cite: false
111	
112	  - bibtex_key: "gibbs2021aci"
113	    title: "Adaptive Conformal Inference Under Distribution Shift"
114	    authors: "Gibbs & Candès"
115	    year: 2021
116	    venue: "NeurIPS 2021"
117	    url: "https://arxiv.org/abs/2106.00170"
118	    category: "cp_foundation"
119	    verified: true
120	    relevance: "Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment."
121	    must_cite: true
122	
123	  - bibtex_key: "gu2025safe"
124	    title: "SAFE: Multitask Failure Detection for Vision-Language-Action Models"
125	    authors: "Gu et al."
126	    year: 2025
127	    venue: "NeurIPS 2025"
128	    url: "https://arxiv.org/abs/2506.09937"
129	    category: "inference_correction"
130	    verified: true
131	    relevance: "VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach."
132	    must_cite: true
133	
134	  - bibtex_key: "kim2024openvla"
135	    title: "OpenVLA: An Open-Source Vision-Language-Action Model"
136	    authors: "Kim et al."
137	    year: 2024
138	    venue: "arXiv:2406.09246"
139	    url: "https://arxiv.org/abs/2406.09246"
140	    category: "vla_foundation"
141	    verified: true
142	    relevance: "Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration."
143	    must_cite: false
144	
145	  - bibtex_key: "ledoit2004well"
146	    title: "A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices"
147	    authors: "Ledoit & Wolf"
148	    year: 2004
149	    venue: "Journal of Multivariate Analysis, 88(2):365-411"
150	    url: "https://www.sciencedirect.com/science/article/pii/S0047259X03000964"
151	    category: "other"
152	    verified: true
153	    relevance: "Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples."
154	    must_cite: false
155	
156	  - bibtex_key: "lipman2023flow"
157	    title: "Flow Matching for Generative Modeling"
158	    authors: "Lipman et al."
159	    year: 2023
160	    venue: "ICLR 2023"
161	    url: "https://arxiv.org/abs/2210.02747"
162	    category: "other"
163	    verified: true
164	    relevance: "Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects."
165	    must_cite: false
166	
167	  - bibtex_key: "liu2023libero"
168	    title: "LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning"
169	    authors: "Liu et al."
170	    year: 2023
171	    venue: "NeurIPS 2023"
172	    url: "https://arxiv.org/abs/2306.03310"
173	    category: "other"
174	    verified: true
175	    relevance: "Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation."
176	    must_cite: false
177	
178	  - bibtex_key: "liu2026ttvla"
179	    title: "On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning"
180	    authors: "Liu et al."
181	    year: 2026
182	    venue: "arXiv:2601.06748"
183	    url: "https://arxiv.org/abs/2601.06748"
184	    category: "vla_robustness_training"
185	    verified: true
186	    relevance: "Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction."
187	    must_cite: true
188	
189	  - bibtex_key: "luan2026snapflow"
190	    title: "SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation"
191	    authors: "Luan et al."
192	    year: 2026
193	    venue: "arXiv:2604.05656"
194	    url: "https://arxiv.org/abs/2604.05656"
195	    category: "vla_robustness_training"
196	    verified: true
197	    relevance: "Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness."
198	    must_cite: true
199	
200	  - bibtex_key: "robustvla2025"
201	    title: "RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models"
202	    authors: "Zhang et al."
203	    year: 2025
204	    venue: "arXiv:2511.01331"
205	    url: "https://arxiv.org/abs/2511.01331"
206	    category: "vla_robustness_training"
207	    verified: true
208	    relevance: "RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach."
209	    must_cite: true
210	
211	  - bibtex_key: "romano2019cqr"
212	    title: "Conformalized Quantile Regression"
213	    authors: "Romano et al."
214	    year: 2019
215	    venue: "NeurIPS 2019"
216	    url: "https://arxiv.org/abs/1905.03222"
217	    category: "cp_foundation"
218	    verified: true
219	    relevance: "Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction."
220	    must_cite: false
221	
222	  - bibtex_key: "shafer2008tutorial"
223	    title: "A Tutorial on Conformal Prediction"
224	    authors: "Shafer & Vovk"
225	    year: 2008
226	    venue: "Journal of Machine Learning Research, 9:371-421"
227	    url: "https://jmlr.org/papers/v9/shafer08a.html"
228	    category: "cp_foundation"
229	    verified: true
230	    relevance: "Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA."
231	    must_cite: false
232	
233	  - bibtex_key: "shukor2025smolvla"
234	    title: "SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics"
235	    authors: "Shukor et al."
236	    year: 2025
237	    venue: "arXiv:2506.01844"
238	    url: "https://arxiv.org/abs/2506.01844"
239	    category: "vla_foundation"
240	    verified: true
241	    relevance: "450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments."
242	    must_cite: true
243	
244	  - bibtex_key: "srpo2025"
245	    title: "SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models"
246	    authors: "Fei et al."
247	    year: 2025
248	    venue: "arXiv:2511.15605"
249	    url: "https://arxiv.org/abs/2511.15605"
250	    category: "vla_robustness_training"
251	    verified: true
252	    relevance: "Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time."
253	    must_cite: true
254	
255	  - bibtex_key: "wang2025cploop"
256	    title: "Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization"
257	    authors: "Wang & Ning"
258	    year: 2025
259	    venue: "arXiv:2510.16376"
260	    url: "https://arxiv.org/abs/2510.16376"
261	    category: "cp_robotics"
262	    verified: true
263	    relevance: "Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning."
264	    must_cite: true
265	
266	  - bibtex_key: "xing2026diu"
267	    title: "Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching"
268	    authors: "Xing et al."
269	    year: 2026
270	    venue: "arXiv:2605.00941"
271	    url: "https://arxiv.org/abs/2605.00941"
272	    category: "uq_flow_matching"
273	    verified: true
274	    relevance: "Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage."
275	    must_cite: true
276	
277	  - bibtex_key: "yuan2026ups"
278	    title: "When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering"
279	    authors: "Yuan et al."
280	    year: 2026
281	    venue: "arXiv:2602.22474"
282	    url: "https://arxiv.org/abs/2602.22474"
283	    category: "inference_correction"
284	    verified: true
285	    relevance: "Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach."
286	    must_cite: true
287	
288	  - bibtex_key: "zhao2024conformalized"
289	    title: "Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions"
290	    authors: "Zhao et al."
291	    year: 2024
292	    venue: "RSS 2024"
293	    url: "https://arxiv.org/abs/2406.07767"
294	    category: "cp_robotics"
295	    verified: true
296	    relevance: "Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach."
297	    must_cite: true
298	
299	  - bibtex_key: "cosmos_policy_2026"
300	    title: "Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning"
301	    authors: "Kim et al."
302	    year: 2026
303	    venue: "arXiv:2601.16163"
304	    url: "https://arxiv.org/abs/2601.16163"
305	    category: "vla_foundation"
306	    verified: true
307	    relevance: "NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic."
308	    must_cite: false
309	
310	  - bibtex_key: "vla_gse_2026"
311	    title: "VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts"
312	    authors: "Jiang et al."
313	    year: 2026
314	    venue: "arXiv:2605.06175"
315	    url: "https://arxiv.org/abs/2605.06175"
316	    category: "vla_robustness_training"
317	    verified: true
318	    relevance: "Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach."
319	    must_cite: false
320	
321	  - bibtex_key: "lakshminarayanan2017ensembles"
322	    title: "Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles"
323	    authors: "Lakshminarayanan et al."
324	    year: 2017
325	    venue: "NeurIPS 2017"
326	    url: "https://arxiv.org/abs/1612.01474"
327	    category: "uq_foundation"
328	    verified: true
329	    relevance: "Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches."
330	    must_cite: false
331	
332	  - bibtex_key: "gal2016dropout"
333	    title: "Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning"
334	    authors: "Gal & Ghahramani"
335	    year: 2016
336	    venue: "ICML 2016"
337	    url: "https://arxiv.org/abs/1506.02142"
338	    category: "uq_foundation"
339	    verified: true
340	    relevance: "Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces."
341	    must_cite: false
342	
343	  - bibtex_key: "chi2023diffusion_policy"
344	    title: "Diffusion Policy: Visuomotor Policy Learning via Action Diffusion"
345	    authors: "Chi et al."
346	    year: 2023
347	    venue: "RSS 2023 / IJRR 2024"
348	    url: "https://arxiv.org/abs/2303.04137"
349	    category: "vla_foundation"
350	    verified: false
351	    verification_note: "Well-known paper, needs URL reachability confirmation"
352	    relevance: "Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits."
353	    must_cite: true
354	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "d0b3b42f-99ed-4959-98ba-b841e0a0960d",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
      "content": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n",
      "numLines": 354,
      "startLine": 1,
      "totalLines": 354
    }
  }
}
```

</details>

---

### Assistant

_source line 78_

<details><summary>Logged reasoning block</summary>

```text
Now I need to append new entries to this file. Let me compose the new entries and add them to the YAML. I'll use the Edit tool to append after the last entry.

Let me compile the final list of new papers to add:

1. **fan2025interpretable_multivariate_cp** - Interpretable Multivariate CP with Fast Transductive Standardization (2512.15383) - Very relevant for per-DOF methodology
2. **klein2025otcp** - Multivariate CP using Optimal Transport (2502.03609) - Background for multivariate CP
3. **zollo2025vla_calibration** - Confidence Calibration in VLA Models (2507.17383) - Directly relevant UQ for VLAs


4. **tang2026shifting_uncertainty** - Shifting Uncertainty to Critical Moments (2603.18342) - UQ for VLA
5. **lcp2025** - Learnable Conformal Prediction for Robotic Planning (2509.21955) - CP + robotics
6. **claps2025** - Lies We Can Trust: CLAPS (2512.10294) - CP + robot dynamics on Lie groups
7. **lucca2024** - LUCCa (2409.08249) - Local conformal calibration for dynamics
8. **sc_vla_2026** - Self-Correcting VLA (2602.21633) - Self-correction mechanisms for VLAs at inference time, and a couple other inference-time policy steering approaches like VLA-Pilot. Then there's chain-of-thought reasoning applied to VLAs, along with several papers combining conformal prediction with safe robotics and diffusion-based control. I'm also tracking failure-informed learning approaches and evaluation metrics for VLA uncertainty quantification.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "cd1f696a-9270-4166-abfa-25d60100b289",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqX8X8cYxyhgNNVDNkqjjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 57097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 79_

Now I'll append the 15 new entries to the literature map.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "6fb355a7-a005-47d2-8311-24c246e43537",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqX8X8cYxyhgNNVDNkqjjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 57097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 80_

<details open><summary>🔧 Tool call — Edit · `toolu_01Mi5gmzMY5dXbQy9g4H8XsD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
  "old_string": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true",
  "new_string": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "7769c7c8-1ce3-4469-b730-4d7abbb6a3be",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JqX8X8cYxyhgNNVDNkqjjJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 8174,
      "cache_read_input_tokens": 57097,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 8174
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

_source line 81 · 2026-05-14T03:20:19.697Z_

<details><summary>↩ Tool result · `toolu_01Mi5gmzMY5dXbQy9g4H8XsD`</summary>

```text
The file /home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml has been updated successfully.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "02674663-f1a1-4350-88c2-583367b2829a",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
    "oldString": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true",
    "newString": "  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"",
    "originalFile": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n",
    "structuredPatch": [
      {
        "oldStart": 351,
        "oldLines": 3,
        "newStart": 351,
        "newLines": 185,
        "lines": [
          "     verification_note: \"Well-known paper, needs URL reachability confirmation\"",
          "     relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"",
          "     must_cite: true",
          "+",
          "+  # ===== New entries added 2026-05-14 =====",
          "+",
          "+  - bibtex_key: \"fan2025interpretable_mcp\"",
          "+    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"",
          "+    authors: \"Fan & Sesia\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2512.15383\"",
          "+    url: \"https://arxiv.org/abs/2512.15383\"",
          "+    category: \"cp_foundation\"",
          "+    verified: true",
          "+    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"klein2025otcp\"",
          "+    title: \"Multivariate Conformal Prediction using Optimal Transport\"",
          "+    authors: \"Klein, Bethune, Ndiaye & Cuturi\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2502.03609\"",
          "+    url: \"https://arxiv.org/abs/2502.03609\"",
          "+    category: \"cp_foundation\"",
          "+    verified: true",
          "+    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"zollo2025vla_calibration\"",
          "+    title: \"Confidence Calibration in Vision-Language-Action Models\"",
          "+    authors: \"Zollo & Zemel\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2507.17383\"",
          "+    url: \"https://arxiv.org/abs/2507.17383\"",
          "+    category: \"uq_vla\"",
          "+    verified: true",
          "+    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"",
          "+    must_cite: true",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"tang2026shifting_uncertainty\"",
          "+    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"",
          "+    authors: \"Tang et al.\"",
          "+    year: 2026",
          "+    venue: \"arXiv:2603.18342\"",
          "+    url: \"https://arxiv.org/abs/2603.18342\"",
          "+    category: \"uq_vla\"",
          "+    verified: true",
          "+    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"lcp2025\"",
          "+    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"",
          "+    authors: \"Not specified\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2509.21955\"",
          "+    url: \"https://arxiv.org/abs/2509.21955\"",
          "+    category: \"cp_robotics\"",
          "+    verified: true",
          "+    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"claps2025\"",
          "+    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"",
          "+    authors: \"Not specified\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2512.10294\"",
          "+    url: \"https://arxiv.org/abs/2512.10294\"",
          "+    category: \"cp_robotics\"",
          "+    verified: true",
          "+    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"lucca2024\"",
          "+    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"",
          "+    authors: \"Marques et al.\"",
          "+    year: 2024",
          "+    venue: \"arXiv:2409.08249\"",
          "+    url: \"https://arxiv.org/abs/2409.08249\"",
          "+    category: \"cp_robotics\"",
          "+    verified: true",
          "+    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"sc_vla_2026\"",
          "+    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"",
          "+    authors: \"Li et al.\"",
          "+    year: 2026",
          "+    venue: \"arXiv:2602.21633\"",
          "+    url: \"https://arxiv.org/abs/2602.21633\"",
          "+    category: \"inference_correction\"",
          "+    verified: true",
          "+    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"",
          "+    must_cite: true",
          "+    relation: \"competitor\"",
          "+",
          "+  - bibtex_key: \"vla_pilot_2025\"",
          "+    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"",
          "+    authors: \"Not specified\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2511.14178\"",
          "+    url: \"https://arxiv.org/abs/2511.14178\"",
          "+    category: \"inference_correction\"",
          "+    verified: true",
          "+    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"",
          "+    must_cite: true",
          "+    relation: \"competitor\"",
          "+",
          "+  - bibtex_key: \"acot_vla_2026\"",
          "+    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"",
          "+    authors: \"AgibotTech\"",
          "+    year: 2026",
          "+    venue: \"CVPR 2026, arXiv:2601.11404\"",
          "+    url: \"https://arxiv.org/abs/2601.11404\"",
          "+    category: \"vla_robustness_training\"",
          "+    verified: true",
          "+    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"gonzales2026crc_cbf\"",
          "+    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"",
          "+    authors: \"Gonzales et al.\"",
          "+    year: 2026",
          "+    venue: \"IROS 2025, arXiv:2603.10392\"",
          "+    url: \"https://arxiv.org/abs/2603.10392\"",
          "+    category: \"cp_robotics\"",
          "+    verified: true",
          "+    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"",
          "+    must_cite: false",
          "+    relation: \"background\"",
          "+",
          "+  - bibtex_key: \"safediffcon2025\"",
          "+    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"",
          "+    authors: \"Not specified\"",
          "+    year: 2025",
          "+    venue: \"ICML 2025, arXiv:2502.02205\"",
          "+    url: \"https://arxiv.org/abs/2502.02205\"",
          "+    category: \"cp_foundation\"",
          "+    verified: true",
          "+    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"",
          "+    must_cite: false",
          "+    relation: \"background\"",
          "+",
          "+  - bibtex_key: \"afil2026\"",
          "+    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"",
          "+    authors: \"Not specified\"",
          "+    year: 2026",
          "+    venue: \"arXiv:2605.08434\"",
          "+    url: \"https://arxiv.org/abs/2605.08434\"",
          "+    category: \"vla_robustness_training\"",
          "+    verified: true",
          "+    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"valle2025vla_uq_metrics\"",
          "+    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"",
          "+    authors: \"Valle et al.\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2507.17049\"",
          "+    url: \"https://arxiv.org/abs/2507.17049\"",
          "+    category: \"uq_vla\"",
          "+    verified: true",
          "+    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"",
          "+    must_cite: false",
          "+    relation: \"complementary\"",
          "+",
          "+  - bibtex_key: \"diffusionvla2024\"",
          "+    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"",
          "+    authors: \"Wen et al.\"",
          "+    year: 2024",
          "+    venue: \"ICML 2025, arXiv:2412.03293\"",
          "+    url: \"https://arxiv.org/abs/2412.03293\"",
          "+    category: \"vla_foundation\"",
          "+    verified: true",
          "+    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"",
          "+    must_cite: false",
          "+    relation: \"background\""
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

### Tool call

_source line 82_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_019sBcv8c7AHNFa946ZoMnEy`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__save_project_file",
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
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "0256211f-1cef-4d37-b4f5-e444aa02eeac",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016Tq72t5YAhUM8vARnJAjSP",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4001,
      "cache_read_input_tokens": 65271,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 4001
      },
      "output_tokens": 34,
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

_source line 83 · 2026-05-14T03:20:23.508Z_

<details><summary>↩ Tool result · `toolu_019sBcv8c7AHNFa946ZoMnEy`</summary>

````text
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
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "14f16a38-2766-41a3-9e0c-5adc5ae565f2",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 84_

<details><summary>Logged reasoning block</summary>

```text
The save_project_file tool only supports memory.md, writing_plan.yaml, and paper_framing.md. literature_map.yaml is not in the whitelist. But I already edited the file directly using the Edit tool, so it's already saved. Let me verify the edit was successful by reading the file.

Actually, let me just verify the file looks correct by reading the end of it.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "0469ac31-9204-42e6-8941-9bce69209431",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8swMTEf7HjwmcJFhkhTT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 69272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 28,
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

_source line 85_

<details open><summary>🔧 Tool call — Read · `toolu_01DzWLSsy3kwLde2Z2m9Hfnd`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
  "offset": 350
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "7f1388c4-34aa-4a1d-8cb3-744ea3423ddf",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S8swMTEf7HjwmcJFhkhTT7",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 363,
      "cache_read_input_tokens": 69272,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 363
      },
      "output_tokens": 28,
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

_source line 86 · 2026-05-14T03:20:30.435Z_

<details><summary>↩ Tool result · `toolu_01DzWLSsy3kwLde2Z2m9Hfnd`</summary>

```text
350	    verified: false
351	    verification_note: "Well-known paper, needs URL reachability confirmation"
352	    relevance: "Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits."
353	    must_cite: true
354	
355	  # ===== New entries added 2026-05-14 =====
356	
357	  - bibtex_key: "fan2025interpretable_mcp"
358	    title: "Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization"
359	    authors: "Fan & Sesia"
360	    year: 2025
361	    venue: "arXiv:2512.15383"
362	    url: "https://arxiv.org/abs/2512.15383"
363	    category: "cp_foundation"
364	    verified: true
365	    relevance: "Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations."
366	    must_cite: false
367	    relation: "complementary"
368	
369	  - bibtex_key: "klein2025otcp"
370	    title: "Multivariate Conformal Prediction using Optimal Transport"
371	    authors: "Klein, Bethune, Ndiaye & Cuturi"
372	    year: 2025
373	    venue: "arXiv:2502.03609"
374	    url: "https://arxiv.org/abs/2502.03609"
375	    category: "cp_foundation"
376	    verified: true
377	    relevance: "Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces."
378	    must_cite: false
379	    relation: "complementary"
380	
381	  - bibtex_key: "zollo2025vla_calibration"
382	    title: "Confidence Calibration in Vision-Language-Action Models"
383	    authors: "Zollo & Zemel"
384	    year: 2025
385	    venue: "arXiv:2507.17383"
386	    url: "https://arxiv.org/abs/2507.17383"
387	    category: "uq_vla"
388	    verified: true
389	    relevance: "First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against."
390	    must_cite: true
391	    relation: "complementary"
392	
393	  - bibtex_key: "tang2026shifting_uncertainty"
394	    title: "Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model"
395	    authors: "Tang et al."
396	    year: 2026
397	    venue: "arXiv:2603.18342"
398	    url: "https://arxiv.org/abs/2603.18342"
399	    category: "uq_vla"
400	    verified: true
401	    relevance: "Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring."
402	    must_cite: false
403	    relation: "complementary"
404	
405	  - bibtex_key: "lcp2025"
406	    title: "Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception"
407	    authors: "Not specified"
408	    year: 2025
409	    venue: "arXiv:2509.21955"
410	    url: "https://arxiv.org/abs/2509.21955"
411	    category: "cp_robotics"
412	    verified: true
413	    relevance: "Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics."
414	    must_cite: false
415	    relation: "complementary"
416	
417	  - bibtex_key: "claps2025"
418	    title: "Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups"
419	    authors: "Not specified"
420	    year: 2025
421	    venue: "arXiv:2512.10294"
422	    url: "https://arxiv.org/abs/2512.10294"
423	    category: "cp_robotics"
424	    verified: true
425	    relevance: "Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones."
426	    must_cite: false
427	    relation: "complementary"
428	
429	  - bibtex_key: "lucca2024"
430	    title: "Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration"
431	    authors: "Marques et al."
432	    year: 2024
433	    venue: "arXiv:2409.08249"
434	    url: "https://arxiv.org/abs/2409.08249"
435	    category: "cp_robotics"
436	    verified: true
437	    relevance: "Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty."
438	    must_cite: false
439	    relation: "complementary"
440	
441	  - bibtex_key: "sc_vla_2026"
442	    title: "Self-Correcting VLA: Online Action Refinement via Sparse World Imagination"
443	    authors: "Li et al."
444	    year: 2026
445	    venue: "arXiv:2602.21633"
446	    url: "https://arxiv.org/abs/2602.21633"
447	    category: "inference_correction"
448	    verified: true
449	    relevance: "Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction."
450	    must_cite: true
451	    relation: "competitor"
452	
453	  - bibtex_key: "vla_pilot_2025"
454	    title: "Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion"
455	    authors: "Not specified"
456	    year: 2025
457	    venue: "arXiv:2511.14178"
458	    url: "https://arxiv.org/abs/2511.14178"
459	    category: "inference_correction"
460	    verified: true
461	    relevance: "VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees."
462	    must_cite: true
463	    relation: "competitor"
464	
465	  - bibtex_key: "acot_vla_2026"
466	    title: "ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models"
467	    authors: "AgibotTech"
468	    year: 2026
469	    venue: "CVPR 2026, arXiv:2601.11404"
470	    url: "https://arxiv.org/abs/2601.11404"
471	    category: "vla_robustness_training"
472	    verified: true
473	    relevance: "Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning."
474	    must_cite: false
475	    relation: "complementary"
476	
477	  - bibtex_key: "gonzales2026crc_cbf"
478	    title: "Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control"
479	    authors: "Gonzales et al."
480	    year: 2026
481	    venue: "IROS 2025, arXiv:2603.10392"
482	    url: "https://arxiv.org/abs/2603.10392"
483	    category: "cp_robotics"
484	    verified: true
485	    relevance: "Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control."
486	    must_cite: false
487	    relation: "background"
488	
489	  - bibtex_key: "safediffcon2025"
490	    title: "From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control"
491	    authors: "Not specified"
492	    year: 2025
493	    venue: "ICML 2025, arXiv:2502.02205"
494	    url: "https://arxiv.org/abs/2502.02205"
495	    category: "cp_foundation"
496	    verified: true
497	    relevance: "SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach."
498	    must_cite: false
499	    relation: "background"
500	
501	  - bibtex_key: "afil2026"
502	    title: "Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models"
503	    authors: "Not specified"
504	    year: 2026
505	    venue: "arXiv:2605.08434"
506	    url: "https://arxiv.org/abs/2605.08434"
507	    category: "vla_robustness_training"
508	    verified: true
509	    relevance: "AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction."
510	    must_cite: false
511	    relation: "complementary"
512	
513	  - bibtex_key: "valle2025vla_uq_metrics"
514	    title: "Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots"
515	    authors: "Valle et al."
516	    year: 2025
517	    venue: "arXiv:2507.17049"
518	    url: "https://arxiv.org/abs/2507.17049"
519	    category: "uq_vla"
520	    verified: true
521	    relevance: "Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against."
522	    must_cite: false
523	    relation: "complementary"
524	
525	  - bibtex_key: "diffusionvla2024"
526	    title: "Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning"
527	    authors: "Wen et al."
528	    year: 2024
529	    venue: "ICML 2025, arXiv:2412.03293"
530	    url: "https://arxiv.org/abs/2412.03293"
531	    category: "vla_foundation"
532	    verified: true
533	    relevance: "Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around."
534	    must_cite: false
535	    relation: "background"
536	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "18facf50-7744-4c46-80a5-be57841bad23",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
      "content": "    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n",
      "numLines": 187,
      "startLine": 350,
      "totalLines": 536
    }
  }
}
```

</details>

---

### Assistant

_source line 87_

文件已更新。总结如下：

## 扫描结果

**新增 15 篇论文**（31 → 46 篇），覆盖 4 个搜索方向：

### 竞争者（2 篇，需重点关注）
- **SC-VLA** (2602.21633) — 在线 action refinement via sparse world imagination + residual RL，9% 成功率提升。与 ACR-VLA 同属 inference-time correction，但用 RL 而非统计方法
- **VLA-Pilot** (2511.14178) — Plug-and-play inference-time policy steering，用 MLLM 做 verifier + evolutionary diffusion 做 action optimizer。同属 zero-shot inference-time 方法，但无统计保证

### CP + 机器人 / 多维 CP（6 篇）
- **Fan & Sesia 2025** — 坐标级标准化做多维 CP，与我们的 per-DOF 方法论直接相关
- **OTCP** (Klein et al.) — 最优传输做多维 CP scoring
- **LCP** (2509.21955) — 可学习 nonconformity function 用于机器人规划
- **CLAPS** (2512.10294) — Lie 群上的 conformalized action prediction sets
- **LUCCa** (2409.08249) — 状态-动作空间的局部 conformal 校准
- **CRC-CBF** (2603.10392) — Conformal risk control + CBF 用于 HRI 安全

### VLA 不确定性量化（3 篇）
- **Zollo & Zemel 2025** — 首个 VLA 置信度校准研究（prompt ensembles + Platt scaling）
- **Tang et al. 2026** — "Averaging Trap" 问题，max-pooling 捕捉关键时刻不确定性
- **Valle et al. 2025** — 8 个不确定性指标 + 5 个质量指标的 VLA 评估框架

### VLA 架构 / 训练（4 篇）
- **ACoT-VLA** (CVPR 2026) — Action chain-of-thought，LIBERO-Plus 84.1%
- **AFIL** (2605.08434) — 失败轨迹作为负向引导
- **SafeDiffCon** (ICML 2025) — CP + 扩散模型安全控制
- **DiffusionVLA** (ICML 2025) — 自回归推理 + 扩散策略

### 直接竞争者分析
**未发现做 per-DOF conformal + VLA 的工作。** 最近的是 ReconVLA（已收录），它用 CQR 做 scalar action-level uncertainty，而非我们的 per-DOF 分解。SC-VLA 和 VLA-Pilot 做 inference-time correction 但不用 conformal prediction。**ACR-VLA 的 per-DOF conformal statistics 创新点仍然成立。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "uuid": "26ad87d7-a1dd-408e-a6dd-2a67c19e704a",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nw2Y6bnnJmyyrEF6j43T6G",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3461,
      "cache_read_input_tokens": 69635,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 3461
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

_source line 88_

文件已更新。总结如下：

## 扫描结果

**新增 15 篇论文**（31 → 46 篇），覆盖 4 个搜索方向：

### 竞争者（2 篇，需重点关注）
- **SC-VLA** (2602.21633) — 在线 action refinement via sparse world imagination + residual RL，9% 成功率提升。与 ACR-VLA 同属 inference-time correction，但用 RL 而非统计方法
- **VLA-Pilot** (2511.14178) — Plug-and-play inference-time policy steering，用 MLLM 做 verifier + evolutionary diffusion 做 action optimizer。同属 zero-shot inference-time 方法，但无统计保证

### CP + 机器人 / 多维 CP（6 篇）
- **Fan & Sesia 2025** — 坐标级标准化做多维 CP，与我们的 per-DOF 方法论直接相关
- **OTCP** (Klein et al.) — 最优传输做多维 CP scoring
- **LCP** (2509.21955) — 可学习 nonconformity function 用于机器人规划
- **CLAPS** (2512.10294) — Lie 群上的 conformalized action prediction sets
- **LUCCa** (2409.08249) — 状态-动作空间的局部 conformal 校准
- **CRC-CBF** (2603.10392) — Conformal risk control + CBF 用于 HRI 安全

### VLA 不确定性量化（3 篇）
- **Zollo & Zemel 2025** — 首个 VLA 置信度校准研究（prompt ensembles + Platt scaling）
- **Tang et al. 2026** — "Averaging Trap" 问题，max-pooling 捕捉关键时刻不确定性
- **Valle et al. 2025** — 8 个不确定性指标 + 5 个质量指标的 VLA 评估框架

### VLA 架构 / 训练（4 篇）
- **ACoT-VLA** (CVPR 2026) — Action chain-of-thought，LIBERO-Plus 84.1%
- **AFIL** (2605.08434) — 失败轨迹作为负向引导
- **SafeDiffCon** (ICML 2025) — CP + 扩散模型安全控制
- **DiffusionVLA** (ICML 2025) — 自回归推理 + 扩散策略

### 直接竞争者分析
**未发现做 per-DOF conformal + VLA 的工作。** 最近的是 ReconVLA（已收录），它用 CQR 做 scalar action-level uncertainty，而非我们的 per-DOF 分解。SC-VLA 和 VLA-Pilot 做 inference-time correction 但不用 conformal prediction。**ACR-VLA 的 per-DOF conformal statistics 创新点仍然成立。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 269314,
  "duration_api_ms": 410921,
  "num_turns": 34,
  "stop_reason": "end_turn",
  "session_id": "851f4528-2897-48c5-bc73-79d97f71e12f",
  "total_cost_usd": 1.7107877500000004,
  "usage": {
    "input_tokens": 3590,
    "cache_creation_input_tokens": 61255,
    "cache_read_input_tokens": 631260,
    "output_tokens": 9324,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 61255,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 847,
        "cache_read_input_tokens": 69635,
        "cache_creation_input_tokens": 3461,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 3461
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 423804,
      "outputTokens": 13492,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 27,
      "costUSD": 0.7612639999999998,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 3590,
      "outputTokens": 9324,
      "cacheReadInputTokens": 631260,
      "cacheCreationInputTokens": 61255,
      "webSearchRequests": 0,
      "costUSD": 0.9495237500000001,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "51f50bd6-07e2-43f7-ac24-95f153d14b27"
}
```

</details>

---
