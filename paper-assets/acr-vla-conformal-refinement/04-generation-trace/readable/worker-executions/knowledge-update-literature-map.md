# knowledge update literature map

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Worker execution logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 19
- **Recorded user turns:** 0
- **Tool calls:** 5
- **Original source:** `logs/workers/worker_knowledge_update-literature-map_20260514T183927.log`
- **Structured JSON:** [`0ae26fbe6b0fad8b597f.json`](../../sessions/0a/0ae26fbe6b0fad8b597f.json)

## Before a recorded user message

19 recorded events

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
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
  "uuid": "8eac54ba-c76e-4fd4-8365-a8fb72b2ad6f",
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
    "resetsAt": 1778798400,
    "rateLimitType": "five_hour",
    "overageStatus": "rejected",
    "overageDisabledReason": "org_level_disabled",
    "isUsingOverage": false
  },
  "uuid": "707fe108-6084-4c54-9daf-44f355a08570",
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285"
}
```

---

### Assistant

_source line 4_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to update the literature_map.yaml file by adding 12 papers related to correction magnitude control. Let me start by reading the current file.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "759e8fdb-d1f7-49cb-8fa8-36fed318b176",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWn2RLiMEYP17ahvPtqzCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11620
      },
      "output_tokens": 42,
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

<details open><summary>🔧 Tool call — ToolSearch · `toolu_016Pu5SoZBQ6ZgeAtmhDPDM2`</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "fe2d4891-62f9-41d8-97b2-4b937716c808",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01BWn2RLiMEYP17ahvPtqzCJ",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11620,
      "cache_read_input_tokens": 11841,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 11620
      },
      "output_tokens": 42,
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

_source line 6 · 2026-05-14T18:39:38.979Z_

<details><summary>↩ Tool result · `toolu_016Pu5SoZBQ6ZgeAtmhDPDM2`</summary>

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "9a634882-2c04-4cb2-be0b-83b528ffb1cd",
  "tool_use_result": {
    "matches": [
      "mcp__agent-ml-research__read_project_file",
      "mcp__agent-ml-research__save_project_file"
    ],
    "query": "select:mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__save_project_file",
    "total_deferred_tools": 22
  }
}
```

</details>

---

### Assistant

_source line 7_

读取当前 literature_map.yaml。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "63abc926-2163-48a0-b72f-479ed9e51834",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJmM3UuMf84s51qPtmiqqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 23461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 8_

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file · `toolu_012mEWseVXNt2MFkQ81QYDC1`</summary>

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "d7de6c67-6882-416e-baff-dd9838ea24ee",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KJmM3UuMf84s51qPtmiqqH",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 747,
      "cache_read_input_tokens": 23461,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 747
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

_source line 9 · 2026-05-14T18:39:42.289Z_

<details><summary>↩ Tool result · `toolu_012mEWseVXNt2MFkQ81QYDC1`</summary>

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "48ae49e4-d8cd-4754-9472-a17fb469781e",
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

### Assistant

_source line 10_

<details><summary>Logged reasoning block</summary>

```text
Now I have the current literature_map.yaml. I need to check which of the 12 papers are already present. Let me scan:

Already present:
- A2C2 (a2c2_2025) - already exists
- SC-VLA (sc_vla_2026) - already exists
- SafeDiffCon (safediffcon2025) - already exists

Not present (need to add):
1. Silver et al. "Residual Policy Learning" RSS 2018 — 1812.06298
2. Johannink et al. 

Looking at the remaining papers to add: Johannink's residual RL work from ICRA 2019, Jiang's TRANSIC from CoRL 2024, Ankile's ResiP from CoRL-W 2024, Xiao's PLD from ICLR 2026, Pan's DRC from arXiv 2025, Ma's DAWN from arXiv 2026, and several others that are partially listed.

I'm realizing that `save_project_file` has a whitelist that doesn't include literature_map.yaml, so I'll need to output the YAML directly for manual addition or find another way to write it to the file path.

Actually, I can use the Edit tool to append the 9 new papers directly to the existing literature_map.yaml file. I'll add them after the last entry, formatting them consistently with the existing style.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "74ea7e93-8f9b-4361-b6c8-2f6c85914f66",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNLS1bvfJX1yswC2SpC1Yn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9795,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9795
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

3 篇已存在（A2C2、SC-VLA、SafeDiffCon），需添加 9 篇。`save_project_file` 白名单不含 literature_map.yaml，直接编辑文件。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "9156ab3a-a74f-4494-b346-156a85f96bb3",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNLS1bvfJX1yswC2SpC1Yn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9795,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9795
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

<details open><summary>🔧 Tool call — Edit · `toolu_013J1CbBHUaWBREaWc7EsjJE`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
  "old_string": "  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"",
  "new_string": "  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\n\n  - bibtex_key: \"silver2018residual\"\n    title: \"Residual Policy Learning\"\n    authors: \"Silver et al.\"\n    year: 2018\n    venue: \"RSS 2018\"\n    url: \"https://arxiv.org/abs/1812.06298\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"johannink2019residual\"\n    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"\n    authors: \"Johannink et al.\"\n    year: 2019\n    venue: \"ICRA 2019\"\n    url: \"https://arxiv.org/abs/1812.03201\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"jiang2024transic\"\n    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"\n    authors: \"Jiang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2405.10315\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"ankile2024resip\"\n    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"\n    authors: \"Ankile et al.\"\n    year: 2024\n    venue: \"CoRL Workshop 2024\"\n    url: \"\"\n    category: \"residual_policy\"\n    verified: false\n    verification_note: \"Workshop paper, no arXiv ID provided\"\n    relevance: \"Introduces scaling coefficient α≤1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"xiao2026pld\"\n    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"\n    authors: \"Xiao et al.\"\n    year: 2026\n    venue: \"ICLR 2026\"\n    url: \"https://arxiv.org/abs/2511.00091\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Scheduled magnitude bound ξ for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"pan2025drc\"\n    title: \"DRC: Decaying Relative Correction for Policy Refinement\"\n    authors: \"Pan et al.\"\n    year: 2025\n    venue: \"arXiv:2503.15368\"\n    url: \"https://arxiv.org/abs/2503.15368\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"ma2026dawn\"\n    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"\n    authors: \"Ma et al.\"\n    year: 2026\n    venue: \"arXiv:2602.10539\"\n    url: \"https://arxiv.org/abs/2602.10539\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"vla_in_the_loop_2025\"\n    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv 2025\"\n    url: \"\"\n    category: \"inference_correction\"\n    verified: false\n    verification_note: \"No arXiv ID provided, needs verification\"\n    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"zhou2025acp_cbf\"\n    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    year: 2025\n    venue: \"ICRA 2025\"\n    url: \"https://arxiv.org/abs/2503.17678\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"\n    must_cite: true\n    relation: \"method-component\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "4faa5a21-286d-4f49-9045-721b2a2876f8",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XNLS1bvfJX1yswC2SpC1Yn",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9795,
      "cache_read_input_tokens": 24208,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9795
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

_source line 13 · 2026-05-14T18:40:25.885Z_

<details><summary>↩ Tool result · reported error · `toolu_013J1CbBHUaWBREaWc7EsjJE`</summary>

```text
&lt;tool_use_error>File has not been read yet. Read it first before writing to it.&lt;/tool_use_error>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "type": "user",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "ca463fb4-e235-4720-a3a1-bfe8cf00e39b",
  "tool_use_result": "Error: File has not been read yet. Read it first before writing to it."
}
```

</details>

---

### Tool call

_source line 14_

<details open><summary>🔧 Tool call — Read · `toolu_01EdA3BTTkHEEcTAMLzwFs5k`</summary>

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "617157e6-75b0-43d7-afde-a2a75608989c",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016BUw9Av1a3JZ83GotBbh5c",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2768,
      "cache_read_input_tokens": 34003,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2768
      },
      "output_tokens": 69,
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

_source line 15 · 2026-05-14T18:40:29.107Z_

<details><summary>↩ Tool result · `toolu_01EdA3BTTkHEEcTAMLzwFs5k`</summary>

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "c5f0ebd7-f67c-495b-9ed2-2766b41d08ef",
  "tool_use_result": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
      "content": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n",
      "numLines": 536,
      "startLine": 1,
      "totalLines": 536
    }
  }
}
```

</details>

---

### Tool call

_source line 16_

<details open><summary>🔧 Tool call — Edit · `toolu_01BGyGMxzuNaFW74qVnfigMD`</summary>

```json
{
  "replace_all": false,
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
  "old_string": "  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"",
  "new_string": "  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\n\n  - bibtex_key: \"silver2018residual\"\n    title: \"Residual Policy Learning\"\n    authors: \"Silver et al.\"\n    year: 2018\n    venue: \"RSS 2018\"\n    url: \"https://arxiv.org/abs/1812.06298\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"johannink2019residual\"\n    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"\n    authors: \"Johannink et al.\"\n    year: 2019\n    venue: \"ICRA 2019\"\n    url: \"https://arxiv.org/abs/1812.03201\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"jiang2024transic\"\n    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"\n    authors: \"Jiang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2405.10315\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"ankile2024resip\"\n    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"\n    authors: \"Ankile et al.\"\n    year: 2024\n    venue: \"CoRL Workshop 2024\"\n    url: \"\"\n    category: \"residual_policy\"\n    verified: false\n    verification_note: \"Workshop paper, no arXiv ID provided\"\n    relevance: \"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"xiao2026pld\"\n    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"\n    authors: \"Xiao et al.\"\n    year: 2026\n    venue: \"ICLR 2026\"\n    url: \"https://arxiv.org/abs/2511.00091\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"pan2025drc\"\n    title: \"DRC: Decaying Relative Correction for Policy Refinement\"\n    authors: \"Pan et al.\"\n    year: 2025\n    venue: \"arXiv:2503.15368\"\n    url: \"https://arxiv.org/abs/2503.15368\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"ma2026dawn\"\n    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"\n    authors: \"Ma et al.\"\n    year: 2026\n    venue: \"arXiv:2602.10539\"\n    url: \"https://arxiv.org/abs/2602.10539\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"vla_in_the_loop_2025\"\n    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv 2025\"\n    url: \"\"\n    category: \"inference_correction\"\n    verified: false\n    verification_note: \"No arXiv ID provided, needs verification\"\n    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"zhou2025acp_cbf\"\n    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    year: 2025\n    venue: \"ICRA 2025\"\n    url: \"https://arxiv.org/abs/2503.17678\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"\n    must_cite: true\n    relation: \"method-component\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "fb9de991-9c82-4026-b9c4-764e0cb97215",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Xm7zgVwVBqKDNPD6EBVQKd",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 9084,
      "cache_read_input_tokens": 36771,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 9084
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

_source line 17 · 2026-05-14T18:41:01.777Z_

<details><summary>↩ Tool result · `toolu_01BGyGMxzuNaFW74qVnfigMD`</summary>

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
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "ba0b70dc-0f64-43f6-bbc3-0e5586f3731f",
  "tool_use_result": {
    "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0509_8/projects/acr-vla-conformal-refinement/literature_map.yaml",
    "oldString": "  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"",
    "newString": "  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n\n  # ===== Correction Magnitude Control literature (added 2026-05-14) =====\n\n  - bibtex_key: \"silver2018residual\"\n    title: \"Residual Policy Learning\"\n    authors: \"Silver et al.\"\n    year: 2018\n    venue: \"RSS 2018\"\n    url: \"https://arxiv.org/abs/1812.06298\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"\n    must_cite: true\n    relation: \"background\"\n\n  - bibtex_key: \"johannink2019residual\"\n    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"\n    authors: \"Johannink et al.\"\n    year: 2019\n    venue: \"ICRA 2019\"\n    url: \"https://arxiv.org/abs/1812.03201\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"jiang2024transic\"\n    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"\n    authors: \"Jiang et al.\"\n    year: 2024\n    venue: \"CoRL 2024\"\n    url: \"https://arxiv.org/abs/2405.10315\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"ankile2024resip\"\n    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"\n    authors: \"Ankile et al.\"\n    year: 2024\n    venue: \"CoRL Workshop 2024\"\n    url: \"\"\n    category: \"residual_policy\"\n    verified: false\n    verification_note: \"Workshop paper, no arXiv ID provided\"\n    relevance: \"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"xiao2026pld\"\n    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"\n    authors: \"Xiao et al.\"\n    year: 2026\n    venue: \"ICLR 2026\"\n    url: \"https://arxiv.org/abs/2511.00091\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"\n    must_cite: true\n    relation: \"direct-competitor\"\n\n  - bibtex_key: \"pan2025drc\"\n    title: \"DRC: Decaying Relative Correction for Policy Refinement\"\n    authors: \"Pan et al.\"\n    year: 2025\n    venue: \"arXiv:2503.15368\"\n    url: \"https://arxiv.org/abs/2503.15368\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"ma2026dawn\"\n    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"\n    authors: \"Ma et al.\"\n    year: 2026\n    venue: \"arXiv:2602.10539\"\n    url: \"https://arxiv.org/abs/2602.10539\"\n    category: \"residual_policy\"\n    verified: true\n    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"vla_in_the_loop_2025\"\n    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv 2025\"\n    url: \"\"\n    category: \"inference_correction\"\n    verified: false\n    verification_note: \"No arXiv ID provided, needs verification\"\n    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"\n    must_cite: false\n    relation: \"method-component\"\n\n  - bibtex_key: \"zhou2025acp_cbf\"\n    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"\n    authors: \"Zhou et al.\"\n    year: 2025\n    venue: \"ICRA 2025\"\n    url: \"https://arxiv.org/abs/2503.17678\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"\n    must_cite: true\n    relation: \"method-component\"",
    "originalFile": "papers:\n  - bibtex_key: \"a2c2_2025\"\n    title: \"Leave No Observation Behind: Real-time Correction for VLA Action Chunks\"\n    authors: \"Sendai et al.\"\n    year: 2025\n    venue: \"arXiv:2509.23224\"\n    url: \"https://arxiv.org/abs/2509.23224\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Proposes A2C2, a lightweight asynchronous action chunk correction head for VLAs. Directly comparable inference-time residual correction approach to ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"angelopoulos2023gentle\"\n    title: \"A Gentle Introduction to Conformal Prediction and Distribution-Free Uncertainty Quantification\"\n    authors: \"Angelopoulos & Bates\"\n    year: 2023\n    venue: \"Foundations and Trends in Machine Learning\"\n    url: \"https://arxiv.org/abs/2107.07511\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Canonical tutorial on conformal prediction. Provides theoretical grounding for CGS, ACI, and CQR components used in ACR-VLA.\"\n    must_cite: true\n\n  - bibtex_key: \"barber2023conformal\"\n    title: \"Conformal Prediction Beyond Exchangeability\"\n    authors: \"Barber et al.\"\n    year: 2023\n    venue: \"Annals of Statistics, 51(2):816-845\"\n    url: \"https://arxiv.org/abs/2202.13415\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Generalizes conformal prediction to non-exchangeable settings via weighted quantiles. Theoretical basis for ACR-VLA's handling of distribution shift in online deployment.\"\n    must_cite: false\n\n  - bibtex_key: \"black2024pi0\"\n    title: \"pi0: A Vision-Language-Action Flow Model for General Robot Control\"\n    authors: \"Black et al.\"\n    year: 2024\n    venue: \"arXiv:2410.24164\"\n    url: \"https://arxiv.org/abs/2410.24164\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Foundational flow-matching VLA architecture. ACR-VLA's multi-sample inference builds on the flow-matching action generation paradigm pioneered by pi0.\"\n    must_cite: false\n\n  - bibtex_key: \"braun2025cgs\"\n    title: \"Multivariate Conformal Prediction via Conformalized Gaussian Scoring\"\n    authors: \"Braun et al.\"\n    year: 2025\n    venue: \"arXiv:2507.20941\"\n    url: \"https://arxiv.org/abs/2507.20941\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Introduces Conformalized Gaussian Scoring (CGS) for multivariate conformal prediction with Mahalanobis-based scores. Direct theoretical basis for ACR-VLA's CGS component.\"\n    must_cite: true\n\n  - bibtex_key: \"brohan2023rt2\"\n    title: \"RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control\"\n    authors: \"Brohan et al.\"\n    year: 2023\n    venue: \"arXiv:2307.15818\"\n    url: \"https://arxiv.org/abs/2307.15818\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Seminal VLA work demonstrating web-scale vision-language pretraining transfer to robotic control. Establishes the VLA paradigm that ACR-VLA builds upon.\"\n    must_cite: false\n\n  - bibtex_key: \"chen2026reconvla\"\n    title: \"ReconVLA: An Uncertainty-Guided and Failure-Aware Vision-Language-Action Framework for Robotic Control\"\n    authors: \"Chen et al.\"\n    year: 2026\n    venue: \"arXiv:2604.16677\"\n    url: \"https://arxiv.org/abs/2604.16677\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Applies conformal prediction to VLA action outputs for calibrated uncertainty estimation and failure detection. Closest comparison for ACR-VLA's per-DOF conformal approach.\"\n    must_cite: true\n\n  - bibtex_key: \"digflow2025\"\n    title: \"DiG-Flow: Discrepancy-Guided Flow Matching for Robust VLA Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2512.01715\"\n    url: \"https://arxiv.org/abs/2512.01715\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Training-time geometric regularization for VLA robustness via representation-level discrepancy guidance. Complementary training-time approach vs ACR-VLA's inference-time correction.\"\n    must_cite: true\n\n  - bibtex_key: \"fei2025liberoplus\"\n    title: \"LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2510.13626\"\n    url: \"https://arxiv.org/abs/2510.13626\"\n    category: \"other\"\n    verified: true\n    relevance: \"Robustness benchmark with 7 perturbation dimensions for VLA evaluation. Primary evaluation benchmark for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"ghosh2024octo\"\n    title: \"Octo: An Open-Source Generalist Robot Policy\"\n    authors: \"Ghosh et al.\"\n    year: 2024\n    venue: \"arXiv:2405.12213\"\n    url: \"https://arxiv.org/abs/2405.12213\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source generalist robot policy trained on Open X-Embodiment. Representative VLA baseline for contextualizing ACR-VLA's contribution.\"\n    must_cite: false\n\n  - bibtex_key: \"gibbs2021aci\"\n    title: \"Adaptive Conformal Inference Under Distribution Shift\"\n    authors: \"Gibbs & Candès\"\n    year: 2021\n    venue: \"NeurIPS 2021\"\n    url: \"https://arxiv.org/abs/2106.00170\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Proposes ACI for online conformal prediction under distribution shift. Directly used in ACR-VLA's ACI+COC component for adaptive threshold adjustment.\"\n    must_cite: true\n\n  - bibtex_key: \"gu2025safe\"\n    title: \"SAFE: Multitask Failure Detection for Vision-Language-Action Models\"\n    authors: \"Gu et al.\"\n    year: 2025\n    venue: \"NeurIPS 2025\"\n    url: \"https://arxiv.org/abs/2506.09937\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA failure detector using internal features and conformal prediction for detection timing. Comparison point for ACR-VLA's anomaly-aware approach.\"\n    must_cite: true\n\n  - bibtex_key: \"kim2024openvla\"\n    title: \"OpenVLA: An Open-Source Vision-Language-Action Model\"\n    authors: \"Kim et al.\"\n    year: 2024\n    venue: \"arXiv:2406.09246\"\n    url: \"https://arxiv.org/abs/2406.09246\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Open-source 7B VLA trained on 970k demonstrations. Key VLA baseline and potential backbone for ACR-VLA integration.\"\n    must_cite: false\n\n  - bibtex_key: \"ledoit2004well\"\n    title: \"A Well-Conditioned Estimator for Large-Dimensional Covariance Matrices\"\n    authors: \"Ledoit & Wolf\"\n    year: 2004\n    venue: \"Journal of Multivariate Analysis, 88(2):365-411\"\n    url: \"https://www.sciencedirect.com/science/article/pii/S0047259X03000964\"\n    category: \"other\"\n    verified: true\n    relevance: \"Shrinkage covariance estimation method. Used in ACR-VLA's CGS component for robust covariance estimation from limited action samples.\"\n    must_cite: false\n\n  - bibtex_key: \"lipman2023flow\"\n    title: \"Flow Matching for Generative Modeling\"\n    authors: \"Lipman et al.\"\n    year: 2023\n    venue: \"ICLR 2023\"\n    url: \"https://arxiv.org/abs/2210.02747\"\n    category: \"other\"\n    verified: true\n    relevance: \"Foundational flow matching paper. Establishes the generative framework underlying flow-matching VLAs (pi0, SmolVLA) that ACR-VLA corrects.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2023libero\"\n    title: \"LIBERO: Benchmarking Knowledge Transfer for Lifelong Robot Learning\"\n    authors: \"Liu et al.\"\n    year: 2023\n    venue: \"NeurIPS 2023\"\n    url: \"https://arxiv.org/abs/2306.03310\"\n    category: \"other\"\n    verified: true\n    relevance: \"Original LIBERO benchmark with 130 manipulation tasks. Base benchmark suite extended by LIBERO-Plus for ACR-VLA evaluation.\"\n    must_cite: false\n\n  - bibtex_key: \"liu2026ttvla\"\n    title: \"On-the-Fly VLA Adaptation via Test-Time Reinforcement Learning\"\n    authors: \"Liu et al.\"\n    year: 2026\n    venue: \"arXiv:2601.06748\"\n    url: \"https://arxiv.org/abs/2601.06748\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Test-time RL adaptation for VLAs using progress-based rewards. Alternative test-time approach requiring environment interaction, unlike ACR-VLA's zero-shot statistical correction.\"\n    must_cite: true\n\n  - bibtex_key: \"luan2026snapflow\"\n    title: \"SnapFlow: One-Step Action Generation for Flow-Matching VLAs via Progressive Self-Distillation\"\n    authors: \"Luan et al.\"\n    year: 2026\n    venue: \"arXiv:2604.05656\"\n    url: \"https://arxiv.org/abs/2604.05656\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Distills multi-step flow-matching VLA inference into single step. Complementary efficiency optimization; ACR-VLA's multi-sample approach trades compute for robustness.\"\n    must_cite: true\n\n  - bibtex_key: \"robustvla2025\"\n    title: \"RobustVLA: Robustness-Aware Reinforcement Post-Training for Vision-Language-Action Models\"\n    authors: \"Zhang et al.\"\n    year: 2025\n    venue: \"arXiv:2511.01331\"\n    url: \"https://arxiv.org/abs/2511.01331\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"RL post-training with Jacobian and smoothness regularization for VLA robustness. Training-time robustness method complementary to ACR-VLA's inference-time approach.\"\n    must_cite: true\n\n  - bibtex_key: \"romano2019cqr\"\n    title: \"Conformalized Quantile Regression\"\n    authors: \"Romano et al.\"\n    year: 2019\n    venue: \"NeurIPS 2019\"\n    url: \"https://arxiv.org/abs/1905.03222\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Combines conformal prediction with quantile regression for heteroscedastic coverage. Theoretical basis for ACR-VLA's per-DOF adaptive interval construction.\"\n    must_cite: false\n\n  - bibtex_key: \"shafer2008tutorial\"\n    title: \"A Tutorial on Conformal Prediction\"\n    authors: \"Shafer & Vovk\"\n    year: 2008\n    venue: \"Journal of Machine Learning Research, 9:371-421\"\n    url: \"https://jmlr.org/papers/v9/shafer08a.html\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Foundational conformal prediction tutorial establishing core theoretical framework used throughout ACR-VLA.\"\n    must_cite: false\n\n  - bibtex_key: \"shukor2025smolvla\"\n    title: \"SmolVLA: A Vision-Language-Action Model for Affordable and Efficient Robotics\"\n    authors: \"Shukor et al.\"\n    year: 2025\n    venue: \"arXiv:2506.01844\"\n    url: \"https://arxiv.org/abs/2506.01844\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"450M parameter flow-matching VLA with efficient architecture. Primary backbone VLA for ACR-VLA experiments.\"\n    must_cite: true\n\n  - bibtex_key: \"srpo2025\"\n    title: \"SRPO: Self-Referential Policy Optimization for Vision-Language-Action Models\"\n    authors: \"Fei et al.\"\n    year: 2025\n    venue: \"arXiv:2511.15605\"\n    url: \"https://arxiv.org/abs/2511.15605\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Self-referential RL fine-tuning achieving 82.1% on LIBERO-Plus. Key training-time baseline; ACR-VLA aims to complement such methods at inference time.\"\n    must_cite: true\n\n  - bibtex_key: \"wang2025cploop\"\n    title: \"Conformal Prediction in The Loop: A Feedback-Based Uncertainty Model for Trajectory Optimization\"\n    authors: \"Wang & Ning\"\n    year: 2025\n    venue: \"arXiv:2510.16376\"\n    url: \"https://arxiv.org/abs/2510.16376\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Feedback-based conformal prediction for trajectory optimization with coverage guarantees. Related CP-in-the-loop paradigm for robot planning.\"\n    must_cite: true\n\n  - bibtex_key: \"xing2026diu\"\n    title: \"Divergence is Uncertainty: A Closed-Form Posterior Covariance for Flow Matching\"\n    authors: \"Xing et al.\"\n    year: 2026\n    venue: \"arXiv:2605.00941\"\n    url: \"https://arxiv.org/abs/2605.00941\"\n    category: \"uq_flow_matching\"\n    verified: true\n    relevance: \"Single-pass uncertainty quantification for flow matching via velocity divergence. Enables efficient per-sample uncertainty estimation that ACR-VLA could leverage.\"\n    must_cite: true\n\n  - bibtex_key: \"yuan2026ups\"\n    title: \"When to Act, Ask, or Learn: Uncertainty-Aware Policy Steering\"\n    authors: \"Yuan et al.\"\n    year: 2026\n    venue: \"arXiv:2602.22474\"\n    url: \"https://arxiv.org/abs/2602.22474\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Uses conformal prediction to calibrate VLM+policy composition for strategy selection (act/ask/learn). Related CP-based policy gating approach.\"\n    must_cite: true\n\n  - bibtex_key: \"zhao2024conformalized\"\n    title: \"Conformalized Teleoperation: Confidently Mapping Human Inputs to High-Dimensional Robot Actions\"\n    authors: \"Zhao et al.\"\n    year: 2024\n    venue: \"RSS 2024\"\n    url: \"https://arxiv.org/abs/2406.07767\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Adaptive conformal prediction for uncertainty detection in assistive teleoperation. Demonstrates CP for high-DOF robot action spaces, directly relevant to ACR-VLA's per-DOF approach.\"\n    must_cite: true\n\n  - bibtex_key: \"cosmos_policy_2026\"\n    title: \"Cosmos Policy: Fine-Tuning Video Models for Visuomotor Control and Planning\"\n    authors: \"Kim et al.\"\n    year: 2026\n    venue: \"arXiv:2601.16163\"\n    url: \"https://arxiv.org/abs/2601.16163\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"NVIDIA's video-model-based robot policy achieving SOTA on LIBERO/RoboCasa. Represents the video foundation model approach to visuomotor control, contextualizing ACR-VLA's inference-time correction as model-agnostic.\"\n    must_cite: false\n\n  - bibtex_key: \"vla_gse_2026\"\n    title: \"VLA-GSE: Boosting Parameter-Efficient Fine-Tuning in VLA with Generalized and Specialized Experts\"\n    authors: \"Jiang et al.\"\n    year: 2026\n    venue: \"arXiv:2605.06175\"\n    url: \"https://arxiv.org/abs/2605.06175\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Parameter-efficient VLA fine-tuning with generalized/specialized experts achieving 81.2% on LIBERO-Plus. Training-time PEFT baseline complementary to ACR-VLA's inference-time approach.\"\n    must_cite: false\n\n  - bibtex_key: \"lakshminarayanan2017ensembles\"\n    title: \"Simple and Scalable Predictive Uncertainty Estimation using Deep Ensembles\"\n    authors: \"Lakshminarayanan et al.\"\n    year: 2017\n    venue: \"NeurIPS 2017\"\n    url: \"https://arxiv.org/abs/1612.01474\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Classic deep ensemble uncertainty estimation method. Key baseline for comparing ACR-VLA's multi-sample uncertainty quantification against ensemble-based approaches.\"\n    must_cite: false\n\n  - bibtex_key: \"gal2016dropout\"\n    title: \"Dropout as a Bayesian Approximation: Representing Model Uncertainty in Deep Learning\"\n    authors: \"Gal & Ghahramani\"\n    year: 2016\n    venue: \"ICML 2016\"\n    url: \"https://arxiv.org/abs/1506.02142\"\n    category: \"uq_foundation\"\n    verified: true\n    relevance: \"Foundational MC-dropout uncertainty estimation framework. Establishes the Bayesian dropout paradigm that ACR-VLA's multi-sample flow-matching approach extends to VLA action spaces.\"\n    must_cite: false\n\n  - bibtex_key: \"chi2023diffusion_policy\"\n    title: \"Diffusion Policy: Visuomotor Policy Learning via Action Diffusion\"\n    authors: \"Chi et al.\"\n    year: 2023\n    venue: \"RSS 2023 / IJRR 2024\"\n    url: \"https://arxiv.org/abs/2303.04137\"\n    category: \"vla_foundation\"\n    verified: false\n    verification_note: \"Well-known paper, needs URL reachability confirmation\"\n    relevance: \"Pioneering diffusion-based robot policy learning. Paradigm source for flow-matching VLAs; establishes the action generation framework that ACR-VLA's multi-sample inference exploits.\"\n    must_cite: true\n\n  # ===== New entries added 2026-05-14 =====\n\n  - bibtex_key: \"fan2025interpretable_mcp\"\n    title: \"Interpretable Multivariate Conformal Prediction with Fast Transductive Standardization\"\n    authors: \"Fan & Sesia\"\n    year: 2025\n    venue: \"arXiv:2512.15383\"\n    url: \"https://arxiv.org/abs/2512.15383\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Coordinate-wise standardization for tight simultaneous prediction intervals in multivariate CP. Directly relevant to ACR-VLA's per-DOF interval construction — provides alternative methodology for decoupling output correlations.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"klein2025otcp\"\n    title: \"Multivariate Conformal Prediction using Optimal Transport\"\n    authors: \"Klein, Bethune, Ndiaye & Cuturi\"\n    year: 2025\n    venue: \"arXiv:2502.03609\"\n    url: \"https://arxiv.org/abs/2502.03609\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"Uses optimal transport ordering for multivariate CP scoring, providing principled higher-dimensional quantiles. Alternative to CGS for constructing joint prediction sets over action spaces.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"zollo2025vla_calibration\"\n    title: \"Confidence Calibration in Vision-Language-Action Models\"\n    authors: \"Zollo & Zemel\"\n    year: 2025\n    venue: \"arXiv:2507.17383\"\n    url: \"https://arxiv.org/abs/2507.17383\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"First systematic study of confidence calibration in VLAs. Introduces prompt ensembles and action-wise Platt scaling. Establishes baseline calibration metrics that ACR-VLA's conformal approach should be compared against.\"\n    must_cite: true\n    relation: \"complementary\"\n\n  - bibtex_key: \"tang2026shifting_uncertainty\"\n    title: \"Shifting Uncertainty to Critical Moments: Towards Reliable Uncertainty Quantification for VLA Model\"\n    authors: \"Tang et al.\"\n    year: 2026\n    venue: \"arXiv:2603.18342\"\n    url: \"https://arxiv.org/abs/2603.18342\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Identifies the 'Averaging Trap' in VLA UQ where mean aggregation dilutes critical uncertainty spikes. Proposes max-based sliding window pooling. Relevant to ACR-VLA's per-timestep conformal monitoring.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lcp2025\"\n    title: \"Learnable Conformal Prediction with Context-Aware Nonconformity Functions for Robotic Planning and Perception\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2509.21955\"\n    url: \"https://arxiv.org/abs/2509.21955\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Replaces fixed CP nonconformity scores with learnable neural functions using geometric/semantic features. Improves path planning safety from 72% to 91%. Related context-aware CP approach for robotics.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"claps2025\"\n    title: \"Lies We Can Trust: Quantifying Action Uncertainty with Inaccurate Stochastic Dynamics through Conformalized Nonholonomic Lie Groups\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2512.10294\"\n    url: \"https://arxiv.org/abs/2512.10294\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Conformal Lie-group Action Prediction Sets (CLAPS) — extends CP from Euclidean to SE(2) configuration spaces for robot dynamics. Post-hoc calibration layer turning approximate covariances into provably calibrated ones.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"lucca2024\"\n    title: \"Quantifying Aleatoric and Epistemic Dynamics Uncertainty via Local Conformal Calibration\"\n    authors: \"Marques et al.\"\n    year: 2024\n    venue: \"arXiv:2409.08249\"\n    url: \"https://arxiv.org/abs/2409.08249\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Local conformal calibration in state-action space for dynamics models, producing probabilistically-valid prediction regions. Related local CP calibration concept applicable to per-DOF action uncertainty.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"sc_vla_2026\"\n    title: \"Self-Correcting VLA: Online Action Refinement via Sparse World Imagination\"\n    authors: \"Li et al.\"\n    year: 2026\n    venue: \"arXiv:2602.21633\"\n    url: \"https://arxiv.org/abs/2602.21633\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"Online action refinement using auxiliary predictive heads for sparse future state prediction + residual RL. Achieves 9% higher success rate than baselines. Directly comparable inference-time correction approach to ACR-VLA, but uses RL rather than statistical correction.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"vla_pilot_2025\"\n    title: \"Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"arXiv:2511.14178\"\n    url: \"https://arxiv.org/abs/2511.14178\"\n    category: \"inference_correction\"\n    verified: true\n    relevance: \"VLA-Pilot: zero-shot inference-time policy steering using MLLM verifier + evolutionary diffusion action optimizer on frozen VLA. Comparable plug-and-play inference-time approach, but requires MLLM verifier rather than statistical guarantees.\"\n    must_cite: true\n    relation: \"competitor\"\n\n  - bibtex_key: \"acot_vla_2026\"\n    title: \"ACoT-VLA: Action Chain-of-Thought for Vision-Language-Action Models\"\n    authors: \"AgibotTech\"\n    year: 2026\n    venue: \"CVPR 2026, arXiv:2601.11404\"\n    url: \"https://arxiv.org/abs/2601.11404\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"Action chain-of-thought with explicit/implicit action reasoners. Achieves 84.1% on LIBERO-Plus. Training-time reasoning approach; ACR-VLA's inference-time correction could complement ACoT's structured planning.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"gonzales2026crc_cbf\"\n    title: \"Safe Probabilistic Planning for Human-Robot Interaction using Conformal Risk Control\"\n    authors: \"Gonzales et al.\"\n    year: 2026\n    venue: \"IROS 2025, arXiv:2603.10392\"\n    url: \"https://arxiv.org/abs/2603.10392\"\n    category: \"cp_robotics\"\n    verified: true\n    relevance: \"Combines conformal risk control with control barrier functions for formal safety guarantees in HRI. Related conformal-based safety framework for robot control.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"safediffcon2025\"\n    title: \"From Uncertain to Safe: Conformal Adaptation of Diffusion Models for Safe PDE Control\"\n    authors: \"Not specified\"\n    year: 2025\n    venue: \"ICML 2025, arXiv:2502.02205\"\n    url: \"https://arxiv.org/abs/2502.02205\"\n    category: \"cp_foundation\"\n    verified: true\n    relevance: \"SafeDiffCon: uses conformal prediction uncertainty quantile to post-train and guide diffusion models for safe control. Demonstrates CP integration with diffusion-based generative control, conceptually parallel to ACR-VLA's CP+flow-matching approach.\"\n    must_cite: false\n    relation: \"background\"\n\n  - bibtex_key: \"afil2026\"\n    title: \"Failing Forward: Adaptive Failure-Informed Learning for Vision-Language-Action Models\"\n    authors: \"Not specified\"\n    year: 2026\n    venue: \"arXiv:2605.08434\"\n    url: \"https://arxiv.org/abs/2605.08434\"\n    category: \"vla_robustness_training\"\n    verified: true\n    relevance: \"AFIL framework using failure trajectories as negative guidance for diffusion/flow VLA policies. Steers action generation away from failure-prone regions during sampling. Complementary training-time approach to ACR-VLA's inference-time statistical correction.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"valle2025vla_uq_metrics\"\n    title: \"Evaluating Uncertainty and Quality of Visual Language Action-enabled Robots\"\n    authors: \"Valle et al.\"\n    year: 2025\n    venue: \"arXiv:2507.17049\"\n    url: \"https://arxiv.org/abs/2507.17049\"\n    category: \"uq_vla\"\n    verified: true\n    relevance: \"Proposes 8 uncertainty metrics and 5 quality metrics for VLA evaluation. Establishes evaluation methodology for VLA uncertainty that ACR-VLA's conformal guarantees should be validated against.\"\n    must_cite: false\n    relation: \"complementary\"\n\n  - bibtex_key: \"diffusionvla2024\"\n    title: \"Diffusion-VLA: Generalizable and Interpretable Robot Foundation Model via Self-Generated Reasoning\"\n    authors: \"Wen et al.\"\n    year: 2024\n    venue: \"ICML 2025, arXiv:2412.03293\"\n    url: \"https://arxiv.org/abs/2412.03293\"\n    category: \"vla_foundation\"\n    verified: true\n    relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"\n    must_cite: false\n    relation: \"background\"\n",
    "structuredPatch": [
      {
        "oldStart": 533,
        "oldLines": 3,
        "newStart": 533,
        "newLines": 115,
        "lines": [
          "     relevance: \"Combines autoregressive reasoning with diffusion action policies. 2B-72B parameter scaling. Representative hybrid VLA architecture that ACR-VLA's model-agnostic correction can wrap around.\"",
          "     must_cite: false",
          "     relation: \"background\"",
          "+",
          "+  # ===== Correction Magnitude Control literature (added 2026-05-14) =====",
          "+",
          "+  - bibtex_key: \"silver2018residual\"",
          "+    title: \"Residual Policy Learning\"",
          "+    authors: \"Silver et al.\"",
          "+    year: 2018",
          "+    venue: \"RSS 2018\"",
          "+    url: \"https://arxiv.org/abs/1812.06298\"",
          "+    category: \"residual_policy\"",
          "+    verified: true",
          "+    relevance: \"First residual policy framework: zero-init output layer + bounded action corrections on top of a base controller. Establishes the paradigm ACR-VLA's correction mechanism builds upon.\"",
          "+    must_cite: true",
          "+    relation: \"background\"",
          "+",
          "+  - bibtex_key: \"johannink2019residual\"",
          "+    title: \"Residual Reinforcement Learning for Robot Manipulator Control\"",
          "+    authors: \"Johannink et al.\"",
          "+    year: 2019",
          "+    venue: \"ICRA 2019\"",
          "+    url: \"https://arxiv.org/abs/1812.03201\"",
          "+    category: \"residual_policy\"",
          "+    verified: true",
          "+    relevance: \"Bounded residual tube with Lyapunov stability analysis for residual RL. Provides theoretical grounding for constraining correction magnitude to preserve base policy stability.\"",
          "+    must_cite: false",
          "+    relation: \"method-component\"",
          "+",
          "+  - bibtex_key: \"jiang2024transic\"",
          "+    title: \"TRANSIC: Sim-to-Real Policy Transfer via Online Correction Learning\"",
          "+    authors: \"Jiang et al.\"",
          "+    year: 2024",
          "+    venue: \"CoRL 2024\"",
          "+    url: \"https://arxiv.org/abs/2405.10315\"",
          "+    category: \"residual_policy\"",
          "+    verified: true",
          "+    relevance: \"Learned binary gate for residual corrections; demonstrates that ungated correction leads to model collapse. Motivates ACR-VLA's conformal gating mechanism.\"",
          "+    must_cite: true",
          "+    relation: \"direct-competitor\"",
          "+",
          "+  - bibtex_key: \"ankile2024resip\"",
          "+    title: \"ResiP: Residual Reinforcement Learning for Precise Assembly\"",
          "+    authors: \"Ankile et al.\"",
          "+    year: 2024",
          "+    venue: \"CoRL Workshop 2024\"",
          "+    url: \"\"",
          "+    category: \"residual_policy\"",
          "+    verified: false",
          "+    verification_note: \"Workshop paper, no arXiv ID provided\"",
          "+    relevance: \"Introduces scaling coefficient alpha<=1 for residual corrections, bounding correction magnitude as fraction of base action. Directly relevant to ACR-VLA's magnitude control design.\"",
          "+    must_cite: false",
          "+    relation: \"method-component\"",
          "+",
          "+  - bibtex_key: \"xiao2026pld\"",
          "+    title: \"PLD: Self-Improving Vision-Language-Action Model via Residual Reinforcement Learning\"",
          "+    authors: \"Xiao et al.\"",
          "+    year: 2026",
          "+    venue: \"ICLR 2026\"",
          "+    url: \"https://arxiv.org/abs/2511.00091\"",
          "+    category: \"residual_policy\"",
          "+    verified: true",
          "+    relevance: \"Scheduled magnitude bound xi for residual corrections on VLAs, validated on LIBERO. Closest residual RL + VLA method with explicit magnitude scheduling; key comparison for ACR-VLA.\"",
          "+    must_cite: true",
          "+    relation: \"direct-competitor\"",
          "+",
          "+  - bibtex_key: \"pan2025drc\"",
          "+    title: \"DRC: Decaying Relative Correction for Policy Refinement\"",
          "+    authors: \"Pan et al.\"",
          "+    year: 2025",
          "+    venue: \"arXiv:2503.15368\"",
          "+    url: \"https://arxiv.org/abs/2503.15368\"",
          "+    category: \"residual_policy\"",
          "+    verified: true",
          "+    relevance: \"Temporal decay of correction magnitude over episode progression. Relevant decay schedule design for ACR-VLA's adaptive correction bounds.\"",
          "+    must_cite: false",
          "+    relation: \"method-component\"",
          "+",
          "+  - bibtex_key: \"ma2026dawn\"",
          "+    title: \"DAWN: Value Learning in Residual Reinforcement Learning\"",
          "+    authors: \"Ma et al.\"",
          "+    year: 2026",
          "+    venue: \"arXiv:2602.10539\"",
          "+    url: \"https://arxiv.org/abs/2602.10539\"",
          "+    category: \"residual_policy\"",
          "+    verified: true",
          "+    relevance: \"Analyzes scale mismatch between base policy and residual correction in value estimation. Provides theoretical motivation for magnitude-aware correction design.\"",
          "+    must_cite: false",
          "+    relation: \"background\"",
          "+",
          "+  - bibtex_key: \"vla_in_the_loop_2025\"",
          "+    title: \"VLA-in-the-Loop: Event-Triggered Correction for Vision-Language-Action Models\"",
          "+    authors: \"Not specified\"",
          "+    year: 2025",
          "+    venue: \"arXiv 2025\"",
          "+    url: \"\"",
          "+    category: \"inference_correction\"",
          "+    verified: false",
          "+    verification_note: \"No arXiv ID provided, needs verification\"",
          "+    relevance: \"Event-triggered binary gate for VLA action correction. Related gating mechanism for deciding when to apply corrections, complementary to ACR-VLA's conformal trigger.\"",
          "+    must_cite: false",
          "+    relation: \"method-component\"",
          "+",
          "+  - bibtex_key: \"zhou2025acp_cbf\"",
          "+    title: \"Adaptive Conformal Prediction with Control Barrier Functions for Safe Reinforcement Learning\"",
          "+    authors: \"Zhou et al.\"",
          "+    year: 2025",
          "+    venue: \"ICRA 2025\"",
          "+    url: \"https://arxiv.org/abs/2503.17678\"",
          "+    category: \"cp_robotics\"",
          "+    verified: true",
          "+    relevance: \"Combines ACP uncertainty quantification with CBF action constraints for formal safety guarantees in RL. Directly relevant to ACR-VLA's conformal-based correction bounding mechanism.\"",
          "+    must_cite: true",
          "+    relation: \"method-component\""
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

_source line 18_

已添加 9 篇新论文（3 篇已存在跳过）：

**新增 residual_policy 类（6篇）：**
- `silver2018residual` — Residual Policy Learning (RSS 2018) ✓ must_cite
- `johannink2019residual` — Residual RL + Lyapunov stability (ICRA 2019)
- `jiang2024transic` — TRANSIC binary gate (CoRL 2024) ✓ must_cite
- `ankile2024resip` — ResiP α≤1 scaling (CoRL-W 2024, unverified)
- `xiao2026pld` — PLD scheduled ξ bound (ICLR 2026) ✓ must_cite
- `pan2025drc` — DRC temporal decay (arXiv 2025)
- `ma2026dawn` — DAWN scale mismatch analysis (arXiv 2026)

**新增 inference_correction 类（1篇）：**
- `vla_in_the_loop_2025` — event-triggered gate (unverified,无 arXiv ID)

**新增 cp_robotics 类（1篇）：**
- `zhou2025acp_cbf` — ACP+CBF safe RL (ICRA 2025) ✓ must_cite

**跳过已存在：** A2C2、SC-VLA、SafeDiffCon。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "type": "assistant",
  "parent_tool_use_id": null,
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "uuid": "e89774ce-0013-41b4-999a-06f9abe20895",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EBGdY5nYzfQY215f4PdoFR",
    "type": "message",
    "stop_reason": null,
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 2038,
      "cache_read_input_tokens": 45855,
      "cache_creation": {
        "ephemeral_5m_input_tokens": 0,
        "ephemeral_1h_input_tokens": 2038
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

_source line 19_

已添加 9 篇新论文（3 篇已存在跳过）：

**新增 residual_policy 类（6篇）：**
- `silver2018residual` — Residual Policy Learning (RSS 2018) ✓ must_cite
- `johannink2019residual` — Residual RL + Lyapunov stability (ICRA 2019)
- `jiang2024transic` — TRANSIC binary gate (CoRL 2024) ✓ must_cite
- `ankile2024resip` — ResiP α≤1 scaling (CoRL-W 2024, unverified)
- `xiao2026pld` — PLD scheduled ξ bound (ICLR 2026) ✓ must_cite
- `pan2025drc` — DRC temporal decay (arXiv 2025)
- `ma2026dawn` — DAWN scale mismatch analysis (arXiv 2026)

**新增 inference_correction 类（1篇）：**
- `vla_in_the_loop_2025` — event-triggered gate (unverified,无 arXiv ID)

**新增 cp_robotics 类（1篇）：**
- `zhou2025acp_cbf` — ACP+CBF safe RL (ICRA 2025) ✓ must_cite

**跳过已存在：** A2C2、SC-VLA、SafeDiffCon。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": null,
  "type": "result",
  "subtype": "success",
  "is_error": false,
  "api_error_status": null,
  "duration_ms": 94147,
  "duration_api_ms": 95155,
  "num_turns": 6,
  "stop_reason": "end_turn",
  "session_id": "f5591638-79a7-4297-b939-fc1ec363e285",
  "total_cost_usd": 0.45027449999999997,
  "usage": {
    "input_tokens": 9,
    "cache_creation_input_tokens": 36052,
    "cache_read_input_tokens": 176139,
    "output_tokens": 5412,
    "server_tool_use": {
      "web_search_requests": 0,
      "web_fetch_requests": 0
    },
    "service_tier": "standard",
    "cache_creation": {
      "ephemeral_1h_input_tokens": 36052,
      "ephemeral_5m_input_tokens": 0
    },
    "inference_geo": "",
    "iterations": [
      {
        "input_tokens": 1,
        "output_tokens": 376,
        "cache_read_input_tokens": 45855,
        "cache_creation_input_tokens": 2038,
        "cache_creation": {
          "ephemeral_5m_input_tokens": 0,
          "ephemeral_1h_input_tokens": 2038
        },
        "type": "message"
      }
    ],
    "speed": "standard"
  },
  "modelUsage": {
    "claude-haiku-4-5-20251001": {
      "inputTokens": 1455,
      "outputTokens": 16,
      "cacheReadInputTokens": 0,
      "cacheCreationInputTokens": 0,
      "webSearchRequests": 0,
      "costUSD": 0.001535,
      "contextWindow": 200000,
      "maxOutputTokens": 32000
    },
    "claude-opus-4-6": {
      "inputTokens": 9,
      "outputTokens": 5412,
      "cacheReadInputTokens": 176139,
      "cacheCreationInputTokens": 36052,
      "webSearchRequests": 0,
      "costUSD": 0.4487395,
      "contextWindow": 200000,
      "maxOutputTokens": 64000
    }
  },
  "permission_denials": [],
  "terminal_reason": "completed",
  "fast_mode_state": "off",
  "uuid": "012a6f34-d434-43bf-b949-ac2021034f6f"
}
```

</details>

---
